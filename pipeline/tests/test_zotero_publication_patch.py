import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import build_bibliography_db as bib


class _Response:
    status = 204

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False


class ZoteroPublicationPatchTests(unittest.TestCase):
    def test_accepted_publication_replaces_and_reorders_authors(self):
        item = {
            "key": "ABC123",
            "version": 42,
            "data": {
                "itemType": "preprint",
                "DOI": "",
                "creators": [
                    {"creatorType": "author", "firstName": "Ada", "lastName": "Lovelace"},
                    {"creatorType": "author", "firstName": "Grace", "lastName": "Hopper"},
                    {"creatorType": "editor", "firstName": "Edsger", "lastName": "Dijkstra"},
                ],
            },
        }
        bibliography = {
            "doi": "10.1000/formal",
            "journal": "Formal Journal",
            "authors": ["Grace Hopper", "New Middle Author", "Ada Lovelace"],
        }
        captured = {}

        def fake_urlopen(request, **_kwargs):
            captured["request"] = request
            return _Response()

        with patch("config_loader.get_zotero_api_key", return_value="secret"), \
             patch("config_loader.get_zotero_user_id", return_value="7"), \
             patch.object(bib.urllib.request, "urlopen", side_effect=fake_urlopen):
            self.assertTrue(bib.patch_zotero(item, bibliography))

        payload = json.loads(captured["request"].data)
        self.assertEqual(payload["itemType"], "journalArticle")
        self.assertEqual(payload["DOI"], "10.1000/formal")
        self.assertEqual(
            [bib._zotero_creator_name(c) for c in payload["creators"][:3]],
            bibliography["authors"],
        )
        self.assertEqual(payload["creators"][3]["creatorType"], "editor")
        self.assertEqual(
            captured["request"].headers["If-unmodified-since-version"], "42"
        )

    def test_matching_record_returns_none_without_network(self):
        item = {
            "key": "ABC123",
            "version": 42,
            "data": {
                "itemType": "journalArticle",
                "DOI": "10.1000/formal",
                "publicationTitle": "Formal Journal",
                "creators": [
                    {"creatorType": "author", "firstName": "Ada", "lastName": "Lovelace"},
                ],
            },
        }
        bibliography = {
            "doi": "10.1000/formal",
            "journal": "Formal Journal",
            "authors": ["Ada Lovelace"],
        }

        def explode(*_args, **_kwargs):
            raise AssertionError("no-op must not reach the network")

        with patch("config_loader.get_zotero_api_key", return_value="secret"), \
             patch("config_loader.get_zotero_user_id", return_value="7"), \
             patch.object(bib.urllib.request, "urlopen", side_effect=explode):
            self.assertIsNone(bib.patch_zotero(item, bibliography))

class PlaceholderDoiTests(unittest.TestCase):
    """A word meaning "no DOI" is not a DOI.

    Review frontmatter is LLM-extracted; with no DOI on the PDF the model wrote
    the absence down as text. Those strings reached `papers.doi` and then
    `zotero_match`, which compares DOIs — so all 177 papers carrying "N/A"
    matched the one Zotero item whose DOI field held "N/A" and inherited its
    title, journal and pagination.
    """

    PLACEHOLDERS = ["N/A", "n/a", "-", "---", "미제공", "미공개", "미기재",
                    "논문", "해당", "제공되지", "없음", "TBD", "none"]

    def test_placeholders_are_not_dois(self):
        for value in self.PLACEHOLDERS:
            with self.subTest(value=value):
                self.assertEqual(bib.clean_doi(value), "")

    def test_real_dois_survive(self):
        for value in ("10.3389/frma.2021.751553",
                      "10.1038/s41586-026-10652-y",
                      "10.1145/3770855.3818827",
                      "10.52202/085713-0312"):
            with self.subTest(value=value):
                self.assertEqual(bib.clean_doi(value), value)

    def test_url_and_prefix_forms_are_unwrapped(self):
        for value in ("https://doi.org/10.3389/frma.2021.751553",
                      "http://dx.doi.org/10.3389/frma.2021.751553",
                      "doi:10.3389/frma.2021.751553",
                      "10.3389/frma.2021.751553."):
            with self.subTest(value=value):
                self.assertEqual(bib.clean_doi(value),
                                 "10.3389/frma.2021.751553")

    def test_arxiv_dois_are_still_dropped(self):
        self.assertEqual(bib.clean_doi("10.48550/arXiv.2505.13400"), "")

    def test_placeholder_no_longer_matches_a_zotero_item(self):
        items = [{"key": "XIN7LQIB",
                  "data": {"title": "Semantic Scholar", "DOI": "N/A"}}]
        self.assertIsNone(
            bib.zotero_match({"title": "TheoremQA: A Theorem-driven Question "
                                       "Answering Dataset",
                              "doi": "N/A", "arxiv": ""}, items))

    def test_a_real_doi_still_matches(self):
        items = [{"key": "RM7J55RG",
                  "data": {"title": "The Scholarly Knowledge Ecosystem",
                           "DOI": "10.3389/frma.2021.751553"}}]
        self.assertEqual(
            bib.zotero_match({"title": "The Scholarly Knowledge Ecosystem",
                              "doi": "10.3389/frma.2021.751553",
                              "arxiv": ""}, items)["key"], "RM7J55RG")


class LibraryProtectionTests(unittest.TestCase):
    """A patch must not rewrite a library item describing another paper."""

    OTHER_PAPER = {
        "key": "RM7J55RG", "version": 40234,
        "data": {"itemType": "journalArticle",
                 "title": "The reorganization of the American innovation "
                          "ecosystem and the challenge of translating science",
                 "publicationTitle": "Industrial and Corporate Change"},
    }
    RECORD = {"doi": "10.3389/frma.2021.751553",
              "title": "The Scholarly Knowledge Ecosystem: Challenges and "
                       "Opportunities for the Field of Information",
              "journal": "Frontiers in Research Metrics and Analytics"}

    def test_mismatched_item_is_refused_without_a_write(self):
        def explode(*_args, **_kwargs):
            raise AssertionError("a mismatched item must not be written to")

        with patch("config_loader.get_zotero_api_key", return_value="secret"), \
             patch("config_loader.get_zotero_user_id", return_value="7"), \
             patch.object(bib.urllib.request, "urlopen", side_effect=explode):
            self.assertIs(bib.patch_zotero(self.OTHER_PAPER, self.RECORD),
                          False)

    def test_subtitle_drift_is_not_a_mismatch(self):
        item = {"key": "K", "version": 1,
                "data": {"title": "The Scholarly Knowledge Ecosystem: "
                                  "Challenges and Opportunities for the "
                                  "Field of Information."}}
        self.assertTrue(bib._titles_agree(item, self.RECORD))

    def test_an_untitled_item_is_not_treated_as_a_conflict(self):
        self.assertTrue(bib._titles_agree({"data": {}}, self.RECORD))

    def test_ingest_guard_matches_the_patch_guard(self):
        # The build path applies the same rule: an item describing another
        # paper supplies no bibliography for this one.
        louvain = {"key": "ZA7W3PFQ",
                   "data": {"title": "Mapping scientific communities at scale",
                            "DOI": "10.1088/1742-5468/2008/10/P10008"}}
        self.assertFalse(bib._titles_agree(
            louvain, {"title": "Fast Unfolding of Communities in Large "
                               "Networks"}))
        self.assertTrue(bib._titles_agree(
            louvain, {"title": "Mapping scientific communities at scale"}))

    def test_a_pdf_scraped_doi_is_never_written_to_zotero(self):
        # The ICC paper cites Altman and Cohen, so `pdf_bibliography` scraped
        # their DOI out of its reference list. Zotero held no DOI to outrank
        # it, and the patch wrote a Frontiers DOI onto item RM7J55RG.
        item = {"key": "RM7J55RG", "version": 40234,
                "data": {"itemType": "journalArticle",
                         "title": "The reorganization of the American "
                                  "innovation ecosystem",
                         "publicationTitle": "Industrial and Corporate Change"}}
        bibliography = {
            "title": "The reorganization of the American innovation ecosystem",
            "doi": "10.3389/frma.2021.751553",
            "url": "https://doi.org/10.3389/frma.2021.751553",
            "journal": "Industrial and Corporate Change",
            "volume": "34",
            "field_sources": {"title": "zotero-local", "doi": "pdf",
                              "url": "pdf", "journal": "zotero-local",
                              "volume": "zotero-local"},
        }
        captured = {}

        def fake_urlopen(request, **_kwargs):
            captured["payload"] = json.loads(request.data)
            return _Response()

        with patch("config_loader.get_zotero_api_key", return_value="secret"), \
             patch("config_loader.get_zotero_user_id", return_value="7"), \
             patch.object(bib.urllib.request, "urlopen", side_effect=fake_urlopen):
            bib.patch_zotero(item, bibliography)

        payload = captured["payload"]
        self.assertNotIn("DOI", payload)
        self.assertNotIn("url", payload)
        self.assertEqual(payload["volume"], "34")   # a Zotero-sourced field

    def test_a_registered_doi_is_still_written(self):
        item = {"key": "K", "version": 1,
                "data": {"itemType": "preprint", "title": "A Paper"}}
        bibliography = {"title": "A Paper", "doi": "10.1038/x",
                        "field_sources": {"doi": "scopus"}}
        captured = {}

        def fake_urlopen(request, **_kwargs):
            captured["payload"] = json.loads(request.data)
            return _Response()

        with patch("config_loader.get_zotero_api_key", return_value="secret"), \
             patch("config_loader.get_zotero_user_id", return_value="7"), \
             patch.object(bib.urllib.request, "urlopen", side_effect=fake_urlopen):
            self.assertTrue(bib.patch_zotero(item, bibliography))
        self.assertEqual(captured["payload"]["DOI"], "10.1038/x")

    def test_reconcile_records_where_each_field_came_from(self):
        merged = bib.reconcile_bibliography(
            {"title": "A Paper"},
            {"journal": "Some Journal"},
            {"doi": "10.3389/frma.2021.751553"})
        self.assertEqual(merged["field_sources"]["title"], "zotero-local")
        self.assertEqual(merged["field_sources"]["journal"], "scopus")
        self.assertEqual(merged["field_sources"]["doi"], "pdf")
        self.assertEqual(merged["field_sources"]["url"], "pdf")


class AuthorNameParserTests(unittest.TestCase):
    def test_name_parser_supports_comma_and_mononym(self):
        self.assertEqual(
            bib._zotero_author_creator("Curie, Marie"),
            {"creatorType": "author", "firstName": "Marie", "lastName": "Curie"},
        )
        self.assertEqual(
            bib._zotero_author_creator("Plato"),
            {"creatorType": "author", "firstName": "", "lastName": "Plato"},
        )


if __name__ == "__main__":
    unittest.main()
