#!/usr/bin/env python3
"""Transactional ownership and index updates for ``docs/papers``.

The lock file is deliberately permanent: POSIX flock ownership, not pathname
existence, is the authority, so a crashed writer cannot leave a blocking lock.
"""
from __future__ import annotations

import argparse
import contextlib
import fcntl
import json
import os
import re
import secrets
import sys
import time
import unicodedata
from pathlib import Path
from typing import Any, Iterator

# This script is also invoked directly by Curio, outside ``pipeline``.
_PIPELINE_DIR = Path(__file__).resolve().parents[1]
if str(_PIPELINE_DIR) not in sys.path:
    sys.path.insert(0, str(_PIPELINE_DIR))
from lib.atomic_io import atomic_write_json

INDEX_NAME = "_papers_index.json"
RESERVATION_NAME = ".corpus-reservation.json"
IDENTITY_FIELDS = {"slug", "key", "zotero_item_key", "doi", "title"}


class CorpusStoreError(RuntimeError):
    def __init__(self, message: str, code: str = "invalid-request"):
        super().__init__(message)
        self.code = code


class CorpusStoreBusyError(CorpusStoreError):
    pass


def _papers_dir(papers_dir: str | Path) -> Path:
    papers = Path(papers_dir).expanduser()
    papers.mkdir(parents=True, exist_ok=True)
    return papers.resolve()


def _safe_slug(slug: object) -> str:
    if not _is_safe_slug(slug):
        raise CorpusStoreError("invalid slug", code="invalid-slug")
    return slug


def _is_safe_slug(slug: object) -> bool:
    """Allow stable Unicode filenames without admitting path syntax."""
    if not isinstance(slug, str):
        return False
    prefix, separator, suffix = slug.partition("_")
    if not separator or not prefix or not suffix or not prefix.isascii() or not prefix.isdecimal():
        return False
    return all(
        character.isalnum()
        or unicodedata.category(character).startswith("M")
        or character in "_-"
        for character in suffix
    )


def _slug_dir(papers: Path, slug: object) -> Path:
    directory = papers / _safe_slug(slug)
    if directory.is_symlink() or directory.resolve(strict=False).parent != papers:
        raise CorpusStoreError("invalid slug directory")
    return directory


def index_path(papers_dir: str | Path) -> Path:
    return _papers_dir(papers_dir) / INDEX_NAME


def index_lock_path(papers_dir: str | Path) -> Path:
    return _papers_dir(papers_dir) / "._papers_index.json.flock"


def operation_lock_path(papers_dir: str | Path) -> Path:
    """Stable corpus-wide lease inode for review and full-pipeline operations."""
    return _papers_dir(papers_dir) / ".corpus-operation.flock"


def _has_pending_reservation(papers: Path) -> bool:
    """Treat every marker, including malformed ones, as a live reservation."""
    return any(
        child.is_dir() and not child.is_symlink()
        and (child / RESERVATION_NAME).exists()
        for child in papers.iterdir()
    )


@contextlib.contextmanager
def corpus_operation_lock(papers_dir: str | Path, *, exclusive: bool = False,
                          timeout: float = 0.0) -> Iterator[None]:
    """Acquire a shared review or exclusive corpus-mutation operation lease.

    An exclusive owner also refuses pending reservations after it owns the
    flock. This closes the interval in which a local review has released its
    output lock but has not registered or cancelled its reservation yet.
    """
    if timeout < 0:
        raise ValueError("operation lock timeout must be non-negative")
    papers = _papers_dir(papers_dir)
    path = operation_lock_path(papers)
    fd = os.open(path, os.O_CREAT | os.O_RDWR, 0o600)
    os.set_inheritable(fd, False)
    os.chmod(path, 0o600)
    operation = fcntl.LOCK_EX if exclusive else fcntl.LOCK_SH
    deadline = time.monotonic() + timeout
    try:
        while True:
            try:
                fcntl.flock(fd, operation | fcntl.LOCK_NB)
                break
            except BlockingIOError as exc:
                if time.monotonic() >= deadline:
                    raise CorpusStoreBusyError("corpus operation lock busy") from exc
                time.sleep(0.05)
        if exclusive and _has_pending_reservation(papers):
            raise CorpusStoreBusyError("corpus operation blocked by pending reservation")
        yield
    finally:
        try:
            fcntl.flock(fd, fcntl.LOCK_UN)
        finally:
            os.close(fd)


@contextlib.contextmanager
def corpus_index_lock(papers_dir: str | Path, *, timeout: float = 5.0) -> Iterator[None]:
    """Acquire the shared bounded POSIX index writer lock."""
    papers = _papers_dir(papers_dir)
    path = index_lock_path(papers)
    fd = os.open(path, os.O_CREAT | os.O_RDWR, 0o600)
    os.set_inheritable(fd, False)
    os.chmod(path, 0o600)
    deadline = time.monotonic() + timeout
    try:
        while True:
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except BlockingIOError as exc:
                if time.monotonic() >= deadline:
                    raise CorpusStoreBusyError("corpus index lock busy") from exc
                time.sleep(0.05)
        yield
    finally:
        try:
            fcntl.flock(fd, fcntl.LOCK_UN)
        finally:
            os.close(fd)


def load_index_strict(papers_dir: str | Path) -> list[dict[str, Any]]:
    path = index_path(papers_dir)
    if not path.exists():
        return []
    try:
        contents = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise CorpusStoreError("corpus index is inaccessible", code="filesystem-error") from exc
    try:
        value = json.loads(contents)
    except json.JSONDecodeError as exc:
        raise CorpusStoreError("corpus index is corrupt", code="invalid-index") from exc
    if not isinstance(value, list) or any(not isinstance(entry, dict) for entry in value):
        raise CorpusStoreError("corpus index must be a list of objects", code="invalid-index")
    return value


def _normal(value: object) -> str:
    return "".join(character for character in str(value or "").casefold() if character.isalnum())


def _doi(value: object) -> str:
    return str(value or "").strip().casefold()


def _identity_match(entry: dict[str, Any], identity: dict[str, Any]) -> bool:
    key = str(identity.get("key") or "").strip()
    if key and key in {str(entry.get("key") or ""), str(entry.get("zotero_item_key") or "")}:
        return True
    doi = _doi(identity.get("doi"))
    if doi and doi == _doi(entry.get("doi") or entry.get("DOI")):
        return True
    title = _normal(identity.get("title"))
    return bool(title and len(title) >= 10 and title == _normal(entry.get("title")))


def _identity_consistent(candidate: dict[str, Any], identity: dict[str, Any]) -> bool:
    """Require every identifier supplied at reservation time to agree."""
    key = str(identity.get("key") or "").strip()
    if key and key not in {str(candidate.get("key") or ""),
                           str(candidate.get("zotero_item_key") or "")}:
        return False
    doi = _doi(identity.get("doi"))
    if doi and doi != _doi(candidate.get("doi") or candidate.get("DOI")):
        return False
    title = _normal(identity.get("title"))
    if title and title != _normal(candidate.get("title")):
        return False
    return bool(key or doi or title)


def _safe_title(title: object) -> str:
    safe = "".join(c if c.isalnum() or c in " -_" else "" for c in str(title or "Unknown"))[:60].strip()
    return safe.replace(" ", "_") or "Unknown"


def _all_slugs(papers: Path, entries: list[dict[str, Any]]) -> set[str]:
    names = {_safe_slug(e["slug"]) for e in entries if e.get("slug")}
    if papers.exists():
        for directory in papers.iterdir():
            if directory.is_dir() and _is_safe_slug(directory.name):
                _slug_dir(papers, directory.name)
                names.add(directory.name)
    return names


def _new_slug(identity: dict[str, Any], slugs: set[str]) -> str:
    maximum = max((int(m.group(1)) for slug in slugs if (m := re.match(r"(\d+)_", slug))), default=0)
    return f"{maximum + 1:03d}_{_safe_title(identity.get('title'))}"


def _reservation_path(papers: Path, slug: str) -> Path:
    return _slug_dir(papers, slug) / RESERVATION_NAME


def _read_reservation(papers: Path, slug: str) -> dict[str, Any] | None:
    marker = _reservation_path(papers, slug)
    if not marker.exists():
        return None
    try:
        contents = marker.read_text(encoding="utf-8")
    except OSError as exc:
        raise CorpusStoreError(f"{slug} reservation is inaccessible",
                               code="filesystem-error") from exc
    try:
        value = json.loads(contents)
    except json.JSONDecodeError as exc:
        raise CorpusStoreError(f"{slug} reservation is corrupt") from exc
    if not isinstance(value, dict) or not isinstance(value.get("token"), str):
        raise CorpusStoreError(f"{slug} reservation is corrupt")
    return value


def slug_is_reserved(papers_dir: str | Path, slug: str) -> bool:
    """Fail closed for a pending reservation, including a damaged marker."""
    papers = _papers_dir(papers_dir)
    try:
        return _read_reservation(papers, slug) is not None
    except CorpusStoreError:
        return True


def _write_reservation(papers: Path, slug: str, token: str, identity: dict[str, Any]) -> None:
    directory = _slug_dir(papers, slug)
    directory.mkdir(parents=True, exist_ok=True)
    marker = _reservation_path(papers, slug)
    if marker.exists():
        raise CorpusStoreBusyError(f"{slug} is already reserved")
    # This is a local ownership credential, not publishable corpus content.
    fd = os.open(marker, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    try:
        os.write(fd, json.dumps({"token": token, "identity": identity}, ensure_ascii=False).encode("utf-8"))
    finally:
        os.close(fd)


def reserve(papers_dir: str | Path, identity: dict[str, Any], requested_slug: str | None = None) -> dict[str, Any]:
    if not isinstance(identity, dict) or not any(str(identity.get(k) or "").strip() for k in ("key", "doi", "title")):
        raise CorpusStoreError("identity requires key, doi, or title")
    papers = _papers_dir(papers_dir)
    with corpus_operation_lock(papers):
        with corpus_index_lock(papers):
            entries = load_index_strict(papers)
            existing = next((entry for entry in entries if _identity_match(entry, identity)), None)
            if existing is not None and not _identity_consistent(existing, identity):
                raise CorpusStoreError("existing index identity conflicts with reservation",
                                       code="identity-conflict")
            slug = _safe_slug(existing["slug"]) if existing and existing.get("slug") else ""
            if not slug:
                indexed_slugs = {entry.get("slug") for entry in entries}
                for directory in papers.iterdir():
                    if (not directory.is_dir() or directory.is_symlink()
                            or not _is_safe_slug(directory.name)):
                        continue
                    pending = _read_reservation(papers, directory.name)
                    if pending and _identity_match(pending.get("identity", {}), identity):
                        slug = directory.name
                        break
                    # A prior review may have published successfully while its
                    # index registration failed. Recover that bundle instead
                    # of allocating a new slug and paying for the same review.
                    if directory.name not in indexed_slugs and _complete_bundle(directory):
                        try:
                            sidecar = json.loads((directory / "bibliography.json").read_text(encoding="utf-8"))
                        except (OSError, ValueError):
                            continue
                        record = sidecar.get("zotero") if isinstance(sidecar, dict) else None
                        if (isinstance(sidecar, dict)
                                and sidecar.get("schema") == "bibliography-sidecar-1"
                                and isinstance(record, dict)
                                and _identity_consistent(record, identity)):
                            slug = directory.name
                            break
            slugs = _all_slugs(papers, entries)
            if not slug:
                if requested_slug:
                    requested_slug = _safe_slug(requested_slug)
                    if requested_slug in slugs:
                        raise CorpusStoreBusyError("requested_slug already exists")
                    slug = requested_slug
                else:
                    slug = _new_slug(identity, slugs)
            if _read_reservation(papers, slug) is not None:
                raise CorpusStoreBusyError(f"{slug} is already reserved")
            token = secrets.token_urlsafe(32)
            _write_reservation(papers, slug, token, identity)
            return {"slug": slug, "token": token, "existing": bool(existing)}


def _owned_reservation(papers: Path, slug: str, token: str) -> Path:
    slug = _safe_slug(slug)
    if not isinstance(token, str) or not token:
        raise CorpusStoreError("slug and token are required")
    marker = _reservation_path(papers, slug)
    reservation = _read_reservation(papers, slug)
    if reservation is None or not secrets.compare_digest(reservation["token"], token):
        raise CorpusStoreError("reservation ownership mismatch")
    return marker


def _complete_bundle(directory: Path) -> bool:
    return all((directory / name).is_file() and (directory / name).stat().st_size > 0
               for name in ("text.md", "review.md", "index.html", "bibliography.json"))


def register(papers_dir: str | Path, slug: str, token: str, entry: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(entry, dict):
        raise CorpusStoreError("entry must be an object")
    papers = _papers_dir(papers_dir)
    with corpus_index_lock(papers):
        marker = _owned_reservation(papers, slug, token)
        reservation = _read_reservation(papers, slug)
        assert reservation is not None
        identity = reservation.get("identity")
        if not isinstance(identity, dict) or not _identity_consistent(entry, identity):
            raise CorpusStoreError("entry identity does not match reservation")
        directory = _slug_dir(papers, slug)
        if not _complete_bundle(directory):
            raise CorpusStoreError("completed paper bundle is required before register")
        try:
            contents = (directory / "bibliography.json").read_text(encoding="utf-8")
        except OSError as exc:
            raise CorpusStoreError("bibliography sidecar is inaccessible",
                                   code="filesystem-error") from exc
        try:
            sidecar = json.loads(contents)
            zotero = sidecar.get("zotero") if isinstance(sidecar, dict) else None
        except json.JSONDecodeError as exc:
            raise CorpusStoreError("bibliography sidecar is invalid") from exc
        if not isinstance(zotero, dict) or not _identity_consistent(zotero, identity):
            raise CorpusStoreError("bibliography sidecar identity does not match reservation")
        entries = load_index_strict(papers)
        previous = next((candidate for candidate in entries if candidate.get("slug") == slug), {})
        merged = dict(entry)
        merged["slug"] = slug
        if not merged.get("classifications") and previous.get("classifications"):
            merged["classifications"] = previous["classifications"]
        else:
            merged.setdefault("classifications", {})
        if previous.get("tags"):
            fresh_tags = merged.get("tags") or []
            if not isinstance(fresh_tags, list):
                raise CorpusStoreError("entry tags must be a list")
            merged["tags"] = list(dict.fromkeys([*previous["tags"], *fresh_tags]))
        # Corpus-only metadata remains authoritative when a local review registers.
        for key, value in previous.items():
            if key not in IDENTITY_FIELDS or key == "slug":
                if key == "connections" and not merged.get(key):
                    merged[key] = value
                else:
                    merged.setdefault(key, value)
        if "key" in merged and "zotero_item_key" not in merged:
            merged["zotero_item_key"] = merged["key"]
        replacement = [candidate for candidate in entries if candidate.get("slug") != slug]
        replacement.append(merged)
        atomic_write_json(index_path(papers), replacement)
        marker.unlink()
        return {"slug": slug, "registered": True}


def cancel(papers_dir: str | Path, slug: str, token: str) -> dict[str, Any]:
    papers = _papers_dir(papers_dir)
    with corpus_index_lock(papers):
        marker = _owned_reservation(papers, slug, token)
        marker.unlink()
        directory = _slug_dir(papers, slug)
        # Never delete anything except the empty directory we created.
        if directory.is_dir() and not any(directory.iterdir()):
            directory.rmdir()
        return {"slug": slug, "cancelled": True}


def handle_request(request: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(request, dict) or request.get("schema_version") != 1:
        raise CorpusStoreError("schema_version must be 1")
    op = request.get("op")
    papers_dir = request.get("papers_dir")
    if not isinstance(papers_dir, str) or not papers_dir:
        raise CorpusStoreError("papers_dir is required")
    if op == "reserve":
        return reserve(papers_dir, request.get("identity"), request.get("requested_slug"))
    if op == "register":
        return register(papers_dir, request.get("slug"), request.get("token"), request.get("entry"))
    if op == "cancel":
        return cancel(papers_dir, request.get("slug"), request.get("token"))
    raise CorpusStoreError("op must be reserve, register, or cancel")


def main() -> int:
    parser = argparse.ArgumentParser(description="Transactional paper corpus store")
    parser.add_argument("--request", required=True, help="JSON request file")
    args = parser.parse_args()
    op = None
    try:
        request = json.loads(Path(args.request).read_text(encoding="utf-8"))
        op = request.get("op") if isinstance(request, dict) else None
        result = handle_request(request)
        print(json.dumps({"schema_version": 1, "op": op, "status": "completed",
                          **result}, ensure_ascii=False))
        return 0
    except CorpusStoreBusyError:
        print(json.dumps({"schema_version": 1, "op": op, "status": "busy",
                          "error": "corpus operation is busy", "error_code": "busy"}, ensure_ascii=False))
        return 1
    except CorpusStoreError as exc:
        print(json.dumps({"schema_version": 1, "op": op, "status": "failed",
                          "error": "invalid corpus request", "error_code": exc.code}, ensure_ascii=False))
        return 1
    except OSError:
        print(json.dumps({"schema_version": 1, "op": op, "status": "failed",
                          "error": "invalid corpus request", "error_code": "filesystem-error"},
                         ensure_ascii=False))
        return 1
    except json.JSONDecodeError:
        print(json.dumps({"schema_version": 1, "op": op, "status": "failed",
                          "error": "invalid corpus request", "error_code": "invalid-request"},
                         ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
