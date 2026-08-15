#!/usr/bin/env python3
"""Rebuild the whole corpus's bibliography, in the right order, and prove it.

This exists because doing it by hand went wrong six times in one sitting, and
every one of those was a mistake a script cannot make twice:

- the ingest was run without the backfill that follows it, so 4,196 papers
  were re-derived by the ingest's own weak classifier and coverage read 88.3%
  to 81.0%. The eight byline parsers live in `backfill_author_institutions`,
  not in the ingest; the ingest alone is half the job.
- `--slugs` takes prefixes, so a list containing `1001` also rebuilt `10010`
  through `10019`.
- `--offline` was passed to a run whose whole point was to fetch deposits.
- a 40-paper trial was judged on corpus totals, where 40 papers cannot move
  the number, instead of per paper.

So the order is fixed here, the safety checks run every time, and a run that
would leave any paper worse off stops and restores.

Usage:
    python pipeline/rebuild_corpus.py --dry-run
    python pipeline/rebuild_corpus.py --sample 60      # per-paper trial first
    python pipeline/rebuild_corpus.py --execute
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import shutil
import sqlite3
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "pipeline"
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import build_bibliography_db as bib                            # noqa: E402
from lib.evidence import RESOLVED_SOURCES                      # noqa: E402

DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"
BACKUP_DIR = ROOT / ".cache" / "backups"


def snapshot(db: Path) -> dict:
    """Per-paper state, because totals hide a paper that got worse."""
    marks = ",".join("?" * len(RESOLVED_SOURCES))
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    try:
        links = {slug: n for slug, n in conn.execute(
            f"SELECT p.slug, COUNT(DISTINCT x.author_id || '/' || "
            f"x.institution_id) FROM paper_author_institutions x"
            f" JOIN papers p USING(paper_id)"
            f" WHERE x.source IN ({marks}) GROUP BY 1", RESOLVED_SOURCES)}
        institutions = {slug: n for slug, n in conn.execute(
            "SELECT p.slug, COUNT(*) FROM paper_institutions pi"
            " JOIN papers p USING(paper_id) GROUP BY 1")}
        by_source = dict(conn.execute(
            "SELECT source, COUNT(DISTINCT paper_id)"
            " FROM paper_author_institutions GROUP BY 1"))
        totals = {
            "papers": conn.execute(
                "SELECT COUNT(*) FROM papers").fetchone()[0],
            "resolved": len(links),
            "links": sum(links.values()),
            "institutions": conn.execute(
                "SELECT COUNT(*) FROM institutions").fetchone()[0],
            "authors": conn.execute(
                "SELECT COUNT(*) FROM authors").fetchone()[0],
        }
        return {"links": links, "institutions": institutions,
                "by_source": by_source, "totals": totals}
    finally:
        conn.close()


def compare(before: dict, after: dict) -> dict:
    """What got worse, named. A net gain is not evidence that nothing broke."""
    lost_resolution = sorted(
        slug for slug in before["links"] if slug not in after["links"])
    fewer_links = sorted(
        (slug, before["links"][slug], after["links"].get(slug, 0))
        for slug in before["links"]
        if after["links"].get(slug, 0) < before["links"][slug])
    fewer_institutions = sorted(
        (slug, before["institutions"][slug], after["institutions"].get(slug, 0))
        for slug in before["institutions"]
        if after["institutions"].get(slug, 0) < before["institutions"][slug])
    return {
        "lost_resolution": lost_resolution,
        "papers_with_fewer_links": len(fewer_links),
        "papers_with_fewer_institutions": len(fewer_institutions),
        "examples": {
            "fewer_links": fewer_links[:5],
            "fewer_institutions": fewer_institutions[:5],
        },
        "totals_before": before["totals"],
        "totals_after": after["totals"],
        "by_source_before": before["by_source"],
        "by_source_after": after["by_source"],
    }


def removed_links(db: Path, before_db: Path, slugs: list[str]) -> list[dict]:
    """For each link a rebuild removed, whether the paper still supports it.

    A rebuild dropping a link is not automatically a regression. Some links
    were wrong: `041_Aaar-10` recorded a single author because the source read
    "Renze Lou et al.", and the sole-author rule handed that one person all
    six of the paper's institutions. Removing five of those is a correction.

    So the test is the one used everywhere else -- does the paper's own front
    matter carry the institution's distinctive tokens. A removed link the page
    still supports is a real loss and stops the run; one the page never
    supported is the parser correcting itself.
    """
    marks = ",".join("?" * len(RESOLVED_SOURCES))
    old = sqlite3.connect(f"file:{before_db}?mode=ro", uri=True)
    new = sqlite3.connect(f"file:{db}?mode=ro", uri=True)

    def links(conn, slug):
        return {(a, i) for a, i in conn.execute(
            f"SELECT x.author_id, x.institution_id"
            f" FROM paper_author_institutions x JOIN papers p USING(paper_id)"
            f" WHERE p.slug=? AND x.source IN ({marks})",
            (slug, *RESOLVED_SOURCES))}

    out: list[dict] = []
    try:
        for slug in slugs:
            gone = links(old, slug) - links(new, slug)
            if not gone:
                continue
            window = bib._fold(bib.affiliation_window(
                ROOT / "docs" / "papers" / slug / "text.md"))
            for _author_id, institution_id in gone:
                row = old.execute(
                    "SELECT institution_name FROM institutions"
                    " WHERE institution_id=?", (institution_id,)).fetchone()
                name = row[0] if row else ""
                tokens = [t for t in bib._affiliation_tokens(name)
                          if len(t) >= 5][:3]
                out.append({
                    "slug": slug, "institution": name,
                    "supported": bool(tokens) and all(t in window
                                                      for t in tokens)})
    finally:
        old.close()
        new.close()
    return out


def run(db: Path, slugs: list[str] | None) -> None:
    """Ingest, then backfill, then finalize. Never one without the next.

    The ingest classifies with its own fallback and writes
    `pdf.unmarked-multi` wherever the byline defeats it; the backfill is where
    the marker, stacked, shared and sole-author parsers live and it retries
    exactly those papers. Running the ingest alone does not half-finish the
    job, it undoes the parsers' work.

    The ingest is a subprocess because it lives inside the module's `main`.
    What matters is that the sequence, and the checks around it, are written
    down here instead of being typed out again each time.
    """
    command = [sys.executable, str(PIPELINE / "build_bibliography_db.py"),
               "--no-email"]
    if slugs:
        # Full slugs, never numeric prefixes: `--slugs 1001` also matches
        # 10010 through 10019, which is how a 415-paper run became a
        # 500-paper one.
        command += ["--slugs", ",".join(slugs)]
    else:
        command += ["--all"]
    print("[1/3] ingest", flush=True)
    completed = subprocess.run(
        command, cwd=str(ROOT),
        env={**os.environ, "PAPER_CURATION_BIBLIO_DB": str(db)})
    if completed.returncode != 0:
        raise SystemExit(f"ingest failed: exit {completed.returncode}")
    print("[2/3] backfill (byline parsers)", flush=True)
    print(json.dumps(bib.backfill_author_institutions(db), ensure_ascii=False),
          flush=True)
    print("[3/3] finalize", flush=True)
    print(json.dumps(bib.finalize(db), ensure_ascii=False), flush=True)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--sample", type=int,
                    help="rebuild this many papers and report per-paper "
                         "deltas without touching the rest")
    ap.add_argument("--execute", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--allow-regression", action="store_true",
                    help="keep the result even if papers got worse")
    ap.add_argument("--report", type=Path,
                    default=ROOT / "reports" / "build" / "rebuild_corpus.json")
    args = ap.parse_args()

    if not args.db.exists():
        print(f"no database at {args.db}", file=sys.stderr)
        return 1
    if not (args.execute or args.dry_run):
        ap.error("--execute 또는 --dry-run 중 하나가 필요하다")

    slugs = None
    if args.sample:
        conn = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True)
        slugs = [row[0] for row in conn.execute(
            "SELECT slug FROM papers ORDER BY paper_id LIMIT ?",
            (args.sample,))]
        conn.close()

    if args.dry_run:
        print(json.dumps({
            "db": str(args.db), "papers": len(slugs) if slugs else "all",
            "steps": ["ingest", "backfill_author_institutions", "finalize"],
        }, ensure_ascii=False, indent=2))
        return 0

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = BACKUP_DIR / f"bibliography_pre_rebuild_{stamp}.sqlite3"
    shutil.copy2(args.db, backup)
    print(f"backup {backup.name}", flush=True)

    before = snapshot(args.db)
    started = time.time()
    run(args.db, slugs)
    after = snapshot(args.db)
    result = compare(before, after)
    shrunk = [slug for slug in before["links"]
              if after["links"].get(slug, 0) < before["links"][slug]]
    result["removed_links"] = removed_links(args.db, backup, shrunk)
    result["removed_supported"] = sum(
        1 for row in result["removed_links"] if row["supported"])
    result["removed_unsupported"] = (
        len(result["removed_links"]) - result["removed_supported"])
    result["seconds"] = round(time.time() - started, 1)
    result["backup"] = str(backup)
    result["sample"] = len(slugs) if slugs else None

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2),
                           encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items()
                      if k != "examples"}, ensure_ascii=False, indent=2))

    # A dropped link only counts against the run when the paper still says it.
    # Counting every drop would block the rebuild for correcting itself, which
    # is most of what it does here.
    regressed = result["lost_resolution"] or result["removed_supported"]
    if regressed and not args.allow_regression:
        shutil.copy2(backup, args.db)
        print(f"\n{len(result['lost_resolution'])} papers lost resolution and "
              f"{result['removed_supported']} links the paper still supports "
              f"were removed; restored from {backup.name}. "
              f"Re-run with --allow-regression to keep it.",
              file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
