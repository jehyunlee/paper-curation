"""Tests for Anthropic client credential resolution."""

from __future__ import annotations

import unittest
from unittest.mock import Mock, patch

from pipeline.lib import credentials


class AnthropicClientTest(unittest.TestCase):
    def test_resolved_credential_is_passed_as_api_key(self):
        client = Mock()
        with patch("anthropic.Anthropic", return_value=client) as constructor, patch.object(
            credentials, "resolve_credential", return_value="keyring-key"
        ):
            self.assertIs(credentials.anthropic_client(timeout=12.0), client)

        constructor.assert_called_once_with(api_key="keyring-key", timeout=12.0)

    def test_missing_credential_uses_sdk_default_lookup(self):
        client = Mock()
        with patch("anthropic.Anthropic", return_value=client) as constructor, patch.object(
            credentials,
            "resolve_credential",
            side_effect=credentials.CredentialNotConfigured("credential is not configured"),
        ):
            self.assertIs(credentials.anthropic_client(max_retries=2), client)

        constructor.assert_called_once_with(max_retries=2)

    def test_kwargs_pass_through_with_resolved_key(self):
        with patch("anthropic.Anthropic") as constructor, patch.object(
            credentials, "resolve_credential", return_value="configured-key"
        ):
            credentials.anthropic_client(timeout=180.0, max_retries=4)

        constructor.assert_called_once_with(
            api_key="configured-key", timeout=180.0, max_retries=4
        )


if __name__ == "__main__":
    unittest.main()
