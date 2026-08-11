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
