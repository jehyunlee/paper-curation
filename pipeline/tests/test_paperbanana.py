import os
import tempfile
import unittest
from pathlib import Path

from pipeline.lib.paperbanana import _resolve_output_path


class PaperBananaOutputPathTests(unittest.TestCase):
    def test_relative_output_is_resolved_before_workdir_change(self):
        original = Path.cwd()
        with tempfile.TemporaryDirectory() as tmp:
            os.chdir(tmp)
            try:
                resolved = _resolve_output_path("artifacts/timeline.png")
            finally:
                os.chdir(original)

        self.assertEqual(
            resolved,
            Path(tmp).resolve() / "artifacts" / "timeline.png",
        )

    def test_none_output_stays_none(self):
        self.assertIsNone(_resolve_output_path(None))


if __name__ == "__main__":
    unittest.main()
