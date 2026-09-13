#!/usr/bin/env python3
"""Draw the author-to-institution attribution pipeline with PaperBanana.

    python pipeline/generate_attribution_diagram.py --style cat
    python pipeline/generate_attribution_diagram.py --style cat --candidates 5
    python pipeline/generate_attribution_diagram.py --aspect 21:9 --rounds 4

`generate_workflow.py` draws the corpus pipeline from README.md and CLAUDE.md.
This draws the part that decides *who worked where*, which is a pipeline of its
own: ten evidence classes tried in order of how directly the source states the
mapping, each writing rows tagged with the class that produced them, one gate
every row must pass, and two checks that measure whether a change helped.

The description below is generated from the live database and the live source
order (`lib.evidence.RESOLVED_SOURCES`), so the diagram carries the ladder the
code actually runs rather than an order written down once and left to rot.

`--style cat` draws it in the same house style as `workflow.png`: a header of
source logos, cats on a winding paw-print path, one short pill label per stage,
dashed enclosures for the parts that are optional or excluded.
"""
from __future__ import annotations

import argparse
import shutil
import sqlite3
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "pipeline"
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

from config_loader import IMG_WORKFLOWS_DIR          # noqa: E402
from lib.evidence import RESOLVED_SOURCES, UNRESOLVED_SOURCE  # noqa: E402

DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"
DEFAULT_OUT = ROOT / "docs" / "img" / "workflows" / "attribution_pipeline.png"
CAT_OUT = ROOT / "attribution_workflow.png"

# Order matters: it is the order the backfill tries them, which is the order of
# how directly each source states who worked where. The short label is what the
# cat figure prints under a cat -- a tag like `pdf.author-information` does not
# fit on a pill and does not read as a picture.
CLASSES = [
    ("openalex", "Deposit", "publisher deposit, ROR-backed"),
    ("scopus", "Scopus", "publisher deposit, by author id"),
    ("pdf.byline-marker", "Markers", "1 / a / ♣ / α resolved to a block"),
    ("pdf.stacked-byline", "Stacked", "affiliation under each name"),
    ("pdf.inline-affiliation", "Inline", "NAME, Institution, Country"),
    ("pdf.author-information", "Back Matter", "ACS author-information block"),
    ("pdf.shared-byline", "Shared", "no marker: everyone shares it"),
    ("pdf.sole-author", "Sole Author", "one author holds every affiliation"),
    ("pdf.sole-affiliation", "Sole Place", "one place, no ambiguity"),
    ("llm.byline", "Page Reader", "rendered first page, read by Claude"),
]

# A diagram that disagrees with the code is worse than no diagram. The ladder
# is drawn from the same tuple the pipeline runs, so a class added or reordered
# in `lib.evidence` stops this script instead of quietly producing a stale
# picture.
if tuple(tag for tag, _, _ in CLASSES) != RESOLVED_SOURCES:
    raise SystemExit(
        "generate_attribution_diagram.CLASSES drifted from "
        f"lib.evidence.RESOLVED_SOURCES\n  code:    {RESOLVED_SOURCES}\n"
        f"  diagram: {tuple(tag for tag, _, _ in CLASSES)}")


# One cat per evidence class, in the order the pipeline tries them. The cast is
# the point: a reader should see at a glance that the front of the queue is
# somebody handing over a record and the back of it is somebody squinting at a
# page.
CAT_CAST = [
    ("Deposit", "an orange tabby postal cat in a smart navy cap, delivering a "
     "sealed envelope stamped with a ROR seal — the publisher's own "
     "deposit, handed over, not guessed"),
    ("Scopus", "a brown Havana cat, a second postman with a smaller satchel, "
     "delivering fewer envelopes of exactly the same kind"),
    ("Markers", "a tuxedo cat in half-moon glasses tracing superscript "
     "numbers from author names down to a numbered list"),
    ("Stacked", "a grey Russian Blue reading a column of names with each "
     "affiliation stacked directly underneath"),
    ("Inline", "a cream Birman following one long line where the name and the "
     "institution sit side by side"),
    ("Back Matter", "a calico cat flipping to the back of the paper, holding "
     "open a boxed AUTHOR INFORMATION block"),
    ("Shared", "a Siamese cat gesturing at one affiliation under a whole "
     "group of names, meaning it belongs to all of them"),
    ("Sole Author", "a small ginger kitten beside a single author holding "
     "several institution badges at once"),
    ("Sole Place", "a white long-haired cat pointing at the only institution "
     "on the page, nothing to disambiguate"),
    ("Page Reader", "a Bengal cat in a tiny headlamp peering at a rendered "
     "page image through a magnifier, awake only because every other cat gave "
     "up"),
]

# Stages that are not one of the ten sources but are drawn as cats too.
SUPPORT_CAST = [
    ("Front Page", "a ginger tabby holding a paper's first page, copying out only a "
     "bare line above the abstract and a line that begins with a superscript "
     "marker, while a small waste-basket beside it takes the body prose it "
     "refused"),
    ("Candidates", "a black-and-white cat filing those lines into a small tray labelled with "
     "the paper's own institutions — the tray every later cat must match "
     "against, so nothing downstream can start until this tray is filled"),
    ("Ground", "a stern grey British Shorthair librarian in a waistcoat at a "
     "large desk, checking each incoming slip against that tray and stamping "
     "only the ones that match"),
    ("Registry", "a cream Maine Coon at a card-catalogue cabinet marked ROR, "
     "with a small hand-written notebook beside it for the organisations ROR "
     "does not have"),
    ("Same Author", "a lilac-point cat clipping together two name cards spelled "
     "differently — one with accents, one without — while wearing an ORCID "
     "badge, and keeping two look-alike cards APART under a small tag"),
    ("Evidence Log", "a Scottish Fold writing in a ledger that two different cats "
     "reached the same link, and that a page was read even when reading it "
     "found nothing"),
    ("Regression", "a Sherlock-ish tabby inspector inside the gates fence, "
     "holding a before photograph beside an after photograph of the same "
     "queue"),
    ("Mismatch", "a smoke-grey second inspector inside the gates fence, holding a "
     "magnifier over a short list of paired name cards that cannot both be "
     "true"),
]

CAT_RULES = """
### ABSOLUTE VISUAL RULES — SAME HOUSE STYLE AS THE CORPUS WORKFLOW FIGURE
This figure is a companion to an existing picture and must look like it came
from the same illustrator on the same afternoon.

CANVAS
- 21:9 ultra-wide, white background, flat kawaii illustration, soft pastel
  palette, soft rounded shapes, thin clean outlines. No gradients, no glow, no
  3D, no drop shadows, no textured paper.

HEADER STRIP (top of the figure, above everything else)
- A single row of source/tool tiles, each a rounded-square logo tile with a
  BOLD short name under it and one small grey subtitle line under that:
  * OpenAlex — "publisher deposit"
  * Scopus — "publisher deposit"
  * PDF — "the paper itself"
  * Claude — "reads the rendered page"
  * ROR — "institution identity"
  * ORCID — "author identity"
- Thin horizontal arrows connect the tiles across the strip. This strip is the
  only place a logo appears.

THE PATH
- Every stage is a CAT doing the work. The cat's pose IS the icon — no extra
  clip-art beside it, no speech bubbles, no thought bubbles.
- The cats are NOT the same cat repeated. Each one has the coat named for it in
  the cast below — tabby, tuxedo, calico, Siamese, grey, cream, ginger — so a
  reader can tell them apart at a glance, exactly as in the companion figure.
- Under each cat sits ONE small rounded pill label, 1-2 words, and nothing
  else. No tags with dots in them, no file names, no numbers anywhere.
- The cats stand on ONE winding path drawn as a trail of small paw prints, with
  an occasional ball of yarn as a decorative connector. The path snakes: row 1
  runs left to right, turns down at the right edge, row 2 runs RIGHT TO LEFT,
  turns down at the left edge, row 3 runs left to right again.
- Because row 2 travels leftwards, its cats must be PLACED on the canvas in
  reverse. Place them exactly like this, from the left edge of the canvas to
  the right edge:
  * Row 1, left to right:  Front Page, Candidates, Deposit, Scopus
  * Row 2, left to right:  Sole Place, Sole Author, Shared, Back Matter,
    Inline, Stacked, Markers      (so the path, arriving from the top right,
    meets Markers first and Sole Place last)
  * Row 3, left to right:  Page Reader, Ground, Registry, Same Author,
    Evidence Log
- Every arrowhead on the path points the way the path travels, so row 2's
  arrows point LEFT.
- The ten source cats form a single-file QUEUE in the order the path visits
  them: Deposit, Scopus, Markers, Stacked, Inline, Back Matter, Shared,
  Sole Author, Sole Place, Page Reader. A cat only steps forward when the cat
  before it turns round with empty paws — draw them waiting their turn, never
  all working at once. This queue is the whole point of the figure and must be
  unmistakable.
- Ground is a GATE, not a stage: every source cat's slip flows into that one
  desk before anything continues. Draw a bundle of thin arrows leaving all ten
  source cats and converging on that single desk from above, and make the desk
  and its librarian visibly larger than any queue cat. If a reader cannot see
  that everything funnels through this desk, the figure has failed.

DASHED ENCLOSURES (the same dashed-fence device the companion figure uses)
Three of them, stacked in a column down the right-hand side of the canvas,
clear of the path. Each fence carries its name ONCE, printed as bare words on
its top edge, with no quotation marks and no prefix. A fence name is never
repeated under the fence and never gets a pill.
- A fence named Augment Pass, with a small wooden sign on its corner lettered
  OPTION. Inside it, a headlamp-wearing cat re-reads a thin stack of papers
  where only some authors were placed. The fence must contain that cat — an
  empty pen is wrong. A dashed arrow loops from the fence back to the Page
  Reader in row 3.
- A fence named Gates, holding two inspector cats, each with its own pill.
  Regression is a cat comparing a before photograph with an after photograph;
  Mismatch is a cat holding a magnifier over a short list of paired name cards.
  Dashed arrows loop from this fence back to the queue.
- A grey fence named Excluded, roped off, holding one grey dimmed cat sitting
  beside a box lettered unresolved. Nothing enters or leaves it. It
  must read as excluded, not as a stage.
- No queue cat may sit inside a fence, and no fence may overlap the path.

CORRECTNESS RULES THAT OVERRIDE PRETTINESS
- NO title text anywhere. No heading, no caption bar, no strapline in any
  corner. The figure begins at the header strip and has nothing above it.
- NO numbers, NO percentages, NO counts, anywhere in the figure.
- Write each label ONCE. Never repeat a label in two places, and never leave a
  partial second copy of one. A fence name printed twice ruins the figure.
- Spell every English word correctly — "affiliation", "byline", "unresolved"
  above all. A misspelt label makes the figure unusable.
- Words that are an instruction to the illustrator must never appear in the
  picture. Only labels a reader needs are drawn. In particular the words
  "figure", "title", "caption", "row", "in", "out", "option zone", "style" and
  "label" must not be lettered anywhere.
- Print every label as bare words. No quotation marks around a fence name, no
  brackets, no letter or number prefixes such as "A —" or "1." before it.
- A pill holds only the stage name from the list above. Never append a word
  from the cast description to it — "Deposit", never "Deposit postal".
- Text inside a drawn document is the most common way this figure fails. Draw
  body text as plain wavy placeholder lines with NO letters at all. Only these
  documents carry real words, and only these: the AUTHOR INFORMATION heading,
  the ROR cabinet label, the "unresolved" box, and the pairs of name cards.
  Invented letter strings such as "mmsnars" or "Semienines" must never appear.
- The six logo tiles in the header must show a simple recognisable mark. If a
  wordmark cannot be lettered correctly inside the tile, draw the tile as a
  plain coloured square with no letters in it rather than a garbled word.
- NO watermarks, NO colour-name labels. English only, short.
"""


def counts(db: Path) -> dict:
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    try:
        papers = conn.execute("SELECT COUNT(*) FROM papers").fetchone()[0]
        by_source = dict(conn.execute(
            "SELECT source, COUNT(DISTINCT paper_id)"
            " FROM paper_author_institutions GROUP BY source"))
        marks = ",".join("?" * len(RESOLVED_SOURCES))
        confirmed = conn.execute(
            f"SELECT COUNT(DISTINCT paper_id) FROM paper_author_institutions"
            f" WHERE source IN ({marks})", RESOLVED_SOURCES).fetchone()[0]
        institutions = conn.execute(
            "SELECT COUNT(*) FROM institutions").fetchone()[0]
        with_ror = conn.execute(
            "SELECT COUNT(*) FROM institutions"
            " WHERE COALESCE(ror_id,'')!=''").fetchone()[0]
        # A link confirmed by two independent sources is the reason `source`
        # sits inside the primary key, so the figure's description should be
        # able to say how often it happens.
        corroborated = conn.execute(
            "SELECT COUNT(*) FROM (SELECT 1 FROM paper_author_institutions"
            " GROUP BY paper_id, author_id, institution_id"
            " HAVING COUNT(DISTINCT source) > 1)").fetchone()[0]
        links = conn.execute(
            "SELECT COUNT(*) FROM (SELECT 1 FROM paper_author_institutions"
            f" WHERE source IN ({marks})"
            " GROUP BY paper_id, author_id, institution_id)",
            RESOLVED_SOURCES).fetchone()[0]
        return {"papers": papers, "by_source": by_source,
                "confirmed": confirmed, "institutions": institutions,
                "with_ror": with_ror, "corroborated": corroborated,
                "links": links}
    finally:
        conn.close()


def method_text(stats: dict, numbers: bool = True) -> str:
    """The pipeline in prose.

    `numbers=False` builds the same text with every count left out rather than
    scrubbing them afterwards with regexes: asking for a figure with no numbers
    while handing the model a page of them produces a figure with numbers.
    """
    def n(value: int, unit: str = "") -> str:
        return f"{value:,}{unit}" if numbers else "many"

    lines = [
        "# Author-to-institution attribution",
        "",
        (f"A corpus of {stats['papers']:,} papers. " if numbers
         else "A corpus of papers. ") +
        "For each paper the pipeline decides which institution each author "
        "belongs to, and records which kind of evidence decided it." +
        (f" {stats['confirmed']:,} papers "
         f"({stats['confirmed'] / stats['papers'] * 100:.1f}%) are settled on "
         f"evidence; the rest keep a guess that queries exclude."
         if numbers else
         " Most papers are settled on evidence; the rest keep a guess that "
         "queries exclude."),
        "",
        "## Stage 0 — The paper's own institution list",
        "",
        "Nothing below can run until the paper has candidate institutions, "
        "because every source is matched against that list. It is built from "
        "the publisher deposit and from the PDF's own front matter -- a bare "
        "line above the abstract, or a line led by the superscript marker that "
        "keys it to an author. Body prose is excluded by position rather than "
        "by wording, since prose is short and names organisations too. A name "
        "broken across a line break is rejoined before matching, and the PDF "
        "path may only link to institutions the corpus already knows: reading "
        "a foundation out of an acknowledgement invented institutions that "
        "were real names and the wrong fragment.",
        "",
        "## Stage 1 — Sources, tried in order of directness",
        "",
        "Each source is tried only when the ones above it produced nothing, "
        "and every row is tagged with the class that produced it. The page "
        "reader is last because it is the only one that costs money and "
        "minutes; " + ("a 300-paper A/B settled" if numbers else "a sampled "
        "A/B settled") + " that moving it earlier resolves exactly the same "
        "papers, so its place buys depth, not reach.",
        "",
    ]
    for source, label, note in CLASSES:
        count = stats["by_source"].get(source, 0)
        tail = f" — {count:,} papers" if numbers else ""
        lines.append(f"- **{label}** (`{source}`) — {note}{tail}")
    lines += [
        "",
        "## Stage 2 — Grounding, the one gate",
        "",
        "No source writes an institution directly. Every affiliation string, "
        "however it was obtained, is matched to one of the paper's own "
        "institution rows by token overlap, and refused when the row's "
        "canonical name shares nothing with the text that chose it. A name "
        "the model or the parser invents therefore cannot enter the database: "
        "there is nothing for it to match. This is why an LLM is safe here — "
        "it is an extractor, never an authority.",
        "",
        "## Stage 3 — Institution identity",
        "",
        (f"{stats['with_ror']:,} of {stats['institutions']:,} institutions "
         if numbers else "Most institutions ") +
        "carry a ROR id and need nothing further. A curated registry covers "
        "only what ROR does not settle: multinationals whose country records "
        "carry no parent edge, organisations too new to have a record, and "
        "strings that name no organisation at all. Curated parent groups sit "
        "under ROR so that a laboratory is counted where the work was led.",
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
        "## Stage 5 — One link, several proofs",
        "",
        "The evidence class is part of the link's key, so a deposit and a "
        "byline parser that reach the same conclusion both leave a row and "
        "the agreement is kept instead of discarded." +
        (f" {stats['corroborated']:,} of {stats['links']:,} links carry more "
         f"than one independent source." if numbers else
         " A tenth of all links carry more than one independent source.") +
        " A separate ledger records that an extractor *ran*, with the outcome "
        "-- linked, empty, unreadable, error -- because a table of successes "
        "cannot answer \"has this page already been paid for?\".",
        "",
        "## Stage 6 — Checks that loop back",
        "",
        "- **regression** — snapshots which class resolves each paper, then "
        "reports lost, gained and reclassified separately. A widening that "
        "narrows elsewhere is invisible in a total.",
        "- **mismatch review** — compares the parsers against the deposits "
        "wherever both answer for the same author and prints the pairs that "
        "cannot both be true. There is no agreement rate to report: joint "
        "appointments make disagreement normal, so the output is a list to "
        "read, not a score.",
        "- **augment** — the page reader is sent back to papers where the "
        "parsers placed only some of the authors. It resolves no new papers; "
        "it finishes the ones already resolved.",
        "",
        "The fallback is not an answer. A paper with several institutions and "
        f"no readable markers links every author to every one, tagged "
        f"`{UNRESOLVED_SOURCE}`, so that a ranking can exclude it rather than "
        "silently credit a university with authors who were never there.",
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

CAT_CAPTION = (
    "A 21:9 flat kawaii cat workflow on a white background, in the same house "
    "style as the project's corpus workflow figure. A header strip of source "
    "logo tiles — OpenAlex, Scopus, PDF, Claude, ROR, ORCID — each with a bold "
    "short name and a small subtitle. Below it, cats stand along one winding "
    "paw-print path that wraps across three rows, each cat with a single "
    "1-2 word rounded pill label under it and no numbers anywhere. Two cats "
    "build the paper's own institution list, then ten source cats wait in a "
    "single-file queue, each stepping forward only when the one before it "
    "turns round empty-pawed; the middle row travels right to left, so its "
    "cats are placed in reverse and its arrows point left. Every slip "
    "converges on one librarian cat at a "
    "desk who checks it against that list before stamping it, then a ROR "
    "card-catalogue cat, an ORCID cat clipping two spellings of one name "
    "together, and a cat writing the evidence ledger. Three dashed fences sit "
    "down the right-hand side, each named once on its top edge: an OPTION pass "
    "holding a headlamp cat re-reading thin papers, a gates pen with a "
    "regression cat and a mismatch cat looping back to the queue, and a "
    "roped-off grey pen holding one dimmed cat beside a box marked unresolved. "
    "Document body text is drawn as wavy placeholder lines, never as invented "
    "letters."
)


def build_prompt(stats: dict, style: str) -> tuple[str, str]:
    """(method, caption) for the requested style."""
    if style != "cat":
        return method_text(stats, numbers=True), CAPTION
    cast = "\n".join(f"- **{label}** — {look}"
                     for label, look in SUPPORT_CAST + CAT_CAST)
    method = (method_text(stats, numbers=False)
              + "\n\n## The cast\n\n" + cast + "\n" + CAT_RULES)
    return method, CAT_CAPTION


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--style", default="academic", choices=("academic", "cat"))
    ap.add_argument("--aspect", default="",
                    help="default: 21:9 for cat, 16:9 for academic")
    ap.add_argument("--rounds", type=int, default=3)
    ap.add_argument("--candidates", type=int, default=1,
                    help="draw N variants into pipeline/_img_workflows/ and "
                         "copy the first success to --out")
    ap.add_argument("--dry-run", action="store_true",
                    help="print the description without drawing")
    args = ap.parse_args()

    if args.out is None:
        # The cat figure is linked from a document that ships, so it lives at
        # the repository root beside workflow.png rather than under the
        # gitignored docs/ tree.
        args.out = CAT_OUT if args.style == "cat" else DEFAULT_OUT
    aspect = args.aspect or ("21:9" if args.style == "cat" else "16:9")

    stats = counts(args.db)
    method, caption = build_prompt(stats, args.style)
    if args.dry_run:
        print(method)
        return 0

    from lib import paperbanana

    def log(msg: str) -> None:
        print(f"[{datetime.now():%H:%M:%S}] {msg}", flush=True)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    if args.candidates <= 1:
        image = paperbanana.generate_diagram(
            method=method, caption=caption, aspect_ratio=aspect,
            critic_rounds=args.rounds, output_path=args.out)
        if not image:
            print("PaperBanana 가 이미지를 만들지 못했다", file=sys.stderr)
            return 1
        print(f"저장: {args.out}  ({len(image):,} bytes)")
        return 0

    # Several candidates, kept side by side so the operator can pick. Drawing
    # is stochastic: the queue reads clearly in some draws and not in others,
    # and picking is cheaper than re-prompting.
    IMG_WORKFLOWS_DIR.mkdir(parents=True, exist_ok=True)
    drawn: list[Path] = []
    for index in range(1, args.candidates + 1):
        candidate = IMG_WORKFLOWS_DIR / f"attribution_{index}.png"
        log(f"candidate #{index} …")
        try:
            image = paperbanana.generate_diagram(
                method=method, caption=caption, aspect_ratio=aspect,
                critic_rounds=args.rounds, output_path=candidate)
        except Exception as exc:                       # noqa: BLE001
            log(f"candidate #{index}: ERROR {str(exc)[:120]}")
            continue
        if image and candidate.exists():
            log(f"candidate #{index}: {candidate.stat().st_size / 1024:.0f}KB")
            drawn.append(candidate)
        else:
            log(f"candidate #{index}: FAILED")
        time.sleep(2)

    if not drawn:
        print("PaperBanana 가 이미지를 만들지 못했다", file=sys.stderr)
        return 1
    shutil.copy2(drawn[0], args.out)
    log(f"{len(drawn)}/{args.candidates} drawn; {drawn[0].name} → {args.out}")
    log("다른 후보가 더 나으면 그 파일을 직접 복사해 덮어쓴다")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
