"""build_slide_deck 의 인용 마커·레퍼런스 선정 규칙 회귀 테스트."""
import unittest

from pipeline import build_slide_deck as B


class TitleCleaningTests(unittest.TestCase):
    def test_clean_title_strips_latex_and_markdown(self):
        self.assertEqual(B.clean_title(r"$\texttt{FlashSchNet}$: Fast MD"), "FlashSchNet: Fast MD")
        self.assertEqual(B.clean_title("**3D 오일러** 방정식"), "3D 오일러 방정식")

    def test_fingerprint_matches_duplicate_slugs(self):
        a = r"$\texttt{FlashSchNet}$: Fast and Accurate Coarse-Grained Neural Network"
        b = "FlashSchNet: Fast and Accurate Coarse-Grained Neural Network"
        self.assertEqual(B.title_fingerprint(a), B.title_fingerprint(b))

    def test_title_phrase_hit_requires_real_phrase(self):
        paper = {"title": "Discovery of Unstable Singularities"}
        self.assertTrue(B.title_phrase_hit(paper, "2025 Discovery of Unstable Singularities: ML과 결합"))
        self.assertFalse(B.title_phrase_hit(paper, "2025 특이점 발견 연구가 나왔다"))


class CitationMarkerTests(unittest.TestCase):
    def test_ref_keys_takes_headword_only(self):
        """범용 모델명(AlphaFold2)이 다른 논문 제목에 섞였다는 이유로 마커가 붙으면 안 된다."""
        keys = B.ref_keys(
            {"title": "MotifCraft: scalable binder design with AlphaFold2 hallucination"},
            tools=["RFdiffusion", "AlphaFold2/3"])
        self.assertEqual(keys, {"MotifCraft"})

    def test_ref_keys_includes_tool_present_in_title(self):
        keys = B.ref_keys(
            {"title": "Atomically accurate de novo design of antibodies with RFdiffusion"},
            tools=["RFdiffusion", "ProteinMPNN"])
        self.assertIn("RFdiffusion", keys)
        self.assertNotIn("ProteinMPNN", keys)

    def test_marker_attaches_only_to_matching_bullet(self):
        refs = [{"title": "PDFBench: A Benchmark for De Novo Protein Design from Function"},
                {"title": "Boltz-2 accelerates affinity prediction"}]
        points = ["2026 신뢰성 감사 — ProtDBench, PDFBench, ProMiSE.", "2025 무관한 불릿."]
        out = B.attach_markers(points, refs, tools=[])
        self.assertTrue(out[0].endswith("[1]"))
        self.assertEqual(out[1], points[1])

    def test_marker_absorbs_singular_plural(self):
        refs = [{"title": "Mitigating Gradient Pathology in PINNs through Aligned Constraint"}]
        out = B.attach_markers(["2026 PINN 실패 모드 진단"], refs, tools=[])
        self.assertTrue(out[0].endswith("[1]"))

    def test_marker_attaches_on_literal_title_mention(self):
        refs = [{"title": "Discovery of Unstable Singularities"}]
        out = B.attach_markers(["2025 Discovery of Unstable Singularities: ML 결합"], refs, tools=[])
        self.assertTrue(out[0].endswith("[1]"))


class ReferenceSelectionTests(unittest.TestCase):
    PAPERS = [
        {"slug": "1_old", "title": "Old landmark work", "date": "2020",
         "citation_count": 5000, "score": 5, "essence": "", "authors": []},
        {"slug": "2_new", "title": "FlashSchNet: Fast MD", "date": "2026",
         "score": 4, "essence": "", "authors": []},
        {"slug": "3_dup", "title": r"$\texttt{FlashSchNet}$: Fast MD", "date": "2026",
         "score": 4, "essence": "", "authors": []},
    ]

    def test_prefers_recent_over_highly_cited_old(self):
        refs = B.pick_papers(self.PAPERS, tools=[], keywords=[], link_base="X",
                             limit=4, since=2025)
        self.assertEqual([r["slug"] for r in refs], ["2_new", "1_old"])

    def test_link_points_at_review_document(self):
        refs = B.pick_papers(self.PAPERS, tools=[], keywords=[],
                             link_base="../../docs/papers", limit=1, since=2025)
        self.assertEqual(refs[0]["url"], "../../docs/papers/2_new/index.html")


if __name__ == "__main__":
    unittest.main()


class SlideEssayTests(unittest.TestCase):
    """v2(줄글) 판본: 50장 골격과 본문 집필 완료 여부를 고정한다."""

    def test_prose_covers_every_slide(self):
        from pipeline import build_slide_essay as E
        from pipeline.lib.slide_prose_ai4s import PROSE
        frame = {k for k, *_ in E.FRAME} | {k for k, *_ in E.CLOSING}
        self.assertEqual(len(frame), 10)
        self.assertTrue(frame <= set(PROSE), f"오프닝/종합 미집필: {frame - set(PROSE)}")
        self.assertEqual(len(PROSE), 50, "본문 40장 + 오프닝·종합 10장 = 50장이어야 한다")

    def test_every_prose_entry_has_lead_body_close(self):
        from pipeline.lib.slide_prose_ai4s import PROSE
        for key, v in PROSE.items():
            with self.subTest(key=key):
                self.assertTrue(v.get("lead"), f"{key}: lead 없음")
                self.assertGreaterEqual(len(v.get("body", [])), 4, f"{key}: 본문 문단 4개 미만")
                self.assertTrue(v.get("close"), f"{key}: close 없음")
                chars = len(v["lead"]) + sum(len(x) for x in v["body"]) + len(v["close"])
                self.assertGreater(chars, 800, f"{key}: 본문 {chars}자 — 절 분량 미달")


class CategoryRecountTests(unittest.TestCase):
    """편수는 요약본 스냅샷이 아니라 `_new_classification.json` 에서 다시 센다.

    이 게이트가 없으면 `_category_summaries.json` 이 만들어진 시점 이후에 들어온
    논문이 슬라이드 편수에 반영되지 않아, 웹 인덱스와 숫자가 어긋난다.
    """

    CLASSIFICATION = {
        "assignments": [
            {"slug": "1_a", "primary_category": "A", "sub_category": "a1",
             "all_categories": ["A", "B"]},
            {"slug": "2_a", "primary_category": "A", "sub_category": "a1",
             "all_categories": ["A"]},
            {"slug": "3_a", "primary_category": "A", "sub_category": "a2",
             "all_categories": ["A", "B", "C"]},
            {"slug": "4_b", "primary_category": "B", "sub_category": "b1",
             "all_categories": ["B", "A"]},
        ]
    }

    def test_recount_fills_both_bases(self):
        summaries = [
            {"category": "A", "count": 1,
             "sub_themes": [{"name": "a1", "count": 1}, {"name": "a2", "count": 99}]},
            {"category": "B", "count": 1, "sub_themes": [{"name": "b1", "count": 1}]},
        ]
        B.recount_categories(summaries, self.CLASSIFICATION)
        a, b = summaries
        self.assertEqual(a["count"], 3)          # primary: 1_a, 2_a, 3_a
        self.assertEqual(a["card_count"], 4)     # all_categories: +4_b
        self.assertEqual(b["count"], 1)
        self.assertEqual(b["card_count"], 3)     # 1_a, 3_a, 4_b
        self.assertEqual([s["count"] for s in a["sub_themes"]], [2, 1])
        self.assertEqual([s["count"] for s in b["sub_themes"]], [1])

    def test_primary_counts_sum_to_corpus(self):
        summaries = [{"category": c, "count": 0, "sub_themes": []} for c in "ABC"]
        B.recount_categories(summaries, self.CLASSIFICATION)
        self.assertEqual(sum(c["count"] for c in summaries),
                         len(self.CLASSIFICATION["assignments"]))

    def test_unknown_category_keeps_its_own_count(self):
        summaries = [{"category": "Z", "count": 7, "sub_themes": [{"name": "z", "count": 7}]}]
        B.recount_categories(summaries, self.CLASSIFICATION)
        self.assertEqual(summaries[0]["count"], 7)
        self.assertEqual(summaries[0]["card_count"], 7)
        self.assertEqual(summaries[0]["sub_themes"][0]["count"], 7)


class Ai4sProseCountDriftTests(unittest.TestCase):
    """ai4s 코퍼스가 있을 때, 손으로 쓴 줄글의 '{N}편' 이 실제 편수와 맞는지 본다."""

    @staticmethod
    def _live_counts():
        import json
        from pathlib import Path
        from collections import Counter
        root = Path(__file__).resolve().parents[2] / "docs" / "ai4s"
        cls_path = root / "_new_classification.json"
        sum_path = root / "_category_summaries.json"
        if not (cls_path.exists() and sum_path.exists()):
            return None, None
        cls = json.loads(cls_path.read_text(encoding="utf-8"))
        summaries = json.loads(sum_path.read_text(encoding="utf-8"))
        B.recount_categories(summaries, cls)
        subs = Counter()
        for a in cls.get("assignments", []):
            subs[a.get("sub_category")] += 1
        return summaries, subs

    def test_prose_leads_match_live_subcategory_counts(self):
        import re
        summaries, subs = self._live_counts()
        if summaries is None:
            self.skipTest("docs/ai4s 코퍼스 없음")
        from pipeline.lib.slide_prose_ai4s import PROSE
        known = {st["name"] for c in summaries for st in c.get("sub_themes", [])}
        for key, v in PROSE.items():
            m = re.match(r"([\d,]+)편", v.get("lead", ""))
            if not m or key not in known:
                continue
            with self.subTest(key=key):
                self.assertEqual(int(m.group(1).replace(",", "")), subs[key],
                                 f"{key}: 줄글 첫 문장 편수가 코퍼스와 다르다")

    def test_landscape_prose_matches_live_category_counts(self):
        summaries, _ = self._live_counts()
        if summaries is None:
            self.skipTest("docs/ai4s 코퍼스 없음")
        from pipeline.lib.slide_prose_ai4s import PROSE
        text = " ".join([PROSE["landscape"]["lead"], *PROSE["landscape"]["body"],
                         PROSE["landscape"]["close"], *PROSE["method"]["body"]])
        for c in summaries:
            with self.subTest(category=c["category"]):
                self.assertIn(f"{c['count']:,}편", text)
                self.assertIn(f"{c['card_count']:,}편", text)
        self.assertIn(f"{sum(c['count'] for c in summaries):,}편", text)
        self.assertIn(f"{sum(c['card_count'] for c in summaries):,}편", text)
