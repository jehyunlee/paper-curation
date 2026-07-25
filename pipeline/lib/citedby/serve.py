"""리포트를 로컬 서버로 띄운다.

Deep Research 패널은 `file://` 에서 동작하지 않는다 — 브라우저가 CORS 로
`fetch()` 를 막아 인덱스를 못 읽고, 쿼리 임베딩용 `/api/embed` 도 없다.
그래서 리포트를 만든 뒤 **자동으로** 서버를 띄우고 http URL 을 돌려준다.

이미 떠 있으면 재사용한다. 매번 새로 띄우면 포트가 충돌하고, 사용자가 열어 둔
다른 탭이 끊긴다. 판별은 포트 점유 여부가 아니라 **우리 서버인지 확인**으로
한다 — 8000 번은 흔한 포트라 남의 서버를 우리 것으로 오인하면 안 된다.
"""
from __future__ import annotations

import json
import logging
import os
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

logger = logging.getLogger(__name__)

DEFAULT_PORT = 8000
# 여러 번 돌려도 같은 서버를 재사용하도록, 충돌 시 위로 몇 칸만 훑는다.
PORT_SCAN = 8
STARTUP_TIMEOUT = 12.0

_PIPELINE = Path(__file__).resolve().parents[2]
_PROJECT = _PIPELINE.parent
_DOCS = _PROJECT / "docs"


def _port_open(port: int, host: str = "127.0.0.1") -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.4)
        return s.connect_ex((host, port)) == 0


def _is_ours(port: int) -> bool:
    """이 포트의 서버가 paper-curation serve_local 인지 확인.

    `/api/embed` 는 우리만 가진 라우트다. 본문 없이 POST 하면 400(missing
    'text')이 돌아온다 — 그 응답 모양이 서명 역할을 한다. 남의 서버라면
    404/405 이거나 아예 다른 본문이다.
    """
    try:
        req = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/embed", data=b"{}",
            headers={"Content-Type": "application/json"}, method="POST")
        urllib.request.urlopen(req, timeout=2)
        return True                      # 200 이면 확실히 우리 것
    except urllib.error.HTTPError as e:
        if e.code != 400:
            return False
        try:
            body = json.loads(e.read().decode("utf-8", "replace"))
        except Exception:  # noqa: BLE001
            return False
        return "text" in str(body.get("error", ""))
    except Exception:  # noqa: BLE001
        return False


def find_running(port: int = DEFAULT_PORT) -> int | None:
    """이미 떠 있는 우리 서버의 포트. 없으면 None."""
    for p in range(port, port + PORT_SCAN):
        if _port_open(p) and _is_ours(p):
            return p
    return None


def _free_port(start: int) -> int | None:
    for p in range(start, start + PORT_SCAN):
        if not _port_open(p):
            return p
    return None


def ensure_server(port: int = DEFAULT_PORT, *,
                  timeout: float = STARTUP_TIMEOUT) -> int | None:
    """서버를 확보한다. 이미 떠 있으면 그 포트, 아니면 새로 띄운다.

    띄운 서버는 **부모와 무관하게 계속 산다** — citedby 프로세스가 끝나도
    브라우저에서 계속 써야 하기 때문이다. 로그는 버린다(장시간 살아 있는
    프로세스라 파이프가 차면 멎는다).
    """
    running = find_running(port)
    if running:
        logger.info("로컬 서버 재사용: http://localhost:%d", running)
        return running

    target = _free_port(port)
    if target is None:
        logger.warning("빈 포트를 찾지 못했다 (%d~%d)", port, port + PORT_SCAN - 1)
        return None

    script = _PIPELINE / "serve_local.py"
    if not script.exists():
        logger.warning("serve_local.py 없음: %s", script)
        return None

    try:
        subprocess.Popen(
            [sys.executable, "-u", str(script), "--port", str(target)],
            cwd=str(_PROJECT),
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
            start_new_session=True,      # 부모가 죽어도 살아남는다
            env={**os.environ, "PYTHONUTF8": "1"},
        )
    except Exception as e:  # noqa: BLE001
        logger.warning("서버 기동 실패: %s", str(e)[:120])
        return None

    deadline = time.time() + timeout
    while time.time() < deadline:
        if _port_open(target) and _is_ours(target):
            logger.info("로컬 서버 기동: http://localhost:%d", target)
            return target
        time.sleep(0.3)

    logger.warning("서버가 %.0f초 안에 뜨지 않았다", timeout)
    return None


def report_url(report_path, port: int) -> str:
    """리포트 파일 경로 → http URL. docs/ 밖이면 빈 문자열."""
    try:
        rel = Path(report_path).resolve().relative_to(_DOCS.resolve())
    except (ValueError, OSError):
        return ""
    return f"http://localhost:{port}/" + "/".join(rel.parts)


def serve_report(report_path, *, port: int = DEFAULT_PORT,
                 open_browser: bool = False) -> str:
    """리포트를 서버로 띄우고 URL 을 돌려준다. 실패하면 빈 문자열.

    산출물이 `docs/` 밖이면(예: --out /tmp) 서버가 서빙할 수 없으므로 URL 을
    만들지 않는다 — 잘못된 링크를 주느니 없는 게 낫다.
    """
    url = ""
    p = ensure_server(port)
    if p:
        url = report_url(report_path, p)
    if url and open_browser:
        try:
            import webbrowser
            webbrowser.open(url)
        except Exception:  # noqa: BLE001
            pass
    return url
