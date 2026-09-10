"""Capability-level regression tests: temporary corpus and mocked external I/O."""
import io
import hashlib
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE))
import run_feature as runner


class FeatureRunnerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.papers = self.root / "docs/papers"
        self.paper = self.papers / "001_Evidence"
        self.topic = self.root / "docs/demo"
        self.paper.mkdir(parents=True)
        self.topic.mkdir(parents=True)
        self.entries = [{"slug": self.paper.name, "title": "Evidence", "topics": ["demo"],
                         "classifications": {"demo": {"primary_category": "Evidence"}}}]
        (self.papers / "_papers_index.json").write_text(json.dumps(self.entries))
        (self.paper / "review.md").write_text("Existing review is preserved.")
        self.index = {"retrieval_mode": "bm25", "model": None, "quant": None, "dim": 0,
                      "source_fingerprint": hashlib.sha256(b"fixture").hexdigest(),
                      "source_file_count": 1, "built_at": 1,
                      "count": 1, "papers": {self.paper.name: {"title": "Evidence"}},
                      "chunks": [{"slug": self.paper.name, "section": "How", "text": "Measured evidence", "text_sha": hashlib.sha256(b"Measured evidence").hexdigest()}]}
        (self.topic / "_search_index.json").write_text(json.dumps(self.index))
        self.root_patch = patch.object(runner, "ROOT", self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)
        self.env_patch = patch.dict(os.environ, {}, clear=True)
        self.env_patch.start()
        self.addCleanup(self.env_patch.stop)

    def request(self, feature, **params):
        return {"schema_version": 1, "feature": feature, "params": params}

    def test_registry_has_real_labels_schemas_and_all_module_groups(self):
        features = runner._registry()
        self.assertEqual({f["group"] for f in features}, {f"M{i}" for i in range(9)})
        self.assertEqual(len(features), len({f["id"] for f in features}))
        self.assertTrue(all(f["label_ko"] and f["label_en"] and f["params_schema"] for f in features))
        by_id = {f["id"]: f for f in features}
        self.assertEqual(by_id["review"]["group"], "M1")
        self.assertEqual(by_id["extract"]["group"], "M0")
        self.assertNotEqual(by_id["timeline-text"]["credential"]["cost_class"], "local")

    def test_keyless_keyword_plan_does_not_lookup_credentials_or_execute(self):
        before = (self.topic / "_search_index.json").read_bytes()
        with patch.object(runner, "_credential", side_effect=AssertionError("key lookup")), patch.object(runner.subprocess, "run") as command:
            result = runner.run_request(self.request("keyword-search", topic="demo", query="evidence"))
        self.assertEqual(result["status"], "ready", result)
        command.assert_not_called()
        self.assertEqual(before, (self.topic / "_search_index.json").read_bytes())

    def test_semantic_sparse_mismatch_blocks_before_key_lookup(self):
        with patch.object(runner, "_credential", side_effect=AssertionError("key lookup")) as key:
            result = runner.run_request(self.request("semantic-search", topic="demo", query="evidence"))
        self.assertEqual(result["status"], "insufficient-data", result)
        key.assert_not_called()

    def test_no_match_query_returns_real_empty_result_without_llm(self):
        completed = SimpleNamespace(returncode=0, stdout=json.dumps({"results": [], "mode": "bm25"}))
        with patch.object(runner, "_child", return_value=completed) as child:
            result = runner.run_request(self.request("keyword-search", topic="demo", query="unmatched"), execute=True)
        self.assertEqual(result["status"], "completed", result)
        self.assertEqual(result["retrieval"]["results"], [])
        self.assertIn("--json", child.call_args.args[0])
        self.assertEqual(child.call_args.kwargs["credentials"], [])

    def test_search_build_is_explicit_and_mode_is_preserved(self):
        with patch.object(runner, "_child", return_value=SimpleNamespace(returncode=0)) as child:
            result = runner.run_request(self.request("keyword-search", topic="demo", operation="build"), execute=True)
        self.assertEqual(result["status"], "completed", result)
        args = child.call_args.args[0]
        self.assertEqual(args[args.index("--mode") + 1], "bm25")
        self.assertTrue(args[0].endswith("build_search_index.py"))

    def test_unknown_fields_boolean_version_and_traversal_fail_closed(self):
        good = self.request("keyword-search", topic="demo", query="evidence")
        bad = [good | {"schema_version": True}, good | {"api_key": "never-store"},
               self.request("keyword-search", topic="../private", query="x"),
               self.request("keyword-search", topic="demo", query="x", shell="bad"),
               self.request("keyword-search", topic="demo", query="x", top_k=True)]
        with patch.object(runner, "_child") as child:
            for request in bad:
                self.assertEqual(runner.run_request(request, execute=True)["status"], "failed")
        child.assert_not_called()

    def test_text_budget_is_delegated_before_provider_call(self):
        import text_task
        request = self.request("summary", sources=[{"id": "a", "title": "A", "text": "Evidence is limited."}])
        request.update(provider="anthropic", budget={"max_cost_usd": 0, "input_per_million_usd": 1,
                                                 "output_per_million_usd": 1, "max_output_tokens": 20})
        with patch.object(text_task, "generate_structured") as call, patch("lib.credentials.credential_status", return_value={"configured": False, "reference": "credential:anthropic"}):
            result = runner.run_request(request, execute=True)
        self.assertEqual(result["status"], "budget-exceeded", result)
        call.assert_not_called()

    def test_text_missing_key_is_not_reported_ready(self):
        request = self.request("summary", sources=[{"id": "a", "title": "A", "text": "Evidence is limited."}])
        request["provider"] = "openai"
        with patch("lib.credentials.credential_status", return_value={"configured": False, "reference": "credential:openai"}):
            self.assertEqual(runner.run_request(request)["status"], "needs-key")

    def test_nested_review_provider_conflict_fails_before_dispatch(self):
        request = self.request("review", request={"provider": "openai"})
        request["provider"] = "anthropic"
        self.assertEqual(runner.run_request(request)["status"], "failed")

    def test_unpriced_audio_budget_never_invents_a_bound(self):
        request = self.request("audio", slug=self.paper.name)
        request["budget"] = {"max_cost_usd": 10, "input_per_million_usd": 1, "output_per_million_usd": 1}
        with patch.object(runner, "_execute") as execute:
            result = runner.run_request(request, execute=True)
        self.assertEqual(result["status"], "budget-unavailable")
        execute.assert_not_called()

    def test_email_failure_preserves_mp3_and_does_not_generate_audio(self):
        path = self.root / "audio.mp3"
        path.write_bytes(b"MP3-original")
        request = self.request("email", file_path=str(path), recipient="to@example.test", sender="from@example.test")
        with patch.object(runner, "_credential", return_value="sentinel-secret"), patch.object(runner.urllib.request, "urlopen", side_effect=OSError("sentinel-secret")):
            result = runner.run_request(request, execute=True)
        self.assertEqual(result["status"], "failed")
        self.assertNotIn("sentinel-secret", json.dumps(result))
        self.assertEqual(path.read_bytes(), b"MP3-original")

    def test_invalid_email_address_stops_before_credential_lookup(self):
        path = self.root / "audio.mp3"
        path.write_bytes(b"MP3")
        with patch.object(runner, "_credential") as key:
            result = runner.run_request(self.request("email", file_path=str(path), recipient="bad\nrecipient", sender="from@example.test"))
        self.assertEqual(result["status"], "failed")
        key.assert_not_called()

    def test_publication_requires_explicit_confirmation_even_with_keys(self):
        with patch.object(runner, "_child") as child:
            result = runner.run_request(self.request("publish", topic="demo", confirm=False), execute=True)
        self.assertEqual(result["status"], "blocked")
        child.assert_not_called()

    def test_metrics_cli_uses_selected_slugs_not_nonexistent_topic_option(self):
        with patch.object(runner, "_child", return_value=SimpleNamespace(returncode=0)) as child:
            result = runner.run_request(self.request("metrics", topic="demo"), execute=True)
        self.assertEqual(result["status"], "completed", result)
        args = child.call_args.args[0]
        self.assertIn("--slugs", args)
        self.assertNotIn("--topic", args)
        self.assertIn(self.paper.name, args)

    def test_offline_bibliography_update_excludes_email_and_remote_zotero(self):
        with patch.object(runner, "_child", return_value=SimpleNamespace(returncode=0)) as child:
            result = runner.run_request(self.request("bibliography-update", topic="demo"), execute=True)
        self.assertEqual(result["status"], "completed", result)
        calls = [c.args[0] for c in child.call_args_list]
        self.assertIn("--offline", calls[0])
        self.assertIn("--skip-zotero", calls[0])
        self.assertTrue(all("--no-email" in call for call in calls))
        self.assertIn("--backfill-author-institutions", calls[1])
        self.assertIn("--finalize", calls[2])

    def test_extraction_never_uses_google_and_publishes_real_files(self):
        import run_update_force as engine
        pdf = self.root / "source.pdf"
        pdf.write_bytes(b"%PDF-1.4\nfixture")
        output = self.root / "extracted"
        def extract(_pdf, directory):
            (Path(directory) / "text.md").write_text("Extracted local evidence.")
            return True
        def figures(_pdf, directory, **kwargs):
            self.assertFalse(kwargs["validate_with_gemini"])
            (Path(directory) / "figures").mkdir()
            return []
        with patch.object(engine, "extract_text", side_effect=extract), patch.object(engine, "extract_figures", side_effect=figures), patch.object(runner, "_credential", side_effect=AssertionError("credentials")):
            result = runner.run_request(self.request("extract", pdf_path=str(pdf), output_dir=str(output)), execute=True)
        self.assertEqual(result["status"], "completed", result)
        self.assertEqual((output / "text.md").read_text(), "Extracted local evidence.")

    def test_existing_review_directory_cannot_be_used_as_extraction_output(self):
        pdf = self.root / "source.pdf"
        pdf.write_bytes(b"%PDF-1.4\nfixture")
        before = (self.paper / "review.md").read_bytes()
        result = runner.run_request(self.request("extract", pdf_path=str(pdf), output_dir=str(self.paper)), execute=True)
        self.assertEqual(result["status"], "failed")
        self.assertEqual((self.paper / "review.md").read_bytes(), before)

    def test_cli_reads_request_file_and_uses_nonzero_blocked_exit(self):
        path = self.root / "request.json"
        path.write_text(json.dumps(self.request("publish", topic="demo", confirm=False)))
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code = runner.main(["--request", str(path), "--execute"])
        self.assertEqual(code, 2)
        self.assertEqual(json.loads(stdout.getvalue())["status"], "blocked")

    def test_api_and_cli_share_the_same_readonly_plan(self):
        import api
        request = self.request("keyword-search", topic="demo", query="evidence")
        self.assertEqual(api.feature(request), runner.run_request(request))


if __name__ == "__main__":
    unittest.main()
