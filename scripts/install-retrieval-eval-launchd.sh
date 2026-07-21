#!/bin/bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd -P)"
LABEL="dev.jehyunlee.paper-curation.retrieval-eval"
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
LOG_DIR="$HOME/Library/Logs/paper-curation"
mkdir -p "$HOME/Library/LaunchAgents" "$LOG_DIR"

/usr/bin/python3 - "$ROOT" "$PLIST" "$LABEL" <<'PY'
import plistlib
import sys
from pathlib import Path

root, destination, label = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
logs = Path.home() / "Library" / "Logs" / "paper-curation"
evaluation = root / "pipeline" / "evaluate_retrieval.py"
eval_dir = root / "pipeline" / "eval"
value = {
    "Label": label,
    # LaunchAgent processes cannot execute scripts from Documents under macOS
    # TCC. Launch Apple-signed Python directly, without a Documents cwd.
    "ProgramArguments": [
        "/usr/bin/python3", str(evaluation),
        "--queries", str(eval_dir / "retrieval_queries.jsonl"),
        "--vectors", str(eval_dir / "retrieval_query_vectors.json"),
        "--all",
        "--baseline", str(eval_dir / "retrieval_baseline.json"),
        "--min-recall-at-5", "0",
        "--max-regression", "0.025",
        "--strict",
        "--output", str(logs / "retrieval-weekly-latest.json"),
        "--failures", str(logs / "retrieval-weekly-failures.json"),
    ],
    "StartCalendarInterval": {"Weekday": 1, "Hour": 3, "Minute": 17},
    "RunAtLoad": False,
    "StandardOutPath": str(logs / "retrieval-weekly-stdout.log"),
    "StandardErrorPath": str(logs / "retrieval-weekly-stderr.log"),
}
with destination.open("wb") as handle:
    plistlib.dump(value, handle, sort_keys=True)
PY

DOMAIN="gui/$UID"
launchctl bootout "$DOMAIN" "$PLIST" >/dev/null 2>&1 || true
launchctl bootstrap "$DOMAIN" "$PLIST"
launchctl enable "$DOMAIN/$LABEL"
echo "Installed $LABEL: Sundays at 03:17"
