#!/usr/bin/env python3
"""Find the DOI of papers that reached the corpus without one.

    python pipeline/resolve_missing_dois.py --limit 50        # dry-run
    python pipeline/resolve_missing_dois.py --execute

Only 1,812 of 4,196 papers carry a DOI, and everything external hangs off it:
citation counts, OpenAlex authorships, the corresponding-author flag, ORCIDs.
2,384 papers are invisible to all of it — 975 hold an arXiv id and 1,409 hold
neither.

This searches OpenAlex and Crossref by title and accepts a match only on
evidence, because a title search is exactly what put a Frontiers paper's DOI
onto an Industrial and Corporate Change item earlier. `review_publications.py`
proposes at 0.90 similarity and asks a human; this writes without asking, so
it demands more:

  * normalized title similarity >= 0.97
  * the first author's family name appears in the candidate's author list
  * a formal work type — never a dataset, a preprint record or a repository DOI
  * exactly one candidate survives; two plausible ones mean neither is proven

A resolution is stored in `doi_resolutions` with the matched title, the
similarity and the source, and `build_bibliography_db` reads it. Storing it
only in `papers.doi` would not survive: the builder derives that column from
Zotero, the review frontmatter and the PDF, none of which learn anything.
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "pipeline"
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import build_bibliography_db as bib            # noqa: E402
import review_publications as rp               # noqa: E402

DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"

# Higher than the 0.90 `review_publications.py` uses, because nobody sees this
# one before it is written.
MIN_SIMILARITY = 0.97


def _family_names(authors) -> set[str]:
    out = set()
    for name in authors or []:
        parts = [p for p in str(name).replace(",", " ").split() if p]
        if parts:
            out.add(parts[-1].casefold())
    return out


def _work_title(work: dict) -> str:
    return str(work.get("display_name") or work.get("title") or "")


def _work_venue(work: dict) -> str:
    source = (work.get("primary_location") or {}).get("source") or {}
    return str(source.get("display_name") or "")


def accept(paper: dict, work: dict) -> tuple[bool, str]:
    """Whether this candidate is the same paper, and why not when it is not."""
    doi = bib.clean_doi(str(work.get("doi") or ""))
    if not doi:
        return False, "no DOI on candidate"
    if doi.lower().startswith(rp.REPOSITORY_DOI_PREFIXES):
        return False, "repository DOI"
    kind = str(work.get("type") or "").lower()
    if kind and kind not in rp.FORMAL_TYPES:
        return False, f"type={kind}"
    if any(host in _work_venue(work).lower() for host in rp.REPOSITORY_VENUES):
        return False, "repository venue"
    score = rp.similarity(paper["title"], _work_title(work))
    if score < MIN_SIMILARITY:
        return False, f"similarity={score:.2f}"
    wanted = _family_names(paper.get("authors"))
    found = _family_names(rp.openalex_authors(work))
    if wanted and not found:
        return False, "candidate lists no authors"
    if wanted and not (wanted & found):
        return False, "no author in common"
    return True, f"similarity={score:.2f}"


def db_authors(conn: sqlite3.Connection, paper_id: int) -> list[str]:
    return [row[0] for row in conn.execute(
        "SELECT a.display_name FROM paper_authors pa"
        " JOIN authors a USING(author_id) WHERE pa.paper_id=?"
        " ORDER BY pa.author_order", (paper_id,))]


def targets(conn: sqlite3.Connection, limit: int | None) -> list[dict]:
    conn.row_factory = sqlite3.Row
    bib.ensure_doi_resolution_table(conn)
    rows = conn.execute(
        "SELECT p.paper_id, p.slug, p.title, p.arxiv_id FROM papers p"
        " LEFT JOIN doi_resolutions r ON r.slug = p.slug"
        " WHERE (p.doi IS NULL OR p.doi='') AND r.slug IS NULL"
        " ORDER BY p.paper_id").fetchall()
    out = [{"paper_id": r["paper_id"], "slug": r["slug"], "title": r["title"],
            "arxiv_id": r["arxiv_id"],
            "authors": db_authors(conn, r["paper_id"])} for r in rows]
    return out[:limit] if limit else out


def resolve(paper: dict) -> dict | None:
    """The one candidate that survives every check, or None."""
    if not (paper.get("title") or "").strip():
        return None
    accepted = []
    for work in rp.candidate_works(paper["title"]):
        ok, why = accept(paper, work)
        if ok:
            accepted.append((work, why))
    # Two survivors means the title is ambiguous — a shared title, a correction
    # notice, a reprint. Refusing is the only safe answer.
    if len(accepted) != 1:
        return None
    work, why = accepted[0]
    # OpenAlex ids carry the openalex.org host; Crossref-shaped ones are built
    # from doi.org. That is the only thing separating the two providers here.
    host = str(work.get("id") or "")
    return {"doi": bib.clean_doi(str(work.get("doi") or "")),
            "source": "openalex" if "openalex.org" in host else "crossref",
            "matched_title": _work_title(work),
            "similarity": round(
                rp.similarity(paper["title"], _work_title(work)), 3),
            "why": why}


def run(db: Path, *, execute: bool, limit: int | None) -> dict:
    conn = sqlite3.connect(db, timeout=60.0)
    conn.execute("PRAGMA busy_timeout = 60000")
    rows = targets(conn, limit)
    report = {"candidates": len(rows), "resolved": 0, "unresolved": 0,
              "by_source": {}, "samples": []}
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    for index, paper in enumerate(rows, 1):
        found = resolve(paper)
        if not found:
            report["unresolved"] += 1
        else:
            report["resolved"] += 1
            report["by_source"][found["source"]] = \
                report["by_source"].get(found["source"], 0) + 1
            if len(report["samples"]) < 12:
                report["samples"].append(
                    {"slug": paper["slug"][:48], "doi": found["doi"],
                     "similarity": found["similarity"],
                     "matched": found["matched_title"][:64]})
            if execute:
                conn.execute(
                    "INSERT INTO doi_resolutions (slug, doi, source,"
                    " matched_title, similarity, resolved_at)"
                    " VALUES (?,?,?,?,?,?)"
                    " ON CONFLICT(slug) DO UPDATE SET doi=excluded.doi,"
                    " source=excluded.source,"
                    " matched_title=excluded.matched_title,"
                    " similarity=excluded.similarity,"
                    " resolved_at=excluded.resolved_at",
                    (paper["slug"], found["doi"], found["source"],
                     found["matched_title"], found["similarity"], now))
                conn.execute("UPDATE papers SET doi=? WHERE paper_id=?",
                             (found["doi"], paper["paper_id"]))
        if index % 25 == 0:
            if execute:
                conn.commit()
            print(f"  [doi] {index}/{len(rows)} resolved={report['resolved']}",
                  file=sys.stderr, flush=True)

    if execute:
        conn.commit()
    conn.close()
    return report


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--execute", action="store_true",
                    help="write (default is dry-run)")
    ap.add_argument("--limit", type=int)
    args = ap.parse_args()

    report = run(args.db, execute=args.execute, limit=args.limit)
    print(json.dumps({"executed": args.execute, **report},
                     ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
