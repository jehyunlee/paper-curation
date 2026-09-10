import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

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


if __name__ == "__main__":
    unittest.main()
