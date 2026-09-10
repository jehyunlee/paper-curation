"""Focused checks for deferred local-review bibliography ingestion.

Local review publication keeps ``bibliography_status: sidecar-only`` in the
paper index. The marker identifies the ingestion path permanently; freshness
comes from the review/text hashes that the bibliography builder records.
"""
import io
import json
import sqlite3
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

PIPELINE_DIR = Path(__file__).resolve().parents[1]
if str(PIPELINE_DIR) not in sys.path:
    sys.path.insert(0, str(PIPELINE_DIR))

import build_bibliography_db as bib
import check_bibliography_db as checker


class LocalReviewStalenessTests(unittest.TestCase):
    slug = "001_local_review"

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.papers_dir = self.root / "docs" / "papers"
        self.paper_dir = self.papers_dir / self.slug
        self.paper_dir.mkdir(parents=True)
        self.index = self.papers_dir / "_papers_index.json"
        self.db = self.root / "bibliography.sqlite3"

        self._write_sources("initial local review")
        self._write_index(marked=True)
        conn = sqlite3.connect(self.db)
        conn.executescript(bib.SCHEMA)
        conn.execute(
            "INSERT INTO papers "
            "(paper_id,slug,title,doi,bibliography_source,review_dir,"
            "zotero_item_key) VALUES (1,?,?,?,?,?,?)",
            (
                self.slug,
                "Local review",
                "",
                "",
                f"docs/papers/{self.slug}",
                "",
            ),
        )
        conn.commit()
        conn.close()
        self._record_current_hashes()

    def _write_index(self, *, marked: bool) -> None:
        entry = {"slug": self.slug, "title": "Local review"}
        if marked:
            entry["bibliography_status"] = "sidecar-only"
        self.index.write_text(
            json.dumps([entry], ensure_ascii=False), encoding="utf-8")

    def _write_sources(self, version: str) -> None:
        review = self.paper_dir / "review.md"
        text = self.paper_dir / "text.md"
        review.write_text(
            "---\ntitle: Local review\n---\n\n# Local review\n\n"
            f"{version}\n",
            encoding="utf-8",
        )
        text.write_text(
            f"# Local review\n\n{version}\n",
            encoding="utf-8",
        )
        (self.paper_dir / "bibliography.json").write_text(
            json.dumps({
                "schema": bib.SIDECAR_SCHEMA,
                "zotero": {"key": "LOCAL1"},
                "text_md_sha256": bib.sha256(text),
            }),
            encoding="utf-8",
        )

    def _record_current_hashes(self) -> None:
        conn = sqlite3.connect(self.db)
        for kind in ("review", "text"):
            path = self.paper_dir / f"{kind}.md"
            conn.execute(
                "INSERT OR REPLACE INTO source_documents "
                "(paper_id,document_type,path,sha256,bytes) "
                "VALUES (1,?,?,?,?)",
                (
                    kind,
                    f"docs/papers/{self.slug}/{path.name}",
                    bib.sha256(path),
                    path.stat().st_size,
                ),
            )
        conn.commit()
        conn.close()

    def _run_checker(self) -> tuple[int, dict]:
        stdout = io.StringIO()
        argv = [
            "check_bibliography_db.py",
            "--db",
            str(self.db),
            "--strict",
        ]
        with (
            patch.object(checker, "ROOT", self.root),
            patch.object(checker, "INDEX", self.index),
            patch.object(sys, "argv", argv),
            redirect_stdout(stdout),
        ):
            code = checker.main()
        return code, json.loads(stdout.getvalue())

    def test_same_count_changed_review_and_text_fail_strict(self):
        self._write_sources("replacement local review")

        code, report = self._run_checker()

        self.assertEqual(report["db_papers"], 1)
        self.assertEqual(report["source_index_papers"], 1)
        self.assertEqual(code, 2)
        self.assertEqual(report["sidecar_only_sources_stale"], 1)
        issue = "\n".join(report["issues"])
        self.assertIn("sidecar-only bibliography DB stale", issue)
        self.assertIn("review.md, text.md", issue)

    def test_reingest_clears_staleness_without_removing_marker(self):
        self._write_sources("replacement local review")
        stale_code, _ = self._run_checker()
        self.assertEqual(stale_code, 2)

        self._record_current_hashes()
        code, report = self._run_checker()

        self.assertEqual(code, 0)
        self.assertEqual(report["sidecar_only_sources_fresh"], 1)
        self.assertEqual(report["sidecar_only_sources_stale"], 0)
        self.assertEqual(report["issues"], [])
        entry = json.loads(self.index.read_text(encoding="utf-8"))[0]
        self.assertEqual(entry["bibliography_status"], "sidecar-only")

    def test_unmarked_entry_is_not_scanned_for_staleness(self):
        self._write_index(marked=False)
        self._write_sources("replacement local review")

        code, report = self._run_checker()

        self.assertEqual(code, 0)
        self.assertEqual(report["sidecar_only_papers"], 0)
        self.assertEqual(report["sidecar_only_sources_stale"], 0)

    def test_missing_source_records_are_reported_as_not_ingested(self):
        conn = sqlite3.connect(self.db)
        conn.execute("DELETE FROM source_documents")
        conn.commit()
        conn.close()

        code, report = self._run_checker()

        self.assertEqual(code, 2)
        self.assertEqual(report["sidecar_only_sources_not_ingested"], 1)
        self.assertTrue(any(
            "missing DB source hashes" in issue
            for issue in report["issues"]
        ))

    def test_missing_source_schema_is_explicit(self):
        conn = sqlite3.connect(self.db)
        conn.execute("DROP TABLE source_documents")
        conn.commit()
        conn.close()

        code, report = self._run_checker()

        self.assertEqual(code, 2)
        self.assertEqual(report["sidecar_only_sources_unverifiable"], 1)
        self.assertTrue(any(
            "missing DB schema: source_documents table" in issue
            for issue in report["issues"]
        ))

    def test_path_traversal_slug_is_rejected_before_source_access(self):
        conn = sqlite3.connect(self.db)
        report = {}
        issues = []
        entry = {
            "slug": "../outside",
            "bibliography_status": "sidecar-only",
        }

        with (
            patch.object(
                Path, "is_file",
                side_effect=AssertionError("unsafe source path was inspected")),
            patch.object(
                bib, "sha256",
                side_effect=AssertionError("unsafe source path was opened")),
        ):
            checker.validate_sidecar_only_sources(
                conn, [entry], self.papers_dir, report, issues)
        conn.close()

        self.assertEqual(report["sidecar_only_sources_unverifiable"], 1)
        self.assertEqual(report["sidecar_only_sources_not_ingested"], 0)
        self.assertEqual(
            issues,
            ["sidecar-only bibliography index entry has unsafe slug: "
             "'../outside'"],
        )


if __name__ == "__main__":
    unittest.main()
