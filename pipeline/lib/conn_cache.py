"""Incremental paper-connection cache (cost control for full-corpus regen).

The expensive path in the pipeline is the *full* connection generation that
paper-curio consumes for inbound/hub edges:
  - ``extract_insights.extract_paper_connections``  (top_k=25)
  - ``topic_modeling`` Step 6                        (top_k=5)

Both build a per-paper top-k candidate dict with
``compute_related_candidates`` (pure numpy, cheap) and then call
``generate_connections_from_candidates`` which fires **one LLM call per key**
in that dict. So the cost is proportional to ``len(candidates)``.

This module lets the integration layer restrict that candidate dict to only the
papers whose connections can actually have changed since the last run — the
*dirty* set — while still saving the FULL current top-k membership so the next
diff is correct.

THE HUB TRAP (why "new-only" is wrong, and how this fixes it):
  When a new paper N is added, an *old* paper O may now have N inside its top-k
  (pushing out O's former #k neighbor). For N to receive its inbound link, O→N
  must be (re)generated. A naive "only the new slug" diff misses O silently and
  the graph quietly thins out. The fix here is the **membership-changed** rule:
  a slug is dirty if its current top-k SET differs from the cached one — this
  covers both gained AND lost candidates, closing the hub trap.

Downstream, ``lib.connections.sync_topic_connections`` only rewrites edges for
slugs present in the dict it is handed (``merge_to_global`` leaves everyone else
untouched) and then ``make_bidirectional_deduped`` synthesizes reverse/inbound
edges for the whole global store for free. So passing only the dirty slugs is
safe: unchanged papers keep their prior edges, and the new inbound links are
materialized at no extra LLM cost.

SAFETY: the diff is wrapped so that ANY error returns the FULL candidate set
(correct but costly) — never a silently-thin graph. The integration layer also
exposes ``CONN_INCREMENTAL`` / ``CONN_FULL_REBUILD`` toggles; this module stays
toggle-agnostic and just takes a ``force`` flag.

Import-light on purpose: stdlib only (no umap/hdbscan/sentence-transformers),
so the integration points pay nothing to import it.
"""

import json
import os


def topk_sets(candidates):
    """``{slug: [(target, score), ...]}`` → ``{slug: sorted([target, ...])}``.

    Drops the cosine scores and keeps only top-k *membership* (a sorted list of
    target slugs). Membership — not score — is what determines whether a paper's
    set of LLM-judged candidates changed, so this is the unit the diff compares.
    Tolerates plain-string candidate lists as well as ``(target, score)`` pairs.
    """
    out = {}
    for slug, cands in (candidates or {}).items():
        targets = []
        for c in cands or []:
            if isinstance(c, (tuple, list)):
                targets.append(c[0])
            else:
                targets.append(c)
        out[slug] = sorted(targets)
    return out


def cache_path(topic_dir, top_k, scope=""):
    """Cache path namespaced by ``scope`` and ``top_k``.

    Two different call sites must NEVER share a cache file even at the same
    ``top_k``: their candidate dicts have different bases (extract_insights saves
    target-restricted sets; topic_modeling saves full sets), so a shared file
    would make each run mark the other's papers membership-changed and mutually
    over-regenerate. ``scope`` ("ei" / "tm") keeps them apart; ``top_k`` keeps a
    k=5 run from invalidating a k=25 run within one scope.
    """
    sc = f"_{scope}" if scope else ""
    return os.path.join(topic_dir, f"_conn_topk_cache{sc}_k{int(top_k)}.json")


def load_topk_cache(topic_dir, top_k, scope=""):
    """Load the top-k membership cache. Returns ``{}`` on any miss/error."""
    if not topic_dir:
        return {}
    path = cache_path(topic_dir, top_k, scope)
    try:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception:
        return {}
    return {}


def save_topk_cache(topic_dir, candidates, top_k, embed_model, scope="", sets=None,
                    empty=None):
    """Persist the top-k sets so the next diff is correct.

    Content: ``{"top_k": int, "embed_model": str|None, "sets": {slug: [targets]},
    "empty": [slug, ...]}``. ``empty`` lists papers the LLM processed and found
    NO connections for; without it the GAP rule re-billed them on every run.
    Atomic-ish (write tmp then ``os.replace``). Call this ONLY after a successful
    generate+sync — a failed run should be retried, not cached as done.

    Pass a precomputed ``sets`` (from :func:`next_cache_sets`) to keep the
    previous membership for dirty slugs that were not actually regenerated this
    run; otherwise the FULL current membership of ``candidates`` is saved.
    """
    path = cache_path(topic_dir, top_k, scope)
    data = {
        "top_k": int(top_k),
        "embed_model": embed_model,
        "sets": sets if sets is not None else topk_sets(candidates),
        "empty": sorted(set(empty or ())),
    }
    os.makedirs(topic_dir, exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)
    return path


def next_cache_sets(candidates, prev_cache, dirty, generated):
    """Top-k sets to persist after a (possibly partial) generation run.

    Advance the cached set to the CURRENT top-k for every slug EXCEPT a dirty
    slug we intended to regenerate but got NO result for this run (absent from
    ``generated`` — e.g. its batch was deadline-truncated). For those, KEEP the
    PREVIOUS cached set so the membership diff still flags them dirty next run and
    they are retried — instead of being silently cached as done, which would leave
    a hub/inbound edge missing until the next full rebuild. Non-dirty slugs and
    successfully-regenerated dirty slugs are advanced to the current membership.

    ``generated`` should be the slugs the generator actually returned a result
    for (its raw output keys, before any downstream verify/drop), so that a slug
    legitimately pruned by verification is treated as done, not retried forever.
    """
    cur = topk_sets(candidates)
    prev = (prev_cache or {}).get("sets") or {}
    dirty = set(dirty or [])
    generated = set(generated or [])
    # A scoped run (extract_insights --categories) hands in only the changed
    # categories' candidates. Papers outside that scope were not re-ranked, so
    # their previous membership must survive; dropping them made the next
    # run treat hundreds of untouched papers as NEW and pay Sonnet again.
    out = {slug: list(prev_set) for slug, prev_set in prev.items() if slug not in cur}
    for slug, cur_set in cur.items():
        if slug in dirty and slug not in generated:
            # Intended to regenerate but got no result (deadline-truncated/skipped).
            if slug in prev:
                out[slug] = list(prev[slug])   # keep prev → stays membership-dirty → retried
            # else NEW-and-not-generated: OMIT entirely → treated NEW next run → dirty
            # (don't rely solely on the GAP rule, which a stray edge could mask).
            continue
        out[slug] = cur_set                    # non-dirty, or dirty-and-regenerated → advance
    return out


def next_empty_slugs(prev_cache, dirty, generated, connections):
    """Papers the LLM processed and found no connections for.

    Carries the previous record forward for papers not regenerated this run,
    adds this run's processed-but-empty papers, and drops any paper that now
    has connections. Persisted as ``empty`` so :func:`compute_dirty` stops
    re-sending a legitimately isolated paper on every run.
    """
    prev_empty = set((prev_cache or {}).get("empty") or [])
    dirty = set(dirty or [])
    generated = set(generated or [])
    connections = connections or {}
    carried = {s for s in prev_empty if s not in dirty}
    fresh = {s for s in generated if not connections.get(s)}
    return sorted((carried | fresh) - {s for s in generated if connections.get(s)})


def compute_dirty(candidates, prev_cache, existing_conns, top_k, embed_model,
                  *, force=False, log=print):
    """Return ``(dirty_slugs:set, reason:str)`` — the papers needing an LLM call.

    FULL regen (dirty = ALL candidate keys) when:
      * ``force`` is True (caller toggle: CONN_FULL_REBUILD or CONN_INCREMENTAL off);
      * ``prev_cache`` is empty/missing (first run, or cache was cleared);
      * ``prev_cache["top_k"]`` != ``top_k`` (different k — sets not comparable);
      * ``prev_cache["embed_model"]`` != ``embed_model`` (embedding geometry
        changed → cosine neighbours, hence reasons, may shift everywhere).

    Otherwise INCREMENTAL — dirty is the union of:
      (a) slugs absent from the previous sets                         (NEW);
      (b) slugs whose current top-k set != the previous set
          (MEMBERSHIP CHANGED — closes the hub trap, covers gained & lost);
      (c) slugs with no existing connections in ``existing_conns``
          (GAP safety — bridge-deferred / previously-failed papers), unless the
          cache records them in ``empty`` (processed, legitimately isolated).

    Any exception inside the diff returns ``(all_keys, "error-fallback:...")``:
    the safe failure direction is FULL regen (correct but costly), never a
    silently-thin graph.
    """
    all_keys = set((candidates or {}).keys())
    try:
        if force:
            return set(all_keys), "force"
        if not prev_cache:
            return set(all_keys), "no-prev-cache"
        prev_k = prev_cache.get("top_k")
        if prev_k != top_k:
            return set(all_keys), f"top_k-changed:{prev_k}->{top_k}"
        prev_model = prev_cache.get("embed_model")
        if prev_model != embed_model:
            return (set(all_keys),
                    f"embed_model-changed:{prev_model!r}->{embed_model!r}")

        prev_sets = prev_cache.get("sets") or {}
        prev_empty = set(prev_cache.get("empty") or [])
        cur_sets = topk_sets(candidates)
        existing_conns = existing_conns or {}

        dirty = set()
        for slug, cur in cur_sets.items():
            prev = prev_sets.get(slug)
            if prev is None:
                dirty.add(slug)            # (a) NEW
                continue
            if list(prev) != list(cur):
                dirty.add(slug)            # (b) MEMBERSHIP CHANGED (hub trap)
                continue
            if not existing_conns.get(slug) and slug not in prev_empty:
                dirty.add(slug)            # (c) GAP safety (unless known-empty)
        return dirty, "incremental"
    except Exception as e:  # safe direction: full regen, never a thin graph
        log(f"  [conn] dirty computation error -> FULL fallback: {str(e)[:120]}")
        return set(all_keys), f"error-fallback:{str(e)[:80]}"


def restrict_candidates(candidates, dirty):
    """``{s: candidates[s] for s in dirty if s in candidates}`` — the dict that
    drives generation, narrowed to dirty keys only (so only they get an LLM call)."""
    return {s: candidates[s] for s in dirty if s in candidates}
