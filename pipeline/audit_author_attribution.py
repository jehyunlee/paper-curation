#!/usr/bin/env python3
"""Why a paper still has no evidenced author-to-institution mapping.

    python pipeline/audit_author_attribution.py
    python pipeline/audit_author_attribution.py --stage E --limit 10
    python pipeline/audit_author_attribution.py --json

Attributing an author to one of a paper's institutions needs the byline to say
so. When it cannot be read, the builder links every author to every
institution and tags the rows `pdf.unmarked-multi`; ranking a university's
researchers over those returns people who were never there, so
`report_field_leaders.py` refuses them.

This reports what is actually blocking each remaining paper, because the
answer keeps moving: it was a marker parser too narrow to see spaced and
symbol markers, then an affiliation block outside the window, then a
60-character prefix comparison standing in for name matching. Each stage names
the next piece of work instead of leaving "the rest" as one number.

Stages, in the order the pipeline tries them:

  A  no text.md — nothing was extracted from a PDF
  B  the record lists fewer than two authors
  C  the PDF byline names nobody the record calls an author
  D  no byline markers, no inline affiliations, no author-information block
  E  markers read, but the block they point at was not found
  F  block found, but its text matched no institution row
  G  everything resolves now — the stored rows are simply stale

Read-only.
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "pipeline"
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import build_bibliography_db as bib            # noqa: E402
from lib import zotero_identity as zi          # noqa: E402

PAPERS_DIR = ROOT / "docs" / "papers"
DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"

RESOLVED_SOURCES = ("openalex", "scopus", "pdf.byline-marker",
                    "pdf.inline-affiliation",
                    "pdf.author-information", "pdf.stacked-byline",
                    "pdf.sole-affiliation")

STAGES = {
    "A": "text.md 없음",
    "B": "레코드 저자 2명 미만",
    "C": "PDF 바이라인이 레코드 저자와 무관",
    "D": "PDF 가 저자별 소속을 말하지 않음",
    "E": "마커는 읽혔으나 소속 블록 못 찾음",
    "F": "블록은 찾았으나 기관 행과 대조 실패",
    "G": "지금 규칙으로는 해결됨 (저장된 행이 낡음)",
}


def unresolved(conn: sqlite3.Connection) -> list[tuple]:
    marks = ",".join("?" * len(RESOLVED_SOURCES))
    return conn.execute(
        f"SELECT DISTINCT p.paper_id, p.slug, p.title FROM papers p"
        f" JOIN paper_author_institutions pai USING(paper_id)"
        f" WHERE pai.source='pdf.unmarked-multi' AND p.paper_id NOT IN"
        f" (SELECT paper_id FROM paper_author_institutions"
        f"  WHERE source IN ({marks})) ORDER BY p.paper_id",
        RESOLVED_SOURCES).fetchall()


def classify(conn: sqlite3.Connection, paper_id: int, slug: str,
             known_surnames: set[str]) -> tuple[str, dict]:
    text = PAPERS_DIR / slug / "text.md"
    if not text.exists():
        return "A", {}
    authors = [row[0] for row in conn.execute(
        "SELECT a.display_name FROM paper_authors pa JOIN authors a"
        " USING(author_id) WHERE pa.paper_id=? ORDER BY pa.author_order",
        (paper_id,))]
    if len(authors) < 2:
        return "B", {"authors": authors}

    header = bib.extract_header(text)[0]
    folded = bib._fold(header)
    # One shared surname is a coincidence — "Wang" and "Li" appear in most
    # bylines in this corpus. "34 examples of llm applications" records Lei
    # Wang while its PDF reads Yoel Zimmermann, and landed in D on that one
    # accidental hit instead of being reported as the mismatch it is.
    own = sum(1 for name in authors
              if (parts := name.split()) and bib._fold(parts[-1]) in folded)
    if own < 2:
        names = zi._pdf_byline_names(header, known_surnames)
        if len(names) >= 2:
            return "C", {"record": authors[:3], "pdf": names[:3]}

    markers, alphabet = bib.read_byline_markers(header, authors, text)
    inline = bib.inline_author_affiliations(header, authors)
    named = bib.author_information_pairs(
        bib.author_information_text(text), authors)
    if not (markers or inline or named):
        return "D", {"authors": authors[:3]}

    institutions = conn.execute(
        "SELECT institution_id, raw_name FROM paper_institutions"
        " WHERE paper_id=?", (paper_id,)).fetchall()
    if markers:
        wanted = {m for values in markers.values() for m in values}
        block = (bib.marker_affiliations(header, wanted, alphabet)
                 or bib.marker_affiliations(
                     bib.affiliation_window(text), wanted, alphabet)
                 or bib.marker_affiliations(
                     bib.author_information_text(text), wanted, alphabet))
        if not block:
            return "E", {"markers": sorted(wanted)[:6]}
        if any(bib.best_institution_for(label, institutions)
               for label in block.values()):
            return "G", {}
        return "F", {"block": list(block.items())[:2],
                     "rows": [(raw or "")[:48] for _, raw in institutions][:3]}
    if any(bib.best_institution_for(value, institutions)
           for value in {**inline, **named}.values()):
        return "G", {}
    return "F", {"rows": [(raw or "")[:48] for _, raw in institutions][:3]}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--stage", choices=sorted(STAGES),
                    help="list the papers in one stage")
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True)
    try:
        known = {zi._norm(name.split()[-1]) for (name,) in conn.execute(
            "SELECT display_name FROM authors") if name.split()}
        rows = unresolved(conn)
        counts, listed = Counter(), []
        for paper_id, slug, title in rows:
            stage, detail = classify(conn, paper_id, slug, known)
            counts[stage] += 1
            if args.stage == stage and len(listed) < args.limit:
                listed.append({"slug": slug, "title": title, **detail})
        total = conn.execute("SELECT COUNT(*) FROM papers").fetchone()[0]
    finally:
        conn.close()

    report = {"papers": total, "unresolved": len(rows),
              "stages": {stage: counts[stage] for stage in sorted(STAGES)}}
    if args.json:
        report["listed"] = listed
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0

    print(f"코퍼스 {total:,}편 · 근거 없는 논문 {len(rows):,}편 "
          f"({len(rows) / total * 100:.1f}%)\n")
    for stage in sorted(STAGES):
        count = counts[stage]
        if not count:
            continue
        share = count / len(rows) * 100 if rows else 0
        print(f"  {stage}  {STAGES[stage]:32s} {count:4d} ({share:4.1f}%)")
    for item in listed:
        print(f"\n── {item['slug'][:60]}")
        for key, value in item.items():
            if key != "slug":
                print(f"     {key}: {str(value)[:96]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
