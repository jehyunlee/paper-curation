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
            with self.subTest(provider=provider), patch.object(providers, "generate_structured", return_value={"data": dict(VALID)} ) as call:
                self.assertTrue(engine.write_review(self.item, str(self.dir), [], provider=provider, model=model, cache_dir=str(self.dir / (provider + "-cache"))))
            self.assertEqual(call.call_args.args[:2], (provider, model))
            review = (self.dir / "review.md").read_text(encoding="utf-8")
            self.assertIn("## Essence", review)
            self.assertIn("## Evaluation", review)

    def test_malformed_provider_data_is_not_published_or_cached_complete(self):
        import lib.text_providers as providers
        cache = self.dir / "cache"
        with patch.object(providers, "generate_structured", return_value={"data": {"essence": "partial"}}):
            self.assertFalse(engine.write_review(self.item, str(self.dir), [], cache_dir=str(cache)))
        self.assertFalse((self.dir / "review.md").exists())
        cached = list(cache.glob("*.json")) if cache.exists() else []
        self.assertFalse(any(json.loads(path.read_text()).get("result") == {"essence": "partial"} for path in cached))

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
