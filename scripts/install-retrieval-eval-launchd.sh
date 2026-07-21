#!/bin/bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd -P)"
LABEL="dev.jehyunlee.paper-curation.retrieval-eval"
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
RESULTS="$ROOT/pipeline/eval/results"
mkdir -p "$HOME/Library/LaunchAgents" "$RESULTS"
chmod +x "$ROOT/scripts/run-weekly-retrieval-eval.sh"

/usr/bin/python3 - "$ROOT" "$PLIST" "$LABEL" <<'PY'
import plistlib
import sys
from pathlib import Path

root, destination, label = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
results = root / "pipeline" / "eval" / "results"
value = {
    "Label": label,
    "ProgramArguments": [str(root / "scripts" / "run-weekly-retrieval-eval.sh")],
    "WorkingDirectory": str(root),
    "StartCalendarInterval": {"Weekday": 1, "Hour": 3, "Minute": 17},
    "RunAtLoad": False,
    "StandardOutPath": str(results / "weekly-stdout.log"),
    "StandardErrorPath": str(results / "weekly-stderr.log"),
}
with destination.open("wb") as handle:
    plistlib.dump(value, handle, sort_keys=True)
PY

DOMAIN="gui/$UID"
launchctl bootout "$DOMAIN" "$PLIST" >/dev/null 2>&1 || true
launchctl bootstrap "$DOMAIN" "$PLIST"
launchctl enable "$DOMAIN/$LABEL"
echo "Installed $LABEL: Sundays at 03:17"
