#!/usr/bin/env python3
"""Acquire and build every input the affiliation normaliser needs.

Institution naming depends on three artifacts that live outside the repository:

1. the ROR data dump (~35 MB zip → 305 MB JSON) from Zenodo,
2. the SQLite lookup index projected from that dump,
3. `dict_afgroupname_confident.json`, the operator-curated Scopus group table.

All three sit under `.cache/`, which is gitignored, so a clean checkout or a
wiped cache silently loses institution normalisation: `build_bibliography_db.py`
prints one warning and carries on with raw PDF strings. This script makes the
acquisition reproducible and idempotent — run it once per machine, and again
only when a new ROR release is wanted.

    python pipeline/setup_affiliation_sources.py            # ensure everything
    python pipeline/setup_affiliation_sources.py --check     # report, change nothing
    python pipeline/setup_affiliation_sources.py --refresh-ror  # pull a new release
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

ROR_DIR = ROOT / ".cache" / "ror"
CURATED_DIR = ROOT / ".cache" / "affiliation"
CURATED_NAME = "dict_afgroupname_confident.json"

ZENODO_COMMUNITY = "https://zenodo.org/api/records?communities=ror-data&sort=newest&size=1"

# The curated Scopus group table is resolved by `lib.affiliation_groups` across
# three layers: PAPER_CURATION_AFGROUP_DICT (live copy), pipeline/data (pinned in
# the repository), .cache/affiliation (staged). This step only has to make sure
# at least one layer exists, and it reports which one won. The Google Drive path
# is the last-resort source used to stage the cache on the operator's own laptop.
CURATED_FALLBACK = str(
    Path.home() / "Library/CloudStorage/GoogleDrive-jehyun.lee@gmail.com/"
    "내 드라이브/KIER_후임자인수인계/ARI/code_copy/data_common/literature"
    / CURATED_NAME)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def latest_ror_release() -> dict:
    with urllib.request.urlopen(ZENODO_COMMUNITY, timeout=60) as response:
        payload = json.loads(response.read().decode("utf-8"))
    hits = payload.get("hits", {}).get("hits") or []
    if not hits:
        raise SystemExit("Zenodo returned no ROR release")
    record = hits[0]
    for entry in record.get("files", []):
        if entry["key"].endswith("-ror-data.zip"):
            return {"key": entry["key"], "size": entry["size"],
                    "url": entry["links"]["self"],
                    "record": str(record.get("id", ""))}
    raise SystemExit("newest ROR release has no -ror-data.zip asset")


def download(url: str, target: Path, expected_size: int) -> None:
    """Download to a temporary file and only then publish it.

    A partial download that keeps the final name is worse than no download: the
    first attempt at this dump stopped at 8 of 35 MB and looked present.
    """
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_suffix(target.suffix + ".part")
    request = urllib.request.Request(
        url, headers={"User-Agent": "paper-curation/1.0 (affiliation setup)"})
    with urllib.request.urlopen(request, timeout=300) as response, \
            temporary.open("wb") as handle:
        shutil.copyfileobj(response, handle, length=1 << 20)
    actual = temporary.stat().st_size
    if expected_size and actual != expected_size:
        temporary.unlink(missing_ok=True)
        raise SystemExit(
            f"incomplete download: {actual} of {expected_size} bytes")
    temporary.replace(target)


def ensure_ror_dump(refresh: bool = False) -> dict:
    from lib import ror_index
    existing = ror_index.latest_dump()
    if existing and not refresh:
        return {"status": "present", "dump": existing.name,
                "bytes": existing.stat().st_size}
    release = latest_ror_release()
    archive = ROR_DIR / release["key"]
    if not archive.exists() or archive.stat().st_size != release["size"]:
        download(release["url"], archive, release["size"])
    with zipfile.ZipFile(archive) as bundle:
        members = [n for n in bundle.namelist() if n.endswith(".json")]
        if not members:
            raise SystemExit(f"{archive.name} contains no JSON payload")
        bundle.extract(members[0], ROR_DIR)
    return {"status": "downloaded", "dump": members[0],
            "archive": archive.name, "zenodo_record": release["record"]}


def ensure_ror_index(rebuild: bool = False) -> dict:
    from lib import ror_index
    if ror_index.INDEX_PATH.exists() and not rebuild:
        import sqlite3
        conn = sqlite3.connect(f"file:{ror_index.INDEX_PATH}?mode=ro", uri=True)
        try:
            meta = dict(conn.execute("SELECT key, value FROM meta").fetchall())
        finally:
            conn.close()
        return {"status": "present", **meta}
    return {"status": "built", **ror_index.build_index()}


def ensure_curated_dict() -> dict:
    """Confirm a curated group table is reachable; stage the fallback if not.

    The pinned copy in `pipeline/data/` normally satisfies this on every machine.
    The Google Drive fallback is staged into the cache only when neither the env
    var nor the pinned copy is present.
    """
    from lib import affiliation_groups
    active = affiliation_groups.active_path()
    if active is not None:
        return {"status": "present", "path": str(active),
                "sha256": sha256_file(active)[:16],
                "entries": affiliation_groups.stats()["entries"]}
    source = Path(CURATED_FALLBACK)
    if source.is_file():
        target = affiliation_groups.CACHED_PATH
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        return {"status": "staged", "from": str(source),
                "sha256": sha256_file(target)[:16]}
    return {"status": "missing", "hint":
            "commit pipeline/data/dict_afgroupname_confident.json or set "
            "PAPER_CURATION_AFGROUP_DICT; without it 1,872 curated parent "
            "hierarchies are lost and only ROR edges remain"}


def report() -> dict:
    from lib import affiliation_groups, ror_index
    dump = ror_index.latest_dump()
    curated = affiliation_groups.active_path()
    return {
        "ror_dump": dump.name if dump else None,
        "ror_index": (str(ror_index.INDEX_PATH)
                      if ror_index.INDEX_PATH.exists() else None),
        "curated_group_dict": str(curated) if curated else None,
        "curated_entries": affiliation_groups.stats()["entries"],
        "curated_layers": [str(p) for p in affiliation_groups.curated_paths()],
        "ready": bool(ror_index.INDEX_PATH.exists()) and curated is not None,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="report what is present and exit non-zero if not ready")
    ap.add_argument("--refresh-ror", action="store_true",
                    help="download the newest ROR release and rebuild the index")
    args = ap.parse_args()

    if args.check:
        state = report()
        print(json.dumps(state, ensure_ascii=False, indent=2))
        return 0 if state["ready"] else 2

    result = {"dump": ensure_ror_dump(refresh=args.refresh_ror)}
    result["index"] = ensure_ror_index(rebuild=args.refresh_ror)
    result["curated"] = ensure_curated_dict()
    result["state"] = report()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["state"]["ready"] else 2


if __name__ == "__main__":
    from _env_guard import force_py312
    force_py312()
    raise SystemExit(main())
