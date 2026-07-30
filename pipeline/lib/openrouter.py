"""OpenRouter unified client: chat / tools / embed / vision / TTS.

Also provides an Anthropic ``messages.create``-compatible shim so existing
callers that expect ``client.messages.create(...)`` → ``resp.content[*]``
keep working without per-file rewrites.
"""
from __future__ import annotations

import base64
import json
import math
import os
import re
import ssl
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from io import BytesIO
from types import SimpleNamespace
from typing import Any, Iterator, Optional

# pipeline/ is on sys.path for most callers; tolerate both layouts.
try:
    from config_loader import get_openrouter_config
except ImportError:  # pragma: no cover
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from config_loader import get_openrouter_config

_SSL_CTX = ssl.create_default_context()
_SSL_CTX.check_hostname = False
_SSL_CTX.verify_mode = ssl.CERT_NONE

# Short Anthropic-style ids → OpenRouter slugs (when OpenRouter is active).
_MODEL_ALIASES = {
    "claude-haiku-4-5": "anthropic/claude-haiku-4.5",
    "claude-haiku-4.5": "anthropic/claude-haiku-4.5",
    "claude-haiku-4-5-20251001": "anthropic/claude-haiku-4.5",
    "claude-sonnet-5": "anthropic/claude-sonnet-5",
    "claude-opus-5": "anthropic/claude-opus-5",
    "gemini-2.5-flash": "google/gemini-2.5-flash",
    "gemini-3.1-pro-preview": "google/gemini-2.5-flash",
    "gemini-3.1-flash-lite": "google/gemini-2.5-flash",
    "gemini-embedding-001": "qwen/qwen3-embedding-8b",
}


def _cfg_or_raise() -> dict:
    cfg = get_openrouter_config()
    if not cfg:
        raise RuntimeError(
            "OPENROUTER_API_KEY missing — set env or config.json openrouter.api_key"
        )
    return cfg


def resolve_openrouter_model(model: str | None, role: str = "sonnet") -> str:
    """Map a short/legacy model id (or None) to an OpenRouter slug."""
    cfg = get_openrouter_config() or {}
    models = cfg.get("models") or {}
    if not model:
        return models.get(role) or _MODEL_ALIASES.get(
            role, f"anthropic/claude-{role}-5" if role != "haiku"
            else "anthropic/claude-haiku-4.5")
    if model in models.values():
        return model
    if "/" in model:
        return model
    if model in _MODEL_ALIASES:
        return _MODEL_ALIASES[model]
    # Role name passed as model
    if model in models:
        return models[model]
    # Best-effort: prefix anthropic/ if it looks like a Claude id
    if model.startswith("claude-"):
        # claude-haiku-4-5 → anthropic/claude-haiku-4.5
        fixed = model.replace("claude-haiku-4-5", "claude-haiku-4.5")
        return f"anthropic/{fixed}"
    return model


def _headers(cfg: dict, *, json_body: bool = True) -> dict:
    h = {
        "Authorization": f"Bearer {cfg['api_key']}",
        "X-Title": cfg.get("app_title") or "paper-curation",
    }
    if json_body:
        h["Content-Type"] = "application/json"
    referer = cfg.get("http_referer") or ""
    if referer:
        h["HTTP-Referer"] = referer
    return h


def _request(method: str, url: str, headers: dict, body: bytes | None = None,
             timeout: float = 180.0, stream: bool = False):
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    return urllib.request.urlopen(req, timeout=timeout, context=_SSL_CTX)


def _post_json(path: str, payload: dict, *, timeout: float = 180.0,
               cfg: dict | None = None) -> dict:
    cfg = cfg or _cfg_or_raise()
    url = f"{cfg['base_url'].rstrip('/')}/{path.lstrip('/')}"
    data = json.dumps(payload).encode("utf-8")
    last_err = None
    for attempt in range(4):
        try:
            with _request("POST", url, _headers(cfg), data, timeout=timeout) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="replace")[:400]
            last_err = RuntimeError(f"OpenRouter HTTP {e.code}: {detail}")
            if e.code in (408, 429, 500, 502, 503, 504) and attempt < 3:
                time.sleep(min(30, 2 ** attempt))
                continue
            raise last_err from e
        except Exception as e:
            last_err = e
            if attempt < 3:
                time.sleep(min(30, 2 ** attempt))
                continue
            raise
    raise RuntimeError(f"OpenRouter request failed: {last_err}")


# ── chat / tools ──────────────────────────────────────────────────────────

def chat(messages: list[dict], *, model: str | None = None, role: str = "sonnet",
         max_tokens: int = 4096, temperature: float | None = None,
         tools: list[dict] | None = None, tool_choice: Any = None,
         response_format: dict | None = None, timeout: float = 180.0,
         cfg: dict | None = None) -> dict:
    """OpenAI-compatible chat.completions. Returns raw OpenRouter JSON."""
    cfg = cfg or _cfg_or_raise()
    payload: dict[str, Any] = {
        "model": resolve_openrouter_model(model, role),
        "messages": messages,
        "max_tokens": max_tokens,
    }
    if temperature is not None:
        payload["temperature"] = temperature
    if tools:
        payload["tools"] = tools
    if tool_choice is not None:
        payload["tool_choice"] = tool_choice
    if response_format is not None:
        payload["response_format"] = response_format
    return _post_json("chat/completions", payload, timeout=timeout, cfg=cfg)


def chat_text(messages: list[dict], **kwargs) -> str:
    data = chat(messages, **kwargs)
    choice = (data.get("choices") or [{}])[0]
    msg = choice.get("message") or {}
    return (msg.get("content") or "").strip()


# ── embeddings ────────────────────────────────────────────────────────────

def embed(texts: list[str] | str, *, model: str | None = None,
          dimensions: int | None = None, timeout: float = 60.0,
          cfg: dict | None = None) -> list[list[float]]:
    """Embed one or many texts. Returns L2-normalised float vectors."""
    cfg = cfg or _cfg_or_raise()
    if isinstance(texts, str):
        texts = [texts]
    if not texts:
        return []
    payload: dict[str, Any] = {
        "model": resolve_openrouter_model(model, "embed"),
        "input": texts,
    }
    dim = dimensions if dimensions is not None else cfg.get("embed_dimensions")
    if dim:
        payload["dimensions"] = int(dim)
    data = _post_json("embeddings", payload, timeout=timeout, cfg=cfg)
    items = sorted(data.get("data") or [], key=lambda x: x.get("index", 0))
    out = []
    for item in items:
        vec = list(item.get("embedding") or [])
        if not vec:
            raise RuntimeError("OpenRouter embedding response missing vector")
        norm = math.sqrt(sum(v * v for v in vec)) or 1.0
        out.append([v / norm for v in vec])
    if len(out) != len(texts):
        raise RuntimeError(
            f"embedding count {len(out)} != input count {len(texts)}"
        )
    return out


def embed_one(text: str, **kwargs) -> list[float]:
    return embed([text], **kwargs)[0]


# ── vision ────────────────────────────────────────────────────────────────

def vision_json(prompt: str, image_bytes: bytes, *, mime: str = "image/png",
                model: str | None = None, max_tokens: int = 1024,
                timeout: float = 120.0) -> dict:
    """Multimodal chat → parse JSON object from the model reply."""
    b64 = base64.b64encode(image_bytes).decode("ascii")
    messages = [{
        "role": "user",
        "content": [
            {"type": "text", "text": prompt},
            {"type": "image_url",
             "image_url": {"url": f"data:{mime};base64,{b64}"}},
        ],
    }]
    text = chat_text(messages, model=model, role="vision",
                     max_tokens=max_tokens, timeout=timeout)
    if "```" in text:
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    text = text.strip()
    start, end = text.find("{"), text.rfind("}")
    if start != -1 and end > start:
        text = text[start:end + 1]
    return json.loads(text)


# ── TTS ───────────────────────────────────────────────────────────────────

def tts(text: str, *, model: str | None = None, voice: str = "alloy",
        response_format: str = "mp3", timeout: float = 180.0,
        cfg: dict | None = None) -> bytes:
    """OpenRouter /audio/speech → raw audio bytes (mp3/wav/…)."""
    cfg = cfg or _cfg_or_raise()
    payload = {
        "model": resolve_openrouter_model(model, "tts"),
        "input": text,
        "voice": voice,
        "response_format": response_format,
    }
    url = f"{cfg['base_url'].rstrip('/')}/audio/speech"
    data = json.dumps(payload).encode("utf-8")
    with _request("POST", url, _headers(cfg), data, timeout=timeout) as resp:
        return resp.read()


# ── Anthropic messages.create shim ────────────────────────────────────────

@dataclass
class _TextBlock:
    type: str = "text"
    text: str = ""


@dataclass
class _ToolUseBlock:
    type: str = "tool_use"
    id: str = ""
    name: str = ""
    input: dict = field(default_factory=dict)


@dataclass
class _MessageResponse:
    content: list = field(default_factory=list)
    model: str = ""
    stop_reason: str = "end_turn"
    usage: Any = None

    def __iter__(self):
        return iter(self.content)


def _anthropic_tools_to_openai(tools: list[dict] | None) -> list[dict] | None:
    if not tools:
        return None
    out = []
    for t in tools:
        if t.get("type") == "function" and "function" in t:
            out.append(t)
            continue
        # Anthropic tool schema: {name, description, input_schema}
        name = t.get("name") or (t.get("function") or {}).get("name")
        if not name:
            continue
        out.append({
            "type": "function",
            "function": {
                "name": name,
                "description": t.get("description") or "",
                "parameters": t.get("input_schema")
                             or t.get("parameters")
                             or {"type": "object", "properties": {}},
            },
        })
    return out or None


def _anthropic_tool_choice_to_openai(tool_choice: Any) -> Any:
    if tool_choice is None:
        return None
    if isinstance(tool_choice, str):
        return tool_choice
    if not isinstance(tool_choice, dict):
        return None
    t = tool_choice.get("type")
    if t == "auto":
        return "auto"
    if t == "any":
        return "required"
    if t == "tool" and tool_choice.get("name"):
        return {"type": "function", "function": {"name": tool_choice["name"]}}
    if t == "function":
        return tool_choice
    return None


def _messages_anthropic_to_openai(messages: list[dict],
                                  system: str | list | None = None) -> list[dict]:
    out: list[dict] = []
    if system:
        if isinstance(system, list):
            # Anthropic system blocks
            parts = []
            for b in system:
                if isinstance(b, dict) and b.get("text"):
                    parts.append(b["text"])
                elif isinstance(b, str):
                    parts.append(b)
            sys_text = "\n".join(parts)
        else:
            sys_text = str(system)
        if sys_text.strip():
            out.append({"role": "system", "content": sys_text})
    for m in messages or []:
        role = m.get("role", "user")
        content = m.get("content")
        if isinstance(content, str):
            out.append({"role": role, "content": content})
            continue
        if isinstance(content, list):
            # Flatten text + image blocks; drop tool_result for now
            parts = []
            text_bits = []
            for b in content:
                if not isinstance(b, dict):
                    text_bits.append(str(b))
                    continue
                btype = b.get("type")
                if btype == "text":
                    text_bits.append(b.get("text") or "")
                elif btype == "image":
                    src = b.get("source") or {}
                    if src.get("type") == "base64":
                        mime = src.get("media_type") or "image/png"
                        data = src.get("data") or ""
                        parts.append({
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:{mime};base64,{data}"
                            },
                        })
            if text_bits:
                parts.insert(0, {"type": "text", "text": "\n".join(text_bits)})
            if len(parts) == 1 and parts[0].get("type") == "text":
                out.append({"role": role, "content": parts[0]["text"]})
            elif parts:
                out.append({"role": role, "content": parts})
            continue
        out.append({"role": role, "content": str(content or "")})
    return out


def _openai_message_to_anthropic(msg: dict, model: str) -> _MessageResponse:
    blocks: list = []
    text = msg.get("content")
    if text:
        blocks.append(_TextBlock(text=text))
    for tc in msg.get("tool_calls") or []:
        fn = tc.get("function") or {}
        raw_args = fn.get("arguments") or "{}"
        try:
            args = json.loads(raw_args) if isinstance(raw_args, str) else dict(raw_args)
        except json.JSONDecodeError:
            args = {"_raw": raw_args}
        blocks.append(_ToolUseBlock(
            id=tc.get("id") or f"toolu_{len(blocks)}",
            name=fn.get("name") or "",
            input=args if isinstance(args, dict) else {"value": args},
        ))
    # JSON fallback: if tools were requested but model returned JSON in text
    # matching a single tool schema, wrap it as tool_use (handled by caller
    # when they iterate content looking for tool_use).
    return _MessageResponse(content=blocks, model=model,
                            stop_reason="tool_use" if any(
                                getattr(b, "type", None) == "tool_use"
                                for b in blocks) else "end_turn")


def _json_fallback_tool_use(text: str, tools: list[dict] | None
                            ) -> _MessageResponse | None:
    """If the model ignored tool_calls but returned JSON, promote to tool_use."""
    if not text or not tools:
        return None
    names = []
    for t in tools:
        if t.get("name"):
            names.append(t["name"])
        elif (t.get("function") or {}).get("name"):
            names.append(t["function"]["name"])
    if not names:
        return None
    s = text.strip()
    if "```" in s:
        s = s.split("```")[1]
        if s.startswith("json"):
            s = s[4:]
    start, end = s.find("{"), s.rfind("}")
    if start == -1 or end <= start:
        return None
    try:
        obj = json.loads(s[start:end + 1])
    except json.JSONDecodeError:
        return None
    if not isinstance(obj, dict):
        return None
    return _MessageResponse(
        content=[_ToolUseBlock(id="toolu_fallback", name=names[0], input=obj)],
        stop_reason="tool_use",
    )


class _StreamCtx:
    """Minimal stand-in for Anthropic ``messages.stream`` context manager."""

    def __init__(self, text: str):
        self._text = text
        self.text_stream = iter([text]) if text else iter([])

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def get_final_message(self) -> _MessageResponse:
        return _MessageResponse(content=[_TextBlock(text=self._text)])


class _MessagesAPI:
    def __init__(self, client: "OpenRouterAnthropicShim"):
        self._client = client

    def create(self, *, model: str, max_tokens: int = 4096,
               messages: list | None = None, system: str | list | None = None,
               tools: list | None = None, tool_choice: Any = None,
               temperature: float | None = None, stream: bool = False,
               **_extra) -> _MessageResponse:
        if stream:
            # Non-streaming fetch then fake a stream — keeps call sites simple.
            resp = self.create(model=model, max_tokens=max_tokens,
                               messages=messages, system=system, tools=tools,
                               tool_choice=tool_choice, temperature=temperature)
            text = "".join(getattr(b, "text", "") or ""
                           for b in resp.content
                           if getattr(b, "type", None) == "text")
            return _StreamCtx(text)  # type: ignore[return-value]

        oai_messages = _messages_anthropic_to_openai(messages or [], system)
        oai_tools = _anthropic_tools_to_openai(tools)
        oai_choice = _anthropic_tool_choice_to_openai(tool_choice)
        # Prefer JSON object mode when a forced single tool is requested and
        # the provider drops tool_calls — chat still runs with tools first.
        data = chat(
            oai_messages,
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            tools=oai_tools,
            tool_choice=oai_choice,
            timeout=self._client._timeout,
            cfg=self._client._cfg,
        )
        choice = (data.get("choices") or [{}])[0]
        msg = choice.get("message") or {}
        resolved = resolve_openrouter_model(model)
        resp = _openai_message_to_anthropic(msg, resolved)
        if tools and not any(getattr(b, "type", None) == "tool_use"
                             for b in resp.content):
            text = msg.get("content") or ""
            fb = _json_fallback_tool_use(text, tools)
            if fb is not None:
                return fb
        return resp

    def stream(self, **kwargs) -> _StreamCtx:
        kwargs = dict(kwargs)
        kwargs.pop("stream", None)
        resp = self.create(**kwargs)
        text = "".join(getattr(b, "text", "") or ""
                       for b in resp.content
                       if getattr(b, "type", None) == "text")
        # Also surface tool JSON as text for stream consumers that only
        # read text_stream (timeline narrative etc.).
        if not text:
            for b in resp.content:
                if getattr(b, "type", None) == "tool_use":
                    text = json.dumps(getattr(b, "input", {}), ensure_ascii=False)
                    break
        return _StreamCtx(text)


class OpenRouterAnthropicShim:
    """Drop-in for ``anthropic.Anthropic`` used by pipeline call sites."""

    def __init__(self, *, api_key: str | None = None, timeout: float = 180.0,
                 max_retries: int = 4, base_url: str | None = None, **_kw):
        cfg = get_openrouter_config()
        if cfg is None and api_key:
            cfg = {
                "api_key": api_key,
                "base_url": (base_url or "https://openrouter.ai/api/v1").rstrip("/"),
                "models": {},
                "embed_dimensions": 768,
                "http_referer": "",
                "app_title": "paper-curation",
            }
        if cfg is None:
            raise RuntimeError("OPENROUTER_API_KEY missing")
        if api_key:
            cfg = dict(cfg)
            cfg["api_key"] = api_key
        if base_url:
            cfg = dict(cfg)
            cfg["base_url"] = base_url.rstrip("/")
        self._cfg = cfg
        self._timeout = float(timeout)
        self._max_retries = int(max_retries)
        self.messages = _MessagesAPI(self)

    def with_options(self, *, timeout: float | None = None,
                     max_retries: int | None = None, **_kw) -> "OpenRouterAnthropicShim":
        return OpenRouterAnthropicShim(
            api_key=self._cfg["api_key"],
            timeout=timeout if timeout is not None else self._timeout,
            max_retries=(max_retries if max_retries is not None
                         else self._max_retries),
            base_url=self._cfg["base_url"],
        )


def available() -> bool:
    return get_openrouter_config() is not None


__all__ = [
    "available",
    "chat",
    "chat_text",
    "embed",
    "embed_one",
    "vision_json",
    "tts",
    "resolve_openrouter_model",
    "OpenRouterAnthropicShim",
]
