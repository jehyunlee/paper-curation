"""
review.md에 YAML frontmatter 삽입/업데이트 + Related Papers 섹션 생성.

데이터 소스:
  - _papers_index.json: title, authors, date, journal, doi, arxiv, score, essence, topics, classifications
  - _paper_connections.json: related papers (per topic)
  - Zotero API: PDF 파일 경로

Obsidian 호환:
  - tags: cat/{category}, sub/{sub_category}, topic/{topic}
  - related: [[slug]] wikilinks
  - pdf: Zotero 로컬 PDF 경로

Usage:
  PYTHONUTF8=1 python pipeline/inject_frontmatter.py --topic ai4s
  PYTHONUTF8=1 python pipeline/inject_frontmatter.py --topic scisci
  PYTHONUTF8=1 python pipeline/inject_frontmatter.py --topic ai4s --skip-zotero
"""

import argparse
import json
import os
import re
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

from config_loader import (
    PAPERS_DIR as _PAPERS_DIR, get_topic_dir, _ssl_ctx,
    get_zotero_api_key, get_zotero_user_id, get_zotero_dir,
)

PAPERS_DIR = str(_PAPERS_DIR)

RELATION_ICONS = {
    "alternative": "\U0001F504 다른 접근",
    "extension": "\U0001F517 후속 연구",
    "foundation": "\U0001F3DB 기반 연구",
    "counterpoint": "\u2696\uFE0F 반론/비판",
    "application": "\U0001F9EA 응용 사례",
}


def log(msg):
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


# ═══════════════════════════════════════════
# Zotero PDF path lookup
# ═══════════════════════════════════════════

def fetch_zotero_pdf_map():
    """Zotero API에서 item title → PDF filename 매핑 조회."""
    api_key = get_zotero_api_key()
    user_id = get_zotero_user_id()
    pdf_dir = get_zotero_dir()

    if not api_key or not user_id:
        log("  WARNING: Zotero API key/user ID missing, skipping PDF lookup")
        return {}

    log("  Fetching Zotero items for PDF matching...")
    title_to_pdf = {}
    start = 0
    limit = 100

    while True:
        url = (f"https://api.zotero.org/users/{user_id}/items"
               f"?format=json&itemType=attachment&limit={limit}&start={start}")
        req = urllib.request.Request(url, headers={
            "Zotero-API-Key": api_key, "User-Agent": "Mozilla/5.0",
        })
        try:
            with urllib.request.urlopen(req, timeout=30, context=_ssl_ctx) as resp:
                items = json.load(resp)
                total = resp.headers.get("Total-Results", "0")
        except Exception as e:
            log(f"  WARNING: Zotero API error: {e}")
            break

        for item in items:
            data = item.get("data", {})
            if data.get("contentType") != "application/pdf":
                continue
            # linked_file: path 사용, imported_file: filename 사용
            filepath = data.get("path", "") or data.get("filename", "")
            parent_key = data.get("parentItem", "")
            if filepath and parent_key:
                title_to_pdf[parent_key] = filepath

        start += limit
        if start >= int(total):
            break

    # Now fetch parent items to get title → parent_key mapping
    log(f"  Found {len(title_to_pdf)} PDF attachments, fetching parent titles...")
    slug_to_pdf = {}

    # Fetch all items (not just attachments)
    start = 0
    while True:
        url = (f"https://api.zotero.org/users/{user_id}/items/top"
               f"?format=json&limit={limit}&start={start}")
        req = urllib.request.Request(url, headers={
            "Zotero-API-Key": api_key, "User-Agent": "Mozilla/5.0",
        })
        try:
            with urllib.request.urlopen(req, timeout=30, context=_ssl_ctx) as resp:
                items = json.load(resp)
                total = resp.headers.get("Total-Results", "0")
        except Exception as e:
            log(f"  WARNING: Zotero API error: {e}")
            break

        for item in items:
            data = item.get("data", {})
            key = data.get("key", "")
            title = data.get("title", "")
            if key in title_to_pdf and title:
                pdf_filename = title_to_pdf[key]
                # Normalize title for matching
                norm_title = _normalize_title(title)
                slug_to_pdf[norm_title] = pdf_filename

        start += limit
        if start >= int(total):
            break

    log(f"  Matched {len(slug_to_pdf)} titles to PDFs")
    return slug_to_pdf


def _normalize_title(title):
    """제목 정규화: 소문자, 특수문자 제거, 공백 통일."""
    t = title.lower().strip()
    t = re.sub(r'[^a-z0-9\s]', '', t)
    t = re.sub(r'\s+', ' ', t)
    return t


def find_pdf_path(paper_title, pdf_map, pdf_dir):
    """논문 제목으로 PDF 경로 찾기."""
    if not pdf_map:
        return None
    norm = _normalize_title(paper_title)
    filepath = pdf_map.get(norm)
    if not filepath:
        return None
    # linked_file: path is absolute; imported_file: filename only
    if os.path.isabs(filepath):
        if os.path.exists(filepath):
            return filepath.replace("\\", "/")
    elif pdf_dir:
        full_path = os.path.join(pdf_dir, filepath)
        if os.path.exists(full_path):
            return full_path.replace("\\", "/")
    return None


# ═══════════════════════════════════════════
# Frontmatter injection
# ═══════════════════════════════════════════

def build_frontmatter(paper, connections, pdf_path, topic):
    """논문 데이터에서 YAML frontmatter dict 생성."""
    cls = paper.get("classifications", {}).get(topic, {})
    primary_cat = cls.get("primary_category", "")
    all_cats = cls.get("all_categories", [])
    sub_cat = cls.get("sub_category", "")

    # tags
    tags = []
    for cat in all_cats:
        tags.append(f"cat/{cat.replace(' ', '_').replace('&', 'and')}")
    if sub_cat:
        tags.append(f"sub/{sub_cat.replace(' ', '_').replace('&', 'and')}")
    for t in paper.get("topics", []):
        tags.append(f"topic/{t}")

    slug = paper.get("slug", "")
    num = slug.split("_")[0] if "_" in slug else ""

    fm = {
        "title": slug,
        "authors": paper.get("authors", ""),
        "date": paper.get("date", "") if re.match(r'^\d{4}', str(paper.get("date", ""))) else "",
        "doi": paper.get("doi", ""),
        "arxiv": paper.get("arxiv", ""),
        "score": paper.get("score", 0),
        "essence": paper.get("essence", ""),
        "tags": tags,
    }

    if pdf_path:
        fm["pdf"] = pdf_path

    return fm


def frontmatter_to_yaml(fm):
    """Dict → YAML 문자열 (간단 직렬화, PyYAML 불필요)."""
    lines = ["---"]
    for key, val in fm.items():
        if isinstance(val, list):
            if not val:
                lines.append(f"{key}: []")
            else:
                lines.append(f"{key}:")
                for item in val:
                    lines.append(f'  - "{item}"')
        elif isinstance(val, (int, float)):
            lines.append(f"{key}: {val}")
        elif val is None:
            lines.append(f"{key}: null")
        else:
            # Escape quotes in strings
            escaped = str(val).replace('"', '\\"')
            lines.append(f'{key}: "{escaped}"')
    lines.append("---")
    return "\n".join(lines)


def build_related_section(slug, connections):
    """Related Papers 마크다운 섹션 생성 (outgoing + incoming)."""
    outgoing = connections.get(slug, [])

    # Incoming: 이 논문을 참조하는 다른 논문들
    incoming = []
    for src_slug, conns_list in connections.items():
        if src_slug == slug:
            continue
        for c in conns_list:
            if c.get("slug") == slug:
                incoming.append({
                    "slug": src_slug,
                    "relation": c.get("relation", "alternative"),
                    "reason": c.get("reason", ""),
                })

    if not outgoing and not incoming:
        return ""

    lines = ["\n## Related Papers\n"]

    for c in outgoing:
        rel = c.get("relation", "alternative")
        icon_label = RELATION_ICONS.get(rel, rel)
        reason = c.get("reason", "")
        target = c.get("slug", "")
        lines.append(f"- {icon_label}: [[papers/{target}/review]] — {reason}")

    for c in incoming:
        rel = c.get("relation", "alternative")
        icon_label = RELATION_ICONS.get(rel, rel)
        reason = c.get("reason", "")
        source = c.get("slug", "")
        lines.append(f"- {icon_label}: [[papers/{source}/review]] — {reason}")

    return "\n".join(lines) + "\n"


def inject_into_review(md_path, frontmatter_yaml, related_section):
    """review.md에 frontmatter 삽입/교체 + Related Papers 섹션 추가/교체."""
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 기존 frontmatter + 잔해 제거: 본문은 항상 "# 제목"으로 시작
    h1_match = re.search(r'^# .+', content, re.MULTILINE)
    if h1_match:
        content = content[h1_match.start():]

    # 기존 Related Papers 섹션 제거
    content = re.sub(
        r'\n## Related Papers\n[\s\S]*?(?=\n## |\Z)',
        '', content
    )

    # 조립: frontmatter + 본문 + related
    result = frontmatter_yaml + "\n\n" + content.strip()
    if related_section:
        result += "\n" + related_section

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(result)


def main():
    parser = argparse.ArgumentParser(description="Inject frontmatter into review.md")
    parser.add_argument("--topic", default="ai4s")
    parser.add_argument("--skip-zotero", action="store_true", help="Skip Zotero PDF lookup")
    args = parser.parse_args()

    topic = args.topic
    topic_dir = str(get_topic_dir(topic))

    # Load data
    log(f"Loading {topic} data...")
    with open(os.path.join(PAPERS_DIR, "_papers_index.json"), "r", encoding="utf-8") as f:
        all_papers = json.load(f)

    topic_papers = [p for p in all_papers if topic in p.get("topics", [])]
    log(f"  {len(topic_papers)} papers")

    # Load connections
    conn_path = os.path.join(topic_dir, "_paper_connections.json")
    connections = {}
    if os.path.exists(conn_path):
        with open(conn_path, "r", encoding="utf-8") as f:
            connections = json.load(f)
        log(f"  {len(connections)} paper connections loaded")

    # Zotero PDF lookup
    pdf_map = {}
    pdf_dir = get_zotero_dir()
    if not args.skip_zotero:
        try:
            pdf_map = fetch_zotero_pdf_map()
        except Exception as e:
            log(f"  WARNING: Zotero PDF lookup failed: {e}")

    # Inject frontmatter
    log(f"\nInjecting frontmatter...")
    injected = 0
    skipped = 0
    pdf_found = 0

    for paper in topic_papers:
        slug = paper.get("slug", "")
        md_path = os.path.join(PAPERS_DIR, slug, "review.md")
        if not os.path.exists(md_path):
            skipped += 1
            continue

        # Find PDF
        pdf_path = find_pdf_path(paper.get("title", ""), pdf_map, pdf_dir)
        if pdf_path:
            pdf_found += 1

        # Build frontmatter
        fm = build_frontmatter(paper, connections, pdf_path, topic)
        fm_yaml = frontmatter_to_yaml(fm)

        # Build related section
        related = build_related_section(slug, connections)

        # Inject
        inject_into_review(md_path, fm_yaml, related)
        injected += 1

    log(f"\nDone!")
    log(f"  Injected: {injected}")
    log(f"  Skipped: {skipped}")
    log(f"  PDF linked: {pdf_found}/{injected}")


if __name__ == "__main__":
    main()
