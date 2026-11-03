#!/usr/bin/env python3
"""Refresh published views from existing reviews, without rerunning the pipeline.

Existing search indexes determine their own retrieval/model/source policy. A
missing index uses the search builder's standard hybrid policy. Hybrid cache
misses can incur separate Google embedding costs; review budgets do not cover
these calls. No PDF ingestion, classification, connection inference or deployment
is performed here.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import selectors
import shlex
import signal
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

PIPELINE_DIR = Path(__file__).resolve().parent
if str(PIPELINE_DIR) not in sys.path:
    sys.path.insert(0, str(PIPELINE_DIR))
from config_loader import PAPERS_DIR, load_config

DEFAULT_MODEL = "gemini-embedding-001"
OUTPUT_LIMIT = 2 * 1024 * 1024
OUTPUT_TAIL = 8000
_RESERVED = {"papers", "notes", "public", "_cross"}


def paper_topics(entry: dict[str, Any]) -> list[str]:
    """Membership comes from the registered corpus, never a review request."""
    topics = entry.get("topics") or []
    if not isinstance(topics, list):
        raise ValueError("invalid registered topic membership")
    return sorted({topic for topic in [*topics, entry.get("primary_topic")]
                   if isinstance(topic, str) and topic})


def _topic_path(papers: Path, topic: str) -> Path:
    if (not isinstance(topic, str) or not topic or topic in {".", ".."}
            or topic.startswith(".") or any(c in topic for c in "/\\\0")):
        raise ValueError("invalid topic name")
    path = papers.parent / topic
    if path.is_symlink() or path.resolve().parent != papers.parent:
        raise ValueError("topic directory escapes the canonical docs root")
    if topic in _RESERVED - {"_cross"}:
        raise ValueError("reserved directory is not a topic")
    return path


def _read_object(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path.name} must be an object")
    return value


def _search_settings(directory: Path, *, index: dict[str, Any] | None = None) -> dict[str, Any]:
    path = directory / "_search_index.json"
    if index is None:
        index = _read_object(path) if path.exists() else {}
    mode = index.get("retrieval_mode")
    if mode is None:
        if path.exists() and not isinstance(index.get("model"), str):
            raise ValueError("legacy search index lacks an embedding model")
        mode = "hybrid"
    if mode not in {"hybrid", "bm25"}:
        raise ValueError("unsupported search retrieval_mode")
    if mode == "bm25" and index.get("model") is not None:
        raise ValueError("BM25 search index must not have an embedding model")
    model = index.get("model", DEFAULT_MODEL) if mode == "hybrid" else None
    if mode == "hybrid" and (not isinstance(model, str) or not model.strip()):
        raise ValueError("hybrid search index lacks an embedding model")
    options = index.get("source_options", {})
    if not isinstance(options, dict):
        raise ValueError("invalid search source_options")
    if options.keys() - {"include_text", "include_personal_notes"}:
        raise ValueError("unsupported search source_options; refusing to change policy")
    settings: dict[str, Any] = {"mode": mode, "model": model,
                                "include_text": "auto", "include_personal_notes": "auto"}
    for name in ("include_text", "include_personal_notes"):
        value = options.get(name, index.get(name, "auto"))
        if isinstance(value, bool):
            value = "yes" if value else "no"
        if value not in {"auto", "yes", "no"}:
            raise ValueError(f"invalid search {name}")
        settings[name] = value
    settings["source_options"] = options
    return settings


def _safe_output(value: object) -> str:
    text = str(value or "")
    for name, secret in os.environ.items():
        if len(secret) >= 4 and any(marker in name.upper() for marker in ("KEY", "TOKEN", "SECRET", "PASSWORD")):
            text = text.replace(secret, "[REDACTED]")
    text = re.sub(r"(?:sk-(?:ant-)?[A-Za-z0-9_-]{8,}|AIza[A-Za-z0-9_-]{20,})", "[REDACTED]", text)
    text = re.sub(r"(?i)bearer\s+\S+", "Bearer [REDACTED]", text)
    return text[-OUTPUT_TAIL:]


def _run_builder(command: list[str], *, timeout: float) -> dict[str, Any]:
    """Drain both output streams with bounded memory and a wall-clock deadline."""
    env = dict(os.environ, SKIP_ZOTERO_KEYS="1", PYTHONUTF8="1")
    process = subprocess.Popen(command, cwd=str(PIPELINE_DIR.parent), env=env,
                               stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT, start_new_session=True)
    tail = bytearray()
    total = 0
    failure = None
    deadline = time.monotonic() + timeout
    selector = selectors.DefaultSelector()
    assert process.stdout is not None
    selector.register(process.stdout, selectors.EVENT_READ)
    try:
        while selector.get_map() or process.poll() is None:
            if time.monotonic() >= deadline:
                failure = f"builder timed out after {timeout:g}s"
                break
            for key, _ in selector.select(min(0.2, max(0, deadline - time.monotonic()))):
                data = os.read(key.fd, 65536)
                if not data:
                    selector.unregister(key.fileobj)
                    continue
                total += len(data)
                tail.extend(data)
                del tail[:-OUTPUT_TAIL]
                if total > OUTPUT_LIMIT:
                    failure = "builder exceeded the output limit"
                    break
            if failure:
                break
        if failure:
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
        code = process.wait(timeout=5)
    finally:
        selector.close()
        process.stdout.close()
        if process.poll() is None:
            process.kill()
            process.wait(timeout=5)
    result: dict[str, Any] = {"status": "failed" if failure or code else "completed",
                              "returncode": code, "output": _safe_output(tail.decode("utf-8", errors="replace"))}
    if failure or code:
        result["error"] = failure or f"builder exited with status {code}"
    return result


def _retry_command(slug: str | None, papers: Path, previous_topics: list[str], all_topics: bool) -> str:
    command = [sys.executable, str(PIPELINE_DIR / "refresh_paper_views.py")]
    command += ["--all-topics"] if all_topics else ["--slug", str(slug)]
    command += ["--papers-dir", str(papers)]
    for topic in previous_topics:
        command += ["--previous-topic", topic]
    return shlex.join(command)


def _cross_plan(papers: Path, topics: list[str], *, all_topics: bool) -> list[dict[str, Any]]:
    directory = _topic_path(papers, "_cross")
    if not any((directory / name).exists() for name in ("index.html", "_search_index.json", "network.html")):
        return []
    meta_path = directory / "_cross_meta.json"
    meta = _read_object(meta_path) if meta_path.exists() else {}
    index_path = directory / "_search_index.json"
    index = _read_object(index_path) if index_path.exists() else {}
    sources = list(index.get("source_indexes") or {})
    if not sources:
        sources = [row.get("slug") if isinstance(row, dict) else row for row in meta.get("topics", [])]
    if not sources:
        raise ValueError("existing _cross has no recorded source topics")
    sources = sorted(set(sources))
    for topic in sources:
        _topic_path(papers, topic)
        if topic == "_cross":
            raise ValueError("_cross cannot be its own source")
    if not all_topics and not set(topics).intersection(sources):
        return []
    settings = _search_settings(directory, index=index)
    command = [sys.executable, str(PIPELINE_DIR / "build_cross_index.py"), "--topics", *sources,
               "--mode", settings["mode"], "--title", str(meta.get("title") or "통합 Deep Research")]
    steps = [{"topic": "_cross", "builder": "cross", "status": "planned", "command": command,
              "settings": {**settings, "topics": sources},
              "outputs": [str(directory / name) for name in
                          ("index.html", "_search_index.json", "_paper_connections.json", "_cross_meta.json")]}]
    if settings["mode"] == "hybrid":
        steps[0]["outputs"].append(str(directory / "_search_index_emb.bin"))
    if (directory / "network.html").is_file():
        steps.append(_network_step("_cross", directory))
    return steps


def _network_step(topic: str, directory: Path) -> dict[str, Any]:
    return {"topic": topic, "builder": "network", "status": "planned",
            "command": [sys.executable, str(PIPELINE_DIR / "generate_network.py"), "--topic", topic],
            "outputs": [str(directory / "network.html")]}


def _refresh_paper_views(slug: str | None = None, *, papers_dir: str | Path | None = None,
                         previous_topics=(), all_topics: bool = False, dry_run: bool = False,
                         timeout: float = 900.0, allow_paid: bool = True) -> dict[str, Any]:
    """Plan and build from a single snapshot under the caller's operation lease."""
    papers = Path(papers_dir if papers_dir is not None else PAPERS_DIR).expanduser().resolve()
    previous = sorted(set(previous_topics))
    report: dict[str, Any] = {"schema_version": 1, "status": "planned" if dry_run else "completed",
                              "slug": slug, "topics": [], "steps": [], "errors": [],
                              "retry_command": _retry_command(slug, papers, previous, all_topics)}
    if papers != Path(PAPERS_DIR).expanduser().resolve():
        report.update(status="skipped", reason="standalone output outside the canonical corpus")
        return report
    try:
        if not math.isfinite(timeout) or timeout <= 0 or timeout > 3600:
            raise ValueError("timeout must be between 0 and 3600 seconds")
        if all_topics == bool(slug):
            raise ValueError("choose either a registered slug or all_topics")
        if not all_topics:
            from lib.corpus_store import _is_safe_slug
            if not _is_safe_slug(slug):
                raise ValueError("invalid paper slug")
            directory = papers / slug
            if directory.is_symlink() or directory.resolve().parent != papers:
                raise ValueError("paper directory escapes the canonical corpus")
            if (directory / ".corpus-reservation.json").exists():
                report.update(status="deferred", reason="pending registration")
                return report
        index_path = papers / "_papers_index.json"
        index = json.loads(index_path.read_text(encoding="utf-8")) if index_path.exists() else []
        if not isinstance(index, list) or any(not isinstance(entry, dict) for entry in index):
            raise ValueError("corpus index must be a list of objects")
        if all_topics:
            config = load_config()
            configured = config.get("zotero", {}).get("collections", {})
            topics = set(configured) | {topic for entry in index for topic in paper_topics(entry)}
        else:
            matches = [entry for entry in index if entry.get("slug") == slug]
            if not matches:
                report.update(status="skipped", reason="paper is not registered in the canonical corpus")
                return report
            if len(matches) != 1:
                raise ValueError("paper slug is registered more than once")
            topics = set(paper_topics(matches[0])) | set(previous)
            if not topics:
                raise ValueError("registered paper has no topics")
            if not (directory / "review.md").is_file():
                raise ValueError("registered paper review is missing")
            report["steps"].append({
                "topic": "papers", "builder": "metadata", "status": "planned",
                "outputs": [str(index_path)],
            })
            render = (
                "import sys; sys.path.insert(0, sys.argv[1]); "
                "from review_to_html import _run_review_to_html; "
                "result = _run_review_to_html(slug=sys.argv[2]); "
                "sys.exit(0 if result == {'converted': 1, 'skipped': 0} else 1)"
            )
            report["steps"].append({
                "topic": "papers", "builder": "review", "status": "planned",
                "command": [sys.executable, "-c", render, str(PIPELINE_DIR), slug],
                "outputs": [str(directory / "index.html")],
            })
        topics.discard("_cross")
        report["topics"] = sorted(topics)
        for topic in report["topics"]:
            directory = _topic_path(papers, topic)
            try:
                settings = _search_settings(directory)
                command = [sys.executable, str(PIPELINE_DIR / "build_search_index.py"), "--topic", topic,
                           "--mode", settings["mode"], "--include-text", settings["include_text"],
                           "--include-personal-notes", settings["include_personal_notes"]]
                if settings["model"]:
                    command += ["--model", settings["model"]]
                outputs = [str(directory / "_search_index.json")]
                if settings["mode"] == "hybrid":
                    outputs.append(str(directory / "_search_index_emb.bin"))
                report["steps"].append({"topic": topic, "builder": "search", "status": "planned",
                                         "command": command, "settings": settings, "outputs": outputs})
            except (OSError, ValueError) as exc:
                report["steps"].append({"topic": topic, "builder": "search", "status": "failed", "error": str(exc)})
            # The page discovers its retrieval UI from the published search
            # index, so a new index must exist before rendering the topic page.
            report["steps"].append({"topic": topic, "builder": "topic", "status": "planned",
                                     "command": [sys.executable, str(PIPELINE_DIR / "build_topic_index.py"), topic],
                                     "outputs": [str(directory / "index.html")]})
            if (directory / "network.html").is_file():
                report["steps"].append(_network_step(topic, directory))
        try:
            cross_steps = _cross_plan(papers, report["topics"], all_topics=all_topics)
            report["steps"].extend(cross_steps)
            if cross_steps:
                report["topics"] = sorted({*report["topics"], "_cross"})
        except (OSError, ValueError, TypeError) as exc:
            report["steps"].append({"topic": "_cross", "builder": "cross", "status": "failed", "error": str(exc)})
        if any(step.get("settings", {}).get("mode") == "hybrid" and step["builder"] == "search"
               for step in report["steps"]):
            report["embedding_cost"] = {"provider": "google", "required_key": "GOOGLE_API_KEY",
                                         "condition": "only embedding cache misses", "cost": "unpriced",
                                         "covered_by_review_budget": False}
        if not dry_run:
            _execute_steps(report, papers, timeout=timeout, allow_paid=allow_paid)
    except Exception as exc:
        report["errors"].append(_safe_output(f"{type(exc).__name__}: {exc}"))
    report["errors"].extend(_safe_output(f"{step['topic']}/{step['builder']}: {step['error']}")
                            for step in report["steps"] if step.get("error"))
    if report["errors"]:
        report["status"] = "failed"
    return report


def refresh_paper_views(slug: str | None = None, *, papers_dir: str | Path | None = None,
                        previous_topics=(), all_topics: bool = False, dry_run: bool = False,
                        timeout: float = 900.0, allow_paid: bool = True) -> dict[str, Any]:
    """Refresh a registered paper's views, or all topics when explicit.

    Call only after releasing review/index/operation locks. Failures are returned
    without discarding paid review outputs. Planning is read-only, including no
    credential lookup or lock acquisition. Executing holds the exclusive lease
    while reading membership/settings as well as publishing their derived views.
    """
    papers = Path(papers_dir if papers_dir is not None else PAPERS_DIR).expanduser().resolve()
    arguments = {"papers_dir": papers, "previous_topics": previous_topics,
                 "all_topics": all_topics, "dry_run": dry_run,
                 "timeout": timeout, "allow_paid": allow_paid}
    if dry_run or papers != Path(PAPERS_DIR).expanduser().resolve():
        return _refresh_paper_views(slug, **arguments)
    from lib.corpus_store import _is_safe_slug, corpus_operation_lock
    if not all_topics and _is_safe_slug(slug) and (papers / slug / ".corpus-reservation.json").exists():
        return _refresh_paper_views(slug, **arguments)
    try:
        with corpus_operation_lock(papers, exclusive=True, timeout=5.0):
            return _refresh_paper_views(slug, **arguments)
    except Exception as exc:
        arguments["dry_run"] = True
        report = _refresh_paper_views(slug, **arguments)
        report["status"] = "failed"
        report["errors"].append(_safe_output(f"{type(exc).__name__}: {exc}"))
        return report


def _sync_review_metadata(papers: Path, slug: str) -> None:
    """Update four review-owned fields under the caller's exclusive lease."""
    from build_papers_index import parse_review
    from lib.atomic_io import atomic_write_json
    from lib.corpus_store import load_index_strict
    parsed = parse_review(slug)
    if not isinstance(parsed, dict):
        raise ValueError("review metadata could not be parsed")
    fields = ("essence", "score", "has_figures", "text_md_sha256")
    metadata = {name: parsed[name] for name in fields}
    index = load_index_strict(papers)
    matches = [entry for entry in index if entry.get("slug") == slug]
    if len(matches) != 1:
        raise ValueError("paper registration changed before metadata refresh")
    entry = matches[0]
    if any(entry.get(name) != value for name, value in metadata.items()):
        entry.update(metadata)
        atomic_write_json(papers / "_papers_index.json", index)


def _execute_steps(report: dict[str, Any], papers: Path, *, timeout: float, allow_paid: bool) -> None:
    for step in report["steps"]:
        if step["status"] == "failed":
            continue
        try:
            if any(Path(path).is_symlink() for path in step.get("outputs", [])):
                raise ValueError("refusing to overwrite a symlinked view output")
            if step["builder"] == "metadata":
                _sync_review_metadata(papers, report["slug"])
                step["status"] = "completed"
                continue
            if step["builder"] == "search" and step["settings"]["mode"] == "hybrid" and not allow_paid:
                raise ValueError("review budget does not cover unpriced Google embedding cache misses; retry views separately")
            if step["builder"] == "cross":
                sources = step["settings"]["topics"]
                if any(previous["status"] == "failed" and previous["topic"] in sources
                       and previous["builder"] == "search" for previous in report["steps"]):
                    raise ValueError("aggregate refresh blocked by failed source search indexes")
                if step["settings"]["mode"] == "hybrid":
                    for topic in sources:
                        settings = _search_settings(_topic_path(papers, topic))
                        if settings["mode"] != "hybrid" or settings["model"] != step["settings"]["model"]:
                            raise ValueError("aggregate source mode/model differs from the existing hybrid aggregate")
            if step["topic"] == "_cross" and step["builder"] == "network" and any(
                    previous["builder"] == "cross" and previous["status"] == "failed" for previous in report["steps"]):
                raise ValueError("aggregate network blocked by failed aggregate refresh")
            if step["builder"] != "review":
                _topic_path(papers, step["topic"]).mkdir(parents=True, exist_ok=True)
            result = _run_builder(step["command"], timeout=timeout)
            step.update(result)
            if result["status"] != "completed":
                step.setdefault("error", "builder did not complete")
            elif any(not Path(path).is_file() or Path(path).stat().st_size == 0 for path in step["outputs"]):
                raise ValueError("builder did not publish every required output")
        except Exception as exc:
            step.update(status="failed", error=_safe_output(f"{type(exc).__name__}: {exc}"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    scope = parser.add_mutually_exclusive_group(required=True)
    scope.add_argument("--slug")
    scope.add_argument("--all-topics", action="store_true")
    parser.add_argument("--papers-dir")
    parser.add_argument("--previous-topic", action="append", default=[])
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--timeout", type=float, default=900.0)
    args = parser.parse_args(argv)
    result = refresh_paper_views(args.slug, papers_dir=args.papers_dir,
                                 previous_topics=args.previous_topic, all_topics=args.all_topics,
                                 dry_run=args.dry_run, timeout=args.timeout)
    print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
    return 1 if result["status"] == "failed" else 0


if __name__ == "__main__":
    from _env_guard import force_py312
    force_py312()
    raise SystemExit(main())
