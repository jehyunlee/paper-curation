#!/usr/bin/env python3
"""Does the byline parser ladder still earn its place above the page reader?

    python pipeline/experiment_ladder_order.py --topic ai4s --sample 300
    python pipeline/experiment_ladder_order.py --sample 40 --seed 7

Two arms over the same random papers:

  A  the shipped order — publisher deposits, then eight PDF byline parsers,
     then `llm.byline` last, as a fallback for what nothing else could read
  B  `llm.byline` promoted above every PDF parser, which keep whatever it
     leaves behind

Both arms end at the same place: an affiliation string is only ever a claim
until `best_institution_for` matches it to one of the paper's own institution
rows, so this compares readers, not writers. Nothing is written to the
database — both arms are computed in memory and compared.

Reported per arm: papers resolved, author-institution links produced, which
class did the work, wall time, and the API cost of the pages actually read.
The question the numbers answer is narrow but real: if arm B resolves what arm
A does and the parsers below it contribute nothing, eight parsers are dead
weight; if the parsers still carry papers the reader misses, the ladder is
earning its complexity.
"""
from __future__ import annotations

import argparse
import json
import os
import random
import sqlite3
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "pipeline"
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import build_bibliography_db as bib            # noqa: E402
import extract_byline_llm as llm               # noqa: E402

PAPERS_DIR = ROOT / "docs" / "papers"
DEFAULT_DB = ROOT / ".cache" / "bibliography.sqlite3"

# Sonnet 4.5, USD per million tokens.
PRICE_IN, PRICE_OUT = 3.00, 15.00


def paper_context(conn: sqlite3.Connection, paper_id: int, slug: str) -> dict:
    text = PAPERS_DIR / slug / "text.md"
    authors = conn.execute(
        "SELECT a.author_id, a.display_name, pa.author_order FROM paper_authors"
        " pa JOIN authors a USING(author_id) WHERE pa.paper_id=?"
        " ORDER BY pa.author_order", (paper_id,)).fetchall()
    institutions = conn.execute(
        "SELECT institution_id, raw_name FROM paper_institutions"
        " WHERE paper_id=?", (paper_id,)).fetchall()
    names = dict(conn.execute(
        "SELECT pi.institution_id, i.institution_name FROM paper_institutions"
        " pi JOIN institutions i USING(institution_id) WHERE pi.paper_id=?",
        (paper_id,)))
    return {"text": text, "authors": authors, "institutions": institutions,
            "names": names,
            "header": bib.extract_header(text)[0] if text.exists() else ""}


def ground(value: str, ctx: dict) -> int | None:
    """An affiliation string turned into one of this paper's institution rows."""
    institution_id = bib.best_institution_for(value, ctx["institutions"])
    if institution_id is None and "@" in value:
        institution_id = bib.institution_for_email(value, ctx["institutions"])
    if institution_id is None:
        return None
    if bib.assignment_disagrees(value, ctx["names"].get(institution_id, "")):
        return None
    return institution_id


def parser_links(ctx: dict) -> tuple[dict, str]:
    """What the PDF parsers make of this paper, and which one did it.

    The same order and the same rules the backfill uses, minus the writing.
    """
    text, header = ctx["text"], ctx["header"]
    authors = ctx["authors"]
    names = [name for _, name, _ in authors]
    if not (header and authors and ctx["institutions"]):
        return {}, ""

    markers, alphabet = bib.read_byline_markers(header, names, text)
    if markers:
        wanted = {m for values in markers.values() for m in values}
        block = (bib.marker_affiliations(header, wanted, alphabet)
                 or bib.marker_affiliations(
                     bib.affiliation_window(text), wanted, alphabet)
                 or bib.marker_affiliations(
                     bib.author_information_text(text), wanted, alphabet)
                 or bib.trailing_marker_affiliations(
                     bib.affiliation_window(text), wanted))
        by_marker = {}
        for marker, label in block.items():
            institution_id = ground(label, ctx)
            if institution_id is not None:
                by_marker[marker] = institution_id
        found = defaultdict(set)
        for author_id, name, _ in authors:
            for marker in markers.get(name, []):
                if marker in by_marker:
                    found[author_id].add(by_marker[marker])
        if found:
            return dict(found), "pdf.byline-marker"

    for label, parser in (("pdf.stacked-byline", bib.stacked_author_affiliations),
                          ("pdf.inline-affiliation", bib.inline_author_affiliations)):
        mapping = parser(header, names)
        found = defaultdict(set)
        for author_id, name, _ in authors:
            value = mapping.get(name)
            if value:
                institution_id = ground(value, ctx)
                if institution_id is not None:
                    found[author_id].add(institution_id)
        if found:
            return dict(found), label

    named = bib.author_information_pairs(
        bib.author_information_text(text), names)
    found = defaultdict(set)
    for author_id, name, _ in authors:
        value = named.get(name)
        if value:
            institution_id = ground(value, ctx)
            if institution_id is not None:
                found[author_id].add(institution_id)
    if found:
        return dict(found), "pdf.author-information"

    shared = bib.shared_affiliation_block(header, names)
    matched = [i for line in shared for i in [ground(line, ctx)] if i is not None]
    if matched:
        return ({author_id: set(matched) for author_id, _, _ in authors},
                "pdf.shared-byline")
    if len(ctx["institutions"]) == 1:
        only = {ctx["institutions"][0][0]}
        return ({author_id: set(only) for author_id, _, _ in authors},
                "pdf.sole-affiliation")
    if len(authors) == 1:
        every = {i for i, _ in ctx["institutions"]}
        return ({authors[0][0]: every}, "pdf.sole-author")
    return {}, ""


def llm_links(client, ctx: dict, budget: dict) -> dict:
    """What the rendered first page gives, grounded the same way."""
    pdf_path = budget.pop("_pdf", None)
    png = llm.first_page_png(pdf_path) if pdf_path else None
    if not png:
        return {}
    started = time.time()
    try:
        response = client.messages.create(
            model=llm.MODEL, max_tokens=2000,
            messages=[{"role": "user", "content": [
                {"type": "image", "source": {
                    "type": "base64", "media_type": "image/png",
                    "data": __import__("base64").b64encode(png).decode()}},
                {"type": "text", "text": llm.PROMPT}]}])
    except Exception:
        budget["failures"] += 1
        return {}
    budget["seconds"] += time.time() - started
    budget["calls"] += 1
    budget["in_tokens"] += response.usage.input_tokens
    budget["out_tokens"] += response.usage.output_tokens
    # A refusal or a stop with no text block comes back with empty content.
    if not response.content:
        budget["failures"] += 1
        return {}
    body = response.content[0].text.strip()
    start, end = body.find("{"), body.rfind("}")
    if start < 0 or end < start:
        return {}
    try:
        byline = json.loads(body[start:end + 1]).get("authors") or []
    except json.JSONDecodeError:
        return {}

    surnames = {}
    for author_id, name, _ in ctx["authors"]:
        parts = [p for p in str(name).split() if p]
        if parts:
            surnames.setdefault(bib._fold(parts[-1]), author_id)
    found = defaultdict(set)
    for entry in byline:
        parts = [p for p in str(entry.get("name") or "").split() if p]
        if not parts:
            continue
        author_id = surnames.get(bib._fold(parts[-1]))
        if author_id is None:
            continue
        for value in entry.get("affiliations") or []:
            institution_id = ground(str(value), ctx)
            if institution_id is not None:
                found[author_id].add(institution_id)
    return dict(found)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--topic", default="ai4s")
    ap.add_argument("--sample", type=int, default=300)
    ap.add_argument("--seed", type=int, default=20260814)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ANTHROPIC_API_KEY 가 없다", file=sys.stderr)
        return 2

    import anthropic
    client = anthropic.Anthropic(timeout=180.0, max_retries=4)
    conn = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True)
    rows = conn.execute(
        "SELECT DISTINCT p.paper_id, p.slug,"
        " json_extract(p.metadata_json,'$.pdf_path') FROM papers p"
        " JOIN json_each(json_extract(p.metadata_json,'$.topics')) t"
        " WHERE t.value=? ORDER BY p.paper_id", (args.topic,)).fetchall()
    rows = [r for r in rows
            if r[2] and Path(r[2]).exists()
            and (PAPERS_DIR / r[1] / "text.md").exists()]
    random.Random(args.seed).shuffle(rows)
    rows = rows[:args.sample]

    budget = {"calls": 0, "in_tokens": 0, "out_tokens": 0, "seconds": 0.0,
              "failures": 0}
    arm_a = {"resolved": 0, "links": 0, "by_class": Counter(), "seconds": 0.0}
    arm_b = {"resolved": 0, "links": 0, "by_class": Counter(), "seconds": 0.0}
    both, only_a, only_b, neither, disagree = 0, 0, 0, 0, 0
    supported, unsupported = Counter(), Counter()

    for index, (paper_id, slug, pdf_path) in enumerate(rows, 1):
        ctx = paper_context(conn, paper_id, slug)

        started = time.time()
        parsed, parser_class = parser_links(ctx)
        parser_seconds = time.time() - started

        budget["_pdf"] = Path(pdf_path)
        read = llm_links(client, ctx, budget)

        # Arm A: parsers first, the reader only for what they left.
        a_links, a_class = (parsed, parser_class) if parsed else (read, "llm.byline")
        arm_a["seconds"] += parser_seconds
        # Arm B: the reader first, the parsers keep the remainder.
        b_links, b_class = (read, "llm.byline") if read else (parsed, parser_class)
        if not read:
            arm_b["seconds"] += parser_seconds

        for arm, links, klass in ((arm_a, a_links, a_class),
                                  (arm_b, b_links, b_class)):
            if links:
                arm["resolved"] += 1
                arm["links"] += sum(len(v) for v in links.values())
                arm["by_class"][klass] += 1

        if a_links and b_links:
            both += 1
            keys = set(a_links) | set(b_links)
            if any(a_links.get(k) != b_links.get(k) for k in keys):
                disagree += 1
                # Which side the page itself supports. Only the extra links
                # are judged: a reader that finds three authors where the
                # parser found one is not disagreeing, it is reading further.
                window = bib._fold(bib.affiliation_window(ctx["text"]))
                for key in keys:
                    for side, links in (("a", a_links), ("b", b_links)):
                        extra = (links.get(key) or set()) - (
                            (b_links if side == "a" else a_links).get(key)
                            or set())
                        for institution_id in extra:
                            name = ctx["names"].get(institution_id, "")
                            tokens = [x for x in bib._affiliation_tokens(name)
                                      if len(x) >= 5][:3]
                            if tokens and all(x in window for x in tokens):
                                supported[side] += 1
                            elif tokens:
                                unsupported[side] += 1
        elif a_links:
            only_a += 1
        elif b_links:
            only_b += 1
        else:
            neither += 1
        if index % 25 == 0:
            print(f"  [exp] {index}/{len(rows)}", file=sys.stderr, flush=True)

    conn.close()
    cost = (budget["in_tokens"] / 1e6 * PRICE_IN
            + budget["out_tokens"] / 1e6 * PRICE_OUT)
    report = {
        "topic": args.topic, "papers": len(rows), "seed": args.seed,
        "arm_a_parsers_first": {
            "resolved": arm_a["resolved"], "links": arm_a["links"],
            "by_class": dict(arm_a["by_class"]),
            "parser_seconds": round(arm_a["seconds"], 1)},
        "arm_b_reader_first": {
            "resolved": arm_b["resolved"], "links": arm_b["links"],
            "by_class": dict(arm_b["by_class"]),
            "parser_seconds": round(arm_b["seconds"], 1)},
        "extra_links_supported_by_page": {
            "parsers": supported["a"], "reader": supported["b"]},
        "extra_links_not_in_page": {
            "parsers": unsupported["a"], "reader": unsupported["b"]},
        "overlap": {"both": both, "only_parsers": only_a,
                    "only_reader": only_b, "neither": neither,
                    "differing_links": disagree},
        "llm": {"calls": budget["calls"], "failures": budget["failures"],
                "seconds": round(budget["seconds"], 1),
                "input_tokens": budget["in_tokens"],
                "output_tokens": budget["out_tokens"],
                "usd": round(cost, 2),
                "usd_per_1000_papers": round(
                    cost / max(1, budget["calls"]) * 1000, 2)},
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2),
                            encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
