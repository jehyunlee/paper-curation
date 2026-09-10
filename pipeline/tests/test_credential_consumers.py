"""Credential-consumer contracts; all OS-keyring access is mocked."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, call, patch

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import config_loader  # noqa: E402
import serve_local  # noqa: E402
from lib import credentials  # noqa: E402
from lib.citedby import scopus  # noqa: E402


class CredentialConsumerTests(unittest.TestCase):
    def setUp(self):
        self.environment = patch.dict("os.environ", {}, clear=True)
        self.environment.start()
        self.addCleanup(self.environment.stop)
        scopus._api_keys = None
        scopus._key_index = 0
        scopus._key_origin = ""
        config_loader._user_id_cache = None
        self.addCleanup(self._reset_scopus_cache)

    @staticmethod
    def _reset_scopus_cache():
        scopus._api_keys = None
        scopus._key_index = 0
        scopus._key_origin = ""

    def test_config_helpers_use_environment_before_keyring(self):
        with patch.dict("os.environ", {
            "ZOTERO_API_KEY": "zotero-env",
            "GEMINI_API_KEY": "google-env",
        }, clear=True), patch.object(
            credentials, "_keyring",
            side_effect=AssertionError("environment must precede keyring"),
        ):
            self.assertEqual(config_loader.get_zotero_api_key(), "zotero-env")
            self.assertEqual(config_loader.get_google_key(), "google-env")

    def test_config_helpers_use_os_store_and_ignore_config_loader(self):
        keyring = Mock()
        keyring.get_password.side_effect = ["zotero-store", "google-store"]
        with patch.object(config_loader, "load_config",
                          side_effect=AssertionError("plaintext config must not be read")), patch.object(
            credentials, "_keyring", return_value=keyring,
        ):
            self.assertEqual(config_loader.get_zotero_api_key(), "zotero-store")
            self.assertEqual(config_loader.get_google_key(), "google-store")
        self.assertEqual(
            keyring.get_password.call_args_list,
            [
                call("paper-curation", "zotero"),
                call("paper-curation", "google"),
            ],
        )

    def test_missing_zotero_credential_is_unavailable_without_network(self):
        with patch.object(
            config_loader, "resolve_credential",
            side_effect=credentials.CredentialNotConfigured(),
        ), patch.object(
            config_loader.urllib.request, "urlopen",
            side_effect=AssertionError("missing credential must not call Zotero"),
        ):
            self.assertEqual(config_loader.get_zotero_api_key(), "")
            with self.assertRaisesRegex(ValueError, "환경변수 또는 OS 보안 저장소"):
                config_loader.get_zotero_user_id()

    def test_scopus_uses_shared_resolvers_not_source_files(self):
        with patch.object(
            scopus, "resolve_credential",
            side_effect=["key-one,key-two", "institution-token"],
        ) as resolve:
            self.assertEqual(scopus.get_api_keys(), ["key-one", "key-two"])
            self.assertEqual(scopus.inst_token(), "institution-token")
        self.assertEqual(
            resolve.call_args_list,
            [call("scopus"), call("scopus-inst")],
        )
        self.assertEqual(scopus.key_origin(), "credential:scopus")

    def test_missing_scopus_credential_is_unavailable_without_network(self):
        with patch.object(
            scopus, "resolve_credential",
            side_effect=credentials.CredentialNotConfigured(),
        ):
            self.assertEqual(scopus.available(), (False,
                "Scopus API key not found. Set SCOPUS_API_KEY/ELSEVIER_API_KEY "
                "or credential:scopus in the OS secure store."))

    def test_server_credentials_ignore_plaintext_and_refresh_os_store(self):
        plaintext = {
            "google_api_key": "plaintext-google",
            "resend_api_key": "plaintext-resend",
            "audio_from": "Configured <sender@example.test>",
            "audio_reply_to": "reply@example.test",
        }
        with patch.object(serve_local, "load_config", return_value=plaintext), patch.object(
            serve_local, "resolve_credential",
            side_effect=["google-store-v1", "google-store-v2", "resend-store"],
        ) as resolve:
            self.assertEqual(serve_local.resolve_google_key(), "google-store-v1")
            self.assertEqual(serve_local.resolve_google_key(), "google-store-v2")
            self.assertEqual(
                serve_local.resolve_resend_config(),
                ("resend-store", "Configured <sender@example.test>", "reply@example.test"),
            )
        self.assertEqual(
            resolve.call_args_list,
            [call("google"), call("google"), call("resend")],
        )


if __name__ == "__main__":
    unittest.main()
