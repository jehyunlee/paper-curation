import tempfile
import unittest
from pathlib import Path

from pipeline import build_bibliography_db as bib


class BibliographyAffiliationTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
