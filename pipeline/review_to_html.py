"""
Canonical review.md → index.html converter.
Enforces consistent layout across all review pages.

Usage:
  PYTHONUTF8=1 python review_to_html.py [--topic ai4s|scisci] [--slugs 251-258] [--all]
  PYTHONUTF8=1 python review_to_html.py --all              # regenerate all
  PYTHONUTF8=1 python review_to_html.py --slugs 251-394    # specific range
"""
import os, re, sys, json, argparse
from html import escape as esc
from urllib.parse import quote as _urlquote

from config_loader import PAPERS_DIR as _PAPERS_DIR
from lib.audio_overview import (
    get_audio_css as _audio_css_lib,
    audio_modal_html as _audio_modal_lib,
    audio_script_block as _audio_script_lib,
)
PAPERS = str(_PAPERS_DIR)

# Zotero PDF attachment keys (slug → key). Written by build_topic_index;
# absent on the very first build, harmless when missing — button just doesn't
# render for papers without a known key.
_ZOTERO_KEYS_PATH = os.path.join(os.path.dirname(_PAPERS_DIR), "_zotero_keys.json")
try:
    with open(_ZOTERO_KEYS_PATH, "r", encoding="utf-8") as _f:
        _ZOTERO_KEYS = json.load(_f)
except Exception:
    _ZOTERO_KEYS = {}

# Gemini key for the browser-direct Audio Overview feature. Baked into the
# review page at build time (like the Deep Research keys in build_topic_index),
# then stripped from every deployed page by prepare_deploy.py. On Cloudflare the
# value is "" so the generate button stays disabled (localhost-only feature).
_GEMINI_KEY = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY") or ""
_LOCAL_EMAILS_RAW = os.environ.get("PAPER_CURATION_LOCAL_EMAILS", "")
if not _GEMINI_KEY or not _LOCAL_EMAILS_RAW:
    _cfg_path = os.path.join(os.path.dirname(os.path.dirname(_PAPERS_DIR)), "config.json")
    try:
        with open(_cfg_path, "r", encoding="utf-8") as _f:
            _cfg = json.load(_f)
        if not _GEMINI_KEY:
            _GEMINI_KEY = _cfg.get("gemini_api_key") or _cfg.get("google_api_key", "")
        if not _LOCAL_EMAILS_RAW:
            _LOCAL_EMAILS_RAW = ",".join(_cfg.get("local_emails", []) or [])
    except Exception:
        pass
_LOCAL_EMAILS = [e.strip() for e in _LOCAL_EMAILS_RAW.split(",") if e.strip()]

THEMES = {
    "ai4s": {"accent": "#D63423", "accent_dark": "#A62018", "accent_bg": "#FEF0EF",
             "essence_border": "#8B1A1A", "essence_bg": "#FDF8F8",
             "link_color": "#A62018", "back_href": "../../ai4s/index.html"},
    "scisci": {"accent": "#2374D6", "accent_dark": "#1856A0", "accent_bg": "#EBF3FF",
               "essence_border": "#1856A0", "essence_bg": "#F8FAFD",
               "link_color": "#1856A0", "back_href": "../../scisci/index.html"},
}

# 배포 도메인 — OG 태그의 절대 URL 용 (= prepare_deploy.CF_BASE_URL).
_CF_BASE = "https://paper-curation.jehyunlee.dev"

# Paper connections cache (loaded once per run)
_connections_cache = {}

_BSI = None

from lib import license_util as _lic

_DEPLOY_TOPICS = None
def _deploy_topics():
    """Topic dirs actually published to Cloudflare (index.html, not in .assetsignore)."""
    global _DEPLOY_TOPICS
    if _DEPLOY_TOPICS is None:
        docs = os.path.dirname(PAPERS)
        ai = set()
        try:
            for raw in open(os.path.join(docs, ".assetsignore"), encoding="utf-8"):
                s = raw.strip().rstrip("/")
                if s and not s.startswith("#") and "/" not in s:
                    ai.add(s)
        except Exception:
            pass
        dep = set()
        try:
            for d in os.listdir(docs):
                if (os.path.isdir(os.path.join(docs, d))
                        and os.path.exists(os.path.join(docs, d, "index.html"))
                        and d not in ai and d not in {"papers", "notes", "public"}):
                    dep.add(d)
        except Exception:
            pass
        _DEPLOY_TOPICS = dep
    return _DEPLOY_TOPICS

_PIDX = None
def _paper_topics(slug):
    """The topic list for a slug (used to decide if its page is publicly featured)."""
    global _PIDX
    if _PIDX is None:
        _PIDX = {}
        try:
            for e in json.load(open(os.path.join(PAPERS, "_papers_index.json"), encoding="utf-8")):
                _PIDX[e["slug"]] = e.get("topics") or []
        except Exception:
            pass
    return _PIDX.get(slug, [])


def _portable_url(doi, title):
    """다운로드된 .html 에서도 살아있는 절대 URL. build_search_index 의
    _resolve_external 재사용 — 유효 DOI → doi.org, arXiv → arxiv.org, 없으면
    Zotero 에 등록된 원문 URL(_zotero_meta.json, 제목 매칭), 최후엔 Scholar 검색.
    compare_papers.py 도 이 구현을 공유한다."""
    global _BSI
    ext = ""
    try:
        if _BSI is None:
            import build_search_index as _bsi
            _BSI = _bsi
        _, _, ext = _BSI._resolve_external(title, doi, "")
    except Exception:
        # 폴백: DOI/arXiv 직접 해석 (Zotero meta 없이)
        d = (doi or "").strip()
        if re.match(r"^10\.\d{3,}/\S+$", d):
            ext = "https://doi.org/" + _urlquote(d)
        elif "arxiv" in d.lower():
            m = re.search(r"(\d{4}\.\d{4,5})", d)
            if m:
                ext = "https://arxiv.org/abs/" + m.group(1)
    return ext or ("https://scholar.google.com/scholar?q=" + _urlquote(title or ""))


def _load_connections():
    """Load every docs/<topic>/_paper_connections.json, freshest file winning.

    Topic dirs are DISCOVERED from the filesystem (any docs/ subdirectory
    holding a _paper_connections.json) — same rule as rebuild_connections.
    Topic names must not be hardcoded here: setup.py installs arbitrary topic
    aliases, and a fixed list silently drops their connections (surfaced as
    paper-curio comparisons missing 같이 보면 좋은 논문).

    A paper in two topics has a key in both files, and those two lists are only
    identical while both files were synced from the same global store. They are
    NOT after a single-topic sync: paper-curio's bridge syncs the primary topic
    only, so the other topic file keeps the previous snapshot. Merging in
    directory-name order then let the STALE file win by alphabet —
    ``ai4s-icml2026`` sorts after ``ai4s+scisci`` ('-' > '+'), so a freshly
    regenerated list was silently replaced by the older one and the new links
    never reached the page (2026-08-31: slug 10911 rendered 28 stale links
    instead of its 37 current ones). Merge oldest-first so the newest snapshot
    wins. A union is wrong here — these files are already-pruned views, and
    unioning them would resurrect edges that build_slug_resolver dropped.
    """
    global _connections_cache
    if _connections_cache:
        return _connections_cache
    docs_dir = os.path.dirname(PAPERS)
    try:
        entries = sorted(os.listdir(docs_dir))
    except OSError:
        entries = []
    paths = []
    for d in entries:
        conn_path = os.path.join(docs_dir, d, "_paper_connections.json")
        if not os.path.exists(conn_path):
            continue
        try:
            paths.append((os.path.getmtime(conn_path), d, conn_path))
        except OSError:
            continue
    for _mtime, d, conn_path in sorted(paths, key=lambda x: x[0]):
        try:
            with open(conn_path, "r", encoding="utf-8") as f:
                _connections_cache.update(json.load(f))
        except Exception as e:
            print(f"  [warn] {d}/_paper_connections.json load failed: {e}")
    return _connections_cache

def get_css(t):
    return f"""* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: 'KoPub Dotum', 'KoPubDotumMedium', -apple-system, 'Noto Sans KR', sans-serif; max-width: 820px; margin: 0 auto; padding: 2rem 1.5rem; line-height: 1.7; color: #333; background: #f0f2f5; }}
h1 {{ font-size: 1.4rem; color: #1a1a2e; border-bottom: 3px solid {t['accent']}; padding-bottom: 0.5rem; margin-bottom: 1rem; }}
h2 {{ font-size: 1.1rem; color: {t['accent']}; margin: 0 0 0.6rem; padding: 0; border: none; }}
h3 {{ font-size: 1rem; color: #333; margin: 0.8rem 0 0.4rem; }}
p {{ margin: 0.4rem 0; font-size: 0.93rem; }}
blockquote {{ border-left: 4px solid {t['accent']}; margin: 0.8rem 0; padding: 0.6rem 1rem; background: #f0f4f8; border-radius: 0 8px 8px 0; font-size: 0.88rem; color: #555; }}
ul, ol {{ margin: 0.4rem 0 0.4rem 1.5rem; }}
li {{ margin: 0.2rem 0; font-size: 0.93rem; }}
.section-box {{ background: white; border-radius: 12px; padding: 1.2rem 1.5rem; margin-bottom: 1rem; box-shadow: 0 1px 4px rgba(0,0,0,0.06); }}
table {{ border-collapse: collapse; margin: 0.5rem 0; font-size: 0.85rem; width: 100%; }}
th, td {{ border: 1px solid #e0e0e0; padding: 6px 12px; text-align: left; }}
th {{ background: {t['accent']}; color: white; font-weight: 600; font-size: 0.82rem; }}
tr:nth-child(even) {{ background: #f8f9fa; }}
td:last-child {{ text-align: center; font-weight: 600; color: {t['accent']}; }}
.eval-badges {{ display: flex; flex-wrap: wrap; gap: 0.4rem; margin: 0.6rem 0; }}
.eval-badge {{ background: {t['accent_bg']}; color: {t['accent_dark']}; padding: 0.2rem 0.7rem; border-radius: 14px; font-size: 0.8rem; font-weight: 600; }}
.dl-bar {{ margin: 0.5rem 0; }}
.dl-btn {{ background: {t['accent']}; color: #fff; border: none; border-radius: 8px; padding: 0.45rem 0.9rem; font-size: 0.85rem; cursor: pointer; font-family: inherit; }}
.dl-btn:hover {{ background: {t['accent_dark']}; }}
.essence-box {{ border: 2px solid {t['essence_border']}; border-radius: 10px; padding: 1rem 1.2rem; margin: 0.8rem 0; background: {t['essence_bg']}; }}
.essence-box h2 {{ color: {t['essence_border']}; margin: 0 0 0.5rem; border: none; padding: 0; }}
code {{ background: #e8edf3; padding: 0.15rem 0.4rem; border-radius: 4px; font-size: 0.85rem; }}
img {{ max-width: min(100%, 700px); border: 1px solid #e8e8e8; border-radius: 8px; margin: 0.8rem auto; display: block; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
hr {{ border: none; border-top: 1px solid #e0e0e0; margin: 0.5rem 0; }}
strong {{ color: #1a1a2e; }}
a {{ color: {t['link_color']}; }}
.back {{ margin-top: 1.5rem; padding: 0.8rem 0; border-top: 2px solid #e0e0e0; }}
.back a {{ font-weight: 600; text-decoration: none; }}
.back a:hover {{ text-decoration: underline; }}
.connections-box {{ background: white; border-radius: 12px; padding: 1.2rem 1.5rem; margin: 1.2rem 0; box-shadow: 0 1px 4px rgba(0,0,0,0.06); }}
.connections-box h2 {{ color: {t['accent']}; margin: 0 0 0.8rem; border: none; padding: 0; font-size: 1.05rem; }}
.conn-item {{ border-left: 3px solid #ddd; padding: 0.6rem 0 0.6rem 1rem; margin-bottom: 0.6rem; }}
.conn-item.alternative {{ border-left-color: #3B82F6; }}
.conn-item.extension {{ border-left-color: #10B981; }}
.conn-item.foundation {{ border-left-color: #8B5CF6; }}
.conn-item.counterpoint {{ border-left-color: #F59E0B; }}
.conn-item.application {{ border-left-color: #EF4444; }}
.conn-type {{ font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; color: #888; margin-bottom: 0.15rem; }}
.conn-item.alternative .conn-type {{ color: #3B82F6; }}
.conn-item.extension .conn-type {{ color: #10B981; }}
.conn-item.foundation .conn-type {{ color: #8B5CF6; }}
.conn-item.counterpoint .conn-type {{ color: #F59E0B; }}
.conn-item.application .conn-type {{ color: #EF4444; }}
.conn-title {{ font-size: 0.9rem; font-weight: 600; margin-bottom: 0.35rem; }}
.conn-title a {{ color: #1a1a2e; text-decoration: none; }}
.conn-title a:hover {{ color: {t['accent']}; text-decoration: underline; }}
.conn-reason {{ font-size: 0.85rem; color: #555; margin-top: 0.3rem; }}
.conn-reason-rel {{ font-weight: 700; color: #888; margin-right: 0.25rem; }}
/* Each reason carries its own relation badge so multiple reasons read equally. */
.conn-rel-badge {{ display: inline-block; font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.03em; margin-right: 0.4rem; padding: 0.05rem 0.4rem; border-radius: 4px; background: #f0f0f0; color: #666; vertical-align: middle; }}
.conn-rel-badge.alternative {{ color: #3B82F6; background: #EAF1FE; }}
.conn-rel-badge.extension {{ color: #10B981; background: #E7F7F1; }}
.conn-rel-badge.foundation {{ color: #8B5CF6; background: #F1ECFD; }}
.conn-rel-badge.counterpoint {{ color: #F59E0B; background: #FEF5E7; }}
.conn-rel-badge.application {{ color: #EF4444; background: #FDECEC; }}
.conn-ref {{ color: {t['accent']}; text-decoration: none; font-weight: 600; }}
.conn-ref:hover {{ text-decoration: underline; }}
.review-fig {{ text-align: center; margin: 1.5rem 0; padding: 1rem; background: #f8f9fa; border-radius: 12px; }}
.review-fig img {{ max-width: min(100%, 700px); border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); cursor: zoom-in; }}
.lightbox {{ display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); z-index: 9999; cursor: zoom-out; align-items: center; justify-content: center; }}
.lightbox.active {{ display: flex; }}
.lightbox img {{ max-width: 95%; max-height: 95%; object-fit: contain; border-radius: 8px; }}
.fig-caption {{ font-size: 0.85rem; color: #888; margin-top: 0.5rem; font-style: italic; }}"""


# ---------------------------------------------------------------------------
# Audio Overview (browser-direct podcast generation via Gemini). localhost-only.
# ---------------------------------------------------------------------------

def get_audio_css(t):
    return _audio_css_lib(t["accent"], t["accent_dark"], t["accent_bg"])


def audio_bar_html():
    """Button shown under the title. Always enabled — when the page is
    deployed without a baked key, the modal JS prompts the visitor for
    their own Gemini API key on first click and remembers it in
    localStorage."""
    return ('<div class="audio-bar">'
            '<button class="audio-btn" id="audio-open" onclick="openAudioModal()">'
            '\U0001F3A7 Audio Overview 생성</button></div>')


def audio_modal_html():
    return _audio_modal_lib(
        "이 논문 리뷰를 팟캐스트형 오디오로 생성합니다. "
        "(Gemini · 키는 브라우저에만 저장 · 완성본은 이메일로도 전송)"
    )


def audio_script_block(ctx):
    """Wrap the shared Audio Overview JS with this paper's static context."""
    return _audio_script_lib(_GEMINI_KEY, mode="paper", ctx=ctx,
                              local_emails=_LOCAL_EMAILS)


def parse_scores(md):
    """Extract evaluation scores from markdown table or list format."""
    scores = {}
    for label, key in [("Novelty", "novelty"), ("Technical Soundness", "tech"),
                        ("Significance", "sig"), ("Clarity", "clarity"), ("Overall", "overall")]:
        # Table: | Label | X/5 |
        m = re.search(rf'\|\s*{label}\s*\|\s*(\d+(?:\.\d+)?)\s*/\s*5\s*\|', md)
        if not m:
            # List: - Label: X/5  (tolerate **bold**/*italic* and a "(한글)"
            # gloss after the label, e.g. "- **Novelty (독창성)**: 4/5")
            m = re.search(rf'-\s*\**\s*{label}\s*(?:\([^)]*\))?\s*\**\s*:\s*(\d+(?:\.\d+)?)\s*/\s*5', md)
        if m:
            scores[key] = m.group(1)
    return scores


def _get_indent(line):
    """Return indent level (number of leading spaces / 2)."""
    stripped = line.lstrip()
    return (len(line) - len(stripped)) // 2 if stripped else 0


def _is_ul(s):
    return bool(re.match(r'^[-*]\s', s))


def _is_ol(s):
    return bool(re.match(r'^\d+\.\s', s))


def _list_content(s):
    if _is_ul(s):
        return re.sub(r'^[-*]\s+', '', s)
    if _is_ol(s):
        return re.sub(r'^\d+\.\s*', '', s)
    return s


def md_section_to_html(text, slug_dir=None):
    """Convert markdown body text to HTML (within a section)."""
    lines = text.strip().split('\n')
    out = []
    in_table = False
    table_header_done = False
    # List state: stack of (tag, indent_level)
    list_stack = []

    def close_lists_to(target_depth):
        while len(list_stack) > target_depth:
            tag, _ = list_stack.pop()
            out.append(f'</{tag}>')

    def close_all_lists():
        close_lists_to(0)

    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        indent = _get_indent(line)

        # Table row
        if s.startswith('|') and '|' in s[1:]:
            close_all_lists()
            if '---' in s:
                i += 1
                continue
            cells = [c.strip() for c in s.split('|')[1:-1]]
            if not in_table:
                out.append('<table>')
                in_table = True
                table_header_done = False
            if not table_header_done:
                out.append('<tr>' + ''.join(f'<th>{esc(c)}</th>' for c in cells) + '</tr>')
                table_header_done = True
            else:
                out.append('<tr>' + ''.join(f'<td>{esc(c)}</td>' for c in cells) + '</tr>')
            i += 1
            continue
        elif in_table:
            out.append('</table>')
            in_table = False

        # List items (any indent level)
        if _is_ul(s) or _is_ol(s):
            tag = 'ol' if _is_ol(s) else 'ul'
            content = _inline(_list_content(s))

            if not list_stack:
                # Start new list
                out.append(f'<{tag}>')
                list_stack.append((tag, indent))
            elif indent > list_stack[-1][1]:
                # Deeper indent → nested list inside last <li>
                # Remove closing </li> from last item to nest inside it
                if out and out[-1].endswith('</li>'):
                    out[-1] = out[-1][:-5]  # strip </li>
                out.append(f'<{tag}>')
                list_stack.append((tag, indent))
            elif indent < list_stack[-1][1]:
                # Shallower → close inner lists
                while list_stack and list_stack[-1][1] > indent:
                    t, _ = list_stack.pop()
                    out.append(f'</{t}>')
                    out.append('</li>')  # close parent <li>
                # Check if tag type matches
                if list_stack and list_stack[-1][0] != tag:
                    t, _ = list_stack.pop()
                    out.append(f'</{t}>')
                    out.append(f'<{tag}>')
                    list_stack.append((tag, indent))
            else:
                # Same level, check tag switch
                if list_stack[-1][0] != tag:
                    t, _ = list_stack.pop()
                    out.append(f'</{t}>')
                    out.append(f'<{tag}>')
                    list_stack.append((tag, indent))

            out.append(f'<li>{content}</li>')
            i += 1
            continue

        # Empty line inside list — look ahead to see if list continues
        if not s and list_stack:
            continues = False
            for j in range(i + 1, len(lines)):
                ps = lines[j].strip()
                if not ps:
                    continue
                if _is_ul(ps) or _is_ol(ps):
                    continues = True
                break
            if not continues:
                close_all_lists()
            i += 1
            continue

        # Non-list content → close any open lists
        if list_stack:
            close_all_lists()

        # Image + optional inline caption: ![alt](src) *caption*
        img_m = re.match(r'!\[([^\]]*)\]\(([^)]+)\)\s*(.*)', s)
        if img_m:
            alt, src, rest = img_m.group(1), img_m.group(2), img_m.group(3).strip()
            # Defensive: drop the reference entirely if the figure file is
            # missing on disk. Some older reviews reference figures that
            # were never extracted or were pruned later; rendering them
            # as-is produces broken <img> tags on the published page.
            # We also peek ahead to eat any adjacent italic-only caption
            # line so it does not end up orphaned after the drop.
            file_ok = True
            if slug_dir and not src.startswith(('http://', 'https://', 'data:')):
                abs_path = os.path.join(slug_dir, src)
                if not os.path.exists(abs_path):
                    file_ok = False
            if not file_ok:
                i += 1
                while i < len(lines) and not lines[i].strip():
                    i += 1
                if i < len(lines):
                    nxt_line = lines[i].strip()
                    if (nxt_line.startswith('*') and nxt_line.endswith('*')
                            and not nxt_line.startswith('**')):
                        i += 1
                continue
            out.append(f'<div class="review-fig"><img src="{esc(src)}" alt="{esc(alt)}">')
            # Inline caption on same line
            if rest and rest.startswith('*') and rest.endswith('*'):
                out.append(f'<p class="fig-caption">{_inline(rest)}</p></div>')
            else:
                out.append('</div>')
                # Check next line for caption
            i += 1
            continue

        # Italic-only line (figure caption) — attaches to preceding review-fig
        if s.startswith('*') and s.endswith('*') and not s.startswith('**'):
            if out and out[-1] == '</div>' and len(out) >= 2 and 'review-fig' in out[-2]:
                out.pop()
                out.append(f'<p class="fig-caption">{_inline(s)}</p></div>')
            else:
                out.append(f'<p class="fig-caption">{_inline(s)}</p>')
            i += 1
            continue

        # HR
        if s == '---' or s == '***':
            out.append('<hr>')
            i += 1
            continue

        # H3
        if s.startswith('### '):
            out.append(f'<h3>{_inline(s[4:])}</h3>')
            i += 1
            continue

        # Empty line
        if not s:
            i += 1
            continue

        # Paragraph
        out.append(f'<p>{_inline(s)}</p>')
        i += 1

    close_all_lists()
    if in_table:
        out.append('</table>')
    return '\n'.join(out)


def _inline(text):
    """Process inline markdown: bold, italic, links, code."""
    # Escape stray angle brackets first so literal tokens in prose (<UNKNOWN>,
    # <EOS>, <N>, leaked schema tags, …) render visibly instead of vanishing as
    # unknown HTML tags. The markdown rules below emit their own real tags on
    # the already-escaped text, so they are unaffected.
    text = text.replace('<', '&lt;').replace('>', '&gt;')
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<em>\1</em>', text)
    text = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2" target="_blank">\1</a>', text)
    # Remove empty markdown links: [](url) → just the URL or nothing
    def _fix_empty_link(m):
        url = m.group(1)
        # Empty DOI link like [](https://doi.org/) → remove entirely
        if url.rstrip('/') == 'https://doi.org':
            return 'N/A'
        # Non-empty URL with empty text → show URL as link
        return f'<a href="{url}" target="_blank">{url}</a>'
    text = re.sub(r'\[\]\((https?://[^)]+)\)', _fix_empty_link, text)
    # DOI auto-link — skip DOIs already inside <a> tags (href or link text)
    def _doi_auto_link(match):
        start = match.start()
        # Check if this DOI is inside an <a> tag by looking for unclosed <a before it
        before = text[:start]
        last_a_open = before.rfind('<a ')
        last_a_close = before.rfind('</a>')
        if last_a_open > last_a_close:
            return match.group(0)  # inside <a>...</a>, don't wrap
        return f'<a href="https://doi.org/{match.group(1)}" target="_blank">{match.group(1)}</a>'
    text = re.sub(r'(10\.\d{4,}/[^\s<"]+)', _doi_auto_link, text)
    return text


# .html 다운로드: 링크를 portable URL 로 치환하고 figure 를 data URI 로
# 인라인한 자기완결 복사본을 만든다 (플레인 문자열 — JS 문자열 안 개행 없음).
_DL_JS = r"""
async function downloadPageHtml() {
  var btn = document.querySelector('.dl-btn');
  var oldLabel = btn ? btn.textContent : '';
  if (btn) { btn.disabled = true; btn.textContent = '이미지 임베딩 중…'; }
  var root = document.documentElement.cloneNode(true);
  root.querySelectorAll('a[data-portable]').forEach(function (a) {
    var u = a.getAttribute('data-portable');
    if (u) { a.setAttribute('href', u); a.setAttribute('target', '_blank'); }
  });
  var live = document.querySelectorAll('img');
  var cloned = root.querySelectorAll('img');
  async function toDataUrl(src, liveImg) {
    // 1) Fetch the exact bytes (same-origin: local server or Cloudflare). This
    //    embeds the real webp/png losslessly and never taints — unlike canvas.
    try {
      var resp = await fetch(src, { cache: 'force-cache' });
      if (resp && resp.ok) {
        var blob = await resp.blob();
        return await new Promise(function (res, rej) {
          var fr = new FileReader();
          fr.onload = function () { res(fr.result); };
          fr.onerror = rej;
          fr.readAsDataURL(blob);
        });
      }
    } catch (e) { /* fall through to canvas */ }
    // 2) Canvas fallback (when fetch is blocked, e.g. file:// origin).
    try {
      if (liveImg && liveImg.complete && liveImg.naturalWidth) {
        var c = document.createElement('canvas');
        c.width = liveImg.naturalWidth; c.height = liveImg.naturalHeight;
        c.getContext('2d').drawImage(liveImg, 0, 0);
        return c.toDataURL('image/webp', 0.92);
      }
    } catch (e) { /* tainted → keep original path */ }
    return null;
  }
  for (var i = 0; i < live.length && i < cloned.length; i++) {
    var src = cloned[i].getAttribute('src') || '';
    if (!src || src.indexOf('data:') === 0) continue;
    var dataUrl = await toDataUrl(src, live[i]);
    if (dataUrl) cloned[i].setAttribute('src', dataUrl);
  }
  var h = '<!DOCTYPE html>' + root.outerHTML;
  var b = new Blob([h], { type: 'text/html' });
  var a = document.createElement('a');
  a.href = URL.createObjectURL(b);
  a.download = window._PAGE_SLUG + '.html';
  a.click();
  URL.revokeObjectURL(a.href);
  if (btn) { btn.disabled = false; btn.textContent = oldLabel; }
}
"""


def convert_review(md_path, topic, slug_dir):
    """Convert review.md to index.html with canonical template."""
    with open(md_path, 'r', encoding='utf-8') as f:
        md = f.read()

    # ── License / deploy 정책 (frontmatter 가 authoritative) ──
    _slug = os.path.basename(slug_dir)
    _fm_m = re.match(r"^---\n(.*?)\n---\n", md, re.DOTALL)
    _lic_raw = _fm_doi = ""
    if _fm_m:
        _b = _fm_m.group(1)
        _lm = re.search(r"(?m)^license:\s*(.*)$", _b)
        _lic_raw = _lm.group(1).strip().strip('"').strip("'") if _lm else ""
        _dm = re.search(r"(?m)^doi:\s*(.*)$", _b)
        _fm_doi = _dm.group(1).strip().strip('"').strip("'") if _dm else ""
    _lic_cls = _lic.normalize(_lic_raw)
    # 게이팅은 배포 사본(PC_PUBLIC_BUILD=1)에서만 — 로컬 렌더는 항상 full
    _is_public = (os.environ.get("PC_PUBLIC_BUILD") == "1"
                  and bool(set(_paper_topics(_slug)) & _deploy_topics()))
    _fig_strict = os.environ.get("PC_FIGURE_POLICY", "") == "strict"
    _allow_figs = (not _is_public) or _lic.figure_public_ok(_lic_cls, strict=_fig_strict)
    _nd_restrict = (_is_public and _lic.is_nd(_lic_cls)
                    and os.environ.get("PC_ND_POLICY", "suppress") != "show")

    # Strip YAML frontmatter (중첩 포함, DOI 등 값 내부 --- 구분)
    while md.startswith("---"):
        lines = md.split("\n")
        end_line = None
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == "---":
                end_line = i
                break
        if end_line is not None:
            md = "\n".join(lines[end_line + 1:]).lstrip("\n")
        else:
            break

    # Strip Related Papers section (auto-generated for Obsidian)
    md = re.sub(r'\n## Related Papers\n[\s\S]*?(?=\n## |\Z)', '', md)

    theme = THEMES.get(topic, THEMES["ai4s"])

    # Extract title — 본문 H1 → frontmatter title → slug 이름 순.
    # slug_dir 은 절대경로라서 그대로 쓰면 <title>/<h1> 에 로컬 경로가 새어 나간다.
    title_m = re.search(r'^#\s+(.+)', md, re.MULTILINE)
    if title_m:
        title = title_m.group(1).strip()
    else:
        _tm = re.search(r'(?m)^title:\s*(.+)$', _fm_m.group(1)) if _fm_m else None
        title = _tm.group(1).strip().strip('"').strip("'") if _tm else _slug

    # Extract metadata blockquote
    meta_m = re.search(r'^>\s*\*\*저자\*\*.*$', md, re.MULTILINE)
    meta_line = meta_m.group(0)[2:].strip() if meta_m else ""
    # Second line of blockquote (리뷰 모드)
    mode_m = re.search(r'^>\s*\*\*리뷰 모드\*\*:\s*(.+)', md, re.MULTILINE)
    mode = mode_m.group(1).strip() if mode_m else ""

    # Extract scores
    scores = parse_scores(md)

    # Split into sections by ## headers
    sections = re.split(r'^##\s+', md, flags=re.MULTILINE)
    # First section is everything before first ##
    parsed_sections = []
    for sec in sections[1:]:  # skip preamble
        lines = sec.split('\n', 1)
        sec_title = lines[0].strip()
        sec_body = lines[1] if len(lines) > 1 else ""
        parsed_sections.append((sec_title, sec_body))

    # Build HTML body
    body_parts = []

    # Title
    body_parts.append(f'<h1>{esc(title)}</h1>')
    # .html 다운로드 — figure 를 data URI 로 인라인하고 논문 링크를 portable
    # URL 로 치환한 자기완결 복사본을 내려받는다.
    body_parts.append(
        '<div class="dl-bar">'
        '<button class="dl-btn" onclick="downloadPageHtml()">.html 다운로드</button>'
        '</div>')
    # Audio Overview button (localhost-only; disabled when no key on deploy)
    body_parts.append(audio_bar_html())

    # Metadata
    if meta_line:
        meta_html = _inline(meta_line)
        # Zotero "Open PDF" button — same inline style as the Deep Research
        # reference list buttons in build_topic_index.py, so the affordance
        # looks identical wherever it appears. Only rendered when we have a
        # PDF attachment key for this slug (otherwise harmless skip).
        # slug_dir is a full path (docs/papers/<slug>) — strip to bare slug for lookup
        zkey = _ZOTERO_KEYS.get(os.path.basename(slug_dir), "")
        pdf_btn = ""
        if zkey:
            pdf_btn = (
                f' <a href="zotero://open-pdf/library/items/{esc(zkey)}" '
                f'title="Open PDF in Zotero" '
                f'style="margin-left:0.5rem; font-size:0.75rem; color:#555; '
                f'text-decoration:none; padding:0.05rem 0.4rem; '
                f'border-radius:3px; background:#f0f0f0; '
                f'border:1px solid #ddd;">'
                f'&#x1F4C4; PDF</a>'
            )
        body_parts.append(f'<blockquote><p>{meta_html}{pdf_btn}</p></blockquote>')

    body_parts.append('<hr>')
    # 인공지능기본법 제31조 고지 + 원문 저작권/출처 안내 (배포 대상=arXiv·OpenReview 공개 프리프린트)
    body_parts.append(
        '<div class="ai-notice" style="margin:0.6rem 0;padding:0.55rem 0.85rem;'
        'background:#fff8e1;border:1px solid #ffe0a3;border-radius:8px;'
        'font-size:0.82rem;color:#7a5b00;line-height:1.55;">'
        '&#9888;&#65039; 이 페이지의 요약&middot;평가&middot;해설은 <strong>생성형 AI(Claude)</strong>가 '
        '자동 생성한 2차적 분석물입니다. 논문 원문의 저작권은 <strong>원저작자</strong>에게 있으며, '
        '정확한 내용은 원문(위 DOI&middot;arXiv 등 출처)을 확인하세요.</div>')
    body_parts.append(
        f'<p style="font-size:0.8rem;color:#777;margin:0.2rem 0 0;">'
        f'라이선스: <strong>{esc(_lic.label(_lic_cls))}</strong></p>')

    # Sections (eval badges moved INTO Evaluation section)
    for sec_title, sec_body in parsed_sections:
        sec_html = md_section_to_html(sec_body, slug_dir)

        if sec_title.startswith('Essence') or '한줄 요약' in sec_title:
            if not sec_html.strip():
                continue
            body_parts.append(f'<div class="essence-box"><h2>Essence</h2>\n{sec_html}</div>')
        elif sec_title.startswith('평가') or sec_title.lower().startswith('eval'):
            # Evaluation section — render as badges (not table)
            badges = []
            for label, key in [("Novelty", "novelty"), ("Technical Soundness", "tech"),
                               ("Significance", "sig"), ("Clarity", "clarity"), ("Overall", "overall")]:
                if key in scores:
                    badges.append(f'<span class="eval-badge">{label}: {scores[key]}/5</span>')
            badges_html = f'<div class="eval-badges">{" ".join(badges)}</div>' if badges else ""
            # Extract 총평 from section body
            verdict_html = ""
            vm = re.search(r'\*\*총평\*\*:\s*([\s\S]+?)(?:\Z)', sec_body)
            if vm:
                verdict_html = f'<p><strong>총평</strong>: {_inline(vm.group(1).strip())}</p>'
            body_parts.append(f'<div class="section-box"><h2>Evaluation</h2>\n{badges_html}\n{verdict_html}</div>')
        else:
            body_parts.append(f'<div class="section-box"><h2>{esc(sec_title)}</h2>\n{sec_html}</div>')

    # Related papers (connections). The per-topic _paper_connections.json is
    # already bidirectional + per-target-deduped (see lib/connections.py): every
    # A→B edge implies B→A and a paper connected for several reasons appears once
    # with all reasons in its ``reasons`` array. So we render the paper's edge
    # list directly — no incoming scan, no per-relation duplication.
    connections = _load_connections()
    slug_dir_name = os.path.basename(slug_dir)
    conns = list(connections.get(slug_dir_name, []))
    if conns:
        # Load paper titles and dates for link text and sorting
        index_path = os.path.join(PAPERS, "_papers_index.json")
        slug_titles = {}
        slug_dates = {}
        slug_dois = {}
        if os.path.exists(index_path):
            with open(index_path, "r", encoding="utf-8") as f:
                for p in json.load(f):
                    slug_titles[p["slug"]] = p.get("title", p["slug"])
                    slug_dates[p["slug"]] = p.get("date", "")
                    slug_dois[p["slug"]] = p.get("doi", "")

        def _purl_attr(tslug):
            """다운로드본용 portable URL 속성 (라이브 페이지는 상대경로 유지)."""
            u = _portable_url(slug_dois.get(tslug, ""),
                              slug_titles.get(tslug, tslug))
            return f' data-portable="{esc(u)}"'

        type_labels = {
            "alternative": "다른 접근",
            "extension": "후속 연구",
            "foundation": "기반 연구",
            "counterpoint": "반론/비판",
            "application": "응용 사례",
        }

        # Defensive dedup by target slug: the data layer already collapses each
        # paper to one entry, but a slug can arrive via two topic files. Keep the
        # first entry and union its ``reasons`` so no reason is lost.
        _by_slug = {}
        for c in conns:
            cs = c.get("slug", "")
            if cs not in _by_slug:
                _by_slug[cs] = dict(c)
            else:
                merged = _by_slug[cs]
                seen = {(r.get("relation"), r.get("reason"))
                        for r in merged.get("reasons", [])}
                for r in c.get("reasons", []):
                    if (r.get("relation"), r.get("reason")) not in seen:
                        merged.setdefault("reasons", []).append(r)
                        seen.add((r.get("relation"), r.get("reason")))
        conns = list(_by_slug.values())

        # 정렬: 1차 관계 유형, 2차 시간순
        rel_order = {"foundation": 0, "alternative": 1, "extension": 2,
                      "application": 3, "counterpoint": 4}
        conns.sort(key=lambda c: (
            rel_order.get(c.get("relation", ""), 9),
            slug_dates.get(c.get("slug", ""), ""),
        ))

        # num → slug map for turning paper-number references inside reason text
        # into links. LLM-written reasons reference papers two ways: bracketed
        # ("[1065]") and bare with a Korean particle ("835는", "1021의"). We link
        # both. The map carries leading-zero-insensitive keys ("070" and "70").
        num_to_slug = {}
        for s in slug_titles:
            pre = s.split("_")[0]
            num_to_slug[pre] = s
            if pre.isdigit():
                num_to_slug[str(int(pre))] = s

        def _resolve(num):
            return num_to_slug.get(num) or (num_to_slug.get(str(int(num)))
                                            if num.isdigit() else None)

        # A bare number is treated as a paper reference only when (a) it is a real
        # paper number AND (b) a Korean reference particle follows it — this keeps
        # years ("2024년"), counts ("7개") and percentages ("79.4%") from linking.
        _JOSA = (r"(?:은|는|이|가|의|을|를|와|과|도|만|로|으로|에서|에게|보다|처럼"
                 r"|이라|라는|라고|및|과는|와는|이라는|이라고)")
        _REF_RE = re.compile(r"\[(\d+)\]|(?<![\d.])(\d{2,})(?=" + _JOSA + r")")

        def _linkify_refs(reason_text):
            """Escape reason text, then link every paper reference (bracketed or
            bare-with-particle). References to papers absent from the corpus stay
            plain; self-references link to the current page so none render dead."""
            def _repl(m):
                num = m.group(1) if m.group(1) is not None else m.group(2)
                tslug = _resolve(num)
                if not tslug:
                    return m.group(0)  # not in corpus → leave plain
                ttitle = esc(slug_titles.get(tslug, tslug))
                cls = ("conn-ref conn-ref-self" if tslug == slug_dir_name
                       else "conn-ref")
                label = f"[{num}]" if m.group(1) is not None else num
                return (f'<a class="{cls}" href="../{esc(tslug)}/index.html"'
                        f'{_purl_attr(tslug)} '
                        f'title="{ttitle}">{label}</a>')
            return _REF_RE.sub(_repl, esc(reason_text))

        conn_items = []
        for c in conns:
            cslug = c.get("slug", "")
            rel = c.get("relation", "alternative")
            ctitle = slug_titles.get(cslug, cslug)
            # One card per paper. Every reason is listed equally, each carrying its
            # own relation badge (기반 연구 / 다른 접근 / ...).
            rlist = c.get("reasons") or [{"relation": rel, "reason": c.get("reason", "")}]
            reason_html = []
            for rr in rlist:
                rreason = rr.get("reason", "")
                if not rreason:
                    continue
                rrel = rr.get("relation", rel)
                rlabel = type_labels.get(rrel, rrel)
                reason_html.append(
                    f'<div class="conn-reason">'
                    f'<span class="conn-rel-badge {esc(rrel)}">{esc(rlabel)}</span>'
                    f'{_linkify_refs(rreason)}</div>')
            conn_items.append(
                f'<div class="conn-item {esc(rel)}">'
                f'<div class="conn-title"><a href="../{esc(cslug)}/index.html"'
                f'{_purl_attr(cslug)}>{esc(ctitle)}</a></div>'
                + "".join(reason_html)
                + '</div>'
            )
        body_parts.append(
            '<div class="connections-box">'
            '<h2>같이 보면 좋은 논문</h2>'
            + "\n".join(conn_items)
            + '</div>'
        )

    # Back link
    body_parts.append(f'<div class="back"><a href="{theme["back_href"]}">&larr; 목록으로 돌아가기</a></div>')

    # Audio Overview context: title + cleaned review + related papers, embedded
    # for the browser-side script prompt. slug_titles/type_labels exist only
    # when conns was non-empty (defined inside the block above).
    audio_connections = []
    if conns:
        for c in conns:
            rlist = c.get("reasons") or [{"relation": c.get("relation", ""),
                                          "reason": c.get("reason", "")}]
            reason_txt = " / ".join(r.get("reason", "") for r in rlist
                                    if r.get("reason"))
            audio_connections.append({
                "title": slug_titles.get(c.get("slug", ""), c.get("slug", "")),
                "relation": type_labels.get(c.get("relation", ""), c.get("relation", "")),
                "reason": reason_txt,
            })
    # ND 논문은 audio overview(리뷰 기반 2차적 저작물)를 만들지 못하게 + 리뷰 텍스트 임베드도 생략
    audio_ctx = {"title": title,
                 "review": ("" if _nd_restrict else md),
                 "connections": ([] if _nd_restrict else audio_connections)}

    # OG 소셜 카드 — 링크 공유 시 제목/Essence/대표 figure 가 카드로 뜬다.
    # 이미지 URL 은 절대경로여야 크롤러가 읽는다. figures/…​.png 는 배포 시
    # prepare_deploy 가 .webp 로 함께 재작성하므로 로컬/웹 모두 정합.
    og_desc = ""
    ess_m = re.search(r'\n##\s*Essence[^\n]*\n([\s\S]+?)(?=\n##\s|\Z)', md)
    if ess_m:
        t = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', ess_m.group(1))
        t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)
        t = re.sub(r'[*_`>#|]', '', t)
        # Essence 박스는 figure 캡션(영문)이 앞서고 한글 요약이 뒤따른다 —
        # 카드 설명은 한글 요약 문단을 우선한다.
        paras = [re.sub(r'\s+', ' ', p).strip()
                 for p in re.split(r'\n\s*\n', t) if p.strip()]
        pick = next((p for p in paras if re.search(r'[가-힣]', p)),
                    paras[0] if paras else "")
        og_desc = pick[:160]
    og_img = ""
    fig_dir = os.path.join(slug_dir, "figures")
    if os.path.isdir(fig_dir):
        figs = sorted((f for f in os.listdir(fig_dir)
                       if re.match(r'fig\d+\.(png|webp)$', f)),
                      key=lambda f: int(re.findall(r'\d+', f)[0]))
        if figs:
            og_img = f"{_CF_BASE}/papers/{slug_dir_name}/figures/{figs[0]}"
    og_meta = (
        '<meta property="og:type" content="article">\n'
        '<meta property="og:site_name" content="Paper Curation">\n'
        f'<meta property="og:title" content="{esc(title)}">\n'
        + (f'<meta property="og:description" content="{esc(og_desc)}">\n' if og_desc else "")
        + f'<meta property="og:url" content="{_CF_BASE}/papers/{slug_dir_name}/">\n'
        + (f'<meta property="og:image" content="{og_img}">\n' if og_img else "")
        + f'<meta name="twitter:card" content="{"summary_large_image" if og_img else "summary"}">'
    )

    # 배포 공개 페이지: 라이선스 정책에 따라 figure(원본) gate + ND(2차적) 제한
    if _nd_restrict:
        _src = _portable_url(_fm_doi, title)
        body_html = (
            f'<h1>{esc(title)}</h1>'
            + (f'<blockquote><p>{_inline(meta_line)}</p></blockquote>' if meta_line else '')
            + f'<p style="font-size:0.8rem;color:#777;margin:0.2rem 0;">라이선스: <strong>{esc(_lic.label(_lic_cls))}</strong></p>'
            + '<div class="ai-notice" style="margin:0.8rem 0;padding:0.7rem 0.9rem;'
              'background:#fdecea;border:1px solid #f5b7b1;border-radius:8px;'
              'font-size:0.9rem;color:#8a2a20;line-height:1.6;">'
              '&#128274; 이 논문은 <strong>변경금지(NoDerivatives)</strong> 라이선스라 '
              '2차적 저작물(AI 리뷰&middot;요약)의 공개가 제한됩니다. 원문에서 확인하세요: '
              f'<a href="{esc(_src)}" target="_blank" rel="noopener" style="color:#8a2a20;font-weight:700;">원문 보기 &rarr;</a></div>'
            + f'<div class="back"><a href="{theme["back_href"]}">&larr; 목록으로 돌아가기</a></div>'
        )
    else:
        body_html = "\n".join(body_parts)
        if not _allow_figs:
            body_html = re.sub(
                r'(<div class="review-fig">)<img[^>]*>',
                (r'\1<div class="fig-gated" style="padding:1.2rem;color:#999;'
                 r'font-size:0.85rem;line-height:1.5;">'
                 '&#128274; 원문 도표는 라이선스(위 표시)상 여기서 재현하지 않습니다 &mdash; 원문에서 확인하세요.'
                 '</div>'),
                body_html)

    # Assemble
    css = get_css(theme) + "\n" + get_audio_css(theme)
    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{esc(title)}</title>
{og_meta}
<link rel="stylesheet" href="https://cdn.jsdelivr.net/font-kopub/1.0/kopubdotum.css">
<script>window.MathJax={{tex:{{inlineMath:[['$','$'],['\\\\(','\\\\)']],displayMath:[['$$','$$'],['\\\\[','\\\\]']]}}}};</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>
<style>
{css}
</style>
</head>
<body>
{body_html}
{"" if _nd_restrict else audio_modal_html()}
<div id="lightbox" class="lightbox"><img id="lightbox-img" alt=""></div>
<script>
document.addEventListener('DOMContentLoaded', function() {{
  const lb = document.getElementById('lightbox');
  const lbImg = document.getElementById('lightbox-img');
  document.addEventListener('click', function(e) {{
    const img = e.target.closest('.review-fig img');
    if (img) {{ lbImg.src = img.src; lb.classList.add('active'); }}
  }});
  lb.addEventListener('click', function() {{ lb.classList.remove('active'); lbImg.src = ''; }});
  document.addEventListener('keydown', function(e) {{
    if (e.key === 'Escape' && lb.classList.contains('active')) {{ lb.classList.remove('active'); lbImg.src = ''; }}
  }});
}});
</script>
<script>
window._PAGE_SLUG = {json.dumps(slug_dir_name)};
{_DL_JS}
</script>
{"" if _nd_restrict else audio_script_block(audio_ctx)}
<footer style="text-align:center;padding:2rem 0 1rem;color:#999;font-size:0.85rem;border-top:1px solid #eee;margin-top:3rem;">
게재 논문은 arXiv&middot;OpenReview 등 공개 프리프린트이며 원문 저작권은 원저작자에게 귀속됩니다 &middot; 이 페이지의 리뷰&middot;요약&middot;해설은 생성형 AI가 생성한 2차적 분석물입니다<br>
Developed by Jehyun Lee, KIST AIX Strategy Department | jehyun.lee@gmail.com
</footer>
</body>
</html>"""
    return html


def detect_topic(slug, index_path=None):
    """Detect topic from _papers_index.json."""
    if index_path and os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            idx = json.load(f)
        for p in idx:
            if p['slug'] == slug:
                topics = p.get('topics', [])
                if topics:
                    return topics[0]
                return p.get('primary_topic', 'ai4s')
    return "ai4s"


def _resolve_target_slugs(all_slugs, *, slug=None, slugs=None,
                          with_connected=False, connections=None):
    """Pure resolver: which paper dirs to (re)render, given the corpus list.

    `slugs` may be a list, a comma-separated string ("9121,9122"), or a
    'start-end' numeric range ("251-258"). A bare prefix matches an exact slug or
    an "NNN_" prefix (so "120" hits 120_* but not 1200_*). NOTE: a raw string is
    normalized to a list first — iterating the string directly would walk
    characters and match almost everything.

    With `with_connected` (and a merged `connections` dict), the result is
    expanded to include every paper connected to a seed, so a new/changed
    connection's reverse edge is re-rendered on the neighbour's own page. The
    bidirectional view is global, so a seed's connection list already names all
    its neighbours in both directions.
    """
    if slug:
        target = [slug] if slug in all_slugs else [d for d in all_slugs if d.startswith(slug)]
    elif isinstance(slugs, str) and re.fullmatch(r'\s*\d+\s*-\s*\d+\s*', slugs):
        a, b = (int(x) for x in slugs.split('-'))
        def _num(d):
            m = re.match(r'^(\d+)_', d)
            return int(m.group(1)) if m else 0
        target = [d for d in all_slugs if a <= _num(d) <= b]
    elif slugs:
        slug_list = ([s.strip() for s in slugs.split(',')]
                     if isinstance(slugs, str) else list(slugs))
        slug_list = [s for s in slug_list if s]
        target = [d for d in all_slugs
                  if any(d == s or d.startswith(s + '_') for s in slug_list)]
    else:
        target = list(all_slugs)

    if with_connected and target and connections:
        valid = set(all_slugs)
        extra = set()
        for s in target:
            for c in connections.get(s, []) or []:
                t = c.get('slug')
                if t in valid:
                    extra.add(t)
        target = sorted(set(target) | extra)
    return target


def _run_review_to_html(*, topic=None, slug=None, slugs=None, all_papers=False,
                        with_connected=False):
    """Programmatic entrypoint for review_to_html.

    - `slug` (str): one slug to convert (mutually exclusive with `slugs`).
    - `slugs`: a list of slugs, a comma-separated string ("9121,9122"), or a
      'start-end' numeric range string ("251-258").
    - `all_papers`: convert everything (same as default behavior).
    - `with_connected`: also re-render every paper connected to the selected
      seeds, so a new/changed connection shows its reverse edge on the
      neighbour's own page.
    """
    index_path = os.path.join(PAPERS, "_papers_index.json")

    all_slugs = sorted(d for d in os.listdir(PAPERS)
                       if os.path.isdir(os.path.join(PAPERS, d)) and re.match(r'^\d{3,}_', d))

    target_slugs = _resolve_target_slugs(
        all_slugs, slug=slug,
        slugs=(None if all_papers else slugs),
        with_connected=with_connected,
        connections=_load_connections() if with_connected else None)

    converted = 0
    skipped = 0
    for s in target_slugs:
        md_path = os.path.join(PAPERS, s, "review.md")
        html_path = os.path.join(PAPERS, s, "index.html")
        if not os.path.exists(md_path):
            skipped += 1
            continue
        slug_topic = topic or detect_topic(s, index_path)
        slug_dir = os.path.join(PAPERS, s)
        html = convert_review(md_path, slug_topic, slug_dir)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)
        converted += 1

    print(f"Converted: {converted}, Skipped: {skipped}")
    return {"converted": converted, "skipped": skipped}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--topic', default=None, help='Force topic (ai4s/scisci)')
    parser.add_argument('--slugs', default=None,
                        help='Slug range "251-258" or comma list "9121,9122"')
    parser.add_argument('--all', action='store_true', help='Regenerate all')
    parser.add_argument('--with-connected', action='store_true',
                        help='Also re-render pages of papers connected to --slugs '
                             '(so reverse edges show on neighbour pages)')
    args = parser.parse_args()
    _run_review_to_html(topic=args.topic, slugs=args.slugs, all_papers=args.all,
                        with_connected=args.with_connected)


if __name__ == "__main__":
    main()
