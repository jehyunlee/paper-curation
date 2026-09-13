#!/usr/bin/env python3
"""Draw the LDA topic-modelling loop as a cat figure with PaperBanana.

    python pipeline/generate_lda_diagram.py
    python pipeline/generate_lda_diagram.py --candidates 5
    python pipeline/generate_lda_diagram.py --aspect 21:9 --rounds 4
    python pipeline/generate_lda_diagram.py --dry-run

This is not part of the curation pipeline. It redraws a plain slide -- two
premises above four steps -- in the same house style as `workflow.png` and
`attribution_workflow.png`: cats on a paw-print path, one short pill per stage,
a strict whitelist of words that may be lettered into the picture.

Drawing is stochastic, so `--candidates N` keeps every variant side by side in
`pipeline/_img_workflows/` and copies the first success to `--out`.
"""
from __future__ import annotations

import argparse
import shutil
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "pipeline"
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

from config_loader import IMG_WORKFLOWS_DIR          # noqa: E402

DEFAULT_OUT = ROOT / "lda_topic_modeling.png"

METHOD = """
# Topic modelling with LDA, and the naming step that follows it

One method, start to finish: Latent Dirichlet Allocation over a corpus of
documents, then a language model that gives the discovered topics their names.

## The two premises (a band across the top, two panels side by side)

- **A document is a mixture of topics.** A document is not *about* one subject;
  it is a blend. One document can be seven parts Technology to three parts
  Economics.
- **A topic is a mixture of words.** A topic is not a name; it is a
  distribution over the vocabulary. Technology leans on words like AI, chip,
  data. Economics leans on words like market, price, trade.

Nothing under the band makes sense without these two premises, so they sit
above the steps, and the colours they introduce are used everywhere below:
Technology is amber, Economics is blue.

## Step 1 - Initialization

Every word occurrence in every document is assigned to one of K topics at
random, K = 20 here. The assignment is deliberately meaningless. It exists only
to give the loop something to correct, which is why the picture should make it
look like a mess.

## Step 2 - Iterative reassignment

This step *is* the method; the other three are setup and readout. One word
occurrence at a time, its current topic is dropped and drawn again from two
quantities multiplied together:

1. **document to topic** - how prevalent this topic already is in *this*
   document.
2. **word to topic** - how often this word is assigned to that topic across the
   *whole corpus*.

The sweep runs over the corpus again and again until the assignments stop
changing appreciably. Early sweeps churn; late sweeps barely move. That
settling is the one dynamic in the figure: the same small operation repeated
until it goes quiet.

## Step 3 - Extract result

Once the assignments hold still, counting them yields the two distributions the
model was after: topic proportions per document, and word probabilities per
topic. Nothing new is decided here. It is a tally of what the final assignments
already say.

## Step 4 - Topic naming

LDA hands back topics as ranked word lists with numbers for names. A language
model is given each topic's top words with a suitable prompt and returns a
short human-readable name. This is the only step outside the statistical model,
and it renames rather than re-estimates: the distributions do not move.
"""

# One cat per panel and per step. The coats differ so a reader can tell the
# stages apart at a glance, the same way the companion figures do it.
CAST = [
    ("Document", "a cream Birman holding an open document whose bar chart is "
     "one amber block and one smaller blue block, showing that a single "
     "document is a blend rather than one subject"),
    ("Topic", "an orange tabby sitting at the centre of a small hub of round "
     "word beads joined by short spokes, each bead a word belonging to that "
     "topic"),
    ("Initialize", "a tuxedo cat with a blindfold pushed up on its forehead, "
     "flinging a pawful of coloured word tiles over a row of open jars so that "
     "every jar ends up with a random jumble of colours"),
    ("Reassign", "a grey Russian Blue in half-moon glasses lifting ONE word "
     "tile out of a jar, glancing at a small two-pan balance beside it, and "
     "dropping the tile into a different jar; a curved arrow loops back over "
     "this cat, and the jars behind it are visibly sorting into cleaner "
     "colours from left to right"),
    ("Extract", "a calico cat with an abacus tallying the settled jars into "
     "two small charts, one stacked bar and one row of word bars, with a "
     "satisfied expression"),
    ("Name", "a Scottish Fold in a tiny mortarboard hanging a small engraved "
     "name plate onto a jar, a sparkling assistant orb floating beside it "
     "reading the jar's top words to help"),
]

RULES = """
### ABSOLUTE VISUAL RULES - SAME HOUSE STYLE AS THE PROJECT'S CAT WORKFLOW FIGURES

CANVAS
- White background, flat kawaii illustration, soft pastel palette, round
  shapes, thin clean outlines. No gradients, no glow, no 3D, no drop shadows,
  no textured paper, no photographic elements.

LAYOUT (two decks, and only two)
- TOP DECK - one wide rounded-rectangle panel with a thin outline, split down
  the middle into two halves by a light divider. It spans the full width.
  * Left half: the Document cat with its blended document.
  * Right half: the Topic cat at the centre of its bead hub.
  This deck states the premises. It is NOT a step: give it no step pill, no
  number, no arrow into the deck below other than one thin arrow dropping from
  the panel's bottom edge to the start of the path.
- BOTTOM DECK - four stages in ONE row, left to right, in this order:
  Initialize, Reassign, Extract, Name. The cats stand on a single trail of
  small paw prints running left to right, with an occasional ball of yarn as a
  decorative connector, exactly as in the companion figures.
- Under each of the four cats sits ONE small rounded pill label and nothing
  else, lettered exactly: Initialize / Reassign / Extract / Name.
- Above the second cat, a curved return arrow loops from its right side back to
  its left side to mean "repeat until it stops changing". This loop belongs to
  the second stage alone and must not enclose any other cat.

THE COLOUR RULE THAT CARRIES THE MEANING
- Two topic colours only: amber and blue. They are introduced in the top deck
  and reused for every word tile, jar and bar below.
- The story must be legible from colour alone, left to right: at Initialize the
  jars hold a random mix of amber and blue; at Reassign they are partly sorted;
  at Extract each jar is almost entirely one colour. If the jars look equally
  jumbled at every stage, the figure has failed.

THE CATS
- Every stage is a CAT doing the work. The cat's pose IS the icon - no extra
  clip art beside it, no speech bubbles, no thought bubbles, no emoji.
- Six cats total, one per entry in the cast, each with the coat named for it.
  Never repeat the same cat twice.
- Cats are the same size as each other, chibi proportions, small scarves or bow
  ties allowed in the stage's colour.

WORDS THAT MAY BE LETTERED - AN EXHAUSTIVE WHITELIST
Nothing outside this list may appear as text anywhere in the image:
- In the top deck: Technology, Economics, 70%, 30%, and the six word beads
  AI, chip, data, market, price, trade.
- Under the four cats: Initialize, Reassign, Extract, Name.
- One small tag by the first cat's jars: K = 20.
- Two tiny tags on the second cat's balance pans: document and corpus.
- Two engraved name plates at the fourth cat: Technology and Economics.
Every one of these words must be spelled correctly. Any other lettering -
titles, captions, numbers, axis labels, file names, invented word-like strings
such as "Ecomonics" or "Tehnolgy" - is a defect.

CORRECTNESS RULES THAT OVERRIDE PRETTINESS
- NO title text anywhere. No heading, no caption bar, no strapline in any
  corner. The figure begins at the top deck and has nothing above it.
- Write each label ONCE. A label printed twice, or a half-drawn second copy of
  one, ruins the figure.
- Body text inside any drawn document is plain wavy placeholder lines with NO
  letters at all. Only the whitelisted words above are real text.
- Words that are instructions to the illustrator must never be drawn: figure,
  title, caption, step, row, deck, label, style, panel.
- Print labels as bare words: no quotation marks, no brackets, no "1." or
  "Step 2" prefixes anywhere.
- No watermarks, no colour-name labels, no logos. English only, short.
"""

CAPTION = (
    "A flat kawaii cat figure on a white background explaining Latent "
    "Dirichlet Allocation. A wide rounded panel across the top holds two "
    "premises side by side: a cat with a document whose bar splits amber "
    "Technology 70% and blue Economics 30%, and a cat at the centre of a hub "
    "of word beads reading AI, chip, data, market, price, trade. Below it four "
    "cats stand on one left-to-right paw-print trail, each under a single "
    "rounded pill: Initialize, where a blindfolded cat flings coloured word "
    "tiles at random into jars tagged K = 20; Reassign, where a spectacled cat "
    "moves one tile between jars while a two-pan balance tagged document and "
    "corpus tips, with a curved arrow looping back over this cat only; "
    "Extract, where a cat tallies the now settled jars into a stacked bar and "
    "a row of word bars; and Name, where a cat in a mortarboard hangs engraved "
    "plates reading Technology and Economics onto the jars with a sparkling "
    "assistant orb beside it. The jars grow visibly less jumbled from left to "
    "right. No title, no numbers beyond those named, document body text drawn "
    "as wavy placeholder lines."
)


def build_method() -> str:
    cast = "\n".join(f"- **{label}** - {look}" for label, look in CAST)
    return f"{METHOD}\n## The cast\n\n{cast}\n{RULES}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--aspect", default="16:9")
    ap.add_argument("--rounds", type=int, default=3)
    ap.add_argument("--candidates", type=int, default=1,
                    help="draw N variants into pipeline/_img_workflows/ and "
                         "copy the first success to --out")
    ap.add_argument("--dry-run", action="store_true",
                    help="print the description without drawing")
    args = ap.parse_args()

    method = build_method()
    if args.dry_run:
        print(method)
        return 0

    from lib import paperbanana

    def log(msg: str) -> None:
        print(f"[{datetime.now():%H:%M:%S}] {msg}", flush=True)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    if args.candidates <= 1:
        image = paperbanana.generate_diagram(
            method=method, caption=CAPTION, aspect_ratio=args.aspect,
            critic_rounds=args.rounds, output_path=args.out)
        if not image:
            print("PaperBanana 가 이미지를 만들지 못했다", file=sys.stderr)
            return 1
        print(f"저장: {args.out}  ({len(image):,} bytes)")
        return 0

    IMG_WORKFLOWS_DIR.mkdir(parents=True, exist_ok=True)
    drawn: list[Path] = []
    for index in range(1, args.candidates + 1):
        candidate = IMG_WORKFLOWS_DIR / f"lda_{index}.png"
        log(f"candidate #{index} …")
        try:
            image = paperbanana.generate_diagram(
                method=method, caption=CAPTION, aspect_ratio=args.aspect,
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
