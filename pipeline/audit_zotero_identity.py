#!/usr/bin/env python3
"""Audit — and optionally repair — papers holding another work's bibliography.

    python pipeline/audit_zotero_identity.py                 # report
    python pipeline/audit_zotero_identity.py --slugs-out f   # write repair list
    python pipeline/audit_zotero_identity.py --repair        # re-ingest them

`--repair` re-runs `build_bibliography_db.py --slugs <affected>`, which is what
actually rewrites the rows: with a validating `clean_doi` the placeholder no
longer matches a Zotero item, so each paper falls back to its own review
frontmatter instead of inheriting a stranger's record.

Read-only without `--repair`. Exits 2 under `--strict` when anything is found.
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "pipeline"
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

from lib import zotero_identity  # noqa: E402

PAPERS_DIR = ROOT / "docs" / "papers"
DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"


def run_audit(db: Path, papers_dir: Path) -> dict:
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    try:
        return zotero_identity.audit(conn, papers_dir)
    finally:
        conn.close()


def repair(report: dict, db: Path) -> dict:
    slugs = report["affected_slugs"]
    if not slugs:
        return {"repaired": 0, "note": "nothing to repair"}
    command = [sys.executable, str(PIPELINE / "build_bibliography_db.py"),
               "--slugs", ",".join(slugs), "--output", str(db), "--no-email"]
    result = subprocess.run(command, cwd=ROOT)
    return {"repaired": len(slugs), "exit": result.returncode}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--papers-dir", type=Path, default=PAPERS_DIR)
    ap.add_argument("--slugs-out", type=Path,
                    help="write the affected slugs as one comma-separated line")
    ap.add_argument("--repair", action="store_true",
                    help="re-ingest the affected papers")
    ap.add_argument("--strict", action="store_true",
                    help="exit 2 when any paper is affected")
    args = ap.parse_args()

    if not args.db.exists():
        print(f"missing database: {args.db}", file=sys.stderr)
        return 2

    report = run_audit(args.db, args.papers_dir)
    if args.slugs_out:
        args.slugs_out.parent.mkdir(parents=True, exist_ok=True)
        args.slugs_out.write_text(",".join(report["affected_slugs"]),
                                  encoding="utf-8")
        report["slugs_out"] = str(args.slugs_out)
    if args.repair:
        report["repair"] = repair(report, args.db)
        report["after"] = {
            key: value for key, value in
            run_audit(args.db, args.papers_dir).items()
            if not key.endswith(("_detail", "_slugs", "_values"))
        }
    printable = {key: value for key, value in report.items()
                 if key != "affected_slugs"}
    print(json.dumps(printable, ensure_ascii=False, indent=2))
    return 2 if (args.strict and report["affected_papers"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
