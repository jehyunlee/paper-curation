"""A DOI written without a human looking needs more evidence than one proposed.

Only 1,812 of 4,196 papers carry a DOI, and citations, OpenAlex authorships,
corresponding authors and ORCIDs all hang off it. Searching by title closes
part of that gap, but a title search is also what put a Frontiers DOI onto an
Industrial and Corporate Change item earlier in this corpus, so the acceptance
rule is what these tests pin.
"""
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import resolve_missing_dois as resolver
import review_publications as rp

PAPER = {"title": "AgentReview: Exploring Peer Review Dynamics with LLM Agents",
         "authors": ["Yiqiao Jin", "Qinlin Zhao"]}


def work(title, doi, kind="article", authors=("Yiqiao Jin",), venue="",
         host="https://openalex.org/W1"):
    return {"display_name": title, "doi": doi, "type": kind, "id": host,
            "primary_location": {"source": {"display_name": venue}},
            "authorships": [{"author": {"display_name": name}}
                            for name in authors]}


class AcceptanceTests(unittest.TestCase):
    def test_an_exact_match_with_a_shared_author_is_accepted(self):
        ok, why = resolver.accept(
            PAPER, work(PAPER["title"], "10.18653/v1/2024.emnlp-main.70"))
        self.assertTrue(ok, why)

    def test_a_conference_paper_is_formal(self):
        # OpenAlex says "conference-paper" where Crossref says
        # "proceedings-article"; listing only Crossref's vocabulary rejected
        # every NeurIPS and EMNLP paper OpenAlex returned.
        ok, why = resolver.accept(
            PAPER, work(PAPER["title"], "10.18653/v1/2024.emnlp-main.70",
                        kind="conference-paper"))
        self.assertTrue(ok, why)

    def test_a_near_miss_title_is_refused(self):
        ok, why = resolver.accept(
            PAPER, work("AgentReview: Peer Review Dynamics", "10.1000/x"))
        self.assertFalse(ok)
        self.assertIn("similarity", why)

    def test_a_paper_with_no_author_in_common_is_refused(self):
        ok, why = resolver.accept(
            PAPER, work(PAPER["title"], "10.1000/x", authors=("Other Person",)))
        self.assertFalse(ok)
        self.assertEqual(why, "no author in common")

    def test_a_dataset_is_refused(self):
        ok, why = resolver.accept(
            PAPER, work(PAPER["title"], "10.1000/x", kind="dataset"))
        self.assertFalse(ok)

    def test_a_repository_doi_is_refused(self):
        ok, why = resolver.accept(
            PAPER, work(PAPER["title"], "10.6084/m9.figshare.32666007"))
        self.assertFalse(ok)
        self.assertEqual(why, "repository DOI")

    def test_an_arxiv_doi_is_not_a_publication(self):
        ok, why = resolver.accept(
            PAPER, work(PAPER["title"], "https://doi.org/10.48550/arxiv.2406.1"))
        self.assertFalse(ok)
        self.assertEqual(why, "no DOI on candidate")

    def test_peer_review_records_are_refused(self):
        ok, _ = resolver.accept(
            PAPER, work(PAPER["title"], "10.7287/peerj-cs.107v0.1/reviews/1",
                        kind="peer-review"))
        self.assertFalse(ok)


class ResolutionTests(unittest.TestCase):
    def test_one_survivor_resolves(self):
        works = [work(PAPER["title"], "10.18653/v1/2024.emnlp-main.70"),
                 work("Something else entirely", "10.1000/other")]
        with patch.object(rp, "candidate_works", return_value=works):
            found = resolver.resolve(PAPER)
        self.assertEqual(found["doi"], "10.18653/v1/2024.emnlp-main.70")
        self.assertEqual(found["source"], "openalex")
        self.assertEqual(found["similarity"], 1.0)

    def test_two_survivors_refuse_rather_than_pick(self):
        # A shared title, a correction notice, a reprint. Choosing between them
        # is guessing, and this writes without anyone checking.
        works = [work(PAPER["title"], "10.1000/a"),
                 work(PAPER["title"], "10.1000/b")]
        with patch.object(rp, "candidate_works", return_value=works):
            self.assertIsNone(resolver.resolve(PAPER))

    def test_no_candidate_resolves_to_nothing(self):
        with patch.object(rp, "candidate_works", return_value=[]):
            self.assertIsNone(resolver.resolve(PAPER))

    def test_an_untitled_paper_is_never_searched(self):
        with patch.object(rp, "candidate_works") as search:
            self.assertIsNone(resolver.resolve({"title": "  ", "authors": []}))
        search.assert_not_called()


class CandidateDeduplicationTests(unittest.TestCase):
    """The same work from two providers is one candidate, not two."""

    def test_url_and_bare_doi_are_the_same_work(self):
        openalex = [work(PAPER["title"],
                         "https://doi.org/10.18653/v1/2024.emnlp-main.70")]
        crossref = [work(PAPER["title"], "10.18653/v1/2024.emnlp-main.70",
                         host="https://doi.org/10.18653/v1/2024.emnlp-main.70")]
        with patch.object(rp, "search_openalex", return_value=openalex), \
             patch.object(rp, "search_crossref", return_value=crossref):
            works = rp.candidate_works(PAPER["title"])
        self.assertEqual(len(works), 1)

    def test_genuinely_different_works_both_survive(self):
        with patch.object(rp, "search_openalex",
                          return_value=[work("A", "10.1000/a")]), \
             patch.object(rp, "search_crossref",
                          return_value=[work("B", "10.1000/b")]):
            self.assertEqual(len(rp.candidate_works("A")), 2)


class OpenAlexBreakerTests(unittest.TestCase):
    """A rate-limit blip must not demote the better provider for the run."""

    def setUp(self):
        rp._OPENALEX_STATE.update({"refusals": 0, "blocked_until": 0.0})

    tearDown = setUp

    def _refuse(self):
        with patch.object(rp.bib, "request_json",
                          side_effect=Exception("HTTP Error 429")), \
             patch.object(rp.time, "sleep"):
            return rp.search_openalex("anything")

    def test_three_refusals_pause_rather_than_latch(self):
        for _ in range(3):
            self._refuse()
        self.assertGreater(rp._OPENALEX_STATE["blocked_until"], 0)

    def test_a_paused_breaker_skips_the_call(self):
        rp._OPENALEX_STATE["blocked_until"] = rp.time.time() + 999
        with patch.object(rp.bib, "request_json") as call:
            self.assertEqual(rp.search_openalex("anything"), [])
        call.assert_not_called()

    def test_the_breaker_reopens_after_the_cooldown(self):
        rp._OPENALEX_STATE.update({"refusals": 3,
                                   "blocked_until": rp.time.time() - 1})
        with patch.object(rp.bib, "request_json",
                          return_value={"results": [{"doi": "10.1000/x"}]}):
            results = rp.search_openalex("anything")
        self.assertEqual(len(results), 1)
        self.assertEqual(rp._OPENALEX_STATE["refusals"], 0)


class FrontmatterWriteTests(unittest.TestCase):
    """A resolution has to land in the paper's own file to survive."""

    HEAD = ('---\ntitle: "A Survey"\nauthors:\n  - "Wenchong He"\n'
            'date: "2023.02"\ndoi: "N/A"\narxiv: ""\njournal: "preprint"\n'
            '---\n\n# A Survey\n\nbody text\n')

    def setUp(self):
        import tempfile
        self.root = Path(tempfile.mkdtemp())
        (self.root / "037_x").mkdir()
        (self.root / "037_x" / "review.md").write_text(self.HEAD,
                                                       encoding="utf-8")
        self._saved = resolver.bib.PAPERS_DIR
        resolver.bib.PAPERS_DIR = self.root

    def tearDown(self):
        resolver.bib.PAPERS_DIR = self._saved

    def _text(self):
        return (self.root / "037_x" / "review.md").read_text(encoding="utf-8")

    def test_the_placeholder_is_replaced(self):
        self.assertTrue(
            resolver.write_frontmatter_doi("037_x", "10.1145/3786319"))
        self.assertIn('doi: "10.1145/3786319"', self._text())
        self.assertNotIn('doi: "N/A"', self._text())

    def test_the_body_is_untouched(self):
        resolver.write_frontmatter_doi("037_x", "10.1145/3786319")
        text = self._text()
        self.assertTrue(text.startswith("---\n"))
        self.assertIn("\n# A Survey\n", text)
        self.assertIn("body text", text)
        self.assertEqual(text.count("---"), 2)

    def test_other_frontmatter_keys_survive(self):
        resolver.write_frontmatter_doi("037_x", "10.1145/3786319")
        text = self._text()
        for key in ('title: "A Survey"', 'date: "2023.02"',
                    'arxiv: ""', 'journal: "preprint"', '  - "Wenchong He"'):
            self.assertIn(key, text)

    def test_a_doi_line_is_added_when_absent(self):
        (self.root / "037_x" / "review.md").write_text(
            '---\ntitle: "X"\n---\n\nbody\n', encoding="utf-8")
        self.assertTrue(resolver.write_frontmatter_doi("037_x", "10.1000/y"))
        self.assertIn('doi: "10.1000/y"', self._text())

    def test_a_file_without_frontmatter_is_refused(self):
        (self.root / "037_x" / "review.md").write_text("# no frontmatter\n",
                                                       encoding="utf-8")
        self.assertFalse(resolver.write_frontmatter_doi("037_x", "10.1000/y"))

    def test_a_missing_paper_is_refused(self):
        self.assertFalse(resolver.write_frontmatter_doi("999_none", "10.1/x"))


if __name__ == "__main__":
    unittest.main()
