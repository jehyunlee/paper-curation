"""Who counts as the same author.

Identity was the lowercased display name, which split one person across rows
whenever a source spelled them differently: `Albert-László Barabási` and
`Albert-Laszlo Barabasi`, `Alán Aspuru‐Guzik` with U+2010 and `Alan
Aspuru-Guzik` with U+002D, `Matthew B.A. McDermott` and `Matthew B. A.
McDermott`. 132 groups, 134 surplus rows, and the effect is visible in the
rankings -- a field-leaders report printed `Pheng-Ann Heng(3)` next to
`Pheng‐Ann Heng(2)`, halving one researcher's output.

Two things this module refuses to do.

It does not strip characters it cannot read. An earlier fold used
`[^a-z0-9]`, which erases Cyrillic, CJK and Hangul entirely, so every
non-Latin name collapsed to the empty key and would have merged into a single
author. Folding removes combining marks and normalises punctuation; letters
survive whatever script they are in.

And it does not treat a shared ORCID as proof on its own. The identifier is
reliable; the act of attaching it to a name is done by OpenAlex or Scopus and
is not. Of 11 ORCIDs held by more than one row, 2 joined people who are
plainly different -- `Sungdong Kim` with `Sunkyu Kim`, `S. B. King` with
`Aditi T. Merchant` -- and in both cases OpenAlex itself had them under
different author ids. So an ORCID merges two rows only when the names can be
the same person; otherwise the attachment is the thing in doubt.
"""
from __future__ import annotations

import re
import unicodedata

# Hyphen-like characters publishers use interchangeably in the same name.
_HYPHENS = re.compile(r"[\u2010-\u2015\u2212\uFE58\uFE63\uFF0D]")
# "et al." and its Korean equivalent arrive inside the author string itself
# ("Tim Green 외 다수", "Renze Lou et al."), inventing an author who is really
# the tail of a list. Everything from the marker on is cut, not just a
# trailing match: one row read "Loubna Ben Allal 외 다수 (Hugging Face", where
# the marker sits mid-string and what follows it is debris.
_ET_AL = re.compile(
    r"(?i)[,;]?\s*(?:et\s*\.?\s*al\.?|외\s*다수|and others|외\s*\d+\s*명).*$")


def strip_et_al(name: str) -> str:
    """Cut a name off at the "and others" that was appended to it."""
    previous = None
    out = (name or "").strip()
    while out != previous:
        previous = out
        out = _ET_AL.sub("", out).strip().strip(",;")
    return out


def fold_author_name(name: str) -> str:
    """A comparison key that survives spelling, script and punctuation."""
    text = strip_et_al(name)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = _HYPHENS.sub("-", text)
    # Keep letters and digits of every script; punctuation becomes a space so
    # "B.A." and "B. A." agree.
    text = re.sub(r"[^\w\s-]", " ", text, flags=re.UNICODE)
    return re.sub(r"[\s-]+", " ", text.lower()).strip()


def name_tokens(name: str) -> list[str]:
    """Tokens in given-name-first order, undoing a "Surname, Given" listing."""
    raw = strip_et_al(name)
    if raw.count(",") == 1:
        surname, given = (part.strip() for part in raw.split(","))
        if surname and given:
            raw = f"{given} {surname}"
    return fold_author_name(raw).split()


def names_compatible(left: str, right: str) -> bool:
    """Whether two spellings can name one person.

    The surname must match. Every other token must either match or be the
    initial of its counterpart, which admits `James A. Evans` for `James
    Evans` and `P. Vischia` for `Vischia, Pietro`, and refuses `Sungdong Kim`
    for `Sunkyu Kim` -- same surname, two different given names, neither an
    abbreviation of the other.
    """
    a, b = name_tokens(left), name_tokens(right)
    if not a or not b:
        return False
    if a[-1] != b[-1]:
        return False
    rest_a, rest_b = a[:-1], b[:-1]
    if not rest_a or not rest_b:
        return True                      # one side gives only a surname
    for x, y in zip(rest_a, rest_b):
        if x == y:
            continue
        if len(x) == 1 and y.startswith(x):
            continue
        if len(y) == 1 and x.startswith(y):
            continue
        return False
    return True
