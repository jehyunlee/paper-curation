"""Regression tests for provenance-aware consumer connection views."""
from __future__ import annotations

import os
import sys
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

PIPELINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PIPELINE not in sys.path:
    sys.path.insert(0, PIPELINE)

from lib.connections import (  # noqa: E402
    filter_for_topic,
    make_bidirectional_deduped,
    merge_to_global,
)
from lib.related import METADATA_REASON  # noqa: E402
import sync_paper_connections as sync  # noqa: E402


class BidirectionalConnectionTests(unittest.TestCase):
    def test_reverse_uses_explicit_target_perspective_reason(self):
        got = make_bidirectional_deduped({
            "A": [{"slug": "B", "relation": "foundation", "reason": "A의 근거 B",
                   "reverse_relation": "extension", "reverse_reason": "B의 확장 A",
                   "basis": "model", "model": "judge-v1", "evidence": {"cosine": .8}}]
        })
        reverse = got["B"][0]
        self.assertEqual((reverse["relation"], reverse["reason"]),
                         ("extension", "B의 확장 A"))
        self.assertEqual(reverse["model"], "judge-v1")

    def test_model_reason_wins_over_metadata_for_same_relation(self):
        got = make_bidirectional_deduped({
            "A": [
                {"slug": "B", "relation": "alternative", "reason": METADATA_REASON,
                 "basis": "metadata", "model": "", "evidence": {"cosine": .8}},
                {"slug": "B", "relation": "alternative", "reason": "내용상 다른 접근입니다.",
                 "basis": "model", "model": "judge-v1", "evidence": {"cosine": .7}},
            ]
        })
        self.assertEqual(got["A"][0]["reason"], "내용상 다른 접근입니다.")
        self.assertEqual(got["A"][0]["basis"], "model")

    def test_provenance_survives_merge_and_filter(self):
        new = {"A": [{"slug": "B", "relation": "alternative", "reason": METADATA_REASON,
                      "basis": "metadata", "model": "", "evidence": {"cosine": .8}}]}
        with patch("lib.connections.load_global_connections", return_value={}), \
             patch("lib.connections.save_global_connections"):
            merged = merge_to_global(new, source_topic="demo")
        view = make_bidirectional_deduped(merged)
        filtered = filter_for_topic(view, ["A"])
        item = filtered["A"][0]
        self.assertEqual(item["basis"], "metadata")
        self.assertEqual(item["model"], "")
        self.assertEqual(item["evidence"], {"cosine": .8})
        self.assertEqual(item["reasons"][0]["basis"], "metadata")
        self.assertEqual(item["reasons"][0]["evidence"], {"cosine": .8})
        self.assertNotIn("source_topic", item)

    def test_related_normalizes_to_alternative(self):
        got = make_bidirectional_deduped({
            "A": [{"slug": "B", "relation": "related", "reason": "기존 항목"}]
        })
        self.assertEqual(got["A"][0]["relation"], "alternative")
        self.assertEqual(got["B"][0]["relation"], "alternative")

    def test_metadata_reason_has_no_category_or_cosine(self):
        self.assertNotIn("카테고리", METADATA_REASON)
        self.assertNotRegex(METADATA_REASON, r"\d+\.\d+")

    def test_db_import_claim_models_reflect_entry_provenance(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "_paper_connections.json"
            with path.open("w", encoding="utf-8") as handle:
                json.dump({
                    "A": [
                        {"slug": "B", "relation": "alternative",
                         "reason": METADATA_REASON, "basis": "metadata", "model": ""},
                        {"slug": "C", "relation": "related", "reason": "이전 항목"},
                        {"slug": "D", "relation": "counterpoint", "reason": "판단",
                         "basis": "model", "model": "judge-v1"},
                    ]
                }, handle, ensure_ascii=False)
            topic_path = Path(tmp) / "demo" / "_paper_connections.json"
            topic_path.parent.mkdir()
            topic_path.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
            with patch.object(sync, "topic_files", return_value=[topic_path]):
                claims, _ = sync.load_json_connections()
        self.assertEqual(claims[("A", "B", "alternative")]["model"], "none:metadata")
        self.assertEqual(claims[("A", "C", "alternative")]["model"], "legacy:unknown")
        self.assertEqual(claims[("A", "D", "counterpoint")]["model"], "judge-v1")



class ModelPrecedenceTests(unittest.TestCase):
    def test_model_judgement_supersedes_legacy_claims_for_the_pair(self):
        from lib.connections import make_bidirectional_deduped
        view = make_bidirectional_deduped({
            "a": [{"slug": "b", "relation": "foundation", "basis": "model",
                   "model": "m", "reason": "A와 B는 같은 문제를 다룬다."}],
            "b": [{"slug": "a", "relation": "counterpoint",
                   "reason": "예전 판단: B는 A를 반박한다."}],
        })
        reasons = view["a"][0]["reasons"]
        self.assertEqual([r["basis"] for r in reasons], ["model"])
        self.assertEqual(view["b"][0]["relation"], "extension")

    def test_retired_template_reason_is_shown_as_honest_fallback(self):
        from lib.connections import make_bidirectional_deduped
        from lib.related import METADATA_REASON
        view = make_bidirectional_deduped({
            "a": [{"slug": "b", "relation": "foundation",
                   "reason": "SPECTER2 임베딩 유사도 0.92 · 공저자 1명 공유(Zhang)."}],
        })
        item = view["a"][0]
        self.assertEqual(item["reason"], METADATA_REASON)
        self.assertEqual(item["relation"], "alternative")
        self.assertEqual(item["basis"], "metadata")

    def test_legacy_model_written_reason_is_kept_without_a_new_judgement(self):
        from lib.connections import make_bidirectional_deduped
        view = make_bidirectional_deduped({
            "a": [{"slug": "b", "relation": "alternative",
                   "reason": "같은 문제를 다른 방법으로 푼다."}],
        })
        self.assertEqual(view["a"][0]["reason"], "같은 문제를 다른 방법으로 푼다.")

class ProcessedEmptyTests(unittest.TestCase):
    def test_source_with_no_related_paper_stays_as_empty_list(self):
        from lib.connections import make_bidirectional_deduped
        view = make_bidirectional_deduped({"a": [], "b": [{"slug": "c", "relation": "alternative",
                                                          "basis": "model", "reason": "B와 C."}]})
        self.assertEqual(view["a"], [])
        self.assertEqual(view["b"][0]["slug"], "c")
        self.assertNotIn("d", view)

if __name__ == "__main__":
    unittest.main(verbosity=2)
