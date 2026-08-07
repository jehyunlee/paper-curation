import tempfile
import unittest
import sqlite3
from pathlib import Path

from pipeline import build_bibliography_db as bib


class BibliographyAffiliationTests(unittest.TestCase):
    def setUp(self):
        bib.set_institution_registry({
            "Tongji University",
            "Massachusetts Institute of Technology",
            "The University of Hong Kong",
            "National University of Singapore",
            "National University of Defense Technology",
            "Technical University of Munich",
            "Technical University of Denmark",
            "Stanford University",
            "Tsinghua University",
            "The Chinese University of Hong Kong, Shenzhen",
            "The Hong Kong University of Science and Technology",
            "The Hong Kong University of Science and Technology (Guangzhou)",
            "Warsaw University of Technology",
            "Hebei University of Technology",
        })

    def test_scopus_subunit_normalizes_to_parent_university(self):
        self.assertEqual(
            bib.canonical_institution("University of Toronto Faculty of Medicine"),
            "University of Toronto",
        )

    def test_scopus_is_validated_and_pdf_adds_missing_institution(self):
        scopus = [{
            "name": "University of Toronto",
            "raw_name": "University of Toronto",
            "country": "Canada",
            "scopus_id": "1",
            "source": "scopus",
        }]
        pdf = (
            "Published online: 26 February 2024\n"
            "1Peter Munk Cardiac Centre, University Health Network, Toronto, Canada. "
            "2Department of Computer Science, University of Toronto, Toronto, Canada."
        )
        rows = bib.reconcile_affiliations(scopus, pdf, [])
        by_name = {row["name"]: row for row in rows}
        self.assertEqual(by_name["University of Toronto"]["source"], "scopus+pdf")
        self.assertIn("University Health Network", by_name)

    def test_scopus_college_profile_maps_to_parent_institution(self):
        rows = bib.reconcile_affiliations([{
            "name": "College of Engineering",
            "raw_name": "College of Engineering",
            "country": "United States",
            "scopus_id": "60137961",
            "source": "scopus",
        }], "University of Illinois at Chicago", [])
        self.assertEqual(
            [row["name"] for row in rows],
            ["University of Illinois at Chicago"],
        )

    def test_unresolved_college_subunit_is_not_stored_as_institution(self):
        rows = bib.reconcile_affiliations([{
            "name": "College of Education",
            "raw_name": "College of Education",
            "country": "United States",
            "scopus_id": "unknown",
            "source": "scopus",
        }], "", [])
        self.assertEqual(rows, [])
        self.assertTrue(
            bib.is_suspicious_institution_name("College of Education"))
        self.assertFalse(
            bib.is_suspicious_institution_name("College of Staten Island"))

    def test_named_college_subunit_maps_to_explicit_parent(self):
        self.assertEqual(
            bib.canonical_institution(
                "College of Computer Science and Technology, Zhejiang University"),
            "Zhejiang University",
        )

    def test_college_raw_affiliation_expands_named_parent(self):
        self.assertEqual(
            bib.resolve_institution_from_raw(
                "Department of Pharmacy Practice, College of Pharmacy, "
                "National University of Science and Technology, Muscat, Oman",
                "College of Pharmacy",
            ),
            "National University of Science & Technology, Oman",
        )
        self.assertEqual(
            bib.canonical_institution(
                "College of Humanities, Arts, and Social Sciences"),
            "Nanyang Technological University",
        )

    def test_longest_registered_parent_wins_over_author_and_department(self):
        cases = {
            (
                "Zihe Wei School of Computer Science & Technology "
                "Tongji University"
            ): "Tongji University",
            (
                "Zituo Chen Department of Mechanical Engineering "
                "Massachusetts Institute of Technology Cambridge"
            ): "Massachusetts Institute of Technology",
            (
                "Department of Medicine, Stanford University School of Medicine"
            ): "Stanford University",
        }
        for raw, expected in cases.items():
            with self.subTest(raw=raw):
                self.assertEqual(
                    bib.resolve_institution_from_raw(raw, raw), expected)

    def test_generic_university_names_expand_from_raw_affiliation(self):
        cases = [
            ("The University", "1The University of Hong Kong, Hong Kong",
             "The University of Hong Kong"),
            ("National University",
             "1National University of Singapore, Singapore",
             "National University of Singapore"),
            ("National University",
             "College, National University of Defense Technology, China",
             "National University of Defense Technology"),
            ("Technical University",
             "Department, Technical University of Munich, Germany",
             "Technical University of Munich"),
        ]
        for current, raw, expected in cases:
            with self.subTest(current=current, raw=raw):
                self.assertEqual(
                    bib.resolve_institution_from_raw(raw, current), expected)

    def test_clean_current_institution_is_not_replaced_by_another_affiliation(self):
        raw = (
            "Tsinghua University, Beijing, China; "
            "The Hong Kong University of Science and Technology, Hong Kong"
        )
        self.assertEqual(
            bib.resolve_institution_from_raw(raw, "Tsinghua University"),
            "Tsinghua University",
        )

    def test_hong_kong_branch_campuses_remain_distinct(self):
        cases = [
            (
                "Chinese University of Hong Kong, Shenzhen, China",
                "Chinese University",
                "The Chinese University of Hong Kong, Shenzhen",
            ),
            (
                "Hong Kong University of Science and Technology (Guangzhou), China",
                "Hong Kong University",
                "The Hong Kong University of Science and Technology (Guangzhou)",
            ),
        ]
        for raw, current, expected in cases:
            with self.subTest(raw=raw):
                self.assertEqual(
                    bib.resolve_institution_from_raw(raw, current), expected)

    def test_affiliation_markers_do_not_truncate_technology_universities(self):
        cases = [
            (
                "aWarsaw University of Technology, Faculty of Mathematics",
                "University of Technology",
                "Warsaw University of Technology",
            ),
            (
                "BUPT 7Hebei University of Technology",
                "University of Technology",
                "Hebei University of Technology",
            ),
        ]
        for raw, current, expected in cases:
            with self.subTest(raw=raw):
                self.assertEqual(
                    bib.resolve_institution_from_raw(raw, current), expected)

    def test_truncated_exact_aliases_are_canonicalized(self):
        self.assertEqual(
            bib.canonical_institution("Massachusetts Institute"),
            "Massachusetts Institute of Technology")
        self.assertEqual(
            bib.canonical_institution("Georgia Institute"),
            "Georgia Institute of Technology")

    def test_text_fallback_scans_after_abstract_and_last_pages(self):
        with tempfile.TemporaryDirectory() as td:
            text = Path(td) / "text.md"
            text.write_text(
                "Title\nAuthors\nAbstract\nBody\n" + "Body\n" * 60 +
                "Published online: 26 February 2024\n"
                "1University of Toronto, Toronto, Canada.\n",
                encoding="utf-8",
            )
            extracted = bib._pdf_text_for_affiliations(None, text)
            self.assertIn("University of Toronto", extracted)
            self.assertIn("Published online", extracted)

    def test_scopus_bibliography_normalizes_full_record(self):
        row = bib.scopus_bibliography({"coredata": {
            "dc:title": "A formal title",
            "prism:publicationName": "Nature Methods",
            "prism:coverDate": "2024-08-01",
            "prism:doi": "10.1038/example",
            "prism:volume": "21",
            "prism:issueIdentifier": "8",
            "prism:pageRange": "1470-1480",
            "dc:publisher": "Nature Research",
            "prism:issn": "15487105 15487091",
            "subtypeDescription": "Article",
            "eid": "2-s2.0-123",
        }})
        self.assertEqual(row["journal"], "Nature Methods")
        self.assertEqual(row["volume"], "21")
        self.assertEqual(row["pages"], "1470-1480")
        self.assertEqual(row["issn"], "1548-7105; 1548-7091")
        self.assertEqual(row["scopus_eid"], "2-s2.0-123")

    def test_pdf_bibliography_extracts_publisher_dates_and_header(self):
        text = (
            "Nature Methods | Volume 21 | August 2024 | 1470–1480\n"
            "https://doi.org/10.1038/s41592-024-02201-0\n"
            "Received: 12 July 2023\nAccepted: 30 January 2024\n"
            "Published online: 26 February 2024\n"
        )
        row = bib.pdf_bibliography(text)
        self.assertEqual(row["journal"], "Nature Methods")
        self.assertEqual(row["volume"], "21")
        self.assertEqual(row["pages"], "1470-1480")
        self.assertEqual(row["received_date"], "2023-07-12")
        self.assertEqual(row["accepted_date"], "2024-01-30")
        self.assertEqual(row["published_online_date"], "2024-02-26")

    def test_pdf_repairs_scopus_and_online_date_wins(self):
        row = bib.reconcile_bibliography(
            {"title": "Local", "journal": "Preprint", "date": "2023"},
            {"title": "Formal", "journal": "Journal", "date": "2024-08-01",
             "volume": "21", "source": "scopus"},
            {"journal": "Nature Methods", "pages": "1470-1480",
             "published_online_date": "2024-02-26"},
        )
        self.assertEqual(row["title"], "Formal")
        self.assertEqual(row["journal"], "Nature Methods")
        self.assertEqual(row["date"], "2024-02-26")
        self.assertEqual(row["source"], "scopus+pdf")

    def test_legacy_database_schema_is_migrated(self):
        conn = sqlite3.connect(":memory:")
        conn.execute(
            "CREATE TABLE papers (paper_id INTEGER PRIMARY KEY, "
            "slug TEXT UNIQUE, title TEXT, review_dir TEXT)")
        bib.ensure_schema_migrations(conn)
        columns = {
            row[1] for row in conn.execute("PRAGMA table_info(papers)").fetchall()
        }
        self.assertTrue(set(bib.PAPER_SCHEMA_COLUMNS).issubset(columns))
        conn.close()


if __name__ == "__main__":
    unittest.main()
