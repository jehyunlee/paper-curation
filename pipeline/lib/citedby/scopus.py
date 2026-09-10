"""Scopus REST API 인프라 — 키 로테이션 + 검색결과 변환.

scisci `lib/retrieval.py` 에서 citing 경로가 실제로 쓰는 부분만 발췌 이식했다
(원본 2,073 줄 중 ~130 줄). 발췌 기준은 `citing.get_citing_from_scopus` 가
import 하던 5개 심볼이다:

    SCOPUS_SEARCH_URL, _get_scopus_api_keys, _get_next_scopus_key,
    _rotate_scopus_key, scopus_results_to_df

Credential lookup is lazy and uses the shared environment-or-OS-keyring resolver.
"""
from __future__ import annotations

import datetime
import logging

from lib.credentials import CredentialsError, resolve_credential

logger = logging.getLogger(__name__)


def _today() -> str:
    """피인용수 수집 시점. 숫자는 시간이 지나면 낡으므로 함께 기록한다."""
    return datetime.date.today().isoformat()

SCOPUS_SEARCH_URL = "https://api.elsevier.com/content/search/scopus"
SCOPUS_ABSTRACT_URL = "https://api.elsevier.com/content/abstract/eid"

_api_keys: list[str] | None = None
_key_index = 0
_key_origin = ""


def inst_token() -> str:
    """기관 토큰(X-ELS-Insttoken). 원격 접속에서 entitlement 를 실어 준다.

    없으면 빈 문자열 — 기관 IP 안에서는 없어도 동작한다.
    """
    try:
        return resolve_credential("scopus-inst")
    except CredentialsError:
        return ""


def get_api_keys() -> list[str]:
    """Scopus API 키 목록 (1회 캐싱).

    환경변수와 OS 보안 저장소를 순서대로 조회한다. 키가 여러 개면 쉼표로
    구분한다 (쿼터 소진 시 회전).

    Raises:
        FileNotFoundError: 어디에도 키가 없을 때.
    """
    global _api_keys, _key_origin
    if _api_keys is not None:
        return _api_keys

    try:
        raw = resolve_credential("scopus")
    except CredentialsError as exc:
        raise FileNotFoundError(
            "Scopus API key not found. Set SCOPUS_API_KEY/ELSEVIER_API_KEY "
            "or credential:scopus in the OS secure store."
        ) from exc
    keys = [key.strip().strip('"') for key in raw.split(",") if key.strip()]
    if not keys:
        raise FileNotFoundError("Scopus API key is empty.")
    _api_keys, _key_origin = keys, "credential:scopus"
    logger.info("Loaded %d Scopus API key(s) from credential:scopus", len(keys))
    return _api_keys


def key_origin() -> str:
    """키를 어디서 읽었는지 (진단용)."""
    return _key_origin


def headers(accept_json: bool = True) -> dict:
    """Scopus 호출 공통 헤더. 기관 토큰이 있으면 함께 싣는다."""
    h = {"X-ELS-APIKey": next_key()}
    if accept_json:
        h["Accept"] = "application/json"
    token = inst_token()
    if token:
        h["X-ELS-Insttoken"] = token
    return h


def next_key() -> str:
    """현재 인덱스의 API 키."""
    keys = get_api_keys()
    return keys[_key_index % len(keys)]


def rotate_key() -> None:
    """쿼터 소진(429)/인증 실패(401) 시 다음 키로 회전."""
    global _key_index
    keys = get_api_keys()
    _key_index = (_key_index + 1) % len(keys)
    logger.info("Rotated to Scopus API key index %d", _key_index)


def available() -> tuple[bool, str]:
    """Scopus 키 보유 여부. (ok, 사유).

    키 존재만 본다 — **권한 등급은 여기서 알 수 없다.** 같은 키라도 Search 는
    200, `REFEID()` citing 검색은 400, Abstract `view=REF` 는 401 이 나올 수
    있다(실측). 등급 판정은 `probe()` 가 실제 호출로 한다.
    """
    try:
        get_api_keys()
    except FileNotFoundError as e:
        return False, str(e)
    except Exception as e:  # noqa: BLE001 — 배지 표시용, 절대 실패시키지 않는다
        return False, f"키 조회 실패: {e}"
    return True, ""


def probe(doi: str = "10.1038/s41586-024-07618-3") -> dict:
    """Scopus 권한 등급을 실제 호출로 판정한다.

    키가 있어도 계약 등급에 따라 되는 API 가 다르다. 실측 결과:
        Search API (서지·피인용수)  → 200 OK
        REFEID() citing 검색        → 400 INVALID_INPUT
        Abstract view=REF (레퍼런스) → 401 AUTHORIZATION_ERROR

    Returns:
        {"search": bool, "citing": bool, "references": bool, "detail": {...}}
    """
    import requests

    result = {"search": False, "citing": False, "references": False, "detail": {}}
    ok, reason = available()
    if not ok:
        result["detail"]["key"] = reason
        return result

    eid = ""
    try:
        r = requests.get(SCOPUS_SEARCH_URL, headers=headers(),
                         params={"query": f'DOI("{doi}")', "count": 1}, timeout=20)
        result["detail"]["search"] = r.status_code
        if r.status_code == 200:
            result["search"] = True
            entries = (r.json().get("search-results") or {}).get("entry") or []
            if entries:
                eid = entries[0].get("eid", "")
    except Exception as e:  # noqa: BLE001
        result["detail"]["search"] = f"error: {str(e)[:80]}"
        return result

    if not eid:
        return result

    try:
        r = requests.get(SCOPUS_SEARCH_URL, headers=headers(),
                         params={"query": f"REFEID({eid})", "count": 1}, timeout=20)
        result["detail"]["citing"] = r.status_code
        result["citing"] = r.status_code == 200
    except Exception as e:  # noqa: BLE001
        result["detail"]["citing"] = f"error: {str(e)[:80]}"

    try:
        r = requests.get(f"{SCOPUS_ABSTRACT_URL}/{eid}", headers=headers(),
                         params={"view": "REF"}, timeout=20)
        result["detail"]["references"] = r.status_code
        result["references"] = r.status_code == 200
    except Exception as e:  # noqa: BLE001
        result["detail"]["references"] = f"error: {str(e)[:80]}"

    return result


def results_to_df(results):
    """Scopus Search API JSON entry 리스트 → DataFrame (CITING_COLUMNS 호환).

    pandas 는 지연 import — citedby 를 안 쓰는 파이프라인 기동에 영향 없게 한다.
    """
    import pandas as pd

    rows = []
    for s in results:
        try:
            cover_date = s.get("prism:coverDate", "")
            affiliations = s.get("affiliation", [])
            if not isinstance(affiliations, list):
                affiliations = [affiliations] if affiliations else []

            author_count_raw = s.get("author-count")
            if isinstance(author_count_raw, dict):
                author_count = int(author_count_raw.get("$", 0) or 0)
            else:
                author_count = int(author_count_raw or 0)

            rows.append({
                "title": s.get("dc:title", ""),
                "abstract": s.get("dc:description", ""),
                "date": cover_date,
                "year": int(cover_date[:4]) if len(cover_date) >= 4 else None,
                "month": int(cover_date[5:7]) if len(cover_date) >= 7 else None,
                "doi": s.get("prism:doi", ""),
                "eid": s.get("eid", ""),
                "arxiv_id": "",
                "pdf_url": "",
                "journal": s.get("prism:publicationName", ""),
                "volume": s.get("prism:volume", ""),
                "issue": s.get("prism:issueIdentifier", "") or "",
                "pages": s.get("prism:pageRange", ""),
                "issn": s.get("prism:issn", "") or s.get("prism:eIssn", "") or "",
                "publisher": "",
                "language": "",
                "item_type": s.get("subtypeDescription", "") or "",
                "citations_scopus": int(s.get("citedby-count", 0) or 0),
                "citations_crossref": None,
                "citations_openalex": None,
                "citations_s2": None,
                "citations_percentile": None,
                "citations_asof": _today(),
                "citationCount": int(s.get("citedby-count", 0) or 0),
                "af_city": ";".join(a.get("affiliation-city", "") or "" for a in affiliations),
                "af_country": ";".join(a.get("affiliation-country", "") or "" for a in affiliations),
                "af_id": ";".join(a.get("afid", "") or "" for a in affiliations),
                "af_name": ";".join(a.get("affilname", "") or "" for a in affiliations),
                "au_keywords": s.get("authkeywords", ""),
                "author_afids": "",
                "author_count": author_count,
                "author_ids": "",
                "author_names": s.get("dc:creator", ""),
                "source": "scopus",
            })
        except Exception as e:  # noqa: BLE001 — 한 건 파싱 실패가 전체를 죽이지 않게
            logger.warning("Failed to parse Scopus result: %s", e)
    return pd.DataFrame(rows)
