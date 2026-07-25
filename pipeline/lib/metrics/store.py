"""citations.md / references.md 읽기·쓰기.

**단일 진실은 frontmatter 다.** 아래 마크다운 표는 거기서 렌더링된 뷰이고,
갱신할 때 표를 역파싱하지 않는다 — 표 파싱은 깨지기 쉽고, 저장소 전체가 이미
YAML frontmatter 규약을 쓴다(review.md 와 동일).

섹션마다 갱신 방식이 다르다:

    history / 추이 표      **append** — 매달 한 줄, 과거는 불변
    latest                 덮어쓰기 (최신 스냅샷)
    인용 논문 목록          덮어쓰기 (현재 상태)

이력을 쌓는 게 이 설계의 핵심이다. 최신값만 남기면 매달 이전 데이터를 버리는
셈이고, 쌓아 두면 **인용 속도**가 공짜로 생긴다.
"""
from __future__ import annotations

import datetime
import logging
from dataclasses import dataclass, field
from pathlib import Path

import yaml

logger = logging.getLogger(__name__)

CITATIONS_FILE = "citations.md"
REFERENCES_FILE = "references.md"
SCHEMA_CITATIONS = "citations-v1"
SCHEMA_REFERENCES = "references-v1"

DEFAULT_REFRESH_DAYS = 30

_SOURCES = ("openalex", "crossref", "scopus")


@dataclass
class CitationSnapshot:
    """한 시점의 피인용수 관측."""
    date: str
    openalex: int | None = None
    crossref: int | None = None
    scopus: int | None = None
    percentile: float | None = None

    def best(self) -> tuple[int | None, str]:
        """대표값과 그 출처. OpenAlex 우선 — 커버리지 최대 + 백분위 제공.

        **0 은 결측이 아니다.** 최근 논문의 0 은 정상값이라 그대로 존중한다.
        """
        for src in ("openalex", "crossref", "scopus"):
            v = getattr(self, src)
            if v is not None:
                return int(v), src
        return None, ""

    def to_dict(self) -> dict:
        d = {"date": self.date}
        for s in _SOURCES:
            d[s] = getattr(self, s)
        d["percentile"] = self.percentile
        return d

    @classmethod
    def from_dict(cls, d: dict) -> CitationSnapshot:
        return cls(
            date=str(d.get("date") or ""),
            openalex=_int_or_none(d.get("openalex")),
            crossref=_int_or_none(d.get("crossref")),
            scopus=_int_or_none(d.get("scopus")),
            percentile=_float_or_none(d.get("percentile")),
        )


@dataclass
class CitationsDoc:
    """citations.md 의 파싱 결과."""
    slug: str = ""
    doi: str = ""
    title: str = ""
    updated: str = ""
    history: list[CitationSnapshot] = field(default_factory=list)
    citing_count: int = 0
    citing_fetched: str = ""

    def latest(self) -> CitationSnapshot | None:
        return self.history[-1] if self.history else None


def _int_or_none(v):
    if v is None or v == "":
        return None
    try:
        return int(v)
    except (TypeError, ValueError):
        return None


def _float_or_none(v):
    if v is None or v == "":
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _today() -> str:
    return datetime.date.today().isoformat()


def split_frontmatter(text: str) -> tuple[dict, str]:
    """`---` 로 감싼 YAML frontmatter 와 본문을 분리."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    raw = text[3:end]
    body = text[end + 4:].lstrip("\n")
    try:
        meta = yaml.safe_load(raw) or {}
    except yaml.YAMLError as e:
        logger.warning("frontmatter 파싱 실패: %s", str(e)[:120])
        return {}, text
    return (meta if isinstance(meta, dict) else {}), body


# ── 읽기 ──────────────────────────────────────────────────────────────────

def read_citations(paper_dir) -> CitationsDoc:
    """citations.md 를 읽는다. 없거나 깨졌으면 빈 문서를 돌려준다.

    깨진 파일 때문에 갱신 자체가 막히면 안 되므로 절대 예외를 던지지 않는다.
    """
    path = Path(paper_dir) / CITATIONS_FILE
    if not path.exists():
        return CitationsDoc()
    try:
        meta, _ = split_frontmatter(path.read_text(encoding="utf-8"))
    except OSError as e:
        logger.warning("citations.md 읽기 실패 %s: %s", path, e)
        return CitationsDoc()

    hist = [CitationSnapshot.from_dict(h)
            for h in (meta.get("history") or []) if isinstance(h, dict)]
    hist.sort(key=lambda s: s.date)
    citing = meta.get("citing_papers") or {}
    return CitationsDoc(
        slug=str(meta.get("slug") or ""),
        doi=str(meta.get("doi") or ""),
        title=str(meta.get("title") or ""),
        updated=str(meta.get("updated") or ""),
        history=hist,
        citing_count=_int_or_none(citing.get("count")) or 0,
        citing_fetched=str(citing.get("fetched") or ""),
    )


def needs_refresh(paper_dir, *, days: int = DEFAULT_REFRESH_DAYS,
                  today: str | None = None) -> bool:
    """마지막 갱신이 `days` 일보다 오래됐으면 True. 파일이 없어도 True."""
    doc = read_citations(paper_dir)
    if not doc.updated:
        return True
    try:
        last = datetime.date.fromisoformat(doc.updated)
    except ValueError:
        return True
    now = (datetime.date.fromisoformat(today) if today
           else datetime.date.today())
    return (now - last).days >= days


# ── 쓰기 ──────────────────────────────────────────────────────────────────

def _fmt_pct(pct: float | None) -> str:
    """연차보정 백분위 → '상위 0.1%'. OpenAlex 값은 0~1 (클수록 상위)."""
    if pct is None:
        return "—"
    top = (1.0 - float(pct)) * 100.0
    return f"상위 {top:.1f}%" if top >= 0.05 else "상위 0.1% 미만"


def _fmt_int(v) -> str:
    return "—" if v is None else f"{int(v):,}"


def _history_table(history: list[CitationSnapshot]) -> str:
    lines = ["| 조회일 | 대표값 | OpenAlex | Crossref | Scopus | 연차보정 |",
             "|---|---|---|---|---|---|"]
    for s in history:
        best, src = s.best()
        best_txt = "—" if best is None else f"{best:,} ({src})"
        lines.append(
            f"| {s.date} | {best_txt} | {_fmt_int(s.openalex)} | "
            f"{_fmt_int(s.crossref)} | {_fmt_int(s.scopus)} | "
            f"{_fmt_pct(s.percentile)} |")
    return "\n".join(lines)


def _velocity_note(history: list[CitationSnapshot]) -> str:
    """이력이 2회 이상이면 증가폭을 적는다 — 이력을 쌓는 이유."""
    if len(history) < 2:
        return ""
    prev_v, _ = history[-2].best()
    curr_v, _ = history[-1].best()
    if prev_v is None or curr_v is None:
        return ""
    try:
        d0 = datetime.date.fromisoformat(history[-2].date)
        d1 = datetime.date.fromisoformat(history[-1].date)
        days = max(1, (d1 - d0).days)
    except ValueError:
        return ""
    delta = curr_v - prev_v
    per_month = delta * 30.0 / days
    sign = "+" if delta >= 0 else ""
    return (f"\n> 직전 관측 대비 **{sign}{delta:,}회** "
            f"({days}일, 월 환산 {sign}{per_month:.1f}회)\n")


def _citing_table(citing: list[dict]) -> str:
    lines = ["| # | 연도 | 피인용 | 제목 | DOI |", "|---|---|---|---|---|"]
    for i, p in enumerate(citing, 1):
        title = (p.get("title") or "").replace("|", "\\|")
        doi = p.get("doi") or ""
        doi_cell = f"[{doi}](https://doi.org/{doi})" if doi else "—"
        lines.append(f"| {i} | {p.get('year') or '—'} | "
                     f"{p.get('cited_by_count') or 0} | {title} | {doi_cell} |")
    return "\n".join(lines)


def write_citations(paper_dir, *, slug: str, doi: str, title: str,
                    snapshot: CitationSnapshot,
                    citing: list[dict] | None = None,
                    citing_fetched: bool = False,
                    min_citations: int = 10) -> Path:
    """citations.md 를 쓴다. 이력은 **append**, 나머지는 덮어쓴다.

    같은 날짜로 두 번 돌리면 그 날 관측을 교체한다 (중복 행 방지).
    """
    paper_dir = Path(paper_dir)
    doc = read_citations(paper_dir)

    history = [s for s in doc.history if s.date != snapshot.date]
    history.append(snapshot)
    history.sort(key=lambda s: s.date)

    best, best_src = snapshot.best()
    # citing 을 이번에 안 받았으면 이전 기록을 보존한다.
    citing_count = len(citing) if citing_fetched else doc.citing_count
    fetched_at = _today() if citing_fetched else doc.citing_fetched

    meta = {
        "schema": SCHEMA_CITATIONS,
        "slug": slug,
        "doi": doi,
        "title": title,
        "updated": snapshot.date,
        "latest": {
            "count": best,
            "source": best_src,
            "percentile": snapshot.percentile,
            "by_source": {s: getattr(snapshot, s) for s in _SOURCES},
        },
        "history": [s.to_dict() for s in history],
        "citing_papers": {
            "threshold": min_citations,
            "fetched": fetched_at,
            "count": citing_count,
        },
    }

    parts = [
        "---",
        yaml.safe_dump(meta, allow_unicode=True, sort_keys=False).rstrip(),
        "---",
        "",
        f"# Citations — {title or slug}",
        "",
        "## 피인용 추이",
        "",
        _history_table(history),
        "",
        "> 대표값은 OpenAlex 우선. 소스마다 세는 범위가 달라 병합하지 않는다 "
        "(Scopus 는 Scopus 색인만, OpenAlex 는 자기 그래프만 센다).",
    ]
    note = _velocity_note(history)
    if note:
        parts.append(note.rstrip())

    parts.append("")
    if citing_fetched and citing:
        parts += [f"## 이 논문을 인용한 논문 ({len(citing):,}건)", "",
                  _citing_table(citing), ""]
    elif best is not None and best < min_citations:
        parts += [f"## 이 논문을 인용한 논문", "",
                  f"피인용 {best}회로 임계값({min_citations}회) 미만이라 "
                  f"목록을 받지 않았다.", ""]

    path = paper_dir / CITATIONS_FILE
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    return path


def _reference_line(r: dict) -> str:
    """운영자 지정 형식 — DOI 1순위, URL 2순위, 둘 다 없을 때만 서지."""
    n = r.get("n") or 0
    doi = (r.get("doi") or "").strip()
    if doi:
        return f"{n}. [{doi}](https://doi.org/{doi})"
    url = (r.get("url") or "").strip()
    if url:
        return f"{n}. <{url}>"

    bits = []
    if r.get("first_author"):
        bits.append(str(r["first_author"]))
    if r.get("year"):
        bits.append(f"({r['year']})")
    if r.get("title"):
        bits.append(str(r["title"]))
    if r.get("venue"):
        bits.append(f"*{r['venue']}*")
    if bits:
        return f"{n}. " + ". ".join(bits)
    raw = (r.get("raw") or "").strip()
    return f"{n}. {raw}" if raw else f"{n}. (서지정보 없음)"


def write_references(paper_dir, *, slug: str, doi: str, title: str,
                     references: list[dict], source: str = "crossref") -> Path:
    """references.md 를 쓴다 (전량 덮어쓰기 — 레퍼런스는 변하지 않는다)."""
    paper_dir = Path(paper_dir)
    refs = list(references or [])
    with_doi = sum(1 for r in refs if (r.get("doi") or "").strip())
    with_url = sum(1 for r in refs
                   if not (r.get("doi") or "").strip() and (r.get("url") or "").strip())

    meta = {
        "schema": SCHEMA_REFERENCES,
        "slug": slug,
        "doi": doi,
        "title": title,
        "updated": _today(),
        "source": source,
        "count": len(refs),
        "with_doi": with_doi,
        "with_url": with_url,
    }
    pct = f"{with_doi * 100 // len(refs)}%" if refs else "—"
    parts = [
        "---",
        yaml.safe_dump(meta, allow_unicode=True, sort_keys=False).rstrip(),
        "---",
        "",
        f"# References — {title or slug}",
        "",
        f"총 {len(refs):,}건 · DOI {with_doi:,} ({pct}) · URL {with_url:,} · "
        f"출처: {source} · {meta['updated']}",
        "",
    ]
    parts += [_reference_line(r) for r in refs] or ["(레퍼런스 없음)"]

    path = paper_dir / REFERENCES_FILE
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    return path
