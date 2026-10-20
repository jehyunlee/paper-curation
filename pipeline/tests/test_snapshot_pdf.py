"""Zotero web snapshots become reviewable sources instead of fuzzy-matched PDFs.

Regression for 913 "Semantic Scholar": the item had no PDF, only a saved
`www.semanticscholar.org.html`; the fuzzy filename scan matched the S2ORC
paper's PDF and two slugs ended up sharing one text.md.
"""
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import run_update_force as R  # noqa: E402

HTML = """<html><head><title>Tool | Home</title><style>p{color:red}</style>
<script>window.app = {state: 1};</script></head>
<body><nav>Skip to content</nav>
<h1>Semantic Scholar</h1>
<p>A free, AI-powered research tool for scientific literature.</p>
<p>A free, AI-powered research tool for scientific literature.</p>
<div>Search 224,708,370 papers from all fields of science.</div>
<template><p>hidden</p></template>
</body></html>"""


class SnapshotAttachmentTests(unittest.TestCase):
    def test_only_saved_html_attachments_qualify(self):
        pdf = {"data": {"itemType": "attachment", "contentType": "application/pdf",
                        "linkMode": "linked_file", "key": "A", "filename": "x.pdf"}}
        linked_url = {"data": {"itemType": "attachment", "contentType": "text/html",
                               "linkMode": "linked_url", "key": "B", "filename": "x.html"}}
        saved = {"data": {"itemType": "attachment", "contentType": "text/html",
                          "linkMode": "imported_url", "key": "C", "filename": "page.html"}}
        self.assertIsNone(R._snapshot_attachment([pdf, linked_url]))
        self.assertEqual(R._snapshot_attachment([pdf, linked_url, saved])["key"], "C")


class SnapshotRenderTests(unittest.TestCase):
    def test_visible_html_drops_code_and_collapses_adjacent_repeats(self):
        cleaned, blocks = R._snapshot_visible_html(HTML, title="Semantic Scholar")
        self.assertNotIn("window.app", cleaned)
        self.assertNotIn("color:red", cleaned)
        self.assertNotIn("hidden", cleaned)
        self.assertEqual(blocks.count("A free, AI-powered research tool for scientific literature."), 1)
        self.assertIn("<h1>Semantic Scholar</h1>", cleaned)

    def test_render_writes_marked_pdf_and_refuses_empty_shells(self):
        import fitz
        with tempfile.TemporaryDirectory() as tmp:
            html_path = os.path.join(tmp, "page.html")
            Path(html_path).write_text(HTML, encoding="utf-8")
            pdf_path = os.path.join(tmp, "out", "page.pdf")
            visible = R.render_snapshot_pdf(html_path, pdf_path, title="Semantic Scholar",
                                            source_url="https://www.semanticscholar.org/",
                                            saved="2025-03-03")
            self.assertGreaterEqual(visible, 100)
            text = fitz.open(pdf_path)[0].get_text()
            self.assertTrue(text.startswith(
                f"{R.SNAPSHOT_MARKER} https://www.semanticscholar.org/ 2025-03-03"))
            self.assertIn("224,708,370", text)

            shell = os.path.join(tmp, "shell.html")
            Path(shell).write_text("<html><body><script>x()</script><p>Hi</p></body></html>",
                                   encoding="utf-8")
            self.assertLess(R.render_snapshot_pdf(shell, os.path.join(tmp, "shell.pdf")), 100)
            self.assertFalse(os.path.exists(os.path.join(tmp, "shell.pdf")))


class FindPdfSnapshotPriorityTests(unittest.TestCase):
    def _children(self, extra=()):
        return [{"data": {"itemType": "attachment", "contentType": "text/html",
                          "linkMode": "imported_url", "key": "QT6IHFHI",
                          "filename": "page.html", "url": "https://example.test/"}},
                *extra]

    def test_snapshot_outranks_fuzzy_and_is_cached(self):
        with tempfile.TemporaryDirectory() as tmp:
            storage = Path(tmp) / "storage" / "QT6IHFHI"
            storage.mkdir(parents=True)
            (storage / "page.html").write_text(HTML, encoding="utf-8")
            zotero_dir = Path(tmp) / "zotero"
            zotero_dir.mkdir()
            # A PDF whose name would satisfy the fuzzy scan for this title.
            (zotero_dir / "semantic scholar open research corpus tool.pdf").write_bytes(b"%PDF")
            item = {"key": "XIN7LQIB", "title": "Semantic Scholar Open Research Corpus Tool",
                    "accessDate": "2025-03-03T01:09:49Z"}
            resp = mock.MagicMock()
            resp.__enter__.return_value = resp
            resp.read.return_value = json.dumps(self._children()).encode("utf-8")
            with mock.patch.object(R, "ZOTERO_DIR", str(zotero_dir)), \
                    mock.patch.object(R, "SNAPSHOT_PDF_DIR", Path(tmp) / "snap"), \
                    mock.patch.object(R, "_audit_append"), \
                    mock.patch("config_loader.get_zotero_storage_dir",
                               return_value=str(Path(tmp) / "storage")), \
                    mock.patch("config_loader.get_zotero_user_id", return_value="1"), \
                    mock.patch("config_loader.get_zotero_api_key", return_value="k"), \
                    mock.patch.object(R, "get_zotero_user_id", return_value="1", create=True), \
                    mock.patch.object(R, "get_zotero_api_key", return_value="k", create=True), \
                    mock.patch("urllib.request.urlopen", return_value=resp):
                path, method = R.find_pdf(item)
                self.assertEqual(method, "zotero_snapshot_html")
                self.assertEqual(path, str(Path(tmp) / "snap" / "QT6IHFHI.pdf"))
                first_mtime = os.path.getmtime(path)
                path2, _ = R.find_pdf(item)
                self.assertEqual(path2, path)
                self.assertEqual(os.path.getmtime(path), first_mtime)

    def test_missing_snapshot_file_falls_through(self):
        with tempfile.TemporaryDirectory() as tmp:
            zotero_dir = Path(tmp) / "zotero"
            zotero_dir.mkdir()
            item = {"key": "XIN7LQIB", "title": "Semantic Scholar"}
            resp = mock.MagicMock()
            resp.__enter__.return_value = resp
            resp.read.return_value = json.dumps(self._children()).encode("utf-8")
            with mock.patch.object(R, "ZOTERO_DIR", str(zotero_dir)), \
                    mock.patch.object(R, "_audit_append"), \
                    mock.patch("config_loader.get_zotero_storage_dir",
                               return_value=str(Path(tmp) / "absent")), \
                    mock.patch.object(R, "get_zotero_user_id", return_value="1", create=True), \
                    mock.patch.object(R, "get_zotero_api_key", return_value="k", create=True), \
                    mock.patch("urllib.request.urlopen", return_value=resp):
                self.assertEqual(R.find_pdf(item), (None, "no_match"))


class SnapshotReviewPromptTests(unittest.TestCase):
    def _prompt_for(self, text):
        captured = {}

        def fake_cached_call(cache_dir, prompt, model, make_call, **kwargs):
            captured["prompt"] = prompt
            return None

        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "text.md").write_text(text, encoding="utf-8")
            with mock.patch("api._llm.cached_call", side_effect=fake_cached_call), \
                    mock.patch("lib.text_providers.validate_review_payload",
                               side_effect=RuntimeError("stop")):
                R.write_review({"title": "T", "creators": []}, tmp, [],
                               provider="anthropic", model="m", cache_dir=tmp)
        return captured["prompt"]

    def test_snapshot_marker_adds_web_resource_note(self):
        prompt = self._prompt_for(f"# T\n\n{R.SNAPSHOT_MARKER} https://x.test 2025-03-03\nbody")
        self.assertIn("웹 자료", prompt)
        self.assertIn("거부하", prompt)

    def test_paper_prompt_is_unchanged(self):
        prompt = self._prompt_for("# T\n\nAbstract. Ordinary paper text.")
        self.assertNotIn("웹 자료", prompt)
        self.assertTrue(prompt.startswith("논문을 분석하고 `emit_review` 도구를 호출해 리뷰 필드를 채워라.\n\n모든 narrative"))


if __name__ == "__main__":
    unittest.main()
