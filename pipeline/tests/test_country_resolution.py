"""Country resolution contract for institutions.

`institutions.country_name_en` was empty for the whole corpus, then 67% filled
and wrong in ways no test could see: ETH Zurich sat in the United States, a CNRS
lab in Rennes sat in the United States, and East China Normal University sat in
South Korea. Every literal here is a real `paper_institutions.raw_name` from the
shipped DB, so the failure modes cannot come back silently.
"""
import sqlite3
import unittest
from pathlib import Path

from pipeline import build_bibliography_db as bib

DB = Path(__file__).resolve().parents[2] / ".cache" / "bibliography.sqlite3"


class CountryFromRawTests(unittest.TestCase):
    """The country is the last place name in an affiliation, not the first."""

    # raw segment -> expected country
    SHIPPED = [
        # Orphan "USA" from the preceding affiliation used to win because
        # "United States" is the first row of the COUNTRIES table.
        ("USA 6Computational Social Science, ETH Zurich, Zurich, Switzerland",
         "Switzerland"),
        ("1ETH Zurich, Zurich, Switzerland", "Switzerland"),
        ("Department of Computer Science, Seoul National University, Seoul, "
         "South Korea", "South Korea"),
        ("Harvard University, Cambridge, MA, USA", "United States"),
        ("Max Planck Institute for Intelligent Systems, Tübingen, Germany",
         "Germany"),
        ("4Indian Institute of Technology Roor- kee, India", "India"),
        ("University of São Paulo, Brazil", "Brazil"),
        ("Universidad de Chile, Santiago, Chile", "Chile"),
        ("Nanyang Technological University, Singapore", "Singapore"),
        ("Hong Kong Polytechnic University, Hong Kong", "Hong Kong"),
        # Country names that double as place or person names must not win when a
        # real country follows them.
        ("Georgia Institute of Technology, Atlanta, GA, USA", "United States"),
        ("University of Georgia, Athens, GA, USA", "United States"),
        ("Niger Delta University, Nigeria", "Nigeria"),
    ]

    NO_COUNTRY = [
        "Indiana University Bloomington",
        "University of Southern California, Los Angeles",
        "Chad Smith Lab, University of Chicago",
        "Jordan Hall, Stanford University, Stanford, CA",
    ]

    def test_shipped_segments_resolve_correctly(self):
        for raw, expected in self.SHIPPED:
            with self.subTest(raw=raw[:48]):
                trimmed = bib._trim_affiliation_segment(raw)
                self.assertEqual(bib.country_from_raw(trimmed), expected)

    def test_absent_country_is_not_guessed(self):
        for raw in self.NO_COUNTRY:
            with self.subTest(raw=raw[:48]):
                self.assertEqual(
                    bib.country_from_raw(bib._trim_affiliation_segment(raw)), "")

    def test_bare_us_token_is_not_the_united_states(self):
        """"US INSERM" in a French unit code is not a country."""
        raw = ("cUniv. Rennes, BIOSIT, UMS CNRS 3840, US INSERM, "
               "F-35043 Rennes, France")
        self.assertEqual(
            bib.country_from_raw(bib._trim_affiliation_segment(raw)), "France")

    def test_venue_footer_is_cut_before_country_extraction(self):
        """A proceedings footer must not relocate the authors."""
        raw = ("8East China Normal University. Correspondence to: Shihui Zhen "
               "<z@zju.edu.cn>. Proceedings of the 43 rd International "
               "Conference on Machine Learning, Seoul, South Korea. PMLR 306.")
        trimmed = bib._trim_affiliation_segment(raw)
        self.assertNotIn("Seoul", trimmed)
        self.assertNotEqual(bib.country_from_raw(trimmed), "South Korea")


class CountryConsolidationTests(unittest.TestCase):
    """One institution, one country, decided by its own source strings."""

    def _db(self):
        conn = sqlite3.connect(":memory:")
        conn.executescript(
            "CREATE TABLE institutions (institution_id INTEGER PRIMARY KEY,"
            " institution_name TEXT, normalized_name TEXT,"
            " country_name_en TEXT DEFAULT '', source TEXT DEFAULT '');"
            "CREATE TABLE paper_institutions (paper_id INTEGER,"
            " institution_id INTEGER, country_name TEXT);")
        return conn

    def _seed(self, conn, country, links):
        conn.execute(
            "INSERT INTO institutions (institution_id,institution_name,"
            "normalized_name,country_name_en) VALUES (1,'X','x',?)", (country,))
        conn.executemany(
            "INSERT INTO paper_institutions VALUES (?,1,?)",
            [(i, c) for i, c in enumerate(links, 1)])

    def _country(self, conn):
        return conn.execute(
            "SELECT country_name_en FROM institutions").fetchone()[0]

    def test_majority_wins(self):
        conn = self._db()
        self._seed(conn, "Singapore", ["India", "India", "Singapore"])
        bib.consolidate_institution_countries(conn)
        self.assertEqual(self._country(conn), "India")

    def test_unsupported_country_is_always_replaced(self):
        """The IIT Roorkee case: a stale value no current link justifies."""
        conn = self._db()
        self._seed(conn, "United States", ["India", "Singapore"])
        bib.consolidate_institution_countries(conn)
        self.assertIn(self._country(conn), {"India", "Singapore"})
        self.assertNotEqual(self._country(conn), "United States")

    def test_single_dissenter_does_not_unseat_a_supported_country(self):
        conn = self._db()
        self._seed(conn, "Germany", ["Germany", "Germany", "Austria"])
        bib.consolidate_institution_countries(conn)
        self.assertEqual(self._country(conn), "Germany")

    def test_no_links_leaves_the_value_alone(self):
        conn = self._db()
        self._seed(conn, "China", [])
        bib.consolidate_institution_countries(conn)
        self.assertEqual(self._country(conn), "China")


@unittest.skipUnless(DB.exists(), ".cache/bibliography.sqlite3 없음")
class ShippedDatabaseInvariantTests(unittest.TestCase):
    """Invariants over the real DB — the data, not the machinery."""

    @classmethod
    def setUpClass(cls):
        cls.conn = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()

    def scalar(self, sql):
        return self.conn.execute(sql).fetchone()[0]

    def test_one_row_per_institution_name(self):
        self.assertEqual(self.scalar(
            "SELECT COUNT(*) FROM (SELECT normalized_name FROM institutions"
            " GROUP BY 1 HAVING COUNT(*)>1)"), 0)

    def test_no_institution_carries_two_countries(self):
        self.assertEqual(self.scalar(
            "SELECT COUNT(*) FROM (SELECT normalized_name FROM institutions"
            " WHERE country_name_en<>'' GROUP BY 1"
            " HAVING COUNT(DISTINCT country_name_en)>1)"), 0)

    def test_no_orphan_institutions(self):
        self.assertEqual(self.scalar(
            "SELECT COUNT(*) FROM institutions i WHERE NOT EXISTS("
            " SELECT 1 FROM paper_institutions pi"
            " WHERE pi.institution_id=i.institution_id)"), 0)

    def test_known_institutions_sit_in_the_right_country(self):
        expected = {
            "Harvard University": "United States",
            "Stanford University": "United States",
            "University of Oxford": "United Kingdom",
            "University of Cambridge": "United Kingdom",
            "ETH Zurich": "Switzerland",
            "Tsinghua University": "China",
            "Peking University": "China",
            "Chinese Academy of Sciences": "China",
            "Seoul National University": "South Korea",
            "Korea Advanced Institute of Science and Technology": "South Korea",
            "University of Tokyo": "Japan",
            "Max Planck Institute": "Germany",
            "Technical University of Munich": "Germany",
            "University of Toronto": "Canada",
            "University of Melbourne": "Australia",
        }
        rows = dict(self.conn.execute(
            "SELECT institution_name, country_name_en FROM institutions "
            "WHERE institution_name IN (%s)"
            % ",".join("?" * len(expected)), tuple(expected)))
        for name, country in expected.items():
            if name in rows:
                with self.subTest(institution=name):
                    self.assertEqual(rows[name], country)

    def test_country_coverage_does_not_regress(self):
        filled = self.scalar(
            "SELECT COUNT(*) FROM institutions WHERE country_name_en<>''")
        total = self.scalar("SELECT COUNT(*) FROM institutions")
        self.assertGreater(filled / total, 0.80,
                           f"country coverage fell to {filled}/{total}")


if __name__ == "__main__":
    unittest.main()
