"""originality.md 캐시의 출처 검증 (2026-08-31).

`originality.md` 는 캐시인데 **자기가 어느 text.md 에서 나왔는지 기록하지
않았다**. 파일이 있고 비어 있지만 않으면 원문을 다시 보지 않았으므로, 한번
잘못 들어간 파일은 영구히 남아 그 논문의 임베딩·분류·연관논문을 전부 남의
내용으로 계산하게 만들었다. 도입 시점 실측 **29편(0.7%)**:

    256_De_novo_design_of_protein_structure_with_RFdiffusion (Nature 2023)
      originality.md : "Here, we introduce VibeGen, ..."   ← 슬러그 065 의 문장
      text.md        : "De novo design ... Watson1,2,15"   ← 자기 것 (정상)
      text.md 내 "VibeGen" 등장: 0회

저장소의 선례를 그대로 쓴다 — `bibliography.json` 사이드카는 `text_md_sha256`
를 같이 적고 해시가 어긋나면 거부한다.

여기서 고정하는 계약:
  * 사이드카가 원문을 가리키면 캐시를 그대로 쓴다.
  * 사이드카가 없으면 재추출하지 **않고** 내용으로 검증해 통과 시 backfill —
    전량 재추출은 임베딩을 흔들어 카테고리를 33% 뒤집으므로 증거 없이 못 한다.
  * 검증 실패(= 남의 논문 것)와 원문 변경만 재추출한다.
  * `_extract_rule_based` 에 끝 경계가 있다 (예전엔 문서 끝까지 잘라 268KB).
  * 임베딩 캐시는 슬러그뿐 아니라 originality 해시도 본다.

Run:
  PYTHONUTF8=1 /opt/homebrew/Caskroom/miniconda/base/envs/py312/bin/python \
      pipeline/tests/test_originality_provenance.py
"""

import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib.originality_extractor import (  # noqa: E402
    MIN_ORIGINALITY_CHARS, _extract_rule_based, derives_from, load_triggers,
    looks_unusable, read_provenance, text_digest, write_provenance,
)

TRIGGERS = load_triggers()

# 실제 사고를 축약한 두 논문.
RF_TEXT = (
    "De novo design of protein structure and function with RFdiffusion. "
    "Joseph L. Watson, David Juergens. Abstract. "
    "Here we describe RFdiffusion, a generative model of protein backbones "
    "obtained by fine-tuning the RoseTTAFold structure prediction network on "
    "protein structure denoising tasks. We show that RFdiffusion enables the "
    "design of protein binders and symmetric oligomers. "
) + "Filler sentence about downstream analysis. " * 40

VIBEGEN_ORIG = (
    "Here, we introduce VibeGen, a generative AI framework that enables "
    "end-to-end de novo protein design conditioned on normal mode vibrations."
)


class DerivesFromTests(unittest.TestCase):

    def test_own_extraction_is_recognised(self):
        orig = _extract_rule_based(RF_TEXT, TRIGGERS)
        self.assertTrue(orig)
        self.assertTrue(derives_from(orig, RF_TEXT))

    def test_another_papers_text_is_rejected(self):
        """실제 사고: RFdiffusion 논문이 VibeGen 문장을 들고 있었다."""
        self.assertNotIn("VibeGen", RF_TEXT)
        self.assertFalse(derives_from(VIBEGEN_ORIG, RF_TEXT))

    def test_hyphenated_linebreaks_do_not_cause_false_alarms(self):
        """PDF 가 단어를 하이픈으로 끊는다. 복원 안 하면 멀쩡한 파일이 탈락한다
        (거친 대조 729편 → 하이픈 복원 118편 → NFKD 까지 맞춰 29편)."""
        text = RF_TEXT.replace("generative model", "genera- tive model")
        orig = _extract_rule_based(RF_TEXT, TRIGGERS)
        self.assertTrue(derives_from(orig, text))

    def test_metadata_leaks_do_not_cause_false_alarms(self):
        """_strip_metadata_leaks 가 DOI/URL 을 지우므로 원문에는 남아 있다."""
        text = RF_TEXT.replace("Abstract.", "Abstract. https://doi.org/10.1038/x1")
        orig = _extract_rule_based(text, TRIGGERS)
        self.assertTrue(derives_from(orig, text))

    def test_ligatures_and_accents_do_not_cause_false_alarms(self):
        """split_sentences 가 NFKD 를 걸어 합자·악센트를 분해한다. 대조 쪽에서
        같은 정규화를 하지 않으면 멀쩡한 파일이 '남의 것' 으로 잘못 걸린다 —
        실제로 116편을 재추출했는데 내용이 바뀐 건 36편뿐이었다."""
        text = RF_TEXT.replace("fine-tuning", "ﬁne-tuning").replace("Joseph", "Josëph")
        orig = _extract_rule_based(text, TRIGGERS)
        self.assertTrue(derives_from(orig, text))

    def test_too_short_to_judge_passes(self):
        """제목+essence fallback 처럼 짧은 건 판정 근거가 없다 — 통과시킨다."""
        self.assertTrue(derives_from("RFdiffusion. A protein model.", RF_TEXT))


class ExtractionBoundaryTests(unittest.TestCase):

    def test_fulltext_extraction_is_bounded(self):
        """예전엔 sentences[start_idx:] 로 문서 끝까지 가져와 268KB 가 나왔다."""
        orig = _extract_rule_based(RF_TEXT, TRIGGERS)
        self.assertLess(len(orig), 2000, orig[:200])
        self.assertLessEqual(orig.count(". Filler sentence"), 12)

    def test_boundary_keeps_the_contribution_sentences(self):
        orig = _extract_rule_based(RF_TEXT, TRIGGERS)
        self.assertIn("RFdiffusion", orig)
        self.assertIn("RoseTTAFold", orig)

    def test_unsplittable_document_is_bounded_by_chars(self):
        """PDF 추출이 마침표를 잃으면 논문 한 편이 '문장 1개' 가 된다. 문장 수
        상한만으로는 그걸 통째로 통과시킨다 — 실제로 711KB 가 나왔다."""
        blob = ("We present a new method for X " + "and then more prose " * 8000)
        orig = _extract_rule_based(blob, TRIGGERS)
        self.assertLessEqual(len(orig), 4000, f"{len(orig)} chars")
        self.assertIn("We present a new method", orig)

    def test_max_sentences_is_honoured(self):
        two = _extract_rule_based(RF_TEXT, TRIGGERS, max_sentences=2)
        twelve = _extract_rule_based(RF_TEXT, TRIGGERS, max_sentences=12)
        self.assertLess(len(two), len(twelve))


class ProvenanceSidecarTests(unittest.TestCase):

    def test_round_trip(self):
        with tempfile.TemporaryDirectory() as d:
            write_provenance(d, text_digest(RF_TEXT), "rule.abstract")
            meta = read_provenance(d)
            self.assertEqual(meta["text_md_sha256"], text_digest(RF_TEXT))
            self.assertEqual(meta["extractor"], "rule.abstract")

    def test_missing_sidecar_is_empty(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(read_provenance(d), {})

    def test_unknown_schema_is_refused(self):
        """모르는 스키마를 신뢰하면 낡은 규약이 조용히 통과한다."""
        with tempfile.TemporaryDirectory() as d:
            with open(os.path.join(d, "originality.meta.json"), "w") as f:
                json.dump({"schema": 99, "text_md_sha256": "x"}, f)
            self.assertEqual(read_provenance(d), {})

    def test_corrupt_sidecar_is_empty_not_an_error(self):
        with tempfile.TemporaryDirectory() as d:
            with open(os.path.join(d, "originality.meta.json"), "w") as f:
                f.write("{not json")
            self.assertEqual(read_provenance(d), {})

    def test_digest_tracks_content(self):
        self.assertNotEqual(text_digest(RF_TEXT), text_digest(RF_TEXT + "x"))


class ExtractOriginalitiesCacheTests(unittest.TestCase):
    """topic_modeling.extract_originalities 의 캐시 판정."""

    def _run(self, papers):
        import topic_modeling as TM
        return TM.extract_originalities(papers)

    def _paper(self, root, slug, text, originality, meta_digest=None):
        d = os.path.join(root, slug)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "text.md"), "w", encoding="utf-8") as f:
            f.write(text)
        if originality is not None:
            with open(os.path.join(d, "originality.md"), "w", encoding="utf-8") as f:
                f.write(originality)
        if meta_digest is not None:
            write_provenance(d, meta_digest, "test")
        return {"slug": slug, "title": "T", "essence": "E"}

    def setUp(self):
        import topic_modeling as TM
        self.TM = TM
        self._old = TM.PAPERS_DIR
        self.tmp = tempfile.TemporaryDirectory()
        TM.PAPERS_DIR = self.tmp.name

    def tearDown(self):
        self.TM.PAPERS_DIR = self._old
        self.tmp.cleanup()

    def test_orphan_cache_is_re_extracted(self):
        p = self._paper(self.tmp.name, "256_RF", RF_TEXT, VIBEGEN_ORIG)
        out = self._run([p])
        self.assertNotIn("VibeGen", out["256_RF"])
        self.assertIn("RFdiffusion", out["256_RF"])
        # 재추출은 사이드카를 남긴다 → 다음 실행은 재검증 없이 hit
        meta = read_provenance(os.path.join(self.tmp.name, "256_RF"))
        self.assertEqual(meta["text_md_sha256"], text_digest(RF_TEXT))

    def test_valid_cache_without_sidecar_is_backfilled_not_rewritten(self):
        """내용은 그대로 두고 사이드카만 채워야 한다 — 전량 재추출을 피하는 핵심."""
        good = _extract_rule_based(RF_TEXT, TRIGGERS)
        p = self._paper(self.tmp.name, "300_Good", RF_TEXT, good)
        out = self._run([p])
        self.assertEqual(out["300_Good"], good)
        self.assertEqual(read_provenance(os.path.join(self.tmp.name, "300_Good"))
                         ["extractor"], "backfill")

    def test_sidecar_hit_short_circuits(self):
        good = _extract_rule_based(RF_TEXT, TRIGGERS)
        p = self._paper(self.tmp.name, "301_Hit", RF_TEXT, good,
                        meta_digest=text_digest(RF_TEXT))
        self.assertEqual(self._run([p])["301_Hit"], good)

    def test_changed_text_invalidates_the_cache(self):
        """원문이 바뀌면 사이드카 해시가 어긋나 재추출된다."""
        stale = "We present QuiteSomethingElse, a wholly unrelated system for X."
        p = self._paper(self.tmp.name, "302_Changed", RF_TEXT, stale,
                        meta_digest=text_digest("some older text.md"))
        out = self._run([p])
        self.assertNotIn("QuiteSomethingElse", out["302_Changed"])


class EmbeddingCacheInputGuardTests(unittest.TestCase):
    """캐시가 슬러그 집합만 보던 탓에, originality 가 바뀌어도 옛 벡터가 나왔다."""

    def test_changed_originality_forces_recompute(self):
        import numpy as np
        import topic_modeling as TM

        calls = []

        class FakeEmbed:
            EMBED_TAG = "fake_tag"

            @staticmethod
            def embed_texts(texts):
                calls.append(list(texts))
                return np.ones((len(texts), 4), dtype=np.float32)

        with tempfile.TemporaryDirectory() as d:
            cache = os.path.join(d, "_embeddings_cache.json")
            # SPECTER2 로더를 가로챈다 — 이 테스트가 재는 건 캐시 판정이지 임베딩이 아니다.
            import lib
            from lib import specter2_embed as real
            lib.specter2_embed = FakeEmbed
            sys.modules["lib.specter2_embed"] = FakeEmbed
            try:
                TM.compute_embeddings({"a": "first text", "b": "second text"}, cache)
                self.assertEqual(len(calls), 1)
                # 같은 입력 → 재계산 없음
                TM.compute_embeddings({"a": "first text", "b": "second text"}, cache)
                self.assertEqual(len(calls), 1)
                # a 의 originality 만 변경 → a 만 재계산
                TM.compute_embeddings({"a": "REWRITTEN", "b": "second text"}, cache)
                self.assertEqual(len(calls), 2)
                self.assertEqual(calls[1], ["REWRITTEN"])
                with open(cache, encoding="utf-8") as f:
                    saved = json.load(f)
                self.assertIn("originality_sha256", saved)
                self.assertEqual(saved["originality_sha256"]["a"],
                                 text_digest("REWRITTEN"))
            finally:
                lib.specter2_embed = real
                sys.modules["lib.specter2_embed"] = real


class UnusableOutputTests(unittest.TestCase):
    """LLM 이 요약 대신 거부문을 돌려주면 파일에 쓰면 안 된다.

    해시 사이드카는 이걸 못 잡는다 — 출처는 진짜로 그 text.md 가 맞기 때문이다.
    거부문이 저장되면 SPECTER2 가 *거부문*을 임베딩하고, 거부당한 논문들끼리
    서로 가까워져 가짜 클러스터가 생긴다. 어설픈 요약보다 훨씬 나쁘다.
    """

    # 실제 claude-haiku-4-5 가 슬러그 9132(목차만 추출된 논문)에 돌려준 응답.
    REAL_REFUSAL = (
        "I cannot provide the requested summary because the provided text is "
        "only a table of contents and section headings, not the actual paper "
        "content or abstract. To state what the paper newly contributes, I "
        "would need access to the abstract, introduction, or contributions "
        "section that describes the work.")

    GOOD = ("The paper introduces RFdiffusion, a generative model of protein "
            "backbones created by fine-tuning the RoseTTAFold structure "
            "prediction network on protein structure denoising tasks. It "
            "enables de novo design of protein binders, symmetric oligomers "
            "and enzyme active site scaffolds.")

    def test_real_haiku_refusal_is_caught(self):
        self.assertEqual(looks_unusable(self.REAL_REFUSAL), "refusal")

    def test_good_summary_passes(self):
        self.assertEqual(looks_unusable(self.GOOD), "")

    def test_short_output_is_rejected(self):
        self.assertTrue(looks_unusable("Not enough.").startswith("too-short"))
        self.assertEqual(looks_unusable("x" * MIN_ORIGINALITY_CHARS), "")

    def test_other_refusal_phrasings(self):
        for text in (
            "I'm unable to summarize this document because no abstract is present "
            "anywhere in the supplied excerpt, so there is nothing to describe here.",
            "As an AI, I do not have the ability to read the attached PDF file, and "
            "therefore cannot determine what this particular paper contributes.",
            "The supplied text is only a list of section headings, so the paper's "
            "contribution cannot be determined from what was provided to me here.",
        ):
            self.assertEqual(looks_unusable(text), "refusal", text[:40])

    def test_prompt_echo_is_rejected(self):
        prompt = "In 2-4 sentences state ONLY what THIS paper newly contributes"
        echo = prompt + " — the method it introduces and what that enables for users."
        self.assertEqual(looks_unusable(echo, prompt_echo=prompt), "prompt-echo")

    def test_contribution_wording_is_not_mistaken_for_refusal(self):
        """'cannot' 이 논문 내용에 등장하는 것과 모델의 거부는 다르다."""
        text = ("The paper introduces SafeGuard, a verifier that proves a policy "
                "cannot enter unsafe states, and shows the controller is unable to "
                "violate the constraint under bounded disturbance.")
        self.assertEqual(looks_unusable(text), "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
