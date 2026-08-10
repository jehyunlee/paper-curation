#!/usr/bin/env python3
"""Top-N institution report for one topic: timelines, parallel labs, notable authors.

Built from `.cache/bibliography.sqlite3` (ROR-normalised institutions, authors,
journals, DOIs) joined with the topic's `_new_classification.json` for research
categories. Two outputs, same content:

    reports/source/{topic}_institutions_top{n}.md    (Obsidian)
    reports/build/{topic}_institutions_top{n}.html   (self-contained, printable)

Research groups are derived from author overlap, not from time: papers that share
at least one author land in the same connected component, so two components are
two labs and are presented side by side rather than as one chronology. Notable
researchers are ranked by output at that institution, with Nature/Science/Cell
family publications flagged separately.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sqlite3
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent))

try:
    from _env_guard import force_py312
except ImportError:  # pragma: no cover
    def force_py312():
        return None

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / ".cache" / "bibliography.sqlite3"
PAPERS_DIR = ROOT / "docs" / "papers"
SOURCE_DIR = ROOT / "reports" / "source"
BUILD_DIR = ROOT / "reports" / "build"

# "science, nature, cell 에 논문을 내는 연구자" — the three families the operator
# named, plus the sibling titles that carry the same brand.
# Springer Nature brands every "Nature X" title, so a prefix match is right
# there. AAAS and Cell Press do not: "Science in Context" (Cambridge UP) and
# "Science Editor and Publisher" are unrelated journals that a bare "Science "
# prefix would have promoted, so those two families are enumerated.
PRESTIGE = re.compile(
    r"(?i)^(?:"
    r"nature(?:\s|$|\s*\()|nature\s+[\w&:\-]+"
    r"|science(?:\s*\(|$)"
    r"|science\s+(?:advances|robotics|immunology|signaling|"
    r"translational\s+medicine)\b"
    r"|cell(?:\s*\(|$)"
    r"|cell\s+(?:reports|systems|metabolism|chemical\s+biology|"
    r"host\s*&?\s*microbe|stem\s+cell|genomics)\b"
    r"|(?:cancer|molecular|developmental|structural)\s+cell\b"
    r"|neuron(?:\s|$)|immunity(?:\s|$)"
    r")")

CATEGORY_KO = {
    "AI-Driven Drug and Materials Discovery": "신약·신소재 발견",
    "LLM Benchmarking and Agent Evaluation": "LLM·에이전트 평가",
    "Scientific AI for Physics and Environment": "물리·환경 과학 AI",
    "Molecular Simulation and Generative Modeling": "분자 시뮬레이션·생성 모델링",
    "Agentic AI for Scientific Automation": "과학 자동화 에이전트",
    "Formal Methods and Computational Reasoning": "형식 방법론·계산 추론",
    "Scientific Information Extraction and QA": "과학 정보추출·QA",
    "AI-Assisted Academic Scholarly Communication": "AI 지원 학술 커뮤니케이션",
}


def year_of(value: str) -> str:
    match = re.match(r"(\d{4})", str(value or ""))
    return match.group(1) if match else "연도미상"


def load_topic_slugs(topic: str) -> set[str]:
    index = json.loads(
        (PAPERS_DIR / "_papers_index.json").read_text(encoding="utf-8"))
    return {p["slug"] for p in index if topic in (p.get("topics") or [])}


def load_categories(topic: str) -> dict[str, tuple[str, str]]:
    path = ROOT / "docs" / topic / "_new_classification.json"
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {a["slug"]: (a.get("primary_category", ""), a.get("sub_category", ""))
            for a in data.get("assignments", [])}


def review_link(slug: str) -> str | None:
    """Local review page for a slug, matched the way the topic index does."""
    if (PAPERS_DIR / slug / "index.html").exists():
        return f"../../docs/papers/{slug}/index.html"
    prefix = slug.split("_")[0]
    for candidate in sorted(PAPERS_DIR.glob(f"{prefix}_*")):
        if (candidate / "index.html").exists():
            return f"../../docs/papers/{candidate.name}/index.html"
    return None


def fetch(topic: str, top: int) -> tuple[list[dict], dict]:
    conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    conn.execute("CREATE TEMP TABLE t(slug TEXT PRIMARY KEY)")
    conn.executemany("INSERT OR IGNORE INTO t VALUES (?)",
                     [(s,) for s in load_topic_slugs(topic)])
    ranked = conn.execute(
        "SELECT i.institution_id, i.institution_name, i.country_name_en,"
        " i.hq_country_name_en, i.parent_name, i.ror_id,"
        " COUNT(DISTINCT p.paper_id) k"
        " FROM t JOIN papers p ON p.slug=t.slug"
        " JOIN paper_institutions pi ON pi.paper_id=p.paper_id"
        " JOIN institutions i ON i.institution_id=pi.institution_id"
        " GROUP BY i.institution_id ORDER BY k DESC, i.institution_name"
        " LIMIT ?", (top,)).fetchall()
    categories = load_categories(topic)
    institutions = []
    for iid, name, country, hq, parent, ror, count in ranked:
        papers = []
        for row in conn.execute(
                "SELECT p.paper_id, p.slug, p.title, p.publication_date,"
                " p.journal_name, p.doi, p.url, p.arxiv_id"
                " FROM t JOIN papers p ON p.slug=t.slug"
                " JOIN paper_institutions pi ON pi.paper_id=p.paper_id"
                " WHERE pi.institution_id=?"
                " ORDER BY p.publication_date DESC, p.title", (iid,)):
            pid, slug, title, pdate, journal, doi, url, arxiv = row
            authors = [a for (a,) in conn.execute(
                "SELECT a.display_name FROM paper_authors pa"
                " JOIN authors a ON a.author_id=pa.author_id"
                " WHERE pa.paper_id=? ORDER BY pa.author_order", (pid,))]
            primary, sub = categories.get(slug, ("", ""))
            papers.append({
                "slug": slug, "title": title or slug,
                "date": pdate or "", "year": year_of(pdate),
                "journal": journal or "", "doi": doi or "",
                "url": url or "", "arxiv": arxiv or "",
                "authors": authors, "category": primary, "sub": sub,
                "prestige": bool(PRESTIGE.match(journal or "")),
                "link": review_link(slug),
                "figure": figure_for(slug),
            })
        institutions.append({
            "name": name, "country": country, "hq": hq, "parent": parent,
            "ror": ror, "count": count, "papers": papers})
    meta = {
        "topic": topic,
        "papers": len(load_topic_slugs(topic)),
        "generated": date.today().isoformat(),
    }
    conn.close()
    return institutions, meta


def figure_for(slug: str) -> str | None:
    """Figure 1 of a paper, as a path relative to reports/build."""
    directory = PAPERS_DIR / slug
    if not directory.exists():
        prefix = slug.split("_")[0]
        matches = sorted(PAPERS_DIR.glob(f"{prefix}_*"))
        directory = matches[0] if matches else None
    if directory is None:
        return None
    for name in ("fig1.webp", "fig1.png"):
        if (directory / "figures" / name).exists():
            return f"../../docs/papers/{directory.name}/figures/{name}"
    return None


def label_authors(names: list[str]) -> str:
    return ", ".join(names[:3]) + (" 외" if len(names) > 3 else "")


def group_by_authors(papers: list[dict]) -> list[dict]:
    """Connected components over shared authorship — one component, one lab.

    Deliberately independent of time: two components running in the same years
    are two groups, and the report shows them in parallel instead of merging
    their papers into a single misleading chronology.
    """
    parent = list(range(len(papers)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    by_author = defaultdict(list)
    for idx, paper in enumerate(papers):
        for author in paper["authors"]:
            by_author[author].append(idx)
    for indices in by_author.values():
        for other in indices[1:]:
            union(indices[0], other)

    buckets = defaultdict(list)
    for idx in range(len(papers)):
        buckets[find(idx)].append(papers[idx])

    groups = []
    for members in buckets.values():
        authors = Counter(a for p in members for a in p["authors"])
        cats = Counter(p["category"] for p in members if p["category"])
        years = sorted({p["year"] for p in members if p["year"] != "연도미상"})
        groups.append({
            "papers": sorted(members, key=lambda p: (p["date"], p["title"])),
            "size": len(members),
            "authors": [a for a, _ in authors.most_common(6)],
            "category": cats.most_common(1)[0][0] if cats else "",
            "span": f"{years[0]}–{years[-1]}" if len(years) > 1 else
                    (years[0] if years else "연도미상"),
            "prestige": sum(1 for p in members if p["prestige"]),
        })
    return sorted(groups, key=lambda g: (-g["size"], g["span"]))


def notable_authors(papers: list[dict], limit: int = 8) -> list[dict]:
    counts, prestige, topics, titles = Counter(), Counter(), defaultdict(Counter), defaultdict(list)
    for paper in papers:
        for author in paper["authors"]:
            counts[author] += 1
            if paper["prestige"]:
                prestige[author] += 1
                titles[author].append(paper)
            if paper["category"]:
                topics[author][paper["category"]] += 1
            if paper["sub"]:
                topics[author][paper["sub"]] += 1
    ranked = sorted(counts.items(), key=lambda kv: (-prestige[kv[0]], -kv[1], kv[0]))
    out = []
    for author, total in ranked[:limit]:
        if total < 2 and not prestige[author]:
            continue
        out.append({
            "name": author, "papers": total, "prestige": prestige[author],
            "topics": [t for t, _ in topics[author].most_common(3)],
            "venues": sorted({p["journal"] for p in titles[author]})[:3],
        })
    return out


def narrative(inst: dict, groups: list[dict]) -> str:
    """One paragraph describing the institution's research flow.

    Assembled from measured quantities only — year counts, the split between the
    early and late halves of activity, the largest author component, and the
    Nature/Science/Cell papers. Nothing is inferred beyond what the numbers say,
    so the prose cannot drift away from the tables next to it.
    """
    papers = [p for p in inst["papers"] if p["year"] != "연도미상"]
    if not papers:
        return "연도 정보가 있는 논문이 없어 흐름을 서술할 수 없다."
    years = sorted(p["year"] for p in papers)
    first, last = years[0], years[-1]
    per_year = Counter(years)
    peak, peak_n = per_year.most_common(1)[0]

    def top_cats(subset, n=2):
        counter = Counter(CATEGORY_KO.get(p["category"], p["category"])
                          for p in subset if p["category"])
        return [c for c, _ in counter.most_common(n)]

    midpoint = str((int(first) + int(last)) // 2) if first != last else first
    early = [p for p in papers if p["year"] <= midpoint]
    late = [p for p in papers if p["year"] > midpoint]

    bits = [f"{first}년부터 {last}년까지 {len(inst['papers'])}편이 확인되고, "
            f"{peak}년 {peak_n}편으로 정점을 찍는다."]
    if early and late:
        before, after = top_cats(early), top_cats(late)
        gained = [c for c in after if c not in before]
        if gained:
            bits.append(f"{midpoint}년 이전에는 {', '.join(before) or '분류미상'} "
                        f"중심이었는데 이후 {', '.join(gained)}가 전면에 나온다.")
        elif before and after and before[0] == after[0]:
            bits.append(f"기간 내내 {before[0]}가 축을 유지한다.")
        elif after:
            bits.append(f"후반부는 {', '.join(after)}로 무게가 옮겨간다.")
    else:
        cats = top_cats(papers)
        if cats:
            bits.append(f"주제는 {', '.join(cats)}에 몰려 있다.")

    multi = [g for g in groups if g["size"] > 1]
    if multi:
        big = multi[0]
        field = CATEGORY_KO.get(big["category"], big["category"]) or "분류미상"
        bits.append(f"저자가 겹치는 묶음은 {len(multi)}개이고, 가장 큰 것은 "
                    f"{label_authors(big['authors'])}의 "
                    f"{big['size']}편({big['span']}, {field})이다.")
        if len(multi) > 1:
            others = ", ".join(f"{g['authors'][0]} {g['size']}편"
                               for g in multi[1:4] if g["authors"])
            if others:
                bits.append(f"저자가 겹치지 않는 별도 묶음으로 {others}이 "
                            "병렬로 돌아간다.")
    singles = len(groups) - len(multi)
    if singles > len(inst["papers"]) * 0.5:
        bits.append(f"다만 {singles}편은 저자가 전혀 겹치지 않아, 소수 대형 랩보다 "
                    "여러 연구자가 산발적으로 참여하는 형태에 가깝다.")

    stars = [p for p in inst["papers"] if p["prestige"]]
    if stars:
        head = sorted(stars, key=lambda p: p["year"], reverse=True)[0]
        bits.append(f"Nature/Science/Cell 계열은 {len(stars)}편이고, 가장 최근은 "
                    f"{head['year']}년 《{head['journal']}》의 "
                    f"「{head['title']}」다.")
    else:
        bits.append("Nature/Science/Cell 계열 게재는 없고 프리프린트·학회 위주다.")
    return " ".join(bits)


def timeline_svg(inst: dict) -> str:
    """Stacked bars: papers per year, split by research category."""
    papers = [p for p in inst["papers"] if p["year"] != "연도미상"]
    if not papers:
        return ""
    years = sorted({p["year"] for p in papers})
    cats = [c for c, _ in Counter(
        CATEGORY_KO.get(p["category"], p["category"]) or "분류미상"
        for p in papers).most_common(6)]
    palette = ["#D63423", "#2374D6", "#0F9D58", "#F4A322", "#7B4FB5",
               "#00A3A3", "#9CA3AF"]
    colour = {c: palette[i] for i, c in enumerate(cats)}
    colour["기타"] = palette[6]

    counts = {y: Counter() for y in years}
    for paper in papers:
        label = CATEGORY_KO.get(paper["category"], paper["category"]) or "분류미상"
        counts[paper["year"]][label if label in colour else "기타"] += 1
    tallest = max(sum(c.values()) for c in counts.values()) or 1

    pad_l, pad_b, top, height = 34, 26, 16, 150
    bar, gap = 40, 14
    width = pad_l + len(years) * (bar + gap) + 10
    out = [f'<svg class="tl" viewBox="0 0 {width} {height + top + pad_b}" '
           'role="img" aria-label="연도별 논문 수">']
    for frac, label in ((0, "0"), (0.5, str(tallest // 2)), (1, str(tallest))):
        y = top + height - frac * height
        out.append(f'<line x1="{pad_l}" y1="{y:.1f}" x2="{width - 6}" '
                   f'y2="{y:.1f}" stroke="#e5e7eb" stroke-width="1"/>')
        out.append(f'<text x="{pad_l - 6}" y="{y + 3:.1f}" text-anchor="end" '
                   f'font-size="9" fill="#9ca3af">{label}</text>')
    for i, year in enumerate(years):
        x = pad_l + i * (bar + gap)
        cursor = top + height
        total = sum(counts[year].values())
        for label in colour:
            n = counts[year].get(label, 0)
            if not n:
                continue
            h = n / tallest * height
            cursor -= h
            out.append(f'<rect x="{x}" y="{cursor:.1f}" width="{bar}" '
                       f'height="{h:.1f}" fill="{colour[label]}" rx="1.5"/>')
        out.append(f'<text x="{x + bar / 2}" y="{cursor - 4:.1f}" '
                   'text-anchor="middle" font-size="9.5" fill="#374151" '
                   f'font-weight="600">{total}</text>')
        out.append(f'<text x="{x + bar / 2}" y="{top + height + 15}" '
                   f'text-anchor="middle" font-size="10" fill="#6b7280">{year}</text>')
    out.append("</svg>")
    legend = " ".join(
        f'<span class="key"><i style="background:{colour[c]}"></i>'
        f'{html.escape(c)}</span>' for c in cats)
    return "".join(out) + f'<div class="legend">{legend}</div>'


def showcase(inst: dict, limit: int = 3) -> list[dict]:
    """Representative papers with a figure: prestige first, then most recent."""
    withfig = [p for p in inst["papers"] if p["figure"]]
    return sorted(withfig, key=lambda p: (
        -int(p["prestige"]),
        -int(p["year"]) if p["year"].isdigit() else 0))[:limit]


def citation(paper: dict) -> str:
    bits = []
    if paper["authors"]:
        first = paper["authors"][0]
        bits.append(f"{first} 외" if len(paper["authors"]) > 1 else first)
    if paper["year"] != "연도미상":
        bits.append(f"({paper['year']})")
    bits.append(paper["title"])
    if paper["journal"]:
        bits.append(f"*{paper['journal']}*")
    return " ".join(bits)


def href(paper: dict) -> str:
    if paper["doi"]:
        return f"https://doi.org/{paper['doi']}"
    if paper["arxiv"]:
        return f"https://arxiv.org/abs/{paper['arxiv']}"
    return paper["url"] or paper["link"] or ""


def render_markdown(institutions: list[dict], meta: dict) -> str:
    L = [f"# AI4S 상위 {len(institutions)}개 기관 분석",
         "",
         f"- 코퍼스: `{meta['topic']}` {meta['papers']:,}편 · 생성 {meta['generated']}",
         "- 기관명은 ROR v2.11 정규화 기준. **지사**는 소속 문자열의 소재지, "
         "**본사**는 ROR 조상 체인의 최상위 국가.",
         "- 연구그룹은 **저자 공유(연결 성분)** 로 나눴다. 저자가 겹치지 않으면 다른 "
         "연구실로 보고 시간 흐름과 무관하게 **병렬로** 배치했다.",
         "- 주요 연구자는 기관 내 논문 수 순이며, "
         "**Nature/Science/Cell 계열** 게재를 별도 표시했다.",
         ""]
    L += ["## 순위 요약", "",
          "| # | 기관 | 지사 | 본사 | 상위그룹 | 편수 | 활동기간 |",
          "|---|---|---|---|---|---|---|"]
    for rank, inst in enumerate(institutions, 1):
        years = sorted({p["year"] for p in inst["papers"]
                        if p["year"] != "연도미상"})
        span = f"{years[0]}–{years[-1]}" if len(years) > 1 else (years[0] if years else "—")
        L.append(f"| {rank} | {inst['name']} | {inst['country'] or '—'} | "
                 f"{inst['hq'] or '—'} | {inst['parent'] or '—'} | "
                 f"{inst['count']} | {span} |")
    L.append("")

    for rank, inst in enumerate(institutions, 1):
        L += ["---", "", f"## {rank}. {inst['name']} ({inst['count']}편)", ""]
        facts = [f"**지사** {inst['country'] or '미확인'}",
                 f"**본사** {inst['hq'] or '미확인'}"]
        if inst["parent"]:
            facts.append(f"**상위그룹** {inst['parent']}")
        if inst["ror"]:
            facts.append(f"[ROR]({inst['ror']})")
        L += [" · ".join(facts), ""]

        groups_md = group_by_authors(inst["papers"])
        L += ["### 연구 흐름", "", narrative(inst, groups_md), ""]
        shots = showcase(inst)
        if shots:
            L += ["대표 도판:", ""]
            for paper in shots:
                star = " ⭐" if paper["prestige"] else ""
                L.append(f"![{paper['title'][:60]}]({paper['figure']})")
                L.append(f"*{paper['year']} · {paper['title']}"
                         f"{(' · ' + paper['journal']) if paper['journal'] else ''}"
                         f"{star}*")
                L.append("")

        by_year = defaultdict(list)
        for paper in inst["papers"]:
            by_year[paper["year"]].append(paper)
        L += ["### 연도별 주제 흐름", ""]
        for year in sorted(by_year, reverse=True):
            group = by_year[year]
            cats = Counter(CATEGORY_KO.get(p["category"], p["category"])
                           for p in group if p["category"])
            headline = ", ".join(f"{c} {n}" for c, n in cats.most_common(3)) or "분류미상"
            L.append(f"**{year}** ({len(group)}편) — {headline}")
            for paper in sorted(group, key=lambda p: p["title"]):
                mark = " ⭐" if paper["prestige"] else ""
                venue = f" · *{paper['journal']}*" if paper["journal"] else ""
                L.append(f"- {paper['title']}{venue}{mark}")
            L.append("")

        groups = group_by_authors(inst["papers"])
        multi = [g for g in groups if g["size"] > 1]
        L += ["### 연구그룹 (저자 공유 기준 · 병렬)", ""]
        if multi:
            L += ["| 그룹 | 편수 | 기간 | 주 분야 | 핵심 저자 |",
                  "|---|---|---|---|---|"]
            for idx, grp in enumerate(multi[:8], 1):
                star = f" ⭐{grp['prestige']}" if grp["prestige"] else ""
                L.append(f"| G{idx} | {grp['size']}{star} | {grp['span']} | "
                         f"{CATEGORY_KO.get(grp['category'], grp['category']) or '—'} | "
                         f"{label_authors(grp['authors'])} |")
            L.append("")
            singles = len(groups) - len(multi)
            if singles:
                L += [f"그 외 단독 논문 {singles}건은 저자가 겹치지 않아 독립 그룹으로 "
                      "집계했다.", ""]
        else:
            L += ["저자가 겹치는 논문 묶음이 없다 — 모두 독립 그룹이다.", ""]

        people = notable_authors(inst["papers"])
        L += ["### 주요 연구자", ""]
        if people:
            L += ["| 연구자 | 편수 | N/S/C | 연구주제 |", "|---|---|---|---|"]
            for person in people:
                venues = f" ({', '.join(person['venues'])})" if person["venues"] else ""
                L.append(f"| {person['name']} | {person['papers']} | "
                         f"{person['prestige'] or '—'}{venues} | "
                         f"{', '.join(person['topics']) or '—'} |")
            L.append("")
        else:
            L += ["이 기관에서 2편 이상 낸 저자가 없다 — 단발 참여로만 등장한다.", ""]

        L += ["### 레퍼런스", ""]
        for paper in sorted(inst["papers"],
                            key=lambda p: (p["year"], p["title"]), reverse=True):
            link, url = paper["link"], href(paper)
            text = citation(paper)
            if url:
                text = f"[{text}]({url})"
            if link:
                text += f" · [리뷰]({link})"
            L.append(f"1. {text}")
        L.append("")
    return "\n".join(L)


def render_html(institutions: list[dict], meta: dict) -> str:
    e = html.escape

    def esc(value):
        return e(str(value or ""))

    parts = [
        "<!doctype html><html lang=\"ko\"><head><meta charset=\"utf-8\">",
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">",
        f"<title>AI4S 상위 {len(institutions)}개 기관 분석</title>",
        "<style>",
        ":root{--ink:#1a1a1a;--mute:#6b7280;--line:#e5e7eb;--accent:#D63423;",
        "--bg:#fff;--soft:#f9fafb}",
        "*{box-sizing:border-box}",
        "body{margin:0;font:16px/1.75 -apple-system,BlinkMacSystemFont,",
        "'Pretendard','Apple SD Gothic Neo','Segoe UI',sans-serif;color:var(--ink);",
        "background:var(--bg)}",
        ".wrap{max-width:980px;margin:0 auto;padding:48px 28px 96px}",
        "h1{font-size:30px;letter-spacing:-.02em;margin:0 0 8px;line-height:1.3}",
        "h2{font-size:22px;margin:0 0 4px;letter-spacing:-.01em}",
        "h3{font-size:15px;text-transform:uppercase;letter-spacing:.08em;",
        "color:var(--mute);margin:32px 0 12px;font-weight:600}",
        ".lede{color:var(--mute);font-size:14.5px;margin:0 0 32px}",
        ".lede li{margin:3px 0}",
        "table{border-collapse:collapse;width:100%;font-size:14px;margin:0 0 8px}",
        "th,td{border-bottom:1px solid var(--line);padding:8px 10px;",
        "text-align:left;vertical-align:top}",
        "th{background:var(--soft);font-weight:600;font-size:13px;color:#374151;",
        "white-space:nowrap}",
        "td.num,th.num{text-align:right;font-variant-numeric:tabular-nums;",
        "white-space:nowrap}",
        "section.inst{border-top:3px solid var(--accent);margin:56px 0 0;",
        "padding-top:20px;page-break-before:always}",
        "section.inst:first-of-type{page-break-before:avoid}",
        ".rank{display:inline-block;min-width:30px;color:var(--accent);",
        "font-weight:700}",
        ".facts{font-size:13.5px;color:var(--mute);margin:2px 0 0}",
        ".facts b{color:var(--ink);font-weight:600}",
        ".yr{margin:0 0 14px}",
        ".yr>.hd{font-weight:600;font-size:14.5px}",
        ".yr>.hd .cats{color:var(--mute);font-weight:400}",
        ".yr ul{margin:5px 0 0;padding-left:20px;font-size:14px}",
        ".yr li{margin:2px 0}",
        ".venue{color:var(--mute);font-style:italic}",
        ".star{color:#b45309;font-weight:700}",
        "ol.refs{font-size:13px;color:#374151;padding-left:22px;margin:0}",
        "ol.refs li{margin:4px 0}",
        "a{color:#1d4ed8;text-decoration:none}a:hover{text-decoration:underline}",
        ".note{font-size:13px;color:var(--mute);margin:6px 0 0}",
        ".story{font-size:15px;line-height:1.85;margin:0 0 16px;",
        "padding:14px 16px;background:var(--soft);border-left:3px solid",
        " var(--accent);border-radius:0 4px 4px 0}",
        ".chart{margin:0 0 6px;overflow-x:auto}",
        "svg.tl{max-width:100%;height:auto;display:block}",
        ".legend{font-size:11.5px;color:var(--mute);margin:0 0 18px;",
        "display:flex;flex-wrap:wrap;gap:4px 14px}",
        ".key{display:inline-flex;align-items:center;gap:5px;white-space:nowrap}",
        ".key i{width:10px;height:10px;border-radius:2px;display:inline-block}",
        ".gallery{display:grid;grid-template-columns:repeat(auto-fit,",
        "minmax(190px,1fr));gap:14px;margin:0 0 8px}",
        ".gallery figure{margin:0}",
        ".gallery img{width:100%;height:132px;object-fit:cover;",
        "border:1px solid var(--line);border-radius:4px;background:#fff}",
        ".gallery figcaption{font-size:11.5px;color:var(--mute);",
        "line-height:1.45;margin-top:5px}",
        "@media print{.wrap{padding:0 12px}a{color:var(--ink)}",
        ".gallery img{height:110px}",
        "section.inst{border-top-width:2px}}",
        "</style></head><body><div class=\"wrap\">",
        f"<h1>AI4S 상위 {len(institutions)}개 기관 분석</h1>",
        "<ul class=\"lede\">",
        f"<li>코퍼스 <b>{meta['papers']:,}편</b> · 생성 {esc(meta['generated'])}</li>",
        "<li>기관명은 <b>ROR v2.11</b> 정규화 기준. <b>지사</b>는 소속 문자열의 "
        "소재지, <b>본사</b>는 ROR 조상 체인 최상위 국가.</li>",
        "<li>연구그룹은 <b>저자 공유(연결 성분)</b> 로 분리했다. 저자가 겹치지 "
        "않으면 다른 연구실로 보고 시간과 무관하게 <b>병렬</b> 배치.</li>",
        "<li><span class=\"star\">⭐</span> = Nature/Science/Cell 계열 게재.</li>",
        "</ul>",
    ]

    parts += ["<h3>순위 요약</h3><table><thead><tr><th class=\"num\">#</th>",
              "<th>기관</th><th>지사</th><th>본사</th><th>상위그룹</th>",
              "<th class=\"num\">편수</th><th>활동기간</th></tr></thead><tbody>"]
    for rank, inst in enumerate(institutions, 1):
        years = sorted({p["year"] for p in inst["papers"] if p["year"] != "연도미상"})
        span = f"{years[0]}–{years[-1]}" if len(years) > 1 else (years[0] if years else "—")
        parts.append(
            f"<tr><td class=\"num\">{rank}</td>"
            f"<td><a href=\"#inst{rank}\">{esc(inst['name'])}</a></td>"
            f"<td>{esc(inst['country'] or '—')}</td>"
            f"<td>{esc(inst['hq'] or '—')}</td>"
            f"<td>{esc(inst['parent'] or '—')}</td>"
            f"<td class=\"num\">{inst['count']}</td><td>{esc(span)}</td></tr>")
    parts.append("</tbody></table>")

    for rank, inst in enumerate(institutions, 1):
        parts += [f"<section class=\"inst\" id=\"inst{rank}\">",
                  f"<h2><span class=\"rank\">{rank}.</span> {esc(inst['name'])} "
                  f"<span class=\"venue\">{inst['count']}편</span></h2>"]
        facts = [f"<b>지사</b> {esc(inst['country'] or '미확인')}",
                 f"<b>본사</b> {esc(inst['hq'] or '미확인')}"]
        if inst["parent"]:
            facts.append(f"<b>상위그룹</b> {esc(inst['parent'])}")
        if inst["ror"]:
            facts.append(f"<a href=\"{esc(inst['ror'])}\">ROR</a>")
        parts.append(f"<p class=\"facts\">{' · '.join(facts)}</p>")

        groups_html = group_by_authors(inst["papers"])
        parts += ["<h3>연구 흐름</h3>",
                  f"<p class=\"story\">{esc(narrative(inst, groups_html))}</p>",
                  f"<div class=\"chart\">{timeline_svg(inst)}</div>"]
        shots = showcase(inst)
        if shots:
            parts.append("<div class=\"gallery\">")
            for paper in shots:
                url = href(paper) or paper["link"] or "#"
                star = " <span class=\"star\">⭐</span>" if paper["prestige"] else ""
                venue = f" · {esc(paper['journal'])}" if paper["journal"] else ""
                parts.append(
                    f"<figure><a href=\"{esc(url)}\">"
                    f"<img loading=\"lazy\" src=\"{esc(paper['figure'])}\" "
                    f"alt=\"{esc(paper['title'][:80])}\"></a>"
                    f"<figcaption>{esc(paper['year'])}{venue}{star}<br>"
                    f"{esc(paper['title'][:90])}</figcaption></figure>")
            parts.append("</div>")

        by_year = defaultdict(list)
        for paper in inst["papers"]:
            by_year[paper["year"]].append(paper)
        parts.append("<h3>연도별 주제 흐름</h3>")
        for year in sorted(by_year, reverse=True):
            group = by_year[year]
            cats = Counter(CATEGORY_KO.get(p["category"], p["category"])
                           for p in group if p["category"])
            headline = ", ".join(f"{c} {n}" for c, n in cats.most_common(3)) or "분류미상"
            parts.append(
                f"<div class=\"yr\"><div class=\"hd\">{esc(year)} "
                f"<span class=\"cats\">({len(group)}편) — {esc(headline)}</span>"
                "</div><ul>")
            for paper in sorted(group, key=lambda p: p["title"]):
                url = href(paper)
                title = esc(paper["title"])
                if url:
                    title = f"<a href=\"{esc(url)}\">{title}</a>"
                venue = (f" <span class=\"venue\">· {esc(paper['journal'])}</span>"
                         if paper["journal"] else "")
                star = " <span class=\"star\">⭐</span>" if paper["prestige"] else ""
                parts.append(f"<li>{title}{venue}{star}</li>")
            parts.append("</ul></div>")

        groups = group_by_authors(inst["papers"])
        multi = [g for g in groups if g["size"] > 1]
        parts.append("<h3>연구그룹 · 저자 공유 기준 (병렬)</h3>")
        if multi:
            parts += ["<table><thead><tr><th>그룹</th><th class=\"num\">편수</th>",
                      "<th>기간</th><th>주 분야</th><th>핵심 저자</th></tr>",
                      "</thead><tbody>"]
            for idx, grp in enumerate(multi[:8], 1):
                star = (f" <span class=\"star\">⭐{grp['prestige']}</span>"
                        if grp["prestige"] else "")
                parts.append(
                    f"<tr><td>G{idx}</td><td class=\"num\">{grp['size']}{star}</td>"
                    f"<td>{esc(grp['span'])}</td>"
                    f"<td>{esc(CATEGORY_KO.get(grp['category'], grp['category']) or '—')}</td>"
                    f"<td>{esc(label_authors(grp['authors']))}</td></tr>")
            parts.append("</tbody></table>")
            singles = len(groups) - len(multi)
            if singles:
                parts.append(f"<p class=\"note\">그 외 단독 논문 {singles}건은 저자가 "
                             "겹치지 않아 독립 그룹으로 집계했다.</p>")
        else:
            parts.append("<p class=\"note\">저자가 겹치는 논문 묶음이 없다 — "
                         "모두 독립 그룹이다.</p>")

        people = notable_authors(inst["papers"])
        parts.append("<h3>주요 연구자</h3>")
        if people:
            parts += ["<table><thead><tr><th>연구자</th><th class=\"num\">편수</th>",
                      "<th>N/S/C</th><th>연구주제</th></tr></thead><tbody>"]
            for person in people:
                venues = (f" <span class=\"venue\">({esc(', '.join(person['venues']))})</span>"
                          if person["venues"] else "")
                nsc = (f"<span class=\"star\">{person['prestige']}</span>{venues}"
                       if person["prestige"] else "—")
                parts.append(
                    f"<tr><td>{esc(person['name'])}</td>"
                    f"<td class=\"num\">{person['papers']}</td><td>{nsc}</td>"
                    f"<td>{esc(', '.join(person['topics']) or '—')}</td></tr>")
            parts.append("</tbody></table>")
        else:
            parts.append("<p class=\"note\">이 기관에서 2편 이상 낸 저자가 없다.</p>")

        parts.append("<h3>레퍼런스</h3><ol class=\"refs\">")
        for paper in sorted(inst["papers"],
                            key=lambda p: (p["year"], p["title"]), reverse=True):
            url, link = href(paper), paper["link"]
            text = esc(citation(paper))
            if url:
                text = f"<a href=\"{esc(url)}\">{text}</a>"
            if link:
                text += f" · <a href=\"{esc(link)}\">리뷰</a>"
            parts.append(f"<li>{text}</li>")
        parts += ["</ol>", "</section>"]

    parts.append("</div></body></html>")
    return "\n".join(parts)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", default="ai4s")
    parser.add_argument("--top", type=int, default=15)
    args = parser.parse_args()

    if not DB_PATH.exists():
        print(f"bibliography DB 없음: {DB_PATH}", file=sys.stderr)
        return 2
    institutions, meta = fetch(args.topic, args.top)
    if not institutions:
        print("해당 토픽 기관이 없음", file=sys.stderr)
        return 3

    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    stem = f"{args.topic}_institutions_top{args.top}"
    md_path = SOURCE_DIR / f"{stem}.md"
    html_path = BUILD_DIR / f"{stem}.html"
    md_path.write_text(render_markdown(institutions, meta), encoding="utf-8")
    html_path.write_text(render_html(institutions, meta), encoding="utf-8")

    print(json.dumps({
        "topic": args.topic,
        "institutions": len(institutions),
        "papers_covered": sum(i["count"] for i in institutions),
        "md": str(md_path), "html": str(html_path),
        "md_bytes": md_path.stat().st_size,
        "html_bytes": html_path.stat().st_size,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    force_py312()
    raise SystemExit(main())
