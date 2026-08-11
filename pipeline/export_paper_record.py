#!/usr/bin/env python3
"""Export one paper's bibliography record, annotated with where each value lives.

Answers "what does the DB actually hold for this paper, and which table holds
it" — every field is printed with its `table.column`, and every value carries
the provenance column the pipeline recorded next to it (`bibliography_source`,
`paper_institutions.source`, `institutions.name_source`), so a number can be
traced back to Zotero, Scopus or the PDF without opening the database.

    python pipeline/export_paper_record.py --doi 10.32479/irmm.23293
    python pipeline/export_paper_record.py --slug 2743_Mapping_fMRI
    python pipeline/export_paper_record.py --doi ... --out reports/source/x.md
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"
SOURCE_DIR = ROOT / "reports" / "source"

# papers columns worth naming individually, in reading order.
PAPER_FIELDS = [
    ("slug", "슬러그 — `docs/papers/{slug}/` 와 1:1"),
    ("title", "제목"),
    ("doi", "DOI"),
    ("url", "URL"),
    ("arxiv_id", "arXiv ID"),
    ("journal_name", "저널"),
    ("volume", "권"), ("issue", "호"), ("pages", "쪽"),
    ("publisher", "출판사"),
    ("issn", "ISSN"), ("eissn", "eISSN"),
    ("publication_date", "발행일"),
    ("received_date", "투고일"),
    ("accepted_date", "게재확정일"),
    ("published_online_date", "온라인 공개일"),
    ("document_type", "문서 유형"),
    ("zotero_item_key", "Zotero 아이템 키"),
    ("scopus_eid", "Scopus EID"),
    ("bibliography_source", "**서지 출처**"),
    ("affiliation_source", "소속 출처"),
    ("affiliation_confidence", "소속 신뢰도"),
    ("review_dir", "리뷰 디렉토리"),
    ("created_at", "DB 최초 기록"),
]

SOURCE_MEANING = {
    "zotero-local": "Zotero 단독으로 완결 (출판사 전사본)",
    "zotero-local+scopus": "Zotero + Scopus 가 빈칸 보충",
    "zotero-local+pdf": "Zotero + PDF 앞부분이 빈칸 보충",
    "zotero-local+scopus+pdf": "Zotero + Scopus + PDF 보충",
    "scopus+pdf": "Scopus 가 제시하고 PDF 본문에서 확인됨",
    "scopus-unconfirmed": "Scopus 에만 있고 PDF 확인 실패",
    "pdf": "PDF 앞부분에서만 발견 (Scopus 미등재)",
}


def find(conn: sqlite3.Connection, doi: str | None, slug: str | None):
    conn.row_factory = sqlite3.Row
    if doi:
        row = conn.execute(
            "SELECT * FROM papers WHERE lower(doi)=lower(?)", (doi.strip(),)
        ).fetchone()
        if row:
            return row
        return conn.execute(
            "SELECT * FROM papers WHERE doi LIKE ?", (f"%{doi.strip()}%",)
        ).fetchone()
    return conn.execute(
        "SELECT * FROM papers WHERE slug=? OR slug LIKE ?", (slug, f"{slug}%")
    ).fetchone()


def render(conn: sqlite3.Connection, paper: sqlite3.Row) -> str:
    conn.row_factory = sqlite3.Row
    pid = paper["paper_id"]
    L = [f"# {paper['title']}", "",
         f"`{paper['doi'] or paper['slug']}`", "",
         "각 값 옆의 `table.column` 이 그 값이 실제로 저장된 위치다.", ""]

    L += ["## `papers` — 서지 본체", "",
          "논문 1편 = 1행. Zotero 레코드를 참값으로 두고 Scopus·PDF 가 빈칸만 채운다.", "",
          "| 항목 | 값 | 저장 위치 |", "|---|---|---|"]
    for col, label in PAPER_FIELDS:
        value = paper[col] if col in paper.keys() else None
        if value in (None, ""):
            continue
        shown = f"`{value}`" if col in ("slug", "doi", "zotero_item_key",
                                        "review_dir", "scopus_eid") else value
        L.append(f"| {label} | {shown} | `papers.{col}` |")
    L.append("")
    meaning = SOURCE_MEANING.get(paper["bibliography_source"] or "")
    if meaning:
        L += [f"> `bibliography_source = {paper['bibliography_source']}` — {meaning}", ""]

    authors = conn.execute(
        "SELECT a.display_name, a.normalized_name, pa.author_order,"
        " pa.is_first_author, pa.is_corresponding_author, pa.source"
        " FROM paper_authors pa JOIN authors a ON a.author_id=pa.author_id"
        " WHERE pa.paper_id=? ORDER BY pa.author_order", (pid,)).fetchall()
    L += [f"## `authors` + `paper_authors` — 저자 {len(authors)}명", "",
          "이름 정본은 `authors`, 이 논문에서의 순서·역할은 `paper_authors` 에 있다.", "",
          "| # | 저자 | 역할 | 저장 위치 |", "|---|---|---|---|"]
    for a in authors:
        role = " · ".join(filter(None, [
            "제1저자" if a["is_first_author"] else "",
            "교신저자" if a["is_corresponding_author"] else ""])) or "—"
        L.append(f"| {a['author_order']} | {a['display_name']} | {role} | "
                 f"`authors.display_name` / `paper_authors.author_order` |")
    if authors:
        L += ["", f"> 출처: `paper_authors.source = {authors[0]['source']}`", ""]

    insts = conn.execute(
        "SELECT i.institution_name, i.country_name_en, i.hq_country_name_en,"
        " i.parent_name, i.ror_id, i.name_source, pi.raw_name, pi.source,"
        " pi.country_name"
        " FROM paper_institutions pi JOIN institutions i"
        " ON i.institution_id=pi.institution_id"
        " WHERE pi.paper_id=? ORDER BY i.institution_name", (pid,)).fetchall()
    L += [f"## `institutions` + `paper_institutions` — 기관 {len(insts)}곳", "",
          "기관 정본은 `institutions` (ROR 정규화), 이 논문과의 연결과 "
          "**원문 문자열**은 `paper_institutions` 에 있다.", ""]
    for n, i in enumerate(insts, 1):
        ror = i["ror_id"].rsplit("/", 1)[-1] if i["ror_id"] else "미해결"
        L += [f"### {n}. {i['institution_name']}", "",
              "| 항목 | 값 | 저장 위치 |", "|---|---|---|",
              f"| 소재 국가 | {i['country_name_en'] or '—'} | `institutions.country_name_en` |",
              f"| 본사 국가 | {i['hq_country_name_en'] or '—'} | `institutions.hq_country_name_en` |",
              f"| 상위 그룹 | {i['parent_name'] or '— (최상위)'} | `institutions.parent_name` |",
              f"| ROR ID | `{ror}` | `institutions.ror_id` |",
              f"| 정규화 근거 | `{i['name_source'] or '—'}` | `institutions.name_source` |",
              f"| 링크 출처 | `{i['source']}` — {SOURCE_MEANING.get(i['source'], '')} | `paper_institutions.source` |",
              f"| PDF 원문 | `{(i['raw_name'] or '')[:110]}` | `paper_institutions.raw_name` |",
              ""]

    docs = conn.execute(
        "SELECT document_type, path, sha256, bytes FROM source_documents"
        " WHERE paper_id=? ORDER BY document_type", (pid,)).fetchall()
    if docs:
        L += ["## `source_documents` — 원문 파일", "",
              "변경 감지용 해시. `--changed-only` 빌드가 이 값으로 재처리 여부를 정한다.", "",
              "| 유형 | 크기 | SHA-256 | 경로 |", "|---|---:|---|---|"]
        for d in docs:
            L.append(f"| `{d['document_type']}` | {d['bytes']:,}B | "
                     f"`{d['sha256'][:16]}…` | `{d['path']}` |")
        L.append("")

    cites = conn.execute(
        "SELECT observed_date, openalex_count, crossref_count, scopus_count,"
        " normalized_percentile FROM citation_snapshots WHERE paper_id=?"
        " ORDER BY observed_date DESC", (pid,)).fetchall()
    L += ["## `citation_snapshots` — 피인용", ""]
    if cites:
        L += ["| 관측일 | OpenAlex | Crossref | Scopus | 백분위 |",
              "|---|---:|---:|---:|---:|"]
        for c in cites:
            L.append(f"| {c['observed_date']} | {c['openalex_count']} | "
                     f"{c['crossref_count']} | {c['scopus_count']} | "
                     f"{c['normalized_percentile']} |")
    else:
        L.append("기록 없음 — `run_metrics.py` 가 아직 이 논문을 수집하지 않았다.")
    L.append("")

    L += ["## DB 밖에 있는 것", "",
          "| 자산 | 위치 | 연결 |", "|---|---|---|",
          f"| 한글 리뷰 | `{paper['review_dir']}/review.md` | `papers.review_dir` |",
          f"| PDF 본문 | `{paper['review_dir']}/text.md` | `source_documents.path` |",
          f"| 도판 | `{paper['review_dir']}/figures/` | 슬러그 |",
          "| 토픽 분류 | `docs/{topic}/_new_classification.json` | 슬러그 |",
          "| 마스터 인덱스 | `docs/papers/_papers_index.json` | 슬러그 |", ""]
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--doi")
    ap.add_argument("--slug")
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()
    if not (args.doi or args.slug):
        print("--doi 또는 --slug 필요", file=sys.stderr)
        return 2
    conn = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True)
    try:
        paper = find(conn, args.doi, args.slug)
        if paper is None:
            print(json.dumps({"found": False, "doi": args.doi,
                              "slug": args.slug}, ensure_ascii=False))
            return 1
        text = render(conn, paper)
    finally:
        conn.close()
    out = args.out or (SOURCE_DIR / f"record_{paper['slug'][:40]}.md")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(json.dumps({"found": True, "slug": paper["slug"],
                      "md": str(out), "bytes": out.stat().st_size},
                     ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
