"""Content digest of a SQLite database, used by the CAS publish path.

Extracted from the retired ``repair_bibliography_institutions.py`` (the
affiliation-3 migration tool) when the affiliation organisation registry was
removed. The digest itself has nothing to do with that registry: it is the
hash the push/pull compare-and-swap uses to prove two hosts hold the same DB.
"""
from __future__ import annotations

import hashlib
import json
import sqlite3


def schema_name(conn: sqlite3.Connection) -> str:
    """Identify the DB layout for CAS receipts."""
    tables = {row[0] for row in conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table'")}
    if {"papers", "institutions", "paper_institutions"} <= tables:
        return "bibliography-1"
    return "legacy"


def logical_digest(conn: sqlite3.Connection) -> str:
    """Hash logical DB content while excluding the self-referential migration audit."""
    value = hashlib.sha256()
    tables = [
        row[0] for row in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' "
            "AND name NOT LIKE 'sqlite_%' AND name<>'affiliation_migration_audit' "
            "ORDER BY name")
    ]
    for table in tables:
        columns = [row[1] for row in conn.execute(
            f'PRAGMA table_info("{table}")')]
        value.update(json.dumps([table, columns], separators=(",", ":")).encode())
        if not columns:
            continue
        quoted = ",".join(f'"{column}"' for column in columns)
        for row in conn.execute(
                f'SELECT {quoted} FROM "{table}" ORDER BY {quoted}'):
            encoded = [
                {"__bytes__": item.hex()} if isinstance(item, bytes) else item
                for item in row
            ]
            value.update(json.dumps(
                encoded, ensure_ascii=False, sort_keys=True,
                separators=(",", ":"), default=str).encode("utf-8"))
            value.update(b"\n")
    return value.hexdigest()

