"""ISO 3166-1 country map for the bibliography DB.

Extracted verbatim from ``lib/affiliation_registry.py`` when the affiliation
organisation registry was retired. The registry resolved nothing —
``institutions.organization_id`` was NULL for every row — but this closed
country table is the tool that fills ``institutions.country_name_en``, which is
still empty for the whole corpus, so it outlives the registry it shipped in.

The embedded digest guard is kept: the map is a pinned snapshot, not editable data.
"""
import hashlib
import json
import unicodedata
from types import MappingProxyType
from typing import Any


def nfc(value: str) -> str:
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
