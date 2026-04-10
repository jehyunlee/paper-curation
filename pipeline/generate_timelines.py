"""
PaperBanana 기반 타임라인 생성 스크립트 (Bottom-up, 3-step).

Step 1 (--narrative-only): 카테고리별 narrative + JSON summary 생성 → _category_narratives.json 저장
Step 2 (--images-only):    narrative + 편수 데이터 → PaperBanana 이미지 생성
Step 3 (기본):             Step 1 → Step 2 순차 실행

프로세스:
  Phase 1: 카테고리별 narrative 먼저 전부 생성 (Opus streaming)
    - 카테고리 내 논문 전체 분석 → 핵심 정보 JSON 저장
  Phase 2: narrative + 편수 → 카테고리 타임라인 이미지 생성 (PaperBanana)
  Phase 3: 카테고리 JSON 종합 → 메인 타임라인 이미지 생성 (PaperBanana)

핵심 원칙:
  - Narrative: Claude Opus (1M context, streaming)
  - 이미지: PaperBanana generate_diagram() 전용 (Gemini 직접 호출 금지)
  - 5 candidate 기본, #1 자동 배포
  - band width는 논문 편수를 정성적으로 반영 (정량 비례는 아님)

Usage:
  PYTHONUTF8=1 python generate_timelines.py --topic ai4s
  PYTHONUTF8=1 python generate_timelines.py --topic ai4s --candidates 10
  PYTHONUTF8=1 python generate_timelines.py --topic ai4s --narrative-only
  PYTHONUTF8=1 python generate_timelines.py --topic ai4s --images-only
  PYTHONUTF8=1 python generate_timelines.py --topic ai4s --main-only
  PYTHONUTF8=1 python generate_timelines.py --topic ai4s --category-only
"""

import argparse
import json
import os
import shutil
import sys
import time
from collections import defaultdict, Counter
from datetime import datetime
from pathlib import Path

# PaperBanana wrapper (config.json의 paperbanana_dir 경로 사용)
# generate_diagram() 사용: from lib.paperbanana import generate_diagram

from config_loader import PAPERS_DIR as _PAPERS_DIR, get_topic_dir, IMG_TIMELINES_DIR
from lib.categories import category_slug
PAPERS_DIR = str(_PAPERS_DIR)


def log(msg):
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


# ═══════════════════════════════════════════
# Step 1: Narrative Generation (Opus streaming)
# ═══════════════════════════════════════════

def opus_streaming_call(prompt, max_tokens=12000):
    """Opus streaming 호출. 10분 초과 방지."""
    from anthropic import Anthropic
    client = Anthropic()

    text = ""
    with client.messages.stream(
        model="claude-opus-4-20250514",
        max_tokens=max_tokens,
        temperature=0.3,
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        for chunk in stream.text_stream:
            text += chunk

    return text


def build_category_narrative(papers, topic, category):
    """카테고리 내 논문 전체를 Opus로 분석.
    Returns: (method_text, caption, summary_json)"""

    sorted_papers = sorted(papers, key=lambda p: p.get("year") or "9999")

    # Sub-category별 편수 집계
    sub_counts = Counter(p.get("sub_category", "General") for p in papers)
    sub_counts_text = "\n".join(
        f"  - {name}: {count} papers" for name, count in sub_counts.most_common()
    )

    paper_lines = []
    for p in sorted_papers:
        year = p.get("year", "?")
        title = p.get("title", "")[:80]
        essence = p.get("essence", "")[:200]
        sub = p.get("sub_category", "")
        paper_lines.append(f"- ({year}) [{sub}] {title} | {essence}")

    papers_text = "\n".join(paper_lines)

    prompt = f"""Analyze the following {len(papers)} papers in the "{category}" category of {topic}.

Sub-category paper counts (use these to inform relative band widths):
{sub_counts_text}

Papers (sorted by year):
{papers_text}

You must produce TWO outputs separated by "===JSON===":

OUTPUT 1 — METHOD TEXT for generating a timeline diagram:

## Category Timeline: {category}

### SUB-THEME A: {{sub_theme_name}} ({{start}}->{{end}}, {{status: ACCELERATING/STABLE/DECLINING/EMERGING}})
Relative size: {{LARGE/MEDIUM/SMALL based on paper count above}}
Branches into:
- **"{{sub_sub_theme_1}}"** ({{start}}-{{end}}): {{description with specific tool/framework names}}
- **"{{sub_sub_theme_2}}"** ({{start}}-{{end}}): {{description}}
Interaction: {{how this sub-theme relates to others. Use MERGE INTO / FEED INTO / SPAWN / ENABLE / RESPOND TO}}

(Repeat for each sub-theme. Identify sub-sub-themes 4-6 per sub-theme with specific paper/tool names.)

### CROSS-CUTTING CONNECTIONS
- {{connections between sub-themes}}

### KEY MILESTONES (annotation boxes)
- **{{year}}: {{label}}** — {{description}}
  Types: Turning Point / Paradigm Shift / Conceptual Shift

### EMERGENCE & DECLINE EVENTS
- ▶ {{field_name}} emerges ({{year}}): {{trigger}}
- ◀ {{field_name}} absorbed into {{other}} ({{year}})

### BAND WIDTH GUIDE
The following sub-themes should have proportionally wider/narrower bands:
{{List sub-themes from largest to smallest, with relative size indicators}}

### ABSOLUTE VISUAL RULES
- Horizontal timeline, left to right, years at top
- Sub-themes as smooth flowing ribbon/river streams with organic curves
- Band width should qualitatively reflect field size (larger fields = wider bands)
- Streams MUST interact: show merging, branching, influence — NO simple parallel bands
- All branches MUST have sub-category name labels — no unlabeled ribbons
- Mark emergence with ▶, decline with ◀
- White background, clean sans-serif font
- NO title in image, NO watermarks, NO color name text, NO specific paper counts
- 16:9 aspect ratio, English only

---

CAPTION:
A one-paragraph figure caption.

===JSON===

OUTPUT 2 — STRUCTURED SUMMARY (JSON) for reuse in main timeline:
{{
  "category": "{category}",
  "paper_count": {len(papers)},
  "sub_category_counts": {json.dumps(dict(sub_counts.most_common()), ensure_ascii=False)},
  "time_span": "YYYY-YYYY",
  "sub_themes": [
    {{
      "name": "sub-theme name",
      "paper_count": 0,
      "start": "YYYY",
      "end": "YYYY",
      "status": "ACCELERATING|STABLE|DECLINING|EMERGING",
      "relative_size": "LARGE|MEDIUM|SMALL",
      "key_developments": ["milestone 1", "milestone 2"],
      "representative_tools": ["tool1", "tool2"]
    }}
  ],
  "milestones": [
    {{"year": "YYYY", "label": "short label", "type": "Turning Point|Paradigm Shift|Conceptual Shift", "description": "what happened"}}
  ],
  "interactions": [
    {{"from": "sub-theme A", "to": "sub-theme B", "type": "MERGE|FEED|SPAWN|ENABLE|RESPOND", "description": "how"}}
  ],
  "emergence_decline": [
    {{"event": "emerge|decline", "field": "name", "year": "YYYY", "description": "why"}}
  ],
  "current_state_summary": "2-3 sentences describing where this category stands now and where it's heading"
}}
"""

    log(f"  Opus narrative (streaming): {len(papers)} papers in {category}...")
    text = opus_streaming_call(prompt)

    # Parse method text and JSON summary
    if "===JSON===" in text:
        parts = text.split("===JSON===", 1)
        method_part = parts[0].strip()
        json_part = parts[1].strip()
    else:
        method_part = text
        json_part = "{}"

    # Parse method + caption
    if "---" in method_part:
        mp = method_part.split("---", 1)
        method = mp[0].strip()
        caption = mp[1].strip()
        for prefix in ["CAPTION:", "SECTION 2:"]:
            caption = caption.replace(prefix, "").strip()
    else:
        method = method_part
        caption = f"Timeline for {category} in {topic} ({len(papers)} papers)."

    # Parse JSON summary
    try:
        jt = json_part.strip()
        if jt.startswith("```"):
            jt = jt.split("```")[1]
            if jt.startswith("json"):
                jt = jt[4:]
        summary = json.loads(jt)
    except (json.JSONDecodeError, IndexError):
        log(f"  WARNING: Failed to parse JSON summary for {category}")
        summary = {
            "category": category,
            "paper_count": len(papers),
            "sub_category_counts": dict(sub_counts.most_common()),
            "current_state_summary": caption[:200],
        }

    log(f"  Narrative: {len(method)} chars method, {len(json.dumps(summary))} chars summary")
    return method, caption, summary


def build_main_narrative_from_summaries(category_summaries, topic):
    """카테고리별 핵심 정보를 종합하여 메인 타임라인 narrative 생성."""

    # 카테고리별 편수 정보
    cat_sizes = "\n".join(
        f"  - {s.get('category', '?')}: {s.get('paper_count', 0)} papers"
        for s in category_summaries
    )

    summaries_text = json.dumps(category_summaries, indent=2, ensure_ascii=False)

    prompt = f"""You are given structured summaries of {len(category_summaries)} research categories in "{topic}".
Each summary contains sub-themes, milestones, interactions, emergence/decline events, and current state.

Category sizes (use these to inform relative band widths):
{cat_sizes}

Category Summaries:
{summaries_text}

Synthesize these into a MAIN RESEARCH TIMELINE method text.

Requirements:
- Each category becomes a STREAM (use the category name)
- Band width should qualitatively reflect category size (more papers = wider band)
- Show how categories influenced each other (use interaction data from summaries)
- Highlight TOP 5 most important milestones across all categories
- Show emergence of new categories and decline of approaches
- Use sub-theme info to add richness (key branches within each stream)

## Research Timeline: {topic}

### STREAM A: {{category_name}} ({{start}}->{{end}})
Relative size: {{LARGE/MEDIUM/SMALL based on paper count}}
Key branches: {{2-3 most important sub-themes from summary}}
- **"{{sub_theme}}"** ({{start}}-{{end}}): {{brief description}}
Status: {{current status from summary}}
Interaction: {{how this category relates to others}}

(Repeat for each category)

### BAND WIDTH GUIDE
Streams ordered by relative size (largest to smallest):
{{List categories with their approximate relative sizes}}

### CROSS-CUTTING THREADS
- {{patterns spanning multiple categories}}

### TURNING POINTS (annotation boxes — TOP 5)
- **{{year}}: {{label}}** — {{description}}

### ABSOLUTE VISUAL RULES
- Horizontal timeline, left to right, years at top
- Categories as smooth flowing ribbon/river streams with organic curves
- Band width qualitatively reflects field size (larger = wider, but not linearly proportional)
- Streams MUST interact: merging, branching, influence — NO simple parallel bands
- Key sub-themes shown as branches within category streams
- Mark emergence with ▶, decline with ◀
- White background, clean sans-serif font
- NO title in image, NO watermarks, NO color name text, NO specific paper counts
- 16:9 aspect ratio, English only

---

CAPTION:
A one-paragraph figure caption.
"""

    log(f"  Opus main narrative (streaming): synthesizing {len(category_summaries)} categories...")
    text = opus_streaming_call(prompt, max_tokens=10000)

    if "---" in text:
        parts = text.split("---", 1)
        method = parts[0].strip()
        caption = parts[1].strip()
        for prefix in ["CAPTION:", "SECTION 2:"]:
            caption = caption.replace(prefix, "").strip()
    else:
        method = text
        caption = f"Research timeline for {topic}."

    log(f"  Main narrative: {len(method)} chars method, {len(caption)} chars caption")
    return method, caption


def build_executive_summary(category_summaries, topic):
    """카테고리별 요약을 종합하여 executive summary (한국어) 생성."""

    summaries_text = json.dumps(category_summaries, indent=2, ensure_ascii=False)

    prompt = f"""당신은 "{topic}" 분야의 학술 연구 동향을 분석하는 전문가입니다.

아래는 {len(category_summaries)}개 카테고리별 연구 요약입니다:

{summaries_text}

위 내용을 바탕으로, 이 분야 전체의 연구 동향을 요약하는 **Executive Summary**를 한국어로 작성하세요.

요구사항:
- 분량: 800~1500자 (반드시 이 범위 안에서 작성할 것)
- 반드시 **완전한 문장으로 끝낼 것** (문장 도중에 끊기지 않도록)
- 시간순으로 주요 발전 흐름을 서술
- 대표적 연구/논문을 2~3개 구체적으로 언급 (저자, 연도 포함)
- 최근 트렌드와 향후 방향 포함
- 기술 용어는 영문 병기 (예: "과학의 과학(Science of Science)")
- 순수 한국어 산문만 출력. 마크다운, 제목, 번호 목록 없이 하나의 연속된 단락으로 작성
"""

    log(f"  Opus executive summary (streaming)...")
    text = opus_streaming_call(prompt, max_tokens=4000)

    # 잘림 검증: 마침표로 끝나지 않으면 마지막 완전한 문장까지 자르기
    text = text.strip()
    if text and not text.endswith(".") and not text.endswith("다."):
        last_period = max(text.rfind("다."), text.rfind(". "))
        if last_period > len(text) * 0.5:  # 절반 이상 살릴 수 있을 때만
            text = text[:last_period + 2].rstrip()
            log(f"  WARNING: executive summary truncated, trimmed to last complete sentence ({len(text)} chars)")

    log(f"  Executive summary: {len(text)} chars")
    return text


def save_timeline_narrative(topic_dir, executive_summary, category_summaries):
    """_timeline_narrative.json 저장."""
    # category_analyses 형식으로 변환
    category_analyses = {}
    for s in category_summaries:
        cat_name = s.get("category", "")
        if cat_name:
            category_analyses[cat_name] = {
                "sub_themes": s.get("sub_themes", [])
            }

    data = {
        "executive_summary_ko": executive_summary,
        "category_analyses": category_analyses,
    }

    path = os.path.join(topic_dir, "_timeline_narrative.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    log(f"  Saved: {path}")
    return path


# ═══════════════════════════════════════════
# Step 2: PaperBanana Image Generation
# ═══════════════════════════════════════════

def generate_with_paperbanana(method_text, caption, output_path, critic_rounds=3):
    """PaperBanana로 이미지 생성. Gemini 폴백 없음."""
    from lib.paperbanana import generate_diagram

    png_bytes = generate_diagram(
        method=method_text,
        caption=caption,
        aspect_ratio="16:9",
        critic_rounds=critic_rounds,
        exp_mode="demo_planner_critic",
        retrieval_setting="auto",
        output_path=output_path,
    )

    if png_bytes and os.path.exists(output_path):
        return os.path.getsize(output_path) / 1024
    return None


def generate_candidates(method_text, caption, prefix, candidates_dir, n=5):
    """N개 candidate 생성."""
    results = []
    for i in range(1, n + 1):
        out_path = os.path.join(candidates_dir, f"{prefix}_{i}.png")
        log(f"  Candidate #{i}...")
        try:
            kb = generate_with_paperbanana(method_text, caption, out_path)
            if kb:
                log(f"  #{i}: {kb:.0f}KB (PaperBanana)")
                results.append((i, kb, out_path))
            else:
                log(f"  #{i}: PaperBanana returned None (FAILED)")
        except Exception as e:
            log(f"  #{i}: ERROR {str(e)[:100]}")
        time.sleep(2)
    return results


def deploy_candidate(results, deploy_path):
    """첫 번째 성공 candidate를 배포."""
    if results:
        shutil.copy2(results[0][2], deploy_path)
        log(f"  -> Deployed #{results[0][0]} to {os.path.basename(deploy_path)}")
        return True
    log(f"  WARNING: No successful candidates!")
    return False


# ═══════════════════════════════════════════
# Main
# ═══════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="Generate timelines (bottom-up, 3-step)")
    parser.add_argument("--topic", default="ai4s")
    parser.add_argument("--candidates", type=int, default=5)
    parser.add_argument("--narrative-only", action="store_true", help="Step 1 only: generate narratives")
    parser.add_argument("--images-only", action="store_true", help="Step 2 only: generate images from existing narratives")
    parser.add_argument("--main-only", action="store_true", help="Main timeline only (requires narratives)")
    parser.add_argument("--category-only", action="store_true", help="Category timelines only")
    parser.add_argument("--categories", nargs="+", help="Specific categories")
    args = parser.parse_args()

    topic = args.topic
    topic_dir = str(get_topic_dir(topic))
    candidates_dir = os.path.join(os.path.dirname(__file__), "_img_timelines", topic)
    os.makedirs(candidates_dir, exist_ok=True)

    narratives_path = os.path.join(topic_dir, "_category_narratives.json")
    method_texts_dir = candidates_dir  # method texts saved alongside candidates

    # Load data
    with open(os.path.join(PAPERS_DIR, "_papers_index.json"), "r", encoding="utf-8") as f:
        all_papers = json.load(f)

    topic_papers = [p for p in all_papers if topic in p.get("topics", [])]
    log(f"Loaded {len(topic_papers)} {topic} papers")

    for p in topic_papers:
        cls = p.get("classifications", {}).get(topic, {})
        p["primary_category"] = cls.get("primary_category", "")
        p["sub_category"] = cls.get("sub_category", "")
        p["year"] = p.get("date", "")[:4] if p.get("date") else ""

    cat_papers = defaultdict(list)
    for p in topic_papers:
        if p["primary_category"]:
            cat_papers[p["primary_category"]].append(p)

    target_cats = args.categories if args.categories else sorted(k for k in cat_papers.keys() if k != "Other")

    # ═══════════════════════════════════════
    # STEP 1: Generate all narratives
    # ═══════════════════════════════════════
    run_narratives = not args.images_only and not args.main_only
    category_summaries = []

    if run_narratives:
        log("\n" + "=" * 60)
        log("STEP 1: NARRATIVE GENERATION (Opus streaming)")
        log("=" * 60)

        for cat_name in target_cats:
            papers = cat_papers.get(cat_name, [])
            if not papers:
                continue

            slug = category_slug(cat_name)
            log(f"\n--- {cat_name} ({len(papers)} papers) ---")

            method_text, caption, summary = build_category_narrative(papers, topic, cat_name)

            # Save method text
            with open(os.path.join(method_texts_dir, f"_method_text_{slug}.txt"), "w", encoding="utf-8") as f:
                f.write(method_text)
            with open(os.path.join(method_texts_dir, f"_caption_{slug}.txt"), "w", encoding="utf-8") as f:
                f.write(caption)

            category_summaries.append(summary)

        # Save narratives
        with open(narratives_path, "w", encoding="utf-8") as f:
            json.dump(category_summaries, f, ensure_ascii=False, indent=2)
        log(f"\nStep 1 done: {len(category_summaries)} narratives → {narratives_path}")

        # Also generate main narrative
        if not args.category_only:
            log("\n--- Main narrative (from category summaries) ---")
            method_text, caption = build_main_narrative_from_summaries(category_summaries, topic)
            with open(os.path.join(method_texts_dir, "_method_text_main.txt"), "w", encoding="utf-8") as f:
                f.write(method_text)
            with open(os.path.join(method_texts_dir, "_caption_main.txt"), "w", encoding="utf-8") as f:
                f.write(caption)
            log("Main narrative saved.")

        # Generate executive summary + _timeline_narrative.json
        if not args.category_only:
            log("\n--- Executive summary (Korean) ---")
            exec_summary = build_executive_summary(category_summaries, topic)
            save_timeline_narrative(topic_dir, exec_summary, category_summaries)

    if args.narrative_only:
        log("\n--narrative-only: stopping after Step 1.")
        return

    # ═══════════════════════════════════════
    # STEP 2: Generate images from narratives
    # ═══════════════════════════════════════
    log("\n" + "=" * 60)
    log("STEP 2: IMAGE GENERATION (PaperBanana)")
    log("=" * 60)

    # Load narratives if not from Step 1
    if not category_summaries and os.path.exists(narratives_path):
        with open(narratives_path, "r", encoding="utf-8") as f:
            category_summaries = json.load(f)
        log(f"Loaded {len(category_summaries)} narratives from {narratives_path}")

    # Category timelines
    if not args.main_only:
        for cat_name in target_cats:
            slug = category_slug(cat_name)
            method_path = os.path.join(method_texts_dir, f"_method_text_{slug}.txt")
            caption_path = os.path.join(method_texts_dir, f"_caption_{slug}.txt")

            if not os.path.exists(method_path):
                log(f"  SKIP {cat_name}: no method text (run without --images-only first)")
                continue

            with open(method_path, "r", encoding="utf-8") as f:
                method_text = f.read()
            caption = ""
            if os.path.exists(caption_path):
                with open(caption_path, "r", encoding="utf-8") as f:
                    caption = f.read()

            log(f"\n--- {cat_name} ({len(method_text)} chars method) ---")
            results = generate_candidates(method_text, caption, f"category_{slug}",
                                          candidates_dir, args.candidates)

            deploy_name = f"category_timeline_{category_slug(cat_name)}.png"
            deploy_candidate(results, os.path.join(topic_dir, deploy_name))

    # Main timeline
    if not args.category_only:
        method_path = os.path.join(method_texts_dir, "_method_text_main.txt")
        caption_path = os.path.join(method_texts_dir, "_caption_main.txt")

        if not os.path.exists(method_path):
            if not category_summaries:
                log("ERROR: No narratives available. Run without --images-only first.")
                return
            log("\n--- Generating main narrative on the fly ---")
            method_text, caption = build_main_narrative_from_summaries(category_summaries, topic)
        else:
            with open(method_path, "r", encoding="utf-8") as f:
                method_text = f.read()
            caption = ""
            if os.path.exists(caption_path):
                with open(caption_path, "r", encoding="utf-8") as f:
                    caption = f.read()

        log(f"\n--- Main timeline ({len(method_text)} chars method) ---")
        results = generate_candidates(method_text, caption, "research_timeline",
                                      candidates_dir, args.candidates)
        deploy_candidate(results, os.path.join(topic_dir, "research_timeline.png"))

    log("\n" + "=" * 60)
    log("ALL DONE")
    log(f"Narratives: {narratives_path}")
    log(f"Candidates: {candidates_dir}")
    log(f"Deploy: {topic_dir}/*.png")
    log("=" * 60)


if __name__ == "__main__":
    main()
