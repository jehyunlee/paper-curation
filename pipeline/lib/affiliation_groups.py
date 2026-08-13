"""Operator-curated parent groups, layered under ROR.

`dict_afgroupname_confident.json` is a hand-checked Scopus AF-ID table from the
KIER literature toolchain: 4,747 affiliations, each with the group it rolls up
to. 2,347 of them record a real hierarchy — "Dalian Institute of Chemical
Physics" under the Chinese Academy of Sciences, "Fraunhofer Institute for Solar
Energy Systems" under the Fraunhofer Society, "Harvard Medical School" under
Harvard University — and those are exactly the edges ROR is missing for this
corpus.

The retired affiliation registry imported the 4,747 AF-IDs from this file and
threw the group relationships away, which is why it produced 4,373 organisations
and zero relationships.

Two rules keep the table honest:

* An entry whose group normalises to the same key as the name is a *spelling
  variant*, not a hierarchy ("ETH Zurich" → "ETH Zürich", "The University of
  Melbourne" → "University of Melbourne"). ROR already handles those, and
  treating them as parents would make every institution its own parent.
* A group that names an administrative organ is refused, same as in ROR.

ROR wins where both have an answer; this table fills the gaps.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

from . import ror_index

ROOT = Path(__file__).resolve().parents[2]

# Three layers, most explicit first:
#   1. PAPER_CURATION_AFGROUP_DICT — the live copy on a machine that has one, so
#      operator edits take effect without a commit;
#   2. pipeline/data/ — the pinned baseline committed to the repository, which is
#      what lets a clean checkout reproduce the same parent groups;
#   3. .cache/affiliation/ — whatever `setup_affiliation_sources.py` staged.
# Without layer 2 a machine lacking the operator's Google Drive silently loses
# 1,872 curated hierarchies and no gate notices, because ROR still resolves.
PINNED_PATH = ROOT / "pipeline" / "data" / "dict_afgroupname_confident.json"
CACHED_PATH = ROOT / ".cache" / "affiliation" / "dict_afgroupname_confident.json"


def is_acronym_of(candidate: str, name: str) -> bool:
    """Is `candidate` just the institution's own initials?

    The curated table lists "Massachusetts Institute of Technology → MIT" and
    "The Hong Kong University of Science and Technology → HKUST". Those are the
    same organisation written short, not a parent group, and the plain
    normalised-key comparison cannot see it.
    """
    short = ror_index.normalize(candidate).replace(" ", "")
    words = ror_index.normalize(name).split()
    if not short or len(words) < 2 or " " in ror_index.normalize(candidate):
        return False
    return short == "".join(w[0] for w in words)


def curated_paths() -> list[Path]:
    """Candidate locations in precedence order."""
    return [Path(c) for c in (os.environ.get("PAPER_CURATION_AFGROUP_DICT", ""),
                              str(PINNED_PATH), str(CACHED_PATH)) if c]


def active_path() -> Path | None:
    """The copy actually in use, or None when no layer has the table."""
    return next((p for p in curated_paths() if p.is_file()), None)

_groups: dict[str, str] | None = None

# Research brands whose members ROR lists without a parent edge. Without this,
# each member becomes an umbrella over its own sibling institutes: ROR gives
# Helmholtz Munich and GSI a parent edge but not Helmholtz Institute Ulm, so Ulm
# collected its own Helmholtz bucket. The prefix is only applied when the name is
# not the association itself.
BRAND_ROLLUP = (
    ("helmholtz", "Helmholtz Association of German Research Centres"),
    ("fraunhofer", "Fraunhofer Society"),
    ("max planck", "Max Planck Society"),
    ("leibniz", "Leibniz Association"),
)


def load(path: Path | None = None) -> dict[str, str]:
    """normalized affiliation name → curated parent group display name."""
    global _groups
    if _groups is not None:
        return _groups
    source = path or active_path()
    if source is None:
        _groups = {}
        return _groups
    mapping: dict[str, str] = {}
    try:
        records = json.loads(source.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        _groups = {}
        return _groups
    index = ror_index.RorIndex()
    canonical: dict[str, str] = {}

    def as_ror_display(group: str) -> str:
        """Spell a group the way ROR does, so rollups do not split.

        The curated table says "Fraunhofer Society" where ROR says
        "Fraunhofer Society" as its English label; without this both spellings land in
        `parent_name` and the Fraunhofer institutes group into two piles.

        A ROR hit that merely *contains* the group's words is a more specific
        organisation, not a respelling: plural folding matches "Indian
        Institutes of Technology" (the system) against "Indian Institute of
        Technology BHU" (one campus), which would file every IIT under BHU.
        """
        if group not in canonical:
            display = group
            if index.available:
                hit = index.resolve(group)
                if hit:
                    want = set(ror_index.normalize(group).split())
                    got = set(ror_index.normalize(hit["display"]).split())
                    if not got > want:
                        display = hit["display"]
            canonical[group] = display
        return canonical[group]

    for record in records.values():
        if not isinstance(record, dict):
            continue
        group = next(iter(record.get("af_groupname") or []), "")
        if not group or ror_index.ADMINISTRATIVE_BODY.search(group):
            continue
        group = as_ror_display(group)
        group_key = ror_index.normalize(group)
        if not group_key:
            continue
        for name in record.get("af_name") or []:
            if is_acronym_of(group, name):
                continue
            for key in ror_index.alias_keys(name):
                if key and key != group_key:
                    mapping.setdefault(key, group)
    index.close()
    _groups = mapping
    return _groups


def brand_group_for(name: str) -> str:
    """Parent group implied by a controlled research brand, or ''.

    Matches the brand anywhere in the name, not only at the front: the GSI
    Helmholtz Centre for Heavy Ion Research carries the brand in the middle, and
    a prefix test left it standing as a second Helmholtz bucket.
    """
    key = ror_index.normalize(name)
    padded = f" {key} "
    for prefix, group in BRAND_ROLLUP:
        if f" {prefix}" in padded and key != ror_index.normalize(group):
            return group
    return ""


REGISTRY_PATH = Path(__file__).resolve().parents[1] / "data" / "institution_registry.json"
_registry: dict | None = None


def registry() -> dict:
    """Organisations ROR cannot settle: split brands, new bodies, non-bodies.

    ROR answers for the overwhelming majority and stays the authority. This
    covers the three things it does not: a multinational whose country records
    carry no parent edge (Nvidia, unlike Google), an organisation too new to
    have a record (Shanghai Innovation Institute, 2025), and a string that is
    not an organisation at all ("Independent Researcher", on 41 papers).
    """
    global _registry
    if _registry is not None:
        return _registry
    try:
        data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        data = {}
    # Keys are normalised on load, not by hand. `normalize` folds plurals —
    # "Complex Systems" becomes "complex system" — so a key typed the way the
    # institution is spelled would never match.
    _registry = {
        section: {ror_index.normalize(key): value
                  for key, value in (data.get(section) or {}).items()}
        for section in ("parent", "canonical", "exclude")}
    return _registry


def registry_group(name: str) -> str:
    """The group this registry puts a name under, or ''.

    Matched on the leading words so the country records come with it:
    "Nvidia (United Kingdom)" and "Nvidia (United States)" both start with
    nvidia and both belong under NVIDIA.
    """
    folded = ror_index.normalize(name or "")
    if not folded:
        return ""
    entries = registry()["parent"]
    for key, entry in entries.items():
        if folded == key or folded.startswith(key + " "):
            group = str(entry.get("group") or "")
            if group and ror_index.normalize(group) != folded:
                return group
    canonical = registry()["canonical"].get(folded)
    return str((canonical or {}).get("parent") or "")


def in_registry(name: str) -> bool:
    """Whether the registry has an opinion about this name.

    Distinct from `registry_group`, which returns nothing for the brand itself
    — "NVIDIA" is its own group and must not point at itself — but the name is
    still covered, and the audit needs to know that.
    """
    folded = ror_index.normalize(name or "")
    if not folded:
        return False
    if folded in registry()["canonical"] or folded in registry()["exclude"]:
        return True
    return any(folded == key or folded.startswith(key + " ")
               for key in registry()["parent"])


def registry_canonical(name: str) -> str:
    """The spelling this registry fixes for an organisation ROR lacks."""
    entry = registry()["canonical"].get(ror_index.normalize(name or ""))
    return str((entry or {}).get("name") or "")


def is_excluded(name: str) -> bool:
    """Whether the string names no organisation at all."""
    return ror_index.normalize(name or "") in registry()["exclude"]


def group_for(name: str) -> str:
    """Curated parent group for an institution name, or ''."""
    # The registry decides first: it exists precisely for the names the
    # curated table and ROR both leave ungrouped.
    from_registry = registry_group(name)
    if from_registry:
        return from_registry
    mapping = load()
    for key in ror_index.alias_keys(name):
        if key in mapping:
            return mapping[key]
    return brand_group_for(name)


def roll_up(parent: str, depth: int = 4) -> str:
    """Follow curated edges from a parent to the outermost group.

    ROR records no parent for the University of Chinese Academy of Sciences, so
    CAS institutes were being filed under UCAS. The curated table does know
    UCAS → CAS, so walking the parent itself through the table closes the gap.
    """
    current = parent
    for _ in range(depth):
        nxt = group_for(current)
        if not nxt or ror_index.normalize(nxt) == ror_index.normalize(current):
            break
        current = nxt
    return current


def stats() -> dict:
    mapping = load()
    source = active_path()
    return {"source": str(source) if source else None,
            "layers": [str(p) for p in curated_paths()],
            "entries": len(mapping),
            "groups": len(set(mapping.values()))}
