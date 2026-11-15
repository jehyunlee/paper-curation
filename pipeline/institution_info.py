#!/usr/bin/env python3
"""Selected papers' research institutions, as the bibliography DB holds them.

Paper Curio's "View Research Institute Info" runs this for the selected
papers and shows the page in its own window: per paper, a table of
institutions with parent, city, country, ROR record and source, and a table of
authors with the institutions the byline ties them to. The page is one
self-contained HTML file; the last stdout line is a JSON receipt.

    python pipeline/institution_info.py --paper 042_Some_Paper --out /tmp/x.html
    python pipeline/institution_info.py --paper 042_A --paper 043_B \
        --unreviewed "Title without a review" --out /tmp/x.html

Read-only: the DB is opened with ``mode=ro``. A paper the DB does not hold yet
is shown as not ingested, not as a paper without institutions. A DB built
before the institution naming pass has no ``city_name`` column; the page says
so instead of failing.
"""
from __future__ import annotations

import argparse
import html
import json
import os
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = Path(os.environ.get(
    "PAPER_CURATION_BIBLIO_DB", str(ROOT / ".cache" / "bibliography.sqlite3")))

# A byline with several affiliations and no superscripts: every author was
# linked to every institution because the split is unknown.
GUESSED_AUTHOR_SOURCE = "pdf.unmarked-multi"

SOURCE_LABELS = {
    "ko": {
        "scopus+pdf": "Scopus·PDF 일치",
        "pdf": "PDF",
        "scopus-unconfirmed": "Scopus (PDF 미확인)",
        "openalex": "OpenAlex (본문 확인)",
        "link:openalex": "OpenAlex (본문 확인)",
        "link:llm.byline": "PDF 바이라인 판독",
        "link:scopus": "Scopus",
    },
    "en": {
        "scopus+pdf": "Scopus, confirmed in PDF",
        "pdf": "PDF",
        "scopus-unconfirmed": "Scopus (not found in PDF)",
        "openalex": "OpenAlex (named in text)",
        "link:openalex": "OpenAlex (named in text)",
        "link:llm.byline": "PDF byline reading",
        "link:scopus": "Scopus",
    },
}

TEXT = {
    "ko": {
        "title": "연구기관 정보",
        "institutions": "소속기관",
        "institution": "소속기관",
        "parent": "상위기관",
        "city": "도시",
        "country": "국가",
        "source": "출처",
        "authors": "저자별 소속",
        "author": "저자",
        "unknown": "바이라인에 저자별 구분 없음",
        "none": "연결된 기관 없음",
        "no_institutions": "이 논문에 연결된 기관이 없습니다.",
        "not_ingested": "서지 DB에 아직 없습니다. Review를 다시 생성하거나 bibliography-update를 실행하세요.",
        "unreviewed": "코퍼스에 리뷰가 없습니다. 먼저 Review 생성을 실행하세요.",
        "papers": "논문",
        "summary": "{papers}편 · 기관 {institutions}곳",
        "not_normalized": ("이 서지 DB에는 아직 기관명 정규화(도시 칸)가 적용되지 않았습니다. "
                           "`python pipeline/normalize_institutions.py --apply` 후 다시 여세요."),
        "show_authors": "저자 {count}명",
        "note": ("기관명은 ROR 영문 공식 명칭, 상위기관이 없으면 기관명 자신, "
                 "도시·국가는 소속 문자열에 명시된 값이 우선이고 없으면 ROR 위치입니다."),
    },
    "en": {
        "title": "Research institute info",
        "institutions": "Institutions",
        "institution": "Institution",
        "parent": "Parent",
        "city": "City",
        "country": "Country",
        "source": "Source",
        "authors": "Authors and affiliations",
        "author": "Author",
        "unknown": "byline does not say which author sits where",
        "none": "no institution linked",
        "no_institutions": "No institution is linked to this paper.",
        "not_ingested": "Not in the bibliography DB yet. Regenerate the review or run bibliography-update.",
        "unreviewed": "No review in the corpus. Run Review generation first.",
        "papers": "Papers",
        "summary": "{papers} paper(s) · {institutions} institution(s)",
        "not_normalized": ("This bibliography DB predates institution naming (no city column). "
                           "Run `python pipeline/normalize_institutions.py --apply` and reopen."),
        "show_authors": "{count} author(s)",
        "note": ("Names are ROR's official English names; an institution without "
                 "an umbrella is its own parent; city and country come from the "
                 "affiliation text when it states them, otherwise from ROR."),
    },
}


def connect(db: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(f"{db.resolve().as_uri()}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def has_city(conn: sqlite3.Connection) -> bool:
    return any(row[1] == "city_name"
               for row in conn.execute("PRAGMA table_info(institutions)"))


def collect(conn: sqlite3.Connection, slug: str, with_city: bool = True) -> dict | None:
    paper = conn.execute(
        "SELECT paper_id, slug, title, doi, publication_date, journal_name "
        "FROM papers WHERE slug=?", (slug,)).fetchone()
    if paper is None:
        return None
    pid = paper["paper_id"]
    city = "i.city_name" if with_city else "''"
    institutions = [dict(row) for row in conn.execute(
        "SELECT i.institution_id, i.institution_name AS institution, "
        f"i.parent_name AS parent, {city} AS city, "
        "i.country_name_en AS country, i.ror_id, pi.source "
        "FROM paper_institutions pi JOIN institutions i USING(institution_id) "
        "WHERE pi.paper_id=? ORDER BY i.institution_name", (pid,))]
    names = {row["institution_id"]: row["institution"] for row in institutions}
    links: dict[int, dict[str, set]] = {}
    for author_id, institution_id, source in conn.execute(
            "SELECT author_id, institution_id, source FROM paper_author_institutions "
            "WHERE paper_id=?", (pid,)):
        if institution_id in names:
            links.setdefault(author_id, {}).setdefault(source, set()).add(institution_id)
    authors = []
    for author_id, name, order in conn.execute(
            "SELECT a.author_id, a.display_name, pa.author_order FROM paper_authors pa "
            "JOIN authors a USING(author_id) WHERE pa.paper_id=? "
            "ORDER BY pa.author_order", (pid,)):
        by_source = links.get(author_id, {})
        stated = set().union(*(ids for source, ids in by_source.items()
                               if source != GUESSED_AUTHOR_SOURCE))
        authors.append({
            "order": order, "name": name,
            "institutions": sorted(names[i] for i in stated),
            "unknown": not stated and GUESSED_AUTHOR_SOURCE in by_source,
        })
    for row in institutions:
        del row["institution_id"]
    return {"status": "ok", "slug": paper["slug"], "title": paper["title"],
            "doi": paper["doi"], "date": paper["publication_date"],
            "journal": paper["journal_name"],
            "institutions": institutions, "authors": authors}


def _paper_section(info: dict, t: dict, labels: dict) -> str:
    e = html.escape
    if info["status"] != "ok":
        return (f"<section><h2>{e(info['title'])}</h2>"
                f"<p class=warn>{t[info['status']]}</p></section>")

    def ror(row: dict) -> str:
        if not row["ror_id"]:
            return e(row["institution"])
        return (f'<a href="{e(row["ror_id"])}" target="_blank" rel="noopener">'
                f'{e(row["institution"])}</a>')

    rows = "".join(
        f"<tr><td>{ror(row)}</td><td>{e(row['parent'])}</td><td>{e(row['city'])}</td>"
        f"<td>{e(row['country'])}</td>"
        f"<td class=src>{e(labels.get(row['source'], row['source']))}</td></tr>"
        for row in info["institutions"])
    table = (f"<table><thead><tr><th>{t['institution']}</th><th>{t['parent']}</th>"
             f"<th>{t['city']}</th><th>{t['country']}</th><th>{t['source']}</th></tr>"
             f"</thead><tbody>{rows}</tbody></table>"
             if info["institutions"] else f"<p class=empty>{t['no_institutions']}</p>")
    author_rows = "".join(
        f"<tr><td class=num>{a['order']}</td><td>{e(a['name'])}</td><td>"
        + ("; ".join(e(n) for n in a["institutions"]) if a["institutions"]
           else f"<span class=muted>{t['unknown'] if a['unknown'] else t['none']}</span>")
        + "</td></tr>"
        for a in info["authors"])
    authors = (f"<details><summary>{t['authors']} — "
               f"{t['show_authors'].format(count=len(info['authors']))}</summary>"
               f"<table><thead><tr><th class=num>#</th><th>{t['author']}</th>"
               f"<th>{t['institutions']}</th></tr></thead><tbody>{author_rows}"
               "</tbody></table></details>") if info["authors"] else ""
    meta = " · ".join(e(str(v)) for v in (info["journal"], info["date"]) if v)
    doi = (f' · <a href="https://doi.org/{e(info["doi"])}" target="_blank" '
           f'rel="noopener">{e(info["doi"])}</a>') if info["doi"] else ""
    return (f"<section><h2>{e(info['title'])}</h2><div class=meta>{meta}{doi}</div>"
            f"{table}{authors}</section>")


def render(papers: list[dict], lang: str, with_city: bool = True) -> str:
    t, labels = TEXT[lang], SOURCE_LABELS[lang]
    e = html.escape
    count = sum(len(p.get("institutions", [])) for p in papers)
    summary = t["summary"].format(papers=len(papers), institutions=count)
    warning = "" if with_city else f"<p class=warn>{e(t['not_normalized'])}</p>"
    sections = "".join(_paper_section(p, t, labels) for p in papers)
    title = papers[0]["title"] if len(papers) == 1 else summary
    return f"""<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t['title']} — {e(title)}</title>
<style>
:root{{color-scheme:light dark}}
body{{font:14px/1.5 -apple-system,BlinkMacSystemFont,"Apple SD Gothic Neo","Segoe UI",sans-serif;
margin:20px 24px;color:#1f2328;background:#fff}}
h1{{font-size:18px;margin:0 0 2px}} h2{{font-size:15px;margin:0 0 2px}}
section{{margin:0 0 26px}}
.summary,.meta{{color:#57606a;font-size:12px;margin-bottom:10px}}
table{{border-collapse:collapse;width:100%;font-size:13px;margin:6px 0}}
th,td{{text-align:left;padding:6px 9px;border:1px solid #d0d7de;vertical-align:top}}
th{{background:#f6f8fa;font-weight:600;position:sticky;top:0}}
tbody tr:nth-child(even) td{{background:#fafbfc}}
td.src,.muted,.empty{{color:#57606a}} .num{{width:2.5em;text-align:right}}
.warn{{background:#fff8c5;border:1px solid #d4a72c;padding:8px 10px;border-radius:6px}}
details summary{{cursor:pointer;color:#57606a;margin:8px 0 4px}}
.note{{color:#57606a;font-size:11px;margin-top:18px}}
a{{color:#0969da;text-decoration:none}} a:hover{{text-decoration:underline}}
@media (prefers-color-scheme:dark){{body{{background:#1e1e1e;color:#e6e6e6}}
th{{background:#2b2b2b}} th,td{{border-color:#444}}
tbody tr:nth-child(even) td{{background:#242424}} a{{color:#58a6ff}}
.warn{{background:#3b2f00;border-color:#9e7a00}}}}
</style></head><body>
<h1>{t['title']}</h1>
<div class=summary>{e(summary)}</div>
{warning}
{sections}
<p class=note>{t['note']}</p>
</body></html>
"""


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--paper", action="append", default=[], metavar="SLUG",
                    help="a reviewed paper's corpus slug (repeatable)")
    ap.add_argument("--unreviewed", action="append", default=[], metavar="TITLE",
                    help="a selected paper with no review in the corpus (repeatable)")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--lang", choices=sorted(TEXT), default="ko")
    args = ap.parse_args(argv)

    def receipt(**fields) -> int:
        print(json.dumps({"schema_version": 1, **fields}, ensure_ascii=False))
        return 0 if fields.get("ok") else 1

    if not args.paper and not args.unreviewed:
        return receipt(ok=False, reason="no-papers")
    if not args.db.is_file():
        return receipt(ok=False, reason="no-db", db=str(args.db))
    papers: list[dict] = []
    try:
        conn = connect(args.db)
        try:
            with_city = has_city(conn)
            for slug in args.paper:
                found = collect(conn, slug, with_city)
                papers.append(found or {"status": "not_ingested", "slug": slug,
                                        "title": _title_of(slug)})
        finally:
            conn.close()
    except sqlite3.Error as exc:
        return receipt(ok=False, reason="db-error", detail=str(exc)[:200])
    papers += [{"status": "unreviewed", "title": title} for title in args.unreviewed]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(render(papers, args.lang, with_city), encoding="utf-8")
    return receipt(
        ok=True, report=str(args.out), papers=len(papers),
        shown=sum(p["status"] == "ok" for p in papers),
        not_ingested=sum(p["status"] == "not_ingested" for p in papers),
        unreviewed=len(args.unreviewed), normalized=with_city,
        institutions=sum(len(p.get("institutions", [])) for p in papers))


def _title_of(slug: str) -> str:
    """The title the corpus index holds for a slug the DB does not know yet."""
    try:
        entries = json.loads((ROOT / "docs" / "papers" / "_papers_index.json")
                             .read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return slug
    for entry in entries if isinstance(entries, list) else []:
        if isinstance(entry, dict) and entry.get("slug") == slug:
            return str(entry.get("title") or slug)
    return slug


if __name__ == "__main__":
    sys.exit(main())
