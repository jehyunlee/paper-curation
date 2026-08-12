#!/usr/bin/env python3
"""Fill the two caches that let a build skip Zotero: pdf_path and the sidecar.

    python pipeline/backfill_paper_cache.py                  # dry-run
    python pipeline/backfill_paper_cache.py --execute
    python pipeline/backfill_paper_cache.py --execute --verify-content

Both come from one page-through of the library, so they are done together.

`_papers_index.json.pdf_path` — `locate_pdf` falls back to matching a PDF by
title when this is empty, and that fuzzy path is wrong often enough to matter:
it answers `10737_latent_dirichlet_allocation` with a file called
`Luo et al._2024_Parallel inference for cross…`. This backfill never guesses.
A paper's PDF is the attachment hanging off its own Zotero item and nothing
else, so a paper with no ID-linked attachment is left empty rather than filled
with a lookalike.

`bibliography.json` — the review-time sidecar. Without one,
`build_bibliography_db.py` pages the whole library on every build (~200 s,
and its failure mode is a silently missing `zotero_item_key`). paper-curio,
which now does most of the registering, never writes one, and the main
pipeline only writes it for papers it reviews itself: 9 of 4,196 have it. The
builder reads only `zotero` and `authors` out of it, so this writes exactly
those, with `text_md_sha256` recorded so a stale sidecar is refused rather
than trusted.

`--verify-content` additionally opens each PDF and drops a pdf_path whose text
does not contain its paper's title — slower, and orthogonal: a wrong file
attached to the right item is a Zotero problem, for
`inspect_zotero_item.py --check-pdf` and `detach_zotero_pdf.py`.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sqlite3
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "pipeline"
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

PAPERS_DIR = ROOT / "docs" / "papers"
INDEX = PAPERS_DIR / "_papers_index.json"
DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"
SIDECAR_NAME = "bibliography.json"
SIDECAR_SCHEMA = "bibliography-sidecar-1"
TITLE_OVERLAP_FLOOR = 0.30


def fetch_library() -> list[dict]:
    """Every item in the library, attachments included.

    `build_bibliography_db.fetch_zotero_items` reads `/items/top`, which omits
    attachments — and the attachment is the only authoritative statement of
    which file belongs to which paper.
    """
    from config_loader import get_zotero_api_key, get_zotero_user_id
    key, user = get_zotero_api_key(), get_zotero_user_id()
    out, start = [], 0
    while True:
        url = (f"https://api.zotero.org/users/{user}/items"
               f"?format=json&limit=100&start={start}")
        request = urllib.request.Request(
            url, headers={"Zotero-API-Key": key, "Zotero-API-Version": "3"})
        for attempt in range(4):
            try:
                with urllib.request.urlopen(request, timeout=40) as response:
                    batch = json.loads(response.read().decode("utf-8"))
                break
            except Exception:
                if attempt == 3:
                    raise
                time.sleep(2 * (attempt + 1))
        if not batch:
            break
        out.extend(batch)
        start += len(batch)
        print(f"  [zotero] {start} items", file=sys.stderr, flush=True)
    return out


def split_library(items: list[dict]) -> tuple[dict, dict]:
    """(item key -> data, parent key -> [pdf attachment data])."""
    parents, attachments = {}, {}
    for item in items:
        data = item.get("data") or {}
        key = data.get("key") or item.get("key") or ""
        if not key:
            continue
        if data.get("itemType") == "attachment":
            parent = data.get("parentItem") or ""
            if parent and data.get("contentType") == "application/pdf":
                attachments.setdefault(parent, []).append(data)
        else:
            parents[key] = data
    return parents, attachments


def resolve_attachment(data: dict) -> Path | None:
    from audit_zotero_pdf import resolve_pdf_path
    try:
        path = resolve_pdf_path(data)
    except Exception:
        return None
    return path if path and Path(path).exists() else None


def sidecar_payload(zdata: dict, directory: Path) -> dict:
    creators = [
        (f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
         or str(c.get("name") or "")).strip()
        for c in zdata.get("creators") or []
        if c.get("creatorType") == "author"
    ]
    text = directory / "text.md"
    return {
        "schema": SIDECAR_SCHEMA,
        "zotero": zdata,
        "authors": [name for name in creators if name],
        # Pins the record to the text it was captured beside; `load_sidecar`
        # refuses the sidecar once text.md changes.
        "text_md_sha256": (hashlib.sha256(text.read_bytes()).hexdigest()
                           if text.exists() else ""),
        "affiliations": [],
        "captured_by": "backfill_paper_cache",
        "captured_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }


def content_matches(path: Path, title: str) -> bool:
    """Whether a PDF's text supports being this paper. Silence is not dissent.

    Small's 1973 co-citation paper is a scan with no text layer, so it scored
    0.0 against its own title and its correct file was refused. A PDF yielding
    too few words to judge is unprovable, not wrong — the same 30-word floor
    `audit_zotero_pdf.audit_item` requires before it will call a mismatch.
    """
    from audit_zotero_pdf import pdf_first_page_text, tokens
    text = pdf_first_page_text(path)
    if not text or len(re.findall(r"[A-Za-z]{3,}", text)) < 30:
        return True          # unreadable or textless proves nothing
    wanted = tokens(title)
    if not wanted:
        return True
    return len(wanted & tokens(text)) / len(wanted) >= TITLE_OVERLAP_FLOOR


def keys_by_slug(db: Path) -> dict[str, str]:
    if not db.exists():
        return {}
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    try:
        return {slug: key for slug, key in conn.execute(
            "SELECT slug, zotero_item_key FROM papers WHERE zotero_item_key<>''")}
    finally:
        conn.close()


def run(db: Path, *, execute: bool, verify: bool) -> dict:
    entries = json.loads(INDEX.read_text(encoding="utf-8"))
    by_slug = keys_by_slug(db)
    parents, attachments = split_library(fetch_library())

    report = {"papers": len(entries), "zotero_items": len(parents),
              "pdf_path_filled": 0, "pdf_path_already": 0,
              "no_zotero_key": 0, "no_attachment": 0, "file_missing": 0,
              "content_rejected": 0, "sidecars_written": 0,
              "sidecar_already": 0, "rejected": []}
    changed = False

    for entry in entries:
        slug = entry.get("slug", "")
        directory = PAPERS_DIR / slug
        key = entry.get("zotero_key") or by_slug.get(slug, "")
        if not key or key not in parents:
            report["no_zotero_key"] += 1
            continue
        zdata = parents[key]

        if entry.get("pdf_path") and Path(entry["pdf_path"]).exists():
            report["pdf_path_already"] += 1
        else:
            paths = [p for p in
                     (resolve_attachment(a) for a in attachments.get(key, []))
                     if p]
            if not attachments.get(key):
                report["no_attachment"] += 1
            elif not paths:
                report["file_missing"] += 1
            else:
                path = paths[0]
                if verify and not content_matches(path, str(zdata.get("title") or "")):
                    report["content_rejected"] += 1
                    # Named, not just counted: a file that is a different paper
                    # is a Zotero problem someone has to look at.
                    report["rejected"].append(
                        {"slug": slug, "zotero_item_key": key,
                         "file": path.name})
                else:
                    entry["pdf_path"] = str(path)
                    report["pdf_path_filled"] += 1
                    changed = True

        if (directory / SIDECAR_NAME).exists():
            report["sidecar_already"] += 1
        elif directory.is_dir():
            if execute:
                payload = sidecar_payload(zdata, directory)
                tmp = directory / (SIDECAR_NAME + ".tmp")
                tmp.write_text(
                    json.dumps(payload, ensure_ascii=False, indent=1),
                    encoding="utf-8")
                os.replace(tmp, directory / SIDECAR_NAME)
            report["sidecars_written"] += 1

    if execute and changed:
        # The index has one canonical writer; reusing it keeps the formatting
        # and the fsync/replace discipline identical to build_papers_index.py.
        from lib.atomic_io import atomic_write_json
        atomic_write_json(str(INDEX), entries)
    report["index_written"] = bool(execute and changed)
    return report


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--execute", action="store_true",
                    help="write (default is dry-run)")
    ap.add_argument("--verify-content", action="store_true",
                    help="open each PDF and reject one that is a different paper")
    args = ap.parse_args()

    report = run(args.db, execute=args.execute, verify=args.verify_content)
    print(json.dumps({"dry_run": not args.execute, **report},
                     ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
