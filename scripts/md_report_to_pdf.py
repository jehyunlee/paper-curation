#!/usr/bin/env python3
"""Render a styled Markdown policy report to PDF via headless Edge (Chromium DevTools).

The report Markdown may mix plain Markdown with raw HTML (cover ``<section class="cover">``,
``<span class="en-sub">`` heading subtitles, recommendation boxes, and notes).
The renderer loads an editable external CSS file and drives Edge's ``Page.printToPDF``
over the DevTools Protocol, preserving linked superscript citations and real
``N / total`` page-number footers.

Usage:
    python scripts/generate_report.py reports/source/report.md
    python scripts/generate_report.py report.md --css reports/styles/policy-report.css
"""
from __future__ import annotations

import argparse
import asyncio
import base64
import itertools
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

import markdown as md_lib

PROJECT_ROOT = Path(__file__).resolve().parent.parent
EDGE = "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
DEFAULT_CSS = PROJECT_ROOT / "reports" / "styles" / "policy-report.css"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "reports" / "output"
DEFAULT_BUILD_DIR = PROJECT_ROOT / "reports" / "build"


FOOTER = (
    '<div style="width:100%;font-size:8px;color:#9a9a9a;text-align:center;'
    'font-family:sans-serif;padding-top:2px;">'
    '<span class="pageNumber"></span> / <span class="totalPages"></span></div>'
)


def validate_report_source(md_text: str) -> list[str]:
    """Return structural errors that would silently degrade the policy-report layout."""
    errors: list[str] = []
    stripped = md_text.lstrip()
    if not stripped.startswith('<section class="cover">'):
        errors.append(
            'the document must start with <section class="cover"> '
            '(copy reports/source/report-template.md)'
        )
    if "</section>" not in stripped:
        errors.append("the cover section is not closed with </section>")
    # Only the title and subtitle are load-bearing; kind/org/date are optional so
    # authors can compose lighter, personal cover pages.
    for class_name in ("c-title", "c-subtitle"):
        if f'class="{class_name}"' not in md_text:
            errors.append(f'missing required cover class "{class_name}"')
    return errors


def build_html(md_text: str, title: str, css: str) -> str:
    # Standalone "✦" lines (outside the cover HTML) become styled ornaments.
    md_text = re.sub(r"(?m)^✦\s*$", '<p class="sec-orn">✦</p>', md_text)
    # "※ ..." note lines become styled callouts.
    md_text = re.sub(r"(?m)^(※\s.*)$", r'<p class="note">\1</p>', md_text)
    # In-text numeric citations become linked superscripts. Reference entries receive
    # matching anchors after the document is split, so links survive Chromium PDF export.

    extensions = ["extra", "sane_lists", "md_in_html"]
    ref_marker = "## 참고문헌"
    if ref_marker in md_text:
        head, refs = md_text.split(ref_marker, 1)
        head = re.sub(
            r"\[(\d+)\]",
            r'<sup class="citation"><a href="#ref-\1" aria-label="참고문헌 \1">\1</a></sup>',
            head,
        )
        refs = re.sub(
            r"(?m)^\[(\d+)\]\s*",
            r'<span class="ref-anchor" id="ref-\1">[\1]</span> ',
            refs,
        )
        head_html = md_lib.markdown(head, extensions=extensions)
        refs_html = md_lib.markdown(ref_marker + refs, extensions=extensions)
        body = head_html + '\n<div class="refs">\n' + refs_html + "\n</div>"
    else:
        body = md_lib.markdown(md_text, extensions=extensions)

    return (
        "<!doctype html><html lang=\"ko\"><head><meta charset=\"utf-8\">"
        f"<title>{title}</title><style>{css}</style></head>"
        f"<body>{body}</body></html>"
    )


def _free_port() -> int:
    import socket
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def _ws_url(port: int, timeout: float = 20.0) -> str:
    deadline = time.time() + timeout
    last = None
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{port}/json/version", timeout=2) as r:
                return json.load(r)["webSocketDebuggerUrl"]
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(0.3)
    raise RuntimeError(f"Edge DevTools endpoint never came up: {last}")


async def _render(file_url: str, out_path: Path) -> None:
    import websockets

    port = _free_port()
    udd = tempfile.mkdtemp(prefix="edge-pdf-")
    proc = subprocess.Popen(
        [EDGE, "--headless=new", "--disable-gpu", "--no-first-run",
         "--no-default-browser-check", "--hide-scrollbars", "--disable-extensions",
         f"--user-data-dir={udd}", f"--remote-debugging-port={port}", "about:blank"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    try:
        ws_url = _ws_url(port)
        async with websockets.connect(ws_url, max_size=None) as ws:
            ids = itertools.count(1)

            async def cmd(method, params=None, session=None):
                mid = next(ids)
                msg = {"id": mid, "method": method, "params": params or {}}
                if session:
                    msg["sessionId"] = session
                await ws.send(json.dumps(msg))
                while True:
                    m = json.loads(await ws.recv())
                    if m.get("id") == mid:
                        if "error" in m:
                            raise RuntimeError(f"{method}: {m['error']}")
                        return m.get("result", {})

            async def wait_event(method, session=None, timeout=20.0):
                async def _loop():
                    while True:
                        m = json.loads(await ws.recv())
                        if m.get("method") == method and (session is None or m.get("sessionId") == session):
                            return m
                try:
                    return await asyncio.wait_for(_loop(), timeout)
                except asyncio.TimeoutError:
                    return None

            target = await cmd("Target.createTarget", {"url": "about:blank"})
            tid = target["targetId"]
            attach = await cmd("Target.attachToTarget", {"targetId": tid, "flatten": True})
            sid = attach["sessionId"]
            await cmd("Page.enable", session=sid)
            await ws.send(json.dumps({"id": next(ids), "method": "Page.navigate",
                                      "params": {"url": file_url}, "sessionId": sid}))
            await wait_event("Page.loadEventFired", session=sid, timeout=20.0)
            await asyncio.sleep(0.6)  # settle fonts/layout

            result = await cmd("Page.printToPDF", {
                "landscape": False, "printBackground": True,
                "paperWidth": 8.27, "paperHeight": 11.69,
                "marginTop": 0.7, "marginBottom": 0.8,
                "marginLeft": 0.9, "marginRight": 0.9,
                "displayHeaderFooter": True,
                "headerTemplate": "<div></div>",
                "footerTemplate": FOOTER,
                "preferCSSPageSize": False, "scale": 1.0,
            }, session=sid)
            out_path.write_bytes(base64.b64decode(result["data"]))
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except Exception:  # noqa: BLE001
            proc.kill()


def main() -> int:
    ap = argparse.ArgumentParser(description="Render a styled Markdown report to PDF via headless Edge")
    ap.add_argument("source", nargs="?", type=Path, help="Markdown source")
    ap.add_argument("--md", dest="legacy_source", type=Path,
                    help="legacy alias for the Markdown source")
    ap.add_argument("--pdf", type=Path, help="PDF output (default: reports/output/<stem>.pdf)")
    ap.add_argument("--css", type=Path, default=DEFAULT_CSS,
                    help=f"editable print stylesheet (default: {DEFAULT_CSS})")
    ap.add_argument("--html", type=Path, help="optional persistent HTML output")
    ap.add_argument("--keep-html", action="store_true",
                    help="keep intermediate HTML in reports/build/<stem>.html")
    args = ap.parse_args()

    source = args.source or args.legacy_source
    if source is None:
        ap.error("a Markdown source is required")
    source = source.resolve()
    output = (args.pdf or (DEFAULT_OUTPUT_DIR / f"{source.stem}.pdf")).resolve()

    if not os.path.exists(EDGE):
        print(f"[error] Microsoft Edge not found at {EDGE}", file=sys.stderr)
        return 2

    if not args.css.exists():
        print(f"[error] stylesheet not found: {args.css}", file=sys.stderr)
        return 2

    md_text = source.read_text(encoding="utf-8")
    errors = validate_report_source(md_text)
    if errors:
        print("[error] report template validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 2
    css = args.css.read_text(encoding="utf-8")
    html = build_html(md_text, title=source.stem, css=css)

    output.parent.mkdir(parents=True, exist_ok=True)
    if args.html:
        html_path = args.html.resolve()
    elif args.keep_html:
        html_path = (DEFAULT_BUILD_DIR / f"{source.stem}.html").resolve()
    else:
        html_path = Path(tempfile.mkstemp(prefix="report-", suffix=".html")[1])
    html_path.parent.mkdir(parents=True, exist_ok=True)
    html_path.write_text(html, encoding="utf-8")
    file_url = "file://" + str(html_path.resolve())

    print(f"[render] {source.name} -> {output}")
    asyncio.run(_render(file_url, output))

    if not args.keep_html and not args.html:
        try:
            html_path.unlink()
        except OSError:
            pass

    kb = output.stat().st_size / 1024
    print(f"[done] {output} ({kb:.0f}KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
