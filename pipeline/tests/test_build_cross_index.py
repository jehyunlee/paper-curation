"""Regression coverage for cross-index provenance metadata."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_cross_index  # noqa: E402


class CrossIndexFingerprintTests(unittest.TestCase):
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
