"""Rebuild the bidirectional, per-target-deduped connection view + re-render.

Connections are stored in two layers (see ``lib/connections.py``):

  * ``docs/papers/_global_connections.json`` — the **raw, directional** store
    (one ``source_topic``-tagged A→B edge per generated connection). This is the
    durable accumulator written by every ``extract_insights`` / ``topic_modeling``
    run through ``sync_topic_connections``.
  * ``docs/<topic>/_paper_connections.json`` — the **consumer view** every
    renderer reads: the *bidirectional + per-target-deduped* projection of the
    global store (each A→B implies B→A with the relation flipped, and a paper
    connected for several reasons appears once with all reasons listed).

Normal pipeline runs already produce this automatically — ``sync_topic_connections``
applies the transform on every run, and ``review_to_html`` renders each reason
with its own relation badge and turns every ``[NNN]`` reference into a link. So
**both paper-curation and paper-curio emit connections in exactly this shape going
forward.** This script is the reproducible, LLM-free way to:

  * recompute every topic's connections in SPECTER2 embedding space from its
    ``_embeddings_cache.json`` (``--recompute``; missing vectors are embedded
    locally, no LLM is called) and replace the whole global store,
  * re-apply the transform to the existing global store, and
  * re-render every affected paper page (and, by default, the D3 networks),

e.g. after editing the transform/render logic or to reproduce the state on demand.

Usage:
  PYTHONUTF8=1 python pipeline/rebuild_connections.py                  # all topics: data + pages + networks
  PYTHONUTF8=1 python pipeline/rebuild_connections.py --recompute      # recompute neighbours in embedding space first
  PYTHONUTF8=1 python pipeline/rebuild_connections.py --topics ai4s scisci
  PYTHONUTF8=1 python pipeline/rebuild_connections.py --no-render      # rebuild topic JSON only
  PYTHONUTF8=1 python pipeline/rebuild_connections.py --no-networks    # data + pages, skip networks
  PYTHONUTF8=1 python pipeline/rebuild_connections.py --dry-run        # report only, write nothing
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from lib.connections import (              # noqa: E402
    load_global_connections, make_bidirectional_deduped, filter_for_topic,
    build_slug_resolver, save_global_connections,
)
from lib.atomic_io import atomic_write_json, atomic_write_text  # noqa: E402
from lib.corpus_store import _is_safe_slug, corpus_operation_lock  # noqa: E402

ROOT = os.path.dirname(_HERE)
DOCS = os.path.join(ROOT, "docs")
PAPERS = os.path.join(DOCS, "papers")
INDEX = os.path.join(PAPERS, "_papers_index.json")


def safe_path(root, path):
    """Check an input/output path without creating it or following symlinks."""
    base = Path(root).absolute()
    root = base.resolve()
    path = Path(path).absolute()
    try:
        parts = path.relative_to(base).parts
    except ValueError:
        try:
            parts = path.relative_to(root).parts
        except ValueError as exc:
            raise ValueError(f"path outside corpus: {path}") from exc
    current = root
    for i, part in enumerate(parts):
        if part in (".", ".."):
            raise ValueError(f"unsafe corpus path: {path}")
        current /= part
        if current.is_symlink():
            raise ValueError(f"symlink corpus path: {current}")
        if i < len(parts) - 1 and current.exists() and not current.is_dir():
            raise ValueError(f"invalid corpus directory: {current}")
    return current


def topic_path(topic):
    if (not isinstance(topic, str) or not topic or topic == "papers"
            or (topic.startswith("_") and topic != "_cross")
            or not all(c.isalnum() or c in "_-+" for c in topic)):
        raise ValueError(f"invalid topic: {topic!r}")
    path = safe_path(DOCS, Path(DOCS) / topic)
    if path.exists() and not path.is_dir():
        raise ValueError(f"invalid topic directory: {path}")
    return path


def paper_path(slug):
    if not _is_safe_slug(slug):
        raise ValueError(f"invalid paper slug: {slug!r}")
    path = safe_path(PAPERS, Path(PAPERS) / slug)
    if path.exists() and not path.is_dir():
        raise ValueError(f"invalid paper directory: {path}")
    return path


def validate_paper_files(slug):
    directory = paper_path(slug)
    for name in ("review.md", "review.md.tmp", "index.html", "originality.md",
                 "originality.meta.json", "text.md", "_figs_inline.js",
                 "_figs_inline.js.tmp", "figures"):
        safe_path(PAPERS, directory / name)
    return directory


def paper_topics(paper):
    """Authoritative membership is the union of all three index fields."""
    topics = paper.get("topics") or []
    classifications = paper.get("classifications") or {}
    primary = paper.get("primary_topic")
    if (not isinstance(topics, list) or not isinstance(classifications, dict)
            or any(not isinstance(t, str) for t in topics)
            or (primary is not None and not isinstance(primary, str))):
        raise ValueError(f"invalid topic memberships: {paper.get('slug')}")
    memberships = set(topics) | set(classifications)
    if primary:
        memberships.add(primary)
    for topic in memberships:
        topic_path(topic)
        if topic == "_cross":
            raise ValueError("_cross is a derived view, not a paper topic")
    return memberships


def load_index():
    """Read and validate the index and paper paths without modifying sidecars."""
    safe_path(DOCS, PAPERS)
    with safe_path(PAPERS, INDEX).open(encoding="utf-8") as f:
        index = json.load(f)
    if not isinstance(index, list):
        raise ValueError("papers index must be a list")
    seen = set()
    for paper in index:
        if not isinstance(paper, dict):
            raise ValueError("invalid paper index entry")
        slug = paper.get("slug")
        validate_paper_files(slug)
        if slug in seen:
            raise ValueError(f"duplicate paper slug: {slug}")
        seen.add(slug)
        paper_topics(paper)
    return index


def topic_slug_map(index=None):
    """topic -> set(slugs), including primary and classification memberships."""
    mapping = {}
    for paper in load_index() if index is None else index:
        for topic in paper_topics(paper):
            mapping.setdefault(topic, set()).add(paper["slug"])
    return mapping


def discover_topics(index=None):
    """Include index memberships and old output topics that need clearing."""
    topics = set(topic_slug_map(index))
    for directory in Path(DOCS).iterdir():
        if (directory / "_paper_connections.json").exists() or directory.name == "_cross":
            topic_path(directory.name)
            topics.add(directory.name)
    return sorted(topics)


def validate_connections(connections):
    if not isinstance(connections, dict):
        raise ValueError("connection snapshot must be an object")
    for slug, entries in connections.items():
        paper_path(slug)
        if not isinstance(entries, list):
            raise ValueError(f"invalid connections for {slug}")
        for entry in entries:
            if not isinstance(entry, dict):
                raise ValueError(f"invalid connection for {slug}")
            paper_path(entry.get("slug"))


def plan_rebuild(topics=None, *, recompute=False):
    """Take a read-only snapshot; execution calls this only inside its lease."""
    index = load_index()
    selected = discover_topics(index) if topics is None else sorted(set(topics))
    previous_sources = set()
    for topic in selected:
        directory = topic_path(topic)
        for name in ("_paper_connections.json", "_paper_connections.json.tmp",
                     "_embeddings_cache.json", "_umap_coords.json", "network.html"):
            safe_path(DOCS, directory / name)
        old_path = directory / "_paper_connections.json"
        if old_path.exists():
            with old_path.open(encoding="utf-8") as f:
                previous = json.load(f)
            validate_connections(previous)
            previous_sources.update(previous)
    global_path = safe_path(PAPERS, Path(PAPERS) / "_global_connections.json")
    safe_path(PAPERS, global_path.with_suffix(".json.tmp"))
    global_connections = load_global_connections()
    validate_connections(global_connections)
    if recompute:
        previous_sources.update(global_connections)
        previous_sources.update(e["slug"] for edges in global_connections.values() for e in edges)
        mapping = topic_slug_map(index)
        for paper in index:
            if any(len(mapping[t]) > 1 for t in paper_topics(paper)) and not paper_path(paper["slug"]).is_dir():
                raise ValueError(f"missing paper directory: {paper['slug']}")
    for slug in previous_sources:
        validate_paper_files(slug)
    return {"topics": selected, "index": index,
            "global_connections": global_connections,
            "previous_sources": previous_sources}


def recompute_global(topics, dry_run=False, *, index=None):
    """Replace the global store with embedding-space neighbours for ``topics``.

    Same retrieval as ``topic_modeling`` Step 6: SPECTER2 cosine fused with
    title/author BM25 (RRF) over the topic's papers. Vectors come from the
    topic's ``_embeddings_cache.json``; only missing or changed ones are embedded,
    locally. Every topic paper is a source, so nothing is left from a prior run.
    """
    index = load_index() if index is None else index
    mapping = topic_slug_map(index)
    for topic in topics:
        topic_path(topic)
    if dry_run:
        for topic in topics:
            print(f"  [dry-run] {topic}: would recompute {len(mapping.get(topic, ()))} papers")
        print(f"  [dry-run] would replace the global store, including all {len(index)} sources")
        return None

    # Explicitly retain processed-empty sources, including singleton/unassigned papers.
    store = {paper["slug"]: [] for paper in index}
    for topic in topics:
        pool = [p for p in index if p["slug"] in mapping.get(topic, ())]
        if len(pool) < 2:
            print(f"  {topic}: {len(pool)} papers, 0 embedding edges")
            continue
        from lib.related import build_connections, max_links
        from topic_modeling import (compute_embeddings, compute_related_candidates,
                                    extract_originalities)

        directory = topic_path(topic)
        directory.mkdir(parents=True, exist_ok=True)
        cache = str(directory / "_embeddings_cache.json")
        embeddings, slugs = compute_embeddings(extract_originalities(pool), cache)
        by_slug = {p["slug"]: p for p in pool}
        if len(slugs) != len(by_slug) or set(slugs) != set(by_slug):
            raise RuntimeError(f"incomplete embeddings for topic: {topic}")
        papers = [by_slug[s] for s in slugs]
        candidates = compute_related_candidates(embeddings, slugs, top_k=max_links(),
                                                papers=papers)
        connections = build_connections(candidates, papers)
        for slug, links in connections.items():
            bucket = store.setdefault(slug, [])
            seen = {c["slug"] for c in bucket}
            bucket.extend(dict(c, source_topic=topic) for c in links if c["slug"] not in seen)
        print(f"  {topic}: {len(connections)} papers, "
              f"{sum(len(v) for v in connections.values())} embedding edges")
    save_global_connections(store)
    print(f"  global store replaced: {len(store)} sources")
    return store


def authoritative_view(global_connections=None, index=None):
    """Fresh normalized graph, never a union with a previous consumer view."""
    index = load_index() if index is None else index
    resolve = build_slug_resolver(p["slug"] for p in index)
    raw = load_global_connections() if global_connections is None else global_connections
    bidi = make_bidirectional_deduped(raw, resolve=resolve)
    if not index:
        bidi = {}
    for paper in index:
        bidi.setdefault(paper["slug"], [])
    st = resolve.stats
    print(f"  normalized: {len(st['remapped'])} remapped (renumbered), "
          f"{len(st['pruned'])} pruned (deleted/ambiguous)")
    return bidi


def rebuild_data(topics, dry_run=False, *, index=None, global_connections=None,
                 previous_sources=None, connections=None):
    """Rebuild each topic's _paper_connections.json from the global store.

    Returns old and new source keys, including explicit processed-empty papers,
    so pages and markdown also lose connections removed by this rebuild.
    """
    if index is None or previous_sources is None:
        plan = plan_rebuild(topics)
        index = plan["index"] if index is None else index
        previous_sources = plan["previous_sources"] if previous_sources is None else previous_sources
        if global_connections is None:
            global_connections = plan["global_connections"]
    bidi = authoritative_view(global_connections, index) if connections is None else connections
    slug_map = topic_slug_map(index)
    source_keys = set(previous_sources)
    outputs = {}
    for topic in topics:
        directory = topic_path(topic)
        out = bidi if topic == "_cross" else filter_for_topic(bidi, slug_map.get(topic, ()))
        outputs[topic] = (directory, out)
        source_keys.update(out)
    for topic, (directory, out) in outputs.items():
        n_links = sum(len(v) for v in out.values())
        fp = directory / "_paper_connections.json"
        if dry_run:
            print(f"  [dry-run] {topic}: would write {len(out)} papers, {n_links} links")
        else:
            atomic_write_json(fp, out)
            print(f"  {topic}: {len(out)} papers, {n_links} links -> {fp}")
    return source_keys


def render_pages(source_keys, dry_run=False, *, connections=None):
    """Re-render every page that is a connection source (has a review.md)."""
    slugs = sorted(s for s in source_keys if (validate_paper_files(s) / "review.md").is_file())
    if dry_run:
        print(f"  [dry-run] would re-render {len(slugs)} pages")
        return
    if not slugs:
        return {"converted": 0, "skipped": 0}
    import review_to_html
    connections = authoritative_view() if connections is None else connections
    # Removed sources must explicitly override any old topic/cache entry too.
    review_to_html._connections_cache = {s: connections.get(s, [])
                                         for s in set(connections) | set(source_keys)}
    print(f"  re-rendering {len(slugs)} pages ...")
    rendered = review_to_html._run_review_to_html(slugs=slugs, with_connected=False)
    if not isinstance(rendered, dict) or rendered.get("converted") != len(slugs) or rendered.get("skipped"):
        raise RuntimeError("connection pages did not render completely")
    return rendered


def inject_related(topics, source_keys, dry_run=False, *, connections=None):
    """Refresh only the "## Related Papers" markdown block in each review.md.

    This is the block paper-curio's reviewHtml.ts and Obsidian render (paper-
    curation's own web pages strip it and use the connections-box instead). We
    swap *only* that section so frontmatter and body stay byte-identical — never
    routed through inject_into_review, which would also rewrite the frontmatter.
    """
    import re as _re
    slugs = sorted(s for s in source_keys if (validate_paper_files(s) / "review.md").is_file())
    if dry_run:
        print(f"  [dry-run] would refresh ## Related Papers in {len(slugs)} review.md")
        return
    from inject_frontmatter import build_related_section

    conns = authoritative_view() if connections is None else connections
    pat = _re.compile(r"\n## Related Papers\n[\s\S]*?(?=\n## |\Z)")
    changed = 0
    for s in slugs:
        md_path = os.path.join(PAPERS, s, "review.md")
        with open(md_path, encoding="utf-8") as f:
            content = f.read()
        section = build_related_section(s, conns)  # "\n## Related Papers\n...\n" or ""
        new = pat.sub("", content).rstrip()
        if section:
            new += "\n" + section
        new += "\n" if not new.endswith("\n") else ""
        if new != content:
            atomic_write_text(md_path, new)
            changed += 1
    print(f"  refreshed ## Related Papers in {changed}/{len(slugs)} review.md")


def regen_networks(topics, dry_run=False):
    """Regenerate each topic's D3 network (undirected dedup of bidi edges)."""
    script = os.path.join(_HERE, "generate_network.py")
    for topic in topics:
        topic_path(topic)
        if dry_run:
            print(f"  [dry-run] would regenerate network: {topic}")
            continue
        r = subprocess.run([sys.executable, script, "--topic", topic],
                           capture_output=True, text=True)
        tail = (r.stdout or r.stderr).strip().splitlines()[-1:] or [""]
        if r.returncode != 0:
            raise RuntimeError(f"network {topic} failed ({r.returncode}): "
                               f"{(r.stderr or r.stdout).strip()}")
        print(f"  network {topic}: OK — {tail[0]}")


def sync_existing_database():
    """Refresh the optional DB only after the full rebuild has succeeded."""
    from sync_paper_connections import DEFAULT_DB, import_connections
    if not Path(DEFAULT_DB).is_file():
        print("  bibliography DB absent: skipped")
        return None
    result = import_connections(DEFAULT_DB)
    print(f"  bibliography DB: {result['imported']} connections imported")
    return result


def run_rebuild(topics=None, *, recompute=False, dry_run=False, no_render=False,
                no_inject=False, no_networks=False):
    """Own the mutation lease before taking any snapshot; plans never lock/write."""
    if recompute and topics is not None:
        raise ValueError("--recompute replaces the whole global store; do not combine it with --topics")
    kwargs = dict(recompute=recompute, dry_run=dry_run, no_render=no_render,
                  no_inject=no_inject, no_networks=no_networks)
    if dry_run:
        return _run_rebuild(topics, **kwargs)
    safe_path(DOCS, PAPERS)
    with corpus_operation_lock(PAPERS, exclusive=True):
        return _run_rebuild(topics, **kwargs)


def _run_rebuild(topics, *, recompute, dry_run, no_render, no_inject, no_networks):
    full_rebuild = topics is None
    plan = plan_rebuild(topics, recompute=recompute)
    topics = plan["topics"]
    index = plan["index"]
    store = plan["global_connections"]
    print(f"Topics: {', '.join(topics)}")
    if recompute:
        print("[0/4] Recomputing neighbours in SPECTER2 embedding space...")
        computed = recompute_global([t for t in topics if t != "_cross"],
                                    dry_run=dry_run, index=index)
        if not dry_run:
            store = computed
        else:
            print("  [dry-run] view/link counts use the current graph; no neighbours are calculated")

    print("[1/4] Rebuilding topic connection files (bidirectional + deduped)...")
    view = authoritative_view(store, index)
    source_keys = rebuild_data(topics, dry_run=dry_run, index=index,
                               global_connections=store,
                               previous_sources=plan["previous_sources"], connections=view)
    if full_rebuild:
        source_keys.update(p["slug"] for p in index)

    if no_render:
        print("[2/4] Page re-render: skipped (--no-render)")
    else:
        print("[2/4] Re-rendering paper pages (equal reason badges + linked [NNN] refs)...")
        render_pages(source_keys, dry_run=dry_run, connections=view)

    if no_inject:
        print("[3/4] ## Related Papers refresh: skipped (--no-inject)")
    else:
        print("[3/4] Refreshing ## Related Papers in review.md (paper-curio/Obsidian)...")
        inject_related(topics, source_keys, dry_run=dry_run, connections=view)

    if no_networks:
        print("[4/4] Network regeneration: skipped (--no-networks)")
    else:
        print("[4/4] Regenerating networks...")
        regen_networks(topics, dry_run=dry_run)

    database = sync_existing_database() if full_rebuild and not dry_run else None
    print("DONE" + (" (dry-run)" if dry_run else ""))
    return {"topics": topics, "source_keys": source_keys, "database": database}


def main():
    ap = argparse.ArgumentParser(description="Rebuild bidirectional connection view + re-render")
    ap.add_argument("--topics", nargs="+", default=None,
                    help="Topic dirs to rebuild (default: all index memberships and existing connection views)")
    ap.add_argument("--no-render", action="store_true", help="Skip page re-rendering")
    ap.add_argument("--no-inject", action="store_true",
                    help="Skip refreshing the ## Related Papers block in review.md (paper-curio/Obsidian)")
    ap.add_argument("--no-networks", action="store_true", help="Skip network regeneration")
    ap.add_argument("--recompute", action="store_true",
                    help="Recompute all neighbours in embedding space and replace the global store")
    ap.add_argument("--dry-run", action="store_true", help="Report only; write nothing")
    args = ap.parse_args()

    if args.recompute and args.topics:
        ap.error("--recompute replaces the whole global store; do not combine it with --topics")
    return run_rebuild(args.topics, recompute=args.recompute, dry_run=args.dry_run,
                       no_render=args.no_render, no_inject=args.no_inject,
                       no_networks=args.no_networks)


if __name__ == "__main__":
    main()
