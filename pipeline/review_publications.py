#!/usr/bin/env python3
"""Propose formal publications for preprints, then apply what the operator accepts.

A Zotero record entered when a paper was a preprint keeps saying preprint after
the paper appears in a journal, and the author list and its order often change
between the two. `build_bibliography_db` already looks a formal record up, but
only when the row carries an arXiv id or an arXiv DOI — 1,184 papers have
neither, so nothing is ever looked up for them, and it writes to Zotero without
asking.

Nothing here edits Zotero on its own. `--scan` searches by title and writes
proposals; `--page` renders them with the publisher URL to open and Accept /
Decline per paper; `--apply` writes only the accepted ones. A proposal records
the title similarity and every field that would change, including authors, so
the decision is made on evidence rather than on trust in a title match.

    python pipeline/review_publications.py --scan --limit 200
    python pipeline/review_publications.py --page
    python pipeline/review_publications.py --apply --decisions ~/Downloads/decisions.json
"""
from __future__ import annotations

import argparse
import difflib
import html
import json
import re
import sqlite3
import sys
import time
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "pipeline"
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import build_bibliography_db as bib          # noqa: E402

DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"
PROPOSALS = ROOT / ".cache" / "publication_proposals.json"
PAGE = ROOT / "reports" / "build" / "publication_review.html"
MIN_TITLE_SIMILARITY = 0.90
_OPENALEX_STATE = {"refusals": 0}
PREPRINT_HOSTS = ("arxiv", "biorxiv", "medrxiv", "chemrxiv", "ssrn",
                  "researchsquare", "preprints.org", "osf.io", "hal.science")

# A search by title also finds the dataset, the poster and the thesis that share
# the paper's name. The first proposal this produced was a Figshare *dataset*
# whose author list had shrunk from three names to one — accepted, it would have
# rewritten a paper's bibliography to point at a data deposit.
FORMAL_TYPES = ("article", "journal-article", "proceedings-article",
                "book-chapter", "review", "letter", "editorial",
                "book-part", "reference-entry")
REPOSITORY_VENUES = ("figshare", "zenodo", "datacite", "researchgate",
                     "semantic scholar", "osf", "dryad", "mendeley data",
                     "open science framework", "papers with code",
                     "techrxiv", "authorea", "hal", "dspace", "eprints")
# Repository DOI prefixes: figshare, Zenodo, OSF, Dryad, Mendeley Data.
REPOSITORY_DOI_PREFIXES = ("10.6084/", "10.5281/", "10.17605/", "10.5061/",
                           "10.17632/")


def _norm_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (value or "").lower()).strip()


def similarity(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, _norm_title(a), _norm_title(b)).ratio()


def looks_like_preprint(journal: str, doi: str, document_type: str) -> bool:
    haystack = f"{journal} {doi} {document_type}".lower()
    if any(host in haystack for host in PREPRINT_HOSTS):
        return True
    return not (journal or "").strip()


def candidates(conn: sqlite3.Connection, limit: int | None) -> list[dict]:
    """Papers whose Zotero record may predate formal publication."""
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT paper_id, slug, title, doi, arxiv_id, journal_name,"
        " document_type, zotero_item_key, publication_date"
        " FROM papers ORDER BY paper_id").fetchall()
    out = []
    for row in rows:
        doi = (row["doi"] or "").lower()
        if doi and not doi.startswith("10.48550/arxiv"):
            continue                    # already a publisher DOI
        if not looks_like_preprint(row["journal_name"], doi,
                                   row["document_type"] or ""):
            continue
        if not (row["title"] or "").strip():
            continue
        entry = dict(row)
        entry["author_count"] = conn.execute(
            "SELECT COUNT(*) FROM paper_authors WHERE paper_id=?",
            (row["paper_id"],)).fetchone()[0]
        out.append(entry)
        if limit and len(out) >= limit:
            break
    return out


def openalex_authors(work: dict) -> list[str]:
    return [
        (entry.get("author") or {}).get("display_name", "").strip()
        for entry in work.get("authorships") or []
        if (entry.get("author") or {}).get("display_name")]


def search_openalex(title: str) -> list[dict]:
    """Title search with the polite-pool identifier and backoff on 429.

    Anonymous calls share one rate limit and start refusing during a scan; a
    silent empty list looked exactly like "not published yet", which is the one
    answer this must never guess at.
    """
    # Circuit breaker: once OpenAlex has refused three times it refuses for the
    # rest of the run, and the exponential backoff was costing 30 s per paper
    # for an answer that never came. Crossref carries the scan from there.
    if _OPENALEX_STATE["refusals"] >= 3:
        return []
    url = ("https://api.openalex.org/works?per-page=5&search="
           + urllib.parse.quote(title[:250]))
    mail = _contact_email()
    if mail:
        url += "&mailto=" + urllib.parse.quote(mail)
    delay = 2.0
    for attempt in range(4):
        try:
            return bib.request_json(url).get("results", []) or []
        except Exception as exc:
            if "429" not in str(exc):
                return []
            if attempt == 2:
                _OPENALEX_STATE["refusals"] += 1
                if _OPENALEX_STATE["refusals"] == 3:
                    print("  [warn] OpenAlex 반복 429 — 이번 실행에서는 "
                          "Crossref 만 사용한다", file=sys.stderr)
                return []
            time.sleep(delay)
            delay *= 2
    return []


def _contact_email() -> str:
    """OpenAlex's polite pool wants a contact address; config already has one."""
    try:
        from config_loader import load_config
        config = load_config() or {}
    except Exception:
        return ""
    return str(config.get("unpaywall_email") or "").strip()


def search_crossref(title: str) -> list[dict]:
    """Crossref title search, shaped like an OpenAlex work.

    A second provider is not redundancy for its own sake: OpenAlex answered 429
    for every call during development, and an empty result is indistinguishable
    from "not published yet" — the one conclusion this must not reach by
    accident.
    """
    mail = _contact_email()
    url = ("https://api.crossref.org/works?rows=5&select=DOI,title,"
           "container-title,issued,volume,issue,page,publisher,ISSN,type,author"
           "&query.bibliographic=" + urllib.parse.quote(title[:250]))
    if mail:
        url += "&mailto=" + urllib.parse.quote(mail)
    try:
        items = bib.request_json(url).get("message", {}).get("items", []) or []
    except Exception as exc:
        print(f"  [warn] Crossref 실패: {exc}", file=sys.stderr)
        return []
    shaped = []
    for item in items:
        issued = ((item.get("issued") or {}).get("date-parts") or [[]])[0]
        date = "-".join(f"{part:02d}" if index else str(part)
                        for index, part in enumerate(issued[:3])) if issued else ""
        container = (item.get("container-title") or [""])[0]
        shaped.append({
            "display_name": (item.get("title") or [""])[0],
            "doi": item.get("DOI") or "",
            "type": item.get("type") or "",
            "publication_date": date,
            "primary_location": {"source": {
                "display_name": container,
                "host_organization_name": item.get("publisher") or "",
                "issn_l": (item.get("ISSN") or [""])[0]}},
            "biblio": {"volume": item.get("volume") or "",
                       "issue": item.get("issue") or "",
                       "first_page": (item.get("page") or "").split("-")[0],
                       "last_page": (item.get("page") or "").split("-")[-1]},
            "authorships": [
                {"author": {"display_name": " ".join(
                    x for x in (a.get("given"), a.get("family")) if x)}}
                for a in item.get("author") or []],
            "id": "https://doi.org/" + (item.get("DOI") or ""),
        })
    return shaped


def candidate_works(title: str) -> list[dict]:
    """Both providers, OpenAlex first; Crossref covers its rate limiting."""
    works = search_openalex(title)
    seen = {(w.get("doi") or "").lower() for w in works}
    for work in search_crossref(title):
        if (work.get("doi") or "").lower() not in seen:
            works.append(work)
    return works


def propose(paper: dict) -> dict | None:
    """Best formal record for one paper, or None when nothing convincing."""
    best = None
    for work in candidate_works(paper["title"]):
        score = similarity(paper["title"], work.get("display_name") or "")
        if score < MIN_TITLE_SIMILARITY:
            continue
        doi = bib.clean_doi((work.get("doi") or "").replace(
            "https://doi.org/", ""))
        if not doi or doi.lower().startswith("10.48550/arxiv"):
            continue
        if any(doi.lower().startswith(prefix)
               for prefix in REPOSITORY_DOI_PREFIXES):
            continue
        if (work.get("type") or "").lower() not in FORMAL_TYPES:
            continue
        venue = ((work.get("primary_location") or {}).get("source") or {})
        journal = venue.get("display_name") or ""
        low = journal.lower()
        if not journal or any(host in low for host in PREPRINT_HOSTS):
            continue
        if any(venue_name in low for venue_name in REPOSITORY_VENUES):
            continue
        # No author-count heuristic. It was written for the Figshare dataset
        # that first slipped through, but the type and repository filters
        # already refuse that, and providers truncate author lists — the rule
        # only ever rejected real papers.
        found_authors = openalex_authors(work)
        entry = {
            "doi": doi,
            "journal": journal,
            "date": work.get("publication_date") or "",
            "volume": str((work.get("biblio") or {}).get("volume") or ""),
            "issue": str((work.get("biblio") or {}).get("issue") or ""),
            "pages": "-".join(x for x in (
                (work.get("biblio") or {}).get("first_page"),
                (work.get("biblio") or {}).get("last_page")) if x),
            "publisher": venue.get("host_organization_name") or "",
            "issn": (venue.get("issn_l") or ""),
            "type": work.get("type") or "",
            "authors": found_authors,
            "similarity": round(score, 4),
            "openalex_id": work.get("id") or "",
        }
        if best is None or entry["similarity"] > best["similarity"]:
            best = entry
    if best is None:
        return None
    return {"slug": paper["slug"], "paper_id": paper["paper_id"],
            "zotero_item_key": paper["zotero_item_key"] or "",
            "current": {"title": paper["title"], "doi": paper["doi"] or "",
                        "journal": paper["journal_name"] or "",
                        "date": paper["publication_date"] or "",
                        "arxiv_id": paper["arxiv_id"] or ""},
            "proposed": best}


def db_authors(conn: sqlite3.Connection, paper_id: int) -> list[str]:
    return [row[0] for row in conn.execute(
        "SELECT a.display_name FROM paper_authors pa JOIN authors a"
        " ON a.author_id=pa.author_id WHERE pa.paper_id=?"
        " ORDER BY pa.author_order", (paper_id,))]


def _load_previous() -> tuple[list[dict], set[str]]:
    """Proposals and examined slugs from an earlier run.

    A full scan is 2,149 candidates against two rate-limited APIs — the better
    part of an hour — so it has to survive being interrupted and continue rather
    than re-asking about papers already answered.
    """
    if not PROPOSALS.exists():
        return [], set()
    try:
        payload = json.loads(PROPOSALS.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return [], set()
    return (payload.get("proposals") or [],
            set(payload.get("examined") or []))


def scan(db: Path, limit: int | None, *, restart: bool = False) -> dict:
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    try:
        proposals, examined = ([], set()) if restart else _load_previous()
        pool = [p for p in candidates(conn, None)
                if p["slug"] not in examined]
        if limit:
            pool = pool[:limit]
        checked = len(examined)
        done = 0
        for paper in pool:
            checked += 1
            done += 1
            examined.add(paper["slug"])
            found = propose(paper)
            if found:
                found["current"]["authors"] = db_authors(conn, paper["paper_id"])
                proposals.append(found)
            if checked % 25 == 0:
                # Checkpoint. A scan of every candidate takes the better part of
                # an hour against two rate-limited APIs, and losing all of it to
                # an interrupted run means nobody ever finishes one.
                _write_proposals(proposals, checked, examined)
                print(f"[scan] this run={done} / {len(pool)} · "
                      f"examined total={checked} · proposals={len(proposals)}",
                      flush=True)
            time.sleep(0.12)            # OpenAlex courtesy rate
    finally:
        conn.close()
    _write_proposals(proposals, checked, examined)
    return {"candidates_examined": checked, "proposals": len(proposals),
            "examined_total": len(examined), "file": str(PROPOSALS)}


def _write_proposals(proposals: list[dict], checked: int,
                     examined: set[str] | None = None) -> None:
    PROPOSALS.parent.mkdir(parents=True, exist_ok=True)
    tmp = PROPOSALS.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(
        {"generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
         "checked": checked, "examined": sorted(examined or []),
         "proposals": proposals},
        ensure_ascii=False, indent=1), encoding="utf-8")
    tmp.replace(PROPOSALS)


def _diff_rows(current: dict, proposed: dict) -> list[tuple[str, str, str]]:
    fields = (("journal", "저널"), ("doi", "DOI"), ("date", "발행일"),
              ("volume", "권"), ("issue", "호"), ("pages", "쪽"),
              ("publisher", "출판사"))
    rows = []
    for key, label in fields:
        new = str(proposed.get(key) or "")
        old = str(current.get(key) or "")
        if new and new != old:
            rows.append((label, old or "—", new))
    old_authors = current.get("authors") or []
    new_authors = proposed.get("authors") or []
    if new_authors and new_authors != old_authors:
        rows.append(("저자", " · ".join(old_authors) or "—",
                     " · ".join(new_authors)))
    return rows


def build_page() -> dict:
    payload = json.loads(PROPOSALS.read_text(encoding="utf-8"))
    proposals = payload["proposals"]
    esc = lambda v: html.escape(str(v), quote=True)          # noqa: E731
    css = (
        "*{box-sizing:border-box}body{margin:0;background:#f6f7f9;color:#1f2933;"
        "font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,"
        "'Apple SD Gothic Neo',sans-serif;line-height:1.6}"
        ".wrap{max-width:1060px;margin:0 auto;padding:30px 22px 90px}"
        "h1{font-size:24px;margin:0 0 4px}.sub{color:#7b8794;font-size:13.5px;"
        "margin:0 0 22px}"
        ".card{background:#fff;border:1px solid #e4e7eb;border-radius:9px;"
        "padding:16px 18px;margin:0 0 16px}"
        ".card.accepted{border-color:#0F9D58;box-shadow:inset 3px 0 0 #0F9D58}"
        ".card.declined{border-color:#D63423;box-shadow:inset 3px 0 0 #D63423;"
        "opacity:.6}"
        ".t{font-size:15px;font-weight:600;margin:0 0 6px}"
        ".meta{font-size:12.5px;color:#7b8794;margin:0 0 10px}"
        "table{border-collapse:collapse;width:100%;font-size:13px;margin:0 0 12px}"
        "th,td{border:1px solid #e4e7eb;padding:6px 9px;text-align:left;"
        "vertical-align:top}th{background:#f0f4f8;width:88px}"
        "td.old{color:#9aa5b1}td.new{color:#0b6b3a;font-weight:600}"
        "a{color:#2374D6}button{font:inherit;padding:7px 16px;border-radius:6px;"
        "border:1px solid #cbd2d9;background:#fff;cursor:pointer;margin-right:8px}"
        "button.ok{border-color:#0F9D58;color:#0b6b3a}"
        "button.no{border-color:#D63423;color:#a12817}"
        ".bar{position:fixed;left:0;right:0;bottom:0;background:#1f2933;"
        "color:#fff;padding:12px 22px;display:flex;gap:14px;align-items:center;"
        "font-size:13.5px}.bar button{background:#fff}"
        ".sim{font-variant-numeric:tabular-nums}"
    )
    parts = [f"<!DOCTYPE html><html lang=ko><head><meta charset=utf-8>"
             f"<title>정식 출간 확인</title><style>{css}</style></head><body>"
             "<div class=wrap><h1>정식 출간 확인</h1>",
             f"<p class=sub>후보 {payload['checked']}편 검사 · 제안 "
             f"{len(proposals)}건 · 제목 유사도 {MIN_TITLE_SIMILARITY} 이상만. "
             "링크를 열어 같은 논문인지 확인하고 Accept / Decline 을 누른 뒤 "
             "맨 아래에서 결정을 내려받아라. 이 페이지는 Zotero 를 고치지 않는다.</p>"]
    for n, item in enumerate(proposals):
        proposed, current = item["proposed"], item["current"]
        rows = _diff_rows(current, proposed)
        parts.append(f"<div class=card id='c{n}' data-slug='{esc(item['slug'])}'>")
        parts.append(f"<p class=t>{esc(current['title'])}</p>")
        parts.append(
            f"<p class=meta>slug <code>{esc(item['slug'])}</code> · Zotero "
            f"<code>{esc(item['zotero_item_key'] or '없음')}</code> · 유사도 "
            f"<span class=sim>{proposed['similarity']}</span> · 유형 "
            f"{esc(proposed['type'])}</p>")
        parts.append(
            f"<p><a href='https://doi.org/{esc(proposed['doi'])}' "
            f"target=_blank rel=noopener>출판사 페이지 열기 → "
            f"{esc(proposed['doi'])}</a></p>")
        parts.append("<table><tr><th></th><th>현재</th><th>제안</th></tr>")
        for label, old, new in rows:
            parts.append(f"<tr><th>{esc(label)}</th>"
                         f"<td class=old>{esc(old)}</td>"
                         f"<td class=new>{esc(new)}</td></tr>")
        parts.append("</table>")
        parts.append(f"<button class=ok onclick=\"mark({n},true)\">Accept</button>"
                     f"<button class=no onclick=\"mark({n},false)\">Decline</button>"
                     f"</div>")
    parts.append(
        "</div><div class=bar><span id=tally>결정 0 / " f"{len(proposals)}</span>"
        "<button onclick=save()>결정 내려받기 (decisions.json)</button>"
        "<span>내려받은 파일을 <code>--apply --decisions</code> 로 넘겨라</span>"
        "</div>")
    parts.append(
        "<script>const D={};const N=" + str(len(proposals)) + ";"
        "function mark(i,ok){const c=document.getElementById('c'+i);"
        "D[c.dataset.slug]=ok;c.className='card '+(ok?'accepted':'declined');"
        "document.getElementById('tally').textContent="
        "'결정 '+Object.keys(D).length+' / '+N;}"
        "function save(){const b=new Blob([JSON.stringify(D,null,1)],"
        "{type:'application/json'});const a=document.createElement('a');"
        "a.href=URL.createObjectURL(b);a.download='decisions.json';a.click();}"
        "</script></body></html>")
    PAGE.parent.mkdir(parents=True, exist_ok=True)
    PAGE.write_text("".join(parts), encoding="utf-8")
    return {"proposals": len(proposals), "page": str(PAGE)}


def apply_decisions(decisions_path: Path, db: Path, *, dry_run: bool) -> dict:
    payload = json.loads(PROPOSALS.read_text(encoding="utf-8"))
    by_slug = {item["slug"]: item for item in payload["proposals"]}
    decisions = json.loads(decisions_path.read_text(encoding="utf-8"))
    accepted = [slug for slug, ok in decisions.items() if ok and slug in by_slug]
    patched, failed = [], []
    for slug in accepted:
        item = by_slug[slug]
        key = item["zotero_item_key"]
        if not key:
            failed.append({"slug": slug, "why": "Zotero 아이템 키 없음"})
            continue
        if dry_run:
            patched.append(slug)
            continue
        try:
            ok = bib.patch_zotero({"key": key, "data": {"key": key}},
                                  item["proposed"])
            (patched if ok else failed).append(
                slug if ok else {"slug": slug, "why": "patch_zotero 실패"})
        except Exception as exc:
            failed.append({"slug": slug, "why": f"{type(exc).__name__}: {exc}"})
    return {"accepted": len(accepted),
            "declined": sum(1 for ok in decisions.values() if not ok),
            "patched": len(patched), "failed": failed, "dry_run": dry_run,
            "next": "python pipeline/build_bibliography_db.py --changed-only"}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--scan", action="store_true")
    mode.add_argument("--page", action="store_true")
    mode.add_argument("--apply", dest="do_apply", action="store_true")
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--limit", type=int)
    ap.add_argument("--decisions", type=Path)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--restart", action="store_true",
                    help="이전 스캔 결과를 버리고 처음부터")
    args = ap.parse_args()
    if args.scan:
        result = scan(args.db, args.limit, restart=args.restart)
    elif args.page:
        result = build_page()
    else:
        if not args.decisions or not args.decisions.exists():
            print("--decisions 파일이 필요하다", file=sys.stderr)
            return 2
        result = apply_decisions(args.decisions, args.db, dry_run=args.dry_run)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
