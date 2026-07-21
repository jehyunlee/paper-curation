"""Coverage for the TCC-safe retrieval evaluation snapshot."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from refresh_retrieval_eval_snapshot import EVAL_FILES, RUNTIME_FILES, refresh_snapshot  # noqa: E402


class RetrievalEvalSnapshotTests(unittest.TestCase):
    def test_refresh_copies_runtime_eval_and_collection_indexes_atomically(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "project"
            output = Path(td) / "snapshot"
            (root / "pipeline" / "eval").mkdir(parents=True)
            (root / "docs" / "demo").mkdir(parents=True)
            for name in RUNTIME_FILES:
                (root / "pipeline" / name).write_text(name, encoding="utf-8")
            query = {"id": "q1", "query": "alpha", "collection": "demo", "relevant_slugs": ["a"]}
            for name in EVAL_FILES:
                content = json.dumps(query) + "\n" if name == "retrieval_queries.jsonl" else "{}\n"
                (root / "pipeline" / "eval" / name).write_text(content, encoding="utf-8")
            (root / "docs" / "demo" / "_search_index.json").write_text("{}", encoding="utf-8")
            (root / "docs" / "demo" / "_search_index_emb.bin").write_bytes(b"index")

            refresh_snapshot(root, output)
            self.assertEqual((output / "pipeline" / "evaluate_retrieval.py").read_text(),
                             "evaluate_retrieval.py")
            self.assertEqual((output / "docs" / "demo" / "_search_index_emb.bin").read_bytes(), b"index")

            (output / "stale").write_text("old", encoding="utf-8")
            refresh_snapshot(root, output)
            self.assertFalse((output / "stale").exists())
            self.assertFalse(output.with_name(".snapshot.previous").exists())


if __name__ == "__main__":
    unittest.main()
