#!/usr/bin/env python3
"""One paper's research institutions, as the bibliography DB holds them.

Paper Curio's "View Research Institute Info" runs this for the selected paper:
each institution with its parent, city, country, ROR record and source, and
each author with the institutions the byline ties them to. The page is a
self-contained HTML file; the last stdout line is a JSON receipt.

    python pipeline/institution_info.py --slug 042_Some_Paper --out /tmp/x.html

Read-only: the DB is opened with ``mode=ro``. A paper the DB does not hold yet
is reported as ``not-ingested``, not rendered as a paper without institutions.
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
        "note": ("Names are ROR's official English names; an institution without "
                 "an umbrella is its own parent; city and country come from the "
                 "affiliation text when it states them, otherwise from ROR."),
    },
}


def connect(db: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(f"{db.resolve().as_uri()}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def collect(conn: sqlite3.Connection, slug: str) -> dict | None:
    paper = conn.execute(
        "SELECT paper_id, slug, title, doi, publication_date, journal_name "
        "FROM papers WHERE slug=?", (slug,)).fetchone()
    if paper is None:
        return None
    pid = paper["paper_id"]
    institutions = [dict(row) for row in conn.execute(
        "SELECT i.institution_id, i.institution_name AS institution, "
        "i.parent_name AS parent, i.city_name AS city, "
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
    return {"slug": paper["slug"], "title": paper["title"], "doi": paper["doi"],
            "date": paper["publication_date"], "journal": paper["journal_name"],
            "institutions": institutions, "authors": authors}


def render(info: dict, lang: str) -> str:
    t, labels = TEXT[lang], SOURCE_LABELS[lang]
    e = html.escape

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
        f"<tr><td>{a['order']}</td><td>{e(a['name'])}</td><td>"
        + ("; ".join(e(n) for n in a["institutions"]) if a["institutions"]
           else f"<span class=muted>{t['unknown'] if a['unknown'] else t['none']}</span>")
        + "</td></tr>"
        for a in info["authors"])
    authors = (f"<h2>{t['authors']}</h2><table><thead><tr><th>#</th><th>{t['author']}"
               f"</th><th>{t['institutions']}</th></tr></thead><tbody>{author_rows}"
               "</tbody></table>") if info["authors"] else ""
    meta = " · ".join(e(str(v)) for v in (info["journal"], info["date"]) if v)
    doi = (f' · <a href="https://doi.org/{e(info["doi"])}" target="_blank" '
           f'rel="noopener">{e(info["doi"])}</a>') if info["doi"] else ""
    return f"""<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t['title']} — {e(info['title'])}</title>
<style>
body{{font:15px/1.55 -apple-system,BlinkMacSystemFont,"Apple SD Gothic Neo","Segoe UI",sans-serif;
max-width:1040px;margin:32px auto;padding:0 20px;color:#1f2328}}
h1{{font-size:22px;margin:0 0 4px}} h2{{font-size:17px;margin:28px 0 8px}}
.kicker{{color:#57606a;font-size:13px;text-transform:uppercase;letter-spacing:.04em}}
.meta{{color:#57606a;font-size:13px;margin-bottom:18px}}
table{{border-collapse:collapse;width:100%;font-size:14px}}
th,td{{text-align:left;padding:7px 10px;border-bottom:1px solid #d0d7de;vertical-align:top}}
th{{background:#f6f8fa;font-weight:600}} td.src,.muted{{color:#57606a}}
.empty{{color:#57606a}} .note{{color:#57606a;font-size:12px;margin-top:22px}}
a{{color:#0969da;text-decoration:none}} a:hover{{text-decoration:underline}}
</style></head><body>
<div class=kicker>{t['title']}</div>
<h1>{e(info['title'])}</h1>
<div class=meta>{meta}{doi}</div>
<h2>{t['institutions']}</h2>
{table}
{authors}
<p class=note>{t['note']}</p>
</body></html>
"""


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--slug", required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--lang", choices=sorted(TEXT), default="ko")
    args = ap.parse_args(argv)

    def receipt(**fields) -> int:
        print(json.dumps({"schema_version": 1, "slug": args.slug, **fields},
                         ensure_ascii=False))
        return 0 if fields.get("ok") else 1

    if not args.db.is_file():
        return receipt(ok=False, reason="no-db", db=str(args.db))
    try:
        conn = connect(args.db)
        try:
            info = collect(conn, args.slug)
        finally:
            conn.close()
    except sqlite3.Error as exc:
        return receipt(ok=False, reason="db-error", detail=str(exc)[:200])
    if info is None:
        return receipt(ok=False, reason="not-ingested")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(render(info, args.lang), encoding="utf-8")
    return receipt(ok=True, report=str(args.out),
                   institutions=len(info["institutions"]),
                   authors=len(info["authors"]))


if __name__ == "__main__":
    sys.exit(main())
