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

REPO = os.path.dirname(os.path.abspath(__file__))
PAPERS = os.path.join(REPO, "papers")

THEMES = {
    "ai4s": {"accent": "#D63423", "accent_dark": "#A62018", "accent_bg": "#FEF0EF",
             "essence_border": "#8B1A1A", "essence_bg": "#FDF8F8",
             "link_color": "#A62018", "back_href": "../../ai4s/index.html"},
    "scisci": {"accent": "#2374D6", "accent_dark": "#1856A0", "accent_bg": "#EBF3FF",
               "essence_border": "#1856A0", "essence_bg": "#F8FAFD",
               "link_color": "#1856A0", "back_href": "../../scisci/index.html"},
}

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


def md_section_to_html(text):
    """Convert markdown body text to HTML (within a section)."""
    lines = text.strip().split('\n')
    out = []
    in_list = False
    in_table = False
    table_header_done = False

    for line in lines:
        s = line.strip()

        # Table row
        if s.startswith('|') and '|' in s[1:]:
            if '---' in s:
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
            continue
        elif in_table:
            out.append('</table>')
            in_table = False

        # List item
        if re.match(r'^[-*]\s', s):
            if not in_list:
                out.append('<ul>')
                in_list = True
            content = re.sub(r'^[-*]\s+', '', s)
            content = _inline(content)
            out.append(f'<li>{content}</li>')
            continue
        elif s.startswith(('1.', '2.', '3.', '4.', '5.')):
            if not in_list:
                out.append('<ol>')
                in_list = True
            content = re.sub(r'^\d+\.\s*', '', s)
            content = _inline(content)
            out.append(f'<li>{content}</li>')
            continue
        elif in_list:
            if s.startswith('  ') and in_list:  # continuation
                content = _inline(s.strip())
                out.append(f'<li>{content}</li>')
                continue
            tag = '</ol>' if any('</ol>' not in x and '<ol>' in x for x in out) else '</ul>'
            out.append('</ul>' if '<ul>' in '\n'.join(out[max(0,len(out)-20):]) else '</ol>')
            in_list = False

        # Image
        m = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', s)
        if m:
            out.append(f'<div class="review-fig"><img src="{esc(m.group(2))}" alt="{esc(m.group(1))}">'
                       f'<p class="fig-caption">{esc(m.group(1))}</p></div>')
            continue

        # Italic-only line (figure caption)
        if s.startswith('*') and s.endswith('*') and not s.startswith('**'):
            out.append(f'<p class="fig-caption">{_inline(s)}</p>')
            continue

        # HR
        if s == '---' or s == '***':
            out.append('<hr>')
            continue

        # H3
        if s.startswith('### '):
            out.append(f'<h3>{_inline(s[4:])}</h3>')
            continue

        # Empty line
        if not s:
            continue

        # Paragraph
        out.append(f'<p>{_inline(s)}</p>')

    if in_list:
        out.append('</ul>')
    if in_table:
        out.append('</table>')
    return '\n'.join(out)


def _inline(text):
    """Process inline markdown: bold, italic, links, code."""
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<em>\1</em>', text)
    text = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2" target="_blank">\1</a>', text)
    # DOI auto-link
    text = re.sub(r'(?<!href=")(10\.\d{4,}/[^\s<]+)', r'<a href="https://doi.org/\1" target="_blank">\1</a>', text)
    return text


def convert_review(md_path, topic, slug_dir):
    """Convert review.md to index.html with canonical template."""
    with open(md_path, 'r', encoding='utf-8') as f:
        md = f.read()

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

    # Check for figures
    fig_dir = os.path.join(os.path.dirname(md_path), "figures")
    has_fig1 = os.path.exists(os.path.join(fig_dir, "fig1.png"))

    # Build HTML body
    body_parts = []

    # Title
    body_parts.append(f'<h1>{esc(title)}</h1>')

    # Metadata
    if meta_line:
        meta_html = _inline(meta_line)
        body_parts.append(f'<blockquote><p>{meta_html}</p></blockquote>')

    # Figure 1 after metadata
    if has_fig1:
        body_parts.append('<div class="review-fig"><img src="figures/fig1.png" alt="Figure 1">'
                         '<p class="fig-caption">Figure 1</p></div>')

    body_parts.append('<hr>')

    # Sections (eval badges moved INTO Evaluation section)
    for sec_title, sec_body in parsed_sections:
        sec_html = md_section_to_html(sec_body)

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
                       if os.path.isdir(os.path.join(PAPERS, d)) and re.match(r'^\d{3}_', d))

    if args.slugs:
        start, end = args.slugs.split('-')
        slugs = [d for d in all_slugs if int(d[:3]) >= int(start) and int(d[:3]) <= int(end)]
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
