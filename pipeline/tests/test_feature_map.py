"""The feature map must show every registry feature and pipeline step, link
duplicates both ways, and stay self-contained."""
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
        self.pmap = json.loads(fm.PIPELINE_MAP.read_text(encoding="utf-8"))
        self.tree = fm.build_tree(self.features, self.pmap)
        self.nodes = list(_walk(self.tree))
        self.by_key = {n["key"]: n for n in self.nodes if n.get("key")}

    def test_top_level_is_three_questions(self):
        self.assertEqual([c["label"] for c in self.tree["children"]],
                         ["어떻게 쓰나", "무엇을 할 수 있나", "전체 큐레이션은 어떻게 도나"])

    def test_every_registry_feature_appears_once(self):
        ids = [k.split(":", 1)[1] for k in self.by_key if k.startswith("feature:")]
        self.assertEqual(sorted(ids), sorted(f["id"] for f in self.features))

    def test_every_pipeline_step_appears(self):
        steps = [s["id"] for st in self.pmap["stages"] for s in st["steps"]] + [o["id"] for o in self.pmap["options"]]
        self.assertEqual(sorted(k.split(":", 1)[1] for k in self.by_key if k.startswith("step:")), sorted(steps))

    def test_same_function_links_resolve_and_are_mutual(self):
        for key, node in self.by_key.items():
            for link in node.get("same", []):
                self.assertIn(link["key"], self.by_key, key)
                back = [x["key"] for x in self.by_key[link["key"]].get("same", [])]
                self.assertIn(key, back, f"{key} -> {link['key']} not mutual")

    def test_features_carry_decision_tags_and_facts(self):
        for key, node in self.by_key.items():
            if key.startswith("feature:"):
                self.assertTrue(node.get("tags"), key)
                self.assertEqual([f[0] for f in node["facts"]], ["키", "비용", "외부 전송"])
        self.assertIn("확인 필수", [t["t"] for t in self.by_key["feature:publish"]["tags"]])

    def test_transmission_values_are_translated(self):
        for f in self.features:
            self.assertIn(f["credential"]["transmission"], fm.TRANSMISSION_KO, f["id"])

    def test_pipeline_stages_are_numbered(self):
        pipeline = self.tree["children"][2]
        self.assertTrue(pipeline["children"][0]["label"].startswith("①"))
        self.assertTrue(pipeline["children"][1]["children"][0]["label"].startswith("2-1 "))

    def test_every_node_has_a_description_and_no_internal_group_code(self):
        for node in self.nodes:
            self.assertTrue(node["desc"], node["label"])
            for row in node.get("tech", []) + node.get("facts", []):
                self.assertNotEqual(row[0], "그룹")

    def test_output_has_no_external_assets(self):
        html = fm.TEMPLATE.replace("__TREE__", json.dumps(self.tree, ensure_ascii=False))
        self.assertNotIn("http://", html)
        self.assertNotIn("https://", html)


if __name__ == "__main__":
    unittest.main()
