"""Publish-contract tests for the bibliography CAS sync.

`test_bibliography_sync_cas.py` was deleted along with the affiliation
organisation registry it exercised, and the module's manifest contract kept
demanding that registry's artifacts — `registry_sha256`, `event_head`,
`ledger_head`, `policy_version`, the contract versions, the evidence oracle, the
cohort and the migration receipt. `--push` therefore died on
`KeyError: 'registry_sha256'` with nothing left to catch it.

These tests pin the contract that survives the registry: a manifest identifies a
build by its content digests, its SQL layout, the Git revision that produced it,
and the lease that owns the write. They are offline — no ssh, no network.
"""
import json
import sqlite3
import subprocess
import sys
import unittest
from pathlib import Path

# `sync_bibliography_db` imports its siblings by bare name, so the package
# directory has to be importable — the same shim the deleted CAS suite used.
PIPELINE_DIR = Path(__file__).resolve().parents[1]
if str(PIPELINE_DIR) not in sys.path:
    sys.path.insert(0, str(PIPELINE_DIR))

import sync_bibliography_db as sync

RETIRED_FIELDS = {
    "registry_sha256", "event_head", "ledger_head", "policy_version",
    "registry_contract_version", "event_contract_version",
    "evidence_oracle_version", "evidence_oracle_sha256",
    "cohort_version", "cohort_sha256", "relationship_set_sha256",
    "migration_receipt_id", "migration_receipt_sha256",
    "migration_receipt_object",
}


def make_db(path: Path) -> Path:
    """A database with the live bibliography layout."""
    conn = sqlite3.connect(path)
    conn.executescript(
        "CREATE TABLE papers (paper_id INTEGER PRIMARY KEY, slug TEXT,"
        " title TEXT, review_dir TEXT);"
        "CREATE TABLE institutions (institution_id INTEGER PRIMARY KEY,"
        " institution_name TEXT, normalized_name TEXT,"
        " country_name_en TEXT DEFAULT '');"
        "CREATE TABLE paper_institutions (paper_id INTEGER,"
        " institution_id INTEGER);"
        "INSERT INTO papers VALUES (1,'001_x','X','docs/papers/001_x');"
        "INSERT INTO institutions VALUES (1,'ETH Zurich','eth zurich',"
        " 'Switzerland');"
        "INSERT INTO paper_institutions VALUES (1,1);")
    conn.commit()
    conn.close()
    return path


class RequiredFieldTests(unittest.TestCase):
    """The contract must not ask for anything the registry used to supply."""

    def test_no_retired_registry_field_is_required(self):
        required = sync._required_manifest_fields()
        self.assertEqual(sorted(required & RETIRED_FIELDS), [])

    def test_rollback_adds_no_retired_field(self):
        required = sync._required_manifest_fields(rollback=True)
        self.assertEqual(sorted(required & RETIRED_FIELDS), [])

    def test_identity_and_ownership_stay_required(self):
        required = sync._required_manifest_fields()
        for field in ("database", "generation", "sha256", "logical_sha256",
                      "schema_version", "source_sha256", "sql_contract_sha256",
                      "git_revision", "git_blobs", "generation_provenance",
                      "lease_protocol", "fence_token", "object", "updated_at"):
            with self.subTest(field=field):
                self.assertIn(field, required)


class InspectTests(unittest.TestCase):
    """Identity comes from the file, not from a registry contract row."""

    def setUp(self):
        import tempfile
        self.dir = Path(tempfile.mkdtemp())
        self.db = make_db(self.dir / "bibliography.sqlite3")

    def test_reports_layout_and_content(self):
        metadata = sync._inspect_sqlite(self.db)
        self.assertEqual(metadata["schema_version"], "bibliography-1")
        self.assertEqual(len(metadata["source_sha256"]), 64)
        self.assertEqual(sorted(metadata), ["schema_version", "source_sha256"])

    def test_reports_no_retired_field(self):
        metadata = sync._inspect_sqlite(self.db)
        self.assertEqual(sorted(set(metadata) & RETIRED_FIELDS), [])

    def test_corruption_is_refused(self):
        broken = self.dir / "broken.sqlite3"
        broken.write_bytes(b"SQLite format 3\x00" + b"\xff" * 4096)
        with self.assertRaises(Exception):
            sync._inspect_sqlite(broken)

    def test_content_digest_tracks_content(self):
        before = sync._inspect_sqlite(self.db)["source_sha256"]
        conn = sqlite3.connect(self.db)
        conn.execute("INSERT INTO papers VALUES (2,'002_y','Y','d')")
        conn.commit()
        conn.close()
        self.assertNotEqual(sync._inspect_sqlite(self.db)["source_sha256"],
                            before)


class ProvenanceTests(unittest.TestCase):
    """Provenance binds a build to a revision that exists."""

    def test_binds_git_revision_and_digests(self):
        metadata = {"source_sha256": "a" * 64, "logical_sha256": "b" * 64}
        provenance = sync._generation_provenance(metadata, "c" * 40)
        self.assertEqual(provenance["git_revision"], "c" * 40)
        self.assertEqual(sorted(set(provenance) & RETIRED_FIELDS), [])

    def test_validation_rejects_a_revision_mismatch(self):
        manifest = {"git_revision": "c" * 40,
                    "generation_provenance": {"git_revision": "d" * 40}}
        with self.assertRaises(RuntimeError):
            sync._validate_generation_provenance(manifest)

    def test_validation_accepts_a_matching_revision(self):
        manifest = {"git_revision": "c" * 40,
                    "generation_provenance": {"git_revision": "c" * 40}}
        sync._validate_generation_provenance(manifest)


class GitTargetTests(unittest.TestCase):
    """Pinned blobs must be files that exist and are tracked."""

    def test_targets_are_not_empty(self):
        self.assertTrue(sync._GIT_TARGETS,
                        "an empty target set pins nothing and made every "
                        "manifest's git_blobs trivially valid")

    def test_every_target_is_tracked_in_git(self):
        root = Path(__file__).resolve().parents[2]
        for target in sync._GIT_TARGETS:
            with self.subTest(target=target):
                self.assertTrue((root / target).is_file())
                listed = subprocess.run(
                    ["git", "-C", str(root), "ls-files", "--error-unmatch",
                     target],
                    capture_output=True, text=True)
                self.assertEqual(listed.returncode, 0, listed.stderr.strip())

    def test_no_retired_registry_payload_is_pinned(self):
        for target in sync._GIT_TARGETS:
            self.assertNotIn("affiliation_registry", target)

    def test_pre_retirement_receipt_is_accepted(self):
        """A receipt from before the retirement pins files that are now gone.

        `.cache/bibliography.base.json` (generation 13) pins the three
        `affiliation_registry*` payloads. It is not corrupt, so push must not
        reject it — those blobs are simply from the other side of the boundary.
        """
        sync._validate_git_blobs({"git_blobs": {
            "pipeline/affiliation_registry.json": "a" * 40,
            "pipeline/affiliation_registry_baseline.json": "b" * 40,
            "pipeline/affiliation_registry_corrections.jsonl": "c" * 40}})

    def test_current_target_set_is_accepted(self):
        sync._validate_git_blobs(
            {"git_blobs": {t: "a" * 40 for t in sync._GIT_TARGETS}})

    def test_some_other_unexpected_set_is_refused(self):
        with self.assertRaises(RuntimeError):
            sync._validate_git_blobs(
                {"git_blobs": {"pipeline/whatever.py": "a" * 40}})

    def test_empty_or_malformed_blobs_are_refused(self):
        for blobs in ({}, None, "x", {"pipeline/x.py": ""}):
            with self.subTest(blobs=blobs):
                with self.assertRaises(RuntimeError):
                    sync._validate_git_blobs({"git_blobs": blobs})


class ManifestRoundTripTests(unittest.TestCase):
    """A manifest this module builds is a manifest this module accepts."""

    def setUp(self):
        import tempfile
        self.dir = Path(tempfile.mkdtemp())
        self.db = make_db(self.dir / "bibliography.sqlite3")
        self._saved = sync.LOCAL_DB
        sync.LOCAL_DB = self.db

    def tearDown(self):
        sync.LOCAL_DB = self._saved

    def _manifest(self):
        manifest = sync.local_manifest()
        # Fields the push path fills once it owns the lease. The contract test
        # is about which names the manifest must carry, not about acquiring a
        # lease, so they are supplied here.
        manifest.update({
            "object": (f"{sync.GENERATIONS}/{manifest['generation']:020d}"
                       f"-{manifest['logical_sha256']}.sqlite3"),
            "lease_protocol": sync.LEASE_PROTOCOL_VERSION,
            "fence_token": 1,
            "authority_host_uuid": "host-uuid",
            "authority_boot_id": "boot-id",
            "owner_run_id": "run-id",
            "owner_writer_uuid": "writer-uuid",
            "owner_client_host_uuid": "client-uuid",
        })
        return manifest

    def test_local_manifest_carries_identity(self):
        manifest = self._manifest()
        self.assertEqual(manifest["database"], self.db.name)
        self.assertEqual(manifest["schema_version"], "bibliography-1")
        self.assertEqual(len(manifest["sha256"]), 64)
        self.assertEqual(len(manifest["logical_sha256"]), 64)
        self.assertTrue(manifest["sql_contract_sha256"])
        self.assertTrue(manifest["git_revision"])
        self.assertEqual(set(manifest["git_blobs"]), set(sync._GIT_TARGETS))

    def test_every_required_field_is_populated(self):
        manifest = self._manifest()
        missing = sorted(field for field in sync._required_manifest_fields()
                         if manifest.get(field) in (None, ""))
        self.assertEqual(missing, [])

    def test_validate_accepts_its_own_manifest(self):
        sync._validate_manifest(self._manifest())

    def test_validate_rejects_a_missing_field(self):
        manifest = self._manifest()
        del manifest["sql_contract_sha256"]
        with self.assertRaises(RuntimeError):
            sync._validate_manifest(manifest)

    def test_validate_rejects_foreign_git_blobs(self):
        manifest = self._manifest()
        manifest["git_blobs"] = {"pipeline/nope.py": "0" * 40}
        with self.assertRaises(RuntimeError):
            sync._validate_manifest(manifest)

    def test_manifest_is_json_serialisable(self):
        json.dumps(self._manifest(), sort_keys=True)


if __name__ == "__main__":
    unittest.main()
