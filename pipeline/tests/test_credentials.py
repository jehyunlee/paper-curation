"""Unit tests for the credential boundary; all keyring access is mocked."""

from __future__ import annotations

import io
import json
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import Mock, patch

from pipeline import credentials as cli
from pipeline.lib import credentials


class CredentialsTest(unittest.TestCase):
    def setUp(self):
        self.keyring = Mock()
        self.environment = patch.dict("os.environ", {}, clear=True)
        self.environment.start()
        self.addCleanup(self.environment.stop)

    def test_environment_precedes_keyring_without_importing_backend(self):
        with patch.dict("os.environ", {"ANTHROPIC_API_KEY": "from-env"}, clear=True), patch.object(
            credentials, "_keyring", side_effect=AssertionError("must not import keyring")
        ):
            self.assertEqual(credentials.resolve_credential("anthropic"), "from-env")

    def test_keyring_value_is_used_after_environment_aliases(self):
        self.keyring.get_password.return_value = "stored"
        with patch.object(credentials, "_keyring", return_value=self.keyring):
            self.assertEqual(credentials.resolve_credential("google", environ={}), "stored")
        self.keyring.get_password.assert_called_once_with("paper-curation", "google")

    def test_rejects_insecure_backend(self):
        backend = type("PlaintextKeyring", (), {"__module__": "keyrings.alt.file"})()
        module = Mock(get_keyring=Mock(return_value=backend))
        with patch.dict(sys.modules, {"keyring": module}):
            with self.assertRaisesRegex(credentials.CredentialsError, "unavailable or insecure"):
                credentials._keyring()

    def test_rejects_chainer_backend_even_if_children_are_not_inspected(self):
        backend = type("ChainerBackend", (), {"__module__": "keyring.backends.chainer"})()
        module = Mock(get_keyring=Mock(return_value=backend))
        with patch.dict(sys.modules, {"keyring": module}):
            with self.assertRaisesRegex(credentials.CredentialsError, "unavailable or insecure"):
                credentials._keyring()

    def test_rejects_unknown_backend(self):
        backend = type("Keyring", (), {"__module__": "custom.file_backend"})()
        module = Mock(get_keyring=Mock(return_value=backend))
        with patch.dict(sys.modules, {"keyring": module}):
            with self.assertRaisesRegex(credentials.CredentialsError, "unavailable or insecure"):
                credentials._keyring()

    def test_rejects_malicious_provider_and_reference(self):
        with self.assertRaises(credentials.CredentialsError):
            credentials.resolve_credential("anthropic;bad", environ={})
        with self.assertRaises(credentials.CredentialsError):
            credentials.resolve_credential("anthropic", "credential:openai", environ={})

    def test_diagnostics_and_errors_do_not_expose_values(self):
        secret = "do-not-leak"
        self.keyring.get_password.side_effect = RuntimeError(secret)
        with patch.object(credentials, "_keyring", return_value=self.keyring):
            status = credentials.credential_status("openai")
        self.assertNotIn(secret, str(status))
        self.assertEqual(status["status"], "unavailable")

    def test_delete_removes_exact_entry(self):
        with patch.object(credentials, "_keyring", return_value=self.keyring):
            credentials.delete_credential("scopus-inst")
        self.keyring.delete_password.assert_called_once_with("paper-curation", "scopus-inst")

    def test_cli_write_reads_stdin_and_never_accepts_value_argument(self):
        stdin = Mock()
        stdin.buffer = io.BytesIO(b"stdin-secret")
        stdout, stderr = io.StringIO(), io.StringIO()
        with patch.object(cli.sys, "stdin", stdin), patch.object(cli, "store_credential", return_value="credential:openai") as store, redirect_stdout(stdout), redirect_stderr(stderr):
            self.assertEqual(cli.main(["--operation", "write", "--provider", "openai"]), 0)
        self.assertEqual(store.call_args.args, ("openai", "stdin-secret"))
        self.assertNotIn("stdin-secret", stdout.getvalue())
        self.assertFalse(stderr.getvalue())

    def test_cli_read_is_a_json_private_pipe_contract(self):
        stdout = io.StringIO()
        with patch.object(cli, "resolve_credential", return_value="pipe-secret"), redirect_stdout(stdout):
            self.assertEqual(cli.main(["--operation", "read", "--provider", "zotero"]), 0)
        self.assertEqual(json.loads(stdout.getvalue()), {"reference": "credential:zotero", "value": "pipe-secret"})

    def test_cli_read_returns_empty_value_for_an_absent_credential(self):
        stdout = io.StringIO()
        with patch.object(cli, "resolve_credential", side_effect=credentials.CredentialNotConfigured()), redirect_stdout(stdout):
            self.assertEqual(cli.main(["--operation", "read", "--provider", "zotero"]), 0)
        self.assertEqual(json.loads(stdout.getvalue()), {"reference": "credential:zotero", "value": ""})


if __name__ == "__main__":
    unittest.main()
