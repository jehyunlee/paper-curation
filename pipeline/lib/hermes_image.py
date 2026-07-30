"""Hermes gateway diagram/timeline image generation.

Prefer this over PaperBanana→vendor image APIs. The Hermes tunnel
(``HERMES_GATEWAY_BASE_URL``, typically ``http://localhost:8642/v1``) is
OpenAI-compatible; images may arrive as multimodal ``message.images``,
markdown ``data:image/...;base64,...`` / URL, or via ``/images/generations``.
"""
from __future__ import annotations

import base64
import json
import logging
import re
import ssl
import urllib.error
import urllib.request
from io import BytesIO
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin

logger = logging.getLogger(__name__)

try:
    from config_loader import get_hermes_config
except ImportError:  # pragma: no cover
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from config_loader import get_hermes_config

_SSL_CTX = ssl.create_default_context()
_SSL_CTX.check_hostname = False
_SSL_CTX.verify_mode = ssl.CERT_NONE

_DATA_URI_RE = re.compile(
    r"data:image/(png|jpeg|jpg|webp|gif);base64,([A-Za-z0-9+/=\s]+)",
    re.IGNORECASE,
)
_MD_IMG_RE = re.compile(
    r"!\[[^\]]*\]\((data:image/[^)]+|https?://[^)\s]+)\)",
    re.IGNORECASE,
)
_URL_RE = re.compile(r"https?://[^\s)\"']+\.(?:png|jpe?g|webp|gif)", re.I)


def available() -> bool:
    return get_hermes_config() is not None


def _headers(cfg: dict) -> dict:
    return {
        "Authorization": f"Bearer {cfg['api_key']}",
        "Content-Type": "application/json",
    }


def _post(cfg: dict, path: str, payload: dict) -> dict | bytes:
    base = cfg["base_url"].rstrip("/") + "/"
    url = urljoin(base, path.lstrip("/"))
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url, data=data, headers=_headers(cfg), method="POST")
    with urllib.request.urlopen(
            req, timeout=float(cfg.get("timeout") or 300),
            context=_SSL_CTX) as resp:
        ctype = (resp.headers.get("Content-Type") or "").lower()
        raw = resp.read()
        if "application/json" in ctype or raw[:1] in (b"{", b"["):
            return json.loads(raw.decode("utf-8"))
        return raw


def _to_png_bytes(raw: bytes) -> bytes:
    from PIL import Image
    img = Image.open(BytesIO(raw))
    buf = BytesIO()
    img.save(buf, "PNG")
    return buf.getvalue()


def _decode_b64(s: str) -> bytes | None:
    s = (s or "").strip()
    if not s:
        return None
    if "," in s and s.lower().startswith("data:"):
        s = s.split(",", 1)[1]
    s = re.sub(r"\s+", "", s)
    try:
        return base64.b64decode(s, validate=False)
    except Exception:
        return None


def _fetch_url(url: str, timeout: float = 60.0) -> bytes | None:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "paper-curation"})
        with urllib.request.urlopen(req, timeout=timeout, context=_SSL_CTX) as resp:
            return resp.read()
    except Exception as e:
        logger.warning("Hermes image URL fetch failed: %s", e)
        return None


def _extract_from_part(part: dict) -> bytes | None:
    if not isinstance(part, dict):
        return None
    # OpenAI-style image_url
    img = part.get("image_url") or part.get("imageUrl")
    if isinstance(img, dict):
        url = img.get("url") or ""
    elif isinstance(img, str):
        url = img
    else:
        url = ""
    if url.startswith("data:"):
        raw = _decode_b64(url)
        return _to_png_bytes(raw) if raw else None
    if url.startswith("http"):
        raw = _fetch_url(url)
        return _to_png_bytes(raw) if raw else None
    # Inline b64 fields
    for key in ("b64_json", "base64", "data", "image_base64"):
        if part.get(key):
            raw = _decode_b64(str(part[key]))
            if raw:
                return _to_png_bytes(raw)
    # Anthropic-ish source block
    src = part.get("source") or {}
    if isinstance(src, dict) and src.get("data"):
        raw = _decode_b64(str(src["data"]))
        if raw:
            return _to_png_bytes(raw)
    return None


def extract_image_bytes(response: dict | bytes) -> bytes | None:
    """Pull PNG bytes out of a Hermes/OpenAI-style chat or images response."""
    if isinstance(response, (bytes, bytearray)):
        try:
            return _to_png_bytes(bytes(response))
        except Exception:
            return None

    # /images/generations shape
    for item in response.get("data") or []:
        if not isinstance(item, dict):
            continue
        if item.get("b64_json"):
            raw = _decode_b64(item["b64_json"])
            if raw:
                return _to_png_bytes(raw)
        if item.get("url"):
            raw = _fetch_url(item["url"])
            if raw:
                return _to_png_bytes(raw)

    choice = (response.get("choices") or [{}])[0]
    msg = choice.get("message") or response.get("message") or {}

    # Explicit images array (some gateways)
    for img in msg.get("images") or response.get("images") or []:
        got = _extract_from_part(img if isinstance(img, dict)
                                 else {"image_url": img})
        if got:
            return got

    content = msg.get("content")
    if isinstance(content, list):
        for part in content:
            got = _extract_from_part(part if isinstance(part, dict) else {})
            if got:
                return got
            if isinstance(part, dict) and part.get("type") == "text":
                got = _extract_from_text(part.get("text") or "")
                if got:
                    return got
    elif isinstance(content, str):
        got = _extract_from_text(content)
        if got:
            return got

    return None


def _extract_from_text(text: str) -> bytes | None:
    if not text:
        return None
    m = _DATA_URI_RE.search(text)
    if m:
        raw = _decode_b64(m.group(2))
        if raw:
            return _to_png_bytes(raw)
    m = _MD_IMG_RE.search(text)
    if m:
        target = m.group(1)
        if target.startswith("data:"):
            raw = _decode_b64(target)
            if raw:
                return _to_png_bytes(raw)
        raw = _fetch_url(target)
        if raw:
            return _to_png_bytes(raw)
    m = _URL_RE.search(text)
    if m:
        raw = _fetch_url(m.group(0))
        if raw:
            return _to_png_bytes(raw)
    # Bare base64 blob (long)
    compact = re.sub(r"\s+", "", text.strip())
    if len(compact) > 200 and re.fullmatch(r"[A-Za-z0-9+/=]+", compact or ""):
        raw = _decode_b64(compact)
        if raw and (raw[:8] == b"\x89PNG\r\n\x1a\n" or raw[:2] == b"\xff\xd8"):
            try:
                return _to_png_bytes(raw)
            except Exception:
                pass
    return None


def _build_prompt(method: str, caption: str, aspect_ratio: str) -> str:
    return (
        "Generate a single clean academic diagram image (PNG). "
        "No explanatory text outside the figure. "
        f"Aspect ratio: {aspect_ratio}.\n\n"
        f"Caption / visual intent: {caption}\n\n"
        f"Diagram content (markdown):\n{method}\n\n"
        "Return the image only (as an image attachment or a "
        "markdown data:image/png;base64,... image)."
    )


def generate_diagram(method: str, caption: str,
                     aspect_ratio: str = "16:9",
                     output_path: str | Path | None = None,
                     cfg: dict | None = None) -> Optional[bytes]:
    """Generate a diagram via Hermes. Returns PNG bytes or None."""
    cfg = cfg or get_hermes_config()
    if not cfg:
        return None

    prompt = _build_prompt(method, caption, aspect_ratio)
    model = cfg.get("model") or "hermes-agent"

    # 1) Try images API if present
    png: bytes | None = None
    try:
        img_resp = _post(cfg, "images/generations", {
            "model": model,
            "prompt": prompt,
            "n": 1,
            "size": "1792x1024" if aspect_ratio.startswith("16") else "1024x1024",
            "response_format": "b64_json",
        })
        png = extract_image_bytes(img_resp)
    except Exception as e:
        logger.info("Hermes /images/generations unavailable (%s); trying chat", e)

    # 2) Chat completions multimodal
    if png is None:
        try:
            chat_resp = _post(cfg, "chat/completions", {
                "model": model,
                "max_tokens": 4096,
                "messages": [
                    {"role": "system",
                     "content": "You are an academic diagram generator. "
                                "Always respond with an image."},
                    {"role": "user", "content": prompt},
                ],
            })
            png = extract_image_bytes(chat_resp)
        except Exception as e:
            logger.warning("Hermes chat image generation failed: %s", e)
            return None

    if not png:
        logger.warning("Hermes returned no extractable image")
        return None

    if output_path is not None:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(png)
        logger.info("Hermes diagram saved: %s", out)
    return png


__all__ = ["available", "generate_diagram", "extract_image_bytes"]
