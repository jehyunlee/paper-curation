"""Shared key-minimal local PDF review entrypoint for CLI and Paper Curio.

The default invocation is a read-only plan.  ``--execute`` performs only the
single-paper path declared in ``STEPS`` and publishes a complete bundle after
all staged artifacts validate.
"""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib.util
import io
import json
import math
import os
import re
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Any


SCHEMA_VERSION = 1
FEATURE = "review"
PROVIDER = "anthropic"
MODEL = "claude-sonnet-5"
REVIEW_TEXT_CHARACTER_LIMIT = 12_000
SIDECAR_SCHEMA = "bibliography-sidecar-1"

STEPS = [
    "validate-pdf",
    "extract-text",
    "validate-pdf-match",
    "extract-figures-geometric",
    "review-selected-provider",
    "render-canonical-html-keyless",
    "write-bibliography-sidecar",
    "publish-atomically",
]

_REQUIRED_ITEM_FIELDS = {
    "key",
    "title",
    "creators",
    "date",
    "DOI",
    "abstractNote",
    "url",
    "publicationTitle",
}
_ALLOWED_REQUEST_FIELDS = {
    "schema_version",
    "feature",
    "provider",
    "model",
    "credential_ref",
    "budget",
    "reservation_token",
    "pdf_path",
    "output_dir",
    "item",
    "overwrite",
}
_ALLOWED_CREATOR_FIELDS = {"firstName", "lastName", "creatorType", "name"}
_REQUIRED_OUTPUT_NAMES = ("text.md", "review.md", "index.html", "bibliography.json")
_OPTIONAL_OUTPUT_NAMES = ("_figs_inline.js",)
_FIGURE_NAME_RE = re.compile(r"^fig[0-9]+\.png$")
_REVIEW_SECTIONS = (
    "Essence",
    "Motivation",
    "Achievement",
    "How",
    "Originality",
    "Limitation & Further Study",
    "Evaluation",
)

# ``run_update_force`` uses script-style imports (``from config_loader ...``).
# Put its own directory on sys.path without importing it during a keyless plan.
_PIPELINE_DIR = Path(__file__).resolve().parent
if str(_PIPELINE_DIR) not in sys.path:
    sys.path.insert(0, str(_PIPELINE_DIR))


class LocalReviewError(Exception):
    """A contract-safe failure with one of the public response statuses."""

    def __init__(
        self,
        status: str,
        message: str,
        *,
        partial: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.status = status
        self.partial = partial


def _sanitize_text(value: Any, *, limit: int = 800) -> str:
    """Remove credential-shaped values before text reaches JSON or stderr."""
    text = str(value or "")
    secret_names = re.compile(
        r"(?:API_KEY|TOKEN|SECRET|PASSWORD|PRIVATE_KEY|ACCESS_KEY)$",
        re.IGNORECASE,
    )
    secret_values = {
        env_value
        for env_name, env_value in os.environ.items()
        if secret_names.search(env_name) and len(env_value) >= 4
    }
    for secret_value in sorted(secret_values, key=len, reverse=True):
        text = text.replace(secret_value, "[REDACTED]")
    substitutions = (
        (r"sk-ant-[A-Za-z0-9_-]{8,}", "[REDACTED]"),
        (r"AIza[A-Za-z0-9_-]{10,}", "[REDACTED]"),
        (r"sk-(?:proj-)?[A-Za-z0-9_-]{12,}", "[REDACTED]"),
        (r"(?i)(authorization\s*:\s*bearer\s+)[^\s]+", r"\1[REDACTED]"),
        (r"(?i)(api[_-]?key=)[^&\s]+", r"\1[REDACTED]"),
    )
    for pattern, replacement in substitutions:
        text = re.sub(pattern, replacement, text)
    text = "".join(ch for ch in text if ch in "\n\t" or ord(ch) >= 32)
    if len(text) > limit:
        text = text[:limit] + "…"
    return text


def _response(
    status: str,
    *,
    error: str | None = None,
    outputs: dict[str, str] | None = None,
    bibliography: str | None = "sidecar-only",
    figures: int | None = None,
    estimate: dict[str, Any] | None = None,
    partial: dict[str, Any] | None = None,
    provider: str = PROVIDER,
    model: str = MODEL,
) -> dict[str, Any]:
    result: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "feature": FEATURE,
        "status": status,
        "steps": list(STEPS),
        "required_keys": [_required_key(provider)],
        "provider": provider,
        "model": model,
        "transmission": [provider],
    }
    if outputs is not None:
        result["outputs"] = outputs
    if bibliography is not None:
        result["bibliography"] = bibliography
    if figures is not None:
        result["figures"] = int(figures)
    if estimate is not None:
        result["estimate"] = estimate
    if partial:
        result["partial"] = partial
    if error:
        result["error"] = _sanitize_text(error)
    return result


def _required_key(provider: str) -> str:
    return {"anthropic": "ANTHROPIC_API_KEY", "openai": "OPENAI_API_KEY",
            "google": "GOOGLE_API_KEY"}.get(provider, "UNKNOWN_API_KEY")


def _selection(provider: Any, model: Any) -> tuple[str, str]:
    from lib.text_providers import CLOUD_PROVIDERS, DEFAULT_MODELS
    if not isinstance(provider, str) or provider not in CLOUD_PROVIDERS:
        raise LocalReviewError("failed", "unsupported provider")
    if model is not None and not isinstance(model, str):
        raise LocalReviewError("failed", "model must be a string")
    selected = model or DEFAULT_MODELS[provider]
    if selected != DEFAULT_MODELS[provider]:
        raise LocalReviewError("failed", "unsupported model")
    return provider, selected


def _response_selection(payload: Any) -> tuple[str, str]:
    if not isinstance(payload, dict):
        return PROVIDER, MODEL
    try:
        return _selection(payload.get("provider", PROVIDER), payload.get("model"))
    except LocalReviewError:
        return PROVIDER, MODEL


def _budget(value: Any) -> dict[str, float | int] | None:
    if value is None:
        return None
    if not isinstance(value, dict) or set(value) - {
        "max_cost_usd", "input_per_million_usd", "output_per_million_usd",
        "max_output_tokens",
    }:
        raise LocalReviewError("failed", "invalid budget")
    result: dict[str, float | int] = {}
    for key, raw in value.items():
        if isinstance(raw, bool) or not isinstance(raw, (int, float)) or not math.isfinite(raw) or raw < 0:
            raise LocalReviewError("failed", f"budget.{key} must be a finite nonnegative number")
        if key == "max_output_tokens":
            if int(raw) != raw or raw < 1 or raw > 4000:
                raise LocalReviewError("failed", "budget.max_output_tokens must be an integer from 1 to 4000")
            result[key] = int(raw)
        else:
            result[key] = float(raw)
    if "max_cost_usd" in result and (
        "input_per_million_usd" not in result or "output_per_million_usd" not in result
    ):
        raise LocalReviewError(
            "budget-unavailable", "max_cost_usd requires input and output rates"
        )
    return result


def _validate_request(payload: Any) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise LocalReviewError("failed", "request must be a JSON object")

    unknown = sorted(set(payload) - _ALLOWED_REQUEST_FIELDS)
    if unknown:
        raise LocalReviewError(
            "failed", f"unsupported request field(s): {', '.join(unknown)}"
        )

    schema = payload.get("schema_version")
    if isinstance(schema, bool) or schema != SCHEMA_VERSION:
        raise LocalReviewError("failed", "unsupported schema_version")
    if payload.get("feature") != FEATURE:
        raise LocalReviewError("failed", "unsupported feature")
    provider, model = _selection(payload.get("provider", PROVIDER), payload.get("model"))
    credential_ref = payload.get("credential_ref")
    if credential_ref is not None and credential_ref != f"credential:{provider}":
        raise LocalReviewError("failed", "invalid credential_ref")
    budget = _budget(payload.get("budget"))
    reservation_token = payload.get("reservation_token")
    if reservation_token is not None and (
        not isinstance(reservation_token, str) or not reservation_token
        or len(reservation_token) > 512
    ):
        raise LocalReviewError("failed", "invalid reservation token")
    if not isinstance(payload.get("overwrite"), bool):
        raise LocalReviewError("failed", "overwrite must be a boolean")

    pdf_raw = payload.get("pdf_path")
    output_raw = payload.get("output_dir")
    if not isinstance(pdf_raw, str) or not Path(pdf_raw).is_absolute():
        raise LocalReviewError("failed", "pdf_path must be an absolute path")
    if not isinstance(output_raw, str) or not Path(output_raw).is_absolute():
        raise LocalReviewError("failed", "output_dir must be an absolute path")

    pdf_path = Path(pdf_raw).resolve(strict=False)
    output_dir = Path(output_raw).resolve(strict=False)
    if output_dir == Path(output_dir.anchor) or not output_dir.name:
        raise LocalReviewError("failed", "output_dir must name a slug directory")
    if output_dir.exists() and not output_dir.is_dir():
        raise LocalReviewError("failed", "output_dir exists and is not a directory")
    if output_dir == pdf_path:
        raise LocalReviewError("failed", "output_dir must differ from pdf_path")

    item = payload.get("item")
    if not isinstance(item, dict):
        raise LocalReviewError("failed", "item must be an object")
    missing = sorted(_REQUIRED_ITEM_FIELDS - set(item))
    if missing:
        raise LocalReviewError(
            "failed", f"item is missing field(s): {', '.join(missing)}"
        )
    unknown_item = sorted(set(item) - _REQUIRED_ITEM_FIELDS)
    if unknown_item:
        raise LocalReviewError(
            "failed", f"unsupported item field(s): {', '.join(unknown_item)}"
        )

    for field in _REQUIRED_ITEM_FIELDS - {"creators"}:
        if not isinstance(item.get(field), str):
            raise LocalReviewError("failed", f"item.{field} must be a string")
    if not item["key"].strip():
        raise LocalReviewError(
            "insufficient-data", "item.key is required for the bibliography sidecar"
        )
    if not item["title"].strip():
        raise LocalReviewError("insufficient-data", "item.title is empty")

    creators = item.get("creators")
    if not isinstance(creators, list):
        raise LocalReviewError("failed", "item.creators must be an array")
    normalized_creators: list[dict[str, str]] = []
    for index, creator in enumerate(creators):
        if not isinstance(creator, dict):
            raise LocalReviewError(
                "failed", f"item.creators[{index}] must be an object"
            )
        unknown_creator = sorted(set(creator) - _ALLOWED_CREATOR_FIELDS)
        if unknown_creator:
            raise LocalReviewError(
                "failed",
                f"item.creators[{index}] has unsupported field(s): "
                + ", ".join(unknown_creator),
            )
        normalized: dict[str, str] = {}
        for field, value in creator.items():
            if not isinstance(value, str):
                raise LocalReviewError(
                    "failed", f"item.creators[{index}].{field} must be a string"
                )
            normalized[field] = value
        if not any(
            normalized.get(field, "").strip()
            for field in ("firstName", "lastName", "name")
        ):
            raise LocalReviewError(
                "insufficient-data", f"item.creators[{index}] has no name"
            )
        normalized_creators.append(normalized)

    normalized_item = {field: item[field] for field in _REQUIRED_ITEM_FIELDS}
    normalized_item["creators"] = normalized_creators
    return {
        "schema_version": SCHEMA_VERSION,
        "feature": FEATURE,
        "provider": provider,
        "model": model,
        "credential_ref": credential_ref,
        "budget": budget,
        "reservation_token": reservation_token,
        "pdf_path": pdf_path,
        "output_dir": output_dir,
        "item": normalized_item,
        "overwrite": payload["overwrite"],
    }


def _pdf_preflight(pdf_path: Path) -> dict[str, Any]:
    if not pdf_path.exists() or not pdf_path.is_file():
        raise LocalReviewError("insufficient-data", "PDF file does not exist")
    try:
        size = pdf_path.stat().st_size
    except OSError as exc:
        raise LocalReviewError(
            "insufficient-data", f"PDF file cannot be inspected: {exc}"
        ) from exc
    if size <= 0:
        raise LocalReviewError("insufficient-data", "PDF file is empty")
    if pdf_path.suffix.lower() != ".pdf":
        raise LocalReviewError("insufficient-data", "pdf_path is not a PDF file")
    try:
        with pdf_path.open("rb") as stream:
            header = stream.read(1024)
    except OSError as exc:
        raise LocalReviewError(
            "insufficient-data", f"PDF file cannot be read: {exc}"
        ) from exc
    if b"%PDF-" not in header:
        raise LocalReviewError("insufficient-data", "PDF signature is invalid")
    return {"pdf_bytes": size}


def _missing_runtimes(provider: str) -> list[str]:
    missing = []
    if sys.version_info[:2] != (3, 12):
        missing.append("Python 3.12")
    try:
        locking_available = importlib.util.find_spec("fcntl") is not None
    except (ImportError, ValueError):
        locking_available = False
    if not locking_available:
        missing.append("POSIX file locking")
    provider_module = {"anthropic": ("anthropic", "anthropic"),
                       "openai": ("openai", "openai"),
                       "google": ("google.genai", "google-genai")}[provider]
    for module, label in (("fitz", "PyMuPDF"), ("jsonschema", "jsonschema"), provider_module):
        try:
            available = importlib.util.find_spec(module) is not None
        except (ImportError, ValueError):
            available = False
        if not available:
            missing.append(label)
    for path, label in (
        (_PIPELINE_DIR / "run_update_force.py", "paper-curation review engine"),
        (_PIPELINE_DIR / "review_to_html.py", "canonical HTML renderer"),
    ):
        if not path.is_file():
            missing.append(label)
    return missing


def _budget_bound(request: dict[str, Any], pdf_bytes: int) -> dict[str, Any] | None:
    """One-attempt upper bound known before PDF extraction or a paid call."""
    budget = request["budget"]
    if budget is None or "max_cost_usd" not in budget:
        return None
    item_bytes = len(json.dumps(
        request["item"], ensure_ascii=False, separators=(",", ":")
    ).encode("utf-8"))
    input_tokens = REVIEW_TEXT_CHARACTER_LIMIT * 4 + item_bytes + pdf_bytes + 16_384
    output_tokens = int(budget.get("max_output_tokens", 4000))
    cost = (input_tokens * float(budget["input_per_million_usd"])
            + output_tokens * float(budget["output_per_million_usd"])) / 1_000_000
    return {
        "estimated_input_tokens": input_tokens,
        "estimated_output_tokens": output_tokens,
        "estimated_cost_usd": cost,
        "max_cost_usd": budget["max_cost_usd"],
        "token_estimate_method": (
            "12,000 Unicode source characters at four UTF-8 bytes each, full "
            "serialized item, PDF-byte figure allowance, and 16,384-token prompt/schema allowance"
        ),
        "attempts": 1,
    }


def _plan_estimate(pdf_info: dict[str, Any], request: dict[str, Any]) -> dict[str, Any]:
    estimate = {
        "pdf_bytes": int(pdf_info["pdf_bytes"]),
        "review_text_character_limit": REVIEW_TEXT_CHARACTER_LIMIT,
        "source_chars": None,
        "estimated_input_tokens": None,
        "cost": "unknown",
        "cost_reason": "Provider rates are not embedded; text is extracted only during execution.",
    }
    bound = _budget_bound(request, int(pdf_info["pdf_bytes"]))
    if bound:
        estimate.update(bound)
        estimate["cost"] = "bounded"
        estimate.pop("cost_reason", None)
    return estimate


def _actual_estimate(text: str, abstract: str, pdf_bytes: int) -> dict[str, Any]:
    transmitted_source_chars = min(len(text), REVIEW_TEXT_CHARACTER_LIMIT) + len(abstract)
    return {
        "pdf_bytes": int(pdf_bytes),
        "source_chars": len(text),
        "review_text_character_limit": REVIEW_TEXT_CHARACTER_LIMIT,
        "estimated_input_tokens": math.ceil(transmitted_source_chars / 4),
        "token_estimate_method": "transmitted source characters divided by 4",
        "token_estimate_scope": (
            "source excerpt and abstract only; fixed instructions and figure labels excluded"
        ),
        "cost": "unknown",
        "cost_reason": "No provider rate table is embedded.",
    }


def _artifact_paths(output_dir: Path) -> dict[str, str]:
    return {
        "review": str((output_dir / "review.md").resolve(strict=False)),
        "html": str((output_dir / "index.html").resolve(strict=False)),
        "text": str((output_dir / "text.md").resolve(strict=False)),
        "sidecar": str((output_dir / "bibliography.json").resolve(strict=False)),
    }


def _has_managed_artifacts(output_dir: Path) -> bool:
    if not output_dir.is_dir():
        return False
    if any(os.path.lexists(output_dir / name) for name in _REQUIRED_OUTPUT_NAMES):
        return True
    if any(os.path.lexists(output_dir / name) for name in _OPTIONAL_OUTPUT_NAMES):
        return True
    figures = output_dir / "figures"
    if figures.is_dir():
        try:
            return any(_FIGURE_NAME_RE.fullmatch(path.name) for path in figures.iterdir())
        except OSError:
            return True
    return False


def _reject_symlinked_figures(output_dir: Path) -> None:
    figures = output_dir / "figures"
    if figures.is_symlink():
        raise LocalReviewError(
            "failed", "output_dir/figures must not be a symbolic link"
        )


def _valid_review(path: Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return False
    if len(text) < 200 or not re.search(r"(?m)^#\s+\S", text):
        return False
    return all(
        re.search(rf"(?m)^##\s+{re.escape(name)}\s*$", text)
        for name in _REVIEW_SECTIONS
    ) and bool(re.search(r"(?m)^\*\*총평\*\*:\s*\S", text))


def _valid_html(path: Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return False
    lowered = text.lower()
    return (
        len(text) >= 200
        and "<!doctype html>" in lowered
        and "<html" in lowered
        and "</html>" in lowered
        and "<title>" in lowered
    )


def _read_valid_sidecar(path: Path, request: dict[str, Any], text_path: Path) -> dict[str, Any] | None:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError):
        return None
    if not isinstance(payload, dict) or payload.get("schema") != SIDECAR_SCHEMA:
        return None
    zotero = payload.get("zotero")
    if not isinstance(zotero, dict):
        return None
    item = request["item"]
    if zotero.get("key") != item["key"] or zotero.get("title") != item["title"]:
        return None
    if item["publicationTitle"] and zotero.get("publicationTitle") != item["publicationTitle"]:
        return None
    creators = payload.get("creators", zotero.get("creators"))
    if creators != item["creators"]:
        return None
    review = payload.get("review")
    if not isinstance(review, dict):
        return None
    if review.get("provider") != request["provider"] or review.get("model") != request["model"]:
        return None
    recorded_hash = payload.get("text_md_sha256")
    if not isinstance(recorded_hash, str) or not recorded_hash:
        return None
    try:
        actual_hash = hashlib.sha256(text_path.read_bytes()).hexdigest()
    except OSError:
        return None
    if recorded_hash != actual_hash:
        return None
    return payload


def _figure_count(directory: Path) -> int:
    figures = directory / "figures"
    if not figures.is_dir():
        return 0
    try:
        return sum(
            1
            for path in figures.iterdir()
            if path.is_file()
            and _FIGURE_NAME_RE.fullmatch(path.name)
            and path.stat().st_size > 0
        )
    except OSError:
        return 0


def _existing_bundle_response(
    request: dict[str, Any], pdf_info: dict[str, Any]
) -> dict[str, Any] | None:
    output_dir = request["output_dir"]
    if not _has_managed_artifacts(output_dir):
        return None
    text_path = output_dir / "text.md"
    try:
        text = text_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        text = ""
    valid = (
        len(text) >= 100
        and _valid_review(output_dir / "review.md")
        and _valid_html(output_dir / "index.html")
        and _read_valid_sidecar(
            output_dir / "bibliography.json", request, text_path
        )
        is not None
    )
    if not valid:
        return _response(
            "failed",
            error=(
                "output_dir contains an incomplete or mismatched review bundle; "
                "set overwrite to true to replace managed artifacts"
            ),
            estimate=_plan_estimate(pdf_info, request),
            provider=request["provider"], model=request["model"],
        )
    return _response(
        "exists",
        outputs=_artifact_paths(output_dir),
        bibliography="sidecar-only",
        figures=_figure_count(output_dir),
        estimate=_actual_estimate(
            text, request["item"]["abstractNote"], pdf_info["pdf_bytes"]
        ),
        provider=request["provider"], model=request["model"],
    )


def _preflight(request: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any] | None]:
    pdf_info = _pdf_preflight(request["pdf_path"])
    _reject_symlinked_figures(request["output_dir"])
    if not request["overwrite"]:
        existing = _existing_bundle_response(request, pdf_info)
        if existing is not None:
            return pdf_info, existing

    try:
        from lib.credentials import resolve_credential
        resolve_credential(request["provider"], request["credential_ref"])
    except Exception:
        return pdf_info, _response(
            "needs-key",
            error=f"{_required_key(request['provider'])} or its OS keyring credential is required only when this review is executed",
            estimate=_plan_estimate(pdf_info, request),
            provider=request["provider"], model=request["model"],
        )

    missing = _missing_runtimes(request["provider"])
    if missing:
        return pdf_info, _response(
            "needs-runtime",
            error="missing runtime: " + ", ".join(missing),
            estimate=_plan_estimate(pdf_info, request),
            provider=request["provider"], model=request["model"],
        )
    return pdf_info, None


def _lock_path(output_dir: Path) -> Path:
    return output_dir.parent / f".{output_dir.name}.local-review.lock"


def _validate_reservation(request: dict[str, Any]) -> None:
    """Require Curio's ownership token only when this output is reserved."""
    from lib.corpus_store import CorpusStoreError, _owned_reservation, slug_is_reserved
    papers_dir = request["output_dir"].parent
    slug = request["output_dir"].name
    token = request["reservation_token"]
    reserved = slug_is_reserved(papers_dir, slug)
    if not reserved:
        if token is not None:
            raise LocalReviewError("failed", "reservation ownership mismatch")
        return
    try:
        _owned_reservation(Path(papers_dir).resolve(), slug, token or "")
    except CorpusStoreError as exc:
        raise LocalReviewError("failed", "reservation ownership mismatch") from exc


@contextlib.contextmanager
def _exclusive_output_lock(output_dir: Path):
    try:
        import fcntl
    except ImportError as exc:
        raise LocalReviewError(
            "needs-runtime", "filesystem locking is unavailable on this runtime"
        ) from exc

    output_dir.parent.mkdir(parents=True, exist_ok=True)
    path = _lock_path(output_dir)
    descriptor = os.open(path, os.O_CREAT | os.O_RDWR, 0o600)
    try:
        try:
            fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise LocalReviewError(
                "failed", "another local review is already writing this output_dir"
            ) from exc
        yield
    finally:
        try:
            fcntl.flock(descriptor, fcntl.LOCK_UN)
        finally:
            os.close(descriptor)


@contextlib.contextmanager
def _captured_engine_output():
    """Keep the machine-readable stdout channel clean and scrub engine logs."""
    buffer = io.StringIO()
    try:
        with contextlib.redirect_stdout(buffer), contextlib.redirect_stderr(buffer):
            yield
    finally:
        logged = buffer.getvalue()
        if logged:
            print("review engine diagnostics suppressed", file=sys.stderr)


def _load_engine():
    """Import reusable batch functions only after key/runtime preflight passes."""
    import run_update_force as review_engine
    import review_to_html as html_renderer

    return review_engine, html_renderer


def _validate_staged_sidecar(
    stage: Path, request: dict[str, Any], returned: Any
) -> None:
    if not isinstance(returned, dict):
        raise LocalReviewError("failed", "bibliography sidecar generation failed")
    if _read_valid_sidecar(
        stage / "bibliography.json", request, stage / "text.md"
    ) is None:
        raise LocalReviewError(
            "failed", "bibliography sidecar is missing required provenance"
        )


def _write_html_atomically(stage: Path, html: str) -> None:
    if not isinstance(html, str):
        raise LocalReviewError("failed", "canonical HTML renderer returned no document")
    lowered = html.lower()
    if (
        len(html) < 200
        or "<!doctype html>" not in lowered
        or "<html" not in lowered
        or "</html>" not in lowered
        or "<title>" not in lowered
    ):
        raise LocalReviewError("failed", "canonical HTML validation failed")
    target = stage / "index.html"
    temporary = stage / "index.html.tmp"
    temporary.write_text(html, encoding="utf-8")
    os.replace(temporary, target)


def _managed_publication_entries(stage: Path, output_dir: Path) -> list[tuple[Path | None, Path]]:
    entries: list[tuple[Path | None, Path]] = []
    for name in ("text.md", "review.md", "index.html"):
        entries.append((stage / name, output_dir / name))

    staged_figures = stage / "figures"
    output_figures = output_dir / "figures"
    staged_names = set()
    if staged_figures.is_dir():
        staged_names = {
            path.name
            for path in staged_figures.iterdir()
            if path.is_file() and _FIGURE_NAME_RE.fullmatch(path.name)
        }
    existing_names = set()
    if output_figures.is_dir():
        existing_names = {
            path.name
            for path in output_figures.iterdir()
            if _FIGURE_NAME_RE.fullmatch(path.name)
        }
    for name in sorted(staged_names | existing_names):
        source = staged_figures / name if name in staged_names else None
        entries.append((source, output_figures / name))

    payload = stage / "_figs_inline.js"
    entries.append((payload if payload.is_file() else None, output_dir / payload.name))
    # Sidecar is the final commit marker for a complete bundle.
    entries.append((stage / "bibliography.json", output_dir / "bibliography.json"))
    return entries


def _remove_path(path: Path) -> None:
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path)
    elif os.path.lexists(path):
        path.unlink()


def _publish_bundle(stage: Path, output_dir: Path) -> None:
    """Publish managed artifacts under the output lock, rolling back on error."""
    output_was_present = output_dir.exists()
    output_dir.mkdir(parents=True, exist_ok=True)
    backup = Path(
        tempfile.mkdtemp(
            prefix=f".{output_dir.name}.local-review-backup-",
            dir=str(output_dir.parent),
        )
    )
    entries = _managed_publication_entries(stage, output_dir)
    backed_up: list[tuple[Path, Path]] = []
    installed: list[Path] = []
    publication_succeeded = False
    rollback_succeeded = True
    try:
        for _source, target in entries:
            if not os.path.lexists(target):
                continue
            relative = target.relative_to(output_dir)
            saved = backup / relative
            saved.parent.mkdir(parents=True, exist_ok=True)
            os.replace(target, saved)
            backed_up.append((saved, target))

        for source, target in entries:
            if source is None or not os.path.lexists(source):
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            os.replace(source, target)
            installed.append(target)
        publication_succeeded = True
    except Exception:
        for target in reversed(installed):
            try:
                _remove_path(target)
            except OSError:
                rollback_succeeded = False
        for saved, target in reversed(backed_up):
            try:
                target.parent.mkdir(parents=True, exist_ok=True)
                os.replace(saved, target)
            except OSError:
                rollback_succeeded = False
        if not output_was_present:
            try:
                (output_dir / "figures").rmdir()
            except OSError:
                pass
            try:
                output_dir.rmdir()
            except OSError:
                pass
        raise
    finally:
        # Never delete the only rollback copy after a failed restoration.
        if publication_succeeded or rollback_succeeded:
            shutil.rmtree(backup, ignore_errors=True)


def _cache_dir(output_dir: Path) -> Path:
    return output_dir.parent / f".{output_dir.name}.local-review-cache"


def _verified_cache_path(
    cache_dir: Path, cache_evidence: dict[str, Any], request: dict[str, Any]
) -> Path | None:
    if not cache_evidence.get("verified"):
        return None
    if (cache_evidence.get("provider"), cache_evidence.get("model")) != (
        request["provider"], request["model"]
    ):
        return None
    try:
        path = Path(str(cache_evidence["path"])).resolve(strict=True)
        expected_parent = cache_dir.resolve(strict=True)
    except (KeyError, OSError, RuntimeError):
        return None
    if path.parent != expected_parent or path.suffix != ".json" or not path.is_file():
        return None
    return path


def _partial_dir(output_dir: Path) -> Path:
    return output_dir.parent / f".{output_dir.name}.local-review-partial"


def _preserve_partial(
    work_root: Path,
    stage: Path,
    output_dir: Path,
    cache_dir: Path,
    cache_evidence: dict[str, Any],
    request: dict[str, Any],
) -> dict[str, Any] | None:
    review_ready = _valid_review(stage / "review.md")
    verified_cache = _verified_cache_path(cache_dir, cache_evidence, request)
    cache_ready = verified_cache is not None
    if not review_ready and not cache_ready:
        return None

    destination = _partial_dir(output_dir)
    try:
        if os.path.lexists(destination):
            _remove_path(destination)
        os.replace(work_root, destination)
        preserved_stage = destination / output_dir.name
    except OSError:
        if not cache_ready:
            return None
        return {
            "published": False,
            "review_ready": False,
            "cache_preserved": True,
            "retry_safe": True,
            "cache": str(verified_cache),
        }
    partial: dict[str, Any] = {
        "published": False,
        "review_ready": review_ready,
        "cache_preserved": cache_ready,
        "retry_safe": cache_ready,
    }
    if review_ready:
        partial["review"] = str(preserved_stage / "review.md")
    if cache_ready:
        partial["cache"] = str(verified_cache)
    return partial


def _execute(request: dict[str, Any], pdf_info: dict[str, Any]) -> dict[str, Any]:
    output_dir = request["output_dir"]
    with _exclusive_output_lock(output_dir):
        _validate_reservation(request)
        _reject_symlinked_figures(output_dir)
        # A plan may race another writer. Re-evaluate the bundle while holding
        # the same lock used for publication.
        if not request["overwrite"]:
            existing = _existing_bundle_response(request, pdf_info)
            if existing is not None:
                return existing

        work_root = Path(
            tempfile.mkdtemp(
                prefix=f".{output_dir.name}.local-review-stage-",
                dir=str(output_dir.parent),
            )
        )
        # The renderer derives its public slug from basename(slug_dir). Keep the
        # requested slug as the inner directory so no random staging prefix can
        # leak into canonical URLs, figure links, or page metadata.
        stage = work_root / output_dir.name
        stage.mkdir()
        cache_dir = _cache_dir(output_dir)
        cache_evidence: dict[str, Any] = {}
        keep_work_root = False
        try:
            with _captured_engine_output():
                engine, renderer = _load_engine()

                extracted = engine.extract_text(
                    str(request["pdf_path"]), str(stage)
                )
                text_path = stage / "text.md"
                if not extracted or not text_path.is_file() or text_path.stat().st_size < 100:
                    raise LocalReviewError(
                        "insufficient-data", "PDF text extraction produced insufficient text"
                    )
                try:
                    text = text_path.read_text(encoding="utf-8")
                except (OSError, UnicodeError) as exc:
                    raise LocalReviewError(
                        "insufficient-data", f"extracted text cannot be read: {exc}"
                    ) from exc

                sane, reason = engine._zotero_text_sanity(
                    request["item"], str(text_path)
                )
                if not sane:
                    raise LocalReviewError(
                        "insufficient-data",
                        "PDF metadata does not match the selected item: " + str(reason),
                    )

                figures = engine.extract_figures(
                    str(request["pdf_path"]),
                    str(stage),
                    validate_with_gemini=False,
                )
                if not isinstance(figures, list):
                    raise LocalReviewError("failed", "geometric figure extraction failed")

                budget_estimate = _budget_bound(request, int(pdf_info["pdf_bytes"]))
                if budget_estimate and budget_estimate["estimated_cost_usd"] > budget_estimate["max_cost_usd"]:
                    raise LocalReviewError(
                        "budget-exceeded", "conservative estimate exceeds max_cost_usd"
                    )
                wrote_review = engine.write_review(
                    request["item"],
                    str(stage),
                    figures,
                    provider=request["provider"],
                    model=request["model"],
                    credential_ref=request["credential_ref"],
                    max_output_tokens=int(
                        (request["budget"] or {}).get("max_output_tokens", 4000)
                    ),
                    cache_dir=cache_dir,
                    cache_evidence=cache_evidence,
                )
                if not wrote_review or not _valid_review(stage / "review.md"):
                    raise LocalReviewError("failed", "review generation failed")

                html = renderer.convert_review(
                    str(stage / "review.md"),
                    "ai4s",
                    str(stage),
                    keyless=True,
                )
                _write_html_atomically(stage, html)

                sidecar = engine.write_bibliography_sidecar(
                    request["item"],
                    str(stage),
                    str(request["pdf_path"]),
                    include_affiliations=False,
                    review_provider=request["provider"],
                    review_model=request["model"],
                )
                _validate_staged_sidecar(stage, request, sidecar)

            _publish_bundle(stage, output_dir)
            prior_partial = _partial_dir(output_dir)
            if os.path.lexists(prior_partial):
                _remove_path(prior_partial)
            estimate = _actual_estimate(
                text, request["item"]["abstractNote"], pdf_info["pdf_bytes"]
            )
            bound = _budget_bound(request, int(pdf_info["pdf_bytes"]))
            if bound:
                estimate.update(bound)
                estimate["cost"] = "bounded"
                estimate.pop("cost_reason", None)
            return _response(
                "completed",
                outputs=_artifact_paths(output_dir),
                bibliography="sidecar-only",
                figures=_figure_count(output_dir),
                estimate=estimate,
                provider=request["provider"],
                model=request["model"],
            )
        except LocalReviewError as exc:
            partial = exc.partial or _preserve_partial(
                work_root, stage, output_dir, cache_dir, cache_evidence, request
            )
            keep_work_root = bool(partial and not work_root.exists())
            raise LocalReviewError(
                exc.status, str(exc), partial=partial
            ) from exc
        except ImportError as exc:
            partial = _preserve_partial(
                work_root, stage, output_dir, cache_dir, cache_evidence, request
            )
            keep_work_root = bool(partial and not work_root.exists())
            raise LocalReviewError(
                "needs-runtime",
                f"review runtime import failed: {type(exc).__name__}",
                partial=partial,
            ) from exc
        except Exception as exc:
            partial = _preserve_partial(
                work_root, stage, output_dir, cache_dir, cache_evidence, request
            )
            keep_work_root = bool(partial and not work_root.exists())
            raise LocalReviewError(
                "failed",
                f"local review failed: {type(exc).__name__}",
                partial=partial,
            ) from exc
        finally:
            # ``_preserve_partial`` atomically moved work_root when successful;
            # otherwise remove only our staging tree. Published/unrelated files
            # are outside it and remain untouched.
            if work_root.exists() and not keep_work_root:
                shutil.rmtree(work_root, ignore_errors=True)


def run_request(payload: Any, *, execute: bool = False) -> dict[str, Any]:
    """Validate and plan/execute one request without ever printing to stdout."""
    request: dict[str, Any] | None = None
    try:
        request = _validate_request(payload)
        pdf_info = _pdf_preflight(request["pdf_path"])
        bound = _budget_bound(request, int(pdf_info["pdf_bytes"]))
        if bound and bound["estimated_cost_usd"] > bound["max_cost_usd"]:
            return _response(
                "budget-exceeded",
                error="budget-exceeded: conservative estimate exceeds max_cost_usd",
                estimate=_plan_estimate(pdf_info, request),
                provider=request["provider"], model=request["model"],
            )
        pdf_info, preflight_response = _preflight(request)
        if preflight_response is not None:
            return preflight_response
        if not execute:
            return _response(
                "ready", estimate=_plan_estimate(pdf_info, request),
                provider=request["provider"], model=request["model"],
            )
        from lib.corpus_store import corpus_operation_lock
        with corpus_operation_lock(request["output_dir"].parent):
            return _execute(request, pdf_info)
    except LocalReviewError as exc:
        provider, model = (
            (request["provider"], request["model"])
            if request else _response_selection(payload)
        )
        return _response(
            exc.status,
            error=str(exc),
            partial=exc.partial,
            provider=provider,
            model=model,
        )
    except Exception as exc:
        return _response(
            "failed", error=f"request failed: {type(exc).__name__}",
            provider=request["provider"] if request else _response_selection(payload)[0],
            model=request["model"] if request else _response_selection(payload)[1],
        )


def _read_request_file(path_value: str | None) -> Any:
    if not path_value:
        raise LocalReviewError("failed", "--request is required")
    path = Path(path_value)
    if not path.is_file():
        raise LocalReviewError("failed", "request file does not exist")
    try:
        if path.stat().st_size > 1_048_576:
            raise LocalReviewError("failed", "request file is too large")
        return json.loads(path.read_text(encoding="utf-8"))
    except LocalReviewError:
        raise
    except (OSError, UnicodeError, ValueError) as exc:
        raise LocalReviewError(
            "failed", f"request file is not valid JSON: {type(exc).__name__}"
        ) from exc


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Plan or execute one local Anthropic PDF review."
    )
    parser.add_argument("--request")
    parser.add_argument("--execute", action="store_true")
    args, unknown = parser.parse_known_args(argv)
    try:
        if unknown:
            raise LocalReviewError(
                "failed", "unsupported command argument(s): " + ", ".join(unknown)
            )
        payload = _read_request_file(args.request)
        result = run_request(payload, execute=args.execute)
    except LocalReviewError as exc:
        result = _response(exc.status, error=str(exc), partial=exc.partial)
    except Exception as exc:
        result = _response(
            "failed", error=f"request failed: {type(exc).__name__}: {exc}"
        )
    sys.stdout.write(json.dumps(result, ensure_ascii=False, separators=(",", ":")) + "\n")
    return 0 if result["status"] in {"ready", "completed", "exists"} else 2


if __name__ == "__main__":
    raise SystemExit(main())
