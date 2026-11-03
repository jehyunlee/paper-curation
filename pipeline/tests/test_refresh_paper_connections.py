"""Focused contract tests for incremental related-paper refresh.

The real SPECTER2 encoder and pair explainer are replaced here: these are
orchestration tests for local retrieval and grounded cloud explanations.
"""
from __future__ import annotations

import hashlib
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
from lib import connections as connection_store, specter2_embed


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
        self.paper_texts = {
            self.slug: "Unknown selects experiments using calibrated uncertainty from a fixed candidate pool.",
            self.other: "Neighbor selects experiments using ensemble disagreement from a fixed candidate pool.",
        }
        self.paper_methods = {self.slug: "보정된 불확실도", self.other: "앙상블 예측의 불일치"}
        (self.papers / "_papers_index.json").write_text(json.dumps(self.index))
        for slug in (self.slug, self.other):
            d = self.papers / slug
            d.mkdir()
            (d / "review.md").write_text("# review")
            (d / "originality.md").write_text(slug)
            (d / "text.md").write_text(self.paper_texts[slug], encoding="utf-8")
        d = self.docs / "demo"
        d.mkdir()
        (d / "_embeddings_cache.json").write_text(json.dumps({
            "embed_model": "test", "slugs": [self.other], "embeddings": [[1.0, 0.0]],
            "originality_sha256": {},
        }))
        self.mod = importlib.reload(importlib.import_module("refresh_paper_connections"))
        self.paths = patch.multiple(self.mod, PAPERS_DIR=self.papers, DOCS_DIR=self.docs)
        self.paths.start()
        self.connection_paths = patch.multiple(
            connection_store, PAPERS_DIR=str(self.papers),
            GLOBAL_CONN_PATH=str(self.papers / "_global_connections.json"))
        self.connection_paths.start()
        self.explainer = patch("lib.related.explain_pair", side_effect=self._explain_pair)
        self.explain_pair = self.explainer.start()

    def tearDown(self):
        self.explainer.stop()
        self.connection_paths.stop()
        self.paths.stop()
        self.tmp.cleanup()

    def _explain_pair(self, source, target):
        def reason(first, second):
            return (f"{first['title']}와 {second['title']}는 제한된 후보에서 다음 실험을 선택하는 문제를 공유한다. "
                    f"{first['title']}에서 사용하는 {self.paper_methods[first['slug']]} 기준을 "
                    f"{second['title']}의 {self.paper_methods[second['slug']]} 기준과 비교할 수 있다.")

        def evidence(first, second):
            first_text, second_text = self.paper_texts[first["slug"]], self.paper_texts[second["slug"]]
            return {"source_quote": first_text, "target_quote": second_text,
                    "source_sha256": hashlib.sha256(first_text.encode("utf-8")).hexdigest(),
                    "target_sha256": hashlib.sha256(second_text.encode("utf-8")).hexdigest(),
                    "provider": "anthropic", "prompt_version": "test-grounded-pairs-v1"}

        return {"relation": "alternative", "reason": reason(source, target),
                "model": "test-grounded-explainer", "evidence": evidence(source, target),
                "reverse": {"relation": "alternative", "reason": reason(target, source),
                            "evidence": evidence(target, source)}}

    def _add_paper(self, slug, title, topic, method):
        paper = {"slug": slug, "title": title, "topics": [topic]}
        self.index.append(paper)
        self.paper_texts[slug] = f"{title} selects experiments using {method} from a fixed candidate pool."
        self.paper_methods[slug] = method
        directory = self.papers / slug
        directory.mkdir()
        (directory / "review.md").write_text(f"# {title} review", encoding="utf-8")
        (directory / "text.md").write_text(self.paper_texts[slug], encoding="utf-8")
        (self.docs / topic).mkdir(exist_ok=True)
        (self.papers / "_papers_index.json").write_text(json.dumps(self.index), encoding="utf-8")
        return paper

    def _legacy_edge(self, target, cosine, topic):
        return {"slug": target, "relation": "alternative", "reason": "old cosine-only explanation",
                "basis": "embedding", "model": "", "evidence": {"cosine": cosine},
                "source_topic": topic}

    def _connection_fixture(self, stored, topics):
        path = self.papers / "_global_connections.json"
        path.write_text(json.dumps(stored, ensure_ascii=False), encoding="utf-8")
        view = connection_store.make_bidirectional_deduped(
            connection_store.load_global_connections(),
            resolve=connection_store.build_slug_resolver(p["slug"] for p in self.index))
        for topic in topics:
            directory = self.docs / topic
            directory.mkdir(exist_ok=True)
            slugs = [p["slug"] for p in self.index if topic == "_cross" or topic in p["topics"]]
            (directory / "_paper_connections.json").write_text(
                json.dumps(connection_store.filter_for_topic(view, slugs), ensure_ascii=False),
                encoding="utf-8")
        return path

    def test_plan_declares_cloud_explanations_without_paid_calls(self):
        with patch.dict("sys.modules", {"lib.specter2_embed": None, "anthropic": None}):
            result = self.mod.plan_connections(self.slug)
        self.assertEqual(result["status"], "ready")
        self.assertNotIn("max_cost_usd", result)
        self.assertTrue(result["embedding_required"])
        self.assertEqual(result["topics"], ["demo"])
        self.assertEqual(result["explanation"]["provider"], "anthropic")
        self.assertEqual(result["explanation"]["cost_class"], "paid")
        self.explain_pair.assert_not_called()

    def test_plan_rejects_invalid_slug_without_a_cost_argument(self):
        with self.assertRaises(ValueError):
            self.mod.plan_connections("../bad")
        with self.assertRaises(TypeError):
            self.mod.plan_connections(self.slug, max_cost_usd=.1)

    def test_refresh_preserves_unrelated_global_sources_and_renders_old_neighbours(self):
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
        events, saved = [], []
        with patch.object(self.mod, "_embedding_for_target", return_value=(self.index[:2], [[0, 1], [1, 0]])), \
             patch.object(topic_modeling, "compute_related_candidates", return_value={self.slug: [(self.other, .9)]}), \
             patch.object(self.mod, "_load_raw_connections", return_value={
                 self.slug: [{"slug": old, "source_topic": "demo"}],
                 "99999_Keep": [{"slug": self.other, "source_topic": "other"}],
             }), \
             patch("lib.connections.save_global_connections",
                   side_effect=lambda store: (events.append("save"), saved.append(store))) as save, \
             patch("lib.atomic_io.atomic_write_json", side_effect=lambda *a, **k: events.append("view")), \
             patch("review_to_html._run_review_to_html", return_value={"converted": 3, "skipped": 0}):
            result = self.mod._refresh_connections_locked(self.slug)
        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["related_count"], 1)
        self.assertIn(str(self.papers / old / "index.html"), result["outputs"])
        self.assertEqual(saved[0]["99999_Keep"], [{"slug": self.other, "source_topic": "other"}])
        save.assert_called_once()
        self.assertEqual(events, ["save", "view"])

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

    def test_connection_refresh_updates_affected_topic_views_after_releasing_lease(self):
        import refresh_paper_views as views
        from lib.corpus_store import corpus_operation_lock

        published = {"status": "completed", "topics": ["demo", "old-neighbor-topic"],
                     "related_count": 1, "outputs": [str(self.papers / "_global_connections.json")]}
        report = {"status": "completed", "topics": published["topics"], "steps": [], "errors": []}
        def refresh(slug, **kwargs):
            self.assertEqual(slug, self.slug)
            self.assertEqual(kwargs, {"papers_dir": self.papers,
                                      "previous_topics": ["demo", "old-neighbor-topic"]})
            with corpus_operation_lock(self.papers, exclusive=True, timeout=0):
                pass
            return report

        with patch.object(views, "PAPERS_DIR", self.papers), \
             patch.object(views, "refresh_paper_views", side_effect=refresh) as refresh_views, \
             patch.object(self.mod, "_refresh_connections_locked", return_value=published):
            result = self.mod.refresh_connections(self.slug)
        self.assertEqual(result["status"], "completed", result)
        self.assertEqual(result["views"], report)
        refresh_views.assert_called_once()

    def test_view_failure_retains_successful_connection_outputs_and_retry_command(self):
        import refresh_paper_views as views

        path = self.papers / "_global_connections.json"
        stored = {self.slug: [{"slug": self.other, "reason": "Retain this published explanation"}]}
        path.write_text(json.dumps(stored), encoding="utf-8")
        report = {"status": "failed", "topics": ["demo"], "steps": [],
                  "errors": ["demo/network: unavailable"],
                  "retry_command": f"python refresh_paper_views.py --slug {self.slug}"}
        with patch.object(views, "PAPERS_DIR", self.papers), \
             patch.object(views, "refresh_paper_views", return_value=report), \
             patch.object(self.mod, "_refresh_connections_locked", return_value={
                 "status": "completed", "topics": ["demo"], "related_count": 1, "outputs": [str(path)],
             }):
            result = self.mod.refresh_connections(self.slug)
        self.assertEqual(result["status"], "failed")
        self.assertEqual(result["related_count"], 1)
        self.assertEqual(result["outputs"], [str(path)])
        self.assertTrue(result["partial"]["connections_published"])
        self.assertTrue(result["partial"]["retry_safe"])
        self.assertEqual(result["partial"]["retry_command"], report["retry_command"])
        self.assertEqual(json.loads(path.read_text(encoding="utf-8")), stored)

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
            # run; no retrieved candidates means no explanations are generated.
            with patch.object(self.mod, "plan_connections",
                              return_value={"classify_topics": [], "classification_plan": []}), \
                 patch.object(self.mod, "_context", return_value=(self.index[0], self.index, ["demo"])), \
                 patch.object(self.mod, "_embedding_for_target", return_value=(self.index, [[0, 1], [1, 0]])), \
                 patch.object(topic_modeling, "compute_related_candidates", return_value={self.slug: []}), \
                 patch.object(self.mod, "_load_raw_connections", return_value={}), \
                 patch("lib.connections.save_global_connections"), \
                 patch("lib.atomic_io.atomic_write_json"):
                with self.assertRaises(RuntimeError):
                    self.mod._refresh_connections_locked(self.slug)
        self.explain_pair.assert_not_called()

    def test_cli_reports_failed_schema(self):
        with patch.object(self.mod, "plan_connections", side_effect=ValueError("bad")):
            with patch.object(sys, "argv", ["refresh_paper_connections.py", "--slug", self.slug]), \
                 patch("builtins.print") as printed:
                self.assertEqual(self.mod.main(), 1)
        result = json.loads(printed.call_args.args[0])
        self.assertEqual(result["status"], "failed")
        self.assertEqual(result["schema_version"], 1)

    def test_refresh_writes_grounded_explanations_for_selected_neighbours(self):
        saved = []
        with patch.object(self.mod, "_embedding_for_target", return_value=(self.index[:2], [[0, 1], [1, 0]])), \
             patch.object(topic_modeling, "compute_related_candidates",
                          return_value={self.slug: [(self.other, .8123)]}), \
             patch.object(self.mod, "_load_raw_connections", return_value={}), \
             patch("lib.connections.save_global_connections", side_effect=lambda store: saved.append(store)) as save, \
             patch("lib.atomic_io.atomic_write_json"), \
             patch("review_to_html._run_review_to_html", return_value={"converted": 2, "skipped": 0}):
            result = self.mod._refresh_connections_locked(self.slug)
        self.assertEqual(result["status"], "completed")
        save.assert_called_once()
        (link,) = saved[0][self.slug]
        explanation = self._explain_pair(self.index[0], self.index[1])
        self.explain_pair.assert_called_once_with(self.index[0], self.index[1])
        self.assertEqual((link["slug"], link["basis"], link["relation"], link["model"]),
                         (self.other, "embedding", "alternative", explanation["model"]))
        self.assertEqual(link["reason"], explanation["reason"])
        self.assertIn("보정된 불확실도", link["reason"])
        self.assertIn("앙상블 예측의 불일치", link["reason"])
        self.assertEqual(link["evidence"], {**explanation["evidence"], "cosine": .8123})
        self.assertEqual(link["reverse"]["reason"], explanation["reverse"]["reason"])
        self.assertNotEqual(link["reverse"]["reason"], link["reason"])
        self.assertEqual(link["reverse"]["evidence"],
                         {**explanation["reverse"]["evidence"], "cosine": .8123})

    def test_explanation_failure_never_publishes_partial_results_or_rewrites_views(self):
        old = "11484_Old"
        self.index.append({"slug": old, "title": "Old", "topics": ["demo"]})
        (self.papers / "_papers_index.json").write_text(json.dumps(self.index))
        directory = self.papers / old
        directory.mkdir()
        (directory / "review.md").write_text("# old review")
        (directory / "index.html").write_text("previous rendered connections")
        previous = {self.slug: [{"slug": old, "relation": "alternative", "reason": "old explanation"}]}
        (self.papers / "_global_connections.json").write_text(json.dumps(previous))
        (self.docs / "demo" / "_paper_connections.json").write_text(json.dumps(previous))
        before = self._snapshot()
        self.explain_pair.side_effect = [self._explain_pair(self.index[0], self.index[1]),
                                        RuntimeError("explanation provider unavailable")]
        with patch.dict(os.environ, {"RELATED_LINKS": "2"}), \
             patch.object(self.mod, "_embedding_for_target", return_value=(self.index, [[0, 1], [1, 0], [1, 1]])), \
             patch.object(topic_modeling, "compute_related_candidates",
                          return_value={self.slug: [(self.other, .9), (old, .8)]}), \
             patch("lib.connections.save_global_connections") as save, \
             patch("lib.atomic_io.atomic_write_json") as write_view, \
             patch("review_to_html._run_review_to_html") as render:
            with self.assertRaisesRegex(RuntimeError, "explanation provider unavailable"):
                self.mod._refresh_connections_locked(self.slug)
        self.assertEqual(self.explain_pair.call_count, 2)
        for operation in (save, write_view, render):
            operation.assert_not_called()
        self.assertEqual(self._snapshot(), before)

    def test_refresh_replaces_all_target_source_topics_without_touching_unrelated_raw_links(self):
        old = self._add_paper("11484_Old", "Old", "retired", "기대 개선량")
        keep = self._add_paper("11485_Keep", "Keep", "untouched", "정보 이득")
        neighbor = self._add_paper("11486_KeepNeighbor", "Keep neighbor", "untouched", "분산 감소")
        previous = {
            self.slug: [self._legacy_edge(old["slug"], .8, "retired"),
                        self._legacy_edge(self.other, .6, "demo"),
                        {"slug": old["slug"], "basis": "model", "source_topic": "obsolete"}],
            keep["slug"]: [self._legacy_edge(neighbor["slug"], .71, "untouched"),
                           {"slug": old["slug"], "basis": "metadata", "custom": "retain raw"}],
            "99999_OffIndex": [{"slug": self.other, "basis": "model", "custom": [1, 2]}],
            "99998_ProcessedEmpty": [],
        }
        path = self._connection_fixture(previous, ("demo", "retired", "untouched", "_cross"))
        untouched = (self.docs / "untouched" / "_paper_connections.json").read_bytes()
        with patch.object(self.mod, "_embedding_for_target", return_value=(self.index[:2], [[0, 1], [1, 0]])), \
             patch.object(topic_modeling, "compute_related_candidates",
                          return_value={self.slug: [(self.other, .91)]}), \
             patch("lib.connections.save_global_connections",
                   wraps=connection_store.save_global_connections) as save, \
             patch("review_to_html._run_review_to_html",
                   side_effect=lambda *, slugs, with_connected: {"converted": len(slugs), "skipped": 0}) as render:
            result = self.mod._refresh_connections_locked(self.slug)
        stored = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(set(stored), set(previous) | {old["slug"]})
        self.assertEqual(stored[old["slug"]], [])
        self.assertEqual([entry["slug"] for entry in stored[self.slug]], [self.other])
        self.assertEqual(stored[self.slug][0]["source_topic"], "demo")
        self.assertEqual(stored[self.slug][0]["reason"], self._explain_pair(self.index[0], self.index[1])["reason"])
        for source in set(previous) - {self.slug}:
            self.assertEqual(stored[source], previous[source])
        save.assert_called_once()
        self.explain_pair.assert_called_once_with(self.index[0], self.index[1])
        self.assertEqual(set(render.call_args.kwargs["slugs"]), {self.slug, self.other, old["slug"]})
        self.assertEqual(result["related_count"], 1)
        self.assertEqual((self.docs / "untouched" / "_paper_connections.json").read_bytes(), untouched)
        self.assertEqual(json.loads((self.docs / "retired" / "_paper_connections.json").read_text()),
                         {old["slug"]: []})
        view = json.loads((self.docs / "_cross" / "_paper_connections.json").read_text())
        self.assertEqual(view[old["slug"]], [])
        self.assertEqual([entry["slug"] for entry in view[keep["slug"]]], [neighbor["slug"]])

    def test_empty_selection_clears_target_outgoing_across_topics_without_explaining_unrelated_edges(self):
        previous = {self.slug: [self._legacy_edge(self.other, .8, "retired"),
                                self._legacy_edge(self.other, .7, "demo")],
                    "99999_Keep": [self._legacy_edge(self.other, .6, "unrelated")]}
        path = self._connection_fixture(previous, ("demo",))
        with patch.object(self.mod, "_embedding_for_target", return_value=(self.index[:2], [[0, 1], [1, 0]])), \
             patch.object(topic_modeling, "compute_related_candidates", return_value={self.slug: []}), \
             patch("review_to_html._run_review_to_html",
                   side_effect=lambda *, slugs, with_connected: {"converted": len(slugs), "skipped": 0}):
            result = self.mod._refresh_connections_locked(self.slug)
        stored = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(stored[self.slug], [])
        self.assertEqual(stored["99999_Keep"], previous["99999_Keep"])
        self.assertEqual(json.loads((self.docs / "demo" / "_paper_connections.json").read_text()),
                         {self.slug: [], self.other: []})
        self.assertEqual(result["related_count"], 0)
        self.explain_pair.assert_not_called()

    def test_refresh_explains_reverse_only_incoming_and_preserves_cosines_topics_and_other_edges(self):
        incoming = self._add_paper("11484_Incoming", "Incoming", "incoming", "정보 이득")
        unrelated = self._add_paper("11485_Unrelated", "Unrelated", "incoming", "분산 감소")
        first = self._legacy_edge(self.slug, .87654321, "incoming")
        first["reasons"] = [{"relation": "alternative", "reason": "obsolete view-level cosine reason"}]
        other_edge = self._legacy_edge(unrelated["slug"], .73, "incoming")
        second = self._legacy_edge(self.slug, .61234567, "older-topic")
        retired = {"slug": self.slug, "basis": "metadata", "source_topic": "retired", "custom": "keep"}
        previous = {self.slug: [], incoming["slug"]: [first, other_edge, second, retired],
                    unrelated["slug"]: [], "99999_Elsewhere": [{"slug": unrelated["slug"], "basis": "model"}]}
        path = self._connection_fixture(previous, ("demo", "incoming", "_cross"))
        with patch.object(self.mod, "_embedding_for_target", return_value=(self.index[:2], [[0, 1], [1, 0]])), \
             patch.object(topic_modeling, "compute_related_candidates", return_value={self.slug: []}), \
             patch("lib.connections.save_global_connections",
                   wraps=connection_store.save_global_connections) as save, \
             patch("review_to_html._run_review_to_html",
                   side_effect=lambda *, slugs, with_connected: {"converted": len(slugs), "skipped": 0}) as render:
            result = self.mod._refresh_connections_locked(self.slug)
        stored = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(stored[self.slug], [])
        self.assertEqual(stored[incoming["slug"]][1], other_edge)
        self.assertEqual(stored[incoming["slug"]][3], retired)
        self.assertEqual(stored[unrelated["slug"]], [])
        self.assertEqual(stored["99999_Elsewhere"], previous["99999_Elsewhere"])
        expected = self._explain_pair(incoming, self.index[0])
        for position, original in ((0, first), (2, second)):
            edge = stored[incoming["slug"]][position]
            self.assertEqual(edge["reason"], expected["reason"])
            self.assertEqual(edge["model"], expected["model"])
            self.assertEqual(edge["source_topic"], original["source_topic"])
            self.assertEqual(edge["evidence"], {**expected["evidence"], "cosine": original["evidence"]["cosine"]})
            self.assertEqual(edge["reverse"]["evidence"],
                             {**expected["reverse"]["evidence"], "cosine": original["evidence"]["cosine"]})
            self.assertNotIn("reasons", edge)
        save.assert_called_once()
        self.assertEqual(self.explain_pair.call_count, 2)
        for call in self.explain_pair.call_args_list:
            self.assertEqual(call.args, (incoming, self.index[0]))
        view = json.loads((self.docs / "demo" / "_paper_connections.json").read_text())
        (edge,) = view[self.slug]
        self.assertEqual(edge["slug"], incoming["slug"])
        self.assertEqual(edge["reason"], expected["reverse"]["reason"])
        self.assertEqual(edge["model"], expected["model"])
        self.assertNotEqual(edge["reason"], expected["reason"])
        self.assertEqual(set(render.call_args.kwargs["slugs"]), {self.slug, incoming["slug"]})
        self.assertEqual(result["related_count"], 0)
        self.assertEqual(result["candidate_count"], 0)

    def test_incoming_explanation_failure_preserves_raw_store_and_all_published_outputs(self):
        incoming = self._add_paper("11484_Incoming", "Incoming", "incoming", "정보 이득")
        unrelated = self._add_paper("11485_Unrelated", "Unrelated", "incoming", "분산 감소")
        previous = {self.slug: [self._legacy_edge(self.other, .4, "older-topic")],
                    incoming["slug"]: [self._legacy_edge(self.slug, .8, "incoming"),
                                       self._legacy_edge(unrelated["slug"], .7, "incoming")]}
        self._connection_fixture(previous, ("demo", "incoming", "_cross"))
        before = self._snapshot()
        self.explain_pair.side_effect = [self._explain_pair(self.index[0], self.index[1]),
                                        RuntimeError("incoming provider failed")]
        with patch.object(self.mod, "_embedding_for_target", return_value=(self.index[:2], [[0, 1], [1, 0]])), \
             patch.object(topic_modeling, "compute_related_candidates",
                          return_value={self.slug: [(self.other, .9)]}), \
             patch("lib.connections.save_global_connections") as save, \
             patch("lib.atomic_io.atomic_write_json") as write_view, \
             patch("review_to_html._run_review_to_html") as render:
            with self.assertRaisesRegex(RuntimeError, "incoming provider failed"):
                self.mod._refresh_connections_locked(self.slug)
        self.assertEqual(self.explain_pair.call_count, 2)
        for operation in (save, write_view, render):
            operation.assert_not_called()
        self.assertEqual(self._snapshot(), before)

    def test_incoming_without_valid_retrieval_cosine_fails_without_a_fallback(self):
        incoming = self._add_paper("11484_Incoming", "Incoming", "incoming", "정보 이득")
        for evidence in ({}, None, {"cosine": None}, {"cosine": True}, {"cosine": "0.8"},
                         {"cosine": float("nan")}, {"cosine": float("inf")}, {"cosine": 1.01}):
            with self.subTest(evidence=evidence):
                edge = self._legacy_edge(self.slug, .8, "incoming")
                edge["evidence"] = evidence
                path = self.papers / "_global_connections.json"
                path.write_text(json.dumps({incoming["slug"]: [edge]}), encoding="utf-8")
                before = self._snapshot()
                with patch.object(self.mod, "_embedding_for_target", return_value=(self.index[:2], [[0, 1], [1, 0]])), \
                     patch.object(topic_modeling, "compute_related_candidates", return_value={self.slug: []}), \
                     patch("lib.connections.save_global_connections") as save, \
                     patch("lib.atomic_io.atomic_write_json") as write_view, \
                     patch("review_to_html._run_review_to_html") as render:
                    with self.assertRaisesRegex(ValueError, "incoming connection requires valid cosine evidence"):
                        self.mod._refresh_connections_locked(self.slug)
                for operation in (save, write_view, render, self.explain_pair):
                    operation.assert_not_called()
                self.assertEqual(self._snapshot(), before)

    def test_unregistered_incoming_source_fails_before_any_store_or_view_write(self):
        previous = {"99999_Unregistered": [self._legacy_edge(self.slug, .8, "unknown-topic")]}
        path = self.papers / "_global_connections.json"
        path.write_text(json.dumps(previous), encoding="utf-8")
        before = self._snapshot()
        with patch.object(self.mod, "_embedding_for_target", return_value=(self.index[:2], [[0, 1], [1, 0]])), \
             patch.object(topic_modeling, "compute_related_candidates", return_value={self.slug: []}), \
             patch("lib.connections.save_global_connections") as save, \
             patch("lib.atomic_io.atomic_write_json") as write_view, \
             patch("review_to_html._run_review_to_html") as render:
            with self.assertRaisesRegex(ValueError, "unregistered incoming connection source"):
                self.mod._refresh_connections_locked(self.slug)
        for operation in (save, write_view, render, self.explain_pair):
            operation.assert_not_called()
        self.assertEqual(self._snapshot(), before)

    def test_atomic_raw_replace_failure_leaves_previous_store_and_views_unchanged(self):
        previous = {self.slug: [self._legacy_edge(self.other, .8, "older-topic")]}
        path = self._connection_fixture(previous, ("demo",))
        before = {path: path.read_bytes(),
                  self.docs / "demo" / "_paper_connections.json":
                  (self.docs / "demo" / "_paper_connections.json").read_bytes()}
        with patch.object(self.mod, "_embedding_for_target", return_value=(self.index[:2], [[0, 1], [1, 0]])), \
             patch.object(topic_modeling, "compute_related_candidates",
                          return_value={self.slug: [(self.other, .9)]}), \
             patch("lib.atomic_io.os.replace", side_effect=OSError("atomic replace failed")) as replace, \
             patch("review_to_html._run_review_to_html") as render:
            with self.assertRaisesRegex(OSError, "atomic replace failed"):
                self.mod._refresh_connections_locked(self.slug)
        self.assertEqual(Path(replace.call_args.args[1]), path)
        replace.assert_called_once()
        render.assert_not_called()
        self.assertEqual({file: file.read_bytes() for file in before}, before)

    def test_raw_snapshot_rejects_malformed_and_outside_symlink_without_losing_data(self):
        path = self.papers / "_global_connections.json"
        for invalid in ([], {self.slug: [42]}, {self.slug: [{"slug": None}]}):
            with self.subTest(invalid=invalid):
                content = json.dumps(invalid)
                path.write_text(content, encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "invalid raw global connections"):
                    self.mod._load_raw_connections()
                self.assertEqual(path.read_text(encoding="utf-8"), content)
        outside = self.docs / "outside.json"
        outside.write_text("{}", encoding="utf-8")
        path.unlink()
        path.symlink_to(outside)
        with self.assertRaisesRegex(ValueError, "unsafe global connections path"):
            self.mod._load_raw_connections()
        self.assertEqual(outside.read_text(encoding="utf-8"), "{}")

    def _bundle(self, topic):
        (self.docs / topic).mkdir(exist_ok=True)
        (self.docs / topic / "_hdbscan_model.joblib").write_bytes(b"bundle")

    def _two_topics(self):
        """`demo` has a model bundle; `nobundle` does not."""
        self.index[0]["topics"] = ["demo", "nobundle"]
        self.index[1]["topics"] = ["demo", "nobundle"]
        (self.papers / "_papers_index.json").write_text(json.dumps(self.index))
        (self.docs / "nobundle").mkdir()
        (self.docs / "nobundle" / "_embeddings_cache.json").write_text(json.dumps({
            "embed_model": "test", "slugs": [self.other], "embeddings": [[1.0, 0.0]],
            "originality_sha256": {},
        }))
        self._bundle("demo")

    def _snapshot(self):
        return {str(p): p.read_bytes() for p in self.docs.rglob("*") if p.is_file()}

    def test_plan_reports_classification_plan_and_writes_nothing(self):
        self._two_topics()
        before = self._snapshot()
        with patch.dict(sys.modules, {"classify_papers": None, "joblib": None}):
            result = self.mod.plan_connections(self.slug)
        self.assertEqual(result["classification_plan"], [
            {"topic": "demo", "model_bundle": True, "classified": False},
            {"topic": "nobundle", "model_bundle": False, "classified": False}])
        self.assertEqual(result["classify_topics"], ["demo"])
        self.assertEqual(result["steps"], ["classify_papers", "refresh_paper_connections"])
        self.assertEqual(self._snapshot(), before)

    def test_plan_without_any_bundle_skips_classification_step(self):
        result = self.mod.plan_connections(self.slug)
        self.assertEqual(result["classify_topics"], [])
        self.assertEqual(result["steps"], ["refresh_paper_connections"])
        self.assertFalse(result["classification_plan"][0]["model_bundle"])

    def _run_locked(self, fake_classify):
        fake = type(sys)("classify_papers")
        fake._run_classify = fake_classify
        with patch.dict(sys.modules, {"classify_papers": fake}), \
             patch.object(self.mod, "_embedding_for_target", return_value=(self.index[:2], [[0, 1], [1, 0]])), \
             patch.object(topic_modeling, "compute_related_candidates",
                          return_value={self.slug: [(self.other, .9)]}), \
             patch.object(self.mod, "_load_raw_connections", return_value={}), \
             patch("lib.connections.save_global_connections") as save, \
             patch("lib.atomic_io.atomic_write_json"), \
             patch("review_to_html._run_review_to_html", return_value={"converted": 2, "skipped": 0}):
            return self.mod._refresh_connections_locked(self.slug), save

    def test_execute_classifies_only_bundle_topics_before_connections(self):
        self._two_topics()
        calls = []

        def fake_classify(topic, *, slugs=None, dry_run=False):
            calls.append((topic, slugs, dry_run))
            index = json.loads((self.papers / "_papers_index.json").read_text())
            index[0]["classifications"] = {topic: {
                "primary_category": "Cat A", "all_categories": ["Cat A"],
                "sub_category": "", "sub_categories": []}}
            (self.papers / "_papers_index.json").write_text(json.dumps(index))

        result, save = self._run_locked(fake_classify)
        self.assertEqual(calls, [("demo", [self.slug], False)])
        self.assertEqual(result["classified_topics"], ["demo"])
        self.assertEqual(result["unclassified_topics"], ["nobundle"])
        self.assertEqual(result["status"], "completed")
        self.assertIn(str(self.docs / "demo" / "_new_classification.json"), result["outputs"])
        self.assertIn(str(self.docs / "demo" / "_umap_coords.json"), result["outputs"])
        self.assertEqual(len(calls), 1)
        save.assert_called_once()

    def test_execute_fails_closed_when_classification_is_missing(self):
        self._two_topics()
        with self.assertRaisesRegex(RuntimeError, "classification did not complete for topic: demo"):
            self._run_locked(lambda topic, *, slugs=None, dry_run=False: None)
        self.assertFalse((self.docs / "_global_connections.json").exists())
        self.assertFalse((self.papers / "_global_connections.json").exists())
        self.assertEqual(list(self.docs.rglob("_paper_connections.json")), [])


if __name__ == "__main__":
    unittest.main()
