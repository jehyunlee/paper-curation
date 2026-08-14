"""Which evidence classes count as an answer, in one place.

The list lived in four modules and drifted: `pdf.shared-byline` was missing
from the report and from the attribution audit, so a recompute that moved 151
papers into that class read as a 2.7 point drop in coverage that had not
happened. A list copied four times is a list that will disagree with itself.

Order is the order the backfill tries them, which is the order of how directly
each source states who worked where.
"""
from __future__ import annotations

# Publisher deposits, then the byline parsers, then the page reader.
RESOLVED_SOURCES: tuple[str, ...] = (
    "openalex",
    "scopus",
    "llm.byline",
    "pdf.byline-marker",
    "pdf.stacked-byline",
    "pdf.inline-affiliation",
    "pdf.author-information",
    "pdf.shared-byline",
    "pdf.sole-author",
    "pdf.sole-affiliation",
)

# Read from the PDF rather than deposited by a publisher. Used where the two
# kinds are compared against each other.
PDF_SOURCES: tuple[str, ...] = tuple(
    s for s in RESOLVED_SOURCES if s not in ("openalex", "scopus"))

# Every author linked to every institution because the byline could not be
# read. Never counted as an answer; queries exclude it by name.
UNRESOLVED_SOURCE = "pdf.unmarked-multi"
