#!/usr/bin/env python3
"""Atomically publish a local bibliography DB into the shared Google Drive."""
from __future__ import annotations

import argparse
import os
import shutil
import time
from pathlib import Path

SHARED = Path.home() / "Library" / "CloudStorage" / "GoogleDrive-jehyun.lee@gmail.com" / "내 드라이브" / "paper-curation" / "bibliography.sqlite3"


def publish(source: Path, target: Path = SHARED) -> None:
    if not source.exists():
        raise FileNotFoundError(source)
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_name(target.name + ".tmp")
    shutil.copy2(source, tmp)
    os.replace(tmp, target)
    print(f"published {source} -> {target}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", type=Path, required=True)
    ap.add_argument("--target", type=Path, default=SHARED)
    ap.add_argument("--wait-for-pid", type=int)
    ap.add_argument("--poll", type=int, default=60)
    args = ap.parse_args()
    if args.wait_for_pid:
        while True:
            try:
                os.kill(args.wait_for_pid, 0)
            except ProcessLookupError:
                break
            except PermissionError:
                break
            time.sleep(args.poll)
    publish(args.source, args.target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
