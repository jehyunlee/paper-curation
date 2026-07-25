"""논문 하나의 피인용수·인용논문·레퍼런스를 모은다.

호출 예산이 설계의 중심이다. 논문당:

    Crossref  1회  → 피인용수(is-referenced-by-count) + **레퍼런스 목록** 동시
    OpenAlex  1회  → 피인용수 + 연차보정 백분위
    Scopus    1회  → 피인용수 (키가 있고 Search 등급이면)
    OpenAlex  +N   → citing 목록 (피인용 임계값 이상일 때만, 200건/page)

레퍼런스를 위해 별도 호출을 추가하지 않는다 — Crossref 응답에 이미 들어 있다.
그래서 "피인용수만" 과 "피인용수+레퍼런스" 의 비용이 사실상 같다.
"""
from __future__ import annotations

import logging
import os
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

logger = logging.getLogger(__name__)

CROSSREF_URL = "https://api.crossref.org/works"
OPENALEX_URL = "https://api.openalex.org/works"

# citing 목록을 받을 최소 피인용수. 실측 분포상 중앙값이 2회라, 임계값이 없으면
# 대부분의 논문이 "인용 2건" 목록을 갖게 돼 파일만 늘고 읽히지 않는다.
DEFAULT_MIN_CITATIONS = 10

PARALLEL = int(os.environ.get("CITEDBY_METRICS_PARALLEL", "6"))

# OpenAlex citing 목록에서 받을 필드 — 목록 표시에 필요한 최소한.
_CITING_SELECT = "id,doi,title,display_name,publication_year,cited_by_count"


def _ua() -> dict:
    """polite pool 헤더. mailto 가 있으면 우선 처리된다."""
    email = (os.environ.get("CROSSREF_EMAIL")
             or os.environ.get("OPENALEX_EMAIL") or "").strip()
    ua = "paper-curation-metrics/1.0"
    if email:
        ua += f" (mailto:{email})"
    return {"User-Agent": ua}


def _openalex_params() -> dict:
    p = {}
    key = os.environ.get("OPENALEX_API_KEY", "").strip()
    email = os.environ.get("OPENALEX_EMAIL", "").strip()
    if key:
        p["api_key"] = key
    elif email:
        p["mailto"] = email
    return p


# ── 개별 소스 조회 ────────────────────────────────────────────────────────

def _crossref_work(doi: str) -> dict | None:
    """Crossref work 원본. 피인용수와 레퍼런스가 한 응답에 함께 온다."""
    try:
        r = requests.get(f"{CROSSREF_URL}/{urllib.parse.quote(doi)}",
                         headers=_ua(), timeout=20)
        if r.status_code == 200:
            return r.json().get("message") or {}
    except Exception as e:  # noqa: BLE001 — 한 소스 실패가 전체를 막지 않는다
        logger.debug("Crossref 조회 실패 %s: %s", doi, str(e)[:80])
    return None


def _openalex_work(doi: str) -> dict | None:
    """OpenAlex work — 피인용수 + 연차보정 백분위."""
    try:
        r = requests.get(
            f"{OPENALEX_URL}/doi:{urllib.parse.quote(doi)}",
            params={"select": "id,cited_by_count,citation_normalized_percentile,"
                              "referenced_works_count",
                    **_openalex_params()},
            headers=_ua(), timeout=20)
        if r.status_code == 200:
            return r.json()
    except Exception as e:  # noqa: BLE001
        logger.debug("OpenAlex 조회 실패 %s: %s", doi, str(e)[:80])
    return None


def _scopus_citations(doi: str) -> int | None:
    """Scopus 피인용수. 키가 없거나 Search 등급이 아니면 None.

    Scopus 는 자기 색인 안에서만 세므로 OpenAlex/S2 보다 대개 낮다 — 틀린 게
    아니라 **다른 것을 센 것**이라, 병합하지 않고 별도 값으로 보존한다.
    """
    from lib.citedby import scopus as sc

    ok, _ = sc.available()
    if not ok:
        return None
    try:
        r = requests.get(sc.SCOPUS_SEARCH_URL, headers=sc.headers(),
                         params={"query": f'DOI("{doi}")', "count": 1}, timeout=20)
        if r.status_code != 200:
            return None
        entries = (r.json().get("search-results") or {}).get("entry") or []
        if not entries or entries[0].get("error"):
            return None
        return int(entries[0].get("citedby-count", 0) or 0)
    except Exception as e:  # noqa: BLE001
        logger.debug("Scopus 조회 실패 %s: %s", doi, str(e)[:80])
    return None


# ── 공개 API ──────────────────────────────────────────────────────────────

def fetch_citation_counts(doi: str, *, use_scopus: bool = True) -> dict:
    """소스별 피인용수를 모은다. 병합하지 않는다.

    Returns:
        {"openalex": int|None, "crossref": int|None, "scopus": int|None,
         "percentile": float|None, "_crossref_msg": dict|None}
        `_crossref_msg` 는 레퍼런스 추출에 재사용하라고 그대로 딸려 보낸다
        (같은 응답을 두 번 받지 않기 위함).
    """
    out = {"openalex": None, "crossref": None, "scopus": None,
           "percentile": None, "_crossref_msg": None}
    if not doi:
        return out

    cr = _crossref_work(doi)
    if cr is not None:
        out["_crossref_msg"] = cr
        n = cr.get("is-referenced-by-count")
        if n is not None:
            out["crossref"] = int(n)

    oa = _openalex_work(doi)
    if oa:
        n = oa.get("cited_by_count")
        if n is not None:
            out["openalex"] = int(n)
        pct = (oa.get("citation_normalized_percentile") or {}).get("value")
        if pct is not None:
            out["percentile"] = float(pct)

    if use_scopus:
        out["scopus"] = _scopus_citations(doi)

    return out


def fetch_references(doi: str, *, crossref_msg: dict | None = None) -> list[dict]:
    """이 논문이 인용한 논문 목록 (Crossref reference).

    운영자 지정 형식 — DOI 1순위, URL 2순위, 둘 다 없을 때만 제목·1저자·연도·
    출판처를 적는다. Crossref 는 DOI 없는 항목도 구조화 필드(article-title /
    author / journal-title / year) 나 `unstructured`(원문 인용 문자열)를 준다.

    실측 DOI 보유율 64~92%. Scopus 는 Abstract view=REF 가 401 이라 못 쓴다.
    """
    msg = crossref_msg if crossref_msg is not None else _crossref_work(doi)
    if not msg:
        return []

    refs = []
    for i, r in enumerate(msg.get("reference") or [], 1):
        entry = {"n": i, "doi": "", "url": "", "title": "",
                 "first_author": "", "year": "", "venue": "", "raw": ""}
        ref_doi = (r.get("DOI") or "").strip()
        if ref_doi:
            entry["doi"] = ref_doi.lower()
        else:
            # DOI 가 없을 때만 나머지를 채운다 (형식 규칙).
            entry["url"] = (r.get("URL") or "").strip()
            entry["title"] = (r.get("article-title")
                              or r.get("volume-title") or "").strip()
            entry["first_author"] = (r.get("author") or "").strip()
            entry["year"] = str(r.get("year") or "").strip()
            entry["venue"] = (r.get("journal-title")
                              or r.get("series-title") or "").strip()
            # 구조화 필드가 하나도 없으면 원문 인용 문자열이라도 남긴다.
            if not any((entry["title"], entry["first_author"],
                        entry["year"], entry["venue"], entry["url"])):
                entry["raw"] = (r.get("unstructured") or "").strip()
        refs.append(entry)
    return refs


def fetch_citing_papers(doi: str, *, max_results: int = 100000,
                        progress=None) -> list[dict]:
    """이 논문을 인용한 논문 목록 (OpenAlex `cites:` 필터).

    Scopus 는 REFEID() 가 400(entitlement 부족)이라 쓰지 못한다. OpenAlex 가
    커버리지·비용 면에서 유일한 현실적 선택이다.
    """
    try:
        r = requests.get(f"{OPENALEX_URL}/doi:{urllib.parse.quote(doi)}",
                         params={"select": "id", **_openalex_params()},
                         headers=_ua(), timeout=20)
        if r.status_code != 200:
            return []
        work_id = (r.json().get("id") or "").replace("https://openalex.org/", "")
    except Exception as e:  # noqa: BLE001
        logger.debug("OpenAlex work id 조회 실패 %s: %s", doi, str(e)[:80])
        return []
    if not work_id:
        return []

    out: list[dict] = []
    cursor = "*"
    while len(out) < max_results:
        try:
            r = requests.get(OPENALEX_URL, headers=_ua(), timeout=30,
                             params={"filter": f"cites:{work_id}",
                                     "per_page": 200, "cursor": cursor,
                                     "select": _CITING_SELECT,
                                     **_openalex_params()})
            if r.status_code != 200:
                break
            data = r.json()
        except Exception as e:  # noqa: BLE001
            logger.debug("OpenAlex citing 조회 실패 %s: %s", doi, str(e)[:80])
            break

        works = data.get("results") or []
        if not works:
            break
        for w in works:
            out.append({
                "doi": (w.get("doi") or "").replace("https://doi.org/", ""),
                "title": w.get("display_name") or w.get("title") or "",
                "year": w.get("publication_year"),
                "cited_by_count": w.get("cited_by_count") or 0,
            })
        if progress:
            progress(len(out))
        cursor = (data.get("meta") or {}).get("next_cursor")
        if not cursor:
            break

    out.sort(key=lambda p: (-(p.get("cited_by_count") or 0),
                            -(p.get("year") or 0)))
    return out


def collect_paper_metrics(paper: dict, *,
                          min_citations: int = DEFAULT_MIN_CITATIONS,
                          use_scopus: bool = True,
                          want_references: bool = True,
                          want_citing: bool = True) -> dict:
    """논문 하나의 지표를 모은다.

    Args:
        paper: `{"slug","doi","title"}` — `_papers_index.json` 엔트리면 충분.
        min_citations: 이 값 이상일 때만 citing 목록을 받는다.

    Returns:
        {"slug","doi","title","counts","percentile","citing","references",
         "citing_fetched": bool}
    """
    doi = (paper.get("doi") or "").strip()
    result = {
        "slug": paper.get("slug", ""),
        "doi": doi,
        "title": paper.get("title", ""),
        "counts": {"openalex": None, "crossref": None, "scopus": None},
        "percentile": None,
        "citing": [],
        "references": [],
        "citing_fetched": False,
    }
    if not doi:
        return result

    counts = fetch_citation_counts(doi, use_scopus=use_scopus)
    result["counts"] = {k: counts[k] for k in ("openalex", "crossref", "scopus")}
    result["percentile"] = counts["percentile"]

    if want_references:
        result["references"] = fetch_references(
            doi, crossref_msg=counts.get("_crossref_msg"))

    best = max((v for v in result["counts"].values() if v is not None),
               default=0)
    if want_citing and best >= min_citations:
        result["citing"] = fetch_citing_papers(doi)
        result["citing_fetched"] = True

    return result


def collect_many(papers: list[dict], *, on_progress=None, **kw) -> list[dict]:
    """여러 논문을 병렬 수집. 순서는 입력을 따른다."""
    papers = list(papers)
    results: list[dict | None] = [None] * len(papers)
    if not papers:
        return []

    workers = max(1, min(PARALLEL, len(papers)))
    done = 0
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = {ex.submit(collect_paper_metrics, p, **kw): i
                   for i, p in enumerate(papers)}
        for fut in as_completed(futures):
            i = futures[fut]
            try:
                results[i] = fut.result()
            except Exception as e:  # noqa: BLE001 — 한 편 실패가 전체를 막지 않는다
                logger.warning("지표 수집 실패 %s: %s",
                               papers[i].get("slug", ""), str(e)[:100])
                results[i] = None
            done += 1
            if on_progress:
                on_progress(done, len(papers))
    return [r for r in results if r is not None]
