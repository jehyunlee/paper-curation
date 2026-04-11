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

from config_loader import PAPERS_DIR as _PAPERS_DIR
PAPERS = str(_PAPERS_DIR)

THEMES = {
    "ai4s": {"accent": "#D63423", "accent_dark": "#A62018", "accent_bg": "#FEF0EF",
             "essence_border": "#8B1A1A", "essence_bg": "#FDF8F8",
             "link_color": "#A62018", "back_href": "../../ai4s/index.html"},
    "scisci": {"accent": "#2374D6", "accent_dark": "#1856A0", "accent_bg": "#EBF3FF",
               "essence_border": "#1856A0", "essence_bg": "#F8FAFD",
               "link_color": "#1856A0", "back_href": "../../scisci/index.html"},
}

# Paper connections cache (loaded once per run)
_connections_cache = {}

def _load_connections():
    """Load all _paper_connections.json files."""
    global _connections_cache
    if _connections_cache:
        return _connections_cache
    from config_loader import get_topic_dir
    for topic in THEMES:
        conn_path = os.path.join(str(get_topic_dir(topic)), "_paper_connections.json")
        if os.path.exists(conn_path):
            with open(conn_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            _connections_cache.update(data)
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
.conn-title {{ font-size: 0.9rem; font-weight: 600; }}
.conn-title a {{ color: #1a1a2e; text-decoration: none; }}
.conn-title a:hover {{ color: {t['accent']}; text-decoration: underline; }}
.conn-reason {{ font-size: 0.85rem; color: #555; margin-top: 0.15rem; }}
.review-fig {{ text-align: center; margin: 1.5rem 0; padding: 1rem; background: #f8f9fa; border-radius: 12px; }}
.review-fig img {{ max-width: min(100%, 700px); border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); cursor: zoom-in; }}
.lightbox {{ display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); z-index: 9999; cursor: zoom-out; align-items: center; justify-content: center; }}
.lightbox.active {{ display: flex; }}
.lightbox img {{ max-width: 95%; max-height: 95%; object-fit: contain; border-radius: 8px; }}
.fig-caption {{ font-size: 0.85rem; color: #888; margin-top: 0.5rem; font-style: italic; }}"""


def parse_scores(md):
    """Extract evaluation scores from markdown table or list format."""
    scores = {}
    for label, key in [("Novelty", "novelty"), ("Technical Soundness", "tech"),
                        ("Significance", "sig"), ("Clarity", "clarity"), ("Overall", "overall")]:
        # Table: | Label | X/5 |
        m = re.search(rf'\|\s*{label}\s*\|\s*(\d+(?:\.\d+)?)\s*/\s*5\s*\|', md)
        if not m:
            # List: - Label: X/5
            m = re.search(rf'-\s*{label}\s*:\s*(\d+(?:\.\d+)?)\s*/\s*5', md)
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


def convert_review(md_path, topic, slug_dir):
    """Convert review.md to index.html with canonical template."""
    with open(md_path, 'r', encoding='utf-8') as f:
        md = f.read()

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

    # Extract title
    title_m = re.search(r'^#\s+(.+)', md, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else slug_dir

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

    # Metadata
    if meta_line:
        meta_html = _inline(meta_line)
        body_parts.append(f'<blockquote><p>{meta_html}</p></blockquote>')

    body_parts.append('<hr>')

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

    # Related papers (connections)
    connections = _load_connections()
    slug_dir_name = os.path.basename(slug_dir)
    outgoing = connections.get(slug_dir_name, [])
    # Incoming: 이 논문을 참조하는 다른 논문들
    incoming = []
    for src_slug, src_conns in connections.items():
        if src_slug == slug_dir_name:
            continue
        for c in src_conns:
            if c.get("slug") == slug_dir_name:
                incoming.append({
                    "slug": src_slug,
                    "relation": c.get("relation", "alternative"),
                    "reason": c.get("reason", ""),
                })
    conns = outgoing + incoming
    if conns:
        # Load paper titles and dates for link text and sorting
        index_path = os.path.join(PAPERS, "_papers_index.json")
        slug_titles = {}
        slug_dates = {}
        if os.path.exists(index_path):
            with open(index_path, "r", encoding="utf-8") as f:
                for p in json.load(f):
                    slug_titles[p["slug"]] = p.get("title", p["slug"])
                    slug_dates[p["slug"]] = p.get("date", "")

        type_labels = {
            "alternative": "다른 접근",
            "extension": "후속 연구",
            "foundation": "기반 연구",
            "counterpoint": "반론/비판",
            "application": "응용 사례",
        }

        # Dedup within the same relation: a paper appearing twice as e.g.
        # "alternative" for the same source is redundant. The same paper
        # is still allowed to show up under *different* relation types
        # (e.g. both "alternative" and "application") because those carry
        # distinct meanings. We keep the first occurrence so upstream
        # ordering (if any) is preserved; the explicit sort below then
        # places every surviving entry in the canonical order.
        _seen_pairs = set()
        _deduped = []
        for c in conns:
            key = (c.get("relation", ""), c.get("slug", ""))
            if key in _seen_pairs:
                continue
            _seen_pairs.add(key)
            _deduped.append(c)
        conns = _deduped

        # 정렬: 1차 관계 유형, 2차 시간순
        rel_order = {"foundation": 0, "alternative": 1, "extension": 2,
                      "application": 3, "counterpoint": 4}
        conns.sort(key=lambda c: (
            rel_order.get(c.get("relation", ""), 9),
            slug_dates.get(c.get("slug", ""), ""),
        ))

        conn_items = []
        for c in conns:
            cslug = c.get("slug", "")
            rel = c.get("relation", "alternative")
            reason = c.get("reason", "")
            ctitle = slug_titles.get(cslug, cslug)
            label = type_labels.get(rel, rel)
            conn_items.append(
                f'<div class="conn-item {esc(rel)}">'
                f'<div class="conn-type">{esc(label)}</div>'
                f'<div class="conn-title"><a href="../{esc(cslug)}/index.html">{esc(ctitle)}</a></div>'
                f'<div class="conn-reason">{esc(reason)}</div>'
                f'</div>'
            )
        body_parts.append(
            '<div class="connections-box">'
            '<h2>같이 보면 좋은 논문</h2>'
            + "\n".join(conn_items)
            + '</div>'
        )

    # Back link
    body_parts.append(f'<div class="back"><a href="{theme["back_href"]}">&larr; 목록으로 돌아가기</a></div>')

    # Assemble
    css = get_css(theme)
    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{esc(title)}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/font-kopub/1.0/kopubdotum.css">
<script>window.MathJax={{tex:{{inlineMath:[['$','$'],['\\\\(','\\\\)']],displayMath:[['$$','$$'],['\\\\[','\\\\]']]}}}};</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>
<style>
{css}
</style>
</head>
<body>
{chr(10).join(body_parts)}
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
<footer style="text-align:center;padding:2rem 0 1rem;color:#999;font-size:0.85rem;border-top:1px solid #eee;margin-top:3rem;">
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--topic', default=None, help='Force topic (ai4s/scisci)')
    parser.add_argument('--slugs', default=None, help='Slug range: 251-258')
    parser.add_argument('--all', action='store_true', help='Regenerate all')
    args = parser.parse_args()

    index_path = os.path.join(PAPERS, "_papers_index.json")

    # Determine which slugs to process
    all_slugs = sorted(d for d in os.listdir(PAPERS)
                       if os.path.isdir(os.path.join(PAPERS, d)) and re.match(r'^\d{3,}_', d))

    if args.slugs:
        start, end = args.slugs.split('-')
        def _slug_num(d):
            m = re.match(r'^(\d+)_', d)
            return int(m.group(1)) if m else 0
        slugs = [d for d in all_slugs if _slug_num(d) >= int(start) and _slug_num(d) <= int(end)]
    elif args.all:
        slugs = all_slugs
    else:
        slugs = all_slugs

    converted = 0
    skipped = 0
    for slug in slugs:
        md_path = os.path.join(PAPERS, slug, "review.md")
        html_path = os.path.join(PAPERS, slug, "index.html")
        if not os.path.exists(md_path):
            skipped += 1
            continue

        topic = args.topic or detect_topic(slug, index_path)
        html = convert_review(md_path, topic, slug)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)
        converted += 1

    print(f"Converted: {converted}, Skipped: {skipped}")


if __name__ == "__main__":
    main()
