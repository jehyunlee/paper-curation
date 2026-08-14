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
from lib.evidence import PDF_SOURCES           # noqa: E402

DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"



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


PAPERS_DIR = ROOT / "docs" / "papers"


def adjudicate(slug: str, pdf_names: list[str],
               openalex_names: list[str]) -> str:
    """Which side the paper's own front matter supports.

    Neither source is authoritative. OpenAlex put "Rutgers Sexual and
    Reproductive Health and Rights", a Dutch organisation, on a paper whose
    byline reads "1Rutgers University"; the parser had it right. The document
    settles it, so each side's institution is looked for in the front matter
    the byline was read from.
    """
    text = PAPERS_DIR / slug / "text.md"
    if not text.exists():
        return "no-text"
    try:
        window = bib._fold(bib.affiliation_window(text))
    except Exception:
        return "no-text"

    def present(names: list[str]) -> bool:
        for name in names:
            tokens = bib._affiliation_tokens(name)
            distinctive = [x for x in tokens if len(x) >= 5]
            if distinctive and all(x in window for x in distinctive[:3]):
                return True
        return False

    in_pdf, in_oa = present(pdf_names), present(openalex_names)
    if in_pdf and not in_oa:
        return "pdf-supported"
    if in_oa and not in_pdf:
        return "openalex-supported"
    if in_pdf and in_oa:
        return "both-present"
    return "neither-present"


def render_review(rows: list[dict], conflicts: list[dict],
                  slugs: dict, people: dict) -> str:
    """A list to read, ordered so the likeliest errors come first.

    No rate is given. A disagreement between the two sources is not by itself
    an error — a Harvard Medical School faculty member listed by OpenAlex at
    Mass General is both — so this is a queue for a person, not a score.
    """
    lines = [
        "# 저자↔기관 검토 목록",
        "",
        f"OpenAlex 와 PDF 파서가 같은 저자에 대해 **공통점이 없는 기관**을 "
        f"말하는 쌍 **{len(rows):,}건**.",
        f"그중 국가까지 어긋난 것이 **{len(conflicts):,}건** — 겸직으로는 "
        f"설명되지 않으므로 한쪽이 틀렸다고 보아야 한다.",
        "",
        "일치율은 계산하지 않는다. 겸직(한 저자, 여러 소속)과 입도 차이"
        "(연구소 ↔ 그 상위 대학) 때문에 불일치가 곧 오류가 아니다.",
        "",
        "|우선|논문|저자|근거 등급|OpenAlex|PDF|원문 판정|",
        "|:--:|---|---|---|---|---|---|",
    ]
    for row in rows:
        mark = "⚠️" if row["country_conflict"] else "·"
        left = " / ".join(row["openalex"])[:70]
        right = " / ".join(row["pdf"])[:70]
        if row["country_conflict"]:
            left += f" ({', '.join(row['openalex_countries'])})"
            right += f" ({', '.join(row['pdf_countries'])})"
        verdict = row.get("verdict", "")
        lines.append(
            f"|{mark}|{slugs.get(row['paper_id'], '')[:44]}|"
            f"{people.get(row['author_id'], '')[:24]}|{row['source']}|"
            f"{left}|{right}|{verdict}|")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--source", help="one evidence class only")
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--out", type=Path,
                    help="검토 목록을 마크다운으로 저장한다")
    ap.add_argument("--adjudicate", action="store_true",
                    help="원문 front matter 로 어느 쪽이 맞는지 판정한다")
    ap.add_argument("--conflicts-only", action="store_true",
                    help="국가까지 어긋난 쌍만 (검토 우선순위)")
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
    if args.conflicts_only:
        rows = conflicts

    if args.adjudicate:
        from collections import Counter
        verdicts = Counter()
        for row in conflicts:
            row["verdict"] = adjudicate(
                slugs.get(row["paper_id"], ""), row["pdf"], row["openalex"])
            verdicts[row["verdict"]] += 1
        total = sum(verdicts.values()) or 1
        print(f"국가까지 어긋난 {total:,}쌍을 원문과 대조\n")
        for verdict, count in verdicts.most_common():
            print(f"  {verdict:22s} {count:5d}  ({count / total * 100:4.1f}%)")
        print("\n  pdf-supported      = 원문이 파서 쪽 기관을 담고 있다")
        print("  openalex-supported = 원문이 OpenAlex 쪽을 담고 있다")
        print("  both/neither       = 원문만으로 판정 불가")
        if args.out:
            args.out.parent.mkdir(parents=True, exist_ok=True)
            args.out.write_text(
                render_review(conflicts, conflicts, slugs, people),
                encoding="utf-8")
            print(f"\n저장: {args.out}")
        return 0

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(
            render_review(rows, conflicts, slugs, people), encoding="utf-8")
        print(f"저장: {args.out}  ({len(rows):,}쌍)")
        return 0

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
