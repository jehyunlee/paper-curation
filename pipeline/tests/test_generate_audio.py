import sys
import tempfile
import unittest
import json
from pathlib import Path
from unittest.mock import patch

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import generate_audio as audio


class AudioPublicationTests(unittest.TestCase):
    def _write_script(self, paper, *, review="review", **params):
        script = "전문가: 기존 대본입니다.\n리포터: 질문입니다."
        defaults = {
            "speakers": 2, "language": "ko", "audience": "student",
            "length": 10, "tone": "friendly", "focus": "",
            "direction": audio.DEFAULT_DIRECTION["ko"],
        }
        defaults.update(params)
        (paper / "audio_script.txt").write_text(script, encoding="utf-8")
        (paper / "audio_script.meta.json").write_text(json.dumps({
            "review_sha256": audio._sha256_text(review),
            "script_sha256": audio._sha256_text(script),
            "input_sha256": audio._script_input_hash(audio._sha256_text(review), defaults),
            "params": defaults,
            "script_model": audio.SCRIPT_MODEL,
        }), encoding="utf-8")

    def test_tts_failure_preserves_existing_mp3_and_reuses_valid_script(self):
        with tempfile.TemporaryDirectory() as tmp:
            papers = Path(tmp) / "papers"
            paper = papers / "0001_example"
            paper.mkdir(parents=True)
            (paper / "review.md").write_text("review", encoding="utf-8")
            self._write_script(paper)
            published = paper / "audio_overview.mp3"
            published.write_bytes(b"old mp3")

            with patch.object(audio, "PAPERS", papers), \
                 patch.object(audio, "resolve_slug", return_value="0001_example"), \
                 patch.object(audio, "resolve_credential", return_value="key"), \
                 patch.object(audio.genai, "Client"), \
                 patch.object(audio, "pool_synth", side_effect=RuntimeError("tts failed")) as synth:
                with self.assertRaisesRegex(RuntimeError, "tts failed"):
                    audio._run_audio("1")

            self.assertEqual(published.read_bytes(), b"old mp3")
            synth.assert_called_once()

    def test_changed_review_blocks_stale_script_before_tts(self):
        with tempfile.TemporaryDirectory() as tmp:
            papers = Path(tmp) / "papers"
            paper = papers / "0001_example"
            paper.mkdir(parents=True)
            (paper / "review.md").write_text("changed review", encoding="utf-8")
            self._write_script(paper)
            with patch.object(audio, "PAPERS", papers), \
                 patch.object(audio, "resolve_slug", return_value="0001_example"), \
                 patch.object(audio, "pool_synth") as synth:
                with self.assertRaisesRegex(RuntimeError, "provenance"):
                    audio._run_audio("1")
            synth.assert_not_called()

    def test_exact_provenance_reuses_script_without_script_model_call(self):
        with tempfile.TemporaryDirectory() as tmp:
            papers = Path(tmp) / "papers"
            paper = papers / "0001_example"
            paper.mkdir(parents=True)
            (paper / "review.md").write_text("review", encoding="utf-8")
            self._write_script(paper)
            with patch.object(audio, "PAPERS", papers), \
                 patch.object(audio, "resolve_slug", return_value="0001_example"), \
                 patch.object(audio, "resolve_credential", return_value="key"), \
                 patch.object(audio.genai, "Client") as client, \
                 patch.object(audio, "pool_synth", side_effect=RuntimeError("tts failed")):
                with self.assertRaisesRegex(RuntimeError, "tts failed"):
                    audio._run_audio("1")
            client.return_value.models.generate_content.assert_not_called()


if __name__ == "__main__":
    unittest.main()
