"""The public capability table must match the executable registry."""
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE))
import render_feature_docs
import run_feature


class FeatureDocumentationTests(unittest.TestCase):
    def test_generated_table_matches_current_registry(self):
        registry = json.loads((PIPELINE / "features.json").read_text())["features"]
        guide = (PIPELINE.parent / "docs/setup-guide.md").read_text()
        self.assertEqual(guide, render_feature_docs.replace_table(guide, render_feature_docs.render_table(registry)))

    def test_metadata_changes_require_doc_regeneration(self):
        registry = json.loads((PIPELINE / "features.json").read_text())["features"]
        original = render_feature_docs.render_table(registry)
        registry[0]["label_en"] = "Changed capability label"
        self.assertNotEqual(original, render_feature_docs.render_table(registry))

    def test_missing_table_marker_fails_instead_of_appending_duplicate(self):
        with self.assertRaises(ValueError):
            render_feature_docs.replace_table("No generated region", "table")

    def test_list_does_not_resolve_credentials_or_run_modules(self):
        import io
        from contextlib import redirect_stdout
        output = io.StringIO()
        with patch.object(run_feature, "_credential", side_effect=AssertionError("credential access")), patch.object(run_feature, "_execute", side_effect=AssertionError("execution")), redirect_stdout(output):
            self.assertEqual(run_feature.main(["--list"]), 0)
        self.assertEqual(len(json.loads(output.getvalue())["features"]), len(run_feature._registry()))


if __name__ == "__main__":
    unittest.main()
