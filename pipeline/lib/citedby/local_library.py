"""내 Zotero 라이브러리(로컬)에서 인용논문을 찾아 정보를 끌어온다.

발상 — 인용논문 중 **내가 이미 갖고 있는 것**은 출판사 API 를 두드릴 이유가
없다. 정당하게 보유한 PDF 와 서지정보가 디스크에 있으니, 거기서 읽는 게 더
빠르고 더 풍부하고 ToS 문제도 없다. 폐쇄형 논문의 초록이 무료 API 에 없어도
내 PDF 에는 있다.

우선순위:
    1. 로컬 Zotero 초록 (abstractNote)   — 즉시, 네트워크 0
    2. 로컬 PDF 본문 앞부분              — 초록이 비었을 때
    3. 외부 API (S2 → Springer Nature)   — 내가 없는 논문만

paper-curation 은 지금까지 Zotero **Web API** 만 썼다. 여기서는 로컬
`zotero.sqlite` 를 **읽기 전용 복사본**으로 읽는다 — Zotero 가 실행 중이면 원본이
잠겨 있어 직접 열면 실패한다.

`docs/_zotero_keys.json`(코퍼스 4,031편) 과 달리 **라이브러리 전체**(7,187편,
PDF 5,864개)를 본다. 그래서 코퍼스 밖 인용논문도 매칭된다.
"""
from __future__ import annotations

import logging
import os
import re
import shutil
import sqlite3
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

logger = logging.getLogger(__name__)

DEFAULT_DB = Path.home() / "Zotero" / "zotero.sqlite"

# PDF 본문에서 읽을 앞부분 — 초록은 대개 1페이지에 있다. 전문을 읽으면 느리고
# 뒤쪽 참고문헌이 섞여 임베딩 품질이 오히려 떨어진다.
PDF_PAGES = 2
PDF_CHARS = 6000

_ATTACH_PREFIX = "attachments:"

_ITEM_QUERY = """
SELECT i.itemID, i.key, f.fieldName, dv.value
FROM items i
JOIN itemTypes t   ON i.itemTypeID = t.itemTypeID
JOIN itemData d    ON d.itemID = i.itemID
JOIN fields f      ON d.fieldID = f.fieldID
JOIN itemDataValues dv ON d.valueID = dv.valueID
WHERE t.typeName NOT IN ('attachment', 'note', 'annotation')
  AND f.fieldName IN ('DOI', 'title', 'abstractNote', 'url', 'extra', 'date')
"""

_ATTACH_QUERY = """
SELECT ia.parentItemID, ia.path, i.key
FROM itemAttachments ia
JOIN items i ON i.itemID = ia.itemID
WHERE ia.contentType = 'application/pdf'
  AND ia.parentItemID IS NOT NULL
  AND ia.path IS NOT NULL
"""

_DELETED_QUERY = "SELECT itemID FROM deletedItems"


def normalize_doi(raw) -> str:
    doi = str(raw or "").strip().lower()
    for pre in ("https://doi.org/", "http://doi.org/",
                "https://dx.doi.org/", "http://dx.doi.org/", "doi:"):
        if doi.startswith(pre):
            doi = doi[len(pre):]
    return doi.strip()


def normalize_title(raw) -> str:
    """비교용 제목 키 — 영숫자만 남기고 60자. 저장소의 title60 관례와 같다."""
    return re.sub(r"[^a-z0-9]", "", str(raw or "").lower())[:60]


def extract_arxiv(*values) -> str:
    """url/extra/DOI 어디에 있든 arXiv id 를 뽑는다.

    세 표기를 모두 받는다 — `.org` 를 빼먹으면 url 형태가 통째로 안 잡힌다:
        https://arxiv.org/abs/2409.04109   (url)
        arXiv:2501.12345                   (extra)
        10.48550/arXiv.2409.04109          (DOI)
    """
    for v in values:
        m = re.search(r"arxiv(?:\.org)?[.:/]*(?:abs/|pdf/)?(\d{4}\.\d{4,5})",
                      str(v or ""), re.IGNORECASE)
        if m:
            return m.group(1)
    return ""


@dataclass
class LibraryItem:
    key: str = ""
    title: str = ""
    doi: str = ""
    abstract: str = ""
    date: str = ""
    pdf_path: str = ""
    attachment_key: str = ""

    @property
    def has_pdf(self) -> bool:
        return bool(self.pdf_path)


@dataclass
class LibraryIndex:
    by_doi: dict = field(default_factory=dict)
    by_arxiv: dict = field(default_factory=dict)
    by_title: dict = field(default_factory=dict)
    items: int = 0
    with_pdf: int = 0

    def __bool__(self) -> bool:
        return bool(self.by_doi or self.by_arxiv or self.by_title)

    def lookup(self, paper: dict) -> LibraryItem | None:
        """DOI → arXiv → 제목 순으로 찾는다. 식별자가 강한 순."""
        doi = normalize_doi(paper.get("doi"))
        if doi and doi in self.by_doi:
            return self.by_doi[doi]
        arx = str(paper.get("arxiv_id") or "").strip() or extract_arxiv(
            paper.get("url"), paper.get("doi"))
        if arx and arx in self.by_arxiv:
            return self.by_arxiv[arx]
        title = normalize_title(paper.get("title"))
        if title and title in self.by_title:
            return self.by_title[title]
        return None


def _resolve_pdf(raw_path: str, pdf_dir: Path | None,
                 attachment_key: str) -> str:
    """Zotero 첨부 경로 표기를 실제 파일 경로로 푼다.

    `attachments:<name>` 은 Zotero 의 "Linked Attachment Base Directory" 기준
    상대경로다 — `find_pdf` 와 같은 규약을 따른다. `storage:<name>` 은 Zotero
    내부 저장소(`~/Zotero/storage/<attachmentKey>/<name>`).
    """
    raw = str(raw_path or "").strip()
    if not raw:
        return ""

    if raw.startswith(_ATTACH_PREFIX):
        name = raw[len(_ATTACH_PREFIX):]
        if pdf_dir:
            p = pdf_dir / name
            return str(p) if p.exists() else ""
        return ""

    if raw.startswith("storage:"):
        name = raw[len("storage:"):]
        p = Path.home() / "Zotero" / "storage" / attachment_key / name
        return str(p) if p.exists() else ""

    p = Path(raw)
    return str(p) if p.is_absolute() and p.exists() else ""


def load_library_index(db_path=None, pdf_dir=None) -> LibraryIndex:
    """로컬 Zotero DB 를 읽어 DOI/arXiv/제목 인덱스를 만든다.

    Zotero 가 실행 중이면 원본 DB 가 잠겨 있으므로 **임시 복사본**을 읽는다.
    어떤 실패도 예외를 던지지 않는다 — 로컬 보강은 부가 기능이라 없으면 그냥
    외부 API 경로로 돌아가면 된다.
    """
    db = Path(db_path or os.environ.get("ZOTERO_SQLITE") or DEFAULT_DB)
    if not db.exists():
        logger.info("로컬 Zotero DB 없음: %s", db)
        return LibraryIndex()

    if pdf_dir is None:
        pdf_dir = _config_pdf_dir()
    pdf_dir = Path(pdf_dir) if pdf_dir else None

    tmp = None
    try:
        # Zotero 실행 중 잠금 회피 — 복사본을 읽는다.
        fd, tmp = tempfile.mkstemp(suffix=".sqlite", prefix="zotero_ro_")
        os.close(fd)
        shutil.copy2(db, tmp)
        conn = sqlite3.connect(f"file:{tmp}?mode=ro", uri=True)
    except Exception as e:  # noqa: BLE001
        logger.warning("Zotero DB 열기 실패: %s", str(e)[:120])
        if tmp:
            Path(tmp).unlink(missing_ok=True)
        return LibraryIndex()

    try:
        deleted = {r[0] for r in conn.execute(_DELETED_QUERY)}

        fields: dict[int, dict] = {}
        for item_id, key, fname, value in conn.execute(_ITEM_QUERY):
            if item_id in deleted:
                continue
            rec = fields.setdefault(item_id, {"key": key})
            rec[fname] = value

        attachments: dict[int, tuple] = {}
        for parent_id, path, akey in conn.execute(_ATTACH_QUERY):
            if parent_id in deleted or parent_id in attachments:
                continue
            attachments[parent_id] = (path, akey)
    except Exception as e:  # noqa: BLE001
        logger.warning("Zotero DB 질의 실패: %s", str(e)[:120])
        return LibraryIndex()
    finally:
        try:
            conn.close()
        finally:
            if tmp:
                Path(tmp).unlink(missing_ok=True)

    idx = LibraryIndex()
    for item_id, rec in fields.items():
        raw_path, akey = attachments.get(item_id, ("", ""))
        item = LibraryItem(
            key=rec.get("key", ""),
            title=rec.get("title", "") or "",
            doi=normalize_doi(rec.get("DOI")),
            abstract=(rec.get("abstractNote") or "").strip(),
            date=rec.get("date", "") or "",
            pdf_path=_resolve_pdf(raw_path, pdf_dir, akey),
            attachment_key=akey,
        )
        idx.items += 1
        if item.has_pdf:
            idx.with_pdf += 1

        if item.doi:
            idx.by_doi.setdefault(item.doi, item)
        arx = extract_arxiv(rec.get("url"), rec.get("extra"), rec.get("DOI"))
        if arx:
            idx.by_arxiv.setdefault(arx, item)
        tkey = normalize_title(item.title)
        if tkey:
            idx.by_title.setdefault(tkey, item)

    logger.info("로컬 Zotero 인덱스: %d편 (PDF %d) · doi %d / arxiv %d / title %d",
                idx.items, idx.with_pdf, len(idx.by_doi), len(idx.by_arxiv),
                len(idx.by_title))
    return idx


def _config_pdf_dir():
    """config.json 의 zotero.pdf_dir."""
    try:
        import json
        cfg = Path(__file__).resolve().parents[3] / "config.json"
        if cfg.exists():
            data = json.loads(cfg.read_text(encoding="utf-8"))
            v = ((data.get("zotero") or {}).get("pdf_dir") or "").strip()
            return v or None
    except Exception:  # noqa: BLE001
        pass
    return None


def pdf_head_text(path: str, pages: int = PDF_PAGES,
                  max_chars: int = PDF_CHARS) -> str:
    """PDF 앞부분 텍스트. 실패하면 빈 문자열.

    전문이 아니라 앞 2페이지만 읽는다 — 초록은 거기 있고, 뒤쪽 참고문헌까지
    끌어오면 느린 데다 임베딩 품질이 떨어진다.
    """
    if not path or not os.path.exists(path):
        return ""
    try:
        import fitz  # PyMuPDF — 이미 파이프라인 의존성
    except ImportError:
        logger.debug("PyMuPDF 없음 — PDF 본문 추출 생략")
        return ""
    try:
        with fitz.open(path) as doc:
            out = []
            for i, page in enumerate(doc):
                if i >= pages:
                    break
                out.append(page.get_text())
            return re.sub(r"\s+", " ", " ".join(out)).strip()[:max_chars]
    except Exception as e:  # noqa: BLE001
        logger.debug("PDF 읽기 실패 %s: %s", path, str(e)[:80])
        return ""


def enrich_from_library(papers: list[dict], index: LibraryIndex | None = None,
                        *, read_pdf: bool = True,
                        progress=None) -> tuple[list[dict], dict]:
    """인용논문 중 내가 보유한 것을 로컬 정보로 채운다.

    각 논문에 표시를 남긴다:
        _in_library     bool   내 라이브러리에 있는가
        _has_pdf        bool   PDF 까지 보유하는가
        _library_key    str    Zotero item key (zotero://select 용)
        _library_attach str    첨부 key (zotero://open-pdf 용)
        _abstract_from  str    "zotero" | "pdf" | ""  (초록 출처)

    Returns:
        (papers, stats)
    """
    papers = [dict(p) for p in (papers or [])]
    stats = {"matched": 0, "with_pdf": 0,
             "abstract_from_zotero": 0, "abstract_from_pdf": 0}
    if index is None:
        index = load_library_index()
    if not index or not papers:
        return papers, stats

    for p in papers:
        hit = index.lookup(p)
        if not hit:
            p["_in_library"] = False
            continue

        p["_in_library"] = True
        p["_has_pdf"] = hit.has_pdf
        p["_library_key"] = hit.key
        p["_library_attach"] = hit.attachment_key
        stats["matched"] += 1
        if hit.has_pdf:
            stats["with_pdf"] += 1

        if len(str(p.get("abstract") or "").strip()) > 20:
            continue

        # 1순위: Zotero 서지의 초록 (네트워크 0)
        if len(hit.abstract) > 20:
            p["abstract"] = hit.abstract
            p["_abstract_from"] = "zotero"
            stats["abstract_from_zotero"] += 1
            continue

        # 2순위: 보유 PDF 본문 앞부분
        if read_pdf and hit.has_pdf:
            text = pdf_head_text(hit.pdf_path)
            if len(text) > 200:
                p["abstract"] = text
                p["_abstract_from"] = "pdf"
                stats["abstract_from_pdf"] += 1

    if progress:
        progress("library",
                 f"내 라이브러리 매칭 {stats['matched']}편 "
                 f"(PDF {stats['with_pdf']}) · 초록 보강 "
                 f"{stats['abstract_from_zotero'] + stats['abstract_from_pdf']}편")
    logger.info("로컬 보강: 매칭 %d편 (PDF %d) · 초록 zotero %d / pdf %d",
                stats["matched"], stats["with_pdf"],
                stats["abstract_from_zotero"], stats["abstract_from_pdf"])
    return papers, stats
