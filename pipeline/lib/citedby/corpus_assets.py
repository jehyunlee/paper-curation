"""코퍼스에 이미 있는 논문의 전처리 자산을 끌어 쓴다.

인용논문 중 일부는 **이미 paper-curation 이 리뷰한 논문**이다. 그런 논문은
원시 PDF 보다 훨씬 나은 재료가 준비돼 있다:

    review.md   섹션별 한국어 리뷰 (Essence/Motivation/How/…/Detail 1-5)
    text.md     정제된 본문 (PDF 파싱 잔재가 제거된)
    figures/    추출된 그림
    connections 연결관계 — "이 논문과 이어지는 다른 논문" (Deeper Research 재료)
    _search_index.json  **이미 섹션 단위로 청킹·임베딩됨**

그래서 근거 우선순위는 이렇게 된다:

    corpus    코퍼스 전처리물   ← 최상. 임베딩 재계산 불필요
    pdf       보유 PDF 전문
    abstract  초록만
    title     제목뿐

특히 마지막 줄이 중요하다 — 코퍼스 논문의 청크는 토픽 인덱스에 **이미
임베딩되어** 있으므로, 벡터를 잘라 재사용하면 Gemini 호출이 0회다. 원문을 다시
파싱·임베딩하는 건 순수한 낭비이자, 이미 검증된 섹션 구조를 버리는 일이다.
"""
from __future__ import annotations

import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

EV_CORPUS = "corpus"

_PIPELINE = Path(__file__).resolve().parents[2]
_DOCS = _PIPELINE.parent / "docs"
_PAPERS = _DOCS / "papers"

GLOBAL_CONN = _PAPERS / "_global_connections.json"
PAPERS_INDEX = _PAPERS / "_papers_index.json"

# 한 논문에서 가져올 코퍼스 청크 상한. 섹션이 12개 안팎이라 넉넉하다.
MAX_CORPUS_CHUNKS = 16


def _norm_doi(v) -> str:
    s = str(v or "").strip().lower()
    for pre in ("https://doi.org/", "http://doi.org/", "doi:"):
        if s.startswith(pre):
            s = s[len(pre):]
    return s.strip()


def _norm_title(v) -> str:
    import re
    return re.sub(r"[^a-z0-9]", "", str(v or "").lower())[:60]


class CorpusIndex:
    """DOI/제목 → 코퍼스 slug, 그리고 그 slug 의 청크·벡터·연결관계."""

    def __init__(self):
        self.by_doi: dict[str, str] = {}
        self.by_title: dict[str, str] = {}
        self.meta: dict[str, dict] = {}
        self.connections: dict[str, list] = {}
        self._chunk_cache: dict[str, tuple] = {}   # topic → (index, embbytes)

    def __bool__(self) -> bool:
        return bool(self.by_doi or self.by_title)

    def lookup(self, paper: dict) -> str:
        doi = _norm_doi(paper.get("doi"))
        if doi and doi in self.by_doi:
            return self.by_doi[doi]
        t = _norm_title(paper.get("title"))
        return self.by_title.get(t, "")


def load_corpus_index() -> CorpusIndex:
    """`_papers_index.json` + `_global_connections.json` 을 읽는다.

    실패해도 예외를 던지지 않는다 — 코퍼스 보강은 부가 기능이라, 없으면 PDF
    경로로 그냥 내려가면 된다.
    """
    idx = CorpusIndex()
    try:
        raw = json.loads(PAPERS_INDEX.read_text(encoding="utf-8"))
        entries = raw if isinstance(raw, list) else (raw.get("papers") or [])
    except Exception as e:  # noqa: BLE001
        logger.info("코퍼스 인덱스 없음: %s", str(e)[:80])
        return idx

    for e in entries:
        slug = e.get("slug")
        if not slug:
            continue
        idx.meta[slug] = {
            "title": e.get("title", ""),
            "doi": e.get("doi", ""),
            "arxiv": e.get("arxiv") or e.get("arxiv_id") or "",
            "external_url": e.get("external_url") or e.get("url") or "",
            "authors": e.get("authors") or e.get("author_names") or "",
            "date": e.get("date", ""),
            "year": e.get("year") or str(e.get("date") or "")[:4],
            "journal": e.get("journal", ""),
            "primary_topic": e.get("primary_topic", ""),
            "score": e.get("score"),
            "citation_count": e.get("citation_count"),
        }
        d = _norm_doi(e.get("doi"))
        if d:
            idx.by_doi.setdefault(d, slug)
        t = _norm_title(e.get("title"))
        if t:
            idx.by_title.setdefault(t, slug)

    try:
        idx.connections = json.loads(GLOBAL_CONN.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001 — 연결관계는 선택
        idx.connections = {}

    logger.info("코퍼스 인덱스: %d편 (doi %d / title %d) · 연결 %d편",
                len(idx.meta), len(idx.by_doi), len(idx.by_title),
                len(idx.connections))
    return idx


def paper_assets(slug: str) -> dict:
    """slug 의 전처리 자산 존재 여부와 경로."""
    d = _PAPERS / slug
    figures = sorted(p.name for p in (d / "figures").glob("*")
                     if p.suffix.lower() in (".webp", ".png", ".jpg"))
    return {
        "dir": str(d),
        "has_review": (d / "review.md").exists(),
        "has_text": (d / "text.md").exists(),
        "figures": figures,
    }


def _topic_index(idx: CorpusIndex, topic: str):
    """토픽 검색 인덱스와 임베딩 사이드카를 캐싱해 로드."""
    if topic in idx._chunk_cache:
        return idx._chunk_cache[topic]
    tdir = _DOCS / topic
    ipath = tdir / "_search_index.json"
    if not ipath.exists():
        idx._chunk_cache[topic] = (None, None)
        return None, None
    try:
        data = json.loads(ipath.read_text(encoding="utf-8"))
        emb = None
        name = data.get("emb_file") or ""
        if name and (tdir / name).exists():
            emb = (tdir / name).read_bytes()
    except Exception as e:  # noqa: BLE001
        logger.warning("토픽 인덱스 로드 실패 %s: %s", topic, str(e)[:90])
        data, emb = None, None
    idx._chunk_cache[topic] = (data, emb)
    return data, emb


def corpus_chunks(slug: str, idx: CorpusIndex, *, dim: int = 768) -> tuple:
    """코퍼스 인덱스에서 이 논문의 청크와 **이미 계산된 벡터**를 잘라 온다.

    Returns:
        (chunks, vector_bytes | None) — 벡터가 있으면 재임베딩이 불필요하다.
    """
    topic = (idx.meta.get(slug) or {}).get("primary_topic") or ""
    candidates = [topic] if topic else []
    candidates += ["ai4s", "scisci", "humanoid", "physical-ai"]

    for t in candidates:
        if not t:
            continue
        data, emb = _topic_index(idx, t)
        if not data:
            continue
        chunks = data.get("chunks") or []
        picked, vecs = [], bytearray()
        for i, c in enumerate(chunks):
            if c.get("slug") != slug:
                continue
            picked.append({"slug": slug, "section": c.get("section", ""),
                           "text": c.get("text", ""),
                           "text_sha": c.get("text_sha", "")})
            if emb is not None:
                off = i * dim
                if off + dim <= len(emb):
                    vecs += emb[off:off + dim]
            if len(picked) >= MAX_CORPUS_CHUNKS:
                break
        if picked:
            ok = emb is not None and len(vecs) == len(picked) * dim
            return picked, (bytes(vecs) if ok else None)
    return [], None


def connected_papers(slug: str, idx: CorpusIndex, *, limit: int = 5) -> list:
    """이 논문과 이어지는 코퍼스 논문들 — Deeper Research 의 확장 축.

    citedby 는 "이 논문을 인용한 논문" 이라는 **시간 축**을 본다. 연결관계는
    "주제가 이어지는 논문" 이라는 **의미 축**이라, 둘을 합치면 한 논문에서
    앞뒤로 뻗어 나갈 수 있다.
    """
    out = []
    for c in (idx.connections.get(slug) or [])[:limit]:
        target = c.get("slug")
        if not target:
            continue
        m = idx.meta.get(target) or {}
        out.append({
            "slug": target,
            "title": m.get("title", ""),
            "year": m.get("year", ""),
            "authors": m.get("authors", ""),
            "journal": m.get("journal", ""),
            "doi": m.get("doi", ""),
            "arxiv": m.get("arxiv", ""),
            "external_url": m.get("external_url", ""),
            "relation": c.get("relation", ""),
            "reason": c.get("reason", ""),
        })
    return out


def enrich_with_corpus(papers: list[dict], idx: CorpusIndex | None = None,
                       *, progress=None) -> tuple[list, dict]:
    """코퍼스에 있는 인용논문에 전처리 자산을 붙인다.

    등급을 `corpus` 로 올리고 다음을 채운다:
        _corpus_slug, _corpus_assets, _connections
    초록이 비어 있으면 review.md 의 Essence 청크로 채운다 (원문보다 정제됨).
    """
    papers = [dict(p) for p in (papers or [])]
    stats = {"matched": 0, "with_conn": 0, "with_figures": 0}
    if idx is None:
        idx = load_corpus_index()
    if not idx:
        return papers, stats

    for p in papers:
        slug = idx.lookup(p)
        if not slug:
            continue
        p["_corpus_slug"] = slug
        p["_evidence"] = EV_CORPUS
        p["_corpus_assets"] = paper_assets(slug)
        conns = connected_papers(slug, idx)
        if conns:
            p["_connections"] = conns
            stats["with_conn"] += 1
        if p["_corpus_assets"]["figures"]:
            stats["with_figures"] += 1
        stats["matched"] += 1

    if progress:
        progress("corpus",
                 f"코퍼스 논문 {stats['matched']}편 — 연결 {stats['with_conn']} · "
                 f"그림 {stats['with_figures']}")
    logger.info("코퍼스 보강: %d편 (연결 %d · 그림 %d)",
                stats["matched"], stats["with_conn"], stats["with_figures"])
    return papers, stats
