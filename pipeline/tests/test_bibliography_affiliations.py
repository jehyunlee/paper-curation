import tempfile
import unittest
import sqlite3
from unittest.mock import patch
from pathlib import Path

from pipeline import build_bibliography_db as bib


class BibliographyAffiliationTests(unittest.TestCase):
    def setUp(self):
        bib.set_institution_registry({
            "Tongji University",
            "Massachusetts Institute of Technology",
            "The University of Hong Kong",
            "National University of Singapore",
            "National University of Defense Technology",
            "Technical University of Munich",
            "Technical University of Denmark",
            "Stanford University",
            "Tsinghua University",
            "The Chinese University of Hong Kong, Shenzhen",
            "The Hong Kong University of Science and Technology",
            "The Hong Kong University of Science and Technology (Guangzhou)",
            "Warsaw University of Technology",
            "Hebei University of Technology",
        })

    def test_scopus_subunit_normalizes_to_parent_university(self):
        self.assertEqual(
            bib.canonical_institution("University of Toronto Faculty of Medicine"),
            "University of Toronto",
        )

    def test_scopus_is_validated_and_pdf_adds_missing_institution(self):
        scopus = [{
            "name": "University of Toronto",
            "raw_name": "University of Toronto",
            "country": "Canada",
            "scopus_id": "1",
            "source": "scopus",
        }]
        pdf = (
            "Published online: 26 February 2024\n"
            "1Peter Munk Cardiac Centre, University Health Network, Toronto, Canada. "
            "2Department of Computer Science, University of Toronto, Toronto, Canada."
        )
        rows = bib.reconcile_affiliations(scopus, pdf, [])
        by_name = {row["name"]: row for row in rows}
        self.assertEqual(by_name["University of Toronto"]["source"], "scopus+pdf")
        self.assertIn("University Health Network", by_name)

    def test_scopus_college_profile_maps_to_parent_institution(self):
        rows = bib.reconcile_affiliations([{
            "name": "College of Engineering",
            "raw_name": "College of Engineering",
            "country": "United States",
            "scopus_id": "60137961",
            "source": "scopus",
        }], "University of Illinois at Chicago", [])
        self.assertEqual(
            [row["name"] for row in rows],
            ["University of Illinois at Chicago"],
        )

    def test_unresolved_college_subunit_is_not_stored_as_institution(self):
        rows = bib.reconcile_affiliations([{
            "name": "College of Education",
            "raw_name": "College of Education",
            "country": "United States",
            "scopus_id": "unknown",
            "source": "scopus",
        }], "", [])
        self.assertEqual(rows, [])
        self.assertTrue(
            bib.is_suspicious_institution_name("College of Education"))
        self.assertFalse(
            bib.is_suspicious_institution_name("College of Staten Island"))

    def test_named_college_subunit_maps_to_explicit_parent(self):
        self.assertEqual(
            bib.canonical_institution(
                "College of Computer Science and Technology, Zhejiang University"),
            "Zhejiang University",
        )

    def test_college_raw_affiliation_expands_named_parent(self):
        self.assertEqual(
            bib.resolve_institution_from_raw(
                "Department of Pharmacy Practice, College of Pharmacy, "
                "National University of Science and Technology, Muscat, Oman",
                "College of Pharmacy",
            ),
            "National University of Science & Technology, Oman",
        )
        self.assertEqual(
            bib.canonical_institution(
                "College of Humanities, Arts, and Social Sciences"),
            "Nanyang Technological University",
        )

    def test_all_multilingual_aliases_resolve_to_english_names(self):
        self.assertGreater(len(bib.INSTITUTION_ENGLISH_ALIASES), 100)
        for source, target in bib.INSTITUTION_ENGLISH_ALIASES.items():
            with self.subTest(source=source):
                self.assertEqual(bib.canonical_institution(source), target)
                self.assertFalse(bib.is_local_language_institution(target))

    def test_unknown_local_language_name_is_rejected(self):
        self.assertTrue(
            bib.is_suspicious_institution_name(
                "Universität für Unbekannte Forschung"))

    def test_unknown_local_name_uses_exact_country_matched_ror_label(self):
        payload = {"items": [
            {
                "names": [
                    {"value": "Universität Beispiel", "lang": "de",
                     "types": ["label"]},
                    {"value": "Example University", "lang": "en",
                     "types": ["ror_display", "label"]},
                ],
                "locations": [{"geonames_details": {
                    "country_name": "Germany"}}],
            },
        ]}
        with tempfile.TemporaryDirectory() as td, patch.object(
                bib, "_ROR_ENGLISH_CACHE_PATH",
                Path(td) / "ror_english_aliases.json"), patch.object(
                bib, "request_json", return_value=payload):
            bib._ROR_ENGLISH_CACHE = {}
            self.assertEqual(
                bib.resolve_english_institution(
                    "Universität Beispiel", "Germany", allow_remote=True),
                "Example University",
            )
        bib._ROR_ENGLISH_CACHE = None
    def test_offline_ror_resolution_neither_calls_provider_nor_writes_cache(self):
        with tempfile.TemporaryDirectory() as td:
            cache = Path(td) / "ror_english_aliases.json"
            with patch.object(bib, "_ROR_ENGLISH_CACHE_PATH", cache), \
                 patch.object(bib, "request_json") as request:
                bib._ROR_ENGLISH_CACHE = None
                self.assertEqual(
                    bib.resolve_english_institution(
                        "Universität für Unbekannte Forschung", "Germany",
                        allow_remote=True, offline=True),
                    "")
                request.assert_not_called()
                self.assertFalse(cache.exists())
        bib._ROR_ENGLISH_CACHE = None

    def test_offline_reconciliation_call_chain_never_calls_remote_provider(self):
        with tempfile.TemporaryDirectory() as td:
            cache = Path(td) / "ror_english_aliases.json"
            with patch.object(bib, "_ROR_ENGLISH_CACHE_PATH", cache), \
                 patch.object(bib, "request_json") as request:
                bib._ROR_ENGLISH_CACHE = None
                rows = bib.reconcile_affiliations(
                    [], "Universität für Unbekannte Forschung, Germany", [],
                    offline=True)
                self.assertEqual(rows, [])
                request.assert_not_called()
                self.assertFalse(cache.exists())
        bib._ROR_ENGLISH_CACHE = None

    def test_registry_projection_reresolves_current_unseen_observation(self):
        connection = sqlite3.connect(":memory:")
        connection.executescript(bib.SCHEMA + bib.AFFILIATION_SCHEMA)
        connection.execute("PRAGMA foreign_keys=OFF")
        organization_id = "org-example"
        alias_id = "alias-example"
        connection.execute(
            "INSERT INTO affiliation_organizations VALUES (?,?,?,?,?,?,?,?,?,?)",
            (organization_id, "Example University", "example university",
             "other", "", "Germany", "unknown", "active", "", 1))
        connection.execute(
            "INSERT INTO affiliation_aliases VALUES (?,?,?,?,?,?)",
            (alias_id, "Example University", "example university", "",
             "source", ""))
        connection.execute(
            "INSERT INTO affiliation_alias_candidates VALUES (?,?,?,?,?,?,?)",
            (alias_id, organization_id, "", "", 1.0, "accepted", ""))
        connection.execute(
            "INSERT INTO observed_affiliation_slots VALUES (?,?,?,?,?,?)",
            ("slot", 1, "pdf", "paper", 0, "seen"))
        connection.execute(
            "INSERT INTO observed_affiliations "
            "(observation_id,observation_slot_id,observation_version,"
            "raw_content_sha256,raw_name,normalized_raw_name,"
            "observed_country_code,observed_country_name,"
            "external_identifiers_json,raw_context_sha256,"
            "resolution_status,current_decision_id,registry_sha256,"
            "policy_version,first_seen_at,last_seen_at,is_current) "
            "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            ("observation", "slot", 1, "content", "Example University",
             "example university", "DE", "Germany", "{}", "context",
             "unseen", "decision-old", "old", "policy", "seen", "seen", 1))
        connection.execute(
            "INSERT INTO affiliation_resolution_decisions VALUES "
            "(?,?,?,?,?,?,?,?,?,?,?,?)",
            ("decision-old", "observation", 1, "unseen", None, "old", 0.0,
             "old", "policy", "seen", "seen", ""))
        connection.execute(
            "INSERT INTO affiliation_pending_cases "
            "(pending_id,normalized_raw_name,observed_country_code,"
            "external_identifiers_json,status,reason_code,first_seen_at,"
            "last_seen_at,active_observation_count,lifetime_observation_count) "
            "VALUES (?,?,?,?,?,?,?,?,?,?)",
            ("pending", "example university", "DE", "{}", "open", "old",
             "seen", "seen", 1, 1))
        connection.execute(
            "INSERT INTO affiliation_pending_observations VALUES (?,?,?)",
            ("pending", "observation", "seen"))

        bib.reresolve_current_affiliations(
            connection, {"policy_version": "policy-2"}, "registry-2")

        row = connection.execute(
            "SELECT resolution_status,resolved_organization_id,registry_sha256 "
            "FROM observed_affiliations WHERE observation_id='observation'"
        ).fetchone()
        self.assertEqual(row, ("resolved", organization_id, "registry-2"))
        pending = connection.execute(
            "SELECT status,active_observation_count FROM "
            "affiliation_pending_cases WHERE pending_id='pending'").fetchone()
        self.assertEqual(pending, ("resolved", 0))
        self.assertEqual(
            connection.execute(
                "SELECT COUNT(*) FROM affiliation_resolution_decisions "
                "WHERE observation_id='observation'").fetchone()[0],
            2)
        self.assertEqual(
            connection.execute(
                "SELECT COUNT(*) FROM affiliation_decision_candidates "
                "WHERE decision_id='decision-old'").fetchone()[0],
            0)
        connection.close()

    def test_external_identifier_precedes_alias_candidates(self):
        connection = sqlite3.connect(":memory:")
        connection.executescript(bib.SCHEMA + bib.AFFILIATION_SCHEMA)
        for organization_id, name in (("id-match", "Identifier University"),
                                      ("alias-match", "Alias University")):
            connection.execute(
                "INSERT INTO affiliation_organizations VALUES (?,?,?,?,?,?,?,?,?,?)",
                (organization_id, name, name.casefold(), "university", "",
                 "Germany", "unknown", "active", "", 1))
        connection.execute(
            "INSERT INTO affiliation_identifiers VALUES (?,?,?,?,?,?,?)",
            ("scopus", "42", "id-match", "active", "", "", "evidence"))
        connection.execute(
            "INSERT INTO affiliation_aliases VALUES (?,?,?,?,?,?)",
            ("alias", "Shared University", "shared university", "", "source", ""))
        connection.execute(
            "INSERT INTO affiliation_alias_candidates VALUES (?,?,?,?,?,?,?)",
            ("alias", "alias-match", "", "", 1.0, "accepted", ""))
        candidates, reason = bib._registry_candidates(
            connection, "shared university", "Germany", "DE", {"scopus_id": "42"})
        self.assertEqual((candidates, reason),
                         (["id-match"], "offline_registry_exact_identifier"))
        connection.close()

    def test_compatibility_groups_discard_legacy_unbound_rows(self):
        connection = sqlite3.connect(":memory:")
        connection.executescript(bib.SCHEMA + bib.AFFILIATION_SCHEMA)
        connection.execute(
            "INSERT INTO institutions (institution_name,normalized_name,source) "
            "VALUES ('Child University','child university','test')")
        connection.execute(
            "INSERT INTO institution_groups (group_name,normalized_name) "
            "VALUES ('legacy heuristic','legacy heuristic')")
        connection.execute("UPDATE institutions SET group_id=1")
        registry = {
            "organizations": [{
                "organization_id": "child", "canonical_name_en": "Child University",
                "status": "active",
            }, {
                "organization_id": "parent", "canonical_name_en": "Parent University",
                "status": "active",
            }],
            "relationships": [{
                "subject_organization_id": "child",
                "object_organization_id": "parent",
                "relationship_type": "part_of", "status": "accepted",
            }],
            "events": [],
        }
        connection.executemany(
            "INSERT INTO affiliation_organizations "
            "(organization_id,canonical_name_en,normalized_name,organization_type,"
            "country_code,country_name_en,country_scope,status,created_event_id,"
            "registry_version) VALUES (?,?,?,?,?,?,?,?,?,?)",
            [
                ("child", "Child University", "child university", "university",
                 "", "", "unknown", "active", "test", 1),
                ("parent", "Parent University", "parent university", "university",
                 "", "", "unknown", "active", "test", 1),
            ],
        )
        connection.execute("UPDATE institutions SET organization_id='child'")
        bib._project_compatibility_groups(connection, registry)
        self.assertEqual(
            connection.execute(
                "SELECT group_name FROM institution_groups").fetchall(),
            [("Parent University",)])
        self.assertEqual(
            connection.execute("SELECT group_id FROM institutions").fetchone()[0],
            1)
        connection.close()

    def test_removed_source_slot_remains_current_and_is_not_reresolved(self):
        connection = sqlite3.connect(":memory:")
        connection.executescript(bib.SCHEMA + bib.AFFILIATION_SCHEMA)
        connection.execute("PRAGMA foreign_keys=OFF")
        connection.execute(
            "INSERT INTO observed_affiliation_slots VALUES (?,?,?,?,?,?)",
            ("removed-slot", 1, "review", "paper", 0, "seen"))
        connection.execute(
            "INSERT INTO observed_affiliations "
            "(observation_id,observation_slot_id,observation_version,"
            "raw_content_sha256,raw_name,normalized_raw_name,"
            "observed_country_code,observed_country_name,"
            "external_identifiers_json,raw_context_sha256,resolution_status,"
            "registry_sha256,policy_version,first_seen_at,last_seen_at,is_current) "
            "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            ("removed-observation", "removed-slot", 1, "content",
             "Removed University", "removed university", "", "", "{}",
             "context", "unseen", "digest", "policy", "seen", "seen", 1))
        connection.execute(
            "INSERT INTO affiliation_pending_cases "
            "(pending_id,normalized_raw_name,observed_country_code,"
            "external_identifiers_json,status,reason_code,first_seen_at,"
            "last_seen_at,active_observation_count,lifetime_observation_count) "
            "VALUES (?,?,?,?,?,?,?,?,?,?)",
            ("pending", "removed university", "", "{}", "open", "unseen",
             "seen", "seen", 1, 1))
        connection.execute(
            "INSERT INTO affiliation_pending_observations VALUES (?,?,?)",
            ("pending", "removed-observation", "seen"))
        bib.supersede_removed_affiliation_slots(
            connection, 1, "paper", set(), {"policy_version": "policy"})
        self.assertEqual(
            connection.execute(
                "SELECT COUNT(*) FROM observed_affiliations "
                "WHERE observation_slot_id='removed-slot' AND is_current=1").fetchone()[0],
            1)
        self.assertEqual(
            connection.execute(
                "SELECT resolution_status FROM observed_affiliations "
                "WHERE observation_id='removed-observation'").fetchone()[0],
            "superseded")
        self.assertEqual(
            connection.execute(
                "SELECT active_observation_count FROM affiliation_pending_cases "
                "WHERE pending_id='pending'").fetchone()[0],
            0)
        decision_count = connection.execute(
            "SELECT COUNT(*) FROM affiliation_resolution_decisions "
            "WHERE observation_id='removed-observation'").fetchone()[0]
        bib.reresolve_current_affiliations(
            connection, {"policy_version": "policy"}, "digest")
        self.assertEqual(
            connection.execute(
                "SELECT COUNT(*) FROM affiliation_resolution_decisions "
                "WHERE observation_id='removed-observation'").fetchone()[0],
            decision_count)
        connection.close()

    def test_repair_restores_current_terminal_observation_for_legacy_slot(self):
        connection = sqlite3.connect(":memory:")
        connection.executescript(bib.SCHEMA + bib.AFFILIATION_SCHEMA)
        connection.execute(
            "INSERT INTO papers (paper_id,slug,title,review_dir) "
            "VALUES (1,'paper','Paper','docs/papers/paper')")
        connection.execute(
            "INSERT INTO observed_affiliation_slots VALUES (?,?,?,?,?,?)",
            ("legacy-slot", 1, "review", "paper", 0, "seen"))
        connection.execute(
            "INSERT INTO observed_affiliations "
            "(observation_id,observation_slot_id,observation_version,"
            "raw_content_sha256,raw_name,normalized_raw_name,"
            "observed_country_code,observed_country_name,"
            "external_identifiers_json,raw_context_sha256,resolution_status,"
            "registry_sha256,policy_version,first_seen_at,last_seen_at,is_current) "
            "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            ("legacy-observation", "legacy-slot", 1, "content",
             "Removed University", "removed university", "", "", "{}",
             "context", "superseded", "digest", "policy", "seen", "seen", 0))
        bib.repair_terminal_superseded_current_slots(connection)
        self.assertEqual(
            connection.execute(
                "SELECT COUNT(*) FROM observed_affiliations "
                "WHERE observation_slot_id='legacy-slot' AND is_current=1").fetchone()[0],
            1)
        connection.close()
    def test_source_records_preserve_each_source_slot_before_deduplication(self):
        records = bib.source_affiliation_records(
            [{"name": "Same University", "scopus_id": "one"},
             {"name": "Same University", "scopus_id": "two"}],
            ["Same University", "Same University"])
        self.assertEqual(len(records), 4)
        self.assertEqual(
            [(record["source"], record["source_record_key"],
              record["_source_ordinal"]) for record in records],
            [("scopus", "scopus:one", 0), ("scopus", "scopus:two", 1),
             ("review", "review:header", 0), ("review", "review:header", 1)])
        self.assertEqual(
            records[0]["context"]["scopus_affiliation"]["scopus_id"], "one")
        self.assertEqual(
            records[2]["context"]["review_affiliation"], "Same University")

    def test_longest_registered_parent_wins_over_author_and_department(self):
        cases = {
            (
                "Zihe Wei School of Computer Science & Technology "
                "Tongji University"
            ): "Tongji University",
            (
                "Zituo Chen Department of Mechanical Engineering "
                "Massachusetts Institute of Technology Cambridge"
            ): "Massachusetts Institute of Technology",
            (
                "Department of Medicine, Stanford University School of Medicine"
            ): "Stanford University",
        }
        for raw, expected in cases.items():
            with self.subTest(raw=raw):
                self.assertEqual(
                    bib.resolve_institution_from_raw(raw, raw), expected)

    def test_generic_university_names_expand_from_raw_affiliation(self):
        cases = [
            ("The University", "1The University of Hong Kong, Hong Kong",
             "The University of Hong Kong"),
            ("National University",
             "1National University of Singapore, Singapore",
             "National University of Singapore"),
            ("National University",
             "College, National University of Defense Technology, China",
             "National University of Defense Technology"),
            ("Technical University",
             "Department, Technical University of Munich, Germany",
             "Technical University of Munich"),
        ]
        for current, raw, expected in cases:
            with self.subTest(current=current, raw=raw):
                self.assertEqual(
                    bib.resolve_institution_from_raw(raw, current), expected)

    def test_clean_current_institution_is_not_replaced_by_another_affiliation(self):
        raw = (
            "Tsinghua University, Beijing, China; "
            "The Hong Kong University of Science and Technology, Hong Kong"
        )
        self.assertEqual(
            bib.resolve_institution_from_raw(raw, "Tsinghua University"),
            "Tsinghua University",
        )

    def test_hong_kong_branch_campuses_remain_distinct(self):
        cases = [
            (
                "Chinese University of Hong Kong, Shenzhen, China",
                "Chinese University",
                "The Chinese University of Hong Kong, Shenzhen",
            ),
            (
                "Hong Kong University of Science and Technology (Guangzhou), China",
                "Hong Kong University",
                "The Hong Kong University of Science and Technology (Guangzhou)",
            ),
        ]
        for raw, current, expected in cases:
            with self.subTest(raw=raw):
                self.assertEqual(
                    bib.resolve_institution_from_raw(raw, current), expected)

    def test_affiliation_markers_do_not_truncate_technology_universities(self):
        cases = [
            (
                "aWarsaw University of Technology, Faculty of Mathematics",
                "University of Technology",
                "Warsaw University of Technology",
            ),
            (
                "BUPT 7Hebei University of Technology",
                "University of Technology",
                "Hebei University of Technology",
            ),
        ]
        for raw, current, expected in cases:
            with self.subTest(raw=raw):
                self.assertEqual(
                    bib.resolve_institution_from_raw(raw, current), expected)

    def test_truncated_exact_aliases_are_canonicalized(self):
        self.assertEqual(
            bib.canonical_institution("Massachusetts Institute"),
            "Massachusetts Institute of Technology")
        self.assertEqual(
            bib.canonical_institution("Georgia Institute"),
            "Georgia Institute of Technology")

    def test_text_fallback_scans_after_abstract_and_last_pages(self):
        with tempfile.TemporaryDirectory() as td:
            text = Path(td) / "text.md"
            text.write_text(
                "Title\nAuthors\nAbstract\nBody\n" + "Body\n" * 60 +
                "Published online: 26 February 2024\n"
                "1University of Toronto, Toronto, Canada.\n",
                encoding="utf-8",
            )
            extracted = bib._pdf_text_for_affiliations(None, text)
            self.assertIn("University of Toronto", extracted)
            self.assertIn("Published online", extracted)

    def test_scopus_bibliography_normalizes_full_record(self):
        row = bib.scopus_bibliography({"coredata": {
            "dc:title": "A formal title",
            "prism:publicationName": "Nature Methods",
            "prism:coverDate": "2024-08-01",
            "prism:doi": "10.1038/example",
            "prism:volume": "21",
            "prism:issueIdentifier": "8",
            "prism:pageRange": "1470-1480",
            "dc:publisher": "Nature Research",
            "prism:issn": "15487105 15487091",
            "subtypeDescription": "Article",
            "eid": "2-s2.0-123",
        }})
        self.assertEqual(row["journal"], "Nature Methods")
        self.assertEqual(row["volume"], "21")
        self.assertEqual(row["pages"], "1470-1480")
        self.assertEqual(row["issn"], "1548-7105; 1548-7091")
        self.assertEqual(row["scopus_eid"], "2-s2.0-123")

    def test_pdf_bibliography_extracts_publisher_dates_and_header(self):
        text = (
            "Nature Methods | Volume 21 | August 2024 | 1470–1480\n"
            "https://doi.org/10.1038/s41592-024-02201-0\n"
            "Received: 12 July 2023\nAccepted: 30 January 2024\n"
            "Published online: 26 February 2024\n"
        )
        row = bib.pdf_bibliography(text)
        self.assertEqual(row["journal"], "Nature Methods")
        self.assertEqual(row["volume"], "21")
        self.assertEqual(row["pages"], "1470-1480")
        self.assertEqual(row["received_date"], "2023-07-12")
        self.assertEqual(row["accepted_date"], "2024-01-30")
        self.assertEqual(row["published_online_date"], "2024-02-26")

    def test_pdf_repairs_scopus_and_online_date_wins(self):
        row = bib.reconcile_bibliography(
            {"title": "Local", "journal": "Preprint", "date": "2023"},
            {"title": "Formal", "journal": "Journal", "date": "2024-08-01",
             "volume": "21", "source": "scopus"},
            {"journal": "Nature Methods", "pages": "1470-1480",
             "published_online_date": "2024-02-26"},
        )
        self.assertEqual(row["title"], "Formal")
        self.assertEqual(row["journal"], "Nature Methods")
        self.assertEqual(row["date"], "2024-02-26")
        self.assertEqual(row["source"], "scopus+pdf")

    def test_legacy_database_schema_is_migrated(self):
        conn = sqlite3.connect(":memory:")
        conn.execute(
            "CREATE TABLE papers (paper_id INTEGER PRIMARY KEY, "
            "slug TEXT UNIQUE, title TEXT, review_dir TEXT)")
        bib.ensure_schema_migrations(conn)
        columns = {
            row[1] for row in conn.execute("PRAGMA table_info(papers)").fetchall()
        }
        self.assertTrue(set(bib.PAPER_SCHEMA_COLUMNS).issubset(columns))
        conn.close()
    def test_fresh_schema_origin_receipt_id_is_deterministic(self):
        origin = {
            "schema_version": "affiliation-2",
            "registry_sha256": "registry",
            "event_head": "event",
            "policy_version": "policy",
            "source_sha256": "source",
        }
        receipt_id = bib.fresh_schema_origin_receipt_id(**origin)
        self.assertEqual(receipt_id, bib.fresh_schema_origin_receipt_id(
            **{key: origin[key] for key in reversed(origin)}))
        self.assertNotEqual(receipt_id, "fresh-schema")
        self.assertNotEqual(receipt_id, bib.fresh_schema_origin_receipt_id(
            **{**origin, "event_head": "changed"}))


if __name__ == "__main__":
    unittest.main()
