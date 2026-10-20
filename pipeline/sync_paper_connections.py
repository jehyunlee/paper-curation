#!/usr/bin/env python3
"""Make the DB the home of paper-to-paper connections; keep the JSON as output.

Connections were stored as `docs/{topic}/_paper_connections.json`, one copy per
topic the two papers happened to share. Measured before this existed: 136,819
stored connections for 23,098 distinct pairs — 83% duplication — 110 of them
pointing at papers that no longer exist, and no way to ask "what connects to X"
without loading all nine files.

They are embedding-space neighbours (SPECTER2 + title/author BM25, see
`lib/related.py`), not bibliographic fact, so they go in their own table, never
mixed into the publisher-verified ones; every row's `model` is `none:embedding`.
Only `basis == "embedding"` entries are imported — anything left from the
retired LLM relation judges is skipped. The integrity gate checks only what is
checkable: that both endpoints are real papers.

    python pipeline/sync_paper_connections.py --import        # JSON  → DB
    python pipeline/sync_paper_connections.py --export        # DB    → JSON
    python pipeline/sync_paper_connections.py --status
"""
from __future__ import annotations

import argparse
import json
import math
import sqlite3
import sys
import time
from contextlib import nullcontext
from pathlib import Path

from build_bibliography_db import PAPER_CONNECTIONS_SCHEMA
from lib.bibliography_lock import bibliography_writer_lock

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"
DOCS = ROOT / "docs"
CONNECTIONS_NAME = "_paper_connections.json"
SOURCE = "extract_insights/paper_connections"
EMBEDDING_BASIS = "embedding"     # lib.related.EMBEDDING_BASIS
EMBEDDING_MODEL = "none:embedding"


def topic_files() -> list[Path]:
    return sorted(p for p in DOCS.glob(f"*/{CONNECTIONS_NAME}") if p.is_file())


def _connect(db: Path, read_only: bool = False) -> sqlite3.Connection:
    uri = f"file:{db}?mode={'ro' if read_only else 'rw'}"
    conn = sqlite3.connect(uri, uri=True, timeout=60.0)
    conn.execute("PRAGMA busy_timeout = 60000")
    if not read_only:
        conn.execute("PRAGMA foreign_keys = ON")
    return conn


def _unique_object(pairs: list[tuple]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _finite_float(value: str) -> float:
    number = float(value)
    if not math.isfinite(number):
        raise ValueError(f"non-finite JSON number: {value}")
    return number


def _invalid_constant(value: str) -> None:
    raise ValueError(f"invalid JSON constant: {value}")


def _read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"),
                          object_pairs_hook=_unique_object,
                          parse_float=_finite_float,
                          parse_constant=_invalid_constant)
    except (OSError, ValueError) as exc:
        raise ValueError(f"{path}: {exc}") from exc


def _name(value) -> bool:
    return (isinstance(value, str) and bool(value.strip())
            and value == value.strip() and value not in {".", ".."}
            and not any(c in value for c in ("/", "\\", ",", "\x00")))


def _topic_sources() -> dict[str, set[str]]:
    """The canonical index makes missing topics and processed-empty views visible."""
    path = DOCS / "papers" / "_papers_index.json"
    index = _read_json(path)
    if not isinstance(index, list):
        raise ValueError(f"{path}: expected a paper list")
    topics: dict[str, set[str]] = {}
    seen = set()
    for paper in index:
        if not isinstance(paper, dict) or not _name(paper.get("slug")):
            raise ValueError(f"{path}: invalid paper slug/topics")
        slug = paper["slug"]
        if slug in seen:
            raise ValueError(f"{path}: duplicate paper slug: {slug}")
        seen.add(slug)
        memberships = paper.get("topics", [])
        classifications = paper.get("classifications", {})
        primary = paper.get("primary_topic")
        if (not isinstance(memberships, list) or not isinstance(classifications, dict)
                or any(not isinstance(topic, str) for topic in memberships)
                or (primary is not None and not isinstance(primary, str))):
            raise ValueError(f"{path}: invalid paper topic memberships: {slug}")
        memberships = set(memberships) | set(classifications)
        if primary:
            memberships.add(primary)
        for topic in memberships:
            if not _name(topic) or topic in {"papers", "_cross"}:
                raise ValueError(f"{path}: invalid topic: {topic!r}")
            topics.setdefault(topic, set()).add(slug)
    if (DOCS / "_cross" / CONNECTIONS_NAME).exists():
        topics["_cross"] = seen
    return topics


def _validate_reason(entry, path: Path) -> None:
    if not isinstance(entry, dict):
        raise ValueError(f"{path}: connection/reason must be an object")
    for field in ("relation", "reason", "basis", "model"):
        if field in entry and not isinstance(entry[field], str):
            raise ValueError(f"{path}: {field} must be a string")
    if "evidence" in entry and not isinstance(entry["evidence"], dict):
        raise ValueError(f"{path}: evidence must be an object")
    if "evidence" in entry and "cosine" in entry["evidence"]:
        if type(entry["evidence"]["cosine"]) not in (int, float):
            raise ValueError(f"{path}: evidence cosine must be numeric")


def _relation(entry: dict) -> str:
    relation = (entry.get("relation") or "alternative").strip() or "alternative"
    return "alternative" if relation == "related" else relation


def load_json_connections() -> tuple[dict, dict]:
    """Validate the entire input set before collapsing identical topic claims.

    Evidence JSON keeps the item header separate from each reason's evidence.
    Conflicting copies cannot be collapsed losslessly and therefore abort.
    """
    topics = _topic_sources()
    paths = {path.parent.name: path for path in topic_files()}
    missing = set(topics) - paths.keys()
    if missing:
        raise ValueError(f"missing connection inputs for topics: {', '.join(sorted(missing))}")
    if not paths:
        raise ValueError("no topic connection inputs; refusing to replace connections")
    claims: dict[tuple[str, str, str], dict] = {}
    per_topic: dict[str, int] = {}
    for topic, path in sorted(paths.items()):
        payload = _read_json(path)
        if not isinstance(payload, dict):
            raise ValueError(f"{path}: expected a source-to-connections object")
        missing_sources = topics.get(topic, set()) - payload.keys()
        if missing_sources:
            raise ValueError(f"{path}: missing source keys: {', '.join(sorted(missing_sources))}")
        count = 0
        for src, items in payload.items():
            if not _name(src) or not isinstance(items, list):
                raise ValueError(f"{path}: invalid source or connection list: {src!r}")
            for item in items:
                _validate_reason(item, path)
                if not _name(item.get("slug")):
                    raise ValueError(f"{path}: connection target slug is missing/invalid")
                if "reasons" in item and not isinstance(item["reasons"], list):
                    raise ValueError(f"{path}: reasons must be a list")
                entries = item.get("reasons") or [item]
                for entry in entries:
                    _validate_reason(entry, path)
                retained = [(position, entry) for position, entry in enumerate(entries)
                            if entry.get("basis", item.get("basis")) == EMBEDDING_BASIS]
                if not retained:
                    continue
                primary = next((entry for _, entry in retained
                                if _relation(entry) == _relation(item)), retained[0][1])
                header_source = (item if item.get("basis") == EMBEDDING_BASIS
                                 and _relation(item) == _relation(primary) else primary)
                header = {"relation": _relation(header_source),
                          "reason": header_source.get("reason", "")}
                if "evidence" in header_source:
                    header["evidence"] = header_source["evidence"]
                for position, entry in retained:
                    relation = _relation(entry)
                    reason = entry.get("reason", item.get("reason", ""))
                    evidence = {"item": header, "reason": {
                        "evidence": entry["evidence"]} if "evidence" in entry else {},
                        "position": position}
                    key = (src, item["slug"], relation)
                    claim = claims.setdefault(key, {"reason": reason, "evidence": evidence,
                                                     "model": EMBEDDING_MODEL, "topics": set()})
                    if claim["reason"] != reason or claim["evidence"] != evidence:
                        raise ValueError(f"{path}: conflicting copies of connection {key!r}")
                    claim["topics"].add(topic)
                    count += 1
        per_topic[topic] = count
    return claims, per_topic


def import_connections(db: Path, *, dry_run: bool = False) -> dict:
    claims, per_topic = load_json_connections()
    with nullcontext() if dry_run else bibliography_writer_lock(db):
        conn = _connect(db, read_only=dry_run)
        try:
            if not dry_run:
                conn.execute("BEGIN IMMEDIATE")
            ids = dict(conn.execute("SELECT slug, paper_id FROM papers"))
            rows, dangling = [], []
            now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            for (src, dst, relation), claim in claims.items():
                src_id, dst_id = ids.get(src), ids.get(dst)
                if src_id is None or dst_id is None:
                    dangling.append((src, dst, relation))
                    continue
                if src_id == dst_id:
                    continue
                rows.append((src_id, dst_id, relation, claim["reason"],
                             ",".join(sorted(claim["topics"])), claim["model"],
                             json.dumps(claim["evidence"], ensure_ascii=False, allow_nan=False),
                             now, SOURCE))
            columns = {row[1] for row in conn.execute("PRAGMA table_info(paper_connections)")}
            recreate = bool(columns) and "evidence" not in columns
            if not dry_run:
                if recreate:
                    conn.execute("DROP TABLE paper_connections")
                # executescript commits pending transactions, so execute each DDL
                # statement separately to keep table replacement and import atomic.
                for statement in PAPER_CONNECTIONS_SCHEMA.split(";"):
                    if statement.strip():
                        conn.execute(statement)
                conn.execute("DELETE FROM paper_connections")
                conn.executemany(
                    "INSERT INTO paper_connections "
                    "(paper_id,related_paper_id,relation,reason,topics,model,evidence,"
                    "generated_at,source) VALUES (?,?,?,?,?,?,?,?,?)", rows)
                conn.commit()
            return {"json_stored": sum(per_topic.values()),
                    "distinct_claims": len(claims), "imported": len(rows),
                    "dangling_dropped": len(dangling), "per_topic": per_topic,
                    "schema_recreated": recreate, "dry_run": dry_run}
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()


def export_connections(db: Path, *, dry_run: bool = False) -> dict:
    """Rebuild each topic's JSON from the DB.

    `review_to_html.py`, `topic_modeling.py`, `build_topic_index.py` and
    `validate_papers.py` all read those files, so the site keeps its input; the
    DB simply becomes what produces it.
    """
    by_topic = {topic: {src: {} for src in sorted(sources)}
                for topic, sources in _topic_sources().items()}
    for path in topic_files():
        by_topic.setdefault(path.parent.name, {})
    conn = _connect(db, read_only=True)
    try:
        rows = []
        for src, dst, relation, reason, topics, evidence in conn.execute(
                "SELECT ps.slug, pd.slug, c.relation, c.reason, c.topics, c.evidence "
                "FROM paper_connections c "
                "JOIN papers ps ON ps.paper_id=c.paper_id "
                "JOIN papers pd ON pd.paper_id=c.related_paper_id "
                "WHERE c.model = ?", (EMBEDDING_MODEL,)):
            metadata = json.loads(evidence)
            rows.append((src, dst, relation, reason, topics, metadata))
        rows.sort(key=lambda row: (row[0], row[1], row[5]["position"], row[2]))
        for src, dst, relation, reason, topics, metadata in rows:
            for topic in (topics or "").split(","):
                if not topic:
                    continue
                sources = by_topic.setdefault(topic, {})
                entry = sources.setdefault(src, {}).setdefault(
                    dst, {"slug": dst, **metadata["item"], "basis": EMBEDDING_BASIS,
                          "model": "", "reasons": []})
                entry["reasons"].append({"relation": relation,
                                         "reason": reason or "",
                                         "basis": EMBEDDING_BASIS, "model": "",
                                         **metadata["reason"]})
    finally:
        conn.close()

    written = {}
    for topic, sources in sorted(by_topic.items()):
        target = DOCS / topic / CONNECTIONS_NAME
        if not target.parent.is_dir():
            continue
        payload = {src: list(items.values()) for src, items in sources.items()}
        written[topic] = sum(len(v) for v in payload.values())
        if dry_run:
            continue
        tmp = target.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=1),
                       encoding="utf-8")
        tmp.replace(target)
    return {"topics": written, "dry_run": dry_run}


def status(db: Path) -> dict:
    conn = _connect(db, read_only=True)
    try:
        total = conn.execute("SELECT COUNT(*) FROM paper_connections").fetchone()[0]
        relations = dict(conn.execute(
            "SELECT relation, COUNT(*) FROM paper_connections GROUP BY 1"))
        orphan = conn.execute(
            "SELECT COUNT(*) FROM paper_connections c "
            "WHERE NOT EXISTS(SELECT 1 FROM papers p WHERE p.paper_id=c.paper_id)"
            "   OR NOT EXISTS(SELECT 1 FROM papers p "
            "                 WHERE p.paper_id=c.related_paper_id)").fetchone()[0]
        models = dict(conn.execute(
            "SELECT COALESCE(model,'(빈값)'), COUNT(*) FROM paper_connections GROUP BY 1"))
    finally:
        conn.close()
    return {"db_connections": total, "relations": relations,
            "orphan_endpoints": orphan, "models": models,
            "json_files": len(topic_files())}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--import", dest="do_import", action="store_true")
    mode.add_argument("--export", dest="do_export", action="store_true")
    mode.add_argument("--status", action="store_true")
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if not args.db.exists():
        print(f"DB 없음: {args.db}", file=sys.stderr)
        return 2
    if args.do_import:
        result = import_connections(args.db, dry_run=args.dry_run)
    elif args.do_export:
        result = export_connections(args.db, dry_run=args.dry_run)
    else:
        result = status(args.db)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
