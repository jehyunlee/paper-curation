#!/usr/bin/env python3
"""CAS synchronize immutable bibliography DB generations over SSH."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shlex
import socket
import sqlite3
import subprocess
import tempfile
import time
import uuid
import sys
from pathlib import Path
import repair_bibliography_institutions as migrator

ROOT = Path(__file__).resolve().parents[1]
LOCAL_DB = ROOT / ".cache/bibliography.sqlite3"
HOST = os.environ.get("PAPER_CURATION_DB_HOST", "macmini-cf")
REMOTE_DB = os.environ.get("PAPER_CURATION_DB_REMOTE",
                           "/Users/jehyunlee/Documents/paper-curation/.cache/bibliography.sqlite3")
MANIFEST = REMOTE_DB + ".manifest.json"
LOCK = REMOTE_DB + ".publish.lock"
GENERATIONS = REMOTE_DB + ".generations"


def run(cmd, *, capture=False):
    return subprocess.run(cmd, check=True, text=True, capture_output=capture)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def remote(command, capture=False):
    return run(["ssh", HOST, command], capture=capture)


def canonical_manifest(manifest: dict) -> str:
    return json.dumps(manifest, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _local_affiliation_metadata() -> dict:
    return _inspect_sqlite(LOCAL_DB, require_affiliation=False)


def _required_manifest_fields(*, rollback: bool = False) -> set[str]:
    fields = {
        "database", "generation", "sha256", "logical_sha256", "schema_version",
        "registry_sha256", "event_head", "policy_version", "source_sha256",
        "migration_receipt_id", "updated_at", "object",
    }
    if rollback:
        fields |= {
            "base_generation", "base_sha256", "base_logical_sha256",
            "migration_receipt_id", "migration_receipt_sha256",
            "restored_schema_version", "requires_controlled_remigration",
        }
    return fields


def _validate_manifest(manifest: dict, *, rollback: bool = False) -> None:
    if not isinstance(manifest, dict):
        raise RuntimeError("manifest is invalid")
    missing = sorted(key for key in _required_manifest_fields(rollback=rollback)
                     if manifest.get(key) in (None, ""))
    if missing:
        raise RuntimeError("manifest lacks required provenance: " + ",".join(missing))
    if not isinstance(manifest["generation"], int) or manifest["generation"] < 0:
        raise RuntimeError("manifest generation is invalid")
    if manifest["object"] != (
            f"{GENERATIONS}/{manifest['generation']:020d}-{manifest['logical_sha256']}.sqlite3"):
        raise RuntimeError("manifest immutable object name mismatch")


def _inspect_sqlite(path: Path, *, require_affiliation: bool) -> dict:
    connection = sqlite3.connect(path)
    try:
        if connection.execute("PRAGMA quick_check").fetchone()[0] != "ok":
            raise RuntimeError(f"SQLite integrity check failed: {path}")
        try:
            row = connection.execute(
                "SELECT schema_version,registry_sha256,event_head,policy_version,"
                "source_sha256,migration_receipt_id FROM "
                "affiliation_registry_metadata WHERE singleton=1"
            ).fetchone()
        except sqlite3.Error:
            row = None
    finally:
        connection.close()
    if require_affiliation and (
            row is None or row[0] != "affiliation-2" or not all(row[1:5])
            or not row[5]):
        raise RuntimeError("affiliation-2 metadata is missing from bibliography DB")
    return {} if row is None else {
        "schema_version": row[0], "registry_sha256": row[1],
        "event_head": row[2], "policy_version": row[3],
        "source_sha256": row[4], "migration_receipt_id": row[5],
    }


def _remote_bootstrap_metadata() -> dict:
    program = (
        "import json,sqlite3,sys;"
        "from pathlib import Path;"
        "sys.path.insert(0,str(Path(sys.argv[1]).parent.parent/'pipeline'));"
        "import repair_bibliography_institutions as m;"
        "c=sqlite3.connect(sys.argv[1]);"
        "ok=c.execute('PRAGMA quick_check').fetchone()[0];"
        "r=c.execute('SELECT schema_version,registry_sha256,event_head,policy_version,"
        "source_sha256,migration_receipt_id FROM affiliation_registry_metadata "
        "WHERE singleton=1').fetchone();"
        "logical=m.logical_digest(c);c.close();"
        "assert ok=='ok' and r and r[0]=='affiliation-2' and all(r[1:]);"
        "print(json.dumps({'schema_version':r[0],'registry_sha256':r[1],"
        "'event_head':r[2],'policy_version':r[3],'source_sha256':r[4],"
        "'migration_receipt_id':r[5],'logical_sha256':logical},"
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
            "cannot bootstrap: remote DB failed affiliation-2 validation"
        ) from exc
    if metadata.get("schema_version") != "affiliation-2" or not all(
            metadata.get(key) for key in (
                "registry_sha256", "event_head", "policy_version",
                "source_sha256", "migration_receipt_id", "logical_sha256")):
        raise RuntimeError("cannot bootstrap: remote DB has invalid affiliation metadata")
    return metadata


def _remigration_marker() -> Path:
    return LOCAL_DB.with_suffix(LOCAL_DB.suffix + ".remigration-required.json")


def _ensure_publishable() -> None:
    marker = _remigration_marker()
    if marker.exists():
        raise RuntimeError("remigration required before bibliography synchronization")
    if not LOCAL_DB.exists():
        raise RuntimeError(f"missing local DB: {LOCAL_DB}")
    metadata = _local_affiliation_metadata()
    if (metadata.get("schema_version") != "affiliation-2" or not all(
            metadata.get(key) for key in (
                "registry_sha256", "event_head", "policy_version",
                "source_sha256", "migration_receipt_id"))):
        raise RuntimeError("affiliation-2 metadata is missing; migrate and validate before push")
    checker = ROOT / "pipeline" / "check_bibliography_db.py"
    try:
        run([sys.executable, str(checker), "--db", str(LOCAL_DB), "--strict"])
    except subprocess.CalledProcessError as exc:
        raise RuntimeError("strict bibliography validation failed; push blocked") from exc


def _ensure_pull_allowed() -> None:
    if _remigration_marker().exists():
        raise RuntimeError("remigration required before bibliography synchronization")


def _logical_sha(path: Path) -> str:
    connection = sqlite3.connect(path)
    try:
        return migrator.logical_digest(connection)
    finally:
        connection.close()


def local_manifest() -> dict:
    metadata = _inspect_sqlite(LOCAL_DB, require_affiliation=True)
    return {
        "database": LOCAL_DB.name,
        "generation": 0,
        "sha256": sha(LOCAL_DB),
        "logical_sha256": _logical_sha(LOCAL_DB),
        "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        **metadata,
    }


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


def _verify_migration_audit(receipt: dict, manifest: dict) -> None:
    """Bind published rollback to the DB's immutable migration audit."""
    connection = sqlite3.connect(LOCAL_DB)
    try:
        row = connection.execute(
            "SELECT operation,base_generation,base_logical_sha256,"
            "result_logical_sha256,registry_sha256,schema_from,schema_to,report_json "
            "FROM affiliation_migration_audit WHERE receipt_id=?",
            (receipt["receipt_id"],),
        ).fetchone()
    except sqlite3.Error as exc:
        raise RuntimeError("current bibliography DB lacks migration audit") from exc
    finally:
        connection.close()
    if row is None:
        raise RuntimeError("migration receipt is absent from current DB audit")
    operation, generation, base_logical, result_logical, registry, schema_from, schema_to, report = row
    if (operation != "migrate" or generation != receipt["base_generation"]
            or base_logical != receipt["base_logical_sha256"]
            or result_logical != receipt["result_logical_sha256"]
            or registry != receipt["registry_sha256"]
            or schema_from != receipt["schema_from"] or schema_to != receipt["schema_to"]):
        raise RuntimeError("migration receipt does not match current DB audit")
    try:
        audited = json.loads(report)
    except json.JSONDecodeError as exc:
        raise RuntimeError("current DB migration audit is invalid") from exc
    if (audited.get("receipt_id") != receipt["receipt_id"]
            or any(audited.get(key) != receipt[key] for key in (
                "base_generation", "base_sha256", "base_logical_sha256",
                "registry_sha256", "event_head", "policy_version",
                "source_sha256", "schema_from", "schema_to"))):
        raise RuntimeError("current DB migration audit receipt mismatch")


def bootstrap():
    """Create generation zero only if remote DB and manifest are still unchanged."""
    digest = remote(
        f"test -f {_remote_q(REMOTE_DB)} && shasum -a 256 {_remote_q(REMOTE_DB)} | awk '{{print $1}}'",
        capture=True,
    ).stdout.strip()
    if not digest:
        raise RuntimeError("cannot bootstrap: remote bibliography DB is missing")
    metadata = _remote_bootstrap_metadata()
    manifest = {"database": Path(REMOTE_DB).name, "generation": 0, "sha256": digest,
                "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "object": f"{GENERATIONS}/{0:020d}-{metadata['logical_sha256']}.sqlite3",
                **metadata}
    _validate_manifest(manifest)
    payload = canonical_manifest(manifest)
    generation = manifest["object"]
    script = (
        f"mkdir {_remote_q(LOCK)} || exit 75; trap 'rmdir {_remote_q(LOCK)}' EXIT; "
        f"test ! -e {_remote_q(MANIFEST)} || exit 74; "
        f"test \"$(shasum -a 256 {_remote_q(REMOTE_DB)} | awk '{{print $1}}')\" = {_remote_q(digest)} || exit 74; "
        f"mkdir -p {_remote_q(GENERATIONS)}; "
        f"if test -e {_remote_q(generation)}; then "
        f"test \"$(shasum -a 256 {_remote_q(generation)} | awk '{{print $1}}')\" = {_remote_q(digest)} "
        f"&& python3 -c 'import sqlite3,sys; c=sqlite3.connect(sys.argv[1]); "
        "ok=c.execute(\"PRAGMA quick_check\").fetchone()[0]==\"ok\"; c.close(); raise SystemExit(not ok)' "
        f"{_remote_q(generation)} || {{ rm -f {_remote_q(generation)}; cp {_remote_q(REMOTE_DB)} {_remote_q(generation)}; }}; "
        f"else cp {_remote_q(REMOTE_DB)} {_remote_q(generation)}; fi; "
        f"test \"$(shasum -a 256 {_remote_q(generation)} | awk '{{print $1}}')\" = {_remote_q(digest)} || exit 74; "
        + _remote_fsync(generation)
        + _atomic_remote_json(MANIFEST, payload)
    )
    try:
        remote(script)
    except subprocess.CalledProcessError as exc:
        raise RuntimeError("bootstrap conflict or remote publish lock busy") from exc
    print(canonical_manifest(manifest))
    return manifest


def pull():
    _ensure_pull_allowed()
    LOCAL_DB.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=LOCAL_DB.parent) as directory:
        db, mf = Path(directory) / "db", Path(directory) / "manifest"
        run(["scp", "-q", HOST + ":" + MANIFEST, str(mf)])
        raw_manifest = mf.read_text(encoding="utf-8")
        manifest = json.loads(raw_manifest)
        if raw_manifest != canonical_manifest(manifest):
            raise RuntimeError("remote manifest is not canonical")
        rollback = bool(manifest.get("requires_controlled_remigration"))
        _validate_manifest(manifest, rollback=rollback)
        remote_object = manifest["object"]
        run(["scp", "-q", HOST + ":" + remote_object, str(db)])
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
        os.replace(db, LOCAL_DB)
        LOCAL_DB.with_suffix(".base.json").write_text(
            canonical_manifest(manifest), encoding="utf-8")
        marker = _remigration_marker()
        if manifest.get("requires_controlled_remigration"):
            marker.write_text(canonical_manifest({
                "operation": "remigration_required",
                "manifest_generation": manifest.get("generation"),
                "migration_receipt_id": manifest.get("migration_receipt_id"),
                "created_at": manifest.get("updated_at"),
            }), encoding="utf-8")
        else:
            marker.unlink(missing_ok=True)
    print(canonical_manifest(manifest))
    return manifest


def push(base_receipt: Path | None):
    _ensure_publishable()
    if not LOCAL_DB.exists():
        raise RuntimeError(f"missing local DB: {LOCAL_DB}")
    base = base_receipt or LOCAL_DB.with_suffix(".base.json")
    if not base.exists():
        raise RuntimeError("stale/missing base receipt; pull before push")
    try:
        expected = json.loads(base.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError("invalid base receipt") from exc
    _validate_manifest(expected, rollback=bool(
        expected.get("requires_controlled_remigration")))
    if expected.get("requires_controlled_remigration"):
        raise RuntimeError("remigration required before bibliography synchronization")
    expected_payload = canonical_manifest(expected)
    upload = REMOTE_DB + ".upload." + uuid.uuid4().hex
    manifest = local_manifest()
    manifest["generation"] = expected["generation"] + 1
    manifest["base_generation"] = expected["generation"]
    manifest["base_sha256"] = expected["sha256"]
    manifest["base_logical_sha256"] = expected["logical_sha256"]
    manifest["object"] = (
        f"{GENERATIONS}/{manifest['generation']:020d}-{manifest['logical_sha256']}.sqlite3")
    _validate_manifest(manifest)
    payload = canonical_manifest(manifest)
    run(["scp", "-q", str(LOCAL_DB), HOST + ":" + upload])
    object_path = manifest["object"]
    script = (
        f"mkdir {_remote_q(LOCK)} || exit 75; trap 'rmdir {_remote_q(LOCK)}' EXIT; "
        f"test -f {_remote_q(MANIFEST)} || exit 74; "
        f"actual=$(cat {_remote_q(MANIFEST)}) || exit 74; "
        f"test \"$actual\" = {_remote_q(expected_payload)} || exit 74; "
        f"test \"$(shasum -a 256 {_remote_q(upload)} | awk '{{print $1}}')\" = {_remote_q(manifest['sha256'])} || exit 74; "
        f"python3 -c 'import sqlite3,sys; c=sqlite3.connect(sys.argv[1]); "
        "ok=c.execute(\"PRAGMA quick_check\").fetchone()[0]==\"ok\"; c.close(); raise SystemExit(not ok)' "
        f"{_remote_q(upload)} || exit 74; "
        f"mkdir -p {_remote_q(GENERATIONS)}; "
        f"if test -e {_remote_q(object_path)}; then "
        f"test \"$(shasum -a 256 {_remote_q(object_path)} | awk '{{print $1}}')\" = {_remote_q(manifest['sha256'])} "
        f"&& python3 -c 'import sqlite3,sys; c=sqlite3.connect(sys.argv[1]); "
        "ok=c.execute(\"PRAGMA quick_check\").fetchone()[0]==\"ok\"; c.close(); raise SystemExit(not ok)' "
        f"{_remote_q(object_path)} && rm -f {_remote_q(upload)} || "
        f"{{ rm -f {_remote_q(object_path)}; mv {_remote_q(upload)} {_remote_q(object_path)}; }}; "
        f"else mv {_remote_q(upload)} {_remote_q(object_path)}; fi; "
        f"test \"$(shasum -a 256 {_remote_q(object_path)} | awk '{{print $1}}')\" = {_remote_q(manifest['sha256'])} || exit 74; "
        + _remote_fsync(object_path)
        + _atomic_remote_json(MANIFEST, payload)
    )
    try:
        remote(script)
    except subprocess.CalledProcessError as exc:
        try:
            remote(f"rm -f {_remote_q(upload)}")
        except subprocess.CalledProcessError:
            pass
        raise RuntimeError("CAS conflict or remote publish lock busy") from exc
    base.write_text(payload, encoding="utf-8")
    print(payload)
    return manifest


def published_rollback(target_generation: int, base_receipt: Path | None,
                       migration_receipt: Path | None) -> dict:
    """Publish a retained generation as a new monotonic generation under CAS."""
    _ensure_publishable()
    base = base_receipt or LOCAL_DB.with_suffix(".base.json")
    if not base.exists():
        raise RuntimeError("stale/missing base receipt; pull before published rollback")
    try:
        expected = json.loads(base.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError("invalid base receipt") from exc
    _validate_manifest(expected)
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
    receipt_digest = hashlib.sha256(migration_receipt.read_bytes()).hexdigest()
    if (migration["operation"] != "migrate"
            or migration["receipt_id"] != expected["migration_receipt_id"]
            or migration["result_sha256"] != expected["sha256"]
            or migration["result_logical_sha256"] != expected["logical_sha256"]
            or migration["schema_to"] != expected["schema_version"]
            or any(migration[key] != expected[key] for key in (
                "registry_sha256", "event_head", "policy_version", "source_sha256"))):
        raise RuntimeError("migration receipt does not bind the current generation")
    if target_generation < 0 or target_generation >= expected["generation"]:
        raise RuntimeError("rollback target must be an older retained generation")
    _verify_migration_audit(migration, expected)

    listing = remote(
        f"set -- {_remote_q(GENERATIONS)}/{target_generation:020d}-*.sqlite3; "
        "test \"$#\" -eq 1 && test -f \"$1\" && printf '%s' \"$1\"",
        capture=True,
    ).stdout.strip()
    if not listing:
        raise RuntimeError("rollback target generation is missing or ambiguous")

    with tempfile.TemporaryDirectory(dir=LOCAL_DB.parent) as directory:
        target = Path(directory) / "rollback.sqlite3"
        run(["scp", "-q", HOST + ":" + listing, str(target)])
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
    object_path = (
        f"{GENERATIONS}/{manifest['generation']:020d}-{target_logical}.sqlite3")
    manifest["object"] = object_path
    _validate_manifest(manifest, rollback=True)
    payload = canonical_manifest(manifest)
    script = (
        f"mkdir {_remote_q(LOCK)} || exit 75; trap 'rmdir {_remote_q(LOCK)}' EXIT; "
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
        + _atomic_remote_json(MANIFEST, payload)
    )
    try:
        remote(script)
    except subprocess.CalledProcessError as exc:
        raise RuntimeError("published rollback CAS conflict or remote publish lock busy") from exc
    base.write_text(payload, encoding="utf-8")
    print(payload)
    return manifest


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--pull", action="store_true")
    group.add_argument("--push", action="store_true")
    group.add_argument("--status", action="store_true")
    group.add_argument("--bootstrap", action="store_true")
    group.add_argument("--rollback-generation", type=int)
    parser.add_argument("--base-receipt", type=Path)
    parser.add_argument("--migration-receipt", type=Path)
    args = parser.parse_args()
    try:
        if args.pull:
            pull()
        elif args.push:
            push(args.base_receipt)
        elif args.rollback_generation is not None:
            published_rollback(
                args.rollback_generation, args.base_receipt,
                args.migration_receipt)
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