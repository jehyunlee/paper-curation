#!/usr/bin/env python3
"""Apply the institution naming rules to the bibliography DB.

    # Resolve ROR's Wikipedia links to current article titles (network) and
    # pin them in pipeline/data/institution_wikipedia_titles.json.
    python pipeline/normalize_institutions.py --refresh-wikipedia

    # Show what the rules and corrections would change (read-only).
    python pipeline/normalize_institutions.py

    # Write the changes.
    python pipeline/normalize_institutions.py --apply

    # Rule 2 review list: every Institute/Laboratory and whether it has a parent.
    python pipeline/normalize_institutions.py --parent-report institutes.csv

The same pass runs at the end of every `build_bibliography_db.py` build, so the
rules and `pipeline/data/institution_corrections.json` hold for new papers too.
The rules themselves are documented in `pipeline/lib/institution_policy.py`
and in the README section "기관명 정규화 기준".
"""
from __future__ import annotations

import argparse
import csv
import json
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

import build_bibliography_db as bib                 # noqa: E402
from lib import bibliography_lock, institution_policy as policy  # noqa: E402
from lib.ror_index import RorIndex                  # noqa: E402

USER_AGENT = f"paper-curation/1.0 ({bib.MAILTO})"
BATCH = 50


def _query(lang: str, titles: list[str], *, langlinks: bool) -> dict:
    params = {"action": "query", "format": "json", "formatversion": "2",
              "redirects": "1", "titles": "|".join(titles)}
    if langlinks:
        params.update({"prop": "langlinks", "lllang": "en", "lllimit": "max"})
    url = f"https://{lang}.wikipedia.org/w/api.php?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)
        except OSError:
            if attempt == 3:
                raise
            time.sleep(2 ** attempt)
    raise AssertionError("unreachable")


def resolve_titles(pages: dict[str, set[str]]) -> dict[str, str]:
    """Current English article title for each linked (language, title).

    A non-English article maps to its English counterpart, or to "" when
    there is none (the ROR English label then names the institution). Deleted
    articles are left out.
    """
    resolved: dict[str, str] = {}
    for lang, titles in sorted(pages.items()):
        ordered = sorted(titles)
        for start in range(0, len(ordered), BATCH):
            chunk = ordered[start:start + BATCH]
            data = _query(lang, chunk, langlinks=lang != "en")["query"]
            moved = {}
            for step in data.get("normalized", []) + data.get("redirects", []):
                moved[step["from"]] = step["to"]
            by_title = {page["title"]: page for page in data.get("pages", [])}
            for original in chunk:
                final = original
                for _ in range(3):
                    final = moved.get(final, final)
                page = by_title.get(final) or {}
                if page.get("missing"):
                    continue
                english = next((link["title"] for link in page.get("langlinks", [])
                                if link.get("lang") == "en"), "")
                resolved[policy.title_key(lang, original)] = (
                    final if lang == "en" else english)
    return resolved


def refresh_wikipedia(db_path: Path) -> dict:
    index = RorIndex()
    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    try:
        ror_ids = {r for (r,) in conn.execute(
            "SELECT ror_id FROM institutions WHERE ror_id<>'' UNION "
            "SELECT parent_ror_id FROM institutions WHERE parent_ror_id<>''")}
    finally:
        conn.close()
    pages: dict[str, set[str]] = {}
    for ror_id in ror_ids:
        lang, title = policy.wikipedia_page(index.reference(ror_id)["wikipedia"])
        if lang:
            pages.setdefault(lang, set()).add(title)
    titles = policy.load_titles()
    fresh = resolve_titles(pages)
    titles.update(fresh)
    policy.WIKIPEDIA_TITLES_PATH.write_text(
        json.dumps(dict(sorted(titles.items())), ensure_ascii=False, indent=1)
        + "\n", encoding="utf-8")
    return {"ror_ids": len(ror_ids),
            "articles": sum(len(v) for v in pages.values()),
            "resolved": len(fresh), "pinned": len(titles),
            "path": str(policy.WIKIPEDIA_TITLES_PATH.relative_to(ROOT))}


def run(db_path: Path, *, write: bool) -> dict:
    descriptor = bibliography_lock.acquire_bibliography_writer_lock(db_path)
    try:
        conn = sqlite3.connect(db_path, timeout=60.0)
        try:
            bib.ensure_schema_migrations(conn)
            result = policy.apply(conn, bib.country_from_raw,
                                  bib.is_local_language_institution)
            if write:
                conn.commit()
            else:
                conn.rollback()
            result["written"] = write
            return result
        finally:
            conn.close()
    finally:
        bibliography_lock.release_bibliography_writer_lock(db_path, descriptor)


def parent_report(db_path: Path, out: Path) -> int:
    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    try:
        rows = policy.parent_review(conn)
    finally:
        conn.close()
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]) if rows else
                                ["institution"])
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--db", type=Path, default=bib.DEFAULT_DB)
    ap.add_argument("--refresh-wikipedia", action="store_true")
    ap.add_argument("--apply", action="store_true", help="write the changes")
    ap.add_argument("--parent-report", type=Path)
    args = ap.parse_args()
    if args.refresh_wikipedia:
        print(json.dumps(refresh_wikipedia(args.db), ensure_ascii=False, indent=2))
    if args.parent_report:
        count = parent_report(args.db, args.parent_report)
        print(f"{count} institutes/laboratories -> {args.parent_report}")
        return 0
    print(json.dumps(run(args.db, write=args.apply), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
