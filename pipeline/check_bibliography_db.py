#!/usr/bin/env python3
"""Validate the bibliography DB against the review corpus.

Rewritten when the affiliation organisation registry was retired. The previous
version was 1,112 lines and spent all but a hundred of them validating registry
machinery — closed cohorts, event ledgers, generation descriptors, relationship
transitions — while the one check that mattered, `suspicious institution names`,
reported 0 against a table that held "A Neural Network" and "3 MIT". Every check
here is about data a reader can actually be shown.
"""
from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path

import build_bibliography_db as bib

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "docs" / "papers" / "_papers_index.json"
DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"


def scalar(conn: sqlite3.Connection, sql: str) -> int:
    return conn.execute(sql).fetchone()[0]


def collect(db: Path, report: dict, issues: list[str], warnings: list[str]) -> None:
    conn = sqlite3.connect(db)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        tables = {row[0] for row in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table'")}
        required = {"papers", "authors", "institutions", "paper_authors",
                    "paper_institutions", "institution_aliases"}
        missing = required - tables
        if missing:
            issues.append("missing tables: " + ", ".join(sorted(missing)))
            return

        report["db_papers"] = scalar(conn, "SELECT COUNT(*) FROM papers")
        report["authors"] = scalar(conn, "SELECT COUNT(*) FROM authors")
        report["institutions"] = scalar(conn, "SELECT COUNT(*) FROM institutions")
        report["institution_aliases"] = scalar(
            conn, "SELECT COUNT(*) FROM institution_aliases")
        report["affiliation_links"] = scalar(
            conn, "SELECT COUNT(*) FROM paper_institutions")
        report["papers_with_affiliation"] = scalar(
            conn, "SELECT COUNT(DISTINCT paper_id) FROM paper_institutions")
        report["papers_with_author"] = scalar(
            conn, "SELECT COUNT(DISTINCT paper_id) FROM paper_authors")
        report["zotero_item_keys"] = scalar(
            conn, "SELECT COUNT(*) FROM papers WHERE zotero_item_key<>''")

        empty_titles = scalar(
            conn, "SELECT COUNT(*) FROM papers WHERE title='' OR title IS NULL")
        empty_dirs = scalar(
            conn,
            "SELECT COUNT(*) FROM papers WHERE review_dir='' OR review_dir IS NULL")
        report["empty_titles"] = empty_titles
        report["empty_review_dirs"] = empty_dirs
        if empty_titles:
            issues.append(f"empty titles: {empty_titles}")
        if empty_dirs:
            issues.append(f"empty review directories: {empty_dirs}")

        # Institutions the parser invented but no paper links to. The build
        # prunes these; a non-zero count means a writer bypassed the pruner.
        orphans = scalar(
            conn,
            "SELECT COUNT(*) FROM institutions i WHERE NOT EXISTS("
            " SELECT 1 FROM paper_institutions pi"
            " WHERE pi.institution_id = i.institution_id)")
        report["orphan_institutions"] = orphans
        if orphans:
            issues.append(f"orphan institutions: {orphans}")

        # The name gates exist to catch parser garbage. A name ROR resolved is
        # by definition not parser garbage, so only unresolved names are judged
        # — otherwise "Yale School of Medicine" and "Technische Universität
        # Berlin", both real ROR records, fail a rule written for fragments.
        columns = {row[1] for row in conn.execute(
            "PRAGMA table_info(institutions)")}
        names = [row[0] for row in conn.execute(
            "SELECT institution_name FROM institutions"
            + (" WHERE ror_id=''" if "ror_id" in columns else ""))]
        suspicious = [n for n in names if bib.is_suspicious_institution_name(n)]
        local_language = [n for n in names if bib.is_local_language_institution(n)]
        report["unverified_institution_names"] = len(names)
        report["suspicious_institution_names"] = len(suspicious)
        report["local_language_institution_names"] = len(local_language)
        if suspicious:
            issues.append("suspicious institution names: "
                          + ", ".join(suspicious[:10]))
        if local_language:
            issues.append("local-language institution names: "
                          + ", ".join(local_language[:10]))

        # Country is still unpopulated corpus-wide; report it rather than fail,
        # so the gap stays visible until the ISO map is wired into the build.
        with_country = scalar(
            conn, "SELECT COUNT(*) FROM institutions WHERE country_name_en<>''")
        report["institutions_with_country"] = with_country
        if report["institutions"] and not with_country:
            warnings.append("no institution carries a country name")

        report["affiliation_sources"] = dict(conn.execute(
            "SELECT source, COUNT(*) FROM paper_institutions GROUP BY source"))
        report["bibliography_sources"] = dict(conn.execute(
            "SELECT bibliography_source, COUNT(*) FROM papers "
            "GROUP BY bibliography_source"))

        # Institution names are ROR-normalised. The normaliser degrades to raw
        # PDF strings when its index is absent, and that degradation used to be
        # one log line, so it is a gate now.
        if {"ror_id", "parent_name"} <= columns and report["institutions"]:
            resolved = scalar(
                conn, "SELECT COUNT(*) FROM institutions WHERE ror_id<>''")
            report["ror_resolved"] = resolved
            report["ror_share"] = round(resolved / report["institutions"], 3)
            report["parent_groups"] = scalar(
                conn, "SELECT COUNT(DISTINCT parent_name) FROM institutions "
                      "WHERE parent_name<>''")
            if report["ror_share"] < 0.40:
                issues.append(
                    f"ROR normalisation collapsed: {resolved}/"
                    f"{report['institutions']} institutions carry a ROR id — "
                    "run python pipeline/setup_affiliation_sources.py")
            from lib.ror_index import ADMINISTRATIVE_BODY, UNIVERSITY_SYSTEM
            ineligible = [
                parent for (parent,) in conn.execute(
                    "SELECT DISTINCT parent_name FROM institutions "
                    "WHERE parent_name<>''")
                if ADMINISTRATIVE_BODY.search(parent)
                or UNIVERSITY_SYSTEM.search(parent)]
            if ineligible:
                issues.append("ineligible parent groups: "
                              + ", ".join(sorted(ineligible)[:8]))

            # The curated group table is the pinned baseline for parent groups.
            # Losing it costs 1,872 hierarchies while ROR keeps resolving, so no
            # other number in this report would move — hence an explicit gate.
            from lib import affiliation_groups
            curated = affiliation_groups.active_path()
            report["curated_group_table"] = str(curated) if curated else None
            report["curated_group_entries"] = \
                affiliation_groups.stats()["entries"]
            if curated is None:
                issues.append(
                    "curated affiliation group table missing — expected "
                    "pipeline/data/dict_afgroupname_confident.json or "
                    "PAPER_CURATION_AFGROUP_DICT; run python "
                    "pipeline/setup_affiliation_sources.py")
    finally:
        conn.close()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--strict", action="store_true",
                    help="exit 2 when any issue is found")
    ap.add_argument("--strict-warnings", action="store_true",
                    help="treat warnings as issues too")
    args = ap.parse_args()

    report: dict = {"ok": True, "issues": [], "warnings": []}
    issues: list[str] = []
    warnings: list[str] = []

    if not args.db.exists():
        issues.append(f"missing database: {args.db}")
    else:
        collect(args.db, report, issues, warnings)

    try:
        source_count = len(json.loads(INDEX.read_text(encoding="utf-8")))
        report["source_index_papers"] = source_count
        if "db_papers" in report and report["db_papers"] != source_count:
            issues.append(
                f"paper count mismatch: DB={report['db_papers']} "
                f"index={source_count}")
    except Exception as exc:
        issues.append(f"index read failed: {exc}")

    report["issues"] = issues
    report["warnings"] = warnings
    report["ok"] = not issues and (not args.strict_warnings or not warnings)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if report["ok"]:
        return 0
    return 2 if (args.strict or args.strict_warnings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
