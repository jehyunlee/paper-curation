"""Detect papers whose bibliography belongs to a different work.

Three defects were measured in the shipped DB, all with the same effect — a
paper carrying another paper's title, journal and pagination:

1. A placeholder where a DOI should be. Review frontmatter is LLM-extracted,
   and with no DOI on the PDF the model wrote the absence down as a word:
   "N/A" (177 papers), "미제공" (78), "미공개" (11), "미기재" (7), "-" (7),
   "논문", "해당", "제공되지". `clean_doi` passed those through and
   `zotero_match` compares DOIs, so every paper holding the same placeholder
   matched the one Zotero item whose DOI field held it.

2. One Zotero item on many papers. A Zotero item is one work; 342 papers were
   attached to 8 items, 177 of them to a single item titled "Semantic
   Scholar", and each inherited that item's bibliography.

3. The DB title disagreeing with the paper's own review. Zotero item RM7J55RG
   describes "The reorganization of the American innovation ecosystem …"
   (Industrial and Corporate Change) but carries the DOI and URL of a 2021
   Frontiers paper by Altman and Cohen, so paper 1042 was stored under the
   wrong title, journal, volume, pages, publisher and ISSN.

The checks are pure and read-only: they name suspects, they do not repair.
"""
from __future__ import annotations

import difflib
import re
import sqlite3
from pathlib import Path

# Same shape `build_bibliography_db.clean_doi` now enforces at the boundary.
DOI_PATTERN = re.compile(r"^10\.\d{4,9}/\S+$")

# Below this, two titles are different works. Measured on this corpus: genuine
# subtitle and punctuation drift stays above 0.85, while every one of the 308
# contaminated rows sat under 0.30.
TITLE_AGREEMENT_FLOOR = 0.60

_FRONTMATTER_TITLE = re.compile(r'^title:\s*"?(.+?)"?\s*$', re.M)
# Hiragana/katakana, CJK ideographs, Hangul syllables.
_CJK = re.compile(r"[\u3040-\u30ff\u3400-\u9fff\uac00-\ud7af]")


def _norm(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").strip()).casefold()


def review_title(papers_dir: Path, slug: str) -> str:
    """Title from a paper's own review frontmatter, or "" when unreadable."""
    path = papers_dir / slug / "review.md"
    try:
        head = path.read_text(encoding="utf-8", errors="replace")[:2000]
    except OSError:
        return ""
    match = _FRONTMATTER_TITLE.search(head)
    return match.group(1).strip() if match else ""


def cjk_ratio(value: str) -> float:
    """Share of a title's letters written in a CJK script."""
    letters = [char for char in value if char.isalpha()]
    if not letters:
        return 0.0
    return sum(1 for char in letters if _CJK.match(char)) / len(letters)


def comparable(left: str, right: str) -> bool:
    """Whether two titles can be compared at all.

    A review may be titled in Korean while the DB holds the English title
    (paper 409, "AI 아이디어가 인간의 창의성…"). Those disagree on nearly every
    character without either being wrong, so a cross-script pair carries no
    evidence and is not judged. The test is a ratio rather than the presence
    of a Latin letter, because that Korean title contains "AI".
    """
    if not left or not right:
        return False
    lower, upper = sorted((cjk_ratio(left), cjk_ratio(right)))
    return not (lower < 0.1 and upper >= 0.3)


def title_similarity(left: str, right: str) -> float:
    return difflib.SequenceMatcher(None, _norm(left), _norm(right)).ratio()


def placeholder_dois(conn: sqlite3.Connection) -> list[dict]:
    """Papers whose `doi` column holds something that is not a DOI."""
    return [
        {"slug": slug, "doi": doi}
        for slug, doi in conn.execute(
            "SELECT slug, doi FROM papers WHERE doi<>'' AND doi IS NOT NULL")
        if not DOI_PATTERN.match(doi.strip())
    ]


_CORRECTION_PREFIX = re.compile(
    r"^\s*(?:publisher\s+correction|author\s+correction|correction|"
    r"corrigendum|erratum|retraction|addendum)\s*[:\-–—]\s*", re.I)


def _correction_pair(titles: list[str]) -> bool:
    """Whether these titles are a correction notice and the work it corrects.

    A journal publishes "Correction: X" as its own article, and Zotero may
    hold one item for both. That is the library being terse, not a paper
    wearing another paper's bibliography.
    """
    if len(titles) != 2:
        return False
    stripped = {_norm(_CORRECTION_PREFIX.sub("", title)) for title in titles}
    return len(stripped) == 1 and any(
        _CORRECTION_PREFIX.match(title) for title in titles)


# A byline names people. "Research Policy" and "Aarhus University" match a
# two-capitalised-words shape too, so an organisation word disqualifies a
# candidate outright — otherwise a journal name reads as an author.
_PERSON_SHAPE = re.compile(r"^[A-Z][a-z'’\-]+(?:\s+[A-Z][a-z'’\-.]*){1,3}$")
_NOT_A_PERSON = re.compile(
    r"universit|institut|college|school|department|laborator|academy|"
    r"policy|review|journal|proceedings|press|society|center|centre|"
    r"hospital|company|corporation|research", re.I)


def _pdf_byline_names(header: str, known_surnames: set[str]) -> list[str]:
    """Names that look like people in a paper's front matter.

    Shape alone is not enough: "Citation Analysis", "Robot Manipulation" and
    "Human Demonstration" are two capitalised words too. The corpus already
    holds 12,900 author names, so a surname it has seen is the test — "Chen"
    passes, "Analysis" does not.
    """
    out = []
    for line in header.splitlines()[:12]:
        for chunk in re.split(r"[,;]|\band\b", line):
            chunk = re.sub(r"[\d*∗†‡§¶♣♢♡♠]+", "", chunk).strip()
            if not _PERSON_SHAPE.match(chunk) or _NOT_A_PERSON.search(chunk):
                continue
            if _norm(chunk.split()[-1]) in known_surnames:
                out.append(chunk)
    return out


def byline_disagreements(conn: sqlite3.Connection, papers_dir: Path,
                         header_of) -> list[dict]:
    """Papers whose PDF byline names nobody the record calls an author.

    A record and its PDF that share no author are not the same paper. The
    Industrial and Corporate Change item earlier in this corpus was found that
    way, and so is "Introspective growth", whose record lists Yongtao Liu
    while its PDF byline reads Siyang Wu.

    Both halves are required: the PDF must actually carry a byline — a report
    with a table of contents has none, and its authors legitimately appear
    nowhere near the front — and none of its names may match the record.
    """
    known_surnames = {
        _norm(name.split()[-1]) for (name,) in conn.execute(
            "SELECT display_name FROM authors") if name.split()}
    out = []
    for paper_id, slug, title in conn.execute(
            "SELECT paper_id, slug, title FROM papers ORDER BY paper_id"):
        text = papers_dir / slug / "text.md"
        if not text.exists():
            continue
        authors = [row[0] for row in conn.execute(
            "SELECT a.display_name FROM paper_authors pa"
            " JOIN authors a USING(author_id) WHERE pa.paper_id=?"
            " ORDER BY pa.author_order", (paper_id,))]
        if len(authors) < 2:
            continue
        header = header_of(text)
        folded = _norm(header)
        if any((parts := name.split()) and _norm(parts[-1]) in folded
               for name in authors):
            continue
        names = _pdf_byline_names(header, known_surnames)
        if len(names) >= 2:
            out.append({"slug": slug, "title": title,
                        "record_authors": authors[:3], "pdf_byline": names[:3]})
    return out


def shared_zotero_keys(conn: sqlite3.Connection,
                       papers_dir: Path | None = None) -> list[dict]:
    """Zotero items attached to more than one paper, worst first.

    `kind` separates the two ways this happens: `correction` when one paper
    corrects the other, `unresolved` when two papers genuinely claim one
    record — contamination, or the same paper filed under two slugs.

    The judgement reads each paper's **own review title**, never the stored
    one: sharing an item is exactly how a paper loses its title, so paper 2587
    is stored as "Overcoming disciplinary divides…" while its review says
    "Correction: Overcoming disciplinary divides…". Deciding from the stored
    title would ask the contamination to describe itself.
    """
    rows = conn.execute(
        "SELECT zotero_item_key, COUNT(*) n, MIN(title) title,"
        " GROUP_CONCAT(slug, '|') slugs FROM papers"
        " WHERE zotero_item_key<>'' AND zotero_item_key IS NOT NULL"
        " GROUP BY zotero_item_key HAVING n > 1 ORDER BY n DESC").fetchall()
    out = []
    for key, count, title, slugs in rows:
        slug_list = slugs.split("|")
        if papers_dir is None:
            titles = [row[0] for row in conn.execute(
                "SELECT title FROM papers WHERE zotero_item_key=?", (key,))]
        else:
            titles = [review_title(papers_dir, slug) or ""
                      for slug in slug_list]
        out.append({"zotero_item_key": key, "papers": count, "title": title,
                    "slugs": slug_list,
                    "kind": ("correction" if _correction_pair(titles)
                             else "unresolved")})
    return out


def title_disagreements(conn: sqlite3.Connection,
                        papers_dir: Path) -> list[dict]:
    """Papers whose stored title is not the title of their own review."""
    out = []
    for slug, title, doi, key in conn.execute(
            "SELECT slug, title, doi, zotero_item_key FROM papers"):
        own = review_title(papers_dir, slug)
        if not comparable(title, own):
            continue
        ratio = title_similarity(title, own)
        if ratio < TITLE_AGREEMENT_FLOOR:
            out.append({"slug": slug, "db_title": title, "review_title": own,
                        "similarity": round(ratio, 3), "doi": doi,
                        "zotero_item_key": key})
    return sorted(out, key=lambda row: row["similarity"])


def audit(conn: sqlite3.Connection, papers_dir: Path) -> dict:
    """Full report plus the exact slug set a repair has to re-ingest.

    A correction notice sharing its original's Zotero item is expected, so it
    is counted and shown but never queued for repair: re-ingesting it would
    change nothing.
    """
    placeholders = placeholder_dois(conn)
    shared = shared_zotero_keys(conn, papers_dir)
    try:
        import build_bibliography_db as _bib
        bylines = byline_disagreements(
            conn, papers_dir, lambda path: _bib.extract_header(path)[0])
    except Exception:                       # header parsing is optional here
        bylines = []
    unresolved = [row for row in shared if row["kind"] == "unresolved"]
    disagreements = title_disagreements(conn, papers_dir)
    affected = (
        {row["slug"] for row in placeholders}
        | {slug for row in unresolved for slug in row["slugs"]}
        | {row["slug"] for row in disagreements}
    )
    return {
        "placeholder_doi_papers": len(placeholders),
        "shared_zotero_keys": len(unresolved),
        "papers_on_a_shared_key": sum(row["papers"] for row in unresolved),
        "correction_pairs": sum(
            1 for row in shared if row["kind"] == "correction"),
        "title_disagreements": len(disagreements),
        "byline_disagreements": len(bylines),
        "affected_papers": len(affected),
        "affected_slugs": sorted(affected),
        "placeholder_doi_values": sorted(
            {row["doi"] for row in placeholders}),
        "shared_key_detail": unresolved[:20],
        "correction_pair_detail": [
            row for row in shared if row["kind"] == "correction"][:20],
        "title_disagreement_detail": disagreements[:20],
        "byline_disagreement_detail": bylines[:20],
    }
