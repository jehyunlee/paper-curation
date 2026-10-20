"""Connections live in the DB; the per-topic JSON is output, not the source.

They were stored as `docs/{topic}/_paper_connections.json`, one copy per topic
the two papers shared: 149,496 stored connections for 51,932 distinct claims,
79 pairs pointing at papers deleted long ago, and no way to ask "what connects
to X" without loading all nine files.

They are embedding neighbours, so these tests also pin the separation between
retrieval evidence and publisher-verified bibliographic facts.
"""
import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

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
                              "basis": "embedding",
                              "reasons": [{"relation": "foundation", "reason": "r1"},
                                          {"relation": "extension", "reason": "r2"}]}],
                   "002_b": []}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "docs"
            (root / "papers").mkdir(parents=True)
            (root / "papers" / "_papers_index.json").write_text(json.dumps([
                {"slug": "001_a", "topics": ["ai4s", "scisci"]},
                {"slug": "002_b", "topics": ["ai4s", "scisci"]},
            ]), encoding="utf-8")
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


class ConnectionSyncTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name) / "docs"
        self.db = Path(tmp.name) / "bibliography.sqlite3"
        (self.root / "papers").mkdir(parents=True)
        self.index = self.root / "papers" / "_papers_index.json"
        self.index.write_text(json.dumps([
            {"slug": "001_a", "topics": ["ai4s", "scisci"]},
            {"slug": "002_b", "topics": ["ai4s", "scisci"]},
            {"slug": "003_empty", "topics": ["ai4s"]},
        ]), encoding="utf-8")
        self.docs_patch = patch.object(conns, "DOCS", self.root)
        self.docs_patch.start()
        self.addCleanup(self.docs_patch.stop)
        with sqlite3.connect(self.db) as conn:
            conn.executescript(bib.SCHEMA)
            for pid, slug in enumerate(("001_a", "002_b", "003_empty"), 1):
                conn.execute("INSERT INTO papers (paper_id,slug,title,review_dir)"
                             " VALUES (?,?,?,?)", (pid, slug, slug, f"docs/papers/{slug}"))
            conn.execute("INSERT INTO authors (display_name,normalized_name)"
                         " VALUES ('Unchanged Author','unchanged author')")
        self.edge = {"slug": "002_b", "relation": "alternative", "reason": "임베딩 이웃",
                     "basis": "embedding", "model": "", "evidence": {"cosine": .8765}}
        self.write_graphs({"001_a": [self.edge], "002_b": [], "003_empty": []})

    def write_graph(self, topic, graph):
        path = self.root / topic / conns.CONNECTIONS_NAME
        path.parent.mkdir(exist_ok=True)
        path.write_text(json.dumps(graph, ensure_ascii=False), encoding="utf-8")
        return path

    def write_graphs(self, graph):
        graph = {"001_a": [], "002_b": [], "003_empty": [], **graph}
        for topic in ("ai4s", "scisci"):
            self.write_graph(topic, graph)
        self.write_graph("retired-topic", {})

    def read_graph(self, topic):
        return json.loads((self.root / topic / conns.CONNECTIONS_NAME).read_text(encoding="utf-8"))

    def snapshot(self):
        with sqlite3.connect(self.db) as conn:
            return tuple(conn.iterdump())

    def make_legacy_table(self):
        with sqlite3.connect(self.db) as conn:
            conn.execute("DROP TABLE paper_connections")
            conn.execute("""CREATE TABLE paper_connections (
                paper_id INTEGER NOT NULL REFERENCES papers ON DELETE CASCADE,
                related_paper_id INTEGER NOT NULL REFERENCES papers ON DELETE CASCADE,
                relation TEXT NOT NULL, reason TEXT, topics TEXT, model TEXT,
                generated_at TEXT, source TEXT NOT NULL,
                PRIMARY KEY (paper_id,related_paper_id,relation))""")
            conn.execute("INSERT INTO paper_connections (paper_id,related_paper_id,"
                         "relation,reason,topics,model,source)"
                         " VALUES (1,2,'foundation','obsolete judgement','ai4s','old-judge','test')")

    def test_roundtrip_preserves_distinct_item_and_reason_evidence(self):
        edge = {**self.edge, "reason": "요약 설명", "evidence": {
            "cosine": .8765, "rank": 2, "rrf": .040983606557377046},
            "reasons": [
                {"relation": "alternative", "reason": "첫 번째 수치 근거",
                 "basis": "embedding", "model": "", "evidence": {"cosine": .7456, "rank": 1}},
                {"relation": "extension", "reason": "두 번째 수치 근거",
                 "basis": "embedding", "model": "", "evidence": {
                     "cosine": -.1234, "bm25": {"rank": 0, "score": 1.25}}},
            ]}
        self.write_graphs({"001_a": [edge], "002_b": [], "003_empty": []})
        result = conns.import_connections(self.db)
        self.assertEqual(result["imported"], 2)
        with sqlite3.connect(self.db) as conn:
            stored = json.loads(conn.execute(
                "SELECT evidence FROM paper_connections WHERE relation='alternative'").fetchone()[0])
            self.assertEqual(stored["item"]["evidence"], edge["evidence"])
            self.assertEqual(stored["reason"]["evidence"], edge["reasons"][0]["evidence"])
            self.assertIsInstance(stored["item"]["evidence"]["cosine"], float)
        self.write_graphs({})
        conns.export_connections(self.db)
        self.assertEqual(self.read_graph("ai4s")["001_a"], [edge])
        self.assertEqual(self.read_graph("scisci")["001_a"], [edge])
        self.assertEqual(self.read_graph("ai4s")["003_empty"], [])
        conns.import_connections(self.db)
        conns.export_connections(self.db)
        self.assertEqual(self.read_graph("ai4s")["001_a"], [edge])

    def test_last_edge_removal_replaces_stale_sources_and_empty_topics(self):
        conns.import_connections(self.db)
        self.write_graphs({"001_a": [], "002_b": [], "003_empty": []})
        self.assertEqual(conns.import_connections(self.db)["imported"], 0)
        self.write_graphs({"001_a": [self.edge]})
        self.write_graph("retired-topic", {"001_a": [self.edge]})
        result = conns.export_connections(self.db)
        self.assertEqual(result["topics"], {"ai4s": 0, "retired-topic": 0, "scisci": 0})
        self.assertEqual(self.read_graph("ai4s"), {"001_a": [], "002_b": [], "003_empty": []})
        self.assertEqual(self.read_graph("scisci"), {"001_a": [], "002_b": []})
        self.assertEqual(self.read_graph("retired-topic"), {})

    def test_model_only_import_and_export_are_empty(self):
        conns.import_connections(self.db)
        judged = {**self.edge, "basis": "model", "model": "old-judge"}
        self.write_graphs({"001_a": [judged]})
        self.assertEqual(conns.import_connections(self.db)["imported"], 0)
        with sqlite3.connect(self.db) as conn:
            conn.execute("INSERT INTO paper_connections (paper_id,related_paper_id,"
                         "relation,model,topics,source) VALUES (1,2,'foundation','old-judge','ai4s','test')")
        conns.export_connections(self.db)
        self.assertEqual(self.read_graph("ai4s")["001_a"], [])
        self.assertEqual(self.read_graph("retired-topic"), {})

    def test_mixed_basis_reasons_do_not_export_a_judged_header(self):
        self.write_graphs({"001_a": [{"slug": "002_b", "relation": "foundation",
            "reason": "obsolete judgement", "basis": "model", "evidence": {"score": .99},
            "reasons": [
                {"relation": "foundation", "reason": "obsolete judgement", "basis": "model"},
                {"relation": "alternative", "reason": "embedding neighbour", "basis": "embedding",
                 "evidence": {"cosine": .81}},
            ]}]})
        conns.import_connections(self.db)
        conns.export_connections(self.db)
        edge = self.read_graph("ai4s")["001_a"][0]
        self.assertEqual(edge["relation"], "alternative")
        self.assertEqual(edge["reason"], "embedding neighbour")
        self.assertEqual(edge["evidence"], {"cosine": .81})
        self.assertEqual([r["basis"] for r in edge["reasons"]], ["embedding"])

    def test_malformed_input_aborts_without_changing_the_db(self):
        conns.import_connections(self.db)
        before = self.snapshot()
        invalid = ["{", "null", "[]", '{"001_a":null,"002_b":[]}',
                   '{"001_a":[null],"002_b":[]}', '{"001_a":[{}],"002_b":[]}',
                   '{"001_a":[],"001_a":[],"002_b":[]}',
                   json.dumps({"001_a": [{**self.edge, "reasons": {}}], "002_b": []}),
                   json.dumps({"001_a": [{**self.edge, "reasons": [None]}], "002_b": []}),
                   json.dumps({"001_a": [{**self.edge, "reason": 4}], "002_b": []}),
                   json.dumps({"001_a": [{**self.edge, "evidence": []}], "002_b": []}),
                   json.dumps({"001_a": [{**self.edge, "evidence": {"cosine": "0.8"}}], "002_b": []}),
                   json.dumps({"001_a": [{**self.edge, "evidence": {"cosine": True}}], "002_b": []}),
                   json.dumps({"001_a": [{**self.edge, "evidence": {"cosine": float("nan")}}], "002_b": []}),
                   '{"001_a":[{"slug":"002_b","basis":"embedding","evidence":{"cosine":1e999}}],"002_b":[]}']
        path = self.root / "scisci" / conns.CONNECTIONS_NAME
        for contents in invalid:
            with self.subTest(contents=contents):
                path.write_text(contents, encoding="utf-8")
                with self.assertRaises(ValueError):
                    conns.import_connections(self.db)
                self.assertEqual(self.snapshot(), before)

    def test_missing_unreadable_or_invalid_utf8_input_leaves_db_unchanged(self):
        conns.import_connections(self.db)
        before = self.snapshot()
        path = self.root / "scisci" / conns.CONNECTIONS_NAME
        contents = path.read_text(encoding="utf-8")
        path.unlink()
        with self.assertRaisesRegex(ValueError, "missing connection inputs"):
            conns.import_connections(self.db)
        self.assertEqual(self.snapshot(), before)
        path.write_bytes(b"\xff")
        with self.assertRaises(ValueError):
            conns.import_connections(self.db)
        self.assertEqual(self.snapshot(), before)
        path.write_text(contents, encoding="utf-8")
        read_text = Path.read_text

        def unreadable(target, *args, **kwargs):
            if target == path:
                raise PermissionError("unreadable topic input")
            return read_text(target, *args, **kwargs)

        with patch.object(Path, "read_text", unreadable):
            with self.assertRaisesRegex(ValueError, "unreadable topic input"):
                conns.import_connections(self.db)
        self.assertEqual(self.snapshot(), before)
        self.index.unlink()
        with self.assertRaises(ValueError):
            conns.import_connections(self.db)
        self.assertEqual(self.snapshot(), before)

    def test_conflicting_cross_topic_evidence_aborts(self):
        conns.import_connections(self.db)
        before = self.snapshot()
        self.write_graph("scisci", {"001_a": [{**self.edge, "evidence": {"cosine": .2}}], "002_b": []})
        with self.assertRaisesRegex(ValueError, "conflicting copies"):
            conns.import_connections(self.db)
        self.assertEqual(self.snapshot(), before)

    def test_union_memberships_and_cross_empty_sources_are_preserved(self):
        self.index.write_text(json.dumps([
            {"slug": "001_a", "topics": ["ai4s"], "primary_topic": "scisci",
             "classifications": {"classified-only": {"primary_category": "Methods"}}},
            {"slug": "002_b", "topics": [], "primary_topic": "scisci"},
            {"slug": "003_empty", "topics": [], "classifications": {"classified-only": {}}},
        ]), encoding="utf-8")
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, "missing connection inputs for topics: classified-only"):
            conns.import_connections(self.db)
        self.assertEqual(self.snapshot(), before)
        self.write_graph("classified-only", {"001_a": [], "003_empty": []})
        self.write_graph("_cross", {"001_a": [], "002_b": [], "003_empty": []})
        conns.import_connections(self.db)
        conns.export_connections(self.db)
        self.assertEqual(self.read_graph("classified-only"), {"001_a": [], "003_empty": []})
        self.assertEqual(self.read_graph("_cross"), {"001_a": [], "002_b": [], "003_empty": []})
        self.assertEqual(set(self.read_graph("scisci")), {"001_a", "002_b"})

    def test_missing_managed_source_key_aborts_even_when_topic_file_exists(self):
        conns.import_connections(self.db)
        before = self.snapshot()
        self.write_graph("scisci", {"001_a": [self.edge]})
        with self.assertRaisesRegex(ValueError, "missing source keys: 002_b"):
            conns.import_connections(self.db)
        self.assertEqual(self.snapshot(), before)
        self.write_graph("scisci", {"001_a": [self.edge], "002_b": []})
        self.write_graph("_cross", {"001_a": [], "002_b": []})
        with self.assertRaisesRegex(ValueError, "missing source keys: 003_empty"):
            conns.import_connections(self.db)
        self.assertEqual(self.snapshot(), before)

    def test_legacy_schema_is_replaced_without_migrating_judged_edges(self):
        self.make_legacy_table()
        before = self.snapshot()
        self.assertTrue(conns.import_connections(self.db, dry_run=True)["schema_recreated"])
        self.assertEqual(self.snapshot(), before)
        result = conns.import_connections(self.db)
        self.assertTrue(result["schema_recreated"])
        with sqlite3.connect(self.db) as conn:
            self.assertIn("evidence", {row[1] for row in conn.execute("PRAGMA table_info(paper_connections)")})
            self.assertEqual(conn.execute("SELECT relation,model FROM paper_connections").fetchall(),
                             [("alternative", conns.EMBEDDING_MODEL)])
            self.assertEqual(conn.execute("SELECT COUNT(*) FROM papers").fetchone()[0], 3)
            self.assertEqual(conn.execute("SELECT display_name FROM authors").fetchall(), [("Unchanged Author",)])

    def test_failed_schema_replacement_rolls_back_the_old_table(self):
        self.make_legacy_table()
        before = self.snapshot()
        with patch.object(conns, "PAPER_CONNECTIONS_SCHEMA", bib.PAPER_CONNECTIONS_SCHEMA + "INVALID SQL;"):
            with self.assertRaises(sqlite3.OperationalError):
                conns.import_connections(self.db)
        self.assertEqual(self.snapshot(), before)
        (self.root / "scisci" / conns.CONNECTIONS_NAME).write_text("{", encoding="utf-8")
        with self.assertRaises(ValueError):
            conns.import_connections(self.db)
        self.assertEqual(self.snapshot(), before)


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
