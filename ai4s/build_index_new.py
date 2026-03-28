"""
Build index.html for ai4s paper curation using new MECE classification.
Run with: PYTHONUTF8=1 python build_index_new.py
"""
import json, os, re
from html import escape
from collections import defaultdict

BASE = "C:/Users/jehyu/Arbeitplatz/paper-curation/ai4s"

with open(f"{BASE}/_new_classification.json", encoding="utf-8") as f:
    cls_data = json.load(f)
with open(f"{BASE}/_timeline_narrative.json", encoding="utf-8") as f:
    narrative = json.load(f)
with open(f"{BASE}/_all_papers.json", encoding="utf-8") as f:
    all_papers = json.load(f)

categories = cls_data["categories"]
assignments = cls_data["assignments"]
category_analyses = narrative["category_analyses"]
executive_summary = narrative["executive_summary_ko"]

slug_to_meta = {p["slug"]: p for p in all_papers}

actual_dirs = sorted(
    d for d in os.listdir(BASE)
    if os.path.isdir(f"{BASE}/{d}") and len(d) >= 3 and d[:3].isdigit()
)

def find_dir_for_slug(slug):
    if slug in actual_dirs:
        return slug
    for d in actual_dirs:
        if d.startswith(slug[:35]):
            return d
    num = slug[:3]
    candidates = [d for d in actual_dirs if d.startswith(num + "_")]
    if len(candidates) == 1:
        return candidates[0]
    return None

def parse_review_md(dir_name):
    md_path = f"{BASE}/{dir_name}/review.md"
    if not os.path.exists(md_path):
        return {}
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    result = {}
    m = re.search(r"^#\s+(.+)", text, re.MULTILINE)
    if m:
        result["title"] = m.group(1).strip()
    hm = re.search(r"^>\s*\*\*저자\*\*:\s*(.+)", text, re.MULTILINE)
    if hm:
        hl = hm.group(1)
        result["authors"] = hl.split("|")[0].strip()
        dm = re.search(r"\*\*날짜\*\*:\s*([^\|]+)", hl)
        if dm: result["date"] = dm.group(1).strip()
        jm = re.search(r"\*\*Journal\*\*:\s*([^\|]+)", hl)
        if jm: result["journal"] = jm.group(1).strip()
        doi_m = re.search(r"\*\*DOI\*\*:\s*([^\|]+)", hl)
        if doi_m: result["doi"] = doi_m.group(1).strip()
        ax_m = re.search(r"\*\*arXiv\*\*:\s*([^\|]+)", hl)
        if ax_m: result["arxiv"] = ax_m.group(1).strip()
    em = re.search(r"## Essence\s*\n+([\s\S]+?)(?=\n## |\Z)", text)
    if em: result["essence"] = em.group(1).strip()
    om = re.search(r"\|\s*Overall\s*\|\s*(\d+(?:\.\d+)?)/5\s*\|", text)
    if om: result["overall_score"] = float(om.group(1))
    for label, key in [("Novelty", "novelty"), ("Technical Soundness", "technical_soundness"),
                        ("Significance", "significance"), ("Clarity", "clarity")]:
        sm = re.search(rf"\|\s*{label}\s*\|\s*(\d+(?:\.\d+)?)/5\s*\|", text)
        if sm: result[key] = int(sm.group(1))
    vm = re.search(r"\*\*총평\*\*:\s*([\s\S]+?)(?=\n##|\Z)", text)
    if vm: result["verdict"] = vm.group(1).strip()
    return result

def normalize_date(ds):
    if not ds: return ""
    ds = str(ds).strip()
    m = re.match(r"^(\d{4})-(\d{2})-\d{2}$", ds)
    if m: return f"{m.group(1)}.{m.group(2)}"
    m = re.match(r"^(\d{4})-(\d{2})$", ds)
    if m: return f"{m.group(1)}.{m.group(2)}"
    if re.match(r"^\d{4}\.\d{2}$", ds): return ds
    if re.match(r"^\d{4}$", ds): return ds
    return ds

cat_order = [c["name"] for c in categories]
cat_papers = defaultdict(list)
unmatched = []

for asgn in assignments:
    slug = asgn["slug"]
    primary_cat = asgn["primary_category"]
    dir_name = find_dir_for_slug(slug)
    if dir_name is None:
        unmatched.append(slug)
        continue
    meta = slug_to_meta.get(slug, {})
    review = parse_review_md(dir_name)
    title = review.get("title") or meta.get("title", slug)
    authors = review.get("authors", "")
    raw_date = review.get("date") or str(meta.get("date", ""))
    date_fmt = normalize_date(raw_date)
    journal = review.get("journal", "")
    doi = review.get("doi", "")
    arxiv = review.get("arxiv", "")
    essence = review.get("essence") or meta.get("essence", "")
    overall_score = review.get("overall_score") or meta.get("score") or 0
    has_fig = os.path.exists(f"{BASE}/{dir_name}/figures/fig1.png")
    cat_papers[primary_cat].append({
        "dir": dir_name, "slug": slug, "title": title, "authors": authors,
        "date": date_fmt, "journal": journal, "doi": doi, "arxiv": arxiv,
        "essence": essence, "overall_score": float(overall_score) if overall_score else 0,
        "novelty": review.get("novelty"), "technical_soundness": review.get("technical_soundness"),
        "significance": review.get("significance"), "clarity": review.get("clarity"),
        "verdict": review.get("verdict", ""),
        "has_fig": has_fig, "fig_src": f"{dir_name}/figures/fig1.png" if has_fig else None,
    })

if unmatched:
    print(f"WARNING unmatched: {unmatched}")
for cat in cat_papers:
    cat_papers[cat].sort(key=lambda p: p["overall_score"], reverse=True)
total_papers = sum(len(v) for v in cat_papers.values())
print(f"Total papers: {total_papers}")
for cn in cat_order:
    print(f"  {cn}: {len(cat_papers[cn])}")


def esc(s):
    return escape(str(s)) if s else ""

def make_doi_link(doi, arxiv):
    if doi:
        if doi.startswith("http"):
            return f'<a href="{esc(doi)}" target="_blank">{esc(doi)}</a>'
        return f'<a href="https://doi.org/{esc(doi)}" target="_blank">{esc(doi)}</a>'
    if arxiv:
        return esc(arxiv)
    return ""

def render_paper_card(paper, num, cat_slug):
    score = paper["overall_score"]
    score_disp = f"{int(score)}/5" if score and score > 0 else "N/A"
    score_val = score if score else 0
    meta_parts = []
    if paper["authors"]: meta_parts.append(f'<strong>저자</strong>: {esc(paper["authors"])}')
    if paper["date"]: meta_parts.append(f'<strong>날짜</strong>: {esc(paper["date"])}')
    if paper["journal"]: meta_parts.append(f'<strong>Journal</strong>: {esc(paper["journal"])}')
    dl = make_doi_link(paper["doi"], paper["arxiv"])
    if dl: meta_parts.append(f'<strong>DOI</strong>: {dl}')
    meta_html = " | ".join(meta_parts)
    badges = []
    for label, key in [("Novelty", "novelty"), ("Technical Soundness", "technical_soundness"),
                        ("Significance", "significance"), ("Clarity", "clarity")]:
        val = paper.get(key)
        if val is not None: badges.append(f'<span class="score-badge">{label}: {val}</span>')
    if score and score > 0: badges.append(f'<span class="score-badge">Overall: {int(score)}</span>')
    badges_html = " ".join(badges)
    fig_html = ""
    if paper["has_fig"]:
        fig_html = (
            '\n          <div class="paper-fig">'
            f'<img data-src="{esc(paper["fig_src"])}" alt="Figure" class="lazy">'
            '</div>'
        )
    essence_html = ""
    if paper["essence"]:
        essence_html = (
            '\n          <div class="section">'
            '\n            <div class="section-label">Essence</div>'
            f'\n            <p>{esc(paper["essence"])}</p>'
            '\n          </div>'
        )
    eval_html = ""
    if badges or paper["verdict"]:
        inner = ""
        if badges_html: inner += f'<div class="scores">{badges_html}</div>\n            '
        if paper["verdict"]: inner += f'<p class="verdict">{esc(paper["verdict"])}</p>'
        eval_html = (
            '\n          <div class="section">'
            '\n            <div class="section-label">Evaluation</div>'
            f'\n            {inner}'
            '\n          </div>'
        )
    return (
        f'        <div class="paper-card" data-date="{esc(paper["date"])}"'
        f' data-score="{score_val}" data-topic="{esc(cat_slug)}">\n'
        f'          <div class="paper-header">\n'
        f'            <span class="paper-num">#{num}</span>\n'
        f'            <span class="paper-date">{esc(paper["date"])}</span>\n'
        f'            <span class="paper-score">{score_disp}</span>\n'
        f'          </div>\n'
        f'          <h3><a href="{esc(paper["dir"])}/index.html">{esc(paper["title"])}</a></h3>\n'
        f'          <p class="meta">{meta_html}</p>'
        f'{fig_html}{essence_html}{eval_html}\n'
        f'        </div>'
    )

def render_category_narrative(cat_name):
    ca = category_analyses.get(cat_name, {})
    if not ca: return ""
    sub_themes = ca.get("sub_themes", [])
    html_parts = []
    for st in sub_themes:
        name = st.get("name", ""); desc = st.get("description", "")
        start = st.get("start_year", ""); peak = st.get("peak_year", "")
        status = st.get("status", "")
        if name and desc:
            yr = f"{start}~{peak}" if start and peak else str(start or peak or "")
            status_str = f" &mdash; <em>{esc(status)}</em>" if status else ""
            html_parts.append(
                f'<p><strong>{esc(name)}</strong>'
                + (f' ({esc(yr)})' if yr else '')
                + f': {esc(desc)}{status_str}</p>'
            )
    return "\n".join(html_parts)

def render_exec_summary(text):
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    return "\n    ".join(f"<p>{esc(p)}</p>" for p in paras)

CSS = (
    "* { margin: 0; padding: 0; box-sizing: border-box; }\n"
    "body { font-family: 'KoPub Dotum', 'KoPubDotumMedium', -apple-system, 'Noto Sans KR', sans-serif;"
    " background: #f0f2f5; color: #333; line-height: 1.6; }\n"
    ".container { max-width: 960px; margin: 0 auto; padding: 2rem 1.5rem; }\n"
    ".hero { background: linear-gradient(135deg, #2a0f0d 0%, #5c1a14 50%, #A62018 100%);"
    " color: white; padding: 3rem 2rem; border-radius: 16px; margin-bottom: 2rem; }\n"
    ".hero h1 { font-size: 1.8rem; font-weight: 700; margin-bottom: 0.5rem; }\n"
    ".hero .subtitle { opacity: 0.85; font-size: 1rem; }\n"
    ".hero .stats { margin-top: 1rem; display: flex; gap: 2rem; }\n"
    ".hero .stat { text-align: center; }\n"
    ".hero .stat-num { font-size: 2rem; font-weight: 700; color: #F06050; }\n"
    ".hero .stat-label { font-size: 0.8rem; opacity: 0.7; }\n"
    ".paper-card { background: white; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.2rem;"
    " box-shadow: 0 2px 8px rgba(0,0,0,0.06); border-left: 4px solid #D63423;"
    " transition: transform 0.15s, box-shadow 0.15s; }\n"
    ".paper-card:hover { transform: translateY(-2px); box-shadow: 0 4px 16px rgba(0,0,0,0.1); }\n"
    ".paper-header { display: flex; justify-content: space-between; align-items: center;"
    " margin-bottom: 0.5rem; }\n"
    ".paper-num { font-size: 0.85rem; color: #888; font-weight: 600; }\n"
    ".paper-score { background: #D63423; color: white; padding: 0.2rem 0.7rem;"
    " border-radius: 20px; font-weight: 700; font-size: 0.9rem; }\n"
    ".paper-card h3 { font-size: 1.05rem; color: #1a1a2e; margin-bottom: 0.3rem; }\n"
    ".paper-card h3 a { color: #1a1a2e; text-decoration: none; }\n"
    ".paper-card h3 a:hover { color: #D63423; }\n"
    ".meta { font-size: 0.8rem; color: #888; margin-bottom: 0.8rem; }\n"
    ".section { margin-top: 0.8rem; }\n"
    ".section-label { font-weight: 700; font-size: 0.85rem; color: #D63423; text-transform: uppercase;"
    " letter-spacing: 0.05em; margin-bottom: 0.3rem; border-bottom: 1px solid #e8edf3;"
    " padding-bottom: 0.2rem; }\n"
    ".section p { font-size: 0.92rem; color: #444; }\n"
    ".scores { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-bottom: 0.4rem; }\n"
    ".score-badge { background: #e8edf3; color: #A62018; padding: 0.15rem 0.6rem;"
    " border-radius: 12px; font-size: 0.78rem; font-weight: 600; }\n"
    ".verdict { font-style: normal; color: #444; font-size: 0.9rem; }\n"
    ".paper-fig { margin: 0.8rem 0; text-align: center; }\n"
    ".paper-fig img { max-width: min(100%, 600px); border: 1px solid #e0e0e0;"
    " border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }\n"
    ".excluded { background: #fff3cd; border-radius: 12px; padding: 1.2rem; margin-top: 1.5rem; }\n"
    ".excluded h3 { color: #856404; font-size: 1rem; margin-bottom: 0.5rem; }\n"
    ".excluded li { font-size: 0.85rem; color: #856404; margin: 0.3rem 0; }\n"
    ".excluded code { background: #ffeeba; padding: 0.1rem 0.4rem; border-radius: 4px; }\n"
    ".credit { text-align: center; font-size: 0.8rem; color: #aaa; margin-top: 2rem;"
    " padding-top: 1rem; border-top: 1px solid #e0e0e0; }\n"
    ".sort-bar { display: flex; gap: 0.5rem; margin-bottom: 1.2rem; flex-wrap: wrap; }\n"
    ".sort-btn { background: white; border: 1px solid #D63423; color: #D63423;"
    " padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.8rem; cursor: pointer;"
    " font-weight: 600; }\n"
    ".sort-btn:hover, .sort-btn.active { background: #D63423; color: white; }\n"
    ".timeline-section { background: white; border-radius: 12px; padding: 1.5rem;"
    " margin-bottom: 1.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }\n"
    ".timeline-section h2 { color: #A62018; font-size: 1.1rem; margin-bottom: 1rem; }\n"
    ".timeline-chart { display: flex; align-items: flex-end; gap: 4px; height: 120px;"
    " margin-bottom: 1rem; padding: 0 0.5rem; }\n"
    ".timeline-bar { flex: 1; background: #D63423; border-radius: 4px 4px 0 0; min-width: 20px;"
    " position: relative; transition: opacity 0.2s; }\n"
    ".timeline-bar:hover { opacity: 0.8; }\n"
    ".timeline-bar .bar-label { position: absolute; bottom: -20px; left: 50%;"
    " transform: translateX(-50%); font-size: 0.7rem; color: #888; }\n"
    ".timeline-bar .bar-count { position: absolute; top: -18px; left: 50%;"
    " transform: translateX(-50%); font-size: 0.7rem; font-weight: 700; color: #A62018; }\n"
    ".timeline-summary { font-size: 0.9rem; color: #444; line-height: 1.6; }\n"
    ".timeline-summary p { margin: 0.5rem 0; }\n"
    ".topic-group { margin-bottom: 1rem; }\n"
    ".topic-header { background: #f5f5f5; border-radius: 12px; padding: 0.8rem 1.2rem;"
    " cursor: pointer; display: flex; align-items: center; gap: 0.8rem;"
    " border-left: 4px solid #999; user-select: none; transition: background 0.15s; }\n"
    ".topic-header:hover { background: #ebebeb; }\n"
    ".topic-name { font-weight: 700; font-size: 1rem; flex: 1; color: #444; }\n"
    ".topic-count { font-size: 0.8rem; color: #888; background: #e0e0e0;"
    " padding: 0.15rem 0.5rem; border-radius: 10px; }\n"
    ".topic-toggle { font-size: 0.8rem; color: #999; transition: transform 0.2s; }\n"
    ".topic-body { padding: 0.5rem 0 0 0; }\n"
    ".topic-body.collapsed { display: none; }\n"
    ".category-timeline { margin: 0.5rem 0 1rem; text-align: center; }\n"
    ".category-timeline img { max-width: 100%; border-radius: 8px;"
    " box-shadow: 0 2px 8px rgba(0,0,0,0.1); }\n"
    ".category-summary { background: white; border-radius: 12px; padding: 1.2rem 1.5rem;"
    " margin-bottom: 1rem; box-shadow: 0 1px 4px rgba(0,0,0,0.06);"
    " font-size: 0.9rem; line-height: 1.7; color: #444; }\n"
    ".category-summary p { margin: 0.6rem 0; }\n"
    ".paper-date { font-size: 0.75rem; color: #999; }\n"
    "img.lazy { opacity: 0; transition: opacity 0.3s; }\n"
    "img.lazy.loaded { opacity: 1; }"
)

# JavaScript — use explicit unicode escapes to avoid any quote issues
JS = (
    "function toggleTopic(id) {\n"
    "  const body = document.getElementById(id);\n"
    "  const toggle = document.getElementById('toggle-' + id);\n"
    "  body.classList.toggle('collapsed');\n"
    "  toggle.textContent = body.classList.contains('collapsed') ? '\u25B6' : '\u25BC';\n"
    "  if (!body.classList.contains('collapsed')) setTimeout(lazyLoad, 100);\n"
    "}\n"
    "function sortCards(key, order) {\n"
    "  document.querySelectorAll('.topic-body').forEach(body => {\n"
    "    const cards = [...body.querySelectorAll('.paper-card')];\n"
    "    cards.sort((a, b) => {\n"
    "      let va, vb;\n"
    "      if (key === 'date') { va = a.dataset.date || ''; vb = b.dataset.date || ''; }\n"
    "      else { va = parseFloat(a.dataset.score) || 0; vb = parseFloat(b.dataset.score) || 0; }\n"
    "      if (order === 'asc') return va > vb ? 1 : va < vb ? -1 : 0;\n"
    "      return va < vb ? 1 : va > vb ? -1 : 0;\n"
    "    });\n"
    "    cards.forEach(c => body.appendChild(c));\n"
    "  });\n"
    "  document.querySelectorAll('.sort-btn').forEach(b => b.classList.remove('active'));\n"
    "  event.target.classList.add('active');\n"
    "  setTimeout(lazyLoad, 100);\n"
    "}\n"
    "function lazyLoad() {\n"
    "  const imgs = document.querySelectorAll('img.lazy:not(.loaded)');\n"
    "  if ('IntersectionObserver' in window) {\n"
    "    const obs = new IntersectionObserver((entries) => {\n"
    "      entries.forEach(e => {\n"
    "        if (e.isIntersecting) {\n"
    "          const img = e.target; img.src = img.dataset.src;\n"
    "          img.classList.add('loaded'); obs.unobserve(img);\n"
    "        }\n"
    "      });\n"
    "    }, {rootMargin: '200px'});\n"
    "    imgs.forEach(img => obs.observe(img));\n"
    "  } else { imgs.forEach(img => { img.src = img.dataset.src; img.classList.add('loaded'); }); }\n"
    "}\n"
    "document.addEventListener('DOMContentLoaded', lazyLoad);"
)

topic_groups_parts = []
global_num = 1
for cat_idx, cat_name in enumerate(cat_order):
    papers = cat_papers.get(cat_name, [])
    topic_id = f"topic-{cat_idx}"
    cat_slug = cat_name.replace(" ", "_").replace("&", "and")
    narr_html = render_category_narrative(cat_name)
    summary_block = f'\n<div class="category-summary">{narr_html}</div>' if narr_html else ""
    cards_parts = []
    for paper in papers:
        cards_parts.append(render_paper_card(paper, global_num, cat_slug))
        global_num += 1
    group = (
        f'<div class="topic-group" data-topic="{esc(cat_name)}">\n'
        f'      <div class="topic-header" onclick="toggleTopic(\'{topic_id}\')">\n'
        f'        <span class="topic-name">{esc(cat_name)}</span>\n'
        f'        <span class="topic-count">{len(papers)}\uD3B8</span>\n'
        f'        <span class="topic-toggle" id="toggle-{topic_id}">&#x25B6;</span>\n'
        f'      </div>\n'
        f'      <div class="topic-body collapsed" id="{topic_id}">{summary_block}\n'
        + "\n".join(cards_parts) + "\n"
        + '      </div>\n'
        + '    </div>'
    )
    topic_groups_parts.append(group)

exec_html = render_exec_summary(executive_summary)

HTML = (
    '<!DOCTYPE html>\n'
    '<html lang="ko">\n'
    '<head>\n'
    '<meta charset="UTF-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1.0">\n'
    '<title>AI for Science &#8212; 248 Papers</title>\n'
    '<link rel="stylesheet" href="https://cdn.jsdelivr.net/font-kopub/1.0/kopubdotum.css">\n'
    '<script>window.MathJax={tex:{inlineMath:[[\'$\',\'$\'],[\'\\\\(\',\'\\\\)\']],displayMath:[[\'$$\',\'$$\'],[\'\\\\[\',\'\\\\]\']]}};</script>\n'
    '<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>\n'
    '<style>\n' + CSS + '\n</style>\n'
    '</head>\n'
    '<body>\n'
    '<div class="container">\n'
    '  <div class="hero">\n'
    '    <h1>AI for Science &#8212; 248 Papers</h1>\n'
    '    <div class="stats">\n'
    '      <div class="stat"><div class="stat-num">248</div><div class="stat-label">\ub9ac\uBDF0 \uc644\ub8cc</div></div>\n'
    '      <div class="stat"><div class="stat-num">8</div><div class="stat-label">MECE \uce74\ud14c\uace0\ub9ac</div></div>\n'
    '      <div class="stat"><div class="stat-num">2026-03-27</div><div class="stat-label">\ud050\ub808\uc774\uc158 \uc77c\uc790</div></div>\n'
    '    </div>\n'
    '  </div>\n\n\n'
    '<div class="timeline-section">\n'
    '  <h2>Research Timeline</h2>\n'
    '  <div style="text-align:center;margin:1rem 0">'
    '<img src="research_timeline.png" alt="Research Timeline"'
    ' style="max-width:100%;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,0.1)">'
    '</div>\n'
    '  <div class="timeline-summary">\n'
    '    ' + exec_html + '\n'
    '  </div>\n'
    '</div>\n\n\n'
    '  <div class="sort-bar">\n'
    '    <button class="sort-btn" onclick="sortCards(\'date\',\'asc\')">\ucd9c\ud310\uc77c &#x25B2;</button>\n'
    '    <button class="sort-btn" onclick="sortCards(\'date\',\'desc\')">\ucd9c\ud310\uc77c &#x25BC;</button>\n'
    '    <button class="sort-btn" onclick="sortCards(\'score\',\'asc\')">\ud3c9\uc810 &#x25B2;</button>\n'
    '    <button class="sort-btn" onclick="sortCards(\'score\',\'desc\')">\ud3c9\uc810 &#x25BC;</button>\n'
    '  </div>\n\n'
    '  <div id="cards">\n\n'
    + "\n\n".join(topic_groups_parts) + "\n\n"
    + '  </div>\n'
    '  <div class="credit">\n'
    '    Generated by Claude Code &middot; AI for Science Paper Curation &middot; 2026-03-27\n'
    '  </div>\n\n'
    '</div>\n\n'
    '<script>\n' + JS + '\n</script>\n\n'
    '</body>\n</html>'
)

out_path = f"{BASE}/index.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"Written: {out_path} ({len(HTML):,} chars)")

# Build _category_summaries.json
cat_summaries = []
for cat_idx, cat_name in enumerate(cat_order):
    cat_def = categories[cat_idx]
    papers = cat_papers.get(cat_name, [])
    ca = category_analyses.get(cat_name, {})
    sub_themes = ca.get("sub_themes", [])
    scored = [p["overall_score"] for p in papers if p["overall_score"]]
    avg_score = round(sum(scored) / len(scored), 2) if scored else 0
    cat_summaries.append({
        "category": cat_name,
        "description": cat_def.get("description", ""),
        "keywords": cat_def.get("keywords", []),
        "count": len(papers),
        "avg_score": avg_score,
        "sub_themes": [
            {"name": st.get("name", ""), "description": st.get("description", ""),
             "start_year": st.get("start_year"), "peak_year": st.get("peak_year"),
             "status": st.get("status", "")}
            for st in sub_themes
        ],
        "papers": [
            {"slug": p["slug"], "dir": p["dir"], "title": p["title"],
             "score": p["overall_score"], "date": p["date"]}
            for p in papers
        ],
    })

summary_path = f"{BASE}/_category_summaries.json"
with open(summary_path, "w", encoding="utf-8") as f:
    json.dump(cat_summaries, f, ensure_ascii=False, indent=2)
print(f"Written: {summary_path}")
