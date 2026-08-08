"""import_references — 학술 도서의 참고문헌 텍스트를 Zotero 컬렉션에 일괄 등록.

워크플로우
1. Parse (Haiku):   reference.txt 의 각 항목을 type/title/authors/year/...
                    구조화 JSON 으로 변환.
2. Resolve:         journalArticle → CrossRef title 검색으로 DOI 확보
                    book → Open Library / Google Books 로 ISBN + 메타 보강
                    bookSection → CrossRef + 파싱 필드 병합.
3. Enrich:          DOI 가 있으면 lib.bib_enrich.enrich() 로 풍성한 메타 채움
                    (CrossRef wizard 수준).
4. Dedup:           내부 중복 제거 (DOI/ISBN/제목+저자+연도)
                    + 기존 Zotero 컬렉션과 비교 후 중복 제거.
5. Register:        Zotero API 로 컬렉션에 일괄 POST (50개 batch).
6. PDF:             journalArticle 대상으로 Unpaywall/CrossRef/S2/OpenAlex
                    경로 PDF 다운로드 + Zotero 첨부.
7. Report:          registered.json / duplicates.json / unmatched.txt /
                    skipped.txt 를 .cache/import_references/ 에 저장.

사용
  PYTHONUTF8=1 python pipeline/import_references.py \
      --input reference.txt \
      --collection scisci \
      --dry-run

  # 실제 등록
  PYTHONUTF8=1 python pipeline/import_references.py \
      --input reference.txt \
      --collection scisci

플래그
  --skip-pdf       PDF 다운로드 건너뜀
  --no-cache       기존 캐시 무시하고 재파싱·재해상
  --limit N        앞 N 개만 처리 (테스트용)
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

PIPELINE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(PIPELINE_DIR))

from config_loader import (  # noqa: E402
    PROJECT_ROOT,
    get_collection_key,
    get_unpaywall_email,
    get_zotero_api_key,
    get_zotero_dir,
    get_zotero_user_id,
)
from lib.bib_enrich import enrich as enrich_bib  # noqa: E402
from lib.bib_enrich import to_zotero_item  # noqa: E402
from register_zotero import (  # noqa: E402
    _patch_item,
    attach_pdf,
    download_pdf,
    get_collection_items_all,
    get_item_children,
    zotero_api,
)

# ──────────────────────────────────────────────────────────────────────────────
# Constants & utilities
# ──────────────────────────────────────────────────────────────────────────────

CACHE_DIR = PROJECT_ROOT / ".cache" / "import_references"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

PARSED_CACHE = CACHE_DIR / "parsed.json"
RESOLVED_CACHE = CACHE_DIR / "resolved.json"
REPORT_DIR = CACHE_DIR

UNPAYWALL_EMAIL = get_unpaywall_email() or "noreply@example.com"
USER_AGENT = f"paper-curation/1.0 (mailto:{UNPAYWALL_EMAIL})"
_SSL = ssl.create_default_context()


def log(msg: str) -> None:
    print(msg, flush=True)


def _http_json(url: str, headers: dict | None = None, timeout: int = 25) -> Any:
    h = {"User-Agent": USER_AGENT}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, headers=h)
    with urllib.request.urlopen(req, timeout=timeout, context=_SSL) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _norm(text: str) -> str:
    """제목 비교용 정규화: 영숫자만, 소문자."""
    return re.sub(r"[^a-z0-9]", "", (text or "").lower())


def _save_json(path: Path, data: Any) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)


# ──────────────────────────────────────────────────────────────────────────────
# Step 1: Parse references with Haiku
# ──────────────────────────────────────────────────────────────────────────────

PARSE_SYSTEM_PROMPT = """학술 참고문헌 목록을 JSON으로 파싱하는 전문가다.
각 항목을 정확히 분류하고 메타데이터를 추출하라."""

PARSE_USER_TEMPLATE = """다음은 학술 도서의 참고문헌 목록이다. 각 항목을 JSON 객체로 변환해 array로 출력하라.

각 객체의 필드:
- ref_num: 항목 번호 (정수)
- type: "journalArticle" | "book" | "bookSection" | "skip"
  · "skip" 사례: 사전, 백과사전(Britannica/Stanford Encyclopedia 등), 단일 웹페이지, 정부 데이터베이스, Forthcoming, 작업보고서(Working Paper), 단순 뉴스기사, FRED 같은 데이터 카탈로그
  · CrossRef/ISBN 으로 찾을 수 없을 가능성이 높으면 skip
- title: 논문/책/챕터 제목 (책 부제는 ":"로 연결, 끝 마침표 제거)
- authors: [{"firstName": "...", "lastName": "..."}]  (et al. 무시, 최대 8명)
- year: "2023" 형식 4자리. 재출판 연도가 있으면 가장 최근 연도. 없으면 빈 문자열
- journalArticle 추가: journal (발행지명), volume, issue, pages
- book 추가: publisher, place (출판도시), edition (예: "2nd", "3rd"; 없으면 빈), language ("en"|"de"|...)
- bookSection 추가: editors [{"firstName","lastName"}], bookTitle, publisher, place, pages, edition

규칙:
- "Cambridge: Cambridge University Press" 형식이면 place="Cambridge", publisher="Cambridge University Press"
- "London: Routledge, 2nd ed. (2002)" → edition="2nd"
- 챕터: "In: Editor (eds), Book Title. ..." 패턴
- 한국어로 추정 / 변환하지 말고 원문 그대로 유지

JSON array 외의 텍스트(설명, 마크다운 fence)는 절대 출력하지 마라. 첫 글자는 '['.

참고문헌:
{REFS}"""


def parse_with_haiku(refs: list[str], anthropic_key: str, batch_size: int = 30) -> list[dict]:
    """Haiku 로 batch 단위로 참고문헌 파싱 (OpenRouter 우선)."""
    from lib.llm_client import get_chat_client, resolve_model

    client = get_chat_client(api_key=anthropic_key or None, timeout=180.0, max_retries=3)
    results: list[dict] = []
    total_batches = (len(refs) + batch_size - 1) // batch_size

    for bi in range(total_batches):
        batch = refs[bi * batch_size : (bi + 1) * batch_size]
        prompt = PARSE_USER_TEMPLATE.replace("{REFS}", "\n".join(batch))
        log(f"  Parse batch {bi+1}/{total_batches} ({len(batch)} entries)…")

        # 짧은 리트라이
        for attempt in range(3):
            try:
                resp = client.messages.create(
                    model=resolve_model("haiku"),
                    max_tokens=8000,
                    system=PARSE_SYSTEM_PROMPT,
                    messages=[{"role": "user", "content": prompt}],
                )
                text = resp.content[0].text.strip()
                # ``` fence 제거
                text = re.sub(r"^```(?:json)?\s*", "", text)
                text = re.sub(r"\s*```\s*$", "", text)
                # JSON array 만 남기기
                m = re.search(r"\[.*\]", text, re.DOTALL)
                if m:
                    text = m.group(0)
                chunk = json.loads(text)
                if not isinstance(chunk, list):
                    raise ValueError("not a list")
                results.extend(chunk)
                break
            except Exception as e:
                log(f"    재시도 {attempt+1}/3: {e}")
                time.sleep(2 ** attempt)
        else:
            log(f"  ⚠ batch {bi+1} 파싱 실패 — 건너뜀")

        time.sleep(0.5)
    return results


# ──────────────────────────────────────────────────────────────────────────────
# Step 2: Resolve identifiers (DOI / ISBN)
# ──────────────────────────────────────────────────────────────────────────────


# parsed type → 허용 가능한 CrossRef type set
_ALLOWED_CR_TYPES = {
    "journalArticle": {"journal-article", "report"},
    "book": {"book", "monograph", "edited-book", "reference-book"},
    "bookSection": {"book-chapter", "reference-entry", "book-section"},
}


def find_doi_by_title(
    title: str,
    authors: list[dict],
    year: str | None,
    parsed_type: str | None = None,
    year_tolerance: int = 2,
) -> str | None:
    """CrossRef title+author 검색 → 신뢰 가능한 매치만 DOI 반환.

    parsed_type 이 주어지면 CrossRef 결과의 'type' 도 같은 그룹이어야 한다.
    (책에 대한 리뷰/논문이 같은 제목으로 매칭되는 false-positive 방지.)
    """
    if not title:
        return None
    params = {"query.title": title, "rows": "5"}
    if authors:
        params["query.author"] = " ".join(
            (a.get("lastName") or "").strip() for a in authors[:2] if a.get("lastName")
        )
    qs = urllib.parse.urlencode(params)
    url = f"https://api.crossref.org/works?{qs}"
    try:
        data = _http_json(url, timeout=25)
    except Exception:
        return None
    items = data.get("message", {}).get("items", [])
    if not items:
        return None

    target = _norm(title)[:50]
    if not target:
        return None
    allowed = _ALLOWED_CR_TYPES.get(parsed_type) if parsed_type else None

    for it in items:
        # type 검증 (있을 때만)
        if allowed and (it.get("type") or "") not in allowed:
            continue
        cand_title = (it.get("title") or [""])[0]
        cand = _norm(cand_title)[:50]
        if not cand:
            continue
        # 양방향 prefix 일치 (40자) — 부제 포함/누락 양쪽 허용
        if not (target[:40] == cand[:40] or target[:30] in cand or cand[:30] in target):
            continue
        # Year 검증 (있을 때만, 기본 ±2년; 책은 재출판 고려해 더 관대)
        try:
            it_year = ((it.get("issued") or {}).get("date-parts") or [[None]])[0][0]
            if year and it_year and abs(int(it_year) - int(year)) > year_tolerance:
                continue
        except Exception:
            pass
        doi = it.get("DOI")
        if doi:
            return doi
    return None


def fetch_openlibrary(title: str, authors: list[dict], year: str | None) -> dict | None:
    """Open Library 검색 → 책 메타데이터(ISBN 포함). 실패 시 None."""
    if not title:
        return None
    params = {"title": title, "limit": "5"}
    if authors:
        last = " ".join(
            (a.get("lastName") or "").strip() for a in authors[:2] if a.get("lastName")
        )
        if last:
            params["author"] = last
    qs = urllib.parse.urlencode(params)
    url = f"https://openlibrary.org/search.json?{qs}"
    try:
        data = _http_json(url, timeout=25)
    except Exception:
        return None

    target = _norm(title)[:40]
    for doc in data.get("docs") or []:
        cand = _norm(doc.get("title") or "")[:40]
        if not cand:
            continue
        if not (target[:30] in cand or cand[:30] in target):
            continue
        # 연도 ±5 (개정판 차이 허용)
        first_year = doc.get("first_publish_year") or 0
        if year and first_year:
            try:
                if abs(int(year) - int(first_year)) > 30:
                    continue
            except Exception:
                pass
        return {
            "title": doc.get("title", title),
            "authors_ext": [
                {"firstName": " ".join(n.split()[:-1]), "lastName": n.split()[-1]}
                for n in (doc.get("author_name") or [])
                if n
            ][:8],
            "publisher": (doc.get("publisher") or [""])[0] if doc.get("publisher") else "",
            "place": (doc.get("publish_place") or [""])[0] if doc.get("publish_place") else "",
            "ISBN": next(iter(doc.get("isbn") or []), ""),
            "year_ext": str(doc.get("first_publish_year") or ""),
            "language": (doc.get("language") or ["eng"])[0],
            "numPages": doc.get("number_of_pages_median"),
            "_source": "openlibrary",
        }
    return None


def fetch_googlebooks(title: str, authors: list[dict], year: str | None) -> dict | None:
    """Google Books 검색 → 책 메타데이터(ISBN 포함). Open Library 실패 시 폴백."""
    if not title:
        return None
    parts = [f'intitle:"{title}"']
    for a in (authors or [])[:2]:
        ln = (a.get("lastName") or "").strip()
        if ln:
            parts.append(f"inauthor:{ln}")
    q = "+".join(urllib.parse.quote_plus(p) for p in parts)
    url = f"https://www.googleapis.com/books/v1/volumes?q={q}&maxResults=5"
    try:
        data = _http_json(url, timeout=25)
    except Exception:
        return None

    target = _norm(title)[:40]
    for it in data.get("items") or []:
        info = it.get("volumeInfo", {})
        cand = _norm(info.get("title") or "")[:40]
        if not (target[:30] in cand or cand[:30] in target):
            continue
        ident = info.get("industryIdentifiers") or []
        isbn13 = next((x.get("identifier") for x in ident if x.get("type") == "ISBN_13"), "")
        isbn10 = next((x.get("identifier") for x in ident if x.get("type") == "ISBN_10"), "")
        pub_date = info.get("publishedDate", "")
        return {
            "title": info.get("title", title),
            "authors_ext": [
                {
                    "firstName": " ".join(n.split()[:-1]),
                    "lastName": n.split()[-1] if n.split() else n,
                }
                for n in (info.get("authors") or [])
            ][:8],
            "publisher": info.get("publisher", ""),
            "place": "",
            "ISBN": isbn13 or isbn10,
            "year_ext": pub_date[:4],
            "language": info.get("language", "en"),
            "numPages": info.get("pageCount"),
            "abstract": (info.get("description") or "")[:1500],
            "_source": "googlebooks",
        }
    return None


def resolve_one(parsed: dict, mailto: str) -> dict:
    """하나의 파싱 결과를 외부 검색으로 보강. 결과 dict 에 doi/ISBN 등 추가."""
    out = dict(parsed)
    typ = parsed.get("type")
    title = parsed.get("title", "")
    authors = parsed.get("authors", []) or []
    year = parsed.get("year") or None

    if typ == "journalArticle":
        doi = find_doi_by_title(title, authors, year, parsed_type="journalArticle")
        if doi:
            out["doi"] = doi
        time.sleep(0.4)
    elif typ == "book":
        # 1차: Open Library, 실패 시 Google Books
        meta = fetch_openlibrary(title, authors, year)
        if not meta or not meta.get("ISBN"):
            time.sleep(0.4)
            gb = fetch_googlebooks(title, authors, year)
            if gb and gb.get("ISBN"):
                meta = gb
        if meta:
            # ISBN/publisher/place 등 빈 필드만 채움
            for k in ("ISBN", "publisher", "place", "language", "numPages"):
                v = meta.get(k)
                if v and not out.get(k):
                    out[k] = v
            # 연도 보강 (없을 때만)
            if not out.get("year") and meta.get("year_ext"):
                out["year"] = meta["year_ext"]
            # 저자가 없을 때만 보강
            if (not out.get("authors")) and meta.get("authors_ext"):
                out["authors"] = meta["authors_ext"]
            if meta.get("abstract") and not out.get("abstract"):
                out["abstract"] = meta["abstract"]
            out["_resolver"] = meta.get("_source")
        time.sleep(0.4)
        # 추가로 책 DOI 가능성: 제목 검색 — 반드시 type=book 만 허용 (저널 리뷰 false-positive 차단)
        if not out.get("doi"):
            doi = find_doi_by_title(
                title, authors, year, parsed_type="book", year_tolerance=10
            )
            if doi:
                out["doi"] = doi
            time.sleep(0.4)
    elif typ == "bookSection":
        # 챕터 DOI (CrossRef 가 일부 챕터를 색인)
        doi = find_doi_by_title(title, authors, year, parsed_type="bookSection")
        if doi:
            out["doi"] = doi
        time.sleep(0.4)
    return out


# ──────────────────────────────────────────────────────────────────────────────
# Step 3: Enrich (DOI → bib_enrich)
# ──────────────────────────────────────────────────────────────────────────────


def to_paper_dict(parsed: dict) -> dict:
    """parsed entry → bib_enrich.enrich() 가 받는 paper dict."""
    typ = parsed.get("type")
    paper: dict = {
        "title": parsed.get("title", ""),
        "authors": parsed.get("authors", []),
        "year": parsed.get("year", ""),
        "date": parsed.get("year", ""),
        "abstract": parsed.get("abstract", ""),
        "itemType": typ,
    }
    if parsed.get("doi"):
        paper["doi"] = parsed["doi"]

    if typ == "journalArticle":
        for k in ("journal", "volume", "issue", "pages"):
            v = parsed.get(k)
            if v:
                paper["publicationTitle" if k == "journal" else k] = v
    elif typ == "book":
        for k in ("publisher", "place", "ISBN", "edition", "numPages", "language"):
            v = parsed.get(k)
            if v:
                paper[k] = v
    elif typ == "bookSection":
        if parsed.get("bookTitle"):
            paper["bookTitle"] = parsed["bookTitle"]
        if parsed.get("editors"):
            paper["editors"] = parsed["editors"]
        for k in ("publisher", "place", "pages", "ISBN", "edition", "language"):
            v = parsed.get(k)
            if v:
                paper[k] = v
    return paper


# ──────────────────────────────────────────────────────────────────────────────
# Step 4: Dedup
# ──────────────────────────────────────────────────────────────────────────────


def dedup_internal(items: list[dict]) -> tuple[list[dict], list[dict]]:
    """파싱 결과 내부 중복 제거. (unique, dups) 반환."""
    seen_doi: set[str] = set()
    seen_isbn: set[str] = set()
    seen_title: dict[str, dict] = {}
    unique: list[dict] = []
    dups: list[dict] = []

    for item in items:
        doi = (item.get("doi") or "").strip().lower()
        isbn = (item.get("ISBN") or "").strip().replace("-", "")
        title_norm = _norm(item.get("title", ""))[:50]
        author_last = ""
        if item.get("authors"):
            author_last = _norm(item["authors"][0].get("lastName", ""))[:20]
        year = (item.get("year") or "")[:4]
        title_key = f"{title_norm}|{author_last}|{year}"

        if doi and doi in seen_doi:
            item["_dup_reason"] = f"doi={doi}"
            dups.append(item)
            continue
        if isbn and isbn in seen_isbn:
            item["_dup_reason"] = f"isbn={isbn}"
            dups.append(item)
            continue
        if title_norm and title_key in seen_title:
            item["_dup_reason"] = f"title={title_norm[:30]}"
            dups.append(item)
            continue

        if doi:
            seen_doi.add(doi)
        if isbn:
            seen_isbn.add(isbn)
        if title_norm:
            seen_title[title_key] = item
        unique.append(item)
    return unique, dups


def dedup_against_collection(items: list[dict], collection_key: str) -> tuple[list[dict], list[dict]]:
    """기존 Zotero 컬렉션과 비교. (new, existing) 반환."""
    log(f"  기존 컬렉션 항목 조회 중…")
    existing = get_collection_items_all(collection_key)
    log(f"    기존 {len(existing)}개 발견")

    existing_dois: dict[str, str] = {}
    existing_isbns: dict[str, str] = {}
    existing_titles: dict[str, str] = {}
    for it in existing:
        d = it.get("data", {})
        key = d.get("key", "")
        if d.get("DOI"):
            existing_dois[d["DOI"].strip().lower()] = key
        if d.get("ISBN"):
            existing_isbns[d["ISBN"].strip().replace("-", "")] = key
        title_norm = _norm(d.get("title", ""))[:50]
        if title_norm:
            existing_titles[title_norm] = key

    new_items: list[dict] = []
    existing_matches: list[dict] = []
    for item in items:
        doi = (item.get("doi") or "").strip().lower()
        isbn = (item.get("ISBN") or "").strip().replace("-", "")
        title_norm = _norm(item.get("title", ""))[:50]

        match_key = None
        match_field = None
        if doi and doi in existing_dois:
            match_key = existing_dois[doi]
            match_field = "doi"
        elif isbn and isbn in existing_isbns:
            match_key = existing_isbns[isbn]
            match_field = "isbn"
        elif title_norm and title_norm[:40] in existing_titles:
            match_key = existing_titles[title_norm[:40]]
            match_field = "title"

        if match_key:
            item["_existing_zotero_key"] = match_key
            item["_match_field"] = match_field
            existing_matches.append(item)
        else:
            new_items.append(item)
    return new_items, existing_matches


# ──────────────────────────────────────────────────────────────────────────────
# Step 5: Register to Zotero (batch 50)
# ──────────────────────────────────────────────────────────────────────────────


def register_to_zotero(items: list[dict], collection_key: str, dry_run: bool) -> list[dict]:
    """parsed/resolved items → Zotero items, batch POST. registered list 반환."""
    registered: list[dict] = []
    BATCH = 50

    for i in range(0, len(items), BATCH):
        batch = items[i : i + BATCH]
        # paper dict → enrich (DOI 있을 때만 실효) → Zotero item
        zotero_items: list[dict] = []
        for parsed in batch:
            paper = to_paper_dict(parsed)
            try:
                enriched = enrich_bib(paper, mailto=UNPAYWALL_EMAIL, sleep=0.3)
            except Exception as e:
                log(f"    enrich 실패: {parsed.get('title','')[:50]} | {e}")
                enriched = paper
            zitem = to_zotero_item(enriched, collection_key=collection_key)
            zotero_items.append(zitem)

        if dry_run:
            for parsed, zi in zip(batch, zotero_items):
                registered.append(
                    {**parsed, "zotero_key": "DRY_RUN", "_zotero_item": zi}
                )
            continue

        log(f"  Zotero 등록 batch {i+1}~{i+len(batch)}/{len(items)}…")
        try:
            resp = zotero_api("items", method="POST", data=zotero_items)
            success = resp.get("success", {})
            failed = resp.get("failed", {})
            for idx_str, key in success.items():
                idx = int(idx_str)
                registered.append(
                    {**batch[idx], "zotero_key": key, "_zotero_item": zotero_items[idx]}
                )
            for idx_str, err in failed.items():
                idx = int(idx_str)
                log(f"    실패 #{batch[idx].get('ref_num')}: {err}")
        except Exception as e:
            log(f"  배치 등록 오류: {e}")
        time.sleep(1.0)

    return registered


# ──────────────────────────────────────────────────────────────────────────────
# Step 6: Download PDFs (journalArticle 만)
# ──────────────────────────────────────────────────────────────────────────────


def _resolve_pdf_dir() -> Path:
    """OS-aware PDF 저장 디렉토리. Windows path on non-Windows → 로컬 캐시."""
    raw = get_zotero_dir() or ""
    if not raw:
        return PROJECT_ROOT / "pdf_cache"
    # Windows drive letter pattern (e.g., "C:\\Users\\...") on macOS/Linux
    if platform.system() != "Windows" and re.match(r"^[A-Za-z]:[\\/]", raw):
        log(f"  Windows 경로 감지 ({raw}) → 로컬 캐시로 fallback")
        return PROJECT_ROOT / "pdf_cache"
    p = Path(raw)
    if not p.parent.exists():
        return PROJECT_ROOT / "pdf_cache"
    return p


def download_pdfs(registered: list[dict], pdf_dir: Path, dry_run: bool) -> list[dict]:
    """journalArticle 한정 PDF 다운로드 + Zotero 첨부."""
    pdf_dir = Path(pdf_dir)
    pdf_dir.mkdir(parents=True, exist_ok=True)
    failed: list[dict] = []

    for item in registered:
        if item.get("type") != "journalArticle":
            continue
        if not item.get("doi") and not item.get("arxiv_id"):
            continue
        zotero_key = item.get("zotero_key")
        if not zotero_key or zotero_key == "DRY_RUN":
            continue

        title = item.get("title", "")
        log(f"  PDF: {title[:60]}…")

        paper = {
            "title": title,
            "doi": item.get("doi", ""),
            "arxiv_id": item.get("arxiv_id", ""),
            "authors": item.get("authors", []),
        }
        if dry_run:
            continue
        try:
            # download_pdf returns (path_or_empty, error_message)
            pdf_path, err = download_pdf(paper, str(pdf_dir))
            if pdf_path and Path(pdf_path).exists():
                attach_pdf(zotero_key, pdf_path)
                item["pdf_attached"] = True
                log(f"    ✓ 첨부 완료")
            else:
                failed.append({**item, "_pdf_error": err})
                log(f"    × {err or 'PDF 없음'}")
        except Exception as e:
            failed.append({**item, "_pdf_error": str(e)})
            log(f"    × 예외: {e}")
        time.sleep(0.5)

    return failed


# ──────────────────────────────────────────────────────────────────────────────
# Recovery: PDF-only mode
# ──────────────────────────────────────────────────────────────────────────────


def pdf_only_mode(parsed: list[dict], collection_key: str, pdf_dir: Path) -> tuple[list[dict], list[dict]]:
    """이미 등록된 항목을 컬렉션에서 찾아 PDF 다운로드 + 첨부.

    이전 실행이 PDF 단계에서 죽어 zotero_key 가 사라진 경우의 복구.
    journalArticle 만 처리. 이미 PDF 가 첨부된 항목은 건너뜀.
    """
    log(f"기존 컬렉션 항목 조회 중…")
    existing = get_collection_items_all(collection_key)
    log(f"  {len(existing)}개 발견")

    dois: dict[str, str] = {}
    titles: dict[str, str] = {}
    for it in existing:
        d = it.get("data", {})
        key = d.get("key", "") or it.get("key", "")
        if d.get("DOI"):
            dois[d["DOI"].strip().lower()] = key
        title_norm = _norm(d.get("title", ""))[:50]
        if title_norm:
            titles[title_norm] = key

    pdf_dir = Path(pdf_dir)
    pdf_dir.mkdir(parents=True, exist_ok=True)

    matched: list[dict] = []
    failed: list[dict] = []
    n_skipped_no_match = 0
    n_skipped_has_pdf = 0

    candidates = [p for p in parsed if p.get("type") == "journalArticle"]
    for i, p in enumerate(candidates, 1):
        doi = (p.get("doi") or "").strip().lower()
        title_norm = _norm(p.get("title", ""))[:50]
        zkey = dois.get(doi) or titles.get(title_norm)
        if not zkey:
            n_skipped_no_match += 1
            continue

        # 이미 PDF 첨부 있으면 skip
        try:
            children = get_item_children(zkey)
            has_pdf = any(
                c.get("data", {}).get("itemType") == "attachment"
                and c.get("data", {}).get("contentType") == "application/pdf"
                for c in children
            )
        except Exception:
            has_pdf = False
        if has_pdf:
            n_skipped_has_pdf += 1
            continue

        log(f"  [{i}/{len(candidates)}] {p.get('title','')[:60]} → {zkey}")
        paper = {
            "title": p.get("title", ""),
            "doi": p.get("doi", ""),
            "arxiv_id": p.get("arxiv_id", ""),
            "authors": p.get("authors", []),
        }
        try:
            pdf_path, err = download_pdf(paper, str(pdf_dir))
            if pdf_path and Path(pdf_path).exists():
                attach_pdf(zkey, pdf_path)
                matched.append({**p, "zotero_key": zkey, "pdf_attached": True})
                log(f"    ✓ 첨부 완료")
            else:
                failed.append({**p, "zotero_key": zkey, "_pdf_error": err})
                log(f"    × {err or 'PDF 없음'}")
        except Exception as e:
            failed.append({**p, "zotero_key": zkey, "_pdf_error": str(e)})
            log(f"    × 예외: {e}")
        time.sleep(0.5)

    log(
        f"  매칭+첨부: {len(matched)} | 실패: {len(failed)} | "
        f"매칭실패: {n_skipped_no_match} | 이미 PDF 있음: {n_skipped_has_pdf}"
    )
    return matched, failed


# ──────────────────────────────────────────────────────────────────────────────
# Move-to-subcollection mode
# ──────────────────────────────────────────────────────────────────────────────


def move_to_subcollection(
    resolved: list[dict],
    parent_collection_key: str,
    sub_name: str,
    pre_existing_keys: set[str] | None = None,
) -> dict:
    """resolved 항목들을 parent_collection 의 sub-collection 으로 이동.

    pre_existing_keys 에 든 zotero key 는 parent + sub 양쪽에 유지.
    그 외(우리가 새로 등록한 것)는 parent 에서 빼고 sub 에만 둔다.
    """
    pre_existing_keys = pre_existing_keys or set()

    # 1) parent 아래에 같은 이름 sub-collection 있는지 확인
    log(f"  collections 조회 중…")
    cols = zotero_api(
        "collections", params={"format": "json", "limit": "200"}
    )
    sub_key = None
    for c in cols:
        d = c.get("data", {})
        if d.get("name") == sub_name and d.get("parentCollection") == parent_collection_key:
            sub_key = d.get("key") or c.get("key")
            log(f"  기존 sub-collection 사용: {sub_name} ({sub_key})")
            break
    if not sub_key:
        log(f"  sub-collection 생성: {sub_name} (parent={parent_collection_key})")
        result = zotero_api(
            "collections",
            method="POST",
            data=[{"name": sub_name, "parentCollection": parent_collection_key}],
        )
        success = result.get("success", {}) or result.get("successful", {})
        if not success:
            raise RuntimeError(f"sub-collection 생성 실패: {result}")
        sub_key = next(iter(success.values()))
        # 일부 응답은 dict 형태 — 정상화
        if isinstance(sub_key, dict):
            sub_key = sub_key.get("key") or sub_key.get("data", {}).get("key", "")
        log(f"  생성 완료: {sub_key}")

    # 2) parent 컬렉션의 모든 item 조회 후 lookup map
    log("  parent 컬렉션 항목 로드 중…")
    parent_items = get_collection_items_all(parent_collection_key)
    log(f"    {len(parent_items)}개")
    by_doi: dict[str, dict] = {}
    by_isbn: dict[str, dict] = {}
    by_title: dict[str, dict] = {}
    for it in parent_items:
        d = it.get("data", {})
        rec = {
            "key": d.get("key") or it.get("key"),
            "version": it.get("version") or d.get("version"),
            "collections": list(d.get("collections") or []),
        }
        if d.get("DOI"):
            by_doi[d["DOI"].strip().lower()] = rec
        if d.get("ISBN"):
            by_isbn[d["ISBN"].strip().replace("-", "")] = rec
        title_norm = _norm(d.get("title", ""))[:50]
        if title_norm:
            by_title[title_norm] = rec

    moved: list[dict] = []
    added_only: list[dict] = []
    not_found: list[dict] = []
    failed: list[dict] = []

    for r in resolved:
        doi = (r.get("doi") or "").strip().lower()
        isbn = (r.get("ISBN") or "").strip().replace("-", "")
        title_norm = _norm(r.get("title", ""))[:50]
        rec = by_doi.get(doi) or by_isbn.get(isbn) or by_title.get(title_norm)
        if not rec:
            not_found.append(r)
            continue
        item_key = rec["key"]
        ver = rec["version"]
        cols_now = set(rec["collections"])

        is_pre = item_key in pre_existing_keys
        new_cols = set(cols_now)
        new_cols.add(sub_key)
        if not is_pre:
            new_cols.discard(parent_collection_key)

        if new_cols == cols_now:
            # 변경 사항 없음 (이미 sub 에 있고 parent 처리도 맞음)
            (added_only if is_pre else moved).append(
                {**r, "zotero_key": item_key, "_skipped": "already-correct"}
            )
            continue

        ok, err = _patch_item(item_key, ver, {"collections": sorted(new_cols)})
        rec_out = {**r, "zotero_key": item_key, "_was_pre_existing": is_pre}
        if ok:
            (added_only if is_pre else moved).append(rec_out)
            log(
                f"    {'+' if is_pre else '→'} {item_key} {r.get('title','')[:60]}"
            )
        else:
            rec_out["_error"] = err
            failed.append(rec_out)
            log(f"    × {item_key} {err}")
        time.sleep(0.15)

    log(
        f"\n  요약 — moved(parent→sub): {len(moved)}, "
        f"added(both, pre-existing): {len(added_only)}, "
        f"not_found: {len(not_found)}, failed: {len(failed)}"
    )
    return {
        "sub_key": sub_key,
        "moved": moved,
        "added_only": added_only,
        "not_found": not_found,
        "failed": failed,
    }


# ──────────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────────


def parse_input(path: Path) -> list[str]:
    """reference.txt 의 비어있지 않은 줄을 항목 리스트로 반환."""
    lines = []
    for ln in path.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if ln and re.match(r"^\d+\.\s", ln):
            lines.append(ln)
    return lines


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--input", required=True, help="reference.txt 경로")
    ap.add_argument(
        "--collection",
        default="scisci",
        help="config.json 의 zotero.collections 키 (기본: scisci)",
    )
    ap.add_argument("--dry-run", action="store_true", help="등록·PDF 단계 건너뜀")
    ap.add_argument("--no-cache", action="store_true", help="기존 캐시 무시")
    ap.add_argument("--skip-pdf", action="store_true", help="PDF 다운로드 건너뜀")
    ap.add_argument("--limit", type=int, default=0, help="앞 N 개만 처리 (0=전체)")
    ap.add_argument(
        "--pdf-only",
        action="store_true",
        help="이전 등록 결과의 PDF 만 (재)다운로드+첨부. 캐시(parsed.json+resolved.json) 필요.",
    )
    ap.add_argument(
        "--move-to-subcollection",
        metavar="NAME",
        help="resolved 항목들을 parent collection 의 sub-collection 으로 이동/추가. 캐시 필요.",
    )
    args = ap.parse_args()

    input_path = Path(args.input)
    if not input_path.is_absolute():
        input_path = PROJECT_ROOT / input_path
    if not input_path.exists():
        sys.exit(f"입력 파일 없음: {input_path}")

    collection_key = get_collection_key(args.collection)
    if not collection_key:
        sys.exit(f"Collection '{args.collection}' 을 config 에서 찾지 못함")
    log(f"Collection: {args.collection} → key={collection_key}")

    raw_lines = parse_input(input_path)
    if args.limit > 0:
        raw_lines = raw_lines[: args.limit]
    log(f"총 {len(raw_lines)}개 참고문헌 읽음")

    # ── Move-to-subcollection 모드 ────────────────────────────────────────────
    if args.move_to_subcollection:
        if not RESOLVED_CACHE.exists():
            sys.exit(f"--move-to-subcollection 은 {RESOLVED_CACHE} 가 필요합니다.")
        resolved = json.loads(RESOLVED_CACHE.read_text(encoding="utf-8"))
        # existing_matches.json 에 있는 키는 사용자가 컬렉션에 두었던 것이므로 양쪽 유지
        pre_existing_keys: set[str] = set()
        em_path = REPORT_DIR / "existing_matches.json"
        if em_path.exists():
            try:
                em = json.loads(em_path.read_text(encoding="utf-8"))
                pre_existing_keys = {
                    e.get("_existing_zotero_key") for e in em if e.get("_existing_zotero_key")
                }
                log(f"기존 매칭(parent 유지) 대상: {len(pre_existing_keys)}개")
            except Exception:
                pass
        result = move_to_subcollection(
            resolved, collection_key, args.move_to_subcollection, pre_existing_keys
        )
        _save_json(REPORT_DIR / "subcollection_result.json", result)
        log(
            f"\n=== sub-collection 요약 ===\n"
            f"  sub_key   : {result['sub_key']}\n"
            f"  moved     : {len(result['moved'])}\n"
            f"  added(양쪽): {len(result['added_only'])}\n"
            f"  not_found : {len(result['not_found'])}\n"
            f"  failed    : {len(result['failed'])}"
        )
        return

    # ── PDF-only 복구 모드 ────────────────────────────────────────────────────
    if args.pdf_only:
        if not RESOLVED_CACHE.exists():
            sys.exit(f"--pdf-only 는 {RESOLVED_CACHE} 가 필요합니다. 먼저 일반 모드로 실행하세요.")
        resolved = json.loads(RESOLVED_CACHE.read_text(encoding="utf-8"))
        if args.limit > 0:
            resolved = [r for r in resolved if r.get("ref_num", 0) <= args.limit]
        pdf_dir = _resolve_pdf_dir()
        log(f"PDF 저장 디렉토리: {pdf_dir}")
        matched, failed = pdf_only_mode(resolved, collection_key, pdf_dir)
        _save_json(REPORT_DIR / "pdf_attached.json", matched)
        _save_json(REPORT_DIR / "pdf_failed.json", failed)
        log(f"\n=== PDF-only 요약 ===\n  첨부 성공: {len(matched)}\n  실패: {len(failed)}")
        return

    # ── Step 1: Parse with Haiku (cached) ─────────────────────────────────────
    if PARSED_CACHE.exists() and not args.no_cache:
        log(f"[1/6] 캐시에서 파싱 결과 로드: {PARSED_CACHE}")
        parsed_all = json.loads(PARSED_CACHE.read_text(encoding="utf-8"))
        # Limit 변경에 맞춰 자르기
        if args.limit > 0:
            parsed_all = [p for p in parsed_all if p.get("ref_num", 0) <= args.limit]
    else:
        log(f"[1/6] Haiku 로 {len(raw_lines)}개 파싱 시작")
        anth_key = os.environ.get("ANTHROPIC_API_KEY", "")
        if not anth_key:
            sys.exit("ANTHROPIC_API_KEY 환경변수 필요")
        parsed_all = parse_with_haiku(raw_lines, anth_key)
        _save_json(PARSED_CACHE, parsed_all)
        log(f"  파싱 결과 저장: {PARSED_CACHE}")

    # 분류 통계
    by_type: dict[str, int] = {}
    for p in parsed_all:
        by_type[p.get("type", "unknown")] = by_type.get(p.get("type", "unknown"), 0) + 1
    log(f"  분류: {by_type}")

    # skip 분리
    skipped = [p for p in parsed_all if p.get("type") == "skip"]
    candidates = [p for p in parsed_all if p.get("type") in ("journalArticle", "book", "bookSection")]
    log(f"  처리 대상: {len(candidates)}개 (skip {len(skipped)}개)")

    # ── Step 2: Resolve identifiers (cached) ──────────────────────────────────
    if RESOLVED_CACHE.exists() and not args.no_cache:
        log(f"[2/6] 캐시에서 해상 결과 로드: {RESOLVED_CACHE}")
        resolved = json.loads(RESOLVED_CACHE.read_text(encoding="utf-8"))
        if args.limit > 0:
            resolved = [r for r in resolved if r.get("ref_num", 0) <= args.limit]
    else:
        log(f"[2/6] DOI/ISBN 해상 시작 (총 {len(candidates)}개)")
        resolved = []
        for i, p in enumerate(candidates, 1):
            log(f"  [{i}/{len(candidates)}] {p.get('type','?')[:1]} {p.get('title','')[:60]}")
            try:
                resolved.append(resolve_one(p, UNPAYWALL_EMAIL))
            except Exception as e:
                log(f"    × resolve 오류: {e}")
                resolved.append(dict(p))
            if i % 10 == 0:
                _save_json(RESOLVED_CACHE, resolved)  # 중간저장
        _save_json(RESOLVED_CACHE, resolved)
        log(f"  해상 결과 저장: {RESOLVED_CACHE}")

    # 해상 통계
    n_doi = sum(1 for r in resolved if r.get("doi"))
    n_isbn = sum(1 for r in resolved if r.get("ISBN"))
    log(f"  DOI 해상: {n_doi}/{len(resolved)} | ISBN: {n_isbn}/{len(resolved)}")

    # ── Step 3: Internal dedup ────────────────────────────────────────────────
    log(f"[3/6] 내부 중복 제거")
    unique, internal_dups = dedup_internal(resolved)
    log(f"  unique={len(unique)} dup={len(internal_dups)}")

    # ── Step 4: Cross-collection dedup ────────────────────────────────────────
    log(f"[4/6] 컬렉션 대조 중복 제거")
    new_items, existing_matches = dedup_against_collection(unique, collection_key)
    log(f"  new={len(new_items)} 기존_컬렉션_중복={len(existing_matches)}")

    # ── Step 5: Register ──────────────────────────────────────────────────────
    log(f"[5/6] Zotero 등록 ({'DRY-RUN' if args.dry_run else 'REAL'})")
    registered = register_to_zotero(new_items, collection_key, args.dry_run)
    log(f"  등록 완료: {len(registered)}/{len(new_items)}")

    # ── Step 6: PDF download ──────────────────────────────────────────────────
    pdf_failed: list[dict] = []
    if not args.skip_pdf and not args.dry_run:
        log(f"[6/6] PDF 다운로드")
        zdir = _resolve_pdf_dir()
        log(f"  PDF 저장 디렉토리: {zdir}")
        pdf_failed = download_pdfs(registered, zdir, args.dry_run)
    else:
        log(f"[6/6] PDF 단계 건너뜀")

    # ── Reports ───────────────────────────────────────────────────────────────
    log("리포트 저장")
    _save_json(REPORT_DIR / "registered.json", registered)
    _save_json(REPORT_DIR / "internal_duplicates.json", internal_dups)
    _save_json(REPORT_DIR / "existing_matches.json", existing_matches)
    _save_json(REPORT_DIR / "skipped.json", skipped)
    _save_json(REPORT_DIR / "pdf_failed.json", pdf_failed)

    # 미해상 요약 (DOI/ISBN 둘다 없는 항목)
    unmatched = [
        r for r in new_items if not r.get("doi") and not r.get("ISBN")
    ]
    _save_json(REPORT_DIR / "unmatched.json", unmatched)

    log(
        f"\n=== 요약 ===\n"
        f"  입력            : {len(raw_lines)}\n"
        f"  skip            : {len(skipped)}\n"
        f"  내부 중복       : {len(internal_dups)}\n"
        f"  기존 컬렉션 중복: {len(existing_matches)}\n"
        f"  Zotero 등록     : {len(registered)}\n"
        f"  미해상(no DOI/ISBN): {len(unmatched)}\n"
        f"  PDF 실패        : {len(pdf_failed)}\n"
        f"  리포트          : {REPORT_DIR}"
    )


if __name__ == "__main__":
    main()
