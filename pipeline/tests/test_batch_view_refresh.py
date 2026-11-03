"""Batch view refresh policy, without invoking the pipeline or its builders."""
import argparse
import ast
import inspect
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import run_update_force as runner


class BatchNetworkRefreshTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.topic_dir = Path(self.tmp.name) / "demo"
        self.topic_dir.mkdir()
        main = ast.parse(inspect.getsource(runner.main))
        self.branches = {}
        for node in ast.walk(main):
            if not isinstance(node, ast.If) or not node.body:
                continue
            first = node.body[0]
            if not isinstance(first, ast.Expr) or not isinstance(first.value, ast.Call):
                continue
            call = first.value
            if (isinstance(call.func, ast.Name) and call.func.id == "run_step"
                    and call.args and isinstance(call.args[0], ast.Constant)
                    and call.args[0].value in {"generate_network", "generate_network (rebuild)"}):
                self.branches[call.args[0].value] = compile(
                    ast.Module(body=[node], type_ignores=[]), runner.__file__, "exec")

    def _run_branches(self, *, insights, expected):
        self.assertEqual(set(self.branches), {"generate_network", "generate_network (rebuild)"})
        for name, branch in self.branches.items():
            with self.subTest(step=name, insights=insights, expected=expected):
                run_step = Mock()
                exec(branch, {
                    "args": argparse.Namespace(insights=insights),
                    "get_topic_dir": lambda topic: self.topic_dir,
                    "topic": "demo", "run_step": run_step, "log": Mock(),
                })
                if expected:
                    run_step.assert_called_once_with(
                        name, ["python", "pipeline/generate_network.py", "--topic", "demo"], 600)
                else:
                    run_step.assert_not_called()

    def test_existing_network_refreshes_without_insights_in_both_places(self):
        (self.topic_dir / "network.html").write_text("old network", encoding="utf-8")
        self._run_branches(insights=False, expected=True)

    def test_missing_network_is_not_created_without_insights(self):
        self._run_branches(insights=False, expected=False)

    def test_explicit_insights_can_create_network(self):
        self._run_branches(insights=True, expected=True)

    def test_network_directory_does_not_count_as_existing_visualization(self):
        (self.topic_dir / "network.html").mkdir()
        self._run_branches(insights=False, expected=False)


class BatchSearchCommandTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.topic_dir = Path(self.tmp.name)
        patcher = patch.object(runner, "get_topic_dir", return_value=self.topic_dir)
        patcher.start()
        self.addCleanup(patcher.stop)

    def _command(self, metadata):
        (self.topic_dir / "_search_index.json").write_text(
            json.dumps(metadata), encoding="utf-8")
        return runner._search_index_command("demo")

    def test_bm25_keeps_keyless_mode_and_explicit_sources(self):
        command = self._command({
            "retrieval_mode": "bm25", "model": None,
            "source_options": {"include_text": False, "include_personal_notes": True},
        })
        self.assertEqual(command, [
            "python", "pipeline/build_search_index.py", "--topic", "demo",
            "--mode", "bm25", "--include-text", "no",
            "--include-personal-notes", "yes",
        ])

    def test_hybrid_keeps_selected_model_and_explicit_sources(self):
        command = self._command({
            "retrieval_mode": "hybrid", "model": "selected-embedding-model",
            "source_options": {"include_text": True, "include_personal_notes": False},
        })
        self.assertEqual(command, [
            "python", "pipeline/build_search_index.py", "--topic", "demo",
            "--mode", "hybrid", "--include-text", "yes",
            "--include-personal-notes", "no", "--model", "selected-embedding-model",
        ])

    def test_legacy_hybrid_keeps_its_model_and_source_flags(self):
        command = self._command({
            "model": "legacy-embedding-model", "include_text": "no",
            "include_personal_notes": "yes",
        })
        self.assertEqual(command, [
            "python", "pipeline/build_search_index.py", "--topic", "demo",
            "--mode", "hybrid", "--include-text", "no",
            "--include-personal-notes", "yes", "--model", "legacy-embedding-model",
        ])

    def test_invalid_existing_mode_is_not_replaced_by_hybrid(self):
        with self.assertRaisesRegex(ValueError, "retrieval_mode"):
            self._command({"retrieval_mode": "unsupported"})

    def test_batch_search_step_uses_the_policy_preserving_command(self):
        main = ast.parse(inspect.getsource(runner.main))
        calls = [node for node in ast.walk(main)
                 if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                 and node.func.id == "run_step" and node.args
                 and isinstance(node.args[0], ast.Constant)
                 and node.args[0].value == "build_search_index"]
        self.assertEqual(len(calls), 1)
        command = ["python", "retained-policy-builder"]
        build_command = Mock(return_value=command)
        run_step = Mock()
        statement = ast.fix_missing_locations(
            ast.Module(body=[ast.Expr(value=calls[0])], type_ignores=[]))
        exec(compile(statement, runner.__file__, "exec"), {
            "run_step": run_step, "_search_index_command": build_command, "topic": "demo",
        })
        build_command.assert_called_once_with("demo")
        run_step.assert_called_once_with("build_search_index", command, 900)


class BatchCrossRefreshTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.papers = Path(self.tmp.name) / "papers"
        self.papers.mkdir()
        self.cross = self.papers.parent / "_cross"
        self.cross.mkdir()
        patcher = patch.object(runner, "PAPERS_DIR", str(self.papers))
        patcher.start()
        self.addCleanup(patcher.stop)

    def _existing_cross(self, *, mode="bm25", sources=("demo", "second"), network=False):
        (self.cross / "_search_index.json").write_text(json.dumps({
            "retrieval_mode": mode,
            "model": "selected-embedding-model" if mode == "hybrid" else None,
            "source_indexes": {source: {} for source in sources},
        }), encoding="utf-8")
        (self.cross / "_cross_meta.json").write_text(json.dumps({
            "title": "Kept title", "topics": [{"slug": "unselected"}],
        }), encoding="utf-8")
        (self.cross / "index.html").write_text("old page", encoding="utf-8")
        if network:
            (self.cross / "network.html").write_text("old network", encoding="utf-8")

    def _cross_command(self, mode):
        return [sys.executable, str(PIPELINE / "build_cross_index.py"),
                "--topics", "demo", "second", "--mode", mode, "--title", "Kept title"]

    def test_existing_bm25_cross_keeps_sources_and_title_and_refreshes_page_and_network(self):
        self._existing_cross(network=True)
        run_step = Mock()
        runner.run_cross_view_refresh(run_step, "demo")
        self.assertEqual(run_step.call_args_list, [
            unittest.mock.call("build_cross_index", self._cross_command("bm25"), 300),
            unittest.mock.call("generate_network (_cross)",
                               [sys.executable, str(PIPELINE / "generate_network.py"),
                                "--topic", "_cross"], 600),
        ])

    def test_missing_cross_network_is_not_created(self):
        self._existing_cross()
        run_step = Mock()
        runner.run_cross_view_refresh(run_step, "demo")
        run_step.assert_called_once_with("build_cross_index", self._cross_command("bm25"), 300)

    def test_unrelated_topic_does_not_expand_existing_cross_membership(self):
        self._existing_cross(sources=("second",), network=True)
        run_step = Mock()
        runner.run_cross_view_refresh(run_step, "demo")
        run_step.assert_not_called()

    def test_absent_cross_keeps_existing_batch_creation_path(self):
        run_step = Mock()
        runner.run_cross_view_refresh(run_step, "demo")
        run_step.assert_called_once_with(
            "build_cross_index", ["python", "pipeline/build_cross_index.py", "--no-page"], 300)

    def test_invalid_cross_mode_fails_before_running_any_builder(self):
        self._existing_cross(mode="unsupported")
        run_step = Mock()
        with self.assertRaisesRegex(ValueError, "retrieval_mode"):
            runner.run_cross_view_refresh(run_step, "demo")
        run_step.assert_not_called()

    def test_failed_merge_stops_before_network_without_retry_or_mode_change(self):
        self._existing_cross(mode="hybrid", network=True)
        run_step = Mock(side_effect=RuntimeError("hybrid cannot merge BM25 source"))
        with self.assertRaisesRegex(RuntimeError, "BM25 source"):
            runner.run_cross_view_refresh(run_step, "demo")
        run_step.assert_called_once_with("build_cross_index", self._cross_command("hybrid"), 300)


if __name__ == "__main__":
    unittest.main()
