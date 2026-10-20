from __future__ import annotations

import json
from pathlib import Path
import sys
import unittest

PIPELINE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE_DIR))

from generate_timelines import (  # noqa: E402
    _parse_summary_json,
    _split_method_caption,
    summary_from_method_text,
)

METHOD_TEXT = """## Category Timeline: Bio

### SUB-THEME A: Discrete Diffusion & Flow Molecule Generation (2018→2026, ACCELERATING)
Relative size: LARGE
Branches into:
- **"Graph generative origins"** (2018–2023): MolGAN implicit graph GANs → CoCoGraph, MolHIT.
- **"Discrete diffusion for molecules"** (2024–2026): MoCDiff, GenMol/IIFT, LLM baselines.
Interaction: MERGES WITH Reward-Guided Diffusion.

### SUB-THEME B: Antibody–Antigen Binding Prediction (2026, EMERGING)
Relative size: MEDIUM-LARGE
- **"Epitope-aware docking"** (2026): AbEpiTope, GearBind.

### SUB-THEME C: Multi-State Conformational Binder Design (2024→2026, EMERGING/ACCELERATING)
Relative size: SMALL
- **"Switchable binders"** (2024–2026): SwitchCraft.

### CROSS-CUTTING CONNECTIONS
- none
"""


class TimelineParserTests(unittest.TestCase):
    def test_method_caption_split_preserves_internal_markdown_rules(self) -> None:
        response = """## Category Timeline

### SUB-THEME A
---
### SUB-THEME B

---

CAPTION: A concise figure caption.
"""

        method, caption = _split_method_caption(response, "Category", "ai4s", 10)

        self.assertIn("### SUB-THEME A\n---\n### SUB-THEME B", method)
        self.assertFalse(method.endswith("---"))
        self.assertEqual(caption, "A concise figure caption.")

    def test_method_caption_split_uses_fallback_only_without_marker(self) -> None:
        method, caption = _split_method_caption("## Complete method", "Category", "ai4s", 10)

        self.assertEqual(method, "## Complete method")
        self.assertEqual(caption, "Timeline for Category in ai4s (10 papers).")

        method, caption = _split_method_caption(
            "## Main method", "ai4s", "ai4s", 100, fallback_caption="Research timeline for ai4s."
        )
        self.assertEqual(method, "## Main method")
        self.assertEqual(caption, "Research timeline for ai4s.")

    def test_summary_from_method_text_recovers_subthemes(self) -> None:
        counts = {
            "Discrete Diffusion Molecule Generation": 43,
            "Antibody-Antigen Binding Prediction": 23,
            "Multi-State Conformational Binder Design": 23,
        }
        summary = summary_from_method_text(METHOD_TEXT, "Bio", counts)

        self.assertEqual(summary["category"], "Bio")
        self.assertEqual(summary["paper_count"], 89)
        self.assertEqual(summary["time_span"], "2018-2026")
        names = [s["name"] for s in summary["sub_themes"]]
        self.assertEqual(names, [
            "Discrete Diffusion & Flow Molecule Generation",
            "Antibody–Antigen Binding Prediction",
            "Multi-State Conformational Binder Design",
        ])
        a, b, c = summary["sub_themes"]
        # Rephrased header still maps to its count by token overlap.
        self.assertEqual(a["paper_count"], 43)
        self.assertEqual((a["start"], a["end"], a["status"], a["relative_size"]),
                         ("2018", "2026", "ACCELERATING", "LARGE"))
        self.assertEqual(a["key_developments"], [
            "Graph generative origins (2018–2023)",
            "Discrete diffusion for molecules (2024–2026)",
        ])
        self.assertIn("MolGAN", a["representative_tools"])
        self.assertIn("GenMol/IIFT", a["representative_tools"])
        self.assertNotIn("LLM", a["representative_tools"])
        # Single-year header and dual status.
        self.assertEqual((b["start"], b["end"], b["status"], b["relative_size"]),
                         ("2026", "2026", "EMERGING", "MEDIUM"))
        self.assertEqual(c["status"], "ACCELERATING")
        self.assertEqual(c["paper_count"], 23)

    def test_summary_from_method_text_returns_none_without_subthemes(self) -> None:
        self.assertIsNone(summary_from_method_text("## nothing here", "Bio", {"x": 1}))

    def test_summary_parser_accepts_fence_and_trailing_prose(self) -> None:
        expected = {"category": "Category", "paper_count": 10}
        payload = f"```json\n{json.dumps(expected)}\n```\nAdditional explanation"

        self.assertEqual(_parse_summary_json(payload), expected)

    def test_summary_parser_rejects_missing_or_empty_object(self) -> None:
        with self.assertRaises(json.JSONDecodeError):
            _parse_summary_json("no structured output")
        with self.assertRaises(json.JSONDecodeError):
            _parse_summary_json("{}")


if __name__ == "__main__":
    unittest.main()
