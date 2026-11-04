"""Related-paper retrieval and independently generated connection explanations.

Guards the three defects found on 2026-08-31 while investigating why
``10911 Accelerating Scientific Research with Gemini in the Real-World`` did not
surface its own direct predecessor, ``044 ... Case Studies and Common
Techniques`` — a paper it literally cites:

  1. Retrieval was SPECTER2 cosine ONLY. SPECTER2 embeds the *contribution*, so
     a titled series whose domain moved (mathematics -> materials/biology wet
     lab) scatters: 044 sat at cosine rank 465/2929 while the candidate window
     is 5 (topic_modeling / paper-curio bridge) or 25 (extract_insights).
     Measured on 956 in-corpus citation pairs harvested from reference lists,
     dense+lexical RRF lifts recall@5 6.80% -> 8.89% and recall@25
     17.15% -> 23.01%.
  2. The fused candidate ranking feeds ``lib.related.build_connections`` in
     full rank order. The explanation model describes those retrieved pairs;
     it neither picks candidates nor replaces their rank with a model score.

And one latent bug fixed on the way: 38 papers in the live ai4s+scisci corpus
share an identical embedding with another paper (degenerate originality text),
which broke the legacy ``sims[1:top_k + 1]`` assumption that a row's argmax is
always the paper itself — 20 papers listed THEMSELVES as a related paper.

Run:
  PYTHONUTF8=1 /opt/homebrew/Caskroom/miniconda/base/envs/py312/bin/python \
      pipeline/tests/test_related_candidates.py
"""

import os
import sys
import unittest
from unittest.mock import call, patch

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import topic_modeling as TM  # noqa: E402
from lib import related  # noqa: E402


def _vec(*values):
    v = np.asarray(values, dtype=np.float32)
    return v / np.linalg.norm(v)


# A miniature stand-in for the real failure. P0 is the new paper; P1 is its
# direct predecessor (same title stem, shared author) but sits in a different
# embedding neighbourhood; P2..P5 are generic agentic-science papers that crowd
# P0 out in pure cosine space.
TARGET = "0100_Accelerating_Scientific_Research_with_Gemini_in_the_Real_World"
PREDECESSOR = "0044_Accelerating_Scientific_Research_with_Gemini_Case_Studies"

CORPUS = [
    {"slug": TARGET,
     "title": "Accelerating Scientific Research with Gemini in the Real-World",
     "authors": ["Samuel Schmidgall", "Tao Tu"],
     "vec": _vec(1.0, 0.0, 0.0)},
    {"slug": PREDECESSOR,
     "title": "Accelerating Scientific Research with Gemini: Case Studies and Common Techniques",
     "authors": ["David P. Woodruff", "Tao Tu"],
     "vec": _vec(0.0, 1.0, 0.0)},
    {"slug": "0201_SciAgents_Automating_Scientific_Discovery",
     "title": "SciAgents: Automating Scientific Discovery Through Bioinspired Multi-Agents",
     "authors": ["Alireza Ghafarollahi"],
     "vec": _vec(1.0, 0.0, 0.05)},
    {"slug": "0202_Prim_Principle_inspired_material_discovery",
     "title": "Prim: Principle-inspired material discovery through multi-agent design",
     "authors": ["Anon One"],
     "vec": _vec(1.0, 0.0, 0.10)},
    {"slug": "0203_Grounded_autonomous_research_pipeline",
     "title": "Grounded autonomous research: a fault-tolerant LLM pipeline",
     "authors": ["Anon Two"],
     "vec": _vec(1.0, 0.0, 0.15)},
    {"slug": "0204_General_Multimodal_Protein_Design",
     "title": "General Multimodal Protein Design Enables DNA-Encoding of Chemistry",
     "authors": ["Anon Three"],
     "vec": _vec(1.0, 0.0, 0.20)},
]

SLUGS = [p["slug"] for p in CORPUS]
EMB = np.asarray([p["vec"] for p in CORPUS], dtype=np.float32)
PAPERS = [{k: v for k, v in p.items() if k != "vec"} for p in CORPUS]


class DenseOnlyContractTests(unittest.TestCase):
    """papers=None must stay byte-for-byte the previous behaviour."""

    def test_dense_only_orders_by_cosine(self):
        got = TM.compute_related_candidates(EMB, SLUGS, top_k=3)
        norm = EMB / np.linalg.norm(EMB, axis=1, keepdims=True)
        for i, slug in enumerate(SLUGS):
            sims = sorted(
                ((float(norm[i] @ norm[j]), SLUGS[j])
                 for j in range(len(SLUGS)) if j != i),
                key=lambda x: -x[0],
            )
            self.assertEqual([s for _, s in sims[:3]],
                             [s for s, _ in got[slug]], slug)

    def test_reported_score_is_cosine(self):
        got = TM.compute_related_candidates(EMB, SLUGS, top_k=2, papers=PAPERS)
        norm = EMB / np.linalg.norm(EMB, axis=1, keepdims=True)
        for i, slug in enumerate(SLUGS):
            for target, score in got[slug]:
                j = SLUGS.index(target)
                self.assertAlmostEqual(score, float(norm[i] @ norm[j]), places=5)

    def test_top_k_larger_than_corpus_is_clamped(self):
        got = TM.compute_related_candidates(EMB, SLUGS, top_k=99, papers=PAPERS)
        for slug in SLUGS:
            self.assertEqual(len(got[slug]), len(SLUGS) - 1, slug)


class SelfExclusionTests(unittest.TestCase):
    """A paper is never its own related paper, even against an identical twin.

    38 live papers have a cosine-1.0 twin. The legacy slice dropped the twin as
    if it were the paper itself and kept the paper in its own candidate list.
    """

    def _twinned(self):
        emb = EMB.copy()
        emb[1] = emb[0]  # PREDECESSOR becomes a byte-identical twin of TARGET
        return emb

    def test_self_absent_from_own_candidates_dense(self):
        got = TM.compute_related_candidates(self._twinned(), SLUGS, top_k=3)
        for slug, cands in got.items():
            self.assertNotIn(slug, [c for c, _ in cands], slug)

    def test_self_absent_from_own_candidates_hybrid(self):
        got = TM.compute_related_candidates(self._twinned(), SLUGS, top_k=3,
                                            papers=PAPERS)
        for slug, cands in got.items():
            self.assertNotIn(slug, [c for c, _ in cands], slug)

    def test_identical_twin_is_kept_as_a_candidate(self):
        got = TM.compute_related_candidates(self._twinned(), SLUGS, top_k=1)
        self.assertEqual([c for c, _ in got[TARGET]], [PREDECESSOR])
        self.assertEqual([c for c, _ in got[PREDECESSOR]], [TARGET])


class HybridRecallTests(unittest.TestCase):

    def test_dense_only_loses_the_series_predecessor(self):
        got = TM.compute_related_candidates(EMB, SLUGS, top_k=3)
        self.assertNotIn(PREDECESSOR, [c for c, _ in got[TARGET]])

    def test_hybrid_recovers_the_series_predecessor(self):
        got = TM.compute_related_candidates(EMB, SLUGS, top_k=3, papers=PAPERS)
        self.assertIn(PREDECESSOR, [c for c, _ in got[TARGET]])

    def test_hybrid_keeps_the_nearest_dense_neighbour(self):
        """Lexical evidence supplements cosine, it does not evict it."""
        dense = TM.compute_related_candidates(EMB, SLUGS, top_k=3)
        hybrid = TM.compute_related_candidates(EMB, SLUGS, top_k=3, papers=PAPERS)
        nearest = dense[TARGET][0][0]
        self.assertIn(nearest, [c for c, _ in hybrid[TARGET]])

    def test_missing_metadata_falls_back_to_the_slug(self):
        """Papers absent from the index must not crash or poison the ranking."""
        partial = [p for p in PAPERS if p["slug"] != PREDECESSOR]
        got = TM.compute_related_candidates(EMB, SLUGS, top_k=3, papers=partial)
        # The slug still carries the title words, so the series link survives.
        self.assertIn(PREDECESSOR, [c for c, _ in got[TARGET]])


class ExplainedConnectionTests(unittest.TestCase):

    @staticmethod
    def _explanation(source, target):
        return {
            "relation": "alternative",
            "reason": ("두 논문은 과학 연구의 자동화를 다루지만, 첫 논문은 실험실의 실제 작업을 "
                       "평가하고 비교 논문은 사례 분석을 통해 도구 사용과 작업 분해의 차이를 설명합니다."),
            "model": "explanation-test-model",
            "evidence": {"source_quote": "The study evaluates research tasks in real laboratories.",
                         "target_quote": "The case studies describe tool use and task decomposition."},
            "reverse": {
                "relation": "alternative",
                "reason": ("사례 연구가 도구 사용과 과제 분해의 접근법을 제시한 반면, 비교 대상은 실제 "
                           "실험실 작업을 평가하므로 연구 자동화의 설계와 적용 조건을 서로 대조할 수 있습니다."),
                "evidence": {"source_quote": "The case studies describe tool use and task decomposition.",
                             "target_quote": "The study evaluates research tasks in real laboratories."},
            },
        }

    def test_build_connections_preserves_fused_candidate_order(self):
        candidates = TM.compute_related_candidates(EMB, SLUGS, top_k=5,
                                                   papers=PAPERS)
        with patch.object(related, "explain_pair", side_effect=self._explanation) as explain:
            got = related.build_connections({TARGET: candidates[TARGET]}, PAPERS,
                                            limit=3)
        self.assertEqual([link["slug"] for link in got[TARGET]],
                         [slug for slug, _score in candidates[TARGET][:3]])
        by_slug = {paper["slug"]: paper for paper in PAPERS}
        # Pairs are explained concurrently; the links above keep the fused order.
        self.assertCountEqual(explain.call_args_list, [
            call(by_slug[TARGET], by_slug[slug]) for slug, _ in candidates[TARGET][:3]
        ])

    def test_build_connections_keeps_explanation_and_embedding_evidence_separate(self):
        papers = [dict(p) for p in PAPERS]
        for paper in papers:
            paper["primary_category"] = "AI for Science"
        next(p for p in papers if p["slug"] == TARGET)["date"] = "2025-01-01"
        next(p for p in papers if p["slug"] == PREDECESSOR)["date"] = "2024-01-01"

        with patch.object(related, "explain_pair", side_effect=self._explanation) as explain:
            got = related.build_connections(
                {TARGET: [(PREDECESSOR, 0.75)]}, papers, limit=1)
        link = got[TARGET][0]
        expected = self._explanation(papers[0], papers[1])
        explain.assert_called_once_with(papers[0], papers[1])
        self.assertEqual(link["relation"], "alternative")
        self.assertEqual(link["basis"], "embedding")
        self.assertEqual(link["model"], "explanation-test-model")
        self.assertEqual(link["evidence"], {**expected["evidence"], "cosine": 0.75})
        self.assertEqual(link["reason"], expected["reason"])
        self.assertNotIn("코사인", link["reason"])



class PairDedupAndMissingTextTests(unittest.TestCase):
    def _papers(self):
        return [{"slug": s, "title": s} for s in ("001_A", "002_B", "003_C")]

    @staticmethod
    def _explanation(source, target):
        def side(a, b):
            return {"relation": "alternative", "reason": f"{a['slug']} 관점에서 {b['slug']}",
                    "evidence": {"source_quote": a["slug"], "target_quote": b["slug"]}}
        return {**side(source, target), "model": "m", "reverse": side(target, source)}

    def test_mutual_neighbours_cost_one_call_and_read_from_each_side(self):
        papers = self._papers()
        with patch.object(related, "explain_pair", side_effect=self._explanation) as explain:
            got = related.build_connections(
                {"001_A": [("002_B", 0.9)], "002_B": [("001_A", 0.9)]}, papers)
        explain.assert_called_once()
        self.assertEqual(got["001_A"][0]["reason"], "001_A 관점에서 002_B")
        self.assertEqual(got["002_B"][0]["reason"], "002_B 관점에서 001_A")
        self.assertEqual(got["002_B"][0]["reverse"]["reason"], "001_A 관점에서 002_B")

    def test_pair_without_source_text_is_skipped_not_templated(self):
        from lib.relation_explanations import MissingSourceText
        papers = self._papers()

        def explain(source, target):
            if "003_C" in (source["slug"], target["slug"]):
                raise MissingSourceText("missing or unreadable source text.md: 003_C")
            return self._explanation(source, target)

        with patch.object(related, "explain_pair", side_effect=explain):
            got = related.build_connections({"001_A": [("003_C", 0.95), ("002_B", 0.9)]}, papers)
        self.assertEqual([link["slug"] for link in got["001_A"]], ["002_B"])

    def test_pair_whose_explanation_stays_invalid_is_left_out(self):
        from lib.relation_explanations import UnexplainablePair
        papers = self._papers()

        def explain(source, target):
            if "003_C" in (source["slug"], target["slug"]):
                raise UnexplainablePair("forward relation contradicts publication chronology")
            return self._explanation(source, target)

        with patch.object(related, "explain_pair", side_effect=explain), patch("builtins.print"):
            got = related.build_connections({"001_A": [("003_C", 0.95), ("002_B", 0.9)]}, papers)
        self.assertEqual([link["slug"] for link in got["001_A"]], ["002_B"])

    def test_provider_failure_still_raises_after_all_pairs_ran(self):
        papers = self._papers()
        calls = []

        def explain(source, target):
            calls.append(target["slug"])
            if target["slug"] == "002_B":
                raise RuntimeError("provider down")
            return self._explanation(source, target)

        with patch.object(related, "explain_pair", side_effect=explain):
            with self.assertRaisesRegex(RuntimeError, "provider down"):
                related.build_connections({"001_A": [("002_B", 0.9), ("003_C", 0.8)]}, papers)
        self.assertCountEqual(calls, ["002_B", "003_C"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
