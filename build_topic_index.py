"""
Unified topic index builder for paper-curation.
Reads reviews from papers/ central repo, generates {topic}/index.html.

Usage: PYTHONUTF8=1 python build_topic_index.py <topic>
  e.g. PYTHONUTF8=1 python build_topic_index.py ai4s
       PYTHONUTF8=1 python build_topic_index.py scisci
"""
import json, os, re, sys
from html import escape
from collections import defaultdict
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))
TODAY = datetime.now(KST).strftime("%Y-%m-%d")

REPO_DIR = r"C:\Users\jehyu\Arbeitplatz\paper-curation"
PAPERS_DIR = os.path.join(REPO_DIR, "papers")

def get_topic():
    if len(sys.argv) > 1:
        return sys.argv[1]
    return "ai4s"

TOPIC = get_topic()
TOPIC_DIR = os.path.join(REPO_DIR, TOPIC)

# Theme colors per topic
THEME = {
    "ai4s": {
        "gradient": "linear-gradient(135deg, #2a0f0d 0%, #5c1a14 50%, #A62018 100%)",
        "accent": "#D63423", "accent_dark": "#A62018", "accent_light": "#F06050",
        "title": "AI for Science",
        "subtitle_prefix": "AI assisted Research",
    },
    "scisci": {
        "gradient": "linear-gradient(135deg, #0d1a2a 0%, #14385c 50%, #1866A6 100%)",
        "accent": "#2374D6", "accent_dark": "#1856A0", "accent_light": "#50A0F0",
        "title": "Science of Science",
        "subtitle_prefix": "Bibliometrics & Scientometrics",
    },
}
theme = THEME.get(TOPIC, THEME["ai4s"])

# Load data
with open(os.path.join(PAPERS_DIR, "_papers_index.json"), encoding="utf-8") as f:
    papers_index = json.load(f)

cls_path = os.path.join(TOPIC_DIR, "_new_classification.json")
narr_path = os.path.join(TOPIC_DIR, "_timeline_narrative.json")

if os.path.exists(cls_path):
    with open(cls_path, encoding="utf-8") as f:
        cls_data = json.load(f)
    categories = cls_data.get("categories", [])
    assignments = cls_data.get("assignments", [])
else:
    categories = []
    assignments = []

if os.path.exists(narr_path):
    with open(narr_path, encoding="utf-8") as f:
        narrative = json.load(f)
    category_analyses = narrative.get("category_analyses", {})
    executive_summary = narrative.get("executive_summary_ko", "")
else:
    category_analyses = {}
    executive_summary = ""

# Merge _category_summaries.json (has description + papers per category)
cat_sum_path = os.path.join(TOPIC_DIR, "_category_summaries.json")
if os.path.exists(cat_sum_path):
    with open(cat_sum_path, encoding="utf-8") as f:
        cat_summaries = json.load(f)
    for cs in cat_summaries:
        cat_name_cs = cs.get("category", "")
        if cat_name_cs not in category_analyses:
            category_analyses[cat_name_cs] = {}
        if cs.get("description"):
            category_analyses[cat_name_cs]["description"] = cs["description"]
        if cs.get("description_ko"):
            category_analyses[cat_name_cs]["description_ko"] = cs["description_ko"]
        if cs.get("sub_themes_ko"):
            category_analyses[cat_name_cs]["sub_themes_ko"] = cs["sub_themes_ko"]
        if cs.get("papers"):
            category_analyses[cat_name_cs]["papers"] = cs["papers"]
        # Merge sub_themes if not already present from narrative
        if not category_analyses[cat_name_cs].get("sub_themes") and cs.get("sub_themes"):
            category_analyses[cat_name_cs]["sub_themes"] = cs["sub_themes"]

# Filter papers for this topic
topic_papers = [p for p in papers_index if TOPIC in p.get("topics", [])]
slug_to_index = {p["slug"]: p for p in topic_papers}

# Assignment slug → category mapping (multi-class)
slug_to_cat = {}       # slug → primary_category (str)
slug_to_all_cats = {}  # slug → all_categories (list)
for a in assignments:
    slug_to_cat[a["slug"]] = a.get("primary_category", "Other")
    slug_to_all_cats[a["slug"]] = a.get("all_categories", [a.get("primary_category", "Other")])

# Available paper directories in papers/
actual_dirs = sorted(
    d for d in os.listdir(PAPERS_DIR)
    if os.path.isdir(os.path.join(PAPERS_DIR, d)) and len(d) >= 3 and d[:3].isdigit()
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

def parse_review_md(slug):
    dir_name = find_dir_for_slug(slug)
    if not dir_name:
        return {}, None
    md_path = os.path.join(PAPERS_DIR, dir_name, "review.md")
    if not os.path.exists(md_path):
        return {}, dir_name
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    result = {}
    m = re.search(r"^#\s+(.+)", text, re.MULTILINE)
    if m: result["title"] = m.group(1).strip()
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
    em = re.search(r"## (?:Essence|한줄 요약)[^\n]*\s*\n+([\s\S]+?)(?=\n## |\Z)", text)
    if em: result["essence"] = em.group(1).strip()
    # Parse scores from table format OR list format
    for label, key in [("Novelty", "novelty"), ("Technical Soundness", "technical_soundness"),
                        ("Significance", "significance"), ("Clarity", "clarity"), ("Overall", "overall_score")]:
        # Table: | Label | X/5 |
        sm = re.search(rf"\|\s*{label}\s*\|\s*(\d+(?:\.\d+)?)\s*/\s*5\s*\|", text)
        if not sm:
            # List: - Label: X/5
            sm = re.search(rf"-\s*{label}\s*:\s*(\d+(?:\.\d+)?)\s*/\s*5", text)
        if sm:
            val = float(sm.group(1))
            if key == "overall_score":
                result[key] = val
            else:
                result[key] = int(val)
    vm = re.search(r"\*\*총평\*\*:\s*([\s\S]+?)(?=\n##|\Z)", text)
    if vm: result["verdict"] = vm.group(1).strip()
    return result, dir_name

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

# Build category → papers mapping
cat_order = [c["name"] for c in categories] if categories else ["Other"]
cat_papers = defaultdict(list)
unmatched = []

for p_idx in topic_papers:
    slug = p_idx["slug"]
    all_cats = slug_to_all_cats.get(slug, p_idx.get("all_categories", [p_idx.get("primary_category", "Other")]))
    if not all_cats:
        all_cats = [slug_to_cat.get(slug, "Other")]
    review, dir_name = parse_review_md(slug)
    if dir_name is None:
        unmatched.append(slug)
        continue
    title = review.get("title") or p_idx.get("title", slug)
    authors = review.get("authors", "")
    raw_date = review.get("date") or str(p_idx.get("date", ""))
    date_fmt = normalize_date(raw_date)
    journal = review.get("journal", "")
    doi = review.get("doi") or p_idx.get("doi", "")
    arxiv = review.get("arxiv", "")
    essence = review.get("essence") or p_idx.get("essence", "")
    overall_score = review.get("overall_score") or p_idx.get("score") or 0
    has_fig = os.path.exists(os.path.join(PAPERS_DIR, dir_name, "figures", "fig1.png"))
    # Extract fig1 caption from pdffigures2 JSON or review.md
    fig_caption = ""
    pf2_json = os.path.join(PAPERS_DIR, dir_name, "figures", "pdffigures2",
                            os.listdir(os.path.join(PAPERS_DIR, dir_name, "figures", "pdffigures2"))[0]) \
                if os.path.isdir(os.path.join(PAPERS_DIR, dir_name, "figures", "pdffigures2")) \
                and any(f.endswith(".json") for f in os.listdir(os.path.join(PAPERS_DIR, dir_name, "figures", "pdffigures2"))) \
                else None
    if pf2_json and pf2_json.endswith(".json"):
        try:
            import json as _json
            with open(pf2_json, "r", encoding="utf-8") as _f:
                figs_meta = _json.load(_f)
            if figs_meta and isinstance(figs_meta, list):
                fig_caption = figs_meta[0].get("caption", "")
        except Exception:
            pass
    if not fig_caption:
        # Fallback: extract from review.md (line after ![Figure 1])
        md_path = os.path.join(PAPERS_DIR, dir_name, "review.md")
        if os.path.exists(md_path):
            with open(md_path, "r", encoding="utf-8") as _f:
                md_text = _f.read()
            import re as _re
            cap_m = _re.search(r'!\[.*?\]\(figures/fig1.*?\)\s*\n+\*(.+?)\*', md_text)
            if cap_m:
                fig_caption = cap_m.group(1).strip()
    paper_data = {
        "dir": dir_name, "slug": slug, "title": title, "authors": authors,
        "date": date_fmt, "journal": journal, "doi": doi, "arxiv": arxiv,
        "essence": essence, "overall_score": float(overall_score) if overall_score else 0,
        "novelty": review.get("novelty"), "technical_soundness": review.get("technical_soundness"),
        "significance": review.get("significance"), "clarity": review.get("clarity"),
        "verdict": review.get("verdict", ""),
        "has_fig": has_fig,
        "fig_src": f"../papers/{dir_name}/figures/fig1.png" if has_fig else None,
        "fig_caption": fig_caption,
    }
    # Multi-class: add to ALL matching categories
    for cat in all_cats:
        if cat in cat_order or cat == "Other":
            cat_papers[cat].append(paper_data)

if unmatched:
    print(f"WARNING unmatched: {unmatched}")
for cat in cat_papers:
    cat_papers[cat].sort(key=lambda p: p["overall_score"], reverse=True)
total_papers = sum(len(v) for v in cat_papers.values())
print(f"Total papers for {TOPIC}: {total_papers}")
for cn in cat_order:
    print(f"  {cn}: {len(cat_papers.get(cn, []))}")

# --- HTML Rendering ---

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
    if paper["authors"]: meta_parts.append(f'<strong>\uc800\uc790</strong>: {esc(paper["authors"])}')
    if paper["date"]: meta_parts.append(f'<strong>\ub0a0\uc9dc</strong>: {esc(paper["date"])}')
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
        cap = paper.get("fig_caption", "")
        cap_html = f'<p class="fig-caption">{esc(cap)}</p>' if cap else ""
        fig_html = (
            '\n          <div class="paper-fig">'
            f'<img data-src="{esc(paper["fig_src"])}" alt="Figure" class="lazy">'
            f'{cap_html}</div>'
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
    # Link to ../papers/{slug}/index.html
    link_href = f"../papers/{esc(paper['dir'])}/index.html"
    return (
        f'        <div class="paper-card" data-date="{esc(paper["date"])}"'
        f' data-score="{score_val}" data-topic="{esc(cat_slug)}">\n'
        f'          <div class="paper-header">\n'
        f'            <span class="paper-num">#{num}</span>\n'
        f'            <span class="paper-date">{esc(paper["date"])}</span>\n'
        f'            <span class="paper-score">{score_disp}</span>\n'
        f'          </div>\n'
        f'          <h3><a href="{link_href}">{esc(paper["title"])}</a></h3>\n'
        f'          <p class="meta">{meta_html}</p>'
        f'{fig_html}{essence_html}{eval_html}\n'
        f'        </div>'
    )

def _match_papers_to_subtheme(st_name, st_desc, papers):
    """Match papers to a sub-theme by keyword overlap in title."""
    keywords = set((st_name + " " + st_desc).lower().split())
    scored = []
    for p in papers:
        title_words = set(p.get("title", "").lower().split())
        overlap = len(keywords & title_words)
        if overlap >= 2:
            scored.append((overlap, p))
    scored.sort(key=lambda x: (-x[0], -x[1].get("score", 0)))
    return [s[1] for s in scored[:4]]  # max 4 papers per sub-theme


def render_category_narrative(cat_name):
    ca = category_analyses.get(cat_name, {})
    if not ca: return ""
    overview = ca.get("description", "")
    sub_themes = ca.get("sub_themes", [])
    cat_papers = ca.get("papers", [])
    html_parts = []

    # Build slug number → paper info lookup (used for [NNN] → link conversion)
    import re as _re
    num_to_paper = {}
    for p in cat_papers:
        slug = p.get("dir", p.get("slug", ""))
        title = p.get("title", "")
        num = slug.split("_")[0] if "_" in slug else slug[:3]
        num_to_paper[num] = (slug, title)

    def _refs_to_links(text_html):
        """Convert [NNN] markers to <a> links."""
        def _repl(m):
            num = m.group(1)
            if num in num_to_paper:
                slug, title = num_to_paper[num]
                return f'<a href="../papers/{esc(slug)}/index.html" title="{esc(title)}">[{num}]</a>'
            return m.group(0)
        return _re.sub(r'\[(\d{3})\]', _repl, text_html)

    # Category Overview (한글 우선)
    overview_ko = ca.get("description_ko", "")
    if overview_ko:
        overview_html = _refs_to_links(esc(overview_ko))
        html_parts.append(f'<h4>Category Overview</h4>\n<p>{overview_html}</p>')
    elif overview:
        html_parts.append(f'<h4>Category Overview</h4>\n<p>{esc(overview)}</p>')

    # Sub-category bullets with paper links (한글 우선)
    # sub_themes_ko can be list of dicts or dict of {snake_case_key: desc}
    raw_stko = ca.get("sub_themes_ko", [])
    _stko_map = {}
    if isinstance(raw_stko, dict):
        for k, v in raw_stko.items():
            _stko_map[k.lower().replace("_", " ").replace("-", " ")] = v
    elif isinstance(raw_stko, list):
        for s in raw_stko:
            if isinstance(s, dict):
                n = s.get("name", "")
                _stko_map[n.lower().replace("_", " ").replace("-", " ")] = s.get("description_ko", "")

    def _get_stko(st_name):
        norm = st_name.lower().replace("_", " ").replace("-", " ").replace("&", "and")
        # Exact match
        if norm in _stko_map:
            return _stko_map[norm]
        # Fuzzy: word overlap
        nw = set(norm.split())
        for k, v in _stko_map.items():
            kw = set(k.split())
            if len(kw & nw) >= min(3, len(kw)):
                return v
        return ""

    if sub_themes:
        html_parts.append('<ul class="subcategory-list">')
        for st in sub_themes:
            name = st.get("name", "")
            desc_en = st.get("description", "")
            desc = _get_stko(name) or desc_en
            if not name or not desc:
                continue
            # Convert [NNN] markers to hyperlinks
            desc_html = _refs_to_links(esc(desc))
            html_parts.append(
                f'<li><strong>{esc(name)}</strong>: {desc_html}</li>'
            )
        html_parts.append('</ul>')

    return "\n".join(html_parts)

def render_exec_summary(text):
    if not text: return ""
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    return "\n    ".join(f"<p>{esc(p)}</p>" for p in paras)

# CSS with theme
accent = theme["accent"]
accent_dark = theme["accent_dark"]
accent_light = theme["accent_light"]
gradient = theme["gradient"]

CSS = f"""* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: 'KoPub Dotum', 'KoPubDotumMedium', -apple-system, 'Noto Sans KR', sans-serif; background: #f0f2f5; color: #333; line-height: 1.6; }}
.container {{ max-width: 960px; margin: 0 auto; padding: 2rem 1.5rem; }}
.hero {{ background: {gradient}; color: white; padding: 3rem 2rem; border-radius: 16px; margin-bottom: 2rem; }}
.hero h1 {{ font-size: 1.8rem; font-weight: 700; margin-bottom: 0.5rem; }}
.hero .subtitle {{ opacity: 0.85; font-size: 1rem; }}
.hero .stats {{ margin-top: 1rem; display: flex; gap: 2rem; }}
.hero .stat {{ text-align: center; }}
.hero .stat-num {{ font-size: 2rem; font-weight: 700; color: {accent_light}; }}
.hero .stat-label {{ font-size: 0.8rem; opacity: 0.7; }}
.paper-card {{ background: white; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.2rem; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border-left: 4px solid {accent}; transition: transform 0.15s, box-shadow 0.15s; }}
.paper-card:hover {{ transform: translateY(-2px); box-shadow: 0 4px 16px rgba(0,0,0,0.1); }}
.paper-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem; }}
.paper-num {{ font-size: 0.85rem; color: #888; font-weight: 600; }}
.paper-score {{ background: {accent}; color: white; padding: 0.2rem 0.7rem; border-radius: 20px; font-weight: 700; font-size: 0.9rem; }}
.paper-card h3 {{ font-size: 1.05rem; color: #1a1a2e; margin-bottom: 0.3rem; }}
.paper-card h3 a {{ color: #1a1a2e; text-decoration: none; }}
.paper-card h3 a:hover {{ color: {accent}; }}
.meta {{ font-size: 0.8rem; color: #888; margin-bottom: 0.8rem; }}
.section {{ margin-top: 0.8rem; }}
.section-label {{ font-weight: 700; font-size: 0.85rem; color: {accent}; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.3rem; border-bottom: 1px solid #e8edf3; padding-bottom: 0.2rem; }}
.section p {{ font-size: 0.92rem; color: #444; }}
.scores {{ display: flex; flex-wrap: wrap; gap: 0.4rem; margin-bottom: 0.4rem; }}
.score-badge {{ background: #e8edf3; color: {accent_dark}; padding: 0.15rem 0.6rem; border-radius: 12px; font-size: 0.78rem; font-weight: 600; }}
.verdict {{ font-style: normal; color: #444; font-size: 0.9rem; }}
.paper-fig {{ margin: 0.8rem 0; text-align: center; }}
.paper-fig img {{ max-width: min(100%, 600px); border: 1px solid #e0e0e0; border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }}
.paper-fig .fig-caption {{ font-size: 0.78rem; color: #888; margin-top: 0.3rem; font-style: italic; line-height: 1.4; }}
.excluded {{ background: #fff3cd; border-radius: 12px; padding: 1.2rem; margin-top: 1.5rem; }}
.excluded h3 {{ color: #856404; font-size: 1rem; margin-bottom: 0.5rem; }}
.excluded li {{ font-size: 0.85rem; color: #856404; margin: 0.3rem 0; }}
.credit {{ text-align: center; font-size: 0.8rem; color: #aaa; margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #e0e0e0; }}
.sort-bar {{ display: flex; gap: 0.5rem; margin-bottom: 1.2rem; flex-wrap: wrap; }}
.sort-btn {{ background: white; border: 1px solid {accent}; color: {accent}; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.8rem; cursor: pointer; font-weight: 600; }}
.sort-btn:hover, .sort-btn.active {{ background: {accent}; color: white; }}
.timeline-section {{ background: white; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }}
.timeline-section h2 {{ color: {accent_dark}; font-size: 1.1rem; margin-bottom: 1rem; }}
.timeline-summary {{ font-size: 0.9rem; color: #444; line-height: 1.6; }}
.timeline-summary p {{ margin: 0.5rem 0; }}
.topic-group {{ margin-bottom: 1rem; }}
.topic-header {{ background: #f5f5f5; border-radius: 12px; padding: 0.8rem 1.2rem; cursor: pointer; display: flex; align-items: center; gap: 0.8rem; border-left: 4px solid #999; user-select: none; transition: background 0.15s; }}
.topic-header:hover {{ background: #ebebeb; }}
.topic-name {{ font-weight: 700; font-size: 1rem; flex: 1; color: #444; }}
.topic-count {{ font-size: 0.8rem; color: #888; background: #e0e0e0; padding: 0.15rem 0.5rem; border-radius: 10px; }}
.topic-toggle {{ font-size: 0.8rem; color: #999; transition: transform 0.2s; }}
.topic-body {{ padding: 0.5rem 0 0 0; }}
.topic-body.collapsed {{ display: none; }}
.category-timeline {{ margin: 0.5rem 0 1rem; text-align: center; }}
.category-timeline img {{ max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }}
.category-summary {{ background: white; border-radius: 12px; padding: 1.2rem 1.5rem; margin-bottom: 1rem; box-shadow: 0 1px 4px rgba(0,0,0,0.06); font-size: 0.9rem; line-height: 1.7; color: #444; }}
.category-summary p {{ margin: 0.6rem 0; }}
.category-summary h4 {{ font-size: 0.95rem; color: {accent_dark}; margin: 0 0 0.4rem; }}
.category-summary .subcategory-list {{ margin: 0.6rem 0 0.2rem 1.2rem; padding: 0; }}
.category-summary .subcategory-list li {{ margin: 0.5rem 0; line-height: 1.6; }}
.category-summary .subcategory-list a {{ color: {accent}; text-decoration: none; font-weight: 500; }}
.category-summary .subcategory-list a:hover {{ text-decoration: underline; }}
.paper-date {{ font-size: 0.75rem; color: #999; }}
img.lazy {{ opacity: 0; transition: opacity 0.3s; }}
img.lazy.loaded {{ opacity: 1; }}
.search-box {{ background: white; border-radius: 12px; padding: 1rem 1.5rem; margin-bottom: 1.2rem; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }}
.search-box input {{ width: 100%; padding: 0.6rem 1rem; border: 2px solid #e0e0e0; border-radius: 8px; font-size: 0.95rem; font-family: inherit; outline: none; transition: border-color 0.2s; }}
.search-box input:focus {{ border-color: {accent}; }}
.search-box .search-hint {{ font-size: 0.75rem; color: #aaa; margin-top: 0.3rem; }}
.search-box .search-count {{ font-size: 0.8rem; color: {accent}; font-weight: 600; margin-top: 0.3rem; display: none; }}
.lightbox {{ display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); z-index: 9999; cursor: zoom-out; align-items: center; justify-content: center; }}
.lightbox.active {{ display: flex; }}
.lightbox img {{ max-width: 95%; max-height: 95%; object-fit: contain; border-radius: 8px; }}
.paper-fig img, .category-timeline img, .timeline-section img {{ cursor: zoom-in; }}"""

JS = """function toggleTopic(id) {
  const body = document.getElementById(id);
  const toggle = document.getElementById('toggle-' + id);
  body.classList.toggle('collapsed');
  toggle.textContent = body.classList.contains('collapsed') ? '\\u25B6' : '\\u25BC';
  if (!body.classList.contains('collapsed')) setTimeout(lazyLoad, 100);
}
function sortCards(key, order) {
  document.querySelectorAll('.topic-body').forEach(body => {
    const cards = [...body.querySelectorAll('.paper-card')];
    cards.sort((a, b) => {
      let va, vb;
      if (key === 'date') { va = a.dataset.date || ''; vb = b.dataset.date || ''; }
      else { va = parseFloat(a.dataset.score) || 0; vb = parseFloat(b.dataset.score) || 0; }
      if (order === 'asc') return va > vb ? 1 : va < vb ? -1 : 0;
      return va < vb ? 1 : va > vb ? -1 : 0;
    });
    cards.forEach(c => body.appendChild(c));
  });
  document.querySelectorAll('.sort-btn').forEach(b => b.classList.remove('active'));
  event.target.classList.add('active');
  setTimeout(lazyLoad, 100);
}
function lazyLoad() {
  const imgs = document.querySelectorAll('img.lazy:not(.loaded)');
  if ('IntersectionObserver' in window) {
    const obs = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          const img = e.target; img.src = img.dataset.src;
          img.classList.add('loaded'); obs.unobserve(img);
        }
      });
    }, {rootMargin: '200px'});
    imgs.forEach(img => obs.observe(img));
  } else { imgs.forEach(img => { img.src = img.dataset.src; img.classList.add('loaded'); }); }
}
document.addEventListener('DOMContentLoaded', lazyLoad);

// Search
function searchPapers(query) {
  const q = query.trim().toLowerCase();
  const groups = document.querySelectorAll('.topic-group');
  const countEl = document.querySelector('.search-count');
  if (!q) {
    groups.forEach(g => { g.style.display = '';
      g.querySelectorAll('.paper-card').forEach(c => c.style.display = '');
      const body = g.querySelector('.topic-body');
      if (body) { body.classList.add('collapsed'); }
      const toggle = g.querySelector('.topic-toggle');
      if (toggle) toggle.textContent = '\\u25B6';
    });
    if (countEl) countEl.style.display = 'none';
    return;
  }
  let total = 0;
  groups.forEach(g => {
    const cards = g.querySelectorAll('.paper-card');
    let matched = 0;
    cards.forEach(c => {
      const text = c.textContent.toLowerCase();
      if (text.includes(q)) { c.style.display = ''; matched++; }
      else { c.style.display = 'none'; }
    });
    if (matched > 0) {
      g.style.display = '';
      // Keep collapsed — just update count badge
      const badge = g.querySelector('.topic-count');
      if (badge) badge.textContent = matched + '\\ud3b8';
      total += matched;
    } else {
      g.style.display = 'none';
    }
  });
  if (countEl) { countEl.textContent = total + ' results'; countEl.style.display = 'block'; }
  setTimeout(lazyLoad, 100);
}
let searchTimer;
document.addEventListener('DOMContentLoaded', function() {
  const input = document.getElementById('search-input');
  if (input) input.addEventListener('input', function() {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(() => searchPapers(this.value), 300);
  });
});

// Lightbox
document.addEventListener('DOMContentLoaded', function() {
  const lb = document.getElementById('lightbox');
  const lbImg = document.getElementById('lightbox-img');
  if (!lb || !lbImg) return;
  document.addEventListener('click', function(e) {
    const img = e.target.closest('.paper-fig img, .category-timeline img, .timeline-section img');
    if (img) {
      const src = img.dataset.src || img.src;
      if (src) { lbImg.src = src; lb.classList.add('active'); }
    }
  });
  lb.addEventListener('click', function() { lb.classList.remove('active'); lbImg.src = ''; });
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && lb.classList.contains('active')) { lb.classList.remove('active'); lbImg.src = ''; }
  });
});"""

# Build topic groups
topic_groups_parts = []
global_num = 1
for cat_idx, cat_name in enumerate(cat_order):
    papers = cat_papers.get(cat_name, [])
    if not papers:
        continue
    topic_id = f"topic-{cat_idx}"
    cat_slug = cat_name.replace(" ", "_").replace("&", "and")
    narr_html = render_category_narrative(cat_name)

    # Category timeline image (in topic dir)
    cat_tl_file = f"category_timeline_{cat_slug}.png"
    cat_tl_exists = os.path.exists(os.path.join(TOPIC_DIR, cat_tl_file))
    cat_tl_html = ""
    if cat_tl_exists:
        cat_tl_html = (
            f'\n<div class="category-timeline">'
            f'<img data-src="{cat_tl_file}" alt="{esc(cat_name)} Timeline" class="lazy">'
            f'</div>'
        )

    summary_block = ""
    if narr_html or cat_tl_html:
        summary_block = f'\n<div class="category-summary">{cat_tl_html}{narr_html}</div>'

    cards_parts = []
    for paper in papers:
        cards_parts.append(render_paper_card(paper, global_num, cat_slug))
        global_num += 1

    group = (
        f'<div class="topic-group" data-topic="{esc(cat_name)}">\n'
        f'      <div class="topic-header" onclick="toggleTopic(\'{topic_id}\')">\n'
        f'        <span class="topic-name">{esc(cat_name)}</span>\n'
        f'        <span class="topic-count">{len(papers)}\ud3b8</span>\n'
        f'        <span class="topic-toggle" id="toggle-{topic_id}">&#x25B6;</span>\n'
        f'      </div>\n'
        f'      <div class="topic-body collapsed" id="{topic_id}">{summary_block}\n'
        + "\n".join(cards_parts) + "\n"
        + '      </div>\n'
        + '    </div>'
    )
    topic_groups_parts.append(group)

exec_html = render_exec_summary(executive_summary)
num_cats = len([c for c in cat_order if cat_papers.get(c)])

# Determine date range
dates = [p.get("date", "") for cat in cat_papers.values() for p in cat]
dates = [d for d in dates if d]
date_range = f"{min(dates)} ~ {max(dates)}" if dates else ""

# Research timeline
has_research_tl = os.path.exists(os.path.join(TOPIC_DIR, "research_timeline.png"))
research_tl_html = ""
if has_research_tl:
    research_tl_html = (
        '<div class="timeline-section">\n'
        '  <h2>Research Timeline</h2>\n'
        '  <div style="text-align:center;margin:1rem 0">'
        '<img src="research_timeline.png" alt="Research Timeline"'
        ' style="max-width:100%;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,0.1)">'
        '</div>\n'
    )
    if exec_html:
        research_tl_html += f'  <div class="timeline-summary">\n    {exec_html}\n  </div>\n'
    research_tl_html += '</div>\n\n\n'

HTML = (
    '<!DOCTYPE html>\n'
    '<html lang="ko">\n'
    '<head>\n'
    '<meta charset="UTF-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1.0">\n'
    f'<title>{esc(theme["title"])} &#8212; {total_papers} Papers</title>\n'
    '<link rel="stylesheet" href="https://cdn.jsdelivr.net/font-kopub/1.0/kopubdotum.css">\n'
    '<script>window.MathJax={tex:{inlineMath:[[\'$\',\'$\'],[\'\\\\(\',\'\\\\)\']],displayMath:[[\'$$\',\'$$\'],[\'\\\\[\',\'\\\\]\']]}};</script>\n'
    '<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>\n'
    f'<style>\n{CSS}\n</style>\n'
    '</head>\n'
    '<body>\n'
    '<div class="container">\n'
    '  <div class="hero">\n'
    f'    <h1>{esc(theme["title"])} &#8212; {total_papers} Papers</h1>\n'
    '    <div class="stats">\n'
    f'      <div class="stat"><div class="stat-num">{total_papers}</div><div class="stat-label">\ub9ac\ubdf0 \uc644\ub8cc</div></div>\n'
    f'      <div class="stat"><div class="stat-num">{num_cats}</div><div class="stat-label">MECE \uce74\ud14c\uace0\ub9ac</div></div>\n'
    f'      <div class="stat"><div class="stat-num">{TODAY}</div><div class="stat-label">\ud050\ub808\uc774\uc158 \uc77c\uc790</div></div>\n'
    '    </div>\n'
    '  </div>\n\n\n'
    + research_tl_html
    + '  <div class="search-box">\n'
    '    <input type="text" id="search-input" placeholder="Search papers by title, DOI, keyword...">\n'
    '    <div class="search-hint">Enter title, DOI, author name, or keyword to filter</div>\n'
    '    <div class="search-count" id="search-count"></div>\n'
    '  </div>\n\n'
    + '  <div class="sort-bar">\n'
    '    <button class="sort-btn" onclick="sortCards(\'date\',\'asc\')">\ucd9c\ud310\uc77c &#x25B2;</button>\n'
    '    <button class="sort-btn" onclick="sortCards(\'date\',\'desc\')">\ucd9c\ud310\uc77c &#x25BC;</button>\n'
    '    <button class="sort-btn" onclick="sortCards(\'score\',\'asc\')">\ud3c9\uc810 &#x25B2;</button>\n'
    '    <button class="sort-btn" onclick="sortCards(\'score\',\'desc\')">\ud3c9\uc810 &#x25BC;</button>\n'
    '  </div>\n\n'
    '  <div id="cards">\n\n'
    + "\n\n".join(topic_groups_parts) + "\n\n"
    + '  </div>\n'
    '  <div class="credit">\n'
    f'    Generated by Claude Code &middot; {esc(theme["title"])} Paper Curation &middot; {TODAY}\n'
    '  </div>\n\n'
    '</div>\n\n'
    '<div id="lightbox" class="lightbox"><img id="lightbox-img" alt=""></div>\n\n'
    f'<script>\n{JS}\n</script>\n\n'
    '</body>\n</html>'
)

out_path = os.path.join(TOPIC_DIR, "index.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"Written: {out_path} ({len(HTML):,} chars)")

# Verify no old-style paths
old_paths = re.findall(r'(?:href|src)="(\d{3}_[^"]*)"', HTML)
if old_paths:
    print(f"WARNING: {len(old_paths)} old-style paths found (should use ../papers/ prefix):")
    for p in old_paths[:5]:
        print(f"  {p}")
else:
    print("OK: All paths use ../papers/ prefix")
