"""Retrieved paper connections with summary-based explanations.

Connected papers are the nearest neighbours of a paper in SPECTER2 embedding
space, re-ranked with a title/author BM25 ranking through RRF so that a title
series is not lost (``topic_modeling.compute_related_candidates``). This module
turns those ranked candidates into ``_paper_connections.json`` entries:

* **selection** — the fused rank order decides; ``max_links`` per paper. A
  paper with neither review essence nor originality summary can neither be explained nor explain, so
  it is skipped as a neighbour and gets no outgoing links.
* **explanation** — compares both papers' summaries (title, date, authors, classification,
  essence, originality) through the shared structured text adapter; earlier
  text-grounded explanations are reused from cache; a separate reverse explanation uses the other perspective.
  Each unordered pair is explained once, concurrently across
  ``RELATED_EXPLAIN_WORKERS`` threads; the opposite edge reuses it.
* **provenance** — ``basis=embedding`` and cosine record retrieval, not a
  bibliographic citation or influence claim. Explanation failures are explicit:
  every pair is attempted (successes stay cached for a rerun), then the first
  failure is raised.
"""
from __future__ import annotations

import os
from concurrent.futures import ThreadPoolExecutor

from lib.relation_explanations import MissingSourceText, explain_pair

MAX_LINKS_ENV = "RELATED_LINKS"
DEFAULT_MAX_LINKS = 5
WORKERS_ENV = "RELATED_EXPLAIN_WORKERS"
DEFAULT_WORKERS = 8
EMBEDDING_BASIS = "embedding"


def _bounded_env(name: str, default: int, upper: int) -> int:
    raw = os.environ.get(name, "").strip()
    try:
        value = int(raw) if raw else default
    except ValueError:
        value = default
    return max(1, min(value, upper))


def max_links() -> int:
    return _bounded_env(MAX_LINKS_ENV, DEFAULT_MAX_LINKS, 20)


def explain_workers() -> int:
    return _bounded_env(WORKERS_ENV, DEFAULT_WORKERS, 32)


def build_connections(candidates: dict, papers: list[dict], *, limit: int | None = None) -> dict:
    """``{slug: [(target_slug, cosine), ...]}`` → ``{slug: [connection, ...]}``.

    Every key in ``candidates`` appears in the result (possibly with an empty
    list) so callers can tell "processed, no neighbour" from "not processed".
    """
    limit = limit or max_links()
    by_slug = {p["slug"]: p for p in papers if isinstance(p, dict) and p.get("slug")}
    selected: dict[str, list[tuple[str, float]]] = {}
    for slug, ranked in candidates.items():
        links = []
        if slug in by_slug:
            for entry in list(ranked)[:limit]:
                target_slug, cosine = (entry if isinstance(entry, (tuple, list)) else (entry, 0.0))
                if target_slug not in by_slug or target_slug == slug:
                    continue
                links.append((target_slug, round(float(cosine), 4)))
        selected[slug] = links

    # One request per unordered pair, oriented as first encountered in rank
    # order; the opposite edge reads the same explanation from the other side.
    requests: dict[frozenset, tuple[str, str]] = {}
    for slug, links in selected.items():
        for target_slug, _ in links:
            requests.setdefault(frozenset((slug, target_slug)), (slug, target_slug))
    explained: dict[tuple[str, str], dict] = {}
    ungrounded: set[frozenset] = set()
    failures: list[Exception] = []

    def run(pair):
        try:
            explained[pair] = explain_pair(by_slug[pair[0]], by_slug[pair[1]])
        except MissingSourceText:
            ungrounded.add(frozenset(pair))
        except Exception as exc:  # collected; raised after every pair was attempted
            failures.append(exc)

    with ThreadPoolExecutor(max_workers=explain_workers()) as pool:
        list(pool.map(run, list(requests.values())))
    if failures:
        raise failures[0]

    result = {}
    for slug, links in selected.items():
        out = []
        for target_slug, cosine in links:
            key = frozenset((slug, target_slug))
            if key in ungrounded:
                continue
            asked = requests[key]
            explanation = explained[asked]
            if asked != (slug, target_slug):
                explanation = _flip(explanation)
            reverse = explanation["reverse"]
            out.append({"slug": target_slug, **explanation,
                        "basis": EMBEDDING_BASIS,
                        "evidence": {**explanation["evidence"], "cosine": cosine},
                        "reverse": {**reverse, "evidence": {
                            **reverse["evidence"], "cosine": cosine}}})
        result[slug] = out
    return result


def _flip(explanation: dict) -> dict:
    """The same pair explanation seen from the other paper."""
    forward = {k: explanation[k] for k in ("relation", "reason", "evidence")}
    return {**explanation["reverse"], "model": explanation["model"], "reverse": forward}
