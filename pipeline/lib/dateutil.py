"""날짜 문자열 정규화. build_papers_index.py, build_topic_index.py 등에서 공유."""

import os
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


# ── 벽시계 ───────────────────────────────────────────────────────────────

def machine_tz():
    """이 기계에 설정된 시간대. `TZ` 환경변수를 **무시**한다.

    `datetime.now()` 는 프로세스가 상속한 `TZ` 를 따른다. 그래서 에이전트
    하네스·cron·launchd·원격 SSH 처럼 TZ 가 다른 환경에서 파이프라인을 돌리면
    산출물 파일명이 엉뚱한 시각을 받는다. 실제로 리포트가 16시간 어긋난 이름으로
    저장돼 시간순 정렬이 깨졌다 (TZ=America/Los_Angeles 상속).

    운영자가 명시하려면 `PAPER_CURATION_TZ` 를 쓴다. 없으면 OS 설정을 읽는다.
    """
    from zoneinfo import ZoneInfo

    name = (os.environ.get("PAPER_CURATION_TZ") or "").strip()
    if not name:
        # macOS/Linux: /etc/localtime → .../zoneinfo/Asia/Seoul
        try:
            link = os.path.realpath("/etc/localtime")
            if "zoneinfo/" in link:
                name = link.split("zoneinfo/", 1)[1]
        except OSError:
            name = ""
    if name:
        try:
            return ZoneInfo(name)
        except Exception:  # noqa: BLE001 — 알 수 없는 이름이면 아래로
            pass
    return None  # 확인 불가 → 호출자가 기존 지역시각으로 폴백


def now_local():
    """기계 설정 시간대의 현재 시각. TZ 환경변수에 흔들리지 않는다."""
    from datetime import datetime

    tz = machine_tz()
    return datetime.now(tz) if tz else datetime.now()
