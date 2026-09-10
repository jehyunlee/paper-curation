"""Regression coverage for cross-index provenance metadata."""
from __future__ import annotations

import json
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_cross_index  # noqa: E402


class CrossIndexFingerprintTests(unittest.TestCase):
    def _sparse_source(self, root, topic, texts):
        directory = root / topic
        directory.mkdir(parents=True, exist_ok=True)
        index = {
            "retrieval_mode": "bm25", "model": None, "dim": 0, "quant": None,
            "count": len(texts), "source_fingerprint": "source-" + topic,
            "papers": {"shared": {"title": topic}},
            "chunks": [
                {"slug": "shared", "section": "How", "text": text,
                 "text_sha": hashlib.sha256(text.encode()).hexdigest()}
                for text in texts
            ],
        }
        (directory / build_cross_index.SEARCH_INDEX).write_text(json.dumps(index))
        return index

    def test_sparse_merge_deduplicates_without_reading_or_changing_vectors(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self._sparse_source(root, "alpha", ["alpha evidence"])
            self._sparse_source(root, "beta", ["beta evidence", "more evidence"])
            output = root / "_cross"
            output.mkdir()
            binary = output / build_cross_index.EMB_BIN
            binary.write_bytes(b"preserved")
            original_read = Path.read_bytes

            def no_vectors(path):
                if path.name.endswith(".bin"):
                    raise AssertionError("BM25 must not read vectors")
                return original_read(path)

            with (
                patch.object(build_cross_index, "DOCS_DIR", root),
                patch.object(build_cross_index, "load_config", return_value={}),
                patch.object(Path, "read_bytes", no_vectors),
            ):
                merged, vectors, counts = build_cross_index.merge_indexes(
                    ["alpha", "beta"], mode="bm25")
                self.assertEqual(vectors, b"")
                self.assertEqual(merged["count"], 2)
                self.assertEqual(len(merged["papers"]), 1)
                self.assertEqual(counts, {"alpha": 1, "beta": 1})
                self.assertNotIn("emb_file", merged)
                build_cross_index.build_cross(
                    ["alpha", "beta"], "Keyword corpus", make_page=False, mode="bm25")
            self.assertEqual(binary.read_bytes(), b"preserved")
            self.assertIn("_cross/", (root / ".assetsignore").read_text())
            published = json.loads((output / build_cross_index.SEARCH_INDEX).read_text())
            self.assertEqual(published["retrieval_mode"], "bm25")

    def test_hybrid_rejects_sparse_sources_before_any_output_change(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self._sparse_source(root, "alpha", ["alpha evidence"])
            before = {p.relative_to(root): p.read_bytes()
                      for p in root.rglob("*") if p.is_file()}
            with (
                patch.object(build_cross_index, "DOCS_DIR", root),
                patch.object(build_cross_index, "load_config", return_value={}),
            ):
                with self.assertRaisesRegex(SystemExit, "BM25 source"):
                    build_cross_index.build_cross(["alpha"], "Hybrid", make_page=False)
            self.assertFalse((root / "_cross").exists())
            self.assertEqual(before, {p.relative_to(root): p.read_bytes()
                                     for p in root.rglob("*") if p.is_file()})

    def test_sparse_source_rejects_conflicting_embedding_metadata(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            index = self._sparse_source(root, "alpha", ["alpha evidence"])
            index["emb_file"] = "stale.bin"
            (root / "alpha" / build_cross_index.SEARCH_INDEX).write_text(json.dumps(index))
            with patch.object(build_cross_index, "DOCS_DIR", root):
                with self.assertRaisesRegex(SystemExit, "malformed bm25"):
                    build_cross_index.merge_indexes(["alpha"], mode="bm25")

    def _source(self, root: Path, topic: str, fingerprint: str, byte: int) -> None:
        directory = root / topic
        directory.mkdir(parents=True, exist_ok=True)
        index = {
            "model": "model", "dim": 2, "quant": "int8-l2norm", "count": 1,
            "source_fingerprint": fingerprint,
            "papers": {f"{topic}-paper": {"title": topic}},
            "chunks": [{"slug": f"{topic}-paper", "text": topic}],
        }
        (directory / build_cross_index.SEARCH_INDEX).write_text(json.dumps(index), encoding="utf-8")
        (directory / build_cross_index.EMB_BIN).write_bytes(bytes([byte, byte]))

    def test_merge_records_sources_and_changes_fingerprint(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self._source(root, "alpha", "source-a", 1)
            self._source(root, "beta", "source-b", 2)
            with patch.object(build_cross_index, "DOCS_DIR", root):
                first, _, _ = build_cross_index.merge_indexes(["alpha", "beta"])
                self.assertEqual(first["source_file_count"], 2)
                self.assertEqual(first["source_indexes"]["alpha"]["source_fingerprint"], "source-a")
                self.assertEqual(first["count"], 2)
                self._source(root, "alpha", "source-a-revised", 3)
                second, _, _ = build_cross_index.merge_indexes(["alpha", "beta"])
            self.assertNotEqual(first["source_fingerprint"], second["source_fingerprint"])
            self.assertNotEqual(first["source_indexes"]["alpha"]["index_sha256"],
                                second["source_indexes"]["alpha"]["index_sha256"])

    def test_merge_rejects_unknown_quantization(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self._source(root, "alpha", "source-a", 1)
            path = root / "alpha" / build_cross_index.SEARCH_INDEX
            index = json.loads(path.read_text(encoding="utf-8"))
            index["quant"] = "float32"
            path.write_text(json.dumps(index), encoding="utf-8")
            with patch.object(build_cross_index, "DOCS_DIR", root):
                with self.assertRaisesRegex(SystemExit, "지원하지 않는 양자화"):
                    build_cross_index.merge_indexes(["alpha"])

    def test_merge_rejects_missing_model(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self._source(root, "alpha", "source-a", 1)
            path = root / "alpha" / build_cross_index.SEARCH_INDEX
            index = json.loads(path.read_text(encoding="utf-8"))
            index["model"] = None
            path.write_text(json.dumps(index), encoding="utf-8")
            with patch.object(build_cross_index, "DOCS_DIR", root):
                with self.assertRaisesRegex(SystemExit, "모델 정보"):
                    build_cross_index.merge_indexes(["alpha"])


if __name__ == "__main__":
    unittest.main()
