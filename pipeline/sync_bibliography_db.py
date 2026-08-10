#!/usr/bin/env python3
"""CAS synchronize immutable bibliography DB generations over SSH.

A generation is identified by its content digests, its SQL contract, the Git
revision and the builder blobs that produced it, and the authority lease that
owns the write.

It used to be identified by the affiliation registry as well — `registry_sha256`,
`event_head`, `ledger_head`, `policy_version`, the contract versions, the
evidence oracle, the cohort and an immutable migration receipt. That registry was
retired, so those artifacts no longer exist and roughly 620 lines of machinery
that carried them (migration receipts, origin-transition checks, legacy recovery,
published rollback, the strict-affiliation artifact set) went with it. What
remains verifies the database rather than a contract row.

A base receipt written before that boundary pins `pipeline/affiliation_registry*`
blobs that are gone. Such a receipt is accepted — see `_validate_git_blobs` — so
that a host holding a pre-retirement generation can still pull and move forward.

The contract is pinned by `pipeline/tests/test_bibliography_sync_contract.py`.
"""
from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import os
import shlex
import socket
import sqlite3
import shutil
import subprocess
import tempfile
import time
import uuid
import sys
import unicodedata
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from threading import Event, Thread
import build_bibliography_db as bibliography
from lib import db_digest as migrator
# Aliased: this module defines wrapper functions with the same names,
# which would otherwise shadow the module they delegate to.
from lib import bibliography_lock as _locks

ROOT = Path(__file__).resolve().parents[1]
LOCAL_DB = ROOT / ".cache/bibliography.sqlite3"
HOST = os.environ.get("PAPER_CURATION_DB_HOST", "macmini-cf")
REMOTE_DB = os.environ.get("PAPER_CURATION_DB_REMOTE",
                           "/Users/jehyunlee/Documents/paper-curation/.cache/bibliography.sqlite3")
MANIFEST = REMOTE_DB + ".manifest.json"
LOCK = REMOTE_DB + ".publish.lock"  # Compatibility name; never ownership.
CONTROL_LOCK = REMOTE_DB + ".publish.control.lock"
FENCE = REMOTE_DB + ".publish.fence"
LEASE = REMOTE_DB + ".publish.lease.json"
AUTHORITY_RPC = None  # Explicit test-only authority helper injection.
GENERATIONS = REMOTE_DB + ".generations"
LEASE_PROTOCOL_VERSION = "bibliography-lease-flock-v1"
LEASE_TTL_SECONDS = 90
LEASE_HEARTBEAT_SECONDS = 20
LEASE_ACQUIRE_TIMEOUT_SECONDS = 120
LEASE_POLL_SECONDS = 2
AUTHORITY_RPC_TIMEOUT_SECONDS = 10
LEASE_COMMIT_MINIMUM_SECONDS = 30
LOCAL_READER_TIMEOUT_SECONDS = 30
LOCAL_WRITER_TIMEOUT_SECONDS = 120
AFFILIATION_ARTIFACT_ROLES = (
    "cohort", "decisions", "ledger", "generation_descriptor",
)
_AFFILIATION_ARTIFACT_SUFFIXES = {
    "cohort": "cohort.json",
    "decisions": "decisions.json",
    "ledger": "ledger.jsonl",
    "generation_descriptor": "generation.json",
}


def bibliography_writer_lock_path(database: Path = LOCAL_DB) -> Path:
    """Return the shared stable lock inode used by every bibliography operation."""
    return _locks.bibliography_writer_lock_path(database)


@contextmanager
def bibliography_lock(database: Path, mode: str, *, timeout: float):
    """Delegate to the single registry-owned advisory-lock implementation."""
    with _locks.bibliography_lock(
            database, mode, timeout=timeout) as descriptor:
        yield descriptor


@contextmanager
def bibliography_reader_lock(database: Path = LOCAL_DB):
    with bibliography_lock(
            database, "reader", timeout=LOCAL_READER_TIMEOUT_SECONDS) as descriptor:
        yield descriptor


@contextmanager
def bibliography_writer_lock(database: Path = LOCAL_DB):
    with bibliography_lock(
            database, "writer", timeout=LOCAL_WRITER_TIMEOUT_SECONDS) as descriptor:
        yield descriptor


def run(cmd, *, capture=False, timeout=None):
    return subprocess.run(cmd, check=True, text=True, capture_output=capture,
                          timeout=timeout)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _authority_is_local() -> bool:
    remote_db = Path(REMOTE_DB).expanduser()
    try:
        return remote_db.exists() and remote_db.resolve() == LOCAL_DB.resolve()
    except OSError:
        return False


def remote(command, capture=False):
    if _authority_is_local():
        return run(["/bin/sh", "-c", command], capture=capture,
                   timeout=AUTHORITY_RPC_TIMEOUT_SECONDS)
    return run(["ssh", "-o", f"ConnectTimeout={AUTHORITY_RPC_TIMEOUT_SECONDS}",
                HOST, command], capture=capture, timeout=AUTHORITY_RPC_TIMEOUT_SECONDS)
_AUTHORITY_PROGRAM = r'''
import fcntl, hashlib, json, os, plistlib, subprocess, sys, time
control, fence_path, lease_path, action, owner_json = sys.argv[1:6]
owner = json.loads(owner_json)
def durable(path, value):
    temporary = path + ".tmp." + str(os.getpid())
    with open(temporary, "w", encoding="utf-8") as handle:
        handle.write(json.dumps(value, sort_keys=True, separators=(",", ":")))
        handle.flush(); os.fsync(handle.fileno())
    os.replace(temporary, path)
    directory = os.open(os.path.dirname(path) or ".", os.O_RDONLY)
    try: os.fsync(directory)
    finally: os.close(directory)
def boot_id():
    try:
        boot = subprocess.check_output(["sysctl", "-n", "kern.boottime"], text=True).strip()
    except Exception:
        boot = str(os.stat("/").st_ctime_ns)
    return hashlib.sha256((os.uname().nodename + "\0" + boot).encode()).hexdigest()
def load(path):
    try:
        with open(path, encoding="utf-8") as handle: return json.load(handle)
    except FileNotFoundError: return None
def filesystem_type(path):
    if sys.platform == "darwin":
        rows = subprocess.check_output(["df", "-P", path], text=True).splitlines()
        device = rows[-1].split()[0]
        info = plistlib.loads(subprocess.check_output(
            ["diskutil", "info", "-plist", device]))
        return str(info.get("FilesystemType", "")).lower()
    return subprocess.check_output(
        ["stat", "-f", "-c", "%T", path], text=True).strip().lower()
if action == "acquire":
    try:
        filesystem = filesystem_type(os.path.dirname(control) or ".")
    except Exception:
        raise SystemExit(74)
    if filesystem != "apfs":
        print(json.dumps({"status":"unpublishable"})); raise SystemExit(74)
with open(control, "a+", encoding="utf-8") as control_handle:
    os.chmod(control, 0o600)
    fcntl.flock(control_handle.fileno(), fcntl.LOCK_EX)
    now, boot = time.monotonic_ns(), boot_id()
    current = load(lease_path)
    exact = current and all(current.get(key) == owner.get(key) for key in
        ("owner_run_id", "owner_writer_uuid", "owner_client_host_uuid", "fence_token"))
    live = current and current.get("authority_boot_id") == boot and now < current.get("expires_monotonic_ns", 0)
    if action == "acquire":
        if live:
            print(json.dumps({"status":"busy"})); raise SystemExit(75)
        try:
            with open(fence_path, encoding="ascii") as handle: fence = int(json.load(handle))
        except FileNotFoundError: fence = 0
        if not 0 <= fence < (1 << 64) - 1:
            print(json.dumps({"status":"fenced"})); raise SystemExit(74)
        fence += 1
        durable(fence_path, str(fence))
        result = {**owner, "authority_host_uuid": hashlib.sha256(os.uname().nodename.encode()).hexdigest(),
                  "authority_boot_id": boot, "fence_token": fence, "issued_monotonic_ns": now,
                  "expires_monotonic_ns": now + 90 * 1_000_000_000, "ttl_seconds":90,
                  "lease_protocol": "bibliography-lease-flock-v1"}
        durable(lease_path, result); print(json.dumps({"status":"ok","lease":result}))
    elif action == "renew":
        if not live or not exact:
            print(json.dumps({"status":"fenced"})); raise SystemExit(74)
        current["expires_monotonic_ns"] = now + 90 * 1_000_000_000
        durable(lease_path, current); print(json.dumps({"status":"ok","lease":current}))
    elif action == "release":
        if exact:
            os.unlink(lease_path)
            directory = os.open(os.path.dirname(lease_path) or ".", os.O_RDONLY)
            try: os.fsync(directory)
            finally: os.close(directory)
        print(json.dumps({"status":"ok"}))
'''


def _lease_owner() -> dict:
    return {
        "owner_run_id": os.urandom(16).hex(),
        "owner_writer_uuid": os.urandom(16).hex(),
        "owner_client_host_uuid": hashlib.sha256(socket.gethostname().encode()).hexdigest(),
    }


def _authority_paths() -> tuple[str, str, str]:
    """Derive authority artifacts from the active remote DB for local test authorities."""
    return (
        REMOTE_DB + ".publish.control.lock",
        REMOTE_DB + ".publish.fence",
        REMOTE_DB + ".publish.lease.json",
    )

def _authority_rpc(action: str, owner: dict) -> dict:
    if AUTHORITY_RPC is not None:
        return AUTHORITY_RPC(action, owner)
    control_lock, fence, lease = _authority_paths()
    command = (
        f"python3 -c {_remote_q(_AUTHORITY_PROGRAM)} {_remote_q(control_lock)} "
        f"{_remote_q(fence)} {_remote_q(lease)} {_remote_q(action)} "
        f"{_remote_q(canonical_manifest(owner))}"
    )
    try:
        result = remote(command, capture=True)
    except subprocess.CalledProcessError as exc:
        if exc.returncode == 75:
            return {"status": "busy"}
        if exc.returncode == 74:
            return {"status": "fenced"}
        raise RuntimeError("authority lease helper failed") from exc
    try:
        return json.loads(result.stdout)
    except (AttributeError, TypeError, json.JSONDecodeError) as exc:
        raise RuntimeError("authority lease helper returned invalid JSON") from exc


@contextmanager
def authority_lease():
    """Acquire remote monotonic lease before any local exclusive lock."""
    owner, deadline = _lease_owner(), time.monotonic() + LEASE_ACQUIRE_TIMEOUT_SECONDS
    while True:
        response = _authority_rpc("acquire", owner)
        if response.get("status") == "ok":
            lease = response.get("lease")
            required = (
                "authority_host_uuid", "authority_boot_id", "fence_token",
                "owner_run_id", "owner_writer_uuid", "owner_client_host_uuid",
            )
            if (not isinstance(lease, dict)
                    or any(lease.get(key) in (None, "") for key in required)
                    or any(lease[key] != owner[key] for key in (
                        "owner_run_id", "owner_writer_uuid", "owner_client_host_uuid"))
                    or not isinstance(lease["fence_token"], int)
                    or lease["fence_token"] <= 0):
                raise RuntimeError("authority lease response is invalid")
            owner["fence_token"] = lease["fence_token"]
            owner["authority_host_uuid"] = lease["authority_host_uuid"]
            owner["authority_boot_id"] = lease["authority_boot_id"]
            break
        if response.get("status") not in {"busy", "fenced"}:
            raise RuntimeError("authority lease helper returned invalid JSON")
        if time.monotonic() >= deadline:
            raise RuntimeError("authority lease busy")
        time.sleep(LEASE_POLL_SECONDS)
    stopped, fenced = Event(), Event()

    def heartbeat():
        while not stopped.wait(LEASE_HEARTBEAT_SECONDS):
            try:
                response = _authority_rpc("renew", owner)
                lease = response.get("lease")
            except BaseException:
                fenced.set()
                return
            if (response.get("status") != "ok" or not isinstance(lease, dict)
                    or any(lease.get(key) != owner.get(key) for key in (
                        "authority_boot_id", "owner_run_id", "owner_writer_uuid",
                        "owner_client_host_uuid", "fence_token"))):
                fenced.set()
                return

    worker = Thread(target=heartbeat, name="bibliography-authority-heartbeat",
                    daemon=True)
    worker.start()
    try:
        yield {**owner, "lease_protocol": LEASE_PROTOCOL_VERSION,
               "ttl_seconds": LEASE_TTL_SECONDS,
               "heartbeat_seconds": LEASE_HEARTBEAT_SECONDS,
               "_fenced": fenced}
    finally:
        stopped.set()
        worker.join(timeout=LEASE_HEARTBEAT_SECONDS + 1)
        try:
            _authority_rpc("release", owner)
        except BaseException:
            fenced.set()


def _authority_commit(command: str, owner: dict) -> None:
    """Run a short fenced authority-side commit while its control flock is held."""
    if owner.get("_fenced") and owner["_fenced"].is_set():
        raise RuntimeError("authority lease renewal fenced this operation")
    if AUTHORITY_RPC is not None:
        response = AUTHORITY_RPC("commit", owner)
        if response.get("status") != "ok":
            raise RuntimeError("authority lease was fenced before commit")
        remote(command)
        return
    guard = r'''import fcntl,hashlib,json,os,subprocess,sys,time
control,lease_path,owner_json,command=sys.argv[1:5]
owner=json.loads(owner_json)
try: boot_time=subprocess.check_output(["sysctl","-n","kern.boottime"],text=True).strip()
except Exception: boot_time=str(os.stat("/").st_ctime_ns)
boot=hashlib.sha256((os.uname().nodename+"\0"+boot_time).encode()).hexdigest()
with open(control,"a+",encoding="utf-8") as handle:
 os.chmod(control,0o600); fcntl.flock(handle.fileno(),fcntl.LOCK_EX)
 try: lease=json.load(open(lease_path,encoding="utf-8"))
 except FileNotFoundError: raise SystemExit(74)
 exact=all(lease.get(k)==owner.get(k) for k in ("authority_boot_id","owner_run_id","owner_writer_uuid","owner_client_host_uuid","fence_token"))
 if lease.get("authority_boot_id") != boot or not exact or time.monotonic_ns() >= lease.get("expires_monotonic_ns",0): raise SystemExit(74)
 if lease["expires_monotonic_ns"]-time.monotonic_ns() < 30*1000000000: raise SystemExit(74)
 raise SystemExit(os.system(command) >> 8)'''
    owner_payload = {key: value for key, value in owner.items()
                     if not key.startswith("_") and key not in
                     {"lease_protocol", "ttl_seconds", "heartbeat_seconds"}}
    wrapped = (
        f"python3 -c {_remote_q(guard)} {_remote_q(_authority_paths()[0])} {_remote_q(_authority_paths()[2])} "
        f"{_remote_q(canonical_manifest(owner_payload))} {_remote_q(command)}"
    )
    remote(wrapped)


def _copy_from_authority(source: str, destination: Path) -> None:
    if _authority_is_local():
        shutil.copyfile(Path(source), destination)
        return
    run(["scp", "-q", HOST + ":" + source, str(destination)])


def _copy_to_authority(source: Path, destination: str) -> None:
    if _authority_is_local():
        shutil.copyfile(source, Path(destination))
        return
    run(["scp", "-q", str(source), HOST + ":" + destination])


def canonical_manifest(manifest: dict) -> str:
    return json.dumps(manifest, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _fresh_schema_receipt_path() -> Path:
    return migrator.receipt_path(LOCAL_DB, "fresh-schema")


def _local_affiliation_metadata() -> dict:
    return _inspect_sqlite(LOCAL_DB, require_affiliation=False)


def _required_manifest_fields(*, rollback: bool = False) -> set[str]:
    fields = {
        "database", "generation", "sha256", "logical_sha256", "schema_version",
        # The affiliation registry supplied registry_sha256, event_head,
        # policy_version, the contract versions, the evidence oracle, the
        # cohort and the migration receipt. It was retired, so a manifest can
        # no longer carry them and requiring them blocks every publish. What
        # remains is what still identifies a build: content digests, the SQL
        # contract, the Git revision and the lease.
        "source_sha256", "sql_contract_sha256",
        "strict_result_sha256", "git_revision", "git_blobs",
        "generation_provenance", "updated_at", "object",
        "lease_protocol", "fence_token", "authority_host_uuid",
        "authority_boot_id", "owner_run_id", "owner_writer_uuid",
        "owner_client_host_uuid",
    }
    if rollback:
        fields |= {
            "base_generation", "base_sha256", "base_logical_sha256",
            "restored_schema_version", "requires_controlled_remigration",
        }
    return fields


# Code that defines how the DB is produced. Pinning these blobs makes a
# published generation traceable to the exact builder that made it; the retired
# registry's JSON payloads used to sit here too.
_GIT_TARGETS = (
    "pipeline/build_bibliography_db.py",
    "pipeline/check_bibliography_db.py",
    "pipeline/data/dict_afgroupname_confident.json",
)


def _git_provenance(
        root: Path = ROOT,
        targets: tuple[str, ...] = _GIT_TARGETS) -> dict:
    revision = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "HEAD"], check=True, text=True,
        capture_output=True).stdout.strip()
    dirty = subprocess.run(
        ["git", "-C", str(root), "diff", "--quiet", revision, "--", *targets],
        check=False, text=True, capture_output=True)
    if dirty.returncode:
        raise RuntimeError("target publication artifacts differ from HEAD")
    blobs = {}
    for target in targets:
        blob = subprocess.run(
            ["git", "-C", str(root), "rev-parse", f"{revision}:{target}"],
            check=True, text=True, capture_output=True).stdout.strip()
        working_blob = subprocess.run(
            ["git", "-C", str(root), "hash-object", "--", target],
            check=True, text=True, capture_output=True).stdout.strip()
        if working_blob != blob:
            raise RuntimeError(
                f"target publication artifact bytes differ from HEAD: {target}")
        blobs[target] = blob
    return {"git_revision": revision, "git_blobs": blobs}


def _sql_contract_sha256(path: Path) -> str:
    connection = sqlite3.connect(path)
    try:
        schema = connection.execute(
            "SELECT type,name,tbl_name,sql FROM sqlite_master "
            "WHERE sql IS NOT NULL ORDER BY type,name").fetchall()
    finally:
        connection.close()
    return hashlib.sha256(canonical_manifest(schema).encode()).hexdigest()


def _strict_result_sha256(metadata: dict) -> str:
    return hashlib.sha256(canonical_manifest(metadata).encode()).hexdigest()

def _generation_provenance(metadata: dict, git_revision: str) -> dict:
    """Bind the same Git revision and registry/event/ledger heads as the manifest."""
    return {
        "git_revision": git_revision,
        "source_sha256": metadata.get("source_sha256", ""),
        "logical_sha256": metadata.get("logical_sha256", ""),
    }
def _validate_git_blobs(manifest: dict) -> None:
    """The pinned builder blobs must be the ones this version pins.

    A manifest written before the affiliation registry was retired pins
    `pipeline/affiliation_registry*.json`, files that no longer exist. Such a
    receipt cannot satisfy the current target set, and it is not corrupt
    either — it is from the other side of that boundary. The blob check is
    skipped for it while every other field is still enforced; a receipt pinning
    some other unexpected set is still an error.
    """
    blobs = manifest.get("git_blobs")
    if not isinstance(blobs, dict) or not all(
            isinstance(blob, str) and blob for blob in blobs.values()):
        raise RuntimeError("manifest Git blob provenance is invalid")
    if set(blobs) == set(_GIT_TARGETS):
        return
    if blobs and all("affiliation_registry" in target for target in blobs):
        print("[sync] base receipt predates the affiliation registry "
              "retirement; its pinned blobs are no longer targets",
              file=sys.stderr, flush=True)
        return
    raise RuntimeError("manifest Git blob provenance is invalid")


def _validate_manifest(manifest: dict, *, rollback: bool = False,
                       allow_legacy: bool = False) -> None:
    if not isinstance(manifest, dict):
        raise RuntimeError("manifest is invalid")
    core_fields = {
        "database", "generation", "sha256", "logical_sha256", "schema_version",
        "source_sha256", "updated_at", "object",
    }
    core_missing = sorted(
        key for key in core_fields if manifest.get(key) in (None, ""))
    if core_missing:
        raise RuntimeError(
            "manifest lacks required provenance: " + ",".join(core_missing))
    if not isinstance(manifest["generation"], int) or manifest["generation"] < 0:
        raise RuntimeError("manifest generation is invalid")
    if manifest["object"] != (
            f"{GENERATIONS}/{manifest['generation']:020d}-{manifest['logical_sha256']}.sqlite3"):
        raise RuntimeError("manifest immutable object name mismatch")
    # The immutable migration receipt was the affiliation registry's, and it
    # was retired with it; a manifest no longer names one.
    legacy = allow_legacy and manifest.get("schema_version") == "affiliation-2"
    missing = sorted(key for key in _required_manifest_fields(rollback=rollback)
                     if manifest.get(key) in (None, ""))
    if missing and not legacy:
        raise RuntimeError("manifest lacks required provenance: " + ",".join(missing))
    if legacy:
        return
    _validate_git_blobs(manifest)
    if manifest["lease_protocol"] != LEASE_PROTOCOL_VERSION:
        raise RuntimeError("manifest lease protocol is invalid")
    if (not isinstance(manifest["fence_token"], int)
            or not 0 < manifest["fence_token"] < (1 << 64)):
        raise RuntimeError("manifest fence token is invalid")
    _validate_generation_provenance(manifest)


def _validate_generation_provenance(manifest: dict) -> None:
    """Provenance must bind the manifest's own Git revision.

    Post-registry this is the whole check: the registry digest, event head and
    ledger head it also used to pin no longer exist. Kept as its own function so
    the contract is testable without acquiring a lease.
    """
    provenance = manifest.get("generation_provenance")
    if provenance is None:
        return
    if not isinstance(provenance, dict):
        raise RuntimeError("manifest generation provenance is invalid")
    if provenance.get("git_revision") != manifest["git_revision"]:
        raise RuntimeError("manifest generation provenance is invalid")


def _inspect_sqlite(path: Path, *, require_affiliation: bool = False) -> dict:
    """Identity of a database file, read from the file itself.

    This used to read the affiliation registry's metadata singleton — schema
    version, registry digest, event head, policy version, migration receipt and
    the rest. That registry was retired, so identity now comes from what the
    file still is: its layout and its content.
    """
    del require_affiliation          # retired along with the registry
    connection = sqlite3.connect(path)
    try:
        if connection.execute("PRAGMA quick_check").fetchone()[0] != "ok":
            raise RuntimeError(f"SQLite integrity check failed: {path}")
        return {"schema_version": migrator.schema_name(connection),
                "source_sha256": migrator.logical_digest(connection)}
    finally:
        connection.close()


def _remote_bootstrap_metadata() -> dict:
    # The remote probe used to assert the affiliation-3 registry contract row.
    # With the registry retired it reports only what still exists: integrity
    # and the logical content digest the CAS compare-and-swap comes down to.
    program = (
        "import json,sqlite3,sys;"
        "from pathlib import Path;"
        "sys.path.insert(0,str(Path(sys.argv[1]).parent.parent/'pipeline'));"
        "from lib import db_digest as m;"
        "c=sqlite3.connect(sys.argv[1]);"
        "ok=c.execute('PRAGMA quick_check').fetchone()[0];"
        "logical=m.logical_digest(c);schema=m.schema_name(c);c.close();"
        "assert ok=='ok';"
        "print(json.dumps({'schema_version':schema,'logical_sha256':logical},"
        "sort_keys=True,separators=(',',':')))"
    )
    try:
        payload = remote(
            f"python3 -c {_remote_q(program)} {_remote_q(REMOTE_DB)}",
            capture=True,
        ).stdout.strip()
        metadata = json.loads(payload)
    except (subprocess.CalledProcessError, json.JSONDecodeError) as exc:
        raise RuntimeError(
            "cannot bootstrap: remote DB failed affiliation-3 validation"
        ) from exc
    if metadata.get("schema_version") != bibliography.AFFILIATION_SCHEMA_VERSION or not all(
            metadata.get(key) for key in (
                "registry_sha256", "event_head", "policy_version",
                "source_sha256", "migration_receipt_id", "logical_sha256")):
        raise RuntimeError("cannot bootstrap: remote DB has invalid affiliation metadata")
    return metadata


def _remigration_marker() -> Path:
    return LOCAL_DB.with_suffix(LOCAL_DB.suffix + ".remigration-required.json")


def _ensure_publishable(
        held_writer_lock_descriptor: int | None = None) -> None:
    marker = _remigration_marker()
    if marker.exists():
        raise RuntimeError("remigration required before bibliography synchronization")
    if not LOCAL_DB.exists():
        raise RuntimeError(f"missing local DB: {LOCAL_DB}")
    # The affiliation registry was retired: there is no metadata singleton, no
    # registry digest and no migration receipt to assert any more. The
    # publication gate is now `check_bibliography_db.py --strict`, invoked just
    # below, which checks the data instead of a contract row.
    checker_path = ROOT / "pipeline" / "check_bibliography_db.py"
    checker_args = ["--db", str(LOCAL_DB), "--strict"]
    # Always a subprocess. The in-process branch existed because the checker
    # used to take the writer flock and would have deadlocked against a caller
    # already holding it; it now opens the DB read-only and takes no lock.
    del held_writer_lock_descriptor
    try:
        run([sys.executable, str(checker_path), *checker_args])
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(
            "strict bibliography validation failed; push blocked") from exc


def _ensure_pull_allowed(manifest: dict | None = None) -> None:
    marker = _remigration_marker()
    if not marker.exists():
        return
    if manifest is None:
        raise RuntimeError("remigration required before bibliography synchronization")
    try:
        blocked = json.loads(marker.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError("invalid remigration hard-stop marker") from exc
    if (manifest.get("requires_controlled_remigration")
            or manifest.get("generation", -1)
            <= blocked.get("manifest_generation", -1)):
        raise RuntimeError("remigration required before bibliography synchronization")


def _logical_sha(path: Path) -> str:
    connection = sqlite3.connect(path)
    try:
        return migrator.logical_digest(connection)
    finally:
        connection.close()


def local_manifest() -> dict:
    """Manifest describing the local DB: identity, contract, provenance."""
    metadata = _inspect_sqlite(LOCAL_DB)
    contracts = {
        "sql_contract_sha256": _sql_contract_sha256(LOCAL_DB),
        **_git_provenance(),
    }
    strict_metadata = {**metadata, **contracts}
    manifest = {
        "database": LOCAL_DB.name,
        "generation": 0,
        "sha256": sha(LOCAL_DB),
        "logical_sha256": _logical_sha(LOCAL_DB),
        "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        **metadata,
        **contracts,
        "strict_result_sha256": _strict_result_sha256(strict_metadata),
        "generation_provenance": _generation_provenance(
            metadata, contracts["git_revision"]),
    }
    return manifest
def _remote_q(value: str) -> str:
    return shlex.quote(value)


def _atomic_remote_json(path: str, payload: str) -> str:
    quoted_path, quoted_payload = _remote_q(path), _remote_q(payload)
    return (
        f"tmp={quoted_path}.$$.tmp; printf '%s' {quoted_payload} > \"$tmp\"; "
        "python3 -c 'import os,sys; f=open(sys.argv[1],\"rb\"); os.fsync(f.fileno()); f.close()' \"$tmp\"; "
        f"mv \"$tmp\" {quoted_path}; "
        f"python3 -c 'import os,sys; d=os.open(sys.argv[1],os.O_RDONLY); os.fsync(d); os.close(d)' "
        f"{_remote_q(str(Path(path).parent))}"
    )
def _remote_fsync(path: str) -> str:
    return (
        f"python3 -c 'import os,sys; f=open(sys.argv[1],\"rb\"); os.fsync(f.fileno()); "
        "f.close(); d=os.open(sys.argv[2],os.O_RDONLY); os.fsync(d); os.close(d); "
        "d=os.open(sys.argv[3],os.O_RDONLY); os.fsync(d); os.close(d)' "
        f"{_remote_q(path)} {_remote_q(str(Path(path).parent))} "
        f"{_remote_q(str(Path(path).parent.parent))}; "
    )


def _atomic_remote_copy(source: str, destination: str, token: str) -> str:
    temporary = f"{destination}.current.{token}"
    return (
        f"cp {_remote_q(source)} {_remote_q(temporary)}; "
        + _remote_fsync(temporary)
        + f"mv {_remote_q(temporary)} {_remote_q(destination)}; "
        + _remote_fsync(destination)
    )


def _ensure_installable_pull(manifest: dict) -> None:
    """Revalidate local hard stops and prevent generation regression."""
    _ensure_pull_allowed(manifest)
    base = LOCAL_DB.with_suffix(".base.json")
    if not base.exists():
        return
    try:
        raw = base.read_text(encoding="utf-8")
        installed = json.loads(raw)
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError("invalid installed base receipt") from exc
    if raw != canonical_manifest(installed):
        raise RuntimeError("installed base receipt is not canonical")
    installed_generation = installed.get("generation")
    remote_generation = manifest.get("generation")
    if (not isinstance(installed_generation, int)
            or not isinstance(remote_generation, int)):
        raise RuntimeError("installed or remote generation is invalid")
    if installed_generation > remote_generation:
        raise RuntimeError("remote manifest would regress the installed generation")
    if (installed_generation == remote_generation
            and canonical_manifest(installed) != canonical_manifest(manifest)):
        raise RuntimeError("remote manifest conflicts with the installed generation")


def bootstrap():
    """Legacy bootstrap is intentionally forbidden without receipt recovery."""
    raise RuntimeError(
        "cannot bootstrap authority without a receipt-bound recovery set; "
        "use --seed-legacy-recovery")


def _pull_phase_receipt_path() -> Path:
    return LOCAL_DB.parent / "affiliation-pull-phase-receipt.json"


def _pull_phase_receipt_directory() -> Path:
    return LOCAL_DB.parent / "affiliation-pull-phase-receipts"


def _pull_install_journal_path() -> Path:
    return LOCAL_DB.with_suffix(".pull-install.json")


def _filesystem_identity_key(path: Path) -> str:
    resolved = path.expanduser().resolve()
    normalized = unicodedata.normalize(
        "NFD", os.path.normpath(str(resolved)))
    return normalized.casefold()


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


def _seconds_between(start_ns: int, finish_ns: int) -> float:
    return round((finish_ns - start_ns) / 1_000_000_000, 9)


@contextmanager
def _measured_pull_writer_lock(metrics: dict):
    requested_ns = time.monotonic_ns()
    metrics.update({
        "requestedMonotonicNs": requested_ns,
        "timeoutSeconds": LOCAL_WRITER_TIMEOUT_SECONDS,
    })
    try:
        descriptor = _locks.acquire_bibliography_writer_lock(
            LOCAL_DB, timeout=LOCAL_WRITER_TIMEOUT_SECONDS)
    except _locks.BibliographyWriterLockBusyError as exc:
        rejected_ns = time.monotonic_ns()
        metrics.update({
            "acquisitionOutcome": exc.reason,
            "rejectedMonotonicNs": rejected_ns,
            "waitSeconds": _seconds_between(requested_ns, rejected_ns),
        })
        if exc.reason == "nested":
            metrics["busyRejections"] += 1
        else:
            metrics["timeouts"] += 1
        raise
    except BaseException:
        rejected_ns = time.monotonic_ns()
        metrics.update({
            "acquisitionOutcome": "error",
            "rejectedMonotonicNs": rejected_ns,
            "waitSeconds": _seconds_between(requested_ns, rejected_ns),
        })
        metrics["acquisitionFailures"] += 1
        raise
    acquired_ns = time.monotonic_ns()
    try:
        metrics.update({
            "acquiredMonotonicNs": acquired_ns,
            "acquisitions": metrics["acquisitions"] + 1,
            "waitSeconds": _seconds_between(requested_ns, acquired_ns),
            "acquisitionOutcome": "acquired",
        })
        metrics["descriptorInheritable"] = os.get_inheritable(descriptor)
        if metrics["descriptorInheritable"]:
            raise RuntimeError(
                "bibliography writer lock descriptor is inheritable")
        yield descriptor
    finally:
        body_error = sys.exc_info()[1]
        release_finished_ns = None
        try:
            _locks.release_bibliography_writer_lock(
                LOCAL_DB, descriptor)
        except BaseException as release_error:
            metrics.update({
                "releaseFailures": metrics["releaseFailures"] + 1,
                "releaseOutcome": "unknown",
                "releaseError": {
                    "type": type(release_error).__name__,
                    "message": str(release_error),
                },
            })
            if body_error is None:
                raise
        else:
            release_finished_ns = time.monotonic_ns()
            metrics.update({
                "releaseOutcome": "released",
                "releasedMonotonicNs": release_finished_ns,
                "holdSeconds": _seconds_between(
                    acquired_ns, release_finished_ns),
            })
        finally:
            metrics["releaseAttemptFinishedMonotonicNs"] = (
                release_finished_ns or time.monotonic_ns())


def _pull_once(
               manifest_metrics: dict, install_metrics: dict,
               lock_metrics: dict, phase_state: dict) -> dict:
    with tempfile.TemporaryDirectory(dir=LOCAL_DB.parent) as directory:
        db, mf = Path(directory) / "db", Path(directory) / "manifest"
        _copy_from_authority(MANIFEST, mf)
        raw_manifest = mf.read_text(encoding="utf-8")
        manifest_metrics["reads"] += 1
        manifest = json.loads(raw_manifest)
        phase_state["manifest"] = manifest
        if raw_manifest != canonical_manifest(manifest):
            raise RuntimeError("remote manifest is not canonical")
        rollback = bool(manifest.get("requires_controlled_remigration"))
        _validate_manifest(manifest, rollback=rollback, allow_legacy=True)
        _ensure_installable_pull(manifest)
        remote_object = manifest["object"]
        _copy_from_authority(remote_object, db)
        if sha(db) != manifest["sha256"]:
            raise RuntimeError("remote manifest hash mismatch")
        if _logical_sha(db) != manifest["logical_sha256"]:
            raise RuntimeError("remote manifest logical hash mismatch")
        metadata = _inspect_sqlite(db, require_affiliation=not rollback)
        if not rollback:
            for key in ("schema_version", "source_sha256"):
                if metadata.get(key) != manifest[key]:
                    raise RuntimeError(f"remote manifest {key} mismatch")
        elif manifest["schema_version"] != manifest["restored_schema_version"]:
            raise RuntimeError("rollback manifest restored schema mismatch")
        # The remote migration receipt and the strict-affiliation artifact set
        # were the retired registry's; a generation now proves itself with the
        # digests already verified above.
        with _measured_pull_writer_lock(lock_metrics):
            _ensure_installable_pull(manifest)
            current_manifest = Path(directory) / "current-manifest"
            _copy_from_authority(MANIFEST, current_manifest)
            current_raw = current_manifest.read_text(encoding="utf-8")
            manifest_metrics["reads"] += 1
            manifest_metrics["revalidations"] += 1
            if current_raw != canonical_manifest(manifest):
                manifest_metrics["changesDetected"] += 1
                raise RuntimeError("remote manifest changed while pull was staged")
            migrator._fsync(db)
            install_metrics["stagedFilesFsynced"] = True
            install_journal = _pull_install_journal_path()
            recovering = install_journal.exists()
            lock_metrics.update({
                "recoveries": 1 if recovering else 0,
                "recoveryStatus": (
                    "reinstalling_authoritative_generation"
                    if recovering else "not_required"),
            })
            migrator._atomic_json(install_journal, {
                "kind": "bibliography-pull-install-journal",
                "schemaVersion": 1,
                "status": "prepared",
                "attemptId": phase_state["attemptId"],
                "manifest": manifest,
            })
            install_metrics["installJournalPrepared"] = True
            os.replace(db, LOCAL_DB)
            migrator._fsync(LOCAL_DB)
            install_metrics["databaseInstalled"] = True
            # The migration receipt and artifact descriptor were the retired
            # registry's; the base receipt below is the only receipt left.
            migrator._atomic_json(
                LOCAL_DB.with_suffix(".base.json"), manifest)
            install_metrics["baseReceiptInstalled"] = True
            marker = _remigration_marker()
            if manifest.get("requires_controlled_remigration"):
                migrator._atomic_json(marker, {
                    "operation": "remigration_required",
                    "manifest_generation": manifest.get("generation"),
                    "created_at": manifest.get("updated_at"),
                })
            else:
                marker.unlink(missing_ok=True)
                migrator._fsync_directory(marker.parent)
            install_metrics["installedHashes"] = {
                "databaseSha256": sha(LOCAL_DB),
                "databaseLogicalSha256": _logical_sha(LOCAL_DB),
                "baseReceiptSha256": sha(LOCAL_DB.with_suffix(".base.json")),
            }
            install_metrics["durabilityBarriersPassed"] = True
            install_journal.unlink()
            migrator._fsync_directory(install_journal.parent)
            install_metrics["installJournalCleared"] = True
            if recovering:
                lock_metrics["recoveryStatus"] = (
                    "completed_by_authoritative_reinstall")
    return manifest


def pull(phase_receipt: Path | str | None = None):
    """Install one generation and preserve an attempt-unique phase receipt."""
    LOCAL_DB.parent.mkdir(parents=True, exist_ok=True)
    receipt_path = (
        Path(phase_receipt).expanduser().resolve()
        if phase_receipt is not None else _pull_phase_receipt_path())
    # The destination validator asserted the retired registry's artifact
    # destinations; a phase receipt now only has to be writable.
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    attempt_directory = _pull_phase_receipt_directory()
    attempt_directory.mkdir(parents=True, exist_ok=True)
    while True:
        attempt_id = uuid.uuid4().hex
        attempt_path = attempt_directory / f"{attempt_id}.json"
        if not attempt_path.exists():
            break
    started_at = _utc_timestamp()
    started_ns = time.monotonic_ns()
    error = None
    phase_state = {"manifest": None, "attemptId": attempt_id}
    manifest_metrics = {"reads": 0, "revalidations": 0, "changesDetected": 0}
    install_metrics = {
        "databaseInstalled": False,
        "migrationReceiptInstalled": False,
        "artifactDescriptorInstalledLast": False,
        "baseReceiptInstalled": False,
        "installJournalPrepared": False,
        "installJournalCleared": False,
        "stagedFilesFsynced": False,
        "durabilityBarriersPassed": False,
    }
    lock_metrics = {
        "acquisitions": 0,
        "timeouts": 0,
        "busyRejections": 0,
        "acquisitionFailures": 0,
        "releaseFailures": 0,
        "recoveries": None,
        "recoveryStatus": "not_observed_lock_not_acquired",
        "waitSeconds": None,
        "holdSeconds": None,
        "descriptorInheritable": None,
        "acquisitionOutcome": "not_attempted",
        "releaseOutcome": "not_attempted",
        "timeoutSeconds": LOCAL_WRITER_TIMEOUT_SECONDS,
    }
    in_progress = {
        "kind": "affiliation-pull-phase-receipt",
        "schemaVersion": 2,
        "attemptId": attempt_id,
        "attemptReceipt": str(attempt_path),
        "latestReceipt": str(receipt_path),
        "status": "in_progress",
        "startedAt": started_at,
        "host": socket.gethostname(),
        "manifest": None,
        "manifestMetrics": manifest_metrics,
        "localLockMetrics": lock_metrics,
        "installMetrics": install_metrics,
        "latestReceiptRole": "best_effort_copy_not_audit_authority",
    }
    migrator._atomic_json(attempt_path, in_progress)
    try:
        manifest = _pull_once(
            manifest_metrics, install_metrics,
            lock_metrics, phase_state)
    except BaseException as exc:
        error = {"type": type(exc).__name__, "message": str(exc)}
        raise
    finally:
        finished_ns = time.monotonic_ns()
        report = {
            "kind": "affiliation-pull-phase-receipt",
            "schemaVersion": 2,
            "attemptId": attempt_id,
            "attemptReceipt": str(attempt_path),
            "latestReceipt": str(receipt_path),
            "status": "passed" if error is None else "failed",
            "startedAt": started_at,
            "finishedAt": _utc_timestamp(),
            "durationSeconds": _seconds_between(started_ns, finished_ns),
            "host": socket.gethostname(),
            "manifest": phase_state["manifest"],
            "manifestMetrics": manifest_metrics,
            "localLockMetrics": lock_metrics,
            "installMetrics": install_metrics,
            "latestReceiptRole": "best_effort_copy_not_audit_authority",
        }
        if error is not None:
            report["error"] = error
        try:
            migrator._atomic_json(attempt_path, report)
        except BaseException as attempt_error:
            if error is None:
                raise
            print(
                "pull attempt receipt finalization failed while preserving "
                f"{error['type']}: {attempt_error}",
                file=sys.stderr)
        else:
            try:
                migrator._atomic_json(receipt_path, report)
            except BaseException as latest_error:
                print(
                    "best-effort latest pull receipt update failed; "
                    f"authoritative attempt receipt is {attempt_path}: "
                    f"{latest_error}",
                    file=sys.stderr)
    print(canonical_manifest(manifest))
    return manifest


def _push_preflight(base_receipt: Path | None) -> None:
    """Reject local provenance failures before acquiring a remote authority lease."""
    _ensure_publishable()
    base = base_receipt or LOCAL_DB.with_suffix(".base.json")
    if not base.exists():
        raise RuntimeError("stale/missing base receipt; pull before push")
    try:
        expected = json.loads(base.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError("invalid base receipt") from exc
    _validate_manifest(
        expected,
        rollback=bool(expected.get("requires_controlled_remigration")),
        allow_legacy=True)
    # The origin-receipt transition check was the affiliation registry's
    # migration bookkeeping. What still has to hold is that the local DB is a
    # publishable generation, which building its manifest proves, and that the
    # base it descends from is valid, which `_validate_manifest` proved above.
    local_manifest()


def _cas_conflict(exc: subprocess.CalledProcessError) -> RuntimeError:
    return RuntimeError(
        "CAS conflict: canonical manifest changed or authority lease was fenced")




def _push_locked(base_receipt: Path | None, lease: dict,
                 writer_lock_descriptor: int):
    _ensure_publishable(held_writer_lock_descriptor=writer_lock_descriptor)
    if not LOCAL_DB.exists():
        raise RuntimeError(f"missing local DB: {LOCAL_DB}")
    base = base_receipt or LOCAL_DB.with_suffix(".base.json")
    if not base.exists():
        raise RuntimeError("stale/missing base receipt; pull before push")
    try:
        expected = json.loads(base.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError("invalid base receipt") from exc
    _validate_manifest(
        expected,
        rollback=bool(expected.get("requires_controlled_remigration")),
        allow_legacy=True)
    # A rollback base is publishable only after the local hard-stop marker has
    # been cleared by controlled remigration. _ensure_publishable and the
    # receipt binding below enforce that transition.
    expected_payload = canonical_manifest(expected)
    upload_id = uuid.uuid4().hex
    upload = REMOTE_DB + ".upload." + upload_id
    # The origin-receipt transition check belonged to the affiliation registry's
    # migration bookkeeping, which was retired; a generation is now identified
    # by its content digests and its Git revision alone.
    manifest = local_manifest()
    manifest["generation"] = expected["generation"] + 1
    manifest["base_generation"] = expected["generation"]
    manifest["base_sha256"] = expected["sha256"]
    manifest["base_logical_sha256"] = expected["logical_sha256"]
    manifest["object"] = (
        f"{GENERATIONS}/{manifest['generation']:020d}-{manifest['logical_sha256']}.sqlite3")
    manifest.update({
        "lease_protocol": LEASE_PROTOCOL_VERSION,
        "fence_token": lease["fence_token"],
        "authority_host_uuid": lease["authority_host_uuid"],
        "authority_boot_id": lease["authority_boot_id"],
        "owner_run_id": lease["owner_run_id"],
        "owner_writer_uuid": lease["owner_writer_uuid"],
        "owner_client_host_uuid": lease["owner_client_host_uuid"],
    })
    _validate_manifest(manifest)
    payload = canonical_manifest(manifest)
    _copy_to_authority(LOCAL_DB, upload)
    object_path = manifest["object"]
    # One object per generation. The migration receipt and the strict-affiliation
    # artifact set (cohort, decisions, ledger, generation descriptor) were the
    # affiliation registry's and went out with it, so the immutable upload is
    # now just the database.
    script = (
        f"test -f {_remote_q(MANIFEST)} || exit 74; "
        f"actual=$(cat {_remote_q(MANIFEST)}) || exit 74; "
        f"test \"$actual\" = {_remote_q(expected_payload)} || exit 74; "
        f"test \"$(shasum -a 256 {_remote_q(upload)} | awk '{{print $1}}')\" = "
        f"{_remote_q(manifest['sha256'])} || exit 74; "
        f"mkdir -p {_remote_q(GENERATIONS)}; "
        f"src={_remote_q(upload)}; dst={_remote_q(object_path)}; "
        "if [ -f \"$dst\" ]; then "
        "test \"$(shasum -a 256 \"$src\" | awk '{print $1}')\" = "
        "\"$(shasum -a 256 \"$dst\" | awk '{print $1}')\" "
        "&& rm -f \"$src\" || exit 74; "
        "else mv \"$src\" \"$dst\"; fi; "
        + _remote_fsync(object_path)
        + _atomic_remote_copy(object_path, REMOTE_DB, upload_id)
        + _atomic_remote_json(MANIFEST, payload)
    )
    try:
        _authority_commit(script, lease)
    except subprocess.CalledProcessError as exc:
        try:
            remote("rm -f " + _remote_q(upload))
        except subprocess.CalledProcessError:
            pass
        raise _cas_conflict(exc) from exc
    migrator._atomic_json(base, manifest)
    print(payload)
    return manifest


def push(base_receipt: Path | None):
    """Validate locally, then acquire remote lease and local exclusive flock."""
    _push_preflight(base_receipt)
    LOCAL_DB.parent.mkdir(parents=True, exist_ok=True)
    with authority_lease() as lease:
        with bibliography_writer_lock(LOCAL_DB) as writer_lock_descriptor:
            return _push_locked(base_receipt, lease, writer_lock_descriptor)


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--pull", action="store_true")
    group.add_argument("--push", action="store_true")
    group.add_argument("--status", action="store_true")
    group.add_argument("--bootstrap", action="store_true")
    parser.add_argument("--base-receipt", type=Path)
    args = parser.parse_args()
    try:
        if args.pull:
            pull(args.phase_receipt)
        elif args.push:
            push(args.base_receipt)
        elif args.bootstrap:
            bootstrap()
        else:
            print(remote(f"test -f {_remote_q(MANIFEST)} && cat {_remote_q(MANIFEST)} || echo missing",
                         capture=True).stdout.strip())
    except RuntimeError as error:
        print(str(error))
        return 3 if "remigration required" in str(error) else 4
    return 0


if __name__ == "__main__":
    raise SystemExit(main())