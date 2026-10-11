"""Prompt and CLI contracts for generated workflow illustrations."""
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE))

import generate_usage_diagram
import generate_workflow


class DiagramPromptTests(unittest.TestCase):
    def test_multi_path_phase_row_uses_first_script(self):
        phases = generate_workflow._parse_phase_rows(
            "| 4.5 | `pipeline/topic_modeling.py` + `pipeline/extract_insights.py` + "
            "`pipeline/lib/related.py` | judge related paper pairs |"
        )
        self.assertEqual(phases, ["Step 4.5: topic_modeling\n  judge related paper pairs"])

    def test_workflow_cat_prompt_has_correct_claude_and_option_facts(self):
        method = generate_workflow.build_method_text()
        phases = [line for line in method.splitlines() if line.startswith("Step ")]
        prompt = method + generate_workflow.VISUAL_RULES_DEFAULT + generate_workflow.build_style_text(phases, "cat")
        self.assertIn("Haiku", prompt)
        self.assertNotIn("Claude (review/classify)", prompt)
        self.assertNotIn("Claude (AI reviews, classification", prompt)
        self.assertNotIn("Workflow diagram", prompt)

    def test_cat_defaults(self):
        self.assertEqual(generate_workflow._parse_args([]).style, "cat")
        self.assertEqual(generate_usage_diagram._parse_args([]).style, "cat")

    def test_usage_cat_prompt_uses_all_lane_labels(self):
        for lang in ("ko", "en"):
            method, _ = generate_usage_diagram.build_cat_prompt(lang)
            for _, name, requirement, cells in generate_usage_diagram.LABELS[lang]["lanes"]:
                self.assertIn(name, method)
                self.assertIn(requirement, method)
                for cell in cells:
                    self.assertIn(cell, method)

    def test_usage_plain_style_calls_existing_renderer(self):
        with patch.object(generate_usage_diagram, "render") as render:
            self.assertEqual(generate_usage_diagram.main(["--style", "plain", "--lang", "ko"]), 0)
        render.assert_called_once_with("ko")


if __name__ == "__main__":
    unittest.main()
