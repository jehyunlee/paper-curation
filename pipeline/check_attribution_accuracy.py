#!/usr/bin/env python3
"""Author-institution pairs worth a human look, ranked by how wrong they smell.

    python pipeline/check_attribution_accuracy.py
    python pipeline/check_attribution_accuracy.py --limit 30 --json

This was written as an accuracy metric and that was a mistake worth recording.
It compared what a PDF parser read against what OpenAlex deposited and reported
the agreement rate, which came out at 0 of 335 and then 1.7% of 1,017. Neither
number meant what it looked like:

    Ming Y. Lu   OpenAlex: Brigham and Women's Hospital, Mass General, MIT
                 PDF     : Broad Institute, Harvard Medical School

Both are right. A Harvard Medical School faculty member holding hospital
appointments is ordinary, and the two sources simply chose different ones. The
byline of another paper names the National Key Laboratory of Data Space
Technology and System where OpenAlex names Peking University — the university
that laboratory belongs to. Rolling up to parents recovered a handful of those
and could not recover the rest, because only 588 of 3,526 institutions have a
parent recorded at all.

So there is no agreement rate to report. What the comparison is good for is
finding the pairs where the two sources are not describing the same place at
all — "University of Hong Kong" against "Massachusetts Institute of
Technology" is not a co-affiliation, it is an error in one of them. Those are
ranked first, by country disagreement, and printed for review.

The only measurements of accuracy this corpus has are hand checks: 88.6% of 70
pairs when the rendered-page reader was graded against the marker parser, and
four wrong of sixteen when the shared-byline rule was reviewed by eye. A
sampled human check is the instrument; this is the thing that decides what to
sample.

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

PDF_SOURCES = ("llm.byline", "pdf.byline-marker", "pdf.inline-affiliation",
               "pdf.author-information", "pdf.stacked-byline",
               "pdf.shared-byline", "pdf.sole-author",
               "pdf.sole-affiliation")


def institution_facts(conn: sqlite3.Connection) -> dict[int, dict]:
    """Name, country and the names this institution may also be called by."""
    parents: dict[str, str] = {}
    facts: dict[int, dict] = {}
    for institution_id, name, ror, parent, country in conn.execute(
            "SELECT institution_id, institution_name, COALESCE(ror_id,''),"
            " COALESCE(parent_name,''), COALESCE(country_name_en,'')"
            " FROM institutions"):
        keys = {ror or bib._fold(name or "")}
        if parent:
            keys.add(bib._fold(parent))
        facts[institution_id] = {"name": name, "country": country,
                                 "keys": {k for k in keys if k}}
        parents[bib._fold(name or "")] = bib._fold(parent) if parent else ""
    for entry in facts.values():
        for key in list(entry["keys"]):
            grand = parents.get(key)
            if grand:
                entry["keys"].add(grand)
    return facts


def review_candidates(conn: sqlite3.Connection) -> list[dict]:
    facts = institution_facts(conn)
    deposited: dict[tuple, set] = defaultdict(set)
    parsed: dict[tuple, set] = defaultdict(set)
    origin: dict[tuple, str] = {}
    for paper_id, author_id, institution_id, source in conn.execute(
            "SELECT paper_id, author_id, institution_id, source"
            " FROM paper_author_institutions"):
        if institution_id not in facts:
            continue
        if source == "openalex":
            deposited[(paper_id, author_id)].add(institution_id)
        elif source in PDF_SOURCES:
            parsed[(paper_id, author_id)].add(institution_id)
            origin[(paper_id, author_id)] = source

    out = []
    for pair, found in parsed.items():
        reference = deposited.get(pair)
        if not reference:
            continue
        left = set().union(*(facts[i]["keys"] for i in found))
        right = set().union(*(facts[i]["keys"] for i in reference))
        if left & right:
            continue                       # the two describe the same place
        countries_left = {facts[i]["country"] for i in found if facts[i]["country"]}
        countries_right = {facts[i]["country"] for i in reference
                           if facts[i]["country"]}
        # A co-affiliation is normally in one country; a parser that read the
        # wrong byline line usually is not.
        conflict = bool(countries_left and countries_right
                        and not (countries_left & countries_right))
        out.append({
            "paper_id": pair[0], "author_id": pair[1],
            "source": origin[pair], "country_conflict": conflict,
            "pdf": sorted(facts[i]["name"] for i in found),
            "openalex": sorted(facts[i]["name"] for i in reference),
            "pdf_countries": sorted(countries_left),
            "openalex_countries": sorted(countries_right)})
    out.sort(key=lambda row: (not row["country_conflict"], row["source"]))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--source", help="one evidence class only")
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True)
    try:
        rows = review_candidates(conn)
        slugs = dict(conn.execute("SELECT paper_id, slug FROM papers"))
        people = dict(conn.execute(
            "SELECT author_id, display_name FROM authors"))
    finally:
        conn.close()

    if args.source:
        rows = [r for r in rows if r["source"] == args.source]
    conflicts = [r for r in rows if r["country_conflict"]]

    if args.json:
        print(json.dumps({"candidates": len(rows),
                          "country_conflicts": len(conflicts),
                          "detail": rows[:args.limit]},
                         ensure_ascii=False, indent=2))
        return 0

    print("OpenAlex 와 PDF 가 같은 저자에 대해 서로 다른 기관을 말하는 쌍\n")
    print(f"  검토 대상 {len(rows):,}쌍 · 그중 국가까지 어긋남 "
          f"{len(conflicts):,}쌍\n")
    by_source: dict[str, int] = defaultdict(int)
    for row in rows:
        by_source[row["source"]] += 1
    for source, count in sorted(by_source.items(), key=lambda kv: -kv[1]):
        hard = sum(1 for r in rows
                   if r["source"] == source and r["country_conflict"])
        print(f"  {source:26s} {count:5d}쌍  국가 불일치 {hard}")

    print(f"\n── 국가까지 어긋난 쌍 (가장 의심스러운 것부터) {args.limit}건")
    for row in conflicts[:args.limit]:
        print(f"  {slugs.get(row['paper_id'], '')[:40]:40s} "
              f"{people.get(row['author_id'], '')[:18]:18s} [{row['source']}]")
        print(f"     OpenAlex: {row['openalex']} {row['openalex_countries']}")
        print(f"     PDF     : {row['pdf']} {row['pdf_countries']}")
    print("\n일치율은 내지 않는다. 겸직과 상하 관계 때문에 두 출처의 불일치가"
          " 곧 오류가 아니며, 정확도는 표본 수동 검증으로만 확인된다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
