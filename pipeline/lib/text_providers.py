"""Explicit structured-text provider adapters.

This module deliberately has no provider fallback: callers must select a
provider and retry explicitly after an error.
"""
from __future__ import annotations

import hashlib
import json
import os
from copy import deepcopy
from urllib.parse import urlparse
from urllib.request import Request, urlopen

DEFAULT_MODELS = {
    "anthropic": "claude-sonnet-5",
    "openai": "gpt-5",
    "google": "gemini-3.1-pro-preview",
    "ollama": "qwen3.8:27b-mlx",
}
CLOUD_PROVIDERS = frozenset(("anthropic", "openai", "google"))


class TextProviderError(RuntimeError):
    """Safe adapter error; messages must not contain credentials."""


class ProviderSelectionError(TextProviderError): pass
class AuthenticationError(TextProviderError): pass
class ProviderResponseError(TextProviderError): pass
class ProviderTruncatedError(ProviderResponseError): pass
class UnsupportedCapabilityError(TextProviderError): pass


def _safe_error(exc: Exception) -> TextProviderError:
    name = type(exc).__name__.lower()
    if "auth" in name or "permission" in name or "apierror" in name and "401" in str(exc):
        return AuthenticationError("provider authentication failed")
    return ProviderResponseError("provider request failed")


def _validate_selection(provider: str, model: str | None, capability: str) -> str:
    if not isinstance(capability, str) or capability not in {"summary", "chat", "comparison", "review"}:
        raise UnsupportedCapabilityError("unsupported text capability")
    if not isinstance(provider, str) or provider not in DEFAULT_MODELS:
        raise ProviderSelectionError("unsupported text provider")
    chosen = model or DEFAULT_MODELS[provider]
    if chosen != DEFAULT_MODELS[provider]:
        raise ProviderSelectionError("unsupported model for provider")
    if capability == "review" and provider not in CLOUD_PROVIDERS:
        raise UnsupportedCapabilityError("review requires a cloud provider")
    if provider == "ollama" and capability not in {"summary", "chat"}:
        raise UnsupportedCapabilityError("unsupported Ollama capability")
    return chosen


def _credential(provider: str, credential_ref: str | None) -> str:
    if provider == "ollama":
        return ""
    from lib.credentials import CredentialsError, resolve_credential
    try:
        return resolve_credential(provider, credential_ref)
    except CredentialsError as exc:
        raise AuthenticationError("selected provider credential is unavailable") from exc


def _usage(value) -> dict:
    value = value or {}
    get = value.get if isinstance(value, dict) else lambda key, default=0: getattr(value, key, default)
    output = get("output_tokens", get("completion_tokens", None))
    if output is None:
        # Gemini reports thinking separately; OpenAI completion_tokens already
        # includes its reasoning tokens, so never add them twice.
        output = int(get("candidates_token_count", 0) or 0) + int(get("thoughts_token_count", 0) or 0)
    return {"input_tokens": int(get("input_tokens", get("prompt_tokens", get("prompt_token_count", 0))) or 0),
            "output_tokens": int(output or 0)}


def _parse_json(value) -> dict:
    if isinstance(value, dict):
        return value
    if not isinstance(value, str):
        raise ProviderResponseError("provider returned no structured payload")
    try:
        parsed = json.loads(value)
    except (TypeError, ValueError) as exc:
        raise ProviderResponseError("provider returned malformed structured payload") from exc
    if not isinstance(parsed, dict):
        raise ProviderResponseError("provider returned malformed structured payload")
    return parsed


def _strict_schema(schema: dict) -> dict:
    """Copy a schema and make every object closed for strict OpenAI output."""
    result = deepcopy(schema)
    def close(value):
        if isinstance(value, dict):
            if value.get("type") == "object":
                value["additionalProperties"] = False
            for child in value.values():
                close(child)
        elif isinstance(value, list):
            for child in value:
                close(child)
    close(result)
    return result


def _validate_schema_shape(data: dict, schema: dict) -> None:
    try:
        import jsonschema
        jsonschema.validate(data, schema)
    except ImportError as exc:
        raise ProviderResponseError("JSON schema validation is unavailable") from exc
    except Exception as exc:
        raise ProviderResponseError("provider returned invalid structured payload") from exc


def _ollama_url() -> str:
    url = os.environ.get("OLLAMA_URL", "http://127.0.0.1:11434")
    host = urlparse(url).hostname
    if host not in {"127.0.0.1", "::1", "localhost"}:
        raise ProviderSelectionError("Ollama endpoint must be loopback")
    return url.rstrip("/")


def _call_ollama(model, system, prompt, schema, max_output_tokens):
    # MLX runners may not enforce Ollama's format field as a decoding grammar.
    # State the same contract in the prompt and still validate the raw result.
    instruction = system + "\nReturn ONLY a JSON object, without Markdown or commentary, matching this JSON Schema:\n" + json.dumps(schema, ensure_ascii=False)
    body = json.dumps({"model": model, "system": instruction, "prompt": prompt,
                       "format": schema, "stream": False, "think": False,
                       "options": {"num_predict": max_output_tokens}}).encode()
    request = Request(_ollama_url() + "/api/generate", data=body,
                      headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urlopen(request, timeout=120) as response:
            result = json.loads(response.read().decode("utf-8"))
    except Exception as exc:
        raise _safe_error(exc) from exc
    if result.get("done") is not True or result.get("done_reason") == "length":
        raise ProviderTruncatedError("provider response was truncated")
    return _parse_json(result.get("response")), {"input_tokens": result.get("prompt_eval_count", 0), "output_tokens": result.get("eval_count", 0)}


def generate_structured(provider, model, system, prompt, schema, *, capability, max_output_tokens, credential_ref=None) -> dict:
    """Call exactly the selected provider and return validated JSON metadata."""
    chosen = _validate_selection(provider, model, capability)
    if not isinstance(schema, dict) or not isinstance(max_output_tokens, int) or max_output_tokens < 1:
        raise ProviderSelectionError("invalid structured generation request")
    # Review callers may pass the existing Anthropic tool declaration directly.
    # Normalize it without mutating that canonical module-level constant.
    validation_schema = schema.get("input_schema", schema) if capability == "review" else schema
    if not isinstance(validation_schema, dict):
        raise ProviderSelectionError("invalid structured generation request")
    key = _credential(provider, credential_ref)
    provider_schema = _strict_schema(validation_schema)
    tool_name = "emit_review" if capability == "review" else "emit_json"
    tool = {"name": tool_name, "input_schema": provider_schema}
    if capability == "review":
        from run_update_force import REVIEW_TOOL_SCHEMA
        tool["description"] = REVIEW_TOOL_SCHEMA["description"]
    try:
        if provider == "ollama":
            data, usage = _call_ollama(chosen, system, prompt, schema, max_output_tokens)
        elif provider == "anthropic":
            from anthropic import Anthropic
            response = Anthropic(api_key=key, max_retries=0).messages.create(model=chosen, max_tokens=max_output_tokens,
                system=system, messages=[{"role": "user", "content": prompt}],
                tools=[tool], tool_choice={"type": "tool", "name": tool_name})
            if getattr(response, "stop_reason", None) == "max_tokens": raise ProviderTruncatedError("provider response was truncated")
            blocks = getattr(response, "content", [])
            block = next((b for b in blocks if getattr(b, "type", "") == "tool_use" and getattr(b, "name", "") == tool_name), None)
            if block is None: raise ProviderResponseError("provider did not return required tool payload")
            data, usage = _parse_json(getattr(block, "input", None)), _usage(getattr(response, "usage", None))
        elif provider == "openai":
            from openai import OpenAI
            response = OpenAI(api_key=key, max_retries=0).chat.completions.create(model=chosen, max_completion_tokens=max_output_tokens,
                messages=[{"role": "system", "content": system}, {"role": "user", "content": prompt}],
                response_format={"type": "json_schema", "json_schema": {"name": "response", "strict": True, "schema": provider_schema}})
            choice = response.choices[0] if getattr(response, "choices", None) else None
            if choice is None or getattr(choice, "finish_reason", None) == "length": raise ProviderTruncatedError("provider response was truncated")
            data, usage = _parse_json(getattr(getattr(choice, "message", None), "content", None)), _usage(getattr(response, "usage", None))
        else:
            from google import genai
            from google.genai import types
            client = genai.Client(api_key=key, http_options=types.HttpOptions(
                retryOptions=types.HttpRetryOptions(attempts=1)))
            response = client.models.generate_content(model=chosen, contents=prompt,
                config=types.GenerateContentConfig(system_instruction=system, response_mime_type="application/json", response_json_schema=provider_schema, max_output_tokens=max_output_tokens))
            candidates = getattr(response, "candidates", []) or []
            finish_reason = getattr(response, "finish_reason", None)
            if candidates:
                finish_reason = getattr(candidates[0], "finish_reason", finish_reason)
            if str(finish_reason).upper().endswith(("MAX_TOKENS", "LENGTH")): raise ProviderTruncatedError("provider response was truncated")
            data, usage = _parse_json(getattr(response, "text", None)), _usage(getattr(response, "usage_metadata", None))
    except TextProviderError:
        raise
    except Exception as exc:
        raise _safe_error(exc) from exc
    if not data:
        raise ProviderResponseError("provider returned empty structured payload")
    if capability == "review":
        data = validate_review_payload(data)
    _validate_schema_shape(data, validation_schema)
    return {"data": data, "provider": provider, "model": chosen, "usage": usage,
            "provenance": {"schema": "text-provider-v1", "schema_sha256": hashlib.sha256(json.dumps(validation_schema, sort_keys=True, separators=(",", ":")).encode()).hexdigest(), "input_sha256": hashlib.sha256((system + "\n" + prompt).encode()).hexdigest()}}


def validate_review_payload(data) -> dict:
    """Apply the existing review completeness contract lazily."""
    from run_update_force import _review_response_is_complete, _salvage_review_data
    fixed = _salvage_review_data(data)
    if not _review_response_is_complete(fixed):
        raise ProviderResponseError("review payload is incomplete")
    return fixed
