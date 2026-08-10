"""ROR-backed institution normalisation: one name, one country, one parent group.

The bibliography DB identified institutions by whatever string a PDF happened to
print, so "Stanford", "Stanford University", "Stanford Engineering" and
"Stanford Institute for Human-Centered Artificial Intelligence" were four
institutions, "University of Chinese Academy of Sciences." (trailing period) was
its own fifth, and the 106 Max Planck institutes never rolled up to Max Planck.

ROR (Research Organization Registry) is the authority for all three problems at
once. Every record carries

* ``names`` — the display name plus every label, alias and acronym, each tagged
  with a language, which is how "Universität Wien"/"University of Vienna" and
  "Centre National de la Recherche Scientifique"/"CNRS" collapse to one entity;
* ``relationships`` — typed ``parent`` edges, which is how Fritz Haber Institute
  rolls up to Max Planck Society;
* ``locations`` — GeoNames country, which beats parsing the country out of the
  affiliation string.

This module turns the ~305 MB ROR dump into a queryable SQLite index once, then
answers lookups from it. The dump is never loaded at build time.
"""
from __future__ import annotations

import json
import re
import sqlite3
import threading
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ROR_DIR = ROOT / ".cache" / "ror"
INDEX_PATH = ROR_DIR / "ror_index.sqlite3"

SCHEMA = """
CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE orgs (
  ror_id TEXT PRIMARY KEY,
  display TEXT NOT NULL,
  country_name TEXT NOT NULL DEFAULT '',
  country_code TEXT NOT NULL DEFAULT '',
  org_types TEXT NOT NULL DEFAULT '',
  status TEXT NOT NULL DEFAULT '',
  parent_id TEXT NOT NULL DEFAULT '');
CREATE TABLE names (
  normalized TEXT NOT NULL,
  ror_id TEXT NOT NULL REFERENCES orgs(ror_id),
  name_type TEXT NOT NULL,
  lang TEXT NOT NULL DEFAULT '',
  PRIMARY KEY (normalized, ror_id, name_type));
CREATE INDEX idx_names_normalized ON names(normalized);
"""

# An acronym is only trustworthy when it is globally unique; "MIT" and "CAS" are
# claimed by dozens of organisations.
NAME_TYPE_RANK = {"ror_display": 0, "label": 1, "alias": 2, "acronym": 3}

_PUNCT = re.compile(r"[^\w\s]", re.UNICODE)
_SPACE = re.compile(r"\s+")
# Leading sub-unit boilerplate: the part before the comma is a department, not
# the institution ("Department of Computer Science, ETH Zurich").
_STOPWORDS = {
    "the", "of", "for", "and", "at", "in", "de", "der", "die", "das", "du",
    "la", "le", "les", "el", "los", "las", "e", "y", "et", "und", "van", "von",
    "dei", "del", "della", "di", "da", "dos", "das_pt",
}

# A parent group must be a research organisation. Administrative organs — a
# ministry, a national government, the board that administers a university
# domain — announce themselves by name, and ROR types cannot separate them from
# genuine umbrellas (CAS, CNRS, Helmholtz and the Swiss federal board are all
# tagged `funder,government`).
ADMINISTRATIVE_BODY = re.compile(
    r"(?i)^(?:(?:federal |national |state )?government of|government\b|"
    r"ministry\b|ministry of|minist[eè]re|ministerio|"
    r"minist[eé]rio|bundesministerium|federal ministry|state council|"
    r"board of|secretariat|executive office|office of\b|parliament|congress|"
    r"national assembly|department of\b|u\.?s\.? department\b|"
    r"united states department\b|european commission|"
    # VA regional networks are administrative catchments, not research groups.
    # ("VA Palo Alto Health Care System" is a real institution and stays.)
    r"va\s+\S*\s*(?:network|visn)\b)\b")

# A multi-campus public university system is a funding and governance layer, not
# a research organisation: its campuses are independent research performers with
# their own faculties. Berkeley is not a sub-unit of "University of California
# System" the way the Fritz Haber Institute is a sub-unit of Max Planck.
UNIVERSITY_SYSTEM = re.compile(
    r"(?i)(?:\bsystem$|\buniversity system\b|\bsystem of higher education\b|"
    r"\bsystem of \w+$|public universities$|^state university of new york$|"
    r"^arizona's public universities$)")

# Below this an organisation is a site or a lab, not a group worth rolling up to.
MIN_UMBRELLA_CHILDREN = 3

# A school, department or faculty is a sub-unit, never the institution. Without
# this the Wikipedia fallback promoted "School of Computer Science", "School of
# Mathematics" and "Guanghua School of Management" to institutions, because
# Wikipedia does describe them and the extract says "school".
# Used only by the Wikipedia fallback, where over-matching is safe: a rejected
# candidate falls back to the umbrella, which is the correct answer for a
# sub-unit anyway. ROR-resolved names never reach this test.
SUBUNIT_NAME = re.compile(
    r"(?i)\b(?:school|department|dept\.?|faculty|division|graduate school|"
    r"programme?|chair|section)\s+of\b"
    r"|^(?:the\s+)?(?:school|department|faculty|division|centre|center|"
    r"laborator\w+|group|unit)\b")

# A single-token comma segment is a place, not an organisation: an affiliation
# ends "…, Cambridge, MA, USA" and "…, Edinburgh, UK". Once unique acronyms
# became acceptable evidence those tokens started matching real records — "UK"
# found an organisation whose acronym is UK, "Cambridge" found Cambridge IVF —
# and 52 and 51 papers were filed under them. Multi-token segments are safe
# ("ETH Zurich", "Broad Institute of MIT and Harvard"); the cost is a bare
# one-word company name, which arrives as a whole string and resolves directly.
def is_place_only_segment(segment: str) -> bool:
    return len(normalize(segment).split()) < 2

WIKIPEDIA_CACHE = ROR_DIR / "wikipedia_organisations.json"
_WIKIPEDIA_API = "https://en.wikipedia.org/w/api.php"
# Wikipedia's own words for "this is an organisation".
_ORGANISATION_CUES = re.compile(
    r"(?i)\b(?:institute|institution|university|college|academy|laborator|"
    r"research (?:cent|organi|institut)|centre|center|school|hospital|"
    r"foundation|society|association|agency|company|corporation|"
    r"is a (?:public|private|national|state|research|German|Chinese|French))\b")
_wikipedia_cache: dict[str, bool] | None = None


def _outcome(institution: str, parent: str, *, ror_id: str = "",
             parent_ror_id: str = "", country_name: str = "",
             evidence: str = "") -> dict:
    return {"institution": institution, "parent": parent, "ror_id": ror_id,
            "parent_ror_id": parent_ror_id, "country_name": country_name,
            "evidence": evidence}


def _load_wikipedia_cache() -> dict[str, bool]:
    global _wikipedia_cache
    if _wikipedia_cache is None:
        try:
            _wikipedia_cache = json.loads(
                WIKIPEDIA_CACHE.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            _wikipedia_cache = {}
    return _wikipedia_cache


def _save_wikipedia_cache() -> None:
    if _wikipedia_cache is None:
        return
    WIKIPEDIA_CACHE.parent.mkdir(parents=True, exist_ok=True)
    WIKIPEDIA_CACHE.write_text(
        json.dumps(_wikipedia_cache, ensure_ascii=False, sort_keys=True,
                   indent=0), encoding="utf-8")


def wikipedia_confirms_organisation(name: str,
                                    allow_remote: bool = True) -> bool:
    """Does Wikipedia describe this string as an organisation?

    The fallback for the case ROR cannot answer: an institute that sits under a
    known umbrella but has no ROR record of its own. Without this the parser
    would promote any comma-delimited fragment to an institution name, which is
    exactly the failure this whole pass exists to remove. Results are cached, so
    a rebuild makes no repeat calls.
    """
    key = re.sub(r"\s+", " ", str(name or "")).strip()
    if len(key) < 6:
        return False
    cache = _load_wikipedia_cache()
    if key in cache:
        return cache[key]
    if not allow_remote:
        return False
    verdict = False
    try:
        import urllib.parse
        import urllib.request
        query = urllib.parse.urlencode({
            "action": "query", "format": "json", "prop": "extracts",
            "exintro": "1", "explaintext": "1", "redirects": "1",
            "titles": key})
        request = urllib.request.Request(
            f"{_WIKIPEDIA_API}?{query}",
            headers={"User-Agent": "paper-curation/1.0 (affiliation check)"})
        with urllib.request.urlopen(request, timeout=15) as response:
            payload = json.loads(response.read().decode("utf-8"))
        for page in (payload.get("query", {}).get("pages") or {}).values():
            if "missing" in page:
                continue
            extract = page.get("extract") or ""
            if _ORGANISATION_CUES.search(extract[:600]):
                verdict = True
                break
    except Exception:
        verdict = False
    cache[key] = verdict
    _save_wikipedia_cache()
    return verdict


# A leading digit run glued to a word is the superscript that ties an author to
# an affiliation ("1Division of Physics", "2Princeton University", "26University
# of Cambridge"), not part of the name. Institution names do carry digits — "L3S
# Research Center", "A5 Genetics Ltd", "Bio21 Institute", "LIP6", "Space Delta 9"
# — but never as a leading run welded onto a following word, so requiring a
# following run of two letters or more leaves them alone: "3M" keeps its digit
# because only one letter follows, while "1UC Berkeley" loses its marker.
MARKER_DIGITS = re.compile(r"(?<![A-Za-z0-9])\d{1,2}(?=[A-Za-z]{2})")


def strip_marker_digits(value: str) -> str:
    return MARKER_DIGITS.sub("", str(value or ""))


def normalize(name: str) -> str:
    """Language- and punctuation-insensitive key for one institution name.

    Plurals are folded because ROR and PDFs disagree freely on them: the corpus
    held both "University of Chinese Academy of Sciences" and "…of Science", and
    only the first matched.
    """
    value = unicodedata.normalize("NFKD", strip_marker_digits(name))
    value = "".join(c for c in value if not unicodedata.combining(c))
    value = _PUNCT.sub(" ", value).casefold()
    tokens = []
    for token in _SPACE.split(value):
        if not token or token in _STOPWORDS:
            continue
        if len(token) > 4 and token.endswith("s") and not token.endswith("ss"):
            token = token[:-1]
        tokens.append(token)
    return " ".join(tokens)


# A trailing acronym is decoration, not identity: the curated table writes
# "Fraunhofer Institute for Solar Energy Systems (ISE)" and PDFs write
# "Fraunhofer Institute for Mechanics of Materials IWM" for organisations whose
# canonical names carry no acronym at all.
_TRAILING_ACRONYM = re.compile(r"\s*[\(\[]([A-Za-z]{2,8})[\)\]]\s*$")
# Legal form is not identity: "DeepMind Technologies Limited" is DeepMind, and
# "Google LLC" is Google. Stripped as an extra lookup key, never as the display.
LEGAL_SUFFIX = re.compile(
    r"(?i)[,\s]+(?:technologies?\s+)?(?:limited|ltd\.?|llc|l\.l\.c\.|inc\.?|"
    r"incorporated|corp\.?|corporation|company|co\.|gmbh|ag|a\.g\.|plc|"
    r"s\.?a\.?|b\.?v\.?|n\.?v\.?|pty|kk|k\.k\.)\s*$")
_BARE_ACRONYM_TAIL = re.compile(r"\s+([A-Z]{2,8})$")


def alias_keys(name: str) -> list[str]:
    """Normalised keys to try for one written name, most specific first."""
    raw = str(name or "").strip()
    variants = [raw]
    stripped = _TRAILING_ACRONYM.sub("", raw).strip()
    if stripped and stripped != raw:
        variants.append(stripped)
    bare = _BARE_ACRONYM_TAIL.sub("", variants[-1]).strip()
    if bare and bare != variants[-1]:
        variants.append(bare)
    for variant in list(variants):
        stripped_legal = LEGAL_SUFFIX.sub("", variant).strip(" ,")
        if stripped_legal and stripped_legal != variant:
            variants.append(stripped_legal)
    keys, seen = [], set()
    for variant in variants:
        key = normalize(variant)
        # A key that is only digits or a two-letter stub is not an identity.
        # Stripping the trailing acronym off "3 MIT" left the key "3", which
        # matched a ROR record and filed the affiliation under "Space Delta 3".
        if not key or key in seen or key.isdigit() or len(key) < 3:
            continue
        seen.add(key)
        keys.append(key)
    return keys


def latest_dump() -> Path | None:
    dumps = sorted(ROR_DIR.glob("v*-ror-data.json"))
    return dumps[-1] if dumps else None


def build_index(dump: Path | None = None, index: Path | None = None) -> dict:
    """Project the ROR dump into the lookup index. Run once per dump release."""
    dump = dump or latest_dump()
    if dump is None:
        raise SystemExit(
            "ROR dump not found. Download it into .cache/ror/:\n"
            "  curl -sL -o .cache/ror/ror.zip "
            "https://zenodo.org/api/records/21773148/files/"
            "v2.11-2026-08-03-ror-data.zip/content && "
            "unzip -o .cache/ror/ror.zip -d .cache/ror/")
    index = index or INDEX_PATH
    records = json.loads(dump.read_text(encoding="utf-8"))
    index.parent.mkdir(parents=True, exist_ok=True)
    if index.exists():
        index.unlink()
    conn = sqlite3.connect(index)
    conn.executescript(SCHEMA)
    org_rows, name_rows = [], []
    for record in records:
        ror_id = record["id"]
        # ROR's own display name is sometimes the native one ("Technische
        # Universität Darmstadt", "École Normale Supérieure - PSL"). The DB
        # stores English so institution names read consistently and the
        # local-language gate stays meaningful: the English label wins when the
        # record has one, and the native display is still indexed as a lookup key.
        display, english, labels = "", "", []
        for entry in record.get("names") or []:
            value = str(entry.get("value") or "").strip()
            if not value:
                continue
            types = entry.get("types") or []
            lang = entry.get("lang") or ""
            if "ror_display" in types:
                display = value
            if not english and lang == "en" and "label" in types:
                english = value
            for name_type in types:
                labels.append((value, name_type, lang))
        display = english or display
        if not display:
            continue
        location = (record.get("locations") or [{}])[0]
        geo = location.get("geonames_details") or {}
        parent = next(
            (r.get("id", "") for r in record.get("relationships") or []
             if r.get("type") == "parent"), "")
        org_rows.append((
            ror_id, display, geo.get("country_name") or "",
            geo.get("country_code") or "", ",".join(record.get("types") or []),
            record.get("status") or "", parent))
        seen = set()
        for value, name_type, lang in labels:
            # ROR disambiguates multinationals with a trailing country —
            # "Microsoft (United States)" — which keeps the bare company name
            # out of the index entirely. Index the stripped form too so the
            # headquarters rule below has all the siblings to choose from.
            for key in alias_keys(value) + alias_keys(
                    re.sub(r"\s*\([^)]*\)\s*$", "", value)):
                if (key, name_type) in seen:
                    continue
                seen.add((key, name_type))
                name_rows.append((key, ror_id, name_type, lang))
    conn.executemany("INSERT INTO orgs VALUES (?,?,?,?,?,?,?)", org_rows)
    conn.executemany("INSERT OR IGNORE INTO names VALUES (?,?,?,?)", name_rows)
    conn.executemany(
        "INSERT INTO meta VALUES (?,?)",
        [("dump", dump.name), ("orgs", str(len(org_rows))),
         ("names", str(len(name_rows)))])
    conn.commit()
    conn.execute("PRAGMA optimize")
    conn.close()
    return {"dump": dump.name, "orgs": len(org_rows), "names": len(name_rows),
            "index": str(index)}


class RorIndex:
    """Read-only lookups against the projected index."""

    def __init__(self, path: Path | None = None) -> None:
        self.path = path or INDEX_PATH
        # One connection per thread. The bibliography build caches a single
        # RorIndex at module level, and the review run's ingest thread reuses
        # it — SQLite refuses a connection created in another thread.
        self._local = threading.local()
        self._cache: dict[tuple[str, str], dict | None] = {}
        self._children: dict[str, int] = {}

    @property
    def available(self) -> bool:
        return self.path.exists()

    def _connect(self) -> sqlite3.Connection:
        conn = getattr(self._local, "conn", None)
        if conn is None:
            conn = sqlite3.connect(f"file:{self.path}?mode=ro", uri=True)
            self._local.conn = conn
        return conn

    def close(self) -> None:
        conn = getattr(self._local, "conn", None)
        if conn is not None:
            conn.close()
            self._local.conn = None

    def org(self, ror_id: str) -> dict | None:
        row = self._connect().execute(
            "SELECT ror_id, display, country_name, country_code, org_types,"
            " status, parent_id FROM orgs WHERE ror_id=?", (ror_id,)).fetchone()
        if not row:
            return None
        keys = ("ror_id", "display", "country_name", "country_code",
                "org_types", "status", "parent_id")
        return dict(zip(keys, row))

    def top_parent(self, ror_id: str) -> dict | None:
        """Walk `parent` edges to the outermost organisation.

        Fritz Haber Institute → Max Planck Society. Depth is bounded because ROR
        contains at least one cycle-shaped pair of mutual parents.
        """
        seen = {ror_id}
        current = self.org(ror_id)
        if current is None:
            return None
        for _ in range(8):
            parent_id = current.get("parent_id") or ""
            if not parent_id or parent_id in seen:
                break
            parent = self.org(parent_id)
            if parent is None:
                break
            seen.add(parent_id)
            current = parent
        return None if current["ror_id"] == ror_id else current

    def resolve(self, name: str, country_name: str = "") -> dict | None:
        """Resolve one affiliation name to a ROR organisation.

        Ambiguity is refused rather than guessed: a key claimed by several
        organisations only resolves when the observed country picks exactly one.
        Acronyms are never used to disambiguate — "MIT", "CAS" and "UCL" are
        claimed by dozens of records.
        """
        keys = alias_keys(name)
        if not keys:
            return None
        cache_key = (keys[0], country_name)
        if cache_key in self._cache:
            return self._cache[cache_key]
        result = None
        for key in keys:
            rows = self._connect().execute(
                "SELECT n.ror_id, n.name_type, o.display, o.country_name,"
                " o.country_code, o.status, o.parent_id"
                " FROM names n JOIN orgs o ON o.ror_id=n.ror_id"
                " WHERE n.normalized=?", (key,)).fetchall()
            result = self._pick(rows, country_name)
            if result:
                break
        self._cache[cache_key] = result
        return result


    def is_research_umbrella(self, org: dict | None) -> bool:
        """Can this organisation stand as a parent group?

        Helmholtz, Max Planck and the Chinese Academy of Sciences may; a
        ministry, a national government or the board that administers the ETH
        Domain may not. ROR types cannot separate them — CAS, CNRS, Helmholtz
        and the Swiss federal board are all ``funder,government`` — so the
        discriminator is the name: administrative organs announce themselves.
        """
        if not org:
            return False
        display = org.get("display", "")
        if ADMINISTRATIVE_BODY.search(display):
            return False
        if UNIVERSITY_SYSTEM.search(display):
            return False
        types = {t for t in (org.get("org_types") or "").split(",") if t}
        if types and types <= {"government"}:
            return False
        return self.child_count(org["ror_id"]) >= MIN_UMBRELLA_CHILDREN

    def child_count(self, ror_id: str) -> int:
        if ror_id not in self._children:
            self._children[ror_id] = self._connect().execute(
                "SELECT COUNT(*) FROM orgs WHERE parent_id=?",
                (ror_id,)).fetchone()[0]
        return self._children[ror_id]

    def eligible_parent(self, ror_id: str) -> dict | None:
        """Outermost ancestor that qualifies as a parent group.

        Walks all the way up instead of stopping at the first qualifying
        ancestor. Helmholtz Munich and the GSI Helmholtz Centre are themselves
        umbrellas over a handful of institutes, so stopping early filed the
        Institute of Computational Biology under "Helmholtz Munich" and the
        Helmholtz Institute Jena under "GSI" — three Helmholtz buckets instead
        of one. Those centres are institutions in their own right; the group
        everything rolls up to is the Association.
        """
        seen = {ror_id}
        current = self.org(ror_id)
        best = None
        for _ in range(8):
            if current is None:
                break
            parent_id = current.get("parent_id") or ""
            if not parent_id or parent_id in seen:
                break
            seen.add(parent_id)
            parent = self.org(parent_id)
            if parent is None:
                break
            if self.is_research_umbrella(parent):
                best = parent
            current = parent
        return best

    def root_org(self, ror_id: str) -> dict | None:
        """Topmost organisation in the ROR parent chain.

        This is the headquarters for a multinational: Microsoft Research Asia is
        a Chinese site of an American company, so its own record says China but
        its root says the United States.
        """
        seen, current = {ror_id}, self.org(ror_id)
        for _ in range(8):
            if current is None:
                return None
            parent_id = current.get("parent_id") or ""
            if not parent_id or parent_id in seen:
                return current
            seen.add(parent_id)
            current = self.org(parent_id)
        return current

    def is_ancestor(self, ancestor_id: str, ror_id: str) -> bool:
        """Does ROR record `ancestor_id` above `ror_id` in the parent chain?"""
        if not ancestor_id or not ror_id or ancestor_id == ror_id:
            return False
        seen = {ror_id}
        current = self.org(ror_id)
        for _ in range(8):
            if current is None:
                return False
            parent_id = current.get("parent_id") or ""
            if not parent_id or parent_id in seen:
                return False
            if parent_id == ancestor_id:
                return True
            seen.add(parent_id)
            current = self.org(parent_id)
        return False


    def resolve_affiliation(self, name: str, country_name: str = "",
                            allow_remote: bool = True) -> dict:
        """Split an affiliation into (institution, parent group).

        Affiliation strings nest a unit inside an umbrella:

            "Institute of Automation, Chinese Academy of Sciences"

        The named institute is the institution and CAS is the parent group. The
        rule is: find the rightmost segment that resolves to an eligible
        research umbrella, then take the segment closest to it on the left as
        the institution. If ROR has no record for that segment — its slot in the
        hierarchy is simply missing — the segment closest to the umbrella is
        still the institution name, verified against Wikipedia so the pipeline
        does not invent organisations out of stray text.
        """
        # PDF line breaks split words with a hyphen ("Seoul National Uni-
        # versity", "As- tronomy"), which stops the real institution from
        # resolving and hands the match to a sub-unit segment instead.
        raw = re.sub(r"([A-Za-z])-\s+([a-z])", r"\1\2", str(name or ""))
        # Author-order markers are dropped outright, so neither the lookup nor
        # the sub-unit test nor the stored display name ever sees them.
        raw = strip_marker_digits(re.sub(r"\s+", " ", raw)).strip()
        if not raw:
            return _outcome("", "", evidence="empty")

        direct = self.resolve(raw, country_name)
        if direct:
            parent = self.eligible_parent(direct["ror_id"])
            return _outcome(
                direct["display"], parent["display"] if parent else "",
                ror_id=direct["ror_id"],
                parent_ror_id=parent["ror_id"] if parent else "",
                country_name=direct["country_name"],
                evidence=f"ror:{direct['matched_as']}")

        segments = [s.strip() for s in raw.split(",") if s.strip()]
        if len(segments) > 1:
            for index in range(len(segments) - 1, 0, -1):
                if is_place_only_segment(segments[index]):
                    continue
                umbrella = self.resolve(segments[index], country_name)
                if not (umbrella and self.is_research_umbrella(umbrella)):
                    continue
                # An administrative organ is never the institution either:
                # "Key Lab …, Ministry of Education, Tsinghua University" names
                # Tsinghua, not the ministry.
                # A sub-unit is never the institution: "1Division of Physics,
                # Mathematics and Astronomy, California Institute of Technology"
                # names Caltech.
                left = [s for s in segments[:index]
                        if not ADMINISTRATIVE_BODY.search(s)
                        and not SUBUNIT_NAME.search(s)]
                for candidate in reversed(left):
                    inner = self.resolve(candidate, country_name)
                    if inner and not ADMINISTRATIVE_BODY.search(inner["display"]):
                        # Co-occurrence on one line is not a hierarchy: a
                        # multi-affiliation footnote put "…MIT…, University of
                        # Amsterdam" on one line and made UvA the parent of MIT.
                        # The umbrella has to actually own the institute.
                        owns = self.is_ancestor(umbrella["ror_id"],
                                                inner["ror_id"])
                        return _outcome(
                            inner["display"],
                            umbrella["display"] if owns else "",
                            ror_id=inner["ror_id"],
                            parent_ror_id=umbrella["ror_id"] if owns else "",
                            country_name=(inner["country_name"]
                                          or umbrella["country_name"]),
                            evidence=("ror:inner+umbrella" if owns
                                      else "ror:inner"))
                nearest = left[-1] if left else ""
                # A sub-unit is not an institution even when Wikipedia has an
                # article about it: the school rolls up to the umbrella.
                if (nearest and not SUBUNIT_NAME.search(nearest)
                        and wikipedia_confirms_organisation(
                            nearest, allow_remote=allow_remote)):
                    return _outcome(
                        nearest, umbrella["display"],
                        parent_ror_id=umbrella["ror_id"],
                        country_name=umbrella["country_name"],
                        evidence="wikipedia+umbrella")
                return _outcome(
                    umbrella["display"], "", ror_id=umbrella["ror_id"],
                    country_name=umbrella["country_name"],
                    evidence="umbrella-only")

            # Sub-unit segments are skipped: "University of Bath, Department of
            # Mathematical Sciences" resolved to a Russian record literally
            # named "Department of Mathematical Sciences" because the last
            # segment was tried first.
            ordered = ([s for s in reversed(segments)
                        if not SUBUNIT_NAME.search(s)]
                       + [s for s in reversed(segments)
                          if SUBUNIT_NAME.search(s)])
            for candidate in (s for s in ordered
                              if not is_place_only_segment(s)):
                inner = self.resolve(candidate, country_name)
                if inner:
                    parent = self.eligible_parent(inner["ror_id"])
                    return _outcome(
                        inner["display"], parent["display"] if parent else "",
                        ror_id=inner["ror_id"],
                        parent_ror_id=parent["ror_id"] if parent else "",
                        country_name=inner["country_name"],
                        evidence="ror:segment")
        # Word-suffix fallback for names with junk welded to the front: an
        # author byline ("Yong Li Tsinghua University", "Robert Jakob ETH
        # Zürich") or a stray token. Drop leading words while a suffix of at
        # least two words still resolves, longest suffix first.
        # Only for a single-segment name. Walking word suffixes across commas
        # reaches into the *next* affiliation: "…, Harvard-MIT, Cambridge, MA"
        # yielded the tail "Cambridge, MA" and matched Cambridge IVF.
        words = raw.split() if len(segments) <= 1 else []
        for start in range(1, min(len(words) - 1, 6)):
            tail = " ".join(words[start:])
            if is_place_only_segment(tail):
                continue
            inner = self.resolve(tail, country_name)
            if inner and not ADMINISTRATIVE_BODY.search(inner["display"]):
                parent = self.eligible_parent(inner["ror_id"])
                return _outcome(
                    inner["display"], parent["display"] if parent else "",
                    ror_id=inner["ror_id"],
                    parent_ror_id=parent["ror_id"] if parent else "",
                    country_name=inner["country_name"],
                    evidence="ror:word-suffix")
        return _outcome(raw, "", evidence="unresolved")
    @staticmethod
    def _pick(rows, country_name: str) -> dict | None:
        active = [r for r in rows if r[5] == "active"] or list(rows)
        if not active:
            return None
        best_rank = min(NAME_TYPE_RANK.get(r[1], 9) for r in active)
        tier = [r for r in active if NAME_TYPE_RANK.get(r[1], 9) == best_rank]
        candidates = {r[0]: r for r in tier}
        if len(candidates) > 1 and country_name:
            narrowed = {rid: r for rid, r in candidates.items()
                        if r[3] == country_name}
            if len(narrowed) == 1:
                candidates = narrowed
        if best_rank >= NAME_TYPE_RANK["acronym"] and len(candidates) > 1:
            # An acronym is evidence only when it resolves to one organisation.
            # "MIT" is claimed by 9 records and "CAS" by 20; "EPFL", "KAIST" and
            # "INRIA" by exactly one. "CNRS" is claimed by three, and only the
            # observed country separates the French CNRS from Lebanon's and
            # Canada's — which is why the country filter runs first.
            return None
        if len(candidates) > 1:
            # ROR splits a multinational into one record per country —
            # "Microsoft (United States)", "(India)", "(Ireland)" — so a bare
            # company name is always ambiguous. The headquarters is the root of
            # that family: the sibling whose parent lies outside it.
            bases = {re.sub(r"\s*\([^)]*\)\s*$", "", row[2]).strip()
                     for row in candidates.values()}
            if len(bases) == 1:
                ids = set(candidates)
                roots = {rid: row for rid, row in candidates.items()
                         if (row[6] or "") not in ids}
                if len(roots) == 1:
                    candidates = roots
        if len(candidates) != 1:
            return None
        ror_id, name_type, display, country, code, _status, parent = \
            next(iter(candidates.values()))
        return {"ror_id": ror_id, "display": display, "country_name": country,
                "country_code": code, "parent_id": parent,
                "matched_as": name_type}


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dump", type=Path, default=None)
    ap.add_argument("--index", type=Path, default=None)
    args = ap.parse_args()
    print(json.dumps(build_index(args.dump, args.index),
                     ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
