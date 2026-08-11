#!/usr/bin/env python3
"""Make the DB the home of paper-to-paper connections; keep the JSON as output.

Connections were stored as `docs/{topic}/_paper_connections.json`, one copy per
topic the two papers happened to share. Measured before this existed: 136,819
stored connections for 23,098 distinct pairs — 83% duplication — 110 of them
pointing at papers that no longer exist, and no way to ask "what connects to X"
without loading all nine files.

They are LLM claims, not bibliographic fact, so they go in their own table with
the asserting model recorded per row, never mixed into the publisher-verified
ones. The integrity gate checks only what is checkable: that both endpoints are
real papers. The content of a claim is not verifiable here and this does not
pretend otherwise.

    python pipeline/sync_paper_connections.py --import        # JSON  → DB
    python pipeline/sync_paper_connections.py --export        # DB    → JSON
    python pipeline/sync_paper_connections.py --status
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import time
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"
DOCS = ROOT / "docs"
CONNECTIONS_NAME = "_paper_connections.json"
MODEL = "claude-sonnet-5"          # extract_insights.py's paper-connection model
SOURCE = "extract_insights/paper_connections"


def topic_files() -> list[Path]:
    return sorted(p for p in DOCS.glob(f"*/{CONNECTIONS_NAME}") if p.is_file())


def _connect(db: Path, read_only: bool = False) -> sqlite3.Connection:
    uri = f"file:{db}?mode=ro" if read_only else f"file:{db}"
    conn = sqlite3.connect(uri, uri=True, timeout=60.0)
    conn.execute("PRAGMA busy_timeout = 60000")
    if not read_only:
        conn.execute("PRAGMA foreign_keys = ON")
    return conn


def load_json_connections() -> tuple[dict, dict]:
    """Collapse every topic file into one pair→claim map.

    Key is (source slug, target slug, relation): the same pair asserted with two
    different relations is two claims, but the same claim repeated across topics
    is one row whose `topics` lists where it was asserted.
    """
    claims: dict[tuple[str, str, str], dict] = {}
    per_topic: dict[str, int] = {}
    for path in topic_files():
        topic = path.parent.name
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            print(f"  [warn] {path}: {exc}", file=sys.stderr)
            continue
        count = 0
        for src, items in (payload or {}).items():
            for item in items or []:
                dst = item.get("slug")
                if not dst:
                    continue
                for entry in (item.get("reasons")
                              or [{"relation": item.get("relation"),
                                   "reason": item.get("reason")}]):
                    relation = (entry.get("relation") or "related").strip()
                    key = (src, dst, relation)
                    claim = claims.setdefault(
                        key, {"reason": (entry.get("reason") or "").strip(),
                              "topics": set()})
                    claim["topics"].add(topic)
                    if not claim["reason"] and entry.get("reason"):
                        claim["reason"] = entry["reason"].strip()
                    count += 1
        per_topic[topic] = count
    return claims, per_topic


def import_connections(db: Path, *, dry_run: bool = False) -> dict:
    conn = _connect(db, read_only=dry_run)
    try:
        ids = {slug: pid for slug, pid in
               conn.execute("SELECT slug, paper_id FROM papers")}
        claims, per_topic = load_json_connections()
        rows, dangling = [], []
        now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        for (src, dst, relation), claim in claims.items():
            src_id, dst_id = ids.get(src), ids.get(dst)
            if src_id is None or dst_id is None:
                dangling.append((src, dst, relation))
                continue
            if src_id == dst_id:            # a paper is not related to itself
                continue
            rows.append((src_id, dst_id, relation, claim["reason"],
                         ",".join(sorted(claim["topics"])), MODEL, now, SOURCE))
        if not dry_run:
            conn.execute("DELETE FROM paper_connections")
            conn.executemany(
                "INSERT OR REPLACE INTO paper_connections "
                "(paper_id,related_paper_id,relation,reason,topics,model,"
                "generated_at,source) VALUES (?,?,?,?,?,?,?,?)", rows)
            conn.commit()
        return {"json_stored": sum(per_topic.values()),
                "distinct_claims": len(claims),
                "imported": len(rows),
                "dangling_dropped": len(dangling),
                "per_topic": per_topic,
                "dry_run": dry_run}
    finally:
        conn.close()


def export_connections(db: Path, *, dry_run: bool = False) -> dict:
    """Rebuild each topic's JSON from the DB.

    `review_to_html.py`, `topic_modeling.py`, `build_topic_index.py` and
    `validate_papers.py` all read those files, so the site keeps its input; the
    DB simply becomes what produces it.
    """
    conn = _connect(db, read_only=True)
    try:
        by_topic: dict[str, dict[str, dict]] = defaultdict(
            lambda: defaultdict(dict))
        for src, dst, relation, reason, topics in conn.execute(
                "SELECT ps.slug, pd.slug, c.relation, c.reason, c.topics "
                "FROM paper_connections c "
                "JOIN papers ps ON ps.paper_id=c.paper_id "
                "JOIN papers pd ON pd.paper_id=c.related_paper_id"):
            for topic in (topics or "").split(","):
                if not topic:
                    continue
                entry = by_topic[topic][src].setdefault(
                    dst, {"slug": dst, "relation": relation,
                          "reason": reason or "", "reasons": []})
                entry["reasons"].append({"relation": relation,
                                         "reason": reason or ""})
    finally:
        conn.close()

    written = {}
    for topic, sources in by_topic.items():
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
