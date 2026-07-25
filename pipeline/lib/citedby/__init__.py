"""citedby — DOI 하나로 인용논문을 수집·분석하는 서브패키지.

scisci(`jehyunlee/scisci`) 의 citedby 웹앱 코어를 paper-curation 으로 이식한
것이다. Flask/SSE/세션 계층은 버리고 **순수 로직만** 가져왔다 — 진입점은
로컬 웹앱(`serve_local.py` 의 `/api/citedby`)과 CLI(`run_citedby.py`) 두 갈래로
붙는다.

paper-curation 의 "같이 보면 좋은 논문"은 SPECTER2 임베딩 **유사도·코퍼스 내부**
축이라, *이 논문을 인용한 새 논문*을 구조적으로 찾지 못한다. citedby 가 그
**인용축·시간축** 공백을 메운다.

지연 로딩(PEP 562): 이 패키지를 import 하는 것만으로는 pandas 를 끌어오지
않는다. 실제 심볼에 접근하는 순간 하위 모듈이 로드된다. citedby 를 쓰지 않는
파이프라인 단계의 기동 비용을 0으로 유지하기 위한 것이다.
"""
from __future__ import annotations

import importlib

__all__ = [
    # citing.py — 인용논문 수집
    "CITING_COLUMNS",
    "UNSUPPORTED_SOURCES",
    "normalize_doi",
    "reconstruct_abstract",
    "fetch_all_citing_papers",
    "get_citing_from_openalex",
    "get_citing_from_scopus",
    "get_citing_from_s2",
    "get_citing_from_arxiv",
    "get_citing_from_wos",
    "enrich_from_crossref",
    # report.py — HTML 리포트(→ 브라우저 PDF) + CSV export
    "build_report_html",
    "papers_to_csv",
    "paper_url",
    # analysis.py — 오케스트레이션 (진입점 둘이 공유)
    "run_citedby",
    "run_citing_analysis",
    "run_topic_analysis",
    "extract_originality_for_papers",
    "fetch_paper_metadata",
    # topic_filter.py — 주제 필터 + 5W1H 요약
    "filter_by_topic",
    "generate_summaries",
    # zotero_links.py — 내 Zotero 라이브러리 PDF 바로열기 링크
    "load_zotero_index",
    "ZoteroIndex",
    # 하위 모듈
    "scopus",
]

_CITING_EXPORTS = frozenset({
    "CITING_COLUMNS", "UNSUPPORTED_SOURCES", "normalize_doi",
    "reconstruct_abstract", "fetch_all_citing_papers",
    "get_citing_from_openalex", "get_citing_from_scopus",
    "get_citing_from_s2", "get_citing_from_arxiv", "get_citing_from_wos",
    "enrich_from_crossref",
})
_REPORT_EXPORTS = frozenset({"build_report_html", "papers_to_csv", "paper_url"})
_ANALYSIS_EXPORTS = frozenset({
    "run_citedby", "run_citing_analysis", "run_topic_analysis",
    "extract_originality_for_papers", "fetch_paper_metadata",
})
_FILTER_EXPORTS = frozenset({"filter_by_topic", "generate_summaries"})
_ZOTERO_EXPORTS = frozenset({"load_zotero_index", "ZoteroIndex"})


def __getattr__(name: str):
    """하위 모듈을 최초 접근 시점에 로드 (PEP 562).

    `importlib.import_module` 를 쓰는 이유: `from . import citing` 형태는
    `_handle_fromlist` 가 부모 패키지에 `hasattr` 를 걸어 확인하는데, 그게 다시
    이 `__getattr__` 를 호출한다. `citing.py` 자신이 `from . import scopus` 를
    하므로 그 경로에서 무한 재귀(RecursionError)가 난다. import_module 은 부모
    속성 조회를 타지 않고 sys.modules 를 직접 보므로 순환이 끊긴다.
    """
    if name == "scopus":
        return importlib.import_module(".scopus", __name__)
    if name in _CITING_EXPORTS:
        citing = importlib.import_module(".citing", __name__)
        return getattr(citing, name)
    if name in _REPORT_EXPORTS:
        report = importlib.import_module(".report", __name__)
        return getattr(report, name)
    if name in _ANALYSIS_EXPORTS:
        analysis = importlib.import_module(".analysis", __name__)
        return getattr(analysis, name)
    if name in _FILTER_EXPORTS:
        topic_filter = importlib.import_module(".topic_filter", __name__)
        return getattr(topic_filter, name)
    if name in _ZOTERO_EXPORTS:
        zotero_links = importlib.import_module(".zotero_links", __name__)
        return getattr(zotero_links, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(__all__)
