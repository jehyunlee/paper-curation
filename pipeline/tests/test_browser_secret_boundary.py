"""Generated browser artifacts must never contain operator credentials."""
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import build_topic_index
import compare_papers
from lib.audio_overview import audio_script_block


class BrowserSecretBoundaryTest(unittest.TestCase):
    sentinels = {
        "ANTHROPIC_API_KEY": "operator-anthropic-sentinel",
        "OPENAI_API_KEY": "operator-openai-sentinel",
        "GOOGLE_API_KEY": "operator-google-sentinel",
        "GEMINI_API_KEY": "operator-gemini-sentinel",
        "PAPER_CURATION_LOCAL_EMAILS": "operator@example.invalid",
    }

    def assert_no_operator_values(self, html):
        for value in self.sentinels.values():
            self.assertNotIn(value, html)

    def test_shared_audio_script_uses_empty_reader_owned_slots(self):
        html = audio_script_block(
            self.sentinels["GOOGLE_API_KEY"],
            mode="deep",
            local_emails=[self.sentinels["PAPER_CURATION_LOCAL_EMAILS"]],
        )
        self.assert_no_operator_values(html)
        self.assertIn("window._GEMINI_KEY = '';", html)
        self.assertIn("localStorage.getItem(\"_GEMINI_KEY\")", html)
        self.assertIn("Audio Overview는 Gemini API Key가 필요합니다", html)

    def test_topic_and_cross_generators_do_not_read_or_emit_operator_values(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, self.sentinels, clear=False):
            root = Path(tmp)
            papers = root / "papers"
            papers.mkdir()
            (papers / "_papers_index.json").write_text("[]", encoding="utf-8")
            topic = root / "topic"
            cross = root / "cross"
            topic.mkdir()
            cross.mkdir()

            def topic_dir(name):
                return cross if name == "cross" else topic

            with patch.object(build_topic_index, "PAPERS_DIR", str(papers)), \
                 patch.object(build_topic_index, "DOCS_DIR", root), \
                 patch.object(build_topic_index, "get_topic_dir", side_effect=topic_dir), \
                 patch("config_loader.load_config", return_value={
                     "zotero": {"collections": {}},
                     "anthropic_api_key": "config-anthropic-sentinel",
                     "openai_api_key": "config-openai-sentinel",
                     "google_api_key": "config-google-sentinel",
                     "gemini_api_key": "config-gemini-sentinel",
                     "local_emails": ["config@example.invalid"],
                 }), \
                 patch.dict(os.environ, {"SKIP_ZOTERO_KEYS": "1"}, clear=False):
                build_topic_index._run_topic_index("topic")
                build_topic_index._run_topic_index("cross", cross={"title": "Cross"})

            for output in (topic / "index.html", cross / "index.html"):
                html = output.read_text(encoding="utf-8")
                self.assert_no_operator_values(html)
                for value in ("config-anthropic-sentinel", "config-openai-sentinel",
                              "config-google-sentinel", "config-gemini-sentinel",
                              "config@example.invalid"):
                    self.assertNotIn(value, html)
                self.assertIn("localStorage.getItem('_LLM_KEY')", html)
                self.assertIn("window._GEMINI_KEY = '';", html)

    def test_comparison_generator_keeps_audio_byok(self):
        papers = [{
            "slug": "001_one", "title": "One", "authors": ["A"], "doi": "",
            "date": "2026", "category": "Test", "purl": "https://example.test/one",
            "connections": [],
        }, {
            "slug": "002_two", "title": "Two", "authors": ["B"], "doi": "",
            "date": "2026", "category": "Test", "purl": "https://example.test/two",
            "connections": [],
        }]
        comp = {"overview_ko": "개요", "reading_guide_ko": "안내", "quick_table": [], "axes": []}
        theme = compare_papers.RH.THEMES["ai4s"]
        with patch.dict(os.environ, self.sentinels, clear=False):
            html = compare_papers.build_html(papers, comp, "comparison", theme, "comparison")
        self.assert_no_operator_values(html)
        self.assertIn("window._GEMINI_KEY = '';", html)
        self.assertIn("localStorage.getItem(\"_GEMINI_KEY\")", html)


if __name__ == "__main__":
    unittest.main()
