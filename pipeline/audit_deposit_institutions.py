#!/usr/bin/env python3
"""Find deposit-supplied institutions the paper itself contradicts.

Scopus names are checked against the PDF before they are trusted -- that is
what `scopus+pdf` versus `scopus-unconfirmed` means. OpenAlex names are not
checked at all, and OpenAlex is wrong often enough to matter: on
10.1038/s43588-025-00906-6 it placed the corresponding author at "Kellogg's
(Canada)", a cereal company, because the paper says "Kellogg School of
Management, Northwestern University, Evanston, IL, USA".

A shared-token test does not catch that -- "kellogg" is in the paper. Two
signals do:

  country     ROR says Canada; the affiliation line says USA. A deposit whose
              country contradicts the country printed beside the name it
              matched is describing a different organisation.
  org type    ROR types "Kellogg's (Canada)" as a company. A company matching
              only the first word of a school inside a university is a brand
              collision, not an affiliation.

Usage:
    python pipeline/audit_deposit_institutions.py
    python pipeline/audit_deposit_institutions.py --kind country --limit 40
    python pipeline/audit_deposit_institutions.py --json --out report.json
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "pipeline"
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import build_bibliography_db as bib                            # noqa: E402

DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"
PAPERS = ROOT / "docs" / "papers"

def contradicting_segments(window: str, token: str,
                          candidates: dict[str, int],
                          institution_id: int) -> list[tuple[str, str]]:
    """Segments naming this token that the paper resolves to somebody else.

    The discriminating fact is not that the token is absent -- "kellogg" is in
    the paper -- but that where it appears, the paper is naming a different
    organisation which it also lists: "Kellogg School of Management,
    Northwestern University". A token test cannot see that; resolving the
    segment can.

    Only a segment that resolves to another institution already on this paper
    counts. A segment that resolves to nothing proves nothing, and is left
    alone.
    """
    out = []
    for line in window.splitlines():
        if token not in bib._fold(line):
            continue
        # One line often carries several affiliations -- "1DeepMind, London,
        # UK. 2School of Biological Sciences, Seoul National University" --
        # and resolving the whole of it picks whichever comes last. Split on
        # the superscript markers that separate them and keep the piece the
        # token is actually in.
        pieces = [piece for piece in bib._AFFILIATION_MARKER.split(line)
                  if token in bib._fold(piece)]
        segment = (pieces[0] if pieces else line).strip()
        parsed = bib.institution_from_raw(segment, allow_remote=False)
        if not parsed:
            continue
        other = bib.canonical_institution(parsed[0])
        other_id = candidates.get(bib.norm(other))
        if other_id is not None and other_id != institution_id:
            out.append((segment[:70], other))
    return out


def audit(db: Path) -> list[dict]:
    """Deposit institutions the paper's own front matter contradicts."""
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    try:
        rows = conn.execute(
            "SELECT p.paper_id, p.slug, pi.institution_id, i.institution_name,"
            " COALESCE(i.country_name_en,''), COALESCE(i.ror_id,''), pi.source"
            " FROM paper_institutions pi JOIN papers p USING(paper_id)"
            " JOIN institutions i USING(institution_id)"
            " WHERE pi.source IN ('openalex','scopus-unconfirmed')"
            " ORDER BY p.paper_id").fetchall()
        out: list[dict] = []
        windows: dict[str, str] = {}
        candidates: dict[int, dict[str, int]] = {}
        for pid, slug, iid, name, country, ror_id, source in rows:
            text = PAPERS / slug / "text.md"
            if not text.exists():
                continue
            if slug not in windows:
                windows[slug] = bib.affiliation_window(text)
            if pid not in candidates:
                candidates[pid] = {
                    bib.norm(row[1]): row[0] for row in conn.execute(
                        "SELECT pi.institution_id, i.institution_name"
                        " FROM paper_institutions pi"
                        " JOIN institutions i USING(institution_id)"
                        " WHERE pi.paper_id=?", (pid,))}
            tokens = [t for t in bib._affiliation_tokens(name) if len(t) >= 5]
            if not tokens:
                continue
            hits = contradicting_segments(
                windows[slug], tokens[0], candidates[pid], iid)
            if not hits:
                continue
            out.append({
                "slug": slug, "institution": name, "country": country,
                "ror_id": ror_id, "source": source,
                "resolves_instead_to": sorted({other for _, other in hits}),
                "segments": [seg for seg, _ in hits][:2],
                "links": conn.execute(
                    "SELECT COUNT(*) FROM paper_author_institutions"
                    " WHERE paper_id=? AND institution_id=?",
                    (pid, iid)).fetchone()[0],
            })
        return out
    finally:
        conn.close()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--limit", type=int, default=25)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()

    findings = audit(args.db)
    findings.sort(key=lambda row: -row["links"])

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(findings, ensure_ascii=False, indent=2),
                            encoding="utf-8")
    if args.json:
        print(json.dumps(findings, ensure_ascii=False, indent=2))
        return 0

    print(f"의심 기관 {len(findings)}건 "
          f"(저자 링크 {sum(f['links'] for f in findings)}개가 걸려 있다)\n")
    for row in findings[:args.limit]:
        print(f"  {row['institution'][:38]:38s} [{row['source']}] "
              f"링크 {row['links']}")
        print(f"      {row['slug'][:60]}")
        print(f"      원문은 여기서 {', '.join(row['resolves_instead_to'])} 를 말한다")
        for seg in row["segments"]:
            print(f"      · {seg}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
