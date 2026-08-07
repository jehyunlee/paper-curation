#!/usr/bin/env python3
"""Synchronize the local SQLite bibliography DB with the Mac mini canonical copy.

The DB is intentionally kept on each machine's local filesystem. Google Drive is
not used as a live SQLite volume because its placeholder/sync layer can produce
SQLite disk-I/O errors. The Mac mini is the canonical transport endpoint.
"""
from __future__ import annotations

import argparse
import os
import shutil
import socket
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCAL_DB = ROOT / ".cache" / "bibliography.sqlite3"
REMOTE_HOST = os.environ.get("PAPER_CURATION_DB_HOST", "macmini-cf")
REMOTE_DB = os.environ.get(
    "PAPER_CURATION_DB_REMOTE",
    "/Users/jehyunlee/Documents/paper-curation/.cache/bibliography.sqlite3",
)


def is_macmini() -> bool:
    name = socket.gethostname().lower()
    return "macmini" in name or name.startswith("jehyun-macmini")


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def pull() -> None:
    LOCAL_DB.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(prefix="bibliography.", suffix=".sqlite3", dir=LOCAL_DB.parent, delete=False) as f:
        tmp = Path(f.name)
    try:
        run(["scp", "-q", REMOTE_HOST + ":" + REMOTE_DB, str(tmp)])
        os.replace(tmp, LOCAL_DB)
        print(f"pulled {REMOTE_HOST}:{REMOTE_DB} -> {LOCAL_DB}")
    finally:
        tmp.unlink(missing_ok=True)


def push() -> None:
    if not LOCAL_DB.exists():
        raise FileNotFoundError(LOCAL_DB)
    remote_tmp = REMOTE_DB + ".tmp"
    run(["scp", "-q", str(LOCAL_DB), REMOTE_HOST + ":" + remote_tmp])
    run(["ssh", REMOTE_HOST, "mv", remote_tmp, REMOTE_DB])
    print(f"pushed {LOCAL_DB} -> {REMOTE_HOST}:{REMOTE_DB}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--pull", action="store_true")
    mode.add_argument("--push", action="store_true")
    mode.add_argument("--status", action="store_true")
    args = ap.parse_args()
    if is_macmini():
        print("Mac mini detected: local DB is canonical; no remote transfer needed.")
        return 0
    if args.pull:
        pull()
    elif args.push:
        push()
    else:
        print(f"local={LOCAL_DB} exists={LOCAL_DB.exists()}")
        print(f"remote={REMOTE_HOST}:{REMOTE_DB}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
