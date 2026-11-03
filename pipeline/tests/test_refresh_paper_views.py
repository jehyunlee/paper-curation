"""Temp-corpus contracts for cache-based publication refresh (no provider calls)."""
from __future__ import annotations

import contextlib
import io
import json
import shlex
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

PIPELINE_DIR = Path(__file__).resolve().parents[1]
if str(PIPELINE_DIR) not in sys.path:
    sys.path.insert(0, str(PIPELINE_DIR))

import refresh_paper_views as views


class RefreshPaperViewsTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.papers = self.root / "docs" / "papers"
        self.papers.mkdir(parents=True)
        self.slug = "042_Contract_Paper"
        directory = self.papers / self.slug
        directory.mkdir()
        (directory / "review.md").write_text("# Reviewed paper", encoding="utf-8")
        (directory / "index.html").write_text("review HTML", encoding="utf-8")
        self.entries = [{"slug": self.slug, "topics": ["demo"],
                         "classifications": {"stale": {"primary_category": "old"}}}]
        self._write_index()
        self._topic("demo")
        for target, kwargs in (
            ("PAPERS_DIR", {"new": self.papers}),
            ("load_config", {"return_value": {"zotero": {"collections": {"demo": [], "other": []}}}}),
            ("_sync_review_metadata", {}),
            ("_run_builder", {"side_effect": self._build}),
        ):
            patcher = patch.object(views, target, **kwargs)
            mocked = patcher.start()
            self.addCleanup(patcher.stop)
            if target == "_run_builder":
                self.builder = mocked
            elif target == "_sync_review_metadata":
                self.sync = mocked
        network = patch("socket.socket.connect", side_effect=AssertionError("network forbidden"))
        self.network = network.start()
        self.addCleanup(network.stop)

    def _write_index(self):
        (self.papers / "_papers_index.json").write_text(json.dumps(self.entries), encoding="utf-8")

    def _topic(self, topic, *, mode="bm25", model=None, options=None, network=False):
        directory = self.papers.parent / topic
        directory.mkdir(exist_ok=True)
        index = {"retrieval_mode": mode, "model": model,
                 "source_options": options if options is not None else {
                     "include_text": False, "include_personal_notes": False}}
        (directory / "_search_index.json").write_text(json.dumps(index), encoding="utf-8")
        (directory / "index.html").write_text("topic HTML", encoding="utf-8")
        if mode == "hybrid":
            (directory / "_search_index_emb.bin").write_bytes(b"cached-vectors")
        if network:
            (directory / "network.html").write_text("existing network", encoding="utf-8")
        return directory

    def _build(self, command, *, timeout):
        script = Path(command[1]).name
        if script == "build_search_index.py":
            topic = command[command.index("--topic") + 1]
            directory = self.papers.parent / topic
            mode = command[command.index("--mode") + 1]
            index = directory / "_search_index.json"
            if not index.exists():
                model = command[command.index("--model") + 1] if "--model" in command else None
                index.write_text(json.dumps({"retrieval_mode": mode, "model": model}), encoding="utf-8")
            if mode == "hybrid":
                (directory / "_search_index_emb.bin").write_bytes(b"cached-vectors")
        elif script == "build_topic_index.py":
            (self.papers.parent / command[-1] / "index.html").write_text("new topic HTML", encoding="utf-8")
        elif script == "generate_network.py":
            topic = command[command.index("--topic") + 1]
            (self.papers.parent / topic / "network.html").write_text("new network", encoding="utf-8")
        elif script == "build_cross_index.py":
            directory = self.papers.parent / "_cross"
            for name in ("index.html", "_search_index.json", "_paper_connections.json", "_cross_meta.json"):
                path = directory / name
                if not path.exists():
                    path.write_text("{}", encoding="utf-8")
        return {"status": "completed", "returncode": 0}

    def _refresh(self, **kwargs):
        return views.refresh_paper_views(self.slug, papers_dir=self.papers, **kwargs)

    def _steps(self, report, builder):
        return [step for step in report["steps"] if step["builder"] == builder]

    def test_paper_scope_uses_membership_not_stale_classification_or_unrelated_directories(self):
        self.entries[0].update(topics=["demo", "demo"], primary_topic="primary")
        self._write_index()
        self._topic("primary")
        unrelated = self._topic("other", network=True)
        before = {path.name: path.read_bytes() for path in unrelated.iterdir()}
        report = self._refresh()
        self.assertEqual(report["status"], "completed", report)
        self.assertEqual(report["topics"], ["demo", "primary"])
        self.assertEqual({step["topic"] for step in self._steps(report, "search")}, {"demo", "primary"})
        self.assertFalse((self.papers.parent / "stale").exists())
        self.assertFalse((self.papers.parent / "_cross").exists())
        self.assertEqual({path.name: path.read_bytes() for path in unrelated.iterdir()}, before)
        self.sync.assert_called_once_with(self.papers.resolve(), self.slug)
        review, = self._steps(report, "review")
        self.assertEqual(review["command"][-1], self.slug)
        self.assertIn("_run_review_to_html", review["command"][2])
        self.assertNotIn("run_update_force", review["command"][2])
        self.network.assert_not_called()

    def test_reregistration_refreshes_old_and_new_membership_union_once(self):
        self._topic("old")
        report = self._refresh(previous_topics=["old", "demo", "old"])
        self.assertEqual(report["status"], "completed", report)
        self.assertEqual(report["topics"], ["demo", "old"])
        self.assertEqual([step["topic"] for step in self._steps(report, "search")], ["demo", "old"])
        retry = shlex.split(report["retry_command"])
        self.assertEqual(retry.count("--previous-topic"), 2)
        self.assertIn("old", retry)

    def test_search_preserves_hybrid_bm25_legacy_model_and_source_options(self):
        cases = [
            ({"retrieval_mode": "hybrid", "model": "existing-embedding-model",
              "source_options": {"include_text": True, "include_personal_notes": False}},
             ("hybrid", "existing-embedding-model", "yes", "no")),
            ({"retrieval_mode": "bm25", "model": None,
              "source_options": {"include_text": False, "include_personal_notes": True}},
             ("bm25", None, "no", "yes")),
            ({"model": "legacy-embedding-model", "include_text": "no", "include_personal_notes": "yes"},
             ("hybrid", "legacy-embedding-model", "no", "yes")),
        ]
        path = self.papers.parent / "demo" / "_search_index.json"
        for index, expected in cases:
            with self.subTest(index=index):
                path.write_text(json.dumps(index), encoding="utf-8")
                report = self._refresh()
                self.assertEqual(report["status"], "completed", report)
                step, = self._steps(report, "search")
                settings = step["settings"]
                self.assertEqual(tuple(settings[name] for name in (
                    "mode", "model", "include_text", "include_personal_notes")), expected)
                command = step["command"]
                for option, value in (("--mode", expected[0]), ("--include-text", expected[2]),
                                      ("--include-personal-notes", expected[3])):
                    self.assertEqual(command[command.index(option) + 1], value)
                if expected[1]:
                    self.assertEqual(command[command.index("--model") + 1], expected[1])
                else:
                    self.assertNotIn("--model", command)

    def test_networks_are_refreshed_only_when_already_present(self):
        self.entries[0]["topics"] = ["demo", "other"]
        self._write_index()
        self._topic("demo", network=True)
        other = self._topic("other")
        report = self._refresh()
        self.assertEqual(report["status"], "completed", report)
        self.assertEqual([step["topic"] for step in self._steps(report, "network")], ["demo"])
        self.assertFalse((other / "network.html").exists())
        builders = {Path(call.args[0][1]).name for call in self.builder.call_args_list}
        self.assertEqual(builders, {"-c", "build_search_index.py", "build_topic_index.py", "generate_network.py"})
        self.assertEqual([step["builder"] for step in report["steps"][:2]], ["metadata", "review"])
        order = [step["builder"] for step in report["steps"] if step["topic"] == "demo"]
        self.assertLess(order.index("search"), order.index("topic"))

    def test_missing_topic_views_are_built_without_creating_a_network(self):
        self.entries[0]["topics"] = ["fresh"]
        self._write_index()
        directory = self.papers.parent / "fresh"
        self.assertFalse(directory.exists())
        report = self._refresh()
        self.assertEqual(report["status"], "completed", report)
        self.assertTrue((directory / "index.html").is_file())
        self.assertTrue((directory / "_search_index.json").is_file())
        self.assertTrue((directory / "_search_index_emb.bin").is_file())
        self.assertFalse((directory / "network.html").exists())
        self.assertFalse(self._steps(report, "network"))

    def test_all_topic_catchup_is_explicit_and_uses_configured_and_registered_topics(self):
        self.entries.append({"slug": "043_Other", "topics": ["registered-only"]})
        self._write_index()
        self._topic("registered-only")
        self._topic("other")
        orphan = self._topic("orphan", network=True)
        before = (orphan / "index.html").read_bytes()
        report = views.refresh_paper_views(papers_dir=self.papers, all_topics=True)
        self.assertEqual(report["status"], "completed", report)
        self.assertEqual(report["topics"], ["demo", "other", "registered-only"])
        self.assertFalse(self._steps(report, "review"))
        self.sync.assert_not_called()
        self.assertEqual((orphan / "index.html").read_bytes(), before)
        self.assertIn("--all-topics", shlex.split(report["retry_command"]))

    def test_existing_cross_view_refreshes_only_for_affected_recorded_sources(self):
        cross = self._topic("_cross", network=True)
        meta = cross / "_cross_meta.json"
        for sources, expected in ((["other"], False), (["demo", "other"], True)):
            with self.subTest(sources=sources):
                meta.write_text(json.dumps({"topics": [{"slug": topic} for topic in sources],
                                            "title": "Saved aggregate title"}), encoding="utf-8")
                report = self._refresh()
                self.assertEqual(report["status"], "completed", report)
                steps = self._steps(report, "cross")
                self.assertEqual(bool(steps), expected)
                if expected:
                    self.assertEqual(steps[0]["settings"]["topics"], sources)
                    self.assertIn("Saved aggregate title", steps[0]["command"])
                    self.assertIn("_cross", [step["topic"] for step in self._steps(report, "network")])

    def test_dry_run_has_no_writes_locks_credentials_or_network(self):
        self.entries[0]["topics"] = ["missing-topic"]
        self._write_index()
        before = sorted(str(path.relative_to(self.root)) for path in self.root.rglob("*"))
        contents = {str(path.relative_to(self.root)): path.read_bytes()
                    for path in self.root.rglob("*") if path.is_file()}
        with patch("lib.corpus_store.corpus_operation_lock", side_effect=AssertionError("no plan lock")) as lock, \
             patch("lib.credentials.resolve_credential", side_effect=AssertionError("no plan credentials")) as credential:
            report = self._refresh(dry_run=True)
        self.assertEqual(report["status"], "planned", report)
        self.assertEqual(sorted(str(path.relative_to(self.root)) for path in self.root.rglob("*")), before)
        self.assertEqual({str(path.relative_to(self.root)): path.read_bytes()
                          for path in self.root.rglob("*") if path.is_file()}, contents)
        self.assertTrue(all(step["status"] == "planned" for step in report["steps"]))
        self.assertFalse(report["embedding_cost"]["covered_by_review_budget"])
        self.builder.assert_not_called()
        self.sync.assert_not_called()
        lock.assert_not_called()
        credential.assert_not_called()
        self.network.assert_not_called()

    def test_reserved_new_review_defers_and_standalone_output_is_untouched(self):
        marker = self.papers / self.slug / ".corpus-reservation.json"
        marker.write_text('{"token":"reserved"}', encoding="utf-8")
        report = self._refresh()
        self.assertEqual(report["status"], "deferred")
        standalone = self.root / "standalone"
        report = views.refresh_paper_views(self.slug, papers_dir=standalone)
        self.assertEqual(report["status"], "skipped")
        self.assertFalse(standalone.exists())
        self.builder.assert_not_called()
        self.sync.assert_not_called()
        self.assertTrue(marker.exists())

    def test_unregistered_review_is_not_published_into_topics(self):
        self.entries = []
        self._write_index()
        report = self._refresh()
        self.assertEqual(report["status"], "skipped")
        self.assertEqual(report["steps"], [])
        self.builder.assert_not_called()

    def test_failed_builder_exposes_partial_outputs_and_other_builders_still_run(self):
        self._topic("demo", network=True)
        review = self.papers / self.slug / "review.md"
        before = review.read_bytes()
        def fail_search(command, *, timeout):
            if Path(command[1]).name == "build_search_index.py":
                return {"status": "failed", "error": "embedding service unavailable", "returncode": 2}
            return self._build(command, timeout=timeout)
        self.builder.side_effect = fail_search
        report = self._refresh()
        self.assertEqual(report["status"], "failed")
        self.assertTrue(any("embedding service unavailable" in error for error in report["errors"]))
        self.assertEqual([step["status"] for step in self._steps(report, "search")], ["failed"])
        self.assertEqual([step["status"] for step in self._steps(report, "topic")], ["completed"])
        self.assertEqual([step["status"] for step in self._steps(report, "network")], ["completed"])
        self.assertEqual(review.read_bytes(), before)
        self.assertIn(self.slug, shlex.split(report["retry_command"]))

    def test_missing_builder_output_is_failure_not_false_completion(self):
        directory = self.papers.parent / "demo"
        (directory / "index.html").unlink()
        self.builder.side_effect = None
        self.builder.return_value = {"status": "completed", "returncode": 0}
        report = self._refresh()
        self.assertEqual(report["status"], "failed")
        self.assertTrue(any("required output" in error for error in report["errors"]))

    def test_unknown_search_policy_fails_without_overwriting_index(self):
        path = self.papers.parent / "demo" / "_search_index.json"
        policies = [
            {"retrieval_mode": "unsupported"},
            {"retrieval_mode": "hybrid", "model": None},
            {"retrieval_mode": "bm25", "model": "not-sparse"},
            {"retrieval_mode": "bm25", "model": None, "source_options": {"unknown": True}},
        ]
        for policy in policies:
            with self.subTest(policy=policy):
                path.write_text(json.dumps(policy), encoding="utf-8")
                before = path.read_bytes()
                self.builder.reset_mock()
                report = self._refresh()
                self.assertEqual(report["status"], "failed")
                self.assertEqual(path.read_bytes(), before)
                self.assertFalse(any(Path(call.args[0][1]).name == "build_search_index.py"
                                     for call in self.builder.call_args_list))

    def test_capped_review_cannot_start_unpriced_hybrid_embedding_build(self):
        self._topic("demo", mode="hybrid", model="saved-model")
        report = self._refresh(allow_paid=False)
        self.assertEqual(report["status"], "failed")
        self.assertTrue(any("budget" in error for error in report["errors"]))
        self.assertFalse(any(Path(call.args[0][1]).name == "build_search_index.py"
                             for call in self.builder.call_args_list))
        self._topic("demo", mode="bm25")
        report = self._refresh(allow_paid=False)
        self.assertEqual(report["status"], "completed", report)

    def test_view_execution_holds_exclusive_operation_lock(self):
        from lib.corpus_store import CorpusStoreBusyError, corpus_operation_lock
        def assert_exclusive(command, *, timeout):
            with self.assertRaises(CorpusStoreBusyError):
                with corpus_operation_lock(self.papers, timeout=0):
                    pass
            return self._build(command, timeout=timeout)
        self.builder.side_effect = assert_exclusive
        self.assertEqual(self._refresh()["status"], "completed")

    def test_unsafe_topic_or_symlinked_output_is_rejected_without_touching_target(self):
        self.entries[0]["topics"] = ["../escape"]
        self._write_index()
        self.assertEqual(self._refresh()["status"], "failed")
        self.builder.assert_not_called()
        self.entries[0]["topics"] = ["demo"]
        self._write_index()
        target = self.root / "external.html"
        target.write_bytes(b"external content")
        output = self.papers.parent / "demo" / "index.html"
        output.unlink()
        output.symlink_to(target)
        report = self._refresh()
        self.assertEqual(report["status"], "failed")
        self.assertEqual(target.read_bytes(), b"external content")

    def test_cli_reports_json_failure_and_passes_explicit_catchup_scope(self):
        stdout = io.StringIO()
        failure = {"status": "failed", "topics": ["demo"], "steps": [], "errors": ["failed"]}
        with patch.object(views, "refresh_paper_views", return_value=failure) as refresh, \
             contextlib.redirect_stdout(stdout):
            code = views.main(["--all-topics", "--papers-dir", str(self.papers), "--dry-run", "--timeout", "30"])
        self.assertEqual(code, 1)
        self.assertEqual(json.loads(stdout.getvalue()), failure)
        refresh.assert_called_once_with(None, papers_dir=str(self.papers), previous_topics=[],
                                        all_topics=True, dry_run=True, timeout=30.0)


class ReviewMetadataSyncTests(unittest.TestCase):
    def test_review_metadata_updates_without_replacing_corpus_owned_fields(self):
        with tempfile.TemporaryDirectory() as temporary:
            papers = Path(temporary)
            original = {"slug": "042_Contract", "topics": ["demo"], "score": 1,
                        "connections": [{"slug": "043_Neighbor"}],
                        "classifications": {"demo": {"primary_category": "Existing"}}, "tags": ["keep"]}
            path = papers / "_papers_index.json"
            path.write_text(json.dumps([original]), encoding="utf-8")
            metadata = {"essence": "Fresh review essence", "score": 4,
                        "has_figures": True, "text_md_sha256": "new-hash"}
            with patch("build_papers_index.parse_review", return_value=metadata) as parse:
                views._sync_review_metadata(papers, original["slug"])
            parse.assert_called_once_with(original["slug"])
            updated, = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(updated, {**original, **metadata})


if __name__ == "__main__":
    unittest.main()
