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


def category_input_hash(papers):
    """카테고리 narrative 의 입력만으로 안정적 해시를 만든다.

    build_category_narrative 의 프롬프트에 실제로 들어가는 필드
    (id/year/sub_category/essence[:200]/title[:80]) 만 모아 정렬 후 SHA-256.
    입력이 동일하면 해시도 동일 → Opus 재호출을 건너뛰는 캐시 키.
    프롬프트에 영향을 주는 필드가 늘면 반드시 여기에도 추가할 것
    (안 그러면 stale narrative 가 새어나간다)."""
    import hashlib

    rows = []
    for p in papers:
        rows.append((
            str(p.get("id", p.get("paper_id", ""))),
            str(p.get("year", "")),
            str(p.get("sub_category", "")),
            (p.get("essence", "") or "")[:200],
            (p.get("title", "") or "")[:80],
        ))
    rows.sort()
    # 편수 변화도 잡도록 len 을 함께 묶는다.
    payload = json.dumps([len(rows), rows], ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


# ═══════════════════════════════════════════
# Step 1: Narrative Generation (Opus streaming)
# ═══════════════════════════════════════════

def opus_streaming_call(prompt, max_tokens=12000):
    """Opus streaming 호출. SDK retry는 request-level만 처리하므로 mid-stream
    Connection reset/ReadError를 잡아서 수동 retry (exp backoff)."""
    import time as _time
    from lib.llm_client import get_chat_client, resolve_model
    client = get_chat_client(timeout=600.0, max_retries=4)

    last_err = None
    for attempt in range(5):
        try:
            text = ""
            # Opus 5 uses adaptive thinking and rejects an explicit `temperature` —
            # the API returns 400 "`temperature` is deprecated for this model."
            with client.messages.stream(
                model=resolve_model("opus"),
                max_tokens=max_tokens,
                messages=[{"role": "user", "content": prompt}],
            ) as stream:
                for chunk in stream.text_stream:
                    text += chunk
            return text
        except Exception as e:
            last_err = e
            wait = min(60, 5 * (2 ** attempt))
            print(f"[opus_streaming_call] attempt {attempt+1}/5 failed: {type(e).__name__}: {str(e)[:120]}; sleeping {wait}s", flush=True)
            _time.sleep(wait)
    raise RuntimeError(f"opus_streaming_call exhausted retries: {last_err}")


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
- TIME AXIS EMPHASIS: give the MAJORITY of horizontal width to 2000–2026, with labeled year gridlines at 2000, 2005, 2010, 2015, 2020, 2025. Collapse everything before 2000 into a single narrow "pre-2000 foundations" zone pinned at the far-left edge — pre-2000 origins show POSITION only and must NEVER stretch or dominate the axis.
- Sub-themes as smooth flowing ribbon/river streams with organic curves
- Band width should qualitatively reflect field size (larger fields = wider bands)
- Streams MUST interact: show merging, branching, influence — NO simple parallel bands
- All branches MUST have sub-category name labels — no unlabeled ribbons
- Mark emergence with ▶, decline with ◀
- STYLE: match a clean editorial Sankey-style infographic — bold stream-name labels at each stream's left origin, thin sub-theme leaf labels along the right edge, milestone annotations as small rounded callout boxes, one saturated consistent color per stream, flat vector look
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
- TIME AXIS EMPHASIS: give the MAJORITY of horizontal width to 2000–2026, with labeled year gridlines at 2000, 2005, 2010, 2015, 2020, 2025. Collapse everything before 2000 into a single narrow "pre-2000 foundations" zone pinned at the far-left edge — pre-2000 origins show POSITION only and must NEVER stretch or dominate the axis.
- Categories as smooth flowing ribbon/river streams with organic curves
- Band width qualitatively reflects field size (larger = wider, but not linearly proportional)
- Streams MUST interact: merging, branching, influence — NO simple parallel bands
- Key sub-themes shown as branches within category streams
- Mark emergence with ▶, decline with ◀
- STYLE: match a clean editorial Sankey-style infographic — bold stream-name labels at each stream's left origin, thin sub-theme leaf labels along the right edge, milestone annotations as small rounded callout boxes, one saturated consistent color per stream, flat vector look
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

import threading as _threading

# 이미지 생성은 process-global os.dup2(fd 1/2) 리다이렉트 + PaperBanana 의
# os.chdir 를 건드린다. fd 테이블과 cwd 는 스레드가 아니라 프로세스 단위라,
# 이미지 ThreadPool 의 워커가 동시에 dup2/chdir 하면 서로의 상태를 덮어써서
# "Bad file descriptor" 로 step 전체가 죽는다. 이 lock 이 fd 리다이렉트 ~
# 복원 + generate_diagram 호출 구간 전체를 직렬화한다 → 이미지 생성이 사실상
# 직렬이 되지만, 어차피 PaperBanana/Gemini 이미지 RPM 이 진짜 병목이라
# 손실은 미미하고 충돌 클래스는 사라진다.
_PB_GLOBAL_LOCK = _threading.Lock()

# Gemini 재시도 스케줄: capped exponential [30s,90s,300s,600s] (최대 ~17분).
# 예전 [60,60,60,1800,1800] (=63분/candidate) 는 candidate×category 곱으로
# 한 카테고리가 막히면 ~4시간을 잡아먹어 6시간 step 천장을 날렸다. 30분
# backoff 는 한 번의 야간 run 안에서 회복되는 일이 드물어 그냥 예산만 태운다.
# 추가로 _GEMINI_BUDGET_S 로 카테고리당 누적 sleep 상한을 둬서 막힌 카테고리는
# fail-soft(None) 로 빠지고 나머지 카테고리는 계속 진행하게 한다.
# TIMELINE_GEMINI_RETRY="30,90,300,600" 형식으로 env override 가능.
def _load_gemini_schedule():
    raw = os.environ.get("TIMELINE_GEMINI_RETRY", "").strip()
    if raw:
        try:
            sched = [int(x) for x in raw.split(",") if x.strip()]
            if sched:
                return sched
        except ValueError:
            pass
    return [30, 90, 300, 600]


_GEMINI_RETRY_SCHEDULE = _load_gemini_schedule()
# 카테고리(=한 candidate 시리즈)당 retry sleep 누적 상한. 이 deadline 을 넘기면
# 더 자지 않고 즉시 포기한다. env TIMELINE_GEMINI_BUDGET_S 로 조정.
_GEMINI_BUDGET_S = int(os.environ.get("TIMELINE_GEMINI_BUDGET_S", "1200"))  # 20분

# watchdog ABORT 신호용 sentinel. _pb_call_with_watchdog 의 워커 스레드는
# 하드 킬이 불가능해서(파이썬 협조적 스레드) timeout 으로 abort 하면 백그라운드에
# 누수된 채 계속 Gemini 를 때린다. 그 위에 새 candidate 를 더 띄우면 누수만
# 가중되므로, ABORT 가 나면 이 sentinel 을 흘려보내 해당 카테고리의 candidate
# 루프를 즉시 멈춘다 (스레드를 죽이진 않는 interim 대응).
_PB_ABORT = object()


def _is_gemini_transient(exc_or_text):
    """Gemini 에러가 재시도 가치가 있는지 판정.
    429/500/502/503/504/RESOURCE_EXHAUSTED 는 모두 transient 로 간주."""
    t = str(exc_or_text).lower()
    markers = ("429", "resource_exhausted", "500", "502", "503", "504",
               "quota", "overloaded", "unavailable", "server error",
               "event loop is closed", "timeout", "deadline exceeded")
    return any(m in t for m in markers)


# PaperBanana watchdog policy.
#
# PaperBanana does not use the `logging` module — its agents print() to stdout.
# Wall-clock timeouts misfire because legitimate critic loops can legitimately
# run 5~10 minutes. The real "stuck" signal is **stdout silence**: when the
# Gemini endpoint hangs without raising, no agent print() ever arrives.
#
# So we redirect fds 1/2 into a pipe and have a reader thread tail the lines,
# stamping a last_activity counter on every byte received. A watchdog loop in
# the main thread aborts if either:
#   - idle (no stdout for _PB_IDLE_TIMEOUT_S) — strong stuck signal
#   - wall (total elapsed > _PB_WALL_TIMEOUT_S) — failsafe ceiling
_PB_IDLE_TIMEOUT_S = 600    # 10 min of stdout silence = stuck (raised from 180s
                            # — PaperBanana's wrap-up + internal asyncio retry
                            # legitimately silences stdout for ~4 minutes)
_PB_WALL_TIMEOUT_S = 1800   # 30 min hard ceiling per call
_PB_POLL_INTERVAL_S = 10    # how often the watchdog checks
_PB_FILE_STABLE_S  = 15     # output file present + stable for this long = success


def _pb_call_with_watchdog(method_text, caption, output_path, critic_rounds):
    """Invoke PaperBanana with stdout-idle + wall-clock + file-presence watchdog.

    Returns (png_bytes_or_None, status):
      status == "ok"            → worker returned cleanly
      status == "file_complete" → output file on disk + stable; worker still running
                                   (PaperBanana finished writing but is in wrap-up)
      status == "idle_timeout"  → no stdout for _PB_IDLE_TIMEOUT_S and no output file
      status == "wall_timeout"  → exceeded _PB_WALL_TIMEOUT_S
    The worker thread may keep running in the background after timeout;
    Python threads are cooperative and cannot be hard-killed. Callers should
    treat any status with an existing, non-empty output_path as success.
    """
    import os as _os
    import threading
    import time as _time
    from lib.paperbanana import generate_diagram

    # 0) Remove any pre-existing output file so the watchdog's _file_ready()
    # check can't trigger on a stale candidate left over from a prior run.
    # Without this, generate_diagram() can fail silently while the OLD file
    # still satisfies `os.path.exists + size > 0`, getting "salvaged from
    # disk" as a phantom success.
    try:
        if output_path and _os.path.exists(str(output_path)):
            _os.remove(str(output_path))
    except Exception:
        pass

    # process-global os.dup2(fd 1/2) 리다이렉트 + PaperBanana 의 os.chdir 는
    # 프로세스 단위 상태라 동시 호출이 서로를 덮어쓴다. 이 lock 으로 fd 리다이렉트
    # ~ 복원 + worker 실행 전 구간을 직렬화한다 (이미지 생성은 사실상 직렬이지만
    # Gemini 이미지 RPM 이 진짜 병목이라 손실은 작고 fd 충돌 클래스는 제거된다).
    with _PB_GLOBAL_LOCK:
        return _pb_call_locked(
            method_text, caption, output_path, critic_rounds,
            generate_diagram, _os, threading, _time)


def _pb_call_locked(method_text, caption, output_path, critic_rounds,
                    generate_diagram, _os, threading, _time):
    """fd/cwd-민감 영역 본체. 반드시 _PB_GLOBAL_LOCK 보유 상태로만 호출."""
    # 1) Re-route fd 1/2 → pipe write end. Save originals.
    saved_out = _os.dup(1)
    saved_err = _os.dup(2)
    pipe_r, pipe_w = _os.pipe()
    _os.dup2(pipe_w, 1)
    _os.dup2(pipe_w, 2)
    _os.close(pipe_w)  # fds 1 and 2 are now the only writers

    last_activity = [_time.time()]
    activity_lock = threading.Lock()

    def reader():
        """Forward PB stdout to saved_out as '[pb] <line>', stamp activity."""
        try:
            with _os.fdopen(pipe_r, "r", buffering=1, errors="replace") as f:
                for line in f:
                    line = line.rstrip("\n")
                    if line:
                        _os.write(saved_out, f"      [pb] {line}\n".encode("utf-8", errors="replace"))
                    with activity_lock:
                        last_activity[0] = _time.time()
        except Exception:
            pass

    reader_t = threading.Thread(target=reader, daemon=True, name="pb-stdout-reader")
    reader_t.start()

    result_box = {"value": None, "exc": None, "done": False}

    def worker():
        try:
            result_box["value"] = generate_diagram(
                method=method_text, caption=caption,
                aspect_ratio="16:9", critic_rounds=critic_rounds,
                exp_mode="demo_planner_critic",
                retrieval_setting="auto",
                output_path=output_path,
            )
        except BaseException as e:  # capture even SystemExit-style
            result_box["exc"] = e
        finally:
            result_box["done"] = True

    worker_t = threading.Thread(target=worker, daemon=True, name="pb-worker")
    worker_t.start()

    def _file_ready():
        """Output file exists with non-zero size."""
        try:
            return bool(output_path) and _os.path.exists(str(output_path)) \
                   and _os.path.getsize(str(output_path)) > 0
        except Exception:
            return False

    t0 = _time.time()
    file_seen_at = None       # time we first saw output_path present
    file_seen_size = 0
    status = "ok"
    while not result_box["done"]:
        worker_t.join(timeout=_PB_POLL_INTERVAL_S)
        if result_box["done"]:
            break
        elapsed = _time.time() - t0
        with activity_lock:
            idle = _time.time() - last_activity[0]

        # B: output-file presence trumps both timeouts. Once PaperBanana has
        # written the PNG to disk, the work is meaningfully done — anything
        # the worker thread is still doing is cleanup/return marshalling.
        if _file_ready():
            try:
                cur_size = _os.path.getsize(str(output_path))
            except Exception:
                cur_size = 0
            if file_seen_at is None:
                file_seen_at = _time.time()
                file_seen_size = cur_size
            else:
                # File is stable (same size) for _PB_FILE_STABLE_S → finalize.
                stable = (cur_size == file_seen_size and
                          (_time.time() - file_seen_at) >= _PB_FILE_STABLE_S)
                if stable:
                    status = "file_complete"
                    break
                if cur_size != file_seen_size:
                    file_seen_size = cur_size
                    file_seen_at = _time.time()

        if elapsed > _PB_WALL_TIMEOUT_S:
            # Wall ceiling — still salvage if file exists.
            status = "file_complete" if _file_ready() else "wall_timeout"
            break
        if idle > _PB_IDLE_TIMEOUT_S:
            # Stdout silence — also salvage if file exists (the silence is
            # most likely PaperBanana's post-write wrap-up).
            status = "file_complete" if _file_ready() else "idle_timeout"
            break

    # 2) Restore fd 1/2 (this closes the pipe writers → reader sees EOF).
    try:
        _os.dup2(saved_out, 1)
        _os.dup2(saved_err, 2)
    finally:
        try: _os.close(saved_out)
        except Exception: pass
        try: _os.close(saved_err)
        except Exception: pass

    reader_t.join(timeout=2)

    if result_box["exc"] is not None and status == "ok":
        # Worker raised before any watchdog fired
        raise result_box["exc"]
    return result_box["value"], status


def generate_with_paperbanana(method_text, caption, output_path, critic_rounds=3):
    """PaperBanana 로 이미지 생성. Gemini 일시 실패 시 재시도.
    각 호출은 stdout-idle + wall watchdog 으로 stuck 을 감지한다.

    Returns:
      float  — 성공 (저장된 PNG 의 KB)
      None   — soft 실패 (재시도 후 포기 / non-transient empty)
      _PB_ABORT — watchdog abort (워커 누수). 호출측(generate_candidates)은
                  이 신호를 받으면 같은 카테고리의 candidate 루프를 즉시 멈춘다.

    재시도 sleep 은 _GEMINI_BUDGET_S(기본 20분) 의 deadline 으로 상한을 둔다 —
    한 카테고리가 막혀도 예산을 넘기면 fail-soft(None) 로 빠져 다른 카테고리가
    계속 진행한다 (예전 candidate×category × 30분 backoff 의 ~4h 폭주 방지)."""
    import time as _time

    deadline = _time.monotonic() + _GEMINI_BUDGET_S
    last_exc = None
    for attempt_idx, sleep_s in enumerate([0] + _GEMINI_RETRY_SCHEDULE):
        if sleep_s:
            # deadline 초과면 더 자지 않고 즉시 포기 (fail-soft).
            if _time.monotonic() + sleep_s > deadline:
                log(f"    [gemini-retry] budget ({_GEMINI_BUDGET_S}s) exhausted — "
                    f"giving up this candidate (fail-soft). Last error: {last_exc}")
                return None
            log(f"    [gemini-retry] sleeping {sleep_s}s before attempt "
                f"{attempt_idx}/{len(_GEMINI_RETRY_SCHEDULE)}...")
            _time.sleep(sleep_s)
        t0 = _time.time()
        log(f"    [paperbanana] calling generate_diagram (attempt {attempt_idx}, "
            f"idle≤{_PB_IDLE_TIMEOUT_S}s, wall≤{_PB_WALL_TIMEOUT_S}s)...")
        try:
            png_bytes, status = _pb_call_with_watchdog(
                method_text, caption, output_path, critic_rounds)
        except Exception as e:
            last_exc = e
            if not _is_gemini_transient(e):
                log(f"    [gemini-retry] non-transient error, aborting: {e}")
                raise
            continue
        elapsed = _time.time() - t0
        # A non-"ok" status from the watchdog is informational. The real
        # success criterion is "does the PNG exist on disk with non-zero size".
        # status=="file_complete" already signals success-via-disk.
        if status not in ("ok", "file_complete") and not (
                output_path and os.path.exists(output_path)
                and os.path.getsize(output_path) > 0):
            log(f"    [paperbanana-watchdog] ABORT: {status} after {elapsed:.0f}s — "
                f"abandoning candidate (worker thread leaked into background; "
                f"stopping remaining candidates for this category)")
            return _PB_ABORT
        if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
            note = "" if status == "ok" else f" (status={status}, salvaged from disk)"
            log(f"    [paperbanana] ok in {elapsed:.0f}s{note}")
            return os.path.getsize(output_path) / 1024
        log(f"    [paperbanana] ERROR: empty output after {elapsed:.0f}s (status={status})")
        last_exc = RuntimeError("PaperBanana returned empty output")
        if not _is_gemini_transient(last_exc):
            return None

    log(f"    [gemini-retry] GAVE UP after schedule {_GEMINI_RETRY_SCHEDULE}. "
        f"Last error: {last_exc}")
    return None


def generate_candidates(method_text, caption, prefix, candidates_dir, n=5):
    """N개 candidate 생성."""
    results = []
    for i in range(1, n + 1):
        out_path = os.path.join(candidates_dir, f"{prefix}_{i}.png")
        log(f"  Candidate #{i}...")
        try:
            kb = generate_with_paperbanana(method_text, caption, out_path)
            if kb is _PB_ABORT:
                # watchdog 가 워커를 누수시킨 채 abort. 그 위에 새 candidate 를
                # 더 띄우면 누수만 가중되므로 이 카테고리 candidate 루프를 중단.
                log(f"  #{i}: ABORT (leaked worker) — stopping candidates for '{prefix}'")
                break
            if kb:
                log(f"  #{i}: {kb:.0f}KB (PaperBanana)")
                results.append((i, kb, out_path))
            else:
                log(f"  #{i}: PaperBanana returned None (FAILED)")
        except Exception as e:
            log(f"  #{i}: ERROR {str(e)[:100]}")
        time.sleep(2)
    return results


# ── Vision judge: pick the best of N timeline candidates ──────────────────
# All N candidates render the SAME data, so selection is a pure quality call.
# Criteria (priority order) come from the operator:
#   1) per-category color is distinct/appropriate and used consistently,
#   2) emergence/disappearance and merging/branching of categories is clear,
#   3) no spurious text (color names, category numbers, watermarks, counts, title).
# 출력이 후보 인덱스 정수 하나라 최저가 티어로 충분하다.
_JUDGE_MODEL = os.environ.get("TIMELINE_JUDGE_MODEL", "claude-haiku-4-5")
_JUDGE_CRITERIA = (
    "You are judging candidate timeline diagrams of how research categories evolve "
    "over time. Every candidate renders the SAME underlying data — pick the single "
    "best RENDERING, by these criteria in priority order:\n"
    "1) COLOR: each category has a distinct, appropriate color used CONSISTENTLY for "
    "that category across the whole timeline; the palette is clear (no two categories "
    "in near-identical colors).\n"
    "2) DYNAMICS: the emergence and disappearance of categories over time, and their "
    "merging (convergence) and branching (divergence), are clearly and accurately shown.\n"
    "3) CLEAN TEXT: NO unwanted text — no color-name labels (e.g. 'blue'/'red'), no "
    "category index numbers, no watermarks, no raw paper counts, no chart title. "
    "(Category names used as labels/legend are fine.)\n"
    "Prefer the candidate that best satisfies 1, then 2, then 3; break ties by overall "
    "readability and clean layout."
)


def select_best_candidate(results, caption=""):
    """Vision-judge the N successful candidate images and return the best
    ``(i, kb, path)`` tuple. Falls back to the first successful candidate on a
    single input or any error, so selection never blocks deployment."""
    if not results:
        return None
    if len(results) == 1:
        return results[0]
    try:
        import base64
        from lib.llm_client import get_chat_client
        judge = get_chat_client(timeout=180.0, max_retries=3)
        content = []
        for n, (_i, _kb, path) in enumerate(results, 1):
            with open(path, "rb") as fh:
                b64 = base64.standard_b64encode(fh.read()).decode()
            content.append({"type": "text", "text": f"--- Candidate {n} ---"})
            content.append({"type": "image", "source": {
                "type": "base64", "media_type": "image/png", "data": b64}})
        ctx = ("\n\nContext (what the diagram should convey):\n" + caption[:1200]) if caption else ""
        content.append({"type": "text", "text": _JUDGE_CRITERIA + ctx +
                        f"\n\nThere are {len(results)} candidates (1..{len(results)}). "
                        "Call pick_best_timeline with the 1-based index of the single best."})
        tool = {
            "name": "pick_best_timeline",
            "description": "Select the single best timeline candidate image.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "best": {"type": "integer",
                             "description": f"1-based index (1..{len(results)}) of the best candidate"},
                    "reason": {"type": "string", "description": "one concise sentence on why"},
                },
                "required": ["best", "reason"],
            },
        }
        resp = judge.messages.create(
            model=_JUDGE_MODEL, max_tokens=400, tools=[tool],
            tool_choice={"type": "tool", "name": "pick_best_timeline"},
            messages=[{"role": "user", "content": content}],
        )
        best, reason = None, ""
        for block in resp.content:
            if getattr(block, "type", "") == "tool_use" and block.name == "pick_best_timeline":
                best = block.input.get("best")
                reason = block.input.get("reason", "")
        if isinstance(best, int) and 1 <= best <= len(results):
            log(f"     [judge] picked candidate {best}/{len(results)} "
                f"(file #{results[best - 1][0]}) — {reason[:120]}")
            return results[best - 1]
        log(f"     [judge] invalid pick {best!r} → first candidate")
    except Exception as e:
        log(f"     [judge] failed ({type(e).__name__}: {str(e)[:90]}) → first candidate")
    return results[0]


def deploy_candidate(results, deploy_path, caption=""):
    """Vision-judge the candidates (best of N), deploy the winner, then clean up
    the sibling candidate files with the same prefix (avoid disk accumulation)."""
    if not results:
        log(f"  WARNING: No successful candidates!")
        return False
    chosen = select_best_candidate(results, caption)
    src = chosen[2]
    shutil.copy2(src, deploy_path)
    log(f"  -> Deployed candidate (file #{chosen[0]}) to {os.path.basename(deploy_path)}")

    # Cleanup unused sibling candidates with same prefix
    import re as _re
    cand_dir = os.path.dirname(src)
    stem = os.path.splitext(os.path.basename(src))[0]
    m = _re.match(r"^(.+)_(\d+)$", stem)
    if m:
        prefix = m.group(1)
        sibling_re = _re.compile(rf"^{_re.escape(prefix)}_\d+\.(png|jpg|jpeg|webp)$",
                                 _re.IGNORECASE)
        removed = 0
        for entry in os.listdir(cand_dir):
            if sibling_re.match(entry):
                try:
                    os.remove(os.path.join(cand_dir, entry))
                    removed += 1
                except OSError:
                    pass
        if removed:
            log(f"     [auto-cleanup] dropped {removed} unused candidates for prefix '{prefix}'")
    return True


# ═══════════════════════════════════════════
# Main
# ═══════════════════════════════════════════

def _run_timeline(topic="ai4s", *, candidates=3, narrative_only=False,
                   images_only=False, main_only=False, category_only=False,
                   categories=None, mode="all", force_narrative=False):
    """Programmatic entrypoint for generate_timelines.

    `mode` is reserved for the api facade (legacy compatibility); the
    actual behavior is controlled by the boolean flags.
    """
    # --force-narrative 는 env 로 흘려보내 narrative 입력 해시 캐시를 우회한다.
    if force_narrative:
        os.environ["TIMELINE_FORCE_NARRATIVE"] = "1"
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

    target_cats = categories if categories else sorted(k for k in cat_papers.keys() if k != "Other")

    # ═══════════════════════════════════════
    # STEP 1: Generate all narratives
    # ═══════════════════════════════════════
    run_narratives = not images_only and not main_only
    category_summaries = []

    if run_narratives:
        log("\n" + "=" * 60)
        log("STEP 1: NARRATIVE GENERATION (Opus streaming)")
        log("=" * 60)

        # ThreadPool: Opus narrative calls are I/O-bound. 9 categories
        # serial × ~2 min each = ~18 min; max_workers=8 → ~2-3 min.
        # Streaming Opus is thread-safe (each call gets its own SSE
        # session); SDK retry/backoff applies per-call.
        from concurrent.futures import ThreadPoolExecutor, as_completed
        max_workers = int(os.environ.get("TIMELINE_NARRATIVE_PARALLEL", "8"))

        # narrative 입력 해시 캐시: 이전 _category_narratives.json 의 summary 에
        # 박아둔 `_input_hash` 가 이번 입력 해시와 같고 method/caption 파일이
        # 디스크에 남아 있으면 Opus 재호출을 건너뛴다 ("신규 논문 1편이라
        # changed_cat 으로 잡혔지만 이 카테고리 내용은 그대로"인 흔한 케이스를
        # 공짜로 만든다). TIMELINE_FORCE_NARRATIVE=1 로 강제 재생성 가능.
        force_narrative = os.environ.get("TIMELINE_FORCE_NARRATIVE", "").strip() in ("1", "true", "yes")
        prev_cache = {}
        if not force_narrative and os.path.exists(narratives_path):
            try:
                with open(narratives_path, "r", encoding="utf-8") as f:
                    for s in json.load(f):
                        cn = s.get("category")
                        if cn:
                            prev_cache[cn] = s
            except (json.JSONDecodeError, OSError):
                prev_cache = {}

        def _build_one(cat_name):
            papers = cat_papers.get(cat_name, [])
            if not papers:
                return None
            slug = category_slug(cat_name)
            input_hash = category_input_hash(papers)

            # 캐시 히트: 해시 일치 + method/caption 파일 존재 → Opus 스킵
            cached = prev_cache.get(cat_name)
            method_path = os.path.join(method_texts_dir, f"_method_text_{slug}.txt")
            caption_path = os.path.join(method_texts_dir, f"_caption_{slug}.txt")
            if (not force_narrative and cached
                    and cached.get("_input_hash") == input_hash
                    and os.path.exists(method_path)):
                log(f"  [cache]  {cat_name} ({len(papers)} papers) — input unchanged, reusing narrative")
                return cached

            log(f"  [start] {cat_name} ({len(papers)} papers)")
            method_text, caption, summary = build_category_narrative(papers, topic, cat_name)
            summary["_input_hash"] = input_hash
            with open(method_path, "w", encoding="utf-8") as f:
                f.write(method_text)
            with open(caption_path, "w", encoding="utf-8") as f:
                f.write(caption)
            log(f"  [done]  {cat_name} (method={len(method_text)}c, summary keys={list(summary.keys())[:3]})")
            return summary

        # 결과를 카테고리명으로 키잉해서 모은 뒤, 마지막에 카테고리명 정렬
        # 순서로 조립한다. as_completed 순서(=완료 순서)는 실행마다 달라서
        # main-narrative/executive-summary 입력과 캐시 JSON 이 비결정적이 되는데,
        # 정렬 순서로 고정해야 narrative 입력 해시 캐시가 안정적으로 동작한다.
        summary_by_cat = {}
        with ThreadPoolExecutor(max_workers=max_workers) as ex:
            futures = {ex.submit(_build_one, c): c for c in target_cats}
            for fut in as_completed(futures):
                c = futures[fut]
                try:
                    s = fut.result()
                    if s is not None:
                        summary_by_cat[c] = s
                except Exception as e:
                    log(f"  [category narrative failed] {c}: {str(e)[:150]}")

        # 결정적 순서: 카테고리명 정렬. `_input_hash` 가 들어간 캐시판은 디스크에
        # 저장하고, downstream(main narrative / executive summary) 에는 캐시
        # 메타키를 제거한 깨끗한 사본을 넘긴다 (프롬프트 오염 방지).
        cached_summaries = [summary_by_cat[c] for c in sorted(summary_by_cat)]
        category_summaries = [
            {k: v for k, v in s.items() if not k.startswith("_")}
            for s in cached_summaries
        ]

        with open(narratives_path, "w", encoding="utf-8") as f:
            json.dump(cached_summaries, f, ensure_ascii=False, indent=2)
        log(f"\nStep 1 done: {len(category_summaries)} narratives → {narratives_path}")

        if not category_only:
            log("\n--- Main narrative (from category summaries) ---")
            method_text, caption = build_main_narrative_from_summaries(category_summaries, topic)
            with open(os.path.join(method_texts_dir, "_method_text_main.txt"), "w", encoding="utf-8") as f:
                f.write(method_text)
            with open(os.path.join(method_texts_dir, "_caption_main.txt"), "w", encoding="utf-8") as f:
                f.write(caption)
            log("Main narrative saved.")

        if not category_only:
            log("\n--- Executive summary (Korean) ---")
            exec_summary = build_executive_summary(category_summaries, topic)
            save_timeline_narrative(topic_dir, exec_summary, category_summaries)

    if narrative_only:
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

    image_failures = []
    # Category timelines
    if not main_only:
        # ThreadPool: PaperBanana (Gemini image) calls per category.
        # 이미지 생성의 fd/cwd 민감 구간은 _PB_GLOBAL_LOCK 으로 직렬화되므로
        # 워커를 여러 개 띄워도 lock 에서 줄을 서기만 한다. default 1 로 두어
        # 직렬임을 명시 (Gemini 이미지 RPM 이 진짜 병목). 필요 시 env override.
        from concurrent.futures import ThreadPoolExecutor, as_completed
        img_workers = int(os.environ.get("TIMELINE_IMAGE_PARALLEL", "1"))

        def _gen_one_image(cat_name):
            slug = category_slug(cat_name)
            method_path = os.path.join(method_texts_dir, f"_method_text_{slug}.txt")
            caption_path = os.path.join(method_texts_dir, f"_caption_{slug}.txt")
            if not os.path.exists(method_path):
                log(f"  SKIP {cat_name}: no method text (run without --images-only first)")
                return None
            with open(method_path, "r", encoding="utf-8") as f:
                method_text = f.read()
            caption = ""
            if os.path.exists(caption_path):
                with open(caption_path, "r", encoding="utf-8") as f:
                    caption = f.read()
            log(f"  [start] {cat_name} ({len(method_text)}c method)")
            results = generate_candidates(method_text, caption, f"category_{slug}",
                                          candidates_dir, candidates)
            deploy_name = f"category_timeline_{category_slug(cat_name)}.png"
            ok = deploy_candidate(results, os.path.join(topic_dir, deploy_name), caption)
            if not ok:
                image_failures.append(deploy_name)
                raise RuntimeError(f"timeline image was not generated: {deploy_name}")
            log(f"  [done]  {cat_name}")
            return deploy_name

        with ThreadPoolExecutor(max_workers=img_workers) as ex:
            futures = {ex.submit(_gen_one_image, c): c for c in target_cats}
            for fut in as_completed(futures):
                c = futures[fut]
                try:
                    fut.result()
                except Exception as e:
                    image_failures.append(f"category:{c}")
                    log(f"  [image failed] {c}: {str(e)[:150]}")

    if not category_only:
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
        main_path = os.path.join(topic_dir, "research_timeline.png")
        results = generate_candidates(method_text, caption, "research_timeline",
                                      candidates_dir, candidates)
        if not deploy_candidate(results, main_path, caption):
            image_failures.append("research_timeline.png")
            raise RuntimeError("main research timeline was not generated: research_timeline.png")

    if image_failures:
        raise RuntimeError("timeline generation failed for: " + ", ".join(image_failures))
    log("\n" + "=" * 60)
    log("ALL DONE")
    log(f"Narratives: {narratives_path}")
    log(f"Candidates: {candidates_dir}")
    log(f"Deploy: {topic_dir}/*.png")
    log("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="Generate timelines (bottom-up, 3-step)")
    parser.add_argument("--topic", default="ai4s")
    parser.add_argument("--candidates", type=int, default=3)
    parser.add_argument("--narrative-only", action="store_true", help="Step 1 only: generate narratives")
    parser.add_argument("--images-only", action="store_true", help="Step 2 only: generate images from existing narratives")
    parser.add_argument("--main-only", action="store_true", help="Main timeline only (requires narratives)")
    parser.add_argument("--category-only", action="store_true", help="Category timelines only")
    parser.add_argument("--categories", nargs="+", help="Specific categories")
    parser.add_argument("--force-narrative", action="store_true",
                        help="narrative 입력 해시 캐시 무시하고 모든 카테고리 narrative 강제 재생성")
    args = parser.parse_args()
    _run_timeline(topic=args.topic, candidates=args.candidates,
                  narrative_only=args.narrative_only,
                  images_only=args.images_only, main_only=args.main_only,
                  category_only=args.category_only, categories=args.categories,
                  force_narrative=args.force_narrative)


if __name__ == "__main__":
    main()
