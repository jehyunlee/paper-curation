"""Focused contract tests for incremental related-paper refresh.

The real SPECTER/Anthropic implementations are deliberately replaced here: these
are orchestration tests and must never spend provider money.
"""
from __future__ import annotations

import importlib
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE))

# Preload C-extension imports before any temporary module substitution.
import numpy as np
import topic_modeling
from lib import specter2_embed


class RefreshConnectionsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.docs, self.papers = root / "docs", root / "docs" / "papers"
        self.papers.mkdir(parents=True)
        self.slug, self.other = "11482_Into_the_Unknown", "11483_Neighbor"
        self.index = [
            {"slug": self.slug, "title": "Unknown", "topics": ["demo"], "classifications": {}},
            {"slug": self.other, "title": "Neighbor", "topics": ["demo"]},
        ]
        (self.papers / "_papers_index.json").write_text(json.dumps(self.index))
        for slug in (self.slug, self.other):
            d = self.papers / slug
            d.mkdir()
            (d / "review.md").write_text("# review")
            (d / "originality.md").write_text(slug)
        d = self.docs / "demo"
        d.mkdir()
        (d / "_embeddings_cache.json").write_text(json.dumps({
            "embed_model": "test", "slugs": [self.other], "embeddings": [[1.0, 0.0]],
            "originality_sha256": {},
        }))
        self.mod = importlib.reload(importlib.import_module("refresh_paper_connections"))
        self.paths = patch.multiple(self.mod, PAPERS_DIR=self.papers, DOCS_DIR=self.docs)
        self.paths.start()

    def tearDown(self):
        self.paths.stop()
        self.tmp.cleanup()

    def test_plan_handles_unclassified_review_without_paid_calls(self):
        with patch.dict("sys.modules", {"lib.specter2_embed": None, "anthropic": None}):
            result = self.mod.plan_connections(self.slug)
        self.assertEqual(result["status"], "ready")
        self.assertNotIn("max_cost_usd", result)
        self.assertTrue(result["embedding_required"])
        self.assertEqual(result["topics"], ["demo"])

    def test_plan_rejects_invalid_slug_without_a_cost_argument(self):
        with self.assertRaises(ValueError):
            self.mod.plan_connections("../bad")
        with self.assertRaises(TypeError):
            self.mod.plan_connections(self.slug, max_cost_usd=.1)

    def test_refresh_preserves_unrelated_global_sources_and_renders_old_incoming(self):
        # Existing link to old is deliberately included: replacing target claims
        # must update its page/view, while a different paper's global edge remains.
        old = "11484_Old"
        self.index.append({"slug": old, "title": "Old", "topics": ["demo"]})
        (self.papers / "_papers_index.json").write_text(json.dumps(self.index))
        (self.docs / "demo" / "_embeddings_cache.json").write_text(json.dumps({
            "embed_model": "test", "slugs": [self.other, old],
            "embeddings": [[1.0, 0.0], [0.0, 1.0]], "originality_sha256": {},
        }))
        d = self.papers / old
        d.mkdir(); (d / "review.md").write_text("# old"); (d / "originality.md").write_text(old)
        calls, events = [], []
        fake_connections = {self.slug: [{"slug": self.other, "basis": "model"}]}
        with patch.object(self.mod, "_embedding_for_target", return_value=(self.index[:2], [[0, 1], [1, 0]])), \
             patch.object(topic_modeling, "compute_related_candidates", return_value={self.slug: [(self.other, .9)]}), \
             patch.object(self.mod, "_judge_or_raise", return_value=fake_connections), \
             patch("lib.connections.load_global_connections", return_value={
                 self.slug: [{"slug": old, "source_topic": "demo"}],
                 "99999_Keep": [{"slug": self.other, "source_topic": "other"}],
             }), \
             patch("lib.connections.merge_to_global", side_effect=lambda *a, **k: events.append("merge")), \
             patch("lib.connections.sync_topic_connections", side_effect=lambda *a, **k: (events.append("sync"), calls.append(a))), \
             patch("review_to_html._run_review_to_html", return_value={"converted": 3, "skipped": 0}):
            result = self.mod._refresh_connections_locked(self.slug)
        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["related_count"], 1)
        self.assertIn(str(self.papers / old / "index.html"), result["outputs"])
        self.assertEqual(len(calls), 1)
        self.assertEqual(events[0], "merge")

    def test_public_refresh_owns_exclusive_operation_lock(self):
        entered = []
        class Lock:
            def __enter__(self): entered.append(True)
            def __exit__(self, *_): return False
        with patch("lib.corpus_store.corpus_operation_lock", return_value=Lock()) as lock, \
             patch.object(self.mod, "_refresh_connections_locked", return_value={"status": "completed"}):
            self.mod.refresh_connections(self.slug)
        self.assertEqual(lock.call_args.kwargs, {"exclusive": True})
        self.assertEqual(entered, [True])

    def test_missing_embedding_plan_counts_whole_corpus(self):
        plan = self.mod.plan_connections(self.slug)
        self.assertEqual(plan["topic_plan"][0]["missing_embedding_count"], 1)

    def test_model_mismatch_is_rejected_before_embedding(self):
        with patch.object(specter2_embed, "EMBED_TAG", "other"):
            with self.assertRaises(ValueError):
                self.mod._embedding_for_target(self.slug, self.index[0], "demo", self.index)

    def test_repeated_embedding_update_does_not_recompute_source_vector(self):
        cache = self.docs / "demo" / "_embeddings_cache.json"
        cache.write_text(json.dumps({
            "embed_model": specter2_embed.EMBED_TAG, "slugs": [self.other],
            "embeddings": [[1.0, 0.0]], "originality_sha256": {},
        }))
        embed = patch.object(specter2_embed, "embed_texts",
                            return_value=np.asarray([[0.0, 1.0]]))
        with embed as mock_embed:
            self.mod._embedding_for_target(self.slug, self.index[0], "demo", self.index)
            self.mod._embedding_for_target(self.slug, self.index[0], "demo", self.index)
        self.assertEqual(mock_embed.call_count, 1)
        self.assertEqual(mock_embed.call_args.args[0], [self.slug])

    def test_symlink_and_topic_traversal_are_rejected(self):
        self.index[0]["topics"] = ["../escape"]
        (self.papers / "_papers_index.json").write_text(json.dumps(self.index))
        with self.assertRaises(ValueError):
            self.mod.plan_connections(self.slug)

    def test_render_shortfall_never_completes(self):
        with patch("review_to_html._run_review_to_html", return_value={"converted": 0, "skipped": 1}):
            # Directly cover the post-render contract through a minimal locked
            # run; all upstream stages are fixed, so no provider is reached.
            with patch.object(self.mod, "plan_connections", return_value={}), \
                 patch.object(self.mod, "_context", return_value=(self.index[0], self.index, ["demo"])), \
                 patch.object(self.mod, "_embedding_for_target", return_value=(self.index, [[0, 1], [1, 0]])), \
                 patch.object(topic_modeling, "compute_related_candidates", return_value={self.slug: []}), \
                 patch.object(self.mod, "_judge_or_raise", return_value={self.slug: []}), \
                 patch("lib.connections.load_global_connections", return_value={}), \
                 patch("lib.connections.merge_to_global"), \
                 patch("lib.connections.sync_topic_connections"):
                with self.assertRaises(RuntimeError):
                    self.mod._refresh_connections_locked(self.slug)

    def test_cli_reports_failed_schema(self):
        with patch.object(self.mod, "plan_connections", side_effect=ValueError("bad")):
            with patch.object(sys, "argv", ["refresh_paper_connections.py", "--slug", self.slug]), \
                 patch("builtins.print") as printed:
                self.assertEqual(self.mod.main(), 1)
        result = json.loads(printed.call_args.args[0])
        self.assertEqual(result["status"], "failed")
        self.assertEqual(result["schema_version"], 1)

    def test_all_unrelated_is_completed_but_metadata_fallback_is_failure(self):
        raw = {self.slug: [{"slug": self.other, "basis": "metadata"}]}
        # The judge adapter's explicit postcondition distinguishes a valid empty
        # result (all unrelated) from its unsafe metadata fallback.
        with patch.dict("os.environ", {"RELATION_JUDGE": "on"}), \
             patch("lib.credentials.resolve_credential", return_value="key"), \
             patch.dict("sys.modules", {"anthropic": type("A", (), {"Anthropic": lambda **_: object()})}), \
             patch("lib.relation_judge.judge_connections", return_value={self.slug: []}):
            self.assertEqual(self.mod._judge_or_raise(raw, self.index, "demo"), {self.slug: []})
        with patch.dict("os.environ", {"RELATION_JUDGE": "on"}), \
             patch("lib.credentials.resolve_credential", return_value="key"), \
             patch.dict("sys.modules", {"anthropic": type("A", (), {"Anthropic": lambda **_: object()})}), \
             patch("lib.relation_judge.judge_connections", return_value=raw):
            with self.assertRaises(RuntimeError):
                self.mod._judge_or_raise(raw, self.index, "demo")

    def test_refresh_uses_relation_judge_default_model(self):
        raw = {self.slug: [{"slug": self.other, "basis": "metadata"}]}
        observed = []

        def fake_judge(*_args, **_kwargs):
            observed.append(os.environ["RELATION_JUDGE_MODEL"])
            return {self.slug: []}

        with patch.dict("os.environ", {"RELATION_JUDGE": "on"}, clear=False), \
             patch("lib.credentials.resolve_credential", return_value="key"), \
             patch.dict("sys.modules", {"anthropic": type("A", (), {"Anthropic": lambda **_: object()})}), \
             patch("lib.relation_judge.judge_connections", side_effect=fake_judge):
            self.mod._judge_or_raise(raw, self.index, "demo")
        from lib.relation_judge import DEFAULT_MODEL
        self.assertEqual(observed, [DEFAULT_MODEL])

    def test_disabled_judge_is_incomplete_not_all_unrelated(self):
        raw = {self.slug: [{"slug": self.other, "basis": "metadata"}]}
        with patch.dict("os.environ", {"RELATION_JUDGE": "off"}):
            with self.assertRaises(RuntimeError):
                self.mod._judge_or_raise(raw, self.index, "demo")


if __name__ == "__main__":
    unittest.main()
