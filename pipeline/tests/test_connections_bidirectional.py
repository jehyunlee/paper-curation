"""Regression tests for the bidirectional consumer connection views."""
from __future__ import annotations

import os
import sys
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

PIPELINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PIPELINE not in sys.path:
    sys.path.insert(0, PIPELINE)

from lib.connections import (  # noqa: E402
    filter_for_topic,
    make_bidirectional_deduped,
    merge_to_global,
)
from lib.related import build_connections  # noqa: E402
import build_bibliography_db as bib  # noqa: E402
import sync_paper_connections as sync  # noqa: E402

PAPERS = [{"slug": "A"}, {"slug": "B"}, {"slug": "C"}]


def _edge(target, cosine):
    return build_connections({"A": [(target, cosine)]}, PAPERS)["A"][0]


class BidirectionalConnectionTests(unittest.TestCase):
    def test_reverse_edge_mirrors_the_mutual_embedding_neighbour(self):
        got = make_bidirectional_deduped({"A": [_edge("B", .8)]})
        forward, reverse = got["A"][0], got["B"][0]
        self.assertEqual((forward["slug"], reverse["slug"]), ("B", "A"))
        self.assertEqual(reverse["relation"], "alternative")
        self.assertEqual(reverse["reason"], forward["reason"])
        self.assertEqual(reverse["basis"], "embedding")

    def test_forward_reason_wins_over_synthesized_reverse(self):
        got = make_bidirectional_deduped({
            "A": [_edge("B", .8)],
            "B": [{**_edge("B", .7), "slug": "A"}],
        })
        self.assertEqual(got["A"][0]["evidence"], {"cosine": .8})
        self.assertEqual(got["B"][0]["evidence"], {"cosine": .7})

    def test_provenance_survives_merge_and_filter(self):
        new = {"A": [_edge("B", .8)]}
        with patch("lib.connections.load_global_connections", return_value={}), \
             patch("lib.connections.save_global_connections"):
            merged = merge_to_global(new, source_topic="demo")
        view = make_bidirectional_deduped(merged)
        item = filter_for_topic(view, ["A"])["A"][0]
        self.assertEqual(item["basis"], "embedding")
        self.assertEqual(item["model"], "")
        self.assertEqual(item["evidence"], {"cosine": .8})
        self.assertEqual(item["reasons"][0]["basis"], "embedding")
        self.assertNotIn("source_topic", item)

    def test_related_normalizes_to_alternative(self):
        got = make_bidirectional_deduped({
            "A": [{"slug": "B", "relation": "related", "reason": "x", "basis": "embedding"}]
        })
        self.assertEqual(got["A"][0]["relation"], "alternative")
        self.assertEqual(got["B"][0]["relation"], "alternative")

    def test_db_import_keeps_only_embedding_edges(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "papers").mkdir()
            (root / "papers" / "_papers_index.json").write_text(json.dumps([
                {**paper, "topics": ["demo"]} for paper in PAPERS]), encoding="utf-8")
            topic_path = Path(tmp) / "demo" / "_paper_connections.json"
            topic_path.parent.mkdir()
            topic_path.write_text(json.dumps({
                "A": [
                    _edge("B", .8),
                    {"slug": "C", "relation": "related", "reason": "이전 항목"},
                    {"slug": "C", "relation": "counterpoint", "reason": "판단",
                     "basis": "model", "model": "claude-haiku-4-5"},
                ], "B": [], "C": []
            }, ensure_ascii=False), encoding="utf-8")
            with patch.object(sync, "DOCS", root):
                claims, _ = sync.load_json_connections()
        self.assertEqual(list(claims), [("A", "B", "alternative")])
        self.assertEqual(claims[("A", "B", "alternative")]["model"], "none:embedding")

    def test_consumer_graph_db_roundtrip_keeps_numeric_forward_and_reverse_evidence(self):
        graph = make_bidirectional_deduped({"A": [_edge("B", .8234)], "C": []})
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "docs"
            (root / "papers").mkdir(parents=True)
            (root / "demo").mkdir()
            (root / "papers" / "_papers_index.json").write_text(json.dumps([
                {**paper, "topics": ["demo"]} for paper in PAPERS]), encoding="utf-8")
            topic_path = root / "demo" / sync.CONNECTIONS_NAME
            topic_path.write_text(json.dumps(graph, ensure_ascii=False), encoding="utf-8")
            db = Path(tmp) / "bibliography.sqlite3"
            with sqlite3.connect(db) as conn:
                conn.executescript(bib.SCHEMA)
                for paper in PAPERS:
                    conn.execute("INSERT INTO papers (slug,title,review_dir) VALUES (?,?,?)",
                                 (paper["slug"], paper["slug"], f"docs/papers/{paper['slug']}"))
            with patch.object(sync, "DOCS", root):
                self.assertEqual(sync.import_connections(db)["imported"], 2)
                topic_path.write_text("{}", encoding="utf-8")
                sync.export_connections(db)
            restored = json.loads(topic_path.read_text(encoding="utf-8"))
        self.assertEqual(restored, graph)
        for source in ("A", "B"):
            self.assertEqual(restored[source][0]["evidence"], {"cosine": .8234})
            self.assertEqual(restored[source][0]["reasons"][0]["evidence"], {"cosine": .8234})
            self.assertIsInstance(restored[source][0]["evidence"]["cosine"], float)


class ProcessedEmptyTests(unittest.TestCase):
    def test_source_with_no_related_paper_stays_as_empty_list(self):
        view = make_bidirectional_deduped({"a": [], "b": [
            {"slug": "c", "relation": "alternative", "basis": "embedding", "reason": "B와 C."}]})
        self.assertEqual(view["a"], [])
        self.assertEqual(view["b"][0]["slug"], "c")
        self.assertNotIn("d", view)


if __name__ == "__main__":
    unittest.main(verbosity=2)
