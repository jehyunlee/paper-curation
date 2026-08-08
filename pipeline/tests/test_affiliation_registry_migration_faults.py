import hashlib
import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

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
