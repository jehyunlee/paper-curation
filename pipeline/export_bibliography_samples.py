#!/usr/bin/env python3
"""Export a bounded, relationally closed local bibliography sample (never publish)."""
import argparse
from contextlib import closing
import datetime
import json
from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
OMITTED = {
    "papers": ["header_raw", "metadata_json", "review_dir"],
    "source_documents": ["path"],
    "extraction_attempts": ["detail"],
}
TABLES = ["papers", "authors", "paper_authors", "institutions", "institution_groups",
          "institution_aliases", "paper_institutions", "paper_author_institutions",
          "extraction_attempts", "paper_connections", "source_documents",
          "citation_snapshots", "citation_yearly", "doi_resolutions", "openalex_enrichment"]


def export_sample(db, limit=100):
    if not 1 <= limit <= 1000:
        raise ValueError("limit must be between 1 and 1000")
    with closing(sqlite3.connect(Path(db).resolve().as_uri() + "?mode=ro", uri=True)) as conn:
        conn.execute("BEGIN")
        conn.row_factory = sqlite3.Row
        present = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        if "papers" not in present:
            raise ValueError("papers table is required")
        data, columns, foreign_keys = {}, {}, {}

        def read(table, where="1", params=()):
            if table not in present:
                data[table] = []
                columns[table] = []
                foreign_keys[table] = []
                return []
            info = conn.execute(f'PRAGMA table_info("{table}")').fetchall()
            names = [r[1] for r in info if r[1] not in OMITTED.get(table, [])]
            columns[table] = names
            foreign_keys[table] = [{"column": r[3], "table": r[2], "target": r[4] or next(
                (x[1] for x in conn.execute(f'PRAGMA table_info("{r[2]}")') if x[5] == 1), "")}
                for r in conn.execute(f'PRAGMA foreign_key_list("{table}")')]
            projection = ",".join(f'"{name}"' for name in names)
            order = ",".join(f'"{r[1]}"' for r in sorted(info, key=lambda x: x[5]) if r[5]) or projection
            rows = [dict(r) for r in conn.execute(
                f'SELECT {projection} FROM "{table}" WHERE {where} ORDER BY {order}', params)]
            data[table] = rows
            return rows

        def subset(table, column, values):
            values = sorted(set(v for v in values if v is not None))
            return read(table, f'"{column}" IN ({",".join("?" for _ in values)})' if values else "0", values)

        # Stable paper IDs, not a relevance or statistical sample.
        ids = [r[0] for r in conn.execute("SELECT paper_id FROM papers ORDER BY paper_id LIMIT ?", (limit,))]
        papers = subset("papers", "paper_id", ids)
        for table in ["paper_authors", "paper_institutions", "paper_author_institutions",
                      "extraction_attempts", "source_documents", "citation_snapshots",
                      "citation_yearly", "openalex_enrichment"]:
            subset(table, "paper_id", ids)
        placeholders = ",".join("?" for _ in ids)
        read("paper_connections", f'paper_id IN ({placeholders}) AND related_paper_id IN ({placeholders})' if ids else "0", ids + ids)
        subset("doi_resolutions", "slug", [r["slug"] for r in papers])
        subset("authors", "author_id", [r["author_id"] for t in ["paper_authors", "paper_author_institutions"] for r in data[t]])
        institutions = subset("institutions", "institution_id", [r["institution_id"] for t in ["paper_institutions", "paper_author_institutions"] for r in data[t]])
        subset("institution_groups", "group_id", [r.get("group_id") for r in institutions])
        subset("institution_aliases", "institution_id", [r["institution_id"] for r in institutions])
        # Refuse dangling exported FK values rather than silently fabricate targets.
        for table, keys in foreign_keys.items():
            for key in keys:
                targets = {r[key["target"]] for r in data.get(key["table"], [])}
                for row in data[table]:
                    value = row.get(key["column"])
                    if value is not None and value not in targets:
                        raise ValueError(f"Dangling FK: {table}.{key['column']}")
        return {
            "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "selection": "paper_id 오름차순 (통계적 대표 표본 아님)",
            "paper_count": len(papers), "requested_limit": limit,
            "total_papers": conn.execute("SELECT COUNT(*) FROM papers").fetchone()[0],
            "tables": data, "columns": columns, "foreign_keys": foreign_keys,
            "omitted": OMITTED, "missing_tables": [t for t in TABLES if t not in present],
        }


def javascript(payload):
    text = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    text = text.replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    return "window.BIBLIOGRAPHY_SAMPLE = " + text + ";\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=ROOT / ".cache/bibliography.sqlite3")
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--output", type=Path, default=ROOT / "docs/bibliography-samples.js")
    args = parser.parse_args()
    payload = export_sample(args.db, args.limit)
    args.output.write_text(javascript(payload), encoding="utf-8")
    print(f"Exported {payload['paper_count']} papers, {sum(map(len, payload['tables'].values()))} related rows to {args.output}")


if __name__ == "__main__":
    main()
