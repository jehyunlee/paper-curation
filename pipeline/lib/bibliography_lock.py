"""Cross-process lock for the canonical bibliography SQLite file.

Split out of ``lib/affiliation_registry.py`` when the affiliation organisation
registry was retired. The lock has nothing to do with that registry — it is what
keeps two review-generation jobs from writing the DB at once — so it outlives it.
"""
from __future__ import annotations

import errno
import fcntl
import os
import threading
import time
from contextlib import contextmanager
from pathlib import Path


class BibliographyWriterLockBusyError(RuntimeError):
    """Another process owns the bibliography database writer boundary."""

    def __init__(self, message: str, *, reason: str):
        super().__init__(message)
        self.reason = reason

def bibliography_writer_lock_path(database: Path) -> Path:
    """Return the stable inode shared by every bibliography reader and writer."""
    return database.with_suffix(database.suffix + ".flock")


_LOCK_STATE: dict[int, str] = {}
_LOCK_STATE_GUARD = threading.Lock()


def _held_bibliography_locks() -> dict[int, str]:
    return _LOCK_STATE


def _acquire_bibliography_lock(database: Path, mode: str, *, timeout: float) -> int:
    """Acquire a process-death-releasing shared or exclusive POSIX advisory lock."""
    if mode not in {"reader", "writer"}:
        raise ValueError("bibliography lock mode must be reader or writer")
    path = bibliography_writer_lock_path(database)
    path.parent.mkdir(parents=True, exist_ok=True)
    key = str(path.resolve())
    held = _held_bibliography_locks()
    with _LOCK_STATE_GUARD:
        nested = key in held.values()
    if nested:
        message = f"bibliography {mode} lock busy: nested acquisition is forbidden"
        if mode == "writer":
            raise BibliographyWriterLockBusyError(message, reason="nested")
        raise RuntimeError(message)
    descriptor = os.open(path, os.O_CREAT | os.O_RDWR, 0o600)
    os.set_inheritable(descriptor, False)
    os.chmod(path, 0o600)
    operation = fcntl.LOCK_SH if mode == "reader" else fcntl.LOCK_EX
    deadline = time.monotonic() + timeout
    try:
        while True:
            try:
                fcntl.flock(descriptor, operation | fcntl.LOCK_NB)
                break
            except BlockingIOError as exc:
                if time.monotonic() >= deadline:
                    message = f"bibliography {mode} lock busy"
                    if mode == "writer":
                        raise BibliographyWriterLockBusyError(
                            message, reason="timeout") from exc
                    raise RuntimeError(message) from exc
                time.sleep(0.25)
        with _LOCK_STATE_GUARD:
            if key in held.values():
                fcntl.flock(descriptor, fcntl.LOCK_UN)
                message = f"bibliography {mode} lock busy: nested acquisition is forbidden"
                if mode == "writer":
                    raise BibliographyWriterLockBusyError(
                        message, reason="nested")
                raise RuntimeError(message)
            held[descriptor] = key
        return descriptor
    except BaseException:
        os.close(descriptor)
        raise


def acquire_bibliography_writer_lock(database: Path, *, timeout: float = 120.0) -> int:
    """Acquire exclusive writer ownership without using pathname existence as authority."""
    return _acquire_bibliography_lock(database, "writer", timeout=timeout)


def acquire_bibliography_reader_lock(database: Path, *, timeout: float = 30.0) -> int:
    """Acquire shared reader ownership on the same stable inode as writers."""
    return _acquire_bibliography_lock(database, "reader", timeout=timeout)


def release_bibliography_lock(database: Path, descriptor: int) -> None:
    """Release a kernel-held bibliography lock; the stable pathname is never removed."""
    expected = str(bibliography_writer_lock_path(database).resolve())
    held = _held_bibliography_locks()
    with _LOCK_STATE_GUARD:
        owned = held.get(descriptor) == expected
    if not owned:
        raise RuntimeError("bibliography lock descriptor is not owned by this operation")
    try:
        fcntl.flock(descriptor, fcntl.LOCK_UN)
    finally:
        with _LOCK_STATE_GUARD:
            held.pop(descriptor, None)
        os.close(descriptor)


def release_bibliography_writer_lock(database: Path, descriptor: int) -> None:
    """Release a writer lock while preserving its stable inode."""
    release_bibliography_lock(database, descriptor)


def release_bibliography_reader_lock(database: Path, descriptor: int) -> None:
    """Release a reader lock while preserving its stable inode."""
    release_bibliography_lock(database, descriptor)


@contextmanager
def bibliography_lock(database: Path, mode: str, *, timeout: float | None = None):
    """Context manager for the one shared reader/writer coordination boundary."""
    if timeout is None:
        timeout = 30.0 if mode == "reader" else 120.0
    descriptor = _acquire_bibliography_lock(database, mode, timeout=timeout)
    try:
        yield descriptor
    finally:
        release_bibliography_lock(database, descriptor)


@contextmanager
def bibliography_reader_lock(database: Path):
    with bibliography_lock(database, "reader") as descriptor:
        yield descriptor


@contextmanager
def bibliography_writer_lock(database: Path):
    with bibliography_lock(database, "writer") as descriptor:
        yield descriptor
