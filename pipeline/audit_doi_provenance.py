#!/usr/bin/env python3
"""Find papers whose DOI belongs to something they merely cite.

`10.1093/genetics/145.2.505` was recorded as the DOI of an ICML 2026 paper on
flow matching. It is a 1997 Genetics paper, and it appears in that ICML
paper's own reference list, 69% of the way through the text:

    Tavaré, S., ... Inferring Coalescence Times From DNA Sequence Data.
    Genetics, 145(2):505-518, February 1997. doi: 10.1093/genetics/145.2.505

The damage is not a wrong string in a field. Everything keyed on the DOI
follows it: OpenAlex was asked about that DOI and returned Simon Tavaré at the
University of Southern California, who was then written into the corpus as an
author of a paper published twenty-nine years later.

The signal is positional, not textual. A paper's own DOI is printed in its
front matter, or comes from Zotero and appears nowhere in the text at all. A
DOI that appears *only* deep in the document is one the paper is citing.

Usage:
    python pipeline/audit_doi_provenance.py
    python pipeline/audit_doi_provenance.py --json --out reports/build/doi.json
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "pipeline"
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"
PAPERS = ROOT / "docs" / "papers"

# How far into a document the front matter can reasonably reach. A DOI past
# this point, with none before it, is being cited rather than claimed.
FRONT_MATTER_CHARS = 6000

# Registrant prefixes, for the cases where the mismatch is flat rather than
# arguable: a machine-learning proceedings paper carrying an Oxford University
# Press DOI is not a borderline call.
REGISTRANTS = {
    "10.1093": "Oxford University Press",
    "10.1038": "Nature Portfolio",
    "10.1126": "Science / AAAS",
    "10.1016": "Elsevier",
    "10.1021": "American Chemical Society",
    "10.1073": "PNAS",
    "10.1145": "ACM",
    "10.1109": "IEEE",
    "10.1101": "Cold Spring Harbor",
    "10.48550": "arXiv",
}

_REFERENCE_SHAPE = re.compile(r"(?i)(?:\[\d+\]|\(\d{4}\)|\bdoi:\s*)\S{0,80}$")


def _words(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def evidence_for(text: str, doi: str) -> dict | None:
    """Where in the paper the DOI appears, and what surrounds it."""
    lowered, needle = text.lower(), doi.lower()
    positions, start = [], lowered.find(needle)
    while start >= 0:
        positions.append(start)
        start = lowered.find(needle, start + 1)
    if not positions:
        return None            # absent from the text; Zotero's word, untested
    first = positions[0]
    # A paper may print its own DOI in a footer or on a last page. If its own
    # title stands beside the DOI, the DOI is its own and the position means
    # nothing; 76 of 780 in this corpus are that case.
    return {
        "occurrences": len(positions),
        "first_ratio": round(first / max(1, len(text)), 3),
        "in_front_matter": first < FRONT_MATTER_CHARS,
        "looks_like_reference": bool(
            _REFERENCE_SHAPE.search(text[max(0, first - 90):first])),
        "context": " ".join(text[max(0, first - 150):first + 40].split()),
        "_around": _words(text[max(0, first - 600):first + 200]),
    }


def audit(db: Path) -> list[dict]:
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    try:
        rows = conn.execute(
            "SELECT paper_id, slug, title, COALESCE(doi,''),"
            " COALESCE(journal_name,''), COALESCE(publication_date,''),"
            " COALESCE(bibliography_source,''), COALESCE(zotero_item_key,'')"
            " FROM papers WHERE COALESCE(doi,'')<>'' ORDER BY paper_id"
        ).fetchall()
        findings = []
        for pid, slug, title, doi, journal, date, source, key in rows:
            path = PAPERS / slug / "text.md"
            if not path.exists():
                continue
            evidence = evidence_for(
                path.read_text(encoding="utf-8", errors="replace"), doi)
            if not evidence or evidence["in_front_matter"]:
                continue
            head = " ".join(_words(title).split()[:5])
            evidence["own_title_beside_doi"] = bool(
                head and head in evidence.pop("_around"))
            if evidence["own_title_beside_doi"]:
                continue
            findings.append({
                "zotero_item_key": key,
                "slug": slug, "title": title[:70], "doi": doi,
                "journal": journal[:60], "date": date,
                "bibliography_source": source,
                "registrant": REGISTRANTS.get(doi.split("/", 1)[0], ""),
                "deposit_links": conn.execute(
                    "SELECT COUNT(*) FROM paper_author_institutions"
                    " WHERE paper_id=? AND source IN ('openalex','scopus')",
                    (pid,)).fetchone()[0],
                **evidence,
            })
        return findings
    finally:
        conn.close()


def as_markdown(findings: list[dict]) -> str:
    """A list to work through in Zotero, worst first.

    Sorted by how many author links rest on the wrong DOI, because that is
    what a wrong DOI costs: the deposit lookup returns the cited paper's
    authors and they are written into this paper.
    """
    carried = sum(row["deposit_links"] for row in findings)
    lines = [
        "# DOI 검토 목록 — 참고문헌의 DOI 가 논문에 붙은 건",
        "",
        f"**{len(findings)}건**, 이 DOI 를 근거로 들어온 기탁 유래 저자 링크 "
        f"**{carried:,}개**.",
        "",
        "논문 자신의 DOI 는 앞부분에 인쇄되거나 Zotero 에서 오고 본문에 없다. "
        "본문 뒤쪽에만 나오고 그 옆에 자기 제목이 없으면, 그 DOI 는 이 논문이 "
        "**인용한** 것이다. 그 DOI 로 Scopus·OpenAlex 를 조회하면 남의 논문 "
        "저자와 소속이 이 논문에 기록된다.",
        "",
        "Zotero 에서 `item key` 로 찾아 DOI 필드를 비우거나 올바른 값으로 고친 뒤 "
        "`run_full --mode curate --source zotero` 를 돌리면 반영된다.",
        "",
        "|Zotero key|논문|현재 DOI|등록기관|본문 위치|기탁 링크|",
        "|---|---|---|---|---:|---:|",
    ]
    for row in findings:
        lines.append(
            f"|`{row['zotero_item_key'] or '-'}`"
            f"|{row['title'][:52]}"
            f"|`{row['doi']}`"
            f"|{row['registrant'] or '-'}"
            f"|{row['first_ratio'] * 100:.0f}%"
            f"|{row['deposit_links']}|")
    lines += ["", "## 문맥", ""]
    for row in findings[:80]:
        lines += [f"### {row['slug']}",
                  f"- 현재 DOI `{row['doi']}` · 우리 기록 저널 "
                  f"{row['journal'] or '-'} ({row['date'] or '-'})",
                  f"- 본문 {row['first_ratio'] * 100:.0f}% 지점: "
                  f"…{row['context']}…", ""]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--out", type=Path)
    ap.add_argument("--markdown", type=Path,
                    help="write a review list to fix in Zotero by hand")
    args = ap.parse_args()

    findings = audit(args.db)
    findings.sort(key=lambda row: (-row["deposit_links"], -row["first_ratio"]))

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(findings, ensure_ascii=False, indent=2),
                            encoding="utf-8")
    if args.markdown:
        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        args.markdown.write_text(as_markdown(findings), encoding="utf-8")
        print(f"검토 목록: {args.markdown}  ({len(findings)}건)")
    if args.json:
        print(json.dumps(findings, ensure_ascii=False, indent=2))
        return 0

    carried = sum(row["deposit_links"] for row in findings)
    print(f"DOI 가 본문 뒤쪽에만 나오는 논문 {len(findings)}건 "
          f"(기탁 유래 저자 링크 {carried}개가 이 DOI 를 근거로 한다)\n")
    for row in findings[:args.limit]:
        print(f"  {row['slug'][:56]}")
        print(f"      DOI {row['doi']}  ({row['registrant'] or '등록기관 미상'})")
        print(f"      저널 {row['journal'] or '-'} · {row['date'] or '-'}"
              f" · 출처 {row['bibliography_source']}")
        print(f"      본문 {row['first_ratio'] * 100:.0f}% 지점"
              f" · 참고문헌 형태 {'예' if row['looks_like_reference'] else '아니오'}"
              f" · 기탁 링크 {row['deposit_links']}")
        print(f"      {row['context'][:110]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
