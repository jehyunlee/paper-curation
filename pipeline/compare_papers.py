"""Multi-paper comparison generator (paper-curio "Comparison" command).

Given 2+ reviewed papers, builds a Korean comparative analysis (관점/방법론/
originality/결과/한계) via one Anthropic call over their review.md contents,
then emits a self-contained HTML page (review-page theme + Audio Overview
widget + .md download button) plus the comparison markdown itself.

Output lives under docs/papers/_comparisons/<NNN_vs_NNN...>/ — local-only
(docs/.assetsignore) and deterministic, so re-running the same paper set
refreshes the same directory.

Usage:
  PYTHONUTF8=1 python pipeline/compare_papers.py --slugs 9121,9122
  (slug tokens may be bare NNN numbers or full slugs; 2-6 papers)

The paper-curio bridge imports run_compare() directly; the CLI prints a final
single-line JSON ({ok, html, md, dir, title}) so callers can lastJson() it.
"""

import argparse
import json
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import review_to_html as RH  # noqa: E402  (THEMES, css, md renderer, audio wiring)

PAPERS = RH.PAPERS
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(PAPERS)))
COMPARE_DIR = os.path.join(PAPERS, "_comparisons")
COMPARE_MODEL = os.environ.get("COMPARE_MODEL", "claude-sonnet-5")
MAX_PAPERS = 6

# review.md 섹션 중 비교 프롬프트에 넣는 것 (Related Papers 등은 제외)
_SECTIONS = ["Essence", "Motivation", "Achievement", "How", "Originality",
             "Limitation & Further Study", "Evaluation"]

# 고정 비교 축 — 프롬프트와 스키마 설명에 함께 명시
_AXES = ["문제 설정과 관점", "방법론", "Originality", "결과와 성과", "한계와 리스크",
         "연구 지형 (같이 보면 좋은 논문)"]

# 연결 관계의 한글 라벨 (review 페이지와 동일)
_REL_LABELS = {
    "alternative": "다른 접근",
    "extension": "후속 연구",
    "foundation": "기반 연구",
    "counterpoint": "반론/비판",
    "application": "응용 사례",
}

# 관계 유형 → 그래프 엣지 색
_REL_COLORS = {
    "기반 연구": "#2374D6",
    "후속 연구": "#2E9E5B",
    "다른 접근": "#E8890C",
    "반론/비판": "#D63423",
    "응용 사례": "#8E44AD",
}

# 비교 논문(P1, P2, ...) 노드 색 팔레트
_PAPER_COLORS = ["#2A9D8F", "#E76F51", "#457B9D", "#9C6644", "#5A189A", "#B5838D"]
_SHARED_COLOR = "#F5B800"  # 공통(2편 이상과 연결) 논문 노드


def log(msg):
    print(msg, flush=True)


# ── paper loading ────────────────────────────────────────────────────────────

def _load_index():
    with open(os.path.join(PAPERS, "_papers_index.json"), encoding="utf-8") as f:
        return json.load(f)


def resolve_slugs(tokens, index):
    """Resolve bare NNN numbers or full slugs to canonical index slugs."""
    by_slug = {p["slug"]: p for p in index}
    resolved = []
    for tok in tokens:
        tok = tok.strip()
        if not tok:
            continue
        if tok in by_slug:
            resolved.append(tok)
            continue
        pref = [s for s in by_slug if s.split("_", 1)[0] == tok]
        if len(pref) != 1:
            raise SystemExit(f"slug '{tok}' resolves to {len(pref)} papers — "
                             f"use the full slug")
        resolved.append(pref[0])
    return resolved


def _portable_url(doi, title):
    """RH._portable_url 위임 — DOI → arXiv → Zotero 원문 URL → Scholar.
    리뷰 페이지 다운로드와 동일한 해석기를 공유한다."""
    return RH._portable_url(doi, title)


def _parse_sections(md):
    """review.md → {section_name: text} (frontmatter stripped)."""
    body = re.sub(r"\A---\n[\s\S]*?\n---\n", "", md)
    parts = re.split(r"\n## +", "\n" + body)
    out = {}
    for p in parts[1:]:
        name, _, text = p.partition("\n")
        out[name.strip()] = text.strip()
    return out


def load_paper(slug, index, slug_titles, slug_dois, all_conns):
    entry = next((p for p in index if p["slug"] == slug), None)
    if entry is None:
        raise SystemExit(f"'{slug}' not in _papers_index.json")
    md_path = os.path.join(PAPERS, slug, "review.md")
    if not os.path.exists(md_path):
        raise SystemExit(f"{slug}: review.md 없음 — 먼저 리뷰를 생성하세요")
    with open(md_path, encoding="utf-8") as f:
        md = f.read()
    # 같이 보면 좋은 논문 (bidirectional connections view, top 8)
    conns = []
    for c in (all_conns.get(slug) or [])[:8]:
        cslug = c.get("slug", "")
        ctitle = slug_titles.get(cslug, cslug)
        conns.append({
            "slug": cslug,
            "title": ctitle,
            "relation": _REL_LABELS.get(c.get("relation", ""), c.get("relation", "")),
            "reason": c.get("reason", ""),
            "purl": _portable_url(slug_dois.get(cslug, ""), ctitle),
        })
    return {
        "slug": slug,
        "num": slug.split("_", 1)[0],
        "title": entry.get("title") or slug,
        "authors": entry.get("authors") or [],
        "date": str(entry.get("date") or ""),
        "doi": entry.get("doi") or "",
        "topic": entry.get("primary_topic") or "",
        "category": (entry.get("classifications", {})
                     .get(entry.get("primary_topic", ""), {})
                     .get("primary_category", "")),
        "sections": _parse_sections(md),
        "connections": conns,
        "purl": _portable_url(entry.get("doi") or "", entry.get("title") or slug),
    }


# ── LLM comparison ───────────────────────────────────────────────────────────

_TOOL = {
    "name": "emit_comparison",
    "description": "논문 비교 분석 결과를 구조화해 반환",
    "input_schema": {
        "type": "object",
        "properties": {
            "overview_ko": {"type": "string", "description":
                            "논문들의 관계와 비교 구도 총평 (한국어 3-5문장, 전문용어는 영어)"},
            "axes": {"type": "array", "items": {
                "type": "object",
                "properties": {
                    "axis_ko": {"type": "string", "description": f"비교 축 이름 — 반드시 이 5개를 순서대로: {', '.join(_AXES)}"},
                    "entries": {"type": "array", "items": {
                        "type": "object",
                        "properties": {
                            "slug": {"type": "string"},
                            "summary_ko": {"type": "string", "description": "이 축에서 이 논문의 입장/내용 (2-4문장)"},
                        },
                        "required": ["slug", "summary_ko"],
                    }},
                    "synthesis_ko": {"type": "string", "description":
                                     "이 축에서 논문들을 맞대어 본 분석 — 공통점/차이/우열/상보성 (2-4문장)"},
                },
                "required": ["axis_ko", "entries", "synthesis_ko"],
            }},
            "quick_table": {"type": "array", "items": {
                "type": "object",
                "properties": {
                    "axis_ko": {"type": "string"},
                    "cells": {"type": "array", "items": {"type": "string"},
                              "description": "논문 순서대로, 각 논문을 한 줄(≤60자)로. "
                                             "이 축에서 유달리 두드러지는 내용이 있으면 "
                                             "그 구절만 **굵게** 마크다운으로 감쌀 것 (남발 금지)"},
                },
                "required": ["axis_ko", "cells"],
            }},
            "reading_guide_ko": {"type": "string", "description":
                                 "독자 유형별로 어떤 논문을 어떤 순서로 읽을지 추천 (3-5문장)"},
            "diagram_spec_en": {
                "type": "object",
                "description": "비교 일러스트용 영어 스펙 — 이미지에 렌더링되므로 반드시 영어",
                "properties": {
                    "labels": {"type": "array", "items": {"type": "string"},
                               "description": "논문 순서대로, 각 논문의 짧은 영어 레이블 (≤6 words)"},
                    "scene_en": {"type": "string", "description":
                                 "논문들을 한 장면에 묶는 배경 설정 (≤25 words, English) — "
                                 "예: 'two explorers charting the same island from opposite shores'"},
                    "personas": {"type": "array", "items": {
                        "type": "object",
                        "properties": {
                            "label_en": {"type": "string", "description": "캐릭터 이름표 (≤5 words)"},
                            "persona_en": {"type": "string", "description":
                                           "이 논문의 의인화/사물 비유 + 하는 동작 (≤20 words) — "
                                           "논문의 실제 접근을 행동으로 보여줄 것. 캐릭터들끼리 "
                                           "실루엣·복장·도구가 한눈에 구별되게"},
                            "tagline_en": {"type": "string", "description":
                                           "이 논문만의 차별점 — 캐릭터 위 배너 "
                                           "(≤6 words, 예: 'HOW FAR it spreads')"},
                            "traits_en": {"type": "array", "items": {"type": "string"},
                                          "description": "이 논문 고유의 **구체적 발견·수치** "
                                          "딱 2개 (각 ≤5 words, 숫자 적극 사용 — 예: "
                                          "'users up 5x', 'humans plan 70%'). 축 이름 금지. "
                                          "그림 전체 글자를 최소화해야 하므로 짧게"},
                        },
                        "required": ["label_en", "persona_en", "tagline_en", "traits_en"],
                    }, "description": "논문 순서대로 하나씩"},
                    "shared_en": {"type": "string", "description":
                                  "공통점을 나타내는 물리적 공유 요소 (≤15 words) — 둘이 함께 들거나 "
                                  "딛고 선 하나의 사물/장소로 그려짐"},
                    "contrast_en": {"type": "string", "description":
                                    "한눈에 보여야 할 핵심 대비 하나 (≤15 words)"},
                    "rows": {"type": "array", "items": {
                        "type": "object",
                        "properties": {
                            "axis_en": {"type": "string", "description": "axis label in English (≤4 words)"},
                            "cells": {"type": "array", "items": {"type": "string"},
                                      "description": "논문 순서대로, 이 축에서 각 논문의 핵심 (≤8 words, English)"},
                        },
                        "required": ["axis_en", "cells"],
                    }},
                    "common_en": {"type": "string",
                                  "description": "shared ground of the papers (≤12 words, English)"},
                },
                "required": ["labels", "scene_en", "personas", "shared_en",
                             "contrast_en", "rows", "common_en"],
            },
        },
        "required": ["overview_ko", "axes", "quick_table", "reading_guide_ko",
                     "diagram_spec_en"],
    },
}


def _section_text(p, name):
    """Section text for the prompt. Evaluation 은 점수 표(| 로 시작하는 행)를
    걷어내고 총평 서술만 남긴다 — 점수 비교는 하지 않는다."""
    text = p["sections"].get(name, "")
    if name == "Evaluation":
        text = "\n".join(ln for ln in text.splitlines()
                         if not ln.lstrip().startswith("|"))
    return text.strip()[:2000]


def _build_prompt(papers):
    blocks = []
    for i, p in enumerate(papers, 1):
        sec_txt = "\n".join(
            f"### {name}\n{_section_text(p, name)}"
            for name in _SECTIONS if p["sections"].get(name))
        authors = ", ".join(p["authors"][:6])
        conn_txt = "\n".join(
            f"- {c['title']} ({c['relation']}): {c['reason'][:150]}"
            for c in p["connections"]) or "- (없음)"
        blocks.append(f"[P{i}] slug={p['slug']}\n제목: {p['title']}\n"
                      f"저자: {authors}\n연도: {p['date']}\n분류: {p['category']}\n"
                      f"{sec_txt}\n### 같이 보면 좋은 논문\n{conn_txt}")
    papers_txt = "\n\n---\n\n".join(blocks)
    return (
        f"다음 {len(papers)}편의 논문 리뷰를 매끄럽게 비교 분석하라.\n\n"
        f"{papers_txt}\n\n"
        "지침:\n"
        "- 최상위 필드 5개(overview_ko, axes, quick_table, reading_guide_ko, "
        "diagram_spec_en)를 하나도 빠뜨리지 말고 모두 채울 것 — overview_ko 를 "
        "가장 먼저 작성하라\n"
        f"- axes 는 정확히 이 6축을 이 순서로: {', '.join(_AXES)}\n"
        "- 각 축의 entries 에는 모든 논문을 slug 로 포함\n"
        "- '연구 지형 (같이 보면 좋은 논문)' 축에서는 각 논문의 주변 논문 목록이 "
        "그리는 연구 지형을 비교 — 공유하는 이웃, 서로 다른 계보와 응용 방향\n"
        "- quick_table 은 같은 6축, cells 는 논문 순서(P1, P2, ...)대로 한 줄 요약. "
        "축마다 유달리 튀는(특기할 만한) 내용이 있는 cell 은 그 핵심 구절만 "
        "**굵게** 표시하고, 없으면 어떤 cell 도 굵게 하지 말 것\n"
        "- 한국어 서술, 전문용어·모델명은 영어 유지. 근거 없는 우열 판정 금지 — "
        "리뷰에 있는 내용만 사용\n"
        "- 점수(숫자 평점)는 언급·비교하지 말 것\n"
        "- 서로 다른 관점(문제를 보는 시각), originality 의 결, 결과의 성격 차이를 "
        "드러내는 데 집중\n"
        "- diagram_spec_en 은 친근한 비교 일러스트로 그려진다: 논문들(또는 핵심 "
        "개념들)을 **의인화하거나 사물에 비유**해 한 장면(scene_en)에 담아라. "
        "비유는 논문이 실제로 하는 일에서 끌어낼 것 — 예: 확산을 재는 논문 = "
        "'a surveyor counting footprints spreading across a map', 협업 구조를 "
        "파고드는 논문 = 'a watchmaker opening a clock to see the gears' "
        "(이 예시들을 복사하지 말고, 이 논문들에 맞는 비유를 새로 창작할 것). "
        "personas 의 동작이 곧 그 논문의 접근이어야 하고, tagline_en 은 그 논문만의 "
        "차별점 선언, traits_en 은 **그 논문 고유의 구체적 발견·수치**(축 이름 금지, "
        "숫자 환영), shared_en 은 공통점을 하나의 물리적 요소로 보여준다. 그림만 "
        "봐도 두 논문이 각각 무엇을 밝혔는지 구별되는 것이 목표. 짧은 영어 문구만 "
        "(rows 는 앞의 5축 요약, 연구 지형 축은 제외)\n"
        "- axes 의 각 원소는 반드시 {\"axis_ko\": ..., \"entries\": "
        "[{\"slug\": ..., \"summary_ko\": ...}], \"synthesis_ko\": ...} 형태의 "
        "객체, quick_table 의 각 원소는 {\"axis_ko\": ..., \"cells\": [...]} 객체"
    )


def _valid_comp(out):
    """Tool input 이 렌더링 가능한 구조인지 검증. 문제면 사유 문자열 반환."""
    for k in _TOOL["input_schema"]["required"]:
        if k not in out:
            return f"missing key: {k}"
    axes = out.get("axes")
    if not isinstance(axes, list) or not axes:
        return "axes is not a non-empty list"
    for ax in axes:
        if not isinstance(ax, dict) or not ax.get("axis_ko") \
                or not isinstance(ax.get("entries"), list):
            return f"malformed axis: {str(ax)[:120]}"
        for e in ax["entries"]:
            if not isinstance(e, dict) or "slug" not in e or "summary_ko" not in e:
                return f"malformed entry: {str(e)[:120]}"
    for row in out.get("quick_table", []):
        if not isinstance(row, dict) or not isinstance(row.get("cells"), list):
            return f"malformed quick_table row: {str(row)[:120]}"
    spec = out.get("diagram_spec_en")
    if not isinstance(spec, dict) or not isinstance(spec.get("labels"), list) \
            or not isinstance(spec.get("rows"), list):
        return f"malformed diagram_spec_en: {str(spec)[:120]}"
    return ""


def compare_llm(papers):
    from lib.llm_client import get_chat_client
    try:
        client = get_chat_client(timeout=300.0, max_retries=4)
    except Exception as e:
        raise SystemExit(f"LLM backend unavailable: {e}") from e
    base_prompt = _build_prompt(papers)
    required = ", ".join(_TOOL["input_schema"]["required"])
    extra = ""
    last_err = ""
    for attempt in range(1, 4):
        # adaptive-thinking 모델은 thinking 토큰이 max_tokens 에 포함되므로
        # 여유 있게 잡아야 tool input 이 잘리지 않는다.
        resp = client.messages.create(
            model=COMPARE_MODEL,
            max_tokens=24000,
            tools=[_TOOL],
            tool_choice={"type": "tool", "name": "emit_comparison"},
            messages=[{"role": "user", "content": base_prompt + extra}],
        )
        block = next((b for b in resp.content if b.type == "tool_use"), None)
        out = block.input if block is not None else {}
        problem = _valid_comp(out) if isinstance(out, dict) else "input not a dict"
        if not problem:
            return out
        got = sorted(out.keys()) if isinstance(out, dict) else []
        last_err = f"stop_reason={resp.stop_reason}, {problem}, got={got}"
        log(f"  attempt {attempt}: invalid tool input ({last_err}) — retrying")
        # 필드 누락이 확률적으로 발생하므로, 무엇이 잘못됐는지 명시해 교정한다.
        extra = (f"\n\n[재시도 지시] 직전 응답은 무효였다 — 문제: {problem}. "
                 f"emit_comparison 의 required 최상위 필드({required})를 하나도 "
                 f"빠뜨리지 말고 전부 채워 완전한 객체를 다시 제출하라. "
                 f"overview_ko 를 가장 먼저 작성하라.")
    raise SystemExit(f"비교 생성 실패: {last_err}")


# ── markdown / html emit ─────────────────────────────────────────────────────

def _comp_title(papers):
    """Plain-text title: [비교] '제목1' vs '제목2'"""
    joined = " vs ".join(f"'{p['title'][:60]}'" for p in papers)
    return f"[비교] {joined}"


def _comp_title_html(papers):
    """h1 markup — '[비교]' 와 'vs' 는 회색으로."""
    parts = [f"&#39;{RH.esc(p['title'][:60])}&#39;" for p in papers]
    joined = ' <span class="cmp-gray">vs</span> '.join(parts)
    return f'<span class="cmp-gray">[비교]</span> {joined}'


def generate_comparison_image(papers, comp, out_dir):
    """PaperBanana 로 두(N) 논문 비교 다이어그램 생성 → comparison.png.

    실패해도 페이지 생성은 계속한다 (이미지 없이). COMPARE_IMAGE=0 으로 스킵.
    """
    if os.environ.get("COMPARE_IMAGE", "1") == "0":
        log("  diagram: skipped (COMPARE_IMAGE=0)")
        return False
    spec = comp.get("diagram_spec_en") or {}
    labels = spec.get("labels") or [p["title"][:40] for p in papers]

    personas = spec.get("personas")
    personas_ok = (isinstance(personas, list) and len(personas) == len(papers)
                   and all(isinstance(p, dict) and p.get("persona_en")
                           for p in personas))
    style = os.environ.get("COMPARE_IMAGE_STYLE", "metaphor")
    if style != "table" and personas_ok:
        # 의인화/사물 비유 장면 — 친근한 일러스트로 공통점(공유 요소)과
        # 차이점(캐릭터 특징)을 그린다.
        char_lines = "\n".join(
            f'- P{i + 1} — "{p.get("label_en", labels[i] if i < len(labels) else "")}": '
            f'{p.get("persona_en", "")}.\n'
            f'  Banner above P{i + 1}: "{p.get("tagline_en", "")}"\n'
            "  Exactly 2 finding cards (keep the numbers EXACTLY): "
            + " / ".join(f'"{t}"' for t in p.get("traits_en", [])[:2])
            for i, p in enumerate(personas))
        method = (
            f"# Friendly metaphorical comparison of {len(papers)} research papers\n\n"
            "One warm illustrated SCENE comparing research papers as "
            "characters/objects — NOT a table, NOT a chart, NOT columns. "
            "PRIMARY GOALS: (1) minimal text — the image must feel light, "
            "not crowded; (2) every text element clearly belongs to P1 or P2 "
            "via big paper badges.\n\n"
            f"Scene setting: {spec.get('scene_en', '')}\n\n"
            f"Characters/objects (left to right, one per paper):\n{char_lines}\n\n"
            f"Shared ground (IMPORTANT): {spec.get('shared_en', '')} — draw it as "
            "ONE physical element the characters share: jointly holding it, "
            "standing on it, or both connected to it, placed center or bottom.\n"
            f"Key contrast to make instantly visible: {spec.get('contrast_en', '')}\n\n"
            "Design rules:\n"
            "- PAPER BADGES (MOST IMPORTANT): each character wears a large bold "
            "circular badge reading exactly \"P1\", \"P2\", ... (like a race bib) "
            "in its accent color — the single biggest text element on its side. "
            "The same small badge mark appears on that character's banner and "
            "finding cards, so every phrase is instantly attributable\n"
            "- KEEP TEXT MINIMAL: per character only the badge, ONE short banner, "
            "TWO short finding cards, and a small name tag — nothing else; one "
            "small label on the shared element; no other words anywhere\n"
            "- flat kawaii/chibi illustration, soft pastel palette, rounded shapes\n"
            "- characters must be VISUALLY DISTINCT at a glance: different "
            "silhouette, outfit, headgear and tools — never near-twins\n"
            "- one distinct accent color per character, tinting that character's "
            "side, badge, banner and cards\n"
            "- each character's pose/action IS its research approach (no abstract icons)\n"
            "- numbers in finding cards kept verbatim; cards sit clearly on their "
            "owner's side\n"
            "- the shared element visually connects everyone; the contrast is obvious at a glance\n"
            "- clean light background, generous whitespace, no watermark"
        )
        caption = ("A friendly metaphorical scene comparing "
                   + " vs ".join(labels)
                   + f" — shared: {spec.get('shared_en', '')}; "
                   + f"contrast: {spec.get('contrast_en', '')}.")
    else:
        if style != "table" and not personas_ok:
            log("  diagram: personas missing/malformed — falling back to table style")
        rows = spec.get("rows") or []
        common = spec.get("common_en", "")
        row_lines = "\n".join(
            f"- {r.get('axis_en', '')}: " + " | ".join(r.get("cells", []))
            for r in rows)
        method = (
            f"# Side-by-side comparison of {len(papers)} research papers\n\n"
            f"A clean {len(papers)}-column versus-style comparison diagram.\n\n"
            f"Columns (one per paper, left to right): "
            + " / ".join(f'"{l}"' for l in labels) + "\n\n"
            f"Comparison rows (axis: one cell per column, left to right):\n{row_lines}\n\n"
            f"Bottom strip spanning all columns — shared ground: {common}\n\n"
            "Design: distinct accent color per column, axis labels on the left "
            "margin, short phrases only (no sentences), generous whitespace, "
            "no watermark, no extra text beyond the given phrases."
        )
        caption = ("Visual comparison of " + " vs ".join(labels)
                   + " across problem framing, method, originality, results, and limitations.")
    try:
        from lib.paperbanana import generate_diagram
        import time as _t
        t0 = _t.time()
        log("  diagram: generating via PaperBanana...")
        png = generate_diagram(method, caption, aspect_ratio="16:9",
                               critic_rounds=2,
                               output_path=os.path.join(out_dir, "comparison.png"))
        if png:
            log(f"  diagram: OK ({len(png)//1024}KB, {int(_t.time() - t0)}s)")
            return True
        log("  diagram: generation returned None — page continues without image")
    except Exception as e:
        log(f"  diagram: failed ({e}) — page continues without image")
    return False


def build_markdown(papers, comp, has_image=False):
    lines = [f"# {_comp_title(papers)}", ""]
    if has_image:
        lines += ["![비교 다이어그램](comparison.png)", ""]
    for i, p in enumerate(papers, 1):
        doi = f" · DOI: {p['doi']}" if p["doi"] else ""
        lines.append(f"- **[P{i}] {p['title']}** ({p['date']}){doi}")
    lines += ["", "## 총평", "", comp["overview_ko"], "",
              "## 읽기 가이드", "", comp.get("reading_guide_ko", ""), "",
              "## 한눈 비교", ""]
    header = "| 비교 축 | " + " | ".join(f"P{i}" for i in range(1, len(papers) + 1)) + " |"
    lines += [header, "|" + "---|" * (len(papers) + 1)]
    for row in comp.get("quick_table", []):
        cells = [c.replace("|", "/") for c in row.get("cells", [])]
        lines.append(f"| {row.get('axis_ko', '')} | " + " | ".join(cells) + " |")
    slug_to_label = {p["slug"]: f"P{i} · {p['title'][:50]}"
                     for i, p in enumerate(papers, 1)}
    for ax in comp.get("axes", []):
        lines += ["", f"## {ax.get('axis_ko', '')}", ""]
        for e in ax.get("entries", []):
            label = slug_to_label.get(e.get("slug", ""), e.get("slug", ""))
            lines += [f"**{label}**", "", e.get("summary_ko", ""), ""]
        lines += ["> " + ax.get("synthesis_ko", ""), ""]
    lines += ["## 같이 보면 좋은 논문", ""]
    for i, p in enumerate(papers, 1):
        lines += [f"**P{i} · {p['title'][:50]}**", ""]
        for c in p["connections"]:
            lines.append(f"- {c['relation']}: {c['title']}")
        lines.append("")
    return "\n".join(lines)


def _paper_card(p, i):
    authors = ", ".join(p["authors"][:4]) + (" 외" if len(p["authors"]) > 4 else "")
    doi_html = (f' · <a href="https://doi.org/{RH.esc(p["doi"])}" target="_blank">DOI</a>'
                if p["doi"] else "")
    review_href = f"../../{p['slug']}/index.html"
    return (f'<div class="cmp-card"><div class="cmp-card-num">P{i}</div>'
            f'<div class="cmp-card-title"><a href="{review_href}" '
            f'data-portable="{RH.esc(p["purl"])}">{RH.esc(p["title"])}</a></div>'
            f'<div class="cmp-card-meta">{RH.esc(authors)} ({RH.esc(p["date"])})'
            f'{doi_html}<br>{RH.esc(p["category"])}</div></div>')


def _cell_html(text):
    """표 셀: escape 후 **…** 만 <strong>으로 (LLM이 튀는 구절 강조에 사용)."""
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", RH.esc(text))


def _graph_data(papers):
    """D3 그래프 데이터: 비교 논문 + 연결 논문 노드, 관계 엣지.

    같은 논문이 여러 비교 논문의 연결 목록에 나타나면 노드 하나로 합치고
    shared 로 표시 — 힘 시뮬레이션에서 자연히 비교 논문들 사이에 놓인다.
    """
    compared = {p["slug"] for p in papers}
    nodes = [{"id": p["slug"], "label": p["title"][:34], "badge": f"P{i}",
              "full": p["title"], "kind": "compared", "ci": i - 1,
              "href": f"../../{p['slug']}/index.html", "purl": p["purl"]}
             for i, p in enumerate(papers, 1)]
    conn_nodes = {}
    links, seen_pairs = [], set()
    for p in papers:
        for c in p["connections"]:
            tgt = c["slug"]
            pair = frozenset((p["slug"], tgt))
            if pair in seen_pairs:
                continue  # 쌍방향 뷰라 역방향 중복 엣지 제거
            seen_pairs.add(pair)
            if tgt not in compared:
                n = conn_nodes.setdefault(tgt, {
                    "id": tgt, "label": c["title"][:34], "full": c["title"],
                    "kind": "conn", "deg": 0,
                    "href": f"../../{tgt}/index.html", "purl": c["purl"]})
                n["deg"] += 1
            links.append({"source": p["slug"], "target": tgt,
                          "relation": c["relation"],
                          "reason": (c["reason"] or "")[:200]})
    for n in conn_nodes.values():
        if n.pop("deg") >= 2:
            n["kind"] = "shared"
    return {"nodes": nodes + list(conn_nodes.values()), "links": links}


# D3 force-directed 그래프. 플레인 문자열 — __DATA__/__REL__/__PCOLORS__/
# __SHARED__ 를 json.dumps 값으로 치환해 사용 (JS 문자열 안에 개행 없음).
_GRAPH_JS = r"""
(function () {
  var data = __DATA__;
  var REL = __REL__;
  var PCOLORS = __PCOLORS__;
  var SHARED = __SHARED__;
  var el = document.getElementById('cmp-graph');
  if (!el || !window.d3 || !data.nodes.length) return;
  el.innerHTML = '';  // .html 다운로드본 재실행 시 이중 렌더 방지 (직렬화된 svg 제거)
  var W = el.clientWidth || 900, H = el.clientHeight || 520;
  var svg = d3.select(el).append('svg')
    .attr('viewBox', '0 0 ' + W + ' ' + H)
    .attr('width', '100%').attr('height', '100%');
  var nCmp = data.nodes.filter(function (d) { return d.kind === 'compared'; }).length;
  data.nodes.forEach(function (d) {
    if (d.kind === 'compared') { d.fx = W * (d.ci + 1) / (nCmp + 1); d.fy = H / 2; }
  });
  function r(d) { return d.kind === 'compared' ? 16 : d.kind === 'shared' ? 10 : 6.5; }
  function fill(d) {
    if (d.kind === 'compared') return PCOLORS[d.ci % PCOLORS.length];
    return d.kind === 'shared' ? SHARED : '#B8BEC9';
  }
  var sim = d3.forceSimulation(data.nodes)
    .force('link', d3.forceLink(data.links).id(function (d) { return d.id; })
      .distance(function (l) {
        var sh = (l.target.kind === 'shared' || l.source.kind === 'shared');
        return sh ? 150 : 110;
      }))
    .force('charge', d3.forceManyBody().strength(-340))
    .force('center', d3.forceCenter(W / 2, H / 2))
    .force('collide', d3.forceCollide().radius(function (d) { return r(d) + 16; }));
  var link = svg.append('g').selectAll('line').data(data.links).join('line')
    .attr('stroke', function (l) { return REL[l.relation] || '#999'; })
    .attr('stroke-width', 2.2).attr('stroke-opacity', 0.6);
  // 2px 선은 호버 판정이 불가능한 수준 — 투명 14px 히트 라인을 겹쳐 깔고
  // 즉시 뜨는 커스텀 툴팁으로 관계+이유를 보여준다.
  var tip = d3.select(el).append('div').attr('class', 'cmp-tip');
  function escT(s) { return String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;'); }
  var hit = svg.append('g').selectAll('line').data(data.links).join('line')
    .attr('stroke', '#000').attr('stroke-opacity', 0)
    .attr('stroke-width', 14).attr('pointer-events', 'stroke')
    .style('cursor', 'help')
    .on('mouseover', function (ev, d) {
      link.filter(function (x) { return x === d; })
        .attr('stroke-opacity', 1).attr('stroke-width', 3.5);
      tip.html('<b>' + escT(d.relation) + '</b><br>' + escT(d.reason))
        .style('opacity', 1);
    })
    .on('mousemove', function (ev) {
      var p = d3.pointer(ev, el);
      var x = Math.max(0, Math.min(p[0] + 14, (el.clientWidth || W) - 335));
      tip.style('left', x + 'px').style('top', (p[1] + 14) + 'px');
    })
    .on('mouseout', function (ev, d) {
      link.filter(function (x) { return x === d; })
        .attr('stroke-opacity', 0.6).attr('stroke-width', 2.2);
      tip.style('opacity', 0);
    });
  var node = svg.append('g').selectAll('g').data(data.nodes).join('g')
    .style('cursor', 'pointer')
    .call(d3.drag()
      .on('start', function (ev, d) { if (!ev.active) sim.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y; })
      .on('drag', function (ev, d) { d.fx = ev.x; d.fy = ev.y; })
      .on('end', function (ev, d) {
        if (!ev.active) sim.alphaTarget(0);
        if (d.kind !== 'compared') { d.fx = null; d.fy = null; }
      }))
    .on('click', function (ev, d) {
      if (ev.defaultPrevented) return;
      // 다운로드된 복사본에서는 로컬 상대경로가 깨지므로 portable URL(DOI 등)로.
      var u = (window._CMP_PORTABLE && d.purl) ? d.purl : d.href;
      if (u) window.open(u, '_blank');
    });
  node.append('circle')
    .attr('r', r).attr('fill', fill)
    .attr('stroke', function (d) { return d.kind === 'shared' ? '#B8860B' : '#fff'; })
    .attr('stroke-width', function (d) { return d.kind === 'shared' ? 2.5 : 1.5; });
  // 비교 논문의 P1/P2 배지는 노드 원 안에 흰색 볼드로 — 공통(금색) 노드와
  // 즉시 구별되고, 아래 제목 라벨과도 중복되지 않는다.
  node.append('text')
    .text(function (d) { return d.badge || ''; })
    .attr('text-anchor', 'middle')
    .attr('dy', '0.35em')
    .attr('font-size', '11.5px')
    .attr('font-weight', 800)
    .attr('fill', '#fff')
    .style('pointer-events', 'none');
  node.append('title').text(function (d) { return d.full; });
  node.append('text')
    .text(function (d) { return d.label; })
    .attr('text-anchor', 'middle')
    .attr('dy', function (d) { return r(d) + 13; })
    .attr('font-size', function (d) { return d.kind === 'compared' ? '11.5px' : '10px'; })
    .attr('font-weight', function (d) { return d.kind === 'conn' ? 400 : 700; })
    .attr('fill', '#444').style('pointer-events', 'none');
  sim.on('tick', function () {
    data.nodes.forEach(function (d) {
      d.x = Math.max(30, Math.min(W - 30, d.x));
      d.y = Math.max(26, Math.min(H - 30, d.y));
    });
    [link, hit].forEach(function (sel) {
      sel.attr('x1', function (l) { return l.source.x; })
         .attr('y1', function (l) { return l.source.y; })
         .attr('x2', function (l) { return l.target.x; })
         .attr('y2', function (l) { return l.target.y; });
    });
    node.attr('transform', function (d) { return 'translate(' + d.x + ',' + d.y + ')'; });
  });
})();
"""


def _connections_section(papers):
    """맨 뒤 '같이 보면 좋은 논문' — 인터랙티브 D3 그래프 + 범례."""
    chips = "".join(
        f'<span class="cmp-chip"><span class="cmp-chip-line" '
        f'style="background:{color}"></span>{RH.esc(rel)}</span>'
        for rel, color in _REL_COLORS.items())
    chips += (f'<span class="cmp-chip"><span class="cmp-chip-dot" '
              f'style="background:{_SHARED_COLOR}"></span>공통 논문</span>')
    graph_json = json.dumps(_graph_data(papers), ensure_ascii=False).replace("</", "<\\/")
    js = (_GRAPH_JS
          .replace("__DATA__", graph_json)
          .replace("__REL__", json.dumps(_REL_COLORS, ensure_ascii=False))
          .replace("__PCOLORS__", json.dumps(_PAPER_COLORS))
          .replace("__SHARED__", json.dumps(_SHARED_COLOR)))
    return (
        '<div class="section"><h2>같이 보면 좋은 논문</h2>'
        f'<div class="cmp-legend">{chips}</div>'
        '<div id="cmp-graph"></div>'
        '<div class="cmp-graph-hint">노드 클릭 = 리뷰 열기 · 드래그로 재배치 · '
        '엣지에 마우스를 올리면 연결 이유가 표시됩니다</div>'
        f"<script>{js}</script></div>")


_CMP_CSS = """
.cmp-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; margin: 1.2rem 0; }
.cmp-card { border: 1px solid #e0e0e8; border-radius: 10px; padding: 1rem; background: #fff; }
.cmp-card-num { font-weight: 700; color: ACCENT; font-size: 0.85rem; margin-bottom: 0.3rem; }
.cmp-card-title { font-weight: 600; line-height: 1.4; margin-bottom: 0.4rem; }
.cmp-card-title a { color: #1a1a2e; text-decoration: none; }
.cmp-card-title a:hover { color: ACCENT; }
.cmp-card-meta { font-size: 0.82rem; color: #666; margin-bottom: 0.5rem; }
.cmp-gray { color: #999; font-weight: 600; }
.cmp-hero { margin: 1.2rem 0; }
.cmp-hero img { width: 100%; border: 1px solid #e0e0e8; border-radius: 10px; }
/* review 페이지 CSS의 점수열 규칙(td:last-child = bold accent) 무효화 —
   비교표의 마지막 열은 점수가 아니라 마지막 논문이다. 강조는 <strong>으로만. */
td:last-child { text-align: left; font-weight: inherit; color: inherit; }
#cmp-graph { width: 100%; height: 540px; border: 1px solid #e0e0e8; border-radius: 10px; background: #fafbfc; margin: 0.6rem 0 0.4rem; position: relative; }
.cmp-tip { position: absolute; max-width: 320px; background: rgba(26,26,46,0.94); color: #fff; font-size: 0.78rem; line-height: 1.5; padding: 0.5rem 0.75rem; border-radius: 8px; pointer-events: none; opacity: 0; transition: opacity 0.15s; z-index: 10; }
.cmp-tip b { color: #FFD166; }
.cmp-legend { display: flex; flex-wrap: wrap; gap: 0.9rem; align-items: center; font-size: 0.8rem; color: #555; margin: 0.4rem 0; }
.cmp-chip { display: inline-flex; align-items: center; gap: 0.35rem; }
.cmp-chip-line { display: inline-block; width: 18px; height: 3px; border-radius: 2px; }
.cmp-chip-dot { display: inline-block; width: 11px; height: 11px; border-radius: 50%; border: 2px solid #B8860B; }
.cmp-graph-hint { font-size: 0.78rem; color: #999; }
.cmp-synthesis { border-left: 4px solid ACCENT; background: ACCENT_BG; padding: 0.7rem 1rem; border-radius: 0 8px 8px 0; margin: 0.8rem 0 1.4rem; }
.dl-bar { margin: 0.6rem 0 1.4rem; }
.dl-btn { background: ACCENT; color: #fff; border: none; border-radius: 8px; padding: 0.5rem 1rem; font-size: 0.88rem; cursor: pointer; font-family: inherit; }
.dl-btn:hover { background: ACCENT_DARK; }
"""


def build_html(papers, comp, md_text, theme, name, image_b64=None):
    title = _comp_title(papers)
    # 이미지는 base64 인라인 — .html 다운로드 시에도 페이지가 자기완결이 되도록.
    hero = (f'<div class="cmp-hero"><img src="data:image/png;base64,{image_b64}" '
            'alt="비교 다이어그램"></div>') if image_b64 else ""
    cards = '<div class="cmp-cards">' + "".join(
        _paper_card(p, i) for i, p in enumerate(papers, 1)) + "</div>"

    n = len(papers)
    thead = ("<tr><th>비교 축</th>" +
             "".join(f"<th>P{i}</th>" for i in range(1, n + 1)) + "</tr>")
    trows = "".join(
        "<tr><td><strong>{}</strong></td>{}</tr>".format(
            RH.esc(r.get("axis_ko", "")),
            "".join(f"<td>{_cell_html(c)}</td>" for c in r.get("cells", [])))
        for r in comp.get("quick_table", []))
    table = f"<table><thead>{thead}</thead><tbody>{trows}</tbody></table>"

    slug_to_label = {p["slug"]: f"P{i} · {p['title'][:50]}"
                     for i, p in enumerate(papers, 1)}
    ax_html = []
    for ax in comp.get("axes", []):
        parts = [f"<h2>{RH.esc(ax.get('axis_ko', ''))}</h2>"]
        for e in ax.get("entries", []):
            label = slug_to_label.get(e.get("slug", ""), e.get("slug", ""))
            parts.append(f"<p><strong>{RH.esc(label)}</strong></p>")
            parts.append(RH.md_section_to_html(e.get("summary_ko", "")))
        parts.append(f'<div class="cmp-synthesis">'
                     f'{RH.md_section_to_html(ax.get("synthesis_ko", ""))}</div>')
        ax_html.append('<div class="section">' + "".join(parts) + "</div>")

    # .md 다운로드: 마크다운 원문을 JS 문자열로 내장 (</ 는 태그 조기 종료 방지)
    md_js = json.dumps(md_text, ensure_ascii=False).replace("</", "<\\/")
    name_js = json.dumps(name)
    # 다운로드본은 로컬 상대링크가 깨지므로 data-portable(DOI/arXiv/Scholar)로
    # 치환하고, _CMP_PORTABLE 플래그를 켜서 그래프 노드 클릭도 portable 로 보낸다.
    dl_js = ("window._CMP_PORTABLE = false; "
             "function _dl(blob, fname) { "
             "var a = document.createElement('a'); "
             "a.href = URL.createObjectURL(blob); "
             "a.download = fname; a.click(); "
             "URL.revokeObjectURL(a.href); } "
             "function downloadCmpMd() { "
             "_dl(new Blob([window._CMP_MD], {type: 'text/markdown'}), "
             "window._CMP_NAME + '.md'); } "
             "function downloadCmpHtml() { "
             "var root = document.documentElement.cloneNode(true); "
             "root.querySelectorAll('a[data-portable]').forEach(function (a) { "
             "var u = a.getAttribute('data-portable'); "
             "if (u) { a.setAttribute('href', u); a.setAttribute('target', '_blank'); } }); "
             "var h = '<!DOCTYPE html>' + root.outerHTML; "
             "var flag = 'window._CMP_PORTABLE = '; "
             "h = h.split(flag + 'false').join(flag + 'true'); "
             "_dl(new Blob([h], {type: 'text/html'}), "
             "window._CMP_NAME + '.html'); }")

    css = (RH.get_css(theme) + "\n" + RH.get_audio_css(theme) + "\n" +
           _CMP_CSS.replace("ACCENT_DARK", theme["accent_dark"])
                   .replace("ACCENT_BG", theme["accent_bg"])
                   .replace("ACCENT", theme["accent"]))
    audio_ctx = {"title": title, "review": md_text, "connections": []}

    body = f"""<div class="container">
<h1>{_comp_title_html(papers)}</h1>
<div class="dl-bar">
<button class="dl-btn" onclick="downloadCmpMd()">.md 다운로드</button>
<button class="dl-btn" onclick="downloadCmpHtml()">.html 다운로드</button>
</div>
{RH.audio_bar_html()}
{hero}
{cards}
<div class="section"><h2>총평</h2>{RH.md_section_to_html(comp["overview_ko"])}</div>
<div class="section"><h2>읽기 가이드</h2>{RH.md_section_to_html(comp.get("reading_guide_ko", ""))}</div>
<div class="section"><h2>한눈 비교</h2>{table}</div>
{"".join(ax_html)}
{_connections_section(papers)}
</div>"""

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{RH.esc(title)}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/font-kopub/1.0/kopubdotum.css">
<script src="https://d3js.org/d3.v7.min.js"></script>
<style>
{css}
</style>
</head>
<body>
{body}
{RH.audio_modal_html()}
<script>
window._CMP_MD = {md_js};
window._CMP_NAME = {name_js};
{dl_js}
</script>
{RH.audio_script_block(audio_ctx)}
<footer style="text-align:center;padding:2rem 0 1rem;color:#999;font-size:0.85rem;border-top:1px solid #eee;margin-top:3rem;">
Developed by Jehyun Lee, KIST AIX Strategy Department | jehyun.lee@gmail.com
</footer>
</body>
</html>"""


# ── entrypoint ───────────────────────────────────────────────────────────────

def run_compare(slug_tokens):
    index = _load_index()
    slugs = resolve_slugs(slug_tokens, index)
    if not 2 <= len(slugs) <= MAX_PAPERS:
        raise SystemExit(f"논문 2~{MAX_PAPERS}편을 지정하세요 (현재 {len(slugs)})")
    slug_titles = {p["slug"]: (p.get("title") or p["slug"]) for p in index}
    slug_dois = {p["slug"]: (p.get("doi") or "") for p in index}
    all_conns = RH._load_connections()
    papers = [load_paper(s, index, slug_titles, slug_dois, all_conns) for s in slugs]
    log(f"Comparing {len(papers)} papers via {COMPARE_MODEL}:")
    for p in papers:
        log(f"  - {p['slug']} ({len(p['connections'])} connections)")

    name = "_vs_".join(p["num"] for p in papers)
    out_dir = os.path.join(COMPARE_DIR, name)
    os.makedirs(out_dir, exist_ok=True)

    comp = compare_llm(papers)
    has_image = generate_comparison_image(papers, comp, out_dir)
    image_b64 = None
    if has_image:
        import base64
        with open(os.path.join(out_dir, "comparison.png"), "rb") as f:
            image_b64 = base64.b64encode(f.read()).decode("ascii")
    md_text = build_markdown(papers, comp, has_image=has_image)
    theme = RH.THEMES.get(papers[0]["topic"], RH.THEMES["ai4s"])
    html = build_html(papers, comp, md_text, theme, name, image_b64=image_b64)
    md_path = os.path.join(out_dir, "comparison.md")
    html_path = os.path.join(out_dir, "index.html")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_text)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    log(f"Wrote {html_path}")
    return {"ok": True, "html": html_path, "md": md_path, "dir": out_dir,
            "title": _comp_title(papers)}


def main():
    ap = argparse.ArgumentParser(description="Multi-paper comparison generator")
    ap.add_argument("--slugs", required=True,
                    help="comma-separated slugs or NNN numbers (2-6 papers)")
    args = ap.parse_args()
    result = run_compare([t for t in args.slugs.split(",") if t.strip()])
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    from _env_guard import force_py312
    force_py312()
    main()
