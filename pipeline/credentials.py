#!/usr/bin/env python3
"""Private subprocess interface for shared OS-keyring credentials.

The ``read`` operation is only for a parent process's private pipe.  Its
stdout must never be relayed to an interactive UI or a log.
"""

from __future__ import annotations

import argparse
import json
import sys

try:  # Script execution: ``python pipeline/credentials.py``.
    from lib.credentials import (
        CredentialNotConfigured,
        CredentialsError,
        credential_status,
        delete_credential,
        resolve_credential,
        store_credential,
    )
except ModuleNotFoundError:  # Package import in tests and Curio.
    from pipeline.lib.credentials import (
        CredentialNotConfigured,
        CredentialsError,
        credential_status,
        delete_credential,
        resolve_credential,
        store_credential,
    )

_MAX_STDIN_BYTES = 16384


def _write_value() -> str:
    data = sys.stdin.buffer.read(_MAX_STDIN_BYTES + 1)
    if len(data) > _MAX_STDIN_BYTES:
        raise CredentialsError("credential input is too large")
    try:
        value = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise CredentialsError("credential input must be UTF-8") from exc
    return value


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Private OS-keyring credential IPC")
    parser.add_argument("--operation", required=True, choices=("status", "read", "write", "delete"))
    parser.add_argument("--provider", required=True)
    args = parser.parse_args(argv)
    try:
        if args.operation == "status":
            output = credential_status(args.provider)
        elif args.operation == "read":
            try:
                value = resolve_credential(args.provider)
            except CredentialNotConfigured:
                value = ""
            output = {"reference": f"credential:{args.provider}", "value": value}
        elif args.operation == "write":
            output = {"reference": store_credential(args.provider, _write_value())}
        else:
            delete_credential(args.provider)
            output = {"reference": f"credential:{args.provider}", "deleted": True}
        print(json.dumps(output, separators=(",", ":")))
        return 0
    except CredentialsError as exc:
        # Do not include arguments, input, backend exception text, or values.
        print(json.dumps({"error": type(exc).__name__}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
