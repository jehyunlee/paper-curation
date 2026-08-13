#!/usr/bin/env python3
"""Which institution names ROR cannot settle, and what to do about each.

    python pipeline/audit_institution_names.py
    python pipeline/audit_institution_names.py --propose
    python pipeline/audit_institution_names.py --kind absent --limit 30

ROR resolves 89.6% of this corpus's institution links. The rest are not one
problem but three, and they need different answers:

  split     ROR holds the name under several country records and refuses to
            guess between them. "Nvidia" matches three. Google and Microsoft
            carry a parent edge between their country records and Nvidia does
            not, so the fix is a group, not a choice: both Nvidia records stay
            and rank together.

  absent    ROR has no record. Shanghai Innovation Institute (founded 2025),
            Zhongguancun Academy and Galbot are real and simply too new. The
            registry fixes one spelling so their counts do not split.

  dropped   Not an organisation. "Independent Researcher" carries 41 papers
            and says there is no affiliation.

`--propose` prints registry entries for what is not yet covered, ranked by
paper count, so the list grows where it matters instead of everywhere. It
prints; a person decides what to paste.

Read-only.
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "pipeline"
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

from lib import affiliation_groups, ror_index      # noqa: E402

DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"


def classify(name: str, index, names_db) -> tuple[str, int]:
    """Which of the three problems this name has, and how many ROR candidates."""
    if affiliation_groups.is_excluded(name):
        return "dropped", 0
    key = ror_index.normalize(name or "")
    matches = names_db.execute(
        "SELECT COUNT(DISTINCT ror_id) FROM names WHERE normalized=?",
        (key,)).fetchone()[0]
    if matches > 1:
        return "split", matches
    if matches == 1:
        return "resolvable", 1
    return "absent", 0


def covered(name: str) -> bool:
    """Whether the registry already says something about this name."""
    return affiliation_groups.in_registry(name)


def survey(db: Path) -> list[dict]:
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    index = ror_index.RorIndex()
    try:
        names_db = index._connect() if hasattr(index, "_connect") else None
        if names_db is None:
            names_db = sqlite3.connect(
                f"file:{ror_index.INDEX_PATH}?mode=ro", uri=True)
        rows = conn.execute(
            "SELECT i.institution_id, i.institution_name,"
            " COALESCE(i.country_name_en,''), COUNT(DISTINCT pi.paper_id)"
            " FROM institutions i JOIN paper_institutions pi"
            " USING(institution_id) WHERE COALESCE(i.ror_id,'')=''"
            " GROUP BY i.institution_id ORDER BY 4 DESC").fetchall()
        out = []
        for institution_id, name, country, papers in rows:
            kind, candidates = classify(name, index, names_db)
            out.append({"institution_id": institution_id, "name": name,
                        "country": country, "papers": papers, "kind": kind,
                        "ror_candidates": candidates,
                        "covered": covered(name)})
        return out
    finally:
        index.close()
        conn.close()


def propose(rows: list[dict], limit: int) -> dict:
    """Registry entries for what is not covered yet, worst first."""
    parent, canonical = {}, {}
    for row in rows:
        if row["covered"] or len(parent) + len(canonical) >= limit:
            continue
        key = ror_index.normalize(row["name"])
        if row["kind"] == "split":
            parent[key] = {"group": row["name"],
                           "note": f"ROR holds {row['ror_candidates']} country "
                                   f"records with no parent edge",
                           "seen": row["papers"]}
        elif row["kind"] == "absent":
            entry = {"name": row["name"], "note": "not in ROR",
                     "seen": row["papers"]}
            if row["country"]:
                entry["country"] = row["country"]
            canonical[key] = entry
    return {"parent": parent, "canonical": canonical}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--kind", choices=("split", "absent", "dropped",
                                       "resolvable"))
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--propose", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    rows = survey(args.db)
    if args.propose:
        print(json.dumps(propose(rows, args.limit), ensure_ascii=False,
                         indent=2))
        return 0
    if args.json:
        print(json.dumps(rows[:args.limit], ensure_ascii=False, indent=2))
        return 0

    total_links = sum(r["papers"] for r in rows)
    print(f"ROR 이 해결하지 못한 기관 {len(rows):,}곳 · 논문 링크 "
          f"{total_links:,}건\n")
    buckets: dict[str, list[dict]] = {}
    for row in rows:
        buckets.setdefault(row["kind"], []).append(row)
    for kind in ("split", "absent", "dropped", "resolvable"):
        group = buckets.get(kind) or []
        if not group:
            continue
        links = sum(r["papers"] for r in group)
        done = sum(1 for r in group if r["covered"])
        print(f"  {kind:11s} {len(group):5,}곳  링크 {links:6,}건  "
              f"명단 반영 {done}/{len(group)}")

    if args.kind:
        shown = [r for r in buckets.get(args.kind) or []][:args.limit]
        print(f"\n── {args.kind} 상위 {len(shown)}곳")
        for row in shown:
            mark = "✓" if row["covered"] else " "
            print(f"  {mark} {row['papers']:4d}편  {row['name'][:44]:44s}"
                  f"  후보 {row['ror_candidates']}  {row['country'][:16]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
