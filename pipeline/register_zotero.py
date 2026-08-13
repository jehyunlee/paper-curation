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
from lib.bib_enrich import enrich as enrich_bib, to_zotero_item

# Zotero 자격증명은 호출 지점에서 해석한다 (import 시 키 요구·네트워크 왕복 없음).
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
    base_url = f"https://api.zotero.org/users/{get_zotero_user_id()}/{endpoint}"
    if params:
        base_url += "?" + urllib.parse.urlencode(params)

    body = json.dumps(data).encode("utf-8") if data is not None else None
    req = urllib.request.Request(
        base_url,
        data=body,
        method=method,
        headers={
            "Zotero-API-Key": get_zotero_api_key(),
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
    """논문 dict → Zotero API item dict.

    arXiv ID / DOI 가 있으면 arXiv API + CrossRef 로 enrichment 후
    publicationTitle, volume, issue, pages, ISSN, archiveID 등까지 채운다.
    Zotero Wizard 와 동일한 수준.
    """
    enriched = enrich_bib(paper, mailto=UNPAYWALL_EMAIL)
    return to_zotero_item(enriched, collection_key=collection_key)


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
        doi = paper.get("doi") or paper.get("DOI") or ""
        archive_id = paper.get("archiveID", "") or paper.get("archive_id", "")
        for s in (url, doi, archive_id):
            if not s:
                continue
            # 표준 arXiv URL: arxiv.org/abs/2404.18400 or /pdf/ or /html/
            m = re.search(r"arxiv\.org/(?:abs|pdf|html)/([0-9]{4}\.[0-9]{4,5})",
                           str(s), re.IGNORECASE)
            if m:
                arxiv_id = m.group(1)
                break
            # arXiv DOI 형식: 10.48550/arXiv.2404.18400 (대소문자 무관)
            m = re.search(r"10\.48550/arxiv\.([0-9]{4}\.[0-9]{4,5})",
                           str(s), re.IGNORECASE)
            if m:
                arxiv_id = m.group(1)
                break
            # archiveID 형식: "arXiv:2404.18400"
            m = re.search(r"arxiv\s*:\s*([0-9]{4}\.[0-9]{4,5})",
                           str(s), re.IGNORECASE)
            if m:
                arxiv_id = m.group(1)
                break
    return arxiv_id


def _try_crossref_pdf_url(doi):
    """CrossRef link[] 배열에서 PDF URL 추출. 없으면 빈문자열."""
    if not doi:
        return ""
    safe = urllib.parse.quote(doi.strip(), safe="")
    url = f"https://api.crossref.org/works/{safe}"
    ua = "paper-curation/1.0"
    if UNPAYWALL_EMAIL:
        ua += f" (mailto:{UNPAYWALL_EMAIL})"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": ua})
        with urllib.request.urlopen(req, timeout=15, context=_ssl_ctx) as resp:
            msg = json.loads(resp.read()).get("message", {})
    except Exception:
        return ""
    # PDF content-type 우선
    for link in msg.get("link", []):
        if "pdf" in (link.get("content-type") or "").lower():
            return link.get("URL") or ""
    # content-type 없는 경우라도 .pdf 확장자
    for link in msg.get("link", []):
        u = link.get("URL") or ""
        if u.lower().endswith(".pdf"):
            return u
    return ""


def _try_semanticscholar_pdf_url(doi="", arxiv_id=""):
    """Semantic Scholar live 조회로 openAccessPdf URL 획득."""
    if arxiv_id:
        spec = f"ArXiv:{arxiv_id}"
    elif doi:
        spec = f"DOI:{doi}"
    else:
        return ""
    url = (f"https://api.semanticscholar.org/graph/v1/paper/"
           f"{urllib.parse.quote(spec, safe=':')}?fields=openAccessPdf")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "paper-curation/1.0"})
        with urllib.request.urlopen(req, timeout=15, context=_ssl_ctx) as resp:
            data = json.loads(resp.read())
    except Exception:
        return ""
    oa = data.get("openAccessPdf") or {}
    if isinstance(oa, dict):
        return oa.get("url") or ""
    return ""


def _try_openalex_pdf_url(doi):
    """OpenAlex 에서 best_oa_location.pdf_url 추출."""
    if not doi:
        return ""
    url = f"https://api.openalex.org/works/doi:{urllib.parse.quote(doi.strip(), safe='/')}"
    if UNPAYWALL_EMAIL:
        url += f"?mailto={UNPAYWALL_EMAIL}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "paper-curation/1.0"})
        with urllib.request.urlopen(req, timeout=15, context=_ssl_ctx) as resp:
            data = json.loads(resp.read())
    except Exception:
        return ""
    best = data.get("best_oa_location") or {}
    if isinstance(best, dict) and best.get("pdf_url"):
        return best["pdf_url"]
    # primary location 폴백
    prim = data.get("primary_location") or {}
    if isinstance(prim, dict) and prim.get("pdf_url"):
        return prim["pdf_url"]
    return ""


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

    # 전략 2: S2 openAccessPdf 캐시 (paper dict 에 이미 있는 경우)
    pdf_url = paper.get("openAccessPdf") or paper.get("pdf_url") or ""
    if isinstance(pdf_url, dict):
        pdf_url = pdf_url.get("url", "")
    if pdf_url and pdf_url.endswith(".pdf"):
        ok, err = _download_url(pdf_url, dest_path)
        if ok:
            log(f"    S2 openAccessPdf (cached) 다운로드 성공")
            return dest_path, ""

    doi = paper.get("doi") or paper.get("DOI") or ""

    # 전략 3: CrossRef link[] 직접 PDF URL
    if doi:
        time.sleep(0.3)
        cr_pdf = _try_crossref_pdf_url(doi)
        if cr_pdf:
            ok, err = _download_url(cr_pdf, dest_path)
            if ok:
                log(f"    CrossRef link 다운로드 성공")
                return dest_path, ""

    # 전략 4: Semantic Scholar live 조회
    if arxiv_id or doi:
        time.sleep(0.3)
        s2_pdf = _try_semanticscholar_pdf_url(doi=doi, arxiv_id=arxiv_id)
        if s2_pdf:
            ok, err = _download_url(s2_pdf, dest_path)
            if ok:
                log(f"    Semantic Scholar 다운로드 성공")
                return dest_path, ""

    # 전략 5: Unpaywall
    if doi and UNPAYWALL_EMAIL:
        time.sleep(0.3)
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
                    log(f"    Unpaywall 다운로드 성공")
                    return dest_path, ""
        except Exception as e:
            log(f"    Unpaywall 조회 실패: {e}")

    # 전략 6: OpenAlex
    if doi:
        time.sleep(0.3)
        oa_pdf = _try_openalex_pdf_url(doi)
        if oa_pdf:
            ok, err = _download_url(oa_pdf, dest_path)
            if ok:
                log(f"    OpenAlex 다운로드 성공")
                return dest_path, ""

    return "", "모든 전략 실패 (arXiv/CrossRef/S2/Unpaywall/OpenAlex)"


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


# ── Step 6b: --fix-metadata mode ──────────────────────────────────────────────

# Zotero fields that the Wizard fills but our older registrations often missed.
_RICH_FIELDS = (
    "publicationTitle", "volume", "issue", "pages", "ISSN", "publisher",
    "abstractNote", "archiveID", "repository",
)


def _is_metadata_thin(d):
    """기존 아이템의 metadata 가 부실한지 판단 (저널/preprint 모두 커버).

    journalArticle: publicationTitle 비어 있거나 abstractNote 빔.
    preprint: archiveID 비어 있거나 abstractNote 빔.
    """
    it = d.get("itemType", "")
    if it == "journalArticle":
        if not d.get("publicationTitle") or not d.get("abstractNote"):
            return True
    elif it == "preprint":
        if not d.get("archiveID") or not d.get("abstractNote"):
            return True
    if not d.get("creators"):
        return True
    return False


def _patch_item(item_key, version, patch):
    """단일 아이템 PATCH. version 은 If-Unmodified-Since-Version 헤더로."""
    base_url = f"https://api.zotero.org/users/{get_zotero_user_id()}/items/{item_key}"
    body = json.dumps(patch).encode("utf-8")
    req = urllib.request.Request(
        base_url, data=body, method="PATCH",
        headers={
            "Zotero-API-Key": get_zotero_api_key(),
            "Content-Type": "application/json",
            "If-Unmodified-Since-Version": str(version),
            "User-Agent": "paper-curation/1.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30, context=_ssl_ctx) as resp:
            return True, ""
    except urllib.error.HTTPError as e:
        body_text = e.read().decode("utf-8", errors="replace")
        return False, f"[{e.code}] {body_text[:200]}"
    except Exception as e:
        return False, str(e)


def fix_metadata(collection_key, dry_run=False, limit=None):
    """기존 컬렉션 아이템 중 metadata 부실한 항목을 enrich 후 PATCH."""
    log("컬렉션 아이템 전체 조회 중...")
    items = get_collection_items_all(collection_key)
    log(f"  총 {len(items)}편")

    targets = [it for it in items
               if it.get("data", {}).get("itemType") not in ("attachment", "note")
               and _is_metadata_thin(it["data"])]
    log(f"  metadata 부실 후보: {len(targets)}편")
    if limit:
        targets = targets[:limit]
        log(f"  --limit 적용: {len(targets)}편만 처리")

    success = skip = failed = 0
    fail_log = []

    for i, it in enumerate(targets):
        d = it["data"]
        key = d["key"]
        version = it.get("version") or d.get("version")
        title = d.get("title", "")[:60]

        # Reconstruct minimal paper dict from existing fields
        paper = {
            "title": d.get("title", ""),
            "doi": d.get("DOI") or "",
            "url": d.get("url", ""),
            "authors": [
                {"firstName": c.get("firstName", ""), "lastName": c.get("lastName", "")}
                for c in d.get("creators", [])
                if c.get("creatorType") == "author"
            ],
            "abstract": d.get("abstractNote", ""),
            "date": d.get("date", ""),
        }

        try:
            enriched = enrich_bib(paper, mailto=UNPAYWALL_EMAIL)
        except Exception as e:
            log(f"  [{i+1}/{len(targets)}] {title}: enrich 실패 — {e}")
            failed += 1
            fail_log.append({"key": key, "title": title, "reason": f"enrich: {e}"})
            continue

        # Zotero itemType별 사용 가능 필드 (preprint는 publisher 없음 → repository로)
        cur_type = d.get("itemType", "")
        invalid_for_type = set()
        if cur_type == "preprint":
            invalid_for_type.update({"publisher", "publicationTitle", "volume",
                                      "issue", "pages", "ISSN"})

        # Build PATCH body — only fields currently empty in Zotero
        patch = {}
        for field in _RICH_FIELDS:
            if field in invalid_for_type:
                continue
            if not d.get(field) and enriched.get(field):
                patch[field] = str(enriched[field])
        # preprint 인데 CrossRef publisher 가 있으면 repository 로 (비어있을 때만)
        if cur_type == "preprint" and not d.get("repository") and enriched.get("publisher"):
            patch["repository"] = str(enriched["publisher"])
        if not d.get("creators") and enriched.get("authors"):
            from lib.bib_enrich import _parse_authors as _pa  # local helper reuse
            patch["creators"] = _pa(enriched["authors"])
        # date: if existing date is just year and CrossRef has full YYYY-MM-DD
        new_date = enriched.get("date", "")
        if new_date and len(new_date) > len(d.get("date", "")):
            patch["date"] = new_date
        # itemType promotion: arXiv ID 발견했는데 journalArticle 인 경우 → preprint
        if (enriched.get("arxiv_id") and d.get("itemType") == "journalArticle"
                and not d.get("DOI")):
            patch["itemType"] = "preprint"
            patch["archiveID"] = f"arXiv:{enriched['arxiv_id']}"
            patch["repository"] = "arXiv"

        if not patch:
            skip += 1
            continue

        log(f"  [{i+1}/{len(targets)}] {title}: patching {list(patch.keys())}")

        if dry_run:
            success += 1
            continue

        ok, err = _patch_item(key, version, patch)
        if ok:
            success += 1
        else:
            failed += 1
            log(f"    PATCH 실패: {err}")
            fail_log.append({"key": key, "title": title, "reason": err})

        time.sleep(0.5)

    log(f"\nMetadata 보강 완료: success={success}, skip={skip}, failed={failed}")
    return success, skip, failed, fail_log


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

        # Reconstruct paper dict — Zotero archiveID/extra 까지 활용해
        # arXiv ID 가 강력하게 추출되도록 한다.
        paper = {
            "title": title,
            "doi": doi,
            "url": url_field,
            "archiveID": d.get("archiveID", ""),
        }
        ax = _extract_arxiv_id(paper)
        if ax:
            paper["arxiv_id"] = ax

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

def _run_register(topic, *, input_path=None, dry_run=False):
    """Programmatic entrypoint for register_zotero (normal register mode)."""
    collection_key = get_collection_key(topic)
    if not collection_key:
        print(f"오류: 토픽 '{topic}'에 대한 컬렉션 키를 찾을 수 없습니다.")
        return None

    zotero_dir = ZOTERO_DIR or os.path.join(str(get_topic_dir(topic)), "_pdfs")
    input_path = input_path or os.path.join(str(get_topic_dir(topic)), "_search_results.json")
    if not os.path.exists(input_path):
        print(f"오류: 검색 결과 파일이 없습니다: {input_path}")
        return None

    log(f"=== Zotero 등록 시작: {topic} ===")
    if dry_run:
        log("[dry-run 모드: 실제 등록/다운로드 없음]")

    with open(input_path, "r", encoding="utf-8") as f:
        papers = json.load(f)
    log(f"입력 논문: {len(papers)}편")

    new_papers, duplicates = check_duplicates(papers)

    log(f"\n신규 등록: {len(new_papers)}편")
    registered = register_items(new_papers, collection_key, dry_run=dry_run)

    log(f"\nPDF 다운로드 + 첨부 시작")
    failed_pdf = download_and_attach(registered, zotero_dir, dry_run=dry_run)

    out_path = save_results(topic, registered, duplicates, failed_pdf)

    pdf_success = sum(1 for r in registered if r.get("pdf"))
    print(f"\nZotero 등록 완료: {topic}")
    print(f"  입력: {len(papers)}편")
    print(f"  중복 (건너뜀): {len(duplicates)}편")
    print(f"  신규 등록: {len(registered)}편")
    print(f"  PDF 다운로드: {pdf_success}/{len(registered)} 성공")
    if failed_pdf:
        print(f"  PDF 실패: {len(failed_pdf)}편 (수동 다운로드 필요)")
    print(f"  결과: {out_path}")
    return {"registered": len(registered), "duplicates": len(duplicates),
            "pdf_success": pdf_success, "pdf_failed": len(failed_pdf),
            "out_path": out_path}


def _run_fix_pdfs(topic, *, dry_run=False):
    """Programmatic entrypoint for register_zotero --fix-pdfs mode."""
    collection_key = get_collection_key(topic)
    if not collection_key:
        print(f"오류: 토픽 '{topic}'에 대한 컬렉션 키를 찾을 수 없습니다.")
        return None
    zotero_dir = ZOTERO_DIR or os.path.join(str(get_topic_dir(topic)), "_pdfs")
    log(f"=== PDF 재시도 모드: {topic} ===")
    if dry_run:
        log("[dry-run 모드]")
    success, total, failed = fix_pdfs(collection_key, zotero_dir, dry_run=dry_run)
    print(f"\nZotero PDF 재시도 완료: {topic}")
    print(f"  대상: {total}편")
    print(f"  성공: {success}편")
    print(f"  실패: {len(failed)}편")
    return {"success": success, "total": total, "failed": failed}


def _run_fix_metadata(topic, *, dry_run=False, limit=None):
    """Programmatic entrypoint for register_zotero --fix-metadata mode."""
    collection_key = get_collection_key(topic)
    if not collection_key:
        print(f"오류: 토픽 '{topic}'에 대한 컬렉션 키를 찾을 수 없습니다.")
        return None
    log(f"=== Metadata 보강 모드: {topic} ===")
    if dry_run:
        log("[dry-run 모드]")
    success, skip, failed, fail_log = fix_metadata(
        collection_key, dry_run=dry_run, limit=limit,
    )
    print(f"\nZotero metadata 보강 완료: {topic}")
    print(f"  보강 (PATCH): {success}편")
    print(f"  변경 없음 (skip): {skip}편")
    print(f"  실패: {failed}편")
    if fail_log:
        out_path = os.path.join(str(get_topic_dir(topic)),
                                 "_fix_metadata_failures.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(fail_log, f, ensure_ascii=False, indent=2)
        print(f"  실패 로그: {out_path}")
    return {"success": success, "skip": skip, "failed": failed}


def main():
    parser = argparse.ArgumentParser(description="Zotero 논문 등록 + PDF 첨부")
    parser.add_argument("--topic", required=True, help="토픽 (ai4s 또는 scisci)")
    parser.add_argument("--input", help="검색 결과 JSON 경로 (기본: {topic}/_search_results.json)")
    parser.add_argument("--fix-pdfs", action="store_true", help="PDF 없는 아이템에 대해 재시도")
    parser.add_argument("--fix-metadata", action="store_true",
                        help="기존 아이템 중 publicationTitle/abstract 등이 비어있는 경우 arXiv+CrossRef 로 보강")
    parser.add_argument("--limit", type=int, default=None,
                        help="--fix-metadata 처리 상한 (테스트용)")
    parser.add_argument("--dry-run", action="store_true", help="실제 등록/다운로드 없이 미리 보기")
    args = parser.parse_args()

    if args.fix_metadata:
        _run_fix_metadata(topic=args.topic, dry_run=args.dry_run, limit=args.limit)
    elif args.fix_pdfs:
        _run_fix_pdfs(topic=args.topic, dry_run=args.dry_run)
    else:
        _run_register(topic=args.topic, input_path=args.input, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
