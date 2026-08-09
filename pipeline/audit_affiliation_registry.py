#!/usr/bin/env python3
"""Create and audit the deterministic offline affiliation registry.

Import is the only command that writes accepted registry artifacts.  Network
resolution is proposal-only and never edits the accepted registry.
"""
from __future__ import annotations

import argparse
import base64
import gzip
import hashlib
import io
import html.parser
import ipaddress
import json
import re
import os
import socket
import ssl
from jsonschema import Draft7Validator
import idna
import sqlite3
import sys
import tempfile
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from datetime import UTC, datetime, timedelta
from pathlib import Path
from urllib.parse import urlencode, urljoin, urlsplit, urlunsplit
from typing import Any
import lib.affiliation_registry as affiliation_registry

from lib.affiliation_registry import (
    SOURCE_SHA256,
    baseline_projection,
    build_registry,
    canonical_country,
    canonical_json_bytes,
    canonical_sha256,
    correction_projection,
    is_generic_fragment,
    load_registry,
    nfc,
    normalize_name,
    normalize_ror_id,
    normalize_website_url,
    promote_approved,
    ror_exact_candidates,
    transition_relationship_policy,
    validate_registry,
)

ROR_V2_ENDPOINT = affiliation_registry.EVIDENCE_ORACLE_MANIFEST["ror"]["endpoint"]
ROR_SCHEMA_VERSION = affiliation_registry.EVIDENCE_ORACLE_MANIFEST["ror"]["schema_version"]
ROR_SCHEMA_COMMIT = affiliation_registry.EVIDENCE_ORACLE_MANIFEST["ror"]["schema_commit"]
PSL_VERSION = affiliation_registry.EVIDENCE_ORACLE_MANIFEST["psl"]["version"]
PSL_COMMIT = affiliation_registry.EVIDENCE_ORACLE_MANIFEST["psl"]["commit"]
MAX_ROR_PAGES = affiliation_registry.EVIDENCE_ORACLE_MANIFEST["ror"]["max_pages"]
MAX_ROR_RECORDS = affiliation_registry.EVIDENCE_ORACLE_MANIFEST["ror"]["max_records"]
MAX_REDIRECTS = affiliation_registry.EVIDENCE_ORACLE_MANIFEST["official_https"]["max_redirects"]
CONNECT_TIMEOUT_SECONDS = affiliation_registry.EVIDENCE_ORACLE_MANIFEST["official_https"]["connect_timeout_seconds"]
READ_TIMEOUT_SECONDS = affiliation_registry.EVIDENCE_ORACLE_MANIFEST["official_https"]["read_idle_timeout_seconds"]
TOTAL_TIMEOUT_SECONDS = affiliation_registry.EVIDENCE_ORACLE_MANIFEST["official_https"]["total_timeout_seconds"]
MAX_WIRE_BYTES = affiliation_registry.EVIDENCE_ORACLE_MANIFEST["official_https"]["wire_bytes_per_response"]
MAX_DECODED_BYTES = affiliation_registry.EVIDENCE_ORACLE_MANIFEST["official_https"]["decoded_bytes_per_response"]
MAX_QUOTE_BYTES = affiliation_registry.EVIDENCE_ORACLE_MANIFEST["official_https"]["quote_bytes"]
MAX_TOTAL_QUOTE_BYTES = affiliation_registry.EVIDENCE_ORACLE_MANIFEST["official_https"]["total_quote_bytes"]
EVIDENCE_FRESHNESS_DAYS = 30
ORACLE_MANIFEST_VERSION = affiliation_registry.EVIDENCE_ORACLE_VERSION


class _PageExtractor(html.parser.HTMLParser):
    """Collect separate deterministic identity-bearing fields without retaining a page."""

    _SUPPRESSED = {"style", "template", "noscript"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._stack: list[tuple[str, tuple[str, int] | None]] = []
        self._parts: dict[str, list[list[str]]] = {
            "title": [], "h1": [], "jsonld": [], "legal": [],
        }

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        attributes = {key.lower(): value or "" for key, value in attrs}
        inherited = self._stack[-1][1] if self._stack else None
        capture: tuple[str, int] | None = inherited
        if tag == "script":
            capture = None
            if attributes.get("type", "").casefold() == "application/ld+json":
                self._parts["jsonld"].append([])
                capture = ("jsonld", len(self._parts["jsonld"]) - 1)
        elif tag in self._SUPPRESSED:
            capture = None
        elif tag in {"title", "h1"}:
            self._parts[tag].append([])
            capture = (tag, len(self._parts[tag]) - 1)
        elif (tag in {"address", "footer"}
              or any(token in (attributes.get("id", "") + " " + attributes.get("class", "")).casefold()
                     for token in ("legal", "contact", "organization", "organisation"))):
            self._parts["legal"].append([])
            capture = ("legal", len(self._parts["legal"]) - 1)
        self._stack.append((tag, capture))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        while self._stack:
            opened, _ = self._stack.pop()
            if opened == tag:
                break

    def handle_data(self, data: str) -> None:
        if self._stack and self._stack[-1][1]:
            key, index = self._stack[-1][1]
            self._parts[key][index].append(data)

    def values(self) -> dict[str, list[str]]:
        values: dict[str, list[str]] = {}
        for key, rows in self._parts.items():
            normalized = [
                " ".join(unicodedata.normalize("NFC", "".join(parts)).split())
                for parts in rows
            ]
            if kept := [value for value in normalized if value]:
                values[key] = kept
        return values


def _require_no_proxy() -> None:
    if any(os.environ.get(key) for key in (
            "http_proxy", "https_proxy", "all_proxy", "HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY")):
        raise ValueError("proxy environment is forbidden for affiliation evidence")


def _public_addresses(hostname: str, port: int) -> tuple[str, ...]:
    addresses = {item[4][0] for item in socket.getaddrinfo(
        hostname, port, type=socket.SOCK_STREAM)}
    if not addresses:
        raise ValueError("DNS returned no addresses")
    try:
        parsed = [ipaddress.ip_address(address) for address in addresses]
    except ValueError as exc:
        raise ValueError("DNS returned invalid address") from exc
    if not all(address.is_global and (
            not isinstance(address, ipaddress.IPv6Address)
            or address.ipv4_mapped is None
            or address.ipv4_mapped.is_global)
            for address in parsed):
        raise ValueError("DNS returned mixed or non-public addresses")
    return tuple(str(address) for address in sorted(
        parsed, key=lambda value: (value.version, value.packed)))


def _canonical_https_url(value: str) -> tuple[str, str]:
    try:
        parsed = urlsplit(value)
        port = parsed.port or 443
    except (TypeError, ValueError) as exc:
        raise ValueError("malformed HTTPS evidence URL") from exc
    if (parsed.scheme != "https" or not parsed.hostname or port != 443
            or parsed.username or parsed.password):
        raise ValueError("only credential-free HTTPS port 443 URLs are allowed")
    try:
        ipaddress.ip_address(parsed.hostname)
    except ValueError:
        pass
    else:
        raise ValueError("IP-literal evidence URLs are forbidden")
    try:
        hostname = idna.encode(parsed.hostname, uts46=False, std3_rules=True).decode("ascii").lower()
    except idna.IDNAError as exc:
        raise ValueError("invalid IDNA2008 hostname") from exc
    url = urlunsplit(("https", hostname, parsed.path or "/", parsed.query, ""))
    return url, hostname


def _psl_rules(oracle_dir: Path) -> tuple[set[str], set[str], set[str]]:
    raw = _oracle_artifact_path(oracle_dir, "psl").read_text(encoding="utf-8")
    exact: set[str] = set()
    wildcard: set[str] = set()
    exception: set[str] = set()
    for source_line in raw.splitlines():
        line = source_line.strip().casefold()
        if not line or line.startswith("//"):
            continue
        if line.startswith("!"):
            exception.add(line[1:])
        elif line.startswith("*."):
            wildcard.add(line[2:])
        else:
            exact.add(line)
    if not exact or not wildcard or not exception:
        raise ValueError("PSL parser did not load exact, wildcard, and exception rules")
    return exact, wildcard, exception


def _registrable_domain(hostname: str, rules: tuple[set[str], set[str], set[str]]) -> str:
    labels = hostname.casefold().rstrip(".").split(".")
    exact, wildcard, exceptions = rules
    exception_matches = [
        rule for rule in exceptions
        if labels[-len(rule.split(".")):] == rule.split(".")
    ]
    if exception_matches:
        public_suffix_labels = len(max(
            exception_matches, key=lambda item: len(item.split("."))).split(".")) - 1
    else:
        lengths = [1]
        for index in range(len(labels)):
            suffix = ".".join(labels[index:])
            if suffix in exact:
                lengths.append(len(labels) - index)
            if index + 1 < len(labels) and ".".join(labels[index + 1:]) in wildcard:
                lengths.append(len(labels) - index)
        public_suffix_labels = max(lengths)
    if len(labels) <= public_suffix_labels:
        raise ValueError("hostname has no registrable domain under pinned PSL")
    return ".".join(labels[-(public_suffix_labels + 1):])


def _bounded_decode(raw: bytes, encoding: str, maximum: int) -> bytes:
    if encoding in {"", "identity"}:
        decoded = raw
    elif encoding == "gzip":
        try:
            with gzip.GzipFile(fileobj=io.BytesIO(raw)) as stream:
                decoded = stream.read(maximum + 1)
        except OSError as exc:
            raise ValueError("invalid gzip response") from exc
    else:
        raise ValueError("unsupported content encoding")
    if len(decoded) > maximum:
        raise ValueError("decoded response exceeds limit")
    return decoded


_CHARSET_ALIASES = {
    "utf-8": "utf-8", "utf8": "utf-8",
    "windows-1252": "windows-1252", "cp1252": "windows-1252",
    "iso-8859-1": "iso-8859-1", "latin1": "iso-8859-1",
}


def _content_type(headers: Any, expected: str, raw: bytes) -> tuple[str, str]:
    value = headers.get("content-type", headers.get("Content-Type", ""))
    parts = [part.strip() for part in value.split(";")]
    media = parts[0].casefold()
    accepted = ({"application/json"} if expected == "application/json" else
                set(affiliation_registry.EVIDENCE_ORACLE_MANIFEST[
                    "official_https"]["accepted_media_types"]))
    if media not in accepted:
        raise ValueError(f"unsupported content type: {media or 'missing'}")
    http_labels = {
        item.strip().strip('"').casefold()
        for part in parts[1:]
        for key, separator, item in [part.partition("=")]
        if separator and key.strip().casefold() == "charset"
    }
    if len(http_labels) > 1:
        raise ValueError("multiple HTTP charset declarations")
    meta_labels = {
        match.decode("ascii").casefold()
        for match in re.findall(
            rb"(?i)(?:charset\s*=\s*[\"']?\s*)([A-Za-z0-9._-]+)",
            raw[:1024])
    } if media == "text/html" else set()
    if len(meta_labels) > 1:
        raise ValueError("multiple HTML charset declarations")
    if raw.startswith(b"\xef\xbb\xbf"):
        charset = "utf-8"
        if http_labels and next(iter(http_labels)) not in {"utf-8", "utf8"}:
            raise ValueError("BOM and HTTP charset disagree")
    else:
        http_charset = _CHARSET_ALIASES.get(next(iter(http_labels)), "") if http_labels else ""
        meta_charset = _CHARSET_ALIASES.get(next(iter(meta_labels)), "") if meta_labels else ""
        if http_labels and not http_charset or meta_labels and not meta_charset:
            raise ValueError("unsupported charset")
        if http_charset and meta_charset and http_charset != meta_charset:
            raise ValueError("HTTP and HTML charset disagree")
        charset = http_charset or meta_charset or "utf-8"
    if media in {"application/json", "application/ld+json", "application/xhtml+xml"} and charset != "utf-8":
        raise ValueError("structured media requires UTF-8")
    return media, charset


def _bounded_direct_https(url: str, expected_content_type: str, *,
                          oracle_dir: Path) -> tuple[bytes, dict[str, Any]]:
    """Dial only vetted IPs while retaining original-host TLS, certificate, and Host."""
    _require_no_proxy()
    _oracle_manifest(oracle_dir)
    import http.client
    profile = "ror" if expected_content_type == "application/json" else "official_https"
    settings = affiliation_registry.EVIDENCE_ORACLE_MANIFEST[profile]
    wire_per_response = settings.get("wire_bytes_per_page",
                                     settings.get("wire_bytes_per_response"))
    wire_per_chain = settings.get("wire_bytes_per_page",
                                  settings.get("wire_bytes_per_chain"))
    decoded_per_response = settings.get("decoded_bytes_per_page",
                                        settings.get("decoded_bytes_per_response"))
    decoded_per_chain = settings.get("decoded_bytes_per_page",
                                     settings.get("decoded_bytes_per_chain"))
    read_timeout = settings["read_idle_timeout_seconds"]
    total_timeout = settings["total_timeout_seconds"]
    started = time.monotonic()
    current, original_host = _canonical_https_url(url)
    rules = _psl_rules(oracle_dir)
    original_domain = _registrable_domain(original_host, rules)
    redirects, verdicts, wire_total, decoded_total = 0, [], 0, 0
    while True:
        remaining = total_timeout - (time.monotonic() - started)
        if remaining <= 0:
            raise ValueError("total request timeout")
        current, hostname = _canonical_https_url(current)
        if _registrable_domain(hostname, rules) != original_domain:
            raise ValueError("cross-registrable-domain redirect")
        if profile == "ror" and hostname != original_host:
            raise ValueError("ROR redirect changed origin")
        addresses = _public_addresses(hostname, 443)
        connection = None
        selected = ""
        last_error: OSError | None = None
        for address in addresses:
            try:
                raw_socket = socket.create_connection(
                    (address, 443),
                    timeout=min(settings["connect_timeout_seconds"], remaining))
                context = ssl.create_default_context()
                wrapped = context.wrap_socket(raw_socket, server_hostname=hostname)
                wrapped.settimeout(min(read_timeout, max(
                    0.001, total_timeout - (time.monotonic() - started))))
                connection = http.client.HTTPSConnection(
                    hostname, 443, timeout=read_timeout, context=context)
                connection.sock = wrapped
                selected = address
                break
            except OSError as exc:
                last_error = exc
        if connection is None:
            raise OSError("all vetted HTTPS addresses failed") from last_error
        try:
            parsed = urlsplit(current)
            connection.request(
                "GET", urlunsplit(("", "", parsed.path or "/", parsed.query, "")),
                headers={"Host": hostname, "User-Agent": "affiliation-registry-audit/2",
                         "Accept-Encoding": "gzip"})
            response = connection.getresponse()
            wire = response.read(wire_per_response + 1)
            status = response.status
            headers = {key.casefold(): value for key, value in response.getheaders()}
        finally:
            connection.close()
        if len(wire) > wire_per_response:
            raise ValueError("wire response exceeds per-response limit")
        wire_total += len(wire)
        if wire_total > wire_per_chain:
            raise ValueError("wire response exceeds chain limit")
        verdicts.append({
            "url": current, "hostname": hostname, "addresses": list(addresses),
            "selected_ip": selected, "status": status, "tls_hostname_verified": True,
            "host_header": hostname, "proxy": "PROXY_DISABLED",
        })
        if status in {301, 302, 303, 307, 308}:
            location = headers.get("location", "")
            if redirects >= MAX_REDIRECTS or not location:
                raise ValueError("redirect limit exceeded")
            current, redirects = urljoin(current, location), redirects + 1
            continue
        if not 200 <= status < 300:
            raise ValueError(f"unexpected HTTP status: {status}")
        decoded = _bounded_decode(
            wire, headers.get("content-encoding", "").casefold(),
            decoded_per_response)
        media, charset = _content_type(headers, expected_content_type, decoded)
        decoded_total += len(decoded)
        if decoded_total > decoded_per_chain:
            raise ValueError("decoded response exceeds chain limit")
        if time.monotonic() - started > total_timeout:
            raise ValueError("total request timeout")
        text = decoded.decode(charset, errors="strict")
        if "\x00" in text or "\ufffd" in text:
            raise ValueError("decoded response contains forbidden characters")
        if decoded.startswith(b"\xef\xbb\xbf"):
            decoded = decoded[3:]
        return decoded, {
            "final_url": current, "registrable_domain": original_domain,
            "headers": headers, "media_type": media, "charset": charset,
            "redirects": verdicts, "wire_bytes": wire_total,
            "decoded_bytes": decoded_total,
        }


def _quote(value: str) -> dict[str, str]:
    raw = value.encode("utf-8")
    if len(raw) > MAX_QUOTE_BYTES:
        raise ValueError("evidence quote exceeds limit")
    return {"quote": value, "quote_sha256": hashlib.sha256(raw).hexdigest()}


def _oracle_artifact_path(oracle_dir: Path, section: str) -> Path:
    entry = affiliation_registry.EVIDENCE_ORACLE_MANIFEST[section]
    return oracle_dir / entry["schema_path" if section == "ror" else "path"]


def _validate_oracle_artifacts(oracle_dir: Path) -> None:
    schema_path = _oracle_artifact_path(oracle_dir, "ror")
    psl_path = _oracle_artifact_path(oracle_dir, "psl")
    if (not schema_path.is_file()
            or hashlib.sha256(schema_path.read_bytes()).hexdigest()
            != affiliation_registry.EVIDENCE_ORACLE_MANIFEST["ror"]["schema_sha256"]):
        raise ValueError("oracle artifact hash mismatch: ror_schema_v2_1.json")
    if (not psl_path.is_file()
            or hashlib.sha256(psl_path.read_bytes()).hexdigest()
            != affiliation_registry.EVIDENCE_ORACLE_MANIFEST["psl"]["sha256"]):
        raise ValueError("oracle artifact hash mismatch: public_suffix_list.dat")
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    Draft7Validator.check_schema(schema)
    psl = psl_path.read_text(encoding="utf-8")
    if (not all(marker in psl for marker in (
                "Mozilla Public", "License, v. 2.0",
                "// ===BEGIN ICANN DOMAINS===",
                "// ===END ICANN DOMAINS===",
                "// ===BEGIN PRIVATE DOMAINS===",
                "// ===END PRIVATE DOMAINS==="))):
        raise ValueError("PSL license or required sections are missing")


def _oracle_manifest(oracle_dir: Path) -> dict[str, Any]:
    """Validate command-installed immutable inputs; runtime download/fallback is prohibited."""
    _validate_oracle_artifacts(oracle_dir)
    manifest_path = oracle_dir / "manifest.json"
    if not manifest_path.is_file():
        raise ValueError("missing command-installed oracle manifest")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    expected = dict(affiliation_registry.EVIDENCE_ORACLE_MANIFEST)
    if manifest != expected:
        raise ValueError("oracle manifest pin mismatch")
    if canonical_sha256(manifest) != affiliation_registry.EVIDENCE_ORACLE_SHA256:
        raise ValueError("oracle manifest digest mismatch")
    return manifest


def command_pin_oracles(args: argparse.Namespace) -> int:
    """Create only the canonical manifest for already-downloaded pinned artifacts."""
    oracle_dir = Path(args.oracle_dir)
    _validate_oracle_artifacts(oracle_dir)
    target = oracle_dir / "manifest.json"
    payload = canonical_json_bytes(dict(affiliation_registry.EVIDENCE_ORACLE_MANIFEST))
    if target.exists() and target.read_bytes() != payload:
        raise ValueError("existing oracle manifest differs from pinned contract")
    if not target.exists():
        temporary = _write_staged(target, payload)
        os.replace(temporary, target)
        directory_fd = os.open(oracle_dir, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    return 0


def _validate_ror_envelope(payload: Any, oracle_dir: Path) -> list[dict[str, Any]]:
    if not isinstance(payload, dict) or not isinstance(payload.get("items"), list):
        raise ValueError("ROR v2 envelope missing items")
    allowed = {"number_of_results", "time_taken", "items", "meta", "links", "next"}
    if set(payload) - allowed:
        raise ValueError("ROR v2 envelope has unknown fields")
    items = payload["items"]
    if len(items) > MAX_ROR_RECORDS:
        raise ValueError("ROR page record limit exceeded")
    result_count = payload.get("number_of_results")
    if result_count is not None and (
            not isinstance(result_count, int) or result_count < len(items)
            or result_count > MAX_ROR_RECORDS):
        raise ValueError("ROR result count is invalid or exceeds the pinned limit")
    validator = None
    if items:
        schema = json.loads(_oracle_artifact_path(
            oracle_dir, "ror").read_text(encoding="utf-8"))
        validator = Draft7Validator(schema)
    for item in items:
        if not isinstance(item, dict):
            raise ValueError("ROR Schema 2.1 item is not an object")
        assert validator is not None
        errors = sorted(validator.iter_errors(item), key=lambda error: list(error.path))
        if errors:
            raise ValueError(f"ROR Schema 2.1 item violation: {errors[0].message}")
    return items


def _jsonld_organizations(value: str) -> list[dict[str, Any]]:
    try:
        decoded = json.loads(value)
    except json.JSONDecodeError as exc:
        raise ValueError("invalid JSON-LD") from exc
    records = decoded if isinstance(decoded, list) else [decoded]
    expanded: list[dict[str, Any]] = []
    for record in records:
        if not isinstance(record, dict):
            continue
        graph = record.get("@graph")
        if isinstance(graph, list):
            expanded.extend(item for item in graph if isinstance(item, dict))
        expanded.append(record)
    organizations = []
    for record in expanded:
        types = record.get("@type", [])
        types = [types] if isinstance(types, str) else types
        if isinstance(types, list) and any(
                item in {"Organization", "CollegeOrUniversity"} for item in types):
            organizations.append(record)
    return organizations


def _official_identity_evidence(url: str, expected_name: str, expected_country: str,
                                *, oracle_dir: Path) -> dict[str, Any]:
    """Return bounded exact official-site identity evidence or fail closed."""
    raw, transport = _bounded_direct_https(
        url, "official", oracle_dir=oracle_dir)
    text = raw.decode(transport["charset"], errors="strict")
    parser = _PageExtractor()
    parser.feed(text)
    values = parser.values()
    names_by_tier: dict[str, set[str]] = {
        "json-ld": set(), "title": set(), "h1": set(), "legal": set(),
    }
    countries_by_tier: dict[str, set[str]] = {"json-ld": set(), "legal": set()}
    pointers: dict[tuple[str, str], str] = {}
    jsonld_scripts = list(values.get("jsonld", []))
    if transport["media_type"] == "application/ld+json":
        jsonld_scripts.append(text)
    for script_index, script in enumerate(jsonld_scripts, start=1):
        for node_index, record in enumerate(_jsonld_organizations(script), start=1):
            scope = record.get("url", record.get("@id", ""))
            if isinstance(scope, str) and scope.startswith(("https://", "http://")):
                try:
                    if (urlsplit(scope).scheme != "https"
                            or urlsplit(scope).hostname.casefold()
                            != urlsplit(transport["final_url"]).hostname.casefold()):
                        raise ValueError("JSON-LD organization is outside the fetched origin")
                except AttributeError as exc:
                    raise ValueError("JSON-LD organization scope is malformed") from exc
            primary_name = record.get("name")
            alternate = record.get("alternateName", [])
            raw_names = ([primary_name] if isinstance(primary_name, str) and primary_name.strip()
                         else (alternate if isinstance(alternate, list) else [alternate]))
            for field_index, name in enumerate(raw_names):
                if isinstance(name, str) and normalize_name(name):
                    normalized = " ".join(nfc(name).split())
                    names_by_tier["json-ld"].add(normalized)
                    pointers[("json-ld", normalized)] = (
                        f"/html/script[@type='application/ld+json'][{script_index}]"
                        f"/organization[{node_index}]/name[{field_index + 1}]")
            address = record.get("address", {})
            country = address.get("addressCountry") if isinstance(address, dict) else None
            code = canonical_country(country) if isinstance(country, str) else None
            if code:
                countries_by_tier["json-ld"].add(code)
                pointers[("json-ld-country", code)] = (
                    f"/html/script[@type='application/ld+json'][{script_index}]"
                    f"/organization[{node_index}]/address/addressCountry")
    for tier in ("title", "h1"):
        for index, name in enumerate(values.get(tier, []), start=1):
            normalized = " ".join(nfc(name).split())
            if normalized:
                names_by_tier[tier].add(normalized)
                pointers[(tier, normalized)] = f"/html/{tier}[{index}]"
    expected_normalized = normalize_name(expected_name)
    for index, legal in enumerate(values.get("legal", []), start=1):
        if normalize_name(legal) == expected_normalized:
            names_by_tier["legal"].add(legal)
            pointers[("legal", legal)] = f"/html/legal-contact[{index}]"
        for _, _, country_name in affiliation_registry.ISO_3166_1_ROWS:
            if re.search(rf"(?<!\\w){re.escape(country_name)}(?!\\w)", legal, re.IGNORECASE):
                code = canonical_country(country_name)
                if code:
                    countries_by_tier["legal"].add(code)
                    pointers[("legal-country", code)] = f"/html/legal-contact[{index}]"
        for alias, code in affiliation_registry.LEGACY_COUNTRY_ALIASES:
            if re.search(rf"(?<!\\w){re.escape(alias)}(?!\\w)", legal, re.IGNORECASE):
                countries_by_tier["legal"].add(code)
                pointers[("legal-country", code)] = f"/html/legal-contact[{index}]"
    all_names = {
        normalize_name(name)
        for tier_names in names_by_tier.values() for name in tier_names
    }
    if not all_names:
        raise ValueError("official extraction missing identity")
    if len(all_names) != 1 or expected_normalized not in all_names:
        raise ValueError("official extraction conflict")
    expected_code = canonical_country(expected_country)
    all_countries = set().union(*countries_by_tier.values())
    if not expected_code or all_countries != {expected_code}:
        raise ValueError("official extraction country missing or conflicting")
    selected_name_tier = next(
        tier for tier in ("json-ld", "title", "h1", "legal")
        if names_by_tier[tier])
    selected_name = sorted(names_by_tier[selected_name_tier])[0]
    selected_country_tier = next(
        tier for tier in ("json-ld", "legal") if countries_by_tier[tier])
    fields = []
    for field_kind, tier, value, pointer_key in (
            ("organization_name", selected_name_tier, selected_name,
             (selected_name_tier, selected_name)),
            ("country", selected_country_tier, expected_code,
             (selected_country_tier + "-country", expected_code))):
        quote_value = selected_name if field_kind == "organization_name" else expected_code
        quote = _quote(quote_value)
        fields.append({
            "field": field_kind, "tier": tier, "pointer": pointers[pointer_key],
            "normalized_value": value, "value_sha256": quote["quote_sha256"],
            "quote": quote["quote"],
        })
    if (len(fields) > 4
            or sum(len(item["quote"].encode("utf-8")) for item in fields)
            > MAX_TOTAL_QUOTE_BYTES):
        raise ValueError("official evidence quote cap exceeded")
    return {
        "provider": "official", "url": normalize_website_url(url),
        "status": "corroborated", "candidate_name": expected_name,
        "candidate_country": expected_code, "payload_sha256": hashlib.sha256(raw).hexdigest(),
        "fields": fields, "transport": transport,
        "evidence_oracle_version": affiliation_registry.EVIDENCE_ORACLE_VERSION,
        "evidence_oracle_sha256": affiliation_registry.EVIDENCE_ORACLE_SHA256,
    }


def _canonical_evidence_timestamp(value: Any) -> tuple[datetime, str]:
    if not isinstance(value, str):
        raise ValueError("evidence timestamp missing")
    timestamp = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if timestamp.tzinfo is None:
        raise ValueError("evidence timestamp must include an offset")
    return timestamp, timestamp.astimezone(UTC).isoformat().replace("+00:00", "Z")


def _canonical_candidate_name(value: Any) -> str:
    if not isinstance(value, str):
        raise ValueError("candidate name missing")
    name = " ".join(nfc(value).split())
    if not name:
        raise ValueError("candidate name missing")
    return name


def _bound_evidence(row: dict[str, Any], provider: str, *, official: bool) -> dict[str, str]:
    if row.get("provider") != provider:
        raise ValueError("unexpected evidence provider")
    _, retrieved_at = _canonical_evidence_timestamp(row.get("retrieved_at"))
    digest = row.get("payload_sha256")
    if not (isinstance(digest, str) and len(digest) == 64
            and all(character in "0123456789abcdef" for character in digest.lower())):
        raise ValueError("evidence payload digest missing or malformed")
    url = normalize_website_url(row.get("url"))
    if official:
        return {
            "provider": provider,
            "retrieved_at": retrieved_at,
            "payload_sha256": digest.lower(),
            "url": url,
        }
    if not url.startswith(ROR_V2_ENDPOINT + "?"):
        raise ValueError("ROR evidence URL is not the pinned v2 endpoint")
    return {
        "provider": provider,
        "retrieved_at": retrieved_at,
        "payload_sha256": digest.lower(),
        "url": url,
    }


def _eligible_identity_decision(key: tuple[str, str], ror: dict[str, Any],
                                official: dict[str, Any]) -> dict[str, Any]:
    candidate_ror_id = normalize_ror_id(ror.get("candidate_external_id"))
    candidate_name = _canonical_candidate_name(ror.get("candidate_name"))
    candidate_country = canonical_country(ror.get("candidate_country"))
    observed_name = _canonical_candidate_name(key[0])
    expected_country = canonical_country(key[1])
    official_name = _canonical_candidate_name(official.get("candidate_name"))
    official_country = canonical_country(official.get("candidate_country"))
    typed_websites = tuple(sorted({
        normalize_website_url(url) for url in ror.get("official_websites", ())
    }))
    ror_evidence = _bound_evidence(ror, "ror", official=False)
    official_evidence = _bound_evidence(official, "official", official=True)
    if (ror.get("reason") != "active_ror_v2_exact_name_country_typed_website"
            or ror.get("evidence_oracle_version") != affiliation_registry.EVIDENCE_ORACLE_VERSION
            or official.get("evidence_oracle_version") != affiliation_registry.EVIDENCE_ORACLE_VERSION
            or ror.get("evidence_oracle_sha256") != affiliation_registry.EVIDENCE_ORACLE_SHA256
            or official.get("evidence_oracle_sha256") != affiliation_registry.EVIDENCE_ORACLE_SHA256
            or normalize_name(observed_name) != normalize_name(candidate_name)
            or not candidate_country or candidate_country != expected_country
            or candidate_ror_id != normalize_ror_id(official.get("candidate_external_id"))
            or candidate_name != official_name or candidate_country != official_country
            or not typed_websites or official_evidence["url"] not in typed_websites):
        raise ValueError("dual evidence does not meet automatic identity contract")
    return {
        "ror_id": candidate_ror_id,
        "name": candidate_name,
        "country": candidate_country,
        "official_websites": list(typed_websites),
        "evidence_oracle_version": affiliation_registry.EVIDENCE_ORACLE_VERSION,
        "evidence_oracle_sha256": affiliation_registry.EVIDENCE_ORACLE_SHA256,
        "evidence": sorted((ror_evidence, official_evidence),
                           key=lambda evidence: (evidence["provider"], evidence["url"],
                                                 evidence["retrieved_at"], evidence["payload_sha256"])),
    }


def evaluate_identity_attempts(attempts: list[dict[str, Any]], decision_at: str) -> list[dict[str, Any]]:
    """Deterministically emit identity-only eligibility; never infer a relationship."""
    now, canonical_decision_at = _canonical_evidence_timestamp(decision_at)
    decisions: list[dict[str, Any]] = []
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for attempt in attempts:
        grouped.setdefault((attempt.get("query", ""), attempt.get("country", "")), []).append(attempt)
    for key, rows in sorted(grouped.items()):
        ror = [row for row in rows if row.get("provider") == "ror" and row.get("status") == "proposal"]
        official = [row for row in rows if row.get("provider") == "official" and row.get("status") == "corroborated"]
        reason, action, applicable = "dual_evidence_missing", "pending", {}
        if not key[1]:
            reason = "country_missing"
        elif len(ror) != 1 or len(official) != 1:
            reason = "ambiguous_or_incomplete_evidence"
        elif any(row.get("relationship") or row.get("relationship_payload") for row in rows):
            reason = "relationship_payload_requires_review"
        else:
            try:
                timestamps = [_canonical_evidence_timestamp(row.get("retrieved_at"))[0]
                              for row in (ror + official)]
                if any(stamp > now or now - stamp > timedelta(
                        days=EVIDENCE_FRESHNESS_DAYS) for stamp in timestamps):
                    reason = "evidence_stale"
                else:
                    applicable = _eligible_identity_decision(key, ror[0], official[0])
                    action, reason = "eligible_identity_only", "dual_corroborated"
            except (KeyError, TypeError, ValueError):
                reason = "dual_evidence_contract_invalid"
        decision = {
            "query": key[0],
            "country": key[1],
            "action": action,
            "reason": reason,
            "attempts_sha256": canonical_sha256(rows),
            "decision_at": canonical_decision_at,
        }
        if action == "eligible_identity_only":
            decision["candidate"] = applicable
        decisions.append(decision)
    return decisions

def _read_source(path: str) -> tuple[dict[str, Any], str]:
    raw = Path(path).read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != SOURCE_SHA256:
        raise ValueError(f"unexpected source SHA-256: {digest}")
    source = json.loads(raw.decode("utf-8"))
    if not isinstance(source, dict) or len(source) != 4747:
        raise ValueError("source must contain exactly 4,747 top-level records")
    return source, digest


def _jsonl_bytes(rows: list[dict[str, Any]]) -> bytes:
    return b"".join(canonical_json_bytes(row) for row in rows)


def _write_or_check(path: str, data: bytes, check: bool) -> None:
    target = Path(path)
    if check:
        if not target.exists() or target.read_bytes() != data:
            raise ValueError(f"generated artifact differs: {target}")
        return
    target.write_bytes(data)



def _preserve_database_baseline(path: str, baseline: dict[str, Any]) -> dict[str, Any]:
    try:
        existing = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return baseline
    if existing.get("source_sha256") == baseline.get("source_sha256"):
        baseline["database_baseline"] = existing.get("database_baseline") or {}
    return baseline

def command_import(args: argparse.Namespace) -> int:
    if getattr(args, "operator_curated", False) and args.legacy_aliases:
        raise ValueError("operator-curated import forbids unpinned legacy aliases")
    source, digest = _read_source(args.source)
    aliases: dict[str, str] = {}
    if args.legacy_aliases:
        aliases = json.loads(Path(args.legacy_aliases).read_text(encoding="utf-8"))
        if not isinstance(aliases, dict) or not all(isinstance(key, str) and isinstance(value, str)
                                                    for key, value in aliases.items()):
            raise ValueError("legacy aliases must be a string-to-string JSON object")
    registry = build_registry(source, source_sha256=digest, timestamp=args.timestamp,
                              version=args.version, canonical_aliases=aliases,
                              operator_curated=getattr(args, "operator_curated", False))
    corrections = correction_projection(registry)
    baseline = _preserve_database_baseline(
        args.baseline,
        baseline_projection(
            registry, corrections, effective_date=args.effective_date))
    _write_or_check(args.registry, canonical_json_bytes(registry), args.check)
    _write_or_check(args.corrections, _jsonl_bytes(corrections), args.check)
    _write_or_check(args.baseline, canonical_json_bytes(baseline), args.check)
    return 0


def _load_corrections(path: str) -> list[dict[str, Any]]:
    raw = Path(path).read_bytes()
    if raw and not raw.endswith(b"\n"):
        raise ValueError("corrections JSONL must end in LF")
    return [json.loads(line) for line in raw.decode("utf-8").splitlines()]


def command_validate(args: argparse.Namespace) -> int:
    source, digest = _read_source(args.source)
    registry = load_registry(args.registry)
    if registry["source_sha256"] != digest:
        raise ValueError("registry source digest mismatch")
    validate_registry(registry)
    corrections = _load_corrections(args.corrections)
    replayed = correction_projection(registry)
    if corrections != replayed:
        raise ValueError("correction projection does not match event replay")
    if len(corrections) != len(source) or {row["source_key"] for row in corrections} != set(source):
        raise ValueError("correction rows do not cover source keys exactly once")
    baseline = json.loads(Path(args.baseline).read_text(encoding="utf-8"))
    validate_registry(registry, effective_date=baseline["effective_date"])
    expected = baseline_projection(
        registry, corrections, effective_date=baseline["effective_date"])
    expected["database_baseline"] = baseline.get("database_baseline") or {}
    if baseline != expected:
        raise ValueError("baseline does not match registry projection")
    if args.strict and baseline["registry_sha256"] != canonical_sha256(registry):
        raise ValueError("baseline registry digest mismatch")
    return 0


def command_snapshot_db_baseline(args: argparse.Namespace) -> int:
    """Bind release thresholds to a validated current bibliography snapshot."""
    registry = load_registry(args.registry)
    baseline_path = Path(args.baseline)
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    if baseline.get("registry_sha256") != canonical_sha256(registry):
        raise ValueError("baseline/registry digest mismatch")
    connection = sqlite3.connect(f"file:{Path(args.db).resolve()}?mode=ro", uri=True)
    try:
        if connection.execute("PRAGMA quick_check").fetchone()[0] != "ok":
            raise ValueError("database quick_check failed")
        current_observations = connection.execute(
            "SELECT COUNT(*) FROM observed_affiliations WHERE is_current=1"
        ).fetchone()[0]
        active_pending = connection.execute(
            "SELECT COALESCE(SUM(active_observation_count),0) "
            "FROM affiliation_pending_cases WHERE status IN ('open','proposed')"
        ).fetchone()[0]
        active_cases = connection.execute(
            "SELECT COUNT(*) FROM affiliation_pending_cases "
            "WHERE status IN ('open','proposed')").fetchone()[0]
        lifetime = connection.execute(
            "SELECT COALESCE(SUM(lifetime_observation_count),0) "
            "FROM affiliation_pending_cases").fetchone()[0]
        oldest = connection.execute(
            "SELECT COALESCE(MAX(0, CAST(julianday(?) - julianday(MIN(first_seen_at)) "
            "AS INTEGER)),0) FROM affiliation_pending_cases "
            "WHERE status IN ('open','proposed')",
            (args.captured_at[:10],)).fetchone()[0]
        mismatch_reasons = {
            reason: count for reason, count in connection.execute(
                "SELECT reason_code,COUNT(*) FROM affiliation_pending_cases "
                "WHERE status IN ('open','proposed') AND reason_code LIKE '%country%' "
                "GROUP BY reason_code ORDER BY reason_code")
        }
        version_count, superseded_count = connection.execute(
            "SELECT COUNT(*),COALESCE(SUM(is_current=0),0) "
            "FROM observed_affiliations").fetchone()
        cardinalities = {}
        for degree, count in connection.execute(
                "SELECT degree,COUNT(*) FROM (SELECT o.organization_id,"
                "COUNT(r.relationship_id) degree FROM affiliation_organizations o "
                "LEFT JOIN affiliation_relationships r ON "
                "r.subject_organization_id=o.organization_id GROUP BY o.organization_id) "
                "GROUP BY degree ORDER BY degree"):
            cardinalities[str(degree)] = count
        group_shares = {}
        denominator = connection.execute(
            "SELECT COUNT(DISTINCT paper_id) FROM paper_institutions").fetchone()[0]
        if denominator:
            for name, count in connection.execute(
                    "SELECT g.group_name,COUNT(DISTINCT pi.paper_id) "
                    "FROM institution_groups g JOIN institutions i USING(group_id) "
                    "JOIN paper_institutions pi USING(institution_id) "
                    "GROUP BY g.group_id ORDER BY g.group_name"):
                group_shares[name] = count / denominator
        metadata = connection.execute(
            "SELECT registry_sha256,event_head,base_generation,migration_receipt_id "
            "FROM affiliation_registry_metadata WHERE singleton=1"
        ).fetchone()
        if metadata is None:
            raise ValueError("database has no affiliation registry metadata")
        if metadata[0] != baseline["registry_sha256"]:
            raise ValueError("database registry digest does not match baseline")
        baseline["database_baseline"] = {
            "captured_at": args.captured_at,
            "registry_sha256": metadata[0],
            "event_head": metadata[1],
            "base_generation": metadata[2],
            "migration_receipt_id": metadata[3],
            "current_observation_count": current_observations,
            "active_pending_total": active_pending,
            "active_pending_case_count": active_cases,
            "lifetime_pending_total": lifetime,
            "oldest_active_age_days": oldest,
            "identity_country_mismatches": sum(mismatch_reasons.values()),
            "identity_country_mismatch_reasons": mismatch_reasons,
            "observation_version_count": version_count,
            "superseded_observation_count": superseded_count,
            "relationship_cardinality_histogram": cardinalities,
            "group_shares": group_shares,
        }
    finally:
        connection.close()
    temporary = _write_staged(baseline_path, canonical_json_bytes(baseline))
    os.replace(temporary, baseline_path)
    return 0


def command_report(args: argparse.Namespace) -> int:
    registry = load_registry(args.registry)
    rows = correction_projection(registry)
    summary = {
        "registry_sha256": canonical_sha256(registry), "event_head": registry["event_head"],
        "organizations": len(registry["organizations"]),
        "accepted_identity_aliases": len(registry["alias_candidates"]),
        "proposed_relationship_edges": len(registry["relationship_proposals"]),
        "accepted_official_relationship_edges": len(registry["relationships"]),
        "corrections": len(rows),
        "pending": sum(row["evidence"]["status"] != "accepted" for row in rows),
    }
    if getattr(args, "cohort", None):
        if not getattr(args, "db", None):
            raise ValueError("cohort report requires --db")
        with affiliation_registry.bibliography_reader_lock(Path(args.db)):
            cohort = _load_frozen_cohort(
                args.cohort, registry, args.db, allow_database_advance=True)
        summary.update({
            "frozen_pending_count": cohort["pending_count"],
            "frozen_pending_ids_sha256": cohort["pending_ids_sha256"],
            "frozen_cohort_sha256": canonical_sha256(cohort),
            "cohort_heads": cohort["heads"],
        })
        with affiliation_registry.bibliography_reader_lock(Path(args.db)):
            connection = sqlite3.connect(
                f"file:{Path(args.db).resolve()}?mode=ro", uri=True)
            try:
                metadata = connection.execute(
                    "SELECT schema_version,registry_sha256,event_head,"
                    "registry_contract_version,event_contract_version,"
                    "country_map_version,country_map_sha256,"
                    "evidence_oracle_version,evidence_oracle_sha256,"
                    "ledger_head,cohort_version,cohort_sha256,"
                    "relationship_set_sha256,relationship_count,"
                    "generation_descriptor_sha256,generation_id "
                    "FROM affiliation_registry_metadata WHERE singleton=1"
                ).fetchone()
                dispositions = {
                    disposition: count
                    for disposition, count in connection.execute(
                        "SELECT disposition,COUNT(*) "
                        "FROM affiliation_cohort_dispositions "
                        "WHERE cohort_sha256=? GROUP BY disposition "
                        "ORDER BY disposition",
                        (canonical_sha256(cohort),))
                }
                current_pending = connection.execute(
                    "SELECT COUNT(*) FROM affiliation_pending_cases "
                    "WHERE status IN ('open','proposed')").fetchone()[0]
                from repair_bibliography_institutions import logical_digest
                logical_sha256 = logical_digest(connection)
            finally:
                connection.close()
        ledger_path = Path(args.ledger) if getattr(args, "ledger", None) else None
        descriptor_path = (
            Path(args.generation_descriptor)
            if getattr(args, "generation_descriptor", None) else None)
        decision_path = (
            Path(args.decisions)
            if getattr(args, "decisions", None) else None)
        identity_keys = [
            affiliation_registry.organization_identity_key(
                row["canonical_name_en"], row["country"],
                country_scope=row.get("country_scope"))
            for row in registry["organizations"]
            if row.get("status") == "active"
        ]
        identity_keys = [key for key in identity_keys if key is not None]
        consolidation_events = [
            event for event in registry["events"]
            if event.get("type") == "pinned_root_consolidated"]
        superseded_proposals = sum(
            len((event.get("payload") or {}).get(
                "proposal_supersessions", []))
            for event in consolidation_events)
        source_identifiers = [
            identifier["value"]
            for organization in registry["organizations"]
            for identifier in organization.get("identifiers", [])
            if identifier.get("authority") == "source_af_id"
        ]
        action_counts = {
            action: sum(
                event.get("type") == f"identity_{action}"
                for event in registry["events"])
            for action in ("created", "enriched", "aliased", "merged",
                           "rejected", "split")
        }
        summary.update({
            "active_duplicate_nonempty_identity_keys":
                len(identity_keys) - len(set(identity_keys)),
            "redirects": len(registry.get("redirects", [])),
            "source_identifier_count": len(source_identifiers),
            "source_identifier_unique_count": len(set(source_identifiers)),
            "pinned_consolidation_event_count": len(consolidation_events),
            "identity_superseded_proposal_count": superseded_proposals,
            "legacy_relationship_accounted_count":
                len(registry["relationship_proposals"]) + superseded_proposals,
            "automatic_identity_event_counts": action_counts,
            "cohort_disposition_counts": dispositions,
            "cohort_unclassified_count": dispositions.get("UNCLASSIFIED", 0),
            "current_pending_case_count": current_pending,
            "database_sha256": _database_sha256(args.db),
            "database_logical_sha256": logical_sha256,
            "database_contracts": dict(zip((
                "schema_version", "registry_sha256", "event_head",
                "registry_contract_version", "event_contract_version",
                "country_map_version", "country_map_sha256",
                "evidence_oracle_version", "evidence_oracle_sha256",
                "ledger_head", "cohort_version", "cohort_sha256",
                "relationship_set_sha256", "relationship_count",
                "generation_descriptor_sha256", "generation_id",
            ), metadata)),
        })
        if ledger_path:
            ledger_raw = ledger_path.read_bytes()
            summary.update({
                "ledger_head": _verified_ledger_tail(ledger_path),
                "ledger_segments": len(ledger_raw.splitlines()),
                "ledger_bytes": len(ledger_raw),
                "ledger_sha256": hashlib.sha256(ledger_raw).hexdigest(),
            })
        if descriptor_path:
            descriptor_raw = descriptor_path.read_bytes()
            descriptor = json.loads(descriptor_raw)
            summary.update({
                "generation_descriptor_sha256":
                    hashlib.sha256(descriptor_raw).hexdigest(),
                "generation_id": descriptor.get("generation_id"),
            })
        if decision_path:
            decision_raw = decision_path.read_bytes()
            decision_artifact = json.loads(decision_raw)
            summary.update({
                "decision_artifact_sha256":
                    hashlib.sha256(decision_raw).hexdigest(),
                "decisions_sha256": decision_artifact.get(
                    "decisions_sha256"),
                "decision_count": len(
                    decision_artifact.get("decisions", [])),
                "decision_unclassified_count":
                    decision_artifact.get("unclassified_count"),
            })
    sys.stdout.write(canonical_json_bytes(summary).decode("utf-8"))
    return 0
def command_check_oracles(args: argparse.Namespace) -> int:
    """Check only command-installed ignored oracle files; never download provider inputs."""
    manifest = _oracle_manifest(Path(args.oracle_dir))
    sys.stdout.write(canonical_json_bytes({
        "oracle_manifest_sha256": canonical_sha256(manifest),
        "ror_endpoint": ROR_V2_ENDPOINT,
        "ror_schema_version": ROR_SCHEMA_VERSION,
        "ror_schema_commit": ROR_SCHEMA_COMMIT,
        "psl_version": PSL_VERSION,
        "psl_commit": PSL_COMMIT,
    }).decode("utf-8"))
    return 0




def _request_json(url: str, context: ssl.SSLContext, *,
                  oracle_dir: Path) -> tuple[dict[str, Any], bytes]:
    del context
    raw, metadata = _bounded_direct_https(
        url, "application/json", oracle_dir=oracle_dir)
    try:
        return json.loads(raw.decode(metadata["charset"], errors="strict")), raw
    except json.JSONDecodeError as exc:
        raise ValueError("invalid JSON provider response") from exc


def _attempt(base: dict[str, Any], **values: Any) -> dict[str, Any]:
    """Return a complete, canonical attempt row with deterministic fields."""
    return {
        **base, "provider": "", "url": "", "status": "pending",
        "candidate_external_id": "", "candidate_name": "", "candidate_country": "",
        "official_websites": [], "score": 0.0, "reason": "", "payload_sha256": "", "quote_sha256": "",
        "evidence_oracle_version": affiliation_registry.EVIDENCE_ORACLE_VERSION,
        "evidence_oracle_sha256": affiliation_registry.EVIDENCE_ORACLE_SHA256,
        "error": "", "attempt_number": 0, "retry_number": 0, **values,
    }


def _request_with_budget(url: str, context: ssl.SSLContext, args: argparse.Namespace,
                         state: dict[str, int]) -> tuple[dict[str, Any], bytes, int]:
    """Issue bounded retries; caller owns deterministic failure recording."""
    last_error: Exception | None = None
    for retry_number in range(args.max_retries + 1):
        if state["requests"] >= args.request_budget:
            raise RuntimeError("request_budget_exhausted")
        state["requests"] += 1
        try:
            payload, raw = _request_json(
                url, context, oracle_dir=Path(args.oracle_dir))
            return payload, raw, retry_number
        except (OSError, ValueError, urllib.error.URLError) as exc:
            last_error = exc
            if retry_number < args.max_retries and args.retry_backoff_seconds:
                time.sleep(args.retry_backoff_seconds * (2 ** retry_number))
    assert last_error is not None
    raise last_error


DB_ATTEMPT_PROVIDERS = frozenset({"official", "ror", "wikidata", "wikipedia", "scopus"})
DB_ATTEMPT_OUTCOMES = frozenset({
    "success", "no_match", "unavailable", "subscription_required", "timeout",
    "rate_limited", "error", "budget_exhausted",
})


def _attempt_outcome(attempt: dict[str, Any]) -> str:
    if attempt["provider"] not in DB_ATTEMPT_PROVIDERS:
        raise ValueError(f"unsupported affiliation attempt provider: {attempt['provider']}")
    status = attempt["status"]
    if status in {"proposal", "discovered", "corroborated"}:
        return "success"
    if status == "pending":
        return "no_match"
    if status == "incomplete":
        return "budget_exhausted"
    if status != "failed":
        raise ValueError(f"unsupported affiliation attempt status: {status}")
    error = attempt.get("error", "")
    if error == "TimeoutError":
        return "timeout"
    if error == "HTTPError":
        return "rate_limited"
    return "unavailable" if error in {"OSError", "URLError"} else "error"


def _load_pending_targets(path: str) -> tuple[set[tuple[str, str]], dict[tuple[str, str], set[str]]]:
    connection = sqlite3.connect(f"file:{Path(path).resolve()}?mode=ro", uri=True)
    try:
        tables = {row[0] for row in connection.execute(
            "SELECT name FROM sqlite_master WHERE type='table'")}
        required = {
            "affiliation_pending_cases", "affiliation_pending_observations",
            "observed_affiliations", "affiliation_enrichment_attempts",
        }
        if missing := required - tables:
            raise ValueError("affiliation-2 pending schema missing: " + ",".join(sorted(missing)))
        attempt_schema = connection.execute(
            "SELECT sql FROM sqlite_master WHERE type='table' "
            "AND name='affiliation_enrichment_attempts'"
        ).fetchone()
        declared = (attempt_schema[0] if attempt_schema else "").lower()
        vocabulary = (*DB_ATTEMPT_PROVIDERS, *DB_ATTEMPT_OUTCOMES)
        if not all(f"'{value}'" in declared for value in vocabulary):
            raise ValueError("affiliation attempt provider/outcome checks are missing")
        rows = connection.execute(
            "SELECT DISTINCT p.pending_id,o.raw_name,p.observed_country_code "
            "FROM affiliation_pending_cases p "
            "JOIN affiliation_pending_observations link USING(pending_id) "
            "JOIN observed_affiliations o USING(observation_id) "
            "WHERE p.status IN ('open','proposed') AND o.is_current=1 "
            "AND o.resolution_status IN ('unseen','ambiguous')"
        ).fetchall()
    finally:
        connection.close()
    targets: set[tuple[str, str]] = set()
    pending_ids: dict[tuple[str, str], set[str]] = {}
    for pending_id, name, country in rows:
        key = (name, country)
        targets.add(key)
        pending_ids.setdefault(key, set()).add(pending_id)
    return targets, pending_ids
FROZEN_PENDING_COUNT = 5162
FROZEN_PENDING_SNAPSHOT_SHA256 = "16d99fbca4a3a305314593b0060157625085351676a86e089530a616b7166f62"
FROZEN_PENDING_ID_SET_SHA256 = "52ff02c15bbc0cb3d370807ba35c073cb6ef0fe72f259d5a6ed96620ba32e3f3"
FROZEN_RELATIONSHIP_COUNT = 2245
FROZEN_RELATIONSHIP_SNAPSHOT_SHA256 = "5f7a45272994384188ea9d516bac9b244feae3b18402bc73e6def00c57479738"
FROZEN_RELATIONSHIP_ID_SET_SHA256 = "9f077283ca47393d284acc30420bf1a98e08a4d3f5774909a1091969b6a67cab"
_CLOSED_DISPOSITIONS = frozenset({
    "RESOLVED", "MANUAL_HOLD", "IDENTITY_CONFLICT", "AMBIGUOUS_HOMONYM",
    "COUNTRY_MISSING_OR_UNMAPPABLE", "RELATIONSHIP_ONLY", "EVIDENCE_STALE",
    "PROVIDER_OR_SECURITY_INCOMPLETE", "NO_MATCH_OR_GENERIC", "UNCLASSIFIED",
})


def _database_sha256(path: str) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _current_heads(registry: dict[str, Any], database: str) -> dict[str, str]:
    """Derive every binding from the current local artifacts, never CLI input."""
    return {
        "registry_sha256": canonical_sha256(registry),
        "event_head": str(registry["event_head"]),
        "policy_version": str(registry["policy_version"]),
        "country_map_version": str(affiliation_registry.COUNTRY_MAP_VERSION),
        "country_map_sha256": str(affiliation_registry.COUNTRY_MAP_SHA256),
        "evidence_oracle_version": affiliation_registry.EVIDENCE_ORACLE_VERSION,
        "evidence_oracle_sha256": affiliation_registry.EVIDENCE_ORACLE_SHA256,
        "registry_schema_version": affiliation_registry.REGISTRY_SCHEMA_VERSION,
        "registry_contract_version": affiliation_registry.REGISTRY_CONTRACT_VERSION,
        "event_contract_version": affiliation_registry.EVENT_CONTRACT_VERSION,
        "database_sha256": _database_sha256(database),
        "database_contract": "affiliation-3",
    }


def _open_pending_ids(path: str) -> list[str]:
    connection = sqlite3.connect(f"file:{Path(path).resolve()}?mode=ro", uri=True)
    try:
        rows = connection.execute(
            "SELECT pending_id FROM affiliation_pending_cases "
            "WHERE status IN ('open','proposed') ORDER BY pending_id"
        ).fetchall()
    finally:
        connection.close()
    identifiers = [str(row[0]) for row in rows]
    if len(identifiers) != len(set(identifiers)):
        raise ValueError("pending cohort contains duplicate IDs")
    return identifiers


def _cohort_payload(ids: list[str], heads: dict[str, str], timestamp: str) -> dict[str, Any]:
    if (len(ids) != FROZEN_PENDING_COUNT
            or canonical_sha256(ids) != FROZEN_PENDING_ID_SET_SHA256):
        raise ValueError("frozen pending cohort does not match the approved exact ID set")
    return {
        "schema_version": "affiliation-frozen-cohort-v1",
        "kind": "frozen_pending",
        "pending_ids": ids,
        "pending_count": len(ids),
        "pending_ids_sha256": canonical_sha256(ids),
        "approved_pending_snapshot_sha256": FROZEN_PENDING_SNAPSHOT_SHA256,
        "heads": heads,
        "frozen_at": _canonical_evidence_timestamp(timestamp)[1],
        "legacy_relationship_count": FROZEN_RELATIONSHIP_COUNT,
        "legacy_relationship_ids_sha256": FROZEN_RELATIONSHIP_ID_SET_SHA256,
        "approved_relationship_snapshot_sha256":
            FROZEN_RELATIONSHIP_SNAPSHOT_SHA256,
    }


def _load_frozen_cohort(path: str, registry: dict[str, Any], database: str,
                        *, allow_database_advance: bool = False) -> dict[str, Any]:
    raw = Path(path).read_bytes()
    cohort = json.loads(raw)
    if canonical_json_bytes(cohort) != raw:
        raise ValueError("cohort artifact is not canonical JSON")
    ids = cohort.get("pending_ids")
    if not isinstance(ids, list) or ids != sorted(ids) or any(not isinstance(item, str) for item in ids):
        raise ValueError("cohort IDs must be sorted unique strings")
    expected = _cohort_payload(ids, cohort.get("heads", {}), cohort.get("frozen_at"))
    if cohort != expected:
        raise ValueError("cohort artifact is incomplete or does not match the frozen contract")
    current = _current_heads(registry, database)
    if allow_database_advance:
        immutable_contracts = (
            "policy_version", "country_map_version", "country_map_sha256",
            "evidence_oracle_version", "evidence_oracle_sha256",
            "registry_schema_version", "registry_contract_version",
            "event_contract_version", "database_contract",
        )
        if any(
                cohort["heads"].get(key) != current.get(key)
                for key in immutable_contracts):
            raise ValueError(
                "COHORT_HEAD_MISMATCH: current contracts differ from freeze")
        frozen_event_head = cohort["heads"].get("event_head")
        replay_digests = {
            event.get("digest") for event in registry.get("events", [])}
        if (
                frozen_event_head != registry.get("event_head")
                and frozen_event_head not in replay_digests):
            raise ValueError(
                "COHORT_HEAD_MISMATCH: frozen event head is not an ancestor")
        cohort_sha256 = canonical_sha256(cohort)
        connection = sqlite3.connect(
            f"file:{Path(database).resolve()}?mode=ro", uri=True)
        try:
            metadata = connection.execute(
                "SELECT cohort_version,cohort_sha256 "
                "FROM affiliation_registry_metadata WHERE singleton=1").fetchone()
        finally:
            connection.close()
        if (
                registry.get("cohort_version") != "affiliation-frozen-cohort-v1"
                or registry.get("cohort_sha256") != cohort_sha256
                or metadata != ("affiliation-frozen-cohort-v1", cohort_sha256)):
            raise ValueError(
                "COHORT_HEAD_MISMATCH: finalized cohort binding differs")
    elif cohort["heads"] != current:
        raise ValueError(
            "COHORT_HEAD_MISMATCH: current registry/contracts/database differ from freeze")
    return cohort


def command_freeze_pending_cohort(args: argparse.Namespace) -> int:
    registry = load_registry(args.registry)
    with affiliation_registry.bibliography_reader_lock(Path(args.db)):
        payload = _cohort_payload(_open_pending_ids(args.db), _current_heads(registry, args.db), args.timestamp)
    target = Path(args.cohort)
    data = canonical_json_bytes(payload)
    if target.exists() and target.read_bytes() != data:
        raise ValueError("frozen cohort artifact is immutable")
    if not target.exists():
        temporary = _write_staged(target, data)
        os.replace(temporary, target)
        _fsync_directory(target.parent)
    sys.stdout.write(canonical_json_bytes({
        "pending_count": payload["pending_count"],
        "pending_ids_sha256": payload["pending_ids_sha256"],
        "heads": payload["heads"],
    }).decode("utf-8"))
    return 0


def _fsync_directory(path: Path) -> None:
    descriptor = os.open(path, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _require_attempt_coverage(attempts: list[dict[str, Any]], cohort: dict[str, Any]) -> None:
    cohort_ids = set(cohort["pending_ids"])
    seen: set[str] = set()
    for attempt in attempts:
        ids = attempt.get("pending_ids", [])
        if not isinstance(ids, list) or ids != sorted(set(ids)):
            raise ValueError("investigation attempt pending_ids must be a sorted unique list")
        if not set(ids) <= cohort_ids:
            raise ValueError("investigation attempt covers an ID outside the frozen cohort")
        seen.update(ids)
    if seen != cohort_ids:
        raise ValueError("investigation ledger does not cover every frozen pending ID")


def _disposition_for_attempts(rows: list[dict[str, Any]], decision_at: str) -> str:
    """Closed, conservative precedence for one frozen pending ID."""
    if any(row.get("relationship") or row.get("relationship_payload") for row in rows):
        return "RELATIONSHIP_ONLY"
    identity = evaluate_identity_attempts(rows, decision_at)
    if any(row.get("action") == "eligible_identity_only" for row in identity):
        return "RESOLVED"
    reasons = {str(row.get("reason", "")) for row in rows}
    if any("manual" in reason for reason in reasons):
        return "MANUAL_HOLD"
    if any("conflict" in reason for reason in reasons):
        return "IDENTITY_CONFLICT"
    if any("ambiguous" in reason or "multiple" in reason for reason in reasons):
        return "AMBIGUOUS_HOMONYM"
    if any(reason in {"country_missing", "country_unmappable"} for reason in reasons):
        return "COUNTRY_MISSING_OR_UNMAPPABLE"
    if any("stale" in reason for reason in reasons):
        return "EVIDENCE_STALE"
    if any(row.get("status") in {"failed", "incomplete"} or "security" in reason
           or "provider" in reason or "budget" in reason for row, reason in
           ((item, str(item.get("reason", ""))) for item in rows)):
        return "PROVIDER_OR_SECURITY_INCOMPLETE"
    return "NO_MATCH_OR_GENERIC"


def _closed_cohort_decisions(attempts: list[dict[str, Any]], cohort: dict[str, Any],
                             decision_at: str) -> list[dict[str, Any]]:
    _require_attempt_coverage(attempts, cohort)
    by_id = {identifier: [] for identifier in cohort["pending_ids"]}
    for row in attempts:
        for identifier in row["pending_ids"]:
            by_id[identifier].append(row)
    decisions = [{
        "pending_id": identifier,
        "disposition": _disposition_for_attempts(by_id[identifier], decision_at),
        "attempts_sha256": canonical_sha256(by_id[identifier]),
    } for identifier in cohort["pending_ids"]]
    if len(decisions) != FROZEN_PENDING_COUNT or any(
            item["disposition"] not in _CLOSED_DISPOSITIONS - {"UNCLASSIFIED"} for item in decisions):
        raise ValueError("closed cohort disposition invariant failed")
    return decisions


def _persist_pending_attempts(path: str, attempts: list[dict[str, Any]],
                              pending_ids: dict[tuple[str, str], set[str]]) -> None:
    connection = sqlite3.connect(path)
    try:
        connection.execute("PRAGMA foreign_keys=ON")
        for attempt in attempts:
            if attempt["provider"] == "policy":
                continue
            key = (attempt["query"], attempt["country"])
            for pending_id in sorted(pending_ids.get(key, ())):
                outcome = _attempt_outcome(attempt)
                if outcome not in DB_ATTEMPT_OUTCOMES:
                    raise ValueError(f"unsupported affiliation attempt outcome: {outcome}")
                attempt_id = hashlib.sha256(
                    canonical_json_bytes([pending_id, attempt])
                ).hexdigest()
                response_digest = attempt.get("payload_sha256", "")
                proposal_digest = (
                    canonical_sha256(attempt)
                    if outcome == "success" else ""
                )
                inserted = connection.execute(
                    "INSERT OR IGNORE INTO affiliation_enrichment_attempts "
                    "(attempt_id,pending_id,provider,started_at,finished_at,outcome,"
                    "response_digest,error_class,proposal_digest) VALUES (?,?,?,?,?,?,?,?,?)",
                    (attempt_id, pending_id, attempt["provider"], attempt["retrieved_at"],
                     attempt["retrieved_at"], outcome, response_digest, attempt.get("error", ""),
                     proposal_digest),
                ).rowcount
                if inserted:
                    connection.execute(
                        "UPDATE affiliation_pending_cases SET "
                        "attempt_count=attempt_count+1,last_attempt_at=?,"
                        "proposal_digest=CASE WHEN ?<>'' THEN ? ELSE proposal_digest END,"
                        "status=CASE WHEN ?='success' AND status='open' THEN 'proposed' ELSE status END "
                        "WHERE pending_id=?",
                        (attempt["retrieved_at"], proposal_digest, proposal_digest, outcome, pending_id),
                    )
        connection.commit()
    except BaseException:
        connection.rollback()
        raise
    finally:
        connection.close()


def _ror_paginated_query(name: str, context: ssl.SSLContext, args: argparse.Namespace,
                         state: dict[str, int], oracle_dir: Path) -> tuple[dict[str, Any], bytes, int]:
    """Follow only provider-supplied same-origin ROR v2 next links."""
    url = ROR_V2_ENDPOINT + "?" + urlencode(
        {"query": name}, quote_via=urllib.parse.quote, safe="")
    items: list[dict[str, Any]] = []
    seen_urls: set[str] = set()
    retry_number = 0
    while url:
        if url in seen_urls or len(seen_urls) >= MAX_ROR_PAGES:
            raise ValueError("ROR pagination exceeds the pinned page limit")
        seen_urls.add(url)
        payload, _, retry_number = _request_with_budget(url, context, args, state)
        page_items = _validate_ror_envelope(payload, oracle_dir)
        items.extend(page_items)
        if len(items) > MAX_ROR_RECORDS:
            raise ValueError("ROR pagination exceeds the pinned record limit")
        next_value = payload.get("next")
        if next_value is None and isinstance(payload.get("links"), dict):
            next_value = payload["links"].get("next")
        if next_value is None and isinstance(payload.get("meta"), dict):
            next_value = payload["meta"].get("next")
        if next_value is not None and not isinstance(next_value, str):
            raise ValueError("ROR pagination next link is malformed")
        if next_value:
            candidate = urljoin(url, next_value)
            parsed = urlsplit(candidate)
            endpoint = urlsplit(ROR_V2_ENDPOINT)
            if (parsed.scheme, parsed.hostname, parsed.port or 443, parsed.path) != (
                    endpoint.scheme, endpoint.hostname, endpoint.port or 443, endpoint.path):
                raise ValueError("ROR pagination left the pinned same-origin endpoint")
            url = candidate
        else:
            url = ""
    return {"items": items, "number_of_results": len(items)}, canonical_json_bytes(items), retry_number

def command_resolve_pending(args: argparse.Namespace) -> int:
    """Append proposal-only, bounded provider attempts; never mutate accepted artifacts."""
    load_registry(args.registry)
    if not args.allow_network:
        raise ValueError("resolve-pending requires --allow-network")
    if (args.request_budget < 1 or args.max_retries < 0
            or args.circuit_breaker_failures < 1 or args.retry_backoff_seconds < 0):
        raise ValueError("request budget, retries, circuit breaker, and backoff must be valid")
    targets = {(name, args.country) for name in args.name}
    pending_ids: dict[tuple[str, str], set[str]] = {}
    cohort = None
    if args.db:
        with affiliation_registry.bibliography_reader_lock(Path(args.db)):
            db_targets, pending_ids = _load_pending_targets(args.db)
            targets.update(db_targets)
            if getattr(args, "cohort", None):
                cohort = _load_frozen_cohort(args.cohort, load_registry(args.registry), args.db)
                frozen_ids = set(cohort["pending_ids"])
                pending_ids = {
                    key: ids & frozen_ids for key, ids in pending_ids.items() if ids & frozen_ids
                }
                targets = set(pending_ids)
    if getattr(args, "cohort", None) and cohort is None:
        raise ValueError("investigate cohort requires --db")
    context, attempts = ssl.create_default_context(), []
    oracle_dir = Path(args.oracle_dir)
    _oracle_manifest(oracle_dir)
    state = {"requests": 0, "failures": 0}
    incomplete = False
    ordered_targets = sorted((nfc_name, nfc_country) for nfc_name, nfc_country in targets
                             if isinstance(nfc_name, str) and isinstance(nfc_country, str))
    for target_index, (name, country) in enumerate(ordered_targets):
        base = {"query": name, "country": country, "retrieved_at": args.retrieved_at,
                "target_index": target_index,
                "pending_ids": sorted(pending_ids.get((name, country), ()))}
        country_state, _ = affiliation_registry.country_resolution(country)
        if country_state != "present":
            attempts.append(_attempt(
                base, provider="policy", status="pending",
                reason=("country_missing" if country_state == "missing"
                        else "country_unmappable")))
            continue
        if state["failures"] >= args.circuit_breaker_failures or state["requests"] >= args.request_budget:
            attempts.append(_attempt(base, provider="policy", status="incomplete",
                reason="circuit_breaker_open" if state["failures"] >= args.circuit_breaker_failures
                else "request_budget_exhausted"))
            incomplete = True
            continue
        if is_generic_fragment(name):
            attempts.append(_attempt(base, provider="policy", status="pending",
                reason="generic_fragment_not_resolved"))
            continue
        url = ROR_V2_ENDPOINT + "?" + urlencode(
            {"query": name}, quote_via=urllib.parse.quote, safe="")
        candidates: list[dict[str, Any]] = []
        try:
            payload, raw, retry_number = _ror_paginated_query(
                name, context, args, state, oracle_dir)
            candidates = affiliation_registry.automatic_ror_v2_candidates(
                payload, name, country)
            if not candidates:
                attempts.append(_attempt(base, provider="ror", url=url, status="pending",
                    reason="no_exact_country_consistent_match", payload_sha256=hashlib.sha256(raw).hexdigest(),
                    attempt_number=state["requests"], retry_number=retry_number))
            for candidate in candidates:
                attempts.append(_attempt(base, provider="ror", url=url, status="proposal",
                    candidate_external_id=candidate["external_id"], candidate_name=candidate["name"],
                    candidate_country=candidate["country"], official_websites=list(candidate.get("websites", ())),
                    score=candidate["score"], reason=candidate["reason"], payload_sha256=hashlib.sha256(raw).hexdigest(),
                    quote_sha256=canonical_sha256(candidate), attempt_number=state["requests"],
                    retry_number=retry_number))
                for official_url in candidate["links"]:
                    if official_url.startswith("https://"):
                        try:
                            evidence = _official_identity_evidence(
                                official_url, candidate["name"], candidate["country"],
                                oracle_dir=oracle_dir)
                            attempts.append(_attempt(
                                base, **evidence, candidate_external_id=candidate["external_id"],
                                score=candidate["score"], reason="typed_ror_website_corroborated",
                                retrieved_at=args.retrieved_at, attempt_number=state["requests"],
                                retry_number=retry_number))
                        except (OSError, ValueError, ssl.SSLError) as exc:
                            attempts.append(_attempt(
                                base, provider="official", url=official_url, status="pending",
                                candidate_external_id=candidate["external_id"], candidate_name=candidate["name"],
                                candidate_country=candidate["country"], reason="official_evidence_incomplete",
                                error=type(exc).__name__, attempt_number=state["requests"],
                                retry_number=retry_number))
        except (OSError, ValueError, urllib.error.URLError, RuntimeError) as exc:
            state["failures"] += 1
            reason = str(exc) if str(exc) == "request_budget_exhausted" else "provider_failure"
            attempts.append(_attempt(base, provider="ror", url=url,
                status="incomplete" if reason == "request_budget_exhausted" else "failed",
                reason=reason, error="" if reason == "request_budget_exhausted" else type(exc).__name__,
                attempt_number=state["requests"], retry_number=args.max_retries))
            incomplete = True
            continue
        if not candidates and state["requests"] >= args.request_budget:
            attempts.append(_attempt(base, provider="policy", status="incomplete",
                reason="request_budget_exhausted"))
            incomplete = True
        elif not candidates:
            wiki_url = "https://en.wikipedia.org/w/api.php?" + urlencode({
                "action": "query", "list": "search", "srsearch": name, "srlimit": 3, "format": "json",
            })
            try:
                wiki_payload, wiki_raw, retry_number = _request_with_budget(wiki_url, context, args, state)
                matches = [item for item in wiki_payload.get("query", {}).get("search", [])
                           if normalize_name(str(item.get("title", ""))) == normalize_name(name)]
                if matches:
                    title = str(matches[0]["title"])
                    attempts.append(_attempt(base, provider="wikipedia",
                        url="https://en.wikipedia.org/wiki/" + title.replace(" ", "_"),
                        status="discovered", candidate_name=title, candidate_country=country, score=0.5,
                        reason="exact_title_discovery_only", payload_sha256=hashlib.sha256(wiki_raw).hexdigest(),
                        quote_sha256=canonical_sha256(matches[0]), attempt_number=state["requests"],
                        retry_number=retry_number))
            except (OSError, ValueError, urllib.error.URLError, RuntimeError) as exc:
                state["failures"] += 1
                attempts.append(_attempt(base, provider="wikipedia", url=wiki_url, status="failed",
                    reason="provider_failure", error=type(exc).__name__, attempt_number=state["requests"],
                    retry_number=args.max_retries))
    if cohort:
        _require_attempt_coverage(attempts, cohort)
    _persist_evidence_segments(getattr(args, "evidence_dir", None), attempts)
    if args.db and attempts:
        with affiliation_registry.bibliography_writer_lock(Path(args.db)):
            _persist_pending_attempts(args.db, attempts, pending_ids)
    _append_fsync(Path(args.proposals), _jsonl_bytes(attempts))
    return 6 if incomplete else 0


def _persist_evidence_segments(evidence_dir: str | None, attempts: list[dict[str, Any]]) -> None:
    """Durably content-address attempts before any DB join; duplicates must be byte-identical."""
    if not evidence_dir or not attempts:
        return
    root = Path(evidence_dir)
    segments = root / "segments"
    segments.mkdir(parents=True, exist_ok=True)
    rows = []
    for attempt in attempts:
        row = dict(attempt)
        row["evidence_id"] = canonical_sha256(row)
        rows.append(row)
    data = _jsonl_bytes(sorted(rows, key=lambda row: row["evidence_id"]))
    digest = hashlib.sha256(data).hexdigest()
    target = segments / f"{digest}.jsonl"
    if target.exists() and target.read_bytes() != data:
        raise ValueError("content-addressed evidence collision")
    if not target.exists():
        temporary = _write_staged(target, data)
        os.replace(temporary, target)
        directory_fd = os.open(segments, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    index = root / "index.jsonl"
    entry = canonical_json_bytes({"segment_sha256": digest, "row_count": len(rows)})
    if index.exists() and entry in index.read_bytes().splitlines(keepends=True):
        return
    _append_fsync(index, entry)


def command_evaluate_pending(args: argparse.Namespace) -> int:
    """Write a deterministic, immutable identity-only decision set; no registry mutation."""
    attempts = _load_corrections(args.proposals)
    registry = load_registry(args.registry) if getattr(args, "registry", None) else None
    cohort = None
    if getattr(args, "cohort", None):
        if not registry or not getattr(args, "db", None):
            raise ValueError("closed cohort evaluation requires --registry and --db")
        with affiliation_registry.bibliography_reader_lock(Path(args.db)):
            cohort = _load_frozen_cohort(
                args.cohort, registry, args.db, allow_database_advance=True)
        decisions = _closed_cohort_decisions(attempts, cohort, args.decision_at)
        heads = _current_heads(registry, args.db)
    else:
        decisions = evaluate_identity_attempts(attempts, args.decision_at)
        heads = {
            "registry_sha256": args.expected_registry_sha256,
            "event_head": args.expected_event_head,
            "ledger_head": getattr(args, "expected_ledger_head", ""),
            "cohort_head": getattr(args, "expected_cohort_head", ""),
        }
    artifact = {
        "schema_version": "affiliation-investigation-v2",
        "heads": heads,
        "cohort_sha256": canonical_sha256(cohort) if cohort else "",
        "decisions": decisions,
        "decisions_sha256": canonical_sha256(decisions),
        "unclassified_count": sum(
            row.get("disposition") == "UNCLASSIFIED" for row in decisions),
    }
    if cohort and (len(decisions) != FROZEN_PENDING_COUNT or artifact["unclassified_count"]):
        raise ValueError("closed cohort must be exact and contain no UNCLASSIFIED disposition")
    payload = canonical_json_bytes(artifact)
    target = Path(args.decisions)
    if target.exists() and target.read_bytes() != payload:
        raise ValueError("decision artifact is immutable")
    if not target.exists():
        temporary = _write_staged(target, payload)
        os.replace(temporary, target)
        _fsync_directory(target.parent)
    sys.stdout.write(canonical_json_bytes({
        "decision_count": len(decisions),
        "decisions_sha256": artifact["decisions_sha256"],
        "cohort_sha256": artifact["cohort_sha256"],
        "unclassified_count": artifact["unclassified_count"],
    }).decode("utf-8"))
    return 0


def _write_apply_journal(path: Path, journal: dict[str, Any]) -> None:
    temporary = _write_staged(path, canonical_json_bytes(journal))
    os.replace(temporary, path)
    with path.open("rb") as handle:
        os.fsync(handle.fileno())
    _fsync_directory(path.parent)


def _immutable_decision_segment(evidence_dir: str, decisions: dict[str, Any]) -> tuple[str, Path]:
    """Persist the decision input before a database row may refer to it."""
    root = Path(evidence_dir)
    rows = [{"evidence_id": canonical_sha256(row), "decision": row}
            for row in decisions.get("decisions", [])]
    data = _jsonl_bytes(sorted(rows, key=lambda row: row["evidence_id"]))
    digest = hashlib.sha256(data).hexdigest()
    target = root / "segments" / f"{digest}.jsonl"
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        if target.read_bytes() != data:
            raise ValueError("content-addressed decision evidence collision")
    else:
        temporary = _write_staged(target, data)
        os.replace(temporary, target)
        directory_fd = os.open(target.parent, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    entry = canonical_json_bytes({"segment_sha256": digest, "row_count": len(rows)})
    index = root / "index.jsonl"
    if not index.exists() or entry not in index.read_bytes().splitlines(keepends=True):
        _append_fsync(index, entry)
    return digest, target
def _verified_ledger_tail(path: Path) -> str | None:
    """Return the exact canonical hash-chain tail, or None for a missing ledger."""
    if not path.exists():
        return None
    previous = None
    lines = path.read_bytes().splitlines(keepends=True)
    if not lines:
        raise ValueError("affiliation ledger is empty")
    for raw in lines:
        entry = json.loads(raw)
        if canonical_json_bytes(entry) != raw:
            raise ValueError("affiliation ledger entry is not canonical JSON")
        claimed = entry.get("ledger_head")
        payload = dict(entry)
        payload.pop("ledger_head", None)
        if canonical_sha256(payload) != claimed:
            raise ValueError("affiliation ledger entry digest mismatch")
        if previous is not None and entry.get("previous_ledger_head") != previous:
            raise ValueError("affiliation ledger hash chain is discontinuous")
        previous = claimed
    return previous




def _quarantine_unreferenced_evidence(journal: dict[str, Any]) -> None:
    """Quarantine only evidence that no committed cohort join references."""
    segment = Path(journal["evidence_segment"])
    if not segment.exists():
        return
    database = journal.get("database")
    if database and Path(database).exists():
        connection = sqlite3.connect(database)
        try:
            table = connection.execute(
                "SELECT 1 FROM sqlite_master WHERE type='table' "
                "AND name='affiliation_cohort_dispositions'").fetchone()
            referenced = table and connection.execute(
                "SELECT 1 FROM affiliation_cohort_dispositions "
                "WHERE evidence_segment_sha256=? LIMIT 1",
                (journal.get("evidence_segment_sha256"),)).fetchone()
        finally:
            connection.close()
        if referenced:
            return
    quarantine = segment.parent.parent / "quarantine"
    quarantine.mkdir(parents=True, exist_ok=True)
    target = quarantine / segment.name
    if target.exists() and target.read_bytes() != segment.read_bytes():
        raise ValueError("quarantine evidence collision")
    os.replace(segment, target)
    index = segment.parent.parent / "index.jsonl"
    if index.exists():
        digest = journal.get("evidence_segment_sha256")
        retained = [
            raw for raw in index.read_bytes().splitlines(keepends=True)
            if json.loads(raw).get("segment_sha256") != digest
        ]
        temporary = _write_staged(index, b"".join(retained))
        os.replace(temporary, index)
        _fsync_directory(index.parent)
    _fsync_directory(quarantine)


def _recover_investigated_apply(journal_path: Path) -> None:
    if not journal_path.exists():
        return
    journal = json.loads(journal_path.read_text(encoding="utf-8"))
    state = journal.get("state")
    if state == "PREPARED":
        ledger_entry = base64.b64decode(journal["ledger_entry"])
        ledger = Path(journal["ledger"])
        if not ledger.exists() or ledger_entry not in ledger.read_bytes().splitlines(keepends=True):
            _quarantine_unreferenced_evidence(journal)
            for entry in journal.get("publication", []):
                Path(entry["temporary"]).unlink(missing_ok=True)
            descriptor = journal.get("descriptor")
            if descriptor:
                Path(descriptor["temporary"]).unlink(missing_ok=True)
            journal_path.unlink()
            _fsync_directory(journal_path.parent)
            return
        journal["state"] = "LEDGER_DURABLE"
        _write_apply_journal(journal_path, journal)
        state = "LEDGER_DURABLE"
    if state == "LEDGER_DURABLE":
        updated = json.loads(base64.b64decode(journal["publication"][0]["after"]))
        _apply_decisions_to_db(
            journal["database"], journal["eligible"], journal["resolutions"],
            journal["expected"], updated, journal["timestamp"],
            journal["decision_segment_sha256"],
            decision_artifact_sha256=journal["decision_artifact_sha256"],
            evidence_segment_sha256=journal["evidence_segment_sha256"],
            ledger_head=journal["ledger_head"],
            cohort_version=journal["cohort_version"],
            cohort_sha256=journal["cohort_sha256"],
            generation_descriptor_sha256=journal["generation_descriptor_sha256"],
            generation_id=journal["generation_id"],
            dispositions=journal["dispositions"],
            project_registry=journal["project_registry"],
        )
        journal["state"] = "DB_COMMITTED"
        _write_apply_journal(journal_path, journal)
        state = "DB_COMMITTED"
    if state == "DB_COMMITTED":
        for entry in journal["publication"]:
            temporary, target = Path(entry["temporary"]), Path(entry["target"])
            if temporary.exists():
                os.replace(temporary, target)
                _fsync_directory(target.parent)
            elif not target.exists() or target.read_bytes() != base64.b64decode(entry["after"]):
                raise ValueError("cannot recover committed publication")
        descriptor = journal.get("descriptor")
        if descriptor:
            temporary, target = Path(descriptor["temporary"]), Path(descriptor["target"])
            if temporary.exists():
                os.replace(temporary, target)
                _fsync_directory(target.parent)
            elif not target.exists() or target.read_bytes() != base64.b64decode(descriptor["after"]):
                raise ValueError("cannot recover committed generation descriptor")
        journal["state"] = "DESCRIPTOR_COMMITTED"
        _write_apply_journal(journal_path, journal)
        state = "DESCRIPTOR_COMMITTED"
    if state == "DESCRIPTOR_COMMITTED":
        journal_path.unlink()
        _fsync_directory(journal_path.parent)
        return
    raise ValueError("unknown investigated-apply journal state")


def _eligible_resolution_map(
        decisions: list[dict[str, Any]],
        resolutions: list[dict[str, Any]]) -> dict[tuple[Any, Any], dict[str, Any]]:
    """Require one successful, organization-bearing result per eligible decision."""
    expected_keys = [
        (row.get("query"), row.get("country"))
        for row in decisions
        if row.get("action") == "eligible_identity_only"
    ]
    actual_rows = [
        row for row in resolutions
        if isinstance(row, dict)
    ]
    actual_keys = [
        (row.get("query"), row.get("country"))
        for row in actual_rows
    ]
    if (
            any(
                not isinstance(query, str) or not isinstance(country, str)
                for query, country in expected_keys + actual_keys)
            or len(expected_keys) != len(set(expected_keys))
            or len(actual_keys) != len(set(actual_keys))
            or set(actual_keys) != set(expected_keys)
            or len(actual_rows) != len(expected_keys)
            or any(
                row.get("action") != "eligible_identity_only"
                or not isinstance(row.get("organization_id"), str)
                or not row["organization_id"]
                for row in actual_rows)):
        raise ValueError(
            "INCOMPLETE_IDENTITY_TRANSITION: every eligible decision requires "
            "one successful organization-bearing resolution")
    return {
        (row["query"], row["country"]): row
        for row in actual_rows
    }


def _apply_decisions_to_db(
        database: str, decisions: list[dict[str, Any]],
        resolutions: list[dict[str, Any]], expected: dict[str, str],
        registry: dict[str, Any], timestamp: str,
        decision_segment_sha256: str, *,
        decision_artifact_sha256: str,
        evidence_segment_sha256: str,
        ledger_head: str,
        cohort_version: str,
        cohort_sha256: str,
        generation_descriptor_sha256: str,
        generation_id: str,
        dispositions: list[dict[str, Any]],
        project_registry: bool) -> None:
    """Project one head-bound decision segment and its complete cohort join atomically."""
    from build_bibliography_db import (
        AFFILIATION_COHORT_DISPOSITION_SQL,
        project_affiliation_registry,
        recount_affiliation_pending_cases,
    )

    by_key = _eligible_resolution_map(decisions, resolutions)
    connection = sqlite3.connect(database)
    try:
        connection.execute("PRAGMA foreign_keys=ON")
        connection.execute("BEGIN IMMEDIATE")
        metadata = connection.execute(
            "SELECT registry_sha256,event_head,ledger_head,cohort_sha256,"
            "generation_descriptor_sha256,generation_id "
            "FROM affiliation_registry_metadata WHERE singleton=1").fetchone()
        before = (
            expected["registry_sha256"], expected["event_head"],
            expected["ledger_head"], expected["cohort_head"],
            expected["generation_descriptor_sha256"], expected["generation_id"],
        )
        after = (
            canonical_sha256(registry), registry["event_head"], ledger_head, cohort_sha256,
            generation_descriptor_sha256, generation_id,
        )
        if metadata != before:
            if metadata == after:
                count = connection.execute(
                    "SELECT COUNT(*) FROM affiliation_cohort_dispositions "
                    "WHERE cohort_sha256=? AND decision_sha256=?",
                    (cohort_sha256, decision_artifact_sha256)).fetchone()[0]
                if count == len(dispositions):
                    connection.rollback()
                    return
            raise ValueError(
                "HEAD_MISMATCH: database registry/event/ledger/cohort heads do not match")
        connection.execute(AFFILIATION_COHORT_DISPOSITION_SQL)
        if project_registry:
            project_affiliation_registry(
                connection, registry=registry, ensure_schema=False, reresolve=False)
        connection.execute(
            "UPDATE affiliation_resolution_decisions "
            "SET reason_code='global_unique_missing_country' "
            "WHERE reason_code='offline_registry_exact_alias' "
            "AND observation_id IN (SELECT observation_id FROM observed_affiliations "
            "WHERE observed_country_code='')")
        connection.execute(
            "UPDATE affiliation_pending_cases "
            "SET reason_code='global_unique_missing_country' "
            "WHERE status='resolved' AND resolved_event_id IN "
            "(SELECT decision_id FROM affiliation_resolution_decisions "
            "WHERE reason_code='global_unique_missing_country')")
        terminal: dict[str, tuple[str, str]] = {}
        pending_ids: set[str] = set()
        for decision in decisions:
            key = (decision["query"], decision["country"])
            resolution = by_key.get(key)
            if decision.get("action") != "eligible_identity_only" or not resolution:
                continue
            organization_id = resolution["organization_id"]
            exists = connection.execute(
                "SELECT 1 FROM affiliation_organizations WHERE organization_id=?",
                (organization_id,)).fetchone()
            if not exists:
                raise ValueError("identity transition organization is not projected in SQLite")
            observations = connection.execute(
                "SELECT o.observation_id,o.current_decision_id,p.pending_id "
                "FROM observed_affiliations o "
                "JOIN affiliation_pending_observations l USING(observation_id) "
                "JOIN affiliation_pending_cases p USING(pending_id) "
                "WHERE o.is_current=1 AND o.raw_name=? AND o.observed_country_code=? "
                "AND o.resolution_status IN ('unseen','ambiguous')",
                key).fetchall()
            for observation_id, previous, pending_id in observations:
                sequence = connection.execute(
                    "SELECT COALESCE(MAX(decision_sequence),0)+1 "
                    "FROM affiliation_resolution_decisions WHERE observation_id=?",
                    (observation_id,)).fetchone()[0]
                decision_id = hashlib.sha256(canonical_json_bytes(
                    ["automatic-identity", observation_id, decision_segment_sha256,
                     organization_id])).hexdigest()
                connection.execute(
                    "INSERT OR IGNORE INTO affiliation_resolution_decisions "
                    "(decision_id,observation_id,decision_sequence,outcome,"
                    "selected_organization_id,reason_code,confidence,registry_sha256,"
                    "policy_version,effective_date,decided_at,previous_decision_id) "
                    "VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                    (decision_id, observation_id, sequence, "resolved", organization_id,
                     "automatic_dual_corroborated_identity", 1.0,
                     canonical_sha256(registry), registry["policy_version"],
                     timestamp[:10], timestamp, previous or ""))
                connection.execute(
                    "INSERT OR IGNORE INTO affiliation_decision_candidates "
                    "(decision_id,organization_id,candidate_rank,reason_code) "
                    "VALUES (?,?,?,?)",
                    (decision_id, organization_id, 1,
                     "automatic_dual_corroborated_identity"))
                connection.execute(
                    "UPDATE observed_affiliations SET resolved_organization_id=?,"
                    "resolution_status='resolved',current_decision_id=?,registry_sha256=?,"
                    "policy_version=? WHERE observation_id=?",
                    (organization_id, decision_id, canonical_sha256(registry),
                     registry["policy_version"], observation_id))
                pending_ids.add(pending_id)
                terminal[pending_id] = ("resolved", decision_id)
        recount_affiliation_pending_cases(connection, pending_ids, terminal, timestamp)
        for disposition in dispositions:
            pending_id = disposition.get("pending_id")
            value = disposition.get("disposition")
            if not isinstance(pending_id, str) or not isinstance(value, str):
                raise ValueError("invalid closed cohort disposition")
            row_sha256 = canonical_sha256(disposition)
            connection.execute(
                "INSERT OR IGNORE INTO affiliation_cohort_dispositions "
                "(cohort_sha256,pending_id,disposition,decision_sha256,"
                "decision_row_sha256,evidence_segment_sha256,decided_at) "
                "VALUES (?,?,?,?,?,?,?)",
                (cohort_sha256, pending_id, value, decision_artifact_sha256,
                 row_sha256, evidence_segment_sha256, timestamp))
            saved = connection.execute(
                "SELECT disposition,decision_sha256,decision_row_sha256,"
                "evidence_segment_sha256,decided_at "
                "FROM affiliation_cohort_dispositions "
                "WHERE cohort_sha256=? AND pending_id=?",
                (cohort_sha256, pending_id)).fetchone()
            if saved != (
                    value, decision_artifact_sha256, row_sha256,
                    evidence_segment_sha256, timestamp):
                raise ValueError("closed cohort disposition collision")
        connection.execute(
            "UPDATE affiliation_registry_metadata SET registry_sha256=?,event_head=?,"
            "ledger_head=?,cohort_version=?,cohort_sha256=?,"
            "generation_descriptor_sha256=?,generation_id=?,projected_at=? "
            "WHERE singleton=1",
            (canonical_sha256(registry), registry["event_head"], ledger_head,
             cohort_version, cohort_sha256, generation_descriptor_sha256,
             generation_id, timestamp))
        connection.commit()
    except BaseException:
        connection.rollback()
        raise
    finally:
        connection.close()


def command_recover_investigated(args: argparse.Namespace) -> int:
    """Recover only a proven descriptor-last apply journal under the writer lock."""
    journal = Path(args.journal)
    with affiliation_registry.bibliography_writer_lock(Path(args.db)):
        _recover_investigated_apply(journal)
    sys.stdout.write(canonical_json_bytes({
        "journal": str(journal), "recovered": not journal.exists(),
        "lock_protocol": "stable-flock-v1",
    }).decode("utf-8"))
    return 0
def _database_apply_heads(database: Path) -> dict[str, str]:
    connection = sqlite3.connect(database)
    try:
        row = connection.execute(
            "SELECT registry_sha256,event_head,ledger_head,cohort_sha256,"
            "generation_descriptor_sha256,generation_id "
            "FROM affiliation_registry_metadata WHERE singleton=1").fetchone()
    finally:
        connection.close()
    if row is None or any(not isinstance(value, str) for value in row):
        raise ValueError("affiliation generation metadata is incomplete")
    return dict(zip((
        "registry_sha256", "event_head", "ledger_head", "cohort_head",
        "generation_descriptor_sha256", "generation_id",
    ), row))


def _stage_publication(path: Path, data: bytes, *, immutable: bool = False) -> dict[str, str]:
    path.parent.mkdir(parents=True, exist_ok=True)
    if immutable and path.exists() and path.read_bytes() != data:
        raise ValueError(f"immutable publication already exists with different bytes: {path}")
    temporary = _write_staged(path, data)
    return {
        "target": str(path),
        "temporary": str(temporary),
        "after": base64.b64encode(data).decode("ascii"),
    }



def command_apply_investigated(args: argparse.Namespace) -> int:
    raw_decisions = Path(args.decisions).read_bytes()
    decisions = json.loads(raw_decisions)
    if canonical_json_bytes(decisions) != raw_decisions:
        raise ValueError("decision artifact is not canonical JSON")
    rows = decisions.get("decisions")
    if not isinstance(rows, list) or decisions.get(
            "decisions_sha256") != canonical_sha256(rows):
        raise ValueError("DECISION_DIGEST_MISMATCH: recomputed decision digest differs")
    current = load_registry(args.registry)
    artifact_heads = decisions.get("heads")
    expected = {
        "registry_sha256": args.expected_registry_sha256,
        "event_head": args.expected_event_head,
        "ledger_head": getattr(args, "expected_ledger_head", ""),
        "cohort_head": getattr(args, "expected_cohort_head", ""),
        "generation_descriptor_sha256": "",
        "generation_id": "",
    }
    if isinstance(artifact_heads, dict):
        if artifact_heads.get("registry_sha256") != canonical_sha256(current) or (
                artifact_heads.get("event_head") != current["event_head"]):
            raise ValueError("HEAD_MISMATCH: decision registry/event heads are stale")
        expected["registry_sha256"] = artifact_heads["registry_sha256"]
        expected["event_head"] = artifact_heads["event_head"]
    elif (
            decisions.get("registry_sha256") != expected["registry_sha256"]
            or canonical_sha256(current) != expected["registry_sha256"]
            or current["event_head"] != expected["event_head"]
            or decisions.get("ledger_head", "") != expected["ledger_head"]
            or decisions.get("cohort_head", "") != expected["cohort_head"]):
        raise ValueError("HEAD_MISMATCH: registry/event/ledger/cohort heads do not match")
    if decisions.get("unclassified_count", 0):
        raise ValueError("UNCLASSIFIED cohort decisions cannot be applied")
    eligible = [row for row in rows if row.get("action") == "eligible_identity_only"]
    if any(row.get("relationship") or row.get("relationship_payload") for row in rows):
        raise ValueError(
            "RELATIONSHIP_PAYLOAD_FORBIDDEN: automatic relationship actions are forbidden")
    if len(eligible) > min(args.max_apply, 100):
        raise ValueError("BATCH_LIMIT_EXCEEDED: automatic apply batch exceeds 100")
    if getattr(args, "canary", False) and len(eligible) > 50:
        raise ValueError("CANARY_LIMIT_EXCEEDED: canary contains more than 50 decisions")
    transition = getattr(affiliation_registry, "apply_identity_transitions", None)
    if eligible and transition is None:
        raise ValueError(
            "IDENTITY_TRANSITION_ENGINE_UNAVAILABLE: decisions remain pending")
    if args.dry_run:
        if isinstance(artifact_heads, dict) and getattr(args, "db", None) and (
                artifact_heads.get("database_sha256") != _database_sha256(args.db)):
            raise ValueError("HEAD_MISMATCH: decision database head is stale")
        if not eligible:
            result = {
                "kind": "automatic_identity_apply",
                "eligible_count": 0,
                "applied_count": 0,
                "vacuous_noop": True,
                "durable_finalization_required": True,
                "decisions_sha256": decisions["decisions_sha256"],
                "cohort_sha256": decisions.get("cohort_sha256", ""),
            }
        else:
            result = transition(
                current, eligible, timestamp=args.timestamp, dry_run=True)
        sys.stdout.write(canonical_json_bytes(result).decode("utf-8"))
        return 0
    required = (
        "db", "evidence_dir", "ledger", "corrections", "baseline", "receipt",
        "effective_date", "generation_descriptor",
    )
    if any(not getattr(args, name, None) for name in required):
        raise ValueError(
            "non-dry-run apply requires DB, evidence, ledger, publication, and "
            "generation descriptor paths")
    database = Path(args.db)
    descriptor_path = Path(args.generation_descriptor)
    journal_path = Path(
        getattr(args, "journal", "")
        or str(Path(args.decisions).with_suffix(".apply.journal")))
    lock_fd = affiliation_registry.acquire_bibliography_writer_lock(database)
    receipt_value: dict[str, Any] | None = None
    try:
        _recover_investigated_apply(journal_path)
        current = load_registry(args.registry)
        if canonical_sha256(current) != expected["registry_sha256"] or (
                current["event_head"] != expected["event_head"]):
            raise ValueError("HEAD_MISMATCH: registry changed before apply")
        if isinstance(artifact_heads, dict) and (
                artifact_heads.get("database_sha256") != _database_sha256(database)):
            raise ValueError("HEAD_MISMATCH: decision database head is stale")
        expected.update(_database_apply_heads(database))
        if (
                expected["registry_sha256"] != canonical_sha256(current)
                or expected["event_head"] != current["event_head"]):
            raise ValueError("HEAD_MISMATCH: database and registry heads differ")
        registry_ledger_head = str(
            current.get("ledger_head") or current["event_head"])
        if expected["ledger_head"] != registry_ledger_head:
            raise ValueError(
                "HEAD_MISMATCH: database and registry ledger heads differ")
        ledger_tail = _verified_ledger_tail(Path(args.ledger))
        if ledger_tail is None:
            if current.get("ledger_head"):
                raise ValueError(
                    "HEAD_MISMATCH: bound affiliation ledger is missing")
        elif ledger_tail != expected["ledger_head"]:
            raise ValueError(
                "HEAD_MISMATCH: affiliation ledger tail differs")
        if eligible:
            result = transition(
                current, eligible, timestamp=args.timestamp, dry_run=False)
            updated = result.get("registry") if isinstance(result, dict) else None
            resolutions = result.get("resolutions") if isinstance(result, dict) else None
        else:
            updated = json.loads(canonical_json_bytes(current))
            resolutions = []
        if not isinstance(updated, dict) or not isinstance(resolutions, list):
            raise ValueError("identity transition returned invalid publication plan")
        _eligible_resolution_map(eligible, resolutions)
        organization_count_before_consolidation = len(updated["organizations"])
        proposal_count_before_consolidation = len(updated["relationship_proposals"])
        updated = affiliation_registry.consolidate_pinned_roots(
            updated, timestamp=args.timestamp, actor="pinned-root-consolidation")
        consolidated_root_count = sum(
            event.get("type") == "pinned_root_consolidated"
            and event.get("timestamp") == args.timestamp
            for event in updated["events"])
        redirected_root_count = (
            organization_count_before_consolidation - len(updated["organizations"]))
        superseded_proposal_count = (
            proposal_count_before_consolidation
            - len(updated["relationship_proposals"]))
        decision_segment_sha256, evidence_segment = _immutable_decision_segment(
            args.evidence_dir, decisions)
        cohort_sha256 = str(decisions.get("cohort_sha256") or "")
        if not cohort_sha256:
            raise ValueError("closed cohort hash is required")
        cohort_version = "affiliation-frozen-cohort-v1"
        ledger_payload = {
            "schema_version": "affiliation-ledger-1",
            "kind": "automatic_identity_apply",
            "previous_ledger_head": expected["ledger_head"],
            "decision_artifact_sha256": decisions["decisions_sha256"],
            "decision_segment_sha256": decision_segment_sha256,
            "evidence_segment_sha256": evidence_segment.name[:-6],
            "cohort_version": cohort_version,
            "cohort_sha256": cohort_sha256,
            "expected": expected,
            "timestamp": args.timestamp,
        }
        ledger_head = canonical_sha256(ledger_payload)
        ledger_entry = canonical_json_bytes({
            **ledger_payload, "ledger_head": ledger_head})
        updated["ledger_head"] = ledger_head
        updated["cohort_version"] = cohort_version
        updated["cohort_sha256"] = cohort_sha256
        validate_registry(updated, effective_date=args.effective_date)
        registry_sha256_after = canonical_sha256(updated)
        descriptor_body = {
            "schema_version": "affiliation-generation-1",
            "registry_sha256": registry_sha256_after,
            "event_head": updated["event_head"],
            "ledger_head": ledger_head,
            "cohort_version": cohort_version,
            "cohort_sha256": cohort_sha256,
            "decision_artifact_sha256": decisions["decisions_sha256"],
            "decision_segment_sha256": decision_segment_sha256,
            "database_base_sha256": artifact_heads.get(
                "database_sha256", "") if isinstance(artifact_heads, dict) else "",
            "journal": str(journal_path),
            "committed_at": args.timestamp,
        }
        generation_id = canonical_sha256(descriptor_body)
        descriptor_value = {**descriptor_body, "generation_id": generation_id}
        descriptor_data = canonical_json_bytes(descriptor_value)
        generation_descriptor_sha256 = hashlib.sha256(descriptor_data).hexdigest()
        disposition_counts: dict[str, int] = {}
        for row in rows:
            value = str(row.get("disposition") or "")
            disposition_counts[value] = disposition_counts.get(value, 0) + 1
        receipt_value = {
            "schema_version": "affiliation-apply-receipt-1",
            "kind": "automatic_identity_apply",
            "registry_sha256_before": canonical_sha256(current),
            "registry_sha256_after": registry_sha256_after,
            "event_head": updated["event_head"],
            "ledger_head": ledger_head,
            "cohort_version": cohort_version,
            "cohort_sha256": cohort_sha256,
            "decision_artifact_sha256": decisions["decisions_sha256"],
            "decision_segment_sha256": decision_segment_sha256,
            "evidence_segment_sha256": evidence_segment.name[:-6],
            "eligible_count": len(eligible),
            "applied_count": len(eligible),
            "vacuous_noop": not eligible,
            "pinned_consolidation_event_count": consolidated_root_count,
            "redirected_root_count": redirected_root_count,
            "identity_superseded_proposal_count": superseded_proposal_count,
            "disposition_counts": disposition_counts,
            "unclassified_count": disposition_counts.get("UNCLASSIFIED", 0),
            "generation_descriptor_sha256": generation_descriptor_sha256,
            "generation_id": generation_id,
            "timestamp": args.timestamp,
        }
        corrections = correction_projection(updated)
        outputs = [
            (Path(args.registry), canonical_json_bytes(updated), False),
            (Path(args.corrections), _jsonl_bytes(corrections), False),
            (Path(args.baseline), canonical_json_bytes(_preserve_database_baseline(
                args.baseline, baseline_projection(
                    updated, corrections, effective_date=args.effective_date))), False),
            (Path(args.receipt), canonical_json_bytes(receipt_value), True),
        ]
        publication = [
            _stage_publication(path, data, immutable=immutable)
            for path, data, immutable in outputs
        ]
        descriptor = _stage_publication(
            descriptor_path, descriptor_data, immutable=False)
        journal = {
            "state": "PREPARED",
            "evidence_segment": str(evidence_segment),
            "evidence_segment_sha256": evidence_segment.name[:-6],
            "publication": publication,
            "descriptor": descriptor,
            "database": str(database),
            "ledger": str(Path(args.ledger)),
            "ledger_entry": base64.b64encode(ledger_entry).decode("ascii"),
            "ledger_head": ledger_head,
            "expected": expected,
            "eligible": eligible,
            "resolutions": resolutions,
            "dispositions": rows,
            "project_registry": canonical_sha256(updated) != expected["registry_sha256"],
            "timestamp": args.timestamp,
            "decision_segment_sha256": decision_segment_sha256,
            "decision_artifact_sha256": decisions["decisions_sha256"],
            "cohort_version": cohort_version,
            "cohort_sha256": cohort_sha256,
            "generation_descriptor_sha256": generation_descriptor_sha256,
            "generation_id": generation_id,
        }
        _write_apply_journal(journal_path, journal)
        ledger_path = Path(args.ledger)
        if not ledger_path.exists() or (
                ledger_entry not in ledger_path.read_bytes().splitlines(keepends=True)):
            _append_fsync(ledger_path, ledger_entry)
        journal["state"] = "LEDGER_DURABLE"
        _write_apply_journal(journal_path, journal)
        _apply_decisions_to_db(
            args.db, eligible, resolutions, expected, updated, args.timestamp,
            decision_segment_sha256,
            decision_artifact_sha256=decisions["decisions_sha256"],
            evidence_segment_sha256=evidence_segment.name[:-6],
            ledger_head=ledger_head,
            cohort_version=cohort_version,
            cohort_sha256=cohort_sha256,
            generation_descriptor_sha256=generation_descriptor_sha256,
            generation_id=generation_id,
            dispositions=rows,
            project_registry=canonical_sha256(updated) != expected["registry_sha256"],
        )
        journal["state"] = "DB_COMMITTED"
        _write_apply_journal(journal_path, journal)
        _recover_investigated_apply(journal_path)
    finally:
        affiliation_registry.release_bibliography_writer_lock(database, lock_fd)
    sys.stdout.write(canonical_json_bytes(receipt_value).decode("utf-8"))
    return 0

def _append_fsync(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("ab") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())


def _write_staged(path: Path, data: bytes) -> Path:
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
    except BaseException:
        Path(temporary).unlink(missing_ok=True)
        raise
    return Path(temporary)


def _recover_publication(journal_path: Path) -> None:
    if not journal_path.exists():
        return
    journal = json.loads(journal_path.read_text(encoding="utf-8"))
    for entry in journal["entries"]:
        Path(entry["temporary"]).unlink(missing_ok=True)
        target = Path(entry["target"])
        if not entry["existed"]:
            target.unlink(missing_ok=True)
            continue
        old = base64.b64decode(entry["old_bytes"])
        replacement = _write_staged(target, old)
        os.replace(replacement, target)
    journal_path.unlink(missing_ok=True)


def command_transition_relationship_policy(args: argparse.Namespace) -> int:
    """Atomically append the one-shot official-only relationship-policy transition."""
    registry_path = Path(args.registry)
    current = load_registry(registry_path)
    if args.expected_registry_sha256 != canonical_sha256(current):
        raise ValueError("expected registry SHA-256 does not match")
    if args.expected_event_head != current["event_head"]:
        raise ValueError("expected event head does not match")
    updated = transition_relationship_policy(
        current, timestamp=args.timestamp, effective_date=args.effective_date,
        actor=args.actor, expected_event_head=args.expected_event_head)
    corrections = correction_projection(updated)
    transition = updated["events"][-1]["payload"]
    receipt = {
        "schema_version": "affiliation-2",
        "transition": "official-relationships-v1",
        "registry_sha256_before": canonical_sha256(current),
        "registry_sha256_after": canonical_sha256(updated),
        "event_head_before": current["event_head"],
        "event_head_after": updated["event_head"],
        "timestamp": args.timestamp, "effective_date": args.effective_date,
        "legacy_count": transition["legacy_count"],
        "official_retained_count": transition["official_retained_count"],
        "demoted_or_superseded_count": transition["demoted_or_superseded_count"],
        "equation": (f'{transition["legacy_count"]} = '
                     f'{transition["official_retained_count"]} + '
                     f'{transition["demoted_or_superseded_count"]}'),
        "pre_relationship_ids_sha256": transition["pre_relationship_ids_sha256"],
    }
    if args.dry_run:
        print(canonical_json_bytes(receipt).decode("utf-8"), end="")
        return 0
    database = Path(getattr(args, "db", "") or
                    Path(__file__).resolve().parents[1] / ".cache" / "bibliography.sqlite3")
    journal_path = registry_path.with_suffix(registry_path.suffix + ".relationship-policy.journal")
    lock_fd = affiliation_registry.acquire_bibliography_writer_lock(database)
    try:
        _recover_publication(journal_path)
        if Path(args.receipt).exists():
            raise ValueError("transition receipt already exists and is immutable")
        current = load_registry(registry_path)
        if (args.expected_registry_sha256 != canonical_sha256(current)
                or args.expected_event_head != current["event_head"]):
            raise ValueError("registry changed before transition publication")
        updated = transition_relationship_policy(
            current, timestamp=args.timestamp, effective_date=args.effective_date,
            actor=args.actor, expected_event_head=args.expected_event_head)
        corrections = correction_projection(updated)
        outputs = [
            (registry_path, canonical_json_bytes(updated)),
            (Path(args.corrections), _jsonl_bytes(corrections)),
            (Path(args.baseline), canonical_json_bytes(_preserve_database_baseline(
                args.baseline, baseline_projection(
                    updated, corrections, effective_date=args.effective_date)))),
            (Path(args.receipt), canonical_json_bytes(receipt)),
        ]
        entries = [{"target": str(path), "temporary": str(_write_staged(path, data)),
                    "old_bytes": base64.b64encode(path.read_bytes() if path.exists() else b"").decode("ascii"),
                    "existed": path.exists()}
                   for path, data in outputs]
        journal_path.write_bytes(canonical_json_bytes({"entries": entries}))
        with journal_path.open("rb") as handle:
            os.fsync(handle.fileno())
        try:
            for entry in entries:
                os.replace(entry["temporary"], entry["target"])
        except BaseException:
            _recover_publication(journal_path)
            raise
        journal_path.unlink()
    finally:
        affiliation_registry.release_bibliography_writer_lock(database, lock_fd)
    return 0

def command_apply_approved(args: argparse.Namespace) -> int:
    registry_path = Path(args.registry)
    database = Path(getattr(args, "db", "") or
                    Path(__file__).resolve().parents[1] / ".cache" / "bibliography.sqlite3")
    journal_path = registry_path.with_suffix(registry_path.suffix + ".apply-approved.journal")
    lock_fd = affiliation_registry.acquire_bibliography_writer_lock(database)
    try:
        _recover_publication(journal_path)
        if Path(args.receipt).exists():
            raise ValueError("approval receipt already exists and is immutable")
        current = load_registry(registry_path)
        if args.expected_registry_sha256 != canonical_sha256(current):
            raise ValueError("expected registry SHA-256 does not match")
        if args.expected_event_head != current["event_head"]:
            raise ValueError("expected event head does not match")
        updated = promote_approved(current, _load_corrections(args.approvals), timestamp=args.timestamp)
        validate_registry(updated, effective_date=args.effective_date)
        corrections = correction_projection(updated)
        receipt = {
            "schema_version": "affiliation-2", "registry_sha256_before": canonical_sha256(current),
            "event_head_before": current["event_head"], "registry_sha256_after": canonical_sha256(updated),
            "event_head_after": updated["event_head"], "approvals_sha256": hashlib.sha256(
                Path(args.approvals).read_bytes()).hexdigest(), "timestamp": args.timestamp,
        }
        outputs = [(registry_path, canonical_json_bytes(updated)),
                   (Path(args.corrections), _jsonl_bytes(corrections)),
                   (Path(args.baseline), canonical_json_bytes(
                       baseline_projection(updated, corrections, effective_date=args.effective_date))),
                   (Path(args.receipt), canonical_json_bytes(receipt))]
        entries = [{"target": str(path), "temporary": str(_write_staged(path, data)),
                    "old_bytes": base64.b64encode(path.read_bytes() if path.exists() else b"").decode("ascii"),
                    "existed": path.exists()}
                   for path, data in outputs]
        journal_path.write_bytes(canonical_json_bytes({"entries": entries}))
        with journal_path.open("rb") as handle:
            os.fsync(handle.fileno())
        try:
            for entry in entries:
                os.replace(entry["temporary"], entry["target"])
        except BaseException:
            _recover_publication(journal_path)
            raise
        journal_path.unlink()
    finally:
        affiliation_registry.release_bibliography_writer_lock(database, lock_fd)
    return 0


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser()
    sub = result.add_subparsers(dest="command", required=True)
    imp = sub.add_parser("import")
    imp.add_argument("--source", required=True); imp.add_argument("--legacy-aliases")
    imp.add_argument("--registry", required=True); imp.add_argument("--corrections", required=True)
    imp.add_argument("--baseline", required=True); imp.add_argument("--offline", action="store_true")
    imp.add_argument("--operator-curated", action="store_true",
                     help="accept only the pinned 4,747-record operator-curated source")
    imp.add_argument("--check", action="store_true"); imp.add_argument("--timestamp", default="1970-01-01T00:00:00Z")
    imp.add_argument("--effective-date", default="1970-01-01"); imp.add_argument("--version", type=int, default=1)
    imp.set_defaults(func=command_import)
    oracle = sub.add_parser("check-oracles")
    oracle.add_argument("--oracle-dir", required=True)
    oracle.set_defaults(func=command_check_oracles)
    pin_oracles = sub.add_parser("pin-oracles")
    pin_oracles.add_argument("--oracle-dir", required=True)
    pin_oracles.set_defaults(func=command_pin_oracles)
    val = sub.add_parser("validate")
    val.add_argument("--source", required=True); val.add_argument("--registry", required=True)
    val.add_argument("--corrections", required=True); val.add_argument("--baseline", required=True)
    val.add_argument("--strict", action="store_true"); val.set_defaults(func=command_validate)
    snapshot = sub.add_parser("snapshot-db-baseline")
    snapshot.add_argument("--db", required=True)
    snapshot.add_argument("--registry", required=True)
    snapshot.add_argument("--baseline", required=True)
    snapshot.add_argument("--captured-at", required=True)
    snapshot.set_defaults(func=command_snapshot_db_baseline)
    freeze = sub.add_parser("freeze-pending-cohort")
    freeze.add_argument("--db", required=True); freeze.add_argument("--registry", required=True)
    freeze.add_argument("--cohort", required=True); freeze.add_argument("--timestamp", required=True)
    freeze.set_defaults(func=command_freeze_pending_cohort)
    report = sub.add_parser("report")
    report.add_argument("--registry", required=True)
    report.add_argument("--db")
    report.add_argument("--cohort")
    report.add_argument("--decisions")
    report.add_argument("--ledger")
    report.add_argument("--generation-descriptor")
    report.set_defaults(func=command_report)
    resolve = sub.add_parser("resolve-pending")
    resolve.add_argument("--db"); resolve.add_argument("--registry", required=True); resolve.add_argument("--proposals", required=True)
    resolve.add_argument("--allow-network", action="store_true"); resolve.add_argument("--name", action="append", default=[])
    resolve.add_argument("--country", default=""); resolve.add_argument("--retrieved-at", required=True)
    resolve.add_argument("--request-budget", type=int, default=100)
    resolve.add_argument("--max-retries", type=int, default=1)
    resolve.add_argument("--retry-backoff-seconds", type=float, default=0.0)
    resolve.add_argument("--circuit-breaker-failures", type=int, default=5)
    resolve.add_argument("--oracle-dir", required=True)
    resolve.add_argument("--evidence-dir")
    resolve.add_argument("--cohort")
    resolve.set_defaults(func=command_resolve_pending)
    investigate = sub.add_parser("investigate")
    investigate.add_argument("--db", required=True); investigate.add_argument("--registry", required=True)
    investigate.add_argument("--proposals", required=True); investigate.add_argument("--cohort", required=True)
    investigate.add_argument("--allow-network", action="store_true"); investigate.add_argument("--name", action="append", default=[])
    investigate.add_argument("--country", default=""); investigate.add_argument("--retrieved-at", required=True)
    investigate.add_argument("--request-budget", type=int, default=100)
    investigate.add_argument("--max-retries", type=int, default=1)
    investigate.add_argument("--retry-backoff-seconds", type=float, default=0.0)
    investigate.add_argument("--circuit-breaker-failures", type=int, default=5)
    investigate.add_argument("--oracle-dir", required=True); investigate.add_argument("--evidence-dir", required=True)
    investigate.set_defaults(func=command_resolve_pending)
    apply = sub.add_parser("apply-approved")
    apply.add_argument("--registry", required=True); apply.add_argument("--corrections", required=True)
    apply.add_argument("--baseline", required=True); apply.add_argument("--approvals", required=True)
    apply.add_argument("--timestamp", required=True); apply.add_argument("--effective-date", required=True)
    apply.add_argument("--db")
    apply.add_argument("--expected-registry-sha256", required=True)
    apply.add_argument("--expected-event-head", required=True)
    apply.add_argument("--receipt", required=True)
    apply.set_defaults(func=command_apply_approved)
    transition = sub.add_parser("transition-relationship-policy")
    transition.add_argument("--registry", required=True); transition.add_argument("--corrections", required=True)
    transition.add_argument("--baseline", required=True); transition.add_argument("--receipt", required=True)
    transition.add_argument("--timestamp", required=True); transition.add_argument("--effective-date", required=True)
    transition.add_argument("--db")
    transition.add_argument("--expected-registry-sha256", required=True)
    transition.add_argument("--expected-event-head", required=True)
    transition.add_argument("--actor", default="relationship-policy-transition")
    transition.add_argument("--dry-run", action="store_true")
    transition.set_defaults(func=command_transition_relationship_policy)
    evaluate = sub.add_parser("evaluate-pending")
    evaluate.add_argument("--proposals", required=True); evaluate.add_argument("--decisions", required=True)
    evaluate.add_argument("--decision-at", required=True); evaluate.add_argument("--expected-registry-sha256", default="")
    evaluate.add_argument("--expected-event-head", default=""); evaluate.set_defaults(func=command_evaluate_pending)
    evaluate.add_argument("--expected-ledger-head", default="")
    evaluate.add_argument("--expected-cohort-head", default="")
    evaluate.add_argument("--registry")
    evaluate.add_argument("--db")
    evaluate.add_argument("--cohort")
    investigated = sub.add_parser("apply-investigated")
    investigated.add_argument("--registry", required=True); investigated.add_argument("--decisions", required=True)
    investigated.add_argument("--expected-registry-sha256", default="")
    investigated.add_argument("--expected-event-head", default="")
    investigated.add_argument("--expected-ledger-head", default="")
    investigated.add_argument("--expected-cohort-head", default="")
    investigated.add_argument("--max-apply", type=int, default=100)
    investigated.add_argument("--canary", action="store_true")
    investigated.add_argument("--timestamp", required=True)
    investigated.add_argument("--dry-run", action="store_true")
    investigated.add_argument("--db")
    investigated.add_argument("--evidence-dir")
    investigated.add_argument("--ledger")
    investigated.add_argument("--corrections")
    investigated.add_argument("--baseline")
    investigated.add_argument("--receipt")
    investigated.add_argument("--effective-date")
    investigated.add_argument("--journal")
    investigated.add_argument("--generation-descriptor")
    investigated.set_defaults(func=command_apply_investigated)
    recover = sub.add_parser("recover-investigated")
    recover.add_argument("--db", required=True); recover.add_argument("--journal", required=True)
    recover.set_defaults(func=command_recover_investigated)
    return result


def main() -> int:
    args = parser().parse_args()
    try:
        return args.func(args)
    except (OSError, RuntimeError, ValueError, json.JSONDecodeError) as exc:
        print(f"affiliation registry audit: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
