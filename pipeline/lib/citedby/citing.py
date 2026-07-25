"""인용논문(citing papers) 수집 — DOI 하나로 여러 학술 DB 를 훑는다.

scisci `scie/lib/citing.py` 이식본. 주어진 DOI 를 인용한 논문을 OpenAlex /
Scopus / Semantic Scholar / arXiv 에서 병렬 수집하고, source 우선순위 기반으로
병합·중복제거해 단일 DataFrame 으로 돌려준다.

paper-curation 의 "같이 보면 좋은 논문"(SPECTER2 임베딩 유사도)은 **코퍼스 내부·
유사도 축**이라 *이 논문을 인용한 새 논문*을 구조적으로 찾지 못한다. 이 모듈이
그 **시간축·인용축** 공백을 메운다.

이식 시 원본에서 바뀐 점:
  1. **429 무한루프 수정** — 원본 OpenAlex/S2 루프는 429 를 만나면 sleep 후
     `continue` 만 해서 커서/오프셋이 전진하지 않아 영구히 돌 수 있었다.
     재시도 횟수를 유한하게 묶었다 (`_MAX_RATE_LIMIT_RETRIES`).
  2. **`find_paper_in_db` 제거** — scisci `literature.db` 의 `papers` 테이블
     스키마 전용이라 paper-curation 에는 대응물이 없다.
  3. **Scopus 인프라 분리** — `.scopus` 모듈로 발췌 (원본은 retrieval.py 의존).
  4. **pandas 지연 import** — citedby 미사용 시 기동 비용 0.
"""
from __future__ import annotations

import logging
import os
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

from . import scopus as _scopus

logger = logging.getLogger(__name__)


def _today() -> str:
    """피인용수 수집 시점. 숫자는 시간이 지나면 낡으므로 함께 기록한다."""
    return _scopus._today()

# citing 논문 통합 컬럼 — 모든 source 의 레코드가 이 스키마로 정규화된다.
CITING_COLUMNS = [
    "doi", "eid", "arxiv_id", "title", "abstract", "journal",
    # `date` 는 소스가 주는 **완전한 ISO 날짜**(YYYY-MM-DD). year/month 는
    # 정렬·집계용 파생값이라 date 를 대체하지 않는다 — Zotero 에는 date 를 쓴다.
    "date", "year", "month",
    "volume", "issue", "pages", "source",
    # 피인용수는 **소스마다 세는 우주가 다르다** — Scopus 는 Scopus 색인만,
    # OpenAlex 는 자기 그래프만, S2 는 프리프린트·회색문헌까지 센다. 실측에서
    # 같은 논문이 CR=47 / OA=52 / S2=104 으로 갈렸다. 그래서 병합(max)하지
    # 않고 **소스별로 보존**하고, 표시할 때 출처·시점을 함께 밝힌다.
    "citations_scopus", "citations_crossref",
    "citations_openalex", "citations_s2",
    # OpenAlex 연차보정 백분위 — 같은 해·분야 대비 상위 몇 %. 절대 피인용수는
    # 분야·연차 편차가 커서 단독으로는 오독하기 쉽다.
    "citations_percentile", "citations_asof",
    # 정렬·표시에 쓰는 대표값 (파생). `_pick_citation_count` 가 채운다.
    "citationCount",
    "issn", "publisher", "language", "item_type",
    "pdf_url", "au_keywords", "author_count", "author_names",
    "author_ids", "author_afids", "af_id", "af_name", "af_city", "af_country",
]

# 구조적으로 citing 조회가 불가능한 source. UI 가 사유를 그대로 노출한다.
UNSUPPORTED_SOURCES = {
    "wos": ("WoS Starter API 는 citing 쿼리(CI= 필드)를 지원하지 않습니다 — "
            "Expanded API 상위 라이선스 필요"),
}

# 429/일시장애 재시도 상한. 원본의 무한 `continue` 를 대체한다.
_MAX_RATE_LIMIT_RETRIES = 5

_DEFAULT_SOURCES = ["scopus", "wos", "openalex", "semanticscholar", "arxiv"]

# OpenAlex 응답 필드 화이트리스트. `_parse_openalex_work` 가 읽는 것과 **반드시**
# 일치해야 한다 — select 에서 빠진 필드는 응답에 아예 담기지 않아, 파서가 조용히
# 빈 값을 채운다 (실제로 `biblio` 누락으로 권/호/페이지가 전부 비어 있었다).
_OPENALEX_SELECT = (
    "id,doi,title,display_name,publication_date,primary_location,"
    "authorships,cited_by_count,abstract_inverted_index,type,biblio,language,"
    "citation_normalized_percentile"
)


def normalize_doi(raw_input: str) -> str:
    """여러 표기의 DOI 를 bare DOI 로 정규화.

    'https://doi.org/10.1234/abc', 'doi:10.1234/abc', 'DOI: 10.1234/abc'
    → '10.1234/abc'
    """
    doi = (raw_input or "").strip()
    for prefix in ("https://doi.org/", "http://doi.org/",
                   "https://dx.doi.org/", "http://dx.doi.org/"):
        if doi.lower().startswith(prefix):
            doi = doi[len(prefix):]
            break
    m = re.match(r"^(?:doi:\s*)", doi, re.IGNORECASE)
    if m:
        doi = doi[m.end():]
    return doi.strip()


def reconstruct_abstract(inv_idx: dict) -> str:
    """OpenAlex inverted index → 평문 초록."""
    if not inv_idx:
        return ""
    word_positions = []
    for word, positions in inv_idx.items():
        for pos in positions:
            word_positions.append((pos, word))
    word_positions.sort()
    return " ".join(wp[1] for wp in word_positions)


def _openalex_params() -> dict:
    """OpenAlex polite pool / premium 파라미터."""
    params = {}
    api_key = os.environ.get("OPENALEX_API_KEY", "")
    email = os.environ.get("OPENALEX_EMAIL", "")
    if api_key:
        params["api_key"] = api_key
    elif email:
        params["mailto"] = email
    return params


# ── OpenAlex ──────────────────────────────────────────────────────────────

def _openalex_resolve_doi(doi: str) -> str | None:
    """DOI → OpenAlex work id."""
    url = f"https://api.openalex.org/works/doi:{doi}"
    try:
        resp = requests.get(url, params=_openalex_params(), timeout=30)
        if resp.status_code == 200:
            return (resp.json().get("id") or "").replace("https://openalex.org/", "")
        logger.warning("OpenAlex DOI resolve failed (%s): %s", resp.status_code, doi)
    except Exception as e:  # noqa: BLE001
        logger.warning("OpenAlex DOI resolve error: %s", e)
    return None


def _parse_openalex_work(w: dict) -> dict:
    """OpenAlex work → 통합 레코드."""
    pub_date = w.get("publication_date") or ""
    loc = w.get("primary_location") or {}
    source_info = loc.get("source") or {}
    authorships = w.get("authorships") or []
    # OpenAlex 는 권/호/페이지를 `biblio` 에 담아 준다. select 에 넣지 않으면
    # 응답에서 통째로 빠지므로 `_OPENALEX_SELECT` 와 짝을 맞춰야 한다.
    biblio = w.get("biblio") or {}
    first_page = (biblio.get("first_page") or "").strip()
    last_page = (biblio.get("last_page") or "").strip()
    if first_page and last_page and first_page != last_page:
        pages = f"{first_page}-{last_page}"
    else:
        pages = first_page or last_page or ""

    af_names, af_countries = [], []
    for a in authorships:
        for inst in (a.get("institutions") or []):
            af_names.append(inst.get("display_name") or "")
            af_countries.append(inst.get("country_code") or "")

    return {
        "title": w.get("display_name") or w.get("title") or "",
        "abstract": reconstruct_abstract(w.get("abstract_inverted_index")),
        # 완전한 날짜를 그대로 보존한다. year/month 는 파생값일 뿐이라,
        # 여기서 잘라 버리면 Zotero 에 "2025" 만 들어간다 (실제 버그였다).
        "date": pub_date,
        "year": int(pub_date[:4]) if len(pub_date) >= 4 else None,
        "month": int(pub_date[5:7]) if len(pub_date) >= 7 else None,
        "doi": (w.get("doi") or "").replace("https://doi.org/", ""),
        "eid": "",
        "arxiv_id": "",
        "pdf_url": loc.get("pdf_url") or loc.get("landing_page_url") or "",
        "journal": source_info.get("display_name", ""),
        "volume": (biblio.get("volume") or "").strip(),
        "issue": (biblio.get("issue") or "").strip(),
        "pages": pages,
        "issn": "; ".join(source_info.get("issn") or []),
        "publisher": source_info.get("host_organization_name", "") or "",
        "language": w.get("language", "") or "",
        "item_type": w.get("type", "") or "",
        "citations_openalex": w.get("cited_by_count"),
        "citations_scopus": None,
        "citations_crossref": None,
        "citations_s2": None,
        # 같은 해·분야 대비 상위 몇 % (0~1). 절대 피인용수보다 해석이 쉽다.
        "citations_percentile": (w.get("citation_normalized_percentile")
                                 or {}).get("value"),
        "citations_asof": _today(),
        "citationCount": w.get("cited_by_count") or 0,
        "af_city": "",
        "af_country": "; ".join(c for c in af_countries[:5] if c),
        "af_id": "",
        "af_name": "; ".join(n for n in af_names[:5] if n),
        "au_keywords": "",
        "author_afids": "",
        "author_count": len(authorships),
        "author_ids": "",
        "author_names": "; ".join(
            (a.get("author") or {}).get("display_name") or "" for a in authorships
        ),
        "source": "openalex",
    }


def get_citing_from_openalex(doi: str, max_results: int = 5000) -> list[dict]:
    """OpenAlex `cites:{work_id}` 필터 + 커서 페이지네이션."""
    work_id = _openalex_resolve_doi(doi)
    if not work_id:
        logger.warning("OpenAlex: could not resolve DOI %s, skipping", doi)
        return []

    results: list[dict] = []
    cursor = "*"
    rate_limit_retries = 0

    while len(results) < max_results:
        params = {
            "filter": f"cites:{work_id}",
            "per_page": 200,
            "cursor": cursor,
            "select": _OPENALEX_SELECT,
            **_openalex_params(),
        }
        try:
            resp = requests.get("https://api.openalex.org/works",
                                params=params, timeout=30)
            if resp.status_code == 429:
                # 원본은 무한 continue 였다. 유한 재시도로 묶는다.
                rate_limit_retries += 1
                if rate_limit_retries > _MAX_RATE_LIMIT_RETRIES:
                    logger.error("OpenAlex: rate limited %d times, giving up "
                                 "(partial: %d)", rate_limit_retries, len(results))
                    break
                wait = min(60, 5 * (2 ** (rate_limit_retries - 1)))
                logger.warning("OpenAlex rate limited (%d/%d). Waiting %ds...",
                               rate_limit_retries, _MAX_RATE_LIMIT_RETRIES, wait)
                time.sleep(wait)
                continue
            if resp.status_code != 200:
                logger.error("OpenAlex citing error %s: %s",
                             resp.status_code, resp.text[:200])
                break

            data = resp.json()
            works = data.get("results") or []
            if not works:
                break
            results.extend(_parse_openalex_work(w) for w in works)

            cursor = (data.get("meta") or {}).get("next_cursor")
            if not cursor:
                break
            time.sleep(0.2)
        except Exception as e:  # noqa: BLE001
            logger.error("OpenAlex citing fetch error: %s", e)
            break

    logger.info("OpenAlex: %d citing papers for DOI %s", len(results), doi)
    return results


# ── Scopus ────────────────────────────────────────────────────────────────

def _scopus_find_eid(doi: str) -> str | None:
    """DOI → Scopus EID."""
    headers = _scopus.headers()
    try:
        resp = requests.get(_scopus.SCOPUS_SEARCH_URL, headers=headers,
                            params={"query": f'DOI("{doi}")', "count": 1}, timeout=15)
        if resp.status_code == 200:
            entries = (resp.json().get("search-results") or {}).get("entry") or []
            if entries and not entries[0].get("error"):
                return entries[0].get("eid", "")
    except Exception as e:  # noqa: BLE001
        logger.warning("Scopus EID lookup error: %s", e)
    return None


def get_citing_from_scopus(doi: str, max_results: int = 5000) -> list[dict]:
    """Scopus `REFEID(eid)` 쿼리로 인용논문 수집.

    pybliometrics.cfg 의 API 키 + **기관 IP** 가 필요하다. 어느 쪽이든 없으면
    빈 리스트로 조용히 degrade 한다 (전체 분석을 중단시키지 않는다).
    """
    ok, reason = _scopus.available()
    if not ok:
        logger.warning("Scopus not available: %s", reason)
        return []

    eid = _scopus_find_eid(doi)
    if not eid:
        logger.warning("Scopus: could not find EID for DOI %s, skipping", doi)
        return []

    headers = {"Accept": "application/json"}
    page_size = 25
    all_entries: list[dict] = []
    max_attempts = 3

    for attempt in range(1, max_attempts + 1):
        start = 0
        all_entries = []
        auth_retries = 0
        try:
            while len(all_entries) < max_results:
                headers = _scopus.headers()
                resp = requests.get(
                    _scopus.SCOPUS_SEARCH_URL, headers=headers,
                    params={"query": f"REFEID({eid})", "count": page_size,
                            "start": start},
                    timeout=30,
                )
                if resp.status_code in (401, 429):
                    # 키 회전으로 풀리는 실패. 키 수만큼만 돌고 포기한다
                    # (원본은 상한이 없어 영구 회전 가능했다).
                    auth_retries += 1
                    if auth_retries > _MAX_RATE_LIMIT_RETRIES:
                        logger.error("Scopus: %s persisted after %d key rotations",
                                     resp.status_code, auth_retries)
                        break
                    _scopus.rotate_key()
                    time.sleep(2 if resp.status_code == 429 else 1)
                    continue
                resp.raise_for_status()

                sr = resp.json().get("search-results") or {}
                entries = sr.get("entry") or []
                if not entries or (len(entries) == 1 and entries[0].get("error")):
                    break
                all_entries.extend(entries)

                total = int(sr.get("opensearch:totalResults", 0) or 0)
                if len(all_entries) >= total:
                    break
                start += page_size
            break  # 성공
        except Exception as e:  # noqa: BLE001
            if attempt < max_attempts:
                logger.warning("Scopus citing failed (attempt %d): %s", attempt, e)
                time.sleep(10)
            else:
                logger.error("Scopus citing failed after %d attempts: %s",
                             max_attempts, e)
                all_entries = []

    if not all_entries:
        logger.info("Scopus: 0 citing papers for DOI %s", doi)
        return []

    results = _scopus.results_to_df(all_entries).to_dict("records")
    logger.info("Scopus: %d citing papers for DOI %s", len(results), doi)
    return results


# ── Semantic Scholar ──────────────────────────────────────────────────────

def get_citing_from_s2(doi: str, max_results: int = 5000) -> list[dict]:
    """S2 `/paper/DOI:{doi}/citations` 페이지네이션."""
    api_key = os.environ.get("S2_API_KEY", "")
    headers = {"x-api-key": api_key} if api_key else {}
    fields = ("title,abstract,externalIds,journal,publicationDate,"
              "citationCount,authors,openAccessPdf,publicationTypes")
    base_url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}/citations"

    results: list[dict] = []
    offset = 0
    limit = 1000  # S2 최대
    rate_limit_retries = 0

    while offset < max_results:
        try:
            resp = requests.get(base_url, headers=headers,
                                params={"fields": fields, "offset": offset,
                                        "limit": limit},
                                timeout=30)
            if resp.status_code == 429:
                rate_limit_retries += 1
                if rate_limit_retries > _MAX_RATE_LIMIT_RETRIES:
                    logger.error("S2: rate limited %d times, giving up (partial: %d)",
                                 rate_limit_retries, len(results))
                    break
                try:
                    wait = int(resp.headers.get("Retry-After", 60))
                except (TypeError, ValueError):
                    wait = 60
                wait = min(wait, 120)
                logger.warning("S2 rate limited (%d/%d). Waiting %ds...",
                               rate_limit_retries, _MAX_RATE_LIMIT_RETRIES, wait)
                time.sleep(wait)
                continue
            if resp.status_code == 404:
                logger.warning("S2: paper not found for DOI %s", doi)
                break
            if resp.status_code != 200:
                logger.error("S2 citing error %s: %s",
                             resp.status_code, resp.text[:200])
                break

            items = (resp.json() or {}).get("data") or []
            if not items:
                break

            for item in items:
                p = item.get("citingPaper") or {}
                if not p.get("title"):
                    continue
                ext_ids = p.get("externalIds") or {}
                pub_date = p.get("publicationDate") or ""
                authors = p.get("authors") or []
                journal = p.get("journal") or {}
                oa_pdf = p.get("openAccessPdf") or {}

                results.append({
                    "title": p.get("title", ""),
                    "abstract": p.get("abstract") or "",
                    "date": pub_date,
                    "year": int(pub_date[:4]) if len(pub_date) >= 4 else None,
                    "month": int(pub_date[5:7]) if len(pub_date) >= 7 else None,
                    "doi": ext_ids.get("DOI", ""),
                    "eid": "",
                    "arxiv_id": ext_ids.get("ArXiv", ""),
                    "pdf_url": oa_pdf.get("url", ""),
                    "journal": journal.get("name", "") or "",
                    "volume": journal.get("volume", "") or "",
                    "issue": "",
                    "pages": (journal.get("pages", "") or "").replace(" - ", "-"),
                    "issn": "",
                    "publisher": "",
                    "language": "",
                    "item_type": "; ".join(p.get("publicationTypes") or []),
                    "citations_s2": p.get("citationCount"),
                    "citations_scopus": None,
                    "citations_crossref": None,
                    "citations_openalex": None,
                    "citations_percentile": None,
                    "citations_asof": _today(),
                    "citationCount": p.get("citationCount") or 0,
                    "af_city": "",
                    "af_country": "",
                    "af_id": "",
                    "af_name": "",
                    "au_keywords": "",
                    "author_afids": "",
                    "author_count": len(authors),
                    "author_ids": "",
                    "author_names": "; ".join(a.get("name", "") for a in authors),
                    "source": "semanticscholar",
                })

            offset += len(items)
            if len(items) < limit:
                break
            time.sleep(1)  # courtesy delay
        except Exception as e:  # noqa: BLE001
            logger.error("S2 citing fetch error: %s", e)
            break

    logger.info("S2: %d citing papers for DOI %s", len(results), doi)
    return results


# ── arXiv ─────────────────────────────────────────────────────────────────

def get_citing_from_arxiv(doi: str, max_results: int = 5000) -> list[dict]:
    """arXiv 는 인용 API 가 없다 — S2 citing 중 arXiv id 를 뽑아 arXiv API 로 보강.

    S2 가 초록을 비워 돌려주는 경우가 많아, arXiv 원문 초록으로 덮는 게 목적이다.
    """
    import arxiv

    all_s2 = get_citing_from_s2(doi, max_results=max_results)
    arxiv_ids = [r["arxiv_id"] for r in all_s2 if r.get("arxiv_id")]
    if not arxiv_ids:
        logger.info("arXiv: no arXiv papers among %d S2 citations", len(all_s2))
        return []

    logger.info("arXiv: fetching %d papers from arXiv API...", len(arxiv_ids))
    results: list[dict] = []
    batch_size = 50
    client = arxiv.Client()

    for start in range(0, len(arxiv_ids), batch_size):
        batch_ids = arxiv_ids[start:start + batch_size]
        try:
            for paper in client.results(arxiv.Search(id_list=batch_ids)):
                aid = paper.entry_id.split("/abs/")[-1]
                results.append({
                    "title": paper.title,
                    "abstract": paper.summary or "",
                    "date": (paper.published.strftime("%Y-%m-%d")
                             if paper.published else ""),
                    "year": paper.published.year if paper.published else None,
                    "month": paper.published.month if paper.published else None,
                    "doi": paper.doi or "",
                    "eid": "",
                    "arxiv_id": aid,
                    "pdf_url": paper.pdf_url or "",
                    "journal": "",
                    "volume": "",
                    "issue": "",
                    "pages": "",
                    "issn": "",
                    "publisher": "arXiv",
                    "language": "",
                    "item_type": "preprint",
                    # arXiv 는 피인용수를 제공하지 않는다 — 0 이 아니라 '모름'.
                    "citations_scopus": None,
                    "citations_crossref": None,
                    "citations_openalex": None,
                    "citations_s2": None,
                    "citations_percentile": None,
                    "citations_asof": "",
                    "citationCount": 0,
                    "af_city": "",
                    "af_country": "",
                    "af_id": "",
                    "af_name": "",
                    "au_keywords": "",
                    "author_afids": "",
                    "author_count": len(paper.authors),
                    "author_ids": "",
                    "author_names": "; ".join(a.name for a in paper.authors),
                    "source": "arxiv",
                })
        except Exception as e:  # noqa: BLE001
            logger.warning("arXiv batch fetch error: %s", e)

        if start + batch_size < len(arxiv_ids):
            time.sleep(3)  # arXiv 권장: 1 req/3sec

    logger.info("arXiv: %d papers fetched (from %d IDs via S2)",
                len(results), len(arxiv_ids))
    return results


# ── Web of Science ────────────────────────────────────────────────────────

def get_citing_from_wos(doi: str, max_results: int = 5000) -> list[dict]:
    """항상 빈 리스트 — WoS Starter API 는 citing 조회를 지원하지 않는다.

    `CI=` 필드 태그는 Expanded API(상위 라이선스) 전용이다. 소스 목록에 wos 를
    넣어도 0건이 정상이며, 사유는 `UNSUPPORTED_SOURCES["wos"]` 로 UI 에 노출된다.
    """
    logger.info("WoS: %s", UNSUPPORTED_SOURCES["wos"])
    return []


_SOURCE_FETCHERS = {
    "scopus": get_citing_from_scopus,
    "wos": get_citing_from_wos,
    "openalex": get_citing_from_openalex,
    "semanticscholar": get_citing_from_s2,
    "arxiv": get_citing_from_arxiv,
}

# 서지 필드 병합 우선순위 — 낮을수록 우선.
#
# 실측(표본 25편) 근거:
#   volume  Crossref 20/25 · OpenAlex 20/25 · S2 13/25
#   pages   Crossref 18/25 · OpenAlex 19/25 · S2 10/25
# Crossref 는 발행사가 직접 등록한 정본이라 권/호/페이지 표기가 가장 믿을 만하고,
# S2 는 서지에서 확연히 뒤진다. Scopus 는 있을 때 가장 조밀하지만 기관 IP 가
# 없으면 0건이라 실질 1순위는 Crossref 가 된다.
_SOURCE_PRIORITY = {
    "scopus": 0,
    "crossref": 1,
    "wos": 2,
    "openalex": 3,
    "arxiv": 4,
    "semanticscholar": 5,
}

# 필드별 권위 재정의 — 전역 순위와 다른 필드만 적는다.
#
# 초록은 커버리지가 정반대다: Crossref 7/25 vs OpenAlex 13/25 · S2 13/25.
# Crossref 는 발행사가 JATS 로 넣어야만 초록이 있어 28% 에 그친다. 전역 순위를
# 그대로 쓰면 초록에서 손해라, 이 필드만 뒤집는다.
_FIELD_AUTHORITY = {
    "abstract": {
        # Scopus 는 최상위 유지 — 큐레이션된 초록이고, 실측으로 열위가 확인된
        # 건 Crossref 뿐이다. 근거 없이 강등하지 않는다.
        "scopus": 0, "openalex": 1, "semanticscholar": 2, "arxiv": 3,
        "crossref": 4, "wos": 5,
    },
}


def _field_rank(field: str, source: str) -> int:
    """해당 필드에서 이 source 의 우선순위. 낮을수록 우선."""
    table = _FIELD_AUTHORITY.get(field) or _SOURCE_PRIORITY
    return table.get(source, 99)


# 피인용수는 병합하지 않는다 — 소스별 컬럼에 그대로 남긴다.
_CITATION_COLUMNS = ("citations_scopus", "citations_crossref",
                     "citations_openalex", "citations_s2",
                     "citations_percentile", "citations_asof",
                     "citationCount")

_ENRICH_FIELDS = [c for c in CITING_COLUMNS
                  if c != "source" and c not in _CITATION_COLUMNS]


# 대표 피인용수를 고를 때의 소스 순서. OpenAlex 가 커버리지가 가장 넓고
# 키가 필요 없으며 연차보정 백분위까지 준다.
_CITATION_PREFERENCE = ("openalex", "crossref", "scopus", "s2")


def _pick_citation_count(row) -> tuple:
    """소스별 피인용수 중 대표값을 고른다. 반환 (값, 출처) — 없으면 (None, "").

    **0 은 결측이 아니다.** 최근 논문의 0 은 정상값이고, citedby 는 바로 그
    "아직 인용이 적은 새 논문"을 찾는 기능이다. 필드 부재(None)만 결측으로 본다.
    """
    for src in _CITATION_PREFERENCE:
        val = row.get(f"citations_{src}")
        if val is not None and str(val).strip() not in ("", "nan", "None"):
            try:
                return int(float(val)), src
            except (TypeError, ValueError):
                continue
    return None, ""


# ── 오케스트레이션 ────────────────────────────────────────────────────────

def fetch_all_citing_papers(doi: str,
                            sources: list[str] | None = None,
                            max_results_per_source: int = 5000,
                            progress_callback=None):
    """여러 source 에서 인용논문을 병렬 수집 → 우선순위 병합 → 중복제거.

    Args:
        doi: 정규화된 DOI.
        sources: source 이름 리스트. 기본은 전체 5종.
        max_results_per_source: source 당 상한.
        progress_callback: `cb(phase, message)` — source 별 found/overlap/new 보고.

    Returns:
        `(merged_df, source_counts)` — source_counts 는 중복제거 **이전** 원시 건수.
    """
    import pandas as pd

    if sources is None:
        sources = list(_DEFAULT_SOURCES)

    source_counts: dict[str, int] = {}
    source_records: dict[str, list[dict]] = {}

    known = [s for s in sources if s in _SOURCE_FETCHERS]
    for s in sources:
        if s not in _SOURCE_FETCHERS:
            logger.warning("Unknown citing source: %s", s)

    if known:
        with ThreadPoolExecutor(max_workers=len(known)) as executor:
            future_to_source = {
                executor.submit(_SOURCE_FETCHERS[s], doi, max_results_per_source): s
                for s in known
            }
            for future in as_completed(future_to_source):
                src = future_to_source[future]
                try:
                    records = future.result()
                except Exception as e:  # noqa: BLE001 — 한 source 실패가 전체를 죽이지 않게
                    logger.error("Failed to fetch citing papers from %s: %s", src, e)
                    records = []
                source_counts[src] = len(records)
                source_records[src] = records

    # source 별 found/overlap/new 를 우선순위 순서로 보고 (dedup 키는 병합과 동일).
    all_records: list[dict] = []
    if progress_callback:
        seen_titles: set[str] = set()
        seen_dois: set[str] = set()
        for src in sources:
            records = source_records.get(src, [])
            new_count = overlap = 0
            for r in records:
                doi_key = (r.get("doi") or "").strip().lower()
                title_key = (r.get("title") or "").lower().strip()
                if (doi_key and doi_key in seen_dois) or \
                   (title_key and title_key in seen_titles):
                    overlap += 1
                    continue
                if doi_key:
                    seen_dois.add(doi_key)
                if title_key:
                    seen_titles.add(title_key)
                new_count += 1
            note = UNSUPPORTED_SOURCES.get(src)
            if note:
                progress_callback("fetch", f"{src}: 미지원 — {note}")
            else:
                progress_callback(
                    "fetch",
                    f"{src}: found({len(records)}), overlap({overlap}), new({new_count})",
                )
            all_records.extend(records)
    else:
        for src in sources:
            all_records.extend(source_records.get(src, []))

    if not all_records:
        return pd.DataFrame(columns=CITING_COLUMNS), source_counts

    df = _merge_by_priority(pd.DataFrame(all_records))
    df = _fill_missing_abstracts_by_doi(df)
    # 병합 이후에 돈다 — 어느 source 도 못 채운 칸만 Crossref(DOI 정본)로 메운다.
    df = enrich_from_crossref(df, progress_callback)

    logger.info("Total citing papers after dedup: %d (raw: %d)",
                len(df), sum(source_counts.values()))
    return df, source_counts


_SPRINGER_META_ENDPOINTS = ("meta/v2/json", "metadata/json")

# Springer Nature 계열 DOI 접두사. 다른 발행사에 헛요청을 보내지 않으려고 미리
# 거른다 (Elsevier·SSRN 등은 이 API 로 못 받는다).
_SPRINGER_PREFIXES = ("10.1038", "10.1007", "10.1186", "10.1057", "10.1140")


def springer_meta_key() -> str:
    """Springer Nature **Metadata** API 키.

    OpenAccess API 키(`NATURESPRINGER_API_KEY`)와 **다른 키**다. 실측:
    OpenAccess 키로 Metadata 를 부르면 401 이고, OpenAccess 는 비OA 논문에
    404 라 초록 결손을 하나도 못 메운다. 초록을 주는 건 Metadata 쪽이다.
    """
    for name in ("SPRINGER_META_API_KEY", "NATURESPRINGERMETA_API_KEY",
                 "NATURESPRINTERMETA_API_KEY"):
        v = (os.environ.get(name) or "").strip()
        if v:
            return v
    return ""


def _springer_abstract(doi: str, key: str) -> str:
    """Springer Nature Metadata API 에서 초록 하나. 없으면 빈 문자열."""
    for path in _SPRINGER_META_ENDPOINTS:
        try:
            resp = requests.get(
                f"https://api.springernature.com/{path}",
                params={"q": f"doi:{doi}", "api_key": key}, timeout=20)
            if resp.status_code != 200:
                continue
            for rec in (resp.json().get("records") or []):
                ab = rec.get("abstract") or ""
                # 응답 형태가 문자열/`{p: ...}`/리스트로 갈린다.
                if isinstance(ab, dict):
                    ab = ab.get("p") or ""
                if isinstance(ab, list):
                    ab = " ".join(str(x) for x in ab)
                ab = str(ab).strip()
                if ab:
                    return ab
        except Exception:  # noqa: BLE001 — 보강 실패는 무시
            continue
    return ""


def _fill_missing_abstracts_by_doi(df):
    """초록이 비었지만 DOI 가 있는 논문을 보강한다.

    두 단계로 시도한다:
      1. Semantic Scholar 직접 조회 (모든 발행사)
      2. Springer Nature Metadata API (SN 계열 DOI 만, 키가 있을 때)

    2단계가 필요한 이유 — 폐쇄형 논문의 초록은 OpenAlex/Crossref/S2 어디에도
    없다(발행사가 재배포를 막는다). 실측: 결손 20편 중 SN 계열 8편이 다른
    소스에서 전부 실패했지만 Metadata API 로는 8/8 회수됐다.
    """
    targets = []
    for idx, row in df.iterrows():
        abstract = str(row.get("abstract", "") or "").strip()
        doi = str(row.get("doi", "") or "").strip()
        if doi and (len(abstract) <= 20 or abstract == "nan"):
            targets.append((idx, doi))
    if not targets:
        return df

    logger.info("Looking up %d missing abstracts by DOI via S2...", len(targets))
    api_key = os.environ.get("S2_API_KEY", "")
    headers = {"x-api-key": api_key} if api_key else {}

    def _fetch_one(doi):
        try:
            resp = requests.get(
                f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}",
                headers=headers, params={"fields": "abstract"}, timeout=10)
            if resp.status_code == 200:
                return resp.json().get("abstract") or ""
        except Exception:  # noqa: BLE001 — 보강 실패는 무시
            pass
        return ""

    filled = 0
    still: list[tuple] = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(_fetch_one, doi): (idx, doi)
                   for idx, doi in targets}
        for future in as_completed(futures):
            idx, doi = futures[future]
            try:
                abstract = future.result()
            except Exception:  # noqa: BLE001
                abstract = ""
            if len(abstract) > 20:
                df.at[idx, "abstract"] = abstract
                filled += 1
            else:
                still.append((idx, doi))

    if filled:
        logger.info("Filled %d/%d missing abstracts via S2 DOI lookup",
                    filled, len(targets))

    # 2단계: Springer Nature Metadata API — 폐쇄형 SN 논문의 마지막 수단.
    sn_key = springer_meta_key()
    sn_targets = [(idx, doi) for idx, doi in still
                  if doi.split("/")[0] in _SPRINGER_PREFIXES]
    if sn_key and sn_targets:
        logger.info("Looking up %d Springer Nature abstracts via Metadata API...",
                    len(sn_targets))
        sn_filled = 0
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = {executor.submit(_springer_abstract, doi, sn_key): idx
                       for idx, doi in sn_targets}
            for future in as_completed(futures):
                try:
                    abstract = future.result()
                except Exception:  # noqa: BLE001
                    continue
                if len(abstract) > 20:
                    df.at[futures[future], "abstract"] = abstract
                    sn_filled += 1
        if sn_filled:
            logger.info("Filled %d/%d abstracts via Springer Nature Metadata",
                        sn_filled, len(sn_targets))
    elif sn_targets and not sn_key:
        logger.info("Springer Nature 계열 %d편의 초록이 비었으나 Metadata API "
                    "키가 없다 (SPRINGER_META_API_KEY)", len(sn_targets))

    return df


def _crossref_headers() -> dict:
    """Crossref polite pool 헤더. mailto 를 넣으면 우선 처리된다."""
    email = (os.environ.get("CROSSREF_EMAIL")
             or os.environ.get("OPENALEX_EMAIL") or "").strip()
    ua = "paper-curation-citedby/1.0"
    if email:
        ua += f" (mailto:{email})"
    return {"User-Agent": ua}


def _crossref_date(msg: dict) -> str:
    """Crossref date-parts → ISO 날짜. 연도만 있으면 연도만 돌려준다."""
    for key in ("published", "published-print", "published-online", "issued"):
        parts = ((msg.get(key) or {}).get("date-parts") or [[]])[0]
        if not parts:
            continue
        nums = [int(p) for p in parts if isinstance(p, int)]
        if len(nums) >= 3:
            return f"{nums[0]:04d}-{nums[1]:02d}-{nums[2]:02d}"
        if len(nums) == 2:
            return f"{nums[0]:04d}-{nums[1]:02d}"
        if len(nums) == 1:
            return f"{nums[0]:04d}"
    return ""


def _crossref_authors(msg: dict) -> str:
    """Crossref author → "First Last; ..." 문자열.

    Crossref 는 given/family 를 분리해 주므로 출처 중 가장 정확하다.
    단일명(mononym)은 family 만 오는데(예: Nature 기자 'Ananya') 정상이다.
    """
    names = []
    for a in (msg.get("author") or []):
        if a.get("name"):                      # 기관 저자
            names.append(a["name"].strip())
            continue
        full = " ".join(x for x in (a.get("given"), a.get("family")) if x)
        if full.strip():
            names.append(full.strip())
    return "; ".join(names)


# Crossref 로 채울 필드 → 응답에서 값을 뽑는 함수.
_CROSSREF_FIELDS = {
    "volume": lambda m: (m.get("volume") or "").strip(),
    "issue": lambda m: (m.get("issue") or "").strip(),
    "pages": lambda m: (m.get("page") or "").strip(),
    "issn": lambda m: "; ".join(m.get("ISSN") or []),
    "publisher": lambda m: (m.get("publisher") or "").strip(),
    "language": lambda m: (m.get("language") or "").strip(),
    "item_type": lambda m: (m.get("type") or "").strip(),
    "journal": lambda m: ((m.get("container-title") or [""]) or [""])[0].strip(),
    "author_names": _crossref_authors,
}

CROSSREF_PARALLEL = int(os.environ.get("CITEDBY_CROSSREF_PARALLEL", "8"))


def _needs_crossref(row) -> bool:
    """Crossref 를 조회할 가치가 있는 행인지.

    권/페이지가 비었거나 날짜가 연도까지밖에 없으면 보강 대상. 이미 모두
    채워져 있으면 요청을 아낀다.
    """
    if _is_empty(row.get("doi")):
        return False
    if _is_empty(row.get("volume")) or _is_empty(row.get("pages")):
        return True
    return len(str(row.get("date") or "").strip()) < 10


def _safe_set(df, idx, col, value) -> None:
    """dtype 충돌 없이 셀에 값을 쓴다.

    pandas 의 문자열 dtype 컬럼에 int 를 넣으면 TypeError 가 난다 (year/month
    를 채울 때 실제로 터졌다). 충돌하면 해당 컬럼만 object 로 승격시킨다.
    """
    try:
        df.at[idx, col] = value
    except (TypeError, ValueError):
        df[col] = df[col].astype(object)
        df.at[idx, col] = value


def enrich_from_crossref(df, progress_callback=None):
    """DOI 기준으로 Crossref 서지정보를 보강한다.

    Crossref 는 DOI 등록기관이 직접 넣은 **정본** 메타데이터라 권/호/페이지·
    발행일·ISSN·발행사·저자 표기가 검색 인덱스(OpenAlex/S2)보다 정확하다.
    키도 기관망도 필요 없다.

    정책:
      * **빈 필드만 채운다** — 상위 source 가 준 값을 덮지 않는다.
      * 단 `date` 는 예외로, **더 정밀한 날짜면 승격**한다
        ("2025" → "2025-08-20"). 연도만 남는 게 이 보강의 주된 동기다.
    """
    import pandas as pd  # noqa: F401 — df 연산에 필요

    if df.empty:
        return df

    targets = [(idx, str(row["doi"]).strip())
               for idx, row in df.iterrows() if _needs_crossref(row)]
    if not targets:
        return df

    if progress_callback:
        progress_callback("crossref", f"Crossref 서지 보강: {len(targets)}편")
    logger.info("Crossref 보강 대상 %d편", len(targets))

    headers = _crossref_headers()

    def _fetch(doi):
        try:
            resp = requests.get(f"https://api.crossref.org/works/{doi}",
                                headers=headers, timeout=15)
            if resp.status_code == 200:
                return resp.json().get("message") or {}
        except Exception:  # noqa: BLE001 — 보강 실패는 무시하고 원본 유지
            pass
        return None

    filled = 0
    workers = max(1, min(CROSSREF_PARALLEL, len(targets)))
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = {ex.submit(_fetch, doi): idx for idx, doi in targets}
        for future in as_completed(futures):
            idx = futures[future]
            try:
                msg = future.result()
            except Exception:  # noqa: BLE001
                continue
            if not msg:
                continue

            touched = False
            row_src = str(df.at[idx, "source"] or "")
            for field, getter in _CROSSREF_FIELDS.items():
                value = getter(msg)
                if not value:
                    continue
                # Crossref 가 이 필드에서 현재 값을 준 source 보다 권위가 높으면
                # **덮어쓴다** (전역 순위 2위). 비어 있으면 당연히 채운다.
                # 초록은 `_FIELD_AUTHORITY` 때문에 Crossref 가 최하위라, 이미
                # 값이 있으면 건드리지 않는다.
                if (_is_empty(df.at[idx, field])
                        or _field_rank(field, "crossref")
                        < _field_rank(field, row_src)):
                    _safe_set(df, idx, field, value)
                    touched = True

            # 피인용수는 병합하지 않고 Crossref 칸에 따로 적는다.
            cr_cites = msg.get("is-referenced-by-count")
            if cr_cites is not None:
                _safe_set(df, idx, "citations_crossref", int(cr_cites))
                if _is_empty(df.at[idx, "citations_asof"]):
                    _safe_set(df, idx, "citations_asof", _today())
                touched = True

            # date 는 **더 정밀할 때만** 덮는다 ("2025" → "2025-08-20").
            cr_date = _crossref_date(msg)
            cur_date = str(df.at[idx, "date"] or "").strip()
            if len(cr_date) > len(cur_date):
                _safe_set(df, idx, "date", cr_date)
                if len(cr_date) >= 4:
                    _safe_set(df, idx, "year", int(cr_date[:4]))
                if len(cr_date) >= 7:
                    _safe_set(df, idx, "month", int(cr_date[5:7]))
                touched = True

            if touched:
                filled += 1

    # Crossref 피인용수가 새로 들어왔을 수 있으니 대표값을 다시 고른다.
    if not df.empty:
        picked = [_pick_citation_count(r) for _, r in df.iterrows()]
        df["citationCount"] = [v if v is not None else 0 for v, _ in picked]
        df["citations_source"] = [s for _, s in picked]

    if filled:
        logger.info("Crossref 보강 완료: %d/%d편", filled, len(targets))
        if progress_callback:
            progress_callback("crossref", f"Crossref 보강 완료: {filled}편")
    return df


def _is_empty(val) -> bool:
    """필드가 사실상 비었는지.

    NOTE: **"0" 은 빈 값이 아니다.** 예전엔 피인용수 0 을 결측으로 보려고
    "0"/"0.0" 을 여기 넣었는데, 최근 논문의 피인용 0 은 정상값이라 그러면
    없는 인용을 만들어낸다. 피인용수는 이제 병합 대상이 아니고, 결측 판정은
    필드 부재(None/빈 문자열)로만 한다.
    """
    if val is None:
        return True
    s = str(val).strip()
    return not s or s in ("nan", "None", "<NA>")


def _merge_by_priority(df):
    """제목 기준으로 dedup 하고, **필드별 권위**에 따라 값을 고른다.

    예전에는 "최우선 source 레코드를 베이스로 삼고 하위가 빈 칸만 채우는"
    방식이었다. 그러면 필드마다 권위가 다른 현실을 담지 못한다 — 서지는
    Crossref/Scopus 가 강하지만 초록은 OpenAlex/S2 가 강하다(실측: Crossref
    초록 7/25 vs OpenAlex 13/25).

    그래서 필드마다 `_field_rank()` 로 가장 권위 있는 source 의 값을 고른다.
    같은 순위면 먼저 온 값을 유지한다. abstract 는 예외로, 기존 내용을 포함하는
    더 긴 버전이면 순위와 무관하게 승격한다 (잘린 초록 방지).

    피인용수는 **병합하지 않는다** — 소스별 컬럼에 그대로 두고, 대표값만
    `_pick_citation_count()` 로 파생한다.
    """
    if df.empty:
        return df

    import pandas as pd

    df = df.copy()
    df["_src_priority"] = df["source"].map(_SOURCE_PRIORITY).fillna(99).astype(int)
    df["_dedup_key"] = df["title"].fillna("").str.lower().str.strip()
    df = df.sort_values(["_src_priority"], ascending=[True])

    merged: dict[str, dict] = {}
    # dedup_key → {field: 그 값을 준 source 의 해당 필드 순위}
    field_rank: dict[str, dict] = {}
    enriched = 0

    for _, row in df.iterrows():
        key = row["_dedup_key"]
        src = row.get("source") or ""

        if key not in merged:
            merged[key] = row.to_dict()
            field_rank[key] = {
                f: (_field_rank(f, src) if not _is_empty(row.get(f)) else 99)
                for f in _ENRICH_FIELDS
            }
            continue

        base = merged[key]
        ranks = field_rank[key]

        # 소스별 피인용수는 서로 다른 측정계라 덮지 않고 각자 칸에 모은다.
        for col in _CITATION_COLUMNS:
            if col in ("citationCount", "citations_asof"):
                continue
            val = row.get(col)
            if val is not None and not _is_empty(val) and _is_empty(base.get(col)):
                base[col] = val
        if _is_empty(base.get("citations_asof")) and row.get("citations_asof"):
            base["citations_asof"] = row["citations_asof"]

        for field in _ENRICH_FIELDS:
            new_val = row.get(field)
            if _is_empty(new_val):
                continue
            base_val = base.get(field)
            new_rank = _field_rank(field, src)

            if field == "abstract":
                base_str = "" if _is_empty(base_val) else str(base_val).strip()
                new_str = str(new_val).strip()
                if not base_str:
                    base[field], ranks[field] = new_val, new_rank
                    enriched += 1
                elif new_rank < ranks.get(field, 99):
                    base[field], ranks[field] = new_val, new_rank
                    enriched += 1
                elif len(new_str) > len(base_str) and base_str in new_str:
                    # 잘린 초록의 더 긴 판본은 순위와 무관하게 승격
                    base[field] = new_val
                    enriched += 1
            elif _is_empty(base_val) or new_rank < ranks.get(field, 99):
                base[field], ranks[field] = new_val, new_rank
                enriched += 1

    if enriched:
        logger.info("Enriched %d fields from lower-priority sources", enriched)

    result = pd.DataFrame(list(merged.values()))
    # 대표 피인용수 파생 — 정렬·표시용. 소스별 원본은 그대로 남는다.
    if not result.empty:
        picked = [_pick_citation_count(r) for _, r in result.iterrows()]
        result["citationCount"] = [v if v is not None else 0 for v, _ in picked]
        result["citations_source"] = [s for _, s in picked]

    drop_cols = [c for c in ("_src_priority", "_dedup_key") if c in result.columns]
    if drop_cols:
        result = result.drop(columns=drop_cols)
    return result.reset_index(drop=True)
