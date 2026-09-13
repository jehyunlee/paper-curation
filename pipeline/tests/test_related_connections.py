"""Focused regression coverage for deterministic related-paper connections.

The test replaces embedding retrieval and provider construction, so it never
loads SPECTER2 weights or contacts an LLM service.
"""
from __future__ import annotations

import contextlib
import ast
import importlib
import io
import os
import sys
import types
import unittest
from unittest.mock import patch

PIPELINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PIPELINE not in sys.path:
    sys.path.insert(0, PIPELINE)

from lib.related import build_connections  # noqa: E402


PAPERS = [
    {"slug": "001_Source", "authors": ["Ada Lovelace"], "date": "2024",
     "classifications": {"demo": {"primary_category": "Methods"}}},
    {"slug": "002_Earlier", "authors": ["Ada Lovelace"], "date": "2022",
     "classifications": {"demo": {"primary_category": "Methods"}}},
    {"slug": "003_Alternative", "authors": ["Grace Hopper"], "date": "2025",
     "classifications": {"demo": {"primary_category": "Applications"}}},
]


class DeterministicBuilderTests(unittest.TestCase):
    def test_relation_limit_and_empty_results_are_deterministic(self):
        candidates = {
            "001_Source": [("002_Earlier", 0.91), ("003_Alternative", 0.88)],
            "003_Alternative": [],
        }
        result = build_connections(candidates, PAPERS, topic="demo", limit=1)

        self.assertEqual(result["003_Alternative"], [])
        self.assertEqual(len(result["001_Source"]), 1)
        link = result["001_Source"][0]
        self.assertEqual(link["slug"], "002_Earlier")
        self.assertEqual(link["relation"], "foundation")
        self.assertIn("SPECTER2", link["reason"])
        self.assertEqual(link["evidence"]["shared_authors"], ["lovelace"])


class ExtractInsightsWiringTests(unittest.TestCase):
    def setUp(self):
        self.topic_modeling = types.ModuleType("topic_modeling")
        self.topic_modeling.extract_originalities = lambda papers: papers
        self.topic_modeling.compute_embeddings = lambda originalities, cache_path: (
            "fake-embeddings", [paper["slug"] for paper in originalities]
        )
        self.topic_modeling.compute_related_candidates = lambda embeddings, slugs, top_k, papers: {
            "001_Source": [("002_Earlier", 0.91)],
            "002_Earlier": [("001_Source", 0.91)],
            "003_Alternative": [],
        }
        self.modules = patch.dict(sys.modules, {"topic_modeling": self.topic_modeling})
        self.modules.start()
        sys.modules.pop("extract_insights", None)
        self.ei = importlib.import_module("extract_insights")

    def tearDown(self):
        sys.modules.pop("extract_insights", None)
        self.modules.stop()

    def test_connection_caller_uses_builder_without_provider_client(self):
        # Three papers make this category eligible; no client argument exists for
        # a connection judge to consume.
        connections = self.ei.extract_paper_connections(
            "demo", {"Methods": PAPERS}, PAPERS
        )
        self.assertEqual(connections["001_Source"][0]["relation"], "foundation")
        self.assertEqual(connections["003_Alternative"], [])

    def test_narrow_and_other_categories_do_not_become_targets(self):
        connections = self.ei.extract_paper_connections(
            "demo",
            {"Other": PAPERS, "Too small": PAPERS[:2]},
            PAPERS,
        )
        self.assertEqual(connections, {})

    def test_scoped_sources_use_the_full_cross_category_pool(self):
        cross_category = {
            "slug": "004_Cross_Category", "authors": ["Linus Torvalds"],
            "date": "2023",
            "classifications": {"demo": {"primary_category": "Applications"}},
        }
        pool = PAPERS + [cross_category]
        seen = {}

        def candidates(embeddings, slugs, top_k, papers):
            seen["pool"] = papers
            return {
                "001_Source": [("004_Cross_Category", 0.92)],
                "002_Earlier": [], "003_Alternative": [],
                "004_Cross_Category": [("001_Source", 0.92)],
            }

        self.topic_modeling.compute_related_candidates = candidates
        connections = self.ei.extract_paper_connections(
            "demo", {"Methods": PAPERS}, pool
        )
        self.assertEqual(seen["pool"], pool)
        self.assertEqual(connections["001_Source"][0]["slug"], "004_Cross_Category")
        self.assertNotIn("004_Cross_Category", connections)

    def test_persistence_receives_empty_results_once(self):
        with patch("lib.connections.sync_topic_connections") as sync:
            self.ei.extract_paper_connections(
                "demo", {"Methods": PAPERS}, PAPERS,
                topic_dir="/tmp/demo", topic_slugs=[paper["slug"] for paper in PAPERS],
            )
        sync.assert_called_once()
        persisted = sync.call_args.args[0]
        self.assertEqual(persisted["003_Alternative"], [])

    def test_persistence_failure_reaches_the_caller(self):
        with patch("lib.connections.sync_topic_connections",
                   side_effect=OSError("disk unavailable")):
            with self.assertRaisesRegex(OSError, "disk unavailable"):
                self.ei.extract_paper_connections(
                    "demo", {"Methods": PAPERS}, PAPERS,
                    topic_dir="/tmp/demo", topic_slugs=[paper["slug"] for paper in PAPERS],
                )

    def test_connections_only_does_not_construct_a_provider(self):
        with patch.object(self.ei, "load_topic_data", return_value=(PAPERS, {"Methods": PAPERS}, [])), \
             patch.object(self.ei, "get_topic_dir", return_value="/tmp/demo"), \
             patch.object(self.ei, "extract_paper_connections", return_value={}) as extract, \
             patch.object(self.ei, "Anthropic", side_effect=AssertionError("judge constructed")):
            self.ei._run_insights("demo", connections_only=True)
        extract.assert_called_once()

    def test_cli_no_longer_accepts_seed_cache_flag(self):
        with patch.object(self.ei, "_run_insights") as run, \
             patch.object(sys, "argv", ["extract_insights.py", "--connections-only"]):
            self.ei.main()
        run.assert_called_once_with(topic="ai4s", insights_only=False,
                                    connections_only=True, categories=None)

        with patch.object(sys, "argv", ["extract_insights.py", "--seed-cache-only"]), \
             contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as error:
                self.ei.main()
        self.assertEqual(error.exception.code, 2)


class TopicModelingCliTests(unittest.TestCase):
    def test_main_passes_only_supported_defaults_to_programmatic_entrypoint(self):
        source_path = os.path.join(PIPELINE, "topic_modeling.py")
        tree = ast.parse(open(source_path, encoding="utf-8").read(), source_path)
        main = next(node for node in tree.body
                    if isinstance(node, ast.FunctionDef) and node.name == "main")
        calls = []
        namespace = {
            "argparse": __import__("argparse"),
            "_run_topic_model": lambda **kwargs: calls.append(kwargs),
        }
        exec(compile(ast.Module(body=[main], type_ignores=[]), source_path, "exec"),
             namespace)
        with patch.object(sys, "argv", ["topic_modeling.py"]):
            namespace["main"]()
        self.assertEqual(calls, [{
            "topic": "ai4s",
            "skip_connections": False,
            "skip_classification": False,
            "min_cats": 8,
            "max_cats": 12,
        }])


if __name__ == "__main__":
    unittest.main()
