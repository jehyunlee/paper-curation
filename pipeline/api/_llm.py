"""
LLM helpers: response caching, tool-use schemas, invariant gates.

Phase 2: ``cached_call`` makes idempotent LLM operations reusable across
runs. A cache hit returns the previously stored response without
touching the LLM. The cache key is ``sha256(model || schema_version ||
prompt)`` truncated to 24 hex chars — enough to make collisions
astronomically unlikely while keeping filenames short.

Phase 3 (Anthropic tool-use migration) will live in this file too:
``tool_use(client, schema, prompt, ...)`` will enforce structured
output via the SDK and retry on schema mismatch, removing the need for
post-hoc fixers (``fix_python_list_literals`` etc.).

Cache layout
------------

Caller picks the directory; conventions used by the existing scripts:

    # per-paper LLM call (review.md generation):
    docs/papers/{slug}/.llm_cache/{hash}.json

    # per-topic LLM call (category summary, insights, timeline narrative):
    docs/{topic}/.llm_cache/{hash}.json

Files are JSON of the shape::

    {"result": <whatever fn() returned>,
     "model": "claude-haiku-4-5-20251001",
     "schema_version": "v1"}
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Callable


def cache_key(prompt: str, model: str, schema_version: str = "v1") -> str:
    """Stable hash for (prompt, model, schema_version). 24 hex chars."""
    h = hashlib.sha256()
    h.update(model.encode("utf-8"))
    h.update(b"\0")
    h.update(schema_version.encode("utf-8"))
    h.update(b"\0")
    h.update(prompt.encode("utf-8"))
    return h.hexdigest()[:24]


def cached_call(cache_dir: str | Path, prompt: str, model: str,
                fn: Callable[[], Any], *,
                schema_version: str = "v1", force: bool = False,
                is_complete: Callable[[Any], bool] | None = None) -> Any:
    """Run ``fn()`` once for a given (prompt, model, schema_version);
    cache the JSON-serialisable return value under ``cache_dir``.

    Subsequent calls with the same key return the cached value without
    invoking ``fn``. Pass ``force=True`` to bypass the cache and refresh
    the stored entry.

    Note: ``fn`` may raise; failures are NOT cached.

    ``is_complete`` guards against caching a *successful but partial* answer.
    A review call that returned only ``essence`` was stored and then replayed
    forever, so the paper's Achievement and Originality sections were
    permanently empty and regenerating the review changed nothing — 488 papers
    ended up holding such an entry. A result that fails this predicate is
    returned to the caller but never written, and a cached entry that fails it
    is discarded rather than replayed.
    """
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    key = cache_key(prompt, model, schema_version)
    cache_path = cache_dir / f"{key}.json"

    if cache_path.exists() and not force:
        try:
            with open(cache_path, "r", encoding="utf-8") as f:
                cached = json.load(f)["result"]
            if is_complete is None or is_complete(cached):
                return cached
        except (json.JSONDecodeError, KeyError):
            # Corrupt cache — fall through and recompute.
            pass

    result = fn()
    if is_complete is not None and not is_complete(result):
        return result
    payload = {"result": result, "model": model,
               "schema_version": schema_version}
    tmp = cache_path.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    tmp.replace(cache_path)
    return result


def topic_cache_dir(topic: str) -> Path:
    """Standard cache location for topic-scoped LLM calls."""
    from config_loader import get_topic_dir
    return Path(get_topic_dir(topic)) / ".llm_cache"


def paper_cache_dir(slug: str) -> Path:
    """Standard cache location for per-paper LLM calls."""
    from config_loader import PAPERS_DIR
    return Path(PAPERS_DIR) / slug / ".llm_cache"


__all__ = ["cache_key", "cached_call", "topic_cache_dir", "paper_cache_dir"]
