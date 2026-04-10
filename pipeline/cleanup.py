"""
배포 전 미사용 파일 정리 스크립트.

Usage:
  PYTHONUTF8=1 python pipeline/cleanup.py                # dry-run (삭제 목록만 출력, text.md 보존)
  PYTHONUTF8=1 python pipeline/cleanup.py --execute       # 실제 삭제
  PYTHONUTF8=1 python pipeline/cleanup.py --purge-text    # text.md도 삭제 (기본: 보존)
"""

import argparse
import json
import os
import shutil
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PAPERS_DIR = PROJECT_ROOT / "docs" / "papers"
PIPELINE_DIR = PROJECT_ROOT / "pipeline"
DOCS_DIR = PROJECT_ROOT / "docs"


def log(msg):
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def _get_current_categories():
    """현재 활성 카테고리 slug 목록을 수집 (_category_summaries.json 기반)."""
    from lib.categories import category_slug
    current_slugs = set()
    for topic_dir in DOCS_DIR.iterdir():
        if not topic_dir.is_dir() or topic_dir.name == "papers":
            continue
        sum_path = topic_dir / "_category_summaries.json"
        if sum_path.exists():
            with open(sum_path, "r", encoding="utf-8") as f:
                summaries = json.load(f)
            for s in summaries:
                current_slugs.add(category_slug(s["category"]))
    return current_slugs


def collect_targets(purge_text=False):
    """삭제 대상 수집. (path, category, size_bytes) 리스트 반환."""
    targets = []

    def add_file(path, category):
        p = Path(path)
        if p.exists():
            targets.append((str(p), category, p.stat().st_size))

    def add_dir(path, category):
        p = Path(path)
        if p.exists() and p.is_dir():
            size = sum(f.stat().st_size for f in p.rglob("*") if f.is_file())
            targets.append((str(p), category, size))

    # 1. text.md — PDF 텍스트 캐시 (기본 보존, --purge-text로 삭제)
    if purge_text:
        for d in PAPERS_DIR.iterdir():
            if d.is_dir() and d.name[0].isdigit():
                tm = d / "text.md"
                if tm.exists():
                    add_file(tm, "text.md (PDF cache)")

    # 2. .chunk_*.txt — graphify 임시 파일
    for f in PAPERS_DIR.glob(".chunk_*.txt"):
        add_file(f, "graphify chunk")

    # 3. .graphify_chunks/ — graphify 임시 디렉토리
    add_dir(PAPERS_DIR / ".graphify_chunks", "graphify chunks dir")

    # 4. graphify-out/ — graphify 출력 디렉토리
    add_dir(PAPERS_DIR / "graphify-out", "graphify output dir")

    # 5. __pycache__ — 프로젝트 내 (venv 제외)
    for cache_dir in [
        PROJECT_ROOT / "__pycache__",
        PIPELINE_DIR / "__pycache__",
        PIPELINE_DIR / "lib" / "__pycache__",
    ]:
        add_dir(cache_dir, "__pycache__")

    # 6. _update_force_checkpoint.json — 완료된 체크포인트
    add_file(PROJECT_ROOT / "_update_force_checkpoint.json", "checkpoint")
    add_file(PIPELINE_DIR / "_update_force_checkpoint.json", "checkpoint")

    # 7. _search_results.json, _register_results.json — 검색 임시 결과
    for topic_dir in DOCS_DIR.iterdir():
        if topic_dir.is_dir() and topic_dir.name != "papers":
            for name in ("_search_results.json", "_register_results.json"):
                p = topic_dir / name
                if p.exists():
                    add_file(p, "search/register cache")

    # 8. docs/{topic}/category_timeline_*.png — 과거 카테고리 배포 이미지 삭제
    current_slugs = _get_current_categories()
    current_slugs.add("main")
    for topic_dir in DOCS_DIR.iterdir():
        if not topic_dir.is_dir() or topic_dir.name == "papers":
            continue
        for f in topic_dir.glob("category_timeline_*"):
            # category_timeline_{slug}.png or .webp
            slug = f.stem.replace("category_timeline_", "")
            if slug not in current_slugs:
                add_file(f, "stale deployed timeline")
        # Also check _method_text_{slug}.txt / _caption_{slug}.txt
        for f in topic_dir.glob("_method_text_*.txt"):
            slug = f.stem[len("_method_text_"):]
            if slug not in current_slugs:
                add_file(f, "stale deployed narrative")
        for f in topic_dir.glob("_caption_*.txt"):
            slug = f.stem[len("_caption_"):]
            if slug not in current_slugs:
                add_file(f, "stale deployed narrative")

    # 9. docs/{topic}/timeline_candidates_pb/ — 과거 candidate 디렉토리 (전체 삭제)
    for topic_dir in DOCS_DIR.iterdir():
        if not topic_dir.is_dir() or topic_dir.name == "papers":
            continue
        tc_dir = topic_dir / "timeline_candidates_pb"
        if tc_dir.exists():
            add_dir(tc_dir, "stale timeline_candidates_pb")

    # 10. pipeline/_img_timelines/ — 과거 카테고리 candidate만 삭제, 현재 카테고리 보존
    img_tl_dir = PIPELINE_DIR / "_img_timelines"
    if img_tl_dir.exists():
        current_slugs = _get_current_categories()
        current_slugs.add("main")  # main timeline은 항상 보존
        for topic_sub in img_tl_dir.iterdir():
            if not topic_sub.is_dir():
                continue
            for f in topic_sub.iterdir():
                if f.is_dir():
                    continue
                # 파일명에서 카테고리 slug 추출: _method_text_{slug}.txt, _caption_{slug}.txt, {slug}_candidate_N.png
                stem = f.stem
                slug = None
                for prefix in ("_method_text_", "_caption_"):
                    if stem.startswith(prefix):
                        slug = stem[len(prefix):]
                        break
                if slug is None:
                    # candidate image: {slug}_candidate_N 또는 기타
                    parts = stem.rsplit("_candidate_", 1)
                    if len(parts) == 2:
                        slug = parts[0]
                if slug and slug not in current_slugs:
                    add_file(f, "stale timeline candidate")

    return targets


def human_size(nbytes):
    for unit in ("B", "KB", "MB", "GB"):
        if abs(nbytes) < 1024:
            return f"{nbytes:.1f}{unit}"
        nbytes /= 1024
    return f"{nbytes:.1f}TB"


def main():
    parser = argparse.ArgumentParser(description="Clean unused files before deploy")
    parser.add_argument("--execute", action="store_true", help="Actually delete (default: dry-run)")
    parser.add_argument("--purge-text", action="store_true", help="Also delete text.md (default: keep)")
    args = parser.parse_args()

    targets = collect_targets(purge_text=args.purge_text)

    if not targets:
        log("Nothing to clean!")
        return

    # Group by category
    from collections import defaultdict
    by_cat = defaultdict(list)
    for path, cat, size in targets:
        by_cat[cat].append((path, size))

    total_size = sum(s for _, _, s in targets)
    total_count = len(targets)

    log(f"{'DRY RUN' if not args.execute else 'EXECUTING'}: {total_count} items, {human_size(total_size)} total\n")

    for cat in sorted(by_cat.keys()):
        items = by_cat[cat]
        cat_size = sum(s for _, s in items)
        log(f"  [{cat}] {len(items)} items, {human_size(cat_size)}")
        for path, size in items[:5]:
            rel = os.path.relpath(path, PROJECT_ROOT)
            log(f"    {rel} ({human_size(size)})")
        if len(items) > 5:
            log(f"    ... and {len(items) - 5} more")

    print()

    if not args.execute:
        log(f"Dry run complete. Run with --execute to delete {total_count} items ({human_size(total_size)})")
        return

    # Execute deletion
    deleted = 0
    freed = 0
    for path, cat, size in targets:
        p = Path(path)
        try:
            if p.is_dir():
                shutil.rmtree(p)
            else:
                p.unlink()
            deleted += 1
            freed += size
        except Exception as e:
            log(f"  ERROR: {path}: {e}")

    log(f"Done! Deleted {deleted}/{total_count} items, freed {human_size(freed)}")


if __name__ == "__main__":
    main()
