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
from pathlib import Path

KST = timezone(timedelta(hours=9))
TODAY = datetime.now(KST).strftime("%Y-%m-%d")

from collections import OrderedDict
from config_loader import PAPERS_DIR as _PAPERS_DIR, DOCS_DIR, get_topic_dir, get_zotero_api_key, get_zotero_user_id
from lib.categories import category_slug
from lib.audio_overview import (
    get_audio_css as _audio_css,
    audio_modal_html as _audio_modal,
    audio_script_block as _audio_script,
)
PAPERS_DIR = str(_PAPERS_DIR)

from lib import license_util as _lic


def _is_deploy_topic(topic):
    """True unless the topic is excluded from Cloudflare via docs/.assetsignore."""
    docs = os.path.dirname(PAPERS_DIR)
    try:
        for raw in open(os.path.join(docs, ".assetsignore"), encoding="utf-8"):
            s = raw.strip().rstrip("/")
            if s and not s.startswith("#") and "/" not in s and s == topic:
                return False
    except Exception:
        pass
    return True

def get_topic():
    if len(sys.argv) > 1:
        return sys.argv[1]
    return "ai4s"


def _run_topic_index(topic=None, cross=None):
    """Build {topic}/index.html (cards + Deep Research UI).

    Phase 5 refactor: module-level code was wrapped into this
    function so the script is importable without side-effects.
    Pass ``topic`` explicitly; falls back to ``sys.argv[1]``.
    """
    TOPIC = topic if topic is not None else get_topic()
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
    if cross:
        theme = {
            "gradient": "linear-gradient(135deg, #1a0d2a 0%, #3a1a5c 50%, #6b21a8 100%)",
            "accent": "#8B3FD6", "accent_dark": "#6B21A8", "accent_light": "#B57BF0",
        }
        theme["title"] = cross.get("title", "통합 Deep Research")
        theme["subtitle_prefix"] = theme["title"]

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
    if cross:
        topic_papers = []
    else:
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
            "license": p_idx.get("license", ""),
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
    if cross:
        unique_papers = cross.get("paper_count", unique_papers)
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

    # 게이팅은 배포 사본(PC_PUBLIC_BUILD=1)에서만 — 로컬 렌더는 항상 full
    _is_deploy = _is_deploy_topic(topic) and os.environ.get("PC_PUBLIC_BUILD") == "1"
    _fig_strict = os.environ.get("PC_FIGURE_POLICY", "") == "strict"
    _nd_suppress = os.environ.get("PC_ND_POLICY", "suppress") != "show"
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
        _cls = _lic.normalize(paper.get("license", ""))
        meta_parts.append(f'<strong>License</strong>: {esc(_lic.label(_cls))}')
        meta_html = " | ".join(meta_parts)
        badges = []
        for label, key in [("Novelty", "novelty"), ("Technical Soundness", "technical_soundness"),
                            ("Significance", "significance"), ("Clarity", "clarity")]:
            val = paper.get(key)
            if val is not None: badges.append(f'<span class="score-badge">{label}: {val}</span>')
        if score and score > 0: badges.append(f'<span class="score-badge">Overall: {int(score)}</span>')
        badges_html = " ".join(badges)
        _nd_public = _is_deploy and _lic.is_nd(_cls) and _nd_suppress
        fig_html = ""
        if paper["has_fig"]:
            cap = paper.get("fig_caption", "")
            cap_html = f'<p class="fig-caption">{esc(cap)}</p>' if cap else ""
            if _is_deploy and not _lic.figure_public_ok(_cls, strict=_fig_strict):
                fig_html = (
                    '\n          <div class="paper-fig">'
                    '<div class="fig-gated" style="padding:0.8rem;color:#999;font-size:0.8rem;">'
                    '&#128274; 원문 도표는 라이선스상 재현하지 않습니다</div>'
                    f'{cap_html}</div>'
                )
            else:
                fig_html = (
                    '\n          <div class="paper-fig">'
                    f'<img data-src="{esc(paper["fig_src"])}" alt="Figure" class="lazy">'
                    f'{cap_html}</div>'
                )
        essence_html = ""
        eval_html = ""
        if _nd_public:
            essence_html = (
                '\n          <div class="section">'
                '\n            <p style="color:#8a2a20;font-size:0.85rem;">'
                '&#128274; 변경금지(ND) 라이선스 — 2차적 저작물(AI 리뷰)의 공개가 제한됩니다. 원문을 확인하세요.</p>'
                '\n          </div>'
            )
        else:
            if paper["essence"]:
                essence_html = (
                    '\n          <div class="section">'
                    '\n            <div class="section-label">Essence</div>'
                    f'\n            <p>{esc(paper["essence"])}</p>'
                    '\n          </div>'
                )
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

        # Build slug number → paper info lookup. Prefer the CURRENT topic's
        # papers so a collision number (same slug number reused across
        # ingestion batches / merged repos) resolves to the paper that belongs
        # to THIS topic; fall back to the global map for numbers absent here.
        num_to_paper = {}
        for p in papers_index:                       # global fallback (legacy last-wins)
            slug = p.get("slug", "")
            title = p.get("title", "")
            num = slug.split("_")[0] if "_" in slug else slug[:3]
            num_to_paper[num] = (slug, title)
        for p in topic_papers:                        # topic-scoped overrides win
            slug = p.get("slug", "")
            title = p.get("title", "")
            num = slug.split("_")[0] if "_" in slug else slug[:3]
            num_to_paper[num] = (slug, title)
        # Category-primary override (highest precedence): resolves a SAME-topic
        # collision number to the paper whose PRIMARY category is the one being
        # rendered — the overview text of this category describes that paper.
        for p in topic_papers:
            cls = p.get("classifications", {}).get(TOPIC, {})
            pc = cls.get("primary_category") or slug_to_cat.get(p.get("slug", ""))
            if pc == cat_name:
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
            return re.sub(r'\[(\d+)\]', _repl, text_html)

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
        if not text:
            return ""
        paras = [p.strip() for p in text.split("\n\n") if p.strip()]

        def _render_para(paragraph):
            safe = esc(paragraph)
            return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", safe)

        return "\n    ".join(f"<p>{_render_para(p)}</p>" for p in paras)

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
    .insights-header {{ cursor: pointer; user-select: none; margin-bottom: 0 !important; }}
    .insights-header.open {{ margin-bottom: 1rem !important; }}
    .insights-body.collapsed {{ display: none; }}
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
    .cat-insight .ci-policy {{ color: #4B5563; }}
    /* ============ Deep Research ============ */
    .search-row {{ display: flex; gap: 0.5rem; align-items: stretch; }}
    .search-row input {{ flex: 1; }}
    .mode-toggle {{ display: flex; gap: 0; border: 2px solid #e0e0e0; border-radius: 8px; overflow: hidden; flex-shrink: 0; }}
    .mode-btn {{ background: white; border: none; padding: 0.5rem 0.9rem; font-size: 0.85rem; cursor: pointer; color: #888; transition: all 0.15s; font-family: inherit; }}
    .mode-btn.active {{ background: {accent}; color: white; }}
    .mode-btn:hover:not(.active) {{ background: #f5f5f5; color: {accent_dark}; }}
    .deep-panel {{ margin-top: 1rem; background: #fcfcfd; border: 1px solid #e5e5e5; border-radius: 10px; overflow: hidden; }}
    .deep-header {{ display: flex; align-items: center; gap: 0.8rem; padding: 0.7rem 1.1rem; background: linear-gradient(135deg, {accent}12, transparent); border-bottom: 1px solid #eee; flex-wrap: wrap; }}
    .deep-header h3 {{ font-size: 0.95rem; color: {accent_dark}; margin: 0; flex-shrink: 0; font-weight: 700; }}
    .deep-model {{ padding: 0.35rem 0.55rem; border: 1px solid #ddd; border-radius: 6px; font-size: 0.78rem; background: white; cursor: pointer; font-family: inherit; color: #444; }}
    .deep-actions {{ margin-left: auto; display: flex; gap: 0.35rem; flex-wrap: wrap; }}
    .deep-btn {{ background: white; border: 1px solid #ddd; border-radius: 6px; padding: 0.32rem 0.7rem; font-size: 0.76rem; cursor: pointer; color: #555; transition: all 0.15s; font-family: inherit; }}
    .deep-btn:hover:not(:disabled) {{ background: {accent}; color: white; border-color: {accent}; }}
    .deep-btn:disabled {{ opacity: 0.4; cursor: not-allowed; }}
    .deep-stop-btn {{ background: #fef3f2; border-color: #f0c2bd; color: #b33a3a; font-weight: 700; }}
    .deep-stop-btn:hover:not(:disabled) {{ background: #b33a3a; color: white; border-color: #b33a3a; }}
    .deep-status {{ padding: 0.55rem 1.1rem; font-size: 0.82rem; color: #555; background: #f7f9fb; border-bottom: 1px solid #eee; display: none; }}
    .deep-status.active {{ display: block; }}
    .deep-status.error {{ color: #b33a3a; background: #fef3f2; border-bottom-color: #fadcd9; }}
    .deep-plan {{ padding: 0.6rem 1.1rem; background: #f9fafb; border-bottom: 1px solid #eee; display: none; }}
    .deep-plan.active {{ display: block; }}
    .deep-plan-title {{ font-size: 0.78rem; font-weight: 700; color: {accent_dark}; margin-bottom: 0.35rem; }}
    .deep-sec-title {{ margin-top: 0.7rem; padding-top: 0.5rem; border-top: 1px dashed #e2e2e2; }}
    .deep-plan-list {{ margin: 0 0 0 1.3rem; font-size: 0.8rem; color: #555; line-height: 1.6; }}
    .deep-plan-list li {{ margin: 0.15rem 0; }}
    .deep-plan-list li .rstat {{ color: #aaa; font-size: 0.73rem; margin-left: 0.45rem; }}
    .deep-plan-list li.done .rstat {{ color: {accent}; font-weight: 600; }}
    .deep-plan-list li.deep-sec-hdr {{ list-style: none; margin: 0.5rem 0 0.2rem -0.7rem; font-weight: 700; color: {accent_dark}; font-size: 0.76rem; }}
    .deep-deeper-lbl {{ display: inline-flex; align-items: center; gap: 0.3rem; font-size: 0.78rem; color: #444; cursor: pointer; user-select: none; white-space: nowrap; }}
    .deep-deeper-lbl input {{ cursor: pointer; }}
    .deep-deeper-note {{ font-size: 0.72rem; color: {accent}; font-weight: 600; }}
    .deep-body {{ padding: 1.2rem 1.5rem; display: none; }}
    .deep-body.active {{ display: block; }}
    .deep-answer {{ font-size: 0.94rem; line-height: 1.75; color: #262626; }}
    .deep-answer p {{ margin: 0.75rem 0; }}
    .deep-answer h1, .deep-answer h2, .deep-answer h3 {{ color: {accent_dark}; margin: 1.1rem 0 0.45rem; line-height: 1.3; }}
    .deep-answer h1 {{ font-size: 1.2rem; }}
    .deep-answer h2 {{ font-size: 1.05rem; }}
    .deep-answer h3 {{ font-size: 0.96rem; }}
    .deep-answer ul, .deep-answer ol {{ margin: 0.5rem 0 0.5rem 1.5rem; }}
    .deep-answer li {{ margin: 0.25rem 0; }}
    .deep-answer strong {{ color: #1a1a1a; }}
    .deep-answer a.ref {{ display: inline-block; color: {accent}; text-decoration: none; font-weight: 700; font-size: 0.72rem; padding: 0 0.32rem; border-radius: 3px; background: {accent}1a; margin: 0 0.12rem; vertical-align: super; line-height: 1.2; }}
    .deep-answer a.ref:hover {{ background: {accent}; color: white; }}
    .deep-answer figure {{ margin: 1rem 0; max-width: 100%; }}
    .deep-answer img {{ width: 100%; height: auto; display: block; margin: 1rem 0; padding: 0.5rem; background: #fafafa; border: 1px solid #eee; border-radius: 6px; box-sizing: border-box; cursor: zoom-in; }}
    .deep-answer figure img {{ margin: 0; }}
    .deep-answer figure figcaption {{ font-size: 0.78rem; color: #666; text-align: center; margin-top: 0.45rem; font-style: italic; }}
    .deep-answer p img {{ margin: 0.5rem 0; }}
    .deep-answer code {{ background: #f2f2f4; padding: 0.1rem 0.35rem; border-radius: 3px; font-size: 0.86em; font-family: ui-monospace, monospace; }}
    .deep-answer pre {{ background: #f6f8fa; padding: 0.7rem 0.9rem; border-radius: 6px; overflow-x: auto; }}
    .deep-refs {{ margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid #eee; }}
    .deep-refs h4 {{ font-size: 0.88rem; color: {accent_dark}; margin-bottom: 0.55rem; }}
    .deep-refs ol {{ margin-left: 1.2rem; font-size: 0.82rem; color: #555; }}
    .deep-refs li {{ margin: 0.3rem 0; line-height: 1.55; }}
    .deep-refs a {{ color: {accent}; text-decoration: none; }}
    .deep-refs a:hover {{ text-decoration: underline; }}
    .deep-figures {{ margin-top: 1.4rem; padding-top: 1rem; border-top: 1px solid #eee; }}
    .deep-figures h4 {{ font-size: 0.88rem; color: {accent_dark}; margin-bottom: 0.6rem; }}
    .deep-figures-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(190px, 1fr)); gap: 0.7rem; }}
    .deep-fig-item {{ background: #fafafa; border: 1px solid #eee; border-radius: 6px; overflow: hidden; }}
    .deep-fig-item a {{ text-decoration: none; color: inherit; display: block; }}
    .deep-fig-item img {{ width: 100%; height: 115px; object-fit: cover; cursor: zoom-in; display: block; }}
    .deep-fig-item .fig-cap {{ padding: 0.35rem 0.6rem; font-size: 0.7rem; color: #666; line-height: 1.35; }}"""

    # Audio Overview styles (shared lib). accent_bg ≈ accent at ~10% alpha.
    CSS = CSS + "\n" + _audio_css(accent, accent_dark, accent + "1a")
    if cross:
        CSS += (
            "\n/* cross-topic 통합 콘솔 (로컬 전용) */\n"
            ".sort-bar{display:none!important;}\n"
            ".mode-toggle{display:none!important;}\n"
            '.hero a[href="feed.xml"]{display:none!important;}\n'
            ".hero .stat:nth-child(2){display:none!important;}\n"
            ".cross-dir{background:#fff;border:1px solid #eee;border-radius:12px;padding:1.2rem 1.4rem;margin:0.5rem 0 0;}\n"
            ".cross-dir h2{font-size:1.05rem;margin-bottom:0.5rem;color:#6B21A8;}\n"
            ".cross-dir p{font-size:0.92rem;color:#444;line-height:1.7;}\n"
            ".cross-topics{display:flex;flex-wrap:wrap;gap:0.6rem;margin-top:0.9rem;}\n"
            "a.cross-topic{display:inline-flex;gap:0.45rem;align-items:center;padding:0.5rem 0.95rem;border:1px solid #e5e5e5;border-radius:999px;text-decoration:none;color:#333;font-size:0.9rem;}\n"
            "a.cross-topic:hover{background:#faf5ff;border-color:#B57BF0;}\n"
            "a.cross-topic strong{color:#6B21A8;}\n"
        )

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
    function toggleInsights() {
      const body = document.getElementById('insights-body');
      if (!body) return;
      const toggle = document.getElementById('toggle-insights-body');
      const header = document.querySelector('.insights-header');
      const collapsed = body.classList.toggle('collapsed');
      if (toggle) toggle.textContent = collapsed ? '\\u25B6' : '\\u25BC';
      if (header) header.classList.toggle('open', !collapsed);
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
        if (window._searchMode === 'deep') return;
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
    });

    // ============================================================================
    // Deep Research (client-side RAG + Anthropic streaming with Extended Thinking)
    // ============================================================================
    const DEEP = { index: null, loading: false, currentAnswer: '', currentRefs: [], currentQuery: '', abort: null, running: false, userAborted: false };

    // Safe DOM helpers (no .innerHTML usage)
    function clearEl(el) { while (el && el.firstChild) el.removeChild(el.firstChild); }
    function renderTo(el, content) {
      if (!el) return;
      clearEl(el);
      if (!content) return;
      const range = document.createRange();
      range.selectNodeContents(el);
      const frag = range.createContextualFragment(content);
      el.appendChild(frag);
    }

    function deepSetStatus(text, isError) {
      const el = document.getElementById('deep-status');
      if (!el) return;
      if (!text) { el.classList.remove('active', 'error'); el.textContent = ''; return; }
      el.textContent = text;
      el.classList.add('active');
      if (isError) el.classList.add('error'); else el.classList.remove('error');
    }

    function deepShowPanel() {
      document.getElementById('deep-panel').style.display = '';
      document.getElementById('deep-body').classList.add('active');
    }

    function deepHidePanel() {
      document.getElementById('deep-panel').style.display = 'none';
      document.getElementById('deep-body').classList.remove('active');
      deepSetStatus('');
      clearEl(document.getElementById('deep-answer'));
      document.getElementById('deep-refs').style.display = 'none';
      document.getElementById('deep-figures').style.display = 'none';
      DEEP.currentAnswer = '';
      DEEP.currentRefs = [];
      DEEP.currentQuery = '';
      deepUpdateButtons(false);
    }

    function deepUpdateButtons(enabled) {
      for (const id of ['deep-copy', 'deep-download', 'deep-download-html', 'deep-newtab', 'deep-obsidian', 'deep-rerun']) {
        const b = document.getElementById(id);
        if (b) b.disabled = !enabled;
      }
      // Audio Overview button: enabled once an answer exists. The user
      // gets prompted for their Gemini key on first click if none is
      // cached (same as the per-paper button).
      const ab = document.getElementById('deep-audio');
      if (ab) ab.disabled = !enabled;
    }

    // ── Kill switch ──────────────────────────────────────────────────
    // Every Deep/Deeper run owns one AbortController. Its signal is fed to
    // every LLM/embed fetch (deepSignal), so clicking 중단 aborts in-flight
    // streams immediately; orchestration boundaries also poll the flag via
    // deepThrowIfAborted so the multi-agent loop stops between steps.
    function deepSignal() { return DEEP.abort ? DEEP.abort.signal : undefined; }
    // fetch() wrapper that auto-attaches the current run's abort signal, so a
    // single 중단 click cancels every in-flight LLM/embed request. Outside a
    // run (DEEP.abort null) it behaves exactly like plain fetch.
    function deepFetch(url, opts) {
      opts = opts || {};
      if (opts.signal === undefined) { const sig = deepSignal(); if (sig) opts.signal = sig; }
      return fetch(url, opts);
    }
    function deepThrowIfAborted() {
      if (DEEP.userAborted || (DEEP.abort && DEEP.abort.signal && DEEP.abort.signal.aborted)) {
        const e = new Error('aborted-by-user');
        e.name = 'AbortError';
        throw e;
      }
    }
    function deepIsAbort(e) {
      return DEEP.userAborted || (e && (e.name === 'AbortError'
        || (e.message && e.message.indexOf('aborted-by-user') !== -1)));
    }
    function deepToggleStop(on) {
      const s = document.getElementById('deep-stop');
      if (s) s.style.display = on ? '' : 'none';
      // Re-run shares the slot — never offer it mid-flight.
      const rr = document.getElementById('deep-rerun');
      if (rr && on) rr.disabled = true;
    }
    function deepBeginRun() {
      DEEP.userAborted = false;
      DEEP.abort = new AbortController();
      DEEP.running = true;
      deepToggleStop(true);
    }
    function deepEndRun() {
      DEEP.running = false;
      DEEP.abort = null;
      deepToggleStop(false);
    }
    function deepRequestStop() {
      if (!DEEP.running) return;
      DEEP.userAborted = true;
      if (DEEP.abort) { try { DEEP.abort.abort(); } catch (e) {} }
      deepSetStatus('⏹️ 중단하는 중...');
    }

    // Show the Deep Research control bar (length/model/Deeper) the moment the
    // user switches into Deep mode — so they can pick분량·모델 BEFORE running,
    // instead of the panel only appearing once a query is already in flight.
    function deepShowControls() {
      const p = document.getElementById('deep-panel');
      if (p) p.style.display = '';
    }

    async function deepLoadIndex() {
      if (DEEP.index) return DEEP.index;
      if (DEEP.loading) {
        while (DEEP.loading) await new Promise(r => setTimeout(r, 100));
        return DEEP.index;
      }
      DEEP.loading = true;
      deepSetStatus('\U0001F4E6 Loading search index...');
      try {
        const resp = await fetch('_search_index.json');
        if (!resp.ok) throw new Error('Index fetch failed: ' + resp.status);
        DEEP.index = await resp.json();
        // 신형 포맷: 임베딩은 바이너리 사이드카(emb_file) — JSON 에서 빠져
        // cold-load 의 JSON.parse 가 가볍고, 쿼리 시 per-chunk atob 도 없다.
        // ArrayBuffer → Int8Array 뷰 (파싱 0ms). 구형(chunk.emb b64)은
        // getChunkVec 가 그대로 지원하므로 미재빌드 토픽도 동작.
        if (DEEP.index.emb_file) {
          const er = await fetch(DEEP.index.emb_file);
          if (!er.ok) throw new Error('Embedding sidecar fetch failed: ' + er.status);
          const buf = await er.arrayBuffer();
          const expect = (DEEP.index.count || 0) * (DEEP.index.dim || 0);
          if (buf.byteLength !== expect) {
            throw new Error('Embedding sidecar size mismatch: ' + buf.byteLength + ' != ' + expect + ' — rebuild the index (build_search_index)');
          }
          DEEP.embI8 = new Int8Array(buf);
        } else {
          DEEP.embI8 = null;
        }
        // Deep Research init: lexical(BM25) 인덱스를 미리 구축해 둔다.
        // (이후 hybridRetrieve 가 같은 캐시를 재사용)
        try { buildBM25(DEEP.index); } catch (e) { console.warn('[bm25] build skipped:', e && e.message || e); }
        return DEEP.index;
      } finally {
        DEEP.loading = false;
      }
    }

    function dequantizeEmb(b64) {
      const binary = atob(b64);
      const dim = binary.length;
      const vec = new Float32Array(dim);
      for (let i = 0; i < dim; i++) {
        let b = binary.charCodeAt(i);
        if (b >= 128) b -= 256;
        vec[i] = b / 127.0;
      }
      let n = 0;
      for (let i = 0; i < dim; i++) n += vec[i] * vec[i];
      n = Math.sqrt(n) || 1;
      for (let i = 0; i < dim; i++) vec[i] /= n;
      return vec;
    }

    function cosineSim(a, b) {
      let s = 0;
      for (let i = 0; i < a.length; i++) s += a[i] * b[i];
      return s;
    }

    function getChunkVec(index, i) {
      // 신형 포맷: 바이너리 사이드카의 Int8 뷰에서 직접 정규화 (atob 불필요)
      if (DEEP.embI8) {
        const dim = index.dim;
        const off = i * dim;
        const vec = new Float32Array(dim);
        let n = 0;
        for (let k = 0; k < dim; k++) {
          const v = DEEP.embI8[off + k] / 127.0;
          vec[k] = v;
          n += v * v;
        }
        n = Math.sqrt(n) || 1;
        for (let k = 0; k < dim; k++) vec[k] /= n;
        return vec;
      }
      // 구형 포맷 호환: chunk 에 박힌 b64 디코드
      return dequantizeEmb(index.chunks[i].emb);
    }

    async function embedQuery(text) {
      // 질의 임베딩은 같은 출처(/api/embed) 프록시가 처리한다. serve_local
      // 런처(또는 Cloudflare Worker)가 GOOGLE_API_KEY 로 gemini-embedding-001
      // (RETRIEVAL_QUERY, 768d) 을 호출하므로 브라우저에는 임베딩용 API 키가
      // 더 이상 필요 없다. 503/404/네트워크 실패는 'embed-proxy-unreachable'
      // 접두사로 태깅 → runDeepResearch 가 친절한 한글 안내로 변환한다.
      let resp;
      try {
        resp = await deepFetch('/api/embed', {
          method: 'POST',
          headers: { 'content-type': 'application/json' },
          body: JSON.stringify({ text: text }),
        });
      } catch (e) {
        if (e && e.name === 'AbortError') throw e;  // user 중단 — bubble as-is
        throw new Error('embed-proxy-unreachable: ' + (e && e.message || e));
      }
      if (resp.status === 503 || resp.status === 404) {
        throw new Error('embed-proxy-unreachable: /api/embed ' + resp.status);
      }
      if (!resp.ok) {
        const err = await resp.text();
        throw new Error('embed-proxy ' + resp.status + ': ' + err.slice(0, 180));
      }
      const data = await resp.json();
      const raw = (data && data.embedding) || [];
      if (!raw.length) throw new Error('embed-proxy-unreachable: empty embedding');
      // gemini-embedding-001 은 output_dimensionality != 3072 일 때 정규화되지
      // 않은 벡터를 반환한다 — 코사인 유사도(정규화된 문서 벡터 가정)와 맞추려면
      // int8 양자화와 동일하게 L2 정규화가 필수.
      let n = 0;
      for (const v of raw) n += v * v;
      n = Math.sqrt(n) || 1;
      return raw.map(v => v / n);
    }

    function parseTimeFilter(q) {
      const now = new Date().getFullYear();
      const P = [
        [/(\\d{4})\\s*년\\s*이후|since\\s+(\\d{4})|after\\s+(\\d{4})/i, m => ({min: +(m[1]||m[2]||m[3])})],
        [/(\\d{4})\\s*년\\s*이전|before\\s+(\\d{4})/i, m => ({max: +(m[1]||m[2])})],
        [/최근\\s*(\\d+)\\s*년|last\\s+(\\d+)\\s+years?|past\\s+(\\d+)\\s+years?/i, m => ({min: now - +(m[1]||m[2]||m[3])})],
        [/최근\\s*1\\s*년|last\\s+year/i, () => ({min: now - 1})],
        [/(\\d{4})\\s*[-~]\\s*(\\d{4})/, m => ({min: +m[1], max: +m[2]})],
        [/\\b((?:19|20)\\d{2})\\b\\s*년?/, m => ({min: +m[1], max: +m[1]})],
      ];
      for (const [re, fn] of P) {
        const m = q.match(re);
        if (m) return fn(m);
      }
      return null;
    }

    // ── Journal-aware filtering ───────────────────────────────────────
    // 저널 메타(papers[].journal)로 후보를 거른다. 질의에 코퍼스의 저널명이
    // 들어 있으면 그 저널로, "preprint/프리프린트/arxiv"면 미게재로 필터.
    function _journalSet(index) {
      if (DEEP._journals) return DEEP._journals;
      const s = Object.create(null);
      const papers = index.papers || {};
      for (const k in papers) {
        const j = String(papers[k].journal || '').trim();
        if (j && j.toLowerCase() !== 'preprint') s[j.toLowerCase()] = j;
      }
      DEEP._journals = s;
      return s;
    }
    // 흔한 단어이기도 한 단일어 저널명(Science, Matter...)은 venue cue 가 있을
    // 때만 필터로 인정 — "AI for science" 같은 도메인 표현 오인식 방지. 멀티워드
    // 저널명(Nature Communications, Science Robotics...)은 cue 없이도 매칭.
    var _JCUE = /저널|학술지|학회지|journal|게재|등재|실린|지에|published in/i;
    var _JSTOP = { science: 1, matter: 1, joule: 1, chaos: 1, brain: 1, patterns: 1, device: 1, sensors: 1 };
    function parseJournalFilter(query, index) {
      const q = String(query || '').toLowerCase();
      if (/preprint|프리프린트|아카이브/.test(q) || /arxiv\\s*(?:만|only|논문)?/.test(q))
        return { kind: 'preprint', label: 'preprint' };
      const cue = _JCUE.test(query);
      const set = _journalSet(index);
      let best = null;
      for (const lc in set) {
        if (lc.length < 5 || q.indexOf(lc) < 0) continue;
        if (!cue && _JSTOP[lc]) continue;       // 흔한-단어 저널명은 cue 있을 때만
        if (!best || lc.length > best.length) best = lc;
      }
      return best ? { kind: 'journal', lc: best, label: set[best] } : null;
    }
    function journalMatches(paperJournal, jf) {
      if (!jf) return true;
      const pj = String(paperJournal || '').trim().toLowerCase();
      if (jf.kind === 'preprint') return (pj === 'preprint' || pj === '');
      return pj.indexOf(jf.lc) >= 0;
    }

    function detectLang(text) {
      const ko = (text.match(/[\\u1100-\\u11FF\\u3130-\\u318F\\uAC00-\\uD7AF]/g) || []).length;
      return (ko / (text.length || 1)) > 0.1 ? 'ko' : 'en';
    }

    // ── Author-aware retrieval ────────────────────────────────────────
    // 저자명은 chunk 본문/임베딩에 들어있지 않다(섹션 본문만 인덱싱). 그래서
    // "Dashun Wang의 연구를 시간순으로" 같은 질의는 dense/BM25 둘 다 매칭이
    // 안 돼 엉뚱한 결과로 흐른다. index.papers 의 authors/first_author 메타
    // (이미 로드됨)를 직접 매칭해 해당 저자 논문을 후보로 구성한다.
    function _normName(s) {
      return String(s || '').toLowerCase()
        .normalize('NFKD').replace(/[\\u0300-\\u036f]/g, '')   // 발음기호 제거 (Barabási→barabasi)
        .replace(/[.\\-]/g, ' ').replace(/\\s+/g, ' ').trim();
    }
    function _latinTokenSet(s) {
      const set = Object.create(null);
      const m = _normName(s).match(/[a-z][a-z]+/g);             // 길이>=2 라틴 토큰만
      if (m) for (const w of m) set[w] = 1;
      return set;
    }
    // index.papers → [{label, tokens:[...], slugs:{...}}] 1회 구축·캐시.
    function buildAuthorMap(index) {
      if (DEEP._authorMap) return DEEP._authorMap;
      const papers = index.papers || {};
      const map = [];
      const byKey = Object.create(null);
      function add(name, slug) {
        const toks = Object.keys(_latinTokenSet(name));
        if (toks.length < 2) return;                           // 단일 토큰 이름은 신뢰성 낮아 제외
        const key = toks.slice().sort().join(' ');
        let e = byKey[key];
        if (!e) { e = { label: name, tokens: toks, slugs: Object.create(null) }; byKey[key] = e; map.push(e); }
        else if (String(name).length > e.label.length) e.label = name;
        e.slugs[slug] = 1;
      }
      for (const slug in papers) {
        const p = papers[slug];
        const list = (p.authors && p.authors.length) ? p.authors : (p.first_author ? [p.first_author] : []);
        for (const a of list) add(a, slug);
      }
      DEEP._authorMap = map;
      return map;
    }
    // 질의가 코퍼스 저자를 가리키면 {label, slugs:[...]}, 아니면 null.
    function matchCorpusAuthor(query, index) {
      const qset = _latinTokenSet(query);
      const map = buildAuthorMap(index);
      let best = null;
      for (const e of map) {
        let all = true;
        for (const t of e.tokens) { if (!qset[t]) { all = false; break; } }
        if (all && (!best || e.tokens.length > best.tokens.length)) best = e;
      }
      return best ? { label: best.label, slugs: Object.keys(best.slugs) } : null;
    }
    // 코퍼스엔 없지만 "이름 + 연구/정리" 형태의 저자 질의로 보이는지.
    function looksLikeAuthorQuery(query) {
      const namePair = /[A-Z][a-z]+\\s+(?:[A-Z]\\.?\\s+)?[A-Z][a-z]+/.test(query);
      const intent = /(연구|논문|저자|업적|work|works|paper|papers|author|publication|정리|요약|시간순|연대순|연도순|chronolog|timeline)/i.test(query);
      return namePair && intent;
    }
    function isChronological(query) {
      return /(시간\\s*순|연대\\s*순|연도\\s*순|시계열|순서대로|발전\\s*과정|chronolog|timeline|over\\s+time|by\\s+year)/i.test(query);
    }
    function _chunkIdxBySlug(index) {
      if (DEEP._cbs) return DEEP._cbs;
      const m = Object.create(null);
      const chunks = index.chunks || [];
      for (let i = 0; i < chunks.length; i++) {
        const s = chunks[i].slug;
        (m[s] || (m[s] = [])).push(i);
      }
      DEEP._cbs = m;
      return m;
    }
    function _sectionRank(sec) {
      const s = String(sec || '').toLowerCase();
      if (s.indexOf('essence') >= 0 || s.indexOf('요약') >= 0 || s.indexOf('한줄') >= 0) return 0;
      if (s.indexOf('achiev') >= 0 || s.indexOf('성과') >= 0) return 1;
      if (s.indexOf('origin') >= 0 || s.indexOf('독창') >= 0) return 2;
      return 3;
    }
    // 저자 논문들을 hybridRetrieve 와 동일한 {chunk,paper,rrf} 후보로 변환.
    // chronological 이면 연도 오름차순(초과 시 연도 분포 보존 stride 샘플),
    // 아니면 질의-best chunk 코사인 관련도 내림차순. 논문당 대표 chunk 최대 2개.
    function authorCandidates(index, hit, queryVec, timeFilter, chronological, journalFilter) {
      const papers = index.papers, chunks = index.chunks;
      const cbs = _chunkIdxBySlug(index);
      const plist = [];
      for (const slug of hit.slugs) {
        const p = papers[slug];
        if (!p) continue;
        const y = parseInt(p.year);
        if (timeFilter) {
          if (timeFilter.min && (!y || y < timeFilter.min)) continue;
          if (timeFilter.max && (!y || y > timeFilter.max)) continue;
        }
        if (!journalMatches(p.journal, journalFilter)) continue;
        const idxs = cbs[slug] || [];
        let best = -1;
        for (const ci of idxs) { const sc = cosineSim(queryVec, getChunkVec(index, ci)); if (sc > best) best = sc; }
        plist.push({ slug: slug, year: y || 0, score: best, idxs: idxs });
      }
      if (!plist.length) return [];
      if (chronological) plist.sort(function(a, b) { return (a.year - b.year) || (b.score - a.score); });
      else plist.sort(function(a, b) { return (b.score - a.score) || (b.year - a.year); });
      const MAXP = chronological ? 24 : 12;                    // 토큰 예산 보호 상한 (시간순은 궤적 커버리지 ↑)
      let chosen = plist;
      if (plist.length > MAXP) {
        if (chronological) {
          chosen = [];
          const stride = (plist.length - 1) / (MAXP - 1);
          for (let k = 0; k < MAXP; k++) chosen.push(plist[Math.round(k * stride)]);
        } else {
          chosen = plist.slice(0, MAXP);
        }
      }
      const cands = [];
      for (const p of chosen) {
        const ranked = p.idxs.map(function(ci) {
          return { ci: ci, sec: chunks[ci].section || '', s: cosineSim(queryVec, getChunkVec(index, ci)) };
        });
        ranked.sort(function(a, b) { return (_sectionRank(a.sec) - _sectionRank(b.sec)) || (b.s - a.s); });
        const take = ranked.slice(0, 2);
        for (const r of take) cands.push({ chunk: chunks[r.ci], paper: papers[p.slug], rrf: r.s });
      }
      return cands;
    }

    // ── Hybrid retrieval: BM25 (lexical) + dense + RRF ────────────────
    // 한글/영문 혼용 코퍼스라 토크나이저는 두 갈래로 나눈다:
    //   · ASCII 단어 토큰 — 영문 전문용어/약어를 통째로 보존 (예: "GNN")
    //   · 한글 run 은 문자 bigram — 형태소 분석 없이도 한국어 매칭에 효과적
    function deepTokenize(text) {
      const t = String(text || '').toLowerCase();
      const toks = [];
      const ascii = t.match(/[a-z0-9]+/g);
      if (ascii) for (const w of ascii) toks.push(w);
      const hangul = t.match(/[\\uAC00-\\uD7AF\\u1100-\\u11FF\\u3130-\\u318F]+/g);
      if (hangul) {
        for (const run of hangul) {
          if (run.length === 1) { toks.push(run); continue; }
          for (let i = 0; i < run.length - 1; i++) toks.push(run.slice(i, i + 2));
        }
      }
      return toks;
    }

    // 인덱스의 chunk.text 전체에 대해 컴팩트한 BM25 인덱스를 1회 구축하고
    // DEEP.bm25 에 캐시한다 (Deep Research init 시점). chunk 수가 바뀌면 재구축.
    function buildBM25(index) {
      const chunks = index.chunks || [];
      const N = chunks.length;
      if (DEEP.bm25 && DEEP.bm25.N === N) return DEEP.bm25;
      const df = Object.create(null);     // term -> document frequency
      const docs = new Array(N);          // chunk 별 { tf, len }
      let totalLen = 0;
      for (let i = 0; i < N; i++) {
        const toks = deepTokenize(chunks[i].text);
        const tf = Object.create(null);
        for (const tk of toks) tf[tk] = (tf[tk] || 0) + 1;
        for (const tk in tf) df[tk] = (df[tk] || 0) + 1;
        docs[i] = { tf: tf, len: toks.length };
        totalLen += toks.length;
      }
      const avgdl = totalLen / (N || 1);
      const idf = Object.create(null);
      for (const tk in df) {
        // BM25 idf (음수 방지를 위해 1 + ... 형태의 표준 변형)
        idf[tk] = Math.log(1 + (N - df[tk] + 0.5) / (df[tk] + 0.5));
      }
      DEEP.bm25 = { N: N, docs: docs, idf: idf, avgdl: avgdl, k1: 1.5, b: 0.75 };
      return DEEP.bm25;
    }

    function bm25Score(bm25, qToks, i) {
      const doc = bm25.docs[i];
      if (!doc) return 0;
      const k1 = bm25.k1, b = bm25.b, avgdl = bm25.avgdl || 1;
      let s = 0;
      const seen = Object.create(null);
      for (const tk of qToks) {
        if (seen[tk]) continue;           // 동일 query term 중복 가중 방지
        seen[tk] = 1;
        const f = doc.tf[tk];
        if (!f) continue;
        const idf = bm25.idf[tk] || 0;
        s += idf * (f * (k1 + 1)) / (f + k1 * (1 - b + b * doc.len / avgdl));
      }
      return s;
    }

    // dense + BM25 두 랭킹을 RRF(score = Σ 1/(60+rank)) 로 융합해 top-N 후보를
    // 만든다. 시간 필터는 두 랭킹의 공통 후보 집합에 먼저 적용해 의미를
    // 일관되게 유지한다. paper 당 최대 3 chunk 로 다양성도 보존 (기존 의미).
    function hybridRetrieve(index, queryVec, query, timeFilter, journalFilter, topN) {
      const chunks = index.chunks, papers = index.papers;
      const bm25 = buildBM25(index);
      const elig = [];
      for (let i = 0; i < chunks.length; i++) {
        const c = chunks[i];
        const paper = papers[c.slug];
        if (!paper) continue;
        if (timeFilter) {
          const y = parseInt(paper.year);
          if (timeFilter.min && (!y || y < timeFilter.min)) continue;
          if (timeFilter.max && (!y || y > timeFilter.max)) continue;
        }
        if (!journalMatches(paper.journal, journalFilter)) continue;
        elig.push(i);
      }
      if (!elig.length) return [];
      // dense 랭킹
      const denseScored = elig.map(function(i) {
        return { i: i, s: cosineSim(queryVec, getChunkVec(index, i)) };
      });
      denseScored.sort(function(a, b) { return b.s - a.s; });
      const denseRank = Object.create(null);
      for (let r = 0; r < denseScored.length; r++) denseRank[denseScored[r].i] = r;
      // BM25 랭킹
      const qToks = deepTokenize(query);
      const bm25Scored = elig.map(function(i) {
        return { i: i, s: bm25Score(bm25, qToks, i) };
      });
      bm25Scored.sort(function(a, b) { return b.s - a.s; });
      const bm25Rank = Object.create(null);
      for (let r = 0; r < bm25Scored.length; r++) bm25Rank[bm25Scored[r].i] = r;
      // RRF 융합
      const RRF_K = 60;
      const fused = elig.map(function(i) {
        let sc = 1 / (RRF_K + (denseRank[i] || 0));
        if (i in bm25Rank) sc += 1 / (RRF_K + bm25Rank[i]);
        return { i: i, score: sc };
      });
      fused.sort(function(a, b) { return b.score - a.score; });
      const used = Object.create(null);
      const out = [];
      for (const f of fused) {
        if (out.length >= topN) break;
        const c = chunks[f.i];
        used[c.slug] = (used[c.slug] || 0) + 1;
        if (used[c.slug] > 3) continue;
        out.push({ chunk: c, paper: papers[c.slug], rrf: f.score });
      }
      return out;
    }

    // ── LLM re-rank ──────────────────────────────────────────────────
    // RRF top-20 을 답변 백엔드의 FAST tier 모델(Anthropic→Sonnet, Google→Flash,
    // OpenAI→소형)로 재정렬. 단발성 non-stream 호출. 어떤 실패든(파싱/타임아웃/
    // 인증) RRF 상위 topK 로 조용히 폴백한다 — 답변 경로는 그대로.
    async function rerankCall(backend, apiKey, model, sys, user) {
      if (backend === 'anthropic') {
        const resp = await deepFetch('https://api.anthropic.com/v1/messages', {
          method: 'POST',
          headers: {
            'content-type': 'application/json',
            'x-api-key': apiKey,
            'anthropic-version': '2023-06-01',
            'anthropic-dangerous-direct-browser-access': 'true',
          },
          body: JSON.stringify({
            model: model,
            max_tokens: 512,
            system: sys,
            messages: [{ role: 'user', content: user }],
          }),
        });
        if (!resp.ok) throw new Error('Anthropic rerank ' + resp.status);
        const data = await resp.json();
        return (data.content && data.content[0] && data.content[0].text) || '';
      }
      if (backend === 'openai') {
        const resp = await deepFetch('https://api.openai.com/v1/chat/completions', {
          method: 'POST',
          headers: { 'content-type': 'application/json', 'authorization': 'Bearer ' + apiKey },
          body: JSON.stringify({
            model: model,
            messages: [{ role: 'system', content: sys }, { role: 'user', content: user }],
            max_completion_tokens: 512,
          }),
        });
        if (!resp.ok) throw new Error('OpenAI rerank ' + resp.status);
        const data = await resp.json();
        return (data.choices && data.choices[0] && data.choices[0].message && data.choices[0].message.content) || '';
      }
      if (backend === 'google') {
        const url = 'https://generativelanguage.googleapis.com/v1beta/models/'
          + encodeURIComponent(model) + ':generateContent?key=' + encodeURIComponent(apiKey);
        const resp = await deepFetch(url, {
          method: 'POST',
          headers: { 'content-type': 'application/json' },
          body: JSON.stringify({
            systemInstruction: { parts: [{ text: sys }] },
            contents: [{ role: 'user', parts: [{ text: user }] }],
            generationConfig: { maxOutputTokens: 512, temperature: 0 },
          }),
        });
        if (!resp.ok) throw new Error('Google rerank ' + resp.status);
        const data = await resp.json();
        const cand = data.candidates && data.candidates[0];
        const parts = cand && cand.content && cand.content.parts;
        let t = '';
        if (parts) for (const p of parts) if (p.text) t += p.text;
        return t;
      }
      throw new Error('Unsupported backend: ' + backend);
    }

    async function rerankCandidates(query, candidates, topK) {
      const fallback = candidates.slice(0, topK);
      if (candidates.length <= topK) return fallback;
      const apiKey = _LLM_KEY || _ANTHROPIC_KEY || _OPENAI_KEY || (window._GEMINI_KEY || '');
      const backend = detectBackend(apiKey);
      if (!backend) return fallback;
      const model = resolveModel(backend, 'fast');
      if (!model) return fallback;
      // 후보 번호 목록: slug/section + 앞 ~200자
      const listLines = candidates.map(function(c, i) {
        const sec = c.chunk.section || '';
        const head = String(c.chunk.text || '').replace(/\\s+/g, ' ').trim().slice(0, 200);
        return '[' + i + '] ' + c.chunk.slug + ' / ' + sec + ': ' + head;
      });
      const sys = 'You are a retrieval re-ranker. Given a user query and a numbered list of candidate passages, return ONLY a JSON array of the ' + topK + ' candidate indices (integers) most relevant to the query, best first. No prose, no markdown — just the JSON array, e.g. [3,0,7].';
      const user = 'Query: ' + query + '\\n\\nCandidates:\\n' + listLines.join('\\n') + '\\n\\nReturn the best ' + topK + ' indices as a JSON array.';
      let text = '';
      try {
        text = await Promise.race([
          rerankCall(backend, apiKey, model, sys, user),
          new Promise(function(_, rej) { setTimeout(function() { rej(new Error('rerank-timeout')); }, 6000); }),
        ]);
      } catch (e) {
        console.warn('[rerank] fallback to RRF:', e && e.message || e);
        return fallback;
      }
      let idxs = null;
      try {
        const m = String(text).match(/\\[[\\s\\S]*?\\]/);
        if (m) idxs = JSON.parse(m[0]);
      } catch (e) { idxs = null; }
      if (!Array.isArray(idxs) || !idxs.length) return fallback;
      const picked = [];
      const seen = Object.create(null);
      for (const v of idxs) {
        const i = parseInt(v);
        if (isNaN(i) || i < 0 || i >= candidates.length || seen[i]) continue;
        seen[i] = 1;
        picked.push(candidates[i]);
        if (picked.length >= topK) break;
      }
      if (!picked.length) return fallback;
      // 모델이 topK 미만을 반환하면 RRF 순서로 채운다
      if (picked.length < topK) {
        for (const c of fallback) {
          if (picked.length >= topK) break;
          if (picked.indexOf(c) === -1) picked.push(c);
        }
      }
      return picked;
    }

    function mdToMarkup(md) {
      if (window.marked) {
        try { return window.marked.parse(md, { gfm: true, breaks: false }); }
        catch (e) { /* fallthrough */ }
      }
      let h = md.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
        .replace(/^### (.+)$/gm, '<h3>$1</h3>')
        .replace(/^## (.+)$/gm, '<h2>$1</h2>')
        .replace(/^# (.+)$/gm, '<h1>$1</h1>')
        .replace(/\\*\\*(.+?)\\*\\*/g, '<strong>$1</strong>')
        .replace(/!\\[([^\\]]*)\\]\\(([^)]+)\\)/g, '<figure><img src="$2" alt="$1"><figcaption>$1</figcaption></figure>')
        .replace(/\\[([^\\]]+)\\]\\(([^)]+)\\)/g, '<a href="$2">$1</a>')
        .replace(/\\n\\n+/g, '</p><p>');
      return '<p>' + h + '</p>';
    }

    function postProcessRefs(markup, refs) {
      // On-page (live topic view): keep numeric [N] chip pointing at the
      // local paper, which gives the curator quick navigation. Used for
      // the topic page itself; HTML / Markdown export use the natural
      // form (see naturalizeCitations below).
      return markup.replace(/\\[ref:(\\d+)\\]/g, (_, n) => {
        const ref = refs[parseInt(n) - 1];
        if (!ref) return '[ref:' + n + ']';
        return '<a class="ref" href="' + ref.url + '" target="_blank">[' + n + ']</a>';
      });
    }

    function formatAuthorTag(ref) {
      // Collapsed first-author form, used ONLY in the references list at
      // the bottom. We never inject this back into the body any more —
      // the prose itself is expected to weave author / paper / year
      // references naturally (the prompt instructs that style).
      const a = ref && (ref.first_author || (ref.authors && ref.authors[0]));
      if (!a) return '';
      const last = a.trim().split(/\\s+/).slice(-1)[0];
      return last + ' et al.';
    }

    function naturalizeCitations(markup, refs) {
      // Export form: replace [ref:N] with a small superscript link
      // ([N]) that points at the external (DOI / arXiv) URL. We do NOT
      // inject "Author et al. (year)" text — that produced ugly double
      // mentions like 'SPARK"SPARK: Safe..." (2025)' when the model
      // already named the paper in prose. The model is now instructed
      // to vary citation phrasing ("Smith et al.에 의하면", "최근 연구에
      // 따르면", "2023년에 밝혀진 바에 따르면", …) directly in the prose,
      // and [N] is just the click target.
      return markup.replace(/\\[ref:(\\d+)\\]/g, (_, n) => {
        const idx = parseInt(n) - 1;
        const ref = refs[idx];
        if (!ref) return '';
        const href = ref.external_url || ref.url || '';
        if (href) {
          return '<sup><a class="cite" href="' + href + '" target="_blank" rel="noopener">[' + n + ']</a></sup>';
        }
        return '<sup class="cite cite-local">[' + n + ']</sup>';
      });
    }

    function escapeAttr(s) {
      return String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
    }

    function collectCitedNums(md) {
      const cited = new Set();
      for (const m of md.matchAll(/\\[ref:(\\d+)\\]/g)) cited.add(parseInt(m[1]));
      return cited;
    }

    function collectInlineFigureUrls(md) {
      const used = new Set();
      for (const m of md.matchAll(/!\\[[^\\]]*\\]\\(([^)]+)\\)/g)) used.add(m[1]);
      return used;
    }

    // T2-3 DR citation guard. The basic answer path had no protection against
    // a [ref:N] whose N has no entry in the retrieved reference set
    // (hallucination, or an off-by-one after re-ranking) — postProcessRefs
    // rendered such a marker as a raw "[ref:N]" string pointing at nothing.
    // This mirrors the Deeper assembler guard (see finalizeDeepAnswer caller):
    // collect every cited N, treat any N with no DEEP.currentRefs[N-1] as
    // dangling, strip those markers, and report which N were dropped so the UI
    // can surface a subtle note. Pure + side-effect free so it stays unit
    // testable in Node. Returns { answer, dropped, changed }; when nothing is
    // dangling, changed===false and answer is the untouched input (the happy
    // path must stay byte-identical). Disable via window._DR_CITE_GUARD=false.
    function guardDanglingCitations(answer, refs) {
      const text = String(answer || '');
      const list = refs || [];
      const dropped = [];
      const seen = new Set();
      for (const m of text.matchAll(/\\[ref:(\\d+)\\]/g)) {
        const n = parseInt(m[1], 10);
        if (list[n - 1]) continue;
        if (!seen.has(n)) { seen.add(n); dropped.push(n); }
      }
      if (!dropped.length) return { answer: text, dropped: [], changed: false };
      const bad = new Set(dropped);
      const cleaned = text.replace(/\\[ref:(\\d+)\\]/g, function(mk, n) {
        return bad.has(parseInt(n, 10)) ? '' : mk;
      });
      return { answer: cleaned, dropped: dropped.sort(function(a, b) { return a - b; }), changed: true };
    }

    // 웹 검색 모드 답변의 인라인 마크다운 링크 [label](http…) 를 코퍼스 뒤
    // 번호를 잇는 pseudo-ref 로 흡수한다. [ref:N] 마커로 치환해 두면
    // postProcessRefs / References 목록 / export 경로가 웹 출처를 논문
    // 레퍼런스와 동일하게 처리한다. 이미지 링크(![...])는 제외, 같은 URL 은
    // 같은 번호를 재사용, 코퍼스 논문의 external_url 과 일치하면 그 번호를
    // 그대로 쓴다. refs 배열은 제자리에서 늘어난다(호출부가 DEEP.currentRefs
    // 를 넘김). 1회 치환 후 본문에 링크가 남지 않으므로 자연 멱등.
    function absorbWebCitations(answer, refs) {
      const text = String(answer || '');
      const list = refs || [];
      const byUrl = new Map();
      for (let i = 0; i < list.length; i++) {
        const u = list[i] && (list[i].external_url || list[i].url);
        if (u && !byUrl.has(u)) byUrl.set(u, i + 1);
      }
      let changed = false;
      const out = text.replace(/(!?)\\[([^\\]]*)\\]\\((https?:\\/\\/[^)\\s]+)\\)/g, function(m, bang, label, url) {
        if (bang) return m;
        let n = byUrl.get(url);
        if (!n) {
          let host = '';
          try { host = new URL(url).hostname.replace(/^www\\./, ''); } catch (e) {}
          list.push({ title: label || host || url, url: url, external_url: url, web: true });
          n = list.length;
          byUrl.set(url, n);
        }
        changed = true;
        return label + '[ref:' + n + ']';
      });
      return { answer: out, changed: changed };
    }

    // Subtle, non-intrusive caption shown below the answer body when the
    // citation guard removed unverifiable [ref:N]. Idempotent: an empty/falsy
    // list removes any prior note, so a clean run leaves no DOM trace.
    function deepRenderCiteWarning(dropped) {
      const body = document.getElementById('deep-body');
      const prev = document.getElementById('deep-cite-warn');
      if (prev) prev.remove();
      if (!body || !dropped || !dropped.length) return;
      const cap = document.createElement('div');
      cap.id = 'deep-cite-warn';
      cap.className = 'deep-cite-warn';
      cap.style.cssText = 'margin:0.45rem 0 0;padding:0.35rem 0.7rem;font-size:0.72rem;color:#8a6d3b;background:#fcf8e3;border:1px solid #faebcc;border-radius:4px;line-height:1.4;';
      cap.textContent = '⚠️ 출처에 없는 인용 ' + dropped.length + '건(' + dropped.map(function(n) { return '[' + n + ']'; }).join(', ') + ')을 제거했습니다.';
      const answerEl = document.getElementById('deep-answer');
      if (answerEl && answerEl.parentNode === body) body.insertBefore(cap, answerEl.nextSibling);
      else body.appendChild(cap);
    }

    function buildPrompt(query, selected, lang, fullTexts, deeper) {
      const systemKo = '당신은 학술 논문 큐레이션의 리서치 보조입니다. 아래에 제공된 논문 발췌문만을 근거로, 큐레이터의 "카테고리 요약" 스타일을 따라 답변하세요.\\n\\n스타일 지침:\\n- 서술형 한국어 문장 (불릿 나열은 꼭 필요할 때만)\\n- 2~5개 문단, 주제별 또는 시간순으로 자연스럽게 묶기\\n- **인용은 글 흐름에 녹여 쓰세요**. 매 주장 끝에 ``[ref:N]`` 마커만 붙입니다 (N=발췌문 번호) — 후처리가 작은 클릭 가능한 ⌈[N]⌉ 링크로 변환합니다. 본문에서는 **저자명·논문명·연도·시점을 어구로 다양하게 표현**해서 자연스럽게 읽히게 하세요:\\n  ▸ "He et al.에 의하면 ~[ref:1]"\\n  ▸ "최근 공개된 연구에 따르면 ~[ref:2]"\\n  ▸ "2024년에 밝혀진 바[ref:3]에 따르면 ~"\\n  ▸ "OmniH2O[ref:1]는 universal teleoperation을 보였고, 이어진 Expressive Whole-Body Control 연구[ref:4]가 이를 확장했다."\\n  ▸ "Sun et al.와 같이[ref:5], ~"\\n  ▸ "SPARK[ref:6]에서 보인 것처럼 ~"\\n  ▸ "이러한 접근은 초기 humanoid teleoperation 연구[ref:1, ref:2]에서 등장했고 ~"\\n  같은 어구를 반복하지 말고 매 문장마다 다른 표현을 선택하세요. 동일 논문을 한 단락 안에서 또 인용해야 하면 그때는 작가명 생략하고 "이 연구[ref:1]는 또한 ~" 같이 짧게.\\n  중요: ``[ref:N]`` 마커만 출력에 남기고, 우리가 생성하는 "Smith et al. (2024)" 같은 표준 표현은 따로 삽입하지 마세요 — 그건 References 섹션에서만 보여줍니다.\\n- 연관된 Figure는 본문의 적절한 위치에 ![caption](url) 형식으로 삽입 (발췌문의 Figures에 명시된 URL만 사용, 임의 URL 금지)\\n- 마지막 문단은 연구들을 종합하는 한두 문장\\n\\n답변 절차 (출력에 포함하지 말 것):\\n1. 먼저 내부적으로 질의를 분석하고, 어떤 논문들을 어떤 그룹/순서로 엮을지 계획을 세우세요.\\n2. 그런 다음 계획에 따라 최종 답변 본문만 작성하세요.\\n3. 제공된 발췌문 밖의 지식을 절대 사용하지 마세요.\\n4. 발췌문으로 뒷받침되지 않는 주장은 생략하세요.\\n5. 일부 논문에는 "ORIGINAL EXCERPT" 블록이 함께 제공될 수 있습니다. 시약 이름·분량·온도·시간·구체적 수치·실험 조건 등 정량적 디테일이 답변에 필요할 때는 그 원문 발췌를 우선 활용하세요.';
      const systemEn = 'You are a research assistant for an academic paper curation. Answer using ONLY the provided excerpts, following the curator\\'s "category overview" style.\\n\\nStyle guidelines:\\n- Narrative prose (use bullets only when truly needed)\\n- 2-5 paragraphs, grouped by theme or chronology\\n- **Weave citations into the flow.** Append only ``[ref:N]`` markers after each claim (N = excerpt number). A post-processor turns them into small clickable [N] superscripts. In the prose, **vary how you mention author / paper / year / temporal context**:\\n  ▸ "According to He et al., ~[ref:1]"\\n  ▸ "Recent work shows ~[ref:2]"\\n  ▸ "A 2024 study reports ~[ref:3]"\\n  ▸ "OmniH2O[ref:1] established universal teleoperation, later extended by Expressive Whole-Body Control[ref:4]."\\n  ▸ "As Sun et al. did[ref:5], ~"\\n  ▸ "As shown in SPARK[ref:6], ~"\\n  ▸ "This direction emerged in early humanoid teleoperation work[ref:1, ref:2] and ~"\\n  Vary the phrasing every sentence — avoid repeating the same lead-in. When the same paper is cited again within a paragraph, drop the author and use a short hand: "This work[ref:1] also ~".\\n  Important: keep only the ``[ref:N]`` marker — do NOT insert formal "Smith et al. (2024)" tags into the prose. Those appear only in the References section at the bottom.\\n- Embed relevant figures inline at natural positions using ![caption](url) markdown; only use figure URLs explicitly listed with the excerpts (no fabricated URLs)\\n- Close with one or two synthesizing sentences\\n\\nProcedure (do NOT include in output):\\n1. First analyse the query internally and plan which papers to cover and how to group/order them.\\n2. Then write only the final answer body according to your plan.\\n3. Do not use any knowledge beyond the excerpts.\\n4. Omit any claim you cannot back up with an excerpt.\\n5. Some papers may also include an "ORIGINAL EXCERPT" block alongside the summary. When the answer needs concrete quantitative detail (reagent names, amounts, temperatures, durations, specific numbers, experimental conditions), prefer the original excerpt over the summary.';
      const lines = [];
      for (let i = 0; i < selected.length; i++) {
        const s = selected[i], n = i + 1, paper = s.paper;
        const figs = (paper.figures && paper.figures.length)
          ? '\\n  Figures:\\n' + paper.figures.map(f => '    - ' + f.url + '  (' + (f.caption || 'figure') + ')').join('\\n')
          : '';
        // s.chunks is now an array of {section, text} for this single paper
        const sectionsBlock = s.chunks.map(function(c) {
          return '  Section: ' + c.section + '\\n  Text:\\n' + c.text.split('\\n').map(function(l) { return '    ' + l; }).join('\\n');
        }).join('\\n');
        let originalBlock = '';
        if (fullTexts && fullTexts[s.slug]) {
          originalBlock = '\\n  ORIGINAL EXCERPT (use for quantitative detail like reagents, amounts, conditions):\\n' + fullTexts[s.slug].split('\\n').map(function(l) { return '    ' + l; }).join('\\n');
        }
        const fa = paper.first_author || '';
        const authorTag = fa ? (' — ' + fa.split(/\\s+/).slice(-1)[0] + ' et al.') : '';
        const idTag = paper.doi ? (' [DOI: ' + paper.doi + ']') : (paper.arxiv ? (' [arXiv:' + paper.arxiv + ']') : '');
        const relTag = (s.relation && !s.isSeed)
          ? (' [연결관계: ' + (RELATION_KO[s.relation] || s.relation) + (s.reason ? (' — ' + s.reason) : '') + ']')
          : '';
        lines.push('[' + n + '] Paper: "' + paper.title + '"' + authorTag + ' (' + (paper.year || 'n/a') + ', category: ' + (paper.category || 'n/a') + ')' + idTag + relTag + figs + '\\n' + sectionsBlock + originalBlock);
      }
      const deeperNote = deeper
        ? (lang === 'ko'
            ? '아래에는 질문의 핵심 논문과, 그와 연결된 논문들(기반·후속/확장·대안·응용·반론)이 함께 제공됩니다. 연결 논문에는 [연결관계: 관계 — 이유] 태그가 붙어 있습니다. 단순 나열이 아니라 연구 계보를 짚어 종합하세요: 무엇이 기반이 되었고, 무엇이 이를 후속·확장·응용했으며, 어떤 반론·대안이 제기됐는지 흐름으로 엮고, 후속/반론 관계를 본문에 명시하세요.\\n\\n'
            : 'Below are the core papers for the question together with their connected papers (foundation / extension / alternative / application / counterpoint). Connected papers carry a [연결관계: relation — reason] tag. Do not merely list them — trace the research lineage: what laid the foundation, what extended/applied it, and what counterarguments or alternatives arose, weaving the follow-up/rebuttal relations explicitly into the prose.\\n\\n')
        : '';
      const user = deeperNote + 'Excerpts from paper reviews:\\n\\n' + lines.join('\\n\\n---\\n\\n') + '\\n\\n---\\nQuestion: ' + query;
      return { system: lang === 'ko' ? systemKo : systemEn, user: user };
    }

    const LENGTH_SPEC = {
      short:  { max_tokens: 4096,  thinking: 1500, ko: '2~5개 문단으로 간결하게 (약 400~900자)',       en: '2-5 concise paragraphs (roughly 300-700 words)' },
      medium: { max_tokens: 6500,  thinking: 2500, ko: '5~10개 문단으로 충실하게 (약 900~1800자)',     en: '5-10 substantial paragraphs (roughly 700-1500 words)' },
      long:   { max_tokens: 24000, thinking: 8000, ko: '20~40개 문단으로 매우 상세하게 (약 3600~9000자)',   en: '20-40 in-depth paragraphs (roughly 3000-7000 words)' },
      ultra:  { max_tokens: 20000, thinking: 6000, ko: '20~40개 문단으로 심층적으로 (약 4500~9000자)', en: '20-40 in-depth paragraphs (roughly 3500-7000 words)' },
    };

    // ── Backend detection + model mapping ─────────────────────────────
    // Web visitors give us ONE key. We sniff the prefix to pick the
    // backend, then map the selected tier (fast / smart) to that
    // provider's equivalent model.
    function detectBackend(key) {
      if (!key) return '';
      const k = String(key).trim();
      if (k.startsWith('sk-ant-')) return 'anthropic';
      if (k.startsWith('sk-')) return 'openai';
      if (k.startsWith('AIza')) return 'google';
      return '';
    }

    const MODEL_MAP = {
      anthropic: { fast: 'claude-sonnet-5', smart: 'claude-opus-5', top: 'claude-opus-5' },
      openai:    { fast: 'gpt-4.1',          smart: 'gpt-5.5',           top: 'gpt-5.5' },
      google:    { fast: 'gemini-3.1-flash-lite', smart: 'gemini-3.5-flash', top: 'gemini-3.5-flash' },
    };

    function resolveModel(backend, tier) {
      const m = MODEL_MAP[backend];
      if (!m) return '';
      if (tier === 'top') return m.top || m.smart;
      return tier === 'smart' ? m.smart : m.fast;
    }

    // Short, human-friendly model labels for the Fast/Smart dropdown so
    // the user sees what they're picking. Keyed by the same backend
    // names detectBackend() returns.
    const MODEL_LABEL = {
      anthropic: { fast: 'Sonnet 5', smart: 'Opus 5', top: 'Opus 5' },
      openai:    { fast: 'GPT-4.1',   smart: 'GPT-5.5',    top: 'GPT-5.5' },
      google:    { fast: 'Gemini 3.1 Flash-Lite', smart: 'Gemini 3.5 Flash', top: 'Gemini 3.5 Flash' },
    };

    function updateDeepModelLabels() {
      // Refresh the Fast/Smart dropdown labels based on whatever key is
      // currently cached. Called on page load and after any key prompt
      // so the user sees concrete model names like "Fast (cost: Sonnet 5)".
      const sel = document.getElementById('deep-model');
      if (!sel) return;
      const key = _LLM_KEY || _ANTHROPIC_KEY || _OPENAI_KEY ||
        (window._GEMINI_KEY || '');
      const backend = detectBackend(key);
      const labels = MODEL_LABEL[backend];
      const fastOpt = sel.querySelector('option[value="fast"]');
      const smartOpt = sel.querySelector('option[value="smart"]');
      if (fastOpt) fastOpt.textContent = labels
        ? 'Fast (cost: ' + labels.fast + ')'
        : 'Fast (cost: 모델 자동 선택)';
      if (smartOpt) smartOpt.textContent = labels
        ? 'Smart (quality: ' + labels.smart + ')'
        : 'Smart (quality: 모델 자동 선택)';
    }

    function deepWebSearchOn() {
      const el = document.getElementById('deep-websearch');
      return !!(el && el.checked);
    }

    // 웹 검색 ON일 때 system 에 덧붙이는 규칙. 기본 규칙("발췌 외 지식 사용 금지")
    // 과 충돌하지 않도록 웹 출처의 사용 조건과 표기법을 명시한다 — [ref:N] 은
    // 코퍼스 발췌 전용이고, 웹 출처는 마크다운 링크로만 표기한다.
    const WEB_SEARCH_ADDENDUM = '\\n\\nWEB SEARCH MODE: the web_search tool is enabled for this request. Corpus excerpts remain the PRIMARY source and [ref:N] markers apply ONLY to them. You MAY search the web when recent news, tech-company blog posts, or papers outside the corpus would materially improve the answer. Attribute every web-sourced claim inline as a markdown link [source name](url) — never with [ref:N]. Use a descriptive source name (publication or article title), never a bare URL — the client converts each link into a numbered entry in the References list. If web results conflict with corpus excerpts, say so explicitly.';

    async function callAnthropic(apiKey, model, prompt, spec, onDelta) {
      let maxTokens = spec.max_tokens;
      let thinkingBudget = spec.thinking;
      if (model.indexOf('haiku') !== -1 && maxTokens > 8000) {
        maxTokens = 8000;
        if (thinkingBudget > 2500) thinkingBudget = 2500;
      }
      const body = {
        model: model,
        max_tokens: maxTokens,
        system: prompt.system,
        messages: [{ role: 'user', content: prompt.user }],
        stream: true,
      };
      if (deepWebSearchOn()) {
        // Sonnet 5 / Opus 5 는 dynamic-filtering 신형(web_search_20260209) 지원.
        // (구 Haiku 4.5 만 web_search_20250305 — 현재 매핑엔 없음.) 서버 툴이라 브라우저
        // BYOK 에서 그대로 동작하고, 스트림 파서는 text_delta 외 블록을 무시한다.
        body.tools = [{
          type: /haiku-4-5/.test(model) ? 'web_search_20250305' : 'web_search_20260209',
          name: 'web_search',
          max_uses: 5,
        }];
        body.system = prompt.system + WEB_SEARCH_ADDENDUM;
      }
      // Adaptive-thinking models (Opus 5, Sonnet 5, Fable 5) REJECT the
      // legacy budget-based thinking.type.enabled (HTTP 400). Send it ONLY to
      // models known to take the explicit budget form — whitelist, so any
      // future model defaults to no thinking param (safe on both kinds).
      if (/sonnet-4-6|haiku-4-5/.test(model)) {
        body.thinking = { type: 'enabled', budget_tokens: thinkingBudget };
      }
      const resp = await deepFetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: {
          'content-type': 'application/json',
          'x-api-key': apiKey,
          'anthropic-version': '2023-06-01',
          'anthropic-dangerous-direct-browser-access': 'true',
        },
        body: JSON.stringify(body),
      });
      if (!resp.ok) {
        const err = await resp.text();
        throw new Error('Anthropic ' + resp.status + ': ' + err.slice(0, 300));
      }
      const reader = resp.body.getReader();
      const decoder = new TextDecoder();
      let buffer = '';
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });
        let idx;
        while ((idx = buffer.indexOf('\\n\\n')) !== -1) {
          const block = buffer.slice(0, idx);
          buffer = buffer.slice(idx + 2);
          for (const line of block.split('\\n')) {
            if (!line.startsWith('data: ')) continue;
            const payload = line.slice(6);
            if (payload === '[DONE]') continue;
            let ev;
            try { ev = JSON.parse(payload); } catch { continue; }
            if (ev.type === 'content_block_start') {
              if (ev.content_block.type === 'thinking') deepSetStatus('\U0001F914 답변 계획 중...');
              else if (ev.content_block.type === 'text') deepSetStatus('\u270D\uFE0F 답변 작성 중...');
            } else if (ev.type === 'content_block_delta') {
              if (ev.delta.type === 'text_delta') onDelta(ev.delta.text);
            } else if (ev.type === 'error') {
              throw new Error('Anthropic stream error: ' + (ev.error && ev.error.message || JSON.stringify(ev)));
            }
          }
        }
      }
    }

    async function callOpenAI(apiKey, model, prompt, spec, onDelta) {
      const body = {
        model: model,
        messages: [
          { role: 'system', content: prompt.system },
          { role: 'user', content: prompt.user },
        ],
        max_completion_tokens: spec.max_tokens,
        stream: true,
      };
      if (model.indexOf('gpt-5') === 0) {
        body.reasoning_effort = 'high';
      }
      deepSetStatus('\u270D\uFE0F 답변 작성 중...');
      const resp = await deepFetch('https://api.openai.com/v1/chat/completions', {
        method: 'POST',
        headers: {
          'content-type': 'application/json',
          'authorization': 'Bearer ' + apiKey,
        },
        body: JSON.stringify(body),
      });
      if (!resp.ok) {
        const err = await resp.text();
        throw new Error('OpenAI ' + resp.status + ': ' + err.slice(0, 300));
      }
      const reader = resp.body.getReader();
      const decoder = new TextDecoder();
      let buffer = '';
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });
        let idx;
        while ((idx = buffer.indexOf('\\n\\n')) !== -1) {
          const block = buffer.slice(0, idx);
          buffer = buffer.slice(idx + 2);
          for (const line of block.split('\\n')) {
            if (!line.startsWith('data: ')) continue;
            const payload = line.slice(6).trim();
            if (payload === '[DONE]') continue;
            let ev;
            try { ev = JSON.parse(payload); } catch { continue; }
            const ch = ev.choices && ev.choices[0];
            if (!ch) continue;
            const txt = ch.delta && ch.delta.content;
            if (txt) onDelta(txt);
            if (ch.finish_reason === 'length') {
              throw new Error('OpenAI: response truncated (max_completion_tokens).');
            }
          }
        }
      }
    }

    async function callGoogle(apiKey, model, prompt, spec, onDelta) {
      const body = {
        systemInstruction: { parts: [{ text: prompt.system }] },
        contents: [{ role: 'user', parts: [{ text: prompt.user }] }],
        generationConfig: { maxOutputTokens: spec.max_tokens, temperature: 0.7 },
      };
      if (deepWebSearchOn()) {
        // Gemini 는 Google Search grounding 툴로 동일 기능 제공.
        body.tools = [{ google_search: {} }];
        body.systemInstruction = { parts: [{ text: prompt.system + WEB_SEARCH_ADDENDUM }] };
      }
      const url = 'https://generativelanguage.googleapis.com/v1beta/models/'
        + encodeURIComponent(model) + ':streamGenerateContent?alt=sse&key=' + encodeURIComponent(apiKey);
      deepSetStatus('\u270D\uFE0F 답변 작성 중...');
      const resp = await deepFetch(url, {
        method: 'POST',
        headers: { 'content-type': 'application/json' },
        body: JSON.stringify(body),
      });
      if (!resp.ok) {
        const err = await resp.text();
        throw new Error('Google ' + resp.status + ': ' + err.slice(0, 300));
      }
      const reader = resp.body.getReader();
      const decoder = new TextDecoder();
      let buffer = '';
      let logged = false;
      // SSE separator: spec says LF-LF, but some Google endpoints emit
      // CRLF-CRLF. Use a regex that accepts either, and split lines
      // with /\\r?\\n/ for the same reason. Earlier versions only
      // matched LF and silently dropped the stream on CRLF responses.
      const SEP_RE = /\\r?\\n\\r?\\n/;
      const LINE_RE = /\\r?\\n/;
      const parseBlock = (block) => {
        for (const line of block.split(LINE_RE)) {
          if (!line.startsWith('data:')) continue;
          // Tolerate "data:foo" as well as "data: foo".
          const payload = line.slice(5).replace(/^ /, '').trim();
          if (!payload || payload === '[DONE]') continue;
          let ev;
          try { ev = JSON.parse(payload); } catch { continue; }
          const cand = ev.candidates && ev.candidates[0];
          if (!cand) continue;
          const parts = cand.content && cand.content.parts;
          if (parts) {
            for (const p of parts) {
              if (p.text) onDelta(p.text);
            }
          }
        }
      };
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });
        if (!logged) {
          console.log('[callGoogle] first chunk (200 chars):', JSON.stringify(buffer.slice(0, 200)));
          logged = true;
        }
        let m;
        while ((m = SEP_RE.exec(buffer)) !== null) {
          const block = buffer.slice(0, m.index);
          buffer = buffer.slice(m.index + m[0].length);
          parseBlock(block);
        }
      }
      // Process any remaining buffered chunk (Google sometimes closes
      // the stream without a trailing blank line on the final event).
      if (buffer.trim()) parseBlock(buffer);
    }

    async function callLLM(query, selected, lang, tier, length, fullTexts, deeper) {
      const apiKey = _LLM_KEY || _ANTHROPIC_KEY;
      if (!apiKey) throw new Error('API key missing — Deep Research \uD328\uB110\uC5D0\uC11C \uD0A4\uB97C \uC785\uB825\uD558\uC138\uC694 (Anthropic / OpenAI / Google \uC911 \uD558\uB098).');
      const backend = detectBackend(apiKey);
      if (!backend) throw new Error('\uC54C \uC218 \uC5C6\uB294 API key \uD615\uC2DD\uC785\uB2C8\uB2E4 (Anthropic\uC740 sk-ant-, OpenAI\uB294 sk-, Google\uC740 AIza \uB85C \uC2DC\uC791).');
      const model = resolveModel(backend, tier);
      const spec = LENGTH_SPEC[length] || LENGTH_SPEC.short;
      const p = buildPrompt(query, selected, lang, fullTexts, deeper);
      p.system += '\\n\\n' + (lang === 'ko'
        ? '\uBD84\uB7C9 \uC9C0\uCE68: \uB2F5\uBCC0\uC744 ' + spec.ko + '\uB85C \uC791\uC131\uD558\uC138\uC694. \uBD84\uB7C9\uC774 \uAE38\uC218\uB85D \uAC01 \uB17C\uBB38\uC744 \uB354 \uAE4A\uC774 \uC788\uAC8C \uB2E4\uB8E8\uACE0, \uC8FC\uC81C \uADF8\uB8F9\uC744 \uB354 \uC138\uBD84\uD654\uD558\uC138\uC694.'
        : 'Length directive: write the answer as ' + spec.en + '. Longer lengths should cover each paper in more depth and introduce finer thematic subdivisions.');
      const onDelta = (txt) => {
        DEEP.currentAnswer += txt;
        renderDeepAnswer(DEEP.currentAnswer);
      };
      DEEP.lastBackend = backend;
      DEEP.lastModel = model;
      if (backend === 'anthropic') return callAnthropic(apiKey, model, p, spec, onDelta);
      if (backend === 'openai')    return callOpenAI(apiKey, model, p, spec, onDelta);
      if (backend === 'google')    return callGoogle(apiKey, model, p, spec, onDelta);
      throw new Error('Unsupported backend: ' + backend);
    }

    // Backward-compat alias for existing callers (e.g. localhost dev
    // entry points that still reference callClaude).
    async function callClaude(query, selected, lang, model, length, fullTexts) {
      const tier = (model && model.indexOf('haiku') !== -1) ? 'fast' : 'smart';
      return callLLM(query, selected, lang, tier, length, fullTexts);
    }

    function renderDeepAnswer(md) {
      const el = document.getElementById('deep-answer');
      if (!el) return;
      // Defend against every step in the markup pipeline. A failure in
      // mdToMarkup (e.g. marked.js throws on weird input) or in
      // postProcessRefs (e.g. refs array out of sync) used to silently
      // wipe the visible answer mid-stream — DEEP.currentAnswer still
      // held the raw text but the user saw an empty panel. Now we fall
      // back to escaped raw markdown so something always shows, and
      // surface the error to the console for debugging.
      let markup = '';
      try { markup = mdToMarkup(md) || ''; }
      catch (e) { console.warn('mdToMarkup failed:', e); markup = ''; }
      try { markup = postProcessRefs(markup, DEEP.currentRefs); }
      catch (e) { console.warn('postProcessRefs failed:', e); }
      if (!markup) {
        const escaped = String(md || '')
          .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
        markup = '<p>' + escaped.replace(/\\n\\n+/g, '</p><p>') + '</p>';
      }
      // deepShowPanel is idempotent — call it here so the body stays
      // visible even if a prior error path removed the .active class.
      const body = document.getElementById('deep-body');
      if (body && !body.classList.contains('active')) body.classList.add('active');
      renderTo(el, markup);
    }

    // 취합기(assembler)가 리포트 본문 대신 자기 역할·편집 지침을 복창하는 서두 메타
    // ("책임 편집장으로서 … 취합하겠습니다 / 초안을 파악했습니다 / [ref:N] 마커를 보존합니다")
    // 를 제거. 첫 마크다운 제목 이전 구간에서 메타 단서를 가진 선두 문장만 하나씩 떼고
    // 첫 정상 문장에서 멈춘다 — 정상 서론/본문은 건드리지 않는다(프롬프트로도 금지).
    function stripDeepMeta(md) {
      const orig = String(md || '');
      let t = orig.replace(/^\\s+/, '');
      const hi = t.search(/(^|\\n)#{1,3}\\s/);
      let head = hi === -1 ? t : t.slice(0, hi);
      const rest = hi === -1 ? '' : t.slice(hi);
      let guard = 0;
      while (guard++ < 12) {
        const m = head.match(/^\\s*[^.!?。\\n]*?(초안|편집장|편집 지침|취합하|보존하겠|보존합니다|파악하겠|파악했|작성하겠|검토하겠|\\[ref:N\\] ?마커|figure를 모두|lead editor|assembl)[^.!?。\\n]*[.!?。]\\s*/);
        if (!m) break;
        head = head.slice(m[0].length);
      }
      const out = (head + rest).replace(/^\\s+/, '');
      return out.length > 0 ? out : orig;
    }
    // 섹션 작성기가 본문 앞에 흘리는 계획·사고과정 메타(KO "~하겠습니다", EN "Let me…/
    // The excerpts give me…")를 선두에서 문장 단위로 제거. 첫 정상 문장에서 멈춘다.
    function stripLeadingMeta(text) {
      let t = String(text || '').replace(/^\\s+/, '');
      const RE = /^\\s*[^.!?。\\n]*?(서술하겠|작성하겠|확인하겠|검토하겠|파악하겠|정리하겠|살펴보겠|하겠습니다|Let me\\b|Let's\\b|I['’]ll\\b|I will\\b|We['’]ll\\b|The excerpts?\\b|figure files?\\b|compose the paragraph|write the (paragraph|section)|before (writing|composing)|Here (is|are|'s))[^.!?。\\n]*[.!?。]\\s*/;
      let guard = 0;
      while (guard++ < 15 && RE.test(t)) t = t.replace(RE, '');
      return t.replace(/^\\s+/, '');
    }
    // 작성기가 [ref:N] 대신 맨 대괄호 [N]/[N, M] 로 인용한 경우를 [ref:N] 로 교정
    // (유효 범위 내 번호만). 마크다운 링크 [txt](url) 와 figure ![..] 는 건드리지 않음.
    function normalizeBareCites(text, refCount) {
      return String(text || '').replace(/(?<!!)\\[(\\d+(?:\\s*,\\s*\\d+)*)\\](?!\\()/g, function(m, grp) {
        const nums = grp.split(',').map(function(x) { return parseInt(x, 10); });
        if (!nums.every(function(n) { return n >= 1 && n <= refCount; })) return m;
        return nums.map(function(n) { return '[ref:' + n + ']'; }).join('');
      });
    }
    function sanitizeSectionDraft(text, refCount) {
      return normalizeBareCites(stripLeadingMeta(text), refCount);
    }
    function finalizeDeepAnswer() {
      // 취합기가 리포트 대신 역할·지침을 복창하는 서두 메타를 제거 (프롬프트로도 금지하지만 방어).
      try {
        const _sm = stripDeepMeta(DEEP.currentAnswer);
        if (_sm !== DEEP.currentAnswer) { DEEP.currentAnswer = _sm; renderDeepAnswer(DEEP.currentAnswer); }
      } catch (e) { console.warn('[meta-strip] skipped:', e && e.message || e); }
      // 웹 검색 실행(토글 ON)의 인라인 웹 링크를 번호 레퍼런스로 흡수 —
      // 일반 실행의 본문 링크는 건드리지 않는다. 인용 가드보다 먼저 돌아야
      // 새로 붙은 번호가 가드에서 살아남는다.
      try {
        if (DEEP.webUsed) {
          const _wc = absorbWebCitations(DEEP.currentAnswer, DEEP.currentRefs);
          if (_wc.changed) {
            DEEP.currentAnswer = _wc.answer;
            renderDeepAnswer(DEEP.currentAnswer);
          }
        }
      } catch (e) { console.warn('[web-cite] skipped:', e && e.message || e); }
      // T2-3 citation guard: strip [ref:N] that point at no retrieved paper
      // before the references list / figures are built from cited nums, and
      // surface a small note. Wrapped so any failure falls back to the prior
      // (un-guarded) behavior. Disable with window._DR_CITE_GUARD = false.
      try {
        if (window._DR_CITE_GUARD !== false) {
          const _cg = guardDanglingCitations(DEEP.currentAnswer, DEEP.currentRefs);
          if (_cg.changed) {
            DEEP.currentAnswer = _cg.answer;
            renderDeepAnswer(DEEP.currentAnswer);
            deepRenderCiteWarning(_cg.dropped);
          } else {
            deepRenderCiteWarning(null);
          }
        }
      } catch (e) { console.warn('[cite-guard] skipped:', e && e.message || e); }
      const cited = collectCitedNums(DEEP.currentAnswer);
      const refsListEl = document.getElementById('deep-refs-list');
      clearEl(refsListEl);
      if (cited.size > 0) {
        const ordered = [...cited].sort((a, b) => a - b);
        for (const n of ordered) {
          const ref = DEEP.currentRefs[n - 1];
          if (!ref) continue;
          const li = document.createElement('li');
          li.appendChild(document.createTextNode('[' + n + '] ' + (ref.web ? '\U0001F310 ' : '')));
          const link = document.createElement('a');
          link.href = ref.url;
          link.target = '_blank';
          link.textContent = ref.title;
          li.appendChild(link);
          if (ref.year) li.appendChild(document.createTextNode(' (' + ref.year + ')'));
          else if (ref.web) {
            // 웹 출처는 연도 대신 도메인으로 출처를 드러낸다 (제목이 이미
            // 도메인과 같으면 중복 표기 생략).
            let _h = '';
            try { _h = new URL(ref.url).hostname.replace(/^www\\./, ''); } catch (e) {}
            if (_h && _h !== ref.title) li.appendChild(document.createTextNode(' — ' + _h));
          }
          // Local-only: render a 'Open PDF' button when we have a Zotero itemKey
          // for this paper. Clicking it triggers the zotero:// protocol handler
          // and the Zotero desktop app pops the PDF immediately.
          if (window._zoteroKeys && window._zoteroKeys[ref.slug]) {
            const pdfLink = document.createElement('a');
            pdfLink.href = 'zotero://open-pdf/library/items/' + window._zoteroKeys[ref.slug];
            pdfLink.title = 'Open PDF in Zotero';
            pdfLink.textContent = '\U0001F4C4 PDF';
            pdfLink.style.marginLeft = '0.5rem';
            pdfLink.style.fontSize = '0.75rem';
            pdfLink.style.color = '#555';
            pdfLink.style.textDecoration = 'none';
            pdfLink.style.padding = '0.05rem 0.4rem';
            pdfLink.style.borderRadius = '3px';
            pdfLink.style.background = '#f0f0f0';
            pdfLink.style.border = '1px solid #ddd';
            li.appendChild(pdfLink);
          }
          refsListEl.appendChild(li);
        }
        document.getElementById('deep-refs').style.display = '';
      }
      const usedInBody = collectInlineFigureUrls(DEEP.currentAnswer);
      const grid = document.getElementById('deep-figures-grid');
      clearEl(grid);
      let added = 0;
      for (const n of [...cited].sort((a, b) => a - b)) {
        const ref = DEEP.currentRefs[n - 1];
        if (!ref || !ref.figures || !ref.figures.length) continue;
        for (const fig of ref.figures) {
          if (usedInBody.has(fig.url)) continue;
          const div = document.createElement('div');
          div.className = 'deep-fig-item';
          const link = document.createElement('a');
          link.href = ref.url;
          link.target = '_blank';
          link.title = ref.title + ' — ' + (fig.caption || '');
          const img = document.createElement('img');
          img.src = fig.url;
          img.alt = fig.caption || '';
          const cap = document.createElement('div');
          cap.className = 'fig-cap';
          cap.textContent = '[' + n + '] ' + (fig.caption || 'Figure');
          link.appendChild(img);
          link.appendChild(cap);
          div.appendChild(link);
          grid.appendChild(div);
          added++;
          if (added >= 20) break;
        }
        if (added >= 20) break;
      }
      document.getElementById('deep-figures').style.display = added > 0 ? '' : 'none';
      deepUpdateButtons(true);
    }

    // Detect provider-side auth failures. Each provider returns a
    // different shape -- Anthropic uses 401 + 'authentication_error',
    // OpenAI uses 401 + 'invalid_api_key', Google returns 400 with
    // 'API_KEY_INVALID' / 'API key not valid'. We check all of them so
    // a single bad-key path catches any backend.
    function isAuthError(err) {
      if (!err || !err.message) return false;
      const m = err.message;
      if (/\\b(401|403)\\b/.test(m)) return true;
      if (/invalid[_ ]?api[_ ]?key/i.test(m)) return true;
      if (/incorrect api key/i.test(m)) return true;
      if (/api key not valid/i.test(m)) return true;
      if (/API_KEY_INVALID/i.test(m)) return true;
      if (/authentication_error/i.test(m)) return true;
      if (/unauthorized/i.test(m)) return true;
      return false;
    }

    // Query embedding now goes through the same-origin /api/embed proxy
    // (no reader key), so every auth failure that reaches here belongs to
    // the answer-generation backend.
    function authErrorScope(err) {
      return 'llm';
    }

    // Wipe the offending key from BOTH globals and localStorage, then
    // pop a fresh prompt with the "API Key Invalid. Try with another
    // one" prefix. Returns the new key, or null if the user cancels.
    function clearKeyAndRePrompt(scope) {
      // LLM (answer-generation) scope -- also drop the cached
      // Anthropic/Gemini aliases so a Google key isn't silently
      // re-used for audio after the user replaces a bad LLM key.
      _LLM_KEY = '';
      _ANTHROPIC_KEY = '';
      try {
        localStorage.removeItem('_LLM_KEY');
        localStorage.removeItem('_ANTHROPIC_KEY');
      } catch (e) {}
      const nk = prompt('API Key Invalid. Try with another one.\\n\\n답변 생성용 API Key를 입력하세요 (Anthropic sk-ant-… / OpenAI sk-… / Google AIza… 중 하나):');
      if (!nk) return null;
      const b = detectBackend(nk);
      if (!b) {
        deepSetStatus('알 수 없는 키 형식입니다 (sk-ant- / sk- / AIza 중 하나로 시작).', true);
        return null;
      }
      _LLM_KEY = nk;
      try { localStorage.setItem('_LLM_KEY', nk); } catch (e) {}
      if (b === 'anthropic') {
        _ANTHROPIC_KEY = nk;
        try { localStorage.setItem('_ANTHROPIC_KEY', nk); } catch (e) {}
      } else if (b === 'google') {
        window._GEMINI_KEY = nk;
        try { localStorage.setItem('_GEMINI_KEY', nk); } catch (e) {}
      }
      updateDeepModelLabels();
      return nk;
    }

    // ── Deeper Research: expand over the paper-connection graph ────────
    // Seed retrieval finds the core papers for the query; we then pull their
    // KNOWN connected papers (foundation / extension / alternative /
    // application / counterpoint) from _paper_connections.json and synthesize
    // across the neighbourhood so the answer traces lineage + counterpoints.
    const RELATION_KO = {
      foundation: '기반', extension: '후속·확장', alternative: '대안',
      application: '응용', counterpoint: '반론', related: '관련'
    };

    async function loadConnections() {
      if (DEEP._conn) return DEEP._conn;
      try {
        const r = await fetch('_paper_connections.json');
        DEEP._conn = r.ok ? await r.json() : {};
      } catch (e) { DEEP._conn = {}; }
      return DEEP._conn;
    }

    // Representative chunk {section,text} for a paper slug (Essence-first).
    function bestChunkForSlug(index, slug) {
      const cbs = _chunkIdxBySlug(index);
      const idxs = cbs[slug];
      if (!idxs || !idxs.length) return null;
      let best = idxs[0], bestRank = 99;
      for (const ci of idxs) {
        const rnk = _sectionRank((index.chunks[ci] || {}).section);
        if (rnk < bestRank) { bestRank = rnk; best = ci; }
      }
      const c = index.chunks[best];
      return { section: c.section, text: c.text };
    }

    // Render the expansion structure into #deep-plan (core + connected by relation).
    function deepRenderExpansion(seeds, connected) {
      const wrap = document.getElementById('deep-plan');
      const list = document.getElementById('deep-plan-list');
      if (!wrap || !list) return;
      const title = wrap.querySelector(':scope > .deep-plan-title');
      if (title) title.textContent = '\U0001F578️ 연결 그래프 — 핵심 ' + seeds.length + '편 · 연결 ' + connected.length + '편';
      clearEl(list);
      function addItem(label, rel) {
        const li = document.createElement('li');
        const t = document.createElement('span');
        t.className = 'rtext';
        t.textContent = label;
        li.appendChild(t);
        if (rel) {
          const stat = document.createElement('span');
          stat.className = 'rstat';
          stat.textContent = rel;
          li.appendChild(stat);
          li.classList.add('done');
        }
        list.appendChild(li);
      }
      for (const s of seeds) addItem('★ ' + (s.paper.title || s.slug), '핵심');
      for (const c of connected) addItem((c.paper.title || c.slug), RELATION_KO[c.relation] || c.relation);
      wrap.classList.add('active');
      wrap.style.display = 'block';
    }

    // Numbered evidence block for the multi-agent report (curated review
    // excerpts + relation tags + figure URLs + optional windowed text.md (fullTexts). Numbering
    // matches DEEP.currentRefs so [ref:N] stays consistent across all agents.
    function buildEvidenceText(selected, allowSet, fullTexts) {
      const lines = [];
      for (let i = 0; i < selected.length; i++) {
        if (allowSet && !allowSet.has(i + 1)) continue;
        const s = selected[i], n = i + 1, paper = s.paper;
        const figs = (paper.figures && paper.figures.length)
          ? '\\n  Figures:\\n' + paper.figures.map(function(f) { return '    - ' + f.url + '  (' + (f.caption || 'figure') + ')'; }).join('\\n')
          : '';
        const sectionsBlock = (s.chunks || []).map(function(c) {
          return '  Section: ' + c.section + '\\n  Text:\\n' + c.text.split('\\n').map(function(l) { return '    ' + l; }).join('\\n');
        }).join('\\n');
        const fa = paper.first_author || '';
        const authorTag = fa ? (' — ' + fa.split(/\\s+/).slice(-1)[0] + ' et al.') : '';
        const idTag = paper.doi ? (' [DOI: ' + paper.doi + ']') : (paper.arxiv ? (' [arXiv:' + paper.arxiv + ']') : '');
        const relTag = (s.relation && !s.isSeed)
          ? (' [연결관계: ' + (RELATION_KO[s.relation] || s.relation) + (s.reason ? (' — ' + s.reason) : '') + ']')
          : '';
        lines.push('[' + n + '] Paper: "' + paper.title + '"' + authorTag + ' (' + (paper.year || 'n/a') + ', category: ' + (paper.category || 'n/a') + ')' + idTag + relTag + figs + '\\n' + sectionsBlock);
        if (fullTexts && fullTexts[s.slug]) {
          lines[lines.length - 1] += '\\n  [원문 발췌 (method·실험·수치 밀집 구간)]:\\n    ' + fullTexts[s.slug];
        }
      }
      return 'Excerpts from paper reviews:\\n\\n' + lines.join('\\n\\n---\\n\\n');
    }

    // ── Deeper depth: windowed text.md for a section's top refs (LOCAL ONLY) ──
    // text.md is git-ignored → 404 on Cloudflare, so this silently falls back to
    // review excerpts there; on serve_local / the cross console it injects the
    // method/experiment/number-dense windows (mirrors build_search_index's
    // textmd_high_signal_chunks) so Deeper isn't shallower than Deep per paper.
    const DEEP_FT_PER_SECTION = 6;    // top refs per section that get full text
    const DEEP_FT_DOC_CAP = 9000;     // per-doc windowed char budget
    const _FT_SIGNAL_RE = /(method|approach|propos|algorithm|model|train|fine-?tun|dataset|benchmark|evaluat|experiment|result|ablation|baseline|accuracy|precision|recall|metric|hyper-?parameter|we (train|use|evaluate|propose|find|observe|measure|report))/i;
    const _FT_NUM_RE = /(\\d+(?:\\.\\d+)?\\s?%|\\d+\\.\\d+)/;
    const _FT_REF_RE = /^\\s*#{0,4}\\s*(references|bibliography|참고문헌|acknowledge?ments?)\\b/im;

    function _ftQueryTerms(query) {
      return String(query || '').toLowerCase().split(/[^a-z0-9\\uac00-\\ud7af]+/).filter(function(t) { return t.length > 3; });
    }
    function _ftHighSignal(raw, terms) {
      const m = _FT_REF_RE.exec(raw);
      let body = (m ? raw.slice(0, m.index) : raw).replace(/\\s+/g, ' ').trim();
      if (body.length > 150000) body = body.slice(0, 150000);
      if (body.length <= DEEP_FT_DOC_CAP) return body;
      const size = 1400, step = 1200, wins = [];
      for (let i = 0; i < body.length; i += step) wins.push(body.slice(i, i + size));
      const sig = new RegExp(_FT_SIGNAL_RE.source, 'gi'), num = new RegExp(_FT_NUM_RE.source, 'g');
      const scored = wins.map(function(w, idx) {
        const lw = w.toLowerCase();
        let q = 0; for (const t of terms) if (lw.indexOf(t) !== -1) q++;
        return { idx: idx, text: w, score: (w.match(sig) || []).length + (w.match(num) || []).length + 2 * q };
      });
      scored.sort(function(a, b) { return b.score - a.score; });
      const picked = []; let used = 0;
      for (const s of scored) {
        if (s.score <= 0 || picked.length >= 6) break;
        if (used + s.text.length > DEEP_FT_DOC_CAP) continue;
        picked.push(s); used += s.text.length;
      }
      if (!picked.length) return body.slice(0, DEEP_FT_DOC_CAP);
      picked.sort(function(a, b) { return a.idx - b.idx; });
      return picked.map(function(p) { return p.text; }).join(' … ');
    }
    async function _ftFetch(slug, terms) {
      if (Object.prototype.hasOwnProperty.call(DEEP._ftCache, slug)) return DEEP._ftCache[slug];
      if (DEEP._ftInflight[slug]) return DEEP._ftInflight[slug];
      const p = (async function() {
        try {
          const r = await deepFetch('../papers/' + slug + '/text.md');
          if (!r.ok) return (DEEP._ftCache[slug] = null);
          const t = await r.text();
          return (DEEP._ftCache[slug] = _ftHighSignal(t, terms) || null);
        } catch (e) { return (DEEP._ftCache[slug] = null); }
        finally { delete DEEP._ftInflight[slug]; }
      })();
      DEEP._ftInflight[slug] = p;
      return p;
    }
    // For one section: windowed text.md for its top-N refs (by evidence rank,
    // seeds first). Returns { slug: windowedText }; 404/missing refs omitted.
    async function sectionFullTexts(sec, all, terms) {
      let idxs;
      if (sec.refs && sec.refs.length) {
        idxs = sec.refs.slice().sort(function(a, b) { return a - b; });
      } else {
        idxs = all.map(function(_, i) { return i + 1; });
      }
      const slugs = [];
      for (const n of idxs) {
        const s = all[n - 1];
        if (s && s.slug) slugs.push(s.slug);
        if (slugs.length >= DEEP_FT_PER_SECTION) break;
      }
      const out = {};
      await Promise.all(slugs.map(async function(slug) {
        const w = await _ftFetch(slug, terms);
        if (w) out[slug] = w;
      }));
      return out;
    }

    // Non-streaming completion across the 3 backends (configurable max tokens).
    // Used by the report planner + per-section writer agents.
    async function llmComplete(backend, apiKey, model, sys, user, maxTokens, web) {
      const mt = maxTokens || 2048;
      // 웹 검색 툴은 web=true(섹션 작성기) + 토글 ON 일 때만 켠다. planner 는 web 미전달 → 코퍼스 전용.
      // OpenAI 는 web_search 미지원이라 코퍼스 전용 유지 (일반 Deep 과 동일).
      const useWeb = !!web && deepWebSearchOn();
      if (backend === 'anthropic') {
        const abody = { model: model, max_tokens: mt, system: useWeb ? (sys + WEB_SEARCH_ADDENDUM) : sys, messages: [{ role: 'user', content: user }] };
        if (useWeb) abody.tools = [{ type: /haiku-4-5/.test(model) ? 'web_search_20250305' : 'web_search_20260209', name: 'web_search', max_uses: 3 }];
        const resp = await deepFetch('https://api.anthropic.com/v1/messages', {
          method: 'POST',
          headers: { 'content-type': 'application/json', 'x-api-key': apiKey,
            'anthropic-version': '2023-06-01', 'anthropic-dangerous-direct-browser-access': 'true' },
          body: JSON.stringify(abody),
        });
        if (!resp.ok) { const eb = await resp.text().catch(function(){ return ''; }); throw new Error('Anthropic complete ' + resp.status + ': ' + eb.slice(0, 300)); }
        const data = await resp.json();
        let t = '';
        if (data.content) for (const b of data.content) if (b.type === 'text' && b.text) t += b.text;
        return t;
      }
      if (backend === 'openai') {
        const resp = await deepFetch('https://api.openai.com/v1/chat/completions', {
          method: 'POST',
          headers: { 'content-type': 'application/json', 'authorization': 'Bearer ' + apiKey },
          body: JSON.stringify({ model: model, messages: [{ role: 'system', content: sys }, { role: 'user', content: user }], max_completion_tokens: mt }),
        });
        if (!resp.ok) { const eb = await resp.text().catch(function(){ return ''; }); throw new Error('OpenAI complete ' + resp.status + ': ' + eb.slice(0, 300)); }
        const data = await resp.json();
        return (data.choices && data.choices[0] && data.choices[0].message && data.choices[0].message.content) || '';
      }
      if (backend === 'google') {
        const url = 'https://generativelanguage.googleapis.com/v1beta/models/' + encodeURIComponent(model) + ':generateContent?key=' + encodeURIComponent(apiKey);
        const gbody = { systemInstruction: { parts: [{ text: useWeb ? (sys + WEB_SEARCH_ADDENDUM) : sys }] }, contents: [{ role: 'user', parts: [{ text: user }] }], generationConfig: { maxOutputTokens: mt } };
        if (useWeb) gbody.tools = [{ google_search: {} }];
        const resp = await deepFetch(url, {
          method: 'POST', headers: { 'content-type': 'application/json' },
          body: JSON.stringify(gbody),
        });
        if (!resp.ok) { const eb = await resp.text().catch(function(){ return ''; }); throw new Error('Google complete ' + resp.status + ': ' + eb.slice(0, 300)); }
        const data = await resp.json();
        const cand = data.candidates && data.candidates[0];
        const parts = cand && cand.content && cand.content.parts;
        let t = ''; if (parts) for (const p of parts) if (p.text) t += p.text;
        return t;
      }
      throw new Error('Unsupported backend: ' + backend);
    }

    // Fallback report outline derived from which relations are present.
    function defaultSections(all, lang) {
      const rels = {};
      for (const s of all) if (!s.isSeed && s.relation) rels[s.relation] = 1;
      const ko = lang === 'ko';
      const secs = [];
      secs.push(ko ? { title: '연구 배경과 기반', focus: 'foundation·핵심 논문의 문제의식과 기반' }
                   : { title: 'Background & Foundations', focus: 'foundation papers and the core problem' });
      secs.push(ko ? { title: '핵심 접근과 성과', focus: '핵심(seed) 논문들의 방법과 기여' }
                   : { title: 'Core Approaches & Contributions', focus: 'methods and contributions of the core papers' });
      if (rels.extension || rels.application)
        secs.push(ko ? { title: '후속 연구와 응용', focus: 'extension·application 논문들의 확장과 적용' }
                     : { title: 'Extensions & Applications', focus: 'extension/application papers' });
      if (rels.counterpoint || rels.alternative)
        secs.push(ko ? { title: '반론과 대안', focus: 'counterpoint·alternative 논문들의 비판과 대안' }
                     : { title: 'Counterpoints & Alternatives', focus: 'counterpoint/alternative papers' });
      secs.push(ko ? { title: '종합과 전망', focus: '전체를 아우르는 종합과 향후 방향' }
                   : { title: 'Synthesis & Outlook', focus: 'overall synthesis and outlook' });
      return secs;
    }

    // Orchestrator: plan 3-5 report sections (fast model, JSON). Falls back to
    // a relation-derived outline on any failure.
    async function planReportSections(query, all, aspects, lang, backend, apiKey) {
      const fallback = defaultSections(all, lang);
      const model = resolveModel(backend, 'fast');
      if (!model) return fallback;
      const lst = all.map(function(s, i) {
        const tag = s.isSeed ? '핵심' : (RELATION_KO[s.relation] || s.relation || '관련');
        return '[' + (i + 1) + '] (' + tag + ') ' + (s.paper.title || s.slug);
      }).join('\\n');
      const aspText = (aspects && aspects.length)
        ? aspects.map(function(a, i) { return '  ' + (i + 1) + '. ' + a; }).join('\\n') : '';
      const sys = (lang === 'ko')
        ? '당신은 학술 리서치 리포트의 구조를 설계하는 편집장입니다. 조사 계획과 근거 논문 목록(핵심/연결관계 표시)을 보고, 모아진 논문들을 어떻게 연결할지 4~8개 단락으로 세밀하게 구성하세요. 연구 계보(기반→핵심→후속·응용→반론)가 드러나게 하고, 각 단락이 다룰 근거 논문 번호를 refs 배열로 지정하세요 — 모든 근거 논문이 최소 한 단락에는 포함되도록 폭넓게 분배하세요. 오직 JSON 배열만 출력: [{"title":"단락 제목","focus":"한 줄 요지","refs":[1,5,9]}]'
        : 'You design the structure of an academic research report. Given the investigation plan and the evidence list (core/relation-tagged), organise how the gathered papers connect into 4-8 fine-grained sections revealing the research lineage (foundation→core→extension/application→counterpoint). Assign each section the evidence paper numbers it covers via a refs array — distribute broadly so EVERY evidence paper appears in at least one section. Output ONLY a JSON array: [{"title":"...","focus":"...","refs":[1,5,9]}]';
      const user = (lang === 'ko' ? '질문: ' : 'Question: ') + query + '\\n\\n'
        + (aspText ? ((lang === 'ko' ? '조사 계획:\\n' : 'Investigation plan:\\n') + aspText + '\\n\\n') : '')
        + (lang === 'ko' ? '근거 논문:\\n' : 'Evidence papers:\\n') + lst + '\\n\\n'
        + (lang === 'ko' ? '4~8개 단락을 refs 포함 JSON 배열로.' : 'Return 4-8 sections (with refs) as a JSON array.');
      let text = '';
      try {
        text = await Promise.race([
          llmComplete(backend, apiKey, model, sys, user, 1500),
          new Promise(function(_, rej) { setTimeout(function() { rej(new Error('plan-timeout')); }, 20000); }),
        ]);
      } catch (e) { return fallback; }
      let arr = null;
      try { const m = String(text).match(/\\[[\\s\\S]*\\]/); if (m) arr = JSON.parse(m[0]); } catch (e) { arr = null; }
      if (!Array.isArray(arr) || !arr.length) return fallback;
      const N = all.length;
      const out = [];
      for (const v of arr) {
        if (v && typeof v.title === 'string' && v.title.trim()) {
          const refs = [];
          if (Array.isArray(v.refs)) {
            for (const r of v.refs) {
              const ri = parseInt(r);
              if (!isNaN(ri) && ri >= 1 && ri <= N && refs.indexOf(ri) === -1) refs.push(ri);
            }
          }
          out.push({ title: v.title.trim(), focus: (typeof v.focus === 'string' ? v.focus.trim() : ''), refs: refs });
        }
        if (out.length >= 8) break;
      }
      return out.length ? out : fallback;
    }

    // Per-section writer agent. Writes ONE section body from the shared
    // numbered evidence, citing [ref:N]. Returns markdown (no heading).
    async function writeSection(query, all, lang, backend, apiKey, model, sec, fullTexts) {
      const refSet = (sec.refs && sec.refs.length) ? new Set(sec.refs) : null;
      const evidence = buildEvidenceText(all, refSet, fullTexts);
      const sys = (lang === 'ko')
        ? '당신은 리서치 리포트의 한 단락을 집필하는 전문 작성자입니다. 아래 번호가 매겨진 발췌문만 근거로, 지정된 단락 주제를 자연스러운 한국어 서술로 작성하세요.\\n\\n인용 규칙(가장 중요):\\n- 논문을 지칭하는 모든 문장에 **반드시** ``[ref:N]`` 마커를 붙이세요(N=발췌 번호). "한 서베이는~", "또 다른 연구는~"처럼 논문을 언급하면서 마커를 빠뜨리면 안 됩니다.\\n- 형식은 **오직 ``[ref:N]``** 만 허용. ``[N]``·"[19]" 같은 맨 대괄호나 논문 제목만 쓰는 것은 금지 — 후처리는 ``[ref:N]`` 만 링크로 변환합니다.\\n- 여러 근거는 ``[ref:1][ref:2]`` 처럼 이어 붙이세요. 예: "He et al.은 ~을 제안했다[ref:3].", "이를 확장한 후속 연구[ref:7]는~", "이에 대한 반론[ref:12]도 제기됐다."\\n\\n출력 규칙:\\n- 단락 제목·머리말 없이 **본문만** 출력. "~하겠습니다"·"먼저 ~ 확인하겠습니다"·"Let me ~"·"The excerpts give me ~" 같은 계획·사고과정 메타를 절대 출력하지 말고 곧바로 한국어 본문 문장부터 시작하세요(영어 메타 문장 금지).\\n- 발췌 밖 지식 금지, 근거 없는 주장 생략. 발췌 논문을 폭넓게 활용하되 단락 주제와 무관한 논문은 인용하지 마세요.\\n- [연결관계:] 태그가 있는 논문은 그 관계를 문장에 녹이세요. 연관 Figure는 ![caption](url) 로 삽입(발췌에 명시된 URL만, 임의 URL 금지).'
        : 'You write ONE section of a research report from the numbered excerpts below, in natural Korean prose.\\n\\nCITATION RULES (most important):\\n- EVERY sentence that refers to a paper MUST carry a [ref:N] marker (N = excerpt number). Never mention a paper ("one survey…", "another study…") without its [ref:N].\\n- Use ONLY the [ref:N] form. Bare brackets like [19] or [N], or naming a paper with no marker, are forbidden — a post-processor converts ONLY [ref:N] into links.\\n- Chain multiple sources as [ref:1][ref:2].\\n\\nOUTPUT RULES:\\n- Output ONLY the body — no heading, no preamble, and NO planning/meta such as "I will…", "Let me…", "먼저 … 하겠습니다", "The excerpts give me…". Begin directly with the Korean prose (no English meta sentences).\\n- No outside knowledge; omit unsupported claims. Use the papers broadly but do not cite ones irrelevant to this section.\\n- For [연결관계:]-tagged papers weave the relation into the prose. Embed figures with ![caption](url) using only listed URLs.';
      const lenDir = (lang === 'ko')
        ? '\\n분량 지침: 이 단락을 8~15개 문단(약 1800~3600자)으로 매우 충실하고 자세하게 작성하세요.'
        : '\\nLength: write this section as 8-15 detailed paragraphs (~1500-3000 words).';
      const user = evidence + '\\n\\n---\\n'
        + (lang === 'ko' ? '작성할 단락: ' : 'Section to write: ') + sec.title + (sec.focus ? (' — ' + sec.focus) : '') + lenDir + '\\n'
        + (lang === 'ko' ? '원 질문: ' : 'Question: ') + query;
      return await llmComplete(backend, apiKey, model, sys, user, 9000, true);
    }

    // Orchestrator: assemble section drafts into one coherent report and
    // STREAM it into #deep-answer. Preserves [ref:N] markers + figures.
    async function assembleReport(query, drafts, lang, backend, apiKey, model) {
      const body = drafts.map(function(d) {
        return '## ' + d.title + '\\n' + (d.text || (lang === 'ko' ? '(내용 없음)' : '(no content)'));
      }).join('\\n\\n');
      const sys = (lang === 'ko')
        ? '당신은 여러 단락 초안을 하나의 일관된 한국어 리서치 리포트로 취합하는 책임 편집장입니다. 규칙: (1) ``[ref:N]`` 인용 마커는 반드시 그대로 보존(번호 변경·삭제 금지). (2) 간결한 서론(질문 맥락)과 종합 결론을 추가. (3) **각 단락의 분량과 깊이를 최대한 보존하세요 — 요약·압축하지 말고**, 단락 간 명백히 중복되는 문장만 정리하며 매끄럽게 연결하고 ## 제목으로 구조화. (4) 연구 계보(기반→핵심→후속·응용→반론)가 한눈에 드러나게. (5) 초안에 있던 ![caption](url) figure 는 적절한 위치에 유지하되 새 URL 은 만들지 말 것. (6) 초안에 없는 사실을 새로 지어내지 말 것. (7) 초안의 인라인 웹 출처 링크 ``[source](url)`` 는 그대로 보존(변경·삭제 금지) — 후처리가 번호 레퍼런스로 흡수합니다. (8) **메타·서두 절대 금지**: 역할이나 이 규칙을 복창하지 말고, "~하겠습니다"·"초안을 파악했습니다" 같은 진행 설명 없이 곧바로 리포트 서론 문장부터 출력하세요.'
        : 'You are the lead editor assembling section drafts into ONE coherent Korean research report. Keep all [ref:N] markers exactly (never renumber or drop them); add a short intro and synthesizing conclusion; PRESERVE the depth and length of each section — do NOT summarize or compress, only trim clearly duplicated sentences across sections; structure with ## headings; make the research lineage (foundation→core→extension/application→counterpoint) clear; keep ![caption](url) figures from the drafts but invent no new URLs; preserve inline [source](url) web-source links from the drafts exactly (never alter or drop them); do not fabricate facts beyond the drafts. Output ONLY the report itself — no preamble, no restating your role or these rules, no "I will…"/"let me…" meta; begin directly with the report intro.';
      const user = (lang === 'ko' ? '원 질문: ' : 'Question: ') + query + '\\n\\n'
        + (lang === 'ko' ? '단락 초안:' : 'Section drafts:') + '\\n\\n' + body;
      const spec = { max_tokens: 60000, thinking: 8000 };
      const prompt = { system: sys, user: user };
      const onDelta = function(txt) { DEEP.currentAnswer += txt; renderDeepAnswer(DEEP.currentAnswer); };
      DEEP.lastBackend = backend;
      DEEP.lastModel = model;
      if (backend === 'anthropic') return callAnthropic(apiKey, model, prompt, spec, onDelta);
      if (backend === 'openai') return callOpenAI(apiKey, model, prompt, spec, onDelta);
      if (backend === 'google') return callGoogle(apiKey, model, prompt, spec, onDelta);
      throw new Error('Unsupported backend: ' + backend);
    }

    // Render the report-section progress as a SEPARATE numbered list that
    // starts at 1 (independent of the graph list above it).
    function deepRenderSections(sections) {
      const wrap = document.getElementById('deep-plan');
      if (!wrap) return;
      const old = document.getElementById('deep-sec-wrap');
      if (old) old.remove();
      const secWrap = document.createElement('div');
      secWrap.id = 'deep-sec-wrap';
      const hdr = document.createElement('div');
      hdr.className = 'deep-plan-title deep-sec-title';
      hdr.textContent = '\U0001F4DD 리포트 단락 (' + sections.length + ')';
      secWrap.appendChild(hdr);
      const ol = document.createElement('ol');
      ol.className = 'deep-plan-list';
      for (let i = 0; i < sections.length; i++) {
        const li = document.createElement('li');
        li.id = 'deep-sec-' + i;
        const t = document.createElement('span'); t.className = 'rtext';
        t.textContent = sections[i].title;
        const stat = document.createElement('span'); stat.className = 'rstat';
        stat.textContent = '대기';
        li.appendChild(t); li.appendChild(stat);
        ol.appendChild(li);
      }
      secWrap.appendChild(ol);
      wrap.appendChild(secWrap);
    }

    function deepMarkSection(i, statusText, done) {
      const li = document.getElementById('deep-sec-' + i);
      if (!li) return;
      const stat = li.querySelector('.rstat');
      if (stat) stat.textContent = statusText;
      if (done) li.classList.add('done');
    }

    // ── Two-stage planning for Deeper Research ─────────────────────────
    // Plan 1: decide WHAT to investigate before searching (pre-search).
    function buildInvestigationPrompt(query, lang) {
      const sys = (lang === 'ko')
        ? '당신은 학술 리서치 플래너입니다. 사용자의 질문에 깊이 있게 답하려면 어떤 측면을 조사해야 하는지 정하세요. 서로 다른 각도를 다루는 3~6개의 조사 관점(하위 질문)으로 분해하되, 각각은 독립적으로 문헌 검색이 가능한 구체적 문장이어야 합니다. 고유명사(저자명·모델명·데이터셋)는 관점에 그대로 유지하세요. 오직 문자열 JSON 배열만 출력: ["...","..."]'
        : 'You are an academic research planner. Decide which aspects must be investigated to answer the question in depth. Decompose into 3-6 investigation angles (sub-questions), each a specific, independently searchable statement; keep proper nouns (author/model/dataset names) intact. Output ONLY a JSON array of strings.';
      const user = (lang === 'ko' ? '질문: ' : 'Question: ') + query
        + (lang === 'ko' ? '\\n\\n3~6개의 조사 관점을 JSON 배열로.' : '\\n\\nReturn 3-6 aspects as a JSON array.');
      return { system: sys, user: user };
    }

    async function planInvestigation(query, lang, backend, apiKey) {
      const fallback = [query];
      const model = resolveModel(backend, 'fast');
      if (!model) return fallback;
      const pp = buildInvestigationPrompt(query, lang);
      let text = '';
      try {
        text = await Promise.race([
          llmComplete(backend, apiKey, model, pp.system, pp.user, 800),
          new Promise(function(_, rej) { setTimeout(function() { rej(new Error('plan-timeout')); }, 15000); }),
        ]);
      } catch (e) { return fallback; }
      let arr = null;
      try { const m = String(text).match(/\\[[\\s\\S]*\\]/); if (m) arr = JSON.parse(m[0]); } catch (e) { arr = null; }
      if (!Array.isArray(arr)) return fallback;
      const out = [];
      for (const v of arr) {
        if (typeof v === 'string' && v.trim()) out.push(v.trim());
        if (out.length >= 6) break;
      }
      return out.length ? out : fallback;
    }

    // Retrieve seed candidates for ONE investigation aspect. Returns [].
    async function retrieveSeeds(index, q) {
      const qv = await embedQuery(q);
      if (index.dim && qv.length !== index.dim) return [];
      const tf = parseTimeFilter(q);
      const jf = parseJournalFilter(q, index);
      const chrono = isChronological(q);
      const authorHit = matchCorpusAuthor(q, index);
      if (authorHit) {
        return authorCandidates(index, authorHit, qv, tf, chrono, jf) || [];
      }
      const cands = hybridRetrieve(index, qv, q, tf, jf, 16);
      if (!cands.length) return [];
      return await rerankCandidates(q, cands, 6);
    }

    // Render the investigation plan (Plan 1) as a separate numbered list,
    // prepended above the connection graph.
    function deepRenderAspects(aspects) {
      const wrap = document.getElementById('deep-plan');
      if (!wrap) return;
      const old = document.getElementById('deep-asp-wrap');
      if (old) old.remove();
      const w = document.createElement('div');
      w.id = 'deep-asp-wrap';
      const hdr = document.createElement('div');
      hdr.className = 'deep-plan-title';
      hdr.textContent = '\U0001F52D 조사 계획 (' + aspects.length + ')';
      w.appendChild(hdr);
      const ol = document.createElement('ol');
      ol.className = 'deep-plan-list';
      for (let i = 0; i < aspects.length; i++) {
        const li = document.createElement('li');
        li.id = 'deep-asp-' + i;
        const t = document.createElement('span'); t.className = 'rtext';
        t.textContent = aspects[i];
        const st = document.createElement('span'); st.className = 'rstat';
        st.textContent = '대기';
        li.appendChild(t); li.appendChild(st);
        ol.appendChild(li);
      }
      w.appendChild(ol);
      wrap.insertBefore(w, wrap.firstChild);
      wrap.classList.add('active');
      wrap.style.display = 'block';
    }

    function deepMarkAspect(i, statusText, done) {
      const li = document.getElementById('deep-asp-' + i);
      if (!li) return;
      const st = li.querySelector('.rstat');
      if (st) st.textContent = statusText;
      if (done) li.classList.add('done');
    }

    // Deeper Research orchestrator: two-stage planning (investigate -> connect)
    // around connection-graph expansion. Returns true if an answer was made.
    async function runDeeperResearch(index, query) {
      const lang = detectLang(query);
      DEEP._ftCache = {}; DEEP._ftInflight = {};  // per-run windowed text.md cache (로컬 전용)
      const _ftTerms = _ftQueryTerms(query);
      const apiKey = _LLM_KEY || _ANTHROPIC_KEY || _OPENAI_KEY || (window._GEMINI_KEY || '');
      const backend = detectBackend(apiKey);
      if (!backend) {
        throw new Error('알 수 없는 API key 형식입니다 (Anthropic sk-ant- / OpenAI sk- / Google AIza).');
      }
      const topModel = resolveModel(backend, 'top');
      const topLabel = (MODEL_LABEL[backend] && MODEL_LABEL[backend].top) || topModel;
      // PLAN 1 — investigation plan (pre-search): what aspects to research.
      deepSetStatus('\U0001F52D 조사 계획 수립 중...');
      const aspects = await planInvestigation(query, lang, backend, apiKey);
      deepThrowIfAborted();
      deepRenderAspects(aspects);
      // SEED retrieval per aspect (union) — broader than a single query.
      const seedMap = new Map();
      for (let ai = 0; ai < aspects.length; ai++) {
        deepThrowIfAborted();
        deepMarkAspect(ai, '검색 중...', false);
        deepSetStatus('\U0001F50D 핵심 논문 검색 중 (' + (ai + 1) + '/' + aspects.length + ')...');
        let sc = [];
        try {
          sc = await retrieveSeeds(index, aspects[ai]);
        } catch (e) {
          if (deepIsAbort(e)) throw e;  // user 중단 → stop the whole run
          if (e && e.message && e.message.indexOf('embed-proxy-unreachable') === 0) throw e;
          console.warn('[aspect] failed:', e && e.message || e);
          deepMarkAspect(ai, '실패', true);
          continue;
        }
        for (const s of sc) {
          const slug = s.chunk.slug;
          if (!seedMap.has(slug)) seedMap.set(slug, { slug: slug, paper: s.paper, chunks: [], best: s.rrf || 0, isSeed: true });
          const e = seedMap.get(slug);
          e.chunks.push({ section: s.chunk.section, text: s.chunk.text });
          if ((s.rrf || 0) > e.best) e.best = s.rrf || 0;
        }
        deepMarkAspect(ai, sc.length + '편', true);
      }
      if (!seedMap.size) {
        deepSetStatus('관련 논문을 찾지 못했어요. 질의를 다시 입력해보세요.', true);
        return false;
      }
      // Cap seeds (rank by best RRF) so connected papers get budget.
      const cappedSeeds = Array.from(seedMap.values()).sort(function(a, b) { return b.best - a.best; }).slice(0, 28);
      const seedSet = new Set(cappedSeeds.map(function(s) { return s.slug; }));
      // 2) Graph expansion — pull connected papers (typed) of the seeds.
      deepSetStatus('\U0001F578️ 연결된 후속·반론·기반 논문 확장 중...');
      const conn = await loadConnections();
      const expand = new Map();
      for (const seed of seedSet) {
        const lst = conn[seed] || [];
        for (const c of lst) {
          if (!c || !c.slug || seedSet.has(c.slug)) continue;
          if (!index.papers[c.slug]) continue;  // must exist in this topic index
          if (!expand.has(c.slug)) {
            expand.set(c.slug, { slug: c.slug, relation: c.relation || 'related', reason: c.reason || '', count: 0 });
          }
          const ex = expand.get(c.slug);
          ex.count += 1;
          // If another seed flags this target as dissent (counterpoint/alternative),
          // let that relation win the tag + ranking boost so rebuttals aren't buried.
          if (relBoost(c.relation || 'related') > relBoost(ex.relation)) {
            ex.relation = c.relation || 'related';
            ex.reason = c.reason || ex.reason;
          }
        }
      }
      // Rank by centrality (# seeds linking), gently boosting dissent
      // (counterpoint / alternative) so rebuttals aren't buried.
      function relBoost(rel) { return (rel === 'counterpoint' || rel === 'alternative') ? 0.5 : 0; }
      const connectedRanked = Array.from(expand.values())
        .sort(function(a, b) { return (b.count + relBoost(b.relation)) - (a.count + relBoost(a.relation)); })
        .slice(0, 80);
      const connectedEntries = [];
      for (const c of connectedRanked) {
        const paper = index.papers[c.slug];
        const ch = bestChunkForSlug(index, c.slug);
        if (!paper || !ch) continue;
        connectedEntries.push({ slug: c.slug, paper: paper, chunks: [ch], best: 0, isSeed: false, relation: c.relation, reason: c.reason });
      }
      deepRenderExpansion(cappedSeeds, connectedEntries);
      // Evidence set (seeds first, then connected). Renumber refs.
      const all = cappedSeeds.concat(connectedEntries).slice(0, 100);
      DEEP.currentRefs = all.map(function(s, i) {
        return { n: i + 1, slug: s.slug, title: s.paper.title, year: s.paper.year,
          url: s.paper.url, external_url: s.paper.external_url || '',
          authors: s.paper.authors || [], first_author: s.paper.first_author || '',
          doi: s.paper.doi || '', arxiv: s.paper.arxiv || '', figures: s.paper.figures || [] };
      });
      // PLAN 2 — connection/report-structure plan (post-expansion, fine-grained).
      deepSetStatus('\U0001F9E9 리포트 구조 설계 중 (' + all.length + '편 연결)...');
      const sections = await planReportSections(query, all, aspects, lang, backend, apiKey);
      deepThrowIfAborted();
      deepRenderSections(sections);
      // MAP — per-section agents write in parallel (each on its assigned refs).
      deepSetStatus('✍️ 단락별 작성 중 (' + sections.length + '개 에이전트 · ' + topLabel + ')...');
      const drafts = await Promise.all(sections.map(async function(sec, i) {
        deepMarkSection(i, '작성 중...', false);
        const secFT = await sectionFullTexts(sec, all, _ftTerms);  // 섹션 top refs 원문 윈도우 (404=요약 폴백)
        return writeSection(query, all, lang, backend, apiKey, topModel, sec, secFT)
          .then(function(txt) { const _tx = sanitizeSectionDraft(txt, all.length); deepMarkSection(i, _tx ? '완료' : '내용 없음', true); return { title: sec.title, text: _tx }; })
          .catch(function(e) {
            if (deepIsAbort(e)) throw e;  // user 중단 → abort the whole run
            if (isAuthError(e)) throw e;  // bad key → fail fast to the outer retry
            console.warn('[section] failed:', e && e.message || e);
            deepMarkSection(i, '실패', true);
            return { title: sec.title, text: '' };
          });
      }));
      // 6) Orchestrator assembles + streams the final report into #deep-answer.
      deepSetStatus('\U0001F9F5 최종 리포트 취합 중 (' + topLabel + ')...');
      // The assembler can throw (e.g. a provider rejects the large max_tokens,
      // or a mid-stream network error). Don't lose the whole report: clear the
      // partial stream and let the ref-integrity guard below rebuild from the
      // section drafts (which already carry correct [ref:N]).
      try {
        // 취합기는 smart tier 로 — anthropic 도 이제 smart=top=Opus 5 이고 openai/google 도
        // smart=top 이라 사실상 top 과 동일. 출력 상한 초과 시 아래 가드가 섹션 draft 로 폴백.
        await assembleReport(query, drafts, lang, backend, apiKey, resolveModel(backend, 'smart') || topModel);
      } catch (e) {
        if (deepIsAbort(e)) throw e;  // user 중단 → bubble to outer handler
        if (isAuthError(e)) throw e;  // bad key → outer re-prompt/retry
        console.warn('[deeper] assembler failed — falling back to drafts:', e && e.message || e);
        DEEP.currentAnswer = '';
      }
      // Guard: the assembler is a 2nd LLM pass. If it dropped all [ref:N] or
      // introduced markers the section agents never cited (renumber / hallucination),
      // fall back to the concatenated section drafts whose [ref:N] are correct —
      // a wrong-paper citation is worse than losing the assembler's polish.
      const draftNums = new Set();
      for (const d of drafts) { collectCitedNums(d.text || '').forEach(function(n) { draftNums.add(n); }); }
      const ansNums = collectCitedNums(DEEP.currentAnswer || '');
      let invented = false;
      ansNums.forEach(function(n) { if (!draftNums.has(n)) invented = true; });
      const draftsText = drafts.map(function(d) { return '## ' + d.title + '\\n\\n' + (d.text || ''); }).join('\\n\\n');
      // 취합기가 max_tokens 상한에 걸려 잘렸거나(길이·인용 保存율이 초안의 60% 미만) 번호를
      // 지어낸 경우 → 완전한 단락 초안으로 폴백해 내용·레퍼런스 손실을 막는다.
      const citeLoss = draftNums.size >= 8 && ansNums.size < draftNums.size * 0.6;
      const lenLoss = draftsText.length > 4000 && DEEP.currentAnswer.length < draftsText.length * 0.6;
      if (draftNums.size && (ansNums.size === 0 || invented || citeLoss || lenLoss)) {
        console.warn('[deeper] assembler diverged/truncated — using full section drafts (cites ' + ansNums.size + '/' + draftNums.size + ', len ' + DEEP.currentAnswer.length + '/' + draftsText.length + ')');
        DEEP.currentAnswer = draftsText;
        renderDeepAnswer(DEEP.currentAnswer);
      }
      finalizeDeepAnswer();
      return true;
    }

    async function runDeepResearch(query) {
      query = (query || '').trim();
      if (!query) return;
      DEEP.currentQuery = query;
      deepShowPanel();
      // Visible heartbeat — proves the function was actually called.
      // Without this, a silent fallthrough on missing keys / prompt
      // cancel can look identical to "nothing happened".
      deepSetStatus('⏳ Deep Research 시작...');
      // 질의 임베딩은 이제 같은 출처 /api/embed 프록시가 처리하므로 별도
      // OpenAI 임베딩 키를 더 받지 않는다. 답변 생성/재정렬용 LLM 키 하나면 된다.
      if (!_LLM_KEY) {
        const lk = prompt('답변 생성용 API Key를 입력하세요 (Anthropic sk-ant-… / OpenAI sk-… / Google AIza… 중 하나):');
        if (!lk) { deepSetStatus('API Key가 필요합니다.', true); return; }
        const _b = detectBackend(lk);
        if (!_b) { deepSetStatus('알 수 없는 키 형식입니다 (Anthropic은 sk-ant-, OpenAI는 sk-, Google은 AIza 로 시작).', true); return; }
        _LLM_KEY = lk;
        localStorage.setItem('_LLM_KEY', lk);
        if (_b === 'anthropic') {
          _ANTHROPIC_KEY = lk;
          localStorage.setItem('_ANTHROPIC_KEY', lk);
        } else if (_b === 'google') {
          // Same key works for Audio Overview (Gemini). Seed _GEMINI_KEY
          // so the audio modal doesn't re-prompt for the same key.
          window._GEMINI_KEY = lk;
          try { localStorage.setItem('_GEMINI_KEY', lk); } catch (e) {}
        }
        deepSetStatus('✓ ' + _b + ' 키 감지됨');
        updateDeepModelLabels();
      }
      clearEl(document.getElementById('deep-answer'));
      document.getElementById('deep-refs').style.display = 'none';
      document.getElementById('deep-figures').style.display = 'none';
      const _dp = document.getElementById('deep-plan');
      if (_dp) { _dp.style.display = 'none'; _dp.classList.remove('active'); clearEl(document.getElementById('deep-plan-list')); const _sw = document.getElementById('deep-sec-wrap'); if (_sw) _sw.remove(); const _aw = document.getElementById('deep-asp-wrap'); if (_aw) _aw.remove(); }
      DEEP.currentAnswer = '';
      DEEP.currentRefs = [];
      // 이 실행이 웹 검색 토글 ON 으로 시작됐는지 캡처 — finalize 의
      // absorbWebCitations 게이트. 스트리밍 중 토글을 바꿔도 영향 없다.
      DEEP.webUsed = deepWebSearchOn();
      deepUpdateButtons(false);
      deepBeginRun();
      try {
        const index = await deepLoadIndex();
        deepThrowIfAborted();
        const _deeperEl = document.getElementById('deep-deeper');
        if (_deeperEl && _deeperEl.checked) {
          const ok = await runDeeperResearch(index, query);
          DEEP._authRetry = 0;
          if (ok) { deepSetStatus('✅ 완료'); setTimeout(() => deepSetStatus(''), 2500); }
          return;
        }
        deepSetStatus('\U0001F50D 질의 임베딩 중... (' + (index.model || 'embedding') + ')');
        const queryVec = await embedQuery(query);
        // 차원 상수는 인덱스 헤더(index.dim)를 따른다 — 질의 임베딩 차원이
        // 인덱스와 다르면(예: 인덱스 미재빌드) 코사인 유사도가 무의미해지므로 차단.
        if (index.dim && queryVec.length !== index.dim) {
          throw new Error('임베딩 차원(' + queryVec.length + ')이 검색 인덱스 차원(' + index.dim + ')과 다릅니다 — 인덱스를 재빌드하세요 (build_search_index).');
        }
        deepSetStatus('\U0001F4DA 관련 논문 검색 중... (BM25 + dense)');
        const timeFilter = parseTimeFilter(query);
        const journalFilter = parseJournalFilter(query, index);
        const chronological = isChronological(query);
        // 저자 인지 검색: 질의가 코퍼스 저자를 가리키면 메타로 직접 후보 구성
        // (저자명은 임베딩/BM25에 없어 일반 검색으로는 매칭 불가).
        const authorHit = matchCorpusAuthor(query, index);
        let candidates, selected;
        if (authorHit) {
          deepSetStatus('\U0001F464 저자 "' + authorHit.label + '" 논문 ' + authorHit.slugs.length + '편' + (chronological ? ' · 시간순' : '') + ' 정리 중...');
          candidates = authorCandidates(index, authorHit, queryVec, timeFilter, chronological, journalFilter);
          if (candidates.length === 0) {
            deepSetStatus('"' + authorHit.label + '" 저자의 논문을 (기간 조건에서) 찾지 못했어요.', true);
            return;
          }
          selected = candidates;  // 이미 논문당 대표 chunk·정렬 완료 → 재정렬 생략(순서 보존)
        } else if (looksLikeAuthorQuery(query)) {
          // 이름+의도는 있으나 이 토픽 코퍼스에 해당 저자가 없음 → 명확히 안내
          // (예: ai4s 에서 Dashun Wang → scisci 토픽에 존재).
          deepSetStatus('이 토픽에는 해당 저자의 논문이 없는 것 같아요. 다른 토픽(예: scisci)에서 시도해보세요.', true);
          return;
        } else {
          // Hybrid: BM25 + dense → RRF 후보 → LLM 재정렬. Long 은 근거를 2배(top-16)로
          // 늘려 Medium 과 실제 분량·깊이 차이가 나게 한다 (근거가 같으면 답도 수렴).
          const _len = document.getElementById('deep-length').value || 'short';
          const _topK = (_len === 'long') ? 16 : 8;
          const _topN = (_len === 'long') ? 40 : 20;
          candidates = hybridRetrieve(index, queryVec, query, timeFilter, journalFilter, _topN);
          if (candidates.length === 0) {
            deepSetStatus('관련 논문을 찾지 못했어요. 질의를 다시 입력해보세요.', true);
            return;
          }
          deepSetStatus('\U0001F9ED 상위 후보 재정렬 중...');
          selected = await rerankCandidates(query, candidates, _topK);
        }
        // Group chunks by paper so each paper appears as a single reference
        // entry. The retrieval step still uses chunk-level cosine similarity
        // (so different sections can independently boost a paper into the
        // top-k), but downstream prompt construction and references list
        // operate on unique papers -- otherwise the same paper shows up as
        // [1], [2], [3] when its Essence/How/Achievement chunks all match.
        const byPaper = new Map();
        for (const s of selected) {
          const slug = s.chunk.slug;
          if (!byPaper.has(slug)) {
            byPaper.set(slug, { slug: slug, paper: s.paper, chunks: [] });
          }
          byPaper.get(slug).chunks.push({ section: s.chunk.section, text: s.chunk.text });
        }
        const dedupedSelected = Array.from(byPaper.values());

        DEEP.currentRefs = dedupedSelected.map((s, i) => ({
          n: i + 1,
          slug: s.slug,
          title: s.paper.title,
          year: s.paper.year,
          url: s.paper.url,
          external_url: s.paper.external_url || '',
          authors: s.paper.authors || [],
          first_author: s.paper.first_author || '',
          doi: s.paper.doi || '',
          arxiv: s.paper.arxiv || '',
          figures: s.paper.figures || [],
        }));
        // Local-only deep dive: try to fetch text.md (raw paper text) for the
        // top distinct papers so Claude can quote concrete quantitative
        // details (reagents, amounts, conditions). text.md is git-ignored,
        // so on Cloudflare these fetches return 404 and we silently fall
        // back to review-only context. On localhost / file:// they succeed
        // and the LLM gets richer source material.
        deepSetStatus('\U0001F4C4 원문 발췌 가져오는 중...');
        const fullTexts = {};
        // 전면 적용: 상위 10편 제한을 없애고 '선택된 모든 참고 논문'의 text.md 를
        // 근거로 쓴다. 다만 컨텍스트 폭주를 막기 위해 전체 char 예산을 편수로 나눠
        // per-paper 상한을 동적으로 정한다(토큰 안전선). 공개 사이트는 text.md 가
        // 없어 404 → review-only 로 그대로 폴백(저작권).
        const FT_TOTAL_BUDGET = 360000;   // 원문 발췌 총 char 예산(≈토큰 안전선)
        const FT_PER_CAP = 30000;         // 편당 상한(기존 값)
        const FT_PER_MIN = 6000;          // 편당 하한(너무 잘리면 근거 가치 하락)
        const ftSlugs = dedupedSelected.map(function(s) { return s.slug; });
        const ftPerCap = Math.max(FT_PER_MIN,
          Math.min(FT_PER_CAP, Math.floor(FT_TOTAL_BUDGET / Math.max(1, ftSlugs.length))));
        await Promise.all(ftSlugs.map(async function(slug) {
          try {
            const r = await fetch('../papers/' + slug + '/text.md');
            if (!r.ok) return;
            const t = await r.text();
            fullTexts[slug] = t.slice(0, ftPerCap);
          } catch (e) { /* fetch error or missing file -- skip silently */ }
        }));
        deepThrowIfAborted();
        const lang = detectLang(query);
        const tier = document.getElementById('deep-model').value || 'fast';
        const length = document.getElementById('deep-length').value || 'short';
        await callLLM(query, dedupedSelected, lang, tier, length, fullTexts);
        finalizeDeepAnswer();
        DEEP._authRetry = 0;
        deepSetStatus('\u2705 완료');
        setTimeout(() => deepSetStatus(''), 2500);
      } catch (e) {
        // User pressed 중단 — not an error. Keep whatever streamed so far so
        // a partial-but-useful answer stays usable (copy/download enabled).
        if (deepIsAbort(e)) {
          if (DEEP.currentAnswer && DEEP.currentAnswer.trim()) {
            finalizeDeepAnswer();
            deepSetStatus('⏹️ 중단됨 — 여기까지 생성된 내용입니다.');
          } else {
            deepSetStatus('⏹️ 중단되었습니다.');
          }
          DEEP._authRetry = 0;
          return;
        }
        console.error(e);
        // /api/embed 프록시 미가동(503/404/네트워크) — 키 문제가 아니므로
        // 친절한 한글 안내로 분기한다. (Cloudflare 미배포 / 로컬 직접 열람 등)
        if (e && e.message && e.message.indexOf('embed-proxy-unreachable') === 0) {
          deepSetStatus('검색 서버(/api/embed)에 연결할 수 없습니다 — 로컬에서는 serve_local 런처로 여세요.', true);
          return;
        }
        // Auth failure path: clear the offending key, re-prompt with
        // "API Key Invalid. Try with another one", retry. Cap at 3
        // attempts so a user mashing Enter on a bad key doesn't
        // recurse forever.
        if (isAuthError(e)) {
          const scope = authErrorScope(e);
          DEEP._authRetry = (DEEP._authRetry || 0) + 1;
          if (DEEP._authRetry <= 3) {
            const nk = clearKeyAndRePrompt(scope);
            if (nk) {
              await runDeepResearch(query);
              return;
            }
          }
          deepSetStatus('API Key Invalid. Try with another one.', true);
          DEEP._authRetry = 0;
          return;
        }
        deepSetStatus('오류: ' + e.message, true);
      } finally {
        deepEndRun();
      }
    }

    function setSearchMode(mode) {
      window._searchMode = mode;
      const cb = document.getElementById('mode-classic');
      const db = document.getElementById('mode-deep');
      const input = document.getElementById('search-input');
      const hint = document.getElementById('search-hint');
      if (cb) cb.classList.toggle('active', mode === 'classic');
      if (db) db.classList.toggle('active', mode === 'deep');
      if (mode === 'deep') {
        if (input) input.placeholder = 'Deep Research: 자유롭게 질의하세요 (예: 2023년 이후 LLM agent 동향)';
        if (hint) hint.textContent = '분량·모델을 고른 뒤 Enter — Deeper 체크 시 연결 그래프 기반 멀티에이전트 리포트.';
        deepShowControls();
      } else {
        if (input) input.placeholder = 'Search papers by title, DOI, keyword...';
        if (hint) hint.textContent = 'Enter title, DOI, author name, or keyword to filter';
        deepHidePanel();
      }
    }


    function naturalizeCitationsMd(answerMd, refs) {
      // Markdown form: render [ref:N] as "[\\[N\\]](external_url)"
      // (square brackets escaped). Same reasoning as the HTML version:
      // body text stays the model's natural prose; the bracketed
      // number is just the clickable pointer.
      return answerMd.replace(/\\[ref:(\\d+)\\]/g, (_, n) => {
        const idx = parseInt(n) - 1;
        const ref = refs[idx];
        if (!ref) return '';
        const href = ref.external_url || '';
        return href ? '[\\\\[' + n + '\\\\]](' + href + ')' : '\\\\[' + n + '\\\\]';
      });
    }

    function buildFullMarkdown() {
      const q = document.getElementById('search-input').value;
      const naturalised = naturalizeCitationsMd(DEEP.currentAnswer, DEEP.currentRefs);
      const lines = ['# Deep Research', '', '**Query**: ' + q, '**Generated**: ' + new Date().toISOString(), '', '---', '', naturalised];
      const cited = collectCitedNums(DEEP.currentAnswer);
      if (cited.size > 0) {
        lines.push('', '## References', '');
        for (const n of [...cited].sort((a, b) => a - b)) {
          const ref = DEEP.currentRefs[n - 1];
          if (!ref) continue;
          const href = ref.external_url || ref.url;
          const authorBits = ref.first_author
            ? ref.first_author.split(/\\s+/).slice(-1)[0] + ' et al. '
            : '';
          const yearBits = ref.year ? '(' + ref.year + '). ' : '';
          const idBits = ref.doi
            ? ' DOI: https://doi.org/' + ref.doi
            : (ref.arxiv ? ' arXiv:' + ref.arxiv : '');
          lines.push('- ' + authorBits + yearBits + '[' + ref.title + '](' + href + ').' + idBits);
        }
      }
      return lines.join('\\n');
    }

    function copyAnswerMd() {
      if (!DEEP.currentAnswer) return;
      const full = buildFullMarkdown();
      navigator.clipboard.writeText(full).then(() => {
        const btn = document.getElementById('deep-copy');
        const orig = btn.textContent;
        btn.textContent = '\u2713 Copied';
        setTimeout(() => { btn.textContent = orig; }, 1500);
      });
    }

    function saveToObsidian() {
      if (!DEEP.currentAnswer) return;
      var query = document.getElementById('search-input').value || 'research-note';
      var topic = window.location.pathname.split('/').filter(Boolean).pop() || 'notes';
      var ts = new Date().toISOString().slice(0, 10);
      var slug = query.slice(0, 40).replace(/[^a-zA-Z0-9\\u1100-\\u11FF\\u3130-\\u318F\\uAC00-\\uD7AF]/g, '-').replace(/-+/g, '-').replace(/^-|-$/g, '');
      var fileName = 'notes/' + topic + '/PCDR_' + ts + '-' + slug;
      var lines = [
        '# ' + query, '',
        '> Deep Research (' + new Date().toLocaleString() + ')', '',
        '## My Notes', '', '(\\uC5EC\\uAE30\\uC5D0 \\uC0DD\\uAC01\\uC744 \\uC801\\uC73C\\uC138\\uC694)', '',
        '---', '',
        '## Deep Research Answer', '',
        DEEP.currentAnswer,
      ];
      var cited = collectCitedNums(DEEP.currentAnswer);
      if (cited.size > 0) {
        lines.push('', '## References', '');
        var ordered = Array.from(cited).sort(function(a, b) { return a - b; });
        for (var i = 0; i < ordered.length; i++) {
          var n = ordered[i];
          var ref = DEEP.currentRefs[n - 1];
          if (!ref) continue;
          // 웹 pseudo-ref 는 로컬 review 노트가 없으므로 일반 링크로.
          if (ref.web) { lines.push('[' + n + '] [' + ref.title + '](' + ref.url + ')'); continue; }
          lines.push('[' + n + '] [[papers/' + ref.slug + '/review|' + ref.title + ']]' + (ref.year ? ' (' + ref.year + ')' : ''));
        }
      }
      var content = lines.join('\\n');
      // Fix relative paths: LLM answers use ../papers/ which is correct
      // from docs/{topic}/, but notes live one level deeper in
      // docs/notes/{topic}/ so we need ../../papers/ instead.
      content = content.replace(/\\.\\.\\//g, '../../');
      var vault = 'docs';
      var uri = 'obsidian://new?vault=' + encodeURIComponent(vault) + '&file=' + encodeURIComponent(fileName) + '&content=' + encodeURIComponent(content);
      window.location.href = uri;
    }

    function downloadAnswerMd() {
      if (!DEEP.currentAnswer) return;
      const full = buildFullMarkdown();
      const blob = new Blob([full], { type: 'text/markdown;charset=utf-8' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      const ts = new Date().toISOString().replace(/[:.]/g, '-').slice(0, 19);
      a.href = url;
      a.download = 'deep-research-' + ts + '.md';
      document.body.appendChild(a);
      a.click();
      setTimeout(() => { document.body.removeChild(a); URL.revokeObjectURL(url); }, 100);
    }

    async function fetchImageAsDataUri(url) {
      // Convert a relative or absolute image URL into a self-contained
      // data: URI so the exported HTML renders on any machine. Returns
      // the original URL on failure (the export remains a degraded
      // image but the rest of the document survives).
      try {
        const resp = await fetch(url);
        if (!resp.ok) return url;
        const blob = await resp.blob();
        return await new Promise((resolve, reject) => {
          const reader = new FileReader();
          reader.onloadend = () => resolve(reader.result);
          reader.onerror = reject;
          reader.readAsDataURL(blob);
        });
      } catch (e) {
        return url;
      }
    }

    async function inlineImages(markup) {
      // Walk every <img src> in the markup and replace the src with a
      // base64 data URI. The download path is synchronous; this helper
      // pre-resolves everything so the resulting string is plain text
      // ready to write to a Blob.
      const srcRe = /<img\\s+[^>]*src="([^"]+)"/g;
      const seen = new Map();
      const matches = [...markup.matchAll(srcRe)];
      for (const m of matches) {
        const src = m[1];
        if (seen.has(src)) continue;
        if (src.startsWith('data:')) { seen.set(src, src); continue; }
        const dataUri = await fetchImageAsDataUri(src);
        seen.set(src, dataUri);
      }
      return markup.replace(srcRe, (full, src) => full.replace(src, seen.get(src) || src));
    }

    // Wrap each <h2> section of the exported report in a collapsible <details>
    // card so long Deeper-Research reports can be folded section-by-section.
    function sectionizeHtml(markup) {
      const parts = String(markup).split(/(<h2[^>]*>[\\s\\S]*?<\\/h2>)/);
      let out = (parts[0] || '').trim();
      if (out) out = '<div class="intro">' + out + '</div>';
      for (let i = 1; i < parts.length; i += 2) {
        const title = (parts[i] || '').replace(/<\\/?h2[^>]*>/g, '');
        const body = parts[i + 1] || '';
        out += '<details class="sec" open><summary>' + title + '</summary><div class="sec-body">' + body + '</div></details>';
      }
      return out;
    }

    // Resolve a working link for a reference so EVERY entry is clickable even
    // without a DOI: valid DOI -> doi.org; an arXiv id (incl. one mislabeled
    // into the doi field, e.g. "arXiv:2310.03302") -> arxiv.org; a real
    // external URL -> as-is; otherwise a title search. Placeholder DOIs
    // ("미제공" / "N/A" / "-") are treated as no-DOI, never linked verbatim.
    function refLink(ref) {
      const rawDoi = (ref.doi || '').trim();
      let arxiv = (ref.arxiv || '').trim();
      if (!arxiv && /ar[xX]iv/.test(rawDoi)) {
        const ax = rawDoi.match(/(\\d{4}\\.\\d{4,5})/);
        if (ax) arxiv = ax[1];
      }
      const validDoi = /^10\\.\\d{3,}\\/\\S+$/.test(rawDoi) ? rawDoi : '';
      const ext = (ref.external_url || '').trim();
      const extOk = /^https?:\\/\\//.test(ext) && !/doi\\.org\\/(?!10\\.)/.test(ext);
      if (validDoi) return { url: 'https://doi.org/' + encodeURIComponent(validDoi), tag: 'DOI: ' + validDoi };
      if (arxiv) return { url: 'https://arxiv.org/abs/' + encodeURIComponent(arxiv), tag: 'arXiv:' + arxiv };
      if (extOk) return { url: ext, tag: 'URL' };
      return { url: 'https://scholar.google.com/scholar?q=' + encodeURIComponent(ref.title || ''), tag: '검색' };
    }

    async function buildFullHtml() {
      const q = document.getElementById('search-input').value;
      let answerMarkup = mdToMarkup(DEEP.currentAnswer);
      // Use naturalised citations for export so the prose reads as
      // "Smith et al. (2024)" rather than numeric [1] [2] chips. Each
      // citation links to the paper's external URL (DOI / arXiv) so
      // the export resolves anywhere.
      answerMarkup = naturalizeCitations(answerMarkup, DEEP.currentRefs);

      const cited = collectCitedNums(DEEP.currentAnswer);
      let refsMarkup = '';
      if (cited.size > 0) {
        refsMarkup = '<h3>참고문헌</h3><ol>';
        for (const n of [...cited].sort((a, b) => a - b)) {
          const ref = DEEP.currentRefs[n - 1];
          if (!ref) continue;
          const link = refLink(ref);
          const titleHtml = '<a href="' + link.url + '" target="_blank" rel="noopener">' + escapeAttr(ref.title) + '</a>';
          const authorBits = ref.first_author
            ? escapeAttr(ref.first_author.split(/\\s+/).slice(-1)[0]) + ' et al. '
            : '';
          const yearBits = ref.year ? '(' + ref.year + '). ' : '';
          const idBits = ' <a href="' + link.url + '" target="_blank" rel="noopener" style="color:#6b7280">' + escapeAttr(link.tag) + '</a>';
          refsMarkup += '<li>' + authorBits + yearBits + titleHtml + '.' + idBits + '</li>';
        }
        refsMarkup += '</ol>';
      }

      // Strip out leftover local relative paths so nothing remains that
      // would only resolve on the original host. Images are converted
      // to base64 below; here we just remove dangling href targets that
      // point at the on-site review (the cite anchor already points at
      // the external URL).
      answerMarkup = answerMarkup.replace(/\\shref="\\.\\.\\/papers\\/[^"]+"/g, '');

      // Inline every figure as a data: URI so the file is fully
      // self-contained.
      answerMarkup = await inlineImages(answerMarkup);
      // Fold each section into a collapsible card for long reports.
      answerMarkup = sectionizeHtml(answerMarkup);

      return '<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Deeper Research</title><style>' +
        '*{box-sizing:border-box;}' +
        'body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans KR",sans-serif;background:#eef1f6;color:#1f2937;line-height:1.78;margin:0;padding:2.2rem 1rem;}' +
        '.wrap{max-width:840px;margin:0 auto;background:#fff;border-radius:16px;box-shadow:0 4px 24px rgba(15,23,42,0.08);overflow:hidden;}' +
        '.hd{background:linear-gradient(135deg,#2563EB,#1e3a8a);color:#fff;padding:1.7rem 2rem;}' +
        '.hd h1{margin:0 0 0.4rem;font-size:1.4rem;font-weight:700;}' +
        '.hd .meta{font-size:0.82rem;opacity:0.92;line-height:1.6;}' +
        '.body{padding:1.4rem 1.9rem 2rem;}' +
        '.intro{font-size:0.97rem;color:#374151;margin-bottom:0.6rem;}' +
        '.intro p{margin:0.8rem 0;}' +
        'details.sec{margin:0.85rem 0;border:1px solid #e5e7eb;border-radius:12px;overflow:hidden;background:#fff;}' +
        'details.sec[open]{box-shadow:0 2px 12px rgba(15,23,42,0.05);}' +
        'details.sec>summary{cursor:pointer;list-style:none;padding:0.9rem 1.2rem;font-weight:700;font-size:1.03rem;color:#1e3a8a;background:#eff3ff;display:flex;align-items:center;gap:0.55rem;user-select:none;}' +
        'details.sec>summary::-webkit-details-marker{display:none;}' +
        'details.sec>summary::before{content:"▸";color:#6366f1;font-size:0.85em;transition:transform 0.15s;}' +
        'details.sec[open]>summary::before{transform:rotate(90deg);}' +
        'details.sec>summary:hover{background:#e0e7ff;}' +
        '.sec-body{padding:0.5rem 1.4rem 1.2rem;font-size:0.96rem;}' +
        '.sec-body p{margin:0.85rem 0;}' +
        '.sec-body h3{color:#374151;margin:1.1rem 0 0.4rem;font-size:1rem;}' +
        'sup{line-height:0;font-size:0.7em;}' +
        'sup a.cite{color:#2563EB;text-decoration:none;font-weight:600;padding:0 0.15em;border-radius:2px;}' +
        'sup a.cite:hover{background:#EBF2FF;}' +
        'sup.cite-local{color:#9ca3af;}' +
        'figure{margin:1rem 0;max-width:100%;}' +
        'img{max-width:100%;height:auto;display:block;margin:0.8rem 0;padding:0.5rem;background:#f8fafc;border:1px solid #e5e7eb;border-radius:8px;}' +
        'figure img{margin:0;padding:0.4rem;}' +
        'figure figcaption{font-size:0.78rem;color:#6b7280;text-align:center;margin-top:0.4rem;font-style:italic;}' +
        '.refs{margin:0 1.9rem 2rem;padding:1.2rem 1.5rem;background:#f8fafc;border:1px solid #eef0f3;border-radius:12px;}' +
        '.refs h3{margin:0 0 0.7rem;color:#1e3a8a;font-size:1rem;}' +
        '.refs ol{font-size:0.85rem;color:#4b5563;margin:0 0 0 1.1rem;padding:0;}' +
        '.refs li{margin:0.35rem 0;line-height:1.6;}' +
        '.refs a{color:#2563EB;text-decoration:none;}' +
        '.refs a:hover{text-decoration:underline;}' +
        '@media print{body{background:#fff;padding:0;}.wrap{box-shadow:none;}details.sec{break-inside:avoid;}}' +
        '@media(max-width:600px){.hd,.body{padding-left:1.1rem;padding-right:1.1rem;}.refs{margin-left:1.1rem;margin-right:1.1rem;}}' +
        '</style></head><body>' +
        '<div class="wrap">' +
        '<div class="hd"><h1>\U0001F578️ Deeper Research</h1><div class="meta"><strong>질문:</strong> ' + escapeAttr(q) + '<br><strong>생성:</strong> ' + new Date().toLocaleString() + '</div></div>' +
        '<div class="body">' + answerMarkup + '</div>' +
        (refsMarkup ? ('<div class="refs">' + refsMarkup + '</div>') : '') +
        '</div></body></html>';
    }

    async function openAnswerInNewTab() {
      if (!DEEP.currentAnswer) return;
      const doc = await buildFullHtml();
      const blob = new Blob([doc], { type: 'text/html;charset=utf-8' });
      const url = URL.createObjectURL(blob);
      window.open(url, '_blank');
      setTimeout(() => URL.revokeObjectURL(url), 60000);
    }

    async function downloadAnswerHtml() {
      if (!DEEP.currentAnswer) return;
      const doc = await buildFullHtml();
      const blob = new Blob([doc], { type: 'text/html;charset=utf-8' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      const ts = new Date().toISOString().replace(/[:.]/g, '-').slice(0, 19);
      a.href = url;
      a.download = 'deep-research-' + ts + '.html';
      document.body.appendChild(a);
      a.click();
      setTimeout(() => { document.body.removeChild(a); URL.revokeObjectURL(url); }, 100);
    }

    document.addEventListener('DOMContentLoaded', function() {
      window._searchMode = window._PC_CROSS ? 'deep' : 'classic';

      // Refresh Fast/Smart dropdown labels based on any cached API key
      // so the user sees concrete model names from page load.
      updateDeepModelLabels();

      // Same pattern for Zotero itemKey lookup. When present (local dev),
      // the Deep Research References list adds a one-click 'Open PDF'
      // button next to each citation. Git-ignored, so Cloudflare visitors
      // get a 404 here and the button never appears for them.
      fetch('../_zotero_keys.json').then(function(r) {
        return r.ok ? r.json() : null;
      }).then(function(keys) {
        if (keys) window._zoteroKeys = keys;
      }).catch(function() { /* no zotero keys; fine */ });

      const cb = document.getElementById('mode-classic');
      const db = document.getElementById('mode-deep');
      if (cb) cb.addEventListener('click', () => setSearchMode('classic'));
      if (db) db.addEventListener('click', () => setSearchMode('deep'));
      if (window._PC_CROSS) setSearchMode('deep');
      const input = document.getElementById('search-input');
      if (input) {
        input.addEventListener('keydown', function(e) {
          if (e.key === 'Enter' && window._searchMode === 'deep') {
            e.preventDefault();
            runDeepResearch(this.value);
          }
        });
      }
      const close = document.getElementById('deep-close');
      if (close) close.addEventListener('click', function() { deepRequestStop(); deepHidePanel(); });
      const stop = document.getElementById('deep-stop');
      if (stop) stop.addEventListener('click', deepRequestStop);
      const copy = document.getElementById('deep-copy');
      if (copy) copy.addEventListener('click', copyAnswerMd);
      const dl = document.getElementById('deep-download');
      if (dl) dl.addEventListener('click', downloadAnswerMd);
      const dlh = document.getElementById('deep-download-html');
      if (dlh) dlh.addEventListener('click', downloadAnswerHtml);
      const nt = document.getElementById('deep-newtab');
      if (nt) nt.addEventListener('click', openAnswerInNewTab);
      const ob = document.getElementById('deep-obsidian');
      if (ob) ob.addEventListener('click', saveToObsidian);
      const rerun = document.getElementById('deep-rerun');
      if (rerun) rerun.addEventListener('click', function() {
        const q = document.getElementById('search-input').value;
        if (q && q.trim()) runDeepResearch(q);
      });
      // Deeper checkbox: forces Long length + top-tier model and disables the
      // length/model dropdowns (the multi-agent report ignores them anyway).
      const deeperCb = document.getElementById('deep-deeper');
      if (deeperCb) {
        const applyDeeper = function() {
          const on = deeperCb.checked;
          const lenSel = document.getElementById('deep-length');
          const modSel = document.getElementById('deep-model');
          if (lenSel) { if (on) lenSel.value = 'long'; lenSel.disabled = on; }
          if (modSel) modSel.disabled = on;
          const note = document.getElementById('deep-deeper-note');
          if (note) {
            if (on) {
              const key = _LLM_KEY || _ANTHROPIC_KEY || _OPENAI_KEY || (window._GEMINI_KEY || '');
              const lbl = (MODEL_LABEL[detectBackend(key)] || {}).top || '최상위 모델';
              note.textContent = '→ Long · ' + lbl + ' · 단락별 에이전트';
            } else { note.textContent = ''; }
          }
        };
        deeperCb.addEventListener('change', applyDeeper);
        applyDeeper();
      }
    });"""

    # --- Build-time: inject API keys from env vars into JS ---
    _cfg_path = Path(__file__).resolve().parent.parent / "config.json"
    _cfg_keys = {}
    if _cfg_path.exists():
        with open(_cfg_path, "r", encoding="utf-8") as _f:
            _cfg_keys = json.load(_f)
    _ANTHROPIC_KEY = os.environ.get("ANTHROPIC_API_KEY") or _cfg_keys.get("anthropic_api_key", "")
    _OPENAI_KEY = os.environ.get("OPENAI_API_KEY") or _cfg_keys.get("openai_api_key", "")
    _GEMINI_KEY = (os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
                   or _cfg_keys.get("gemini_api_key", "") or _cfg_keys.get("google_api_key", ""))
    # Local-only Audio Overview recipients (baked for localhost convenience;
    # stripped by prepare_deploy.py before Cloudflare upload).
    _LOCAL_EMAILS_RAW = (os.environ.get("PAPER_CURATION_LOCAL_EMAILS", "")
                         or ",".join(_cfg_keys.get("local_emails", []) or []))
    _LOCAL_EMAILS = [e.strip() for e in _LOCAL_EMAILS_RAW.split(",") if e.strip()]
    # ── Deep Research multi-backend keys ──────────────────────────────
    # We baked these at build time for local dev (where prepare_deploy
    # strips them on the way to Cloudflare). At runtime the modal
    # accepts any one of the three; we sniff the prefix to pick the
    # backend (sk-ant-* → Anthropic, sk-* → OpenAI, AIza* → Google).
    # `_LLM_KEY` is the unified slot; `_ANTHROPIC_KEY` is kept for
    # backward-compat with any code still referencing it. The embedding
    # step (Deep Research RAG) continues to require an OpenAI key —
    # that's a separate slot.
    JS = ("let _ANTHROPIC_KEY = " + json.dumps(_ANTHROPIC_KEY) + " || localStorage.getItem('_ANTHROPIC_KEY') || '';\n"
          "let _OPENAI_KEY = " + json.dumps(_OPENAI_KEY) + " || localStorage.getItem('_OPENAI_KEY') || '';\n"
          "let _LLM_KEY = localStorage.getItem('_LLM_KEY') || _ANTHROPIC_KEY || '';\n" + ("window._PC_CROSS = " + ("true" if cross else "false") + ";\n") + JS)


    def render_insights_section():
        """_insights.json에서 cross-category insights 렌더링."""
        cross = insights_data.get("cross_category", [])
        if not cross:
            return ""

        # Build slug number → paper info lookup (topic-first; see _refs_to_links)
        num_to_paper = {}
        for p in papers_index:                       # global fallback
            slug = p.get("slug", "")
            title = p.get("title", "")
            num = slug.split("_")[0] if "_" in slug else slug[:3]
            num_to_paper[num] = (slug, title)
        for p in topic_papers:                        # topic-scoped overrides win
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

        # Collapsed by default — only the header shows; click to expand.
        return (
            '<div class="insights-section">\n'
            '  <h2 class="insights-header" onclick="toggleInsights()">'
            '<span class="topic-toggle" id="toggle-insights-body">&#x25B6;</span>'
            f' Research Insights <span class="insight-count">{len(cross)} findings</span></h2>\n'
            '  <div class="insights-body collapsed" id="insights-body">\n'
            + "\n".join(cards) + "\n"
            + '  </div>\n'
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
    if cross:
        _tlinks = "".join(
            f'<a class="cross-topic" href="../{esc(t["slug"])}/index.html">'
            f'{esc(t.get("title", t["slug"]))} <strong>{int(t.get("papers", 0))}</strong></a>'
            for t in cross.get("topics", [])
        )
        topic_groups_parts = [
            '<div class="cross-dir">'
            '<h2>🧠 통합 Deep Research — 모든 토픽을 하나의 코퍼스로</h2>'
            f'<p>{unique_papers}편의 리뷰를 토픽 경계 없이 검색합니다. 위 검색창에서 '
            '<strong>🧠 Deep</strong> 을 누르고 질문하세요 — 연결 그래프를 넘나드는 '
            '<strong>Deeper</strong> 확장도 지원합니다. <em>(로컬 전용)</em></p>'
            '<div class="cross-topics">' + _tlinks + '</div>'
            '</div>'
        ]

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
            research_tl_html += f'  <div style="text-align:right;margin-top:0.8rem"><a href="network.html" target="_blank" rel="noopener noreferrer" style="color:{accent};font-weight:600;text-decoration:none;font-size:0.9rem">&#x1F517; Interactive Paper Network &rarr;</a></div>\n'
        research_tl_html += '</div>\n\n\n'

    # Deep Research Audio Overview: context provider built live from the answer.
    _AUDIO_PROVIDER_JS = (
        "window._audioContextProvider = function() {\n"
        "  return {\n"
        "    title: (DEEP.currentQuery || 'deep-research'),\n"
        "    review: '[질문]\\n' + (DEEP.currentQuery || '') + '\\n\\n[답변]\\n' + (DEEP.currentAnswer || ''),\n"
        "    connections: (DEEP.currentRefs || []).map(function(r) { return {title: r.title, relation: '인용', reason: ''}; })\n"
        "  };\n"
        "};"
    )

    HTML = (
        '<!DOCTYPE html>\n'
        '<html lang="ko">\n'
        '<head>\n'
        '<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1.0">\n'
        f'<title>{esc(theme["title"])} &#8212; Paper Curation</title>\n'
        # OG 소셜 카드 — 토픽 링크 공유 시 타임라인 이미지가 카드로 뜬다
        # (research_timeline.png 는 배포 시 prepare_deploy 가 .webp 로 재작성).
        '<meta property="og:type" content="website">\n'
        '<meta property="og:site_name" content="Paper Curation">\n'
        f'<meta property="og:title" content="{esc(theme["title"])} — Paper Curation">\n'
        '<meta property="og:description" content="AI 논문 큐레이션 — 구조화 리뷰 · 연결 그래프 · 타임라인 · Deep Research">\n'
        f'<meta property="og:url" content="https://paper-curation.jehyunlee.dev/{topic}/">\n'
        f'<meta property="og:image" content="https://paper-curation.jehyunlee.dev/{topic}/research_timeline.png">\n'
        '<meta name="twitter:card" content="summary_large_image">\n'
        # Atom 피드 autodiscovery — RSS 리더가 feed.xml 을 자동 인식 (build_rss.py 생성)
        f'<link rel="alternate" type="application/atom+xml" title="{esc(theme["title"])} — Paper Curation" href="feed.xml">\n'
        '<link rel="stylesheet" href="https://cdn.jsdelivr.net/font-kopub/1.0/kopubdotum.css">\n'
        '<script>window.MathJax={tex:{inlineMath:[[\'$\',\'$\'],[\'\\\\(\',\'\\\\)\']],displayMath:[[\'$$\',\'$$\'],[\'\\\\[\',\'\\\\]\']]}};</script>\n'
        '<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>\n'
        '<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>\n'
        f'<style>\n{CSS}\n</style>\n'
        '</head>\n'
        '<body>\n'
        '<div class="container">\n'
        '  <div class="hero">\n'
        f'    <h1>{esc(theme["title"])} &#8212; Paper Curation</h1>\n'
        '    <div class="ai-notice" style="margin:0.7rem 0 0.3rem;padding:0.55rem 0.9rem;background:#fff8e1;border:1px solid #ffe0a3;border-radius:8px;font-size:0.82rem;color:#7a5b00;line-height:1.55;">'
        '&#9888;&#65039; 이 사이트의 리뷰&middot;요약&middot;타임라인&middot;Deep Research 답변은 <strong>생성형 AI</strong>가 자동 생성한 결과물입니다. '
        '게재 논문은 arXiv&middot;OpenReview 등 공개 프리프린트이며, 원문 저작권은 <strong>원저작자</strong>에게 있습니다.'
        '</div>\n'
        '    <div class="stats">\n'
        f'      <div class="stat"><div class="stat-num">{unique_papers}</div><div class="stat-label">\ub9ac\ubdf0 \uc644\ub8cc</div></div>\n'
        f'      <div class="stat"><div class="stat-num">{num_cats}</div><div class="stat-label">MECE \uce74\ud14c\uace0\ub9ac</div></div>\n'
        f'      <div class="stat"><div class="stat-num">{TODAY}</div><div class="stat-label">\ud050\ub808\uc774\uc158 \uc77c\uc790</div></div>\n'
        '    </div>\n'
        # Atom \ud53c\ub4dc \ub9c1\ud06c \u2014 hero(\ub2e4\ud06c \uadf8\ub77c\ub514\uc5b8\ud2b8) \uc704\ub77c \ud770\uc0c9+opacity \ub85c \uc774\uc9c8\uac10 \uc5c6\uac8c
        '    <div style="margin-top:1rem;text-align:right"><a href="feed.xml" title="Atom \ud53c\ub4dc \uad6c\ub3c5 (RSS)" style="color:white;opacity:0.75;text-decoration:none;font-size:0.85rem;font-weight:600">&#x1F4E1; RSS</a></div>\n'
        '  </div>\n\n\n'
        + research_tl_html
        + render_insights_section()
        + '  <div class="search-box">\n'
        '    <div class="search-row">\n'
        '      <input type="text" id="search-input" placeholder="Search papers by title, DOI, keyword...">\n'
        '      <div class="mode-toggle">\n'
        '        <button class="mode-btn active" id="mode-classic" title="Substring search">Classic</button>\n'
        '        <button class="mode-btn" id="mode-deep" title="Deep Research (uses your API keys)">&#x1F9E0; Deep</button>\n'
        '      </div>\n'
        '    </div>\n'
        '    <div class="search-hint" id="search-hint">Enter title, DOI, author name, or keyword to filter</div>\n'
        '    <div class="search-count" id="search-count"></div>\n'
        '    <div id="deep-panel" class="deep-panel" style="display:none">\n'
        '      <div class="deep-header">\n'
        '        <h3>Deep Research</h3>\n'
        '        <select id="deep-length" class="deep-model" title="답변 분량">\n'
        '          <option value="short" selected>Short</option>\n'
        '          <option value="medium">Medium (2x)</option>\n'
        '          <option value="long">Long (5x)</option>\n'
        '        </select>\n'
        '        <select id="deep-model" class="deep-model" title="모델 등급. 키에 따라 Anthropic Sonnet/Opus, OpenAI GPT-4.1/GPT-5.5, Google Gemini 3.1 Flash-Lite/3.5 Flash 로 자동 매핑">\n'
        '          <option value="fast">Fast (cheap)</option>\n'
        '          <option value="smart">Smart (best)</option>\n'
        '        </select>\n'
        '        <label class="deep-deeper-lbl" title="체크 시: 답변 생성에 웹 검색을 허용합니다 — 관련 뉴스·빅테크 블로그·코퍼스 밖 최신 논문 참조. Anthropic/Gemini 키에서 동작 (OpenAI 키는 미지원). 검색 호출 비용이 소액 추가됩니다. 기본 OFF = 코퍼스 발췌만 사용.">\n'
        '          <input type="checkbox" id="deep-websearch"> &#x1F310; web\n'
        '        </label>\n'
        '        <label class="deep-deeper-lbl" title="체크 시: 핵심 논문의 연결 그래프(후속·반론·기반·응용)를 따라 확장하고, 단락별 에이전트가 작성한 뒤 오케스트레이터가 취합합니다. 분량 Long·최상위 모델이 자동 적용 (LLM 호출·시간·비용 증가).">\n'
        '          <input type="checkbox" id="deep-deeper"> Deeper\n'
        '        </label>\n'
        '        <span class="deep-deeper-note" id="deep-deeper-note"></span>\n'
        '        <button class="deep-btn deep-stop-btn" id="deep-stop" style="display:none" title="생성 중인 답변을 즉시 중단">&#x23F9;&#xFE0F; 중단</button>\n'
        '        <button class="deep-btn" id="deep-rerun" disabled title="현재 질의를 선택한 모델·분량으로 다시 실행">&#x21BB; 재시작</button>\n'
        '        <div class="deep-actions">\n'
        '          <button class="deep-btn" id="deep-copy" disabled title="Copy markdown">&#x1F4CB; Copy</button>\n'
        '          <button class="deep-btn" id="deep-download" disabled title="Download .md">&#x2B07; MARKDOWN</button>\n'
        '          <button class="deep-btn" id="deep-download-html" disabled title="Download .html">&#x2B07; HTML</button>\n'
        '          <button class="deep-btn" id="deep-newtab" disabled title="Open in new tab">&#x1F517; New tab</button>\n'
        '          <button class="deep-btn" id="deep-obsidian" disabled title="Save answer + your notes to Obsidian">&#x1F4DD; Obsidian</button>\n'
        '          <button class="deep-btn" id="deep-audio" disabled title="이 답변을 팟캐스트형 오디오로 생성 (Gemini · 키는 브라우저에만 저장)" onclick="openAudioModal()">&#x1F3A7; Audio</button>\n'
        '          <button class="deep-btn" id="deep-close" title="Close">&#x2715;</button>\n'
        '        </div>\n'
        '      </div>\n'
        '      <div class="deep-status" id="deep-status"></div>\n'
        '      <div class="deep-plan" id="deep-plan" style="display:none">\n'
        '        <div class="deep-plan-title">&#x1F5FA;&#xFE0F; Research plan</div>\n'
        '        <ol class="deep-plan-list" id="deep-plan-list"></ol>\n'
        '      </div>\n'
        '      <div class="deep-body" id="deep-body">\n'
        '        <div class="deep-answer" id="deep-answer"></div>\n'
        '        <div class="deep-refs" id="deep-refs" style="display:none">\n'
        '          <h4>References</h4>\n'
        '          <ol id="deep-refs-list"></ol>\n'
        '        </div>\n'
        '        <div class="deep-figures" id="deep-figures" style="display:none">\n'
        '          <h4>Related Figures</h4>\n'
        '          <div class="deep-figures-grid" id="deep-figures-grid"></div>\n'
        '        </div>\n'
        '      </div>\n'
        '    </div>\n'
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
        + _audio_modal("이 Deep Research 답변을 팟캐스트형 오디오로 생성합니다. (Gemini · 키는 브라우저에만 저장 · 완성본은 이메일로도 전송)") + "\n"
        + _audio_script(_GEMINI_KEY, mode="deep", provider_js=_AUDIO_PROVIDER_JS,
                        local_emails=_LOCAL_EMAILS) + "\n"
        + '<footer style="text-align:center;padding:2rem 0 1rem;color:#999;font-size:0.85rem;border-top:1px solid #eee;margin-top:3rem;">'
        '게재 논문은 arXiv&middot;OpenReview 등 공개 프리프린트이며 저작권은 원저작자에게 귀속됩니다 &middot; 리뷰&middot;요약&middot;Deep Research 답변은 생성형 AI가 생성한 결과물입니다'
        '<br>Developed by Jehyun Lee, KIST AIX Strategy Department | jehyun.lee@gmail.com'
        '</footer>\n\n'
        '</body>\n</html>'
    )

    out_path = os.path.join(TOPIC_DIR, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(HTML)
    print(f"Written: {out_path} ({len(HTML):,} chars)")


    # Operator convenience: write docs/_zotero_keys.json (slug -> Zotero
    # itemKey). The Deep Research References list checks this on page load
    # and, if present, adds a one-click 'Open PDF' button next to each
    # reference. The button uses 'zotero://open-pdf/library/items/<KEY>'
    # which the Zotero desktop app handles directly. Git-ignored, so the
    # Cloudflare deployment never sees it.
    try:
        import urllib.request as _urllib_request
        import time as _time
        _api_key = get_zotero_api_key()
        _user_id = get_zotero_user_id()
        # The map is shared across all topics + git-ignored (localhost only).
        # Re-paginating the whole Zotero library on every topic build only risks
        # an API hang for no benefit, so reuse a recent (<24h) file. Force a
        # refresh by deleting docs/_zotero_keys.json; skip entirely with
        # SKIP_ZOTERO_KEYS=1.
        _zk_existing = Path(DOCS_DIR) / "_zotero_keys.json"
        _zm_existing = Path(DOCS_DIR) / "_zotero_meta.json"
        _zk_fresh = (_zk_existing.exists() and _zm_existing.exists()
                     and (_time.time() - _zk_existing.stat().st_mtime) < 86400)
        if os.environ.get("SKIP_ZOTERO_KEYS") or _zk_fresh:
            print(f"Zotero keys: reusing existing {_zk_existing} (fresh; skip re-fetch)")
        elif _api_key and _user_id:
            _items = []
            _start = 0
            _limit = 100
            while True:
                _url = f"https://api.zotero.org/users/{_user_id}/items/top?format=json&limit={_limit}&start={_start}"
                _req = _urllib_request.Request(_url, headers={
                    "Zotero-API-Key": _api_key,
                    "User-Agent": "Mozilla/5.0",
                })
                with _urllib_request.urlopen(_req, timeout=30) as _resp:
                    _batch = json.load(_resp)
                if not _batch:
                    break
                _items.extend(_batch)
                if len(_batch) < _limit:
                    break
                _start += _limit

            def _norm_title(t):
                return re.sub(r"\s+", " ", t.lower().strip()) if t else ""

            def _norm_arxiv(s):
                m = re.search(r"(\d{4}\.\d{4,5})", s or "")
                return m.group(1) if m else ""

            # Index Zotero items by title AND DOI AND arXiv-id. The 'Open PDF'
            # button must reflect "this paper has a PDF", not "its title happens
            # to match" — exact-title matching silently dropped papers whose
            # stored title differs (truncation, punctuation, version suffix) even
            # when a PDF exists. DOI/arXiv give a robust ID-first fallback.
            _title_to_key, _doi_to_key, _arxiv_to_key = {}, {}, {}
            _zmeta = {}  # normalized-title -> {url, doi} for build_search_index
            for _it in _items:
                _d2 = _it.get("data", {})
                _zt = re.sub(r"[^a-z0-9]", "", (_d2.get("title", "") or "").lower())
                if _zt:
                    _zmeta.setdefault(_zt, {"url": (_d2.get("url") or "").strip(),
                                            "doi": (_d2.get("DOI") or "").strip()})
                _k = _it.get("key", "")
                if not _k:
                    continue
                if _d2.get("title"):
                    _title_to_key.setdefault(_norm_title(_d2["title"]), _k)
                _doi = (_d2.get("DOI", "") or "").lower().strip()
                if _doi:
                    _doi_to_key.setdefault(_doi, _k)
                _ax = _norm_arxiv((_d2.get("url", "") or "") + " "
                                  + (_d2.get("extra", "") or "") + " "
                                  + (_d2.get("archiveID", "") or ""))
                if _ax:
                    _arxiv_to_key.setdefault(_ax, _k)

            # Fetch attachment items so we can map parent -> PDF attachment
            # key. zotero://open-pdf requires the *attachment* key, not the
            # parent item key, to open the PDF directly.
            print("  Fetching Zotero attachments for PDF key mapping...")
            _attach_items = []
            _start = 0
            while True:
                _url = f"https://api.zotero.org/users/{_user_id}/items?itemType=attachment&format=json&limit={_limit}&start={_start}"
                _req = _urllib_request.Request(_url, headers={
                    "Zotero-API-Key": _api_key,
                    "User-Agent": "Mozilla/5.0",
                })
                with _urllib_request.urlopen(_req, timeout=30) as _resp:
                    _batch = json.load(_resp)
                if not _batch:
                    break
                _attach_items.extend(_batch)
                if len(_batch) < _limit:
                    break
                _start += _limit

            # Build parent_key -> first PDF attachment_key map
            _parent_to_pdf = {}
            for _att in _attach_items:
                _d = _att.get("data", {})
                _parent = _d.get("parentItem", "")
                _ct = _d.get("contentType", "") or ""
                _att_key = _att.get("key", "")
                if _parent and _att_key and "pdf" in _ct.lower() and _parent not in _parent_to_pdf:
                    _parent_to_pdf[_parent] = _att_key
            print(f"  {len(_parent_to_pdf)} PDF attachments found")

            _slug_to_key = {}
            _papers_index = Path(_PAPERS_DIR) / "_papers_index.json"
            if _papers_index.exists():
                with open(_papers_index, "r", encoding="utf-8") as _pf:
                    for _p in json.load(_pf):
                        _s = _p.get("slug", "")
                        if not _s:
                            continue
                        # Resolve the Zotero parent item: title first (preserves
                        # all existing matches), then DOI, then arXiv-id — so a
                        # title mismatch no longer hides a paper that has a PDF.
                        _parent_key = _title_to_key.get(_norm_title(_p.get("title", "")))
                        if not _parent_key:
                            _doi = (_p.get("doi", "") or "").lower().strip()
                            _parent_key = _doi_to_key.get(_doi) if _doi else None
                        if not _parent_key:
                            _ax = _norm_arxiv((_p.get("arxiv_id", "") or "") + " "
                                              + (_p.get("url", "") or "") + " " + _s)
                            _parent_key = _arxiv_to_key.get(_ax) if _ax else None
                        if _parent_key:
                            # Use PDF attachment key if available, fall back
                            # to parent key (which at least selects the item)
                            _slug_to_key[_s] = _parent_to_pdf.get(_parent_key, _parent_key)
            if _slug_to_key:
                _zk_path = Path(DOCS_DIR) / "_zotero_keys.json"
                _zk_path.write_text(json.dumps(_slug_to_key), encoding="utf-8")
                print(f"Zotero keys: {_zk_path} ({len(_slug_to_key)} matched, for localhost dev, git-ignored)")
            # Title -> {url, doi} map so build_search_index can give non-DOI
            # papers a real external URL (Zotero `url`). Local-only, git-ignored.
            _zm_path = Path(DOCS_DIR) / "_zotero_meta.json"
            _zm_path.write_text(json.dumps(_zmeta, ensure_ascii=False), encoding="utf-8")
            print(f"Zotero meta: {_zm_path} ({len(_zmeta)} titles, url/doi enrichment, git-ignored)")
    except Exception as _e:
        print(f"Zotero keys skipped: {_e}")

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


if __name__ == "__main__":
    from _env_guard import force_py312
    force_py312()
    _run_topic_index()
