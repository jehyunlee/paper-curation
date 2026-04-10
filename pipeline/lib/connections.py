"""
Global paper connections management.

All topics share a single global connections file (docs/papers/_global_connections.json).
Topic-specific _paper_connections.json files are derived from global by filtering.

This ensures cross-topic connections are preserved regardless of execution order.
"""

import json
import os

PAPERS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "docs", "papers")
GLOBAL_CONN_PATH = os.path.join(PAPERS_DIR, "_global_connections.json")


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
    # Merge into global
    global_conns = merge_to_global(new_connections, source_topic=topic)
    global_total = sum(len(v) for v in global_conns.values())
    log(f"  Global connections: {len(global_conns)} papers, {global_total} total links")

    # Filter for this topic
    topic_conns = filter_for_topic(global_conns, topic_slugs)
    topic_total = sum(len(v) for v in topic_conns.values())

    # Save topic file
    conn_path = os.path.join(topic_dir, "_paper_connections.json")
    with open(conn_path, "w", encoding="utf-8") as f:
        json.dump(topic_conns, f, ensure_ascii=False, indent=2)
    log(f"  Topic connections: {len(topic_conns)} papers, {topic_total} links → {conn_path}")

    return topic_conns
