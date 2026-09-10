"""Shared OS-keyring credentials for Paper Curation.

Secrets may come from the documented environment variables or from the OS
keyring.  This module intentionally has no file/config fallback.
"""

from __future__ import annotations

import os
from collections.abc import Mapping
from typing import Any

SERVICE_NAME = "paper-curation"
REFERENCE_PREFIX = "credential:"
_NATIVE_BACKEND_MODULES = (
    "keyring.backends.macos",
    "keyring.backends.windows",
    "keyring.backends.secretservice",
    "keyring.backends.kwallet",
)

_PROVIDER_ENV_NAMES = {
    "anthropic": ("ANTHROPIC_API_KEY",),
    "openai": ("OPENAI_API_KEY",),
    "google": ("GOOGLE_API_KEY", "GEMINI_API_KEY"),
    "resend": ("RESEND_API_KEY",),
    "zotero": ("ZOTERO_API_KEY",),
    "scopus": ("SCOPUS_API_KEY", "ELSEVIER_API_KEY"),
    "scopus-inst": ("SCOPUS_INST_TOKEN",),
    "semantic-scholar": ("S2_API_KEY",),
    "springer": (
        "SPRINGER_META_API_KEY",
        "NATURESPRINGERMETA_API_KEY",
        "NATURESPRINTERMETA_API_KEY",
    ),
    "cloudflare": ("CLOUDFLARE_API_TOKEN", "CF_API_TOKEN"),
    "cloudflare-account": ("CLOUDFLARE_ACCOUNT_ID",),
}


class CredentialsError(RuntimeError):
    """A safe credential error: its text never contains a credential value."""


class CredentialNotConfigured(CredentialsError):
    """The requested provider has no environment or keyring value."""


def _provider(provider: str) -> str:
    if not isinstance(provider, str) or provider not in _PROVIDER_ENV_NAMES:
        raise CredentialsError("unsupported credential provider")
    return provider


def _reference(provider: str, credential_ref: str | None = None) -> str:
    provider = _provider(provider)
    reference = f"{REFERENCE_PREFIX}{provider}"
    if credential_ref is not None and credential_ref != reference:
        raise CredentialsError("invalid credential reference")
    return reference


def _keyring() -> Any:
    try:
        import keyring
    except ImportError as exc:
        raise CredentialsError("OS keyring support is unavailable") from exc

    try:
        backend = keyring.get_keyring()
    except Exception as exc:
        raise CredentialsError("OS keyring backend is unavailable") from exc

    backend_type = type(backend)
    module = backend_type.__module__.lower()
    name = backend_type.__name__.lower()
    # Only the native, OS-protected keyring implementations are acceptable.
    # In particular, ChainerBackend can conceal keyrings.alt/file backends;
    # custom backends cannot establish an equivalent security guarantee.
    if not module.startswith(_NATIVE_BACKEND_MODULES):
        raise CredentialsError("OS keyring backend is unavailable or insecure")
    return keyring


def _environment_value(provider: str, environ: Mapping[str, str]) -> str:
    for name in _PROVIDER_ENV_NAMES[provider]:
        value = environ.get(name, "")
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


def resolve_credential(
    provider: str, credential_ref: str | None = None, environ: Mapping[str, str] | None = None
) -> str:
    """Return a credential from fixed environment aliases, then the OS keyring."""
    provider = _provider(provider)
    _reference(provider, credential_ref)
    value = _environment_value(provider, os.environ if environ is None else environ)
    if value:
        return value
    try:
        value = _keyring().get_password(SERVICE_NAME, provider)
    except CredentialsError:
        raise
    except Exception as exc:
        raise CredentialsError("OS keyring lookup failed") from exc
    if isinstance(value, str) and value:
        return value
    raise CredentialNotConfigured("credential is not configured")


def store_credential(provider: str, value: str) -> str:
    """Store a credential in the configured OS keyring and return its reference."""
    provider = _provider(provider)
    if not isinstance(value, str) or not value or len(value) > 16384:
        raise CredentialsError("invalid credential value")
    try:
        _keyring().set_password(SERVICE_NAME, provider, value)
    except CredentialsError:
        raise
    except Exception as exc:
        raise CredentialsError("OS keyring write failed") from exc
    return _reference(provider)


def delete_credential(provider: str) -> None:
    """Delete exactly this provider's OS-keyring entry."""
    provider = _provider(provider)
    try:
        _keyring().delete_password(SERVICE_NAME, provider)
    except CredentialsError:
        raise
    except Exception as exc:
        raise CredentialsError("OS keyring delete failed") from exc


def credential_status(provider: str) -> dict[str, object]:
    """Return non-secret diagnostic metadata for one fixed provider."""
    provider = _provider(provider)
    reference = _reference(provider)
    if _environment_value(provider, os.environ):
        return {"reference": reference, "configured": True, "source": "environment", "status": "configured"}
    try:
        value = _keyring().get_password(SERVICE_NAME, provider)
    except CredentialsError:
        return {"reference": reference, "configured": False, "source": "keyring", "status": "unavailable"}
    except Exception:
        return {"reference": reference, "configured": False, "source": "keyring", "status": "unavailable"}
    return {
        "reference": reference,
        "configured": bool(value),
        "source": "keyring" if value else "none",
        "status": "configured" if value else "not-configured",
    }
