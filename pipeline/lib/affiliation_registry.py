"""Deterministic, offline affiliation-registry primitives.

The registry is a canonical JSON snapshot.  It deliberately treats imported group
labels as proposals: relationships enter the accepted graph only with official
evidence.  The public functions below are used by the audit CLI and later DB
projection code.
"""
from __future__ import annotations

import copy
import hashlib
import fcntl
import json
import os
import re
import unicodedata
import uuid
import threading
import time
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from contextlib import contextmanager
from pathlib import Path
from types import MappingProxyType
from typing import Any, Iterable, Mapping
from urllib.parse import urlsplit, urlunsplit

SOURCE_NAMESPACE = uuid.UUID("8d81aeb5-6231-5e97-8a65-cc9e5658bd22")
ZERO_DIGEST = "0" * 64
REGISTRY_SCHEMA_VERSION = "affiliation-2"
POLICY_VERSION = "official-relationships-v1"
SOURCE_SHA256 = "c6077715a3b14b7e0655da519be3bae39d03d9882addaea1899ef24d2ca3f72a"
OPERATOR_CURATED_APPROVER = "operator:jehyunlee"
OPERATOR_CURATED_RECORD_COUNT = 4747
OPERATOR_CURATED_CANONICAL_SHA256 = "3d439c95968232148ad1d2df933bc0c1b47e695462b682ae01393329c2fe858b"
HKUST_CANONICAL_SOURCE_KEY = "60008592"
HKUST_EXCLUDED_SOURCE_KEYS = frozenset({"60276981", "60112417", "60112621"})

GENERIC_GROUP_RE = re.compile(
    r"^(?:(?:faculty|school|college|department)(?:\s+of\b.*)?|"
    r"ministry(?:\s+of\s+education)?|university(?:\s+of\s+science\s+and\s+technology)?)$",
    re.IGNORECASE,
)
GENERIC_FRAGMENT_RE = re.compile(r"^(?:faculty|school|college|department)(?:\s+of\b.*)?$", re.IGNORECASE)
RELATIONSHIP_TYPES = frozenset({
    "part_of", "jointly_operated_by", "member_of", "network_member_of",
})
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
FROZEN_LEGACY_RELATIONSHIP_COUNT = 2245
FROZEN_LEGACY_RELATIONSHIP_SET_SHA256 = (
    "5f7a45272994384188ea9d516bac9b244feae3b18402bc73e6def00c57479738"
)
FROZEN_LEGACY_RELATIONSHIP_ID_SET_SHA256 = (
    "9f077283ca47393d284acc30420bf1a98e08a4d3f5774909a1091969b6a67cab"
)


class BibliographyWriterLockBusyError(RuntimeError):
    """Another process owns the bibliography database writer boundary."""

def bibliography_writer_lock_path(database: Path) -> Path:
    """Return the stable inode shared by every bibliography reader and writer."""
    return database.with_suffix(database.suffix + ".flock")


_LOCK_STATE: dict[int, str] = {}
_LOCK_STATE_GUARD = threading.Lock()


def _held_bibliography_locks() -> dict[int, str]:
    return _LOCK_STATE


def _acquire_bibliography_lock(database: Path, mode: str, *, timeout: float) -> int:
    """Acquire a process-death-releasing shared or exclusive POSIX advisory lock."""
    if mode not in {"reader", "writer"}:
        raise ValueError("bibliography lock mode must be reader or writer")
    path = bibliography_writer_lock_path(database)
    path.parent.mkdir(parents=True, exist_ok=True)
    key = str(path.resolve())
    held = _held_bibliography_locks()
    with _LOCK_STATE_GUARD:
        nested = key in held.values()
    if nested:
        message = f"bibliography {mode} lock busy: nested acquisition is forbidden"
        if mode == "writer":
            raise BibliographyWriterLockBusyError(message)
        raise RuntimeError(message)
    descriptor = os.open(path, os.O_CREAT | os.O_RDWR, 0o600)
    os.set_inheritable(descriptor, False)
    os.chmod(path, 0o600)
    operation = fcntl.LOCK_SH if mode == "reader" else fcntl.LOCK_EX
    deadline = time.monotonic() + timeout
    try:
        while True:
            try:
                fcntl.flock(descriptor, operation | fcntl.LOCK_NB)
                break
            except BlockingIOError as exc:
                if time.monotonic() >= deadline:
                    message = f"bibliography {mode} lock busy"
                    if mode == "writer":
                        raise BibliographyWriterLockBusyError(message) from exc
                    raise RuntimeError(message) from exc
                time.sleep(0.25)
        with _LOCK_STATE_GUARD:
            if key in held.values():
                fcntl.flock(descriptor, fcntl.LOCK_UN)
                message = f"bibliography {mode} lock busy: nested acquisition is forbidden"
                if mode == "writer":
                    raise BibliographyWriterLockBusyError(message)
                raise RuntimeError(message)
            held[descriptor] = key
        return descriptor
    except BaseException:
        os.close(descriptor)
        raise


def acquire_bibliography_writer_lock(database: Path, *, timeout: float = 120.0) -> int:
    """Acquire exclusive writer ownership without using pathname existence as authority."""
    return _acquire_bibliography_lock(database, "writer", timeout=timeout)


def acquire_bibliography_reader_lock(database: Path, *, timeout: float = 30.0) -> int:
    """Acquire shared reader ownership on the same stable inode as writers."""
    return _acquire_bibliography_lock(database, "reader", timeout=timeout)


def release_bibliography_lock(database: Path, descriptor: int) -> None:
    """Release a kernel-held bibliography lock; the stable pathname is never removed."""
    expected = str(bibliography_writer_lock_path(database).resolve())
    held = _held_bibliography_locks()
    with _LOCK_STATE_GUARD:
        owned = held.get(descriptor) == expected
    if not owned:
        raise RuntimeError("bibliography lock descriptor is not owned by this operation")
    try:
        fcntl.flock(descriptor, fcntl.LOCK_UN)
    finally:
        with _LOCK_STATE_GUARD:
            held.pop(descriptor, None)
        os.close(descriptor)


def release_bibliography_writer_lock(database: Path, descriptor: int) -> None:
    """Release a writer lock while preserving its stable inode."""
    release_bibliography_lock(database, descriptor)


def release_bibliography_reader_lock(database: Path, descriptor: int) -> None:
    """Release a reader lock while preserving its stable inode."""
    release_bibliography_lock(database, descriptor)


@contextmanager
def bibliography_lock(database: Path, mode: str, *, timeout: float | None = None):
    """Context manager for the one shared reader/writer coordination boundary."""
    if timeout is None:
        timeout = 30.0 if mode == "reader" else 120.0
    descriptor = _acquire_bibliography_lock(database, mode, timeout=timeout)
    try:
        yield descriptor
    finally:
        release_bibliography_lock(database, descriptor)


@contextmanager
def bibliography_reader_lock(database: Path):
    with bibliography_lock(database, "reader") as descriptor:
        yield descriptor


@contextmanager
def bibliography_writer_lock(database: Path):
    with bibliography_lock(database, "writer") as descriptor:
        yield descriptor

def nfc(value: str) -> str:
    """Return a Unicode-NFC string or reject non-string registry data."""
    if not isinstance(value, str):
        raise ValueError("registry strings must be strings")
    return unicodedata.normalize("NFC", value)


def canonical_json_bytes(value: Any) -> bytes:
    """Serialize JSON deterministically as UTF-8 NFC with one final newline."""
    def normalize(item: Any) -> Any:
        if isinstance(item, str):
            return nfc(item)
        if isinstance(item, list):
            return [normalize(member) for member in item]
        if isinstance(item, dict):
            return {nfc(str(key)): normalize(member) for key, member in item.items()}
        if item is None or isinstance(item, (bool, int, float)):
            return item
        raise ValueError(f"unsupported canonical JSON value: {type(item)!r}")
    return (json.dumps(normalize(value), ensure_ascii=False, sort_keys=True,
                       separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")


def canonical_sha256(value: Any) -> str:
    """Return the SHA-256 of canonical JSON bytes."""
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()
# These contracts intentionally do not track the SQLite projection contract.
REGISTRY_CONTRACT_VERSION = "affiliation-registry-3"
EVENT_CONTRACT_VERSION = "affiliation-event-3"
COUNTRY_MAP_VERSION = "iso-3166-1-2020/debian-iso-codes-4.18.0-1"
ISO_COUNTRY_SOURCE = MappingProxyType({
    "standard": "ISO 3166-1:2020",
    "upstream_version": "4.18.0",
    "upstream_release_date": "2025-04-11",
    "debian_source_version": "4.18.0-1",
    "path": "data/iso_3166-1.json",
    "url": "https://sources.debian.org/data/main/i/iso-codes/4.18.0-1/data/iso_3166-1.json",
    "upstream_repository": "https://salsa.debian.org/iso-codes-team/iso-codes",
    "license": "LGPL-2.1-or-later",
    "raw_sha256": "f01b812b57fba9f31ff621bf33e7c7570a01964dbeb5be2167e94decf538c89f",
})
# The tuples are deliberately tracked rather than derived from the host locale.
# Each row is (current alpha-2, current alpha-3, English short name), alpha-2 sorted.
_ISO_3166_1_DATA = """AD AND Andorra
AE ARE United Arab Emirates
AF AFG Afghanistan
AG ATG Antigua and Barbuda
AI AIA Anguilla
AL ALB Albania
AM ARM Armenia
AO AGO Angola
AQ ATA Antarctica
AR ARG Argentina
AS ASM American Samoa
AT AUT Austria
AU AUS Australia
AW ABW Aruba
AX ALA Åland Islands
AZ AZE Azerbaijan
BA BIH Bosnia and Herzegovina
BB BRB Barbados
BD BGD Bangladesh
BE BEL Belgium
BF BFA Burkina Faso
BG BGR Bulgaria
BH BHR Bahrain
BI BDI Burundi
BJ BEN Benin
BL BLM Saint Barthélemy
BM BMU Bermuda
BN BRN Brunei Darussalam
BO BOL Bolivia, Plurinational State of
BQ BES Bonaire, Sint Eustatius and Saba
BR BRA Brazil
BS BHS Bahamas
BT BTN Bhutan
BV BVT Bouvet Island
BW BWA Botswana
BY BLR Belarus
BZ BLZ Belize
CA CAN Canada
CC CCK Cocos (Keeling) Islands
CD COD Congo, The Democratic Republic of the
CF CAF Central African Republic
CG COG Congo
CH CHE Switzerland
CI CIV Côte d'Ivoire
CK COK Cook Islands
CL CHL Chile
CM CMR Cameroon
CN CHN China
CO COL Colombia
CR CRI Costa Rica
CU CUB Cuba
CV CPV Cabo Verde
CW CUW Curaçao
CX CXR Christmas Island
CY CYP Cyprus
CZ CZE Czechia
DE DEU Germany
DJ DJI Djibouti
DK DNK Denmark
DM DMA Dominica
DO DOM Dominican Republic
DZ DZA Algeria
EC ECU Ecuador
EE EST Estonia
EG EGY Egypt
EH ESH Western Sahara
ER ERI Eritrea
ES ESP Spain
ET ETH Ethiopia
FI FIN Finland
FJ FJI Fiji
FK FLK Falkland Islands (Malvinas)
FM FSM Micronesia, Federated States of
FO FRO Faroe Islands
FR FRA France
GA GAB Gabon
GB GBR United Kingdom
GD GRD Grenada
GE GEO Georgia
GF GUF French Guiana
GG GGY Guernsey
GH GHA Ghana
GI GIB Gibraltar
GL GRL Greenland
GM GMB Gambia
GN GIN Guinea
GP GLP Guadeloupe
GQ GNQ Equatorial Guinea
GR GRC Greece
GS SGS South Georgia and the South Sandwich Islands
GT GTM Guatemala
GU GUM Guam
GW GNB Guinea-Bissau
GY GUY Guyana
HK HKG Hong Kong
HM HMD Heard Island and McDonald Islands
HN HND Honduras
HR HRV Croatia
HT HTI Haiti
HU HUN Hungary
ID IDN Indonesia
IE IRL Ireland
IL ISR Israel
IM IMN Isle of Man
IN IND India
IO IOT British Indian Ocean Territory
IQ IRQ Iraq
IR IRN Iran, Islamic Republic of
IS ISL Iceland
IT ITA Italy
JE JEY Jersey
JM JAM Jamaica
JO JOR Jordan
JP JPN Japan
KE KEN Kenya
KG KGZ Kyrgyzstan
KH KHM Cambodia
KI KIR Kiribati
KM COM Comoros
KN KNA Saint Kitts and Nevis
KP PRK Korea, Democratic People's Republic of
KR KOR Korea, Republic of
KW KWT Kuwait
KY CYM Cayman Islands
KZ KAZ Kazakhstan
LA LAO Lao People's Democratic Republic
LB LBN Lebanon
LC LCA Saint Lucia
LI LIE Liechtenstein
LK LKA Sri Lanka
LR LBR Liberia
LS LSO Lesotho
LT LTU Lithuania
LU LUX Luxembourg
LV LVA Latvia
LY LBY Libya
MA MAR Morocco
MC MCO Monaco
MD MDA Moldova, Republic of
ME MNE Montenegro
MF MAF Saint Martin (French part)
MG MDG Madagascar
MH MHL Marshall Islands
MK MKD North Macedonia
ML MLI Mali
MM MMR Myanmar
MN MNG Mongolia
MO MAC Macao
MP MNP Northern Mariana Islands
MQ MTQ Martinique
MR MRT Mauritania
MS MSR Montserrat
MT MLT Malta
MU MUS Mauritius
MV MDV Maldives
MW MWI Malawi
MX MEX Mexico
MY MYS Malaysia
MZ MOZ Mozambique
NA NAM Namibia
NC NCL New Caledonia
NE NER Niger
NF NFK Norfolk Island
NG NGA Nigeria
NI NIC Nicaragua
NL NLD Netherlands
NO NOR Norway
NP NPL Nepal
NR NRU Nauru
NU NIU Niue
NZ NZL New Zealand
OM OMN Oman
PA PAN Panama
PE PER Peru
PF PYF French Polynesia
PG PNG Papua New Guinea
PH PHL Philippines
PK PAK Pakistan
PL POL Poland
PM SPM Saint Pierre and Miquelon
PN PCN Pitcairn
PR PRI Puerto Rico
PS PSE Palestine, State of
PT PRT Portugal
PW PLW Palau
PY PRY Paraguay
QA QAT Qatar
RE REU Réunion
RO ROU Romania
RS SRB Serbia
RU RUS Russian Federation
RW RWA Rwanda
SA SAU Saudi Arabia
SB SLB Solomon Islands
SC SYC Seychelles
SD SDN Sudan
SE SWE Sweden
SG SGP Singapore
SH SHN Saint Helena, Ascension and Tristan da Cunha
SI SVN Slovenia
SJ SJM Svalbard and Jan Mayen
SK SVK Slovakia
SL SLE Sierra Leone
SM SMR San Marino
SN SEN Senegal
SO SOM Somalia
SR SUR Suriname
SS SSD South Sudan
ST STP Sao Tome and Principe
SV SLV El Salvador
SX SXM Sint Maarten (Dutch part)
SY SYR Syrian Arab Republic
SZ SWZ Eswatini
TC TCA Turks and Caicos Islands
TD TCD Chad
TF ATF French Southern Territories
TG TGO Togo
TH THA Thailand
TJ TJK Tajikistan
TK TKL Tokelau
TL TLS Timor-Leste
TM TKM Turkmenistan
TN TUN Tunisia
TO TON Tonga
TR TUR Türkiye
TT TTO Trinidad and Tobago
TV TUV Tuvalu
TW TWN Taiwan, Province of China
TZ TZA Tanzania, United Republic of
UA UKR Ukraine
UG UGA Uganda
UM UMI United States Minor Outlying Islands
US USA United States
UY URY Uruguay
UZ UZB Uzbekistan
VA VAT Holy See (Vatican City State)
VC VCT Saint Vincent and the Grenadines
VE VEN Venezuela, Bolivarian Republic of
VG VGB Virgin Islands, British
VI VIR Virgin Islands, U.S.
VN VNM Viet Nam
VU VUT Vanuatu
WF WLF Wallis and Futuna
WS WSM Samoa
YE YEM Yemen
YT MYT Mayotte
ZA ZAF South Africa
ZM ZMB Zambia
ZW ZWE Zimbabwe"""
ISO_3166_1_ROWS = tuple(
    (parts[0], parts[1], parts[2])
    for parts in (row.split(" ", 2) for row in _ISO_3166_1_DATA.splitlines())
)
LEGACY_COUNTRY_ALIASES = (
    ("Bolivia", "BO"), ("Brunei", "BN"), ("Britain", "GB"), ("Cape Verde", "CV"),
    ("China", "CN"), ("Czech Republic", "CZ"), ("Democratic People's Republic of Korea", "KP"),
    ("East Timor", "TL"), ("FYROM", "MK"), ("Great Britain", "GB"), ("Hong Kong", "HK"),
    ("Iran", "IR"), ("Ivory Coast", "CI"), ("Korea North", "KP"), ("Korea South", "KR"),
    ("Korea, North", "KP"), ("Korea, South", "KR"), ("Laos", "LA"), ("Macao", "MO"),
    ("Macedonia", "MK"), ("Macau", "MO"), ("Moldova", "MD"), ("North Korea", "KP"),
    ("Palestine", "PS"), ("Palestinian Territories", "PS"), ("Republic of Korea", "KR"),
    ("Russia", "RU"),
    ("South Korea", "KR"), ("Swaziland", "SZ"), ("Syria", "SY"), ("Taiwan", "TW"),
    ("Tanzania", "TZ"), ("Turkey", "TR"), ("U.K.", "GB"), ("U.S.", "US"),
    ("U.S.A.", "US"), ("UK", "GB"), ("USA", "US"), ("United Kingdom", "GB"),
    ("United States", "US"), ("United States of America", "US"), ("Venezuela", "VE"),
    ("Vietnam", "VN"),
)
_COUNTRY_LOOKUP = {
    " ".join(nfc(value).casefold().split()): alpha2
    for alpha2, alpha3, name in ISO_3166_1_ROWS
    for value in (alpha2, alpha3, name)
}
_COUNTRY_LOOKUP.update({
    " ".join(nfc(name).casefold().split()): code for name, code in LEGACY_COUNTRY_ALIASES
})
_COUNTRY_MAP_PAYLOAD = {
    "source": dict(ISO_COUNTRY_SOURCE),
    "rows": [list(row) for row in ISO_3166_1_ROWS],
    "aliases": [list(alias) for alias in LEGACY_COUNTRY_ALIASES],
    "normalization_version": "nfc-trim-collapse-casefold-v1",
    "territory_policy": "current ISO-assigned territories remain distinct site codes",
    "non_iso_policy": "numeric, historical, user-assigned, and unlisted values are unmappable",
}
EXPECTED_COUNTRY_MAP_SHA256 = "079e9037803744d92198452b06ae230ba8952ea6e592b666dbb81206247278e3"
COUNTRY_MAP_SHA256 = canonical_sha256(_COUNTRY_MAP_PAYLOAD)
if COUNTRY_MAP_SHA256 != EXPECTED_COUNTRY_MAP_SHA256:
    raise RuntimeError("embedded country map digest does not match the country map")
EVIDENCE_ORACLE_VERSION = "affiliation-oracle-v1"
EVIDENCE_ORACLE_MANIFEST = MappingProxyType({
    "version": EVIDENCE_ORACLE_VERSION,
    "parser_extractor_version": "affiliation-evidence-parser-v2",
    "ror": {
        "endpoint": "https://api.ror.org/v2/organizations",
        "schema_version": "2.1",
        "schema_commit": "20ec1cf1edc3e0051de0ea2eae2bfdf536b9ba63",
        "schema_sha256": "5df548a5f7a927fc9e94f196d2c3e78c96c25343909999dfda5110b535e2ddf7",
        "schema_path": "ror-schema/20ec1cf1edc3e0051de0ea2eae2bfdf536b9ba63/ror_schema_v2_1.json",
        "schema_url": "https://raw.githubusercontent.com/ror-community/ror-schema/20ec1cf1edc3e0051de0ea2eae2bfdf536b9ba63/ror_schema_v2_1.json",
        "connect_timeout_seconds": 5,
        "read_idle_timeout_seconds": 15,
        "total_timeout_seconds": 30,
        "wire_bytes_per_page": 2097152,
        "decoded_bytes_per_page": 8388608,
        "max_pages": 10,
        "max_records": 200,
    },
    "psl": {
        "version": "2026-07-25_14-20-03_UTC",
        "commit": "e1b8015c3b2f0f4f8c18659c2480fc1a22c07b20",
        "sha256": "fe6adc7fb8014f57d28d69b18d0aa3e581efb432544922e12131a5d4a87bd954",
        "path": "psl/2026-07-25_14-20-03_UTC-e1b8015/public_suffix_list.dat",
        "url": "https://raw.githubusercontent.com/publicsuffix/list/e1b8015c3b2f0f4f8c18659c2480fc1a22c07b20/public_suffix_list.dat",
        "license": "MPL-2.0",
        "sections": ["ICANN", "PRIVATE"],
    },
    "official_https": {
        "connect_timeout_seconds": 5,
        "read_idle_timeout_seconds": 10,
        "total_timeout_seconds": 30,
        "max_redirects": 3,
        "wire_bytes_per_response": 1048576,
        "wire_bytes_per_chain": 2097152,
        "decoded_bytes_per_response": 4194304,
        "decoded_bytes_per_chain": 8388608,
        "quote_bytes": 512,
        "total_quote_bytes": 2048,
        "accepted_content_encodings": ["identity", "gzip"],
        "accepted_media_types": [
            "application/ld+json", "application/xhtml+xml", "text/html",
        ],
        "accepted_charsets": ["iso-8859-1", "utf-8", "windows-1252"],
    },
    "country": {
        "version": COUNTRY_MAP_VERSION,
        "sha256": COUNTRY_MAP_SHA256,
        "source_sha256": ISO_COUNTRY_SOURCE["raw_sha256"],
    },
    "retrieved_at": "2026-08-08T00:00:00Z",
})
EVIDENCE_ORACLE_SHA256 = canonical_sha256(dict(EVIDENCE_ORACLE_MANIFEST))


def stable_json_sha256(value: Any) -> str:
    """Public name for canonical JSON hashes used by evidence and decisions."""
    return canonical_sha256(value)


def country_resolution(value: str | None, *, country_scope: str | None = None) -> tuple[str, str | None]:
    """Return an explicit country state: present, missing, unmappable, or multinational."""
    if country_scope == "multinational":
        return "multinational", None
    if value is None:
        return "missing", None
    if not isinstance(value, str):
        return "unmappable", None
    if not nfc(value).strip():
        return "missing", None
    code = _COUNTRY_LOOKUP.get(" ".join(nfc(value).casefold().split()))
    return ("present", code) if code else ("unmappable", None)


def canonical_country(value: str | None, *, country_scope: str | None = None) -> str | None:
    """Return a current ISO alpha-2 code; missing, unmappable, and multinational have no code."""
    return country_resolution(value, country_scope=country_scope)[1]


canonicalize_country = canonical_country


def organization_identity_key(name: str, country: str | None, *,
                              country_scope: str | None = None) -> tuple[str, str] | None:
    """Pinned exact key; a name without a present site country is never mergeable."""
    code = canonical_country(country, country_scope=country_scope)
    normalized = normalize_name(name)
    return (normalized, code) if normalized and code else None


def normalize_ror_id(value: str) -> str:
    """Normalize only the ROR v2 identifier representation."""
    if not isinstance(value, str):
        raise ValueError("ROR ID must be a string")
    identifier = value.strip()
    if re.fullmatch(r"0[a-hj-km-np-tv-z0-9]{7}[0-9]", identifier):
        identifier = f"https://ror.org/{identifier}"
    if not re.fullmatch(r"https://ror\.org/0[a-hj-km-np-tv-z0-9]{7}[0-9]", identifier):
        raise ValueError("malformed ROR v2 ID")
    return identifier


def normalize_website_url(value: str) -> str:
    """Normalize a typed ROR website without accepting credentials, fragments, or HTTP."""
    if not isinstance(value, str):
        raise ValueError("website URL must be a string")
    try:
        parts = urlsplit(value.strip())
        port_value = parts.port
    except ValueError as exc:
        raise ValueError("malformed website URL") from exc
    if parts.scheme != "https" or not parts.hostname or parts.username or parts.password or parts.fragment:
        raise ValueError("website must be a credential-free HTTPS URL")
    host = parts.hostname.encode("idna").decode("ascii").lower()
    port = f":{port_value}" if port_value and port_value != 443 else ""
    return urlunsplit(("https", host + port, parts.path or "/", parts.query, ""))


def ror_v2_website_links(record: Mapping[str, Any]) -> tuple[str, ...]:
    """Extract only explicit ROR v2 `website` links; untyped links are non-authoritative."""
    links = record.get("links", [])
    if not isinstance(links, list):
        return ()
    values = []
    for link in links:
        if not isinstance(link, Mapping) or link.get("type") != "website":
            continue
        value = link.get("value")
        if isinstance(value, str):
            try:
                values.append(normalize_website_url(value))
            except ValueError:
                continue
    return tuple(sorted(set(values)))


def normalize_name(name: str) -> str:
    """NFC/casefold whitespace normalization for lookup only, never identity."""
    return " ".join(nfc(name).casefold().split())


def _id(kind: str, source_sha256: str, key: str) -> str:
    return str(uuid.uuid5(SOURCE_NAMESPACE, f"{kind}:{source_sha256}:{key}"))


def _event_digest(event: Mapping[str, Any]) -> str:
    body = dict(event)
    body.pop("digest", None)
    return canonical_sha256(body)


def _country(record: Mapping[str, Any]) -> str:
    values = record.get("af_country", [])
    return nfc(values[0]) if isinstance(values, list) and values else ""


def _name(record: Mapping[str, Any]) -> str:
    values = record.get("af_name", [])
    return nfc(values[0]) if isinstance(values, list) and values else ""


def _groups(record: Mapping[str, Any]) -> list[str]:
    values = record.get("af_groupname", [])
    return [nfc(value) for value in values if isinstance(value, str) and value.strip()]


def _issue_codes(key: str, record: Mapping[str, Any]) -> list[str]:
    group = " | ".join(_groups(record))
    codes: list[str] = []
    if key == "60029470" or group.casefold() == "criso":
        codes.append("group_label_typo_criso")
    if key == "60008592" or group.casefold() == "hkust":
        codes.append("group_label_abbreviation_hkust")
    if key == "60029832" or ("csic" in group.casefold() and "sevilla" in group.casefold()):
        codes.append("flattened_multi_parent_group")
    if key == "60002970":
        codes.append("unsupported_hec_montreal_parent")
    if any(GENERIC_GROUP_RE.match(value.strip()) for value in _groups(record)):
        codes.append("generic_group_label_untrusted")
    return sorted(set(codes))
def _replacement_tokens(key: str, record: Mapping[str, Any], source_keys: set[str]) -> list[dict[str, str]]:
    """Classify every legacy replacement token without inferring a relationship."""
    seen: set[str] = set()
    tokens: list[dict[str, str]] = []
    for raw in record.get("af_id_replace", []):
        token = nfc(str(raw))
        if token in seen:
            category = "duplicate within record"
        elif token == key:
            category = "self"
        elif token in source_keys:
            category = "alias target"
        else:
            category = "missing target"
        seen.add(token)
        tokens.append({"token": token, "category": category})
    return tokens




def _organization(key: str, record: Mapping[str, Any], source_sha256: str,
                  canonical_aliases: Mapping[str, str], *, status: str = "proposed") -> dict[str, Any]:
    source_name = _name(record) or f"Unspecified affiliation {key}"
    name = nfc(canonical_aliases.get(source_name, source_name))
    organization_id = _id("source", source_sha256, key)
    aliases = sorted({source_name, name, *[x for x in record.get("af_abbgroupname", []) if isinstance(x, str)]},
                     key=lambda alias: (normalize_name(alias), _country(record), organization_id,
                                        _id("alias", source_sha256, key + ":" + alias)))
    return {
        "organization_id": organization_id,
        "canonical_name_en": name,
        "normalized_name": normalize_name(name),
        "country": _country(record),
        "organization_type": "other",
        "status": status,
        "identifiers": [{"authority": "source_af_id", "value": key}],
        "aliases": [{"alias_id": _id("alias", source_sha256, key + ":" + alias),
                     "name": alias, "normalized_alias": normalize_name(alias),
                     "country_discriminator": _country(record)} for alias in aliases],
    }


def _group_organization(group: str, country: str, source_sha256: str, *,
                        status: str = "proposed") -> dict[str, Any]:
    """Create a deterministic group identity without inferring source identity."""
    normalized = normalize_name(group)
    organization_id = _id("group", source_sha256, f"{country}:{normalized}")
    alias_id = _id("group-alias", source_sha256, f"{country}:{normalized}")
    return {
        "organization_id": organization_id,
        "canonical_name_en": group,
        "normalized_name": normalized,
        "country": country,
        "organization_type": "other",
        "status": status,
        "identifiers": [],
        "aliases": [{"alias_id": alias_id, "name": group, "normalized_alias": normalized,
                     "country_discriminator": country}],
    }


def _proposal_is_forbidden(group: str, issues: list[str]) -> bool:
    return bool(issues) or bool(GENERIC_GROUP_RE.match(group.strip()))


def _identity_candidates(organizations: Iterable[Mapping[str, Any]]) -> list[dict[str, Any]]:
    """Return explicit, collision-preserving reviewed identity aliases."""
    candidates = []
    for organization in organizations:
        if organization.get("status") != "active":
            continue
        for alias in organization["aliases"]:
            candidates.append({
                "alias_id": alias["alias_id"],
                "organization_id": organization["organization_id"],
                "normalized_alias": alias["normalized_alias"],
                "country_discriminator": alias["country_discriminator"],
                "name": alias["name"],
                "status": "accepted_identity",
                "provenance": organization.get("identity_provenance", "reviewed_identity"),
            })
    return sorted(candidates, key=lambda item: (item["normalized_alias"], item["country_discriminator"],
                                                  item["organization_id"], item["alias_id"]))



def _corrected_groups(key: str, record: Mapping[str, Any], issues: list[str], *,
                      curated: bool = False) -> list[str]:
    """Return audited labels; never derive a parent from a substring match."""
    groups = _groups(record)
    if curated and key in HKUST_EXCLUDED_SOURCE_KEYS:
        return []
    if "group_label_typo_criso" in issues:
        return ["Commonwealth Scientific and Industrial Research Organisation (CSIRO)"]
    if "group_label_abbreviation_hkust" in issues:
        return ["Hong Kong University of Science and Technology"]
    if "flattened_multi_parent_group" in issues:
        return ["Spanish National Research Council (CSIC)", "University of Seville"]
    if "unsupported_hec_montreal_parent" in issues:
        return [group for group in groups
                if normalize_name(group) != normalize_name(
                    "University of Montreal" if curated else "HEC Montréal")]
    return [group for group in groups if not GENERIC_GROUP_RE.match(group.strip())]


def _after(key: str, record: Mapping[str, Any], organization: Mapping[str, Any], issues: list[str],
           *, curated: bool = False, relationship_ids: list[str] | None = None) -> dict[str, Any]:
    groups = _corrected_groups(key, record, issues, curated=curated)
    return {
        "organization_id": organization["organization_id"],
        "canonical_name_en": organization["canonical_name_en"],
        "country": organization["country"],
        "accepted_relationship_ids": relationship_ids or [],
        "proposed_group_labels": groups,
        "resolution": "operator_curated_hierarchy" if curated else "standalone_pending_official_evidence",
    }


def build_registry(source: Mapping[str, Any], *, source_sha256: str = SOURCE_SHA256,
                   timestamp: str = "1970-01-01T00:00:00Z", version: int = 1,
                   canonical_aliases: Mapping[str, str] | None = None,
                   operator_curated: bool = False,
                   _validate_result: bool = True) -> dict[str, Any]:
    """Build source proposals or the explicitly pinned operator-curated baseline."""
    if not isinstance(source, Mapping):
        raise ValueError("source must be an object keyed by source affiliation ID")
    if operator_curated and (
            source_sha256 != SOURCE_SHA256
            or len(source) != OPERATOR_CURATED_RECORD_COUNT
            or canonical_sha256(source) != OPERATOR_CURATED_CANONICAL_SHA256):
        raise ValueError("operator-curated import requires the pinned 4,747-record source")
    if operator_curated and canonical_aliases:
        raise ValueError("operator-curated import forbids unpinned canonical aliases")
    source_records: dict[str, Mapping[str, Any]] = {}
    for raw_key, record in source.items():
        key = nfc(str(raw_key))
        if key in source_records or not isinstance(record, Mapping):
            raise ValueError(f"source record {raw_key!r} is not an object")
        source_records[key] = record
    source_keys = set(source_records)
    canonical_aliases = canonical_aliases or {}
    organizations: list[dict[str, Any]] = []
    organization_by_source: dict[str, dict[str, Any]] = {}
    root_key_by_source: dict[str, str] = {}
    if operator_curated:
        resolving: set[str] = set()

        def resolve_root(key: str) -> str:
            if key in root_key_by_source:
                return root_key_by_source[key]
            if key in resolving:
                raise ValueError(f"cyclic af_id_replace target for {key}")
            resolving.add(key)
            targets = {token["token"] for token in _replacement_tokens(
                key, source_records[key], source_keys)
                if token["category"] == "alias target"}
            invalid = [token for token in _replacement_tokens(key, source_records[key], source_keys)
                       if token["category"] == "missing target"]
            if invalid:
                raise ValueError(f"missing af_id_replace target for {key}")
            if len(targets) > 1:
                raise ValueError(f"conflicting af_id_replace targets for {key}")
            root = resolve_root(next(iter(targets))) if targets else key
            resolving.remove(key)
            root_key_by_source[key] = root
            return root

        for key in sorted(source_records):
            resolve_root(key)
        for root in sorted(set(root_key_by_source.values())):
            organization = _organization(root, source_records[root], source_sha256, canonical_aliases,
                                         status="active")
            organization["identity_provenance"] = "operator_curated"
            identifiers = []
            aliases = []
            for key in sorted(key for key, value in root_key_by_source.items() if value == root):
                record = source_records[key]
                identifiers.append({"authority": "source_af_id", "value": key})
                names = {_name(record) or f"Unspecified affiliation {key}",
                         nfc(canonical_aliases.get(
                             _name(record) or f"Unspecified affiliation {key}",
                             _name(record) or f"Unspecified affiliation {key}")),
                         *[nfc(value) for value in record.get("af_abbgroupname", [])
                           if isinstance(value, str)]}
                for name in names:
                    aliases.append({
                        "alias_id": _id("alias", source_sha256, key + ":" + name),
                        "name": name, "normalized_alias": normalize_name(name),
                        "country_discriminator": _country(record),
                    })
            organization["identifiers"] = identifiers
            organization["aliases"] = sorted(aliases, key=lambda alias: (
                alias["normalized_alias"], alias["country_discriminator"], alias["alias_id"]))
            organizations.append(organization)
            for key, value in root_key_by_source.items():
                if value == root:
                    organization_by_source[key] = organization
    else:
        for key in sorted(source_records):
            organization = _organization(key, source_records[key], source_sha256, canonical_aliases)
            organizations.append(organization)
            organization_by_source[key] = organization
            root_key_by_source[key] = key
    by_identity: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for organization in organizations:
        by_identity.setdefault(
            (organization["normalized_name"], organization["country"]), []).append(organization)
    group_organizations: dict[str, dict[str, Any]] = {}
    corrections: list[dict[str, Any]] = []
    evidence: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    proposals: list[dict[str, Any]] = []
    relationships_by_edge: dict[tuple[str, str, str], dict[str, Any]] = {}


    for key in sorted(source_records):
        organization = organization_by_source[key]
        record = source_records[key]
        issues = _issue_codes(key, record)
        source_aliases = {alias["normalized_alias"] for alias in organization["aliases"]}
        groups_for_mode = (_corrected_groups(key, record, issues, curated=True)
                           if operator_curated else _groups(record))
        relationship_ids: list[str] = []
        proposal_ids: list[str] = []
        proposed_groups: list[str] = []
        for group in sorted(set(groups_for_mode), key=lambda value: (normalize_name(value), value)):
            if not operator_curated and (
                    normalize_name(group) in source_aliases or _proposal_is_forbidden(group, issues)):
                continue
            target = None
            if (operator_curated and "group_label_abbreviation_hkust" in issues
                    and key not in HKUST_EXCLUDED_SOURCE_KEYS):
                target = organization_by_source.get(HKUST_CANONICAL_SOURCE_KEY)
                if target is None:
                    raise ValueError("HKUST curated target is missing")
            if target is None:
                matches = by_identity.get((normalize_name(group), organization["country"]), [])
                target = matches[0] if len(matches) == 1 else None
            if target is None:
                candidate = _group_organization(
                    group, organization["country"], source_sha256,
                    status="active" if operator_curated else "proposed")
                if operator_curated:
                    candidate["identity_provenance"] = "operator_curated"
                target = group_organizations.setdefault(candidate["organization_id"], candidate)
            if target["organization_id"] == organization["organization_id"]:
                continue
            evidence_id = _id("source-evidence", source_sha256, f"{key}:{normalize_name(group)}")
            edge_key = (organization["organization_id"], target["organization_id"], "part_of")
            relationship_id = (_id("relationship", source_sha256, ":".join(edge_key))
                               if operator_curated else
                               _id("relationship", source_sha256, f"{key}:{normalize_name(group)}"))
            if operator_curated:
                payload = {
                    "import_mode": "pinned_operator_curated",
                    "source_sha256": source_sha256, "source_key": key,
                    "original_group_labels": _groups(record),
                    "corrected_group_label": group, "issue_codes": issues,
                }
                evidence.append({
                    "evidence_id": evidence_id, "authority": "operator_curated",
                    "status": "accepted", "review_status": "approved",
                    "approved_by": [OPERATOR_CURATED_APPROVER], "quote": group,
                    "cross_border_explicit": _country(record) != target["country"],
                    "payload": payload, "payload_sha256": canonical_sha256(payload),
                    "quote_sha256": canonical_sha256(group),
                })
                relationship = relationships_by_edge.get(edge_key)
                if relationship is None:
                    relationship = {
                        "relationship_id": relationship_id, "relationship_type": "part_of",
                        "subject_organization_id": organization["organization_id"],
                        "object_organization_id": target["organization_id"],
                        "evidence_ids": [], "status": "accepted",
                        "approved_by": [OPERATOR_CURATED_APPROVER],
                    }
                    relationships_by_edge[edge_key] = relationship
                    relationships.append(relationship)
                relationship["evidence_ids"].append(evidence_id)
                relationship_ids.append(relationship_id)
            else:
                evidence.append({
                    "evidence_id": evidence_id, "authority": "source_untrusted", "status": "proposed",
                    "source_key": key, "field": "af_groupname", "quote": group,
                    "payload_sha256": canonical_sha256({"source_key": key, "af_groupname": group}),
                })
                proposals.append({
                    "relationship_id": relationship_id, "relationship_type": "member_of",
                    "subject_organization_id": organization["organization_id"],
                    "object_organization_id": target["organization_id"],
                    "evidence_ids": [evidence_id], "status": "proposed",
                    "requires_official_membership_evidence": True,
                })
                proposal_ids.append(relationship_id)
                proposed_groups.append(group)
        after = _after(key, record, organization, issues, curated=operator_curated,
                       relationship_ids=relationship_ids)
        correction = {
            "source_sha256": source_sha256, "source_key": key, "source_record": copy.deepcopy(record),
            "organization_ids": [organization["organization_id"]], "relationship_ids": relationship_ids,
            "relationship_proposal_ids": proposal_ids, "aliases": copy.deepcopy(organization["aliases"]),
            "af_id_replace_tokens": _replacement_tokens(key, record, source_keys),
            "before": {"af_name": copy.deepcopy(record.get("af_name", [])),
                       "af_groupname": copy.deepcopy(record.get("af_groupname", [])),
                       "af_id_replace": copy.deepcopy(record.get("af_id_replace", []))},
            "original_group_labels": _groups(record),
            "proposed_corrected_group_labels": after["proposed_group_labels"],
            "proposed_relationship_group_labels": proposed_groups, "after": after,
            "disposition": ("identity_accepted_operator_curated" if operator_curated
                            else ("identity_proposed_relationship_pending" if proposal_ids
                                  else "identity_proposed")),
            "issue_codes": issues,
            "correction_decisions": [{
                "field": "af_groupname",
                "action": "replace_accepted_label" if operator_curated else "replace_proposed_label",
                "corrected_values": copy.deepcopy(after["proposed_group_labels"]),
                "acceptance": ("operator_curated" if operator_curated
                               else "pending_official_relationship_evidence"),
            }] if issues else [],
            "evidence": {
                "status": "accepted" if operator_curated else "proposed",
                "authority": "operator_curated" if operator_curated else "source_untrusted",
                "official_identity_evidence_required": not operator_curated,
                "official_membership_evidence_required": bool(proposal_ids),
                "references": [relationship_id for relationship_id in relationship_ids],
            },
            "confidence": 1.0 if operator_curated else 0.0,
            "reviewers": [OPERATOR_CURATED_APPROVER] if operator_curated else [],
            "decision_provenance": ("operator_curated_pinned_source" if operator_curated
                                    else "untrusted_source_audit"),
            "rationale": ("Operator-curated acceptance is limited to this SHA-bound pinned source."
                          if operator_curated else
                          "This source record remains proposal-only until distinct reviewed evidence is approved."),
        }
        corrections.append(correction)

    events: list[dict[str, Any]] = []
    previous = ZERO_DIGEST
    def append_event(event_type: str, event_key: str, payload: dict[str, Any]) -> None:
        nonlocal previous
        event = {"sequence": len(events) + 1, "event_id": _id("event", source_sha256, event_key),
                 "type": event_type, "timestamp": timestamp,
                 "actor": OPERATOR_CURATED_APPROVER if operator_curated else "offline-import",
                 "policy_version": POLICY_VERSION, "previous_digest": previous,
                 "registry_contract_version": REGISTRY_CONTRACT_VERSION,
                 "event_contract_version": EVENT_CONTRACT_VERSION,
                 "country_map_version": COUNTRY_MAP_VERSION,
                 "country_map_sha256": COUNTRY_MAP_SHA256,
                 "evidence_oracle_version": EVIDENCE_ORACLE_VERSION,
                 "evidence_oracle_sha256": EVIDENCE_ORACLE_SHA256,
                 "payload": copy.deepcopy(payload)}
        event["digest"] = _event_digest(event)
        previous = event["digest"]
        events.append(event)
    if operator_curated:
        corrections_by_key = {correction["source_key"]: correction for correction in corrections}
        for organization in sorted(organizations, key=lambda item: item["organization_id"]):
            root = next(key for key, value in organization_by_source.items()
                        if value is organization and root_key_by_source[key] == key)
            append_event("source_identity_accepted", root, {
                "organization": organization, "correction": corrections_by_key[root],
            })
        for correction in sorted(corrections, key=lambda item: item["source_key"]):
            if root_key_by_source[correction["source_key"]] != correction["source_key"]:
                append_event("source_decision_created", f"decision:{correction['source_key']}", {
                    "source_key": correction["source_key"], "correction": correction,
                })
    else:
        for organization, correction in sorted(zip(organizations, corrections),
                                               key=lambda item: item[1]["source_key"]):
            append_event("source_identity_proposed", correction["source_key"], {
                "organization": organization, "correction": correction,
            })
            if correction["issue_codes"]:
                append_event("known_correction_decided", f"correction:{correction['source_key']}", {
                    "source_key": correction["source_key"], "correction": correction,
                    "decisions": correction["correction_decisions"],
                })
    for organization in sorted(group_organizations.values(), key=lambda item: item["organization_id"]):
        append_event("group_identity_accepted" if operator_curated else "group_identity_proposed",
                     organization["organization_id"], {"organization": organization})
    evidence_by_id = {item["evidence_id"]: item for item in evidence}
    for relationship in sorted(relationships, key=lambda item: item["relationship_id"]):
        append_event("relationship_accepted", relationship["relationship_id"], {
            "relationship": relationship,
            "evidence": [evidence_by_id[item] for item in relationship["evidence_ids"]]})
    for proposal in sorted(proposals, key=lambda item: item["relationship_id"]):
        append_event("relationship_proposed", proposal["relationship_id"], {
            "relationship_proposal": proposal,
            "evidence": [evidence_by_id[item] for item in proposal["evidence_ids"]]})
    all_organizations = sorted([*organizations, *group_organizations.values()],
                               key=lambda item: item["organization_id"])
    registry = {
        "schema_version": REGISTRY_SCHEMA_VERSION, "registry_version": version,
        "registry_contract_version": REGISTRY_CONTRACT_VERSION,
        "event_contract_version": EVENT_CONTRACT_VERSION,
        "policy_version": POLICY_VERSION, "source_sha256": source_sha256,
        "country_map_version": COUNTRY_MAP_VERSION, "country_map_sha256": COUNTRY_MAP_SHA256,
        "evidence_oracle_version": EVIDENCE_ORACLE_VERSION,
        "evidence_oracle_sha256": EVIDENCE_ORACLE_SHA256,
        "import_mode": "pinned_operator_curated" if operator_curated else "source_proposals",
        "organizations": all_organizations, "alias_candidates": _identity_candidates(all_organizations),
        "relationships": sorted(relationships, key=lambda item: item["relationship_id"]),
        "relationship_proposals": sorted(proposals, key=lambda item: item["relationship_id"]),
        "evidence": sorted(evidence, key=lambda item: item["evidence_id"]),
        "events": events, "event_head": previous,
    }
    if _validate_result:
        validate_registry(registry, require_replay=True)
    return registry


def correction_projection(registry: Mapping[str, Any]) -> list[dict[str, Any]]:
    """Replay current source decisions into one deterministic correction per key."""
    rows: dict[str, dict[str, Any]] = {}
    for event in registry.get("events", []):
        if event.get("type") not in {
                "source_decision_created", "source_decision_superseded",
                "source_identity_proposed", "source_identity_accepted",
                "known_correction_decided"}:
            continue
        correction = event.get("payload", {}).get("correction")
        if isinstance(correction, Mapping):
            row = copy.deepcopy(correction)
            row["current_event_id"] = event["event_id"]
            rows[row["source_key"]] = row
    return [rows[key] for key in sorted(rows)]


def _unique(items: Iterable[Mapping[str, Any]], keys: tuple[str, ...], label: str) -> None:
    seen = set()
    for item in items:
        value = tuple(item.get(key) for key in keys)
        if value in seen:
            raise ValueError(f"duplicate {label}: {value!r}")
        seen.add(value)

def _relationship_id_set_sha256(relationship_ids: Iterable[str]) -> str:
    """Hash the complete sorted relationship-ID set bound into a policy transition."""
    return canonical_sha256(sorted(relationship_ids))


def _relationship_projection_set_sha256(
        relationships: Iterable[Mapping[str, Any]]) -> str:
    """Hash the frozen SQLite edge projection, including every accepted edge field."""
    rows = []
    for relationship in sorted(
            relationships, key=lambda item: str(item.get("relationship_id", ""))):
        interval = relationship.get("validity_interval") or {}
        rows.append({
            "relationship_id": relationship.get("relationship_id"),
            "subject_organization_id": relationship.get("subject_organization_id"),
            "object_organization_id": relationship.get("object_organization_id"),
            "relationship_type": relationship.get("relationship_type"),
            "valid_from": interval.get("start", ""),
            "valid_to": interval.get("end", ""),
            "status": relationship.get("status"),
            "confidence": 1.0,
            "created_event_id": "",
            "managed_by": "registry",
        })
    return canonical_sha256(rows)


def _replay_relationship_policy_transition(
        event: Mapping[str, Any], relationships: list[dict[str, Any]],
        relationship_proposals: list[dict[str, Any]], evidence: list[dict[str, Any]],
        *, source_sha256: str) -> None:
    """Project one exact-head relationship-policy transition without discarding history."""
    payload = event.get("payload")
    if not isinstance(payload, Mapping):
        raise ValueError("relationship policy transition payload must be an object")
    legacy_ids = sorted(item.get("relationship_id") for item in relationships)
    if (any(not isinstance(item, str) for item in legacy_ids)
            or not isinstance(payload.get("effective_date"), str)
            or not DATE_RE.fullmatch(payload["effective_date"])
            or payload.get("expected_event_head") != event.get("previous_digest")
            or payload.get("pre_relationship_ids") != legacy_ids
            or payload.get("pre_relationship_ids_sha256") != _relationship_id_set_sha256(legacy_ids)
            or payload.get("legacy_count") != len(legacy_ids)):
        raise ValueError("relationship policy transition pre-state mismatch")
    if (len(legacy_ids) != FROZEN_LEGACY_RELATIONSHIP_COUNT
            or len(set(legacy_ids)) != FROZEN_LEGACY_RELATIONSHIP_COUNT
            or _relationship_id_set_sha256(legacy_ids)
            != FROZEN_LEGACY_RELATIONSHIP_ID_SET_SHA256
            or payload.get("pre_relationship_snapshot_sha256")
            != FROZEN_LEGACY_RELATIONSHIP_SET_SHA256):
        raise ValueError("relationship policy transition legacy cohort is not the frozen set")
    retained = payload.get("official_retained_relationship_ids")
    demoted = payload.get("demoted_relationships")
    if (not isinstance(retained, list) or not isinstance(demoted, list)
            or retained != sorted(retained)
            or any(not isinstance(item, str) for item in retained)
            or not all(isinstance(item, Mapping) for item in demoted)):
        raise ValueError("relationship policy transition classifications are malformed")
    demoted_ids = [item.get("relationship_id") for item in demoted]
    if (any(not isinstance(item, str) for item in demoted_ids)
            or demoted_ids != sorted(demoted_ids)
            or len(set(retained)) != len(retained)
            or len(set(demoted_ids)) != len(demoted_ids)
            or set(retained) | set(demoted_ids) != set(legacy_ids)
            or set(retained) & set(demoted_ids)
            or payload.get("official_retained_count") != len(retained)
            or payload.get("demoted_or_superseded_count") != len(demoted_ids)
            or len(legacy_ids) != len(retained) + len(demoted_ids)):
        raise ValueError("relationship policy transition does not classify every edge exactly once")
    evidence_by_id = {item.get("evidence_id"): item for item in evidence}
    relationship_by_id = {
        item["relationship_id"]: item for item in relationships}
    for relationship in relationships:
        relationship_id = relationship["relationship_id"]
        if relationship_id in retained and not any(
                item.get("authority") == "official" and _official_evidence_valid(item)
                for item in (evidence_by_id.get(ref) for ref in relationship.get("evidence_ids", []))
                if isinstance(item, Mapping)):
            raise ValueError("retained relationship lacks reviewed official evidence")
    demoted_by_id = {item["relationship_id"]: item for item in demoted}
    new_proposals: list[dict[str, Any]] = []
    new_evidence: list[dict[str, Any]] = []
    for relationship_id in demoted_ids:
        item = demoted_by_id[relationship_id]
        source = relationship_by_id[relationship_id]
        proposal, proposal_evidence = item.get("relationship_proposal"), item.get("evidence")
        evidence_id = _id(
            "relationship-policy-proposal-evidence",
            source_sha256,
            relationship_id)
        proposal_id = _id(
            "relationship-policy-proposal",
            source_sha256,
            relationship_id)
        expected_evidence = {
            "evidence_id": evidence_id,
            "authority": "operator_curated",
            "status": "proposed",
            "review_status": "superseded",
            "quote": relationship_id,
            "payload": {
                "transition": "official-relationships-v1",
                "source_relationship_id": relationship_id,
                "legacy_evidence_ids": list(source["evidence_ids"]),
            },
        }
        expected_evidence["payload_sha256"] = canonical_sha256(
            expected_evidence["payload"])
        expected_evidence["quote_sha256"] = canonical_sha256(
            expected_evidence["quote"])
        expected_proposal = {
            "relationship_id": proposal_id,
            "source_relationship_id": relationship_id,
            "relationship_type": source["relationship_type"],
            "subject_organization_id": source["subject_organization_id"],
            "object_organization_id": source["object_organization_id"],
            "evidence_ids": [evidence_id],
            "status": "proposed",
            "requires_official_membership_evidence": True,
        }
        if "validity_interval" in source:
            expected_proposal["validity_interval"] = copy.deepcopy(
                source["validity_interval"])
        if (
                not isinstance(proposal, Mapping)
                or not isinstance(proposal_evidence, Mapping)
                or dict(proposal) != expected_proposal
                or dict(proposal_evidence) != expected_evidence):
            raise ValueError(
                "relationship policy transition demotion is malformed")
        new_proposals.append(copy.deepcopy(dict(proposal)))
        new_evidence.append(copy.deepcopy(dict(proposal_evidence)))
    relationships[:] = [item for item in relationships if item["relationship_id"] in set(retained)]
    relationship_proposals.extend(new_proposals)
    evidence.extend(new_evidence)

def _replay_pinned_proposal_changes(
        event: Mapping[str, Any], proposals: list[dict[str, Any]]) -> None:
    payload = event.get("payload") or {}
    rewrites = payload.get("proposal_rewrites", [])
    supersessions = payload.get("proposal_supersessions", [])
    if not isinstance(rewrites, list) or not isinstance(supersessions, list):
        raise ValueError("pinned consolidation proposal history must be arrays")
    by_id = {row["relationship_id"]: row for row in proposals}
    touched: set[str] = set()
    for change in rewrites:
        if not isinstance(change, Mapping):
            raise ValueError("pinned consolidation proposal rewrite is malformed")
        before, after = change.get("before"), change.get("after")
        relationship_id = change.get("relationship_id")
        if (
                not isinstance(before, Mapping)
                or not isinstance(after, Mapping)
                or relationship_id in touched
                or before.get("relationship_id") != relationship_id
                or after.get("relationship_id") != relationship_id
                or by_id.get(relationship_id) != before
                or after.get("subject_organization_id")
                == after.get("object_organization_id")):
            raise ValueError("pinned consolidation proposal rewrite does not match replay")
        by_id[relationship_id] = copy.deepcopy(dict(after))
        touched.add(relationship_id)
    for change in supersessions:
        if not isinstance(change, Mapping):
            raise ValueError("pinned consolidation proposal supersession is malformed")
        before = change.get("before")
        relationship_id = change.get("relationship_id")
        if (
                not isinstance(before, Mapping)
                or relationship_id in touched
                or before.get("relationship_id") != relationship_id
                or by_id.get(relationship_id) != before):
            raise ValueError("pinned consolidation proposal supersession does not match replay")
        del by_id[relationship_id]
        touched.add(relationship_id)
    proposals[:] = sorted(by_id.values(), key=lambda row: row["relationship_id"])


def replay_registry(registry: Mapping[str, Any]) -> dict[str, Any]:
    """Replay immutable events and return the projection used for validation."""
    previous = ZERO_DIGEST
    organizations: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    relationship_proposals: list[dict[str, Any]] = []
    evidence: list[dict[str, Any]] = []
    redirects: list[dict[str, Any]] = []
    expected_sequence = 1
    for event in registry.get("events", []):
        if event.get("sequence") != expected_sequence:
            raise ValueError("event sequence is not contiguous")
        if event.get("previous_digest") != previous or event.get("digest") != _event_digest(event):
            raise ValueError("event hash chain mismatch")
        if "registry_contract_version" in registry and (
                event.get("registry_contract_version") != REGISTRY_CONTRACT_VERSION
                or event.get("event_contract_version") != EVENT_CONTRACT_VERSION
                or event.get("policy_version") != POLICY_VERSION
                or event.get("country_map_version") != COUNTRY_MAP_VERSION
                or event.get("country_map_sha256") != COUNTRY_MAP_SHA256
                or event.get("evidence_oracle_version") != EVIDENCE_ORACLE_VERSION
                or event.get("evidence_oracle_sha256") != EVIDENCE_ORACLE_SHA256):
            raise ValueError("event policy, contract, country map, or evidence oracle mismatch")
        previous = event["digest"]
        expected_sequence += 1
        payload = event.get("payload", {})
        if not isinstance(payload, Mapping):
            raise ValueError("event payload must be an object")
        if event.get("type") in {"source_decision_created", "source_identity_proposed",
                                 "group_identity_proposed", "source_identity_accepted",
                                 "group_identity_accepted"}:
            if "organization" in payload:
                organizations.append(copy.deepcopy(payload["organization"]))
        elif event.get("type") == "relationship_accepted":
            relationships.append(copy.deepcopy(payload["relationship"]))
            evidence.extend(copy.deepcopy(payload["evidence"]))
        elif event.get("type") == "relationship_proposed":
            relationship_proposals.append(copy.deepcopy(payload["relationship_proposal"]))
            evidence.extend(copy.deepcopy(payload["evidence"]))
        elif event.get("type") == "relationship_policy_transition":
            _replay_relationship_policy_transition(
                event, relationships, relationship_proposals, evidence,
                source_sha256=str(registry.get("source_sha256") or ""))
        elif event.get("type") == "identity_accepted":
            for organization in organizations:
                if organization["organization_id"] == payload["organization_id"]:
                    organization["status"] = "active"
                    organization["identifiers"].append(copy.deepcopy(payload["identifier"]))
                    organization["identifiers"].sort(
                        key=lambda item: (item["authority"], item["value"]))
                    evidence.extend(copy.deepcopy(payload["evidence"]))
                    break
        elif event.get("type") in {
                "pinned_root_consolidated", "identity_created", "identity_enriched",
                "identity_aliased", "identity_merged", "identity_rejected", "identity_split"}:
            replay_identity_transition(event, organizations)
            if event.get("type") == "identity_split":
                restored = payload.get("restored", [])
                restored_ids = {item.get("organization_id") for item in restored
                                if isinstance(item, Mapping)}
                redirects[:] = [
                    item for item in redirects
                    if item.get("from_organization_id") not in restored_ids
                ]
            else:
                redirects.extend(copy.deepcopy(payload.get("redirects", [])))
            if event.get("type") == "pinned_root_consolidated":
                _replay_pinned_proposal_changes(event, relationship_proposals)
        elif event.get("type") == "identity_alias_accepted":
            for organization in organizations:
                if organization["organization_id"] == payload["organization_id"]:
                    organization["aliases"].append(copy.deepcopy(payload["alias"]))
                    organization["aliases"].sort(key=lambda item: (item["normalized_alias"],
                                                                  item["country_discriminator"], item["alias_id"]))
                    evidence.extend(copy.deepcopy(payload.get("evidence", [])))
                    break
        elif event.get("type") == "country_map_changed":
            validate_country_event(event)
        elif event.get("type") == "country_corrected":
            validate_country_event(event)
            replacement = payload["after"]
            if not isinstance(replacement, Mapping):
                raise ValueError("country correction after projection must be an object")
            for index, organization in enumerate(organizations):
                if organization["organization_id"] == payload["organization_id"]:
                    if canonical_country(organization.get("country")) != canonical_country(payload["old_country"]):
                        raise ValueError("country correction old country does not match replay state")
                    organizations[index] = copy.deepcopy(dict(replacement))
                    break
            else:
                raise ValueError("country correction references unknown organization")
        elif event.get("type") == "known_correction_decided":
            continue
        else:
            raise ValueError("unsupported event type")
    organizations = sorted(organizations, key=lambda item: item["organization_id"])
    return {"organizations": organizations, "alias_candidates": _identity_candidates(organizations),
            "relationships": sorted(relationships, key=lambda item: item["relationship_id"]),
            "relationship_proposals": sorted(relationship_proposals, key=lambda item: item["relationship_id"]),
            "evidence": sorted(evidence, key=lambda item: item["evidence_id"]),
            "redirects": sorted(redirects, key=lambda item: (
                item["from_organization_id"], item["to_organization_id"])),
            "event_head": previous}


def _validate_operator_curated_registry(registry: Mapping[str, Any]) -> None:
    correction_events = [
        event["payload"]["correction"]
        for event in registry["events"]
        if isinstance(event.get("payload"), Mapping)
        and isinstance(event["payload"].get("correction"), Mapping)
    ]
    correction_keys = [item.get("source_key") for item in correction_events]
    reconstructed_source = {
        item["source_key"]: item.get("source_record")
        for item in correction_events
        if isinstance(item.get("source_key"), str)
    }
    if (registry.get("source_sha256") != SOURCE_SHA256
            or len(correction_events) != OPERATOR_CURATED_RECORD_COUNT
            or len(set(correction_keys)) != OPERATOR_CURATED_RECORD_COUNT
            or canonical_sha256(reconstructed_source)
            != OPERATOR_CURATED_CANONICAL_SHA256):
        raise ValueError("operator-curated correction provenance mismatch")
    events = registry.get("events", [])
    if not events:
        raise ValueError("operator-curated event provenance missing")
    expected = build_registry(
        reconstructed_source,
        source_sha256=SOURCE_SHA256,
        timestamp=events[0].get("timestamp", ""),
        version=registry.get("registry_version"),
        operator_curated=True,
        _validate_result=False,
    )
    if "registry_contract_version" not in registry:
        for key in ("registry_contract_version", "event_contract_version",
                    "country_map_version", "country_map_sha256",
                    "evidence_oracle_version", "evidence_oracle_sha256"):
            expected.pop(key, None)
        for event in expected["events"]:
            for key in ("registry_contract_version", "event_contract_version",
                        "country_map_version", "country_map_sha256",
                        "evidence_oracle_version", "evidence_oracle_sha256"):
                event.pop(key, None)
            event["digest"] = _event_digest(event)
        previous = ZERO_DIGEST
        for event in expected["events"]:
            event["previous_digest"] = previous
            event["digest"] = _event_digest(event)
            previous = event["digest"]
        expected["event_head"] = previous
    prefix = expected["events"]
    if events[:len(prefix)] != prefix:
        raise ValueError("operator-curated immutable event/root prefix mismatch")
    suffix = events[len(prefix):]
    transition_positions = [
        index for index, event in enumerate(suffix)
        if event.get("type") == "relationship_policy_transition"
    ]
    if len(transition_positions) > 1:
        raise ValueError("relationship policy transition was already applied")
    allowed_after_transition = {
        "pinned_root_consolidated", "identity_created", "identity_enriched",
        "identity_aliased", "identity_merged", "identity_rejected", "identity_split",
        "country_map_changed", "country_corrected",
    }
    if suffix:
        if not transition_positions or transition_positions[0] != 0:
            raise ValueError("operator-curated identity events require relationship policy transition")
        if any(event.get("type") not in allowed_after_transition
               for event in suffix[1:]):
            raise ValueError("unsupported operator-curated append event")


def validate_registry(registry: Mapping[str, Any], *, require_replay: bool = True,
                      effective_date: str | None = None) -> None:
    """Validate canonical ordering, immutable event replay, and publishable graph evidence."""
    if effective_date is not None and (not isinstance(effective_date, str)
                                       or not DATE_RE.fullmatch(effective_date)):
        raise ValueError("effective date must be an ISO date")
    if registry.get("schema_version") != REGISTRY_SCHEMA_VERSION:
        raise ValueError("unsupported registry schema")
    if "registry_contract_version" in registry and (
            registry.get("registry_contract_version") != REGISTRY_CONTRACT_VERSION
            or registry.get("event_contract_version") != EVENT_CONTRACT_VERSION
            or registry.get("policy_version") != POLICY_VERSION
            or registry.get("country_map_version") != COUNTRY_MAP_VERSION
            or registry.get("country_map_sha256") != COUNTRY_MAP_SHA256
            or registry.get("evidence_oracle_version") != EVIDENCE_ORACLE_VERSION
            or registry.get("evidence_oracle_sha256") != EVIDENCE_ORACLE_SHA256):
        raise ValueError("unsupported registry policy, contract, country map, or evidence oracle")
    organizations = registry.get("organizations")
    alias_candidates = registry.get("alias_candidates")
    relationships = registry.get("relationships")
    relationship_proposals = registry.get("relationship_proposals")
    evidence = registry.get("evidence")
    events = registry.get("events")
    if not all(isinstance(value, list) for value in (
            organizations, alias_candidates, relationships,
            relationship_proposals, evidence, events)):
        raise ValueError("registry collections must be arrays")
    replayed = None
    if require_replay or registry.get("import_mode") == "pinned_operator_curated":
        replayed = replay_registry(registry)
    if registry.get("import_mode") == "pinned_operator_curated":
        _validate_operator_curated_registry(registry)
    if organizations != sorted(organizations, key=lambda x: x["organization_id"]):
        raise ValueError("organizations are not sorted by immutable ID")
    if alias_candidates != _identity_candidates(organizations):
        raise ValueError("alias candidates are not the identity projection")
    _unique(organizations, ("organization_id",), "organization ID")
    _unique(alias_candidates, ("normalized_alias", "country_discriminator", "organization_id", "alias_id"),
            "alias candidate")
    _unique(relationships, ("relationship_id",), "relationship ID")
    _unique(relationship_proposals, ("relationship_id",), "relationship proposal ID")
    _unique(evidence, ("evidence_id",), "evidence ID")
    evidence_by_id = {item["evidence_id"]: item for item in evidence}
    organization_ids = {item["organization_id"] for item in organizations}
    organization_by_id = {item["organization_id"]: item for item in organizations}
    redirects = registry.get("redirects", [])
    if not isinstance(redirects, list):
        raise ValueError("registry redirects must be an array")
    redirect_sources = set()
    for redirect in redirects:
        source_id, target_id = redirect.get("from_organization_id"), redirect.get("to_organization_id")
        if (not isinstance(source_id, str) or not isinstance(target_id, str)
                or source_id == target_id or source_id in organization_ids
                or target_id not in organization_ids or source_id in redirect_sources):
            raise ValueError("invalid direct organization redirect")
        redirect_sources.add(source_id)
    for organization in organizations:
        uuid.UUID(organization["organization_id"])
        if organization["canonical_name_en"] != nfc(organization["canonical_name_en"]):
            raise ValueError("non-NFC canonical name")
        _unique(organization.get("identifiers", []), ("authority", "value"), "identifier within organization")
        _unique(organization.get("aliases", []), ("alias_id",), "alias ID")
    _unique(
        [
            identifier
            for organization in organizations
            for identifier in organization.get("identifiers", [])
        ],
        ("authority", "value"),
        "identifier across organizations",
    )
    for relationship in relationships:
        if relationship.get("relationship_type") not in RELATIONSHIP_TYPES:
            raise ValueError("unsupported relationship type")
        if relationship.get("subject_organization_id") not in organization_ids or relationship.get("object_organization_id") not in organization_ids:
            raise ValueError("relationship has unknown organization")
        if (organization_by_id[relationship["subject_organization_id"]].get("status") != "active"
                or organization_by_id[relationship["object_organization_id"]].get("status") != "active"):
            raise ValueError("relationship references unreviewed identity")
        if relationship.get("subject_organization_id") == relationship.get("object_organization_id"):
            raise ValueError("self relationship is forbidden")
        if (relationship.get("status") != "accepted"
                or not isinstance(relationship.get("approved_by"), list)
                or not relationship["approved_by"]):
            raise ValueError("relationship is not approved")
        _validate_interval(relationship)
        refs = relationship.get("evidence_ids", [])
        if not refs or any(
                ref not in evidence_by_id
                or not _official_evidence_valid(evidence_by_id[ref], effective_date)
                or (evidence_by_id[ref].get("authority") == "operator_curated"
                    and (registry.get("import_mode") != "pinned_operator_curated"
                         or registry.get("source_sha256") != SOURCE_SHA256))
                for ref in refs):
            raise ValueError("relationship lacks accepted official evidence")
    for proposal in relationship_proposals:
        if proposal.get("relationship_type") not in RELATIONSHIP_TYPES:
            raise ValueError("unsupported relationship proposal type")
        if proposal.get("subject_organization_id") not in organization_ids or proposal.get("object_organization_id") not in organization_ids:
            raise ValueError("relationship proposal has unknown organization")
        if proposal.get("subject_organization_id") == proposal.get("object_organization_id"):
            raise ValueError("self relationship proposal is forbidden")
        _validate_interval(proposal)
        refs = proposal.get("evidence_ids", [])
        if not refs or any(ref not in evidence_by_id or evidence_by_id[ref].get("status") != "proposed" for ref in refs):
            raise ValueError("relationship proposal lacks source provenance")
        if proposal.get("status") != "proposed" or not proposal.get("requires_official_membership_evidence"):
            raise ValueError("relationship proposal must remain pending official evidence")
    _validate_relationship_graph(
        relationships, organizations, evidence_by_id,
        enforce_single_parent=any(
            event.get("type") == "relationship_policy_transition"
            for event in events))
    if require_replay and (
            replayed["organizations"] != organizations
            or replayed["alias_candidates"] != alias_candidates
            or replayed["relationships"] != relationships
            or replayed["relationship_proposals"] != relationship_proposals
            or replayed["evidence"] != evidence
            or ("redirects" in registry and replayed["redirects"] != redirects)
            or replayed["event_head"] != registry.get("event_head")):
        raise ValueError("registry projection does not match event replay")
def _validate_interval(relationship: Mapping[str, Any]) -> None:
    """Reject malformed relationship validity intervals while allowing open intervals."""
    interval = relationship.get("validity_interval")
    if interval is None:
        return
    if not isinstance(interval, Mapping):
        raise ValueError("relationship interval must be an object")
    start, end = interval.get("start", ""), interval.get("end", "")
    if start and (not isinstance(start, str) or not DATE_RE.fullmatch(start)):
        raise ValueError("relationship interval start must be an ISO date")
    if end and (not isinstance(end, str) or not DATE_RE.fullmatch(end)):
        raise ValueError("relationship interval end must be an ISO date")
    if start and end and start > end:
        raise ValueError("relationship interval is inverted")


def _official_evidence_valid(evidence: Mapping[str, Any],
                             effective_date: str | None = None) -> bool:
    if not isinstance(evidence, Mapping):
        return False
    if evidence.get("authority") == "operator_curated":
        payload = evidence.get("payload")
        return (
            evidence.get("status") == "accepted"
            and evidence.get("review_status") == "approved"
            and evidence.get("approved_by") == [OPERATOR_CURATED_APPROVER]
            and isinstance(evidence.get("quote"), str) and bool(evidence["quote"].strip())
            and isinstance(payload, Mapping)
            and payload.get("import_mode") == "pinned_operator_curated"
            and payload.get("source_sha256") == SOURCE_SHA256
            and isinstance(payload.get("source_key"), str)
            and isinstance(payload.get("original_group_labels"), list)
            and isinstance(payload.get("corrected_group_label"), str)
            and isinstance(payload.get("issue_codes"), list)
            and evidence.get("payload_sha256") == canonical_sha256(payload)
            and evidence.get("quote_sha256") == canonical_sha256(evidence["quote"])
        )
    quote = evidence.get("quote")
    payload = evidence.get("payload")
    revalidated_at = evidence.get("revalidated_at")
    if (evidence.get("review_status") != "approved"
            or not isinstance(evidence.get("approved_by"), list)
            or not evidence["approved_by"]
            or not isinstance(revalidated_at, str)
            or not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", revalidated_at)):
        return False
    if effective_date is not None:
        try:
            if (date.fromisoformat(effective_date)
                    - date.fromisoformat(revalidated_at[:10])).days > 90:
                return False
        except ValueError:
            return False
    return (
        evidence.get("authority") == "official"
        and evidence.get("status") == "accepted"
        and isinstance(evidence.get("url"), str)
        and evidence["url"].startswith("https://")
        and isinstance(quote, str) and bool(quote.strip())
        and isinstance(payload, Mapping)
        and evidence.get("payload_sha256") == canonical_sha256(payload)
        and evidence.get("quote_sha256") == canonical_sha256(quote)
    )


def _validate_relationship_graph(relationships: Iterable[Mapping[str, Any]],
                                 organizations: Iterable[Mapping[str, Any]],
                                 evidence_by_id: Mapping[str, Mapping[str, Any]],
                                 *, enforce_single_parent: bool = True) -> None:
    """Reject invalid accepted graph states before canonical publication."""
    organization_by_id = {item["organization_id"]: item for item in organizations}
    intervals: dict[tuple[str, str, str], list[tuple[str, str]]] = {}
    parents: dict[str, list[str]] = {}
    for relationship in relationships:
        key = (relationship["subject_organization_id"], relationship["object_organization_id"],
               relationship["relationship_type"])
        interval = relationship.get("validity_interval") or {}
        intervals.setdefault(key, []).append((interval.get("start", ""), interval.get("end", "")))
        if relationship["relationship_type"] == "part_of":
            parents.setdefault(relationship["subject_organization_id"], []).append(
                relationship["object_organization_id"])
        if (relationship["relationship_type"] in {"part_of", "jointly_operated_by"}
                and organization_by_id[relationship["subject_organization_id"]]["country"]
                != organization_by_id[relationship["object_organization_id"]]["country"]
                and not all(evidence_by_id[evidence_id].get("cross_border_explicit") is True
                            for evidence_id in relationship["evidence_ids"])):
            raise ValueError("cross-border structural relationship lacks explicit official evidence")
    current_parents: dict[str, set[str]] = {}
    for relationship in relationships:
        if (relationship["relationship_type"] == "part_of"
                and not (relationship.get("validity_interval") or {}).get("end")):
            current_parents.setdefault(relationship["subject_organization_id"], set()).add(
                relationship["object_organization_id"])
    if (enforce_single_parent
            and any(len(objects) > 1 for objects in current_parents.values())):
        raise ValueError("organization has more than one current part_of parent")
    for key, values in intervals.items():
        values.sort()
        for (_, previous_end), (current_start, _) in zip(values, values[1:]):
            if not previous_end or not current_start or current_start < previous_end:
                raise ValueError(f"overlapping relationship validity intervals: {key!r}")
    visiting, depths = set(), {}

    def walk(organization_id: str) -> int:
        if organization_id in visiting:
            raise ValueError("part_of relationship cycle")
        if organization_id in depths:
            return depths[organization_id]
        visiting.add(organization_id)
        depth = 0
        for parent in parents.get(organization_id, []):
            depth = max(depth, 1 + walk(parent))
        visiting.remove(organization_id)
        if depth > 8:
            raise ValueError("part_of depth exceeds 8")
        depths[organization_id] = depth
        return depth

    for organization_id in parents:
        walk(organization_id)


def load_registry(path: str | Path, *, validate: bool = True) -> dict[str, Any]:
    """Load a UTF-8 registry snapshot and optionally validate replay integrity."""
    raw = Path(path).read_bytes()
    if raw.startswith(b"\xef\xbb\xbf") or not raw.endswith(b"\n"):
        raise ValueError("registry must be UTF-8 without BOM and end in LF")
    registry = json.loads(raw.decode("utf-8"))
    if canonical_json_bytes(registry) != raw:
        raise ValueError("registry is not canonical JSON")
    if validate:
        validate_registry(registry)
    return registry
def transition_relationship_policy(
        registry: Mapping[str, Any], *, timestamp: str, effective_date: str,
        actor: str, expected_event_head: str) -> dict[str, Any]:
    """Append the one-shot official-only relationship transition."""
    if not DATE_RE.fullmatch(effective_date):
        raise ValueError("effective date must be an ISO date")
    validate_registry(registry)
    if registry.get("event_head") != expected_event_head:
        raise ValueError("expected event head does not match")
    if any(event.get("type") == "relationship_policy_transition" for event in registry["events"]):
        raise ValueError("relationship policy transition was already applied")
    if (len(registry["relationships"]) != FROZEN_LEGACY_RELATIONSHIP_COUNT
            or _relationship_id_set_sha256(
                item.get("relationship_id") for item in registry["relationships"])
            != FROZEN_LEGACY_RELATIONSHIP_ID_SET_SHA256
            or _relationship_projection_set_sha256(registry["relationships"])
            != FROZEN_LEGACY_RELATIONSHIP_SET_SHA256):
        raise ValueError("relationship policy transition requires the frozen legacy cohort")
    result = copy.deepcopy(dict(registry))
    evidence_by_id = {item["evidence_id"]: item for item in result["evidence"]}
    legacy = sorted(result["relationships"], key=lambda item: item["relationship_id"])
    retained_ids: list[str] = []
    demoted: list[dict[str, Any]] = []
    for relationship in legacy:
        relationship_id = relationship["relationship_id"]
        official = any(
            item.get("authority") == "official" and _official_evidence_valid(item)
            for item in (evidence_by_id.get(ref) for ref in relationship["evidence_ids"])
            if isinstance(item, Mapping))
        if official:
            retained_ids.append(relationship_id)
            continue
        evidence_id = _id("relationship-policy-proposal-evidence", result["source_sha256"],
                          relationship_id)
        proposal_id = _id("relationship-policy-proposal", result["source_sha256"], relationship_id)
        proposal_evidence = {
            "evidence_id": evidence_id, "authority": "operator_curated",
            "status": "proposed", "review_status": "superseded",
            "quote": relationship_id,
            "payload": {"transition": "official-relationships-v1",
                        "source_relationship_id": relationship_id,
                        "legacy_evidence_ids": list(relationship["evidence_ids"])},
        }
        proposal_evidence["payload_sha256"] = canonical_sha256(proposal_evidence["payload"])
        proposal_evidence["quote_sha256"] = canonical_sha256(proposal_evidence["quote"])
        proposal = {
            "relationship_id": proposal_id,
            "source_relationship_id": relationship_id,
            "relationship_type": relationship["relationship_type"],
            "subject_organization_id": relationship["subject_organization_id"],
            "object_organization_id": relationship["object_organization_id"],
            "evidence_ids": [evidence_id], "status": "proposed",
            "requires_official_membership_evidence": True,
        }
        if "validity_interval" in relationship:
            proposal["validity_interval"] = copy.deepcopy(relationship["validity_interval"])
        demoted.append({"relationship_id": relationship_id,
                        "relationship_proposal": proposal, "evidence": proposal_evidence})
    payload = {
        "expected_event_head": expected_event_head,
        "effective_date": effective_date,
        "pre_relationship_ids": [item["relationship_id"] for item in legacy],
        "pre_relationship_ids_sha256": _relationship_id_set_sha256(
            item["relationship_id"] for item in legacy),
        "pre_relationship_snapshot_sha256":
            _relationship_projection_set_sha256(legacy),
        "legacy_count": len(legacy), "official_retained_count": len(retained_ids),
        "demoted_or_superseded_count": len(demoted),
        "official_retained_relationship_ids": retained_ids,
        "demoted_relationships": demoted,
    }
    event = {
        "sequence": len(result["events"]) + 1,
        "event_id": _id("relationship-policy-transition", result["source_sha256"],
                        payload["pre_relationship_ids_sha256"]),
        "type": "relationship_policy_transition", "timestamp": timestamp, "actor": actor,
        "policy_version": POLICY_VERSION, "previous_digest": expected_event_head,
        "registry_contract_version": REGISTRY_CONTRACT_VERSION,
        "event_contract_version": EVENT_CONTRACT_VERSION,
        "country_map_version": COUNTRY_MAP_VERSION, "country_map_sha256": COUNTRY_MAP_SHA256,
        "evidence_oracle_version": EVIDENCE_ORACLE_VERSION,
        "evidence_oracle_sha256": EVIDENCE_ORACLE_SHA256,
        "payload": payload,
    }
    event["digest"] = _event_digest(event)
    result["events"].append(event)
    projected = replay_registry(result)
    for key in ("organizations", "alias_candidates", "relationships", "relationship_proposals",
                "evidence", "redirects", "event_head"):
        if key in projected:
            result[key] = projected[key]
    validate_registry(result, effective_date=effective_date)
    return result


def relationship_lookup(registry: Mapping[str, Any], organization_id: str,
                        relationship_type: str | None = None) -> list[dict[str, Any]]:
    """Return accepted outgoing relationships, optionally filtered by type."""
    return [edge for edge in registry["relationships"]
            if edge["subject_organization_id"] == organization_id
            and (relationship_type is None or edge.get("relationship_type") == relationship_type)]
def is_generic_fragment(name: str) -> bool:
    """Whether a name is too generic to resolve or promote without context."""
    return bool(GENERIC_FRAGMENT_RE.match(nfc(name).strip()))


def _ror_v1_exact_candidates(payload: Mapping[str, Any], name: str,
                             country: str) -> list[dict[str, Any]]:
    """Keep the legacy discovery contract separate from automatic eligibility."""
    target, expected_country = normalize_name(name), canonical_country(country)
    if not target or not expected_country or not isinstance(payload.get("items"), list):
        return []
    candidates = []
    for item in payload["items"]:
        if not isinstance(item, Mapping):
            continue
        names = [item.get("name"), *item.get("aliases", [])]
        if target not in {normalize_name(value) for value in names if isinstance(value, str)}:
            continue
        location = item.get("country", {})
        observed = location.get("country_name") if isinstance(location, Mapping) else None
        if canonical_country(observed) != expected_country:
            continue
        links = item.get("links", [])
        if not isinstance(links, list) or not all(isinstance(link, str) for link in links):
            continue
        identifier = item.get("id")
        display_name = item.get("name")
        if not isinstance(identifier, str) or not isinstance(display_name, str):
            continue
        candidates.append({
            "external_id": identifier,
            "name": display_name,
            "country": expected_country,
            "links": sorted(set(links)),
            "score": 1.0,
            "reason": "legacy_ror_v1_exact_name_country_discovery",
        })
    return candidates


def automatic_ror_v2_candidates(payload: Mapping[str, Any], name: str,
                                country: str) -> list[dict[str, Any]]:
    """Return the only ROR candidates eligible for an automatic identity decision."""
    target, expected_country = normalize_name(name), canonical_country(country)
    if not target or not expected_country or not isinstance(payload.get("items"), list):
        return []
    candidates = []
    for item in payload["items"]:
        if not isinstance(item, Mapping) or item.get("status") not in {"active", "ACTIVE"}:
            continue
        names = [item.get("name", "")]
        display_name = item.get("name", "")
        for entry in item.get("names", []):
            if isinstance(entry, Mapping) and isinstance(entry.get("value"), str):
                names.append(entry["value"])
                if "ror_display" in entry.get("types", []):
                    display_name = entry["value"]
        if target not in {normalize_name(value) for value in names if isinstance(value, str)}:
            continue
        country_values = []
        for location in item.get("locations", []):
            if isinstance(location, Mapping):
                details = location.get("geonames_details", {})
                if isinstance(details, Mapping):
                    country_values.extend(details.get(key) for key in ("country_name", "country_code"))
        codes = sorted({code for value in country_values if isinstance(value, str)
                        for code in [canonical_country(value)] if code})
        websites = ror_v2_website_links(item)
        try:
            identifier = normalize_ror_id(item.get("id", ""))
        except ValueError:
            continue
        if codes != [expected_country] or not websites or not isinstance(display_name, str):
            continue
        candidates.append({
            "external_id": identifier,
            "name": display_name,
            "country": expected_country,
            "websites": websites,
            "links": list(websites),
            "score": 1.0,
            "reason": "active_ror_v2_exact_name_country_typed_website",
        })
    return sorted(candidates, key=lambda candidate: (candidate["external_id"], candidate["name"]))


def ror_exact_candidates(payload: Mapping[str, Any], name: str, country: str) -> list[dict[str, Any]]:
    """Return exact ROR discovery candidates, retaining the v1 caller contract.

    This function is intentionally not an automatic-acceptance gate.  Call
    :func:`automatic_ror_v2_candidates` for the strict v2/typed-website set.
    """
    v2 = automatic_ror_v2_candidates(payload, name, country)
    v1 = _ror_v1_exact_candidates(payload, name, country)
    return sorted([*v2, *v1], key=lambda candidate: (candidate["external_id"], candidate["name"]))
def promote_approved(registry: Mapping[str, Any], approvals: Iterable[Mapping[str, Any]], *,
                     timestamp: str) -> dict[str, Any]:
    """Append only policy-compliant reviewed promotions to a registry snapshot."""
    validate_registry(registry)
    result = copy.deepcopy(registry)
    organizations = {item["organization_id"]: item for item in result["organizations"]}
    previous = result["event_head"]
    for approval in approvals:
        if not isinstance(approval, Mapping) or approval.get("policy_version") != result["policy_version"]:
            raise ValueError("approval policy version does not match registry policy")
        if approval.get("kind") == "identity_alias":
            evidence = approval.get("evidence", {})
            reviewers = approval.get("approved_by")
            organization_id, alias = approval.get("organization_id"), approval.get("alias")
            if (not isinstance(evidence, Mapping) or organization_id not in organizations
                    or not isinstance(alias, str) or is_generic_fragment(alias)
                    or approval.get("confidence") != 1.0 or evidence.get("provider") != "ror"
                    or evidence.get("match") != "exact_country_consistent" or not evidence.get("external_id")
                    or not isinstance(reviewers, list) or len(set(reviewers)) < 2
                    or not all(isinstance(reviewer, str) and reviewer for reviewer in reviewers)):
                raise ValueError("identity alias approval lacks exact country-consistent ROR evidence and two reviewers")
            organization = organizations[organization_id]
            if organization.get("status") != "active":
                raise ValueError("identity alias approval requires a reviewed identity")
            alias_record = {"alias_id": _id("approved-alias", result["source_sha256"],
                                             f"{organization_id}:{normalize_name(alias)}:{evidence['external_id']}"),
                            "name": nfc(alias), "normalized_alias": normalize_name(alias),
                            "country_discriminator": organization["country"]}
            if any(item["alias_id"] == alias_record["alias_id"] for item in organization["aliases"]):
                continue
            alias_evidence = copy.deepcopy(dict(evidence))
            alias_evidence.update({
                "evidence_id": _id(
                    "identity-alias-evidence", result["source_sha256"],
                    canonical_sha256(alias_evidence)),
                "status": "accepted",
                "review_status": "approved",
                "approved_by": sorted(set(reviewers)),
                "revalidated_at": timestamp,
            })
            organization["aliases"].append(alias_record)
            organization["aliases"].sort(key=lambda item: (
                item["normalized_alias"], item["country_discriminator"], item["alias_id"]))
            result["evidence"].append(alias_evidence)
            result["evidence"].sort(key=lambda item: item["evidence_id"])
            event_type, payload = "identity_alias_accepted", {
                "organization_id": organization_id,
                "alias": alias_record,
                "evidence": [alias_evidence],
            }
        elif approval.get("kind") == "identity":
            evidence = approval.get("evidence", {})
            reviewers = approval.get("approved_by")
            organization_id = approval.get("organization_id")
            if (organization_id not in organizations or not isinstance(evidence, Mapping)
                    or approval.get("confidence") != 1.0
                    or evidence.get("provider") != "ror"
                    or evidence.get("match") != "exact_country_consistent"
                    or not isinstance(evidence.get("external_id"), str) or not evidence["external_id"]
                    or not isinstance(reviewers, list) or len(set(reviewers)) < 2
                    or not all(isinstance(reviewer, str) and reviewer for reviewer in reviewers)):
                raise ValueError("identity approval requires confidence 1.0, exact country-consistent ROR evidence, and two reviewers")
            organization = organizations[organization_id]
            identifier = {"authority": "ror", "value": evidence["external_id"]}
            if any(item == identifier for item in organization["identifiers"]):
                continue
            identity_evidence = copy.deepcopy(dict(evidence))
            identity_evidence.update({
                "evidence_id": _id(
                    "identity-evidence", result["source_sha256"],
                    canonical_sha256(identity_evidence)),
                "status": "accepted",
                "review_status": "approved",
                "approved_by": sorted(set(reviewers)),
                "revalidated_at": timestamp,
            })
            organization["status"] = "active"
            organization["identifiers"].append(identifier)
            organization["identifiers"].sort(key=lambda item: (item["authority"], item["value"]))
            result["evidence"].append(identity_evidence)
            result["evidence"].sort(key=lambda item: item["evidence_id"])
            event_type, payload = "identity_accepted", {
                "organization_id": organization_id,
                "identifier": identifier,
                "evidence": [identity_evidence],
            }
        elif approval.get("kind") == "relationship":
            relationship, evidence = approval.get("relationship"), approval.get("evidence", {})
            reviewers = approval.get("approved_by")
            evidence_record = copy.deepcopy(dict(evidence)) if isinstance(evidence, Mapping) else {}
            evidence_record.update({
                "approved_by": sorted(set(reviewers)) if isinstance(reviewers, list) else [],
                "review_status": "approved",
                "revalidated_at": timestamp,
            })
            if (not isinstance(relationship, Mapping) or relationship.get("relationship_type") not in RELATIONSHIP_TYPES
                    or relationship.get("subject_organization_id") not in organizations
                    or relationship.get("object_organization_id") not in organizations
                    or relationship.get("subject_organization_id") == relationship.get("object_organization_id")
                    or not isinstance(reviewers, list) or len(set(reviewers)) < 2
                    or not all(isinstance(reviewer, str) and reviewer for reviewer in reviewers)
                    or not _official_evidence_valid(evidence_record, timestamp[:10])):
                raise ValueError("relationship approval lacks exact official HTTPS evidence and two reviewer approvals")
            _validate_interval(relationship)
            evidence_record["evidence_id"] = _id(
                "official-evidence", result["source_sha256"], canonical_sha256(evidence_record)
            )
            relationship_record = dict(
                relationship,
                relationship_id=_id("accepted-relationship", result["source_sha256"], canonical_sha256(relationship)),
                evidence_ids=[evidence_record["evidence_id"]], status="accepted",
                approved_by=sorted(set(reviewers)),
            )
            if any(item["relationship_id"] == relationship_record["relationship_id"]
                   for item in result["relationships"]):
                continue
            result["evidence"].append(evidence_record)
            result["relationships"].append(relationship_record)
            result["evidence"].sort(key=lambda item: item["evidence_id"])
            result["relationships"].sort(key=lambda item: item["relationship_id"])
            event_type, payload = "relationship_accepted", {
                "relationship": relationship_record, "evidence": [evidence_record],
            }
        else:
            raise ValueError("approved record kind must be identity, identity_alias or relationship")
        event = {"sequence": len(result["events"]) + 1,
                 "event_id": _id("approved-event", result["source_sha256"], f"{len(result['events']) + 1}:{canonical_sha256(payload)}"),
                 "type": event_type, "timestamp": timestamp, "actor": "reviewed-approval",
                 "policy_version": result["policy_version"], "previous_digest": previous,
                 "payload": copy.deepcopy(payload),
                 "registry_contract_version": result.get("registry_contract_version", REGISTRY_CONTRACT_VERSION),
                 "event_contract_version": result.get("event_contract_version", EVENT_CONTRACT_VERSION),
                 "country_map_version": result.get("country_map_version", COUNTRY_MAP_VERSION),
                 "country_map_sha256": result.get("country_map_sha256", COUNTRY_MAP_SHA256),
                 "evidence_oracle_version": result.get(
                     "evidence_oracle_version", EVIDENCE_ORACLE_VERSION),
                 "evidence_oracle_sha256": result.get(
                     "evidence_oracle_sha256", EVIDENCE_ORACLE_SHA256)}
        event["digest"] = _event_digest(event)
        previous = event["digest"]
        result["events"].append(event)
    result["event_head"] = previous
    result["alias_candidates"] = _identity_candidates(result["organizations"])
    validate_registry(result, effective_date=timestamp[:10])
    return result


def identity_transition_action(organizations: Iterable[Mapping[str, Any]], *,
                               name: str, country: str | None, ror_id: str,
                               typed_websites: Iterable[str]) -> str:
    """Classify strict automatic create/enrich/alias/merge/reject transitions."""
    key = organization_identity_key(name, country)
    try:
        ror_id = normalize_ror_id(ror_id)
        websites = tuple(normalize_website_url(value) for value in typed_websites)
    except ValueError:
        return "reject"
    if key is None or not websites:
        return "reject"
    active = [item for item in organizations if item.get("status") == "active"]
    exact = [item for item in active if organization_identity_key(
        item.get("canonical_name_en", ""), item.get("country"),
        country_scope=item.get("country_scope")) == key]
    owners = [item for item in active if any(
        identifier.get("authority") == "ror" and identifier.get("value") == ror_id
        for identifier in item.get("identifiers", []))]
    if len(owners) != len({item.get("organization_id") for item in owners}) or len(owners) > 1:
        return "reject"
    if not exact and not owners:
        return "create"
    if len(exact) == 1 and not owners:
        return "enrich" if not any(
            item.get("authority") == "ror" for item in exact[0].get("identifiers", [])) else "reject"
    if len(exact) >= 2 and len(owners) == 1 and owners[0] in exact:
        return "merge"
    if len(owners) == 1:
        aliases = {
            (item.get("normalized_alias"), item.get("country_discriminator"))
            for item in owners[0].get("aliases", [])
        }
        return "alias" if (normalize_name(name), key[1]) not in aliases else "reject"
    return "reject"


def consolidate_pinned_roots(registry: Mapping[str, Any], *, timestamp: str,
                             actor: str = "pinned-root-consolidation") -> dict[str, Any]:
    """Merge exact pinned roots and preserve proposal endpoint history without accepting edges."""
    validate_registry(registry)
    result = copy.deepcopy(dict(registry))
    by_id = {item["organization_id"]: item for item in result["organizations"]}
    created_at = {
        event["payload"]["organization"]["organization_id"]: event["sequence"]
        for event in result["events"]
        if isinstance(event.get("payload"), Mapping)
        and isinstance(event["payload"].get("organization"), Mapping)
    }
    groups: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for organization in by_id.values():
        if organization.get("status") != "active":
            continue
        key = organization_identity_key(
            organization.get("canonical_name_en", ""), organization.get("country"),
            country_scope=organization.get("country_scope"),
        )
        if key is not None:
            groups.setdefault(key, []).append(organization)
    redirects = list(result.get("redirects", []))
    previous = result["event_head"]

    def merge_owned_rows(
            members: list[dict[str, Any]], field: str,
            key_fields: tuple[str, ...]) -> list[dict[str, Any]]:
        grouped: dict[tuple[Any, ...], list[tuple[str, dict[str, Any]]]] = {}
        for member in members:
            for row in member.get(field, []):
                grouped.setdefault(
                    tuple(row.get(name) for name in key_fields), []).append(
                        (member["organization_id"], row))
        merged_rows = []
        for _key, owned in sorted(grouped.items()):
            base = copy.deepcopy(min(
                (row for _owner, row in owned),
                key=lambda row: canonical_json_bytes(row)))
            owners = {
                owner for owner, _row in owned
                if owner != members[0]["organization_id"]
            }
            for _owner, row in owned:
                prior = row.get("prior_owner_organization_id")
                if isinstance(prior, str) and prior:
                    owners.add(prior)
                owners.update(
                    value for value in row.get("prior_owner_organization_ids", [])
                    if isinstance(value, str) and value)
            base.pop("prior_owner_organization_id", None)
            if owners:
                base["prior_owner_organization_ids"] = sorted(owners)
            merged_rows.append(base)
        return sorted(
            merged_rows, key=lambda row: tuple(
                str(row.get(name) or "") for name in key_fields))

    for key, members in sorted(groups.items()):
        if len(members) < 2:
            continue
        ror_values = {
            identifier.get("value")
            for item in members for identifier in item.get("identifiers", [])
            if identifier.get("authority") == "ror"
        }
        if len(ror_values) > 1:
            continue
        ror_owners = [
            item for item in members if any(
                identifier.get("authority") == "ror"
                for identifier in item.get("identifiers", []))
        ]
        survivor = min(ror_owners or members, key=lambda item: (
            created_at.get(item["organization_id"], float("inf")),
            item["organization_id"]))
        ordered_members = [survivor, *sorted(
            (item for item in members
             if item["organization_id"] != survivor["organization_id"]),
            key=lambda item: item["organization_id"])]
        losers = ordered_members[1:]
        loser_ids = {item["organization_id"] for item in losers}
        if any(
                edge.get("subject_organization_id") in loser_ids
                or edge.get("object_organization_id") in loser_ids
                for edge in result["relationships"]):
            continue
        merged = copy.deepcopy(survivor)
        merged["identifiers"] = merge_owned_rows(
            ordered_members, "identifiers", ("authority", "value"))
        merged["aliases"] = merge_owned_rows(
            ordered_members, "aliases",
            ("normalized_alias", "country_discriminator", "alias_id"))
        sequence = len(result["events"]) + 1
        event_id = _id(
            "pinned-root-consolidation", result["source_sha256"],
            f"{sequence}:{key[0]}:{key[1]}:{survivor['organization_id']}")
        redirect_rows = [
            {
                "from_organization_id": loser["organization_id"],
                "to_organization_id": survivor["organization_id"],
                "reason": "pinned_exact_name_country_consolidation",
                "event_id": event_id,
            }
            for loser in losers
        ]
        rewrites = []
        supersessions = []
        projected_proposals = []
        for proposal in result["relationship_proposals"]:
            if (
                    proposal.get("subject_organization_id") not in loser_ids
                    and proposal.get("object_organization_id") not in loser_ids):
                projected_proposals.append(proposal)
                continue
            before = copy.deepcopy(proposal)
            after = copy.deepcopy(proposal)
            after["subject_organization_id"] = (
                survivor["organization_id"]
                if proposal.get("subject_organization_id") in loser_ids
                else proposal.get("subject_organization_id"))
            after["object_organization_id"] = (
                survivor["organization_id"]
                if proposal.get("object_organization_id") in loser_ids
                else proposal.get("object_organization_id"))
            history = list(after.get("identity_endpoint_history", []))
            history.append({
                "event_id": event_id,
                "subject_organization_id": proposal.get("subject_organization_id"),
                "object_organization_id": proposal.get("object_organization_id"),
            })
            after["identity_endpoint_history"] = history
            change = {
                "relationship_id": proposal["relationship_id"],
                "before": before,
            }
            if after["subject_organization_id"] == after["object_organization_id"]:
                supersessions.append({
                    **change,
                    "reason": "identity_consolidation_self_relationship",
                })
            else:
                rewrites.append({**change, "after": after})
                projected_proposals.append(after)
        payload = {
            "identity_key": list(key),
            "survivor": merged,
            "loser_ids": sorted(loser_ids),
            "losers_before": copy.deepcopy(losers),
            "redirects": redirect_rows,
            "proposal_rewrites": sorted(
                rewrites, key=lambda row: row["relationship_id"]),
            "proposal_supersessions": sorted(
                supersessions, key=lambda row: row["relationship_id"]),
        }
        event = {
            "sequence": sequence,
            "event_id": event_id,
            "type": "pinned_root_consolidated",
            "timestamp": timestamp,
            "actor": actor,
            "policy_version": result["policy_version"],
            "previous_digest": previous,
            "payload": payload,
            "registry_contract_version": result.get(
                "registry_contract_version", REGISTRY_CONTRACT_VERSION),
            "event_contract_version": result.get(
                "event_contract_version", EVENT_CONTRACT_VERSION),
            "country_map_version": result.get(
                "country_map_version", COUNTRY_MAP_VERSION),
            "country_map_sha256": result.get(
                "country_map_sha256", COUNTRY_MAP_SHA256),
            "evidence_oracle_version": result.get(
                "evidence_oracle_version", EVIDENCE_ORACLE_VERSION),
            "evidence_oracle_sha256": result.get(
                "evidence_oracle_sha256", EVIDENCE_ORACLE_SHA256),
        }
        event["digest"] = _event_digest(event)
        previous = event["digest"]
        result["events"].append(event)
        result["relationship_proposals"] = sorted(
            projected_proposals, key=lambda row: row["relationship_id"])
        by_id[merged["organization_id"]] = merged
        for loser in losers:
            del by_id[loser["organization_id"]]
        redirects.extend(redirect_rows)
    result["organizations"] = sorted(
        by_id.values(), key=lambda item: item["organization_id"])
    result["alias_candidates"] = _identity_candidates(result["organizations"])
    result["redirects"] = sorted(redirects, key=lambda item: (
        item["from_organization_id"], item["to_organization_id"]))
    result["event_head"] = previous
    validate_registry(result)
    return result


def replay_identity_transition(event: Mapping[str, Any], organizations: list[dict[str, Any]]) -> None:
    """Replay create/enrich/alias/merge/reject/split identity projections."""
    payload = event.get("payload", {})
    if not isinstance(payload, Mapping):
        raise ValueError("identity transition payload must be an object")
    event_type = event.get("type")
    present = {organization["organization_id"] for organization in organizations}
    if event_type == "identity_rejected":
        if payload.get("reason") not in {
                "ambiguous", "conflicting_identifier", "missing_country",
                "unmappable_country", "provider_incomplete", "unsupported"}:
            raise ValueError("identity rejection requires a closed reason")
        return
    if event_type == "identity_created":
        after = payload.get("after")
        if not isinstance(after, Mapping) or after.get("organization_id") in present:
            raise ValueError("invalid identity create replay")
        after_key = organization_identity_key(
            after.get("canonical_name_en", ""), after.get("country"),
            country_scope=after.get("country_scope"),
        )
        if after.get("status") == "active" and after_key is not None and any(
                organization.get("status") == "active"
                and organization_identity_key(
                    organization.get("canonical_name_en", ""), organization.get("country"),
                    country_scope=organization.get("country_scope"),
                ) == after_key
                for organization in organizations):
            raise ValueError("identity create duplicates an active nonempty identity key")
        organizations.append(copy.deepcopy(dict(after)))
        return
    if event_type in {"identity_enriched", "identity_aliased"}:
        after = payload.get("after")
        if not isinstance(after, Mapping) or after.get("organization_id") not in present:
            raise ValueError("invalid identity enrich or alias replay")
        organizations[:] = [
            copy.deepcopy(dict(after)) if item["organization_id"] == after["organization_id"] else item
            for item in organizations
        ]
        return
    if event_type in {"pinned_root_consolidated", "identity_merged"}:
        survivor = payload.get("survivor")
        loser_ids = payload.get("loser_ids")
        if not isinstance(survivor, Mapping) or not isinstance(loser_ids, list):
            raise ValueError("malformed identity merge")
        if (survivor.get("organization_id") not in present
                or not set(loser_ids) <= present or survivor["organization_id"] in loser_ids):
            raise ValueError("identity merge references unknown organization")
        redirects = payload.get("redirects")
        expected_redirects = [
            {"from_organization_id": loser_id,
             "to_organization_id": survivor["organization_id"]}
            for loser_id in sorted(loser_ids)
        ]
        if (not isinstance(redirects, list)
                or [{key: row.get(key) for key in ("from_organization_id", "to_organization_id")}
                    for row in redirects] != expected_redirects):
            raise ValueError("identity merge requires direct redirects for every loser")
        organizations[:] = [
            item for item in organizations
            if item["organization_id"] not in set(loser_ids)
            and item["organization_id"] != survivor["organization_id"]
        ]
        organizations.append(copy.deepcopy(dict(survivor)))
        return
    if event_type == "identity_split":
        restored = payload.get("restored")
        merged_id = payload.get("merged_organization_id")
        if (not isinstance(restored, list) or not isinstance(merged_id, str)
                or merged_id not in present or not all(isinstance(item, Mapping) for item in restored)):
            raise ValueError("invalid identity split replay")
        organizations[:] = [item for item in organizations if item["organization_id"] != merged_id]
        organizations.extend(copy.deepcopy(dict(item)) for item in restored)
        return
    raise ValueError("unsupported identity transition event")
def append_identity_transition(registry: Mapping[str, Any], event_type: str,
                               payload: Mapping[str, Any], *, timestamp: str, actor: str,
                               expected_event_head: str) -> dict[str, Any]:
    """Append an exact-head guarded identity transition and replay its projection."""
    if event_type not in {
            "identity_created", "identity_enriched", "identity_aliased",
            "identity_merged", "identity_rejected", "identity_split"}:
        raise ValueError("unsupported identity transition")
    validate_registry(registry)
    if registry.get("event_head") != expected_event_head:
        raise ValueError("identity transition event head is stale")
    transition_payload = copy.deepcopy(dict(payload))
    if ("expected_event_head" in transition_payload
            and transition_payload["expected_event_head"] != registry["event_head"]):
        raise ValueError("identity transition expected event head is stale")
    transition_payload["expected_event_head"] = registry["event_head"]
    if event_type == "identity_merged":
        loser_ids = transition_payload.get("loser_ids")
        if not isinstance(loser_ids, list) or not loser_ids:
            raise ValueError("identity merge requires direct loser IDs")
        if any(edge.get("subject_organization_id") in loser_ids
               or edge.get("object_organization_id") in loser_ids
               for edge in registry["relationships"] + registry["relationship_proposals"]):
            raise ValueError("identity merge cannot rewire relationships")
        survivor = transition_payload.get("survivor")
        if not isinstance(survivor, Mapping):
            raise ValueError("identity merge requires a survivor projection")
        expected_redirects = [
            {"from_organization_id": loser_id,
             "to_organization_id": survivor.get("organization_id")}
            for loser_id in sorted(loser_ids)
        ]
        redirects = transition_payload.get("redirects")
        if (not isinstance(redirects, list)
                or [{key: row.get(key) for key in ("from_organization_id", "to_organization_id")}
                    for row in redirects] != expected_redirects):
            raise ValueError("identity merge requires one direct redirect per loser")
        losers_before = transition_payload.get("losers_before")
        if (
                not isinstance(losers_before, list)
                or sorted(row.get("organization_id") for row in losers_before)
                != sorted(loser_ids)):
            raise ValueError("identity merge requires complete loser before-state")
    if event_type == "identity_split":
        merge_event_id = transition_payload.get("merge_event_id")
        if (not isinstance(merge_event_id, str) or not registry["events"]
                or registry["events"][-1].get("event_id") != merge_event_id
                or registry["events"][-1].get("type") not in {
                    "identity_merged", "pinned_root_consolidated"}):
            raise ValueError("identity split requires the immediately preceding merge event")
        restored = transition_payload.get("restored")
        if (not isinstance(restored, list) or not restored
                or not all(isinstance(item, Mapping)
                           and isinstance(item.get("organization_id"), str) for item in restored)
                or len({item["organization_id"] for item in restored}) != len(restored)):
            raise ValueError("identity split requires a complete unique restoration")
    result = copy.deepcopy(dict(registry))
    event = {
        "sequence": len(result["events"]) + 1,
        "event_id": _id("identity-transition", result["source_sha256"],
                        f"{len(result['events']) + 1}:{event_type}:{canonical_sha256(transition_payload)}"),
        "type": event_type, "timestamp": timestamp, "actor": actor,
        "policy_version": result["policy_version"], "previous_digest": result["event_head"],
        "payload": transition_payload,
        "registry_contract_version": result.get("registry_contract_version", REGISTRY_CONTRACT_VERSION),
        "event_contract_version": result.get("event_contract_version", EVENT_CONTRACT_VERSION),
        "country_map_version": result.get("country_map_version", COUNTRY_MAP_VERSION),
        "country_map_sha256": result.get("country_map_sha256", COUNTRY_MAP_SHA256),
        "evidence_oracle_version": result.get(
            "evidence_oracle_version", EVIDENCE_ORACLE_VERSION),
        "evidence_oracle_sha256": result.get(
            "evidence_oracle_sha256", EVIDENCE_ORACLE_SHA256),
    }
    if event_type == "identity_merged":
        for redirect in transition_payload["redirects"]:
            redirect["event_id"] = event["event_id"]
    event["digest"] = _event_digest(event)
    result["events"].append(event)
    replayed = replay_registry(result)
    result["organizations"] = replayed["organizations"]
    result["alias_candidates"] = replayed["alias_candidates"]
    result["event_head"] = replayed["event_head"]
    if "redirects" in result or transition_payload.get("redirects"):
        result["redirects"] = replayed["redirects"]
    validate_registry(result)
    return result


def _canonical_identity_timestamp(value: Any) -> datetime:
    if not isinstance(value, str):
        raise ValueError("identity evidence timestamp missing")
    timestamp = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if timestamp.tzinfo is None:
        raise ValueError("identity evidence timestamp must include an offset")
    return timestamp.astimezone(timezone.utc)


def _strict_identity_candidate(row: Mapping[str, Any]) -> dict[str, Any]:
    """Validate the evaluator's sole automatic identity decision schema."""
    if (row.get("action") != "eligible_identity_only"
            or row.get("reason") != "dual_corroborated"
            or row.get("relationship") or row.get("relationship_payload")):
        raise ValueError("identity decision is not automatically eligible")
    expected_keys = {"query", "country", "action", "reason", "attempts_sha256", "decision_at", "candidate"}
    if set(row) != expected_keys:
        raise ValueError("identity decision schema is invalid")
    attempts_sha256 = row.get("attempts_sha256")
    if not isinstance(attempts_sha256, str) or not re.fullmatch(r"[0-9a-f]{64}", attempts_sha256):
        raise ValueError("identity decision digest is invalid")
    candidate = row.get("candidate")
    required = {
        "ror_id", "name", "country", "official_websites", "evidence",
        "evidence_oracle_version", "evidence_oracle_sha256",
    }
    if not isinstance(candidate, Mapping) or set(candidate) != required:
        raise ValueError("identity candidate schema is invalid")
    if (candidate.get("evidence_oracle_version") != EVIDENCE_ORACLE_VERSION
            or candidate.get("evidence_oracle_sha256") != EVIDENCE_ORACLE_SHA256):
        raise ValueError("identity candidate evidence oracle is invalid")
    query = row.get("query")
    if not isinstance(query, str) or not normalize_name(query):
        raise ValueError("identity query is invalid")
    ror_id = normalize_ror_id(candidate["ror_id"])
    name = nfc(candidate["name"])
    if name != " ".join(name.split()) or not normalize_name(name):
        raise ValueError("identity candidate name is invalid")
    if normalize_name(query) != normalize_name(name):
        raise ValueError("identity alias is not officially proven")
    country = canonical_country(candidate["country"])
    if not country or candidate["country"] != country:
        raise ValueError("identity candidate country is invalid")
    requested_country = canonical_country(row.get("country"))
    if requested_country != country:
        raise ValueError("identity country mismatch")
    websites_value = candidate["official_websites"]
    if not isinstance(websites_value, list) or not websites_value:
        raise ValueError("identity typed websites are invalid")
    websites = sorted({normalize_website_url(value) for value in websites_value})
    if websites != websites_value:
        raise ValueError("identity typed websites are not canonical")
    evidence = candidate["evidence"]
    if not isinstance(evidence, list) or len(evidence) != 2:
        raise ValueError("identity evidence is incomplete")
    if evidence != sorted(evidence, key=lambda item: (
            item["provider"], item["url"], item["retrieved_at"], item["payload_sha256"])):
        raise ValueError("identity evidence is not deterministic")
    expected_evidence_keys = {"provider", "retrieved_at", "payload_sha256", "url"}
    by_provider: dict[str, Mapping[str, Any]] = {}
    for item in evidence:
        if not isinstance(item, Mapping) or set(item) != expected_evidence_keys:
            raise ValueError("identity evidence schema is invalid")
        provider = item.get("provider")
        digest = item.get("payload_sha256")
        if (provider not in {"ror", "official"} or provider in by_provider
                or not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest)):
            raise ValueError("identity evidence is invalid")
        _canonical_identity_timestamp(item.get("retrieved_at"))
        by_provider[provider] = item
    ror_url = normalize_website_url(by_provider["ror"]["url"])
    official_url = normalize_website_url(by_provider["official"]["url"])
    if not ror_url.startswith("https://api.ror.org/v2/organizations?"):
        raise ValueError("identity evidence is not ROR v2")
    if official_url not in websites:
        raise ValueError("official evidence URL is not ROR typed")
    decision_at = _canonical_identity_timestamp(row.get("decision_at"))
    evidence_times = [_canonical_identity_timestamp(item["retrieved_at"]) for item in evidence]
    if any(item > decision_at or decision_at - item > timedelta(days=30) for item in evidence_times):
        raise ValueError("identity evidence is stale")
    return {
        "ror_id": ror_id, "name": name, "country": country,
        "official_websites": websites, "evidence": copy.deepcopy(evidence),
        "evidence_oracle_version": EVIDENCE_ORACLE_VERSION,
        "evidence_oracle_sha256": EVIDENCE_ORACLE_SHA256,
    }


def _automatic_identity_organization(registry: Mapping[str, Any], candidate: Mapping[str, Any],
                                     query: str) -> dict[str, Any]:
    """Create the minimal deterministic organization projection for strict ROR evidence."""
    ror_id = normalize_ror_id(candidate["ror_id"])
    name = nfc(candidate["name"])
    country = nfc(candidate["country"])
    organization_id = _id("ror", registry["source_sha256"], ror_id)
    alias_names = sorted({name, nfc(query)}, key=normalize_name)
    return {
        "organization_id": organization_id,
        "canonical_name_en": name,
        "normalized_name": normalize_name(name),
        "country": country,
        "organization_type": "other",
        "status": "active",
        "identifiers": [{"authority": "ror", "value": ror_id}],
        "aliases": [
            {"alias_id": _id("ror-alias", registry["source_sha256"],
                             f"{ror_id}:{normalize_name(alias)}"),
             "name": alias, "normalized_alias": normalize_name(alias),
             "country_discriminator": country}
            for alias in alias_names
        ],
        "websites": list(candidate["official_websites"]),
    }


def _identity_rejection(registry: Mapping[str, Any], *, query: str, country: Any,
                        reason: str, timestamp: str) -> dict[str, Any]:
    return append_identity_transition(
        registry, "identity_rejected",
        {"query": query, "country": country, "reason": reason},
        timestamp=timestamp, actor="automatic-identity-transition",
        expected_event_head=registry["event_head"],
    )


def apply_identity_transitions(registry: Mapping[str, Any], decisions: Iterable[Mapping[str, Any]], *,
                               timestamp: str, dry_run: bool = False) -> dict[str, Any]:
    """Apply strict identity-only ROR decisions; dry runs return the simulated projection."""
    validate_registry(registry)
    if (registry.get("import_mode") == "pinned_operator_curated"
            and not any(event.get("type") == "relationship_policy_transition"
                        for event in registry["events"])):
        raise ValueError("automatic identity transitions require the relationship-policy transition")
    rows = list(decisions)
    if not all(isinstance(row, Mapping) for row in rows):
        raise ValueError("identity decisions must be objects")
    ordered = sorted(rows, key=lambda row: (
        str(row.get("query", "")), str(row.get("country", "")), canonical_sha256(row)))
    if len({(row.get("query"), row.get("country")) for row in ordered}) != len(ordered):
        raise ValueError("identity decisions must have unique query and country keys")
    result = copy.deepcopy(dict(registry))
    resolutions: list[dict[str, Any]] = []
    for row in ordered:
        query, requested_country = row.get("query"), row.get("country")
        action, organization_id, reason = "reject", None, "provider_incomplete"
        try:
            strict_candidate = _strict_identity_candidate(row)
        except (KeyError, TypeError, ValueError):
            result = _identity_rejection(
                result, query=query if isinstance(query, str) else "", country=requested_country,
                reason=reason, timestamp=timestamp)
        else:
            requested_state, requested_code = country_resolution(requested_country)
            reason = "dual_corroborated"
            candidate_state, candidate_code = country_resolution(strict_candidate["country"])
            websites = strict_candidate["official_websites"]
            ror_id = strict_candidate["ror_id"]
            name = strict_candidate["name"]
            if requested_state != "present" or candidate_state != "present":
                reason = "missing_country" if (
                    requested_state == "missing" or candidate_state == "missing") else "unmappable_country"
                result = _identity_rejection(result, query=query, country=requested_country,
                                             reason=reason, timestamp=timestamp)
            elif requested_code != candidate_code:
                result = _identity_rejection(result, query=query, country=requested_country,
                                             reason="provider_incomplete", timestamp=timestamp)
            else:
                action = identity_transition_action(
                    result["organizations"], name=name, country=strict_candidate["country"],
                    ror_id=ror_id, typed_websites=websites)
                key = organization_identity_key(name, strict_candidate["country"])
                exact = [item for item in result["organizations"] if item.get("status") == "active"
                         and organization_identity_key(item.get("canonical_name_en", ""),
                                                       item.get("country"),
                                                       country_scope=item.get("country_scope")) == key]
                owners = [item for item in result["organizations"] if item.get("status") == "active"
                          and any(identifier.get("authority") == "ror"
                                  and identifier.get("value") == ror_id
                                  for identifier in item.get("identifiers", []))]
                if action == "merge":
                    loser_ids = {item["organization_id"] for item in exact
                                 if item["organization_id"] != owners[0]["organization_id"]}
                    if any(edge.get("subject_organization_id") in loser_ids
                           or edge.get("object_organization_id") in loser_ids
                           for edge in result["relationships"] + result["relationship_proposals"]):
                        action, reason = "reject", "relationship_payload_requires_review"
                if action == "create":
                    after = _automatic_identity_organization(result, strict_candidate, query)
                    organization_id = after["organization_id"]
                    payload = {"after": after, "query": query, "country": requested_country,
                               "candidate": strict_candidate}
                    result = append_identity_transition(
                        result, "identity_created", payload, timestamp=timestamp,
                        actor="automatic-identity-transition", expected_event_head=result["event_head"])
                elif action == "enrich":
                    after = copy.deepcopy(exact[0])
                    after["status"] = "active"
                    after["identifiers"].append({"authority": "ror", "value": ror_id})
                    after["identifiers"].sort(key=lambda item: (item["authority"], item["value"]))
                    after["websites"] = sorted(set(after.get("websites", [])) | set(websites))
                    organization_id = after["organization_id"]
                    result = append_identity_transition(
                        result, "identity_enriched",
                        {"after": after, "query": query, "country": requested_country,
                         "candidate": strict_candidate},
                        timestamp=timestamp, actor="automatic-identity-transition",
                        expected_event_head=result["event_head"])
                elif action == "alias":
                    after = copy.deepcopy(owners[0])
                    alias_name = name
                    after["aliases"].append({
                        "alias_id": _id("ror-alias", result["source_sha256"],
                                        f"{ror_id}:{normalize_name(alias_name)}"),
                        "name": alias_name, "normalized_alias": normalize_name(alias_name),
                        "country_discriminator": after["country"],
                    })
                    after["aliases"].sort(key=lambda item: (
                        item["normalized_alias"], item["country_discriminator"], item["alias_id"]))
                    organization_id = after["organization_id"]
                    result = append_identity_transition(
                        result, "identity_aliased",
                        {"after": after, "query": query, "country": requested_country,
                         "candidate": strict_candidate},
                        timestamp=timestamp, actor="automatic-identity-transition",
                        expected_event_head=result["event_head"])
                elif action == "merge":
                    created_sequence = {}
                    for event in result["events"]:
                        payload = event.get("payload")
                        if not isinstance(payload, Mapping):
                            continue
                        created = payload.get("after", payload.get("organization"))
                        if isinstance(created, Mapping) and isinstance(created.get("organization_id"), str):
                            created_sequence.setdefault(created["organization_id"], event["sequence"])
                    survivor = copy.deepcopy(min(
                        exact,
                        key=lambda item: (created_sequence.get(item["organization_id"], float("inf")),
                                          item["organization_id"]),
                    ))
                    losers = sorted((item for item in exact
                                     if item["organization_id"] != survivor["organization_id"]),
                                    key=lambda item: item["organization_id"])
                    identifiers = list(survivor["identifiers"])
                    aliases = list(survivor["aliases"])
                    for loser in losers:
                        identifiers.extend(dict(identifier,
                                                prior_owner_organization_id=loser["organization_id"])
                                           for identifier in loser["identifiers"])
                        aliases.extend(dict(alias, prior_owner_organization_id=loser["organization_id"])
                                       for alias in loser["aliases"])
                    identifier_rows = {}
                    for identifier in identifiers:
                        identifier_rows.setdefault(
                            (identifier["authority"], identifier["value"]), identifier)
                    alias_rows = {}
                    for alias in aliases:
                        alias_rows.setdefault(
                            (alias["normalized_alias"], alias["country_discriminator"]), alias)
                    survivor["identifiers"] = sorted(
                        identifier_rows.values(),
                        key=lambda item: (item["authority"], item["value"],
                                          item.get("prior_owner_organization_id", "")))
                    survivor["aliases"] = sorted(
                        alias_rows.values(),
                        key=lambda item: (item["normalized_alias"], item["country_discriminator"],
                                          item["alias_id"], item.get("prior_owner_organization_id", "")))
                    organization_id = survivor["organization_id"]
                    redirects = [{"from_organization_id": item["organization_id"],
                                  "to_organization_id": organization_id,
                                  "reason": "exact_name_country_ror_consolidation"} for item in losers]
                    result = append_identity_transition(
                        result, "identity_merged",
                        {"survivor": survivor,
                         "loser_ids": [item["organization_id"] for item in losers],
                         "losers_before": copy.deepcopy(losers),
                         "redirects": redirects, "query": query,
                         "country": requested_country, "candidate": strict_candidate},
                        timestamp=timestamp, actor="automatic-identity-transition",
                        expected_event_head=result["event_head"])
                else:
                    action, reason = "reject", "ambiguous"
                    result = _identity_rejection(result, query=query, country=requested_country,
                                                 reason=reason, timestamp=timestamp)
        resolutions.append({"query": query if isinstance(query, str) else "",
                            "country": requested_country, "action": action,
                            "organization_id": organization_id, "reason": reason})
    return {"registry": result, "resolutions": resolutions}

def resolve_organization_redirect(registry: Mapping[str, Any], organization_id: str) -> str:
    """Resolve one direct immutable consolidation redirect, or return the input."""
    redirects = {
        item["from_organization_id"]: item["to_organization_id"]
        for item in registry.get("redirects", [])
        if isinstance(item, Mapping)
        and isinstance(item.get("from_organization_id"), str)
        and isinstance(item.get("to_organization_id"), str)
    }
    target = redirects.get(organization_id, organization_id)
    if target in redirects:
        raise ValueError("organization redirects must be direct")
    return target

def alias_candidate_lookup(registry: Mapping[str, Any], name: str, country: str = "") -> list[dict[str, Any]]:
    """Return all accepted identity candidates; collisions intentionally remain plural."""
    normalized = normalize_name(name)
    return [candidate for candidate in registry["alias_candidates"]
            if candidate["normalized_alias"] == normalized
            and (not country or candidate["country_discriminator"] == country)]




def baseline_projection(registry: Mapping[str, Any], corrections: Iterable[Mapping[str, Any]], *,
                        effective_date: str) -> dict[str, Any]:
    """Build deterministic baseline metrics from registry and correction projection."""
    rows = list(corrections)
    proposals = registry["relationship_proposals"]
    pending_count = len(proposals)
    replacement_categories = Counter(
        token["category"] for row in rows for token in row.get("af_id_replace_tokens", [])
    )
    return {"schema_version": REGISTRY_SCHEMA_VERSION, "effective_date": effective_date,
            "registry_sha256": canonical_sha256(registry), "policy_version": registry["policy_version"],
            "source_sha256": registry["source_sha256"], "current_observation_count": len(rows),
            "registry_contract_version": registry.get("registry_contract_version", ""),
            "event_contract_version": registry.get("event_contract_version", ""),
            "country_map_version": registry.get("country_map_version", ""),
            "country_map_sha256": registry.get("country_map_sha256", ""),
            "evidence_oracle_version": registry.get("evidence_oracle_version", ""),
            "evidence_oracle_sha256": registry.get("evidence_oracle_sha256", ""),
            "event_head": registry.get("event_head", ""),
            "ledger_head": registry.get("ledger_head", ""),
            "cohort_version": registry.get("cohort_version", ""),
            "cohort_sha256": registry.get("cohort_sha256", ""),
            "accepted_identity_alias_count": len(registry["alias_candidates"]),
            "accepted_identity_alias_organization_count": len({
                candidate["organization_id"]
                for candidate in registry["alias_candidates"]}),
            "proposed_relationship_edge_count": len(proposals),
            "accepted_official_relationship_edge_count": len(registry["relationships"]),
            "active_pending_total": pending_count,
            "lifetime_pending_total": pending_count,
            "pending_relationship_evidence_count": pending_count,
            "pending_reason_counts": (
                {"official_evidence_pending": pending_count}
                if pending_count else {}
            ),
            "oldest_active_age_days": 0, "identity_country_mismatches": 0,
            "relationships_by_official_evidence_tier": {}, "group_shares": {},
            "relationship_cardinality_histogram": {"0": len(rows)},
            "database_baseline": {},
            "correction_reconciliation": {"source_keys": len(rows), "correction_rows": len(rows),
                                          "replacement_token_categories": dict(sorted(replacement_categories.items())),
                                          "complete": len(rows) == len(set(row["source_key"] for row in rows))}}
def compatibility_parent_id(registry: Mapping[str, Any], organization_id: str) -> str | None:
    """Return the one current `part_of` parent; JV operators never provide parentage."""
    parents = [
        edge["object_organization_id"] for edge in relationship_lookup(registry, organization_id, "part_of")
        if edge.get("status") == "accepted"
    ]
    if len(parents) > 1:
        raise ValueError("multiple current part_of parents")
    return parents[0] if parents else None


def relationship_group_id(registry: Mapping[str, Any], organization_id: str) -> str:
    """Compatibility grouping follows accepted `part_of` edges only."""
    parent = compatibility_parent_id(registry, organization_id)
    return parent or organization_id


def jointly_operated_by(registry: Mapping[str, Any], organization_id: str) -> tuple[str, ...]:
    """Return all JV operators without treating any of them as a hierarchy parent."""
    return tuple(sorted(
        edge["object_organization_id"]
        for edge in relationship_lookup(registry, organization_id, "jointly_operated_by")
        if edge.get("status") == "accepted"
    ))


def validate_country_event(event: Mapping[str, Any]) -> None:
    """Validate the immutable payload required for map migrations and corrections."""
    event_type, payload = event.get("type"), event.get("payload")
    if event_type not in {"country_map_changed", "country_corrected"} or not isinstance(payload, Mapping):
        raise ValueError("unsupported country event")
    if event_type == "country_map_changed":
        required = {"old_version", "new_version", "old_sha256", "new_sha256", "old_source_sha256",
                    "new_source_sha256", "added_rows", "removed_rows", "changed_rows",
                    "added_aliases", "removed_aliases", "changed_aliases", "approvals",
                    "effective_at", "affected_organization_ids", "affected_observation_ids"}
    else:
        required = {"organization_id", "old_country", "new_country", "basis", "evidence_ids",
                    "before", "after"}
        if canonical_country(payload.get("new_country")) is None:
            raise ValueError("country correction must name a current ISO country")
    if required - set(payload):
        raise ValueError("country event payload is incomplete")
    if event_type == "country_map_changed" and (
            not isinstance(payload.get("approvals"), list) or not payload["approvals"]):
        raise ValueError("country map change requires approvals")


class RegistryStore:
    """Read-only deterministic access to one registry snapshot and its bound heads."""

    def __init__(self, registry: Mapping[str, Any]) -> None:
        validate_registry(registry)
        self._registry = copy.deepcopy(dict(registry))
        self._organizations = {
            item["organization_id"]: item for item in self._registry["organizations"]
        }
        self._by_ror = {}
        self._by_domain = {}
        self._by_identity = {}
        for organization in self._organizations.values():
            for identifier in organization.get("identifiers", []):
                if identifier.get("authority") == "ror":
                    self._by_ror[normalize_ror_id(identifier["value"])] = organization["organization_id"]
            key = organization_identity_key(
                organization.get("canonical_name_en", ""), organization.get("country"),
                country_scope=organization.get("country_scope"),
            )
            if key:
                self._by_identity.setdefault(key, []).append(organization["organization_id"])
            for website in organization.get("websites", []):
                try:
                    domain = urlsplit(normalize_website_url(website)).hostname
                except ValueError:
                    continue
                self._by_domain.setdefault(domain, []).append(organization["organization_id"])
        self._by_identity = {key: tuple(sorted(value)) for key, value in self._by_identity.items()}
        self._by_domain = {key: tuple(sorted(value)) for key, value in self._by_domain.items()}

    @property
    def registry_head(self) -> str:
        return canonical_sha256(self._registry)

    @property
    def event_head(self) -> str:
        return self._registry["event_head"]

    @property
    def ledger_head(self) -> str | None:
        return self._registry.get("ledger_head")

    @property
    def cohort_head(self) -> str | None:
        return self._registry.get("cohort_head")

    @property
    def current_heads(self) -> Mapping[str, str | None]:
        return MappingProxyType({
            "registry": self.registry_head, "event": self.event_head,
            "ledger": self.ledger_head, "cohort": self.cohort_head,
        })

    def registry(self) -> Mapping[str, Any]:
        return MappingProxyType(copy.deepcopy(self._registry))

    def organization(self, organization_id: str) -> Mapping[str, Any] | None:
        organization = self._organizations.get(organization_id)
        return MappingProxyType(copy.deepcopy(organization)) if organization else None

    def by_ror_id(self, ror_id: str) -> Mapping[str, Any] | None:
        try:
            organization_id = self._by_ror.get(normalize_ror_id(ror_id))
        except ValueError:
            return None
        return self.organization(organization_id) if organization_id else None

    def by_domain(self, domain_or_url: str) -> tuple[Mapping[str, Any], ...]:
        try:
            domain = urlsplit(normalize_website_url(domain_or_url)).hostname
        except ValueError:
            domain = domain_or_url.strip().casefold()
        return tuple(self.organization(identifier) for identifier in self._by_domain.get(domain, ()))

    def by_normalized_name(self, name: str, country: str | None) -> tuple[Mapping[str, Any], ...]:
        key = organization_identity_key(name, country)
        return tuple(self.organization(identifier) for identifier in self._by_identity.get(key, ())) if key else ()
