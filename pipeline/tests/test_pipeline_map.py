"""pipeline_map.json must stay true to the code it describes."""
import json
import re
import unittest
from pathlib import Path

PIPELINE = Path(__file__).resolve().parents[1]
MAP = json.loads((PIPELINE / "pipeline_map.json").read_text(encoding="utf-8"))
FEATURES = {f["id"] for f in json.loads((PIPELINE / "features.json").read_text(encoding="utf-8"))["features"]}
RUN_UPDATE = (PIPELINE / "run_update_force.py").read_text(encoding="utf-8")
RUN_STEPS = set(re.findall(r'run_step\(\s*"([^"(]+?)(?: \([^)]*\))?"', RUN_UPDATE))
COSTS = {"local", "paid", "external"}


def all_steps():
    for stage in MAP["stages"]:
        yield from stage["steps"]
    yield from MAP["options"]


class PipelineMapTests(unittest.TestCase):
    def test_every_script_exists(self):
        for step in all_steps():
            self.assertTrue((PIPELINE / f"{step['script']}.py").is_file(), step["id"])

    def test_run_step_names_are_real(self):
        for step in all_steps():
            for name in step.get("run_steps", []):
                self.assertIn(name, RUN_STEPS, f"{step['id']}: {name}")

    def test_feature_links_point_at_registry(self):
        for step in all_steps():
            for fid in step.get("features", []):
                self.assertIn(fid, FEATURES, step["id"])

    def test_ids_unique_and_fields_present(self):
        ids = [s["id"] for s in all_steps()] + [st["id"] for st in MAP["stages"]]
        self.assertEqual(len(ids), len(set(ids)))
        for step in all_steps():
            self.assertTrue(step["label"] and step["desc"], step["id"])
            self.assertIn(step["cost"], COSTS, step["id"])

    def test_core_curation_steps_are_mapped(self):
        """A core run_update_force step that no map entry claims is a map gap."""
        claimed = {name for step in all_steps() for name in step.get("run_steps", [])}
        ignored = {"evaluate_retrieval", "refresh_retrieval_eval_snapshot", "generate_moc", "build_rss"}  # gates and side outputs
        missing = RUN_STEPS - claimed - ignored
        self.assertFalse(missing, f"unmapped run_update_force steps: {sorted(missing)}")


if __name__ == "__main__":
    unittest.main()
