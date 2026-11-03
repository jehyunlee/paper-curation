"""Network membership follows topic/search views without rebuilding relations."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import generate_network as builder  # noqa: E402


class NetworkMembershipTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.docs = Path(temporary.name) / "docs"
        self.papers = self.docs / "papers"
        self.papers.mkdir(parents=True)
        for topic in ("alpha", "beta", "_cross"):
            (self.docs / topic).mkdir()
        self.alpha = {
            "slug": "001_alpha", "title": "Alpha Paper", "date": "2024",
            "primary_topic": "alpha", "topics": ["alpha", "beta"],
            "classifications": {
                "alpha": {"primary_category": "Alpha Category", "sub_category": "Alpha Sub"},
                "beta": {
                    "primary_category": "Beta Category", "sub_category": "Beta Sub",
                    "all_categories": ["Beta Category", "Another Category"],
                },
            },
        }
        self.beta = {
            "slug": "002_beta", "title": "Beta Paper", "date": "2025",
            "primary_topic": "beta", "topics": ["beta"],
            "classifications": {"beta": {"primary_category": "Beta Category"}},
        }
        self.excluded = {
            "slug": "003_excluded", "title": "Not in Search", "date": "2023",
            "primary_topic": "alpha", "topics": ["alpha", "_cross"],
            "classifications": {"alpha": {"primary_category": "Excluded Category"}},
        }
        self.primary_only = {
            "slug": "004_primary", "title": "Primary Only", "date": "2026",
            "primary_topic": "alpha", "topics": None,
            "classifications": {"alpha": {"primary_category": "Primary Category"}},
        }
        self.index_path = self.papers / "_papers_index.json"
        self._write_json(self.index_path, [
            self.alpha, self.beta, self.excluded, self.primary_only,
        ])
        self.cross_index = self.docs / "_cross" / "_search_index.json"
        self._write_json(self.cross_index, {"papers": {
            "001_alpha": {"category": "Beta Category"},
            "002_beta": {"category": "Beta Category"},
            "not-in-authoritative-index": {"category": "Ignored"},
            "_note_private": {"category": "Personal Notes"},
        }})
        for patcher in (
            patch.object(builder, "PAPERS_DIR", str(self.papers)),
            patch.object(builder, "get_topic_dir", side_effect=lambda topic: self.docs / topic),
        ):
            patcher.start()
            self.addCleanup(patcher.stop)

    @staticmethod
    def _write_json(path, payload):
        path.write_text(json.dumps(payload), encoding="utf-8")

    @staticmethod
    def _html_data(html, name):
        prefix = f"const {name} = "
        line = next(line for line in html.splitlines() if line.startswith(prefix))
        return json.loads(line[len(prefix):-1])

    def test_cross_uses_search_membership_deduplicates_and_keeps_source_classification(self):
        self._write_json(self.index_path, [
            self.alpha, self.beta, self.excluded, self.primary_only, self.alpha,
        ])
        before_papers = self.index_path.read_bytes()
        before_search = self.cross_index.read_bytes()

        nodes, links, colors, _, _, _, _, node_conns = builder.build_network_data("_cross")

        self.assertEqual([node["id"] for node in nodes], ["001_alpha", "002_beta"])
        alpha = nodes[0]
        self.assertEqual(alpha["category"], "Beta Category")
        self.assertEqual(alpha["sub_category"], "Beta Sub")
        self.assertEqual(alpha["all_categories"], ["Beta Category", "Another Category"])
        self.assertTrue(alpha["multi"])
        self.assertEqual(set(colors), {"Beta Category"})
        self.assertEqual(links, [])
        self.assertEqual(node_conns, {})
        self.assertEqual(self.index_path.read_bytes(), before_papers)
        self.assertEqual(self.cross_index.read_bytes(), before_search)

    def test_cross_without_category_uses_primary_source_not_aggregate_classification(self):
        self.alpha["classifications"]["_cross"] = {"primary_category": "Wrong Aggregate"}
        self._write_json(self.index_path, [self.alpha])
        self._write_json(self.cross_index, {"papers": {"001_alpha": {}}})

        nodes, *_ = builder.build_network_data("_cross")

        self.assertEqual(nodes[0]["category"], "Alpha Category")
        self.assertEqual(nodes[0]["sub_category"], "Alpha Sub")

    def test_cross_can_use_source_metadata_without_classifications(self):
        self.alpha.pop("classifications")
        self._write_json(self.index_path, [self.alpha])

        nodes, *_ = builder.build_network_data("_cross")

        self.assertEqual(nodes[0]["category"], "Beta Category")

    def test_dedicated_topic_includes_primary_only_and_secondary_members(self):
        self.cross_index.unlink()
        self._write_json(self.index_path, [
            self.alpha, self.beta, self.excluded, self.primary_only, self.alpha,
        ])
        self._write_json(self.docs / "alpha" / "_paper_connections.json", {
            "001_alpha": [
                {"slug": "004_primary", "relation": "extension", "reason": "Existing forward reason"},
                {"slug": "002_beta", "relation": "alternative", "reason": "Outside this topic"},
            ],
            "004_primary": [
                {"slug": "001_alpha", "relation": "foundation", "reason": "Existing reverse reason"},
            ],
        })

        nodes, links, _, _, _, _, _, node_conns = builder.build_network_data("alpha")

        self.assertEqual([node["id"] for node in nodes], [
            "001_alpha", "003_excluded", "004_primary",
        ])
        self.assertEqual(nodes[0]["category"], "Alpha Category")
        self.assertEqual(nodes[0]["sub_category"], "Alpha Sub")
        self.assertEqual(len(links), 1)
        self.assertEqual({links[0]["source"], links[0]["target"]}, {"001_alpha", "004_primary"})
        self.assertEqual(links[0]["relation"], "foundation")
        self.assertEqual(links[0]["reason"], "Existing reverse reason")
        self.assertEqual(node_conns["001_alpha"], [{
            "o": "004_primary", "r": [["extension", "Existing forward reason"]],
        }])

        beta_nodes, *_ = builder.build_network_data("beta")
        self.assertEqual([node["id"] for node in beta_nodes], ["001_alpha", "002_beta"])
        self.assertEqual(beta_nodes[0]["category"], "Beta Category")

    def test_missing_connections_publishes_cross_nodes_without_inventing_edges(self):
        before_papers = self.index_path.read_bytes()
        before_search = self.cross_index.read_bytes()

        path = builder._run_network("_cross")

        self.assertEqual(Path(path), self.docs / "_cross" / "network.html")
        html = Path(path).read_text(encoding="utf-8")
        self.assertEqual([node["id"] for node in self._html_data(html, "nodesRaw")], [
            "001_alpha", "002_beta",
        ])
        self.assertEqual(self._html_data(html, "linksRaw"), [])
        self.assertEqual(self._html_data(html, "NODECONNS"), {})
        self.assertFalse((self.docs / "_cross" / "_paper_connections.json").exists())
        self.assertEqual(self.index_path.read_bytes(), before_papers)
        self.assertEqual(self.cross_index.read_bytes(), before_search)

    def test_cross_filters_existing_edges_to_search_members_and_preserves_reasons(self):
        self._write_json(self.docs / "_cross" / "_paper_connections.json", {
            "001_alpha": [
                {
                    "slug": "002_beta", "relation": "alternative", "reason": "Existing reason",
                    "reasons": [
                        {"relation": "alternative", "reason": "Existing reason"},
                        {"relation": "counterpoint", "reason": "Existing second reason"},
                    ],
                },
                {"slug": "003_excluded", "relation": "extension", "reason": "Not a member"},
            ],
            "003_excluded": [
                {"slug": "002_beta", "relation": "foundation", "reason": "Not a member"},
            ],
        })

        _, links, _, _, _, _, _, node_conns = builder.build_network_data("_cross")

        self.assertEqual(len(links), 1)
        self.assertEqual(links[0]["source"], "001_alpha")
        self.assertEqual(links[0]["target"], "002_beta")
        self.assertEqual(links[0]["reason"], "Existing reason")
        self.assertEqual(node_conns["001_alpha"], [{
            "o": "002_beta", "r": [
                ["alternative", "Existing reason"],
                ["counterpoint", "Existing second reason"],
            ],
        }])

    def test_empty_cross_membership_does_not_fall_back_to_literal_topic(self):
        self._write_json(self.cross_index, {"papers": {}})

        nodes, links, *_ = builder.build_network_data("_cross")

        self.assertEqual(nodes, [])
        self.assertEqual(links, [])

    def test_malformed_connections_fail_without_replacing_existing_network(self):
        malformed = [
            "{", "[]", "null",
            json.dumps({"001_alpha": None}),
            json.dumps({"001_alpha": {}}),
            json.dumps({"001_alpha": [None]}),
            json.dumps({"001_alpha": [{}]}),
            json.dumps({"001_alpha": [{"slug": "../outside"}]}),
            json.dumps({"001_alpha": [{"slug": "002_beta", "relation": []}]}),
            json.dumps({"001_alpha": [{"slug": "002_beta", "reason": 4}]}),
            json.dumps({"001_alpha": [{"slug": "002_beta", "reasons": {}}]}),
            json.dumps({"001_alpha": [{"slug": "002_beta", "reasons": None}]}),
            json.dumps({"001_alpha": [{"slug": "002_beta", "reasons": [None]}]}),
            json.dumps({"001_alpha": [{"slug": "002_beta", "reasons": [{"reason": []}]}]}),
            json.dumps({"not-in-this-topic": [None]}),
        ]
        for topic in ("alpha", "_cross"):
            output = self.docs / topic / "network.html"
            output.write_text("existing network", encoding="utf-8")
            connections = self.docs / topic / "_paper_connections.json"
            for payload in malformed:
                with self.subTest(topic=topic, payload=payload):
                    connections.write_text(payload, encoding="utf-8")
                    with self.assertRaises(ValueError):
                        builder._run_network(topic)
                    self.assertEqual(output.read_text(encoding="utf-8"), "existing network")

    def test_missing_cross_index_fails_instead_of_using_literal_topic(self):
        self.cross_index.unlink()
        output = self.docs / "_cross" / "network.html"
        output.write_text("existing network", encoding="utf-8")

        with self.assertRaises(FileNotFoundError):
            builder._run_network("_cross")

        self.assertEqual(output.read_text(encoding="utf-8"), "existing network")

    def test_malformed_cross_membership_is_rejected_before_replacing_network(self):
        malformed = [
            "{", "[]", "null", "{}", json.dumps({"papers": []}),
            json.dumps({"papers": {"": {}}}),
            json.dumps({"papers": {"../outside": {}}}),
            json.dumps({"papers": {"folder\\paper": {}}}),
            json.dumps({"papers": {"001_alpha": None}}),
            json.dumps({"papers": {"001_alpha": []}}),
            json.dumps({"papers": {"001_alpha": {"category": []}}}),
        ]
        output = self.docs / "_cross" / "network.html"
        output.write_text("existing network", encoding="utf-8")
        for payload in malformed:
            with self.subTest(payload=payload):
                self.cross_index.write_text(payload, encoding="utf-8")
                with self.assertRaises(ValueError):
                    builder._run_network("_cross")
                self.assertEqual(output.read_text(encoding="utf-8"), "existing network")


if __name__ == "__main__":
    unittest.main()
