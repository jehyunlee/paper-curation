import hashlib
from contextlib import closing
import importlib.util
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

MODULE = Path(__file__).resolve().parents[1] / 'export_bibliography_samples.py'
spec = importlib.util.spec_from_file_location('export_bibliography_samples', MODULE)
exporter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(exporter)


class SamplesTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.db = Path(self.tmp.name) / 'test.sqlite3'
        with closing(sqlite3.connect(self.db)) as c, c:
            c.executescript('''
                CREATE TABLE papers(paper_id INTEGER PRIMARY KEY, slug TEXT, title TEXT, header_raw TEXT, metadata_json TEXT, review_dir TEXT);
                CREATE TABLE authors(author_id INTEGER PRIMARY KEY, display_name TEXT);
                CREATE TABLE paper_authors(paper_id INTEGER REFERENCES papers, author_id INTEGER REFERENCES authors);
                CREATE TABLE institutions(institution_id INTEGER PRIMARY KEY, group_id INTEGER REFERENCES institution_groups);
                CREATE TABLE institution_groups(group_id INTEGER PRIMARY KEY);
                CREATE TABLE paper_institutions(paper_id INTEGER REFERENCES papers, institution_id INTEGER REFERENCES institutions);
                CREATE TABLE paper_connections(paper_id INTEGER REFERENCES papers, related_paper_id INTEGER REFERENCES papers);
                CREATE TABLE doi_resolutions(slug TEXT PRIMARY KEY, doi TEXT);
                CREATE TABLE source_documents(paper_id INTEGER REFERENCES papers, path TEXT, sha256 TEXT);
                CREATE TABLE extraction_attempts(paper_id INTEGER REFERENCES papers, detail TEXT, outcome TEXT);
                INSERT INTO papers VALUES(1,'one','Title <script>','secret','secret','secret'),(2,'two','Second','secret','secret','secret'),(3,'three','Third','secret','secret','secret');
                INSERT INTO authors VALUES(5,'Author'),(6,'Other');
                INSERT INTO paper_authors VALUES(1,5),(3,6);
                INSERT INTO institution_groups VALUES(9),(10);
                INSERT INTO institutions VALUES(7,9),(8,10);
                INSERT INTO paper_institutions VALUES(1,7),(3,8);
                INSERT INTO paper_connections VALUES(1,2),(1,3);
                INSERT INTO doi_resolutions VALUES('one','10/example'),('three','10/other');
                INSERT INTO source_documents VALUES(1,'secret','abc');
                INSERT INTO extraction_attempts VALUES(1,'secret','empty');
            ''')

    def test_bound_closure_and_read_only(self):
        before = hashlib.sha256(self.db.read_bytes()).digest()
        data = exporter.export_sample(self.db, 2)
        self.assertEqual(before, hashlib.sha256(self.db.read_bytes()).digest())
        self.assertEqual(data['paper_count'], 2)
        self.assertEqual(data['total_papers'], 3)
        self.assertEqual([r['paper_id'] for r in data['tables']['papers']], [1, 2])
        self.assertEqual(data['tables']['paper_connections'], [{'paper_id': 1, 'related_paper_id': 2}])
        self.assertEqual(data['tables']['authors'], [{'author_id': 5, 'display_name': 'Author'}])
        self.assertEqual(data['tables']['institution_groups'], [{'group_id': 9}])
        self.assertEqual(data['tables']['doi_resolutions'], [{'slug': 'one', 'doi': '10/example'}])
        self.assertIn('openalex_enrichment', data['missing_tables'])
        for table, omitted in exporter.OMITTED.items():
            for row in data['tables'][table]:
                self.assertFalse(set(row).intersection(omitted))
        self.assertNotIn('secret', json.dumps(data))

    def test_script_safe_round_trip(self):
        original = {'text': '</script><script>alert(1)</script>&\u2028\u2029 한글'}
        script = exporter.javascript(original)
        self.assertNotIn('<', script)
        self.assertNotIn('&', script)
        self.assertEqual(json.loads(script.removeprefix('window.BIBLIOGRAPHY_SAMPLE = ').rstrip(';\n')), original)

    def test_empty_sample_and_invalid_limit(self):
        with closing(sqlite3.connect(self.db)) as c, c:
            c.execute('DELETE FROM papers')
        data = exporter.export_sample(self.db, 100)
        self.assertEqual(data['paper_count'], 0)
        self.assertTrue(all(not rows for rows in data['tables'].values()))
        for limit in [0, -1, 1001]:
            with self.assertRaises(ValueError):
                exporter.export_sample(self.db, limit)

    def test_rejects_dangling_reference(self):
        with closing(sqlite3.connect(self.db)) as c, c:
            c.execute('INSERT INTO paper_authors VALUES(1,999)')
        with self.assertRaisesRegex(ValueError, 'Dangling FK'):
            exporter.export_sample(self.db, 2)


if __name__ == '__main__':
    unittest.main()
