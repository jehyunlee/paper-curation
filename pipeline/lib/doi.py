"""One definition of what a DOI is, for every boundary that accepts one.

A DOI arrives in several shapes and only one of them is the identifier:

    10.18653/v1/2024.emnlp-main.70          Crossref, Zotero
    https://doi.org/10.18653/v1/2024...     OpenAlex, publisher pages
    doi:10.1038/s41586-026-10652-y          PDF front matter
    N/A · 미제공 · 미공개 · - · 논문          a review model writing "none"

Comparing the raw strings treats the first two as different works, which is
how one paper became two candidates in `candidate_works` and the
exactly-one-survivor rule then refused it. Accepting the fourth is worse: 177
papers carrying `doi: "N/A"` matched the single Zotero item whose DOI field
held that same string, and inherited its title, journal and pagination.

Normalising by *stripping* is the safe direction. Adding a prefix would not
merge `DOI:10.1038/x` with `doi:10.1038/x`, and would happily prefix `N/A`.
"""
from __future__ import annotations

import re

# 10. + a registrant (4-9 digits) + / + a suffix. Crossref's own recommended
# shape, and the reason "N/A" and "미제공" cannot pass for identifiers.
DOI_PATTERN = re.compile(r"^10\.\d{4,9}/\S+$")

_URL_PREFIX = re.compile(r"^https?://(?:dx\.)?doi\.org/", re.I)
_DOI_PREFIX = re.compile(r"^doi:\s*", re.I)
_ARXIV_FORMS = ("10.48550/arxiv.", "arxiv:")


def clean_doi(value: str) -> str:
    """The bare DOI, or "" when the input is not one.

    arXiv's DOI is dropped on purpose: it identifies the preprint, and every
    caller here is asking about the published work.
    """
    text = (value or "").strip()
    text = _URL_PREFIX.sub("", text)
    text = _DOI_PREFIX.sub("", text)
    text = text.rstrip(" .;,)")
    if text.lower().startswith(_ARXIV_FORMS):
        return ""
    return text if DOI_PATTERN.match(text) else ""


def clean_arxiv(value: str) -> str:
    """The bare arXiv id, without the scheme, host or `arXiv:` label."""
    text = (value or "").strip()
    text = re.sub(r"^arXiv:", "", text, flags=re.I)
    text = re.sub(r"^https?://arxiv\.org/(?:abs|pdf)/", "", text, flags=re.I)
    return text.rstrip(" .;,)")
