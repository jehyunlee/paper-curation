"""Canonical review writer provider integration without network calls."""
from __future__ import annotations

import json
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch

PIPELINE_DIR = Path(__file__).resolve().parents[1]
if str(PIPELINE_DIR) not in sys.path:
    sys.path.insert(0, str(PIPELINE_DIR))

import run_update_force as engine


# Section-filling fields clear the 50-character floor the real contract
# enforces (validate_papers SHORT_SECTION); short fields may stay short.
_SECTION = "이 문장은 한 섹션을 채우는 서술로, 검증 게이트의 최소 길이를 넘기도록 충분히 길게 썼다. "
VALID = {
    "essence": "핵심 결과를 충분히 설명하는 문장입니다. " + _SECTION, "fig_essence": 0,
    "known": "기존 연구입니다.", "gap": "해결할 간극입니다.", "why": "중요한 이유입니다.",
    "approach": "제안 방법입니다.", "achievement": "검증된 성과입니다. " + _SECTION, "fig_achievement": 0,
    "how": "실험 방법입니다. " + _SECTION, "fig_how": 0, "originality": "독창성입니다. " + _SECTION,
    "limitation": "한계입니다. " + _SECTION, "novelty": 4, "technical": 4, "significance": 4,
    "clarity": 4, "overall": 4, "verdict": "신뢰할 수 있는 결론입니다.",
}


ARTIFACTS = [{"id": "streetlight", "rel": 2, "evidence": "공개 데이터셋만 썼다.",
              "note": "빠진 대상을 확인해야 한다."}]


def _by_capability(*_args, capability, **_kwargs):
    if capability == "data_artifacts":
        return {"data": {"data_artifacts": list(ARTIFACTS)}}
    return {"data": dict(VALID)}


class ReviewCompletenessGateTests(unittest.TestCase):
    """Partial answers that validate_papers would flag must never be cached as complete."""

    def test_valid_fixture_is_complete(self):
        self.assertTrue(engine._review_response_is_complete(dict(VALID)))

    def test_empty_limitation_is_partial(self):
        # 10751/10905: Limitation & Further Study rendered empty because the
        # gate never required the field.
        self.assertFalse(engine._review_response_is_complete({**VALID, "limitation": ""}))

    def test_short_section_field_is_partial(self):
        # 10788: a 20-character Achievement passed the tool schema (minLength
        # 20) and became a permanent SHORT_SECTION.
        self.assertFalse(engine._review_response_is_complete({**VALID, "achievement": "검증된 성과를 스무 글자로 다 채운다."}))

    def test_short_non_section_fields_stay_allowed(self):
        self.assertTrue(engine._review_response_is_complete({**VALID, "known": "짧은 문장.", "verdict": "짧은 총평."}))


def _xml_dump(fields: dict, open_tag=lambda t: f"<{t}>", close=True) -> str:
    """The review as claude-sonnet-5 dumps it into one tool field."""
    return "\n".join(
        f"{open_tag(t)}{v}" + (f"</{t}>" if close else "")
        for t, v in fields.items()) + "\n</emit_review>"


class MalformedTagSalvageTests(unittest.TestCase):
    """Tag shapes from the RoRI 'Seize the Meta-Moment' report: three of four
    calls failed as 'review payload is incomplete'."""

    def assert_recovers(self, data, field):
        fixed = engine._salvage_review_data(data)
        self.assertTrue(engine._review_response_is_complete(fixed), fixed)
        self.assertEqual(fixed[field], VALID[field].strip())
        return fixed

    def test_open_tag_with_an_attribute(self):
        dump = _xml_dump(VALID).replace("<achievement>", '<achievement fig="0">')
        fixed = self.assert_recovers({"essence": dump}, "achievement")
        self.assertEqual(fixed["overall"], 4)

    def test_open_tag_with_a_stray_quote(self):
        dump = _xml_dump(VALID).replace("<originality>", '<originality">')
        self.assert_recovers({"essence": dump}, "originality")

    def test_unclosed_parameter_ends_with_its_carrier_field(self):
        # `known` carries an unclosed <parameter name="achievement">; the clean
        # `how` field that follows must not be read into it.
        rest = {k: v for k, v in VALID.items() if k not in {"essence", "known", "achievement"}}
        data = {
            "essence": VALID["essence"] + '</parameter>\n<parameter name="known">',
            "known": VALID["known"] + '</parameter>\n<parameter name="achievement">'
                     + VALID["achievement"],
            **rest,
        }
        fixed = self.assert_recovers(data, "achievement")
        self.assertEqual(fixed["known"], VALID["known"].strip())
        self.assertEqual(fixed["how"], VALID["how"].strip())

    def test_clean_payload_is_untouched(self):
        self.assertEqual(engine._salvage_review_data(dict(VALID)), VALID)


class PdfMatchSanityTests(unittest.TestCase):
    """The PDF-to-item check that blocks a review before any provider call."""

    TITLE = "Evolution of the social network of scientific collaborations"

    def check(self, last_name, text):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "text.md"
            path.write_text(text, encoding="utf-8")
            return engine._zotero_text_sanity(
                {"title": self.TITLE, "DOI": "10.1016/S0378-4371(02)00736-7",
                 "creators": [{"lastName": last_name, "firstName": "A.-L."}]},
                str(path))[0]

    def test_tex_spacing_accent_matches_the_zotero_name(self):
        # arXiv PDF of Barabási et al. prints "Barab´asi"; the review was refused.
        self.assertTrue(self.check(
            "Barabási", "Evolution of the social network of scientiﬁc "
                        "collaborations A.L. Barab´asi1,2, H. Jeong"))

    def test_other_first_author_still_fails(self):
        self.assertFalse(self.check(
            "Kubler", "Evolution of the social network of scientific "
                      "collaborations A.L. Barabasi, H. Jeong"))


class ReviewProviderIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        (self.dir / "text.md").write_text("source evidence " * 200, encoding="utf-8")
        self.item = {"title": "Provider Contract", "creators": [], "date": "2026", "DOI": "", "abstractNote": "abstract", "url": ""}

    def tearDown(self):
        self.tmp.cleanup()

    def test_each_selected_provider_writes_same_canonical_review(self):
        import lib.text_providers as providers
        for provider, model in (("anthropic", "claude-sonnet-5"), ("openai", "gpt-5"), ("google", "gemini-3.1-pro-preview")):
            with self.subTest(provider=provider), patch.object(providers, "generate_structured", side_effect=_by_capability) as call:
                self.assertTrue(engine.write_review(self.item, str(self.dir), [], provider=provider, model=model, cache_dir=str(self.dir / (provider + "-cache"))))
            review_call, artifact_call = call.call_args_list
            self.assertEqual(review_call.kwargs["capability"], "review")
            self.assertEqual(artifact_call.kwargs["capability"], "data_artifacts")
            self.assertEqual(review_call.args[:2], (provider, model))
            self.assertEqual(artifact_call.args[:2], (provider, model))
            review = (self.dir / "review.md").read_text(encoding="utf-8")
            self.assertIn("## Essence", review)
            self.assertIn("## Evaluation", review)
            limitation = review.split("## Limitation & Further Study", 1)[1].split("## Evaluation", 1)[0]
            self.assertIn("### Data Artifacts", limitation)
            self.assertIn("- **가로등 효과** (Streetlight effect) · 1 지표 설계 · ●●○", limitation)
            self.assertIn("  - 근거: 공개 데이터셋만 썼다.", limitation)
            self.assertIn("  - 설명: 빠진 대상을 확인해야 한다.", limitation)
            self.assertIn("streetlight | 가로등 효과 | design |", artifact_call.args[2])
            self.assertIn("source evidence", artifact_call.args[3])
            self.assertNotIn("data_artifacts", review_call.args[4]["properties"])

    def test_malformed_provider_data_is_not_published_or_cached_complete(self):
        import lib.text_providers as providers
        cache = self.dir / "cache"
        with patch.object(providers, "generate_structured", return_value={"data": {"essence": "partial"}}):
            self.assertFalse(engine.write_review(self.item, str(self.dir), [], cache_dir=str(cache)))
        self.assertFalse((self.dir / "review.md").exists())
        cached = list(cache.glob("*.json")) if cache.exists() else []
        self.assertFalse(any(json.loads(path.read_text()).get("result") == {"essence": "partial"} for path in cached))

    def test_failed_data_artifacts_analysis_fails_the_review(self):
        import lib.text_providers as providers

        def no_list(*_args, capability, **_kwargs):
            return {"data": dict(VALID) if capability == "review" else {"data_artifacts": "none"}}

        with patch.object(providers, "generate_structured", side_effect=no_list):
            self.assertFalse(engine.write_review(self.item, str(self.dir), [], cache_dir=str(self.dir / "cache")))
        self.assertFalse((self.dir / "review.md").exists())

    def test_data_artifacts_requires_a_cloud_provider(self):
        import lib.text_providers as providers
        with self.assertRaises(providers.UnsupportedCapabilityError):
            providers._validate_selection("ollama", None, "data_artifacts")

    def test_adapter_uses_selected_sdk_with_retries_disabled(self):
        import lib.text_providers as providers
        schema = {"required": list(VALID)}
        tool = types.SimpleNamespace(type="tool_use", name="emit_review", input=dict(VALID))
        created = []

        class Anthropic:
            def __init__(self, **kwargs):
                created.append(kwargs)
                self.messages = types.SimpleNamespace(
                    create=lambda **_: types.SimpleNamespace(content=[tool], usage={})
                )

        with (
            patch.dict(sys.modules, {"anthropic": types.SimpleNamespace(Anthropic=Anthropic)}),
            patch.object(providers, "_credential", return_value="secret"),
        ):
            result = providers.generate_structured(
                "anthropic", None, "system", "prompt", schema,
                capability="review", max_output_tokens=4000,
            )
        self.assertEqual(result["data"], VALID)
        self.assertEqual(created, [{"api_key": "secret", "max_retries": 0}])

    def test_openai_sdk_is_selected_without_anthropic_import(self):
        import lib.text_providers as providers
        schema = {"required": list(VALID)}
        created = []

        class OpenAI:
            def __init__(self, **kwargs):
                created.append(kwargs)
                choice = types.SimpleNamespace(
                    finish_reason="stop",
                    message=types.SimpleNamespace(content=json.dumps(VALID)),
                )
                self.chat = types.SimpleNamespace(completions=types.SimpleNamespace(
                    create=lambda **_: types.SimpleNamespace(choices=[choice], usage={})
                ))

        with (
            patch.dict(sys.modules, {"openai": types.SimpleNamespace(OpenAI=OpenAI)}),
            patch.object(providers, "_credential", return_value="secret"),
        ):
            result = providers.generate_structured(
                "openai", None, "system", "prompt", schema,
                capability="review", max_output_tokens=4000,
            )
        self.assertEqual(result["data"], VALID)
        self.assertEqual(created, [{"api_key": "secret", "max_retries": 0}])

    def test_google_sdk_is_selected_with_single_attempt(self):
        import lib.text_providers as providers
        schema = {"required": list(VALID)}
        created = []

        class Client:
            def __init__(self, **kwargs):
                created.append(kwargs)
                self.models = types.SimpleNamespace(generate_content=lambda **_: types.SimpleNamespace(
                    text=json.dumps(VALID), candidates=[], usage_metadata={}))

        with (
            patch("google.genai.Client", Client),
            patch.object(providers, "_credential", return_value="secret"),
        ):
            result = providers.generate_structured(
                "google", None, "system", "prompt", schema,
                capability="review", max_output_tokens=4000,
            )
        self.assertEqual(result["data"], VALID)
        self.assertEqual(created[0]["http_options"].retry_options.attempts, 1)


if __name__ == "__main__":
    unittest.main()
