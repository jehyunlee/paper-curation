"""
빌드 후 검증 스크립트.

4가지 완결성 체크:
  1. 문장 완결 — 빈 섹션, 닫히지 않은 bold 감지
  2. 링크 완결 — 깨진 DOI, 마크다운 링크 감지
  3. 그림 완결 — review.md의 그림 참조가 실제 파일과 일치하는지
  4. Python 리스트 리터럴 — ['a', 'b'] 형태가 그대로 남아있는지

Usage:
  PYTHONUTF8=1 python pipeline/validate_papers.py --topic ai4s
  PYTHONUTF8=1 python pipeline/validate_papers.py --topic ai4s --fix  # 자동 수정
"""

import argparse
import hashlib
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

from config_loader import PAPERS_DIR as _PAPERS_DIR, DOCS_DIR, get_topic_dir
PAPERS_DIR = str(_PAPERS_DIR)

try:
    from lib.categories import category_slug, CATEGORIES_BY_TOPIC
except Exception:
    category_slug = None
    CATEGORIES_BY_TOPIC = {}


def log(msg):
    print(msg, flush=True)


# ── 1. 문장 완결 체크 ──

def check_title_header(review_path):
    """review.md 본문에 H1 제목이 있는지 검사.

    H1 이 없으면 review_to_html 이 제목을 slug 디렉터리(절대경로)로 대체해
    <title>/<h1>/og:title 에 로컬 경로가 노출된다. 복구는
    `python pipeline/fix_review_headers.py --execute`.
    """
    with open(review_path, "r", encoding="utf-8") as f:
        content = f.read()
    body = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
    if re.search(r'^#\s+\S', body, re.MULTILINE):
        return []
    return ["  NO_TITLE_HEADER: 본문에 '# 제목' 없음 → HTML 제목이 경로로 대체됨"
            " (fix_review_headers.py --execute)"]


def check_truncated_sections(review_path):
    """섹션 본문이 확실히 잘린 경우만 감지 (보수적).

    한국어 문장 끝은 매우 다양하므로, 확실한 경우만:
    1. 닫히지 않은 마크다운 bold (**가 홀수 개)
    2. 본문 섹션이 비어있음 (## 제목만 있고 내용 없음)
    3. 본문이 극히 짧음 (50자 미만, Evaluation 제외)
    """
    issues = []
    with open(review_path, "r", encoding="utf-8") as f:
        content = f.read()

    sections = re.split(r'^## ', content, flags=re.MULTILINE)
    for sec in sections[1:]:
        lines = sec.strip().split("\n")
        sec_name = lines[0].strip()
        if sec_name in ("Evaluation",):
            continue
        body_lines = [l.strip() for l in lines[1:] if l.strip()
                      and not l.strip().startswith("#")
                      and not l.strip().startswith("![")
                      and not l.strip().startswith("*Figure")
                      and not l.strip().startswith(">")]

        # Empty section
        if not body_lines:
            issues.append(f"  EMPTY_SECTION [{sec_name}]")
            continue

        # Very short section body
        body_text = " ".join(body_lines)
        if len(body_text) < 50:
            issues.append(f"  SHORT_SECTION [{sec_name}]: {len(body_text)} chars")

        # Unclosed bold: odd number of ** in last line
        last_line = body_lines[-1]
        if last_line.count("**") % 2 != 0:
            issues.append(f"  UNCLOSED_BOLD [{sec_name}]: ...{last_line[-60:]}")

    return issues


# ── 2. 링크 완결 체크 ──

def check_broken_links(review_path, slug):
    """깨진 마크다운 링크, 빈 DOI, 불완전한 URL 감지."""
    issues = []
    with open(review_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Empty DOI link: [](https://doi.org/) or [](https://doi.org)
    if re.search(r'\[]\(https://doi\.org/?\)', content):
        issues.append("  EMPTY_DOI: empty DOI link")

    # Broken markdown links: [text]() or [text](  )
    for m in re.finditer(r'\[([^\]]+)\]\((\s*)\)', content):
        issues.append(f"  EMPTY_LINK: [{m.group(1)}]()")

    # Incomplete URLs (http without domain)
    for m in re.finditer(r'\]\((https?://)\)', content):
        issues.append(f"  INCOMPLETE_URL: {m.group(1)}")

    # DOI link with DOI in text AND href (double-encoding check)
    if re.search(r'https://doi\.org/\[', content):
        issues.append("  DOUBLE_DOI: DOI double-encoded")

    return issues


# ── 3. 그림 완결 체크 + 자동 수정 ──

def check_figure_refs(review_path, slug, fix=False):
    """review.md의 그림 참조가 실제 파일과 일치하는지 확인.

    감지 대상:
      - 외부 image URL (`![](http(s)://...)`) — LLM 환각 / legacy prompt 잔재
      - 로컬 path 깨짐 (`figures/figN.png` 인데 webp만 있는 경우 등)
      - 없는 figure 참조 (`MISSING_FIG`)
    """
    issues = []
    slug_dir = os.path.join(PAPERS_DIR, slug)
    fig_dir = os.path.join(slug_dir, "figures")

    with open(review_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Build map of actual figure files
    actual_figs = {}
    fig_map = {}
    if os.path.isdir(fig_dir):
        for fname in sorted(os.listdir(fig_dir)):
            if re.match(r'fig\d+\.(png|webp)', fname):
                actual_figs[fname] = True
                m = re.match(r'fig(\d+)\.(png|webp)', fname)
                if m:
                    fig_map[int(m.group(1))] = f"figures/{fname}"

    changed = False
    new_content = content

    # ── External image URL detection (LLM hallucination / legacy prompt) ──
    ext_refs = list(re.finditer(r'!\[([^\]]*)\]\((https?://[^)]+)\)', new_content))
    for m in ext_refs:
        alt = m.group(1)
        url = m.group(2)
        issues.append(f"  EXTERNAL_FIG_URL: ![{alt[:40]}]({url[:60]})")

    if fix and ext_refs and fig_map:
        sorted_keys = sorted(fig_map.keys())
        seq_state = {"next": sorted_keys[0]}

        def replace_external_image(mm):
            alt = mm.group(1)
            target = None
            num_m = re.search(r'(?:Figure|Fig\.?|그림)\s*(\d+)', alt, re.IGNORECASE)
            if num_m:
                n = int(num_m.group(1))
                if n in fig_map:
                    target = fig_map[n]
            if target is None:
                for k in sorted_keys:
                    if k >= seq_state["next"]:
                        target = fig_map[k]
                        seq_state["next"] = k + 1
                        break
            if target is None:
                return mm.group(0)
            return f"![{alt}]({target})"

        replaced = re.sub(
            r'!\[([^\]]*)\]\((https?://[^)]+)\)',
            replace_external_image,
            new_content,
        )
        if replaced != new_content:
            new_content = replaced
            changed = True

    # ── Existing local-path checks ──
    refs = list(re.finditer(r'!\[([^\]]*)\]\((figures/[^)]+)\)', new_content))
    for m in refs:
        ref_path = m.group(2)
        full_path = os.path.join(slug_dir, ref_path)
        if os.path.exists(full_path):
            continue

        fig_name = os.path.basename(ref_path)
        num_match = re.search(r'fig(\d+)', fig_name)
        if not num_match:
            issues.append(f"  BROKEN_FIG: {ref_path} (no number found)")
            continue

        fig_num = num_match.group(1)
        candidates = [f for f in actual_figs if f.startswith(f"fig{fig_num}.")]
        if candidates:
            correct_path = f"figures/{candidates[0]}"
            issues.append(f"  FIG_MISMATCH: {ref_path} -> {correct_path}")
            if fix:
                new_content = new_content.replace(f"({ref_path})", f"({correct_path})")
                changed = True
        else:
            issues.append(f"  MISSING_FIG: {ref_path} (no file found)")

    if fix and changed:
        with open(review_path, "w", encoding="utf-8") as f:
            f.write(new_content)

    return issues, changed


# ── 4. Python 리스트 리터럴 잔류 체크 + 자동 수정 ──

def check_python_list_literals(review_path, fix=False):
    """review.md에 Python 리스트 리터럴 ['a', 'b'] 가 남아있는 경우 감지/수정."""
    issues = []
    with open(review_path, "r", encoding="utf-8") as f:
        content = f.read()

    if "['" not in content and '["' not in content:
        return issues, False

    lines = content.split("\n")
    new_lines = []
    changed = False
    for line in lines:
        s = line.strip()
        if (s.startswith("[") and s.endswith("]") and
                ("'" in s or '"' in s) and len(s) > 20):
            inner = s[1:-1]
            items = re.split(r"""['"]?\s*,\s*['"]""", inner)
            if len(items) > 1:
                issues.append(f"  PYTHON_LIST: {s[:60]}...")
                if fix:
                    for item in items:
                        clean = item.strip().strip("'\"")
                        if clean:
                            new_lines.append(f"- {clean}")
                    changed = True
                    continue
        new_lines.append(line)

    if fix and changed:
        with open(review_path, "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines))

    return issues, changed


# ── Main ──

# ── 5. Category ↔ timeline PNG mismatch (physical-ai 사건 재발 방지) ──

def check_timeline_mismatch(topic):
    """{topic}/index.html/_new_classification.json의 카테고리 목록과 실제 존재하는
    category_timeline_*.png 파일명을 비교. 둘 중 한쪽에만 있으면 경고.

    - 분류에 있는데 이미지 없음 → timeline 재생성 필요
    - 이미지가 있는데 분류에 없음 → stale PNG (cleanup 대상)
    """
    issues = []
    topic_dir = Path(get_topic_dir(topic))
    cls_path = topic_dir / "_new_classification.json"
    if not cls_path.exists():
        return issues  # 토픽 구조 부재 시 스킵

    cls = json.loads(cls_path.read_text(encoding="utf-8"))
    raw = cls.get("categories", []) if isinstance(cls, dict) else cls
    categories = []
    if isinstance(raw, dict):
        categories = list(raw.keys())
    elif isinstance(raw, list):
        for item in raw:
            if isinstance(item, dict) and "name" in item:
                categories.append(item["name"])
            elif isinstance(item, str):
                categories.append(item)

    if not categories or category_slug is None:
        return issues

    expected_slugs = {category_slug(c) for c in categories}
    # Check both png and webp (deploy-stage webp)
    actual_slugs = set()
    for p in topic_dir.iterdir():
        m = re.match(r"category_timeline_(.+)\.(png|webp)$", p.name)
        if m:
            actual_slugs.add(m.group(1))

    missing_images = expected_slugs - actual_slugs
    stale_images = actual_slugs - expected_slugs
    for slug in sorted(missing_images):
        issues.append(f"  [timeline] MISSING image for category slug: {slug}")
    for slug in sorted(stale_images):
        issues.append(f"  [timeline] STALE image (no matching category): {slug}")
    return issues


# ── 5b. Classifications schema + 카테고리 화이트리스트 ──

def check_classifications_schema(topic):
    """`_papers_index.json`의 `classifications[topic]` schema를 점검.

    Required:
      * primary_category : str (non-empty)
      * all_categories   : list[str] (1~3 entries)
      * sub_category     : str (optional but recommended)

    화이트리스트: primary/all categories 가 `_new_classification.json` 의 카테고리
    집합에 모두 속해야 한다.
    """
    issues = []
    idx_path = Path(PAPERS_DIR) / "_papers_index.json"
    cls_path = Path(get_topic_dir(topic)) / "_new_classification.json"
    if not idx_path.exists() or not cls_path.exists():
        return issues
    idx = json.loads(idx_path.read_text(encoding="utf-8"))
    cls = json.loads(cls_path.read_text(encoding="utf-8"))
    valid_cats = {c.get("name") for c in cls.get("categories", [])
                  if isinstance(c, dict)}
    bad_schema = 0
    bad_cat_refs = []
    for p in idx:
        if topic not in p.get("topics", []):
            continue
        c = p.get("classifications", {}).get(topic)
        if not isinstance(c, dict):
            bad_schema += 1
            continue
        if not c.get("primary_category"):
            bad_schema += 1
            continue
        if not isinstance(c.get("all_categories"), list) or not c["all_categories"]:
            bad_schema += 1
            continue
        # Whitelist
        bad = [cat for cat in [c["primary_category"]] + list(c["all_categories"])
               if valid_cats and cat not in valid_cats]
        if bad:
            bad_cat_refs.append((p.get("slug", "?"), bad))
    if bad_schema:
        issues.append(f"  [schema] {bad_schema} papers have malformed classifications[{topic}]")
    for slug, bad in bad_cat_refs[:5]:
        issues.append(f"  [whitelist] {slug[:55]}: unknown category(s) {bad}")
    if len(bad_cat_refs) > 5:
        issues.append(f"  [whitelist] ... +{len(bad_cat_refs)-5} more papers with unknown categories")
    return issues


# ── 5c. DOI 교차검증 게이트 ──

def check_doi_cross_validation(topic):
    """index.doi 와 review.md 본문에 등장하는 DOI 가 일치하는지 표본 검증.

    review.md 의 markdown 링크 또는 'doi:' 표기에서 DOI 추출 → index.doi 와 비교.
    review가 다른 PDF 로부터 생성됐을 때 강한 불일치 신호.
    """
    issues = []
    idx_path = Path(PAPERS_DIR) / "_papers_index.json"
    if not idx_path.exists():
        return issues
    idx = json.loads(idx_path.read_text(encoding="utf-8"))
    doi_re = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE)
    mismatches = []
    no_doi_in_review = 0
    for p in idx:
        if topic not in p.get("topics", []):
            continue
        idx_doi = (p.get("doi") or "").strip().lower()
        # Normalize: strip URL prefix
        for pref in ("https://doi.org/", "http://doi.org/", "doi:"):
            if idx_doi.startswith(pref):
                idx_doi = idx_doi[len(pref):].strip()
        if not idx_doi:
            continue  # nothing to compare
        review_path = Path(PAPERS_DIR) / p.get("slug", "") / "review.md"
        if not review_path.exists():
            continue
        try:
            text = review_path.read_text(encoding="utf-8", errors="replace")[:8000]
        except Exception:
            continue
        found = {m.group(0).lower() for m in doi_re.finditer(text)}
        if not found:
            no_doi_in_review += 1
            continue
        if idx_doi not in found:
            # Allow truncation: check by prefix match
            if any(d.startswith(idx_doi[:20]) or idx_doi.startswith(d[:20]) for d in found):
                continue
            mismatches.append((p.get("slug", "?"), idx_doi, list(found)[:2]))
    for slug, idoi, fdois in mismatches[:10]:
        issues.append(f"  [doi] {slug[:55]}: index='{idoi[:40]}' review={fdois}")
    if len(mismatches) > 10:
        issues.append(f"  [doi] ... +{len(mismatches)-10} more DOI mismatches")
    return issues


# ── 6. Duplicate text.md (PDF 오매칭 재발 방지) ──

def check_duplicate_text_md(topic):
    """docs/papers/{slug}/text.md의 SHA256이 같은 슬러그 쌍을 찾는다.
    동일 해시가 여러 슬러그에 걸쳐 있으면 같은 PDF로 중복 리뷰된 것."""
    issues = []
    by_hash = defaultdict(list)
    papers_dir = Path(PAPERS_DIR)
    index = json.loads((papers_dir / "_papers_index.json").read_text(encoding="utf-8"))
    topic_slugs = {e["slug"] for e in index if topic in e.get("topics", [])}
    for slug_dir in papers_dir.iterdir():
        if not slug_dir.is_dir() or slug_dir.name not in topic_slugs:
            continue
        txt = slug_dir / "text.md"
        if not txt.exists():
            continue
        try:
            h = hashlib.sha256(txt.read_bytes()).hexdigest()
        except Exception:
            continue
        by_hash[h].append(slug_dir.name)
    for h, slugs in by_hash.items():
        if len(slugs) > 1:
            issues.append(f"  [dup-text] {len(slugs)} slugs share text.md hash {h[:10]}: "
                          f"{', '.join(slugs[:3])}{'...' if len(slugs) > 3 else ''}")
    return issues


def check_orphan_originality(topic):
    """originality.md 가 자기 text.md 에서 나온 것인지 검사한다.

    `originality.md` 는 캐시인데 오래도록 **출처 기록이 없었다**. 파일이 있으면
    원문을 다시 보지 않았으므로, 한번 잘못 들어간 파일은 영구히 남아 그 논문의
    임베딩·분류·연관논문을 전부 남의 내용으로 계산하게 만들었다 — 도입 시점
    실측 29편(0.7%). 예: 슬러그 256(RFdiffusion, Nature 2023)이 슬러그
    065(VibeGen)의 문장을 들고 있었고, 256 의 text.md 에 VibeGen 은 0회 등장한다.

    이제 `extract_originalities` 가 sha256 사이드카를 남기므로, 이 게이트는
    사이드카가 원문을 가리키는지와 내용이 실제로 그 원문에서 나오는지를 본다.
    """
    from lib.originality_extractor import derives_from, read_provenance, text_digest

    issues = []
    papers_dir = Path(PAPERS_DIR)
    index = json.loads((papers_dir / "_papers_index.json").read_text(encoding="utf-8"))
    topic_slugs = {e["slug"] for e in index if topic in e.get("topics", [])}
    stale = []
    for slug in sorted(topic_slugs):
        slug_dir = papers_dir / slug
        orig_path, text_path = slug_dir / "originality.md", slug_dir / "text.md"
        if not orig_path.exists() or not text_path.exists():
            continue
        try:
            orig = orig_path.read_text(encoding="utf-8", errors="replace").strip()
            full = text_path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        if not orig:
            continue
        recorded = read_provenance(slug_dir).get("text_md_sha256")
        if recorded == text_digest(full):
            continue
        if derives_from(orig, full):
            continue
        stale.append(slug)
    for slug in stale[:10]:
        issues.append(f"  [orphan-originality] {slug[:60]}: 자기 text.md 에서 재현 불가")
    if len(stale) > 10:
        issues.append(f"  [orphan-originality] ... +{len(stale) - 10} more")
    return issues


def check_connection_coverage(topic):
    """분류된 논문(_new_classification.json assignments)이 연결(_paper_connections.json
    키)을 갖는지 검사한다.

    paper-curio 등 일부 ingestion 경로는 review·분류까지만 도달하고 연결 생성
    (extract_insights)을 트리거하지 못해, 분류됐지만 연결이 없는 논문이 남는다.
    이 게이트가 그 빈틈을 빌드 때마다 드러낸다. 진단 가치를 위해 paper-curio
    예약 번호대(9xxx)와 일반 파이프라인 논문을 구분해 보고한다."""
    issues = []
    topic_dir = Path(get_topic_dir(topic))
    cls_path = topic_dir / "_new_classification.json"
    conn_path = topic_dir / "_paper_connections.json"
    if not cls_path.exists() or not conn_path.exists():
        return issues  # 토픽 구조 부재 시 스킵
    try:
        assignments = json.loads(cls_path.read_text(encoding="utf-8")).get("assignments", [])
        conn = json.loads(conn_path.read_text(encoding="utf-8"))
    except Exception:
        return issues

    assigned = [a["slug"] for a in assignments if a.get("slug")]
    missing = [s for s in assigned if s not in conn]
    if not missing:
        return issues

    def _is_curio(slug):
        m = re.match(r"(\d+)_", slug)
        return bool(m) and int(m.group(1)) >= 9000

    curio = [s for s in missing if _is_curio(s)]
    issues.append(f"  {len(missing)} classified paper(s) have NO connections "
                  f"({len(curio)} paper-curio 9xxx, {len(missing) - len(curio)} pipeline) "
                  f"— run extract_insights --topic {topic} --connections-only")
    for s in sorted(missing)[:8]:
        issues.append(f"  missing: {s[:60]}")
    if len(missing) > 8:
        issues.append(f"  ... +{len(missing) - 8} more")
    return issues


def _run_validate(topic="ai4s", *, fix=False, strict=False):
    """Programmatic entrypoint for validate_papers."""
    index_path = os.path.join(PAPERS_DIR, "_papers_index.json")
    with open(index_path, "r", encoding="utf-8") as f:
        papers = json.load(f)

    topic_papers = [p for p in papers if topic in p.get("topics", [])]
    log(f"Validating {len(topic_papers)} papers (topic: {topic})")

    total_truncated = 0
    total_title = 0
    total_link = 0
    total_fig = 0
    total_pylist = 0
    total_fixed = 0
    fixed_slugs = []  # for HTML regeneration

    for p in sorted(topic_papers, key=lambda x: x.get("slug", "")):
        slug = p.get("slug", "")
        review_path = os.path.join(PAPERS_DIR, slug, "review.md")
        if not os.path.exists(review_path):
            continue

        paper_issues = []
        slug_fixed = False

        # 0. 제목 헤더 유실 (HTML 제목이 절대경로로 새는 원인)
        title_issues = check_title_header(review_path)
        paper_issues.extend(title_issues)
        total_title += len(title_issues)

        # 1. Truncated sections
        trunc = check_truncated_sections(review_path)
        paper_issues.extend(trunc)
        total_truncated += len(trunc)

        # 2. Broken links
        links = check_broken_links(review_path, slug)
        paper_issues.extend(links)
        total_link += len(links)

        # 3. Figure refs
        figs, fig_fixed = check_figure_refs(review_path, slug, fix=fix)
        paper_issues.extend(figs)
        total_fig += len(figs)
        if fig_fixed:
            total_fixed += 1
            slug_fixed = True

        # 4. Python list literals
        pylist, pylist_fixed = check_python_list_literals(review_path, fix=fix)
        paper_issues.extend(pylist)
        total_pylist += len(pylist)
        if pylist_fixed:
            total_fixed += 1
            slug_fixed = True

        if slug_fixed:
            fixed_slugs.append(slug)

        if paper_issues:
            log(f"\n{slug}:")
            for issue in paper_issues:
                log(issue)

    # 4.5 Re-render index.html for slugs whose review.md was auto-fixed
    if fix and fixed_slugs:
        log(f"\n[fix] Regenerating HTML for {len(fixed_slugs)} repaired slugs...")
        try:
            from review_to_html import convert_review, detect_topic
            index_path = os.path.join(PAPERS_DIR, "_papers_index.json")
            ok, fail = 0, 0
            for slug in fixed_slugs:
                slug_dir = os.path.join(PAPERS_DIR, slug)
                md_path = os.path.join(slug_dir, "review.md")
                html_path = os.path.join(slug_dir, "index.html")
                try:
                    detected_topic = detect_topic(slug, index_path) or topic
                    html = convert_review(md_path, detected_topic, slug_dir)
                    with open(html_path, "w", encoding="utf-8") as f:
                        f.write(html)
                    ok += 1
                except Exception as inner:
                    log(f"  [fix] {slug}: HTML regen failed: {inner}")
                    fail += 1
            log(f"[fix] HTML regeneration: {ok} ok, {fail} failed")
        except Exception as e:
            log(f"[fix] HTML regen import failed: {e}")

    # 5. Category ↔ timeline mismatch (topic-level)
    timeline_issues = check_timeline_mismatch(topic)
    if timeline_issues:
        log(f"\n[topic {topic}] timeline mismatch:")
        for i in timeline_issues:
            log(i)

    # 5b. classifications schema + 카테고리 화이트리스트
    schema_issues = check_classifications_schema(topic)
    if schema_issues:
        log(f"\n[topic {topic}] classifications schema/whitelist:")
        for i in schema_issues:
            log(i)

    # 5c. DOI 교차검증 (index.doi vs review.md DOI)
    doi_issues = check_doi_cross_validation(topic)
    if doi_issues:
        log(f"\n[topic {topic}] DOI cross-validation mismatches:")
        for i in doi_issues:
            log(i)

    # 6. Duplicate text.md (topic-level, PDF 오매칭)
    dup_issues = check_duplicate_text_md(topic)
    if dup_issues:
        log(f"\n[topic {topic}] duplicate text.md groups:")
        for i in dup_issues:
            log(i)

    # 6b. Orphan originality (남의 논문 내용을 든 originality.md 캐시)
    orphan_issues = check_orphan_originality(topic)
    if orphan_issues:
        log(f"\n[topic {topic}] orphan originality.md:")
        for i in orphan_issues:
            log(i)

    # 7. Connection coverage (분류됐는데 연결 없는 논문 — paper-curio 핸드오프 빈틈)
    conn_issues = check_connection_coverage(topic)
    if conn_issues:
        log(f"\n[topic {topic}] connection coverage gaps:")
        for i in conn_issues:
            log(i)

    log(f"\n{'='*60}")
    log(f"Validation Summary ({topic})")
    log(f"{'='*60}")
    log(f"  Papers checked: {len(topic_papers)}")
    log(f"  Missing title header: {total_title}")
    log(f"  Truncated sections: {total_truncated}")
    log(f"  Broken links: {total_link}")
    log(f"  Figure issues: {total_fig}")
    log(f"  Python list literals: {total_pylist}")
    log(f"  Timeline mismatches: {len(timeline_issues)}")
    log(f"  Schema/whitelist issues: {len(schema_issues)}")
    log(f"  DOI mismatches: {len(doi_issues)}")
    log(f"  Duplicate text.md groups: {len(dup_issues)}")
    log(f"  Orphan originality.md: {len(orphan_issues)}")
    log(f"  Connection coverage gaps: {len(conn_issues)}")
    if fix:
        log(f"  Auto-fixed: {total_fixed} papers")
    total_all = (total_title + total_truncated + total_link + total_fig + total_pylist
                 + len(timeline_issues) + len(schema_issues)
                 + len(doi_issues) + len(dup_issues) + len(orphan_issues)
                 + len(conn_issues))
    if total_all == 0:
        log(f"  ALL CLEAR!")
    else:
        log(f"  Total issues: {total_all}")

    if strict and total_all > 0:
        log(f"\n--strict: failing build due to {total_all} issue(s)")
        sys.exit(1)
    return total_all


def main():
    parser = argparse.ArgumentParser(description="Post-build validation")
    parser.add_argument("--topic", default="ai4s")
    parser.add_argument("--fix", action="store_true", help="Auto-fix figure refs + Python list literals")
    parser.add_argument("--strict", action="store_true",
                        help="Exit non-zero if any issue is found (deploy gate).")
    args = parser.parse_args()
    _run_validate(topic=args.topic, fix=args.fix, strict=args.strict)


if __name__ == "__main__":
    main()
