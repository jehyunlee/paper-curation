"""Deterministic stdlib tests for the read-only Deep Research query engine."""
from __future__ import annotations

import json
import hashlib
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import query_search_index as query_module  # noqa: E402
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


def _write_sparse_index(root: Path) -> Path:
    docs = root / "docs"
    topic = docs / "demo"
    topic.mkdir(parents=True)
    chunks = [
        {"slug": "a", "section": "How", "text": "alpha alpha method"},
        {"slug": "b", "section": "How", "text": "beta Korean 한국어"},
    ]
    for chunk in chunks:
        chunk["text_sha"] = hashlib.sha256(
            chunk["text"].encode("utf-8")).hexdigest()
    index = {
        "retrieval_mode": "bm25",
        "model": None,
        "dim": 0,
        "quant": None,
        "count": len(chunks),
        "papers": {
            "a": {"title": "Alpha paper", "year": 2024,
                  "url": "https://example.test/a"},
            "b": {"title": "Beta paper", "year": 2021,
                  "external_url": "https://doi.org/test-b"},
        },
        "chunks": chunks,
        "source_fingerprint": "a" * 64,
        "source_file_count": 2,
        "built_at": 1,
    }
    (topic / "_search_index.json").write_text(
        json.dumps(index), encoding="utf-8")
    return docs


class QuerySearchIndexTests(unittest.TestCase):
    def test_automatic_query_embedding_requires_matching_model_and_dimension(self):
        with tempfile.TemporaryDirectory() as td:
            docs = _write_index(Path(td), sidecar=bytes([127, 0] * 5))
            with patch.object(query_module, "_embed_query", side_effect=AssertionError("embedding request")) as embed:
                with self.assertRaisesRegex(ValueError, "model/dimension differs"):
                    query_search_index("demo", "alpha", mode="hybrid", docs_dir=docs)
            embed.assert_not_called()

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

    def test_sparse_schema_is_keyless_and_no_match_returns_empty(self):
        with tempfile.TemporaryDirectory() as td, patch.dict(
                os.environ, {}, clear=True), patch.object(
                query_module, "_embed_query",
                side_effect=AssertionError("sparse BM25 requested embedding")):
            docs = _write_sparse_index(Path(td))
            match = query_search_index(
                "demo", "한국어", mode="bm25", docs_dir=docs)
            no_match = query_search_index(
                "demo", "zzznomatchtoken", mode="bm25", docs_dir=docs)
        self.assertEqual(match["results"][0]["slug"], "b")
        self.assertEqual(match["model"], None)
        self.assertEqual(match["dim"], 0)
        self.assertEqual(no_match["results"], [])

    def test_dense_modes_reject_sparse_index_before_embedding_or_sidecar(self):
        with tempfile.TemporaryDirectory() as td:
            docs = _write_sparse_index(Path(td))
            with patch.object(
                    query_module, "_embed_query",
                    side_effect=AssertionError("credential/query embedding lookup")
                    ) as embed, patch.object(
                    query_module, "_normalize_query_vector",
                    side_effect=AssertionError("query vector normalization")
                    ) as normalize, patch.object(
                    query_module, "_load_embedding_bytes",
                    side_effect=AssertionError("embedding sidecar lookup")
                    ) as sidecar:
                for mode, vector in (("hybrid", None), ("dense", [1, 0])):
                    with self.subTest(mode=mode), self.assertRaisesRegex(
                            ValueError, "requires a dense/hybrid index"):
                        query_search_index(
                            "demo", "alpha", mode=mode,
                            query_vector=vector, docs_dir=docs)
            embed.assert_not_called()
            normalize.assert_not_called()
            sidecar.assert_not_called()

    def test_sparse_schema_rejects_mixed_embedding_metadata(self):
        mutations = {
            "positive dim": lambda index: index.update(dim=2),
            "model": lambda index: index.update(model="dense-model"),
            "quant": lambda index: index.update(quant="int8-l2norm"),
            "emb_file": lambda index: index.update(emb_file="vectors.bin"),
            "chunk emb": lambda index: index["chunks"][0].update(emb="AA=="),
            "cache-style text sha": lambda index: index["chunks"][0].update(
                text_sha="0" * 64),
        }
        for label, mutate in mutations.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as td:
                docs = _write_sparse_index(Path(td))
                path = docs / "demo" / "_search_index.json"
                index = json.loads(path.read_text(encoding="utf-8"))
                mutate(index)
                path.write_text(json.dumps(index), encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "invalid sparse search index"):
                    query_search_index(
                        "demo", "alpha", mode="bm25", docs_dir=docs)

    def test_bm25_no_match_is_empty_on_legacy_dense_index(self):
        with tempfile.TemporaryDirectory() as td:
            docs = _write_index(Path(td), sidecar=None)
            result = query_search_index(
                "demo", "zzznomatchtoken", mode="bm25", docs_dir=docs)
        self.assertEqual(result["results"], [])

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
