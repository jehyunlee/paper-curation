#!/usr/bin/env python3
"""Schematic of the bibliography DB and everything it is wired to.

The diagram is drawn from the live database, not from a picture kept in sync by
hand: tables, columns, row counts and foreign keys are read out of
`.cache/bibliography.sqlite3` at build time, so a schema change shows up here
without anyone remembering to redraw it. The surrounding boxes — Zotero, the
Zotero PDFs, `docs/papers/`, the ROR index, the curated group table and the
downstream pages — are declared below because they are pipeline structure
rather than schema, and each arrow names the module that actually moves the
data.

    python pipeline/build_schema_diagram.py            # ai4s
    python pipeline/build_schema_diagram.py --db PATH  # another database
"""
from __future__ import annotations

import argparse
import html
import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"
BUILD_DIR = ROOT / "reports" / "build"
SOURCE_DIR = ROOT / "reports" / "source"

# Where each table's rows come from. Kept next to the drawing because "which
# upstream writes this" is the question the diagram exists to answer.
ORIGIN = {
    "papers": "Zotero record (ground truth) + Scopus/PDF gap-fill",
    "authors": "Zotero creators → review.md frontmatter → index",
    "paper_authors": "authorship order, first/corresponding flags",
    "institutions": "ROR v2.11 normalised identity",
    "paper_institutions": "Scopus FULL + PDF front matter",
    "institution_aliases": "raw affiliation strings seen in PDFs",
    "institution_groups": "legacy grouping — superseded by parent_name",
    "source_documents": "review.md / text.md content hashes",
    "citation_snapshots": "OpenAlex · Crossref · Scopus (run_metrics)",
    "citation_yearly": "per-year citation counts (run_metrics)",
}

# Columns worth showing. The rest are collapsed into a "+N more" line so the
# boxes stay readable.
HIGHLIGHT = {
    "papers": ["paper_id", "slug", "title", "doi", "zotero_item_key",
               "journal_name", "publication_date", "bibliography_source"],
    "authors": ["author_id", "display_name", "normalized_name"],
    "paper_authors": ["paper_id", "author_id", "author_order",
                      "is_first_author", "is_corresponding_author"],
    "institutions": ["institution_id", "institution_name", "ror_id",
                     "country_name_en", "hq_country_name_en", "parent_name",
                     "name_source"],
    "paper_institutions": ["paper_id", "institution_id", "raw_name",
                           "country_name", "source"],
    "institution_aliases": ["alias_id", "raw_name", "normalized_alias",
                            "institution_id"],
    "source_documents": ["paper_id", "document_type", "path", "sha256"],
    "citation_snapshots": ["paper_id", "observed_date", "openalex_count",
                           "scopus_count", "normalized_percentile"],
    "citation_yearly": ["paper_id", "citation_year", "citation_count"],
    "institution_groups": ["group_id", "group_name"],
}

CORE = ("papers", "authors", "paper_authors", "institutions",
        "paper_institutions", "institution_aliases")


def inspect(db: Path) -> dict:
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    try:
        tables = [r[0] for r in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' "
            "AND name NOT LIKE 'sqlite_%' ORDER BY name")]
        out = {}
        for table in tables:
            cols = [(r[1], r[2], bool(r[5]))
                    for r in conn.execute(f"PRAGMA table_info({table})")]
            fks = [(r[3], r[2], r[4])
                   for r in conn.execute(f"PRAGMA foreign_key_list({table})")]
            count = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            out[table] = {"columns": cols, "fks": fks, "rows": count}
        facts = {}
        for label, sql in (
                ("affiliation_source",
                 "SELECT source, COUNT(*) FROM paper_institutions GROUP BY 1"),
                ("bibliography_source",
                 "SELECT bibliography_source, COUNT(*) FROM papers GROUP BY 1"),
                ("document_type",
                 "SELECT document_type, COUNT(*) FROM source_documents GROUP BY 1")):
            try:
                facts[label] = dict(conn.execute(sql))
            except sqlite3.Error:
                facts[label] = {}
        facts["ror_resolved"] = conn.execute(
            "SELECT COUNT(*) FROM institutions WHERE ror_id<>''").fetchone()[0]
        facts["parent_groups"] = conn.execute(
            "SELECT COUNT(DISTINCT parent_name) FROM institutions "
            "WHERE parent_name<>''").fetchone()[0]
        return {"tables": out, "facts": facts}
    finally:
        conn.close()


def markdown(schema: dict, db: Path) -> str:
    tables, facts = schema["tables"], schema["facts"]
    L = ["# Bibliography DB — 구조와 연결",
         "",
         f"`{db.relative_to(ROOT)}` · 테이블 {len(tables)}개 · "
         f"논문 {tables['papers']['rows']:,}편",
         "",
         "## 파이프라인 위치", "",
         "```",
         "  Zotero Web API            Zotero PDF 디렉토리",
         "  (서지 참값)                (6,009개 로컬 캐시)",
         "        │                          │",
         "        └────────┬─────────────────┘",
         "                 ▼",
         "     run_update_force.py  ── 리뷰 생성 (concurrency 16)",
         "                 │",
         "                 ├─▶ docs/papers/{slug}/text.md      PDF 본문",
         "                 ├─▶ docs/papers/{slug}/review.md    한글 리뷰",
         "                 ├─▶ docs/papers/{slug}/figures/     도판",
         "                 └─▶ docs/papers/{slug}/bibliography.json",
         "                          ↑ 사이드카: Zotero 레코드 + 저자 +",
         "                            ROR 정규화 기관 (리뷰 시점 포착)",
         "                 │",
         "                 ▼  단일 ingest 스레드 (배치 8편)",
         "        .cache/bibliography.sqlite3   ← 이 문서의 대상",
         "                 │",
         "                 ├─ check_bibliography_db.py --strict   게이트",
         "                 └─ sync_bibliography_db.py --push      Mac mini",
         "```",
         "",
         "## 외부 권위 자료", "",
         "| 자료 | 역할 | 위치 |",
         "|---|---|---|",
         "| **Zotero** | 서지 **참값**. 출판사 전사본이라 Scopus·PDF보다 우선 | Web API + 사이드카 |",
         "| **ROR v2.11** | 기관 신원. 다국어·약칭·법인형 변이를 하나로 병합 | `.cache/ror/ror_index.sqlite3` (135,710 조직) |",
         "| **큐레이션 그룹표** | ROR이 빠뜨린 상위관계 보정 | `pipeline/data/dict_afgroupname_confident.json` |",
         "| **Scopus** | 소속·서지 **빈칸만** 채움 | `.cache/scopus_affiliations.json` |",
         "| **OpenAlex/Crossref** | 피인용수 | `run_metrics.py` |",
         "",
         "## 테이블", ""]

    for name in list(CORE) + [t for t in tables if t not in CORE]:
        info = tables.get(name)
        if info is None:
            continue
        L.append(f"### `{name}` — {info['rows']:,}행")
        L.append("")
        L.append(f"출처: {ORIGIN.get(name, '—')}")
        L.append("")
        shown = HIGHLIGHT.get(name, [c[0] for c in info["columns"]][:8])
        L.append("| 컬럼 | 타입 | |")
        L.append("|---|---|---|")
        by_name = {c[0]: c for c in info["columns"]}
        fk_by_col = {f[0]: (f[1], f[2]) for f in info["fks"]}
        for col in shown:
            if col not in by_name:
                continue
            _, ctype, pk = by_name[col]
            note = "PK" if pk else ""
            if col in fk_by_col:
                target, tcol = fk_by_col[col]
                note = f"FK → `{target}`"
            L.append(f"| `{col}` | {ctype or '—'} | {note} |")
        extra = len(info["columns"]) - len([c for c in shown if c in by_name])
        if extra > 0:
            L.append(f"| _+{extra}개 컬럼_ | | |")
        L.append("")

    L += ["## 출처 분포 (실측)", ""]
    for label, title in (("bibliography_source", "서지 출처 (papers)"),
                         ("affiliation_source", "소속 출처 (paper_institutions)"),
                         ("document_type", "원문 (source_documents)")):
        dist = facts.get(label) or {}
        if not dist:
            continue
        L.append(f"**{title}**")
        L.append("")
        for k, v in sorted(dist.items(), key=lambda kv: -kv[1]):
            L.append(f"- `{k or '(빈값)'}` — {v:,}")
        L.append("")
    L.append(f"기관 {tables['institutions']['rows']:,}개 중 ROR 해결 "
             f"{facts['ror_resolved']:,}개 · 상위그룹 {facts['parent_groups']}종")
    L.append("")
    return "\n".join(L)


# ── SVG ──────────────────────────────────────────────────────────────────
def esc(v):
    return html.escape(str(v), quote=True)


def box(x, y, w, h, title, subtitle, rows, fill, stroke, rowfill="#ffffff"):
    out = [f'<g><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" '
           f'fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>',
           f'<rect x="{x}" y="{y}" width="{w}" height="26" rx="7" fill="{stroke}"/>',
           f'<rect x="{x}" y="{y+18}" width="{w}" height="8" fill="{stroke}"/>',
           f'<text x="{x+10}" y="{y+18}" font-size="12.5" font-weight="700" '
           f'fill="#fff">{esc(title)}</text>']
    if subtitle:
        out.append(f'<text x="{x+w-10}" y="{y+18}" font-size="10.5" '
                   f'text-anchor="end" fill="#ffffffcc">{esc(subtitle)}</text>')
    cy = y + 42
    for label, note in rows:
        out.append(f'<text x="{x+11}" y="{cy}" font-size="10.8" '
                   f'fill="#1f2933">{esc(label)}</text>')
        if note:
            out.append(f'<text x="{x+w-11}" y="{cy}" font-size="9.6" '
                       f'text-anchor="end" fill="#7b8794">{esc(note)}</text>')
        cy += 15
    out.append("</g>")
    return "".join(out)


def arrow(x1, y1, x2, y2, label="", dash=False, colour="#52606d", bend=None):
    d = (f'M {x1} {y1} Q {bend[0]} {bend[1]} {x2} {y2}' if bend
         else f'M {x1} {y1} L {x2} {y2}')
    style = ' stroke-dasharray="5 4"' if dash else ""
    out = [f'<path d="{d}" fill="none" stroke="{colour}" stroke-width="1.6"'
           f'{style} marker-end="url(#arw)"/>']
    if label:
        mx = bend[0] if bend else (x1 + x2) / 2
        my = (bend[1] if bend else (y1 + y2) / 2) - 6
        out.append(f'<text x="{mx}" y="{my}" font-size="9.8" '
                   f'text-anchor="middle" fill="#52606d">'
                   f'<tspan class="lbl">{esc(label)}</tspan></text>')
    return "".join(out)


def svg(schema: dict) -> str:
    t = schema["tables"]
    f = schema["facts"]

    def rows_for(name, limit=7):
        info = t.get(name, {"columns": [], "fks": [], "rows": 0})
        fk = {x[0]: x[1] for x in info["fks"]}
        pk = {c[0] for c in info["columns"] if c[2]}
        out = []
        for col in HIGHLIGHT.get(name, [])[:limit]:
            note = "FK" if col in fk else ("PK" if col in pk else "")
            out.append((col, note))
        return out

    W, H = 1420, 1180
    P = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
         'font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,'
         'Apple SD Gothic Neo,sans-serif">' % (W, H),
         '<defs><marker id="arw" viewBox="0 0 10 10" refX="9" refY="5" '
         'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
         '<path d="M 0 0 L 10 5 L 0 10 z" fill="#52606d"/></marker></defs>',
         f'<rect width="{W}" height="{H}" fill="#fbfcfd"/>']

    # ── upstream authorities
    P.append('<text x="40" y="34" font-size="13.5" font-weight="700" '
             'fill="#1f2933">외부 권위 자료</text>')
    P.append(box(40, 48, 250, 92, "Zotero Web API", "서지 참값",
                 [("컬렉션 아이템 5,605건", ""),
                  ("creators · DOI · 저널 · 권호", ""),
                  ("출판사 전사본 → 최우선", "")],
                 "#fff5f4", "#D63423"))
    P.append(box(320, 48, 250, 92, "Zotero PDF", "로컬 캐시",
                 [("6,009개 · Google Drive", ""),
                  ("locate_pdf() 제목 토큰 매칭", ""),
                  ("앞 3p + author-info 뒷장", "")],
                 "#fff5f4", "#D63423"))
    P.append(box(600, 48, 250, 92, "ROR v2.11", "기관 신원",
                 [("조직 135,710 · 이름 448,550", ""),
                  ("다국어·약칭·법인형 병합", ""),
                  (".cache/ror/ror_index.sqlite3", "")],
                 "#f2f7fd", "#2374D6"))
    P.append(box(880, 48, 250, 92, "큐레이션 그룹표", "ROR 보정",
                 [("dict_afgroupname_confident", ""),
                  ("상위관계 2,679건", ""),
                  ("pipeline/data/ (저장소 고정)", "")],
                 "#f2f7fd", "#2374D6"))
    P.append(box(1160, 48, 220, 92, "Scopus · OpenAlex", "빈칸/피인용",
                 [("소속·서지 gap-fill", ""),
                  ("피인용수 3소스", ""),
                  ("Crossref 연차보정", "")],
                 "#f2f7fd", "#2374D6"))

    # ── review generation
    P.append(box(40, 196, 810, 108, "run_update_force.py",
                 "리뷰 생성 · concurrency 16",
                 [("PDF 매칭 → text.md 추출 → sanity gate → figure 추출", ""),
                  ("review.md 생성 (Claude) → 서지 추출 → HTML 변환", ""),
                  ("단일 ingest 스레드가 배치 8편씩 DB에 적재", "논블로킹")],
                 "#ffffff", "#0F9D58"))

    # ── per-paper assets
    P.append('<text x="900" y="192" font-size="13.5" font-weight="700" '
             'fill="#1f2933">논문별 자산 docs/papers/{slug}/</text>')
    P.append(box(900, 196, 480, 108, "기존 curation asset", "논문당 1디렉토리",
                 [("text.md — PDF 본문", "4,145"),
                  ("review.md — 한글 리뷰", "4,195"),
                  ("figures/*.webp — 도판", ""),
                  ("bibliography.json — 사이드카(신규)", "")],
                 "#fffdf5", "#F4A322"))

    # ── the DB
    P.append('<text x="40" y="352" font-size="13.5" font-weight="700" '
             f'fill="#1f2933">.cache/bibliography.sqlite3 — 테이블 {len(t)}개</text>')

    P.append(box(40, 368, 300, 160, "papers", f"{t['papers']['rows']:,}",
                 rows_for("papers", 7), "#ffffff", "#334e68"))
    P.append(box(40, 556, 300, 118, "source_documents",
                 f"{t['source_documents']['rows']:,}",
                 rows_for("source_documents", 4), "#ffffff", "#829ab1"))
    P.append(box(40, 700, 300, 118, "citation_snapshots",
                 f"{t['citation_snapshots']['rows']:,}",
                 rows_for("citation_snapshots", 4), "#ffffff", "#829ab1"))

    P.append(box(400, 368, 300, 118, "paper_authors",
                 f"{t['paper_authors']['rows']:,}",
                 rows_for("paper_authors", 5), "#ffffff", "#627d98"))
    P.append(box(400, 520, 300, 88, "authors", f"{t['authors']['rows']:,}",
                 rows_for("authors", 3), "#ffffff", "#627d98"))

    P.append(box(760, 368, 320, 118, "paper_institutions",
                 f"{t['paper_institutions']['rows']:,}",
                 rows_for("paper_institutions", 5), "#ffffff", "#627d98"))
    P.append(box(760, 520, 320, 160, "institutions",
                 f"{t['institutions']['rows']:,}",
                 rows_for("institutions", 7), "#ffffff", "#334e68"))
    P.append(box(760, 712, 320, 88, "institution_aliases",
                 f"{t['institution_aliases']['rows']:,}",
                 rows_for("institution_aliases", 3), "#ffffff", "#829ab1"))

    P.append(box(1120, 368, 260, 118, "institution_groups",
                 f"{t['institution_groups']['rows']:,}",
                 [("group_id", "PK"), ("group_name", ""),
                  ("legacy — parent_name 이 대체", "")],
                 "#f7f8f9", "#9aa5b1"))

    # ── relations
    P.append(arrow(340, 420, 400, 420, "paper_id"))
    P.append(arrow(550, 520, 550, 486, "author_id"))
    P.append(arrow(340, 440, 760, 440, "paper_id", bend=(550, 350)))
    P.append(arrow(920, 520, 920, 486, "institution_id"))
    P.append(arrow(920, 712, 920, 680, "institution_id"))
    P.append(arrow(190, 556, 190, 528, "paper_id"))
    P.append(arrow(190, 700, 190, 674, "paper_id"))
    P.append(arrow(1120, 430, 1080, 500, "group_id (미사용)", dash=True,
                   colour="#9aa5b1"))

    # ── feeds
    P.append(arrow(165, 140, 165, 196, "", colour="#D63423"))
    P.append(arrow(445, 140, 445, 196, "", colour="#D63423"))
    P.append(arrow(725, 140, 640, 196, "정규화", colour="#2374D6"))
    P.append(arrow(1005, 140, 760, 196, "상위그룹", colour="#2374D6"))
    P.append(arrow(1270, 140, 1140, 300, "gap-fill", colour="#2374D6",
                   bend=(1300, 240)))
    P.append(arrow(445, 304, 445, 368, "ingest (배치 8편)", colour="#0F9D58"))
    P.append(arrow(1140, 304, 1140, 340, "사이드카", colour="#F4A322"))
    P.append(arrow(1140, 340, 1000, 368, "", colour="#F4A322"))

    # ── downstream
    P.append('<text x="40" y="872" font-size="13.5" font-weight="700" '
             'fill="#1f2933">소비처</text>')
    P.append(box(40, 886, 300, 100, "check_bibliography_db.py", "게이트",
                 [("--strict: 논문수·고아·오염", ""),
                  ("ROR 커버리지 40% 하한", ""),
                  ("사이드카·큐레이션표 존재", "")],
                 "#ffffff", "#0F9D58"))
    P.append(box(380, 886, 300, 100, "sync_bibliography_db.py", "CAS 발행",
                 [("--pull / --push (SSH)", ""),
                  ("세대 = 다이제스트+Git rev", ""),
                  ("Mac mini 권위 호스트", "")],
                 "#ffffff", "#0F9D58"))
    P.append(box(720, 886, 300, 100, "build_institution_report.py", "리포트",
                 [("기관 타임라인·연구그룹", ""),
                  ("주요 연구자 · N/S/C", ""),
                  ("run_full --mode report", "")],
                 "#ffffff", "#7B4FB5"))
    P.append(box(1060, 886, 320, 100, "query_bibliography.py", "조회",
                 [("--institution / --country", ""),
                  ("--author / --sort date", ""),
                  ("pipeline.api", "")],
                 "#ffffff", "#7B4FB5"))
    for x in (190, 530, 870, 1220):
        P.append(arrow(x, 830, x, 886, "", colour="#829ab1", dash=True))

    # ── topic assets (not in the DB)
    P.append(box(40, 1024, 1340, 92, "토픽 자산 — DB 밖, 슬러그로 연결",
                 "docs/{topic}/",
                 [("_papers_index.json — 마스터 인덱스 (papers.slug 와 1:1, 개수 불일치 시 --strict 실패)", ""),
                  ("_new_classification.json — 8개 대분류 + 서브카테고리 배정 · _category_summaries.json", ""),
                  ("index.html · network.html · _search_index.json — DB 를 읽지 않고 인덱스에서 생성", "")],
                 "#fffdf5", "#F4A322"))
    P.append(arrow(700, 986, 700, 1024, "slug", colour="#F4A322", dash=True))

    P.append("</svg>")
    return "".join(P)


def render_html(schema: dict, db: Path) -> str:
    t = schema["tables"]
    f = schema["facts"]
    css = (
        "*{box-sizing:border-box}"
        "body{margin:0;background:#f6f7f9;color:#1f2933;"
        "font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,"
        "'Apple SD Gothic Neo',sans-serif;line-height:1.65}"
        ".wrap{max-width:1480px;margin:0 auto;padding:34px 24px 70px}"
        "h1{font-size:26px;margin:0 0 6px;letter-spacing:-.4px}"
        ".sub{color:#7b8794;font-size:13.5px;margin:0 0 26px}"
        ".card{background:#fff;border:1px solid #e4e7eb;border-radius:9px;"
        "padding:18px;margin:0 0 22px;overflow-x:auto}"
        "svg{display:block;min-width:1100px;max-width:100%;height:auto}"
        "h2{font-size:17px;margin:28px 0 12px;padding-bottom:7px;"
        "border-bottom:2px solid #D63423}"
        "table{border-collapse:collapse;width:100%;font-size:13px}"
        "th,td{border:1px solid #e4e7eb;padding:7px 10px;text-align:left;"
        "vertical-align:top}"
        "th{background:#f0f4f8;font-weight:600}"
        "code{background:#f0f4f8;padding:1px 5px;border-radius:3px;"
        "font-size:12px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}"
        ".n{text-align:right;font-variant-numeric:tabular-nums}"
        ".lbl{paint-order:stroke;stroke:#fbfcfd;stroke-width:3px}"
        "@media print{body{background:#fff}.card{break-inside:avoid}}"
    )
    parts = [f"<!DOCTYPE html><html lang=ko><head><meta charset=utf-8>"
             f"<meta name=viewport content='width=device-width,initial-scale=1'>"
             f"<title>Bibliography DB 구조</title><style>{css}</style></head><body>"
             "<div class=wrap>",
             "<h1>Bibliography DB — 구조와 연결</h1>",
             f"<p class=sub><code>{esc(db.relative_to(ROOT))}</code> · "
             f"테이블 {len(t)}개 · 논문 {t['papers']['rows']:,}편 · "
             f"기관 {t['institutions']['rows']:,}개 "
             f"(ROR 해결 {f['ror_resolved']:,} · 상위그룹 {f['parent_groups']}종)"
             " · 스키마는 실행 시점의 DB에서 직접 읽는다</p>",
             f"<div class=card>{svg(schema)}</div>"]

    parts.append("<h2>테이블</h2>")
    for name in list(CORE) + [x for x in t if x not in CORE]:
        info = t.get(name)
        if info is None:
            continue
        parts.append(f"<h3><code>{esc(name)}</code> — {info['rows']:,}행</h3>")
        parts.append(f"<p class=sub style='margin:-6px 0 8px'>"
                     f"{esc(ORIGIN.get(name, '—'))}</p>")
        fk = {x[0]: (x[1], x[2]) for x in info["fks"]}
        pk = {c[0] for c in info["columns"] if c[2]}
        parts.append("<table><tr><th>컬럼</th><th>타입</th><th>관계</th></tr>")
        shown = HIGHLIGHT.get(name, [c[0] for c in info["columns"]][:8])
        by = {c[0]: c for c in info["columns"]}
        for col in shown:
            if col not in by:
                continue
            note = ""
            if col in fk:
                note = f"FK → <code>{esc(fk[col][0])}</code>"
            elif col in pk:
                note = "PK"
            parts.append(f"<tr><td><code>{esc(col)}</code></td>"
                         f"<td>{esc(by[col][1] or '—')}</td><td>{note}</td></tr>")
        rest = len(info["columns"]) - len([c for c in shown if c in by])
        if rest > 0:
            parts.append(f"<tr><td colspan=3 style='color:#7b8794'>"
                         f"+{rest}개 컬럼</td></tr>")
        parts.append("</table>")

    parts.append("<h2>출처 분포 (실측)</h2><table>"
                 "<tr><th>구분</th><th>값</th><th class=n>건수</th></tr>")
    for label, title in (("bibliography_source", "서지 출처"),
                         ("affiliation_source", "소속 출처"),
                         ("document_type", "원문")):
        for k, v in sorted((f.get(label) or {}).items(), key=lambda kv: -kv[1]):
            parts.append(f"<tr><td>{esc(title)}</td>"
                         f"<td><code>{esc(k or '(빈값)')}</code></td>"
                         f"<td class=n>{v:,}</td></tr>")
    parts.append("</table></div></body></html>")
    return "".join(parts)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--stem", default="bibliography_schema")
    args = ap.parse_args()
    if not args.db.exists():
        print(f"DB 없음: {args.db}", file=sys.stderr)
        return 2
    schema = inspect(args.db)
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    md = SOURCE_DIR / f"{args.stem}.md"
    hp = BUILD_DIR / f"{args.stem}.html"
    md.write_text(markdown(schema, args.db), encoding="utf-8")
    hp.write_text(render_html(schema, args.db), encoding="utf-8")
    print(json.dumps({"tables": len(schema["tables"]),
                      "papers": schema["tables"]["papers"]["rows"],
                      "md": str(md), "html": str(hp),
                      "html_bytes": hp.stat().st_size}, ensure_ascii=False,
                     indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
