"""Data Artifacts block rendered under Limitation & Further Study."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

PIPELINE_DIR = Path(__file__).resolve().parents[1]
if str(PIPELINE_DIR) not in sys.path:
    sys.path.insert(0, str(PIPELINE_DIR))

from lib import data_artifacts as da


class CatalogTests(unittest.TestCase):
    def test_catalog_matches_atlas_shape(self):
        stages, effects = da._catalog()
        self.assertEqual(list(stages), ["design", "capture", "observe", "report",
                                        "process", "interpret", "feedback"])
        self.assertEqual(len(effects), 78)
        self.assertTrue(all(e["stage"] in stages for e in effects.values()))

    def test_schema_enum_is_catalog_ids(self):
        schema = da.output_schema()["properties"]["data_artifacts"]
        self.assertEqual(schema["items"]["properties"]["id"]["enum"], da.effect_ids())
        self.assertEqual(schema["maxItems"], da.MAX_ITEMS)

    def test_prompt_lists_every_effect_with_its_stage(self):
        prompt = da.system_prompt()
        self.assertIn("nonresponse | ", prompt)
        self.assertEqual(prompt.count(" | "), 3 * len(da.effect_ids()) + 3)


class AnalyzeTests(unittest.TestCase):
    def test_result_is_cached_per_paper_and_text_is_bounded(self):
        import lib.text_providers as providers
        reply = {"data": {"data_artifacts": [{"id": "hawthorne", "rel": 2, "evidence": "e", "note": "n"}]}}
        with tempfile.TemporaryDirectory() as cache, \
                patch.object(providers, "generate_structured", return_value=reply) as call:
            kwargs = dict(title="T", abstract="A", paper_text="x" * 30_000, provider="anthropic",
                          model="claude-sonnet-5", credential_ref=None, cache_dir=cache)
            self.assertEqual(da.analyze(**kwargs)[0]["id"], "hawthorne")
            self.assertEqual(da.analyze(**kwargs)[0]["id"], "hawthorne")
        call.assert_called_once()
        self.assertEqual(call.call_args.kwargs["capability"], "data_artifacts")
        self.assertEqual(call.call_args.args[3].count("x"), da.TEXT_CHARACTER_LIMIT)

    def test_adapter_decodes_array_sent_as_json_text(self):
        # Observed on LabOS 10973: tool input {"data_artifacts": "[{...}]"}.
        import lib.text_providers as providers
        items = [{"id": "hawthorne", "rel": 3, "evidence": "안경을 착용했다.", "note": "비교가 필요하다."}]
        fixed = providers._decode_stringified_containers(
            {"data_artifacts": json.dumps(items, ensure_ascii=False)}, da.output_schema())
        providers._validate_schema_shape(fixed, da.output_schema())
        self.assertEqual(fixed["data_artifacts"], items)
        wrapped = providers._decode_stringified_containers(
            {"data_artifacts": json.dumps({"data_artifacts": items}, ensure_ascii=False)}, da.output_schema())
        self.assertEqual(wrapped["data_artifacts"], items)
        untouched = providers._decode_stringified_containers({"data_artifacts": "not json"}, da.output_schema())
        self.assertEqual(untouched, {"data_artifacts": "not json"})

    def test_missing_list_raises_and_is_not_cached(self):
        import lib.text_providers as providers
        with tempfile.TemporaryDirectory() as cache, \
                patch.object(providers, "generate_structured", return_value={"data": {}}):
            with self.assertRaises(da.DataArtifactsError):
                da.analyze(title="T", abstract="A", paper_text="text", provider="anthropic",
                           model="claude-sonnet-5", credential_ref=None, cache_dir=cache)
            self.assertEqual(list(Path(cache).glob("*.json")), [])


class RenderTests(unittest.TestCase):
    def test_empty_list_states_no_signal(self):
        self.assertEqual(da.render([]), "### Data Artifacts\n\n" + da.EMPTY_LINE)

    def test_item_keeps_atlas_fields_without_box(self):
        out = da.render([{"id": "nonresponse", "rel": 3,
                          "evidence": "응답률 7%의\n설문을 썼다.", "note": "응답자 편향을 확인한다."}])
        lines = out.splitlines()
        self.assertEqual(lines[0], "### Data Artifacts")
        self.assertRegex(lines[2], r"^- \*\*.+\*\* \(.+\) · 2 포착·표본 · ●●●$")
        self.assertEqual(lines[3], "  - 근거: 응답률 7%의 설문을 썼다.")
        self.assertEqual(lines[4], "  - 설명: 응답자 편향을 확인한다.")

    def test_duplicates_and_unknown_ids_are_dropped(self):
        out = da.render([
            {"id": "streetlight", "rel": 1, "evidence": "a", "note": "b"},
            {"id": "streetlight", "rel": 3, "evidence": "c", "note": "d"},
            {"id": "not-an-effect", "rel": 2, "evidence": "e", "note": "f"},
        ])
        self.assertEqual(out.count("- **"), 1)
        self.assertIn("●○○", out)
        self.assertNotIn("not-an-effect", out)

    def test_only_unknown_ids_falls_to_empty_line(self):
        self.assertTrue(da.render([{"id": "x", "rel": 1}]).endswith(da.EMPTY_LINE))


if __name__ == "__main__":
    unittest.main()
