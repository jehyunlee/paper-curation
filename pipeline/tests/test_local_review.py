"""Provider-isolated contract tests for the shared local review endpoint.

No paid/provider calls are made and no corpus paths are used.
Run only this file under the repository py312 environment.
"""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


PIPELINE_DIR = Path(__file__).resolve().parents[1]
if str(PIPELINE_DIR) not in sys.path:
    sys.path.insert(0, str(PIPELINE_DIR))

import local_review as local  # noqa: E402


REVIEW = """# Contract Paper

> **저자**: Ada Lovelace | **날짜**: 2026 | **DOI**: [10.1000/test](https://doi.org/10.1000/test)

---

## Essence

충분히 긴 핵심 설명입니다. Canonical review validation을 통과하기 위한 근거 문장입니다.

## Motivation

- **Known**: 알려진 사실
- **Gap**: 남은 문제
- **Why**: 중요한 이유
- **Approach**: 사용한 접근

## Achievement

주요 성과를 설명합니다.

## How

구체적인 방법을 설명합니다.

## Originality

독창성을 설명합니다.

## Limitation & Further Study

근거와 일반화 범위의 한계를 설명합니다.

## Evaluation

- **Novelty**: 4/5
- **Technical Soundness**: 4/5
- **Significance**: 4/5
- **Clarity**: 4/5
- **Overall**: 4/5

**총평**: 검증 가능한 결론입니다.
"""
HTML = (
    "<!DOCTYPE html><html lang=\"ko\"><head><title>Contract Paper</title></head>"
    "<body><main>" + ("canonical " * 30) + "</main></body></html>"
)


class FakeEngine:
    def __init__(self, *, sanity=True, review_result=True, sidecar_result=True):
        self.calls = []
        self.sanity = sanity
        self.review_result = review_result
        self.sidecar_result = sidecar_result

    def extract_text(self, pdf_path, slug_dir):
        self.calls.append(("extract_text", pdf_path, Path(slug_dir).name))
        text = (
            "Contract Paper Ada Lovelace DOI 10.1000/test. "
            + "source evidence " * 30
        )
        Path(slug_dir, "text.md").write_text(text, encoding="utf-8")
        return True

    def _zotero_text_sanity(self, item, text_path):
        self.calls.append(("sanity", item["key"], Path(text_path).name))
        return (True, "ok") if self.sanity else (False, "title_hits=0/2")

    def extract_figures(self, pdf_path, slug_dir, *, validate_with_gemini):
        self.calls.append(("figures", validate_with_gemini))
        figure_dir = Path(slug_dir, "figures")
        figure_dir.mkdir()
        (figure_dir / "fig1.png").write_bytes(b"mock-png")
        return [{"name": "1", "page": 0, "caption": "Figure 1. Contract"}]

    def write_bibliography_sidecar(
        self,
        item,
        slug_dir,
        pdf_path,
        *,
        include_affiliations,
        review_provider,
        review_model,
    ):
        self.calls.append(
            (
                "sidecar",
                include_affiliations,
                review_provider,
                review_model,
            )
        )
        if not self.sidecar_result:
            return False
        text_path = Path(slug_dir, "text.md")
        payload = {
            "schema": local.SIDECAR_SCHEMA,
            "zotero": {
                "key": item["key"],
                "title": item["title"],
                "publicationTitle": item["publicationTitle"],
                "creators": item["creators"],
            },
            "creators": item["creators"],
            "authors": ["Ada Lovelace", "Contract Research Organization"],
            "affiliations": [],
            "review": {
                "provider": review_provider,
                "model": review_model,
                "schema_version": "v1",
            },
            "text_md_sha256": hashlib.sha256(text_path.read_bytes()).hexdigest(),
        }
        Path(slug_dir, "bibliography.json").write_text(
            json.dumps(payload), encoding="utf-8"
        )
        return payload

    def write_review(
        self, item, slug_dir, figures, *, provider, model, credential_ref,
        max_output_tokens, cache_dir, cache_evidence
    ):
        self.calls.append(
            ("review", provider, model, credential_ref, max_output_tokens, Path(cache_dir))
        )
        Path(cache_dir).mkdir(parents=True, exist_ok=True)
        cache_path = Path(cache_dir, "mock.json")
        cache_path.write_text(
            json.dumps({"model": model, "result": {"essence": "cached"}}),
            encoding="utf-8",
        )
        cache_evidence.update(
            {"path": str(cache_path), "provider": provider, "model": model, "verified": True}
        )
        Path(slug_dir, "review.md").write_text(REVIEW, encoding="utf-8")
        return self.review_result


class FakeRenderer:
    def __init__(self, *, fail=False):
        self.calls = []
        self.fail = fail

    def convert_review(self, md_path, topic, slug_dir, *, keyless):
        self.calls.append(
            (Path(md_path).name, topic, Path(slug_dir).name, keyless)
        )
        if self.fail:
            raise RuntimeError("renderer failed")
        return HTML


class LocalReviewContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.pdf = self.root / "paper.pdf"
        self.pdf.write_bytes(b"%PDF-1.7\nmock local-review fixture")
        self.output = self.root / "042_Contract_Paper"
        self.item = {
            "key": "ZOTERO42",
            "title": "Contract Paper",
            "creators": [
                {
                    "firstName": "Ada",
                    "lastName": "Lovelace",
                    "creatorType": "author",
                },
                {
                    "firstName": "Eve",
                    "lastName": "Editor",
                    "creatorType": "editor",
                },
                {
                    "name": "Contract Research Organization",
                    "creatorType": "author",
                },
            ],
            "date": "2026",
            "DOI": "10.1000/test",
            "abstractNote": "A local contract abstract.",
            "url": "https://example.test/paper",
            "publicationTitle": "Journal of Contracts",
        }

    def tearDown(self):
        self.temp.cleanup()

    def request(self, **changes):
        payload = {
            "schema_version": 1,
            "feature": "review",
            "pdf_path": str(self.pdf),
            "output_dir": str(self.output),
            "item": json.loads(json.dumps(self.item)),
            "overwrite": False,
        }
        payload.update(changes)
        return payload

    def run_execute(self, engine=None, renderer=None, payload=None):
        engine = engine or FakeEngine()
        renderer = renderer or FakeRenderer()
        with (
            patch.dict(
                os.environ,
                {
                    "ANTHROPIC_API_KEY": "sk-ant-contract-secret",
                    "GOOGLE_API_KEY": "GOOGLE-MUST-NOT-BE-USED",
                    "RESEND_API_KEY": "RESEND-MUST-NOT-BE-USED",
                    "ZOTERO_API_KEY": "ZOTERO-MUST-NOT-BE-USED",
                },
                clear=False,
            ),
            patch.object(local, "_missing_runtimes", return_value=[]),
            patch.object(local, "_load_engine", return_value=(engine, renderer)),
        ):
            result = local.run_request(payload or self.request(), execute=True)
        return result, engine, renderer

    def write_existing_bundle(self):
        self.output.mkdir(parents=True)
        text = "existing source " * 30
        (self.output / "text.md").write_text(text, encoding="utf-8")
        (self.output / "review.md").write_text(REVIEW, encoding="utf-8")
        (self.output / "index.html").write_text(HTML, encoding="utf-8")
        sidecar = {
            "schema": local.SIDECAR_SCHEMA,
            "zotero": {
                "key": self.item["key"],
                "title": self.item["title"],
                "publicationTitle": self.item["publicationTitle"],
                "creators": self.item["creators"],
            },
            "creators": self.item["creators"],
            "authors": ["Ada Lovelace", "Contract Research Organization"],
            "review": {"provider": local.PROVIDER, "model": local.MODEL},
            "text_md_sha256": hashlib.sha256(text.encode()).hexdigest(),
        }
        (self.output / "bibliography.json").write_text(
            json.dumps(sidecar), encoding="utf-8"
        )
        figure_dir = self.output / "figures"
        figure_dir.mkdir()
        (figure_dir / "fig1.png").write_bytes(b"old-figure")

    def test_keyless_plan_needs_only_anthropic_without_import_or_write(self):
        from lib.credentials import CredentialNotConfigured
        with (
            patch.dict(os.environ, {}, clear=True),
            patch("lib.credentials.resolve_credential",
                  side_effect=CredentialNotConfigured("not configured in test")),
            patch.object(
                local, "_load_engine", side_effect=AssertionError("heavy import")
            ) as loader,
        ):
            result = local.run_request(self.request())
        self.assertEqual(result["status"], "needs-key")
        self.assertEqual(result["required_keys"], ["ANTHROPIC_API_KEY"])
        self.assertEqual(result["provider"], "anthropic")
        self.assertEqual(result["model"], "claude-sonnet-5")
        self.assertEqual(result["transmission"], ["anthropic"])
        self.assertEqual(result["estimate"]["cost"], "unknown")
        self.assertIsNone(result["estimate"]["source_chars"])
        self.assertFalse(self.output.exists())
        self.assertFalse(local._lock_path(self.output).exists())
        loader.assert_not_called()

    def test_plan_with_key_is_ready_and_read_only(self):
        with (
            patch.dict(
                os.environ, {"ANTHROPIC_API_KEY": "sk-ant-ready-secret"}, clear=False
            ),
            patch.object(local, "_missing_runtimes", return_value=[]),
            patch.object(
                local, "_load_engine", side_effect=AssertionError("execute only")
            ) as loader,
        ):
            result = local.run_request(self.request())
        self.assertEqual(result["status"], "ready")
        self.assertFalse(self.output.exists())
        self.assertFalse(local._lock_path(self.output).exists())
        loader.assert_not_called()

    def test_runtime_preflight_requires_python312_and_posix_locking(self):
        with patch.object(local.sys, "version_info", (3, 14, 0)):
            missing = local._missing_runtimes("anthropic")
        self.assertIn("Python 3.12", missing)

        real_find_spec = local.importlib.util.find_spec

        def without_fcntl(name):
            return None if name == "fcntl" else real_find_spec(name)

        with patch.object(
            local.importlib.util, "find_spec", side_effect=without_fcntl
        ):
            missing = local._missing_runtimes("anthropic")
        self.assertIn("POSIX file locking", missing)

    def test_invalid_schema_feature_provider_model_and_paths_fail_closed(self):
        invalid = [
            {"schema_version": 2},
            {"feature": "compare"},
            {"provider": "ollama"},
            {"model": "claude-haiku-4-5"},
            {"pdf_path": "relative.pdf"},
            {"output_dir": "relative-output"},
            {"unexpected": True},
        ]
        for change in invalid:
            with self.subTest(change=change):
                result = local.run_request(self.request(**change))
                self.assertEqual(result["status"], "failed")

    def test_missing_empty_and_invalid_pdf_fail_before_key_or_engine(self):
        cases = [
            self.root / "missing.pdf",
            self.root / "empty.pdf",
            self.root / "not-a-pdf.pdf",
        ]
        cases[1].write_bytes(b"")
        cases[2].write_bytes(b"plain text")
        with patch.dict(os.environ, {}, clear=True), patch.object(
            local, "_load_engine", side_effect=AssertionError("must not import")
        ) as loader:
            for path in cases:
                with self.subTest(path=path.name):
                    result = local.run_request(self.request(pdf_path=str(path)))
                    self.assertEqual(result["status"], "insufficient-data")
        loader.assert_not_called()

    def test_execute_uses_only_canonical_anthropic_keyless_path(self):
        self.output.mkdir()
        (self.output / "curio-note.txt").write_text("preserve me", encoding="utf-8")
        result, engine, renderer = self.run_execute()
        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["bibliography"], "sidecar-only")
        self.assertEqual(result["figures"], 1)
        self.assertEqual(set(result["outputs"]), {"review", "html", "text", "sidecar"})
        self.assertTrue(all(Path(path).is_file() for path in result["outputs"].values()))
        self.assertEqual(
            (self.output / "curio-note.txt").read_text(encoding="utf-8"),
            "preserve me",
        )
        self.assertIn(("figures", False), engine.calls)
        self.assertIn(
            ("sidecar", False, local.PROVIDER, local.MODEL), engine.calls
        )
        review_call = next(call for call in engine.calls if call[0] == "review")
        self.assertEqual(review_call[1:5], ("anthropic", local.MODEL, None, 4000))
        self.assertEqual(
            renderer.calls,
            [("review.md", "ai4s", self.output.name, True)],
        )
        sidecar = json.loads(
            (self.output / "bibliography.json").read_text(encoding="utf-8")
        )
        self.assertEqual(sidecar["zotero"]["key"], self.item["key"])
        self.assertEqual(
            sidecar["zotero"]["publicationTitle"],
            self.item["publicationTitle"],
        )
        self.assertEqual(sidecar["creators"], self.item["creators"])
        self.assertEqual(sidecar["review"]["model"], local.MODEL)
        self.assertFalse((self.root / "_papers_index.json").exists())
        self.assertFalse((self.root / "bibliography.sqlite3").exists())

    def test_selected_provider_is_forwarded_to_writer_and_sidecar(self):
        payload = self.request(provider="openai", model="gpt-5")
        with patch.dict(os.environ, {"OPENAI_API_KEY": "openai-test-key"}, clear=True):
            result, engine, _renderer = self.run_execute(payload=payload)
        self.assertEqual(result["status"], "completed")
        self.assertEqual((result["provider"], result["model"]), ("openai", "gpt-5"))
        self.assertIn(("sidecar", False, "openai", "gpt-5"), engine.calls)
        self.assertEqual(next(c for c in engine.calls if c[0] == "review")[1:3], ("openai", "gpt-5"))

    def test_budget_exceeded_plan_blocks_before_key_or_writer(self):
        payload = self.request(budget={
            "max_cost_usd": 0, "input_per_million_usd": 1,
            "output_per_million_usd": 1, "max_output_tokens": 4000,
        })
        with patch.dict(os.environ, {}, clear=True):
            result = local.run_request(payload)
        self.assertEqual(result["status"], "budget-exceeded")
        self.assertIn("budget-exceeded", result["error"])
        self.assertEqual(result["estimate"]["attempts"], 1)

    def test_budget_bound_covers_large_item_fields_without_extracting_pdf(self):
        item = json.loads(json.dumps(self.item))
        item["title"] = "한" * 20_000
        payload = self.request(item=item, budget={
            "max_cost_usd": 0, "input_per_million_usd": 1,
            "output_per_million_usd": 1,
        })
        result = local.run_request(payload)
        self.assertEqual(result["status"], "budget-exceeded")
        self.assertGreater(result["estimate"]["estimated_input_tokens"], 48_000)

    def test_reserved_output_rejects_missing_or_mismatched_token_before_engine(self):
        from lib.corpus_store import reserve

        reservation = reserve(
            self.root, {"key": self.item["key"], "title": self.item["title"]},
            requested_slug=self.output.name,
        )
        for token in (None, "wrong-token"):
            with self.subTest(token=bool(token)):
                engine = FakeEngine()
                result, engine, _renderer = self.run_execute(
                    engine=engine,
                    payload=self.request(overwrite=True, reservation_token=token)
                )
                self.assertEqual(result["status"], "failed")
                self.assertIn("reservation ownership mismatch", result["error"])
                self.assertEqual(engine.calls, [])

        result, engine, _renderer = self.run_execute(
            payload=self.request(overwrite=True, reservation_token=reservation["token"])
        )
        self.assertEqual(result["status"], "completed")
        self.assertNotIn(reservation["token"], json.dumps(result))

    def test_unreserved_output_rejects_supplied_token_before_engine(self):
        engine = FakeEngine()
        result, engine, _renderer = self.run_execute(
            engine=engine,
            payload=self.request(overwrite=True, reservation_token="unexpected-token"),
        )
        self.assertEqual(result["status"], "failed")
        self.assertIn("reservation ownership mismatch", result["error"])
        self.assertEqual(engine.calls, [])

    def test_sanity_mismatch_stops_before_figures_sidecar_and_llm(self):
        result, engine, _renderer = self.run_execute(engine=FakeEngine(sanity=False))
        self.assertEqual(result["status"], "insufficient-data")
        self.assertEqual([call[0] for call in engine.calls], ["extract_text", "sanity"])
        self.assertFalse(self.output.exists())

    def test_sidecar_is_mandatory_and_paid_review_is_preserved_on_failure(self):
        result, engine, _renderer = self.run_execute(
            engine=FakeEngine(sidecar_result=False)
        )
        self.assertEqual(result["status"], "failed")
        self.assertIn("review", [call[0] for call in engine.calls])
        self.assertTrue(result["partial"]["review_ready"])
        self.assertTrue(result["partial"]["retry_safe"])
        self.assertFalse(self.output.exists())

    def test_failed_review_cannot_succeed_from_old_artifacts(self):
        self.write_existing_bundle()
        before = {
            name: (self.output / name).read_bytes()
            for name in local._REQUIRED_OUTPUT_NAMES
        }
        payload = self.request(overwrite=True)
        result, _engine, _renderer = self.run_execute(
            engine=FakeEngine(review_result=False), payload=payload
        )
        self.assertEqual(result["status"], "failed")
        self.assertIn("partial", result)
        self.assertTrue(result["partial"]["cache_preserved"])
        for name, content in before.items():
            self.assertEqual((self.output / name).read_bytes(), content)

    def test_stale_cache_does_not_claim_retry_safe_for_a_new_failure(self):
        cache_dir = local._cache_dir(self.output)
        cache_dir.mkdir()
        (cache_dir / "unrelated-old.json").write_text(
            '{\"model\":\"old\"}', encoding="utf-8"
        )

        class NoResultEngine(FakeEngine):
            def write_review(
                self,
                item,
                slug_dir,
                figures,
                *,
                provider,
                model,
                credential_ref,
                max_output_tokens,
                cache_dir,
                cache_evidence,
            ):
                self.calls.append(
                    ("review", provider, model, credential_ref, max_output_tokens, Path(cache_dir))
                )
                return False

        result, _engine, _renderer = self.run_execute(engine=NoResultEngine())
        self.assertEqual(result["status"], "failed")
        self.assertNotIn("partial", result)

    def test_renderer_failure_preserves_review_and_cache_as_partial(self):
        result, _engine, _renderer = self.run_execute(
            renderer=FakeRenderer(fail=True)
        )
        self.assertEqual(result["status"], "failed")
        self.assertTrue(result["partial"]["review_ready"])
        self.assertTrue(result["partial"]["retry_safe"])
        self.assertTrue(Path(result["partial"]["review"]).is_file())
        self.assertTrue(Path(result["partial"]["cache"]).is_file())
        self.assertFalse(self.output.exists())

    def test_overwrite_false_returns_only_a_complete_matching_bundle(self):
        self.write_existing_bundle()
        with (
            patch.dict(os.environ, {}, clear=True),
            patch.object(
                local, "_load_engine", side_effect=AssertionError("must not execute")
            ) as loader,
        ):
            result = local.run_request(self.request(), execute=True)
        self.assertEqual(result["status"], "exists")
        self.assertEqual(result["bibliography"], "sidecar-only")
        self.assertEqual(result["figures"], 1)
        loader.assert_not_called()

    def test_incomplete_existing_bundle_is_not_reported_as_exists(self):
        self.output.mkdir()
        (self.output / "review.md").write_text(REVIEW, encoding="utf-8")
        with patch.dict(os.environ, {}, clear=True):
            result = local.run_request(self.request(), execute=True)
        self.assertEqual(result["status"], "failed")
        self.assertNotIn("outputs", result)

    @unittest.skipUnless(
        hasattr(os, "symlink"), "symbolic links are unavailable"
    )
    def test_symlinked_figures_directory_is_refused_without_touching_target(self):
        external = self.root / "external-figures"
        external.mkdir()
        external_figure = external / "fig1.png"
        external_figure.write_bytes(b"external-content")
        self.output.mkdir()
        os.symlink(external, self.output / "figures", target_is_directory=True)
        result, engine, _renderer = self.run_execute(
            payload=self.request(overwrite=True)
        )
        self.assertEqual(result["status"], "failed")
        self.assertIn("symbolic link", result["error"])
        self.assertEqual(external_figure.read_bytes(), b"external-content")
        self.assertEqual(engine.calls, [])

    @unittest.skipUnless(sys.platform != "win32", "fcntl contract is POSIX-only")
    def test_concurrent_output_lock_fails_without_starting_engine(self):
        import fcntl

        lock_path = local._lock_path(self.output)
        descriptor = os.open(lock_path, os.O_CREAT | os.O_RDWR, 0o600)
        fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
        try:
            with (
                patch.dict(
                    os.environ,
                    {"ANTHROPIC_API_KEY": "sk-ant-lock-secret"},
                    clear=False,
                ),
                patch.object(local, "_missing_runtimes", return_value=[]),
                patch.object(
                    local, "_load_engine", side_effect=AssertionError("locked")
                ) as loader,
            ):
                result = local.run_request(self.request(), execute=True)
        finally:
            fcntl.flock(descriptor, fcntl.LOCK_UN)
            os.close(descriptor)
        self.assertEqual(result["status"], "failed")
        self.assertIn("already writing", result["error"])
        loader.assert_not_called()

    def test_cli_stdout_is_one_json_object_and_logs_are_secret_scrubbed(self):
        request_file = self.root / "request.json"
        request_file.write_text(json.dumps(self.request()), encoding="utf-8")
        secret = "test-secret"
        other_secret = "RESEND_NONSTANDARD_SENTINEL"
        engine = FakeEngine()
        original_extract = engine.extract_text

        def noisy_extract(*args, **kwargs):
            print("engine log " + secret + " " + other_secret)
            return original_extract(*args, **kwargs)

        engine.extract_text = noisy_extract
        stdout = io.StringIO()
        stderr = io.StringIO()
        with (
            patch.dict(
                os.environ,
                {
                    "ANTHROPIC_API_KEY": secret,
                    "RESEND_API_KEY": other_secret,
                },
                clear=False,
            ),
            patch.object(local, "_missing_runtimes", return_value=[]),
            patch.object(
                local,
                "_load_engine",
                return_value=(engine, FakeRenderer()),
            ),
            contextlib.redirect_stdout(stdout),
            contextlib.redirect_stderr(stderr),
        ):
            code = local.main(["--request", str(request_file), "--execute"])
        self.assertEqual(code, 0)
        lines = stdout.getvalue().splitlines()
        self.assertEqual(len(lines), 1)
        self.assertEqual(json.loads(lines[0])["status"], "completed")
        self.assertNotIn(secret, stdout.getvalue())
        self.assertNotIn(secret, stderr.getvalue())
        self.assertNotIn(other_secret, stdout.getvalue())
        self.assertNotIn(other_secret, stderr.getvalue())
        self.assertEqual(stderr.getvalue().strip(), "review engine diagnostics suppressed")

    def test_other_provider_secret_is_scrubbed_from_failure_json(self):
        other_secret = "GOOGLE_ODD_SENTINEL_VALUE"

        class ExplodingEngine(FakeEngine):
            def extract_text(self, pdf_path, slug_dir):
                raise RuntimeError(other_secret)

        engine = ExplodingEngine()
        with (
            patch.dict(
                os.environ,
                {
                    "ANTHROPIC_API_KEY": "sk-ant-contract-secret",
                    "GOOGLE_API_KEY": other_secret,
                },
                clear=False,
            ),
            patch.object(local, "_missing_runtimes", return_value=[]),
            patch.object(
                local,
                "_load_engine",
                return_value=(engine, FakeRenderer()),
            ),
        ):
            result = local.run_request(self.request(), execute=True)
        encoded = json.dumps(result)
        self.assertEqual(result["status"], "failed")
        self.assertNotIn(other_secret, encoded)
        self.assertEqual(result["error"], "local review failed: RuntimeError")

    def test_malformed_request_file_still_returns_final_json_only(self):
        request_file = self.root / "bad.json"
        request_file.write_text("{bad", encoding="utf-8")
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            code = local.main(["--request", str(request_file)])
        self.assertEqual(code, 2)
        lines = stdout.getvalue().splitlines()
        self.assertEqual(len(lines), 1)
        self.assertEqual(json.loads(lines[0])["status"], "failed")

    def test_help_uses_standard_cli_help(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout), self.assertRaises(SystemExit) as raised:
            local.main(["--help"])
        self.assertEqual(raised.exception.code, 0)
        self.assertIn("--request", stdout.getvalue())
        self.assertIn("--execute", stdout.getvalue())

    def test_batch_import_is_lazy_and_sidecar_can_skip_heavy_affiliations(self):
        import run_update_force as batch

        self.assertFalse(hasattr(batch, "TOPIC_MODELING_PYTHON"))
        self.assertIsNone(batch.ZOTERO_DIR)
        self.assertIsNone(batch.COLLECTIONS)
        stage = self.root / "sidecar-stage"
        stage.mkdir()
        (stage / "text.md").write_text("source " * 30, encoding="utf-8")
        with patch.object(
            batch,
            "_extract_affiliations_for_sidecar",
            side_effect=AssertionError("heavy post-processing"),
        ) as affiliations:
            payload = batch.write_bibliography_sidecar(
                self.item,
                str(stage),
                str(self.pdf),
                include_affiliations=False,
                review_provider=local.PROVIDER,
                review_model=local.MODEL,
            )
        affiliations.assert_not_called()
        self.assertEqual(payload["creators"], self.item["creators"])
        self.assertEqual(payload["zotero"]["creators"], self.item["creators"])
        self.assertEqual(
            payload["zotero"]["publicationTitle"], self.item["publicationTitle"]
        )
        self.assertEqual(
            payload["zotero"]["abstractNote"], self.item["abstractNote"]
        )
        self.assertEqual(payload["review"]["model"], local.MODEL)

    def test_real_review_writer_keeps_structured_organization_name(self):
        import run_update_force as batch

        stage = self.root / "writer-stage"
        stage.mkdir()
        (stage / "text.md").write_text("source text " * 100, encoding="utf-8")
        data = {
            "essence": "핵심",
            "known": "알려짐",
            "gap": "공백",
            "why": "이유",
            "approach": "접근",
            "achievement": "성과",
            "how": "방법",
            "originality": "독창성",
            "limitation": "한계",
            "verdict": "판정",
            "fig_essence": 0,
            "fig_achievement": 0,
            "fig_how": 0,
            "novelty": 4,
            "technical": 4,
            "significance": 4,
            "clarity": 4,
            "overall": 4,
        }
        fake_anthropic = SimpleNamespace(Anthropic=lambda **_kwargs: object())
        with (
            patch.dict(sys.modules, {"anthropic": fake_anthropic}),
            patch("api._llm.cached_call", return_value=data),
        ):
            wrote = batch.write_review(
                self.item,
                str(stage),
                [],
                model=local.MODEL,
                cache_dir=stage / ".cache",
            )
        self.assertTrue(wrote)
        review = (stage / "review.md").read_text(encoding="utf-8")
        self.assertIn(
            "Ada Lovelace, Eve Editor, Contract Research Organization", review
        )

    def test_canonical_renderer_keyless_mode_never_loads_optional_integrations(self):
        import review_to_html as renderer

        stage = self.root / self.output.name
        stage.mkdir()
        review_path = stage / "review.md"
        review_path.write_text(REVIEW, encoding="utf-8")
        with (
            patch.dict(
                os.environ,
                {
                    "GOOGLE_API_KEY": "GOOGLE-HTML-SENTINEL",
                    "PAPER_CURATION_LOCAL_EMAILS": "private@example.test",
                },
                clear=False,
            ),
            patch.object(
                renderer,
                "_load_connections",
                side_effect=AssertionError("corpus connections"),
            ) as connections,
            patch.object(
                renderer,
                "_zotero_keys",
                side_effect=AssertionError("Zotero corpus state"),
            ) as zotero_keys,
        ):
            html = renderer.convert_review(
                str(review_path), "ai4s", str(stage), keyless=True
            )
        connections.assert_not_called()
        zotero_keys.assert_not_called()
        self.assertNotIn("GOOGLE-HTML-SENTINEL", html)
        self.assertNotIn("private@example.test", html)
        self.assertNotIn("Audio Overview 생성", html)
        self.assertIn(self.output.name, html)


class RealPrimitiveIntegrationTests(unittest.TestCase):
    def test_real_pdf_review_renderer_and_sidecar_with_only_provider_mocked(self):
        import fitz
        import run_update_force as engine

        title = "Shared Local Review Contract Study"
        creators = [
            {"firstName": "Ada", "lastName": "Lovelace", "creatorType": "author"},
            {"name": "Research Consortium", "creatorType": "author"},
        ]
        properties = engine.REVIEW_TOOL_SCHEMA["input_schema"]["properties"]
        payload = {
            name: (0 if name.startswith("fig_") else 3)
            if spec["type"] == "integer"
            else "검증용 논문의 동작과 근거를 설명하는 테스트 리뷰 문장입니다."
            for name, spec in properties.items()
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pdf = root / "paper.pdf"
            output = root / "001_Contract_Study"
            document = fitz.open()
            page = document.new_page()
            page.insert_textbox(
                fitz.Rect(40, 40, 550, 780),
                f"{title}\nAda Lovelace, Research Consortium\n"
                "DOI: 10.1234/local-review-contract\nAbstract\n"
                + "This study verifies an isolated local review workflow with source evidence. " * 12,
                fontsize=11,
            )
            document.save(pdf)
            document.close()
            request = {
                "schema_version": 1,
                "feature": "review",
                "pdf_path": str(pdf),
                "output_dir": str(output),
                "overwrite": False,
                "item": {
                    "key": "ABC12345", "title": title, "creators": creators,
                    "date": "2026", "DOI": "10.1234/local-review-contract",
                    "abstractNote": "A local review workflow contract study.",
                    "url": "https://example.test/paper",
                    "publicationTitle": "Contract Journal",
                },
            }
            with (
                patch.dict(os.environ, {
                    "ANTHROPIC_API_KEY": "ANTHROPIC-INTEGRATION-SENTINEL",
                }, clear=True),
                patch.dict(sys.modules, {"opendataloader_pdf": None}),
                patch("socket.socket.connect", side_effect=AssertionError("network forbidden")) as network,
                patch.object(engine, "get_google_key", side_effect=AssertionError("Google forbidden")) as google,
                patch.object(engine, "WRITE_REVIEW_MODEL", "unapproved-model"),
                patch("anthropic.Anthropic") as client_factory,
            ):
                create = client_factory.return_value.messages.create
                create.return_value = SimpleNamespace(content=[SimpleNamespace(
                    type="tool_use", name="emit_review", input=payload,
                )])
                first = local.run_request(request, execute=True)
                self.assertEqual(first["status"], "completed", first)
                os.environ["GOOGLE_API_KEY"] = "GOOGLE-INTEGRATION-SENTINEL"
                request["overwrite"] = True
                second = local.run_request(request, execute=True)
                self.assertEqual(second["status"], "completed", second)
                self.assertEqual(create.call_count, 1, "identical retry must use the real cache")
                self.assertEqual(create.call_args.kwargs["model"], "claude-sonnet-5")
                network.assert_not_called()
                google.assert_not_called()
            html = (output / "index.html").read_text(encoding="utf-8")
            review = (output / "review.md").read_text(encoding="utf-8")
            sidecar = json.loads((output / "bibliography.json").read_text(encoding="utf-8"))
            self.assertIn(title, html)
            self.assertIn("Research Consortium", review)
            self.assertEqual(sidecar["creators"], creators)
            self.assertEqual(sidecar["review"]["model"], "claude-sonnet-5")
            self.assertNotIn("INTEGRATION-SENTINEL", html)
            self.assertFalse((root / "_papers_index.json").exists())
            # Recover a published-but-unindexed bundle with the real sidecar,
            # whose Zotero DOI key is uppercase (unlike index entries).
            from lib.corpus_store import reserve, register
            identity = {"key": request["item"]["key"], "doi": request["item"]["DOI"], "title": title}
            reservation = reserve(root, identity)
            self.assertEqual(reservation["slug"], output.name)
            registered = register(root, reservation["slug"], reservation["token"], {
                "title": title, "doi": identity["doi"],
                "zotero_item_key": identity["key"], "bibliography_status": "sidecar-only",
            })
            self.assertTrue(registered["registered"])
            index = json.loads((root / "_papers_index.json").read_text())
            self.assertEqual(len(index), 1)
            self.assertEqual(index[0]["doi"], request["item"]["DOI"])


if __name__ == "__main__":
    unittest.main()
