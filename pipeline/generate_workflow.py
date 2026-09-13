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
        r'\|\s*([\d.]+[ab]?|Entry|Recover)\s*\|\s*`([^`]+)`\s*\|\s*(.+?)\s*\|',
        steps_section
    ):
        step, script, description = m.groups()
        # Strip path/extension so file names never reach the diagram prompt.
        # e.g. `pipeline/run_update_force.py` → `run_update_force`
        script = re.sub(r'^pipeline/', '', script)
        script = re.sub(r'\.py$', '', script)
        phases.append(f"Step {step}: {script}\n  {description.strip()}")

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

    # 6. Workflow mermaid block (English version preferred — has the latest
    #    multi-backend + Audio Overview + Worker function nodes the table
    #    above doesn't surface). Strip the ```mermaid fences so the LLM
    #    sees raw nodes/edges.
    mermaid_section = _extract_section(readme, "Workflow")
    if not mermaid_section:
        mermaid_section = _extract_section(readme, "워크플로우")
    mermaid_block = ""
    m = re.search(r'```mermaid\s*\n(.*?)\n```', mermaid_section, re.DOTALL)
    if m:
        mermaid_block = m.group(1).strip()

    method = f"""## Paper Curation Pipeline — Zotero + Claude Code + Deep Research + Obsidian

### TOOL ECOSYSTEM (show as interconnected logos/icons at the top)
The system is orchestrated by **Claude Code** (Anthropic's CLI agent) which coordinates five tools:
- **Zotero** (reference manager, red Z logo): paper collection, PDF storage, linked files
- **Claude** (Anthropic LLM, Anthropic logo): structured reviews (Haiku), topic naming (Sonnet), timeline narratives (Opus), Deep Research answers (Extended Thinking)
- **PaperBanana** (diagram engine, banana icon): auto-generates per-category research trend timeline diagrams from Claude Opus narratives
- **Obsidian** (knowledge IDE, purple gem logo): personal notes editing, [[wiki-links]] between papers, Graph View for cross-query knowledge topology
- **Google Gemini** (Google logo): gemini-embedding-001 for the Deep Research RAG index, figure validation, and Audio Overview TTS

Data flow: Zotero → Claude Code → Claude (review/classify) → PaperBanana (timelines) → Deep Research (RAG Q&A) → Obsidian (compounding knowledge)

Each tool MUST be represented by its recognizable logo/icon. Show Claude Code as the central orchestrator connecting all tools.

### CORE vs OPTION (CRITICAL — must be visually distinguishable!)
The pipeline has two tiers. The diagram MUST make the tier of every element obvious at a glance:
- **CORE (always runs, solid style)**: data collection → structured review → topic modeling/classification → Related Papers connections → category summaries + timelines → Deep Research index → topic index page → local browsing (serve_local) → in-browser Deep Research + Audio Overview.
- **OPTION (opt-in, dashed-border zones, each zone labeled with a small "OPTION" badge/ribbon)**:
  * O-1 Content Deploy (`--mode deploy`): Cloudflare Workers + gh-pages redirect stubs + Resend email delivery
  * O-2 Research Insights + Network (`--insights`): cross-category insights analysis + interactive network visualization
  * Workflow diagram generation (this very diagram, standalone)
- Core flow uses solid arrows/borders; every Option element lives inside a clearly dashed enclosure with an "OPTION" tag. A reader must instantly see "this part is optional".

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

### CANONICAL WORKFLOW GRAPH (use this as the source of truth — every
### node and edge here MUST appear in the diagram, including the
### in-browser Deep Research multi-backend choice, the Audio Overview
### node, the Cloudflare Worker `/api/audio-email` function, the Resend
### email send, and the Local-vs-Deploy fork)
{mermaid_block}

### IN-BROWSER FEATURES (must be visible in the diagram, separate from
### the build-time pipeline above)
- Deep Research: client-side natural-language Q&A. Detects user-pasted
  API key by prefix and routes to ONE OF Anthropic (sk-ant-…) /
  OpenAI (sk-…) / Google (AIza…) — three logos shown as a fan-in choice.
- Audio Overview: in-browser podcast generation. Calls Gemini TTS,
  encodes MP3 client-side, downloads locally AND (on deployed Worker)
  POSTs to /api/audio-email → Resend → email with MP3 attachment.

### DELIVERY FORK (must appear as a clear branching point)
- LOCAL: `python -m http.server` — full text.md available, richer Deep
  Research, no email delivery.
- DEPLOY: Cloudflare Workers serves docs/ + Worker function handles
  /api/audio-email. gh-pages redirect stubs forward visitors from
  jehyunlee.github.io/paper-curation/{{topic}}/ to the Worker URL.
"""
    return method


VISUAL_RULES_DEFAULT = """
### ABSOLUTE VISUAL RULES
- Left to right flow, 21:9 ultra-wide aspect ratio
- Each phase box: SHORT label (1-2 words max) + a representative ICON/CLIPART inside or beside it
- Phase labels must be minimal: "Search", "Register", "Review", "Classify", "Insights", "Timeline", "Network", "Validate", "HTML", "Deep Research", "Obsidian"
- Icons/cliparts are the primary visual — text is secondary
- Example icons: magnifying glass (Search), book stack (Register), quill pen (Review), tag/folder (Classify), lightbulb (Insights), clock/timeline bar (Timeline), web/graph nodes (Network), checkmark (Validate), code brackets (HTML), brain/sparkle (Deep Research), purple gem (Obsidian)
- Decision diamonds for mode switches (--update, --category, --timeline) with minimal labels
- Fan-out / fan-in arrows for parallel operations
- Dashed lines for optional/skippable paths
- CORE vs OPTION: Core flow solid; every OPTION group (Deploy O-1, Insights+Network O-2,
  Workflow diagram) inside a dashed rounded enclosure with a small
  "OPTION" ribbon/badge on its corner — instantly distinguishable from the Core flow
- White background, clean modern style, soft rounded shapes
- NO verbose descriptions in boxes — icons speak louder than words
- NO title text, NO watermarks, NO color name labels
- English only
- Show recognizable logos/icons for these tools near the stages they power:
  * Claude Code (Anthropic terminal CLI icon) — central orchestrator
  * Zotero (red Z logo) — paper source
  * Claude (Anthropic logo) — LLM review/classify/insights/Deep Research
  * PaperBanana (banana icon) — timeline diagram generation
  * Obsidian (purple gem icon) — knowledge compounding destination
  * Google Gemini (Google logo) — Deep Research embeddings + figure validation + TTS
"""

VISUAL_RULES_ACADEMIC = """
### ABSOLUTE VISUAL RULES — ACADEMIC PAPER FIGURE
The diagram must look like a *method overview figure* from a top-tier ML/NLP conference
paper (NeurIPS/ICML/ACL). Serious, restrained, information-dense.

LAYOUT
- Left-to-right horizontal flow, 21:9 ultra-wide aspect ratio
- Four swim lanes stacked vertically, left-to-right logical flow inside each lane:
  1. ACQUIRE  (Web search → Zotero registration → Sync → Dedup)
  2. REVIEW   (PDF → Text+Figures → Sanity gate → Structured review)
  3. ANALYZE  (Embedding → Cluster assignment → Category summaries → Cross-category insights → Timeline narrative)
  4. DELIVER  (Validate → Topic page → Search index → Deploy / Recovery audit)

NODE STYLE
- Rectangles with thin 1.5px black borders, subtle off-white fill (#F7F7F5)
- Short 1-3 word concept labels in bold serif (e.g. "Embedding", "Cluster Assignment", "Sanity Gate")
- NO filenames, NO .py, NO command-line flags, NO script paths
- Optional: tiny monochrome pictogram (magnifying glass, document, graph node) in node corner — not the primary visual
- Tool logos allowed ONLY as small badges next to the relevant lane label: Zotero, Claude, OpenAI, PaperBanana, Obsidian

EDGES
- Solid thin arrows for primary data flow
- Dashed arrows for optional / preflight paths (dedup preflight, audit recovery)
- CORE vs OPTION: Core nodes/edges solid; OPTION groups (Deploy O-1, Insights+Network O-2)
  enclosed in thin dashed rounded rectangles, each with a small
  italic "Option" label at the enclosure corner
- Diamond decision nodes only for the 3-axis MECE mode gate
  ("mode: curate / rebuild / reclassify / retime / deploy")
- No thick colored edges; monochrome black arrows

ANNOTATIONS
- Below each lane, a thin italic one-line caption describing what that lane produces
  (e.g. "structured Korean reviews with extracted figures", "hybrid node-based classification")
- Top-left: small bold serif title "Paper Curation Pipeline"
- Bottom-right: tiny italic "single entrypoint orchestrates all stages"
- English only, no color names, no watermarks

PALETTE
- Mostly grayscale (#000 / #333 / #666 / #F7F7F5)
- Accent: at most two muted academic colors (#2C5F9E navy, #B23A3A brick) used sparingly
  — one for the sanity/validate gates, one for the LLM/embedding nodes
- No neon, no gradients, no drop shadows

FORBIDDEN
- No cartoon characters, mascots, emojis, chibi figures
- No gradients, glow, neon, 3D effects
- No file names, no argparse flags, no code snippets, no bracketed command args
- No long sentences inside nodes
"""

# Script name → (keyword, color, cat description, fairy description)
# Used to dynamically generate per-step character descriptions
_CHARACTER_DB = {
    "run_full":                ("Orchestrate","navy",   "majestic silver tabby conductor with a tiny baton, standing on a podium directing all other cats", "conducts with a glowing baton, navy wings"),
    "dedup_zotero":            ("Dedup",     "cyan",    "twin-spotting Japanese Bobtail holding two identical papers side by side, one eyebrow raised", "compares two identical scrolls, cyan wings"),
    "cleanup":                 ("Cleanup",   "mint",    "tidy white cat with a tiny broom, sweeping stale files into a small bin", "sweeps sparkles into a bin, mint wings"),
    "prepare_deploy":          ("Deploy",    "sky",     "adventurous cat in a tiny astronaut helmet, launching a paper-airplane rocket to a cloud", "launches a paper rocket to a cloud, sky wings"),
    "audit_matching":          ("Audit",     "slate",   "sharp-eyed Sherlock cat with deerstalker hat, comparing two documents with a magnifier", "inspects mismatched scrolls, slate wings"),
    "fix_matching":            ("Fix",       "copper",  "handy cat with a tiny wrench and tool belt, repairing a broken paper link", "repairs a broken link with a wrench, copper wings"),
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
    "build_search_index":      ("Deep Research", "indigo", "wise owl-eyed cat with glowing brain, surrounded by floating search queries and citation badges", "has a glowing brain aura, indigo wings"),
    "obsidian_notes":          ("Obsidian",  "purple",  "mystical black cat holding a purple gem (Obsidian logo), wiki-link threads radiating from it, sitting on a stack of personal notes", "holds a purple gem, radiating wiki-link threads, purple wings"),
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
    if style in ("default", "academic"):
        # academic / default 는 캐릭터 추가 없이 VISUAL_RULES 단독으로 사용.
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
- CORE vs OPTION (IMPORTANT): Core cats sit along the main solid path. OPTION features
  (Deploy O-1, Research Insights + Network O-2) are dashed-fence
  "play pens" — each pen has a tiny wooden sign reading "OPTION", and the cats inside
  wear a small star-shaped name tag. A reader must instantly see which cats are optional.
"""
    elif style == "fairy":
        return f"""
### FAIRY AGENT CHARACTERS (IMPORTANT!)
- Each pipeline phase has a cute fairy agent character sitting on or beside the phase box
- Fairies are tiny (chibi/kawaii style), each with a distinct look matching their role:
{char_list}
- Fairies should be charming but not distract from the pipeline flow
- Each fairy has a tiny speech bubble with one keyword (e.g., "Search!", "Review!", "Research!")
- Style: flat illustration, pastel colors, consistent size across all fairies
"""
    return ""


def main():
    parser = argparse.ArgumentParser(description="Generate paper-curation workflow diagram")
    parser.add_argument("--candidates", type=int, default=5)
    parser.add_argument("--style", default="academic",
                        choices=["default", "cat", "fairy", "academic"],
                        help="Visual style preset. academic = serious paper figure (no characters, no filenames)")
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
    visual_rules = VISUAL_RULES_ACADEMIC if args.style == "academic" else VISUAL_RULES_DEFAULT
    method_text = pipeline_text + visual_rules + style_text

    log(f"METHOD_TEXT: {len(method_text)} chars")
    log(f"Style: {args.style}")
    log(f"Generating {args.candidates} workflow candidates (21:9, PaperBanana)")

    caption = ("Paper Curation Pipeline: Claude Code orchestrates Zotero (paper source), "
               "Claude (AI reviews, classification, related-papers connections, Deep Research), "
               "PaperBanana (category trend timelines), Google Gemini (embedding index, "
               "figure validation, TTS), and Obsidian (knowledge compounding). "
               "Core stages flow solid; Option zones (Deploy O-1, Insights+Network O-2, "
               "Workflow diagram) are dashed enclosures labeled OPTION.")

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
        log(f"\nSelecting #{results[0][0]} as workflow.png")
        shutil.copy2(results[0][2], str(WORKFLOW_DIR / "workflow.png"))

    log(f"\nDone! {len(results)}/{args.candidates} successful")
    log(f"Files: {WORKFLOW_DIR}")


if __name__ == "__main__":
    main()
