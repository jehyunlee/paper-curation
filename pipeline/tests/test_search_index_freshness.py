#!/usr/bin/env python3
"""Tests for fingerprint-based search-index deploy freshness."""
from __future__ import annotations

import hashlib
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

    def write_sparse_index(self, fingerprint, source_count, mutate=None):
        text = "sparse chunk"
        data = {
            "retrieval_mode": "bm25",
            "model": None,
            "dim": 0,
            "quant": None,
            "count": 1,
            "papers": {"p1": {"title": "Paper"}},
            "chunks": [{
                "slug": "p1",
                "section": "Essence",
                "text": text,
                "text_sha": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            }],
            "source_fingerprint": fingerprint,
            "source_file_count": source_count,
        }
        if mutate is not None:
            mutate(data)
        topic_dir = self.docs / self.topic
        (topic_dir / "_search_index.json").write_text(json.dumps(data), encoding="utf-8")

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

    def test_fresh_sparse_index_does_not_require_embedding_sidecar(self):
        fingerprint, count = builder.source_fingerprint(
            self.topic, ["p1"], docs_dir=self.docs, papers_dir=self.papers)
        self.write_sparse_index(fingerprint, count)

        result = deploy._search_index_freshness(self.topic)

        self.assertTrue(result["fresh"])
        self.assertEqual(result["retrieval_mode"], "bm25")
        self.assertFalse((self.docs / self.topic / "_search_index_emb.bin").exists())

    def test_stale_sparse_preflight_prints_mode_preserving_command_only(self):
        fingerprint, count = builder.source_fingerprint(
            self.topic, ["p1"], docs_dir=self.docs, papers_dir=self.papers)
        self.write_sparse_index(fingerprint, count)
        (self.papers / "p1" / "review.md").write_text(
            "review v2 changed", encoding="utf-8")

        with patch("builtins.print") as print_mock, \
                patch.object(deploy.subprocess, "run") as run_mock:
            with self.assertRaises(SystemExit):
                deploy._preflight_search_indexes([self.topic])

        output = "\n".join(
            " ".join(str(arg) for arg in call.args)
            for call in print_mock.call_args_list
        )
        self.assertIn(
            "build_search_index.py --topic demo --mode bm25",
            output,
        )
        run_mock.assert_not_called()

    def test_dense_index_still_requires_embedding_sidecar(self):
        fingerprint, _ = builder.source_fingerprint(
            self.topic, ["p1"], docs_dir=self.docs, papers_dir=self.papers)
        self.write_index(fingerprint)
        (self.docs / self.topic / "_search_index_emb.bin").unlink()

        result = deploy._search_index_freshness(self.topic)

        self.assertFalse(result["fresh"])
        self.assertIn("embedding sidecar missing", result["reason"])

    def test_mixed_sparse_dense_metadata_is_malformed(self):
        fingerprint, count = builder.source_fingerprint(
            self.topic, ["p1"], docs_dir=self.docs, papers_dir=self.papers)
        mutations = {
            "model": lambda data: data.update(model="gemini-embedding-001"),
            "dim": lambda data: data.update(dim=768),
            "quant": lambda data: data.update(quant="int8-l2norm"),
            "emb_file": lambda data: data.update(emb_file="_search_index_emb.bin"),
            "inline_embedding": lambda data: data["chunks"][0].update(emb="AAAA"),
            "count": lambda data: data.update(count=2),
        }
        for label, mutate in mutations.items():
            with self.subTest(label=label):
                self.write_sparse_index(fingerprint, count, mutate=mutate)
                result = deploy._search_index_freshness(self.topic)
                self.assertFalse(result["fresh"])
                self.assertIn("malformed bm25 index metadata", result["reason"])

    def test_sparse_source_file_count_must_match_current_sources(self):
        fingerprint, count = builder.source_fingerprint(
            self.topic, ["p1"], docs_dir=self.docs, papers_dir=self.papers)
        self.write_sparse_index(fingerprint, count + 1)

        result = deploy._search_index_freshness(self.topic)

        self.assertFalse(result["fresh"])
        self.assertIn("source_file_count", result["reason"])


if __name__ == "__main__":
    unittest.main()
