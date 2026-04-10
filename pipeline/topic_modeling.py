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
import time
import numpy as np
from collections import defaultdict
from datetime import datetime

from config_loader import PAPERS_DIR as _PAPERS_DIR, get_topic_dir

PAPERS_DIR = str(_PAPERS_DIR)


def log(msg):
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


# ═══════════════════════════════════════════
# Step 1: Originality extraction from text.md
# ═══════════════════════════════════════════

def extract_originalities(topic_papers):
    """각 논문의 text.md 앞 1000자에서 originality 추출."""
    from lib.originality_extractor import _extract_rule_based, load_triggers

    triggers = load_triggers()
    results = {}
    cached = 0
    extracted = 0
    no_text = 0

    for p in topic_papers:
        slug = p["slug"]
        orig_path = os.path.join(PAPERS_DIR, slug, "originality.md")

        # 1차: originality.md 캐시 사용
        if os.path.exists(orig_path):
            with open(orig_path, "r", encoding="utf-8") as f:
                orig = f.read().strip()
            if orig:
                results[slug] = orig
                cached += 1
                continue

        # 2차: text.md에서 추출 + originality.md 저장
        text_path = os.path.join(PAPERS_DIR, slug, "text.md")
        if not os.path.exists(text_path):
            no_text += 1
            results[slug] = f"{p.get('title', '')}. {p.get('essence', '')}"
            with open(orig_path, "w", encoding="utf-8") as f:
                f.write(results[slug])
            continue

        with open(text_path, "r", encoding="utf-8") as f:
            full = f.read()

        abs_pos = full.lower().find("abstract")
        text = full[abs_pos:abs_pos + 1000] if abs_pos >= 0 else full[:1000]
        orig = _extract_rule_based(text, triggers)
        if not orig:
            orig = _extract_rule_based(full, triggers)
        if not orig:
            orig = f"{p.get('title', '')}. {p.get('essence', '')}"

        results[slug] = orig
        with open(orig_path, "w", encoding="utf-8") as f:
            f.write(orig)
        extracted += 1

    log(f"  Originality: {len(results)} papers (cached: {cached}, extracted: {extracted}, no text.md: {no_text})")
    return results


# ═══════════════════════════════════════════
# Step 2: SPECTER2 Embedding
# ═══════════════════════════════════════════

def compute_embeddings(originalities, cache_path=None):
    """SPECTER2로 임베딩 계산. 캐시 지원 (incremental: 신규 논문만 추가 계산)."""
    current_slugs = sorted(originalities.keys())

    if cache_path and os.path.exists(cache_path):
        log(f"  Loading cached embeddings: {cache_path}")
        with open(cache_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        cached_slugs = data["slugs"]
        cached_embeddings = np.array(data["embeddings"])

        cached_set = set(cached_slugs)
        current_set = set(current_slugs)

        if cached_set == current_set:
            log(f"  Cache hit: {len(cached_slugs)} papers (exact match)")
            return cached_embeddings, cached_slugs

        # Incremental update: reuse cached embeddings, compute only new ones
        new_slugs = sorted(current_set - cached_set)
        removed_slugs = cached_set - current_set
        log(f"  Cache stale: cached={len(cached_slugs)}, current={len(current_slugs)}, "
            f"new={len(new_slugs)}, removed={len(removed_slugs)}")

        # Build slug→embedding map from cache
        slug_to_emb = dict(zip(cached_slugs, cached_embeddings))

        # Remove deleted papers
        for s in removed_slugs:
            slug_to_emb.pop(s, None)

        if new_slugs:
            from sentence_transformers import SentenceTransformer
            log("  Loading SPECTER2 model for incremental update...")
            model = SentenceTransformer("allenai/specter2_base", local_files_only=True)
            new_texts = [originalities[s] for s in new_slugs]
            log(f"  Embedding {len(new_texts)} new papers...")
            new_embeddings = model.encode(new_texts, show_progress_bar=True, batch_size=32)
            for s, emb in zip(new_slugs, new_embeddings):
                slug_to_emb[s] = emb

        # Rebuild in sorted order
        slugs = sorted(slug_to_emb.keys())
        embeddings = np.array([slug_to_emb[s] for s in slugs])

        # Update cache
        if cache_path:
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)
            cache_data = {"slugs": slugs, "embeddings": embeddings.tolist()}
            with open(cache_path, "w", encoding="utf-8") as f:
                json.dump(cache_data, f)
            log(f"  Cache updated: {len(slugs)} papers ({cache_path})")

        return embeddings, slugs

    from sentence_transformers import SentenceTransformer

    log("  Loading SPECTER2 model...")
    model = SentenceTransformer("allenai/specter2_base", local_files_only=True)

    slugs = current_slugs
    texts = [originalities[s] for s in slugs]

    log(f"  Embedding {len(texts)} papers...")
    embeddings = model.encode(texts, show_progress_bar=True, batch_size=32)

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        cache_data = {
            "slugs": slugs,
            "embeddings": embeddings.tolist(),
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
    """sklearn HDBSCAN + UMAP으로 fine-grained clustering (BERTopic 대체).

    1. UMAP 차원축소 (768D → 5D) for clustering
    2. HDBSCAN 클러스터링 (min_cluster_size 자동 조정으로 sub-topic 40~100개)
    3. TF-IDF 키워드 추출 (c-TF-IDF 대체)
    """
    from umap import UMAP
    from sklearn.cluster import HDBSCAN
    from sklearn.feature_extraction.text import TfidfVectorizer

    docs = [originalities[s] for s in slugs]
    n_docs = len(docs)

    log(f"  Running UMAP + HDBSCAN (n_docs={n_docs})...")

    # 1. UMAP 5D for clustering
    umap_cluster = UMAP(
        n_neighbors=5, n_components=5, min_dist=0.0,
        metric="cosine", random_state=42,
    )
    embeddings_5d = umap_cluster.fit_transform(embeddings)

    # 2. HDBSCAN — adaptive min_cluster_size (target_min~target_max)
    mcs = min_cluster_size
    for attempt in range(20):
        hdbscan_model = HDBSCAN(
            min_cluster_size=mcs,
            min_samples=1, metric="euclidean",
        )
        topics = hdbscan_model.fit_predict(embeddings_5d).tolist()
        probs = hdbscan_model.probabilities_ if hasattr(hdbscan_model, 'probabilities_') else None

        n_topics = len(set(t for t in topics if t != -1))
        outliers = sum(1 for t in topics if t == -1)
        log(f"  [attempt {attempt+1}] min_cluster_size={mcs} → {n_topics} topics ({outliers} outliers)")

        if target_min <= n_topics <= target_max:
            break
        elif n_topics > target_max:
            mcs += 1
        elif n_topics < target_min and mcs > 2:
            mcs -= 1
            break
        else:
            break

    log(f"  Final: {n_topics} sub-topics (min_cluster_size={mcs}, {outliers} outliers)")

    # 4. TF-IDF 키워드 추출 (c-TF-IDF 대체)
    vectorizer = TfidfVectorizer(max_features=10000, stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(docs)
    feature_names = vectorizer.get_feature_names_out()

    topic_keywords = {}
    for tid in set(topics):
        if tid == -1:
            continue
        indices = [i for i, t in enumerate(topics) if t == tid]
        cluster_tfidf = tfidf_matrix[indices].mean(axis=0).A1
        top_indices = cluster_tfidf.argsort()[-10:][::-1]
        topic_keywords[tid] = [(feature_names[i], float(cluster_tfidf[i])) for i in top_indices]

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

    return topics, probs, topic_keywords, centroids, coords_2d, coords_3d


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
            model="claude-sonnet-4-20250514",
            max_tokens=8000,
            messages=[{"role": "user", "content": prompt}],
        )
        text = resp.content[0].text.strip()
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
        model="claude-sonnet-4-20250514",
        max_tokens=4000,
        messages=[{"role": "user", "content": prompt}],
    )
    text = resp.content[0].text.strip()
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

def compute_related_candidates(embeddings, slugs, top_k=5):
    """코사인 유사도 top-k 후보 선정."""
    from sklearn.metrics.pairwise import cosine_similarity

    log(f"  Computing cosine similarity ({len(slugs)} papers, top_k={top_k})...")
    sim_matrix = cosine_similarity(embeddings)

    candidates = {}
    for i, slug in enumerate(slugs):
        sims = list(enumerate(sim_matrix[i]))
        sims.sort(key=lambda x: -x[1])
        top = [(slugs[j], float(score)) for j, score in sims[1:top_k + 1]]
        candidates[slug] = top

    total = sum(len(v) for v in candidates.values())
    avg = total / len(candidates) if candidates else 0
    log(f"  {total} candidates (avg {avg:.1f}/paper)")
    return candidates


def generate_connections_from_candidates(candidates, topic_papers, client, batch_size=25):
    """임베딩 top-20 후보 -> Sonnet이 이유/관계 작성."""
    from concurrent.futures import ThreadPoolExecutor, as_completed

    slug_to_paper = {p["slug"]: p for p in topic_papers}
    num_to_slug = {p["slug"].split("_")[0]: p["slug"] for p in topic_papers}
    all_connections = {}
    all_slugs = sorted(candidates.keys())
    batches = [all_slugs[i:i + batch_size] for i in range(0, len(all_slugs), batch_size)]
    log(f"  {len(all_slugs)} papers, {len(batches)} batches (parallel 4)...")

    def process_batch(batch_slugs):
        papers_block = []
        for slug in batch_slugs:
            p = slug_to_paper.get(slug, {})
            num = slug.split("_")[0]
            title = p.get("title", "")[:60]
            essence = p.get("essence", "")[:150]
            cands = candidates.get(slug, [])
            cand_text = ", ".join(
                f"[{cs.split('_')[0]}]({sim:.2f})" for cs, sim in cands[:10]
            )
            papers_block.append(
                f"[{num}] {title} | {essence}\n  Candidates: {cand_text}"
            )

        prompt = f"""For each paper below, select the most meaningful related papers from its candidates.
Candidates are sorted by embedding similarity (score in parentheses).

Papers:
{chr(10).join(papers_block)}

Connection types:
- alternative: Same problem, different approach
- extension: Builds on or extends this work
- foundation: Theoretical/methodological foundation
- counterpoint: Opposite perspective or critiques
- application: Applies this method to a real problem

Output ONLY valid JSON:
{{
  "045": [
    {{"target": "123", "relation": "alternative", "reason": "한국어 이유 1문장"}}
  ]
}}

Rules:
- reason은 한국어로 구체적으로 (1문장)
- 유사도가 높아도 의미 없는 연결은 제외
- target은 candidate 목록의 논문 번호만 사용"""

        resp = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=10000,
            messages=[{"role": "user", "content": prompt}],
        )
        text = resp.content[0].text.strip()
        if text.startswith("```"):
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]
        return json.loads(text)

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {
            executor.submit(process_batch, batch): bi
            for bi, batch in enumerate(batches)
        }
        for future in as_completed(futures):
            bi = futures[future]
            try:
                batch_result = future.result()
                for num, conns in batch_result.items():
                    slug = num_to_slug.get(num)
                    if not slug:
                        continue
                    resolved = []
                    for c in conns:
                        target_slug = num_to_slug.get(c.get("target", ""))
                        if target_slug:
                            resolved.append({
                                "slug": target_slug,
                                "relation": c.get("relation", "alternative"),
                                "reason": c.get("reason", ""),
                            })
                    if resolved:
                        existing = all_connections.get(slug, [])
                        seen = {r["slug"] for r in existing}
                        for r in resolved:
                            if r["slug"] not in seen:
                                existing.append(r)
                                seen.add(r["slug"])
                        all_connections[slug] = existing
                log(f"    batch {bi + 1}/{len(batches)}: {len(batch_result)} papers")
            except Exception as e:
                log(f"    batch {bi + 1}/{len(batches)} ERROR: {str(e)[:100]}")
            time.sleep(0.5)

    return all_connections


# ═══════════════════════════════════════════
# Main
# ═══════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="BERTopic topic modeling + UMAP")
    parser.add_argument("--topic", default="ai4s")
    parser.add_argument("--skip-connections", action="store_true")
    parser.add_argument("--skip-classification", action="store_true",
                        help="Skip Steps 4-5 (naming/grouping/assignment). Run embedding, UMAP, connections only.")
    parser.add_argument("--min-cats", type=int, default=8)
    parser.add_argument("--max-cats", type=int, default=12)
    args = parser.parse_args()

    topic = args.topic
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
    topics, probs, topic_keywords, centroids, coords_2d, coords_3d = run_clustering(
        embeddings, slugs, originalities
    )

    from anthropic import Anthropic
    client = Anthropic()

    if args.skip_classification:
        log("\n  [Steps 4-5] SKIP (--skip-classification: preserving existing categories)")
    else:
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
        tid_to_cat, cat_info = group_into_categories(topic_names, topics, centroids, args.min_cats, args.max_cats, client)
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

    # Save topic model info
    topic_info_data = {
        "generated_at": datetime.now().strftime("%Y-%m-%d"),
        "model": "SPECTER2 + sklearn.HDBSCAN + UMAP",
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

    # Step 6
    if not args.skip_connections:
        log("\n" + "=" * 50)
        log("STEP 6: RELATED PAPERS (Embedding + Sonnet)")
        log("=" * 50)
        candidates = compute_related_candidates(embeddings, slugs, top_k=5)
        connections = generate_connections_from_candidates(
            candidates, topic_papers, client
        )
        from lib.connections import sync_topic_connections
        sync_topic_connections(connections, topic, slugs, topic_dir, log=log)

    log("\n" + "=" * 50)
    log("DONE!")
    log(f"  Topics: {len(topic_names)}")
    log(f"  UMAP: {umap_path}")
    log(f"  Cache: {cache_path}")
    log("=" * 50)


if __name__ == "__main__":
    main()
