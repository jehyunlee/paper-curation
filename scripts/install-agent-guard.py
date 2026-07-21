#!/usr/bin/env python3
"""Install and wire the source-controlled Claude PreToolUse guard."""
from __future__ import annotations

import json
import shutil
import stat
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOME = Path.home()
SETTINGS = HOME / ".claude/settings.json"
SOURCE = ROOT / "scripts/claude_guard.py"
DEST = HOME / ".claude/hooks/guard.py"
COMMAND = 'python3 "$HOME/.claude/hooks/guard.py"'
MATCHER = "Bash|Write|Edit|MultiEdit"

DENY = [
    "Bash(git push --no-verify:*)",
    "Bash(git push --force:*)",
    "Bash(git push -f:*)",
    "Bash(git init:*)",
    "Bash(git config core.hooksPath:*)",
    "Bash(mv .git:*)",
    "Bash(rm -rf /:*)",
    "Bash(rm -rf ~:*)",
    "Bash(sudo rm -rf:*)",
    "Bash(chmod -x .git/hooks/pre-push:*)",
    "Bash(find ~/.ssh:*)",
    "Bash(mkfs:*)",
    "Bash(diskutil erase:*)",
    "Bash(tmutil delete:*)",
    "Read(./config.json)",
    "Read(~/.ssh/**)",
    "Write(.git/**)",
    "Edit(.git/**)",
    "Write(~/.claude/settings.json)",
    "Edit(~/.claude/settings.json)",
    "Write(~/.claude/hooks/**)",
    "Edit(~/.claude/hooks/**)",
]


def main() -> int:
    if SETTINGS.exists():
        settings = json.loads(SETTINGS.read_text(encoding="utf-8"))
    else:
        settings = {}

    # Dangerous-mode bypass must stay absent. Do not create a stale settings
    # backup that can silently restore it later; git tracks the installer/source.
    settings.pop("skipDangerousModePermissionPrompt", None)

    permissions = settings.setdefault("permissions", {})
    existing = permissions.get("deny", [])
    permissions["deny"] = list(dict.fromkeys([*existing, *DENY]))

    hooks = settings.setdefault("hooks", {})
    pre = hooks.setdefault("PreToolUse", [])
    wanted = {"matcher": MATCHER, "hooks": [{"type": "command", "command": COMMAND}]}
    # Replace prior entries that invoke this guard; retain unrelated user hooks.
    pre[:] = [entry for entry in pre
              if COMMAND not in json.dumps(entry, ensure_ascii=False)]
    pre.append(wanted)

    DEST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SOURCE, DEST)
    DEST.chmod(DEST.stat().st_mode | stat.S_IXUSR)
    SETTINGS.parent.mkdir(parents=True, exist_ok=True)
    SETTINGS.write_text(json.dumps(settings, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8")
    SETTINGS.chmod(0o600)

    assert DEST.read_bytes() == SOURCE.read_bytes()
    verify = json.loads(SETTINGS.read_text(encoding="utf-8"))
    assert "skipDangerousModePermissionPrompt" not in verify
    assert wanted in verify["hooks"]["PreToolUse"]
    assert all(rule in verify["permissions"]["deny"] for rule in DENY)
    print(f"Installed + verified: {DEST}")
    print(f"Hardened: {SETTINGS} ({len(verify['permissions']['deny'])} deny rules)")
    print("Restart Claude Code to load the updated permissions/hooks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
