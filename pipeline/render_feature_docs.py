#!/usr/bin/env python3
"""Render/check the canonical feature table without duplicating registry data."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = "<!-- GENERATED FEATURE REGISTRY: pipeline/run_feature.py --list; parent generator owns this region. -->"
END = "<!-- END GENERATED FEATURE REGISTRY -->"


def render_table(features: list[dict]) -> str:
    def cell(value) -> str:
        return str(value).replace("|", "\\|").replace("\n", " ")
    lines = ["| 모듈 | 기능 ID | 기능 / Feature | 제공자 | 전송 대상 | 비용 유형 |",
             "|---|---|---|---|---|---|"]
    for feature in features:
        lines.append("| " + " | ".join(cell(value) for value in (
            feature["group"], f"`{feature['id']}`",
            feature["label_ko"] + " / " + feature["label_en"],
            ", ".join(feature["supported_providers"]) or "none / configured sources",
            feature["credential"]["transmission"], feature["credential"]["cost_class"],
        )) + " |")
    return "\n".join(lines)


def replace_table(document: str, table: str) -> str:
    if document.count(START) != 1 or document.count(END) != 1:
        raise ValueError("feature table markers must appear exactly once")
    before, rest = document.split(START)
    _, after = rest.split(END)
    return before + START + "\n" + table + "\n" + END + after


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="update the existing setup guide")
    args = parser.parse_args(argv)
    features = json.loads((ROOT / "pipeline/features.json").read_text(encoding="utf-8"))["features"]
    path = ROOT / "docs/setup-guide.md"
    current = path.read_text(encoding="utf-8")
    expected = replace_table(current, render_table(features))
    if current == expected:
        print("Feature documentation matches the registry.")
        return 0
    if not args.write:
        print("Feature documentation is stale; run python pipeline/render_feature_docs.py --write")
        return 1
    path.write_text(expected, encoding="utf-8")
    print("Updated the feature table in docs/setup-guide.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
