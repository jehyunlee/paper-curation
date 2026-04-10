"""
Paper Curation Workflow 다이어그램 생성 (PaperBanana).

- METHOD_TEXT를 README.md Pipeline Steps + Project Structure에서 자동 생성
- VISUAL_RULES는 별도 유지 (스타일 지시)
- 21:9 aspect ratio (ultra-wide, cinematic)
- 5 candidates 기본, #1 자동 배포

Usage:
  PYTHONUTF8=1 python pipeline/generate_workflow.py
  PYTHONUTF8=1 python pipeline/generate_workflow.py --candidates 10
  PYTHONUTF8=1 python pipeline/generate_workflow.py --style fairy
"""

import argparse
import os
import re
import sys
import time
from pathlib import Path

from config_loader import IMG_WORKFLOWS_DIR, PROJECT_ROOT
WORKFLOW_DIR = IMG_WORKFLOWS_DIR


def _extract_section(content, heading):
    """Extract a markdown section by heading (matches ## or ###)."""
    pattern = rf'#{{2,3}}\s+{re.escape(heading)}\s*\n(.*?)(?=\n#{{2,3}}\s|\Z)'
    m = re.search(pattern, content, re.DOTALL)
    return m.group(1).strip() if m else ""


def build_method_text():
    """README.md + CLAUDE.md에서 METHOD_TEXT를 동적으로 생성."""
    readme_path = PROJECT_ROOT / "README.md"
    claude_path = PROJECT_ROOT / "CLAUDE.md"

    readme = ""
    if readme_path.exists():
        with open(readme_path, "r", encoding="utf-8") as f:
            readme = f.read()

    claude = ""
    if claude_path.exists():
        with open(claude_path, "r", encoding="utf-8") as f:
            claude = f.read()

    # 1. Pipeline Steps 테이블 (README > CLAUDE 순으로 탐색)
    steps_section = _extract_section(readme, "Pipeline Steps")
    if not steps_section:
        steps_section = _extract_section(claude, "Pipeline Scripts (execution order)")

    phases = []
    for m in re.finditer(
        r'\|\s*([\d.]+[ab]?)\s*\|\s*`([^`]+)`\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|',
        steps_section
    ):
        step, script, description, output = m.groups()
        phases.append(f"Step {step}: {script}\n  {description.strip()}\n  Output: {output.strip()}")

    # 2. Project Structure (README)
    structure_section = _extract_section(readme, "Project Structure")

    # 3. Architecture details (CLAUDE.md — richer info)
    architecture_parts = []
    for heading in ["Central Data Store", "Topic Views", "Shared Modules"]:
        section = _extract_section(claude, heading)
        if section:
            architecture_parts.append(f"#### {heading}\n{section}")
    architecture_section = "\n\n".join(architecture_parts)

    # 4. Execution Modes (README)
    modes_section = _extract_section(readme, "Execution Modes")
    if not modes_section:
        modes_section = _extract_section(readme, "실행 모드")

    # 5. Key Design Decisions (CLAUDE.md)
    design_section = _extract_section(claude, "Key Design Decisions")

    method = f"""## Paper Curation Pipeline — Automated Academic Paper Search, Review & Publishing

### PIPELINE PHASES (left to right flow)

{chr(10).join(phases) if phases else "(No pipeline steps found in README.md or CLAUDE.md)"}

### PROJECT STRUCTURE
{structure_section}

### DATA ARCHITECTURE
{architecture_section}

### MODE DECISION LOGIC (diamond shapes)
{modes_section}

### KEY DESIGN PRINCIPLES
{design_section}
"""
    return method


VISUAL_RULES = """
### ABSOLUTE VISUAL RULES
- Left to right flow, 21:9 ultra-wide aspect ratio
- Each phase box: SHORT label (1-2 words max) + a representative ICON/CLIPART inside or beside it
- Phase labels must be minimal: "Search", "Register", "Review", "Classify", "Insights", "Timeline", "Relation Network", "Validate", "HTML", "Deploy"
- Icons/cliparts are the primary visual — text is secondary
- Example icons: magnifying glass (Search), book stack (Register), quill pen (Review), tag/folder (Classify), lightbulb (Insights), clock/timeline bar (Timeline), web/graph nodes (Relation Network), checkmark (Validate), code brackets (HTML), rocket (Deploy)
- Decision diamonds for mode switches (--update, --category, --timeline) with minimal labels
- Fan-out / fan-in arrows for parallel operations
- Dashed lines for optional/skippable paths
- White background, clean modern style, soft rounded shapes
- NO verbose descriptions in boxes — icons speak louder than words
- NO title text, NO watermarks, NO color name labels
- English only
"""

# Script name → (keyword, color, cat description, fairy description)
# Used to dynamically generate per-step character descriptions
_CHARACTER_DB = {
    "search_papers":           ("Search",    "blue",    "orange tabby wearing tiny detective hat, holds magnifying glass, curious wide eyes", "holds a magnifying glass, blue wings"),
    "register_zotero":         ("Register",  "green",   "tuxedo cat with round glasses, carries a stack of tiny books on its head", "carries a tiny book stack, green wings"),
    "sync_zotero":             ("Sync",      "green",   "tuxedo cat checking a pocket watch, syncing two book piles", "syncs two floating book stacks, green wings"),
    "run_update_force":        ("Review",    "orange",  "fluffy white cat wearing a beret, writes with a quill pen, ink spot on nose", "writes with a quill pen, orange wings"),
    "build_papers_index":      ("Index",     "amber",   "Abyssinian cat stacking tiny index cards into a filing cabinet", "sorts floating index cards, amber wings"),
    "classify_papers":         ("Classify",  "red",     "calico cat sorting colorful paper cards with both paws, focused expression", "sorts colorful cards, red wings"),
    "build_category_summaries":("Summarize", "coral",   "Siamese cat wearing a monocle, connecting yarn threads on a corkboard", "connects threads between stars, coral wings"),
    "extract_insights":        ("Insights",  "rose",    "Ragdoll cat with a magnifying glass studying a web of connected papers", "traces glowing lines between paper clusters, rose wings"),
    "generate_timelines":      ("Timeline",  "purple",  "gray Russian Blue with a tiny paintbrush in mouth, palette on tail", "holds a paintbrush, purple wings"),
    "generate_network":        ("Network",   "teal",    "Bengal cat sitting in the center of a glowing web, tapping connected nodes with paws", "weaves a glowing web between nodes, teal wings"),
    "generate_workflow":       ("Workflow",  "violet",  "Persian cat in a tiny director's chair, orchestrating the other cats", "conducts an orchestra of tiny diagrams, violet wings"),
    "validate_papers":         ("Validate",  "yellow",  "Scottish Fold with a tiny clipboard and green checkmark stamp", "has a checklist and checkmark stamp, yellow wings"),
    "review_to_html":          ("HTML",      "lime",    "Munchkin cat typing on a tiny keyboard, HTML tags floating around", "types on a floating keyboard, lime wings"),
    "build_topic_index":       ("TopicIndex","indigo",  "Maine Coon arranging tiny paper cards into a neat grid, proud expression", "arranges tiny cards into a grid, indigo wings"),
    "prepare_deploy":          ("Deploy",    "gray",    "black cat riding a tiny rocket, goggles on forehead, tail streaming behind", "rides a tiny rocket, silver wings"),
}

# Cat breeds cycle for unknown scripts
_CAT_BREEDS = ["Sphynx", "Norwegian Forest", "British Shorthair", "Birman", "Chartreux",
               "Turkish Van", "Singapura", "Korat", "Havana Brown", "Tonkinese"]
_EXTRA_COLORS = ["pink", "mint", "peach", "sage", "lavender", "gold", "slate", "sky", "plum", "sand"]


def _build_characters_from_phases(phases, style):
    """Parse pipeline phases and generate character descriptions dynamically."""
    characters = []
    unknown_idx = 0

    for phase in phases:
        # Extract script name: "Step 0a: search_papers.py" → "search_papers"
        m = re.match(r'Step\s+[\d.]+[ab]?:\s+(\S+?)(?:\.py)?$', phase.split('\n')[0])
        if not m:
            continue
        script = m.group(1)

        if script in _CHARACTER_DB:
            keyword, color, cat_desc, fairy_desc = _CHARACTER_DB[script]
        else:
            # Generate for unknown scripts
            keyword = script.replace('_', ' ').title().split()[0]
            color = _EXTRA_COLORS[unknown_idx % len(_EXTRA_COLORS)]
            breed = _CAT_BREEDS[unknown_idx % len(_CAT_BREEDS)]
            cat_desc = f"{breed} cat working on {script.replace('_', ' ')}, determined expression"
            fairy_desc = f"works on {script.replace('_', ' ')}, {color} wings"
            unknown_idx += 1

        if style == "cat":
            characters.append(f"  - {keyword} cat: {cat_desc}")
        elif style == "fairy":
            characters.append(f"  - {keyword} fairy: {fairy_desc}")

    return characters


def build_style_text(phases, style):
    """Build dynamic style text from parsed pipeline phases."""
    if style == "default":
        return ""

    characters = _build_characters_from_phases(phases, style)
    char_list = "\n".join(characters)

    if style == "cat":
        return f"""
### CUTE CAT AGENT CHARACTERS (IMPORTANT!)
- Each pipeline phase has an adorable cat agent character sitting on, beside, or interacting with the phase box
- Cats are small chibi/kawaii style, each with a distinct look matching their role:
{char_list}
- NO speech bubbles — the cat's action IS the phase (cat with magnifying glass = Search, cat with quill = Review)
- Cats may have small accessories: scarves, bow ties, or tiny hats matching their phase color
- Style: flat kawaii illustration, soft pastel colors, round shapes, consistent size across all cats
- Cats ARE the icons — each cat's pose/action replaces a traditional icon
- Small paw prints or yarn balls as decorative connectors between phases
"""
    elif style == "fairy":
        return f"""
### FAIRY AGENT CHARACTERS (IMPORTANT!)
- Each pipeline phase has a cute fairy agent character sitting on or beside the phase box
- Fairies are tiny (chibi/kawaii style), each with a distinct look matching their role:
{char_list}
- Fairies should be charming but not distract from the pipeline flow
- Each fairy has a tiny speech bubble with one keyword (e.g., "Search!", "Review!", "Deploy!")
- Style: flat illustration, pastel colors, consistent size across all fairies
"""
    return ""


def main():
    parser = argparse.ArgumentParser(description="Generate paper-curation workflow diagram")
    parser.add_argument("--candidates", type=int, default=5)
    parser.add_argument("--style", default="default", choices=["default", "cat", "fairy"],
                        help="Visual style preset (default, cat, fairy)")
    args = parser.parse_args()

    from lib.paperbanana import generate_diagram
    from datetime import datetime
    import shutil

    def log(msg):
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"[{ts}] {msg}", flush=True)

    # Build METHOD_TEXT from README.md + CLAUDE.md
    log("Building METHOD_TEXT from README.md + CLAUDE.md...")
    pipeline_text = build_method_text()

    # Extract phases for dynamic character generation
    phases = [l for l in pipeline_text.split('\n') if l.startswith('Step ')]
    style_text = build_style_text(phases, args.style)
    method_text = pipeline_text + VISUAL_RULES + style_text

    log(f"METHOD_TEXT: {len(method_text)} chars")
    log(f"Style: {args.style}")
    log(f"Generating {args.candidates} workflow candidates (21:9, PaperBanana)")

    caption = ("Paper Curation Pipeline: end-to-end automated system with Zotero sync, "
               "multi-source search, review generation, classification, validation, "
               "timeline generation, and GitHub Pages deployment.")

    os.makedirs(WORKFLOW_DIR, exist_ok=True)

    results = []
    for i in range(1, args.candidates + 1):
        out_path = str(WORKFLOW_DIR / f"workflow_{i}.png")
        log(f"  Candidate #{i}...")
        try:
            png_bytes = generate_diagram(
                method=method_text,
                caption=caption,
                aspect_ratio="21:9",
                critic_rounds=3,
                exp_mode="demo_planner_critic",
                retrieval_setting="auto",
                output_path=out_path,
            )
            if png_bytes and os.path.exists(out_path):
                kb = os.path.getsize(out_path) / 1024
                log(f"  #{i}: {kb:.0f}KB")
                results.append((i, kb, out_path))
            else:
                log(f"  #{i}: FAILED (PaperBanana returned None)")
        except Exception as e:
            log(f"  #{i}: ERROR {str(e)[:100]}")
        time.sleep(2)

    if results:
        log(f"\nDeploying #{results[0][0]} as workflow.png")
        shutil.copy2(results[0][2], str(WORKFLOW_DIR / "workflow.png"))

    log(f"\nDone! {len(results)}/{args.candidates} successful")
    log(f"Files: {WORKFLOW_DIR}")


if __name__ == "__main__":
    main()
