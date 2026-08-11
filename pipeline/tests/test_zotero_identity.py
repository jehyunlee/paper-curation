"""A paper must carry its own bibliography, not a neighbour's.

Every literal here reached the shipped DB. 342 papers were attached to 8
Zotero items because a placeholder string passed for a DOI, and paper 1042 was
stored under the title, journal, volume, pages, publisher and ISSN of a
different work because its Zotero item held another paper's metadata.
"""
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

from lib import zotero_identity as zi


def make_db(rows):
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE papers (slug TEXT, title TEXT, doi TEXT,"
                 " zotero_item_key TEXT)")
    conn.executemany("INSERT INTO papers VALUES (?,?,?,?)", rows)
    conn.commit()
    return conn


def make_corpus(titles):
    directory = Path(tempfile.mkdtemp())
    for slug, title in titles.items():
        paper = directory / slug
        paper.mkdir(parents=True)
        (paper / "review.md").write_text(
            f'---\ntitle: "{title}"\nauthors:\n  - "X"\n---\n',
            encoding="utf-8")
    return directory


class PlaceholderDoiTests(unittest.TestCase):
    def test_words_meaning_no_doi_are_reported(self):
        conn = make_db([
            ("884_Wiki", "Semantic Scholar", "N/A", "XIN7LQIB"),
            ("470_Self", "Semantic Scholar", "미제공", "XIN7LQIB"),
            ("481_Lazy", "Openai o1 system card", "-", "SD3SZZXM"),
            ("1042_Sch", "Ok", "10.3389/frma.2021.751553", "RM7J55RG"),
        ])
        found = {row["doi"] for row in zi.placeholder_dois(conn)}
        self.assertEqual(found, {"N/A", "미제공", "-"})

    def test_a_real_doi_is_never_reported(self):
        conn = make_db([("a", "t", "10.1038/s41586-026-10652-y", "K")])
        self.assertEqual(zi.placeholder_dois(conn), [])

    def test_empty_doi_is_not_a_defect(self):
        conn = make_db([("a", "t", "", "K")])
        self.assertEqual(zi.placeholder_dois(conn), [])


class SharedZoteroKeyTests(unittest.TestCase):
    def test_one_item_on_many_papers_is_reported_worst_first(self):
        conn = make_db([
            ("a", "Semantic Scholar", "N/A", "XIN7LQIB"),
            ("b", "Semantic Scholar", "N/A", "XIN7LQIB"),
            ("c", "Semantic Scholar", "N/A", "XIN7LQIB"),
            ("d", "Withdrarxiv", "미공개", "AJWCA76M"),
            ("e", "Withdrarxiv", "미공개", "AJWCA76M"),
            ("f", "Fine", "10.1000/x", "UNIQUE1"),
        ])
        shared = zi.shared_zotero_keys(conn)
        self.assertEqual([row["zotero_item_key"] for row in shared],
                         ["XIN7LQIB", "AJWCA76M"])
        self.assertEqual(shared[0]["papers"], 3)
        self.assertEqual(sorted(shared[0]["slugs"]), ["a", "b", "c"])

    def test_one_paper_per_item_is_clean(self):
        conn = make_db([("a", "t", "10.1000/x", "K1"), ("b", "u", "10.1000/y", "K2")])
        self.assertEqual(zi.shared_zotero_keys(conn), [])

    def test_a_correction_and_its_original_are_expected(self):
        # A journal publishes "Correction: X" as its own article; Zotero may
        # hold one item for both. That is not a paper wearing another's
        # bibliography, so it must not be queued for repair.
        conn = make_db([
            ("1156_Corr", "Correction: Enabling transparent research "
                          "evaluation", "10.1162/qss_x_00123", "FCTXZTSA"),
            ("1167_Orig", "Enabling transparent research evaluation",
             "10.1162/qss_a_00456", "FCTXZTSA"),
        ])
        shared = zi.shared_zotero_keys(conn)
        self.assertEqual([row["kind"] for row in shared], ["correction"])

    def test_two_unrelated_papers_on_one_item_stay_unresolved(self):
        conn = make_db([
            ("a", "Quantifying the dynamics of failure", "10.1038/x1", "T"),
            ("b", "A completely different paper", "10.1038/x2", "T"),
        ])
        self.assertEqual(
            [row["kind"] for row in zi.shared_zotero_keys(conn)],
            ["unresolved"])

    def test_correction_pairs_are_excluded_from_repair(self):
        corpus = make_corpus({
            "1156_Corr": "Correction: Enabling transparent research evaluation",
            "1167_Orig": "Enabling transparent research evaluation"})
        conn = make_db([
            ("1156_Corr", "Correction: Enabling transparent research "
                          "evaluation", "10.1162/qss_x_00123", "FCTXZTSA"),
            ("1167_Orig", "Enabling transparent research evaluation",
             "10.1162/qss_a_00456", "FCTXZTSA"),
        ])
        report = zi.audit(conn, corpus)
        self.assertEqual(report["correction_pairs"], 1)
        self.assertEqual(report["papers_on_a_shared_key"], 0)
        self.assertEqual(report["affected_slugs"], [])


class TitleDisagreementTests(unittest.TestCase):
    FRONTIERS = ("The Scholarly Knowledge Ecosystem: Challenges and "
                 "Opportunities for the Field of Information")
    ICC = ("The reorganization of the American innovation ecosystem and the "
           "challenge of translating science")

    def test_another_works_title_is_reported(self):
        corpus = make_corpus({"1042_Sch": self.FRONTIERS})
        conn = make_db([("1042_Sch", self.ICC,
                         "10.3389/frma.2021.751553", "RM7J55RG")])
        found = zi.title_disagreements(conn, corpus)
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]["slug"], "1042_Sch")
        self.assertLess(found[0]["similarity"], zi.TITLE_AGREEMENT_FLOOR)

    def test_punctuation_and_case_drift_is_not_a_disagreement(self):
        corpus = make_corpus({"a": self.FRONTIERS})
        conn = make_db([("a", self.FRONTIERS.upper() + ".", "10.1000/x", "K")])
        self.assertEqual(zi.title_disagreements(conn, corpus), [])

    def test_a_korean_review_title_is_not_judged(self):
        # Paper 409's review is titled in Korean while the DB holds the
        # English title. They share no characters without either being wrong.
        corpus = make_corpus(
            {"409_AI": "AI 아이디어가 인간의 창의성에 미치는 영향"})
        conn = make_db([("409_AI", "How Experience Moderates the Impact of "
                         "Generative AI Ideas", "10.1145/3715928.3737481",
                         "W4XQYV9N")])
        self.assertEqual(zi.title_disagreements(conn, corpus), [])

    def test_a_missing_review_is_not_judged(self):
        conn = make_db([("gone", "Anything", "10.1000/x", "K")])
        self.assertEqual(
            zi.title_disagreements(conn, Path(tempfile.mkdtemp())), [])


class AuditTests(unittest.TestCase):
    def test_affected_slugs_union_every_defect(self):
        corpus = make_corpus({"a": "Real Title Of A", "d": "Real Title Of D"})
        conn = make_db([
            ("a", "Semantic Scholar", "N/A", "XIN7LQIB"),
            ("b", "Semantic Scholar", "N/A", "XIN7LQIB"),
            ("d", "Real Title Of D", "10.1000/ok", "UNIQUE1"),
        ])
        report = zi.audit(conn, corpus)
        self.assertEqual(report["placeholder_doi_papers"], 2)
        self.assertEqual(report["papers_on_a_shared_key"], 2)
        self.assertEqual(report["title_disagreements"], 1)   # only "a"
        self.assertEqual(report["affected_slugs"], ["a", "b"])

    def test_a_clean_corpus_reports_nothing(self):
        corpus = make_corpus({"a": "Real Title Of A"})
        conn = make_db([("a", "Real Title Of A", "10.1000/ok", "K1")])
        report = zi.audit(conn, corpus)
        self.assertEqual(report["affected_papers"], 0)
        self.assertEqual(report["affected_slugs"], [])


if __name__ == "__main__":
    unittest.main()
