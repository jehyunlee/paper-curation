"""Oversized category blocks must be compressed within Haiku's context window."""
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import extract_insights as insights


class FakeMessages:
    def __init__(self, calls):
        self.calls = calls

    def create(self, *, model, max_tokens, messages):
        prompt = messages[0]["content"]
        self.calls.append(insights._est_tokens(prompt))
        block = prompt.split("INPUT:\n", 1)[1]
        header = block.partition("\n")[0]
        return SimpleNamespace(content=[SimpleNamespace(
            type="text", text=f"{header}\n  [001] condensed themes")])


class FakeClient:
    def __init__(self):
        self.calls = []
        self.messages = FakeMessages(self.calls)

    def with_options(self, **_kwargs):
        return self


class HaikuBlockCompressionTests(unittest.TestCase):
    def test_oversized_block_is_compressed_in_bounded_chunks(self):
        header = "### Autonomous AI Scientific Discovery (900 papers)"
        lines = [f"  [{i:04d}] (2026) Paper {i} | " + "essence " * 60
                 for i in range(900)]
        block = header + "\n" + "\n".join(lines)
        client = FakeClient()

        with patch.object(insights, "_HAIKU_MAX_INPUT_TOKENS", 20000):
            self.assertGreater(insights._est_tokens(block), 20000)
            result = insights._haiku_summarize_block(block, client, 4000)

        self.assertGreater(len(client.calls), 1)
        self.assertTrue(all(tokens <= 20000 for tokens in client.calls))
        self.assertTrue(result.startswith(header))
        self.assertEqual(result.count(header), 1)

    def test_small_block_uses_one_call(self):
        block = "### Small (2 papers)\n  [001] (2026) A | x\n  [002] (2026) B | y"
        client = FakeClient()

        result = insights._haiku_summarize_block(block, client, 4000)

        self.assertEqual(len(client.calls), 1)
        self.assertTrue(result.startswith("### Small (2 papers)"))


if __name__ == "__main__":
    unittest.main()
