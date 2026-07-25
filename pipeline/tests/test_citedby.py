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

import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

PIPELINE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE_DIR))

from lib.citedby import citing  # noqa: E402
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


if __name__ == "__main__":
    unittest.main(verbosity=2)
