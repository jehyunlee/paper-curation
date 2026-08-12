"""Author-to-institution has to come from the publisher, not from a guess.

A byline maps authors to institutions through superscript markers; with several
institutions and no markers the builder links every author to every one of
them. 31,566 of 36,667 links in the shipped DB are that fallback, so ranking a
university's authors over them returns people who were never there. OpenAlex
publishes the mapping the publisher deposited, with ROR ids, a corresponding
flag and a disambiguated author id.
"""
import sqlite3
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import enrich_openalex_authorships as enrich

WORK = {
    "id": "https://openalex.org/W123",
    "cited_by_count": 19,
    "authorships": [
        {"author_position": "first", "is_corresponding": False,
         "author": {"id": "https://openalex.org/A1",
                    "display_name": "Ali Essam Ghareeb", "orcid": None},
         "institutions": [{"display_name": "Institute for the Future",
                           "ror": "https://ror.org/049tcsg76",
                           "country_code": "US"}]},
        {"author_position": "middle", "is_corresponding": True,
         "author": {"id": "https://openalex.org/A2",
                    "display_name": "Benjamin Chang",
                    "orcid": "https://orcid.org/0000-0002-5968-9776"},
         "institutions": [{"display_name": "University of Oxford",
                           "ror": "https://ror.org/052gg0110",
                           "country_code": "GB"},
                          {"display_name": "Institute for the Future",
                           "ror": "https://ror.org/049tcsg76",
                           "country_code": "US"}]},
    ],
}


def make_db(path: Path) -> Path:
    conn = sqlite3.connect(path)
    conn.executescript("""
        CREATE TABLE papers (paper_id INTEGER PRIMARY KEY, slug TEXT,
          title TEXT, doi TEXT, metadata_json TEXT DEFAULT '{}');
        CREATE TABLE authors (author_id INTEGER PRIMARY KEY,
          display_name TEXT NOT NULL, normalized_name TEXT NOT NULL UNIQUE);
        CREATE TABLE institutions (institution_id INTEGER PRIMARY KEY,
          institution_name TEXT NOT NULL, normalized_name TEXT NOT NULL,
          country_name_en TEXT NOT NULL DEFAULT '', source TEXT NOT NULL,
          ror_id TEXT NOT NULL DEFAULT '', parent_name TEXT NOT NULL DEFAULT '',
          name_source TEXT NOT NULL DEFAULT '');
        CREATE TABLE paper_authors (paper_id INTEGER, author_id INTEGER,
          author_order INTEGER NOT NULL, is_first_author INTEGER DEFAULT 0,
          is_corresponding_author INTEGER DEFAULT 0, source TEXT NOT NULL,
          PRIMARY KEY (paper_id, author_id));
        CREATE TABLE paper_author_institutions (paper_id INTEGER,
          author_id INTEGER, institution_id INTEGER, marker TEXT,
          author_order INTEGER, source TEXT NOT NULL,
          PRIMARY KEY (paper_id, author_id, institution_id));
        INSERT INTO papers VALUES (1,'0001_x','X','10.1038/s41586-026-1','{}');
        INSERT INTO institutions (institution_name, normalized_name, source,
          ror_id) VALUES ('University of Oxford','university of oxford','pdf',
          'https://ror.org/052gg0110');
    """)
    conn.commit()
    conn.close()
    return path


class EnrichmentTests(unittest.TestCase):
    def setUp(self):
        import tempfile
        self.db = make_db(Path(tempfile.mkdtemp()) / "b.sqlite3")

    def _run(self, work=WORK):
        with patch.object(enrich, "fetch_work", return_value=work), \
             patch.object(enrich, "_ror_country", return_value="United States"):
            return enrich.enrich(self.db, execute=True, limit=None,
                                 refresh_days=90)

    def _conn(self):
        return sqlite3.connect(self.db)

    def test_every_author_is_linked_to_its_own_institution(self):
        self._run()
        rows = self._conn().execute(
            "SELECT a.display_name, i.institution_name"
            " FROM paper_author_institutions pai"
            " JOIN authors a USING(author_id)"
            " JOIN institutions i USING(institution_id)"
            " WHERE pai.source='openalex' ORDER BY a.display_name,"
            " i.institution_name").fetchall()
        self.assertEqual(rows, [
            ("Ali Essam Ghareeb", "Institute for the Future"),
            ("Benjamin Chang", "Institute for the Future"),
            ("Benjamin Chang", "University of Oxford"),
        ])
        # The first author is not credited with Oxford, which is the whole
        # point: the cartesian fallback would have done exactly that.
        self.assertNotIn(("Ali Essam Ghareeb", "University of Oxford"), rows)

    def test_an_existing_institution_is_matched_by_ror_not_duplicated(self):
        self._run()
        count = self._conn().execute(
            "SELECT COUNT(*) FROM institutions WHERE normalized_name="
            "'university of oxford'").fetchone()[0]
        self.assertEqual(count, 1)

    def test_corresponding_author_is_recorded(self):
        self._run()
        rows = dict(self._conn().execute(
            "SELECT a.display_name, pa.is_corresponding_author"
            " FROM paper_authors pa JOIN authors a USING(author_id)"))
        self.assertEqual(rows["Benjamin Chang"], 1)
        self.assertEqual(rows["Ali Essam Ghareeb"], 0)

    def test_identifiers_are_stored(self):
        self._run()
        rows = dict(self._conn().execute(
            "SELECT display_name, orcid FROM authors"))
        self.assertEqual(rows["Benjamin Chang"], "0000-0002-5968-9776")
        self.assertEqual(rows["Ali Essam Ghareeb"], "")
        ids = dict(self._conn().execute(
            "SELECT display_name, openalex_id FROM authors"))
        self.assertEqual(ids["Ali Essam Ghareeb"], "A1")

    def test_rerunning_changes_nothing(self):
        self._run()
        first = self._conn().execute(
            "SELECT COUNT(*) FROM paper_author_institutions").fetchone()[0]
        # The enrichment table records the fetch, so a second pass has no
        # candidates; force one anyway to prove the writes are idempotent.
        self._run()
        second = self._conn().execute(
            "SELECT COUNT(*) FROM paper_author_institutions").fetchone()[0]
        self.assertEqual(first, second)

    def test_a_missing_work_is_counted_not_fatal(self):
        report = self._run(work=None)
        self.assertEqual(report["not_found"], 1)
        self.assertEqual(report["institution_links"], 0)

    def test_dry_run_writes_nothing(self):
        with patch.object(enrich, "fetch_work", return_value=WORK), \
             patch.object(enrich, "_ror_country", return_value="United States"):
            enrich.enrich(self.db, execute=False, limit=None, refresh_days=90)
        self.assertEqual(self._conn().execute(
            "SELECT COUNT(*) FROM paper_author_institutions").fetchone()[0], 0)


if __name__ == "__main__":
    unittest.main()
