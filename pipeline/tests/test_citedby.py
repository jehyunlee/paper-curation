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

import json
import os
import re
import subprocess
import tempfile
import sys
import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

PIPELINE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE_DIR))

from lib.citedby import analysis  # noqa: E402
from lib.citedby import citing  # noqa: E402
from lib.citedby import report  # noqa: E402
from lib.citedby import scopus  # noqa: E402
from lib.citedby import topic_filter  # noqa: E402
from lib.citedby import zotero_links  # noqa: E402


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

    def test_citation_counts_are_kept_per_source_not_merged(self):
        """피인용수는 max() 로 뭉개지 않는다 — 소스마다 세는 우주가 다르다.

        실측: 같은 논문이 Crossref 47 / OpenAlex 52 / S2 104. max 를 취하면
        어느 소스에서도 나오지 않은 숫자가 된다.
        """
        out = self._merge([
            self._row(title="P", source="scopus", citations_scopus=3),
            self._row(title="P", source="openalex", citations_openalex=17),
        ])
        row = out.iloc[0]
        self.assertEqual(int(row["citations_scopus"]), 3)
        self.assertEqual(int(row["citations_openalex"]), 17)
        # 대표값은 OpenAlex 선호 (커버리지 최대 + 백분위 제공)
        self.assertEqual(int(row["citationCount"]), 17)
        self.assertEqual(row["citations_source"], "openalex")

    def test_zero_citations_is_a_real_value_not_missing(self):
        """최근 논문의 피인용 0 은 정상값 — 다른 소스 값으로 덮으면 안 된다."""
        out = self._merge([
            self._row(title="P", source="openalex", citations_openalex=0),
        ])
        self.assertEqual(int(out.iloc[0]["citationCount"]), 0)
        self.assertEqual(out.iloc[0]["citations_source"], "openalex")

    def test_bibliographic_field_follows_source_priority(self):
        """서지는 Scopus > Crossref > OpenAlex > S2."""
        out = self._merge([
            self._row(title="P", source="semanticscholar", volume="S2VOL"),
            self._row(title="P", source="openalex", volume="OAVOL"),
        ])
        self.assertEqual(out.iloc[0]["volume"], "OAVOL")

    def test_abstract_uses_field_authority_over_global_priority(self):
        """초록만은 Crossref 를 뒤로 민다 (실측 커버리지 7/25 vs 13/25)."""
        self.assertLess(citing._field_rank("abstract", "openalex"),
                        citing._field_rank("abstract", "crossref"))
        # 서지 필드는 반대 — Crossref 가 앞선다
        self.assertLess(citing._field_rank("volume", "crossref"),
                        citing._field_rank("volume", "openalex"))

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
        for v in (None, "", "   ", "nan", "None"):
            with self.subTest(v=v):
                self.assertTrue(citing._is_empty(v))

    def test_non_empty_values(self):
        for v in ("text", 5, "10.1/x", 1.5, "0", 0, "0.0"):
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
    def test_available_false_only_when_no_key_anywhere(self):
        """키가 어디에도 없을 때만 False. cfg 부재만으로는 False 가 아니다.

        실환경의 SCOPUS_API_KEY 가 새어들면 이 검증이 무의미해지므로 env 를
        비운다.
        """
        scopus._api_keys = None
        with patch.dict(os.environ, {}, clear=True), \
             patch.object(scopus, "config_path", return_value=None), \
             patch.object(scopus, "_keys_from_config_json", return_value=[]):
            ok, reason = scopus.available()
        scopus._api_keys = None
        self.assertFalse(ok)
        self.assertIn("SCOPUS_API_KEY", reason)

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


class JsonParsingTests(unittest.TestCase):
    """LLM 응답은 코드펜스/군더더기를 달고 오는 일이 잦다."""

    def test_plain_json(self):
        self.assertEqual(topic_filter._parse_json('{"a": 1}'), {"a": 1})

    def test_fenced_json(self):
        self.assertEqual(
            topic_filter._parse_json('```json\n{"a": 1}\n```'), {"a": 1})

    def test_json_embedded_in_prose(self):
        self.assertEqual(
            topic_filter._parse_json('Sure!\n{"a": 1}\nHope that helps.'),
            {"a": 1})

    def test_unparseable_returns_none(self):
        for bad in ("", "not json at all", "{broken"):
            with self.subTest(bad=bad):
                self.assertIsNone(topic_filter._parse_json(bad))


class KeyResolutionTests(unittest.TestCase):
    def test_env_keys_are_picked_up(self):
        with patch.dict(os.environ, {"ANTHROPIC_API_KEY": "sk-ant-1",
                                     "GOOGLE_API_KEY": "AIza-1",
                                     "OPENAI_API_KEY": "sk-2"}, clear=False):
            keys = topic_filter.resolve_keys()
        self.assertEqual(keys["anthropic"], "sk-ant-1")
        self.assertEqual(keys["google"], "AIza-1")
        self.assertEqual(keys["openai"], "sk-2")

    def test_alias_env_names(self):
        with patch.dict(os.environ, {"CLAUDE_API_KEY": "sk-ant-alias"},
                        clear=True):
            keys = topic_filter.resolve_keys()
        self.assertEqual(keys.get("anthropic"), "sk-ant-alias")


class LlmCascadeTests(unittest.TestCase):
    """Anthropic → Google → OpenAI 순서와 폴백."""

    def test_uses_first_available_provider(self):
        calls = []

        def anth(key, model, prompt, mt):
            calls.append("anthropic")
            return '{"ok": 1}'

        with patch.dict(topic_filter._CALLERS, {"anthropic": anth}, clear=False):
            out = topic_filter.llm_json("p", keys={"anthropic": "k",
                                                   "openai": "k2"})
        self.assertEqual(out, {"ok": 1})
        self.assertEqual(calls, ["anthropic"])

    def test_falls_through_on_exception(self):
        def boom(key, model, prompt, mt):
            raise RuntimeError("429")

        def ok(key, model, prompt, mt):
            return '{"ok": 2}'

        with patch.dict(topic_filter._CALLERS,
                        {"anthropic": boom, "google": ok}, clear=False):
            out = topic_filter.llm_json("p", keys={"anthropic": "k",
                                                   "google": "k"})
        self.assertEqual(out, {"ok": 2})

    def test_falls_through_on_unparseable_json(self):
        with patch.dict(topic_filter._CALLERS,
                        {"anthropic": lambda *a: "garbage",
                         "google": lambda *a: '{"ok": 3}'}, clear=False):
            out = topic_filter.llm_json("p", keys={"anthropic": "k",
                                                   "google": "k"})
        self.assertEqual(out, {"ok": 3})

    def test_no_keys_returns_none(self):
        self.assertIsNone(topic_filter.llm_json("p", keys={}))

    def test_provider_without_key_is_skipped(self):
        called = []
        with patch.dict(topic_filter._CALLERS,
                        {"anthropic": lambda *a: called.append("a") or "{}",
                         "google": lambda *a: called.append("g") or '{"ok":1}'},
                        clear=False):
            topic_filter.llm_json("p", keys={"google": "k"})
        self.assertEqual(called, ["g"])


class GeminiSdkMigrationTests(unittest.TestCase):
    """구 SDK(google.generativeai) 잔재 회귀 방지.

    paper-curation 표준은 `google-genai` 다. 원본 scisci 는 둘을 혼용했고,
    구 SDK 가 py312 에 딸려 들어오면 충돌한다.
    """

    # 문서/주석은 "무엇을 제거했는지" 설명하며 옛 이름을 언급한다. 실제 import
    # 문만 잡도록 좁힌다 — 그렇지 않으면 설명문에 걸려 거짓 양성이 난다.
    LEGACY_SDK_RE = re.compile(
        r"^\s*(?:import\s+google\.generativeai|from\s+google\.generativeai\b)",
        re.MULTILINE)
    MYAPIKEY_RE = re.compile(
        r"^\s*(?:import\s+MyAPIKEY|from\s+MyAPIKEY\b)", re.MULTILINE)

    def test_source_does_not_import_legacy_sdk(self):
        src = Path(topic_filter.__file__).read_text(encoding="utf-8")
        self.assertIsNone(self.LEGACY_SDK_RE.search(src),
                          "deprecated google.generativeai 를 import 하고 있다")
        self.assertIn("from google import genai", src)

    def test_no_myapikey_import_anywhere(self):
        pkg = Path(topic_filter.__file__).parent
        for py in sorted(pkg.glob("*.py")):
            with self.subTest(file=py.name):
                self.assertIsNone(
                    self.MYAPIKEY_RE.search(py.read_text(encoding="utf-8")),
                    "개인 로컬 모듈 MyAPIKEY 의존이 남아 있다")


class BatchResultMappingTests(unittest.TestCase):
    """LLM 이 요청한 개수와 다르게 돌려줘도 흘려보내지 않는다."""

    def test_exact_count_maps_in_order(self):
        slots = [None] * 3
        topic_filter._apply_batch_results(
            slots, [{"v": 1}, {"v": 2}, {"v": 3}], 0, 3, lambda i: i["v"])
        self.assertEqual(slots, [1, 2, 3])

    def test_count_mismatch_falls_back_to_paper_index(self):
        slots = [None] * 3
        topic_filter._apply_batch_results(
            slots, [{"paper": 3, "v": 9}], 0, 3, lambda i: i["v"])
        self.assertEqual(slots, [None, None, 9])

    def test_out_of_range_index_is_ignored(self):
        slots = [None] * 2
        topic_filter._apply_batch_results(
            slots, [{"paper": 99, "v": 1}], 0, 2, lambda i: i["v"])
        self.assertEqual(slots, [None, None])


class TopicFilterTests(unittest.TestCase):
    @staticmethod
    def _papers(n):
        return [{"title": f"P{i}", "abstract": f"abs {i}"} for i in range(n)]

    def test_selects_only_relevant_and_attaches_reason(self):
        payload = {"results": [
            {"paper": 1, "relevant": True, "reason": "직접 관련"},
            {"paper": 2, "relevant": False, "reason": "무관"},
        ]}
        with patch.object(topic_filter, "llm_json", return_value=payload):
            out = topic_filter.filter_by_topic(self._papers(2), "융합연구")
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0]["title"], "P0")
        self.assertEqual(out[0]["topic_reason"], "직접 관련")

    def test_empty_topic_returns_nothing(self):
        self.assertEqual(topic_filter.filter_by_topic(self._papers(3), "  "), [])

    def test_llm_failure_drops_batch_without_raising(self):
        with patch.object(topic_filter, "llm_json", return_value=None):
            out = topic_filter.filter_by_topic(self._papers(3), "t")
        self.assertEqual(out, [])

    def test_batches_are_chunked(self):
        seen = []

        def fake(prompt, **kw):
            seen.append(prompt)
            return {"results": []}

        with patch.object(topic_filter, "llm_json", side_effect=fake):
            topic_filter.filter_by_topic(
                self._papers(topic_filter.FILTER_BATCH_SIZE + 1), "t")
        self.assertEqual(len(seen), 2)

    def test_does_not_mutate_input(self):
        payload = {"results": [{"paper": 1, "relevant": True, "reason": "r"}]}
        papers = self._papers(1)
        with patch.object(topic_filter, "llm_json", return_value=payload):
            topic_filter.filter_by_topic(papers, "t")
        self.assertNotIn("topic_reason", papers[0])


class SummaryTests(unittest.TestCase):
    def test_attaches_5w1h_summary(self):
        payload = {"results": [{"paper": 1, "what": "W", "how": "H",
                                "result": "R", "relevance": "V"}]}
        with patch.object(topic_filter, "llm_json", return_value=payload):
            out = topic_filter.generate_summaries([{"title": "P"}], "t")
        self.assertEqual(out[0]["summary"]["what"], "W")
        self.assertEqual(out[0]["summary"]["relevance"], "V")

    def test_failure_leaves_paper_without_summary(self):
        with patch.object(topic_filter, "llm_json", return_value=None):
            out = topic_filter.generate_summaries([{"title": "P"}], "t")
        self.assertNotIn("summary", out[0])

    def test_all_empty_fields_are_not_attached(self):
        payload = {"results": [{"paper": 1, "what": "", "how": "",
                                "result": "", "relevance": ""}]}
        with patch.object(topic_filter, "llm_json", return_value=payload):
            out = topic_filter.generate_summaries([{"title": "P"}], "t")
        self.assertNotIn("summary", out[0])


class OriginalityAdapterTests(unittest.TestCase):
    """기존 originality_extractor 재사용 계약."""

    def test_rule_based_hit_skips_llm(self):
        papers = [{"title": "P", "abstract": "We propose a novel method."}]
        with patch.object(analysis, "_emit", return_value=lambda *a, **k: None):
            with patch("lib.originality_extractor._extract_rule_based",
                       return_value="We propose a novel method."), \
                 patch("lib.originality_extractor._llm_fallback") as llm:
                out = analysis.extract_originality_for_papers(papers)
        llm.assert_not_called()
        self.assertEqual(out[0]["originality_source"], "rule_base")

    def test_llm_fallback_only_for_misses(self):
        papers = [{"title": "A", "abstract": "hit"},
                  {"title": "B", "abstract": "miss"}]

        def rule(text, triggers):
            return "found" if text == "hit" else ""

        with patch("lib.originality_extractor._extract_rule_based",
                   side_effect=rule), \
             patch("lib.originality_extractor._llm_fallback",
                   return_value=("llm text", [])) as llm, \
             patch("lib.originality_extractor._update_triggers", return_value=0):
            out = analysis.extract_originality_for_papers(papers)
        self.assertEqual(llm.call_count, 1)
        self.assertEqual(out[0]["originality_source"], "rule_base")
        self.assertEqual(out[1]["originality_source"], "llm")

    def test_use_llm_false_skips_fallback(self):
        with patch("lib.originality_extractor._extract_rule_based",
                   return_value=""), \
             patch("lib.originality_extractor._llm_fallback") as llm:
            out = analysis.extract_originality_for_papers(
                [{"title": "P", "abstract": "x"}], use_llm=False)
        llm.assert_not_called()
        self.assertEqual(out[0]["originality"], "")

    def test_empty_abstract_is_skipped(self):
        with patch("lib.originality_extractor._extract_rule_based") as rule:
            out = analysis.extract_originality_for_papers(
                [{"title": "P", "abstract": "  "}])
        rule.assert_not_called()
        self.assertEqual(out[0]["originality"], "")

    def test_llm_exception_does_not_kill_run(self):
        with patch("lib.originality_extractor._extract_rule_based",
                   return_value=""), \
             patch("lib.originality_extractor._llm_fallback",
                   side_effect=RuntimeError("boom")):
            out = analysis.extract_originality_for_papers(
                [{"title": "P", "abstract": "x"}])
        self.assertEqual(out[0]["originality"], "")

    def test_does_not_mutate_input(self):
        papers = [{"title": "P", "abstract": "x"}]
        with patch("lib.originality_extractor._extract_rule_based",
                   return_value="orig"):
            analysis.extract_originality_for_papers(papers)
        self.assertNotIn("originality", papers[0])


class AnalysisOrchestrationTests(unittest.TestCase):
    def test_blank_doi_raises(self):
        with self.assertRaises(ValueError):
            analysis.run_citing_analysis("   ")

    def test_topic_analysis_passthrough_when_no_topic(self):
        """주제가 없으면 **필터·5W1H 는** 돌지 않는다.

        컬렉션 추천은 주제와 무관하게 별도로 도는 기능이라, 여기서는 꺼서
        필터 경로만 검증한다.
        """
        papers = [{"title": "A", "doi": "10.1/a"}]
        with patch.object(topic_filter, "llm_json") as llm:
            out = analysis.run_topic_analysis(papers, topic="",
                                              suggest_collections=False)
        llm.assert_not_called()
        self.assertEqual(out["matched"], 1)
        self.assertIn("<!DOCTYPE html>", out["report_html"])

    def test_collections_suggested_even_without_topic(self):
        """주제 미지정이어도 컬렉션 추천은 돈다 — Unfiled 를 줄이는 게 목적."""
        papers = [{"title": "A", "doi": "10.1/a"}]
        from lib.citedby import collections as C
        with patch.object(C, "recommend_collections",
                          side_effect=lambda p, **k: p) as rec:
            analysis.run_topic_analysis(papers, topic="",
                                        suggest_collections=True)
        rec.assert_called_once()

    def test_topic_analysis_reports_matched_over_total(self):
        papers = [{"title": f"P{i}"} for i in range(3)]
        payload = {"results": [{"paper": 1, "relevant": True, "reason": "r"},
                               {"paper": 2, "relevant": False, "reason": ""},
                               {"paper": 3, "relevant": False, "reason": ""}]}
        with patch.object(topic_filter, "llm_json", return_value=payload):
            out = analysis.run_topic_analysis(papers, topic="t",
                                              make_summaries=False)
        self.assertEqual((out["matched"], out["total"]), (1, 3))

    def test_full_pipeline_emits_events_and_builds_report(self):
        import pandas as pd

        df = pd.DataFrame([{**{c: "" for c in citing.CITING_COLUMNS},
                            "title": "Citing One", "doi": "10.1/c",
                            "abstract": "We propose X.", "citationCount": 5,
                            "source": "openalex"}])
        events = []

        with patch("lib.citedby.citing.fetch_all_citing_papers",
                   return_value=(df, {"openalex": 1})), \
             patch.object(analysis, "fetch_paper_metadata",
                          return_value={"title": "Seed", "doi": "10.1/seed"}), \
             patch("lib.originality_extractor._extract_rule_based",
                   return_value="We propose X."), \
             patch.object(topic_filter, "llm_json", return_value={"results": [
                 {"paper": 1, "relevant": True, "reason": "직접 관련"}]}):
            out = analysis.run_citedby(
                "https://doi.org/10.1/seed", sources=["openalex"], topic="AI",
                on_event=lambda phase, msg, cur=0, tot=0: events.append(phase))

        self.assertEqual(out["doi"], "10.1/seed")
        self.assertEqual(out["matched"], 1)
        self.assertIn("Citing One", out["report_html"])
        self.assertIn("https://doi.org/10.1/c", out["report_html"])
        self.assertIn("title", out["csv"])
        self.assertIn("done", events)
        self.assertGreaterEqual(out["elapsed_sec"], 0)


class ZoteroKeyNormalizationTests(unittest.TestCase):
    def test_doi_key_strips_url_prefix_and_cases(self):
        for raw in ("https://doi.org/10.1/ABC", "http://dx.doi.org/10.1/abc",
                    "  10.1/AbC  "):
            with self.subTest(raw=raw):
                self.assertEqual(zotero_links.normalize_doi_key(raw), "10.1/abc")

    def test_doi_key_rejects_empty_markers(self):
        for raw in ("", "  ", "nan", "None"):
            with self.subTest(raw=raw):
                self.assertEqual(zotero_links.normalize_doi_key(raw), "")

    def test_title_key_is_alphanumeric_lower(self):
        self.assertEqual(
            zotero_links.normalize_title_key("Towards Discovery, with AI!"),
            "towardsdiscoverywithai")

    def test_title_key_matches_across_punctuation_variants(self):
        a = zotero_links.normalize_title_key("Deep Learning: A Review")
        b = zotero_links.normalize_title_key("deep learning - a review.")
        self.assertEqual(a, b)

    def test_title_key_truncates_long_titles(self):
        self.assertLessEqual(
            len(zotero_links.normalize_title_key("word " * 60)), 60)


class ZoteroIndexTests(unittest.TestCase):
    def _index(self):
        return zotero_links.ZoteroIndex(by_doi={"10.1/a": "KEYA"},
                                        by_title={"papertitleb": "KEYB"})

    def test_doi_match_wins_over_title(self):
        self.assertEqual(
            self._index().lookup({"doi": "10.1/a", "title": "Paper Title B"}),
            "KEYA")

    def test_title_fallback_when_no_doi(self):
        self.assertEqual(
            self._index().lookup({"doi": "", "title": "Paper Title B"}), "KEYB")

    def test_miss_returns_empty(self):
        self.assertEqual(
            self._index().lookup({"doi": "10.9/z", "title": "Nope"}), "")

    def test_url_builds_open_pdf_protocol(self):
        self.assertEqual(self._index().url({"doi": "10.1/a"}),
                         "zotero://open-pdf/library/items/KEYA")

    def test_url_empty_on_miss(self):
        self.assertEqual(self._index().url({"doi": "10.9/z"}), "")

    def test_item_key_fallback_when_no_attachment(self):
        """PDF 첨부가 없으면 서지정보(zotero://select)로 폴백한다."""
        idx = zotero_links.ZoteroIndex(item_by_doi={"10.1/b": "ITEMB"})
        self.assertEqual(idx.url({"doi": "10.1/b"}),
                         "zotero://select/library/items/ITEMB")
        self.assertEqual(idx.url_kind({"doi": "10.1/b"}), "item")

    def test_attachment_wins_over_item_key(self):
        idx = zotero_links.ZoteroIndex(by_doi={"10.1/a": "ATT"},
                                       item_by_doi={"10.1/a": "ITEM"})
        self.assertEqual(idx.url({"doi": "10.1/a"}),
                         "zotero://open-pdf/library/items/ATT")
        self.assertEqual(idx.url_kind({"doi": "10.1/a"}), "pdf")

    def test_url_kind_empty_on_miss(self):
        self.assertEqual(self._index().url_kind({"doi": "10.9/z"}), "")

    def test_empty_index_is_falsy_and_safe(self):
        empty = zotero_links.ZoteroIndex()
        self.assertFalse(empty)
        self.assertEqual(empty.url({"doi": "10.1/a"}), "")


class ZoteroIndexLoadTests(unittest.TestCase):
    def test_missing_files_return_empty_index_without_raising(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertFalse(zotero_links.load_zotero_index(tmp))

    def test_joins_papers_index_with_zotero_keys_on_slug(self):
        with tempfile.TemporaryDirectory() as tmp:
            docs = Path(tmp)
            (docs / "papers").mkdir()
            (docs / "_zotero_keys.json").write_text(json.dumps({
                "001_Alpha": "ATTACH1",
                "002_Beta": "ATTACH2",
                "999_Orphan": "ATTACH9",      # papers_index 에 없음 → 무시
            }), encoding="utf-8")
            (docs / "papers" / "_papers_index.json").write_text(json.dumps([
                {"slug": "001_Alpha", "doi": "10.1/ALPHA", "title": "Alpha One"},
                {"slug": "002_Beta", "doi": "", "title": "Beta Two"},
                {"slug": "003_NoKey", "doi": "10.1/c", "title": "Gamma"},
            ]), encoding="utf-8")
            idx = zotero_links.load_zotero_index(docs)

        self.assertEqual(idx.by_doi.get("10.1/alpha"), "ATTACH1")
        self.assertEqual(idx.by_title.get("alphaone"), "ATTACH1")
        self.assertEqual(idx.by_title.get("betatwo"), "ATTACH2")
        self.assertNotIn("10.1/c", idx.by_doi)   # Zotero 키 없는 논문은 제외

    def test_corrupt_json_returns_empty_index(self):
        with tempfile.TemporaryDirectory() as tmp:
            docs = Path(tmp)
            (docs / "papers").mkdir()
            (docs / "_zotero_keys.json").write_text("{broken", encoding="utf-8")
            (docs / "papers" / "_papers_index.json").write_text(
                "[]", encoding="utf-8")
            self.assertFalse(zotero_links.load_zotero_index(docs))


class ReportZoteroLinkTests(unittest.TestCase):
    """정적 HTML 문서에서 Zotero PDF 바로열기 링크."""

    def setUp(self):
        self.idx = zotero_links.ZoteroIndex(by_doi={"10.1/a": "KEYA"})

    def test_zotero_scheme_passes_absolute_url_guard(self):
        self.assertEqual(
            report._absolute_url("zotero://open-pdf/library/items/K"),
            "zotero://open-pdf/library/items/K")

    def test_other_schemes_still_blocked(self):
        for bad in ("javascript:alert(1)", "file:///etc/passwd",
                    "../rel.html", "data:text/html,x"):
            with self.subTest(bad=bad):
                self.assertEqual(report._absolute_url(bad), "")

    def test_library_hit_renders_zotero_link(self):
        out = report.build_report_html(
            papers=[{"title": "In Library", "doi": "10.1/a"}],
            zotero_index=self.idx)
        self.assertIn("zotero://open-pdf/library/items/KEYA", out)

    def test_library_miss_falls_back_to_external_link(self):
        out = report.build_report_html(
            papers=[{"title": "Not In Library", "doi": "10.9/z"}],
            zotero_index=self.idx)
        self.assertNotIn("zotero://", out)
        self.assertIn("https://doi.org/10.9/z", out)

    def test_no_index_means_no_zotero_links(self):
        out = report.build_report_html(
            papers=[{"title": "X", "doi": "10.1/a"}], zotero_index=None)
        self.assertNotIn("zotero://", out)

    def test_seed_paper_gets_zotero_link(self):
        out = report.build_report_html(
            papers=[], paper_info={"title": "Seed", "doi": "10.1/a"},
            zotero_index=self.idx)
        self.assertIn("zotero://open-pdf/library/items/KEYA", out)

    def test_all_hrefs_remain_absolute_with_zotero(self):
        out = report.build_report_html(
            papers=[{"title": "A", "doi": "10.1/a"},
                    {"title": "B", "doi": "10.9/z"}],
            zotero_index=self.idx)
        for href in re.findall(r'href="([^"]*)"', out):
            with self.subTest(href=href):
                self.assertRegex(href, r"^(https?|zotero)://")

    def test_input_papers_are_not_mutated(self):
        papers = [{"title": "A", "doi": "10.1/a"}]
        report.build_report_html(papers=papers, zotero_index=self.idx)
        self.assertNotIn("_zotero_url", papers[0])


class ScopusKeyResolutionTests(unittest.TestCase):
    """키 탐색 경로 회귀 방지.

    실제 버그: `SCOPUS_API_KEY` 환경변수가 있는데도 코드가 pybliometrics.cfg
    파일만 봐서 "설정 없음" 으로 판정했고, 거기서 "기관망 밖" 이라고 오진까지
    했다. 실제로는 Search API 가 200 으로 잘 붙는 상태였다.
    """

    def setUp(self):
        scopus._api_keys = None
        scopus._key_origin = ""

    tearDown = setUp

    def test_env_var_is_used(self):
        with patch.dict(os.environ, {"SCOPUS_API_KEY": "K1"}, clear=True):
            self.assertEqual(scopus.get_api_keys(), ["K1"])
            self.assertEqual(scopus.key_origin(), "env:SCOPUS_API_KEY")

    def test_elsevier_alias_env_var(self):
        with patch.dict(os.environ, {"ELSEVIER_API_KEY": "K2"}, clear=True):
            self.assertEqual(scopus.get_api_keys(), ["K2"])

    def test_comma_separated_keys(self):
        with patch.dict(os.environ, {"SCOPUS_API_KEY": "A,B,C"}, clear=True):
            self.assertEqual(scopus.get_api_keys(), ["A", "B", "C"])

    def test_available_true_with_env_key_and_no_cfg(self):
        """cfg 파일이 없어도 환경변수만 있으면 사용 가능해야 한다."""
        with patch.dict(os.environ, {"SCOPUS_API_KEY": "K"}, clear=True), \
             patch.object(scopus, "config_path", return_value=None):
            ok, reason = scopus.available()
        self.assertTrue(ok, reason)

    def test_missing_key_everywhere_raises(self):
        with patch.dict(os.environ, {}, clear=True), \
             patch.object(scopus, "config_path", return_value=None), \
             patch.object(scopus, "_keys_from_config_json", return_value=[]):
            with self.assertRaises(FileNotFoundError):
                scopus.get_api_keys()

    def test_headers_carry_key_and_optional_inst_token(self):
        with patch.dict(os.environ, {"SCOPUS_API_KEY": "K"}, clear=True), \
             patch.object(scopus, "inst_token", return_value=""):
            h = scopus.headers()
        self.assertEqual(h["X-ELS-APIKey"], "K")
        self.assertNotIn("X-ELS-Insttoken", h)

        scopus._api_keys = None
        with patch.dict(os.environ, {"SCOPUS_API_KEY": "K"}, clear=True), \
             patch.object(scopus, "inst_token", return_value="TOK"):
            h = scopus.headers()
        self.assertEqual(h["X-ELS-Insttoken"], "TOK")

    def test_probe_reports_tier_per_endpoint(self):
        """키가 있어도 엔드포인트별 권한이 다르다 — 실측 200/400/401."""
        from unittest.mock import MagicMock
        import requests as _rq

        def fake_get(url, headers=None, params=None, timeout=None):
            r = MagicMock()
            if "abstract" in url:
                r.status_code = 401
            elif "REFEID" in str((params or {}).get("query", "")):
                r.status_code = 400
            else:
                r.status_code = 200
                r.json.return_value = {
                    "search-results": {"entry": [{"eid": "2-s2.0-1"}]}}
            return r

        with patch.dict(os.environ, {"SCOPUS_API_KEY": "K"}, clear=True), \
             patch.object(_rq, "get", side_effect=fake_get):
            p = scopus.probe()
        self.assertTrue(p["search"])
        self.assertFalse(p["citing"])
        self.assertFalse(p["references"])
        self.assertEqual(p["detail"]["citing"], 400)
        self.assertEqual(p["detail"]["references"], 401)


class MetadataCompletenessTests(unittest.TestCase):
    """서지 필드 누락 회귀 방지.

    실제 버그: OpenAlex 파서가 volume/pages 를 빈 문자열로 **하드코딩**하고
    `select` 에 `biblio` 를 넣지 않아 권/호/페이지가 통째로 비었다. 날짜도
    완전한 ISO 를 연/월로 잘라 Zotero 에 "2025" 만 들어갔다.
    """

    WORK = {
        "display_name": "What counts as plagiarism?",
        "publication_date": "2025-08-20",
        "doi": "https://doi.org/10.1038/d41586-025-02616-5",
        "biblio": {"volume": "644", "issue": "8077",
                   "first_page": "598", "last_page": "600"},
        "primary_location": {
            "source": {"display_name": "Nature",
                       "issn": ["0028-0836", "1476-4687"],
                       "host_organization_name": "Nature Portfolio"},
        },
        "authorships": [{"author": {"display_name": "Ananya"}}],
        "cited_by_count": 3,
        "language": "en",
        "type": "article",
    }

    def test_openalex_select_requests_biblio(self):
        """select 에서 빠지면 응답에 아예 안 담긴다 — 파서와 짝을 맞춘다."""
        self.assertIn("biblio", citing._OPENALEX_SELECT)
        self.assertIn("language", citing._OPENALEX_SELECT)
        self.assertIn("citation_normalized_percentile", citing._OPENALEX_SELECT)

    def test_select_covers_every_field_the_parser_reads(self):
        """`select` 누락은 조용한 데이터 손실이다 — 실제로 두 번 당했다.

        `biblio` 누락으로 권/호/페이지가, `citation_normalized_percentile`
        누락으로 백분위가 통째로 비었다. 파서가 최상위에서 읽는 키가 select 에
        모두 들어있는지 기계적으로 확인한다.
        """
        import inspect
        import re as _re
        src = inspect.getsource(citing._parse_openalex_work)
        read = set(_re.findall(r'w\.get\(\s*"([a-z_]+)"', src))
        selected = set(citing._OPENALEX_SELECT.split(","))
        missing = sorted(read - selected)
        self.assertEqual(missing, [],
                         f"파서가 읽지만 select 에 없는 필드: {missing}")

    def test_parses_volume_issue_pages(self):
        rec = citing._parse_openalex_work(self.WORK)
        self.assertEqual(rec["volume"], "644")
        self.assertEqual(rec["issue"], "8077")
        self.assertEqual(rec["pages"], "598-600")

    def test_single_page_is_not_duplicated(self):
        w = {**self.WORK, "biblio": {"first_page": "42", "last_page": "42"}}
        self.assertEqual(citing._parse_openalex_work(w)["pages"], "42")

    def test_keeps_full_iso_date(self):
        """연/월로 잘라 버리면 Zotero Date 가 "2025" 로 남는다."""
        rec = citing._parse_openalex_work(self.WORK)
        self.assertEqual(rec["date"], "2025-08-20")
        self.assertEqual(rec["year"], 2025)
        self.assertEqual(rec["month"], 8)

    def test_parses_issn_publisher_language_type(self):
        rec = citing._parse_openalex_work(self.WORK)
        self.assertEqual(rec["issn"], "0028-0836; 1476-4687")
        self.assertEqual(rec["publisher"], "Nature Portfolio")
        self.assertEqual(rec["language"], "en")
        self.assertEqual(rec["item_type"], "article")

    def test_all_columns_present_in_parser_output(self):
        """스키마 드리프트 방지 — 컬럼을 빠뜨리면 병합에서 조용히 깨진다."""
        rec = citing._parse_openalex_work(self.WORK)
        missing = [c for c in citing.CITING_COLUMNS if c not in rec]
        self.assertEqual(missing, [], f"OpenAlex 파서 누락 컬럼: {missing}")


class CrossrefEnrichmentTests(unittest.TestCase):
    MSG = {
        "volume": "644", "issue": "8077", "page": "598-600",
        "ISSN": ["0028-0836", "1476-4687"],
        "publisher": "Springer Science and Business Media LLC",
        "language": "en", "type": "journal-article",
        "container-title": ["Nature"],
        "published": {"date-parts": [[2025, 8, 20]]},
        "author": [{"given": None, "family": "Ananya"}],
        "is-referenced-by-count": 47,
    }

    def _row(self, **over):
        base = {c: "" for c in citing.CITING_COLUMNS}
        base.update({"doi": "10.1/x", "title": "t", "citationCount": 0})
        base.update(over)
        return base

    def _run(self, row):
        import pandas as pd
        with patch.object(citing.requests, "get") as g:
            g.return_value.status_code = 200
            g.return_value.json.return_value = {"message": self.MSG}
            return citing.enrich_from_crossref(pd.DataFrame([row])).iloc[0]

    def test_date_parts_to_iso(self):
        self.assertEqual(citing._crossref_date(self.MSG), "2025-08-20")

    def test_date_parts_partial(self):
        self.assertEqual(
            citing._crossref_date({"issued": {"date-parts": [[2025, 8]]}}),
            "2025-08")
        self.assertEqual(
            citing._crossref_date({"issued": {"date-parts": [[2025]]}}), "2025")
        self.assertEqual(citing._crossref_date({}), "")

    def test_authors_given_family(self):
        self.assertEqual(citing._crossref_authors(self.MSG), "Ananya")
        self.assertEqual(
            citing._crossref_authors(
                {"author": [{"given": "Jane", "family": "Doe"}]}), "Jane Doe")

    def test_institutional_author_name(self):
        self.assertEqual(
            citing._crossref_authors({"author": [{"name": "WHO Group"}]}),
            "WHO Group")

    def test_fills_empty_bibliographic_fields(self):
        r = self._run(self._row(date="2025"))
        self.assertEqual(r["volume"], "644")
        self.assertEqual(r["issue"], "8077")
        self.assertEqual(r["pages"], "598-600")
        self.assertEqual(r["journal"], "Nature")

    def test_promotes_year_only_date_to_full_date(self):
        """이 보강의 주된 동기 — Zotero Date 가 "2025" 로 남던 문제."""
        r = self._run(self._row(date="2025"))
        self.assertEqual(r["date"], "2025-08-20")
        self.assertEqual(int(r["year"]), 2025)
        self.assertEqual(int(r["month"]), 8)

    def test_overrides_lower_authority_bibliographic_source(self):
        """Crossref 는 서지 2순위 — OpenAlex/S2 값을 덮는다."""
        r = self._run(self._row(source="openalex", volume="999",
                                journal="OA 저널", date="2025-01-02"))
        self.assertEqual(r["volume"], "644")
        self.assertEqual(r["journal"], "Nature")
        self.assertEqual(r["date"], "2025-01-02")   # 이미 완전한 날짜는 유지

    def test_does_not_override_scopus(self):
        """Scopus 는 서지 1순위 — Crossref 가 덮지 않는다."""
        r = self._run(self._row(source="scopus", volume="999",
                                journal="Scopus 저널", date="2025"))
        self.assertEqual(r["volume"], "999")
        self.assertEqual(r["journal"], "Scopus 저널")
        self.assertEqual(r["date"], "2025-08-20")   # 날짜는 정밀해지면 승격

    def test_does_not_override_abstract(self):
        """초록은 Crossref 가 최하위 — 기존 값을 건드리지 않는다."""
        msg = {**self.MSG, "abstract": "<jats:p>CR abstract</jats:p>"}
        import pandas as pd
        with patch.object(citing.requests, "get") as g:
            g.return_value.status_code = 200
            g.return_value.json.return_value = {"message": msg}
            row = self._row(source="openalex", abstract="OA 초록", date="2025")
            r = citing.enrich_from_crossref(pd.DataFrame([row])).iloc[0]
        self.assertEqual(r["abstract"], "OA 초록")

    def test_records_crossref_citation_count_separately(self):
        r = self._run(self._row(source="openalex", citations_openalex=52,
                                date="2025"))
        self.assertEqual(int(r["citations_crossref"]), 47)
        self.assertEqual(int(r["citations_openalex"]), 52)
        # 대표값은 OpenAlex 선호 — max(52,47) 같은 합성값이 아니다
        self.assertEqual(int(r["citationCount"]), 52)
        self.assertEqual(r["citations_source"], "openalex")
        self.assertTrue(r["citations_asof"])

    def test_skips_rows_that_need_nothing(self):
        row = self._row(date="2025-08-20", volume="644", pages="598-600")
        self.assertFalse(citing._needs_crossref(row))

    def test_skips_rows_without_doi(self):
        self.assertFalse(citing._needs_crossref(self._row(doi="")))

    def test_needs_enrichment_when_date_is_year_only(self):
        self.assertTrue(citing._needs_crossref(
            self._row(date="2025", volume="644", pages="1-2")))

    def test_network_failure_leaves_frame_unchanged(self):
        import pandas as pd
        row = self._row(date="2025")
        with patch.object(citing.requests, "get",
                          side_effect=RuntimeError("down")):
            r = citing.enrich_from_crossref(pd.DataFrame([row])).iloc[0]
        self.assertEqual(r["volume"], "")
        self.assertEqual(r["date"], "2025")

    def test_safe_set_promotes_dtype_on_conflict(self):
        """문자열 dtype 컬럼에 int 를 쓰면 pandas 가 던진다 (실제로 터졌다)."""
        import pandas as pd
        df = pd.DataFrame({"year": pd.array(["2025"], dtype="string")})
        citing._safe_set(df, 0, "year", 2026)
        self.assertEqual(df.at[0, "year"], 2026)


if __name__ == "__main__":
    unittest.main(verbosity=2)


class SpringerAbstractFallbackTests(unittest.TestCase):
    """폐쇄형 Springer Nature 논문의 초록 보강.

    실측 배경: 초록 결손 20편 중 SN 계열 8편이 OpenAlex/Crossref/S2/Scopus
    **전부**에서 실패했다(발행사가 재배포를 막는다). Springer Nature
    **Metadata** API 로는 8/8 회수됐다. OpenAccess API 키로는 401 이고,
    OpenAccess 는 비OA 에 404 라 하나도 못 메운다 — 별개 키가 필요하다.
    """

    def _frame(self, dois):
        import pandas as pd
        rows = []
        for d in dois:
            r = {c: "" for c in citing.CITING_COLUMNS}
            r.update({"doi": d, "title": "t", "abstract": "",
                      "source": "openalex"})
            rows.append(r)
        return pd.DataFrame(rows)

    def test_key_resolution_order(self):
        with patch.dict(os.environ, {"SPRINGER_META_API_KEY": "A"}, clear=True):
            self.assertEqual(citing.springer_meta_key(), "A")
        with patch.dict(os.environ, {"NATURESPRINTERMETA_API_KEY": "B"},
                        clear=True):
            self.assertEqual(citing.springer_meta_key(), "B")
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(citing.springer_meta_key(), "")

    def test_only_springer_prefixes_are_queried(self):
        """Elsevier/SSRN 에 헛요청을 보내지 않는다."""
        seen = []

        def fake_sn(doi, key):
            seen.append(doi)
            return "S" * 50

        with patch.dict(os.environ, {"SPRINGER_META_API_KEY": "K"}), \
             patch.object(citing.requests, "get") as g, \
             patch.object(citing, "_springer_abstract", side_effect=fake_sn):
            g.return_value.status_code = 404          # S2 는 전부 실패
            citing._fill_missing_abstracts_by_doi(
                self._frame(["10.1038/a", "10.1007/b",
                             "10.1016/c", "10.2139/ssrn.1"]))
        self.assertEqual(sorted(seen), ["10.1007/b", "10.1038/a"])

    def test_springer_fills_when_s2_fails(self):
        with patch.dict(os.environ, {"SPRINGER_META_API_KEY": "K"}), \
             patch.object(citing.requests, "get") as g, \
             patch.object(citing, "_springer_abstract",
                          return_value="Q" * 80):
            g.return_value.status_code = 404
            out = citing._fill_missing_abstracts_by_doi(
                self._frame(["10.1038/a"]))
        self.assertEqual(len(out.iloc[0]["abstract"]), 80)

    def test_s2_hit_skips_springer(self):
        """S2 가 이미 채웠으면 SN 을 부르지 않는다 (호출 예산)."""
        with patch.dict(os.environ, {"SPRINGER_META_API_KEY": "K"}), \
             patch.object(citing.requests, "get") as g, \
             patch.object(citing, "_springer_abstract") as sn:
            g.return_value.status_code = 200
            g.return_value.json.return_value = {"abstract": "Z" * 60}
            citing._fill_missing_abstracts_by_doi(self._frame(["10.1038/a"]))
        sn.assert_not_called()

    def test_no_key_is_a_noop(self):
        with patch.dict(os.environ, {}, clear=True), \
             patch.object(citing.requests, "get") as g, \
             patch.object(citing, "_springer_abstract") as sn:
            g.return_value.status_code = 404
            out = citing._fill_missing_abstracts_by_doi(
                self._frame(["10.1038/a"]))
        sn.assert_not_called()
        self.assertEqual(out.iloc[0]["abstract"], "")

    def test_abstract_shapes_are_normalised(self):
        """응답의 abstract 가 str / {p:...} / list 로 갈린다."""
        for payload, want in (
            ({"records": [{"abstract": "plain text " * 5}]}, True),
            ({"records": [{"abstract": {"p": "dict form " * 5}}]}, True),
            ({"records": [{"abstract": ["list ", "form " * 8]}]}, True),
            ({"records": [{"abstract": ""}]}, False),
            ({"records": []}, False),
        ):
            with self.subTest(payload=str(payload)[:40]):
                with patch.object(citing.requests, "get") as g:
                    g.return_value.status_code = 200
                    g.return_value.json.return_value = payload
                    got = citing._springer_abstract("10.1038/a", "K")
                self.assertEqual(bool(got), want)

    def test_http_error_is_swallowed(self):
        with patch.object(citing.requests, "get",
                          side_effect=RuntimeError("down")):
            self.assertEqual(citing._springer_abstract("10.1038/a", "K"), "")


class ThemeAnalysisTests(unittest.TestCase):
    """주제 미지정 시의 자동 군집 분석.

    부가 기능이므로 **어떤 실패도 리포트 생성을 막아선 안 된다** — 편수 부족,
    의존성 없음, 군집화 예외, 전량 미분류 모두 None 으로 조용히 빠진다.
    """

    def _papers(self, n=40, year=2025):
        return [{"title": f"Paper {i}", "abstract": "x" * 60,
                 "year": year, "citation_count": i}
                for i in range(n)]

    def test_below_threshold_returns_none(self):
        from lib.citedby import themes
        self.assertIsNone(themes.analyze_themes(self._papers(5), min_papers=30))

    def test_untitled_papers_are_dropped_from_count(self):
        from lib.citedby import themes
        papers = self._papers(29) + [{"title": "", "abstract": "y"}]
        self.assertIsNone(themes.analyze_themes(papers, min_papers=30))

    def test_missing_dependency_returns_none(self):
        from lib.citedby import themes
        with patch.dict("sys.modules", {"topic_modeling": None}):
            self.assertIsNone(
                themes.analyze_themes(self._papers(40), min_papers=30))

    def test_clustering_exception_returns_none(self):
        from lib.citedby import themes
        import types
        fake = types.SimpleNamespace(
            compute_embeddings=lambda t: (_ for _ in ()).throw(RuntimeError("x")),
            run_clustering=lambda *a, **k: None)
        with patch.dict("sys.modules", {"topic_modeling": fake}):
            self.assertIsNone(
                themes.analyze_themes(self._papers(40), min_papers=30))

    def test_all_outliers_returns_none(self):
        from lib.citedby import themes
        import types
        n = 40
        fake = types.SimpleNamespace(
            compute_embeddings=lambda t: (None, sorted(t)),
            run_clustering=lambda e, s, t, **k: ([-1] * n, None, {}, None))
        with patch.dict("sys.modules", {"topic_modeling": fake}):
            self.assertIsNone(
                themes.analyze_themes(self._papers(n), min_papers=30))

    def test_year_parsing_prefers_full_date(self):
        from lib.citedby import themes
        self.assertEqual(themes._year_of({"date": "2025-08-20"}), 2025)
        self.assertEqual(themes._year_of({"year": 2024}), 2024)
        self.assertIsNone(themes._year_of({"date": "", "year": ""}))

    def test_paper_text_prefers_abstract_then_originality(self):
        from lib.citedby import themes
        self.assertIn("ABS", themes._paper_text(
            {"title": "T", "abstract": "ABS", "originality": "ORIG"}))
        self.assertIn("ORIG", themes._paper_text(
            {"title": "T", "abstract": "", "originality": "ORIG"}))
        self.assertEqual(themes._paper_text(
            {"title": "T", "abstract": "", "originality": ""}), "T")

    def test_fallback_name_filters_stopwords(self):
        from lib.citedby import themes
        name = themes._fallback_name(["the", "and", "la", "agents",
                                      "discovery", "protein"])
        self.assertNotIn("the", name)
        self.assertIn("agents", name)

    def test_report_renders_theme_table(self):
        themes_data = {
            "clusters": [{"id": 0, "name": "LLM 에이전트", "keywords": ["agent"],
                          "count": 3, "citations": 42,
                          "years": {2024: 1, 2025: 2}, "papers": []}],
            "years": [2024, 2025], "outliers": 1, "total": 4,
        }
        out = report.build_report_html(
            papers=[{"title": "P", "doi": "10.1/a"}], themes=themes_data)
        self.assertIn("인용 주제 분포", out)
        self.assertIn("LLM 에이전트", out)
        self.assertIn("미분류", out)

    def test_report_without_themes_has_no_section(self):
        out = report.build_report_html(
            papers=[{"title": "P", "doi": "10.1/a"}], themes=None)
        self.assertNotIn("인용 주제 분포", out)

    def test_theme_name_is_escaped(self):
        themes_data = {
            "clusters": [{"id": 0, "name": "<script>x</script>",
                          "keywords": [], "count": 1, "citations": 0,
                          "years": {}, "papers": []}],
            "years": [], "outliers": 0, "total": 1,
        }
        out = report.build_report_html(papers=[], themes=themes_data)
        self.assertNotIn("<script>x</script>", out)


class ThemeTotalsTests(unittest.TestCase):
    """표의 합이 실제와 어긋나지 않아야 한다.

    실제 버그: 미분류(outlier)를 편수만 세고 버려서 그들의 피인용이 표에서
    누락됐다 — 화면 325 vs 실제 328. 표가 "총 41편"이라 해놓고 피인용은
    40편분만 보여줬다.
    """

    def _fake_topic_modeling(self, labels):
        import types
        n = len(labels)
        return types.SimpleNamespace(
            compute_embeddings=lambda t: (None, sorted(t)),
            run_clustering=lambda e, s, t, **k: (
                labels, None, {i: [("kw", 1.0)] for i in set(labels) if i != -1},
                None, None, None))

    def _run(self, papers, labels):
        from lib.citedby import themes
        with patch.dict("sys.modules",
                        {"topic_modeling": self._fake_topic_modeling(labels)}), \
             patch.object(themes, "_name_clusters",
                          side_effect=lambda kw, ti, **k: {t: f"C{t}" for t in kw}):
            return themes.analyze_themes(papers, min_papers=3)

    def test_outlier_citations_are_counted(self):
        papers = [{"title": f"P{i}", "year": 2025, "citation_count": 10}
                  for i in range(4)]
        papers[3]["citation_count"] = 3          # 이 편이 outlier
        th = self._run(papers, [0, 0, 0, -1])
        self.assertEqual(th["outliers"], 1)
        self.assertEqual(th["outlier_citations"], 3)
        self.assertEqual(th["total_citations"], 33)

    def test_total_equals_sum_of_parts(self):
        papers = [{"title": f"P{i}", "year": 2024 + (i % 2),
                   "citation_count": i} for i in range(6)]
        th = self._run(papers, [0, 0, 1, 1, -1, -1])
        parts = sum(c["citations"] for c in th["clusters"]) \
            + th["outlier_citations"]
        self.assertEqual(parts, th["total_citations"])
        self.assertEqual(parts, sum(range(6)))

    def test_outlier_years_are_recorded(self):
        papers = [{"title": f"P{i}", "year": 2025, "citation_count": 1}
                  for i in range(4)]
        papers[3]["year"] = 2024
        th = self._run(papers, [0, 0, 0, -1])
        self.assertEqual(th["outlier_years"], {2024: 1})
        self.assertIn(2024, th["years"])

    def test_counts_add_up_to_total(self):
        papers = [{"title": f"P{i}", "year": 2025, "citation_count": 1}
                  for i in range(7)]
        th = self._run(papers, [0, 0, 1, 1, 1, -1, -1])
        self.assertEqual(sum(c["count"] for c in th["clusters"])
                         + th["outliers"], th["total"])

    def test_citations_parse_both_field_spellings(self):
        from lib.citedby import themes
        self.assertEqual(themes._citations_of({"citation_count": "42"}), 42)
        self.assertEqual(themes._citations_of({"citationCount": 7}), 7)
        self.assertEqual(themes._citations_of({"citation_count": "nan"}), 0)
        self.assertEqual(themes._citations_of({}), 0)

    def test_report_renders_total_row(self):
        themes_data = {
            "clusters": [{"id": 0, "name": "A", "keywords": [], "count": 2,
                          "citations": 10, "years": {2025: 2}, "papers": []}],
            "years": [2025], "outliers": 1, "outlier_years": {2025: 1},
            "outlier_citations": 3, "total": 3, "total_citations": 13,
        }
        out = report.build_report_html(papers=[], themes=themes_data)
        self.assertIn("합계", out)
        self.assertIn("13", out)      # 총 피인용
        self.assertIn(">3<", out)     # 미분류 피인용이 · 가 아니다


class LocalLibraryTests(unittest.TestCase):
    """로컬 Zotero DB 매칭 — 내가 보유한 논문은 API 를 두드리지 않는다."""

    def _idx(self):
        from lib.citedby import local_library as ll
        return ll.LibraryIndex(
            by_doi={"10.1/a": ll.LibraryItem(key="K1", title="A",
                                             doi="10.1/a", abstract="AB" * 30,
                                             pdf_path="/tmp/a.pdf",
                                             attachment_key="ATT1")},
            by_arxiv={"2409.04109": ll.LibraryItem(key="K2", title="B")},
            by_title={"papertitlec": ll.LibraryItem(key="K3", title="Paper Title C")})

    def test_lookup_priority_doi_first(self):
        idx = self._idx()
        hit = idx.lookup({"doi": "10.1/a", "title": "Paper Title C"})
        self.assertEqual(hit.key, "K1")

    def test_lookup_arxiv_fallback(self):
        hit = self._idx().lookup({"doi": "", "arxiv_id": "2409.04109"})
        self.assertEqual(hit.key, "K2")

    def test_lookup_title_last(self):
        hit = self._idx().lookup({"doi": "", "title": "Paper Title C!"})
        self.assertEqual(hit.key, "K3")

    def test_lookup_miss(self):
        self.assertIsNone(self._idx().lookup({"doi": "10.9/z", "title": "Nope"}))

    def test_doi_normalisation(self):
        from lib.citedby import local_library as ll
        for raw in ("https://doi.org/10.1/A", "doi:10.1/a", " 10.1/A "):
            self.assertEqual(ll.normalize_doi(raw), "10.1/a")

    def test_arxiv_extraction_from_url_or_extra(self):
        from lib.citedby import local_library as ll
        self.assertEqual(
            ll.extract_arxiv("https://arxiv.org/abs/2409.04109"), "2409.04109")
        self.assertEqual(ll.extract_arxiv("", "arXiv:2501.12345"), "2501.12345")
        self.assertEqual(ll.extract_arxiv("no id here"), "")

    def test_missing_db_returns_empty_index(self):
        from lib.citedby import local_library as ll
        idx = ll.load_library_index(db_path="/nonexistent/zotero.sqlite")
        self.assertFalse(idx)

    def test_enrich_fills_abstract_from_zotero(self):
        from lib.citedby import local_library as ll
        papers = [{"doi": "10.1/a", "title": "A", "abstract": ""}]
        out, st = ll.enrich_from_library(papers, self._idx(), read_pdf=False)
        self.assertTrue(out[0]["_in_library"])
        self.assertEqual(out[0]["_abstract_from"], "zotero")
        self.assertEqual(st["abstract_from_zotero"], 1)

    def test_enrich_does_not_overwrite_existing_abstract(self):
        from lib.citedby import local_library as ll
        papers = [{"doi": "10.1/a", "title": "A", "abstract": "기존 초록" * 10}]
        out, _ = ll.enrich_from_library(papers, self._idx(), read_pdf=False)
        self.assertIn("기존 초록", out[0]["abstract"])
        self.assertNotIn("_abstract_from", out[0])

    def test_enrich_marks_non_library_papers(self):
        from lib.citedby import local_library as ll
        out, st = ll.enrich_from_library(
            [{"doi": "10.9/z", "title": "Nope"}], self._idx(), read_pdf=False)
        self.assertFalse(out[0]["_in_library"])
        self.assertEqual(st["matched"], 0)

    def test_attachment_path_convention(self):
        from lib.citedby import local_library as ll
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            (d / "x.pdf").write_bytes(b"%PDF-1.4")
            self.assertEqual(ll._resolve_pdf("attachments:x.pdf", d, "K"),
                             str(d / "x.pdf"))
            self.assertEqual(ll._resolve_pdf("attachments:none.pdf", d, "K"), "")
            self.assertEqual(ll._resolve_pdf("", d, "K"), "")


class PdfCorpusTests(unittest.TestCase):
    """PDF 전문 기반 코퍼스 — 초록 대신 원문을 쓴다."""

    def _idx(self):
        from lib.citedby import local_library as ll
        return ll.LibraryIndex(by_doi={
            "10.1/held": ll.LibraryItem(key="K1", doi="10.1/held",
                                        pdf_path="/tmp/x.pdf",
                                        attachment_key="ATT1"),
            "10.1/nopdf": ll.LibraryItem(key="K2", doi="10.1/nopdf"),
        })

    def test_selects_only_pdf_holders(self):
        from lib.citedby.pdf_corpus import select_pdf_papers
        held, missing = select_pdf_papers([
            {"doi": "10.1/held", "title": "A"},
            {"doi": "10.1/nopdf", "title": "B"},     # 라이브러리에 있으나 PDF 없음
            {"doi": "10.9/z", "title": "C"},          # 라이브러리에 없음
        ], self._idx())
        self.assertEqual([p["doi"] for p in held], ["10.1/held"])
        self.assertEqual(len(missing), 2)
        self.assertEqual(held[0]["_library_attach"], "ATT1")

    def test_empty_index_holds_nothing(self):
        from lib.citedby import local_library as ll
        from lib.citedby.pdf_corpus import select_pdf_papers
        held, missing = select_pdf_papers([{"doi": "10.1/a"}], ll.LibraryIndex())
        self.assertEqual(held, [])
        self.assertEqual(len(missing), 1)

    def test_paper_key_prefers_doi_then_arxiv_then_title(self):
        from lib.citedby.pdf_corpus import paper_key
        self.assertEqual(paper_key({"doi": "10.1/A"}), "10.1/a")
        self.assertEqual(paper_key({"doi": "", "arxiv_id": "2409.04109"}),
                         "2409.04109")
        self.assertEqual(paper_key({"title": "Some Title!"}), "sometitle")

    def test_reference_meta_keeps_context_targets(self):
        from lib.citedby import pdf_corpus as PC
        corpus = PC._reference_meta(
            {"title": "Known", "doi": "https://doi.org/10.1234/X"},
            "known", "042_Known")
        self.assertEqual(corpus["reference_type"], "corpus")
        self.assertEqual(corpus["external_url"], "https://doi.org/10.1234/X")
        self.assertEqual(corpus["corpus_slug"], "042_Known")

        outside = PC._reference_meta(
            {"title": "Outside", "arxiv_id": "2409.04109"}, "outside")
        self.assertEqual(outside["reference_type"], "citedby-note")
        self.assertEqual(
            outside["external_url"], "https://arxiv.org/abs/2409.04109")
        self.assertTrue(outside["note_file"].endswith(".md"))


    def test_references_are_trimmed_from_fulltext(self):
        from lib.citedby import pdf_corpus
        body = "본문 " * 400 + "\nReferences\n" + "[1] cite " * 100
        with patch.object(pdf_corpus, "_REF_HEAD", pdf_corpus._REF_HEAD):
            m = pdf_corpus._REF_HEAD.search(body)
        self.assertIsNotNone(m)
        self.assertGreater(m.start(), len(body) * 0.3)

    def test_missing_pdf_yields_empty_text(self):
        from lib.citedby.pdf_corpus import pdf_fulltext
        self.assertEqual(pdf_fulltext("/nonexistent/x.pdf"), "")
        self.assertEqual(pdf_fulltext(""), "")

    def test_build_index_returns_none_without_chunks(self):
        from lib.citedby import pdf_corpus
        with tempfile.TemporaryDirectory() as tmp, \
             patch.object(pdf_corpus, "build_chunks", return_value=([], {}, {})):
            self.assertIsNone(pdf_corpus.build_index([], tmp))

    def test_index_schema_matches_search_index(self):
        """Deep Research UI 가 코퍼스 인덱스와 구분 없이 읽어야 한다."""
        from lib.citedby import pdf_corpus
        chunks = [{"slug": "s", "section": "본문", "text": "t" * 300,
                   "text_sha": "abc"}]
        meta = {"s": {"title": "T", "chunks": 1}}
        with tempfile.TemporaryDirectory() as tmp, \
             patch.object(pdf_corpus, "build_chunks", return_value=(chunks, meta, {})), \
             patch.object(pdf_corpus, "embed_chunks", return_value=None):
            info = pdf_corpus.build_index([{"title": "T"}], tmp)
            data = json.loads((Path(tmp) / pdf_corpus.INDEX_NAME)
                              .read_text(encoding="utf-8"))
        for key in ("model", "dim", "quant", "count", "papers", "chunks"):
            self.assertIn(key, data)
        self.assertEqual(data["dim"], 768)
        self.assertEqual(data["quant"], "int8-l2norm")
        self.assertEqual(info["chunks"], 1)

    def test_unmatched_papers_get_obsidian_evidence_notes(self):
        from lib.citedby import pdf_corpus as PC
        chunks = [{"slug": "outside", "section": "Results",
                   "text": "measured evidence", "text_sha": "a"}]
        meta = {"outside": {
            "title": "Outside Paper", "authors": ["A", "B"], "year": "2025",
            "journal": "J", "doi": "10.1234/out", "external_url":
            "https://doi.org/10.1234/out", "evidence": "pdf",
            "reference_type": "citedby-note", "note_file": "outside.md",
            "chunks": 1}}
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "papers" / "001_Seed" / "citedby"
            with patch.object(PC, "build_chunks",
                              return_value=(chunks, meta, {})), \
                 patch.object(PC, "embed_chunks", return_value=None):
                info = PC.build_index([], out)
            data = json.loads((out / PC.INDEX_NAME).read_text(encoding="utf-8"))
            note = (out / "notes" / "outside.md").read_text(encoding="utf-8")
        ref = data["papers"]["outside"]
        self.assertEqual(info["evidence_notes"], 1)
        self.assertEqual(
            ref["obsidian_path"],
            "papers/001_Seed/citedby/notes/outside")
        self.assertIn("[[papers/001_Seed/review|원논문 review]]", note)
        self.assertIn("measured evidence", note)

    def test_title_only_papers_still_get_local_notes(self):
        from lib.citedby import pdf_corpus as PC
        chunks = [{"slug": "grounded", "section": "본문",
                   "text": "x" * 300, "text_sha": "a"}]
        meta = {"grounded": {
            "title": "Grounded", "reference_type": "citedby-note",
            "note_file": "grounded.md", "chunks": 1}}
        title_only = {"title": "Title Only Paper", "_evidence": PC.EV_TITLE}
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "papers" / "001_Seed" / "citedby"
            with patch.object(PC, "build_chunks",
                              return_value=(chunks, meta, {})), \
                 patch.object(PC, "embed_chunks", return_value=None):
                info = PC.build_index([title_only], out)
            note = out / "notes" / Path(title_only["_citedby_note_file"]).name
            index = json.loads((out / PC.INDEX_NAME).read_text())
            note_exists = note.exists()
        self.assertTrue(note_exists)
        self.assertIn("papers/001_Seed/citedby/notes/",
                      title_only["_citedby_obsidian_path"])
        self.assertEqual(index["papers"][PC.paper_key(title_only)]["chunks"], 0)
        self.assertEqual(info["evidence_notes"], 2)


    def test_vector_length_mismatch_drops_vectors(self):
        """길이가 안 맞으면 잘못된 사이드카를 쓰느니 벡터 없이 저장한다."""
        from lib.citedby import pdf_corpus
        chunks = [{"slug": "s", "section": "본문", "text": "t" * 300,
                   "text_sha": "a"}]
        with tempfile.TemporaryDirectory() as tmp, \
             patch.object(pdf_corpus, "build_chunks",
                          return_value=(chunks, {"s": {"chunks": 1}}, {})), \
             patch.object(pdf_corpus, "embed_chunks", return_value=b"\x00" * 10):
            info = pdf_corpus.build_index([{"title": "T"}], tmp)
        self.assertFalse(info["has_vectors"])


class EvidenceTierTests(unittest.TestCase):
    """근거 등급 — PDF 없다고 논문을 버리지 않는다."""

    def _idx(self):
        from lib.citedby import local_library as ll
        return ll.LibraryIndex(by_doi={
            "10.1/pdf": ll.LibraryItem(key="K1", doi="10.1/pdf",
                                       pdf_path="/tmp/x.pdf",
                                       attachment_key="ATT1"),
            "10.1/abs": ll.LibraryItem(key="K2", doi="10.1/abs",
                                       abstract="초" * 200),
        })

    def test_three_tiers(self):
        from lib.citedby.pdf_corpus import (tier_papers, EV_CORPUS, EV_PDF,
                                            EV_ABSTRACT, EV_TITLE)
        out, stats = tier_papers([
            {"doi": "10.1/pdf", "title": "A"},
            {"doi": "10.1/abs", "title": "B"},
            {"doi": "10.9/z", "title": "C"},
            {"doi": "10.9/y", "title": "D", "abstract": "x" * 300},
        ], self._idx())
        self.assertEqual([p["_evidence"] for p in out],
                         [EV_PDF, EV_ABSTRACT, EV_TITLE, EV_ABSTRACT])
        self.assertEqual(stats, {EV_CORPUS: 0, EV_PDF: 1,
                                 EV_ABSTRACT: 2, EV_TITLE: 1})

    def test_nothing_is_dropped(self):
        from lib.citedby.pdf_corpus import tier_papers
        papers = [{"doi": f"10.9/{i}", "title": f"P{i}"} for i in range(7)]
        out, _ = tier_papers(papers, self._idx())
        self.assertEqual(len(out), 7)

    def test_short_abstract_counts_as_title_only(self):
        from lib.citedby.pdf_corpus import tier_papers, EV_TITLE
        out, _ = tier_papers([{"doi": "10.9/z", "abstract": "짧다"}], self._idx())
        self.assertEqual(out[0]["_evidence"], EV_TITLE)

    def test_library_abstract_upgrades_tier(self):
        """라이브러리에 초록이 있으면 제목만 → 초록으로 올라간다."""
        from lib.citedby.pdf_corpus import tier_papers, EV_ABSTRACT
        out, _ = tier_papers([{"doi": "10.1/abs", "title": "B"}], self._idx())
        self.assertEqual(out[0]["_evidence"], EV_ABSTRACT)

    def test_input_not_mutated(self):
        from lib.citedby.pdf_corpus import tier_papers
        src = [{"doi": "10.1/pdf", "title": "A"}]
        tier_papers(src, self._idx())
        self.assertNotIn("_evidence", src[0])


class CollectionSuggestionTests(unittest.TestCase):
    """컬렉션 추천 — 기존 컬렉션만, 확신 없으면 비워 둔다."""

    COLS = [{"id": 1, "name": "AI for Science", "label": "AI for Science",
             "count": 2883},
            {"id": 2, "name": "Humanoid", "label": "Humanoid", "count": 561}]

    def _run(self, results):
        from lib.citedby import collections as C
        with patch.object(C, "load_collections", return_value=self.COLS), \
             patch("lib.citedby.topic_filter.llm_json",
                   return_value={"results": results}):
            return C.recommend_collections(
                [{"title": "P1", "abstract": "a" * 200},
                 {"title": "P2", "abstract": "b" * 200}])

    def test_assigns_known_collection(self):
        out = self._run([{"paper": 1, "collection": "AI for Science",
                          "reason": "과학 AI", "confidence": "high"}])
        self.assertEqual(out[0]["_suggest_collection"], "AI for Science")
        self.assertEqual(out[0]["_suggest_confidence"], "high")
        self.assertNotIn("_suggest_collection", out[1])

    def test_hallucinated_collection_is_rejected(self):
        """목록에 없는 이름은 버린다 — 새 컬렉션 제안은 범위 밖이다."""
        out = self._run([{"paper": 1, "collection": "존재하지 않는 컬렉션",
                          "reason": "x"}])
        self.assertNotIn("_suggest_collection", out[0])

    def test_blank_collection_means_unfiled(self):
        out = self._run([{"paper": 1, "collection": "", "reason": "애매"}])
        self.assertNotIn("_suggest_collection", out[0])

    def test_no_collections_is_noop(self):
        from lib.citedby import collections as C
        with patch.object(C, "load_collections", return_value=[]):
            out = C.recommend_collections([{"title": "P"}])
        self.assertNotIn("_suggest_collection", out[0])

    def test_summarize_groups_and_counts_unfiled(self):
        from lib.citedby.collections import summarize
        rows = summarize([
            {"title": "A", "_suggest_collection": "X"},
            {"title": "B", "_suggest_collection": "X"},
            {"title": "C", "_suggest_collection": "Y"},
            {"title": "D"},
        ])
        self.assertEqual(rows[0]["name"], "X")
        self.assertEqual(rows[0]["count"], 2)
        self.assertEqual(rows[-1]["name"], "")
        self.assertEqual(rows[-1]["count"], 1)

    def test_report_renders_suggestion(self):
        out = report.build_report_html(papers=[{
            "title": "P", "doi": "10.1/a",
            "_suggest_collection": "AI for Science",
            "_suggest_reason": "과학 AI 주제",
            "_suggest_confidence": "high"}])
        self.assertIn("AI for Science", out)
        self.assertIn("컬렉션 배정 제안", out)


class DeepPanelTests(unittest.TestCase):
    def test_panel_absent_without_index(self):
        out = report.build_report_html(papers=[{"title": "P", "doi": "10.1/a"}])
        self.assertNotIn("drGo", out)

    def test_panel_present_with_index(self):
        out = report.build_report_html(papers=[{"title": "P", "doi": "10.1/a"}],
                                       deep_index="_citedby_index.json")
        self.assertIn("drGo", out)
        self.assertIn("_citedby_index.json", out)
        self.assertIn("/api/embed", out)

    def test_panel_is_not_printed(self):
        """PDF 출력에 검색 UI 가 끼면 안 된다."""
        out = report.build_report_html(papers=[{"title": "P"}],
                                       deep_index="_citedby_index.json")
        self.assertIn('class="dr no-print"', out)

    def test_offline_notice_exists(self):
        out = report.build_report_html(papers=[{"title": "P"}],
                                       deep_index="_citedby_index.json")
        self.assertIn("serve_local.py", out)


class CorpusAssetTests(unittest.TestCase):
    """코퍼스 전처리물이 원시 PDF 보다 우선한다."""

    def _idx(self):
        from lib.citedby import corpus_assets as CA
        idx = CA.CorpusIndex()
        idx.by_doi = {"10.1/corp": "042_Corpus_Paper"}
        idx.by_title = {"corpuspaper": "042_Corpus_Paper"}
        idx.meta = {"042_Corpus_Paper": {"title": "Corpus Paper",
                                         "primary_topic": "ai4s"}}
        idx.connections = {"042_Corpus_Paper": [
            {"slug": "099_Other", "relation": "extension", "reason": "확장"}]}
        idx.meta["099_Other"] = {"title": "Other Paper"}
        return idx

    def test_corpus_match_sets_evidence_and_connections(self):
        from lib.citedby.corpus_assets import enrich_with_corpus, EV_CORPUS
        out, st = enrich_with_corpus(
            [{"doi": "10.1/corp", "title": "Corpus Paper"},
             {"doi": "10.9/z", "title": "Outside"}], self._idx())
        self.assertEqual(out[0]["_evidence"], EV_CORPUS)
        self.assertEqual(out[0]["_corpus_slug"], "042_Corpus_Paper")
        self.assertEqual(out[0]["_connections"][0]["title"], "Other Paper")
        self.assertNotIn("_corpus_slug", out[1])
        self.assertEqual(st["matched"], 1)

    def test_connections_preserve_reference_identity(self):
        from lib.citedby.corpus_assets import connected_papers
        idx = self._idx()
        idx.meta["099_Other"].update({
            "doi": "10.1234/other", "year": "2024",
            "authors": "Kim; Lee", "external_url": "https://example.org/other"})
        ref = connected_papers("042_Corpus_Paper", idx)[0]
        self.assertEqual(ref["doi"], "10.1234/other")
        self.assertEqual(ref["year"], "2024")
        self.assertEqual(ref["authors"], "Kim; Lee")
        self.assertEqual(ref["external_url"], "https://example.org/other")

    def test_corpus_beats_pdf_in_tiering(self):
        """PDF 를 갖고 있어도 코퍼스 자산이 있으면 corpus 등급이다."""
        from lib.citedby import pdf_corpus as PC
        from lib.citedby import local_library as ll
        lib = ll.LibraryIndex(by_doi={
            "10.1/corp": ll.LibraryItem(key="K", doi="10.1/corp",
                                        pdf_path="/tmp/x.pdf",
                                        attachment_key="A")})
        with patch("lib.citedby.corpus_assets.load_corpus_index",
                   return_value=self._idx()):
            out, stats = PC.tier_papers(
                [{"doi": "10.1/corp", "title": "Corpus Paper"}], lib)
        self.assertEqual(out[0]["_evidence"], PC.EV_CORPUS)
        self.assertEqual(stats[PC.EV_CORPUS], 1)
        self.assertEqual(stats[PC.EV_PDF], 0)

    def test_lookup_by_title_when_doi_missing(self):
        self.assertEqual(self._idx().lookup({"title": "Corpus  Paper!"}),
                         "042_Corpus_Paper")

    def test_empty_index_is_noop(self):
        from lib.citedby import corpus_assets as CA
        out, st = CA.enrich_with_corpus([{"doi": "10.1/a"}], CA.CorpusIndex())
        self.assertNotIn("_corpus_slug", out[0])
        self.assertEqual(st["matched"], 0)

    def test_connections_are_capped(self):
        from lib.citedby.corpus_assets import connected_papers
        idx = self._idx()
        idx.connections["042_Corpus_Paper"] = [
            {"slug": f"s{i}", "relation": "r"} for i in range(9)]
        for i in range(9):
            idx.meta[f"s{i}"] = {"title": f"T{i}"}
        self.assertEqual(len(connected_papers("042_Corpus_Paper", idx, limit=5)), 5)

    def test_report_shows_connections(self):
        out = report.build_report_html(papers=[{
            "title": "P", "doi": "10.1/a", "_evidence": "corpus",
            "_connections": [{"title": "이어지는 논문", "relation": "extension"}]}])
        self.assertIn("이어지는 논문", out)
        self.assertIn("ev-corpus", out)


class ServeTests(unittest.TestCase):
    """리포트를 로컬 서버로 띄우는 경로 — Deep Research 는 file:// 에서 안 된다."""

    def test_report_url_maps_docs_relative_path(self):
        from lib.citedby import serve
        p = serve._DOCS / "papers" / "042_X" / "citedby" / "r.html"
        self.assertEqual(serve.report_url(p, 8000),
                         "http://localhost:8000/papers/042_X/citedby/r.html")

    def test_report_url_empty_outside_docs(self):
        """docs/ 밖이면 서빙할 수 없다 — 잘못된 링크를 주느니 없는 게 낫다."""
        from lib.citedby import serve
        self.assertEqual(serve.report_url("/tmp/r.html", 8000), "")

    def test_reuses_running_server(self):
        from lib.citedby import serve
        with patch.object(serve, "find_running", return_value=8003), \
             patch.object(serve.subprocess, "Popen") as popen:
            self.assertEqual(serve.ensure_server(), 8003)
        popen.assert_not_called()

    def test_is_ours_rejects_foreign_server(self):
        """8000 은 흔한 포트다. 남의 서버를 우리 것으로 오인하면 안 된다."""
        from lib.citedby import serve
        import urllib.error
        err = urllib.error.HTTPError("u", 404, "nf", None, None)
        with patch.object(serve.urllib.request, "urlopen", side_effect=err):
            self.assertFalse(serve._is_ours(8000))

    def test_is_ours_accepts_health_signature(self):
        from lib.citedby import serve
        import io
        body = io.BytesIO(json.dumps({
            "ok": True,
            "service": "paper-curation-serve-local",
        }).encode())
        with patch.object(serve.urllib.request, "urlopen",
                          return_value=body) as request:
            self.assertTrue(serve._is_ours(8000))
        self.assertIn("/api/health", request.call_args.args[0])

    def test_no_free_port_returns_none(self):
        from lib.citedby import serve
        with patch.object(serve, "find_running", return_value=None), \
             patch.object(serve, "_port_open", return_value=True):
            self.assertIsNone(serve.ensure_server())

    def test_serve_report_returns_empty_when_server_fails(self):
        from lib.citedby import serve
        with patch.object(serve, "ensure_server", return_value=None):
            self.assertEqual(serve.serve_report("/x/r.html"), "")


class DeepPanelDepthTests(unittest.TestCase):
    """답변 깊이 회귀 방지.

    "Deep Research 가 부실하다" 는 보고의 원인이 넷이었다 — 프롬프트가 명시적
    으로 "간결하게" 를 요구했고, 근거가 12청크, 출력이 1,600토큰, 청크가
    1,400자였다. 컨텍스트가 15.6k자에 그쳐 논문 여러 편을 비교할 여지가 없었다.
    """

    def _js(self):
        from lib.citedby.deep_panel import panel_script
        return panel_script("_citedby_index.json")

    def test_context_budget_is_large_enough(self):
        from lib.citedby import deep_panel as DP
        from lib.citedby import pdf_corpus as PC
        ctx = DP.TOPK * PC.CHUNK_SIZE
        self.assertGreaterEqual(ctx, 50000, f"컨텍스트가 {ctx}자로 너무 작다")

    def test_output_budget_allows_a_long_answer(self):
        from lib.citedby import deep_panel as DP
        self.assertGreaterEqual(DP.MAX_OUT, 6000)

    def test_prompt_does_not_ask_for_brevity(self):
        """'간결하게' 가 얇은 답변의 직접 원인이었다."""
        js = self._js()
        self.assertNotIn("간결하게", js)
        self.assertIn("분량은 아끼지 않는다", js)

    def test_prompt_demands_concrete_numbers_and_comparison(self):
        js = self._js()
        for phrase in ("수치", "비교", "그대로 인용"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, js)

    def test_per_paper_cap_prevents_single_paper_domination(self):
        from lib.citedby import deep_panel as DP
        self.assertGreater(DP.PER_PAPER, 0)
        self.assertLess(DP.PER_PAPER, DP.TOPK,
                        "논문당 상한이 최종 근거 수 이상이면 상한이 무의미하다")
        self.assertIn("PER_PAPER", self._js())

    def test_candidate_pool_exceeds_final_selection(self):
        from lib.citedby import deep_panel as DP
        self.assertGreater(DP.POOL, DP.TOPK)

    def test_constants_are_injected_into_js(self):
        js = self._js()
        for name in ("TOPK", "POOL", "PER_PAPER", "MAX_OUT"):
            with self.subTest(name=name):
                self.assertIn(f"var {name}=", js)

    def test_context_carries_section_and_year(self):
        """섹션·연도가 없으면 LLM 이 근거를 제대로 귀속하지 못한다."""
        js = self._js()
        self.assertIn("r.section", js)
        self.assertIn("r.year", js)

    def test_refs_show_excerpt_preview(self):
        self.assertIn("dr-prev", self._js())

    def test_chunk_size_covers_a_full_paragraph(self):
        from lib.citedby import pdf_corpus as PC
        self.assertGreaterEqual(PC.CHUNK_SIZE, 2000)
        self.assertGreaterEqual(PC.CHUNK_OVERLAP, 300)

    def test_per_paper_chunk_cap_covers_full_text(self):
        """전문 평균 63k자 / 2.2k = ~29청크. 상한이 그보다 작으면 뒷부분이 잘린다."""
        from lib.citedby import pdf_corpus as PC
        self.assertGreaterEqual(PC.MAX_CHUNKS_PER_PAPER * PC.CHUNK_SIZE, 120000)


class TimelineProcedureTests(unittest.TestCase):
    """타임라인은 **narrative → 후보 N개 → vision judge 선별** 절차를 따른다.

    통계를 PaperBanana 에 바로 던지면 "무엇을 그릴지" 를 생성기가 스스로
    지어내야 해서 같은 데이터로도 결과가 매번 달라진다. paper-curation 의
    generate_timelines 가 narrative 단계를 두는 이유가 그것이다.
    """

    THEMES = {
        "clusters": [
            {"id": 0, "name": "AI Agents", "keywords": ["agent", "llm"],
             "count": 8, "citations": 120, "years": {2024: 3, 2025: 5},
             "titles": ["Virtual Lab designs nanobodies"], "papers": []},
            {"id": 1, "name": "Peer Review", "keywords": ["review"],
             "count": 3, "citations": 20, "years": {2025: 3},
             "titles": ["ReviewEval"], "papers": []},
        ],
        "years": [2024, 2025], "outliers": 0, "outlier_years": {},
        "outlier_citations": 0, "total": 11, "total_citations": 140,
    }

    def test_narrative_prompt_carries_paper_titles(self):
        """제목이 없으면 스트림 이름밖에 못 쓴다 — 구체성이 사라진다."""
        from lib.citedby import timeline as TL
        block = TL._themes_block(self.THEMES)
        self.assertIn("Virtual Lab designs nanobodies", block)
        self.assertIn("120 citations", block)

    def test_narrative_requested_before_image(self):
        from lib.citedby import timeline as TL
        seen = {}

        def fake_llm(prompt, **kw):
            seen["prompt"] = prompt
            return {"method_text": "## Citation Timeline", "caption": "c"}

        with patch("lib.citedby.topic_filter.llm_json", side_effect=fake_llm):
            mt, cap, ov, st = TL.build_narrative(self.THEMES, {"title": "Seed"})
        self.assertEqual(mt, "## Citation Timeline")
        self.assertIn("STREAM:", seen["prompt"])
        self.assertIn("Seed", seen["prompt"])

    def test_no_narrative_means_no_image_attempt(self):
        from lib.citedby import timeline as TL
        with patch.object(TL, "build_narrative", return_value=("", "", "", [])), \
             patch.object(TL, "_generate_candidates") as gen:
            self.assertEqual(TL.generate(self.THEMES).uri, "")
        gen.assert_not_called()

    def test_overview_survives_narrative_failure(self):
        """작화 지시가 없어 그림을 못 그려도, 개요가 나왔으면 그건 살린다."""
        from lib.citedby import timeline as TL
        with patch.object(TL, "build_narrative",
                          return_value=("", "", "개요는 나왔다.", [])), \
             patch.object(TL, "_generate_candidates") as gen:
            r = TL.generate(self.THEMES)
        self.assertEqual(r.uri, "")
        self.assertEqual(r.overview, "개요는 나왔다.")
        gen.assert_not_called()

    def test_judge_picks_among_candidates(self):
        from lib.citedby import timeline as TL
        res = [(1, 10, "/a.png", b"A"), (2, 20, "/b.png", b"B"),
               (3, 30, "/c.png", b"C")]
        block = unittest.mock.MagicMock()
        block.type = "tool_use"
        block.input = {"best": 2, "reason": "선명"}
        resp = unittest.mock.MagicMock(content=[block])
        client = unittest.mock.MagicMock()
        client.messages.create.return_value = resp
        with patch("anthropic.Anthropic", return_value=client):
            self.assertEqual(TL._select_best(res, "cap")[0], 2)

    def test_judge_failure_falls_back_to_first(self):
        """선별이 배치를 막아서는 안 된다."""
        from lib.citedby import timeline as TL
        res = [(1, 10, "/a.png", b"A"), (2, 20, "/b.png", b"B")]
        with patch("anthropic.Anthropic", side_effect=RuntimeError("down")):
            self.assertEqual(TL._select_best(res, "")[0], 1)

    def test_single_candidate_skips_judge(self):
        from lib.citedby import timeline as TL
        with patch("anthropic.Anthropic") as A:
            TL._select_best([(1, 10, "/a.png", b"A")], "")
        A.assert_not_called()

    def test_no_candidates_returns_none(self):
        from lib.citedby import timeline as TL
        self.assertIsNone(TL._select_best([], ""))

    def test_empty_themes_is_noop(self):
        from lib.citedby import timeline as TL
        self.assertEqual(TL.generate({}).uri, "")
        self.assertEqual(TL.generate({"clusters": []}).uri, "")

    def test_report_embeds_timeline_as_data_uri(self):
        """사이드카 PNG 를 참조하면 파일을 옮기거나 PDF 로 뽑을 때 사라진다."""
        uri = "data:image/png;base64,AAAA"
        out = report.build_report_html(papers=[{"title": "P"}],
                                       timeline_uri=uri)
        self.assertIn(uri, out)
        self.assertIn("인용 흐름 타임라인", out)

    def test_report_without_timeline_has_no_figure(self):
        out = report.build_report_html(papers=[{"title": "P"}])
        self.assertNotIn("figure class=\"tl\"", out)


class ElapsedClockTests(unittest.TestCase):
    """경과시간은 시계 조정에 흔들리면 안 된다.

    실제 사고: 실행 중 시스템 시계가 뒤로 점프해 리포트에 -56,645초가 찍혔다.
    datetime.now() 차이는 NTP 보정·절전 복귀에 그대로 노출된다.
    """

    def test_uses_monotonic_not_wallclock(self):
        src = (PIPELINE_DIR / "lib" / "citedby" / "analysis.py").read_text(
            encoding="utf-8")
        self.assertIn("time.monotonic()", src)
        self.assertNotIn("(datetime.now() - started)", src)

    def test_elapsed_never_negative(self):
        """시계가 뒤로 뛰어도 음수가 새어 나가지 않는다."""
        seq = iter([1000.0, 100.0])       # 두 번째 호출이 더 작다
        with patch.object(analysis.time, "monotonic", lambda: next(seq)), \
             patch.object(analysis, "run_citing_analysis",
                          return_value={"papers": [], "paper_info": None,
                                        "source_counts": {}, "csv": "",
                                        "doi": "10.1/a"}), \
             patch.object(analysis, "run_topic_analysis",
                          return_value={"papers": [], "report_html": "<html>",
                                        "csv": "", "matched": 0, "total": 0,
                                        "topic": "", "themes": None}):
            out = analysis.run_citedby("10.1/a")
        self.assertGreaterEqual(out["elapsed_sec"], 0)


class ServerSideKeyTests(unittest.TestCase):
    """로컬 전용이므로 키는 서버에 두고 브라우저로 내려보내지 않는다."""

    def test_panel_has_no_key_input(self):
        from lib.citedby.deep_panel import panel_script, panel_html
        js = panel_script("_citedby_index.json")
        html = panel_html("_citedby_index.json",
                          {"dr_title": "t", "dr_sub": "s", "dr_ph": "p",
                           "dr_go": "g", "dr_offline": "o",
                           "exp_pdf": "P", "exp_md": "M", "exp_obs": "O",
                           "exp_audio": "A"})
        self.assertNotIn("drKey", js)
        self.assertNotIn("drKey", html)
        self.assertNotIn("type=\"password\"", html)

    def test_panel_calls_server_answer_route(self):
        from lib.citedby.deep_panel import panel_script
        js = panel_script("_citedby_index.json")
        self.assertIn("/api/citedby-answer", js)
        self.assertNotIn("api.anthropic.com", js)
        self.assertNotIn("api.openai.com", js)
        self.assertNotIn("generativelanguage.googleapis.com", js)

    def test_panel_streams_ndjson_and_has_research_options(self):
        from lib.citedby.deep_panel import panel_script, panel_html
        labels = {"dr_title": "t", "dr_sub": "s", "dr_ph": "p",
                  "dr_go": "g", "dr_offline": "o",
                  "exp_pdf": "P", "exp_md": "M", "exp_obs": "O",
                  "exp_audio": "A"}
        js = panel_script("_citedby_index.json")
        html = panel_html("_citedby_index.json", labels)
        self.assertIn("getReader()", js)
        self.assertIn("ev.event==='delta'", js)
        self.assertIn("web_search:!!web", js)
        self.assertIn('id="drWeb"', html)
        self.assertIn('id="drDeeper"', html)

    def test_deeper_runs_plan_and_related_expansion(self):
        from lib.citedby.deep_panel import panel_script, panel_html
        labels = {"dr_title": "t", "dr_sub": "s", "dr_ph": "p",
                  "dr_go": "g", "dr_offline": "o",
                  "exp_pdf": "P", "exp_md": "M", "exp_obs": "O",
                  "exp_audio": "A"}
        js = panel_script("_citedby_index.json")
        html = panel_html("_citedby_index.json", labels)
        self.assertIn("plan=await planResearch(q,refs)", js)
        self.assertIn("refs=await expandRelated(refs)", js)
        self.assertIn("connections:p.connections||[]", js)
        self.assertIn("purpose:'plan'", js)
        self.assertIn('id="drPlan"', html)

    def test_web_activity_is_visible_not_discarded(self):
        from lib.citedby.deep_panel import panel_script
        from lib.citedby import topic_filter as TF
        js = panel_script("_citedby_index.json")
        self.assertIn("function researchEvent", js)
        self.assertIn("WEB_COUNT++", js)
        self.assertIn("WEB_SOURCES++", js)
        self.assertIn("MUST perform web", TF._STREAM_SYSTEM)

    def test_server_answer_route_is_streaming(self):
        import serve_local
        src = inspect.getsource(serve_local.LocalHandler._handle_citedby_answer)
        self.assertIn("application/x-ndjson", src)
        self.assertIn("llm_text_stream", src)
        self.assertIn('"event": "delta"', src)
        self.assertIn("PLAN_MODELS", src)
        self.assertIn("on_event=emit_event", src)

    def test_llm_text_does_not_force_json(self):
        """JSON system 프롬프트를 그대로 쓰면 답변이 ```json 으로 감싸여 나온다."""
        from lib.citedby import topic_filter as TF
        seen = {}

        def fake(key, model, prompt, max_tokens, system=None):
            seen["system"] = system
            return "평문 답변"

        with patch.dict(TF._CALLERS, {"anthropic": fake}), \
             patch.object(TF, "resolve_keys", return_value={"anthropic": "K"}):
            ans, prov, model = TF.llm_text("q")
        self.assertEqual(ans, "평문 답변")
        self.assertEqual(prov, "anthropic")
        self.assertEqual(seen["system"], TF.TEXT_SYSTEM)
        self.assertNotEqual(seen["system"], TF._JSON_SYSTEM)

    def test_llm_text_cascades_on_failure(self):
        from lib.citedby import topic_filter as TF

        def boom(*a, **k):
            raise RuntimeError("down")

        with patch.dict(TF._CALLERS, {"anthropic": boom,
                                      "google": lambda *a, **k: "구글 답변"}), \
             patch.object(TF, "resolve_keys",
                          return_value={"anthropic": "A", "google": "G"}):
            ans, prov, _ = TF.llm_text("q")
        self.assertEqual(ans, "구글 답변")
        self.assertEqual(prov, "google")

    def test_llm_text_empty_when_no_keys(self):
        from lib.citedby import topic_filter as TF
        with patch.object(TF, "resolve_keys", return_value={}):
            self.assertEqual(TF.llm_text("q"), ("", "", ""))

    def test_llm_text_stream_continues_truncated_answer(self):
        from lib.citedby import topic_filter as TF
        calls = []

        def fake(key, model, prompt, max_tokens, emit, web, on_event):
            calls.append(prompt)
            text = "첫 부분." if len(calls) == 1 else " 마지막 부분."
            emit(text)
            return text, len(calls) == 1

        deltas = []
        with patch.dict(TF._STREAM_CALLERS, {"anthropic": fake}), \
             patch.object(TF, "resolve_keys", return_value={"anthropic": "K"}):
            ans, provider, _ = TF.llm_text_stream(
                "질문", deltas.append, models=[("anthropic", "model")])
        self.assertEqual(ans, "첫 부분. 마지막 부분.")
        self.assertEqual("".join(deltas), ans)
        self.assertEqual(provider, "anthropic")
        self.assertEqual(len(calls), 2)
        self.assertIn("PARTIAL ANSWER", calls[1])

    def test_llm_text_stream_relays_provider_events(self):
        from lib.citedby import topic_filter as TF

        def fake(key, model, prompt, max_tokens, emit, web, on_event):
            on_event("web_search", {"query": "q1"})
            on_event("web_result", {"url": "https://example.org"})
            emit("답")
            return "답", False

        events = []
        with patch.dict(TF._STREAM_CALLERS, {"anthropic": fake}), \
             patch.object(TF, "resolve_keys", return_value={"anthropic": "K"}):
            TF.llm_text_stream(
                "질문", lambda text: None, web_search=True,
                models=[("anthropic", "model")],
                on_event=lambda event, payload: events.append((event, payload)))
        self.assertEqual([e[0] for e in events], ["web_search", "web_result"])

    def test_json_path_still_forces_json(self):
        """자유 텍스트 경로를 추가하면서 JSON 경로가 깨지면 안 된다."""
        from lib.citedby import topic_filter as TF
        seen = {}

        def fake(key, model, prompt, max_tokens, system=TF._JSON_SYSTEM):
            seen["system"] = system
            return '{"ok": 1}'

        with patch.dict(TF._CALLERS, {"anthropic": fake}), \
             patch.object(TF, "resolve_keys", return_value={"anthropic": "K"}):
            self.assertEqual(TF.llm_json("q"), {"ok": 1})
        self.assertEqual(seen["system"], TF._JSON_SYSTEM)


class AnswerExportTests(unittest.TestCase):
    """답변 렌더·내보내기 — paper-curation 의 기존 구현을 재사용한다.

    처음엔 마크다운 렌더러·TTS·Obsidian 저장 라우트를 새로 만들려 했는데,
    셋 다 이미 있었다 (marked.js, lib/audio_overview, obsidian://new URI).
    """

    def _html(self, **kw):
        kw.setdefault("papers", [{"title": "P", "doi": "10.1/a"}])
        return report.build_report_html(**kw)

    def test_answer_model_is_top_tier(self):
        """배치 분류용 저비용 tier 로는 6만 자 근거를 못 다룬다."""
        from lib.citedby.topic_filter import ANSWER_MODELS, DEFAULT_MODELS
        self.assertEqual(ANSWER_MODELS[0], ("anthropic", "claude-opus-5"))
        self.assertNotEqual(ANSWER_MODELS[0], DEFAULT_MODELS[0])

    def test_markdown_is_rendered_not_raw(self):
        js = self._html(deep_index="_citedby_index.json")
        self.assertIn("mdToMarkup", js)
        self.assertIn("marked.min.js", js)
        self.assertNotIn("$('drAns').textContent=text", js)

    def test_inline_citations_target_reference_entries(self):
        h = self._html(deep_index="_citedby_index.json")
        self.assertIn('href="#\'+prefix+n', h)
        self.assertIn('id="dr-ref-\'+(i+1)', h)
        self.assertIn("mdToMarkup(LAST.answer,'dr-pdf-ref-')", h)
        self.assertIn('id="dr-pdf-ref-\'+n', h)

    def test_export_buttons_present(self):
        h = self._html(deep_index="_citedby_index.json")
        for bid in ("drPdf", "drMd", "drObs", "drAudioBtn"):
            with self.subTest(bid=bid):
                self.assertIn(bid, h)

    def test_obsidian_uses_uri_not_server_route(self):
        """obsidian://new 면 서버 라우트가 필요 없다 — 코퍼스와 같은 방식."""
        h = self._html(deep_index="_citedby_index.json")
        self.assertIn("obsidian://new?vault=docs", h)
        self.assertNotIn("/api/citedby-save", h)

    def test_obsidian_path_and_filename_convention(self):
        h = self._html(deep_index="_citedby_index.json", collection="ai4s")
        self.assertIn("'notes/'+COLLECTION+'/help/CITEDBY_'", h)
        self.assertIn('var COLLECTION="ai4s"', h)

    def test_obsidian_links_reviews_and_generated_evidence_notes(self):
        h = self._html(deep_index="_citedby_index.json")
        identity = h[h.index("function obsidianTarget"):
                     h.index("function safeName")]
        self.assertIn("r.obsidian_path", identity)
        self.assertIn("'papers/'+slug+'/review'", identity)
        self.assertIn("linkAnswerForExport", identity)
        self.assertIn("('[['+note+'|['+n+']]]')", identity)

    def test_markdown_and_pdf_use_external_reference_urls(self):
        h = self._html(deep_index="_citedby_index.json")
        markdown = h[h.index("function buildFullMarkdown"):
                     h.index("function safeName")]
        self.assertIn("else if(refUrl(r))", markdown)
        self.assertIn("linked='['+title+']('+refUrl(r)+')'", markdown)
        self.assertIn("linkAnswerForExport", markdown)

    def test_live_references_use_local_html_on_localhost(self):
        h = self._html(deep_index="_citedby_index.json")
        identity = h[h.index("function localRefUrl"):
                     h.index("function obsidianTarget")]
        refs = h[h.index("function renderRefs"):h.index("async function run")]
        self.assertIn("location.hostname==='localhost'", identity)
        self.assertIn("localRefUrl(r)", identity)
        self.assertIn("liveRefUrl(r)", refs)
        self.assertIn("evidence note", refs)

    def test_web_citations_reuse_corpus_identity(self):
        h = self._html(deep_index="_citedby_index.json")
        dedup = h[h.index("function absorbWebCitations"):
                  h.index("function cleanWebPreamble")]
        self.assertIn("r.reference_type==='corpus'||r.corpus_slug", dedup)
        self.assertIn("byDoi", dedup)
        self.assertIn("canonicalUrl", dedup)
        self.assertIn("byTitle", dedup)
        self.assertIn("return prefix+'[ref:'+n+']'", dedup)
        self.assertIn("text=absorbWebCitations(text,refs)", h)

    def test_pdf_export_keeps_absolute_reference_links(self):
        """파일을 받은 사람이 클릭할 수 있어야 한다."""
        h = self._html(deep_index="_citedby_index.json")
        self.assertIn("https://doi.org/", h)
        self.assertIn("https://arxiv.org/abs/", h)
        self.assertIn("function exportPdf", h)

    def test_pdf_exports_include_attribution_footer(self):
        h = self._html(deep_index="_citedby_index.json")
        self.assertGreaterEqual(h.count("Jehyun Lee ("), 2)
        self.assertGreaterEqual(
            h.count("https://github.com/jehyunlee/paper-curation"), 4)
        self.assertIn('class="pdf-footer"', h)
    def test_audio_reuses_existing_module(self):
        """TTS 를 새로 만들지 않는다 — audio_overview 가 대본·TTS·mp3·이메일을
        전부 갖고 있다."""
        h = self._html(deep_index="_citedby_index.json")
        self.assertIn("lamejs", h)               # audio_overview 의 mp3 인코더
        self.assertIn("_audioContextProvider", h)
        self.assertIn("window._AUDIO_MODE", h)

    def test_audio_absent_without_panel(self):
        self.assertNotIn("lamejs", self._html())

    def test_export_bar_hidden_until_answered(self):
        h = self._html(deep_index="_citedby_index.json")
        self.assertIn('id="drExport" style="display:none"', h)

    def test_result_export_bar_precedes_streamed_answer(self):
        h = self._html(deep_index="_citedby_index.json")
        self.assertLess(h.index('id="drExport"'), h.index('id="drAns"'))

    def test_report_and_result_exports_are_separate(self):
        h = self._html(deep_index="_citedby_index.json", collection="ai4s")
        for bid in ("rpMd", "rpObs", "rpAudio", "drMd", "drObs", "drAudioBtn"):
            self.assertIn('id="' + bid + '"', h)
        self.assertIn("CITEDBY_REPORT_", h)
        self.assertIn("window._citedbyAudioMode=\"report\"", h)
        self.assertIn("window._citedbyAudioMode='deep'", h)
        self.assertIn("root.querySelectorAll('.no-print,.dr", h)

    def test_whole_report_obsidian_export_uses_local_notes(self):
        h = self._html(
            paper_info={"title": "Seed", "doi": "10.1234/seed"},
            papers=[
                {"title": "Reviewed", "doi": "10.1234/reviewed",
                 "_corpus_slug": "042_Reviewed"},
                {"title": "Evidence", "doi": "10.1234/evidence",
                 "_citedby_obsidian_path":
                 "papers/001_Seed/citedby/notes/evidence"},
            ])
        self.assertIn(
            'data-obsidian="papers/042_Reviewed/review"', h)
        self.assertIn(
            'data-obsidian="papers/001_Seed/citedby/notes/evidence"', h)
        self.assertIn('data-obsidian="@seed/review"', h)
        self.assertIn("reportMarkdown('obsidian')", h)
        self.assertIn("if(note) return '[['+note+'|'+body+']]'", h)
        self.assertIn("window._citedbyReportMarkdown=reportMarkdown", h)

    def test_report_titles_use_local_reviews_live_and_external_links_in_pdf(self):
        h = self._html(
            paper_info={"title": "Seed", "doi": "10.1234/seed"},
            papers=[{
                "title": "Reviewed", "doi": "10.1234/reviewed",
                "_corpus_slug": "042_Reviewed Paper",
            }])
        self.assertIn(
            'href="https://doi.org/10.1234/reviewed" '
            'data-local="/papers/042_Reviewed%20Paper/" '
            'data-external="https://doi.org/10.1234/reviewed"', h)
        self.assertIn(
            'class="seed-t" data-local="@seed" '
            'data-external="https://doi.org/10.1234/seed"', h)
        self.assertIn('window.addEventListener("beforeprint", applyPrintLinks)', h)
        self.assertIn('window.addEventListener("afterprint", applyLiveLinks)', h)
        self.assertIn("window._citedbyApplyLiveLinks = applyLiveLinks", h)
        self.assertIn("window._citedbyApplyPrintLinks = applyPrintLinks", h)
        self.assertIn(
            '<a href="https://doi.org/10.1234/reviewed" rel="noopener">원문</a>',
            h)

    def test_python_markdown_recovery_uses_same_local_identity(self):
        papers = [
            {"title": "Reviewed", "doi": "10.1234/reviewed",
             "_corpus_slug": "042_Reviewed"},
            {"title": "Evidence", "doi": "10.1234/evidence",
             "_citedby_obsidian_path":
             "papers/001_Seed/citedby/notes/evidence"},
        ]
        source = (
            "[Reviewed](https://doi.org/10.1234/reviewed) "
            "[Evidence](#p2) "
            "[Seed](https://doi.org/10.1234/seed)")
        converted = report.obsidianize_report_markdown(
            source, papers, seed_slug="001_Seed", seed_title="Seed",
            seed_url="https://doi.org/10.1234/seed")
        self.assertIn(
            "[[papers/042_Reviewed/review|Reviewed]]", converted)
        self.assertIn(
            "[[papers/001_Seed/citedby/notes/evidence|Evidence]]", converted)
        self.assertIn("[[papers/001_Seed/review|Seed]]", converted)


import inspect


class TimelineDefaultTests(unittest.TestCase):
    """타임라인은 기본으로 그린다.

    인용 흐름은 연도별 표보다 그림이 훨씬 빨리 읽힌다. opt-in 이면 사실상
    아무도 안 켜므로 기본을 뒤집고, 급할 때 `--no-timeline` 으로 끈다.
    """

    def _parser(self):
        import run_citedby
        return run_citedby.build_parser() if hasattr(run_citedby, "build_parser") else None

    def test_cli_draws_timeline_by_default(self):
        import subprocess, sys, pathlib
        root = pathlib.Path(__file__).resolve().parents[2]
        out = subprocess.run(
            [sys.executable, str(root / "pipeline" / "run_citedby.py"), "--help"],
            capture_output=True, text=True, timeout=120).stdout
        self.assertIn("--no-timeline", out)

    def test_library_default_is_on(self):
        import inspect
        from lib.citedby import analysis
        for fn, param in ((analysis.run_topic_analysis, "want_timeline"),
                          (analysis.run_citedby, "timeline")):
            with self.subTest(fn=fn.__name__):
                sig = inspect.signature(fn)
                self.assertTrue(sig.parameters[param].default,
                                f"{fn.__name__}({param}=) 가 기본 False 면 "
                                "CLI 만 바꾼 셈이라 API 호출자와 어긋난다")

    def test_timeline_failure_does_not_break_report(self):
        """그림은 부가물이다 — 실패해도 리포트는 나와야 한다."""
        import lib.citedby.analysis as A
        src = inspect.getsource(A.run_topic_analysis)
        self.assertIn("except", src)


class TimelineNarrativeTests(unittest.TestCase):
    """그림과 함께 narrative 도 싣는다.

    narrative 는 LLM 이 인용 흐름을 읽고 쓴 본문이다. 그림을 만드는 재료로만
    쓰고 버렸는데, 정보량은 그림보다 많다.
    """

    def _html(self, **kw):
        kw.setdefault("papers", [{"title": "P"}])
        return report.build_report_html(**kw)

    def test_image_and_narrative_both_rendered(self):
        h = self._html(timeline_uri="data:image/png;base64,AAA",
                       timeline_narrative="첫 문단.\n\n둘째 문단.")
        self.assertIn("data:image/png;base64,AAA", h)
        self.assertIn('<div class="tl-narr">', h)
        # 마크다운 변환을 거치므로 문단이 <p> 로 나온다
        self.assertIn("첫 문단.", h)
        self.assertIn("둘째 문단.", h)

    def test_narrative_survives_image_failure(self):
        """그림만 실패한 것이지 글은 이미 나와 있다."""
        h = self._html(timeline_narrative="글만 있다.")
        self.assertIn('<div class="tl-narr">', h)
        self.assertNotIn("<img src=\"data:image/png", h)

    def test_section_omitted_when_both_absent(self):
        self.assertNotIn('<div class="tl-narr">', self._html())

    def test_narrative_is_escaped(self):
        h = self._html(timeline_narrative="<script>alert(1)</script>")
        self.assertNotIn("<script>alert(1)</script>", h)

    def test_generate_returns_narrative_with_uri(self):
        from lib.citedby.timeline import TimelineResult
        r = TimelineResult(uri="u", narrative="n", caption="c")
        self.assertEqual((r.uri, r.narrative, r.caption), ("u", "n", "c"))
        self.assertTrue(r)
        self.assertFalse(TimelineResult(narrative="글만"))  # uri 없으면 falsy

    def test_analysis_passes_narrative_through(self):
        import inspect
        from lib.citedby import analysis
        src = inspect.getsource(analysis.run_topic_analysis)
        self.assertIn("timeline_narrative=timeline_narrative", src)


class TimelineNarrativeShapeTests(unittest.TestCase):
    """독자에게 보여줄 것만, 읽을 수 있는 형태로.

    method_text 뒷부분은 PaperBanana 용 작화 지시문(배경색·픽셀 크기·금지 요소)
    이라 독자에게 의미가 없다. 그대로 뿌리면 리포트가 프롬프트 덤프가 된다.
    """

    def test_drawing_spec_is_stripped(self):
        from lib.citedby.timeline import reader_portion
        src = ("## Citation Timeline\n### STREAM: a\n분석 본문\n"
               "### BAND WIDTH GUIDE\n밴드 폭 지시\n"
               "### ABSOLUTE VISUAL RULES\n- Background: Pure white\n")
        got = reader_portion(src)
        self.assertIn("분석 본문", got)
        for banned in ("BAND WIDTH GUIDE", "ABSOLUTE VISUAL RULES",
                       "Pure white"):
            with self.subTest(banned=banned):
                self.assertNotIn(banned, got)

    def test_reader_portion_keeps_all_when_no_spec(self):
        from lib.citedby.timeline import reader_portion
        self.assertEqual(reader_portion("## T\n본문"), "## T\n본문")

    def test_narrative_rendered_as_markdown(self):
        """`##` 가 글자로 보이면 안 된다."""
        h = report.build_report_html(
            papers=[{"title": "P"}],
            timeline_narrative="## 제목\n\n**굵게** 본문")
        import re as _re
        m = _re.search(r'<div class="tl-narr">(.*?)</div>', h, _re.S)
        self.assertIsNotNone(m)
        inner = m.group(1)
        self.assertIn("<strong>굵게</strong>", inner)
        self.assertNotIn("## 제목", inner)


class TimelineOverviewTests(unittest.TestCase):
    """그림 아래 첫 글은 **줄글 개요**여야 한다.

    스트림별 항목 나열은 이미 그림이 하는 일이다. 독자가 먼저 알아야 할 것은
    "무엇이 생겼고 사라졌고 갈라졌고 합쳐졌는가" 라는 시간의 서사다.
    """

    def _html(self, **kw):
        kw.setdefault("papers", [{"title": "P"}])
        return report.build_report_html(**kw)

    def test_overview_precedes_stream_detail(self):
        h = self._html(timeline_uri="data:image/png;base64,AAA",
                       timeline_overview="줄글 개요.",
                       timeline_narrative="### STREAM: a\n세부")
        self.assertLess(h.index('<div class="tl-over">'),
                        h.index('<div class="tl-narr">'))

    def test_image_precedes_overview(self):
        h = self._html(timeline_uri="data:image/png;base64,AAA",
                       timeline_overview="줄글 개요.")
        self.assertLess(h.index("base64,AAA"), h.index('<div class="tl-over">'))

    def test_blank_line_splits_paragraphs(self):
        """줄글은 문단으로 끊어 읽힌다 — 한 덩어리로 뭉치면 안 된다."""
        h = self._html(timeline_overview="가.\n\n나.\n\n다.")
        import re as _re
        inner = _re.search(r'<div class="tl-over">(.*?)</div>', h, _re.S).group(1)
        self.assertEqual(inner.count("<p>"), 3)

    def test_overview_alone_renders_section(self):
        """그림이 실패해도 개요만으로 절이 성립한다."""
        h = self._html(timeline_overview="개요만 있다.")
        self.assertIn('<div class="tl-over">', h)

    def test_overview_is_escaped(self):
        h = self._html(timeline_overview="<script>alert(1)</script>")
        self.assertNotIn("<script>alert(1)</script>", h)

    def test_prompt_demands_prose_and_temporal_focus(self):
        """항목 나열이 아니라 줄글이어야 하고, 시간축 변화를 요구해야 한다."""
        from lib.citedby import timeline as TL
        p = TL._NARRATIVE_PROMPT
        self.assertIn("OVERVIEW", p)
        self.assertIn("flowing prose", p)
        self.assertIn("no bullet points", p)
        for concept in ("appeared", "faded", "split into branches", "converged"):
            with self.subTest(concept=concept):
                self.assertIn(concept, p)
        self.assertIn("research group", p)   # 연구 그룹 강조
        self.assertIn("hinge", p)            # turning point 논문

    def test_overview_language_follows_report(self):
        from lib.citedby import timeline as TL
        self.assertEqual(TL._LANG_NAMES["ko"], "Korean")
        self.assertEqual(TL._LANG_NAMES["en"], "English")
        self.assertIn("{lang_name}", TL._NARRATIVE_PROMPT)

    def test_overview_kept_out_of_drawing_spec(self):
        """개요는 별도 필드다 — method_text 에 섞여 그림에 새면 안 된다."""
        from lib.citedby.timeline import TimelineResult
        r = TimelineResult(uri="u", narrative="n", caption="c", overview="o")
        self.assertEqual(r.overview, "o")
        self.assertNotIn("o", r.narrative)


class TimelineOverviewLangTests(unittest.TestCase):
    """개요는 리포트 언어로 쓴다.

    프롬프트 전체가 영어(그림 생성기용)라, 언어를 한 번만 적으면 모델이
    그대로 영어로 써 버린다 — 실제로 그렇게 나왔다.
    """

    def _render(self, lang):
        from lib.citedby.timeline import _NARRATIVE_PROMPT as P, _LANG_NAMES
        return P.format(seed="S", short_seed="S", total=1, span="s",
                        themes="t", lang_name=_LANG_NAMES[lang])

    def test_language_instruction_is_emphatic(self):
        r = self._render("ko")
        self.assertIn("NOT IN ENGLISH", r)
        self.assertGreaterEqual(r.count("Korean"), 3)

    def test_technical_terms_stay_english(self):
        """한국어 문장 안에 영어 기술 용어 — paper-curation 전체 관례."""
        self.assertIn("do not translate them", self._render("ko"))

    def test_english_report_asks_for_english(self):
        r = self._render("en")
        self.assertIn("English", r)
        self.assertNotIn("Korean", r)

    def test_research_group_hint_is_actionable(self):
        """'그룹을 언급하라'만으론 근거가 없다 — 어디서 찾을지 알려줘야 한다."""
        r = self._render("ko")
        self.assertIn("repeated author", r)


class WallClockTests(unittest.TestCase):
    """산출물 시각은 상속된 TZ 에 흔들리면 안 된다.

    에이전트 하네스가 TZ=America/Los_Angeles 를 물려줘서, 11:16 에 만든 리포트가
    `report_260725_1916.html` 로 저장됐다 — 16시간 어긋나 목록이 시간순으로
    정렬되지 않았다. cron·launchd·원격 SSH 도 같은 함정에 빠진다.
    """

    def test_now_local_ignores_TZ_env(self):
        import os, time
        from lib.dateutil import now_local
        before = now_local().strftime("%Y%m%d_%H%M")
        old = os.environ.get("TZ")
        try:
            os.environ["TZ"] = "America/Los_Angeles"
            time.tzset()
            self.assertEqual(now_local().strftime("%Y%m%d_%H%M"), before)
        finally:
            if old is None:
                os.environ.pop("TZ", None)
            else:
                os.environ["TZ"] = old
            time.tzset()

    def test_explicit_override_is_honoured(self):
        """운영자가 명시하면 그것을 따른다."""
        import os
        from lib.dateutil import machine_tz
        old = os.environ.get("PAPER_CURATION_TZ")
        try:
            os.environ["PAPER_CURATION_TZ"] = "UTC"
            self.assertEqual(str(machine_tz()), "UTC")
        finally:
            if old is None:
                os.environ.pop("PAPER_CURATION_TZ", None)
            else:
                os.environ["PAPER_CURATION_TZ"] = old

    def test_unknown_zone_falls_back_not_crashes(self):
        import os
        from lib.dateutil import machine_tz, now_local
        old = os.environ.get("PAPER_CURATION_TZ")
        try:
            os.environ["PAPER_CURATION_TZ"] = "Not/AZone"
            self.assertIsNone(machine_tz())
            self.assertIsNotNone(now_local())   # 죽지 않는다
        finally:
            if old is None:
                os.environ.pop("PAPER_CURATION_TZ", None)
            else:
                os.environ["PAPER_CURATION_TZ"] = old

    def test_no_raw_datetime_now_in_stamp_paths(self):
        """다시 새지 않도록 호출부를 고정한다."""
        import pathlib
        root = pathlib.Path(__file__).resolve().parents[1]
        for rel in ("run_citedby.py", "serve_local.py", "lib/citedby/report.py"):
            src = (root / rel).read_text(encoding="utf-8")
            for line in src.splitlines():
                if "strftime" in line and "%y%m%d_%H%M" in line or (
                        "strftime" in line and "%Y-%m-%d %H:%M" in line):
                    with self.subTest(rel=rel, line=line.strip()[:60]):
                        self.assertNotIn("datetime.now()", line)


class StreamCardTests(unittest.TestCase):
    """스트림은 항목 나열이 아니라 카드다 — 배지·흐름 단락·근거 링크.

    예전엔 `Relative size: LARGE` 같은 줄이 본문으로 흘러 세로로 길어지고,
    논문은 글자로만 적혀 독자가 아래 목록에서 눈으로 찾아야 했다.
    """

    PAPERS = [{"title": "The Virtual Lab: AI Agents Design New Nanobodies"},
              {"title": "GeoFactory: automated geospatial workflows"}]
    STREAM = [{"name": "Autonomous agents", "start": 2024, "end": 2026,
               "trend": "ACCELERATING", "size": "LARGE", "influence": "HIGH",
               "summary": "The Virtual Lab: AI Agents Design New Nanobodies 가 문을 열었다.",
               "papers": ["The Virtual Lab: AI Agents Design New Nanobodies",
                          "GeoFactory: automated geospatial workflows"],
               "interaction": "MERGE INTO 지식 표현"}]

    def _html(self, **kw):
        kw.setdefault("papers", self.PAPERS)
        return report.build_report_html(**kw)

    def test_paper_cards_have_anchors(self):
        h = self._html()
        self.assertIn('<article class="card" id="p1"', h)
        self.assertIn('<article class="card" id="p2"', h)

    def test_stream_renders_as_card_with_badges(self):
        h = self._html(timeline_streams=self.STREAM)
        self.assertIn('class="stc"', h)
        self.assertIn('class="sbs"', h)
        for token in ("2024–2026", "Accelerating", "Large", "High"):
            with self.subTest(token=token):
                self.assertIn(token, h)

    def test_size_and_influence_are_not_body_lines(self):
        """등급은 배지다 — 본문 줄로 흘러 세로로 길어지면 안 된다."""
        h = self._html(timeline_streams=self.STREAM)
        self.assertNotIn("<p>Relative size", h)
        self.assertNotIn("<p>Influence", h)

    def test_stream_papers_link_to_cards(self):
        h = self._html(timeline_streams=self.STREAM)
        self.assertIn('<a class="pref" href="#p1"', h)
        self.assertIn('<a class="pref" href="#p2"', h)

    def test_stream_has_prose_paragraph(self):
        h = self._html(timeline_streams=self.STREAM)
        self.assertIn("문을 열었다", h)

    def test_titles_in_prose_are_linkified(self):
        """줄글 안에 글자로만 적힌 제목도 카드로 보낸다."""
        h = self._html(timeline_overview="연구 GeoFactory: automated geospatial workflows 가 나왔다.")
        self.assertIn('<a class="pref" href="#p2">', h)

    def test_unknown_title_degrades_not_breaks(self):
        st = [dict(self.STREAM[0], papers=["Never Seen This Title At All"])]
        h = self._html(timeline_streams=st)
        self.assertIn('class="pref off"', h)   # 링크 없이 표시만
        self.assertNotIn('href="#pNone"', h)

    def test_linkify_skips_inside_existing_anchor(self):
        from lib.citedby.report import _linkify_papers
        src = '<a href="x">GeoFactory: automated geospatial workflows</a>'
        self.assertEqual(_linkify_papers(src, self.PAPERS), src)

    def test_linkify_once_per_paper(self):
        from lib.citedby.report import _linkify_papers
        ttl = "GeoFactory: automated geospatial workflows"
        got = _linkify_papers(f"<p>{ttl} 그리고 {ttl}</p>", self.PAPERS)
        self.assertEqual(got.count('href="#p2"'), 1)

    def test_streams_take_precedence_over_markdown(self):
        """구조화된 streams 가 있으면 옛 마크다운 덤프는 쓰지 않는다."""
        h = self._html(timeline_streams=self.STREAM,
                       timeline_narrative="### STREAM: 옛날 마크다운")
        self.assertIn('class="stc"', h)
        self.assertNotIn("옛날 마크다운", h)

    def test_markdown_fallback_when_no_streams(self):
        h = self._html(timeline_narrative="### STREAM: 폴백 경로")
        self.assertIn("폴백 경로", h)


class TopBarAudioTests(unittest.TestCase):
    """PDF 출력 옆에서 바로 오디오. 질문을 던지지 않고도 듣고 싶다.

    기존 오디오 버튼은 Deep Research 패널 안에만 있어서, 답변을 받아야만
    누를 수 있었다. 리포트 자체를 듣고 싶은 경우를 막고 있었다.
    """

    def _html(self, **kw):
        kw.setdefault("papers", [{"title": "P"}])
        return report.build_report_html(**kw)

    def test_button_sits_next_to_pdf(self):
        h = self._html(deep_index="_citedby_index.json")
        self.assertIn('id="rpAudio"', h)
        self.assertLess(h.index("citedbyPrint()"), h.index("rpAudio"))
        self.assertLess(h.index("rpAudio"), h.index('class="hint"'))

    def test_button_absent_without_audio_module(self):
        """모듈이 안 실리면 눌러도 아무 일 없는 버튼이 남으면 안 된다."""
        h = self._html()
        self.assertNotIn("rpAudio", h)

    def test_button_wired_to_shared_modal(self):
        h = self._html(deep_index="_citedby_index.json")
        self.assertIn('getElementById("rpAudio")', h)
        self.assertIn("openAudioModal", h)

    def test_provider_falls_back_to_report_body(self):
        """답변이 없으면 개요와 스트림을 읽는다."""
        from lib.citedby.deep_panel import AUDIO_PROVIDER_JS as A
        self.assertIn("if (L.answer)", A)      # 답변 있으면 그것
        self.assertIn(".tl-over", A)           # 없으면 개요
        self.assertIn(".stc", A)               # 그리고 스트림
        self.assertIn(".card", A)              # 논문은 근거로

    def test_provider_is_valid_js(self):
        import subprocess, tempfile, pathlib
        from lib.citedby.deep_panel import AUDIO_PROVIDER_JS as A
        f = pathlib.Path(tempfile.mktemp(suffix=".js"))
        f.write_text(A, encoding="utf-8")
        r = subprocess.run(["node", "--check", str(f)],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr[:300])


class TimelineFailureVisibilityTests(unittest.TestCase):
    """그림이 없으면 **왜 없는지** 남긴다.

    기본값을 켜면서 예외만 격리하고 사유를 버렸더니, 15분 기다린 뒤 빈손으로
    남은 사람이 다시 돌릴지 판단할 근거가 없었다. 실제로 원인을 사후에 찾지
    못했다.
    """

    def _html(self, **kw):
        kw.setdefault("papers", [{"title": "P"}])
        return report.build_report_html(**kw)

    def test_reason_shown_when_image_missing(self):
        h = self._html(timeline_overview="개요.", timeline_failure="1800초 초과")
        self.assertIn('class="tl-fail"', h)
        self.assertIn("1800초 초과", h)

    def test_analysis_survives_and_stays_useful(self):
        """그림만 없을 뿐 갈래 설명은 그대로 유효하다고 알린다."""
        h = self._html(timeline_overview="개요.", timeline_failure="x")
        self.assertIn("유효", h)
        self.assertIn('<div class="tl-over">', h)

    def test_no_notice_when_image_present(self):
        h = self._html(timeline_uri="data:image/png;base64,A",
                       timeline_failure="x")
        self.assertNotIn('class="tl-fail"', h)

    def test_timeout_is_1800(self):
        """운영자 지시 — 900초로는 후보 3개 × critic round 가 빠듯했다."""
        from lib.citedby import timeline as TL
        self.assertEqual(TL.WALL_TIMEOUT_S, 1800)

    def test_timeout_result_carries_reason(self):
        from lib.citedby.timeline import TimelineResult, WALL_TIMEOUT_S
        r = TimelineResult(overview="o", failure=f"{WALL_TIMEOUT_S}초 초과")
        self.assertIn("1800", r.failure)
        self.assertFalse(r)          # uri 없으니 falsy

    def test_candidate_errors_are_collected(self):
        """후보별 예외를 로그에만 남기면 사후에 못 본다."""
        from lib.citedby import timeline as TL
        errs: list[str] = []
        with patch.object(TL, "CRITIC_ROUNDS", 0), \
             patch("lib.paperbanana.generate_diagram",
                   side_effect=RuntimeError("boom")):
            got = TL._generate_candidates("m", "c", "/tmp", 2, None, errs)
        self.assertEqual(got, [])
        self.assertEqual(len(errs), 2)
        self.assertIn("RuntimeError", errs[0])
        self.assertIn("boom", errs[0])

    def test_missing_paperbanana_names_itself(self):
        from lib.citedby import timeline as TL
        with patch.dict("sys.modules", {"lib.paperbanana": None}):
            r = TL.generate({"clusters": [{"name": "a", "count": 1,
                                           "citations": 0, "years": {},
                                           "keywords": [], "titles": []}],
                             "years": [2024], "total": 1})
        self.assertEqual(r.uri, "")
        self.assertIn("PaperBanana", r.failure)
