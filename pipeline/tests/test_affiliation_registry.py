import copy
import base64
import json
import hashlib
import tempfile
import sqlite3
from types import SimpleNamespace
import sys
import unittest
from pathlib import Path
from unittest import mock

PIPELINE_DIR = Path(__file__).resolve().parents[1]
if str(PIPELINE_DIR) not in sys.path:
    sys.path.insert(0, str(PIPELINE_DIR))

import audit_affiliation_registry as audit
import check_bibliography_db as checker
from pipeline.lib import affiliation_registry as registry


REGISTRY_PATH = Path(__file__).resolve().parents[1] / "affiliation_registry.json"
BASELINE_PATH = Path(__file__).resolve().parents[1] / "affiliation_registry_baseline.json"


class AffiliationRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.snapshot = registry.load_registry(REGISTRY_PATH)
    def _review_identities(self, snapshot):
        approvals = []
        for organization in snapshot["organizations"]:
            approvals.append({
                "kind": "identity",
                "policy_version": snapshot["policy_version"],
                "organization_id": organization["organization_id"],
                "approved_by": ["reviewer-one", "reviewer-two"],
                "confidence": 1.0,
                "evidence": {
                    "provider": "ror",
                    "match": "exact_country_consistent",
                    "external_id": f"https://ror.org/{organization['organization_id'][-12:]}",
                },
            })
        return registry.promote_approved(snapshot, approvals, timestamp="2026-08-08T00:00:00Z")

    def test_canonical_bytes_normalize_nfc_sort_keys_and_end_in_lf(self):
        composed = {"é": ["café", {"b": 2, "a": "e\u0301"}]}
        decomposed = {"e\u0301": ["cafe\u0301", {"a": "é", "b": 2}]}
        expected = b'{"\xc3\xa9":["caf\xc3\xa9",{"a":"\xc3\xa9","b":2}]}\n'
        self.assertEqual(registry.canonical_json_bytes(composed), expected)
        self.assertEqual(registry.canonical_json_bytes(decomposed), expected)
        self.assertEqual(registry.canonical_sha256(composed), registry.canonical_sha256(decomposed))

    def test_snapshot_replays_and_has_one_correction_for_each_source_key(self):
        corrections = registry.correction_projection(self.snapshot)
        baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        self.assertEqual(len(corrections), 4747)
        self.assertEqual([row["source_key"] for row in corrections],
                         sorted(row["source_key"] for row in corrections))
        self.assertEqual(len({row["source_key"] for row in corrections}), 4747)
        self.assertEqual(baseline["correction_reconciliation"]["correction_rows"], len(corrections))
        self.assertEqual(baseline["correction_reconciliation"]["source_keys"], 4747)
        self.assertEqual(registry.replay_registry(self.snapshot)["event_head"], self.snapshot["event_head"])
    def test_relationship_transition_preserves_every_legacy_edge_field(self):
        tampered = copy.deepcopy(self.snapshot)
        transition = next(
            event for event in tampered["events"]
            if event["type"] == "relationship_policy_transition")
        transition["payload"]["demoted_relationships"][0][
            "relationship_proposal"]["relationship_type"] = "member_of"
        transition["digest"] = registry._event_digest(transition)
        tampered["event_head"] = transition["digest"]
        with self.assertRaisesRegex(
                ValueError, "relationship policy transition demotion is malformed"):
            registry.validate_registry(tampered)

    def test_pinned_root_consolidation_replays_and_conserves_proposals(self):
        consolidated = registry.consolidate_pinned_roots(
            self.snapshot, timestamp="2026-08-10T00:00:00Z",
            actor="test-pinned-consolidation")
        registry.validate_registry(consolidated)
        active_keys = [
            key
            for row in consolidated["organizations"]
            if row["status"] == "active"
            for key in [registry.organization_identity_key(
                row["canonical_name_en"], row["country"],
                country_scope=row.get("country_scope"))]
            if key is not None
        ]
        self.assertEqual(len(active_keys), len(set(active_keys)))
        events = [
            event for event in consolidated["events"]
            if event["type"] == "pinned_root_consolidated"
        ]
        self.assertEqual(len(events), 143)
        self.assertEqual(len(consolidated["redirects"]), 332)
        self.assertEqual(len(consolidated["relationship_proposals"]), 2019)
        current_sources = {
            row["source_relationship_id"]
            for row in consolidated["relationship_proposals"]
        }
        superseded_sources = {
            change["before"]["source_relationship_id"]
            for event in events
            for change in event["payload"]["proposal_supersessions"]
        }
        self.assertFalse(current_sources & superseded_sources)
        self.assertEqual(len(current_sources | superseded_sources), 2245)
        self.assertTrue(all(
            row["subject_organization_id"] != row["object_organization_id"]
            for row in consolidated["relationship_proposals"]))
        self.assertEqual(
            registry.replay_registry(consolidated)["event_head"],
            consolidated["event_head"])

    def test_untrusted_source_identities_remain_pending_and_known_corrections_are_events(self):
        source = {
            "60029470": {"af_name": ["CRISO"], "af_groupname": ["CRISO"]},
            "2": {"af_name": ["Unreviewed Institute"], "af_abbgroupname": ["UI"]},
        }
        built = registry.build_registry(source)
        rows = registry.correction_projection(built)
        self.assertEqual(built["alias_candidates"], [])
        self.assertTrue(all(item["status"] == "proposed" for item in built["organizations"]))
        self.assertTrue(all(row["evidence"]["status"] == "proposed" for row in rows))
        corrected = next(row for row in rows if row["source_key"] == "60029470")
        self.assertEqual(corrected["disposition"], "identity_proposed")
        self.assertEqual(
            corrected["correction_decisions"][0]["acceptance"],
            "pending_official_relationship_evidence",
        )
        correction_events = [
            event for event in built["events"] if event["type"] == "known_correction_decided"
        ]
        self.assertEqual(len(correction_events), 1)
        self.assertEqual(correction_events[0]["payload"]["source_key"], "60029470")
        self.assertEqual(registry.correction_projection(built), rows)
    def test_pinned_operator_curated_import_accepts_bound_evidence_and_corrections(self):
        source = {
            "60029470": {"af_name": ["CSIRO Lab"], "af_country": ["AU"], "af_groupname": ["CRISO"]},
            "60008592": {"af_name": ["Hong Kong University of Science and Technology"],
                         "af_country": ["HK"], "af_groupname": ["HKUST"]},
            "126622688": {"af_name": ["SRI at HKUST"], "af_country": ["HK"],
                           "af_id_replace": ["60008592"]},
            "55": {"af_name": ["HKUST Platform"], "af_country": ["CN"], "af_groupname": ["HKUST"]},
            "60276981": {"af_name": ["HKUST Guangzhou"], "af_country": ["CN"],
                         "af_groupname": ["HKUST"]},
            "60112417": {"af_name": ["Shenzhen PKU-HKUST Medical Center"], "af_country": ["CN"],
                         "af_groupname": ["HKUST"]},
            "60112621": {"af_name": ["PKU-HKUST Institution"], "af_country": ["CN"],
                         "af_groupname": ["HKUST"]},
            "60111413": {"af_name": ["SRI"], "af_country": ["US"], "af_groupname": ["Parent"]},
            "60111414": {"af_name": ["SRI Duplicate"], "af_country": ["US"],
                         "af_groupname": ["Parent"], "af_id_replace": ["60111413"]},
            "60029832": {"af_name": ["Joint Lab"], "af_country": ["ES"],
                          "af_groupname": ["CSIC and University of Sevilla"]},
            "60002970": {"af_name": ["HEC Unit"], "af_country": ["CA"],
                          "af_groupname": ["University of Montreal"]},
        }
        digest = "a" * 64
        with mock.patch.object(registry, "SOURCE_SHA256", digest), mock.patch.object(
                registry, "OPERATOR_CURATED_RECORD_COUNT", len(source)), mock.patch.object(
                registry, "OPERATOR_CURATED_CANONICAL_SHA256",
                registry.canonical_sha256(source)):
            built = registry.build_registry(source, source_sha256=digest, operator_curated=True)
        rows = {row["source_key"]: row for row in registry.correction_projection(built)}
        organizations = {
            item["organization_id"]: item for item in built["organizations"] if item["identifiers"]
        }
        hkust = next(item for item in organizations.values()
                     if {identifier["value"] for identifier in item["identifiers"]}
                     >= {"60008592", "126622688"})
        sri = next(item for item in organizations.values()
                   if {identifier["value"] for identifier in item["identifiers"]}
                   >= {"60111413", "60111414"})
        self.assertTrue(all(item["status"] == "active" for item in built["organizations"]))
        self.assertTrue(all(item["authority"] == "operator_curated" for item in built["evidence"]))
        self.assertEqual(rows["60002970"]["after"]["accepted_relationship_ids"], [])
        self.assertTrue(all(not rows[key]["relationship_ids"] for key in registry.HKUST_EXCLUDED_SOURCE_KEYS))
        self.assertEqual(rows["126622688"]["organization_ids"], [hkust["organization_id"]])
        self.assertEqual(
            {identifier["value"] for identifier in hkust["identifiers"]},
            {"60008592", "126622688"},
        )
        self.assertEqual(
            {identifier["value"] for identifier in sri["identifiers"]},
            {"60111413", "60111414"},
        )
        sri_edge = next(edge for edge in built["relationships"]
                        if edge["subject_organization_id"] == sri["organization_id"])
        self.assertEqual(len(sri_edge["evidence_ids"]), 2)
        self.assertEqual(rows["60111413"]["relationship_ids"], rows["60111414"]["relationship_ids"])
        hkust_edge = next(edge for edge in built["relationships"]
                          if edge["subject_organization_id"] != hkust["organization_id"]
                          and edge["object_organization_id"] == hkust["organization_id"])
        self.assertTrue(all(
            item["cross_border_explicit"] for item in built["evidence"]
            if item["evidence_id"] in hkust_edge["evidence_ids"]
        ))
        self.assertEqual(
            len([event for event in built["events"] if "organization" in event["payload"]]),
            len(built["organizations"]),
        )
        self.assertEqual(len(rows), len(source))
        self.assertEqual(set(rows), set(source))
        self.assertEqual(registry.replay_registry(built)["event_head"], built["event_head"])
        tampered = copy.deepcopy(built)
        tampered["evidence"][0]["payload"]["source_key"] = "tampered"
        with mock.patch.object(registry, "SOURCE_SHA256", digest), mock.patch.object(
                registry, "OPERATOR_CURATED_RECORD_COUNT", len(source)), mock.patch.object(
                registry, "OPERATOR_CURATED_CANONICAL_SHA256",
                registry.canonical_sha256(source)):
            with self.assertRaisesRegex(
                    ValueError, "relationship lacks accepted official evidence"):
                registry.validate_registry(tampered, require_replay=False)
            correction_tampered = copy.deepcopy(built)
            correction_event = next(
                event for event in correction_tampered["events"]
                if isinstance(event.get("payload", {}).get("correction"), dict)
            )
            correction_event["payload"]["correction"]["source_record"]["af_name"] = [
                "Tampered"
            ]
            with self.assertRaisesRegex(
                    ValueError, "event hash chain mismatch"):
                registry.validate_registry(
                    correction_tampered, require_replay=False)

    def test_operator_curated_mode_rejects_unpinned_source(self):
        with self.assertRaisesRegex(ValueError, "pinned 4,747-record"):
            registry.build_registry({"1": {"af_name": ["One"]}}, operator_curated=True)
    def test_operator_curated_replacement_targets_fail_closed(self):
        digest = "c" * 64
        cases = (
            ({"1": {"af_name": ["One"], "af_id_replace": ["2"]},
              "2": {"af_name": ["Two"], "af_id_replace": ["1"]}}, "cyclic"),
            ({"1": {"af_name": ["One"], "af_id_replace": ["2", "3"]},
              "2": {"af_name": ["Two"]}, "3": {"af_name": ["Three"]}}, "conflicting"),
            ({"1": {"af_name": ["One"], "af_id_replace": ["missing"]}}, "missing"),
        )
        for source, error in cases:
            with self.subTest(error=error), mock.patch.object(
                    registry, "SOURCE_SHA256", digest), mock.patch.object(
                    registry, "OPERATOR_CURATED_RECORD_COUNT", len(source)), mock.patch.object(
                    registry, "OPERATOR_CURATED_CANONICAL_SHA256",
                    registry.canonical_sha256(source)):
                with self.assertRaisesRegex(ValueError, error):
                    registry.build_registry(source, source_sha256=digest, operator_curated=True)
    def test_operator_curated_ambiguous_group_target_creates_group_identity(self):
        source = {
            "1": {"af_name": ["Child"], "af_country": ["US"], "af_groupname": ["Shared Parent"]},
            "2": {"af_name": ["Shared Parent"], "af_country": ["US"]},
            "3": {"af_name": ["Shared Parent"], "af_country": ["US"]},
        }
        digest = "b" * 64
        with mock.patch.object(registry, "SOURCE_SHA256", digest), mock.patch.object(
                registry, "OPERATOR_CURATED_RECORD_COUNT", len(source)), mock.patch.object(
                registry, "OPERATOR_CURATED_CANONICAL_SHA256",
                registry.canonical_sha256(source)):
            built = registry.build_registry(source, source_sha256=digest, operator_curated=True)
        edge = built["relationships"][0]
        source_parent_ids = {
            item["organization_id"] for item in built["organizations"]
            if item["canonical_name_en"] == "Shared Parent" and item["identifiers"]
        }
        self.assertNotIn(edge["object_organization_id"], source_parent_ids)

    def test_operator_curated_mode_rejects_asserted_digest_for_different_content(self):
        source = {"1": {"af_name": ["Different"]}}
        digest = "d" * 64
        with mock.patch.object(registry, "SOURCE_SHA256", digest), mock.patch.object(
                registry, "OPERATOR_CURATED_RECORD_COUNT", len(source)):
            with self.assertRaisesRegex(ValueError, "pinned 4,747-record"):
                registry.build_registry(
                    source, source_sha256=digest, operator_curated=True)

    def test_operator_curated_import_rejects_unpinned_legacy_aliases(self):
        args = SimpleNamespace(operator_curated=True, legacy_aliases="aliases.json")
        with self.assertRaisesRegex(ValueError, "forbids unpinned legacy aliases"):
            audit.command_import(args)

    def test_operator_curated_library_rejects_unpinned_canonical_aliases(self):
        source = {"1": {"af_name": ["One"]}}
        digest = "f" * 64
        with mock.patch.object(registry, "SOURCE_SHA256", digest), mock.patch.object(
                registry, "OPERATOR_CURATED_RECORD_COUNT", len(source)), mock.patch.object(
                registry, "OPERATOR_CURATED_CANONICAL_SHA256",
                registry.canonical_sha256(source)):
            with self.assertRaisesRegex(
                    ValueError, "forbids unpinned canonical aliases"):
                registry.build_registry(
                    source,
                    source_sha256=digest,
                    operator_curated=True,
                    canonical_aliases={"One": "Changed"},
                )

    def test_operator_curated_relationship_cycle_fails_closed(self):
        source = {
            "1": {
                "af_name": ["One"],
                "af_country": ["US"],
                "af_groupname": ["Two"],
            },
            "2": {
                "af_name": ["Two"],
                "af_country": ["US"],
                "af_groupname": ["One"],
            },
        }
        digest = "e" * 64
        with mock.patch.object(registry, "SOURCE_SHA256", digest), mock.patch.object(
                registry, "OPERATOR_CURATED_RECORD_COUNT", len(source)), mock.patch.object(
                registry, "OPERATOR_CURATED_CANONICAL_SHA256",
                registry.canonical_sha256(source)):
            with self.assertRaisesRegex(ValueError, "part_of relationship cycle"):
                registry.build_registry(
                    source, source_sha256=digest, operator_curated=True)
    def test_operational_threshold_boundaries_are_fail_closed(self):
        approved = {
            "current_observation_count": 1000,
            "active_pending_total": 100,
            "identity_country_mismatches": 2,
            "group_shares": {"Umbrella": 0.20},
        }
        at_boundary = {
            "current_observation_count": 1100,
            "active_pending_total": 105,
            "oldest_active_age_days": 30,
            "identity_country_mismatches": 5,
            "group_shares": {"Umbrella": 0.25},
        }
        self.assertEqual(
            checker.operational_threshold_issues(approved, at_boundary), [])
        beyond = {
            **at_boundary,
            "active_pending_total": 106,
            "oldest_active_age_days": 31,
            "identity_country_mismatches": 6,
            "group_shares": {"Umbrella": 0.36},
        }
        issues = checker.operational_threshold_issues(approved, beyond)
        self.assertTrue(any("baseline allowance" in issue for issue in issues))
        self.assertTrue(any("per-run allowance" in issue for issue in issues))
        self.assertTrue(any("exceeds 30 days" in issue for issue in issues))
        self.assertTrue(any("identity/country" in issue for issue in issues))
        self.assertTrue(any("group share" in issue for issue in issues))

    def test_event_tampering_and_noncanonical_snapshot_are_rejected(self):
        tampered = copy.deepcopy(self.snapshot)
        tampered["events"][0]["actor"] = "tampered"
        with self.assertRaisesRegex(ValueError, "hash chain mismatch"):
            registry.validate_registry(tampered)

        with self.subTest("canonical load rejects reordered pretty JSON"):
            import tempfile
            with tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "registry.json"
                path.write_text(
                    json.dumps(self.snapshot, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8",
                )
                with self.assertRaisesRegex(ValueError, "canonical JSON"):
                    registry.load_registry(path, validate=False)

    def test_relationship_requires_accepted_official_evidence(self):
        tiny = registry.build_registry({
            "1": {"af_name": ["One"]},
            "2": {"af_name": ["Two"]},
        })
        first, second = tiny["organizations"]
        for organization in tiny["organizations"]:
            organization["status"] = "active"
        tiny["alias_candidates"] = registry._identity_candidates(tiny["organizations"])
        tiny["relationships"] = [{
            "relationship_id": "edge-1",
            "subject_organization_id": first["organization_id"],
            "object_organization_id": second["organization_id"],
            "relationship_type": "member_of",
            "status": "accepted",
            "approved_by": ["reviewer-one"],
            "evidence_ids": ["unofficial"],
        }]
        tiny["evidence"] = [{"evidence_id": "unofficial", "authority": "source_untrusted", "status": "accepted"}]
        with self.assertRaisesRegex(ValueError, "accepted official evidence"):
            registry.validate_registry(tiny, require_replay=False)
    def test_ror_exact_candidates_reject_country_conflict_and_generic_fragments(self):
        payload = {"items": [{"id": "https://ror.org/01", "name": "Example University",
                              "aliases": ["EU"], "country": {"country_name": "Canada"},
                              "links": ["https://example.edu"]}]}
        self.assertEqual(registry.ror_exact_candidates(payload, "EU", "Canada")[0]["external_id"],
                         "https://ror.org/01")
        self.assertEqual(registry.ror_exact_candidates(payload, "EU", "United States"), [])
        v2_payload = {"items": [{
            "id": "https://ror.org/02abcde12",
            "status": "active",
            "names": [{"value": "Example Institute", "types": ["ror_display", "label"]}],
            "locations": [{"geonames_details": {
                "country_code": "US", "country_name": "United States",
            }}],
            "links": [{"type": "website", "value": "https://example.org"}],
        }]}
        candidate = registry.ror_exact_candidates(
            v2_payload, "Example Institute", "US"
        )[0]
        self.assertEqual(candidate["name"], "Example Institute")
        self.assertEqual(candidate["country"], "US")
        self.assertEqual(candidate["links"], ["https://example.org/"])
        self.assertTrue(registry.is_generic_fragment("Department of Physics"))

    def test_apply_approved_requires_exact_official_relationship_evidence_and_two_reviewers(self):
        tiny = self._review_identities(
            registry.build_registry({"1": {"af_name": ["One"]}, "2": {"af_name": ["Two"]}}))
        first, second = tiny["organizations"]
        approval = {
            "kind": "relationship", "policy_version": tiny["policy_version"],
            "approved_by": ["reviewer-one"],
            "relationship": {"subject_organization_id": first["organization_id"],
                             "object_organization_id": second["organization_id"],
                             "relationship_type": "member_of",
                             "validity_interval": {"start": "2020-01-01", "end": ""}},
            "evidence": {"authority": "official", "status": "accepted",
                         "url": "https://one.example/member", "quote": "One is a member.",
                         "payload": {"source": "official-page"}},
        }
        approval["evidence"]["payload_sha256"] = registry.canonical_sha256(approval["evidence"]["payload"])
        approval["evidence"]["quote_sha256"] = registry.canonical_sha256(approval["evidence"]["quote"])
        with self.assertRaisesRegex(ValueError, "two reviewer approvals"):
            registry.promote_approved(tiny, [approval], timestamp="2026-08-08T00:00:00Z")
        approval["approved_by"].append("reviewer-two")
        promoted = registry.promote_approved(tiny, [approval], timestamp="2026-08-08T00:00:00Z")
        self.assertEqual(len(promoted["relationships"]), 1)
        self.assertEqual(len(tiny["relationships"]), 0)

    def test_replay_does_not_mutate_historical_event_payloads(self):
        tiny = registry.build_registry({"1": {"af_name": ["One"]}})
        event_payload = copy.deepcopy(tiny["events"][0]["payload"])
        with mock.patch.object(registry.copy, "deepcopy", wraps=copy.deepcopy) as deepcopy:
            replayed = registry.replay_registry(tiny)
        self.assertGreater(deepcopy.call_count, 0)
        replayed["organizations"][0]["aliases"][0]["name"] = "mutated"
        self.assertEqual(tiny["events"][0]["payload"], event_payload)
        self.assertEqual(registry.replay_registry(tiny)["organizations"][0]["aliases"][0]["name"],
                         event_payload["organization"]["aliases"][0]["name"])

    def test_official_evidence_quote_and_payload_digests_are_tamper_detected(self):
        tiny = self._review_identities(
            registry.build_registry({"1": {"af_name": ["One"]}, "2": {"af_name": ["Two"]}}))
        first, second = tiny["organizations"]
        evidence = {"authority": "official", "status": "accepted", "url": "https://one.example/member",
                    "quote": "One is a member.", "payload": {"source": "official-page"}}
        evidence["payload_sha256"] = registry.canonical_sha256(evidence["payload"])
        evidence["quote_sha256"] = registry.canonical_sha256(evidence["quote"])
        approval = {"kind": "relationship", "policy_version": tiny["policy_version"],
                    "approved_by": ["reviewer-one", "reviewer-two"],
                    "relationship": {"subject_organization_id": first["organization_id"],
                                     "object_organization_id": second["organization_id"],
                                     "relationship_type": "member_of"},
                    "evidence": evidence}
        promoted = registry.promote_approved(tiny, [approval], timestamp="2026-08-08T00:00:00Z")
        relationship_evidence_id = promoted["relationships"][0]["evidence_ids"][0]
        next(item for item in promoted["evidence"]
             if item["evidence_id"] == relationship_evidence_id)["quote"] = "tampered"
        with self.assertRaisesRegex(ValueError, "accepted official evidence"):
            registry.validate_registry(promoted, require_replay=False)
    def test_promotion_fails_closed_for_graph_and_evidence_violations(self):
        source = {
            "1": {"af_name": ["One"], "af_country": ["US"]},
            "2": {"af_name": ["Two"], "af_country": ["CA"]},
        }
        reviewed = self._review_identities(registry.build_registry(source))
        first, second = reviewed["organizations"]
        approval = {
            "kind": "relationship",
            "policy_version": reviewed["policy_version"],
            "approved_by": ["reviewer-one", "reviewer-two"],
            "relationship": {
                "subject_organization_id": first["organization_id"],
                "object_organization_id": second["organization_id"],
                "relationship_type": "part_of",
                "validity_interval": {"start": "2020-01-01", "end": ""},
            },
            "evidence": {
                "authority": "official",
                "status": "accepted",
                "url": "https://one.example/governance",
                "quote": "One is part of Two.",
                "payload": {"source": "official"},
            },
        }
        approval["evidence"]["payload_sha256"] = registry.canonical_sha256(
            approval["evidence"]["payload"])
        approval["evidence"]["quote_sha256"] = registry.canonical_sha256(
            approval["evidence"]["quote"])
        with self.assertRaisesRegex(ValueError, "cross-border structural"):
            registry.promote_approved(reviewed, [approval], timestamp="2026-08-08T00:00:00Z")
        approval["evidence"]["cross_border_explicit"] = True
        promoted = registry.promote_approved(
            reviewed, [approval], timestamp="2026-08-08T00:00:00Z")
        reversed_approval = copy.deepcopy(approval)
        reversed_approval["relationship"].update({
            "subject_organization_id": second["organization_id"],
            "object_organization_id": first["organization_id"],
        })
        reversed_approval["evidence"].update({
            "url": "https://two.example/governance",
            "quote": "Two is part of One.",
            "payload": {"source": "official-reverse"},
        })
        reversed_approval["evidence"]["payload_sha256"] = registry.canonical_sha256(
            reversed_approval["evidence"]["payload"])
        reversed_approval["evidence"]["quote_sha256"] = registry.canonical_sha256(
            reversed_approval["evidence"]["quote"])
        with self.assertRaisesRegex(ValueError, "cycle"):
            registry.promote_approved(promoted, [reversed_approval], timestamp="2026-08-08T00:00:00Z")
        overlapping = copy.deepcopy(approval)
        overlapping["relationship"]["validity_interval"] = {
            "start": "2021-01-01", "end": "2022-01-01",
        }
        overlapping["evidence"].update({
            "url": "https://one.example/governance-overlap",
            "quote": "One remained part of Two.",
            "payload": {"source": "official-overlap"},
        })
        overlapping["evidence"]["payload_sha256"] = registry.canonical_sha256(
            overlapping["evidence"]["payload"])
        overlapping["evidence"]["quote_sha256"] = registry.canonical_sha256(
            overlapping["evidence"]["quote"])
        with self.assertRaisesRegex(ValueError, "overlapping"):
            registry.promote_approved(promoted, [overlapping], timestamp="2026-08-08T00:00:00Z")
        expired = copy.deepcopy(promoted)
        edge_evidence_id = expired["relationships"][0]["evidence_ids"][0]
        next(item for item in expired["evidence"]
             if item["evidence_id"] == edge_evidence_id)["revalidated_at"] = "2026-01-01T00:00:00Z"
        with self.assertRaisesRegex(ValueError, "accepted official evidence"):
            registry.validate_registry(expired, require_replay=False, effective_date="2026-08-08")
        unapproved = copy.deepcopy(promoted)
        edge_evidence_id = unapproved["relationships"][0]["evidence_ids"][0]
        next(item for item in unapproved["evidence"]
             if item["evidence_id"] == edge_evidence_id)["review_status"] = "proposed"
        with self.assertRaisesRegex(ValueError, "accepted official evidence"):
            registry.validate_registry(unapproved, require_replay=False, effective_date="2026-08-08")
        deep = registry.build_registry({
            str(index): {"af_name": [f"Organization {index}"]}
            for index in range(10)
        })
        for organization in deep["organizations"]:
            organization["status"] = "active"
        deep["alias_candidates"] = registry._identity_candidates(deep["organizations"])
        deep["relationships"], deep["evidence"] = [], []
        organizations = deep["organizations"]
        for index in range(9):
            payload = {"edge": index}
            evidence = {
                "evidence_id": f"depth-evidence-{index}",
                "authority": "official",
                "status": "accepted",
                "review_status": "approved",
                "approved_by": ["reviewer-one"],
                "revalidated_at": "2026-08-08T00:00:00Z",
                "url": f"https://example.org/{index}",
                "quote": f"Organization {index} is part of Organization {index + 1}.",
                "payload": payload,
                "payload_sha256": registry.canonical_sha256(payload),
            }
            evidence["quote_sha256"] = registry.canonical_sha256(evidence["quote"])
            deep["evidence"].append(evidence)
            deep["relationships"].append({
                "relationship_id": f"depth-edge-{index}",
                "subject_organization_id": organizations[index]["organization_id"],
                "object_organization_id": organizations[index + 1]["organization_id"],
                "relationship_type": "part_of",
                "status": "accepted",
                "approved_by": ["reviewer-one"],
                "evidence_ids": [evidence["evidence_id"]],
            })
        with self.assertRaisesRegex(ValueError, "depth exceeds 8"):
            registry.validate_registry(deep, require_replay=False, effective_date="2026-08-08")

    def test_provider_failure_preserves_accepted_artifacts_and_proposal_prefix(self):
        with tempfile.TemporaryDirectory() as directory:
            proposals = Path(directory) / "proposals.jsonl"
            prefix = b'{"existing":"proposal"}\n'
            proposals.write_bytes(prefix)
            registry_before = hashlib.sha256(REGISTRY_PATH.read_bytes()).hexdigest()
            corrections = REGISTRY_PATH.with_name(
                "affiliation_registry_corrections.jsonl")
            corrections_before = hashlib.sha256(corrections.read_bytes()).hexdigest()
            args = SimpleNamespace(
                registry=REGISTRY_PATH,
                allow_network=True,
                request_budget=3,
                max_retries=0,
                circuit_breaker_failures=3,
                retry_backoff_seconds=0,
                name=["Example University"],
                country="US",
                db=None,
                retrieved_at="2026-08-08T00:00:00Z",
                proposals=proposals,
                oracle_dir=directory,
            )
            with mock.patch.object(audit, "_oracle_manifest", return_value={}), \
                    mock.patch.object(
                        audit, "_request_with_budget",
                        side_effect=OSError("provider unavailable")):
                self.assertEqual(audit.command_resolve_pending(args), 6)

            self.assertEqual(
                hashlib.sha256(REGISTRY_PATH.read_bytes()).hexdigest(),
                registry_before)
            self.assertEqual(
                hashlib.sha256(corrections.read_bytes()).hexdigest(),
                corrections_before)
            self.assertTrue(proposals.read_bytes().startswith(prefix))
            appended = [
                json.loads(line) for line in proposals.read_text(
                    encoding="utf-8").splitlines()[1:]
            ]
            self.assertEqual(appended[0]["status"], "failed")
            self.assertEqual(appended[0]["reason"], "provider_failure")
    def test_identity_approval_requires_exact_confidence_and_replay(self):
        tiny = registry.build_registry({"1": {"af_name": ["One"]}})
        organization = tiny["organizations"][0]
        approval = {
            "kind": "identity",
            "policy_version": tiny["policy_version"],
            "organization_id": organization["organization_id"],
            "approved_by": ["reviewer-one", "reviewer-two"],
            "evidence": {
                "provider": "ror",
                "match": "exact_country_consistent",
                "external_id": "https://ror.org/01",
            },
        }
        with self.assertRaisesRegex(ValueError, "confidence 1.0"):
            registry.promote_approved(tiny, [approval], timestamp="2026-08-08T00:00:00Z")
        approval["confidence"] = 1.0
        promoted = registry.promote_approved(tiny, [approval], timestamp="2026-08-08T00:00:00Z")
        self.assertEqual(registry.replay_registry(promoted)["organizations"], promoted["organizations"])

    def test_pending_attempt_persistence_uses_pending_schema_and_counters(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "affiliation.sqlite3"
            conn = sqlite3.connect(path)
            conn.executescript("""
                CREATE TABLE affiliation_pending_cases (
                    pending_id TEXT PRIMARY KEY, status TEXT NOT NULL, attempt_count INTEGER NOT NULL,
                    last_attempt_at TEXT NOT NULL, proposal_digest TEXT NOT NULL);
                CREATE TABLE affiliation_enrichment_attempts (
                    attempt_id TEXT PRIMARY KEY, pending_id TEXT NOT NULL, provider TEXT NOT NULL,
                    started_at TEXT NOT NULL, finished_at TEXT NOT NULL, outcome TEXT NOT NULL,
                    response_digest TEXT NOT NULL, error_class TEXT NOT NULL, proposal_digest TEXT NOT NULL);
            """)
            conn.execute(
                "INSERT INTO affiliation_pending_cases VALUES (?,?,?,?,?)",
                ("pending-1", "open", 0, "", ""),
            )
            conn.commit()
            conn.close()
            attempt = audit._attempt(
                {"query": "Example University", "country": "US",
                 "retrieved_at": "2026-08-08T00:00:00Z", "target_index": 0},
                provider="ror", status="proposal", payload_sha256="response",
                candidate_external_id="https://ror.org/01",
            )
            audit._persist_pending_attempts(
                str(path), [attempt], {("Example University", "US"): {"pending-1"}})
            conn = sqlite3.connect(path)
            self.assertEqual(
                conn.execute(
                    "SELECT pending_id,provider,outcome,response_digest,proposal_digest "
                    "FROM affiliation_enrichment_attempts").fetchone()[0:4],
                ("pending-1", "ror", "success", "response"),
            )
            self.assertEqual(
                conn.execute(
                    "SELECT status,attempt_count,last_attempt_at FROM affiliation_pending_cases"
                ).fetchone(),
                ("proposed", 1, "2026-08-08T00:00:00Z"),
            )
            conn.close()

    def test_correction_projection_and_evidence_freshness_are_exact(self):
        tiny = registry.build_registry({"1": {"af_name": ["One"]}})
        rows = registry.correction_projection(tiny)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "corrections.jsonl"
            path.write_bytes(b"".join(registry.canonical_json_bytes(row) for row in rows))
            issues = []
            checker.correction_projection_issues(path, tiny, issues)
            self.assertEqual(issues, [])
            path.write_bytes(b'{"not":"the projection"}\n')
            checker.correction_projection_issues(path, tiny, issues)
            self.assertIn("registry correction ledger projection mismatch", issues)
        registry_with_evidence = {
            "relationships": [{"status": "accepted", "evidence_ids": ["evidence-1"]}],
            "evidence": [{"evidence_id": "evidence-1",
                          "revalidated_at": "2026-06-08T00:00:00Z"}],
        }
        issues, warnings = [], []
        checker.evidence_issues(registry_with_evidence, "2026-08-08", issues, warnings)
        self.assertEqual(issues, [])
        self.assertEqual(warnings, ["relationship evidence revalidation due within 30 days"])
        registry_with_evidence["evidence"][0]["revalidated_at"] = "2026-05-09T00:00:00Z"
        checker.evidence_issues(registry_with_evidence, "2026-08-08", issues, warnings)
        self.assertIn("relationship evidence revalidation exceeds 90 days", issues)

    def test_operator_curated_evidence_is_not_subject_to_web_revalidation_expiry(self):
        issues, warnings = [], []
        checker.evidence_issues(self.snapshot, "2026-08-08", issues, warnings)
        self.assertEqual(issues, [])
        self.assertEqual(warnings, [])

    def test_operator_curated_evidence_exemption_requires_pinned_provenance(self):
        untrusted = {
            "import_mode": "source_proposals",
            "source_sha256": "wrong",
            "relationships": [{
                "status": "accepted",
                "evidence_ids": ["operator-evidence"],
            }],
            "evidence": [{
                "evidence_id": "operator-evidence",
                "authority": "operator_curated",
                "status": "accepted",
            }],
        }
        issues, warnings = [], []
        checker.evidence_issues(untrusted, "2026-08-08", issues, warnings)
        self.assertEqual(
            issues, ["operator-curated relationship evidence provenance invalid"])
        self.assertEqual(warnings, [])
    def _pending_db(self, path, names):
        conn = sqlite3.connect(path)
        conn.executescript("""
            CREATE TABLE affiliation_pending_cases (
                pending_id TEXT PRIMARY KEY, observed_country_code TEXT NOT NULL,
                status TEXT NOT NULL, attempt_count INTEGER NOT NULL DEFAULT 0,
                last_attempt_at TEXT NOT NULL DEFAULT '', proposal_digest TEXT NOT NULL DEFAULT '');
            CREATE TABLE observed_affiliations (
                observation_id TEXT PRIMARY KEY, raw_name TEXT NOT NULL,
                is_current INTEGER NOT NULL, resolution_status TEXT NOT NULL);
            CREATE TABLE affiliation_pending_observations (
                pending_id TEXT NOT NULL, observation_id TEXT NOT NULL);
            CREATE TABLE affiliation_enrichment_attempts (
                attempt_id TEXT PRIMARY KEY, pending_id TEXT NOT NULL,
                provider TEXT NOT NULL CHECK(provider IN ('official','ror','wikidata','wikipedia','scopus')),
                started_at TEXT NOT NULL, finished_at TEXT NOT NULL,
                outcome TEXT NOT NULL CHECK(outcome IN ('success','no_match','unavailable',
                    'subscription_required','timeout','rate_limited','error','budget_exhausted')),
                response_digest TEXT NOT NULL DEFAULT '', error_class TEXT NOT NULL DEFAULT '',
                proposal_digest TEXT NOT NULL DEFAULT '');
        """)
        for index, name in enumerate(names):
            pending_id = f"pending-{index}"
            observation_id = f"observation-{index}"
            conn.execute(
                "INSERT INTO affiliation_pending_cases "
                "(pending_id,observed_country_code,status) VALUES (?,?,?)",
                (pending_id, "US", "open"),
            )
            conn.execute(
                "INSERT INTO observed_affiliations VALUES (?,?,?,?)",
                (observation_id, name, 1, "unseen"),
            )
            conn.execute(
                "INSERT INTO affiliation_pending_observations VALUES (?,?)",
                (pending_id, observation_id),
            )
        conn.commit()
        return conn

    def test_policy_attempts_stay_jsonl_and_out_of_pending_attempts(self):
        with tempfile.TemporaryDirectory() as directory:
            def resolve(names, budget=1, circuit_failures=5, request=None):
                database = Path(directory) / f"{len(names)}-{budget}-{circuit_failures}.sqlite3"
                proposals = database.with_suffix(".jsonl")
                conn = self._pending_db(database, names)
                conn.close()
                args = SimpleNamespace(
                    registry=REGISTRY_PATH, allow_network=True, request_budget=budget,
                    max_retries=0, circuit_breaker_failures=circuit_failures,
                    retry_backoff_seconds=0, name=[], country="", db=str(database),
                    retrieved_at="2026-08-08T00:00:00Z", proposals=proposals,
                    oracle_dir=directory,
                )
                def fake_request(_url, _context, _args, state):
                    state["requests"] += 1
                    if isinstance(request, BaseException):
                        raise request
                    return request

                with mock.patch.object(audit, "_oracle_manifest", return_value={}), \
                        mock.patch.object(
                            audit, "_request_with_budget", side_effect=fake_request):
                    result = audit.command_resolve_pending(args)
                conn = sqlite3.connect(database)
                rows = conn.execute(
                    "SELECT provider,outcome FROM affiliation_enrichment_attempts ORDER BY provider"
                ).fetchall()
                counters = conn.execute(
                    "SELECT attempt_count FROM affiliation_pending_cases ORDER BY pending_id"
                ).fetchall()
                conn.close()
                return result, rows, counters, [
                    json.loads(line) for line in proposals.read_text(encoding="utf-8").splitlines()
                ]

            result, rows, counters, proposals = resolve(["Department of Physics"])
            self.assertEqual((result, rows, counters), (0, [], [(0,)]))
            self.assertEqual(proposals[0]["provider"], "policy")

            result, rows, counters, proposals = resolve(
                ["Alpha Institute", "Beta Institute"],
                request=({"items": []}, b"{}", 0),
            )
            self.assertEqual(result, 6)
            self.assertEqual(rows, [("ror", "no_match")])
            self.assertEqual(counters, [(1,), (0,)])
            self.assertTrue(any(row["provider"] == "policy" for row in proposals))

            result, rows, counters, proposals = resolve(
                ["Alpha Institute", "Beta Institute"], circuit_failures=1,
                request=OSError("provider unavailable"),
            )
            self.assertEqual(result, 6)
            self.assertEqual(rows, [("ror", "unavailable")])
            self.assertEqual(counters, [(1,), (0,)])
            self.assertTrue(any(row["provider"] == "policy" for row in proposals))

    def test_checker_release_date_cli_blocks_stale_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            database = Path(directory) / "bibliography.sqlite3"
            conn = sqlite3.connect(database)
            import build_bibliography_db as bib
            conn.executescript(bib.SCHEMA + bib.AFFILIATION_SCHEMA)
            snapshot_bytes = REGISTRY_PATH.read_bytes()
            snapshot = registry.load_registry(REGISTRY_PATH)
            conn.execute(
                "INSERT INTO affiliation_registry_metadata "
                "(singleton,schema_version,registry_version,registry_sha256,event_head,"
                "policy_version,source_sha256,projected_at,base_generation,migration_receipt_id) "
                "VALUES (1,?,?,?,?,?,?,?,?,?)",
                (bib.AFFILIATION_SCHEMA_VERSION, snapshot["registry_version"],
                 hashlib.sha256(snapshot_bytes).hexdigest(), snapshot["event_head"],
                 snapshot["policy_version"], snapshot["source_sha256"],
                 "2026-08-08T00:00:00Z", 0, "fresh-schema"),
            )
            conn.commit()
            conn.close()
            stale_registry = {
                "relationships": [{"status": "accepted", "evidence_ids": ["stale"]}],
                "evidence": [{"evidence_id": "stale",
                              "revalidated_at": "2026-05-09T00:00:00Z"}],
            }
            observed = {}
            real_evidence_issues = checker.evidence_issues

            def check_staleness(_registry, release_date, issues, warnings):
                observed["release_date"] = release_date
                observed["issues"] = issues
                real_evidence_issues(stale_registry, release_date, issues, warnings)

            with mock.patch.object(
                    checker, "evidence_issues", side_effect=check_staleness):
                checker.main([
                    "--db", str(database),
                    "--registry", str(REGISTRY_PATH),
                    "--baseline", str(BASELINE_PATH),
                    "--release-date", "2026-08-08",
                ])
            self.assertEqual(observed["release_date"], "2026-08-08")
            self.assertIn(
                "relationship evidence revalidation exceeds 90 days",
                observed["issues"],
            )

    def test_terminal_slots_require_a_current_superseded_observation(self):
        conn = sqlite3.connect(":memory:")
        conn.executescript("""
            CREATE TABLE observed_affiliation_slots (
                observation_slot_id TEXT PRIMARY KEY);
            CREATE TABLE observed_affiliations (
                observation_slot_id TEXT NOT NULL,
                observation_version INTEGER NOT NULL,
                resolution_status TEXT NOT NULL,
                is_current INTEGER NOT NULL);
        """)
        conn.execute(
            "INSERT INTO observed_affiliation_slots VALUES (?)", ("terminal-slot",))
        conn.execute(
            "INSERT INTO observed_affiliations VALUES (?,?,?,?)",
            ("terminal-slot", 1, "superseded", 1),
        )
        self.assertEqual(checker.invalid_slot_current_version_count(conn), 0)
        conn.execute("UPDATE observed_affiliations SET is_current=0 "
                     "WHERE observation_slot_id=?", ("terminal-slot",))
        self.assertEqual(checker.invalid_slot_current_version_count(conn), 1)
        conn.close()
    def test_projection_rejects_orphan_compatibility_group_rows(self):
        tiny = registry.build_registry({"1": {"af_name": ["One"]}})
        with tempfile.TemporaryDirectory() as directory:
            database = Path(directory) / "groups.sqlite3"
            conn = sqlite3.connect(database)
            conn.executescript("""
                CREATE TABLE affiliation_organizations (
                    organization_id TEXT PRIMARY KEY, canonical_name_en TEXT,
                    normalized_name TEXT, organization_type TEXT, country_code TEXT,
                    country_name_en TEXT, country_scope TEXT, status TEXT,
                    created_event_id TEXT, registry_version INTEGER);
                CREATE TABLE affiliation_identifiers (
                    authority TEXT, identifier_value TEXT, organization_id TEXT, status TEXT,
                    valid_from TEXT, valid_to TEXT, evidence_id TEXT);
                CREATE TABLE affiliation_aliases (
                    alias_id TEXT, alias_text TEXT, normalized_alias TEXT,
                    language_code TEXT, alias_type TEXT, created_event_id TEXT);
                CREATE TABLE affiliation_alias_candidates (
                    alias_id TEXT, organization_id TEXT, country_discriminator TEXT,
                    evidence_id TEXT, confidence REAL, review_status TEXT, event_id TEXT);
                CREATE TABLE affiliation_relationships (
                    relationship_id TEXT, subject_organization_id TEXT,
                    object_organization_id TEXT, relationship_type TEXT, valid_from TEXT,
                    valid_to TEXT, status TEXT, confidence REAL, created_event_id TEXT,
                    managed_by TEXT);
                CREATE TABLE affiliation_relationship_evidence (
                    relationship_id TEXT, evidence_id TEXT);
                CREATE TABLE institution_groups (
                    group_id INTEGER PRIMARY KEY, group_name TEXT, normalized_name TEXT,
                    organization_id TEXT);
                CREATE TABLE institutions (
                    institution_id INTEGER PRIMARY KEY, organization_id TEXT,
                    group_id INTEGER, country_name_en TEXT);
            """)
            conn.execute(
                "INSERT INTO institution_groups (group_name,normalized_name,organization_id) "
                "VALUES (?,?,NULL)", ("orphan", "orphan"),
            )
            issues = []
            checker.projection_issues(conn, tiny, issues)
            conn.close()
            self.assertIn("orphan compatibility group organization", issues)
    def test_investigator_pins_oracle_and_rejects_proxy_and_nonpublic_dns(self):
        self.assertEqual(audit.ROR_V2_ENDPOINT, "https://api.ror.org/v2/organizations")
        self.assertEqual(audit.ROR_SCHEMA_VERSION, "2.1")
        self.assertEqual(audit.PSL_VERSION, "2026-07-25_14-20-03_UTC")
        with mock.patch.dict("os.environ", {"HTTPS_PROXY": "http://proxy.invalid"}, clear=False):
            with self.assertRaisesRegex(ValueError, "proxy"):
                audit._require_no_proxy()
        with mock.patch.object(audit.socket, "getaddrinfo", return_value=[
                (0, 0, 0, "", ("8.8.8.8", 443)), (0, 0, 0, "", ("127.0.0.1", 443))]):
            with self.assertRaisesRegex(ValueError, "non-public"):
                audit._public_addresses("example.edu", 443)

    def test_evaluator_requires_fresh_dual_identity_evidence_and_never_relationships(self):
        ror = audit._attempt(
            {"query": "Example University", "country": "US", "retrieved_at": "2026-08-08T00:00:00Z"},
            provider="ror", status="proposal", url="https://api.ror.org/v2/organizations?query=Example",
            candidate_external_id="https://ror.org/01abcde12",
            candidate_name="  Example University  ", candidate_country="US",
            official_websites=["https://example.edu/", "https://example.edu/"],
            reason="active_ror_v2_exact_name_country_typed_website", payload_sha256="a" * 64)
        official = audit._attempt(
            {"query": "Example University", "country": "US", "retrieved_at": "2026-08-08T00:00:00Z"},
            provider="official", status="corroborated", url="https://example.edu/",
            candidate_external_id="https://ror.org/01abcde12",
            candidate_name="Example University", candidate_country="US", payload_sha256="b" * 64)
        decision = audit.evaluate_identity_attempts([ror, official], "2026-08-09T00:00:00Z")[0]
        self.assertEqual((decision["action"], decision["reason"]),
                         ("eligible_identity_only", "dual_corroborated"))
        self.assertEqual(
            decision["candidate"],
            {
                "ror_id": "https://ror.org/01abcde12",
                "name": "Example University",
                "country": "US",
                "official_websites": ["https://example.edu/"],
                "evidence_oracle_version": registry.EVIDENCE_ORACLE_VERSION,
                "evidence_oracle_sha256": registry.EVIDENCE_ORACLE_SHA256,
                "evidence": [
                    {"provider": "official", "retrieved_at": "2026-08-08T00:00:00Z",
                     "payload_sha256": "b" * 64, "url": "https://example.edu/"},
                    {"provider": "ror", "retrieved_at": "2026-08-08T00:00:00Z",
                     "payload_sha256": "a" * 64,
                     "url": "https://api.ror.org/v2/organizations?query=Example"},
                ],
            },
        )
        self.assertEqual(
            registry.apply_identity_transitions(
                registry.build_registry({}), [decision],
                timestamp="2026-08-09T00:00:00Z", dry_run=True,
            )["resolutions"][0]["action"],
            "create",
        )
        stale = audit.evaluate_identity_attempts(
            [ror, official], "2026-10-01T00:00:00Z")[0]
        self.assertEqual(stale["action"], "pending")
        self.assertNotIn("candidate", stale)
        legacy = dict(ror, url="https://api.ror.org/organizations?query=Example")
        self.assertEqual(
            audit.evaluate_identity_attempts([legacy, official], "2026-08-09T00:00:00Z")[0]["action"],
            "pending",
        )
        unsafe_website = dict(ror, official_websites=["https://other.example.edu/"])
        self.assertEqual(
            audit.evaluate_identity_attempts([unsafe_website, official], "2026-08-09T00:00:00Z")[0]["action"],
            "pending",
        )
        unsafe_alias = dict(ror, query="Example U")
        unsafe_alias_official = dict(official, query="Example U")
        self.assertEqual(
            audit.evaluate_identity_attempts([unsafe_alias, unsafe_alias_official],
                                             "2026-08-09T00:00:00Z")[0]["action"],
            "pending",
        )
        relationship = dict(official, relationship_payload={"type": "part_of"})
        blocked = audit.evaluate_identity_attempts([ror, relationship], "2026-08-09T00:00:00Z")[0]
        self.assertEqual(blocked["reason"], "relationship_payload_requires_review")
        self.assertNotIn("candidate", blocked)
        self.assertEqual(set(blocked), {"query", "country", "action", "reason", "attempts_sha256", "decision_at"})
        firewall_registry = registry.build_registry({})
        rejected = registry.apply_identity_transitions(
            firewall_registry, [dict(decision, relationship_payload={"type": "part_of"})],
            timestamp="2026-08-09T00:00:00Z", dry_run=True,
        )
        self.assertEqual(rejected["resolutions"][0]["action"], "reject")
        self.assertEqual(rejected["registry"]["relationships"], firewall_registry["relationships"])
        missing = audit.evaluate_identity_attempts(
            [dict(ror, country=""), dict(official, country="")], "2026-08-09T00:00:00Z")[0]
        self.assertEqual(missing["reason"], "country_missing")

    def test_evidence_segments_are_content_addressed_and_idempotent(self):
        attempt = audit._attempt(
            {"query": "Example", "country": "US", "retrieved_at": "2026-08-08T00:00:00Z"},
            provider="ror", status="pending", reason="no_match")
        with tempfile.TemporaryDirectory() as directory:
            audit._persist_evidence_segments(directory, [attempt])
            audit._persist_evidence_segments(directory, [attempt])
            root = Path(directory)
            self.assertEqual(len(list((root / "segments").glob("*.jsonl"))), 1)
            self.assertEqual(len((root / "index.jsonl").read_text(encoding="utf-8").splitlines()), 1)
    def test_investigated_apply_rejects_head_mismatch_before_transition(self):
        with tempfile.TemporaryDirectory() as directory:
            decisions = Path(directory) / "decisions.json"
            rows = []
            decisions.write_bytes(audit.canonical_json_bytes({
                "registry_sha256": "wrong", "event_head": self.snapshot["event_head"],
                "ledger_head": "", "cohort_head": "", "decisions": rows,
                "decisions_sha256": audit.canonical_sha256(rows)}))
            args = SimpleNamespace(registry=str(REGISTRY_PATH), decisions=str(decisions),
                expected_registry_sha256=audit.canonical_sha256(self.snapshot),
                expected_event_head=self.snapshot["event_head"], expected_ledger_head="",
                expected_cohort_head="", max_apply=100, timestamp="2026-08-08T00:00:00Z",
                dry_run=True)
            with self.assertRaisesRegex(ValueError, "HEAD_MISMATCH"):
                audit.command_apply_investigated(args)

    def test_investigated_recovery_quarantines_unreferenced_prepared_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            segment = root / "evidence" / "segments" / "a.jsonl"
            segment.parent.mkdir(parents=True)
            segment.write_bytes(b"evidence\n")
            index = root / "evidence" / "index.jsonl"
            index.write_bytes(audit.canonical_json_bytes({
                "segment_sha256": "a", "row_count": 1}))
            temporary = root / "staged"
            temporary.write_bytes(b"staged")
            journal = root / "apply.journal"
            journal.write_bytes(audit.canonical_json_bytes({
                "state": "PREPARED", "evidence_segment": str(segment),
                "evidence_segment_sha256": "a",
                "ledger": str(root / "ledger.jsonl"),
                "ledger_entry": base64.b64encode(b"ledger\n").decode(),
                "publication": [{
                    "target": str(root / "target"),
                    "temporary": str(temporary),
                    "after": base64.b64encode(b"target\n").decode(),
                }],
            }))
            audit._recover_investigated_apply(journal)
            self.assertFalse(journal.exists())
            self.assertTrue((root / "evidence" / "quarantine" / "a.jsonl").exists())
            self.assertFalse(temporary.exists())
            self.assertEqual(index.read_bytes(), b"")

    def test_non_dry_investigated_apply_uses_ledger_and_db_boundary(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            snapshot = copy.deepcopy(self.snapshot)
            for key in (
                    "ledger_head", "cohort_version", "cohort_sha256",
                    "generation_descriptor_sha256", "generation_id"):
                snapshot.pop(key, None)
            registry_path = root / "registry.json"
            registry_path.write_bytes(audit.canonical_json_bytes(snapshot))
            decision = {"pending_id": "pending-1", "query": "Example", "country": "US",
                        "action": "eligible_identity_only", "disposition": "RESOLVED",
                        "reason": "dual_corroborated", "decision_at": "2026-08-08T00:00:00Z"}
            decisions = {"registry_sha256": audit.canonical_sha256(snapshot),
                         "event_head": snapshot["event_head"], "ledger_head": "",
                         "cohort_head": "", "cohort_sha256": audit.canonical_sha256([]),
                         "decisions": [decision]}
            decisions["decisions_sha256"] = audit.canonical_sha256(decisions["decisions"])
            decision_path = root / "decisions.json"
            decision_path.write_bytes(audit.canonical_json_bytes(decisions))
            args = SimpleNamespace(registry=str(registry_path), decisions=str(decision_path),
                expected_registry_sha256=audit.canonical_sha256(snapshot),
                expected_event_head=snapshot["event_head"], expected_ledger_head="",
                expected_cohort_head="", max_apply=100, timestamp="2026-08-08T00:00:00Z",
                dry_run=False, db=str(root / "bibliography.db"), evidence_dir=str(root / "evidence"),
                ledger=str(root / "ledger.jsonl"), corrections=str(root / "corrections.jsonl"),
                baseline=str(root / "baseline.json"), receipt=str(root / "receipt.json"),
                effective_date="2026-08-08", journal=str(root / "journal.json"),
                generation_descriptor=str(root / "generation.json"))
            transition = mock.Mock(return_value={
                "registry": copy.deepcopy(snapshot),
                "resolutions": [{
                    "query": "Example", "country": "US",
                    "action": "eligible_identity_only",
                    "organization_id": "organization-1",
                    "reason": "dual_corroborated",
                }],
            })
            db_heads = {
                "registry_sha256": audit.canonical_sha256(snapshot),
                "event_head": snapshot["event_head"],
                "ledger_head": snapshot["event_head"],
                "cohort_head": "", "generation_descriptor_sha256": "old-descriptor",
                "generation_id": "old-generation",
            }
            with mock.patch.object(
                    audit.affiliation_registry, "apply_identity_transitions", transition,
                    create=True), mock.patch.object(
                        audit, "_apply_decisions_to_db") as apply_db, mock.patch.object(
                            audit, "_database_apply_heads", return_value=db_heads):
                self.assertEqual(audit.command_apply_investigated(args), 0)
            self.assertTrue(Path(args.ledger).exists())
            self.assertFalse(Path(args.journal).exists())
            apply_db.assert_called_once()
    def test_investigated_apply_rejects_incomplete_identity_transition(self):
        decision = {
            "query": "Example", "country": "US",
            "action": "eligible_identity_only",
        }
        with self.assertRaisesRegex(
                ValueError, "INCOMPLETE_IDENTITY_TRANSITION"):
            audit._eligible_resolution_map([decision], [])
        with self.assertRaisesRegex(
                ValueError, "INCOMPLETE_IDENTITY_TRANSITION"):
            audit._eligible_resolution_map([decision], [{
                "query": "Example", "country": "US",
                "action": "reject", "organization_id": None,
            }])

    def test_zero_eligible_apply_finalizes_ledger_join_and_descriptor(self):
        bib = checker.bib
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            snapshot = registry.build_registry({})
            registry_path = root / "registry.json"
            corrections_path = root / "affiliation_registry_corrections.jsonl"
            baseline_path = root / "baseline.json"
            database = root / "bibliography.sqlite3"
            registry_path.write_bytes(audit.canonical_json_bytes(snapshot))
            corrections = registry.correction_projection(snapshot)
            corrections_path.write_bytes(audit._jsonl_bytes(corrections))
            baseline = registry.baseline_projection(
                snapshot, corrections, effective_date="2026-08-08")
            baseline["database_baseline"] = {"sentinel": 1}
            baseline_path.write_bytes(audit.canonical_json_bytes(baseline))

            connection = sqlite3.connect(database)
            connection.execute("PRAGMA foreign_keys=ON")
            connection.executescript(bib.SCHEMA + bib.AFFILIATION_SCHEMA)
            bib.project_affiliation_registry(
                connection, registry=snapshot, ensure_schema=False)
            connection.execute(
                "INSERT INTO affiliation_pending_cases "
                "(pending_id,normalized_raw_name,observed_country_code,"
                "external_identifiers_json,status,reason_code,first_seen_at,"
                "last_seen_at,active_observation_count,lifetime_observation_count) "
                "VALUES (?,?,?,?,?,?,?,?,?,?)",
                ("pending-1", "example", "", "{}", "open", "country_missing",
                 "2026-08-08T00:00:00Z", "2026-08-08T00:00:00Z", 1, 1))
            connection.commit()
            connection.close()

            decision_rows = [{
                "pending_id": "pending-1",
                "query": "Example",
                "country": "",
                "action": "pending",
                "disposition": "COUNTRY_MISSING_OR_UNMAPPABLE",
                "reason": "country_missing",
                "decision_at": "2026-08-08T00:00:00Z",
            }]
            cohort_sha256 = audit.canonical_sha256(["pending-1"])
            decisions = {
                "schema_version": "affiliation-decisions-v1",
                "cohort_sha256": cohort_sha256,
                "decisions": decision_rows,
                "decisions_sha256": audit.canonical_sha256(decision_rows),
                "unclassified_count": 0,
                "heads": {
                    "registry_sha256": audit.canonical_sha256(snapshot),
                    "event_head": snapshot["event_head"],
                    "database_sha256": audit._database_sha256(database),
                },
            }
            decisions_path = root / "decisions.json"
            decisions_path.write_bytes(audit.canonical_json_bytes(decisions))
            args = SimpleNamespace(
                registry=str(registry_path),
                decisions=str(decisions_path),
                expected_registry_sha256="",
                expected_event_head="",
                expected_ledger_head="",
                expected_cohort_head="",
                max_apply=100,
                canary=False,
                timestamp="2026-08-08T00:00:00Z",
                dry_run=False,
                db=str(database),
                evidence_dir=str(root / "evidence"),
                ledger=str(root / "ledger.jsonl"),
                corrections=str(corrections_path),
                baseline=str(baseline_path),
                receipt=str(root / "receipt.json"),
                effective_date="2026-08-08",
                journal=str(root / "journal.json"),
                generation_descriptor=str(root / "generation.json"),
            )

            self.assertEqual(audit.command_apply_investigated(args), 0)
            self.assertFalse(Path(args.journal).exists())
            self.assertEqual(audit._verified_ledger_tail(Path(args.ledger)),
                             registry.load_registry(registry_path)["ledger_head"])
            receipt = json.loads(Path(args.receipt).read_text(encoding="utf-8"))
            descriptor = json.loads(
                Path(args.generation_descriptor).read_text(encoding="utf-8"))
            self.assertTrue(receipt["vacuous_noop"])
            self.assertEqual(receipt["applied_count"], 0)
            self.assertEqual(descriptor["ledger_head"], receipt["ledger_head"])
            self.assertEqual(
                json.loads(baseline_path.read_text(encoding="utf-8"))[
                    "database_baseline"],
                {"sentinel": 1},
            )
            connection = sqlite3.connect(database)
            try:
                joined = connection.execute(
                    "SELECT pending_id,disposition,decision_sha256 "
                    "FROM affiliation_cohort_dispositions").fetchall()
                metadata = connection.execute(
                    "SELECT ledger_head,cohort_sha256,generation_id "
                    "FROM affiliation_registry_metadata WHERE singleton=1").fetchone()
            finally:
                connection.close()
            self.assertEqual(joined, [(
                "pending-1", "COUNTRY_MISSING_OR_UNMAPPABLE",
                decisions["decisions_sha256"])])
            self.assertEqual(metadata, (
                receipt["ledger_head"], cohort_sha256,
                descriptor["generation_id"]))
