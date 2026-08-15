"""Which evidence classes count as an answer, in one place.

The list lived in four modules and drifted: `pdf.shared-byline` was missing
from the report and from the attribution audit, so a recompute that moved 151
papers into that class read as a 2.7 point drop in coverage that had not
happened. A list copied four times is a list that will disagree with itself.

Order is execution order. The publisher deposits are read first, then the
eight byline parsers, and the page reader runs last -- not because it is the
weakest but because it is the only one that costs money and minutes. A 300
paper A/B (`experiment_ladder_order.py`) settled that: moving the reader above
the parsers resolves exactly the same papers, so its place in the ladder buys
depth, not reach, and depth is bought selectively by `--augment` instead.
"""
from __future__ import annotations

# Publisher deposits, then the byline parsers, then the page reader.
RESOLVED_SOURCES: tuple[str, ...] = (
    "openalex",
    "scopus",
    "pdf.byline-marker",
    "pdf.stacked-byline",
    "pdf.inline-affiliation",
    "pdf.author-information",
    "pdf.shared-byline",
    "pdf.sole-author",
    "pdf.sole-affiliation",
    "llm.byline",
)

# Read from the PDF rather than deposited by a publisher. Used where the two
# kinds are compared against each other.
PDF_SOURCES: tuple[str, ...] = tuple(
    s for s in RESOLVED_SOURCES if s not in ("openalex", "scopus"))

# Every author linked to every institution because the byline could not be
# read. Never counted as an answer; queries exclude it by name.
UNRESOLVED_SOURCE = "pdf.unmarked-multi"


def record_attempt(conn, paper_id: int, extractor: str, outcome: str,
                   links: int = 0, detail: str = "") -> None:
    """Write down that an extractor ran, whatever came of it.

    A table of successes cannot answer "has this been tried?", and for an
    extractor billed per page that answer decides whether to pay again. The row
    is replaced rather than appended: what matters is whether the paper, as it
    stands now, has been read.
    """
    from datetime import datetime, timezone
    conn.execute(
        "INSERT INTO extraction_attempts"
        " (paper_id, extractor, attempted_at, outcome, links, detail)"
        " VALUES (?,?,?,?,?,?)"
        " ON CONFLICT(paper_id, extractor) DO UPDATE SET"
        "  attempted_at=excluded.attempted_at, outcome=excluded.outcome,"
        "  links=excluded.links, detail=excluded.detail",
        (paper_id, extractor,
         datetime.now(timezone.utc).isoformat(timespec="seconds"),
         outcome, links, detail or ""))


def attempted(conn, extractor: str) -> set[int]:
    """Paper ids this extractor has already been run against."""
    try:
        return {row[0] for row in conn.execute(
            "SELECT paper_id FROM extraction_attempts WHERE extractor=?",
            (extractor,))}
    except Exception:      # table absent on a database not yet migrated
        return set()
