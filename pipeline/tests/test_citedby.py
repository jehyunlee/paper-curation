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
        papers = [{"title": "A", "doi": "10.1/a"}]
        with patch.object(topic_filter, "llm_json") as llm:
            out = analysis.run_topic_analysis(papers, topic="")
        llm.assert_not_called()
        self.assertEqual(out["matched"], 1)
        self.assertIn("<!DOCTYPE html>", out["report_html"])

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
