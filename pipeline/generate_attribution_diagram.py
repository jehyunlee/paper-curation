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
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "pipeline"
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"
DEFAULT_OUT = ROOT / "docs" / "img" / "workflows" / "attribution_pipeline.png"
CAT_OUT = ROOT / "attribution_workflow.png"

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


# One cat per evidence class, in the order the pipeline tries them. The cast
# is the point: a reader should see at a glance that the top of the ladder is
# somebody handing over a record and the bottom is somebody squinting at a page.
CAT_CAST = [
    ("openalex", "a well-dressed postal cat delivering a sealed envelope stamped "
     "with a ROR seal — the publisher's own deposit, handed over, not guessed"),
    ("scopus", "a second postal cat with a smaller satchel, delivering fewer "
     "envelopes but the same kind"),
    ("pdf.byline-marker", "a scholarly cat in half-moon glasses tracing "
     "superscript numbers from author names down to a numbered list"),
    ("pdf.stacked-byline", "a cat reading a column of names with each "
     "affiliation stacked directly underneath"),
    ("pdf.inline-affiliation", "a cat following one long line where the name "
     "and the institution sit side by side"),
    ("pdf.author-information", "a cat flipping to the back of the paper to a "
     "boxed AUTHOR INFORMATION block"),
    ("pdf.shared-byline", "a cat gesturing at one affiliation under a whole "
     "group of names, meaning it belongs to all of them"),
    ("pdf.sole-author", "a small cat beside a single author holding several "
     "institution badges at once"),
    ("pdf.sole-affiliation", "a cat pointing at the only institution on the "
     "page, nothing to disambiguate"),
    ("llm.byline", "a cat wearing a tiny headlamp, peering at a rendered page "
     "image through a magnifier when every other cat has given up"),
]

CAT_RULES = """
VISUAL STYLE — CAT WORKFLOW
- Every stage is a cat character doing the work, warm and hand-drawn, in the
  style of a friendly children's science book. Soft rounded shapes.
- White background, clean modern layout, soft pastel palette.
- BEFORE the ladder, on its left, a first cat builds the paper's institution
  list: it holds the front page and copies out only two kinds of line — a bare
  line above the abstract, and a line that begins with a superscript marker —
  while a small waste-basket beside it takes the body prose it refused. Draw an
  arrow from this cat's list into the librarian's desk, and make clear the
  ladder cannot start without it.
- The ten source cats form a visible LADDER, top to bottom, each holding a
  small sign carrying its tag and nothing else — no counts anywhere in this
  figure. A cat only acts when the ones above
  it came back empty — draw them queued, not working in parallel.
- Every cat's output flows into ONE gate: a stern librarian cat at a desk who
  checks each slip against the paper's own institution list before stamping it.
  Nothing reaches the archive without passing this desk. Make the gate obvious.
- Behind the desk, a card-catalogue cabinet labelled ROR, with a small
  hand-written notebook beside it for the names ROR does not have.
- Two inspector cats loop back to the ladder: one comparing before/after
  photographs (regression), one holding a magnifier over a short list
  (review queue).
- One grey, dimmed cat sits apart in a roped-off corner with a box marked
  "unresolved" — visibly excluded, not part of the flow.
- AFTER the desk, before the archive, one more cat settles who the author is:
  it holds two name cards spelled differently — one with accents, one without —
  and clips them together, while wearing a badge marked ORCID. Beside it, two
  cards that look alike are being kept APART with a small "different people"
  tag, to show a shared identifier is not enough on its own.
- NO title text anywhere. Do not draw a heading, a caption bar or a strapline
  in any corner. The figure begins at Stage 0 and has nothing above it.
- Write each label ONCE. Never repeat a sentence in two places in one panel,
  and never leave a partial second copy of it.
- Spell every English word correctly -- "affiliation" and "byline" above all.
  A misspelt label makes the figure unusable.
- Any words that are an instruction to the illustrator must never appear in
  the picture. Only labels that a reader needs are drawn.
- Sample text inside a drawn document must be plausible English words, never
  invented letter strings.
- NO watermarks, NO color name labels. English labels only, short. Icons and
  cats speak louder than words.
"""


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
        "## Stage 0 — The paper's institution list",
        "",
        "Nothing below can run until the paper has candidate institutions, "
        "because every source is matched against that list. It is built from "
        "the publisher deposit and from the PDF's own front matter -- a bare "
        "line above the abstract, or a line led by the superscript marker that "
        "keys it to an author. Body prose is excluded by position rather than "
        "by wording, since prose is short and names organisations too.",
        "",
        "## Stage 1 — Sources, tried in order of directness",
        "",
        "Each source is tried only when the ones above it produced nothing, "
        "and every row is tagged with the class that produced it. The page "
        "reader is last because it is the only one that costs money and "
        "minutes; it is also sent back to papers the parsers left thin.",
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
        "## Stage 4 — Author identity",
        "",
        "A link needs a person as well as a place. Two spellings of one name "
        "-- accents, hyphen variants, initial spacing -- used to file one "
        "researcher under two rows and halve their count in a ranking. Names "
        "fold to a key that keeps the letters of every script. ORCID decides "
        "identity when present, but only when the two names can be one person: "
        "the identifier is reliable and the act of attaching it to a name is "
        "not.",
        "",
        "## Stage 5 — Gates",
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
    ap.add_argument("--out", type=Path)
    ap.add_argument("--style", default="academic", choices=("academic", "cat"))
    ap.add_argument("--aspect", default="16:9")
    ap.add_argument("--rounds", type=int, default=3)
    ap.add_argument("--dry-run", action="store_true",
                    help="print the description without drawing")
    args = ap.parse_args()

    if args.out is None:
        # The cat figure is linked from a document that ships, so it lives at
        # the repository root beside workflow.png rather than under the
        # gitignored docs/ tree.
        args.out = CAT_OUT if args.style == "cat" else DEFAULT_OUT
    stats = counts(args.db)
    method = method_text(stats)
    caption = CAPTION
    if args.style == "cat":
        # Strip every count from the prose too. Asking for a figure with no
        # numbers while handing the model a page of them produces a figure
        # with numbers.
        method = re.sub(r"[\d,]+ papers?", "papers", method)
        method = re.sub(r"\([\d.]+%\)", "", method)
        method = re.sub(r"[\d,]{3,} of [\d,]{3,}", "most", method)
        # No counts in the cat figure. The flow is what has to be legible,
        # and a number drawn into an image is wrong the moment the next
        # backfill runs. The academic figure keeps its counts.
        cast = "\n".join(f"- **{source}** — {look}"
                          for source, look in CAT_CAST)
        method = (method + "\n\n## The cast\n\n" + cast + "\n" + CAT_RULES)
        caption = (
            "A warm hand-drawn cat workflow. Ten cats queue in a vertical "
            "ladder, each holding a sign with its tag and no numbers, each "
            "acting only when the cats above came back empty. Every cat's slip "
            "flows to one librarian cat at a desk who checks it against the "
            "paper's own institution list and stamps it — the only way into "
            "the archive behind her, a card-catalogue cabinet labelled ROR "
            "with a small notebook beside it. Two inspector cats loop back to "
            "the ladder. One grey cat sits apart in a roped-off corner with a "
            "box marked unresolved. Children's science-book style, pastel, "
            "white background, short English labels only.")
    if args.dry_run:
        print(method)
        return 0

    from lib import paperbanana
    args.out.parent.mkdir(parents=True, exist_ok=True)
    image = paperbanana.generate_diagram(
        method=method, caption=caption, aspect_ratio=args.aspect,
        critic_rounds=args.rounds, output_path=args.out)
    if not image:
        print("PaperBanana 가 이미지를 만들지 못했다", file=sys.stderr)
        return 1
    print(f"저장: {args.out}  ({len(image):,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
