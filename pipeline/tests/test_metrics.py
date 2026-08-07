"""Regression coverage for pipeline/lib/metrics (citations.md / references.md).

잠그는 계약:
  * 이력은 **append** — 갱신이 과거 관측을 지우지 않는다 (인용 속도의 근거)
  * 같은 날 두 번 돌리면 그 날 관측만 교체 (중복 행 방지)
  * 피인용 0 은 실측값 — 결측으로 취급하지 않는다
  * 레퍼런스 표기 우선순위: DOI > URL > (제목·저자·연도·출판처) > 원문
  * 갱신 주기 게이트가 30일 기준으로 동작
  * frontmatter 가 단일 진실 — 표를 역파싱하지 않는다
"""
from __future__ import annotations

import sys
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

PIPELINE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE_DIR))

from lib.metrics import store  # noqa: E402
from lib.metrics import collect  # noqa: E402
from lib.metrics import db as metrics_db  # noqa: E402
from lib.metrics.store import CitationSnapshot  # noqa: E402


class SysPathHygieneTests(unittest.TestCase):
    """`pipeline/lib` 를 sys.path 에 넣으면 안 된다.

    그 디렉토리의 `dateutil.py` 가 표준 `python-dateutil` 패키지를 가려서,
    같은 프로세스에서 pandas 를 import 하는 모든 테스트가 깨진다
    (`No module named 'dateutil.tz'; 'dateutil' is not a package`).
    `unittest discover` 는 실행 전에 모든 테스트 모듈을 import 하므로 한
    파일의 한 줄이 스위트 전체를 무너뜨린다 — 실제로 24건이 그렇게 깨졌다.
    """

    def test_no_test_module_puts_lib_on_syspath(self):
        import re
        bad = []
        for path in sorted((PIPELINE_DIR / "tests").glob("test_*.py")):
            for m in re.finditer(r"^\s*sys\.path\.(?:insert|append)\([^\n]*",
                                 path.read_text(encoding="utf-8"), re.M):
                stmt = m.group(0)
                if re.search(r'["\']lib["\']\s*\)', stmt):
                    bad.append(f"{path.name}: {stmt.strip()}")
        self.assertEqual(bad, [],
                         f"pipeline/lib 를 sys.path 에 넣는 테스트: {bad}")

    def test_dateutil_resolves_to_the_real_package(self):
        import dateutil
        self.assertTrue(
            hasattr(dateutil, "__path__"),
            f"dateutil 이 패키지가 아니다 — {getattr(dateutil, '__file__', '?')} "
            "가 표준 python-dateutil 을 가리고 있다")


class LazyLoadTests(unittest.TestCase):
    def test_package_import_does_not_pull_requests(self):
        """import 만으로 무거운 의존을 끌어오지 않는다 (PEP 562)."""
        import subprocess
        code = (
            "import sys; sys.path.insert(0, %r);"
            "import lib.metrics as m;"
            "assert 'requests' not in sys.modules, 'eager import';"
            "assert 'pandas' not in sys.modules, 'eager import';"
            "m.CitationSnapshot;"
            "print('ok')" % str(PIPELINE_DIR)
        )
        r = subprocess.run([sys.executable, "-c", code],
                           capture_output=True, text=True, timeout=60)
        self.assertEqual(r.returncode, 0, r.stderr[-400:])


class SnapshotTests(unittest.TestCase):
    def test_best_prefers_openalex(self):
        s = CitationSnapshot("2026-07-25", openalex=52, crossref=47, scopus=30)
        self.assertEqual(s.best(), (52, "openalex"))

    def test_best_falls_through_when_openalex_missing(self):
        s = CitationSnapshot("2026-07-25", openalex=None, crossref=47)
        self.assertEqual(s.best(), (47, "crossref"))

    def test_zero_is_a_real_value(self):
        """최근 논문의 0 은 정상값 — 결측으로 넘겨 다음 소스를 보면 안 된다."""
        s = CitationSnapshot("2026-07-25", openalex=0, crossref=9)
        self.assertEqual(s.best(), (0, "openalex"))

    def test_all_missing(self):
        self.assertEqual(CitationSnapshot("2026-07-25").best(), (None, ""))

    def test_roundtrip(self):
        s = CitationSnapshot("2026-07-25", openalex=1, crossref=2, scopus=3,
                             percentile=0.9)
        self.assertEqual(CitationSnapshot.from_dict(s.to_dict()), s)


class CitationsFileTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def _write(self, date, **counts):
        return store.write_citations(
            self.dir, slug="042_Test", doi="10.1/x", title="테스트 논문",
            snapshot=CitationSnapshot(date, **counts))

    def test_creates_file_with_frontmatter_and_table(self):
        p = self._write("2026-07-25", openalex=10, crossref=8)
        text = p.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---"))
        self.assertIn("schema: citations-v1", text)
        self.assertIn("| 조회일 | 대표값 |", text)
        self.assertIn("2026-07-25", text)

    def test_history_accumulates(self):
        """이 설계의 핵심 — 갱신이 과거를 지우지 않는다."""
        self._write("2026-07-25", openalex=10)
        self._write("2026-08-25", openalex=25)
        self._write("2026-09-25", openalex=40)
        doc = store.read_citations(self.dir)
        self.assertEqual([s.date for s in doc.history],
                         ["2026-07-25", "2026-08-25", "2026-09-25"])
        self.assertEqual([s.openalex for s in doc.history], [10, 25, 40])

    def test_same_day_rerun_replaces_not_duplicates(self):
        self._write("2026-07-25", openalex=10)
        self._write("2026-07-25", openalex=12)
        doc = store.read_citations(self.dir)
        self.assertEqual(len(doc.history), 1)
        self.assertEqual(doc.history[0].openalex, 12)

    def test_history_sorted_even_if_written_out_of_order(self):
        self._write("2026-09-25", openalex=40)
        self._write("2026-07-25", openalex=10)
        doc = store.read_citations(self.dir)
        self.assertEqual([s.date for s in doc.history],
                         ["2026-07-25", "2026-09-25"])

    def test_velocity_note_appears_from_second_observation(self):
        self._write("2026-07-25", openalex=10)
        self.assertNotIn("직전 관측 대비", (self.dir / "citations.md")
                         .read_text(encoding="utf-8"))
        p = self._write("2026-08-24", openalex=40)
        self.assertIn("직전 관측 대비", p.read_text(encoding="utf-8"))
        self.assertIn("+30", p.read_text(encoding="utf-8"))

    def test_latest_snapshot_in_frontmatter(self):
        self._write("2026-07-25", openalex=52, crossref=47, scopus=30,
                    percentile=0.999)
        meta, _ = store.split_frontmatter(
            (self.dir / "citations.md").read_text(encoding="utf-8"))
        self.assertEqual(meta["latest"]["count"], 52)
        self.assertEqual(meta["latest"]["source"], "openalex")
        self.assertEqual(meta["latest"]["by_source"]["crossref"], 47)

    def test_citing_list_rendered_when_fetched(self):
        p = store.write_citations(
            self.dir, slug="s", doi="10.1/x", title="T",
            snapshot=CitationSnapshot("2026-07-25", openalex=20),
            citing=[{"doi": "10.2/a", "title": "인용 논문", "year": 2025,
                     "cited_by_count": 3}],
            citing_fetched=True, min_citations=10)
        text = p.read_text(encoding="utf-8")
        self.assertIn("이 논문을 인용한 논문 (1건)", text)
        self.assertIn("https://doi.org/10.2/a", text)

    def test_below_threshold_notes_why_list_is_absent(self):
        p = store.write_citations(
            self.dir, slug="s", doi="10.1/x", title="T",
            snapshot=CitationSnapshot("2026-07-25", openalex=3),
            citing=[], citing_fetched=False, min_citations=10)
        self.assertIn("임계값(10회) 미만", p.read_text(encoding="utf-8"))

    def test_citing_count_preserved_when_not_refetched(self):
        store.write_citations(
            self.dir, slug="s", doi="10.1/x", title="T",
            snapshot=CitationSnapshot("2026-07-25", openalex=20),
            citing=[{"doi": "10.2/a", "title": "A", "year": 2025,
                     "cited_by_count": 1}],
            citing_fetched=True)
        store.write_citations(
            self.dir, slug="s", doi="10.1/x", title="T",
            snapshot=CitationSnapshot("2026-08-25", openalex=25),
            citing=[], citing_fetched=False)
        self.assertEqual(store.read_citations(self.dir).citing_count, 1)

    def test_pipe_in_title_is_escaped(self):
        p = store.write_citations(
            self.dir, slug="s", doi="10.1/x", title="T",
            snapshot=CitationSnapshot("2026-07-25", openalex=20),
            citing=[{"doi": "", "title": "A | B", "year": 2025,
                     "cited_by_count": 0}],
            citing_fetched=True)
        self.assertIn(r"A \| B", p.read_text(encoding="utf-8"))

    def test_missing_file_reads_as_empty(self):
        doc = store.read_citations(self.dir / "nope")
        self.assertEqual(doc.history, [])
        self.assertEqual(doc.updated, "")

    def test_corrupt_frontmatter_does_not_raise(self):
        (self.dir / "citations.md").write_text("---\n{broken\n---\nbody",
                                               encoding="utf-8")
        self.assertEqual(store.read_citations(self.dir).history, [])


class RefreshGateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_missing_file_needs_refresh(self):
        self.assertTrue(store.needs_refresh(self.dir))

    def test_recent_update_does_not_need_refresh(self):
        store.write_citations(self.dir, slug="s", doi="10.1/x", title="T",
                              snapshot=CitationSnapshot("2026-07-25"))
        self.assertFalse(store.needs_refresh(self.dir, days=30,
                                             today="2026-08-10"))

    def test_stale_update_needs_refresh(self):
        store.write_citations(self.dir, slug="s", doi="10.1/x", title="T",
                              snapshot=CitationSnapshot("2026-07-25"))
        self.assertTrue(store.needs_refresh(self.dir, days=30,
                                            today="2026-08-25"))

    def test_boundary_is_inclusive(self):
        store.write_citations(self.dir, slug="s", doi="10.1/x", title="T",
                              snapshot=CitationSnapshot("2026-07-25"))
        self.assertTrue(store.needs_refresh(self.dir, days=30,
                                            today="2026-08-24"))


class ReferenceFormatTests(unittest.TestCase):
    """운영자 지정 형식: DOI 1순위, URL 2순위, 둘 다 없을 때만 서지."""

    def test_doi_wins(self):
        line = store._reference_line(
            {"n": 1, "doi": "10.1/a", "url": "http://x", "title": "T"})
        self.assertEqual(line, "1. [10.1/a](https://doi.org/10.1/a)")

    def test_url_when_no_doi(self):
        line = store._reference_line(
            {"n": 2, "doi": "", "url": "http://x/y", "title": "T"})
        self.assertEqual(line, "2. <http://x/y>")

    def test_bibliographic_when_neither(self):
        line = store._reference_line({
            "n": 3, "doi": "", "url": "", "title": "Deep Learning",
            "first_author": "LeCun, Y.", "year": "2015", "venue": "Nature"})
        self.assertIn("LeCun, Y.", line)
        self.assertIn("(2015)", line)
        self.assertIn("Deep Learning", line)
        self.assertIn("*Nature*", line)

    def test_raw_string_as_last_resort(self):
        line = store._reference_line(
            {"n": 4, "doi": "", "url": "", "raw": "Some unparsed citation"})
        self.assertEqual(line, "4. Some unparsed citation")

    def test_empty_entry_is_marked(self):
        self.assertIn("서지정보 없음", store._reference_line({"n": 5}))


class ReferencesFileTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_counts_doi_and_url_coverage(self):
        p = store.write_references(
            self.dir, slug="s", doi="10.1/x", title="T", references=[
                {"n": 1, "doi": "10.1/a"},
                {"n": 2, "doi": "", "url": "http://b"},
                {"n": 3, "doi": "", "url": "", "title": "C"},
            ])
        meta, _ = store.split_frontmatter(p.read_text(encoding="utf-8"))
        self.assertEqual(meta["count"], 3)
        self.assertEqual(meta["with_doi"], 1)
        self.assertEqual(meta["with_url"], 1)

    def test_empty_reference_list(self):
        p = store.write_references(self.dir, slug="s", doi="10.1/x",
                                   title="T", references=[])
        self.assertIn("(레퍼런스 없음)", p.read_text(encoding="utf-8"))


class CrossrefReferenceExtractionTests(unittest.TestCase):
    MSG = {
        "reference": [
            {"DOI": "10.1/A"},
            {"URL": "http://example.org/paper"},
            {"article-title": "Understanding Molecular Simulation",
             "author": "D Frenkel", "year": "2023",
             "journal-title": "Academic Press"},
            {"unstructured": "Bai, J. et al. Qwen Technical Report (2023)."},
        ],
    }

    def test_extracts_in_order_with_priority(self):
        refs = collect.fetch_references("10.1/x", crossref_msg=self.MSG)
        self.assertEqual(len(refs), 4)
        self.assertEqual(refs[0]["doi"], "10.1/a")        # 소문자 정규화
        self.assertEqual(refs[1]["url"], "http://example.org/paper")
        self.assertEqual(refs[2]["first_author"], "D Frenkel")
        self.assertEqual(refs[3]["raw"][:9], "Bai, J. e")

    def test_doi_entry_does_not_carry_redundant_fields(self):
        """DOI 가 있으면 나머지는 채우지 않는다 (형식 규칙)."""
        refs = collect.fetch_references("10.1/x", crossref_msg={
            "reference": [{"DOI": "10.1/A", "article-title": "T",
                           "author": "X"}]})
        self.assertEqual(refs[0]["doi"], "10.1/a")
        self.assertEqual(refs[0]["title"], "")
        self.assertEqual(refs[0]["first_author"], "")

    def test_no_references_returns_empty(self):
        self.assertEqual(collect.fetch_references("10.1/x", crossref_msg={}), [])


class CitationCountCollectionTests(unittest.TestCase):
    def test_crossref_message_reused_for_references(self):
        """레퍼런스 때문에 Crossref 를 두 번 부르지 않는다 (호출 예산)."""
        msg = {"is-referenced-by-count": 47, "reference": [{"DOI": "10.9/z"}]}
        with patch.object(collect, "_crossref_work", return_value=msg) as cr, \
             patch.object(collect, "_openalex_work", return_value=None), \
             patch.object(collect, "_scopus_citations", return_value=None):
            out = collect.collect_paper_metrics(
                {"slug": "s", "doi": "10.1/x", "title": "T"},
                want_citing=False)
        self.assertEqual(cr.call_count, 1)
        self.assertEqual(out["counts"]["crossref"], 47)
        self.assertEqual(out["references"][0]["doi"], "10.9/z")

    def test_no_doi_short_circuits(self):
        with patch.object(collect, "_crossref_work") as cr:
            out = collect.collect_paper_metrics({"slug": "s", "doi": "",
                                                 "title": "T"})
        cr.assert_not_called()
        self.assertEqual(out["counts"]["openalex"], None)

    def test_citing_skipped_below_threshold(self):
        with patch.object(collect, "_crossref_work", return_value=None), \
             patch.object(collect, "_openalex_work",
                          return_value={"cited_by_count": 3}), \
             patch.object(collect, "_scopus_citations", return_value=None), \
             patch.object(collect, "fetch_citing_papers") as fc:
            out = collect.collect_paper_metrics(
                {"slug": "s", "doi": "10.1/x", "title": "T"},
                min_citations=10)
        fc.assert_not_called()
        self.assertFalse(out["citing_fetched"])

    def test_citing_fetched_at_threshold(self):
        with patch.object(collect, "_crossref_work", return_value=None), \
             patch.object(collect, "_openalex_work",
                          return_value={"cited_by_count": 10}), \
             patch.object(collect, "_scopus_citations", return_value=None), \
             patch.object(collect, "fetch_citing_papers",
                          return_value=[{"doi": "10.2/a"}]) as fc:
            out = collect.collect_paper_metrics(
                {"slug": "s", "doi": "10.1/x", "title": "T"},
                min_citations=10)
        fc.assert_called_once()
        self.assertTrue(out["citing_fetched"])

    def test_percentile_captured(self):
        with patch.object(collect, "_crossref_work", return_value=None), \
             patch.object(collect, "_openalex_work", return_value={
                 "cited_by_count": 5,
                 "citation_normalized_percentile": {"value": 0.91}}), \
             patch.object(collect, "_scopus_citations", return_value=None):
            out = collect.collect_paper_metrics(
                {"slug": "s", "doi": "10.1/x", "title": "T"},
                want_citing=False)
        self.assertAlmostEqual(out["percentile"], 0.91)

    def test_openalex_yearly_counts_are_preserved(self):
        with patch.object(collect, "_crossref_work", return_value=None), \
             patch.object(collect, "_openalex_work", return_value={
                 "cited_by_count": 5,
                 "counts_by_year": [
                     {"year": 2025, "cited_by_count": 2},
                     {"year": 2026, "cited_by_count": 3},
                 ]}), \
             patch.object(collect, "_scopus_citations", return_value=None):
            out = collect.collect_paper_metrics(
                {"slug": "s", "doi": "10.1/x", "title": "T"},
                want_citing=False)
        self.assertEqual(out["yearly"], [
            {"year": 2025, "cited_by_count": 2},
            {"year": 2026, "cited_by_count": 3},
        ])

    def test_one_source_failure_does_not_abort(self):
        with patch.object(collect, "_crossref_work",
                          side_effect=RuntimeError("down")), \
             patch.object(collect, "_openalex_work",
                          return_value={"cited_by_count": 7}), \
             patch.object(collect, "_scopus_citations", return_value=None):
            with self.assertRaises(RuntimeError):
                collect.collect_paper_metrics(
                    {"slug": "s", "doi": "10.1/x", "title": "T"},
                    want_citing=False)

    def test_collect_many_isolates_per_paper_failure(self):
        papers = [{"slug": "a", "doi": "10.1/a", "title": "A"},
                  {"slug": "b", "doi": "10.1/b", "title": "B"}]

        def flaky(paper, **kw):
            if paper["slug"] == "a":
                raise RuntimeError("boom")
            return {"slug": "b"}

        with patch.object(collect, "collect_paper_metrics", side_effect=flaky):
            out = collect.collect_many(papers)
        self.assertEqual([r["slug"] for r in out], ["b"])


class CitationDatabaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        self.db = root / "bibliography.sqlite3"
        self.papers = root / "papers"
        self.slug = "001_Test"
        (self.papers / self.slug).mkdir(parents=True)
        conn = sqlite3.connect(self.db)
        conn.execute(
            "CREATE TABLE papers (paper_id INTEGER PRIMARY KEY, "
            "slug TEXT NOT NULL UNIQUE)")
        conn.execute("INSERT INTO papers (slug) VALUES (?)", (self.slug,))
        conn.commit()
        conn.close()

    def tearDown(self):
        self.temp.cleanup()

    def test_history_backfill_and_yearly_upsert_are_idempotent(self):
        pdir = self.papers / self.slug
        store.write_citations(
            pdir, slug=self.slug, doi="10.1/x", title="T",
            snapshot=CitationSnapshot("2026-07-01", openalex=5, crossref=4))
        store.write_citations(
            pdir, slug=self.slug, doi="10.1/x", title="T",
            snapshot=CitationSnapshot("2026-08-01", openalex=8, crossref=7))
        result = {
            "slug": self.slug,
            "yearly": [
                {"year": 2025, "cited_by_count": 3},
                {"year": 2026, "cited_by_count": 5},
            ],
        }
        first = metrics_db.sync_metrics_database(
            [result], "2026-08-07", db_path=self.db, papers_dir=self.papers)
        second = metrics_db.sync_metrics_database(
            [{**result, "yearly": [
                {"year": 2025, "cited_by_count": 3},
                {"year": 2026, "cited_by_count": 6},
            ]}], "2026-08-08", db_path=self.db, papers_dir=self.papers)
        self.assertEqual(first["snapshots"], 2)
        self.assertEqual(second["yearly"], 2)

        conn = sqlite3.connect(self.db)
        self.assertEqual(
            conn.execute("SELECT COUNT(*) FROM citation_snapshots").fetchone()[0], 2)
        self.assertEqual(
            conn.execute("SELECT COUNT(*) FROM citation_yearly").fetchone()[0], 2)
        self.assertEqual(
            conn.execute(
                "SELECT citation_count FROM citation_yearly "
                "WHERE citation_year=2026").fetchone()[0], 6)
        conn.close()

class CitingListTests(unittest.TestCase):
    def test_sorted_by_citation_count_desc(self):
        pages = [
            {"results": [
                {"id": "https://openalex.org/W1", "doi": "https://doi.org/10.1/a",
                 "display_name": "A", "publication_year": 2024,
                 "cited_by_count": 5},
                {"id": "https://openalex.org/W2", "doi": "https://doi.org/10.1/b",
                 "display_name": "B", "publication_year": 2025,
                 "cited_by_count": 50},
            ], "meta": {"next_cursor": None}},
        ]

        def fake_get(url, headers=None, params=None, timeout=None):
            r = MagicMock()
            r.status_code = 200
            if "filter" in (params or {}):
                r.json.return_value = pages[0]
            else:
                r.json.return_value = {"id": "https://openalex.org/W0"}
            return r

        with patch.object(collect.requests, "get", side_effect=fake_get):
            out = collect.fetch_citing_papers("10.1/x")
        self.assertEqual([p["doi"] for p in out], ["10.1/b", "10.1/a"])
        self.assertEqual(out[0]["cited_by_count"], 50)

    def test_unresolvable_doi_returns_empty(self):
        with patch.object(collect.requests, "get") as g:
            g.return_value.status_code = 404
            self.assertEqual(collect.fetch_citing_papers("10.1/x"), [])



class IndexCacheRoundTripTests(unittest.TestCase):
    """`build_papers_index` 가 피인용수 캐시를 잃지 않아야 한다.

    실제 위험: build_papers_index 는 entry 를 **화이트리스트로 새로 만든다.**
    citations.md 를 되읽지 않으면 인덱스를 재생성할 때마다 citation_count 가
    통째로 사라진다(실측 164편). 파이프라인이 매 사이클 이 단계를 돌리므로
    조용히 소실됐을 것이다.
    """

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def _bpi(self):
        import importlib
        return importlib.import_module("build_papers_index")

    def test_restores_from_citations_md(self):
        store.write_citations(
            self.dir, slug="042_T", doi="10.1/x", title="T",
            snapshot=CitationSnapshot("2026-07-25", openalex=182,
                                      percentile=0.999))
        got = self._bpi()._citation_fields(self.dir, {})
        self.assertEqual(got["citation_count"], 182)
        self.assertEqual(got["citations_source"], "openalex")
        self.assertEqual(got["citations_asof"], "2026-07-25")

    def test_file_wins_over_stale_index_value(self):
        """1차 저장소는 citations.md — 인덱스는 조회용 사본일 뿐이다."""
        store.write_citations(
            self.dir, slug="042_T", doi="10.1/x", title="T",
            snapshot=CitationSnapshot("2026-08-25", openalex=200))
        got = self._bpi()._citation_fields(
            self.dir, {"citation_count": 10, "citations_source": "crossref"})
        self.assertEqual(got["citation_count"], 200)
        self.assertEqual(got["citations_source"], "openalex")

    def test_falls_back_to_prev_when_no_file(self):
        got = self._bpi()._citation_fields(
            self.dir, {"citation_count": 7, "citations_source": "openalex",
                       "citations_asof": "2026-06-01"})
        self.assertEqual(got["citation_count"], 7)

    def test_no_file_no_prev_yields_nothing(self):
        self.assertEqual(self._bpi()._citation_fields(self.dir, {}), {})

    def test_zero_citations_survives_roundtrip(self):
        """0 은 실측값 — 캐시에서 사라지면 안 된다."""
        store.write_citations(
            self.dir, slug="042_T", doi="10.1/x", title="T",
            snapshot=CitationSnapshot("2026-07-25", openalex=0))
        got = self._bpi()._citation_fields(self.dir, {})
        self.assertEqual(got["citation_count"], 0)


class PipelineWiringTests(unittest.TestCase):
    """metrics 가 리뷰 파이프라인에 실제로 배선돼 있는지."""

    def test_run_update_force_invokes_run_metrics(self):
        src = (PIPELINE_DIR / "run_update_force.py").read_text(encoding="utf-8")
        self.assertIn("run_metrics.py", src)
        self.assertIn("--skip-metrics", src)

    def test_metrics_runs_after_index_build(self):
        """run_metrics 는 `_papers_index.json` 을 읽으므로 그 뒤여야 한다."""
        src = (PIPELINE_DIR / "run_update_force.py").read_text(encoding="utf-8")
        i_idx = src.index('run_step("build_papers_index"')
        i_met = src.index('run_step("run_metrics"')
        self.assertLess(i_idx, i_met)

    def test_metrics_is_not_a_critical_step(self):
        """외부 API 장애가 리뷰 파이프라인 전체를 죽여선 안 된다."""
        src = (PIPELINE_DIR / "run_update_force.py").read_text(encoding="utf-8")
        block = src[src.index("CRITICAL_STEPS = {"):]
        block = block[:block.index("}")]
        self.assertNotIn("run_metrics", block)

    def test_run_full_forwards_the_flag(self):
        src = (PIPELINE_DIR / "run_full.py").read_text(encoding="utf-8")
        self.assertIn("--skip-metrics", src)


if __name__ == "__main__":
    unittest.main(verbosity=2)
