from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parents[1]
OUT = str((HERE / "figures" / "concept.png").resolve())
sys.path.insert(0, str(PROJECT_ROOT / "pipeline"))

from lib.paperbanana import generate_diagram
method = """A clean side-by-side diagram that focuses PURELY on HOW two strategies for an LLM question-answering "wiki" over research-paper PDFs DIFFER mechanically. Do NOT include any pros/cons, strengths, limitations, or evaluation text — show only the process/data difference.

LEFT PIPELINE — "Curate, then Query" (paper-curation), top to bottom:
  1. a stack of PDF papers ->
  2. an "LLM Review (distill once)" box ->
  3. a "Curated Library" drawn as structured cards containing: short reviews, category tags, a small connection graph between papers, a timeline, and pre-extracted figure thumbnails ->
  4. a user question that retrieves only A FEW SHORT distilled snippets plus the ONE relevant pre-extracted figure ->
  5. a SMALL focused context box -> LLM -> Answer.

RIGHT PIPELINE — "Pile, then Query" (raw PDF stack), top to bottom:
  1. the same raw PDF papers piled directly into a "Vector Index" with NO curation step (mark the missing distill step clearly) ->
  2. a user question that retrieves SEVERAL LARGE RAW TEXT CHUNKS (full passages including references and equations; figures not handled) ->
  3. a LARGE raw context box -> LLM -> Answer.

Make the DIFFERENCES visually obvious by aligning matching stages at the same height and contrasting them:
  - distill step PRESENT (left) vs ABSENT (right);
  - "Curated Library = structured (reviews, categories, connections, timeline, figures)" (left) vs "Raw chunks = unstructured text" (right);
  - retrieved context = a few SMALL high-signal snippets + 1 figure (left) vs a few LARGE raw blocks, no figures (right);
  - context handed to the LLM = visibly SMALL (left) vs visibly LARGE (right).

Clean modern academic style: rounded boxes and directional arrows; BLUE palette for the left pipeline, ORANGE palette for the right; a faint vertical divider down the middle; small icons (document, database, figure) where helpful."""
caption = "Mechanical difference between the two LLM-wiki strategies: curate-and-distill once then retrieve small structured snippets plus a pre-extracted figure (paper-curation) versus pile raw PDFs and retrieve large raw text chunks (raw PDF stack)."
print("PB start", flush=True)
out = generate_diagram(method, caption, aspect_ratio="16:9", critic_rounds=1,
                       exp_mode="demo_planner_critic", retrieval_setting="none",
                       output_path=OUT)
print("PB ok ->", OUT if out else "FAILED", flush=True)
