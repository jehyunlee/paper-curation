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
                              register, reserve)


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


if __name__ == "__main__":
    unittest.main()
