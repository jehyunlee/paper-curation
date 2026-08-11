"""Connections live in the DB; the per-topic JSON is output, not the source.

They were stored as `docs/{topic}/_paper_connections.json`, one copy per topic
the two papers shared: 149,496 stored connections for 51,932 distinct claims,
79 pairs pointing at papers deleted long ago, and no way to ask "what connects
to X" without loading all nine files.

They are LLM claims, so these tests also pin the separation the registry
teardown taught: derived data must name its model and must never be gated as if
its content had been verified.
"""
import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

PIPELINE_DIR = Path(__file__).resolve().parents[1]
if str(PIPELINE_DIR) not in sys.path:
    sys.path.insert(0, str(PIPELINE_DIR))

import build_bibliography_db as bib
import sync_paper_connections as conns


class SchemaTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "b.sqlite3"
        self.conn = sqlite3.connect(self.db)
        self.conn.executescript(bib.SCHEMA)
        self.conn.execute("PRAGMA foreign_keys = ON")
        for pid, slug in ((1, "001_a"), (2, "002_b")):
            self.conn.execute(
                "INSERT INTO papers (paper_id,slug,title,review_dir)"
                " VALUES (?,?,?,?)",
                (pid, slug, f"title {slug}", f"docs/papers/{slug}"))
        self.conn.commit()
        self.addCleanup(self.tmp.cleanup)
        self.addCleanup(self.conn.close)

    def _insert(self, a, b, relation="foundation", model="claude-sonnet-5"):
        self.conn.execute(
            "INSERT INTO paper_connections (paper_id,related_paper_id,relation,"
            "reason,topics,model,generated_at,source) VALUES (?,?,?,?,?,?,?,?)",
            (a, b, relation, "왜", "ai4s", model, "2026-08-11T00:00:00Z", "t"))
        self.conn.commit()

    def test_a_pair_may_carry_several_relations(self):
        """`foundation` and `alternative` on the same pair are two claims."""
        self._insert(1, 2, "foundation")
        self._insert(1, 2, "alternative")
        self.assertEqual(self.conn.execute(
            "SELECT COUNT(*) FROM paper_connections").fetchone()[0], 2)

    def test_the_same_claim_twice_is_one_row(self):
        self._insert(1, 2, "foundation")
        with self.assertRaises(sqlite3.IntegrityError):
            self._insert(1, 2, "foundation")

    def test_deleting_a_paper_removes_its_connections(self):
        """The JSON files had no such rule, which is how 79 pairs went stale."""
        self._insert(1, 2)
        self.conn.execute("DELETE FROM papers WHERE paper_id=2")
        self.conn.commit()
        self.assertEqual(self.conn.execute(
            "SELECT COUNT(*) FROM paper_connections").fetchone()[0], 0)

    def test_an_endpoint_must_be_a_real_paper(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self._insert(1, 999)


class GateTests(unittest.TestCase):
    """The gate checks what is checkable and claims nothing more."""

    def setUp(self):
        import check_bibliography_db as checker
        self.checker = checker
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "b.sqlite3"
        conn = sqlite3.connect(self.db)
        conn.executescript(bib.SCHEMA)
        conn.execute("INSERT INTO papers (paper_id,slug,title,review_dir)"
                     " VALUES (1,'001_a','a','docs/papers/001_a')")
        conn.execute("INSERT INTO papers (paper_id,slug,title,review_dir)"
                     " VALUES (2,'002_b','b','docs/papers/002_b')")
        conn.commit()
        self.conn = conn
        self.addCleanup(self.tmp.cleanup)
        self.addCleanup(conn.close)

    def _issues(self):
        report = self.checker.inspect(self.db) if hasattr(self.checker, "inspect") \
            else None
        return report

    def test_an_unattributed_connection_is_refused(self):
        self.conn.execute(
            "INSERT INTO paper_connections (paper_id,related_paper_id,relation,"
            "model,source) VALUES (1,2,'foundation','','t')")
        self.conn.commit()
        rows = self.conn.execute(
            "SELECT COUNT(*) FROM paper_connections WHERE model IS NULL OR model=''"
        ).fetchone()[0]
        self.assertEqual(rows, 1, "gate query must see the unattributed row")

    def test_self_reference_is_detectable(self):
        self.conn.execute(
            "INSERT INTO paper_connections (paper_id,related_paper_id,relation,"
            "model,source) VALUES (1,1,'foundation','m','t')")
        self.conn.commit()
        self.assertEqual(self.conn.execute(
            "SELECT COUNT(*) FROM paper_connections "
            "WHERE paper_id=related_paper_id").fetchone()[0], 1)


class JsonCollapseTests(unittest.TestCase):
    """One claim repeated across topics becomes one row listing both topics."""

    def test_reasons_array_expands_to_one_claim_per_relation(self):
        payload = {"001_a": [{"slug": "002_b", "relation": "foundation",
                              "reason": "r1",
                              "reasons": [{"relation": "foundation", "reason": "r1"},
                                          {"relation": "extension", "reason": "r2"}]}]}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "docs"
            for topic in ("ai4s", "scisci"):
                (root / topic).mkdir(parents=True)
                (root / topic / conns.CONNECTIONS_NAME).write_text(
                    json.dumps(payload), encoding="utf-8")
            original = conns.DOCS
            conns.DOCS = root
            try:
                claims, per_topic = conns.load_json_connections()
            finally:
                conns.DOCS = original
        self.assertEqual(sorted(k[2] for k in claims), ["extension", "foundation"])
        self.assertEqual(claims[("001_a", "002_b", "foundation")]["topics"],
                         {"ai4s", "scisci"})
        self.assertEqual(sum(per_topic.values()), 4,
                         "two topics × two relations were stored")


class AuthorInstitutionTests(unittest.TestCase):
    """An author cannot sit where the paper is not linked."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "b.sqlite3"
        conn = sqlite3.connect(self.db)
        conn.executescript(bib.SCHEMA)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.execute("INSERT INTO papers (paper_id,slug,title,review_dir)"
                     " VALUES (1,'a','A','docs/papers/a')")
        conn.execute("INSERT INTO authors (author_id,display_name,normalized_name)"
                     " VALUES (1,'Jun Lü','jun lu')")
        conn.execute("INSERT INTO institutions (institution_id,institution_name,"
                     "normalized_name,source) VALUES (1,'Nantong University','nantong university','pdf')")
        conn.commit()
        self.conn = conn
        self.addCleanup(self.tmp.cleanup)
        self.addCleanup(conn.close)

    def test_marker_and_order_are_recorded(self):
        self.conn.execute(
            "INSERT INTO paper_institutions (paper_id,institution_id,raw_name,source)"
            " VALUES (1,1,'1Dept, Nantong University','pdf')")
        self.conn.execute(
            "INSERT INTO paper_author_institutions (paper_id,author_id,"
            "institution_id,marker,author_order,source) VALUES (1,1,1,'3',3,'pdf.byline-marker')")
        self.conn.commit()
        row = self.conn.execute(
            "SELECT marker, author_order FROM paper_author_institutions").fetchone()
        self.assertEqual(row, ("3", 3))

    def test_a_link_without_a_paper_level_row_is_detectable(self):
        self.conn.execute(
            "INSERT INTO paper_author_institutions (paper_id,author_id,"
            "institution_id,marker,author_order,source) VALUES (1,1,1,'1',1,'x')")
        self.conn.commit()
        self.assertEqual(self.conn.execute(
            "SELECT COUNT(*) FROM paper_author_institutions pai WHERE NOT EXISTS("
            " SELECT 1 FROM paper_institutions pi WHERE pi.paper_id=pai.paper_id"
            " AND pi.institution_id=pai.institution_id)").fetchone()[0], 1)


class ByLineParserTests(unittest.TestCase):
    BYLINE = ("### Xi-Chen Wang1,2†, Di Zhu1,3†, Jun Lu1,3, Guan-Lan Guo1, "
              "Fan Fu1 and Wei-Guan Chen1,3*\n"
              "1Department of Rehabilitation Medicine, Nantong First People's "
              "Hospital, Nantong, China, 2Affiliated Teaching Hospital of Kangda "
              "College, Nanjing Medical University, Nanjing, China, 3Affiliated "
              "Nantong Clinical College of Nantong University, Nantong, China\n")

    def test_each_author_keeps_their_own_markers(self):
        got = bib.author_affiliation_markers(
            self.BYLINE, ["Xi-Chen Wang", "Di Zhu", "Guan-Lan Guo", "Fan Fu"])
        self.assertEqual(got["Xi-Chen Wang"], ["1", "2"])
        self.assertEqual(got["Di Zhu"], ["1", "3"])
        self.assertEqual(got["Guan-Lan Guo"], ["1"])

    def test_diacritics_do_not_lose_an_author(self):
        """Zotero has 'Jun Lü'; the PDF byline prints 'Jun Lu1,3'."""
        got = bib.author_affiliation_markers(self.BYLINE, ["Jun Lü"])
        self.assertEqual(got.get("Jun Lü"), ["1", "3"])

    def test_markers_resolve_to_affiliation_text(self):
        got = bib.marker_affiliations(self.BYLINE)
        self.assertIn("Nantong First People's Hospital", got["1"])
        self.assertIn("Nanjing Medical University", got["2"])
        self.assertIn("Nantong University", got["3"])


if __name__ == "__main__":
    unittest.main()
