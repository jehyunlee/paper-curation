#!/usr/bin/env python3
"""Draw the bibliography database's schema, read from the database itself.

A hand-drawn ERD goes stale the first time a column moves. This reads
`sqlite_master` and `PRAGMA` output, so the picture cannot claim a key the
database does not have -- which matters here, because two of the keys are the
whole point: `source` sits inside `paper_author_institutions`'s primary key so
that two extractors agreeing on one link both leave a record, and
`extraction_attempts` exists so that "no row" stops meaning both "never tried"
and "tried and found nothing".

Usage:
    python pipeline/generate_schema_diagram.py --dry-run
    python pipeline/generate_schema_diagram.py --style academic
"""
from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "pipeline"
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

from lib import paperbanana                                   # noqa: E402

DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"
OUT = ROOT / "docs" / "img" / "bibliography_schema.png"

# The tables that carry the attribution story. The database holds more --
# citations history, deep-research caches -- and drawing all of them would bury
# the part a reader needs.
CORE = ("papers", "authors", "institutions", "paper_authors",
        "paper_institutions", "paper_author_institutions",
        "extraction_attempts", "institution_aliases", "paper_connections",
        "source_documents")

NOTES = {
    "paper_author_institutions":
        "`source` is IN the primary key. One link may carry several rows, one "
        "per kind of evidence, so a deposit and a parser agreeing on the same "
        "author and institution both leave a record instead of one silently "
        "overwriting the other. Aggregations must select DISTINCT "
        "(paper_id, author_id, institution_id) before summing.",
    "extraction_attempts":
        "What was tried, as opposed to what worked. Absence of a link used to "
        "mean either 'never run' or 'run and found nothing', which for an "
        "extractor billed per page is the difference between a bill and a "
        "repeat bill.",
    "paper_institutions":
        "The paper's candidate institutions. Every parser and the page reader "
        "match against this list, so an empty one idles all of them.",
    "authors":
        "Identity is the folded name, and ORCID when present. A partial "
        "unique index forbids two rows claiming one ORCID.",
    "paper_connections":
        "LLM claims, not bibliographic fact. Kept apart from the "
        "publisher-verified tables, and every row names the model.",
}


def schema(db: Path) -> list[dict]:
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    try:
        tables = []
        for (name,) in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
                " ORDER BY name"):
            if name not in CORE:
                continue
            columns = [(row[1], row[2], bool(row[5]))
                       for row in conn.execute(f"PRAGMA table_info({name})")]
            fks = [(row[3], row[2], row[4])
                   for row in conn.execute(
                       f"PRAGMA foreign_key_list({name})")]
            indexes = [row[0] for row in conn.execute(
                "SELECT sql FROM sqlite_master WHERE type='index'"
                " AND tbl_name=? AND sql IS NOT NULL", (name,))]
            tables.append({
                "name": name,
                "rows": conn.execute(
                    f"SELECT COUNT(*) FROM {name}").fetchone()[0],
                "columns": columns,
                "primary_key": [c for c, _t, pk in columns if pk],
                "foreign_keys": fks,
                "unique_indexes": [s for s in indexes if "UNIQUE" in s.upper()],
            })
        return tables
    finally:
        conn.close()


def method(tables: list[dict]) -> str:
    lines = [
        "# Bibliography database — schema",
        "",
        "An entity-relationship diagram of the tables that answer "
        "\"which author worked at which institution, and on what evidence\". "
        "Read from the live database, so every key shown is a key that "
        "exists.",
        "",
    ]
    for table in tables:
        lines.append(f"## {table['name']} ({table['rows']:,} rows)")
        lines.append("")
        lines.append("- **primary key**: "
                     + (", ".join(table["primary_key"]) or "rowid"))
        cols = ", ".join(f"{c} {t}" for c, t, _ in table["columns"])
        lines.append(f"- **columns**: {cols}")
        for column, target, target_column in table["foreign_keys"]:
            # SQLite reports the parent column as NULL when the child points
            # at the parent's own primary key. Name it, rather than print
            # "rowid", which is not what a reader will find in the schema.
            if not target_column:
                target_column = {"papers": "paper_id", "authors": "author_id",
                                 "institutions": "institution_id"}.get(
                                     target, "rowid")
            lines.append(f"- **references**: {column} → "
                         f"{target}.{target_column} (ON DELETE CASCADE)")
        if table["name"] in NOTES:
            lines.append(f"- **note**: {NOTES[table['name']]}")
        lines.append("")
    return "\n".join(lines)

def mermaid(tables: list[dict]) -> str:
    """An `erDiagram` in Mermaid, which GitHub renders and which cannot drift.

    Preferred over a generated picture. Three image attempts each got the one
    fact that matters wrong -- whether `source` sits inside
    `paper_author_institutions`'s primary key -- and a schema drawing that
    disagrees with the schema is worse than none. This is emitted from
    `PRAGMA` output, so it is right by construction.
    """
    type_of = {"INTEGER": "int", "TEXT": "string", "REAL": "float",
               "BLOB": "blob", "": "any"}
    lines = ["```mermaid", "erDiagram"]
    for table in tables:
        lines.append(f"    {table['name']} {{")
        for column, sql_type, _pk in table["columns"]:
            kind = type_of.get((sql_type or "").upper(), "string")
            marks = []
            if column in table["primary_key"]:
                marks.append("PK")
            if any(column == fk[0] for fk in table["foreign_keys"]):
                marks.append("FK")
            suffix = f' "{",".join(marks)}"' if marks else ""
            lines.append(f"        {kind} {column}{suffix}")
        lines.append("    }")
    seen = set()
    for table in tables:
        for column, target, _target_column in table["foreign_keys"]:
            edge = (target, table["name"], column)
            if edge in seen:
                continue
            seen.add(edge)
            lines.append(
                f'    {target} ||--o{{ {table["name"]} : "{column}"')
    lines.append("```")
    return "\n".join(lines)



ACADEMIC_RULES = """
VISUAL STYLE — ENTITY RELATIONSHIP DIAGRAM
- A formal ERD, not an illustration. No characters, no mascots, no scenery.
- Each table is a rectangle with a header bar carrying the table name and a
  list of its columns beneath. Mark primary-key columns with a key icon and
  foreign-key columns with a small link icon.
- Draw crow's-foot notation on every relationship line, and label the line
  with the joining column.
- Place `papers`, `authors` and `institutions` as the three entities, with
  `paper_author_institutions` between them as the associative table, drawn
  larger and centred because it is the table the whole design turns on.
- Put `extraction_attempts` beside `papers`, connected by paper_id.
- Muted professional palette: greys and one accent colour. White background.
- Set the four columns of paper_author_institutions's primary key in the
  accent colour so the composite key is visible at a glance. All FOUR carry a
  key icon -- paper_id, author_id, institution_id AND source. That `source` is
  part of the key is the single most important fact in this diagram: a reader
  who misses it will assume one link holds one row.
- Every word must be spelled exactly as given. Do not invent columns.
- No title text, no watermark, no legend beyond the notation itself.
"""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--style", default="academic",
                    choices=["academic", "cat"])
    ap.add_argument("--aspect", default="16:9")
    ap.add_argument("--rounds", type=int, default=3)
    ap.add_argument("--out", type=Path, default=OUT)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--format", default="image",
                    choices=["image", "mermaid"],
                    help="mermaid prints an erDiagram and draws nothing; it is "
                         "exact, so it is what the docs carry")
    args = ap.parse_args()

    if not args.db.exists():
        print(f"no database at {args.db}", file=sys.stderr)
        return 1
    tables = schema(args.db)
    if args.format == "mermaid":
        print(mermaid(tables))
        return 0
    body = method(tables)
    if args.style == "academic":
        body += "\n" + ACADEMIC_RULES
    if args.dry_run:
        print(body)
        return 0

    args.out.parent.mkdir(parents=True, exist_ok=True)
    caption = ("Entity-relationship diagram of the bibliography database, "
               "generated from the live schema.")
    image = paperbanana.generate_diagram(
        method=body, caption=caption, aspect_ratio=args.aspect,
        critic_rounds=args.rounds, output_path=args.out)
    if not image:
        print("PaperBanana 가 이미지를 만들지 못했다", file=sys.stderr)
        return 1
    print(f"저장: {args.out}  ({len(image):,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
