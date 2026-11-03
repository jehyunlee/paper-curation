#!/usr/bin/env python3
"""Classify one reviewed paper and refresh its related-paper links.

First the paper is routed into each topic's existing
categories with the stored HDBSCAN bundle (``classify_papers``, approximate
predict; topics without a bundle are skipped). Then neighbours come from
SPECTER2 vectors (plus title/author BM25 through RRF) in the paper's topic
embedding caches. Anthropic then explains each selected pair from both papers'
source text; retrieval scores are provenance, not reader-facing explanations.
Existing retrieval-backed incoming links are also re-explained. The raw store
is replaced atomically only after every target-related explanation succeeds.

``plan_connections`` is strictly read-only. ``refresh_connections`` owns the
exclusive corpus-operation lock; callers must not wrap it in another corpus
lock.
"""
from __future__ import annotations

import argparse
import contextlib
import json
import math
import re
import sys
from pathlib import Path
from typing import Any

from config_loader import DOCS_DIR, PAPERS_DIR

_SCHEMA_VERSION = 1
# Same alphabet as run_update_force.make_slug: `str.isalnum()` (Unicode
# letters such as ö, é, π, ² included) plus `_` and `-`. macOS stores names
# NFD-decomposed, so combining marks (U+0300-U+036F: Schrödinger, Rényi) must
# pass too. An ASCII-only class used to reject eight real slugs from this
# stage. Path containment is enforced separately by `_inside`.
_SLUG = re.compile(r"^\d{3,}_[^\W_][\w\u0300-\u036f-]*$", re.UNICODE)


def _load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ValueError(f"invalid required sidecar: {path}") from exc


def _inside(root: Path, path: Path, *, kind: str) -> Path:
    """Resolve an input path and reject symlink traversal outside its root."""
    root = root.resolve()
    try:
        resolved = path.resolve(strict=True)
        resolved.relative_to(root)
    except (OSError, ValueError) as exc:
        raise ValueError(f"unsafe {kind} path") from exc
    return resolved


def _belongs_to(topic: str, paper: dict) -> bool:
    return (topic in (paper.get("topics") or [])
            or paper.get("primary_topic") == topic
            or topic in (paper.get("classifications") or {}))


def _context(slug: str) -> tuple[dict, list[dict], list[str]]:
    if not isinstance(slug, str) or not _SLUG.fullmatch(slug):
        raise ValueError("invalid paper slug")
    papers_root = Path(PAPERS_DIR).resolve()
    paper_dir = _inside(papers_root, papers_root / slug, kind="paper")
    if not paper_dir.is_dir():
        raise ValueError("registered reviewed paper directory and review.md are required")
    review = _inside(papers_root, paper_dir / "review.md", kind="review")
    if not review.is_file():
        raise ValueError("registered reviewed paper directory and review.md are required")
    index = _load_json(_inside(papers_root, papers_root / "_papers_index.json", kind="index"))
    if not isinstance(index, list):
        raise ValueError("invalid papers index")
    paper = next((p for p in index if isinstance(p, dict) and p.get("slug") == slug), None)
    if paper is None:
        raise ValueError("paper slug is not registered in _papers_index.json")
    topics = sorted({t for t in (paper.get("topics") or []) if isinstance(t, str) and t}
                    | ({paper["primary_topic"]} if isinstance(paper.get("primary_topic"), str)
                       and paper["primary_topic"] else set())
                    | {t for t in (paper.get("classifications") or {}) if isinstance(t, str) and t})
    if not topics:
        raise ValueError("registered paper has no topics")
    for topic in topics:
        docs_root = Path(DOCS_DIR).resolve()
        cache = _inside(docs_root, docs_root / topic / "_embeddings_cache.json", kind="topic sidecar")
        data = _load_json(cache)
        if not isinstance(data, dict) or not isinstance(data.get("slugs"), list) or not isinstance(data.get("embeddings"), list):
            raise ValueError(f"invalid embedding sidecar for topic: {topic}")
    return paper, index, sorted(set(topics))


def _originality(paper: dict) -> str:
    root = Path(PAPERS_DIR).resolve()
    try:
        path = _inside(root, root / paper["slug"] / "originality.md", kind="originality")
    except ValueError:
        path = root / ".missing-originality"
    try:
        text = path.read_text(encoding="utf-8").strip()
    except OSError:
        text = ""
    # Planning must not invoke topic_modeling.extract_originalities: it writes
    # provenance/originality sidecars.  Execution likewise never regenerates a review.
    return text or f"{paper.get('title', '')}. {paper.get('essence', '')}".strip()


def _topic_pool(topic: str, index: list[dict]) -> list[dict]:
    return [p for p in index if isinstance(p, dict) and p.get("slug") and _belongs_to(topic, p)]


def _cached_embeddings(topic: str, pool: list[dict]) -> tuple[dict[str, Any], dict]:
    docs_root = Path(DOCS_DIR).resolve()
    data = _load_json(_inside(docs_root, docs_root / topic / "_embeddings_cache.json",
                              kind="topic sidecar"))
    slugs, vectors = data["slugs"], data["embeddings"]
    if len(slugs) != len(vectors):
        raise ValueError(f"corrupt embedding sidecar for topic: {topic}")
    return dict(zip(slugs, vectors)), data


def _has_model_bundle(topic: str) -> bool:
    docs_root = Path(DOCS_DIR).resolve()
    try:
        bundle = _inside(docs_root, docs_root / topic / "_hdbscan_model.joblib",
                         kind="topic model bundle")
    except ValueError:
        return False
    return bundle.is_file()


def _is_classified(paper: dict, topic: str) -> bool:
    entry = (paper.get("classifications") or {}).get(topic)
    return (isinstance(entry, dict) and bool(entry.get("primary_category"))
            and isinstance(entry.get("all_categories"), list)
            and bool(entry["all_categories"]))


def plan_connections(slug: str) -> dict:
    """Plan local retrieval and cloud explanations without making paid calls."""
    paper, index, topics = _context(slug)
    classification_plan = [{"topic": t, "model_bundle": _has_model_bundle(t),
                            "classified": _is_classified(paper, t)} for t in topics]
    classify_topics = [c["topic"] for c in classification_plan if c["model_bundle"]]
    from lib.related import max_links
    from lib.text_providers import DEFAULT_MODELS
    limit = max_links()
    details = []
    for topic in topics:
        pool = _topic_pool(topic, index)
        cached, _ = _cached_embeddings(topic, pool)
        missing = [p["slug"] for p in pool if p["slug"] not in cached]
        details.append({"topic": topic, "corpus_size": len(pool),
                        "target_embedding_cached": slug in cached,
                        "missing_embedding_count": len(missing),
                        "candidate_limit": min(limit, max(0, len(pool) - 1))})
    return {"outputs": [], "topics": topics, "related_count": 0,
            "status": "ready",
            "embedding_required": sum(d["missing_embedding_count"] for d in details),
            "candidate_limit": limit, "topic_plan": details,
            "explanation": {"provider": "anthropic",
                            "model": DEFAULT_MODELS["anthropic"],
                            "transmission": "source excerpts from selected pairs and existing retrieval-backed incoming pairs",
                            "credential_ref": "credential:anthropic",
                            "cost_class": "paid"},
            "classification_plan": classification_plan,
            "classify_topics": classify_topics,
            "steps": (["classify_papers"] if classify_topics else [])
                     + ["refresh_paper_connections"],
            "registered_slug": paper["slug"]}


def _embedding_for_target(slug: str, paper: dict, topic: str, pool: list[dict]) -> tuple[list[dict], Any]:
    """Incrementally fill missing reviewed corpus vectors, without refitting."""
    import numpy as np
    docs_root = Path(DOCS_DIR).resolve()
    cache_path = _inside(docs_root, docs_root / topic / "_embeddings_cache.json",
                         kind="topic sidecar")
    mapping, data = _cached_embeddings(topic, pool)
    if mapping:
        existing_matrix = np.asarray(list(mapping.values()), dtype=float)
        if (existing_matrix.ndim != 2 or not np.isfinite(existing_matrix).all()
                or len({len(v) for v in mapping.values()}) != 1):
            raise ValueError(f"invalid cached embedding vectors for topic: {topic}")
    missing = [p for p in pool if p["slug"] not in mapping]
    if missing:
        from lib.specter2_embed import embed_texts
        from lib import specter2_embed
        tag = data.get("embed_model")
        if tag != specter2_embed.EMBED_TAG:
            raise ValueError(f"embedding model mismatch for topic: {topic}")
        papers_root = Path(PAPERS_DIR).resolve()
        for item in missing:
            review = _inside(papers_root, papers_root / item["slug"] / "review.md",
                             kind="candidate review")
            if not review.is_file():
                raise ValueError(f"missing reviewed candidate: {item['slug']}")
        vectors = np.asarray(embed_texts([_originality(p) for p in missing]), dtype=float)
        if data.get("embed_model") != specter2_embed.EMBED_TAG:
            raise ValueError(f"embedding model changed during update for topic: {topic}")
        existing = next(iter(mapping.values()), None)
        expected_dim = len(existing) if existing is not None else vectors.shape[1]
        if (vectors.ndim != 2 or len(vectors) != len(missing) or vectors.shape[1] != expected_dim
                or not np.isfinite(vectors).all()):
            raise ValueError(f"invalid incremental embeddings for topic: {topic}")
        for item, vector in zip(missing, vectors):
            mapping[item["slug"]] = vector.tolist()
        # Keep cached entries for papers outside this current topic pool: a
        # stale cache must not erase unrelated vectors during a single refresh.
        slugs = sorted(mapping)
        data["slugs"] = slugs
        data["embeddings"] = [mapping[s] for s in slugs]
        # Preserve the existing model contract; only extend digest metadata when present.
        if isinstance(data.get("originality_sha256"), dict):
            from lib.originality_extractor import text_digest
            data["originality_sha256"].update(
                {item["slug"]: text_digest(_originality(item)) for item in missing})
        tmp = cache_path.with_suffix(cache_path.suffix + ".tmp")
        tmp.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        tmp.replace(cache_path)
    ordered = [p for p in pool if p["slug"] in mapping]
    return ordered, np.asarray([mapping[p["slug"]] for p in ordered])


def _published_topic_connections() -> dict[str, dict]:
    """Snapshot unfiltered consumer views before legacy edges are discarded."""
    docs_root = Path(DOCS_DIR).resolve()
    views = {}
    for path in sorted(docs_root.glob("*/_paper_connections.json")):
        view = _load_json(_inside(docs_root, path, kind="topic connections"))
        if (not isinstance(view, dict)
                or any(not isinstance(source, str) or not isinstance(entries, list)
                       or any(not isinstance(entry, dict)
                              or not isinstance(entry.get("slug"), str)
                              for entry in entries)
                       for source, entries in view.items())):
            raise ValueError(f"invalid published connections for topic: {path.parent.name}")
        views[path.parent.name] = view
    return views


def _load_raw_connections() -> dict[str, list[dict]]:
    """Keep unrelated raw entries, including retired bases hidden from views."""
    root = Path(PAPERS_DIR).resolve()
    path = root / "_global_connections.json"
    if not path.exists() and not path.is_symlink():
        return {}
    stored = _load_json(_inside(root, path, kind="global connections"))
    if (not isinstance(stored, dict)
            or any(not isinstance(source, str) or not isinstance(entries, list)
                   or any(not isinstance(entry, dict) or not isinstance(entry.get("slug"), str)
                          for entry in entries)
                   for source, entries in stored.items())):
        raise ValueError("invalid raw global connections")
    return stored


def _target_connection_update(slug: str, connections: dict, previous: dict,
                              papers: dict[str, dict], source_topic: str) -> dict:
    """Prepare all outgoing/incoming replacements without publishing a partial graph."""
    from lib.related import EMBEDDING_BASIS, build_connections

    updated = {**previous, slug: [dict(entry, source_topic=source_topic)
                                 for entry in connections[slug]]}
    for source, entries in previous.items():
        if source == slug:
            continue
        replacements = []
        for entry in entries:
            if entry.get("slug") != slug or entry.get("basis") != EMBEDDING_BASIS:
                replacements.append(entry)
                continue
            if source not in papers:
                raise ValueError(f"unregistered incoming connection source: {source}")
            evidence = entry.get("evidence")
            cosine = evidence.get("cosine") if isinstance(evidence, dict) else None
            if (isinstance(cosine, bool) or not isinstance(cosine, (int, float))
                    or not -1 <= cosine <= 1 or not math.isfinite(cosine)):
                raise ValueError(f"incoming connection requires valid cosine evidence: {source}")
            links = build_connections({source: [(slug, cosine)]},
                                      [papers[source], papers[slug]], limit=1)[source]
            if not links:
                # A source without original text cannot ground the reason.
                continue
            explained = links[0]
            replacement = {**entry, **explained,
                           "evidence": {**explained["evidence"], "cosine": cosine},
                           "reverse": {**explained["reverse"], "evidence": {
                               **explained["reverse"]["evidence"], "cosine": cosine}}}
            # A legacy consumer-view payload must not override the new explanation.
            replacement.pop("reasons", None)
            replacements.append(replacement)
        updated[source] = replacements
    return updated


def _refresh_connections_locked(slug: str) -> dict:
    """Classify, then embed/retrieve one paper and publish its bidirectional views.

    Called only while the exclusive corpus operation lock is held.
    """
    plan = plan_connections(slug)
    _, _, all_topics = _context(slug)
    classify_topics = sorted(t for t in all_topics if _has_model_bundle(t))
    unclassified_topics = [t for t in all_topics if t not in classify_topics]
    classify_outputs: list[str] = []
    if classify_topics:
        from classify_papers import _run_classify
        for topic in classify_topics:
            _run_classify(topic, slugs=[slug], dry_run=False)
            # Re-read the index: classification must be durable before any
            # connection or global mutation happens.
            done, _, _ = _context(slug)
            if not _is_classified(done, topic):
                raise RuntimeError(f"classification did not complete for topic: {topic}")
            topic_dir = Path(DOCS_DIR) / topic
            classify_outputs += [str(topic_dir / "_new_classification.json"),
                                 str(topic_dir / "_umap_coords.json")]
    paper, index, topics = _context(slug)
    published_views = _published_topic_connections()
    from lib.related import build_connections, max_links
    from topic_modeling import RELATED_RRF_K, compute_related_candidates
    merged_candidates: dict[str, float] = {}
    fused_ranks: dict[str, float] = {}
    for topic in topics:
        pool = _topic_pool(topic, index)
        papers, embeddings = _embedding_for_target(slug, paper, topic, pool)
        candidates = compute_related_candidates(embeddings, [p["slug"] for p in papers],
                                                top_k=max_links(), papers=papers).get(slug, [])
        for rank, (other, score) in enumerate(candidates, 1):
            if other == slug:
                continue
            fused_ranks[other] = fused_ranks.get(other, 0.0) + 1.0 / (RELATED_RRF_K + rank)
            merged_candidates[other] = max(score, merged_candidates.get(other, -1.0))
    # The whole operation has a bounded, unique candidate set, not a per-topic multiplication.
    # Candidate scores are cosine evidence, NOT the hybrid ranking score.
    # Preserve each topic's RRF order instead of reverting to dense-only sorting.
    selected = sorted(merged_candidates.items(), key=lambda x: (-fused_ranks[x[0]], x[0]))[:max_links()]
    all_papers = {p["slug"]: p for p in index if isinstance(p, dict) and p.get("slug")}
    candidate_papers = [paper] + [all_papers[s] for s, _ in selected if s in all_papers]
    previous = _load_raw_connections()
    connections = build_connections({slug: selected}, candidate_papers, limit=len(selected))
    updated = _target_connection_update(slug, connections, previous, all_papers, topics[0])

    from lib.atomic_io import atomic_write_json
    from lib.connections import (build_slug_resolver, filter_for_topic,
                                 make_bidirectional_deduped, save_global_connections)
    from lib.related import EMBEDDING_BASIS

    # Published views can also contain retired-basis links absent from the
    # retrieval-backed projection. Their pages must lose the obsolete reasons.
    affected_slugs = ({slug} | {e["slug"] for e in connections.get(slug, [])}
                      | {e["slug"] for e in previous.get(slug, [])}
                      | {source for source, entries in previous.items()
                         if any(e["slug"] == slug for e in entries)})
    for view in published_views.values():
        affected_slugs.update(e["slug"] for e in view.get(slug, []))
        affected_slugs.update(source for source, entries in view.items()
                              if any(e["slug"] == slug for e in entries))
    affected_slugs.intersection_update(all_papers)
    affected_topics = sorted({t for p in index if isinstance(p, dict) and p.get("slug") in affected_slugs
                              for t in ((p.get("topics") or [])
                                        + ([p["primary_topic"]] if isinstance(p.get("primary_topic"), str) else [])
                                        + list((p.get("classifications") or {})))
                              if isinstance(t, str)})
    affected_topics = sorted(set(affected_topics) | set(topics)
                             | {t for t, view in published_views.items()
                                if affected_slugs.intersection(view)})
    old_sources = {source for topic in affected_topics
                   for source in published_views.get(topic, {}) if source in all_papers}
    # Keep the existing consumer basis filter, without dropping unrelated raw
    # entries by round-tripping through the filtered global loader/merge path.
    visible = {source: [entry for entry in entries if entry.get("basis") == EMBEDDING_BASIS]
               for source, entries in updated.items()}
    current_view = make_bidirectional_deduped(visible,
                                            resolve=build_slug_resolver(all_papers))
    # Keep deleted published sources explicitly empty, so a newer view clears
    # an older topic's cached legacy entry. Active reverse-only sources need no
    # raw key, and unrelated clean sources must not become render targets.
    cleared = {source: [] for source in sorted(old_sources - current_view.keys())}
    updated.update(cleared)
    current_view.update(cleared)
    # All explanations and the projection have succeeded. Replace raw claims
    # once, then publish each affected view from that exact snapshot.
    save_global_connections(updated)
    for topic in affected_topics:
        topic_dir = _inside(Path(DOCS_DIR).resolve(), Path(DOCS_DIR).resolve() / topic,
                            kind="topic")
        topic_slugs = (list(all_papers) if topic == "_cross"
                       else [p["slug"] for p in _topic_pool(topic, index)])
        view = filter_for_topic(current_view, topic_slugs)
        atomic_write_json(topic_dir / "_paper_connections.json", view)
        old_view = published_views.get(topic, {})
        affected_slugs.update(source for source in set(old_view) | set(view)
                              if source in all_papers and old_view.get(source) != view.get(source))

    from review_to_html import _run_review_to_html
    import review_to_html
    review_to_html._connections_cache = {}
    rendered = _run_review_to_html(slugs=sorted(affected_slugs), with_connected=False)
    if rendered.get("converted") != len(affected_slugs) or rendered.get("skipped"):
        raise RuntimeError("connection pages did not render completely")
    outputs = list(classify_outputs)
    outputs += [str(Path(DOCS_DIR) / t / "_paper_connections.json") for t in affected_topics]
    outputs += [str(Path(PAPERS_DIR) / s / "index.html") for s in sorted(affected_slugs)]
    return {"outputs": outputs, "topics": affected_topics,
            "related_count": len(connections.get(slug, [])), "status": "completed",
            "rendered": rendered, "candidate_count": len(selected),
            "classified_topics": classify_topics,
            "unclassified_topics": unclassified_topics, "plan": plan}


def refresh_connections(slug: str) -> dict:
    """Refresh connections, then their published views after releasing the lease."""
    from lib.corpus_store import corpus_operation_lock
    with corpus_operation_lock(PAPERS_DIR, exclusive=True):
        result = _refresh_connections_locked(slug)
    if result.get("status") != "completed":
        return result
    from refresh_paper_views import PAPERS_DIR as canonical_papers, refresh_paper_views
    if Path(PAPERS_DIR).resolve() != Path(canonical_papers).resolve():
        return result
    try:
        views = refresh_paper_views(slug, papers_dir=PAPERS_DIR,
                                    previous_topics=result.get("topics", []))
    except Exception as exc:
        import shlex
        command = [sys.executable, str(Path(__file__).with_name("refresh_paper_views.py")),
                   "--slug", slug]
        for topic in result.get("topics", []):
            command += ["--previous-topic", topic]
        views = {"status": "failed", "topics": [], "steps": [],
                 "errors": [f"view refresh failed: {type(exc).__name__}"],
                 "retry_command": shlex.join(command)}
    result["views"] = views
    if views["status"] != "completed":
        result["status"] = "failed"
        result["error"] = "Connections are retained; retry view refresh only."
        result["partial"] = {"connections_published": True, "retry_safe": True,
                             "retry_command": views["retry_command"]}
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()
    try:
        if args.execute:
            with contextlib.redirect_stdout(sys.stderr):
                result = refresh_connections(args.slug)
        else:
            result = plan_connections(args.slug)
        result.update({"schema_version": _SCHEMA_VERSION, "feature": "related-papers"})
    except Exception as exc:
        result = {"schema_version": _SCHEMA_VERSION, "feature": "related-papers",
                  "status": "failed", "error": f"{type(exc).__name__}: operation failed",
                  "outputs": [], "topics": [], "related_count": 0}
    print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
    return 0 if result["status"] in {"ready", "completed"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
