"""
Zotero 등록 스크립트.

검색 결과 JSON을 입력받아 Zotero에 중복 확인 후 신규 등록하고,
PDF를 다운로드하여 linked file로 첨부.

Usage:
  PYTHONUTF8=1 python register_zotero.py --topic scisci
  PYTHONUTF8=1 python register_zotero.py --topic ai4s --input ai4s/_search_results.json
  PYTHONUTF8=1 python register_zotero.py --topic scisci --fix-pdfs
  PYTHONUTF8=1 python register_zotero.py --topic scisci --dry-run
"""

import argparse
import json
import os
import re
import time
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime
from pathlib import Path

from config_loader import get_topic_dir, PROJECT_ROOT
REPO = str(PROJECT_ROOT)

from config_loader import (
    get_zotero_api_key,
    get_zotero_user_id,
    get_collection_key,
    get_zotero_dir,
    get_unpaywall_email,
    _ssl_ctx,
)

API_KEY = get_zotero_api_key()
USER_ID = get_zotero_user_id()
ZOTERO_DIR = get_zotero_dir()
UNPAYWALL_EMAIL = get_unpaywall_email()


# ── Logging ──────────────────────────────────────────────────────────────────

def log(msg):
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


# ── Safe filename ─────────────────────────────────────────────────────────────

def safe_filename(title, max_len=80):
    """제목에서 파일 이름에 안전한 문자열 생성."""
    name = re.sub(r'[\\/:*?"<>|]', "", title)
    name = re.sub(r"\s+", " ", name).strip()
    return name[:max_len]


# ── Zotero API ────────────────────────────────────────────────────────────────

def zotero_api(endpoint, method="GET", data=None, params=None):
    """Zotero Web API 호출. JSON 반환."""
    base_url = f"https://api.zotero.org/users/{USER_ID}/{endpoint}"
    if params:
        base_url += "?" + urllib.parse.urlencode(params)

    body = json.dumps(data).encode("utf-8") if data is not None else None
    req = urllib.request.Request(
        base_url,
        data=body,
        method=method,
        headers={
            "Zotero-API-Key": API_KEY,
            "Content-Type": "application/json",
            "User-Agent": "paper-curation/1.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30, context=_ssl_ctx) as resp:
            raw = resp.read()
            if raw:
                return json.loads(raw.decode("utf-8"))
            return {}
    except urllib.error.HTTPError as e:
        body_text = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Zotero API 오류 [{e.code}] {endpoint}: {body_text[:300]}")


def search_zotero_by_title(title):
    """제목 앞 40자로 Zotero 검색. 최대 5건 반환."""
    query = title[:40]
    return zotero_api("items", params={"q": query, "limit": 5, "format": "json"})


def is_duplicate(title, existing_items):
    """기존 아이템 중 제목 앞 30자가 일치하면 중복."""
    prefix = re.sub(r"[^a-z0-9]", "", title.lower())[:30]
    for item in existing_items:
        d = item.get("data", {})
        existing_title = d.get("title", "")
        existing_prefix = re.sub(r"[^a-z0-9]", "", existing_title.lower())[:30]
        if prefix and existing_prefix and prefix == existing_prefix:
            return item["data"]["key"]
    return None


def get_collection_items_all(collection_key):
    """컬렉션의 모든 상위 아이템 반환 (페이지네이션)."""
    items = []
    start = 0
    while True:
        batch = zotero_api(
            f"collections/{collection_key}/items/top",
            params={"limit": 100, "start": start, "format": "json"},
        )
        if not batch:
            break
        items.extend(batch)
        start += 100
        if len(batch) < 100:
            break
        time.sleep(1)
    return items


def get_item_children(item_key):
    """아이템의 자식(첨부파일 등) 반환."""
    try:
        return zotero_api(f"items/{item_key}/children", params={"format": "json"})
    except Exception:
        return []


# ── Author parsing ────────────────────────────────────────────────────────────

def parse_authors(authors_raw):
    """저자 목록을 Zotero creator 형식으로 변환.

    입력 형식:
      - list of str: ["Jane Doe", "John Smith"]
      - list of dict: [{"name": "Jane Doe"}, ...] or [{"firstName": ..., "lastName": ...}]
      - str: "Jane Doe, John Smith"
    """
    creators = []
    if not authors_raw:
        return creators

    if isinstance(authors_raw, str):
        authors_raw = [a.strip() for a in authors_raw.split(",") if a.strip()]

    for author in authors_raw:
        if isinstance(author, dict):
            # 이미 구조화된 경우
            if "lastName" in author or "firstName" in author:
                creators.append({
                    "creatorType": "author",
                    "firstName": author.get("firstName", ""),
                    "lastName": author.get("lastName", ""),
                })
            elif "name" in author:
                name = author["name"].strip()
                parts = name.split()
                creators.append({
                    "creatorType": "author",
                    "firstName": " ".join(parts[:-1]) if len(parts) > 1 else "",
                    "lastName": parts[-1] if parts else name,
                })
        elif isinstance(author, str):
            name = author.strip()
            parts = name.split()
            creators.append({
                "creatorType": "author",
                "firstName": " ".join(parts[:-1]) if len(parts) > 1 else "",
                "lastName": parts[-1] if parts else name,
            })
    return creators


# ── Build Zotero item template ────────────────────────────────────────────────

def build_item_template(paper, collection_key):
    """논문 dict → Zotero API item dict."""
    creators = parse_authors(paper.get("authors") or paper.get("author") or [])

    # Date: prefer year field, fallback to publicationDate / date
    date_val = (
        paper.get("year")
        or paper.get("publicationDate")
        or paper.get("date")
        or ""
    )
    if isinstance(date_val, int):
        date_val = str(date_val)

    doi = paper.get("doi") or paper.get("DOI") or ""
    url = paper.get("url") or paper.get("pdf_url") or ""
    if not url and doi:
        url = f"https://doi.org/{doi}"

    return {
        "itemType": "journalArticle",
        "title": paper.get("title", "").strip(),
        "creators": creators,
        "abstractNote": paper.get("abstract") or paper.get("abstractNote") or "",
        "date": str(date_val),
        "DOI": doi,
        "url": url,
        "collections": [collection_key],
    }


# ── PDF download strategies ───────────────────────────────────────────────────

def _download_url(url, dest_path, min_size=5120):
    """URL에서 파일 다운로드. 5KB 미만이면 오류 페이지로 간주."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30, context=_ssl_ctx) as resp:
            data = resp.read()
        if len(data) < min_size:
            return False, f"파일 크기 너무 작음 ({len(data)} bytes)"
        with open(dest_path, "wb") as f:
            f.write(data)
        return True, ""
    except Exception as e:
        return False, str(e)


def _extract_arxiv_id(paper):
    """논문 dict에서 arXiv ID 추출."""
    arxiv_id = paper.get("arxiv_id") or paper.get("arxivId") or ""
    if not arxiv_id:
        url = paper.get("url") or paper.get("pdf_url") or ""
        doi = paper.get("doi") or ""
        for s in (url, doi):
            m = re.search(r"arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]+)", s)
            if m:
                arxiv_id = m.group(1)
                break
    return arxiv_id


def download_pdf(paper, dest_dir):
    """PDF 다운로드 다중 전략. (경로, 오류메시지) 반환."""
    title = paper.get("title", "unknown")
    fname = safe_filename(title) + ".pdf"
    dest_path = os.path.join(dest_dir, fname)

    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 5120:
        return dest_path, ""

    # 전략 1: arXiv
    arxiv_id = _extract_arxiv_id(paper)
    if arxiv_id:
        arxiv_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
        ok, err = _download_url(arxiv_url, dest_path)
        if ok:
            log(f"    arXiv PDF 다운로드 성공: {arxiv_id}")
            return dest_path, ""
        time.sleep(3)

    # 전략 2: S2 openAccessPdf
    pdf_url = paper.get("openAccessPdf") or paper.get("pdf_url") or ""
    if isinstance(pdf_url, dict):
        pdf_url = pdf_url.get("url", "")
    if pdf_url and pdf_url.endswith(".pdf"):
        ok, err = _download_url(pdf_url, dest_path)
        if ok:
            log(f"    S2 openAccessPdf 다운로드 성공")
            return dest_path, ""

    # 전략 3: Unpaywall
    doi = paper.get("doi") or paper.get("DOI") or ""
    if doi and UNPAYWALL_EMAIL:
        time.sleep(0.5)
        try:
            upw_url = f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi, safe='')}?email={UNPAYWALL_EMAIL}"
            req = urllib.request.Request(upw_url, headers={"User-Agent": "paper-curation/1.0"})
            with urllib.request.urlopen(req, timeout=15, context=_ssl_ctx) as resp:
                upw_data = json.loads(resp.read().decode("utf-8"))
            best = upw_data.get("best_oa_location") or {}
            upw_pdf = best.get("url_for_pdf") or ""
            if upw_pdf:
                ok, err = _download_url(upw_pdf, dest_path)
                if ok:
                    log(f"    Unpaywall PDF 다운로드 성공")
                    return dest_path, ""
        except Exception as e:
            log(f"    Unpaywall 조회 실패: {e}")

    return "", "모든 전략 실패"


# ── Attach PDF to Zotero item ─────────────────────────────────────────────────

def attach_pdf(item_key, pdf_path):
    """PDF를 Zotero 아이템에 linked file로 첨부."""
    fname = os.path.basename(pdf_path)
    # Zotero linked_file path: Windows → 절대경로 그대로 사용
    attachment = {
        "itemType": "attachment",
        "linkMode": "linked_file",
        "title": fname,
        "path": pdf_path,
        "contentType": "application/pdf",
        "parentItem": item_key,
    }
    result = zotero_api("items", method="POST", data=[attachment])
    return result


# ── Step 2: Duplicate check ───────────────────────────────────────────────────

def check_duplicates(papers):
    """각 논문에 대해 Zotero 중복 검사. (new_papers, duplicates) 반환."""
    new_papers = []
    duplicates = []

    log(f"중복 검사 시작: {len(papers)}편")
    for i, paper in enumerate(papers):
        title = paper.get("title", "").strip()
        if not title:
            log(f"  [{i+1}/{len(papers)}] 제목 없음, 건너뜀")
            continue

        try:
            existing = search_zotero_by_title(title)
            dup_key = is_duplicate(title, existing)
            if dup_key:
                log(f"  [{i+1}/{len(papers)}] 중복: {title[:60]}")
                duplicates.append({"title": title, "existing_key": dup_key, "_paper": paper})
            else:
                new_papers.append(paper)
        except Exception as e:
            log(f"  [{i+1}/{len(papers)}] 중복 검사 오류: {e}")
            new_papers.append(paper)  # 오류 시 신규로 처리

        time.sleep(1)  # Zotero rate limit

    log(f"  중복: {len(duplicates)}편, 신규: {len(new_papers)}편")
    return new_papers, duplicates


# ── Step 3: Register items ────────────────────────────────────────────────────

def register_items(papers, collection_key, dry_run=False):
    """신규 논문을 Zotero에 등록. 등록 결과 목록 반환."""
    if not papers:
        return []

    registered = []
    batch_size = 50

    for i in range(0, len(papers), batch_size):
        batch = papers[i:i + batch_size]
        items = [build_item_template(p, collection_key) for p in batch]

        log(f"  Zotero 등록 중: {i+1}~{min(i+len(batch), len(papers))}편")

        if dry_run:
            for p in batch:
                registered.append({
                    "title": p.get("title", ""),
                    "zotero_key": "DRY_RUN",
                    "pdf": False,
                    "_paper": p,
                })
            continue

        try:
            result = zotero_api("items", method="POST", data=items)
            # 결과: {"success": {"0": "KEY1", ...}, "failed": {...}}
            success_map = result.get("success", {})
            failed_map = result.get("failed", {})

            for idx_str, key in success_map.items():
                idx = int(idx_str)
                p = batch[idx]
                registered.append({
                    "title": p.get("title", ""),
                    "zotero_key": key,
                    "pdf": False,
                    "_paper": p,
                })
                log(f"    등록 완료: {p.get('title','')[:60]} → {key}")

            for idx_str, err_info in failed_map.items():
                idx = int(idx_str)
                p = batch[idx]
                log(f"    등록 실패: {p.get('title','')[:60]} | {err_info}")

        except Exception as e:
            log(f"  배치 등록 오류: {e}")

        time.sleep(1)

    return registered


# ── Step 4+5: Download and attach PDFs ───────────────────────────────────────

def download_and_attach(registered, zotero_dir, dry_run=False):
    """등록된 논문 목록에 대해 PDF 다운로드 + Zotero 첨부."""
    failed_pdf = []

    os.makedirs(zotero_dir, exist_ok=True)

    for item in registered:
        title = item["title"]
        key = item["zotero_key"]
        paper = item.get("_paper", {})

        log(f"  PDF 다운로드 시도: {title[:60]}")

        if dry_run:
            log(f"    [dry-run] 건너뜀")
            continue

        pdf_path, err = download_pdf(paper, zotero_dir)
        if pdf_path:
            item["pdf"] = True
            item["pdf_path"] = pdf_path
            if key != "DRY_RUN":
                try:
                    attach_pdf(key, pdf_path)
                    log(f"    첨부 완료: {os.path.basename(pdf_path)}")
                except Exception as e:
                    log(f"    첨부 오류: {e}")
            time.sleep(1)
        else:
            log(f"    PDF 실패: {err}")
            failed_pdf.append({
                "title": title,
                "zotero_key": key,
                "reason": err,
            })

    return failed_pdf


# ── Step 6: --fix-pdfs mode ───────────────────────────────────────────────────

def fix_pdfs(collection_key, zotero_dir, dry_run=False):
    """PDF 없는 아이템 찾아 재시도."""
    log(f"컬렉션 아이템 전체 조회 중...")
    items = get_collection_items_all(collection_key)
    log(f"  총 {len(items)}편")

    missing = []
    for item in items:
        d = item.get("data", {})
        if d.get("itemType") in ("attachment", "note"):
            continue
        key = d["key"]
        children = get_item_children(key)
        has_pdf = any(
            c.get("data", {}).get("itemType") == "attachment"
            and c.get("data", {}).get("contentType") == "application/pdf"
            for c in children
        )
        if not has_pdf:
            missing.append(item)
        time.sleep(0.5)

    log(f"  PDF 없는 아이템: {len(missing)}편")

    os.makedirs(zotero_dir, exist_ok=True)
    success_count = 0
    failed_pdf = []

    for item in missing:
        d = item["data"]
        title = d.get("title", "")
        key = d["key"]
        doi = d.get("DOI") or d.get("doi") or ""
        url_field = d.get("url", "")

        # Reconstruct minimal paper dict
        paper = {
            "title": title,
            "doi": doi,
            "url": url_field,
        }
        # Try to extract arXiv from URL
        if "arxiv.org/abs/" in url_field:
            arxiv_id = url_field.split("arxiv.org/abs/")[-1].split("v")[0]
            paper["arxiv_id"] = arxiv_id

        log(f"  재시도: {title[:60]}")

        if dry_run:
            log(f"    [dry-run] 건너뜀")
            continue

        pdf_path, err = download_pdf(paper, zotero_dir)
        if pdf_path:
            try:
                attach_pdf(key, pdf_path)
                log(f"    첨부 완료: {os.path.basename(pdf_path)}")
                success_count += 1
            except Exception as e:
                log(f"    첨부 오류: {e}")
        else:
            log(f"    PDF 실패: {err}")
            failed_pdf.append({"title": title, "zotero_key": key, "reason": err})

        time.sleep(3)

    log(f"\nPDF 재시도 완료: {success_count}/{len(missing)} 성공")
    return success_count, len(missing), failed_pdf


# ── Save results ──────────────────────────────────────────────────────────────

def save_results(topic, registered, duplicates, failed_pdf):
    topic_dir = str(get_topic_dir(topic))
    out_path = os.path.join(topic_dir, "_register_results.json")
    os.makedirs(topic_dir, exist_ok=True)

    # _paper 필드 제거 (내부 전용)
    clean_registered = [
        {k: v for k, v in r.items() if k != "_paper"}
        for r in registered
    ]
    clean_duplicates = [
        {k: v for k, v in d.items() if k != "_paper"}
        for d in duplicates
    ]

    data = {
        "registered": clean_registered,
        "duplicates": clean_duplicates,
        "failed_pdf": failed_pdf,
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return out_path


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Zotero 논문 등록 + PDF 첨부")
    parser.add_argument("--topic", required=True, help="토픽 (ai4s 또는 scisci)")
    parser.add_argument("--input", help="검색 결과 JSON 경로 (기본: {topic}/_search_results.json)")
    parser.add_argument("--fix-pdfs", action="store_true", help="PDF 없는 아이템에 대해 재시도")
    parser.add_argument("--dry-run", action="store_true", help="실제 등록/다운로드 없이 미리 보기")
    args = parser.parse_args()

    topic = args.topic
    collection_key = get_collection_key(topic)
    if not collection_key:
        print(f"오류: 토픽 '{topic}'에 대한 컬렉션 키를 찾을 수 없습니다.")
        return

    zotero_dir = ZOTERO_DIR or os.path.join(str(get_topic_dir(topic)), "_pdfs")

    # ── --fix-pdfs 모드 ──
    if args.fix_pdfs:
        log(f"=== PDF 재시도 모드: {topic} ===")
        if args.dry_run:
            log("[dry-run 모드]")
        success, total, failed = fix_pdfs(collection_key, zotero_dir, dry_run=args.dry_run)
        print(f"\nZotero PDF 재시도 완료: {topic}")
        print(f"  대상: {total}편")
        print(f"  성공: {success}편")
        print(f"  실패: {len(failed)}편")
        return

    # ── 일반 등록 모드 ──
    input_path = args.input or os.path.join(str(get_topic_dir(topic)), "_search_results.json")
    if not os.path.exists(input_path):
        print(f"오류: 검색 결과 파일이 없습니다: {input_path}")
        return

    log(f"=== Zotero 등록 시작: {topic} ===")
    if args.dry_run:
        log("[dry-run 모드: 실제 등록/다운로드 없음]")

    # Step 1: 입력 로드
    with open(input_path, "r", encoding="utf-8") as f:
        papers = json.load(f)
    log(f"입력 논문: {len(papers)}편")

    # Step 2: 중복 검사
    new_papers, duplicates = check_duplicates(papers)

    # Step 3: Zotero 등록
    log(f"\n신규 등록: {len(new_papers)}편")
    registered = register_items(new_papers, collection_key, dry_run=args.dry_run)

    # Step 4+5: PDF 다운로드 + 첨부
    log(f"\nPDF 다운로드 + 첨부 시작")
    failed_pdf = download_and_attach(registered, zotero_dir, dry_run=args.dry_run)

    # Step 6: 결과 저장
    out_path = save_results(topic, registered, duplicates, failed_pdf)

    # 요약 출력
    pdf_success = sum(1 for r in registered if r.get("pdf"))
    print(f"\nZotero 등록 완료: {topic}")
    print(f"  입력: {len(papers)}편")
    print(f"  중복 (건너뜀): {len(duplicates)}편")
    print(f"  신규 등록: {len(registered)}편")
    print(f"  PDF 다운로드: {pdf_success}/{len(registered)} 성공")
    if failed_pdf:
        print(f"  PDF 실패: {len(failed_pdf)}편 (수동 다운로드 필요)")
    print(f"  결과: {out_path}")


if __name__ == "__main__":
    main()
