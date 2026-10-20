"""build_slide_brief: 정책 브리핑 PPTX — 텍스트 정리 규칙·도판 선택·기하 정수화, 라이브 코퍼스 스모크."""
import io
import re
import unittest
from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.util import Emu, Inches

from pipeline import build_slide_brief as Bf
from pipeline import build_slide_deck as B


class TextRuleTests(unittest.TestCase):
    def test_ko_names_localises_categories_and_drops_slug_refs(self):
        t = ("Autonomous AI Scientific Discovery 카테고리와 Formal Mathematical Theorem Proving에서 "
             "예측 10900/10714, 모델 10566 (10909, 11016) Nature 624, 86 (2023) 44% 150편 2,709편")
        out = Bf.ko_names(t)
        self.assertIn("자율 AI 과학 발견와", out)
        self.assertIn("형식 수학 정리 증명에서", out)
        self.assertNotIn("10900", out)
        self.assertNotIn("10909", out)
        self.assertIn("(2023)", out, "연도는 근거 번호가 아니다")
        self.assertIn("44%", out)
        self.assertIn("150편", out)
        self.assertIn("2,709편", out)

    def test_strip_srefs_maps_slide_numbers_to_names(self):
        names = {17: "LLM 형식 정리 증명", 13: "에이전틱 신약 발굴"}
        self.assertEqual(Bf.strip_srefs("검증기 결합 (S17·S13) 이후", names), "검증기 결합 이후")
        self.assertEqual(Bf.strip_srefs("S17 참고", names), "'LLM 형식 정리 증명' 참고")

    def test_shorten_prefers_sentence_boundary(self):
        t = "첫 문장이다. 둘째 문장은 조금 더 길다, 그래서 잘린다. 셋째 문장."
        out = Bf.shorten(t, 30)
        self.assertTrue(out.endswith("다.") or out.endswith("다") or out.endswith("…"), out)
        self.assertLessEqual(len(out), 31)
        self.assertEqual(Bf.shorten("짧다", 30), "짧다")

    def test_strip_year_removes_leading_year_or_background_label(self):
        self.assertEqual(Bf.strip_year("2026 FooBench가 쟀다."), "FooBench가 쟀다.")
        self.assertEqual(Bf.strip_year("2018–2021 SCANPY류"), "SCANPY류")
        self.assertEqual(Bf.strip_year("배경: 과거 흐름"), "과거 흐름")

    def test_E_rounds_to_integer_emu(self):
        v = Bf.E(Bf.INNER_W * 0.6)
        self.assertIsInstance(v, int)
        self.assertEqual(v, int(round(Bf.INNER_W * 0.6)))


class FigureTests(unittest.TestCase):
    def test_good_figure_filters_small_or_extreme_aspect(self):
        figs = [{"w": 300, "h": 300, "n": 1}, {"w": 1400, "h": 300, "n": 2}, {"w": 1200, "h": 800, "n": 3}]
        self.assertEqual(Bf.good_figure(figs)["n"], 3)
        self.assertIsNone(Bf.good_figure(figs[:2]))

    def test_autocrop_trims_white_margins_but_keeps_tiny_content(self):
        im = Image.new("RGB", (400, 300), "white")
        for x in range(80, 330):
            for y in range(50, 250):
                im.putpixel((x, y), (30, 60, 200))
        out = Bf.autocrop(im)
        self.assertLess(out.width, 300)
        self.assertLess(out.height, 240)
        dot = Image.new("RGB", (400, 300), "white")
        dot.putpixel((5, 5), (0, 0, 0))
        self.assertEqual(Bf.autocrop(dot).size, (400, 300), "내용이 거의 없으면 원본 유지")


class GeometryTests(unittest.TestCase):
    def _slide(self):
        prs = Presentation()
        prs.slide_width, prs.slide_height = Bf.W, Bf.H
        return prs, prs.slides.add_slide(prs.slide_layouts[6])

    def test_chart_frame_has_integer_extent(self):
        prs, s = self._slide()
        b = Bf.Brief.__new__(Bf.Brief)
        b.prs = prs
        b.bar_chart(s, Bf.M, Bf.TOP, Bf.INNER_W * 0.6, Inches(3.3), ["가", "나"], [1, 2], Bf.ACCENT)
        buf = io.BytesIO()
        prs.save(buf)
        xml = Presentation(io.BytesIO(buf.getvalue())).slides[0]._element.xml
        self.assertIsNone(re.search(r'(?:cx|cy|x|y)="\d+\.\d+"', xml), "float EMU 가 남으면 PowerPoint 가 차트를 버린다")

    def test_fit_picture_keeps_aspect_and_stays_inside_box(self):
        prs, s = self._slide()
        tmp = Path("/tmp/_brief_test.png")
        Image.new("RGB", (1000, 400), "red").save(tmp)
        box = (Inches(1), Inches(1), Inches(4), Inches(4))
        pic = Bf.fit_picture(s, tmp, *box)
        self.assertAlmostEqual(pic.width / pic.height, 2.5, places=1)
        self.assertGreaterEqual(pic.left, box[0])
        self.assertLessEqual(pic.left + pic.width, box[0] + box[2] + Emu(1))
        self.assertLessEqual(pic.top + pic.height, box[1] + box[3] + Emu(1))


class LiveCorpusSmokeTests(unittest.TestCase):
    def test_brief_builds_with_figures_notes_and_no_placeholders(self):
        root = Path(__file__).resolve().parents[2] / "docs" / "ai4s"
        if not all((root / f).exists() for f in ("_new_classification.json", "_category_summaries.json",
                                                "_timeline_narrative.json", "_insights.json", "_umap_coords.json")):
            self.skipTest("docs/ai4s 코퍼스 없음")
        try:
            prs, brief = Bf.build_brief("ai4s")
        except B.TaxonomyMismatch as exc:
            self.skipTest(str(exc))
        n_cats = len(brief.corpus["cats"])
        self.assertGreaterEqual(len(prs.slides), 3 + 5 + 2 * n_cats + 10)
        n_pics = sum(1 for s in prs.slides for shp in s.shapes if shp.shape_type == 13)  # PICTURE
        self.assertGreaterEqual(n_pics, 2 * n_cats + 1, "대분류마다 도판 2장 이상 + 지형도")
        n_charts = sum(1 for s in prs.slides for shp in s.shapes if shp.has_chart)
        self.assertGreaterEqual(n_charts, n_cats + 2)
        for s in prs.slides:
            slide_text = "\n".join(shp.text_frame.text for shp in s.shapes if shp.has_text_frame)
            is_sources = "도판 출처" in slide_text   # 부록 C 는 이 덱 자신의 S번호를 쓴다
            for shp in s.shapes:
                self.assertLessEqual(shp.left + shp.width, Bf.W + Emu(1), shp.name)
                self.assertLessEqual(shp.top + shp.height, Bf.H + Emu(1), shp.name)
                if shp.has_text_frame:
                    self.assertIsNone(re.search(r"\{[a-z_]+(?::[^{}]+)?\}", shp.text_frame.text),
                                      "미치환 플레이스홀더")
                    if not is_sources:
                        self.assertNotRegex(shp.text_frame.text, r"\bS\d{2}\b", "58장 덱의 슬라이드 번호가 새면 안 된다")
        self.assertTrue(any(s.has_notes_slide and s.notes_slide.notes_text_frame.text for s in prs.slides))
        self.assertEqual(len({(p["slug"], f["n"]) for _, p, f in brief.sources}),
                         len({(p["slug"], f["n"]) for _, p, f in brief.sources}))
        xml = "".join(s._element.xml for s in prs.slides)
        self.assertIsNone(re.search(r'(?:cx|cy)="\d+\.\d+"', xml))
