"""Whitelist/timeline consistency for categories that only appear in all_categories.

Regression for the smart-laboratory case: the bundle taxonomy had two
categories, every paper had the same primary, and the second category showed
up only in `all_categories`. `_new_classification.json` listed primaries only,
so validate_papers flagged 15 "unknown category" issues; after widening the
whitelist, the timeline check demanded an image for a category that has no
primary papers (generate_timelines renders primaries only).
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import classify_papers  # noqa: E402
import validate_papers  # noqa: E402


class BundleErrorTests(unittest.TestCase):
    def test_missing_bundle_raises_instead_of_exiting(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(classify_papers.BundleError):
                classify_papers.load_bundle(tmp)

    def test_embed_mode_mismatch_raises(self):
        import joblib
        with tempfile.TemporaryDirectory() as tmp:
            joblib.dump({"hdbscan_model": 1, "umap_cluster": 1, "centroids": {},
                         "tid_to_cat": {}, "tid_to_subname": {},
                         "embed_model": "not-the-current-mode"},
                        Path(tmp) / "_hdbscan_model.joblib")
            with self.assertRaisesRegex(classify_papers.BundleError, "embed_model"):
                classify_papers.load_bundle(tmp)


class TimelineMismatchTests(unittest.TestCase):
    def _run(self, tmp, cls, images):
        topic_dir = Path(tmp) / "t"
        topic_dir.mkdir()
        (topic_dir / "_new_classification.json").write_text(
            json.dumps(cls), encoding="utf-8")
        for name in images:
            (topic_dir / f"category_timeline_{name}.png").write_bytes(b"")
        with mock.patch.object(validate_papers, "get_topic_dir", return_value=topic_dir):
            return validate_papers.check_timeline_mismatch("t")

    def test_secondary_only_category_needs_no_timeline(self):
        cls = {"categories": [{"name": "A"}, {"name": "B"}],
               "assignments": [{"slug": "s", "primary_category": "A",
                                "all_categories": ["A", "B"], "sub_category": "a"}]}
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(self._run(tmp, cls, ["A"]), [])

    def test_primary_category_without_image_is_reported(self):
        cls = {"categories": [{"name": "A"}, {"name": "B"}],
               "assignments": [{"slug": "s", "primary_category": "A",
                                "all_categories": ["A"], "sub_category": "a"},
                               {"slug": "u", "primary_category": "B",
                                "all_categories": ["B"], "sub_category": "b"}]}
        with tempfile.TemporaryDirectory() as tmp:
            issues = self._run(tmp, cls, ["A"])
        self.assertEqual(len(issues), 1)
        self.assertIn("MISSING image for category slug: B", issues[0])


if __name__ == "__main__":
    unittest.main()
