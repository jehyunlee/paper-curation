#!/usr/bin/env python3
"""Attach each author to the institution the publisher says they were at.

    python pipeline/enrich_openalex_authorships.py --dry-run --limit 20
    python pipeline/enrich_openalex_authorships.py --execute

"Who are the strong researchers at institution X" cannot be answered from the
PDF-derived links alone. A byline maps an author to an institution through
superscript markers, and when a paper has several institutions and no markers
the builder has to fall back to linking every author to every institution:
31,566 of 36,667 links -- 86% -- are that cartesian guess, tagged
`pdf.unmarked-multi`. Ranking Stanford's authors over them returns people who
were never at Stanford; ranking over the 14% that are resolved returns nobody
with more than two papers.

OpenAlex publishes the mapping the publisher deposited: per author, the
institutions with ROR ids, whether they are the corresponding author, and a
disambiguated author id plus ORCID. One request per paper -- the same endpoint
`lib/metrics/collect.py` already calls, which asks only for citation fields.

Institutions are matched to ours by ROR first, then by normalized name, and a
name that matches nothing is inserted so the link is never dropped. Nothing
here overwrites PDF-derived rows: OpenAlex links are added with
`source='openalex'` alongside them, so a query can choose its evidence.
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "pipeline"
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"
MAILTO = "jehyun.lee@gmail.com"
SELECT = "id,doi,cited_by_count,authorships"


def _norm(value: str) -> str:
    import re
    return re.sub(r"\s+", " ", (value or "").strip()).casefold()


def ensure_schema(conn: sqlite3.Connection) -> None:
    """Columns and table this enrichment needs, added in place."""
    authors = {row[1] for row in conn.execute("PRAGMA table_info(authors)")}
    for name in ("openalex_id", "orcid"):
        if name not in authors:
            conn.execute(
                f"ALTER TABLE authors ADD COLUMN {name} TEXT NOT NULL DEFAULT ''")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_authors_openalex "
                 "ON authors(openalex_id)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_authors_orcid "
                 "ON authors(orcid)")
    # Per-paper provenance so a re-run is idempotent and a stale row is visible.
    conn.execute("""
        CREATE TABLE IF NOT EXISTS openalex_enrichment (
          paper_id INTEGER PRIMARY KEY REFERENCES papers ON DELETE CASCADE,
          openalex_id TEXT NOT NULL DEFAULT '',
          cited_by_count INTEGER,
          authorships INTEGER NOT NULL DEFAULT 0,
          linked_institutions INTEGER NOT NULL DEFAULT 0,
          corresponding INTEGER NOT NULL DEFAULT 0,
          retrieved_at TEXT NOT NULL)""")


def fetch_work(doi: str) -> dict | None:
    url = (f"https://api.openalex.org/works/doi:{urllib.parse.quote(doi)}"
           f"?select={SELECT}&mailto={MAILTO}")
    request = urllib.request.Request(
        url, headers={"User-Agent": f"paper-curation/1.0 (mailto:{MAILTO})"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.loads(response.read())
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None
            time.sleep(2 * (attempt + 1))
        except Exception:
            time.sleep(2 * (attempt + 1))
    return None


def institution_index(conn: sqlite3.Connection) -> tuple[dict, dict]:
    by_ror, by_name = {}, {}
    for iid, name, ror in conn.execute(
            "SELECT institution_id, institution_name, ror_id FROM institutions"):
        if ror:
            by_ror[ror.rsplit("/", 1)[-1].lower()] = iid
        by_name.setdefault(_norm(name), iid)
    return by_ror, by_name


def author_index(conn: sqlite3.Connection) -> dict:
    return {norm: aid for aid, norm in conn.execute(
        "SELECT author_id, normalized_name FROM authors")}


_ROR_CONN = None


def _ror_country(ror: str) -> str:
    """English country name for a ROR id, from the local ROR index.

    OpenAlex reports a country as an ISO code ("US"), but this DB stores names
    ("United States") and `country_map.canonical_country` does not expand a
    code. The ROR dump already holds the name under the same id OpenAlex hands
    back, so the authority stays ROR rather than a hand-written table.
    """
    global _ROR_CONN
    if not ror:
        return ""
    if _ROR_CONN is None:
        from lib import ror_index
        _ROR_CONN = (sqlite3.connect(f"file:{ror_index.INDEX_PATH}?mode=ro",
                                     uri=True)
                     if ror_index.INDEX_PATH.exists() else False)
    if _ROR_CONN is False:
        return ""
    row = _ROR_CONN.execute(
        "SELECT country_name FROM orgs WHERE ror_id=?", (ror,)).fetchone()
    return row[0] if row else ""


def upsert_institution(conn, by_ror, by_name, inst: dict) -> int | None:
    """Our institution_id for an OpenAlex institution, creating it if new."""
    name = str(inst.get("display_name") or "").strip()
    if not name:
        return None
    ror = str(inst.get("ror") or "")
    ror_key = ror.rsplit("/", 1)[-1].lower() if ror else ""
    if ror_key and ror_key in by_ror:
        return by_ror[ror_key]
    key = _norm(name)
    if key in by_name:
        return by_name[key]
    cur = conn.execute(
        "INSERT INTO institutions (institution_name, normalized_name,"
        " country_name_en, source, ror_id, name_source)"
        " VALUES (?,?,?,?,?,?)",
        (name, key, _ror_country(ror), "openalex", ror, "openalex"))
    iid = cur.lastrowid
    by_name[key] = iid
    if ror_key:
        by_ror[ror_key] = iid
    return iid


def upsert_author(conn, authors, display_name: str, openalex_id: str,
                  orcid: str) -> int | None:
    name = str(display_name or "").strip()
    if not name:
        return None
    key = _norm(name)
    aid = authors.get(key)
    if aid is None:
        cur = conn.execute(
            "INSERT INTO authors (display_name, normalized_name, openalex_id,"
            " orcid) VALUES (?,?,?,?)", (name, key, openalex_id, orcid))
        aid = cur.lastrowid
        authors[key] = aid
        return aid
    # Fill identifiers without overwriting one already recorded.
    conn.execute(
        "UPDATE authors SET openalex_id = CASE WHEN openalex_id='' THEN ?"
        " ELSE openalex_id END, orcid = CASE WHEN orcid='' THEN ? ELSE orcid END"
        " WHERE author_id=?", (openalex_id, orcid, aid))
    return aid


def enrich(db: Path, *, execute: bool, limit: int | None,
           refresh_days: int) -> dict:
    conn = sqlite3.connect(db, timeout=60.0)
    conn.execute("PRAGMA busy_timeout = 60000")
    ensure_schema(conn)
    conn.commit()

    cutoff = time.strftime(
        "%Y-%m-%d", time.gmtime(time.time() - refresh_days * 86400))
    rows = conn.execute(
        "SELECT p.paper_id, p.slug, p.doi FROM papers p"
        " LEFT JOIN openalex_enrichment e USING(paper_id)"
        " WHERE p.doi<>'' AND (e.paper_id IS NULL OR e.retrieved_at < ?)"
        " ORDER BY p.paper_id", (cutoff,)).fetchall()
    if limit:
        rows = rows[:limit]

    by_ror, by_name = institution_index(conn)
    authors = author_index(conn)
    report = {"candidates": len(rows), "fetched": 0, "not_found": 0,
              "authorships": 0, "institution_links": 0, "corresponding": 0,
              "orcids": 0, "new_institutions": 0}
    before_inst = conn.execute("SELECT COUNT(*) FROM institutions").fetchone()[0]

    for index, (paper_id, slug, doi) in enumerate(rows, 1):
        work = fetch_work(doi)
        if work is None:
            report["not_found"] += 1
            continue
        report["fetched"] += 1
        authorships = work.get("authorships") or []
        linked = corresponding = 0
        for position, entry in enumerate(authorships, 1):
            person = entry.get("author") or {}
            aid = upsert_author(
                conn, authors, person.get("display_name", ""),
                str(person.get("id") or "").rsplit("/", 1)[-1],
                str(person.get("orcid") or "").rsplit("/", 1)[-1])
            if aid is None:
                continue
            if person.get("orcid"):
                report["orcids"] += 1
            is_corresponding = 1 if entry.get("is_corresponding") else 0
            corresponding += is_corresponding
            conn.execute(
                "INSERT INTO paper_authors (paper_id, author_id, author_order,"
                " is_first_author, is_corresponding_author, source)"
                " VALUES (?,?,?,?,?,'openalex')"
                " ON CONFLICT(paper_id, author_id) DO UPDATE SET"
                "  is_corresponding_author = MAX(is_corresponding_author, ?)",
                (paper_id, aid, position,
                 1 if entry.get("author_position") == "first" else 0,
                 is_corresponding, is_corresponding))
            for inst in entry.get("institutions") or []:
                iid = upsert_institution(conn, by_ror, by_name, inst)
                if iid is None:
                    continue
                conn.execute(
                    "INSERT OR IGNORE INTO paper_author_institutions"
                    " (paper_id, author_id, institution_id, marker,"
                    "  author_order, source) VALUES (?,?,?,NULL,?,'openalex')",
                    (paper_id, aid, iid, position))
                linked += 1
        report["authorships"] += len(authorships)
        report["institution_links"] += linked
        report["corresponding"] += corresponding
        conn.execute(
            "INSERT INTO openalex_enrichment (paper_id, openalex_id,"
            " cited_by_count, authorships, linked_institutions, corresponding,"
            " retrieved_at) VALUES (?,?,?,?,?,?,?)"
            " ON CONFLICT(paper_id) DO UPDATE SET openalex_id=excluded.openalex_id,"
            " cited_by_count=excluded.cited_by_count,"
            " authorships=excluded.authorships,"
            " linked_institutions=excluded.linked_institutions,"
            " corresponding=excluded.corresponding,"
            " retrieved_at=excluded.retrieved_at",
            (paper_id, str(work.get("id") or "").rsplit("/", 1)[-1],
             work.get("cited_by_count"), len(authorships), linked,
             corresponding, time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())))
        if execute and index % 25 == 0:
            conn.commit()
            print(f"  [openalex] {index}/{len(rows)}", file=sys.stderr, flush=True)

    report["new_institutions"] = (
        conn.execute("SELECT COUNT(*) FROM institutions").fetchone()[0]
        - before_inst)
    if execute:
        conn.commit()
    else:
        conn.rollback()
    conn.close()
    return report


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--execute", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--refresh-days", type=int, default=90)
    args = ap.parse_args()

    report = enrich(args.db, execute=args.execute and not args.dry_run,
                    limit=args.limit, refresh_days=args.refresh_days)
    print(json.dumps({"executed": args.execute and not args.dry_run, **report},
                     ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
