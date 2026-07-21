#!/usr/bin/env python3
"""Atomically mirror retrieval-evaluation inputs outside macOS Documents TCC."""
from __future__ import annotations

import argparse
import json
import os
import shutil
import tempfile
from pathlib import Path
from typing import Sequence

LABEL = "dev.jehyunlee.paper-curation.retrieval-eval"
RUNTIME_FILES = ("evaluate_retrieval.py", "query_search_index.py")
EVAL_FILES = (
    "retrieval_queries.jsonl",
    "retrieval_queries.meta.json",
    "retrieval_query_vectors.json",
    "retrieval_baseline.json",
    "retrieval_decisions.json",
)
INDEX_FILES = ("_search_index.json", "_search_index_emb.bin")


def _collections(query_path: Path) -> list[str]:
    names: set[str] = set()
    for number, line in enumerate(query_path.read_text(encoding="utf-8").splitlines(), 1):
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"query line {number}: invalid JSON") from exc
        collection = row.get("collection") if isinstance(row, dict) else None
        if not isinstance(collection, str) or not collection:
            raise ValueError(f"query line {number}: collection must be a non-empty string")
        names.add(collection)
    if not names:
        raise ValueError("query set contains no collections")
    return sorted(names)


def refresh_snapshot(project_root: str | Path, output: str | Path) -> Path:
    root, destination = Path(project_root).resolve(), Path(output).expanduser().resolve()
    pipeline, eval_dir, docs = root / "pipeline", root / "pipeline" / "eval", root / "docs"
    collections = _collections(eval_dir / "retrieval_queries.jsonl")
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=f".{destination.name}.", dir=destination.parent))
    backup = destination.with_name(f".{destination.name}.previous")
    try:
        (temporary / "pipeline" / "eval").mkdir(parents=True)
        for name in RUNTIME_FILES:
            shutil.copy2(pipeline / name, temporary / "pipeline" / name)
        for name in EVAL_FILES:
            shutil.copy2(eval_dir / name, temporary / "pipeline" / "eval" / name)
        for collection in collections:
            target = temporary / "docs" / collection
            target.mkdir(parents=True)
            for name in INDEX_FILES:
                shutil.copy2(docs / collection / name, target / name)

        if backup.exists():
            shutil.rmtree(backup)
        if destination.exists():
            os.replace(destination, backup)
        try:
            os.replace(temporary, destination)
        except BaseException:
            if backup.exists() and not destination.exists():
                os.replace(backup, destination)
            raise
        if backup.exists():
            shutil.rmtree(backup)
    except BaseException:
        if temporary.exists():
            shutil.rmtree(temporary)
        raise
    print(f"retrieval evaluation snapshot: {len(collections)} collections -> {destination}")
    return destination


def build_parser() -> argparse.ArgumentParser:
    root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description="Refresh the TCC-safe retrieval evaluation snapshot")
    parser.add_argument("--project-root", default=str(root))
    parser.add_argument(
        "--output",
        default=str(Path.home() / "Library" / "Application Support" / "paper-curation" / "retrieval-eval"),
    )
    parser.add_argument("--if-installed", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.if_installed:
        plist = Path.home() / "Library" / "LaunchAgents" / f"{LABEL}.plist"
        if not plist.exists():
            print("retrieval evaluation snapshot: skipped (LaunchAgent not installed)")
            return 0
    try:
        refresh_snapshot(args.project_root, args.output)
        return 0
    except (OSError, ValueError) as exc:
        print(f"retrieval evaluation snapshot error: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
