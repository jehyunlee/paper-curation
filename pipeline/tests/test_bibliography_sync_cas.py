from contextlib import nullcontext
import fcntl
import hashlib
import json
import os
import signal
import subprocess
import shutil
import sqlite3
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

PIPELINE_DIR = Path(__file__).resolve().parents[1]
if str(PIPELINE_DIR) not in sys.path:
    sys.path.insert(0, str(PIPELINE_DIR))

import sync_bibliography_db as sync
import run_update_force as update


class BibliographySyncCASTests(unittest.TestCase):
    def setUp(self):
        self.authority_patch = patch.object(sync, "AUTHORITY_RPC", self.authority_rpc)
        self.authority_patch.start()
        self.addCleanup(self.authority_patch.stop)
        self.git_patch = patch.object(
            sync, "_git_provenance", return_value={
                "git_revision": "test-revision",
                "git_blobs": {
                    target: f"test-blob-{index}"
                    for index, target in enumerate(sync._GIT_TARGETS)
                },
            })
        self.git_patch.start()
        self.addCleanup(self.git_patch.stop)

    @staticmethod
    def authority_rpc(action, owner):
        if action == "acquire":
            return {"status": "ok", "lease": {
                **owner, "fence_token": 1, "authority_host_uuid": "test-host",
                "authority_boot_id": "test-boot",
            }}
        return {"status": "ok"}
    def make_latest_db(self, path):
        connection = sqlite3.connect(path)
        connection.execute(
            "CREATE TABLE affiliation_registry_metadata ("
            "singleton INTEGER PRIMARY KEY,schema_version TEXT,registry_sha256 TEXT,"
            "event_head TEXT,policy_version TEXT,source_sha256 TEXT,"
            "migration_receipt_id TEXT,registry_contract_version TEXT,"
            "event_contract_version TEXT,country_map_version TEXT,"
            "country_map_sha256 TEXT,evidence_oracle_version TEXT,"
            "evidence_oracle_sha256 TEXT,ledger_head TEXT,cohort_version TEXT,"
            "cohort_sha256 TEXT)")
        connection.execute(
            "INSERT INTO affiliation_registry_metadata VALUES "
            "(1,'affiliation-3','registry','event','policy','source','receipt',"
            "'registry-contract','event-contract','country-map','country-digest',"
            "'oracle','oracle-digest','ledger','cohort','cohort-digest')")
        connection.commit()
        connection.close()
        return path
    def make_fresh_db(self, path):
        self.make_latest_db(path)
        metadata = {
            "schema_version": "affiliation-3",
            "registry_sha256": "registry",
            "event_head": "event",
            "policy_version": "policy",
            "source_sha256": "source",
        }
        receipt = sync._fresh_schema_origin_receipt(metadata)
        connection = sqlite3.connect(path)
        connection.execute(
            "UPDATE affiliation_registry_metadata SET migration_receipt_id=?",
            (receipt["receipt_id"],))
        connection.commit()
        connection.close()
        return path
    def add_migration_audit(self, path, receipt):
        connection = sqlite3.connect(path)
        connection.execute(
            "CREATE TABLE affiliation_migration_audit ("
            "receipt_id TEXT,operation TEXT,base_generation INTEGER,"
            "base_logical_sha256 TEXT,result_logical_sha256 TEXT,"
            "registry_sha256 TEXT,schema_from TEXT,schema_to TEXT,"
            "backup_path TEXT,backup_sha256 TEXT,started_at TEXT,"
            "finished_at TEXT,report_json TEXT)")
        report = {
            key: receipt[key] for key in (
                "base_generation", "base_sha256", "base_logical_sha256",
                "registry_sha256", "event_head", "policy_version",
                "source_sha256", "schema_from", "schema_to")
        }
        report["receipt_id"] = receipt["receipt_id"]
        connection.execute(
            "INSERT INTO affiliation_migration_audit VALUES "
            "(?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (receipt["receipt_id"], receipt["operation"],
             receipt["base_generation"], receipt["base_logical_sha256"],
             receipt["result_logical_sha256"], receipt["registry_sha256"],
             receipt["schema_from"], receipt["schema_to"],
             receipt.get("backup", "backup.sqlite3"),
             receipt.get("backup_sha256", "f" * 64),
             receipt.get("started_at", "2026-08-08T00:00:00Z"),
             receipt.get("finished_at", "2026-08-08T00:01:00Z"),
             json.dumps(report)))
        connection.commit()
        connection.close()

    def migration_receipt(self):
        return {
            "operation": "migrate", "receipt_id": "receipt",
            "base_generation": 0, "base_sha256": "base-file",
            "base_logical_sha256": "base-logical",
            "result_sha256": "migration-file",
            "result_logical_sha256": "migration-logical",
            "schema_from": "legacy", "schema_to": "affiliation-3",
            "registry_sha256": "registry", "event_head": "event",
            "policy_version": "policy", "source_sha256": "source",
        }

    def receipt_loader(self, db):
        path = sync.migrator.receipt_path(db, "migrate")
        path.write_text("{}", encoding="utf-8")
        return patch.object(
            sync, "_load_current_migration_receipt",
            return_value=({}, path, "receipt-sha"))
    def authority_fields(self):
        return {
            "lease_protocol": sync.LEASE_PROTOCOL_VERSION,
            "fence_token": 1,
            "authority_host_uuid": "test-host",
            "authority_boot_id": "test-boot",
            "owner_run_id": "test-run",
            "owner_writer_uuid": "test-writer",
            "owner_client_host_uuid": "test-client",
        }

    def authority_lease(self):
        return nullcontext(self.authority_fields())

    def complete_manifest(self, *, generation=0, sha256="file-digest",
                          logical_sha256="logical-digest",
                          schema_version="affiliation-3"):
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
            "registry_contract_version": "registry-contract",
            "event_contract_version": "event-contract",
            "country_map_version": "country-map",
            "country_map_sha256": "country-digest",
            "evidence_oracle_version": "oracle",
            "evidence_oracle_sha256": "oracle-digest",
            "ledger_head": "ledger",
            "cohort_version": "cohort",
            "cohort_sha256": "cohort-digest",
            "relationship_set_sha256": "relationship-digest",
            "sql_contract_sha256": "sql-digest",
            "strict_result_sha256": "strict-digest",
            "git_revision": "revision",
            "git_blobs": {target: "blob" for target in sync._GIT_TARGETS},
            "lease_protocol": sync.LEASE_PROTOCOL_VERSION,
            "fence_token": 1,
            "authority_host_uuid": "test-host",
            "authority_boot_id": "test-boot",
            "owner_run_id": "test-run",
            "owner_writer_uuid": "test-writer",
            "owner_client_host_uuid": "test-client",
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
            self.assertEqual(manifest["schema_version"], "affiliation-3")
            self.assertEqual(manifest["migration_receipt_id"], "receipt")
    def test_local_authority_transport_avoids_self_ssh(self):
        with tempfile.TemporaryDirectory() as directory:
            authority = Path(directory) / "bibliography.sqlite3"
            authority.write_bytes(b"authority")
            destination = Path(directory) / "copy"
            with patch.object(sync, "LOCAL_DB", authority), \
                 patch.object(sync, "REMOTE_DB", str(authority)), \
                 patch.object(sync, "run") as run:
                sync._copy_from_authority(str(authority), destination)
                sync.remote("true")
            self.assertEqual(destination.read_bytes(), b"authority")
            run.assert_called_once_with(
                ["/bin/sh", "-c", "true"], capture=False,
                timeout=sync.AUTHORITY_RPC_TIMEOUT_SECONDS)
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
    def test_strict_affiliation_bindings_require_all_immutable_roles(self):
        manifest = self.complete_manifest(generation=7)
        artifact_data = {
            "cohort": b'{"cohort":true}\n',
            "decisions": b'{"decisions":[]}\n',
            "ledger": b'{"event":"closed"}\n',
            "generation_descriptor": b'{"generation":"strict"}\n',
        }
        manifest["strict_affiliation_generation"] = True
        manifest["affiliation_artifacts"] = {
            role: {
                "sha256": hashlib.sha256(data).hexdigest(),
                "object": sync._artifact_object(
                    manifest["generation"], role, hashlib.sha256(data).hexdigest()),
            }
            for role, data in artifact_data.items()
        }
        sync._validate_manifest(manifest)
        manifest["affiliation_artifacts"].pop("ledger")
        with self.assertRaisesRegex(RuntimeError, "roles are incomplete"):
            sync._validate_manifest(manifest)

    def test_strict_affiliation_declared_binding_rejects_missing_hash_or_object(self):
        manifest = self.complete_manifest(generation=7)
        manifest["strict_affiliation_generation"] = True
        manifest["affiliation_artifacts"] = {
            role: {
                "sha256": "a" * 64,
                "object": sync._artifact_object(7, role, "a" * 64),
            }
            for role in sync.AFFILIATION_ARTIFACT_ROLES
        }
        manifest["affiliation_artifacts"]["decisions"].pop("sha256")
        with self.assertRaisesRegex(RuntimeError, "binding is invalid: decisions"):
            sync._validate_manifest(manifest)
    def test_strict_affiliation_artifacts_stage_byte_identically(self):
        artifact_data = {
            "cohort": b'{"cohort":true}\n',
            "decisions": b'{"decisions":[]}\n',
            "ledger": b'{"ledger":"head"}\n',
            "generation_descriptor": b'{"generation":"strict"}\n',
        }
        manifest = self.complete_manifest(generation=9)
        manifest["strict_affiliation_generation"] = True
        manifest["affiliation_artifacts"] = {
            role: {
                "sha256": hashlib.sha256(data).hexdigest(),
                "object": sync._artifact_object(
                    manifest["generation"], role,
                    hashlib.sha256(data).hexdigest()),
            }
            for role, data in artifact_data.items()
        }
        remote = {
            binding["object"]: artifact_data[role]
            for role, binding in manifest["affiliation_artifacts"].items()
        }
        with tempfile.TemporaryDirectory() as directory, patch.object(
                sync, "_copy_from_authority",
                side_effect=lambda source, target: target.write_bytes(
                    remote[source])):
            staged = sync._stage_artifacts(manifest, Path(directory))
            sync._validate_artifact_equality(manifest, staged)
            self.assertEqual(
                {role: path.read_bytes() for role, path in staged.items()},
                artifact_data,
            )
            staged["decisions"].write_bytes(b"tampered\n")
            with self.assertRaisesRegex(
                    RuntimeError, "artifact equality mismatch: decisions"):
                sync._validate_artifact_equality(manifest, staged)

    def test_strict_affiliation_descriptor_is_installed_last(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            staged = {
                role: root / f"staged-{role}"
                for role in sync.AFFILIATION_ARTIFACT_ROLES
            }
            destinations = {
                role: root / "installed" / role
                for role in sync.AFFILIATION_ARTIFACT_ROLES
            }
            for path in staged.values():
                path.write_bytes(b"artifact")
            calls = []
            with patch.object(
                    sync.os, "replace",
                    side_effect=lambda source, target: calls.append(
                        (Path(source), Path(target)))):
                sync._install_artifacts_descriptor_last(
                    staged, destinations)
            self.assertEqual(
                [source for source, _ in calls],
                [staged[role] for role in (
                    "cohort", "decisions", "ledger",
                    "generation_descriptor")],
            )
            self.assertEqual(
                calls[-1],
                (staged["generation_descriptor"],
                 destinations["generation_descriptor"]),
            )
    def test_fresh_schema_origin_receipt_is_content_derived_and_stable(self):
        metadata = {
            "schema_version": "affiliation-3",
            "registry_sha256": "registry",
            "event_head": "event",
            "policy_version": "policy",
            "source_sha256": "source",
        }
        receipt = sync._fresh_schema_origin_receipt(metadata)
        self.assertEqual(
            receipt["receipt_id"],
            sync._fresh_schema_origin_receipt({
                key: metadata[key] for key in reversed(metadata)
            })["receipt_id"])
        self.assertNotEqual(receipt["receipt_id"], "fresh-schema")
        manifest = {**metadata, "migration_receipt_id": receipt["receipt_id"]}
        sync._validate_fresh_schema_receipt(receipt, manifest)
        receipt["event_head"] = "tampered"
        with self.assertRaisesRegex(RuntimeError, "fresh-schema origin receipt"):
            sync._validate_fresh_schema_receipt(receipt, manifest)

    def test_fresh_schema_origin_sidecar_is_constructed_and_reused(self):
        with tempfile.TemporaryDirectory() as directory:
            db = self.make_fresh_db(Path(directory) / "bibliography.sqlite3")
            with patch.object(sync, "LOCAL_DB", db):
                manifest = sync.local_manifest()
                receipt, path, digest = sync._load_current_origin_receipt(manifest)
                loaded, loaded_path, loaded_digest = (
                    sync._load_current_origin_receipt(manifest))
            self.assertEqual(receipt, loaded)
            self.assertEqual(path, loaded_path)
            self.assertEqual(digest, loaded_digest)
            self.assertEqual(receipt["receipt_id"], manifest["migration_receipt_id"])
            self.assertTrue(path.exists())
    def test_fresh_schema_origin_rotates_when_registry_provenance_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            db = self.make_fresh_db(Path(directory) / "bibliography.sqlite3")
            with patch.object(sync, "LOCAL_DB", db):
                first = sync.local_manifest()
                sync._load_current_origin_receipt(first)
                connection = sqlite3.connect(db)
                connection.execute(
                    "UPDATE affiliation_registry_metadata SET registry_sha256=?,"
                    "event_head=?,migration_receipt_id=?",
                    ("registry-r2", "event-r2", sync._fresh_schema_origin_receipt({
                        **first, "registry_sha256": "registry-r2",
                        "event_head": "event-r2",
                    })["receipt_id"]))
                connection.commit()
                connection.close()
                second = sync.local_manifest()
                _, path, _ = sync._load_current_origin_receipt(second)
            self.assertNotEqual(
                first["migration_receipt_id"], second["migration_receipt_id"])
            self.assertTrue(path.exists())

    def test_push_rejects_changed_sidecar_under_unchanged_origin_id(self):
        with tempfile.TemporaryDirectory() as directory:
            db = self.make_fresh_db(Path(directory) / "bibliography.sqlite3")
            with patch.object(sync, "LOCAL_DB", db):
                manifest = sync.local_manifest()
            base = Path(directory) / "base.json"
            expected = {
                **manifest, "migration_receipt_sha256": "synchronized-sha",
                "migration_receipt_object": (
                    f"{sync.GENERATIONS}/{0:020d}-"
                    "synchronized-sha.migration.json"),
                "object": (
                    f"{sync.GENERATIONS}/{0:020d}-"
                    f"{manifest['logical_sha256']}.sqlite3"),
            }
            expected.update(self.authority_fields())
            base.write_text(sync.canonical_manifest(expected), encoding="utf-8")
            sidecar = Path(directory) / "changed.json"
            sidecar.write_text("changed", encoding="utf-8")
            with patch.object(sync, "LOCAL_DB", db), \
                 patch.object(sync, "_ensure_publishable"), \
                 patch.object(sync, "_load_current_origin_receipt",
                              return_value=({}, sidecar, sync.sha(sidecar))), \
                 patch.object(sync, "run") as run:
                with self.assertRaisesRegex(RuntimeError, "sidecar differs"):
                    sync.push(base)
            run.assert_not_called()

    def test_push_snapshot_contends_with_every_local_writer(self):
        with tempfile.TemporaryDirectory() as directory:
            db = self.make_fresh_db(Path(directory) / "bibliography.sqlite3")
            with sync.bibliography_writer_lock(db):
                with self.assertRaisesRegex(RuntimeError, "writer lock busy"):
                    with sync.bibliography_lock(db, "writer", timeout=0):
                        pass

    def test_changed_migration_origin_requires_bound_controlled_remigration(self):
        with tempfile.TemporaryDirectory() as directory:
            db = self.make_latest_db(Path(directory) / "bibliography.sqlite3")
            registry_sha = "1" * 64
            source_sha = "2" * 64
            expected = {
                **self.complete_manifest(generation=3, schema_version="legacy"),
                "sha256": "a" * 64,
                "logical_sha256": "b" * 64,
                "restored_schema_version": "legacy",
                "requires_controlled_remigration": True,
                "base_generation": 2,
                "base_sha256": "d" * 64,
                "base_logical_sha256": "e" * 64,
                "object": (
                    f"{sync.GENERATIONS}/{3:020d}-{'b' * 64}.sqlite3"),
                "registry_sha256": registry_sha,
                "source_sha256": source_sha,
            }
            receipt = {
                "operation": "migrate",
                "database": str(db),
                "backup": str(Path(directory) / "backup.sqlite3"),
                "backup_sha256": "c" * 64,
                "base_generation": expected["generation"],
                "base_sha256": expected["sha256"],
                "base_logical_sha256": expected["logical_sha256"],
                "registry_sha256": registry_sha,
                "event_head": "event",
                "policy_version": "policy",
                "source_sha256": source_sha,
                "schema_from": "legacy",
                "schema_version": "affiliation-3",
                "schema_to": "affiliation-3",
                "started_at": "2026-08-08T00:00:00Z",
                "finished_at": "2026-08-08T00:01:00Z",
                "issues": [],
                "result_logical_sha256": sync._logical_sha(db),
            }
            receipt["receipt_id"] = sync.migrator._receipt_id(receipt)
            connection = sqlite3.connect(db)
            connection.execute(
                "UPDATE affiliation_registry_metadata SET "
                "migration_receipt_id=?,registry_sha256=?,source_sha256=?",
                (receipt["receipt_id"], registry_sha, source_sha))
            connection.commit()
            connection.close()
            receipt["result_logical_sha256"] = sync._logical_sha(db)
            self.add_migration_audit(db, receipt)
            connection = sqlite3.connect(db)
            connection.execute(
                "UPDATE affiliation_migration_audit SET report_json=? "
                "WHERE receipt_id=?",
                (json.dumps(receipt, sort_keys=True, separators=(",", ":")),
                 receipt["receipt_id"]))
            connection.commit()
            connection.close()
            with patch.object(sync, "LOCAL_DB", db):
                manifest = sync.local_manifest()
                receipt["result_sha256"] = manifest["sha256"]
                sync._validate_origin_transition(
                    expected, manifest, receipt, "new-receipt-digest")
                sidecar = sync.migrator.receipt_path(db, "migrate")
                sidecar.write_text(json.dumps(receipt), encoding="utf-8")
                base = Path(directory) / "rollback.base.json"
                base.write_text(
                    sync.canonical_manifest(expected), encoding="utf-8")
                with patch.object(sync, "_ensure_publishable"), \
                     patch.object(sync, "_copy_to_authority"), \
                     patch.object(sync, "remote"), \
                     patch.object(sync.uuid, "uuid4",
                                  return_value=Mock(hex="controlled")):
                    published = sync.push(base)
                self.assertEqual(published["generation"], 4)
                self.assertEqual(
                    published["migration_receipt_id"], receipt["receipt_id"])
                tampered = {**receipt, "result_sha256": "0" * 64}
                with self.assertRaisesRegex(
                        RuntimeError, "does not bind the local result"):
                    sync._validate_origin_transition(
                        expected, manifest, tampered, "tampered-digest")
                audited_field_tamper = {**receipt, "backup": "other-backup"}
                with self.assertRaisesRegex(
                        RuntimeError, "exactly match immutable audit"):
                    sync._validate_origin_transition(
                        expected, manifest, audited_field_tamper,
                        "tampered-audit-field")
                ordinary = dict(expected)
                ordinary.pop("requires_controlled_remigration")
                with self.assertRaisesRegex(
                        RuntimeError, "changed without fresh rotation"):
                    sync._validate_origin_transition(
                        ordinary, manifest, receipt, "new-receipt-digest")
                connection = sqlite3.connect(db)
                connection.execute(
                    "CREATE TABLE post_migration_projection(marker TEXT NOT NULL)")
                connection.execute(
                    "INSERT INTO post_migration_projection VALUES ('strict-final')")
                connection.commit()
                connection.close()
                strict_manifest = sync.local_manifest()
                self.assertNotEqual(
                    strict_manifest["logical_sha256"],
                    receipt["result_logical_sha256"])
                strict_manifest["strict_affiliation_generation"] = True
                strict_manifest["affiliation_artifacts"] = {
                    role: {
                        "sha256": "a" * 64,
                        "object": sync._artifact_object(
                            strict_manifest["generation"], role, "a" * 64),
                    }
                    for role in sync.AFFILIATION_ARTIFACT_ROLES
                }
                sync._validate_origin_transition(
                    ordinary, strict_manifest, receipt,
                    "new-receipt-digest")
                complete_report = {
                    key: value for key, value in receipt.items()
                    if key != "result_sha256"
                }
                for shape in ("missing", "extra"):
                    with self.subTest(audit_shape=shape):
                        malformed = dict(complete_report)
                        if shape == "missing":
                            malformed.pop("backup")
                        else:
                            malformed["unexpected"] = "field"
                        malformed["receipt_id"] = sync.migrator._receipt_id(
                            malformed)
                        connection = sqlite3.connect(db)
                        connection.execute(
                            "UPDATE affiliation_migration_audit "
                            "SET receipt_id=?,report_json=? WHERE receipt_id=?",
                            (malformed["receipt_id"], json.dumps(
                                malformed, sort_keys=True, separators=(",", ":")),
                             receipt["receipt_id"]))
                        connection.commit()
                        connection.close()
                        malformed_sidecar = {
                            **malformed,
                            "result_sha256": receipt["result_sha256"],
                        }
                        with self.assertRaisesRegex(
                                RuntimeError, "incomplete immutable audit"):
                            sync._verify_complete_migration_receipt(
                                malformed_sidecar, manifest, db)
                        connection = sqlite3.connect(db)
                        connection.execute(
                            "UPDATE affiliation_migration_audit "
                            "SET receipt_id=?,report_json=? WHERE receipt_id=?",
                            (receipt["receipt_id"], json.dumps(
                                complete_report, sort_keys=True,
                                separators=(",", ":")),
                             malformed["receipt_id"]))
                        connection.commit()
                        connection.close()
    def test_fresh_schema_push_changed_generation_and_pull(self):
        with tempfile.TemporaryDirectory() as directory:
            directory_path = Path(directory)
            source = self.make_fresh_db(directory_path / "source.sqlite3")
            remote_db = directory_path / "remote.sqlite3"
            shutil.copyfile(source, remote_db)
            generations = str(remote_db) + ".generations"
            manifest_path = str(remote_db) + ".manifest.json"
            lock_path = str(remote_db) + ".publish.lock"
            with patch.object(sync, "LOCAL_DB", source):
                initial = sync.local_manifest()
                receipt, receipt_path, receipt_digest = (
                    sync._load_current_origin_receipt(initial))
            base_manifest = {
                **initial,
                "migration_receipt_sha256": receipt_digest,
                "migration_receipt_object": (
                    f"{generations}/{0:020d}-{receipt_digest}.migration.json"),
                "object": (
                    f"{generations}/{0:020d}-"
                    f"{initial['logical_sha256']}.sqlite3"),
            }
            base_manifest.update(self.authority_fields())
            Path(generations).mkdir()
            shutil.copyfile(source, base_manifest["object"])
            shutil.copyfile(receipt_path, base_manifest["migration_receipt_object"])
            Path(manifest_path).write_text(
                sync.canonical_manifest(base_manifest), encoding="utf-8")
            source.with_suffix(".base.json").write_text(
                sync.canonical_manifest(base_manifest), encoding="utf-8")
            patches = (
                patch.object(sync, "REMOTE_DB", str(remote_db)),
                patch.object(sync, "MANIFEST", manifest_path),
                patch.object(sync, "LOCK", lock_path),
                patch.object(sync, "GENERATIONS", generations),
                patch.object(sync, "_authority_is_local", return_value=True),
                patch.object(sync, "_ensure_publishable"),
            )
            with patches[0], patches[1], patches[2], patches[3], patches[4], patches[5], \
                 patch.object(sync, "LOCAL_DB", source):
                first = sync.push(None)
                connection = sqlite3.connect(source)
                connection.execute("CREATE TABLE later_projection (value TEXT)")
                connection.commit()
                connection.close()
                second = sync.push(None)
            destination = directory_path / "destination.sqlite3"
            with patches[0], patches[1], patches[2], patches[3], patches[4], \
                 patch.object(sync, "LOCAL_DB", destination):
                with sync.bibliography_writer_lock(destination):
                    with self.assertRaisesRegex(RuntimeError, "writer lock busy"):
                        sync.pull()
                    self.assertFalse(destination.exists())

                real_ensure = sync._ensure_installable_pull
                calls = 0

                def require_remigration(manifest):
                    nonlocal calls
                    calls += 1
                    if calls == 2:
                        sync.migrator._atomic_json(sync._remigration_marker(), {
                            "operation": "remigration_required",
                            "manifest_generation": second["generation"],
                            "migration_receipt_id": second["migration_receipt_id"],
                            "created_at": second["updated_at"],
                        })
                    return real_ensure(manifest)

                with patch.object(
                        sync, "_ensure_installable_pull",
                        side_effect=require_remigration):
                    with self.assertRaisesRegex(
                            RuntimeError, "remigration required"):
                        sync.pull()
                self.assertFalse(destination.exists())
                sync._remigration_marker().unlink()
                pulled = sync.pull()
            self.assertEqual(first["migration_receipt_id"], second["migration_receipt_id"])
            self.assertNotEqual(first["logical_sha256"], second["logical_sha256"])
            self.assertEqual(pulled, second)
            self.assertTrue(sync.migrator.receipt_path(
                destination, "fresh-schema").exists())

    def test_tampered_fresh_schema_origin_sidecar_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            db = self.make_fresh_db(Path(directory) / "bibliography.sqlite3")
            with patch.object(sync, "LOCAL_DB", db):
                manifest = sync.local_manifest()
                path = sync._fresh_schema_receipt_path()
                path.write_text('{"receipt_id":"tampered"}', encoding="utf-8")
                with self.assertRaisesRegex(RuntimeError, "fresh-schema origin receipt"):
                    sync._load_current_origin_receipt(manifest)

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
    def test_receipt_provenance_allows_later_generation_with_immutable_audit(self):
        with tempfile.TemporaryDirectory() as directory:
            db = self.make_latest_db(Path(directory) / "bibliography.sqlite3")
            receipt = self.migration_receipt()
            self.add_migration_audit(db, receipt)
            connection = sqlite3.connect(db)
            connection.execute("CREATE TABLE later_projection (value TEXT)")
            connection.execute("INSERT INTO later_projection VALUES ('reviewed')")
            connection.execute(
                "UPDATE affiliation_registry_metadata SET registry_sha256=?,"
                "event_head=?,policy_version=?,source_sha256=?",
                ("registry-r2", "event-r2", "policy-r2", "source-r2"))
            connection.commit()
            connection.close()
            receipt_path = sync.migrator.receipt_path(db, "migrate")
            receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
            with patch.object(sync, "LOCAL_DB", db):
                manifest = sync.local_manifest()
                loaded, _, _ = sync._load_current_migration_receipt(manifest)
            self.assertEqual(loaded, receipt)
            self.assertEqual(manifest["registry_sha256"], "registry-r2")
            self.assertEqual(manifest["migration_receipt_id"], receipt["receipt_id"])
            self.assertNotEqual(receipt["result_sha256"], manifest["sha256"])
    def test_tampered_local_receipt_provenance_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            db = self.make_latest_db(Path(directory) / "bibliography.sqlite3")
            receipt = self.migration_receipt()
            self.add_migration_audit(db, receipt)
            receipt["event_head"] = "tampered"
            sync.migrator.receipt_path(db, "migrate").write_text(
                json.dumps(receipt), encoding="utf-8")
            with patch.object(sync, "LOCAL_DB", db):
                with self.assertRaisesRegex(RuntimeError, "DB migration audit receipt mismatch"):
                    sync._load_current_migration_receipt(sync.local_manifest())

    def test_pull_accepts_later_generation_and_rejects_tampered_audit(self):
        with tempfile.TemporaryDirectory() as directory:
            directory_path = Path(directory)
            source = self.make_latest_db(directory_path / "source.sqlite3")
            receipt = self.migration_receipt()
            self.add_migration_audit(source, receipt)
            connection = sqlite3.connect(source)
            connection.execute("CREATE TABLE later_projection (value TEXT)")
            connection.execute(
                "UPDATE affiliation_registry_metadata SET registry_sha256=?,"
                "event_head=?,policy_version=?,source_sha256=?",
                ("registry-r2", "event-r2", "policy-r2", "source-r2"))
            connection.commit()
            connection.close()
            receipt_file = directory_path / "receipt.json"
            receipt_file.write_text(json.dumps(receipt), encoding="utf-8")
            with patch.object(sync, "LOCAL_DB", source):
                manifest = sync.local_manifest()
            manifest.update({
                "generation": 3,
                "migration_receipt_sha256": sync.sha(receipt_file),
                "migration_receipt_object": (
                    f"{sync.GENERATIONS}/{3:020d}-{sync.sha(receipt_file)}.migration.json"),
                "object": f"{sync.GENERATIONS}/{3:020d}-{manifest['logical_sha256']}.sqlite3",
            })
            manifest.update(self.authority_fields())
            payload = sync.canonical_manifest(manifest)

            def transport(command, **_kwargs):
                source_name, destination = command[-2], Path(command[-1])
                if source_name.endswith(".manifest.json"):
                    destination.write_text(payload, encoding="utf-8")
                elif source_name.endswith(".migration.json"):
                    shutil.copyfile(receipt_file, destination)
                else:
                    shutil.copyfile(source, destination)
                return Mock()

            destination = directory_path / "destination.sqlite3"
            with patch.object(sync, "LOCAL_DB", destination), \
                 patch.object(sync, "run", side_effect=transport):
                self.assertEqual(sync.pull(), manifest)
            connection = sqlite3.connect(source)
            connection.execute(
                "UPDATE affiliation_migration_audit SET registry_sha256='tampered'")
            connection.commit()
            connection.close()
            manifest["sha256"] = sync.sha(source)
            manifest["logical_sha256"] = sync._logical_sha(source)
            manifest["object"] = (
                f"{sync.GENERATIONS}/{3:020d}-{manifest['logical_sha256']}.sqlite3")
            payload = sync.canonical_manifest(manifest)
            with patch.object(sync, "LOCAL_DB", directory_path / "tampered.sqlite3"), \
                 patch.object(sync, "run", side_effect=transport):
                with self.assertRaisesRegex(RuntimeError, "does not match DB audit"):
                    sync.pull()

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
    def test_hard_stop_allows_newer_normal_generation(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "bibliography.sqlite3"
            marker = sync.migrator.marker_path(db)
            marker.write_text(json.dumps({
                "manifest_generation": 3,
            }), encoding="utf-8")
            with patch.object(sync, "LOCAL_DB", db):
                sync._ensure_pull_allowed({"generation": 4})
                with self.assertRaisesRegex(RuntimeError, "remigration required"):
                    sync._ensure_pull_allowed({
                        "generation": 3,
                        "requires_controlled_remigration": True,
                    })
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
            self.assertEqual(run.call_count, 5)


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
                with self.assertRaisesRegex(RuntimeError, "affiliation-3 metadata is missing"):
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
                with self.assertRaisesRegex(RuntimeError, "CAS conflict: canonical manifest changed"):
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
                "schema_to": "affiliation-3",
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
                "schema_to": "affiliation-3",
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
            **self.complete_manifest(generation=1),
            "sha256": "a" * 64,
            "logical_sha256": "b" * 64,
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
                "schema_to": "affiliation-3",
            }
            with patch.object(sync, "LOCAL_DB", db):
                with self.assertRaisesRegex(RuntimeError, "lacks migration audit"):
                    sync._verify_migration_audit(
                        receipt, self.complete_manifest(), db)
class BibliographySyncFlockLeaseTests(unittest.TestCase):
    def test_live_local_writer_excludes_and_stable_path_survives(self):
        with tempfile.TemporaryDirectory() as directory:
            database = Path(directory) / "bibliography.sqlite3"
            lock = sync.bibliography_writer_lock_path(database)
            descriptor = os.open(lock, os.O_CREAT | os.O_RDWR, 0o600)
            try:
                fcntl.flock(descriptor, fcntl.LOCK_EX)
                with self.assertRaisesRegex(RuntimeError, "writer lock busy"):
                    with sync.bibliography_lock(database, "writer", timeout=0):
                        pass
                self.assertTrue(lock.exists())
            finally:
                fcntl.flock(descriptor, fcntl.LOCK_UN)
                os.close(descriptor)
            with sync.bibliography_lock(database, "writer", timeout=0):
                self.assertTrue(lock.exists())

    def test_sigkill_releases_kernel_flock_without_removing_stable_file(self):
        with tempfile.TemporaryDirectory() as directory:
            database = Path(directory) / "bibliography.sqlite3"
            lock = sync.bibliography_writer_lock_path(database)
            child = subprocess.Popen([
                sys.executable, "-c",
                "import fcntl,os,sys,time; f=os.open(sys.argv[1],os.O_CREAT|os.O_RDWR,0o600); "
                "fcntl.flock(f,fcntl.LOCK_EX); print('locked', flush=True); time.sleep(60)",
                str(lock),
            ], stdout=subprocess.PIPE, text=True)
            self.assertEqual(child.stdout.readline().strip(), "locked")
            os.kill(child.pid, signal.SIGKILL)
            child.wait(timeout=5)
            child.stdout.close()
            with sync.bibliography_lock(database, "writer", timeout=1):
                self.assertTrue(lock.exists())

    def test_authority_lease_polls_then_returns_higher_fence(self):
        owner = {"owner_run_id": "run", "owner_writer_uuid": "writer",
                 "owner_client_host_uuid": "client"}
        responses = iter([
            {"status": "busy"},
            {"status": "ok", "lease": {**owner, "fence_token": 8,
                                       "authority_host_uuid": "host",
                                       "authority_boot_id": "boot"}},
            {"status": "ok"},
        ])
        with patch.object(sync, "_lease_owner", return_value=owner), \
             patch.object(sync, "_authority_rpc", side_effect=lambda *_: next(responses)), \
             patch.object(sync.time, "sleep"):
            with sync.authority_lease() as lease:
                self.assertEqual(lease["fence_token"], 8)
                self.assertEqual(lease["lease_protocol"], sync.LEASE_PROTOCOL_VERSION)

    def test_stale_or_rebooted_fence_is_rejected_before_manifest_command(self):
        owner = {
            "owner_run_id": "run", "owner_writer_uuid": "writer",
            "owner_client_host_uuid": "client", "authority_boot_id": "new-boot",
            "fence_token": 9,
            "authority_host_uuid": "host",
        }
        with patch.object(sync, "remote",
                          side_effect=subprocess.CalledProcessError(74, ["ssh"])):
            with self.assertRaises(subprocess.CalledProcessError):
                sync._authority_commit("echo should-not-commit", owner)

    def test_pull_rejects_manifest_race_before_install(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "bibliography.sqlite3"
            manifest = {
                "database": "bibliography.sqlite3", "generation": 1, "sha256": "db",
                "logical_sha256": "logical", "schema_version": "legacy",
                "registry_sha256": "registry", "event_head": "event",
                "policy_version": "policy", "source_sha256": "source",
                "migration_receipt_id": "receipt",
                "migration_receipt_sha256": "1c5e693fde3f8917588cee744dd0eab51df2000657b27faa350179c272e9be22",
                "updated_at": "2026-08-08T00:00:00Z",
                "lease_protocol": sync.LEASE_PROTOCOL_VERSION, "fence_token": 1,
                "authority_boot_id": "boot", "owner_run_id": "run",
                "authority_host_uuid": "host",
                "owner_writer_uuid": "writer", "owner_client_host_uuid": "client",
                "registry_contract_version": "registry-contract",
                "event_contract_version": "event-contract",
                "country_map_version": "country-map",
                "country_map_sha256": "country-digest",
                "evidence_oracle_version": "oracle",
                "evidence_oracle_sha256": "oracle-digest",
                "ledger_head": "ledger", "cohort_version": "cohort",
                "cohort_sha256": "cohort-digest",
                "relationship_set_sha256": "relationship-digest",
                "sql_contract_sha256": "sql-digest",
                "strict_result_sha256": "strict-digest",
                "git_revision": "revision",
                "git_blobs": {target: "blob" for target in sync._GIT_TARGETS},
                "object": f"{sync.GENERATIONS}/00000000000000000001-logical.sqlite3",
                "migration_receipt_object": (
                    f"{sync.GENERATIONS}/00000000000000000001-"
                    "1c5e693fde3f8917588cee744dd0eab51df2000657b27faa350179c272e9be22.migration.json"
                ),
                "requires_controlled_remigration": True, "restored_schema_version": "legacy",
                "base_generation": 0, "base_sha256": "old-db",
                "base_logical_sha256": "old-logical",
                "generation_provenance": {
                    "git_revision": "test-revision", "registry_sha256": "registry",
                    "evidence_ledger_head": "event",
                },
            }
            copies = 0

            def copy(source, destination):
                nonlocal copies
                if source == sync.MANIFEST:
                    copies += 1
                    value = dict(manifest)
                    if copies == 2:
                        value["generation"] = 2
                    destination.write_text(sync.canonical_manifest(value), encoding="utf-8")
                elif source.endswith(".migration.json"):
                    destination.write_text('{"receipt_id":"receipt"}', encoding="utf-8")
                else:
                    destination.write_bytes(b"db")

            with patch.object(sync, "_copy_from_authority", side_effect=copy), \
                 patch.object(sync, "_ensure_installable_pull"), \
                 patch.object(
                     sync,
                     "sha",
                     side_effect=lambda path: (
                         "db" if Path(path).read_bytes() == b"db"
                         else "1c5e693fde3f8917588cee744dd0eab51df2000657b27faa350179c272e9be22"
                     ),
                 ), \
                 patch.object(sync, "_logical_sha", return_value="logical"), \
                 patch.object(sync, "_inspect_sqlite", return_value={}):
                with patch.object(sync, "LOCAL_DB", db):
                    with self.assertRaisesRegex(RuntimeError, "changed while pull"):
                        sync.pull()
    def test_authority_commit_is_fail_closed_after_heartbeat_failure(self):
        fenced = sync.Event()
        fenced.set()
        owner = {
            "_fenced": fenced, "fence_token": 2,
            "authority_host_uuid": "host", "authority_boot_id": "boot",
            "owner_run_id": "run", "owner_writer_uuid": "writer",
            "owner_client_host_uuid": "client",
        }
        with patch.object(sync, "remote") as remote:
            with self.assertRaisesRegex(RuntimeError, "renewal fenced"):
                sync._authority_commit("false", owner)
        remote.assert_not_called()

    def test_manifest_rejects_missing_complete_affiliation_contract(self):
        manifest = {
            "database": "bibliography.sqlite3", "generation": 1,
            "sha256": "a" * 64, "logical_sha256": "b" * 64,
            "schema_version": "affiliation-3",
        }
        with self.assertRaisesRegex(RuntimeError, "required provenance"):
            sync._validate_manifest(manifest)
