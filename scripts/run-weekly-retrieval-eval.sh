#!/bin/bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd -P)"
RESULTS="$ROOT/pipeline/eval/results"
mkdir -p "$RESULTS"

if [[ -n "${PAPER_CURATION_PYTHON:-}" ]]; then
  PYTHON="$PAPER_CURATION_PYTHON"
elif [[ -x /opt/homebrew/Caskroom/miniconda/base/envs/py312/bin/python ]]; then
  PYTHON=/opt/homebrew/Caskroom/miniconda/base/envs/py312/bin/python
elif command -v python3.12 >/dev/null 2>&1; then
  PYTHON="$(command -v python3.12)"
elif [[ -x /opt/homebrew/bin/python3 ]]; then
  PYTHON=/opt/homebrew/bin/python3
elif command -v python3 >/dev/null 2>&1; then
  PYTHON="$(command -v python3)"
else
  echo "retrieval evaluation: Python 3.10+ not found; set PAPER_CURATION_PYTHON" >&2
  exit 2
fi

if [[ ! -x "$PYTHON" ]] || ! "$PYTHON" -c 'import sys; raise SystemExit(sys.version_info < (3, 10))'; then
  echo "retrieval evaluation: $PYTHON is not an executable Python 3.10+" >&2
  exit 2
fi

exec "$PYTHON" "$ROOT/pipeline/evaluate_retrieval.py" \
  --queries "$ROOT/pipeline/eval/retrieval_queries.jsonl" \
  --vectors "$ROOT/pipeline/eval/retrieval_query_vectors.json" \
  --all \
  --baseline "$ROOT/pipeline/eval/retrieval_baseline.json" \
  --min-recall-at-5 0 \
  --max-regression 0.025 \
  --strict \
  --output "$RESULTS/weekly-latest.json" \
  --failures "$RESULTS/weekly-failures.json"
