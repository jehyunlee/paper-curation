"""Related-paper connections, found in embedding space. No model is called.

Connected papers are the nearest neighbours of a paper in SPECTER2 embedding
space, re-ranked with a title/author BM25 ranking through RRF so that a title
series is not lost (``topic_modeling.compute_related_candidates``). This module
turns those ranked candidates into ``_paper_connections.json`` entries:

* **selection** — the fused rank order decides; ``max_links`` per paper.
* **relation** — always ``alternative`` (the neutral, mutual label). Retrieval
  cannot establish a directed relationship, and no LLM is asked to invent one.
* **reason** — states the embedding evidence (SPECTER2 cosine).

Stdlib only. Never import a provider SDK here; ``tests/test_related_connections.py``
guards that connection finding cannot regress into an LLM judge again.
"""
from __future__ import annotations

import os

MAX_LINKS_ENV = "RELATED_LINKS"
DEFAULT_MAX_LINKS = 5
EMBEDDING_BASIS = "embedding"


def max_links() -> int:
    raw = os.environ.get(MAX_LINKS_ENV, "").strip()
    try:
        value = int(raw) if raw else DEFAULT_MAX_LINKS
    except ValueError:
        value = DEFAULT_MAX_LINKS
    return max(1, min(value, 20))


def embedding_reason(cosine: float) -> str:
    return f"SPECTER2 임베딩 공간에서 가까운 논문입니다 (코사인 유사도 {cosine:.2f})."


def build_connections(candidates: dict, papers: list[dict], *, limit: int | None = None) -> dict:
    """``{slug: [(target_slug, cosine), ...]}`` → ``{slug: [connection, ...]}``.

    Every key in ``candidates`` appears in the result (possibly with an empty
    list) so callers can tell "processed, no neighbour" from "not processed".
    """
    limit = limit or max_links()
    by_slug = {p["slug"]: p for p in papers if isinstance(p, dict) and p.get("slug")}
    result = {}
    for slug, ranked in candidates.items():
        links = []
        if slug in by_slug:
            for entry in list(ranked)[:limit]:
                target_slug, cosine = (entry if isinstance(entry, (tuple, list)) else (entry, 0.0))
                if target_slug not in by_slug or target_slug == slug:
                    continue
                cosine = round(float(cosine), 4)
                links.append({"slug": target_slug, "relation": "alternative",
                              "reason": embedding_reason(cosine),
                              "basis": EMBEDDING_BASIS, "model": "",
                              "evidence": {"cosine": cosine}})
        result[slug] = links
    return result
