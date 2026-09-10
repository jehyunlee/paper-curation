import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE))
import run_full
import local_review
from lib.corpus_store import corpus_operation_lock, CorpusStoreBusyError


class OperationLeaseIntegrationTests(unittest.TestCase):
    def test_full_dry_run_does_not_create_operation_lock_or_execute(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            with patch.object(run_full, "PIPELINE", root / "pipeline"), patch.object(sys, "argv", ["run_full.py", "--topic", "demo", "--mode", "curate", "--source", "zotero", "--dry-run"]), patch.object(run_full, "run", side_effect=AssertionError("execution")):
                run_full.main()
            self.assertFalse((root / "docs/papers").exists())

    def test_full_plan_holds_exclusive_lease_across_child_steps(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            papers = root / "docs/papers"
            checked = []
            def step(command, timeout=None):
                with self.assertRaises(CorpusStoreBusyError):
                    with corpus_operation_lock(papers):
                        pass
                checked.append(command)
                return 0
            with patch.object(run_full, "PIPELINE", root / "pipeline"), patch.object(sys, "argv", ["run_full.py", "--topic", "demo", "--mode", "curate", "--source", "zotero", "--no-validate"]), patch.object(run_full, "run", side_effect=step), patch.object(run_full, "mark_running"), patch.object(run_full, "mark_finished"):
                run_full.main()
            self.assertGreater(len(checked), 0)
            with corpus_operation_lock(papers):
                pass

    def test_local_review_holds_shared_lease_through_execution(self):
        with tempfile.TemporaryDirectory() as temporary:
            papers = Path(temporary)
            pdf = papers / "source.pdf"
            pdf.write_bytes(b"%PDF-1.4\nfixture")
            request = {"provider": "anthropic", "model": "claude-sonnet-5", "output_dir": papers / "001_Review",
                       "pdf_path": pdf, "budget": None}
            def execute(_request, _pdf):
                with self.assertRaises(CorpusStoreBusyError):
                    with corpus_operation_lock(papers, exclusive=True):
                        pass
                return {"status": "completed"}
            with patch.object(local_review, "_validate_request", return_value=request), patch.object(local_review, "_preflight", return_value=({}, None)), patch.object(local_review, "_execute", side_effect=execute):
                self.assertEqual(local_review.run_request({}, execute=True)["status"], "completed")
            with corpus_operation_lock(papers, exclusive=True):
                pass


if __name__ == "__main__":
    unittest.main()
