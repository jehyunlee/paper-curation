#!/usr/bin/env python3
"""What the bibliography DB needs per paper, and which papers do not supply it.

    python pipeline/audit_ingest_inputs.py
    python pipeline/audit_ingest_inputs.py --missing text --limit 20
    python pipeline/audit_ingest_inputs.py --strict

Review generation feeds the DB through four files in `docs/papers/<slug>/`:

  review.md          frontmatter — title, authors, DOI, arXiv, date
  text.md            the PDF's full text: the only source of affiliations,
                     and the `source_documents` row `--changed-only` reads
  bibliography.json  the Zotero record captured at review time; without it a
                     build has to page the whole library (~200 s, and its
                     failure mode is silent `zotero_item_key` loss)
  figures/           not used by the DB

A generator that writes only review.md produces a paper the DB can register
but never populate. Measured here: the 49 papers papercurio wrote — their
Zotero items carry a `papercurio:` marker in `extra` — have no text.md, and
against the papers that do have one they hold author-institution links for
16% instead of 85%, carry unconfirmed Scopus affiliations 52% of the time
instead of 9%, and have no affiliation at all 30% of the time instead of 15%.
`--changed-only` is blind to them too: with no `source_documents` row of type
`text`, nothing but review.md can mark them changed.

Read-only.
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS_DIR = ROOT / "docs" / "papers"
INDEX = PAPERS_DIR / "_papers_index.json"
DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"

INPUTS = ("review", "text", "sidecar")


def paper_inputs(slug: str) -> dict:
    directory = PAPERS_DIR / slug
    return {
        "review": (directory / "review.md").exists(),
        "text": (directory / "text.md").exists(),
        "sidecar": (directory / "bibliography.json").exists(),
    }


def db_state(conn: sqlite3.Connection) -> dict:
    rows = {}
    for slug, doi, key in conn.execute(
            "SELECT slug, doi, zotero_item_key FROM papers"):
        rows[slug] = {"in_db": True, "doi": doi or "",
                      "zotero_item_key": key or "",
                      "institutions": 0, "authors": 0, "source_docs": []}
    for slug, count in conn.execute(
            "SELECT p.slug, COUNT(*) FROM paper_institutions pi"
            " JOIN papers p USING(paper_id) GROUP BY p.slug"):
        if slug in rows:
            rows[slug]["institutions"] = count
    for slug, count in conn.execute(
            "SELECT p.slug, COUNT(*) FROM paper_authors pa"
            " JOIN papers p USING(paper_id) GROUP BY p.slug"):
        if slug in rows:
            rows[slug]["authors"] = count
    for slug, kind in conn.execute(
            "SELECT p.slug, sd.document_type FROM source_documents sd"
            " JOIN papers p USING(paper_id)"):
        if slug in rows:
            rows[slug]["source_docs"].append(kind)
    return rows


def audit(db: Path) -> dict:
    entries = json.loads(INDEX.read_text(encoding="utf-8"))
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    try:
        db_rows = db_state(conn)
    finally:
        conn.close()

    papers = []
    for entry in entries:
        slug = entry.get("slug", "")
        if not slug:
            continue
        present = paper_inputs(slug)
        state = db_rows.get(slug, {"in_db": False, "institutions": 0,
                                   "authors": 0, "source_docs": [],
                                   "zotero_item_key": "", "doi": ""})
        papers.append({"slug": slug, **present, **state,
                       "missing": [name for name in INPUTS if not present[name]]})

    def count(predicate) -> int:
        return sum(1 for paper in papers if predicate(paper))

    return {
        "papers": len(papers),
        "in_db": count(lambda p: p["in_db"]),
        "missing_review_md": count(lambda p: not p["review"]),
        "missing_text_md": count(lambda p: not p["text"]),
        "missing_sidecar": count(lambda p: not p["sidecar"]),
        "complete_inputs": count(lambda p: not p["missing"]),
        # What the gap costs, measured rather than asserted.
        "no_institutions": count(lambda p: p["in_db"] and not p["institutions"]),
        "no_institutions_and_no_text": count(
            lambda p: p["in_db"] and not p["institutions"] and not p["text"]),
        "no_text_source_document": count(
            lambda p: p["in_db"] and "text" not in p["source_docs"]),
        "no_zotero_key": count(lambda p: p["in_db"] and not p["zotero_item_key"]),
        "_papers": papers,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--missing", choices=INPUTS,
                    help="list papers missing this input")
    ap.add_argument("--limit", type=int, default=15)
    ap.add_argument("--strict", action="store_true",
                    help="exit 2 when any paper is missing an input")
    args = ap.parse_args()

    report = audit(args.db)
    papers = report.pop("_papers")
    print(json.dumps(report, ensure_ascii=False, indent=2))

    if args.missing:
        listed = [p for p in papers if args.missing in p["missing"]]
        print(f"\n{len(listed)} papers without {args.missing}:")
        for paper in listed[:args.limit]:
            print(f"  {paper['slug'][:56]:56s} "
                  f"inst={paper['institutions']:<3} "
                  f"auth={paper['authors']:<3} "
                  f"zotero={paper['zotero_item_key'] or '-'}")
        if len(listed) > args.limit:
            print(f"  … +{len(listed) - args.limit} more")

    incomplete = report["papers"] - report["complete_inputs"]
    return 2 if (args.strict and incomplete) else 0


if __name__ == "__main__":
    raise SystemExit(main())
