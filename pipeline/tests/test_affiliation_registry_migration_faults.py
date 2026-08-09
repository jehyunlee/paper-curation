import hashlib
import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

PIPELINE_DIR = Path(__file__).resolve().parents[1]
if str(PIPELINE_DIR) not in sys.path:
    sys.path.insert(0, str(PIPELINE_DIR))

import build_bibliography_db as bib
import repair_bibliography_institutions as migrator


class AffiliationMigrationFaultTests(unittest.TestCase):
    def legacy_db(self, path):
        conn = sqlite3.connect(path)
        conn.executescript("""
            CREATE TABLE papers (paper_id INTEGER PRIMARY KEY);
            CREATE TABLE institutions (institution_id INTEGER PRIMARY KEY, normalized_name TEXT);
            CREATE TABLE paper_institutions (institution_id INTEGER, paper_id INTEGER,
                raw_name TEXT, country_name TEXT, source TEXT);
            INSERT INTO papers VALUES (1);
            INSERT INTO institutions VALUES (1, 'legacy');
            INSERT INTO paper_institutions VALUES (1, 1, 'Legacy', 'KR', 'review');
        """)
        conn.close()

    def complete_base(self, db):
        connection = sqlite3.connect(db)
        try:
            logical_sha256 = migrator.logical_digest(connection)
            schema_version = migrator._schema_name(connection)
        finally:
            connection.close()
        registry = bib.affiliation_registry.load_registry(bib.REGISTRY_PATH)
        return {
            "database": str(db),
            "sha256": migrator.digest(db),
            "logical_sha256": logical_sha256,
            "schema_version": schema_version,
            "generation": 0,
            "registry_sha256": bib._registry_digest(),
            "event_head": registry["event_head"],
            "policy_version": registry["policy_version"],
            "source_sha256": registry["source_sha256"],
        }

    def test_projector_fault_rolls_back_schema_but_keeps_verified_backup(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "legacy.sqlite3"
            self.legacy_db(db)
            original_hash = migrator.digest(db)
            base = Path(directory) / "base.json"
            base.write_text(json.dumps(self.complete_base(db)), encoding="utf-8")
            with patch.object(bib, "project_affiliation_registry", side_effect=RuntimeError("fault")):
                with self.assertRaisesRegex(RuntimeError, "fault"):
                    migrator.migrate(db, execute=True, base_receipt=base)
            self.assertEqual(migrator.digest(db), original_hash)
            conn = sqlite3.connect(db)
            try:
                self.assertFalse(bib.is_latest_affiliation_schema(conn))
            finally:
                conn.close()
            backup = db.with_suffix(db.suffix + ".pre-affiliation-2.sqlite3")
            backup_conn = sqlite3.connect(backup)
            try:
                self.assertEqual(
                    backup_conn.execute("SELECT normalized_name FROM institutions").fetchall(),
                    [("legacy",)],
                )
                self.assertEqual(
                    backup_conn.execute("PRAGMA quick_check").fetchone()[0], "ok"
                )
            finally:
                backup_conn.close()

    def test_bad_base_receipt_fails_before_backup_or_schema_change(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "legacy.sqlite3"
            self.legacy_db(db)
            base = Path(directory) / "base.json"
            receipt = self.complete_base(db)
            receipt["sha256"] = "wrong"
            base.write_text(json.dumps(receipt))
            with self.assertRaisesRegex(RuntimeError, "database hash mismatch"):
                migrator.migrate(db, execute=True, base_receipt=base)
            self.assertFalse(db.with_suffix(db.suffix + ".pre-affiliation-2.sqlite3").exists())

    def test_rollback_rejects_tampered_backup_before_replacing_database(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "legacy.sqlite3"
            self.legacy_db(db)
            backup = db.with_suffix(db.suffix + ".pre-affiliation-2.sqlite3")
            backup.write_bytes(b"not sqlite")
            receipt = migrator.receipt_path(db, "migrate")
            receipt.write_text(json.dumps({"backup": str(backup),
                                           "backup_sha256": hashlib.sha256(b"other").hexdigest()}))
            before = migrator.digest(db)
            with self.assertRaisesRegex(RuntimeError, "receipt/hash mismatch"):
                migrator.rollback(db)
            self.assertEqual(migrator.digest(db), before)
    def test_hash_only_base_receipt_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "legacy.sqlite3"
            self.legacy_db(db)
            receipt = Path(directory) / "base.json"
            receipt.write_text(json.dumps({"sha256": migrator.digest(db)}), encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError, "required provenance"):
                migrator.migrate(db, execute=True, base_receipt=receipt)
    def test_backup_includes_committed_nonempty_wal_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "legacy.sqlite3"
            self.legacy_db(db)
            writer = sqlite3.connect(db)
            try:
                self.assertEqual(writer.execute("PRAGMA journal_mode=WAL").fetchone()[0], "wal")
                writer.execute("INSERT INTO papers VALUES (2)")
                writer.commit()
                self.assertTrue(Path(str(db) + "-wal").stat().st_size > 0)
                base = Path(directory) / "base.json"
                base.write_text(json.dumps(self.complete_base(db)), encoding="utf-8")
                receipt = migrator.migrate(db, execute=True, base_receipt=base)
            finally:
                writer.close()
            backup = sqlite3.connect(receipt["backup"])
            try:
                self.assertEqual(backup.execute("SELECT paper_id FROM papers ORDER BY paper_id").fetchall(),
                                 [(1,), (2,)])
                self.assertEqual(backup.execute("PRAGMA quick_check").fetchone()[0], "ok")
                self.assertEqual(migrator.logical_digest(backup), receipt["base_logical_sha256"])
            finally:
                backup.close()

    def test_rollback_rejects_current_result_mismatch_before_replacing_database(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "legacy.sqlite3"
            self.legacy_db(db)
            base = Path(directory) / "base.json"
            base.write_text(json.dumps(self.complete_base(db)), encoding="utf-8")
            receipt = migrator.migrate(db, execute=True, base_receipt=base)
            current = sqlite3.connect(db)
            try:
                current.execute(
                    "UPDATE affiliation_registry_metadata SET migration_receipt_id='tampered'")
                current.commit()
            finally:
                current.close()
            before = migrator.digest(db)
            with self.assertRaisesRegex(RuntimeError, "current database"):
                migrator.rollback(db)
            self.assertEqual(migrator.digest(db), before)

    def test_rollback_quarantines_stale_wal_and_shm_sidecars(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "legacy.sqlite3"
            self.legacy_db(db)
            base = Path(directory) / "base.json"
            base.write_text(json.dumps(self.complete_base(db)), encoding="utf-8")
            migrator.migrate(db, execute=True, base_receipt=base)
            for suffix in ("-wal", "-shm"):
                Path(str(db) + suffix).write_bytes(b"")
            migrator.rollback(db)
            self.assertFalse(Path(str(db) + "-wal").exists())
            self.assertFalse(Path(str(db) + "-shm").exists())
            self.assertFalse(any(Path(directory).glob(".*.rollback-quarantine.*")))
    def test_receipt_crash_keeps_migration_and_audit_in_one_committed_boundary(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "legacy.sqlite3"
            self.legacy_db(db)
            base = Path(directory) / "base.json"
            base.write_text(json.dumps(self.complete_base(db)), encoding="utf-8")
            sidecar = migrator.receipt_path(db, "migrate")
            with patch.object(migrator, "_atomic_json", side_effect=RuntimeError("publish fault")):
                with self.assertRaisesRegex(RuntimeError, "publish fault"):
                    migrator.migrate(db, execute=True, base_receipt=base)
            self.assertFalse(sidecar.exists())
            conn = sqlite3.connect(db)
            try:
                self.assertTrue(bib.is_latest_affiliation_schema(conn))
                receipt_id = conn.execute(
                    "SELECT migration_receipt_id FROM affiliation_registry_metadata "
                    "WHERE singleton=1").fetchone()[0]
                audit = conn.execute(
                    "SELECT receipt_id,report_json FROM affiliation_migration_audit").fetchone()
                self.assertEqual(audit[0], receipt_id)
                self.assertEqual(json.loads(audit[1])["receipt_id"], receipt_id)
            finally:
                conn.close()

    def test_already_latest_missing_receipt_is_reconstructed_from_audit(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "legacy.sqlite3"
            self.legacy_db(db)
            base = Path(directory) / "base.json"
            base.write_text(json.dumps(self.complete_base(db)), encoding="utf-8")
            original = migrator.migrate(db, execute=True, base_receipt=base)
            sidecar = migrator.receipt_path(db, "migrate")
            sidecar.unlink()
            recovered = migrator.migrate(db, execute=True, base_receipt=None)
            self.assertEqual(recovered, json.loads(sidecar.read_text(encoding="utf-8")))
            self.assertEqual(recovered["receipt_id"], original["receipt_id"])
            self.assertEqual(recovered["result_logical_sha256"], original["result_logical_sha256"])
            self.assertEqual(recovered["result_sha256"], migrator.digest(db))
            before = sidecar.read_bytes()
            existing = migrator.migrate(db, execute=True, base_receipt=None)
            self.assertTrue(existing["already_latest"])
            self.assertEqual(existing["receipt_id"], recovered["receipt_id"])
            self.assertEqual(sidecar.read_bytes(), before)

    def test_missing_receipt_recovery_rejects_tampered_audit_or_metadata_provenance(self):
        for target, statement, error in (
                ("audit", "UPDATE affiliation_migration_audit SET registry_sha256='tampered'",
                 "migration audit mismatch"),
                ("metadata", "UPDATE affiliation_registry_metadata "
                 "SET migration_receipt_id='tampered' WHERE singleton=1",
                 "metadata receipt id is invalid")):
            with self.subTest(target=target), tempfile.TemporaryDirectory() as directory:
                db = Path(directory) / "legacy.sqlite3"
                self.legacy_db(db)
                base = Path(directory) / "base.json"
                base.write_text(json.dumps(self.complete_base(db)), encoding="utf-8")
                migrator.migrate(db, execute=True, base_receipt=base)
                sidecar = migrator.receipt_path(db, "migrate")
                sidecar.unlink()
                conn = sqlite3.connect(db)
                try:
                    conn.execute(statement)
                    conn.commit()
                finally:
                    conn.close()
                with self.assertRaisesRegex(RuntimeError, error):
                    migrator.migrate(db, execute=True, base_receipt=None)
                self.assertFalse(sidecar.exists())
    def test_stale_sidecar_is_replaced_after_rollback_remigration_publish_fault(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "legacy.sqlite3"
            self.legacy_db(db)
            base = Path(directory) / "base.json"
            base.write_text(json.dumps(self.complete_base(db)), encoding="utf-8")
            migrator.migrate(db, execute=True, base_receipt=base)
            sidecar = migrator.receipt_path(db, "migrate")
            migrator.rollback(db)
            stale = json.loads(sidecar.read_text(encoding="utf-8"))
            stale["result_sha256"] = "0" * 64
            sidecar.write_text(json.dumps(stale), encoding="utf-8")
            base.write_text(json.dumps(self.complete_base(db)), encoding="utf-8")
            with patch.object(migrator, "_atomic_json", side_effect=RuntimeError("publish fault")):
                with self.assertRaisesRegex(RuntimeError, "publish fault"):
                    migrator.migrate(db, execute=True, base_receipt=base)
            recovered = migrator.migrate(db, execute=True, base_receipt=None)
            self.assertEqual(recovered, json.loads(sidecar.read_text(encoding="utf-8")))
            self.assertNotEqual(recovered["result_sha256"], "0" * 64)

    def test_missing_receipt_recovery_rejects_embedded_base_sha_tamper(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "legacy.sqlite3"
            self.legacy_db(db)
            base = Path(directory) / "base.json"
            base.write_text(json.dumps(self.complete_base(db)), encoding="utf-8")
            migrator.migrate(db, execute=True, base_receipt=base)
            sidecar = migrator.receipt_path(db, "migrate")
            sidecar.unlink()
            conn = sqlite3.connect(db)
            try:
                receipt_id, report_json = conn.execute(
                    "SELECT receipt_id,report_json FROM affiliation_migration_audit").fetchone()
                report = json.loads(report_json)
                report["base_sha256"] = "0" * 64
                conn.execute(
                    "UPDATE affiliation_migration_audit SET report_json=? WHERE receipt_id=?",
                    (json.dumps(report, sort_keys=True, separators=(",", ":")), receipt_id))
                conn.commit()
            finally:
                conn.close()
            with self.assertRaisesRegex(RuntimeError, "migration audit report is invalid"):
                migrator.migrate(db, execute=True, base_receipt=None)
            self.assertFalse(sidecar.exists())

    def test_incomplete_wal_checkpoint_fails_closed(self):
        connection = MagicMock()
        connection.execute.return_value.fetchone.return_value = (1, 3, 2)
        with self.assertRaisesRegex(RuntimeError, "checkpoint did not complete"):
            migrator._checkpoint_fully(connection)

    def test_real_wal_reader_prevents_complete_checkpoint(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "wal.sqlite3"
            writer = sqlite3.connect(db)
            reader = None
            try:
                writer.execute("PRAGMA journal_mode=WAL")
                writer.execute("CREATE TABLE sample (value INTEGER)")
                writer.execute("INSERT INTO sample VALUES (1)")
                writer.commit()
                reader = sqlite3.connect(db)
                reader.execute("BEGIN")
                self.assertEqual(
                    reader.execute("SELECT value FROM sample").fetchall(), [(1,)])
                writer.execute("INSERT INTO sample VALUES (2)")
                writer.commit()
                with self.assertRaisesRegex(
                        RuntimeError, "checkpoint did not complete"):
                    migrator._checkpoint_fully(writer)
            finally:
                if reader is not None:
                    reader.close()
                writer.close()

    def test_busy_wal_migration_recovers_receipt_after_reader_releases(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "legacy.sqlite3"
            self.legacy_db(db)
            writer = sqlite3.connect(db)
            writer.execute("PRAGMA journal_mode=WAL")
            writer.close()
            base = Path(directory) / "base.json"
            base.write_text(json.dumps(self.complete_base(db)), encoding="utf-8")
            reader = sqlite3.connect(db)
            reader.execute("BEGIN")
            self.assertEqual(
                reader.execute("SELECT paper_id FROM papers").fetchall(), [(1,)])
            try:
                with self.assertRaisesRegex(
                        RuntimeError, "checkpoint did not complete"):
                    migrator.migrate(db, execute=True, base_receipt=base)
            finally:
                reader.close()
            sidecar = migrator.receipt_path(db, "migrate")
            self.assertFalse(sidecar.exists())
            connection = sqlite3.connect(db)
            try:
                self.assertTrue(bib.is_latest_affiliation_schema(connection))
                self.assertEqual(
                    connection.execute(
                        "SELECT COUNT(*) FROM affiliation_migration_audit"
                    ).fetchone()[0], 1)
            finally:
                connection.close()
            recovered = migrator.migrate(
                db, execute=True, base_receipt=None)
            self.assertTrue(sidecar.exists())
            self.assertEqual(recovered["receipt_id"], json.loads(
                sidecar.read_text(encoding="utf-8"))["receipt_id"])

    def test_builder_and_migration_share_exclusive_writer_lock(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "bibliography.sqlite3"
            descriptor = migrator.acquire_lock(db)
            try:
                with self.assertRaisesRegex(RuntimeError, "writer lock busy"):
                    bib.build([], db, skip_zotero=True, offline=True)
            finally:
                bib.affiliation_registry.release_bibliography_writer_lock(
                    db, descriptor)
            self.assertTrue(migrator.lock_path(db).exists())

    def test_receipt_recovery_excludes_builder_until_sidecar_is_durable(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "legacy.sqlite3"
            self.legacy_db(db)
            base = Path(directory) / "base.json"
            base.write_text(json.dumps(self.complete_base(db)), encoding="utf-8")
            migrator.migrate(db, execute=True, base_receipt=base)
            sidecar = migrator.receipt_path(db, "migrate")
            sidecar.unlink()
            original_atomic_json = migrator._atomic_json
            builder_attempted = False

            def publish_while_probing_writer(path, value):
                nonlocal builder_attempted
                if path == sidecar:
                    builder_attempted = True
                    with self.assertRaisesRegex(RuntimeError, "writer lock busy"):
                        bib.build([], db, skip_zotero=True, offline=True)
                original_atomic_json(path, value)

            with patch.object(migrator, "_atomic_json",
                              side_effect=publish_while_probing_writer):
                recovered = migrator.migrate(
                    db, execute=True, base_receipt=None)
            self.assertTrue(builder_attempted)
            self.assertEqual(
                recovered, json.loads(sidecar.read_text(encoding="utf-8")))
            self.assertTrue(migrator.lock_path(db).exists())

    def test_builder_cli_reports_lock_contention_as_exit_five(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "bibliography.sqlite3"
            db.touch()
            descriptor = migrator.acquire_lock(db)
            try:
                with patch.object(bib, "load_entries", return_value=[]), \
                     patch.object(sys, "argv", [
                         "build_bibliography_db.py", "--output", str(db),
                         "--no-email",
                     ]):
                    self.assertEqual(bib.main(), 5)
            finally:
                bib.affiliation_registry.release_bibliography_writer_lock(
                    db, descriptor)
