import os, re, html as html_lib

base = r'C:/Users/jehyu/Arbeitplatz/paper-curation/ai4s'

# Category assignments (HTML-escaped)
category_assignments = {
    236: "AI Ethics &amp; Integrity",
    237: "Scientific Discovery &amp; Foundation Models",
    238: "LLM Agents for Science",
    239: "Domain Applications",
    240: "Benchmarks &amp; Evaluation",
    241: "AI Ethics &amp; Integrity",
    242: "Domain Applications",
    243: "LLM Agents for Science",
    244: "Scientific Writing &amp; Peer Review",
    245: "Scientific Knowledge &amp; NLP",
    246: "Scientific Knowledge &amp; NLP",
    247: "Scientific Knowledge &amp; NLP",
    248: "LLM Agents for Science",
    249: "Scientific Writing &amp; Peer Review",
    250: "Other",
}

def extract_meta(num):
    for d in sorted(os.listdir(base)):
        m = re.match(r'^(\d+)_', d)
        if m and int(m.group(1)) == num:
            rp = os.path.join(base, d, 'review.md')
            if not os.path.exists(rp):
                return None
            with open(rp, 'r', encoding='utf-8') as f:
                content = f.read()

            title_m = re.search(r'^# (.+)', content, re.MULTILINE)
            title = title_m.group(1).strip() if title_m else d

            author_m = re.search(r'\*\*저자\*\*:\s*(.+?)(?:\s*\||\n)', content)
            date_m = re.search(r'\*\*날짜\*\*:\s*(.+?)(?:\s*\||\n)', content)
            doi_m = re.search(r'\*\*DOI[^*]*\*\*:\s*(.+?)(?:\n|$)', content)

            authors = author_m.group(1).strip() if author_m else ''
            date_raw = date_m.group(1).strip() if date_m else ''
            doi_raw = doi_m.group(1).strip() if doi_m else ''

            dm = re.search(r'(\d{4})-(\d{2})', date_raw)
            if dm:
                date_fmt = f"{dm.group(1)}.{dm.group(2)}"
            else:
                ym = re.search(r'(\d{4})', date_raw)
                date_fmt = f"{ym.group(1)}.01" if ym else "2024.01"

            essence_m = re.search(r'## Essence[^\n]*\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
            essence = ''
            if essence_m:
                lines = [l.strip() for l in essence_m.group(1).split('\n')
                         if l.strip() and not l.strip().startswith('>') and not l.strip().startswith('#')]
                essence = ' '.join(lines[:3])[:500]

            overall_m = re.search(r'\|\s*Overall\s*\|\s*(\d+)', content)
            novelty_m = re.search(r'\|\s*Novelty\s*\|\s*(\d+)', content)
            technical_m = re.search(r'\|\s*Technical[^|]*\|\s*(\d+)', content)
            significance_m = re.search(r'\|\s*Significance\s*\|\s*(\d+)', content)
            clarity_m = re.search(r'\|\s*Clarity\s*\|\s*(\d+)', content)

            overall = int(overall_m.group(1)) if overall_m else 0
            novelty = int(novelty_m.group(1)) if novelty_m else 0
            technical = int(technical_m.group(1)) if technical_m else 0
            significance = int(significance_m.group(1)) if significance_m else 0
            clarity = int(clarity_m.group(1)) if clarity_m else 0

            verdict_m = re.search(r'\*\*총평\*\*:\s*(.+?)(?=\n\n|\Z)', content, re.DOTALL)
            verdict = verdict_m.group(1).strip()[:600] if verdict_m else ''

            doi_url = ''
            doi_link_m = re.search(r'\[https?://[^\]]+\]\((https?://[^)]+)\)', doi_raw)
            if doi_link_m:
                doi_url = doi_link_m.group(1)
            else:
                doi_url_m = re.search(r'https?://\S+', doi_raw)
                doi_url = doi_url_m.group(0).rstrip(').,') if doi_url_m else ''

            doi_num_m = re.search(r'10\.\d{4,}/\S+', doi_url)
            doi_num = doi_num_m.group(0).rstrip(').,') if doi_num_m else ''

            has_fig = os.path.exists(os.path.join(base, d, 'figures', 'fig1.png'))

            return {
                'num': num, 'dir': d, 'title': title,
                'authors': authors, 'date_fmt': date_fmt,
                'doi_url': doi_url, 'doi_num': doi_num,
                'essence': essence, 'verdict': verdict,
                'overall': overall, 'novelty': novelty,
                'technical': technical, 'significance': significance,
                'clarity': clarity, 'has_fig': has_fig,
                'content': content
            }
    return None


def esc(s):
    return html_lib.escape(str(s))


def make_card(meta, cat, card_num):
    score_val = meta['overall']
    score_disp = f"{score_val}/5" if score_val > 0 else "N/A"
    score_data = score_val if score_val > 0 else 0

    badges = []
    for label, val in [('Novelty', meta['novelty']), ('Technical Soundness', meta['technical']),
                       ('Significance', meta['significance']), ('Clarity', meta['clarity']),
                       ('Overall', meta['overall'])]:
        if val > 0:
            badges.append(f'<span class="score-badge">{label}: {val}</span>')
    badges_html = '<div class="scores">' + ' '.join(badges) + '</div>' if badges else ''

    fig_html = ''
    if meta['has_fig']:
        fig_html = f'          <div class="paper-fig"><img data-src="{meta["dir"]}/figures/fig1.png" alt="Figure" class="lazy"></div>'

    meta_parts = []
    if meta['authors']:
        meta_parts.append(f'<strong>저자</strong>: {esc(meta["authors"])}')
    if meta['date_fmt']:
        meta_parts.append(f'<strong>날짜</strong>: {meta["date_fmt"]}')
    if meta['doi_num']:
        meta_parts.append(f'<strong>DOI</strong>: <a href="{meta["doi_url"]}" target="_blank">{esc(meta["doi_num"])}</a>')
    elif meta['doi_url']:
        meta_parts.append(f'<strong>출처</strong>: <a href="{meta["doi_url"]}" target="_blank">{esc(meta["doi_url"][:60])}</a>')
    meta_line = ' | '.join(meta_parts)

    essence_html = ''
    if meta['essence']:
        essence_html = f"""          <div class="section">
            <div class="section-label">Essence</div>
            <p>{esc(meta["essence"])}</p>
          </div>"""

    verdict_html = ''
    if meta['verdict']:
        verdict_html = f"""          <div class="section">
            <div class="section-label">Evaluation</div>
            {badges_html}
            <p class="verdict">{esc(meta["verdict"])}</p>
          </div>"""
    elif badges_html:
        verdict_html = f"""          <div class="section">
            <div class="section-label">Evaluation</div>
            {badges_html}
          </div>"""

    return f"""        <div class="paper-card" data-date="{meta["date_fmt"]}" data-score="{score_data}" data-topic="{cat}">
          <div class="paper-header">
            <span class="paper-num">#{card_num}</span>
            <span class="paper-date">{meta["date_fmt"]}</span>
            <span class="paper-score">{score_disp}</span>
          </div>
          <h3><a href="{meta["dir"]}/index.html">{esc(meta["title"])}</a></h3>
          <p class="meta">{meta_line}</p>
{fig_html}
{essence_html}
{verdict_html}
        </div>"""


# ── Read existing index.html ────────────────────────────────────────────────
with open(os.path.join(base, 'index.html'), 'r', encoding='utf-8') as f:
    old_html = f.read()

# ── Extract topic groups ────────────────────────────────────────────────────
topic_group_pat = re.compile(
    r'(<div class="topic-group" data-topic="([^"]+)">.*?)(?=<div class="topic-group"|  </div>\s*\n\s*<div class="credit">)',
    re.DOTALL
)

topic_groups_order = []
topic_groups = {}
for m in topic_group_pat.finditer(old_html):
    cat = m.group(2)
    topic_groups[cat] = m.group(1)
    if cat not in topic_groups_order:
        topic_groups_order.append(cat)

print(f"Found {len(topic_groups)} topic groups: {topic_groups_order}")

# ── Extract new paper data ──────────────────────────────────────────────────
new_papers = {}
for n in range(236, 251):
    meta = extract_meta(n)
    if meta:
        new_papers[n] = meta

print(f"Extracted {len(new_papers)} new papers")

# ── Count existing cards per category ──────────────────────────────────────
cat_card_counts = {}
for cat, tg_html in topic_groups.items():
    cards = re.findall(r'<div class="paper-card"', tg_html)
    cat_card_counts[cat] = len(cards)

# ── Inject new cards into topic groups ────────────────────────────────────
for n in sorted(new_papers.keys()):
    meta = new_papers[n]
    cat = category_assignments[n]
    cat_card_counts[cat] = cat_card_counts.get(cat, 0) + 1
    card_num = cat_card_counts[cat]
    card_html = make_card(meta, cat, card_num)

    old_tg = topic_groups.get(cat, '')
    # Insert before the last closing div of topic-body
    insert_pos = old_tg.rfind('\n      </div>')
    if insert_pos == -1:
        insert_pos = len(old_tg)
        old_tg += '\n      </div>'
    new_tg = old_tg[:insert_pos] + '\n' + card_html + '\n      </div>'
    topic_groups[cat] = new_tg

# ── Update topic-count spans ───────────────────────────────────────────────
for cat, tg_html in topic_groups.items():
    cards = re.findall(r'<div class="paper-card"', tg_html)
    count = len(cards)
    new_tg = re.sub(r'(<span class="topic-count">)\d+편(</span>)',
                    rf'\g<1>{count}편\g<2>', tg_html)
    topic_groups[cat] = new_tg

# ── Total paper count ──────────────────────────────────────────────────────
total = sum(len(re.findall(r'<div class="paper-card"', tg)) for tg in topic_groups.values())
print(f"Total cards: {total}")

# ── Rebuild the cards section of index.html ───────────────────────────────
# Find the <div id="cards"> ... </div>  section
cards_start = old_html.find('<div id="cards">')
# Find the closing: </div>\n\n  <div class="credit">
cards_end_pat = re.search(r'\n  </div>\s*\n\n\s*<div class="credit">', old_html)
if not cards_end_pat:
    cards_end_pat = re.search(r'\n  </div>\s*\n\s*<div class="credit">', old_html)
cards_end = cards_end_pat.start() if cards_end_pat else -1

print(f"cards_start={cards_start}, cards_end={cards_end}")

# Build new cards section
new_cards_lines = ['<div id="cards">']
new_cards_lines.append('')
for cat in topic_groups_order:
    new_cards_lines.append(topic_groups[cat])
    new_cards_lines.append('')
new_cards_lines.append('  </div>')

new_cards_html = '\n'.join(new_cards_lines)

# ── Update stat number in hero ────────────────────────────────────────────
new_html = old_html[:cards_start] + new_cards_html + old_html[cards_end + len(cards_end_pat.group(0)):]

# Update total count
new_html = re.sub(r'(<div class="stat-num">)\d+(</div><div class="stat-label">리뷰 완료)',
                  rf'\g<1>{total}\g<2>', new_html)

# Update curation date
new_html = re.sub(r'(<div class="stat-num">)[\d-]+(</div><div class="stat-label">큐레이션 일자)',
                  r'\g<1>2026-03-27\g<2>', new_html)

# Write new index.html
out_path = os.path.join(base, 'index.html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(new_html)
print(f"Written: {out_path} ({len(new_html)} chars)")

# ── Verify ────────────────────────────────────────────────────────────────
with open(out_path, 'r', encoding='utf-8') as f:
    verify = f.read()
total_check = len(re.findall(r'<div class="paper-card"', verify))
print(f"Verification: {total_check} cards in output HTML")
