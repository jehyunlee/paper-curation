#!/usr/bin/env python3
"""Draw the author-to-institution attribution pipeline with PaperBanana.

    python pipeline/generate_attribution_diagram.py
    python pipeline/generate_attribution_diagram.py --aspect 21:9 --rounds 4

`generate_workflow.py` draws the corpus pipeline from README.md and CLAUDE.md.
This draws the part that decides *who worked where*, which is a pipeline of its
own: nine evidence classes tried in order of how directly the source states the
mapping, each writing rows tagged with the class that produced them, and two
gates that measure whether a change helped.

The description below is generated from the live database, so the diagram
carries the counts the corpus actually has rather than counts written down once
and left to rot.
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

DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"
DEFAULT_OUT = ROOT / "docs" / "img" / "workflows" / "attribution_pipeline.png"

# Order matters: it is the order the backfill tries them, which is the order of
# how directly each source states who worked where.
CLASSES = [
    ("openalex", "OpenAlex authorships", "publisher deposit, ROR-backed"),
    ("scopus", "Scopus authorships", "publisher deposit, by author id"),
    ("pdf.byline-marker", "byline markers", "1 / a / ♣ / α resolved to a block"),
    ("pdf.stacked-byline", "stacked byline", "affiliation under each name"),
    ("pdf.inline-affiliation", "inline byline", "NAME, Institution, Country"),
    ("pdf.author-information", "author-information block", "ACS back matter"),
    ("pdf.shared-byline", "shared byline", "no marker: everyone shares it"),
    ("pdf.sole-author", "sole author", "one author holds every affiliation"),
    ("pdf.sole-affiliation", "sole affiliation", "one place, no ambiguity"),
    ("llm.byline", "rendered first page", "read by Claude, then matched"),
]


def counts(db: Path) -> dict:
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    try:
        papers = conn.execute("SELECT COUNT(*) FROM papers").fetchone()[0]
        by_source = dict(conn.execute(
            "SELECT source, COUNT(DISTINCT paper_id)"
            " FROM paper_author_institutions GROUP BY source"))
        resolved = [s for s, _, _ in CLASSES]
        marks = ",".join("?" * len(resolved))
        confirmed = conn.execute(
            f"SELECT COUNT(DISTINCT paper_id) FROM paper_author_institutions"
            f" WHERE source IN ({marks})", resolved).fetchone()[0]
        institutions = conn.execute(
            "SELECT COUNT(*) FROM institutions").fetchone()[0]
        with_ror = conn.execute(
            "SELECT COUNT(*) FROM institutions"
            " WHERE COALESCE(ror_id,'')!=''").fetchone()[0]
        return {"papers": papers, "by_source": by_source,
                "confirmed": confirmed, "institutions": institutions,
                "with_ror": with_ror}
    finally:
        conn.close()


def method_text(stats: dict) -> str:
    lines = [
        "# Author-to-institution attribution",
        "",
        f"A corpus of {stats['papers']:,} papers. For each paper the pipeline "
        f"decides which institution each author belongs to, and records which "
        f"kind of evidence decided it. {stats['confirmed']:,} papers "
        f"({stats['confirmed'] / stats['papers'] * 100:.1f}%) are settled on "
        f"evidence; the rest keep a guess that queries exclude.",
        "",
        "## Stage 1 — Sources, tried in order of directness",
        "",
        "Each source is tried only when the ones above it produced nothing, "
        "and every row is tagged with the class that produced it.",
        "",
    ]
    for source, label, note in CLASSES:
        n = stats["by_source"].get(source, 0)
        lines.append(f"- **{label}** ({source}) — {note} — {n:,} papers")
    lines += [
        "",
        "## Stage 2 — Grounding",
        "",
        "No source writes an institution directly. Every affiliation string, "
        "however it was obtained, is matched to one of the paper's own "
        "institution rows by token overlap, and refused when the row's "
        "canonical name shares nothing with the text that chose it. A name "
        "the model or the parser invents therefore cannot enter the database: "
        "there is nothing for it to match.",
        "",
        "## Stage 3 — Institution identity",
        "",
        f"{stats['with_ror']:,} of {stats['institutions']:,} institutions "
        f"carry a ROR id and need nothing further. A curated registry covers "
        f"only what ROR does not settle: multinationals whose country records "
        f"carry no parent edge, organisations too new to have a record, and "
        f"strings that name no organisation at all.",
        "",
        "## Stage 4 — Gates",
        "",
        "- **regression** — snapshots which class resolves each paper, then "
        "reports lost, gained and reclassified separately. A widening that "
        "narrows elsewhere is invisible in a total.",
        "- **accuracy** — compares the parsers against OpenAlex wherever both "
        "answer for the same author, and prints the pairs rather than only "
        "the rate.",
        "",
        "The fallback is not an answer. A paper with several institutions and "
        "no readable markers links every author to every one, tagged unresolved, "
        "so that a ranking can exclude it rather than silently credit a "
        "university with authors who were never there.",
    ]
    return "\n".join(lines)


CAPTION = (
    "A four-stage pipeline diagram. Stage 1 is a vertical ladder of ten "
    "evidence sources, tried top to bottom, each labelled with its tag and the "
    "number of papers it settles; publisher deposits at the top, PDF byline "
    "parsers in the middle, the rendered-page reader at the bottom. Every "
    "source feeds one shared Stage 2 box, 'match to this paper's own "
    "institution rows', which is the only way anything reaches the database — "
    "draw it as a gate all arrows must pass. Stage 3 resolves institution "
    "identity through ROR with a small curated registry beside it for what ROR "
    "does not cover. Stage 4 shows two feedback gates, regression and accuracy, "
    "looping back to Stage 1. A separate muted box off to the side holds the "
    "unresolved fallback, explicitly excluded from queries. Clean academic "
    "figure, restrained palette, no clip art."
)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--aspect", default="16:9")
    ap.add_argument("--rounds", type=int, default=3)
    ap.add_argument("--dry-run", action="store_true",
                    help="print the description without drawing")
    args = ap.parse_args()

    stats = counts(args.db)
    method = method_text(stats)
    if args.dry_run:
        print(method)
        return 0

    from lib import paperbanana
    args.out.parent.mkdir(parents=True, exist_ok=True)
    image = paperbanana.generate_diagram(
        method=method, caption=CAPTION, aspect_ratio=args.aspect,
        critic_rounds=args.rounds, output_path=args.out)
    if not image:
        print("PaperBanana 가 이미지를 만들지 못했다", file=sys.stderr)
        return 1
    print(f"저장: {args.out}  ({len(image):,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
