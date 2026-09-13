"""Related-paper candidate retrieval and deterministic connection building.

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
     full rank order. Its relation, Korean reason, and evidence are derived
     from recorded metadata, never an LLM judge.

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


class DeterministicConnectionTests(unittest.TestCase):

    def test_build_connections_preserves_fused_candidate_order(self):
        candidates = TM.compute_related_candidates(EMB, SLUGS, top_k=5,
                                                   papers=PAPERS)
        got = related.build_connections({TARGET: candidates[TARGET]}, PAPERS,
                                        limit=5)
        self.assertEqual([link["slug"] for link in got[TARGET]],
                         [slug for slug, _score in candidates[TARGET]])

    def test_build_connections_uses_metadata_backed_relation_and_evidence(self):
        papers = [dict(p) for p in PAPERS]
        for paper in papers:
            paper["primary_category"] = "AI for Science"
        next(p for p in papers if p["slug"] == TARGET)["date"] = "2025-01-01"
        next(p for p in papers if p["slug"] == PREDECESSOR)["date"] = "2024-01-01"

        got = related.build_connections(
            {TARGET: [(PREDECESSOR, 0.75)]}, papers, limit=1)
        link = got[TARGET][0]
        self.assertEqual(link["relation"], "foundation")
        self.assertEqual(link["evidence"]["shared_authors"], ["tu"])
        self.assertTrue(link["evidence"]["same_category"])
        self.assertIn("SPECTER2 임베딩 유사도 0.75", link["reason"])
        self.assertIn("1년 앞선 연구", link["reason"])

if __name__ == "__main__":
    unittest.main(verbosity=2)
