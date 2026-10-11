"""No-model fallback for related-paper connections computed in embedding space.

The candidate ranking already fuses SPECTER2 cosine similarity with a
title/author BM25 ranking (``topic_modeling.compute_related_candidates``).
This module turns those ranked candidates into the ``_paper_connections.json``
entries deterministically:

* **selection** — the fused rank order decides; ``max_links`` per paper.
* **relation** — always ``alternative``: retrieval metadata cannot establish a
  content relationship.
* **reason** — an explicit no-analysis notice. Content explanations are
  supplied by ``lib.relation_judge.py`` when that optional stage is used.

Stdlib only. Never import a provider SDK here; ``tests/test_related_connections.py``
guards that this stage cannot regress into a paid judge again.
"""
from __future__ import annotations

import os
import re

MAX_LINKS_ENV = "RELATED_LINKS"
DEFAULT_MAX_LINKS = 5
METADATA_REASON = "관계 미분석 — 임베딩 유사도로 추천된 후보입니다."


def max_links() -> int:
    raw = os.environ.get(MAX_LINKS_ENV, "").strip()
    try:
        value = int(raw) if raw else DEFAULT_MAX_LINKS
    except ValueError:
        value = DEFAULT_MAX_LINKS
    return max(1, min(value, 20))


def _year(paper: dict) -> int | None:
    match = re.search(r"(19|20)\d{2}", str(paper.get("date") or paper.get("year") or ""))
    return int(match.group(0)) if match else None


def describe_link(source: dict, target: dict, cosine: float, topic: str | None) -> tuple[str, str, dict]:
    """Return the honest metadata fallback and retrieval evidence."""
    source_year, target_year = _year(source), _year(target)
    evidence = {"cosine": round(float(cosine), 4), "source_year": source_year,
                "target_year": target_year}
    return "alternative", METADATA_REASON, evidence


def build_connections(candidates: dict, papers: list[dict], *, topic: str | None = None,
                      limit: int | None = None) -> dict:
    """``{slug: [(target_slug, cosine), ...]}`` → ``{slug: [connection, ...]}``.

    Every key in ``candidates`` appears in the result (possibly with an empty
    list) so callers can tell "processed, no neighbour" from "not processed".
    """
    limit = limit or max_links()
    by_slug = {p["slug"]: p for p in papers if isinstance(p, dict) and p.get("slug")}
    result = {}
    for slug, ranked in candidates.items():
        source = by_slug.get(slug)
        links = []
        if source is not None:
            for entry in list(ranked)[:limit]:
                target_slug, cosine = (entry if isinstance(entry, (tuple, list)) else (entry, 0.0))
                target = by_slug.get(target_slug)
                if target is None or target_slug == slug:
                    continue
                relation, reason, evidence = describe_link(source, target, float(cosine), topic)
                links.append({"slug": target_slug, "relation": relation, "reason": reason,
                              "basis": "metadata", "model": "", "evidence": evidence})
        result[slug] = links
    return result
