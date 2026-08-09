#!/usr/bin/env python3
"""CAS synchronize immutable bibliography DB generations over SSH."""
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
from contextlib import contextmanager
from pathlib import Path
from threading import Event, Thread
import build_bibliography_db as bibliography
import repair_bibliography_institutions as migrator
from lib import affiliation_registry

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
    return affiliation_registry.bibliography_writer_lock_path(database)


@contextmanager
def bibliography_lock(database: Path, mode: str, *, timeout: float):
    """Delegate to the single registry-owned advisory-lock implementation."""
    with affiliation_registry.bibliography_lock(
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


def _fresh_schema_origin_fields(metadata: dict) -> dict:
    return {
        "operation": "fresh-schema",
        "schema_version": metadata["schema_version"],
        "registry_sha256": metadata["registry_sha256"],
        "event_head": metadata["event_head"],
        "policy_version": metadata["policy_version"],
        "source_sha256": metadata["source_sha256"],
    }


def _fresh_schema_origin_receipt(metadata: dict) -> dict:
    origin = _fresh_schema_origin_fields(metadata)
    return {
        **origin,
        "receipt_id": hashlib.sha256(
            canonical_manifest(origin).encode("utf-8")).hexdigest(),
    }


def _is_valid_fresh_schema_receipt(receipt: object) -> bool:
    if not isinstance(receipt, dict):
        return False
    try:
        return receipt == _fresh_schema_origin_receipt(receipt)
    except KeyError:
        return False


def _is_fresh_schema_origin(manifest: dict) -> bool:
    try:
        return manifest["migration_receipt_id"] == _fresh_schema_origin_receipt(
            manifest)["receipt_id"]
    except KeyError:
        return False


def _fresh_schema_receipt_path() -> Path:
    return migrator.receipt_path(LOCAL_DB, "fresh-schema")


def _validate_fresh_schema_receipt(receipt: dict, manifest: dict) -> None:
    expected = _fresh_schema_origin_receipt(manifest)
    if (not _is_valid_fresh_schema_receipt(receipt) or receipt != expected
            or not _is_fresh_schema_origin(manifest)):
        raise RuntimeError("fresh-schema origin receipt does not bind current provenance")


def _local_affiliation_metadata() -> dict:
    return _inspect_sqlite(LOCAL_DB, require_affiliation=False)


def _required_manifest_fields(*, rollback: bool = False) -> set[str]:
    fields = {
        "database", "generation", "sha256", "logical_sha256", "schema_version",
        "registry_sha256", "event_head", "policy_version", "source_sha256",
        "registry_contract_version", "event_contract_version",
        "country_map_version", "country_map_sha256",
        "evidence_oracle_version", "evidence_oracle_sha256",
        "ledger_head", "cohort_version", "cohort_sha256",
        "relationship_set_sha256", "sql_contract_sha256",
        "strict_result_sha256", "git_revision", "git_blobs",
        "generation_provenance",
        "migration_receipt_id", "migration_receipt_sha256",
        "migration_receipt_object", "updated_at", "object",
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


_GIT_TARGETS = (
    "pipeline/affiliation_registry.json",
    "pipeline/affiliation_registry_corrections.jsonl",
    "pipeline/affiliation_registry_baseline.json",
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


def _relationship_set_sha256() -> str:
    registry = json.loads((ROOT / "pipeline/affiliation_registry.json").read_text(
        encoding="utf-8"))
    values = sorted(item["relationship_id"] for item in registry["relationships"])
    return hashlib.sha256(canonical_manifest(values).encode()).hexdigest()


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
        "registry_sha256": metadata["registry_sha256"],
        "event_head": metadata["event_head"],
        "ledger_head": metadata["ledger_head"],
    }
def _artifact_paths(artifacts: dict[str, Path | str] | None) -> dict[str, Path]:
    """Require a complete explicit strict-affiliation artifact set."""
    if not artifacts:
        return {}
    if set(artifacts) != set(AFFILIATION_ARTIFACT_ROLES):
        raise RuntimeError(
            "strict affiliation artifacts must supply exactly: "
            + ",".join(AFFILIATION_ARTIFACT_ROLES))
    paths = {role: Path(path) for role, path in artifacts.items()}
    missing = [role for role, path in paths.items() if not path.is_file()]
    if missing:
        raise RuntimeError(
            "missing strict affiliation artifact: " + ",".join(sorted(missing)))
    return paths
def _artifact_destinations(artifacts: dict[str, Path | str] | None) -> dict[str, Path]:
    if not artifacts:
        return {}
    if set(artifacts) != set(AFFILIATION_ARTIFACT_ROLES):
        raise RuntimeError(
            "strict affiliation artifacts must supply exactly: "
            + ",".join(AFFILIATION_ARTIFACT_ROLES))
    return {role: Path(path) for role, path in artifacts.items()}




def _artifact_object(generation: int, role: str, digest: str) -> str:
    return f"{GENERATIONS}/{generation:020d}-{digest}.{_AFFILIATION_ARTIFACT_SUFFIXES[role]}"


def _manifest_artifacts(manifest: dict) -> dict[str, dict]:
    """Return validated strict bindings, rejecting incomplete declarations."""
    bindings = manifest.get("affiliation_artifacts")
    strict = manifest.get("strict_affiliation_generation", False)
    if bindings is None:
        if strict:
            raise RuntimeError("strict affiliation generation lacks artifact bindings")
        return {}
    if strict is not True or not isinstance(bindings, dict):
        raise RuntimeError("affiliation artifact bindings require a strict generation claim")
    if set(bindings) != set(AFFILIATION_ARTIFACT_ROLES):
        raise RuntimeError("strict affiliation artifact roles are incomplete or invalid")
    generation = manifest.get("generation")
    for role, binding in bindings.items():
        if (not isinstance(binding, dict)
                or not isinstance(binding.get("sha256"), str)
                or len(binding["sha256"]) != 64
                or any(char not in "0123456789abcdef" for char in binding["sha256"])
                or binding.get("object") != _artifact_object(
                    generation, role, binding["sha256"])):
            raise RuntimeError(f"strict affiliation artifact binding is invalid: {role}")
    return bindings


def _add_artifact_bindings(manifest: dict, paths: dict[str, Path]) -> None:
    if not paths:
        return
    manifest["strict_affiliation_generation"] = True
    manifest["affiliation_artifacts"] = {
        role: {"sha256": sha(path), "object": _artifact_object(
            manifest["generation"], role, sha(path))}
        for role, path in paths.items()
    }


def _stage_artifacts(manifest: dict, directory: Path) -> dict[str, Path]:
    staged = {}
    for role, binding in _manifest_artifacts(manifest).items():
        target = directory / f"affiliation-{role}"
        _copy_from_authority(binding["object"], target)
        if sha(target) != binding["sha256"]:
            raise RuntimeError(f"remote strict affiliation artifact hash mismatch: {role}")
        staged[role] = target
    return staged


def _validate_artifact_equality(manifest: dict, paths: dict[str, Path]) -> None:
    bindings = _manifest_artifacts(manifest)
    if bool(bindings) != bool(paths):
        raise RuntimeError("strict affiliation artifact destinations do not match manifest")
    for role, path in paths.items():
        if sha(path) != bindings[role]["sha256"]:
            raise RuntimeError(f"strict affiliation artifact equality mismatch: {role}")


def _install_artifacts_descriptor_last(
        staged: dict[str, Path], destinations: dict[str, Path]) -> None:
    """Install ordinary strict artifacts first and the generation pointer last."""
    for role in ("cohort", "decisions", "ledger", "generation_descriptor"):
        if role not in staged:
            continue
        destination = destinations[role]
        destination.parent.mkdir(parents=True, exist_ok=True)
        os.replace(staged[role], destination)


def _validate_manifest(manifest: dict, *, rollback: bool = False,
                       allow_legacy: bool = False) -> None:
    if not isinstance(manifest, dict):
        raise RuntimeError("manifest is invalid")
    core_fields = {
        "database", "generation", "sha256", "logical_sha256", "schema_version",
        "registry_sha256", "event_head", "policy_version", "source_sha256",
        "migration_receipt_id", "migration_receipt_sha256",
        "migration_receipt_object", "updated_at", "object",
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
    if manifest["migration_receipt_object"] != (
            f"{GENERATIONS}/{manifest['generation']:020d}-"
            f"{manifest['migration_receipt_sha256']}.migration.json"):
        raise RuntimeError("manifest immutable migration receipt name mismatch")
    legacy = allow_legacy and manifest.get("schema_version") == "affiliation-2"
    missing = sorted(key for key in _required_manifest_fields(rollback=rollback)
                     if manifest.get(key) in (None, ""))
    if missing and not legacy:
        raise RuntimeError("manifest lacks required provenance: " + ",".join(missing))
    _manifest_artifacts(manifest)
    if legacy:
        return
    if (not isinstance(manifest["git_blobs"], dict)
            or set(manifest["git_blobs"]) != set(_GIT_TARGETS)
            or not all(isinstance(blob, str) and blob for blob
                       in manifest["git_blobs"].values())):
        raise RuntimeError("manifest Git blob provenance is invalid")
    if manifest["lease_protocol"] != LEASE_PROTOCOL_VERSION:
        raise RuntimeError("manifest lease protocol is invalid")
    if (not isinstance(manifest["fence_token"], int)
            or not 0 < manifest["fence_token"] < (1 << 64)):
        raise RuntimeError("manifest fence token is invalid")
    provenance = manifest.get("generation_provenance")
    if provenance is not None:
        if not isinstance(provenance, dict):
            raise RuntimeError("manifest generation provenance is invalid")
        common_invalid = (
            provenance.get("git_revision") != manifest["git_revision"]
            or provenance.get("registry_sha256") != manifest["registry_sha256"])
        current_invalid = (
            provenance.get("event_head") != manifest["event_head"]
            or provenance.get("ledger_head") != manifest["ledger_head"])
        legacy_valid = (
            allow_legacy
            and provenance.get("evidence_ledger_head") == manifest["event_head"]
            and set(provenance) == {
                "git_revision", "registry_sha256", "evidence_ledger_head"})
        if common_invalid or (current_invalid and not legacy_valid):
            raise RuntimeError("manifest generation provenance is invalid")


def _inspect_sqlite(path: Path, *, require_affiliation: bool) -> dict:
    connection = sqlite3.connect(path)
    try:
        if connection.execute("PRAGMA quick_check").fetchone()[0] != "ok":
            raise RuntimeError(f"SQLite integrity check failed: {path}")
        try:
            row = connection.execute(
                "SELECT schema_version,registry_sha256,event_head,policy_version,"
                "source_sha256,migration_receipt_id,registry_contract_version,"
                "event_contract_version,country_map_version,country_map_sha256,"
                "evidence_oracle_version,evidence_oracle_sha256,ledger_head,"
                "cohort_version,cohort_sha256 FROM affiliation_registry_metadata "
                "WHERE singleton=1"
            ).fetchone()
        except sqlite3.Error:
            row = None
    finally:
        connection.close()
    if require_affiliation and (
            row is None or row[0] != bibliography.AFFILIATION_SCHEMA_VERSION
            or not all(row[1:])):
        raise RuntimeError(
            f"{bibliography.AFFILIATION_SCHEMA_VERSION} metadata is missing from bibliography DB")
    keys = (
        "schema_version", "registry_sha256", "event_head", "policy_version",
        "source_sha256", "migration_receipt_id", "registry_contract_version",
        "event_contract_version", "country_map_version", "country_map_sha256",
        "evidence_oracle_version", "evidence_oracle_sha256", "ledger_head",
        "cohort_version", "cohort_sha256",
    )
    return {} if row is None else dict(zip(keys, row))


def _remote_bootstrap_metadata() -> dict:
    program = (
        "import json,sqlite3,sys;"
        "from pathlib import Path;"
        "sys.path.insert(0,str(Path(sys.argv[1]).parent.parent/'pipeline'));"
        "import repair_bibliography_institutions as m;"
        "c=sqlite3.connect(sys.argv[1]);"
        "ok=c.execute('PRAGMA quick_check').fetchone()[0];"
        "r=c.execute('SELECT schema_version,registry_sha256,event_head,policy_version,"
        "source_sha256,migration_receipt_id,registry_contract_version,"
        "event_contract_version,country_map_version,country_map_sha256,"
        "evidence_oracle_version,evidence_oracle_sha256,ledger_head,"
        "cohort_version,cohort_sha256 FROM affiliation_registry_metadata "
        "WHERE singleton=1').fetchone();"
        "logical=m.logical_digest(c);c.close();"
        "assert ok=='ok' and r and r[0]=='affiliation-3' and all(r[1:]);"
        "print(json.dumps({'schema_version':r[0],'registry_sha256':r[1],"
        "'event_head':r[2],'policy_version':r[3],'source_sha256':r[4],"
        "'migration_receipt_id':r[5],'registry_contract_version':r[6],"
        "'event_contract_version':r[7],'country_map_version':r[8],"
        "'country_map_sha256':r[9],'evidence_oracle_version':r[10],"
        "'evidence_oracle_sha256':r[11],'ledger_head':r[12],"
        "'cohort_version':r[13],'cohort_sha256':r[14],'logical_sha256':logical},"
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
        affiliation_artifacts: dict[str, Path | str] | None = None,
        held_writer_lock_descriptor: int | None = None) -> None:
    marker = _remigration_marker()
    if marker.exists():
        raise RuntimeError("remigration required before bibliography synchronization")
    if not LOCAL_DB.exists():
        raise RuntimeError(f"missing local DB: {LOCAL_DB}")
    metadata = _local_affiliation_metadata()
    if (metadata.get("schema_version") != bibliography.AFFILIATION_SCHEMA_VERSION or not all(
            metadata.get(key) for key in (
                "registry_sha256", "event_head", "policy_version",
                "source_sha256", "migration_receipt_id"))):
        raise RuntimeError(
            f"{bibliography.AFFILIATION_SCHEMA_VERSION} metadata is missing; migrate and validate before push")
    checker_path = ROOT / "pipeline" / "check_bibliography_db.py"
    artifact_paths = _artifact_paths(affiliation_artifacts)
    checker_args = ["--db", str(LOCAL_DB), "--strict"]
    if artifact_paths:
        checker_args.extend([
            "--cohort", str(artifact_paths["cohort"]),
            "--decisions", str(artifact_paths["decisions"]),
            "--ledger", str(artifact_paths["ledger"]),
            "--generation-descriptor",
            str(artifact_paths["generation_descriptor"]),
        ])
    try:
        if held_writer_lock_descriptor is None:
            run([sys.executable, str(checker_path), *checker_args])
        else:
            import check_bibliography_db as checker
            result = checker.main(
                checker_args,
                held_writer_lock_descriptor=held_writer_lock_descriptor)
            if result:
                raise subprocess.CalledProcessError(
                    result, [str(checker_path), *checker_args])
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


def local_manifest(affiliation_artifacts: dict[str, Path | str] | None = None) -> dict:
    metadata = _inspect_sqlite(LOCAL_DB, require_affiliation=True)
    contracts = {
        "relationship_set_sha256": _relationship_set_sha256(),
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
    _add_artifact_bindings(manifest, _artifact_paths(affiliation_artifacts))
    return manifest
def _migration_receipt_path() -> Path:
    return migrator.receipt_path(LOCAL_DB, "migrate")


def _load_current_migration_receipt(manifest: dict) -> tuple[dict, Path, str]:
    path = _migration_receipt_path()
    if not path.exists():
        raise RuntimeError("missing local migration receipt sidecar")
    try:
        receipt = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError("invalid local migration receipt sidecar") from exc
    receipt_digest = sha(path)
    if (receipt.get("operation") != "migrate"
            or receipt.get("receipt_id") != manifest["migration_receipt_id"]
            or receipt.get("schema_to") != manifest["schema_version"]):
        raise RuntimeError("migration receipt does not bind immutable migration provenance")
    _verify_migration_audit(receipt, manifest, LOCAL_DB)
    return receipt, path, receipt_digest
def _has_migration_audit(database: Path) -> bool:
    connection = sqlite3.connect(database)
    try:
        row = connection.execute(
            "SELECT 1 FROM affiliation_migration_audit "
            "WHERE operation='migrate' LIMIT 1").fetchone()
    except sqlite3.Error:
        return False
    finally:
        connection.close()
    return row is not None


def _load_current_origin_receipt(manifest: dict) -> tuple[dict, Path, str]:
    if not _is_fresh_schema_origin(manifest):
        return _load_current_migration_receipt(manifest)
    if _has_migration_audit(LOCAL_DB):
        raise RuntimeError("fresh-schema origin is invalid for a migrated DB")
    path = _fresh_schema_receipt_path()
    receipt = _fresh_schema_origin_receipt(manifest)
    if path.exists():
        try:
            saved = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise RuntimeError("invalid local fresh-schema origin receipt") from exc
        if not _is_valid_fresh_schema_receipt(saved):
            raise RuntimeError("invalid local fresh-schema origin receipt")
        if saved["receipt_id"] != receipt["receipt_id"]:
            migrator._atomic_json(path, receipt)
        else:
            _validate_fresh_schema_receipt(saved, manifest)
    else:
        migrator._atomic_json(path, receipt)
    return receipt, path, sha(path)


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


def _verify_migration_audit(receipt: dict, manifest: dict, database: Path) -> None:
    """Verify immutable migration provenance recorded in a specific DB."""
    connection = sqlite3.connect(database)
    try:
        row = connection.execute(
            "SELECT operation,base_generation,base_logical_sha256,"
            "result_logical_sha256,registry_sha256,schema_from,schema_to,report_json "
            "FROM affiliation_migration_audit WHERE receipt_id=?",
            (receipt["receipt_id"],),
        ).fetchone()
    except sqlite3.Error as exc:
        raise RuntimeError("bibliography DB lacks migration audit") from exc
    finally:
        connection.close()
    if row is None:
        raise RuntimeError("migration receipt is absent from DB audit")
    operation, generation, base_logical, result_logical, registry, schema_from, schema_to, report = row
    if (operation != "migrate" or generation != receipt["base_generation"]
            or base_logical != receipt["base_logical_sha256"]
            or result_logical != receipt["result_logical_sha256"]
            or registry != receipt["registry_sha256"]
            or schema_from != receipt["schema_from"] or schema_to != receipt["schema_to"]):
        raise RuntimeError("migration provenance does not match DB audit")
    try:
        audited = json.loads(report)
    except json.JSONDecodeError as exc:
        raise RuntimeError("DB migration audit is invalid") from exc
    if (audited.get("receipt_id") != receipt["receipt_id"]
            or any(audited.get(key) != receipt[key] for key in (
                "base_generation", "base_sha256", "base_logical_sha256",
                "registry_sha256", "event_head", "policy_version",
                "source_sha256", "schema_from", "schema_to"))):
        raise RuntimeError("DB migration audit receipt mismatch")


def _verify_complete_migration_receipt(receipt: dict, manifest: dict,
                                       database: Path) -> None:
    """Bind a changed origin to the complete immutable audit payload."""
    connection = sqlite3.connect(database)
    try:
        row = connection.execute(
            "SELECT operation,base_generation,base_logical_sha256,"
            "result_logical_sha256,registry_sha256,schema_from,schema_to,"
            "backup_path,backup_sha256,started_at,finished_at,report_json "
            "FROM affiliation_migration_audit WHERE receipt_id=?",
            (receipt["receipt_id"],)).fetchone()
    except sqlite3.Error as exc:
        raise RuntimeError("bibliography DB lacks migration audit") from exc
    finally:
        connection.close()
    if row is None:
        raise RuntimeError("migration receipt is absent from DB audit")
    try:
        audited = json.loads(row[11])
    except (TypeError, json.JSONDecodeError) as exc:
        raise RuntimeError("DB migration audit is invalid") from exc
    try:
        migrator.validate_migration_audit_report(audited)
    except RuntimeError as exc:
        raise RuntimeError(
            "changed migration receipt has incomplete immutable audit") from exc
    expected = {**audited, "result_sha256": receipt.get("result_sha256")}
    columns = (
        audited["operation"], audited["base_generation"],
        audited["base_logical_sha256"], audited["result_logical_sha256"],
        audited["registry_sha256"], audited["schema_from"],
        audited["schema_to"], audited["backup"],
        audited["backup_sha256"], audited["started_at"], audited["finished_at"],
    )
    if receipt != expected or row[:11] != columns:
        raise RuntimeError(
            "changed migration receipt does not exactly match immutable audit")
    _verify_migration_audit(receipt, manifest, database)


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


def pull(affiliation_artifacts: dict[str, Path | str] | None = None):
    LOCAL_DB.parent.mkdir(parents=True, exist_ok=True)
    artifact_destinations = _artifact_destinations(affiliation_artifacts)
    with tempfile.TemporaryDirectory(dir=LOCAL_DB.parent) as directory:
        db, mf = Path(directory) / "db", Path(directory) / "manifest"
        _copy_from_authority(MANIFEST, mf)
        raw_manifest = mf.read_text(encoding="utf-8")
        manifest = json.loads(raw_manifest)
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
            for key in ("schema_version", "registry_sha256", "event_head",
                        "policy_version", "source_sha256", "migration_receipt_id"):
                if metadata.get(key) != manifest[key]:
                    raise RuntimeError(f"remote manifest {key} mismatch")
        elif manifest["schema_version"] != manifest["restored_schema_version"]:
            raise RuntimeError("rollback manifest restored schema mismatch")
        receipt = Path(directory) / "migration-receipt"
        _copy_from_authority(manifest["migration_receipt_object"], receipt)
        if sha(receipt) != manifest["migration_receipt_sha256"]:
            raise RuntimeError("remote migration receipt hash mismatch")
        try:
            receipt_value = json.loads(receipt.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise RuntimeError("remote migration receipt is invalid") from exc
        if receipt_value.get("receipt_id") != manifest["migration_receipt_id"]:
            raise RuntimeError("remote migration receipt ID mismatch")
        if not rollback:
            if _is_fresh_schema_origin(manifest):
                _validate_fresh_schema_receipt(receipt_value, manifest)
                if _has_migration_audit(db):
                    raise RuntimeError(
                        "fresh-schema origin is invalid for a migrated DB")
            elif (receipt_value.get("operation") != "migrate"
                  or receipt_value.get("schema_to") != manifest["schema_version"]):
                raise RuntimeError(
                    "remote migration receipt does not bind immutable migration provenance")
            else:
                _verify_migration_audit(receipt_value, manifest, db)
        staged_artifacts = _stage_artifacts(manifest, Path(directory))
        if _manifest_artifacts(manifest) and not artifact_destinations:
            raise RuntimeError("strict affiliation generation requires artifact destinations")
        with bibliography_writer_lock(LOCAL_DB):
            _ensure_installable_pull(manifest)
            current_manifest = Path(directory) / "current-manifest"
            _copy_from_authority(MANIFEST, current_manifest)
            if current_manifest.read_text(encoding="utf-8") != canonical_manifest(manifest):
                raise RuntimeError("remote manifest changed while pull was staged")
            _validate_artifact_equality(manifest, staged_artifacts)
            os.replace(db, LOCAL_DB)
            if _is_fresh_schema_origin(manifest):
                migrator._atomic_json(_fresh_schema_receipt_path(), receipt_value)
            else:
                migrator._atomic_json(_migration_receipt_path(), receipt_value)
            _install_artifacts_descriptor_last(
                staged_artifacts, artifact_destinations)
            _validate_artifact_equality(manifest, artifact_destinations)
            migrator._atomic_json(
                LOCAL_DB.with_suffix(".base.json"), manifest)
            marker = _remigration_marker()
            if manifest.get("requires_controlled_remigration"):
                migrator._atomic_json(marker, {
                    "operation": "remigration_required",
                    "manifest_generation": manifest.get("generation"),
                    "migration_receipt_id": manifest.get("migration_receipt_id"),
                    "created_at": manifest.get("updated_at"),
                })
            else:
                marker.unlink(missing_ok=True)
    print(canonical_manifest(manifest))
    return manifest


def _validate_origin_transition(expected: dict, manifest: dict,
                                receipt: dict, receipt_digest: str) -> None:
    """Allow only exact reuse, deterministic fresh rotation, or remigration."""
    if manifest["migration_receipt_id"] == expected["migration_receipt_id"]:
        if receipt_digest != expected["migration_receipt_sha256"]:
            raise RuntimeError(
                "current receipt sidecar differs from the synchronized origin receipt")
        return
    if (_is_fresh_schema_origin(expected) and _is_fresh_schema_origin(manifest)
            and not _has_migration_audit(LOCAL_DB)):
        _validate_fresh_schema_receipt(receipt, manifest)
        return
    if (
            manifest.get("strict_affiliation_generation") is True
            and _manifest_artifacts(manifest)
            and receipt.get("operation") == "migrate"):
        required = {
            "base_generation": expected["generation"],
            "base_sha256": expected["sha256"],
            "base_logical_sha256": expected["logical_sha256"],
            "schema_from": expected["schema_version"],
            "schema_to": manifest["schema_version"],
            "receipt_id": manifest["migration_receipt_id"],
        }
        if any(receipt.get(key) != value for key, value in required.items()):
            raise RuntimeError(
                "strict generation migration receipt does not bind the synchronized base")
        _verify_complete_migration_receipt(receipt, manifest, LOCAL_DB)
        return
    if expected.get("requires_controlled_remigration"):
        required = {
            "operation": "migrate",
            "base_generation": expected["generation"],
            "base_sha256": expected["sha256"],
            "base_logical_sha256": expected["logical_sha256"],
            "schema_from": expected["schema_version"],
            "schema_to": manifest["schema_version"],
            "result_sha256": manifest["sha256"],
            "result_logical_sha256": manifest["logical_sha256"],
            "receipt_id": manifest["migration_receipt_id"],
        }
        if (any(receipt.get(key) != value for key, value in required.items())
                or any(receipt.get(key) != manifest[key] for key in (
                    "registry_sha256", "event_head", "policy_version",
                    "source_sha256"))):
            raise RuntimeError(
                "controlled remigration receipt does not bind the local result")
        _verify_complete_migration_receipt(receipt, manifest, LOCAL_DB)
        return
    raise RuntimeError(
        "origin receipt changed without fresh rotation or controlled remigration")
def _push_preflight(
        base_receipt: Path | None,
        affiliation_artifacts: dict[str, Path | str] | None = None) -> None:
    """Reject local provenance failures before acquiring a remote authority lease."""
    artifact_paths = _artifact_paths(affiliation_artifacts)
    _ensure_publishable(artifact_paths)
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
    manifest = local_manifest(artifact_paths)
    receipt, _, receipt_digest = _load_current_origin_receipt(manifest)
    _validate_origin_transition(expected, manifest, receipt, receipt_digest)


def _cas_conflict(exc: subprocess.CalledProcessError) -> RuntimeError:
    return RuntimeError(
        "CAS conflict: canonical manifest changed or authority lease was fenced")




def _push_locked(base_receipt: Path | None, lease: dict,
                 affiliation_artifacts: dict[str, Path | str] | None,
                 writer_lock_descriptor: int):
    artifact_paths = _artifact_paths(affiliation_artifacts)
    _ensure_publishable(
        artifact_paths, held_writer_lock_descriptor=writer_lock_descriptor)
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
    receipt_upload = REMOTE_DB + ".receipt.upload." + upload_id
    manifest = local_manifest(artifact_paths)
    receipt, receipt_path, receipt_digest = _load_current_origin_receipt(manifest)
    _validate_origin_transition(expected, manifest, receipt, receipt_digest)
    manifest["generation"] = expected["generation"] + 1
    manifest["base_generation"] = expected["generation"]
    manifest["base_sha256"] = expected["sha256"]
    manifest["base_logical_sha256"] = expected["logical_sha256"]
    manifest["migration_receipt_sha256"] = receipt_digest
    _add_artifact_bindings(manifest, artifact_paths)
    manifest["object"] = (
        f"{GENERATIONS}/{manifest['generation']:020d}-{manifest['logical_sha256']}.sqlite3")
    manifest["migration_receipt_object"] = (
        f"{GENERATIONS}/{manifest['generation']:020d}-{receipt_digest}.migration.json")
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
    _copy_to_authority(receipt_path, receipt_upload)
    object_path = manifest["object"]
    receipt_object = manifest["migration_receipt_object"]
    artifact_uploads = {
        role: REMOTE_DB + f".{role}.upload." + upload_id
        for role in AFFILIATION_ARTIFACT_ROLES if role in artifact_paths
    }
    for role, upload_path in artifact_uploads.items():
        _copy_to_authority(artifact_paths[role], upload_path)
    script = (
        f"test -f {_remote_q(MANIFEST)} || exit 74; "
        f"actual=$(cat {_remote_q(MANIFEST)}) || exit 74; "
        f"test \"$actual\" = {_remote_q(expected_payload)} || exit 74; "
        f"test \"$(shasum -a 256 {_remote_q(upload)} | awk '{{print $1}}')\" = {_remote_q(manifest['sha256'])} || exit 74; "
        f"test \"$(shasum -a 256 {_remote_q(receipt_upload)} | awk '{{print $1}}')\" = {_remote_q(receipt_digest)} || exit 74; "
        + "".join(
            f"test \"$(shasum -a 256 {_remote_q(artifact_uploads[role])} | awk '{{print $1}}')\" = "
            f"{_remote_q(manifest['affiliation_artifacts'][role]['sha256'])} || exit 74; "
            for role in AFFILIATION_ARTIFACT_ROLES if role in artifact_uploads)
        + f"python3 -c 'import sqlite3,sys; c=sqlite3.connect(sys.argv[1]); "
        "ok=c.execute(\"PRAGMA quick_check\").fetchone()[0]==\"ok\"; c.close(); raise SystemExit(not ok)' "
        f"{_remote_q(upload)} || exit 74; mkdir -p {_remote_q(GENERATIONS)}; "
        f"for pair in {_remote_q(upload)}:{_remote_q(object_path)} {_remote_q(receipt_upload)}:{_remote_q(receipt_object)} "
        + " ".join(
            _remote_q(f"{artifact_uploads[role]}:{manifest['affiliation_artifacts'][role]['object']}")
            for role in ("cohort", "decisions", "ledger", "generation_descriptor")
            if role in artifact_uploads)
        + "; do "
        "src=${pair%%:*}; dst=${pair#*:}; if test -e \"$dst\"; then "
        "test \"$(shasum -a 256 \"$dst\" | awk '{print $1}')\" = \"$(shasum -a 256 \"$src\" | awk '{print $1}')\" "
        "&& rm -f \"$src\" || { rm -f \"$dst\"; mv \"$src\" \"$dst\"; }; else mv \"$src\" \"$dst\"; fi; done; "
        + _remote_fsync(object_path)
        + "".join(
            _remote_fsync(manifest["affiliation_artifacts"][role]["object"])
            for role in ("cohort", "decisions", "ledger", "generation_descriptor")
            if role in artifact_uploads)
        + _remote_fsync(receipt_object)
        + _atomic_remote_copy(object_path, REMOTE_DB, upload_id)
        + _atomic_remote_json(MANIFEST, payload)
    )
    try:
        _authority_commit(script, lease)
    except subprocess.CalledProcessError as exc:
        try:
            remote(
                "rm -f " + " ".join(
                    _remote_q(path) for path in (
                        upload, receipt_upload, *artifact_uploads.values())))
        except subprocess.CalledProcessError:
            pass
        raise _cas_conflict(exc) from exc
    migrator._atomic_json(base, manifest)
    print(payload)
    return manifest


def push(base_receipt: Path | None,
         affiliation_artifacts: dict[str, Path | str] | None = None):
    """Validate locally, then acquire remote lease and local exclusive flock."""
    _push_preflight(base_receipt, affiliation_artifacts)
    LOCAL_DB.parent.mkdir(parents=True, exist_ok=True)
    with authority_lease() as lease:
        with bibliography_writer_lock(LOCAL_DB) as writer_lock_descriptor:
            return _push_locked(
                base_receipt, lease, affiliation_artifacts,
                writer_lock_descriptor)


def _seed_legacy_recovery_locked(base_receipt: Path | None, lease: dict) -> dict:
    """Publish the verified retained pre-migration DB as a monotonic recovery generation."""
    if _remigration_marker().exists():
        raise RuntimeError("remigration required before legacy recovery seed")
    if not LOCAL_DB.exists():
        raise RuntimeError(f"missing local DB: {LOCAL_DB}")
    base = base_receipt or LOCAL_DB.with_suffix(".base.json")
    if not base.exists():
        raise RuntimeError("legacy recovery seed requires the pulled generation receipt")
    expected = json.loads(base.read_text(encoding="utf-8"))
    required = {"database", "generation", "sha256", "logical_sha256"}
    if any(expected.get(key) in (None, "") for key in required):
        raise RuntimeError("legacy recovery seed base receipt is incomplete")
    manifest = local_manifest()
    for key in (
            "database", "sha256", "logical_sha256", "schema_version",
            "registry_sha256", "event_head", "policy_version",
            "source_sha256", "migration_receipt_id"):
        if manifest.get(key) != expected.get(key):
            raise RuntimeError(
                f"legacy recovery seed base receipt does not match local {key}")
    receipt_path = _migration_receipt_path()
    if not receipt_path.exists():
        raise RuntimeError("legacy recovery seed requires the original migration receipt")
    try:
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError("legacy recovery seed migration receipt is invalid") from exc
    receipt_digest = sha(receipt_path)
    if (receipt.get("operation") != "migrate"
            or receipt.get("receipt_id") != manifest["migration_receipt_id"]
            or receipt.get("base_generation") != expected["generation"]
            or any(receipt.get(key) != manifest[key] for key in (
                "registry_sha256", "event_head", "policy_version",
                "source_sha256"))):
        raise RuntimeError(
            "legacy recovery seed migration receipt does not bind current provenance")
    _verify_migration_audit(receipt, manifest, LOCAL_DB)
    backup = Path(receipt["backup"])
    if not backup.exists() or sha(backup) != receipt["backup_sha256"]:
        raise RuntimeError("legacy recovery seed requires the retained migration backup")
    probe = sqlite3.connect(backup)
    try:
        if (probe.execute("PRAGMA quick_check").fetchone()[0] != "ok"
                or migrator.logical_digest(probe) != receipt["base_logical_sha256"]
                or migrator._schema_name(probe) != receipt["schema_from"]):
            raise RuntimeError("legacy recovery backup provenance mismatch")
    finally:
        probe.close()
    generation = expected["generation"] + 1
    result = {
        "database": expected["database"], "generation": generation,
        "sha256": sha(backup), "logical_sha256": receipt["base_logical_sha256"],
        "schema_version": receipt["schema_from"],
        "registry_sha256": receipt["registry_sha256"], "event_head": receipt["event_head"],
        "policy_version": receipt["policy_version"], "source_sha256": receipt["source_sha256"],
        "migration_receipt_id": receipt["receipt_id"],
        "migration_receipt_sha256": receipt_digest,
        "migration_receipt_object": f"{GENERATIONS}/{generation:020d}-{receipt_digest}.migration.json",
        "base_generation": expected["generation"], "base_sha256": expected["sha256"],
        "base_logical_sha256": expected["logical_sha256"],
        "restored_schema_version": receipt["schema_from"],
        "requires_controlled_remigration": True, "operation": "legacy_recovery_seed",
        "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "object": f"{GENERATIONS}/{generation:020d}-{receipt['base_logical_sha256']}.sqlite3",
    }
    result.update({key: expected[key] for key in _required_manifest_fields()
                   if key in expected and key not in result})
    result.update({
        "lease_protocol": LEASE_PROTOCOL_VERSION,
        "fence_token": lease["fence_token"],
        "authority_host_uuid": lease["authority_host_uuid"],
        "authority_boot_id": lease["authority_boot_id"],
        "owner_run_id": lease["owner_run_id"],
        "owner_writer_uuid": lease["owner_writer_uuid"],
        "owner_client_host_uuid": lease["owner_client_host_uuid"],
    })
    _validate_manifest(result, rollback=True)
    payload, expected_payload = canonical_manifest(result), canonical_manifest(expected)
    upload_id = uuid.uuid4().hex
    upload, receipt_upload = REMOTE_DB + ".seed." + upload_id, REMOTE_DB + ".seed-receipt." + upload_id
    _copy_to_authority(backup, upload)
    _copy_to_authority(receipt_path, receipt_upload)
    script = (
        f"actual=$(cat {_remote_q(MANIFEST)}) || exit 74; test \"$actual\" = {_remote_q(expected_payload)} || exit 74; "
        f"test \"$(shasum -a 256 {_remote_q(upload)} | awk '{{print $1}}')\" = {_remote_q(result['sha256'])} || exit 74; "
        f"test \"$(shasum -a 256 {_remote_q(receipt_upload)} | awk '{{print $1}}')\" = {_remote_q(receipt_digest)} || exit 74; "
        f"mkdir -p {_remote_q(GENERATIONS)}; mv {_remote_q(upload)} {_remote_q(result['object'])}; "
        f"mv {_remote_q(receipt_upload)} {_remote_q(result['migration_receipt_object'])}; "
        + _remote_fsync(result["object"]) + _remote_fsync(result["migration_receipt_object"])
        + _atomic_remote_copy(result["object"], REMOTE_DB, upload_id)
        + _atomic_remote_json(MANIFEST, payload))
    try:
        _authority_commit(script, lease)
    except subprocess.CalledProcessError as exc:
        raise _cas_conflict(exc) from exc
    base.write_text(payload, encoding="utf-8")
    return result

def seed_legacy_recovery(base_receipt: Path | None) -> dict:
    _seed_legacy_recovery_preflight(base_receipt)
    with authority_lease() as lease:
        with bibliography_writer_lock(LOCAL_DB):
            return _seed_legacy_recovery_locked(base_receipt, lease)

def _seed_legacy_recovery_preflight(base_receipt: Path | None) -> None:
    if _remigration_marker().exists():
        raise RuntimeError("remigration required before legacy recovery seed")
    if not LOCAL_DB.exists():
        raise RuntimeError(f"missing local DB: {LOCAL_DB}")
    base = base_receipt or LOCAL_DB.with_suffix(".base.json")
    if not base.exists():
        raise RuntimeError("legacy recovery seed requires the pulled generation receipt")
    try:
        expected = json.loads(base.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError("invalid base receipt") from exc
    required = {"database", "generation", "sha256", "logical_sha256"}
    if any(expected.get(key) in (None, "") for key in required):
        raise RuntimeError("legacy recovery seed base receipt is incomplete")
    if not _migration_receipt_path().exists():
        raise RuntimeError("legacy recovery seed requires the original migration receipt")



def _published_rollback_locked(target_generation: int, base_receipt: Path | None,
                               migration_receipt: Path | None, lease: dict) -> dict:
    """Publish a retained generation as a new monotonic generation under CAS."""
    _ensure_publishable()
    base = base_receipt or LOCAL_DB.with_suffix(".base.json")
    if not base.exists():
        raise RuntimeError("stale/missing base receipt; pull before published rollback")
    try:
        expected = json.loads(base.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError("invalid base receipt") from exc
    _validate_manifest(expected, allow_legacy=True)
    expected_payload = canonical_manifest(expected)
    if migration_receipt is None or not migration_receipt.exists():
        raise RuntimeError("published rollback requires a migration receipt")
    try:
        migration = json.loads(migration_receipt.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError("invalid migration receipt") from exc
    required_receipt = {
        "operation", "receipt_id", "base_generation", "base_sha256", "base_logical_sha256",
        "result_sha256", "result_logical_sha256", "schema_from", "schema_to",
        "registry_sha256", "event_head", "policy_version", "source_sha256",
    }
    missing = sorted(key for key in required_receipt if migration.get(key) in (None, ""))
    if missing:
        raise RuntimeError("migration receipt lacks required provenance: " + ",".join(missing))
    receipt_digest = sha(migration_receipt)
    if (migration["operation"] != "migrate"
            or migration["receipt_id"] != expected["migration_receipt_id"]
            or migration["result_sha256"] != expected["sha256"]
            or migration["result_logical_sha256"] != expected["logical_sha256"]
            or migration["schema_to"] != expected["schema_version"]
            or any(migration[key] != expected[key] for key in (
                "registry_sha256", "event_head", "policy_version", "source_sha256"))):
        raise RuntimeError("migration receipt does not bind the current generation")
    if receipt_digest != expected["migration_receipt_sha256"]:
        raise RuntimeError("migration receipt is not the synchronized receipt artifact")
    if target_generation < 0 or target_generation >= expected["generation"]:
        raise RuntimeError("rollback target must be an older retained generation")
    _verify_migration_audit(migration, expected, LOCAL_DB)

    listing = remote(
        f"set -- {_remote_q(GENERATIONS)}/{target_generation:020d}-*.sqlite3; "
        "test \"$#\" -eq 1 && test -f \"$1\" && printf '%s' \"$1\"",
        capture=True,
    ).stdout.strip()
    if not listing:
        raise RuntimeError("rollback target generation is missing or ambiguous")

    with tempfile.TemporaryDirectory(dir=LOCAL_DB.parent) as directory:
        target = Path(directory) / "rollback.sqlite3"
        _copy_from_authority(listing, target)
        target_digest = sha(target)
        target_logical = _logical_sha(target)
        filename_digest = Path(listing).stem.split("-", 1)[-1]
        if target_logical != filename_digest:
            raise RuntimeError("rollback target object logical hash mismatch")
        if (migration["base_generation"] != target_generation
                or migration["base_sha256"] != target_digest
                or migration["base_logical_sha256"] != target_logical):
            raise RuntimeError("migration receipt does not bind the rollback target")
        connection = sqlite3.connect(target)
        try:
            if connection.execute("PRAGMA quick_check").fetchone()[0] != "ok":
                raise RuntimeError("rollback target integrity check failed")
            if migrator._schema_name(connection) != migration["schema_from"]:
                raise RuntimeError("rollback target original schema mismatch")
        finally:
            connection.close()

    manifest = {
        "database": expected["database"],
        "generation": expected["generation"] + 1,
        "sha256": target_digest,
        "logical_sha256": target_logical,
        "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "base_generation": expected["generation"],
        "base_sha256": expected["sha256"],
        "base_logical_sha256": expected["logical_sha256"],
        "rollback_of_generation": target_generation,
        "operation": "rollback",
        "requires_controlled_remigration": True,
        "migration_receipt_id": migration["receipt_id"],
        "migration_receipt_sha256": receipt_digest,
        "restored_schema_version": migration["schema_from"],
        "schema_version": migration["schema_from"],
        "registry_sha256": migration["registry_sha256"],
        "event_head": migration["event_head"],
        "policy_version": migration["policy_version"],
        "source_sha256": migration["source_sha256"],
    }
    manifest.update({key: expected[key] for key in _required_manifest_fields()
                     if key in expected and key not in manifest})
    manifest.update({
        "lease_protocol": LEASE_PROTOCOL_VERSION,
        "fence_token": lease["fence_token"],
        "authority_host_uuid": lease["authority_host_uuid"],
        "authority_boot_id": lease["authority_boot_id"],
        "owner_run_id": lease["owner_run_id"],
        "owner_writer_uuid": lease["owner_writer_uuid"],
        "owner_client_host_uuid": lease["owner_client_host_uuid"],
    })
    object_path = (
        f"{GENERATIONS}/{manifest['generation']:020d}-{target_logical}.sqlite3")
    manifest["object"] = object_path
    manifest["migration_receipt_object"] = (
        f"{GENERATIONS}/{manifest['generation']:020d}-{receipt_digest}.migration.json")
    _validate_manifest(manifest, rollback=True)
    payload = canonical_manifest(manifest)
    script = (
        f"test -f {_remote_q(MANIFEST)} || exit 74; "
        f"actual=$(cat {_remote_q(MANIFEST)}) || exit 74; "
        f"test \"$actual\" = {_remote_q(expected_payload)} || exit 74; "
        f"test -f {_remote_q(listing)} || exit 74; "
        f"test \"$(shasum -a 256 {_remote_q(listing)} | awk '{{print $1}}')\" = "
        f"{_remote_q(target_digest)} || exit 74; "
        f"if test -e {_remote_q(object_path)}; then "
        f"test \"$(shasum -a 256 {_remote_q(object_path)} | awk '{{print $1}}')\" = "
        f"{_remote_q(target_digest)} && "
        f"python3 -c 'import sqlite3,sys; c=sqlite3.connect(sys.argv[1]); "
        "ok=c.execute(\"PRAGMA quick_check\").fetchone()[0]==\"ok\"; "
        "c.close(); raise SystemExit(not ok)' "
        f"{_remote_q(object_path)} || "
        f"{{ rm -f {_remote_q(object_path)}; cp {_remote_q(listing)} {_remote_q(object_path)}; }}; "
        f"else cp {_remote_q(listing)} {_remote_q(object_path)}; fi; "
        f"test \"$(shasum -a 256 {_remote_q(object_path)} | awk '{{print $1}}')\" = "
        f"{_remote_q(target_digest)} || exit 74; "
        + _remote_fsync(object_path)
        + f"test -f {_remote_q(expected['migration_receipt_object'])} || exit 74; "
        + f"test \"$(shasum -a 256 {_remote_q(expected['migration_receipt_object'])} | awk '{{print $1}}')\" = {_remote_q(receipt_digest)} || exit 74; "
        + f"cp {_remote_q(expected['migration_receipt_object'])} {_remote_q(manifest['migration_receipt_object'])}; "
        + _remote_fsync(manifest["migration_receipt_object"])
        + _atomic_remote_copy(
            object_path, REMOTE_DB, f"rollback-{manifest['generation']}")
        + _atomic_remote_json(MANIFEST, payload)
    )
    try:
        _authority_commit(script, lease)
    except subprocess.CalledProcessError as exc:
        raise _cas_conflict(exc) from exc
    base.write_text(payload, encoding="utf-8")
    print(payload)
    return manifest


def published_rollback(target_generation: int, base_receipt: Path | None,
                       migration_receipt: Path | None) -> dict:
    _published_rollback_preflight(target_generation, base_receipt, migration_receipt)
    with authority_lease() as lease:
        with bibliography_writer_lock(LOCAL_DB):
            return _published_rollback_locked(
                target_generation, base_receipt, migration_receipt, lease)

def _published_rollback_preflight(target_generation: int, base_receipt: Path | None,
                                  migration_receipt: Path | None) -> None:
    _ensure_publishable()
    base = base_receipt or LOCAL_DB.with_suffix(".base.json")
    if not base.exists():
        raise RuntimeError("stale/missing base receipt; pull before published rollback")
    try:
        expected = json.loads(base.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError("invalid base receipt") from exc
    _validate_manifest(expected, allow_legacy=True)
    if migration_receipt is None or not migration_receipt.exists():
        raise RuntimeError("published rollback requires a migration receipt")
    try:
        migration = json.loads(migration_receipt.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError("invalid migration receipt") from exc
    if target_generation < 0 or target_generation >= expected["generation"]:
        raise RuntimeError("rollback target must be an older retained generation")
    _verify_migration_audit(migration, expected, LOCAL_DB)

def _cli_affiliation_artifacts(args) -> dict[str, Path] | None:
    values = {
        role: getattr(args, role.replace("_", "-").replace("-", "_"))
        for role in AFFILIATION_ARTIFACT_ROLES
    }
    present = {role: path for role, path in values.items() if path is not None}
    return None if not present else _artifact_destinations(present)


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--pull", action="store_true")
    group.add_argument("--push", action="store_true")
    group.add_argument("--status", action="store_true")
    group.add_argument("--bootstrap", action="store_true")
    group.add_argument("--rollback-generation", type=int)
    group.add_argument("--seed-legacy-recovery", action="store_true")
    parser.add_argument("--base-receipt", type=Path)
    parser.add_argument("--migration-receipt", type=Path)
    parser.add_argument("--cohort", type=Path)
    parser.add_argument("--decisions", type=Path)
    parser.add_argument("--ledger", type=Path)
    parser.add_argument("--generation-descriptor", type=Path)
    args = parser.parse_args()
    try:
        if args.pull:
            pull(_cli_affiliation_artifacts(args))
        elif args.push:
            push(args.base_receipt, _cli_affiliation_artifacts(args))
        elif args.rollback_generation is not None:
            published_rollback(
                args.rollback_generation, args.base_receipt,
                args.migration_receipt)
        elif args.seed_legacy_recovery:
            seed_legacy_recovery(args.base_receipt)
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