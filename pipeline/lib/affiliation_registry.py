"""Deterministic, offline affiliation-registry primitives.

The registry is a canonical JSON snapshot.  It deliberately treats imported group
labels as proposals: relationships enter the accepted graph only with official
evidence.  The public functions below are used by the audit CLI and later DB
projection code.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import unicodedata
import uuid
from datetime import date
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Mapping
import copy

SOURCE_NAMESPACE = uuid.UUID("8d81aeb5-6231-5e97-8a65-cc9e5658bd22")
ZERO_DIGEST = "0" * 64
REGISTRY_SCHEMA_VERSION = "affiliation-2"
POLICY_VERSION = "official-relationships-v1"
SOURCE_SHA256 = "c6077715a3b14b7e0655da519be3bae39d03d9882addaea1899ef24d2ca3f72a"

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


class BibliographyWriterLockBusyError(RuntimeError):
    """Another process owns the bibliography database writer boundary."""

def bibliography_writer_lock_path(database: Path) -> Path:
    """Return the process-wide writer lock shared by builders and migrations."""
    return database.with_suffix(database.suffix + ".affiliation-migrate.lock")


def acquire_bibliography_writer_lock(database: Path) -> int:
    """Acquire exclusive writer ownership for one bibliography database."""
    path = bibliography_writer_lock_path(database)
    try:
        descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise BibliographyWriterLockBusyError(
            "bibliography writer lock busy; remove only after confirming no "
            "builder or migration is running"
        ) from exc
    try:
        os.write(descriptor, f"{os.getpid()}\n".encode())
        os.fsync(descriptor)
    except BaseException:
        os.close(descriptor)
        path.unlink(missing_ok=True)
        raise
    return descriptor


def release_bibliography_writer_lock(database: Path, descriptor: int) -> None:
    """Release a lock acquired by :func:`acquire_bibliography_writer_lock`."""
    try:
        os.close(descriptor)
    finally:
        bibliography_writer_lock_path(database).unlink(missing_ok=True)

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
                  canonical_aliases: Mapping[str, str]) -> dict[str, Any]:
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
        "status": "proposed",
        "identifiers": [{"authority": "source_af_id", "value": key}],
        "aliases": [{"alias_id": _id("alias", source_sha256, key + ":" + alias),
                     "name": alias, "normalized_alias": normalize_name(alias),
                     "country_discriminator": _country(record)} for alias in aliases],
    }
def _group_organization(group: str, country: str, source_sha256: str) -> dict[str, Any]:
    """Create a source-proposed group identity without accepting membership."""
    normalized = normalize_name(group)
    organization_id = _id("group", source_sha256, f"{country}:{normalized}")
    alias_id = _id("group-alias", source_sha256, f"{country}:{normalized}")
    return {
        "organization_id": organization_id,
        "canonical_name_en": group,
        "normalized_name": normalized,
        "country": country,
        "organization_type": "other",
        "status": "proposed",
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
                "provenance": "reviewed_identity",
            })
    return sorted(candidates, key=lambda item: (item["normalized_alias"], item["country_discriminator"],
                                                  item["organization_id"], item["alias_id"]))



def _after(key: str, record: Mapping[str, Any], organization: Mapping[str, Any], issues: list[str]) -> dict[str, Any]:
    """Build a conservative correction: no imported group label becomes an edge."""
    groups = _groups(record)
    after_groups: list[str] = []
    if "group_label_typo_criso" in issues:
        after_groups = ["Commonwealth Scientific and Industrial Research Organisation (CSIRO)"]
    elif "group_label_abbreviation_hkust" in issues:
        after_groups = ["Hong Kong University of Science and Technology"]
    elif "flattened_multi_parent_group" in issues:
        after_groups = ["Spanish National Research Council (CSIC)", "University of Seville"]
    # HEC and generic labels intentionally have no after group: no official edge exists.
    return {"organization_id": organization["organization_id"],
            "canonical_name_en": organization["canonical_name_en"],
            "country": organization["country"],
            "accepted_relationship_ids": [],
            "proposed_group_labels": after_groups,
            "resolution": "standalone_pending_official_evidence"}


def build_registry(source: Mapping[str, Any], *, source_sha256: str = SOURCE_SHA256,
                   timestamp: str = "1970-01-01T00:00:00Z", version: int = 1,
                   canonical_aliases: Mapping[str, str] | None = None) -> dict[str, Any]:
    """Build an offline registry of source proposals and relationship proposals."""
    if not isinstance(source, Mapping):
        raise ValueError("source must be an object keyed by source affiliation ID")
    source_keys = {nfc(str(source_key)) for source_key in source}
    canonical_aliases = canonical_aliases or {}
    organizations: list[dict[str, Any]] = []
    group_organizations: dict[str, dict[str, Any]] = {}
    corrections: list[dict[str, Any]] = []
    evidence: list[dict[str, Any]] = []
    proposals: list[dict[str, Any]] = []
    for raw_key in sorted(source, key=str):
        record = source[raw_key]
        if not isinstance(record, Mapping):
            raise ValueError(f"source record {raw_key!r} is not an object")
        key = nfc(str(raw_key))
        organization = _organization(key, record, source_sha256, canonical_aliases)
        issues = _issue_codes(key, record)
        source_aliases = {alias["normalized_alias"] for alias in organization["aliases"]}
        proposal_ids: list[str] = []
        proposed_groups: list[str] = []
        for group in sorted(set(_groups(record)), key=lambda value: (normalize_name(value), value)):
            if normalize_name(group) in source_aliases or _proposal_is_forbidden(group, issues):
                continue
            group_organization = _group_organization(group, _country(record), source_sha256)
            group_organizations.setdefault(group_organization["organization_id"], group_organization)
            evidence_id = _id("source-evidence", source_sha256, f"{key}:{normalize_name(group)}")
            proposal_id = _id("relationship-proposal", source_sha256, f"{key}:{normalize_name(group)}")
            evidence.append({
                "evidence_id": evidence_id, "authority": "source_untrusted", "status": "proposed",
                "source_key": key, "field": "af_groupname", "quote": group,
                "payload_sha256": canonical_sha256({"source_key": key, "af_groupname": group}),
            })
            proposals.append({
                "relationship_id": proposal_id, "relationship_type": "member_of",
                "subject_organization_id": organization["organization_id"],
                "object_organization_id": group_organization["organization_id"],
                "evidence_ids": [evidence_id], "status": "proposed",
                "requires_official_membership_evidence": True,
            })
            proposal_ids.append(proposal_id)
            proposed_groups.append(group)
        disposition = "corrected" if issues else (
            "pending manual review" if proposal_ids else "standalone no-group"
        )
        correction = {
            "source_sha256": source_sha256, "source_key": key, "source_record": copy.deepcopy(record),
            "organization_ids": [organization["organization_id"]], "relationship_ids": [],
            "relationship_proposal_ids": proposal_ids, "aliases": copy.deepcopy(organization["aliases"]),
            "af_id_replace_tokens": _replacement_tokens(key, record, source_keys),
            "before": {"af_name": copy.deepcopy(record.get("af_name", [])),
                       "af_groupname": copy.deepcopy(record.get("af_groupname", [])),
                       "af_id_replace": copy.deepcopy(record.get("af_id_replace", []))},
            "original_group_labels": _groups(record),
            "proposed_corrected_group_labels": _after(key, record, organization, issues)["proposed_group_labels"],
            "proposed_relationship_group_labels": proposed_groups,
            "after": _after(key, record, organization, issues),
            "disposition": (
                "identity_proposed_relationship_pending"
                if proposal_ids else "identity_proposed"
            ),
            "issue_codes": issues,
            "correction_decisions": [
                {
                    "field": "af_groupname",
                    "action": "replace_proposed_label",
                    "corrected_values": copy.deepcopy(
                        _after(key, record, organization, issues)["proposed_group_labels"]),
                    "acceptance": "pending_official_relationship_evidence",
                }
            ] if issues else [],
            "evidence": {
                "status": "proposed",
                "authority": "source_untrusted",
                "official_identity_evidence_required": True,
                "official_membership_evidence_required": bool(proposal_ids),
                "references": [],
            },
            "confidence": 0.0,
            "reviewers": [],
            "decision_provenance": "untrusted_source_audit",
            "rationale": (
                "This source record was exhaustively audited, but its identity and aliases "
                "remain proposal-only until a distinct reviewed identity event supplies "
                "permitted identity evidence. Group labels remain proposal-only until "
                "official relationship evidence is approved."
            ),
        }
        organizations.append(organization)
        corrections.append(correction)
    events: list[dict[str, Any]] = []
    previous = ZERO_DIGEST
    def append_event(event_type: str, event_key: str, payload: dict[str, Any]) -> None:
        nonlocal previous
        event = {"sequence": len(events) + 1, "event_id": _id("event", source_sha256, event_key),
                 "type": event_type, "timestamp": timestamp, "actor": "offline-import",
                 "policy_version": POLICY_VERSION, "previous_digest": previous,
                 "payload": copy.deepcopy(payload)}
        event["digest"] = _event_digest(event)
        previous = event["digest"]
        events.append(event)
    for organization, correction in sorted(zip(organizations, corrections), key=lambda item: item[1]["source_key"]):
        append_event("source_identity_proposed", correction["source_key"],
                     {"organization": organization, "correction": correction})
        if correction["issue_codes"]:
            append_event("known_correction_decided", f"correction:{correction['source_key']}", {
                "source_key": correction["source_key"],
                "correction": correction,
                "decisions": correction["correction_decisions"],
            })
    for organization in sorted(group_organizations.values(), key=lambda item: item["organization_id"]):
        append_event("group_identity_proposed", organization["organization_id"], {"organization": organization})
    evidence_by_id = {item["evidence_id"]: item for item in evidence}
    for proposal in sorted(proposals, key=lambda item: item["relationship_id"]):
        append_event("relationship_proposed", proposal["relationship_id"], {
            "relationship_proposal": proposal,
            "evidence": [evidence_by_id[evidence_id] for evidence_id in proposal["evidence_ids"]],
        })
    all_organizations = sorted([*organizations, *group_organizations.values()], key=lambda item: item["organization_id"])
    registry = {
        "schema_version": REGISTRY_SCHEMA_VERSION, "registry_version": version,
        "policy_version": POLICY_VERSION, "source_sha256": source_sha256,
        "organizations": all_organizations, "alias_candidates": _identity_candidates(all_organizations),
        "relationships": [], "relationship_proposals": sorted(proposals, key=lambda item: item["relationship_id"]),
        "evidence": sorted(evidence, key=lambda item: item["evidence_id"]),
        "events": events, "event_head": previous,
    }
    validate_registry(registry, require_replay=True)
    return registry


def correction_projection(registry: Mapping[str, Any]) -> list[dict[str, Any]]:
    """Replay current source decisions into one deterministic correction per key."""
    rows: dict[str, dict[str, Any]] = {}
    for event in registry.get("events", []):
        if event.get("type") not in {
                "source_decision_created", "source_decision_superseded",
                "source_identity_proposed", "known_correction_decided"}:
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


def replay_registry(registry: Mapping[str, Any]) -> dict[str, Any]:
    """Replay immutable events and return the projection used for validation."""
    previous = ZERO_DIGEST
    organizations: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    relationship_proposals: list[dict[str, Any]] = []
    evidence: list[dict[str, Any]] = []
    expected_sequence = 1
    for event in registry.get("events", []):
        if event.get("sequence") != expected_sequence:
            raise ValueError("event sequence is not contiguous")
        if event.get("previous_digest") != previous or event.get("digest") != _event_digest(event):
            raise ValueError("event hash chain mismatch")
        previous = event["digest"]
        expected_sequence += 1
        payload = event.get("payload", {})
        if not isinstance(payload, Mapping):
            raise ValueError("event payload must be an object")
        if event.get("type") in {"source_decision_created", "source_identity_proposed",
                                 "group_identity_proposed"}:
            organizations.append(copy.deepcopy(payload["organization"]))
        elif event.get("type") == "relationship_accepted":
            relationships.append(copy.deepcopy(payload["relationship"]))
            evidence.extend(copy.deepcopy(payload["evidence"]))
        elif event.get("type") == "relationship_proposed":
            relationship_proposals.append(copy.deepcopy(payload["relationship_proposal"]))
            evidence.extend(copy.deepcopy(payload["evidence"]))
        elif event.get("type") == "identity_accepted":
            for organization in organizations:
                if organization["organization_id"] == payload["organization_id"]:
                    organization["status"] = "active"
                    organization["identifiers"].append(copy.deepcopy(payload["identifier"]))
                    organization["identifiers"].sort(
                        key=lambda item: (item["authority"], item["value"]))
                    evidence.extend(copy.deepcopy(payload["evidence"]))
                    break
        elif event.get("type") == "identity_alias_accepted":
            for organization in organizations:
                if organization["organization_id"] == payload["organization_id"]:
                    organization["aliases"].append(copy.deepcopy(payload["alias"]))
                    organization["aliases"].sort(key=lambda item: (item["normalized_alias"],
                                                                  item["country_discriminator"], item["alias_id"]))
                    evidence.extend(copy.deepcopy(payload.get("evidence", [])))
                    break
        elif event.get("type") == "known_correction_decided":
            continue
        else:
            raise ValueError("unsupported event type")
    organizations = sorted(organizations, key=lambda item: item["organization_id"])
    return {"organizations": organizations, "alias_candidates": _identity_candidates(organizations),
            "relationships": sorted(relationships, key=lambda item: item["relationship_id"]),
            "relationship_proposals": sorted(relationship_proposals, key=lambda item: item["relationship_id"]),
            "evidence": sorted(evidence, key=lambda item: item["evidence_id"]),
            "event_head": previous}


def validate_registry(registry: Mapping[str, Any], *, require_replay: bool = True,
                      effective_date: str | None = None) -> None:
    """Validate canonical ordering, immutable event replay, and publishable graph evidence."""
    if effective_date is not None and (not isinstance(effective_date, str)
                                       or not DATE_RE.fullmatch(effective_date)):
        raise ValueError("effective date must be an ISO date")
    if registry.get("schema_version") != REGISTRY_SCHEMA_VERSION:
        raise ValueError("unsupported registry schema")
    organizations = registry.get("organizations")
    alias_candidates = registry.get("alias_candidates")
    relationships = registry.get("relationships")
    relationship_proposals = registry.get("relationship_proposals")
    evidence = registry.get("evidence")
    if not all(isinstance(value, list) for value in (organizations, alias_candidates, relationships,
                                                      relationship_proposals, evidence, registry.get("events"))):
        raise ValueError("registry collections must be arrays")
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
    for organization in organizations:
        uuid.UUID(organization["organization_id"])
        if organization["canonical_name_en"] != nfc(organization["canonical_name_en"]):
            raise ValueError("non-NFC canonical name")
        _unique(organization.get("identifiers", []), ("authority", "value"), "identifier within organization")
        _unique(organization.get("aliases", []), ("alias_id",), "alias ID")
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
    _validate_relationship_graph(relationships, organizations, evidence_by_id)
    if require_replay:
        replayed = replay_registry(registry)
        if (replayed["organizations"] != organizations
                or replayed["alias_candidates"] != alias_candidates
                or replayed["relationships"] != relationships
                or replayed["relationship_proposals"] != relationship_proposals
                or replayed["evidence"] != evidence
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
                                 evidence_by_id: Mapping[str, Mapping[str, Any]]) -> None:
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


def relationship_lookup(registry: Mapping[str, Any], organization_id: str,
                        relationship_type: str | None = None) -> list[dict[str, Any]]:
    """Return accepted outgoing relationships, optionally filtered by type."""
    return [edge for edge in registry["relationships"]
            if edge["subject_organization_id"] == organization_id
            and (relationship_type is None or edge.get("relationship_type") == relationship_type)]
def is_generic_fragment(name: str) -> bool:
    """Whether a name is too generic to resolve or promote without context."""
    return bool(GENERIC_FRAGMENT_RE.match(nfc(name).strip()))


def ror_exact_candidates(payload: Mapping[str, Any], name: str, country: str) -> list[dict[str, Any]]:
    """Extract only exact, country-consistent candidates from ROR v1/v2 responses."""
    target = normalize_name(name)
    expected_country = normalize_name(country)
    candidates = []
    for item in payload.get("items", []):
        if not isinstance(item, Mapping):
            continue
        names = [item.get("name", ""), *item.get("aliases", [])]
        display_name = item.get("name", "")
        for entry in item.get("names", []):
            if not isinstance(entry, Mapping) or not isinstance(entry.get("value"), str):
                continue
            names.append(entry["value"])
            if "ror_display" in entry.get("types", []):
                display_name = entry["value"]
        if target not in {normalize_name(value) for value in names if isinstance(value, str)}:
            continue

        country_names: set[str] = set()
        candidate_country = item.get("country", {})
        if isinstance(candidate_country, Mapping):
            for key in ("country_name", "country_code"):
                if candidate_country.get(key):
                    country_names.add(str(candidate_country[key]))
        elif candidate_country:
            country_names.add(str(candidate_country))
        for location in item.get("locations", []):
            if not isinstance(location, Mapping):
                continue
            details = location.get("geonames_details", {})
            if isinstance(details, Mapping):
                for key in ("country_name", "country_code"):
                    if details.get(key):
                        country_names.add(str(details[key]))
        if expected_country and expected_country not in {
            normalize_name(value) for value in country_names
        }:
            continue

        identifier = item.get("id") or item.get("ror") or ""
        links = []
        for link in item.get("links", []):
            if isinstance(link, str):
                links.append(link)
            elif isinstance(link, Mapping) and isinstance(link.get("value"), str):
                links.append(link["value"])
        if isinstance(identifier, str) and identifier:
            candidates.append({
                "external_id": identifier,
                "name": display_name,
                "country": sorted(country_names)[0] if country_names else "",
                "links": sorted(set(links)),
                "score": 1.0,
                "reason": "exact_name_or_alias_country_consistent_ror",
            })
    return sorted(candidates, key=lambda candidate: (
        candidate["external_id"], candidate["name"]
    ))
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
                 "payload": copy.deepcopy(payload)}
        event["digest"] = _event_digest(event)
        previous = event["digest"]
        result["events"].append(event)
    result["event_head"] = previous
    result["alias_candidates"] = _identity_candidates(result["organizations"])
    validate_registry(result, effective_date=timestamp[:10])
    return result


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
