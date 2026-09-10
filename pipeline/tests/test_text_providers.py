import os
import json
import sys
import unittest
import weakref
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lib.text_providers import (ProviderSelectionError, ProviderTruncatedError,
                                ProviderResponseError, UnsupportedCapabilityError,
                                generate_structured)


class TextProviderTests(unittest.TestCase):
    def _generate(self, provider):
        return generate_structured(provider, None, "system", "prompt", {"type": "object"},
                                   capability="summary", max_output_tokens=7)

    def test_cloud_clients_disable_implicit_retries_and_bound_output(self):
        anthropic_client = unittest.mock.Mock()
        anthropic_client.return_value.messages.create.return_value = SimpleNamespace(
            stop_reason="tool_use",
            content=[SimpleNamespace(type="tool_use", name="emit_json", input={"ok": True})],
            usage=SimpleNamespace(input_tokens=1, output_tokens=2))
        openai_client = unittest.mock.Mock()
        openai_client.return_value.chat.completions.create.return_value = SimpleNamespace(
            choices=[SimpleNamespace(finish_reason="stop", message=SimpleNamespace(content='{"ok": true}'))],
            usage=SimpleNamespace(prompt_tokens=1, completion_tokens=2))
        google_client = unittest.mock.Mock()
        google_client.return_value.models.generate_content.return_value = SimpleNamespace(
            text='{"ok": true}', candidates=[], usage_metadata=SimpleNamespace(
                prompt_token_count=1, candidates_token_count=2))
        anthropic = SimpleNamespace(Anthropic=anthropic_client)
        openai = SimpleNamespace(OpenAI=openai_client)
        retry_options = unittest.mock.Mock()
        http_options = unittest.mock.Mock()
        generate_config = unittest.mock.Mock()
        google_genai = SimpleNamespace(Client=google_client, types=SimpleNamespace(
            HttpOptions=http_options, HttpRetryOptions=retry_options,
            GenerateContentConfig=generate_config))
        with patch("lib.text_providers._credential", return_value="secret"), patch.dict(
                sys.modules, {"anthropic": anthropic, "openai": openai,
                              "google": SimpleNamespace(genai=google_genai),
                              "google.genai": google_genai,
                              "google.genai.types": google_genai.types}):
            self._generate("anthropic")
            self._generate("openai")
            self._generate("google")
        self.assertEqual(anthropic_client.call_args.kwargs["max_retries"], 0)
        self.assertEqual(openai_client.call_args.kwargs["max_retries"], 0)
        self.assertEqual(anthropic_client.return_value.messages.create.call_args.kwargs["max_tokens"], 7)
        self.assertEqual(openai_client.return_value.chat.completions.create.call_args.kwargs["max_completion_tokens"], 7)
        self.assertEqual(generate_config.call_args.kwargs["max_output_tokens"], 7)
        self.assertEqual(retry_options.call_args.kwargs["attempts"], 1)

    def test_ollama_only_permits_loopback(self):
        with patch.dict(os.environ, {"OLLAMA_URL": "http://example.test:11434"}):
            with self.assertRaises(ProviderSelectionError):
                generate_structured("ollama", None, "s", "p", {"type": "object"},
                                    capability="summary", max_output_tokens=4)

    def test_mlx_prompt_enforces_json_even_without_decoding_grammar(self):
        with patch("lib.text_providers.urlopen") as open_call:
            response = open_call.return_value.__enter__.return_value
            response.read.return_value = b'{"done": true, "done_reason": "stop", "response": "{\\"ok\\": true}"}'
            result = self._generate("ollama")
        request = json.loads(open_call.call_args.args[0].data)
        self.assertFalse(request["think"])
        self.assertIn("Return ONLY a JSON object", request["system"])
        self.assertIn(json.dumps(request["format"]), request["system"])
        self.assertEqual(result["data"], {"ok": True})

    def test_google_client_remains_alive_through_request(self):
        class Models:
            def __init__(self, owner):
                self.owner = weakref.ref(owner)

            def generate_content(self, **kwargs):
                if self.owner() is None:
                    raise RuntimeError("client was closed before request")
                return SimpleNamespace(
                    text='{"ok": true}', candidates=[], usage_metadata=None)

        class Client:
            def __init__(self, **kwargs):
                self.models = Models(self)

        with patch("lib.text_providers._credential", return_value="test"), patch("google.genai.Client", Client):
            self.assertEqual(self._generate("google")["data"], {"ok": True})

    def test_ollama_server_down_does_not_fallback(self):
        with patch.dict(os.environ, {"OLLAMA_URL": "http://127.0.0.1:1"}):
            with self.assertRaises(Exception) as raised:
                generate_structured("ollama", None, "s", "p", {"type": "object"},
                                    capability="summary", max_output_tokens=4)
        self.assertNotIn("key", str(raised.exception).lower())

    def test_review_rejects_ollama_before_network(self):
        with self.assertRaises(UnsupportedCapabilityError):
            generate_structured("ollama", None, "s", "p", {"type": "object"},
                                capability="review", max_output_tokens=4)

    def test_truncated_ollama_response_fails(self):
        with patch("lib.text_providers.urlopen") as open_call:
            response = open_call.return_value.__enter__.return_value
            response.read.return_value = b'{"done": false, "response": "{}"}'
            with self.assertRaises(ProviderTruncatedError):
                generate_structured("ollama", None, "s", "p", {"type": "object"},
                                    capability="summary", max_output_tokens=4)

    def test_schema_rejects_wrong_field_type(self):
        with patch("lib.text_providers.urlopen") as open_call:
            response = open_call.return_value.__enter__.return_value
            response.read.return_value = b'{"done": true, "response": "{\\"score\\": \\"five\\"}"}'
            with self.assertRaises(ProviderResponseError):
                generate_structured("ollama", None, "s", "p",
                                    {"type": "object", "properties": {"score": {"type": "integer"}}, "required": ["score"]},
                                    capability="summary", max_output_tokens=4)


if __name__ == "__main__": unittest.main()
