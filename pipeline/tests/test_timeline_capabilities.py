import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import generate_timelines as timelines


class TimelineCapabilityTests(unittest.TestCase):
    def test_template_only_requires_active_configuration(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            configs = root / "configs"
            configs.mkdir()
            (configs / "model_config.template.yaml").write_text(
                "defaults:\n  main_model_name: gemini-3\n"
                "  image_gen_model_name: gemini-image\n", encoding="utf-8")
            with patch.object(timelines, "get_paperbanana_dir", return_value=str(root)):
                result = timelines.diagnose_timeline_capabilities(images_only=True)
        self.assertEqual(result["status"], "needs-configuration")

    def test_active_config_reports_missing_selected_backend_credential(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            configs = root / "configs"
            configs.mkdir()
            (configs / "model_config.yaml").write_text(
                "defaults:\n  main_model_name: gemini-3\n"
                "  image_gen_model_name: gemini-image\n", encoding="utf-8")
            def credentials(provider):
                return {"reference": f"credential:{provider}", "configured": provider == "anthropic",
                        "source": "environment" if provider == "anthropic" else "none",
                        "status": "configured" if provider == "anthropic" else "not-configured"}
            with patch.object(timelines, "get_paperbanana_dir", return_value=str(root)), \
                 patch.object(timelines, "credential_status", side_effect=credentials):
                result = timelines.diagnose_timeline_capabilities(images_only=True)
        self.assertEqual(result["status"], "needs-credential")
        self.assertEqual(result["missing"], ["credential:google"])

    def test_active_config_reports_selected_models_when_credentials_available(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            configs = root / "configs"
            configs.mkdir()
            (configs / "model_config.yaml").write_text(
                "defaults:\n  main_model_name: gemini-3\n"
                "  image_gen_model_name: gemini-image\n", encoding="utf-8")
            def credentials(provider):
                return {"reference": f"credential:{provider}",
                        "configured": provider == "google",
                        "source": "environment" if provider == "google" else "none",
                        "status": "configured" if provider == "google" else "not-configured"}
            with patch.object(timelines, "get_paperbanana_dir", return_value=str(root)), \
                 patch.object(timelines, "credential_status", side_effect=credentials):
                result = timelines.diagnose_timeline_capabilities(images_only=True)
        self.assertFalse(result["available"])
        self.assertEqual(result["status"], "needs-credential")
        self.assertIn("credential:anthropic", result["missing"])
        self.assertEqual(result["models"]["main_model_name"], "gemini-3")

    def test_active_config_is_ready_when_google_and_judge_credentials_exist(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            configs = root / "configs"
            configs.mkdir()
            (configs / "model_config.yaml").write_text(
                "defaults:\n  main_model_name: gemini-3\n"
                "  image_gen_model_name: gemini-image\n", encoding="utf-8")
            def credentials(provider):
                return {"reference": f"credential:{provider}", "configured": True,
                        "source": "keyring", "status": "configured"}
            with patch.object(timelines, "get_paperbanana_dir", return_value=str(root)), \
                 patch.object(timelines, "credential_status", side_effect=credentials):
                result = timelines.diagnose_timeline_capabilities(images_only=True)
        self.assertTrue(result["available"])
        self.assertEqual(result["roles"]["candidate_judge"], timelines._JUDGE_MODEL)

    def test_mutually_exclusive_independent_modes_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "mutually exclusive"):
            timelines._run_timeline(narrative_only=True, images_only=True)

    def test_images_only_without_saved_narrative_returns_insufficient_data(self):
        with tempfile.TemporaryDirectory() as tmp:
            topic_dir = Path(tmp) / "topic"
            topic_dir.mkdir()
            with patch.object(timelines, "get_topic_dir", return_value=topic_dir), \
                 patch.object(timelines, "diagnose_timeline_capabilities",
                              return_value={"available": True, "status": "ready"}), \
                 patch.object(timelines, "generate_candidates") as images, \
                 patch.object(timelines, "build_main_narrative_from_summaries") as narrative:
                result = timelines._run_timeline(topic="test", images_only=True)

        self.assertEqual(result["status"], "insufficient-data")
        images.assert_not_called()
        narrative.assert_not_called()

    def test_narrative_only_never_calls_image_generation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            papers = root / "papers"
            papers.mkdir()
            (papers / "_papers_index.json").write_text(json.dumps([]), encoding="utf-8")
            topic_dir = root / "topic"
            topic_dir.mkdir()
            with patch.object(timelines, "PAPERS_DIR", str(papers)), \
                 patch.object(timelines, "get_topic_dir", return_value=topic_dir), \
                 patch.object(timelines, "generate_candidates") as images:
                timelines._run_timeline(topic="test", narrative_only=True,
                                        category_only=True)

        images.assert_not_called()

    def test_scoped_narrative_run_keeps_other_categories_and_skips_unneeded_synthesis(self):
        """One changed category must not erase the others' Opus cache or
        rebuild the executive summary from a subset."""
        def paper(slug, category, year):
            return {"slug": slug, "title": slug, "date": f"{year}-01-01", "topics": ["test"],
                    "essence": "e", "classifications": {"test": {"primary_category": category,
                                                                 "sub_category": "s"}}}
        index = [paper("1_a", "Alpha", 2024), paper("2_b", "Beta", 2023), paper("3_c", "Beta", 2025)]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            papers = root / "papers"
            papers.mkdir()
            (papers / "_papers_index.json").write_text(json.dumps(index), encoding="utf-8")
            topic_dir = root / "topic"
            topic_dir.mkdir()
            candidates_dir = root / "_img_timelines" / "test"
            candidates_dir.mkdir(parents=True)
            beta_hash = timelines.category_input_hash([p for p in index if p["classifications"]["test"]["primary_category"] == "Beta"])
            # Prior full run left both categories cached; Beta's inputs are unchanged.
            (topic_dir / "_category_narratives.json").write_text(json.dumps([
                {"category": "Alpha", "sub_themes": [], "_input_hash": "stale"},
                {"category": "Beta", "sub_themes": ["kept"], "_input_hash": beta_hash},
            ]), encoding="utf-8")
            for slug in ("alpha", "beta"):
                (candidates_dir / f"_method_text_{slug}.txt").write_text("m", encoding="utf-8")
            (candidates_dir / "_method_text_main.txt").write_text("main", encoding="utf-8")
            (topic_dir / "_timeline_narrative.json").write_text("{}", encoding="utf-8")
            narrative = MagicMock(return_value=("method", "caption", {"category": "Alpha", "sub_themes": ["new"]}))
            with patch.object(timelines, "PAPERS_DIR", str(papers)), \
                 patch.object(timelines, "__file__", str(root / "generate_timelines.py")), \
                 patch.object(timelines, "get_topic_dir", return_value=topic_dir), \
                 patch.object(timelines, "build_category_narrative", narrative), \
                 patch.object(timelines, "build_main_narrative_from_summaries", return_value=("main2", "cap")) as main_call, \
                 patch.object(timelines, "build_executive_summary", return_value="exec") as exec_call, \
                 patch.object(timelines, "generate_candidates") as images, \
                 patch.dict(os.environ, {"TIMELINE_NARRATIVE_PARALLEL": "1"}):
                timelines._run_timeline(topic="test", narrative_only=True, categories=["Alpha"])
            saved = {s["category"]: s for s in json.loads((topic_dir / "_category_narratives.json").read_text())}

        narrative.assert_called_once()
        self.assertEqual(saved["Beta"]["_input_hash"], beta_hash, "unchanged category cache must survive a scoped run")
        self.assertEqual(saved["Alpha"]["sub_themes"], ["new"])
        self.assertEqual(exec_call.call_args.args[0][0]["category"], "Alpha")
        self.assertEqual([s["category"] for s in exec_call.call_args.args[0]], ["Alpha", "Beta"],
                         "synthesis must cover the whole topic, not the changed subset")
        main_call.assert_called_once()
        images.assert_not_called()


if __name__ == "__main__":
    unittest.main()
