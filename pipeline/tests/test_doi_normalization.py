"""Every boundary that accepts a DOI has to accept the same things.

The rule lived in `build_bibliography_db` alone, so `build_papers_index` kept
its own answer: 715 of the 1,762 DOI values in `_papers_index.json` were not
DOIs — "N/A" on 123 papers, "미제공" on 57 — and one was the template string
`10.1007/sxxxxx-yyy-zzzz-1`. Comparing unnormalised strings is the other half:
OpenAlex returns `https://doi.org/10.18653/...` where Crossref returns the bare
form, so one work counted as two candidates.
"""
import sys
import unittest
from pathlib import Path

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

from lib.doi import clean_arxiv, clean_doi


class ShapeTests(unittest.TestCase):
    def test_a_bare_doi_survives(self):
        self.assertEqual(clean_doi("10.18653/v1/2024.emnlp-main.70"),
                         "10.18653/v1/2024.emnlp-main.70")

    def test_every_prefix_form_normalises_to_one_string(self):
        bare = "10.1038/s41586-026-10652-y"
        for value in (bare,
                      "https://doi.org/" + bare,
                      "http://doi.org/" + bare,
                      "https://dx.doi.org/" + bare,
                      "HTTPS://DOI.ORG/" + bare,
                      "doi:" + bare,
                      "DOI: " + bare,
                      bare + ".",
                      "  " + bare + "  "):
            with self.subTest(value=value):
                self.assertEqual(clean_doi(value), bare)

    def test_words_meaning_no_doi_are_refused(self):
        for value in ("N/A", "n/a", "-", "---", "미제공", "미공개", "미기재",
                      "논문", "해당", "제공되지", "없음", "TBD", "none", ""):
            with self.subTest(value=value):
                self.assertEqual(clean_doi(value), "")

    def test_a_template_placeholder_is_refused(self):
        # Found in the shipped index: a fill-in-the-blanks DOI.
        self.assertEqual(clean_doi("https://doi.org/10.1007/sxxxxx-yyy-zzzz-1"),
                         "10.1007/sxxxxx-yyy-zzzz-1")
        # It matches the shape, so shape alone cannot catch it — the registrant
        # is real. This test records that limit rather than pretending it does.

    def test_a_registrant_must_be_four_digits(self):
        self.assertEqual(clean_doi("10.1/x"), "")
        self.assertEqual(clean_doi("10.1000/x"), "10.1000/x")

    def test_arxiv_dois_identify_the_preprint_not_the_paper(self):
        for value in ("10.48550/arXiv.2505.13400",
                      "https://doi.org/10.48550/arxiv.2502.18864",
                      "arXiv:2505.13400"):
            with self.subTest(value=value):
                self.assertEqual(clean_doi(value), "")


class ArxivShapeTests(unittest.TestCase):
    def test_every_form_normalises(self):
        for value in ("2505.13400", "arXiv:2505.13400",
                      "https://arxiv.org/abs/2505.13400",
                      "https://arxiv.org/pdf/2505.13400"):
            with self.subTest(value=value):
                self.assertEqual(clean_arxiv(value), "2505.13400")


class SingleDefinitionTests(unittest.TestCase):
    """The modules that accept DOIs must share one implementation."""

    def test_bibliography_db_reuses_the_library(self):
        import build_bibliography_db as bib
        self.assertIs(bib.clean_doi, clean_doi)
        self.assertIs(bib.clean_arxiv, clean_arxiv)

    def test_the_index_builder_reuses_the_library(self):
        import build_papers_index
        self.assertIs(build_papers_index.clean_doi, clean_doi)


if __name__ == "__main__":
    unittest.main()
