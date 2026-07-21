#!/bin/sh
# Install paper-curation git hooks (idempotent + self-verifying).
# Usage: bash scripts/install-hooks.sh
#
# Run this once per clone. `pipeline/doctor.py` (check 10) reports when the
# installed hook is missing or drifted from scripts/pre-push, so it can never
# stay silently off again.

set -e
ROOT="$(git rev-parse --show-toplevel)"
HOOKS="$(git -C "$ROOT" rev-parse --git-path hooks)"
case "$HOOKS" in /*) ;; *) HOOKS="$ROOT/$HOOKS" ;; esac
SRC="$ROOT/scripts/pre-push"
DST="$HOOKS/pre-push"

mkdir -p "$HOOKS"
cp "$SRC" "$DST"
chmod +x "$DST"

# Verify: content matches source and file is executable.
if cmp -s "$SRC" "$DST" && [ -x "$DST" ]; then
    echo "Installed + verified: $DST"
    echo "  · secret-leak scan  → blocks push"
    echo "  · validate_papers   → advisory (deploy gate lives in CI)"
    echo "Override per-push with: git push --no-verify"
else
    echo "ERROR: hook install failed verification ($DST)" >&2
    exit 1
fi
