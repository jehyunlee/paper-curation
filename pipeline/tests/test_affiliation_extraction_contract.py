"""Affiliation extraction contract (AGENTS.md "Bibliography DB").

The contract is: Scopus FULL abstract metadata first, then PDF verification
using *first and last pages plus abstract-adjacent and Author information
blocks*. A previous build satisfied every structural test (CAS, locks, event
chain) while quietly reading 54% of each paper's body text into the institution
parser, so the shipped DB contained cited paper titles, abstract prose and
author bylines as institutions.

Every literal in this file is a string that actually reached
`.cache/bibliography.sqlite3`, together with the `paper_institutions.raw_name`
it came from. These tests exist so that class of regression fails loudly
instead of passing `check_bibliography_db.py --strict`.
"""
import re
import unittest

from pipeline import build_bibliography_db as bib


# name -> raw_name recorded in the shipped DB
SHIPPED_GARBAGE = {
    "A Neural Network":
        "3D point clouds. arXiv preprint arXiv:1802.08219, 2018. Unke",
    "A Dynamic Network":
        "Russell J. Funk, Jason Owen-Smith (2017) A Dynamic Network M",
    "A Bibliometric and Network":
        "International Journal of Economic Practices and Theories (IJ",
    "A Novel Framework for Dynamic Semantic Network": "",
    "Application of a Convolutional Neural Network": "",
    "Fast and Accurate Coarse-Grained Neural Network": "",
    "University of Helsinki Abstract World models are a powerful":
        "5University of Helsinki riccardo.mereu@aalto",
    "We introduce Wheeze Impedance Pneumography Scalogram Network": "",
    "Acer Liquid Network":
        "3GS Display, Display_Protection, corning gorilla glass Displ",
    "Encoder Network": "",
    "Decoder Network": "",
    "Policy Network": "",
    "Blip Prediction Network": "",
    "DoF Pose Estimation Network": "",
    "Vehicle to Network": "",
}

# Real institutions in the same corpus. None of them may be rejected.
REAL_INSTITUTIONS = [
    "Seoul National University",
    "Korea Advanced Institute of Science and Technology",
    "Harvard University", "Princeton University", "University of Cambridge",
    "ETH Zurich", "Chinese Academy of Sciences", "Max Planck Institute",
    "Texas A&M University", "Aalto University", "Goethe University",
    "Microsoft Research", "Genentech", "Santa Fe Institute",
    "Barcelona Supercomputing Center", "Beth Israel Deaconess Medical Center",
    "National Institute of Advanced Industrial Science and Technology",
    "The Chinese University of Hong Kong, Shenzhen", "Idiap Research Institute",
    # These end in an ML-artefact word but are genuine organisations.
    "University Health Network", "HUN-REN Hungarian Research Network",
    "Key Laboratory of Computing Power Network",
    "Hubei Key Laboratory of Multimedia and Network",
]


class SuspiciousNameDetectorTests(unittest.TestCase):
    """The gate `check_bibliography_db.py --strict` relies on."""

    def test_rejects_every_shipped_garbage_name(self):
        missed = [name for name in SHIPPED_GARBAGE
                  if not bib.is_suspicious_institution_name(name)]
        self.assertEqual(
            missed, [],
            "detector reported 0 suspicious names for these shipped rows")

    def test_accepts_every_real_institution(self):
        rejected = [name for name in REAL_INSTITUTIONS
                    if bib.is_suspicious_institution_name(name)]
        self.assertEqual(rejected, [], "false positives on real institutions")

    def test_artefact_tail_needs_an_organisation_cue(self):
        self.assertTrue(bib.is_suspicious_institution_name("Policy Network"))
        self.assertFalse(
            bib.is_suspicious_institution_name("University Health Network"))


class ExtractionWindowTests(unittest.TestCase):
    """The affiliation zone is front matter, not the whole paper."""

    BODY = "\n".join(
        ["Deep Learning for Widgets", "Jane Roe1, John Doe2",
         "1Seoul National University", "2Aalto University", "", "Abstract"]
        + ["Body sentence about neural networks." for _ in range(2000)]
        + ["References",
           "Russell J. Funk, Jason Owen-Smith (2017) A Dynamic Network "
           "Measure of Technological Change. Management Science.",
           "Unke et al. 3D point clouds. arXiv preprint arXiv:1802.08219."]
    )

    def _write(self, text):
        import tempfile
        from pathlib import Path
        path = Path(tempfile.mkdtemp()) / "text.md"
        path.write_text(text, encoding="utf-8")
        return path

    def test_reference_list_is_not_read(self):
        window = bib._pdf_text_for_affiliations(None, self._write(self.BODY))
        self.assertNotIn("arXiv preprint", window)
        self.assertNotIn("Owen-Smith", window)

    def test_front_matter_is_read(self):
        window = bib._pdf_text_for_affiliations(None, self._write(self.BODY))
        self.assertIn("Seoul National University", window)
        self.assertIn("Aalto University", window)

    def test_window_does_not_grow_with_the_paper(self):
        """A longer paper must not widen the affiliation zone.

        This is the property the old code violated: the window was anchored to
        both ends of the document, so every extra page of body text and every
        extra reference entry became institution-parser input.
        """
        short = self._write("\n".join(self.BODY.splitlines()[:300]))
        long_ = self._write(self.BODY)
        self.assertEqual(
            len(bib._pdf_text_for_affiliations(None, short)),
            len(bib._pdf_text_for_affiliations(None, long_)),
            "window scales with document length — the tail is being read again")


class SegmentSplittingTests(unittest.TestCase):
    """Superscript markers separate affiliations; both spellings must split."""

    def test_spaced_marker_separates_the_trailing_affiliation(self):
        """"5 UC Berkeley" must become its own segment.

        The old pattern only split on a digit glued to the next word, so
        everything after the first spaced marker was swallowed into one
        over-long segment and dropped.
        """
        segments = [s for s in re.split(
            r"(?=(?<![A-Za-z0-9])[1-9]\d?\s*[A-Z])",
            "1Texas A&M University, 5 UC Berkeley") if s.strip()]
        self.assertEqual(len(segments), 2, segments)
        self.assertEqual(bib._trim_affiliation_segment(segments[1]),
                         "5 UC Berkeley")
        names = {r["name"] for r in bib.reconcile_affiliations(
            [], "", ["1Texas A&M University, 5 Aalto University"],
            offline=True)}
        self.assertEqual(names, {"Texas A&M University", "Aalto University"})

    def test_glued_marker_does_not_leak_the_digit(self):
        names = {r["name"] for r in bib.reconcile_affiliations(
            [], "", ["1Genentech, 2Princeton University, 3 MIT"],
            offline=True)}
        self.assertNotIn("3 MIT", names)
        for name in names:
            self.assertFalse(re.match(r"^\d", name), f"digit leaked into {name!r}")

    def test_segment_is_trimmed_at_the_affiliation_boundary(self):
        raw = ("Goethe University Frankfurt, Germany. Corresponding authors. "
               "Emails: a@b.de Fig. 1. Motion retargeting pipeline overview")
        self.assertEqual(bib._trim_affiliation_segment(raw),
                         "Goethe University Frankfurt, Germany")


class TitleAndBylineGuardTests(unittest.TestCase):
    """Front matter starts with the title and the author byline."""

    def test_paper_title_is_not_an_institution(self):
        names = {r["name"] for r in bib.reconcile_affiliations(
            [], "", ["A Dynamic Network Measure of Technological Change"],
            offline=True,
            paper_title="A Dynamic Network Measure of Technological Change")}
        self.assertEqual(names, set())

    def test_author_byline_is_stripped_from_the_affiliation(self):
        stripped = bib._strip_leading_author_names(
            "Iz Beltagy Kyle Lo Arman Cohan Allen Institute for AI",
            bib._person_name_tokens(["Iz Beltagy", "Kyle Lo", "Arman Cohan"]))
        self.assertEqual(stripped, "Allen Institute for AI")

    def test_multiword_institution_is_never_treated_as_a_byline(self):
        self.assertEqual(
            bib._strip_leading_author_names(
                "Seoul National University",
                bib._person_name_tokens(["Jane Roe", "John Doe"])),
            "Seoul National University")


class ScopusPrecedenceTests(unittest.TestCase):
    """`Scopus is never hierarchy authority` (docs/operations.md)."""

    def test_resolved_name_outranks_the_scopus_parent_rollup(self):
        original = "Idiap Research Institute"
        parent = bib.scopus_parent_institution.__wrapped__ \
            if hasattr(bib.scopus_parent_institution, "__wrapped__") else None
        self.assertIsNone(parent)  # plain dict lookup, no caching wrapper
        records = [{"name": original, "country": "Switzerland",
                    "scopus_id": "", "raw_name": original}]
        out = bib.reconcile_affiliations(records, original, [], offline=True)
        self.assertEqual([r["name"] for r in out], [original])

    def test_confirmation_requires_every_distinctive_token(self):
        records = [{"name": "Aalto University", "country": "Finland",
                    "scopus_id": "", "raw_name": "Aalto University"}]
        hit = bib.reconcile_affiliations(
            records, "… Aalto University, Espoo …", [], offline=True)
        self.assertEqual(hit[0]["source"], "scopus+pdf")
        miss = bib.reconcile_affiliations(
            records, "… a university somewhere …", [], offline=True)
        self.assertEqual(miss[0]["source"], "scopus-unconfirmed")


class PdfBibliographyIssueTests(unittest.TestCase):
    """`issue` must be an identifier, never a word from body prose."""

    def test_prose_issue_of_does_not_match(self):
        # "Strategic Hypothesis Testing" (NeurIPS 2025) shipped issue="of"
        # captured from "the issue of strategic behavior".
        out = bib.pdf_bibliography("we study the issue of strategic behavior")
        self.assertNotIn("issue", out)

    def test_real_issue_identifiers_match(self):
        self.assertEqual(bib.pdf_bibliography("Volume 98, Issue 24")["issue"], "24")
        self.assertEqual(bib.pdf_bibliography("Vol. 12, No. 3-4")["issue"], "3-4")
        self.assertEqual(bib.pdf_bibliography("Issue S1, 2024")["issue"], "S1")


# Verbatim from the LC Agent PDF (Anal. Chem. 2026, 98, 18151−18163). The
# separator is U+2212 MINUS SIGN and the heading carries a leading "■".
ACS_AUTHOR_INFORMATION = (
    "■AUTHOR INFORMATION\n"
    "Corresponding Authors\n"
    "Youn-Suk Choi \u2212Samsung Advanced Institute of Technology,\n"
    "Samsung Electronics Co. Ltd., Suwon 16678, Republic of\n"
    "Korea;\norcid.org/0000-0001-7119-8788;\n"
    "Email: ysuk.choi@samsung.com\n"
    "Seokho Kang \u2212Department of Industrial Engineering,\n"
    "Sungkyunkwan University, Suwon 16419, Republic of Korea;\n"
    "orcid.org/0000-0002-0960-0294; Email: s.kang@skku.edu\n"
    "Author Contributions\n"
    "\u00a7Y.K. and H.K. contributed equally to this work.\n"
)


class AuthorInformationBlockTests(unittest.TestCase):
    """An ACS paper keeps its only affiliations in back-matter author info."""

    def test_heading_with_leading_symbol_is_found(self):
        self.assertTrue(bib._AUTHOR_INFO_CUE.search(ACS_AUTHOR_INFORMATION))

    def test_entries_yield_their_affiliations(self):
        found = bib.author_information_affiliations(ACS_AUTHOR_INFORMATION)
        joined = " | ".join(found)
        self.assertIn("Samsung Advanced Institute of Technology", joined)
        self.assertIn("Sungkyunkwan University", joined)

    def test_block_stops_before_author_contributions(self):
        found = " | ".join(bib.author_information_affiliations(
            ACS_AUTHOR_INFORMATION))
        self.assertNotIn("contributed equally", found)

    def test_orcid_and_email_are_not_affiliations(self):
        for value in bib.author_information_affiliations(
                ACS_AUTHOR_INFORMATION):
            self.assertNotIn("orcid", value.lower())
            self.assertNotIn("@", value)


class CompositeLocalLanguageAffiliationTests(unittest.TestCase):
    """ROR knows the parts of a composite affiliation, not the whole string."""

    FRENCH = ("Institut de Physique Théorique, Université Paris-Saclay, "
              "CNRS, CEA, Gif-sur-Yvette, France")

    def _stub_resolver(self, answers):
        seen = []

        def resolver(name, country="", *, allow_remote=False, offline=False):
            seen.append(name)
            return answers.get(name, "")

        return resolver, seen

    def test_segment_resolution_returns_the_english_name(self):
        from unittest.mock import patch
        resolver, seen = self._stub_resolver(
            {"Université Paris-Saclay": "University of Paris-Saclay"})
        with patch.object(bib, "resolve_english_institution", resolver):
            parsed = bib.institution_from_raw(self.FRENCH, allow_remote=True)
        self.assertIsNotNone(parsed)
        self.assertEqual(parsed[0], "University of Paris-Saclay")
        # The whole string is asked first, then the organisation-naming parts.
        self.assertEqual(seen[0], self.FRENCH)
        self.assertIn("Université Paris-Saclay", seen)

    def test_plain_place_segments_are_not_queried(self):
        from unittest.mock import patch
        resolver, seen = self._stub_resolver({})
        with patch.object(bib, "resolve_english_institution", resolver):
            bib.institution_from_raw(self.FRENCH, allow_remote=True)
        self.assertNotIn("Gif-sur-Yvette", seen)
        self.assertNotIn("France", seen)


class HeaderCueBoundaryTests(unittest.TestCase):
    """Acronym cues must not fire inside ordinary words."""

    def _candidates(self, body: str) -> list[str]:
        import tempfile
        from pathlib import Path
        with tempfile.NamedTemporaryFile(
                "w", suffix=".md", encoding="utf-8", delete=False) as handle:
            handle.write(body)
            path = Path(handle.name)
        try:
            return bib.extract_header(path)[1]
        finally:
            path.unlink()

    def test_licence_prose_is_not_an_affiliation(self):
        # An IOP cover sheet sentence: "permitted" contains "MIT".
        found = self._candidates(
            "Everyone is permitted to use all or part of the original content "
            "in this article, provided that they adhere to the licence\n")
        self.assertEqual(found, [])

    def test_methods_prose_is_not_an_affiliation(self):
        # "method" contains "ETH".
        found = self._candidates(
            "We evaluate this method against every published baseline here\n")
        self.assertEqual(found, [])

    def test_a_real_byline_still_parses(self):
        found = self._candidates(
            "Steering Sequence Generation in Protein Language Models\n"
            "Francesco Calvanese1,2, Martin Weigt2\n"
            "1Institut de Physique Théorique, Université Paris-Saclay, "
            "CNRS, CEA, Gif-sur-Yvette, France\n")
        self.assertTrue(
            any("Paris-Saclay" in value for value in found), found)


class BylineMarkerLayoutTests(unittest.TestCase):
    """Every layout a publisher uses to attach a marker to a name.

    All are verbatim from this corpus. The parser demanded the glued form and
    read only the end of a comma-chunk, so it mapped one author per byline:
    310 of 400 sampled papers had markers it could not see, and each fell back
    to linking every author to every institution.
    """

    def test_glued_marker(self):
        got = bib.author_affiliation_markers(
            "A Sentiment Consolidation Framework\n"
            "Miao Li1 Jey Han Lau1 Eduard Hovy1,2\n",
            ["Miao Li", "Jey Han Lau", "Eduard Hovy"])
        self.assertEqual(got, {"Miao Li": ["1"], "Jey Han Lau": ["1"],
                               "Eduard Hovy": ["1", "2"]})

    def test_spaced_marker(self):
        got = bib.author_affiliation_markers(
            "A Sober Look at LLMs\n"
            "Agustinus Kristiadi 1 Felix Strieth-Kalthoff 2 Marta Skreta 3\n",
            ["Agustinus Kristiadi", "Felix Strieth-Kalthoff", "Marta Skreta"])
        self.assertEqual(got, {"Agustinus Kristiadi": ["1"],
                               "Felix Strieth-Kalthoff": ["2"],
                               "Marta Skreta": ["3"]})

    def test_comma_left_by_a_stripped_orcid(self):
        got = bib.author_affiliation_markers(
            "A Review of LLM-Assisted Ideation\n"
            "Sitong Li ,1 Stefano Padilla ,1 Junyu Dong ,2 and Mike Chantler *,1\n",
            ["Sitong Li", "Stefano Padilla", "Junyu Dong", "Mike Chantler"])
        self.assertEqual(got, {"Sitong Li": ["1"], "Stefano Padilla": ["1"],
                               "Junyu Dong": ["2"], "Mike Chantler": ["1"]})

    def test_a_diacritic_in_zotero_still_matches_a_stripped_byline(self):
        got = bib.author_affiliation_markers(
            "Title\nXi-Chen Wang1 Jun Lu3 Wei-Guan Chen1\n",
            ["Xi-Chen Wang", "Jun Lü", "Wei-Guan Chen"])
        self.assertEqual(got["Jun Lü"], ["3"])

    def test_an_affiliation_block_is_not_a_byline(self):
        # "1Heriot-Watt University, Edinburgh, UK 2Ocean University" passed the
        # old digit-counting test. Only lines carrying this paper's own author
        # surnames are considered now.
        got = bib.author_affiliation_markers(
            "1Heriot-Watt University, Edinburgh, UK 2Ocean University, China\n",
            ["Sitong Li", "Stefano Padilla"])
        self.assertEqual(got, {})

    def test_a_paper_with_no_authors_maps_nothing(self):
        self.assertEqual(
            bib.author_affiliation_markers("Miao Li1 Jey Han Lau1\n", []), {})

    def test_a_byline_without_markers_maps_nothing(self):
        self.assertEqual(
            bib.author_affiliation_markers(
                "Title\nMiao Li, Jey Han Lau, Eduard Hovy\n",
                ["Miao Li", "Jey Han Lau", "Eduard Hovy"]), {})


if __name__ == "__main__":
    unittest.main()
