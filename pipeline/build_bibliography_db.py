#!/usr/bin/env python3
"""Build a collection-independent bibliographic SQLite database.

The default run processes the reproducible 30-paper sample.  ``--all`` processes
all local papers.  OpenAlex/Crossref are used to resolve formal publications
for arXiv records; Zotero keys are matched from the user's library and, with
``--update-zotero``, safe bibliographic fields are patched there too.
"""
from __future__ import annotations
import os
import shutil
import argparse
import hashlib
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
    from .lib import affiliation_registry
except ImportError:
    from lib import affiliation_registry

ROOT = Path(__file__).resolve().parents[1]
PAPERS_DIR = ROOT / "docs" / "papers"
INDEX_PATH = PAPERS_DIR / "_papers_index.json"
SHARED_ROOT = (Path.home() / "Library" / "CloudStorage" /
               "GoogleDrive-jehyun.lee@gmail.com" / "내 드라이브" / "paper-curation")
SHARED_DB = SHARED_ROOT / "bibliography.sqlite3"
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
 group_id INTEGER PRIMARY KEY, group_name TEXT NOT NULL, normalized_name TEXT NOT NULL,
 organization_id TEXT UNIQUE REFERENCES affiliation_organizations(organization_id));
CREATE INDEX IF NOT EXISTS idx_institution_groups_name ON institution_groups(normalized_name);
CREATE TABLE IF NOT EXISTS institutions (
 institution_id INTEGER PRIMARY KEY, institution_name TEXT NOT NULL,
 normalized_name TEXT NOT NULL, country_name_en TEXT NOT NULL DEFAULT '',
 group_id INTEGER REFERENCES institution_groups(group_id),
 organization_id TEXT UNIQUE REFERENCES affiliation_organizations(organization_id),
 source TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS institution_aliases (
 alias_id INTEGER PRIMARY KEY, raw_name TEXT NOT NULL, normalized_alias TEXT NOT NULL,
 institution_id INTEGER NOT NULL REFERENCES institutions(institution_id),
 UNIQUE(normalized_alias,institution_id));
CREATE TABLE IF NOT EXISTS paper_institutions (
 paper_id INTEGER NOT NULL REFERENCES papers ON DELETE CASCADE,
 institution_id INTEGER NOT NULL REFERENCES institutions ON DELETE CASCADE,
 raw_name TEXT NOT NULL, country_name TEXT, source TEXT NOT NULL, PRIMARY KEY (paper_id, institution_id));
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
AFFILIATION_SCHEMA_VERSION = "affiliation-2"
def fresh_schema_origin_receipt_id(*, schema_version: str, registry_sha256: str,
                                   event_head: str, policy_version: str,
                                   source_sha256: str) -> str:
    """Return the deterministic immutable origin ID for a new affiliation schema."""
    origin = {
        "operation": "fresh-schema",
        "schema_version": schema_version,
        "registry_sha256": registry_sha256,
        "event_head": event_head,
        "policy_version": policy_version,
        "source_sha256": source_sha256,
    }
    return hashlib.sha256(json.dumps(
        origin, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")).hexdigest()
AFFILIATION_OBSERVATION_NAMESPACE = uuid.UUID("8d81aeb5-6231-5e97-8a65-cc9e5658bd22")
REGISTRY_PATH = Path(__file__).with_name("affiliation_registry.json")
AFFILIATION_SCHEMA = """
CREATE TABLE IF NOT EXISTS affiliation_organizations (
 organization_id TEXT PRIMARY KEY, canonical_name_en TEXT NOT NULL, normalized_name TEXT NOT NULL,
 organization_type TEXT NOT NULL CHECK (organization_type IN
  ('university','research_organization','company','hospital','government','facility','laboratory','association','network','other')),
 country_code TEXT NOT NULL DEFAULT '', country_name_en TEXT NOT NULL DEFAULT '',
 country_scope TEXT NOT NULL CHECK (country_scope IN ('domestic','multinational','unknown')),
 status TEXT NOT NULL CHECK (status IN ('active','historical','redirected','proposed')),
 created_event_id TEXT NOT NULL, registry_version INTEGER NOT NULL);
CREATE INDEX IF NOT EXISTS idx_aff_org_normalized ON affiliation_organizations(normalized_name,country_code);
CREATE TABLE IF NOT EXISTS affiliation_organization_redirects (
 old_organization_id TEXT PRIMARY KEY REFERENCES affiliation_organizations(organization_id),
 survivor_organization_id TEXT NOT NULL REFERENCES affiliation_organizations(organization_id),
 event_id TEXT NOT NULL, CHECK(old_organization_id<>survivor_organization_id));
CREATE TABLE IF NOT EXISTS affiliation_identifiers (
 authority TEXT NOT NULL CHECK (authority IN ('ror','wikidata','scopus','grid','isni','source')),
 identifier_value TEXT NOT NULL, organization_id TEXT NOT NULL REFERENCES affiliation_organizations(organization_id),
 status TEXT NOT NULL CHECK (status IN ('active','deprecated')), valid_from TEXT NOT NULL DEFAULT '',
 valid_to TEXT NOT NULL DEFAULT '', evidence_id TEXT NOT NULL,
 PRIMARY KEY(authority,identifier_value,valid_from),
 UNIQUE(organization_id,authority,identifier_value,valid_from));
CREATE TABLE IF NOT EXISTS affiliation_aliases (
 alias_id TEXT PRIMARY KEY, alias_text TEXT NOT NULL, normalized_alias TEXT NOT NULL, language_code TEXT NOT NULL DEFAULT '',
 alias_type TEXT NOT NULL CHECK(alias_type IN ('official','english','native','acronym','legacy','source')),
 created_event_id TEXT NOT NULL);
CREATE INDEX IF NOT EXISTS idx_aff_alias_norm ON affiliation_aliases(normalized_alias);
CREATE TABLE IF NOT EXISTS affiliation_alias_candidates (
 alias_id TEXT NOT NULL REFERENCES affiliation_aliases(alias_id), organization_id TEXT NOT NULL REFERENCES affiliation_organizations(organization_id),
 country_discriminator TEXT NOT NULL DEFAULT '', evidence_id TEXT NOT NULL, confidence REAL NOT NULL CHECK(confidence BETWEEN 0 AND 1),
 review_status TEXT NOT NULL CHECK(review_status IN ('accepted','pending','rejected','superseded')),
 event_id TEXT NOT NULL, PRIMARY KEY(alias_id,organization_id,country_discriminator,event_id));
CREATE INDEX IF NOT EXISTS idx_aff_alias_candidate_lookup
 ON affiliation_alias_candidates(alias_id,country_discriminator,review_status);
CREATE TABLE IF NOT EXISTS affiliation_relationships (
 relationship_id TEXT PRIMARY KEY, subject_organization_id TEXT NOT NULL REFERENCES affiliation_organizations(organization_id),
 object_organization_id TEXT NOT NULL REFERENCES affiliation_organizations(organization_id),
 relationship_type TEXT NOT NULL CHECK(relationship_type IN
  ('part_of','jointly_operated_by','member_of','network_member_of')),
 valid_from TEXT NOT NULL DEFAULT '', valid_to TEXT NOT NULL DEFAULT '',
 status TEXT NOT NULL CHECK(status IN ('accepted','historical','superseded')),
 confidence REAL NOT NULL CHECK(confidence BETWEEN 0 AND 1), created_event_id TEXT NOT NULL,
 managed_by TEXT NOT NULL CHECK(managed_by IN ('registry','manual')),
 CHECK(subject_organization_id<>object_organization_id),
 CHECK(valid_to='' OR valid_from='' OR valid_from<valid_to),
 UNIQUE(subject_organization_id,object_organization_id,relationship_type,valid_from,valid_to));
CREATE TABLE IF NOT EXISTS affiliation_relationship_evidence (
 relationship_id TEXT NOT NULL REFERENCES affiliation_relationships(relationship_id),
 evidence_id TEXT NOT NULL, PRIMARY KEY(relationship_id,evidence_id));
CREATE TABLE IF NOT EXISTS observed_affiliation_slots (
 observation_slot_id TEXT PRIMARY KEY, paper_id INTEGER NOT NULL REFERENCES papers(paper_id) ON DELETE CASCADE,
 source_kind TEXT NOT NULL CHECK(source_kind IN ('scopus','pdf','review','legacy')),
 source_record_key TEXT NOT NULL, source_ordinal INTEGER NOT NULL CHECK(source_ordinal>=0), created_at TEXT NOT NULL,
 UNIQUE(paper_id,source_kind,source_record_key,source_ordinal));
CREATE TABLE IF NOT EXISTS observed_affiliations (
 observation_id TEXT PRIMARY KEY, observation_slot_id TEXT NOT NULL REFERENCES observed_affiliation_slots(observation_slot_id) ON DELETE CASCADE,
 observation_version INTEGER NOT NULL CHECK(observation_version>=1), raw_content_sha256 TEXT NOT NULL,
 raw_name TEXT NOT NULL, normalized_raw_name TEXT NOT NULL, observed_country_code TEXT NOT NULL DEFAULT '',
 observed_country_name TEXT NOT NULL DEFAULT '', external_identifiers_json TEXT NOT NULL DEFAULT '{}',
 raw_context_sha256 TEXT NOT NULL, resolved_organization_id TEXT REFERENCES affiliation_organizations(organization_id),
 resolution_status TEXT NOT NULL CHECK(resolution_status IN ('resolved','ambiguous','unseen','rejected','superseded')),
 current_decision_id TEXT, registry_sha256 TEXT NOT NULL, policy_version TEXT NOT NULL,
 first_seen_at TEXT NOT NULL, last_seen_at TEXT NOT NULL, is_current INTEGER NOT NULL CHECK(is_current IN (0,1)),
 supersedes_observation_id TEXT REFERENCES observed_affiliations(observation_id),
 superseded_by_observation_id TEXT REFERENCES observed_affiliations(observation_id),
 UNIQUE(observation_slot_id,observation_version),
 UNIQUE(observation_slot_id,observation_version,raw_content_sha256));
CREATE UNIQUE INDEX IF NOT EXISTS idx_observed_aff_one_current ON observed_affiliations(observation_slot_id) WHERE is_current=1;
CREATE INDEX IF NOT EXISTS idx_observed_aff_pending
 ON observed_affiliations(is_current,resolution_status,normalized_raw_name,observed_country_code);
CREATE TABLE IF NOT EXISTS affiliation_resolution_decisions (
 decision_id TEXT PRIMARY KEY, observation_id TEXT NOT NULL REFERENCES observed_affiliations(observation_id) ON DELETE CASCADE,
 decision_sequence INTEGER NOT NULL, outcome TEXT NOT NULL CHECK(outcome IN ('resolved','ambiguous','unseen','rejected','superseded')),
 selected_organization_id TEXT REFERENCES affiliation_organizations(organization_id), reason_code TEXT NOT NULL,
 confidence REAL NOT NULL CHECK(confidence BETWEEN 0 AND 1), registry_sha256 TEXT NOT NULL, policy_version TEXT NOT NULL,
 effective_date TEXT NOT NULL, decided_at TEXT NOT NULL,
 previous_decision_id TEXT REFERENCES affiliation_resolution_decisions(decision_id),
 UNIQUE(observation_id,decision_sequence));
CREATE TABLE IF NOT EXISTS affiliation_decision_candidates (
 decision_id TEXT NOT NULL REFERENCES affiliation_resolution_decisions(decision_id) ON DELETE CASCADE,
 organization_id TEXT NOT NULL REFERENCES affiliation_organizations(organization_id), candidate_rank INTEGER NOT NULL,
 reason_code TEXT NOT NULL, PRIMARY KEY(decision_id,organization_id), UNIQUE(decision_id,candidate_rank));
CREATE TABLE IF NOT EXISTS affiliation_pending_cases (
 pending_id TEXT PRIMARY KEY, normalized_raw_name TEXT NOT NULL, observed_country_code TEXT NOT NULL DEFAULT '',
 external_identifiers_json TEXT NOT NULL DEFAULT '{}',
 status TEXT NOT NULL CHECK(status IN ('open','proposed','resolved','rejected')), reason_code TEXT NOT NULL,
 first_seen_at TEXT NOT NULL, last_seen_at TEXT NOT NULL,
 active_observation_count INTEGER NOT NULL DEFAULT 0 CHECK(active_observation_count>=0),
 lifetime_observation_count INTEGER NOT NULL CHECK(lifetime_observation_count>0 AND lifetime_observation_count>=active_observation_count),
 attempt_count INTEGER NOT NULL DEFAULT 0, last_attempt_at TEXT NOT NULL DEFAULT '',
 proposal_digest TEXT NOT NULL DEFAULT '', resolved_event_id TEXT NOT NULL DEFAULT '',
 CHECK((status IN ('open','proposed') AND active_observation_count>0 AND resolved_event_id='')
   OR (status IN ('resolved','rejected') AND active_observation_count=0 AND resolved_event_id<>'')),
 UNIQUE(normalized_raw_name,observed_country_code,external_identifiers_json));
CREATE TABLE IF NOT EXISTS affiliation_pending_observations (
 pending_id TEXT NOT NULL REFERENCES affiliation_pending_cases(pending_id) ON DELETE CASCADE,
 observation_id TEXT NOT NULL UNIQUE REFERENCES observed_affiliations(observation_id) ON DELETE CASCADE,
 linked_at TEXT NOT NULL, PRIMARY KEY(pending_id,observation_id));
CREATE TABLE IF NOT EXISTS affiliation_enrichment_attempts (
 attempt_id TEXT PRIMARY KEY, pending_id TEXT NOT NULL REFERENCES affiliation_pending_cases(pending_id) ON DELETE CASCADE,
 provider TEXT NOT NULL CHECK(provider IN ('official','ror','wikidata','wikipedia','scopus')),
 started_at TEXT NOT NULL, finished_at TEXT NOT NULL,
 outcome TEXT NOT NULL CHECK(outcome IN
  ('success','no_match','unavailable','subscription_required','timeout','rate_limited','error','budget_exhausted')),
 response_digest TEXT NOT NULL DEFAULT '', error_class TEXT NOT NULL DEFAULT '', proposal_digest TEXT NOT NULL DEFAULT '');
CREATE INDEX IF NOT EXISTS idx_affiliation_attempt_pending ON affiliation_enrichment_attempts(pending_id);
CREATE TABLE IF NOT EXISTS affiliation_registry_metadata (
 singleton INTEGER PRIMARY KEY CHECK(singleton=1), schema_version TEXT NOT NULL, registry_version INTEGER NOT NULL,
 registry_sha256 TEXT NOT NULL, event_head TEXT NOT NULL, policy_version TEXT NOT NULL, source_sha256 TEXT NOT NULL,
 projected_at TEXT NOT NULL, base_generation INTEGER NOT NULL DEFAULT 0, migration_receipt_id TEXT NOT NULL DEFAULT '');
CREATE TABLE IF NOT EXISTS affiliation_migration_audit (
 receipt_id TEXT PRIMARY KEY, operation TEXT NOT NULL, base_generation INTEGER NOT NULL, base_logical_sha256 TEXT NOT NULL,
 result_logical_sha256 TEXT NOT NULL, registry_sha256 TEXT NOT NULL, schema_from TEXT NOT NULL, schema_to TEXT NOT NULL,
 backup_path TEXT NOT NULL, backup_sha256 TEXT NOT NULL, started_at TEXT NOT NULL, finished_at TEXT NOT NULL, report_json TEXT NOT NULL);
"""


def ensure_schema_migrations(conn: sqlite3.Connection) -> None:
    """Add bibliographic columns to databases created by earlier releases."""
    existing = {
        row[1] for row in conn.execute("PRAGMA table_info(papers)").fetchall()
    }
    for name, sql_type in PAPER_SCHEMA_COLUMNS.items():
        if name not in existing:
            conn.execute(f"ALTER TABLE papers ADD COLUMN {name} {sql_type}")



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
            and {"organization_id"} <= group_columns
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
          normalized_name TEXT NOT NULL,
          organization_id TEXT UNIQUE REFERENCES affiliation_organizations(organization_id));
        CREATE INDEX idx_institution_groups_name
          ON institution_groups(normalized_name);
        CREATE TABLE institutions (
          institution_id INTEGER PRIMARY KEY, institution_name TEXT NOT NULL,
          normalized_name TEXT NOT NULL, country_name_en TEXT NOT NULL DEFAULT '',
          group_id INTEGER REFERENCES institution_groups(group_id),
          organization_id TEXT UNIQUE REFERENCES affiliation_organizations(organization_id),
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
            "INSERT INTO institution_groups VALUES (?,?,?,?)",
            (row.get("group_id"), row.get("group_name", ""),
             row.get("normalized_name", ""), row.get("organization_id")))
    for row in institutions:
        conn.execute(
            "INSERT INTO institutions VALUES (?,?,?,?,?,?,?)",
            (row.get("institution_id"),
             row.get("institution_name") or row.get("normalized_name", ""),
             row.get("normalized_name", ""),
             row.get("country_name_en", ""), row.get("group_id"),
             row.get("organization_id"), row.get("source", "legacy")))
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


def clean_doi(s: str) -> str:
    s = (s or "").strip()
    s = re.sub(r"^https?://doi\.org/", "", s, flags=re.I)
    s = s.rstrip(" .;,)")
    if s.lower().startswith("10.48550/arxiv.") or s.lower().startswith("arxiv:"):
        return ""
    return s


def clean_arxiv(s: str) -> str:
    s = (s or "").strip()
    s = re.sub(r"^arXiv:", "", s, flags=re.I)
    s = re.sub(r"^https?://arxiv\.org/(?:abs|pdf)/", "", s, flags=re.I)
    return s.rstrip(" .;,)")


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


def extract_header(text_path: Path) -> tuple[str, list[str], float]:
    try:
        text = text_path.read_text(encoding="utf-8", errors="replace")[:12000]
    except OSError:
        return "", [], 0.0
    normalized = []
    for line in text.splitlines():
        line = re.sub(r"^\s*[-–—]?\s*\d+\s+", "", line)
        line = re.sub(r"\s+", " ", line).strip()
        if line:
            normalized.append(line)
    text = "\n".join(normalized)
    stop = re.search(r"(?im)^\s*(?:#+\s*)?(?:abstract|초록)\b", text)
    if stop:
        text = text[:stop.start()]
    lines = [x.strip() for x in text.splitlines() if x.strip()][:40]
    raw = "\n".join(lines)
    cues = re.compile(r"university|institute|laborator|school|college|department|center|centre|hospital|academy|ETH|MIT|Caltech|CNRS|대학교|연구원|연구소|병원|학부|학과|@", re.I)
    candidates = []
    for line in lines:
        if 5 <= len(line) <= 240 and cues.search(line) and not re.match(r"^(abstract|keywords?|초록|introduction)\b", line, re.I):
            if re.search(r"correspondence|corresponding author|contact", line, re.I):
                continue
            line = re.sub(r"^[-*\d\s]+", "", line).strip()
            if line and line not in candidates:
                candidates.append(line)
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
    ("United States", r"\b(?:USA|U\.S\.A\.|United States|US)\b"),
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

def country_from_raw(raw: str) -> str:
    for name, pattern in COUNTRIES:
        if re.search(pattern, raw, re.I):
            return name
    return ""


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
    value = re.sub(r"(?<![A-Za-z])\d+(?=[A-Z])", " ", value)
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


def is_suspicious_institution_name(name: str) -> bool:
    value = _apply_institution_aliases(_clean_affiliation_text(name))
    if value in STANDALONE_INSTITUTION_NAMES:
        return False
    if (not value or value in GENERIC_INSTITUTION_NAMES or len(value) > 90
            or is_local_language_institution(value)):
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


def fetch_scopus_record(doi: str, title: str = "") -> dict:
    """Fetch one Scopus record and reuse it for bibliography and affiliations."""
    doi = clean_doi(doi).lower()
    title = re.sub(r"\s+", " ", title or "").strip()
    if not doi and not title:
        return {"bibliography": {}, "affiliations": []}
    cache_key = doi or "title:" + norm(title)
    cache = _load_scopus_record_cache()
    cached = cache.get(cache_key)
    if isinstance(cached, dict) and "bibliography" in cached:
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
                        name = canonical_institution(str(aff.get("affilname") or ""))
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


def _pdf_text_for_affiliations(pdf_path: Path | None, text_path: Path) -> str:
    """Search first/last PDF pages plus abstract-adjacent and author-info zones."""
    chunks = []
    if pdf_path and pdf_path.exists():
        try:
            import fitz
            doc = fitz.open(pdf_path)
            pages = sorted(set(range(min(3, len(doc)))) |
                           set(range(max(0, len(doc) - 3), len(doc))))
            chunks = [doc[i].get_text("text") for i in pages]
            doc.close()
        except Exception:
            chunks = []
    try:
        text = text_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        text = ""
    lines = text.splitlines()
    chunks.extend(["\n".join(lines[:260]), "\n".join(lines[-600:])])
    for match in re.finditer(
            r"(?im)^(?:author information|affiliations?|published online|received:).*$", text):
        chunks.append(text[max(0, match.start() - 1000):match.start() + 5000])
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

    issue = re.search(r"\b(?:Issue|No\.)\s+([A-Za-z0-9.-]+)", pdf_text, re.I)
    if issue:
        result["issue"] = issue.group(1)
    return result


def reconcile_bibliography(local: dict, scopus: dict, pdf: dict) -> dict:
    """Use Scopus as the baseline, then verify and repair it from the PDF."""
    fields = (
        "title", "journal", "date", "doi", "url", "volume", "issue", "pages",
        "publisher", "issn", "eissn", "document_type", "scopus_eid",
        "received_date", "accepted_date", "published_online_date",
    )
    result = {field: str(local.get(field) or "").strip() for field in fields}
    used = ["local-metadata"]
    if scopus:
        for field in fields:
            if scopus.get(field):
                result[field] = str(scopus[field]).strip()
        used = ["scopus"]

    pdf_used = False
    for field in ("journal", "doi", "volume", "issue", "pages",
                  "received_date", "accepted_date", "published_online_date"):
        if pdf.get(field):
            result[field] = str(pdf[field]).strip()
            pdf_used = True
    if result["published_online_date"]:
        result["date"] = result["published_online_date"]
    if result["doi"]:
        result["url"] = external_url(result["doi"], "")
    if pdf_used:
        used.append("pdf")
    result["source"] = "+".join(used)
    return result


def reconcile_affiliations(
        scopus_records: list[dict], pdf_text: str,
        fallback_lines: list[str], *, offline: bool = False) -> list[dict]:
    """Validate Scopus against PDF text and add institutions missing in Scopus."""
    flat = re.sub(r"\s+", " ", pdf_text)
    normalized_pdf = norm(flat)
    out = {}
    for rec in scopus_records:
        original_name = str(rec.get("name") or "")
        english = resolve_english_institution(
            original_name, str(rec.get("country") or ""),
            allow_remote=not offline)
        parent = scopus_parent_institution(
            str(rec.get("scopus_id") or ""))
        name = canonical_institution(parent or english or original_name)
        if is_suspicious_institution_name(name):
            name = resolve_institution_from_raw(
                str(rec.get("raw_name") or original_name), name)
        if not name or is_suspicious_institution_name(name):
            continue
        tokens = [x for x in re.findall(r"[a-z0-9]+", norm(name))
                  if x not in {"of", "the", "and", "for"}]
        confirmed = bool(tokens) and sum(t in normalized_pdf for t in tokens) >= max(1, len(tokens) - 1)
        out[norm(name)] = {
            **rec, "name": name,
            "source": "scopus+pdf" if confirmed else "scopus-unconfirmed",
        }

    segments = list(fallback_lines)
    segments.extend(re.split(r"(?=\s(?:[1-9]|1\d)(?=[A-Z]))", flat))
    for raw in segments:
        if len(raw) > 600:
            continue
        parsed = institution_from_raw(raw, allow_remote=not offline)
        if not parsed:
            continue
        name, _group = parsed
        name = canonical_institution(name)
        key = norm(name)
        country = country_from_raw(raw)
        if key in out:
            out[key]["source"] = "scopus+pdf"
            out[key]["country"] = out[key].get("country") or country
        else:
            out[key] = {
                "name": name, "raw_name": raw.strip(), "country": country,
                "scopus_id": "", "source": "pdf",
            }
    return list(out.values())


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
        try:
            batch = request_json(url, {"Zotero-API-Key": key, "User-Agent": "paper-curation-bibliography/1.0"}, 40)
        except Exception as e:
            print(f"Zotero read warning: {e}", file=sys.stderr)
            break
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


def patch_zotero(item: dict, bibliography: dict) -> bool:
    """Patch Zotero with the Scopus record after PDF reconciliation."""
    if not bibliography.get("doi"):
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
        patch = {
            zotero_field: bibliography[source_field]
            for source_field, zotero_field in field_map.items()
            if bibliography.get(source_field)
        }
        issns = "; ".join(
            value for value in (bibliography.get("issn"), bibliography.get("eissn"))
            if value)
        if issns:
            patch["ISSN"] = issns
        patch["itemType"] = "journalArticle"
        current = item.get("data") or {}
        patch = {key_: value for key_, value in patch.items()
                 if str(current.get(key_) or "") != str(value)}
        if not patch:
            return False
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


def _registry_digest() -> str:
    return hashlib.sha256(REGISTRY_PATH.read_bytes()).hexdigest()


def _project_compatibility_groups(conn: sqlite3.Connection, registry: dict) -> None:
    """Project one current, lowest-precedence official edge into legacy group_id."""
    tables = {
        row[0] for row in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table'")
    }
    if not {"institutions", "institution_groups"} <= tables:
        return
    columns = {
        row[1] for row in conn.execute("PRAGMA table_info(institutions)")
    }
    if not {"organization_id", "group_id"} <= columns:
        return
    # Compatibility groups are a disposable projection, never an authority.
    # Clearing every link prevents unbound legacy heuristic groups from leaking.
    conn.execute("UPDATE institutions SET group_id=NULL")
    conn.execute("DELETE FROM institution_groups")
    organizations = {
        row["organization_id"]: row for row in registry["organizations"]
    }
    effective_date = max(
        (str(event.get("timestamp") or "")[:10]
         for event in registry.get("events", [])),
        default=time.strftime("%Y-%m-%d", time.gmtime()),
    )
    precedence = {"part_of": 1, "jointly_operated_by": 2, "member_of": 3}
    eligible: dict[str, list[tuple[int, str]]] = {}
    for edge in registry.get("relationships", []):
        relationship_type = edge.get("relationship_type")
        if edge.get("status") != "accepted" or relationship_type not in precedence:
            continue
        subject = organizations.get(edge["subject_organization_id"])
        object_organization = organizations.get(edge["object_organization_id"])
        if (not subject or not object_organization or
                subject.get("status") == "proposed" or
                object_organization.get("status") == "proposed"):
            continue
        interval = edge.get("validity_interval") or {}
        valid_from = edge.get("valid_from", interval.get("start", ""))
        valid_to = edge.get("valid_to", interval.get("end", ""))
        if (valid_from and effective_date < valid_from) or (
                valid_to and effective_date >= valid_to):
            continue
        eligible.setdefault(edge["subject_organization_id"], []).append(
            (precedence[relationship_type], edge["object_organization_id"]))
    for subject_id, candidates in sorted(eligible.items()):
        best = min(rank for rank, _object_id in candidates)
        targets = sorted({
            object_id for rank, object_id in candidates if rank == best
        })
        if len(targets) != 1:
            continue
        target = organizations.get(targets[0])
        if not target:
            continue
        group_name = target["canonical_name_en"]
        normalized_group = affiliation_registry.normalize_name(group_name)
        conn.execute(
            "INSERT INTO institution_groups "
            "(group_name,normalized_name,organization_id) VALUES (?,?,?)",
            (group_name, normalized_group, targets[0]))
        group_id = conn.execute(
            "SELECT group_id FROM institution_groups WHERE organization_id=?",
            (targets[0],)).fetchone()[0]
        conn.execute(
            "UPDATE institutions SET group_id=? WHERE organization_id=?",
            (group_id, subject_id))


def _registry_candidates(conn: sqlite3.Connection, normalized: str, country: str,
                         country_code: str, external_identifiers: dict) -> tuple[list[str], str]:
    """Resolve reviewed identifiers before accepted alias candidates."""
    authority_for = {
        "ror": ("ror",), "ror_id": ("ror",),
        "wikidata": ("wikidata",), "wikidata_id": ("wikidata",),
        # Imported source affiliation IDs predate authority-specific review and
        # are projected as `source`; retain them as exact, non-alias evidence.
        "scopus": ("scopus", "source"), "scopus_id": ("scopus", "source"),
        "grid": ("grid",), "grid_id": ("grid",),
        "isni": ("isni",), "isni_id": ("isni",),
    }
    identifiers = sorted(
        (authority, str(value))
        for key, value in external_identifiers.items()
        for authority in authority_for.get(
            key, ("source",) if key.startswith("source_") else ())
        if str(value).strip()
    )
    country_terms = {affiliation_registry.normalize_name(value) for value in
                     (country, country_code) if value}
    if identifiers:
        clauses, params = [], []
        for authority, value in identifiers:
            clauses.append("(i.authority=? AND i.identifier_value=?)")
            params.extend((authority, value))
        rows = conn.execute(
            "SELECT DISTINCT i.organization_id,o.country_name_en "
            "FROM affiliation_identifiers i JOIN affiliation_organizations o "
            "ON o.organization_id=i.organization_id "
            "WHERE i.status='active' AND o.status IN ('active','historical') "
            f"AND ({' OR '.join(clauses)}) ORDER BY i.organization_id",
            params).fetchall()
        matches = sorted({
            organization_id for organization_id, organization_country in rows
            if not country_terms or not organization_country or
            affiliation_registry.normalize_name(organization_country) in country_terms
        })
        if matches:
            return matches, "offline_registry_exact_identifier"
    if country:
        rows = conn.execute(
            "SELECT DISTINCT c.organization_id FROM affiliation_aliases a "
            "JOIN affiliation_alias_candidates c USING(alias_id) "
            "JOIN affiliation_organizations o ON o.organization_id=c.organization_id "
            "WHERE a.normalized_alias=? AND c.review_status='accepted' "
            "AND o.status IN ('active','historical') "
            "AND (c.country_discriminator='' OR c.country_discriminator=?) "
            "ORDER BY c.organization_id", (normalized, country)).fetchall()
    else:
        rows = conn.execute(
            "SELECT DISTINCT c.organization_id FROM affiliation_aliases a "
            "JOIN affiliation_alias_candidates c USING(alias_id) "
            "JOIN affiliation_organizations o ON o.organization_id=c.organization_id "
            "WHERE a.normalized_alias=? AND c.review_status='accepted' "
            "AND o.status IN ('active','historical') "
            "ORDER BY c.organization_id", (normalized,)).fetchall()
    return [row[0] for row in rows], "offline_registry_exact_alias"
def reresolve_current_affiliations(conn: sqlite3.Connection, registry: dict,
                                   registry_digest: str) -> None:
    """Re-evaluate every current observation after a registry projection changes."""
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    pending_ids: set[str] = set()
    terminal: dict[str, tuple[str, str]] = {}
    rows = conn.execute(
        "SELECT observation_id,normalized_raw_name,observed_country_code,"
        "observed_country_name,external_identifiers_json,resolved_organization_id,"
        "resolution_status,current_decision_id "
        "FROM observed_affiliations WHERE is_current=1 "
        "AND resolution_status!='superseded' ORDER BY observation_id"
    ).fetchall()
    for (observation_id, normalized, country_code, country, external_json,
         old_selected, old_status, previous) in rows:
        identifiers = json.loads(external_json or "{}")
        candidates, resolution_reason = _registry_candidates(
            conn, normalized, country, country_code, identifiers)
        status = "resolved" if len(candidates) == 1 else (
            "ambiguous" if candidates else "unseen")
        selected = candidates[0] if status == "resolved" else None
        prior = conn.execute(
            "SELECT registry_sha256,policy_version FROM "
            "affiliation_resolution_decisions WHERE decision_id=?",
            (previous,)).fetchone()
        prior_candidates = [
            row[0] for row in conn.execute(
                "SELECT organization_id FROM affiliation_decision_candidates "
                "WHERE decision_id=? ORDER BY candidate_rank", (previous,))]
        needs_decision = (
            (status, selected) != (old_status, old_selected) or
            candidates != prior_candidates or
            prior != (registry_digest, registry["policy_version"]))
        if not needs_decision:
            continue
        sequence = conn.execute(
            "SELECT COALESCE(MAX(decision_sequence),0)+1 FROM "
            "affiliation_resolution_decisions WHERE observation_id=?",
            (observation_id,)).fetchone()[0]
        decision_id = hashlib.sha256(
            f"registry-reresolve:{observation_id}:{sequence}:{registry_digest}".encode()
        ).hexdigest()
        conn.execute(
            "INSERT INTO affiliation_resolution_decisions VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
            (decision_id, observation_id, sequence, status, selected,
             resolution_reason, 1.0 if selected else 0.0,
             registry_digest, registry["policy_version"], now, now, previous or ""))
        for rank, candidate in enumerate(candidates, 1):
            conn.execute(
                "INSERT INTO affiliation_decision_candidates VALUES (?,?,?,?)",
                (decision_id, candidate, rank, resolution_reason))
        conn.execute(
            "UPDATE observed_affiliations SET resolved_organization_id=?,"
            "resolution_status=?,current_decision_id=?,registry_sha256=?,policy_version=? "
            "WHERE observation_id=?",
            (selected, status, decision_id, registry_digest,
             registry["policy_version"], observation_id))
        linked = {row[0] for row in conn.execute(
            "SELECT pending_id FROM affiliation_pending_observations "
            "WHERE observation_id=?", (observation_id,))}
        pending_ids.update(linked)
        if status == "resolved":
            for pending_id in linked:
                terminal[pending_id] = ("resolved", decision_id)
        else:
            identifiers = json.loads(external_json or "{}")
            pending_id = hashlib.sha256(
                affiliation_registry.canonical_json_bytes(
                    [normalized, country_code, identifiers])
            ).hexdigest()
            conn.execute(
                "INSERT OR IGNORE INTO affiliation_pending_cases "
                "(pending_id,normalized_raw_name,observed_country_code,"
                "external_identifiers_json,status,reason_code,first_seen_at,last_seen_at,"
                "active_observation_count,lifetime_observation_count) VALUES (?,?,?,?,?,?,?,?,?,?)",
                (pending_id, normalized, country_code, external_json, "open",
                 "registry_projection_no_unique_alias", now, now, 1, 1))
            actual_pending = conn.execute(
                "SELECT pending_id FROM affiliation_pending_cases WHERE "
                "normalized_raw_name=? AND observed_country_code=? AND "
                "external_identifiers_json=?",
                (normalized, country_code, external_json)).fetchone()[0]
            conn.execute(
                "INSERT OR IGNORE INTO affiliation_pending_observations VALUES (?,?,?)",
                (actual_pending, observation_id, now))
            pending_ids.add(actual_pending)
            terminal.pop(actual_pending, None)

    if pending_ids:
        recount_affiliation_pending_cases(conn, pending_ids, terminal, now)


def project_affiliation_registry(conn: sqlite3.Connection) -> dict:
    """Make the managed registry projection an exact, offline snapshot."""
    registry = affiliation_registry.load_registry(REGISTRY_PATH)
    affiliation_registry.validate_registry(registry)
    digest = _registry_digest()
    conn.executescript(AFFILIATION_SCHEMA)
    existing_metadata = conn.execute(
        "SELECT base_generation FROM affiliation_registry_metadata "
        "WHERE singleton=1").fetchone()
    audit_row = conn.execute(
        "SELECT receipt_id,base_generation FROM affiliation_migration_audit "
        "WHERE operation='migrate' ORDER BY finished_at DESC LIMIT 1"
    ).fetchone()
    if audit_row:
        migration_receipt_id, base_generation = audit_row
    else:
        base_generation = existing_metadata[0] if existing_metadata else 0
        migration_receipt_id = fresh_schema_origin_receipt_id(
            schema_version=AFFILIATION_SCHEMA_VERSION,
            registry_sha256=digest,
            event_head=registry["event_head"],
            policy_version=registry["policy_version"],
            source_sha256=registry["source_sha256"],
        )
    organization_ids = {org["organization_id"] for org in registry["organizations"]}
    if organization_ids:
        conn.execute("UPDATE observed_affiliations SET resolved_organization_id=NULL "
                     "WHERE resolved_organization_id NOT IN (" + ",".join("?" for _ in organization_ids) + ")",
                     tuple(organization_ids))
    else:
        conn.execute("UPDATE observed_affiliations SET resolved_organization_id=NULL")
    if conn.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='institutions'").fetchone():
        if organization_ids:
            conn.execute("UPDATE institutions SET organization_id=NULL WHERE organization_id NOT IN ("
                         + ",".join("?" for _ in organization_ids) + ")", tuple(organization_ids))
        else:
            conn.execute("UPDATE institutions SET organization_id=NULL WHERE organization_id IS NOT NULL")
    conn.execute("DELETE FROM affiliation_relationship_evidence")
    conn.execute("DELETE FROM affiliation_relationships")
    conn.execute("DELETE FROM affiliation_alias_candidates")
    conn.execute("DELETE FROM affiliation_aliases")
    conn.execute("DELETE FROM affiliation_identifiers")
    conn.execute("DELETE FROM affiliation_organization_redirects")
    if organization_ids:
        conn.execute("DELETE FROM affiliation_organizations WHERE organization_id NOT IN ("
                     + ",".join("?" for _ in organization_ids) + ")", tuple(organization_ids))
    else:
        conn.execute("DELETE FROM affiliation_organizations")
    for org in registry["organizations"]:
        conn.execute("INSERT OR IGNORE INTO affiliation_organizations VALUES (?,?,?,?,?,?,?,?,?,?)",
                     (org["organization_id"], org["canonical_name_en"], org["normalized_name"],
                      org["organization_type"], "", org.get("country", ""), "unknown",
                      org["status"], "", registry["registry_version"]))
        conn.execute("UPDATE affiliation_organizations SET canonical_name_en=?,normalized_name=?,"
                     "organization_type=?,country_code='',country_name_en=?,country_scope='unknown',"
                     "status=?,created_event_id='',registry_version=? WHERE organization_id=?",
                     (org["canonical_name_en"], org["normalized_name"], org["organization_type"],
                      org.get("country", ""), org["status"], registry["registry_version"],
                      org["organization_id"]))
        for ident in org.get("identifiers", []):
            authority = ident["authority"]
            if authority.startswith("source_"):
                authority = "source"
            conn.execute("INSERT INTO affiliation_identifiers "
                         "(authority,identifier_value,organization_id,status,"
                         "valid_from,valid_to,evidence_id) VALUES (?,?,?,?,?,?,?)",
                         (authority, ident["value"], org["organization_id"],
                          "active", "", "", ""))
        for alias in org.get("aliases", []):
            conn.execute("INSERT INTO affiliation_aliases VALUES (?,?,?,?,?,?)",
                         (alias["alias_id"], alias["name"], alias["normalized_alias"], "", "source", ""))
    for candidate in registry["alias_candidates"]:
        conn.execute("INSERT INTO affiliation_alias_candidates VALUES (?,?,?,?,?,?,?)",
                     (candidate["alias_id"], candidate["organization_id"],
                      candidate.get("country_discriminator", ""), "", 1.0, "accepted", ""))
    for edge in registry["relationships"]:
        if edge.get("status") in {"accepted", "historical"}:
            interval = edge.get("validity_interval") or {}
            conn.execute("INSERT INTO affiliation_relationships VALUES (?,?,?,?,?,?,?,?,?,?)",
                         (edge["relationship_id"], edge["subject_organization_id"], edge["object_organization_id"],
                          edge["relationship_type"],
                          edge.get("valid_from", interval.get("start", "")),
                          edge.get("valid_to", interval.get("end", "")),
                          edge["status"], edge.get("confidence", 1.0),
                          edge.get("created_event_id", ""), "registry"))
            for evidence_id in edge.get("evidence_ids", []):
                conn.execute("INSERT INTO affiliation_relationship_evidence VALUES (?,?)",
                             (edge["relationship_id"], evidence_id))
    repair_terminal_superseded_current_slots(conn)
    reresolve_current_affiliations(conn, registry, digest)
    _project_compatibility_groups(conn, registry)
    conn.execute("INSERT OR REPLACE INTO affiliation_registry_metadata VALUES (1,?,?,?,?,?,?,?,?,?)",
                 (AFFILIATION_SCHEMA_VERSION, registry["registry_version"], digest,
                  registry["event_head"], registry["policy_version"],
                  registry["source_sha256"],
                  time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                  base_generation, migration_receipt_id))
    return registry


def recount_affiliation_pending_cases(conn: sqlite3.Connection, pending_ids: set[str],
                                     terminal_decisions: dict[str, tuple[str, str]],
                                     now: str) -> None:
    """Finalize all affected pending cases after one observation-version write."""
    for pending_id in sorted(pending_ids):
        counts = conn.execute(
            "SELECT COUNT(*), COALESCE(SUM(o.is_current=1 AND o.resolution_status "
            "IN ('ambiguous','unseen')),0) FROM affiliation_pending_observations l "
            "JOIN observed_affiliations o USING(observation_id) WHERE l.pending_id=?",
            (pending_id,)).fetchone()
        lifetime, active = counts
        if not lifetime:
            conn.execute("DELETE FROM affiliation_pending_cases WHERE pending_id=?",
                         (pending_id,))
        elif active:
            proposal_digest = conn.execute(
                "SELECT proposal_digest FROM affiliation_pending_cases WHERE pending_id=?",
                (pending_id,)).fetchone()[0]
            conn.execute(
                "UPDATE affiliation_pending_cases SET lifetime_observation_count=?,"
                "active_observation_count=?,status=?,resolved_event_id='',"
                "last_seen_at=? WHERE pending_id=?",
                (lifetime, active, "proposed" if proposal_digest else "open", now, pending_id))
        else:
            status, decision_id = terminal_decisions.get(
                pending_id, ("rejected", ""))
            conn.execute(
                "UPDATE affiliation_pending_cases SET lifetime_observation_count=?,"
                "active_observation_count=0,status=?,resolved_event_id=?,"
                "last_seen_at=? WHERE pending_id=?",
                (lifetime, status, decision_id, now, pending_id))


def _uuid5_affiliation_observation(parts: list[object]) -> str:
    """Return the approved stable UUIDv5 identity for canonical observation data."""
    return str(uuid.uuid5(
        AFFILIATION_OBSERVATION_NAMESPACE,
        affiliation_registry.canonical_json_bytes(parts).decode("utf-8"),
    ))


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


def record_affiliation_observation(
        conn: sqlite3.Connection, paper_id: int, record: dict, ordinal: int,
        registry: dict, *, paper_key: str | None = None,
        pending_ids: set[str] | None = None,
        terminal_decisions: dict[str, tuple[str, str]] | None = None,
        pending_now: str | None = None) -> str | None:
    """Store every raw source slot and resolve only exact reviewed aliases offline."""
    raw = unicodedata.normalize(
        "NFC", str(record.get("raw_name") or record.get("name") or "").strip())
    if not raw:
        return
    source = str(record.get("source") or "review").split("+")[0]
    source = source if source in {"scopus", "pdf", "review"} else "legacy"
    country = str(record.get("country") or country_from_raw(raw) or "")
    country_code = str(record.get("country_code") or "").strip().upper()
    external_identifiers = dict(record.get("external_identifiers") or {})
    if record.get("scopus_id"):
        external_identifiers.setdefault("scopus_id", str(record["scopus_id"]))
    external_json = affiliation_registry.canonical_json_bytes(external_identifiers).decode("utf-8")
    context = record.get("context") or record.get("raw_context") or {}
    context_json = affiliation_registry.canonical_json_bytes(context)
    normalized = affiliation_registry.normalize_name(raw)
    source_record_key = str(record.get("source_record_key") or paper_key or paper_id)
    stable_slug = _paper_stable_slug(conn, paper_id, paper_key)
    slot_id = _uuid5_affiliation_observation(
        [stable_slug, source, source_record_key, ordinal])
    now = pending_now or time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    conn.execute("INSERT OR IGNORE INTO observed_affiliation_slots VALUES (?,?,?,?,?,?)",
                 (slot_id, paper_id, source, source_record_key, ordinal, now))
    context_digest = hashlib.sha256(context_json).hexdigest()
    normalized_country = country_code or affiliation_registry.normalize_name(country)
    content = hashlib.sha256(affiliation_registry.canonical_json_bytes(
        [raw, normalized_country, external_identifiers, context_digest])).hexdigest()
    prior = conn.execute(
        "SELECT observation_id,observation_version,raw_content_sha256,current_decision_id,"
        "resolution_status FROM observed_affiliations WHERE observation_slot_id=? AND is_current=1",
        (slot_id,)).fetchone()
    if prior and prior[2] == content and prior[4] != "superseded":
        conn.execute("UPDATE observed_affiliations SET last_seen_at=? WHERE observation_id=?",
                     (now, prior[0]))
        return slot_id
    affected_pending_ids = set()
    local_terminal: dict[str, tuple[str, str]] = {}
    if prior:
        affected_pending_ids.update(row[0] for row in conn.execute(
            "SELECT pending_id FROM affiliation_pending_observations WHERE observation_id=?",
            (prior[0],)))
    version = prior[1] + 1 if prior else 1
    observation_id = _uuid5_affiliation_observation([slot_id, version, content])
    candidates, resolution_reason = _registry_candidates(
        conn, normalized, country, country_code, external_identifiers)
    status, selected = ("resolved", candidates[0]) if len(candidates) == 1 else (
        ("ambiguous", None) if candidates else ("unseen", None))
    digest = _registry_digest()
    if prior:
        supersession_id = hashlib.sha256(
            ("superseded:" + prior[0] + ":" + observation_id).encode()).hexdigest()
        sequence = conn.execute(
            "SELECT COALESCE(MAX(decision_sequence),0)+1 FROM "
            "affiliation_resolution_decisions WHERE observation_id=?", (prior[0],)
        ).fetchone()[0]
        conn.execute(
            "INSERT INTO affiliation_resolution_decisions VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
            (supersession_id, prior[0], sequence, "superseded", None,
             "superseded_to_observation:" + observation_id, 1.0, digest,
             registry["policy_version"], now, now, prior[3] or None))
        conn.execute(
            "UPDATE observed_affiliations SET is_current=0,"
            "resolution_status='superseded',current_decision_id=? "
            "WHERE observation_id=?",
            (supersession_id, prior[0]))
        for pending_id in affected_pending_ids:
            local_terminal[pending_id] = ("rejected", supersession_id)
    conn.execute("INSERT INTO observed_affiliations VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                 (observation_id, slot_id, version, content, raw, normalized, country_code, country,
                  external_json, context_digest, selected, status, None, digest,
                  registry["policy_version"], now, now, 1, prior[0] if prior else None, None))
    if prior:
        conn.execute(
            "UPDATE observed_affiliations SET superseded_by_observation_id=? "
            "WHERE observation_id=?",
            (observation_id, prior[0]))
    decision_id = hashlib.sha256(("decision:" + observation_id).encode()).hexdigest()
    conn.execute(
        "INSERT INTO affiliation_resolution_decisions VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
        (decision_id, observation_id, 1, status, selected,
         resolution_reason if selected else "offline_registry_no_unique_alias",
         1.0 if selected else 0.0, digest, registry["policy_version"], now, now, None))
    for rank, candidate in enumerate(candidates, 1):
        conn.execute(
            "INSERT INTO affiliation_decision_candidates VALUES (?,?,?,?)",
            (decision_id, candidate, rank, resolution_reason))
    conn.execute("UPDATE observed_affiliations SET current_decision_id=? WHERE observation_id=?",
                 (decision_id, observation_id))
    if status == "resolved":
        for pending_id in affected_pending_ids:
            local_terminal[pending_id] = ("resolved", decision_id)
    else:
        pending_id = hashlib.sha256(
            affiliation_registry.canonical_json_bytes(
                [normalized, country_code, external_identifiers])).hexdigest()
        conn.execute(
            "INSERT OR IGNORE INTO affiliation_pending_cases "
            "(pending_id,normalized_raw_name,observed_country_code,"
            "external_identifiers_json,status,reason_code,first_seen_at,last_seen_at,"
            "active_observation_count,lifetime_observation_count) VALUES (?,?,?,?,?,?,?,?,?,?)",
            (pending_id, normalized, country_code, external_json, "open",
             "offline_registry_no_unique_alias", now, now, 1, 1))
        conn.execute("INSERT OR IGNORE INTO affiliation_pending_observations VALUES (?,?,?)",
                     (pending_id, observation_id, now))
        affected_pending_ids.add(pending_id)
        local_terminal.pop(pending_id, None)
    if pending_ids is None:
        recount_affiliation_pending_cases(conn, affected_pending_ids, local_terminal, now)
    else:
        pending_ids.update(affected_pending_ids)
        if terminal_decisions is not None:
            terminal_decisions.update(local_terminal)
    return slot_id
def supersede_removed_affiliation_slots(
        conn: sqlite3.Connection, paper_id: int, paper_key: str,
        seen_slots: set[str], registry: dict, *, pending_ids: set[str] | None = None,
        terminal_decisions: dict[str, tuple[str, str]] | None = None,
        pending_now: str | None = None) -> None:
    """Close current versions for source slots removed from a rebuilt paper."""
    now = pending_now or time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    digest = _registry_digest()
    local_pending_ids: set[str] = set()
    local_terminal: dict[str, tuple[str, str]] = {}
    rows = conn.execute(
        "SELECT o.observation_id,o.current_decision_id FROM observed_affiliation_slots s "
        "JOIN observed_affiliations o USING(observation_slot_id) "
        "WHERE s.paper_id=? AND o.is_current=1",
        (paper_id,)).fetchall()
    for observation_id, previous_decision in rows:
        if conn.execute("SELECT observation_slot_id FROM observed_affiliations WHERE observation_id=?",
                        (observation_id,)).fetchone()[0] in seen_slots:
            continue
        decision_id = hashlib.sha256(("removed:" + observation_id).encode()).hexdigest()
        sequence = conn.execute(
            "SELECT COALESCE(MAX(decision_sequence),0)+1 FROM affiliation_resolution_decisions "
            "WHERE observation_id=?", (observation_id,)).fetchone()[0]
        conn.execute("INSERT OR IGNORE INTO affiliation_resolution_decisions VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                     (decision_id, observation_id, sequence, "superseded", None,
                      "source_slot_removed", 1.0, digest, registry["policy_version"],
                      now, now, previous_decision or ""))
        conn.execute("UPDATE observed_affiliations SET resolution_status='superseded',"
                     "current_decision_id=? WHERE observation_id=?", (decision_id, observation_id))
        for (pending_id,) in conn.execute(
                "SELECT pending_id FROM affiliation_pending_observations WHERE observation_id=?",
                (observation_id,)):
            local_pending_ids.add(pending_id)
            local_terminal[pending_id] = ("rejected", decision_id)
    if pending_ids is None:
        recount_affiliation_pending_cases(conn, local_pending_ids, local_terminal, now)
    else:
        pending_ids.update(local_pending_ids)
        if terminal_decisions is not None:
            terminal_decisions.update(local_terminal)
def repair_terminal_superseded_current_slots(conn: sqlite3.Connection) -> None:
    """Restore one current terminal row for legacy slots that lost it on removal."""
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    rows = conn.execute(
        "SELECT o.observation_id,o.current_decision_id FROM observed_affiliation_slots s "
        "JOIN observed_affiliations o USING(observation_slot_id) "
        "WHERE o.resolution_status='superseded' "
        "AND o.observation_version=(SELECT MAX(latest.observation_version) "
        "FROM observed_affiliations latest WHERE latest.observation_slot_id=s.observation_slot_id) "
        "AND NOT EXISTS (SELECT 1 FROM observed_affiliations current_row "
        "WHERE current_row.observation_slot_id=s.observation_slot_id AND current_row.is_current=1) "
        "ORDER BY o.observation_slot_id"
    ).fetchall()
    pending_ids: set[str] = set()
    terminal: dict[str, tuple[str, str]] = {}
    for observation_id, decision_id in rows:
        conn.execute(
            "UPDATE observed_affiliations SET is_current=1 WHERE observation_id=?",
            (observation_id,))
        for (pending_id,) in conn.execute(
                "SELECT pending_id FROM affiliation_pending_observations "
                "WHERE observation_id=?", (observation_id,)):
            pending_ids.add(pending_id)
            terminal[pending_id] = ("rejected", decision_id or "")
    if pending_ids:
        recount_affiliation_pending_cases(conn, pending_ids, terminal, now)

def source_affiliation_records(scopus_records: list[dict],
                               fallback_lines: list[str]) -> list[dict]:
    """Preserve each source-cardinality record before compatibility deduplication."""
    records = []
    for ordinal, source_record in enumerate(scopus_records):
        record = dict(source_record)
        raw = str(record.get("raw_name") or record.get("name") or "").strip()
        if not raw:
            continue
        record.update({
            "raw_name": raw,
            "source": "scopus",
            "source_record_key": f"scopus:{record.get('scopus_id') or ordinal}",
            "context": {"scopus_affiliation": source_record},
            "_source_ordinal": ordinal,
        })
        records.append(record)
    for ordinal, raw in enumerate(fallback_lines):
        raw = str(raw).strip()
        if not raw:
            continue
        records.append({
            "raw_name": raw,
            "source": "review",
            "source_record_key": "review:header",
            "context": {"review_affiliation": raw},
            "_source_ordinal": ordinal,
        })
    return records


def is_latest_affiliation_schema(conn: sqlite3.Connection) -> bool:
    metadata = conn.execute(
        "SELECT schema_version FROM affiliation_registry_metadata WHERE singleton=1"
    ).fetchone() if conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' "
        "AND name='affiliation_registry_metadata'").fetchone() else None
    if metadata != (AFFILIATION_SCHEMA_VERSION,):
        return False
    required_columns = {
        "affiliation_organizations": {"organization_id", "status"},
        "affiliation_organization_redirects": {
            "old_organization_id", "survivor_organization_id", "event_id"},
        "observed_affiliations": {
            "observation_id", "supersedes_observation_id",
            "superseded_by_observation_id"},
        "affiliation_pending_cases": {
            "pending_id", "active_observation_count",
            "lifetime_observation_count", "resolved_event_id"},
        "affiliation_enrichment_attempts": {
            "attempt_id", "pending_id", "provider", "started_at", "finished_at",
            "outcome", "response_digest", "error_class", "proposal_digest"},
    }
    for table, expected in required_columns.items():
        columns = {
            row[1] for row in conn.execute(f'PRAGMA table_info("{table}")')
        }
        if not expected <= columns:
            return False
    return True

def _build_unlocked(entries: list[dict], db_path: Path, update_zotero: bool = False,
          skip_zotero: bool = False, offline: bool = False) -> dict:
    total = len(entries)
    print(f"[bibliography] starting {total} papers", flush=True)
    start = time.perf_counter(); db_path.parent.mkdir(parents=True, exist_ok=True)
    if db_path.exists() and db_path.stat().st_size:
        probe = sqlite3.connect(db_path)
        try:
            if not is_latest_affiliation_schema(probe):
                raise RuntimeError(
                    "bibliography DB requires controlled migration: "
                    f"python pipeline/repair_bibliography_institutions.py --db {db_path} --execute")
        finally:
            probe.close()
    conn = sqlite3.connect(db_path)
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
    registry = project_affiliation_registry(conn)
    initialize_institution_registry(conn)
    conn.commit()
    zitems = [] if skip_zotero or offline else fetch_zotero_items()
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
            zitem = zotero_match(
                {"title": title, "doi": doi, "arxiv": arxiv}, zitems
            ) if zitems else None
            zdata = zitem.get("data", {}) if zitem else {}
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

            local_bib = {
                "title": title,
                "journal": str(
                    official.get("journal") or meta.get("journal")
                    or p.get("journal") or zdata.get("publicationTitle") or ""
                ).strip(),
                "date": str(
                    official.get("date") or meta.get("date")
                    or p.get("date") or zdata.get("date") or ""
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
                offline=offline)
            source_records = source_affiliation_records(
                scopus_record.get("affiliations") or [], raw_affs)
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
                zitem.get("key", "") if zitem else p.get("zotero_item_key", ""),
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
            conn.execute("DELETE FROM paper_authors WHERE paper_id=?", (pid,)); conn.execute("DELETE FROM paper_institutions WHERE paper_id=?", (pid,))
            authors = meta.get("authors") or p.get("authors") or []
            if isinstance(authors, str): authors = [x.strip() for x in re.split(r"[,;]", authors) if x.strip()]
            for order, author in enumerate(authors, 1):
                aid = upsert(conn, "authors", str(author).strip(), "display_name")
                conn.execute("INSERT OR IGNORE INTO paper_authors VALUES (?,?,?,?,?,?)", (pid,aid,order,int(order==1),0,"review.frontmatter/_papers_index"))
            seen_slots = set()
            pending_ids: set[str] = set()
            terminal_decisions: dict[str, tuple[str, str]] = {}
            pending_now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            for record in source_records:
                slot_id = record_affiliation_observation(
                    conn, pid, record, record["_source_ordinal"], registry,
                    paper_key=p["slug"], pending_ids=pending_ids,
                    terminal_decisions=terminal_decisions, pending_now=pending_now)
                if slot_id:
                    seen_slots.add(slot_id)
            for record in affiliation_records:
                name = canonical_institution(record["name"])
                raw = record.get("raw_name") or name
                country = record.get("country") or country_from_raw(raw)
                external_identifiers = dict(record.get("external_identifiers") or {})
                if record.get("scopus_id"):
                    external_identifiers.setdefault("scopus_id", str(record["scopus_id"]))
                candidates, _reason = _registry_candidates(
                    conn, affiliation_registry.normalize_name(raw), country,
                    str(record.get("country_code") or "").strip().upper(),
                    external_identifiers)
                organization_id = candidates[0] if len(candidates) == 1 else None
                if organization_id:
                    row = conn.execute(
                        "SELECT institution_id FROM institutions "
                        "WHERE organization_id=?", (organization_id,)).fetchone()
                else:
                    row = conn.execute(
                        "SELECT institution_id FROM institutions "
                        "WHERE normalized_name=? AND country_name_en=?",
                        (norm(name), country)).fetchone()
                iid = row[0] if row else conn.execute(
                    "INSERT INTO institutions "
                    "(institution_name,normalized_name,country_name_en,"
                    "organization_id,source) VALUES (?,?,?,?,?)",
                    (name, norm(name), country, organization_id,
                     record["source"])).lastrowid
                if organization_id:
                    conn.execute("UPDATE institutions SET organization_id=? WHERE institution_id=?",
                                 (organization_id, iid))
                conn.execute("INSERT OR IGNORE INTO institution_aliases (raw_name,normalized_alias,institution_id) VALUES (?,?,?)", (raw,norm(raw),iid))
                conn.execute("INSERT OR IGNORE INTO paper_institutions (paper_id,institution_id,raw_name,country_name,source) VALUES (?,?,?,?,?)", (pid,iid,raw,country,record["source"]))
            supersede_removed_affiliation_slots(
                conn, pid, p["slug"], seen_slots, registry, pending_ids=pending_ids,
                terminal_decisions=terminal_decisions, pending_now=pending_now)
            if pending_ids:
                recount_affiliation_pending_cases(
                    conn, pending_ids, terminal_decisions, pending_now)
            for kind, path in (("review",review),("text",text)):
                if path.exists(): conn.execute("INSERT OR REPLACE INTO source_documents VALUES (?,?,?,?,?)", (pid,kind,rel(path),sha256(path),path.stat().st_size))
            conn.commit()
            print(f"[bibliography] progress={index}/{total} ({index / total * 100:.1f}%) title={title[:100]}", flush=True)
    _project_compatibility_groups(conn, registry)
    conn.commit()
    conn.execute("PRAGMA optimize"); conn.close()
    return {"processed":len(entries),"seconds":round(time.perf_counter()-start,4),"zotero_items_seen":len(zitems),"zotero_updated":zupdated,"formal_publications_resolved":resolved,"db":str(db_path)}


def build(entries: list[dict], db_path: Path, update_zotero: bool = False,
          skip_zotero: bool = False, offline: bool = False) -> dict:
    """Build while excluding migration recovery and every other DB writer."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    descriptor = affiliation_registry.acquire_bibliography_writer_lock(db_path)
    try:
        return _build_unlocked(
            entries, db_path, update_zotero=update_zotero,
            skip_zotero=skip_zotero, offline=offline)
    finally:
        affiliation_registry.release_bibliography_writer_lock(db_path, descriptor)


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

def publish_shared_db(db_path: Path) -> str:
    """Atomically publish a locally built DB into the shared Google Drive."""
    if db_path.resolve() == SHARED_DB.resolve():
        return str(db_path)
    SHARED_ROOT.mkdir(parents=True, exist_ok=True)
    temp = SHARED_DB.with_name(SHARED_DB.name + ".tmp")
    shutil.copy2(db_path, temp)
    os.replace(temp, SHARED_DB)
    return str(SHARED_DB)

def changed_entries(entries: list[dict], db_path: Path) -> list[dict]:
    """Return papers whose source review/text files are new or changed."""
    if not db_path.exists():
        return entries
    conn = sqlite3.connect(db_path)
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
    ap.add_argument("--changed-only", action="store_true",
                    help="process only papers whose review.md/text.md changed")
    ap.add_argument("--no-email", action="store_true")
    ap.add_argument("--skip-zotero", action="store_true",
                    help="skip the full Zotero library scan for a local incremental repair")
    ap.add_argument("--slugs", help="comma-separated slug prefixes to rebuild")
    ap.add_argument("--offline", action="store_true",
                    help="use the deterministic offline affiliation registry")
    args = ap.parse_args()
    entries = load_entries()
    if args.slugs:
        prefixes = [value.strip() for value in args.slugs.split(",") if value.strip()]
        entries = [p for p in entries if any(p["slug"].startswith(prefix) for prefix in prefixes)]
    if args.changed_only:
        entries = changed_entries(entries, args.output)
    elif not args.all:
        entries = random.Random(args.seed).sample(entries, min(args.sample, len(entries)))
    if not entries:
        if args.output.exists():
            try:
                result = build([], args.output, False, True, args.offline)
            except RuntimeError as exc:
                print(str(exc), file=sys.stderr)
                return 3
            print(json.dumps({**result, "changed": 0}, ensure_ascii=False, indent=2))
            return 0
        print(json.dumps({"processed": 0, "changed": 0, "db": str(args.output)}, ensure_ascii=False, indent=2))
        return 0
    try:
        result = build(entries, args.output, args.update_zotero, args.skip_zotero, args.offline)
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
