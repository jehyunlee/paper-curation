#!/usr/bin/env python3
"""Show how one paper's authors and affiliations were arrived at, table by table.

Answers "who wrote this and where do they work" and, more usefully, shows the
path: which row in which table supplied each part of the answer and which class
of evidence decided it. Written as a script rather than typed out each time,
because a query whose result cannot be reproduced is not a check.

Usage:
    python pipeline/explain_paper_attribution.py --doi 10.1038/s43588-025-00906-6
    python pipeline/explain_paper_attribution.py --slug 1022_SciSciGPT --json
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "pipeline"
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

from lib.evidence import RESOLVED_SOURCES, UNRESOLVED_SOURCE   # noqa: E402

DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"


def find_paper(conn: sqlite3.Connection, doi: str | None,
               slug: str | None) -> sqlite3.Row:
    if doi:
        row = conn.execute(
            "SELECT * FROM papers WHERE lower(doi)=lower(?)", (doi,)).fetchone()
    else:
        row = conn.execute(
            "SELECT * FROM papers WHERE slug LIKE ?||'%'", (slug,)).fetchone()
    if row is None:
        raise SystemExit("no such paper")
    return row


def collect(conn: sqlite3.Connection, paper: sqlite3.Row) -> dict:
    pid = paper["paper_id"]
    marks = ",".join("?" * len(RESOLVED_SOURCES))

    authors = [dict(r) for r in conn.execute(
        "SELECT pa.author_order, a.author_id, a.display_name,"
        " a.normalized_name, COALESCE(a.orcid,'') orcid,"
        " COALESCE(a.openalex_id,'') openalex_id,"
        " pa.is_first_author, pa.is_corresponding_author, pa.source"
        " FROM paper_authors pa JOIN authors a USING(author_id)"
        " WHERE pa.paper_id=? ORDER BY pa.author_order", (pid,))]

    candidates = [dict(r) for r in conn.execute(
        "SELECT pi.institution_id, i.institution_name,"
        " COALESCE(i.country_name_en,'') country, COALESCE(i.ror_id,'') ror_id,"
        " COALESCE(i.parent_name,'') parent_name,"
        " pi.raw_name, pi.source"
        " FROM paper_institutions pi JOIN institutions i USING(institution_id)"
        " WHERE pi.paper_id=? ORDER BY i.institution_name", (pid,))]

    links = [dict(r) for r in conn.execute(
        "SELECT a.display_name author, i.institution_name institution,"
        " COALESCE(i.country_name_en,'') country, x.source, x.marker,"
        " x.author_order"
        " FROM paper_author_institutions x JOIN authors a USING(author_id)"
        " JOIN institutions i USING(institution_id)"
        " WHERE x.paper_id=? ORDER BY x.author_order, x.source", (pid,))]

    attempts = [dict(r) for r in conn.execute(
        "SELECT extractor, attempted_at, outcome, links, COALESCE(detail,'')"
        " detail FROM extraction_attempts WHERE paper_id=?", (pid,))]

    documents = [dict(r) for r in conn.execute(
        "SELECT document_type, path, bytes FROM source_documents"
        " WHERE paper_id=?", (pid,))]

    resolved = conn.execute(
        f"SELECT COUNT(DISTINCT author_id) FROM paper_author_institutions"
        f" WHERE paper_id=? AND source IN ({marks})",
        (pid, *RESOLVED_SOURCES)).fetchone()[0]

    return {"paper": dict(paper), "authors": authors,
            "candidate_institutions": candidates, "links": links,
            "attempts": attempts, "documents": documents,
            "authors_placed": resolved}


def render(data: dict) -> str:
    paper = data["paper"]
    out: list[str] = []
    add = out.append

    add("=" * 78)
    add("① papers — 논문 자체")
    add("=" * 78)
    add(f"  paper_id           {paper['paper_id']}")
    add(f"  slug               {paper['slug']}")
    add(f"  title              {paper['title']}")
    add(f"  doi                {paper.get('doi') or '-'}")
    add(f"  journal            {paper.get('journal_name') or '-'}")
    add(f"  date               {paper.get('publication_date') or '-'}")
    add(f"  affiliation_source {paper.get('affiliation_source') or '-'}"
        f"  (confidence {paper.get('affiliation_confidence')})")
    add(f"  zotero_item_key    {paper.get('zotero_item_key') or '-'}")

    add("")
    add("=" * 78)
    add("② source_documents — 답의 근거가 된 파일")
    add("=" * 78)
    for doc in data["documents"]:
        add(f"  {doc['document_type']:14s} {doc['bytes']:>9,} bytes"
            f"  {doc['path']}")
    if not data["documents"]:
        add("  (없음)")

    add("")
    add("=" * 78)
    add("③ paper_authors + authors — 저자와 그 신원")
    add("=" * 78)
    add(f"  {'#':>2}  {'display_name':26s} {'ORCID':21s} {'openalex':13s} 표시")
    for a in data["authors"]:
        flags = ("first" if a["is_first_author"] else "") + \
                (" corr" if a["is_corresponding_author"] else "")
        add(f"  {a['author_order']:>2}  {a['display_name'][:26]:26s} "
            f"{(a['orcid'] or '-'):21s} {(a['openalex_id'] or '-'):13s} "
            f"{flags}")
    if data["authors"]:
        add(f"  source: {data['authors'][0]['source']}")

    add("")
    add("=" * 78)
    add("④ paper_institutions — 이 논문의 기관 후보 (모든 파서가 여기에 접지)")
    add("=" * 78)
    add(f"  {'institution':38s} {'country':14s} {'source':20s} ROR")
    for c in data["candidate_institutions"]:
        add(f"  {c['institution_name'][:38]:38s} {c['country'][:14]:14s} "
            f"{c['source']:20s} {'있음' if c['ror_id'] else '없음'}")
        add(f"      raw: {(c['raw_name'] or '')[:66]}")
    if not data["candidate_institutions"]:
        add("  (없음 — 이 목록이 비면 어떤 파서도 저자를 붙일 수 없다)")

    add("")
    add("=" * 78)
    add("⑤ paper_author_institutions — 저자↔기관, 근거 등급별")
    add("=" * 78)
    resolved = [l for l in data["links"] if l["source"] in RESOLVED_SOURCES]
    guessed = [l for l in data["links"] if l["source"] == UNRESOLVED_SOURCE]
    add(f"  {'author':22s} {'institution':32s} {'evidence':20s} marker")
    for l in resolved:
        add(f"  {l['author'][:22]:22s} {l['institution'][:32]:32s} "
            f"{l['source']:20s} {l['marker'] or '-'}")
    if guessed:
        add(f"  … 추정({UNRESOLVED_SOURCE}) {len(guessed)}행 — 리포트에서 제외됨")
    if not data["links"]:
        add("  (없음)")

    add("")
    add("=" * 78)
    add("⑥ extraction_attempts — 무엇을 시도했나")
    add("=" * 78)
    for t in data["attempts"]:
        add(f"  {t['extractor']:14s} {t['outcome']:10s} links={t['links']:<4} "
            f"{t['attempted_at']}")
    if not data["attempts"]:
        add("  (기록 없음 — 이 논문에는 페이지 판독기를 돌린 적이 없다)")

    add("")
    add("=" * 78)
    add("최종 답")
    add("=" * 78)
    by_author: dict[str, list[str]] = {}
    for l in resolved:
        by_author.setdefault(l["author"], [])
        label = l["institution"] + (f" ({l['country']})" if l["country"] else "")
        if label not in by_author[l["author"]]:
            by_author[l["author"]].append(label)
    for a in data["authors"]:
        places = by_author.get(a["display_name"])
        add(f"  {a['author_order']:>2}. {a['display_name']}")
        for place in (places or ["— 미확정"]):
            add(f"        {place}")
    add("")
    add(f"  저자 {len(data['authors'])}명 중 기관 확정 {data['authors_placed']}명")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--doi")
    ap.add_argument("--slug")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    if not (args.doi or args.slug):
        ap.error("--doi 또는 --slug 가 필요하다")

    conn = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    try:
        data = collect(conn, find_paper(conn, args.doi, args.slug))
    finally:
        conn.close()
    print(json.dumps(data, ensure_ascii=False, indent=2, default=str)
          if args.json else render(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
