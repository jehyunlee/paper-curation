"""Scopus REST API 인프라 — 키 로테이션 + 검색결과 변환.

scisci `lib/retrieval.py` 에서 citing 경로가 실제로 쓰는 부분만 발췌 이식했다
(원본 2,073 줄 중 ~130 줄). 발췌 기준은 `citing.get_citing_from_scopus` 가
import 하던 5개 심볼이다:

    SCOPUS_SEARCH_URL, _get_scopus_api_keys, _get_next_scopus_key,
    _rotate_scopus_key, scopus_results_to_df

NOTE: `pybliometrics` 패키지 자체는 의존성이 아니다. 이 모듈은 pybliometrics 가
남긴 **설정 파일**(`~/.config/pybliometrics.cfg`)에서 API 키만 configparser 로
읽고, 호출은 순수 `requests` 로 한다. 따라서 requirements 에 pybliometrics 를
추가할 필요가 없다.
"""
from __future__ import annotations

import configparser
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

SCOPUS_SEARCH_URL = "https://api.elsevier.com/content/search/scopus"

_CFG_CANDIDATES = (
    Path.home() / ".config" / "pybliometrics.cfg",
    Path.home() / ".pybliometrics" / "pybliometrics.cfg",
)

_api_keys: list[str] | None = None
_key_index = 0


def config_path() -> Path | None:
    """존재하는 pybliometrics.cfg 경로. 없으면 None."""
    for p in _CFG_CANDIDATES:
        if p.exists():
            return p
    return None


def get_api_keys() -> list[str]:
    """pybliometrics.cfg 에서 Scopus API 키 목록을 읽는다 (1회 캐싱).

    Raises:
        FileNotFoundError: cfg 파일이 없을 때.
        ValueError: cfg 에 키가 비어 있을 때.
    """
    global _api_keys
    if _api_keys is not None:
        return _api_keys

    cfg_path = config_path()
    if cfg_path is None:
        raise FileNotFoundError(
            "pybliometrics.cfg not found. Expected at "
            "~/.config/pybliometrics.cfg or ~/.pybliometrics/pybliometrics.cfg"
        )

    cfg = configparser.ConfigParser()
    cfg.read(cfg_path)
    keys_str = cfg.get("Authentication", "APIKey", fallback="")
    keys = [k.strip().strip('"') for k in keys_str.split(",") if k.strip()]
    if not keys:
        raise ValueError(f"No API keys found in {cfg_path}")

    _api_keys = keys
    logger.info("Loaded %d Scopus API key(s) from %s", len(keys), cfg_path)
    return _api_keys


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
    """Scopus 사용 가능 여부. (ok, 사유) 반환.

    설정 존재 여부만 본다 — 기관 IP 도달성은 실제 호출에서 판정한다.
    UI 배지용이라 예외를 던지지 않는다.
    """
    try:
        get_api_keys()
    except FileNotFoundError:
        return False, "pybliometrics.cfg 없음 (~/.config/pybliometrics.cfg)"
    except ValueError as e:
        return False, str(e)
    except Exception as e:  # noqa: BLE001 — 배지 표시용, 절대 실패시키지 않는다
        return False, f"설정 읽기 실패: {e}"
    return True, ""


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
                "year": int(cover_date[:4]) if len(cover_date) >= 4 else None,
                "month": int(cover_date[5:7]) if len(cover_date) >= 7 else None,
                "doi": s.get("prism:doi", ""),
                "eid": s.get("eid", ""),
                "arxiv_id": "",
                "pdf_url": "",
                "journal": s.get("prism:publicationName", ""),
                "volume": s.get("prism:volume", ""),
                "pages": s.get("prism:pageRange", ""),
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
