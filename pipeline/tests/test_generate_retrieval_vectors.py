"""Stdlib coverage for fixed retrieval-query vector generation."""
from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from evaluate_retrieval import EvaluationError  # noqa: E402
from generate_retrieval_vectors import generate_manifest  # noqa: E402


class RetrievalVectorGeneratorTests(unittest.TestCase):
    def _queries(self, root: Path) -> Path:
        path = root / "queries.jsonl"
        path.write_text(
            json.dumps({"id": "q1", "query": "alpha", "collection": "demo",
                        "relevant_slugs": ["paper-a"]}) + "\n",
            encoding="utf-8",
        )
        return path

    def test_generate_writes_versioned_manifest(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            queries, output = self._queries(root), root / "vectors.json"
            with patch("generate_retrieval_vectors.resolve_embed_key", return_value="key"), \
                    patch("generate_retrieval_vectors.gemini_embed", return_value=[0.0] * 767 + [1.0]):
                manifest = generate_manifest(queries, output, delay_seconds=0)
            self.assertEqual(manifest["task_type"], "RETRIEVAL_QUERY")
            self.assertEqual(manifest["query_set_sha256"], hashlib.sha256(queries.read_bytes()).hexdigest())
            self.assertEqual(len(manifest["vectors"]["q1"]), 768)
            self.assertEqual(
                json.loads(output.read_text(encoding="utf-8"))["model"],
                "qwen/qwen3-embedding-8b",
            )

    def test_existing_matching_manifest_is_reused_without_api(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            queries, output = self._queries(root), root / "vectors.json"
            with patch("generate_retrieval_vectors.resolve_embed_key", return_value="key"), \
                    patch("generate_retrieval_vectors.gemini_embed", return_value=[1.0] * 768):
                generate_manifest(queries, output, delay_seconds=0)
            with patch("generate_retrieval_vectors.gemini_embed") as embed:
                generate_manifest(queries, output, delay_seconds=0)
            embed.assert_not_called()

    def test_existing_stale_manifest_requires_force(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            queries, output = self._queries(root), root / "vectors.json"
            output.write_text(json.dumps({
                "schema_version": 1, "model": "qwen/qwen3-embedding-8b",
                "task_type": "RETRIEVAL_QUERY", "dim": 1,
                "query_set_sha256": "stale", "vectors": {"q1": [1.0]},
            }), encoding="utf-8")
            with self.assertRaisesRegex(EvaluationError, "does not match"):
                generate_manifest(queries, output, delay_seconds=0)

    def test_new_zero_vector_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            queries, output = self._queries(root), root / "vectors.json"
            with patch("generate_retrieval_vectors.resolve_embed_key", return_value="key"), \
                    patch("generate_retrieval_vectors.gemini_embed", return_value=[0.0] * 768):
                with self.assertRaisesRegex(EvaluationError, "must not be all zeros"):
                    generate_manifest(queries, output, delay_seconds=0)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
