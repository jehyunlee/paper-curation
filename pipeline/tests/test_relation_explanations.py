"""Grounded pair explanations use temporary originals and a mocked provider."""
from __future__ import annotations

import copy
import hashlib
import json
import sys
import tempfile
import unicodedata
import unittest
from pathlib import Path
from unittest.mock import patch

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

from lib import relation_explanations as explanations
from lib import text_providers


SOURCE_QUOTE = "We extend the sequential search baseline with parallel candidate evaluation."
TARGET_QUOTE = "Our sequential search baseline evaluates one candidate at each iteration."
FORWARD_REASON = (
    "두 논문은 후보 탐색의 평가 비용을 다룹니다. 비교 대상의 순차 탐색을 기반으로 "
    "현재 논문은 후보를 병렬 평가하므로, 같은 과제에서 탐색 비용과 정확도의 변화를 비교합니다."
)
REVERSE_REASON = (
    "이 논문이 제시한 순차 탐색은 비교 논문에서 병렬 후보 평가로 확장됩니다. "
    "두 방법은 동일한 과제의 비용과 정확도를 측정하지만 후보를 평가하는 순서가 다릅니다."
)


class RelationExplanationTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        self.papers, self.cache = root / "papers", root / "cache"
        self.source = {"slug": "001_Parallel_Search", "title": "Parallel candidate evaluation"}
        self.target = {"slug": "002_Sequential_Search", "title": "Sequential search baseline"}
        self.texts = {
            self.source["slug"]: "# Parallel search\n\n" + SOURCE_QUOTE + "\nWe measure cost and accuracy on identical tasks.\n",
            self.target["slug"]: "# Sequential search\n\n" + TARGET_QUOTE + "\nWe report the evaluation cost on the same tasks.\n",
        }
        for slug, text in self.texts.items():
            directory = self.papers / slug
            directory.mkdir(parents=True)
            (directory / "text.md").write_text(text, encoding="utf-8")
        paths = patch.multiple(explanations, PAPERS_DIR=self.papers, CACHE_DIR=self.cache)
        paths.start()
        self.addCleanup(paths.stop)
        self.payload = {
            "forward": {"relation": "foundation", "reason": FORWARD_REASON,
                        "evidence": {"source_quote": SOURCE_QUOTE, "target_quote": TARGET_QUOTE}},
            "reverse": {"relation": "extension", "reason": REVERSE_REASON,
                        "evidence": {"source_quote": TARGET_QUOTE, "target_quote": SOURCE_QUOTE}},
        }
        provider = patch.object(text_providers, "generate_structured", side_effect=self._generate)
        self.generate = provider.start()
        self.addCleanup(provider.stop)

    def _generate(self, provider, model, *_args, **_kwargs):
        return {"data": copy.deepcopy(self.payload), "provider": provider, "model": model}

    def _explain(self):
        return explanations.explain_pair(self.source, self.target)

    def _cache_paths(self):
        return set(self.cache.glob("*.json"))

    def _assert_invalid_payload(self, payload):
        response = {"data": payload, "provider": "anthropic",
                    "model": text_providers.DEFAULT_MODELS["anthropic"]}
        with patch.object(text_providers, "generate_structured", return_value=response) as generate:
            with self.assertRaises(explanations.RelationExplanationError):
                self._explain()
        self.assertEqual(generate.call_count, 2)
        self.assertEqual(self._cache_paths(), set())

    def test_invalid_fresh_payload_is_repaired_once_and_only_the_valid_result_is_cached(self):
        invalid = self._generate("anthropic", text_providers.DEFAULT_MODELS["anthropic"])
        invalid["data"]["forward"]["evidence"]["source_quote"] = (
            "This invented quotation does not occur in the original search paper."
        )
        valid = self._generate("anthropic", text_providers.DEFAULT_MODELS["anthropic"])
        with patch.object(text_providers, "generate_structured", side_effect=[invalid, valid]) as generate, \
             patch.object(explanations, "atomic_write_json", wraps=explanations.atomic_write_json) as write:
            result = self._explain()
            self.assertEqual(generate.call_count, 2)
            first, repair = generate.call_args_list
            original_prompt = json.loads(first.args[3])
            repair_prompt = json.loads(repair.args[3])
            self.assertEqual(repair_prompt["source"], original_prompt["source"])
            self.assertEqual(repair_prompt["target"], original_prompt["target"])
            self.assertEqual(repair_prompt["previous_payload"], invalid["data"])
            self.assertIn("source_quote", repair_prompt["validation_error"])
            self.assertNotIn("validation_error", original_prompt)
            self.assertNotIn("previous_payload", original_prompt)
            self.assertEqual(repair.args[:3], first.args[:3])
            self.assertEqual(repair.args[4:], first.args[4:])
            self.assertEqual(repair.kwargs, first.kwargs)
            self.assertEqual(result["reason"], FORWARD_REASON)
            self.assertEqual(result["evidence"]["source_quote"], SOURCE_QUOTE)
            write.assert_called_once()
            (cache,) = self._cache_paths()
            stored = json.loads(cache.read_text(encoding="utf-8"))
            self.assertEqual(stored["result"], valid)
            expected_prompt_hash = hashlib.sha256(
                (first.args[2] + "\n" + first.args[3]).encode("utf-8")
            ).hexdigest()
            self.assertEqual(stored["identity"]["prompt_sha256"], expected_prompt_hash)
            self.assertEqual(self._explain(), result)
            self.assertEqual(generate.call_count, 2)
            write.assert_called_once()

    def test_two_invalid_fresh_payloads_raise_the_last_validation_error_without_a_third_attempt(self):
        first = self._generate("anthropic", text_providers.DEFAULT_MODELS["anthropic"])
        first["data"]["forward"]["evidence"]["source_quote"] = (
            "This invented quotation does not occur in the original search paper."
        )
        second = self._generate("anthropic", text_providers.DEFAULT_MODELS["anthropic"])
        second["data"]["reverse"]["reason"] = second["data"]["forward"]["reason"]
        valid = self._generate("anthropic", text_providers.DEFAULT_MODELS["anthropic"])
        with patch.object(text_providers, "generate_structured", side_effect=[first, second, valid]) as generate, \
             patch.object(explanations, "atomic_write_json") as write:
            with self.assertRaisesRegex(explanations.RelationExplanationError, "reverse explanation"):
                self._explain()
        self.assertEqual(generate.call_count, 2)
        write.assert_not_called()
        self.assertEqual(self._cache_paths(), set())

    def test_quote_whitespace_is_recovered_as_verbatim_source_without_retry(self):
        actual = SOURCE_QUOTE.replace("sequential search", "sequential\r\n\tsearch")
        path = self.papers / self.source["slug"] / "text.md"
        path.write_bytes(self.texts[self.source["slug"]].replace(SOURCE_QUOTE, actual).encode())
        result = self._explain()
        self.generate.assert_called_once()
        self.assertEqual(result["evidence"]["source_quote"], actual)
        self.assertEqual(result["reverse"]["evidence"]["target_quote"], actual)
        stored = json.loads(next(iter(self._cache_paths())).read_text())
        self.assertEqual(stored["result"]["data"]["forward"]["evidence"]["source_quote"], actual)

    def test_whitespace_recovery_does_not_accept_changed_punctuation(self):
        payload = copy.deepcopy(self.payload)
        payload["forward"]["evidence"]["source_quote"] = SOURCE_QUOTE.replace("baseline", "baseline,")
        self._assert_invalid_payload(payload)

    def test_corpus_field_labels_reach_the_prompt(self):
        self.source["classifications"] = {"ai4s": {
            "primary_category": "Autonomous AI Scientific Discovery",
            "all_categories": ["Autonomous AI Scientific Discovery", "Formal Mathematical Theorem Proving"],
            "sub_category": "Autonomous Scientific Discovery Systems"}}
        self._explain()
        prompt = json.loads(self.generate.call_args.args[3])
        self.assertEqual(prompt["source"]["fields"], [{
            "topic": "ai4s", "category": "Autonomous AI Scientific Discovery",
            "sub_category": "Autonomous Scientific Discovery Systems"}])
        self.assertEqual(prompt["target"]["fields"], [])
        self.assertIn("연구 분야", self.generate.call_args.args[2])

    def test_reason_about_retrieval_instead_of_content_is_rejected(self):
        for phrase in ("SPECTER2 임베딩에서 가까운", "코사인 유사도가 높은", "BM25 순위가 높은"):
            with self.subTest(phrase=phrase):
                payload = copy.deepcopy(self.payload)
                payload["forward"]["reason"] = f"두 논문은 {phrase} 후보 탐색 연구로, 탐색 비용과 정확도를 함께 비교할 수 있습니다."
                self._assert_invalid_payload(payload)

    def test_earlier_paper_cannot_apply_a_later_papers_method(self):
        self.source["date"] = "2026-10-22"
        self.target["date"] = "2025-03-01"
        payload = copy.deepcopy(self.payload)
        payload["forward"]["relation"] = "application"
        self._assert_invalid_payload(payload)

    def test_later_paper_cannot_be_a_prior_foundation(self):
        self.source["date"] = "2024-01-01"
        self.target["date"] = "2026-01-01"
        self._assert_invalid_payload(copy.deepcopy(self.payload))

    def test_exact_quotes_korean_reasons_and_model_provenance_are_retained(self):
        result = self._explain()
        self.generate.assert_called_once()
        args, kwargs = self.generate.call_args
        self.assertEqual(args[:2], ("anthropic", text_providers.DEFAULT_MODELS["anthropic"]))
        self.assertEqual(kwargs["capability"], "comparison")
        self.assertEqual(kwargs["credential_ref"], "credential:anthropic")
        prompt = json.loads(args[3])
        self.assertEqual(prompt["source"]["slug"], self.source["slug"])
        self.assertEqual(prompt["target"]["slug"], self.target["slug"])
        self.assertIn(SOURCE_QUOTE, "\n".join(prompt["source"]["excerpts"]))
        self.assertIn(TARGET_QUOTE, "\n".join(prompt["target"]["excerpts"]))
        self.assertEqual(set(args[4]["required"]), {"forward", "reverse"})
        self.assertEqual(result["relation"], "foundation")
        self.assertEqual(result["reason"], FORWARD_REASON)
        self.assertEqual(result["model"], text_providers.DEFAULT_MODELS["anthropic"])
        self.assertEqual(result["reverse"]["relation"], "extension")
        self.assertEqual(result["reverse"]["reason"], REVERSE_REASON)
        source_hash = hashlib.sha256(self.texts[self.source["slug"]].encode("utf-8")).hexdigest()
        target_hash = hashlib.sha256(self.texts[self.target["slug"]].encode("utf-8")).hexdigest()
        self.assertEqual(result["evidence"], {
            "source_quote": SOURCE_QUOTE, "target_quote": TARGET_QUOTE,
            "source_sha256": source_hash, "target_sha256": target_hash,
            "provider": "anthropic", "prompt_version": explanations.PROMPT_VERSION,
        })
        self.assertEqual(result["reverse"]["evidence"], {
            "source_quote": TARGET_QUOTE, "target_quote": SOURCE_QUOTE,
            "source_sha256": target_hash, "target_sha256": source_hash,
            "provider": "anthropic", "prompt_version": explanations.PROMPT_VERSION,
        })

    def test_repeat_and_reversed_pairs_reuse_the_cache_with_the_correct_perspective(self):
        forward = self._explain()
        paths = self._cache_paths()
        self.assertEqual(len(paths), 1)
        self.assertEqual(self._explain(), forward)
        reverse = explanations.explain_pair(self.target, self.source)
        self.generate.assert_called_once()
        self.assertEqual(self._cache_paths(), paths)
        self.assertEqual({key: reverse[key] for key in ("relation", "reason", "evidence")},
                         forward["reverse"])
        self.assertEqual(reverse["reverse"], {
            key: forward[key] for key in ("relation", "reason", "evidence")
        })
        self.assertNotEqual(reverse["reason"], forward["reason"])

    def test_cache_key_changes_when_either_original_changes(self):
        for paper in (self.source, self.target):
            path = self.papers / paper["slug"] / "text.md"
            path.write_text(self.texts[paper["slug"]] + "x" * 60000, encoding="utf-8")
        self._explain()
        previous = self._cache_paths()
        prompt = self.generate.call_args.args[3]
        for paper in (self.source, self.target):
            with self.subTest(slug=paper["slug"]):
                path = self.papers / paper["slug"] / "text.md"
                text = path.read_text(encoding="utf-8")
                path.write_text(text[:12000] + "y" + text[12001:], encoding="utf-8")
                result = self._explain()
                self.assertEqual(len(self._cache_paths() - previous), 1)
                self.assertEqual(self.generate.call_args.args[3], prompt,
                                 "edits outside the supplied excerpts must still invalidate the cache")
                key = "source_sha256" if paper is self.source else "target_sha256"
                self.assertEqual(result["evidence"][key], hashlib.sha256(path.read_bytes()).hexdigest())
                previous = self._cache_paths()
        self.assertEqual(self.generate.call_count, 3)

    def test_cache_key_changes_with_the_selected_model(self):
        old = self._explain()
        previous = self._cache_paths()
        with patch.dict(text_providers.DEFAULT_MODELS, {"anthropic": "comparison-test-model-v2"}):
            changed = self._explain()
        self.assertNotEqual(changed["model"], old["model"])
        self.assertEqual(changed["model"], "comparison-test-model-v2")
        self.assertEqual(len(self._cache_paths() - previous), 1)
        self.assertEqual(self.generate.call_count, 2)

    def test_cache_key_changes_with_prompt_version(self):
        self._explain()
        previous = self._cache_paths()
        with patch.object(explanations, "PROMPT_VERSION", "paper-comparison-test-v2"):
            result = self._explain()
        self.assertEqual(result["evidence"]["prompt_version"], "paper-comparison-test-v2")
        self.assertEqual(len(self._cache_paths() - previous), 1)
        self.assertEqual(self.generate.call_count, 2)

    def test_cache_key_changes_with_actual_prompt_without_a_version_bump(self):
        self._explain()
        previous = self._cache_paths()
        with patch.object(explanations, "SYSTEM_PROMPT", explanations.SYSTEM_PROMPT + "\n추가 비교 지침."):
            self._explain()
        self.assertEqual(len(self._cache_paths() - previous), 1)
        self.assertEqual(self.generate.call_count, 2)

    def test_missing_quotes_are_rejected_without_cache_or_fallback(self):
        for direction in ("forward", "reverse"):
            for field in ("source_quote", "target_quote"):
                with self.subTest(direction=direction, field=field):
                    payload = copy.deepcopy(self.payload)
                    del payload[direction]["evidence"][field]
                    self._assert_invalid_payload(payload)

    def test_invented_and_wrong_direction_quotes_are_rejected(self):
        for direction in ("forward", "reverse"):
            for field in ("source_quote", "target_quote"):
                with self.subTest(direction=direction, field=field):
                    payload = copy.deepcopy(self.payload)
                    payload[direction]["evidence"][field] = "This invented quotation is absent from both original papers."
                    self._assert_invalid_payload(payload)
        payload = copy.deepcopy(self.payload)
        payload["reverse"]["evidence"] = copy.deepcopy(payload["forward"]["evidence"])
        self._assert_invalid_payload(payload)

    def test_quotes_cannot_be_empty_or_short(self):
        for quote in ("", "We extend"):
            with self.subTest(quote=quote):
                payload = copy.deepcopy(self.payload)
                payload["forward"]["evidence"]["source_quote"] = quote
                self._assert_invalid_payload(payload)

    def test_empty_short_english_and_cosine_template_reasons_are_rejected(self):
        invalid = ("", "두 논문은 비슷합니다.",
                   "Both studies investigate search methods but use different candidate evaluation orders.",
                   "SPECTER2 임베딩 공간에서 가까운 논문입니다. 코사인 유사도가 높아 관련 논문으로 선택되었습니다.")
        for reason in invalid:
            with self.subTest(reason=reason):
                payload = copy.deepcopy(self.payload)
                payload["forward"]["reason"] = reason
                self._assert_invalid_payload(payload)

    def test_reverse_must_be_complete_and_independently_worded(self):
        for mutation in ("missing", "identical", "invalid_relation"):
            with self.subTest(mutation=mutation):
                payload = copy.deepcopy(self.payload)
                if mutation == "missing":
                    del payload["reverse"]
                elif mutation == "identical":
                    payload["reverse"]["reason"] = payload["forward"]["reason"]
                else:
                    payload["reverse"]["relation"] = "similarity"
                self._assert_invalid_payload(payload)

    def test_quotes_present_only_outside_the_sent_excerpts_are_rejected(self):
        path = self.papers / self.source["slug"] / "text.md"
        path.write_text("A" * 12000 + SOURCE_QUOTE + "B" * 40000, encoding="utf-8")
        with self.assertRaises(explanations.RelationExplanationError):
            self._explain()
        self.assertEqual(self.generate.call_count, 2)
        prompt = json.loads(self.generate.call_args.args[3])
        self.assertNotIn(SOURCE_QUOTE, "\n".join(prompt["source"]["excerpts"]))
        self.assertEqual(self._cache_paths(), set())

    def test_provider_failures_propagate_without_a_cosine_fallback_or_cache(self):
        failures = (text_providers.AuthenticationError("credential unavailable"),
                    text_providers.ProviderResponseError("invalid provider response"),
                    explanations.RelationExplanationError("provider raised a non-validation error"),
                    RuntimeError("connection unavailable"))
        for failure in failures:
            with self.subTest(failure=type(failure).__name__):
                with patch.object(text_providers, "generate_structured", side_effect=failure) as generate:
                    with self.assertRaises(type(failure)) as caught:
                        self._explain()
                self.assertIs(caught.exception, failure)
                generate.assert_called_once()
                self.assertEqual(self._cache_paths(), set())

    def test_non_relation_validation_errors_are_not_retried(self):
        failure = RuntimeError("unexpected validation failure")
        with patch.object(explanations, "_validate", side_effect=failure) as validate:
            with self.assertRaises(RuntimeError) as caught:
                self._explain()
        self.assertIs(caught.exception, failure)
        self.generate.assert_called_once()
        validate.assert_called_once()
        self.assertEqual(self._cache_paths(), set())

    def test_wrong_model_or_provider_provenance_is_rejected(self):
        for field, value in (("model", "unexpected-model"), ("provider", "openai")):
            with self.subTest(field=field):
                response = self._generate("anthropic", text_providers.DEFAULT_MODELS["anthropic"])
                response[field] = value
                with patch.object(text_providers, "generate_structured", return_value=response) as generate:
                    with self.assertRaises(explanations.RelationExplanationError):
                        self._explain()
                generate.assert_called_once()
                self.assertEqual(self._cache_paths(), set())

    def test_nfd_slug_combining_marks_are_preserved_in_the_prompt_and_cache_identity(self):
        slugs = (unicodedata.normalize("NFD", "001_Café_Search"),
                 "001_Grave" + chr(0x0300) + "_Search", "001_Mark" + chr(0x036F) + "_Search")
        for slug in slugs:
            with self.subTest(slug=slug):
                source = {**self.source, "slug": slug}
                directory = self.papers / slug
                directory.mkdir()
                (directory / "text.md").write_text(self.texts[self.source["slug"]], encoding="utf-8")
                previous = self._cache_paths()
                before = self.generate.call_count
                result = explanations.explain_pair(source, self.target)
                self.assertEqual(json.loads(self.generate.call_args.args[3])["source"]["slug"], slug)
                (cache,) = self._cache_paths() - previous
                stored = json.loads(cache.read_text(encoding="utf-8"))
                self.assertEqual(stored["identity"]["source_slug"], slug)
                self.assertEqual(explanations.explain_pair(source, self.target), result)
                self.assertEqual(self.generate.call_count, before + 1)

    def test_missing_and_invalid_originals_fail_before_the_provider(self):
        for paper in (self.source, self.target):
            path = self.papers / paper["slug"] / "text.md"
            original = path.read_bytes()
            for invalid in (None, b"", b" \n", b"\xff", b"original\x00content"):
                with self.subTest(slug=paper["slug"], invalid=invalid):
                    if invalid is None:
                        path.unlink()
                    else:
                        path.write_bytes(invalid)
                    with self.assertRaises(explanations.RelationExplanationError):
                        self._explain()
                    path.write_bytes(original)
        self.generate.assert_not_called()
        self.assertEqual(self._cache_paths(), set())

    def test_original_is_required_even_after_a_successful_cached_explanation(self):
        self._explain()
        (self.papers / self.target["slug"] / "text.md").unlink()
        with self.assertRaises(explanations.RelationExplanationError):
            self._explain()
        self.generate.assert_called_once()

    def test_title_only_originals_are_not_content_evidence(self):
        (self.papers / self.source["slug"] / "text.md").write_text(self.source["title"], encoding="utf-8")
        with self.assertRaises(explanations.RelationExplanationError):
            self._explain()
        self.generate.assert_not_called()

    def test_unsafe_slug_and_symlinked_originals_are_rejected(self):
        for slug in ("../outside", "/absolute", "bad\\path", "bad\x00slug"):
            with self.subTest(slug=slug):
                with self.assertRaises(explanations.RelationExplanationError):
                    explanations.explain_pair({"slug": slug}, self.target)
        path = self.papers / self.source["slug"] / "text.md"
        outside = self.papers.parent / "outside.md"
        outside.write_text(self.texts[self.source["slug"]], encoding="utf-8")
        path.unlink()
        path.symlink_to(outside)
        with self.assertRaises(explanations.RelationExplanationError):
            self._explain()
        self.generate.assert_not_called()
        self.assertEqual(self._cache_paths(), set())

    def test_corrupted_cache_is_revalidated_instead_of_served_or_regenerated(self):
        self._explain()
        self.generate.reset_mock()
        (path,) = self._cache_paths()
        original = path.read_text(encoding="utf-8")
        invalid_quote = json.loads(original)
        invalid_quote["result"]["data"]["forward"]["evidence"]["source_quote"] = (
            "A fabricated quote inserted into an otherwise valid cached explanation."
        )
        for contents in ("{", json.dumps(invalid_quote, ensure_ascii=False)):
            with self.subTest(contents=contents):
                path.write_text(contents, encoding="utf-8")
                with self.assertRaises(explanations.RelationExplanationError):
                    self._explain()
                self.assertEqual(path.read_text(encoding="utf-8"), contents)
        self.generate.assert_not_called()


if __name__ == "__main__":
    unittest.main()
