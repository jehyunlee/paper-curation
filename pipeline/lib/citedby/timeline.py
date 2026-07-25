"""인용 흐름 타임라인 — paper-curation 의 타임라인 절차를 그대로 따른다.

**절차가 핵심이다.** `generate_timelines.py` 는 통계를 PaperBanana 에 바로
넘기지 않는다:

    1) LLM 이 논문 목록을 읽고 **narrative(method text)** 를 쓴다
       — 어떤 갈래가 언제 생겼고 무엇과 합쳐졌는지, 시각 규칙까지 포함
    2) 그 narrative 로 **후보 이미지를 N개** 만든다
    3) **vision judge** 가 색·역학·잡텍스트 기준으로 하나를 고른다

통계표를 그대로 던지면 PaperBanana 가 "무엇을 그릴지" 를 스스로 지어내야 해서
결과가 들쭉날쭉해진다. narrative 는 그 판단을 LLM 에게 먼저 시키는 단계다.

citedby 는 코퍼스 타임라인과 축이 다르다 — 코퍼스는 "이 분야가 어떻게 흘러
왔나", citedby 는 **"이 논문 한 편이 어디로 퍼졌나"** 다. 그래서 seed 논문이
왼쪽 원점에 고정되고, 시간 범위가 훨씬 짧다(대개 2~4년).
"""
from __future__ import annotations

import base64
import logging
import os
import tempfile

logger = logging.getLogger(__name__)

WALL_TIMEOUT_S = 900       # 후보 생성 전체 상한 (대화형이라 코퍼스보다 짧게)
CRITIC_ROUNDS = 2
DEFAULT_CANDIDATES = 3     # 코퍼스는 5개. 대화형이라 3개로 줄인다.

_JUDGE_MODEL = os.environ.get("TIMELINE_JUDGE_MODEL", "claude-haiku-4-5")

# ── 1단계: narrative ─────────────────────────────────────────────────────

_NARRATIVE_PROMPT = """You are analysing how a single paper propagated through \
the literature that cites it.

SEED PAPER: {seed}

CITING PAPERS grouped into themes by clustering ({total} papers, {span}):

{themes}

Write a METHOD TEXT that instructs a diagram generator to draw this \
propagation as a timeline. Follow this structure exactly:

## Citation Timeline: how "{short_seed}" propagated

### STREAM: {{theme_name}} ({{start}}->{{end}}, {{ACCELERATING/STABLE/EMERGING}})
Relative size: {{LARGE/MEDIUM/SMALL — from the paper counts above}}
Influence: {{HIGH/MEDIUM/LOW — from cumulative citations, NOT paper count}}
Branches into:
- **"{{specific_topic}}"** ({{year}}): {{what these papers actually did — name \
concrete methods, benchmarks, or findings}}
Interaction: {{how this stream relates to others — MERGE INTO / FEED INTO / \
SPAWN / RESPOND TO}}

(Repeat for every theme above.)

### KEY MILESTONES
- **{{year}}: {{label}}** — {{what shifted}}

### DIVERGENCE
- ▶ {{stream}} emerges ({{year}}): {{trigger}}
- ◀ {{stream}} absorbed into {{other}} ({{year}})

### BAND WIDTH GUIDE
{{Streams from largest to smallest, with relative size}}

### ABSOLUTE VISUAL RULES
- Horizontal timeline, left to right, years labelled across the top.
- The SEED PAPER is a single anchored node at the far left; every stream \
originates from it.
- The time span is short ({span}) — spread it across the full width; do NOT \
compress recent years.
- Streams as smooth flowing ribbons with organic curves.
- Band width reflects paper count; colour intensity reflects citation impact. \
A narrow-but-intense stream must be visually distinguishable from a \
wide-but-pale one.
- Streams MUST interact — merging, branching, influence. NO parallel bands.
- Every branch carries its topic label — no unlabelled ribbons.
- Mark emergence with ▶, absorption with ◀.
- STYLE: clean editorial Sankey-style infographic, bold stream labels at each \
origin, thin leaf labels along the right edge, milestone annotations as small \
rounded callout boxes, one saturated consistent colour per stream, flat vector.
- White background, clean sans-serif.
- NO title in image, NO watermarks, NO colour-name text, NO raw paper counts.
- 16:9, English only.

---

CAPTION:
A one-paragraph figure caption describing what the timeline shows.
"""


def _themes_block(themes: dict) -> str:
    years = themes.get("years") or []
    lines = []
    for c in themes.get("clusters", []):
        per_year = ", ".join(f"{y}:{c['years'][y]}" for y in years
                             if c["years"].get(y))
        kw = ", ".join((c.get("keywords") or [])[:6])
        titles = "; ".join(t[:70] for t in (c.get("titles") or [])[:4])
        lines.append(
            f"- {c['name']} — {c['count']} papers, {c['citations']} citations\n"
            f"    yearly: {per_year or 'n/a'}\n"
            f"    keywords: {kw}\n"
            f"    papers: {titles}")
    return "\n".join(lines)


def build_narrative(themes: dict, paper_info: dict | None = None, *,
                    keys=None, cache_dir=None) -> tuple[str, str]:
    """LLM 으로 method text + caption 을 만든다. 실패하면 ("", "").

    이 단계를 건너뛰면 PaperBanana 가 무엇을 그릴지 스스로 지어내야 한다 —
    같은 데이터로도 결과가 매번 달라지는 원인이다.
    """
    from .topic_filter import llm_json

    seed = (paper_info or {}).get("title") or "the seed paper"
    years = themes.get("years") or []
    span = f"{years[0]}-{years[-1]}" if years else "recent years"

    prompt = _NARRATIVE_PROMPT.format(
        seed=seed, short_seed=seed[:60], total=themes.get("total", 0),
        span=span, themes=_themes_block(themes))
    prompt += ('\n\nReturn JSON only:\n'
               '{"method_text": "...", "caption": "..."}')

    got = llm_json(prompt, max_tokens=6000, keys=keys, cache_dir=cache_dir)
    if not got:
        logger.warning("타임라인 narrative 생성 실패")
        return "", ""
    return (str(got.get("method_text") or "").strip(),
            str(got.get("caption") or "").strip())


# ── 2단계: 후보 생성 ─────────────────────────────────────────────────────

def _generate_candidates(method_text: str, caption: str, out_dir: str,
                         n: int, progress=None) -> list:
    """PaperBanana 로 후보 N개. 실패한 것은 조용히 건너뛴다."""
    from lib.paperbanana import generate_diagram

    results = []
    for i in range(1, n + 1):
        if progress:
            progress("timeline", f"타임라인 후보 {i}/{n} 생성 중…")
        path = os.path.join(out_dir, f"cand_{i}.png")
        try:
            png = generate_diagram(method_text, caption, aspect_ratio="16:9",
                                   critic_rounds=CRITIC_ROUNDS,
                                   retrieval_setting="auto",
                                   output_path=path)
        except Exception as e:  # noqa: BLE001 — 후보 하나 실패가 전체를 막지 않는다
            logger.warning("후보 %d 실패: %s", i, str(e)[:110])
            continue
        if png:
            results.append((i, len(png), path, png))
            logger.info("후보 %d: %.0fKB", i, len(png) / 1024)
    return results


# ── 3단계: vision judge 선별 ─────────────────────────────────────────────

_JUDGE_CRITERIA = (
    "You are judging candidate timeline diagrams showing how ONE paper "
    "propagated through the papers that cite it. Every candidate renders the "
    "SAME data — pick the single best RENDERING, by these criteria in order:\n"
    "1) COLOR: each stream has a distinct colour used CONSISTENTLY across the "
    "timeline; no two streams in near-identical colours.\n"
    "2) DYNAMICS: emergence, absorption, merging and branching of streams over "
    "time are clearly and accurately shown, all anchored at the seed paper.\n"
    "3) CLEAN TEXT: no colour-name labels, no index numbers, no watermarks, no "
    "raw paper counts, no chart title. (Stream names as labels are fine.)\n"
    "Prefer 1, then 2, then 3; break ties by readability."
)


def _select_best(results: list, caption: str = ""):
    """후보가 여럿이면 vision judge 로 고른다. 실패하면 첫 번째 — 선별이
    배치를 막아서는 안 된다."""
    if not results:
        return None
    if len(results) == 1:
        return results[0]
    try:
        from anthropic import Anthropic

        judge = Anthropic(timeout=180.0, max_retries=3)
        content = []
        for n, (_i, _sz, _path, png) in enumerate(results, 1):
            content.append({"type": "text", "text": f"--- Candidate {n} ---"})
            content.append({"type": "image", "source": {
                "type": "base64", "media_type": "image/png",
                "data": base64.standard_b64encode(png).decode()}})
        ctx = f"\n\nContext:\n{caption[:1200]}" if caption else ""
        content.append({"type": "text", "text": _JUDGE_CRITERIA + ctx +
                        f"\n\nThere are {len(results)} candidates "
                        f"(1..{len(results)}). Call pick_best_timeline with "
                        "the 1-based index of the single best."})
        tool = {
            "name": "pick_best_timeline",
            "description": "Select the single best timeline candidate image.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "best": {"type": "integer"},
                    "reason": {"type": "string"},
                },
                "required": ["best", "reason"],
            },
        }
        resp = judge.messages.create(
            model=_JUDGE_MODEL, max_tokens=400, tools=[tool],
            tool_choice={"type": "tool", "name": "pick_best_timeline"},
            messages=[{"role": "user", "content": content}])
        for block in resp.content:
            if getattr(block, "type", "") == "tool_use":
                idx = int(block.input.get("best", 1))
                logger.info("타임라인 선별: 후보 %d — %s", idx,
                            str(block.input.get("reason", ""))[:90])
                if 1 <= idx <= len(results):
                    return results[idx - 1]
    except Exception as e:  # noqa: BLE001
        logger.warning("타임라인 선별 실패, 첫 후보 사용: %s", str(e)[:110])
    return results[0]


# ── 공개 API ─────────────────────────────────────────────────────────────

def generate(themes: dict, *, paper_info: dict | None = None,
             candidates: int = DEFAULT_CANDIDATES,
             keys=None, cache_dir=None, progress=None) -> str:
    """narrative → 후보 N개 → 선별 → data URI. 실패하면 빈 문자열.

    어떤 실패도 예외로 올리지 않는다 — 그림은 부가물이고, 리포트가 그것 때문에
    막히면 안 된다.
    """
    if not themes or not themes.get("clusters"):
        return ""

    try:
        import lib.paperbanana  # noqa: F401
    except Exception as e:  # noqa: BLE001
        logger.info("타임라인 생략: PaperBanana 없음 (%s)", str(e)[:80])
        return ""

    if progress:
        progress("timeline", "타임라인 narrative 작성 중…")
    method_text, caption = build_narrative(themes, paper_info,
                                           keys=keys, cache_dir=cache_dir)
    if not method_text:
        if progress:
            progress("timeline", "타임라인 생략 (narrative 실패)")
        return ""

    box: dict = {}

    def _run():
        with tempfile.TemporaryDirectory(prefix="citedby_tl_") as tmp:
            res = _generate_candidates(method_text, caption, tmp,
                                       candidates, progress)
            best = _select_best(res, caption)
            if best:
                box["png"] = best[3]

    # PaperBanana 는 Gemini 응답을 기다리다 멎는 사례가 있다. 대화형 흐름에서는
    # 무한정 기다릴 수 없으므로 상한을 넘기면 포기한다. 데몬 스레드라 남아도
    # 프로세스 종료를 막지 않는다.
    import threading
    th = threading.Thread(target=_run, daemon=True)
    th.start()
    th.join(WALL_TIMEOUT_S)
    if th.is_alive():
        logger.warning("타임라인이 %d초를 넘겨 포기", WALL_TIMEOUT_S)
        if progress:
            progress("timeline", "타임라인 생략 (시간 초과)")
        return ""

    png = box.get("png")
    if not png:
        if progress:
            progress("timeline", "타임라인 생략 (생성 실패)")
        return ""

    logger.info("타임라인 확정: %.0fKB", len(png) / 1024)
    if progress:
        progress("timeline", f"타임라인 완료 ({len(png) // 1024}KB)")
    return "data:image/png;base64," + base64.b64encode(png).decode("ascii")
