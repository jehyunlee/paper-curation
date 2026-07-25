"""citedby 를 **PDF 전문 기반**으로 돌리기 위한 코퍼스 층.

전환의 배경 — 초록은 폐쇄형 논문에서 무료 API 로 못 받는다(실측: 결손 12편,
그중 SN 8편만 Metadata API 로 회수). 반면 내가 Zotero 에 보유한 PDF 에는 전문이
있다. 그래서 **초록을 쫓는 대신 내가 가진 PDF 만 대상으로** 분석한다:

    대상    인용논문 ∩ 내 Zotero 라이브러리 ∩ PDF 보유
    기반    초록(수백 자) → **전문(수만 자)**
    링크    논문마다 zotero://open-pdf 로 원문 즉시 열기

부수 효과가 크다. 주제 군집화가 제목·초록이 아니라 전문을 보므로 훨씬 정확해지고
(초록 없는 논문이 제목만으로 임베딩돼 언어별로 묶이던 문제가 사라진다),
Deep Research 의 근거 문서가 review.md 가 아닌 **원문**이 된다.

이 모듈은 세 가지를 한다:
    1. PDF 보유 논문만 선별
    2. 전문 추출 (참고문헌 이전까지)
    3. 청킹 + Gemini 임베딩 → `_citedby_index.json` + `_citedby_index_emb.bin`
       (기존 Deep Research 인덱스와 **같은 스키마** — UI 를 그대로 재사용한다)
"""
from __future__ import annotations

import hashlib
import json
import logging
import os
import re
import sys
import time
from pathlib import Path

logger = logging.getLogger(__name__)

INDEX_NAME = "_citedby_index.json"
EMB_NAME = "_citedby_index_emb.bin"

CHUNK_SIZE = 1400
CHUNK_OVERLAP = 200
EMBED_BATCH = 32
EMBED_DIM = 768
EMBED_MODEL = "gemini-embedding-001"

# 참고문헌부터는 본문이 아니다 — 청크에 들어가면 검색 노이즈가 되고 임베딩
# 품질도 떨어진다. text.md 파이프라인과 같은 판단.
_REF_HEAD = re.compile(
    r"\n\s*(references|bibliography|works\s+cited|참고\s*문헌)\s*\n",
    re.IGNORECASE)

# 한 논문에서 뽑을 청크 상한. 전문이 길어도 Deep Research 는 상위 근거만 쓰므로,
# 무한정 넣으면 인덱스만 비대해진다.
MAX_CHUNKS_PER_PAPER = 40


def _pipeline_dir() -> Path:
    return Path(__file__).resolve().parents[2]


def _import_search_index():
    """build_search_index 의 재사용 가능한 조각을 가져온다."""
    d = str(_pipeline_dir())
    if d not in sys.path:
        sys.path.insert(0, d)
    import build_search_index as bsi
    return bsi


def select_pdf_papers(papers: list[dict], index=None) -> tuple[list, list]:
    """PDF 를 보유한 논문만 남긴다.

    Returns:
        (보유 논문[, Zotero 정보가 붙은 dict], 미보유 논문)
    """
    from .local_library import load_library_index

    if index is None:
        index = load_library_index()
    held, missing = [], []
    if not index:
        return held, list(papers or [])

    for p in (papers or []):
        hit = index.lookup(p)
        if hit and hit.has_pdf:
            q = dict(p)
            q["_library_key"] = hit.key
            q["_library_attach"] = hit.attachment_key
            q["_pdf_path"] = hit.pdf_path
            q["_in_library"] = True
            q["_has_pdf"] = True
            if not str(q.get("abstract") or "").strip() and hit.abstract:
                q["abstract"] = hit.abstract
            held.append(q)
        else:
            missing.append(dict(p))
    return held, missing


def pdf_fulltext(path: str, *, max_chars: int = 120_000) -> str:
    """PDF 전문. 참고문헌 이전까지만.

    `local_library.pdf_head_text` 는 초록용으로 앞 2페이지만 읽지만, 여기서는
    Deep Research 근거로 쓸 본문 전체가 필요하다.
    """
    if not path or not os.path.exists(path):
        return ""
    try:
        import fitz  # PyMuPDF
    except ImportError:
        logger.warning("PyMuPDF 없음 — PDF 전문 추출 불가")
        return ""
    try:
        parts = []
        with fitz.open(path) as doc:
            for page in doc:
                parts.append(page.get_text())
        text = "\n".join(parts)
    except Exception as e:  # noqa: BLE001
        logger.debug("PDF 읽기 실패 %s: %s", path, str(e)[:100])
        return ""

    m = _REF_HEAD.search(text)
    if m and m.start() > len(text) * 0.3:   # 너무 앞이면 오탐 — 무시
        text = text[:m.start()]
    return re.sub(r"[ \t]+", " ", text).strip()[:max_chars]


def paper_key(p: dict) -> str:
    """인덱스 안에서 논문을 가리키는 안정 키."""
    for field in ("doi", "arxiv_id"):
        v = str(p.get(field) or "").strip().lower()
        if v:
            return re.sub(r"[^a-z0-9._/-]", "", v)[:80]
    t = re.sub(r"[^a-z0-9]", "", str(p.get("title") or "").lower())[:60]
    return t or hashlib.sha1(
        str(p.get("title") or "").encode("utf-8")).hexdigest()[:16]


def build_chunks(papers: list[dict], *, progress=None) -> tuple[list, dict]:
    """PDF 전문을 청크로 쪼갠다.

    Returns:
        (chunks, papers_meta) — chunks 는 `_search_index.json` 과 같은 모양
        `{slug, section, text, text_sha}` 이라 Deep Research UI 가 그대로 읽는다.
    """
    bsi = _import_search_index()
    chunks: list[dict] = []
    meta: dict[str, dict] = {}

    for i, p in enumerate(papers, 1):
        key = paper_key(p)
        text = pdf_fulltext(p.get("_pdf_path", ""))
        if len(text) < 500:
            logger.debug("본문 부족, 건너뜀: %s", p.get("title", "")[:50])
            continue

        windows = bsi._text_windows(text, size=CHUNK_SIZE,
                                    overlap=CHUNK_OVERLAP)
        added = 0
        for w in windows[:MAX_CHUNKS_PER_PAPER]:
            body = bsi.clean_chunk_text(w)
            if len(body) < 200:
                continue
            chunks.append({
                "slug": key,
                "section": "본문",
                "text": body,
                "text_sha": hashlib.sha256(body.encode("utf-8")).hexdigest()[:16],
            })
            added += 1

        if added:
            meta[key] = {
                "title": p.get("title", ""),
                "doi": p.get("doi", ""),
                "year": p.get("year") or p.get("date", ""),
                "journal": p.get("journal", ""),
                "authors": p.get("authors") or p.get("author_names", ""),
                "zotero_key": p.get("_library_key", ""),
                "zotero_attach": p.get("_library_attach", ""),
                "chunks": added,
            }
        if progress and (i % 5 == 0 or i == len(papers)):
            progress("index", f"본문 청킹 {i}/{len(papers)}편 · 청크 {len(chunks)}개")

    return chunks, meta


def embed_chunks(chunks: list[dict], *, progress=None) -> bytes | None:
    """청크를 Gemini 로 임베딩해 int8 사이드카 바이트로 만든다.

    반드시 L2-normalize 후 int8 로 양자화한다 — `gemini-embedding-001` 은
    output_dimensionality != 3072 일 때 **비정규화 벡터**를 돌려주기 때문이다
    (build_search_index 의 오래된 gotcha).
    """
    if not chunks:
        return None
    bsi = _import_search_index()
    try:
        from google import genai
    except ImportError:
        logger.warning("google-genai 없음 — 임베딩 생략")
        return None

    key = (os.environ.get("GOOGLE_API_KEY")
           or os.environ.get("GEMINI_API_KEY")
           or bsi._load_gemini_key_from_config())
    if not key:
        logger.warning("GOOGLE_API_KEY 없음 — 임베딩 생략")
        return None

    client = genai.Client(api_key=key)
    out = bytearray()
    total = len(chunks)
    for start in range(0, total, EMBED_BATCH):
        batch = chunks[start:start + EMBED_BATCH]
        try:
            vecs = bsi.embed_batch(client, [c["text"] for c in batch],
                                   EMBED_MODEL)
        except Exception as e:  # noqa: BLE001
            logger.warning("임베딩 배치 실패 (%d~): %s", start, str(e)[:100])
            return None
        for v in vecs:
            out += bsi.quantize_int8_l2(v)
        if progress:
            done = min(start + EMBED_BATCH, total)
            progress("index", f"임베딩 {done}/{total} 청크")
    return bytes(out)


def build_index(papers: list[dict], out_dir, *, embed: bool = True,
                progress=None) -> dict | None:
    """PDF 보유 논문으로 Deep Research 인덱스를 만든다.

    기존 `_search_index.json` 과 **같은 스키마**로 낸다 — 벡터는 별도 int8
    사이드카, 청크는 JSON. Deep Research UI 가 코퍼스 인덱스와 구분 없이 읽는다.

    Returns:
        인덱스 요약 dict. 만들 게 없으면 None.
    """
    out_dir = Path(out_dir)
    chunks, meta = build_chunks(papers, progress=progress)
    if not chunks:
        logger.info("인덱스 생략: 청크 0개")
        return None

    emb = embed_chunks(chunks, progress=progress) if embed else None
    if emb is not None and len(emb) != len(chunks) * EMBED_DIM:
        logger.warning("임베딩 길이 불일치 — 벡터 없이 저장 (%d != %d)",
                       len(emb), len(chunks) * EMBED_DIM)
        emb = None

    payload = {
        "model": EMBED_MODEL,
        "dim": EMBED_DIM,
        "quant": "int8-l2norm",
        "count": len(chunks),
        "emb_file": EMB_NAME if emb else "",
        "papers": meta,
        "chunks": chunks,
        "built_at": int(time.time()),
        "source": "citedby-pdf",
    }

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / INDEX_NAME).write_text(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8")
    if emb:
        (out_dir / EMB_NAME).write_bytes(emb)

    logger.info("citedby 인덱스: 논문 %d편 · 청크 %d개 · 벡터 %s",
                len(meta), len(chunks), "있음" if emb else "없음")
    return {
        "papers": len(meta),
        "chunks": len(chunks),
        "has_vectors": bool(emb),
        "index_path": str(out_dir / INDEX_NAME),
    }
