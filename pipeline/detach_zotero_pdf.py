#!/usr/bin/env python3
"""Remove a PDF attachment that holds a different paper than its parent item.

    python pipeline/detach_zotero_pdf.py --keys RM7J55RG
    python pipeline/detach_zotero_pdf.py --keys RM7J55RG --execute

A wrong `url` on an item leads to the wrong download, and the Zotmoov plugin
then renames that file after the item's own title — so the filename always
looks right and only the text tells the truth. Each PDF is read and scored
against its parent's title; one that does not contain its parent's paper is
proposed for removal.

Safety, because this deletes: the linked file is copied into
``.cache/pdf_backups/`` first, and removal is refused when any other Zotero
item or any paper in `_papers_index.json` points at the same file. Dry-run by
default.
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "pipeline"
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

INDEX = ROOT / "docs" / "papers" / "_papers_index.json"
BACKUPS = ROOT / ".cache" / "pdf_backups"
CONTAINS_FLOOR = 0.50


def _zotero(path: str, *, method: str = "GET", version: int | None = None):
    from config_loader import get_zotero_api_key, get_zotero_user_id
    url = f"https://api.zotero.org/users/{get_zotero_user_id()}/{path}"
    headers = {"Zotero-API-Key": get_zotero_api_key(),
               "Zotero-API-Version": "3"}
    if version is not None:
        headers["If-Unmodified-Since-Version"] = str(version)
    request = urllib.request.Request(url, method=method, headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        body = response.read().decode("utf-8")
        return response.status, (json.loads(body) if body.strip() else None)


def index_pdf_paths() -> dict[str, str]:
    """Which corpus paper claims which PDF, so a shared file is never cut."""
    try:
        entries = json.loads(INDEX.read_text(encoding="utf-8"))
    except OSError:
        return {}
    return {str(entry.get("pdf_path") or ""): entry.get("slug", "")
            for entry in entries if entry.get("pdf_path")}


def plan(parent_key: str) -> dict:
    from audit_zotero_pdf import pdf_first_page_text, resolve_pdf_path, tokens

    _status, parent = _zotero(f"items/{urllib.parse.quote(parent_key)}")
    parent_data = (parent or {}).get("data") or {}
    parent_title = str(parent_data.get("title") or "")
    parent_tokens = tokens(parent_title)

    _status, children = _zotero(f"items/{urllib.parse.quote(parent_key)}/children")
    claimed = index_pdf_paths()

    steps = []
    for child in children or []:
        data = child.get("data") or {}
        if data.get("contentType") != "application/pdf":
            continue
        path = resolve_pdf_path(data)
        step = {"attachment_key": child.get("key"),
                "version": child.get("version"),
                "filename": data.get("filename") or data.get("path") or "",
                "linkMode": data.get("linkMode"),
                "file": str(path) if path else None}
        text = pdf_first_page_text(path) if path else None
        if not text:
            step["action"] = "skip: file unreadable or absent"
            steps.append(step)
            continue
        overlap = (len(parent_tokens & tokens(text)) / len(parent_tokens)
                   if parent_tokens else 0.0)
        step["overlap_with_parent"] = round(overlap, 2)
        step["first_line"] = " ".join(text.split())[:110]
        if overlap >= CONTAINS_FLOOR:
            step["action"] = "keep: contains its parent's paper"
        elif path and str(path) in claimed:
            step["action"] = (f"refuse: {claimed[str(path)]} in _papers_index "
                              f"points at this file")
        else:
            step["action"] = "remove"
        steps.append(step)
    return {"parent_key": parent_key, "parent_title": parent_title,
            "attachments": steps}


def execute(step: dict) -> dict:
    result = {}
    source = Path(step["file"]) if step.get("file") else None
    if source and source.exists():
        target = BACKUPS / f"{time.strftime('%Y-%m-%d')}_detached"
        target.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target / source.name)
        result["backup"] = str(target / source.name)
    status, _ = _zotero(f"items/{urllib.parse.quote(step['attachment_key'])}",
                        method="DELETE", version=step["version"])
    result["zotero_delete_status"] = status
    if status in (204, 200) and source and source.exists():
        source.unlink()
        result["file_removed"] = str(source)
    return result


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--keys", required=True,
                    help="comma-separated parent Zotero item keys")
    ap.add_argument("--execute", action="store_true",
                    help="actually delete (default is dry-run)")
    args = ap.parse_args()

    reports = []
    for key in [k.strip() for k in args.keys.split(",") if k.strip()]:
        try:
            report = plan(key)
        except Exception as exc:
            reports.append({"parent_key": key,
                            "error": f"{type(exc).__name__}: {exc}"})
            continue
        if args.execute:
            for step in report["attachments"]:
                if step.get("action") == "remove":
                    step["result"] = execute(step)
        reports.append(report)

    print(json.dumps({"dry_run": not args.execute, "items": reports},
                     ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
