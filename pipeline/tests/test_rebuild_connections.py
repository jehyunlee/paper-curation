"""Rebuild safety regressions; all writes stay in temporary corpus fixtures."""
from __future__ import annotations

import contextlib
import json
import os
import subprocess
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import rebuild_connections as rebuild
import sync_paper_connections as sync
from lib import atomic_io, connections
from lib.corpus_store import CorpusStoreBusyError, corpus_operation_lock


def edge(slug):
    return {"slug": slug, "relation": "alternative", "reason": "old edge",
            "basis": "embedding", "evidence": {"cosine": .8}}


class RebuildConnectionsTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.docs = self.root / "docs"
        self.papers = self.docs / "papers"
        self.papers.mkdir(parents=True)
        self.index_path = self.papers / "_papers_index.json"
        self.global_path = self.papers / "_global_connections.json"
        self.a, self.b, self.old = "001_Alpha", "002_Beta", "003_Old"
        self.index = [{"slug": self.a, "topics": ["demo"]},
                      {"slug": self.b, "topics": ["demo"]}]
        self.write_index(self.index)
        self.write_json(self.global_path, {})
        for slug in (self.a, self.b):
            self.make_paper(slug)

        stack = contextlib.ExitStack()
        self.addCleanup(stack.close)
        stack.enter_context(patch.multiple(
            rebuild, ROOT=str(self.root), DOCS=str(self.docs), PAPERS=str(self.papers),
            INDEX=str(self.index_path)))
        stack.enter_context(patch.multiple(
            connections, PAPERS_DIR=str(self.papers), GLOBAL_CONN_PATH=str(self.global_path)))
        self.importer = stack.enter_context(patch.object(sync, "import_connections",
                                                        return_value={"imported": 0}))
        self.db = self.root / "cache" / "bibliography.sqlite3"
        stack.enter_context(patch.object(sync, "DEFAULT_DB", self.db))

    def write_json(self, path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")

    def write_index(self, index):
        self.write_json(self.index_path, index)

    def make_paper(self, slug, review="# Review\n\nBody stays unchanged.\n"):
        directory = self.papers / slug
        directory.mkdir(exist_ok=True)
        (directory / "review.md").write_text(review, encoding="utf-8")
        return directory

    def topic_json(self, topic, value):
        self.write_json(self.docs / topic / "_paper_connections.json", value)

    def snapshot(self):
        return {str(p.relative_to(self.root)): (
            p.stat().st_mtime_ns, p.stat().st_mode,
            p.read_bytes() if p.is_file() else None)
            for p in [self.root, *self.root.rglob("*")]}

    def model(self):
        model = types.ModuleType("topic_modeling")
        model.extract_originalities = Mock(side_effect=lambda pool: {p["slug"]: "text" for p in pool})
        model.compute_embeddings = Mock(side_effect=lambda texts, cache: (
            [[1.0, 0.0] for _ in texts], list(texts)))
        model.compute_related_candidates = Mock(side_effect=lambda vectors, slugs, **kw: {
            s: [(t, .8) for t in slugs if t != s] for s in slugs})
        return model

    def test_plan_and_both_dry_runs_never_write_lock_extract_or_embed(self):
        self.index[0]["primary_topic"] = "new-topic"
        self.write_index(self.index)
        self.topic_json("demo", {self.a: [edge(self.b)]})
        model = self.model()
        before = self.snapshot()
        with patch.dict(sys.modules, {"topic_modeling": model}), \
             patch.object(rebuild, "corpus_operation_lock") as lock, \
             patch.object(rebuild, "atomic_write_json") as write_json, \
             patch.object(rebuild, "atomic_write_text") as write_text, \
             patch.object(rebuild, "save_global_connections") as save, \
             patch.object(subprocess, "run") as network, patch("builtins.print"):
            self.assertIn("new-topic", rebuild.plan_rebuild(recompute=True)["topics"])
            rebuild.run_rebuild(dry_run=True)
            rebuild.run_rebuild(recompute=True, dry_run=True)
        self.assertEqual(self.snapshot(), before)
        for operation in (lock, write_json, write_text, save, network,
                          model.extract_originalities, model.compute_embeddings,
                          model.compute_related_candidates, self.importer):
            operation.assert_not_called()
        self.assertFalse((self.docs / "new-topic").exists())
        self.assertFalse(self.db.exists())

    def test_recompute_covers_all_memberships_missing_dirs_and_empty_sources(self):
        self.index = [
            {"slug": self.a, "topics": ["listed"], "primary_topic": "primary",
             "classifications": {"classified": {}}},
            {"slug": self.b, "topics": ["listed"], "primary_topic": "primary",
             "classifications": {"classified": {}}},
            {"slug": self.old, "topics": ["singleton"]},
            {"slug": "004_Unassigned"},
        ]
        self.write_index(self.index)
        self.make_paper(self.old)
        self.make_paper("004_Unassigned")
        self.topic_json("retired", {self.a: [edge(self.b)]})
        self.topic_json("_cross", {self.a: [edge(self.old)]})
        model = self.model()
        with patch.dict(sys.modules, {"topic_modeling": model}), patch("builtins.print"):
            result = rebuild.run_rebuild(recompute=True, no_render=True,
                                         no_inject=True, no_networks=True)
        self.assertEqual(set(result["topics"]),
                         {"listed", "primary", "classified", "singleton", "retired", "_cross"})
        self.assertEqual(model.compute_embeddings.call_count, 3)
        for call in model.extract_originalities.call_args_list:
            self.assertEqual({p["slug"] for p in call.args[0]}, {self.a, self.b})
        stored = json.loads(self.global_path.read_text())
        self.assertEqual(set(stored), {p["slug"] for p in self.index})
        self.assertEqual(stored[self.old], [])
        self.assertEqual(stored["004_Unassigned"], [])
        for topic in ("listed", "primary", "classified"):
            view = json.loads((self.docs / topic / "_paper_connections.json").read_text())
            self.assertEqual(view[self.a][0]["slug"], self.b)
            self.assertEqual(view[self.b][0]["slug"], self.a)
        self.assertEqual(json.loads((self.docs / "singleton" / "_paper_connections.json").read_text()),
                         {self.old: []})
        self.assertEqual(json.loads((self.docs / "retired" / "_paper_connections.json").read_text()), {})
        cross = json.loads((self.docs / "_cross" / "_paper_connections.json").read_text())
        self.assertEqual(cross[self.a][0]["slug"], self.b)
        self.assertEqual(cross[self.old], [])

    def test_singleton_clears_old_and_new_sources_from_html_and_markdown(self):
        self.write_index([{"slug": self.a, "primary_topic": "solo"}])
        content = "---\ntitle: Test\n---\n# Review\n\nBody.\n\n## Related Papers\n\nold edge\n\n## End\nKeep.\n"
        for slug in (self.a, self.old):
            self.make_paper(slug, content)
            (self.papers / slug / "index.html").write_text("old edge")
        old_view = {self.a: [edge(self.old)], self.old: [edge(self.a)]}
        self.topic_json("solo", old_view)
        self.topic_json("_cross", old_view)
        self.write_json(self.global_path, {self.a: [dict(edge(self.old), source_topic="solo")]})
        renderer = types.ModuleType("review_to_html")
        renderer._connections_cache = old_view

        def render(*, slugs, with_connected):
            self.assertFalse(with_connected)
            self.assertEqual(set(slugs), {self.a, self.old})
            for slug in slugs:
                self.assertEqual(renderer._connections_cache[slug], [])
                (self.papers / slug / "index.html").write_text("no connections")
            return {"converted": len(slugs), "skipped": 0}

        renderer._run_review_to_html = Mock(side_effect=render)
        # Exercise the real markdown section replacement, without any provider.
        injector = types.ModuleType("inject_frontmatter")
        injector.build_related_section = Mock(return_value="")
        with patch.dict(sys.modules, {"review_to_html": renderer, "inject_frontmatter": injector,
                                      "topic_modeling": self.model()}), patch("builtins.print"):
            result = rebuild.run_rebuild(recompute=True, no_networks=True)
        self.assertEqual(result["source_keys"], {self.a, self.old})
        self.assertEqual(json.loads(self.global_path.read_text()), {self.a: []})
        for slug in (self.a, self.old):
            self.assertEqual((self.papers / slug / "review.md").read_text(),
                             content.replace("\n## Related Papers\n\nold edge\n", ""))
            self.assertNotIn("old edge", (self.papers / slug / "index.html").read_text())
        self.assertEqual(json.loads((self.docs / "_cross" / "_paper_connections.json").read_text()),
                         {self.a: []})
        self.assertEqual(injector.build_related_section.call_count, 2)

    def test_empty_corpus_clears_existing_views_instead_of_retaining_graph(self):
        self.write_index([])
        self.topic_json("demo", {self.a: [edge(self.b)]})
        self.topic_json("_cross", {self.a: [edge(self.b)]})
        with patch("builtins.print"):
            rebuild.run_rebuild(recompute=True, no_render=True, no_inject=True, no_networks=True)
        for path in (self.global_path, self.docs / "demo" / "_paper_connections.json",
                     self.docs / "_cross" / "_paper_connections.json"):
            self.assertEqual(json.loads(path.read_text()), {})

    def test_exclusive_lease_covers_snapshot_calculation_publication_and_db(self):
        held, events = [], []

        @contextlib.contextmanager
        def lease(papers, *, exclusive):
            self.assertEqual(Path(papers), self.papers)
            self.assertTrue(exclusive)
            held.append(True)
            try:
                yield
            finally:
                held.pop()
                events.append("released")

        def checked(name, operation):
            def call(*args, **kwargs):
                self.assertTrue(held, name)
                events.append(name)
                return operation(*args, **kwargs)
            return call

        model = self.model()
        model.extract_originalities.side_effect = checked("extract", model.extract_originalities.side_effect)
        with patch.dict(sys.modules, {"topic_modeling": model}), \
             patch.object(rebuild, "corpus_operation_lock", side_effect=lease), \
             patch.object(rebuild, "load_index", side_effect=checked("index", rebuild.load_index)), \
             patch.object(rebuild, "load_global_connections",
                          side_effect=checked("global", rebuild.load_global_connections)), \
             patch.object(rebuild, "save_global_connections",
                          side_effect=checked("save", rebuild.save_global_connections)), \
             patch.object(rebuild, "render_pages", side_effect=checked("render", lambda *a, **k: None)), \
             patch.object(rebuild, "inject_related", side_effect=checked("inject", lambda *a, **k: None)), \
             patch.object(rebuild, "regen_networks", side_effect=checked("network", lambda *a, **k: None)), \
             patch.object(rebuild, "sync_existing_database", side_effect=checked("db", lambda: None)), \
             patch("builtins.print"):
            rebuild.run_rebuild(recompute=True)
        self.assertEqual(events, ["index", "global", "extract", "save", "render", "inject",
                                  "network", "db", "released"])

    def test_live_review_lease_and_pending_reservation_block_before_snapshot(self):
        with corpus_operation_lock(self.papers), patch.object(rebuild, "load_index") as read:
            with self.assertRaises(CorpusStoreBusyError):
                rebuild.run_rebuild()
            read.assert_not_called()
        (self.papers / self.a / ".corpus-reservation.json").write_text("{}")
        with patch.object(rebuild, "load_index") as read:
            with self.assertRaises(CorpusStoreBusyError):
                rebuild.run_rebuild()
            read.assert_not_called()

    def test_invalid_topic_slug_and_symlink_paths_fail_before_publication(self):
        for bad in ("../escape", "demo/../../escape", "papers", "_cross"):
            with self.subTest(topic=bad):
                self.write_index([{"slug": self.a, "topics": [bad]}])
                with patch.object(rebuild, "save_global_connections") as save, \
                     patch.object(rebuild, "atomic_write_json") as write:
                    with self.assertRaises(ValueError):
                        rebuild.run_rebuild(recompute=True)
                    save.assert_not_called()
                    write.assert_not_called()
        self.write_index([{"slug": "../escape", "topics": ["demo"]}])
        with self.assertRaises(ValueError):
            rebuild.plan_rebuild()
        self.write_index(self.index)
        outside = self.root / "outside"
        outside.mkdir()
        (self.docs / "demo").symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ValueError):
            rebuild.plan_rebuild()
        (self.docs / "demo").unlink()
        review = self.papers / self.a / "review.md"
        review.unlink()
        review.symlink_to(outside / "review.md")
        with self.assertRaises(ValueError):
            rebuild.plan_rebuild()

    def test_global_save_replaces_atomically_and_failure_preserves_old_store(self):
        old = self.global_path.read_bytes()
        new = {self.a: [edge(self.b)]}
        replace = os.replace

        def observe(source, destination):
            self.assertEqual(Path(destination), self.global_path)
            self.assertEqual(self.global_path.read_bytes(), old)
            self.assertEqual(json.loads(Path(source).read_text()), new)
            replace(source, destination)

        with patch.object(atomic_io.os, "replace", side_effect=observe) as replaced:
            connections.save_global_connections(new)
        replaced.assert_called_once()
        self.assertEqual(json.loads(self.global_path.read_text()), new)
        before = self.global_path.read_bytes()
        with patch.object(atomic_io.os, "replace", side_effect=OSError("replace failed")):
            with self.assertRaises(OSError):
                connections.save_global_connections({self.a: []})
        self.assertEqual(self.global_path.read_bytes(), before)

    def test_embedding_error_or_shortfall_does_not_publish_or_report_done(self):
        for outcome in (OSError("encoder unavailable"), ([[1, 0]], [self.a])):
            with self.subTest(outcome=outcome):
                model = self.model()
                model.compute_embeddings.side_effect = outcome if isinstance(outcome, Exception) else None
                model.compute_embeddings.return_value = outcome
                before = self.global_path.read_bytes()
                with patch.dict(sys.modules, {"topic_modeling": model}), \
                     patch("builtins.print") as printed:
                    with self.assertRaises((OSError, RuntimeError)):
                        rebuild.run_rebuild(recompute=True, no_render=True, no_inject=True, no_networks=True)
                self.assertEqual(self.global_path.read_bytes(), before)
                self.assertFalse(any(str(c.args[0]).startswith("DONE") for c in printed.call_args_list))
        self.importer.assert_not_called()

    def test_render_shortfall_or_crash_propagates_and_stops_downstream(self):
        for outcome in ({"converted": 1, "skipped": 1}, RuntimeError("renderer failed")):
            with self.subTest(outcome=outcome):
                renderer = types.ModuleType("review_to_html")
                renderer._run_review_to_html = Mock(return_value=outcome)
                if isinstance(outcome, Exception):
                    renderer._run_review_to_html.side_effect = outcome
                with patch.dict(sys.modules, {"review_to_html": renderer}), \
                     patch.object(rebuild, "inject_related") as inject, \
                     patch.object(rebuild, "regen_networks") as network, \
                     patch.object(rebuild, "sync_existing_database") as database, \
                     patch("builtins.print") as printed:
                    with self.assertRaises(RuntimeError):
                        rebuild.run_rebuild()
                for operation in (inject, network, database):
                    operation.assert_not_called()
                self.assertFalse(any(str(c.args[0]).startswith("DONE") for c in printed.call_args_list))

    def test_empty_render_set_never_selects_all_papers(self):
        renderer = types.ModuleType("review_to_html")
        renderer._run_review_to_html = Mock()
        with patch.dict(sys.modules, {"review_to_html": renderer}):
            rebuild.render_pages(set(), connections={})
        renderer._run_review_to_html.assert_not_called()

    def test_network_failure_propagates_without_done_or_database_sync(self):
        failed = subprocess.CompletedProcess(["network"], 9, stdout="partial", stderr="failed build")
        with patch.object(subprocess, "run", return_value=failed), \
             patch.object(rebuild, "sync_existing_database") as database, \
             patch("builtins.print") as printed:
            with self.assertRaisesRegex(RuntimeError, "network demo failed.*failed build"):
                rebuild.run_rebuild(no_render=True, no_inject=True)
        database.assert_not_called()
        self.assertFalse(any(str(c.args[0]).startswith("DONE") for c in printed.call_args_list))

    def test_optional_database_only_syncs_existing_db_after_valid_full_views(self):
        with patch("builtins.print"):
            rebuild.run_rebuild(no_render=True, no_inject=True, no_networks=True)
        self.importer.assert_not_called()
        self.assertFalse(self.db.exists())
        self.db.parent.mkdir()
        self.db.write_bytes(b"fixture; importer is mocked")

        def imported(db):
            self.assertEqual(db, self.db)
            self.assertEqual(json.loads((self.docs / "demo" / "_paper_connections.json").read_text()),
                             {self.a: [], self.b: []})
            return {"imported": 0}

        self.importer.side_effect = imported
        with patch("builtins.print"):
            rebuild.run_rebuild(no_render=True, no_inject=True, no_networks=True)
        self.importer.assert_called_once_with(self.db)
        self.importer.reset_mock()
        with patch("builtins.print"):
            rebuild.run_rebuild(["demo"], no_render=True, no_inject=True, no_networks=True)
        self.importer.assert_not_called()
        self.importer.side_effect = RuntimeError("invalid DB snapshot")
        with patch("builtins.print") as printed:
            with self.assertRaisesRegex(RuntimeError, "invalid DB snapshot"):
                rebuild.run_rebuild(no_render=True, no_inject=True, no_networks=True)
        self.assertFalse(any(str(c.args[0]).startswith("DONE") for c in printed.call_args_list))


if __name__ == "__main__":
    unittest.main()
