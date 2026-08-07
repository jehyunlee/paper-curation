#!/usr/bin/env python3
"""Search and sort the collection-independent bibliography database.

Examples:
  python pipeline/query_bibliography.py --institution "Cambridge" --sort date
  python pipeline/query_bibliography.py --country "United Kingdom" --json
  python pipeline/query_bibliography.py --author "Yuan" --limit 20
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARED_DB = (Path.home() / "Library" / "CloudStorage" /
             "GoogleDrive-jehyun.lee@gmail.com" / "내 드라이브" /
             "paper-curation" / "bibliography.sqlite3")
DEFAULT_DB = Path(os.environ.get(
    "PAPER_CURATION_BIBLIO_DB", str(ROOT / ".cache" / "bibliography.sqlite3")
))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--institution")
    ap.add_argument("--country")
    ap.add_argument("--author")
    ap.add_argument("--journal")
    ap.add_argument("--year")
    ap.add_argument("--sort", choices=("date", "title", "institution", "author"), default="date")
    ap.add_argument("--desc", action="store_true")
    ap.add_argument("--limit", type=int, default=100)
    ap.add_argument("--json", action="store_true", dest="as_json")
    args = ap.parse_args()
    if not args.db.exists():
        ap.error(f"database not found: {args.db}")
    where, params = [], []
    if args.institution:
        where.append("i.institution_name LIKE ?"); params.append(f"%{args.institution}%")
    if args.country:
        where.append("pi.country_name LIKE ?"); params.append(f"%{args.country}%")
    if args.author:
        where.append("a.display_name LIKE ?"); params.append(f"%{args.author}%")
    if args.journal:
        where.append("p.journal_name LIKE ?"); params.append(f"%{args.journal}%")
    if args.year:
        where.append("p.publication_date LIKE ?"); params.append(f"{args.year}%")
    order = {"date": "p.publication_date", "title": "p.title", "institution": "i.institution_name", "author": "a.display_name"}[args.sort]
    direction = "DESC" if args.desc else "ASC"
    sql = f"""SELECT DISTINCT p.title, p.publication_date, p.journal_name,
        p.volume, p.issue, p.pages, p.publisher, p.issn, p.eissn,
        p.document_type, p.doi, p.url, p.scopus_eid, p.received_date,
        p.accepted_date, p.published_online_date, p.bibliography_source,
        p.review_dir, p.zotero_item_key, i.institution_name,
        pi.country_name, a.display_name AS first_author
        FROM papers p
        LEFT JOIN paper_institutions pi ON pi.paper_id=p.paper_id
        LEFT JOIN institutions i ON i.institution_id=pi.institution_id
        LEFT JOIN paper_authors pa ON pa.paper_id=p.paper_id AND pa.is_first_author=1
        LEFT JOIN authors a ON a.author_id=pa.author_id
        {('WHERE ' + ' AND '.join(where)) if where else ''}
        ORDER BY {order} {direction}, p.title ASC LIMIT ?"""
    params.append(max(1, args.limit))
    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    rows = [dict(row) for row in conn.execute(sql, params)]
    conn.close()
    if args.as_json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
    else:
        for n, row in enumerate(rows, 1):
            org = row["institution_name"] or "-"
            country = row["country_name"] or "-"
            print(f"{n:3}. {row['title']} | {row['publication_date'] or '-'} | {org} ({country}) | {row['review_dir']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
