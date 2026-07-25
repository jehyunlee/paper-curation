"""인용논문 → 내 Zotero 라이브러리 링크 해석.

citedby 리포트는 정적 HTML 문서다. 거기서 논문 제목을 클릭했을 때 **내 Zotero에
그 논문이 있으면 PDF(없으면 서지정보)를 바로 열어주는** 링크를 만드는 게 이
모듈의 일이다. 라이브러리에 없으면 호출부가 외부 DOI 링크로 폴백한다.

해석 경로 (저장소에 이미 있는 두 파일을 slug 로 조인):

    docs/_zotero_keys.json    slug → **첨부(PDF) 키**      (4,031건)
    docs/papers/_papers_index.json
                              slug ↔ doi / title          (4,048건)

    ⇒ doi → 첨부키,  정규화제목 → 첨부키

`_papers_index.json` 에도 `zotero_item_key` 필드가 있지만 커버리지가 121/4,048
로 낮아 쓰지 않는다. `_zotero_keys.json` 이 압도적으로 조밀하다.

프로토콜 (Zotero 데스크톱이 처리):
    zotero://open-pdf/library/items/<attachmentKey>   PDF 바로 열기
    zotero://select/library/items/<itemKey>           항목(서지정보) 선택

`_zotero_keys.json` 은 gitignore + .assetsignore 대상이라 **로컬 전용**이다.
파일이 없으면 이 모듈은 조용히 빈 인덱스를 돌려주고, 리포트는 외부 링크만 쓴다.
"""
from __future__ import annotations

import json
import logging
import re
from pathlib import Path

logger = logging.getLogger(__name__)

ZOTERO_PDF_PREFIX = "zotero://open-pdf/library/items/"
ZOTERO_SELECT_PREFIX = "zotero://select/library/items/"

# 제목 정규화 폭 — 저장소의 title60 dedup 관례와 맞춘다.
_TITLE_KEY_LEN = 60


def normalize_doi_key(doi: str) -> str:
    """DOI 비교용 키. URL 접두사 제거 + 소문자."""
    s = (doi or "").strip().lower()
    if not s or s in ("nan", "none"):
        return ""
    for prefix in ("https://doi.org/", "http://doi.org/",
                   "https://dx.doi.org/", "http://dx.doi.org/"):
        if s.startswith(prefix):
            s = s[len(prefix):]
            break
    return s.strip()


def normalize_title_key(title: str) -> str:
    """제목 비교용 키. 영숫자만 남기고 소문자 + 앞 60자.

    출처마다 구두점·공백·대소문자가 달라 그대로는 매칭되지 않는다.
    """
    s = (title or "").strip().lower()
    if not s or s == "nan":
        return ""
    s = re.sub(r"[^a-z0-9]+", "", s)
    return s[:_TITLE_KEY_LEN]


class ZoteroIndex:
    """doi / 정규화제목 → Zotero 링크 조회기.

    두 종류의 키를 구분해 담는다:

        첨부(attachment) 키 → ``zotero://open-pdf``  PDF 를 바로 연다
        항목(item) 키       → ``zotero://select``    서지정보를 띄운다

    PDF 첨부가 있으면 PDF 를, 없으면 서지정보를 여는 게 요구사항이라
    `url()` 이 첨부 → 항목 순으로 폴백한다.

    비어 있어도(파일 없음) 정상 동작한다 — `url()` 이 항상 빈 문자열을 준다.
    """

    def __init__(self, by_doi: dict | None = None, by_title: dict | None = None,
                 item_by_doi: dict | None = None,
                 item_by_title: dict | None = None):
        self.by_doi = by_doi or {}                  # → 첨부 키
        self.by_title = by_title or {}              # → 첨부 키
        self.item_by_doi = item_by_doi or {}        # → 항목 키
        self.item_by_title = item_by_title or {}    # → 항목 키

    def __bool__(self) -> bool:
        return bool(self.by_doi or self.by_title
                    or self.item_by_doi or self.item_by_title)

    def __len__(self) -> int:
        return len(self.by_doi) + len(self.by_title)

    @staticmethod
    def _get(paper: dict, by_doi: dict, by_title: dict) -> str:
        """DOI 우선, 제목 차선 조회."""
        key = by_doi.get(normalize_doi_key(paper.get("doi", "")))
        if key:
            return key
        return by_title.get(normalize_title_key(paper.get("title", "")), "")

    def lookup(self, paper: dict) -> str:
        """PDF 첨부 키. 없으면 빈 문자열."""
        return self._get(paper, self.by_doi, self.by_title)

    def lookup_item(self, paper: dict) -> str:
        """항목(서지정보) 키. 없으면 빈 문자열."""
        return self._get(paper, self.item_by_doi, self.item_by_title)

    def url(self, paper: dict) -> str:
        """Zotero 열기 URL. **PDF 우선, 없으면 서지정보**, 둘 다 없으면 빈 문자열."""
        key = self.lookup(paper)
        if key:
            return f"{ZOTERO_PDF_PREFIX}{key}"
        item_key = self.lookup_item(paper)
        if item_key:
            return f"{ZOTERO_SELECT_PREFIX}{item_key}"
        return ""

    def url_kind(self, paper: dict) -> str:
        """`url()` 이 어떤 종류를 돌려주는지 — "pdf" | "item" | ""."""
        if self.lookup(paper):
            return "pdf"
        return "item" if self.lookup_item(paper) else ""


_EMPTY = ZoteroIndex()


def load_zotero_index(docs_dir=None) -> ZoteroIndex:
    """`_zotero_keys.json` + `_papers_index.json` 을 조인해 인덱스를 만든다.

    Args:
        docs_dir: docs/ 경로. 기본은 저장소 루트의 docs/.

    Returns:
        ZoteroIndex. 파일이 없거나 깨졌으면 빈 인덱스 (예외를 던지지 않는다 —
        Zotero 링크는 부가 기능이고, 없으면 외부 DOI 링크로 폴백하면 된다).
    """
    docs = Path(docs_dir) if docs_dir else \
        Path(__file__).resolve().parents[3] / "docs"

    keys_path = docs / "_zotero_keys.json"
    index_path = docs / "papers" / "_papers_index.json"
    if not keys_path.exists() or not index_path.exists():
        logger.debug("Zotero 인덱스 없음 (%s / %s)", keys_path, index_path)
        return _EMPTY

    try:
        slug_to_key = json.loads(keys_path.read_text(encoding="utf-8"))
        raw = json.loads(index_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        logger.warning("Zotero 인덱스 로드 실패: %s", e)
        return _EMPTY

    if not isinstance(slug_to_key, dict):
        return _EMPTY

    entries = raw if isinstance(raw, list) else (raw.get("papers") or [])
    by_doi: dict[str, str] = {}
    by_title: dict[str, str] = {}
    item_by_doi: dict[str, str] = {}
    item_by_title: dict[str, str] = {}

    for entry in entries:
        if not isinstance(entry, dict):
            continue
        doi_key = normalize_doi_key(entry.get("doi", ""))
        title_key = normalize_title_key(entry.get("title", ""))
        if not (doi_key or title_key):
            continue

        # 1순위: 첨부(PDF) 키 — zotero://open-pdf 로 PDF 를 바로 연다.
        attach_key = slug_to_key.get(entry.get("slug", ""))
        if attach_key:
            if doi_key:
                by_doi.setdefault(doi_key, attach_key)
            if title_key:
                by_title.setdefault(title_key, attach_key)

        # 2순위: 항목 키 — PDF 첨부가 없을 때 zotero://select 로 서지정보를
        # 띄운다. `_papers_index.json` 의 커버리지가 낮아(121/4,048) 보조용.
        item_key = (entry.get("zotero_item_key") or "").strip()
        if item_key:
            if doi_key:
                item_by_doi.setdefault(doi_key, item_key)
            if title_key:
                item_by_title.setdefault(title_key, item_key)

    logger.info("Zotero 인덱스: PDF(doi %d/title %d), 서지(doi %d/title %d)",
                len(by_doi), len(by_title), len(item_by_doi), len(item_by_title))
    return ZoteroIndex(by_doi, by_title, item_by_doi, item_by_title)
