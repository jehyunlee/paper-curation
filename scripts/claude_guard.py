#!/usr/bin/env python3
"""Claude PreToolUse guard for destructive agent actions.

The guard is source-controlled here and installed to ~/.claude/hooks/guard.py by
scripts/install-agent-guard.py. Input is Claude's tool-call JSON on stdin.
Exit 2 blocks the call; exit 0 allows it.
"""
from __future__ import annotations

import json
import os
import re
import shlex
import sys
from pathlib import Path

CATASTROPHIC = {"/", "~", "$HOME", "~/", "$HOME/", "*", ".", "./*", "/*", "~/*"}
SENSITIVE_NAMES = {"id_rsa", "id_ed25519", "id_ecdsa", "config.json"}
PROTECTED_HOOK_NAMES = {"pre-push", "scan-secrets.py", "guard.py", "claude_guard.py"}
OPERATORS = {";", "&&", "||", "|", "&"}


def _commands(line: str) -> list[list[str]]:
    """Shell-tokenize one executable line, preserving operator boundaries.

    Quoted prose remains an argument to echo/printf instead of being searched as
    raw text, avoiding blocks merely because documentation mentions `rm -rf`.
    """
    try:
        lex = shlex.shlex(line, posix=True, punctuation_chars=";&|")
        lex.whitespace_split = True
        lex.commenters = "#"
        tokens = list(lex)
    except ValueError:
        return []
    groups: list[list[str]] = [[]]
    for token in tokens:
        if token in OPERATORS or set(token) <= set(";&|"):
            if groups[-1]:
                groups.append([])
        else:
            groups[-1].append(token)
    return [g for g in groups if g]


def _executable_lines(script: str) -> list[str]:
    """Drop heredoc bodies, preserving every actual command line."""
    result: list[str] = []
    heredoc: str | None = None
    for raw in script.splitlines() or [script]:
        stripped = raw.strip()
        if heredoc is not None:
            if stripped == heredoc:
                heredoc = None
            continue
        result.append(raw)
        match = re.search(r"<<-?\s*(['\"]?)([A-Za-z_][A-Za-z0-9_]*)\1", raw)
        if match:
            heredoc = match.group(2)
    return result


def _strip_prefix(argv: list[str]) -> list[str]:
    out = list(argv)
    while out and re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", out[0]):
        out.pop(0)
    if out and Path(out[0]).name == "sudo":
        out.pop(0)
        while out and out[0].startswith("-"):
            out.pop(0)
    return out


def _inside_git_repo(cwd: str) -> bool:
    path = Path(cwd).resolve()
    return any((parent / ".git").exists() for parent in (path, *path.parents))


def _catastrophic_rm(args: list[str]) -> bool:
    flags = "".join(a[1:] for a in args if a.startswith("-") and not a.startswith("--"))
    recursive = "r" in flags.lower() or "R" in flags or "--recursive" in args
    force = "f" in flags.lower() or "--force" in args
    targets = [a for a in args if not a.startswith("-")]
    return recursive and force and any(t in CATASTROPHIC for t in targets)


def _protected_target(args: list[str]) -> bool:
    for arg in args:
        expanded = os.path.expandvars(os.path.expanduser(arg))
        parts = Path(expanded).parts
        if ".git" in parts and any(x in parts for x in ("hooks", "config")):
            return True
        if Path(expanded).name in PROTECTED_HOOK_NAMES:
            return True
        if ".claude/hooks" in expanded or expanded.endswith(".claude/settings.json"):
            return True
    return False


def _bash_reason(command: str, cwd: str) -> str | None:
    previous: list[str] | None = None
    previous_op: str | None = None
    for line in _executable_lines(command):
        # Keep operator context for remote-download | shell detection.
        try:
            lex = shlex.shlex(line, posix=True, punctuation_chars=";&|")
            lex.whitespace_split = True
            lex.commenters = "#"
            raw_tokens = list(lex)
        except ValueError:
            raw_tokens = []

        groups = _commands(line)
        group_index = 0
        for token in raw_tokens + [";"]:
            if token in OPERATORS or (token and set(token) <= set(";&|")):
                if group_index < len(groups):
                    argv = _strip_prefix(groups[group_index])
                    group_index += 1
                    if argv:
                        exe = Path(argv[0]).name
                        args = argv[1:]

                        if exe == "git" and args:
                            if args[0] == "push":
                                if "--no-verify" in args:
                                    return "git push --no-verify bypasses the secret scanner"
                                if "-f" in args or any(a == "--force" or a.startswith("--force=") for a in args):
                                    return "forced push; use --force-with-lease if necessary"
                            if args[0] == "init" and _inside_git_repo(cwd):
                                return "git init inside an existing repository"
                            if args[0] == "config" and any(a.lower() == "core.hookspath" for a in args[1:]):
                                read_flags = {"--get", "--get-all", "--get-regexp",
                                              "--get-urlmatch", "--list", "-l", "--show-origin"}
                                if not any(a in read_flags for a in args[1:]):
                                    return "changing core.hooksPath disables or redirects repository hooks"

                        if exe in {"rm", "mv", "unlink"}:
                            if any(Path(os.path.expanduser(a)).name == ".git" for a in args if not a.startswith("-")):
                                return "removing or moving the .git directory"
                            if _protected_target(args):
                                return "removing or moving a security guard/hook"
                        if exe == "rm" and _catastrophic_rm(args):
                            return "recursive rm of a catastrophic target (/ ~ $HOME . *)"

                        if exe == "chmod" and _protected_target(args):
                            mode = next((a for a in args if a.startswith("-") or re.fullmatch(r"[0-7]{3,4}", a)), "")
                            if "-x" in mode or (mode.isdigit() and int(mode[-1]) % 2 == 0):
                                return "removing execute permission from a security guard/hook"

                        if exe == "find":
                            joined = " ".join(args)
                            if any(".ssh" in a or ".claude" in a for a in args) \
                                    or any(name in joined for name in SENSITIVE_NAMES):
                                return "searching for credential or agent-control files"

                        if exe in {"mkfs", "diskutil", "dd", "tmutil"}:
                            joined = " ".join(args)
                            if exe == "mkfs" or (exe == "diskutil" and "erase" in joined) \
                                    or (exe == "dd" and "of=/dev/" in joined) \
                                    or (exe == "tmutil" and args and args[0] == "delete"):
                                return "disk or backup destruction command"

                        if previous_op == "|" and previous:
                            pexe = Path(previous[0]).name
                            if pexe in {"curl", "wget"} and exe in {"sh", "bash", "zsh"}:
                                return "piping a remote download directly into a shell"
                        previous = argv
                previous_op = token

        # Shell redirection can mutate controls without invoking Write/Edit.
        if re.search(r"(?:>|>>)\s*[^;&|]*(?:\.claude/(?:settings\.json|hooks/)|\.git/(?:hooks|config))", line):
            return "redirecting output into an agent or git guard path"
    return None


def _write_reason(tool: str, inp: dict, cwd: str) -> str | None:
    if tool not in {"Write", "Edit", "MultiEdit"}:
        return None
    raw = inp.get("file_path") or inp.get("path") or ""
    if not raw:
        return None
    expanded = Path(os.path.expandvars(os.path.expanduser(raw)))
    path = expanded.resolve() if expanded.is_absolute() else (Path(cwd) / expanded).resolve()
    home = Path.home().resolve()
    parts = path.parts
    if ".git" in parts:
        return f"writing inside a .git directory ({raw})"
    if path == home / ".claude/settings.json" or path.is_relative_to(home / ".claude/hooks"):
        return "editing the agent settings/guard would disable protection"
    if path.is_relative_to(home / ".ssh"):
        return "writing into ~/.ssh"
    return None


def evaluate(data: dict) -> str | None:
    tool = data.get("tool_name", "")
    inp = data.get("tool_input", {}) or {}
    cwd = data.get("cwd", "") or os.getcwd()
    if tool == "Bash":
        return _bash_reason(inp.get("command", "") or "", cwd)
    return _write_reason(tool, inp, cwd)


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception as exc:
        print(f"[guard] BLOCKED — invalid hook input: {exc}", file=sys.stderr)
        return 2  # fail closed: malformed input must not silently disable defense
    reason = evaluate(data)
    if reason:
        print(f"[guard] BLOCKED — {reason}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
