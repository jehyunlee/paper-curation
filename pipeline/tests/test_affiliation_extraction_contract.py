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


class InlineBylineTests(unittest.TestCase):
    """ACM-style bylines state the affiliation on the author's own line."""

    ACM = ("A Survey on Uncertainty Quantification Methods for Deep Learning\n"
           "WENCHONG HE, University of Florida, USA\n"
           "ZHE JIANG∗, University of Florida, USA\n"
           "YUKUN LI, Tufts University, USA\n")
    AUTHORS = ["Wenchong He", "Zhe Jiang", "Yukun Li"]

    def test_each_author_gets_its_own_line(self):
        got = bib.inline_author_affiliations(self.ACM, self.AUTHORS)
        self.assertEqual(got, {
            "Wenchong He": "University of Florida, USA",
            "Zhe Jiang": "University of Florida, USA",
            "Yukun Li": "Tufts University, USA"})

    def test_a_correspondence_mark_does_not_hide_the_author(self):
        self.assertIn("Zhe Jiang",
                      bib.inline_author_affiliations(self.ACM, self.AUTHORS))

    def test_an_affiliation_block_is_not_a_byline(self):
        # "Institute for Artificial Intelligence, Peking University" reads as
        # name-comma-organisation but names no author of this paper.
        got = bib.inline_author_affiliations(
            "Institute for Artificial Intelligence, Peking University\n"
            "State Key Laboratory of General Artificial Intelligence, BIGAI\n",
            self.AUTHORS)
        self.assertEqual(got, {})

    def test_a_line_without_an_organisation_is_ignored(self):
        got = bib.inline_author_affiliations(
            "WENCHONG HE, wenchong@ufl.edu\n", self.AUTHORS)
        self.assertEqual(got, {})

    def test_a_diacritic_in_zotero_still_matches(self):
        got = bib.inline_author_affiliations(
            "JUN LU, Nantong University, China\n", ["Jun Lü"])
        self.assertEqual(got, {"Jun Lü": "Nantong University, China"})

    def test_no_authors_maps_nothing(self):
        self.assertEqual(bib.inline_author_affiliations(self.ACM, []), {})


class SymbolMarkerTests(unittest.TestCase):
    """ACL templates key affiliations with suit symbols, not digits."""

    ACL = ("A Comprehensive Survey of Scientific Large Language Models\n"
           "Yu Zhang♣∗, Xiusi Chen♢♣∗, Bowen Jin♣∗,\n"
           "Sheng Wang♡, Jiawei Han♣\n"
           "♣University of Illinois at Urbana-Champaign\n"
           "♢University of California, Los Angeles\n"
           "♡University of Washington\n")
    AUTHORS = ["Yu Zhang", "Xiusi Chen", "Bowen Jin", "Sheng Wang",
               "Jiawei Han"]

    def test_symbols_are_read_as_markers(self):
        got = bib.author_affiliation_markers(self.ACL, self.AUTHORS)
        self.assertEqual(got["Yu Zhang"], ["♣"])
        self.assertEqual(got["Sheng Wang"], ["♡"])

    def test_a_symbol_run_is_several_markers(self):
        # "♢♣" is written without a separator; "12" is one number.
        self.assertEqual(
            bib.author_affiliation_markers(self.ACL, self.AUTHORS)["Xiusi Chen"],
            ["♢", "♣"])
        self.assertEqual(bib._split_marker_run("12"), ["12"])
        self.assertEqual(bib._split_marker_run("1,2"), ["1", "2"])

    def test_equal_contribution_marks_are_not_affiliations(self):
        # ∗ sits right beside the real markers and means something else.
        for markers in bib.author_affiliation_markers(
                self.ACL, self.AUTHORS).values():
            self.assertNotIn("∗", markers)
            self.assertNotIn("*", markers)

    def test_the_symbol_block_maps_to_affiliations(self):
        got = bib.marker_affiliations(self.ACL)
        self.assertEqual(got["♣"], "University of Illinois at Urbana-Champaign")
        self.assertEqual(got["♡"], "University of Washington")


class AuthorInformationPairTests(unittest.TestCase):
    """ACS names each author's affiliation in a back-matter block."""

    BLOCK = ("■AUTHOR INFORMATION\n"
             "Corresponding Author\n"
             "Yousung Jung \u2212Department of Chemical and Biological "
             "Engineering, Seoul National University, Korea;\n"
             "orcid.org/0000-0002-1129-158X; Email: yousung@snu.ac.kr\n"
             "Authors\n"
             "Junyoung Choi \u2212Department of Chemical Engineering, KAIST, "
             "Korea;\n"
             "Author Contributions\nAll authors contributed.\n")
    AUTHORS = ["Junyoung Choi", "Yousung Jung"]

    def test_each_author_is_paired_with_its_own_affiliation(self):
        got = bib.author_information_pairs(self.BLOCK, self.AUTHORS)
        self.assertIn("Seoul National University", got["Yousung Jung"])
        self.assertIn("KAIST", got["Junyoung Choi"])

    def test_a_subheading_is_not_an_author(self):
        got = bib.author_information_pairs(self.BLOCK, self.AUTHORS)
        self.assertEqual(set(got), set(self.AUTHORS))

    def test_an_author_from_another_paper_is_refused(self):
        self.assertEqual(
            bib.author_information_pairs(self.BLOCK, ["Someone Else"]), {})

    def test_the_block_is_found_at_the_end_of_a_long_paper(self):
        # ACS prints it at character 71,392 of 119,073, well past any
        # front-matter window.
        padded = ("body text.\n" * 8000) + self.BLOCK
        got = bib.author_information_pairs(padded, self.AUTHORS)
        self.assertIn("Seoul National University", got["Yousung Jung"])


class AffiliationMatchingTests(unittest.TestCase):
    """Joining a marker to an institution row is name matching, not prefixes.

    `raw[:60] in label` failed on everything a PDF does to a name, and 141
    papers read their markers and their affiliation block and then matched
    nothing.
    """

    def test_a_line_break_hyphen_is_the_same_name(self):
        self.assertGreaterEqual(
            bib.affiliation_match_score(
                "Indian Institute of Technology Roorkee",
                "4Indian Institute of Technology Roor- kee, India"),
            bib.AFFILIATION_MATCH_FLOOR)

    def test_a_department_prefix_on_one_side_only_still_matches(self):
        self.assertGreaterEqual(
            bib.affiliation_match_score(
                "Vanderbilt University",
                "Department of Computer Science, Vanderbilt University, "
                "Nashville, TN, USA"),
            bib.AFFILIATION_MATCH_FLOOR)

    def test_two_different_organisations_do_not_match(self):
        self.assertLess(
            bib.affiliation_match_score(
                "Department of Computer Science, Stanford University",
                "Department of Computer Science, Tsinghua University"),
            bib.AFFILIATION_MATCH_FLOOR)

    def test_a_shared_department_prefix_alone_is_not_a_match(self):
        # The prefix test matched these; the tokens that decide are the ones
        # that name the organisation, not the ones every paper shares.
        self.assertLess(
            bib.affiliation_match_score(
                "Department of Computer Science, University of Oxford",
                "Department of Computer Science, University of Cambridge"),
            bib.AFFILIATION_MATCH_FLOOR)

    def test_the_best_row_wins_not_the_first(self):
        institutions = [
            (1, "Department of Computer Science, Tsinghua University"),
            (2, "Department of Computer Science, Vanderbilt University"),
        ]
        self.assertEqual(
            bib.best_institution_for(
                "1Department of Computer Science, Vanderbilt University, "
                "Nashville, TN", institutions), 2)

    def test_nothing_close_enough_returns_none(self):
        self.assertIsNone(bib.best_institution_for(
            "Max Planck Institute for Intelligent Systems",
            [(1, "Seoul National University")]))


class WrappedAffiliationBlockTests(unittest.TestCase):
    """A marker can wrap onto its own line, and sit far from the byline."""

    BLOCK = ("Yamin Li 1 Shiyu Wang 1 Catie Chang 1\n"
             "1\n"
             "Department of Computer Science, Vanderbilt University\n")

    def test_a_marker_alone_on_a_line_joins_the_next(self):
        got = bib.marker_affiliations(self.BLOCK)
        self.assertIn("1", got)
        self.assertIn("Vanderbilt University", got["1"])

    def test_wanted_restricts_what_a_full_document_scan_reads(self):
        # Scanning a whole paper unrestricted is how a reference list becomes
        # affiliations; only the markers the byline used are accepted.
        text = self.BLOCK + "2 Proceedings of the International Conference\n"
        self.assertEqual(set(bib.marker_affiliations(text, {"1"})), {"1"})

    def test_no_wanted_set_keeps_the_old_behaviour(self):
        self.assertIn("1", bib.marker_affiliations(self.BLOCK, None))

    def test_spaced_markers_are_separate(self):
        # "Ruichen Qiu * 1 2" means markers 1 and 2. Read as one token, "1 2"
        # matches no affiliation and the paper loses its mapping.
        self.assertEqual(bib._split_marker_run("1 2"), ["1", "2"])
        self.assertEqual(bib._split_marker_run("12"), ["12"])
        got = bib.author_affiliation_markers(
            "MechMath\nRuichen Qiu * 1 2 Yichuan Cao * 2 3\n",
            ["Ruichen Qiu", "Yichuan Cao"])
        self.assertEqual(got["Ruichen Qiu"], ["1", "2"])
        self.assertEqual(got["Yichuan Cao"], ["2", "3"])

    def test_a_body_heading_is_not_an_affiliation(self):
        # Scanning a whole document, ".2. State Space Models for Time Series"
        # was read as affiliation 2 while the real one sat beside it.
        text = ("2\n.2. State Space Models for Time Series\n"
                "1Northwest Polytechni- cal University\n")
        got = bib.marker_affiliations(text, {"1", "2"})
        self.assertNotIn("2", got)
        self.assertIn("1", got)


class StackedBylineTests(unittest.TestCase):
    """arXiv and IEEE columns stack the affiliation under the author's name."""

    HEADER = ("AGENTIC RETRIEVAL-AUGMENTED GENERATION: A SURVEY\n"
              "Aditi Singh\n"
              "Department of Computer Science\n"
              "Cleveland State University\n"
              "Cleveland, OH, USA\n"
              "a.singh22@csuohio.edu\n"
              "Abul Ehtesham\n"
              "The Davey Tree Expert Company\n"
              "Kent, OH, USA\n"
              "abul.ehtesham@davey.com\n"
              "Tala Talaei Khoei\n"
              "Khoury College of Computer Science\n"
              "Roux Institute at Northeastern University\n"
              "Portland, ME, USA\n"
              "ABSTRACT\n"
              "Large Language Models have revolutionized artificial "
              "intelligence at the University of Nowhere.\n")
    AUTHORS = ["Aditi Singh", "Abul Ehtesham", "T. T. Khoei"]

    def test_every_author_gets_the_lines_under_its_name(self):
        got = bib.stacked_author_affiliations(self.HEADER, self.AUTHORS)
        self.assertIn("Cleveland State University", got["Aditi Singh"])
        self.assertIn("Davey Tree Expert Company", got["Abul Ehtesham"])
        self.assertIn("Northeastern University", got["T. T. Khoei"])

    def test_an_abbreviated_record_name_still_matches(self):
        # Zotero records "T. T. Khoei" where the byline reads "Tala Talaei
        # Khoei", so the surname is what can be compared.
        self.assertIn("T. T. Khoei",
                      bib.stacked_author_affiliations(self.HEADER, self.AUTHORS))

    def test_the_block_stops_at_the_email(self):
        got = bib.stacked_author_affiliations(self.HEADER, self.AUTHORS)
        self.assertNotIn("@", got["Aditi Singh"])

    def test_the_block_stops_at_the_abstract(self):
        got = bib.stacked_author_affiliations(self.HEADER, self.AUTHORS)
        self.assertNotIn("University of Nowhere", got["T. T. Khoei"])

    def test_one_lone_match_is_a_coincidence(self):
        # A name followed by a university line proves nothing on its own; a
        # byline is several of them in a row.
        self.assertEqual(
            bib.stacked_author_affiliations(
                "Title\nAditi Singh\nCleveland State University\n",
                self.AUTHORS), {})

    def test_a_line_with_an_organisation_is_not_a_name(self):
        self.assertEqual(
            bib.stacked_author_affiliations(
                "Cleveland State University\nDepartment of Computer Science\n"
                "Roux Institute at Northeastern University\nPortland, ME\n",
                self.AUTHORS), {})


class MarkerAlphabetTests(unittest.TestCase):
    """Which characters key a paper's affiliations is a property of the paper.

    ∗ marks the affiliation in one template and equal contribution in another,
    so no fixed rule reads both. The alphabet is read off the affiliation
    block: whatever a line naming an organisation begins with is a marker here.
    """

    ARXIV = ("Architecture Design for Human-Driven Systems\n"
             "Mahyar T. Moghaddam∗, Moamin B. Abughazala†, "
             "Vittorio Cortellessa†\n"
             "∗MMMI Institute, University of Southern Denmark, Odense\n"
             "†DISIM Department, University of L'Aquila, L'Aquila, Italy\n")
    ACL = ("A Comprehensive Survey\n"
           "Yu Zhang♣∗, Xiusi Chen♢♣∗, Sheng Wang♡\n"
           "♣University of Illinois at Urbana-Champaign\n"
           "♢University of California, Los Angeles\n"
           "♡University of Washington\n")
    PNAS = ("Productivity, prominence, and the effects of academic environment\n"
            "Samuel F. Waya,1, Allison C. Morgana, Daniel B. Larremorea,b,2\n"
            "aDepartment of Computer Science, University of Colorado Boulder\n")

    def test_a_star_is_a_marker_when_the_block_uses_it(self):
        self.assertEqual(bib.infer_marker_alphabet(self.ARXIV), {"∗", "†"})

    def test_the_same_star_is_not_a_marker_when_the_block_does_not(self):
        # Here ∗ means equal contribution and only the suits key affiliations.
        self.assertEqual(bib.infer_marker_alphabet(self.ACL),
                         {"♣", "♢", "♡"})

    def test_lowercase_letters_key_a_pnas_byline(self):
        self.assertEqual(bib.infer_marker_alphabet(self.PNAS), {"a"})

    def test_the_byline_is_read_with_the_papers_own_alphabet(self):
        got = bib.author_affiliation_markers(
            self.ARXIV, ["Mahyar T. Moghaddam", "Moamin B. Abughazala",
                         "Vittorio Cortellessa"],
            bib.infer_marker_alphabet(self.ARXIV))
        self.assertEqual(got["Mahyar T. Moghaddam"], ["∗"])
        self.assertEqual(got["Vittorio Cortellessa"], ["†"])

    def test_equal_contribution_stays_out_when_it_is_not_in_the_alphabet(self):
        got = bib.author_affiliation_markers(
            self.ACL, ["Yu Zhang", "Xiusi Chen", "Sheng Wang"],
            bib.infer_marker_alphabet(self.ACL))
        self.assertEqual(got["Yu Zhang"], ["♣"])
        self.assertEqual(got["Xiusi Chen"], ["♢", "♣"])

    def test_a_corresponding_author_digit_does_not_hide_the_surname(self):
        # "Waya,1" is affiliation a and corresponding author 1.
        got = bib.author_affiliation_markers(
            self.PNAS, ["Samuel F. Way", "Allison C. Morgan",
                        "Daniel B. Larremore"],
            bib.infer_marker_alphabet(self.PNAS))
        self.assertEqual(got["Samuel F. Way"], ["a"])
        self.assertEqual(got["Allison C. Morgan"], ["a"])

    def test_digits_still_work_with_no_alphabet_inferred(self):
        header = ("A Sober Look at LLMs\n"
                  "Agustinus Kristiadi 1 Felix Strieth-Kalthoff 2\n")
        got = bib.author_affiliation_markers(
            header, ["Agustinus Kristiadi", "Felix Strieth-Kalthoff"], set())
        self.assertEqual(got["Agustinus Kristiadi"], ["1"])


class SpacingAccentTests(unittest.TestCase):
    """A PDF may print the accent as a character standing before the letter."""

    def test_a_spacing_diaeresis_folds_like_the_composed_letter(self):
        # "G¨atzner" in the PDF, "Gätzner" in the record.
        self.assertEqual(bib._fold("G\u00a8atzner"), bib._fold("Gätzner"))

    def test_folding_does_not_swallow_spaces(self):
        # NFKD turns U+00A8 into a space plus a combining mark, so the accent
        # has to be removed first or the surname is split in two.
        self.assertEqual(bib._fold("Indian Institute"), "indian institute")


class ScopusInstitutionNameTests(unittest.TestCase):
    """Scopus indexes the unit it was given, which is often not an institution.

    A paper comes back under "College of Engineering and Applied Science" with
    the university it belongs to nowhere in the record. The PDF path already
    puts every candidate past ROR; Scopus names skipped that check and were
    minted as institutions unchecked.
    """

    def test_a_university_passes(self):
        self.assertEqual(bib.scopus_institution_name("Stanford University"),
                         "Stanford University")

    def test_an_internal_unit_is_refused(self):
        for name in ("College of Engineering and Applied Science",
                     "Department of Computer Science",
                     "Center for Computational Science and Engineering"):
            with self.subTest(name=name):
                self.assertEqual(bib.scopus_institution_name(name), "")

    def test_a_real_organisation_named_like_one_is_kept(self):
        # ROR holds records for these; the name alone cannot decide.
        for name in ("Center for Open Science",
                     "Center for Theoretical Biological Physics"):
            with self.subTest(name=name):
                self.assertEqual(bib.scopus_institution_name(name), name)

    def test_an_empty_name_is_refused(self):
        self.assertEqual(bib.scopus_institution_name(""), "")


class TruncatedLabelMatchTests(unittest.TestCase):
    """A PDF can break a name mid-word and leave the rest behind."""

    def test_a_truncated_token_matches_the_whole_one(self):
        # The label stopped at "Polytechni-"; the row kept "Polytechni- cal
        # University", which rejoins to "polytechnical".
        self.assertGreaterEqual(
            bib.affiliation_match_score(
                "1Northwest Polytechni- cal University",
                "Northwest Polytechni-"),
            bib.AFFILIATION_MATCH_FLOOR)

    def test_a_short_prefix_is_not_enough(self):
        # Four characters would make "Univ" match anything.
        self.assertLess(
            bib.affiliation_match_score("Tsinghua University", "Tsin"),
            bib.AFFILIATION_MATCH_FLOOR)

    def test_two_different_organisations_still_do_not_match(self):
        self.assertLess(
            bib.affiliation_match_score(
                "Northwest Polytechnical University",
                "Northeastern University"),
            bib.AFFILIATION_MATCH_FLOOR)

    def test_a_label_of_only_generic_words_matches_nothing(self):
        # "University" alone names no organisation; refusing is correct and no
        # amount of reasoning could recover which one it was.
        self.assertEqual(
            bib.affiliation_match_score("2University of British Columbia",
                                        "University"), 0.0)


class WrappedInNarrowColumnTests(unittest.TestCase):
    """A two-column footnote wraps after a word or two.

    "1ShanghaiTech" lands on one line and "University;" on the next, so the
    marker sits on a line naming no organisation and the organisation sits on
    a line carrying no marker. 42 of the 48 papers in this stage held their
    affiliation in text.md and were failing for exactly this reason.
    """

    WRAPPED = ("1ShanghaiTech\n"
               "University;\n"
               "2Shanghai Jiao\n"
               "Tong University.\n")

    def test_a_wrapped_affiliation_is_read(self):
        got = bib.marker_affiliations(self.WRAPPED, {"1", "2"}, {"1", "2"})
        self.assertIn("ShanghaiTech University", got.get("1", ""))

    def test_body_prose_is_not_absorbed(self):
        # A marker-led line that never reaches an organisation stays alone.
        text = ("1Introduction\n"
                "Computed tomography is a ubiquitous imaging technique\n"
                "used across medicine and manufacturing.\n")
        self.assertEqual(bib.marker_affiliations(text, {"1"}, {"1"}), {})

    def test_the_join_stops_at_a_section_heading(self):
        text = ("1ShanghaiTech\n"
                "2. Related Work\n"
                "University of Somewhere\n")
        self.assertEqual(bib.marker_affiliations(text, {"1"}, {"1"}), {})

    def test_an_unwrapped_block_still_works(self):
        got = bib.marker_affiliations(
            "1Heriot-Watt University, Edinburgh, UK 2Ocean University, China\n",
            {"1", "2"}, {"1", "2"})
        self.assertIn("Heriot-Watt University", got.get("1", ""))


class AffiliationShapeTests(unittest.TestCase):
    """A marker-led segment names a place, a company, or neither.

    `_AFFILIATION_ORG_CUE` lists the words a university's name contains, and
    companies do not contain them. "1Genentech 2Guide Labs 3Department of
    Computer Science, New York University" was refused whole because its first
    segment named a company, taking the two universities behind it along.
    """

    def test_a_company_is_an_affiliation(self):
        for name in ("Genentech", "Together AI", "ByteDance", "NVIDIA",
                     "Guide Labs", "Microsoft Research"):
            with self.subTest(name=name):
                self.assertTrue(bib.looks_like_affiliation(name))

    def test_an_abbreviated_campus_is_an_affiliation(self):
        # ROR reads these: UC Berkeley is University of California, Berkeley.
        for name in ("UC Berkeley", "UT Austin", "UC San Diego"):
            with self.subTest(name=name):
                self.assertTrue(bib.looks_like_affiliation(name))

    def test_a_cited_title_is_not(self):
        # These reached the shipped DB as institutions once.
        for name in ("A Neural Network", "A Dynamic Network",
                     "Acer Liquid Network"):
            with self.subTest(name=name):
                self.assertFalse(bib.looks_like_affiliation(name))

    def test_a_citation_is_refused_outright(self):
        for name in ("Nature 596, 583 (2021)", "Smith et al., 2023",
                     "arXiv preprint arXiv:1802.08219", "J. Chem. vol. 12"):
            with self.subTest(name=name):
                self.assertFalse(bib.looks_like_affiliation(name))

    def test_body_prose_is_not_an_affiliation(self):
        self.assertFalse(bib.looks_like_affiliation(
            "agents could potentially discover new materials and"))

    def test_a_university_still_passes_without_asking_ror(self):
        self.assertTrue(bib.looks_like_affiliation(
            "Department of Computer Science, New York University"))


class CompanyBlockTests(unittest.TestCase):
    """The block that motivated widening the test."""

    BLOCK = ("*Equal contribution 1Genentech 2Guide Labs 3Department of "
             "Computer Science, New York University\n")

    def test_every_marker_in_the_block_is_read(self):
        got = bib.marker_affiliations(self.BLOCK, {"1", "2", "3"},
                                      {"1", "2", "3"})
        self.assertEqual(got["1"], "Genentech")
        self.assertEqual(got["2"], "Guide Labs")
        self.assertIn("New York University", got["3"])


if __name__ == "__main__":
    unittest.main()
