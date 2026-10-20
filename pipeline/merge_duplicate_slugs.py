"""Merge corpus slugs that are the same Zotero item registered twice.

One Zotero item can end up as two `docs/papers/<slug>/` directories when the
two topic syncs that saw it could not match them (no `zotero_item_key` in the
index, different title versions). `dedup_text.py` only handles slugs that share
a text.md; here the two slugs usually have their *own* extraction and review,
and live in *different* topics. Deleting one would silently drop a topic
membership, so this tool merges instead:

  1. keep.topics  := keep.topics + drop.topics (order preserved, primary kept)
  2. keep.zotero_item_key := the shared item key when keep has none
  3. drop is removed from the index, its directory, every topic's
     `_new_classification.json` / `_paper_connections.json` /
     `_embeddings_cache.json` / `_umap_coords.json`, and slug references in
     `_category_summaries.json` / `_insights.json` / `_timeline_narrative.json`
     are remapped to keep (`dedup_text.delete_slugs` + `redirect_references`
     do the index/dir/classification/connection/wiki-link part).
  4. the dropped directory is archived to `.cache/merge-backups/<ts>/`.

Afterwards the kept slug must be classified and connected in its new topics:
    python pipeline/run_feature.py --request '{"schema_version":1,"feature":"related-papers","params":{"slug":"<keep>"}}' --execute
then `build_bibliography_db.py --finalize` (drops the deleted rows) and
`build_topic_index.py <topic>` / `build_search_index.py --topic <topic>`.

Canonical choice (`choose_keep`) is deterministic and identity-based, not
quality-based: the slug Zotero's `extra` papercurio marker names, else the
slug whose index key is the item key, else the slug whose DOI is the item's
DOI, else the slug whose title matches the Zotero title, else more topics,
else higher score, else the lower prefix.

Usage:
  python pipeline/merge_duplicate_slugs.py --pairs 10911:10910,1005:9060
  python pipeline/merge_duplicate_slugs.py --pairs 10911:10910 --item-key IVXN2E5U --execute
"""
import argparse
import glob
import json
import os
import re
import shutil
import sys
import tarfile
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config_loader import PAPERS_DIR, DOCS_DIR, PROJECT_ROOT  # noqa: E402
from lib.atomic_io import atomic_write_json  # noqa: E402
from lib.doi import clean_doi  # noqa: E402
from dedup_text import delete_slugs, redirect_references  # noqa: E402

PAPERS = str(PAPERS_DIR)
DOCS = str(DOCS_DIR)
BACKUP_ROOT = PROJECT_ROOT / ".cache" / "merge-backups"
_SIDECARS_WITH_SLUG_REFS = ("_category_summaries.json", "_insights.json",
                            "_timeline_narrative.json")


def _norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def choose_keep(members, item):
    """Pick the canonical slug for one Zotero item. `members` are index rows."""
    marker = ""
    for line in str(item.get("extra") or "").splitlines():
        if line.lower().startswith("papercurio:"):
            marker = line.split(":", 1)[1].split(";")[0].strip()
    key = item.get("key", "")
    doi = clean_doi(item.get("DOI") or "").lower()
    title = _norm(item.get("title"))[:40]

    def rank(p):
        return (
            p["slug"] == marker,
            bool(key) and p.get("zotero_item_key") == key,
            bool(doi) and clean_doi(p.get("doi") or "").lower() == doi,
            bool(title) and _norm(p.get("title"))[:40] == title,
            len(p.get("topics") or []),
            float(p.get("score") or 0),
            -int(re.match(r"(\d+)_", p["slug"]).group(1)),
        )
    return max(members, key=rank)["slug"]


def _prefix(slug):
    return re.match(r"(\d+)_", slug).group(1)


def _remap_values(obj, mapping):
    """Replace exact slug strings anywhere in a JSON tree; dedupe lists."""
    if isinstance(obj, str):
        return mapping.get(obj, obj)
    if isinstance(obj, list):
        out, seen = [], set()
        for v in obj:
            nv = _remap_values(v, mapping)
            if isinstance(nv, str):
                if nv in seen:
                    continue  # keep and drop both listed -> one entry
                seen.add(nv)
            out.append(nv)
        return out
    if isinstance(obj, dict):
        return {mapping.get(k, k): _remap_values(v, mapping) for k, v in obj.items()}
    return obj


def _prune_topic_vectors(drop_slugs):
    """Remove dropped slugs from every topic's embedding cache and UMAP coords."""
    drop = set(drop_slugs)
    touched = []
    for topic_dir in sorted(glob.glob(os.path.join(DOCS, "*"))):
        if not os.path.isdir(topic_dir) or os.path.basename(topic_dir) == "papers":
            continue
        cache = os.path.join(topic_dir, "_embeddings_cache.json")
        if os.path.exists(cache):
            data = json.load(open(cache, encoding="utf-8"))
            slugs = data.get("slugs") or []
            keep_idx = [i for i, s in enumerate(slugs) if s not in drop]
            if len(keep_idx) != len(slugs):
                data["slugs"] = [slugs[i] for i in keep_idx]
                data["embeddings"] = [data["embeddings"][i] for i in keep_idx]
                if isinstance(data.get("originality_sha256"), dict):
                    for s in drop:
                        data["originality_sha256"].pop(s, None)
                tmp = cache + ".tmp"
                with open(tmp, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False)
                os.replace(tmp, cache)
                touched.append(cache)
        coords = os.path.join(topic_dir, "_umap_coords.json")
        if os.path.exists(coords):
            data = json.load(open(coords, encoding="utf-8"))
            if isinstance(data, dict) and any(s in data for s in drop):
                for s in drop:
                    data.pop(s, None)
                atomic_write_json(coords, data)
                touched.append(coords)
    return touched


def _remap_sidecars(mapping):
    touched = []
    for topic_dir in sorted(glob.glob(os.path.join(DOCS, "*"))):
        if not os.path.isdir(topic_dir) or os.path.basename(topic_dir) == "papers":
            continue
        for name in _SIDECARS_WITH_SLUG_REFS:
            path = os.path.join(topic_dir, name)
            if not os.path.exists(path):
                continue
            raw = open(path, encoding="utf-8").read()
            if not any(s in raw for s in mapping):
                continue
            data = _remap_values(json.loads(raw), mapping)
            atomic_write_json(path, data)
            touched.append(path)
    return touched


def _archive(slug, ts):
    BACKUP_ROOT.mkdir(parents=True, exist_ok=True)
    out = BACKUP_ROOT / ts / f"{slug}.tgz"
    out.parent.mkdir(parents=True, exist_ok=True)
    with tarfile.open(out, "w:gz") as tar:
        tar.add(os.path.join(PAPERS, slug), arcname=slug)
    return str(out)


def merge(pairs, *, item_keys=None, execute=False):
    """pairs: [(keep_prefix_or_slug, drop_prefix_or_slug)]. Returns a report."""
    item_keys = item_keys or {}
    idx = json.load(open(os.path.join(PAPERS, "_papers_index.json"), encoding="utf-8"))
    by_slug = {p["slug"]: p for p in idx}

    def _full(ref):
        if ref in by_slug:
            return ref
        hits = [s for s in by_slug if s.startswith(ref + "_")]
        if len(hits) != 1:
            raise SystemExit(f"ERROR: '{ref}' matches {len(hits)} slugs: {hits[:3]}")
        return hits[0]

    plan = []
    for keep_ref, drop_ref in pairs:
        keep, drop = _full(keep_ref), _full(drop_ref)
        if keep == drop:
            raise SystemExit(f"ERROR: keep and drop are the same slug: {keep}")
        k, d = by_slug[keep], by_slug[drop]
        new_topics = list(k.get("topics") or [])
        added = [t for t in (d.get("topics") or []) if t not in new_topics]
        new_topics += added
        key = item_keys.get(keep_ref) or item_keys.get(keep) or k.get("zotero_item_key") or d.get("zotero_item_key") or ""
        plan.append({"keep": keep, "drop": drop, "topics": new_topics, "added_topics": added,
                     "zotero_item_key": key, "drop_topics": list(d.get("topics") or [])})

    for p in plan:
        print(f"KEEP {p['keep']}\n  DROP {p['drop']}  (topics {p['drop_topics']})\n"
              f"  -> topics {p['topics']}  +{p['added_topics'] or '-'}  key={p['zotero_item_key'] or '-'}")
    if not execute:
        print(f"\nDRY-RUN: {len(plan)} merge(s). --execute to apply.")
        return {"plan": plan, "executed": False}

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    archives = [_archive(p["drop"], ts) for p in plan]

    from lib.corpus_store import corpus_operation_lock
    with corpus_operation_lock(PAPERS):
        idx = json.load(open(os.path.join(PAPERS, "_papers_index.json"), encoding="utf-8"))
        by_slug = {p["slug"]: p for p in idx}
        for p in plan:
            entry = by_slug[p["keep"]]
            entry["topics"] = p["topics"]
            if p["zotero_item_key"] and not entry.get("zotero_item_key"):
                entry["zotero_item_key"] = p["zotero_item_key"]
            tags = entry.get("tags")
            if isinstance(tags, list):
                for t in p["added_topics"]:
                    if t not in tags:
                        tags.append(t)
        drops = [p["drop"] for p in plan]
        new_idx = delete_slugs(drops, idx)
        atomic_write_json(os.path.join(PAPERS, "_papers_index.json"), new_idx)
        vec_touched = _prune_topic_vectors(drops)
        redirect = {_prefix(p["drop"]): p["keep"] for p in plan}
        changed = redirect_references(redirect, new_idx)
        side_touched = _remap_sidecars({p["drop"]: p["keep"] for p in plan})

    print(f"\nmerged {len(plan)}: archived {len(archives)} -> {BACKUP_ROOT / ts}")
    print(f"  vectors pruned in {len(vec_touched)} files; sidecars remapped in {len(side_touched)}; "
          f"{len(changed)} review.md redirected")
    print("Next: related-papers --execute for each kept slug, build_bibliography_db.py --finalize, "
          "build_topic_index / build_search_index for affected topics.")
    return {"plan": plan, "executed": True, "archives": archives, "redirected": sorted(changed),
            "affected_topics": sorted({t for p in plan for t in p["topics"] + p["drop_topics"]})}


def main():
    ap = argparse.ArgumentParser(description="Merge duplicate corpus slugs of one Zotero item")
    ap.add_argument("--pairs", required=True, help="keep:drop,keep:drop (slug prefixes or full slugs)")
    ap.add_argument("--item-key", action="append", default=[],
                    help="keep=ZOTEROKEY — set the kept slug's zotero_item_key (repeatable)")
    ap.add_argument("--execute", action="store_true", help="apply (default dry-run)")
    args = ap.parse_args()
    pairs = [tuple(x.split(":", 1)) for x in args.pairs.split(",") if x.strip()]
    keys = dict(x.split("=", 1) for x in args.item_key)
    merge(pairs, item_keys=keys, execute=args.execute)


if __name__ == "__main__":
    main()
