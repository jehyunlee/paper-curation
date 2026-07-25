"""citedby 오케스트레이션 — DOI → 인용논문 → 독창성 → 주제필터 → 요약 → 리포트.

scisci `scie/lib/pipeline_worker.py`("zero Flask dependency" 순수 로직) 이식본.
원본은 Flask 앱이 SSE 로 감싸 쓰던 계층인데, 여기서는 진입점이 둘이다:

    serve_local.py `/api/citedby`  (로컬 웹앱, NDJSON 청크 스트리밍)
    run_citedby.py                 (CLI → paper-curio 브리지)

두 진입점 모두 이 모듈의 순수 함수를 부른다. 이 모듈은 파일을 쓰지 않고
**산출물을 문자열/딕트로 반환**한다 — 저장 위치 결정은 호출부 몫이라 테스트가
네트워크·파일시스템 없이 돌아간다.

이식하며 제거한 중복 (계획된 3건):
  1. originality → paper-curation `lib/originality_extractor` 재사용.
     scisci 의 `get_originality_strict/tagged/llm_batch` 를 가져오지 않았다.
     대신 기존 `extract_originality()`(rule-based → LLM 폴백 → self-learning)를
     **ThreadPool 로 병렬 호출**해 원본의 순차 지연을 없앴다.
  2. LLM 재시도/캐시 → `api/_llm.cached_call` (topic_filter 모듈에서 처리).
  3. 리포트/엑셀 → `report.py` (HTML + stdlib CSV). python-docx/openpyxl 불필요.
"""
from __future__ import annotations

import logging
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
from datetime import datetime
from pathlib import Path

import requests

logger = logging.getLogger(__name__)

DEFAULT_SOURCES = ("scopus", "wos", "openalex", "semanticscholar", "arxiv")

# originality LLM 폴백 동시 실행 수. rule-based 가 대부분을 잡으므로 실제
# 호출은 일부지만, 순차로 돌면 편당 왕복이 그대로 쌓인다.
ORIGINALITY_PARALLEL = int(os.environ.get("CITEDBY_ORIGINALITY_PARALLEL", "8"))


def _noop_event(phase: str, message: str, current: int = 0, total: int = 0):
    """진행 이벤트 기본 싱크."""


def _emit(on_event):
    return on_event or _noop_event


# ── 원논문(seed) 메타 ─────────────────────────────────────────────────────

def fetch_paper_metadata(doi: str) -> dict | None:
    """OpenAlex 에서 원논문 서지정보를 가져온다. 실패하면 None.

    리포트 상단 '원논문' 블록 표시에만 쓰이므로 실패해도 분석은 계속된다.
    """
    from .citing import _openalex_params, _parse_openalex_work

    try:
        resp = requests.get(f"https://api.openalex.org/works/doi:{doi}",
                            params=_openalex_params(), timeout=20)
        if resp.status_code != 200:
            logger.warning("seed 메타 조회 실패 (%s): %s", resp.status_code, doi)
            return None
        info = _parse_openalex_work(resp.json())
    except Exception as e:  # noqa: BLE001 — 비필수 단계
        logger.warning("seed 메타 조회 오류: %s", e)
        return None

    if not info.get("doi"):
        info["doi"] = doi
    return info


# ── 독창성 추출 ───────────────────────────────────────────────────────────

def _originality_categories(text: str, triggers: dict) -> str:
    """추출된 독창성 문장에 걸린 트리거 카테고리 라벨.

    scisci 는 `get_originality_tagged` 로 태그를 따로 계산했지만, 여기서는
    이미 뽑힌 문장을 기존 트리거 사전으로 역조회해 같은 정보를 얻는다
    (모듈 하나를 통째로 이식하지 않기 위한 얇은 어댑터).
    """
    if not text:
        return ""
    low = text.lower()
    hits = {cat for cat, words in (triggers.get("categories") or {}).items()
            if any(w in low for w in words)}
    return "; ".join(sorted(hits))


def extract_originality_for_papers(papers: list[dict], *,
                                   use_llm: bool = True,
                                   on_event=None) -> list[dict]:
    """논문마다 초록에서 독창성 문장을 뽑아 `originality` 키로 붙인다.

    기존 `lib/originality_extractor.extract_originality` 를 그대로 쓴다
    (rule-based → LLM 폴백 → self-learning 트리거 학습 포함).

    Args:
        use_llm: False 면 rule-based 만. 키가 없거나 비용을 아낄 때.
    """
    from lib import originality_extractor as oe

    emit = _emit(on_event)
    papers = [dict(p) for p in (papers or [])]
    total = len(papers)
    if not total:
        return papers

    triggers = oe.load_triggers()

    # 1) rule-based — 무료·즉시. 대부분 여기서 끝난다.
    needs_llm: list[int] = []
    for i, p in enumerate(papers):
        abstract = (p.get("abstract") or "").strip()
        p["originality"] = ""
        p["originality_category"] = ""
        p["originality_source"] = ""
        if not abstract:
            continue
        text = oe._extract_rule_based(abstract, triggers)
        if text:
            p["originality"] = text
            p["originality_category"] = _originality_categories(text, triggers)
            p["originality_source"] = "rule_base"
        else:
            needs_llm.append(i)

    rule_count = sum(1 for p in papers if p["originality"])
    emit("rule_based",
         f"Rule-based: {rule_count}편 추출, {len(needs_llm)}편 LLM 필요",
         rule_count, total)

    if not (use_llm and needs_llm):
        return papers

    # 2) LLM 폴백 — 남은 것만, 병렬로. 원본은 순차라 편당 왕복이 쌓였다.
    emit("llm_originality", f"LLM fallback: {len(needs_llm)}편 처리 중...",
         0, len(needs_llm))

    def _one(idx: int):
        abstract = (papers[idx].get("abstract") or "").strip()
        try:
            text, new_triggers = oe._llm_fallback(abstract)
        except Exception as e:  # noqa: BLE001 — 한 편 실패가 전체를 죽이지 않게
            logger.warning("originality LLM 실패: %s", str(e)[:120])
            return idx, "", []
        return idx, text, new_triggers

    learned: list[str] = []
    done = 0
    workers = max(1, min(ORIGINALITY_PARALLEL, len(needs_llm)))
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for future in as_completed([ex.submit(_one, i) for i in needs_llm]):
            idx, text, new_triggers = future.result()
            done += 1
            if text:
                papers[idx]["originality"] = text
                papers[idx]["originality_category"] = (
                    _originality_categories(text, triggers) or "llm_detected")
                papers[idx]["originality_source"] = "llm"
            learned.extend(new_triggers or [])
            if done % 10 == 0 or done == len(needs_llm):
                emit("llm_originality",
                     f"LLM fallback: {done}/{len(needs_llm)}", done, len(needs_llm))

    # 3) self-learning — 새 트리거를 사전에 되먹인다 (기존 구현 재사용).
    if learned:
        try:
            added = oe._update_triggers(triggers, learned)
            if added:
                emit("llm_originality", f"Self-learning: {added}개 트리거 추가")
        except Exception as e:  # noqa: BLE001
            logger.warning("트리거 self-learning 실패: %s", e)

    return papers


# ── 1단계: 인용논문 수집 ──────────────────────────────────────────────────

def run_citing_analysis(doi: str, *,
                        sources=None,
                        max_results_per_source: int = 5000,
                        use_llm_originality: bool = True,
                        on_event=None) -> dict:
    """DOI → 인용논문 수집 + 독창성 추출.

    Returns:
        {"doi", "papers", "source_counts", "paper_info", "csv"}
        `papers` 는 피인용 내림차순 dict 리스트.

    Raises:
        ValueError: DOI 가 비었을 때.
    """
    from .citing import normalize_doi, fetch_all_citing_papers
    from .report import papers_to_csv

    emit = _emit(on_event)
    doi = normalize_doi(doi)
    if not doi:
        raise ValueError("DOI가 비어 있습니다.")

    src = list(sources or DEFAULT_SOURCES)
    emit("fetch", f"인용논문 검색 중... (소스: {', '.join(src)})")

    df, source_counts = fetch_all_citing_papers(
        doi, sources=src, max_results_per_source=max_results_per_source,
        progress_callback=lambda phase, msg: emit(phase, msg))

    # 피인용 내림차순 — 리포트/CSV 의 기본 정렬.
    if not df.empty and "citationCount" in df.columns:
        df = df.sort_values("citationCount", ascending=False).reset_index(drop=True)

    papers = df.to_dict("records") if not df.empty else []
    emit("fetch",
         f"검색 완료: 중복 제거 후 {len(papers)}편", len(papers), len(papers))

    paper_info = fetch_paper_metadata(doi)
    if paper_info:
        emit("paper_info", paper_info.get("title", ""))

    if papers:
        papers = extract_originality_for_papers(
            papers, use_llm=use_llm_originality, on_event=on_event)

    return {
        "doi": doi,
        "papers": papers,
        "source_counts": source_counts,
        "paper_info": paper_info,
        "csv": papers_to_csv(papers) if papers else "",
    }


# ── 2단계: 주제 필터 + 요약 + 리포트 ──────────────────────────────────────

def run_topic_analysis(papers: list[dict], *,
                       topic: str,
                       paper_info: dict | None = None,
                       source_counts: dict | None = None,
                       lang: str = "ko",
                       cache_dir=None,
                       make_summaries: bool = True,
                       link_zotero: bool = True,
                       deep_index: str = "",
                       suggest_collections: bool = True,
                       collection: str = "",
                       want_timeline: bool = False,
                       on_event=None) -> dict:
    """주제로 필터링 → 5W1H 요약 → HTML 리포트.

    `topic` 이 비면 필터를 건너뛰고 전체를 대상으로 리포트만 만든다 (요약 없음).
    인용논문 재수집 없이 주제만 바꿔 다시 부를 수 있다 — 원본 웹앱의
    '재필터링' 동작에 대응한다.

    Returns:
        {"topic", "papers", "report_html", "csv", "matched", "total"}
    """
    from .report import build_report_html, papers_to_csv
    from .topic_filter import filter_by_topic, generate_summaries
    from .zotero_links import load_zotero_index

    emit = _emit(on_event)
    papers = list(papers or [])
    total = len(papers)
    topic = (topic or "").strip()

    themes = None
    timeline_uri = ""
    if topic:
        emit("topic_filter", f"주제 필터링 시작: {topic}", 0, total)
        selected = filter_by_topic(
            papers, topic, cache_dir=cache_dir,
            progress_callback=lambda phase, msg, cur=0, tot=0:
                emit(phase, msg, cur, tot))
        emit("topic_filter", f"주제 일치: {len(selected)}/{total}편",
             len(selected), total)

        if selected and make_summaries:
            selected = generate_summaries(
                selected, topic, lang=lang, cache_dir=cache_dir,
                progress_callback=lambda phase, msg, cur=0, tot=0:
                    emit(phase, msg, cur, tot))
    else:
        # 주제 미지정 → 자동 주제 분석. 실패해도 목록 리포트는 그대로 나간다.
        selected = papers
        from .themes import analyze_themes
        themes = analyze_themes(
            papers, cache_dir=cache_dir,
            progress=lambda phase, msg: emit(phase, msg))
        if themes:
            emit("themes", f"주제 {len(themes['clusters'])}개 갈래 도출")
            if want_timeline:
                from .timeline import generate as _gen_timeline
                timeline_uri = _gen_timeline(
                    themes, paper_info=paper_info,
                    progress=lambda phase, msg: emit(phase, msg))

    # 컬렉션 추천 — citedby 등록분은 Unfiled 로 가므로 배정 후보를 함께 낸다.
    if suggest_collections and selected:
        from .collections import recommend_collections
        selected = recommend_collections(
            selected, cache_dir=cache_dir,
            progress=lambda phase, msg: emit(phase, msg))

    emit("report", "리포트 생성 중...")
    # 내 Zotero 라이브러리에 있는 논문은 제목 옆에 PDF 바로열기 링크가 붙는다.
    # `docs/_zotero_keys.json` 은 로컬 전용이라, 없으면 조용히 외부 링크만 남는다.
    zindex = load_zotero_index() if link_zotero else None
    if zindex:
        emit("report", f"Zotero 링크 매칭 (인덱스 {len(zindex)}건)")

    report_html = build_report_html(
        papers=selected, paper_info=paper_info, topic=topic, lang=lang,
        source_counts=source_counts, zotero_index=zindex, themes=themes,
        deep_index=deep_index, timeline_uri=timeline_uri,
        collection=collection)

    return {
        "topic": topic,
        "papers": selected,
        "report_html": report_html,
        "csv": papers_to_csv(selected) if selected else "",
        "themes": themes,
        "matched": len(selected),
        "total": total,
    }


# ── 전체 파이프라인 ───────────────────────────────────────────────────────

def run_citedby(doi: str, *,
                sources=None,
                topic: str = "",
                lang: str = "ko",
                max_results_per_source: int = 5000,
                use_llm_originality: bool = True,
                pdf_first: bool = False,
                timeline: bool = False,
                build_index: bool = False,
                index_dir=None,
                cache_dir=None,
                on_event=None) -> dict:
    """수집 → (PDF 선별) → 필터 → 요약 → 리포트를 한 번에.

    `pdf_first` — 논문마다 **근거 등급**을 매긴다(PDF 전문 > 초록 > 제목).
    제외하지 않는다 — 초록만이라도 있으면 축소된 근거로 쓰는 게 버리는 것보다
    낫다. 초록은
    폐쇄형 논문에서 무료 API 로 못 받지만 내 PDF 에는 전문이 있다. 대상이
    줄어드는 대신 편당 기반이 수백 자에서 수만 자로 넓어져, 주제 군집화와
    5W1H 요약이 원문을 보고 판단하게 된다.

    `build_index` — PDF 전문을 청킹·임베딩해 Deep Research 인덱스를 만든다
    (`_citedby_index.json` + 사이드카). 기존 코퍼스 인덱스와 같은 스키마다.
    """
    emit = _emit(on_event)
    # **monotonic** 을 쓴다 — 벽시계는 실행 중 NTP 보정·절전 복귀로 뒤로 뛸 수
    # 있고, 실제로 -56,645초(음수)가 리포트에 찍힌 적이 있다. 경과시간은
    # 시계 조정과 무관해야 한다.
    started = time.monotonic()

    citing = run_citing_analysis(
        doi, sources=sources, max_results_per_source=max_results_per_source,
        use_llm_originality=use_llm_originality, on_event=on_event)

    papers = citing["papers"]
    pdf_stats = None
    if pdf_first:
        from .pdf_corpus import tier_papers
        papers, pdf_stats = tier_papers(papers)
        emit("library",
             f"근거 등급 — 리뷰완료 {pdf_stats.get('corpus', 0)}편 · "
             f"PDF 전문 {pdf_stats['pdf']}편 · 초록 {pdf_stats['abstract']}편 · "
             f"제목뿐 {pdf_stats['title']}편",
             pdf_stats.get("corpus", 0) + pdf_stats["pdf"], len(papers))

    # 인덱스를 **리포트보다 먼저** 만든다 — 리포트가 인덱스 파일명을 알아야
    # Deep Research 패널을 붙일 수 있다.
    index_info = None
    deep_index = ""
    if build_index and papers:
        from .pdf_corpus import build_index as _build_index, INDEX_NAME
        target = index_dir or Path.cwd()
        index_info = _build_index(papers, target,
                                  progress=lambda p, m: emit(p, m))
        if index_info:
            deep_index = INDEX_NAME
            emit("index",
                 f"Deep Research 인덱스: 논문 {index_info['papers']}편 · "
                 f"청크 {index_info['chunks']}개")

    topical = run_topic_analysis(
        papers, topic=topic, paper_info=citing["paper_info"],
        source_counts=citing["source_counts"], lang=lang,
        cache_dir=cache_dir, deep_index=deep_index,
        want_timeline=timeline, on_event=on_event)

    elapsed = max(0.0, time.monotonic() - started)
    emit("done", f"완료: {topical['matched']}/{topical['total']}편 "
                 f"({elapsed:.0f}초)", topical["matched"], topical["total"])

    return {
        "doi": citing["doi"],
        "paper_info": citing["paper_info"],
        "source_counts": citing["source_counts"],
        "all_papers": citing["papers"],
        "all_csv": citing["csv"],
        "pdf_stats": pdf_stats,
        "index": index_info,
        "topic": topical["topic"],
        "papers": topical["papers"],
        "report_html": topical["report_html"],
        "csv": topical["csv"],
        "matched": topical["matched"],
        "total": topical["total"],
        "elapsed_sec": round(elapsed, 1),
    }
