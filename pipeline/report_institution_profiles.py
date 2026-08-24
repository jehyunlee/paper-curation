#!/usr/bin/env python3
"""Per-institution profiles: output over time, who did what, and what to read.

`report_field_leaders.py` answers "which institutions are most active" with a
table. This answers the follow-up -- what that activity consists of -- with a
page per institution: a flat plot of papers per year, the researchers behind
them, and a one-line description of each researcher's work carrying superscript
references to the actual papers.

Two things this is careful about.

References are global and deduplicated by paper. Institutions co-author, so the
same paper backs a line under Stanford and a line under MIT; it is numbered
once and both cite that number. A reference list where the same paper appears
three times under three numbers is not a reference list.

Descriptions are written from the titles of the papers being cited and nothing
else. The model is given the researcher's own papers and asked to summarise
them; it is never asked what it knows about the person. A sentence that cannot
be checked against its own superscripts does not belong in a report whose
purpose is that its claims can be checked.

Usage:
    python pipeline/report_institution_profiles.py --topic ai4s --top 20
    python pipeline/report_institution_profiles.py --topic ai4s --no-llm
"""
from __future__ import annotations

import argparse
import html
import json
import os
import sqlite3
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "pipeline"
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

from lib.evidence import RESOLVED_SOURCES                      # noqa: E402

DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"
MODEL = "claude-sonnet-4-5-20250929"

LATEST_CITATIONS = """
  SELECT cs.paper_id,
         MAX(COALESCE(cs.openalex_count, 0), COALESCE(cs.crossref_count, 0),
             COALESCE(cs.scopus_count, 0)) AS citations
  FROM citation_snapshots cs
  JOIN (SELECT paper_id, MAX(observed_date) d FROM citation_snapshots
        GROUP BY paper_id) newest
    ON newest.paper_id = cs.paper_id AND newest.d = cs.observed_date
"""

TOPIC_PAPERS = """
  SELECT p.paper_id FROM papers p
  JOIN json_each(json_extract(p.metadata_json, '$.topics')) t
  WHERE t.value = ?
"""

# A year before this is a data error rather than a publication date -- one
# paper in the corpus carries 1929 -- and plotting it flattens everything else.
FIRST_YEAR = 2016


def institutions(conn, topic: str, top: int) -> list[dict]:
    """Ranked by papers whose *first author* sits at the institution.

    Counting every affiliation ranks by participation, which favours whoever
    joins the largest collaborations. Counting first authors ranks by where
    the work was led. 2,172 of ai4s's 2,663 papers (81.6%) name a first author
    whose institution is established on evidence; the rest are absent from the
    comparison rather than guessed at.
    """
    marks = ",".join("?" * len(RESOLVED_SOURCES))
    rows = conn.execute(f"""
      WITH topic_papers AS ({TOPIC_PAPERS}), cites AS ({LATEST_CITATIONS})
      SELECT i.institution_id, i.institution_name,
             COALESCE(i.country_name_en, '') country,
             COUNT(DISTINCT pa.paper_id) papers,
             COALESCE(SUM(ct.citations), 0) citations,
             COUNT(DISTINCT ct.paper_id) papers_with_citations
      FROM paper_authors pa
      JOIN topic_papers tp ON tp.paper_id = pa.paper_id
      JOIN (SELECT DISTINCT paper_id, author_id, institution_id
              FROM paper_author_institutions
             WHERE source IN ({marks})) pai
        ON pai.paper_id = pa.paper_id AND pai.author_id = pa.author_id
      JOIN institutions i ON i.institution_id = pai.institution_id
      LEFT JOIN cites ct ON ct.paper_id = pa.paper_id
      WHERE pa.is_first_author = 1
      GROUP BY i.institution_id
      ORDER BY papers DESC, i.institution_name
      LIMIT ?""", (topic, *RESOLVED_SOURCES, top)).fetchall()
    return [{"institution_id": r[0], "name": r[1], "country": r[2],
             "papers": r[3], "citations": r[4],
             "papers_with_citations": r[5]} for r in rows]


def yearly(conn, topic: str, institution_id: int) -> dict[int, int]:
    """Papers per year, on the same first-author basis as the ranking."""
    marks = ",".join("?" * len(RESOLVED_SOURCES))
    rows = conn.execute(f"""
      WITH topic_papers AS ({TOPIC_PAPERS})
      SELECT COALESCE(p.publication_date, ''), COUNT(DISTINCT p.paper_id)
      FROM paper_authors pa
      JOIN topic_papers tp ON tp.paper_id = pa.paper_id
      JOIN (SELECT DISTINCT paper_id, author_id, institution_id
              FROM paper_author_institutions
             WHERE source IN ({marks})) pai
        ON pai.paper_id = pa.paper_id AND pai.author_id = pa.author_id
      JOIN papers p ON p.paper_id = pa.paper_id
      WHERE pa.is_first_author = 1 AND pai.institution_id = ?
      GROUP BY 1""", (topic, *RESOLVED_SOURCES, institution_id)).fetchall()
    counts: Counter[int] = Counter()
    for date, n in rows:
        head = (date or "")[:4]
        if head.isdigit() and int(head) >= FIRST_YEAR:
            counts[int(head)] += n
    return dict(counts)


def researchers(conn, topic: str, institution_id: int, limit: int,
                papers_each: int) -> list[dict]:
    """Authors at this institution, with the papers that put them there."""
    marks = ",".join("?" * len(RESOLVED_SOURCES))
    rows = conn.execute(f"""
      WITH topic_papers AS ({TOPIC_PAPERS})
      SELECT a.author_id, a.display_name, COUNT(DISTINCT pai.paper_id) n
      FROM (SELECT DISTINCT paper_id, author_id, institution_id
              FROM paper_author_institutions
             WHERE source IN ({marks})) pai
      JOIN topic_papers tp ON tp.paper_id = pai.paper_id
      JOIN authors a ON a.author_id = pai.author_id
      WHERE pai.institution_id = ?
      GROUP BY a.author_id
      ORDER BY n DESC, a.display_name
      LIMIT ?""", (topic, *RESOLVED_SOURCES, institution_id, limit)).fetchall()
    out = []
    for author_id, name, n in rows:
        papers = conn.execute(f"""
          WITH topic_papers AS ({TOPIC_PAPERS})
          SELECT DISTINCT p.paper_id, p.title, COALESCE(p.publication_date,''),
                 p.slug, COALESCE(p.doi,'')
          FROM (SELECT DISTINCT paper_id, author_id, institution_id
                  FROM paper_author_institutions
                 WHERE source IN ({marks})) pai
          JOIN topic_papers tp ON tp.paper_id = pai.paper_id
          JOIN papers p ON p.paper_id = pai.paper_id
          WHERE pai.author_id = ? AND pai.institution_id = ?
          ORDER BY COALESCE(p.publication_date,'') DESC
          LIMIT ?""", (topic, *RESOLVED_SOURCES, author_id, institution_id,
                       papers_each)).fetchall()
        out.append({"author_id": author_id, "name": name, "papers_total": n,
                    "papers": [{"paper_id": r[0], "title": r[1],
                                "date": r[2], "slug": r[3], "doi": r[4]}
                               for r in papers]})
    return out


class References:
    """Global numbering, one number per paper however often it is cited."""

    def __init__(self) -> None:
        self._number: dict[int, int] = {}
        self._papers: list[dict] = []

    def cite(self, paper: dict) -> int:
        pid = paper["paper_id"]
        if pid not in self._number:
            self._number[pid] = len(self._papers) + 1
            self._papers.append(paper)
        return self._number[pid]

    @property
    def entries(self) -> list[dict]:
        return self._papers


def describe(profiles: list[dict], use_llm: bool) -> None:
    """One line per researcher, written from that researcher's own titles."""
    todo = [(inst, person) for inst in profiles
            for person in inst["researchers"] if person["papers"]]
    if not use_llm:
        for _inst, person in todo:
            person["description"] = person["papers"][0]["title"]
        return
    import anthropic
    client = anthropic.Anthropic(timeout=180.0, max_retries=4)
    batch = 25
    for start in range(0, len(todo), batch):
        chunk = todo[start:start + batch]
        listing = []
        for index, (inst, person) in enumerate(chunk, 1):
            titles = "\n".join(f"    - {p['title']}" for p in person["papers"])
            listing.append(
                f"{index}. {person['name']} ({inst['name']})\n{titles}")
        prompt = (
            "다음은 연구자별로 이 코퍼스에 있는 논문 제목이다. 각 연구자에 대해 "
            "그 제목들만 근거로 어떤 연구를 했는지 한국어 한 줄(공백 포함 45자 "
            "이내)로 요약하라. 제목에 없는 사실을 덧붙이지 말고, 소속·경력·"
            "수상 등 외부 지식을 쓰지 마라. 번호와 요약만 `N| 요약` 형식으로 "
            "한 줄씩 출력하라.\n\n" + "\n\n".join(listing))
        try:
            reply = client.messages.create(
                model=MODEL, max_tokens=2000,
                messages=[{"role": "user", "content": prompt}])
            text = reply.content[0].text if reply.content else ""
        except Exception as exc:                       # noqa: BLE001
            print(f"  [warn] 요약 실패: {exc}", file=sys.stderr)
            text = ""
        got: dict[int, str] = {}
        for line in text.splitlines():
            if "|" not in line:
                continue
            head, _, tail = line.partition("|")
            head = head.strip().rstrip(".")
            if head.isdigit():
                got[int(head)] = tail.strip()
        for index, (_inst, person) in enumerate(chunk, 1):
            person["description"] = got.get(index) or person["papers"][0]["title"]
        print(f"  [요약] {min(start + batch, len(todo))}/{len(todo)}",
              file=sys.stderr, flush=True)


def sparkline(counts: dict[int, int], years: list[int], peak: int,
              width: int = 500) -> str:
    """A 10:3 plot of papers per year, inline so the page stays one file.

    `years` and `peak` are passed in rather than taken from `counts`, so every
    institution is drawn on the same axes. Per-chart scaling made an
    institution with four papers look like one with fifty-seven, and put 2016
    under one chart's leftmost bar and 2023 under another's.
    """
    height = round(width * 3 / 10)
    if not years or not peak:
        return ""
    left, right, top, bottom = 34, 8, 10, 22
    plot_w = width - left - right
    plot_h = height - top - bottom
    step = plot_w / max(1, len(years))
    bar_w = max(2.0, step * 0.62)
    parts = [f'<svg viewBox="0 0 {width} {height}" width="100%" '
             f'preserveAspectRatio="xMidYMid meet" '
             f'role="img" aria-label="연도별 논문 수">']
    parts.append(f'<line x1="{left}" y1="{top + plot_h}" x2="{width - right}" '
                 f'y2="{top + plot_h}" stroke="#d8d2c8" stroke-width="1"/>')
    parts.append(f'<text x="{left - 6}" y="{top + 8}" font-size="10" '
                 f'fill="#8a8178" text-anchor="end">{peak}</text>')
    for index, year in enumerate(years):
        n = counts.get(year, 0)
        h = 0 if peak == 0 else plot_h * n / peak
        x = left + index * step + (step - bar_w) / 2
        y = top + plot_h - h
        if n:
            parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" '
                         f'height="{h:.1f}" fill="#D63423" rx="1"/>')
            parts.append(f'<text x="{x + bar_w / 2:.1f}" y="{y - 3:.1f}" '
                         f'font-size="9" fill="#6b635a" '
                         f'text-anchor="middle">{n}</text>')
        parts.append(f'<text x="{x + bar_w / 2:.1f}" y="{height - 2}" '
                     f'font-size="9" fill="#8a8178" text-anchor="middle">'
                     f'{str(year)[2:]}</text>')
    parts.append("</svg>")
    return "".join(parts)


def merge_coauthors(people: list[dict]) -> list[dict]:
    """Fold together researchers whose cited papers are the same set.

    Co-authors at one institution often appear with an identical paper list --
    Barzilay and Jaakkola, Mark and Pollard -- and giving each their own line
    printed the same sentence and the same superscripts twice. They are one
    piece of work by several people, so they get one line naming all of them.

    Only an exact match folds. Overlapping-but-different bodies of work stay
    apart, because summarising them together would describe neither.
    """
    grouped: dict[frozenset[int], dict] = {}
    order: list[frozenset[int]] = []
    for person in people:
        key = frozenset(p["paper_id"] for p in person["papers"])
        if not key:
            key = frozenset({-person["author_id"]})
        if key not in grouped:
            grouped[key] = dict(person, names=[person["name"]])
            order.append(key)
            continue
        held = grouped[key]
        held["names"].append(person["name"])
        held["papers_total"] = max(held["papers_total"], person["papers_total"])
    out = []
    for key in order:
        person = grouped[key]
        person["name"] = " · ".join(person["names"])
        out.append(person)
    return out


def overview_chart(profiles: list[dict], width: int = 900) -> str:
    """Institutions down the middle, papers to the right, citations to the left.

    The two sides count different things, so each is scaled to its own maximum
    and labelled with its own unit. A shared scale would be meaningless -- the
    largest citation total is three orders of magnitude above the largest
    paper count -- and a reader who assumed one was shared would conclude that
    MIT published sixty-five thousand papers.

    The citation side is drawn dimmer on purpose. Citations are collected for
    only part of the corpus and unevenly -- Oxford has them for 20 of its 44
    papers, MIT for 34 of 43 -- so the left bars compare coverage as much as
    impact.
    """
    if not profiles:
        return ""
    row_h, top, bottom, gutter = 22, 34, 26, 200
    # The value sits outside its bar, so the longest one -- "264,991" -- needs
    # room or it renders past the edge of the picture.
    pad = 62
    height = top + bottom + row_h * len(profiles)
    side = (width - gutter) / 2 - pad
    left_edge, right_edge = pad + side, pad + side + gutter
    max_papers = max(p["papers"] for p in profiles) or 1
    max_cites = max(p["citations"] for p in profiles) or 1

    out = [f'<svg viewBox="0 0 {width} {height}" width="100%" '
           f'preserveAspectRatio="xMidYMid meet" role="img" '
           f'aria-label="기관별 논문 수와 총 피인용 수">']
    out.append(f'<text x="{right_edge + 4}" y="16" font-size="12" '
               f'fill="#D63423" font-weight="600">논문 편수 &#8594;</text>')
    out.append(f'<text x="{left_edge - 4}" y="16" font-size="12" '
               f'fill="#8a8178" font-weight="600" text-anchor="end">'
               f'&#8592; 총 피인용 수</text>')
    out.append(f'<text x="{right_edge + 4}" y="{height - 8}" font-size="10" '
               f'fill="#8a8178">최대 {max_papers}편</text>')
    out.append(f'<text x="{left_edge - 4}" y="{height - 8}" font-size="10" '
               f'fill="#8a8178" text-anchor="end">최대 {max_cites:,}회 '
               f'· 두 축은 서로 독립</text>')

    for index, inst in enumerate(profiles):
        y = top + index * row_h
        mid = y + row_h / 2
        name = inst["name"]
        if len(name) > 27:
            name = name[:26] + "\u2026"
        out.append(f'<text x="{width / 2}" y="{mid + 4}" font-size="11" '
                   f'fill="#2b2723" text-anchor="middle">'
                   f'{html.escape(name)}</text>')
        pw = side * inst["papers"] / max_papers
        out.append(f'<rect x="{right_edge}" y="{y + 4}" width="{pw:.1f}" '
                   f'height="{row_h - 8}" fill="#D63423" rx="2"/>')
        out.append(f'<text x="{right_edge + pw + 4:.1f}" y="{mid + 4}" '
                   f'font-size="10" fill="#6b635a">{inst["papers"]}</text>')
        cw = side * inst["citations"] / max_cites
        out.append(f'<rect x="{left_edge - cw:.1f}" y="{y + 4}" '
                   f'width="{cw:.1f}" height="{row_h - 8}" fill="#b9b0a4" '
                   f'rx="2"/>')
        out.append(f'<text x="{left_edge - cw - 4:.1f}" y="{mid + 4}" '
                   f'font-size="10" fill="#8a8178" text-anchor="end">'
                   f'{inst["citations"]:,}</text>')
    out.append("</svg>")
    return "".join(out)


def build(conn, topic: str, top: int, per_institution: int,
          papers_each: int, use_llm: bool) -> dict:
    profiles = institutions(conn, topic, top)
    for inst in profiles:
        inst["yearly"] = yearly(conn, topic, inst["institution_id"])
        inst["researchers"] = merge_coauthors(researchers(
            conn, topic, inst["institution_id"], per_institution, papers_each))
    describe(profiles, use_llm)

    refs = References()
    for inst in profiles:
        for person in inst["researchers"]:
            person["refs"] = [refs.cite(p) for p in person["papers"]]

    # One axis for every chart, so the bars can be compared across sections.
    all_years = [y for inst in profiles for y in inst["yearly"]]
    axis = list(range(min(all_years), max(all_years) + 1)) if all_years else []
    peak = max((n for inst in profiles for n in inst["yearly"].values()),
               default=0)
    total = conn.execute(
        f"SELECT COUNT(*) FROM ({TOPIC_PAPERS})", (topic,)).fetchone()[0]
    return {"topic": topic, "papers": total, "profiles": profiles,
            "references": refs.entries, "axis": axis, "peak": peak}


def render_html(data: dict) -> str:
    esc = html.escape
    out = [
        "<!doctype html><html lang=\"ko\"><head><meta charset=\"utf-8\">",
        f"<title>{esc(data['topic'])} — 기관 프로파일</title>",
        "<style>",
        "body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',"
        "'Noto Sans KR',sans-serif;max-width:860px;margin:0 auto;padding:40px 24px;"
        "color:#2b2723;background:#faf8f5;line-height:1.7}",
        "h1{font-size:26px;margin:0 0 4px}",
        "h2{font-size:19px;margin:44px 0 2px;padding-top:18px;"
        "border-top:1px solid #e6e0d6}",
        ".meta{color:#8a8178;font-size:13px;margin:0 0 10px}",
        ".chart{margin:6px 0 14px}",
        "ul{padding-left:18px;margin:8px 0}",
        "li{margin:5px 0}",
        ".who{font-weight:600}",
        "sup{font-size:10px;color:#D63423;font-weight:600}",
        ".refs{font-size:13px;color:#4a443d}",
        ".refs li{margin:3px 0}",
        "a{color:#D63423;text-decoration:none}a:hover{text-decoration:underline}",
        "</style></head><body>",
        f"<h1>{esc(data['topic'])} — 가장 활발한 기관 "
        f"{len(data['profiles'])}곳</h1>",
        f"<p class=\"meta\">대상 논문 {data['papers']:,}편 · "
        f"막대는 연도별 편수 · 위첨자는 맨 뒤 참고문헌 번호</p>",
        f"<div class=\"chart\">{overview_chart(data['profiles'])}</div>",
        "<p class=\"meta\">오른쪽은 주저자 소속 기준 논문 편수, 왼쪽은 그 "
        "논문들의 총 피인용 수입니다. 단위가 다르므로 두 축은 각각 자기 "
        "최대값으로 따로 조정됩니다. 피인용은 코퍼스의 일부에서만 수집되었고 "
        "기관마다 수집률이 달라, 왼쪽 막대는 영향력만큼이나 수집 범위를 "
        "반영합니다.</p>",
    ]
    for rank, inst in enumerate(data["profiles"], 1):
        out.append(f"<h2>{rank}. {esc(inst['name'])}</h2>")
        out.append(
            f"<p class=\"meta\">{esc(inst['country'] or '국가 미상')} · "
            f"논문 {inst['papers']}편 · 피인용 {inst['citations']:,}회 "
            f"({inst['papers_with_citations']}/{inst['papers']}편에서 수집)"
            f"</p>")
        out.append(f"<div class=\"chart\">"
                   f"{sparkline(inst['yearly'], data['axis'], data['peak'])}"
                   f"</div>")
        out.append("<ul>")
        for person in inst["researchers"]:
            # The superscript is the only route from a claim to its
            # evidence, so it has to be clickable rather than decorative.
            sups = "".join(
                f'<sup><a href="#ref-{n}">{n}</a></sup>'
                for n in person.get("refs", []))
            out.append(
                f"<li><span class=\"who\">{esc(person['name'])}</span>"
                f"({person['papers_total']}편) — "
                f"{esc(person.get('description') or '')}{sups}</li>")
        out.append("</ul>")

    out.append("<h2>참고문헌</h2>")
    out.append("<p class=\"meta\">공저 논문은 한 번호를 여러 기관이 함께 "
               "인용합니다.</p><ol class=\"refs\">")
    for index, paper in enumerate(data["references"], 1):
        year = (paper["date"] or "")[:4]
        link = f"papers/{paper['slug']}/index.html"
        doi = (f" doi:<a href=\"https://doi.org/{esc(paper['doi'])}\">"
               f"{esc(paper['doi'])}</a>" if paper["doi"] else "")
        out.append(f"<li id=\"ref-{index}\">"
                   f"<a href=\"{esc(link)}\">{esc(paper['title'])}</a>"
                   f"{' (' + year + ')' if year else ''}{doi}</li>")
    out.append("</ol></body></html>")
    return "\n".join(out)


def render_markdown(data: dict) -> str:
    out = [f"# {data['topic']} — 가장 활발한 기관 {len(data['profiles'])}곳",
           "",
           f"- 대상 논문 **{data['papers']:,}편**",
           "- 위첨자 번호는 맨 뒤 참고문헌을 가리키며, 공저 논문은 여러 기관이 "
           "같은 번호를 인용합니다.", "",
           "|순위|기관|국가|논문|총 피인용|피인용 수집|",
           "|---:|---|---|---:|---:|---:|"]
    for rank, inst in enumerate(data["profiles"], 1):
        out.append(f"|{rank}|{inst['name']}|{inst['country'] or '-'}|"
                   f"{inst['papers']}|{inst['citations']:,}|"
                   f"{inst['papers_with_citations']}/{inst['papers']}|")
    out.append("")
    for rank, inst in enumerate(data["profiles"], 1):
        out += [f"## {rank}. {inst['name']}", "",
                f"{inst['country'] or '국가 미상'} · 논문 {inst['papers']}편 · "
                f"피인용 {inst['citations']:,}회 "
                f"({inst['papers_with_citations']}/{inst['papers']}편 수집)", ""]
        years = data["axis"]
        if years:
            head = " | ".join(str(y) for y in years)
            body = " | ".join(str(inst["yearly"].get(y, 0)) for y in years)
            out += [f"|{head}|", "|" + "|".join(["---:"] * len(years)) + "|",
                    f"|{body}|", ""]
        for person in inst["researchers"]:
            sups = "".join(f"[{n}]" for n in person.get("refs", []))
            out.append(f"- **{person['name']}**({person['papers_total']}편) — "
                       f"{person.get('description') or ''}{sups}")
        out.append("")
    out += ["## 참고문헌", ""]
    for index, paper in enumerate(data["references"], 1):
        year = (paper["date"] or "")[:4]
        out.append(f"{index}. {paper['title']}"
                   f"{' (' + year + ')' if year else ''}"
                   f"{' doi:' + paper['doi'] if paper['doi'] else ''}")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--topic", default="ai4s")
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--researchers", type=int, default=6)
    ap.add_argument("--papers-each", type=int, default=3)
    ap.add_argument("--no-llm", action="store_true",
                    help="skip the one-line summaries and print a title")
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()

    conn = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True)
    try:
        data = build(conn, args.topic, args.top, args.researchers,
                     args.papers_each, not args.no_llm)
    finally:
        conn.close()

    out = args.out or (ROOT / "reports" / "build"
                       / f"{args.topic}_institution_profiles.html")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_html(data), encoding="utf-8")
    md = out.with_suffix(".md")
    md.write_text(render_markdown(data), encoding="utf-8")
    print(json.dumps({
        "html": str(out), "markdown": str(md),
        "institutions": len(data["profiles"]),
        "researchers": sum(len(i["researchers"]) for i in data["profiles"]),
        "references": len(data["references"]),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
