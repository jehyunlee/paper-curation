#!/usr/bin/env python3
"""Tests for fingerprint-based search-index deploy freshness."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import build_search_index as builder
import prepare_deploy as deploy


class SearchIndexFreshnessTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.docs = self.root / "docs"
        self.papers = self.docs / "papers"
        self.topic = "demo"
        (self.docs / self.topic).mkdir(parents=True)
        (self.papers / "p1").mkdir(parents=True)
        (self.papers / "p1" / "review.md").write_text("review v1", encoding="utf-8")
        self.patches = [
            patch.object(deploy, "DOCS_DIR", self.docs),
            patch.object(deploy, "PAPERS_DIR", str(self.papers)),
        ]
        for item in self.patches:
            item.start()

    def tearDown(self):
        for item in reversed(self.patches):
            item.stop()
        self.tmp.cleanup()

    def write_index(self, fingerprint=None):
        data = {
            "papers": {"p1": {"title": "Paper"}},
            "emb_file": "_search_index_emb.bin",
        }
        if fingerprint is not None:
            data["source_fingerprint"] = fingerprint
        topic_dir = self.docs / self.topic
        (topic_dir / "_search_index.json").write_text(json.dumps(data), encoding="utf-8")
        (topic_dir / "_search_index_emb.bin").write_bytes(b"\x00")

    def test_existing_index_without_manifest_is_unknown_not_false_stale(self):
        self.write_index()
        result = deploy._search_index_freshness(self.topic)
        self.assertIsNone(result["fresh"])

    def test_matching_fingerprint_is_fresh(self):
        fingerprint, count = builder.source_fingerprint(
            self.topic, ["p1"], docs_dir=self.docs, papers_dir=self.papers)
        self.assertEqual(count, 1)
        self.write_index(fingerprint)
        self.assertTrue(deploy._search_index_freshness(self.topic)["fresh"])

    def test_source_change_is_stale_and_preflight_blocks(self):
        fingerprint, _ = builder.source_fingerprint(
            self.topic, ["p1"], docs_dir=self.docs, papers_dir=self.papers)
        self.write_index(fingerprint)
        (self.papers / "p1" / "review.md").write_text("review v2 changed", encoding="utf-8")
        result = deploy._search_index_freshness(self.topic)
        self.assertFalse(result["fresh"])
        with self.assertRaises(SystemExit):
            deploy._preflight_search_indexes([self.topic])


if __name__ == "__main__":
    unittest.main()
