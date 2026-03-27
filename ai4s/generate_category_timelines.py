"""
Generate detailed T-3c method texts for all 8 categories and produce
category timeline images via PaperBanana.

Run:  PYTHONUTF8=1 python generate_category_timelines.py
"""
import json
import os
import re
import sys
import time
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────
WORK_DIR = Path(r"C:\Users\jehyu\Arbeitplatz\paper-curation\ai4s")
OUTPUT_DIR = Path(r"C:\Users\jehyu\Arbeitplatz\claude_output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PAPERBANANA_LIB = Path(r"C:\Users\jehyu\Arbeitplatz\01_Work\01_Devs\AX\scisci\scie")
sys.path.insert(0, str(PAPERBANANA_LIB))


# ── Load data ──────────────────────────────────────────────────────────────
def load_data():
    with open(WORK_DIR / "_all_papers.json", encoding="utf-8") as f:
        all_papers = json.load(f)
    with open(WORK_DIR / "_new_classification.json", encoding="utf-8") as f:
        cls = json.load(f)
    with open(WORK_DIR / "_timeline_narrative.json", encoding="utf-8") as f:
        timeline = json.load(f)

    paper_map = {p["slug"]: p for p in all_papers}

    cat_papers: dict[str, list] = {}
    for assign in cls["assignments"]:
        cat = assign["primary_category"]
        slug = assign["slug"]
        if cat not in cat_papers:
            cat_papers[cat] = []
        if slug in paper_map:
            cat_papers[cat].append(paper_map[slug])

    return cat_papers, timeline["category_analyses"]


# ── Gemini Flash method text generation ───────────────────────────────────
def generate_method_text(cat_name: str, papers: list, sub_themes: list) -> str:
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

    papers_sorted = sorted(papers, key=lambda p: str(p.get("date", "2020")))

    paper_lines = []
    for p in papers_sorted:
        essence_short = (p.get("essence") or "")[:150].replace("\n", " ")
        paper_lines.append(f"- [{p['date']}] {p['title']} — {essence_short}")
    paper_list_text = "\n".join(paper_lines)

    sub_theme_hints = "\n".join(
        f"  • {t['name']} ({t['start_year']}→{t.get('peak_year','?')}, {t['status']}): {t['description']}"
        for t in sub_themes
    )

    years = sorted(set(str(p.get("date", "2020")) for p in papers_sorted))
    year_start = years[0] if years else "2018"
    year_end = years[-1] if years else "2026"

    prompt = f"""You are a science historian and data visualization expert.
Analyze these {len(papers)} papers in the "{cat_name}" category of AI for Science, sorted chronologically.

Papers ({year_start}–{year_end}):
{paper_list_text}

Existing sub-theme hints (use as starting context, but enhance significantly with paper evidence):
{sub_theme_hints}

Generate a detailed research evolution method text following this EXACT structure.
ALL text must be in English only.

---
## Category Timeline: {cat_name} ({year_start}–{year_end}) — Detailed Research Evolution

### SUB-THEME A: [name] ([start_year]→[end_year], [STATUS])
Branches into:
- **"[sub-sub-theme-1]"** ([start]–[end]): [2-3 sentence description citing specific paper titles and tool/framework names from the list above]
- **"[sub-sub-theme-2]"** ([start]–[end]): [description with paper/tool names]
- **"[sub-sub-theme-3]"** ([start]–[end]): [description with paper/tool names]
- **"[sub-sub-theme-4]"** ([start]–[end]): [description with paper/tool names]
- **"[sub-sub-theme-5]"** ([start]–[end]): [optional, description]
Interaction: [describe using MERGE/FEED/SPAWN/ENABLE/RESPOND verbs how this sub-theme relates to others]

### SUB-THEME B: [name] ([start_year]→[end_year], [STATUS])
Branches into:
- **"[sub-sub-theme-1]"** ([start]–[end]): [description with paper/tool names]
- **"[sub-sub-theme-2]"** ([start]–[end]): [description]
- **"[sub-sub-theme-3]"** ([start]–[end]): [description]
- **"[sub-sub-theme-4]"** ([start]–[end]): [description]
Interaction: [MERGE/FEED/SPAWN/ENABLE/RESPOND description]

### SUB-THEME C: [name] ([start_year]→[end_year], [STATUS])
Branches into:
- **"[sub-sub-theme-1]"** ([start]–[end]): [description]
- **"[sub-sub-theme-2]"** ([start]–[end]): [description]
- **"[sub-sub-theme-3]"** ([start]–[end]): [description]
- **"[sub-sub-theme-4]"** ([start]–[end]): [description]
Interaction: [MERGE/FEED/SPAWN/ENABLE/RESPOND description]

[Add SUB-THEME D if warranted by the data]

### CROSS-CUTTING CONNECTIONS
- [specific connection between sub-themes A and B with year and mechanism]
- [specific connection between sub-themes B and C]
- [any paradigm-level convergence or divergence with year]

### KEY MILESTONES (annotation boxes)
- **[year]: [event name]** — [1-2 sentence significance, cite paper if applicable]
- **[year]: [event name]** — [significance]
- **[year]: [event name]** — [significance]
▶ [sub-field] emerges ([year])
▶ [sub-field] emerges ([year])
◀ [field] absorbed into [other] ([year]) [only if applicable based on data]
---

Requirements:
- Identify exactly 3-4 major sub-themes directly evidenced by the paper list.
- Each sub-theme must have 4-6 sub-sub-themes named with specific paper titles or framework names.
- STATUS must be one of: EMERGING, ACCELERATING, CONVERGING, DECLINING, STABLE.
- Use MERGE/FEED/SPAWN/ENABLE/RESPOND verbs in every Interaction block.
- Show temporal evolution: which sub-sub-themes appeared first, which faded, which grew.
- Include 3-4 Key Milestones as turning points or paradigm shifts.
- Total length: 2500-4000 characters.
- ALL text in English only — no Korean, no other languages.
"""

    resp = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,
            max_output_tokens=8192,
        ),
    )
    return resp.text


# ── Safe filename ──────────────────────────────────────────────────────────
def safe_name(cat_name: str) -> str:
    return re.sub(r"[^\w]+", "_", cat_name).strip("_")


# ── PaperBanana diagram generation ────────────────────────────────────────
def generate_via_paperbanana(cat_name: str, method_text: str, output_path: Path) -> bool:
    from lib.paperbanana import generate_diagram

    print(f"  [PaperBanana] Starting generation for: {cat_name}")
    try:
        png_bytes = generate_diagram(
            method=method_text,
            caption=f"Category Timeline: {cat_name}",
            aspect_ratio="16:9",
            critic_rounds=3,
            exp_mode="demo_planner_critic",
            retrieval_setting="auto",
            output_path=str(output_path),
        )
        if png_bytes and len(png_bytes) > 10_000:
            print(f"  [PaperBanana] OK — {len(png_bytes)//1024}KB → {output_path.name}")
            return True
        print(f"  [PaperBanana] Returned empty/tiny image for {cat_name}")
        return False
    except Exception as e:
        print(f"  [PaperBanana] ERROR: {e}")
        return False


# ── Gemini image generation fallback ─────────────────────────────────────
def generate_via_gemini_image(cat_name: str, method_text: str, output_path: Path) -> bool:
    try:
        from google import genai
        from google.genai import types
        import base64

        client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

        image_prompt = f"""Create a research timeline visualization for the category "{cat_name}" in AI for Science research.

Diagram style:
- River delta / Sankey-like organic flowing ribbons
- Horizontal orientation, left→right, year axis labeled on top
- White background, clean sans-serif font, 16:9 wide format
- Band WIDTH indicates activity level (wider = more active, narrower = declining)
- Every ribbon labeled with its sub-theme name
- English text only
- NO title, NO watercolor, NO paper counts, NO paper titles
- NEVER write color names as text labels

Research evolution data to visualize:
{method_text}

Render as a clean professional scientific visualization following all rules above.
"""

        resp = client.models.generate_content(
            model="gemini-3.1-flash-image-preview",
            contents=image_prompt,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE", "TEXT"],
            ),
        )

        for part in resp.candidates[0].content.parts:
            if hasattr(part, "inline_data") and part.inline_data:
                img_data = part.inline_data.data
                if isinstance(img_data, str):
                    img_data = base64.b64decode(img_data)
                output_path.write_bytes(img_data)
                print(f"  [Gemini image] OK — {len(img_data)//1024}KB → {output_path.name}")
                return True

        print(f"  [Gemini image] No image part in response for {cat_name}")
        return False
    except Exception as e:
        print(f"  [Gemini image] ERROR: {e}")
        return False


# ── Main ───────────────────────────────────────────────────────────────────
def main():
    print("Loading data...")
    cat_papers, cat_analyses = load_data()

    categories = [
        "Autonomous Agents & Research Workflow",
        "Ethics, Policy & Meta-Science",
        "Physical Sciences & Engineering",
        "Scientific NLP & Document Intelligence",
        "Scientific Foundation Models",
        "Benchmarks & Evaluation",
        "Life Sciences & Molecular Discovery",
        "Other",
    ]

    results = []

    for i, cat_name in enumerate(categories, 1):
        print(f"\n{'='*60}")
        print(f"[{i}/{len(categories)}] {cat_name}")
        print(f"{'='*60}")

        papers = cat_papers.get(cat_name, [])
        sub_themes = cat_analyses.get(cat_name, {}).get("sub_themes", [])
        print(f"  Papers: {len(papers)}, existing sub-themes: {len(sub_themes)}")

        safe = safe_name(cat_name)
        method_path = OUTPUT_DIR / f"_method_text_{safe}.txt"
        image_path = OUTPUT_DIR / f"category_timeline_{safe}.png"

        # Step 1: Generate (or reuse) detailed method text via Gemini Flash
        if method_path.exists():
            print(f"  [Gemini Flash] Reusing: {method_path.name}")
            method_text = method_path.read_text(encoding="utf-8")
        else:
            print(f"  [Gemini Flash] Generating method text ({len(papers)} papers)...")
            try:
                method_text = generate_method_text(cat_name, papers, sub_themes)
                method_path.write_text(method_text, encoding="utf-8")
                print(f"  [Gemini Flash] Saved {len(method_text)} chars → {method_path.name}")
            except Exception as e:
                print(f"  [Gemini Flash] FAILED: {e}")
                results.append((cat_name, "method_failed", None))
                continue

        # Step 2: Generate image
        if image_path.exists() and image_path.stat().st_size > 10_000:
            print(f"  [Image] Already exists ({image_path.stat().st_size//1024}KB), skipping.")
            results.append((cat_name, "skipped", image_path))
        else:
            success = generate_via_paperbanana(cat_name, method_text, image_path)
            if not success:
                print(f"  [Fallback] PaperBanana failed, trying Gemini image generation...")
                success = generate_via_gemini_image(cat_name, method_text, image_path)
            results.append((cat_name, "ok" if success else "failed", image_path if success else None))

        if i < len(categories):
            print("  Waiting 5s...")
            time.sleep(5)

    # ── Summary ────────────────────────────────────────────────────────────
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    for cat_name, status, path in results:
        icon = "OK  " if status in ("ok", "skipped") else "FAIL"
        fname = path.name if path else "—"
        print(f"  [{icon}] {cat_name:<45}  {fname}")
    print(f"\nOutput: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
