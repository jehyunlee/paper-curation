"""
Zotero 컬렉션과 _papers_index.json 간 동기화.

기능:
  1. 삭제 감지: Zotero에서 제거된 논문 → index에서도 제거
  2. 제목 변경 감지: Zotero에서 제목이 바뀐 논문 → index 제목 업데이트
  3. 매칭: DOI 우선, 제목 퍼지 매칭 폴백

Usage:
  PYTHONUTF8=1 python sync_zotero.py --topic ai4s
  PYTHONUTF8=1 python sync_zotero.py --topic ai4s --dry-run
"""

import argparse
import json
import os
import re
import shutil
import urllib.request
import urllib.parse
from datetime import datetime

from config_loader import PAPERS_DIR as _PAPERS_DIR
PAPERS_DIR = str(_PAPERS_DIR)

from config_loader import get_zotero_api_key, get_zotero_user_id, get_collections, _ssl_ctx

# Zotero 자격증명은 호출 지점에서 해석한다 (import 시 키 요구·네트워크 왕복 없음).
COLLECTIONS = get_collections()


def log(msg):
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def normalize_title(title):
    """제목 정규화: 소문자, 비알파벳 제거, 앞 50자."""
    return re.sub(r"[^a-z0-9]", "", title.lower())[:50]


def normalize_doi(doi):
    """DOI 정규화: 소문자, 앞뒤 공백 제거. arXiv: prefix 포함."""
    if not doi:
        return ""
    doi = doi.strip().lower()
    # Remove URL prefix
    for prefix in ["https://doi.org/", "http://doi.org/", "doi:"]:
        if doi.startswith(prefix):
            doi = doi[len(prefix):]
    return doi


def fetch_zotero_items(collection_key):
    """Zotero 컬렉션의 모든 논문 메타데이터를 반환."""
    items = []
    start = 0
    while True:
        url = (f"https://api.zotero.org/users/{get_zotero_user_id()}/collections/"
               f"{collection_key}/items/top?limit=100&start={start}&format=json")
        req = urllib.request.Request(url, headers={
            "Zotero-API-Key": get_zotero_api_key(), "User-Agent": "Mozilla/5.0"
        })
        with urllib.request.urlopen(req, timeout=30, context=_ssl_ctx) as resp:
            batch = json.load(resp)
        if not batch:
            break
        for item in batch:
            d = item["data"]
            if d.get("itemType") in ("attachment", "note", "forumPost", "videoRecording"):
                continue
            title = d.get("title", "").strip()
            doi = normalize_doi(d.get("DOI", ""))
            # arXiv ID from archiveID or URL
            arxiv_id = ""
            archive_id = d.get("archiveID", "")
            url_field = d.get("url", "")
            if "arXiv:" in archive_id:
                arxiv_id = archive_id.split("arXiv:")[-1]
            elif "arxiv.org/abs/" in url_field:
                arxiv_id = url_field.split("arxiv.org/abs/")[-1].split("v")[0]

            items.append({
                "key": d["key"],
                "title": title,
                "title_norm": normalize_title(title),
                "doi": doi,
                "arxiv_id": arxiv_id,
            })
        start += 100
        if len(batch) < 100:
            break
    return items


def match_paper(index_paper, zotero_items, zotero_doi_map, zotero_title_map):
    """Index 논문을 Zotero 아이템과 매칭. 매칭된 Zotero 아이템 반환, 없으면 None."""
    # 1차: DOI 매칭
    idx_doi = normalize_doi(index_paper.get("doi", ""))
    if idx_doi and idx_doi in zotero_doi_map:
        return zotero_doi_map[idx_doi]

    # 2차: arXiv ID 매칭 (doi 필드에 arXiv: 형태로 저장된 경우)
    idx_doi_raw = index_paper.get("doi", "")
    if idx_doi_raw.startswith("arXiv:"):
        arxiv_id = idx_doi_raw.split("arXiv:")[-1]
        for zi in zotero_items:
            if zi.get("arxiv_id") == arxiv_id:
                return zi

    # 3차: 제목 정규화 매칭
    idx_title_norm = normalize_title(index_paper.get("title", ""))
    if idx_title_norm and idx_title_norm in zotero_title_map:
        return zotero_title_map[idx_title_norm]

    # 4차: 제목 앞 25자 퍼지 매칭 (제목이 약간 바뀐 경우)
    idx_short = idx_title_norm[:25]
    if len(idx_short) > 15:
        for zi in zotero_items:
            if zi["title_norm"][:25] == idx_short:
                return zi

    return None


# 삭제 안전 가드 임계값.
#   - 빈 fetch: 토픽 논문이 있는데 Zotero 가 0건을 돌려주면 (transient 200-empty 등)
#     모든 단일-토픽 논문 디렉토리가 rmtree 대상이 되므로 무조건 차단.
#   - 비율: 한 사이클에 토픽 논문의 이 비율 이상이 삭제 대상이면 (정상 주간 churn 이
#     아니라 fetch 결함일 가능성) 차단. --force-delete 로 우회.
_DELETE_RATIO_THRESHOLD = 0.30


def _run_sync(topic, *, dry_run=False, force_delete=False):
    """Programmatic entrypoint for sync_zotero."""
    collection_key = COLLECTIONS.get(topic)
    if not collection_key:
        print(f"Unknown topic: {topic}")
        return

    index_path = os.path.join(PAPERS_DIR, "_papers_index.json")
    with open(index_path, "r", encoding="utf-8") as f:
        papers = json.load(f)

    # Fetch Zotero
    log(f"Fetching Zotero collection '{topic}' ({collection_key})...")
    zotero_items = fetch_zotero_items(collection_key)
    log(f"Zotero: {len(zotero_items)} papers")

    # Build lookup maps
    zotero_doi_map = {}
    zotero_title_map = {}
    for zi in zotero_items:
        if zi["doi"]:
            zotero_doi_map[zi["doi"]] = zi
        if zi["title_norm"]:
            zotero_title_map[zi["title_norm"]] = zi

    # Find papers in index with this topic
    topic_papers = [p for p in papers if topic in p.get("topics", [])]
    log(f"Index: {len(topic_papers)} papers with topic '{topic}'")

    # Compare
    matched = []
    title_changed = []
    deleted = []

    for p in topic_papers:
        zi = match_paper(p, zotero_items, zotero_doi_map, zotero_title_map)
        if zi:
            matched.append((p, zi))
            # Check title change
            if normalize_title(p["title"])[:30] != zi["title_norm"][:30]:
                title_changed.append((p, zi))
        else:
            remaining_topics = [t for t in p.get("topics", []) if t != topic]
            deleted.append((p, remaining_topics))

    log(f"\nResults:")
    log(f"  Matched: {len(matched)}")
    log(f"  Title changed: {len(title_changed)}")
    log(f"  Deleted from Zotero: {len(deleted)}")

    if title_changed:
        log(f"\n--- Title changes ---")
        for p, zi in title_changed:
            log(f"  {p['slug'][:35]}")
            log(f"    OLD: {p['title'][:70]}")
            log(f"    NEW: {zi['title'][:70]}")

    to_remove_topic = [(p, remaining) for p, remaining in deleted if remaining]
    to_delete_dir = [(p, remaining) for p, remaining in deleted if not remaining]

    if to_remove_topic:
        log(f"\n--- Remove '{topic}' tag (keep other topics): {len(to_remove_topic)} ---")
        for p, remaining in to_remove_topic:
            log(f"  {p['slug'][:40]} | remaining: {remaining}")

    if to_delete_dir:
        log(f"\n--- Delete entirely: {len(to_delete_dir)} ---")
        for p, _ in to_delete_dir:
            log(f"  {p['slug'][:40]} | {p.get('title','')[:60]}")

    if not title_changed and not deleted:
        log("\nAll in sync. No changes needed.")
        return

    if dry_run:
        log("\n--dry-run: no changes made.")
        return

    # --- 삭제 안전 가드 ---------------------------------------------------
    # fetch_zotero_items 는 retry/floor 가 없어 transient 200-empty 나 짧은 응답에서
    # 모든 미매칭 논문을 "Zotero 에서 삭제됨" 으로 오인할 수 있다. 디렉토리 rmtree 는
    # 영구·비가역이므로, 의심스러운 fetch 에서는 파괴적 삭제만 차단한다.
    # (title-update / remove-topic 는 비파괴적이므로 그대로 진행.)
    delete_blocked = False
    if to_delete_dir and not force_delete:
        n_papers = len(topic_papers)
        # 1) 빈/실패 fetch: 토픽 논문이 있는데 Zotero 가 0건 → 정상 상황이 아님.
        if not zotero_items and n_papers:
            log(f"\n[ABORT] Zotero fetch returned 0 items but index has "
                f"{n_papers} '{topic}' papers — likely a transient Zotero outage.")
            delete_blocked = True
        else:
            # 2) 비율: 토픽 논문의 30% 이상이 한 번에 삭제 대상 → fetch 결함 의심.
            del_ratio = len(to_delete_dir) / max(1, n_papers)
            if del_ratio > _DELETE_RATIO_THRESHOLD:
                log(f"\n[ABORT] {len(to_delete_dir)}/{n_papers} "
                    f"({del_ratio:.0%}) of '{topic}' papers would be deleted, "
                    f"over the {_DELETE_RATIO_THRESHOLD:.0%} safety threshold.")
                delete_blocked = True
        if delete_blocked:
            log("  Refusing to delete directories. If this is a real collection "
                "purge, re-run with --force-delete. Otherwise re-run later.")
            # 파괴적 삭제만 비활성화하고 비파괴적 변경은 계속 적용한다.
            to_delete_dir = []

    # Execute
    log("\nExecuting...")
    changes = 0

    # Title updates
    for p, zi in title_changed:
        for paper in papers:
            if paper["slug"] == p["slug"]:
                paper["title"] = zi["title"]
                changes += 1
                break
        log(f"  Updated title: {p['slug'][:40]}")

    # Remove topic tag
    for p, remaining in to_remove_topic:
        for paper in papers:
            if paper["slug"] == p["slug"]:
                paper["topics"] = remaining
                cls = paper.get("classifications", {})
                cls.pop(topic, None)
                changes += 1
                break
        log(f"  Removed '{topic}': {p['slug'][:40]}")

    # Delete entirely
    for p, _ in to_delete_dir:
        papers = [paper for paper in papers if paper["slug"] != p["slug"]]
        slug_dir = os.path.join(PAPERS_DIR, p["slug"])
        if os.path.isdir(slug_dir):
            shutil.rmtree(slug_dir)
            log(f"  Deleted: {p['slug'][:40]} (dir removed)")
        else:
            log(f"  Deleted: {p['slug'][:40]} (index only)")
        changes += 1

    # Save
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(papers, f, ensure_ascii=False, indent=2)

    log(f"\nDone. {changes} changes applied. {len(papers)} papers remaining.")


def main():
    parser = argparse.ArgumentParser(description="Sync deletions/renames from Zotero")
    parser.add_argument("--topic", required=True)
    parser.add_argument("--dry-run", action="store_true", help="Show changes, don't execute")
    parser.add_argument("--force-delete", action="store_true",
                        help="Bypass the empty-fetch / >30%% delete-ratio safety guard "
                             "(intentional large collection purge)")
    args = parser.parse_args()
    _run_sync(topic=args.topic, dry_run=args.dry_run, force_delete=args.force_delete)


if __name__ == "__main__":
    main()
