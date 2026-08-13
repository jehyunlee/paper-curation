#!/usr/bin/env python3
"""Verify that a parser change did not un-resolve papers it used to resolve.

    python pipeline/check_attribution_regression.py --snapshot
    …change a parser…
    python pipeline/check_attribution_regression.py --compare

Widening a byline parser to reach a new layout can narrow it elsewhere. It has
already happened twice here: anchoring on author surnames fixed the spaced and
comma layouts and broke every glued one — 200 of 200 papers stopped resolving —
and stopping a stacked block at the author's e-mail read one template correctly
while hiding the affiliation in the template that prints the e-mail first.

A count going up hides that: 40 newly resolved papers and 40 newly broken ones
look like no change at all. So the snapshot is per paper, and the comparison
reports the two directions separately. Papers, not totals, are the unit.

The snapshot lives in `.cache/attribution_snapshot.json` and holds, for every
paper, which evidence class resolved it. `--compare` exits 2 when any paper
that used to resolve no longer does.
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

import build_bibliography_db as bib            # noqa: E402

PAPERS_DIR = ROOT / "docs" / "papers"
DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"
SNAPSHOT = ROOT / ".cache" / "attribution_snapshot.json"


def resolve_one(conn: sqlite3.Connection, paper_id: int,
                slug: str) -> str | None:
    """Which parser resolves this paper right now, using live code.

    Deliberately re-derived rather than read from `paper_author_institutions`:
    the stored rows are the output of whatever the parsers were when the
    backfill last ran, so comparing them would compare backfills, not parsers.
    """
    text = PAPERS_DIR / slug / "text.md"
    if not text.exists():
        return None
    authors = [row[0] for row in conn.execute(
        "SELECT a.display_name FROM paper_authors pa JOIN authors a"
        " USING(author_id) WHERE pa.paper_id=? ORDER BY pa.author_order",
        (paper_id,))]
    if not authors:
        return None
    institutions = conn.execute(
        "SELECT institution_id, raw_name FROM paper_institutions"
        " WHERE paper_id=?", (paper_id,)).fetchall()
    if not institutions:
        return None
    if len(institutions) == 1:
        return "sole-affiliation"
    if len(authors) == 1:
        # Every affiliation on a single-author paper is that author's.
        return "sole-author"

    header = bib.extract_header(text)[0]
    markers, alphabet = bib.read_byline_markers(header, authors, text)
    if markers:
        wanted = {m for values in markers.values() for m in values}
        block = (bib.marker_affiliations(header, wanted, alphabet)
                 or bib.marker_affiliations(
                     bib.affiliation_window(text), wanted, alphabet)
                 or bib.marker_affiliations(
                     bib.author_information_text(text), wanted, alphabet))
        if any(bib.best_institution_for(label, institutions)
               for label in block.values()):
            return "byline-marker"
    for name, parser in (("stacked-byline", bib.stacked_author_affiliations),
                         ("inline-affiliation", bib.inline_author_affiliations)):
        mapping = parser(header, authors)
        if any(bib.best_institution_for(value, institutions)
               for value in mapping.values()):
            return name
    named = bib.author_information_pairs(
        bib.author_information_text(text), authors)
    if any(bib.best_institution_for(value, institutions)
           for value in named.values()):
        return "author-information"
    return None


def snapshot(db: Path) -> dict:
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    try:
        out = {}
        rows = conn.execute(
            "SELECT paper_id, slug FROM papers ORDER BY paper_id").fetchall()
        for index, (paper_id, slug) in enumerate(rows, 1):
            resolved = resolve_one(conn, paper_id, slug)
            if resolved:
                out[slug] = resolved
            if index % 500 == 0:
                print(f"  {index}/{len(rows)}", file=sys.stderr, flush=True)
    finally:
        conn.close()
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--snapshot", action="store_true",
                    help="record how every paper resolves today")
    ap.add_argument("--compare", action="store_true",
                    help="compare the current parsers against the snapshot")
    ap.add_argument("--limit", type=int, default=12)
    args = ap.parse_args()

    if args.snapshot:
        current = snapshot(args.db)
        SNAPSHOT.parent.mkdir(parents=True, exist_ok=True)
        SNAPSHOT.write_text(json.dumps(current, ensure_ascii=False, indent=1),
                            encoding="utf-8")
        print(json.dumps({"snapshot": str(SNAPSHOT), "resolved": len(current)},
                         ensure_ascii=False, indent=2))
        return 0

    if not args.compare:
        ap.error("--snapshot 또는 --compare 가 필요하다")
    if not SNAPSHOT.exists():
        print(f"기준 스냅샷이 없다: {SNAPSHOT}", file=sys.stderr)
        return 2

    before = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    after = snapshot(args.db)
    lost = sorted(set(before) - set(after))
    gained = sorted(set(after) - set(before))
    changed = sorted(slug for slug in set(before) & set(after)
                     if before[slug] != after[slug])
    report = {
        "before": len(before), "after": len(after),
        "regressed": len(lost), "gained": len(gained),
        "reclassified": len(changed),
        "regressed_papers": lost[:args.limit],
        "gained_papers": gained[:args.limit],
        "reclassified_papers": [
            {"slug": slug, "was": before[slug], "now": after[slug]}
            for slug in changed[:args.limit]],
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 2 if lost else 0


if __name__ == "__main__":
    raise SystemExit(main())
