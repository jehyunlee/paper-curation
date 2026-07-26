"""주제 필터링 + 5W1H 요약 — citedby 의 LLM 단계.

scisci `scie/lib/topic_filter.py` 이식본. 인용논문 목록을 사용자가 준 주제로
걸러내고, 통과한 논문마다 What/How/Result/Relevance 구조 요약을 만든다.

이식하며 바뀐 점 (계획된 중복 제거):
  1. **구 Gemini SDK 제거** — 원본은 `google.generativeai`(deprecated) 를 썼다.
     paper-curation 표준인 `google-genai` 로 마이그레이션했다. 안 하면 py312 에
     deprecated 패키지가 딸려 들어와 충돌한다.
  2. **`llm_call_with_retry` → `api/_llm.cached_call`** — scisci 자체 재시도
     헬퍼(utils.py) 대신 paper-curation 의 SHA-256 캐시 호출을 쓴다. 같은
     (프롬프트, 모델) 조합은 재실행 시 **LLM 호출 0회** → 동일 DOI 재분석이 공짜.
  3. **`import MyAPIKEY` 제거** — 개인 로컬 모듈 의존을 걷어내고 env →
     config.json 순으로만 키를 찾는다.
"""
from __future__ import annotations

import json
import logging
import os
import re
from pathlib import Path

logger = logging.getLogger(__name__)

# 배치 분류/요약은 저비용 tier 로 충분하다. paper-curation 의 다른 배치 단계
# (build_category_summaries) 와 같은 급을 쓴다.
DEFAULT_MODELS = (
    ("anthropic", "claude-haiku-4-5"),
    ("google", "gemini-3.1-flash-lite"),
    ("openai", "gpt-4.1"),
)

FILTER_BATCH_SIZE = 15
SUMMARY_BATCH_SIZE = 5      # 출력이 길어 배치를 작게 잡는다

_LANG_NAME = {"ko": "Korean", "en": "English"}

_ENV_KEYS = {
    "anthropic": ("ANTHROPIC_API_KEY", "CLAUDE_API_KEY"),
    "google": ("GOOGLE_API_KEY", "GEMINI_API_KEY"),
    "openai": ("OPENAI_API_KEY",),
}

_CONFIG_KEYS = {
    "anthropic": ("anthropic_api_key",),
    "google": ("google_api_key", "gemini_api_key"),
    "openai": ("openai_api_key",),
}


def resolve_keys() -> dict[str, str]:
    """LLM 제공자별 API 키. env 우선, 없으면 config.json.

    scisci 의 `MyAPIKEY` 폴백은 제거했다 (개인 로컬 모듈 의존).
    """
    keys: dict[str, str] = {}
    for provider, names in _ENV_KEYS.items():
        for n in names:
            v = (os.environ.get(n) or "").strip()
            if v:
                keys[provider] = v
                break

    missing = [p for p in _ENV_KEYS if p not in keys]
    if missing:
        cfg = {}
        try:
            cfg_path = Path(__file__).resolve().parents[3] / "config.json"
            if cfg_path.exists():
                cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001 — 키 조회 실패가 전체를 죽이지 않게
            logger.debug("config.json 읽기 실패: %s", e)
        for provider in missing:
            for field in _CONFIG_KEYS[provider]:
                v = (cfg.get(field) or "").strip()
                if v:
                    keys[provider] = v
                    break
    return keys


def _parse_json(text: str):
    """LLM 응답에서 JSON 오브젝트를 뽑는다. 코드펜스/잡텍스트를 허용."""
    if not text:
        return None
    s = text.strip()
    s = re.sub(r"^```(?:json)?\s*", "", s)
    s = re.sub(r"\s*```$", "", s)
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        pass
    # 본문에 섞여 있으면 첫 {...} 블록만 잘라 재시도
    start = s.find("{")
    end = s.rfind("}")
    if start != -1 and end > start:
        try:
            return json.loads(s[start:end + 1])
        except json.JSONDecodeError:
            return None
    return None


_JSON_SYSTEM = "You are a JSON-only responder. Output ONLY valid JSON."


def _call_anthropic(key: str, model: str, prompt: str, max_tokens: int,
                    system: str = _JSON_SYSTEM) -> str:
    from anthropic import Anthropic
    client = Anthropic(api_key=key, timeout=180.0, max_retries=4)
    resp = client.messages.create(
        model=model, max_tokens=max_tokens, system=system,
        messages=[{"role": "user", "content": prompt}],
    )
    return "".join(b.text for b in resp.content
                   if getattr(b, "type", "") == "text")


def _call_google(key: str, model: str, prompt: str, max_tokens: int,
                 system: str = _JSON_SYSTEM) -> str:
    """신 SDK(`google-genai`). 원본의 `google.generativeai` 는 deprecated."""
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=key)
    resp = client.models.generate_content(
        model=model,
        contents=(f"{system}\n\n{prompt}" if system else prompt),
        config=types.GenerateContentConfig(
            temperature=0,
            max_output_tokens=max_tokens,
            response_mime_type=("application/json"
                                if system == _JSON_SYSTEM else "text/plain"),
        ),
    )
    return resp.text or ""


def _call_openai(key: str, model: str, prompt: str, max_tokens: int,
                 system: str = _JSON_SYSTEM) -> str:
    from openai import OpenAI
    client = OpenAI(api_key=key, timeout=180.0, max_retries=4)
    resp = client.chat.completions.create(
        model=model,
        max_completion_tokens=max_tokens,
        **({"response_format": {"type": "json_object"}}
           if system == _JSON_SYSTEM else {}),
        messages=[{"role": "system", "content": system},
                  {"role": "user", "content": prompt}],
    )
    return resp.choices[0].message.content or ""


_CALLERS = {
    "anthropic": _call_anthropic,
    "google": _call_google,
    "openai": _call_openai,
}


def llm_json(prompt: str, *, max_tokens: int = 1024,
             keys: dict | None = None,
             models=None,
             cache_dir=None):
    """3-provider cascade 로 JSON 응답을 받는다. 실패하면 None.

    Anthropic → Google → OpenAI 순으로 키가 있는 것만 시도한다. 각 호출은
    `api/_llm.cached_call` 로 감싸므로, 같은 (프롬프트, 모델) 은 재실행 시
    네트워크를 타지 않는다 — 동일 DOI 재분석이 무료가 되는 지점.
    """
    keys = resolve_keys() if keys is None else keys
    models = list(models or DEFAULT_MODELS)

    for provider, model in models:
        key = keys.get(provider, "")
        if not key:
            continue
        caller = _CALLERS.get(provider)
        if caller is None:
            continue

        def _run(_c=caller, _k=key, _m=model):
            return _c(_k, _m, prompt, max_tokens)

        try:
            if cache_dir:
                from api._llm import cached_call
                raw = cached_call(cache_dir, prompt, model, _run,
                                  schema_version="citedby-v1")
            else:
                raw = _run()
        except Exception as e:  # noqa: BLE001 — 다음 provider 로 넘어간다
            logger.warning("citedby LLM 실패 (%s/%s): %s", provider, model,
                           str(e)[:160])
            continue

        parsed = _parse_json(raw if isinstance(raw, str) else str(raw))
        if parsed is not None:
            return parsed
        logger.warning("citedby LLM 응답 JSON 파싱 실패 (%s/%s)", provider, model)

    return None


# ── 주제 필터링 ───────────────────────────────────────────────────────────

_FILTER_PROMPT = """You are a scientific paper classifier.

For each paper below, determine if it is relevant to the following topic:
**"{topic}"**

Papers:
{papers}

Return a JSON object:
{{
  "results": [
    {{"paper": 1, "relevant": true, "reason": "brief reason"}},
    {{"paper": 2, "relevant": false, "reason": "brief reason"}}
  ]
}}

Rules:
- "relevant" is true if the paper's originality/abstract is clearly related to the topic.
- "reason" should be a brief (1 sentence) explanation.
- You MUST return exactly {n_papers} results, in order.
- Be selective: only mark as relevant if there is a clear, substantive connection.
"""


def _format_for_filter(papers: list[dict]) -> str:
    parts = []
    for i, p in enumerate(papers, 1):
        content = (p.get("originality") or "").strip() or \
                  (p.get("abstract") or "")[:500]
        parts.append(f"[Paper {i}]\nTitle: {p.get('title', '')}\nContent: {content}")
    return "\n\n".join(parts)


def _apply_batch_results(slots: list, items: list, start: int, size: int,
                         builder) -> None:
    """배치 응답을 slots 에 반영. 개수가 맞으면 순서대로, 아니면 `paper` 인덱스로.

    LLM 이 요청한 개수와 다르게 돌려주는 일이 흔해서 두 경로를 모두 둔다.
    """
    if len(items) == size:
        for i, item in enumerate(items):
            slots[start + i] = builder(item)
        return
    for item in items:
        idx = (item.get("paper") or 0) - 1
        if 0 <= idx < size:
            slots[start + idx] = builder(item)


def filter_by_topic(papers: list[dict], topic: str, *,
                    keys: dict | None = None,
                    models=None,
                    cache_dir=None,
                    progress_callback=None) -> list[dict]:
    """주제 관련성으로 논문을 거른다. 통과분에 `topic_reason` 을 붙여 반환."""
    papers = list(papers or [])
    total = len(papers)
    if not total or not topic.strip():
        return []

    verdicts: list[dict | None] = [None] * total

    for start in range(0, total, FILTER_BATCH_SIZE):
        batch = papers[start:start + FILTER_BATCH_SIZE]
        end = min(start + FILTER_BATCH_SIZE, total)
        if progress_callback:
            progress_callback("topic_filter",
                              f"주제 필터링: {start + 1}-{end}/{total}", end, total)

        result = llm_json(
            _FILTER_PROMPT.format(topic=topic, papers=_format_for_filter(batch),
                                  n_papers=len(batch)),
            max_tokens=128 * len(batch), keys=keys, models=models,
            cache_dir=cache_dir,
        )
        if not result or "results" not in result:
            continue
        _apply_batch_results(
            verdicts, result["results"] or [], start, len(batch),
            lambda item: {"relevant": bool(item.get("relevant", False)),
                          "reason": item.get("reason", "")},
        )

    filtered = []
    for i, paper in enumerate(papers):
        v = verdicts[i]
        if v and v["relevant"]:
            p = dict(paper)
            p["topic_reason"] = v["reason"]
            filtered.append(p)

    logger.info("Topic filter: %d/%d papers match %r", len(filtered), total, topic)
    return filtered


# ── 5W1H 요약 ─────────────────────────────────────────────────────────────

_SUMMARY_PROMPT = """You are a scientific paper analyst.

For each paper below, generate a structured summary answering:
- **What**: What is the main contribution or finding?
- **How**: What methodology or approach was used?
- **Result**: What are the key results or conclusions?
- **Relevance**: How does this relate to "{topic}"?

Papers:
{papers}

Return a JSON object:
{{
  "results": [
    {{"paper": 1, "what": "...", "how": "...", "result": "...", "relevance": "..."}}
  ]
}}

Rules:
- Write in {lang}.
- Use bulletin (개조식) style: short, concise phrases. Not full sentences.
- Include specific numerical data whenever available (percentages, counts, scores).
- Base your answers on the abstract and originality content provided.
- You MUST return exactly {n_papers} results, in order.
"""


def _format_for_summary(papers: list[dict]) -> str:
    parts = []
    for i, p in enumerate(papers, 1):
        originality = (p.get("originality") or "").strip()
        abstract = (p.get("abstract") or "")[:1200]
        parts.append(
            f"[Paper {i}]\nTitle: {p.get('title', '')}\n"
            f"Originality: {originality}\nAbstract: {abstract}"
        )
    return "\n\n".join(parts)


_SUMMARY_FIELDS = ("what", "how", "result", "relevance")


def generate_summaries(papers: list[dict], topic: str, *,
                       lang: str = "ko",
                       keys: dict | None = None,
                       models=None,
                       cache_dir=None,
                       progress_callback=None) -> list[dict]:
    """논문마다 5W1H 요약을 만들어 `summary` 키로 붙인 새 리스트를 반환.

    요약 생성이 실패한 논문은 `summary` 없이 그대로 통과한다 — 리포트 렌더러가
    표를 생략하므로 부분 실패가 전체를 막지 않는다.
    """
    papers = [dict(p) for p in (papers or [])]
    total = len(papers)
    if not total:
        return papers

    lang_name = _LANG_NAME.get(lang, "Korean")
    slots: list[dict | None] = [None] * total

    for start in range(0, total, SUMMARY_BATCH_SIZE):
        batch = papers[start:start + SUMMARY_BATCH_SIZE]
        end = min(start + SUMMARY_BATCH_SIZE, total)
        if progress_callback:
            progress_callback("summary",
                              f"요약 생성: {start + 1}-{end}/{total}", end, total)

        result = llm_json(
            _SUMMARY_PROMPT.format(topic=topic, lang=lang_name,
                                   papers=_format_for_summary(batch),
                                   n_papers=len(batch)),
            max_tokens=600 * len(batch), keys=keys, models=models,
            cache_dir=cache_dir,
        )
        if not result or "results" not in result:
            continue
        _apply_batch_results(
            slots, result["results"] or [], start, len(batch),
            lambda item: {f: (item.get(f) or "").strip()
                          for f in _SUMMARY_FIELDS},
        )

    filled = 0
    for i, summary in enumerate(slots):
        if summary and any(summary.values()):
            papers[i]["summary"] = summary
            filled += 1

    logger.info("5W1H summaries: %d/%d generated", filled, total)
    return papers


# ── 자유 텍스트 (Deep Research 답변) ──────────────────────────────────────

# 답변 전용 모델 — DEFAULT_MODELS 는 배치 분류용 저비용 tier 라 답변에는 얇다.
# 근거 6만 자를 읽고 논문을 비교하는 작업이므로 최상위를 쓴다.
ANSWER_MODELS = (
    ("anthropic", "claude-opus-5"),
    ("google", "gemini-3.5-flash"),
    ("openai", "gpt-5.5"),
)

TEXT_SYSTEM = ("You are a careful research assistant. Answer in prose, "
               "grounded strictly in the provided excerpts.")


def llm_text(prompt: str, *, max_tokens: int = 8000,
             keys: dict | None = None, models=None) -> tuple[str, str, str]:
    """3-provider cascade 로 **자유 텍스트** 답변을 받는다.

    `llm_json` 과 달리 JSON 을 강제하지 않는다 — 그 system 프롬프트를 그대로
    쓰면 답변이 ```json {...} 로 감싸여 나온다 (실제로 그랬다).

    Returns:
        (answer, provider, model) — 전부 실패하면 ("", "", "").
    """
    keys = resolve_keys() if keys is None else keys
    for provider, model in list(models or ANSWER_MODELS):
        key = keys.get(provider)
        caller = _CALLERS.get(provider)
        if not key or caller is None:
            continue
        try:
            text = caller(key, model, prompt, max_tokens, TEXT_SYSTEM)
        except Exception as e:  # noqa: BLE001 — 다음 provider 로
            logger.warning("답변 생성 실패 (%s/%s): %s",
                           provider, model, str(e)[:140])
            continue
        if text and text.strip():
            return text, provider, model
    return "", "", ""
_STREAM_SYSTEM = (
    "You are a careful research assistant. Write a complete, self-contained "
    "answer grounded in the supplied corpus. Never end mid-sentence. When web "
    "search is enabled, corpus excerpts remain primary and every web-derived "
    "claim must carry a descriptive inline markdown link."
)


def _stream_anthropic(key, model, prompt, max_tokens, on_delta, web_search):
    from anthropic import Anthropic

    client = Anthropic(api_key=key, timeout=600.0, max_retries=4)
    kwargs = {
        "model": model,
        "max_tokens": max_tokens,
        "system": _STREAM_SYSTEM,
        "messages": [{"role": "user", "content": prompt}],
        "stream": True,
    }
    if web_search:
        kwargs["tools"] = [{
            "type": ("web_search_20250305" if "haiku-4-5" in model
                     else "web_search_20260209"),
            "name": "web_search",
            "max_uses": 5,
        }]
    answer, stop_reason = [], ""
    for event in client.messages.create(**kwargs):
        if getattr(event, "type", "") == "content_block_delta":
            delta = getattr(event, "delta", None)
            if getattr(delta, "type", "") == "text_delta":
                text = getattr(delta, "text", "") or ""
                if text:
                    answer.append(text)
                    on_delta(text)
        elif getattr(event, "type", "") == "message_delta":
            stop_reason = getattr(getattr(event, "delta", None),
                                  "stop_reason", "") or stop_reason
    return "".join(answer), stop_reason == "max_tokens"


def _stream_google(key, model, prompt, max_tokens, on_delta, web_search):
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=key)
    config = {
        "system_instruction": _STREAM_SYSTEM,
        "temperature": 0.4,
        "max_output_tokens": max_tokens,
    }
    if web_search:
        config["tools"] = [types.Tool(google_search=types.GoogleSearch())]
    answer, truncated = [], False
    for chunk in client.models.generate_content_stream(
            model=model, contents=prompt,
            config=types.GenerateContentConfig(**config)):
        text = getattr(chunk, "text", "") or ""
        if text:
            answer.append(text)
            on_delta(text)
        for cand in getattr(chunk, "candidates", None) or []:
            reason = str(getattr(cand, "finish_reason", "") or "").upper()
            truncated = truncated or "MAX_TOKENS" in reason
    return "".join(answer), truncated


def _stream_openai(key, model, prompt, max_tokens, on_delta, web_search):
    from openai import OpenAI

    if web_search:
        raise RuntimeError("OpenAI citedby web search is not supported")
    client = OpenAI(api_key=key, timeout=600.0, max_retries=4)
    stream = client.chat.completions.create(
        model=model, max_completion_tokens=max_tokens, stream=True,
        messages=[{"role": "system", "content": _STREAM_SYSTEM},
                  {"role": "user", "content": prompt}],
    )
    answer, truncated = [], False
    for event in stream:
        choice = event.choices[0] if getattr(event, "choices", None) else None
        text = getattr(getattr(choice, "delta", None), "content", "") or ""
        if text:
            answer.append(text)
            on_delta(text)
        truncated = truncated or getattr(choice, "finish_reason", "") == "length"
    return "".join(answer), truncated


_STREAM_CALLERS = {
    "anthropic": _stream_anthropic,
    "google": _stream_google,
    "openai": _stream_openai,
}


def llm_text_stream(prompt: str, on_delta, *, max_tokens: int = 16000,
                    web_search: bool = False, keys: dict | None = None,
                    models=None) -> tuple[str, str, str]:
    """Stream a complete answer, continuing once when a provider hits its cap.

    Provider fallback is safe only before any text reaches the browser. Once a
    stream has emitted text, switching providers would duplicate or contradict
    the visible answer, so a mid-stream failure is surfaced to the caller.
    """
    keys = resolve_keys() if keys is None else keys
    for provider, model in list(models or ANSWER_MODELS):
        key = keys.get(provider)
        caller = _STREAM_CALLERS.get(provider)
        if not key or caller is None or (web_search and provider == "openai"):
            continue
        emitted = []
        emit = lambda text: (emitted.append(text), on_delta(text))
        try:
            text, truncated = caller(
                key, model, prompt, max_tokens, emit, web_search)
            if truncated and text.strip():
                continuation = (
                    prompt + "\n\n---\nThe answer below reached the output limit. "
                    "Continue from its final sentence without repeating any text. "
                    "Finish every remaining section and conclusion.\n\n"
                    "PARTIAL ANSWER:\n" + text)
                more, truncated_again = caller(
                    key, model, continuation, max_tokens, emit, web_search)
                text += more
                if truncated_again:
                    raise RuntimeError(
                        f"{provider} response remained truncated after continuation")
        except Exception as e:  # noqa: BLE001
            if emitted:
                raise
            logger.warning("스트리밍 답변 생성 실패 (%s/%s): %s",
                           provider, model, str(e)[:180])
            continue
        if text.strip():
            return text, provider, model
    return "", "", ""
