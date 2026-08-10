"""ROR-backed institution normalisation contract.

Before this layer the DB identified an institution by whatever string a PDF
printed: "Stanford", "Stanford University" and "Stanford Engineering" were three
institutions, "University of Chinese Academy of Sciences." (trailing period) a
fourth, and the 106 Max Planck institutes never rolled up to Max Planck.

Every literal below is a string that actually reached
`.cache/bibliography.sqlite3`, or a rule the operator set:

* multilingual and acronym variants collapse onto one record;
* `parent_name` is the *outermost* eligible research umbrella;
* administrative organs (ministries, governments, DOE-style offices, VA
  networks) are never an institution or a parent;
* multi-campus public university systems are not parents — their campuses are
  independent research performers;
* co-occurrence on one affiliation line is not a hierarchy.

Tests are offline: no test may call Zenodo or Wikipedia.
"""
import sqlite3
import unittest
from pathlib import Path

from pipeline.lib import affiliation_groups, ror_index

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / ".cache" / "bibliography.sqlite3"
INDEX_READY = ror_index.INDEX_PATH.exists()

requires_index = unittest.skipUnless(
    INDEX_READY,
    "ROR index missing — run python pipeline/setup_affiliation_sources.py")


class NormalizeTests(unittest.TestCase):
    """Key building is language-, punctuation- and plural-insensitive."""

    def test_plurals_fold(self):
        self.assertEqual(
            ror_index.normalize("University of Chinese Academy of Sciences"),
            ror_index.normalize("University of Chinese Academy of Science"))

    def test_articles_and_diacritics_fold(self):
        self.assertEqual(ror_index.normalize("The University of Melbourne"),
                         ror_index.normalize("University of Melbourne"))
        self.assertEqual(ror_index.normalize("ETH Zürich"),
                         ror_index.normalize("ETH Zurich"))

    def test_trailing_acronym_yields_an_extra_key(self):
        keys = ror_index.alias_keys(
            "Fraunhofer Institute for Solar Energy Systems (ISE)")
        self.assertIn("fraunhofer institute solar energy system", keys)
        keys = ror_index.alias_keys(
            "Fraunhofer Institute for Mechanics of Materials IWM")
        self.assertIn("fraunhofer institute mechanic material", keys)


class EligibilityRuleTests(unittest.TestCase):
    """Who may be a parent group, decided by name because ROR types cannot."""

    ADMINISTRATIVE = [
        "Government of the United States of America",
        "Federal Government of Brazil",
        "State Council of the People's Republic of China",
        "Ministry of Education, Culture, Sports, Science and Technology",
        "Board of the Swiss Federal Institutes of Technology",
        "Office of Science",
        "United States Department of Defense",
        "United States Department of Veterans Affairs",
        "Department of Atomic Energy",
        "Department of Mathematical Sciences",
        "VA Heartland Network",
        "VA Healthcare-VISN 4",
    ]
    # All four are tagged `funder,government` in ROR, exactly like the bodies
    # above; only the name separates them.
    RESEARCH_UMBRELLAS = [
        "Chinese Academy of Sciences",
        "Centre National de la Recherche Scientifique",
        "Helmholtz Association of German Research Centres",
        "Max Planck Society",
        "Fraunhofer Society",
        "Leibniz Association",
        "Research Organization of Information and Systems",
        "National Institutes of Natural Sciences",
    ]
    UNIVERSITY_SYSTEMS = [
        "University of California System",
        "The University of Texas System",
        "State University System of Florida",
        "University System of Georgia",
        "State University of New York",
        "Utah System of Higher Education",
        "Pennsylvania State System of Higher Education",
        "Arizona's Public Universities",
    ]

    def test_administrative_organs_are_rejected(self):
        missed = [n for n in self.ADMINISTRATIVE
                  if not ror_index.ADMINISTRATIVE_BODY.search(n)]
        self.assertEqual(missed, [])

    def test_research_umbrellas_are_not_administrative(self):
        wrong = [n for n in self.RESEARCH_UMBRELLAS
                 if ror_index.ADMINISTRATIVE_BODY.search(n)
                 or ror_index.UNIVERSITY_SYSTEM.search(n)]
        self.assertEqual(wrong, [])

    def test_university_systems_are_rejected(self):
        missed = [n for n in self.UNIVERSITY_SYSTEMS
                  if not ror_index.UNIVERSITY_SYSTEM.search(n)]
        self.assertEqual(missed, [])

    def test_a_real_va_medical_centre_is_not_administrative(self):
        self.assertFalse(ror_index.ADMINISTRATIVE_BODY.search(
            "VA Palo Alto Health Care System"))

    def test_sub_units_are_rejected_by_the_wikipedia_fallback(self):
        for name in ("School of Computer Science", "School of Mathematics",
                     "Guanghua School of Management",
                     "Paul G. Allen School of Computer Science and Engineering",
                     "School of Public Policy and Administration"):
            with self.subTest(name=name):
                self.assertTrue(ror_index.SUBUNIT_NAME.search(name))

    def test_real_institutes_pass_the_sub_unit_test(self):
        for name in ("Institute of Automation", "Institute of Physics",
                     "Shenzhen Institutes of Advanced Technology",
                     "Max Planck Institute for Intelligent Systems"):
            with self.subTest(name=name):
                self.assertIsNone(ror_index.SUBUNIT_NAME.search(name))


@requires_index
class ResolutionTests(unittest.TestCase):
    """Lookups against the projected ROR index."""

    @classmethod
    def setUpClass(cls):
        cls.index = ror_index.RorIndex()

    @classmethod
    def tearDownClass(cls):
        cls.index.close()

    def display(self, name, country=""):
        hit = self.index.resolve(name, country)
        return hit["display"] if hit else ""

    def test_multilingual_variants_collapse(self):
        cases = [
            ("Universität Wien", "University of Vienna"),
            ("清华大学", "Tsinghua University"),
            ("北京大学", "Peking University"),
            ("中国科学院", "Chinese Academy of Sciences"),
            ("서울대학교", "Seoul National University"),
            ("東京大学", "The University of Tokyo"),
            ("Fritz-Haber-Institut der Max-Planck-Gesellschaft",
             "Fritz Haber Institute of the Max Planck Society"),
        ]
        for written, expected in cases:
            with self.subTest(written=written):
                self.assertEqual(self.display(written), expected)

    def test_english_label_beats_native_ror_display(self):
        """ROR displays this record in German; the DB stores English."""
        self.assertEqual(self.display("Technische Universität Darmstadt"),
                         "Technical University of Darmstadt")

    def test_unique_acronyms_resolve(self):
        for acronym in ("EPFL", "KAIST", "INRIA"):
            with self.subTest(acronym=acronym):
                self.assertTrue(self.display(acronym))

    def test_ambiguous_acronyms_need_a_country(self):
        """"CNRS" is claimed by France, Lebanon and Canada."""
        self.assertEqual(self.display("CNRS"), "")
        # The English label wins over ROR's French display name.
        self.assertEqual(self.display("CNRS", "France"),
                         "French National Centre for Scientific Research")

    def test_trailing_acronym_still_matches(self):
        self.assertTrue(self.display(
            "Fraunhofer Institute for Solar Energy Systems (ISE)"))


@requires_index
class ParentGroupTests(unittest.TestCase):
    """`parent_name` is the outermost eligible umbrella."""

    @classmethod
    def setUpClass(cls):
        cls.index = ror_index.RorIndex()

    @classmethod
    def tearDownClass(cls):
        cls.index.close()

    def resolve(self, name, country=""):
        return self.index.resolve_affiliation(
            name, country, allow_remote=False)

    def test_max_planck_institutes_roll_up(self):
        out = self.resolve("Max Planck Institute for Intelligent Systems",
                           "Germany")
        self.assertEqual(out["parent"], "Max Planck Society")

    def test_helmholtz_centres_roll_up_to_the_association(self):
        """Helmholtz Munich and GSI are institutions, not buckets of their own."""
        for name in ("Helmholtz Munich", "Institute of Computational Biology",
                     "Helmholtz Institute Jena"):
            with self.subTest(name=name):
                out = self.resolve(name, "Germany")
                self.assertEqual(
                    out["parent"],
                    "Helmholtz Association of German Research Centres")

    def test_named_institute_under_an_umbrella(self):
        out = self.resolve(
            "Institute of Automation, Chinese Academy of Sciences", "China")
        self.assertEqual(out["institution"], "Institute of Automation")
        self.assertEqual(out["parent"], "Chinese Academy of Sciences")

    def test_department_prefix_resolves_to_the_institution(self):
        out = self.resolve("Department of Computer Science, ETH Zurich",
                           "Switzerland")
        self.assertEqual(out["institution"], "ETH Zurich")

    def test_ministry_is_never_the_institution(self):
        out = self.resolve(
            "Key Laboratory of Machine Perception, Ministry of Education, "
            "Peking University", "China")
        self.assertEqual(out["institution"], "Peking University")

    def test_author_byline_is_dropped(self):
        for name, expected in (("Yong Li Tsinghua University",
                                "Tsinghua University"),
                               ("Robert Jakob ETH Zürich", "ETH Zurich")):
            with self.subTest(name=name):
                self.assertEqual(self.resolve(name)["institution"], expected)

    def test_co_occurrence_is_not_a_hierarchy(self):
        """A multi-affiliation line made the University of Amsterdam MIT's parent."""
        out = self.resolve(
            "Massachusetts Institute of Technology, University of Amsterdam")
        self.assertNotEqual(out["parent"], "University of Amsterdam")

    def test_university_system_is_not_offered_as_a_parent(self):
        hit = self.index.resolve("University of California, Berkeley",
                                 "United States")
        self.assertIsNotNone(hit)
        parent = self.index.eligible_parent(hit["ror_id"])
        self.assertIsNone(parent, f"got {parent and parent['display']}")


class CuratedGroupTests(unittest.TestCase):
    """The operator-curated Scopus table fills gaps ROR leaves."""

    def test_real_hierarchies_are_kept(self):
        for name, group in (("Harvard Medical School", "Harvard University"),
                            ("Dalian Institute of Chemical Physics",
                             "Chinese Academy of Sciences"),
                            ("Indian Institute of Technology Madras",
                             "Indian Institutes of Technology")):
            with self.subTest(name=name):
                self.assertEqual(affiliation_groups.group_for(name), group)

    def test_spelling_variants_are_not_hierarchies(self):
        """"ETH Zurich" → "ETH Zürich" is a variant; it must not become a parent."""
        for name in ("ETH Zurich", "The University of Melbourne",
                     "University of Edinburgh"):
            with self.subTest(name=name):
                group = affiliation_groups.group_for(name)
                self.assertNotEqual(ror_index.normalize(group or name),
                                    ror_index.normalize(name)) if group else None
                if group:
                    self.assertNotEqual(ror_index.normalize(group),
                                        ror_index.normalize(name))

    def test_brand_rollup_covers_ror_gaps(self):
        """ROR records no parent for Helmholtz Institute Ulm."""
        self.assertEqual(
            affiliation_groups.group_for("Helmholtz Institute Ulm"),
            "Helmholtz Association of German Research Centres")

    def test_transitive_roll_up(self):
        """CAS institutes were filed under UCAS, which ROR gives no parent."""
        self.assertEqual(
            affiliation_groups.roll_up("University of Chinese Academy of Sciences"),
            "Chinese Academy of Sciences")

    def test_roll_up_terminates(self):
        self.assertEqual(
            affiliation_groups.roll_up("Chinese Academy of Sciences"),
            "Chinese Academy of Sciences")


@unittest.skipUnless(DB.exists(), ".cache/bibliography.sqlite3 없음")
class ShippedDatabaseTests(unittest.TestCase):
    """Invariants over the real DB — the data, not the machinery."""

    @classmethod
    def setUpClass(cls):
        cls.conn = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
        cls.columns = {row[1] for row in cls.conn.execute(
            "PRAGMA table_info(institutions)")}

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()

    def scalar(self, sql):
        return self.conn.execute(sql).fetchone()[0]

    def test_normalisation_columns_exist(self):
        self.assertTrue(
            {"ror_id", "parent_name", "parent_ror_id", "name_source"}
            <= self.columns)

    def test_no_ineligible_parent_groups(self):
        parents = [p for (p,) in self.conn.execute(
            "SELECT DISTINCT parent_name FROM institutions WHERE parent_name<>''")]
        bad = [p for p in parents
               if ror_index.ADMINISTRATIVE_BODY.search(p)
               or ror_index.UNIVERSITY_SYSTEM.search(p)]
        self.assertEqual(bad, [])

    def test_no_institution_is_its_own_parent(self):
        self.assertEqual(self.scalar(
            "SELECT COUNT(*) FROM institutions "
            "WHERE parent_name<>'' AND normalized_name="
            "  (SELECT normalized_name FROM institutions x"
            "   WHERE x.institution_id=institutions.institution_id)"
            " AND LOWER(parent_name)=LOWER(institution_name)"), 0)

    def test_no_school_or_department_shaped_institution_names(self):
        """A school or department is a sub-unit, never an institution.

        Only the strongly diagnostic forms are asserted. `SUBUNIT_NAME` is
        deliberately over-broad for the Wikipedia fallback, where a rejected
        candidate falls back safely to the umbrella, so it also flags real
        research centres ("Center for Information Technology Policy").
        """
        bad = [n for (n,) in self.conn.execute(
            "SELECT institution_name FROM institutions "
            "WHERE institution_name LIKE 'School of%'"
            "   OR institution_name LIKE 'Department of%'"
            "   OR institution_name LIKE 'Faculty of%'"
            "   OR institution_name LIKE 'Division of%'")]
        self.assertEqual(bad, [])

    def test_ror_coverage_does_not_regress(self):
        total = self.scalar("SELECT COUNT(*) FROM institutions")
        resolved = self.scalar(
            "SELECT COUNT(*) FROM institutions WHERE ror_id<>''")
        self.assertGreater(resolved / total, 0.60,
                           f"ROR coverage fell to {resolved}/{total}")

    def test_helmholtz_groups_into_one_bucket(self):
        buckets = [p for (p,) in self.conn.execute(
            "SELECT DISTINCT parent_name FROM institutions "
            "WHERE parent_name LIKE '%Helmholtz%'")]
        self.assertEqual(
            buckets, ["Helmholtz Association of German Research Centres"])


if __name__ == "__main__":
    unittest.main()
