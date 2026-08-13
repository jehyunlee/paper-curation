#!/usr/bin/env python3
"""Build a collection-independent bibliographic SQLite database.

The default run processes the reproducible 30-paper sample.  ``--all`` processes
all local papers.  OpenAlex/Crossref are used to resolve formal publications
for arXiv records; Zotero keys are matched from the user's library and, with
``--update-zotero``, safe bibliographic fields are patched there too.
"""
from __future__ import annotations
import os
import argparse
import difflib
import hashlib
import functools
import json
import random
import re
import sqlite3
import ssl
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
import uuid
from pathlib import Path
try:
    from .lib import bibliography_lock, country_map, doi as _doi
except ImportError:
    from lib import bibliography_lock, country_map, doi as _doi

ROOT = Path(__file__).resolve().parents[1]
PAPERS_DIR = ROOT / "docs" / "papers"
INDEX_PATH = PAPERS_DIR / "_papers_index.json"
DEFAULT_DB = Path(os.environ.get("PAPER_CURATION_BIBLIO_DB", str(
    ROOT / ".cache" / "bibliography.sqlite3"
)))
MAILTO = "jehyun.lee@gmail.com"
SSL_CTX = ssl.create_default_context()

SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS papers (
 paper_id INTEGER PRIMARY KEY, slug TEXT NOT NULL UNIQUE, title TEXT NOT NULL,
 publication_date TEXT, journal_name TEXT, doi TEXT, arxiv_id TEXT, url TEXT,
 volume TEXT, issue TEXT, pages TEXT, publisher TEXT, issn TEXT, eissn TEXT,
 document_type TEXT, scopus_eid TEXT, received_date TEXT, accepted_date TEXT,
 published_online_date TEXT, bibliography_source TEXT,
 review_dir TEXT NOT NULL, zotero_item_key TEXT, affiliation_source TEXT,
 affiliation_confidence REAL, header_raw TEXT, metadata_json TEXT NOT NULL DEFAULT '{}',
 created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS authors (
 author_id INTEGER PRIMARY KEY, display_name TEXT NOT NULL, normalized_name TEXT NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS paper_authors (
 paper_id INTEGER NOT NULL REFERENCES papers ON DELETE CASCADE,
 author_id INTEGER NOT NULL REFERENCES authors ON DELETE CASCADE,
 author_order INTEGER NOT NULL, is_first_author INTEGER NOT NULL DEFAULT 0,
 is_corresponding_author INTEGER NOT NULL DEFAULT 0, source TEXT NOT NULL,
 PRIMARY KEY (paper_id, author_id));
CREATE TABLE IF NOT EXISTS institution_groups (
 group_id INTEGER PRIMARY KEY, group_name TEXT NOT NULL, normalized_name TEXT NOT NULL);
CREATE INDEX IF NOT EXISTS idx_institution_groups_name ON institution_groups(normalized_name);
CREATE TABLE IF NOT EXISTS institutions (
 institution_id INTEGER PRIMARY KEY, institution_name TEXT NOT NULL,
 normalized_name TEXT NOT NULL,
 -- Two countries, because a multinational has both. `country_name_en` is where
 -- the affiliation sat (the site: Microsoft Research Asia is in China);
 -- `hq_country_name_en` is where the organisation is headquartered (Microsoft
 -- is American). ROR supplies the headquarters, the PDF supplies the site.
 country_name_en TEXT NOT NULL DEFAULT '',
 hq_country_name_en TEXT NOT NULL DEFAULT '',
 group_id INTEGER REFERENCES institution_groups(group_id),
 -- ROR-backed identity. `parent_name` is the research umbrella an institution
 -- rolls up to (Max Planck Society, Helmholtz, Chinese Academy of Sciences);
 -- ministries and governing boards are never eligible.
 ror_id TEXT NOT NULL DEFAULT '',
 parent_name TEXT NOT NULL DEFAULT '',
 parent_ror_id TEXT NOT NULL DEFAULT '',
 name_source TEXT NOT NULL DEFAULT '',
 source TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS institution_aliases (
 alias_id INTEGER PRIMARY KEY, raw_name TEXT NOT NULL, normalized_alias TEXT NOT NULL,
 institution_id INTEGER NOT NULL REFERENCES institutions(institution_id),
 UNIQUE(normalized_alias,institution_id));
CREATE TABLE IF NOT EXISTS paper_institutions (
 paper_id INTEGER NOT NULL REFERENCES papers ON DELETE CASCADE,
 institution_id INTEGER NOT NULL REFERENCES institutions ON DELETE CASCADE,
 raw_name TEXT NOT NULL, country_name TEXT, source TEXT NOT NULL, PRIMARY KEY (paper_id, institution_id));
-- Which author sat at which institution. `paper_institutions` is paper-level,
-- so a five-author paper with five affiliations read as though everyone sat
-- everywhere; the byline superscripts carry the real mapping and were being
-- discarded. `marker` keeps the printed label so a row can be checked against
-- the PDF, and `author_order` makes first-author attribution a query.
CREATE TABLE IF NOT EXISTS paper_author_institutions (
 paper_id INTEGER NOT NULL REFERENCES papers ON DELETE CASCADE,
 author_id INTEGER NOT NULL REFERENCES authors ON DELETE CASCADE,
 institution_id INTEGER NOT NULL REFERENCES institutions ON DELETE CASCADE,
 marker TEXT, author_order INTEGER, source TEXT NOT NULL,
 PRIMARY KEY (paper_id, author_id, institution_id));
CREATE INDEX IF NOT EXISTS idx_pai_author ON paper_author_institutions(author_id);
CREATE INDEX IF NOT EXISTS idx_pai_inst ON paper_author_institutions(institution_id);
-- Paper-to-paper connections. These are LLM claims, not bibliographic fact, so
-- they are kept apart from the publisher-verified tables and every row names
-- the model that asserted it — the registry's lesson was that derived data
-- stored as if it were ground truth becomes impossible to audit later.
--
-- They lived in nine `docs/{topic}/_paper_connections.json` files, one copy per
-- topic the two papers happened to share: 136,819 stored connections for 23,098
-- distinct pairs (83% duplication), 110 of them pointing at papers that no
-- longer exist, and unqueryable without loading every file.
--
-- `topics` records which topic views asserted the pair, so the per-topic JSON
-- the site builds from can still be regenerated from here.
CREATE TABLE IF NOT EXISTS paper_connections (
 paper_id INTEGER NOT NULL REFERENCES papers ON DELETE CASCADE,
 related_paper_id INTEGER NOT NULL REFERENCES papers ON DELETE CASCADE,
 relation TEXT NOT NULL, reason TEXT, topics TEXT, model TEXT,
 generated_at TEXT, source TEXT NOT NULL,
 PRIMARY KEY (paper_id, related_paper_id, relation));
CREATE INDEX IF NOT EXISTS idx_conn_related ON paper_connections(related_paper_id);
CREATE INDEX IF NOT EXISTS idx_conn_relation ON paper_connections(relation);
CREATE TABLE IF NOT EXISTS source_documents (
 paper_id INTEGER NOT NULL REFERENCES papers ON DELETE CASCADE, document_type TEXT NOT NULL,
 path TEXT NOT NULL, sha256 TEXT, bytes INTEGER, PRIMARY KEY (paper_id, document_type));
CREATE TABLE IF NOT EXISTS citation_snapshots (
 paper_id INTEGER NOT NULL REFERENCES papers ON DELETE CASCADE,
 observed_date TEXT NOT NULL, openalex_count INTEGER, crossref_count INTEGER,
 scopus_count INTEGER, normalized_percentile REAL,
 PRIMARY KEY (paper_id, observed_date));
CREATE TABLE IF NOT EXISTS citation_yearly (
 paper_id INTEGER NOT NULL REFERENCES papers ON DELETE CASCADE,
 citation_year INTEGER NOT NULL, source TEXT NOT NULL,
 citation_count INTEGER NOT NULL, retrieved_at TEXT NOT NULL,
 PRIMARY KEY (paper_id, citation_year, source));
CREATE INDEX IF NOT EXISTS idx_papers_doi ON papers(doi);
CREATE INDEX IF NOT EXISTS idx_papers_date ON papers(publication_date);
CREATE INDEX IF NOT EXISTS idx_authors_name ON authors(normalized_name);
CREATE INDEX IF NOT EXISTS idx_institutions_name ON institutions(normalized_name);
CREATE INDEX IF NOT EXISTS idx_citation_snapshots_date
 ON citation_snapshots(observed_date);
CREATE INDEX IF NOT EXISTS idx_citation_yearly_year
 ON citation_yearly(citation_year);
"""

PAPER_SCHEMA_COLUMNS = {
    "volume": "TEXT",
    "issue": "TEXT",
    "pages": "TEXT",
    "publisher": "TEXT",
    "issn": "TEXT",
    "eissn": "TEXT",
    "document_type": "TEXT",
    "scopus_eid": "TEXT",
    "received_date": "TEXT",
    "accepted_date": "TEXT",
    "published_online_date": "TEXT",
    "bibliography_source": "TEXT",
}
AFFILIATION_SCHEMA_VERSION = "affiliation-3"
def fresh_schema_origin_receipt_id(*, schema_version: str, registry_sha256: str,
                                   event_head: str, policy_version: str,
                                   source_sha256: str,
                                   contracts: dict[str, str] | None = None) -> str:
    """Return the deterministic immutable origin ID for a new affiliation schema."""
    origin = {
        "operation": "fresh-schema",
        "schema_version": schema_version,
        "registry_sha256": registry_sha256,
        "event_head": event_head,
        "policy_version": policy_version,
        "source_sha256": source_sha256,
        "contracts": dict(sorted((contracts or {}).items())),
    }
    return hashlib.sha256(json.dumps(
        origin, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")).hexdigest()
AFFILIATION_OBSERVATION_NAMESPACE = uuid.UUID("8d81aeb5-6231-5e97-8a65-cc9e5658bd22")
def canonical_affiliation_country(country: str = "", country_code: str = "",
                                  country_scope: str | None = None) -> tuple[str, str, str]:
    """Return the closed registry country projection; unknown input is never guessed."""
    resolve = country_map.country_resolution
    canonicalize = country_map.canonical_country
    for value in (country_code, country):
        if not value:
            continue
        if callable(resolve):
            state, code = resolve(value, country_scope=country_scope)
        elif callable(canonicalize):
            code = canonicalize(value, country_scope=country_scope)
            state = "present" if code else "unmappable"
        else:
            return "", "", "unknown"
        if state == "multinational":
            return "", "", "multinational"
        if state != "present" or not code:
            continue
        names = {
            alpha2: name for alpha2, _alpha3, name in country_map.ISO_3166_1_ROWS
        }
        name = names.get(code)
        if name:
            return code, name, "domestic"
    if country_scope == "multinational":
        return "", "", "multinational"
    return "", "", "unknown"

AFFILIATION_COHORT_DISPOSITION_SQL = """
CREATE TABLE IF NOT EXISTS affiliation_cohort_dispositions (
 cohort_sha256 TEXT NOT NULL, pending_id TEXT NOT NULL REFERENCES affiliation_pending_cases(pending_id) ON DELETE CASCADE,
 disposition TEXT NOT NULL CHECK(disposition IN
  ('RESOLVED','MANUAL_HOLD','IDENTITY_CONFLICT','AMBIGUOUS_HOMONYM',
   'COUNTRY_MISSING_OR_UNMAPPABLE','RELATIONSHIP_ONLY','EVIDENCE_STALE',
   'PROVIDER_OR_SECURITY_INCOMPLETE','NO_MATCH_OR_GENERIC')),
 decision_sha256 TEXT NOT NULL, decision_row_sha256 TEXT NOT NULL,
 evidence_segment_sha256 TEXT NOT NULL, decided_at TEXT NOT NULL,
 PRIMARY KEY(cohort_sha256,pending_id))
"""


AFFILIATION_METADATA_COLUMNS = {
    "registry_contract_version": "TEXT NOT NULL DEFAULT ''",
    "event_contract_version": "TEXT NOT NULL DEFAULT ''",
    "country_map_version": "TEXT NOT NULL DEFAULT ''",
    "country_map_sha256": "TEXT NOT NULL DEFAULT ''",
    "evidence_oracle_version": "TEXT NOT NULL DEFAULT ''",
    "evidence_oracle_sha256": "TEXT NOT NULL DEFAULT ''",
    "ledger_head": "TEXT NOT NULL DEFAULT ''",
    "cohort_version": "TEXT NOT NULL DEFAULT ''",
    "cohort_sha256": "TEXT NOT NULL DEFAULT ''",
    "relationship_set_sha256": "TEXT NOT NULL DEFAULT ''",
    "relationship_count": "INTEGER NOT NULL DEFAULT 0",
    "generation_descriptor_sha256": "TEXT NOT NULL DEFAULT ''",
    "generation_id": "TEXT NOT NULL DEFAULT ''",
}


def ensure_schema_migrations(conn: sqlite3.Connection) -> None:
    """Add bibliographic columns to databases created by earlier releases."""
    tables = {row[0] for row in conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table'")}
    if "papers" in tables:
        existing = {
            row[1] for row in conn.execute("PRAGMA table_info(papers)").fetchall()
        }
        for name, sql_type in PAPER_SCHEMA_COLUMNS.items():
            if name not in existing:
                conn.execute(f"ALTER TABLE papers ADD COLUMN {name} {sql_type}")
    if "institutions" in tables:
        existing = {row[1] for row in
                    conn.execute("PRAGMA table_info(institutions)").fetchall()}
        for name, sql_type in (("ror_id", "TEXT NOT NULL DEFAULT ''"),
                               ("hq_country_name_en", "TEXT NOT NULL DEFAULT ''"),
                               ("parent_name", "TEXT NOT NULL DEFAULT ''"),
                               ("parent_ror_id", "TEXT NOT NULL DEFAULT ''"),
                               ("name_source", "TEXT NOT NULL DEFAULT ''")):
            if name not in existing:
                conn.execute(
                    f"ALTER TABLE institutions ADD COLUMN {name} {sql_type}")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_institutions_parent "
                     "ON institutions(parent_name)")



def ensure_legacy_institution_schema(conn: sqlite3.Connection) -> None:
    """Rebuild legacy compatibility tables without global name uniqueness."""
    existing_tables = {
        row[0] for row in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table'")
    }
    institution_columns = {
        row[1] for row in conn.execute("PRAGMA table_info(institutions)")
    }
    group_columns = {
        row[1] for row in conn.execute("PRAGMA table_info(institution_groups)")
    }
    alias_sql_row = conn.execute(
        "SELECT sql FROM sqlite_master WHERE type='table' "
        "AND name='institution_aliases'").fetchone()
    institution_sql_row = conn.execute(
        "SELECT sql FROM sqlite_master WHERE type='table' "
        "AND name='institutions'").fetchone()
    alias_sql = alias_sql_row[0] if alias_sql_row else ""
    institution_sql = institution_sql_row[0] if institution_sql_row else ""
    if ({"country_name_en"} <= institution_columns
            and "organization_id" not in institution_columns
            and "normalized_nameTEXTNOTNULLUNIQUE" not in re.sub(
                r"\s+", "", institution_sql)
            and "UNIQUE" in alias_sql.upper()
            and "normalized_alias,institution_id" in re.sub(
                r"\s+", "", alias_sql)):
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_institutions_identity "
            "ON institutions(normalized_name,country_name_en)")
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_institution_groups_name "
            "ON institution_groups(normalized_name)")
        return

    def rows(table: str) -> list[dict]:
        if table not in existing_tables:
            return []
        cursor = conn.execute(f'SELECT * FROM "{table}"')
        names = [item[0] for item in cursor.description]
        return [dict(zip(names, row)) for row in cursor.fetchall()]

    groups = rows("institution_groups")
    institutions = rows("institutions")
    aliases = rows("institution_aliases")
    links = rows("paper_institutions")
    for table in (
            "paper_institutions", "institution_aliases", "institutions",
            "institution_groups"):
        if table in existing_tables:
            conn.execute(f'DROP TABLE "{table}"')
    compatibility_schema = """
        CREATE TABLE institution_groups (
          group_id INTEGER PRIMARY KEY, group_name TEXT NOT NULL,
          normalized_name TEXT NOT NULL);
        CREATE INDEX idx_institution_groups_name
          ON institution_groups(normalized_name);
        CREATE TABLE institutions (
          institution_id INTEGER PRIMARY KEY, institution_name TEXT NOT NULL,
          normalized_name TEXT NOT NULL, country_name_en TEXT NOT NULL DEFAULT '',
          group_id INTEGER REFERENCES institution_groups(group_id),
          ror_id TEXT NOT NULL DEFAULT '',
  hq_country_name_en TEXT NOT NULL DEFAULT '',
          parent_name TEXT NOT NULL DEFAULT '',
          parent_ror_id TEXT NOT NULL DEFAULT '',
          name_source TEXT NOT NULL DEFAULT '',
          source TEXT NOT NULL);
        CREATE INDEX idx_institutions_identity
          ON institutions(normalized_name,country_name_en);
        CREATE TABLE institution_aliases (
          alias_id INTEGER PRIMARY KEY, raw_name TEXT NOT NULL,
          normalized_alias TEXT NOT NULL,
          institution_id INTEGER NOT NULL REFERENCES institutions(institution_id),
          UNIQUE(normalized_alias,institution_id));
        CREATE TABLE paper_institutions (
          paper_id INTEGER NOT NULL REFERENCES papers ON DELETE CASCADE,
          institution_id INTEGER NOT NULL REFERENCES institutions ON DELETE CASCADE,
          raw_name TEXT NOT NULL, country_name TEXT, source TEXT NOT NULL,
          PRIMARY KEY (paper_id,institution_id));
    """
    for statement in compatibility_schema.split(";"):
        if statement.strip():
            conn.execute(statement)
    for row in groups:
        conn.execute(
            "INSERT INTO institution_groups VALUES (?,?,?)",
            (row.get("group_id"), row.get("group_name", ""),
             row.get("normalized_name", "")))
    for row in institutions:
        conn.execute(
            "INSERT INTO institutions (institution_id,institution_name,"
            "normalized_name,country_name_en,group_id,source) "
            "VALUES (?,?,?,?,?,?)",
            (row.get("institution_id"),
             row.get("institution_name") or row.get("normalized_name", ""),
             row.get("normalized_name", ""),
             row.get("country_name_en", ""), row.get("group_id"),
             row.get("source", "legacy")))
    for row in aliases:
        conn.execute(
            "INSERT OR IGNORE INTO institution_aliases VALUES (?,?,?,?)",
            (row.get("alias_id"), row.get("raw_name", ""),
             row.get("normalized_alias", ""), row.get("institution_id")))
    for row in links:
        conn.execute(
            "INSERT OR IGNORE INTO paper_institutions VALUES (?,?,?,?,?)",
            (row.get("paper_id"), row.get("institution_id"),
             row.get("raw_name", ""), row.get("country_name", ""),
             row.get("source", "legacy")))

def norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip()).casefold()

INSTITUTION_ENGLISH_ALIASES_PATH = (
    Path(__file__).with_name("institution_english_aliases.json")
)
try:
    INSTITUTION_ENGLISH_ALIASES = json.loads(
        INSTITUTION_ENGLISH_ALIASES_PATH.read_text(encoding="utf-8"))
except (OSError, ValueError):
    INSTITUTION_ENGLISH_ALIASES = {}
_INSTITUTION_ENGLISH_ALIASES_BY_NORM = {
    norm(source): target
    for source, target in INSTITUTION_ENGLISH_ALIASES.items()
}
LOCAL_LANGUAGE_INSTITUTION_RE = re.compile(
    r"Universität|Universitaet|Université|Università|Universidad|"
    r"Universidade|Universiteit|Universitat|Universitatea|Universitet(?:et)?|"
    r"Uniwersytet|Universitas|Universitäts|Hochschule|Akademie|"
    r"Gesellschaft|Institut für|\bInstitut\b|École|Ecole|"
    r"Institut national|Centre national|Politecnico|Politécnica|"
    r"\bIstituto\b|\bScuola\b|\bConsiglio\b|\bInstituto\b|"
    r"\bConsejo\b|\bFundação\b|\bFundacion\b|\bFundación\b|"
    r"Forschungs|Zentrum für|Bundesanstalt|Laboratoire|Ospedale|"
    r"Institutet|Akademia|Instituto Superior Técnico|[А-Яа-яЁё]",
    re.I,
)


def is_local_language_institution(name: str) -> bool:
    return bool(LOCAL_LANGUAGE_INSTITUTION_RE.search(name or ""))


def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def fm(path: Path) -> dict:
    try:
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            return {}
        end = text.find("\n---", 3)
        if end < 0:
            return {}
        import yaml
        value = yaml.safe_load(text[4:end]) or {}
        return value if isinstance(value, dict) else {}
    except Exception:
        return {}


# What counts as a DOI now lives in `lib/doi.py`, because every boundary that
# accepts one has to agree. Keeping the rule here meant `build_papers_index.py`
# had its own answer: 715 of the 1,762 DOI values in `_papers_index.json` are
# not DOIs — "N/A" on 123 papers, "미제공" on 57 — and one is the template
# string `10.1007/sxxxxx-yyy-zzzz-1`.
_DOI_PATTERN = _doi.DOI_PATTERN
clean_doi = _doi.clean_doi
clean_arxiv = _doi.clean_arxiv


def arxiv_from(*values: str) -> str:
    for value in values:
        value = str(value or "")
        m = re.search(r"(?:arxiv:|arxiv\.org/(?:abs|pdf)/|10\.48550/arxiv\.)([0-9]{4}\.[0-9]{4,5}(?:v\d+)?)", value, re.I)
        if m:
            return m.group(1)
    return ""


def external_url(doi: str, arxiv: str) -> str:
    if doi:
        return "https://doi.org/" + doi
    if arxiv:
        return "https://arxiv.org/abs/" + arxiv
    return ""


def request_json(url: str, headers: dict | None = None, timeout: int = 30) -> dict:
    req = urllib.request.Request(url, headers=headers or {"User-Agent": f"paper-curation/1.0 (mailto:{MAILTO})"})
    with urllib.request.urlopen(req, timeout=timeout, context=SSL_CTX) as r:
        return json.load(r)

_ROR_ENGLISH_CACHE_PATH = ROOT / ".cache" / "ror_english_aliases.json"
_ROR_ENGLISH_CACHE = None


def _load_ror_english_cache() -> dict:
    global _ROR_ENGLISH_CACHE
    if _ROR_ENGLISH_CACHE is None:
        try:
            _ROR_ENGLISH_CACHE = json.loads(
                _ROR_ENGLISH_CACHE_PATH.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            _ROR_ENGLISH_CACHE = {}
    return _ROR_ENGLISH_CACHE


def resolve_english_institution(name: str, country: str = "",
                                *, allow_remote: bool = False,
                                offline: bool = False) -> str:
    """Resolve a local-language organization label to an English ROR label."""
    name = re.sub(r"\s+", " ", name or "").strip(" ,;:-")
    static = _INSTITUTION_ENGLISH_ALIASES_BY_NORM.get(norm(name))
    if static:
        return static
    if not is_local_language_institution(name) or not allow_remote or offline:
        return ""

    cache = _load_ror_english_cache()
    cache_key = norm(name) + "|" + norm(country)
    if cache_key in cache:
        return str(cache[cache_key] or "")

    resolved = ""
    try:
        query = urllib.parse.urlencode({"query": name})
        payload = request_json(
            "https://api.ror.org/v2/organizations?" + query, timeout=30)
        wanted = norm(name)
        wanted_country = norm(country)
        for item in payload.get("items") or []:
            names = item.get("names") or []
            if wanted not in {
                    norm(str(candidate.get("value") or ""))
                    for candidate in names}:
                continue
            locations = item.get("locations") or [{}]
            ror_country = norm(str(
                (locations[0].get("geonames_details") or {}).get(
                    "country_name") or ""))
            if wanted_country and ror_country != wanted_country:
                continue
            english = [
                str(candidate.get("value") or "") for candidate in names
                if candidate.get("lang") == "en"
                and ("ror_display" in (candidate.get("types") or [])
                     or "label" in (candidate.get("types") or []))
            ]
            if not english:
                english = [
                    str(candidate.get("value") or "") for candidate in names
                    if candidate.get("lang") == "en"
                    and "alias" in (candidate.get("types") or [])
                ]
            resolved = next(
                (candidate for candidate in english
                 if candidate and not is_local_language_institution(candidate)),
                "")
            if resolved:
                break
    except Exception:
        resolved = ""

    cache[cache_key] = resolved
    try:
        _ROR_ENGLISH_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
        temp = _ROR_ENGLISH_CACHE_PATH.with_suffix(".tmp")
        temp.write_text(
            json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
        os.replace(temp, _ROR_ENGLISH_CACHE_PATH)
    except OSError:
        pass
    return resolved


def date_from_header(header: str) -> str:
    months = {"January":"01","February":"02","March":"03","April":"04","May":"05","June":"06",
              "July":"07","August":"08","September":"09","October":"10","November":"11","December":"12"}
    m = re.search(r"\b(\d{1,2})\s+(" + "|".join(months) + r")\s+((?:19|20)\d{2})\b", header)
    return f"{m.group(3)}-{months[m.group(2)]}-{int(m.group(1)):02d}" if m else ""


def resolve_publication(title: str, doi: str, arxiv: str) -> dict:
    """Return formal DOI/journal/date when a publisher record is found."""
    if doi and not doi.lower().startswith("10.48550/arxiv."):
        try:
            data = request_json("https://api.openalex.org/works/https://doi.org/" + urllib.parse.quote(doi, safe="/"))
            return openalex_record(data, "openalex")
        except Exception:
            pass
    queries = [title]
    if arxiv:
        queries.insert(0, "")
    for query in queries:
        if not query:
            continue
        try:
            url = "https://api.openalex.org/works?per-page=5&search=" + urllib.parse.quote(query)
            results = request_json(url).get("results", [])
            target = norm(title)
            for item in results:
                if norm(item.get("title", "")) == target:
                    rec = openalex_record(item, "openalex-title")
                    if rec.get("doi") and not rec["doi"].lower().startswith("10.48550/arxiv."):
                        return rec
        except Exception:
            continue
    return {}


def openalex_record(item: dict, source: str) -> dict:
    loc = item.get("primary_location") or {}
    source_obj = loc.get("source") or {}
    doi = clean_doi(item.get("doi", ""))
    if doi.lower().startswith("10.48550/arxiv."):
        doi = ""
    return {"doi": doi, "journal": source_obj.get("display_name", "") or "",
            "date": item.get("publication_date", "") or "", "source": source}


# Frontiers, Hindawi and PeerJ print the handling editor and the peer reviewers,
# with their affiliations, above the author byline:
#
#     EDITED BY
#     Qiuyou Xie, Southern Medical University, China
#     REVIEWED BY
#     Mani Abdul Karim, XIM University, India
#     Linghui Dong, Shandong University, China
#
# Those are other people's employers. Reading them as author affiliations put
# Southern Medical University and Shandong University on a paper written
# entirely in Nantong — 49 such links across 29 papers. A block runs until the
# next front-matter heading.
_EDITORIAL_HEADS = (
    r"EDITED\s+BY|REVIEWED\s+BY|ACADEMIC\s+EDITOR|HANDLING\s+EDITOR|"
    r"SECTION\s+EDITOR|ASSOCIATE\s+EDITOR")
_EDITORIAL_BLOCK = re.compile(
    rf"(?ims)^\s*#*\s*(?:{_EDITORIAL_HEADS})\s*:?\s*$.*?"
    rf"(?=^\s*#*\s*(?:{_EDITORIAL_HEADS}|\*?CORRESPONDENCE|RECEIVED|ACCEPTED|"
    r"PUBLISHED|CITATION|COPYRIGHT|ABSTRACT|KEYWORDS|TYPE\b|OPEN\s+ACCESS)|\Z)")
_EDITORIAL_INLINE = re.compile(
    rf"(?im)^\s*#*\s*(?:{_EDITORIAL_HEADS})\b.*$")


def _strip_editorial_blocks(text: str) -> str:
    """Remove journal editor/reviewer credits from a front-matter window."""
    return _EDITORIAL_INLINE.sub("", _EDITORIAL_BLOCK.sub("\n", text))


# Superscript affiliation markers. The digit may be glued to the next word
# ("2Princeton") or spaced off it ("5 UC Berkeley"), and must not fire inside a
# legitimate name ("L3S", "Bio21", "LIP6").
# Suit symbols key ACL affiliation blocks the way digits key everyone
# else's ("♣University of Illinois at Urbana-Champaign").
_AFFILIATION_MARKER = re.compile(
    r"(?=(?<![A-Za-z0-9])(?:[1-9]\d?|[♣♢♡♠◊△▽○●□■◆★])\s*[A-Z])")


def _split_marked_affiliations(line: str) -> list[str]:
    """Break a byline that packs several affiliations onto one line."""
    return [piece.strip() for piece in _AFFILIATION_MARKER.split(line)
            if piece.strip()]


# A byline carries the author-to-affiliation mapping in its superscripts:
#
#     Xi-Chen Wang1,2†, Di Zhu1,3†, Jun Lu1,3, … Bao-Guo Xu4 and Wei-Guan Chen1,3*
#     1Department of Rehabilitation Medicine, Nantong First People's Hospital, …
#     2Affiliated Teaching Hospital of Kangda College, Nanjing Medical University, …
#
# `paper_institutions` flattens that away, so a paper reads as though every
# author sat at every institution. Recovering the markers is what makes
# first-author attribution possible.
# Markers attach to a name in every layout a publisher can invent:
#
#     Miao Li1 Jey Han Lau1 Eduard Hovy1,2      glued
#     Agustinus Kristiadi 1 Felix Strieth 2     spaced
#     Sitong Li ,1 Stefano Padilla ,1           comma left by a stripped ORCID
#     Mike Chantler *,1                         correspondence star first
#
# The previous parser demanded the glued form and read only the end of a
# chunk, so it mapped one author per byline and refused the other three
# layouts: 310 of 400 sampled papers had markers it could not see, and every
# one of them fell back to linking every author to every institution.
# Not every publisher numbers its affiliations. ACL templates key them with
# suit symbols — "Yu Zhang♣∗, Xiusi Chen♢♣∗" against "♣University of Illinois
# at Urbana-Champaign" — and reading only digits left those papers with no
# mapping at all. `∗` and `†` are excluded from the alphabet on purpose: they
# mark equal contribution and correspondence, not an affiliation, and they sit
# beside the real markers in exactly these bylines.
_MARKER_SYMBOLS = "♣♢♡♠◊△▽○●□■◆★§¶"
_MARKER_ATOM = r"(?:\d{1,2}|[" + _MARKER_SYMBOLS + r"])"
_MARKER_RUN = r"(" + _MARKER_ATOM + r"(?:\s*,?\s*" + _MARKER_ATOM + r")*)"
_MARKER_AFTER_NAME = re.compile(
    r"[\s,]*[†‡*∗⋆]*[\s,]*" + _MARKER_RUN)
_MARKER_HEAD = re.compile(r"^(" + _MARKER_ATOM + r")\s*(.+)$")


_LIGATURES = str.maketrans({
    "æ": "ae", "Æ": "AE", "ø": "o", "Ø": "O", "ß": "ss",
    "œ": "oe", "Œ": "OE", "ł": "l", "Ł": "L", "đ": "d",
    "Đ": "D", "þ": "th", "Þ": "TH", "ð": "d", "Ð": "D",
    "ı": "i", "ŧ": "t", "ħ": "h",
})
_SPACING_ACCENTS = {ord(ch): None for ch in
                    "\u00a8\u00b4\u0060\u005e\u02c6\u02dc"
                    "\u00af\u02da\u02dd\u02d8\u02c7\u00b0"}


def _fold(token: str) -> str:
    """ASCII-folded, case-insensitive key for a name token.

    Zotero transcribes the publisher's diacritics ("Jun Lü") while the PDF
    byline is often stripped ("Jun Lu4"); without folding every such author
    loses their affiliation.
    """
    # A PDF may print the accent as a *spacing* character before the letter —
    # "G¨atzner" for "Gätzner". This runs before NFKD on purpose: NFKD expands
    # U+00A8 into a space plus a combining mark, and the space would then split
    # the surname in two. They never occur inside a real name.
    folded = (token or "").translate(_SPACING_ACCENTS)
    # NFKD does not touch these: they are letters in their own right, not
    # composed characters. A PDF prints "Biskjaer" where Zotero records
    # "Biskjær", and without this the two are different people.
    folded = folded.translate(_LIGATURES)
    folded = unicodedata.normalize("NFKD", folded)
    folded = "".join(ch for ch in folded if not unicodedata.combining(ch))
    return folded.lower().strip(".,'\u2019-")


# Joining a marker to an institution row is a name-matching problem, and it was
# being done with `raw[:60] in label`. That fails on everything a PDF does to a
# name: a line-break hyphen ("Indian Institute of Technology Roor- kee"), a
# department prefix present on one side only, a comma that moved. 141 papers
# read their markers and their affiliation block and then matched nothing.
_AFFILIATION_STOPWORDS = frozenset({
    "of", "the", "and", "for", "at", "in", "de", "da", "di", "du", "des",
    "der", "und", "dept", "department", "departments", "div", "division",
    "school", "faculty", "college", "unit", "group", "team", "lab",
    "laboratory", "laboratories", "center", "centre", "institute", "institut",
    "university", "universite", "universitat", "universidad", "universita",
    "state", "national", "research", "science", "sciences", "technology",
    "engineering", "usa", "uk", "china", "korea", "japan", "germany",
    "france", "canada", "india", "singapore", "australia", "city", "campus",
})


def _affiliation_tokens(value: str) -> set[str]:
    """Comparable tokens for an affiliation string.

    A PDF breaks words across lines with a hyphen, so "Roor- kee" and
    "Roorkee" have to become one token before anything is compared.
    """
    # A label still carries the marker it was split on ("4Indian Institute…"),
    # which would glue to the first word and make it a different token. Only a
    # *leading* marker is removed, so "LIP6" and "Bio21" keep their digits.
    value = re.sub(r"^\s*(?:\d{1,2}|[" + _MARKER_SYMBOLS + r"])\s*", "",
                   value or "")
    folded = _fold(value)
    folded = re.sub(r"[-\u2010-\u2015]\s+", "", folded)      # re-join "Roor- kee"
    return {token for token in re.findall(r"[a-z0-9]+", folded)
            if len(token) >= 3 and token not in _AFFILIATION_STOPWORDS}


def affiliation_match_score(left: str, right: str) -> float:
    """How strongly two affiliation strings name the same organisation.

    Containment rather than Jaccard: one side is often the byline's short form
    ("Vanderbilt University") and the other the full postal string, so the
    smaller set being contained in the larger is the signal.
    """
    a, b = _affiliation_tokens(left), _affiliation_tokens(right)
    if not a or not b:
        return 0.0
    shared = a & b
    # A label can stop mid-word where the PDF broke the line and the
    # continuation stayed behind: "Northwest Polytechni-" against "Northwest
    # Polytechni- cal University". The truncated token is a prefix of the whole
    # one, and five characters is long enough that a prefix is not a
    # coincidence between two different organisations.
    for short in a - shared:
        if len(short) >= 5 and any(long.startswith(short) for long in b - shared):
            shared = shared | {short}
    for short in b - shared:
        if len(short) >= 5 and any(long.startswith(short) for long in a - shared):
            shared = shared | {short}
    return len(shared) / min(len(a), len(b))


# Below this, two strings are different organisations. Measured here: a genuine
# pair ("Vanderbilt University" against "Department of Computer Science,
# Vanderbilt University, Nashville, TN") scores 1.0.
AFFILIATION_MATCH_FLOOR = 0.60


def best_institution_for(label: str, institutions) -> int | None:
    """The institution row a marker's text names, or None if none is close.

    Taking the first row whose 60-character prefix happened to appear was both
    too strict — any drift broke it — and too loose, since a shared prefix like
    "Department of Computer Science," matched the wrong row.
    """
    best, best_score = None, 0.0
    for institution_id, raw in institutions:
        score = affiliation_match_score(raw or "", label)
        if score > best_score:
            best, best_score = institution_id, score
    return best if best_score >= AFFILIATION_MATCH_FLOOR else None


# Which characters a paper keys its affiliations with cannot be fixed in
# advance. "Architecture Design for Human-Driven Systems" writes
#
#     Mahyar T. Moghaddam∗, Moamin B. Abughazala†, ...
#     ∗MMMI Institute, University of Southern Denmark
#     †DISIM Department, University of L'Aquila
#
# where ∗ and † are the affiliation markers, while an ACL paper writes "Yu
# Zhang♣∗" and there ∗ means equal contribution. The same character, opposite
# roles. Excluding ∗ and † by rule read one correctly and lost the other, so
# the alphabet is read off the affiliation block instead: whatever a line
# naming an organisation begins with is a marker in *this* paper.
_CANDIDATE_MARKER = re.compile(
    r"^(\d{1,2}|[a-j]|[*∗†‡§¶⋆♣♢♡♠◊△▽○●□■◆★])\s*\.?\s*(?=[A-Z])(.+)$")


def _marker_regexes(alphabet: set[str]):
    """(trailing-marker stripper, marker-run reader) for one paper's alphabet.

    Built per paper because the alphabet is: `a` keys the affiliations of a
    PNAS article and is an ordinary letter everywhere else.
    """
    # Expanded by class, not by character. A block usually shows an
    # organisation cue on only some of its lines, so seeing "1" is evidence
    # that this paper numbers its affiliations — not that 2 and 3 are
    # something else. Restricting to the exact characters found cost 330
    # papers their mapping. Symbols stay literal: that is where the
    # discrimination lives, since ∗ is a marker in one template and equal
    # contribution in another.
    atoms = []
    if any(atom.isdigit() for atom in alphabet):
        atoms.append(r"\d{1,2}")
    if any(atom.isalpha() and atom.islower() for atom in alphabet):
        atoms.append(r"[a-j]")
    symbols = sorted(atom for atom in alphabet
                     if not atom.isdigit() and not atom.isalpha())
    atoms.extend(re.escape(symbol) for symbol in symbols)
    alternation = "|".join(atoms)
    singles = "".join(re.escape(symbol) for symbol in symbols)
    if any(atom.isalpha() and atom.islower() for atom in alphabet):
        singles += "a-j"
    # Digits come off too: PNAS writes "Waya,1" where `a` is the affiliation
    # and `1` marks the corresponding author. Either way they hide the surname.
    # Whatever trails a name has to come off before the surname can be
    # matched, marker or not: "Yu Zhang♣∗" ends in an equal-contribution star
    # that is deliberately absent from this paper's alphabet.
    trailing = re.compile(r"[" + singles + r"\d,*∗†‡§¶⋆]+$")
    # An equal-contribution star can stand between the name and the marker
    # ("Seungik Cho * 1"). Decorations this paper does *not* use as markers are
    # skipped; ones it does are left for the run itself to read.
    skip = "".join(ch for ch in "*∗†‡§¶⋆♦♢♣♡♠◊△▽○●□■◆★"
                   if ch not in alphabet)
    lead = r"[\s,]*" + (r"[" + re.escape(skip) + r"]*" if skip else "") + r"[\s,]*"
    run = re.compile(lead + r"((?:" + alternation + r")"
                     r"(?:\s*,?\s*(?:" + alternation + r"))*)")
    return trailing, run


# Lines that begin like an affiliation but are not one.
_NOT_AN_AFFILIATION = re.compile(
    r"(?i)^(?:equal(?:ly)? contribut|these authors|corresponding|work done|"
    r"now at|shared|joint first)")


def infer_marker_alphabet(text: str) -> set[str]:
    """The marker characters this paper's affiliation block actually uses.

    Two passes. A marker followed by an organisation name is proof, and it is
    also what identifies the block; once the block is known, its sibling lines
    contribute their markers too. "♣Ubiquitous Knowledge Processing Lab (UKP
    Lab)" names no word the organisation cue lists, so demanding proof of every
    line dropped ♣ and cost the paper its first author.

    Splitting each line first keeps "*Equal contribution 1Department of
    Mathematics, ETH" from nominating the star: the marker it hides is the 1.
    """
    proven: set[str] = set()
    seen: set[str] = set()
    for line in text.splitlines():
        line = re.sub(r"^#+\s*", "", line).strip()
        if not line:
            continue
        for piece in _split_marked_affiliations(line):
            piece = piece.strip()
            head = _CANDIDATE_MARKER.match(piece)
            if not head or _SECTION_HEADING.match(piece):
                continue
            body = head.group(2)
            if _NOT_AN_AFFILIATION.match(body):
                continue
            seen.add(head.group(1))
            if _AFFILIATION_ORG_CUE.search(body):
                proven.add(head.group(1))
    if not proven:
        return set()
    # Only markers of the same kind: a proven symbol does not make a stray
    # digit elsewhere in the document a marker.
    kinds = {_marker_kind(marker) for marker in proven}
    return proven | {marker for marker in seen
                     if _marker_kind(marker) in kinds}


def _marker_kind(marker: str) -> str:
    if marker.isdigit():
        return "digit"
    return "letter" if marker.isalpha() else "symbol"


def _split_marker_run(run: str) -> list[str]:
    """"1,2" is two markers and so is "♢♣" — but "12" is one.

    Symbols are written without a separator, digits are not, so only the
    symbol runs are split character by character.
    """
    out = []
    # "1 2" is two markers spaced apart; "12" is one number. Splitting on
    # whitespace as well as commas is what separates them — read as one token,
    # "1 2" matched no affiliation and cost 94 papers their mapping.
    for piece in re.split(r"[,\s]+", run):
        piece = piece.strip()
        if not piece:
            continue
        if piece[0].isdigit():
            out.append(piece)
        else:
            out.extend(ch for ch in piece if not ch.isspace())
    return out


def _byline_candidates(raw_header: str, surnames: set[str],
                       trailing=None) -> list[str]:
    """Lines that carry at least two of this paper's own author surnames.

    Counting digits was the old test, and an affiliation block passes it
    ("1Heriot-Watt University, Edinburgh, UK 2Ocean University"). The author
    list is already in hand, so it is the far better discriminator.

    Neighbouring lines are also offered joined, because a wide byline wraps
    and the wrap can fall between a name and its marker:

        Yoel Zimmermann
        1, Adib Bazgir

    Read line by line, Zimmermann has no marker and the mapping is lost for a
    22-institution collaboration. Joined, the pair reads like any other byline.
    """
    def strip(token: str) -> str:
        # The same stripper the marker reader uses, so a line cannot be
        # rejected here and then parsed successfully there.
        return (trailing.sub("", token) if trailing else
                re.sub(r"[\d†‡§¶*∗⋆,♣♢♡♠◊△▽○●□■◆★]+$", "", token))

    def score(text: str) -> int:
        return sum(1 for token in re.split(r"[\s,;]+", text)
                   if _fold(token) in surnames or _fold(strip(token)) in surnames)

    lines = [re.sub(r"^#+\s*", "", line).strip()
             for line in raw_header.splitlines()]
    lines = [line for line in lines if line and len(line) <= 600]

    out = []
    for index, line in enumerate(lines):
        hits = score(line)
        if hits >= 2:
            out.append((hits, line))
        if index + 1 < len(lines):
            joined = f"{line} {lines[index + 1]}"
            if len(joined) <= 600 and score(joined) > max(hits, 1):
                out.append((score(joined), joined))
    # A byline can also set one author per line:
    #
    #     Homer Walke1
    #     Kevin Black1
    #     Moo Jin Kim2
    #
    # No single line then holds two surnames and every one of them is
    # discarded. Consecutive one-name lines are gathered into a byline of
    # their own. Only the header is searched, so a reference list — where
    # names also stand one per line — is never reached.
    run: list[str] = []
    for line in lines + [""]:
        if line and score(line) == 1 and len(line) <= 80:
            run.append(line)
            continue
        if len(run) >= 2:
            gathered = " ".join(run)
            if len(gathered) <= 600:
                out.append((len(run), gathered))
        run = []
    out.sort(key=lambda pair: -pair[0])
    return [text for _, text in out]


def author_affiliation_markers(raw_header: str, authors,
                               alphabet: set[str] | None = None
                               ) -> dict[str, list[str]]:
    """Map each author name to the affiliation markers printed after it.

    Anchored on the surnames this paper actually has rather than on chunk
    boundaries, so every author on the line is read, not just the last one.
    """
    if isinstance(authors, str):
        authors = [x.strip() for x in re.split(r"[,;]", authors) if x.strip()]

    surnames: dict[str, str] = {}
    for name in authors or []:
        parts = [p for p in re.split(r"\s+", str(name).strip()) if p]
        if parts:
            surnames.setdefault(_fold(parts[-1]), str(name))
    if not surnames:
        return {}

    trailing, run = (_marker_regexes(alphabet) if alphabet
                     else (None, _MARKER_AFTER_NAME))

    mapping: dict[str, list[str]] = {}
    for byline in _byline_candidates(raw_header, set(surnames), trailing):
        for token_match in re.finditer(r"[^\s,;]+", byline):
            token = token_match.group(0)
            # The marker may be glued to the surname ("Li1", "Hovy1,2"), so the
            # token is not the name. Strip the trailing marker characters and
            # read the markers from exactly where the name ends — that one
            # position is what makes the glued and spaced layouts the same
            # problem instead of two.
            # The whole token may already be the surname ("Costa" under an
            # alphabet containing "a"), so it is tried before anything is
            # stripped off the end.
            core = token
            resolved = surnames.get(_fold(core))
            if not resolved:
                core = ((trailing.sub("", token) if trailing else
                         re.sub(r"[\d†‡§¶*∗⋆,♣♢♡♠◊△▽○●□■◆★]+$", "", token)))
                if not core:
                    continue
                resolved = surnames.get(_fold(core))
            if not resolved or resolved in mapping:
                continue
            tail = run.match(byline, token_match.start() + len(core))
            if not tail:
                continue
            markers = _split_marker_run(tail.group(1))
            if markers:
                mapping[resolved] = markers
        if mapping:
            break
    return mapping


def affiliation_window(text_path: Path) -> str:
    """A wider slice of `text.md` for reading the marker→affiliation block.

    `extract_header` stops at the abstract, which is right for finding the
    byline and wrong for finding what the byline points at: two-column
    conference layouts print the affiliations as a page-one footnote, so
    PyMuPDF emits them *after* the abstract. 171 of 200 sampled papers had
    their author→marker map read successfully and then no marker→affiliation
    block to join it to.
    """
    try:
        text = text_path.read_text(encoding="utf-8", errors="replace")[:24000]
    except OSError:
        return ""
    lines = []
    for line in text.splitlines():
        head = re.match(r"^\s*[-–—]?\s*(\d+)\s+(.*)$", line)
        if head and not _ORGANISATION_CUES.search(head.group(2)[:80]):
            line = head.group(2)
        line = re.sub(r"\s+", " ", line).strip()
        if line:
            lines.append(line)
    return "\n".join(_strip_editorial_blocks("\n".join(lines[:320])).splitlines())


_EMAIL_LINE = re.compile(r"[\w.+-]+@[\w.-]+|@\s*[\w.-]+\.\w+")
_FRONT_MATTER_END = re.compile(
    r"(?i)^\s*(?:abstract|초록|keywords?|index terms|introduction|"
    r"1\.?\s+introduction|ccs concepts|acm reference)\b")


def stacked_author_affiliations(raw_header: str, authors) -> dict[str, str]:
    """Bylines that stack each author's affiliation under the author's name.

    arXiv and IEEE templates set the authors in columns with no markers at
    all, and PyMuPDF reads them column by column:

        Aditi Singh
        Department of Computer Science
        Cleveland State University
        Cleveland, OH, USA
        a.singh22@csuohio.edu
        Abul Ehtesham
        The Davey Tree Expert Company
        ...

    Nothing here is a superscript, so the marker machinery finds nothing and
    the paper is filed as "the PDF does not say" — while the PDF says it
    plainly. The affiliation is the run of lines between a name and the next
    name, stopping at the author's e-mail or at the abstract.

    Two authors must be found this way before any of it is believed: one name
    followed by a line mentioning a university is a coincidence, four in a row
    is a byline.
    """
    if isinstance(authors, str):
        authors = [x.strip() for x in re.split(r"[,;]", authors) if x.strip()]
    # Zotero abbreviates: the byline reads "Tala Talaei Khoei" while the
    # record says "T. T. Khoei", so the surname is what can be compared.
    by_surname: dict[str, str] = {}
    for name in authors or []:
        parts = [p for p in re.split(r"\s+", str(name).strip()) if p]
        if parts:
            by_surname.setdefault(_fold(parts[-1]), str(name))
    if not by_surname:
        return {}

    def author_on(line: str) -> str | None:
        """The author this line names, if the line is a name and not a place."""
        tokens = [x for x in re.split(r"\s+", line) if x]
        if not (1 < len(tokens) <= 5) or _AFFILIATION_ORG_CUE.search(line):
            return None
        if any(ch.isdigit() for ch in line) or "," in line:
            return None
        # "Daking Rai∗" — the correspondence mark is part of the token.
        return by_surname.get(
            _fold(tokens[-1].strip(".,*∗†‡§¶⋆♣♢♡♠")))

    lines = [line.strip() for line in raw_header.splitlines()]
    out: dict[str, str] = {}
    for index, line in enumerate(lines):
        resolved = author_on(line)
        if not resolved or resolved in out:
            continue
        block, email = [], ""
        for follower in lines[index + 1:index + 7]:
            if not follower or _FRONT_MATTER_END.match(follower):
                break
            if author_on(follower):
                break
            # An e-mail is never an affiliation, but it is not the end of the
            # block either: this template right-aligns it beside the name, so
            # PyMuPDF emits name, e-mail, affiliation in that order.
            if _EMAIL_LINE.search(follower):
                email = email or _EMAIL_LINE.search(follower).group(0)
                continue
            block.append(follower)
        text = ", ".join(block).strip(" ,")
        if text and _AFFILIATION_ORG_CUE.search(text):
            out[resolved] = text
        elif email:
            # Some templates print only the address: "Grégoire Mialon" then
            # "gmialon@meta.com" and straight on to the next author. The
            # caller resolves the domain against the paper's own institutions.
            out[resolved] = email
    return out if len(out) >= 2 else {}


def _marker_emails(raw_text: str, wanted: set[str] | None,
                   alphabet: set[str] | None) -> dict[str, str]:
    """Markers whose body is an e-mail address rather than a name."""
    atom = _marker_atom(alphabet)
    pattern = re.compile(r"(?<![A-Za-z0-9])(" + atom + r")\s*([\w.+-]+@[\w.-]+)")
    out: dict[str, str] = {}
    for match in pattern.finditer(raw_text):
        marker, email = match.group(1), match.group(2)
        if wanted is not None and marker not in wanted:
            continue
        out.setdefault(marker, email)
    return out


def trailing_marker_affiliations(raw_text: str,
                                 wanted: set[str] | None = None) -> dict[str, str]:
    """Blocks that print the marker *after* the institution.

        Institute for Human-Centered Artificial Intelligence (HAI)8
        Stanford University The University of Texas at Austin9

    Every other parser here assumes the marker leads. Reading trailing digits
    anywhere would turn a reference list into affiliations, so only the text
    before the abstract is considered — a byline block is always there, and a
    reference list never is.
    """
    head = re.split(r"(?im)^\s*#*\s*(?:abstract|초록|1\.?\s+introduction)\b",
                    raw_text, maxsplit=1)[0]
    out: dict[str, str] = {}
    for match in re.finditer(r"([A-Z][^\n\d]{9,90}?)\s*(\d{1,2})(?=\s|$)", head):
        name, marker = match.group(1).strip(" ,;·"), match.group(2)
        if wanted is not None and marker not in wanted:
            continue
        if marker in out or not looks_like_affiliation(name):
            continue
        out[marker] = name
    return out


def inline_author_affiliations(raw_header: str, authors) -> dict[str, str]:
    """Bylines that print each author's affiliation on the author's own line.

    ACM and several society templates skip superscripts entirely:

        WENCHONG HE, University of Florida, USA
        ZHE JIANG∗, University of Florida, USA

    There is no marker to resolve — the line states the affiliation — so the
    marker machinery reads nothing and the paper falls back to linking every
    author to every institution. Measured on this corpus it is a small class,
    8 of the 536 papers still unresolved, but it is the strongest evidence
    there is: the byline says it outright.

    A line qualifies only when the text before the first comma ends in one of
    this paper's own author surnames and the remainder names an organisation,
    so an affiliation block ("Institute for AI, Peking University") cannot
    pass for a byline.
    """
    if isinstance(authors, str):
        authors = [x.strip() for x in re.split(r"[,;]", authors) if x.strip()]
    surnames: dict[str, str] = {}
    for name in authors or []:
        parts = [p for p in re.split(r"\s+", str(name).strip()) if p]
        if parts:
            surnames.setdefault(_fold(parts[-1]), str(name))
    if not surnames:
        return {}

    out: dict[str, str] = {}
    for line in raw_header.splitlines():
        line = re.sub(r"^#+\s*", "", line).strip()
        if "," not in line or len(line) > 200:
            continue
        head, _, rest = line.partition(",")
        tokens = [t for t in re.split(r"\s+", head.strip()) if t]
        if not tokens:
            continue
        resolved = surnames.get(_fold(tokens[-1].rstrip("*∗†‡§¶⋆")))
        rest = rest.strip()
        if resolved and resolved not in out and _ORGANISATION_CUES.search(rest):
            out[resolved] = rest
    return out


# `_ORGANISATION_CUES` is deliberately broad — it also accepts "state",
# "national" and "research" — which is right for judging a name and wrong for
# finding an affiliation in a whole document: it read the body heading ".2.
# State Space Models for Time Series" as one. An affiliation names a kind of
# organisation outright.
_AFFILIATION_ORG_CUE = re.compile(
    r"universit|institut|laborator|college|academy|hospital|polytech|"
    r"school of|faculty|department of|centre for|center for|"
    r"\bcorporation\b|\bcompany\b|\binc\b|\bltd\b|\bllc\b|\bgmbh\b|"
    r"research (?:center|centre|institute|laborator)", re.I)
# "2.1 Related Work", ".2. State Space Models" — a numbered section, not a place.
_SECTION_HEADING = re.compile(r"^\s*[.\d]+\s*[.)]?\s+[A-Z]")


# A numbered section opens many papers and is not an affiliation, even when
# the number is glued to the word: "1Introduction", "2Related Work".
_BODY_OPENING = re.compile(
    r"(?i)^(?:\d{1,2}|[a-j])\s*\.?\s*(?:introduction|related work|background|"
    r"abstract|methods?|results?|discussion|conclusion|preliminaries|"
    r"experiments?|acknowledg)")


# Organisations ROR does not hold a record for. The list is deliberately short
# and grows only when a real affiliation is seen to fall through: ROR already
# knows Genentech, Together AI, ByteDance, UC Berkeley and UT Austin, so a
# hand-kept dictionary would mostly duplicate it and drift out of date.
_KNOWN_ORGANISATIONS = frozenset({
    "nvidia", "microsoft research", "guide labs", "openai", "anthropic",
    "google research", "google brain", "meta ai", "amazon science",
    "ibm research", "huawei noah's ark lab", "tencent ai lab",
    "alibaba damo academy", "baidu research", "salesforce research",
    "adobe research", "bytedance seed", "moonshot ai", "zhipu ai",
    # Publishers appear as affiliations of their own staff.
    "mdpi", "elsevier", "springer nature", "wiley", "frontiers media",
    "digital science", "clarivate", "scopus", "web of science",
})

# A citation, not a place: "Nature 596, 583 (2021)", "Smith et al., 2023".
_LOOKS_LIKE_CITATION = re.compile(
    r"\bet al\b|\(\s*(?:19|20)\d{2}\s*\)|\bpp?\.\s*\d|"
    r"\barXiv\b|\bdoi\b|\bvol\.|\bno\.\s*\d", re.I)


@functools.lru_cache(maxsize=4096)
def _ror_knows(name: str) -> bool:
    """Whether ROR holds a record for this name. Cached; opens the index once."""
    try:
        from .lib.ror_index import RorIndex
    except ImportError:
        try:
            from lib.ror_index import RorIndex
        except ImportError:
            return False
    index = _ror_knows.index if hasattr(_ror_knows, "index") else RorIndex()
    _ror_knows.index = index
    if not index.available:
        return False
    try:
        return bool(index.resolve(name))
    except Exception:
        return False


def looks_like_affiliation(text: str) -> bool:
    """Whether a marker-led segment names a place rather than prose.

    `_AFFILIATION_ORG_CUE` alone was the test, and it lists the words a
    university's name contains. Companies do not contain them: "1Genentech
    2Guide Labs 3Department of Computer Science, New York University" was
    refused whole because its first segment named a company, and the two
    universities behind it went with it.

    The cue was written to keep a reference list out of the institution table —
    a previous build shipped "A Neural Network" and "Acer Liquid Network" as
    institutions, read from cited titles — and that reason still holds. So it
    is widened rather than dropped: ROR is asked, a short list covers what ROR
    does not hold, and anything shaped like a citation is refused outright.
    """
    text = (text or "").strip()
    if not text:
        return False
    # The organisation cue decides first and without a length limit: an
    # affiliation line often carries a full postal address, and capping it at
    # 200 characters rejected 116 papers that used to resolve.
    if _AFFILIATION_ORG_CUE.search(text):
        return True
    if _LOOKS_LIKE_CITATION.search(text) or len(text) > 200:
        return False
    head = re.split(r"[,;]", text)[0].strip(" .;:")
    if not head or not head[:1].isupper():
        return False
    if _fold(head) in _KNOWN_ORGANISATIONS:
        return True
    return _ror_knows(head)


# Academic domains whose label is neither a prefix nor the initials of the
# name they belong to. Kept small on purpose: prefix and initials cover
# stanford.edu, mit.edu, tsinghua.edu.cn and most of the rest.
_DOMAIN_ALIASES = {
    "pku": "peking university", "sjtu": "shanghai jiao tong university",
    "thu": "tsinghua university", "zju": "zhejiang university",
    "ustc": "university of science and technology of china",
    "fudan": "fudan university", "nus": "national university of singapore",
    "ntu": "nanyang technological university", "kaist": "kaist",
    "snu": "seoul national university", "postech": "postech",
    "ethz": "eth zurich", "epfl": "epfl", "tum": "technical university of munich",
    "ox": "university of oxford", "cam": "university of cambridge",
    "ucl": "university college london", "imperial": "imperial college london",
    "berkeley": "university of california, berkeley",
    "cmu": "carnegie mellon university", "gatech": "georgia institute of technology",
    "umich": "university of michigan", "illinois": "university of illinois",
}


def _domain_label(email: str) -> str:
    """The distinctive label of an academic e-mail domain.

    "liangs@stu.pku.edu.cn" is Peking University's, and the part that says so
    is "pku": the host, the generic academic suffixes and the country code
    carry no information.
    """
    match = re.search(r"@\s*([\w.-]+)", email or "")
    if not match:
        return ""
    parts = [p for p in match.group(1).lower().split(".") if p]
    generic = {"edu", "ac", "org", "com", "net", "gov", "info", "stu", "mail",
               "cs", "eecs", "www", "alumni", "student", "students"}
    parts = [p for p in parts if p not in generic and len(p) > 1]
    # Drop a trailing two-letter country code ("cn", "uk", "jp").
    if parts and len(parts[-1]) == 2:
        parts = parts[:-1]
    return parts[-1] if parts else ""


def institution_for_email(email: str, institutions) -> int | None:
    """Which of this paper's institutions an e-mail address belongs to.

    A byline can key its markers to e-mail addresses and print the affiliation
    on a line of its own with no marker at all:

        Shuang Liang1, Zhiyu Tao2, Qingshan Zhou3
        1liangs@stu.pku.edu.cn, 3zqs@pku.edu.cn
        Department of Information Management, Peking University

    The choice is between the two to four institutions the paper already has,
    not among all of them, so a domain label is enough — and only when exactly
    one candidate matches, because a paper with two Chinese universities must
    not have either picked by a coin toss.
    """
    label = _domain_label(email)
    if not label:
        return None
    alias = _DOMAIN_ALIASES.get(label, "")
    hits = []
    for institution_id, raw in institutions:
        name = _fold(raw or "")
        if not name:
            continue
        words = [w for w in re.findall(r"[a-z]+", name) if len(w) > 2]
        initials = "".join(w[0] for w in words)
        if (alias and alias in name) or label in words or initials == label:
            hits.append(institution_id)
    return hits[0] if len(set(hits)) == 1 else None


# "Figure 1. The gap between the records …" reads as marker 1 once a period is
# allowed between a marker and its text, and the sentence behind it mentioned
# "physical laboratories", which passed the organisation test. A caption is
# never an affiliation.
_CAPTION_LINE = re.compile(
    r"(?i)^\s*(?:figure|fig\.?|table|algorithm|alg\.?|equation|eq\.?|"
    r"section|sec\.?|chapter|appendix|theorem|lemma|proof|listing)\b")


def _marker_atom(alphabet: set[str] | None) -> str:
    """Regex alternation for one paper's markers, or the default set."""
    if not alphabet:
        return _MARKER_ATOM
    atoms = []
    if any(a.isdigit() for a in alphabet):
        atoms.append(r"\d{1,2}")
    if any(a.isalpha() and a.islower() for a in alphabet):
        atoms.append(r"[a-j]")
    atoms.extend(re.escape(a) for a in sorted(alphabet)
                 if not a.isdigit() and not a.isalpha())
    return "(?:" + "|".join(atoms) + ")"


def split_runs_beyond(markers: dict[str, list[str]],
                      defined: set[str]) -> dict[str, list[str]]:
    """Split a digit run the affiliation block cannot possibly define.

        Yuhui Chen12 … 1SKL-MAIS, Institute of Automation
                       2School of Artificial Intelligence, UCAS

    The block defines 1 and 2, so "12" is not a twelfth institution — it is
    the first and the second. Only runs above the largest marker the block
    actually declares are split, so a paper that really does list twelve
    affiliations keeps its 12.
    """
    numbers = sorted(int(m) for m in defined if m.isdigit())
    if not numbers:
        return markers
    largest = numbers[-1]
    known = {str(n) for n in numbers}
    out: dict[str, list[str]] = {}
    for name, values in markers.items():
        expanded: list[str] = []
        for value in values:
            if (value.isdigit() and int(value) > largest
                    and all(digit in known for digit in value)):
                expanded.extend(value)
            else:
                expanded.append(value)
        out[name] = expanded
    return out


def read_byline_markers(raw_header: str, authors, text_path: Path | None
                        ) -> tuple[dict[str, list[str]], set[str]]:
    """Author→markers, read whichever way maps more of this paper's authors.

    Inferring the alphabet is a heuristic, and a wrong guess is worse than no
    guess: a footnote elsewhere in the document nominated § and ‡ for a paper
    whose byline is numbered, and the restriction dropped all five authors.
    Both readings are cheap, and the paper's own author count decides between
    them, so widening the parser can no longer narrow it.
    """
    plain = author_affiliation_markers(raw_header, authors)
    alphabet = infer_marker_alphabet(raw_header)
    if not alphabet and text_path is not None:
        alphabet = infer_marker_alphabet(affiliation_window(text_path))
    if not alphabet:
        return plain, set()
    keyed = author_affiliation_markers(raw_header, authors, alphabet)
    markers = keyed if len(keyed) >= len(plain) else plain
    used = alphabet if len(keyed) >= len(plain) else set()
    # The block says which markers exist; a run above the largest of them is
    # several markers written together, not a number.
    defined = set(marker_affiliations(raw_header, None, used))
    if not defined and text_path is not None:
        defined = set(marker_affiliations(
            affiliation_window(text_path), None, used))
    return split_runs_beyond(markers, defined or alphabet), used


def marker_affiliations(raw_header: str, wanted: set[str] | None = None,
                        alphabet: set[str] | None = None) -> dict[str, str]:
    """Map each affiliation marker to the affiliation text it labels.

    Requiring the line to *begin* with a marker missed the common layout that
    runs the whole block together — "1Heriot-Watt University, Edinburgh, UK
    2Ocean University, China" — and any line whose first affiliation had
    already been consumed. Every line carrying an organisation name is split
    on its markers instead.

    A marker also gets a line of its own when the PDF wraps:

        1
        Department of Marketing, ESCP Business School

    so a line that is nothing but a marker is joined to the one below it.

    `wanted` restricts the search to the markers a byline actually used. That
    is what makes it safe to scan a whole paper rather than its front matter:
    the affiliations of 15 of these papers sit past any window — one at
    character 89,582 of 89,729 — and an unrestricted scan of a full document
    would read the reference list as affiliations, which is how this parser
    once minted institutions out of cited paper titles.
    """
    # The block has to be read with the same alphabet as the byline. Reading
    # it with the fixed symbol set left "⋆Tsinghua University" unparsed while
    # the byline had already resolved "Chen Qian⋆".
    atom = _marker_atom(alphabet)
    # "1Genentech", "2 MDPI", "1. Artificial Intelligence …" — the separator
    # between a marker and its affiliation is nothing, a space, or a period.
    head_re = re.compile(r"^(" + atom + r")\s*\.?\s*(.+)$")
    split_re = re.compile(
        r"(?=(?<![A-Za-z0-9])(?:" + atom + r")\s*\.?\s*[A-Z])")

    lines = [re.sub(r"^#+\s*", "", line).strip()
             for line in raw_header.splitlines()]
    # Same guard as `_CANDIDATE_MARKER`: a marker is followed by a capital or
    # a space. Without it a lowercase alphabet made the "a" of "agents" a
    # marker and swallowed the sentence after it.
    lead_re = re.compile(r"^(?:" + atom + r")(?=[A-Z\s])\s*\S")
    joined: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        if line and re.fullmatch(atom, line) and index + 1 < len(lines):
            joined.append(f"{line}{lines[index + 1]}")
            index += 2
            continue
        # A two-column layout sets its footnote in a narrow measure, so the
        # affiliation wraps after a word or two: "1ShanghaiTech" on one line
        # and "University;" on the next. The organisation cue is then on a line
        # that carries no marker and the marker is on a line that names no
        # organisation, so neither is read. Once a line begins with a marker,
        # the following lines are pulled in until it names one.
        if line and lead_re.match(line) and not looks_like_affiliation(line):
            merged, step = line, 1
            while step <= 3 and index + step < len(lines):
                nxt = lines[index + step]
                if not nxt or _SECTION_HEADING.match(nxt):
                    break
                merged = f"{merged} {nxt}"
                step += 1
                if looks_like_affiliation(merged):
                    break
            # The organisation has to be near the marker. Reading further and
            # accepting the first university named three lines later turned
            # "1Introduction …" into an affiliation by way of the body text.
            if (looks_like_affiliation(merged[:120])
                    and not _BODY_OPENING.match(merged[len(line) - len(line.lstrip()):])):
                joined.append(merged)
                index += step
                continue
        joined.append(line)
        index += 1

    out: dict[str, str] = {}
    for line in joined:
        if not line or _CAPTION_LINE.match(line):
            continue
        if not looks_like_affiliation(line):
            continue
        for piece in split_re.split(line):
            head = head_re.match(piece.strip())
            if not head:
                continue
            marker, body = head.group(1), head.group(2).strip(" ,;")
            if len(body) < 5 or marker in out:
                continue
            if wanted is not None and marker not in wanted:
                continue
            if not looks_like_affiliation(body):
                continue
            # "1. Artificial Intelligence and Translational Imaging (ATI) Lab,
            # … University of Crete" has a section heading's shape and is an
            # affiliation. The heading guard exists to keep body text out, so
            # it only applies when the body does not name an organisation.
            if _SECTION_HEADING.match(body) and not looks_like_affiliation(body):
                continue
            out[marker] = body
    return out


def extract_header(text_path: Path) -> tuple[str, list[str], float]:
    try:
        text = text_path.read_text(encoding="utf-8", errors="replace")[:12000]
    except OSError:
        return "", [], 0.0
    normalized = []
    for line in text.splitlines():
        # A leading number is usually a PDF line number, but on an affiliation
        # line it is the marker the byline points at ("1 Heriot-Watt
        # University, Edinburgh, UK"). Stripping it unconditionally erased the
        # mapping before `marker_affiliations` could read it, so it is kept
        # when an organisation name follows.
        head = re.match(r"^\s*[-–—]?\s*(\d+)\s+(.*)$", line)
        if head and not _ORGANISATION_CUES.search(head.group(2)[:80]):
            line = head.group(2)
        line = re.sub(r"\s+", " ", line).strip()
        if line:
            normalized.append(line)
    text = "\n".join(normalized)
    text = _strip_editorial_blocks(text)
    stop = re.search(r"(?im)^\s*(?:#+\s*)?(?:abstract|초록)\b", text)
    if stop:
        text = text[:stop.start()]
    lines = [x.strip() for x in text.splitlines() if x.strip()][:40]
    raw = "\n".join(lines)
    cues = re.compile(
        r"university|institute|laborator|school|college|department|center|"
        r"centre|hospital|academy|대학교|연구원|연구소|병원|학부|학과|@"
        # Acronyms need boundaries: unanchored "MIT" matched "permitted" and
        # "ETH" matched "method", so a licence paragraph on an IOP cover sheet
        # and any sentence about methodology became affiliation candidates.
        r"|\bETH\b|\bMIT\b|\bCaltech\b|\bCNRS\b", re.I)
    candidates = []
    for line in lines:
        # A byline that packs every affiliation onto one line runs past any
        # sane per-line cap — the Frontiers paper above put three of them in
        # 468 characters, so the whole line was dropped and only Scopus knew
        # where those authors worked. Split on the superscript markers that
        # separate them and judge each piece on its own.
        for piece in (_split_marked_affiliations(line)
                      if len(line) > 240 else [line]):
            if not (5 <= len(piece) <= 240) or not cues.search(piece):
                continue
            if re.match(r"^(abstract|keywords?|초록|introduction)\b", piece, re.I):
                continue
            if re.search(r"correspondence|corresponding author|contact", piece, re.I):
                continue
            piece = re.sub(r"^[-*\d\s]+", "", piece).strip()
            if piece and piece not in candidates:
                candidates.append(piece)
    confidence = min(0.55 + (0.1 if any("@" in x for x in candidates) else 0) + (0.1 if len(candidates) > 1 else 0), 0.75) if candidates else 0.0
    return raw, candidates, confidence


GROUPS = [
    ("Max Planck Society", r"max[- ]planck"),
    ("Helmholtz Association", r"helmholtz"),
    ("Leibniz Association", r"leibniz"),
    ("Chinese Academy of Sciences", r"chinese academy of sciences|\bcas\b"),
    ("CNRS", r"\bcnrs\b|centre national de la recherche scientifique"),
]

COUNTRIES = [
    # Bare "US" is not accepted: it collides with unit codes in non-US
    # affiliations ("Univ. Rennes, BIOSIT, UMS CNRS 3840, US INSERM"), which is
    # how a CNRS lab ended up in the United States.
    ("United States", r"\b(?:USA|U\.S\.A\.|U\.S\.|United States)\b"),
    ("United Kingdom", r"\b(?:UK|U\.K\.|United Kingdom|England)\b"),
    ("South Korea", r"\b(?:South Korea|Republic of Korea|Korea)\b"),
    ("China", r"\bChina\b"),
    ("Taiwan", r"\bTaiwan\b"),
    ("Netherlands", r"\bNetherlands\b"),
    ("Canada", r"\bCanada\b"),
    ("Switzerland", r"\bSwitzerland\b"),
    ("Singapore", r"\bSingapore\b"),
    ("Germany", r"\bGermany\b"),
    ("France", r"\bFrance\b"),
    ("Australia", r"\bAustralia\b"),
    ("Japan", r"\bJapan\b"),
    ("India", r"\bIndia\b"),
    ("Italy", r"\bItaly\b"),
    ("Spain", r"\bSpain\b"),
    ("Israel", r"\bIsrael\b"),
    ("Brazil", r"\bBrazil\b"),
    ("Austria", r"\bAustria\b"),
    ("Sweden", r"\bSweden\b"),
    ("Denmark", r"\bDenmark\b"),
    ("Norway", r"\bNorway\b"),
    ("Finland", r"\bFinland\b"),
    ("Belgium", r"\bBelgium\b"),
]

# Display names for the 24 countries the corpus is dominated by. Everything else
# falls back to the ISO 3166-1 short name from `lib/country_map.py`.
_COUNTRY_DISPLAY = {name: name for name, _pattern in COUNTRIES}
_COUNTRY_DISPLAY_BY_CODE = {
    "KR": "South Korea", "US": "United States", "GB": "United Kingdom",
    "CN": "China", "TW": "Taiwan", "NL": "Netherlands", "RU": "Russia",
    "IR": "Iran", "VN": "Vietnam", "CZ": "Czech Republic", "HK": "Hong Kong",
}


def _iso_country_display() -> dict[str, str]:
    """alpha-2 → the name this DB shows, preferring the corpus's own spellings."""
    names = {a2: name for a2, _a3, name in country_map.ISO_3166_1_ROWS}
    names.update(_COUNTRY_DISPLAY_BY_CODE)
    return names


_ISO_COUNTRY_NAMES = _iso_country_display()
_ISO_COUNTRY_PATTERN = re.compile(
    "|".join(
        r"\b" + re.escape(alias) + r"\b"
        for alias in sorted(
            {name for _a2, _a3, name in country_map.ISO_3166_1_ROWS}
            | {alias for alias, _code in country_map.LEGACY_COUNTRY_ALIASES},
            key=len, reverse=True)),
    re.I)


def country_from_raw(raw: str) -> str:
    """Resolve the country an affiliation segment ends with.

    An affiliation reads "Department, Institution, City, Country", so the
    country is the *last* place name in the segment. The previous version
    returned the first entry of a 24-row list that happened to match anywhere,
    which is why "USA 6Computational Social Science, ETH Zurich, Zurich,
    Switzerland" resolved ETH Zurich to the United States: the orphan "USA"
    belonged to the preceding affiliation and "United States" sorts first.
    """
    best_name, best_end = "", -1
    for name, pattern in COUNTRIES:
        for match in re.finditer(pattern, raw, re.I):
            if match.end() > best_end:
                best_name, best_end = name, match.end()
    for match in _ISO_COUNTRY_PATTERN.finditer(raw):
        if match.end() <= best_end:
            continue
        state, code = country_map.country_resolution(match.group(0))
        if state == "present" and code in _ISO_COUNTRY_NAMES:
            best_name, best_end = _ISO_COUNTRY_NAMES[code], match.end()
    return best_name


INSTITUTION_CANONICAL_ALIASES = [
    (r"^Massachusetts Institute(?: of Technology)?$", "Massachusetts Institute of Technology"),
    (r"^Georgia Institute(?: of Technology)?$", "Georgia Institute of Technology"),
    (r"^California Institute(?: of Technology)?$", "California Institute of Technology"),
    (r"^Harbin Institute(?: of Technology)?(?: Shenzhen)?$", "Harbin Institute of Technology"),
    (r"^Imperial College(?: London)?$", "Imperial College London"),
    (r"^University College(?: London)?$", "University College London"),
    (r"^The Chinese University(?: of Hong Kong)?$", "The Chinese University of Hong Kong"),
    (r"^The Hong Kong University(?: of Science and Technology)?$", "The Hong Kong University of Science and Technology"),
    (r"^Chinese Academy(?: of Science| of Sciences)?$", "Chinese Academy of Sciences"),
    (r"^Korea Advanced Institute(?: of Science (?:and|&) Technology)?(?: \(KAIST\))?$", "Korea Advanced Institute of Science and Technology"),
    (r"^KTH Royal Institute(?: of Technology)?$", "KTH Royal Institute of Technology"),
    (r"^Karlsruhe Institute(?: of Technology)?$", "Karlsruhe Institute of Technology"),
    (r"^Stevens Institute(?: of Technology)?$", "Stevens Institute of Technology"),
    (r"^Illinois Institute(?: of Technology)?$", "Illinois Institute of Technology"),
    (r"^Eastern Institute(?: of Technology)?$", "Eastern Institute of Technology"),
    (r"^Polish Academy(?: of Sciences)?$", "Polish Academy of Sciences"),
    (r"^College of (?:Chemical and Biological Engineering|Computer Science and Technology), Zhejiang University$", "Zhejiang University"),
    (r"^College of (?:Computer Science and Technology|Intelligent Systems Science and Engineering), Harbin Engineering University$", "Harbin Engineering University"),
    (r"^College of Computer Science and Technology, Harbin Institute of Technology$", "Harbin Institute of Technology"),
    (r"^College of Education, Zhejiang University$", "Zhejiang University"),
    (r"^College of (?:Arts and Sciences|Computing Studies|Education) Pampanga State University.*$", "Pampanga State University"),
    (r"^College of Humanities, Arts, and Social Sciences$", "Nanyang Technological University"),
    (r"^University of Toronto Faculty of Medicine$", "University of Toronto"),
    (r"^University Health Network,? Toronto.*$", "University Health Network"),
    (r"^Microsoft Research,? Redmond.*$", "Microsoft Research"),
    (r"^.*Robert R\. McCormick School of Engineering.*$", "Northwestern University"),
    (r"^.*MIT (?:School|Department|Sloan).*$", "Massachusetts Institute of Technology"),
    (r"^.*USC Viterbi School of Engineering.*$", "University of Southern California"),
    (r"^.*Harvard (?:Faculty|John A\. Paulson School|T\.H\. Chan School).*$", "Harvard University"),
    (r"^.*Haas School of Business.*$", "University of California, Berkeley"),
    (r"^.*John F\. Kennedy School of Government.*$", "Harvard University"),
    (r"^.*UCLA (?:Samueli School|School of Dentistry).*$", "University of California, Los Angeles"),
    (r"^.*Whiting School of Engineering.*$", "Johns Hopkins University"),
    (r"^.*Carlson School of Management.*$", "University of Minnesota"),
    (r"^.*Princeton School of Public and International Affairs.*$", "Princeton University"),
    (r"^.*(?:NYU Tandon|Leonard N\. Stern|Robert F\. Wagner).*$", "New York University"),
    (r"^.*Fuqua School of Business.*$", "Duke University"),
    (r"^.*Questrom School of Business.*$", "Boston University"),
    (r"^.*DeGroote School of Business.*$", "McMaster University"),
    (r"^.*Rady School of Management.*$", "University of California, San Diego"),
    (r"^.*McDonough School of Business.*$", "Georgetown University"),
    (r"^.*Pritzker School of Molecular Engineering.*$", "The University of Chicago"),
    (r"^.*UNC (?:Eshelman School|School of Medicine).*$", "The University of North Carolina at Chapel Hill"),
    (r"^.*UCSF School of Medicine.*$", "University of California, San Francisco"),
    (r"^.*UC Berkeley(?:’s)? (?:School|Industrial Engineering).*$", "University of California, Berkeley"),
    (r"^.*Johns Hopkins Department of Biomedical Engineering.*$", "Johns Hopkins University"),
    (r"^.*McGill Faculty of Medicine.*$", "McGill University"),
    (r"^.*Wake Forest School of Business.*$", "Wake Forest University"),
    (r"^.*Gaoling School of Artificial Intelligence.*$", "Renmin University of China"),
    (r"^.*Luddy School of Informatics.*$", "Indiana University"),
    (r"^.*ECUST School of Business.*$", "East China University of Science and Technology"),
    (r"^.*Department of Cognitive Robotics,? TU Delft.*$", "Delft University of Technology"),
    (r"^.*ETH Zuirch.*$", "ETH Zurich"),
    (r"^.*Idiap Research Institute.*$", "Idiap Research Institute"),
    (r"^.*BNM Institute(?: of Technology)?.*$", "BNM Institute of Technology"),
    (r"^Amsterdam School of Communication Research$", "University of Amsterdam"),
    (r"^Dalian University$", "Dalian University of Technology"),
    (r"^Chinese University$", "The Chinese University of Hong Kong"),
    (r"^Chinese University of Hong Kong$", "The Chinese University of Hong Kong"),
    (r"^Chinese University of Hong Kong, Shenzhen$", "The Chinese University of Hong Kong, Shenzhen"),
    (r"^Hong Kong University of Science and Technology$", "The Hong Kong University of Science and Technology"),
    # Sub-organisations and legal entities that belong to one institution.
    # Curated explicitly rather than derived: automatic brand-head merging was
    # tried and rejected — grouping by leading distinctive token collapses MIT
    # with UMass Amherst and Massachusetts General, UIUC with UIC and Illinois
    # Tech, and "Munich Data Science Institute" with "Munich Center for Machine
    # Learning", because the head is often a city or a shared adjective.
    (r"^Stanford$|^Stanford (?:Engineering|Healthcare|Health Care|Medicine|"
     r"Institute for Human-Centered Artificial Intelligence|HAI|Graduate School"
     r"(?: of Business)?|Law School|Doerr School.*|School of (?:Medicine|"
     r"Engineering|Humanities.*))$", "Stanford University"),
    (r"^University of Illinois Urbana-?Champaign[.,].*$",
     "University of Illinois Urbana-Champaign"),
    (r"^Meta(?: AI(?: Research)?| Ai| Platforms.*| Reality Labs)?$", "Meta"),
    (r"^Google(?: LLC.*| Switzerland GmbH| Inc\.?| Research)?$", "Google"),
    (r"^Microsoft(?: Search| International Holdings B\.V\.| Corporation)?$",
     "Microsoft"),
    (r"^ETH Z[^a-zA-Z]*urich$", "ETH Zurich"),
    # "UC <campus>" is the University of California family. ROR carries most of
    # these as aliases; the three it misses are spelled out here.
    (r"^UC ?Davis$", "University of California, Davis"),
    (r"^UCLA$|^UC Los Angeles$", "University of California, Los Angeles"),
    (r"^UCSF$|^UC San Francisco$", "University of California, San Francisco"),
    (r"^Berkeley$", "University of California, Berkeley"),
    (r"^DeepMind(?: Technologies(?: Limited)?)?$", "Google DeepMind"),
]

RAW_INSTITUTION_ALIASES = [
    (r"\bTechnical University(?: of)? Munich\b", "Technical University of Munich"),
    (r"\bTechnical University(?: of)? Berlin\b", "Technical University of Berlin"),
    (r"\bIndian Institute of Technology,?\s*Delhi\b", "Indian Institute of Technology Delhi"),
    (r"\bIndian Institute of Technology,?\s*Roorkee\b", "Indian Institute of Technology Roorkee"),
    (r"\bIndian Institute of Technology,?\s*Guwahati\b", "Indian Institute of Technology Guwahati"),
    (r"\bIndian Institute of Technol(?:ogy)?\b", "Indian Institute of Technology"),
    (r"\bNational Institute of Standards and Technology\b", "National Institute of Standards and Technology"),
    (r"\bNational Institute of Information and Communications Technology\b", "National Institute of Information and Communications Technology"),
    (r"\bNational Institute of Advanced Industrial Science and Technology\b", "National Institute of Advanced Industrial Science and Technology"),
    (r"\bNational Institute for Materials Science\b", "National Institute for Materials Science"),
    (r"\bNational Institute for Research in Digital Science and Technology\b", "National Institute for Research in Digital Science and Technology"),
    (r"\bNational Institute of Telecommunications\b", "National Institute of Telecommunications"),
    (r"\bNational Institute of Aging\b", "National Institute on Aging"),
    (r"\bBeijing Institute of Technology\b", "Beijing Institute of Technology"),
    (r"\bBeijing Institute for General Artificial Intelligence\b", "Beijing Institute for General Artificial Intelligence"),
    (r"\bBeijing Institute of Mathematical Sciences and Applications\b", "Beijing Institute of Mathematical Sciences and Applications"),
    (r"\bBeijing Institute of Heart, Lung and Blood Vessel Diseases\b", "Beijing Institute of Heart, Lung and Blood Vessel Diseases"),
    (r"\bBeijing Institute of Collaborative Innovation\b", "Beijing Institute of Collaborative Innovation"),
    (r"\bBeijing University of Technology\b", "Beijing University of Technology"),
    (r"\bBeijing University of Posts and Telecommunications\b", "Beijing University of Posts and Telecommunications"),
    (r"\bMedical University(?: of)? Vienna\b", "Medical University of Vienna"),
    (r"\bMedical University(?: of)? Graz\b", "Medical University of Graz"),
    (r"\bMedical University(?: of)? Warsaw\b", "Medical University of Warsaw"),
    (r"\bState University of New York at Binghamton\b", "Binghamton University"),
    (r"\bNational University of Malaysia\b", "National University of Malaysia"),
    (r"\bDalian University of Technology\b", "Dalian University of Technology"),
    (r"\bHong Kong University of Science and Technology\s*\(Guangzhou\)", "The Hong Kong University of Science and Technology (Guangzhou)"),
    (r"\bHong Kong University of Science and Technology\b", "The Hong Kong University of Science and Technology"),
    (r"\bChinese University of Hong Kong,?\s*Shenzhen\b", "The Chinese University of Hong Kong, Shenzhen"),
    (r"\bChinese University of Hong Kong\b", "The Chinese University of Hong Kong"),
    (r"\bPampanga State University\b", "Pampanga State University"),
    (r"\bHal Marcus College of Science and Engineering\b", "University of West Florida"),
    (r"\bNational University of Science (?:and|&) Technology,?\s*Muscat,?\s*Oman\b", "National University of Science & Technology, Oman"),
    (r"\bColorado State University\b", "Colorado State University"),
    (r"\bInstitute of Physics\b", "Institute of Physics"),
]

# Scopus sometimes returns a university subunit as an independent affiliation.
# These IDs are stable organization records; normalize them to the degree-granting
# parent verified against the corresponding article affiliation blocks.
SCOPUS_AFFILIATION_PARENT_BY_ID = {
    "60028786": "Iowa State University",
    "60142023": "The University of North Carolina at Chapel Hill",
    "60155621": "University of Miami",
    "60117840": "Zhejiang University",
    "60362739": "Jilin University",
    "60417404": "Harbin Engineering University",
    "60117751": "Zhejiang University",
    "60097290": "Georgia Institute of Technology",
    "60117795": "Zhejiang University",
    "60031330": "Carnegie Mellon University",
    "60104842": "Carnegie Mellon University",
    "60137364": "Oregon State University",
    "60137961": "University of Illinois at Chicago",
    "60146411": "Michigan State University",
    "60148980": "Texas A&M University",
    "60149838": "The Ohio State University",
    "60149993": "University of Arizona",
    "60154915": "The University of Iowa",
    "60155914": "University of Notre Dame",
    "60279839": "University of Nevada, Reno",
    "60154476": "University of Colorado Boulder",
    "60279457": "University of Vermont",
    "60139609": "Clemson University",
    "60118484": "Nanyang Technological University",
    "60417010": "Harbin Engineering University",
    "130639393": "The Ohio State University",
    "60145179": "George Mason University",
    "60008161": "Idaho State University",
    "60152345": "University of Minnesota",
    "60190913": "Flinders University",
    "60149312": "Temple University",
    "60156837": "University of Washington",
}

INSTITUTION_SEED_NAMES = {
    "Massachusetts Institute of Technology",
    "Georgia Institute of Technology",
    "California Institute of Technology",
    "Harbin Institute of Technology",
    "Imperial College London",
    "University College London",
    "The Chinese University of Hong Kong",
    "The Hong Kong University of Science and Technology",
    "Chinese Academy of Sciences",
    "National University of Singapore",
    "National University of Defense Technology",
    "Technical University of Munich",
    "Technical University of Darmstadt",
    "Technical University of Berlin",
    "Technical University of Denmark",
    "Indian Institute of Science",
    "Indian Institute of Technology Delhi",
    "Indian Institute of Technology Madras",
    "Indian Institute of Technology Patna",
    "Indian Institute of Technology Ropar",
    "Indian Institute of Technology Roorkee",
    "Indian Institute of Science Education and Research Pune",
    "Korea Advanced Institute of Science and Technology",
    "KTH Royal Institute of Technology",
    "Karlsruhe Institute of Technology",
    "Stevens Institute of Technology",
    "Illinois Institute of Technology",
    "Eastern Institute of Technology",
    "Warsaw University of Technology",
    "Hebei University of Technology",
    "Polish Academy of Sciences",
    "Tongji University",
    "The University of Hong Kong",
    "The University of Tokyo",
    "The University of Chicago",
    "The University of Sydney",
    "The University of Texas at Austin",
    "The University of Edinburgh",
    "The University of Manchester",
    "The University of Melbourne",
    "The University of Adelaide",
    "The University of British Columbia",
    "The University of Texas at Dallas",
    "The University of Utah",
    "The University of Arizona",
    "The University of Iowa",
    "The University of North Carolina at Chapel Hill",
    "The University of Osaka",
    "The University of Queensland",
    "The University of Sheffield",
    "The University of Texas Rio Grande Valley",
    "The University of Waterloo",
    "Australian National University",
    "Seoul National University",
}

GENERIC_INSTITUTION_NAMES = {
    "The University", "National University", "Technical University",
    "Massachusetts Institute", "Chinese Academy", "Harbin Institute",
    "Georgia Institute", "California Institute", "Imperial College",
    "University College", "Indian Institute", "The Chinese University",
    "The Hong Kong University", "Beijing Institute", "National Institute",
    "State University", "Medical University", "Central University",
    "University of California", "City University", "Hong Kong University",
    "Beijing University", "Huazhong University", "Renmin University",
    "Southern University", "Dalian University", "Chinese University",
    "King Abdullah University", "Singapore University",
    "South China University", "Queensland University", "Max Planck Institute",
    "University of Technology", "University of Science and Technology",
    "Allen Institute",
}

STANDALONE_INSTITUTION_NAMES = {
    "London School of Economics and Political Science",
    "College of Staten Island",
    "Sant'Anna School of Advanced Studies",
    "Allen Institute",
    "Max Planck Institute",
    "University of California",
    "Hefei National Laboratory for Physical Sciences at the Microscale",
    "Idiap Research Institute",
    "National Engineering Laboratory for Big Data Analysis and Applications",
}

_INSTITUTION_REGISTRY: list[str] = []
_INSTITUTION_REGISTRY_BY_TOKEN: dict[str, list[str]] = {}


def _clean_affiliation_text(value: str) -> str:
    value = re.sub(r"([A-Za-z])-\s+([a-z])", r"\1\2", value or "")
    value = re.sub(r"^[a-z](?=[A-Z])", "", value)
    value = re.sub(r"(?<![A-Za-z])\d+\s*(?=[A-Z])", " ", value)
    value = re.sub(r"\{[^}]*\}|\S+@\S+", " ", value)
    return re.sub(r"\s+", " ", value).strip(" ,;:-")


def _apply_institution_aliases(value: str) -> str:
    value = re.sub(r"\s+", " ", value or "").strip(" ,;:-†‡")
    english = _INSTITUTION_ENGLISH_ALIASES_BY_NORM.get(norm(value))
    if english:
        return english
    for pattern, canonical in INSTITUTION_CANONICAL_ALIASES:
        if re.match(pattern, value, re.I):
            return canonical
    return value


# Prose that only ever appears in a title, abstract or reference entry — never
# inside an affiliation line. Each pattern here is backed by a real row that
# reached the shipped DB through the old front/back-matter window.
_PROSE_INSTITUTION_CUES = re.compile(
    r"\bAbstract\b"                       # "University of Helsinki Abstract World models…"
    r"|\barXiv\b|\bpreprint\b|\bdoi\.org\b|\bet al\b"   # reference entries
    r"|\bpp\.|\bVol\.|\bIn Proceedings\b|\(\s*(?:19|20)\d{2}\s*\)"
    r"|^(?:A|An|The)\s+(?:\w+\s+){0,4}"
    r"(?:Network|Model|Framework|Approach|Method|Study|Analysis|Survey|Dataset|"
    r"Benchmark|Measure|System)\b"        # "A Dynamic Network", "A Neural Network"
    r"|\b(?:we|our|this paper|is proposed|are proposed|propose[sd]?|introduce)\b",
    re.I)

# A real organisation names itself with one of these. Used only to disqualify
# names that end in a machine-learning artefact word, so that "University Health
# Network" and "HUN-REN Hungarian Research Network" survive while "Encoder
# Network", "Policy Network" and "Acer Liquid Network" do not.
_ORGANISATION_CUES = re.compile(
    r"universit|institut|laborator|college|academy|hospital|cent(?:er|re)|"
    r"school|research|ministry|agency|foundation|association|society|council|"
    r"observator|museum|clinic|bureau|\bnational\b|\bstate\b|\bcorp|\binc\b|"
    r"\bltd\b|\bllc\b|\bgmbh\b|\bco\.|\bcompany\b|\bgroup\b|\btrust\b", re.I)

_ARTEFACT_TAIL = re.compile(
    r"\b(?:networks?|models?|encoder|decoder|transformer|benchmark|dataset|"
    r"framework|algorithm|architecture|pipeline|module)$", re.I)

# Where an affiliation line stops and the rest of the page begins. Cutting here
# keeps the institution that leads the segment ("5Goethe University Frankfurt,
# Germany.∗Corresponding authors. Emails: … Fig. 1. Motion retargeting") instead
# of discarding the whole over-long segment.
_AFFILIATION_STOP = re.compile(
    r"(?i)(?:\bcorresponding\s+author|\bcorrespondence\s+to|\be-?mails?\s*:|"
    r"\bfig(?:ure)?\.?\s*\d|\babstract\b|\bkeywords?\b|\bintroduction\b|"
    r"https?://|\barXiv\b|\bwork (?:was|performed)\b|\bequal contribution|"
    # Venue boilerplate. "…, Seoul, South Korea. PMLR 306, 2026." made every
    # author of that paper Korean.
    r"\bproceedings\s+of\b|\bcopyright\b|\bPMLR\b|\bpreprint\b|"
    r"\b(?:accepted|published|submitted)\s+(?:at|to|in|as)\b|"
    r"\b\d{1,2}\s*(?:st|nd|rd|th)\s+(?:international\s+)?conference\b)")


def _person_name_tokens(authors) -> set[str]:
    """Surname/given-name tokens of this paper's own authors."""
    if isinstance(authors, str):
        authors = re.split(r"[,;]|\band\b", authors)
    tokens = set()
    for author in authors or []:
        for token in re.findall(r"[A-Za-z][A-Za-z'’-]{1,}", str(author)):
            if len(token) >= 2:
                tokens.add(token.casefold())
    return tokens


def _strip_leading_author_names(raw: str, author_tokens: set[str]) -> str:
    """Drop the author byline that runs straight into the affiliation.

    Front matter reads "Iz Beltagy Kyle Lo Arman Cohan Allen Institute for AI";
    without this the parser mints "Text Iz Beltagy Kyle Lo Arman Cohan Allen
    Institute". Only this paper's own author tokens are removed, so real
    multiword names ("Seoul National University") are never touched.
    """
    if not author_tokens:
        return raw
    words = raw.split()
    cut = 0
    for index, word in enumerate(words):
        if re.sub(r"[^A-Za-z'’-]", "", word).casefold() in author_tokens:
            cut = index + 1
        elif cut and index - cut >= 2:
            break
    return " ".join(words[cut:]) if cut else raw


def _trim_affiliation_segment(raw: str) -> str:
    """Cut a candidate segment at the first non-affiliation boundary.

    Also drops a leading orphan country: splitting on superscript markers leaves
    the tail of the previous affiliation at the front ("USA 6Computational Social
    Science, ETH Zurich, Zurich, Switzerland"), and that stray country was what
    put ETH Zurich in the United States.
    """
    stop = _AFFILIATION_STOP.search(raw)
    if stop:
        raw = raw[:stop.start()]
    raw = raw.strip(" ,;:-.*∗†‡")
    lead = _ISO_COUNTRY_PATTERN.match(raw) or re.match(
        r"(?i)(?:USA|U\.S\.A\.|UK|U\.K\.|PRC)\b", raw)
    if lead and lead.end() < len(raw):
        raw = raw[lead.end():].strip(" ,;:-.*∗†‡")
    return raw


def is_suspicious_institution_name(name: str) -> bool:
    value = _apply_institution_aliases(_clean_affiliation_text(name))
    if value in STANDALONE_INSTITUTION_NAMES:
        return False
    if (not value or value in GENERIC_INSTITUTION_NAMES or len(value) > 90
            or is_local_language_institution(value)):
        return True
    if _PROSE_INSTITUTION_CUES.search(value):
        return True
    if _ARTEFACT_TAIL.search(value) and not _ORGANISATION_CUES.search(value):
        return True
    return bool(re.search(
        r"@|^College of\b|\b(?:Department|School of|Faculty|Published|Accepted|"
        r"Proceedings|Corresponding|Authors?|Laboratory for|is with|are with|"
        r"work was|Submitted|Copyright)\b|(?:\band|\bof)$", value, re.I))


def set_institution_registry(names) -> None:
    global _INSTITUTION_REGISTRY, _INSTITUTION_REGISTRY_BY_TOKEN
    cleaned = {_apply_institution_aliases(str(name)) for name in names if name}
    cleaned.update(INSTITUTION_SEED_NAMES)
    _INSTITUTION_REGISTRY = sorted(
        (name for name in cleaned if not is_suspicious_institution_name(name)),
        key=lambda name: (-len(name), name.casefold()))
    by_token = {}
    generic = {
        "university", "institute", "academy", "college", "hospital",
        "centre", "center", "research", "national", "technology",
    }
    for name in _INSTITUTION_REGISTRY:
        tokens = [
            token for token in re.findall(r"[a-z0-9]+", name.casefold())
            if len(token) >= 4 and token not in generic
        ]
        key = max(tokens, key=len) if tokens else ""
        if key:
            by_token.setdefault(key, []).append(name)
    _INSTITUTION_REGISTRY_BY_TOKEN = by_token


def initialize_institution_registry(conn: sqlite3.Connection) -> None:
    names = {
        row[0] for row in conn.execute(
            "SELECT institution_name FROM institutions").fetchall()
        if row[0] and not is_suspicious_institution_name(row[0])
    }
    cache = _load_scopus_record_cache()
    for record in cache.values():
        if not isinstance(record, dict):
            continue
        for affiliation in record.get("affiliations") or []:
            candidate = _apply_institution_aliases(
                str(affiliation.get("name") or ""))
            if candidate and not is_suspicious_institution_name(candidate):
                names.add(candidate)
    set_institution_registry(names)


def _registered_institution(raw: str, current_name: str = "") -> str:
    text = _clean_affiliation_text(raw)
    folded = text.casefold()
    current = _clean_affiliation_text(current_name)
    current_folded = current.casefold()
    raw_tokens = set(re.findall(r"[a-z0-9]+", folded))
    registry_candidates = {
        name for token in raw_tokens
        for name in _INSTITUTION_REGISTRY_BY_TOKEN.get(token, ())
    }
    candidates = []
    for name in registry_candidates:
        match = re.search(
            r"(?<![A-Za-z])" + re.escape(name.casefold()) + r"(?![A-Za-z])",
            folded)
        if not match:
            continue
        expandable = current in GENERIC_INSTITUTION_NAMES
        related = (
            not current or expandable or is_suspicious_institution_name(current)
            or current_folded in name.casefold()
            or name.casefold() in current_folded
        )
        if not related:
            continue
        exact_relation = int(
            bool(current) and not expandable
            and name.casefold() == current_folded)
        prefix_relation = int(
            bool(current) and (
                name.casefold().startswith(current_folded)
                or current_folded.startswith(name.casefold())))
        candidates.append(
            (exact_relation, prefix_relation, len(name), -match.start(), name))
    return max(candidates)[-1] if candidates else ""


def canonical_institution(name: str) -> str:
    value = _apply_institution_aliases(_clean_affiliation_text(name))
    registered = _registered_institution(value, value)
    if registered and (
            is_suspicious_institution_name(value)
            or registered.casefold() in value.casefold()
            or value.casefold() in registered.casefold()):
        value = registered
    match = re.match(
        r"^(.+?\bUniversity)\s+(?:Faculty|School|Department|College)\b",
        value, re.I)
    return _apply_institution_aliases(
        match.group(1).strip() if match else value)


def _raw_institution_alias(raw: str) -> str:
    text = _clean_affiliation_text(raw)
    for pattern, canonical in RAW_INSTITUTION_ALIASES:
        if re.search(pattern, text, re.I):
            return canonical
    return ""


def resolve_institution_from_raw(raw: str, current_name: str = "") -> str:
    direct = _raw_institution_alias(raw)
    current = _clean_affiliation_text(current_name)
    if direct and (
            not current
            or current in GENERIC_INSTITUTION_NAMES
            or is_suspicious_institution_name(current)
            or direct.casefold().startswith(current.casefold())):
        return canonical_institution(direct)
    registered = _registered_institution(raw, current_name)
    if registered:
        return canonical_institution(registered)
    return ""


def institution_from_raw(
        raw: str, *, allow_remote: bool = True) -> tuple[str, str] | None:
    original = raw
    raw = _clean_affiliation_text(raw)
    raw = re.sub(r"^[\d\s*†‡(),.-]+", "", raw)
    if len(raw) < 5:
        return None
    if re.match(
            r"^(abstract|keywords?|introduction|research|fine[- ]tuning|"
            r"limited task|correspondence|computational|deep learning)\b",
            raw, re.I):
        return None
    group = ""
    for name, pattern in GROUPS:
        if re.search(pattern, raw, re.I):
            group = name
            break

    english = resolve_english_institution(
        raw, country_from_raw(original), allow_remote=allow_remote)
    if english:
        return canonical_institution(english), group

    registered = resolve_institution_from_raw(original)
    if registered:
        return registered, group

    # A composite affiliation names its parts in the local language:
    # "Institut de Physique Théorique, Université Paris-Saclay, CNRS, CEA,
    # Gif-sur-Yvette, France". ROR holds no record for the whole string and the
    # English-only patterns below match none of the parts, so all four
    # affiliations of that paper were dropped. ROR does know the parts, so ask
    # it about each one that names an organisation and take the first it
    # recognises — that is also what turns the local-language name into the
    # English one the DB stores ("Université Paris-Saclay" → "University of
    # Paris-Saclay", "Sorbonne Université" → "Sorbonne University").
    for segment in re.split(r"[,;|]", raw):
        segment = segment.strip(" ,;:-()")
        if (not (5 <= len(segment) <= 120)
                or not _ORGANISATION_CUES.search(segment)):
            continue
        english = resolve_english_institution(
            segment, country_from_raw(original), allow_remote=allow_remote)
        if english:
            return canonical_institution(english), group

    parts = [
        part.strip(" ,;:-") for part in re.split(r"[,;|]", raw)
        if part.strip()
    ]
    preferred = [
        part for part in parts if re.search(
            r"\b(university|institute|laborator|academy|college|hospital|"
            r"centre|center|network)\b|Microsoft Research|CNRS|ETH|MIT|Caltech",
            part, re.I)
    ]
    candidate = preferred[-1] if preferred else raw
    candidate = re.sub(
        r"^(department|school|faculty|division|laboratory of)\b.*?,\s*",
        "", candidate, flags=re.I)
    candidate = re.sub(
        r"^(?:USA|UK|Canada|China|Germany|France)\s*\d*\s*", "",
        candidate, flags=re.I)
    candidate = re.sub(r"\s+", " ", candidate).strip(" ,;:-")

    patterns = [
        r"\bThe University of [A-Z][A-Za-z .&'’()-]+",
        r"\bUniversity of [A-Z][A-Za-z .&'’()-]+",
        r"\b[A-Z][A-Za-z .&'’()-]+ Institute of Technology\b",
        r"\b[A-Z][A-Za-z .&'’()-]+ (?:University|Institute|Academy|College|"
        r"Hospital|Centre|Center|Network)\b",
        r"\bMicrosoft Research\b",
    ]
    matches = [
        match.group(0).strip(" ,;:-")
        for pattern in patterns for match in re.finditer(pattern, candidate)
    ]
    if matches:
        candidate = max(matches, key=lambda value: (len(value), value))
    elif not re.search(r"\b(?:MIT|ETH|CNRS)\b", candidate):
        return None
    candidate = canonical_institution(candidate)
    if (len(candidate) < 5 or len(candidate) > 180
            or is_suspicious_institution_name(candidate)):
        return None
    return candidate, group


_SCOPUS_RECORD_CACHE = None
SCOPUS_RECORD_CACHE_PATH = ROOT / ".cache" / "scopus_affiliations.json"


def _load_scopus_record_cache() -> dict:
    global _SCOPUS_RECORD_CACHE
    if _SCOPUS_RECORD_CACHE is None:
        try:
            _SCOPUS_RECORD_CACHE = json.loads(
                SCOPUS_RECORD_CACHE_PATH.read_text(encoding="utf-8"))
        except Exception:
            _SCOPUS_RECORD_CACHE = {}
    return _SCOPUS_RECORD_CACHE

def scopus_parent_institution(scopus_id: str) -> str:
    return SCOPUS_AFFILIATION_PARENT_BY_ID.get(str(scopus_id or "").strip(), "")


def cached_scopus_parent(doi: str, title: str,
                         affiliation_name: str) -> str:
    cache = _load_scopus_record_cache()
    record = cache.get(clean_doi(doi).lower()) if doi else None
    if not isinstance(record, dict):
        record = cache.get("title:" + norm(title))
    if not isinstance(record, dict):
        return ""
    wanted = norm(affiliation_name)
    for affiliation in record.get("affiliations") or []:
        if norm(str(affiliation.get("name") or "")) != wanted:
            continue
        parent = scopus_parent_institution(
            str(affiliation.get("scopus_id") or ""))
        if parent:
            return parent
    return ""


def _format_issn(value) -> str:
    values = re.findall(r"\d{8}", str(value or ""))
    return "; ".join(f"{v[:4]}-{v[4:]}" for v in values)


def scopus_bibliography(payload: dict) -> dict:
    """Normalize Scopus Abstract Retrieval metadata into database fields."""
    core = payload.get("coredata") or {}
    doi = clean_doi(str(core.get("prism:doi") or ""))
    return {
        "title": str(core.get("dc:title") or "").strip(),
        "journal": str(core.get("prism:publicationName") or "").strip(),
        "date": str(core.get("prism:coverDate") or "").strip(),
        "doi": doi,
        "url": external_url(doi, ""),
        "volume": str(core.get("prism:volume") or "").strip(),
        "issue": str(core.get("prism:issueIdentifier") or "").strip(),
        "pages": str(core.get("prism:pageRange") or "").strip(),
        "publisher": str(core.get("dc:publisher") or "").strip(),
        "issn": _format_issn(core.get("prism:issn")),
        "eissn": _format_issn(core.get("prism:eIssn")),
        "document_type": str(core.get("subtypeDescription") or "").strip(),
        "scopus_eid": str(core.get("eid") or "").strip(),
        "source": "scopus",
    }


def scopus_author_pairs(doi: str, title: str, authors) -> dict[str, str]:
    """Record author → the institution Scopus recorded for them.

    Scopus writes "Way S.F." where the record says "Samuel F. Way", so the
    surname is compared and the first initial has to agree — a corpus this
    size has many authors sharing a surname, and crediting the wrong one is
    worse than crediting nobody. An author with several affiliations is left
    out: which is theirs is exactly the ambiguity this whole path exists to
    avoid guessing at.
    """
    if isinstance(authors, str):
        authors = [x.strip() for x in re.split(r"[,;]", authors) if x.strip()]
    record = {}
    for name in authors or []:
        parts = [x for x in re.split(r"\s+", str(name).strip()) if x]
        if parts:
            record.setdefault(_fold(parts[-1]), (str(name), _fold(parts[0])[:1]))
    if not record:
        return {}

    fetched = fetch_scopus_record(doi, title, want_authors=True) or {}
    out: dict[str, str] = {}
    for row in fetched.get("author_affiliations") or []:
        surname = _fold(row.get("surname") or
                        (row.get("indexed_name") or " ").split()[0])
        found = record.get(surname)
        if not found:
            continue
        name, initial = found
        given = _fold(row.get("initials") or "")[:1]
        if initial and given and initial != given:
            continue
        affiliations = row.get("affiliations") or []
        if len(affiliations) == 1 and name not in out:
            out[name] = affiliations[0]
    return out


# A department, a college or a named centre is part of an institution, not one.
# ROR knows the ones that are independent — "Center for Open Science" has a
# record, "Center for Computational Science and Engineering" does not — so the
# name alone cannot decide.
_SUB_UNIT_NAME = re.compile(
    r"(?i)^(college|department|dept|school|faculty|division|graduate school|"
    r"centre|center|laborator)\b")


def drop_sub_unit_institutions(conn: sqlite3.Connection) -> dict:
    """Remove institutions that name part of one, keeping ROR-known bodies.

    Scopus names were minted unchecked before `scopus_institution_name`
    existed, so the rows are already in the DB. They cannot be repaired into
    their parent — Scopus does not say which university a college belongs to —
    so they are removed rather than left to distort an institution ranking.
    """
    try:
        from .lib.ror_index import RorIndex
    except ImportError:
        from lib.ror_index import RorIndex
    index = RorIndex()
    try:
        doomed = []
        for institution_id, name, ror_id in conn.execute(
                "SELECT institution_id, institution_name, COALESCE(ror_id,'')"
                " FROM institutions"):
            if ror_id or not _SUB_UNIT_NAME.match(name or ""):
                continue
            if not (index.available and index.resolve(name)):
                doomed.append(institution_id)
    finally:
        index.close()
    if not doomed:
        return {"institutions": 0, "paper_links": 0, "author_links": 0}
    marks = ",".join("?" * len(doomed))
    author_links = conn.execute(
        f"SELECT COUNT(*) FROM paper_author_institutions"
        f" WHERE institution_id IN ({marks})", doomed).fetchone()[0]
    paper_links = conn.execute(
        f"SELECT COUNT(*) FROM paper_institutions"
        f" WHERE institution_id IN ({marks})", doomed).fetchone()[0]
    for table in ("paper_author_institutions", "paper_institutions",
                  "institution_aliases", "institutions"):
        conn.execute(f"DELETE FROM {table} WHERE institution_id IN ({marks})",
                     doomed)
    return {"institutions": len(doomed), "paper_links": paper_links,
            "author_links": author_links}


def scopus_institution_name(affilname: str, country: str = "") -> str:
    """A Scopus affiliation name, or "" when it names only part of one.

    Scopus indexes the unit it was given, so a paper comes back under "College
    of Engineering and Applied Science" with the university it belongs to
    nowhere in the record. The PDF path already puts every candidate past ROR;
    Scopus names skipped that and were minted as institutions unchecked.
    """
    name = canonical_institution(str(affilname or "").strip())
    if not name:
        return ""
    if not _SUB_UNIT_NAME.match(name):
        return name
    # ROR decides, offline. Its records are what separate a real organisation
    # whose name begins that way — Center for Open Science, Center for
    # Theoretical Biological Physics — from a university's internal unit.
    try:
        from .lib.ror_index import RorIndex
    except ImportError:
        try:
            from lib.ror_index import RorIndex
        except ImportError:
            return name
    index = RorIndex()
    try:
        if not index.available:
            return name
        return name if index.resolve(name, country) else ""
    finally:
        index.close()


def scopus_author_affiliations(payload: dict) -> list[dict]:
    """Each indexed author with the institutions Scopus recorded for them.

    Scopus keys an author's affiliations by id against the paper's affiliation
    list, so the mapping is stated rather than parsed. It is the answer for
    papers whose PDF never prints it — "Productivity, prominence" keys its
    byline with lowercase letters that no marker parser saw, and "The
    Increasing Dominance of Teams" was scanned starting at its reference list.
    """
    listed = payload.get("affiliation") or []
    listed = [listed] if isinstance(listed, dict) else listed
    names = {str(item.get("@id") or ""): str(item.get("affilname") or "")
             for item in listed}
    authors = (payload.get("authors") or {}).get("author") or []
    authors = [authors] if isinstance(authors, dict) else authors
    out = []
    for author in authors:
        affiliations = author.get("affiliation")
        affiliations = ([affiliations] if isinstance(affiliations, dict)
                        else affiliations or [])
        resolved = [names.get(str(item.get("@id") or ""), "")
                    for item in affiliations]
        resolved = [name for name in resolved if name]
        if not resolved:
            continue
        out.append({
            "indexed_name": str(author.get("ce:indexed-name") or ""),
            "surname": str(author.get("ce:surname") or ""),
            "initials": str(author.get("ce:initials") or ""),
            "affiliations": resolved,
        })
    return out


def fetch_scopus_record(doi: str, title: str = "",
                        want_authors: bool = False) -> dict:
    """Fetch one Scopus record and reuse it for bibliography and affiliations."""
    doi = clean_doi(doi).lower()
    title = re.sub(r"\s+", " ", title or "").strip()
    if not doi and not title:
        return {"bibliography": {}, "affiliations": []}
    # Look under both keys. The cache was largely built before Zotero supplied
    # DOIs, so it holds 3,102 title-keyed records against 818 DOI-keyed ones;
    # keying only by DOI made every Zotero-enriched paper a cache miss and
    # turned a 15-minute rebuild into a 5-hour one.
    cache_key = doi or "title:" + norm(title)
    cache = _load_scopus_record_cache()
    cached = cache.get(cache_key)
    if not (isinstance(cached, dict) and "bibliography" in cached) and doi and title:
        alternate = cache.get("title:" + norm(title))
        if isinstance(alternate, dict) and "bibliography" in alternate:
            cached = alternate
    if isinstance(cached, dict) and "bibliography" in cached:
        # Entries written before author-level affiliations were read have no
        # such key. Re-fetching all 4,234 of them to add a field almost no
        # caller needs would be wasteful, so only a caller that asks for the
        # mapping pays for it.
        if not (want_authors and "author_affiliations" not in cached):
            return cached
    legacy_affiliations = cached if isinstance(cached, list) else []
    record = {"bibliography": {}, "affiliations": legacy_affiliations}
    try:
        import requests
        from lib.citedby import scopus
        ok, _ = scopus.available()
        if ok:
            query = (f'DOI("{doi}")' if doi else
                     f'TITLE("{title.replace(chr(34), " ")}")')
            search = requests.get(
                scopus.SCOPUS_SEARCH_URL, headers=scopus.headers(),
                params={"query": query, "count": 5 if title and not doi else 1},
                timeout=30)
            entries = ((search.json().get("search-results") or {}).get("entry") or []
                       if search.status_code == 200 else [])
            if title and not doi:
                entries = [
                    entry for entry in entries
                    if norm(str(entry.get("dc:title") or "")) == norm(title)
                ]
            eid = entries[0].get("eid", "") if entries else ""
            if eid:
                abstract = requests.get(
                    f"{scopus.SCOPUS_ABSTRACT_URL}/{eid}",
                    headers=scopus.headers(), params={"view": "FULL"}, timeout=30)
                if abstract.status_code == 200:
                    payload = abstract.json().get("abstracts-retrieval-response") or {}
                    affiliations = []
                    for aff in payload.get("affiliation") or []:
                        name = scopus_institution_name(
                            str(aff.get("affilname") or ""),
                            str(aff.get("affiliation-country") or ""))
                        if name:
                            affiliations.append({
                                "name": name,
                                "raw_name": str(aff.get("affilname") or name),
                                "country": str(aff.get("affiliation-country") or ""),
                                "scopus_id": str(aff.get("@id") or ""),
                                "source": "scopus",
                            })
                    record = {
                        "bibliography": scopus_bibliography(payload),
                        "affiliations": affiliations,
                        # Scopus indexes who sat where, in the same response
                        # this has always fetched for the paper's institution
                        # list. Reading only the list threw the mapping away.
                        "author_affiliations": scopus_author_affiliations(
                            payload),
                    }
    except Exception:
        pass
    cache[cache_key] = record
    try:
        SCOPUS_RECORD_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
        temp = SCOPUS_RECORD_CACHE_PATH.with_suffix(".tmp")
        temp.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
        os.replace(temp, SCOPUS_RECORD_CACHE_PATH)
    except OSError:
        pass
    return record


def fetch_scopus_affiliations(doi: str) -> list[dict]:
    """Compatibility wrapper for affiliation-only callers."""
    return fetch_scopus_record(doi).get("affiliations") or []


_PDF_FILES = None


def locate_pdf(paper: dict, frontmatter: dict) -> Path | None:
    for value in (paper.get("pdf_path"), frontmatter.get("pdf")):
        if value and Path(str(value)).exists():
            return Path(str(value))
    try:
        from config_loader import get_zotero_dir
        root = Path(get_zotero_dir())
    except Exception:
        return None
    global _PDF_FILES
    if _PDF_FILES is None:
        try:
            _PDF_FILES = list(root.rglob("*.pdf"))
        except OSError:
            _PDF_FILES = []
    title_tokens = re.findall(r"[a-z0-9]+", str(paper.get("title") or "").lower())[:10]
    best, best_score = None, 0
    for path in _PDF_FILES:
        stem = path.stem.lower()
        score = sum(token in stem for token in title_tokens)
        if score > best_score:
            best, best_score = path, score
    return best if best_score >= max(3, len(title_tokens) // 2) else None


_AUTHOR_INFO_CUE = re.compile(
    # ACS prints the heading as "■AUTHOR INFORMATION"; anchoring on the letter
    # alone missed it, so an ACS paper's only affiliation block — which sits in
    # the back matter — never entered any window.
    r"(?im)^[\s\W]{0,4}(?:author information|affiliations?|published online|"
    r"received:).*$")


def author_information_text(text_path: Path) -> str:
    """The whole of `text.md`, for finding a back-matter author-info block.

    `affiliation_window` caps at 24,000 characters because it looks for front
    matter. ACS prints "AUTHOR INFORMATION" at the *end* of the article —
    character 71,392 of 119,073 in "A Perspective on Foundation Models in
    Chemistry" — so that cap hides exactly the block this needs.
    """
    try:
        return text_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def author_information_pairs(text: str, authors) -> dict[str, str]:
    """Author → affiliation from a back-matter author-information block.

    ACS writes one entry per author as "Name −Affiliation, City, Country;"
    under "■AUTHOR INFORMATION", using U+2212 MINUS SIGN as the separator, and
    prints no superscripts anywhere — so the marker machinery reads nothing
    and the paper falls back to linking every author to every institution.
    The name is right there in front of the separator, so the mapping is
    stated, not inferred.

    Only this paper's own author surnames are accepted, which keeps the
    "Corresponding Authors" / "Authors" subheadings and any editor credit out.
    """
    if isinstance(authors, str):
        authors = [x.strip() for x in re.split(r"[,;]", authors) if x.strip()]
    surnames: dict[str, str] = {}
    for name in authors or []:
        parts = [p for p in re.split(r"\s+", str(name).strip()) if p]
        if parts:
            surnames.setdefault(_fold(parts[-1]), str(name))

    out: dict[str, str] = {}
    for head in _AUTHOR_INFO_CUE.finditer(text):
        block = text[head.end():head.end() + 2500]
        block = re.split(
            r"(?im)^[\s\W]{0,4}(?:author contributions|notes|acknowledg|"
            r"references|funding|supporting information)\b", block)[0]
        pieces = re.split(r"[−–—]", block)
        for index, chunk in enumerate(pieces[1:], 1):
            affiliation = re.split(
                r";|\borcid\b|\bemail\b|https?://", chunk, flags=re.I)[0]
            affiliation = re.sub(r"\s+", " ", affiliation).strip(" ,.;:-")
            if not (5 <= len(affiliation) <= 240):
                continue
            # The name sits at the end of the piece before the separator.
            tokens = [t for t in re.split(r"[\s]+", pieces[index - 1].strip())
                      if t]
            for token in reversed(tokens[-3:]):
                resolved = surnames.get(_fold(token))
                if resolved and resolved not in out:
                    out[resolved] = affiliation
                    break
    return out


def author_information_affiliations(text: str) -> list[str]:
    """Affiliation strings from the same block, without the names.

    Kept because `reconcile_affiliations` wants segments, not a mapping; the
    two share one parse so a layout fix cannot help one and miss the other.
    """
    out = []
    for head in _AUTHOR_INFO_CUE.finditer(text):
        block = text[head.end():head.end() + 2500]
        block = re.split(
            r"(?im)^[\s\W]{0,4}(?:author contributions|notes|acknowledg|"
            r"references|funding|supporting information)\b", block)[0]
        for chunk in re.split(r"[−–—]", block)[1:]:
            chunk = re.split(
                r";|\borcid\b|\bemail\b|https?://", chunk, flags=re.I)[0]
            chunk = re.sub(r"\s+", " ", chunk).strip(" ,.;:-")
            if 5 <= len(chunk) <= 240:
                out.append(chunk)
    return out


def _pdf_text_for_affiliations(pdf_path: Path | None, text_path: Path) -> str:
    """Front matter only: leading PDF pages, author-info back matter, pre-abstract text.

    The affiliation block lives in front matter. The previous tail window
    (``text.md`` ``lines[-600:]``) fed the *reference list* to the institution
    parser, which minted institutions out of cited paper titles — "A Neural
    Network", "A Dynamic Network", "Acer Liquid Network", "Application of a
    Convolutional Neural Network". Measured across 120 papers that window
    contributed zero unique institutions, so it is not read at all.

    Back-matter PDF pages are kept only when they actually carry an
    author-information cue; that is what "Author information blocks" means in
    the affiliation contract, and it keeps Nature-style back matter working
    without re-admitting the bibliography.
    """
    chunks = []
    if pdf_path and pdf_path.exists():
        try:
            import fitz
            doc = fitz.open(pdf_path)
            chunks = [doc[i].get_text("text") for i in range(min(3, len(doc)))]
            for index in range(max(3, len(doc) - 3), len(doc)):
                page = doc[index].get_text("text")
                if _AUTHOR_INFO_CUE.search(page):
                    chunks.append(page)
            doc.close()
        except Exception:
            chunks = []
    try:
        text = text_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        text = ""
    chunks.append("\n".join(text.splitlines()[:260]))
    for match in _AUTHOR_INFO_CUE.finditer(text):
        chunks.append(text[max(0, match.start() - 400):match.start() + 1200])
    return "\n".join(chunks)

_MONTHS = {
    name.lower(): f"{index:02d}" for index, name in enumerate(
        ("January", "February", "March", "April", "May", "June", "July",
         "August", "September", "October", "November", "December"), 1)
}


def _human_date(value: str) -> str:
    match = re.search(
        r"\b(\d{1,2})\s+(" + "|".join(_MONTHS) + r")\s+((?:19|20)\d{2})\b",
        value or "", re.I)
    if not match:
        return ""
    return f"{match.group(3)}-{_MONTHS[match.group(2).lower()]}-{int(match.group(1)):02d}"


def pdf_bibliography(pdf_text: str) -> dict:
    """Extract publisher-facing metadata from the PDF's front/back matter."""
    result = {}
    date_labels = {
        "received_date": r"received(?:\s*:|\s+)",
        "accepted_date": r"accepted(?:\s*:|\s+)",
        "published_online_date": r"published\s+online(?:\s*:|\s+)",
    }
    for field, label in date_labels.items():
        match = re.search(
            label + r"\s*(\d{1,2}\s+[A-Za-z]+\s+(?:19|20)\d{2})",
            pdf_text, re.I)
        if match:
            result[field] = _human_date(match.group(1))

    doi_match = re.search(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", pdf_text, re.I)
    if doi_match:
        result["doi"] = clean_doi(doi_match.group(0))

    # Common publisher running header, e.g.
    # "Nature Methods | Volume 21 | August 2024 | 1470–1480".
    header = re.search(
        r"(?m)^\s*([^|\n]{2,120}?)\s*\|\s*Volume\s+([^|\n]+?)\s*\|"
        r"\s*(?:[A-Za-z]+\s+)?(?:19|20)\d{2}\s*\|\s*"
        r"([A-Za-z]?\d+(?:\s*[-–—]\s*[A-Za-z]?\d+)?)\s*$",
        pdf_text, re.I)
    if header:
        journal = re.sub(r"\s+", " ", header.group(1)).strip()
        if not re.search(r"copyright|http|doi", journal, re.I):
            result["journal"] = journal
        result["volume"] = header.group(2).strip()
        result["pages"] = re.sub(r"\s*[-–—]\s*", "-", header.group(3))

    # An issue identifier carries a digit ("Issue 24", "No. 3-4", "Issue S1").
    # Bare words must not match: prose like "the issue of strategic behavior"
    # once put issue="of" into a NeurIPS paper's record.
    issue = re.search(
        r"\b(?:Issue|No\.)\s+([A-Za-z]?\d+(?:[.-]\d+)?[A-Za-z]?)\b",
        pdf_text, re.I)
    if issue:
        result["issue"] = issue.group(1)
    return result


def reconcile_bibliography(local: dict, scopus: dict, pdf: dict) -> dict:
    """Zotero-backed local metadata is ground truth; Scopus and PDF fill gaps only.

    Zotero records are transcribed from the publisher's own record, so they are
    authoritative for bibliographic fields. Scopus and PDF front matter are
    gap-fillers, never overrides. The previous behaviour did the opposite —
    ``if scopus: result[field] = scopus[field]`` overwrote every field Scopus
    returned, and the PDF regex pass then overwrote that in turn, so a correct
    publisher-sourced volume/issue/pages/journal could be replaced by a Scopus
    variant or by a running-header misparse.
    """
    fields = (
        "title", "journal", "date", "doi", "url", "volume", "issue", "pages",
        "publisher", "issn", "eissn", "document_type", "scopus_eid",
        "received_date", "accepted_date", "published_online_date",
    )
    result = {field: str(local.get(field) or "").strip() for field in fields}
    used = ["zotero-local"] if any(result.values()) else []
    field_sources = {field: "zotero-local"
                     for field in fields if result[field]}

    # `scopus_eid` has no local counterpart, so Scopus stays authoritative there.
    for label, source, owned in (("scopus", scopus, ("scopus_eid",)),
                                 ("pdf", pdf, ())):
        if not source:
            continue
        filled = False
        for field in fields:
            value = str(source.get(field) or "").strip()
            if not value:
                continue
            if result.get(field) and field not in owned:
                continue
            result[field] = value
            # Which source supplied each field, so a caller can tell a
            # publisher-registered value from one scraped off a page.
            field_sources[field] = label
            filled = True
        if filled:
            used.append(label)

    if not result["date"] and result["published_online_date"]:
        result["date"] = result["published_online_date"]
    if result["doi"] and not result["url"]:
        result["url"] = external_url(result["doi"], "")
        field_sources["url"] = field_sources.get("doi", "")
    result["source"] = "+".join(used) or "empty"
    result["field_sources"] = field_sources
    return result


def reconcile_affiliations(
        scopus_records: list[dict], pdf_text: str,
        fallback_lines: list[str], *, offline: bool = False,
        paper_title: str = "", authors=()) -> list[dict]:
    """Validate Scopus against PDF text and add institutions missing in Scopus."""
    flat = re.sub(r"\s+", " ", pdf_text)
    normalized_pdf = norm(flat)
    title_key = norm(paper_title)
    author_tokens = _person_name_tokens(authors)
    out = {}

    def from_own_title(name: str) -> bool:
        """Reject the paper's own title leaking in as an institution.

        Front matter starts with the title, so a segment that is contained in
        it ("A Dynamic Network", "A Novel Framework for Dynamic Semantic
        Network") is a title fragment, not an affiliation.
        """
        key = norm(name)
        return bool(title_key) and len(key) >= 8 and key in title_key

    for rec in scopus_records:
        original_name = str(rec.get("name") or "")
        english = resolve_english_institution(
            original_name, str(rec.get("country") or ""),
            allow_remote=not offline)
        parent = scopus_parent_institution(
            str(rec.get("scopus_id") or ""))
        # Scopus is never hierarchy authority: its parent rollup is the last
        # resort, behind the resolved English name and the reported name.
        name = canonical_institution(english or original_name or parent)
        if is_suspicious_institution_name(name):
            name = resolve_institution_from_raw(
                str(rec.get("raw_name") or original_name), name)
        if not name or is_suspicious_institution_name(name):
            continue
        tokens = [x for x in re.findall(r"[a-z0-9]+", norm(name))
                  if x not in {"of", "the", "and", "for"}]
        # Every distinctive token must appear; the old "len-1" slack confirmed
        # any common word pair (e.g. "neural"+"network") against the paper body.
        confirmed = bool(tokens) and all(t in normalized_pdf for t in tokens)
        out[norm(name)] = {
            **rec, "name": name,
            "source": "scopus+pdf" if confirmed else "scopus-unconfirmed",
        }

    segments = list(fallback_lines)
    # An author-information block names each affiliation without a superscript
    # marker, so the splitter below cannot reach it.
    segments.extend(author_information_affiliations(pdf_text))
    # Split on superscript affiliation markers. The digit may be glued to the
    # next word ("2Princeton") or spaced off it ("5 UC Berkeley"); the old
    # pattern only handled the glued form and silently swallowed the rest of
    # the line, losing every institution after the first marker.
    for line in list(fallback_lines) + [flat]:
        segments.extend(_AFFILIATION_MARKER.split(line))
    for raw in segments:
        raw = _strip_leading_author_names(
            _trim_affiliation_segment(raw), author_tokens)
        # An affiliation line is short. 600 characters was a third of a page of
        # prose, which is how abstract and body text became institution names.
        if not raw or len(raw) > 240:
            continue
        parsed = institution_from_raw(raw, allow_remote=not offline)
        if not parsed:
            continue
        name, _group = parsed
        name = canonical_institution(name)
        if not name or from_own_title(name) or is_suspicious_institution_name(name):
            continue
        key = norm(name)
        country = country_from_raw(raw)
        if key in out:
            out[key]["source"] = "scopus+pdf"
            out[key]["country"] = out[key].get("country") or country
        else:
            out[key] = {
                "name": name, "raw_name": raw, "country": country,
                "scopus_id": "", "source": "pdf",
            }
    return list(out.values())


SIDECAR_NAME = "bibliography.json"
SIDECAR_SCHEMA = "bibliography-sidecar-1"


DOI_RESOLUTION_SCHEMA = """
CREATE TABLE IF NOT EXISTS doi_resolutions (
 slug TEXT PRIMARY KEY, doi TEXT NOT NULL, source TEXT NOT NULL,
 matched_title TEXT NOT NULL DEFAULT '', similarity REAL,
 resolved_at TEXT NOT NULL)"""


def ensure_doi_resolution_table(conn: sqlite3.Connection) -> None:
    conn.execute(DOI_RESOLUTION_SCHEMA)


def cached_doi_resolution(conn: sqlite3.Connection, slug: str) -> str:
    """A DOI recovered for this paper by an earlier resolution pass.

    The builder reads DOIs from Zotero, the review frontmatter and the PDF.
    None of those learn anything, so a DOI found by searching OpenAlex or
    Crossref has nowhere to live and would be lost on the next rebuild. This
    table is that home; `resolve_missing_dois.py` writes it.
    """
    try:
        row = conn.execute(
            "SELECT doi FROM doi_resolutions WHERE slug=?", (slug,)).fetchone()
    except sqlite3.OperationalError:      # table absent on an older DB
        return ""
    return clean_doi(row[0]) if row else ""


def load_sidecar(directory: Path) -> dict | None:
    """Read the review-time bibliography sidecar, or None if unusable.

    Written by `run_update_force.write_bibliography_sidecar` while the Zotero
    item, `text.md` and the PDF were all still in hand. Refused when the schema
    is unknown, the Zotero key is missing, or `text.md` changed since capture —
    a stale sidecar must not silently outrank a fresh extraction.
    """
    try:
        payload = json.loads(
            (directory / SIDECAR_NAME).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    if payload.get("schema") != SIDECAR_SCHEMA:
        return None
    if not (payload.get("zotero") or {}).get("key"):
        return None
    recorded = payload.get("text_md_sha256") or ""
    text = directory / "text.md"
    if recorded and text.exists():
        if hashlib.sha256(text.read_bytes()).hexdigest() != recorded:
            return None
    return payload


def fetch_zotero_items() -> list[dict]:
    try:
        from config_loader import get_zotero_api_key, get_zotero_user_id
        key, user = get_zotero_api_key(), get_zotero_user_id()
    except Exception:
        return []
    if not key or not user:
        return []
    out, start = [], 0
    while True:
        url = f"https://api.zotero.org/users/{user}/items/top?format=json&limit=100&start={start}"
        batch = None
        # A single transient 502 used to `break` and hand back a partial
        # library: one such failure at item 3,400 of 5,604 silently dropped 939
        # `zotero_item_key` values, because every unmatched paper simply looks
        # like a paper Zotero does not have.
        for attempt in range(4):
            try:
                batch = request_json(url, {"Zotero-API-Key": key, "User-Agent": "paper-curation-bibliography/1.0"}, 40)
                break
            except Exception as exc:
                print(f"Zotero read retry {attempt + 1}/4 at start={start}: {exc}",
                      file=sys.stderr, flush=True)
                time.sleep(2 ** attempt)
        if batch is None:
            raise RuntimeError(
                f"Zotero library read failed at start={start} after 4 attempts; "
                f"refusing to build with {len(out)} of an unknown item count. "
                "Re-run, or pass --skip-zotero to build without Zotero keys.")
        if not batch:
            break
        out.extend(batch)
        start += len(batch)
        if len(batch) < 100:
            break
    return out


def zotero_match(p: dict, items: list[dict]) -> dict | None:
    doi, arxiv, title = clean_doi(p.get("doi", "")), clean_arxiv(p.get("arxiv", "")), norm(p.get("title", ""))
    for item in items:
        d = item.get("data", {})
        if doi and clean_doi(d.get("DOI", "")).casefold() == doi.casefold():
            return item
        if arxiv and arxiv_from(d.get("archiveID", ""), d.get("url", "")) == arxiv:
            return item
    candidates = [x for x in items if norm(x.get("data", {}).get("title", "")) == title]
    return candidates[0] if len(candidates) == 1 else None


def _zotero_author_creator(display_name: str) -> dict:
    """Convert a publication-index display name to a Zotero person creator."""
    name = re.sub(r"\s+", " ", display_name or "").strip()
    if "," in name:
        last_name, first_name = (part.strip() for part in name.split(",", 1))
    elif " " in name:
        first_name, last_name = name.rsplit(" ", 1)
    else:
        first_name, last_name = "", name
    return {
        "creatorType": "author",
        "firstName": first_name,
        "lastName": last_name,
    }


def _zotero_creator_name(creator: dict) -> str:
    return re.sub(
        r"\s+", " ",
        f"{creator.get('firstName', '')} {creator.get('lastName', '')}".strip()
        or str(creator.get("name") or "").strip(),
    )


def _zotero_title(item: dict) -> str:
    return str((item.get("data") or {}).get("title") or "")


def _titles_agree(item: dict, bibliography: dict) -> bool:
    """Whether a Zotero item and a bibliography record describe one paper.

    An empty title on either side carries no evidence, so it is not treated as
    a conflict. Everything else is compared on normalized text: the 308
    mismatched rows measured in this corpus sat below 0.6 similarity while
    genuine subtitle and punctuation drift stayed far above it.
    """
    item_title = norm(_zotero_title(item))
    record_title = norm(str(bibliography.get("title") or ""))
    if not item_title or not record_title:
        return True
    if item_title == record_title:
        return True
    return difflib.SequenceMatcher(
        None, item_title, record_title).ratio() >= 0.6


def patch_zotero(item: dict, bibliography: dict) -> bool | None:
    """Patch Zotero with the accepted formal-publication record.

    Returns True when the item was patched, None when the record already
    matches (nothing to write), False on failure. Callers that count
    updates can keep truth-testing the result; callers that report
    success/failure must treat None as "already up to date", not failure.
    """
    if not bibliography.get("doi"):
        return False
    # Never write into a library item describing a different paper. Zotero item
    # RM7J55RG holds "The reorganization of the American innovation ecosystem
    # and the challenge of translating science" (Industrial and Corporate
    # Change, Arora et al.) — and the DOI and URL of a 2021 Frontiers paper by
    # Altman and Cohen, because a patch wrote them there. DOI and url are the
    # two fields this function writes that identify the work itself, so a
    # mismatched title makes the write destructive to the user's own library.
    if not _titles_agree(item, bibliography):
        print(f"Zotero update refused ({item.get('key')}): title mismatch — "
              f"item={_zotero_title(item)!r} record={bibliography.get('title')!r}",
              file=sys.stderr)
        return False
    try:
        from config_loader import get_zotero_api_key, get_zotero_user_id
        key, user = get_zotero_api_key(), get_zotero_user_id()
        field_map = {
            "doi": "DOI",
            "journal": "publicationTitle",
            "date": "date",
            "url": "url",
            "volume": "volume",
            "issue": "issue",
            "pages": "pages",
            "publisher": "publisher",
        }
        # A DOI recovered by regex from the page has no authority to redefine
        # a library item. `pdf_bibliography` takes the first DOI in its window,
        # and the window reaches the reference list: the Industrial and
        # Corporate Change paper cites Altman and Cohen, so its scraped DOI was
        # theirs, Zotero held no DOI of its own to outrank it, and the patch
        # wrote a Frontiers DOI onto item RM7J55RG. Identity fields may only be
        # written from a registered record.
        sources = bibliography.get("field_sources") or {}
        scraped = {field for field in ("doi", "url")
                   if sources.get(field) == "pdf"}
        patch = {
            zotero_field: bibliography[source_field]
            for source_field, zotero_field in field_map.items()
            if bibliography.get(source_field) and source_field not in scraped
        }
        if scraped:
            print(f"Zotero identity fields not written ({item.get('key')}): "
                  f"{sorted(scraped)} came from the PDF, not a registry",
                  file=sys.stderr)
        issns = "; ".join(
            value for value in (bibliography.get("issn"), bibliography.get("eissn"))
            if value)
        if issns:
            patch["ISSN"] = issns
        patch["itemType"] = "journalArticle"
        current = item.get("data") or {}
        proposed_authors = [
            str(author).strip() for author in bibliography.get("authors", [])
            if str(author).strip()
        ]
        if proposed_authors:
            current_creators = current.get("creators") or []
            current_authors = [
                _zotero_creator_name(creator) for creator in current_creators
                if creator.get("creatorType") == "author"
            ]
            if current_authors != proposed_authors:
                patch["creators"] = [
                    _zotero_author_creator(author) for author in proposed_authors
                ] + [
                    creator for creator in current_creators
                    if creator.get("creatorType") != "author"
                ]
        patch = {key_: value for key_, value in patch.items()
                 if str(current.get(key_) or "") != str(value)}
        if not patch:
            return None
        req = urllib.request.Request(
            f"https://api.zotero.org/users/{user}/items/{item['key']}",
            data=json.dumps(patch).encode(), method="PATCH",
            headers={
                "Zotero-API-Key": key,
                "If-Unmodified-Since-Version": str(item.get("version", "")),
                "Content-Type": "application/json",
                "User-Agent": "paper-curation-bibliography/1.0",
            })
        with urllib.request.urlopen(req, timeout=30, context=SSL_CTX) as response:
            return response.status in (200, 204)
    except Exception as exc:
        print(f"Zotero update warning ({item.get('key')}): {exc}", file=sys.stderr)
        return False


def load_entries() -> list[dict]:
    return [p for p in json.loads(INDEX_PATH.read_text(encoding="utf-8")) if (PAPERS_DIR / p.get("slug", "")).is_dir()]


def upsert(conn, table: str, name: str, column: str) -> int:
    key = norm(name)
    id_col = "author_id" if table == "authors" else "institution_id" if table == "institutions" else "group_id"
    row = conn.execute(f"SELECT {id_col} FROM {table} WHERE normalized_name=?", (key,)).fetchone()
    if row:
        return row[0]
    return conn.execute(f"INSERT INTO {table} ({column},normalized_name,source) VALUES (?,?,?)" if table == "institutions" else f"INSERT INTO {table} ({column},normalized_name) VALUES (?,?)", (name, key, "text.md:normalized") if table == "institutions" else (name, key)).lastrowid




def _paper_stable_slug(conn: sqlite3.Connection, paper_id: int,
                       paper_key: str | None) -> str:
    if paper_key:
        return paper_key
    columns = {row[1] for row in conn.execute("PRAGMA table_info(papers)")}
    if "slug" in columns:
        row = conn.execute(
            "SELECT slug FROM papers WHERE paper_id=?", (paper_id,)).fetchone()
        if row and row[0]:
            return str(row[0])
    return str(paper_id)


def _build_unlocked(entries: list[dict], db_path: Path, update_zotero: bool = False,
          skip_zotero: bool = False, offline: bool = False,
          defer_consolidation: bool = False) -> dict:
    total = len(entries)
    print(f"[bibliography] starting {total} papers", flush=True)
    start = time.perf_counter(); db_path.parent.mkdir(parents=True, exist_ok=True)
    # The affiliation organisation registry was retired: it resolved nothing
    # (`institutions.organization_id` was NULL for all 2,339 rows because the
    # resolver never produced a unique candidate), and its entire payload
    # reduced to two usable aliases. Institutions now come straight from Scopus
    # plus PDF front matter, so there is no registry schema to gate on.
    conn = sqlite3.connect(db_path, timeout=60.0)
    # WAL so the review run's ingest thread can write while other processes
    # read, and a busy timeout so a momentary overlap waits instead of raising
    # "database is locked" — the default journal is `delete` with timeout 0.
    conn.execute("PRAGMA journal_mode = WAL")
    conn.execute("PRAGMA busy_timeout = 60000")
    conn.execute("PRAGMA synchronous = NORMAL")
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(SCHEMA)
    ensure_schema_migrations(conn)
    conn.commit()
    conn.execute("PRAGMA foreign_keys = OFF")
    try:
        conn.execute("BEGIN IMMEDIATE")
        ensure_legacy_institution_schema(conn)
        conn.commit()
    except BaseException:
        conn.rollback()
        raise
    finally:
        conn.execute("PRAGMA foreign_keys = ON")
    initialize_institution_registry(conn)
    conn.commit()
    # Review generation writes a per-paper `bibliography.json` sidecar holding
    # the Zotero record it already had in hand. When every paper being built has
    # one, the Zotero library needs no paging at all — that read costs a fixed
    # ~200 s and its failure mode is silent `zotero_item_key` loss.
    sidecars = {p["slug"]: load_sidecar(PAPERS_DIR / p["slug"]) for p in entries}
    need_zotero = any(s is None for s in sidecars.values())
    zitems = ([] if skip_zotero or offline or not need_zotero
              else fetch_zotero_items())
    if entries and not need_zotero:
        print(f"[bibliography] 사이드카 {len(entries)}건 사용 — "
              "Zotero 재조회 생략", flush=True)
    zupdated = 0; resolved = 0
    with conn:
        for index, p in enumerate(entries, 1):
            directory = PAPERS_DIR / p["slug"]
            review = directory / "review.md"
            text = directory / "text.md"
            meta = fm(review)
            title = str(meta.get("title") or p.get("title") or p["slug"]).strip()
            doi = clean_doi(str(meta.get("doi") or p.get("doi") or ""))
            arxiv = clean_arxiv(str(meta.get("arxiv") or p.get("arxiv") or ""))
            sidecar = sidecars.get(p["slug"])
            zitem = zotero_match(
                {"title": title, "doi": doi, "arxiv": arxiv}, zitems
            ) if zitems else None
            # An item describing a different paper is not evidence about this
            # one. Zotero item ZA7W3PFQ is titled "Mapping scientific
            # communities at scale" yet carries the DOI of Blondel's "Fast
            # Unfolding of Communities in Large Networks", so the Louvain paper
            # was stored under the other work's title, journal and pagination —
            # 20 papers reached the DB that way. Zotero stays authoritative for
            # the paper it actually describes.
            if zitem is not None and not _titles_agree(zitem, {"title": title}):
                print(f"[bibliography] Zotero item {zitem.get('key')} describes "
                      f"{_zotero_title(zitem)[:60]!r}, not {title[:60]!r} — "
                      f"ignored", file=sys.stderr)
                zitem = None
            # The sidecar carries the same Zotero record, captured at review
            # time, so it stands in when the library was not paged.
            sidecar_zotero = (sidecar or {}).get("zotero") or {}
            if sidecar_zotero and not _titles_agree(
                    {"data": sidecar_zotero}, {"title": title}):
                sidecar_zotero = {}
            zdata = (zitem.get("data", {}) if zitem else sidecar_zotero)
            zdoi = clean_doi(zdata.get("DOI", ""))
            if not doi and zdoi:
                doi = zdoi
            arxiv = arxiv or arxiv_from(
                zdata.get("archiveID", ""), zdata.get("url", ""), zdoi)
            official = resolve_publication(
                title, doi or zdoi, arxiv
            ) if (not offline and (arxiv or doi.lower().startswith("10.48550"))) else {}
            if official.get("doi"):
                doi = official["doi"]
                resolved += 1
            # A DOI recovered offline by `resolve_missing_dois.py` and kept in
            # `doi_resolutions`. Without this the resolution would not survive:
            # the builder derives `doi` from Zotero, the review frontmatter and
            # the PDF, none of which learn anything, so the next rebuild would
            # blank 2,384 papers again. The table records how each one was
            # matched, so a bad row can be found and dropped.
            if not doi:
                cached = cached_doi_resolution(conn, p["slug"])
                if cached:
                    doi = cached
                    resolved += 1

            # Zotero first: its records are transcribed from the publisher, so
            # they outrank review.md frontmatter (LLM-extracted from the PDF)
            # and the index snapshot. `official` (OpenAlex/Crossref) only
            # matters for arXiv preprints that have since been published, which
            # is a gap Zotero cannot cover, so it stays ahead of the local files
            # but behind Zotero itself.
            local_bib = {
                "title": str(
                    zdata.get("title") or title or ""
                ).strip(),
                "journal": str(
                    zdata.get("publicationTitle") or official.get("journal")
                    or meta.get("journal") or p.get("journal") or ""
                ).strip(),
                "date": str(
                    zdata.get("date") or official.get("date")
                    or meta.get("date") or p.get("date") or ""
                ).strip(),
                "doi": doi,
                "url": external_url(doi, arxiv) or str(zdata.get("url") or ""),
                "volume": str(zdata.get("volume") or "").strip(),
                "issue": str(zdata.get("issue") or "").strip(),
                "pages": str(zdata.get("pages") or "").strip(),
                "publisher": str(zdata.get("publisher") or "").strip(),
                "issn": str(zdata.get("ISSN") or "").strip(),
                "document_type": str(zdata.get("itemType") or "").strip(),
            }
            scopus_record = {} if offline else fetch_scopus_record(doi, title)
            header, raw_affs, _header_conf = extract_header(text)
            pdf_path = locate_pdf(p, meta)
            pdf_text = _pdf_text_for_affiliations(pdf_path, text)
            bibliography = reconcile_bibliography(
                local_bib, scopus_record.get("bibliography") or {},
                pdf_bibliography(pdf_text))
            if len(bibliography["date"]) < 10:
                bibliography["date"] = (
                    date_from_header(header) or bibliography["date"])
            title = bibliography["title"] or title
            doi = bibliography["doi"] or doi

            # Affiliation precedence: the same Scopus response is validated and
            # repaired from source-PDF front/back matter.
            affiliation_records = reconcile_affiliations(
                scopus_record.get("affiliations") or [], pdf_text, raw_affs,
                offline=offline, paper_title=title,
                authors=(sidecar or {}).get("authors")
                        or meta.get("authors") or p.get("authors") or [])
            sources = {record["source"] for record in affiliation_records}
            aff_source = "+".join(sorted(sources)) if sources else "missing"
            conf = 0.95 if "scopus+pdf" in sources else (
                0.8 if affiliation_records else 0.0)
            if update_zotero and zitem and patch_zotero(zitem, bibliography):
                zupdated += 1

            columns = (
                "slug", "title", "publication_date", "journal_name", "doi",
                "arxiv_id", "url", "volume", "issue", "pages", "publisher",
                "issn", "eissn", "document_type", "scopus_eid",
                "received_date", "accepted_date", "published_online_date",
                "bibliography_source", "review_dir", "zotero_item_key",
                "affiliation_source", "affiliation_confidence", "header_raw",
                "metadata_json",
            )
            values = (
                p["slug"], title, bibliography["date"], bibliography["journal"],
                doi, arxiv, bibliography["url"] or external_url(doi, arxiv),
                bibliography["volume"], bibliography["issue"],
                bibliography["pages"], bibliography["publisher"],
                bibliography["issn"], bibliography["eissn"],
                bibliography["document_type"], bibliography["scopus_eid"],
                bibliography["received_date"], bibliography["accepted_date"],
                bibliography["published_online_date"], bibliography["source"],
                rel(directory),
                (zitem.get("key", "") if zitem
                 else zdata.get("key", "") or p.get("zotero_item_key", "")),
                aff_source, conf, header,
                json.dumps({
                    "publication_source": bibliography["source"],
                    "formal_resolution_source": official.get("source", ""),
                    "topics": p.get("topics", []),
                    "pdf_path": str(pdf_path or ""),
                }, ensure_ascii=False),
            )
            updates = ",".join(
                f"{column}=excluded.{column}" for column in columns if column != "slug")
            conn.execute(
                f"INSERT INTO papers ({','.join(columns)}) "
                f"VALUES ({','.join('?' for _ in columns)}) "
                f"ON CONFLICT(slug) DO UPDATE SET {updates}",
                values)
            pid = conn.execute("SELECT paper_id FROM papers WHERE slug=?", (p["slug"],)).fetchone()[0]
            conn.execute("DELETE FROM paper_authors WHERE paper_id=?", (pid,))
            conn.execute("DELETE FROM paper_institutions WHERE paper_id=?", (pid,))
            conn.execute("DELETE FROM paper_author_institutions WHERE paper_id=?", (pid,))
            # Zotero's creator list (captured in the sidecar) is transcribed
            # from the publisher, so it outranks review.md's LLM extraction.
            authors = ((sidecar or {}).get("authors")
                       or meta.get("authors") or p.get("authors") or [])
            if isinstance(authors, str): authors = [x.strip() for x in re.split(r"[,;]", authors) if x.strip()]
            author_ids = {}
            for order, author in enumerate(authors, 1):
                aid = upsert(conn, "authors", str(author).strip(), "display_name")
                author_ids[str(author)] = (aid, order)
                conn.execute("INSERT OR IGNORE INTO paper_authors VALUES (?,?,?,?,?,?)", (pid,aid,order,int(order==1),0,"review.frontmatter/_papers_index"))
            # The byline superscripts say who sat where. Resolved below, once
            # each affiliation has an institution_id.
            markers_by_author, marker_alphabet = read_byline_markers(
                header, authors, text)
            affiliation_by_marker = marker_affiliations(
                header, None, marker_alphabet)
            if not affiliation_by_marker:
                # Same reason as the backfill: a two-column layout prints the
                # affiliations as a footnote that lands after the abstract.
                affiliation_by_marker = marker_affiliations(
                    affiliation_window(text), None, marker_alphabet)
            institution_by_marker = {}
            linked_institution_ids = []
            for record in affiliation_records:
                name = canonical_institution(record["name"])
                raw = record.get("raw_name") or name
                country = country_from_raw(raw) or record.get("country") or ""
                # ROR is the naming authority: it collapses "Stanford"/"Stanford
                # University", "Universität Wien"/"University of Vienna" and
                # 清华大学/"Tsinghua University" onto one record, and it supplies
                # the research umbrella an institute belongs to.
                ror = ror_normalize(raw, name, country, offline=offline)
                name = ror["institution"] or name
                country = ror["country_name"] or country
                iid = resolve_institution_row(
                    conn, name, country, record["source"], ror)
                conn.execute("INSERT OR IGNORE INTO institution_aliases (raw_name,normalized_alias,institution_id) VALUES (?,?,?)", (raw,norm(raw),iid))
                conn.execute("INSERT OR IGNORE INTO paper_institutions (paper_id,institution_id,raw_name,country_name,source) VALUES (?,?,?,?,?)", (pid,iid,raw,country,record["source"]))
                if iid not in linked_institution_ids:
                    linked_institution_ids.append(iid)
                # Tie this institution back to the marker whose text it came
                # from. The prefix test this replaces failed on a line-break
                # hyphen, a department prefix on one side only, or a comma
                # that moved; `affiliation_match_score` compares tokens.
                for marker, text_of_marker in affiliation_by_marker.items():
                    if marker in institution_by_marker:
                        continue
                    if affiliation_match_score(raw, text_of_marker) >= \
                            AFFILIATION_MATCH_FLOOR:
                        institution_by_marker[marker] = iid
                        break
            author_links = [
                (pid, aid, institution_by_marker[marker], marker, order,
                 "pdf.byline-marker")
                for author, (aid, order) in author_ids.items()
                for marker in markers_by_author.get(author, [])
                if marker in institution_by_marker]
            if not author_links and linked_institution_ids:
                # Same rule as the backfill: one affiliation means everyone sits
                # there; several with no superscripts means the split is unknown,
                # so the rows are kept but tagged unresolved.
                # there. One author means every affiliation the paper prints
                # is that author's, however many — an author can hold several
                # appointments and nothing is being guessed. Several of each
                # is the genuinely unknown case.
                if len(linked_institution_ids) == 1:
                    tag = "pdf.sole-affiliation"
                elif len(author_ids) == 1:
                    tag = "pdf.sole-author"
                else:
                    tag = "pdf.unmarked-multi"
                author_links = [(pid, aid, iid, None, order, tag)
                                for aid, order in author_ids.values()
                                for iid in linked_institution_ids]
            conn.executemany(
                "INSERT OR IGNORE INTO paper_author_institutions "
                "(paper_id,author_id,institution_id,marker,author_order,source) "
                "VALUES (?,?,?,?,?,?)", author_links)
            for kind, path in (("review",review),("text",text)):
                if path.exists(): conn.execute("INSERT OR REPLACE INTO source_documents VALUES (?,?,?,?,?)", (pid,kind,rel(path),sha256(path),path.stat().st_size))
            conn.commit()
            print(f"[bibliography] progress={index}/{total} ({index / total * 100:.1f}%) title={title[:100]}", flush=True)
    # The consolidation passes walk the whole institutions table (~1.6 s), so a
    # streaming ingest defers them and runs them once when the run ends.
    if defer_consolidation:
        stale_pruned = pruned = recountried = reparented = 0
    else:
        stale_pruned = prune_missing_papers(conn)
        pruned = prune_orphan_institutions(conn)
        recountried = consolidate_institution_countries(conn)
        reparented = consolidate_institution_parents(conn)
    conn.commit()
    conn.execute("PRAGMA optimize"); conn.close()
    return {"processed":len(entries),"seconds":round(time.perf_counter()-start,4),"zotero_items_seen":len(zitems),"zotero_updated":zupdated,"formal_publications_resolved":resolved,"stale_papers_pruned":stale_pruned,"orphan_institutions_pruned":pruned,"institution_countries_consolidated":recountried,"institution_parents_cleared":reparented,"db":str(db_path)}


_ROR_INDEX = None
_ROR_MISSING_REPORTED = False


def ror_normalize(raw: str, fallback_name: str, country: str,
                  offline: bool = False) -> dict:
    """Resolve an affiliation string through ROR, falling back to the parser.

    Tries the raw affiliation first — it still carries the comma structure that
    tells an institute apart from its umbrella — then the parser's cleaned name.
    """
    global _ROR_INDEX, _ROR_MISSING_REPORTED
    from lib import ror_index
    if _ROR_INDEX is None:
        _ROR_INDEX = ror_index.RorIndex()
    if not _ROR_INDEX.available:
        if not _ROR_MISSING_REPORTED:
            print("[bibliography] ROR index missing; institution names are not "
                  "normalised. Build it with: python pipeline/lib/ror_index.py",
                  flush=True)
            _ROR_MISSING_REPORTED = True
        return {"institution": "", "parent": "", "ror_id": "",
                "parent_ror_id": "", "country_name": "", "evidence": "no-index"}
    for candidate in (raw, fallback_name):
        if not candidate:
            continue
        outcome = _ROR_INDEX.resolve_affiliation(
            candidate, country, allow_remote=not offline)
        if outcome["evidence"] not in {"unresolved", "empty"}:
            if not outcome.get("parent"):
                outcome = dict(outcome)
                outcome["parent"] = curated_group_for(
                    outcome.get("institution") or candidate)
            return outcome
    curated = curated_group_for(fallback_name or raw)
    return {"institution": "", "parent": curated, "ror_id": "",
            "parent_ror_id": "", "country_name": "",
            "evidence": "curated-group" if curated else "unresolved"}


def curated_group_for(name: str) -> str:
    """Parent group from the operator-curated Scopus table.

    Layered under ROR: it only ever fills a gap, never overrides an edge ROR
    actually records.
    """
    try:
        from lib import affiliation_groups
    except ImportError:
        return ""
    group = affiliation_groups.group_for(name)
    return "" if norm(group) == norm(name) else group


def resolve_institution_row(conn: sqlite3.Connection, name: str, country: str,
                            source: str, ror: dict | None = None) -> int:
    """One row per institution, not one row per (institution, extracted country).

    Keying on ``(normalized_name, country_name_en)`` split single institutions
    across rows whenever the country was absent from one affiliation string and
    present in another: 536 duplicate name groups, 697 surplus rows, "Harvard
    University" three times. An institution is identified by its name; the
    country is an attribute filled in as soon as any affiliation string carries
    it, and the ROR identity plus parent group are filled the same way.
    """
    ror = ror or {}
    key = norm(name)
    row = conn.execute(
        "SELECT institution_id, country_name_en, ror_id, parent_name "
        "FROM institutions WHERE normalized_name=? "
        "ORDER BY country_name_en='', institution_id", (key,)).fetchone()
    if row is None:
        return conn.execute(
            "INSERT INTO institutions (institution_name,normalized_name,"
            "country_name_en,ror_id,parent_name,parent_ror_id,name_source,"
            "source) VALUES (?,?,?,?,?,?,?,?)",
            (name, key, country, ror.get("ror_id", ""),
             ror.get("parent", ""), ror.get("parent_ror_id", ""),
             ror.get("evidence", ""), source)).lastrowid
    institution_id, existing_country, existing_ror, existing_parent = row
    if country and not existing_country:
        conn.execute(
            "UPDATE institutions SET country_name_en=? WHERE institution_id=?",
            (country, institution_id))
    if ror.get("ror_id") and not existing_ror:
        conn.execute(
            "UPDATE institutions SET ror_id=?, name_source=? "
            "WHERE institution_id=?",
            (ror["ror_id"], ror.get("evidence", ""), institution_id))
    if ror.get("parent") and not existing_parent:
        conn.execute(
            "UPDATE institutions SET parent_name=?, parent_ror_id=? "
            "WHERE institution_id=?",
            (ror["parent"], ror.get("parent_ror_id", ""), institution_id))
    return institution_id


def consolidate_institution_parents(conn: sqlite3.Connection) -> int:
    """Re-derive `parent_name` on every rebuild instead of trusting it.

    `parent_name` is a derived field, but `resolve_institution_row` only ever
    *fills* an empty one, so a value written by an older pass was permanent:
    "MIT → University of Amsterdam" (a multi-affiliation line), "Shanghai Jiao
    Tong University → Peking University" and "UC Berkeley → Argonne National
    Laboratory" (a wrong row in the curated table) all survived the rules that
    now reject them, exactly as a stale country survived before the country
    consolidation pass. The parent is therefore recomputed from scratch here.

    Precedence: ROR ancestry decides whenever ROR records any parent at all,
    even when that ancestor is then rejected — Berkeley's ROR parent is the
    University of California System, a governance layer, so Berkeley has no
    research umbrella and the curated table's Argonne claim must not fill the
    hole. The curated table speaks only where ROR is silent, which is the
    Helmholtz Institute Ulm case it exists for.
    """
    try:
        from lib.ror_index import (ADMINISTRATIVE_BODY, UNIVERSITY_SYSTEM,
                                   RorIndex)
        from lib import affiliation_groups
    except ImportError:
        return 0
    index = RorIndex()
    changed = 0
    try:
        rows = conn.execute(
            "SELECT institution_id, institution_name, ror_id, parent_name "
            "FROM institutions").fetchall()
        for institution_id, name, ror_id, current in rows:
            # Headquarters comes from the ROR record itself; the observed site
            # country stays in `country_name_en` and is not touched here.
            if ror_id and index.available:
                root = index.root_org(ror_id)
                hq = (root or {}).get("country_name", "")
                if hq:
                    conn.execute(
                        "UPDATE institutions SET hq_country_name_en=? "
                        "WHERE institution_id=? AND hq_country_name_en<>?",
                        (hq, institution_id, hq))
            parent, parent_ror = "", ""
            ror_states_a_parent = False
            if ror_id and index.available:
                org = index.org(ror_id)
                ror_states_a_parent = bool(org and org.get("parent_id"))
                eligible = index.eligible_parent(ror_id)
                if eligible:
                    parent, parent_ror = eligible["display"], eligible["ror_id"]
            if not parent and not ror_states_a_parent:
                parent = affiliation_groups.group_for(name)
            if parent:
                parent = affiliation_groups.roll_up(parent)
            if parent and (ADMINISTRATIVE_BODY.search(parent)
                           or UNIVERSITY_SYSTEM.search(parent)
                           or norm(parent) == norm(name)):
                parent, parent_ror = "", ""
            if parent != current:
                conn.execute(
                    "UPDATE institutions SET parent_name=?, parent_ror_id=? "
                    "WHERE institution_id=?",
                    (parent, parent_ror, institution_id))
                changed += 1
    finally:
        index.close()
    return changed


def consolidate_institution_countries(conn: sqlite3.Connection) -> int:
    """Set each institution's country by majority vote over its own links.

    First-write-wins let one bad affiliation string decide forever: "Indian
    Institute of Technology Roorkee" was fixed to the United States by a segment
    that packed six affiliations onto one line, and the later, correct
    "4Indian Institute of Technology Roor- kee, India" could not overwrite it.
    A country supported by more source strings beats one supported by fewer.
    """
    updated = 0
    for institution_id, current in conn.execute(
            "SELECT institution_id, country_name_en FROM institutions").fetchall():
        votes = conn.execute(
            "SELECT country_name, COUNT(*) n FROM paper_institutions "
            "WHERE institution_id=? AND country_name<>'' "
            "GROUP BY country_name ORDER BY n DESC, country_name",
            (institution_id,)).fetchall()
        if not votes:
            continue
        winner, top = votes[0]
        if winner == current:
            continue
        tally = dict(votes)
        # A country no source string supports is stale — an earlier cycle wrote
        # it and the link that justified it is gone. Replace it unconditionally.
        # Otherwise a strict majority is required to unseat the incumbent.
        if current not in tally or top > tally[current]:
            conn.execute(
                "UPDATE institutions SET country_name_en=? WHERE institution_id=?",
                (winner, institution_id))
            updated += 1
    return updated


def prune_missing_papers(conn: sqlite3.Connection) -> int:
    """Drop papers whose review directory vanished from the corpus.

    Papers are keyed to ``docs/papers/<slug>``; deleting or renaming a slug
    removed the directory but never the row, so the DB drifted ahead of the
    source index (DB=4197, index=4196) and ``--strict`` failed on the count
    mismatch. The directory on disk is the authority: no directory, no paper.
    Dependent rows are removed explicitly — CASCADE only fires when the
    connection has ``PRAGMA foreign_keys`` on, which not every caller does.
    """
    stale = [row[0] for row in conn.execute(
        "SELECT paper_id, review_dir FROM papers")
        if not (ROOT / row[1]).is_dir()]
    if not stale:
        return 0
    marks = ",".join("?" * len(stale))
    for table, column in (
            ("paper_authors", "paper_id"),
            ("paper_institutions", "paper_id"),
            ("paper_author_institutions", "paper_id"),
            ("source_documents", "paper_id"),
            ("paper_connections", "paper_id"),
            ("paper_connections", "related_paper_id"),
    ):
        try:
            conn.execute(
                f"DELETE FROM {table} WHERE {column} IN ({marks})", stale)
        except sqlite3.OperationalError:
            pass  # optional table absent in minimal test databases
    conn.execute(f"DELETE FROM papers WHERE paper_id IN ({marks})", stale)
    return len(stale)


def prune_orphan_institutions(conn: sqlite3.Connection) -> int:
    """Drop institutions no paper links to any more.

    `paper_institutions` rows are deleted and rewritten per paper, but the
    `institutions` rows they pointed at were never collected, so every name the
    parser ever invented stayed in the table for good — 1,497 of 4,463 rows
    after one rebuild, including all of the pre-fix garbage. The rebuilt link
    table is the authority for which institutions exist.
    """
    orphans = [row[0] for row in conn.execute(
        "SELECT institution_id FROM institutions i WHERE NOT EXISTS("
        " SELECT 1 FROM paper_institutions pi"
        " WHERE pi.institution_id = i.institution_id)")]
    if not orphans:
        return 0
    marks = ",".join("?" * len(orphans))
    conn.execute(
        f"DELETE FROM institution_aliases WHERE institution_id IN ({marks})",
        orphans)
    conn.execute(
        f"DELETE FROM institutions WHERE institution_id IN ({marks})", orphans)
    return len(orphans)


def backfill_author_institutions(db_path: Path, limit: int | None = None,
                                 retry_guessed: bool = True,
                                 offline: bool = False) -> dict:
    """Fill `paper_author_institutions` for papers built before it existed.

    The mapping derives from `text.md` and the paper's existing institution
    rows, so it needs neither Zotero nor Scopus nor the PDF — a full rebuild
    would spend twenty minutes redoing work whose answer is already on disk.

    A paper that already has resolved links is skipped. One whose only links
    are `pdf.unmarked-multi` is retried, because that tag means "the byline
    defeated the parser", and the parser improves: widening it to the spaced,
    comma-and-ORCID and glued marker layouts took a 400-paper sample from 9%
    parsed to 78%. Without the retry those papers would keep their guess
    forever.
    """
    descriptor = bibliography_lock.acquire_bibliography_writer_lock(db_path)
    try:
        conn = sqlite3.connect(db_path, timeout=60.0)
        conn.execute("PRAGMA busy_timeout = 60000")
        conn.execute("PRAGMA foreign_keys = ON")
        try:
            pending = conn.execute(
                "SELECT p.paper_id, p.slug FROM papers p WHERE NOT EXISTS("
                " SELECT 1 FROM paper_author_institutions pai"
                " WHERE pai.paper_id=p.paper_id) ORDER BY p.paper_id").fetchall()
            if retry_guessed:
                pending += conn.execute(
                    "SELECT p.paper_id, p.slug FROM papers p WHERE EXISTS("
                    " SELECT 1 FROM paper_author_institutions pai"
                    " WHERE pai.paper_id=p.paper_id"
                    "   AND pai.source='pdf.unmarked-multi')"
                    " AND NOT EXISTS(SELECT 1 FROM paper_author_institutions pai"
                    "   WHERE pai.paper_id=p.paper_id"
                    "     AND pai.source<>'pdf.unmarked-multi')"
                    " ORDER BY p.paper_id").fetchall()
            if limit:
                pending = pending[:limit]
            filled = linked = skipped = 0
            for pid, slug in pending:
                text = PAPERS_DIR / slug / "text.md"
                if not text.exists():
                    skipped += 1
                    continue
                header = extract_header(text)[0]
                authors = conn.execute(
                    "SELECT a.author_id, a.display_name, pa.author_order"
                    " FROM paper_authors pa JOIN authors a"
                    " ON a.author_id=pa.author_id WHERE pa.paper_id=?"
                    " ORDER BY pa.author_order", (pid,)).fetchall()
                if not authors:
                    skipped += 1
                    continue
                # No early exit on a missing marker map: a single-affiliation
                # paper resolves below without any superscripts.
                # Read what this paper keys its affiliations with before
                # reading its byline: ∗ is an affiliation marker in one
                # template and "equal contribution" in another.
                markers, alphabet = read_byline_markers(
                    header, [name for _, name, _ in authors], text)
                # Only the markers this byline used, so widening the search to
                # the whole document cannot pull an affiliation out of the
                # reference list.
                wanted = {m for ms in markers.values() for m in ms}
                marker_text = marker_affiliations(header, wanted, alphabet)
                if not marker_text and wanted:
                    # The byline is in the header; what it points at may be a
                    # page-one footnote emitted after the abstract, or a block
                    # at the very end of the file.
                    marker_text = (
                        marker_affiliations(
                            affiliation_window(text), wanted, alphabet)
                        or marker_affiliations(
                            author_information_text(text), wanted, alphabet))
                institutions = conn.execute(
                    "SELECT institution_id, raw_name FROM paper_institutions"
                    " WHERE paper_id=?", (pid,)).fetchall()
                if not marker_text and wanted:
                    # Some blocks print the marker after the institution, and
                    # some key it to an e-mail rather than a name.
                    marker_text = trailing_marker_affiliations(
                        affiliation_window(text), wanted)
                by_marker = {}
                for marker, label in marker_text.items():
                    iid = best_institution_for(label, institutions)
                    if iid is None and "@" in label:
                        iid = institution_for_email(label, institutions)
                    if iid is not None:
                        by_marker[marker] = iid
                if wanted - set(by_marker):
                    # An e-mail keyed to a marker names its institution by
                    # domain: "1liangs@stu.pku.edu.cn" is Peking University.
                    for marker, label in _marker_emails(
                            affiliation_window(text), wanted, alphabet).items():
                        if marker in by_marker:
                            continue
                        iid = institution_for_email(label, institutions)
                        if iid is not None:
                            by_marker[marker] = iid
                rows = [
                    (pid, aid, by_marker[marker], marker, order,
                     "pdf.byline-marker")
                    for aid, name, order in authors
                    for marker in markers.get(name, [])
                    if marker in by_marker]
                if not rows and institutions and not offline:
                    # Every PDF layout failed. Scopus indexed who sat where in
                    # the same response this build already fetches for the
                    # paper's institution list.
                    paired = scopus_author_pairs(
                        conn.execute("SELECT doi FROM papers WHERE paper_id=?",
                                     (pid,)).fetchone()[0] or "",
                        conn.execute("SELECT title FROM papers WHERE paper_id=?",
                                     (pid,)).fetchone()[0] or "",
                        [name for _, name, _ in authors])
                    rows = [
                        (pid, aid, iid, None, order, "scopus")
                        for aid, name, order in authors
                        if name in paired
                        for iid in [best_institution_for(paired[name],
                                                         institutions)]
                        if iid is not None]
                if not rows and institutions:
                    # arXiv/IEEE columns stack the affiliation under the name
                    # with no marker anywhere; PyMuPDF reads them in order.
                    stacked = stacked_author_affiliations(
                        header, [name for _, name, _ in authors])
                    rows = []
                    for aid, name, order in authors:
                        value = stacked.get(name)
                        if not value:
                            continue
                        iid = best_institution_for(value, institutions)
                        if iid is None and "@" in value:
                            # The stacked block can be an e-mail rather than a
                            # name: "Grégoire Mialon / gmialon@meta.com". The
                            # domain says which institution that is.
                            iid = institution_for_email(value, institutions)
                        if iid is not None:
                            rows.append((pid, aid, iid, None, order,
                                         "pdf.stacked-byline"))
                if not rows and institutions:
                    # ACS states the mapping in a back-matter block instead of
                    # a byline: "Yousung Jung -Department of Chemical and
                    # Biological Engineering, ... Seoul National University".
                    named = author_information_pairs(
                        author_information_text(text),
                        [name for _, name, _ in authors])
                    rows = [
                        (pid, aid, iid, None, order, "pdf.author-information")
                        for aid, name, order in authors
                        if name in named
                        for iid in [best_institution_for(named[name], institutions)]
                        if iid is not None]
                if not rows and institutions:
                    # No superscripts, but the byline may name each author's
                    # affiliation on the author's own line (ACM style). That
                    # states the mapping outright, so it outranks the guess.
                    inline = inline_author_affiliations(
                        header, [name for _, name, _ in authors])
                    rows = [
                        (pid, aid, iid, None, order, "pdf.inline-affiliation")
                        for aid, name, order in authors
                        if name in inline
                        for iid in [best_institution_for(inline[name], institutions)]
                        if iid is not None]
                if not rows and institutions:
                    # No superscripts to read. With one affiliation the byline
                    # already says everyone sits there. With several, who sits
                    # where is genuinely unknown, so every author is linked to
                    # every institution under a source of its own — the paper's
                    # institutions are still recorded against its authors, while
                    # `pdf.unmarked-multi` marks the rows unresolved so a
                    # first-author query can exclude them rather than silently
                    # crediting one author with three employers.
                    # One institution: the byline already says everyone sits
                    # there. One author: every affiliation the paper prints is
                    # that author's, however many — an author can hold several
                    # appointments, and nothing here is being guessed. Several
                    # of each is the genuinely unknown case.
                    if len(institutions) == 1:
                        tag = "pdf.sole-affiliation"
                    elif len(authors) == 1:
                        tag = "pdf.sole-author"
                    else:
                        tag = "pdf.unmarked-multi"
                    rows = [(pid, aid, iid, None, order, tag)
                            for aid, _name, order in authors
                            for iid, _raw in institutions]
                if not rows:
                    skipped += 1
                    continue
                if rows[0][5] in ("pdf.byline-marker", "pdf.inline-affiliation",
                                  "pdf.author-information",
                                  "pdf.stacked-byline", "scopus",
                                  "pdf.sole-author"):
                    # A retried paper still carries the guess that stood in
                    # while the parser could not read its byline. Resolved rows
                    # replace it; leaving both would let a query count the same
                    # author at institutions the byline never gave them.
                    conn.execute(
                        "DELETE FROM paper_author_institutions"
                        " WHERE paper_id=? AND source='pdf.unmarked-multi'",
                        (pid,))
                conn.executemany(
                    "INSERT OR IGNORE INTO paper_author_institutions "
                    "(paper_id,author_id,institution_id,marker,author_order,"
                    "source) VALUES (?,?,?,?,?,?)", rows)
                filled += 1
                linked += len(rows)
                if filled % 200 == 0:
                    conn.commit()
                    print(f"[backfill] papers={filled} links={linked}",
                          flush=True)
            conn.commit()
            return {"candidates": len(pending), "papers_filled": filled,
                    "links": linked, "skipped": skipped}
        finally:
            conn.close()
    finally:
        bibliography_lock.release_bibliography_writer_lock(db_path, descriptor)


def finalize(db_path: Path) -> dict:
    """Run only the table-wide passes a streaming ingest deferred.

    `parent_name`, `country_name_en` and orphan removal are derived over the
    whole institutions table, so a per-batch ingest skips them and calls this
    once when the run ends.
    """
    if not db_path.exists():
        return {"stale_papers": 0, "pruned": 0, "countries": 0, "parents": 0}
    descriptor = bibliography_lock.acquire_bibliography_writer_lock(db_path)
    try:
        conn = sqlite3.connect(db_path, timeout=60.0)
        conn.execute("PRAGMA busy_timeout = 60000")
        try:
            result = {"stale_papers": prune_missing_papers(conn),
                      "pruned": prune_orphan_institutions(conn),
                      "countries": consolidate_institution_countries(conn),
                      "parents": consolidate_institution_parents(conn)}
            conn.commit()
        finally:
            conn.close()
        return result
    finally:
        bibliography_lock.release_bibliography_writer_lock(db_path, descriptor)


def build(entries: list[dict], db_path: Path, update_zotero: bool = False,
          skip_zotero: bool = False, offline: bool = False,
          defer_consolidation: bool = False) -> dict:
    """Build while excluding migration recovery and every other DB writer."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    descriptor = bibliography_lock.acquire_bibliography_writer_lock(db_path)
    try:
        return _build_unlocked(
            entries, db_path, update_zotero=update_zotero,
            skip_zotero=skip_zotero, offline=offline,
            defer_consolidation=defer_consolidation)
    finally:
        bibliography_lock.release_bibliography_writer_lock(db_path, descriptor)


def send_completion_email(result: dict) -> None:
    """Send a short completion report through the repository's Resend setup."""
    config = {}
    try:
        config = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
    except Exception:
        pass
    local_keys = {}
    try:
        local_keys = json.loads((ROOT / "docs" / "_local_keys.json").read_text(encoding="utf-8"))
    except Exception:
        pass
    api_key = (os.environ.get("RESEND_API_KEY") or config.get("resend_api_key")
               or local_keys.get("resend_key") or local_keys.get("resend_api_key") or "")
    sender = (os.environ.get("AUDIO_FROM") or config.get("audio_from")
              or local_keys.get("audio_from") or "Paper Curation <onboarding@resend.dev>")
    reply_to = os.environ.get("AUDIO_REPLY_TO") or config.get("audio_reply_to") or local_keys.get("audio_reply_to") or ""
    if not api_key:
        print("[bibliography] completion email skipped: RESEND_API_KEY unavailable", flush=True)
        return
    subject = f"Paper bibliography DB complete: {result.get('processed', 0)} papers"
    lines = [
        f"<h2>Bibliography database completed</h2>",
        f"<p>Processed papers: <b>{result.get('processed', 0)}</b></p>",
        f"<p>Elapsed: <b>{result.get('seconds', 0)} seconds</b></p>",
        f"<p>Zotero items scanned: {result.get('zotero_items_seen', 0)}<br>"
        f"Zotero records updated: {result.get('zotero_updated', 0)}<br>"
        f"Formal publications resolved: {result.get('formal_publications_resolved', 0)}</p>",
        f"<p>Database: <code>{result.get('db', '')}</code></p>",
    ]
    payload = {"from": sender, "to": ["jehyun.lee@gmail.com"], "subject": subject,
               "html": "\n".join(lines)}
    if reply_to:
        payload["reply_to"] = reply_to
    try:
        req = urllib.request.Request(
            "https://api.resend.com/emails",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Authorization": "Bearer " + api_key,
                     "Content-Type": "application/json",
                     "User-Agent": "paper-curation-bibliography/1.0"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=60, context=SSL_CTX) as response:
            print(f"[bibliography] completion email sent: HTTP {response.status}", flush=True)
    except Exception as exc:
        print(f"[bibliography] completion email failed: {exc}", flush=True)


def changed_entries(entries: list[dict], db_path: Path) -> list[dict]:
    """Return papers whose source review/text files are new or changed."""
    if not db_path.exists():
        return entries
    conn = sqlite3.connect(db_path, timeout=60.0)
    conn.execute("PRAGMA busy_timeout = 60000")
    known = {}
    for slug, kind, digest in conn.execute(
        "SELECT p.slug, sd.document_type, sd.sha256 FROM papers p "
        "JOIN source_documents sd ON sd.paper_id=p.paper_id"
    ):
        known[(slug, kind)] = digest
    conn.close()
    changed = []
    for p in entries:
        directory = PAPERS_DIR / p["slug"]
        is_changed = False
        for kind in ("review", "text"):
            path = directory / f"{kind}.md"
            digest = sha256(path) if path.exists() else None
            if known.get((p["slug"], kind)) != digest:
                is_changed = True
                break
        if is_changed:
            changed.append(p)
    return changed

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    group = ap.add_mutually_exclusive_group()
    group.add_argument("--sample", type=int, default=30)
    group.add_argument("--all", action="store_true")
    ap.add_argument("--seed", type=int, default=20260807)
    ap.add_argument("--output", type=Path, default=DEFAULT_DB)
    ap.add_argument("--update-zotero", action="store_true")
    ap.add_argument("--backfill-author-institutions", action="store_true",
                    help="text.md 바이라인 첨자로 저자↔기관 링크만 채운다 "
                         "(Zotero·Scopus·PDF 접근 없음)")
    ap.add_argument("--changed-only", action="store_true",
                    help="process only papers whose review.md/text.md changed")
    ap.add_argument("--no-email", action="store_true")
    ap.add_argument("--skip-zotero", action="store_true",
                    help="skip the full Zotero library scan for a local incremental repair")
    ap.add_argument("--slugs", help="comma-separated slug prefixes to rebuild")
    ap.add_argument("--offline", action="store_true",
                    help="use the deterministic offline affiliation registry")
    args = ap.parse_args()
    if args.backfill_author_institutions:
        print(json.dumps(backfill_author_institutions(args.output),
                         ensure_ascii=False, indent=2))
        return 0
    entries = load_entries()
    if args.slugs:
        prefixes = [value.strip() for value in args.slugs.split(",") if value.strip()]
        entries = [p for p in entries if any(p["slug"].startswith(prefix) for prefix in prefixes)]
    if args.changed_only:
        entries = changed_entries(entries, args.output)
    elif not args.all and not args.slugs:
        # `--slugs` already names the exact set to process. Sampling it again
        # silently dropped the rest: a repair run over 352 named slugs
        # processed 30 of them and reported success.
        entries = random.Random(args.seed).sample(entries, min(args.sample, len(entries)))
    if not entries:
        if args.output.exists():
            try:
                result = build([], args.output, False, True, args.offline)
            except bibliography_lock.BibliographyWriterLockBusyError as exc:
                print(str(exc), file=sys.stderr)
                return 5
            except RuntimeError as exc:
                print(str(exc), file=sys.stderr)
                return 3
            print(json.dumps({**result, "changed": 0}, ensure_ascii=False, indent=2))
            return 0
        print(json.dumps({"processed": 0, "changed": 0, "db": str(args.output)}, ensure_ascii=False, indent=2))
        return 0
    try:
        result = build(entries, args.output, args.update_zotero, args.skip_zotero, args.offline)
    except bibliography_lock.BibliographyWriterLockBusyError as exc:
        print(str(exc), file=sys.stderr)
        return 5
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 3
    conn = sqlite3.connect(args.output)
    result.update({
        "papers": conn.execute("SELECT COUNT(*) FROM papers").fetchone()[0],
        "authors": conn.execute("SELECT COUNT(*) FROM authors").fetchone()[0],
        "institutions": conn.execute("SELECT COUNT(*) FROM institutions").fetchone()[0],
        "institution_groups": conn.execute("SELECT COUNT(*) FROM institution_groups").fetchone()[0],
    })
    conn.close()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if not args.no_email:
        send_completion_email(result)
    return 0

if __name__ == "__main__": raise SystemExit(main())
