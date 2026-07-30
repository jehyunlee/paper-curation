"""
Cross-paper insight 추출 + 논문 간 연결 생성.

카테고리별 논문 essence를 Sonnet으로 분석하여:
1. _insights.json — 카테고리 간 교차 트렌드, 연구 갭, 융합 신호
2. _paper_connections.json — 논문별 "같이 보면 좋은 논문" 추천 (이유 포함)

Usage:
  PYTHONUTF8=1 python pipeline/extract_insights.py --topic scisci
  PYTHONUTF8=1 python pipeline/extract_insights.py --topic ai4s --connections-only
  PYTHONUTF8=1 python pipeline/extract_insights.py --topic ai4s --insights-only
"""

import argparse
import json
import os
import sys
import time
from collections import defaultdict
from datetime import datetime

from lib.llm_client import get_chat_client, try_chat_client
from config_loader import PAPERS_DIR as _PAPERS_DIR, get_topic_dir, load_config

PAPERS_DIR = str(_PAPERS_DIR)


def log(msg):
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)

def _anthropic_text(resp):
    parts = []
    for block in getattr(resp, "content", []) or []:
        if getattr(block, "type", None) == "text" and getattr(block, "text", None):
            parts.append(block.text)
    text = "".join(parts).strip()
    if not text:
        types = [getattr(b, "type", type(b).__name__) for b in getattr(resp, "content", []) or []]
        raise RuntimeError(f"Anthropic response contained no text blocks: {types}")
    return text



def load_topic_data(topic):
    """토픽의 논문, 분류, 카테고리 요약 로드."""
    with open(os.path.join(PAPERS_DIR, "_papers_index.json"), "r", encoding="utf-8") as f:
        all_papers = json.load(f)

    topic_papers = [p for p in all_papers if topic in p.get("topics", [])]

    # 카테고리별 분류 (all_categories 기반, multi-class)
    cat_papers = defaultdict(list)
    seen_in_cat = defaultdict(set)  # 중복 방지
    for p in topic_papers:
        cls = p.get("classifications", {}).get(topic, {})
        all_cats = cls.get("all_categories", [cls.get("primary_category", "Other")])
        for cat in all_cats:
            if p["slug"] not in seen_in_cat[cat]:
                cat_papers[cat].append(p)
                seen_in_cat[cat].add(p["slug"])

    # 카테고리 요약 로드
    topic_dir = str(get_topic_dir(topic))
    sum_path = os.path.join(topic_dir, "_category_summaries.json")
    cat_summaries = []
    if os.path.exists(sum_path):
        with open(sum_path, "r", encoding="utf-8") as f:
            cat_summaries = json.load(f)

    return topic_papers, cat_papers, cat_summaries


# ═══════════════════════════════════════════
# 1. Cross-Category Insights
# ═══════════════════════════════════════════

# Sonnet 4.6 의 context window 는 1M 이고, 실제 insight 호출은 max_tokens=8000
# 출력을 요청한다 (_cc_anthropic_call). 따라서 input+output 이 window 를 넘지 않으려면
# 프롬프트 자체는 (window - max_output - safety_margin) 아래여야 한다. 1M 를 그대로
# 임계값으로 쓰면 ~192~200k 프롬프트가 shrink gate 를 그냥 통과한 뒤 호출 시점에
# context-length 초과로 죽고, 바깥 try/except 가 빈 insight 를 돌려준다.
# CONTEXT_WINDOW - MAX_OUTPUT_TOKENS - SAFETY_MARGIN = 1000000 - 8000 - 4000 = 988000.
_CONTEXT_WINDOW = 1000000
_MAX_OUTPUT_TOKENS = 8000   # _cc_anthropic_call max_tokens
_SAFETY_MARGIN = 4000       # tool schema/오버헤드/추정 오차 흡수
MAX_PROMPT_TOKENS = _CONTEXT_WINDOW - _MAX_OUTPUT_TOKENS - _SAFETY_MARGIN  # 988000
TARGET_PROMPT_TOKENS = 900000


def _est_tokens(text):
    """Conservative rough estimate for scaffolding (Korean-heavy=1.5)."""
    return int(len(text) / 1.5)


def _count_tokens(client, text, model="claude-sonnet-5"):
    """Authoritative token count via Anthropic API (no output tokens spent).
    Falls back to _est_tokens on any API error."""
    try:
        resp = client.messages.count_tokens(
            model=model,
            messages=[{"role": "user", "content": text}],
        )
        return resp.input_tokens
    except Exception as e:
        log(f"  count_tokens API failed ({e}); using local estimate")
        return _est_tokens(text)


def _build_cat_block(cat_name, papers, essence_chars=None):
    """Render one category's block as plain text. essence_chars truncates
    each paper's essence if set."""
    sorted_papers = sorted(papers, key=lambda x: -x.get("score", 0))
    lines = []
    for p in sorted_papers:
        num = p["slug"].split("_")[0]
        essence = p.get("essence", "") or ""
        if essence_chars is not None:
            essence = essence[:essence_chars]
        year = str(p.get("date", ""))[:4]
        lines.append(f"  [{num}] ({year}) {p.get('title', '')[:60]} | {essence}")
    return (f"### {cat_name} ({len(papers)} papers)\n" + "\n".join(lines))


def _haiku_summarize_block(block, client, target_chars):
    """Compress a category block while preserving category header, paper
    numbers/years, and distilled technical signal."""
    prompt = (
        f"Compress the following academic-paper list to at most {target_chars} characters. "
        f"Preserve:\n"
        f"  * The first '### CategoryName (N papers)' header line verbatim\n"
        f"  * Paper numbers in brackets (e.g. [091])\n"
        f"  * Year when present\n"
        f"  * Key technical themes (condense essence sentences but keep keywords)\n"
        f"Keep the top-represented papers in full, then group remaining papers into\n"
        f"one or two summary lines like '  [015, 042, 088] (2024-2025) survey papers on X focusing on Y, Z'.\n"
        f"Output plain text only (no markdown fences).\n\n"
        f"INPUT:\n{block}"
    )
    _t0 = time.time()
    log(f"    [haiku-summarize] calling Haiku 4.5 (~{_est_tokens(prompt)} input tokens, target {target_chars} chars)...")
    resp = client.with_options(timeout=600.0).messages.create(
        model="claude-haiku-4-5",
        max_tokens=max(2000, target_chars // 3),
        messages=[{"role": "user", "content": prompt}],
    )
    out = _anthropic_text(resp)
    log(f"    [haiku-summarize] -> {len(out)} chars in {time.time()-_t0:.0f}s")
    return out


def _fit_cat_blocks(cat_papers, client, max_prompt_tokens, target_prompt_tokens,
                    prompt_head, prompt_tail):
    """Assemble cat blocks. If (head+blocks+tail) token count > max_prompt_tokens,
    progressively summarize the largest block (via Haiku) until total ≤
    target_prompt_tokens. Returns the concatenated text + set of summarized
    category names.

    Token 측정 비용 최적화: count_tokens API (네트워크 왕복) 는 시작 1회 +
    종료 1회만 호출한다. shrink 루프 안에서는 매 반복마다 API 를 때리는 대신,
    시작 시 측정한 (authoritative tokens / total chars) 비율로 char→token 을
    국소 추정해서 언제 멈출지 결정한다. 이렇게 하면 큰 토픽에서 발생하던
    ~22 회의 직렬 count_tokens 왕복이 2 회로 줄어든다. (한국↔Anthropic 경로에서
    각 호출은 ~150~200k 페이로드라 수십 초씩 걸림.)
    """
    blocks = {}
    summarized = set()
    for cat_name, papers in cat_papers.items():
        if cat_name == "Other" or not papers:
            continue
        blocks[cat_name] = _build_cat_block(cat_name, papers)

    def full_prompt_text():
        cat_text = "\n\n".join(blocks[c] for c in sorted(blocks.keys()))
        return prompt_head + cat_text + prompt_tail

    def api_total_tokens():
        return _count_tokens(client, full_prompt_text())

    # ── 시작 1회: authoritative 측정 ──────────────────────────────────────
    initial_text = full_prompt_text()
    initial_total = _count_tokens(client, initial_text)
    log(f"  Prompt token count (authoritative): {initial_total}")
    if initial_total <= max_prompt_tokens:
        return "\n\n".join(blocks[c] for c in sorted(blocks.keys())), summarized

    log(f"  {initial_total} > {max_prompt_tokens} — running Haiku summarization "
        f"loop (target {target_prompt_tokens}).")

    # 시작 시점의 토큰/문자 비율로 char→token 국소 추정기를 보정한다.
    # (Korean-heavy 혼합 텍스트라 _est_tokens 의 고정 1/1.5 보다 실측 비율이 정확.)
    tok_per_char = (initial_total / max(1, len(initial_text)))

    def est_total_tokens():
        return int(len(full_prompt_text()) * tok_per_char)

    max_loops = 20
    for _ in range(max_loops):
        cur = est_total_tokens()  # 국소 추정 — 루프 안에서는 API 호출 없음
        if cur <= target_prompt_tokens:
            break
        # Summarize the biggest remaining block
        biggest_cat = max(blocks, key=lambda c: len(blocks[c]))
        # Target char size for this summary: proportional to shortfall
        overflow = cur - target_prompt_tokens
        shrink_chars = max(2000, int(overflow * 2.5))  # tokens → chars
        current_chars = len(blocks[biggest_cat])
        target_chars = max(1500, current_chars - shrink_chars)
        if target_chars >= current_chars - 200:
            # Can't meaningfully shrink; stop to avoid infinite loop
            log(f"  WARN: {biggest_cat} already near target; stopping summary loop")
            break
        log(f"  [summary] {biggest_cat}: {current_chars} → ≤{target_chars} chars")
        blocks[biggest_cat] = _haiku_summarize_block(
            blocks[biggest_cat], client, target_chars)
        summarized.add(biggest_cat)

    # ── 종료 1회: 실제 Sonnet 호출 전 authoritative 재측정 ────────────────
    final_total = api_total_tokens()
    log(f"  Prompt after summarization: ~{final_total} tokens "
        f"(summarized categories: {len(summarized)})")
    return "\n\n".join(blocks[c] for c in sorted(blocks.keys())), summarized


def extract_cross_category_insights(topic, cat_papers, cat_summaries, client):
    """카테고리 간 교차 insight 추출. Sonnet 1회 호출.

    988k 토큰 초과 시 Haiku summarization fallback 으로 900k 아래로 압축.
    """

    # Build prompt skeleton first (without cat data) to measure overhead.
    total = sum(len(v) for v in cat_papers.values() if v)
    prompt_head = (
        f"You are analyzing {total} academic papers across {len(cat_papers)} "
        f'categories in the "{topic}" research field.\n\nBelow is a summary '
        f"of each category with representative papers:\n\n"
    )
    prompt_tail = """

Produce a JSON array of 3-7 cross-category research insights. Each insight should be one of:
- "convergence": Two+ categories are merging or their methods are combining
- "gap": Important research gap — something NOT being studied that should be
- "emerging": A new trend just starting to appear
- "declining": An approach losing traction

For each insight, provide:
- type: convergence | gap | emerging | declining
- title: 한국어 제목 (15자 이내)
- description: 한국어 설명 (2-3문장, 구체적 근거 포함)
- categories: related category names (array)
- evidence: paper numbers as strings (array, e.g. ["045", "123"])
- signal_strength: "strong" (5+ papers support) or "weak" (2-4 papers)
- policy_implication: 한국어 1문장 — 정책 보고서에 어떤 시사점이 있는지

Also produce a per-category object with:
- trend: ACCELERATING | STABLE | EMERGING | DECLINING
- key_finding: 한국어 1문장 핵심 발견
- gap: 한국어 1문장 연구 갭
- policy_implication: 한국어 1문장 정책 시사점

Output ONLY valid JSON in this exact format:
{
  "cross_category": [ ... ],
  "per_category": {
    "Category Name": {
      "trend": "...",
      "key_finding": "...",
      "gap": "...",
      "policy_implication": "..."
    }
  },
  "meta": {
    "underserved_domains": ["...", "..."],
    "hot_combinations": [
      {"pair": ["A", "B"], "description": "한국어 설명"}
    ]
  }
}"""
    all_cats_text, summarized_cats = _fit_cat_blocks(
        cat_papers, client,
        max_prompt_tokens=MAX_PROMPT_TOKENS,
        target_prompt_tokens=TARGET_PROMPT_TOKENS,
        prompt_head=prompt_head,
        prompt_tail=prompt_tail,
    )
    prompt = prompt_head + all_cats_text + prompt_tail

    log(f"  Cross-category insight extraction ({total} papers, {len(cat_papers)} categories, "
        f"~{_est_tokens(prompt)} tokens)...")
    _t0 = time.time()
    log(f"    [insights] calling Sonnet 4.6 via tool-use (max_tokens=8000)...")

    insight_schema = {
        "name": "emit_insights",
        "description": "Emit cross-category research insights.",
        "input_schema": {
            "type": "object",
            "properties": {
                "cross_category": {
                    "type": "array",
                    "minItems": 3, "maxItems": 7,
                    "items": {
                        "type": "object",
                        "properties": {
                            "type": {"enum": ["convergence", "gap", "emerging", "declining"]},
                            "title": {"type": "string", "maxLength": 30},
                            "description": {"type": "string", "minLength": 30},
                            "categories": {"type": "array", "items": {"type": "string"}},
                            "evidence": {"type": "array",
                                          "items": {"type": "string"}},
                            "signal_strength": {"enum": ["strong", "weak"]},
                            "policy_implication": {"type": "string", "minLength": 10},
                        },
                        "required": ["type", "title", "description", "categories",
                                      "evidence", "signal_strength",
                                      "policy_implication"],
                    },
                },
                "per_category": {
                    "type": "object",
                    "additionalProperties": {
                        "type": "object",
                        "properties": {
                            "trend": {"enum": ["ACCELERATING", "STABLE",
                                                "EMERGING", "DECLINING"]},
                            "key_finding": {"type": "string", "minLength": 10},
                            "gap": {"type": "string", "minLength": 10},
                            "policy_implication": {"type": "string", "minLength": 10},
                        },
                        "required": ["trend", "key_finding", "gap",
                                      "policy_implication"],
                    },
                },
                "meta": {
                    "type": "object",
                    "properties": {
                        "underserved_domains": {"type": "array",
                                                 "items": {"type": "string"}},
                        "hot_combinations": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "pair": {"type": "array", "minItems": 2,
                                              "maxItems": 2,
                                              "items": {"type": "string"}},
                                    "description": {"type": "string"},
                                },
                                "required": ["pair", "description"],
                            },
                        },
                    },
                },
            },
            "required": ["cross_category", "per_category"],
        },
    }

    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from api._llm import cached_call, topic_cache_dir
    cache_dir = topic_cache_dir(topic)

    def _make_call():
        last_err = None
        for backend in _CC_BACKENDS:
            try:
                if backend == "anthropic":
                    out = _cc_anthropic_call(client, prompt, insight_schema)
                elif backend == "openai":
                    out = _cc_openai_call(prompt, insight_schema)
                elif backend == "gemini":
                    out = _cc_gemini_call(prompt, insight_schema)
                else:
                    log(f"    [insights:{backend}] unknown backend, skipping")
                    continue
                log(f"    [insights:{backend}] OK in {time.time()-_t0:.0f}s")
                return out
            except Exception as e:
                last_err = e
                log(f"    [insights:{backend}] failed ({type(e).__name__}: {str(e)[:80]}) → next backend")
        raise RuntimeError(f"all cross-category backends failed: "
                           f"{type(last_err).__name__}: {str(last_err)[:120]}")

    try:
        return cached_call(cache_dir, prompt, "+".join(_CC_BACKENDS), _make_call,
                            schema_version="v1")
    except Exception as e:
        log(f"  WARNING: insight tool-use failed: {e}")
        return {"cross_category": [], "per_category": {}, "meta": {}}


# ─────────────────────────────────────────────────────────────────────────────
# Cross-category insights backend helpers (Anthropic / OpenAI / Gemini)
# All three return a dict matching ``insight_schema`` so the caller stays
# provider-agnostic. Each helper raises on failure so the outer try/except
# chain can move to the next backend.
# ─────────────────────────────────────────────────────────────────────────────

_CC_ANTHROPIC_MODEL = os.environ.get(
    "EXTRACT_INSIGHTS_CC_ANTHROPIC_MODEL", "claude-sonnet-5")


def _cc_anthropic_call(client, prompt, schema):
    if client is None:
        raise RuntimeError("Anthropic client unavailable")
    resp = client.messages.create(
        model=_CC_ANTHROPIC_MODEL,
        max_tokens=8000,
        tools=[schema],
        tool_choice={"type": "tool", "name": schema["name"]},
        messages=[{"role": "user", "content": prompt}],
    )
    for block in resp.content:
        if getattr(block, "type", None) == "tool_use" \
                and getattr(block, "name", None) == schema["name"]:
            return dict(block.input)
    raise RuntimeError(f"{schema['name']} tool was not invoked")


def _cc_openai_call(prompt, schema):
    try:
        from openai import OpenAI
    except ImportError as e:
        raise RuntimeError(f"openai SDK missing: {e}")
    api_key = (os.environ.get("OPENAI_API_KEY") or
               load_config().get("openai_api_key", ""))
    if not api_key:
        raise RuntimeError("no OpenAI API key (OPENAI_API_KEY env or config)")
    oai = OpenAI(api_key=api_key, timeout=180.0, max_retries=1)
    func_def = {
        "type": "function",
        "function": {
            "name": schema["name"],
            "description": schema.get("description", ""),
            "parameters": schema["input_schema"],
        },
    }
    resp = oai.chat.completions.create(
        model=_OPENAI_CC_MODEL,
        max_tokens=8000,
        tools=[func_def],
        tool_choice={"type": "function", "function": {"name": schema["name"]}},
        messages=[{"role": "user", "content": prompt}],
    )
    msg = resp.choices[0].message
    if not getattr(msg, "tool_calls", None):
        raise RuntimeError(f"OpenAI did not invoke {schema['name']}")
    return json.loads(msg.tool_calls[0].function.arguments)


def _cc_gemini_call(prompt, schema):
    try:
        from google import genai
        from google.genai import types as gtypes
    except ImportError as e:
        raise RuntimeError(f"google-genai SDK missing: {e}")
    api_key = (os.environ.get("GEMINI_API_KEY")
               or os.environ.get("GOOGLE_API_KEY")
               or load_config().get("gemini_api_key", "")
               or load_config().get("google_api_key", ""))
    if not api_key:
        raise RuntimeError("no Gemini API key (GEMINI_API_KEY/GOOGLE_API_KEY env or config)")
    gem = genai.Client(api_key=api_key)
    resp = gem.models.generate_content(
        model=_GEMINI_CC_MODEL,
        contents=prompt,
        config=gtypes.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=schema["input_schema"],
        ),
    )
    text = (resp.text or "").strip()
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    return json.loads(text)


# Cross-category insights fallback chain (separate from paper_connections):
# anthropic → openai → gemini. Each backend is forced into the same JSON schema
# so the downstream consumer is provider-agnostic. Override with
# EXTRACT_INSIGHTS_CC_BACKENDS=openai,gemini etc.
_CC_BACKENDS = [b.strip().lower() for b in
                 os.environ.get("EXTRACT_INSIGHTS_CC_BACKENDS",
                                "anthropic,openai,gemini").split(",")
                 if b.strip()]
_CC_BACKENDS = list(dict.fromkeys(_CC_BACKENDS))
_OPENAI_CC_MODEL = os.environ.get("EXTRACT_INSIGHTS_CC_OPENAI_MODEL", "gpt-5.5")
_GEMINI_CC_MODEL = os.environ.get("EXTRACT_INSIGHTS_CC_GEMINI_MODEL", "gemini-3.1-pro-preview")


def _embed_model_tag(cache_path):
    """Embedding-geometry tag for the connection cache.

    A change in embedding geometry means cosine neighbours (hence connection
    reasons) can shift everywhere, so the incremental diff treats a tag change as
    a full-regen trigger. Prefer the tag the embeddings cache was written with;
    fall back to the live SPECTER2 tag; ``None`` if neither is available (None vs
    a real tag compares unequal → safe full regen)."""
    try:
        if cache_path and os.path.exists(cache_path):
            with open(cache_path, "r", encoding="utf-8") as f:
                tag = json.load(f).get("embed_model")
            if tag:
                return tag
    except Exception:
        pass
    try:
        from lib import specter2_embed
        return specter2_embed.EMBED_TAG
    except Exception:
        return None


def extract_paper_connections(topic, cat_papers, clients, all_topic_papers=None,
                              topic_dir=None, topic_slugs=None, seed_cache_only=False):
    """SPECTER2 코사인 top-N 후보 → Sonnet 이 관계·이유 판정 (하이브리드).

    topic_modeling / paper-curio 와 **동일한 SPECTER2 임베딩 기준**을 공유한다:
    후보는 `compute_related_candidates`(코사인 top-N, 전체 토픽 풀에서) 로 좁히고,
    판정은 `generate_connections_from_candidates`(Sonnet, 후보 내에서만 선택) 로 한다.
    카테고리 통째 덤프 방식 대비 (1) topic_modeling 과 기준 통일, (2) paper-curio
    경로와 방식 일치, (3) 프롬프트 페이로드 급감(느린 망 타임아웃 완화).

    연결을 생성할 대상은 `cat_papers`(= --categories 필터 반영)에 한정하되, 후보
    풀은 `all_topic_papers` 전체에서 뽑아 cross-category 연결을 유지한다. top-N 은
    `EXTRACT_INSIGHTS_TOPN_CAND`(기본 25)로 넉넉히 둬 counterpoint/application 처럼
    임베딩상 멀지만 관련 있는 연결의 recall 을 확보한다."""
    from topic_modeling import (
        extract_originalities, compute_embeddings,
        compute_related_candidates, generate_connections_from_candidates,
    )

    # 연결을 생성할 대상 = cat_papers (Other/초소형 카테고리 제외)
    target_slugs = set()
    for cat, papers in cat_papers.items():
        if cat == "Other" or len(papers) < 3:
            continue
        for p in papers:
            target_slugs.add(p["slug"])
    if not target_slugs:
        log("  연결 대상 논문 없음 — skip")
        return {}

    # 후보 풀 = 전체 토픽(cross-category 후보 유지). 임베딩은 캐시 우선.
    pool = all_topic_papers or [p for ps in cat_papers.values() for p in ps]
    seen = set()
    pool_uniq = []
    for p in pool:
        if p["slug"] not in seen:
            seen.add(p["slug"])
            pool_uniq.append(p)
    pool = pool_uniq

    originalities = extract_originalities(pool)
    cache_path = os.path.join(topic_dir, "_embeddings_cache.json") if topic_dir else None
    embeddings, slugs = compute_embeddings(originalities, cache_path)

    top_n = int(os.environ.get("EXTRACT_INSIGHTS_TOPN_CAND", "25"))
    full_cand = compute_related_candidates(embeddings, slugs, top_k=top_n)
    # 대상 논문에 대해서만 연결 생성(후보 값은 전체 토픽에서 온 것)
    candidates = {s: full_cand[s] for s in slugs
                  if s in target_slugs and s in full_cand}
    if not candidates:
        log("  후보 없음 — skip")
        return {}

    # seed-cache-only: 현재 top-k 를 conn 캐시 베이스라인으로만 저장하고 LLM 생성은
    # 건너뛴다. 기존 연결은 그대로(이미 멀쩡) 두고, 이후 실행이 *진짜 신규/변동* 논문만
    # 증분 생성하도록 캐시를 깐다. 전체 재생성($$·느림·JSON 절단) 없이 증분 모드를
    # 부팅하는 1회용 시드.
    if seed_cache_only:
        from lib import conn_cache
        _tag = _embed_model_tag(cache_path)
        conn_cache.save_topk_cache(topic_dir, candidates, top_n, _tag, scope="ei")
        log(f"  [conn] seed-cache-only: {len(candidates)}편 top-k 베이스라인 저장 "
            f"(LLM 호출 0). 이후 실행은 신규/변동 논문만 증분 생성.")
        return {}

    client = clients.get("anthropic")  # 이 단계는 Anthropic messages API 전용
    if client is None:
        log("  Anthropic client 없음 — skip")
        return {}

    # 기존 연결 로드 (신규/갭 우선 + 증분 dirty 판정)
    existing = {}
    if topic_dir:
        cp = os.path.join(topic_dir, "_paper_connections.json")
        if os.path.exists(cp):
            try:
                with open(cp, encoding="utf-8") as f:
                    existing = json.load(f)
            except Exception:
                existing = {}

    # ── 증분 연결 생성: top-k 멤버십이 바뀐(=hub) + 신규 + 연결갭 논문만 LLM 호출.
    # 변화 없는 논문은 generate 를 건너뛰고, sync 의 bidi 재구성으로 inbound 만 무료
    # 갱신한다. CONN_INCREMENTAL=0/off → 항상 full(기존 동작), CONN_FULL_REBUILD=1
    # → 이번 실행만 강제 full(주기적 대량 rebuild). 오류 시 안전하게 full 로 fallback.
    from lib import conn_cache
    _inc_on = os.environ.get("CONN_INCREMENTAL", "1").strip().lower() \
        not in ("0", "off", "false", "no")
    _full_rebuild = os.environ.get("CONN_FULL_REBUILD", "").strip().lower() \
        in ("1", "on", "true", "yes")
    _force_full = _full_rebuild or not _inc_on
    _embed_tag = _embed_model_tag(cache_path)
    _prev_cache = conn_cache.load_topk_cache(topic_dir, top_n, scope="ei") if topic_dir else {}
    dirty, reason = conn_cache.compute_dirty(
        candidates, _prev_cache, existing, top_n, _embed_tag,
        force=_force_full, log=log)
    _total = len(candidates)
    _pct = int(round(100 * (1 - len(dirty) / _total))) if _total else 0
    log(f"  [conn] incremental k={top_n}: {len(dirty)}/{_total} dirty ({reason}); "
        f"skipping {_total - len(dirty)} unchanged -> ~{_pct}% fewer LLM calls")
    gen_candidates = conn_cache.restrict_candidates(candidates, dirty)
    priority = set(s for s in gen_candidates if not existing.get(s))

    if gen_candidates:
        req_timeout = float(os.environ.get("EXTRACT_INSIGHTS_HTTP_TIMEOUT", "120"))
        conn_batch = int(os.environ.get("EXTRACT_INSIGHTS_CONN_BATCH", "15"))
        conn_deadline = int(os.environ.get("EXTRACT_INSIGHTS_CONN_DEADLINE", "300"))
        conn_rounds = int(os.environ.get("EXTRACT_INSIGHTS_CONN_ROUNDS", "3"))
        log(f"  연결 생성: 대상 {len(gen_candidates)}편, top_n={top_n}, "
            f"우선(갭) {len(priority)}편, req_timeout={req_timeout:.0f}s, "
            f"deadline={conn_deadline}s×{conn_rounds}r")
        all_connections = generate_connections_from_candidates(
            gen_candidates, pool, client, batch_size=conn_batch,
            deadline_s=conn_deadline, max_rounds=conn_rounds,
            request_timeout_s=req_timeout, priority_slugs=priority)
    else:
        # 0 dirty: LLM 호출을 통째로 생략. sync 는 그래도 호출해 consumer view 를
        # 싸게 재구성한다(merge_to_global({}) 는 no-op, bidi+filter 는 LLM 없음).
        log("  [conn] 0 dirty — LLM 호출 생략, consumer view 만 재구성")
        all_connections = {}

    # 영속화: merge_to_global → filter_for_topic → per-topic JSON
    if topic_dir and topic_slugs:
        try:
            from lib.connections import sync_topic_connections
            sync_topic_connections(all_connections, topic, topic_slugs, topic_dir, log=log)
            # 성공 시에만 캐시 갱신. 단 이번 run 에 *실제로 생성된* slug 만 current
            # set 으로 올리고, dirty 였지만 결과를 못 받은(deadline 절단 등) slug 은
            # prev set 을 유지해 다음 run 에 재시도되게 한다(hub inbound 누락 방지).
            try:
                _next_sets = conn_cache.next_cache_sets(
                    candidates, _prev_cache, dirty, set(all_connections.keys()))
                conn_cache.save_topk_cache(
                    topic_dir, candidates, top_n, _embed_tag,
                    scope="ei", sets=_next_sets)
            except Exception as e:
                log(f"  [conn] cache save failed: {str(e)[:80]}")
        except Exception as e:
            log(f"  [save] failed: {str(e)[:100]}")

    # 증분 생성된 논문 + 그 연결 이웃의 per-paper 페이지를 다시 렌더 — 새 역방향
    # 엣지(이웃→신규)가 이웃의 *개별 페이지* "같이 보면 좋은 논문" 에 즉시 뜨도록.
    # (데이터/네트워크/토픽인덱스는 sync+build 로 이미 완성되지만 per-paper 페이지는
    #  review_to_html 가 다시 그려야 반영된다.) 증분(reason=="incremental")일 때만 자동
    # 렌더(=dirty 소규모, 싸다); full 재생성은 파이프라인 review_to_html 단계가 처리.
    # env CONN_RENDER_NEIGHBORS=0 으로 끌 수 있다.
    if (all_connections and reason == "incremental" and topic_dir
            and os.environ.get("CONN_RENDER_NEIGHBORS", "1").strip().lower()
            not in ("0", "off", "false", "no")):
        try:
            import review_to_html as _RTH
            _RTH._run_review_to_html(slugs=list(dirty), with_connected=True)
            log(f"  [conn] 이웃 페이지 재렌더: dirty {len(dirty)}편 + 연결 이웃 (--with-connected)")
        except Exception as e:
            log(f"  [conn] 이웃 재렌더 skip: {str(e)[:80]}")

    return all_connections


def _run_insights(topic="ai4s", *, insights_only=False, connections_only=False,
                   categories=None, seed_cache_only=False):
    """Programmatic entrypoint for extract_insights."""
    topic_dir = str(get_topic_dir(topic))

    log(f"Loading {topic} data...")
    topic_papers, cat_papers, cat_summaries = load_topic_data(topic)

    if categories:
        cat_papers = {k: v for k, v in cat_papers.items() if k in categories}
        cat_summaries = [s for s in cat_summaries if s.get("category") in categories]
        log(f"  {len(topic_papers)} papers total, {len(cat_papers)} categories (filtered)")
    else:
        log(f"  {len(topic_papers)} papers, {len(cat_papers)} categories")

    # Per-request timeout — 느린 망에서 대용량 출력(25편 연결 = 수천 토큰)이
    # 기본 120s read-timeout 을 넘겨 APITimeoutError 가 나는 것을 막기 위해 env 로 상향 가능.
    _http_timeout = float(os.environ.get("EXTRACT_INSIGHTS_HTTP_TIMEOUT", "120"))
    _http_retries = int(os.environ.get("EXTRACT_INSIGHTS_HTTP_RETRIES", "1"))
    clients: dict = {"anthropic": None, "openai": None}
    try:
        clients["anthropic"] = get_chat_client(
            timeout=_http_timeout, max_retries=_http_retries)
    except Exception as e:
        log(f"  [backend] LLM (OpenRouter/Anthropic) init failed: {str(e)[:80]}")
    try:
        from openai import OpenAI
        from config_loader import get_openrouter_config
        _or = get_openrouter_config()
        if _or:
            # OpenRouter also covers the former OpenAI fallback path
            clients["openai"] = OpenAI(
                api_key=_or["api_key"],
                base_url=_or["base_url"],
                timeout=_http_timeout, max_retries=_http_retries)
        else:
            _oai_key = os.environ.get("OPENAI_API_KEY") or load_config().get("openai_api_key", "")
            if _oai_key:
                clients["openai"] = OpenAI(api_key=_oai_key, timeout=_http_timeout, max_retries=_http_retries)
    except Exception as e:
        log(f"  [backend] OpenAI/OpenRouter init failed: {str(e)[:80]}")
    client = clients["anthropic"] or clients["openai"]
    log(f"  [backend] connections: LLM {'OK' if clients.get('anthropic') else 'MISSING'} "
        f"(SPECTER2 후보 → Sonnet); cross-category insights: {'/'.join(_CC_BACKENDS)}")
    run_insights = not connections_only
    run_connections = not insights_only

    if run_insights:
        log("\n" + "=" * 50)
        log("CROSS-CATEGORY INSIGHTS (Sonnet)")
        log("=" * 50)

        insights = extract_cross_category_insights(topic, cat_papers, cat_summaries, client)
        # T2-4: verify cited evidence actually backs each cross-category insight.
        # Default ON (cheap, few items); env VERIFY_INSIGHTS=0 disables. Drops/
        # annotates unsupported insights. Uses the Anthropic (Haiku) client; if it
        # is unavailable or anything fails, originals are kept untouched.
        try:
            from lib import verify
            paper_meta = {
                p["slug"].split("_")[0]: {"title": p.get("title", ""),
                                          "essence": p.get("essence", "")}
                for p in topic_papers
            }
            verify.apply_insight_verification(
                insights, paper_meta, clients.get("anthropic"), log=log)
        except Exception as e:
            log(f"  [verify] insights hook skipped: {str(e)[:80]}")
        insights["generated_at"] = datetime.now().strftime("%Y-%m-%d")
        insights["topic"] = topic
        insights["paper_count"] = len(topic_papers)

        insights_path = os.path.join(topic_dir, "_insights.json")
        if categories and os.path.exists(insights_path):
            with open(insights_path, "r", encoding="utf-8") as f:
                existing_insights = json.load(f)
            current_cats = set(cat_papers.keys())
            existing_per_cat = {k: v for k, v in existing_insights.get("per_category", {}).items()
                                if k in current_cats}
            existing_per_cat.update(insights.get("per_category", {}))
            insights["per_category"] = existing_per_cat
            insights["paper_count"] = len(topic_papers)
        from lib.atomic_io import atomic_write_json
        atomic_write_json(insights_path, insights)
        log(f"\nSaved: {insights_path}")
        log(f"  {len(insights.get('cross_category', []))} cross-category insights")
        log(f"  {len(insights.get('per_category', {}))} per-category insights")

    if run_connections:
        log("\n" + "=" * 50)
        log("PAPER CONNECTIONS (Sonnet)")
        log("=" * 50)

        topic_slugs = [p["slug"] for p in topic_papers]
        connections = extract_paper_connections(
            topic, cat_papers, clients, topic_papers,
            topic_dir=topic_dir, topic_slugs=topic_slugs,
            seed_cache_only=seed_cache_only)

        # seed-cache-only 면 connections=={} 이고 캐시만 깔렸으니 sync(=no-op) 생략.
        if not seed_cache_only:
            from lib.connections import sync_topic_connections
            sync_topic_connections(connections, topic, topic_slugs, topic_dir, log=log)

    log("\nDone!")


def main():
    parser = argparse.ArgumentParser(description="Extract cross-paper insights and connections")
    parser.add_argument("--topic", default="ai4s")
    parser.add_argument("--insights-only", action="store_true", help="Cross-category insights only")
    parser.add_argument("--connections-only", action="store_true", help="Paper connections only")
    parser.add_argument("--only", choices=["connections", "insights", "all"], default="all",
                        help="생성 대상 선택. connections=paper connections(Core)만, "
                             "insights=cross-category insights(Option)만, all=둘 다(기본, 하위호환).")
    parser.add_argument("--categories", nargs="+", help="Specific categories to process (others preserved)")
    parser.add_argument("--seed-cache-only", action="store_true",
                        help="연결 LLM 생성 없이 현재 top-k 를 conn 캐시 베이스라인으로만 저장. "
                             "증분 모드를 1회 부팅(전체 재생성 회피); 기존 연결은 그대로 두고 "
                             "이후 실행이 신규/변동 논문만 증분 생성하게 한다.")
    args = parser.parse_args()
    # --only 를 기존 *_only 게이트로 매핑 (둘 다 동일 효과; --insights-only/--connections-only 와 OR).
    insights_only = args.insights_only or args.only == "insights"
    connections_only = (args.connections_only or args.only == "connections"
                        or args.seed_cache_only)
    _run_insights(topic=args.topic, insights_only=insights_only,
                  connections_only=connections_only, categories=args.categories,
                  seed_cache_only=args.seed_cache_only)


if __name__ == "__main__":
    # 연결 생성이 SPECTER2 임베딩(compute_related_candidates) 을 쓰므로 py312 강제
    # (classify_papers 와 동일 표준 — 다른 인터프리터면 py312 로 자동 재실행).
    from _env_guard import force_py312
    force_py312()
    main()
