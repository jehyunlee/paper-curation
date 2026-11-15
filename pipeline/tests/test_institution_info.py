"""Paper Curio's "View Research Institute Info" page (pipeline/institution_info.py)."""
from __future__ import annotations

import contextlib
import io
import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import build_bibliography_db as bib
import institution_info as info


def _db(path: Path) -> None:
    conn = sqlite3.connect(path)
    conn.executescript(bib.SCHEMA)
    conn.execute("INSERT INTO papers (paper_id, slug, title, doi, review_dir) VALUES "
                 "(1, '042_x', 'A <Paper>', '10.1/x', 'docs/papers/042_x')")
    for iid, name, parent, city, country, ror in (
            (10, "IBM Research - Zurich", "IBM", "Rüschlikon", "Switzerland", "https://ror.org/zrl"),
            (11, "Stanford University", "Stanford University", "Stanford", "United States", "")):
        conn.execute(
            "INSERT INTO institutions (institution_id, institution_name, normalized_name, "
            "parent_name, city_name, country_name_en, ror_id, source) VALUES (?,?,?,?,?,?,?,?)",
            (iid, name, name.lower(), parent, city, country, ror, "test"))
        conn.execute("INSERT INTO paper_institutions VALUES (1, ?, ?, '', 'scopus+pdf')",
                     (iid, name))
    for aid, name, order in ((1, "Ada Marked", 1), (2, "Bo Guessed", 2), (3, "Cy None", 3)):
        conn.execute("INSERT INTO authors (author_id, display_name, normalized_name) "
                     "VALUES (?,?,?)", (aid, name, name.lower()))
        conn.execute("INSERT INTO paper_authors VALUES (1, ?, ?, ?, 0, 'test')",
                     (aid, order, int(order == 1)))
    links = [(1, 10, "pdf.byline-marker"), (1, 11, "pdf.unmarked-multi"),
             (2, 10, "pdf.unmarked-multi"), (2, 11, "pdf.unmarked-multi")]
    conn.executemany("INSERT INTO paper_author_institutions (paper_id, author_id, "
                     "institution_id, marker, author_order, source) VALUES (1,?,?,NULL,1,?)",
                     links)
    conn.commit()
    conn.close()


class InstitutionInfoTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.dir = Path(tmp.name)
        self.db = self.dir / "bib.sqlite3"
        _db(self.db)

    def run_main(self, *args):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = info.main(["--db", str(self.db), *args])
        return code, json.loads(out.getvalue().strip().splitlines()[-1])

    def test_paper_page_lists_four_fields_and_author_links(self):
        page = self.dir / "out" / "042_x.html"
        code, receipt = self.run_main("--slug", "042_x", "--out", str(page))
        self.assertEqual(code, 0)
        self.assertEqual(receipt, {"schema_version": 1, "slug": "042_x", "ok": True,
                                   "report": str(page), "institutions": 2, "authors": 3})
        html = page.read_text(encoding="utf-8")
        for value in ("IBM Research - Zurich", "Rüschlikon", "Switzerland",
                      "Stanford University", "United States", "Scopus·PDF 일치"):
            self.assertIn(value, html)
        self.assertIn('<a href="https://ror.org/zrl"', html)
        self.assertIn("A &lt;Paper&gt;", html)
        self.assertNotIn("A <Paper>", html)

    def test_guessed_author_links_are_not_shown_as_affiliations(self):
        conn = info.connect(self.db)
        try:
            authors = info.collect(conn, "042_x")["authors"]
        finally:
            conn.close()
        self.assertEqual([(a["name"], a["institutions"], a["unknown"]) for a in authors], [
            ("Ada Marked", ["IBM Research - Zurich"], False),
            ("Bo Guessed", [], True),
            ("Cy None", [], False),
        ])

    def test_english_page(self):
        page = self.dir / "en.html"
        self.run_main("--slug", "042_x", "--out", str(page), "--lang", "en")
        html = page.read_text(encoding="utf-8")
        self.assertIn("Research institute info", html)
        self.assertIn("byline does not say which author sits where", html)

    def test_paper_missing_from_db_is_not_ingested(self):
        page = self.dir / "missing.html"
        code, receipt = self.run_main("--slug", "999_none", "--out", str(page))
        self.assertEqual(code, 1)
        self.assertEqual(receipt["reason"], "not-ingested")
        self.assertFalse(page.exists())

    def test_missing_db(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = info.main(["--db", str(self.dir / "absent.sqlite3"), "--slug", "042_x",
                              "--out", str(self.dir / "x.html")])
        self.assertEqual(code, 1)
        self.assertEqual(json.loads(out.getvalue())["reason"], "no-db")

    def test_db_is_opened_read_only(self):
        conn = info.connect(self.db)
        try:
            with self.assertRaises(sqlite3.OperationalError):
                conn.execute("DELETE FROM papers")
        finally:
            conn.close()


if __name__ == "__main__":
    unittest.main()
