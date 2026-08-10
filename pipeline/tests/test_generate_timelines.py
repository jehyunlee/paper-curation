from __future__ import annotations

import json
from pathlib import Path
import sys
import unittest

PIPELINE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE_DIR))

from generate_timelines import _parse_summary_json, _split_method_caption  # noqa: E402


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
