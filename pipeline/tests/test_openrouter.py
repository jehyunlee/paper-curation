"""Unit tests for OpenRouter client + Anthropic shim + Hermes image extract."""
from __future__ import annotations

import base64
import io
import json
import os
import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE))


def _tiny_png_bytes() -> bytes:
    from PIL import Image
    buf = io.BytesIO()
    Image.new("RGB", (8, 8), color=(20, 40, 60)).save(buf, format="PNG")
    return buf.getvalue()


class TestOpenRouterConfig(unittest.TestCase):
    def test_get_openrouter_config_from_env(self):
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "sk-or-test-1"}, clear=False):
            # Bust config_loader cache
            import config_loader as cl
            cl._config_cache = None
            cfg = cl.get_openrouter_config()
            self.assertIsNotNone(cfg)
            self.assertEqual(cfg["api_key"], "sk-or-test-1")
            self.assertEqual(cfg["models"]["embed"], "qwen/qwen3-embedding-8b")
            self.assertEqual(cfg["embed_dimensions"], 768)

    def test_get_openrouter_config_missing(self):
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": ""}, clear=False):
            import config_loader as cl
            cl._config_cache = {"openrouter": {}}
            cfg = cl.get_openrouter_config()
            self.assertIsNone(cfg)

    def test_get_hermes_config(self):
        with patch.dict(os.environ, {
            "HERMES_GATEWAY_BASE_URL": "http://localhost:8642/v1",
            "HERMES_GATEWAY_API_KEY": "hk-test",
            "HERMES_GATEWAY_MODEL": "hermes-agent",
        }, clear=False):
            import config_loader as cl
            cl._config_cache = {}
            cfg = cl.get_hermes_config()
            self.assertIsNotNone(cfg)
            self.assertEqual(cfg["model"], "hermes-agent")
            self.assertTrue(cfg["base_url"].endswith("/v1"))


class TestModelResolve(unittest.TestCase):
    def test_alias_mapping(self):
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "sk-or-x"}, clear=False):
            import config_loader as cl
            cl._config_cache = None
            from lib.openrouter import resolve_openrouter_model
            self.assertEqual(
                resolve_openrouter_model("claude-sonnet-5"),
                "anthropic/claude-sonnet-5")
            self.assertEqual(
                resolve_openrouter_model("claude-haiku-4-5"),
                "anthropic/claude-haiku-4.5")
            self.assertEqual(
                resolve_openrouter_model(None, "embed"),
                "qwen/qwen3-embedding-8b")


class TestAnthropicShim(unittest.TestCase):
    def test_text_response(self):
        fake = {
            "choices": [{
                "message": {"role": "assistant", "content": "hello world"},
            }],
        }
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "sk-or-x"}, clear=False):
            import config_loader as cl
            cl._config_cache = None
            from lib.openrouter import OpenRouterAnthropicShim
            with patch("lib.openrouter.chat", return_value=fake) as m:
                client = OpenRouterAnthropicShim(timeout=10)
                resp = client.messages.create(
                    model="claude-sonnet-5",
                    max_tokens=100,
                    messages=[{"role": "user", "content": "hi"}],
                )
                self.assertEqual(resp.content[0].text, "hello world")
                self.assertEqual(resp.content[0].type, "text")
                self.assertTrue(m.called)

    def test_tool_use_conversion(self):
        fake = {
            "choices": [{
                "message": {
                    "role": "assistant",
                    "content": None,
                    "tool_calls": [{
                        "id": "call_1",
                        "type": "function",
                        "function": {
                            "name": "emit_review",
                            "arguments": json.dumps({"title": "T", "score": 1}),
                        },
                    }],
                },
            }],
        }
        tools = [{
            "name": "emit_review",
            "description": "emit",
            "input_schema": {
                "type": "object",
                "properties": {"title": {"type": "string"}, "score": {"type": "integer"}},
                "required": ["title", "score"],
            },
        }]
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "sk-or-x"}, clear=False):
            import config_loader as cl
            cl._config_cache = None
            from lib.openrouter import OpenRouterAnthropicShim
            with patch("lib.openrouter.chat", return_value=fake):
                client = OpenRouterAnthropicShim()
                resp = client.messages.create(
                    model="claude-sonnet-5",
                    max_tokens=500,
                    tools=tools,
                    tool_choice={"type": "tool", "name": "emit_review"},
                    messages=[{"role": "user", "content": "review"}],
                )
                block = resp.content[0]
                self.assertEqual(block.type, "tool_use")
                self.assertEqual(block.name, "emit_review")
                self.assertEqual(block.input["title"], "T")

    def test_json_fallback_tool_use(self):
        fake = {
            "choices": [{
                "message": {
                    "role": "assistant",
                    "content": '```json\n{"title": "X", "score": 2}\n```',
                },
            }],
        }
        tools = [{
            "name": "emit_review",
            "description": "emit",
            "input_schema": {"type": "object", "properties": {}},
        }]
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "sk-or-x"}, clear=False):
            import config_loader as cl
            cl._config_cache = None
            from lib.openrouter import OpenRouterAnthropicShim
            with patch("lib.openrouter.chat", return_value=fake):
                client = OpenRouterAnthropicShim()
                resp = client.messages.create(
                    model="claude-haiku-4-5",
                    max_tokens=200,
                    tools=tools,
                    tool_choice={"type": "tool", "name": "emit_review"},
                    messages=[{"role": "user", "content": "x"}],
                )
                self.assertEqual(resp.content[0].type, "tool_use")
                self.assertEqual(resp.content[0].input["title"], "X")

    def test_stream_text(self):
        fake = {
            "choices": [{
                "message": {"role": "assistant", "content": "streamed"},
            }],
        }
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "sk-or-x"}, clear=False):
            import config_loader as cl
            cl._config_cache = None
            from lib.openrouter import OpenRouterAnthropicShim
            with patch("lib.openrouter.chat", return_value=fake):
                client = OpenRouterAnthropicShim()
                text = ""
                with client.messages.stream(
                    model="claude-opus-5",
                    max_tokens=50,
                    messages=[{"role": "user", "content": "hi"}],
                ) as stream:
                    for chunk in stream.text_stream:
                        text += chunk
                self.assertEqual(text, "streamed")


class TestEmbed(unittest.TestCase):
    def test_embed_normalizes(self):
        raw = [3.0, 4.0] + [0.0] * 766
        fake = {
            "data": [{"index": 0, "embedding": raw}],
        }
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "sk-or-x"}, clear=False):
            import config_loader as cl
            cl._config_cache = None
            from lib import openrouter as orouter
            with patch("lib.openrouter._post_json", return_value=fake):
                vecs = orouter.embed(["hello"], dimensions=768)
                self.assertEqual(len(vecs), 1)
                self.assertEqual(len(vecs[0]), 768)
                # 3-4-5 triangle → unit vector
                self.assertAlmostEqual(vecs[0][0], 0.6, places=5)
                self.assertAlmostEqual(vecs[0][1], 0.8, places=5)


class TestHermesImage(unittest.TestCase):
    def test_extract_from_markdown_data_uri(self):
        png = _tiny_png_bytes()
        b64 = base64.b64encode(png).decode("ascii")
        resp = {
            "choices": [{
                "message": {
                    "content": f"Here you go:\n![diagram](data:image/png;base64,{b64})\n",
                },
            }],
        }
        from lib.hermes_image import extract_image_bytes
        out = extract_image_bytes(resp)
        self.assertIsNotNone(out)
        self.assertTrue(out[:8] == b"\x89PNG\r\n\x1a\n")

    def test_extract_from_images_array(self):
        png = _tiny_png_bytes()
        b64 = base64.b64encode(png).decode("ascii")
        resp = {
            "choices": [{
                "message": {
                    "content": "ok",
                    "images": [{"image_url": {"url": f"data:image/png;base64,{b64}"}}],
                },
            }],
        }
        from lib.hermes_image import extract_image_bytes
        out = extract_image_bytes(resp)
        self.assertIsNotNone(out)
        self.assertGreater(len(out), 20)

    def test_generate_diagram_mock_chat(self):
        png = _tiny_png_bytes()
        b64 = base64.b64encode(png).decode("ascii")
        chat_resp = {
            "choices": [{
                "message": {
                    "content": f"![img](data:image/png;base64,{b64})",
                },
            }],
        }
        cfg = {
            "base_url": "http://localhost:8642/v1",
            "api_key": "hk",
            "model": "hermes-agent",
            "timeout": 10,
        }
        from lib import hermes_image

        def fake_post(_cfg, path, _payload):
            if "images" in path:
                raise RuntimeError("no images api")
            return chat_resp

        with patch.object(hermes_image, "_post", side_effect=fake_post):
            out = hermes_image.generate_diagram(
                "# Method\nboxes", "A flowchart", aspect_ratio="16:9", cfg=cfg)
        self.assertIsNotNone(out)
        self.assertTrue(out.startswith(b"\x89PNG"))

    def test_paperbanana_prefers_hermes(self):
        png = _tiny_png_bytes()
        with patch.dict(os.environ, {
            "HERMES_GATEWAY_BASE_URL": "http://localhost:8642/v1",
            "HERMES_GATEWAY_API_KEY": "hk",
        }, clear=False):
            import config_loader as cl
            cl._config_cache = {}
            # Avoid requiring PaperBanana dir
            with patch("lib.hermes_image.generate_diagram", return_value=png) as m:
                # Import after env is set; paperbanana may have cached PAPERBANANA_DIR
                import importlib
                import lib.paperbanana as pb
                importlib.reload(pb)
                out = pb.generate_diagram("method", "caption")
                self.assertEqual(out, png)
                self.assertTrue(m.called)


class TestLlmClientFactory(unittest.TestCase):
    def test_get_chat_client_openrouter(self):
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "sk-or-x"}, clear=False):
            import config_loader as cl
            cl._config_cache = None
            from lib.llm_client import get_chat_client, resolve_model
            client = get_chat_client()
            self.assertTrue(hasattr(client, "messages"))
            self.assertIn("anthropic/", resolve_model("sonnet"))


if __name__ == "__main__":
    unittest.main()
