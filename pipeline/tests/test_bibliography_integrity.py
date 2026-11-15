"""Foreign-key drift: prune must cascade by hand, finalize must sweep, check must report."""
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import build_bibliography_db as bib
import check_bibliography_db as check


def make_db(path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.executescript(bib.SCHEMA)
    conn.execute("PRAGMA foreign_keys = OFF")  # callers of the prune run this way
    return conn


def add_paper(conn: sqlite3.Connection, paper_id: int, review_dir: str) -> None:
    conn.execute(
        "INSERT INTO papers (paper_id, slug, title, review_dir) VALUES (?,?,?,?)",
        (paper_id, f"slug-{paper_id}", f"Title {paper_id}", review_dir))
    conn.execute(
        "INSERT INTO citation_snapshots (paper_id, observed_date) VALUES (?, '2026-01-01')",
        (paper_id,))
    conn.execute(
        "INSERT INTO extraction_attempts (paper_id, extractor, attempted_at, outcome)"
        " VALUES (?, 'x', '2026-01-01', 'empty')", (paper_id,))


class PruneMissingPapersTests(unittest.TestCase):
    def test_removes_snapshots_and_attempts_of_vanished_paper(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs" / "papers" / "slug-1").mkdir(parents=True)
            conn = make_db(root / "b.sqlite3")
            add_paper(conn, 1, "docs/papers/slug-1")
            add_paper(conn, 2, "docs/papers/slug-2")  # directory absent
            with mock.patch.object(bib, "ROOT", root):
                self.assertEqual(bib.prune_missing_papers(conn), 1)
            for table in ("citation_snapshots", "extraction_attempts"):
                ids = [r[0] for r in conn.execute(f"SELECT paper_id FROM {table}")]
                self.assertEqual(ids, [1], table)
            self.assertEqual(conn.execute("PRAGMA foreign_key_check").fetchall(), [])
            conn.close()


class PruneOrphanRowsTests(unittest.TestCase):
    def test_deletes_existing_orphans_and_keeps_valid_rows(self):
        with tempfile.TemporaryDirectory() as tmp:
            conn = make_db(Path(tmp) / "b.sqlite3")
            add_paper(conn, 1, "docs/papers/slug-1")
            for orphan in (66, 2271):
                conn.execute(
                    "INSERT INTO citation_snapshots (paper_id, observed_date)"
                    " VALUES (?, '2026-01-01')", (orphan,))
            self.assertEqual(len(conn.execute("PRAGMA foreign_key_check").fetchall()), 2)
            self.assertEqual(bib.prune_orphan_rows(conn), 2)
            self.assertEqual(
                [r[0] for r in conn.execute("SELECT paper_id FROM citation_snapshots")], [1])
            self.assertEqual(conn.execute("SELECT COUNT(*) FROM papers").fetchone()[0], 1)
            self.assertEqual(bib.prune_orphan_rows(conn), 0)
            conn.close()


class CheckForeignKeyTests(unittest.TestCase):
    def test_collect_reports_orphan_row(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / "b.sqlite3"
            conn = make_db(db)
            add_paper(conn, 1, "docs/papers/slug-1")
            conn.execute(
                "INSERT INTO citation_snapshots (paper_id, observed_date)"
                " VALUES (66, '2026-01-01')")
            conn.commit()
            conn.close()
            report, issues, warnings = {}, [], []
            check.collect(db, report, issues, warnings)
            self.assertEqual(report["foreign_key_violations"], 1)
            self.assertIn(
                "foreign key violations: 1 (run build_bibliography_db.py --finalize)",
                issues)


if __name__ == "__main__":
    unittest.main()


class IngestReviewedPaperTests(unittest.TestCase):
    """Review generation writes one paper and settles its institutions."""

    def test_unregistered_slug_is_refused(self):
        with mock.patch.object(bib, "load_entries", return_value=[]), \
                mock.patch.object(bib, "build") as build:
            with self.assertRaises(ValueError):
                bib.ingest_reviewed_paper("042_x", Path("unused.sqlite3"))
        build.assert_not_called()

    def test_one_paper_is_built_linked_and_finalized(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / "bib.sqlite3"
            conn = make_db(db)
            conn.execute("INSERT INTO papers (paper_id, slug, title, review_dir) VALUES (1, '042_x', 'T', 'docs/papers/042_x')")
            conn.execute(
                "INSERT INTO institutions (institution_id, institution_name, normalized_name, "
                "country_name_en, city_name, parent_name, ror_id, source) VALUES "
                "(7, 'IBM Research - Zurich', 'ibm research - zurich', 'Switzerland', "
                "'Rüschlikon', 'IBM', 'r:zrl', 'test')")
            conn.execute("INSERT INTO paper_institutions VALUES (1, 7, 'IBM Research', 'CH', 'pdf')")
            conn.commit()
            conn.close()
            calls = []
            entries = [{"slug": "042_x"}, {"slug": "043_y"}]
            with mock.patch.object(bib, "load_entries", return_value=entries), \
                    mock.patch.object(bib, "build", side_effect=lambda e, *a, **k: calls.append(
                        ("build", [x["slug"] for x in e], k)) or {"processed": len(e)}), \
                    mock.patch.object(bib, "backfill_author_institutions", side_effect=lambda *a, **k: calls.append(
                        ("backfill", k["slugs"])) or {}), \
                    mock.patch.object(bib, "finalize", side_effect=lambda *a, **k: calls.append(
                        ("finalize",)) or {}):
                result = bib.ingest_reviewed_paper("042_x", db)
        self.assertEqual([c[0] for c in calls], ["build", "backfill", "finalize"])
        self.assertEqual(calls[0][1], ["042_x"])
        self.assertTrue(calls[0][2]["skip_zotero"])
        self.assertTrue(calls[0][2]["offline"])
        self.assertEqual(calls[1][1], {"042_x"})
        self.assertEqual(result["institutions"], [{
            "institution": "IBM Research - Zurich", "parent": "IBM",
            "city": "Rüschlikon", "country": "Switzerland",
            "ror_id": "r:zrl", "source": "pdf"}])
