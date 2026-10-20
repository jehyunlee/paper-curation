"""
LLM verification pass over generated cross-category insights.

Cross-category insights (claims citing paper numbers) are model-written, so this
module adds a best-effort audit that asks a cheap Haiku-class model whether the
cited papers actually back each claim. Paper connections are NOT audited here:
they are found in embedding space without any model (``lib.related``).

Design goals
------------
* **Dependency-light.** This module imports ONLY the Python standard library. The
  LLM client is *passed in* (any object exposing the Anthropic ``messages.create``
  shape, or a stub with the same interface), so importing ``verify`` never pulls in
  ``umap`` / ``hdbscan`` / ``sentence-transformers`` / SPECTER2.
* **Never breaks the default path.** On ANY failure (no client, network error,
  malformed/empty JSON) verification is *skipped* and insights stay
  ``supported=True``. Nothing is ever dropped because of an error.

Public API
----------
``verify_insights(insights, paper_meta, client)``
    For each cross-category insight, ask the model whether its cited papers
    actually back the claim. Annotates each insight *in place* with
    ``supported: bool`` (+ ``verify_reason``) and returns the list of insights.

``apply_insight_verification(insights, paper_meta, client, ...)``
    Thin env-driven wrapper used by the ``extract_insights`` hook.
"""

import json
import os
import re

# Cheap auditor model. Overridable via env for cost/quality tuning.
VERIFY_MODEL = os.environ.get("VERIFY_MODEL", "claude-haiku-4-5")

# ─────────────────────────────────────────────────────────────────────────────
# Small pure helpers (no I/O, no deps)
# ─────────────────────────────────────────────────────────────────────────────

def _slug_num(slug):
    """'045_Foo_Bar' -> '045'. Pass through if there is no underscore."""
    return str(slug).split("_")[0]


def _canon_num(slug):
    """Canonical comparable id: drop leading zeros from a numeric prefix.

    '045'->'45', '45'->'45', '045_Foo'->'45'; non-numeric tokens pass through.
    Lets a model that emits an unpadded number ('45') still match a corpus keyed
    by the zero-padded NNN form ('045'), avoiding false 'not found' → false drops.
    """
    tok = _slug_num(slug)
    return (tok.lstrip("0") or "0") if tok.isdigit() else tok


def _short(text, n):
    """Collapse whitespace and truncate to ``n`` chars (None-safe)."""
    return (text or "").strip().replace("\n", " ")[:n]


def _parse_json_block(text):
    """Best-effort extraction of the first JSON object/array from model text."""
    text = (text or "").strip()
    if text.startswith("```"):
        parts = text.split("```")
        if len(parts) >= 2:
            text = parts[1]
        if text.startswith("json"):
            text = text[4:]
        text = text.strip()
    try:
        return json.loads(text)
    except Exception:
        pass
    m = re.search(r"(\{.*\}|\[.*\])", text, re.DOTALL)
    if m:
        return json.loads(m.group(1))
    raise ValueError("no JSON found in model response")


def _call_text(client, prompt, *, max_tokens=300, model=None):
    """One Haiku-class call; return the first content block's text.

    Works with the real Anthropic SDK client and with stubs exposing the same
    ``messages.create(...)`` → ``resp.content[0].text`` shape.
    """
    resp = client.messages.create(
        model=model or VERIFY_MODEL,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    block = resp.content[0]
    return (getattr(block, "text", None) or "").strip()


# ─────────────────────────────────────────────────────────────────────────────
# Core: insight verification
# ─────────────────────────────────────────────────────────────────────────────

def _cited_meta(ins, paper_meta):
    """Render the papers an insight cites (by number) as readable evidence lines."""
    nums = ins.get("evidence") or ins.get("paper_numbers") or ins.get("papers") or []
    if isinstance(nums, str):
        nums = [nums]
    lines = []
    for n in list(nums)[:12]:
        key = str(n)
        v = paper_meta.get(key)
        if v is None:
            v = paper_meta.get(_slug_num(key))
        if v is None and key.isdigit():
            v = paper_meta.get(key.zfill(3))
        if v is None:
            ckey = _canon_num(key)
            for k, val in paper_meta.items():
                if _canon_num(k) == ckey:
                    v = val
                    break
        if isinstance(v, dict):
            txt = v.get("essence") or v.get("abstract") or v.get("title") or ""
            lines.append(f"[{key}] {v.get('title', '')} | {_short(txt, 300)}")
        elif v:
            lines.append(f"[{key}] {_short(v, 300)}")
        else:
            lines.append(f"[{key}] (not found in corpus)")
    return lines


def _verify_one_insight(client, ins, cited_lines):
    cited_block = "\n".join(cited_lines) if cited_lines else "(no papers cited)"
    prompt = (
        "You are auditing an automatically-generated cross-category research "
        "insight.\n\n"
        f"Insight type: {ins.get('type', '')}\n"
        f"Title: {ins.get('title', '')}\n"
        f"Claim: {_short(ins.get('description', ''), 600)}\n\n"
        "Papers cited as evidence for this claim:\n"
        f"{cited_block}\n\n"
        "Do the cited papers actually support this claim? It is supported ONLY if "
        "at least some cited papers are clearly relevant to the claim. If the cited "
        "papers are about unrelated topics, or no real papers are cited, the claim "
        "is NOT supported.\n"
        "Respond with ONLY a JSON object, no prose:\n"
        '{"supported": true|false, "reason": "<=1 short sentence"}'
    )
    data = _parse_json_block(_call_text(client, prompt, max_tokens=300))
    return {"supported": bool(data.get("supported", True)),
            "reason": str(data.get("reason", ""))}


def verify_insights(insights, paper_meta, client):
    """Annotate each cross-category insight with ``supported: bool``.

    Args:
        insights: the full insights dict (with ``"cross_category"``) OR a plain
            list of insight dicts. Each insight has at least
            ``{"title", "description", "evidence"}`` (evidence = cited paper nums).
        paper_meta: ``{num_or_slug: text}`` or ``{num_or_slug: {"title"/"essence"}}``.
        client: LLM client (Anthropic/stub). ``None`` → annotate ``supported=True``.

    Returns:
        the list of insight dicts (same objects, annotated *in place*). On any
        per-insight error that insight defaults to ``supported=True`` (never
        dropped here — dropping is the caller's policy).
    """
    items = insights.get("cross_category", []) if isinstance(insights, dict) \
        else (insights or [])
    if not items:
        return items
    for ins in items:
        ins.setdefault("supported", True)
        ins.setdefault("verify_reason", "")
        if client is None:
            ins["verify_reason"] = "skipped (no client)"
            continue
        try:
            v = _verify_one_insight(client, ins, _cited_meta(ins, paper_meta))
            ins["supported"] = bool(v.get("supported", True))
            ins["verify_reason"] = str(v.get("reason", ""))[:200]
        except Exception as e:  # graceful: keep insight on any failure
            ins["supported"] = True
            ins["verify_reason"] = f"verify-error: {str(e)[:80]}"
    return items


# ─────────────────────────────────────────────────────────────────────────────
# Pipeline hooks (env-driven wrappers; never raise)
# ─────────────────────────────────────────────────────────────────────────────

def _insights_enabled():
    raw = (os.environ.get("VERIFY_INSIGHTS", "1") or "1").strip().lower()
    return raw not in ("0", "off", "false", "no")


def apply_insight_verification(insights, paper_meta, client, *, drop=True, log=print):
    """extract_insights hook for cross-category insights.

    Controlled by env ``VERIFY_INSIGHTS`` (default on; ``0``/``off``/``false`` to
    disable). Annotates each ``cross_category`` insight with ``supported: bool``.
    When ``drop`` is True (default) unsupported insights are removed from
    ``insights['cross_category']`` and stashed under ``insights['_verify_dropped']``
    for traceability. Returns the insights dict. Never raises.
    """
    try:
        if not _insights_enabled():
            log("  [verify] insights: disabled (VERIFY_INSIGHTS=0)")
            return insights
        items = insights.get("cross_category", []) if isinstance(insights, dict) \
            else insights
        if not items or client is None:
            log("  [verify] insights: skipped (no client / no insights)")
            return insights
        verify_insights(insights, paper_meta, client)
        unsupported = [i for i in items if not i.get("supported", True)]
        log(f"  [verify] insights: checked {len(items)}, "
            f"{len(unsupported)} unsupported")
        for i in unsupported:
            log(f"    [verify] unsupported insight '{i.get('title', '')}': "
                f"{i.get('verify_reason', '')[:80]}")
        if drop and unsupported and isinstance(insights, dict):
            insights["cross_category"] = [i for i in items
                                          if i.get("supported", True)]
            insights.setdefault("_verify_dropped", []).extend(unsupported)
            log(f"  [verify] insights: dropped {len(unsupported)} unsupported")
        return insights
    except Exception as e:
        log(f"  [verify] insights: skipped on error ({str(e)[:80]})")
        return insights
