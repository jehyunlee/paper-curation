"""
Zotero 컬렉션 중복 탐지·제거.

중복 그룹핑 축 (하나라도 겹치면 같은 그룹):
  - normalized title prefix (첫 30자, 특수문자 제거·lowercase)
  - DOI (정규화)
  - arXiv ID (URL/DOI/extra에서 추출)
  - 첨부 PDF의 파일명 (basename) — 같은 PDF 공유 감지

남길 항목 선정 점수 (높을수록 보존):
  1. has_pdf (가장 강한 우선순위: PDF 있는 것 > 없는 것) — +1000
  2. 메타데이터 풍부도 — abstract 길이/100 + creator 수*5 + (DOI? +20) + (date? +10) + (url? +5)
  3. 최근 수정 시각 (동점시 마지막 보루) — ISO version +1/1000

같은 점수면 먼저 등록된 것(낮은 version)을 유지.

Usage:
  # 기본 dry-run (실제 삭제 없음)
  PYTHONUTF8=1 python pipeline/dedup_zotero.py --topic ai4s

  # 실제 삭제
  PYTHONUTF8=1 python pipeline/dedup_zotero.py --topic ai4s --execute

  # 특정 그룹만 확인
  PYTHONUTF8=1 python pipeline/dedup_zotero.py --topic ai4s --show-all

결과 리포트: docs/{topic}/_dedup_zotero_report.json
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.request
import urllib.parse
import urllib.error
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from config_loader import (
    get_zotero_api_key,
    get_zotero_user_id,
    get_collection_key,
    get_topic_dir,
    _ssl_ctx,
)

# Zotero 자격증명은 호출 지점에서 해석한다 (import 시 키 요구·네트워크 왕복 없음).


# ── Zotero API helpers ───────────────────────────────────────────────────────

def _api(endpoint, method="GET", data=None, if_unmod_version=None, params=None):
    base = f"https://api.zotero.org/users/{get_zotero_user_id()}/{endpoint}"
    if params:
        base += "?" + urllib.parse.urlencode(params)
    body = json.dumps(data).encode("utf-8") if data is not None else None
    headers = {
        "Zotero-API-Key": get_zotero_api_key(),
        "User-Agent": "paper-curation-dedup/1.0",
    }
    if data is not None:
        headers["Content-Type"] = "application/json"
    if if_unmod_version is not None:
        headers["If-Unmodified-Since-Version"] = str(if_unmod_version)
    req = urllib.request.Request(base, data=body, method=method, headers=headers)
    with urllib.request.urlopen(req, timeout=30, context=_ssl_ctx) as resp:
        raw = resp.read()
        return json.loads(raw.decode("utf-8")) if raw else {}


def list_collection_items(collection_key):
    """Top-level items (no attachments/notes)."""
    items = []
    start = 0
    while True:
        batch = _api(f"collections/{collection_key}/items/top",
                     params={"limit": 100, "start": start, "format": "json"})
        if not batch:
            break
        items.extend(batch)
        if len(batch) < 100:
            break
        start += 100
        time.sleep(0.5)
    return items


def list_children(item_key):
    try:
        return _api(f"items/{item_key}/children", params={"format": "json"})
    except Exception:
        return []


def delete_item(item_key, version):
    return _api(f"items/{item_key}", method="DELETE", if_unmod_version=version)


# ── Normalizers ──────────────────────────────────────────────────────────────

def norm_title(title):
    # 60-char prefix is long enough that overlap between different papers is
    # unlikely even for same-topic surveys, while still catching re-registrations
    # of the same paper (Zotero imports sometimes truncate or re-case titles).
    return re.sub(r"[^a-z0-9]", "", (title or "").lower())[:60]


def norm_doi(doi):
    return re.sub(r"[^a-z0-9]", "", (doi or "").lower())


def extract_arxiv_id(item_data):
    for field in ("url", "DOI", "extra", "archiveID"):
        v = item_data.get(field, "") or ""
        m = re.search(r"(\d{4}\.\d{4,5})", v)
        if m:
            return m.group(1)
    return ""


# ── Scoring (higher = keep) ──────────────────────────────────────────────────

def score_item(item, children):
    d = item.get("data", {})
    pdfs = [c for c in children
            if c.get("data", {}).get("itemType") == "attachment"
            and c.get("data", {}).get("contentType") == "application/pdf"]
    pdf_present = any(
        (c.get("data", {}).get("linkMode") in ("imported_file", "imported_url")
         or os.path.exists(c.get("data", {}).get("path", "") or ""))
        for c in pdfs
    ) or bool(pdfs)  # at least a linked PDF record counts

    score = 0.0
    if pdf_present:
        score += 1000
    # metadata richness
    score += min(300, len(d.get("abstractNote", "") or "") / 100)
    score += len(d.get("creators", []) or []) * 5
    if d.get("DOI"):
        score += 20
    if d.get("date"):
        score += 10
    if d.get("url"):
        score += 5
    score += item.get("version", 0) / 1e6  # tiebreaker: newer version slightly preferred
    return score, pdf_present


# ── Group items by any overlapping key ───────────────────────────────────────

def group_duplicates(items):
    """Union-Find over (normalized title, DOI, arxiv_id, pdf_basename)."""
    parent = {}

    def find(x):
        while parent.get(x, x) != x:
            parent[x] = parent.get(parent[x], parent[x])
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for item in items:
        parent.setdefault(item["key"], item["key"])

    for key_type in ("title", "doi", "arxiv", "pdf"):
        bucket = defaultdict(list)
        for it in items:
            d = it.get("data", {})
            if key_type == "title":
                k = norm_title(d.get("title", ""))
            elif key_type == "doi":
                k = norm_doi(d.get("DOI", ""))
            elif key_type == "arxiv":
                k = extract_arxiv_id(d)
            else:  # pdf basename
                k = None
                for c in it.get("_children", []):
                    cd = c.get("data", {})
                    if cd.get("contentType") == "application/pdf":
                        path = cd.get("path", "") or cd.get("filename", "")
                        if path:
                            k = os.path.basename(path).lower()
                            break
            if k and len(k) >= 8:
                bucket[k].append(it["key"])

        for keys in bucket.values():
            if len(keys) < 2:
                continue
            anchor = keys[0]
            for other in keys[1:]:
                union(anchor, other)

    groups = defaultdict(list)
    for it in items:
        groups[find(it["key"])].append(it)
    return [g for g in groups.values() if len(g) > 1]


# ── Main ─────────────────────────────────────────────────────────────────────

def _run_dedup(topic, *, execute=False, show_all=False, sleep=0.3):
    """Programmatic entrypoint for dedup_zotero."""
    ck = get_collection_key(topic)
    if not ck:
        print(f"ERROR: collection for topic {topic} not configured", file=sys.stderr)
        sys.exit(2)

    print(f"[{datetime.now():%H:%M:%S}] Fetching collection '{topic}' ({ck})...")
    items = list_collection_items(ck)
    print(f"  {len(items)} top-level items")

    print(f"[{datetime.now():%H:%M:%S}] Fetching children for {len(items)} items...")
    t0 = time.time()
    for i, it in enumerate(items, 1):
        it["_children"] = list_children(it["key"])
        if i % 50 == 0 or i == len(items):
            print(f"  [{i}/{len(items)}] {time.time()-t0:.0f}s elapsed")
        time.sleep(sleep)

    groups = group_duplicates(items)
    print(f"\n[{datetime.now():%H:%M:%S}] Duplicate groups: {len(groups)}")

    # Decide keep/remove per group
    actions = []
    total_to_delete = 0
    for g in sorted(groups, key=lambda lst: -len(lst)):
        scored = []
        for it in g:
            s, has_pdf = score_item(it, it.get("_children", []))
            scored.append((s, has_pdf, it))
        scored.sort(key=lambda t: -t[0])
        keeper = scored[0][2]
        removers = [t[2] for t in scored[1:]]
        actions.append({
            "group_size": len(g),
            "keep": {
                "key": keeper["key"],
                "title": keeper["data"].get("title", "")[:120],
                "has_pdf": scored[0][1],
                "score": round(scored[0][0], 2),
            },
            "remove": [
                {
                    "key": t[2]["key"],
                    "title": t[2]["data"].get("title", "")[:120],
                    "has_pdf": t[1],
                    "score": round(t[0], 2),
                    "version": t[2].get("version", 0),
                }
                for t in scored[1:]
            ],
        })
        total_to_delete += len(removers)

    print(f"  Items to delete: {total_to_delete}")
    print(f"  Items to keep  : {len(actions)}  (one per group)")

    if show_all or not execute:
        for i, a in enumerate(actions, 1):
            print(f"\n  [group {i}] size={a['group_size']}")
            k = a["keep"]
            print(f"    KEEP   {k['key']} (pdf={k['has_pdf']}, score={k['score']}): {k['title']}")
            for r in a["remove"]:
                print(f"    DELETE {r['key']} (pdf={r['has_pdf']}, score={r['score']}): {r['title']}")

    report_path = get_topic_dir(topic) / "_dedup_zotero_report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    from lib.atomic_io import atomic_write_json
    atomic_write_json(report_path, {
        "topic": topic,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "total_items": len(items),
        "duplicate_groups": len(groups),
        "items_to_delete": total_to_delete,
        "actions": actions,
        "mode": "execute" if execute else "dry-run",
    })
    print(f"\n  Report: {report_path}")

    if not execute:
        print("\n  (dry-run) No deletions performed. Run with --execute to apply.")
        return {"groups": len(groups), "items_to_delete": total_to_delete,
                "report_path": str(report_path)}

    print(f"\n[{datetime.now():%H:%M:%S}] Deleting {total_to_delete} items...")
    deleted = 0
    failed = []
    for a in actions:
        for r in a["remove"]:
            try:
                delete_item(r["key"], r["version"])
                deleted += 1
                print(f"  DEL {r['key']}: {r['title'][:60]}")
            except urllib.error.HTTPError as e:
                body = e.read().decode("utf-8", errors="replace")[:200]
                print(f"  FAIL {r['key']} [{e.code}]: {body}")
                failed.append({"key": r["key"], "error": f"{e.code} {body}"})
            except Exception as e:
                print(f"  FAIL {r['key']}: {e}")
                failed.append({"key": r["key"], "error": str(e)})
            time.sleep(sleep)

    print(f"\nDone. Deleted {deleted}/{total_to_delete}")
    if failed:
        print(f"Failed: {len(failed)} — see {report_path}")
    return {"groups": len(groups), "deleted": deleted, "failed": failed,
            "report_path": str(report_path)}


def main():
    ap = argparse.ArgumentParser(description="Zotero collection deduplication")
    ap.add_argument("--topic", required=True)
    ap.add_argument("--execute", action="store_true",
                    help="Actually delete. Default is dry-run.")
    ap.add_argument("--show-all", action="store_true",
                    help="Print every duplicate group (verbose).")
    ap.add_argument("--sleep", type=float, default=0.3,
                    help="Per-request sleep (seconds) to be nice to Zotero API.")
    args = ap.parse_args()
    _run_dedup(topic=args.topic, execute=args.execute,
               show_all=args.show_all, sleep=args.sleep)


if __name__ == "__main__":
    main()
