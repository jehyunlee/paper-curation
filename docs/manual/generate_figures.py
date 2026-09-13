"""Generate manual illustrations with the existing PaperBanana wrapper.

Run from the repository root using Python 3.12:
    python docs/manual/generate_figures.py
    python docs/manual/generate_figures.py --figure quickstart

This explicitly makes paid calls to the configured PaperBanana backends.
Existing images are preserved unless --force is supplied.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "pipeline"))

STYLE = """
Draw a polished educational diagram, white background, flat pastel kawaii cats,
consistent thin outlines, spacious typography and clear arrowheads. Cats perform
actual tasks; they are not decorative stickers. Use short English labels only
(the surrounding manual provides Korean explanations). No fake UI screenshot,
no invented tool logos, no watermarks, no pricing or API keys. Only the labels
explicitly quoted below should be printed. Keep labels large and readable.
"""

FIGURES = {
    "quickstart": (
        """Show the beginner's SINGLE PAPER review workflow, not a bulk pipeline.
A clear two-row layout, three equal stations per row; numbering 1 through 6.
Top row left to right: 1 'Zotero + PDF' (orange tabby holds one reference card
with attached PDF), 2 'Paper Curio' (tuxedo cat selects that parent reference),
3 'Plan' (Scottish Fold checks three items 'Provider', 'Output', 'Budget').
Bottom row left to right: 4 'Confirm' (cat pressing checkmark), 5 'Paper Curation'
(white cat reading extracted text and writing a review), 6 'Open Review'
(calico cat reading a browser page). Draw a connector from station 3 down around
the outside RIGHT margin and then across the gap above the bottom row to
station 4 on the LEFT; no crossing over labels. Ordinary arrows 1→2→3→4→5→6.
A small cloud 'Selected API' connects ONLY to station 5 using a double arrow,
showing selected evidence sent out and a generated review returned.
Bottom separate dashed box 'Separate tasks' with three small icons and labels
'Index', 'Timeline', 'Publish'. NO automatic arrow from review to these tasks.
The diagram must make human confirmation before API generation unmistakable.
""",
        "Single-paper workflow: Zotero and Paper Curio lead to a reviewed plan, explicit confirmation, Paper Curation generation, and an HTML review. Collection operations are separate.",
    ),
    "architecture": (
        """Show the relationship and data boundaries of Paper Curio and Paper Curation.
Use a left-to-right layered architecture, NOT a sequential execute-everything flow.
LEFT column two input boxes: 'Paper Curio' with a cat at Zotero, and 'CLI' with a
cat at a terminal. Both arrows enter CENTER box 'Paper Curation'. Inside center,
three small linked labels 'Plan', 'Confirm', 'Execute'. Beneath it a cylinder
'Shared corpus' connected by a double arrow; beside cylinder three output cards
'Review', 'Figures', 'Metadata'. No invented filenames.
RIGHT column three distinct action groups, all reachable from Execute as CHOICES,
not as an automatic sequence: green 'Local' containing 'Extract', 'BM25',
'Bibliography'; blue 'Selected API' containing 'Review', 'Summary', 'Chat';
orange DASHED group 'Explicit only' containing 'Timeline', 'Audio', 'Publish',
'Email'. Label connecting branches collectively 'Choose one task'.
Bottom thin separated security strip with a lock-bearing cat: 'OS keyring' and
'Environment overrides'. Do not draw credentials going into shared corpus.
Add a small note 'GJC subscription is separate' in this strip: the CLI coding
assistant subscription is NOT a credential for the pipeline's API calls.
Cats distinguish the two entry points and the engine; groups use small icons
and readable text rather than one cat for every subfeature. Arrows must be
unambiguous and must not imply every optional action runs after each review.
""",
        "Paper Curio and CLI are entry points to Paper Curation. Shared corpus, local actions, selected API actions, and explicitly requested optional actions remain separate.",
    ),
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--figure", choices=tuple(FIGURES), action="append")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    from lib.paperbanana import generate_diagram

    for name in args.figure or FIGURES:
        out = Path(__file__).resolve().parent / "images" / f"{name}.png"
        if out.exists() and not args.force:
            print(f"Preserving {out}", flush=True)
            continue
        method, caption = FIGURES[name]
        print(f"Generating {name} via PaperBanana", flush=True)
        image = generate_diagram(
            method=method + STYLE,
            caption=caption,
            aspect_ratio="16:9",
            critic_rounds=2,
            exp_mode="demo_planner_critic",
            retrieval_setting="auto",
            output_path=out,
        )
        if not image:
            raise RuntimeError(f"PaperBanana returned no image for {name}")
        print(f"Saved {out}: {len(image)} bytes", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
