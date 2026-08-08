import contextlib
import io
import json
import sqlite3
import sys
import tempfile
import unittest
import uuid
from pathlib import Path
from unittest.mock import patch

PIPELINE_DIR = Path(__file__).resolve().parents[1]
if str(PIPELINE_DIR) not in sys.path:
    sys.path.insert(0, str(PIPELINE_DIR))

import build_bibliography_db as bib
import check_bibliography_db as checker
import repair_bibliography_institutions as migrator
from lib import affiliation_registry


class AffiliationRegistryMigrationTests(unittest.TestCase):
    def make_registry_file(self, directory):
        snapshot = affiliation_registry.build_registry({
            "1": {"af_name": ["Reviewed Organization"], "af_country": ["KR"]},
            "2": {"af_name": ["Second Organization"], "af_country": ["KR"]},
        })
        path = Path(directory) / "registry.json"
        path.write_bytes(affiliation_registry.canonical_json_bytes(snapshot))
        return path, snapshot

    def make_legacy_db(self, path):
        conn = sqlite3.connect(path)
        conn.executescript("""
            CREATE TABLE papers (paper_id INTEGER PRIMARY KEY);
            CREATE TABLE institutions (institution_id INTEGER PRIMARY KEY, normalized_name TEXT);
            CREATE TABLE paper_institutions (
                institution_id INTEGER, paper_id INTEGER, raw_name TEXT,
                country_name TEXT, source TEXT);
            INSERT INTO papers VALUES (1);
            INSERT INTO institutions VALUES (1, 'legacy organization');
            INSERT INTO paper_institutions VALUES (1, 1, 'Unreviewed legacy organization', 'KR', 'review');
        """)
        conn.commit()
        conn.close()

    def make_base_receipt(self, db, registry_path, generation=0):
        path = Path(db).with_suffix(".base.json")
        connection = sqlite3.connect(db)
        try:
            logical_sha256 = migrator.logical_digest(connection)
            schema_version = migrator._schema_name(connection)
        finally:
            connection.close()
        snapshot = affiliation_registry.load_registry(registry_path)
        path.write_text(json.dumps({
            "database": str(db),
            "generation": generation,
            "sha256": migrator.digest(Path(db)),
            "logical_sha256": logical_sha256,
            "schema_version": schema_version,
            "registry_sha256": __import__("hashlib").sha256(
                Path(registry_path).read_bytes()).hexdigest(),
            "event_head": snapshot["event_head"],
            "policy_version": snapshot["policy_version"],
            "source_sha256": snapshot["source_sha256"],
        }), encoding="utf-8")
        return path

    def test_fresh_builder_creates_affiliation_2_projection(self):
        with tempfile.TemporaryDirectory() as directory:
            registry_path, _ = self.make_registry_file(directory)
            db = Path(directory) / "fresh.sqlite3"
            with patch.object(bib, "REGISTRY_PATH", registry_path):
                bib.build([], db, skip_zotero=True, offline=True)
            conn = sqlite3.connect(db)
            try:
                self.assertTrue(bib.is_latest_affiliation_schema(conn))
                self.assertEqual(conn.execute(
                    "SELECT schema_version FROM affiliation_registry_metadata").fetchone()[0],
                    "affiliation-2")
                self.assertEqual(conn.execute(
                    "SELECT COUNT(*) FROM affiliation_organizations").fetchone()[0], 2)
            finally:
                conn.close()

    def test_builder_rejects_legacy_db_but_controlled_migration_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            registry_path, _ = self.make_registry_file(directory)
            db = Path(directory) / "legacy.sqlite3"
            self.make_legacy_db(db)
            with patch.object(bib, "REGISTRY_PATH", registry_path):
                with self.assertRaisesRegex(RuntimeError, "requires controlled migration"):
                    bib.build([], db, skip_zotero=True, offline=True)
                receipt = migrator.migrate(
                    db, execute=True,
                    base_receipt=self.make_base_receipt(db, registry_path))
                second = migrator.migrate(db, execute=True, base_receipt=None)
            self.assertEqual(receipt["operation"], "migrate")
            self.assertTrue(Path(receipt["backup"]).exists())
            self.assertTrue(second["already_latest"])
            self.assertEqual(second["issues"], [])

    def test_migrate_rollback_remigrate_preserves_receipts_and_marker_lifecycle(self):
        with tempfile.TemporaryDirectory() as directory:
            registry_path, _ = self.make_registry_file(directory)
            db = Path(directory) / "recovery.sqlite3"
            self.make_legacy_db(db)
            with patch.object(bib, "REGISTRY_PATH", registry_path):
                first = migrator.migrate(
                    db, execute=True,
                    base_receipt=self.make_base_receipt(db, registry_path))
                rollback = migrator.rollback(db)
                marker = migrator.marker_path(db)
                self.assertTrue(marker.exists())
                self.assertEqual(rollback["schema_version"], "legacy")
                self.assertEqual(migrator.digest(db), first["backup_sha256"])
                second = migrator.migrate(
                    db, execute=True,
                    base_receipt=self.make_base_receipt(db, registry_path))
            self.assertFalse(marker.exists())
            self.assertEqual(len(second["result_sha256"]), 64)
            self.assertEqual(len(first["base_logical_sha256"]), 64)
            self.assertEqual(len(first["result_logical_sha256"]), 64)
            connection = sqlite3.connect(db)
            try:
                self.assertEqual(migrator.validate(connection), [])
                audit = connection.execute(
                    "SELECT base_logical_sha256,result_logical_sha256 "
                    "FROM affiliation_migration_audit ORDER BY finished_at DESC LIMIT 1"
                ).fetchone()
                self.assertEqual(
                    audit,
                    (second["base_logical_sha256"],
                     second["result_logical_sha256"]))
            finally:
                connection.close()

    def test_compatibility_schema_preserves_country_collisions_and_direct_edge_precedence(self):
        with tempfile.TemporaryDirectory() as directory:
            conn = sqlite3.connect(Path(directory) / "compatibility.sqlite3")
            conn.executescript(bib.SCHEMA + bib.AFFILIATION_SCHEMA)
            organizations = [
                ("child", "Shared Institute", "shared institute", "other", "US",
                 "United States", "domestic", "active", "event", 1),
                ("parent-a", "Parent A", "parent a", "other", "US",
                 "United States", "domestic", "active", "event", 1),
                ("parent-b", "Parent B", "parent b", "other", "GB",
                 "United Kingdom", "domestic", "active", "event", 1),
            ]
            conn.executemany(
                "INSERT INTO affiliation_organizations VALUES (?,?,?,?,?,?,?,?,?,?)",
                organizations,
            )
            conn.executemany(
                "INSERT INTO institutions "
                "(institution_name,normalized_name,country_name_en,organization_id,source) "
                "VALUES (?,?,?,?,?)",
                [
                    ("Shared Institute", "shared institute", "United States", "child", "review"),
                    ("Shared Institute", "shared institute", "United Kingdom", None, "review"),
                ],
            )
            institution_ids = [
                row[0] for row in conn.execute(
                    "SELECT institution_id FROM institutions ORDER BY institution_id")
            ]
            conn.executemany(
                "INSERT INTO institution_aliases "
                "(raw_name,normalized_alias,institution_id) VALUES (?,?,?)",
                [("Shared Inst.", "shared inst", institution_id)
                 for institution_id in institution_ids],
            )
            registry = {
                "organizations": [
                    {"organization_id": row[0], "canonical_name_en": row[1]}
                    for row in organizations
                ],
                "events": [{"timestamp": "2026-08-08T00:00:00Z"}],
                "relationships": [
                    {"relationship_id": "one", "subject_organization_id": "child",
                     "object_organization_id": "parent-a", "relationship_type": "part_of",
                     "status": "accepted", "validity_interval": {"start": "", "end": ""}},
                    {"relationship_id": "two", "subject_organization_id": "child",
                     "object_organization_id": "parent-b", "relationship_type": "part_of",
                     "status": "accepted", "validity_interval": {"start": "", "end": ""}},
                    {"relationship_id": "network", "subject_organization_id": "child",
                     "object_organization_id": "parent-b",
                     "relationship_type": "network_member_of", "status": "accepted",
                     "validity_interval": {"start": "", "end": ""}},
                ],
            }
            bib._project_compatibility_groups(conn, registry)
            child_group = conn.execute(
                "SELECT group_id FROM institutions WHERE organization_id='child'"
            ).fetchone()[0]
            self.assertIsNone(child_group)
            registry["relationships"][1]["relationship_type"] = "member_of"
            bib._project_compatibility_groups(conn, registry)
            child_group_name = conn.execute(
                "SELECT g.group_name FROM institutions i "
                "JOIN institution_groups g USING(group_id) "
                "WHERE i.organization_id='child'"
            ).fetchone()[0]
            self.assertEqual(child_group_name, "Parent A")
            registry["organizations"][0]["status"] = "proposed"
            bib._project_compatibility_groups(conn, registry)
            self.assertIsNone(conn.execute(
                "SELECT group_id FROM institutions WHERE organization_id='child'"
            ).fetchone()[0])
            conn.close()

    def test_ambiguous_alias_never_guesses_and_resolved_supersession_closes_pending_case(self):
        with tempfile.TemporaryDirectory() as directory:
            registry_path, snapshot = self.make_registry_file(directory)
            db = Path(directory) / "observations.sqlite3"
            conn = sqlite3.connect(db)
            conn.execute("CREATE TABLE papers (paper_id INTEGER PRIMARY KEY)")
            conn.execute("INSERT INTO papers VALUES (1)")
            with patch.object(bib, "REGISTRY_PATH", registry_path):
                bib.project_affiliation_registry(conn)
                reviewed = next(org for org in snapshot["organizations"]
                                if org["canonical_name_en"] == "Reviewed Organization")
                other = next(org for org in snapshot["organizations"]
                             if org["organization_id"] != reviewed["organization_id"])
                alias_id = reviewed["aliases"][0]["alias_id"]
                conn.execute("INSERT INTO affiliation_alias_candidates VALUES (?,?,?,?,?,?,?)",
                             (alias_id, other["organization_id"], "", "", 1.0,
                              "accepted", "duplicate-review"))
                bib.record_affiliation_observation(conn, 1,
                                                   {"raw_name": "Reviewed Organization", "source": "review"},
                                                   0, snapshot)
                self.assertEqual(conn.execute("SELECT resolution_status FROM observed_affiliations").fetchone()[0],
                                 "unseen")
                conn.execute("DELETE FROM affiliation_alias_candidates WHERE event_id='duplicate-review'")
                bib.record_affiliation_observation(conn, 1,
                                                   {"raw_name": "Reviewed Organization revised", "source": "review"},
                                                   0, snapshot)
                observations = conn.execute("SELECT observation_version,is_current,resolution_status FROM observed_affiliations ORDER BY observation_version").fetchall()
            conn.close()
            self.assertEqual(observations, [(1, 0, "superseded"), (2, 1, "unseen")])
    def test_resolved_supersession_closes_pending_but_retains_observation_history(self):
        with tempfile.TemporaryDirectory() as directory:
            registry_path, snapshot = self.make_registry_file(directory)
            conn = sqlite3.connect(Path(directory) / "resolved.sqlite3")
            conn.execute("CREATE TABLE papers (paper_id INTEGER PRIMARY KEY)")
            conn.execute("INSERT INTO papers VALUES (1)")
            with patch.object(bib, "REGISTRY_PATH", registry_path):
                bib.project_affiliation_registry(conn)
                bib.record_affiliation_observation(
                    conn, 1, {"raw_name": "Unreviewed Organization", "source": "review"}, 0, snapshot)
                bib.record_affiliation_observation(
                    conn, 1, {"raw_name": "Reviewed Organization", "source": "review"}, 0, snapshot)
            history = conn.execute(
                "SELECT observation_version,is_current,resolution_status "
                "FROM observed_affiliations ORDER BY observation_version").fetchall()
            pending = conn.execute(
                "SELECT status,active_observation_count,lifetime_observation_count "
                "FROM affiliation_pending_cases WHERE normalized_raw_name='unreviewed organization'"
            ).fetchone()
            conn.close()
            self.assertEqual(history, [(1, 0, "superseded"), (2, 1, "unseen")])
            self.assertEqual(pending, ("rejected", 0, 1))

    def test_removed_slot_is_superseded_and_not_current(self):
        with tempfile.TemporaryDirectory() as directory:
            registry_path, snapshot = self.make_registry_file(directory)
            conn = sqlite3.connect(Path(directory) / "removed.sqlite3")
            conn.executescript(bib.SCHEMA)
            conn.execute(
                "INSERT INTO papers (slug,title,review_dir) VALUES ('stable-paper','Paper','docs/papers/stable-paper')")
            with patch.object(bib, "REGISTRY_PATH", registry_path):
                bib.project_affiliation_registry(conn)
                slot_id = bib.record_affiliation_observation(
                    conn, 1, {"raw_name": "Unseen", "source": "review"}, 0,
                    snapshot, paper_key="stable-paper")
                bib.supersede_removed_affiliation_slots(
                    conn, 1, "stable-paper", set(), snapshot)
            self.assertEqual(conn.execute(
                "SELECT is_current,resolution_status FROM observed_affiliations "
                "WHERE observation_slot_id=?", (slot_id,)).fetchone(),
                (0, "superseded"))
            self.assertEqual(conn.execute(
                "SELECT active_observation_count FROM affiliation_pending_cases").fetchone()[0], 0)
            conn.close()
    def test_strict_checker_rejects_forged_registry_edge_and_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            registry_path, snapshot = self.make_registry_file(directory)
            db = Path(directory) / "forged.sqlite3"
            conn = sqlite3.connect(db)
            conn.executescript(bib.SCHEMA)
            conn.execute(
                "INSERT INTO papers (slug,title,review_dir) VALUES ('paper','Paper','docs/papers/paper')")
            with patch.object(bib, "REGISTRY_PATH", registry_path):
                bib.project_affiliation_registry(conn)
            first, second = [org["organization_id"] for org in snapshot["organizations"]]
            conn.execute(
                "INSERT INTO affiliation_relationships VALUES (?,?,?,?,?,?,?,?,?,?)",
                ("forged", first, second, "part_of", "", "", "accepted",
                 1.0, "forged", "registry"))
            conn.execute(
                "INSERT INTO affiliation_relationship_evidence VALUES (?,?)",
                ("forged", "forged-evidence"))
            conn.commit()
            conn.close()
            output = io.StringIO()
            with patch.object(checker.bib, "REGISTRY_PATH", registry_path), \
                 patch.object(sys, "argv", ["check_bibliography_db.py", "--db", str(db),
                                            "--registry", str(registry_path), "--strict"]), \
                 contextlib.redirect_stdout(output):
                self.assertEqual(checker.main(), 2)
            self.assertTrue(any("relationship projection mismatch" in issue
                                for issue in json.loads(output.getvalue())["issues"]))
    def test_strict_checker_detects_pending_count_invariant(self):
        with tempfile.TemporaryDirectory() as directory:
            registry_path, snapshot = self.make_registry_file(directory)
            db = Path(directory) / "check.sqlite3"
            conn = sqlite3.connect(db)
            conn.execute("CREATE TABLE papers (paper_id INTEGER PRIMARY KEY)")
            conn.execute("INSERT INTO papers VALUES (1)")
            with patch.object(bib, "REGISTRY_PATH", registry_path):
                bib.project_affiliation_registry(conn)
                bib.record_affiliation_observation(conn, 1, {"raw_name": "Unseen", "source": "review"}, 0, snapshot)
            conn.execute("PRAGMA ignore_check_constraints=ON")
            conn.execute("UPDATE affiliation_pending_cases SET active_observation_count=0")
            conn.execute("PRAGMA ignore_check_constraints=OFF")
            conn.commit()
            conn.close()
            output = io.StringIO()
            with patch.object(checker.bib, "REGISTRY_PATH", registry_path), \
                 patch.object(sys, "argv", ["check_bibliography_db.py", "--db", str(db), "--registry", str(registry_path), "--strict"]), \
                 contextlib.redirect_stdout(output):
                self.assertEqual(checker.main(), 2)
            report = json.loads(output.getvalue())
            self.assertFalse(report["ok"])
            self.assertTrue(any("pending status/count" in issue for issue in report["issues"]))
            self.assertTrue(any("pending active recount mismatch" in issue for issue in report["issues"]))
    def test_affiliation_ddl_rejects_invalid_canonical_states(self):
        conn = sqlite3.connect(":memory:")
        conn.executescript(bib.SCHEMA + bib.AFFILIATION_SCHEMA)
        conn.execute("PRAGMA foreign_keys=ON")
        with self.assertRaises(sqlite3.IntegrityError):
            conn.execute(
                "INSERT INTO affiliation_organizations VALUES (?,?,?,?,?,?,?,?,?,?)",
                ("invalid", "Invalid", "invalid", "institution", "", "",
                 "unknown", "active", "event", 1))
        conn.execute(
            "INSERT INTO affiliation_organizations VALUES (?,?,?,?,?,?,?,?,?,?)",
            ("org", "Organization", "organization", "other", "", "",
             "unknown", "active", "event", 1))
        with self.assertRaises(sqlite3.IntegrityError):
            conn.execute(
                "INSERT INTO affiliation_organization_redirects VALUES (?,?,?)",
                ("org", "org", "event"))
        with self.assertRaises(sqlite3.IntegrityError):
            conn.execute(
                "INSERT INTO affiliation_identifiers VALUES (?,?,?,?,?,?,?)",
                ("ror", "https://ror.org/example", "missing", "active", "", "", "evidence"))
        with self.assertRaises(sqlite3.IntegrityError):
            conn.execute(
                "INSERT INTO affiliation_relationships VALUES (?,?,?,?,?,?,?,?,?,?)",
                ("invalid-edge", "org", "org", "parent_of", "", "", "accepted",
                 1.0, "event", "registry"))
        with self.assertRaises(sqlite3.IntegrityError):
            conn.execute(
                "INSERT INTO affiliation_pending_cases "
                "(pending_id,normalized_raw_name,status,reason_code,first_seen_at,last_seen_at,"
                "lifetime_observation_count) VALUES (?,?,?,?,?,?,?)",
                ("invalid-pending", "unknown", "open", "unseen", "now", "now", 1))
        conn.close()

    def test_observation_ids_are_namespace_uuidv5_over_canonical_inputs(self):
        with tempfile.TemporaryDirectory() as directory:
            registry_path, snapshot = self.make_registry_file(directory)
            conn = sqlite3.connect(":memory:")
            conn.executescript(bib.SCHEMA)
            conn.execute(
                "INSERT INTO papers (paper_id,slug,title,review_dir) VALUES (1,?,?,?)",
                ("stable-paper", "Paper", "docs/papers/stable-paper"))
            with patch.object(bib, "REGISTRY_PATH", registry_path):
                bib.project_affiliation_registry(conn)
                slot_id = bib.record_affiliation_observation(
                    conn, 1, {"raw_name": "Unseen", "source": "review",
                              "source_record_key": "source-1"}, 0, snapshot)
            observation_id, content = conn.execute(
                "SELECT observation_id,raw_content_sha256 FROM observed_affiliations").fetchone()
            expected_slot = str(uuid.uuid5(
                bib.AFFILIATION_OBSERVATION_NAMESPACE,
                affiliation_registry.canonical_json_bytes(
                    ["stable-paper", "review", "source-1", 0]).decode("utf-8")))
            expected_observation = str(uuid.uuid5(
                bib.AFFILIATION_OBSERVATION_NAMESPACE,
                affiliation_registry.canonical_json_bytes(
                    [expected_slot, 1, content]).decode("utf-8")))
            self.assertEqual(slot_id, expected_slot)
            self.assertEqual(observation_id, expected_observation)
            conn.close()

    def test_pending_owned_enrichment_attempt_survives_observation_supersession(self):
        with tempfile.TemporaryDirectory() as directory:
            registry_path, snapshot = self.make_registry_file(directory)
            conn = sqlite3.connect(":memory:")
            conn.executescript(bib.SCHEMA)
            conn.execute(
                "INSERT INTO papers (paper_id,slug,title,review_dir) VALUES (1,?,?,?)",
                ("stable-paper", "Paper", "docs/papers/stable-paper"))
            with patch.object(bib, "REGISTRY_PATH", registry_path):
                bib.project_affiliation_registry(conn)
                bib.record_affiliation_observation(
                    conn, 1, {"raw_name": "Unseen One", "source": "review"}, 0, snapshot)
                pending_id = conn.execute(
                    "SELECT pending_id FROM affiliation_pending_cases").fetchone()[0]
                conn.execute(
                    "INSERT INTO affiliation_enrichment_attempts VALUES (?,?,?,?,?,?,?,?,?)",
                    ("attempt", pending_id, "ror", "start", "finish", "no_match",
                     "response-digest", "", "proposal-digest"))
                bib.record_affiliation_observation(
                    conn, 1, {"raw_name": "Unseen Two", "source": "review"}, 0, snapshot)
            self.assertEqual(conn.execute(
                "SELECT pending_id,provider,outcome,response_digest,proposal_digest "
                "FROM affiliation_enrichment_attempts").fetchone(),
                (pending_id, "ror", "no_match", "response-digest", "proposal-digest"))
            self.assertEqual(conn.execute(
                "SELECT status,active_observation_count FROM affiliation_pending_cases "
                "WHERE pending_id=?", (pending_id,)).fetchone(),
                ("rejected", 0))
            conn.close()
    def test_proposed_organization_is_excluded_from_offline_resolution(self):
        with tempfile.TemporaryDirectory() as directory:
            registry_path, snapshot = self.make_registry_file(directory)
            conn = sqlite3.connect(":memory:")
            conn.executescript(bib.SCHEMA)
            conn.execute(
                "INSERT INTO papers (paper_id,slug,title,review_dir) VALUES (1,?,?,?)",
                ("stable-paper", "Paper", "docs/papers/stable-paper"))
            with patch.object(bib, "REGISTRY_PATH", registry_path):
                bib.project_affiliation_registry(conn)
                bib.record_affiliation_observation(
                    conn, 1, {"raw_name": "Reviewed Organization", "source": "review"},
                    0, snapshot)
            self.assertEqual(conn.execute(
                "SELECT resolution_status,resolved_organization_id FROM observed_affiliations"
            ).fetchone(), ("unseen", None))
            conn.close()
