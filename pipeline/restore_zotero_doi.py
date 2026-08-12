#!/usr/bin/env python3
"""Restore a Zotero item's DOI when a patch wrote a foreign one into it.

    python pipeline/restore_zotero_doi.py --keys RM7J55RG,ZA7W3PFQ
    python pipeline/restore_zotero_doi.py --keys RM7J55RG --execute

`pdf_bibliography` takes the first DOI in its window and the window reaches
the reference list, so a paper citing another paper adopted the other paper's
DOI; with no DOI of its own in Zotero to outrank it, `patch_zotero` wrote it
into the library. Two items were damaged that way — the DOI and the url, and
nothing else.

The correct DOI is recovered from Crossref by searching the item's *own*
title, and accepted only when the returned record agrees with the item on
title and first author. Dry-run by default: nothing is written without
``--execute``.
"""
from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "pipeline"
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

MAILTO = "jehyun.lee@gmail.com"
TITLE_FLOOR = 0.90


def _norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (value or "").lower()).strip()


def _similar(left: str, right: str) -> float:
    return difflib.SequenceMatcher(None, _norm(left), _norm(right)).ratio()


def _zotero_request(path: str, *, data=None, method="GET", version=None):
    from config_loader import get_zotero_api_key, get_zotero_user_id
    url = f"https://api.zotero.org/users/{get_zotero_user_id()}/{path}"
    headers = {"Zotero-API-Key": get_zotero_api_key(),
               "Zotero-API-Version": "3"}
    if data is not None:
        headers["Content-Type"] = "application/json"
        headers["If-Unmodified-Since-Version"] = str(version)
    request = urllib.request.Request(
        url, data=data, method=method, headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        body = response.read().decode("utf-8")
        return response.status, (json.loads(body) if body.strip() else None)


def crossref_by_title(title: str, authors: list[str]) -> dict:
    """The Crossref record whose title and first author match this item."""
    query = urllib.parse.urlencode(
        {"query.bibliographic": title, "rows": 5, "mailto": MAILTO})
    request = urllib.request.Request(
        "https://api.crossref.org/works?" + query,
        headers={"User-Agent": f"paper-curation/1.0 (mailto:{MAILTO})"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            items = json.loads(response.read())["message"]["items"]
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}"}

    first_author = _norm(authors[0].split()[-1]) if authors else ""
    for item in items:
        candidate = (item.get("title") or [""])[0]
        score = _similar(title, candidate)
        if score < TITLE_FLOOR:
            continue
        families = [_norm(a.get("family", "")) for a in item.get("author", [])]
        if first_author and first_author not in families:
            continue
        return {"doi": item.get("DOI", ""), "title": candidate,
                "journal": (item.get("container-title") or [""])[0],
                "similarity": round(score, 3),
                "authors": [f"{a.get('given', '')} {a.get('family', '')}".strip()
                            for a in item.get("author", [])][:4]}
    return {"error": "no Crossref record agreed with the item"}


def crossref_by_doi(doi: str) -> dict:
    """What a DOI is registered to, so a foreign one can be proven foreign."""
    if not doi:
        return {}
    request = urllib.request.Request(
        "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/"),
        headers={"User-Agent": f"paper-curation/1.0 (mailto:{MAILTO})"})
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            message = json.loads(response.read())["message"]
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}"}
    return {"title": (message.get("title") or [""])[0],
            "journal": (message.get("container-title") or [""])[0]}


def arxiv_id(data: dict) -> str:
    match = re.search(
        r"arXiv:\s*(\d{4}\.\d{4,5})",
        f"{data.get('extra', '')} {data.get('archiveID', '')}", re.I)
    return match.group(1) if match else ""


def plan(key: str) -> dict:
    _status, item = _zotero_request(f"items/{urllib.parse.quote(key)}")
    data = (item or {}).get("data") or {}
    title = str(data.get("title") or "")
    current = str(data.get("DOI") or "")
    authors = [f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
               for c in data.get("creators") or []
               if c.get("creatorType") == "author"]
    found = crossref_by_title(title, authors)
    registered = crossref_by_doi(current)
    step = {"key": key, "version": item.get("version"), "title": title,
            "current_doi": current,
            "current_doi_belongs_to": registered.get("title", ""),
            "found": found}

    if found.get("doi") and found["doi"].lower() == current.lower():
        step["action"] = "skip: already correct"
        return step
    if found.get("doi"):
        step["action"] = "replace"
        step["patch"] = {"DOI": found["doi"],
                         "url": "https://doi.org/" + found["doi"]}
        return step

    # No replacement exists. Clearing is justified only when the DOI now in
    # the item provably describes a different work: an arXiv preprint has no
    # Crossref DOI of its own, so "not found by title" alone proves nothing.
    if registered.get("title") and _similar(
            title, registered["title"]) < TITLE_FLOOR:
        arxiv = arxiv_id(data)
        step["action"] = "clear"
        step["patch"] = {
            "DOI": "",
            "url": (f"https://arxiv.org/abs/{arxiv}" if arxiv
                    else str(data.get("url") or "")),
        }
        return step
    step["action"] = "skip: " + (found.get("error") or "nothing to do")
    return step


def apply(step: dict) -> dict:
    status, _ = _zotero_request(
        f"items/{urllib.parse.quote(step['key'])}",
        data=json.dumps(step["patch"]).encode(), method="PATCH",
        version=step["version"])
    return {"status": status, "ok": status in (200, 204)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--keys", required=True,
                    help="comma-separated Zotero item keys")
    ap.add_argument("--execute", action="store_true",
                    help="actually write (default is dry-run)")
    args = ap.parse_args()

    steps = []
    for key in [k.strip() for k in args.keys.split(",") if k.strip()]:
        try:
            step = plan(key)
        except Exception as exc:
            step = {"key": key, "action": f"error: {type(exc).__name__}: {exc}"}
        # Both writing actions carry a `patch`; keying on "replace" alone
        # silently skipped every "clear" and reported the plan as if done.
        if args.execute and "patch" in step:
            step["result"] = apply(step)
        steps.append(step)

    print(json.dumps({"dry_run": not args.execute, "items": steps},
                     ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
