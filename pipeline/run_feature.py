#!/usr/bin/env python3
"""Shared capability registry, read-only plans and explicitly selected execution."""
from __future__ import annotations

import argparse
import base64
import contextlib
import importlib.util
import io
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
REGISTRY_PATH = Path(__file__).with_name("features.json")
TEXT_FEATURES = {"summary", "chat", "comparison"}
SUCCESS = {"ready", "completed", "exists"}
ENV_NAMES = {"anthropic": "ANTHROPIC_API_KEY", "openai": "OPENAI_API_KEY",
             "google": "GOOGLE_API_KEY", "resend": "RESEND_API_KEY",
             "zotero": "ZOTERO_API_KEY", "cloudflare": "CLOUDFLARE_API_TOKEN",
             "cloudflare-account": "CLOUDFLARE_ACCOUNT_ID", "scopus": "SCOPUS_API_KEY"}


class FeatureBlocked(Exception):
    def __init__(self, status: str, message: str):
        self.status = status
        super().__init__(message)


def _registry() -> list[dict[str, Any]]:
    payload = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    features = payload["features"]
    if payload.get("schema_version") != 1 or not isinstance(features, list):
        raise ValueError("invalid capability registry")
    if len({f["id"] for f in features}) != len(features):
        raise ValueError("duplicate capability ID")
    return features


def _result(feature: str, status: str, **extra: Any) -> dict[str, Any]:
    return {"schema_version": 1, "feature": feature, "status": status, **extra}


def _component(value: Any) -> bool:
    return (isinstance(value, str) and 0 < len(value) <= 255
            and value not in {".", ".."} and not any(x in value for x in ("/", "\\", "\0")))


def _inside(root: Path, value: str) -> Path:
    if not _component(value):
        raise FeatureBlocked("failed", "invalid corpus path component")
    path = (root / value).resolve()
    if not path.is_relative_to(root.resolve()):
        raise FeatureBlocked("failed", "corpus path escapes its root")
    return path


def _validate(feature: dict, request: Any) -> dict:
    if (not isinstance(request, dict) or type(request.get("schema_version")) is not int
            or request["schema_version"] != 1
            or set(request) - {"schema_version", "feature", "params", "provider", "credential_ref", "budget"}):
        raise FeatureBlocked("failed", "invalid request schema or unknown field")
    import jsonschema
    params = request.get("params")
    try:
        jsonschema.validate(params, feature["params_schema"])
    except jsonschema.ValidationError as exc:
        raise FeatureBlocked("failed", "parameters do not match the capability schema") from exc
    params = dict(params)
    for name, spec in feature["params_schema"]["properties"].items():
        if name not in params and "default" in spec:
            params[name] = spec["default"]
    if "topic" in params:
        _inside(ROOT / "docs", params["topic"])
    if "slug" in params:
        _inside(ROOT / "docs/papers", params["slug"])
    provider = request.get("provider")
    if provider is not None and provider not in feature["supported_providers"]:
        raise FeatureBlocked("failed", "provider is not supported for this capability")
    selected = provider or next(iter(feature["supported_providers"]), None)
    reference = request.get("credential_ref")
    if reference is not None and (selected is None or selected == "ollama" or reference != f"credential:{selected}"):
        raise FeatureBlocked("failed", "invalid credential reference")
    budget = request.get("budget")
    if budget is not None:
        fields = {"max_cost_usd", "input_per_million_usd", "output_per_million_usd", "max_output_tokens"}
        if (not isinstance(budget, dict) or set(budget) - fields
                or any(isinstance(v, bool) or not isinstance(v, (int, float))
                       or not math.isfinite(v) or v < 0 for v in budget.values())):
            raise FeatureBlocked("failed", "invalid budget")
        if "max_output_tokens" in budget and (type(budget["max_output_tokens"]) is not int or not 1 <= budget["max_output_tokens"] <= 32000):
            raise FeatureBlocked("failed", "invalid output token limit")
        if "max_cost_usd" in budget and feature["id"] not in TEXT_FEATURES | {"review"}:
            if feature["credential"]["cost_class"] != "local" and not (
                feature["id"] == "bibliography-update" and params.get("offline", True)
            ):
                raise FeatureBlocked("budget-unavailable", "this capability has no verified monetary estimator")
    return params


def _text_request(request: dict, params: dict) -> dict:
    data = {"schema_version": 1, "feature": request["feature"],
            "provider": request.get("provider", "anthropic"), **params}
    if "credential_ref" in request:
        data["credential_ref"] = request["credential_ref"]
    budget = request.get("budget") or {}
    if "max_output_tokens" in budget:
        data["max_output_tokens"] = budget["max_output_tokens"]
    if "max_cost_usd" in budget:
        data["max_cost_usd"] = budget["max_cost_usd"]
        if {"input_per_million_usd", "output_per_million_usd"} <= budget.keys():
            data["per_million_rates"] = {"input": budget["input_per_million_usd"], "output": budget["output_per_million_usd"]}
    return data


def _review_request(request: dict, params: dict) -> dict:
    data = dict(params["request"])
    for name in ("provider", "credential_ref", "budget"):
        if name in request:
            if name in data and data[name] != request[name]:
                raise FeatureBlocked("failed", f"conflicting nested {name}")
            data[name] = request[name]
    return data


def _credential(provider: str, reference: str | None = None) -> str:
    from lib.credentials import CredentialsError, resolve_credential
    try:
        return resolve_credential(provider, reference)
    except CredentialsError as exc:
        raise FeatureBlocked("needs-key", f"selected {provider} credential is unavailable") from exc


def _topic_papers(topic: str) -> list[dict]:
    path = ROOT / "docs/papers/_papers_index.json"
    if not path.is_file():
        raise FeatureBlocked("insufficient-data", "paper index is missing")
    entries = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(entries, list):
        raise FeatureBlocked("failed", "paper index must be an array")
    result = [p for p in entries if isinstance(p, dict) and (
        topic in p.get("topics", []) or p.get("primary_topic") == topic or topic in (p.get("classifications") or {}))]
    if not result:
        raise FeatureBlocked("insufficient-data", "no papers belong to the selected topic")
    for paper in result:
        _inside(ROOT / "docs/papers", paper.get("slug"))
    return result


def _require_file(path: Path, label: str) -> None:
    if not path.is_file():
        raise FeatureBlocked("insufficient-data", f"{label} is missing")


def _preflight(feature: dict, request: dict, params: dict) -> dict:
    if sys.version_info[:2] != (3, 12):
        raise FeatureBlocked("needs-runtime", "Python 3.12 is required")
    feature_id = feature["id"]
    provider = request.get("provider") or next(iter(feature["supported_providers"]), None)
    plan = _result(feature_id, "ready", provider=provider, steps=[feature["module"]],
                   outputs=[], transmission=feature["credential"]["transmission"],
                   cost={"status": "none" if feature["credential"]["cost_class"] == "local" else "unknown"},
                   authorization="not-verified")
    if feature_id in {"keyword-search", "semantic-search"}:
        if params["operation"] == "build":
            _topic_papers(params["topic"])
            if params["include_text"] == "yes":
                from build_search_index import is_local_topic
                if not is_local_topic(params["topic"]):
                    raise FeatureBlocked("failed", "source text cannot be indexed for public topics")
        else:
            if not params.get("query", "").strip():
                raise FeatureBlocked("failed", "query is required for retrieval")
            from query_search_index import _load_index, _load_embedding_bytes
            index, directory = _load_index(params["topic"], ROOT / "docs")
            if feature_id == "semantic-search":
                if index.get("retrieval_mode") == "bm25":
                    raise FeatureBlocked("insufficient-data", "semantic retrieval requires an explicit hybrid index rebuild")
                _load_embedding_bytes(index, directory)
        plan["steps"] = [f"{params['operation']}:{'bm25' if feature_id == 'keyword-search' else 'hybrid'}"]
    elif feature_id == "extract":
        pdf, output = Path(params["pdf_path"]), Path(params["output_dir"])
        if not pdf.is_absolute() or not output.is_absolute():
            raise FeatureBlocked("failed", "PDF and output paths must be absolute")
        from local_review import _pdf_preflight
        _pdf_preflight(pdf)
        if output.is_symlink() or (output.exists() and (not output.is_dir() or any(output.iterdir()))):
            raise FeatureBlocked("failed", "extraction requires an empty output directory")
        if importlib.util.find_spec("fitz") is None:
            raise FeatureBlocked("needs-runtime", "PyMuPDF is required")
        plan["outputs"] = [str(output / "text.md"), str(output / "figures")]
    elif feature_id in {"metrics", "bibliography-update", "timeline-text", "timeline-image"}:
        papers = _topic_papers(params["topic"])
        plan["paper_count"] = len(papers)
        if feature_id == "bibliography-update" and params["offline"]:
            plan["transmission"] = "none; local sidecars and PDF evidence only"
            plan["cost"] = {"status": "none"}
        if feature_id.startswith("timeline-"):
            from generate_timelines import diagnose_timeline_capabilities
            diagnosis = diagnose_timeline_capabilities(narrative_only=feature_id == "timeline-text", images_only=feature_id == "timeline-image")
            plan["backend"] = diagnosis
            if not diagnosis.get("available"):
                raise FeatureBlocked("needs-runtime", "timeline backend configuration is not ready")
            if not any((p.get("classifications") or {}).get(params["topic"], {}).get("primary_category") for p in papers):
                raise FeatureBlocked("insufficient-data", "timeline requires existing paper categories")
            if feature_id == "timeline-image":
                _require_file(ROOT / "docs" / params["topic"] / "_category_narratives.json", "saved timeline narratives")
    elif feature_id == "institution-export":
        _require_file(Path(params.get("db") or ROOT / ".cache/bibliography.sqlite3"), "bibliography database")
        if importlib.util.find_spec("openpyxl") is None:
            raise FeatureBlocked("needs-runtime", "openpyxl is required for public Excel export")
    elif feature_id == "audio":
        directory = _inside(ROOT / "docs/papers", params["slug"])
        if not (directory / "review.md").is_file() and not (directory / "audio_script.txt").is_file():
            raise FeatureBlocked("insufficient-data", "review or validated saved audio script is required")
        if not shutil.which("ffmpeg"):
            raise FeatureBlocked("needs-runtime", "ffmpeg is required for MP3 output")
    elif feature_id == "email":
        path = Path(params["file_path"])
        _require_file(path, "MP3 attachment")
        if path.suffix.lower() != ".mp3" or not 0 < path.stat().st_size <= 20 * 1024 * 1024:
            raise FeatureBlocked("failed", "attachment must be a nonempty MP3 no larger than 20 MiB")
        if any(not re.fullmatch(r"[^\s<>@]+@[^\s<>@]+\.[^\s<>@]+", params[field]) for field in ("sender", "recipient")):
            raise FeatureBlocked("failed", "sender and recipient must be plain email addresses")
        if any(ch in params.get("subject", "") for ch in "\r\n\0"):
            raise FeatureBlocked("failed", "invalid email subject")
        plan["authorization"] = "sender domain and recipient permissions are checked by Resend only on send"
    elif feature_id == "zotero-sync":
        if not params["dry_run"] and not params["confirm"]:
            raise FeatureBlocked("blocked", "applying remote deletions requires confirm: true")
        path = ROOT / "config.json"
        _require_file(path, "Zotero topic configuration")
        config = json.loads(path.read_text(encoding="utf-8"))
        if not (config.get("zotero", {}).get("collections") or {}).get(params["topic"]):
            raise FeatureBlocked("insufficient-data", "Zotero collection mapping is required")
    elif feature_id == "publish":
        if not params["confirm"]:
            raise FeatureBlocked("blocked", "publication requires confirm: true")
        if not shutil.which("node") or not shutil.which("git"):
            raise FeatureBlocked("needs-runtime", "Node.js and Git are required for publication")
        _require_file(ROOT / "docs" / params["topic"] / "index.html", "topic HTML")
        _credential("cloudflare-account")
    if provider:
        _credential(provider, request.get("credential_ref"))
    return plan


@contextlib.contextmanager
def _safe_output():
    stream = io.StringIO()
    try:
        with contextlib.redirect_stdout(stream), contextlib.redirect_stderr(stream):
            yield
    finally:
        if stream.getvalue():
            from local_review import _sanitize_text
            print(_sanitize_text(stream.getvalue(), limit=16000), file=sys.stderr)


def _child(argv: list[str], *, credentials: list[str] = ()) -> subprocess.CompletedProcess:
    environment = dict(os.environ)
    for provider in credentials:
        environment[ENV_NAMES[provider]] = _credential(provider)
    result = subprocess.run([sys.executable, *argv], cwd=ROOT, env=environment,
                            capture_output=True, text=True, timeout=28800, check=False)
    if result.returncode:
        raise FeatureBlocked("failed", f"selected module exited with code {result.returncode}")
    return result


def _email(params: dict) -> dict:
    key = _credential("resend")
    path = Path(params["file_path"])
    body = json.dumps({"from": params["sender"], "to": [params["recipient"]],
                       "subject": params["subject"], "text": "The requested audio overview is attached.",
                       "attachments": [{"filename": path.name, "content": base64.b64encode(path.read_bytes()).decode("ascii")}]}).encode()
    req = urllib.request.Request("https://api.resend.com/emails", body,
                                 {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=30) as response:
        receipt = json.load(response)
    if not isinstance(receipt, dict) or not isinstance(receipt.get("id"), str) or not receipt["id"]:
        raise FeatureBlocked("failed", "Resend did not return a send receipt")
    return {"outputs": [str(path)], "provenance": {"resend_id": receipt["id"]}}


def _extract(params: dict) -> dict:
    from local_review import _exclusive_output_lock
    from run_update_force import extract_text, extract_figures
    output = Path(params["output_dir"])
    with _exclusive_output_lock(output):
        if output.exists() and any(output.iterdir()):
            raise FeatureBlocked("failed", "extraction output is no longer empty")
        with tempfile.TemporaryDirectory(prefix=".extract-stage-", dir=output.parent) as temporary:
            stage = Path(temporary) / output.name
            stage.mkdir()
            if not extract_text(params["pdf_path"], str(stage)):
                raise FeatureBlocked("insufficient-data", "PDF text extraction failed")
            figures = extract_figures(params["pdf_path"], str(stage), validate_with_gemini=False)
            _require_file(stage / "text.md", "extracted text")
            if output.exists():
                output.rmdir()
            os.replace(stage, output)
    return {"outputs": [str(output / "text.md"), str(output / "figures")], "figures": len(figures)}


def _execute(feature: dict, params: dict) -> dict:
    feature_id = feature["id"]
    pipe = ROOT / "pipeline"
    if feature_id == "extract":
        return _extract(params)
    if feature_id == "email":
        return _email(params)
    if feature_id == "audio":
        from generate_audio import _run_audio
        result = _run_audio(params["slug"], out=params.get("output_path"),
                            speakers=params["speakers"], language=params["language"],
                            regenerate_script=params["regenerate_script"])
        return {"outputs": [result["audio_path"], result["script_path"]], "provenance": result}
    if feature_id in {"keyword-search", "semantic-search"}:
        mode = "bm25" if feature_id == "keyword-search" else "hybrid"
        credentials = ["google"] if feature_id == "semantic-search" else []
        if params["operation"] == "build":
            _child([str(pipe / "build_search_index.py"), "--topic", params["topic"], "--mode", mode,
                    "--include-text", params["include_text"]], credentials=credentials)
            path = ROOT / "docs" / params["topic"] / "_search_index.json"
            _require_file(path, "built search index")
            return {"outputs": [str(path)], "retrieval_mode": mode}
        result = _child([str(pipe / "query_search_index.py"), "--topic", params["topic"],
                         "--query", params["query"], "--top-k", str(params["top_k"]), "--mode", mode, "--json"], credentials=credentials)
        payload = json.loads(result.stdout)
        if not isinstance(payload, dict) or not isinstance(payload.get("results"), list):
            raise FeatureBlocked("failed", "invalid retrieval response")
        return {"outputs": [], "retrieval": payload}
    if feature_id == "institution-export":
        from export_institutions_public import fetch_rows, write_csv, write_xlsx
        rows, redacted = fetch_rows(params.get("db") or ROOT / ".cache/bibliography.sqlite3")
        directory = Path(params["outdir"])
        directory.mkdir(parents=True, exist_ok=True)
        csv_path, xlsx_path = directory / "institutions_public.csv", directory / "institutions_public.xlsx"
        write_csv(rows, csv_path)
        write_xlsx(rows, xlsx_path)
        return {"outputs": [str(csv_path), str(xlsx_path)], "provenance": {"rows": len(rows), "redacted": redacted}}
    if feature_id in {"metrics", "bibliography-update"}:
        papers = _topic_papers(params["topic"])
        for offset in range(0, len(papers), 100):
            slugs = ",".join(p["slug"] for p in papers[offset:offset + 100])
            if feature_id == "metrics":
                command = [str(pipe / "run_metrics.py"), "--slugs", slugs]
            else:
                command = [str(pipe / "build_bibliography_db.py"), "--slugs", slugs,
                           "--changed-only", "--skip-zotero", "--no-email"]
                if params["offline"]:
                    command.append("--offline")
            _child(command)
        if feature_id == "bibliography-update":
            for option in ("--backfill-author-institutions", "--finalize"):
                _child([str(pipe / "build_bibliography_db.py"), option, "--no-email"])
            return {"outputs": [str(ROOT / ".cache/bibliography.sqlite3")], "paper_count": len(papers)}
        outputs = [str(ROOT / "docs/papers" / p["slug"] / name) for p in papers
                   for name in ("citations.md", "references.md")
                   if (ROOT / "docs/papers" / p["slug"] / name).is_file()]
        return {"outputs": outputs, "paper_count": len(papers)}
    if feature_id in {"timeline-text", "timeline-image"}:
        # Fixed child program isolates the narrative SDK environment and captures
        # early insufficient-data returns that the historical CLI did not expose.
        code = ("import json,sys;sys.path.insert(0,sys.argv[1]);"
                "from generate_timelines import _run_timeline;"
                "r=_run_timeline(sys.argv[2],narrative_only=sys.argv[3]=='timeline-text',"
                "images_only=sys.argv[3]=='timeline-image');print(json.dumps(r))")
        if feature_id == "timeline-text":
            credentials = ["anthropic"]
        else:
            from generate_timelines import diagnose_timeline_capabilities
            diagnosis = diagnose_timeline_capabilities(images_only=True)
            if not diagnosis.get("available"):
                raise FeatureBlocked("needs-runtime", "configured image backend is unavailable")
            credentials = list(diagnosis.get("credentials", {}))
        result = _child(["-c", code, str(pipe), params["topic"], feature_id],
                        credentials=credentials)
        response = json.loads(result.stdout.strip().splitlines()[-1])
        if isinstance(response, dict) and response.get("status") not in SUCCESS:
            raise FeatureBlocked("insufficient-data", "timeline inputs or configured backend are unavailable")
        topic_dir = ROOT / "docs" / params["topic"]
        outputs = ([topic_dir / "_category_narratives.json"] if feature_id == "timeline-text"
                   else [*topic_dir.glob("category_timeline_*.png"), topic_dir / "research_timeline.png"])
        outputs = [str(path) for path in outputs if path.is_file()]
        if not outputs:
            raise FeatureBlocked("failed", "timeline produced no requested artifact")
        return {"outputs": outputs}
    if feature_id == "zotero-sync":
        command = [str(pipe / "sync_zotero.py"), "--topic", params["topic"]]
        if params["dry_run"]:
            command.append("--dry-run")
        _child(command, credentials=["zotero"])
        return {"outputs": [], "applied": not params["dry_run"]}
    if feature_id == "publish":
        _child([str(pipe / "prepare_deploy.py"), "--topic", params["topic"], "--push", "--cf-strict"],
               credentials=["cloudflare", "cloudflare-account"])
        return {"outputs": [], "published": True}
    raise FeatureBlocked("failed", "capability has no execution handler")


def run_request(payload: Any, *, execute: bool = False) -> dict[str, Any]:
    feature_id = payload.get("feature") if isinstance(payload, dict) else None
    if not isinstance(feature_id, str):
        feature_id = "unknown"
    try:
        feature = next((f for f in _registry() if f["id"] == feature_id), None)
        if feature is None:
            feature_id = "unknown"
            raise FeatureBlocked("failed", "unsupported feature")
        params = _validate(feature, payload)
        if feature_id == "review":
            from local_review import run_request as review_request
            return review_request(_review_request(payload, params), execute=execute)
        if feature_id in TEXT_FEATURES:
            from text_task import run
            return run(_text_request(payload, params), execute=execute)
        plan = _preflight(feature, payload, params)
        if not execute:
            return plan
        mutates_corpus = feature_id in {
            "extract", "audio", "metrics", "bibliography-update",
            "timeline-text", "timeline-image", "publish",
        } or (feature_id == "zotero-sync" and not params["dry_run"]) or (
            feature_id in {"keyword-search", "semantic-search"} and params["operation"] == "build")
        if mutates_corpus:
            from lib.corpus_store import corpus_operation_lock
            lease = corpus_operation_lock(ROOT / "docs/papers", exclusive=True)
        else:
            lease = contextlib.nullcontext()
        with lease, _safe_output():
            result = _execute(feature, params)
        return {**plan, "status": "completed", **result}
    except FeatureBlocked as exc:
        return _result(feature_id, exc.status, error=str(exc))
    except ImportError as exc:
        return _result(feature_id, "needs-runtime", error=f"selected capability runtime is unavailable ({type(exc).__name__})")
    except Exception as exc:
        # Third-party exception text may contain credentials or source data.
        return _result(feature_id, "failed", error=f"selected capability failed ({type(exc).__name__})")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", help="JSON request file")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--list", action="store_true")
    args = parser.parse_args(argv)
    if args.list:
        if args.request or args.execute:
            parser.error("--list cannot be combined with a task")
        print(json.dumps({"schema_version": 1, "features": _registry()}, ensure_ascii=False))
        return 0
    if not args.request:
        parser.error("--request is required")
    try:
        path = Path(args.request)
        if path.stat().st_size > 2_000_000:
            raise ValueError("request size")
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        payload = None
    result = run_request(payload, execute=args.execute)
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["status"] in SUCCESS else 2


if __name__ == "__main__":
    raise SystemExit(main())
