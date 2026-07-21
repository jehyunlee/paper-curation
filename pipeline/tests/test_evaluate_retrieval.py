"""Stdlib coverage for deterministic local retrieval evaluation."""
from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from evaluate_retrieval import (  # noqa: E402
    EvaluationError, build_report, compute_metrics, evaluate_rows, load_query_set,
    load_vector_manifest, main, strict_failures, validate_baseline_identity,
    validate_baseline_metrics, validate_relevant_slugs, write_baseline, write_report,
)


class RetrievalEvaluatorTests(unittest.TestCase):
    def _fixture(self, root: Path, *, relevant: str = "a") -> tuple[Path, Path, Path]:
        docs = root / "docs"
        topic = docs / "demo"
        topic.mkdir(parents=True)
        (topic / "_search_index.json").write_text(json.dumps({"papers": {"a": {}, "b": {}}}), encoding="utf-8")
        queries = root / "queries.jsonl"
        queries.write_text(json.dumps({"id": "q1", "query": "alpha", "collection": "demo",
                                      "relevant_slugs": [relevant]}) + "\n", encoding="utf-8")
        digest = hashlib.sha256(queries.read_bytes()).hexdigest()
        vectors = root / "vectors.json"
        vectors.write_text(json.dumps({"schema_version": 1, "model": "fixed", "dim": 2,
                                       "query_set_sha256": digest, "vectors": {"q1": [1, 0]}}), encoding="utf-8")
        return docs, queries, vectors

    def test_schema_errors_and_manifest_hash_coverage(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            queries = root / "bad.jsonl"
            queries.write_text('{"id":"x"}\n', encoding="utf-8")
            with self.assertRaisesRegex(EvaluationError, "missing required"):
                load_query_set(queries)
            docs, queries, vectors = self._fixture(root)
            rows, digest = load_query_set(queries)
            bad = json.loads(vectors.read_text(encoding="utf-8"))
            bad["query_set_sha256"] = "0" * 64
            vectors.write_text(json.dumps(bad), encoding="utf-8")
            with self.assertRaisesRegex(EvaluationError, "does not match"):
                load_vector_manifest(vectors, rows, digest)

    def test_metrics_ranks_and_expected_slug_metadata(self):
        rows = [{"id": "q1", "query": "alpha", "collection": "demo", "relevant_slugs": ["a", "b"]}]
        with patch("evaluate_retrieval.query_search_index", return_value={"results": [
                {"slug": "x"}, {"slug": "a"}, {"slug": "b"}]}) as query:
            evaluated = evaluate_rows(rows, {"q1": [1.0, 0.0]}, docs_dir="unused")
        self.assertEqual(evaluated[0]["ranks"], {"a": 2, "b": 3})
        query.assert_called_once_with("demo", "alpha", mode="hybrid", query_vector=[1.0, 0.0], top_k=10,
                                      docs_dir="unused")
        metrics = compute_metrics(evaluated)
        self.assertEqual(metrics["collections"]["demo"]["query_count"], 1)
        self.assertEqual(metrics["aggregate"]["recall_at_5"], 1.0)
        self.assertEqual(metrics["aggregate"]["mrr_at_10"], 0.5)
        with tempfile.TemporaryDirectory() as td:
            docs, queries, vectors = self._fixture(Path(td), relevant="missing")
            rows, _ = load_query_set(queries)
            with self.assertRaisesRegex(EvaluationError, "absent"):
                validate_relevant_slugs(rows, docs)

    def test_strict_threshold_and_regression(self):
        metrics = {"collections": {"demo": {"query_count": 1, "recall_at_5": 0.8,
                    "recall_at_10": 1.0, "mrr_at_10": 1.0, "failure_count": 0}}, "aggregate": {}}
        report = build_report([], metrics, query_set_sha256="q", vector_manifest_sha256="v")
        threshold = strict_failures(report, None, min_recall_at_5=0.95, max_regression=0.025)
        self.assertEqual(len(threshold), 1)
        baseline = {"collections": {"demo": {"recall_at_5": 0.9}}}
        regression = strict_failures(report, baseline, min_recall_at_5=0.0, max_regression=0.025)
        self.assertEqual(len(regression), 1)

    def test_failures_capture_recall_at_five_misses(self):
        evaluations = [{"id": "q1", "query": "alpha", "collection": "demo",
                        "relevant_slugs": ["a"], "ranks": {"a": 6}, "top_slugs": ["x"] * 6}]
        metrics = compute_metrics(evaluations)
        report = build_report(evaluations, metrics, query_set_sha256="q", vector_manifest_sha256="v")
        self.assertEqual(metrics["aggregate"]["failure_count"], 1)
        self.assertEqual([item["id"] for item in report["failures"]], ["q1"])

    def test_baseline_identity_must_match(self):
        report = {"query_set_sha256": "current", "vector_manifest_sha256": "vectors"}
        with self.assertRaisesRegex(EvaluationError, "query_set_sha256"):
            validate_baseline_identity(
                {"query_set_sha256": "stale", "vector_manifest_sha256": "vectors"}, report)

        with self.assertRaisesRegex(EvaluationError, "valid recall_at_5"):
            validate_baseline_metrics(
                {"collections": {"demo": {"recall_at_5": float("nan")}}},
                {"collections": {"demo": {}}},
            )
        with self.assertRaisesRegex(EvaluationError, "valid recall_at_5"):
            validate_baseline_metrics(
                {"collections": {}},
                {"collections": {"demo": {}}},
            )

    def test_atomic_report_and_compact_baseline_outputs(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            report = {"schema_version": 1, "query_set_sha256": "q", "vector_manifest_sha256": "v",
                      "collections": {"demo": {"recall_at_5": 1.0}}, "aggregate": {"recall_at_5": 1.0},
                      "queries": [], "failures": []}
            report_path, baseline_path = root / "nested/report.json", root / "baseline.json"
            write_report(report_path, report)
            write_baseline(baseline_path, report)
            self.assertEqual(json.loads(report_path.read_text(encoding="utf-8"))["failures"], [])
            baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
            self.assertNotIn("queries", baseline)
            self.assertEqual(baseline["collections"], report["collections"])

    def test_cli_strict_regression_exit_code(self):
        with tempfile.TemporaryDirectory() as td:
            docs, queries, vectors = self._fixture(Path(td))
            output = Path(td) / "report.json"
            with patch("evaluate_retrieval.query_search_index", return_value={"results": []}):
                code = main(["--queries", str(queries), "--vectors", str(vectors), "--topic", "demo",
                             "--docs-dir", str(docs), "--output", str(output), "--strict",
                             "--min-recall-at-5", "0.95"])
            self.assertEqual(code, 1)
            self.assertTrue(output.is_file())

    def test_cli_rejects_topic_scoped_baseline_recording(self):
        with tempfile.TemporaryDirectory() as td:
            docs, queries, vectors = self._fixture(Path(td))
            code = main(["--queries", str(queries), "--vectors", str(vectors),
                         "--topic", "demo", "--output", str(Path(td) / "report.json"),
                         "--baseline", str(Path(td) / "baseline.json"), "--record-baseline"])
            self.assertEqual(code, 2)

    def test_cli_rejects_nonfinite_regression_threshold(self):
        code = main([
            "--queries", "missing.jsonl", "--vectors", "missing.json",
            "--all", "--output", "unused.json", "--max-regression", "nan",
        ])
        self.assertEqual(code, 2)


if __name__ == "__main__":
    unittest.main()
