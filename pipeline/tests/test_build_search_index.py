"""Builder contracts for keyless BM25 and opt-in hybrid search indexes."""
from __future__ import annotations

import builtins
import hashlib
import json
import os
import sys
import tempfile
import types
import unittest
from contextlib import contextmanager
from pathlib import Path
from unittest.mock import Mock, patch

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import api as public_api  # noqa: E402
import build_search_index as builder  # noqa: E402
import query_search_index as query_engine  # noqa: E402


@contextmanager
def _block_dense_dependencies():
    real_import = builtins.__import__

    def guarded_import(name, *args, **kwargs):
        if name == "numpy" or name == "google" or name.startswith("google."):
            raise AssertionError(f"dense dependency imported during BM25 build: {name}")
        return real_import(name, *args, **kwargs)

    with patch("builtins.__import__", side_effect=guarded_import), patch.object(
            builder, "_resolve_google_key",
            side_effect=AssertionError("credential lookup during BM25 build")):
        yield


class BuildSearchIndexTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.docs = self.root / "docs"
        self.topic_dir = self.docs / "demo"
        self.papers = self.docs / "papers"
        self.paper_dir = self.papers / "alpha-paper"
        self.topic_dir.mkdir(parents=True)
        (self.paper_dir / "figures").mkdir(parents=True)
        (self.paper_dir / "figures" / "fig1.png").write_bytes(b"not-an-image")

        review = """# Alpha Catalyst Discovery

> **저자**: Ada Example, Bob Example | **날짜**: 2024-01-02

## How
The alpha catalyst method uses a graph search to identify stable reaction pathways efficiently.

## Achievement
Alpha catalyst retrieval improves the measured reaction yield over the baseline experiment.
"""
        (self.paper_dir / "review.md").write_text(review, encoding="utf-8")
        (self.paper_dir / "text.md").write_text(
            "Figure 1: SOURCE-CAPTION-SECRET from the licensed paper body.\n"
            "SOURCE-TEXT-SECRET method proposes an algorithm model trained on a "
            "dataset and reports experiment accuracy of 91.7 percent.",
            encoding="utf-8",
        )
        (self.paper_dir / "notes.md").write_text(
            "COLOCATED-NOTE-SECRET is a private hypothesis that must remain local.",
            encoding="utf-8",
        )
        notes_dir = self.docs / "notes" / "demo"
        notes_dir.mkdir(parents=True)
        (notes_dir / "private.md").write_text(
            "# Private idea\n\nDOCS-NOTE-SECRET is another private research hypothesis.",
            encoding="utf-8",
        )
        self.papers_index = self.papers / "_papers_index.json"
        self.papers_index.write_text(json.dumps([{
            "slug": "alpha-paper",
            "title": "Alpha Catalyst Discovery",
            "date": "2024",
            "primary_topic": "demo",
            "classifications": {
                "demo": {"primary_category": "Catalysis"},
            },
        }]), encoding="utf-8")

        self.topic_lookup = Mock(side_effect=lambda topic: self.docs / topic)
        self.patchers = [
            patch.object(builder, "DOCS_DIR", self.docs),
            patch.object(builder, "PAPERS_DIR", self.papers),

            patch.object(builder, "get_topic_dir", self.topic_lookup),
            patch.object(builder, "get_papers_index_path",
                         return_value=self.papers_index),
            patch.object(builder, "_ZMETA_CACHE", {}),
        ]
        for patcher in self.patchers:
            patcher.start()

    def tearDown(self):
        for patcher in reversed(self.patchers):
            patcher.stop()
        self.tmp.cleanup()

    def _snapshot(self):
        return {
            path.relative_to(self.root).as_posix(): path.read_bytes()
            for path in self.root.rglob("*")
            if path.is_file()
        }

    def test_local_sparse_freshness_uses_the_build_source_options(self):
        import prepare_deploy

        (self.docs / ".assetsignore").write_text("demo/\n", encoding="utf-8")
        with patch.dict(os.environ, {}, clear=True), _block_dense_dependencies():
            built = builder.build_index(
                "demo", "gemini-embedding-001", None, False, mode="bm25")
        self.assertTrue(built["source_options"]["include_text"])
        with (
            patch.object(prepare_deploy, "DOCS_DIR", self.docs),
            patch.object(prepare_deploy, "PAPERS_DIR", self.papers),
        ):
            self.assertTrue(prepare_deploy._search_index_freshness("demo")["fresh"])
            with (self.paper_dir / "text.md").open("a") as handle:
                handle.write("\nNew source evidence.")
            self.assertFalse(prepare_deploy._search_index_freshness("demo")["fresh"])

    def test_sparse_builder_to_query_is_keyless_and_has_real_no_match(self):
        binary_path = self.topic_dir / builder.EMB_BIN_NAME
        cache_path = self.topic_dir / builder.EMBED_CACHE_NAME
        binary_path.write_bytes(b"prior-dense-binary")
        cache_path.write_bytes(b"prior-dense-cache")

        with patch.dict(os.environ, {}, clear=True), patch.object(
                builder, "load_embedding_cache",
                side_effect=AssertionError("BM25 loaded embedding cache")), patch.object(
                builder, "save_embedding_cache",
                side_effect=AssertionError("BM25 saved embedding cache")), _block_dense_dependencies():
            built = builder._run_search_index(
                "demo", mode="bm25", include_text="no")
            with patch.object(
                    query_engine, "_embed_query",
                    side_effect=AssertionError("BM25 queried an embedding provider")):
                match = query_engine.query_search_index(
                    "demo", "alpha catalyst", mode="bm25", docs_dir=self.docs)
                no_match = query_engine.query_search_index(
                    "demo", "zzznomatchtoken", mode="bm25", docs_dir=self.docs)

        index = json.loads(
            (self.topic_dir / "_search_index.json").read_text(encoding="utf-8"))
        self.assertEqual(built, index)
        self.assertEqual(index["retrieval_mode"], "bm25")
        self.assertIsNone(index["model"])
        self.assertEqual(index["dim"], 0)
        self.assertIsNone(index["quant"])
        self.assertEqual(index["count"], len(index["chunks"]))
        self.assertNotIn("emb_file", index)
        for chunk in index["chunks"]:
            self.assertNotIn("emb", chunk)
            self.assertEqual(
                chunk["text_sha"],
                hashlib.sha256(chunk["text"].encode("utf-8")).hexdigest(),
            )
        self.assertEqual(match["results"][0]["slug"], "alpha-paper")
        self.assertEqual(no_match["results"], [])
        self.assertEqual(binary_path.read_bytes(), b"prior-dense-binary")
        self.assertEqual(cache_path.read_bytes(), b"prior-dense-cache")

    def test_public_sparse_index_excludes_source_text_and_personal_notes(self):
        with _block_dense_dependencies():
            builder._run_search_index("demo", mode="bm25")

        payload = (self.topic_dir / "_search_index.json").read_text(encoding="utf-8")
        for secret in (
                "SOURCE-CAPTION-SECRET", "SOURCE-TEXT-SECRET",
                "COLOCATED-NOTE-SECRET", "DOCS-NOTE-SECRET"):
            self.assertNotIn(secret, payload)
        self.assertNotIn("_note_private", json.loads(payload)["papers"])

        before = self._snapshot()
        with self.assertRaises(SystemExit) as raised:
            builder._run_search_index(
                "demo", mode="bm25", include_text="yes")
        self.assertEqual(raised.exception.code, 4)
        self.assertEqual(self._snapshot(), before)

    def test_local_sparse_index_keeps_local_source_and_notes(self):
        (self.docs / ".assetsignore").write_text("demo/\n", encoding="utf-8")
        with _block_dense_dependencies():
            builder._run_search_index("demo", mode="bm25")
        payload = (self.topic_dir / "_search_index.json").read_text(encoding="utf-8")
        self.assertIn("SOURCE-TEXT-SECRET", payload)
        self.assertIn("COLOCATED-NOTE-SECRET", payload)
        self.assertIn("DOCS-NOTE-SECRET", payload)

    def test_dry_run_is_read_only_for_both_modes(self):
        (self.topic_dir / "_search_index.json").write_bytes(b"existing-json")
        (self.topic_dir / builder.EMB_BIN_NAME).write_bytes(b"existing-binary")
        (self.topic_dir / builder.EMBED_CACHE_NAME).write_bytes(b"existing-cache")
        expected = self._snapshot()

        for mode in ("hybrid", "bm25"):
            with self.subTest(mode=mode), patch.dict(
                    os.environ, {}, clear=True), _block_dense_dependencies():
                plan = builder._run_search_index(
                    "demo", mode=mode, dry_run=True, include_text="no")
            self.assertTrue(plan["dry_run"])
            self.assertEqual(plan["retrieval_mode"], mode)
            self.assertEqual(self._snapshot(), expected)

    def test_default_mode_remains_hybrid_with_mocked_embeddings(self):
        fake_google = types.ModuleType("google")
        fake_genai = types.ModuleType("google.genai")
        client = object()
        fake_genai.Client = Mock(return_value=client)
        fake_google.genai = fake_genai

        def fake_embed(actual_client, texts, model):
            self.assertIs(actual_client, client)
            self.assertEqual(model, "gemini-embedding-001")
            return [[1.0] + [0.0] * 767 for _ in texts]

        with patch.dict(
                sys.modules,
                {"google": fake_google, "google.genai": fake_genai}), patch.dict(
                os.environ, {"GOOGLE_API_KEY": "test-only"}, clear=True), patch.object(
                builder, "embed_batch", side_effect=fake_embed), patch.object(
                builder, "_resolve_google_key",
                return_value="test-only"):
            built = builder._run_search_index("demo", include_text="no")

        self.assertEqual(built["retrieval_mode"], "hybrid")
        self.assertEqual(built["model"], "gemini-embedding-001")
        self.assertEqual(built["dim"], 768)
        self.assertEqual(built["quant"], "int8-l2norm")
        self.assertEqual(built["emb_file"], builder.EMB_BIN_NAME)
        self.assertEqual(
            (self.topic_dir / builder.EMB_BIN_NAME).stat().st_size,
            built["count"] * built["dim"],
        )
        cache = json.loads(
            (self.topic_dir / builder.EMBED_CACHE_NAME).read_text(encoding="utf-8"))
        self.assertEqual((cache["model"], cache["dim"]),
                         ("gemini-embedding-001", 768))

    def test_unsupported_mode_is_rejected_before_filesystem_access(self):
        self.topic_lookup.reset_mock()
        with self.assertRaisesRegex(ValueError, "mode must be one of"):
            builder._run_search_index("demo", mode="semantic")
        self.topic_lookup.assert_not_called()

    def test_public_api_passes_mode_to_builder(self):
        with patch.object(
                builder, "_run_search_index", return_value={"ok": True}) as run:
            self.assertEqual(
                public_api.build_search_index("demo", mode="bm25"),
                {"ok": True},
            )
            run.assert_called_once_with(
                topic="demo", mode="bm25", model="gemini-embedding-001",
                limit=None, dry_run=False, include_text="auto")


if __name__ == "__main__":
    unittest.main()
