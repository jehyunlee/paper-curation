"""Figure extraction must not pay for a vision call that cannot change the crop."""
import os
import sys
import tempfile
import types
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE))
import run_update_force as engine  # noqa: E402


def _synthetic_pdf(path: Path) -> None:
    import fitz
    doc = fitz.open()
    page = doc.new_page(width=595, height=842)
    page.draw_rect(fitz.Rect(80, 120, 500, 420), color=(0, 0, 0), fill=(0.3, 0.5, 0.8))
    page.insert_text((80, 445), "Figure 1. Synthetic validation figure for the crop loop.", fontsize=10)
    page.insert_textbox(fitz.Rect(60, 480, 540, 800), "Body text. " * 120, fontsize=9)
    doc.save(str(path))
    doc.close()


class FigureValidationCostTests(unittest.TestCase):
    def _run(self, verdict):
        calls = []

        class Models:
            def generate_content(self, **kwargs):
                calls.append(kwargs["model"])
                return SimpleNamespace(text=verdict)

        class Client:
            def __init__(self, **kwargs):
                self.models = Models()

        fake_google = types.ModuleType("google")
        fake_genai = types.ModuleType("google.genai")
        fake_types = types.ModuleType("google.genai.types")
        fake_genai.Client = Client
        fake_types.Part = SimpleNamespace(from_bytes=lambda **kw: kw)
        fake_genai.types = fake_types
        fake_google.genai = fake_genai
        with tempfile.TemporaryDirectory() as tmp:
            pdf = Path(tmp) / "paper.pdf"
            _synthetic_pdf(pdf)
            out = Path(tmp) / "slug"
            out.mkdir()
            with patch.dict(sys.modules, {"google": fake_google,
                                          "google.genai": fake_genai,
                                          "google.genai.types": fake_types}), \
                 patch.object(engine, "get_google_key", return_value="test-key"), \
                 patch.dict(os.environ, {}, clear=False), \
                 patch("api.extract.pre_validate_figure", return_value=None):
                os.environ.pop("PAPER_CURATION_NO_GEMINI", None)
                figures = engine.extract_figures(str(pdf), str(out))
            return figures, calls

    def test_expand_verdict_on_full_box_costs_one_call(self):
        figures, calls = self._run(
            '{"status":"clipped","issues":"top","adjust_pt":{"top":40,"bottom":40,"left":0,"right":0}}')
        self.assertEqual(len(figures), 1)
        self.assertEqual(calls, ["gemini-3.1-pro-preview"],
                         "a clamped no-op adjustment must not re-send the identical crop")

    def test_shrink_verdict_still_gets_one_refinement_round(self):
        figures, calls = self._run(
            '{"status":"oversized","issues":"text","adjust_pt":{"top":0,"bottom":-20,"left":0,"right":0}}')
        self.assertEqual(len(figures), 1)
        self.assertEqual(len(calls), 2)

    def test_keyless_callers_never_reach_the_vision_model(self):
        with tempfile.TemporaryDirectory() as tmp:
            pdf = Path(tmp) / "paper.pdf"
            _synthetic_pdf(pdf)
            with patch.object(engine, "get_google_key", side_effect=AssertionError("key lookup")), \
                 patch("api.extract.pre_validate_figure", return_value=None):
                figures = engine.extract_figures(str(pdf), tmp, validate_with_gemini=False)
        self.assertEqual(len(figures), 1)


if __name__ == "__main__":
    unittest.main()
