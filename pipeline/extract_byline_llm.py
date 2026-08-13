#!/usr/bin/env python3
"""Read a paper's byline off the rendered first page instead of parsing it.

    python pipeline/extract_byline_llm.py --validate --limit 20
    python pipeline/extract_byline_llm.py --unresolved --execute

The deterministic parsers in `build_bibliography_db` reached 85.8% of the
corpus over about a dozen layout fixes, and every remaining paper needs its
own: markers that trail the name, Greek letters, e-mail addresses standing in
for affiliations, footnotes wrapped in a narrow column. A rendered page has
none of those problems — the layout is the thing being read, not an obstacle
to reading it.

The model is used as an *extractor*, never as an authority. It returns the
affiliation strings as printed; those strings are then matched to the paper's
own institution rows by `best_institution_for`, the same function every other
path uses, and an author it names who is not in the record is discarded. So a
hallucinated institution cannot enter the DB: there is nothing for it to match.

`--validate` measures it against papers the marker parser already resolved,
because a tool that cannot be checked should not be run over the corpus.

Rows are written with source `llm.byline`, distinct from every parser, so the
accuracy check can grade it separately and it can be deleted in one statement.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import sqlite3
import sys
import time
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "pipeline"
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import build_bibliography_db as bib            # noqa: E402

DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"
MODEL = "claude-sonnet-4-5-20250929"
DPI = 150

PROMPT = """Read only the byline of this paper's first page.

Return JSON: {"authors": [{"name": ..., "affiliations": [...]}]}

Copy each affiliation string verbatim as printed, including the department.
Resolve superscript numbers, symbols, Greek letters, or a stacked layout to
decide which affiliation belongs to which author. If the page marks none of
them, give every author every affiliation the byline prints. Ignore e-mail
addresses, funding notes, and equal-contribution marks. If the page shows no
byline at all, return {"authors": []}. JSON only, no prose."""


def first_page_png(pdf_path: Path) -> bytes | None:
    try:
        import fitz
    except ImportError:
        return None
    try:
        document = fitz.open(pdf_path)
        try:
            return document[0].get_pixmap(dpi=DPI).tobytes("png")
        finally:
            document.close()
    except Exception:
        return None


def read_byline(client, png: bytes) -> list[dict]:
    """The byline as the model reads it, or [] when it cannot."""
    response = client.messages.create(
        model=MODEL, max_tokens=2000,
        messages=[{"role": "user", "content": [
            {"type": "image", "source": {
                "type": "base64", "media_type": "image/png",
                "data": base64.b64encode(png).decode()}},
            {"type": "text", "text": PROMPT}]}])
    text = response.content[0].text.strip()
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < start:
        return []
    try:
        return json.loads(text[start:end + 1]).get("authors") or []
    except json.JSONDecodeError:
        return []


def record_authors(conn: sqlite3.Connection, paper_id: int) -> dict[str, int]:
    """This paper's authors, keyed by folded surname.

    The model reads what the page prints and the record holds what Zotero
    transcribed; "Xiusi Chen" comes back as "Xinsi Chen" often enough that
    matching on the full name loses real authors. The surname decides, and an
    author the record does not have is dropped.
    """
    out: dict[str, int] = {}
    for author_id, name in conn.execute(
            "SELECT a.author_id, a.display_name FROM paper_authors pa"
            " JOIN authors a USING(author_id) WHERE pa.paper_id=?",
            (paper_id,)):
        parts = [p for p in str(name).split() if p]
        if parts:
            out.setdefault(bib._fold(parts[-1]), author_id)
    return out


def resolve(conn: sqlite3.Connection, paper_id: int,
            byline: list[dict]) -> list[tuple]:
    """Model output turned into rows, or nothing it cannot ground."""
    authors = record_authors(conn, paper_id)
    institutions = conn.execute(
        "SELECT institution_id, raw_name FROM paper_institutions"
        " WHERE paper_id=?", (paper_id,)).fetchall()
    names = dict(conn.execute(
        "SELECT pi.institution_id, i.institution_name FROM paper_institutions"
        " pi JOIN institutions i USING(institution_id) WHERE pi.paper_id=?",
        (paper_id,)))
    order = {aid: n for n, (_, aid) in enumerate(
        sorted(authors.items(), key=lambda kv: kv[1]), 1)}

    rows = []
    for entry in byline:
        parts = [p for p in str(entry.get("name") or "").split() if p]
        if not parts:
            continue
        author_id = authors.get(bib._fold(parts[-1]))
        if author_id is None:
            continue
        for affiliation in entry.get("affiliations") or []:
            institution_id = bib.best_institution_for(
                str(affiliation), institutions)
            if institution_id is None:
                continue
            # Same guard the shared paths use: a row whose canonical name has
            # nothing in common with the text that chose it is not it.
            if bib.assignment_disagrees(str(affiliation),
                                        names.get(institution_id, "")):
                continue
            rows.append((paper_id, author_id, institution_id, None,
                         order.get(author_id, 0), "llm.byline"))
    return rows


def targets(conn: sqlite3.Connection, mode: str, limit: int | None) -> list:
    resolved = ("openalex", "scopus", "pdf.byline-marker",
                "pdf.inline-affiliation", "pdf.author-information",
                "pdf.stacked-byline", "pdf.shared-byline", "pdf.sole-author",
                "pdf.sole-affiliation")
    marks = ",".join("?" * len(resolved))
    if mode == "validate":
        sql = ("SELECT DISTINCT p.paper_id, p.slug,"
               " json_extract(p.metadata_json,'$.pdf_path')"
               " FROM paper_author_institutions pai JOIN papers p"
               " USING(paper_id) WHERE pai.source='pdf.byline-marker'"
               " ORDER BY p.paper_id")
        rows = conn.execute(sql).fetchall()
    else:
        sql = (f"SELECT DISTINCT p.paper_id, p.slug,"
               f" json_extract(p.metadata_json,'$.pdf_path')"
               f" FROM paper_author_institutions pai JOIN papers p"
               f" USING(paper_id) WHERE pai.source='pdf.unmarked-multi'"
               f" AND p.paper_id NOT IN (SELECT paper_id FROM"
               f" paper_author_institutions WHERE source IN ({marks}))"
               f" ORDER BY p.paper_id")
        rows = conn.execute(sql, resolved).fetchall()
    rows = [r for r in rows if r[2] and Path(r[2]).exists()]
    return rows[:limit] if limit else rows


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--validate", action="store_true",
                    help="grade against papers the marker parser resolved")
    ap.add_argument("--unresolved", action="store_true",
                    help="read the papers no parser could resolve")
    ap.add_argument("--execute", action="store_true", help="write rows")
    ap.add_argument("--limit", type=int)
    args = ap.parse_args()
    if not (args.validate or args.unresolved):
        ap.error("--validate 또는 --unresolved 가 필요하다")
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ANTHROPIC_API_KEY 가 없다", file=sys.stderr)
        return 2

    import anthropic
    client = anthropic.Anthropic(timeout=180.0, max_retries=4)
    conn = sqlite3.connect(args.db, timeout=60.0)
    conn.execute("PRAGMA busy_timeout = 60000")
    mode = "validate" if args.validate else "unresolved"
    rows = targets(conn, mode, args.limit)
    report = {"mode": mode, "papers": len(rows), "read": 0, "linked": 0,
              "agree": 0, "partial": 0, "disagree": 0, "samples": []}

    for index, (paper_id, slug, pdf_path) in enumerate(rows, 1):
        png = first_page_png(Path(pdf_path))
        if not png:
            continue
        try:
            byline = read_byline(client, png)
        except Exception as exc:
            print(f"  [warn] {slug[:40]}: {exc}", file=sys.stderr)
            continue
        report["read"] += 1
        produced = resolve(conn, paper_id, byline)
        report["linked"] += len(produced)

        if mode == "validate":
            reference = defaultdict(set)
            for author_id, institution_id in conn.execute(
                    "SELECT author_id, institution_id FROM"
                    " paper_author_institutions WHERE paper_id=?"
                    " AND source='pdf.byline-marker'", (paper_id,)):
                reference[author_id].add(institution_id)
            model = defaultdict(set)
            for row in produced:
                model[row[1]].add(row[2])
            for author_id, expected in reference.items():
                got = model.get(author_id)
                if got is None:
                    continue
                if got == expected:
                    report["agree"] += 1
                elif got & expected:
                    report["partial"] += 1
                else:
                    report["disagree"] += 1
                    if len(report["samples"]) < 8:
                        report["samples"].append(
                            {"slug": slug[:44],
                             "expected": sorted(expected), "model": sorted(got)})
        elif args.execute and produced:
            # The guessed rows go first. The primary key does not include
            # `source`, so inserting over an existing (paper, author,
            # institution) triple is silently ignored — and deleting after
            # that removed 81 papers' links and wrote nothing in their place.
            conn.execute(
                "DELETE FROM paper_author_institutions WHERE paper_id=?"
                " AND source='pdf.unmarked-multi'", (paper_id,))
            conn.executemany(
                "INSERT OR IGNORE INTO paper_author_institutions"
                " (paper_id,author_id,institution_id,marker,author_order,"
                " source) VALUES (?,?,?,?,?,?)", produced)
            conn.commit()
        if index % 10 == 0:
            print(f"  [llm] {index}/{len(rows)}", file=sys.stderr, flush=True)
        time.sleep(0.4)

    conn.close()
    graded = report["agree"] + report["partial"] + report["disagree"]
    if graded:
        report["rate"] = round((report["agree"] + report["partial"]) / graded, 3)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
