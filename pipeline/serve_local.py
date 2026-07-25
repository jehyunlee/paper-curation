#!/usr/bin/env python3
"""로컬 미리보기 서버 — docs/ 정적 서빙 + /api/embed Gemini 프록시.

`python -m http.server` 는 정적 파일만 돌려주므로, Deep Research UI 가
같은 출처(`/api/embed`) 로 쿼리 임베딩을 요청하면 응답하지 못한다. 이
스크립트는 docs/ 를 그대로 서빙하면서 `/api/embed` POST 를 운영자의
Gemini 키로 프록시해 로컬 미리보기에서도 검색이 동작하게 한다.

- GET                 → docs/ 정적 파일 (mime 자동, 디렉토리는 index.html)
- POST /api/embed     → {"text": ...} → gemini-embedding-001 (768d,
                        taskType RETRIEVAL_QUERY) → L2 정규화 후
                        {"embedding": [...], "model": ..., "dim": 768}
- POST /api/audio-email → Resend 포워딩 (worker/index.js 와 동일). 운영자
                        RESEND_API_KEY 로 MP3 첨부 메일 발송. 키 없으면 503
                        → UI 가 다운로드로 폴백.

추가 의존성 없음 — 표준 라이브러리(http.server + urllib + base64)만 사용.

키 우선순위:
- 임베딩: GOOGLE_API_KEY/GEMINI_API_KEY env → config.json
  (gemini_api_key/google_api_key) → docs/_local_keys.json (google_key/gemini_key).
- 이메일: RESEND_API_KEY/AUDIO_FROM/AUDIO_REPLY_TO env → config.json
  (resend_api_key/audio_from/audio_reply_to) → docs/_local_keys.json
  (resend_key/audio_from/audio_reply_to).

참고: Resend 샌드박스 발신자(onboarding@resend.dev)는 도메인 인증 전까지
Resend 계정 본인 이메일로만 배달된다. 타인에게 보내려면 커스텀 도메인 인증 +
AUDIO_FROM 설정 필요.
"""

import argparse
import base64
import datetime
import functools
import json
import math
import os
import re
import ssl
import sys
import urllib.error
import urllib.request
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

# config_loader 를 그대로 재사용 (sys.path 트릭 — config_loader 는 건드리지 않는다).
PIPELINE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = PIPELINE_DIR.parent
DOCS_DIR = PROJECT_ROOT / "docs"
sys.path.insert(0, str(PIPELINE_DIR))
try:
    from config_loader import load_config
except Exception:  # config.json 없거나 import 실패해도 env/_local_keys 로 동작
    load_config = None

# Gemini 임베딩 설정 (인덱스 빌드와 동일 — RETRIEVAL_QUERY 만 다르다).
GEMINI_MODEL = "gemini-embedding-001"
GEMINI_ENDPOINT = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    f"{GEMINI_MODEL}:embedContent"
)
EMBED_DIM = 768

# Audio Overview 이메일 발송 — worker/index.js 와 동일하게 Resend 로 포워딩.
RESEND_ENDPOINT = "https://api.resend.com/emails"
DEFAULT_FROM = "Paper Curation <onboarding@resend.dev>"
MAX_ATTACHMENT_BYTES = 25 * 1024 * 1024  # Resend 첨부 상한
MAX_RECIPIENTS = 10
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

# 사내 프록시가 HTTPS 를 self-signed 인증서로 가로채는 환경 대응 (config_loader 와 동일).
_ssl_ctx = ssl.create_default_context()
_ssl_ctx.check_hostname = False
_ssl_ctx.verify_mode = ssl.CERT_NONE

_GOOGLE_KEY_CACHE = None


def resolve_google_key():
    """Gemini 키 조회. env → config.json → docs/_local_keys.json 순. 캐싱(비어있으면 재시도)."""
    global _GOOGLE_KEY_CACHE
    if _GOOGLE_KEY_CACHE:
        return _GOOGLE_KEY_CACHE

    key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY") or ""

    if not key and load_config is not None:
        try:
            cfg = load_config() or {}
            key = cfg.get("gemini_api_key") or cfg.get("google_api_key") or ""
        except Exception:
            key = ""

    if not key:
        local_keys = DOCS_DIR / "_local_keys.json"
        if local_keys.exists():
            try:
                data = json.loads(local_keys.read_text(encoding="utf-8"))
                key = data.get("google_key") or data.get("gemini_key") or ""
            except Exception:
                key = ""

    if key:
        _GOOGLE_KEY_CACHE = key
    return key


def gemini_embed(text, api_key):
    """gemini-embedding-001 으로 쿼리 임베딩 → L2 정규화한 768d 리스트 반환.

    중요: output_dimensionality != 3072 이면 Gemini 가 비정규화 벡터를 돌려준다.
    int8 양자화/코사인 비교 전에 반드시 L2 정규화해야 인덱스와 스케일이 맞는다.
    """
    payload = {
        "model": f"models/{GEMINI_MODEL}",
        "content": {"parts": [{"text": text}]},
        "taskType": "RETRIEVAL_QUERY",
        "outputDimensionality": EMBED_DIM,
    }
    req = urllib.request.Request(
        GEMINI_ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": api_key,
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30, context=_ssl_ctx) as resp:
        out = json.load(resp)

    values = (out.get("embedding") or {}).get("values") or []
    if not values:
        raise ValueError("Gemini 응답에 embedding.values 가 없습니다: " + json.dumps(out)[:200])

    norm = math.sqrt(sum(v * v for v in values)) or 1.0
    return [v / norm for v in values]


def resolve_resend_config():
    """Resend 설정 조회 — (api_key, from, reply_to).

    우선순위: env(RESEND_API_KEY/AUDIO_FROM/AUDIO_REPLY_TO) → config.json
    (resend_api_key/audio_from/audio_reply_to) → docs/_local_keys.json
    (resend_key/audio_from/audio_reply_to). worker 와 동일하게 from 기본값은
    Resend 샌드박스 발신자.
    """
    api_key = os.environ.get("RESEND_API_KEY") or ""
    audio_from = os.environ.get("AUDIO_FROM") or ""
    reply_to = os.environ.get("AUDIO_REPLY_TO") or ""

    if (not api_key or not audio_from or not reply_to) and load_config is not None:
        try:
            cfg = load_config() or {}
            api_key = api_key or cfg.get("resend_api_key") or ""
            audio_from = audio_from or cfg.get("audio_from") or ""
            reply_to = reply_to or cfg.get("audio_reply_to") or ""
        except Exception:
            pass

    if not api_key or not audio_from or not reply_to:
        local_keys = DOCS_DIR / "_local_keys.json"
        if local_keys.exists():
            try:
                data = json.loads(local_keys.read_text(encoding="utf-8"))
                api_key = api_key or data.get("resend_key") or data.get("resend_api_key") or ""
                audio_from = audio_from or data.get("audio_from") or ""
                reply_to = reply_to or data.get("audio_reply_to") or ""
            except Exception:
                pass

    return api_key, (audio_from or DEFAULT_FROM), reply_to


def _escape_html(s):
    """worker/index.js escapeHtml 과 동일."""
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;").replace("'", "&#39;"))


def parse_multipart(content_type, body):
    """multipart/form-data → (fields, files). 바이너리 안전(boundary 수동 분할).

    fields: {name: [str, ...]}, files: {name: (filename, bytes)}.
    cgi.FieldStorage 는 3.13 에서 제거 예정이라 표준 라이브러리만으로 직접 분할한다.
    """
    if "multipart/form-data" not in content_type:
        return {}, {}
    m = re.search(r'boundary=("?)([^";]+)\1', content_type)
    if not m:
        return {}, {}
    boundary = ("--" + m.group(2)).encode("utf-8")

    fields, files = {}, {}
    for seg in body.split(boundary):
        if not seg or seg in (b"--", b"--\r\n", b"\r\n"):
            continue
        if seg.startswith(b"--"):  # 종료 boundary 마커
            continue
        if seg.startswith(b"\r\n"):
            seg = seg[2:]
        hdr_end = seg.find(b"\r\n\r\n")
        if hdr_end == -1:
            continue
        raw_headers = seg[:hdr_end].decode("utf-8", "replace")
        content = seg[hdr_end + 4:]
        if content.endswith(b"\r\n"):  # 다음 boundary 앞 CRLF 제거
            content = content[:-2]
        name = filename = None
        for line in raw_headers.split("\r\n"):
            if line.lower().startswith("content-disposition"):
                for item in line.split(";"):
                    item = item.strip()
                    if item.lower().startswith("name="):
                        name = item[5:].strip().strip('"')
                    elif item.lower().startswith("filename="):
                        filename = item[9:].strip().strip('"')
        if name is None:
            continue
        if filename is not None:
            files[name] = (filename, content)
        else:
            fields.setdefault(name, []).append(content.decode("utf-8", "replace"))
    return fields, files


def resolve_local_emails():
    """로컬 Audio Overview 수신자 목록. env(PAPER_CURATION_LOCAL_EMAILS) →
    config.json(local_emails)."""
    raw = os.environ.get("PAPER_CURATION_LOCAL_EMAILS", "")
    if not raw and load_config is not None:
        try:
            raw = ",".join((load_config() or {}).get("local_emails", []) or [])
        except Exception:
            raw = ""
    return [e.strip() for e in raw.split(",") if e.strip()]


def _inject_local_keys(data):
    """배포 시 strip 된 빈 키 슬롯(_GEMINI_KEY/_LOCAL_EMAILS)을 env→config 값으로
    즉석 주입한다(로컬 서빙 전용, bytes in/out). 리뷰 페이지가 deploy strip 된 채
    남아 있어도 로컬 Audio Overview 가 동작하게 한다. 배포본(Cloudflare)에는
    serve_local 이 없으므로 BYOK strip 상태가 그대로 유지된다."""
    key = resolve_google_key()
    if key:
        data = data.replace(b'_GEMINI_KEY = ""',
                            b'_GEMINI_KEY = "' + key.encode("utf-8") + b'"')
    emails = resolve_local_emails()
    if emails:
        arr = b"[" + b", ".join(json.dumps(e).encode("utf-8") for e in emails) + b"]"
        data = data.replace(b'window._LOCAL_EMAILS = []',
                            b'window._LOCAL_EMAILS = ' + arr)
    return data


class LocalHandler(SimpleHTTPRequestHandler):
    """docs/ 정적 서빙 + /api/* POST 핸들러."""

    def do_GET(self):  # noqa: N802 (stdlib 규약)
        # .html 은 env→config 키를 즉석 주입해 서빙한다 (Audio Overview _GEMINI_KEY,
        # 로컬 이메일 _LOCAL_EMAILS). baked 상태(배포 strip 후 미복원 등)와 무관하게
        # 로컬에서 동작하게 한다. 그 외 파일은 표준 정적 서빙.
        fs_path = self.translate_path(self.path)
        serve_path = None
        if fs_path.endswith(".html") and os.path.isfile(fs_path):
            serve_path = fs_path
        elif self.path.split("?", 1)[0].endswith("/") and os.path.isdir(fs_path):
            idx = os.path.join(fs_path, "index.html")
            if os.path.isfile(idx):
                serve_path = idx
        if not serve_path:
            return super().do_GET()
        try:
            with open(serve_path, "rb") as f:
                data = _inject_local_keys(f.read())
        except OSError:
            self.send_error(404, "File not found")
            return
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def _send_json(self, code, obj):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_body(self):
        length = int(self.headers.get("Content-Length", 0) or 0)
        return self.rfile.read(length) if length > 0 else b""

    def do_POST(self):  # noqa: N802 (stdlib 규약)
        route = self.path.split("?", 1)[0]
        if route == "/api/embed":
            self._handle_embed()
        elif route == "/api/audio-email":
            self._handle_audio_email()
        elif route == "/api/citedby":
            self._handle_citedby()
        else:
            self._send_json(404, {"error": "not found"})

    # ── Citedby (인용논문 분석) — NDJSON 스트리밍 ──────────────────────────
    #
    # 분석은 수 분이 걸린다. 한 번에 응답하면 브라우저가 죽은 것처럼 보이므로
    # 진행 이벤트를 한 줄에 하나씩(JSON) 흘려보낸다. HTTP/1.0 + Content-Length
    # 생략이면 연결 종료가 곧 스트림 끝이라 별도 chunked 인코딩이 필요 없다.
    # 클라이언트는 fetch() + ReadableStream 으로 읽는다 (Deep Research 와 동일 패턴).
    def _stream_line(self, obj):
        try:
            self.wfile.write(
                (json.dumps(obj, ensure_ascii=False) + "\n").encode("utf-8"))
            self.wfile.flush()
            return True
        except (BrokenPipeError, ConnectionResetError):
            return False    # 사용자가 탭을 닫았거나 중단했다

    def _handle_citedby(self):
        try:
            req = json.loads(self._read_body() or b"{}")
        except Exception as e:
            self._send_json(400, {"error": f"invalid JSON body: {e}"})
            return

        doi = (req.get("doi") or "").strip()
        if not doi:
            self._send_json(400, {"error": "missing 'doi'"})
            return

        sources = req.get("sources") or None
        topic = (req.get("topic") or "").strip()
        lang = (req.get("lang") or "ko").strip()
        slug = (req.get("slug") or "").strip()
        use_llm = bool(req.get("use_llm_originality", True))

        self.send_response(200)
        self.send_header("Content-Type", "application/x-ndjson; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Accel-Buffering", "no")
        self.end_headers()

        alive = {"ok": True}

        def on_event(phase, message, current=0, total=0):
            if not alive["ok"]:
                return
            alive["ok"] = self._stream_line({
                "event": "progress", "phase": phase, "message": message,
                "current": current, "total": total,
            })

        try:
            # 지연 import — citedby 를 안 쓰는 서버 기동에 pandas 비용을 물리지 않는다.
            from lib.citedby import run_citedby
            result = run_citedby(doi, sources=sources, topic=topic, lang=lang,
                                 use_llm_originality=use_llm, on_event=on_event)
        except Exception as e:
            self._stream_line({"event": "error", "message": str(e)[:400]})
            return

        files = self._save_citedby_outputs(slug, result)
        self._stream_line({
            "event": "done",
            "doi": result["doi"],
            "matched": result["matched"],
            "total": result["total"],
            "elapsed_sec": result["elapsed_sec"],
            "source_counts": result["source_counts"],
            "report_html": result["report_html"],
            "files": files,
        })

    def _save_citedby_outputs(self, slug, result):
        """리포트/CSV 를 docs/papers/{slug}/citedby/ 에 저장하고 URL 을 돌려준다.

        slug 가 없으면 저장을 건너뛴다. docs/papers/ 는 gitignore +
        .assetsignore 대상이라 저장소·배포를 오염시키지 않는다.
        """
        if not slug:
            return {}
        # 경로 소독 2단: 허용 문자만 남기고 → 남은 점 연속(`..`)을 접는다.
        # 문자 필터만으로는 "../../etc/evil" 이 "....etcevil" 로 남아 경로
        # 성분에 `..` 가 살아난다.
        safe = re.sub(r"[^A-Za-z0-9._-]", "", slug)
        safe = re.sub(r"\.{2,}", ".", safe).strip("._-")
        if not safe:
            return {}
        papers_root = (DOCS_DIR / "papers").resolve()
        out_dir = (papers_root / safe / "citedby").resolve()
        # 봉쇄 검증 — 어떤 입력이 와도 papers/ 밖에는 쓰지 않는다.
        if not str(out_dir).startswith(str(papers_root) + os.sep):
            print(f"  [citedby] slug 거부(경로 이탈): {slug!r}")
            return {}
        try:
            out_dir.mkdir(parents=True, exist_ok=True)
            stamp = datetime.datetime.now().strftime("%y%m%d_%H%M")
            files = {}
            report_path = out_dir / f"report_{stamp}.html"
            report_path.write_text(result["report_html"], encoding="utf-8")
            files["report"] = f"/papers/{safe}/citedby/{report_path.name}"
            if result.get("csv"):
                csv_path = out_dir / f"citing_{stamp}.csv"
                csv_path.write_text(result["csv"], encoding="utf-8")
                files["csv"] = f"/papers/{safe}/citedby/{csv_path.name}"
            return files
        except OSError as e:
            print(f"  [citedby] 저장 실패: {e}")
            return {}

    def _handle_embed(self):
        try:
            req = json.loads(self._read_body() or b"{}")
        except Exception as e:
            self._send_json(400, {"error": f"invalid JSON body: {e}"})
            return

        text = (req.get("text") or "").strip()
        if not text:
            self._send_json(400, {"error": "missing 'text'"})
            return

        api_key = resolve_google_key()
        if not api_key:
            self._send_json(503, {
                "error": "Gemini 키 없음 — GOOGLE_API_KEY env 또는 "
                         "config.json(gemini_api_key) 를 설정하세요.",
            })
            return

        try:
            vec = gemini_embed(text, api_key)
        except urllib.error.HTTPError as e:
            try:
                detail = e.read().decode("utf-8", "replace")[:300]
            except Exception:
                detail = str(e)
            self._send_json(502, {"error": f"Gemini embed {e.code}: {detail}"})
            return
        except Exception as e:
            self._send_json(502, {"error": f"Gemini embed 실패: {e}"})
            return

        self._send_json(200, {"embedding": vec, "model": GEMINI_MODEL, "dim": len(vec)})

    # ── Audio Overview 이메일 발송 (Resend 포워딩) ──────────────────────────
    def _parse_multipart(self):
        return parse_multipart(self.headers.get("Content-Type", "") or "", self._read_body())

    def _resend_send(self, api_key, payload):
        """Resend /emails POST 1건. (status_code, body_snippet) 반환."""
        req = urllib.request.Request(
            RESEND_ENDPOINT,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": "Bearer " + api_key,
                "Content-Type": "application/json",
                # api.resend.com 은 Cloudflare 뒤에 있어 기본 User-Agent
                # (Python-urllib)는 1010 으로 차단된다. 명시적 UA 필수.
                "User-Agent": "paper-curation-serve-local/1.0 (+https://github.com/jehyunlee/paper-curation)",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30, context=_ssl_ctx) as resp:
                return resp.status, resp.read().decode("utf-8", "replace")[:400]
        except urllib.error.HTTPError as e:
            try:
                detail = e.read().decode("utf-8", "replace")[:400]
            except Exception:
                detail = str(e)
            return e.code, detail
        except Exception as e:
            return 0, str(e)[:400]

    def _handle_audio_email(self):
        # worker/index.js handleAudioEmail 와 동일 계약. 키 없으면 503 →
        # UI(sendAudioEmail)가 다운로드로 graceful 폴백.
        api_key, audio_from, reply_to = resolve_resend_config()
        if not api_key:
            self._send_json(503, {
                "error": "RESEND_API_KEY 없음 — env 또는 config.json(resend_api_key) "
                         "또는 docs/_local_keys.json(resend_key) 를 설정하세요.",
            })
            return

        try:
            fields, files = self._parse_multipart()
        except Exception as e:
            self._send_json(400, {"error": f"multipart 파싱 실패: {e}"})
            return

        recipients = [v.strip() for v in fields.get("email", []) if EMAIL_RE.match(v.strip())]
        if not recipients:
            self._send_json(400, {"error": "유효한 수신자 없음"})
            return
        if len(recipients) > MAX_RECIPIENTS:
            self._send_json(400, {"error": f"수신자 너무 많음 (최대 {MAX_RECIPIENTS})"})
            return
        if "mp3" not in files:
            self._send_json(400, {"error": "mp3 첨부 없음"})
            return

        file_name, content = files["mp3"]
        if len(content) > MAX_ATTACHMENT_BYTES:
            self._send_json(413, {"error": "첨부 용량 초과"})
            return
        b64 = base64.b64encode(content).decode("ascii")

        filename = (fields.get("filename") or [file_name or "audio-overview.mp3"])[0]
        title = (fields.get("title") or ["Audio Overview"])[0]
        lang = (fields.get("lang") or ["ko"])[0]
        is_ko = lang == "ko"

        subject = f"[Paper Curation] Audio Overview: {title}"
        if is_ko:
            html = (
                "<p>요청하신 Audio Overview 가 첨부되어 있습니다.</p>"
                f"<p><b>제목</b>: {_escape_html(title)}</p>"
                "<p>이 메일은 Paper Curation 의 자동 발송입니다. 답장은 운영자에게 전달됩니다.</p>"
            )
        else:
            html = (
                "<p>Your requested Audio Overview is attached.</p>"
                f"<p><b>Title</b>: {_escape_html(title)}</p>"
                "<p>This is an automated message from Paper Curation. Replies route to the operator.</p>"
            )

        payload_base = {
            "from": audio_from,
            "subject": subject,
            "html": html,
            "attachments": [{"filename": filename, "content": b64}],
        }
        if reply_to:
            payload_base["reply_to"] = reply_to

        results, any_fail = [], False
        for to in recipients:
            payload = dict(payload_base, to=[to])
            code, text = self._resend_send(api_key, payload)
            ok = 200 <= code < 300
            any_fail = any_fail or not ok
            results.append({"to": to, "ok": ok, "status": code, "body": text})

        self._send_json(502 if any_fail else 200, {"results": results})


def main():
    parser = argparse.ArgumentParser(
        description="docs/ 정적 서빙 + /api/embed Gemini 프록시 (로컬 미리보기용)"
    )
    parser.add_argument("--port", type=int, default=8000, help="리슨 포트 (기본 8000)")
    parser.add_argument("--topic", default="", help="열어볼 토픽 (URL 안내용, 예: ai4s)")
    args = parser.parse_args()

    if not DOCS_DIR.exists():
        print(f"ERROR: docs 디렉토리를 찾을 수 없습니다: {DOCS_DIR}", file=sys.stderr)
        sys.exit(1)

    sub = (args.topic.strip("/") + "/") if args.topic else ""
    url = f"http://localhost:{args.port}/{sub}"

    handler = functools.partial(LocalHandler, directory=str(DOCS_DIR))
    httpd = ThreadingHTTPServer(("", args.port), handler)

    has_key = bool(resolve_google_key())
    print(f"docs/ 서빙 + /api/embed → Gemini ({GEMINI_MODEL}, {EMBED_DIM}d) 프록시")
    print(f"Gemini 키: {'감지됨' if has_key else '없음 (검색 임베딩 비활성 — 키 설정 필요)'}")
    print(f"열기: {url}")
    if (DOCS_DIR / "_cross" / "index.html").exists():
        print(f"통합 Deep Research (로컬 전용): http://localhost:{args.port}/_cross/")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n종료합니다.")
    finally:
        httpd.shutdown()
        httpd.server_close()


if __name__ == "__main__":
    main()
