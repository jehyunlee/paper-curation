#!/usr/bin/env python3
"""Audit and repair malformed institution names in the bibliography database."""
from __future__ import annotations

import argparse
import json
import shutil
import sqlite3
from collections import Counter
from pathlib import Path

import build_bibliography_db as bib


def _group_for(name: str) -> str:
    for group, pattern in bib.GROUPS:
        if bib.re.search(pattern, name, bib.re.I):
            return group
    return ""


def _source_rank(source: str) -> int:
    return {
        "scopus+pdf": 4,
        "scopus": 3,
        "pdf": 2,
        "scopus-unconfirmed": 1,
    }.get(source or "", 0)


def _should_prune_unresolved(name: str) -> bool:
    if name in bib.STANDALONE_INSTITUTION_NAMES:
        return False
    if name in bib.GENERIC_INSTITUTION_NAMES:
        return True
    if bib.re.search(r"(?:\band|\bof)$", name, bib.re.I):
        return True
    if len(name) > 90:
        return True
    if bib.re.search(
            r"^(?:Department|School|Faculty)\b|\b(?:Authors?|Published|"
            r"Proceedings|Copyright|is with|are with|work was)\b",
            name, bib.re.I):
        return True
    return not bool(bib.re.search(
        r"\b(?:University|Institute|Academy|College|Hospital|Laboratory|"
        r"Centre|Center|Research|Network)\b|MIT|ETH|CNRS", name, bib.re.I))


def audit_and_repair(db_path: Path, *, execute: bool = False) -> dict:
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    bib.initialize_institution_registry(conn)
    rows = conn.execute(
        "SELECT pi.paper_id,pi.institution_id,pi.raw_name,pi.country_name,"
        "pi.source,i.institution_name FROM paper_institutions pi "
        "JOIN institutions i USING(institution_id) "
        "ORDER BY pi.paper_id,pi.institution_id"
    ).fetchall()

    changes = []
    unresolved = Counter()
    pruned = []
    for paper_id, institution_id, raw, country, source, current in rows:
        canonical_current = bib.canonical_institution(current)
        resolved = bib.resolve_institution_from_raw(raw, current)
        if not resolved and canonical_current != current:
            resolved = canonical_current
        if not resolved and bib.is_suspicious_institution_name(current):
            parsed = bib.institution_from_raw(raw)
            resolved = parsed[0] if parsed else ""
        if resolved and resolved != current and not bib.is_suspicious_institution_name(resolved):
            changes.append({
                "paper_id": paper_id,
                "old_id": institution_id,
                "old_name": current,
                "new_name": resolved,
                "raw_name": raw,
                "country": country or bib.country_from_raw(raw),
                "source": source,
            })
        elif bib.is_suspicious_institution_name(current):
            if _should_prune_unresolved(current):
                pruned.append({
                    "paper_id": paper_id,
                    "institution_id": institution_id,
                    "name": current,
                    "raw_name": raw,
                })
            else:
                unresolved[current] += 1

    report = {
        "database": str(db_path),
        "paper_institution_rows": len(rows),
        "changes": len(changes),
        "pruned_rows": len(pruned),
        "unresolved_rows": sum(unresolved.values()),
        "unresolved_names": len(unresolved),
        "top_changes": Counter(
            (row["old_name"], row["new_name"]) for row in changes
        ).most_common(100),
        "top_unresolved": unresolved.most_common(100),
        "executed": execute,
    }
    if not execute:
        conn.close()
        return report

    backup = db_path.with_suffix(db_path.suffix + ".pre-institution-repair")
    shutil.copy2(db_path, backup)
    report["backup"] = str(backup)

    with conn:
        for row in pruned:
            conn.execute(
                "DELETE FROM paper_institutions WHERE paper_id=? "
                "AND institution_id=?",
                (row["paper_id"], row["institution_id"]),
            )
        for row in changes:
            group = _group_for(row["new_name"])
            group_id = None
            if group:
                found = conn.execute(
                    "SELECT group_id FROM institution_groups "
                    "WHERE normalized_name=?", (bib.norm(group),)).fetchone()
                group_id = found[0] if found else conn.execute(
                    "INSERT INTO institution_groups (group_name,normalized_name) "
                    "VALUES (?,?)", (group, bib.norm(group))).lastrowid

            found = conn.execute(
                "SELECT institution_id,group_id,source FROM institutions "
                "WHERE normalized_name=?", (bib.norm(row["new_name"]),)).fetchone()
            if found:
                target_id = found[0]
                if group_id and not found[1]:
                    conn.execute(
                        "UPDATE institutions SET group_id=? WHERE institution_id=?",
                        (group_id, target_id))
            else:
                target_id = conn.execute(
                    "INSERT INTO institutions "
                    "(institution_name,normalized_name,group_id,source) "
                    "VALUES (?,?,?,?)",
                    (row["new_name"], bib.norm(row["new_name"]), group_id,
                     row["source"]),
                ).lastrowid

            existing = conn.execute(
                "SELECT raw_name,country_name,source FROM paper_institutions "
                "WHERE paper_id=? AND institution_id=?",
                (row["paper_id"], target_id),
            ).fetchone()
            if existing:
                source = (row["source"] if _source_rank(row["source"]) >
                          _source_rank(existing[2]) else existing[2])
                conn.execute(
                    "UPDATE paper_institutions SET country_name=?,source=? "
                    "WHERE paper_id=? AND institution_id=?",
                    (existing[1] or row["country"], source,
                     row["paper_id"], target_id),
                )
                conn.execute(
                    "DELETE FROM paper_institutions WHERE paper_id=? "
                    "AND institution_id=?",
                    (row["paper_id"], row["old_id"]),
                )
            else:
                conn.execute(
                    "UPDATE paper_institutions SET institution_id=?,"
                    "country_name=? WHERE paper_id=? AND institution_id=?",
                    (target_id, row["country"], row["paper_id"], row["old_id"]),
                )
            normalized_alias = bib.norm(row["raw_name"])
            updated = conn.execute(
                "UPDATE institution_aliases SET institution_id=? "
                "WHERE raw_name=? OR normalized_alias=?",
                (target_id, row["raw_name"], normalized_alias),
            ).rowcount
            if not updated:
                conn.execute(
                    "INSERT INTO institution_aliases "
                    "(raw_name,normalized_alias,institution_id) VALUES (?,?,?)",
                    (row["raw_name"], normalized_alias, target_id),
                )

        conn.execute(
            "DELETE FROM institution_aliases WHERE institution_id NOT IN "
            "(SELECT DISTINCT institution_id FROM paper_institutions)")
        conn.execute(
            "DELETE FROM institutions WHERE institution_id NOT IN "
            "(SELECT DISTINCT institution_id FROM paper_institutions)")
        conn.execute("PRAGMA optimize")

    report["institutions_after"] = conn.execute(
        "SELECT COUNT(*) FROM institutions").fetchone()[0]
    report["links_after"] = conn.execute(
        "SELECT COUNT(*) FROM paper_institutions").fetchone()[0]
    conn.close()
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=bib.DEFAULT_DB)
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--report", type=Path,
                        default=bib.ROOT / ".cache" / "institution_repair_report.json")
    args = parser.parse_args()
    result = audit_and_repair(args.db, execute=args.execute)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
