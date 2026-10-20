"""build_slide_deck 의 인용 마커·레퍼런스 선정 규칙 회귀 테스트."""
import unittest

from pipeline import build_slide_deck as B


class TitleCleaningTests(unittest.TestCase):
    def test_clean_title_strips_latex_and_markdown(self):
        self.assertEqual(B.clean_title(r"$\texttt{FlashSchNet}$: Fast MD"), "FlashSchNet: Fast MD")
        self.assertEqual(B.clean_title("**3D 오일러** 방정식"), "3D 오일러 방정식")
        self.assertEqual(B.clean_title(r"Series for $\boldsymbol{\frac{1}{\pi}}$"), "Series for 1/π")

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
    """v2(줄글) 판본: 오프닝·종합 골격과 집필본 형식을 고정한다."""

    def test_prose_and_narrative_cover_every_frame_slide(self):
        from pipeline import build_slide_essay as E
        from pipeline.lib.slide_prose_ai4s import NARRATIVE, PROSE
        frame = {k for k, *_ in E.FRAME} | {k for k, *_ in E.CLOSING}
        self.assertEqual(frame, set(B.FRAME_KEYS))
        self.assertTrue(frame <= set(PROSE), f"오프닝/종합 줄글 미집필: {frame - set(PROSE)}")
        self.assertTrue(frame <= set(NARRATIVE), f"오프닝/종합 불릿 미집필: {frame - set(NARRATIVE)}")
        # 본문 키는 두 사전이 같은 서브카테고리 집합을 가져야 한다.
        self.assertEqual(set(PROSE) - frame, set(NARRATIVE) - frame)
        for key in ("arc", "verification", "action"):
            self.assertGreaterEqual(len(NARRATIVE[key].get("points", [])), 4, key)
        self.assertTrue(NARRATIVE["verification"].get("refs"))

    def test_every_prose_entry_has_lead_body_close(self):
        from pipeline.lib.slide_prose_ai4s import PROSE
        for key, v in PROSE.items():
            with self.subTest(key=key):
                self.assertTrue(v.get("lead"), f"{key}: lead 없음")
                self.assertGreaterEqual(len(v.get("body", [])), 4, f"{key}: 본문 문단 4개 미만")
                self.assertTrue(v.get("close"), f"{key}: close 없음")
                chars = len(v["lead"]) + sum(len(x) for x in v["body"]) + len(v["close"])
                self.assertGreater(chars, 800, f"{key}: 본문 {chars}자 — 절 분량 미달")

    def test_every_narrative_sub_entry_has_five_points(self):
        from pipeline.lib.slide_prose_ai4s import NARRATIVE
        for key, v in NARRATIVE.items():
            if key in B.FRAME_KEYS:
                continue
            with self.subTest(key=key):
                self.assertTrue(v.get("ko") and v.get("headline") and v.get("sowhat"), key)
                self.assertEqual(len(v.get("points", [])), 5, key)


class ProseContextTests(unittest.TestCase):
    """집필본 플레이스홀더 치환: 편수·슬라이드 번호·이름을 빌드 시점 코퍼스에서 읽는다."""

    def _ctx(self):
        cats = [
            {"category": "A", "count": 60, "card_count": 90,
             "sub_themes": [{"name": "a-big", "count": 40}, {"name": "a-small", "count": 20}]},
            {"category": "B", "count": 40, "card_count": 50,
             "sub_themes": [{"name": "b-only", "count": 40}]},
        ]
        years = {2024: 10, 2025: 30, 2026: 60}
        slide_no = {"a-big": 6, "a-small": 7, "b-only": 8}
        return B.ProseContext(cats, years, 100, 5, 2025, 3, slide_no,
                              {"a-big": 35, "a-small": 10, "b-only": 40}), cats

    def test_global_placeholders(self):
        ctx, _ = self._ctx()
        self.assertEqual(ctx.fill("{total}편/{cards}편, {n_cats}개, {n_subs}개, {n_body}장, "
                                  "{since}+ {recent_share}%, {y:2026}편"),
                         "100편/140편, 2개, 3개, 3장, 2025+ 90%, 60편")
        self.assertEqual(ctx.fill("{n:A}·{n:a-big}·{cards:B}·{s:b-only}"), "60·40·50·S08")

    def test_scoped_placeholders_require_context(self):
        ctx, cats = self._ctx()
        a = cats[0]
        self.assertEqual(ctx.fill("{cat_count}/{cat_cards}/{cat_share}%/{nsubs}", cat=a), "60/90/60%/2")
        self.assertEqual(ctx.fill("{count}편 중 {recent}편, {sub_share}%", sub=a["sub_themes"][0]),
                         "40편 중 35편, 67%")
        with self.assertRaises(KeyError):
            ctx.fill("{count}")
        with self.assertRaises(KeyError):
            ctx.fill("{cat_count}")

    def test_unknown_names_fail_loudly(self):
        ctx, _ = self._ctx()
        with self.assertRaisesRegex(KeyError, "없는 이름"):
            ctx.fill("{n:Nope}")
        with self.assertRaisesRegex(KeyError, "없는 이름"):
            ctx.fill("{s:a-nope}")
        with self.assertRaisesRegex(KeyError, "알 수 없는"):
            ctx.fill("{bogus}")

    def test_fill_all_recurses_and_leaves_plain_braces(self):
        ctx, cats = self._ctx()
        out = ctx.fill_all({"points": ["{count}편", {"x": ["{total}"]}], "k": 1},
                           sub=cats[1]["sub_themes"][0])
        self.assertEqual(out, {"points": ["40편", {"x": ["100"]}], "k": 1})
        self.assertEqual(ctx.fill("집합 {1, 2} 는 그대로"), "집합 {1, 2} 는 그대로")

    def test_category_wins_name_collision_and_sub_key_forces_sub(self):
        cats = [{"category": "Same", "count": 300, "card_count": 800,
                 "sub_themes": [{"name": "Same", "count": 26}]}]
        ctx = B.ProseContext(cats, {}, 300, 5, 2025, 1, {"Same": 6}, {"Same": 20})
        self.assertEqual(ctx.fill("{n:Same}/{sub:Same}/{cards:Same}/{s:Same}"), "300/26/800/S06")
        with self.assertRaises(KeyError):
            ctx.fill("{sub:Nope}")

    def test_thousands_separator(self):
        cats = [{"category": "A", "count": 1234, "card_count": 2345, "sub_themes": []}]
        ctx = B.ProseContext(cats, {}, 1234, 5, 2025, 0, {}, {})
        self.assertEqual(ctx.fill("{total}편 {cards}편 {n:A}"), "1,234편 2,345편 1,234")


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


class TaxonomyPinTests(unittest.TestCase):
    """덱은 CATEGORY_KO 의 분류체계로 집필된 날짜별 산출물이다. 다른 분류체계에서는 빌드를 거부한다."""

    def test_gap_lists_only_unauthored_categories(self):
        authored = next(iter(B.CATEGORY_KO))
        summaries = [{"category": authored}, {"category": "Brand New Category"}]
        self.assertEqual(B.authored_taxonomy_gap(summaries), ["Brand New Category"])
        self.assertEqual(B.authored_taxonomy_gap([{"category": authored}]), [])

    def test_load_corpus_refuses_unauthored_taxonomy(self):
        import json
        import tempfile
        from pathlib import Path
        from unittest import mock
        with tempfile.TemporaryDirectory() as tmp:
            tdir = Path(tmp) / "topic"
            papers = Path(tmp) / "papers"
            tdir.mkdir()
            papers.mkdir()
            (tdir / "_category_summaries.json").write_text(
                json.dumps([{"category": "Brand New Category", "count": 1, "sub_themes": []}]),
                encoding="utf-8")
            for name in ("_new_classification.json", "_timeline_narrative.json"):
                (tdir / name).write_text("{}", encoding="utf-8")
            (papers / "_papers_index.json").write_text("[]", encoding="utf-8")
            with mock.patch.object(B, "get_topic_dir", return_value=tdir), \
                    mock.patch.object(B, "PAPERS_DIR", papers):
                with self.assertRaisesRegex(B.TaxonomyMismatch, "Brand New Category"):
                    B.load_corpus("topic")


class Ai4sProseCountDriftTests(unittest.TestCase):
    """ai4s 코퍼스가 있을 때, 집필본이 라이브 분류체계와 맞물리는지 본다.

    편수는 플레이스홀더라 숫자 드리프트는 없다. 남는 위험은 (1) 집필본 키가 라이브
    상위 서브카테고리와 어긋남, (2) `{n:NAME}`/`{s:NAME}` 가 없는 이름을 가리킴,
    (3) 지형도 줄글이 어떤 대분류의 편수를 빠뜨림 — 셋 다 여기서 잡는다. 분류체계
    자체가 바뀐 경우는 비교할 대상이 없으므로 이유를 밝히고 건너뛴다(빌드는
    TaxonomyPinTests 가 보증하듯 거부된다).
    """

    @staticmethod
    def _live():
        import json
        from pathlib import Path
        root = Path(__file__).resolve().parents[2] / "docs"
        tdir = root / "ai4s"
        paths = [tdir / "_new_classification.json", tdir / "_category_summaries.json",
                 tdir / "_timeline_narrative.json", root / "papers" / "_papers_index.json"]
        if not all(p.exists() for p in paths):
            return None
        cls, summaries, timeline, index = [json.loads(p.read_text(encoding="utf-8")) for p in paths]
        gap = B.authored_taxonomy_gap(summaries)
        if gap:
            raise unittest.SkipTest(
                f"덱 집필본({B.PROSE_AUTHORED})과 다른 분류체계: 미집필 카테고리 {len(gap)}개 "
                f"({gap[0]} 등) — 빌드는 TaxonomyMismatch 로 거부됨. 재집필 필요")
        B.recount_categories(summaries, cls)
        return B.prepare_corpus(summaries, cls, timeline, index, per_category=5, since=2025)

    def test_authored_keys_match_live_top_subcategories(self):
        corpus = self._live()
        if corpus is None:
            self.skipTest("docs/ai4s 코퍼스 없음")
        from pipeline.lib.slide_prose_ai4s import NARRATIVE, PROSE
        live = {st["name"] for _, st in corpus["order"]}
        frame = set(B.FRAME_KEYS)
        self.assertEqual(set(NARRATIVE) - frame, live,
                         "집필본 서브카테고리 키가 라이브 상위 서브카테고리와 다르다")
        self.assertEqual(set(PROSE) - frame, live)

    def test_every_placeholder_resolves_against_live_corpus(self):
        corpus = self._live()
        if corpus is None:
            self.skipTest("docs/ai4s 코퍼스 없음")
        from pipeline.lib.slide_prose_ai4s import CATEGORY_LEAD, NARRATIVE, PROSE
        ctx = corpus["ctx"]
        for c, st in corpus["order"]:
            with self.subTest(sub=st["name"]):
                ctx.fill_all(NARRATIVE[st["name"]], cat=c, sub=st)
                ctx.fill_all(PROSE[st["name"]], cat=c, sub=st)
        for c in corpus["cats"]:
            with self.subTest(cat=c["category"]):
                ctx.fill(CATEGORY_LEAD[c["category"]], cat=c)
        for key in B.FRAME_KEYS:
            with self.subTest(frame=key):
                ctx.fill_all(NARRATIVE[key])
                ctx.fill_all(PROSE[key])

    def test_landscape_prose_names_every_category_count(self):
        corpus = self._live()
        if corpus is None:
            self.skipTest("docs/ai4s 코퍼스 없음")
        from pipeline.lib.slide_prose_ai4s import PROSE
        ctx = corpus["ctx"]
        text = " ".join(ctx.fill(t) for t in [PROSE["landscape"]["lead"], *PROSE["landscape"]["body"],
                                              PROSE["landscape"]["close"], *PROSE["method"]["body"]])
        for c in corpus["cats"]:
            with self.subTest(category=c["category"]):
                self.assertIn(f"{c['count']:,}편", text)
                self.assertIn(f"{c['card_count']:,}편", text)
        self.assertIn(f"{corpus['total']:,}편", text)
        self.assertIn(f"{corpus['cards_total']:,}편", text)

    def test_authored_text_never_hardcodes_live_counts(self):
        """코퍼스 편수는 플레이스홀더여야 한다. 라이브 값과 같은 '{N}편' 리터럴은 하드코딩이다
        (논문이 보고한 데이터셋 규모처럼 코퍼스와 무관한 수치는 허용)."""
        import re
        corpus = self._live()
        if corpus is None:
            self.skipTest("docs/ai4s 코퍼스 없음")
        from pipeline.lib.slide_prose_ai4s import CATEGORY_LEAD, NARRATIVE, PROSE
        ctx = corpus["ctx"]

        def texts(v):
            return [v.get("lead", ""), v.get("close", ""), v.get("headline", ""),
                    v.get("sowhat", ""), *v.get("body", []), *v.get("points", [])]

        for c, st in corpus["order"]:
            forbidden = {st["count"], ctx.n_recent_by_sub.get(st["name"]), c["count"],
                         c["card_count"], ctx.total, ctx.cards}
            for t in texts(NARRATIVE[st["name"]]) + texts(PROSE[st["name"]]) + [CATEGORY_LEAD[c["category"]]]:
                for n in forbidden:
                    with self.subTest(sub=st["name"], n=n):
                        self.assertIsNone(re.search(rf"(?<![\d,{{:]){n:,}편", t),
                                          f"{st['name']}: {n:,}편 하드코딩 — {t[:60]!r}")
        for key in B.FRAME_KEYS:
            for t in texts(NARRATIVE[key]) + texts(PROSE[key]):
                for n in (ctx.total, ctx.cards):
                    with self.subTest(frame=key, n=n):
                        self.assertIsNone(re.search(rf"(?<![\d,{{:]){n:,}편", t),
                                          f"{key}: {n:,}편 하드코딩 — {t[:60]!r}")
