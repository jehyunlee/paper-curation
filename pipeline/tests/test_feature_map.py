"""The feature map must show every registry feature and stay self-contained."""
import json
import sys
import unittest
from pathlib import Path

PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE))

import build_feature_map as fm  # noqa: E402


def _walk(node):
    yield node
    for child in node.get("children", []):
        yield from _walk(child)


class FeatureMapTests(unittest.TestCase):
    def setUp(self):
        self.features = json.loads(fm.REGISTRY.read_text(encoding="utf-8"))["features"]
        self.tree = fm.build_tree(self.features)

    def test_every_registry_feature_appears_once(self):
        ids = [n["meta"]["기능 ID"] for n in _walk(self.tree) if n.get("kind") == "feature"]
        self.assertEqual(sorted(ids), sorted(f["id"] for f in self.features))

    def test_every_feature_has_a_description(self):
        for node in _walk(self.tree):
            self.assertTrue(node["desc"], node["label"])

    def test_output_has_no_external_assets(self):
        html = fm.TEMPLATE.replace("__TREE__", json.dumps(self.tree, ensure_ascii=False))
        self.assertNotIn("http://", html)
        self.assertNotIn("https://", html)


if __name__ == "__main__":
    unittest.main()
