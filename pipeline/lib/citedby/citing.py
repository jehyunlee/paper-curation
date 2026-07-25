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

# citing 논문 통합 컬럼 — 모든 source 의 레코드가 이 스키마로 정규화된다.
CITING_COLUMNS = [
    "doi", "eid", "arxiv_id", "title", "abstract", "journal",
    "year", "month", "volume", "pages", "citationCount", "source",
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

    af_names, af_countries = [], []
    for a in authorships:
        for inst in (a.get("institutions") or []):
            af_names.append(inst.get("display_name") or "")
            af_countries.append(inst.get("country_code") or "")

    return {
        "title": w.get("display_name") or w.get("title") or "",
        "abstract": reconstruct_abstract(w.get("abstract_inverted_index")),
        "year": int(pub_date[:4]) if len(pub_date) >= 4 else None,
        "month": int(pub_date[5:7]) if len(pub_date) >= 7 else None,
        "doi": (w.get("doi") or "").replace("https://doi.org/", ""),
        "eid": "",
        "arxiv_id": "",
        "pdf_url": loc.get("pdf_url") or loc.get("landing_page_url") or "",
        "journal": source_info.get("display_name", ""),
        "volume": "",
        "pages": "",
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
            "select": "id,doi,title,display_name,publication_date,primary_location,"
                      "authorships,cited_by_count,abstract_inverted_index,type",
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
    headers = {"Accept": "application/json", "X-ELS-APIKey": _scopus.next_key()}
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
                headers["X-ELS-APIKey"] = _scopus.next_key()
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
              "citationCount,authors,openAccessPdf")
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
                    "year": int(pub_date[:4]) if len(pub_date) >= 4 else None,
                    "month": int(pub_date[5:7]) if len(pub_date) >= 7 else None,
                    "doi": ext_ids.get("DOI", ""),
                    "eid": "",
                    "arxiv_id": ext_ids.get("ArXiv", ""),
                    "pdf_url": oa_pdf.get("url", ""),
                    "journal": journal.get("name", "") or "",
                    "volume": journal.get("volume", "") or "",
                    "pages": journal.get("pages", "") or "",
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
                    "year": paper.published.year if paper.published else None,
                    "month": paper.published.month if paper.published else None,
                    "doi": paper.doi or "",
                    "eid": "",
                    "arxiv_id": aid,
                    "pdf_url": paper.pdf_url or "",
                    "journal": "",
                    "volume": "",
                    "pages": "",
                    "citationCount": 0,  # arXiv 는 제공하지 않음
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

# 병합 우선순위 — 낮을수록 우선. Scopus 가 서지 필드가 가장 조밀하다.
_SOURCE_PRIORITY = {
    "scopus": 0,
    "wos": 1,
    "arxiv": 2,
    "openalex": 3,
    "semanticscholar": 4,
}

_ENRICH_FIELDS = [c for c in CITING_COLUMNS if c != "source"]


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

    logger.info("Total citing papers after dedup: %d (raw: %d)",
                len(df), sum(source_counts.values()))
    return df, source_counts


def _fill_missing_abstracts_by_doi(df):
    """초록이 비었지만 DOI 가 있는 논문을 S2 직접 조회로 보강."""
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
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(_fetch_one, doi): idx for idx, doi in targets}
        for future in as_completed(futures):
            try:
                abstract = future.result()
            except Exception:  # noqa: BLE001
                continue
            if len(abstract) > 20:
                df.at[futures[future], "abstract"] = abstract
                filled += 1

    if filled:
        logger.info("Filled %d/%d missing abstracts via S2 DOI lookup",
                    filled, len(targets))
    return df


def _is_empty(val) -> bool:
    """필드가 사실상 비었는지. pandas NaN/문자열 'nan'/0 을 모두 빈 값으로 본다."""
    if val is None:
        return True
    s = str(val).strip()
    return not s or s in ("nan", "0", "None", "0.0")


def _merge_by_priority(df):
    """source 우선순위로 논문을 병합한다 (제목 기준 dedup).

    1. 우선순위 오름차순·피인용 내림차순 정렬
    2. 같은 제목의 첫(최우선) 레코드를 베이스로 삼고
    3. 하위 source 레코드로 빈 필드를 채운다
       - abstract: 기존 내용을 포함하는 **더 긴** 버전이면 승격
       - citationCount: 더 큰 값 유지
    """
    if df.empty:
        return df

    df = df.copy()
    df["_src_priority"] = df["source"].map(_SOURCE_PRIORITY).fillna(99).astype(int)
    df["_dedup_key"] = df["title"].fillna("").str.lower().str.strip()
    df = df.sort_values(["_src_priority", "citationCount"], ascending=[True, False])

    merged: dict[str, dict] = {}
    enriched = 0

    for _, row in df.iterrows():
        key = row["_dedup_key"]
        if key not in merged:
            merged[key] = row.to_dict()
            continue

        base = merged[key]
        for field in _ENRICH_FIELDS:
            new_val = row.get(field)
            if _is_empty(new_val):
                continue
            base_val = base.get(field)

            if field == "abstract":
                base_str = "" if _is_empty(base_val) else str(base_val).strip()
                new_str = str(new_val).strip()
                if not base_str:
                    base[field] = new_val
                    enriched += 1
                elif len(new_str) > len(base_str) and base_str in new_str:
                    base[field] = new_val
                    enriched += 1
            elif field == "citationCount":
                try:
                    if int(new_val) > int(base_val or 0):
                        base[field] = new_val
                        enriched += 1
                except (ValueError, TypeError):
                    pass
            elif _is_empty(base_val):
                base[field] = new_val
                enriched += 1

    if enriched:
        logger.info("Enriched %d fields from lower-priority sources", enriched)

    import pandas as pd
    result = pd.DataFrame(list(merged.values()))
    drop_cols = [c for c in ("_src_priority", "_dedup_key") if c in result.columns]
    if drop_cols:
        result = result.drop(columns=drop_cols)
    return result.reset_index(drop=True)
