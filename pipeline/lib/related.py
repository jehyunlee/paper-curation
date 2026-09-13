"""Related-paper connections computed in embedding space — no language model.

The candidate ranking already fuses SPECTER2 cosine similarity with a
title/author BM25 ranking (``topic_modeling.compute_related_candidates``).
This module turns those ranked candidates into the ``_paper_connections.json``
entries deterministically:

* **selection** — the fused rank order decides; ``max_links`` per paper.
* **relation** — derived only from recorded metadata: shared authors plus the
  publication order give ``foundation`` (earlier work by the same group) or
  ``extension`` (later work by the same group); everything else is
  ``alternative``. No relation is invented.
* **reason** — one Korean sentence that states the evidence actually used
  (cosine, shared authors, category, year gap), so a reader can check it.

Stdlib only. Never import a provider SDK here; ``tests/test_related_connections.py``
guards that this stage cannot regress into a paid judge again.
"""
from __future__ import annotations

import os
import re
import unicodedata

MAX_LINKS_ENV = "RELATED_LINKS"
DEFAULT_MAX_LINKS = 5


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


def _author_keys(paper: dict) -> set[str]:
    """Normalised surname keys (accent-folded, lowercase) for overlap checks."""
    keys = set()
    for author in paper.get("authors") or []:
        if isinstance(author, dict):
            author = author.get("lastName") or author.get("name") or ""
        folded = unicodedata.normalize("NFKD", str(author))
        folded = "".join(c for c in folded if not unicodedata.combining(c)).lower()
        parts = [p for p in re.split(r"[\s,]+", folded) if p]
        if parts:
            keys.add(parts[-1] if len(parts[-1]) > 1 else parts[0])
    return keys


def _primary_category(paper: dict, topic: str | None) -> str:
    classes = paper.get("classifications") or {}
    if topic and isinstance(classes.get(topic), dict):
        return str(classes[topic].get("primary_category") or "")
    for value in classes.values():
        if isinstance(value, dict) and value.get("primary_category"):
            return str(value["primary_category"])
    return str(paper.get("primary_category") or "")


def describe_link(source: dict, target: dict, cosine: float, topic: str | None) -> tuple[str, str, dict]:
    """Return ``(relation, reason_ko, evidence)`` from recorded metadata only."""
    shared = sorted(_author_keys(source) & _author_keys(target))
    source_year, target_year = _year(source), _year(target)
    source_cat, target_cat = _primary_category(source, topic), _primary_category(target, topic)

    relation = "alternative"
    if shared and source_year and target_year and target_year != source_year:
        relation = "foundation" if target_year < source_year else "extension"

    parts = [f"SPECTER2 임베딩 유사도 {cosine:.2f}"]
    if source_cat and target_cat:
        parts.append(f"같은 카테고리({source_cat})" if source_cat == target_cat
                     else f"인접 카테고리({target_cat})")
    if shared:
        names = ", ".join(s.title() for s in shared[:3])
        parts.append(f"공저자 {len(shared)}명 공유({names})")
    if source_year and target_year and target_year != source_year:
        gap = abs(source_year - target_year)
        parts.append(f"{gap}년 {'앞선' if target_year < source_year else '뒤의'} 연구")
    reason = " · ".join(parts) + "."

    evidence = {"cosine": round(float(cosine), 4), "shared_authors": shared,
                "source_year": source_year, "target_year": target_year,
                "same_category": bool(source_cat and source_cat == target_cat)}
    return relation, reason, evidence


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
                              "evidence": evidence})
        result[slug] = links
    return result
