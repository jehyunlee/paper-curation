"""
Global paper connections management.

All topics share a single global connections file (docs/papers/_global_connections.json).
Topic-specific _paper_connections.json files are derived from global by filtering.

This ensures cross-topic connections are preserved regardless of execution order.

The global file stores the *raw, directional* edges exactly as generated (one
``source_topic``-tagged entry per A→B). The per-topic ``_paper_connections.json``
files — which every renderer consumes — are derived as a **bidirectional,
per-target-deduped** view: each A→B edge implies B→A (relation flipped), and a
paper connected for several reasons appears once with all reasons listed. See
:func:`make_bidirectional_deduped`.
"""

import json
import os
from collections import OrderedDict

PAPERS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "docs", "papers")
GLOBAL_CONN_PATH = os.path.join(PAPERS_DIR, "_global_connections.json")

# When we synthesize the reverse edge B→A from a stored edge A→B, the relation
# must be re-expressed from B's point of view. The stored relation describes how
# the *target* relates to the *source* (A→B "foundation" means "B is a
# foundation for A"). Flipping the direction therefore flips the relation:
#   A→B foundation  ⇒  B→A extension   (A builds on / extends B)
#   A→B extension   ⇒  B→A foundation  (B is the basis A extends)
#   A→B application ⇒  B→A foundation  (B is the method A applies)
#   alternative / counterpoint are mutual ⇒ unchanged.
REVERSE_RELATION = {
    "foundation": "extension",
    "extension": "foundation",
    "application": "foundation",
    "alternative": "alternative",
    "counterpoint": "counterpoint",
    "related": "alternative",
}

# Canonical display/sort priority for relations (also used to pick the "primary"
# relation when one paper is connected for several reasons).
REL_ORDER = {"foundation": 0, "alternative": 1, "extension": 2,
             "application": 3, "counterpoint": 4}


def _normalize_relation(relation):
    return "alternative" if relation == "related" else relation


def _entry_reasons(entry):
    """Normalize a connection entry to reason dictionaries.

    Accepts both the new multi-reason schema (``reasons: [{relation, reason}]``)
    and the legacy single ``relation``/``reason`` fields.
    """
    rs = entry.get("reasons")
    if isinstance(rs, list) and rs:
        return [{**entry, **r, "relation": _normalize_relation(
            r.get("relation") or "alternative")} for r in rs]
    return [{**entry, "relation": _normalize_relation(
        entry.get("relation") or "alternative")}]


def _title_part(slug):
    """Slug minus its NNN_ sequence prefix — the part that is stable across
    renumbering. '1762_WoCoCo_Learning...' -> 'WoCoCo_Learning...'. No
    underscore -> returned as-is."""
    return slug.split("_", 1)[1] if "_" in slug else slug


def load_index_slugs():
    """Current valid slugs from _papers_index.json (empty set on any error)."""
    path = os.path.join(PAPERS_DIR, "_papers_index.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            return {p["slug"] for p in json.load(f) if p.get("slug")}
    except Exception:
        return set()


def build_slug_resolver(index_slugs):
    """Map a (possibly stale) connection slug to the CURRENT index slug.

    Papers keep their title but get re-assigned NNN sequence numbers over time, so
    a connection stored as '1762_WoCoCo_…' becomes an orphan once that paper is
    '1759_WoCoCo_…'. This remaps such an orphan to the current slug by its stable
    title-part, and drops slugs that no longer resolve — deleted (no title match)
    or ambiguous (title-part shared by 2+ current papers, can't safely pick).

    Returns a ``resolve(slug) -> slug | None`` callable carrying ``.stats`` =
    ``{'remapped': {old: new}, 'pruned': set()}``. With an EMPTY index the resolver
    is an identity that never prunes — a safety guard so a failed index load can't
    wipe the connection view.
    """
    index_slugs = set(index_slugs or ())
    stats = {"remapped": {}, "pruned": set()}
    if not index_slugs:
        def _ident(slug):
            return slug
        _ident.stats = stats
        return _ident

    by_tp = {}
    for s in index_slugs:
        by_tp.setdefault(_title_part(s), []).append(s)

    def resolve(slug):
        if not slug:
            return None
        if slug in index_slugs:
            return slug                      # already current
        cands = by_tp.get(_title_part(slug))
        if cands and len(cands) == 1:
            stats["remapped"][slug] = cands[0]
            return cands[0]                  # renumbered -> current slug
        stats["pruned"].add(slug)
        return None                          # deleted or ambiguous -> drop
    resolve.stats = stats
    return resolve


def make_bidirectional_deduped(conns_by_slug, resolve=None):
    """Return a bidirectional, per-target-deduped connections dict.

    For every directed edge A→B we also synthesize the reverse edge B→A (relation
    flipped via :data:`REVERSE_RELATION`). For each ordered pair we keep **one
    reason per relation** — so a paper connected several times under the *same*
    relation (e.g. a forward "foundation" edge plus a reverse "application" edge
    that flips back to "foundation") shows a single "기반 연구" line, while genuinely
    distinct relations (foundation + alternative) each get their own. Forward
    reasons (written from this paper's own perspective) win over reverse-derived
    ones. The top-level ``relation``/``reason`` mirror the highest-priority reason
    for consumers that read a single relation.
    """
    # buckets[src][tgt] = {relation: (payload, is_forward)} — one reason / relation
    buckets = {}

    def _add(src, tgt, payload, is_forward):
        if not src or not tgt or src == tgt:
            return
        rel = _normalize_relation(payload["relation"])
        payload = {key: payload.get(key, "") for key in
                   ("relation", "reason", "basis", "model", "evidence")}
        payload["relation"] = rel
        relmap = buckets.setdefault(src, OrderedDict()).setdefault(tgt, OrderedDict())
        cur = relmap.get(rel)
        # A content judgement is stronger than retrieval metadata; after that,
        # a source-perspective reason wins over a synthesized reverse.
        model = payload["basis"] == "model"
        if cur is None or (model, is_forward) > (cur[0]["basis"] == "model", cur[1]):
            relmap[rel] = (payload, is_forward)

    for src, conns in conns_by_slug.items():
        if resolve is not None:
            src = resolve(src)
            if src is None:                  # source paper deleted/ambiguous → drop its edges
                continue
        for entry in conns or []:
            tgt = entry.get("slug")
            if resolve is not None:
                tgt = resolve(tgt)
                if tgt is None:              # target deleted/ambiguous → drop this edge
                    continue
            for forward in _entry_reasons(entry):
                _add(src, tgt, forward, True)
                reverse = dict(forward)
                reverse["relation"] = _normalize_relation(
                    entry.get("reverse_relation") or
                    REVERSE_RELATION.get(forward["relation"], forward["relation"]))
                reverse["reason"] = (entry.get("reverse_reason") if
                                     entry.get("reverse_reason") is not None else
                                     forward.get("reason", ""))
                _add(tgt, src, reverse, False)

    result = {}
    for src, tgts in buckets.items():
        items = []
        for tgt, relmap in tgts.items():
            reasons = [dict(rr[0]) for rr in relmap.values()]
            reasons.sort(key=lambda r: REL_ORDER.get(r["relation"], 9))
            primary = reasons[0]
            items.append({
                "slug": tgt,
                "relation": primary["relation"],
                "reason": primary["reason"],
                "reasons": reasons,
                "basis": primary["basis"],
                "model": primary["model"],
                "evidence": primary["evidence"],
            })
        items.sort(key=lambda c: (REL_ORDER.get(c["relation"], 9), c["slug"]))
        result[src] = items
    return result


def load_global_connections():
    """Load global connections file. Returns empty dict if not found."""
    if os.path.exists(GLOBAL_CONN_PATH):
        with open(GLOBAL_CONN_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_global_connections(connections):
    """Save global connections file."""
    with open(GLOBAL_CONN_PATH, "w", encoding="utf-8") as f:
        json.dump(connections, f, ensure_ascii=False, indent=2)


def merge_to_global(new_connections, source_topic=None):
    """Merge new connections into global file. Returns merged global connections.

    For each slug, new connections are added alongside existing ones (dedup by target slug).
    If source_topic is given, existing connections from the SAME topic are replaced
    (prevents stale entries from prior runs of the same topic).
    """
    global_conns = load_global_connections()

    if source_topic:
        # Remove prior connections from this topic for slugs being updated
        for slug in new_connections:
            if slug in global_conns:
                global_conns[slug] = [
                    c for c in global_conns[slug]
                    if c.get("source_topic") != source_topic
                ]

    # Merge new connections
    for slug, conns in new_connections.items():
        existing = global_conns.get(slug, [])
        seen_targets = {c["slug"] for c in existing}
        for c in conns:
            if c["slug"] not in seen_targets:
                entry = dict(c)
                if source_topic:
                    entry["source_topic"] = source_topic
                existing.append(entry)
                seen_targets.add(c["slug"])
        global_conns[slug] = existing

    save_global_connections(global_conns)
    return global_conns


def filter_for_topic(global_conns, topic_slugs):
    """Filter global connections to those where source is in topic_slugs.

    Returns connections dict suitable for topic's _paper_connections.json.
    Connections to targets outside the topic are kept (generate_network filters them).
    """
    topic_set = set(topic_slugs)
    filtered = {}
    for slug, conns in global_conns.items():
        if slug in topic_set:
            # Strip source_topic from output (internal field)
            filtered[slug] = [
                {k: v for k, v in c.items() if k != "source_topic"}
                for c in conns
            ]
    return filtered


def sync_topic_connections(new_connections, topic, topic_slugs, topic_dir, log=print):
    """Full workflow: merge to global → filter for topic → save topic file.

    Args:
        new_connections: newly computed connections dict {slug: [{slug, relation, reason}]}
        topic: topic name (e.g. "ai4s", "scisci")
        topic_slugs: list of slugs belonging to this topic
        topic_dir: path to topic directory (e.g. docs/ai4s/)
        log: logging function
    """
    # Merge into global (raw directional store)
    global_conns = merge_to_global(new_connections, source_topic=topic)
    global_total = sum(len(v) for v in global_conns.values())
    log(f"  Global connections: {len(global_conns)} papers, {global_total} total links")

    # Derive the bidirectional + per-target-deduped view, then filter for topic.
    # Self-heal renumbered connection endpoints to current slugs (and prune
    # deleted/ambiguous ones) so the consumer view never shows orphan slug-titles.
    _resolve = build_slug_resolver(load_index_slugs())
    bidi_conns = make_bidirectional_deduped(global_conns, resolve=_resolve)
    _st = _resolve.stats
    if _st["remapped"] or _st["pruned"]:
        log(f"  Connections normalized: {len(_st['remapped'])} remapped (renumbered), "
            f"{len(_st['pruned'])} pruned (deleted/ambiguous)")
    topic_conns = filter_for_topic(bidi_conns, topic_slugs)
    topic_total = sum(len(v) for v in topic_conns.values())

    # Save topic file
    conn_path = os.path.join(topic_dir, "_paper_connections.json")
    with open(conn_path, "w", encoding="utf-8") as f:
        json.dump(topic_conns, f, ensure_ascii=False, indent=2)
    log(f"  Topic connections: {len(topic_conns)} papers, {topic_total} links → {conn_path}")

    return topic_conns
