#!/usr/bin/env python3
"""Scan git objects that a push would introduce for credential material.

Unlike patch/diff scanners, this reads raw commit/tag/blob objects through
`git cat-file --batch`. Therefore merge-resolution content, `-diff` paths,
binary/NUL blobs, and annotated-tag messages are all inspected.

Input (default): pre-push ref lines on stdin:
    <local-ref> <local-oid> <remote-ref> <remote-oid>
New refs are enumerated with `rev-list <oid> --not --remotes`; updates use
`rev-list <local> ^<remote>`. The local ref object itself is always included so
annotated tag messages are scanned. With no stdin, HEAD objects not on any
remote are scanned (safe manual fallback).
"""
from __future__ import annotations

import argparse
import base64
import binascii
import re
import subprocess
import sys
import threading
from collections.abc import Iterable

ZERO_RE = re.compile(r"^0+$")
RAW_PATTERNS = (
    ("Anthropic/OpenAI", re.compile(rb"sk-(?:ant|proj)-[A-Za-z0-9_-]{20,}")),
    ("AWS access key", re.compile(rb"AKIA[0-9A-Z]{16}")),
    ("GitHub token", re.compile(rb"gh[pousr]_[A-Za-z0-9]{20,}")),
    ("Google API key", re.compile(rb"AIza[0-9A-Za-z_-]{35}")),
)
BASE64_TOKEN = re.compile(rb"(?<![A-Za-z0-9+/=])[A-Za-z0-9+/]{24,}={0,2}(?![A-Za-z0-9+/=])")
WHITESPACE = re.compile(rb"\s+")


def git(*args: str, input_data: bytes | None = None) -> bytes:
    proc = subprocess.run(
        ["git", *args], input=input_data, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, check=False)
    if proc.returncode:
        raise RuntimeError(proc.stderr.decode("utf-8", "replace").strip())
    return proc.stdout


def rev_objects(args: list[str]) -> set[str]:
    out = git("rev-list", "--objects", "--no-object-names", *args)
    return {line.decode("ascii") for line in out.splitlines() if line}


def pushed_objects(lines: Iterable[str]) -> set[str]:
    objects: set[str] = set()
    refs_seen = 0
    for line in lines:
        fields = line.split()
        if len(fields) != 4:
            continue
        _local_ref, local_oid, _remote_ref, remote_oid = fields
        refs_seen += 1
        if ZERO_RE.fullmatch(local_oid):  # deletion
            continue
        objects.add(local_oid)  # annotated tag object / tip commit itself
        if ZERO_RE.fullmatch(remote_oid):
            objects.update(rev_objects([local_oid, "--not", "--remotes"]))
        else:
            objects.update(rev_objects([local_oid, f"^{remote_oid}"]))
    if refs_seen == 0:
        objects.add(git("rev-parse", "HEAD").decode().strip())
        objects.update(rev_objects(["HEAD", "--not", "--remotes"]))
    return objects


def all_reachable_objects() -> set[str]:
    # CI mode: inspect the complete current snapshot independent of diff attrs
    # or binary status, plus HEAD and annotated-tag objects/messages.
    objects = {git("rev-parse", "HEAD").decode().strip()}
    out = git("ls-tree", "-r", "-z", "--format=%(objectname)", "HEAD")
    objects.update(x.decode("ascii") for x in out.split(b"\0") if x)
    tags = git("for-each-ref", "--format=%(objectname)", "refs/tags")
    objects.update(x.decode("ascii") for x in tags.splitlines() if x)
    return objects


def findings(data: bytes) -> set[str]:
    found = {name for name, pattern in RAW_PATTERNS if pattern.search(data)}

    # Catch keys split across whitespace/newlines without changing the object.
    compact = WHITESPACE.sub(b"", data)
    found.update(name + " (whitespace-split)"
                 for name, pattern in RAW_PATTERNS if pattern.search(compact))

    # Catch a key stored as a single standard-base64 token. Decode only
    # plausible tokens; malformed candidates are ignored.
    for token in BASE64_TOKEN.findall(data):
        try:
            decoded = base64.b64decode(token, validate=True)
        except (binascii.Error, ValueError):
            continue
        found.update(name + " (base64)"
                     for name, pattern in RAW_PATTERNS if pattern.search(decoded))
    return found


def scan_objects(oids: set[str]) -> list[tuple[str, str, set[str]]]:
    if not oids:
        return []
    proc = subprocess.Popen(
        ["git", "cat-file", "--batch"], stdin=subprocess.PIPE,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert proc.stdin is not None and proc.stdout is not None
    ordered = sorted(oids)

    # Feed stdin concurrently while consuming stdout. Writing every OID first
    # can deadlock once cat-file fills its stdout pipe.
    def feed() -> None:
        try:
            proc.stdin.write("".join(f"{oid}\n" for oid in ordered).encode("ascii"))
            proc.stdin.close()
        except BrokenPipeError:
            pass

    writer = threading.Thread(target=feed, daemon=True)
    writer.start()

    hits: list[tuple[str, str, set[str]]] = []
    for _expected in ordered:
        header = proc.stdout.readline().decode("ascii", "replace").strip().split()
        if len(header) < 3 or header[1] == "missing":
            continue
        oid, obj_type, size_s = header[:3]
        size = int(size_s)
        data = proc.stdout.read(size)
        proc.stdout.read(1)  # batch separator newline
        matched = findings(data)
        if matched:
            hits.append((oid, obj_type, matched))
    writer.join()
    rc = proc.wait()
    if rc:
        err = (proc.stderr.read() if proc.stderr else b"").decode("utf-8", "replace")
        raise RuntimeError(err.strip() or f"git cat-file exited {rc}")
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan raw pushed git objects for secrets")
    parser.add_argument("--all", action="store_true",
                        help="scan HEAD snapshot and annotated-tag objects")
    args = parser.parse_args()
    try:
        oids = all_reachable_objects() if args.all else pushed_objects(sys.stdin)
        hits = scan_objects(oids)
    except Exception as exc:
        print(f"[secret-scan] ERROR: {exc}", file=sys.stderr)
        return 2  # scanner failures block the push (fail closed)

    if hits:
        print("[secret-scan] credential material found — refusing operation", file=sys.stderr)
        for oid, obj_type, names in hits[:20]:
            print(f"  {oid[:12]} {obj_type}: {', '.join(sorted(names))}", file=sys.stderr)
        print("Remove the secret from git history and rotate it before retrying.", file=sys.stderr)
        return 1
    print(f"[secret-scan] ✓ scanned {len(oids)} raw git objects; no credentials")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
