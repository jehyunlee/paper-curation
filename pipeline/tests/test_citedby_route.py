"""Integration coverage for serve_local `/api/citedby` (NDJSON 스트리밍).

실제 `ThreadingHTTPServer` 를 띄워 라우트를 왕복 검증한다. citedby 코어는
가짜로 갈아끼워 네트워크·LLM 을 타지 않는다.

잠그는 계약:
  * 진행 이벤트가 **완료 전에** 도착한다 (스트리밍이지 버퍼링이 아니다).
  * 마지막 줄이 `done` 이고 report_html 을 싣는다.
  * 코어가 던지면 `error` 이벤트로 내려온다 (500 이 아니라 스트림 안에서).
  * slug 를 주면 docs/papers/{slug}/citedby/ 에 저장하고 URL 을 돌려준다.
  * slug 는 경로 이스케이프가 불가능하도록 소독된다.
"""
from __future__ import annotations

import json
import sys
import threading
import unittest
import urllib.error
import urllib.request
from functools import partial
from http.server import ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch

PIPELINE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE_DIR))

import lib.citedby as citedby_pkg  # noqa: E402
import serve_local  # noqa: E402


def _fake_result(**over):
    base = {
        "doi": "10.1/seed",
        "paper_info": {"title": "Seed", "doi": "10.1/seed"},
        "source_counts": {"openalex": 3},
        "all_papers": [],
        "all_csv": "",
        "topic": "AI",
        "papers": [{"title": "Citing", "doi": "10.1/c"}],
        "report_html": "<!DOCTYPE html><html><body>REPORT</body></html>",
        "csv": "title,url\nCiting,https://doi.org/10.1/c\n",
        "matched": 1,
        "total": 3,
        "elapsed_sec": 0.4,
    }
    base.update(over)
    return base


class CitedbyRouteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(__import__("tempfile").mkdtemp())
        (cls.tmp / "papers").mkdir(parents=True, exist_ok=True)
        cls._orig_docs = serve_local.DOCS_DIR
        serve_local.DOCS_DIR = cls.tmp

        handler = partial(serve_local.LocalHandler, directory=str(cls.tmp))
        cls.httpd = ThreadingHTTPServer(("127.0.0.1", 0), handler)
        cls.port = cls.httpd.server_address[1]
        cls.thread = threading.Thread(target=cls.httpd.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()
        serve_local.DOCS_DIR = cls._orig_docs
        __import__("shutil").rmtree(cls.tmp, ignore_errors=True)

    def _post(self, payload, timeout=30):
        req = urllib.request.Request(
            f"http://127.0.0.1:{self.port}/api/citedby",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}, method="POST")
        return urllib.request.urlopen(req, timeout=timeout)

    def _post_lines(self, payload, timeout=30):
        with self._post(payload, timeout) as resp:
            self.assertEqual(resp.status, 200)
            raw = resp.read().decode("utf-8")
        return [json.loads(ln) for ln in raw.splitlines() if ln.strip()]

    # ── 정상 경로 ────────────────────────────────────────────────────────
    def test_streams_progress_then_done(self):
        def fake(doi, **kw):
            emit = kw["on_event"]
            emit("fetch", "검색 중", 0, 0)
            emit("topic_filter", "필터링", 1, 3)
            return _fake_result()

        with patch.object(citedby_pkg, "run_citedby", fake, create=True):
            lines = self._post_lines({"doi": "10.1/seed", "topic": "AI"})

        kinds = [ln["event"] for ln in lines]
        self.assertEqual(kinds[-1], "done")
        self.assertEqual(kinds[:2], ["progress", "progress"])
        self.assertEqual(lines[0]["phase"], "fetch")
        self.assertEqual(lines[1]["current"], 1)

        done = lines[-1]
        self.assertIn("REPORT", done["report_html"])
        self.assertEqual((done["matched"], done["total"]), (1, 3))
        self.assertEqual(done["source_counts"], {"openalex": 3})

    def test_ndjson_content_type(self):
        with patch.object(citedby_pkg, "run_citedby",
                          lambda doi, **kw: _fake_result(), create=True):
            with self._post({"doi": "10.1/x"}) as resp:
                ctype = resp.headers.get("Content-Type", "")
        self.assertIn("application/x-ndjson", ctype)

    def test_request_params_are_forwarded(self):
        seen = {}

        def fake(doi, **kw):
            seen["doi"] = doi
            seen.update(kw)
            return _fake_result()

        with patch.object(citedby_pkg, "run_citedby", fake, create=True):
            self._post_lines({"doi": "10.1/z", "topic": "T", "lang": "en",
                              "sources": ["openalex"],
                              "use_llm_originality": False})

        self.assertEqual(seen["doi"], "10.1/z")
        self.assertEqual(seen["topic"], "T")
        self.assertEqual(seen["lang"], "en")
        self.assertEqual(seen["sources"], ["openalex"])
        self.assertFalse(seen["use_llm_originality"])

    # ── 실패 경로 ────────────────────────────────────────────────────────
    def test_missing_doi_is_400(self):
        with self.assertRaises(urllib.error.HTTPError) as cm:
            self._post({"topic": "x"})
        self.assertEqual(cm.exception.code, 400)

    def test_invalid_json_body_is_400(self):
        req = urllib.request.Request(
            f"http://127.0.0.1:{self.port}/api/citedby",
            data=b"{not json", headers={"Content-Type": "application/json"},
            method="POST")
        with self.assertRaises(urllib.error.HTTPError) as cm:
            urllib.request.urlopen(req, timeout=10)
        self.assertEqual(cm.exception.code, 400)

    def test_core_exception_becomes_error_event(self):
        def boom(doi, **kw):
            raise RuntimeError("scopus exploded")

        with patch.object(citedby_pkg, "run_citedby", boom, create=True):
            lines = self._post_lines({"doi": "10.1/x"})

        self.assertEqual(lines[-1]["event"], "error")
        self.assertIn("scopus exploded", lines[-1]["message"])

    def test_unknown_route_is_404(self):
        req = urllib.request.Request(
            f"http://127.0.0.1:{self.port}/api/nope", data=b"{}",
            method="POST")
        with self.assertRaises(urllib.error.HTTPError) as cm:
            urllib.request.urlopen(req, timeout=10)
        self.assertEqual(cm.exception.code, 404)

    # ── 산출물 저장 ──────────────────────────────────────────────────────
    def test_saves_report_and_csv_under_slug(self):
        with patch.object(citedby_pkg, "run_citedby",
                          lambda doi, **kw: _fake_result(), create=True):
            lines = self._post_lines({"doi": "10.1/x", "slug": "042_Some_Paper"})

        files = lines[-1]["files"]
        self.assertTrue(files["report"].startswith(
            "/papers/042_Some_Paper/citedby/"))
        self.assertTrue(files["csv"].endswith(".csv"))

        out_dir = self.tmp / "papers" / "042_Some_Paper" / "citedby"
        written = sorted(p.name for p in out_dir.iterdir())
        self.assertTrue(any(n.endswith(".html") for n in written), written)
        self.assertTrue(any(n.endswith(".csv") for n in written), written)
        html = next(p for p in out_dir.iterdir() if p.suffix == ".html")
        self.assertIn("REPORT", html.read_text(encoding="utf-8"))

    def test_no_slug_skips_saving(self):
        with patch.object(citedby_pkg, "run_citedby",
                          lambda doi, **kw: _fake_result(), create=True):
            lines = self._post_lines({"doi": "10.1/x"})
        self.assertEqual(lines[-1]["files"], {})

    def test_slug_traversal_is_sanitized(self):
        """`../` 를 섞어도 papers/ 밖으로 나가지 못한다."""
        with patch.object(citedby_pkg, "run_citedby",
                          lambda doi, **kw: _fake_result(), create=True):
            lines = self._post_lines({"doi": "10.1/x", "slug": "../../etc/evil"})

        files = lines[-1]["files"]
        self.assertNotIn("..", files.get("report", ""))
        resolved = (self.tmp / "papers").resolve()
        for p in (self.tmp / "papers").rglob("*.html"):
            self.assertTrue(str(p.resolve()).startswith(str(resolved)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
