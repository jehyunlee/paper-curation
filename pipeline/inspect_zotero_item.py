#!/usr/bin/env python3
"""Show what a Zotero item actually holds, and what its DOI actually is.

    python pipeline/inspect_zotero_item.py --keys RM7J55RG,ZA7W3PFQ
    python pipeline/inspect_zotero_item.py --slugs 1042,961 --json

Two items in this library carry a DOI belonging to a different paper, so the
build matched them to the wrong work. Deciding what to do about that needs the
item's own fields side by side with the publisher record its DOI resolves to,
plus the collections and attachments that say what the item is for.

Read-only: this script never writes to Zotero.
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "pipeline"
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"
MAILTO = "jehyun.lee@gmail.com"

FIELDS = ("itemType", "title", "publicationTitle", "DOI", "url", "date",
          "volume", "issue", "pages", "publisher", "ISSN", "journalAbbreviation",
          "libraryCatalog", "archiveID", "extra", "dateAdded", "dateModified")


def _zotero(path: str) -> object:
    from config_loader import get_zotero_api_key, get_zotero_user_id
    url = (f"https://api.zotero.org/users/{get_zotero_user_id()}/{path}")
    request = urllib.request.Request(
        url, headers={"Zotero-API-Key": get_zotero_api_key(),
                      "Zotero-API-Version": "3"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def fetch_item(key: str) -> dict | None:
    try:
        return _zotero(f"items/{urllib.parse.quote(key)}")
    except Exception as exc:
        print(f"  [warn] item {key}: {exc}", file=sys.stderr)
        return None


def fetch_children(key: str) -> list[dict]:
    try:
        return _zotero(f"items/{urllib.parse.quote(key)}/children")
    except Exception as exc:
        print(f"  [warn] children {key}: {exc}", file=sys.stderr)
        return []


def fetch_collection_names(keys: list[str]) -> list[str]:
    names = []
    for key in keys:
        try:
            payload = _zotero(f"collections/{urllib.parse.quote(key)}")
            names.append(str((payload.get("data") or {}).get("name") or key))
        except Exception:
            names.append(key)
    return names


def crossref(doi: str) -> dict:
    """What the DOI resolves to at the registration agency."""
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
    return {
        "title": (message.get("title") or [""])[0],
        "journal": (message.get("container-title") or [""])[0],
        "publisher": message.get("publisher", ""),
        "issued": "-".join(
            str(part) for part in
            (message.get("issued", {}).get("date-parts") or [[""]])[0]),
        "authors": [f"{a.get('given', '')} {a.get('family', '')}".strip()
                    for a in message.get("author", [])],
    }


def corpus_papers(db: Path, key: str) -> list[dict]:
    if not db.exists():
        return []
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    try:
        return [{"slug": slug, "db_title": title, "doi": doi}
                for slug, title, doi in conn.execute(
                    "SELECT slug, title, doi FROM papers "
                    "WHERE zotero_item_key=? ORDER BY slug", (key,))]
    finally:
        conn.close()


def keys_for_slugs(db: Path, slugs: list[str]) -> list[str]:
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    try:
        found = []
        for prefix in slugs:
            row = conn.execute(
                "SELECT zotero_item_key FROM papers WHERE slug LIKE ?"
                " AND zotero_item_key<>''", (prefix + "%",)).fetchone()
            if row:
                found.append(row[0])
        return found
    finally:
        conn.close()


def inspect(key: str, db: Path) -> dict:
    item = fetch_item(key)
    if item is None:
        return {"key": key, "found": False}
    data = item.get("data") or {}
    doi = str(data.get("DOI") or "")
    children = fetch_children(key)
    return {
        "key": key,
        "found": True,
        "version": item.get("version"),
        "fields": {name: data.get(name) for name in FIELDS
                   if data.get(name) not in (None, "")},
        "creators": [
            {"type": c.get("creatorType"),
             "name": (f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
                      or c.get("name", ""))}
            for c in data.get("creators") or []],
        "collections": fetch_collection_names(data.get("collections") or []),
        "tags": [t.get("tag") for t in data.get("tags") or []],
        "children": [
            {"itemType": (c.get("data") or {}).get("itemType"),
             "title": (c.get("data") or {}).get("title"),
             "filename": (c.get("data") or {}).get("filename"),
             "linkMode": (c.get("data") or {}).get("linkMode"),
             "url": (c.get("data") or {}).get("url")}
            for c in children],
        "doi_resolves_to": crossref(doi),
        "corpus_papers": corpus_papers(db, key),
    }


def render(report: dict) -> str:
    if not report.get("found"):
        return f"[{report['key']}] NOT FOUND"
    lines = [f"═══ Zotero item {report['key']}  (version {report['version']})"]
    for name, value in report["fields"].items():
        lines.append(f"  {name:20s} {value}")
    lines.append("  creators")
    for creator in report["creators"]:
        lines.append(f"      {creator['type']:12s} {creator['name']}")
    lines.append(f"  collections          {report['collections'] or '—'}")
    lines.append(f"  tags                 {report['tags'] or '—'}")
    lines.append("  attachments")
    for child in report["children"] or []:
        lines.append(f"      {child['itemType']:12s} "
                     f"{child.get('filename') or child.get('title') or ''} "
                     f"{child.get('linkMode') or ''}")
    if not report["children"]:
        lines.append("      —")
    resolved = report["doi_resolves_to"]
    lines.append("  ── this DOI is registered to ──")
    if resolved.get("error"):
        lines.append(f"      unresolved: {resolved['error']}")
    elif resolved:
        lines.append(f"      title     {resolved['title']}")
        lines.append(f"      journal   {resolved['journal']} "
                     f"({resolved['publisher']}, {resolved['issued']})")
        lines.append(f"      authors   {', '.join(resolved['authors'])}")
    lines.append("  ── corpus papers pointing at this item ──")
    for paper in report["corpus_papers"] or []:
        lines.append(f"      {paper['slug'][:60]}")
        lines.append(f"        db_title {paper['db_title'][:70]}")
    if not report["corpus_papers"]:
        lines.append("      — (none: the DB no longer trusts this item)")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--keys", help="comma-separated Zotero item keys")
    ap.add_argument("--slugs", help="comma-separated slug prefixes")
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    keys = [k.strip() for k in (args.keys or "").split(",") if k.strip()]
    if args.slugs:
        keys += keys_for_slugs(
            args.db, [s.strip() for s in args.slugs.split(",") if s.strip()])
    if not keys:
        print("--keys 또는 --slugs 가 필요하다", file=sys.stderr)
        return 2

    reports = [inspect(key, args.db) for key in dict.fromkeys(keys)]
    if args.json:
        print(json.dumps(reports, ensure_ascii=False, indent=2))
    else:
        print("\n\n".join(render(report) for report in reports))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
