#!/usr/bin/env python3
"""Create and audit the deterministic offline affiliation registry.

Import is the only command that writes accepted registry artifacts.  Network
resolution is proposal-only and never edits the accepted registry.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import ssl
import sqlite3
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlencode
from typing import Any

from lib.affiliation_registry import (
    SOURCE_SHA256,
    baseline_projection,
    build_registry,
    canonical_json_bytes,
    canonical_sha256,
    correction_projection,
    is_generic_fragment,
    load_registry,
    normalize_name,
    promote_approved,
    ror_exact_candidates,
    validate_registry,
)


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
    sys.stdout.write(canonical_json_bytes(summary).decode("utf-8"))
    return 0


def _request_json(url: str, context: ssl.SSLContext) -> tuple[dict[str, Any], bytes]:
    request = urllib.request.Request(url, headers={"User-Agent": "affiliation-registry-audit/1"})
    with urllib.request.urlopen(request, timeout=20, context=context) as response:
        raw = response.read(5 * 1024 * 1024 + 1)
    if len(raw) > 5 * 1024 * 1024:
        raise ValueError("provider response exceeds 5 MiB")
    return json.loads(raw.decode("utf-8")), raw


def _attempt(base: dict[str, Any], **values: Any) -> dict[str, Any]:
    """Return a complete, canonical attempt row with deterministic fields."""
    return {
        **base, "provider": "", "url": "", "status": "pending",
        "candidate_external_id": "", "candidate_name": "", "candidate_country": "",
        "score": 0.0, "reason": "", "payload_sha256": "", "quote_sha256": "",
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
            payload, raw = _request_json(url, context)
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
    if status in {"proposal", "discovered"}:
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
    if args.db:
        db_targets, pending_ids = _load_pending_targets(args.db)
        targets.update(db_targets)
    context, attempts = ssl.create_default_context(), []
    state = {"requests": 0, "failures": 0}
    incomplete = False
    ordered_targets = sorted((nfc_name, nfc_country) for nfc_name, nfc_country in targets
                             if isinstance(nfc_name, str) and isinstance(nfc_country, str))
    for target_index, (name, country) in enumerate(ordered_targets):
        base = {"query": name, "country": country, "retrieved_at": args.retrieved_at,
                "target_index": target_index}
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
        url = "https://api.ror.org/organizations?" + urlencode({"query": name})
        candidates: list[dict[str, Any]] = []
        try:
            payload, raw, retry_number = _request_with_budget(url, context, args, state)
            candidates = ror_exact_candidates(payload, name, country)
            if not candidates:
                attempts.append(_attempt(base, provider="ror", url=url, status="pending",
                    reason="no_exact_country_consistent_match", payload_sha256=hashlib.sha256(raw).hexdigest(),
                    attempt_number=state["requests"], retry_number=retry_number))
            for candidate in candidates:
                attempts.append(_attempt(base, provider="ror", url=url, status="proposal",
                    candidate_external_id=candidate["external_id"], candidate_name=candidate["name"],
                    candidate_country=candidate["country"], score=candidate["score"],
                    reason=candidate["reason"], payload_sha256=hashlib.sha256(raw).hexdigest(),
                    quote_sha256=canonical_sha256(candidate), attempt_number=state["requests"],
                    retry_number=retry_number))
                for official_url in candidate["links"]:
                    if official_url.startswith("https://"):
                        attempts.append(_attempt(base, provider="official", url=official_url,
                            status="discovered", candidate_external_id=candidate["external_id"],
                            candidate_name=candidate["name"], candidate_country=candidate["country"],
                            score=candidate["score"], reason="ror_official_url_discovery"))
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
    if args.db and attempts:
        _persist_pending_attempts(args.db, attempts, pending_ids)
    _append_fsync(Path(args.proposals), _jsonl_bytes(attempts))
    return 6 if incomplete else 0


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


def command_apply_approved(args: argparse.Namespace) -> int:
    registry_path = Path(args.registry)
    lock_path = registry_path.with_suffix(registry_path.suffix + ".lock")
    journal_path = registry_path.with_suffix(registry_path.suffix + ".apply-approved.journal")
    try:
        lock_fd = os.open(lock_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError as exc:
        raise ValueError(f"registry lock exists: {lock_path}") from exc
    try:
        os.write(lock_fd, b"apply-approved\n")
        os.fsync(lock_fd)
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
        os.close(lock_fd)
        lock_path.unlink(missing_ok=True)
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
    report = sub.add_parser("report"); report.add_argument("--registry", required=True); report.set_defaults(func=command_report)
    resolve = sub.add_parser("resolve-pending")
    resolve.add_argument("--db"); resolve.add_argument("--registry", required=True); resolve.add_argument("--proposals", required=True)
    resolve.add_argument("--allow-network", action="store_true"); resolve.add_argument("--name", action="append", default=[])
    resolve.add_argument("--country", default=""); resolve.add_argument("--retrieved-at", required=True)
    resolve.add_argument("--request-budget", type=int, default=100)
    resolve.add_argument("--max-retries", type=int, default=1)
    resolve.add_argument("--retry-backoff-seconds", type=float, default=0.0)
    resolve.add_argument("--circuit-breaker-failures", type=int, default=5)
    resolve.set_defaults(func=command_resolve_pending)
    apply = sub.add_parser("apply-approved")
    apply.add_argument("--registry", required=True); apply.add_argument("--corrections", required=True)
    apply.add_argument("--baseline", required=True); apply.add_argument("--approvals", required=True)
    apply.add_argument("--timestamp", required=True); apply.add_argument("--effective-date", required=True)
    apply.add_argument("--expected-registry-sha256", required=True)
    apply.add_argument("--expected-event-head", required=True)
    apply.add_argument("--receipt", required=True)
    apply.set_defaults(func=command_apply_approved)
    return result


def main() -> int:
    args = parser().parse_args()
    try:
        return args.func(args)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"affiliation registry audit: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
