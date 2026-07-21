#!/usr/bin/env python3
"""Deterministic, offline retrieval-quality evaluator for local search indexes."""
from __future__ import annotations

import argparse
import datetime as _datetime
import hashlib
import json
import math
import os
import tempfile
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

try:  # Script execution from pipeline/ and package imports are both supported.
    from query_search_index import query_search_index
except ImportError:
    from pipeline.query_search_index import query_search_index

SCHEMA_VERSION = 1
MAX_K = 10
FAILURE_K = 5


class EvaluationError(ValueError):
    """Invalid evaluator input or local index configuration."""


def sha256_file(path: str | Path) -> str:
    """Return the SHA-256 of a file's exact bytes."""
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _read_json(path: str | Path, label: str) -> Any:
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except OSError as exc:
        raise EvaluationError(f"cannot read {label}: {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise EvaluationError(f"invalid {label} JSON: {path}: {exc.msg}") from exc


def load_query_set(path: str | Path) -> tuple[list[dict[str, Any]], str]:
    """Load and validate JSONL queries, returning rows and their byte hash."""
    query_path = Path(path)
    try:
        lines = query_path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise EvaluationError(f"cannot read query set: {path}: {exc}") from exc
    rows: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    required = {"id", "query", "collection", "relevant_slugs"}
    optional = {"language", "category", "notes"}
    for number, line in enumerate(lines, 1):
        if not line.strip():
            raise EvaluationError(f"query set line {number}: blank lines are not allowed")
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise EvaluationError(f"query set line {number}: invalid JSON: {exc.msg}") from exc
        if not isinstance(row, dict):
            raise EvaluationError(f"query set line {number}: row must be an object")
        missing = required - row.keys()
        unknown = row.keys() - required - optional
        if missing:
            raise EvaluationError(f"query set line {number}: missing required fields: {', '.join(sorted(missing))}")
        if unknown:
            raise EvaluationError(f"query set line {number}: unknown fields: {', '.join(sorted(unknown))}")
        for field in ("id", "query", "collection"):
            if not isinstance(row[field], str) or not row[field].strip():
                raise EvaluationError(f"query set line {number}: {field} must be a non-empty string")
        if row["id"] in seen_ids:
            raise EvaluationError(f"query set line {number}: duplicate id: {row['id']}")
        relevant = row["relevant_slugs"]
        if (not isinstance(relevant, list) or not relevant or
                any(not isinstance(slug, str) or not slug.strip() for slug in relevant)):
            raise EvaluationError(f"query set line {number}: relevant_slugs must be a non-empty string list")
        if len(set(relevant)) != len(relevant):
            raise EvaluationError(f"query set line {number}: relevant_slugs must not contain duplicates")
        for field in optional:
            if field in row and not isinstance(row[field], str):
                raise EvaluationError(f"query set line {number}: {field} must be a string")
        seen_ids.add(row["id"])
        rows.append(row)
    if not rows:
        raise EvaluationError("query set must contain at least one row")
    return rows, sha256_file(query_path)


def load_vector_manifest(path: str | Path, rows: Sequence[Mapping[str, Any]], query_set_sha256: str
                         ) -> dict[str, Any]:
    """Load a fixed-vector manifest and validate it against query rows."""
    manifest = _read_json(path, "vector manifest")
    if not isinstance(manifest, dict):
        raise EvaluationError("vector manifest must be an object")
    required = {"schema_version", "model", "dim", "query_set_sha256", "vectors"}
    missing = required - manifest.keys()
    if missing:
        raise EvaluationError(f"vector manifest missing fields: {', '.join(sorted(missing))}")
    if manifest["schema_version"] != SCHEMA_VERSION:
        raise EvaluationError(f"unsupported vector manifest schema_version: {manifest['schema_version']!r}")
    if not isinstance(manifest["model"], str) or not manifest["model"].strip():
        raise EvaluationError("vector manifest model must be a non-empty string")
    dim = manifest["dim"]
    if not isinstance(dim, int) or isinstance(dim, bool) or dim <= 0:
        raise EvaluationError("vector manifest dim must be a positive integer")
    if manifest["query_set_sha256"] != query_set_sha256:
        raise EvaluationError("vector manifest query_set_sha256 does not match query set")
    vectors = manifest["vectors"]
    if not isinstance(vectors, dict):
        raise EvaluationError("vector manifest vectors must be an object")
    ids = {str(row["id"]) for row in rows}
    if set(vectors) != ids:
        missing_ids, extra_ids = ids - set(vectors), set(vectors) - ids
        details = []
        if missing_ids:
            details.append("missing IDs: " + ", ".join(sorted(missing_ids)))
        if extra_ids:
            details.append("unknown IDs: " + ", ".join(sorted(extra_ids)))
        raise EvaluationError("vector manifest ID coverage mismatch (" + "; ".join(details) + ")")
    normalized: dict[str, list[float]] = {}
    for query_id, raw_vector in vectors.items():
        if not isinstance(raw_vector, list) or len(raw_vector) != dim:
            raise EvaluationError(f"vector for {query_id!r} must have dimension {dim}")
        try:
            vector = [float(value) for value in raw_vector]
        except (TypeError, ValueError) as exc:
            raise EvaluationError(f"vector for {query_id!r} must contain numbers") from exc
        if not all(math.isfinite(value) for value in vector):
            raise EvaluationError(f"vector for {query_id!r} must contain finite numbers")
        if not any(value != 0 for value in vector):
            raise EvaluationError(f"vector for {query_id!r} must not be all zeros")
        normalized[query_id] = vector
    return {**manifest, "vectors": normalized}


def collection_paper_slugs(collection: str, docs_dir: str | Path | None) -> set[str]:
    """Read a collection's paper metadata without changing the local index."""
    root = Path(docs_dir) if docs_dir is not None else Path(__file__).resolve().parent.parent / "docs"
    index_path = root / collection / "_search_index.json"
    index = _read_json(index_path, "search index")
    if not isinstance(index, dict) or not isinstance(index.get("papers"), dict):
        raise EvaluationError(f"invalid search index papers metadata: {index_path}")
    return set(index["papers"])


def validate_relevant_slugs(rows: Iterable[Mapping[str, Any]], docs_dir: str | Path | None) -> dict[str, set[str]]:
    """Ensure each expected slug exists in its collection's papers metadata."""
    available: dict[str, set[str]] = {}
    absent: list[str] = []
    for row in rows:
        collection = str(row["collection"])
        if collection not in available:
            available[collection] = collection_paper_slugs(collection, docs_dir)
        missing = sorted(set(row["relevant_slugs"]) - available[collection])
        if missing:
            absent.append(f"{row['id']} ({collection}): {', '.join(missing)}")
    if absent:
        raise EvaluationError("expected slug absent from collection metadata: " + "; ".join(absent))
    return available


def evaluate_rows(rows: Sequence[Mapping[str, Any]], vectors: Mapping[str, Sequence[float]], *,
                  docs_dir: str | Path | None = None, max_k: int = MAX_K) -> list[dict[str, Any]]:
    """Run each query using supplied vectors only; no embedding/network path is used."""
    if max_k < MAX_K:
        raise EvaluationError(f"max_k must be at least {MAX_K}")
    evaluations: list[dict[str, Any]] = []
    for row in rows:
        result = query_search_index(str(row["collection"]), str(row["query"]), mode="hybrid",
                                    query_vector=vectors[str(row["id"])], top_k=max_k,
                                    docs_dir=docs_dir)
        top_slugs = [str(item.get("slug", "")) for item in result.get("results", [])]
        ranks: dict[str, int | None] = {}
        for slug in row["relevant_slugs"]:
            ranks[slug] = next((rank for rank, actual in enumerate(top_slugs, 1) if actual == slug), None)
        evaluations.append({"id": row["id"], "query": row["query"], "collection": row["collection"],
                            "relevant_slugs": list(row["relevant_slugs"]), "ranks": ranks,
                            "top_slugs": top_slugs[:max_k]})
    return evaluations


def compute_metrics(evaluations: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    """Compute collection and aggregate recall/MRR metrics from evaluation rows."""
    grouped: dict[str, list[Mapping[str, Any]]] = {}
    for item in evaluations:
        grouped.setdefault(str(item["collection"]), []).append(item)

    def metrics(items: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
        count = len(items)
        recall5 = sum(sum(rank is not None and rank <= 5 for rank in item["ranks"].values()) /
                      len(item["relevant_slugs"]) for item in items) / count if count else 0.0
        recall10 = sum(sum(rank is not None and rank <= 10 for rank in item["ranks"].values()) /
                       len(item["relevant_slugs"]) for item in items) / count if count else 0.0
        mrr10 = sum(1 / min(ranks) if (ranks := [rank for rank in item["ranks"].values()
                                               if rank is not None and rank <= 10]) else 0.0
                    for item in items) / count if count else 0.0
        failures = [item for item in items
                    if any(rank is None or rank > FAILURE_K for rank in item["ranks"].values())]
        return {"query_count": count, "recall_at_5": recall5, "recall_at_10": recall10,
                "mrr_at_10": mrr10, "failure_count": len(failures)}

    return {"collections": {name: metrics(grouped[name]) for name in sorted(grouped)},
            "aggregate": metrics(evaluations)}


def build_report(evaluations: Sequence[Mapping[str, Any]], metrics: Mapping[str, Any], *,
                 query_set_sha256: str, vector_manifest_sha256: str) -> dict[str, Any]:
    failures = [{"id": item["id"], "collection": item["collection"],
                 "expected_slugs": item["relevant_slugs"], "actual_top_slugs": item["top_slugs"],
                 "ranks": item["ranks"]}
                for item in evaluations
                if any(rank is None or rank > FAILURE_K for rank in item["ranks"].values())]
    return {"schema_version": SCHEMA_VERSION,
            "timestamp": _datetime.datetime.now(_datetime.timezone.utc).isoformat().replace("+00:00", "Z"),
            "query_set_sha256": query_set_sha256, "vector_manifest_sha256": vector_manifest_sha256,
            "collections": metrics["collections"], "aggregate": metrics["aggregate"],
            "queries": list(evaluations), "failures": failures}


def write_json_atomic(path: str | Path, value: Mapping[str, Any]) -> None:
    """Atomically replace a JSON output, never exposing a partial report."""
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    descriptor, temporary = tempfile.mkstemp(prefix=f".{destination.name}.", dir=destination.parent, text=True)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, destination)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def write_report(path: str | Path, report: Mapping[str, Any]) -> None:
    write_json_atomic(path, report)


def write_baseline(path: str | Path, report: Mapping[str, Any]) -> None:
    """Write only comparable metrics and input identities, never query detail."""
    baseline = {"schema_version": SCHEMA_VERSION, "query_set_sha256": report["query_set_sha256"],
                "vector_manifest_sha256": report["vector_manifest_sha256"],
                "collections": report["collections"], "aggregate": report["aggregate"]}
    write_json_atomic(path, baseline)


def load_baseline(path: str | Path) -> dict[str, Any]:
    baseline = _read_json(path, "baseline")
    if not isinstance(baseline, dict) or not isinstance(baseline.get("collections"), dict):
        raise EvaluationError("baseline must contain collection metrics")
    return baseline


def validate_baseline_identity(baseline: Mapping[str, Any], report: Mapping[str, Any]) -> None:
    """Reject comparisons across different query sets or fixed-vector manifests."""
    for field in ("query_set_sha256", "vector_manifest_sha256"):
        if baseline.get(field) != report.get(field):
            raise EvaluationError(f"baseline {field} does not match current evaluation")


def validate_baseline_metrics(baseline: Mapping[str, Any], report: Mapping[str, Any]) -> None:
    """Require a finite recall comparator for every evaluated collection."""
    prior = baseline.get("collections")
    if not isinstance(prior, dict):
        raise EvaluationError("baseline collections must be an object")
    for collection in report["collections"]:
        metrics = prior.get(collection)
        recall = metrics.get("recall_at_5") if isinstance(metrics, dict) else None
        if (not isinstance(recall, (int, float)) or isinstance(recall, bool)
                or not math.isfinite(recall) or not 0 <= recall <= 1):
            raise EvaluationError(
                f"baseline missing valid recall_at_5 for evaluated collection: {collection}"
            )


def strict_failures(report: Mapping[str, Any], baseline: Mapping[str, Any] | None, *,
                    min_recall_at_5: float, max_regression: float) -> list[str]:
    problems: list[str] = []
    prior = baseline.get("collections", {}) if baseline else {}
    for collection, metrics in report["collections"].items():
        recall = metrics["recall_at_5"]
        if recall < min_recall_at_5:
            problems.append(f"{collection}: recall_at_5 {recall:.6f} < {min_recall_at_5:.6f}")
        old = prior.get(collection)
        if isinstance(old, dict) and isinstance(old.get("recall_at_5"), (int, float)):
            if recall < old["recall_at_5"] - max_regression:
                problems.append(f"{collection}: recall_at_5 regression {old['recall_at_5'] - recall:.6f} > {max_regression:.6f}")
    return problems


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate local search-index retrieval with fixed vectors")
    parser.add_argument("--queries", required=True, help="JSONL query set")
    parser.add_argument("--vectors", required=True, help="fixed-vector JSON manifest")
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--topic", help="evaluate rows for this collection")
    selection.add_argument("--all", action="store_true", help="evaluate all query rows")
    parser.add_argument("--docs-dir", help="docs directory containing collection indexes")
    parser.add_argument("--output", required=True, help="JSON report output")
    parser.add_argument("--failures", help="optional failures-only JSON output")
    parser.add_argument("--baseline", help="baseline JSON for regression comparison")
    parser.add_argument("--strict", action="store_true", help="return failure for quality gate violations")
    parser.add_argument("--record-baseline", action="store_true", help="write compact baseline to --baseline")
    parser.add_argument("--min-recall-at-5", type=float, default=0.95)
    parser.add_argument("--max-regression", type=float, default=0.025)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if (not 0 <= args.min_recall_at_5 <= 1
                or not math.isfinite(args.max_regression) or args.max_regression < 0):
            raise EvaluationError(
                "min-recall-at-5 must be 0..1 and max-regression must be finite and non-negative"
            )
        if args.record_baseline and not args.baseline:
            raise EvaluationError("--record-baseline requires --baseline")
        if args.record_baseline and args.topic:
            raise EvaluationError(
                "--record-baseline requires --all; topic baselines may not replace the shared baseline"
            )
        all_rows, query_hash = load_query_set(args.queries)
        manifest = load_vector_manifest(args.vectors, all_rows, query_hash)
        rows = all_rows
        if args.topic:
            rows = [row for row in all_rows if row["collection"] == args.topic]
            if not rows:
                raise EvaluationError(f"no query rows for topic: {args.topic}")
        # Manifest hashes the complete source file; evaluation can use a selected subset.
        selected_vectors = {row["id"]: manifest["vectors"][row["id"]] for row in rows}
        missing_metadata: list[str] = []
        available: dict[str, set[str]] = {}
        for row in rows:
            collection = row["collection"]
            available.setdefault(collection, collection_paper_slugs(collection, args.docs_dir))
            missing = sorted(set(row["relevant_slugs"]) - available[collection])
            if missing:
                missing_metadata.append(f"{row['id']} ({collection}): {', '.join(missing)}")
        evaluations = evaluate_rows(rows, selected_vectors, docs_dir=args.docs_dir)
        metrics = compute_metrics(evaluations)
        report = build_report(evaluations, metrics, query_set_sha256=query_hash,
                              vector_manifest_sha256=sha256_file(args.vectors))
        write_report(args.output, report)
        aggregate = report["aggregate"]
        print(
            "retrieval evaluation: "
            f"{aggregate['query_count']} queries, "
            f"recall@5={aggregate['recall_at_5']:.3f}, "
            f"recall@10={aggregate['recall_at_10']:.3f}, "
            f"mrr@10={aggregate['mrr_at_10']:.3f}, "
            f"failures={aggregate['failure_count']}"
        )
        if args.failures:
            write_json_atomic(args.failures, {"schema_version": SCHEMA_VERSION, "failures": report["failures"]})
        if args.record_baseline:
            write_baseline(args.baseline, report)
        baseline = load_baseline(args.baseline) if args.baseline and not args.record_baseline else None
        if baseline:
            validate_baseline_identity(baseline, report)
            validate_baseline_metrics(baseline, report)
        problems = strict_failures(report, baseline, min_recall_at_5=args.min_recall_at_5,
                                   max_regression=args.max_regression)
        problems.extend("expected slug absent from collection metadata: " + item
                        for item in missing_metadata)
        if args.strict and problems:
            for problem in problems:
                print(f"quality gate failed: {problem}")
            return 1
        return 0
    except (EvaluationError, OSError, ValueError) as exc:
        print(f"evaluation configuration error: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
