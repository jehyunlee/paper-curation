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

# ─────────────────────────────────────────────────────────────────────────────
# Schema v1 frontmatter (Phase 3)
#
# - `title` is the real paper title (was a bug: slug got stored).
# - `primary_category`, `all_categories`, `sub_categories` are first-class
#   fields so build_papers_index / build_topic_index can read them without
#   re-parsing classifications from _papers_index.json.
# - `scores` is a nested dict (novelty/technical/significance/clarity/overall)
#   for Obsidian Bases + Dataview queries.
# - `tags` are nested in the form `topic/category-slug/sub-slug` so Obsidian's
#   tag tree groups them automatically.
# - `schema_version: v1` lets future migrations check shape.
# ─────────────────────────────────────────────────────────────────────────────

SCHEMA_VERSION = "v1"


def _slugify_tag(s):
    """Lowercase, replace spaces/&/punctuation with single dashes."""
    s = re.sub(r"[&]+", "and", s.lower())
    s = re.sub(r"[^a-z0-9가-힣]+", "-", s)
    return s.strip("-")


def _read_review_body_signals(md_path):
    """Best-effort extract scores + essence from existing review.md body
    (for use during migration when _papers_index.json is missing values).

    Returns dict with whichever fields could be parsed; keys absent when
    not found.
    """
    if not os.path.exists(md_path):
        return {}
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    # Strip any existing frontmatter so regex doesn't pick up frontmatter strings
    if content.startswith("---"):
        end = content.find("\n---", 3)
        if end != -1:
            content = content[end + 4:]
    out = {}
    # Scores: "- Novelty: 4/5"
    for label, key in [("Novelty", "novelty"), ("Technical Soundness", "technical"),
                       ("Significance", "significance"), ("Clarity", "clarity"),
                       ("Overall", "overall")]:
        m = re.search(rf"{label}\D*(\d+(?:\.\d+)?)\s*/\s*5", content)
        if m:
            out[key] = float(m.group(1))
    # Essence: first non-figure line under "## Essence"
    m = re.search(r"##\s*Essence\s*\n(.+?)(?=\n##|\Z)", content, re.DOTALL)
    if m:
        lines = [ln.strip() for ln in m.group(1).splitlines()
                 if ln.strip() and not ln.strip().startswith(("![","*"))]
        if lines:
            out["essence"] = " ".join(lines)[:500]
    return out


def build_frontmatter(paper, connections, pdf_path, topic):
    """Build schema v1 frontmatter dict from index entry + body signals.

    Multi-topic papers: classifications come from ``primary_topic``
    (fallback to the ``topic`` arg) so the frontmatter is stable
    regardless of which topic last ran inject_frontmatter. Nested tags
    are emitted for EVERY topic the paper belongs to, so Obsidian's tag
    tree shows it under each.

    Body signals are read as fallback when the index lacks scores
    (older entries). Once tool-use migration is run, scores will always
    come from the index, but the fallback keeps migration of legacy
    review.md files lossless.
    """
    slug = paper.get("slug", "")
    md_path = os.path.join(PAPERS_DIR, slug, "review.md")
    body_signals = _read_review_body_signals(md_path)

    # primary_topic is what determines the canonical classification
    primary_topic = paper.get("primary_topic") or topic
    cls = (paper.get("classifications", {}).get(primary_topic)
            or paper.get("classifications", {}).get(topic, {}))
    primary_cat = cls.get("primary_category", "")
    all_cats = cls.get("all_categories", []) or ([primary_cat] if primary_cat else [])
    sub_cat = cls.get("sub_category", "")
    sub_categories = cls.get("sub_categories", {}) or (
        {primary_cat: sub_cat} if primary_cat and sub_cat else {}
    )

    # Nested tags: emit for every topic the paper belongs to.
    # Format: `paper`, `{topic}`, `{topic}/cat-slug/sub-slug`
    paper_topics = paper.get("topics", []) or [primary_topic]
    tags = ["paper"]
    for t in paper_topics:
        tags.append(t)
        # Use that topic's own classifications when available; fall back
        # to primary_topic's classifications.
        t_cls = paper.get("classifications", {}).get(t) or cls
        t_all_cats = t_cls.get("all_categories", []) or (
            [t_cls.get("primary_category", "")] if t_cls.get("primary_category") else []
        )
        t_sub_cats = t_cls.get("sub_categories", {}) or {}
        for cat in t_all_cats:
            if not cat:
                continue
            cat_slug = _slugify_tag(cat)
            sub_for_cat = t_sub_cats.get(cat, "")
            if sub_for_cat:
                tags.append(f"{t}/{cat_slug}/{_slugify_tag(sub_for_cat)}")
            else:
                tags.append(f"{t}/{cat_slug}")
    # Dedup preserving order
    seen = set(); tags = [x for x in tags if not (x in seen or seen.add(x))]

    # Scores: prefer index (if scores object present), fall back to body signals
    idx_scores = paper.get("scores") or {}
    scores = {
        "novelty":      idx_scores.get("novelty",      body_signals.get("novelty",      0)),
        "technical":    idx_scores.get("technical",    body_signals.get("technical",    0)),
        "significance": idx_scores.get("significance", body_signals.get("significance", 0)),
        "clarity":      idx_scores.get("clarity",      body_signals.get("clarity",      0)),
        "overall":      idx_scores.get("overall",      body_signals.get("overall",
                                                      paper.get("score", 0))),
    }

    title = paper.get("title", "") or slug
    essence = paper.get("essence", "") or body_signals.get("essence", "")

    fm = {
        "title": title,
        "authors": paper.get("authors", []),
        "date": paper.get("date", "") if re.match(r"^\d{4}", str(paper.get("date", ""))) else "",
        "doi": paper.get("doi", ""),
        "arxiv": paper.get("arxiv", ""),
        "journal": paper.get("journal", ""),
        "primary_topic": paper.get("primary_topic", topic),
        "primary_category": primary_cat,
        "all_categories": all_cats,
        "sub_categories": sub_categories,
        "sub_category": sub_cat,
        "scores": scores,
        "score": scores["overall"],
        "essence": essence,
        "tags": tags,
        "schema_version": SCHEMA_VERSION,
        "review_date": paper.get("review_date", ""),
    }

    if pdf_path:
        fm["pdf"] = pdf_path

    return fm


def _yaml_str(s):
    """Quote a string for safe YAML emission (double-quoted, escapes)."""
    escaped = str(s).replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
    return f'"{escaped}"'


def _yaml_value(val, indent=0):
    """Serialise a single scalar/list/dict value. Returns list of lines."""
    pad = "  " * indent
    if val is None:
        return [f"{pad}null"]
    if isinstance(val, bool):
        return [f"{pad}{'true' if val else 'false'}"]
    if isinstance(val, (int, float)):
        return [f"{pad}{val}"]
    if isinstance(val, list):
        if not val:
            return [f"{pad}[]"]
        out = []
        for item in val:
            if isinstance(item, (dict, list)):
                sub = _yaml_value(item, indent + 1)
                if not sub:
                    out.append(f"{pad}-")
                else:
                    out.append(f"{pad}- {sub[0].lstrip()}")
                    out.extend(sub[1:])
            else:
                out.append(f"{pad}- {_yaml_str(item) if isinstance(item, str) else item}")
        return out
    if isinstance(val, dict):
        if not val:
            return [f"{pad}{{}}"]
        out = []
        for k, v in val.items():
            key = _yaml_str(k) if (not isinstance(k, str) or
                                    re.search(r"[\s:&'\"]", str(k))) else str(k)
            if isinstance(v, (dict, list)):
                sub = _yaml_value(v, indent + 1)
                out.append(f"{pad}{key}:")
                out.extend(sub)
            else:
                scalar = _yaml_value(v, 0)[0]
                out.append(f"{pad}{key}: {scalar.lstrip()}")
        return out
    return [f"{pad}{_yaml_str(val)}"]


def frontmatter_to_yaml(fm):
    """Dict → YAML string. Supports nested dicts/lists (used for
    ``sub_categories`` and ``scores``)."""
    lines = ["---"]
    for key, val in fm.items():
        if isinstance(val, (dict, list)):
            if val:
                lines.append(f"{key}:")
                lines.extend(_yaml_value(val, 1))
            elif isinstance(val, list):
                lines.append(f"{key}: []")
            else:
                lines.append(f"{key}: {{}}")
        elif isinstance(val, (int, float)):
            lines.append(f"{key}: {val}")
        elif val is None:
            lines.append(f"{key}: null")
        else:
            lines.append(f"{key}: {_yaml_str(val)}")
    lines.append("---")
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────────────────────
# Public parse helper — used by build_papers_index, build_topic_index,
# validate_papers etc. to read frontmatter without re-implementing YAML.
# ─────────────────────────────────────────────────────────────────────────────

_FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(md_text):
    """Return (frontmatter_dict, body_text). frontmatter_dict is {} when
    no frontmatter is present.

    Uses a minimal YAML reader that handles the shapes
    ``frontmatter_to_yaml`` emits: scalars, single-line arrays ``[]``,
    bulleted lists, nested dicts (one level). Imports PyYAML when
    available for full compliance; otherwise falls back to the minimal
    reader.
    """
    m = _FM_RE.match(md_text)
    if not m:
        return {}, md_text
    fm_block = m.group(1)
    body = md_text[m.end():]

    try:
        import yaml  # type: ignore
        return yaml.safe_load(fm_block) or {}, body
    except ImportError:
        pass

    # Minimal fallback parser ----------------------------------------------
    out = {}
    cur_key = None
    cur_list = None
    cur_dict = None
    for raw in fm_block.splitlines():
        if not raw.strip():
            continue
        # nested dict line (sub_categories key)
        if cur_dict is not None and raw.startswith("  ") and ":" in raw and not raw.strip().startswith("-"):
            k, _, v = raw.strip().partition(":")
            cur_dict[k.strip().strip('"')] = v.strip().strip('"')
            continue
        # list item
        if raw.startswith("  - ") or raw.startswith("- "):
            item = raw.strip()[2:].strip().strip('"')
            if cur_list is not None:
                cur_list.append(item)
            continue
        # top-level key
        if raw.startswith(("  ", "\t")) and cur_key:
            continue  # unhandled nested scalar
        if ":" in raw:
            k, _, v = raw.partition(":")
            k = k.strip()
            v = v.strip()
            cur_dict = None
            cur_list = None
            cur_key = k
            if v == "":
                # could be a list or dict; peek next nonblank line later
                out[k] = []
                cur_list = out[k]
                # If next line starts with two-space + non-dash, switch to dict
            elif v == "[]":
                out[k] = []
            elif v == "{}":
                out[k] = {}
            elif v in ("null", "~"):
                out[k] = None
            else:
                # scalar
                if v.startswith('"') and v.endswith('"'):
                    out[k] = v[1:-1].replace('\\"', '"').replace("\\n", "\n")
                else:
                    try:
                        out[k] = int(v)
                    except ValueError:
                        try:
                            out[k] = float(v)
                        except ValueError:
                            out[k] = v
    # Repair: any list left empty might really be a dict; can't tell
    # without lookahead. Acceptable for fallback path; PyYAML is the
    # recommended runtime.
    return out, body


def build_related_section(slug, connections):
    """Related Papers 마크다운 섹션 생성.

    ``connections`` (_paper_connections.json) is already the bidirectional +
    per-target-deduped view (see lib/connections.py), so we render this paper's
    edge list directly — NO incoming scan (that would double every link now that
    each A→B edge already implies B→A). One bullet per related paper; when a paper
    is connected for several reasons each reason is listed as an indented
    sub-bullet with its own relation icon, so all reasons read equally.
    """
    outgoing = connections.get(slug, [])
    if not outgoing:
        return ""

    rel_order = {"foundation": 0, "alternative": 1, "extension": 2,
                 "application": 3, "counterpoint": 4}
    # Defensive dedup by target slug (data layer already collapses these).
    by_slug = {}
    order = []
    for c in outgoing:
        t = c.get("slug", "")
        if t not in by_slug:
            by_slug[t] = c
            order.append(t)
    items = [by_slug[t] for t in order]
    items.sort(key=lambda c: rel_order.get(c.get("relation", ""), 9))

    lines = ["\n## Related Papers\n"]
    for c in items:
        target = c.get("slug", "")
        reasons = c.get("reasons") or [{"relation": c.get("relation", "alternative"),
                                        "reason": c.get("reason", "")}]
        primary = reasons[0]
        p_icon = RELATION_ICONS.get(primary.get("relation", "alternative"),
                                    primary.get("relation", ""))
        lines.append(f"- {p_icon}: [[papers/{target}/review]] — {primary.get('reason', '')}")
        for r in reasons[1:]:
            icon = RELATION_ICONS.get(r.get("relation", "alternative"),
                                      r.get("relation", ""))
            lines.append(f"    - {icon}: {r.get('reason', '')}")

    return "\n".join(lines) + "\n"


def _rebuild_title_header(frontmatter_yaml):
    """H1 이 유실된 review.md 용 제목 헤더 복원 (run_update_force.REVIEW_TEMPLATE 와 동일 형식)."""
    def field(name):
        m = re.search(r'(?m)^%s:\s*(.+)$' % name, frontmatter_yaml)
        return m.group(1).strip().strip('"').strip("'") if m else ""

    title = field("title")
    date = field("date")
    doi = field("doi")
    am = re.search(r'(?m)^authors:\n((?:\s+-\s.*\n)+)', frontmatter_yaml)
    authors = ", ".join(
        re.sub(r'^\s*-\s*', '', ln).strip().strip('"').strip("'")
        for ln in am.group(1).splitlines()) if am else ""
    if doi and doi.upper() not in {"N/A", "미제공", "NONE"}:
        ref = f"**DOI**: [{doi}](https://doi.org/{doi})"
    else:
        url = field("url")
        ref = f"**URL**: [{url}]({url})" if url else "**DOI**: N/A"
    return f"# {title}\n\n> **저자**: {authors} | **날짜**: {date} | {ref}\n\n---\n\n"


def inject_into_review(md_path, frontmatter_yaml, related_section):
    """review.md에 frontmatter 삽입/교체 + Related Papers 섹션 추가/교체."""
    with open(md_path, "r", encoding="utf-8") as f:
        original = f.read()
        content = original

    # 기존 frontmatter + 잔해 제거: 본문은 항상 "# 제목"으로 시작한다.
    # H1 이 유실된 파일(예: 과거 salvage 산출물)을 그대로 두면 frontmatter 가
    # 중복 삽입되고, review_to_html 이 제목을 slug 경로로 대체해 버린다.
    h1_match = re.search(r'^# .+', content, re.MULTILINE)
    if h1_match:
        content = content[h1_match.start():]
    else:
        body = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL).lstrip("\n")
        content = _rebuild_title_header(frontmatter_yaml) + body

    # 기존 Related Papers 섹션 제거
    content = re.sub(
        r'\n## Related Papers\n[\s\S]*?(?=\n## |\Z)',
        '', content
    )

    # 조립: frontmatter + 본문 + related
    result = frontmatter_yaml + "\n\n" + content.strip()
    if related_section:
        result += "\n" + related_section
    if result == original:
        return False
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(result)
    return True


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
