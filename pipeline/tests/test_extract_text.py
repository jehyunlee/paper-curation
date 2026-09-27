"""Regression coverage for OpenDataLoader text extraction fallbacks."""
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch

PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE))
import run_update_force as engine  # noqa: E402


class NormalizeOdlMarkdownImagesTests(unittest.TestCase):
    def test_normalizes_odl_images_without_touching_ordinary_links(self):
        text = (
            "Legacy ![image 7](Legacy_images/imageFile7.png)\n"
            "New ![](<Some Paper_images/imageFile11.png>)\n"
            "Underscore ![](<Some Paper_images/image_011.png>)\n"
            "Spaced ![](<Some Paper_images/image 12.png>)\n"
            "Unknown ![](<Some Paper_images/diagram.png>)\n"
            "[Documentation](https://example.test/docs)\n"
            "![Normal chart](figures/chart.png)"
        )

        self.assertEqual(
            engine._normalize_odl_markdown_images(text),
            "Legacy [Figure 7]\n"
            "New [Figure 11]\n"
            "Underscore [Figure 11]\n"
            "Spaced [Figure 12]\n"
            "Unknown [Figure]\n"
            "[Documentation](https://example.test/docs)\n"
            "![Normal chart](figures/chart.png)",
        )

    def test_collapses_excess_newlines(self):
        self.assertEqual(
            engine._normalize_odl_markdown_images("Before\n\n\n\nAfter"),
            "Before\n\nAfter",
        )


class ExtractTextTests(unittest.TestCase):
    def test_odl_2511_markdown_writes_figure_placeholders(self):
        odl = types.ModuleType("opendataloader_pdf")
        source = (
            "# Synthetic paper\n\n"
            "![](<Some Paper_images/imageFile11.png>)\n\n"
            "![](<Some Paper_images/unknown-diagram.png>)\n\n"
            "Body text " + "evidence " * 20
        )

        def convert(*, output_dir, **_kwargs):
            Path(output_dir, "paper.md").write_text(source, encoding="utf-8")

        odl.convert = convert
        with tempfile.TemporaryDirectory() as tmp, patch.dict(
            sys.modules, {"opendataloader_pdf": odl}
        ):
            slug_dir = Path(tmp) / "paper"
            slug_dir.mkdir()
            self.assertTrue(engine.extract_text("ignored.pdf", str(slug_dir)))
            output = (slug_dir / "text.md").read_text(encoding="utf-8")

        self.assertIn("[Figure 11]", output)
        self.assertIn("[Figure]", output)
        self.assertNotIn("_images/", output)

    def test_unavailable_odl_logs_warning_and_uses_pymupdf(self):
        fallback_text = "PyMuPDF fallback text " * 10
        page = types.SimpleNamespace(get_text=lambda: fallback_text)

        class Document:
            def __len__(self):
                return 1

            def __getitem__(self, index):
                return page

            def close(self):
                pass

        fitz = types.ModuleType("fitz")
        fitz.open = lambda _path: Document()

        with tempfile.TemporaryDirectory() as tmp, patch.dict(
            sys.modules, {"opendataloader_pdf": None, "fitz": fitz}
        ), patch.object(engine, "log") as log:
            slug_dir = Path(tmp) / "paper"
            slug_dir.mkdir()
            self.assertTrue(engine.extract_text("ignored.pdf", str(slug_dir)))
            output = (slug_dir / "text.md").read_text(encoding="utf-8")

        self.assertEqual(output, fallback_text)
        warning = log.call_args.args[0]
        self.assertIn("OpenDataLoader unavailable", warning)
        self.assertIn("falling back to PyMuPDF", warning)
        self.assertIn("pip install -r requirements.txt", warning)


if __name__ == "__main__":
    unittest.main()
