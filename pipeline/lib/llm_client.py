"""LLM client factories — prefer OpenRouter, fall back to vendor SDKs.

Typical usage::

    from lib.llm_client import get_chat_client, resolve_model

    client = get_chat_client(timeout=180.0)
    resp = client.messages.create(
        model=resolve_model("sonnet"),  # or a short id like "claude-sonnet-5"
        max_tokens=4000,
        messages=[{"role": "user", "content": "..."}],
    )
"""
from __future__ import annotations

import os
from typing import Any, Optional

try:
    from config_loader import (
        get_openrouter_config,
        load_config,
    )
except ImportError:  # pragma: no cover
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from config_loader import get_openrouter_config, load_config


def resolve_model(role_or_id: str = "sonnet") -> str:
    """Resolve a role (``haiku``/``sonnet``/``opus``/``embed``/``vision``/``tts``)
    or a short Claude id to the model string callers should pass.

    When OpenRouter is configured, returns an OpenRouter slug
    (``anthropic/claude-sonnet-5``). Otherwise returns the short Anthropic id
    so the legacy SDK still works.
    """
    from lib import openrouter as orouter

    cfg = get_openrouter_config()
    if cfg:
        return orouter.resolve_openrouter_model(role_or_id, role_or_id
                                                 if role_or_id in (cfg.get("models") or {})
                                                 else "sonnet")
    # Legacy Anthropic short ids
    legacy = {
        "haiku": "claude-haiku-4-5",
        "sonnet": "claude-sonnet-5",
        "opus": "claude-opus-5",
        "embed": "gemini-embedding-001",
        "vision": "gemini-2.5-flash",
        "tts": "gemini-2.5-flash-preview-tts",
    }
    return legacy.get(role_or_id, role_or_id)


def get_chat_client(*, timeout: float = 180.0, max_retries: int = 4,
                    prefer: str = "openrouter",
                    api_key: str | None = None) -> Any:
    """Return a client exposing Anthropic-shaped ``.messages.create``.

    Preference order:
      1. OpenRouter shim (when ``OPENROUTER_API_KEY`` / config present)
      2. Real ``anthropic.Anthropic`` (legacy ``ANTHROPIC_API_KEY``)
    """
    if prefer == "openrouter" or prefer == "auto":
        from lib import openrouter as orouter
        if orouter.available() or (api_key and str(api_key).startswith("sk-or-")):
            return orouter.OpenRouterAnthropicShim(
                api_key=api_key, timeout=timeout, max_retries=max_retries)

    # Legacy Anthropic
    from anthropic import Anthropic
    key = api_key or os.environ.get("ANTHROPIC_API_KEY") or ""
    if not key:
        try:
            key = load_config().get("anthropic_api_key", "") or ""
        except Exception:
            key = ""
    if not key:
        raise RuntimeError(
            "No LLM backend configured — set OPENROUTER_API_KEY "
            "(preferred) or ANTHROPIC_API_KEY"
        )
    return Anthropic(api_key=key, timeout=timeout, max_retries=max_retries)


def try_chat_client(**kwargs) -> Optional[Any]:
    """Like ``get_chat_client`` but returns None instead of raising."""
    try:
        return get_chat_client(**kwargs)
    except Exception:
        return None


def get_embed_config() -> dict:
    """Return ``{model, dimensions, backend}`` for the active embed path."""
    cfg = get_openrouter_config()
    if cfg:
        return {
            "backend": "openrouter",
            "model": (cfg.get("models") or {}).get("embed",
                                                    "qwen/qwen3-embedding-8b"),
            "dimensions": int(cfg.get("embed_dimensions") or 768),
            "api_key": cfg["api_key"],
            "base_url": cfg["base_url"],
        }
    return {
        "backend": "gemini",
        "model": "gemini-embedding-001",
        "dimensions": 768,
        "api_key": (os.environ.get("GOOGLE_API_KEY")
                    or os.environ.get("GEMINI_API_KEY") or ""),
        "base_url": "",
    }


__all__ = [
    "resolve_model",
    "get_chat_client",
    "try_chat_client",
    "get_embed_config",
]
