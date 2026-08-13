#!/usr/bin/env python3
"""Are the author-to-institution links right, not just present.

    python pipeline/check_attribution_accuracy.py
    python pipeline/check_attribution_accuracy.py --source pdf.byline-marker --limit 10
    python pipeline/check_attribution_accuracy.py --json

`check_attribution_regression.py` counts how many papers resolve. Nothing
counted whether they resolve *correctly*, and the difference is not academic:
reviewing sixteen papers by hand found four wrong, including an Indonesian
institute on a Tsinghua paper and "National Center for PTSD" on a nuclear
materials paper. Both would have gone straight into an institution ranking.

The check is OpenAlex, which carries what the publisher deposited. Where it
and a PDF parser both answer for the same author on the same paper, they
should agree; where they do not, one of them is wrong and the pair is worth
looking at. Institutions are compared by ROR id, falling back to the folded
name, because OpenAlex mints its own rows for the same organisations.

Two things this does not do. It cannot judge a paper OpenAlex has never seen,
which is most of the corpus. And a disagreement is not proof the PDF side is
wrong — OpenAlex records the affiliation at publication, and a preprint's
byline can legitimately differ. Read the pairs, do not just take the rate.

Read-only.
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "pipeline"
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import build_bibliography_db as bib            # noqa: E402

DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"

# Everything derived from the PDF. `pdf.unmarked-multi` is deliberately absent:
# it links every author to every institution by construction, so measuring it
# against OpenAlex would measure the fallback, not a parser.
PDF_SOURCES = ("llm.byline", "pdf.byline-marker", "pdf.inline-affiliation",
               "pdf.author-information", "pdf.stacked-byline",
               "pdf.shared-byline", "pdf.sole-author",
               "pdf.sole-affiliation")


def institution_keys(conn: sqlite3.Connection) -> dict[int, str]:
    """One key per organisation, so two rows for it compare equal."""
    return {
        institution_id: (ror or bib._fold(name or ""))
        for institution_id, name, ror in conn.execute(
            "SELECT institution_id, institution_name, COALESCE(ror_id,'')"
            " FROM institutions")}


def compare(conn: sqlite3.Connection) -> dict:
    keys = institution_keys(conn)
    names = dict(conn.execute(
        "SELECT institution_id, institution_name FROM institutions"))
    deposited: dict[tuple, set] = defaultdict(set)
    parsed: dict[str, dict[tuple, set]] = defaultdict(lambda: defaultdict(set))
    for paper_id, author_id, institution_id, source in conn.execute(
            "SELECT paper_id, author_id, institution_id, source"
            " FROM paper_author_institutions"):
        key = keys.get(institution_id)
        if not key:
            continue
        if source == "openalex":
            deposited[(paper_id, author_id)].add((key, institution_id))
        elif source in PDF_SOURCES:
            parsed[source][(paper_id, author_id)].add((key, institution_id))

    report = {"by_source": {}, "pairs": 0, "agree": 0, "partial": 0,
              "disagree": 0, "detail": []}
    for source, mapping in parsed.items():
        agree = partial = disagree = 0
        for pair, found in mapping.items():
            reference = deposited.get(pair)
            if not reference:
                continue
            left = {key for key, _ in found}
            right = {key for key, _ in reference}
            if left == right:
                agree += 1
            elif left & right:
                partial += 1
            else:
                disagree += 1
                report["detail"].append({
                    "source": source, "paper_id": pair[0],
                    "author_id": pair[1],
                    "pdf": sorted(names.get(i, "") for _, i in found),
                    "openalex": sorted(names.get(i, "") for _, i in reference)})
        total = agree + partial + disagree
        if not total:
            continue
        report["by_source"][source] = {
            "pairs": total, "agree": agree, "partial": partial,
            "disagree": disagree,
            "rate": round((agree + partial) / total, 3)}
        report["pairs"] += total
        report["agree"] += agree
        report["partial"] += partial
        report["disagree"] += disagree
    return report


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--source", help="list disagreements for one class")
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True)
    conn.row_factory = None
    try:
        report = compare(conn)
        slugs = dict(conn.execute("SELECT paper_id, slug FROM papers"))
        people = dict(conn.execute(
            "SELECT author_id, display_name FROM authors"))
    finally:
        conn.close()

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0

    print("OpenAlex 가 기록한 소속과 PDF 파서가 읽은 소속의 일치\n")
    print(f"  {'근거 등급':26s}{'비교':>7s}{'일치':>7s}{'부분':>7s}"
          f"{'불일치':>8s}{'일치율':>9s}")
    for source, row in sorted(report["by_source"].items()):
        print(f"  {source:26s}{row['pairs']:7d}{row['agree']:7d}"
              f"{row['partial']:7d}{row['disagree']:8d}"
              f"{row['rate'] * 100:8.1f}%")
    total = report["pairs"]
    if total:
        rate = (report["agree"] + report["partial"]) / total
        print(f"\n  {'전체':26s}{total:7d}{report['agree']:7d}"
              f"{report['partial']:7d}{report['disagree']:8d}"
              f"{rate * 100:8.1f}%")
    else:
        print("\n  비교 가능한 쌍이 없다 — OpenAlex 보강을 먼저 실행한다.")

    if args.source:
        shown = [d for d in report["detail"] if d["source"] == args.source]
        print(f"\n── {args.source} 불일치 {len(shown)}건 중 {args.limit}건")
        for item in shown[:args.limit]:
            print(f"  {slugs.get(item['paper_id'], '')[:44]:44s} "
                  f"{people.get(item['author_id'], '')[:20]}")
            print(f"     OpenAlex: {item['openalex']}")
            print(f"     PDF     : {item['pdf']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
