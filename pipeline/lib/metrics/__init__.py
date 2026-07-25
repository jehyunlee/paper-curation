"""metrics — 코퍼스 논문의 피인용수·레퍼런스 수집.

paper-curation 을 적용한 논문(`docs/papers/{slug}/`)마다 두 파일을 만든다:

    citations.md   피인용수 **이력** + (임계값 이상이면) 이 논문을 인용한 논문 목록
    references.md  이 논문이 인용한 논문 목록

설계 원칙 — 운영자 결정:
  * **데이터가 먼저다.** 사이트 표시는 부수적이라 지금은 하지 않는다. 데이터가
    잘 쌓여 있으면 표시는 나중에 언제든 만들 수 있지만 반대는 안 된다.
  * **대상은 Zotero 전체가 아니라 큐레이션한 논문**이다. 파일이 논문 디렉토리
    안에 있으니 범위가 자연히 한정되고, `zotero_item_key` 커버리지 2% 문제도
    사라진다.
  * **덮어쓰지 않고 쌓는다.** 월 1회 갱신이 이력으로 누적돼 인용 속도를 남긴다.

소스 권위 (실측 근거는 `citedby.citing` 참조):
    서지·피인용수   Scopus > Crossref > OpenAlex > S2
    citing 목록     OpenAlex  (Scopus 는 REFEID 가 400 — entitlement 부족)
    references     Crossref  (Scopus 는 view=REF 가 401)

지연 로딩(PEP 562): import 만으로는 pandas/requests 를 끌어오지 않는다.
"""
from __future__ import annotations

import importlib

__all__ = [
    # collect.py — 수집
    "collect_paper_metrics",
    "fetch_citation_counts",
    "fetch_citing_papers",
    "fetch_references",
    # store.py — citations.md / references.md 읽기·쓰기
    "read_citations",
    "write_citations",
    "write_references",
    "needs_refresh",
    "CitationSnapshot",
]

_COLLECT_EXPORTS = frozenset({
    "collect_paper_metrics", "fetch_citation_counts",
    "fetch_citing_papers", "fetch_references",
})
_STORE_EXPORTS = frozenset({
    "read_citations", "write_citations", "write_references",
    "needs_refresh", "CitationSnapshot",
})


def __getattr__(name: str):
    """하위 모듈을 최초 접근 시점에 로드 (PEP 562).

    `importlib.import_module` 을 쓰는 이유는 citedby 패키지와 동일 —
    `from . import x` 는 부모 `hasattr` 검사를 타서 순환이 날 수 있다.
    """
    if name in _COLLECT_EXPORTS:
        return getattr(importlib.import_module(".collect", __name__), name)
    if name in _STORE_EXPORTS:
        return getattr(importlib.import_module(".store", __name__), name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(__all__)
