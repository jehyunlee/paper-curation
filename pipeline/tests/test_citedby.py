"""Regression coverage for the citedby subpackage (인용논문 수집).

이식(scisci → paper-curation) 과정에서 실제로 터졌거나 고친 계약을 잠근다:

  * 지연 로딩 — `import lib.citedby` 만으로 pandas 가 딸려오면 안 된다.
  * 재귀 — `__getattr__` 가 `from . import X` 를 쓰면 `_handle_fromlist` 의
    hasattr 검사와 물려 RecursionError 가 난다 (실제로 났고 import_module 로 고침).
  * 429 유한 재시도 — 원본은 rate limit 시 커서를 전진시키지 않고 `continue` 만
    해서 영구히 돌 수 있었다.
  * WoS 는 구조적으로 citing 조회 불가 → 항상 0건 + 사유 노출.
  * 우선순위 병합 — 상위 source 우선, 초록은 더 긴 버전으로 승격, 피인용은 최대값.
"""
from __future__ import annotations

import re
import subprocess
import sys
import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

PIPELINE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE_DIR))

from lib.citedby import citing  # noqa: E402
from lib.citedby import report  # noqa: E402
from lib.citedby import scopus  # noqa: E402


class LazyImportTests(unittest.TestCase):
    """패키지 import 만으로 무거운 의존성이 로드되면 안 된다."""

    def test_import_package_does_not_load_pandas(self):
        # 이미 citing 을 import 한 이 프로세스로는 검증이 불가능하므로
        # 깨끗한 서브프로세스에서 확인한다.
        code = (
            "import sys;"
            f"sys.path.insert(0, {str(PIPELINE_DIR)!r});"
            "import lib.citedby;"
            "print('pandas' in sys.modules)"
        )
        out = subprocess.run([sys.executable, "-c", code],
                             capture_output=True, text=True, timeout=120)
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertEqual(out.stdout.strip(), "False",
                         "citedby import 만으로 pandas 가 로드됐다 (지연 로딩 깨짐)")

    def test_attribute_access_does_not_recurse(self):
        """`__getattr__` ↔ `_handle_fromlist` 순환 회귀 방지.

        citing.py 가 `from . import scopus` 를 하므로, 부모의 `__getattr__` 가
        같은 형태를 쓰면 무한 재귀가 난다. 낮은 재귀 한도로 즉시 잡는다.
        """
        code = (
            "import sys;"
            f"sys.path.insert(0, {str(PIPELINE_DIR)!r});"
            "sys.setrecursionlimit(200);"
            "import lib.citedby as cb;"
            "cb.normalize_doi;"
            "print(cb.scopus.SCOPUS_SEARCH_URL)"
        )
        out = subprocess.run([sys.executable, "-c", code],
                             capture_output=True, text=True, timeout=120)
        self.assertEqual(out.returncode, 0,
                         f"submodule 접근에서 실패 (재귀 회귀?):\n{out.stderr[-1500:]}")
        self.assertIn("elsevier.com", out.stdout)


class NormalizeDoiTests(unittest.TestCase):
    def test_strips_known_prefixes(self):
        cases = {
            "https://doi.org/10.1038/abc": "10.1038/abc",
            "http://dx.doi.org/10.1/x": "10.1/x",
            "doi: 10.1234/abc": "10.1234/abc",
            "DOI:10.5/x": "10.5/x",
            "  10.9/y  ": "10.9/y",
            "10.1/plain": "10.1/plain",
        }
        for raw, expected in cases.items():
            with self.subTest(raw=raw):
                self.assertEqual(citing.normalize_doi(raw), expected)

    def test_empty_input_is_safe(self):
        self.assertEqual(citing.normalize_doi(""), "")
        self.assertEqual(citing.normalize_doi(None), "")


class WosUnsupportedTests(unittest.TestCase):
    def test_wos_always_returns_empty(self):
        self.assertEqual(citing.get_citing_from_wos("10.1/x"), [])

    def test_reason_is_surfaced(self):
        self.assertIn("wos", citing.UNSUPPORTED_SOURCES)
        self.assertTrue(citing.UNSUPPORTED_SOURCES["wos"].strip())

    def test_wos_included_in_fetchers_and_priority(self):
        # 소스 목록에 넣어도 죽지 않아야 한다 (0건이 정상).
        self.assertIn("wos", citing._SOURCE_FETCHERS)
        self.assertIn("wos", citing._SOURCE_PRIORITY)


class RateLimitTerminationTests(unittest.TestCase):
    """429 가 계속 와도 유한 시간에 끝나야 한다 (원본 무한루프 회귀 방지)."""

    class _Resp:
        status_code = 429
        headers: dict = {}
        text = "rate limited"

    def test_openalex_gives_up_after_bounded_retries(self):
        with patch.object(citing, "_openalex_resolve_doi", return_value="W123"), \
             patch.object(citing.time, "sleep"), \
             patch.object(citing.requests, "get",
                          return_value=self._Resp()) as mock_get:
            result = citing.get_citing_from_openalex("10.1/x")
        self.assertEqual(result, [])
        self.assertLessEqual(mock_get.call_count,
                             citing._MAX_RATE_LIMIT_RETRIES + 2,
                             "429 재시도가 상한을 넘었다 (무한루프 위험)")

    def test_s2_gives_up_after_bounded_retries(self):
        with patch.object(citing.time, "sleep"), \
             patch.object(citing.requests, "get",
                          return_value=self._Resp()) as mock_get:
            result = citing.get_citing_from_s2("10.1/x")
        self.assertEqual(result, [])
        self.assertLessEqual(mock_get.call_count,
                             citing._MAX_RATE_LIMIT_RETRIES + 2,
                             "429 재시도가 상한을 넘었다 (무한루프 위험)")


class MergeByPriorityTests(unittest.TestCase):
    """source 우선순위 병합 규칙."""

    @staticmethod
    def _row(**kw):
        base = {c: "" for c in citing.CITING_COLUMNS}
        base["citationCount"] = 0
        base.update(kw)
        return base

    def _merge(self, rows):
        import pandas as pd
        return citing._merge_by_priority(pd.DataFrame(rows))

    def test_higher_priority_source_wins_base_record(self):
        out = self._merge([
            self._row(title="Same Paper", source="semanticscholar", journal="S2 J"),
            self._row(title="Same Paper", source="scopus", journal="Scopus J"),
        ])
        self.assertEqual(len(out), 1)
        self.assertEqual(out.iloc[0]["source"], "scopus")
        self.assertEqual(out.iloc[0]["journal"], "Scopus J")

    def test_empty_field_filled_from_lower_priority(self):
        out = self._merge([
            self._row(title="P", source="scopus", journal=""),
            self._row(title="P", source="openalex", journal="OA Journal"),
        ])
        self.assertEqual(out.iloc[0]["journal"], "OA Journal")

    def test_abstract_upgraded_only_when_longer_and_superset(self):
        short = "Core claim."
        long_super = "Core claim. With much more detail appended here."
        out = self._merge([
            self._row(title="P", source="scopus", abstract=short),
            self._row(title="P", source="openalex", abstract=long_super),
        ])
        self.assertEqual(out.iloc[0]["abstract"], long_super)

    def test_abstract_not_replaced_when_unrelated(self):
        keep = "Original abstract text."
        other = "A completely different and longer abstract body here."
        out = self._merge([
            self._row(title="P", source="scopus", abstract=keep),
            self._row(title="P", source="openalex", abstract=other),
        ])
        self.assertEqual(out.iloc[0]["abstract"], keep)

    def test_citation_count_keeps_maximum(self):
        out = self._merge([
            self._row(title="P", source="scopus", citationCount=3),
            self._row(title="P", source="openalex", citationCount=17),
        ])
        self.assertEqual(int(out.iloc[0]["citationCount"]), 17)

    def test_distinct_titles_are_kept(self):
        out = self._merge([
            self._row(title="Paper A", source="scopus"),
            self._row(title="Paper B", source="scopus"),
        ])
        self.assertEqual(len(out), 2)

    def test_helper_columns_are_dropped(self):
        out = self._merge([self._row(title="P", source="scopus")])
        self.assertNotIn("_src_priority", out.columns)
        self.assertNotIn("_dedup_key", out.columns)


class IsEmptyTests(unittest.TestCase):
    def test_empty_values(self):
        for v in (None, "", "   ", "nan", "None", "0", "0.0"):
            with self.subTest(v=v):
                self.assertTrue(citing._is_empty(v))

    def test_non_empty_values(self):
        for v in ("text", 5, "10.1/x", 1.5):
            with self.subTest(v=v):
                self.assertFalse(citing._is_empty(v))


class FetchAllCitingTests(unittest.TestCase):
    """오케스트레이션: 병렬 수집 → 보고 → 병합."""

    def _fake_fetchers(self, mapping):
        return {src: (lambda recs: (lambda doi, n: list(recs)))(recs)
                for src, recs in mapping.items()}

    def test_dedups_across_sources_and_reports_counts(self):
        rows = {
            "scopus": [{**{c: "" for c in citing.CITING_COLUMNS},
                        "title": "Shared", "doi": "10.1/a",
                        "citationCount": 1, "source": "scopus"}],
            "openalex": [{**{c: "" for c in citing.CITING_COLUMNS},
                          "title": "Shared", "doi": "10.1/a",
                          "citationCount": 9, "source": "openalex"},
                         {**{c: "" for c in citing.CITING_COLUMNS},
                          "title": "Unique", "doi": "10.1/b",
                          "citationCount": 0, "source": "openalex"}],
        }
        events = []
        with patch.dict(citing._SOURCE_FETCHERS, self._fake_fetchers(rows),
                        clear=True), \
             patch.object(citing, "_fill_missing_abstracts_by_doi",
                          side_effect=lambda df: df):
            df, counts = citing.fetch_all_citing_papers(
                "10.1/seed", sources=["scopus", "openalex"],
                progress_callback=lambda phase, msg: events.append(msg))

        self.assertEqual(counts, {"scopus": 1, "openalex": 2})
        self.assertEqual(len(df), 2)                       # Shared 중복 제거
        self.assertEqual(sorted(df["title"]), ["Shared", "Unique"])
        self.assertTrue(any("scopus" in e for e in events))
        self.assertTrue(any("overlap(1)" in e for e in events))

    def test_unknown_source_is_ignored(self):
        with patch.dict(citing._SOURCE_FETCHERS, {}, clear=True):
            df, counts = citing.fetch_all_citing_papers("10.1/x",
                                                        sources=["nope"])
        self.assertTrue(df.empty)
        self.assertEqual(counts, {})
        self.assertEqual(list(df.columns), citing.CITING_COLUMNS)

    def test_failing_source_does_not_kill_the_run(self):
        def boom(doi, n):
            raise RuntimeError("network down")

        good = [{**{c: "" for c in citing.CITING_COLUMNS},
                 "title": "OK", "source": "openalex", "citationCount": 0}]
        with patch.dict(citing._SOURCE_FETCHERS,
                        {"scopus": boom, "openalex": lambda d, n: list(good)},
                        clear=True), \
             patch.object(citing, "_fill_missing_abstracts_by_doi",
                          side_effect=lambda df: df):
            df, counts = citing.fetch_all_citing_papers(
                "10.1/x", sources=["scopus", "openalex"])

        self.assertEqual(counts["scopus"], 0)
        self.assertEqual(len(df), 1)

    def test_unsupported_source_note_is_reported(self):
        events = []
        with patch.dict(citing._SOURCE_FETCHERS,
                        {"wos": citing.get_citing_from_wos}, clear=True):
            citing.fetch_all_citing_papers(
                "10.1/x", sources=["wos"],
                progress_callback=lambda phase, msg: events.append(msg))
        self.assertTrue(any("미지원" in e for e in events), events)


class ScopusConfigTests(unittest.TestCase):
    def test_available_degrades_gracefully_without_cfg(self):
        with patch.object(scopus, "config_path", return_value=None):
            scopus._api_keys = None          # 캐시 무효화
            ok, reason = scopus.available()
        self.assertFalse(ok)
        self.assertIn("pybliometrics.cfg", reason)

    def test_results_to_df_maps_scopus_fields(self):
        df = scopus.results_to_df([{
            "dc:title": "T", "dc:description": "A",
            "prism:coverDate": "2024-05-01", "prism:doi": "10.1/x",
            "eid": "2-s2.0-1", "citedby-count": "7",
            "prism:publicationName": "J", "author-count": {"$": "3"},
            "affiliation": [{"affilname": "KIST", "affiliation-country": "KOR"}],
        }])
        self.assertEqual(len(df), 1)
        row = df.iloc[0]
        self.assertEqual(row["title"], "T")
        self.assertEqual(row["year"], 2024)
        self.assertEqual(row["month"], 5)
        self.assertEqual(row["citationCount"], 7)
        self.assertEqual(row["author_count"], 3)
        self.assertEqual(row["af_name"], "KIST")
        self.assertEqual(row["source"], "scopus")

    def test_results_to_df_survives_malformed_entry(self):
        df = scopus.results_to_df([{"citedby-count": "not-a-number"},
                                   {"dc:title": "Good"}])
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]["title"], "Good")


class ReportLinkIntegrityTests(unittest.TestCase):
    """PDF 출력의 제1 불변식: 모든 앵커 href 가 절대 URL.

    브라우저 print-to-PDF 는 `<a href>` 를 PDF 링크 주석으로 보존하지만,
    상대경로는 인쇄 시점 문서 위치에 묶여 PDF 안에서 열리지 않는다. 따라서
    렌더러는 절대 URL 만 링크로 내보내고 나머지는 평문으로 떨어뜨려야 한다.
    """

    HREF_RE = re.compile(r'href="([^"]*)"')

    @staticmethod
    def _paper(**kw):
        base = {"title": "A Citing Paper", "journal": "Nature",
                "year": 2025, "citationCount": 4, "source": "openalex",
                "author_names": "Kim, J.; Lee, S.", "doi": "", "arxiv_id": "",
                "pdf_url": ""}
        base.update(kw)
        return base

    def _all_hrefs(self, html_text):
        return self.HREF_RE.findall(html_text)

    def test_every_anchor_href_is_absolute(self):
        papers = [
            self._paper(doi="10.1038/abc"),
            self._paper(title="ArXiv One", doi="", arxiv_id="2501.00001"),
            self._paper(title="OA PDF", pdf_url="https://ex.org/p.pdf"),
            self._paper(title="No Link At All"),
        ]
        out = report.build_report_html(
            papers=papers,
            paper_info={"title": "Seed", "doi": "10.1/seed"},
            topic="융합연구")
        hrefs = self._all_hrefs(out)
        self.assertTrue(hrefs, "링크가 하나도 없다 — 렌더가 깨졌다")
        for h in hrefs:
            with self.subTest(href=h):
                self.assertRegex(h, r"^https?://",
                                 f"절대 URL 이 아닌 href 가 PDF 로 새어나간다: {h}")

    def test_relative_and_scheme_hrefs_are_rejected(self):
        for bad in ("../papers/001_x/index.html", "/local/path",
                    "javascript:alert(1)", "file:///etc/passwd", "  "):
            with self.subTest(bad=bad):
                self.assertEqual(report._absolute_url(bad), "")

    def test_link_falls_back_to_plain_text(self):
        out = report._link("../relative.html", "Some Title")
        self.assertNotIn("<a", out)
        self.assertIn("Some Title", out)

    def test_paper_url_priority_doi_then_arxiv_then_pdf(self):
        self.assertEqual(
            report.paper_url({"doi": "10.1/x", "arxiv_id": "2501.1",
                              "pdf_url": "https://e/p.pdf"}),
            "https://doi.org/10.1/x")
        self.assertEqual(
            report.paper_url({"doi": "", "arxiv_id": "2501.00002"}),
            "https://arxiv.org/abs/2501.00002")
        self.assertEqual(
            report.paper_url({"pdf_url": "https://e/p.pdf"}),
            "https://e/p.pdf")
        self.assertEqual(report.paper_url({}), "")

    def test_doi_already_url_is_not_double_prefixed(self):
        url = report.paper_url({"doi": "https://doi.org/10.1/x"})
        self.assertEqual(url, "https://doi.org/10.1/x")
        self.assertNotIn("doi.org/https", url)

    def test_nan_fields_do_not_become_links(self):
        url = report.paper_url({"doi": "nan", "arxiv_id": "nan",
                                "pdf_url": "nan"})
        self.assertEqual(url, "")


class ReportPrintCssTests(unittest.TestCase):
    """브라우저 PDF 저장 품질을 좌우하는 print 규칙."""

    def setUp(self):
        self.out = report.build_report_html(
            papers=[{"title": "P", "doi": "10.1/x", "year": 2025}])

    def test_has_print_button_wired_to_window_print(self):
        self.assertIn("window.print()", self.out)
        self.assertIn("citedbyPrint()", self.out)

    def test_button_is_hidden_in_print(self):
        self.assertIn("no-print", self.out)
        self.assertRegex(self.out, r"\.no-print\{display:none")

    def test_page_and_color_rules_present(self):
        self.assertIn("@page", self.out)
        self.assertIn("@media print", self.out)
        # 표 헤더/칩 배경이 인쇄에서 날아가지 않아야 한다
        self.assertIn("print-color-adjust:exact", self.out)

    def test_cards_avoid_page_breaks(self):
        self.assertIn("break-inside:avoid", self.out)

    def test_does_not_append_url_text_after_links(self):
        """`a::after{content:attr(href)}` 트릭 금지 — 링크 주석이 이미 보존된다."""
        self.assertNotIn("attr(href)", self.out)

    def test_report_is_self_contained(self):
        """외부 자원 참조 0 — 파일로 저장해도 그대로 열려야 한다."""
        self.assertNotIn("<link", self.out)
        self.assertNotIn("<script src", self.out)
        self.assertNotIn("@import", self.out)


class ReportRenderTests(unittest.TestCase):
    def test_escapes_html_in_untrusted_fields(self):
        out = report.build_report_html(papers=[{
            "title": "<script>alert(1)</script>",
            "journal": 'J" onload="x',
        }])
        self.assertNotIn("<script>alert(1)</script>", out)
        self.assertIn("&lt;script&gt;", out)
        self.assertNotIn('onload="x', out)

    def test_renders_5w1h_summary_table(self):
        out = report.build_report_html(papers=[{
            "title": "P", "doi": "10.1/x",
            "summary": {"what": "무엇", "how": "어떻게",
                        "result": "결과", "relevance": "관련"},
        }])
        self.assertIn("무엇", out)
        self.assertIn("어떻게", out)
        self.assertIn('class="sum"', out)

    def test_missing_summary_omits_table(self):
        out = report.build_report_html(papers=[{"title": "P"}])
        self.assertNotIn('class="sum"', out)

    def test_empty_paper_list_is_handled(self):
        out = report.build_report_html(papers=[])
        self.assertIn("인용논문이 없습니다", out)
        self.assertTrue(out.startswith("<!DOCTYPE html>"))

    def test_english_locale(self):
        out = report.build_report_html(papers=[], lang="en")
        self.assertIn("Citing Paper Analysis Report", out)
        self.assertIn('lang="en"', out)

    def test_source_counts_and_year_range_chips(self):
        out = report.build_report_html(
            papers=[{"title": "A", "year": 2020}, {"title": "B", "year": 2025}],
            source_counts={"openalex": 12, "scopus": 3})
        self.assertIn("2020–2025", out)
        self.assertIn("openalex 12", out)

    def test_deterministic_with_fixed_timestamp(self):
        stamp = datetime(2026, 7, 25, 9, 30)
        a = report.build_report_html(papers=[{"title": "X"}], generated_at=stamp)
        b = report.build_report_html(papers=[{"title": "X"}], generated_at=stamp)
        self.assertEqual(a, b)
        self.assertIn("2026-07-25 09:30", a)


class ReportCsvTests(unittest.TestCase):
    def test_csv_has_header_and_url_column(self):
        csv_text = report.papers_to_csv([
            {"title": "A", "doi": "10.1/a"},
            {"title": "B", "arxiv_id": "2501.1"},
        ])
        lines = csv_text.strip().splitlines()
        self.assertIn("url", lines[0])
        self.assertIn("https://doi.org/10.1/a", csv_text)
        self.assertIn("https://arxiv.org/abs/2501.1", csv_text)
        self.assertEqual(len(lines), 3)          # header + 2 rows

    def test_csv_includes_originality_when_present(self):
        csv_text = report.papers_to_csv([{"title": "A", "originality": "novel"}])
        self.assertIn("originality", csv_text.splitlines()[0])
        self.assertIn("novel", csv_text)

    def test_csv_ignores_unknown_keys(self):
        csv_text = report.papers_to_csv([{"title": "A", "zzz_unknown": "drop"}])
        self.assertNotIn("zzz_unknown", csv_text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
