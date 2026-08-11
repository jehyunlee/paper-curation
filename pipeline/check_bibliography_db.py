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

        # A paper must carry its own bibliography. Each of these was measured
        # in the shipped DB and each produced the same damage — a row holding
        # another work's title, journal and pagination. Gated so a repair
        # cannot silently rot back.
        from lib import zotero_identity
        identity = zotero_identity.audit(conn, ROOT / "docs" / "papers")
        report["placeholder_doi_papers"] = identity["placeholder_doi_papers"]
        report["papers_on_a_shared_zotero_key"] = \
            identity["papers_on_a_shared_key"]
        report["title_disagreements"] = identity["title_disagreements"]
        if identity["placeholder_doi_papers"]:
            issues.append(
                f"non-DOI values in papers.doi: "
                f"{identity['placeholder_doi_papers']} "
                f"({', '.join(identity['placeholder_doi_values'][:6])})")
        report["correction_pairs"] = identity["correction_pairs"]
        if identity["papers_on_a_shared_key"]:
            worst = identity["shared_key_detail"][0]
            # Two papers claiming one Zotero record is either contamination or
            # the same paper filed under two slugs. The second needs an
            # operator's decision (pipeline/dedup_zotero.py,
            # pipeline/audit_matching.py), so it is surfaced without blocking.
            warnings.append(
                f"papers sharing a Zotero item: "
                f"{identity['papers_on_a_shared_key']} across "
                f"{identity['shared_zotero_keys']} items "
                f"(worst: {worst['zotero_item_key']} — "
                f"{', '.join(slug[:28] for slug in worst['slugs'])})")
        if identity["title_disagreements"]:
            worst = identity["title_disagreement_detail"][0]
            issues.append(
                f"papers titled as another work: "
                f"{identity['title_disagreements']} "
                f"(worst: {worst['slug'][:40]} — DB {worst['db_title'][:40]!r})")

        # Connections are LLM claims: whether a claim is *true* cannot be
        # checked here and this gate does not pretend to. What is checkable is
        # that both endpoints are real papers — the JSON files this replaced
        # held 79 pairs pointing at papers deleted long ago, with nothing to
        # notice — and that every row names the model that asserted it, so a
        # later reader can tell derived data from bibliographic fact.
        if "paper_connections" in tables:
            report["connections"] = scalar(
                conn, "SELECT COUNT(*) FROM paper_connections")
            broken = scalar(
                conn,
                "SELECT COUNT(*) FROM paper_connections c WHERE NOT EXISTS("
                " SELECT 1 FROM papers p WHERE p.paper_id=c.paper_id) OR NOT"
                " EXISTS(SELECT 1 FROM papers p"
                "        WHERE p.paper_id=c.related_paper_id)")
            report["connection_dangling_endpoints"] = broken
            if broken:
                issues.append(f"connections with missing endpoints: {broken}")
            unattributed = scalar(
                conn,
                "SELECT COUNT(*) FROM paper_connections"
                " WHERE model IS NULL OR model=''")
            report["connections_without_model"] = unattributed
            if unattributed:
                issues.append(
                    f"connections not attributed to a model: {unattributed}")
            self_linked = scalar(
                conn, "SELECT COUNT(*) FROM paper_connections"
                      " WHERE paper_id=related_paper_id")
            if self_linked:
                issues.append(f"self-referential connections: {self_linked}")

        # Author-level affiliation. A row must agree with the paper-level table:
        # an author cannot sit at an institution the paper is not linked to.
        if "paper_author_institutions" in tables:
            report["author_institution_links"] = scalar(
                conn, "SELECT COUNT(*) FROM paper_author_institutions")
            inconsistent = scalar(
                conn,
                "SELECT COUNT(*) FROM paper_author_institutions pai"
                " WHERE NOT EXISTS(SELECT 1 FROM paper_institutions pi"
                "  WHERE pi.paper_id=pai.paper_id"
                "    AND pi.institution_id=pai.institution_id)")
            report["author_institution_inconsistent"] = inconsistent
            if inconsistent:
                issues.append(
                    "author affiliations absent from paper_institutions: "
                    f"{inconsistent}")

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
