"""Focused contracts for the keyless setup entry point."""

import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import Mock, patch

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import setup


CREDENTIAL_ENV = (
    "ANTHROPIC_API_KEY",
    "GOOGLE_API_KEY",
    "GEMINI_API_KEY",
    "RESEND_API_KEY",
    "ZOTERO_API_KEY",
)


def empty_credentials(**overrides):
    values = {name: "" for name in CREDENTIAL_ENV}
    values.update(overrides)
    return values


class KeylessSetupTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        self.config_path = self.root / "config.json"
        self.template_path = self.root / "SKILL.md.template"
        self.skill_output = self.root / "SKILL.md"
        self.install_dir = self.root / "installed-skill"
        self.papers_dir = self.root / "docs" / "papers"
        self.template_path.write_text(
            "project={project_dir}\nrepo={github_repo}\npapers={zotero_dir}\n",
            encoding="utf-8",
        )

        constants = {
            "REPO": self.root,
            "CONFIG_PATH": self.config_path,
            "TEMPLATE_PATH": self.template_path,
            "SKILL_OUTPUT": self.skill_output,
            "SKILL_INSTALL_DIR": self.install_dir,
            "LOCAL_PAPERS_DIR": self.papers_dir,
        }
        self.patchers = [patch.object(setup, name, value) for name, value in constants.items()]
        backend = Mock()
        backend.get_password.return_value = None
        self.patchers.append(patch("lib.credentials._keyring", return_value=backend))
        for patcher in self.patchers:
            patcher.start()

    def tearDown(self):
        for patcher in reversed(self.patchers):
            patcher.stop()
        self.tempdir.cleanup()

    def test_default_install_is_keyless_and_has_no_external_side_effects(self):
        output = io.StringIO()
        with (
            patch.dict(os.environ, empty_credentials(), clear=False),
            patch("builtins.input", side_effect=AssertionError("setup must not prompt")) as prompt,
            patch.object(setup.urllib.request, "urlopen") as urlopen,
            patch.object(subprocess, "run") as run,
            patch.object(setup, "check_keyword_search") as keyword_check,
            redirect_stdout(output),
        ):
            exit_code = setup.main([])

        self.assertEqual(exit_code, 0)
        prompt.assert_not_called()
        urlopen.assert_not_called()
        run.assert_not_called()
        keyword_check.assert_not_called()
        self.assertEqual(
            json.loads(self.config_path.read_text(encoding="utf-8")),
            {"zotero": {"collections": {}}},
        )
        self.assertTrue(self.papers_dir.is_dir())
        self.assertTrue(self.skill_output.is_file())
        self.assertEqual(
            (self.install_dir / "SKILL.md").read_text(encoding="utf-8"),
            self.skill_output.read_text(encoding="utf-8")
            + "\n\nInstalled checkout (local-only): "
            + json.dumps(str(self.root), ensure_ascii=False) + "\n",
        )
        self.assertIn("전체 파이프라인은 실행하지 않았습니다", output.getvalue())
        self.assertIn(
            f"--check-feature {{{','.join(setup.FEATURE_CHOICES)}}}",
            output.getvalue(),
        )

    def test_existing_config_loads_without_copying_environment_keys(self):
        original = {"zotero": {"collections": {"local": "Existing"}}}
        self.config_path.write_text(json.dumps(original), encoding="utf-8")
        env = empty_credentials(
            ANTHROPIC_API_KEY="anthropic-env",
            GOOGLE_API_KEY="google-env",
            RESEND_API_KEY="resend-env",
            ZOTERO_API_KEY="zotero-env",
        )
        with patch.dict(os.environ, env, clear=False):
            loaded = setup.step_config()

        self.assertEqual(loaded, original)
        self.assertEqual(
            json.loads(self.config_path.read_text(encoding="utf-8")), original
        )

    def test_no_install_preserves_manual_generation_and_skips_copy(self):
        with (
            patch.dict(os.environ, empty_credentials(), clear=False),
            patch.object(setup, "step_install") as install,
            redirect_stdout(io.StringIO()) as output,
        ):
            exit_code = setup.main(["--no-install"])

        self.assertEqual(exit_code, 0)
        self.assertTrue(self.skill_output.is_file())
        install.assert_not_called()
        self.assertIn("수동 설치", output.getvalue())


class FeatureDiagnosticTests(unittest.TestCase):
    def setUp(self):
        backend = Mock()
        backend.get_password.return_value = None
        self.keyring_patch = patch("lib.credentials._keyring", return_value=backend)
        self.keyring_patch.start()
        self.addCleanup(self.keyring_patch.stop)

    def test_anthropic_only_satisfies_review(self):
        with (
            patch.dict(
                os.environ,
                empty_credentials(ANTHROPIC_API_KEY="anthropic-env"),
                clear=False,
            ),
            patch.object(setup.urllib.request, "urlopen") as urlopen,
        ):
            results = {
                name: setup.check_feature(name, {})
                for name in setup.FEATURE_CHOICES
            }

        self.assertTrue(results["review"]["ok"])
        self.assertEqual(results["review"]["status"], "configured_unverified")
        self.assertEqual(results["review"]["authorization"], "not_checked")
        self.assertFalse(results["semantic-search"]["ok"])
        self.assertFalse(results["audio"]["ok"])
        self.assertFalse(results["email"]["ok"])
        self.assertFalse(results["zotero-sync"]["ok"])
        urlopen.assert_not_called()

    def test_keyword_search_is_keyless_local_bm25(self):
        with tempfile.TemporaryDirectory() as tempdir:
            builder = Path(tempdir) / "build_search_index.py"
            query = Path(tempdir) / "query_search_index.py"
            builder.write_text("", encoding="utf-8")
            query.write_text("", encoding="utf-8")
            with (
                patch.dict(os.environ, empty_credentials(), clear=False),
                patch.object(setup.sys, "version_info", (3, 12, 0)),
                patch.object(setup, "BUILD_SEARCH_INDEX_PATH", builder),
                patch.object(setup, "QUERY_SEARCH_INDEX_PATH", query),
                patch.object(
                    setup,
                    "_credential_source",
                    side_effect=AssertionError("keyword search must not inspect credentials"),
                ) as credential_source,
                patch.object(setup.urllib.request, "urlopen") as urlopen,
            ):
                result = setup.check_feature("keyword-search", {})

        self.assertEqual(
            result,
            {
                "feature": "keyword-search",
                "ok": True,
                "status": "ready",
                "credential": None,
                "credential_source": None,
                "authorization": "not_required",
                "message": (
                    "로컬 BM25 키워드 검색 준비 완료. 의미 검색이나 생성형 답변은 포함하지 않습니다. "
                    "빌드: python3.12 pipeline/build_search_index.py --topic TOPIC --mode bm25; "
                    "조회: python3.12 pipeline/query_search_index.py --topic TOPIC --query QUERY --mode bm25"
                ),
            },
        )
        credential_source.assert_not_called()
        urlopen.assert_not_called()

    def test_keyword_search_reports_unavailable_local_runtime(self):
        with tempfile.TemporaryDirectory() as tempdir:
            missing_builder = Path(tempdir) / "build_search_index.py"
            missing_query = Path(tempdir) / "query_search_index.py"
            with (
                patch.object(setup.sys, "version_info", (3, 11, 9)),
                patch.object(setup, "BUILD_SEARCH_INDEX_PATH", missing_builder),
                patch.object(setup, "QUERY_SEARCH_INDEX_PATH", missing_query),
            ):
                result = setup.check_keyword_search({})

        self.assertFalse(result["ok"])
        self.assertEqual(result["status"], "runtime_unavailable")
        self.assertIsNone(result["credential"])
        self.assertIsNone(result["credential_source"])
        self.assertEqual(result["authorization"], "not_required")
        self.assertIn("Python 3.12 정확히 필요 (현재 3.11)", result["message"])
        self.assertIn("pipeline/build_search_index.py", result["message"])
        self.assertIn("pipeline/query_search_index.py", result["message"])
        self.assertIn("의미 검색이나 생성형 답변 진단이 아닙니다", result["message"])

    def test_keyword_search_rejects_python_314(self):
        with tempfile.TemporaryDirectory() as tempdir:
            builder = Path(tempdir) / "build_search_index.py"
            query = Path(tempdir) / "query_search_index.py"
            builder.write_text("", encoding="utf-8")
            query.write_text("", encoding="utf-8")
            with (
                patch.object(setup.sys, "version_info", (3, 14, 0)),
                patch.object(setup, "BUILD_SEARCH_INDEX_PATH", builder),
                patch.object(setup, "QUERY_SEARCH_INDEX_PATH", query),
            ):
                result = setup.check_keyword_search({})

        self.assertFalse(result["ok"])
        self.assertEqual(result["status"], "runtime_unavailable")
        self.assertEqual(result["authorization"], "not_required")
        self.assertIn("Python 3.12 정확히 필요 (현재 3.14)", result["message"])
        self.assertNotIn("pipeline/build_search_index.py", result["message"])
        self.assertNotIn("pipeline/query_search_index.py", result["message"])

    def test_google_is_shared_only_by_semantic_search_and_audio(self):
        with patch.dict(
            os.environ,
            empty_credentials(GOOGLE_API_KEY="google-env"),
            clear=False,
        ):
            review = setup.check_review({})
            semantic = setup.check_semantic_search({})
            audio = setup.check_audio({})
            email_result = setup.check_email({})

        self.assertFalse(review["ok"])
        self.assertTrue(semantic["ok"])
        self.assertTrue(audio["ok"])
        self.assertFalse(email_result["ok"])
        self.assertEqual(semantic["authorization"], "not_checked")
        self.assertEqual(audio["authorization"], "not_checked")

    def test_semantic_search_still_requests_google_when_selected(self):
        with patch.dict(os.environ, empty_credentials(), clear=False):
            result = setup.check_feature("semantic-search", {})

        self.assertFalse(result["ok"])
        self.assertEqual(result["status"], "missing_credential")
        self.assertEqual(result["credential"], "GOOGLE_API_KEY")
        self.assertIn("GOOGLE_API_KEY가 필요합니다", result["message"])

    def test_resend_is_isolated_to_email(self):
        with patch.dict(
            os.environ,
            empty_credentials(RESEND_API_KEY="resend-env"),
            clear=False,
        ):
            self.assertTrue(setup.check_email({})["ok"])
            self.assertFalse(setup.check_review({})["ok"])
            self.assertFalse(setup.check_semantic_search({})["ok"])
            self.assertFalse(setup.check_audio({})["ok"])

    def test_plaintext_config_keys_are_never_used_as_credentials(self):
        cfg = {
            "anthropic_api_key": "anthropic-config",
            "gemini_api_key": "google-config",
            "resend_api_key": "resend-config",
        }
        with patch.dict(os.environ, empty_credentials(), clear=False):
            review = setup.check_review(cfg)
            self.assertEqual(
                setup.check_semantic_search(cfg)["credential_source"],
                None,
            )
            self.assertEqual(
                setup.check_audio(cfg)["credential_source"],
                None,
            )
            self.assertEqual(
                setup.check_email(cfg)["credential_source"],
                None,
            )
        self.assertFalse(review["ok"])
        self.assertEqual(review["status"], "missing_credential")
        self.assertIsNone(review["credential_source"])

    def test_review_diagnostic_reuses_shared_os_credential_status(self):
        with patch.dict(os.environ, empty_credentials(), clear=False), patch("lib.credentials.credential_status", return_value={
            "reference": "credential:anthropic", "configured": True,
            "source": "keyring", "status": "configured",
        }) as status:
            result = setup.check_review({})
        self.assertTrue(result["ok"])
        self.assertEqual(result["credential_source"], "keyring")
        status.assert_called_once_with("anthropic")

    def test_zotero_requires_env_and_performs_remote_check(self):
        response = io.BytesIO(b'{"userID": 42}')
        with (
            patch.dict(
                os.environ,
                empty_credentials(ZOTERO_API_KEY="zotero-env"),
                clear=False,
            ),
            patch.object(setup.urllib.request, "urlopen", return_value=response) as urlopen,
        ):
            result = setup.check_zotero_sync({"zotero": {"api_key": "ignored"}})

        self.assertTrue(result["ok"])
        self.assertEqual(result["status"], "connected")
        self.assertEqual(result["authorization"], "verified")
        urlopen.assert_called_once()
        request = urlopen.call_args.args[0]
        self.assertEqual(request.full_url, "https://api.zotero.org/keys/current")
        self.assertEqual(request.get_header("Zotero-api-key"), "zotero-env")

    def test_zotero_connection_failure_is_non_ready(self):
        with (
            patch.dict(
                os.environ,
                empty_credentials(ZOTERO_API_KEY="zotero-env"),
                clear=False,
            ),
            patch.object(
                setup.urllib.request,
                "urlopen",
                side_effect=OSError("offline: zotero-env"),
            ),
        ):
            result = setup.check_zotero_sync({})

        self.assertFalse(result["ok"])
        self.assertEqual(result["status"], "connection_failed")
        self.assertEqual(result["authorization"], "failed")
        self.assertNotIn("zotero-env", result["message"])
        self.assertIn("OSError", result["message"])

    def test_legacy_zotero_config_key_is_not_a_credential(self):
        with (
            patch.dict(os.environ, empty_credentials(), clear=False),
            patch.object(setup.urllib.request, "urlopen") as urlopen,
        ):
            result = setup.check_zotero_sync(
                {"zotero": {"api_key": "legacy-config"}}
            )

        self.assertFalse(result["ok"])
        self.assertEqual(result["status"], "missing_credential")
        urlopen.assert_not_called()

    def test_unknown_feature_has_explicit_unsupported_result(self):
        result = setup.check_feature("diagram", {})
        self.assertFalse(result["ok"])
        self.assertEqual(result["status"], "unsupported")


class MainExitStatusTests(unittest.TestCase):
    def setUp(self):
        backend = Mock()
        backend.get_password.return_value = None
        self.keyring_patch = patch("lib.credentials._keyring", return_value=backend)
        self.keyring_patch.start()
        self.addCleanup(self.keyring_patch.stop)

    def _base_patches(self):
        return (
            patch.object(setup, "step_config", return_value={"zotero": {"collections": {}}}),
            patch.object(setup, "step_local_output", return_value=True),
            patch.object(setup, "step_skill_md", return_value=True),
            patch.object(setup, "step_install", return_value=True),
        )

    def test_no_selected_check_succeeds_without_credentials(self):
        config, local_output, skill, install = self._base_patches()
        with (
            patch.dict(os.environ, empty_credentials(), clear=False),
            config,
            local_output,
            skill,
            install,
            redirect_stdout(io.StringIO()),
        ):
            self.assertEqual(setup.main([]), 0)

    def test_selected_check_with_missing_key_returns_nonzero(self):
        config, local_output, skill, install = self._base_patches()
        with (
            patch.dict(os.environ, empty_credentials(), clear=False),
            config,
            local_output,
            skill,
            install,
            redirect_stdout(io.StringIO()),
        ):
            self.assertEqual(setup.main(["--check-feature", "review"]), 1)

    def test_selected_review_with_anthropic_key_succeeds_without_network(self):
        config, local_output, skill, install = self._base_patches()
        with (
            patch.dict(
                os.environ,
                empty_credentials(ANTHROPIC_API_KEY="anthropic-env"),
                clear=False,
            ),
            config,
            local_output,
            skill,
            install,
            patch.object(setup.urllib.request, "urlopen") as urlopen,
            redirect_stdout(io.StringIO()),
        ):
            self.assertEqual(setup.main(["--check-feature", "review"]), 0)
        urlopen.assert_not_called()

    def test_selected_keyword_search_succeeds_keyless_without_network(self):
        config, local_output, skill, install = self._base_patches()
        with tempfile.TemporaryDirectory() as tempdir:
            builder = Path(tempdir) / "build_search_index.py"
            query = Path(tempdir) / "query_search_index.py"
            builder.write_text("", encoding="utf-8")
            query.write_text("", encoding="utf-8")
            with (
                patch.dict(os.environ, empty_credentials(), clear=False),
                config,
                local_output,
                skill,
                install,
                patch.object(setup.sys, "version_info", (3, 12, 0)),
                patch.object(setup, "BUILD_SEARCH_INDEX_PATH", builder),
                patch.object(setup, "QUERY_SEARCH_INDEX_PATH", query),
                patch.object(
                    setup,
                    "_credential_source",
                    side_effect=AssertionError("keyword search must not inspect credentials"),
                ) as credential_source,
                patch.object(setup.urllib.request, "urlopen") as urlopen,
                redirect_stdout(io.StringIO()) as output,
            ):
                exit_code = setup.main(["--check-feature", "keyword-search"])

        self.assertEqual(exit_code, 0)
        credential_source.assert_not_called()
        urlopen.assert_not_called()
        self.assertIn("[기능 진단] keyword-search", output.getvalue())
        self.assertIn("✓ ready", output.getvalue())

    def test_combined_checks_fail_only_for_selected_unavailable_feature(self):
        def run_selected(credentials, selected):
            config, local_output, skill, install = self._base_patches()
            with tempfile.TemporaryDirectory() as tempdir:
                builder = Path(tempdir) / "build_search_index.py"
                query = Path(tempdir) / "query_search_index.py"
                builder.write_text("", encoding="utf-8")
                query.write_text("", encoding="utf-8")
                with (
                    patch.dict(os.environ, credentials, clear=False),
                    config,
                    local_output,
                    skill,
                    install,
                    patch.object(setup.sys, "version_info", (3, 12, 0)),
                    patch.object(setup, "BUILD_SEARCH_INDEX_PATH", builder),
                    patch.object(setup, "QUERY_SEARCH_INDEX_PATH", query),
                    redirect_stdout(io.StringIO()),
                ):
                    return setup.main(selected)

        self.assertEqual(
            run_selected(
                empty_credentials(),
                ["--check-feature", "keyword-search"],
            ),
            0,
        )
        self.assertEqual(
            run_selected(
                empty_credentials(),
                [
                    "--check-feature",
                    "keyword-search",
                    "--check-feature",
                    "semantic-search",
                ],
            ),
            1,
        )
        self.assertEqual(
            run_selected(
                empty_credentials(GOOGLE_API_KEY="google-env"),
                [
                    "--check-feature",
                    "keyword-search",
                    "--check-feature",
                    "semantic-search",
                ],
            ),
            0,
        )

    def test_repeated_feature_checks_run_in_argument_order(self):
        config, local_output, skill, install = self._base_patches()
        diagnostics = [
            {
                "feature": "email",
                "ok": True,
                "status": "configured_unverified",
                "credential": "RESEND_API_KEY",
                "credential_source": "env:RESEND_API_KEY",
                "authorization": "not_checked",
                "message": "configured",
            },
            {
                "feature": "review",
                "ok": True,
                "status": "configured_unverified",
                "credential": "ANTHROPIC_API_KEY",
                "credential_source": "env:ANTHROPIC_API_KEY",
                "authorization": "not_checked",
                "message": "configured",
            },
        ]
        with (
            config,
            local_output,
            skill,
            install,
            patch.object(setup, "check_feature", side_effect=diagnostics) as check,
            redirect_stdout(io.StringIO()),
        ):
            exit_code = setup.main(
                [
                    "--check-feature",
                    "email",
                    "--check-feature",
                    "review",
                ]
            )

        self.assertEqual(exit_code, 0)
        self.assertEqual(
            [call.args[0] for call in check.call_args_list],
            ["email", "review"],
        )

    def test_skill_generation_failure_returns_nonzero_and_does_not_install(self):
        with (
            patch.object(setup, "step_config", return_value={}),
            patch.object(setup, "step_local_output", return_value=True),
            patch.object(setup, "step_skill_md", return_value=False),
            patch.object(setup, "step_install") as install,
            redirect_stdout(io.StringIO()),
        ):
            self.assertEqual(setup.main([]), 1)
        install.assert_not_called()

    def test_skill_install_failure_returns_nonzero(self):
        with (
            patch.object(setup, "step_config", return_value={}),
            patch.object(setup, "step_local_output", return_value=True),
            patch.object(setup, "step_skill_md", return_value=True),
            patch.object(setup, "step_install", return_value=False),
            redirect_stdout(io.StringIO()),
        ):
            self.assertEqual(setup.main([]), 1)


if __name__ == "__main__":
    unittest.main()
