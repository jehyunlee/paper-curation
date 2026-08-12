#!/usr/bin/env python3
"""Most active institutions in a field, and the researchers behind them.

    python pipeline/report_field_leaders.py --topic ai4s --top 20
    python pipeline/report_field_leaders.py --topic ai4s --json

Institution counts come from `paper_institutions`, which records that a paper
carries an affiliation — that link is safe to count.

Researchers do not come from the same place. Mapping an author to one of a
paper's institutions needs the byline superscripts, and when a paper lists
several institutions without them the builder links every author to every one:
86% of `paper_author_institutions` is that fallback, tagged
`pdf.unmarked-multi`. Counting it credits a university with authors who were
never there, so this report refuses it and uses only:

  openalex             the mapping the publisher deposited (ROR-backed)
  pdf.byline-marker    superscripts actually resolved
  pdf.inline-affiliation the byline names it on the author's own line (ACM)
  pdf.sole-affiliation one institution on the paper, so no ambiguity

`--include-guessed` puts the fallback back in, and the report says so, because
a number whose evidence is unstated is worse than no number.

Impact uses the newest `citation_snapshots` row per paper. Coverage is printed
rather than assumed: a citation column over a corpus that is only partly
collected would silently rank the collected papers first.
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"

TRUSTED_SOURCES = ("openalex", "pdf.byline-marker", "pdf.inline-affiliation",
                   "pdf.sole-affiliation")

# Newest snapshot per paper, with the highest count any source reported.
# Scopus indexes less than OpenAlex, so the sources are kept separate in the
# table and only reconciled here, at read time.
LATEST_CITATIONS = """
  SELECT cs.paper_id,
         MAX(COALESCE(cs.openalex_count, 0), COALESCE(cs.crossref_count, 0),
             COALESCE(cs.scopus_count, 0)) AS citations,
         cs.normalized_percentile AS percentile
  FROM citation_snapshots cs
  JOIN (SELECT paper_id, MAX(observed_date) d FROM citation_snapshots
        GROUP BY paper_id) newest
    ON newest.paper_id = cs.paper_id AND newest.d = cs.observed_date
"""

TOPIC_PAPERS = """
  SELECT p.paper_id
  FROM papers p
  JOIN json_each(json_extract(p.metadata_json, '$.topics')) t
  WHERE t.value = ?
"""


def institutions(conn, topic: str, top: int) -> list[dict]:
    rows = conn.execute(f"""
      WITH topic_papers AS ({TOPIC_PAPERS}), cites AS ({LATEST_CITATIONS})
      SELECT i.institution_id, i.institution_name,
             COALESCE(i.country_name_en, '') country,
             COUNT(DISTINCT pi.paper_id) papers,
             COUNT(DISTINCT c.paper_id) papers_with_citations,
             COALESCE(SUM(c.citations), 0) citations,
             ROUND(AVG(c.percentile), 3) mean_percentile
      FROM paper_institutions pi
      JOIN topic_papers tp ON tp.paper_id = pi.paper_id
      JOIN institutions i ON i.institution_id = pi.institution_id
      LEFT JOIN cites c ON c.paper_id = pi.paper_id
      GROUP BY i.institution_id
      ORDER BY papers DESC, citations DESC
      LIMIT ?""", (topic, top)).fetchall()
    return [dict(row) for row in rows]


def researchers(conn, topic: str, institution_id: int, limit: int,
                sources: tuple[str, ...]) -> list[dict]:
    marks = ",".join("?" * len(sources))
    rows = conn.execute(f"""
      WITH topic_papers AS ({TOPIC_PAPERS}), cites AS ({LATEST_CITATIONS})
      SELECT a.display_name, COALESCE(a.orcid, '') orcid,
             COUNT(DISTINCT pai.paper_id) papers,
             COALESCE(SUM(c.citations), 0) citations,
             SUM(COALESCE(pa.is_first_author, 0)) first_author,
             SUM(COALESCE(pa.is_corresponding_author, 0)) corresponding
      FROM paper_author_institutions pai
      JOIN topic_papers tp ON tp.paper_id = pai.paper_id
      JOIN authors a ON a.author_id = pai.author_id
      LEFT JOIN paper_authors pa
        ON pa.paper_id = pai.paper_id AND pa.author_id = pai.author_id
      LEFT JOIN cites c ON c.paper_id = pai.paper_id
      WHERE pai.institution_id = ? AND pai.source IN ({marks})
      GROUP BY a.author_id
      ORDER BY papers DESC, citations DESC, corresponding DESC
      LIMIT ?""", (topic, institution_id, *sources, limit)).fetchall()
    return [dict(row) for row in rows]


def coverage(conn, topic: str, sources: tuple[str, ...]) -> dict:
    marks = ",".join("?" * len(sources))
    papers = conn.execute(
        f"SELECT COUNT(*) FROM ({TOPIC_PAPERS})", (topic,)).fetchone()[0]
    with_cites = conn.execute(f"""
      WITH topic_papers AS ({TOPIC_PAPERS}), cites AS ({LATEST_CITATIONS})
      SELECT COUNT(*) FROM topic_papers tp
      JOIN cites c ON c.paper_id = tp.paper_id""", (topic,)).fetchone()[0]
    with_authors = conn.execute(f"""
      WITH topic_papers AS ({TOPIC_PAPERS})
      SELECT COUNT(DISTINCT pai.paper_id) FROM paper_author_institutions pai
      JOIN topic_papers tp ON tp.paper_id = pai.paper_id
      WHERE pai.source IN ({marks})""", (topic, *sources)).fetchone()[0]
    return {
        "topic_papers": papers,
        "papers_with_citations": with_cites,
        "citation_coverage": round(with_cites / papers, 3) if papers else 0.0,
        "papers_with_trusted_author_links": with_authors,
        "author_link_coverage": round(with_authors / papers, 3) if papers else 0.0,
    }


def render(topic: str, cov: dict, rows: list[dict], per: int,
           guessed: bool) -> str:
    lines = [f"# {topic} — 가장 활발한 기관 {len(rows)}곳", ""]
    lines.append(f"- 대상 논문 **{cov['topic_papers']:,}편**")
    lines.append(f"- 피인용 수집됨 **{cov['papers_with_citations']:,}편** "
                 f"({cov['citation_coverage'] * 100:.1f}%)")
    lines.append(f"- 저자↔기관이 근거로 확정된 논문 "
                 f"**{cov['papers_with_trusted_author_links']:,}편** "
                 f"({cov['author_link_coverage'] * 100:.1f}%)")
    if guessed:
        lines.append("- ⚠️ `--include-guessed`: 마커 없는 논문의 저자×기관 "
                     "전조합이 포함됨 — 소속이 아닌 사람이 섞인다")
    lines.append("")
    lines.append("|#|기관|국가|논문|피인용|평균 백분위|대표 연구자|")
    lines.append("|--:|---|---|--:|--:|--:|---|")
    for rank, row in enumerate(rows, 1):
        people = " · ".join(
            f"{r['display_name']}({r['papers']})" for r in row["researchers"]
        ) or "—"
        pct = ("-" if row["mean_percentile"] is None
               else f"{row['mean_percentile']:.2f}")
        lines.append(
            f"|{rank}|{row['institution_name']}|{row['country'] or '-'}|"
            f"{row['papers']}|{row['citations']}|{pct}|{people}|")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--topic", default="ai4s")
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--researchers", type=int, default=5)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--include-guessed", action="store_true",
                    help="마커 없는 저자×기관 전조합까지 포함 (권장하지 않음)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()

    sources = TRUSTED_SOURCES + (("pdf.unmarked-multi",)
                                 if args.include_guessed else ())
    conn = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    try:
        cov = coverage(conn, args.topic, sources)
        rows = institutions(conn, args.topic, args.top)
        for row in rows:
            row["researchers"] = researchers(
                conn, args.topic, row["institution_id"], args.researchers,
                sources)
    finally:
        conn.close()

    if args.json:
        print(json.dumps({"topic": args.topic, "coverage": cov,
                          "institutions": rows}, ensure_ascii=False, indent=2))
    else:
        text = render(args.topic, cov, rows, args.researchers,
                      args.include_guessed)
        print(text)
        if args.out:
            args.out.parent.mkdir(parents=True, exist_ok=True)
            args.out.write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
