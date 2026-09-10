#!/usr/bin/env python3
"""Plan or execute an explicitly selected, source-grounded text task."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys

from lib.text_providers import DEFAULT_MODELS, TextProviderError, generate_structured

CLAIMS_SCHEMA = {"type": "object", "properties": {"status": {"type": "string", "enum": ["completed", "insufficient-data"]},
    "claims": {"type": "array",
    "items": {"type": "object", "properties": {"text": {"type": "string", "minLength": 1}, "source_id": {"type": "string", "minLength": 1}, "quote": {"type": "string", "minLength": 1}}, "required": ["text", "source_id", "quote"], "additionalProperties": False}}}, "required": ["status", "claims"], "additionalProperties": False}
_REQUEST_FIELDS = {"schema_version", "feature", "provider", "sources", "question", "model", "credential_ref",
                   "max_input_chars", "max_output_tokens", "max_cost_usd", "per_million_rates"}
_SOURCE_FIELDS = {"id", "title", "text"}


def _error(message):
    return {"schema_version": 1, "status": "failed", "error": {"type": "validation_error", "message": message}}


def _validate(request):
    if not isinstance(request, dict) or type(request.get("schema_version")) is not int or request["schema_version"] != 1:
        return None, _error("schema_version must be 1")
    if set(request) - _REQUEST_FIELDS:
        return None, _error("unknown request field")
    feature, provider = request.get("feature"), request.get("provider")
    if not isinstance(feature, str) or not isinstance(provider, str) or feature not in {"summary", "chat", "comparison"} or provider not in DEFAULT_MODELS:
        return None, _error("unsupported feature or provider")
    if provider == "ollama" and feature == "comparison":
        return None, _error("Ollama supports summary and chat only")
    model = request.get("model", DEFAULT_MODELS[provider])
    if model != DEFAULT_MODELS[provider]: return None, _error("unsupported model for provider")
    reference = request.get("credential_ref")
    if reference is not None and (provider == "ollama" or reference != f"credential:{provider}"):
        return None, _error("invalid credential_ref")
    sources = request.get("sources")
    if not isinstance(sources, list) or not sources: return None, _error("sources are required")
    if feature == "comparison" and len(sources) < 2: return None, _error("comparison requires at least two sources")
    ids = set()
    normal = []
    for source in sources:
        if not isinstance(source, dict) or set(source) - _SOURCE_FIELDS or not all(isinstance(source.get(k), str) and source[k].strip() for k in ("id", "title", "text")) or source["id"] in ids:
            return None, _error("each source needs a unique id, title, and text")
        ids.add(source["id"]); normal.append({k: source[k] for k in ("id", "title", "text")})
    max_chars = request.get("max_input_chars", 30000)
    max_tokens = request.get("max_output_tokens", 1000)
    if isinstance(max_chars, bool) or isinstance(max_tokens, bool) or not isinstance(max_chars, int) or max_chars < 1 or max_chars > 1_000_000 or not isinstance(max_tokens, int) or max_tokens < 1 or max_tokens > 32_000:
        return None, _error("token and input limits must be positive integers")
    if "question" in request and not isinstance(request["question"], str):
        return None, _error("question must be a string")
    joined = "\n\n".join("[%s] %s\n%s" % (x["id"], x["title"], x["text"]) for x in normal)
    if len(joined) > max_chars: return None, _error("sources exceed max_input_chars")
    return {"feature": feature, "provider": provider, "model": model, "sources": normal, "question": request.get("question", ""), "max_output_tokens": max_tokens, "joined": joined, "credential_ref": reference}, None


def _estimate(request):
    cap = request.get("max_cost_usd")
    rates = request.get("per_million_rates")
    if request["provider"] == "ollama":
        if cap is not None and (isinstance(cap, bool) or not isinstance(cap, (int, float)) or not math.isfinite(cap) or cap < 0):
            return None, "max_cost_usd requires a finite nonnegative value"
        return 0.0, None
    if cap is None: return None, None
    if isinstance(cap, bool) or not isinstance(cap, (int, float)) or not math.isfinite(cap) or cap < 0 or not isinstance(rates, dict) or set(rates) != {"input", "output"}: return None, "max_cost_usd requires supplied per_million_rates"
    inp, out = rates.get("input"), rates.get("output")
    if not all(not isinstance(v, bool) and isinstance(v, (int, float)) and math.isfinite(v) and v >= 0 for v in (inp, out)): return None, "max_cost_usd requires input and output per-million rates"
    estimate = request["input_token_bound"] / 1_000_000 * inp + request["max_output_tokens"] / 1_000_000 * out
    return estimate, "estimated cost exceeds max_cost_usd" if estimate > cap else None


def _validate_claims(data, sources):
    if not isinstance(data, dict) or not isinstance(data.get("status"), str) or data["status"] not in {"completed", "insufficient-data"}:
        raise TextProviderError("provider returned invalid evidence status")
    if data.get("status") == "insufficient-data" and data.get("claims") == []:
        return []
    if data.get("status") == "insufficient-data":
        raise TextProviderError("insufficient-data response must not contain claims")
    claims = data.get("claims") if isinstance(data, dict) else None
    index = {source["id"]: source["text"] for source in sources}
    if not isinstance(claims, list) or not claims: raise TextProviderError("provider returned unsupported claims payload")
    for claim in claims:
        if not isinstance(claim, dict) or not all(isinstance(claim.get(k), str) and claim[k] for k in ("text", "source_id", "quote")):
            raise TextProviderError("provider returned unsupported claims payload")
        if claim["source_id"] not in index or claim["quote"] not in index[claim["source_id"]]:
            raise TextProviderError("provider returned unsupported citation")
    return claims


def run(request, execute=False):
    validated, err = _validate(request)
    if err:
        value = request.get("feature") if isinstance(request, dict) else None
        err["feature"] = value if isinstance(value, str) and value in {"summary", "chat", "comparison"} else "unknown"
        return err
    system = "Answer only from supplied sources. Return claims with exact supporting quotes and source IDs; state insufficient-data rather than inventing claims."
    prompt = "Feature: %s\nQuestion: %s\nSources:\n%s" % (validated["feature"], validated["question"], validated["joined"])
    input_bound = len((system + prompt + json.dumps(CLAIMS_SCHEMA, ensure_ascii=False)).encode("utf-8")) + 4096
    estimate, budget_error = _estimate({
        **validated, "input_token_bound": input_bound,
        "max_cost_usd": request.get("max_cost_usd"),
        "per_million_rates": request.get("per_million_rates"),
    })
    input_sha256 = hashlib.sha256((system + "\n" + prompt).encode()).hexdigest()
    if validated["provider"] == "ollama":
        credential = {"configured": True, "reference": None}
    else:
        from lib.credentials import credential_status
        status = credential_status(validated["provider"])
        credential = {"configured": bool(status["configured"]), "reference": status["reference"]}
    plan = {"schema_version": 1, "feature": validated["feature"], "status": "ready", "provider": validated["provider"], "model": validated["model"],
            "source_count": len(validated["sources"]), "data_destinations": [validated["provider"]],
            "cost_estimate_usd": estimate, "input_sha256": input_sha256,
            "input_token_upper_bound": input_bound,
            "credential": credential}
    if budget_error:
        plan["status"] = "budget-unavailable" if "requires" in budget_error else "budget-exceeded"
        plan["error"] = {"type": "budget_error", "message": budget_error}
        return plan
    if not credential["configured"]:
        plan["status"] = "needs-key"
        plan["error"] = {"type": "credential_missing", "message": "selected provider credential is unavailable"}
        return plan
    modules = ["jsonschema"]
    sdk = {"anthropic": "anthropic", "openai": "openai", "google": "google.genai"}.get(validated["provider"])
    if sdk:
        modules.append(sdk)
    missing = []
    for name in modules:
        try:
            if importlib.util.find_spec(name) is None:
                missing.append(name)
        except (ImportError, ValueError):
            missing.append(name)
    if missing:
        plan["status"] = "needs-runtime"
        plan["error"] = {"type": "runtime_missing", "message": "required runtime is missing: " + ", ".join(missing)}
        return plan
    if not execute: return plan
    try:
        result = generate_structured(validated["provider"], validated["model"], system, prompt, CLAIMS_SCHEMA,
            capability=validated["feature"], max_output_tokens=validated["max_output_tokens"],
            credential_ref=validated["credential_ref"])
        claims = _validate_claims(result["data"], validated["sources"])
    except TextProviderError as exc:
        return {**plan, "status": "failed", "error": {"type": type(exc).__name__, "message": str(exc)}}
    result["schema_version"] = 1
    result["feature"] = validated["feature"]
    result["status"] = "insufficient-data" if not claims else "completed"
    result["text"] = "\n".join("- %s [%s: %s]" % (x["text"], x["source_id"], x["quote"]) for x in claims)
    return result


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True, help="path to JSON request")
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args(argv)
    try:
        with open(args.request, encoding="utf-8") as request_file:
            raw = request_file.read(1_000_001)
        if len(raw) > 1_000_000: raise ValueError("request too large")
        request = json.loads(raw)
    except (OSError, ValueError, json.JSONDecodeError): print(json.dumps(_error("request file must contain JSON"))); return 2
    result = run(request, args.execute)
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result.get("status") in {"ready", "completed", "insufficient-data"} else 2

if __name__ == "__main__": raise SystemExit(main())
