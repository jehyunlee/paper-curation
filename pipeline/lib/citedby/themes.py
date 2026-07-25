"""인용논문의 주제 자동 분석 — 군집화 + 작명 + 연도 흐름.

주제를 지정하지 않았을 때 도는 경로다. 두 모드가 **다른 질문에 답한다**:

    주제 입력 O   "내 관심 주제로 이 논문을 인용한 건?"  → LLM 필터 + 5W1H
    주제 입력 X   "이 논문이 어떤 갈래로 확산됐나?"      → 군집 + 연도 흐름표

paper-curation 의 `topic_modeling` 을 재사용한다 — `compute_embeddings` /
`run_clustering` 은 리스트를 받는 순수 함수라 코퍼스에 묶여 있지 않고,
`run_clustering` 은 이미 작은 코퍼스에 맞춰 sub-topic 목표를 자동 하향한다
(n_docs < target_min*5 이면 n//10 ~ n//3).

**이미지·Opus narrative 는 만들지 않는다.** 코퍼스 4,048편용 타임라인 생성은
인용논문 수십~수백 편에 과하고, "주제별로 얼마나 어떻게 흘러갔는지" 는
연도×군집 교차표로 더 정확하게 읽힌다 (year·cited_by_count 가 이미 있다).

실측(41편): 군집 12개, 미분류 1편. 초록이 없는 논문은 제목만으로 임베딩돼
군집 품질이 떨어진다 — 언어가 같다는 이유로 묶이는 경우가 관찰됐다.
"""
from __future__ import annotations

import logging
import re
from collections import Counter, defaultdict

logger = logging.getLogger(__name__)

# 이보다 적으면 군집이 통계적으로 의미가 없다. 실측 분포상 수십 편 아래에서는
# 군집당 2~3편짜리 파편만 나와, 눈으로 목록을 읽는 편이 빠르다.
DEFAULT_MIN_PAPERS = 30

# 작명 실패 시 폴백에 쓰는 불용어 (c-TF-IDF 키워드에서 걸러낸다).
_STOP = frozenset({
    "the", "and", "for", "with", "that", "this", "from", "are", "was",
    "using", "based", "toward", "towards", "via", "into", "their", "its",
    "la", "en", "el", "que", "como", "de", "los", "las",
})


def _paper_text(p: dict) -> str:
    """임베딩 입력. 초록이 최선, 없으면 독창성 문장, 최후엔 제목뿐."""
    body = (p.get("abstract") or "").strip() or (p.get("originality") or "").strip()
    title = (p.get("title") or "").strip()
    return f"{title}. {body}".strip() if body else title


def _fallback_name(keywords: list[str]) -> str:
    """LLM 작명이 실패했을 때 키워드로 만드는 이름."""
    words = [w for w in keywords if w.lower() not in _STOP and len(w) > 2]
    return " / ".join(words[:3]) if words else "미분류 주제"


_NAME_PROMPT = """아래는 어떤 논문을 인용한 논문들을 군집화한 결과다.
각 군집의 대표 키워드와 논문 제목 일부를 준다.

{blocks}

각 군집에 **한국어 이름**을 붙여라. 규칙:
- 3~7 단어, 명사구. 학술 주제로 읽히게.
- 기술 용어는 영어 그대로 (LLM, agent, RAG 등).
- 키워드 나열이 아니라 그 군집이 다루는 **연구 주제**를 말할 것.

JSON 만 출력:
{{"names": {{"0": "이름", "1": "이름"}}}}
"""


def _name_clusters(cluster_kw: dict, cluster_titles: dict, *,
                   cache_dir=None, keys=None) -> dict:
    """군집에 한국어 이름을 붙인다. LLM 실패 시 키워드 폴백."""
    from .topic_filter import llm_json

    blocks = []
    for tid in sorted(cluster_kw):
        kws = ", ".join(cluster_kw[tid][:10])
        titles = "\n".join(f"    - {t[:80]}" for t in cluster_titles[tid][:4])
        blocks.append(f"[군집 {tid}] 키워드: {kws}\n{titles}")

    names: dict[int, str] = {}
    result = llm_json(_NAME_PROMPT.format(blocks="\n\n".join(blocks)),
                      max_tokens=120 * max(1, len(cluster_kw)),
                      keys=keys, cache_dir=cache_dir)
    if result and isinstance(result.get("names"), dict):
        for k, v in result["names"].items():
            try:
                names[int(k)] = str(v).strip()
            except (TypeError, ValueError):
                continue

    for tid in cluster_kw:
        if not names.get(tid):
            names[tid] = _fallback_name(cluster_kw[tid])
    return names


def _year_of(p: dict):
    """발행연도 정수. date(완전한 ISO) 우선, 없으면 year."""
    for key in ("date", "year"):
        raw = str(p.get(key) or "").strip()
        m = re.match(r"(\d{4})", raw)
        if m:
            return int(m.group(1))
    return None


def analyze_themes(papers: list[dict], *,
                   min_papers: int = DEFAULT_MIN_PAPERS,
                   cache_dir=None,
                   keys=None,
                   progress=None) -> dict | None:
    """인용논문을 군집화하고 연도별 흐름을 낸다.

    Returns:
        {"clusters": [{id, name, keywords, count, citations, years{}, papers[]}],
         "years": [정렬된 연도], "outliers": int, "total": int}
        또는 None (편수 부족 / 의존성 없음 / 군집화 실패).

    호출부는 None 을 "주제 분석 없음" 으로 조용히 처리해야 한다 — 이건 부가
    기능이라 실패가 리포트 생성을 막아서는 안 된다.
    """
    papers = [p for p in (papers or []) if (p.get("title") or "").strip()]
    total = len(papers)
    if total < min_papers:
        logger.info("주제 분석 생략: %d편 (임계값 %d편 미만)", total, min_papers)
        return None

    if progress:
        progress("themes", f"주제 군집화 시작 ({total}편)")

    try:
        import sys
        from pathlib import Path
        pipeline_dir = Path(__file__).resolve().parents[2]
        if str(pipeline_dir) not in sys.path:
            sys.path.insert(0, str(pipeline_dir))
        from topic_modeling import compute_embeddings, run_clustering
    except Exception as e:  # noqa: BLE001 — umap/hdbscan/SPECTER2 미설치 등
        logger.warning("주제 분석 불가 (의존성): %s", str(e)[:120])
        return None

    keyed = {f"c{i:04d}": p for i, p in enumerate(papers)}
    texts = {k: _paper_text(p) for k, p in keyed.items()}

    try:
        embeddings, slugs = compute_embeddings(texts)
        if progress:
            progress("themes", f"임베딩 완료 ({len(slugs)}편) — 군집화 중")
        topics, _probs, topic_keywords, *_ = run_clustering(
            embeddings, slugs, texts, min_cluster_size=2)
    except Exception as e:  # noqa: BLE001
        logger.warning("주제 군집화 실패: %s", str(e)[:160])
        return None

    members: dict[int, list] = defaultdict(list)
    for slug, tid in zip(slugs, topics):
        members[int(tid)].append(keyed[slug])

    outliers = len(members.pop(-1, []))
    if not members:
        logger.info("주제 분석 생략: 유효 군집 0개 (전량 미분류)")
        return None

    cluster_kw = {tid: [w for w, _ in (topic_keywords.get(tid) or [])[:12]]
                  for tid in members}
    cluster_titles = {tid: [p.get("title", "") for p in ms]
                      for tid, ms in members.items()}

    if progress:
        progress("themes", f"군집 {len(members)}개 — 이름 생성 중")
    names = _name_clusters(cluster_kw, cluster_titles,
                           cache_dir=cache_dir, keys=keys)

    all_years: set[int] = set()
    clusters = []
    for tid, ms in members.items():
        years = Counter()
        citations = 0
        for p in ms:
            y = _year_of(p)
            if y:
                years[y] += 1
                all_years.add(y)
            try:
                citations += int(float(p.get("citation_count")
                                       or p.get("citationCount") or 0))
            except (TypeError, ValueError):
                pass
        clusters.append({
            "id": tid,
            "name": names.get(tid) or _fallback_name(cluster_kw[tid]),
            "keywords": cluster_kw[tid][:6],
            "count": len(ms),
            "citations": citations,
            "years": dict(years),
            "papers": ms,
        })

    # 편수 → 피인용 순. 큰 갈래가 위로 오게.
    clusters.sort(key=lambda c: (-c["count"], -c["citations"]))
    logger.info("주제 분석: %d개 군집 (미분류 %d편 / 총 %d편)",
                len(clusters), outliers, total)
    return {
        "clusters": clusters,
        "years": sorted(all_years),
        "outliers": outliers,
        "total": total,
    }
