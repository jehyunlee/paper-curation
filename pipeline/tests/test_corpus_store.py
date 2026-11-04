import contextlib
import io
import json
import multiprocessing
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import patch

PIPELINE_DIR = Path(__file__).resolve().parents[1]
if str(PIPELINE_DIR) not in sys.path:
    sys.path.insert(0, str(PIPELINE_DIR))

from lib.corpus_store import (CorpusStoreBusyError, CorpusStoreError, cancel,
                              corpus_index_lock, corpus_operation_lock,
                              main, register, reserve)

MARKED_SLUGS = (
    "10067_Multi-marginal_temporal_Schrödinger_Bridge_Matching_from_unp",
    "10138_Optimal_Guarantees_for_Auditing_Rényi_Differentially_Private",
    "9520_Discovering_Scaling_Exponents_with_Physics-Informed_Müntz-Sz",
)


def _reserve_worker(papers, number, queue):
    result = reserve(papers, {"key": f"K{number}", "title": f"Concurrent paper {number}"})
    queue.put(result)


def _shared_operation_worker(papers, ready, release):
    with corpus_operation_lock(papers):
        ready.put("held")
        release.get(timeout=5)


class CorpusStoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.papers = Path(self.tmp.name) / "papers"
        self.papers.mkdir()

    def _bundle(self, slug, identity):
        directory = self.papers / slug
        for name in ("text.md", "review.md", "index.html"):
            (directory / name).write_text("content", encoding="utf-8")
        (directory / "bibliography.json").write_text(
            json.dumps({"zotero": identity}), encoding="utf-8")

    def _canonical_papers(self):
        self.papers = Path(self.tmp.name) / "docs" / "papers"
        self.papers.mkdir(parents=True)
        return self.papers

    def _view_report(self, status="completed"):
        return {"status": status, "topics": ["demo"],
                "steps": [{"topic": "demo", "builder": "search", "status": status}],
                "errors": ["demo/search: unavailable"] if status == "failed" else [],
                "retry_command": "python refresh_paper_views.py --slug 001_Registered"}

    def test_register_refreshes_committed_membership_after_index_lock_and_marker_release(self):
        import refresh_paper_views as views

        papers = self._canonical_papers()
        identity = {"key": "K", "title": "Registered paper"}
        slug = "001_Registered"
        (papers / slug).mkdir()
        (papers / "_papers_index.json").write_text(json.dumps([{
            "slug": slug, **identity, "topics": ["old"], "primary_topic": "old-primary",
            "classifications": {"stale": {"primary_category": "Retained metadata"}},
        }]), encoding="utf-8")
        reservation = reserve(papers, identity)
        self._bundle(slug, identity)

        def refresh(refreshed_slug, **kwargs):
            self.assertEqual(refreshed_slug, slug)
            self.assertEqual(kwargs, {"papers_dir": papers.resolve(),
                                      "previous_topics": ["old", "old-primary"], "allow_paid": True})
            self.assertFalse((papers / slug / ".corpus-reservation.json").exists())
            committed, = json.loads((papers / "_papers_index.json").read_text())
            self.assertEqual(committed["topics"], ["new"])
            self.assertEqual(committed["primary_topic"], "new-primary")
            with corpus_index_lock(papers, timeout=0):
                pass
            with corpus_operation_lock(papers, exclusive=True, timeout=0):
                pass
            return self._view_report()

        with patch.object(views, "PAPERS_DIR", papers), \
             patch.object(views, "refresh_paper_views", side_effect=refresh) as refreshed:
            result = register(papers, slug, reservation["token"], {
                **identity, "topics": ["new"], "primary_topic": "new-primary",
            })
        self.assertTrue(result["registered"])
        self.assertEqual(result["status"], "completed", result)
        refreshed.assert_called_once()

    def test_register_view_failure_is_nonzero_cli_but_registration_and_bundle_remain(self):
        import refresh_paper_views as views

        papers = self._canonical_papers()
        identity = {"key": "K", "title": "Registered paper"}
        reservation = reserve(papers, identity, requested_slug="001_Registered")
        self._bundle(reservation["slug"], identity)
        before = {path.name: path.read_bytes() for path in (papers / reservation["slug"]).iterdir()
                  if path.name != ".corpus-reservation.json"}
        request = Path(self.tmp.name) / "register.json"
        request.write_text(json.dumps({
            "schema_version": 1, "op": "register", "papers_dir": str(papers),
            "slug": reservation["slug"], "token": reservation["token"],
            "entry": {**identity, "topics": ["demo"]},
        }), encoding="utf-8")
        stdout = io.StringIO()
        with patch.object(views, "PAPERS_DIR", papers), \
             patch.object(views, "refresh_paper_views", return_value=self._view_report("failed")), \
             patch.object(sys, "argv", ["corpus_store.py", "--request", str(request)]), \
             contextlib.redirect_stdout(stdout):
            code = main()
        result = json.loads(stdout.getvalue())
        self.assertEqual(code, 1)
        self.assertEqual(result["status"], "failed")
        self.assertTrue(result["registered"])
        self.assertTrue(result["partial"]["registered"])
        self.assertTrue(result["partial"]["published"])
        self.assertTrue(result["partial"]["retry_safe"])
        self.assertEqual(result["partial"]["retry_command"], result["views"]["retry_command"])
        self.assertTrue(all(Path(path).is_file() for path in result["outputs"]))
        self.assertFalse((papers / reservation["slug"] / ".corpus-reservation.json").exists())
        committed, = json.loads((papers / "_papers_index.json").read_text())
        self.assertEqual(committed["slug"], reservation["slug"])
        self.assertEqual({path.name: path.read_bytes() for path in (papers / reservation["slug"]).iterdir()}, before)

    def test_register_unexpected_refresh_error_keeps_committed_registration(self):
        import refresh_paper_views as views

        papers = self._canonical_papers()
        identity = {"key": "K", "title": "Registered paper"}
        reservation = reserve(papers, identity)
        self._bundle(reservation["slug"], identity)
        with patch.object(views, "PAPERS_DIR", papers), \
             patch.object(views, "refresh_paper_views", side_effect=RuntimeError("builder crashed")):
            result = register(papers, reservation["slug"], reservation["token"], {**identity, "topics": ["demo"]})
        self.assertEqual(result["status"], "failed")
        self.assertTrue(result["registered"])
        self.assertTrue(result["views"]["errors"])
        self.assertIn(reservation["slug"], result["partial"]["retry_command"])
        self.assertFalse((papers / reservation["slug"] / ".corpus-reservation.json").exists())

    def test_standalone_register_does_not_refresh_canonical_topic_views(self):
        import refresh_paper_views as views

        identity = {"key": "K", "title": "Standalone paper"}
        reservation = reserve(self.papers, identity)
        self._bundle(reservation["slug"], identity)
        with patch.object(views, "PAPERS_DIR", Path(self.tmp.name) / "docs" / "papers"), \
             patch.object(views, "refresh_paper_views", side_effect=AssertionError("standalone")) as refresh:
            result = register(self.papers, reservation["slug"], reservation["token"], identity)
        self.assertTrue(result["registered"])
        refresh.assert_not_called()

    def test_reserved_review_budget_restriction_survives_until_registration(self):
        import refresh_paper_views as views
        from lib.corpus_store import restrict_view_refresh_to_budget

        papers = self._canonical_papers()
        identity = {"key": "K", "title": "Capped paper"}
        reservation = reserve(papers, identity)
        restrict_view_refresh_to_budget(papers, reservation["slug"], reservation["token"])
        self._bundle(reservation["slug"], identity)
        with patch.object(views, "PAPERS_DIR", papers), \
             patch.object(views, "refresh_paper_views", return_value=self._view_report("failed")) as refresh:
            result = register(papers, reservation["slug"], reservation["token"], {**identity, "topics": ["demo"]})
        self.assertFalse(refresh.call_args.kwargs["allow_paid"])
        self.assertTrue(result["registered"])
        self.assertEqual(result["status"], "failed")

    def test_concurrent_reservations_allocate_unique_numbers_and_register(self):
        queue = multiprocessing.Queue()
        workers = [multiprocessing.Process(target=_reserve_worker, args=(str(self.papers), n, queue)) for n in range(2)]
        for worker in workers:
            worker.start()
        results = [queue.get(timeout=5) for _ in workers]
        for worker in workers:
            worker.join(5)
            self.assertEqual(worker.exitcode, 0)
        self.assertEqual({r["slug"].split("_", 1)[0] for r in results}, {"001", "002"})
        for result in results:
            identity = {"key": f"K{result['slug'].split('_')[0][-1]}",
                        "title": result["slug"].replace("_", " ")}
            # Preserve exact reservation identity rather than guessing a title.
            identity = next({"key": f"K{n}", "title": f"Concurrent paper {n}"}
                            for n in range(2) if result["slug"].endswith(str(n)))
            self._bundle(result["slug"], identity)
            register(self.papers, result["slug"], result["token"], identity)
        index = json.loads((self.papers / "_papers_index.json").read_text())
        self.assertEqual({item["slug"] for item in index}, {r["slug"] for r in results})

    def test_busy_and_token_mismatch_fail_closed(self):
        first = reserve(self.papers, {"key": "A", "title": "Same paper"})
        with self.assertRaises(CorpusStoreBusyError):
            reserve(self.papers, {"key": "A", "title": "Same paper"})
        with self.assertRaises(CorpusStoreError):
            cancel(self.papers, first["slug"], "wrong")
        self._bundle(first["slug"], {"key": "A", "title": "Same paper"})
        with self.assertRaises(CorpusStoreError):
            register(self.papers, first["slug"], "wrong", {"title": "wrong"})

    def test_conflicting_identifier_does_not_reuse_existing_slug(self):
        slug = "001_existing"
        (self.papers / slug).mkdir()
        (self.papers / "_papers_index.json").write_text(json.dumps([{
            "slug": slug,
            "key": "K1",
            "doi": "10.1000/original",
            "title": "The original paper title",
        }]), encoding="utf-8")

        with self.assertRaisesRegex(
            CorpusStoreError, "existing index identity conflicts with reservation"
        ):
            reserve(self.papers, {
                "key": "K1",
                "doi": "10.1000/different",
                "title": "The original paper title",
            })

        self.assertFalse((self.papers / slug / ".corpus-reservation.json").exists())

    def test_existing_entry_without_key_or_doi_is_reused_not_a_conflict(self):
        # Observed: 10925 'AI in Science: Early Insights' had no key/doi in the
        # index (only in its sidecar), and a Curio re-review was refused.
        slug = "001_Early_Insights"
        (self.papers / slug).mkdir()
        (self.papers / slug / "bibliography.json").write_text(json.dumps({
            "schema": "bibliography-sidecar-1",
            "zotero": {"key": "K1", "title": "AI in Science: Early Insights"}}), encoding="utf-8")
        (self.papers / "_papers_index.json").write_text(json.dumps([{
            "slug": slug, "key": None, "doi": "", "title": "AI in Science: Early Insights"}]),
            encoding="utf-8")
        got = reserve(self.papers, {"key": "K1", "doi": "10.48550/arXiv.2609.28504",
                                    "title": "AI in Science: Early Insights"})
        self.assertEqual(got["slug"], slug)

    def test_existing_entry_with_a_different_sidecar_key_still_conflicts(self):
        slug = "001_Early_Insights"
        (self.papers / slug).mkdir()
        (self.papers / slug / "bibliography.json").write_text(json.dumps({
            "schema": "bibliography-sidecar-1",
            "zotero": {"key": "K1", "title": "AI in Science: Early Insights"}}), encoding="utf-8")
        (self.papers / "_papers_index.json").write_text(json.dumps([{
            "slug": slug, "doi": "", "title": "AI in Science: Early Insights"}]), encoding="utf-8")
        with self.assertRaisesRegex(CorpusStoreError, "conflicts with reservation"):
            reserve(self.papers, {"key": "K2", "title": "AI in Science: Early Insights"})

    def test_corruption_does_not_become_empty_index(self):
        (self.papers / "_papers_index.json").write_text("not json", encoding="utf-8")
        with self.assertRaises(CorpusStoreError):
            reserve(self.papers, {"title": "New paper"})
        self.assertEqual((self.papers / "_papers_index.json").read_text(encoding="utf-8"), "not json")

    def test_register_preserves_existing_corpus_metadata_and_lock_releases(self):
        slug = "001_existing"
        directory = self.papers / slug
        directory.mkdir()
        (self.papers / "_papers_index.json").write_text(json.dumps([{
            "slug": slug, "title": "Existing paper", "key": "K", "tags": ["keep"],
            "connections": [{"slug": "002"}], "bibliography_status": "sidecar-only",
            "classifications": {"ai4s": {"primary_category": "x"}},
        }]), encoding="utf-8")
        owned = reserve(self.papers, {"key": "K", "title": "Existing paper"})
        self._bundle(slug, {"key": "K", "title": "Existing paper"})
        register(self.papers, slug, owned["token"],
                 {"key": "K", "title": "Existing paper", "connections": [],
                  "classifications": {}, "tags": ["fresh"]})
        item = json.loads((self.papers / "_papers_index.json").read_text())[0]
        self.assertEqual(item["tags"], ["keep", "fresh"])
        self.assertEqual(item["connections"], [{"slug": "002"}])
        self.assertEqual(item["bibliography_status"], "sidecar-only")
        self.assertEqual(item["classifications"], {"ai4s": {"primary_category": "x"}})
        try:
            with corpus_index_lock(self.papers):
                raise RuntimeError("simulated failure")
        except RuntimeError:
            pass
        with corpus_index_lock(self.papers):
            pass

    def test_rejects_path_traversal_and_symlink_slug(self):
        reservation = reserve(self.papers, {"key": "safe", "title": "Safe paper"})
        with self.assertRaises(CorpusStoreError):
            cancel(self.papers, "../outside", reservation["token"])
        for invalid_slug in ("003_bad\x00slug", "003_bad\nslug", "003_bad\u200dslug"):
            with self.assertRaises(CorpusStoreError):
                reserve(self.papers, {"key": invalid_slug, "title": "Invalid paper"},
                        requested_slug=invalid_slug)
        outside = Path(self.tmp.name) / "outside"
        outside.mkdir()
        link = self.papers / "002_link"
        link.symlink_to(outside, target_is_directory=True)
        with self.assertRaises(CorpusStoreError):
            reserve(self.papers, {"key": "link", "title": "Link paper"},
                    requested_slug="002_link")

    def test_batch_process_refuses_live_reservation(self):
        import run_update_force

        reservation = reserve(
            self.papers, {"key": "batch", "title": "Batch must not overwrite"})
        with patch.object(run_update_force, "PAPERS_DIR", str(self.papers)), \
             patch.object(run_update_force, "_process_paper_locked") as process:
            self.assertEqual(
                run_update_force.process_paper({}, reservation["slug"],
                                               {"completed": []}),
                "busy")
        process.assert_not_called()

    def test_index_rebuild_skips_reserved_new_and_keeps_reserved_existing(self):
        import build_papers_index

        existing_slug = "001_existing"
        new_slug = "002_pending"
        (self.papers / existing_slug).mkdir()
        (self.papers / "_papers_index.json").write_text(json.dumps([{
            "slug": existing_slug, "key": "existing", "title": "Existing paper",
            "tags": ["retained"],
        }]), encoding="utf-8")
        reserve(self.papers, {"key": "existing", "title": "Existing paper"})
        reserve(self.papers, {"key": "new", "title": "Pending"}, requested_slug=new_slug)
        with patch.object(build_papers_index, "PAPERS_DIR", str(self.papers)):
            build_papers_index._run_build_index()
        index = json.loads((self.papers / "_papers_index.json").read_text())
        self.assertEqual(index, [{
            "slug": existing_slug, "key": "existing", "title": "Existing paper",
            "tags": ["retained"],
        }])

    def test_operation_lease_excludes_full_mutation_and_reservations(self):
        ready = multiprocessing.Queue()
        release = multiprocessing.Queue()
        worker = multiprocessing.Process(
            target=_shared_operation_worker, args=(str(self.papers), ready, release))
        worker.start()
        self.assertEqual(ready.get(timeout=5), "held")
        with self.assertRaises(CorpusStoreBusyError):
            with corpus_operation_lock(self.papers, exclusive=True):
                pass
        release.put("release")
        worker.join(5)
        self.assertEqual(worker.exitcode, 0)

        reserve(self.papers, {"key": "held", "title": "Reserved blocks full mutation"})
        with self.assertRaises(CorpusStoreBusyError):
            with corpus_operation_lock(self.papers, exclusive=True):
                pass

    def test_unicode_combining_mark_slugs_are_scanned_and_reused(self):
        entries = []
        for number, slug in enumerate(MARKED_SLUGS):
            (self.papers / slug).mkdir()
            entries.append({
                "slug": slug,
                "key": f"marked-{number}",
                "title": f"Marked paper {number}",
            })
        (self.papers / "_papers_index.json").write_text(
            json.dumps(entries, ensure_ascii=False), encoding="utf-8")

        unrelated = reserve(
            self.papers, {"key": "unrelated", "title": "New unrelated paper"})
        self.assertEqual(unrelated["slug"], "10139_New_unrelated_paper")
        cancel(self.papers, unrelated["slug"], unrelated["token"])

        reused = reserve(self.papers, {"key": "marked-0", "title": "Marked paper 0"})
        self.assertEqual(reused["slug"], MARKED_SLUGS[0])
        self.assertTrue(reused["existing"])
        self._bundle(MARKED_SLUGS[0], {"key": "marked-0", "title": "Marked paper 0"})
        register(self.papers, MARKED_SLUGS[0], reused["token"],
                 {"key": "marked-0", "title": "Marked paper 0"})

        cancelled = reserve(self.papers, {"key": "marked-1", "title": "Marked paper 1"})
        self.assertEqual(cancelled["slug"], MARKED_SLUGS[1])
        cancel(self.papers, MARKED_SLUGS[1], cancelled["token"])

    def test_noncomposable_combining_mark_slug_is_safe(self):
        slug = "10139_A⃝"
        reservation = reserve(
            self.papers, {"key": "noncomposable", "title": "Noncomposable mark"},
            requested_slug=slug)
        self.assertEqual(reservation["slug"], slug)
        cancel(self.papers, slug, reservation["token"])

    def test_cli_reports_invalid_slug_error_code_without_request_details(self):
        request = self.papers / "request.json"
        request.write_text(json.dumps({
            "schema_version": 1,
            "op": "reserve",
            "papers_dir": str(self.papers),
            "identity": {"key": "invalid"},
            "requested_slug": "001_bad/slash",
        }), encoding="utf-8")
        output = io.StringIO()
        with patch.object(sys, "argv", ["corpus_store.py", "--request", str(request)]), \
             contextlib.redirect_stdout(output):
            self.assertEqual(main(), 1)
        response = json.loads(output.getvalue())
        self.assertEqual(response["status"], "failed")
        self.assertEqual(response["error"], "invalid corpus request")
        self.assertEqual(response["error_code"], "invalid-slug")
        self.assertNotIn("001_bad/slash", output.getvalue())


if __name__ == "__main__":
    unittest.main()
