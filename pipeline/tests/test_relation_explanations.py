"""Pair explanations: summary comparison, grounded-cache reuse, validation."""
from __future__ import annotations

import copy
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

from lib import relation_explanations as explanations
from lib import text_providers

MODEL = text_providers.DEFAULT_MODELS["anthropic"]
FORWARD_REASON = (
    "두 논문은 후보 탐색의 평가 비용을 다룹니다. Parallel search는 후보를 병렬로 평가하고 "
    "Sequential search는 한 번에 하나씩 평가하므로 같은 과제에서 비용과 정확도를 비교할 수 있습니다."
)
REVERSE_REASON = (
    "Sequential search의 순차 탐색은 Parallel search에서 병렬 후보 평가로 바뀝니다. "
    "두 방법은 같은 과제의 비용과 정확도를 측정하지만 후보를 평가하는 순서가 다릅니다."
)
SOURCE_QUOTE = "We extend the sequential search baseline with parallel candidate evaluation."
TARGET_QUOTE = "Our sequential search baseline evaluates one candidate at each iteration."


class RelationExplanationTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        self.papers, self.cache = root / "papers", root / "cache"
        self.source = {"slug": "001_Parallel_Search", "title": "Parallel candidate evaluation",
                       "date": "2025", "authors": ["Ada Lovelace"],
                       "essence": "후보를 병렬로 평가해 탐색 비용을 줄이는 방법을 제안한다.",
                       "classifications": {"ai4s": {"primary_category": "Search",
                                                    "sub_category": "Parallel Search"}}}
        self.target = {"slug": "002_Sequential_Search", "title": "Sequential search baseline",
                       "date": "2023", "authors": ["Grace Hopper"],
                       "essence": "후보를 하나씩 평가하는 순차 탐색 기준선을 제시한다."}
        self.texts = {
            self.source["slug"]: "# Parallel search\n\n" + SOURCE_QUOTE + "\nWe measure cost and accuracy.\n",
            self.target["slug"]: "# Sequential search\n\n" + TARGET_QUOTE + "\nWe report the evaluation cost.\n",
        }
        for slug, text in self.texts.items():
            directory = self.papers / slug
            directory.mkdir(parents=True)
            (directory / "text.md").write_text(text, encoding="utf-8")
            (directory / "originality.md").write_text(f"Originality of {slug}: a search method.", encoding="utf-8")
        paths = patch.multiple(explanations, PAPERS_DIR=self.papers, CACHE_DIR=self.cache)
        paths.start()
        self.addCleanup(paths.stop)
        self.payload = {"forward_relation": "alternative", "forward_reason": FORWARD_REASON,
                        "reverse_relation": "alternative", "reverse_reason": REVERSE_REASON}
        provider = patch.object(text_providers, "generate_structured", side_effect=self._generate)
        self.generate = provider.start()
        self.addCleanup(provider.stop)

    def _generate(self, provider, model, *_args, **_kwargs):
        return {"data": copy.deepcopy(self.payload), "provider": provider, "model": model}

    def _explain(self):
        return explanations.explain_pair(self.source, self.target)

    def _cache_paths(self):
        return set(self.cache.glob("*.json"))

    def _assert_invalid(self, payload):
        response = {"data": payload, "provider": "anthropic", "model": MODEL}
        with patch.object(text_providers, "generate_structured", return_value=response) as generate:
            with self.assertRaises(explanations.RelationExplanationError):
                self._explain()
        self.assertEqual(generate.call_count, 2)
        self.assertEqual(self._cache_paths(), set())

    # --- summary comparison -------------------------------------------------

    def test_prompt_carries_summaries_and_fields_not_original_text(self):
        result = self._explain()
        prompt = json.loads(self.generate.call_args.args[3])
        sent = json.dumps(prompt, ensure_ascii=False)
        self.assertNotIn(SOURCE_QUOTE, sent)
        self.assertNotIn(TARGET_QUOTE, sent)
        source = prompt["source"]
        self.assertEqual(source["essence"], self.source["essence"])
        self.assertIn("Originality of 001_Parallel_Search", source["originality"])
        self.assertEqual(source["fields"], [{"topic": "ai4s", "category": "Search",
                                             "sub_category": "Parallel Search"}])
        self.assertIn("연구 분야", self.generate.call_args.args[2])
        self.assertEqual(self.generate.call_args.kwargs["max_output_tokens"],
                         explanations.MAX_OUTPUT_TOKENS)
        self.assertEqual(result["reason"], FORWARD_REASON)
        self.assertEqual(result["reverse"]["reason"], REVERSE_REASON)
        self.assertEqual(result["evidence"]["prompt_version"], explanations.PROMPT_VERSION)

    def test_summary_prompt_is_small(self):
        self.source["essence"] = "가" * 400
        (self.papers / self.source["slug"] / "originality.md").write_text("x" * 50_000)
        self._explain()
        prompt = self.generate.call_args.args[3]
        self.assertLess(len(prompt), 3_000)

    def test_result_is_cached_and_reverse_request_reuses_it(self):
        first = self._explain()
        again = explanations.explain_pair(self.target, self.source)
        self.assertEqual(self.generate.call_count, 1)
        self.assertEqual(again["reason"], first["reverse"]["reason"])
        self.assertEqual(again["reverse"]["reason"], first["reason"])
        (cache,) = self._cache_paths()
        stored = json.loads(cache.read_text(encoding="utf-8"))
        call = self.generate.call_args
        self.assertEqual(stored["identity"]["prompt_sha256"], hashlib.sha256(
            (call.args[2] + "\n" + call.args[3]).encode("utf-8")).hexdigest())

    def test_changed_summary_is_a_new_request(self):
        self._explain()
        self.source["essence"] = "후보 평가를 분산 처리해 비용을 줄이는 다른 방법을 제안한다."
        self._explain()
        self.assertEqual(self.generate.call_count, 2)

    def test_invalid_payload_is_repaired_once_then_cached(self):
        bad = self._generate("anthropic", MODEL)
        bad["data"]["forward_reason"] = "SPECTER2 임베딩 공간에서 가까운 논문입니다 (코사인 유사도 0.95)."
        good = self._generate("anthropic", MODEL)
        with patch.object(text_providers, "generate_structured", side_effect=[bad, good]) as generate:
            result = self._explain()
        first, repair = generate.call_args_list
        repaired = json.loads(repair.args[3])
        self.assertEqual(repaired["previous_payload"], bad["data"])
        self.assertIn("validation_error", repaired)
        self.assertEqual(result["reason"], FORWARD_REASON)
        self.assertEqual(len(self._cache_paths()), 1)

    def test_adapter_unwraps_a_single_unknown_wrapper_key(self):
        # Observed live: tool input {"parameter name": {"forward": ..., "reverse": ...}}.
        schema = explanations.EXPLANATION_SCHEMA
        fixed = text_providers._decode_stringified_containers({"parameter name": self.payload}, schema)
        text_providers._validate_schema_shape(fixed, schema)
        self.assertEqual(fixed, self.payload)
        partial = {"wrapper": {"forward_reason": FORWARD_REASON}}
        self.assertEqual(text_providers._decode_stringified_containers(partial, schema), partial)
        known = {"forward_reason": self.payload}
        self.assertEqual(text_providers._decode_stringified_containers(known, schema), known)

    def test_retrieval_talk_english_short_and_repeated_reasons_are_rejected(self):
        for forward in ("SPECTER2 임베딩에서 가까운 후보 탐색 연구로, 탐색 비용과 정확도를 함께 비교할 수 있습니다.",
                        "BM25 순위가 높은 후보 탐색 연구로, 탐색 비용과 정확도를 함께 비교할 수 있습니다.",
                        "Both papers study candidate search cost and accuracy on the same tasks in detail.",
                        "짧음"):
            with self.subTest(forward=forward):
                payload = copy.deepcopy(self.payload)
                payload["forward_reason"] = forward
                self._assert_invalid(payload)
        payload = copy.deepcopy(self.payload)
        payload["reverse_reason"] = payload["forward_reason"]
        self._assert_invalid(payload)

    def test_relation_must_respect_publication_order(self):
        payload = copy.deepcopy(self.payload)
        # Canonical order puts 001 (2025) first: the 2023 target cannot extend it.
        payload["forward_relation"] = "extension"
        self._assert_invalid(payload)

    def test_schema_violation_from_provider_gets_one_repair(self):
        good = self._generate("anthropic", MODEL)
        with patch.object(text_providers, "generate_structured",
                          side_effect=[text_providers.ProviderSchemaError("missing field"), good]) as generate:
            result = self._explain()
        self.assertEqual(generate.call_count, 2)
        self.assertIn("validation_error", json.loads(generate.call_args.args[3]))
        self.assertEqual(result["reason"], FORWARD_REASON)
        with patch.object(text_providers, "generate_structured",
                          side_effect=text_providers.ProviderSchemaError("missing field")) as generate:
            self.source["essence"] = "다른 요약으로 바꿔 캐시를 피하는 후보 탐색 방법을 제안한다."
            with self.assertRaises(text_providers.ProviderSchemaError):
                self._explain()
        self.assertEqual(generate.call_count, 2)

    def test_provider_failure_propagates_without_cache(self):
        with patch.object(text_providers, "generate_structured",
                          side_effect=text_providers.ProviderResponseError("down")):
            with self.assertRaises(text_providers.ProviderResponseError):
                self._explain()
        self.assertEqual(self._cache_paths(), set())

    def test_wrong_model_provenance_is_rejected(self):
        with patch.object(text_providers, "generate_structured",
                          return_value={"data": self.payload, "provider": "anthropic", "model": "other"}):
            with self.assertRaises(explanations.RelationExplanationError):
                self._explain()

    def test_paper_without_any_summary_is_missing_source(self):
        self.target["essence"] = ""
        (self.papers / self.target["slug"] / "originality.md").unlink()
        with self.assertRaises(explanations.MissingSourceText):
            self._explain()
        self.generate.assert_not_called()

    def test_unsafe_slug_and_symlinked_originality_are_rejected(self):
        with self.assertRaises(explanations.RelationExplanationError):
            explanations.explain_pair({**self.source, "slug": "../escape"}, self.target)
        link = self.papers / self.source["slug"] / "originality.md"
        link.unlink()
        link.symlink_to(self.papers / self.target["slug"] / "originality.md")
        with self.assertRaises(explanations.RelationExplanationError):
            self._explain()

    def test_corrupted_cache_is_an_error_not_a_new_request(self):
        self._explain()
        (cache,) = self._cache_paths()
        cache.write_text("{not json", encoding="utf-8")
        with self.assertRaises(explanations.RelationExplanationError):
            self._explain()
        self.assertEqual(self.generate.call_count, 1)

    # --- grounded (v5) cache reuse -----------------------------------------

    def _seed_grounded(self, *, quote_ok=True):
        """Write a cache entry exactly as paper-comparison-v5 stored it."""
        left = explanations._source(self.source)
        right = explanations._source(self.target)
        if left["slug"] > right["slug"]:
            left, right = right, left
        context = {
            "source": {k: left[k] for k in ("slug", "title", "date", "authors", "fields", "excerpts")},
            "target": {k: right[k] for k in ("slug", "title", "date", "authors", "fields", "excerpts")},
        }
        prompt = json.dumps(context, ensure_ascii=False)
        identity = {"source_slug": left["slug"], "target_slug": right["slug"],
                    "source_sha256": left["sha256"], "target_sha256": right["sha256"],
                    "provider": "anthropic", "model": MODEL,
                    "prompt_version": explanations.GROUNDED_PROMPT_VERSION,
                    "prompt_sha256": hashlib.sha256(
                        (explanations.GROUNDED_SYSTEM_PROMPT + "\n" + prompt).encode("utf-8")).hexdigest()}
        quote = SOURCE_QUOTE if quote_ok else "This sentence does not appear in either original paper text."
        data = {
            "forward": {"relation": "alternative", "reason": "근거 기반 정방향 설명입니다. " + FORWARD_REASON,
                        "evidence": {"source_quote": quote, "target_quote": TARGET_QUOTE}},
            "reverse": {"relation": "alternative", "reason": "근거 기반 역방향 설명입니다. " + REVERSE_REASON,
                        "evidence": {"source_quote": TARGET_QUOTE, "target_quote": SOURCE_QUOTE}},
        }
        key = hashlib.sha256(json.dumps(identity, sort_keys=True).encode("utf-8")).hexdigest()
        self.cache.mkdir(parents=True, exist_ok=True)
        (self.cache / f"{key}.json").write_text(json.dumps(
            {"identity": identity, "result": {"data": data, "provider": "anthropic", "model": MODEL}},
            ensure_ascii=False), encoding="utf-8")

    def test_existing_grounded_explanation_is_reused_without_a_call(self):
        self._seed_grounded()
        result = self._explain()
        self.generate.assert_not_called()
        self.assertTrue(result["reason"].startswith("근거 기반 정방향"))
        self.assertEqual(result["evidence"]["source_quote"], SOURCE_QUOTE)
        self.assertEqual(result["evidence"]["prompt_version"], explanations.GROUNDED_PROMPT_VERSION)
        reverse = explanations.explain_pair(self.target, self.source)
        self.assertTrue(reverse["reason"].startswith("근거 기반 역방향"))
        self.generate.assert_not_called()

    def test_grounded_entry_for_changed_text_is_not_reused(self):
        self._seed_grounded()
        (self.papers / self.source["slug"] / "text.md").write_text(
            self.texts[self.source["slug"]] + "\nA revised paragraph.\n", encoding="utf-8")
        result = self._explain()
        self.generate.assert_called_once()
        self.assertEqual(result["evidence"]["prompt_version"], explanations.PROMPT_VERSION)

    def test_invalid_grounded_entry_is_an_error(self):
        self._seed_grounded(quote_ok=False)
        with self.assertRaises(explanations.RelationExplanationError):
            self._explain()
        self.generate.assert_not_called()

    def test_paper_without_text_uses_summaries(self):
        (self.papers / self.target["slug"] / "text.md").unlink()
        result = self._explain()
        self.generate.assert_called_once()
        self.assertEqual(result["reason"], FORWARD_REASON)


if __name__ == "__main__":
    unittest.main()
