#!/usr/bin/env python3
"""Validate bibliography DB completeness and source alignment."""
from __future__ import annotations

import argparse
import json
import sqlite3
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "docs" / "papers"
INDEX = PAPERS / "_papers_index.json"
DB = Path(os.environ.get(
    "PAPER_CURATION_BIBLIO_DB", str(ROOT / ".cache" / "bibliography.sqlite3")
))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DB)
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()
    report = {"ok": True, "issues": []}
    if not args.db.exists():
        report["ok"] = False; report["issues"].append(f"missing database: {args.db}")
    else:
        conn = sqlite3.connect(args.db)
        count = conn.execute("SELECT COUNT(*) FROM papers").fetchone()[0]
        empty_titles = conn.execute("SELECT COUNT(*) FROM papers WHERE title='' OR title IS NULL").fetchone()[0]
        bad_dirs = conn.execute("SELECT COUNT(*) FROM papers WHERE review_dir='' OR review_dir IS NULL").fetchone()[0]
        aliases = conn.execute("SELECT COUNT(*) FROM institution_aliases").fetchone()[0]
        countries = conn.execute("SELECT COUNT(*) FROM paper_institutions WHERE country_name<>''").fetchone()[0]
        tables = {
            row[0] for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        }
        snapshots = conn.execute(
            "SELECT COUNT(*) FROM citation_snapshots").fetchone()[0] \
            if "citation_snapshots" in tables else 0
        yearly = conn.execute(
            "SELECT COUNT(*) FROM citation_yearly").fetchone()[0] \
            if "citation_yearly" in tables else 0
        report.update({
            "db_papers": count,
            "empty_titles": empty_titles,
            "empty_review_dirs": bad_dirs,
            "institution_aliases": aliases,
            "country_links": countries,
            "citation_snapshots": snapshots,
            "citation_yearly_rows": yearly,
        })
        if empty_titles: report["issues"].append(f"empty titles: {empty_titles}")
        if bad_dirs: report["issues"].append(f"empty review directories: {bad_dirs}")
        conn.close()
    try:
        source_count = len(json.loads(INDEX.read_text(encoding="utf-8")))
        report["source_index_papers"] = source_count
        if report.get("db_papers") != source_count:
            report["issues"].append(f"paper count mismatch: DB={report.get('db_papers')} index={source_count}")
    except Exception as exc:
        report["issues"].append(f"index read failed: {exc}")
    report["ok"] = not report["issues"]
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok"] or not args.strict else 1


if __name__ == "__main__":
    raise SystemExit(main())
