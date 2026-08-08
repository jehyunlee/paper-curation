import json
import subprocess
import shutil
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

PIPELINE_DIR = Path(__file__).resolve().parents[1]
if str(PIPELINE_DIR) not in sys.path:
    sys.path.insert(0, str(PIPELINE_DIR))

import sync_bibliography_db as sync
import run_update_force as update


class BibliographySyncCASTests(unittest.TestCase):
    def make_latest_db(self, path):
        connection = sqlite3.connect(path)
        connection.execute(
            "CREATE TABLE affiliation_registry_metadata ("
            "singleton INTEGER PRIMARY KEY,schema_version TEXT,registry_sha256 TEXT,"
            "event_head TEXT,policy_version TEXT,source_sha256 TEXT,"
            "migration_receipt_id TEXT)")
        connection.execute(
            "INSERT INTO affiliation_registry_metadata VALUES "
            "(1,'affiliation-2','registry','event','policy','source','receipt')")
        connection.commit()
        connection.close()
        return path

    def receipt_loader(self, db):
        path = sync.migrator.receipt_path(db, "migrate")
        path.write_text("{}", encoding="utf-8")
        return patch.object(
            sync, "_load_current_migration_receipt",
            return_value=({}, path, sync.sha(path)))

    def complete_manifest(self, *, generation=0, sha256="file-digest",
                          logical_sha256="logical-digest",
                          schema_version="affiliation-2"):
        return {
            "database": "bibliography.sqlite3",
            "generation": generation,
            "sha256": sha256,
            "logical_sha256": logical_sha256,
            "schema_version": schema_version,
            "registry_sha256": "registry",
            "event_head": "event",
            "policy_version": "policy",
            "source_sha256": "source",
            "migration_receipt_id": "receipt",
            "migration_receipt_sha256": "receipt-sha",
            "migration_receipt_object": (
                f"{sync.GENERATIONS}/{generation:020d}-receipt-sha.migration.json"),
            "updated_at": "2026-08-08T00:00:00Z",
            "object": (
                f"{sync.GENERATIONS}/{generation:020d}-{logical_sha256}.sqlite3"),
        }
    def test_local_manifest_hashes_exact_bytes_and_starts_at_generation_zero(self):
        with tempfile.TemporaryDirectory() as directory:
            db = self.make_latest_db(Path(directory) / "bibliography.sqlite3")
            with patch.object(sync, "LOCAL_DB", db), \
                 patch.object(sync.time, "strftime",
                              return_value="2026-08-08T00:00:00Z"):
                manifest = sync.local_manifest()
            self.assertEqual(manifest["generation"], 0)
            self.assertEqual(manifest["sha256"], sync.sha(db))
            self.assertEqual(manifest["logical_sha256"], sync._logical_sha(db))
            self.assertEqual(manifest["schema_version"], "affiliation-2")
            self.assertEqual(manifest["migration_receipt_id"], "receipt")
    def test_manifest_serialization_is_byte_identical_for_compare_and_write(self):
        manifest = {"sha256": "digest", "generation": 3, "updated_at": "fixed"}
        self.assertEqual(sync.canonical_manifest(manifest),
                         '{"generation":3,"sha256":"digest","updated_at":"fixed"}')
    def test_manifest_requires_content_addressed_migration_receipt(self):
        manifest = self.complete_manifest()
        sync._validate_manifest(manifest)
        manifest.pop("migration_receipt_object")
        with self.assertRaisesRegex(RuntimeError, "migration_receipt_object"):
            sync._validate_manifest(manifest)

    def test_bootstrap_refuses_to_fabricate_legacy_authority(self):
        with self.assertRaisesRegex(RuntimeError, "receipt-bound recovery"):
            sync.bootstrap()
    def test_push_rejects_missing_migration_receipt_before_transport(self):
        with tempfile.TemporaryDirectory() as directory:
            db = self.make_latest_db(Path(directory) / "bibliography.sqlite3")
            base = Path(directory) / "base.json"
            base.write_text(sync.canonical_manifest(self.complete_manifest()), encoding="utf-8")
            with patch.object(sync, "LOCAL_DB", db), \
                 patch.object(sync, "_ensure_publishable"), \
                 patch.object(sync, "run") as run:
                with self.assertRaisesRegex(RuntimeError, "missing local migration receipt"):
                    sync.push(base)
            run.assert_not_called()

    def test_bootstrap_binds_remote_affiliation_metadata(self):
        with patch.object(sync, "remote") as remote:
            with self.assertRaisesRegex(RuntimeError, "receipt-bound recovery"):
                sync.bootstrap()
        remote.assert_not_called()

    def test_seed_legacy_recovery_accepts_audited_pre_receipt_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            directory_path = Path(directory)
            db = self.make_latest_db(directory_path / "bibliography.sqlite3")
            backup = directory_path / "legacy.sqlite3"
            sqlite3.connect(backup).close()
            backup_logical = sync._logical_sha(backup)
            expected = self.complete_manifest(
                generation=0, sha256=sync.sha(db),
                logical_sha256=sync._logical_sha(db))
            expected.pop("migration_receipt_sha256")
            expected.pop("migration_receipt_object")
            base = directory_path / "base.json"
            base.write_text(sync.canonical_manifest(expected), encoding="utf-8")
            receipt_path = sync.migrator.receipt_path(db, "migrate")
            receipt_path.write_text(json.dumps({
                "operation": "migrate",
                "receipt_id": "receipt",
                "base_generation": 0,
                "base_sha256": sync.sha(backup),
                "base_logical_sha256": backup_logical,
                "backup": str(backup),
                "backup_sha256": sync.sha(backup),
                "schema_from": "legacy",
                "registry_sha256": "registry",
                "event_head": "event",
                "policy_version": "policy",
                "source_sha256": "source",
            }), encoding="utf-8")
            with patch.object(sync, "LOCAL_DB", db), \
                 patch.object(sync, "_ensure_publishable"), \
                 patch.object(sync, "_verify_migration_audit") as verify_audit, \
                 patch.object(sync, "run"), \
                 patch.object(sync, "remote"), \
                 patch.object(sync.uuid, "uuid4", return_value=Mock(hex="seed")), \
                 patch.object(sync.time, "strftime",
                              return_value="2026-08-08T00:00:00Z"):
                result = sync.seed_legacy_recovery(base)
            verify_audit.assert_called_once()
            self.assertEqual(result["generation"], 1)
            self.assertEqual(result["sha256"], sync.sha(backup))
            self.assertEqual(result["logical_sha256"], backup_logical)
            self.assertEqual(result["base_sha256"], expected["sha256"])
            self.assertTrue(result["requires_controlled_remigration"])
            self.assertEqual(result["operation"], "legacy_recovery_seed")
    def test_pull_of_published_rollback_writes_hard_stop_marker(self):
        with tempfile.TemporaryDirectory() as directory:
            directory_path = Path(directory)
            local_db = directory_path / "bibliography.sqlite3"
            remote_db = directory_path / "remote.sqlite3"
            sqlite3.connect(remote_db).close()
            receipt = directory_path / "receipt.json"
            receipt.write_text('{"receipt_id":"receipt"}', encoding="utf-8")
            logical = sync._logical_sha(remote_db)
            manifest = {
                **self.complete_manifest(
                    generation=8, sha256=sync.sha(remote_db),
                    logical_sha256=logical, schema_version="legacy"),
                "operation": "rollback",
                "base_generation": 7,
                "base_sha256": "base-file",
                "base_logical_sha256": "base-logical",
                "requires_controlled_remigration": True,
                "migration_receipt_id": "receipt",
                "migration_receipt_sha256": sync.sha(receipt),
                "restored_schema_version": "legacy",
            }
            manifest["migration_receipt_object"] = (
                f"{sync.GENERATIONS}/{manifest['generation']:020d}-"
                f"{manifest['migration_receipt_sha256']}.migration.json")

            def transport(command, **_kwargs):
                destination = Path(command[-1])
                source = command[-2]
                if source.endswith(sync.MANIFEST):
                    destination.write_text(
                        sync.canonical_manifest(manifest), encoding="utf-8")
                elif source.endswith(manifest["migration_receipt_object"]):
                    shutil.copyfile(receipt, destination)
                else:
                    shutil.copyfile(remote_db, destination)
                return Mock()

            with patch.object(sync, "LOCAL_DB", local_db), \
                 patch.object(sync, "run", side_effect=transport) as run:
                self.assertEqual(sync.pull(), manifest)
                marker = sync._remigration_marker()
                self.assertTrue(marker.exists())
                self.assertEqual(
                    json.loads(marker.read_text())["manifest_generation"], 8)
                with self.assertRaisesRegex(RuntimeError, "remigration required"):
                    sync.pull()
            self.assertEqual(run.call_count, 3)


    def test_push_rejects_missing_base_receipt_before_any_transport(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "bibliography.sqlite3"
            db.write_bytes(b"db")
            with patch.object(sync, "LOCAL_DB", db), \
                 patch.object(sync, "_ensure_publishable"), \
                 patch.object(sync, "run") as run:
                with self.assertRaisesRegex(RuntimeError, "stale/missing base receipt"):
                    sync.push(None)
            run.assert_not_called()

    def test_push_rejects_legacy_db_before_transport(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "bibliography.sqlite3"
            sqlite3.connect(db).close()
            with patch.object(sync, "LOCAL_DB", db), patch.object(sync, "run") as run:
                with self.assertRaisesRegex(RuntimeError, "affiliation-2 metadata is missing"):
                    sync.push(Path(directory) / "unused.json")
            run.assert_not_called()

    def test_push_accepts_rollback_base_after_controlled_remigration(self):
        with tempfile.TemporaryDirectory() as directory:
            db = self.make_latest_db(Path(directory) / "bibliography.sqlite3")
            base = Path(directory) / "base.json"
            expected = {
                **self.complete_manifest(
                    generation=1, schema_version="legacy"),
                "base_generation": 0,
                "base_sha256": "prior-file",
                "base_logical_sha256": "prior-logical",
                "restored_schema_version": "legacy",
                "requires_controlled_remigration": True,
            }
            base.write_text(sync.canonical_manifest(expected), encoding="utf-8")
            with patch.object(sync, "LOCAL_DB", db), \
                 patch.object(sync, "_ensure_publishable"), \
                 self.receipt_loader(db), \
                 patch.object(sync, "run"), \
                 patch.object(sync, "remote"), \
                 patch.object(sync.uuid, "uuid4",
                              return_value=Mock(hex="remigrated")):
                result = sync.push(base)
            self.assertEqual(result["generation"], 2)
            self.assertEqual(result["base_generation"], 1)
            self.assertNotIn("requires_controlled_remigration", result)
    def test_push_uses_unique_upload_names_and_advances_manifest_from_base(self):
        with tempfile.TemporaryDirectory() as directory:
            db = self.make_latest_db(Path(directory) / "bibliography.sqlite3")
            first_base = Path(directory) / "first.base.json"
            second_base = Path(directory) / "second.base.json"
            expected = self.complete_manifest(generation=7)
            first_base.write_text(sync.canonical_manifest(expected), encoding="utf-8")
            second_base.write_text(sync.canonical_manifest(expected), encoding="utf-8")
            run = Mock()
            remote = Mock()
            ids = [Mock(hex="first"), Mock(hex="second")]
            with patch.object(sync, "LOCAL_DB", db), \
                 patch.object(sync, "_ensure_publishable"), \
                 self.receipt_loader(db), \
                 patch.object(sync, "run", run), \
                 patch.object(sync, "remote", remote), \
                 patch.object(sync.uuid, "uuid4", side_effect=ids), \
                 patch.object(sync.time, "strftime", return_value="2026-08-08T00:00:00Z"):
                first = sync.push(first_base)
                second = sync.push(second_base)
            uploads = [call.args[0][3] for call in run.call_args_list]
            self.assertEqual(uploads, [
                sync.HOST + ":" + sync.REMOTE_DB + ".upload.first",
                sync.HOST + ":" + sync.REMOTE_DB + ".receipt.upload.first",
                sync.HOST + ":" + sync.REMOTE_DB + ".upload.second",
                sync.HOST + ":" + sync.REMOTE_DB + ".receipt.upload.second",
            ])
            self.assertNotEqual(uploads[0], uploads[2])
            self.assertEqual(first["generation"], 8)
            self.assertEqual(second["generation"], 8)
            self.assertEqual(json.loads(first_base.read_text()), first)
            self.assertIn("test -f " + sync.MANIFEST, remote.call_args_list[0].args[0])
            self.assertIn("exit 74", remote.call_args_list[0].args[0])
    def test_push_publishes_generation_before_advancing_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            db = self.make_latest_db(Path(directory) / "bibliography.sqlite3")
            base = Path(directory) / "base.json"
            base.write_text(sync.canonical_manifest(
                self.complete_manifest(generation=1)), encoding="utf-8")
            with patch.object(sync, "LOCAL_DB", db), patch.object(sync, "run"), \
                 patch.object(sync, "_ensure_publishable"), \
                 self.receipt_loader(db), \
                 patch.object(sync, "remote") as remote, \
                 patch.object(sync.uuid, "uuid4", return_value=Mock(hex="generation")):
                sync.push(base)
            script = remote.call_args.args[0]
            self.assertIn(".generations/", script)
            self.assertLess(
                script.index(sync.REMOTE_DB + ".upload.generation"),
                script.rindex("manifest.json"))

    def test_push_converts_remote_cas_conflict_to_safe_error_and_removes_upload(self):
        with tempfile.TemporaryDirectory() as directory:
            db = self.make_latest_db(Path(directory) / "bibliography.sqlite3")
            base = Path(directory) / "base.json"
            base.write_text(sync.canonical_manifest(
                self.complete_manifest(generation=0)), encoding="utf-8")
            remote = Mock(side_effect=subprocess.CalledProcessError(74, ["ssh"]))
            with patch.object(sync, "LOCAL_DB", db), \
                 patch.object(sync, "_ensure_publishable"), \
                 self.receipt_loader(db), \
                 patch.object(sync, "run"), \
                 patch.object(sync, "remote", remote), \
                 patch.object(sync.uuid, "uuid4", return_value=Mock(hex="conflict")):
                with self.assertRaisesRegex(RuntimeError, "CAS conflict or remote publish lock busy"):
                    sync.push(base)
            self.assertEqual(remote.call_count, 2)
            self.assertIn("rm -f " + sync.REMOTE_DB + ".upload.conflict", remote.call_args_list[1].args[0])

    def test_published_rollback_republishes_retained_object_under_cas(self):
        with tempfile.TemporaryDirectory() as directory:
            local_db = Path(directory) / "bibliography.sqlite3"
            sqlite3.connect(local_db).close()
            target_source = Path(directory) / "retained.sqlite3"
            sqlite3.connect(target_source).close()
            target_digest = sync.sha(target_source)
            target_logical = sync._logical_sha(target_source)
            retained = (
                f"{sync.GENERATIONS}/{2:020d}-{target_logical}.sqlite3")
            base = Path(directory) / "base.json"
            expected = self.complete_manifest(
                generation=5, sha256="current",
                logical_sha256="current-logical")
            expected["migration_receipt_id"] = "migration-receipt"
            migration_receipt = Path(directory) / "migration.json"
            migration_receipt.write_text(json.dumps({
                "operation": "migrate",
                "receipt_id": "migration-receipt",
                "base_sha256": target_digest,
                "base_generation": 2,
                "base_logical_sha256": target_logical,
                "result_sha256": expected["sha256"],
                "result_logical_sha256": expected["logical_sha256"],
                "schema_from": "legacy",
                "schema_to": "affiliation-2",
                "registry_sha256": "registry",
                "event_head": "event",
                "policy_version": "policy",
                "source_sha256": "source",
            }), encoding="utf-8")
            expected["migration_receipt_sha256"] = sync.sha(migration_receipt)
            expected["migration_receipt_object"] = (
                f"{sync.GENERATIONS}/{expected['generation']:020d}-"
                f"{expected['migration_receipt_sha256']}.migration.json")
            base.write_text(sync.canonical_manifest(expected), encoding="utf-8")

            def transport(command, **_kwargs):
                shutil.copyfile(target_source, Path(command[-1]))
                return Mock()

            remote = Mock(side_effect=[
                Mock(stdout=retained),
                Mock(stdout=""),
            ])
            with patch.object(sync, "LOCAL_DB", local_db), \
                 patch.object(sync, "_ensure_publishable"), \
                 patch.object(sync, "_verify_migration_audit"), \
                 patch.object(sync, "run", side_effect=transport), \
                 patch.object(sync, "remote", remote), \
                 patch.object(sync.time, "strftime",
                              return_value="2026-08-08T00:00:00Z"):
                result = sync.published_rollback(
                    2, base, migration_receipt)

            self.assertEqual(result["generation"], 6)
            self.assertEqual(result["rollback_of_generation"], 2)
            self.assertEqual(result["operation"], "rollback")
            self.assertEqual(result["schema_version"], "legacy")
            self.assertTrue(result["requires_controlled_remigration"])
            self.assertEqual(result["migration_receipt_id"], "migration-receipt")
            self.assertEqual(json.loads(base.read_text()), result)
            publish_script = remote.call_args_list[1].args[0]
            self.assertIn(sync.canonical_manifest(expected), publish_script)
            self.assertIn("cp " + retained, publish_script)
            self.assertIn(result["object"], publish_script)

    def test_published_rollback_rejects_non_older_target_without_transport(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "bibliography.sqlite3"
            sqlite3.connect(db).close()
            base = Path(directory) / "base.json"
            expected = self.complete_manifest(
                generation=3, sha256="current",
                logical_sha256="current-logical")
            expected["migration_receipt_id"] = "migration-receipt"
            migration_receipt = Path(directory) / "migration.json"
            migration_receipt.write_text(json.dumps({
                "operation": "migrate",
                "receipt_id": "migration-receipt",
                "base_sha256": "old",
                "base_generation": 0,
                "base_logical_sha256": "old-logical",
                "result_sha256": expected["sha256"],
                "result_logical_sha256": expected["logical_sha256"],
                "schema_from": "legacy",
                "schema_to": "affiliation-2",
                "registry_sha256": "registry",
                "event_head": "event",
                "policy_version": "policy",
                "source_sha256": "source",
            }), encoding="utf-8")
            expected["migration_receipt_sha256"] = sync.sha(migration_receipt)
            expected["migration_receipt_object"] = (
                f"{sync.GENERATIONS}/{expected['generation']:020d}-"
                f"{expected['migration_receipt_sha256']}.migration.json")
            base.write_text(sync.canonical_manifest(expected), encoding="utf-8")
            with patch.object(sync, "LOCAL_DB", db), \
                 patch.object(sync, "_ensure_publishable"), \
                 patch.object(sync, "remote") as remote:
                with self.assertRaisesRegex(RuntimeError, "older retained generation"):
                    sync.published_rollback(3, base, migration_receipt)
            remote.assert_not_called()

    def test_review_release_gate_never_pushes_after_strict_failure(self):
        calls = []

        def run_step(name, command, timeout):
            calls.append((name, command, timeout))
            if name == "check_bibliography_db":
                raise RuntimeError("strict validation failed")

        with self.assertRaisesRegex(RuntimeError, "strict validation failed"):
            update.run_bibliography_release_steps(run_step)

        self.assertEqual(
            [name for name, _command, _timeout in calls],
            ["build_bibliography_db", "check_bibliography_db"],
        )
    def test_manifest_rejects_hash_only_and_bad_logical_object_name(self):
        with self.assertRaisesRegex(RuntimeError, "required provenance"):
            sync._validate_manifest({"generation": 1, "sha256": "a" * 64})
        manifest = {
            "database": "bibliography.sqlite3", "generation": 1, "sha256": "a" * 64,
            "logical_sha256": "b" * 64, "schema_version": "affiliation-2",
            "registry_sha256": "registry", "event_head": "event",
            "policy_version": "policy", "source_sha256": "source",
            "migration_receipt_id": "receipt", "updated_at": "2026-08-08T00:00:00Z",
            "migration_receipt_sha256": "receipt-sha",
            "migration_receipt_object": (
                f"{sync.GENERATIONS}/{1:020d}-receipt-sha.migration.json"),
            "object": f"{sync.GENERATIONS}/1-{'b' * 64}.sqlite3",
        }
        with self.assertRaisesRegex(RuntimeError, "immutable object name"):
            sync._validate_manifest(manifest)
    def test_push_durably_reuses_verified_orphan_before_manifest_advance(self):
        with tempfile.TemporaryDirectory() as directory:
            db = self.make_latest_db(Path(directory) / "bibliography.sqlite3")
            base = Path(directory) / "base.json"
            base.write_text(sync.canonical_manifest(
                self.complete_manifest(generation=1)), encoding="utf-8")
            with patch.object(sync, "LOCAL_DB", db), patch.object(sync, "run"), \
                 patch.object(sync, "_ensure_publishable"), \
                 self.receipt_loader(db), \
                 patch.object(sync, "remote") as remote, \
                 patch.object(sync.uuid, "uuid4", return_value=Mock(hex="orphan")):
                sync.push(base)
            script = remote.call_args.args[0]
            self.assertIn("if test -e", script)
            self.assertIn(sync.REMOTE_DB + ".upload.orphan", script)
            self.assertIn('rm -f "$src"', script)
            self.assertIn("os.fsync", script)
            self.assertLess(script.index("os.fsync"), script.rindex("manifest.json"))

    def test_published_rollback_rejects_missing_current_db_audit(self):
        with tempfile.TemporaryDirectory() as directory:
            db = self.make_latest_db(Path(directory) / "bibliography.sqlite3")
            receipt = {
                "receipt_id": "receipt", "base_generation": 0,
                "base_logical_sha256": "base", "result_logical_sha256": "result",
                "registry_sha256": "registry", "schema_from": "legacy",
                "schema_to": "affiliation-2",
            }
            with patch.object(sync, "LOCAL_DB", db):
                with self.assertRaisesRegex(RuntimeError, "lacks migration audit"):
                    sync._verify_migration_audit(receipt, self.complete_manifest())
