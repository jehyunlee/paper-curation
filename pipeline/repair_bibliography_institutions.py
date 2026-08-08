#!/usr/bin/env python3
"""Controlled, local-only migrator for existing bibliography databases."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sqlite3
import sys
import time
from pathlib import Path

import build_bibliography_db as bib


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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


def _fsync_directory(directory: Path) -> None:
    descriptor = os.open(directory, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _fsync(path: Path) -> None:
    with path.open("rb") as stream:
        os.fsync(stream.fileno())
    _fsync_directory(path.parent)
def _checkpoint_fully(conn: sqlite3.Connection) -> None:
    result = conn.execute("PRAGMA wal_checkpoint(FULL)").fetchone()
    if result is None or len(result) != 3 or result[0] != 0 or result[1] != result[2]:
        raise RuntimeError("SQLite WAL checkpoint did not complete")
    _fsync(Path(conn.execute("PRAGMA database_list").fetchone()[2]))


def _verify_standalone_database(db: Path, expected_logical_hash: str) -> None:
    """Verify the checkpointed main database is independently reopenable."""
    copied = db.with_name(f".{db.name}.{os.getpid()}.receipt-verify.sqlite3")
    standalone = None
    try:
        shutil.copyfile(db, copied)
        _fsync(copied)
        standalone = sqlite3.connect(copied)
        if standalone.execute("PRAGMA quick_check").fetchone()[0] != "ok":
            raise RuntimeError("standalone receipt database integrity check failed")
        if standalone.execute("PRAGMA foreign_key_check").fetchone() is not None:
            raise RuntimeError("standalone receipt database foreign-key check failed")
        if logical_digest(standalone) != expected_logical_hash:
            raise RuntimeError("standalone receipt database logical hash mismatch")
    finally:
        if standalone is not None:
            standalone.close()
        copied.unlink(missing_ok=True)


def _is_sha256(value: object) -> bool:
    return (isinstance(value, str) and len(value) == 64
            and all(character in "0123456789abcdef" for character in value))


def _receipt_id(report: dict) -> str:
    """Bind report inputs that do not depend on the metadata receipt ID itself."""
    bound = {key: value for key, value in report.items()
             if key not in {"receipt_id", "result_sha256", "result_logical_sha256"}}
    return hashlib.sha256(json.dumps(
        bound, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def _atomic_json(path: Path, value: dict) -> None:
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    try:
        temporary.write_text(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                       separators=(",", ":")), encoding="utf-8")
        _fsync(temporary)
        os.replace(temporary, path)
        _fsync(path)
    finally:
        temporary.unlink(missing_ok=True)


def lock_path(db: Path) -> Path:
    return db.with_suffix(db.suffix + ".affiliation-migrate.lock")


def marker_path(db: Path) -> Path:
    return db.with_suffix(db.suffix + ".remigration-required.json")


def receipt_path(db: Path, operation: str) -> Path:
    return db.with_suffix(db.suffix + f".affiliation-{operation}.json")


def acquire_lock(db: Path) -> int:
    try:
        return os.open(lock_path(db), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as exc:
        raise RuntimeError("migration lock busy; remove only after confirming no migration is running") from exc


def _schema_name(conn: sqlite3.Connection) -> str:
    return bib.AFFILIATION_SCHEMA_VERSION if bib.is_latest_affiliation_schema(conn) else "legacy"


def _ddl_statements(script: str) -> list[str]:
    """Split SQLite statements without executescript's implicit transaction commit."""
    statements, pending = [], ""
    for line in script.splitlines(keepends=True):
        pending += line
        if sqlite3.complete_statement(pending):
            statement = pending.strip()
            if statement:
                statements.append(statement)
            pending = ""
    if pending.strip():
        raise RuntimeError("incomplete affiliation schema DDL")
    return statements
class _SchemaInstalledConnection:
    """Proxy that prevents a public projector from re-running transactional DDL."""

    def __init__(self, connection: sqlite3.Connection) -> None:
        self._connection = connection

    def executescript(self, script: str) -> None:
        if script != bib.AFFILIATION_SCHEMA:
            raise RuntimeError("unexpected projector schema script")

    def __getattr__(self, name: str):
        return getattr(self._connection, name)




def _registry_provenance() -> dict:
    registry = bib.affiliation_registry.load_registry(bib.REGISTRY_PATH)
    return {
        "registry_sha256": bib._registry_digest(),
        "event_head": registry["event_head"],
        "policy_version": registry["policy_version"],
        "source_sha256": registry["source_sha256"],
    }


def _verify_base(db: Path, conn: sqlite3.Connection, base_receipt: Path | None) -> dict:
    if base_receipt is None:
        raise RuntimeError("execute requires a complete base receipt")
    if not base_receipt.exists():
        raise RuntimeError(f"missing expected base receipt: {base_receipt}")
    try:
        expected = json.loads(base_receipt.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError("invalid expected base receipt") from exc
    if not isinstance(expected, dict):
        raise RuntimeError("invalid expected base receipt")
    required = {
        "database", "sha256", "logical_sha256", "schema_version", "generation",
        "registry_sha256", "event_head", "policy_version", "source_sha256",
    }
    missing = sorted(key for key in required if expected.get(key) in (None, ""))
    if missing:
        raise RuntimeError("expected base receipt lacks required provenance: " + ",".join(missing))
    if expected["database"] not in {str(db), db.name}:
        raise RuntimeError("expected base receipt database path mismatch")
    if expected["sha256"] != digest(db):
        raise RuntimeError("expected base receipt database hash mismatch")
    if expected["logical_sha256"] != logical_digest(conn):
        raise RuntimeError("expected base receipt logical hash mismatch")
    if expected["schema_version"] != _schema_name(conn):
        raise RuntimeError("expected base receipt schema mismatch")
    if not isinstance(expected["generation"], int) or expected["generation"] < 0:
        raise RuntimeError("expected base receipt generation is invalid")
    actual = _registry_provenance()
    for key, value in actual.items():
        if expected[key] != value:
            raise RuntimeError(f"expected base receipt {key} mismatch")
    return expected


def validate(conn: sqlite3.Connection) -> list[str]:
    issues = []
    if conn.execute("PRAGMA quick_check").fetchone()[0] != "ok":
        issues.append("quick_check failed")
    if conn.execute("PRAGMA foreign_key_check").fetchone() is not None:
        issues.append("foreign-key violation")
    bad_current = conn.execute(
        "SELECT COUNT(*) FROM observed_affiliation_slots s WHERE "
        "(SELECT COUNT(*) FROM observed_affiliations o WHERE "
        "o.observation_slot_id=s.observation_slot_id AND o.is_current=1) != 1"
    ).fetchone()[0]
    if bad_current:
        issues.append(f"slots without exactly one current observation: {bad_current}")
    bad_pending = conn.execute(
        "SELECT COUNT(*) FROM affiliation_pending_cases WHERE "
        "active_observation_count < 0 OR lifetime_observation_count < active_observation_count "
        "OR (status IN ('open','proposed') AND active_observation_count=0) "
        "OR (status IN ('resolved','rejected') AND active_observation_count<>0)"
    ).fetchone()[0]
    if bad_pending:
        issues.append(f"pending invariant violations: {bad_pending}")
    return issues


def _backup(source: sqlite3.Connection, backup: Path, base_logical_hash: str,
            base_schema: str) -> str:
    """Durably stage a SQLite snapshot while the source write lock is held."""
    temporary = backup.with_name(f".{backup.name}.{os.getpid()}.tmp")
    target = None
    try:
        snapshot = source.serialize()
        with temporary.open("wb") as handle:
            handle.write(snapshot)
            handle.flush()
            os.fsync(handle.fileno())
        target = sqlite3.connect(temporary)
        target.commit()
        if target.execute("PRAGMA quick_check").fetchone()[0] != "ok":
            raise RuntimeError("SQLite backup integrity check failed")
        if logical_digest(target) != base_logical_hash:
            raise RuntimeError("SQLite backup logical hash mismatch")
        if _schema_name(target) != base_schema:
            raise RuntimeError("SQLite backup schema mismatch")
        target.close()
        target = None
        _fsync(temporary)
        os.replace(temporary, backup)
        _fsync(backup)
        return digest(backup)
    finally:
        if target is not None:
            target.close()
        temporary.unlink(missing_ok=True)


def _recover_missing_receipt(db: Path, source: sqlite3.Connection) -> dict:
    """Rebuild a sidecar only from the committed migration authority."""
    if not bib.is_latest_affiliation_schema(source):
        raise RuntimeError("receipt recovery requires the latest affiliation schema")
    issues = validate(source)
    if issues:
        raise RuntimeError("receipt recovery database validation failed: " + "; ".join(issues))
    metadata = source.execute(
        "SELECT schema_version,registry_sha256,event_head,policy_version,source_sha256,"
        "base_generation,migration_receipt_id FROM affiliation_registry_metadata "
        "WHERE singleton=1").fetchone()
    if metadata is None:
        raise RuntimeError("receipt recovery metadata is missing")
    (schema_version, metadata_registry, metadata_event_head, metadata_policy,
     metadata_source, metadata_generation, receipt_id) = metadata
    if not _is_sha256(receipt_id):
        raise RuntimeError("receipt recovery metadata receipt id is invalid")
    audit = source.execute(
        "SELECT operation,base_generation,base_logical_sha256,result_logical_sha256,"
        "registry_sha256,schema_from,schema_to,backup_path,backup_sha256,"
        "started_at,finished_at,report_json FROM affiliation_migration_audit "
        "WHERE receipt_id=?",
        (receipt_id,),
    ).fetchone()
    if audit is None:
        raise RuntimeError("receipt recovery migration audit is missing")
    try:
        report = json.loads(audit[11])
    except (TypeError, json.JSONDecodeError) as exc:
        raise RuntimeError("receipt recovery migration audit is invalid") from exc
    required = {
        "operation", "database", "backup", "backup_sha256", "base_sha256",
        "base_logical_sha256", "result_logical_sha256", "registry_sha256",
        "event_head", "policy_version", "source_sha256", "schema_from",
        "schema_version", "schema_to", "base_generation", "started_at",
        "finished_at", "issues", "receipt_id",
    }
    if (not isinstance(report, dict) or set(report) != required
            or report["operation"] != "migrate" or report["issues"] != []):
        raise RuntimeError("receipt recovery migration audit provenance is invalid")
    if (not all(_is_sha256(report[key]) for key in (
            "backup_sha256", "base_sha256", "base_logical_sha256",
            "result_logical_sha256", "registry_sha256", "source_sha256"))
            or not isinstance(report["base_generation"], int)
            or report["base_generation"] < 0
            or not _is_sha256(report["receipt_id"])):
        raise RuntimeError("receipt recovery migration audit report is invalid")
    if report["database"] not in {str(db), db.name} or report["receipt_id"] != receipt_id:
        raise RuntimeError("receipt recovery migration audit identity mismatch")
    if _receipt_id(report) != receipt_id:
        raise RuntimeError("receipt recovery migration audit receipt id mismatch")
    if audit[:11] != (
            "migrate", report["base_generation"], report["base_logical_sha256"],
            report["result_logical_sha256"], report["registry_sha256"],
            report["schema_from"], report["schema_to"], report["backup"],
            report["backup_sha256"], report["started_at"], report["finished_at"]):
        raise RuntimeError("receipt recovery migration audit mismatch")
    if (schema_version != report["schema_to"]
            or report["schema_version"] != report["schema_to"]
            or metadata_generation != report["base_generation"]
            or (metadata_registry, metadata_event_head, metadata_policy, metadata_source)
            != (report["registry_sha256"], report["event_head"],
                report["policy_version"], report["source_sha256"])):
        raise RuntimeError("receipt recovery metadata provenance mismatch")
    for key, value in _registry_provenance().items():
        if report[key] != value:
            raise RuntimeError(f"receipt recovery {key} mismatch")
    if logical_digest(source) != report["result_logical_sha256"]:
        raise RuntimeError("receipt recovery database logical hash mismatch")
    backup = Path(report["backup"])
    if not backup.exists() or digest(backup) != report["backup_sha256"]:
        raise RuntimeError("receipt recovery migration backup provenance mismatch")
    _checkpoint_fully(source)
    _verify_standalone_database(db, report["result_logical_sha256"])
    receipt = dict(report)
    receipt["result_sha256"] = digest(db)
    return receipt


def _existing_receipt_matches(path: Path, expected: dict) -> bool:
    try:
        receipt = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return receipt == expected

def migrate(db: Path, *, execute: bool, base_receipt: Path | None) -> dict:
    if not db.exists():
        raise RuntimeError(f"missing database: {db}")
    conn = sqlite3.connect(db)
    try:
        already = bib.is_latest_affiliation_schema(conn)
        tables = {row[0] for row in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        plan = {"database": str(db), "already_latest": already, "execute": execute,
                "legacy_links": conn.execute("SELECT COUNT(*) FROM paper_institutions").fetchone()[0]
                if "paper_institutions" in tables else 0,
                "registry_sha256": bib._registry_digest()}
        if already:
            plan["issues"] = validate(conn)
            if not execute:
                return plan
        if not execute:
            return plan
    finally:
        conn.close()
    if base_receipt is None and not already:
        raise RuntimeError(
            "execute requires a matching base receipt with database, schema, "
            "registry, and generation provenance")

    fd = acquire_lock(db)
    backup = db.with_suffix(db.suffix + ".pre-affiliation-2.sqlite3")
    source = None
    try:
        source = sqlite3.connect(db)
        if bib.is_latest_affiliation_schema(source):
            receipt = _recover_missing_receipt(db, source)
            sidecar = receipt_path(db, "migrate")
            receipt_matches = _existing_receipt_matches(sidecar, receipt)
            if not receipt_matches:
                _atomic_json(sidecar, receipt)
            marker_path(db).unlink(missing_ok=True)
            if receipt_matches:
                return {
                    "database": str(db),
                    "already_latest": True,
                    "execute": execute,
                    "issues": validate(source),
                    "registry_sha256": bib._registry_digest(),
                    "receipt_id": receipt["receipt_id"],
                }
            return receipt
        source.execute("PRAGMA foreign_keys = OFF")
        # The write snapshot must precede every provenance check and the backup.
        source.execute("BEGIN IMMEDIATE")
        expected = _verify_base(db, source, base_receipt)
        base_logical_hash = expected["logical_sha256"]
        base_hash = expected["sha256"]
        backup_hash = _backup(
            source, backup, base_logical_hash, expected["schema_version"])
        started = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        try:
            for statement in _ddl_statements(bib.AFFILIATION_SCHEMA):
                source.execute(statement)
            bib.ensure_legacy_institution_schema(source)
            registry = bib.project_affiliation_registry(_SchemaInstalledConnection(source))
            rows = source.execute(
                "SELECT pi.paper_id,pi.raw_name,pi.country_name,pi.source FROM paper_institutions pi "
                "ORDER BY pi.paper_id,pi.institution_id"
            ).fetchall()
            for ordinal, (paper_id, raw, country, source_name) in enumerate(rows):
                bib.record_affiliation_observation(
                    source, paper_id, {"raw_name": raw, "country": country, "source": source_name},
                    ordinal, registry)
            provenance = _registry_provenance()
            receipt = {
                "operation": "migrate", "database": str(db), "backup": str(backup),
                "backup_sha256": backup_hash, "base_sha256": base_hash,
                "base_logical_sha256": base_logical_hash,
                "registry_sha256": provenance["registry_sha256"],
                "event_head": provenance["event_head"],
                "policy_version": provenance["policy_version"],
                "source_sha256": provenance["source_sha256"],
                "schema_from": expected["schema_version"],
                "schema_version": bib.AFFILIATION_SCHEMA_VERSION,
                "schema_to": bib.AFFILIATION_SCHEMA_VERSION,
                "base_generation": expected["generation"], "started_at": started,
                "finished_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "issues": [],
            }
            receipt_id = _receipt_id(receipt)
            receipt["receipt_id"] = receipt_id
            source.execute(
                "UPDATE affiliation_registry_metadata SET base_generation=?,"
                "migration_receipt_id=? WHERE singleton=1",
                (expected.get("generation", 0), receipt_id))
            issues = validate(source)
            if issues:
                raise RuntimeError("; ".join(issues))
            result_logical_hash = logical_digest(source)
            receipt["result_logical_sha256"] = result_logical_hash
            source.execute("INSERT INTO affiliation_migration_audit VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                           (receipt_id, "migrate", receipt["base_generation"],
                            base_logical_hash, result_logical_hash,
                            receipt["registry_sha256"], "legacy", receipt["schema_version"], str(backup),
                            backup_hash, started, receipt["finished_at"],
                            json.dumps(receipt, sort_keys=True, separators=(",", ":"))))
            source.commit()
            source.execute("PRAGMA foreign_keys = ON")
            _checkpoint_fully(source)
            _verify_standalone_database(db, receipt["result_logical_sha256"])
        except BaseException:
            source.rollback()
            source.execute("PRAGMA foreign_keys = ON")
            raise
        receipt["result_sha256"] = digest(db)
        _atomic_json(receipt_path(db, "migrate"), receipt)
        marker_path(db).unlink(missing_ok=True)
        return receipt
    finally:
        if source is not None:
            source.close()
        try:
            os.close(fd)
        finally:
            lock_path(db).unlink(missing_ok=True)


def _verify_current_result(db: Path, receipt: dict) -> None:
    """Require rollback to replace exactly the migration result it names."""
    current = sqlite3.connect(db)
    try:
        if current.execute("PRAGMA quick_check").fetchone()[0] != "ok":
            raise RuntimeError("current database integrity check failed")
        if digest(db) != receipt["result_sha256"]:
            raise RuntimeError("current database file hash mismatch")
        if logical_digest(current) != receipt["result_logical_sha256"]:
            raise RuntimeError("current database logical hash mismatch")
        if _schema_name(current) != receipt["schema_to"]:
            raise RuntimeError("current database schema mismatch")
        for key, value in _registry_provenance().items():
            if receipt[key] != value:
                raise RuntimeError(f"current database {key} mismatch")
        audit = current.execute(
            "SELECT operation,base_generation,base_logical_sha256,"
            "result_logical_sha256,registry_sha256,schema_from,schema_to,report_json "
            "FROM affiliation_migration_audit WHERE receipt_id=?",
            (receipt["receipt_id"],),
        ).fetchone()
        if audit is None:
            raise RuntimeError("current database migration audit is missing")
        if audit[:7] != (
                "migrate", receipt["base_generation"], receipt["base_logical_sha256"],
                receipt["result_logical_sha256"], receipt["registry_sha256"],
                receipt["schema_from"], receipt["schema_to"]):
            raise RuntimeError("current database migration audit mismatch")
        try:
            report = json.loads(audit[7])
        except (TypeError, json.JSONDecodeError) as exc:
            raise RuntimeError("current database migration audit is invalid") from exc
        for key, value in receipt.items():
            if key != "result_sha256" and report.get(key) != value:
                raise RuntimeError("current database migration audit receipt mismatch")
    finally:
        current.close()


def rollback(db: Path, *, expected_receipt: Path | None = None) -> dict:
    backup = db.with_suffix(db.suffix + ".pre-affiliation-2.sqlite3")
    receipt_file = expected_receipt or receipt_path(db, "migrate")
    if not backup.exists() or not receipt_file.exists():
        raise RuntimeError("missing migration backup or receipt")
    try:
        receipt = json.loads(receipt_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError("invalid migration receipt") from exc
    if receipt.get("backup") != str(backup) or receipt.get("backup_sha256") != digest(backup):
        raise RuntimeError("migration backup receipt/hash mismatch")
    required = {
        "operation", "receipt_id", "backup", "backup_sha256", "base_sha256",
        "base_logical_sha256", "result_sha256", "result_logical_sha256",
        "schema_from", "schema_to", "base_generation",
        "registry_sha256", "event_head", "policy_version", "source_sha256",
    }
    missing = sorted(key for key in required if receipt.get(key) in (None, ""))
    if missing or receipt.get("operation") != "migrate":
        raise RuntimeError("invalid migration receipt provenance")
    probe = sqlite3.connect(backup)
    try:
        if _schema_name(probe) != receipt["schema_from"]:
            raise RuntimeError("migration backup schema mismatch")
        if probe.execute("PRAGMA quick_check").fetchone()[0] != "ok":
            raise RuntimeError("migration backup integrity check failed")
        if logical_digest(probe) != receipt["base_logical_sha256"]:
            raise RuntimeError("migration backup logical hash mismatch")
    finally:
        probe.close()

    fd = acquire_lock(db)
    temporary = db.with_name(f".{db.name}.rollback.{os.getpid()}.tmp")
    quarantined: list[tuple[Path, Path]] = []
    quarantines_removed = False
    try:
        _verify_current_result(db, receipt)
        shutil.copyfile(backup, temporary)
        _fsync(temporary)
        restored = sqlite3.connect(temporary)
        try:
            if restored.execute("PRAGMA quick_check").fetchone()[0] != "ok":
                raise RuntimeError("rollback temporary integrity check failed")
            if _schema_name(restored) != receipt["schema_from"]:
                raise RuntimeError("rollback temporary schema mismatch")
            if logical_digest(restored) != receipt["base_logical_sha256"]:
                raise RuntimeError("rollback temporary logical hash mismatch")
        finally:
            restored.close()

        for path in (db, Path(str(db) + "-wal"), Path(str(db) + "-shm")):
            if path.exists():
                quarantine = path.with_name(
                    f".{path.name}.rollback-quarantine.{os.getpid()}")
                quarantine.unlink(missing_ok=True)
                os.replace(path, quarantine)
                quarantined.append((path, quarantine))
        _fsync_directory(db.parent)
        os.replace(temporary, db)
        _fsync(db)
        restored = sqlite3.connect(db)
        try:
            if (digest(db) != receipt["backup_sha256"]
                    or logical_digest(restored) != receipt["base_logical_sha256"]
                    or _schema_name(restored) != receipt["schema_from"]):
                raise RuntimeError("rollback restore provenance mismatch")
        finally:
            restored.close()
        for _, quarantine in quarantined:
            quarantine.unlink(missing_ok=True)
        quarantines_removed = True
        _fsync_directory(db.parent)
        result = {"operation": "rollback", "database": str(db), "backup": str(backup),
                  "backup_sha256": digest(backup), "schema_version": receipt["schema_from"],
                  "finished_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
        _atomic_json(receipt_path(db, "rollback"), result)
        _atomic_json(marker_path(db), {
            "operation": "remigration_required", "database": str(db),
            "rollback_receipt": str(receipt_path(db, "rollback")),
            "required_schema_version": bib.AFFILIATION_SCHEMA_VERSION,
            "created_at": result["finished_at"],
        })
        return result
    except BaseException:
        if quarantined and not quarantines_removed:
            db.unlink(missing_ok=True)
            for original, quarantine in quarantined:
                if quarantine.exists():
                    os.replace(quarantine, original)
            _fsync_directory(db.parent)
        raise
    finally:
        temporary.unlink(missing_ok=True)
        try:
            os.close(fd)
        finally:
            lock_path(db).unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=bib.DEFAULT_DB)
    parser.add_argument("--registry", type=Path, default=bib.REGISTRY_PATH)
    parser.add_argument("--base-receipt", type=Path)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--rollback", action="store_true")
    args = parser.parse_args()
    bib.REGISTRY_PATH = args.registry
    try:
        result = rollback(args.db, expected_receipt=args.base_receipt) if args.rollback else migrate(
            args.db, execute=args.execute, base_receipt=args.base_receipt)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 5 if "lock busy" in str(exc) else 1
    if args.report:
        _atomic_json(args.report, result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
