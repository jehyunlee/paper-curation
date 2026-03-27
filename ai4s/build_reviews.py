import os, re, html as html_lib

base = r'C:/Users/jehyu/Arbeitplatz/paper-curation/ai4s'

REVIEW_CSS = """* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'KoPub Dotum', 'KoPubDotumMedium', -apple-system, 'Noto Sans KR', sans-serif; max-width: 820px; margin: 0 auto; padding: 2rem 1.5rem; line-height: 1.7; color: #333; background: #f0f2f5; }
h1 { font-size: 1.4rem; color: #1a1a2e; border-bottom: 3px solid #D63423; padding-bottom: 0.5rem; margin-bottom: 1rem; }
h2 { font-size: 1.1rem; color: #D63423; margin: 1.2rem 0 0.6rem; }
h3 { font-size: 1rem; color: #333; margin: 0.8rem 0 0.4rem; }
p { margin: 0.4rem 0; }
blockquote { border-left: 4px solid #D63423; margin: 0.8rem 0; padding: 0.6rem 1rem; background: #f0f4f8; border-radius: 0 8px 8px 0; font-size: 0.88rem; color: #555; }
ul, ol { margin: 0.4rem 0 0.4rem 1.5rem; }
li { margin: 0.2rem 0; font-size: 0.93rem; }
.section-box { background: white; border-radius: 12px; padding: 1.2rem 1.5rem; margin-bottom: 1rem; box-shadow: 0 1px 4px rgba(0,0,0,0.06); }
table { border-collapse: collapse; margin: 0.5rem 0; font-size: 0.85rem; width: auto; }
th, td { border: 1px solid #e0e0e0; padding: 4px 10px; text-align: left; }
th { background: #D63423; color: white; font-weight: 600; font-size: 0.82rem; }
tr:nth-child(even) { background: #f8f9fa; }
td:last-child { text-align: center; font-weight: 600; color: #D63423; }
.eval-badges { display: flex; flex-wrap: wrap; gap: 0.4rem; margin: 0.6rem 0; }
.eval-badge { background: #FEF0EF; color: #A62018; padding: 0.2rem 0.7rem; border-radius: 14px; font-size: 0.8rem; font-weight: 600; }
.essence-box { border: 2px solid #8B1A1A; border-radius: 10px; padding: 1rem 1.2rem; margin: 0.8rem 0; background: #FDF8F8; }
.essence-box h2 { color: #8B1A1A; margin: 0 0 0.5rem; }
code { background: #e8edf3; padding: 0.15rem 0.4rem; border-radius: 4px; font-size: 0.85rem; }
pre { background: #1a1a2e; color: #e0e0e0; padding: 1rem; border-radius: 8px; overflow-x: auto; margin: 0.8rem 0; }
pre code { background: none; color: inherit; }
img { max-width: min(100%, 800px); border: 1px solid #e8e8e8; border-radius: 8px; margin: 0.8rem auto; display: block; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
em { font-style: italic; }
hr { border: none; border-top: 1px solid #e0e0e0; margin: 0.5rem 0; }
strong { color: #1a1a2e; }
a { color: #A62018; }
.back { margin-top: 2rem; padding: 1rem 0; border-top: 2px solid #e0e0e0; }
.back a { font-weight: 600; text-decoration: none; font-size: 0.95rem; }
.back a:hover { text-decoration: underline; }
.review-fig { text-align: center; margin: 1.5rem 0; padding: 1rem; background: #f8f9fa; border-radius: 12px; }
.review-fig img { max-width: min(100%, 800px); border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
.fig-caption { font-size: 0.85rem; color: #888; margin-top: 0.5rem; font-style: italic; }"""


def md_to_html(content, dir_name):
    """Convert review.md markdown to HTML body content."""
    lines = content.split('\n')
    out = []
    in_table = False
    table_lines = []
    in_code = False
    code_lang = ''
    code_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]

        # Code block
        if line.startswith('```'):
            if not in_code:
                in_code = True
                code_lang = line[3:].strip()
                code_lines = []
            else:
                in_code = False
                code_text = '\n'.join(html_lib.escape(cl) for cl in code_lines)
                lang_attr = f' class="language-{code_lang}"' if code_lang else ''
                out.append(f'<pre><code{lang_attr}>{code_text}</code></pre>')
            i += 1
            continue

        if in_code:
            code_lines.append(line)
            i += 1
            continue

        # Table
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                in_table = True
                table_lines = []
            table_lines.append(line)
            i += 1
            continue
        elif in_table:
            in_table = False
            # Render table
            rows = [r for r in table_lines if r.strip() and not re.match(r'^\s*\|[-| :]+\|\s*$', r)]
            if rows:
                out.append('<table>')
                for ri, row in enumerate(rows):
                    cells = [c.strip() for c in row.strip().strip('|').split('|')]
                    tag = 'th' if ri == 0 else 'td'
                    out.append('<tr>' + ''.join(f'<{tag}>{html_lib.escape(c)}</{tag}>' for c in cells) + '</tr>')
                out.append('</table>')
            table_lines = []

        # Headings
        if line.startswith('# '):
            # Skip h1 - title is already in <h1> tag
            i += 1
            continue
        elif line.startswith('## '):
            text = line[3:].strip()
            out.append(f'<h2>{html_lib.escape(text)}</h2>')
            i += 1
            continue
        elif line.startswith('### '):
            text = line[4:].strip()
            out.append(f'<h3>{html_lib.escape(text)}</h3>')
            i += 1
            continue
        elif line.startswith('#### '):
            text = line[5:].strip()
            out.append(f'<h4>{html_lib.escape(text)}</h4>')
            i += 1
            continue

        # Blockquote
        if line.startswith('> '):
            # Collect consecutive blockquote lines
            bq_lines = []
            while i < len(lines) and lines[i].startswith('> '):
                bq_lines.append(inline_md(lines[i][2:]))
                i += 1
            out.append('<blockquote><p>' + '</p><p>'.join(bq_lines) + '</p></blockquote>')
            continue

        # HR
        if re.match(r'^[-*_]{3,}\s*$', line):
            out.append('<hr>')
            i += 1
            continue

        # Unordered list
        if re.match(r'^[-*+] ', line):
            ul_lines = []
            while i < len(lines) and re.match(r'^[-*+] ', lines[i]):
                ul_lines.append(f'<li>{inline_md(lines[i][2:])}</li>')
                i += 1
            out.append('<ul>' + ''.join(ul_lines) + '</ul>')
            continue

        # Ordered list
        if re.match(r'^\d+\. ', line):
            ol_lines = []
            while i < len(lines) and re.match(r'^\d+\. ', lines[i]):
                text = re.sub(r'^\d+\. ', '', lines[i])
                ol_lines.append(f'<li>{inline_md(text)}</li>')
                i += 1
            out.append('<ol>' + ''.join(ol_lines) + '</ol>')
            continue

        # Image: ![alt](src)
        img_m = re.match(r'^!\[([^\]]*)\]\(([^)]+)\)', line.strip())
        if img_m:
            alt = html_lib.escape(img_m.group(1))
            src = img_m.group(2)
            # Convert relative paths (keep as-is for review HTML)
            out.append(f'<div class="review-fig"><img src="{src}" alt="{alt}"><p class="fig-caption">{alt}</p></div>')
            i += 1
            continue

        # Empty line
        if not line.strip():
            i += 1
            continue

        # Paragraph
        out.append(f'<p>{inline_md(line)}</p>')
        i += 1

    # Flush table if at end
    if in_table and table_lines:
        rows = [r for r in table_lines if r.strip() and not re.match(r'^\s*\|[-| :]+\|\s*$', r)]
        if rows:
            out.append('<table>')
            for ri, row in enumerate(rows):
                cells = [c.strip() for c in row.strip().strip('|').split('|')]
                tag = 'th' if ri == 0 else 'td'
                out.append('<tr>' + ''.join(f'<{tag}>{html_lib.escape(c)}</{tag}>' for c in cells) + '</tr>')
            out.append('</table>')

    return '\n'.join(out)


def inline_md(text):
    """Convert inline markdown to HTML."""
    # Bold+italic
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Inline code
    text = re.sub(r'`([^`]+)`', lambda m: f'<code>{html_lib.escape(m.group(1))}</code>', text)
    # Links
    text = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2" target="_blank">\1</a>', text)
    # Bare URLs
    text = re.sub(r'(?<!["\(])(https?://\S+)', r'<a href="\1" target="_blank">\1</a>', text)
    # Escape remaining HTML (but preserve our tags)
    # Actually we need to be careful not to double-escape - inline_md works on raw text
    return text


def generate_review_html(meta, content, dir_path):
    title = html_lib.escape(meta['title'])
    body_content = md_to_html(content, meta['dir'])

    # Fig1 at top if exists
    fig_html = ''
    if meta['has_fig']:
        fig_html = '<div class="review-fig"><img src="figures/fig1.png" alt="Figure 1"><p class="fig-caption">Figure 1</p></div>'

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/font-kopub/1.0/kopubdotum.css">
<script>window.MathJax={{tex:{{inlineMath:[['$','$'],['\\\\(','\\\\)']],displayMath:[['$$','$$'],['\\\\[','\\\\]']]}}}};</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>
<style>
{REVIEW_CSS}
</style>
</head>
<body>
<h1>{title}</h1>
{fig_html}
{body_content}
<div class="back"><a href="../index.html">← 목록으로 돌아가기</a></div>
</body>
</html>"""


# Process each new paper
count = 0
for n in range(236, 251):
    for d in sorted(os.listdir(base)):
        m = re.match(r'^(\d+)_', d)
        if m and int(m.group(1)) == n:
            rp = os.path.join(base, d, 'review.md')
            if not os.path.exists(rp):
                print(f"#{n}: No review.md found in {d}")
                continue

            with open(rp, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract title
            title_m = re.search(r'^# (.+)', content, re.MULTILINE)
            title = title_m.group(1).strip() if title_m else d

            has_fig = os.path.exists(os.path.join(base, d, 'figures', 'fig1.png'))

            meta = {
                'title': title,
                'dir': d,
                'has_fig': has_fig,
            }

            html_out = generate_review_html(meta, content, os.path.join(base, d))

            out_path = os.path.join(base, d, 'index.html')
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(html_out)
            count += 1
            print(f"Written: {d}/index.html ({len(html_out)} chars)")

print(f"\nTotal review HTMLs generated: {count}")
