"""날짜 문자열 정규화. build_papers_index.py, build_topic_index.py 등에서 공유."""

import re

MONTH_MAP = {
    "january": "01", "february": "02", "march": "03", "april": "04",
    "may": "05", "june": "06", "july": "07", "august": "08",
    "september": "09", "october": "10", "november": "11", "december": "12",
    "jan": "01", "feb": "02", "mar": "03", "apr": "04",
    "jun": "06", "jul": "07", "aug": "08", "sep": "09",
    "oct": "10", "nov": "11", "dec": "12",
}


def normalize_date(ds):
    """Normalize any date string to YYYY.MM format."""
    if not ds:
        return ""
    ds = str(ds).strip()

    # Already YYYY.MM
    if re.match(r"^\d{4}\.\d{2}$", ds):
        return ds

    # YYYY-MM-DD or YYYY-MM-DDTHH:...
    m = re.match(r"^(\d{4})-(\d{2})", ds)
    if m:
        return f"{m.group(1)}.{m.group(2)}"

    # MM/YYYY or M/YYYY
    m = re.match(r"^(\d{1,2})/(\d{4})$", ds)
    if m:
        return f"{m.group(2)}.{int(m.group(1)):02d}"

    # YYYY/MM
    m = re.match(r"^(\d{4})/(\d{1,2})$", ds)
    if m:
        return f"{m.group(1)}.{int(m.group(2)):02d}"

    # "Month YYYY" or "Mon YYYY"
    m = re.match(r"^([A-Za-z]+)\s+(\d{4})$", ds)
    if m:
        mon = MONTH_MAP.get(m.group(1).lower(), "")
        if mon:
            return f"{m.group(2)}.{mon}"

    # "YYYY Month" or "YYYY Mon"
    m = re.match(r"^(\d{4})\s+([A-Za-z]+)$", ds)
    if m:
        mon = MONTH_MAP.get(m.group(2).lower(), "")
        if mon:
            return f"{m.group(1)}.{mon}"

    # YYYY only
    if re.match(r"^\d{4}$", ds):
        return ds

    # Fallback: try to extract any 4-digit year
    m = re.search(r"(\d{4})", ds)
    if m:
        return m.group(1)

    return ds
