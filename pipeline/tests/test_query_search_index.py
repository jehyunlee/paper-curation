"""Deterministic stdlib tests for the read-only Deep Research query engine."""
from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from query_search_index import build_parser, query_search_index, tokenize  # noqa: E402


def _write_index(root: Path, *, sidecar: bytes | None = None,
                 count: int = 5, dim: int = 2) -> Path:
    docs = root / "docs"
    topic = docs / "demo"
    topic.mkdir(parents=True)
    chunks = [
        {"slug": "a", "section": "How", "text": "alpha alpha method"},
        {"slug": "a", "section": "Achievement", "text": "alpha result"},
        {"slug": "a", "section": "Evaluation", "text": "alpha evaluation"},
        {"slug": "a", "section": "Limitation", "text": "alpha limitation"},
        {"slug": "b", "section": "How", "text": "beta Korean 한국어"},
    ]
    index = {
        "model": "test-model", "dim": dim, "count": count,
        "emb_file": "_search_index_emb.bin",
        "papers": {
            "a": {"title": "Alpha paper", "year": 2024,
                  "url": "https://example.test/a"},
            "b": {"title": "Beta paper", "year": 2021,
                  "external_url": "https://doi.org/test-b"},
        },
        "chunks": chunks,
    }
    (topic / "_search_index.json").write_text(json.dumps(index), encoding="utf-8")
    if sidecar is not None:
        (topic / "_search_index_emb.bin").write_bytes(sidecar)
    return docs


class QuerySearchIndexTests(unittest.TestCase):
    def test_tokenize_matches_browser_ascii_and_hangul_bigrams(self):
        self.assertEqual(tokenize("GNN-2 한국어 가"), ["gnn", "2", "한국", "국어", "가"])

    def test_bm25_needs_neither_sidecar_nor_key(self):
        with tempfile.TemporaryDirectory() as td, patch.dict(
                os.environ, {"GOOGLE_API_KEY": "", "GEMINI_API_KEY": ""}):
            docs = _write_index(Path(td), sidecar=None)
            result = query_search_index("demo", "alpha", mode="bm25", docs_dir=docs)
        self.assertEqual(result["results"][0]["slug"], "a")
        self.assertEqual(result["results"][0]["dense_score"], 0.0)
        self.assertEqual(result["results"][0]["url"], "https://example.test/a")

    def test_dense_and_hybrid_use_deterministic_query_vector(self):
        sidecar = bytes([127, 0, 127, 0, 127, 0, 127, 0, 0, 127])
        with tempfile.TemporaryDirectory() as td:
            docs = _write_index(Path(td), sidecar=sidecar)
            dense = query_search_index(
                "demo", "unrelated", mode="dense", query_vector=[0, 4], docs_dir=docs)
            hybrid = query_search_index(
                "demo", "beta", mode="hybrid", query_vector=[0, 1], docs_dir=docs)
        self.assertEqual(dense["results"][0]["slug"], "b")
        self.assertAlmostEqual(dense["results"][0]["dense_score"], 1.0)
        self.assertEqual(hybrid["results"][0]["slug"], "b")
        self.assertAlmostEqual(hybrid["results"][0]["rrf_score"], 2 / 60)

    def test_rrf_and_diversity_cap_three_chunks_per_paper(self):
        with tempfile.TemporaryDirectory() as td:
            docs = _write_index(Path(td), sidecar=bytes([127, 0] * 4 + [0, 127]))
            result = query_search_index(
                "demo", "alpha", top_k=5, mode="hybrid",
                query_vector=[1, 0], docs_dir=docs)
        self.assertEqual([item["slug"] for item in result["results"]].count("a"), 3)
        self.assertAlmostEqual(result["results"][0]["rrf_score"], 2 / 60)
        self.assertEqual(result["results"][3]["slug"], "b")

    def test_year_filters_are_inclusive(self):
        with tempfile.TemporaryDirectory() as td:
            docs = _write_index(Path(td), sidecar=None)
            result = query_search_index(
                "demo", "alpha beta", mode="bm25", min_year=2024,
                max_year=2024, docs_dir=docs)
        self.assertEqual([item["slug"] for item in result["results"]], ["a", "a", "a"])

    def test_sidecar_and_vector_validation(self):
        with tempfile.TemporaryDirectory() as td:
            docs = _write_index(Path(td), sidecar=b"bad")
            with self.assertRaisesRegex(ValueError, "sidecar size mismatch"):
                query_search_index("demo", "alpha", mode="dense",
                                   query_vector=[1, 0], docs_dir=docs)
            with self.assertRaisesRegex(ValueError, "dimension mismatch"):
                query_search_index("demo", "alpha", mode="dense",
                                   query_vector=[1], docs_dir=docs)

    def test_json_ready_output_and_cli_defaults(self):
        with tempfile.TemporaryDirectory() as td:
            docs = _write_index(Path(td), sidecar=None)
            result = query_search_index("demo", "한국어", mode="bm25", docs_dir=docs)
        roundtrip = json.loads(json.dumps(result, ensure_ascii=False))
        self.assertEqual(roundtrip["results"][0]["url"], "https://doi.org/test-b")
        args = build_parser().parse_args(["--query", "test", "--json"])
        self.assertEqual((args.topic, args.as_json, args.mode), ("_cross", True, "hybrid"))


if __name__ == "__main__":
    unittest.main()
