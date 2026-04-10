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
import json
import os
import re
import sys
from pathlib import Path

from config_loader import PAPERS_DIR as _PAPERS_DIR
PAPERS_DIR = str(_PAPERS_DIR)


def log(msg):
    print(msg, flush=True)


# ── 1. 문장 완결 체크 ──

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
    """review.md의 그림 참조가 실제 파일과 일치하는지 확인."""
    issues = []
    slug_dir = os.path.join(PAPERS_DIR, slug)
    fig_dir = os.path.join(slug_dir, "figures")

    with open(review_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find all figure references in markdown
    refs = list(re.finditer(r'!\[([^\]]*)\]\((figures/[^)]+)\)', content))
    if not refs:
        return issues, False

    # Build map of actual figure files
    actual_figs = {}
    if os.path.isdir(fig_dir):
        for fname in os.listdir(fig_dir):
            if re.match(r'fig\d+\.(png|webp)', fname):
                actual_figs[fname] = True

    changed = False
    new_content = content

    for m in refs:
        ref_path = m.group(2)  # e.g. "figures/fig1a.webp"
        full_path = os.path.join(slug_dir, ref_path)
        if os.path.exists(full_path):
            continue

        # File doesn't exist — try to find a match
        fig_name = os.path.basename(ref_path)
        # Extract figure number from reference
        num_match = re.search(r'fig(\d+)', fig_name)
        if not num_match:
            issues.append(f"  BROKEN_FIG: {ref_path} (no number found)")
            continue

        fig_num = num_match.group(1)
        # Look for actual file with this number
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

def main():
    parser = argparse.ArgumentParser(description="Post-build validation")
    parser.add_argument("--topic", default="ai4s")
    parser.add_argument("--fix", action="store_true", help="Auto-fix figure refs + Python list literals")
    args = parser.parse_args()

    # Load index
    index_path = os.path.join(PAPERS_DIR, "_papers_index.json")
    with open(index_path, "r", encoding="utf-8") as f:
        papers = json.load(f)

    topic_papers = [p for p in papers if args.topic in p.get("topics", [])]
    log(f"Validating {len(topic_papers)} papers (topic: {args.topic})")

    total_truncated = 0
    total_link = 0
    total_fig = 0
    total_pylist = 0
    total_fixed = 0

    for p in sorted(topic_papers, key=lambda x: x.get("slug", "")):
        slug = p.get("slug", "")
        review_path = os.path.join(PAPERS_DIR, slug, "review.md")
        if not os.path.exists(review_path):
            continue

        paper_issues = []

        # 1. Truncated sections
        trunc = check_truncated_sections(review_path)
        paper_issues.extend(trunc)
        total_truncated += len(trunc)

        # 2. Broken links
        links = check_broken_links(review_path, slug)
        paper_issues.extend(links)
        total_link += len(links)

        # 3. Figure refs
        figs, fig_fixed = check_figure_refs(review_path, slug, fix=args.fix)
        paper_issues.extend(figs)
        total_fig += len(figs)
        if fig_fixed:
            total_fixed += 1

        # 4. Python list literals
        pylist, pylist_fixed = check_python_list_literals(review_path, fix=args.fix)
        paper_issues.extend(pylist)
        total_pylist += len(pylist)
        if pylist_fixed:
            total_fixed += 1

        if paper_issues:
            log(f"\n{slug}:")
            for issue in paper_issues:
                log(issue)

    log(f"\n{'='*60}")
    log(f"Validation Summary ({args.topic})")
    log(f"{'='*60}")
    log(f"  Papers checked: {len(topic_papers)}")
    log(f"  Truncated sections: {total_truncated}")
    log(f"  Broken links: {total_link}")
    log(f"  Figure issues: {total_fig}")
    log(f"  Python list literals: {total_pylist}")
    if args.fix:
        log(f"  Auto-fixed: {total_fixed} papers")
    total_all = total_truncated + total_link + total_fig + total_pylist
    if total_all == 0:
        log(f"  ALL CLEAR!")
    else:
        log(f"  Total issues: {total_all}")


if __name__ == "__main__":
    main()
