"""Synchronize citation observations into the bibliography SQLite database."""
from __future__ import annotations

import os
import sqlite3
from pathlib import Path

from .store import read_citations

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_DB = Path(os.environ.get(
    "PAPER_CURATION_BIBLIO_DB", str(ROOT / ".cache" / "bibliography.sqlite3")
))
PAPERS_DIR = ROOT / "docs" / "papers"

SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS citation_snapshots (
 paper_id INTEGER NOT NULL REFERENCES papers ON DELETE CASCADE,
 observed_date TEXT NOT NULL, openalex_count INTEGER, crossref_count INTEGER,
 scopus_count INTEGER, normalized_percentile REAL,
 PRIMARY KEY (paper_id, observed_date));
CREATE TABLE IF NOT EXISTS citation_yearly (
 paper_id INTEGER NOT NULL REFERENCES papers ON DELETE CASCADE,
 citation_year INTEGER NOT NULL, source TEXT NOT NULL,
 citation_count INTEGER NOT NULL, retrieved_at TEXT NOT NULL,
 PRIMARY KEY (paper_id, citation_year, source));
CREATE INDEX IF NOT EXISTS idx_citation_snapshots_date
 ON citation_snapshots(observed_date);
CREATE INDEX IF NOT EXISTS idx_citation_yearly_year
 ON citation_yearly(citation_year);
"""


def sync_metrics_database(
    results: list[dict], observed_date: str, *, db_path: Path = DEFAULT_DB,
    papers_dir: Path = PAPERS_DIR,
) -> dict:
    """Backfill observed history and upsert OpenAlex annual citation flows."""
    db_path = Path(db_path)
    if not db_path.exists():
        return {"skipped": True, "reason": f"database not found: {db_path}",
                "snapshots": 0, "yearly": 0}

    conn = sqlite3.connect(db_path)
    conn.executescript(SCHEMA)
    snapshots = yearly = 0
    with conn:
        papers = conn.execute("SELECT paper_id, slug FROM papers").fetchall()
        for paper_id, slug in papers:
            doc = read_citations(Path(papers_dir) / slug)
            for snapshot in doc.history:
                conn.execute(
                    "INSERT INTO citation_snapshots "
                    "(paper_id,observed_date,openalex_count,crossref_count,"
                    "scopus_count,normalized_percentile) VALUES (?,?,?,?,?,?) "
                    "ON CONFLICT(paper_id,observed_date) DO UPDATE SET "
                    "openalex_count=COALESCE(excluded.openalex_count,openalex_count),"
                    "crossref_count=COALESCE(excluded.crossref_count,crossref_count),"
                    "scopus_count=COALESCE(excluded.scopus_count,scopus_count),"
                    "normalized_percentile=COALESCE("
                    "excluded.normalized_percentile,normalized_percentile)",
                    (paper_id, snapshot.date, snapshot.openalex,
                     snapshot.crossref, snapshot.scopus, snapshot.percentile),
                )
                snapshots += 1

        paper_ids = {slug: paper_id for paper_id, slug in papers}
        for result in results:
            paper_id = paper_ids.get(result.get("slug", ""))
            if paper_id is None:
                continue
            for annual in result.get("yearly") or []:
                year = annual.get("year")
                count = annual.get("cited_by_count")
                if year is None or count is None:
                    continue
                conn.execute(
                    "INSERT INTO citation_yearly "
                    "(paper_id,citation_year,source,citation_count,retrieved_at) "
                    "VALUES (?,?,?,?,?) ON CONFLICT(paper_id,citation_year,source) "
                    "DO UPDATE SET citation_count=excluded.citation_count,"
                    "retrieved_at=excluded.retrieved_at",
                    (paper_id, int(year), "openalex", int(count), observed_date),
                )
                yearly += 1
    conn.execute("PRAGMA optimize")
    conn.close()
    return {"skipped": False, "snapshots": snapshots, "yearly": yearly,
            "db": str(db_path)}
