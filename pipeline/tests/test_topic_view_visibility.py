"""Topic cards include reviewed members without classification or taxonomy updates."""
from __future__ import annotations

import json
import os
import re
import sys
import tempfile
import unittest
from html import unescape
from pathlib import Path
from unittest.mock import patch

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import build_topic_index as builder  # noqa: E402


class TopicViewVisibilityTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.docs = Path(temporary.name) / "docs"
        self.papers = self.docs / "papers"
        self.topic = self.docs / "demo"
        self.papers.mkdir(parents=True)
        self.topic.mkdir()
        self.records = []
        self.assignments = []

    def _add_paper(self, slug, classification=None, *, topics=None, license=""):
        directory = self.papers / slug
        directory.mkdir()
        (directory / "review.md").write_text(
            f"# Review {slug}\n\n"
            "> **저자**: Ada Example | **날짜**: 2026-10-25\n\n"
            f"## Essence\nESSENCE-{slug}\n\n"
            "## Evaluation\n- Novelty: 4/5\n- Overall: 4/5\n\n"
            f"**총평**: VERDICT-{slug}\n",
            encoding="utf-8",
        )
        self.records.append({
            "slug": slug,
            "title": f"Review {slug}",
            "topics": ["demo"] if topics is None else topics,
            "classifications": {} if classification is None else {"demo": classification},
            "license": license,
        })

    def _build(self, *, public=False):
        index_path = self.papers / "_papers_index.json"
        classification_path = self.topic / "_new_classification.json"
        index_path.write_text(json.dumps(self.records), encoding="utf-8")
        classification_path.write_text(json.dumps({
            "categories": [{"name": "Established"}],
            "assignments": self.assignments,
        }), encoding="utf-8")
        source_bytes = {
            path: path.read_bytes()
            for path in [index_path, classification_path, *self.papers.glob("*/review.md")]
        }
        with (
            patch.object(builder, "PAPERS_DIR", str(self.papers)),
            patch.object(builder, "DOCS_DIR", self.docs),
            patch.object(builder, "get_topic_dir", return_value=self.topic),
            patch("config_loader.load_config", return_value={"zotero": {"collections": {}}}),
            patch.object(builder, "get_zotero_api_key", return_value="") as api_key,
            patch.object(builder, "get_zotero_user_id", side_effect=AssertionError(
                "keyless topic refresh resolved a Zotero user ID")) as user_id,
            patch("urllib.request.urlopen", side_effect=AssertionError(
                "topic refresh attempted a network request")) as network,
            patch.dict(os.environ, {
                "SKIP_ZOTERO_KEYS": "1",
                "PC_PUBLIC_BUILD": "1" if public else "",
                "PC_ND_POLICY": "suppress",
            }, clear=True),
        ):
            builder._run_topic_index("demo")
        api_key.assert_not_called()
        user_id.assert_not_called()
        network.assert_not_called()
        for path, content in source_bytes.items():
            self.assertEqual(path.read_bytes(), content, str(path))
        self.assertFalse((self.docs / "_zotero_keys.json").exists())
        self.assertFalse((self.docs / "_zotero_meta.json").exists())
        return (self.topic / "index.html").read_text(encoding="utf-8")

    def _groups(self, html):
        parts = re.split(r'<div class="topic-group" data-topic="([^"]*)">', html)
        return {unescape(name): body for name, body in zip(parts[1::2], parts[2::2])}

    def _link(self, slug):
        return f'href="../papers/{slug}/index.html"'

    def test_unclassified_and_explicit_other_members_render_with_known_categories(self):
        self._add_paper("001_known", {"primary_category": "Established"})
        unclassified = [
            None,
            {},
            {"primary_category": None, "all_categories": []},
            {"all_categories": [None, "", "   ", 17]},
            {"all_categories": None},
            {"all_categories": "Established"},
            {"primary_category": "Other", "all_categories": ["Other"]},
        ]
        for number, classification in enumerate(unclassified, 2):
            self._add_paper(f"{number:03d}_unclassified", classification)
        self._add_paper("099_nonmember", topics=["another-topic"])

        groups = self._groups(self._build())

        self.assertEqual(set(groups), {"Established", "Other"})
        self.assertIn(self._link("001_known"), groups["Established"])
        for number in range(2, len(unclassified) + 2):
            self.assertIn(self._link(f"{number:03d}_unclassified"), groups["Other"])
        self.assertNotIn(self._link("099_nonmember"), "".join(groups.values()))

    def test_primary_topic_only_members_render_with_empty_missing_or_null_topics(self):
        for slug, fields in (
            ("001_primary_empty", {"primary_topic": "demo", "topics": []}),
            ("002_primary_missing", {"primary_topic": "demo"}),
            ("003_primary_null", {"primary_topic": "demo", "topics": None}),
            ("099_nonmember", {"primary_topic": "another-topic", "topics": None}),
        ):
            self._add_paper(slug)
            self.records[-1].pop("topics")
            self.records[-1].update(fields)

        groups = self._groups(self._build())

        for slug in ("001_primary_empty", "002_primary_missing", "003_primary_null"):
            self.assertIn(self._link(slug), groups["Other"])
        self.assertNotIn(self._link("099_nonmember"), "".join(groups.values()))

    def test_recorded_categories_missing_from_stale_taxonomy_render_exactly(self):
        emerging = "Emerging & Unlisted"
        self._add_paper("001_new_primary", {
            "primary_category": emerging,
            "all_categories": [],
        })
        self._add_paper("002_multiclass", {
            "primary_category": "Established",
            "all_categories": ["Established", emerging, emerging],
        })
        self.assignments = [{
            "slug": "001_new_primary",
            "primary_category": "Established",
            "all_categories": ["Established"],
        }]

        groups = self._groups(self._build())

        self.assertEqual(set(groups), {"Established", emerging})
        self.assertIn(self._link("001_new_primary"), groups[emerging])
        self.assertNotIn(self._link("001_new_primary"), groups["Established"])
        self.assertEqual(groups[emerging].count(self._link("002_multiclass")), 1)
        self.assertEqual(groups["Established"].count(self._link("002_multiclass")), 1)

    def test_keyless_skip_avoids_credentials_user_id_resolution_and_network(self):
        self._add_paper("001_keyless")

        html = self._build()

        self.assertIn(self._link("001_keyless"), self._groups(html)["Other"])

    def test_other_visibility_preserves_public_nd_suppression_and_local_review(self):
        slug = "001_nd_review"
        self._add_paper(slug, license="cc-by-nd")

        public_html = self._build(public=True)
        local_html = self._build()

        public_other = self._groups(public_html)["Other"]
        self.assertIn(self._link(slug), public_other)
        self.assertIn("변경금지(ND)", public_other)
        self.assertNotIn(f"ESSENCE-{slug}", public_html)
        self.assertNotIn(f"VERDICT-{slug}", public_html)
        self.assertIn(f"ESSENCE-{slug}", local_html)
        self.assertIn(f"VERDICT-{slug}", local_html)


if __name__ == "__main__":
    unittest.main()
