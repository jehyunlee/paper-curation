"""Retrieved paper connections with original-text-grounded explanations.

Connected papers are the nearest neighbours of a paper in SPECTER2 embedding
space, re-ranked with a title/author BM25 ranking through RRF so that a title
series is not lost (``topic_modeling.compute_related_candidates``). This module
turns those ranked candidates into ``_paper_connections.json`` entries:

* **selection** — the fused rank order decides; ``max_links`` per paper.
* **explanation** — compares both original papers through the shared structured
  text adapter; a separate reverse explanation uses the other perspective.
* **provenance** — ``basis=embedding`` and cosine record retrieval, not a
  bibliographic citation or influence claim. Explanation failures are explicit.
"""
from __future__ import annotations

import os

from lib.relation_explanations import explain_pair

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
                explanation = explain_pair(by_slug[slug], by_slug[target_slug])
                reverse = explanation["reverse"]
                links.append({"slug": target_slug, **explanation,
                              "basis": EMBEDDING_BASIS,
                              "evidence": {**explanation["evidence"], "cosine": cosine},
                              "reverse": {**reverse, "evidence": {
                                  **reverse["evidence"], "cosine": cosine}}})
        result[slug] = links
    return result
