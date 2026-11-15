"""Institution naming policy for the bibliography DB.

The six rules (README "기관명 정규화 기준"):

1. Institution name: the university or research institute itself, under its
   official English name, which is ROR's English name ("Georgia Institute of
   Technology", not the Wikipedia title "Georgia Tech"). Without an English
   ROR name, the English Wikipedia article title; without either, the native
   name. One name per institution whatever language a paper wrote it in.
2. Parent: only a real structural umbrella (Helmholtz Association, Max Planck
   Society, Chinese Academy of Sciences). Multi-campus university systems such
   as the University of California are not parents. Named by the same Wikipedia
   rule. The parent is never empty: an institution without an umbrella has
   its own name as parent ("IBM" -> "IBM"), so grouping by parent keeps IBM
   Research - Zurich and IBM together. Names containing "Institute" or "Laboratory" are listed by the
   audit with their parent status so a missing umbrella is visible.
3. Affiliation numbers ("3Stanford University") are not part of any string.
4. Download watermarks ("Authorized licensed use limited to: …") are not
   affiliations.
5. Every name, alias and source string is a single line.
6. City and country: what the affiliation string states explicitly
   ("…, Seoul 02792, Republic of Korea"); otherwise the institution's ROR record
   (GeoNames location, the coordinates Wikipedia also cites).

Corrections for wrong links and names live in
``pipeline/data/institution_corrections.json`` and are applied on every build,
so a rebuild cannot bring a corrected error back.
"""
from __future__ import annotations

import html
import json
import re
import sqlite3
import unicodedata
from collections import Counter
from pathlib import Path
from typing import Callable
from urllib.parse import unquote, urlparse

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
WIKIPEDIA_TITLES_PATH = DATA_DIR / "institution_wikipedia_titles.json"
CORRECTIONS_PATH = DATA_DIR / "institution_corrections.json"

# Rule 4. Publisher download stamps printed on every page of a licensed PDF.
WATERMARK = re.compile(
    r"(?i)authori[sz]ed licensed use limited to"
    r"|\bdownloaded (?:on|from)\b"
    r"|\bpersonal use is permitted\b"
    r"|\brestrictions apply\b")

# Rule 3. A footnote marker welded to the following word: "3Stanford",
# "26University". Two letters must follow so "3M" keeps its digit.
_MARKER = re.compile(r"(?<![\w.])(\d{1,2})(?=[^\W\d_][´`¨]?[^\W\d_])")
_LEADING_SYMBOLS = re.compile(r"^[\s*†‡§¶#♣♢♡♠◊△▽○●□■◆★⁰¹²³⁴⁵⁶⁷⁸⁹]+")
_LEADING_SPACED_MARKER = re.compile(r"^\d{1,2}\s+(?=[A-Z])")
# Rule 5. A line-break hyphen inside a word: "Uni- versity", "Re- public".
_LINE_BREAK_HYPHEN = re.compile(r"(?<=[a-z])-\s+(?=[a-z])")
_SPACE = re.compile(r"\s+")

# Wikipedia article titles for the country names ROR and the parsers write.
WIKIPEDIA_COUNTRY = {
    "Czechia": "Czech Republic",
    "Macao": "Macau",
    "The Netherlands": "Netherlands",
    "Russian Federation": "Russia",
    "DR Congo": "Democratic Republic of the Congo",
    "Congo Republic": "Republic of the Congo",
    "Türkiye": "Turkey",
    "Cabo Verde": "Cape Verde",
    "Timor-Leste": "East Timor",
    "Viet Nam": "Vietnam",
    "Republic of Korea": "South Korea",
    "Korea": "South Korea",
    "USA": "United States",
    "UK": "United Kingdom",
    "Syrian Arab Republic": "Syria",
    "Moldova, Republic of": "Moldova",
    "Iran, Islamic Republic of": "Iran",
    "Korea, Republic of": "South Korea",
    "Taiwan, Province of China": "Taiwan",
    "Tanzania, United Republic of": "Tanzania",
    "Lao People's Democratic Republic": "Laos",
    "Bolivia, Plurinational State of": "Bolivia",
    "Venezuela, Bolivarian Republic of": "Venezuela",
}

# A trailing segment that is a country by itself. Two-letter tokens are
# refused except these: "GA" is Georgia the US state as often as Gabon, and "CA"
# is California far more often than Canada.
_COUNTRY_ACRONYMS = {"USA", "US", "UK", "UAE", "PRC", "ROK", "U.S.", "U.S.A.",
                     "U.K."}
# Country names that are also US states: "Atlanta, Georgia" is not Georgia.
_US_STATE_COUNTRIES = {"georgia"}
_COUNTRY_PHRASES = {"p.r. china", "pr china", "p. r. china", "hong kong sar",
                    "england", "scotland", "wales", "northern ireland",
                    "korea", "the netherlands", "republic of korea"}

_INSTITUTE_OR_LAB = re.compile(r"(?i)\binstitut|\blaborator|\blab\b")


def wikipedia_country(name: str) -> str:
    name = (name or "").strip()
    return WIKIPEDIA_COUNTRY.get(name, name)


def is_access_watermark(text: str) -> bool:
    return bool(WATERMARK.search(text or ""))


def one_line(text: str) -> str:
    """Rule 5: collapse line breaks and rejoin words split by a wrap hyphen.

    HTML entities left by the text extractor ("Electrical &amp; Computer") are
    decoded too.
    """
    value = unicodedata.normalize("NFC", html.unescape(str(text or "")))
    value = _SPACE.sub(" ", value).strip()
    return _LINE_BREAK_HYPHEN.sub("", value)


def strip_affiliation_numbers(text: str,
                              is_name: Callable[[str], bool] | None = None) -> str:
    """Rule 3: drop footnote numbers; keep digits that belong to a name.

    ``is_name`` vetoes a strip when the digit-led token is itself a known
    organisation name ("4Paradigm").
    """
    value = _LEADING_SYMBOLS.sub("", text)
    value = _LEADING_SPACED_MARKER.sub("", value)

    def drop(match: re.Match) -> str:
        if is_name is not None:
            word = re.match(r"\d{1,2}[^\W\d_][\w.-]*", value[match.start():])
            if word and is_name(word.group(0)):
                return match.group(0)
        return ""

    return _MARKER.sub(drop, value).strip(" ,;")


def clean_affiliation_text(text: str,
                           is_name: Callable[[str], bool] | None = None) -> str:
    """Rules 3 and 5 for one affiliation string."""
    return strip_affiliation_numbers(one_line(text), is_name)


def _norm(text: str) -> str:
    return _SPACE.sub(" ", (text or "").strip()).casefold()


def _normalize(text: str) -> str:
    try:
        from .ror_index import normalize
    except ImportError:
        from lib.ror_index import normalize
    return normalize(text)


# --- Rule 1/2: Wikipedia titles -------------------------------------------

def wikipedia_page(url: str) -> tuple[str, str]:
    """(language, title) of a Wikipedia article URL; ("", "") otherwise."""
    parsed = urlparse(url or "")
    host = parsed.netloc.lower()
    if not host.endswith("wikipedia.org") or "/wiki/" not in parsed.path:
        return "", ""
    lang = host.split(".")[0]
    title = unquote(parsed.path.split("/wiki/", 1)[1]).replace("_", " ").strip()
    return (lang, title) if title else ("", "")


def title_key(lang: str, title: str) -> str:
    return f"{lang}:{title}"


def load_titles(path: Path | None = None) -> dict[str, str]:
    path = path or WIKIPEDIA_TITLES_PATH
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def display_title(title: str) -> str:
    """Drop a Wikipedia disambiguator: "Mila (research institute)" → "Mila".

    Only a lower-case disambiguator is dropped; "(Guangzhou)" is part of the
    name of the Hong Kong University of Science and Technology (Guangzhou).
    """
    return re.sub(r"\s+\([a-z][^)]*\)$", "", title).strip()


_LEGAL_FORM = {"inc", "corporation", "corp", "company", "co", "group", "sa",
               "ag", "gmbh", "ltd", "plc", "llc", "platform", "d", "o",
               "holding", "se", "nv", "bv", "spa"}


def ror_display(org: dict) -> str:
    """ROR's label without the country ROR appends to subsidiaries."""
    display = org["display"]
    country = org.get("country_name") or ""
    if country and display.endswith(f"({country})"):
        return display[: -len(country) - 2].strip()
    return display


def _initials(words: list[str]) -> str:
    return "".join(w[0] for w in words)


class Names:
    """Official institution names.

    The official name is ROR's English name: the registry records the name an
    organisation uses for itself ("Georgia Institute of Technology", not the
    Wikipedia article title "Georgia Tech"; "Massachusetts Institute of
    Technology", not "MIT"). ROR's country suffix for multinationals is
    dropped ("IBM (United States)" -> "IBM").

    Only when ROR has no English name ("Ludwig-Maximilians-Universität
    München") does the English Wikipedia article title name the institution.
    The pinned title map holds, per linked article, the current English title
    ("" when the article has no English version). An English title is used
    only when it still describes the organisation: ROR links that now
    redirect to a parent or a topic fail the fit test and the native ROR name
    is kept.
    """

    def __init__(self, index, titles: dict[str, str] | None = None,
                 is_local_language: Callable[[str], bool] | None = None) -> None:
        if is_local_language is None:
            raise ValueError("Names needs the local-language test "
                             "(build_bibliography_db.is_local_language_institution)")
        self.is_local_language = is_local_language
        self.index = index
        self.titles = load_titles() if titles is None else titles
        self.unrefreshed: set[str] = set()
        self.rejected: dict[str, str] = {}
        self._cache: dict[str, tuple[str, str]] = {}

    def _fits(self, title: str, ror_id: str) -> bool:
        """Does a redirected or translated title still name this record?"""
        core = _normalize(re.sub(r"\s*\([^)]*\)", "", title))
        tokens = set(core.split()) - _LEGAL_FORM
        if not tokens:
            return False
        keys = self.index.name_keys(ror_id)
        vocabulary = {word for key in keys for word in key.split()}
        if len(tokens & vocabulary) / len(tokens) >= 0.5:
            return True
        compact = "".join(sorted(tokens)) if len(tokens) == 1 else ""
        return any(compact and compact == _initials(key.split()) for key in keys)

    def _broader(self, title: str, org: dict) -> bool:
        """Is the article about a wider organisation that ROR records apart?

        ROR links Microsoft Research Asia to the article "Microsoft Research",
        which ROR holds as its own record. A country subsidiary ("Google
        (Ireland)" → "Google") is the same organisation and is not broader.
        """
        core = _normalize(re.sub(r"\s*\([^)]*\)\s*$", "", org["display"]))
        title_tokens = set(_normalize(display_title(title)).split())
        missing = set(core.split()) - title_tokens - _LEGAL_FORM
        if not missing or not (missing - GENERIC_WORDS):
            return False
        return bool(self.index.other_records(display_title(title), org["ror_id"]))

    def name_for(self, ror_id: str) -> tuple[str, str]:
        """(name, source) for a ROR id; ("", "") when ROR does not know it."""
        if ror_id not in self._cache:
            self._cache[ror_id] = self._name_for(ror_id)
        return self._cache[ror_id]

    def _name_for(self, ror_id: str) -> tuple[str, str]:
        org = self.index.org(ror_id)
        if not org:
            return "", ""
        official = ror_display(org)
        if self.index.display_is_english(ror_id) and \
                not self.is_local_language(official):
            return official, "ror"
        lang, title = wikipedia_page(self.index.reference(ror_id)["wikipedia"])
        if lang:
            key = title_key(lang, title)
            if key not in self.titles:
                self.unrefreshed.add(ror_id)
                english = title if lang == "en" else ""
            else:
                english = self.titles[key]
            # ROR's curators chose the linked article, so a direct English
            # link is trusted. A redirect or a cross-language link is where
            # an article about a parent or a topic slips in.
            direct = lang == "en" and english.casefold() == title.casefold()
            if english:
                if (direct or self._fits(english, ror_id)) and \
                        not self._broader(english, org):
                    return display_title(english), "wikipedia"
                self.rejected[ror_id] = english
        return official, "ror"


# --- Identity evidence ------------------------------------------------------
#
# ROR matching on a generic phrase put 72 papers under "InterAction" (the word
# "interaction" in body text), 37 under "Research Center SHARQ" (any "Research
# Center") and 17 "FAIR at Meta" links under the Facility for Antiproton and Ion
# Research. A ROR link stands only when the source string names the record by
# something distinctive: a name with a non-generic word, or a generic name of
# two words or more that is the whole of a comma-delimited span ("National
# Institutes of Health", not "Indian Institute of Science" read as "Institute
# of Science").
GENERIC_WORDS = frozenset("""
research center centre institute institution university college school
laboratory lab national international department ministry education advanced
technology science engineering applied health medical hospital foundation
society academy innovation development information studie study program
programme group unit division office service system network agency council
commission corporation company inc graduate faculty polytechnic technical
federal state key general public global independent new open high performance
computing computer data digital life biology biomedical clinical cancer
molecular genetic chemical material mathematic physic artificial intelligence
ai machine learning interaction impact future frontier translational social
human natural energy environmental management business economic policy art
design medicine communication electronic alliance consortium initiative fair
""".split())


def _spans(raw: str) -> set[str]:
    parts = [_normalize(p) for p in re.split(r"[,;]", raw)]
    spans = set()
    for start in range(len(parts)):
        for end in range(start + 1, min(start + 3, len(parts)) + 1):
            span = " ".join(p for p in parts[start:end] if p)
            spans.add(" ".join(t for t in span.split() if t not in _LEGAL_FORM))
    return spans


def identity_evidence(raw: str, keys: list[str]) -> bool | None:
    """Does ``raw`` name the record distinctively?

    None when no name of the record occurs at all: the link came from a
    publisher affiliation id (Scopus maps "Haas School of Business" to UC
    Berkeley), which the string cannot confirm or refute.
    """
    text = f" {_normalize(raw)} "
    found = [k for k in keys if k and f" {k} " in text]
    if not found:
        return None
    spans = None
    for key in found:
        tokens = key.split()
        if set(tokens) - GENERIC_WORDS:
            return True
        if len(tokens) >= 2:
            spans = _spans(raw) if spans is None else spans
            if " ".join(t for t in tokens if t not in _LEGAL_FORM) in spans:
                return True
    return False


def distinctive_organisation(raw: str, index) -> str:
    """ROR id of the organisation the string names distinctively, or "".

    The last such comma segment wins: affiliations run sub-unit first,
    institution last ("Institute for Machine Learning, D-INFK, ETH Zurich").
    """
    found = ""
    for segment in re.split(r"[,;]", raw):
        segment = segment.strip()
        if len(_normalize(segment).split()) < 2 and not re.fullmatch(
                r"[A-Z][A-Za-z]{2,9}", segment):
            continue
        hit = index.resolve(segment)
        if hit and identity_evidence(segment, index.name_keys(hit["ror_id"])):
            found = hit["ror_id"]
    return found


# --- Rule 6: explicit place in the affiliation string ----------------------

_POSTAL = re.compile(r"[\d\-]+")


def _segments(raw: str) -> list[str]:
    return [s.strip(" .") for s in re.split(r"[,;]", raw) if s.strip(" .")]


def _is_country_name(text: str) -> bool:
    """The whole of ``text`` is a country name (not "New Jersey", not "GA")."""
    if len(text) < 4:
        return False
    try:
        from . import country_map
    except ImportError:
        from lib import country_map
    return country_map.country_resolution(text)[0] == "present"


def is_multi_affiliation(raw: str) -> bool:
    """A string that packs several numbered affiliations onto one line."""
    return bool(re.search(r"[,;]\s*\d{1,2}\s*[A-Z]|\S\s*[⁰¹²³⁴⁵⁶⁷⁸⁹]{1,2}\s*[A-Z]",
                          raw))


def explicit_place(raw: str, country_of: Callable[[str], str],
                   cities: dict[str, set[str]]) -> tuple[str, str]:
    """(city, country) the string itself states in its trailing segments."""
    if is_multi_affiliation(raw):
        return "", ""
    parts = _segments(raw)
    if len(parts) < 2:
        return "", ""
    tail = _SPACE.sub(" ", _POSTAL.sub(" ", parts[-1])).strip()
    if not tail or len(tail.split()) > 4:
        return "", ""
    if not (tail in _COUNTRY_ACRONYMS or tail.casefold() in _COUNTRY_PHRASES
            or _is_country_name(tail)) or tail.casefold() in _US_STATE_COUNTRIES:
        return "", ""
    country = wikipedia_country(country_of(tail))
    if not country:
        return "", ""
    # Two affiliations run together without markers ("…, Shanghai, China Johns
    # Hopkins University, Baltimore, USA"): another country earlier in the
    # string means the tail need not belong to this institution.
    earlier = wikipedia_country(country_of(", ".join(parts[:-1])))
    if earlier and earlier != country:
        return "", ""
    known = cities.get(country, set())
    city = ""
    for part in reversed(parts[-3:-1]):
        candidate = _SPACE.sub(" ", _POSTAL.sub(" ", part)).strip()
        if candidate in known:
            city = candidate
            break
    return city, country


# --- Merging --------------------------------------------------------------

def merge_institutions(conn: sqlite3.Connection, keep: int, drop: int) -> None:
    """Move every link of ``drop`` onto ``keep`` and delete ``drop``."""
    if keep == drop:
        return
    conn.execute(
        "INSERT OR IGNORE INTO paper_institutions "
        "(paper_id,institution_id,raw_name,country_name,source) "
        "SELECT paper_id,?,raw_name,country_name,source "
        "FROM paper_institutions WHERE institution_id=?", (keep, drop))
    conn.execute("DELETE FROM paper_institutions WHERE institution_id=?", (drop,))
    conn.execute("UPDATE OR IGNORE paper_author_institutions SET institution_id=? "
                 "WHERE institution_id=?", (keep, drop))
    conn.execute("DELETE FROM paper_author_institutions WHERE institution_id=?",
                 (drop,))
    conn.execute("UPDATE OR IGNORE institution_aliases SET institution_id=? "
                 "WHERE institution_id=?", (keep, drop))
    conn.execute("DELETE FROM institution_aliases WHERE institution_id=?", (drop,))
    for column in ("country_name_en", "hq_country_name_en", "ror_id",
                   "parent_name", "parent_ror_id", "city_name"):
        conn.execute(
            f"UPDATE institutions SET {column}=(SELECT {column} FROM "
            f"institutions WHERE institution_id=?) WHERE institution_id=? "
            f"AND {column}=''", (drop, keep))
    conn.execute("DELETE FROM institutions WHERE institution_id=?", (drop,))


def _drop_link(conn: sqlite3.Connection, paper_id: int, institution_id: int) -> None:
    conn.execute("DELETE FROM paper_institutions WHERE paper_id=? "
                 "AND institution_id=?", (paper_id, institution_id))
    conn.execute("DELETE FROM paper_author_institutions WHERE paper_id=? "
                 "AND institution_id=?", (paper_id, institution_id))


def _move_link(conn: sqlite3.Connection, paper_id: int, source: int,
               target: int) -> None:
    conn.execute(
        "INSERT OR IGNORE INTO paper_institutions "
        "(paper_id,institution_id,raw_name,country_name,source) "
        "SELECT paper_id,?,raw_name,country_name,source FROM paper_institutions "
        "WHERE paper_id=? AND institution_id=?", (target, paper_id, source))
    conn.execute(
        "UPDATE OR IGNORE paper_author_institutions SET institution_id=? "
        "WHERE paper_id=? AND institution_id=?", (target, paper_id, source))
    _drop_link(conn, paper_id, source)


# --- Corrections ------------------------------------------------------------

def load_corrections(path: Path | None = None) -> list[dict]:
    path = path or CORRECTIONS_PATH
    data = json.loads(path.read_text(encoding="utf-8"))
    rules = data["rules"]
    seen = set()
    for rule in rules:
        if rule["id"] in seen:
            raise ValueError(f"duplicate correction id {rule['id']}")
        seen.add(rule["id"])
        if rule["action"] not in {"relink", "drop", "set"}:
            raise ValueError(f"{rule['id']}: unknown action {rule['action']}")
        if not rule.get("reason"):
            raise ValueError(f"{rule['id']}: reason is required")
        match = rule.get("match") or {}
        if not (match.get("ror_id") or match.get("institution")
                or match.get("raw_contains")):
            raise ValueError(f"{rule['id']}: match needs ror_id, institution "
                             "or raw_contains")
    return rules


def _matching_links(conn: sqlite3.Connection, match: dict) -> list[tuple]:
    clauses, params = [], []
    if match.get("ror_id"):
        clauses.append("i.ror_id=?")
        params.append(match["ror_id"])
    if match.get("institution"):
        clauses.append("i.normalized_name=?")
        params.append(_norm(match["institution"]))
    if match.get("raw_contains"):
        clauses.append("instr(lower(pi.raw_name), ?) > 0")
        params.append(match["raw_contains"].lower())
    if match.get("paper"):
        clauses.append("p.slug LIKE ?")
        params.append(match["paper"] + "%")
    return conn.execute(
        "SELECT pi.paper_id, pi.institution_id FROM paper_institutions pi "
        "JOIN institutions i USING(institution_id) JOIN papers p USING(paper_id) "
        "WHERE " + " AND ".join(clauses), params).fetchall()


def _target_institution(conn: sqlite3.Connection, target: dict, names: Names,
                        index) -> int:
    ror_id = target.get("ror_id", "")
    if ror_id:
        row = conn.execute("SELECT institution_id FROM institutions WHERE "
                           "ror_id=? ORDER BY institution_id", (ror_id,)).fetchone()
        if row:
            return row[0]
        name, source = names.name_for(ror_id)
        if not name:
            raise ValueError(f"correction target {ror_id} is not in ROR")
        # The record may already be stored under its Wikipedia name through
        # another ROR record of the same article.
        if source == "wikipedia":
            for institution_id, other_ror in conn.execute(
                    "SELECT institution_id, ror_id FROM institutions "
                    "WHERE ror_id<>'' ORDER BY institution_id").fetchall():
                if names.name_for(other_ror)[0] == name:
                    return institution_id
        org = index.org(ror_id)
        country = wikipedia_country(org["country_name"])
    else:
        name, source = target["institution"], "correction"
        country = target.get("country", "")
        row = conn.execute("SELECT institution_id FROM institutions WHERE "
                           "normalized_name=?", (_norm(name),)).fetchone()
        if row:
            return row[0]
    return conn.execute(
        "INSERT INTO institutions (institution_name,normalized_name,"
        "country_name_en,ror_id,name_source,source) VALUES (?,?,?,?,?,?)",
        (name, _norm(name), country, ror_id, source, "correction")).lastrowid


def apply_link_corrections(conn: sqlite3.Connection, rules: list[dict],
                           names: Names, index,
                           settled: set | None = None) -> dict[str, int]:
    """Apply relink/drop rules in file order; a link moved by one rule is
    added to ``settled`` and not matched by later rules or the identity check.
    """
    applied: dict[str, int] = {}
    settled = set() if settled is None else settled
    for rule in rules:
        if rule["action"] == "set":
            continue
        links = [link for link in _matching_links(conn, rule["match"])
                 if link not in settled]
        if not links:
            continue
        if rule["action"] == "drop":
            for paper_id, institution_id in links:
                _drop_link(conn, paper_id, institution_id)
        else:
            target = _target_institution(conn, rule["to"], names, index)
            moved = [link for link in links if link[1] != target]
            for paper_id, institution_id in moved:
                _move_link(conn, paper_id, institution_id, target)
            settled.update((paper_id, target) for paper_id, _iid in links)
            links = moved
        if links:
            applied[rule["id"]] = len(links)
    return applied


_SETTABLE = {"institution": "institution_name", "country": "country_name_en",
             "city": "city_name", "parent": "parent_name",
             "parent_ror_id": "parent_ror_id", "ror_id": "ror_id"}


def apply_set_corrections(conn: sqlite3.Connection,
                          rules: list[dict]) -> dict[str, int]:
    applied: dict[str, int] = {}
    for rule in rules:
        if rule["action"] != "set":
            continue
        ids = sorted({iid for _pid, iid in _matching_links(conn, rule["match"])})
        for institution_id in ids:
            for key, value in rule["to"].items():
                column = _SETTABLE[key]
                conn.execute(f"UPDATE institutions SET {column}=? "
                             "WHERE institution_id=?", (value, institution_id))
                if column == "institution_name":
                    conn.execute("UPDATE institutions SET normalized_name=?, "
                                 "name_source='correction' WHERE institution_id=?",
                                 (_norm(value), institution_id))
        if ids:
            applied[rule["id"]] = len(ids)
    return applied


# --- The pass ---------------------------------------------------------------

def _clean_strings(conn: sqlite3.Connection, is_name) -> dict[str, int]:
    dropped = cleaned = 0
    for paper_id, institution_id, raw in conn.execute(
            "SELECT paper_id, institution_id, raw_name FROM paper_institutions"
    ).fetchall():
        if is_access_watermark(raw):
            _drop_link(conn, paper_id, institution_id)
            dropped += 1
            continue
        value = clean_affiliation_text(raw, is_name)
        if value != raw:
            conn.execute("UPDATE paper_institutions SET raw_name=? WHERE "
                         "paper_id=? AND institution_id=?",
                         (value, paper_id, institution_id))
            cleaned += 1
    aliases = 0
    for alias_id, raw, institution_id in conn.execute(
            "SELECT alias_id, raw_name, institution_id FROM institution_aliases"
    ).fetchall():
        value = clean_affiliation_text(raw, is_name)
        if is_access_watermark(raw) or not value:
            conn.execute("DELETE FROM institution_aliases WHERE alias_id=?",
                         (alias_id,))
            aliases += 1
        elif value != raw:
            changed = conn.execute(
                "UPDATE OR IGNORE institution_aliases SET raw_name=?, "
                "normalized_alias=? WHERE alias_id=?",
                (value, _norm(value), alias_id)).rowcount
            if not changed:  # the cleaned alias already exists
                conn.execute("DELETE FROM institution_aliases WHERE alias_id=?",
                             (alias_id,))
            aliases += 1
    for institution_id, name in conn.execute(
            "SELECT institution_id, institution_name FROM institutions").fetchall():
        value = one_line(name)
        if value != name:
            conn.execute("UPDATE institutions SET institution_name=?, "
                         "normalized_name=? WHERE institution_id=?",
                         (value, _norm(value), institution_id))
    return {"watermark_links_dropped": dropped, "source_strings_cleaned": cleaned,
            "aliases_cleaned": aliases}


_UNIVERSITY_UNIT = re.compile(
    r"(?i)\b(?:school|college|faculty|department|division)\b")
_RESEARCH_BODY = re.compile(r"(?i)\b(?:institut|laborator|centre|center|"
                            r"observator|hospital|clinic)")


_UNIT_SPLIT = re.compile(
    r"\s+(?:School|College|Faculty|Department|Division)\b|,|\s+at\s+(?:the\s+)?",
    re.IGNORECASE)


# A school or faculty inside a university. "College" alone is not: King's
# College London, Harvey Mudd College and the University of Maryland, College
# Park are institutions of their own even where ROR files them under a system.
_SUB_UNIT = re.compile(r"(?i)\b(?:school|faculty|department|division)\b")
# Federations and systems whose members are institutions in their own right.
_FEDERATION = re.compile(
    r"(?i)^(?:university of london|city university of new york|"
    r"state university of new york|national university of ireland|"
    r"claremont colleges)$|\bsystem\b|\bgroup$|\bcolleges$")


def _is_university(org: dict) -> bool:
    return "education" in (org.get("org_types") or "").split(",")


def _university_of_unit(name: str, ror_id: str, parent_ror: str,
                        parent_name: str, index) -> str:
    """ROR id of the university a school or college belongs to, or "".

    - ROR's parent edge ("Questrom School of Business" -> Boston University).
    - The parent recorded on the row when it is a university ("Harvard
      Medical School" carries "Harvard University"; ROR gives no edge).
    - A withdrawn ROR record names its university inside its own name: ROR
      withdrew "Johns Hopkins University School of Medicine" and "Stanford
      University School of Medicine" as not separate organisations. Only the
      part that says "University" counts, and only in the same country.
    An active education record without either edge is a university of its
    own ("Hamamatsu University School of Medicine", "Lincoln University
    College" in Malaysia) and stays.
    """
    org = index.org(ror_id) or {}
    withdrawn = org.get("status") == "withdrawn"
    # A school is an education record; "Imperial College Healthcare NHS
    # Trust" is a hospital trust, not a college of Imperial.
    if not (_is_university(org) or withdrawn):
        return ""
    if _SUB_UNIT.search(name):
        if not parent_ror and parent_name:
            # A curated parent carries only a name; it counts when it is
            # exactly a ROR record's English name.
            hit = index.resolve(parent_name)
            if hit and ror_display(hit).casefold() == parent_name.casefold():
                parent_ror = hit["ror_id"]
        for candidate in (org.get("parent_id") or "", parent_ror):
            parent = index.org(candidate) if candidate else None
            if parent and candidate != ror_id and _is_university(parent) \
                    and not _FEDERATION.search(ror_display(parent)):
                return candidate
    if not withdrawn:
        return ""
    for part in _UNIT_SPLIT.split(name):
        part = part.strip(" .")
        if not re.search(r"(?i)universit", part):
            continue
        hit = index.resolve(part)
        if not hit or hit["ror_id"] == ror_id:
            continue
        university = index.org(hit["ror_id"]) or {}
        if _is_university(university) and \
                university.get("country_name") == org.get("country_name"):
            return hit["ror_id"]
    return ""


def _fold_university_units(conn: sqlite3.Connection, index, names: Names) -> int:
    """Rule 1: a school, college or faculty is its university.

    The institution of record is the university, so "Harvard Medical School"
    links count for Harvard University. Institutes, laboratories, centres and
    hospitals keep their own rows (rule 1 names research institutes as
    institutions), and a school that is a university of its own ("Icahn
    School of Medicine at Mount Sinai") stays.
    """
    folded = 0
    for institution_id, name, ror_id, parent_ror, parent_name in conn.execute(
            "SELECT institution_id, institution_name, ror_id, parent_ror_id, "
            "parent_name FROM institutions WHERE ror_id<>''").fetchall():
        if not _UNIVERSITY_UNIT.search(name) or _RESEARCH_BODY.search(name):
            continue
        university = _university_of_unit(name, ror_id, parent_ror,
                                         parent_name, index)
        if not university:
            continue
        target = _target_institution(conn, {"ror_id": university}, names, index)
        if target != institution_id:
            merge_institutions(conn, target, institution_id)
            folded += 1
    return folded


_GOVERNMENT = re.compile(r"(?i)\bgovernment\b")


def _settle_parents(conn: sqlite3.Connection, index, names: Names) -> int:
    """Rule 2 on the final rows.

    One Wikipedia name per parent; administrative bodies, university systems
    and governments are never parents. The parent is never empty: a row with
    no umbrella carries its own name ("IBM" -> "IBM", "Stanford University"
    -> "Stanford University"), so grouping by parent puts IBM Research - Zurich
    and IBM together and every institution in exactly one group. A parent that
    is one of the row's own names ("Georgia Tech" under "Georgia Institute of
    Technology") becomes the row's own name.
    """
    try:
        from .ror_index import ADMINISTRATIVE_BODY, UNIVERSITY_SYSTEM
    except ImportError:
        from lib.ror_index import ADMINISTRATIVE_BODY, UNIVERSITY_SYSTEM
    rows = conn.execute(
        "SELECT institution_id, institution_name, ror_id, parent_name, "
        "parent_ror_id FROM institutions").fetchall()
    settled: dict[int, tuple[str, str]] = {}
    for institution_id, name, ror_id, parent, parent_ror in rows:
        if not parent:
            settled[institution_id] = ("", "")
            continue
        if not parent_ror:
            # Only an exact ROR label names a curated parent: normalised
            # lookup folds plurals, and "Indian Institutes of Technology" (the
            # umbrella) would land on one IIT.
            hit = index.resolve(parent)
            if hit and ror_display(hit).casefold() == parent.casefold():
                parent_ror = hit["ror_id"]
        canonical = names.name_for(parent_ror)[0] if parent_ror else parent
        own = {_normalize(name)}
        if ror_id:
            own.update(index.name_keys(ror_id))
        if (ADMINISTRATIVE_BODY.search(canonical)
                or UNIVERSITY_SYSTEM.search(canonical)
                or _GOVERNMENT.search(canonical)):
            settled[institution_id] = ("", "")
        elif (_normalize(canonical) in own or _normalize(parent) in own
                or (parent_ror and parent_ror == ror_id)):
            settled[institution_id] = (name, ror_id)
        else:
            settled[institution_id] = (canonical, parent_ror)
    # No empty parent: an institution without an umbrella is its own group.
    for institution_id, name, ror_id, _parent, _parent_ror in rows:
        if settled[institution_id] == ("", ""):
            settled[institution_id] = (name, ror_id)
    changed = 0
    for institution_id, _name, _ror, parent, parent_ror in rows:
        if settled[institution_id] != (parent, parent_ror):
            conn.execute("UPDATE institutions SET parent_name=?, parent_ror_id=? "
                         "WHERE institution_id=?",
                         (*settled[institution_id], institution_id))
            changed += 1
    return changed


def _verify_identities(conn: sqlite3.Connection, index, names: Names,
                       settled: set) -> dict[str, int]:
    """Re-home or drop ROR links whose string names the record only generically."""
    keys: dict[str, list[str]] = {}
    relinked = dropped = 0
    for paper_id, institution_id, raw, ror_id in conn.execute(
            "SELECT pi.paper_id, pi.institution_id, pi.raw_name, i.ror_id "
            "FROM paper_institutions pi JOIN institutions i "
            "USING(institution_id) WHERE i.ror_id<>''").fetchall():
        if (paper_id, institution_id) in settled:
            continue
        if ror_id not in keys:
            keys[ror_id] = index.name_keys(ror_id)
        if identity_evidence(raw, keys[ror_id]) is not False:
            continue
        target_ror = distinctive_organisation(raw, index)
        if target_ror and target_ror != ror_id:
            target = _target_institution(conn, {"ror_id": target_ror}, names, index)
            _move_link(conn, paper_id, institution_id, target)
            relinked += 1
        else:
            _drop_link(conn, paper_id, institution_id)
            dropped += 1
    return {"generic_links_relinked": relinked, "generic_links_dropped": dropped}


# Sources whose links come from a publisher record looked up by DOI, not from
# the paper's own pages, and the same links restored from an author link by
# `reinstate_linked_institutions`. OpenAlex links were the ones that carried a
# cited paper's institutions in when the stored DOI belonged to a reference
# (paper 9957: Broad Institute, Dana-Farber, Revolution Medicines).
LOOKUP_SOURCES = ("openalex", "link:openalex")
_MARKER_GLUE = re.compile(r"(\d)([^\W\d_])")


def _rule_assertions(conn: sqlite3.Connection, rules: list[dict],
                     text_of: Callable[[int], str | None]) -> set:
    """(paper_id, ror_id) pairs a relink rule states the paper names.

    A rule scoped to a paper, or keyed on a phrase the paper's text contains,
    is an operator's reading of that paper's byline ("Harvard Medical School"
    for Harvard University on 9957), so it confirms the link however the
    institution's ROR names are spelled there.
    """
    asserted = set()
    for rule in rules:
        target = (rule.get("to") or {}).get("ror_id")
        match = rule["match"]
        if rule["action"] != "relink" or not target or not (
                match.get("paper") or match.get("raw_contains")):
            continue
        query, params = "SELECT paper_id FROM papers", []
        if match.get("paper"):
            query += " WHERE slug LIKE ?"
            params.append(match["paper"] + "%")
        for (paper_id,) in conn.execute(query, params).fetchall():
            phrase = (match.get("raw_contains") or "").casefold()
            if phrase:
                text = text_of(paper_id)
                if text is None or phrase not in text.casefold():
                    continue
            asserted.add((paper_id, target))
    return asserted


def _verify_lookup_links(conn: sqlite3.Connection, index,
                         paper_text: Callable[[int], str | None],
                         rules: list[dict]) -> int:
    """Source priority: the paper's own pages outrank a DOI lookup.

    A lookup-sourced link stands only when the paper's text names the
    institution (any ROR name, label, alias or acronym, or the stored name),
    or a relink rule states that it does. The whole text, not the byline
    alone: journals print affiliations after the references too. Measured on
    the corpus, about 2,450 of 3,192 OpenAlex links fail this, many on papers
    whose stored DOI is a cited work's (HelioX carried
    10.1038/s41592-025-02895-w and Tübingen with it). Papers without
    extracted text are left alone: there is nothing to check against, and the
    link's source column still says where it came from.
    """
    texts: dict[int, str | None] = {}

    def text_of(paper_id: int) -> str | None:
        if paper_id not in texts:
            text = paper_text(paper_id)
            # "4Tsinghua": a byline marker glued to the name.
            texts[paper_id] = (None if text is None
                               else _MARKER_GLUE.sub(r"\1 \2", text))
        return texts[paper_id]

    asserted = _rule_assertions(conn, rules, text_of)
    keys: dict[str, list[str]] = {}
    dropped = 0
    marks = ",".join("?" * len(LOOKUP_SOURCES))
    for paper_id, institution_id, name, ror_id in conn.execute(
            "SELECT pi.paper_id, pi.institution_id, i.institution_name, i.ror_id "
            "FROM paper_institutions pi JOIN institutions i USING(institution_id) "
            f"WHERE pi.source IN ({marks})", LOOKUP_SOURCES).fetchall():
        if (paper_id, ror_id) in asserted:
            continue
        text = text_of(paper_id)
        if text is None:
            continue
        names = [_normalize(name)]
        if ror_id:
            if ror_id not in keys:
                keys[ror_id] = index.name_keys(ror_id)
            names += keys[ror_id]
        if identity_evidence(text, [k for k in names if k]) is not True:
            _drop_link(conn, paper_id, institution_id)
            dropped += 1
    return dropped


def _drop_redundant_umbrellas(conn: sqlite3.Connection) -> int:
    """A lookup-sourced umbrella next to its own member adds nothing.

    OpenAlex lists "IBM" beside "IBM Research - Zurich" from the byline;
    grouping by parent already counts the paper for IBM.
    """
    marks = ",".join("?" * len(LOOKUP_SOURCES))
    rows = conn.execute(
        "SELECT DISTINCT pi.paper_id, pi.institution_id FROM paper_institutions pi "
        "JOIN institutions u USING(institution_id) "
        "JOIN paper_institutions member ON member.paper_id=pi.paper_id "
        "AND member.institution_id<>pi.institution_id "
        "JOIN institutions m ON m.institution_id=member.institution_id "
        f"WHERE pi.source IN ({marks}) AND (m.parent_name=u.institution_name "
        "OR (u.ror_id<>'' AND m.parent_ror_id=u.ror_id))",
        LOOKUP_SOURCES).fetchall()
    for paper_id, institution_id in rows:
        _drop_link(conn, paper_id, institution_id)
    return len(rows)


def _canonical_names(conn: sqlite3.Connection, names: Names) -> int:
    renamed = 0
    for institution_id, name, ror_id, parent, parent_ror in conn.execute(
            "SELECT institution_id, institution_name, ror_id, parent_name, "
            "parent_ror_id FROM institutions").fetchall():
        if ror_id:
            canonical, source = names.name_for(ror_id)
            if canonical and canonical != name:
                conn.execute("UPDATE institutions SET institution_name=?, "
                             "normalized_name=?, name_source=? "
                             "WHERE institution_id=?",
                             (canonical, _norm(canonical), source, institution_id))
                renamed += 1
        if parent_ror:
            canonical, _source = names.name_for(parent_ror)
            if canonical and canonical != parent:
                conn.execute("UPDATE institutions SET parent_name=? "
                             "WHERE institution_id=?", (canonical, institution_id))
    return renamed


def _merge_duplicates(conn: sqlite3.Connection, index) -> int:
    """One row per institution.

    Rows merge when they carry the same ROR id, or the same name and
    - all but at most one are ROR country records of a multinational
      ("Meta (Israel)", "Meta (United States)"), or
    - belong to one ROR family (a company and its country subsidiaries:
      "Google (Ireland)" and "Google (United States)" share a root record), or
    - all name the same Wikipedia article, or
    - at most one of them is ROR-backed (a registry row "Meta" joins the ROR
      record whose label is "Meta").
    Two unrelated ROR records that share a name ("Institute of Chemical
    Technology" in Mumbai and in Valencia) stay apart.
    """
    def root(ror_id: str) -> str:
        if not ror_id:
            return ""
        top = index.top_parent(ror_id)
        return top["ror_id"] if top else ror_id

    merged = 0
    rows = conn.execute(
        "SELECT institution_id, normalized_name, ror_id, name_source, "
        "(SELECT count(*) FROM paper_institutions pi "
        " WHERE pi.institution_id=i.institution_id) "
        "FROM institutions i").fetchall()
    # Labels of ROR-backed rows, so a non-ROR row named by ROR's label finds them.
    label_owner: dict[str, set[int]] = {}
    for institution_id, _name, ror_id, _source, _links in rows:
        org = index.org(ror_id) if ror_id else None
        if org:
            label_owner.setdefault(_norm(ror_display(org)), set()).add(institution_id)
    groups: dict[str, list[tuple]] = {}
    for row in rows:
        groups.setdefault(row[1], []).append(row)
    for row in rows:
        if not row[2] and row[1] in label_owner and len(label_owner[row[1]]) == 1:
            owner = next(iter(label_owner[row[1]]))
            owner_row = next(r for r in rows if r[0] == owner)
            if owner_row[1] != row[1]:
                groups.setdefault(owner_row[1], []).append(row)
                groups[row[1]] = [r for r in groups[row[1]] if r[0] != row[0]]
    by_ror: dict[str, list[tuple]] = {}
    for row in rows:
        if row[2]:
            by_ror.setdefault(row[2], []).append(row)
    clusters = [members for members in by_ror.values() if len(members) > 1]
    for members in groups.values():
        if len(members) < 2:
            continue
        backed = [m for m in members if m[2]]
        # ROR marks a multinational's country records with a suffix
        # ("Meta (Israel)", "Meta (United States)"): same name, same company.
        unsuffixed = [m for m in backed
                      if (index.org(m[2]) or {}).get("display", "")
                      == ror_display(index.org(m[2]) or {"display": ""})]
        if (len({m[2] for m in backed}) <= 1
                or len({root(m[2]) for m in backed}) == 1
                or len(unsuffixed) <= 1
                or all(m[3] == "wikipedia" for m in backed)):
            clusters.append(members)
    done: set[int] = set()
    for members in clusters:
        alive = [m for m in members if m[0] not in done]
        if len(alive) < 2:
            continue
        ranked = sorted(alive, key=lambda m: (
            not m[2], bool((index.org(m[2]) or {}).get("parent_id")) if m[2] else True,
            -m[4], m[0]))
        keep = ranked[0][0]
        for other in ranked[1:]:
            merge_institutions(conn, keep, other[0])
            done.add(other[0])
            merged += 1
    return merged


def _places(conn: sqlite3.Connection, index, country_of) -> dict[str, int]:
    cities = {wikipedia_country(k): v for k, v in index.cities().items()}
    countries_set = cities_set = 0
    for institution_id, ror_id, country, city in conn.execute(
            "SELECT institution_id, ror_id, country_name_en, city_name "
            "FROM institutions").fetchall():
        stated_country: Counter = Counter()
        stated_city: dict[str, Counter] = {}
        for (raw,) in conn.execute("SELECT raw_name FROM paper_institutions "
                                   "WHERE institution_id=?", (institution_id,)):
            c, k = explicit_place(raw, country_of, cities)
            if k:
                stated_country[k] += 1
                if c:
                    stated_city.setdefault(k, Counter())[c] += 1
        reference = index.reference(ror_id) if ror_id else {}
        reference_country = wikipedia_country(reference.get("country_name", ""))
        new_country = (stated_country.most_common(1)[0][0] if stated_country
                       else reference_country or wikipedia_country(country))
        # The city must sit in the chosen country: a stated city for that
        # country, else ROR's city when ROR places the record there.
        if stated_city.get(new_country):
            new_city = stated_city[new_country].most_common(1)[0][0]
        elif reference_country == new_country and reference.get("city"):
            new_city = reference["city"]
        elif new_country == wikipedia_country(country):
            new_city = city
        else:
            new_city = ""
        if new_country != country:
            conn.execute("UPDATE institutions SET country_name_en=? "
                         "WHERE institution_id=?", (new_country, institution_id))
            countries_set += 1
        if new_city != city:
            conn.execute("UPDATE institutions SET city_name=? "
                         "WHERE institution_id=?", (new_city, institution_id))
            cities_set += 1
    for column, table in (("hq_country_name_en", "institutions"),
                          ("country_name", "paper_institutions")):
        for old, new in WIKIPEDIA_COUNTRY.items():
            conn.execute(f"UPDATE {table} SET {column}=? WHERE {column}=?",
                         (new, old))
    return {"countries_set": countries_set, "cities_set": cities_set}


def apply(conn: sqlite3.Connection, country_of: Callable[[str], str],
          is_local_language: Callable[[str], bool],
          paper_text: Callable[[int], str | None],
          index=None, titles: dict[str, str] | None = None,
          corrections: list[dict] | None = None) -> dict:
    """Bring the institution tables in line with the six rules.

    ``paper_text(paper_id)`` returns the paper's text as extracted from its
    PDF (None when there is no text), the evidence lookup-sourced links are
    checked against.

    Runs at the end of every build after the parent and country passes. The
    result counts what changed; ``wikipedia_unrefreshed`` counts ROR records
    whose article title has not been resolved into the pinned title map yet
    (run ``pipeline/normalize_institutions.py --refresh-wikipedia``).
    """
    try:
        from .ror_index import RorIndex
    except ImportError:
        from lib.ror_index import RorIndex
    own_index = index is None
    index = index or RorIndex()
    if not index.available:
        raise RuntimeError("ROR index missing: python pipeline/lib/ror_index.py")
    try:
        names = Names(index, titles, is_local_language)
        rules = load_corrections() if corrections is None else corrections

        # Organisations whose own name starts with digits ("4Paradigm", "23andMe").
        # ROR's normalised keys drop leading digits, so the lookup has to be
        # against the display names themselves.
        digit_names = index.digit_led_names()

        def is_name(token: str) -> bool:
            return token.casefold() in digit_names

        settled: set = set()
        result = _clean_strings(conn, is_name)
        result["link_corrections"] = apply_link_corrections(
            conn, rules, names, index, settled)
        result.update(_verify_identities(conn, index, names, settled))
        result["renamed"] = _canonical_names(conn, names)
        result["university_units_folded"] = _fold_university_units(
            conn, index, names)
        result["merged"] = _merge_duplicates(conn, index)
        result.update(_places(conn, index, country_of))
        result["parents_settled"] = _settle_parents(conn, index, names)
        # Operator corrections have the last word on attributes.
        result["set_corrections"] = apply_set_corrections(conn, rules)
        result["merged"] += _merge_duplicates(conn, index)
        # Source priority, once every row has its final identity: a merge
        # can move a lookup link onto a row the paper does not name.
        result["lookup_links_unconfirmed"] = _verify_lookup_links(
            conn, index, paper_text, rules)
        result["redundant_umbrella_links"] = _drop_redundant_umbrellas(conn)
        conn.execute("DELETE FROM institutions WHERE institution_id NOT IN "
                     "(SELECT institution_id FROM paper_institutions)")
        conn.execute("DELETE FROM institution_aliases WHERE institution_id NOT IN "
                     "(SELECT institution_id FROM institutions)")
        result["wikipedia_unrefreshed"] = len(names.unrefreshed)
        return result
    finally:
        if own_index:
            index.close()


def parent_review(conn: sqlite3.Connection) -> list[dict]:
    """Rule 2 audit: every Institute/Laboratory with its parent status."""
    rows = conn.execute(
        "SELECT i.institution_name, i.parent_name, i.ror_id, i.country_name_en, "
        "count(pi.paper_id) FROM institutions i JOIN paper_institutions pi "
        "USING(institution_id) GROUP BY i.institution_id "
        "ORDER BY i.parent_name<>'', count(pi.paper_id) DESC").fetchall()
    return [{"institution": name, "parent": parent, "ror_id": ror,
             "country": country, "papers": papers,
             "parent_status": "has parent" if parent else "no parent"}
            for name, parent, ror, country, papers in rows
            if _INSTITUTE_OR_LAB.search(name)]
