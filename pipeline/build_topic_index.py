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

from collections import OrderedDict
from config_loader import PAPERS_DIR as _PAPERS_DIR, get_topic_dir
from lib.categories import category_slug
PAPERS_DIR = str(_PAPERS_DIR)

def get_topic():
    if len(sys.argv) > 1:
        return sys.argv[1]
    return "ai4s"

TOPIC = get_topic()
TOPIC_DIR = str(get_topic_dir(TOPIC))

# Theme colors per topic (title from config.json Zotero collection name)
from config_loader import load_config
_collections_raw = load_config().get("zotero", {}).get("collections", {})

THEME = {
    "ai4s": {
        "gradient": "linear-gradient(135deg, #2a0f0d 0%, #5c1a14 50%, #A62018 100%)",
        "accent": "#D63423", "accent_dark": "#A62018", "accent_light": "#F06050",
    },
    "scisci": {
        "gradient": "linear-gradient(135deg, #0d1a2a 0%, #14385c 50%, #1866A6 100%)",
        "accent": "#2374D6", "accent_dark": "#1856A0", "accent_light": "#50A0F0",
    },
}
# Default theme for unknown topics
_default_theme = {
    "gradient": "linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%)",
    "accent": "#3B82F6", "accent_dark": "#2563EB", "accent_light": "#60A5FA",
}
theme = THEME.get(TOPIC, _default_theme)
# Title from Zotero collection name in config.json
_collection_name = _collections_raw.get(TOPIC, TOPIC)
theme["title"] = _collection_name
theme["subtitle_prefix"] = _collection_name

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
    # Fallback: extract categories from classifications[TOPIC] in _papers_index.json
    _cat_names = set()
    for p in papers_index:
        cls = p.get("classifications", {}).get(TOPIC, {})
        for c in cls.get("all_categories", []):
            _cat_names.add(c)
        if cls.get("primary_category"):
            _cat_names.add(cls["primary_category"])
    categories = [{"name": c} for c in sorted(_cat_names)] if _cat_names else []
    assignments = []

if os.path.exists(narr_path):
    with open(narr_path, encoding="utf-8") as f:
        narrative = json.load(f)
    category_analyses = narrative.get("category_analyses", {})
    executive_summary = narrative.get("executive_summary_ko", "")
else:
    category_analyses = {}
    executive_summary = ""

# Load insights
insights_path = os.path.join(TOPIC_DIR, "_insights.json")
if os.path.exists(insights_path):
    with open(insights_path, encoding="utf-8") as f:
        insights_data = json.load(f)
else:
    insights_data = {}

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
        # sub_themes from _category_summaries.json always wins (has description_ko)
        if cs.get("sub_themes"):
            category_analyses[cat_name_cs]["sub_themes"] = cs["sub_themes"]

# Filter papers for this topic
topic_papers = [p for p in papers_index if TOPIC in p.get("topics", [])]
slug_to_index = {p["slug"]: p for p in topic_papers}

# Assignment slug → category mapping (multi-class)
# Priority: 1) classifications[TOPIC] in papers_index, 2) _new_classification.json assignments
slug_to_cat = {}       # slug → primary_category (str)
slug_to_all_cats = {}  # slug → all_categories (list)

# From _new_classification.json (legacy, lower priority)
for a in assignments:
    slug_to_cat[a["slug"]] = a.get("primary_category", "Other")
    slug_to_all_cats[a["slug"]] = a.get("all_categories", [a.get("primary_category", "Other")])

# From classifications[TOPIC] in papers_index (higher priority, overrides)
for p in topic_papers:
    cls = p.get("classifications", {}).get(TOPIC, {})
    if cls.get("primary_category"):
        slug_to_cat[p["slug"]] = cls["primary_category"]
        slug_to_all_cats[p["slug"]] = cls.get("all_categories", [cls["primary_category"]])

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
    num = slug.split("_")[0] if "_" in slug else slug[:4]
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

from lib.dateutil import normalize_date

# Build category → papers mapping
cat_order = [c["name"] for c in categories] if categories else ["Other"]
cat_papers = defaultdict(list)
unmatched = []

for p_idx in topic_papers:
    slug = p_idx["slug"]
    p_cls = p_idx.get("classifications", {}).get(TOPIC, {})
    all_cats = slug_to_all_cats.get(slug, p_cls.get("all_categories", [p_cls.get("primary_category", "Other")]))
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
    has_fig = (os.path.exists(os.path.join(PAPERS_DIR, dir_name, "figures", "fig1.webp"))
               or os.path.exists(os.path.join(PAPERS_DIR, dir_name, "figures", "fig1.png")))
    # Extract fig1 caption from pdffigures2 JSON or review.md
    fig_caption = ""
    pf2_dir = os.path.join(PAPERS_DIR, dir_name, "figures", "pdffigures2")
    pf2_json = None
    if os.path.isdir(pf2_dir):
        pf2_jsons = [f for f in os.listdir(pf2_dir) if f.endswith(".json")]
        if pf2_jsons:
            pf2_json = os.path.join(pf2_dir, pf2_jsons[0])
    if pf2_json and pf2_json.endswith(".json"):
        try:
            with open(pf2_json, "r", encoding="utf-8") as _f:
                figs_meta = json.load(_f)
            if figs_meta and isinstance(figs_meta, list):
                fig_caption = figs_meta[0].get("caption", "")
        except Exception as e:
            print(f"WARNING: pdffigures2 parse failed for {dir_name}: {e}")
    if not fig_caption:
        # Fallback: extract from review.md (line after ![Figure 1])
        md_path = os.path.join(PAPERS_DIR, dir_name, "review.md")
        if os.path.exists(md_path):
            with open(md_path, "r", encoding="utf-8") as _f:
                md_text = _f.read()
            cap_m = re.search(r'!\[.*?\]\(figures/fig1.*?\)\s*\n+\*(.+?)\*', md_text)
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
        "fig_src": (f"../papers/{dir_name}/figures/fig1.webp" if os.path.exists(os.path.join(PAPERS_DIR, dir_name, "figures", "fig1.webp"))
                    else f"../papers/{dir_name}/figures/fig1.png") if has_fig else None,
        "fig_caption": fig_caption,
    }
    # Multi-class: add to ALL matching categories, with per-category sub_category
    sub_categories_map = p_cls.get("sub_categories", {})
    for cat in all_cats:
        if cat in cat_order or cat == "Other":
            card = dict(paper_data)
            card["sub_category"] = sub_categories_map.get(cat, p_cls.get("sub_category", "General") if cat == p_cls.get("primary_category") else "General")
            cat_papers[cat].append(card)

if unmatched:
    print(f"WARNING unmatched: {unmatched}")
for cat in cat_papers:
    cat_papers[cat].sort(key=lambda p: p["overall_score"], reverse=True)
total_cards = sum(len(v) for v in cat_papers.values())
unique_papers = len(topic_papers)
print(f"Total papers for {TOPIC}: {unique_papers} unique ({total_cards} cards with multi-class)")
for cn in cat_order:
    print(f"  {cn}: {len(cat_papers.get(cn, []))}")

# --- HTML Rendering ---

def esc(s):
    return escape(str(s)) if s else ""

def make_doi_link(doi, arxiv):
    if doi:
        # Skip invalid/empty values
        if doi in ('N/A', '[', ''):
            pass  # fall through to arxiv
        # Parse markdown link: [text](url)
        elif doi.startswith('['):
            md_m = re.match(r'\[([^\]]*)\]\((https?://[^)]+)\)', doi)
            if md_m:
                text, url = md_m.group(1), md_m.group(2)
                label = text if text else url
                return f'<a href="{esc(url)}" target="_blank">{esc(label)}</a>'
        elif doi.startswith("http"):
            return f'<a href="{esc(doi)}" target="_blank">{esc(doi)}</a>'
        elif re.match(r'10\.\d{4,}/', doi):
            return f'<a href="https://doi.org/{esc(doi)}" target="_blank">{esc(doi)}</a>'
        else:
            return esc(doi)
    if arxiv:
        aid = arxiv.strip()
        if aid.startswith("http"):
            arxiv_id = aid.rsplit('/', 1)[-1]
            return f'<a href="{esc(aid)}" target="_blank">arXiv:{esc(arxiv_id)}</a>'
        return f'<a href="https://arxiv.org/abs/{esc(aid)}" target="_blank">arXiv:{esc(aid)}</a>'
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


def validate_description(text, cat_name, sub_name=""):
    """카테고리/sub-category 설명 품질 검증."""
    issues = []
    label = f"{cat_name}/{sub_name}" if sub_name else cat_name

    if not text or len(text) < 50:
        issues.append(f"{label}: 설명 누락 또는 너무 짧음 ({len(text or '')}자)")
    elif len(text) < 150:
        issues.append(f"{label}: 설명 부실 ({len(text)}자, 최소 150자 권장)")

    if text:
        # [NNN] 리터럴 체크
        if "[NNN]" in text:
            issues.append(f"{label}: [NNN] 리터럴 남아있음")
        # 논문 제목 인라인 체크 (영문 20자 이상 따옴표)
        quoted = re.findall(r"['\"][A-Z][^'\"]{20,}['\"]", text)
        if quoted:
            issues.append(f"{label}: 논문 제목 인라인 ({quoted[0][:40]}...)")
        # 한국어 비율 체크
        korean = len(re.findall(r'[\uac00-\ud7af]', text))
        if korean < len(text) * 0.3:
            issues.append(f"{label}: 한국어 비율 낮음 ({korean}/{len(text)})")
        # 마침표 종료
        if text.strip() and text.strip()[-1] not in ".다":
            issues.append(f"{label}: 마침표로 끝나지 않음 ('{text.strip()[-5:]}')")

    return issues


def render_category_narrative(cat_name):
    ca = category_analyses.get(cat_name, {})
    if not ca: return ""
    overview = ca.get("description", "")
    sub_themes = ca.get("sub_themes", [])
    cat_papers = ca.get("papers", [])
    html_parts = []

    # Build slug number → paper info lookup from ALL papers (not just top 20)
    num_to_paper = {}
    for p in papers_index:
        slug = p.get("slug", "")
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
            # Try zero-padded: "87" → "087", "9" → "009"
            padded = num.zfill(3)
            if padded in num_to_paper:
                slug, title = num_to_paper[padded]
                return f'<a href="../papers/{esc(slug)}/index.html" title="{esc(title)}">[{num}]</a>'
            return m.group(0)
        return re.sub(r'\[(\d{1,4})\]', _repl, text_html)

    # Category Overview (한글 우선)
    overview_ko = ca.get("description_ko", "")
    if overview_ko:
        overview_html = _refs_to_links(esc(overview_ko))
        html_parts.append(f'<h4>Category Overview</h4>\n<p>{overview_html}</p>')
    elif overview:
        html_parts.append(f'<h4>Category Overview</h4>\n<p>{esc(overview)}</p>')

    # Sub-category bullets — description_ko directly from sub_themes
    if sub_themes:
        html_parts.append('<ul class="subcategory-list">')
        for st in sub_themes:
            name = st.get("name", "")
            desc = st.get("description_ko", "") or st.get("description", "")
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
.sub-group {{ margin: 0.5rem 0; }}
.sub-header {{ background: #fafafa; border-radius: 8px; padding: 0.5rem 1rem; cursor: pointer; display: flex; align-items: center; gap: 0.6rem; border-left: 3px solid {accent_light}; user-select: none; transition: background 0.15s; }}
.sub-header:hover {{ background: #f0f0f0; }}
.sub-name {{ font-weight: 600; font-size: 0.9rem; flex: 1; color: #555; }}
.sub-count {{ font-size: 0.75rem; color: #999; background: #e8e8e8; padding: 0.1rem 0.4rem; border-radius: 8px; }}
.sub-toggle {{ font-size: 0.7rem; color: #bbb; transition: transform 0.2s; }}
.sub-body {{ padding: 0 0 0 0.5rem; }}
.sub-body.collapsed {{ display: none; }}
.category-summary p {{ margin: 0.6rem 0; }}
.category-summary h4 {{ font-size: 0.95rem; color: {accent_dark}; margin: 0 0 0.4rem; }}
.category-summary .subcategory-list {{ margin: 0.6rem 0 0.2rem 1.2rem; padding: 0; }}
.category-summary .subcategory-list li {{ margin: 0.5rem 0; line-height: 1.6; }}
.category-summary a {{ color: #2563EB; text-decoration: none; font-weight: 500; }}
.category-summary a:hover {{ text-decoration: underline; }}
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
.paper-fig img, .category-timeline img, .timeline-section img {{ cursor: zoom-in; }}
.insights-section {{ background: white; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }}
.insights-section h2 {{ color: {accent_dark}; font-size: 1.1rem; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem; }}
.insights-section .insight-count {{ font-size: 0.8rem; color: #888; font-weight: 400; }}
.insight-card {{ border-left: 4px solid #999; border-radius: 0 8px 8px 0; padding: 1rem 1.2rem; margin-bottom: 0.8rem; background: #fafafa; }}
.insight-card.convergence {{ border-left-color: #7C3AED; background: #FAF5FF; }}
.insight-card.gap {{ border-left-color: #F59E0B; background: #FFFBEB; }}
.insight-card.emerging {{ border-left-color: #10B981; background: #F0FDF4; }}
.insight-card.declining {{ border-left-color: #9CA3AF; background: #F9FAFB; }}
.insight-type {{ font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.3rem; }}
.convergence .insight-type {{ color: #7C3AED; }}
.gap .insight-type {{ color: #D97706; }}
.emerging .insight-type {{ color: #059669; }}
.declining .insight-type {{ color: #6B7280; }}
.insight-title {{ font-size: 1rem; font-weight: 700; color: #1a1a2e; margin-bottom: 0.4rem; }}
.insight-desc {{ font-size: 0.9rem; color: #444; line-height: 1.6; margin-bottom: 0.5rem; }}
.insight-meta {{ font-size: 0.8rem; color: #888; display: flex; flex-wrap: wrap; gap: 0.8rem; }}
.insight-meta .cats {{ color: {accent}; }}
.insight-meta .evidence a {{ color: #2563EB; text-decoration: none; font-weight: 500; }}
.insight-meta .evidence a:hover {{ text-decoration: underline; }}
.insight-policy {{ font-size: 0.85rem; color: #4B5563; margin-top: 0.4rem; padding: 0.4rem 0.6rem; background: rgba(0,0,0,0.03); border-radius: 4px; }}
.cat-insight {{ background: #f8f9fa; border-radius: 8px; padding: 0.8rem 1rem; margin-top: 0.8rem; font-size: 0.88rem; line-height: 1.6; }}
.cat-insight .ci-label {{ font-weight: 600; color: {accent_dark}; margin-right: 0.3rem; }}
.cat-insight .ci-gap {{ color: #D97706; }}
.cat-insight .ci-policy {{ color: #4B5563; }}"""

JS = """function toggleTopic(id) {
  const body = document.getElementById(id);
  const toggle = document.getElementById('toggle-' + id);
  body.classList.toggle('collapsed');
  toggle.textContent = body.classList.contains('collapsed') ? '\\u25B6' : '\\u25BC';
  if (!body.classList.contains('collapsed')) setTimeout(lazyLoad, 100);
}
function toggleSub(id) {
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
    let catMatched = 0;
    const subs = g.querySelectorAll('.sub-group');
    if (subs.length > 0) {
      subs.forEach(sg => {
        const cards = sg.querySelectorAll('.paper-card');
        let subMatched = 0;
        cards.forEach(c => {
          const text = c.textContent.toLowerCase();
          if (text.includes(q)) { c.style.display = ''; subMatched++; }
          else { c.style.display = 'none'; }
        });
        if (subMatched > 0) {
          sg.style.display = '';
          const subBadge = sg.querySelector('.sub-count');
          if (subBadge) subBadge.textContent = subMatched;
        } else {
          sg.style.display = 'none';
        }
        // Keep sub-category collapsed — user clicks to expand
        const subBody = sg.querySelector('.sub-body');
        if (subBody) subBody.classList.add('collapsed');
        const subToggle = sg.querySelector('.sub-toggle');
        if (subToggle) subToggle.textContent = '\\u25B6';
        catMatched += subMatched;
      });
    } else {
      g.querySelectorAll('.paper-card').forEach(c => {
        const text = c.textContent.toLowerCase();
        if (text.includes(q)) { c.style.display = ''; catMatched++; }
        else { c.style.display = 'none'; }
      });
    }
    if (catMatched > 0) {
      g.style.display = '';
      // Keep category collapsed — only update count badge
      const body = g.querySelector('.topic-body');
      if (body) body.classList.add('collapsed');
      const toggle = g.querySelector('.topic-toggle');
      if (toggle) toggle.textContent = '\\u25B6';
      const badge = g.querySelector('.topic-count');
      if (badge) badge.textContent = catMatched + '\\ud3b8';
      total += catMatched;
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


def render_insights_section():
    """_insights.json에서 cross-category insights 렌더링."""
    cross = insights_data.get("cross_category", [])
    if not cross:
        return ""

    # Build slug number → paper info lookup
    num_to_paper = {}
    for p in papers_index:
        slug = p.get("slug", "")
        title = p.get("title", "")
        num = slug.split("_")[0] if "_" in slug else slug[:3]
        num_to_paper[num] = (slug, title)

    type_labels = {
        "convergence": "융합",
        "gap": "연구 갭",
        "emerging": "신흥 트렌드",
        "declining": "감소 추세",
    }

    cards = []
    for ins in cross:
        itype = ins.get("type", "gap")
        label = type_labels.get(itype, itype)
        title = escape(ins.get("title", ""))
        desc = escape(ins.get("description", ""))
        cats = ins.get("categories", [])
        evidence = ins.get("evidence", [])
        policy = ins.get("policy_implication", "")

        cats_html = " · ".join(escape(c) for c in cats)
        ev_links = []
        for num in evidence:
            matched = num_to_paper.get(num) or num_to_paper.get(str(num).zfill(3))
            if matched:
                slug, ptitle = matched
                ev_links.append(
                    f'<a href="../papers/{escape(slug)}/index.html" title="{escape(ptitle)}">[{num}]</a>'
                )
            else:
                ev_links.append(f"[{num}]")
        ev_html = " ".join(ev_links)

        policy_html = ""
        if policy:
            policy_html = f'\n      <div class="insight-policy">&#x1F3DB; {escape(policy)}</div>'

        cards.append(
            f'    <div class="insight-card {itype}">\n'
            f'      <div class="insight-type">{label}</div>\n'
            f'      <div class="insight-title">{title}</div>\n'
            f'      <div class="insight-desc">{desc}</div>\n'
            f'      <div class="insight-meta">\n'
            f'        <span class="cats">{cats_html}</span>\n'
            f'        <span class="evidence">{ev_html}</span>\n'
            f'      </div>{policy_html}\n'
            f'    </div>'
        )

    return (
        '<div class="insights-section">\n'
        f'  <h2>Research Insights <span class="insight-count">{len(cross)} findings</span></h2>\n'
        + "\n".join(cards) + "\n"
        + '</div>\n\n'
    )


def render_category_insight(cat_name):
    """per_category insight를 카테고리 summary에 삽입할 HTML 반환."""
    per_cat = insights_data.get("per_category", {}).get(cat_name, {})
    if not per_cat:
        return ""
    parts = []
    kf = per_cat.get("key_finding", "")
    gap = per_cat.get("gap", "")
    pi = per_cat.get("policy_implication", "")
    if kf:
        parts.append(f'<span class="ci-label">&#x1F4CC; 핵심:</span> {escape(kf)}')
    if gap:
        parts.append(f'<span class="ci-label ci-gap">&#x26A0; 갭:</span> {escape(gap)}')
    if pi:
        parts.append(f'<span class="ci-label ci-policy">&#x1F3DB; 정책:</span> {escape(pi)}')
    if not parts:
        return ""
    return '<div class="cat-insight">' + "<br>".join(parts) + '</div>'


# Build topic groups
topic_groups_parts = []
global_num = 1
for cat_idx, cat_name in enumerate(cat_order):
    papers = cat_papers.get(cat_name, [])
    if not papers:
        continue
    topic_id = f"topic-{cat_idx}"
    cat_slug = category_slug(cat_name)
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

    cat_insight_html = render_category_insight(cat_name)
    summary_block = ""
    if narr_html or cat_tl_html or cat_insight_html:
        summary_block = f'\n<div class="category-summary">{cat_tl_html}{narr_html}{cat_insight_html}</div>'

    # Group papers by sub_category (if >30 papers in category)
    if len(papers) > 30:
        sub_groups = OrderedDict()
        for paper in papers:
            sc = paper.get("sub_category", "General")
            if sc not in sub_groups:
                sub_groups[sc] = []
            sub_groups[sc].append(paper)

        # Merge small sub-categories (<3 papers) into "Others"
        small = [k for k, v in sub_groups.items() if len(v) < 3 and k != "Others"]
        if small:
            others = sub_groups.pop("Others", [])
            for k in small:
                others.extend(sub_groups.pop(k))
            if others:
                sub_groups["Others"] = others

        cards_html = ""
        for sc_idx, (sc_name, sc_papers) in enumerate(sub_groups.items()):
            sc_id = f"{topic_id}-sub-{sc_idx}"
            sc_cards = []
            for paper in sc_papers:
                sc_cards.append(render_paper_card(paper, global_num, cat_slug))
                global_num += 1
            cards_html += (
                f'\n<div class="sub-group">'
                f'\n  <div class="sub-header" onclick="toggleSub(\'{sc_id}\')">'
                f'\n    <span class="sub-name">{esc(sc_name)}</span>'
                f'\n    <span class="sub-count">{len(sc_papers)}</span>'
                f'\n    <span class="sub-toggle" id="toggle-{sc_id}">&#x25B6;</span>'
                f'\n  </div>'
                f'\n  <div class="sub-body collapsed" id="{sc_id}">'
                + "\n".join(sc_cards)
                + '\n  </div>'
                + '\n</div>'
            )
    else:
        cards_html = ""
        for paper in papers:
            cards_html += render_paper_card(paper, global_num, cat_slug)
            global_num += 1

    group = (
        f'<div class="topic-group" data-topic="{esc(cat_name)}">\n'
        f'      <div class="topic-header" onclick="toggleTopic(\'{topic_id}\')">\n'
        f'        <span class="topic-name">{esc(cat_name)}</span>\n'
        f'        <span class="topic-count">{len(papers)}\ud3b8</span>\n'
        f'        <span class="topic-toggle" id="toggle-{topic_id}">&#x25B6;</span>\n'
        f'      </div>\n'
        f'      <div class="topic-body collapsed" id="{topic_id}">{summary_block}\n'
        + cards_html + "\n"
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
    if os.path.exists(os.path.join(TOPIC_DIR, "network.html")):
        research_tl_html += f'  <div style="text-align:right;margin-top:0.8rem"><a href="network.html" style="color:{accent};font-weight:600;text-decoration:none;font-size:0.9rem">&#x1F517; Interactive Paper Network &rarr;</a></div>\n'
    research_tl_html += '</div>\n\n\n'

HTML = (
    '<!DOCTYPE html>\n'
    '<html lang="ko">\n'
    '<head>\n'
    '<meta charset="UTF-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1.0">\n'
    f'<title>{esc(theme["title"])} &#8212; Paper Curation</title>\n'
    '<link rel="stylesheet" href="https://cdn.jsdelivr.net/font-kopub/1.0/kopubdotum.css">\n'
    '<script>window.MathJax={tex:{inlineMath:[[\'$\',\'$\'],[\'\\\\(\',\'\\\\)\']],displayMath:[[\'$$\',\'$$\'],[\'\\\\[\',\'\\\\]\']]}};</script>\n'
    '<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>\n'
    f'<style>\n{CSS}\n</style>\n'
    '</head>\n'
    '<body>\n'
    '<div class="container">\n'
    '  <div class="hero">\n'
    f'    <h1>{esc(theme["title"])} &#8212; Paper Curation</h1>\n'
    '    <div class="stats">\n'
    f'      <div class="stat"><div class="stat-num">{unique_papers}</div><div class="stat-label">\ub9ac\ubdf0 \uc644\ub8cc</div></div>\n'
    f'      <div class="stat"><div class="stat-num">{num_cats}</div><div class="stat-label">MECE \uce74\ud14c\uace0\ub9ac</div></div>\n'
    f'      <div class="stat"><div class="stat-num">{TODAY}</div><div class="stat-label">\ud050\ub808\uc774\uc158 \uc77c\uc790</div></div>\n'
    '    </div>\n'
    '  </div>\n\n\n'
    + research_tl_html
    + render_insights_section()
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
    '<footer style="text-align:center;padding:2rem 0 1rem;color:#999;font-size:0.85rem;border-top:1px solid #eee;margin-top:3rem;">'
    'Developed by Jehyun Lee, KIST AIX Strategy Department | jehyun.lee@gmail.com'
    '</footer>\n\n'
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

# Validate category/sub-category descriptions
print("\n=== Description Quality Check ===")
all_issues = []
for ca_name, ca_data in category_analyses.items():
    # Validate overview
    overview = ca_data.get("description_ko", "")
    all_issues.extend(validate_description(overview, ca_name))
    # Validate sub-theme descriptions
    raw_stko = ca_data.get("sub_themes_ko", [])
    if isinstance(raw_stko, list):
        for st in raw_stko:
            if isinstance(st, dict):
                all_issues.extend(validate_description(
                    st.get("description_ko", ""), ca_name, st.get("name", "")))
    elif isinstance(raw_stko, dict):
        for k, v in raw_stko.items():
            all_issues.extend(validate_description(v, ca_name, k))

if all_issues:
    print(f"WARNING: {len(all_issues)} issues found:")
    for issue in all_issues:
        print(f"  - {issue}")
else:
    print("OK: All descriptions pass quality check")
