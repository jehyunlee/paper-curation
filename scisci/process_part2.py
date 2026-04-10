
def make_review_md(e, rv):
    """Generate review.md content."""
    slug = e["slug"]
    title = e["title"]
    authors = e["authors"]
    date = e["date"]
    doi = e["doi"]
    arxiv_id = e.get("arxiv_id", "")
    venue = e["venue"]
    mode = rv["mode"]

    doi_str = f"[{doi}](https://doi.org/{doi})" if doi else "N/A"
    arxiv_str = f"[{arxiv_id}](https://arxiv.org/abs/{arxiv_id})" if arxiv_id else "N/A"

    has_fig = (BASE / slug / "figures" / "fig1.png").exists()
    fig_block = "\n![Figure 1](figures/fig1.png)\n*Figure 1: 논문 핵심 결과 또는 방법론 개요*\n" if has_fig else ""

    scores = rv["scores"]
    score_rows = "\n".join(f"| {k} | {v}/5 |" for k, v in scores.items())

    return f"""# {title}

> **저자**: {authors} | **날짜**: {date} | **Journal**: {venue} | **DOI**: {doi_str} | **arXiv**: {arxiv_str}
> **리뷰 모드**: {mode}

---

## Essence

{rv['essence']}
{fig_block}
## Originality (Abstract 기반)

{rv['originality']}

## How (방법론)

{rv['how']}

## Why (중요성)

{rv['why']}

## Limitation

{rv['limitation']}

## Further Study

{rv['further']}

## 평가

| 항목 | 점수 |
|------|------|
{score_rows}

**총평**: {rv['summary']}
"""


def inline_md(text):
    """Convert inline markdown to HTML."""
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*([^*]+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', text)
    return text


def md_to_html_body(md):
    """Convert markdown string to HTML body."""
    lines = md.split('\n')
    out = []
    in_ul = False
    in_ol = False
    in_table = False
    in_blockquote = False
    table_rows = []

    def close_list():
        nonlocal in_ul, in_ol
        if in_ul:
            out.append('</ul>')
            in_ul = False
        if in_ol:
            out.append('</ol>')
            in_ol = False

    def close_table():
        nonlocal in_table, table_rows
        if in_table and table_rows:
            out.append('<table>')
            header = [c.strip() for c in table_rows[0].strip('|').split('|')]
            out.append('<tr>' + ''.join(f'<th>{h}</th>' for h in header) + '</tr>')
            for row in table_rows[2:]:
                cells = [c.strip() for c in row.strip('|').split('|')]
                out.append('<tr>' + ''.join(f'<td>{c}</td>' for c in cells) + '</tr>')
            out.append('</table>')
            table_rows.clear()
            in_table = False

    i = 0
    while i < len(lines):
        line = lines[i]

        # Table
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                close_list()
                in_table = True
            table_rows.append(line)
            i += 1
            continue
        elif in_table:
            close_table()

        # Blockquote
        if line.startswith('> '):
            if not in_blockquote:
                close_list()
                out.append('<blockquote>')
                in_blockquote = True
            content = inline_md(line[2:])
            out.append(f'<p>{content}</p>')
            i += 1
            continue
        elif in_blockquote:
            out.append('</blockquote>')
            in_blockquote = False

        # Headings
        if line.startswith('# '):
            close_list()
            out.append(f'<h1>{inline_md(line[2:])}</h1>')
        elif line.startswith('## '):
            close_list()
            out.append(f'<h2>{inline_md(line[3:])}</h2>')
        elif line.startswith('### '):
            close_list()
            out.append(f'<h3>{inline_md(line[4:])}</h3>')
        elif line.strip() == '---':
            close_list()
            out.append('<hr />')
        elif line.startswith('!['):
            close_list()
            m = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', line)
            if m:
                alt, src = m.group(1), m.group(2)
                out.append(f'<div class="review-fig"><img src="{src}" alt="{alt}"><p class="fig-caption">{alt}</p></div>')
        elif line.startswith('*Figure ') and line.endswith('*'):
            # figure caption - already captured by div above; skip
            pass
        elif line.startswith('- '):
            if not in_ul:
                close_list()
                out.append('<ul>')
                in_ul = True
            out.append(f'<li>{inline_md(line[2:])}</li>')
        elif re.match(r'^\d+\. ', line):
            if not in_ol:
                close_list()
                out.append('<ol>')
                in_ol = True
            content = re.sub(r'^\d+\. ', '', line)
            out.append(f'<li>{inline_md(content)}</li>')
        elif line.strip() == '':
            close_list()
        else:
            close_list()
            if line.strip():
                out.append(f'<p>{inline_md(line)}</p>')

        i += 1

    close_list()
    close_table()
    if in_blockquote:
        out.append('</blockquote>')

    return '\n'.join(out)


def make_index_html(e, rv):
    """Generate styled index.html."""
    title = e["title"]
    md = make_review_md(e, rv)
    body_html = md_to_html_body(md)

    # Wrap sections
    sections = re.split(r'(?=<h2>)', body_html)
    wrapped = []
    for sec in sections:
        if not sec.strip():
            continue
        if sec.startswith('<h1>') or sec.startswith('<blockquote>') or sec.startswith('<hr'):
            wrapped.append(sec)
        elif sec.startswith('<h2>Essence'):
            wrapped.append(f'<div class="section-box essence-box">{sec}</div>')
        elif sec.startswith('<h2>'):
            wrapped.append(f'<div class="section-box">{sec}</div>')
        else:
            wrapped.append(sec)

    final_body = '\n'.join(wrapped)

    scores = rv["scores"]
    badges = ''.join(f'<span class="eval-badge">{k}: {v}/5</span>' for k, v in scores.items())
    final_body = final_body.replace(
        '<h2>평가</h2>',
        f'<h2>평가</h2><div class="eval-badges">{badges}</div>'
    )

    css = """* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'KoPub Dotum', 'KoPubDotumMedium', -apple-system, 'Noto Sans KR', sans-serif; max-width: 820px; margin: 0 auto; padding: 2rem 1.5rem; line-height: 1.7; color: #333; background: #f0f2f5; }
h1 { font-size: 1.4rem; color: #1a1a2e; border-bottom: 3px solid #2374D6; padding-bottom: 0.5rem; margin-bottom: 1rem; }
h2 { font-size: 1.1rem; color: #2374D6; margin: 0 0 0.6rem; padding: 0; border: none; }
h3 { font-size: 1rem; color: #333; margin: 0.8rem 0 0.4rem; }
p { margin: 0.4rem 0; }
blockquote { border-left: 4px solid #2374D6; margin: 0.8rem 0; padding: 0.6rem 1rem; background: #f0f4f8; border-radius: 0 8px 8px 0; font-size: 0.88rem; color: #555; }
ul, ol { margin: 0.4rem 0 0.4rem 1.5rem; }
li { margin: 0.2rem 0; font-size: 0.93rem; }
.section-box { background: white; border-radius: 12px; padding: 1.2rem 1.5rem; margin-bottom: 1rem; box-shadow: 0 1px 4px rgba(0,0,0,0.06); }
table { border-collapse: collapse; margin: 0.5rem 0; font-size: 0.85rem; display: none; }
th, td { border: 1px solid #e0e0e0; padding: 4px 10px; text-align: left; }
th { background: #2374D6; color: white; font-weight: 600; font-size: 0.82rem; }
tr:nth-child(even) { background: #f8f9fa; }
td:last-child { text-align: center; font-weight: 600; color: #2374D6; }
.eval-badges { display: flex; flex-wrap: wrap; gap: 0.4rem; margin: 0.6rem 0; }
.eval-badge { background: #EEF4FD; color: #1A5CA8; padding: 0.2rem 0.7rem; border-radius: 14px; font-size: 0.8rem; font-weight: 600; }
.essence-box { border: 2px solid #1A5CA8; border-radius: 10px; padding: 1rem 1.2rem; margin: 0.8rem 0; background: #F5F8FE; }
.essence-box h2 { color: #1A5CA8; margin: 0 0 0.5rem; border: none; padding: 0; }
code { background: #e8edf3; padding: 0.15rem 0.4rem; border-radius: 4px; font-size: 0.85rem; }
pre { background: #1a1a2e; color: #e0e0e0; padding: 1rem; border-radius: 8px; overflow-x: auto; margin: 0.8rem 0; }
pre code { background: none; color: inherit; }
img { max-width: min(100%, 700px); border: 1px solid #e8e8e8; border-radius: 8px; margin: 0.8rem auto; display: block; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
img + em, p > em:only-child { font-size: 0.85rem; color: #888; display: block; text-align: center; }
em { font-style: italic; }
hr { border: none; border-top: 1px solid #e0e0e0; margin: 0.5rem 0; }
strong { color: #1a1a2e; }
a { color: #1A5CA8; }
.back { margin-top: 1.5rem; padding: 0.8rem 0; border-top: 2px solid #e0e0e0; }
.back a { font-weight: 600; text-decoration: none; }
.back a:hover { text-decoration: underline; }
.review-fig { text-align: center; margin: 1.5rem 0; padding: 1rem; background: #f8f9fa; border-radius: 12px; }
.review-fig img { max-width: min(100%, 700px); border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
.fig-caption { font-size: 0.85rem; color: #888; margin-top: 0.5rem; font-style: italic; }"""

    mathjax_init = r"window.MathJax={tex:{inlineMath:[['$','$'],['\\(','\\)']],displayMath:[['$$','$$'],['\\[','\\]']]}};"

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/font-kopub/1.0/kopubdotum.css">
<script>{mathjax_init}</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>
<style>
{css}
</style>
</head>
<body>
{final_body}
<div class="back"><a href="../../scisci/index.html">&larr; 목록으로 돌아가기</a></div>
</body>
</html>
"""


# ── Main processing ──
print("Starting figure extraction...")
fig_results = {}
for e in ENTRIES:
    slug = e["slug"]
    num = e["num"]
    fig_dir = BASE / slug / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)

    if e["has_pdf"]:
        ok = extract_fig1(e["pdf_path"], str(fig_dir))
        fig_results[num] = "extracted" if ok else "failed"
        status = "OK" if ok else "FAILED"
    else:
        fig_results[num] = "no_pdf"
        status = "no PDF"
    print(f"  [{num}] {slug[:45]} -> {status}")

print("\nGenerating review.md and index.html files...")
for e in ENTRIES:
    num = e["num"]
    slug = e["slug"]
    rv = REVIEWS.get(num)
    if not rv:
        print(f"  [{num}] NO REVIEW DATA - skipping")
        continue

    paper_dir = BASE / slug
    paper_dir.mkdir(parents=True, exist_ok=True)

    review_content = make_review_md(e, rv)
    (paper_dir / "review.md").write_text(review_content, encoding="utf-8")

    html_content = make_index_html(e, rv)
    (paper_dir / "index.html").write_text(html_content, encoding="utf-8")

    print(f"  [{num}] {slug[:45]} -> written")

print("\nAll done!")
