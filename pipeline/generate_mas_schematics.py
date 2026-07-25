"""Generate schematic diagrams of representative Multi-Agent System (MAS) topologies.

Grounded in corpus (ai4s) papers found via the Deep Research search index:
  - Hierarchical : RepurAgent (3134), SCION (10747), El Agente (308)
  - Round-table  : Mol-Debate (3172), LLM-MA survey (464), Xolver (10721)
  - Team         : Robin/Crow-Falcon-Finch (10726/2994), Heterogeneous team (10718)
  - Pipeline     : Robin discovery loop (10726), orchestrated theorem-proving sub-agents (10546)

Each schematic is a clean academic method-overview figure (no mascots, no filenames),
rendered by PaperBanana at 21:9 ultra-wide aspect ratio.

Usage:
    PYTHONUTF8=1 python pipeline/generate_mas_schematics.py            # all four
    PYTHONUTF8=1 python pipeline/generate_mas_schematics.py --only hierarchical round_table
"""

import argparse
import os
import sys
import time
from datetime import datetime
from pathlib import Path

from config_loader import PROJECT_ROOT
from lib.paperbanana import generate_diagram

OUT_DIR = PROJECT_ROOT / "pipeline" / "_img_mas"

# Shared academic-figure styling — clean schematic, no characters, no filenames.
VISUAL_RULES = """
### ABSOLUTE VISUAL RULES — ACADEMIC SCHEMATIC
The image must read like a *system-architecture schematic* from a top-tier ML/NLP
paper (NeurIPS/ICML/ACL). Serious, restrained, self-explanatory.

LAYOUT
- 21:9 ultra-wide aspect ratio, generous margins, no crowding.
- One clear topology per figure; the spatial arrangement itself must communicate the structure.

NODE STYLE
- Agents = rounded rectangles or circles with a thin 1.5px dark border and subtle
  off-white fill (#F7F7F5). Each agent has a SHORT 1-3 word role label in bold serif.
- A small monochrome pictogram (brain / magnifying glass / flask / document) may sit in a
  node corner, but text stays primary.
- Shared stores (blackboard / memory) = a distinct slightly shaded panel.

EDGES
- Solid thin arrows for primary message / data flow.
- Dashed arrows for feedback / return / aggregation paths.
- Bidirectional arrows where agents exchange messages as peers.
- Monochrome black arrows only — no thick colored edges.

PALETTE
- Mostly grayscale (#000 / #333 / #666 / #F7F7F5).
- At most two muted academic accents (#2C5F9E navy, #B23A3A brick), used sparingly to
  distinguish the coordinator/output role.

FORBIDDEN
- No cartoon characters, mascots, emojis, chibi figures.
- No gradients, glow, neon, 3D effects, drop shadows.
- No file names, no code, no command flags.
- English only. No watermarks.
"""

SPECS = {
    "hierarchical": {
        "title": "Hierarchical (Supervisor-Worker)",
        "caption": (
            "Hierarchical multi-agent system. A top-level supervisor recursively decomposes a "
            "goal into subtasks and delegates them down a tree of specialized worker agents; "
            "partial results aggregate back up to the supervisor. Coordination is top-down, "
            "context is split across layers (e.g. RepurAgent, SCION, El Agente)."
        ),
        "method": """
# Schematic: HIERARCHICAL Multi-Agent System (Supervisor -> Worker tree)

A rooted tree, drawn top-to-bottom, spanning the ultra-wide canvas.

NODES (top to bottom):
- LEVEL 0 (root, top-center, accent navy): "Supervisor / Orchestrator" — owns the overall goal.
- LEVEL 1 (single node under root): "Planner" — decomposes the goal into ordered subtasks.
- LEVEL 2 (a row of 4 sibling worker agents, evenly spread across the width):
  "Research", "Prediction", "Data", "Report". Each is a specialized agent with its own tools.
- LEVEL 3 (optional): one Level-2 worker fans out to 2 smaller "Sub-agent" leaves to show
  RECURSIVE decomposition continuing to deeper layers.

EDGES:
- Solid downward arrows from each parent to its children, labeled "delegate subtask".
- Dashed upward arrows from children back to parents, labeled "return result".
- A small curved self-loop annotation near Level 2 reading "recursive decomposition (depth <= 6)".

MESSAGE:
- The vertical depth of the tree = how deeply the task is decomposed.
- Only the supervisor sees the full objective; each worker sees only its local subtask,
  so total context far exceeds any single model's window.
""",
    },
    "hier_vs_roundtable": {
        "title": "Hierarchical vs Round-table (Comparison)",
        "caption": (
            "Two contrasting multi-agent topologies side by side. LEFT: a hierarchical "
            "supervisor-worker tree with top-down delegation and bottom-up aggregation "
            "(centralized control, decomposable tasks). RIGHT: a round-table peer debate where "
            "equal agents critique across rounds until a judge distills consensus (decentralized "
            "control, contested judgments). A comparison strip contrasts them axis by axis."
        ),
        "method": """
# Schematic: HIERARCHICAL vs ROUND-TABLE (single comparison figure)

One ultra-wide 21:9 canvas split into TWO panels by a thin vertical divider, plus a
comparison strip along the bottom. Each panel has a bold serif panel title at its top.

LEFT PANEL -- title "Hierarchical (Supervisor-Worker)":
- A rooted tree drawn top-to-bottom.
- Top (accent navy): "Supervisor". Below it: a row of 3 worker agents
  "Worker A", "Worker B", "Worker C".
- Solid downward arrows "delegate" from Supervisor to each worker.
- Dashed upward arrows "aggregate" from each worker back to Supervisor.
- One worker fans out to 2 small "Sub-agent" leaves to hint at recursion.
- Tiny italic tag under the panel: "centralized control, top-down".

RIGHT PANEL -- title "Round-table (Debate / Consensus)":
- 5 equal peer agents arranged in a circle ("Agent A".."Agent E"), all identical style.
- Bidirectional double-headed arrows forming a dense peer-to-peer mesh, tagged
  "argue / critique".
- A distinct node (accent brick) below the circle: "Judge" with a single solid arrow to
  an output box "Consensus".
- Tiny italic tag under the panel: "decentralized control, lateral".

BOTTOM COMPARISON STRIP -- a clean 2-column table (Hierarchical | Round-table),
one short row per axis:
- Control: "Centralized" | "Decentralized"
- Flow: "Vertical delegate/aggregate" | "Lateral critique rounds"
- Decision: "Supervisor decides" | "Judge distills consensus"
- Best for: "Decomposable tasks" | "Ambiguous / contested calls"
- Risk: "Supervisor bottleneck" | "Interaction tax / groupthink"

MESSAGE:
- The two panels must look visibly DIFFERENT in shape: a downward TREE on the left,
  a symmetric CIRCLE/MESH on the right. The contrast in geometry is the main point.
""",
    },
    "round_table": {
        "title": "Round-table (Debate / Peer Consensus)",
        "caption": (
            "Round-table debate. Peer agents of equal status exchange arguments and critiques "
            "over multiple rounds; a moderator/judge distills the converged consensus into a "
            "final answer. No hierarchy — influence flows laterally (e.g. Mol-Debate, LLM-MA "
            "debate paradigm, Xolver)."
        ),
        "method": """
# Schematic: ROUND-TABLE Multi-Agent System (Debate -> Consensus)

LEFT HALF — the round table:
- 5 peer agents arranged evenly AROUND a circle (a literal round table): label them
  "Agent A", "Agent B", "Agent C", "Agent D", "Agent E". All identical in size/style —
  they are equals, no hierarchy.
- Bidirectional double-headed arrows connect every adjacent pair AND cross the circle,
  forming a dense peer-to-peer mesh, annotated "argue / critique / defend".
- A small central token in the middle of the table: "Shared Proposition".

RIGHT HALF — convergence over rounds:
- Three stacked horizontal bands labeled "Round 1", "Round 2", "Round 3", showing the
  spread of opinions narrowing from wide (divergent) to tight (convergent).
- A distinct node (accent brick): "Judge / Moderator" reads the final round.
- A single solid arrow from the Judge to an output box: "Consensus Answer".

MESSAGE:
- Peers iterate laterally; disagreement is the mechanism, not a failure.
- Quality emerges from repeated critique rounds, then a judge collapses it to one answer.
""",
    },
    "team": {
        "title": "Team (Cooperative Specialists + Shared Blackboard)",
        "caption": (
            "Cooperative team. Heterogeneous specialist agents (literature, data analysis, "
            "domain expert, human-in-the-loop) read and write a shared workspace/blackboard, "
            "contributing complementary skills toward one goal without a strict command chain "
            "(e.g. Robin's Crow/Falcon/Finch, heterogeneous generalist+specialist+human team)."
        ),
        "method": """
# Schematic: TEAM Multi-Agent System (Cooperative specialists on a shared blackboard)

CENTER:
- A large shaded panel: "Shared Workspace / Blackboard (memory)". This is the hub everyone
  reads from and writes to.

AROUND THE HUB (hub-and-spoke, agents spread across the ultra-wide canvas):
- "Literature Agent" (magnifying-glass pictogram) — surveys prior work (like Crow / Falcon).
- "Data-Analysis Agent" (chart pictogram) — analyzes experimental data (like Finch).
- "Domain Specialist" (flask pictogram) — narrow expert model.
- "Human-in-the-loop" (person pictogram, accent navy) — oversight & approval.
- "Generalist Coordinator" (brain pictogram) — keeps the shared goal coherent.

EDGES:
- Every agent has a BIDIRECTIONAL read/write arrow to the central blackboard
  (post findings, pull others' contributions). No agent commands another.
- Thin dashed arrows between a couple of agents show occasional direct hand-offs.

MESSAGE:
- Flat, cooperative team: roles differ, status is equal.
- The shared blackboard is the single source of truth that fuses complementary skills.
""",
    },
    "pipeline": {
        "title": "Pipeline (Sequential Handoff / Assembly Line)",
        "caption": (
            "Sequential pipeline. Stage-specialized agents form an assembly line: each consumes "
            "the previous agent's artifact and produces the next, with a feedback loop closing "
            "the discovery cycle (e.g. Robin's hypothesis->experiment->analysis->revision loop, "
            "mechanically orchestrated theorem-proving sub-agents)."
        ),
        "method": """
# Schematic: PIPELINE Multi-Agent System (Sequential handoff)

LEFT-TO-RIGHT CHAIN (4 stage-agents evenly spaced across the ultra-wide canvas):
1. "Hypothesis" — generates candidate hypotheses.
2. "Experiment Design" — turns a hypothesis into an executable protocol.
3. "Data Analysis" — runs/interprets the experiment's data.
4. "Revision" — revises hypotheses from the evidence.

EDGES:
- Solid forward arrows between consecutive stages, each labeled with the artifact it carries:
  "hypothesis" -> "protocol" -> "results" -> "revised hypothesis".
- A single long DASHED feedback arrow from "Revision" back to "Hypothesis", labeled
  "iterate", closing the loop.
- Small tool badges under stages (database / instrument icons) show external resources tapped.

MESSAGE:
- Linear, ordered handoff — each agent owns exactly one stage.
- The dashed return arrow makes it a *cycle*, not a one-shot chain.
""",
    },
}


def log(msg: str) -> None:
    print(f"[{datetime.now():%H:%M:%S}] {msg}", flush=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate MAS topology schematics (21:9)")
    parser.add_argument("--only", nargs="*", choices=list(SPECS), default=list(SPECS),
                        help="Subset of topologies to render (default: all)")
    parser.add_argument("--critic-rounds", type=int, default=3)
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    log(f"Output dir: {OUT_DIR}")
    log(f"Rendering {len(args.only)} topology schematic(s) at 21:9")

    results = []
    for key in args.only:
        spec = SPECS[key]
        out_path = OUT_DIR / f"mas_{key}.png"
        method_text = f"# {spec['title']}\n{spec['method']}\n{VISUAL_RULES}"
        log(f"  [{key}] {spec['title']} ...")
        try:
            png = generate_diagram(
                method=method_text,
                caption=spec["caption"],
                aspect_ratio="21:9",
                critic_rounds=args.critic_rounds,
                exp_mode="demo_planner_critic",
                retrieval_setting="auto",
                output_path=str(out_path),
            )
            if png and out_path.exists():
                kb = out_path.stat().st_size / 1024
                log(f"  [{key}] OK -> {out_path.name} ({kb:.0f}KB)")
                results.append((key, out_path))
            else:
                log(f"  [{key}] FAILED (PaperBanana returned None)")
        except Exception as e:  # noqa: BLE001 - report and continue to next topology
            log(f"  [{key}] ERROR: {str(e)[:200]}")
        time.sleep(2)

    log(f"Done: {len(results)}/{len(args.only)} succeeded")
    for key, path in results:
        log(f"  - {key}: {path}")
    return 0 if len(results) == len(args.only) else 1


if __name__ == "__main__":
    sys.exit(main())
