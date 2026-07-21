#!/usr/bin/env python3
"""Generate a versioned fixed-vector manifest for retrieval evaluation."""
from __future__ import annotations

import argparse
import json
import math
import os
import tempfile
import time
from pathlib import Path
from typing import Sequence

try:
    from evaluate_retrieval import (
        SCHEMA_VERSION, EvaluationError, load_query_set, load_vector_manifest,
    )
    from serve_local import EMBED_DIM, GEMINI_MODEL, gemini_embed, resolve_google_key
except ImportError:
    from pipeline.evaluate_retrieval import (
        SCHEMA_VERSION, EvaluationError, load_query_set, load_vector_manifest,
    )
    from pipeline.serve_local import EMBED_DIM, GEMINI_MODEL, gemini_embed, resolve_google_key


def _write_atomic(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent, text=True)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            json.dump(value, handle, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def generate_manifest(query_path: str | Path, output_path: str | Path, *, force: bool = False,
                      delay_seconds: float = 0.1) -> dict:
    rows, query_hash = load_query_set(query_path)
    destination = Path(output_path)
    if destination.exists() and not force:
        existing = load_vector_manifest(destination, rows, query_hash)
        if (existing.get("model") != GEMINI_MODEL
                or existing.get("dim") != EMBED_DIM
                or existing.get("task_type") != "RETRIEVAL_QUERY"):
            raise EvaluationError(
                f"vector manifest metadata is incompatible: {destination}; use --force"
            )
        return existing

    api_key = resolve_google_key()
    if not api_key:
        raise EvaluationError("GOOGLE_API_KEY/GEMINI_API_KEY is required to generate query vectors")

    vectors: dict[str, list[float]] = {}
    for position, row in enumerate(rows, 1):
        try:
            vector = [float(value) for value in gemini_embed(row["query"], api_key)]
        except (TypeError, ValueError) as exc:
            raise EvaluationError(f"query {row['id']}: embedding must contain numbers") from exc
        if len(vector) != EMBED_DIM:
            raise EvaluationError(f"query {row['id']}: expected {EMBED_DIM} dimensions, got {len(vector)}")
        if not all(math.isfinite(value) for value in vector):
            raise EvaluationError(f"query {row['id']}: embedding must contain finite numbers")
        if not any(value != 0 for value in vector):
            raise EvaluationError(f"query {row['id']}: embedding must not be all zeros")
        vectors[row["id"]] = vector
        print(f"[{position}/{len(rows)}] {row['id']}")
        if position < len(rows) and delay_seconds:
            time.sleep(delay_seconds)

    manifest = {
        "schema_version": SCHEMA_VERSION,
        "model": GEMINI_MODEL,
        "task_type": "RETRIEVAL_QUERY",
        "dim": EMBED_DIM,
        "query_set_sha256": query_hash,
        "vectors": vectors,
    }
    _write_atomic(destination, manifest)
    return manifest


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate fixed Gemini vectors for retrieval evaluation")
    parser.add_argument("--queries", required=True, help="versioned JSONL query set")
    parser.add_argument("--output", required=True, help="vector manifest output")
    parser.add_argument("--force", action="store_true", help="replace an existing manifest")
    parser.add_argument("--delay", type=float, default=0.1, help="delay between API calls in seconds")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.delay < 0:
            raise EvaluationError("--delay must be non-negative")
        generate_manifest(args.queries, args.output, force=args.force, delay_seconds=args.delay)
        return 0
    except (EvaluationError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"vector generation error: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
