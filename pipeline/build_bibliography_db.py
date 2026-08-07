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
import urllib.parse
import urllib.request
from pathlib import Path

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
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

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
 group_id INTEGER PRIMARY KEY, group_name TEXT NOT NULL UNIQUE, normalized_name TEXT NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS institutions (
 institution_id INTEGER PRIMARY KEY, institution_name TEXT NOT NULL UNIQUE,
 normalized_name TEXT NOT NULL UNIQUE, group_id INTEGER REFERENCES institution_groups(group_id),
 source TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS institution_aliases (
 alias_id INTEGER PRIMARY KEY, raw_name TEXT NOT NULL UNIQUE, normalized_alias TEXT NOT NULL UNIQUE,
 institution_id INTEGER NOT NULL REFERENCES institutions(institution_id));
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


def ensure_schema_migrations(conn: sqlite3.Connection) -> None:
    """Add bibliographic columns to databases created by earlier releases."""
    existing = {
        row[1] for row in conn.execute("PRAGMA table_info(papers)").fetchall()
    }
    for name, sql_type in PAPER_SCHEMA_COLUMNS.items():
        if name not in existing:
            conn.execute(f"ALTER TABLE papers ADD COLUMN {name} {sql_type}")


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip()).casefold()


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


def institution_from_raw(raw: str) -> tuple[str, str] | None:
    raw = re.sub(r"\{[^}]*\}", " ", raw)
    raw = re.sub(r"\S+@\S+", " ", raw)
    raw = re.sub(r"^[\d\s*†‡(),.-]+", "", raw)
    raw = re.sub(r"\s+", " ", raw).strip(" ,;:-")
    if len(raw) < 5:
        return None
    if re.match(r"^(abstract|keywords?|introduction|research|fine[- ]tuning|limited task|correspondence|computational|deep learning)\b", raw, re.I):
        return None
    group = ""
    for name, pattern in GROUPS:
        if re.search(pattern, raw, re.I):
            group = name
            break
    parts = [p.strip(" ,;:-") for p in re.split(r"[,;|]", raw) if p.strip()]
    preferred = [p for p in parts if re.search(r"\b(university|institute|laborator|academy|college|hospital|centre|center|network)\b|Microsoft Research|CNRS|ETH|MIT|Caltech", p, re.I)]
    candidate = preferred[-1] if preferred else raw
    candidate = re.sub(r"^(department|school|faculty|division|institute of|laboratory of)\b.*?,\s*", "", candidate, flags=re.I)
    candidate = re.sub(r"^(?:USA|UK|Canada|China|Germany|France)\s*\d*\s*", "", candidate, flags=re.I)
    candidate = re.sub(r"\s+", " ", candidate).strip(" ,;:-")
    university = re.search(r"\bUniversity\s+of\s+[A-Z][A-Za-z .&'’-]+|\b[A-Z][A-Za-z .&'’-]+\s+University\b", candidate)
    institute = re.search(r"\b[A-Z][A-Za-z .&'’-]+\s+(?:Institute|Academy|College|Hospital|Centre|Center|Network)\b|\bMicrosoft Research\b", candidate)
    if university or institute:
        candidate = (university or institute).group(0).strip(" ,;:-")
    elif not re.search(r"\b(?:MIT|ETH|CNRS)\b", candidate):
        return None
    if len(candidate) < 5 or len(candidate) > 180 or re.match(r"^(research|department|university|institute)$", candidate, re.I):
        return None
    return candidate, group
INSTITUTION_CANONICAL_ALIASES = [
    (r"^University of Toronto Faculty of Medicine$", "University of Toronto"),
    (r"^University Health Network,? Toronto.*$", "University Health Network"),
    (r"^Microsoft Research,? Redmond.*$", "Microsoft Research"),
]


def canonical_institution(name: str) -> str:
    value = re.sub(r"\s+", " ", (name or "")).strip(" ,;:-")
    for pattern, canonical in INSTITUTION_CANONICAL_ALIASES:
        if re.match(pattern, value, re.I):
            return canonical
    m = re.match(r"^(University of [A-Z][A-Za-z .&'’-]+?)\s+(?:Faculty|School|Department)\b", value)
    return m.group(1).strip() if m else value


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


def reconcile_affiliations(scopus_records: list[dict], pdf_text: str,
                           fallback_lines: list[str]) -> list[dict]:
    """Validate Scopus against PDF text and add institutions missing in Scopus."""
    flat = re.sub(r"\s+", " ", pdf_text)
    normalized_pdf = norm(flat)
    out = {}
    for rec in scopus_records:
        name = canonical_institution(rec["name"])
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
        parsed = institution_from_raw(raw)
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


def build(entries: list[dict], db_path: Path, update_zotero: bool = False,
          skip_zotero: bool = False) -> dict:
    total = len(entries)
    print(f"[bibliography] starting {total} papers", flush=True)
    start = time.perf_counter(); db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.executescript(SCHEMA)
    ensure_schema_migrations(conn)
    zitems = [] if skip_zotero else fetch_zotero_items()
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
            ) if (arxiv or doi.lower().startswith("10.48550")) else {}
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
            scopus_record = fetch_scopus_record(doi, title)
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
                scopus_record.get("affiliations") or [], pdf_text, raw_affs)
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
            for record in affiliation_records:
                name = canonical_institution(record["name"])
                raw = record.get("raw_name") or name
                group = ""
                for group_name, pattern in GROUPS:
                    if re.search(pattern, name, re.I):
                        group = group_name
                        break
                gid = None
                if group:
                    row = conn.execute("SELECT group_id FROM institution_groups WHERE normalized_name=?", (norm(group),)).fetchone()
                    gid = row[0] if row else conn.execute("INSERT INTO institution_groups (group_name,normalized_name) VALUES (?,?)", (group,norm(group))).lastrowid
                row = conn.execute("SELECT institution_id FROM institutions WHERE normalized_name=?", (norm(name),)).fetchone()
                iid = row[0] if row else conn.execute("INSERT INTO institutions (institution_name,normalized_name,group_id,source) VALUES (?,?,?,?)", (name,norm(name),gid,record["source"])).lastrowid
                conn.execute("INSERT OR IGNORE INTO institution_aliases (raw_name,normalized_alias,institution_id) VALUES (?,?,?)", (raw,norm(raw),iid))
                country = record.get("country") or country_from_raw(raw)
                conn.execute("INSERT OR IGNORE INTO paper_institutions (paper_id,institution_id,raw_name,country_name,source) VALUES (?,?,?,?,?)", (pid,iid,raw,country,record["source"]))
            for kind, path in (("review",review),("text",text)):
                if path.exists(): conn.execute("INSERT OR REPLACE INTO source_documents VALUES (?,?,?,?,?)", (pid,kind,rel(path),sha256(path),path.stat().st_size))
            print(f"[bibliography] progress={index}/{total} ({index / total * 100:.1f}%) title={title[:100]}", flush=True)
    conn.execute("PRAGMA optimize"); conn.close()
    return {"processed":len(entries),"seconds":round(time.perf_counter()-start,4),"zotero_items_seen":len(zitems),"zotero_updated":zupdated,"formal_publications_resolved":resolved,"db":str(db_path)}


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
        print(json.dumps({"processed": 0, "changed": 0, "db": str(args.output)}, ensure_ascii=False, indent=2))
        return 0
    result = build(entries, args.output, args.update_zotero, args.skip_zotero)
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
