import sqlite3
import sys
import unittest
from pathlib import Path

PIPELINE_DIR = Path(__file__).resolve().parents[1]
if str(PIPELINE_DIR) not in sys.path:
    sys.path.insert(0, str(PIPELINE_DIR))

import build_bibliography_db as bib  # noqa: E402
from lib import institution_policy as policy  # noqa: E402
from lib.ror_index import alias_keys, normalize  # noqa: E402

COUNTRY_OF = bib.country_from_raw


class FakeIndex:
    """The RorIndex surface the policy uses, over a handful of records."""

    available = True

    def __init__(self, orgs):
        self.orgs = {o["ror_id"]: o for o in orgs}

    def org(self, ror_id):
        o = self.orgs.get(ror_id)
        if not o:
            return None
        return {k: o.get(k, "") for k in ("ror_id", "display", "country_name",
                                          "country_code", "org_types", "status",
                                          "parent_id")}

    def reference(self, ror_id):
        o = self.orgs.get(ror_id, {})
        return {"wikipedia": o.get("wikipedia", ""), "city": o.get("city", ""),
                "country_name": o.get("country_name", "")}

    def name_keys(self, ror_id):
        o = self.orgs[ror_id]
        return sorted({normalize(n) for n in [o["display"], *o.get("aliases", [])]})

    def resolve(self, name, country_name=""):
        key = alias_keys(name)[0] if alias_keys(name) else ""
        hits = [o for o in self.orgs.values() if key in self.name_keys(o["ror_id"])]
        return self.org(hits[0]["ror_id"]) if len(hits) == 1 else None

    def display_is_english(self, ror_id):
        return self.orgs[ror_id].get("lang", "en") == "en"

    def other_records(self, name, ror_id):
        key = normalize(name)
        return [r for r in self.orgs if r != ror_id and key in self.name_keys(r)]

    def cities(self):
        out = {}
        for o in self.orgs.values():
            if o.get("city"):
                out.setdefault(o["country_name"], set()).add(o["city"])
        return out

    def digit_led_names(self):
        return {"23andme"}

    def top_parent(self, ror_id):
        o = self.orgs.get(ror_id)
        while o and o.get("parent_id") in self.orgs:
            o = self.orgs[o["parent_id"]]
        return None if not o or o["ror_id"] == ror_id else self.org(o["ror_id"])

    def close(self):
        pass


ORGS = [
    {"ror_id": "r:stanford", "display": "Stanford University",
     "country_name": "United States", "city": "Stanford",
     "wikipedia": "http://en.wikipedia.org/wiki/Stanford_University"},
    {"ror_id": "r:kist", "display": "Korea Institute of Science and Technology",
     "country_name": "South Korea", "city": "Seoul", "aliases": ["KIST"],
     "wikipedia": "https://en.wikipedia.org/wiki/Korea_Institute_of_Science_and_Technology"},
    {"ror_id": "r:ub", "display": "University of Barcelona",
     "country_name": "Spain", "city": "Barcelona",
     "aliases": ["Universitat de Barcelona"],
     "wikipedia": "https://ca.wikipedia.org/wiki/Universitat_de_Barcelona"},
    {"ror_id": "r:cmu", "display": "Carnegie Mellon University",
     "country_name": "United States", "city": "Pittsburgh",
     "wikipedia": "http://en.wikipedia.org/wiki/Carnegie_Mellon_University"},
    {"ror_id": "r:interaction", "display": "InterAction",
     "country_name": "United States"},
    {"ror_id": "r:google", "display": "Google (United States)",
     "country_name": "United States", "city": "Mountain View",
     "wikipedia": "http://en.wikipedia.org/wiki/Google"},
    {"ror_id": "r:google-ie", "display": "Google (Ireland)",
     "country_name": "Ireland", "city": "Dublin", "parent_id": "r:google",
     "wikipedia": "http://en.wikipedia.org/wiki/Google"},
    {"ror_id": "r:gt", "display": "Georgia Institute of Technology",
     "country_name": "United States", "city": "Atlanta", "aliases": ["Georgia Tech"],
     "wikipedia": "http://en.wikipedia.org/wiki/Georgia_Institute_of_Technology"},
    {"ror_id": "r:lmu", "display": "Ludwig-Maximilians-Universität München", "lang": "de",
     "country_name": "Germany", "city": "Munich", "aliases": ["LMU", "University of Munich"],
     "wikipedia": "https://de.wikipedia.org/wiki/Ludwig-Maximilians-Universit%C3%A4t_M%C3%BCnchen"},
    {"ror_id": "r:ibm", "display": "IBM (United States)",
     "country_name": "United States", "city": "Armonk",
     "wikipedia": "http://en.wikipedia.org/wiki/IBM"},
    {"ror_id": "r:ibm-zrl", "display": "IBM Research - Zurich",
     "country_name": "Switzerland", "city": "Rüschlikon", "parent_id": "r:ibm"},
    {"ror_id": "r:harvard", "display": "Harvard University",
     "country_name": "United States", "city": "Cambridge", "org_types": "education",
     "wikipedia": "http://en.wikipedia.org/wiki/Harvard_University"},
    {"ror_id": "r:hks", "display": "Harvard Kennedy School",
     "country_name": "United States", "city": "Cambridge", "parent_id": "r:harvard", "org_types": "education",
     "aliases": ["John F. Kennedy School of Government"]},
]

TITLES = {"en:Stanford University": "Stanford University",
          "en:Korea Institute of Science and Technology":
              "Korea Institute of Science and Technology",
          "ca:Universitat de Barcelona": "University of Barcelona",
          "en:Carnegie Mellon University": "Carnegie Mellon University",
          "en:Georgia Institute of Technology": "Georgia Tech",
          "de:Ludwig-Maximilians-Universität München": "LMU Munich",
          "en:Google": "Google", "en:IBM": "IBM",
          "en:Harvard University": "Harvard University"}


class CleaningRules(unittest.TestCase):
    def test_affiliation_numbers_are_removed(self):
        clean = policy.clean_affiliation_text
        self.assertEqual(clean("3Stanford University"), "Stanford University")
        self.assertEqual(clean("26University of Cambridge"), "University of Cambridge")
        self.assertEqual(clean("10 KU Leuven"), "KU Leuven")
        self.assertEqual(clean("3Tübingen AI Center"), "Tübingen AI Center")
        self.assertEqual(clean("†2Institute of X"), "Institute of X")
        self.assertEqual(clean("¹ Department of Pathology, Stanford University"),
                         "Department of Pathology, Stanford University")

    def test_digits_that_belong_to_a_name_stay(self):
        clean = policy.clean_affiliation_text
        self.assertEqual(clean("3M Company"), "3M Company")
        self.assertEqual(clean("Bio21 Institute"), "Bio21 Institute")
        self.assertEqual(clean("L3S Research Center"), "L3S Research Center")
        self.assertEqual(clean("23andMe", lambda t: t.casefold() == "23andme"),
                         "23andMe")

    def test_one_line(self):
        self.assertEqual(policy.one_line("Korea Uni- versity,\n Seoul"),
                         "Korea University, Seoul")
        self.assertEqual(policy.one_line("Re- public of Korea"), "Republic of Korea")
        self.assertEqual(policy.one_line("Electrical &amp; Computer Engineering"),
                         "Electrical & Computer Engineering")

    def test_tex_spacing_accents_are_dropped(self):
        # "ETH Zürich" as TeX-built PDFs extract it, glued or spaced.
        for raw in ("ETH Zu\u00a8rich", "ETH Zu \u00a8rich", "ETH Zu\u00a8 rich"):
            self.assertEqual(policy.one_line(raw), "ETH Zurich")
        self.assertEqual(
            policy.one_line("Ecole Polytechnique F\u00b4ed\u00b4erale de Lausanne"),
            "Ecole Polytechnique Federale de Lausanne")
        # Composed letters and a stray accent between words are left alone.
        self.assertEqual(policy.one_line("ETH Zürich"), "ETH Zürich")
        self.assertEqual(policy.one_line("A \u00a8 B"), "A \u00a8 B")

    def test_watermark(self):
        self.assertTrue(policy.is_access_watermark(
            "Authorized licensed use limited to: Korea Institute of Science and "
            "Technology. Downloaded on June 13,2026"))
        self.assertFalse(policy.is_access_watermark(
            "Korea Institute of Science and Technology (KIST), Seoul"))


class PlaceRules(unittest.TestCase):
    cities = {"United States": {"Stanford", "Atlanta"}, "South Korea": {"Seoul"}}

    def place(self, raw):
        return policy.explicit_place(raw, COUNTRY_OF, self.cities)

    def test_superscript_packed_line_states_no_place(self):
        # LabOS: Oregon State and UW on one line; "Seattle" is UW's city.
        self.assertTrue(policy.is_multi_affiliation(
            "School of EECS, Oregon State University, Corvallis, OR, USA "
            "⁵ Department of Bioengineering, University of Washington, Seattle, WA, USA"))
        self.assertEqual(self.place(
            "Oregon State University, Corvallis, OR, USA "
            "⁵ University of Washington, Atlanta, USA"), ("", ""))

    def test_explicit_city_and_country(self):
        self.assertEqual(self.place("Department of X, Stanford University, "
                                    "Stanford, CA 94305, USA")[1], "United States")
        self.assertEqual(self.place("KIST, Seoul 02792, Republic of Korea"),
                         ("Seoul", "South Korea"))

    def test_city_matches_without_accents_in_ror_spelling(self):
        cities = {"Iceland": {"Reykjavik"},
                  "Spain": {"Donostia / San Sebastian"}}
        # ASE (JPCM 2017): TeX accents, and the Spanish half of a dual name.
        self.assertEqual(policy.explicit_place(
            "S\u0131\u00b4minn, Reykjav\u0131\u00b4k, Iceland", COUNTRY_OF, cities),
            ("Reykjavik", "Iceland"))
        self.assertEqual(policy.explicit_place(
            "Universidad del Pa\u0131\u00b4s Vasco UPV/EHU, San Sebasti\u00b4an, Spain",
            COUNTRY_OF, cities), ("San Sebastian", "Spain"))

    def test_state_and_postcode_are_not_countries(self):
        self.assertEqual(self.place("Princeton University, Princeton, New Jersey"),
                         ("", ""))
        self.assertEqual(self.place("Georgia Tech, Atlanta, GA"), ("", ""))
        self.assertEqual(self.place("Georgia Tech, Atlanta, Georgia"), ("", ""))

    def test_run_together_affiliations_state_nothing(self):
        self.assertEqual(self.place("Shanghai Jiao Tong University, Shanghai, China "
                                    "Johns Hopkins University, Baltimore, USA"),
                         ("", ""))
        self.assertEqual(self.place("Wisconsin–Madison, 4University of Oxford, UK"),
                         ("", ""))


class IdentityEvidence(unittest.TestCase):
    def test_generic_phrase_in_prose_is_not_evidence(self):
        self.assertIs(policy.identity_evidence(
            "3 Layer Interaction . . . 58", ["interaction"]), False)
        self.assertIs(policy.identity_evidence(
            "German Research Center for AI (DFKI)", ["research center"]), False)

    def test_distinctive_or_whole_segment_name_is_evidence(self):
        self.assertIs(policy.identity_evidence(
            "1Stanford University", ["stanford university"]), True)
        self.assertIs(policy.identity_evidence(
            "National Institutes of Health, Bethesda", ["national institute health"]),
            True)

    def test_publisher_mapped_unit_is_undecided(self):
        self.assertIsNone(policy.identity_evidence(
            "Haas School of Business", ["university california berkeley"]))


class WikipediaNames(unittest.TestCase):
    def test_disambiguator(self):
        self.assertEqual(policy.display_title("Mila (research institute)"), "Mila")
        self.assertEqual(policy.display_title(
            "Hong Kong University of Science and Technology (Guangzhou)"),
            "Hong Kong University of Science and Technology (Guangzhou)")

    def test_page_url(self):
        self.assertEqual(policy.wikipedia_page(
            "https://de.wikipedia.org/wiki/Technische_Universit%C3%A4t_M%C3%BCnchen"),
            ("de", "Technische Universität München"))
        self.assertEqual(policy.wikipedia_page("https://www.example.org"), ("", ""))

    def test_official_english_name_beats_wikipedia_short_title(self):
        names = policy.Names(FakeIndex(ORGS), TITLES, bib.is_local_language_institution)
        self.assertEqual(names.name_for("r:gt"),
                         ("Georgia Institute of Technology", "ror"))
        self.assertEqual(names.name_for("r:ub"), ("University of Barcelona", "ror"))
        self.assertEqual(names.name_for("r:ibm"), ("IBM", "ror"))

    def test_native_only_ror_name_uses_english_wikipedia_title(self):
        names = policy.Names(FakeIndex(ORGS), TITLES, bib.is_local_language_institution)
        self.assertEqual(names.name_for("r:lmu"), ("LMU Munich", "wikipedia"))

    def test_names_require_the_local_language_test(self):
        with self.assertRaises(ValueError):
            policy.Names(FakeIndex(ORGS), TITLES)

    def test_no_article_falls_back_to_ror_without_country_suffix(self):
        names = policy.Names(FakeIndex(ORGS), TITLES, bib.is_local_language_institution)
        self.assertEqual(names.name_for("r:interaction"), ("InterAction", "ror"))
        self.assertEqual(policy.ror_display(
            {"display": "Meta (Israel)", "country_name": "Israel"}), "Meta")


def _db():
    conn = sqlite3.connect(":memory:")
    conn.executescript(bib.SCHEMA)
    return conn


def _paper(conn, pid):
    conn.execute("INSERT INTO papers (paper_id, slug, title, review_dir) "
                 "VALUES (?,?,?,?)", (pid, f"{pid}_paper", "T", f"docs/papers/{pid}"))


def _inst(conn, iid, name, ror="", country="", parent="", source="ror"):
    conn.execute("INSERT INTO institutions (institution_id, institution_name, "
                 "normalized_name, country_name_en, ror_id, parent_name, name_source, "
                 "source) VALUES (?,?,?,?,?,?,?,?)",
                 (iid, name, bib.norm(name), country, ror, parent, source, "test"))


def _link(conn, pid, iid, raw, source="scopus+pdf"):
    conn.execute("INSERT INTO paper_institutions VALUES (?,?,?,?,?)",
                 (pid, iid, raw, "", source))


class ApplyPass(unittest.TestCase):
    def run_policy(self, conn, corrections=(), texts=None):
        texts = texts or {}
        return policy.apply(conn, COUNTRY_OF, bib.is_local_language_institution,
                            texts.get, index=FakeIndex(ORGS), titles=TITLES,
                            corrections=list(corrections))

    def test_lookup_link_needs_the_paper_to_name_the_institution(self):
        conn = _db()
        for pid in (1, 2, 3):
            _paper(conn, pid)
        _inst(conn, 10, "Korea Institute of Science and Technology", "r:kist")
        _inst(conn, 11, "University of Barcelona", "r:ub")
        for pid in (1, 2, 3):
            _link(conn, pid, 10, "Korea Institute of Science and Technology", "openalex")
            _link(conn, pid, 11, "University of Barcelona", "openalex")
        result = self.run_policy(conn, texts={
            # A byline marker glued to the name still names it.
            1: "Jane Doe1\n1Korea Institute of Science and Technology, Seoul",
            # The stored DOI was a cited work's: neither institution appears.
            2: "Anonymous authors\nAbstract ...",
        })
        self.assertEqual(result["lookup_links_unconfirmed"], 3)
        self.assertEqual(self.names(conn, 1),
                         ["Korea Institute of Science and Technology"])
        self.assertEqual(self.names(conn, 2), [])
        # No text to check against: the links stand.
        self.assertEqual(self.names(conn, 3), [
            "Korea Institute of Science and Technology", "University of Barcelona"])

    def test_relink_rule_confirms_a_lookup_link_the_text_spells_differently(self):
        conn = _db()
        _paper(conn, 1)
        _inst(conn, 10, "University of Barcelona", "r:ub")
        _link(conn, 1, 10, "University of Barcelona", "openalex")
        rule = {"id": "ub-faculty", "action": "relink",
                "match": {"raw_contains": "Facultat de Biologia"},
                "to": {"ror_id": "r:ub"}, "reason": "faculty of UB"}
        result = self.run_policy(conn, corrections=[rule], texts={
            1: "1 Facultat de Biologia, Barcelona"})
        self.assertEqual(result["lookup_links_unconfirmed"], 0)
        self.assertEqual(self.names(conn, 1), ["University of Barcelona"])
        # A second pass keeps it too.
        self.assertEqual(self.run_policy(conn, corrections=[rule], texts={
            1: "1 Facultat de Biologia, Barcelona"})["lookup_links_unconfirmed"], 0)

    def test_page_sourced_links_are_not_checked_against_text(self):
        conn = _db()
        _paper(conn, 1)
        _inst(conn, 10, "University of Barcelona", "r:ub")
        _link(conn, 1, 10, "University of Barcelona, Barcelona, Spain")
        self.run_policy(conn, texts={1: "no institution printed"})
        self.assertEqual(self.names(conn, 1), ["University of Barcelona"])

    def test_lookup_umbrella_beside_its_member_is_dropped(self):
        conn = _db()
        _paper(conn, 1)
        _inst(conn, 10, "IBM (United States)", "r:ibm", source="openalex")
        _inst(conn, 11, "IBM Research - Zurich", "r:ibm-zrl",
              parent="IBM (United States)")
        conn.execute("UPDATE institutions SET parent_ror_id='r:ibm' "
                     "WHERE institution_id=11")
        _link(conn, 1, 10, "IBM (United States)", "openalex")
        _link(conn, 1, 11, "IBM Research Europe, Rüschlikon, Switzerland")
        result = self.run_policy(conn, texts={
            1: "IBM Research Europe, Rüschlikon, Switzerland; IBM (United States)"})
        self.assertEqual(result["redundant_umbrella_links"], 1)
        self.assertEqual(self.names(conn, 1), ["IBM Research - Zurich"])
        parent, = conn.execute("SELECT parent_name FROM institutions "
                               "WHERE ror_id='r:ibm-zrl'").fetchone()
        self.assertEqual(parent, "IBM")

    def names(self, conn, pid):
        return sorted(n for (n,) in conn.execute(
            "SELECT i.institution_name FROM paper_institutions pi JOIN institutions i "
            "USING(institution_id) WHERE pi.paper_id=?", (pid,)))

    def test_watermark_link_is_dropped_and_markers_cleaned(self):
        conn = _db()
        for pid in (1, 2):
            _paper(conn, pid)
        _inst(conn, 10, "Korea Institute of Science and Technology", "r:kist")
        _link(conn, 1, 10, "2Korea Institute of Science and Technology (KIST), "
                           "Seoul, Re- public of Korea")
        _link(conn, 2, 10, "40M citation data. Authorized licensed use limited to: "
                           "Korea Institute of Science and Technology. Downloaded on")
        self.run_policy(conn)
        self.assertEqual(self.names(conn, 1),
                         ["Korea Institute of Science and Technology"])
        self.assertEqual(self.names(conn, 2), [])
        raw, = conn.execute("SELECT raw_name FROM paper_institutions").fetchone()
        self.assertEqual(raw, "Korea Institute of Science and Technology (KIST), "
                              "Seoul, Republic of Korea")
        city, country = conn.execute("SELECT city_name, country_name_en FROM "
                                     "institutions").fetchone()
        self.assertEqual((city, country), ("Seoul", "South Korea"))

    def test_same_ror_rows_merge_under_the_wikipedia_name(self):
        conn = _db()
        _paper(conn, 1)
        _paper(conn, 2)
        _inst(conn, 10, "Universitat de Barcelona", "r:ub", source="openalex")
        _inst(conn, 11, "University of Barcelona", "r:ub")
        _link(conn, 1, 10, "Universitat de Barcelona")
        _link(conn, 2, 11, "University of Barcelona, Barcelona, Spain")
        self.run_policy(conn)
        rows = conn.execute("SELECT institution_name, city_name, country_name_en "
                            "FROM institutions").fetchall()
        self.assertEqual(rows, [("University of Barcelona", "Barcelona", "Spain")])

    def test_country_subsidiaries_become_one_company(self):
        conn = _db()
        _paper(conn, 1)
        _paper(conn, 2)
        _inst(conn, 10, "Google (Ireland)", "r:google-ie", parent="Google")
        _inst(conn, 11, "Google (United States)", "r:google")
        _link(conn, 1, 10, "Google, Dublin")
        _link(conn, 2, 11, "Google Research, Mountain View")
        self.run_policy(conn)
        rows = conn.execute("SELECT institution_name, ror_id, parent_name "
                            "FROM institutions").fetchall()
        self.assertEqual(rows, [("Google", "r:google", "Google")])

    def test_umbrella_is_its_own_parent(self):
        conn = _db()
        _paper(conn, 1)
        _inst(conn, 10, "IBM (United States)", "r:ibm")
        _inst(conn, 11, "IBM Research - Zurich", "r:ibm-zrl",
              parent="IBM (United States)")
        conn.execute("UPDATE institutions SET parent_ror_id='r:ibm' "
                     "WHERE institution_id=11")
        _link(conn, 1, 10, "IBM (United States)")
        _link(conn, 1, 11, "IBM Research Europe, Rüschlikon, Switzerland")
        self.run_policy(conn)
        rows = conn.execute("SELECT institution_name, parent_name FROM institutions "
                            "ORDER BY institution_name").fetchall()
        self.assertEqual(rows, [("IBM", "IBM"), ("IBM Research - Zurich", "IBM")])
        # Stable on a second pass.
        self.run_policy(conn)
        self.assertEqual(conn.execute("SELECT institution_name, parent_name FROM "
                                      "institutions ORDER BY institution_name")
                         .fetchall(), rows)

    def test_institution_without_umbrella_is_its_own_parent(self):
        conn = _db()
        _paper(conn, 1)
        _inst(conn, 10, "Stanford University", "r:stanford")
        _link(conn, 1, 10, "Stanford University")
        self.run_policy(conn)
        self.assertEqual(conn.execute("SELECT parent_name FROM institutions")
                         .fetchone()[0], "Stanford University")

    def test_generic_phrase_link_is_dropped(self):
        conn = _db()
        _paper(conn, 1)
        _inst(conn, 10, "InterAction", "r:interaction")
        _link(conn, 1, 10, "3 Layer Interaction . . . 58")
        self.run_policy(conn)
        self.assertEqual(self.names(conn, 1), [])

    def test_school_folds_into_its_university(self):
        conn = _db()
        _paper(conn, 1)
        _inst(conn, 10, "Harvard Kennedy School", "r:hks")
        _link(conn, 1, 10, "John F. Kennedy School of Government")
        self.run_policy(conn)
        self.assertEqual(self.names(conn, 1), ["Harvard University"])

    def test_withdrawn_school_record_folds_into_named_university(self):
        index = FakeIndex(ORGS + [
            {"ror_id": "r:jhu", "display": "Johns Hopkins University",
             "country_name": "United States", "org_types": "education"},
            {"ror_id": "r:jhusom", "display": "Johns Hopkins University School of Medicine",
             "country_name": "United States", "org_types": "other",
             "status": "withdrawn"},
            {"ror_id": "r:hamamatsu-som", "display": "Hamamatsu University School of Medicine",
             "country_name": "Japan", "org_types": "education"},
            {"ror_id": "r:kcl", "display": "King's College London",
             "country_name": "United Kingdom", "org_types": "education",
             "parent_id": "r:uol"},
            {"ror_id": "r:uol", "display": "University of London",
             "country_name": "United Kingdom", "org_types": "education"}])
        self.assertEqual(policy._university_of_unit(
            "Johns Hopkins University School of Medicine", "r:jhusom", "", "", index),
            "r:jhu")
        # An active school with no parent is a university of its own.
        self.assertEqual(policy._university_of_unit(
            "Hamamatsu University School of Medicine", "r:hamamatsu-som", "", "",
            index), "")
        # A college inside a federation is an institution of its own.
        self.assertEqual(policy._university_of_unit(
            "King's College London", "r:kcl", "", "", index), "")

    def test_corrections_relink_and_survive_a_second_pass(self):
        conn = _db()
        _paper(conn, 1)
        _inst(conn, 10, "The Robotics Institute", source="")
        _link(conn, 1, 10, "are with the Robotics Institute, School")
        rule = {"id": "ri", "action": "relink",
                "match": {"raw_contains": "Robotics Institute"},
                "to": {"ror_id": "r:cmu"}, "reason": "unit of CMU"}
        first = self.run_policy(conn, [rule])
        self.assertEqual(first["link_corrections"], {"ri": 1})
        self.assertEqual(self.names(conn, 1), ["Carnegie Mellon University"])
        second = self.run_policy(conn, [rule])
        self.assertEqual(second["link_corrections"], {})
        self.assertEqual(self.names(conn, 1), ["Carnegie Mellon University"])

    def test_set_correction_has_the_last_word(self):
        conn = _db()
        _paper(conn, 1)
        _inst(conn, 10, "Stanford University", "r:stanford")
        _link(conn, 1, 10, "Stanford University")
        self.run_policy(conn, [{"id": "c", "action": "set",
                                "match": {"ror_id": "r:stanford"},
                                "to": {"city": "Palo Alto"}, "reason": "test"}])
        self.assertEqual(conn.execute("SELECT city_name FROM institutions")
                         .fetchone()[0], "Palo Alto")


class CorrectionsFile(unittest.TestCase):
    def test_shipped_file_is_valid(self):
        rules = policy.load_corrections()
        self.assertTrue(rules)
        self.assertTrue(all(r["reason"] for r in rules))

    def test_rule_without_reason_is_rejected(self):
        import json
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "c.json"
            path.write_text(json.dumps({"rules": [{"id": "x", "action": "drop",
                                                   "match": {"ror_id": "r"}}]}))
            with self.assertRaises(ValueError):
                policy.load_corrections(path)


if __name__ == "__main__":
    unittest.main()
