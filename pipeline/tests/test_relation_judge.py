"""Focused tests for content-grounded connection judging (no network)."""
import os
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE))
from lib import relation_judge as judge  # noqa: E402


class FakeMessages:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        response = self.responses.pop(0)
        if isinstance(response, Exception):
            raise response
        return response


class FakeClient:
    def __init__(self, responses):
        self.messages = FakeMessages(responses)


def response(judgments):
    return SimpleNamespace(content=[SimpleNamespace(type="tool_use", name="judge_relations",
                                                     input={"judgments": judgments})],
                           usage=SimpleNamespace(input_tokens=100, output_tokens=50))


def papers():
    return [{"slug": "a", "title": "Source", "year": "2024", "essence": "분자 설계 방법을 제안한다."},
            {"slug": "b", "title": "Target", "year": "2023", "essence": "분자 설계 방법을 검증한다."}]


def connections(source="a", target="b"):
    return {source: [{"slug": target, "relation": "alternative",
                      "reason": judge.METADATA_REASON, "basis": "metadata", "model": "",
                      "evidence": {"cosine": .92, "same_category": True}}]}


def judgment(target="C1", relation="this_builds_on_candidate"):
    return {"target": target, "relation": relation,
            "reason": "Source는 Target의 분자 설계 방법을 가져와 검증 범위를 넓힌다."}


class RelationJudgeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.env = patch.dict(os.environ, {"RELATION_JUDGE": "on", "RELATION_JUDGE_MAX_USD": "5"}, clear=False)
        self.env.start()
        self.addCleanup(self.env.stop)

    def test_paper_profile_extracts_review_content(self):
        root = Path(self.temp.name) / "papers"
        review = root / "a" / "review.md"
        review.parent.mkdir(parents=True)
        review.write_text("# 검증 논문\n\n## Essence\n![Figure](x.png)\n*Figure 1. ignored*\n핵심 발견입니다.\n\n## Motivation\n- **Gap**: 기존 방법은 검증이 없다.\n- **Approach**: 새 검증기를 제안한다.\n\n## Achievement\n1. **성과**: 정확도를 높였다.\n2. 기타\n", encoding="utf-8")
        with patch.object(judge, "PAPERS_DIR", root):
            profile = judge.paper_profile("a", papers()[0])
        self.assertIn("검증 논문", profile)
        self.assertIn("기존 방법은 검증이 없다", profile)
        self.assertIn("새 검증기를 제안한다", profile)
        self.assertNotIn("Figure", profile)

    def test_cache_reuses_pair_from_opposite_direction(self):
        client = FakeClient([response([judgment()])])
        first = judge.judge_connections(connections(), papers(), topic="demo", cache_dir=self.temp.name, client=client, log=lambda _: None)
        self.assertEqual(first["a"][0]["basis"], "model")
        second = judge.judge_connections(connections("b", "a"), papers(), topic="demo", cache_dir=self.temp.name, client=client, log=lambda _: None)
        self.assertEqual(len(client.messages.calls), 1)
        self.assertEqual(second["b"][0]["relation"], "extension")
        self.assertEqual(second["b"][0]["reason"], judgment()["reason"])

    def test_unrelated_drops_link_and_prompt_excludes_metadata(self):
        client = FakeClient([response([judgment(relation="unrelated")])])
        result = judge.judge_connections(connections(), papers(), topic="demo", cache_dir=self.temp.name, client=client, log=lambda _: None)
        self.assertEqual(result["a"], [])
        prompt = client.messages.calls[0]["messages"][0]["content"].lower()
        self.assertNotIn("cosine", prompt)
        self.assertNotIn("category", prompt)
        self.assertNotIn("0.92", prompt)

    def test_parse_failure_keeps_metadata_entry(self):
        client = FakeClient([SimpleNamespace(content=[], usage=SimpleNamespace(input_tokens=1, output_tokens=1))])
        result = judge.judge_connections(connections(), papers(), topic="demo", cache_dir=self.temp.name, client=client, log=lambda _: None)
        self.assertEqual(result, connections())

    def test_budget_cap_stops_calls_and_keeps_metadata(self):
        with patch.dict(os.environ, {"RELATION_JUDGE_MAX_USD": "0"}):
            client = FakeClient([])
            result = judge.judge_connections(connections(), papers(), topic="demo", cache_dir=self.temp.name, client=client, log=lambda _: None)
        self.assertEqual(client.messages.calls, [])
        self.assertEqual(result, connections())


    def test_mutual_candidates_are_judged_once_per_pair(self):
        both = {**connections("a", "b"), **connections("b", "a")}
        client = FakeClient([response([judgment()])])
        result = judge.judge_connections(both, papers(), topic="demo", cache_dir=self.temp.name,
                                         client=client, log=lambda _: None)
        self.assertEqual(len(client.messages.calls), 1)
        self.assertEqual(result["a"][0]["reason"], judgment()["reason"])
        self.assertEqual(result["b"][0]["reason"], judgment()["reason"])
        self.assertEqual(result["b"][0]["relation"], "extension")

    def test_budget_counts_korean_prompt_near_one_token_per_char(self):
        prompt = judge._prompt("a", "핵심: " + "분자" * 400, [("b", "핵심: " + "설계" * 400)])
        self.assertGreaterEqual(judge._estimate_input_tokens(prompt), len(prompt))
        # A cap below the one-call worst case must refuse the call outright.
        worst = judge._cost(judge._estimate_input_tokens(prompt), 260, "claude-haiku-4-5")
        with patch.dict(os.environ, {"RELATION_JUDGE_MAX_USD": str(worst / 2)}), \
             patch.object(judge, "paper_profile", side_effect=lambda slug, _p: "핵심: " + ("분자" if slug == "a" else "설계") * 400):
            client = FakeClient([])
            result = judge.judge_connections(connections(), papers(), topic="demo",
                                             cache_dir=self.temp.name, client=client, log=lambda _: None)
        self.assertEqual(client.messages.calls, [])
        self.assertEqual(result, connections())

    def test_call_exception_keeps_metadata_and_is_reported(self):
        client = FakeClient([RuntimeError("rate limited")])
        logs = []
        result = judge.judge_connections(connections(), papers(), topic="demo", cache_dir=self.temp.name,
                                         client=client, log=logs.append)
        self.assertEqual(result, connections())
        self.assertTrue(any("rate limited" in line for line in logs))

    def test_reverse_relation_is_derived_not_trusted_from_model(self):
        contradictory = dict(judgment(relation="this_builds_on_candidate"), reverse_relation="foundation")
        client = FakeClient([response([contradictory])])
        both = {**connections("a", "b"), **connections("b", "a")}
        result = judge.judge_connections(both, papers(), topic="demo", cache_dir=self.temp.name,
                                         client=client, log=lambda _: None)
        # The model's own reverse_relation ("foundation") is ignored: a builds on
        # b, so from b's page a is an extension.
        self.assertEqual(result["a"][0]["relation"], "foundation")
        self.assertEqual(result["b"][0]["relation"], "extension")

    def test_reverse_map_matches_connection_view(self):
        from lib.connections import REVERSE_RELATION
        for relation, reverse in judge.REVERSE.items():
            self.assertEqual(REVERSE_RELATION[relation], reverse)

    def test_prompt_defines_direction_and_bans_internal_terms(self):
        prompt = judge._prompt("a", "제목: A", [("b", "제목: B")])
        for key in judge.MODEL_LINKS:
            self.assertIn(key, prompt)
        self.assertIn("방향에 주의", prompt)
        self.assertIn("금지", prompt)
        self.assertIn("unrelated", prompt)

    def test_truncated_response_reports_stop_reason(self):
        truncated = SimpleNamespace(content=[], stop_reason="max_tokens",
                                    usage=SimpleNamespace(input_tokens=1, output_tokens=1))
        logs = []
        result = judge.judge_connections(connections(), papers(), topic="demo", cache_dir=self.temp.name,
                                         client=FakeClient([truncated]), log=logs.append)
        self.assertEqual(result, connections())
        self.assertTrue(any("max_tokens" in line for line in logs))

    def test_candidate_keys_survive_model_shortening(self):
        long_target = "535_MetaOpenFOAM_an_LLM-based_multi-agent_framework_for_CFD"
        catalog = papers() + [{"slug": long_target, "title": "MetaOpenFOAM", "year": "2024",
                               "essence": "CFD 자동화 에이전트."}]
        conns = {"a": [dict(connections()["a"][0]),
                       dict(connections()["a"][0], slug=long_target)]}
        second = dict(judgment(target="C2", relation="alternative"))
        client = FakeClient([response([judgment(target="C1"), second])])
        result = judge.judge_connections(conns, catalog, topic="demo", cache_dir=self.temp.name,
                                         client=client, log=lambda _: None)
        prompt = client.messages.calls[0]["messages"][0]["content"]
        self.assertNotIn(long_target, prompt)
        self.assertEqual([link["basis"] for link in result["a"]], ["model", "model"])
        self.assertEqual(result["a"][1]["slug"], long_target)

    def test_short_name_uses_title_prefix(self):
        self.assertEqual(judge.short_name("제목: Safe-SDL:Establishing Safety Boundaries"), "Safe-SDL")
        self.assertEqual(judge.short_name("제목: Talking to instruments: device-integration standards"),
                         "Talking to instruments")
        self.assertEqual(judge.short_name("제목: A B C D E F G"), "A B C D E…")

    def test_year_guard_rejects_impossible_lineage(self):
        # b (2023) is earlier than a (2024): b cannot build on a.
        client = FakeClient([response([judgment(relation="candidate_builds_on_this")])])
        result = judge.judge_connections(connections(), papers(), topic="demo", cache_dir=self.temp.name,
                                         client=client, log=lambda _: None)
        self.assertEqual(result["a"][0]["relation"], "alternative")
        self.assertEqual(judge._guard_direction("foundation", 2024, 2025), "alternative")
        self.assertEqual(judge._guard_direction("foundation", 2024, 2023), "foundation")
        self.assertEqual(judge._guard_direction("extension", 2024, 2024), "extension")

    def test_sanitizer_rewrites_only_paper_references(self):
        names = {1: "NIMO-IvoryOS", 3: "Safe-SDL"}
        text = judge._sanitize("기준 논문과 후보 논문 C3 모두 안전을 다루며 C1과 다르다.",
                               "Talking", "Safe-SDL", names)
        self.assertEqual(text, "Talking과 Safe-SDL 모두 안전을 다루며 NIMO-IvoryOS과 다르다.")
        self.assertEqual(judge._sanitize("이 논문은 표준을 정리한다.", "Talking", "X", names),
                         "Talking은 표준을 정리한다.")

    def test_sanitizer_keeps_ordinary_korean_and_formulae(self):
        names = {3: "Safe-SDL"}
        for text in ("12,000명 교수자를 대상으로 추적했다.", "후보 물질을 선별한다.",
                     "C3H8 연소 반응을 다룬다."):
            self.assertEqual(judge._sanitize(text, "A", "B", names), text)

    def test_pair_cache_is_shared_across_topics(self):
        self.assertEqual(judge.pair_cache_dir().name, ".llm_cache")
        self.assertNotIn("ai4s", str(judge.pair_cache_dir()))

    def test_sanitizer_treats_names_as_literal_text(self):
        self.assertEqual(judge._sanitize("기준 논문은 빠르다.", r"\lambda-Net", "B", {}),
                         r"\lambda-Net은 빠르다.")
        self.assertEqual(judge._sanitize("이 논문은 C1과 다르다.", r"\mathrm{X}", "B", {1: r"\beta-VAE"}),
                         r"\mathrm{X}은 \beta-VAE과 다르다.")

    def test_judgments_serialised_as_json_string_are_accepted(self):
        import json as _json
        raw = SimpleNamespace(content=[SimpleNamespace(type="tool_use", name="judge_relations",
                                                        input={"judgments": _json.dumps([judgment()])})],
                              usage=SimpleNamespace(input_tokens=10, output_tokens=5))
        result = judge.judge_connections(connections(), papers(), topic="demo", cache_dir=self.temp.name,
                                         client=FakeClient([raw]), log=lambda _: None)
        self.assertEqual(result["a"][0]["basis"], "model")

    def test_failed_call_is_retried_once(self):
        client = FakeClient([RuntimeError("transient"), response([judgment()])])
        result = judge.judge_connections(connections(), papers(), topic="demo", cache_dir=self.temp.name,
                                         client=client, log=lambda _: None)
        self.assertEqual(len(client.messages.calls), 2)
        self.assertEqual(result["a"][0]["basis"], "model")

if __name__ == "__main__":
    unittest.main()
