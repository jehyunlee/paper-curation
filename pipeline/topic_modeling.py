"""
BERTopic 기반 hierarchical topic modeling + UMAP 시각화 좌표 생성.

1. text.md에서 originality 추출 (룰 기반, 영어 아니면 번역)
2. SPECTER2 임베딩
3. BERTopic fine-grained clustering → 40~60 sub-topics
4. Sonnet names sub-topics, then groups into 8~12 categories (bottom-up)
5. UMAP 2D 좌표 저장
6. 임베딩 코사인 유사도 top-20 → Sonnet이 이유/관계 작성

Usage:
  PYTHONUTF8=1 python pipeline/topic_modeling.py --topic ai4s
  PYTHONUTF8=1 python pipeline/topic_modeling.py --topic scisci
  PYTHONUTF8=1 python pipeline/topic_modeling.py --topic ai4s --skip-connections
"""

import argparse
import json
import os
import re
import time
import numpy as np
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from config_loader import PAPERS_DIR as _PAPERS_DIR, get_topic_dir

PAPERS_DIR = str(_PAPERS_DIR)

# SPECTER2 모델 경로 결정.
# 한국에서 huggingface.co LFS 가 일관되게 막힐 때를 대비해, 프로젝트 .cache/base/ 가
# 존재하면 거기서 로드 (AWS S3 ai2-s2-research-public 에서 받은 tar 압축 해제 결과).
# 없으면 HF Hub 이름 fallback — HF cache 가 채워져 있어야 동작.
_SPECTER2_LOCAL = Path(__file__).resolve().parent.parent / ".cache" / "base"
SPECTER2_MODEL = str(_SPECTER2_LOCAL) if (_SPECTER2_LOCAL / "config.json").exists() \
                 else "allenai/specter2_base"

# 서브토픽/카테고리 작명 + 연결 생성에 쓰는 Anthropic 모델.
LLM_MODEL = os.environ.get("TOPIC_MODELING_LLM_MODEL", "claude-sonnet-5")


def log(msg):
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def _anthropic_text(resp):
    """Anthropic content blocks에서 text block만 결합한다.

    claude-sonnet-5 계열이 reasoning/thinking block을 text보다 먼저 줄 수 있는데
    resp.content[0].text 를 가정하면 ThinkingBlock 에서 AttributeError가 난다.
    """
    parts = []
    for block in getattr(resp, "content", []) or []:
        if getattr(block, "type", None) == "text" and getattr(block, "text", None):
            parts.append(block.text)
    text = "".join(parts).strip()
    if not text:
        types = [getattr(b, "type", type(b).__name__) for b in getattr(resp, "content", []) or []]
        raise RuntimeError(f"Anthropic response contained no text blocks: {types}")
    return text


# ═══════════════════════════════════════════
# Step 1: Originality extraction from text.md
# ═══════════════════════════════════════════

def extract_originalities(topic_papers):
    """각 논문의 text.md 에서 originality 추출 (originality.md 캐시).

    캐시는 **자기 text.md 의 sha256 을 사이드카에 들고 있어야** 신뢰된다.
    예전엔 파일이 존재하고 비어 있지만 않으면 원문을 다시 보지 않았고, 그래서
    한번 잘못 들어간 파일이 영구히 남았다 — 실측 29편(0.7%)이 자기 text.md 에서
    재현 불가능한 내용을 들고 있었다(예: 슬러그 256 RFdiffusion 이 슬러그 065
    VibeGen 의 문장을 들고 있고, 256 의 text.md 에 VibeGen 은 0회 등장).

    사이드카가 없는 기존 파일은 **재추출하지 않는다**. `derives_from` 으로
    자기 원문에서 나올 수 있는지 검증해 통과하면 사이드카만 채운다(backfill).
    전량 재추출은 임베딩을 통째로 흔들어 카테고리를 33% 뒤집으므로, 증거 없이
    할 일이 아니다. 검증에 실패한 것만 다시 뽑는다.
    """
    from lib.originality_extractor import (
        _extract_rule_based, _strip_metadata_leaks, load_triggers,
        derives_from, read_provenance, text_digest, write_provenance,
    )

    triggers = load_triggers()
    results = {}
    cached = 0
    extracted = 0
    no_text = 0
    backfilled = 0
    orphaned = []

    for p in topic_papers:
        slug = p["slug"]
        slug_dir = os.path.join(PAPERS_DIR, slug)
        orig_path = os.path.join(slug_dir, "originality.md")
        text_path = os.path.join(slug_dir, "text.md")

        full = None
        digest = None
        if os.path.exists(text_path):
            with open(text_path, "r", encoding="utf-8") as f:
                full = f.read()
            digest = text_digest(full)

        # 1차: originality.md 캐시 — 단, 출처가 확인될 때만.
        if os.path.exists(orig_path):
            with open(orig_path, "r", encoding="utf-8") as f:
                orig = f.read().strip()
            if orig:
                # 캐시 경로도 leak strip 통과 — 기존 965편 originality.md 는
                # 이 strip 도입 전에 기록돼 DOI/arXiv/URL/HTML leak 이 남아 있고,
                # 그대로 c-TF-IDF 에 들어가면 메타데이터가 클러스터 구별 단어로
                # 부각된다. _strip_metadata_leaks 는 idempotent 하므로 이미 깨끗한
                # 텍스트에는 no-op. 실제로 바뀐 경우에만 파일을 self-heal.
                cleaned = _strip_metadata_leaks(orig)
                if cleaned != orig:
                    with open(orig_path, "w", encoding="utf-8") as f:
                        f.write(cleaned)

                meta = read_provenance(slug_dir)
                recorded = meta.get("text_md_sha256")
                if digest is None:
                    trusted = True          # 대조할 원문이 없다 — 있는 걸 쓴다
                elif recorded == digest:
                    trusted = True          # 사이드카가 이 원문을 가리킨다
                elif recorded:
                    trusted = False         # 원문이 바뀌었다 → 다시 뽑는다
                elif derives_from(cleaned, full):
                    trusted = True          # 사이드카는 없지만 원문에서 나온다
                    write_provenance(slug_dir, digest, "backfill")
                    backfilled += 1
                else:
                    trusted = False         # 이 원문에서 나올 수 없다 = 남의 것
                    orphaned.append(slug)

                if trusted:
                    results[slug] = cleaned
                    cached += 1
                    continue

        # 2차: text.md에서 추출 + originality.md 저장
        if full is None:
            no_text += 1
            results[slug] = f"{p.get('title', '')}. {p.get('essence', '')}"
            with open(orig_path, "w", encoding="utf-8") as f:
                f.write(results[slug])
            continue

        abs_pos = full.lower().find("abstract")
        text = full[abs_pos:abs_pos + 1000] if abs_pos >= 0 else full[:1000]
        orig = _extract_rule_based(text, triggers)
        source = "rule.abstract"
        if not orig:
            orig = _extract_rule_based(full, triggers)
            source = "rule.fulltext"
        if not orig:
            orig = f"{p.get('title', '')}. {p.get('essence', '')}"
            source = "title+essence"

        results[slug] = orig
        with open(orig_path, "w", encoding="utf-8") as f:
            f.write(orig)
        write_provenance(slug_dir, digest, source)
        extracted += 1

    log(f"  Originality: {len(results)} papers (cached: {cached}, extracted: {extracted}, no text.md: {no_text})")
    if backfilled:
        log(f"    provenance backfilled: {backfilled} (내용 변경 없음)")
    if orphaned:
        log(f"    ORPHAN 재추출: {len(orphaned)}편 — 자기 text.md 에서 재현 불가한 "
            f"캐시였음 (예: {', '.join(s[:34] for s in orphaned[:3])})")
    return results


# ═══════════════════════════════════════════
# Step 2: SPECTER2 Embedding
# ═══════════════════════════════════════════

def compute_embeddings(originalities, cache_path=None):
    """SPECTER2로 임베딩 계산. 캐시 지원 (incremental: 신규·변경 논문만 재계산).

    임베딩은 공유 로더 `lib.specter2_embed` 를 통한다 — base + proximity adapter
    + [CLS] pooling (AI2 권장). adapters 미설치 시 base/mean-pooling fallback.

    캐시 버전 가드: 캐시 JSON 의 "embed_model" 태그가 현재 임베딩 모드
    (specter2_embed.EMBED_TAG) 와 다르거나 없으면, 구 모델 벡터가 신 모델 벡터와
    섞이는 silent corruption 을 막기 위해 캐시를 통째로 무효화하고 전량 재계산한다
    (구 _embeddings_cache.json 은 mean-pooling 벡터라 태그가 없으므로 자동 무효화).

    입력 가드: 캐시는 **슬러그 집합만** 보고 hit 을 판정했다. 그래서 originality
    가 바뀌어도 같은 논문이면 옛 벡터를 그대로 돌려줬다 — 모델은 검사하면서
    입력은 검사하지 않는 반쪽 가드였다. 이제 슬러그별 originality sha256 을 함께
    저장하고, 기록이 없거나 어긋나는 슬러그만 다시 임베딩한다.
    """
    from lib import specter2_embed
    from lib.originality_extractor import text_digest

    digests = {s: text_digest(t) for s, t in originalities.items()}

    current_slugs = sorted(originalities.keys())
    current_tag = specter2_embed.EMBED_TAG

    if cache_path and os.path.exists(cache_path):
        log(f"  Loading cached embeddings: {cache_path}")
        with open(cache_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        cached_tag = data.get("embed_model")
        if cached_tag != current_tag:
            # 태그 불일치 → 캐시 무효. 아래 full recompute 로 fall through.
            log(f"  Cache INVALID: embed_model tag mismatch "
                f"(cached={cached_tag!r}, current={current_tag!r}) — "
                f"전량 재계산 (구·신 모델 벡터 혼합 방지)")
        else:
            cached_slugs = data["slugs"]
            cached_embeddings = np.array(data["embeddings"])
            cached_digests = data.get("originality_sha256") or {}

            cached_set = set(cached_slugs)
            current_set = set(current_slugs)
            # 기록이 없는 슬러그는 '검증 불가' 라 신뢰하지 않는다 — embed_model
            # 태그 가드와 같은 태도. 최초 1회는 전량 재계산이 되므로, 마이그레이션
            # 스크립트가 현재 텍스트로 해시를 채워 두고 실제로 바뀐 것만 남긴다.
            changed = {s for s in cached_set & current_set
                       if cached_digests.get(s) != digests[s]}

            if cached_set == current_set and not changed:
                log(f"  Cache hit: {len(cached_slugs)} papers (exact match, "
                    f"embed_model={current_tag})")
                return cached_embeddings, cached_slugs

            # Incremental update: reuse cached embeddings, compute only new ones
            new_slugs = sorted((current_set - cached_set) | changed)
            removed_slugs = cached_set - current_set
            log(f"  Cache stale: cached={len(cached_slugs)}, current={len(current_slugs)}, "
                f"new={len(current_set - cached_set)}, "
                f"originality changed={len(changed)}, removed={len(removed_slugs)}")

            # Build slug→embedding map from cache
            slug_to_emb = dict(zip(cached_slugs, cached_embeddings))

            # Remove deleted papers
            for s in removed_slugs:
                slug_to_emb.pop(s, None)

            if new_slugs:
                new_texts = [originalities[s] for s in new_slugs]
                log(f"  Embedding {len(new_texts)} new/changed papers via shared SPECTER2 loader...")
                new_embeddings = specter2_embed.embed_texts(new_texts)
                for s, emb in zip(new_slugs, new_embeddings):
                    slug_to_emb[s] = emb

            # Rebuild in sorted order
            slugs = sorted(slug_to_emb.keys())
            embeddings = np.array([slug_to_emb[s] for s in slugs])

            # Update cache
            if cache_path:
                os.makedirs(os.path.dirname(cache_path), exist_ok=True)
                cache_data = {"embed_model": current_tag,
                              "slugs": slugs, "embeddings": embeddings.tolist(),
                              "originality_sha256": {s: digests[s] for s in slugs
                                                     if s in digests}}
                with open(cache_path, "w", encoding="utf-8") as f:
                    json.dump(cache_data, f)
                log(f"  Cache updated: {len(slugs)} papers ({cache_path})")

            return embeddings, slugs

    # Full compute — 캐시 없음, 또는 태그 불일치로 캐시 무효화됨.
    slugs = current_slugs
    texts = [originalities[s] for s in slugs]

    log(f"  Embedding {len(texts)} papers via shared SPECTER2 loader ({current_tag})...")
    embeddings = specter2_embed.embed_texts(texts)

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        cache_data = {
            "embed_model": current_tag,
            "slugs": slugs,
            "embeddings": embeddings.tolist(),
            "originality_sha256": {s: digests[s] for s in slugs if s in digests},
        }
        with open(cache_path, "w", encoding="utf-8") as f:
            json.dump(cache_data, f)
        log(f"  Cached: {cache_path}")

    return embeddings, slugs


# ═══════════════════════════════════════════
# Step 3: BERTopic Hierarchical Clustering
# ═══════════════════════════════════════════

def run_clustering(embeddings, slugs, originalities, min_cluster_size=2,
                    target_min=40, target_max=100):
    """hdbscan + UMAP으로 fine-grained clustering (BERTopic 대체).

    1. UMAP 차원축소 (768D → 5D) for clustering
    2. HDBSCAN 클러스터링 (min_cluster_size 자동 조정으로 sub-topic 40~100개)
       — `hdbscan` 라이브러리 사용, `prediction_data=True` 설정해 신규 논문이
       `approximate_predict()` 로 같은 클러스터에 매핑될 수 있도록 한다
       (`classify_papers.py` 가 모델을 로드해 사용).
    3. c-TF-IDF 키워드 추출 (Grootendorst 2022, BERTopic 표준 — 클러스터를
       1문서로 취급한 tf × 클래스 기준 idf=log(1+A/f_x))
    """
    from umap import UMAP
    import hdbscan
    from sklearn.feature_extraction import text as _sk_text
    from sklearn.feature_extraction.text import CountVectorizer

    docs = [originalities[s] for s in slugs]
    n_docs = len(docs)

    # 작은 코퍼스를 40개 sub-topic 으로 억지로 쪼개면 클러스터당 1~2편짜리
    # 파편 클러스터만 양산된다 → 코퍼스 크기에 맞춰 sub-topic 목표 하향.
    # (대형 코퍼스는 기존 40~100 유지)
    if n_docs < target_min * 5:
        target_min = max(3, n_docs // 10)
        target_max = max(target_min + 2, n_docs // 3)

    log(f"  Running UMAP + HDBSCAN (n_docs={n_docs}, "
        f"target sub-topics={target_min}~{target_max})...")

    # 1. UMAP 5D for clustering
    umap_cluster = UMAP(
        n_neighbors=5, n_components=5, min_dist=0.0,
        metric="cosine", random_state=42,
    )
    embeddings_5d = umap_cluster.fit_transform(embeddings)

    # 2. HDBSCAN — adaptive min_cluster_size (target_min~target_max)
    # prediction_data=True 가 필수: classify_papers 가 approximate_predict 호출
    #
    # 검색 전략: n_topics 가 target_min 미만이면 mcs 를 낮춰 *재적합* 한다
    # (이전 버전은 decrement 후 곧바로 break 해서 줄인 mcs 를 한 번도 평가하지
    # 못하고 첫 under-target 클러스터링을 그대로 받아들였음 — 작은 코퍼스에서
    # sub-topic 이 2~3개로 수렴해 버리는 원인). mcs 가 2까지 내려가면 더는
    # 못 낮추므로 거기서 멈춘다. 어느 시도도 target 안에 들지 못하면, 지금까지
    # 본 것 중 target_min 에 *가장 가까운* 결과를 채택한다 (마지막 적합을
    # 버리지 않음). range(20) hard stop 으로 무한루프 차단.
    mcs = min_cluster_size
    best = None  # (distance_to_target, model, topics, probs, n_topics, outliers, mcs)
    for attempt in range(20):
        hdbscan_model = hdbscan.HDBSCAN(
            min_cluster_size=mcs,
            min_samples=1, metric="euclidean",
            prediction_data=True,
        )
        topics = hdbscan_model.fit_predict(embeddings_5d).tolist()
        probs = hdbscan_model.probabilities_ if hasattr(hdbscan_model, 'probabilities_') else None

        n_topics = len(set(t for t in topics if t != -1))
        outliers = sum(1 for t in topics if t == -1)
        log(f"  [attempt {attempt+1}] min_cluster_size={mcs} → {n_topics} topics ({outliers} outliers)")

        # target 범위 안의 클러스터링 (또는 적어도 1개 이상) 중 target_min 에
        # 가장 가까운 것을 best 로 보존 — 빈 클러스터링(0개)은 best 후보에서 제외.
        if n_topics > 0:
            dist = 0 if target_min <= n_topics <= target_max else \
                min(abs(n_topics - target_min), abs(n_topics - target_max))
            if best is None or dist < best[0]:
                best = (dist, hdbscan_model, topics, probs, n_topics, outliers, mcs)

        if target_min <= n_topics <= target_max:
            break
        elif n_topics > target_max:
            mcs += 1
        elif n_topics < target_min and mcs > 2:
            mcs -= 1
            continue  # 줄인 mcs 로 재적합 (decrement 를 실제로 평가)
        else:
            # mcs 가 이미 2이거나 더 낮출 수 없는 degenerate 상태 → 종료
            break

    # target 범위에 든 적합이 없으면 가장 가까웠던 best 를 복원.
    if best is not None and not (target_min <= n_topics <= target_max):
        _, hdbscan_model, topics, probs, n_topics, outliers, mcs = best

    # Degenerate: HDBSCAN 이 클러스터를 0개 만들고 전부 outlier(-1) 로 본 경우
    # (아주 작거나 sparse 한 코퍼스). 아래 c-TF-IDF 의 np.vstack([]) 는 물론
    # group_into_categories 의 centroid_matrix 도 빈 행렬이 되어 전 파이프라인이
    # 죽는다. 모든 논문을 1개의 합성 클러스터(tid=0)로 묶어 centroid·키워드가
    # 정상적으로 생성되게 한다 — 카테고리는 1개뿐이지만 abort 보다 낫다.
    if n_topics == 0:
        log("  WARN: HDBSCAN produced 0 sub-clusters (all outliers); "
            "falling back to a single cluster of all papers")
        topics = [0] * n_docs
        probs = np.ones(n_docs, dtype=float) if probs is not None else probs
        n_topics = 1
        outliers = 0

    log(f"  Final: {n_topics} sub-topics (min_cluster_size={mcs}, {outliers} outliers)")

    # 4. c-TF-IDF 키워드 추출 (Grootendorst 2022, BERTopic 표준)
    #
    # 각 클러스터를 1개의 큰 문서로 취급하고 IDF 를 *클러스터 K개 기준* 으로 계산.
    # 일반 TF-IDF (문서 단위 → 클러스터 평균) 보다 클러스터 *구별성* 면에서 우월:
    #   - tf_x,c = 단어 x 의 클러스터 c 내 빈도 / 클러스터 c 총 단어수
    #   - f_x = 단어 x 의 전체 코퍼스 빈도 (모든 클러스터 합)
    #   - A = 클러스터당 평균 단어수
    #   - idf_x = log(1 + A/f_x)
    #   - c-tfidf_x,c = tf_x,c × idf_x
    #
    # token_pattern + stop_words 보강: 알파벳 시작 2자+ 만 — 숫자 단독 토큰,
    # DOI/arXiv ID 같은 메타데이터 leak (예: "10", "1038", "48550") 차단.
    # 학술 보일러플레이트 (et, al, arxiv, doi, ...) + HTML 태그 leak (br, github)
    # 도 stop 에 포함.
    _TOKEN_PATTERN = r"(?u)\b[a-zA-Z][a-zA-Z\-]{1,}\b"
    _DOMAIN_STOPS = frozenset({
        "arxiv", "doi", "https", "http", "org", "pdf", "url", "preprint",
        "corr", "vol", "abs", "issn", "isbn", "html", "www",
        "et", "al", "pp", "eds", "ed", "fig", "figs", "tab", "tabs",
        "paper", "papers", "section", "chapter", "introduction",
        "say", "says", "said",
        "br", "github",
    })
    _stop_words = list(_sk_text.ENGLISH_STOP_WORDS | _DOMAIN_STOPS)

    vectorizer = CountVectorizer(
        max_features=10000,
        stop_words=_stop_words,
        token_pattern=_TOKEN_PATTERN,
    )
    X = vectorizer.fit_transform(docs)  # n_docs × V
    feature_names = vectorizer.get_feature_names_out()

    tids = sorted({t for t in topics if t != -1})
    topic_keywords = {}
    # 방어적 가드: tids 가 비면 np.vstack([]) 가 ValueError 로 죽는다.
    # 위 degenerate fallback 이 보통 막아주지만, 어떤 경로로든 non-outlier
    # 클러스터가 0개면 c-TF-IDF 를 건너뛰고 빈 topic_keywords 로 진행한다.
    if not tids:
        log("  WARN: no non-outlier clusters; skipping c-TF-IDF keyword extraction")
    else:
        cluster_rows = []
        for tid in tids:
            idx = [i for i, t in enumerate(topics) if t == tid]
            cluster_rows.append(np.asarray(X[idx].sum(axis=0)).ravel())
        X_c = np.vstack(cluster_rows).astype(np.float64)  # K × V

        row_sums = X_c.sum(axis=1, keepdims=True)
        row_sums[row_sums == 0] = 1.0
        tf = X_c / row_sums                                  # K × V

        f_x = X_c.sum(axis=0)                                # V
        f_x[f_x == 0] = 1.0
        A = X_c.sum(axis=1).mean()
        idf = np.log(1.0 + A / f_x)                          # V

        c_tfidf = tf * idf                                   # K × V

        for row, tid in enumerate(tids):
            score = c_tfidf[row]
            top_idx = score.argsort()[-10:][::-1]
            topic_keywords[tid] = [(feature_names[i], float(score[i])) for i in top_idx]

    # Sub-topic centroids (768D 원본 임베딩 공간)
    centroids = {}
    for tid in set(topics):
        if tid == -1:
            continue
        indices = [i for i, t in enumerate(topics) if t == tid]
        centroids[tid] = embeddings[indices].mean(axis=0)

    # UMAP 2D for visualization
    log("  Computing UMAP 2D coordinates...")
    umap_2d = UMAP(
        n_neighbors=15, n_components=2, min_dist=0.1,
        metric="cosine", random_state=42,
    )
    coords_2d = umap_2d.fit_transform(embeddings)

    # UMAP 3D for visualization
    log("  Computing UMAP 3D coordinates...")
    umap_3d = UMAP(
        n_neighbors=15, n_components=3, min_dist=0.1,
        metric="cosine", random_state=42,
    )
    coords_3d = umap_3d.fit_transform(embeddings)

    # Return clustering model + UMAP transformers too — classify_papers persists
    # them via joblib so new papers can be projected to the same 5D space and
    # routed via hdbscan.approximate_predict. umap_2d/umap_3d 도 함께 돌려보내
    # 번들에 저장 → 신규 논문 시각화 좌표(_umap_coords.json)를 같은 fit 으로 투영.
    return (topics, probs, topic_keywords, centroids, coords_2d, coords_3d,
            hdbscan_model, umap_cluster, umap_2d, umap_3d)


# ═══════════════════════════════════════════
# Step 4: Category Naming (Sonnet)
# ═══════════════════════════════════════════

def name_sub_topics(topic_keywords, topics, client, batch_size=40):
    """TF-IDF keywords -> Sonnet names fine-grained sub-topics (배치 처리)."""
    topic_counts = defaultdict(int)
    for t in topics:
        topic_counts[t] += 1

    all_tids = sorted(topic_keywords.keys())
    batches = [all_tids[i:i + batch_size] for i in range(0, len(all_tids), batch_size)]
    log(f"  Naming {len(all_tids)} sub-topics via Sonnet ({len(batches)} batches)...")

    result = {}
    for bi, batch_tids in enumerate(batches):
        prompt_parts = []
        for tid in batch_tids:
            kw_scores = topic_keywords[tid]
            count = topic_counts.get(tid, 0)
            keywords = [w for w, _ in kw_scores[:10]]
            prompt_parts.append(f"Topic {tid} ({count} papers): {', '.join(keywords)}")

        prompt = f"""Below are fine-grained topic clusters from academic papers, each with top keywords and paper count.

{chr(10).join(prompt_parts)}

For each topic, create:
1. A sub-topic name: 2-5 word English academic term (specific, e.g., "Protein Structure Prediction", "Graph Neural Network Scalability")
2. A one-sentence description

Output ONLY valid JSON:
{{
  "{batch_tids[0]}": {{"name": "Sub-topic Name", "description": "One sentence description"}}
}}

Rules:
- Names should be specific and granular (NOT broad like "Machine Learning" or "Deep Learning")
- Each name must be unique and distinguishable
- Use & for compound concepts only when necessary
"""

        resp = client.messages.create(
            model=LLM_MODEL,
            max_tokens=8000,
            messages=[{"role": "user", "content": prompt}],
        )
        text = _anthropic_text(resp)
        if text.startswith("```"):
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]

        try:
            names = json.loads(text)
            for tid_str, info in names.items():
                result[int(tid_str)] = info
            log(f"    batch {bi+1}/{len(batches)}: {len(names)} named")
        except json.JSONDecodeError as e:
            log(f"    batch {bi+1}/{len(batches)} WARNING: JSON parse failed: {e}")
            for tid in batch_tids:
                if tid not in result:
                    kw = topic_keywords[tid]
                    result[tid] = {"name": f"Topic {tid}: {', '.join(w for w, _ in kw[:3])}", "description": ""}
        time.sleep(0.5)

    return result


# ═══════════════════════════════════════════
# Step 4.5: Group Sub-topics into Categories
# ═══════════════════════════════════════════

def group_into_categories(sub_topic_names, topics, centroids,
                          min_cats=8, max_cats=12, client=None):
    """Sub-topic centroid의 cosine distance + average linkage로 카테고리 그룹핑.

    1. centroid 간 cosine distance → scipy average linkage hierarchy
    2. fcluster로 min_cats~max_cats 범위에서 자르기
    3. Sonnet이 각 카테고리에 이름만 부여 (그룹핑은 하지 않음)
    """
    from sklearn.metrics.pairwise import cosine_distances
    from scipy.cluster.hierarchy import linkage, fcluster
    from scipy.spatial.distance import squareform

    tids = sorted(centroids.keys())
    centroid_matrix = np.array([centroids[tid] for tid in tids])

    # Cosine distance → ward linkage hierarchy (균등 크기 클러스터 생성)
    dist_matrix = cosine_distances(centroid_matrix)
    condensed = squareform(dist_matrix, checks=False)
    Z = linkage(condensed, method='ward')

    # target 카테고리 수로 자르기
    target_n = (min_cats + max_cats) // 2
    cat_labels = fcluster(Z, t=target_n, criterion='maxclust')

    # tid → category_id 매핑
    tid_to_catid = {tids[i]: int(cat_labels[i]) for i in range(len(tids))}

    # outlier(-1)는 가장 가까운 centroid의 카테고리에 배정
    outlier_tids = [tid for tid in sub_topic_names if tid not in tid_to_catid]
    if outlier_tids:
        log(f"  Note: {len(outlier_tids)} sub-topics without centroids assigned to nearest")

    # 카테고리별 sub-topic 정리
    cat_groups = defaultdict(list)
    for tid, catid in tid_to_catid.items():
        cat_groups[catid].append(tid)

    # 싱글톤 병합: 1~2개짜리 카테고리는 가장 가까운 카테고리에 흡수
    small_cats = [catid for catid, members in cat_groups.items() if len(members) <= 2]
    for small_catid in small_cats:
        small_members = cat_groups[small_catid]
        small_centroid = centroid_matrix[[tids.index(tid) for tid in small_members]].mean(axis=0)
        # 다른 카테고리 중 가장 가까운 것 찾기
        best_catid, best_dist = None, float('inf')
        for catid, members in cat_groups.items():
            if catid == small_catid or len(members) <= 2:
                continue
            cat_centroid = centroid_matrix[[tids.index(tid) for tid in members]].mean(axis=0)
            d = cosine_distances([small_centroid], [cat_centroid])[0][0]
            if d < best_dist:
                best_dist = d
                best_catid = catid
        if best_catid is not None:
            cat_groups[best_catid].extend(small_members)
            del cat_groups[small_catid]
            for tid in small_members:
                tid_to_catid[tid] = best_catid
            log(f"  Merged singleton cat {small_catid} ({len(small_members)} sub-topics) → cat {best_catid}")

    n_cats = len(cat_groups)
    log(f"  Hierarchy cut: {len(tids)} sub-topics → {n_cats} categories")
    for catid, members in sorted(cat_groups.items()):
        names = [sub_topic_names[tid]['name'] for tid in members if tid in sub_topic_names]
        log(f"    cat {catid} ({len(members)} sub-topics): {', '.join(names[:4])}...")

    # Sonnet이 각 카테고리에 이름 부여 (그룹핑은 이미 완료)
    topic_counts = defaultdict(int)
    for t in topics:
        topic_counts[t] += 1

    prompt_parts = []
    for catid, members in sorted(cat_groups.items()):
        member_descs = []
        for tid in members:
            info = sub_topic_names.get(tid, {})
            count = topic_counts.get(tid, 0)
            member_descs.append(f"    - \"{info.get('name', f'Topic {tid}')}\" ({count} papers)")
        prompt_parts.append(f"  Category {catid} ({len(members)} sub-topics):\n" + "\n".join(member_descs))

    prompt = f"""Below are {n_cats} category groups, each containing related sub-topic clusters.
The groups were formed by hierarchical clustering on embedding similarity.
Name each category.

{chr(10).join(prompt_parts)}

Output ONLY valid JSON:
{{
  "1": {{"name": "Category Name", "description": "One sentence description"}},
  "2": {{"name": "Category Name", "description": "One sentence description"}}
}}

Rules:
- Category names: 3-6 word English academic terms
- Each name must be unique and distinguishable
- Names should reflect the common theme of the sub-topics in that group
"""

    log(f"  Naming {n_cats} categories via Sonnet...")
    resp = client.messages.create(
        model=LLM_MODEL,
        max_tokens=4000,
        messages=[{"role": "user", "content": prompt}],
    )
    text = _anthropic_text(resp)
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]

    cat_names = json.loads(text)

    # Build tid → category_name mapping
    tid_to_cat = {}
    cat_info = {}
    for catid, members in cat_groups.items():
        catid_str = str(catid)
        if catid_str in cat_names:
            cat_name = cat_names[catid_str]["name"]
            cat_info[cat_name] = cat_names[catid_str].get("description", "")
        else:
            cat_name = f"Category {catid}"
            cat_info[cat_name] = ""
        for tid in members:
            tid_to_cat[tid] = cat_name

    # outlier sub-topics → "Other"
    for tid in sub_topic_names:
        if tid not in tid_to_cat:
            tid_to_cat[tid] = "Other"

    return tid_to_cat, cat_info


# ═══════════════════════════════════════════
# Step 5: Multi-class Assignment
# ═══════════════════════════════════════════

def assign_multi_class(topics, probs, sub_topic_names, tid_to_cat,
                       embeddings=None, centroids=None, threshold=0.1):
    """확률 threshold 기반 멀티클래스 배정. Outlier는 가장 가까운 sub-topic에 배정."""
    from sklearn.metrics.pairwise import cosine_similarity

    # Outlier → 가장 가까운 centroid의 sub-topic으로 배정
    nearest_tid_map = {}
    if embeddings is not None and centroids:
        centroid_tids = sorted(centroids.keys())
        centroid_matrix = np.array([centroids[tid] for tid in centroid_tids])
        for i, tid in enumerate(topics):
            if tid == -1:
                sims = cosine_similarity([embeddings[i]], centroid_matrix)[0]
                nearest_idx = sims.argmax()
                nearest_tid_map[i] = centroid_tids[nearest_idx]

    assignments = []
    for i, primary_tid in enumerate(topics):
        if primary_tid == -1:
            assigned_tid = nearest_tid_map.get(i)
            if assigned_tid is not None:
                primary_category = tid_to_cat.get(assigned_tid, "Other")
                sub_category = sub_topic_names.get(assigned_tid, {}).get("name", "Other")
            else:
                primary_category = "Other"
                sub_category = "Other"
        else:
            primary_category = tid_to_cat.get(primary_tid, "Other")
            sub_category = sub_topic_names.get(primary_tid, {}).get("name", "Other")

        all_cats = [primary_category]
        if probs is not None and hasattr(probs, '__len__') and i < len(probs):
            prob_row = probs[i]
            if hasattr(prob_row, '__len__') and len(prob_row) > 0:
                for tid in range(len(prob_row)):
                    if tid != primary_tid and tid != -1 and prob_row[tid] >= threshold:
                        cat_name = tid_to_cat.get(tid, "")
                        if cat_name and cat_name not in all_cats:
                            all_cats.append(cat_name)

        assignments.append({
            "primary_category": primary_category,
            "all_categories": all_cats[:3],
            "sub_category": sub_category,
        })

    return assignments


# ═══════════════════════════════════════════
# Step 6: Related Papers (Embedding + Sonnet)
# ═══════════════════════════════════════════

# Deep Research 검색(`query_search_index`)과 동일한 RRF 상수. 두 랭킹을
# 융합하는 규칙을 이 저장소에서 두 벌 유지하지 않는다.
RELATED_RRF_K = 60


def _lexical_score_matrix(slugs, papers):
    """제목·저자 BM25 점수 행렬 (행 i = 논문 i 를 질의로 쓴 결과).

    SPECTER2 는 **기여 내용**을 임베딩한다. 그래서 같은 제목 시리즈의 후속편이라도
    다루는 분야가 옮겨가면(수학 증명 → 재료·생물 폐루프 실험) 코사인상 멀어진다.
    실측: `10911 Accelerating Scientific Research with Gemini in the Real-World`
    에서 직전편 `044 ... Case Studies and Common Techniques` 가 코사인 465위/2929
    라 top-5·top-25 창 어디에도 들지 못했다 — 그 논문의 참고문헌에 실제로 인용돼
    있는데도. 제목 토큰과 저자 이름은 그 계보를 담고 코사인은 담지 못하므로,
    임베딩 텍스트에 이어붙이지 않고 **따로 채점해 RRF 로 융합**한다(융합 후 12위).
    """
    import math
    from collections import Counter
    from scipy.sparse import csr_matrix
    from query_search_index import tokenize, BM25_K1, BM25_B

    by_slug = {p["slug"]: p for p in (papers or []) if p.get("slug")}
    docs = []
    for slug in slugs:
        paper = by_slug.get(slug) or {}
        # 인덱스에 없는 슬러그는 슬러그 자체가 제목을 담고 있다(`NNN_Title_Words`).
        title = paper.get("title") or slug.split("_", 1)[-1].replace("_", " ")
        authors = " ".join(str(a) for a in (paper.get("authors") or [])[:12])
        docs.append(Counter(tokenize(title) + tokenize(authors)))

    n = len(docs)
    lengths = np.array([sum(d.values()) or 1 for d in docs], dtype=np.float64)
    avg_len = float(lengths.mean()) or 1.0
    doc_freq = Counter()
    for doc in docs:
        doc_freq.update(doc.keys())

    vocab = {}
    w_rows, w_cols, w_vals = [], [], []
    q_rows, q_cols = [], []
    for i, doc in enumerate(docs):
        for term, freq in doc.items():
            col = vocab.setdefault(term, len(vocab))
            df = doc_freq[term]
            idf = math.log(1.0 + (n - df + 0.5) / (df + 0.5))
            denom = freq + BM25_K1 * (1.0 - BM25_B + BM25_B * lengths[i] / avg_len)
            w_rows.append(i)
            w_cols.append(col)
            w_vals.append(idf * freq * (BM25_K1 + 1.0) / denom)
            q_rows.append(i)
            q_cols.append(col)
    shape = (n, len(vocab) or 1)
    weights = csr_matrix((w_vals, (w_rows, w_cols)), shape=shape)
    queries = csr_matrix((np.ones(len(q_rows), dtype=np.float64), (q_rows, q_cols)),
                         shape=shape)
    return np.asarray((queries @ weights.T).todense(), dtype=np.float32)


def _row_ranks(scores):
    """행마다 내림차순 0-based 순위. 대각선이 -inf 라 자기 자신은 항상 꼴찌."""
    order = np.argsort(-scores, axis=1, kind="stable")
    ranks = np.empty(order.shape, dtype=np.int32)
    np.put_along_axis(ranks, order,
                      np.arange(order.shape[1], dtype=np.int32)[None, :], axis=1)
    return ranks


def compute_related_candidates(embeddings, slugs, top_k=5, papers=None):
    """연관 후보 top-k — dense(SPECTER2 코사인) + lexical(제목·저자 BM25) 하이브리드.

    ``papers``(``{slug,title,authors}`` dict 목록)가 주어지면 두 랭킹을 RRF 로
    융합한다. 없으면 코사인 단독 — 융합 순위가 코사인 점수 순과 같아져 기존 동작
    그대로다. 반환 점수는 계속 코사인이다(순서만 융합 순위).
    """
    from sklearn.metrics.pairwise import cosine_similarity

    mode = "dense+lexical RRF" if papers else "dense only"
    log(f"  Related candidates ({len(slugs)} papers, top_k={top_k}, {mode})...")
    sim_matrix = cosine_similarity(embeddings)
    np.fill_diagonal(sim_matrix, -np.inf)
    fused = (1.0 / (RELATED_RRF_K + _row_ranks(sim_matrix))).astype(np.float32)
    if papers:
        lexical = _lexical_score_matrix(slugs, papers)
        np.fill_diagonal(lexical, -np.inf)
        lex_ranks = _row_ranks(lexical)
        del lexical
        fused += (1.0 / (RELATED_RRF_K + lex_ranks)).astype(np.float32)
        del lex_ranks

    n = len(slugs)
    keep = max(0, min(top_k, n - 1))
    candidates = {}
    for i, slug in enumerate(slugs):
        row = fused[i]
        row[i] = -np.inf  # 자기 자신 제외
        if keep:
            picked = np.argpartition(-row, keep - 1)[:keep]
            picked = picked[np.argsort(-row[picked], kind="stable")]
        else:
            picked = np.empty(0, dtype=int)
        candidates[slug] = [(slugs[j], float(sim_matrix[i, j])) for j in picked]

    total = sum(len(v) for v in candidates.values())
    avg = total / len(candidates) if candidates else 0
    log(f"  {total} candidates (avg {avg:.1f}/paper)")
    return candidates


# ═══════════════════════════════════════════
# Main
# ═══════════════════════════════════════════

def _run_topic_model(topic="ai4s", *, skip_connections=False,
                      skip_classification=False, min_cats=8, max_cats=12):
    """Programmatic entrypoint for topic_modeling."""
    topic_dir = str(get_topic_dir(topic))

    log(f"Loading {topic} data...")
    with open(os.path.join(PAPERS_DIR, "_papers_index.json"), "r", encoding="utf-8") as f:
        all_papers = json.load(f)
    topic_papers = [p for p in all_papers if topic in p.get("topics", [])]
    log(f"  {len(topic_papers)} papers")

    # Step 1
    log("\n" + "=" * 50)
    log("STEP 1: ORIGINALITY EXTRACTION")
    log("=" * 50)
    originalities = extract_originalities(topic_papers)

    # Step 2
    log("\n" + "=" * 50)
    log("STEP 2: SPECTER2 EMBEDDING")
    log("=" * 50)
    cache_path = os.path.join(topic_dir, "_embeddings_cache.json")
    embeddings, slugs = compute_embeddings(originalities, cache_path)

    # Step 3: Fine-grained clustering (sklearn HDBSCAN + UMAP)
    log("\n" + "=" * 50)
    log("STEP 3: HDBSCAN FINE-GRAINED CLUSTERING")
    log("=" * 50)
    (topics, probs, topic_keywords, centroids, coords_2d, coords_3d,
     hdbscan_model, umap_cluster, umap_2d, umap_3d) = run_clustering(
        embeddings, slugs, originalities
    )

    if skip_classification:
        log("\n  [Steps 4-5] SKIP (--skip-classification: preserving existing categories)")
    else:
        # Category naming is the only model-backed step left in this module;
        # connections below are computed in embedding space without a model.
        from anthropic import Anthropic
        client = Anthropic(timeout=180.0, max_retries=4)
        # Step 4: Name sub-topics
        log("\n" + "=" * 50)
        log("STEP 4: SUB-TOPIC NAMING (Sonnet)")
        log("=" * 50)
        topic_names = name_sub_topics(topic_keywords, topics, client)
        for tid, info in sorted(topic_names.items()):
            count = sum(1 for t in topics if t == tid)
            log(f"  [{tid}] {info['name']} ({count} papers)")

        # Step 4.5: Group sub-topics into categories
        log("\n" + "=" * 50)
        log("STEP 4.5: GROUPING SUB-TOPICS INTO CATEGORIES (Sonnet)")
        log("=" * 50)
        tid_to_cat, cat_info = group_into_categories(topic_names, topics, centroids, min_cats, max_cats, client)
        for cat_name, desc in sorted(cat_info.items()):
            count = sum(1 for tid, cat in tid_to_cat.items() if cat == cat_name)
            log(f"  [{cat_name}] {count} sub-topics")

        # Step 5: Multi-class assignment (includes sub_category)
        log("\n" + "=" * 50)
        log("STEP 5: MULTI-CLASS ASSIGNMENT")
        log("=" * 50)
        assignments = assign_multi_class(topics, probs, topic_names, tid_to_cat,
                                          embeddings, centroids)
        slug_to_assignment = dict(zip(slugs, assignments))
        for p in all_papers:
            if p["slug"] in slug_to_assignment:
                a = slug_to_assignment[p["slug"]]
                if "classifications" not in p:
                    p["classifications"] = {}
                p["classifications"][topic] = {
                    "primary_category": a["primary_category"],
                    "all_categories": a["all_categories"],
                    "sub_category": a["sub_category"],
                }
        with open(os.path.join(PAPERS_DIR, "_papers_index.json"), "w", encoding="utf-8") as f:
            json.dump(all_papers, f, ensure_ascii=False, indent=2)
        log(f"  Updated classifications in _papers_index.json")

        # Update _new_classification.json
        cats_list = sorted(set(a["primary_category"] for a in assignments))
        cls_data = {
            "categories": [{"name": c} for c in cats_list],
            "assignments": [
                {"slug": slugs[i], "primary_category": a["primary_category"],
                 "all_categories": a["all_categories"], "sub_category": a["sub_category"]}
                for i, a in enumerate(assignments)
            ],
        }
        cls_path = os.path.join(topic_dir, "_new_classification.json")
        with open(cls_path, "w", encoding="utf-8") as f:
            json.dump(cls_data, f, ensure_ascii=False, indent=2)
        log(f"  Updated _new_classification.json ({len(cats_list)} categories)")

    # Save UMAP coordinates
    umap_data = {}
    for i, slug in enumerate(slugs):
        entry = {"x": float(coords_2d[i][0]), "y": float(coords_2d[i][1])}
        if coords_3d is not None:
            entry["x3"] = float(coords_3d[i][0])
            entry["y3"] = float(coords_3d[i][1])
            entry["z3"] = float(coords_3d[i][2])
        umap_data[slug] = entry
    umap_path = os.path.join(topic_dir, "_umap_coords.json")
    with open(umap_path, "w", encoding="utf-8") as f:
        json.dump(umap_data, f, ensure_ascii=False, indent=2)
    log(f"  UMAP coordinates: {umap_path}")

    # Save topic model info + persisted clustering bundle. classify_papers
    # loads the joblib bundle and routes new papers via:
    #   1. umap_cluster.transform(new_768D) → 5D
    #   2. hdbscan.approximate_predict(hdbscan_model, 5D) → primary sub-cluster
    #   3. centroids[sub_id] (768D) → outlier fallback + all_categories top-N
    # 즉 클러스터링은 density-faithful (HDBSCAN), centroid 는 outlier 와
    # 부차 카테고리 선정에만 사용한다 (원 설계 그대로).
    if not skip_classification:
        topic_info_data = {
            "generated_at": datetime.now().strftime("%Y-%m-%d"),
            "model": "SPECTER2 + hdbscan.HDBSCAN(prediction_data=True) + UMAP",
            "n_papers": len(topic_papers),
            "n_topics": len(topic_names),
            "topics": {str(tid): info for tid, info in topic_names.items()},
            "topic_counts": {str(tid): sum(1 for t in topics if t == tid)
                             for tid in topic_names},
        }
        info_path = os.path.join(topic_dir, "_topic_model_info.json")
        with open(info_path, "w", encoding="utf-8") as f:
            json.dump(topic_info_data, f, ensure_ascii=False, indent=2)
        log(f"  Topic model info: {info_path}")

        # Persist HDBSCAN model + UMAP transformer + centroids + maps.
        # classify_papers loads this and uses:
        #   - umap_cluster.transform(new_768D) → 5D
        #   - hdbscan.approximate_predict(hdbscan_model, 5D) → primary tid (int)
        #   - tid_to_subname[tid] → textual sub-category name
        #   - tid_to_cat[tid]     → parent category name
        #   - centroids[tid]      → outlier fallback + all_categories top-N (cosine on 768D)
        import joblib
        from lib import specter2_embed
        bundle = {
            "hdbscan_model": hdbscan_model,
            "umap_cluster": umap_cluster,
            "centroids": {int(k): v for k, v in centroids.items()},
            "tid_to_cat": {int(k): v for k, v in tid_to_cat.items()},
            "tid_to_subname": {int(k): v["name"] for k, v in topic_names.items()},
            # 분류기(classify_papers)가 동일 임베딩 모드인지 검증하는 가드 키.
            # 번들의 manifold 가 어느 임베딩으로 학습됐는지 박아 둔다.
            "embed_model": specter2_embed.EMBED_TAG,
            # 시각화 transformer — classify_papers.compute_viz_coords 가 신규 논문을
            # 같은 2D/3D 공간에 투영해 _umap_coords.json 에 좌표를 채우는 데 사용.
            "umap_2d": umap_2d,
            "umap_3d": umap_3d,
            "trained_at": datetime.now().isoformat(),
            "n_papers": len(topic_papers),
            "n_subclusters": len(centroids),
        }
        bundle_path = os.path.join(topic_dir, "_hdbscan_model.joblib")
        joblib.dump(bundle, bundle_path)
        log(f"  HDBSCAN bundle: {bundle_path} "
            f"({len(centroids)} sub-clusters, {len(tid_to_cat)} mapped)")

    # Step 6
    if not skip_connections:
        log("\n" + "=" * 50)
        log("STEP 6: RELATED PAPERS (SPECTER2 + BM25, embedding space only)")
        log("=" * 50)
        # Connections are a deterministic function of the embedding geometry
        # and the recorded metadata. Recomputing every paper costs nothing but
        # CPU, so there is no incremental LLM cache and no judge to retry.
        from lib.related import build_connections, max_links
        candidates = compute_related_candidates(embeddings, slugs, top_k=max_links(),
                                                papers=topic_papers)
        connections = build_connections(candidates, topic_papers, topic=topic)
        linked = sum(1 for links in connections.values() if links)
        log(f"  {linked}/{len(connections)} papers linked "
            f"({sum(len(v) for v in connections.values())} directed edges)")
        from lib.connections import sync_topic_connections
        sync_topic_connections(connections, topic, slugs, topic_dir, log=log)

    log("\n" + "=" * 50)
    log("DONE!")
    if not skip_classification:
        log(f"  Topics: {len(topic_names)}")
    log(f"  UMAP: {umap_path}")
    log(f"  Cache: {cache_path}")
    log("=" * 50)


def main():
    parser = argparse.ArgumentParser(description="BERTopic topic modeling + UMAP")
    parser.add_argument("--topic", default="ai4s")
    parser.add_argument("--skip-connections", action="store_true")
    parser.add_argument("--skip-classification", action="store_true",
                        help="Skip Steps 4-5 (naming/grouping/assignment). Run embedding, UMAP, connections only.")
    parser.add_argument("--min-cats", type=int, default=8)
    parser.add_argument("--max-cats", type=int, default=12)
    args = parser.parse_args()

    _run_topic_model(topic=args.topic,
                     skip_connections=args.skip_connections,
                     skip_classification=args.skip_classification,
                     min_cats=args.min_cats, max_cats=args.max_cats)


if __name__ == "__main__":
    from _env_guard import force_py312
    force_py312()
    main()
