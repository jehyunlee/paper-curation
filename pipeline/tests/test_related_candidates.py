"""Related-paper candidate retrieval + the prompt that consumes it.

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
  2. ``_build_prompt`` truncated to ``cands[:10]``, so 15 of the 25 candidates
     extract_insights computes for recall were cached, diffed, then silently
     dropped before the model ever saw them.
  3. Candidates were rendered as a bare slug number plus a cosine score with no
     title, so the judge invented both the relation and the Korean reason for a
     paper it could not identify.

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


class _Response:
    def __init__(self, text):
        self.content = [type("Block", (), {"text": text})()]


class _RecordingClient:
    """Anthropic-shaped stub that records prompts and answers with no links."""

    def __init__(self):
        self.prompts = []

    def with_options(self, **_kwargs):
        return self

    @property
    def messages(self):
        return self

    def create(self, **kwargs):
        self.prompts.append(kwargs["messages"][0]["content"])
        return _Response("{}")


class PromptContentTests(unittest.TestCase):

    def _prompt_for(self, top_k):
        candidates = TM.compute_related_candidates(EMB, SLUGS, top_k=top_k,
                                                   papers=PAPERS)
        client = _RecordingClient()
        TM.generate_connections_from_candidates(
            {TARGET: candidates[TARGET]}, PAPERS, client,
            batch_size=25, deadline_s=30, max_rounds=1)
        self.assertEqual(len(client.prompts), 1)
        return client.prompts[0]

    def test_every_candidate_reaches_the_prompt(self):
        """No `cands[:10]`: the caller's top_k is what the model sees."""
        prompt = self._prompt_for(top_k=5)
        for slug in SLUGS:
            if slug == TARGET:
                continue
            self.assertIn(f"[{slug.split('_')[0]}]", prompt, slug)

    def test_candidates_carry_their_titles(self):
        prompt = self._prompt_for(top_k=5)
        for paper in PAPERS:
            if paper["slug"] == TARGET:
                continue
            self.assertIn(paper["title"][:40], prompt, paper["slug"])

    def test_prompt_does_not_claim_cosine_ordering(self):
        """The list is RRF-ordered; telling the model it is cosine-sorted makes
        a low score read as 'unrelated' when it only means 'lexically found'."""
        prompt = self._prompt_for(top_k=5)
        self.assertNotIn("sorted by embedding similarity", prompt)
        self.assertIn("RRF-fused", prompt)

class SalvageJsonTests(unittest.TestCase):
    """A malformed byte must cost one paper, not the whole 15-paper batch.

    Both broken shapes below are transcribed from the live full-corpus run
    (2026-08-31): `Expecting value: line 203 column 15` and `Expecting property
    name enclosed in double quotes: line 131 column 6`.
    """

    GOOD = ('{"0100": [{"target": "0044", "relation": "foundation", '
            '"reason": "직접적인 선행 연구."}], '
            '"0201": [{"target": "0202", "relation": "alternative", '
            '"reason": "같은 문제의 다른 접근."}]}')

    def test_valid_json_passes_through(self):
        got = TM.parse_connection_json(self.GOOD)
        self.assertEqual(sorted(got), ["0100", "0201"])
        self.assertEqual(got["0100"][0]["target"], "0044")

    def test_truncated_tail_keeps_the_completed_papers(self):
        cut = self.GOOD[:self.GOOD.index('"0201"')] + '"0201": [{"target": "02'
        got = TM.parse_connection_json(cut)
        self.assertIn("0100", got)
        self.assertEqual(got["0100"][0]["relation"], "foundation")

    def test_one_broken_object_does_not_kill_its_siblings(self):
        broken = ('{"0100": [{"target": "0044", "relation": "foundation", '
                  '"reason": "ok."}, '
                  '{target: "0203", "relation": }, '        # 깨진 객체
                  '{"target": "0202", "relation": "alternative", '
                  '"reason": "살아남아야 한다."}]}')
        got = TM.parse_connection_json(broken)
        targets = [c["target"] for c in got["0100"]]
        self.assertEqual(targets, ["0044", "0202"])

    def test_a_broken_paper_does_not_kill_the_batch(self):
        broken = ('{"0100": [{"target": , }], '
                  '"0201": [{"target": "0202", "relation": "alternative", '
                  '"reason": "정상."}]}')
        got = TM.parse_connection_json(broken)
        self.assertNotIn("0100", got)
        self.assertEqual(got["0201"][0]["target"], "0202")

    def test_objects_without_a_target_are_dropped(self):
        got = TM.parse_connection_json(
            '{"0100": [{"relation": "foundation", "reason": "타깃 없음"}, '
            '{"target": "0044", "relation": "extension", "reason": "ok"}] ')
        self.assertEqual([c["target"] for c in got["0100"]], ["0044"])

    def test_total_garbage_still_raises(self):
        """Unparseable must stay an error so the round retries the batch."""
        with self.assertRaises(ValueError):
            TM.parse_connection_json("I'm sorry, I can't help with that.")



if __name__ == "__main__":
    unittest.main(verbosity=2)
