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

# 청크가 작으면 근거가 문장 조각으로 잘려 답변이 얇아진다. 방법·실험 서술은
# 한 문단이 2천 자를 넘는 일이 흔하므로 넉넉히 잡고, 경계에서 문맥이 끊기지
# 않도록 겹침도 늘린다.
CHUNK_SIZE = 2200
CHUNK_OVERLAP = 400
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
# 전문 평균이 63k자라 2,200자 청크로 ~29개다. 80이면 12만 자(추출 상한)까지
# 잘림 없이 담긴다 — 뒷부분(실험·결론)이 잘려 나가면 답변이 서론만 인용한다.
MAX_CHUNKS_PER_PAPER = 80


def _pipeline_dir() -> Path:
    return Path(__file__).resolve().parents[2]


def _import_search_index():
    """build_search_index 의 재사용 가능한 조각을 가져온다."""
    d = str(_pipeline_dir())
    if d not in sys.path:
        sys.path.insert(0, d)
    import build_search_index as bsi
    return bsi


# 근거 등급 — 각 논문의 분석이 무엇에 기반했는지. 리포트에 그대로 노출해
# 독자가 신뢰도를 판단할 수 있게 한다.
EV_CORPUS = "corpus"      # 코퍼스 전처리물 (review 섹션 + text.md + figures + 연결)
EV_PDF = "pdf"            # 보유 PDF 전문 (수만 자)
EV_ABSTRACT = "abstract"  # 초록만 (수백~2천 자)
EV_TITLE = "title"        # 제목뿐

# 초록으로 인정할 최소 길이. 이보다 짧으면 사실상 제목만 있는 것과 같다.
MIN_ABSTRACT = 120


def tier_papers(papers: list[dict], index=None) -> tuple[list, dict]:
    """모든 인용논문에 **근거 등급**을 매긴다. 제외하지 않는다.

    PDF 가 없다고 논문을 버리면 정보가 통째로 사라진다 — 초록만이라도 있으면
    주제 군집·요약에 쓸 수 있고, 목록에 남아 있는 것 자체가 정보다.

        pdf       내 Zotero 보유 PDF 전문   (최선)
        abstract  초록만                     (제한적)
        title     제목뿐                     (최소)

    Returns:
        (등급이 매겨진 papers, 등급별 편수)
    """
    from .local_library import load_library_index
    from .corpus_assets import enrich_with_corpus

    if index is None:
        index = load_library_index()

    # 코퍼스 전처리물이 최우선 — review 섹션·text.md·figures·연결관계가 있고
    # 검색 인덱스에 **이미 임베딩되어** 있다. 원시 PDF 를 다시 파싱할 이유가 없다.
    papers, _corpus_stats = enrich_with_corpus(list(papers or []))

    out = []
    stats = {EV_CORPUS: 0, EV_PDF: 0, EV_ABSTRACT: 0, EV_TITLE: 0}
    for p in papers:
        q = dict(p)
        hit = index.lookup(q) if index else None
        if hit:
            q["_in_library"] = True
            q["_library_key"] = hit.key
            q["_library_attach"] = hit.attachment_key
            if hit.has_pdf:
                q["_pdf_path"] = hit.pdf_path
                q["_has_pdf"] = True
            if not str(q.get("abstract") or "").strip() and hit.abstract:
                q["abstract"] = hit.abstract
        else:
            q["_in_library"] = False

        if q.get("_corpus_slug"):
            q["_evidence"] = EV_CORPUS
        elif q.get("_pdf_path"):
            q["_evidence"] = EV_PDF
        elif len(str(q.get("abstract") or "").strip()) >= MIN_ABSTRACT:
            q["_evidence"] = EV_ABSTRACT
        else:
            q["_evidence"] = EV_TITLE
        stats[q["_evidence"]] += 1
        out.append(q)
    return out, stats


def select_pdf_papers(papers: list[dict], index=None) -> tuple[list, list]:
    """PDF 보유분만 골라낸다 (엄격 모드용). 등급 분류는 `tier_papers` 를 쓴다."""
    tiered, _ = tier_papers(papers, index)
    held = [p for p in tiered if p["_evidence"] == EV_PDF]
    missing = [p for p in tiered if p["_evidence"] != EV_PDF]
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


def _clean_doi(value) -> str:
    doi = str(value or "").strip()
    doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", doi,
                 flags=re.IGNORECASE)
    doi = re.sub(r"^doi:\s*", "", doi, flags=re.IGNORECASE)
    return doi if re.match(r"^10\.\d{3,}/\S+$", doi) else ""


def _external_url(paper: dict) -> str:
    """독립 export에서 항상 해석되는 논문 원문 주소."""
    doi = _clean_doi(paper.get("doi"))
    if doi:
        return f"https://doi.org/{doi}"
    arxiv = str(paper.get("arxiv") or paper.get("arxiv_id") or "").strip()
    arxiv = re.sub(r"^arxiv:\s*", "", arxiv, flags=re.IGNORECASE)
    if arxiv:
        return f"https://arxiv.org/abs/{arxiv}"
    for field in ("external_url", "url", "landing_page_url"):
        url = str(paper.get(field) or "").strip()
        if re.match(r"^https?://", url):
            return url
    return ""


def _note_file(key: str, title: str) -> str:
    stem = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:48]
    digest = hashlib.sha1(key.encode("utf-8")).hexdigest()[:10]
    return f"{stem or 'paper'}-{digest}.md"


def _reference_meta(paper: dict, key: str, corpus_slug: str = "") -> dict:
    doi = _clean_doi(paper.get("doi"))
    arxiv = str(paper.get("arxiv") or paper.get("arxiv_id") or "").strip()
    meta = {
        "title": paper.get("title", ""),
        "doi": doi,
        "arxiv": re.sub(r"^arxiv:\s*", "", arxiv, flags=re.IGNORECASE),
        "external_url": _external_url(paper),
        "year": paper.get("year") or paper.get("date", ""),
        "journal": paper.get("journal", ""),
        "authors": paper.get("authors") or paper.get("author_names", ""),
        "zotero_key": paper.get("_library_key", ""),
        "zotero_attach": paper.get("_library_attach", ""),
        "corpus_slug": corpus_slug,
        "reference_type": EV_CORPUS if corpus_slug else "citedby-note",
    }
    if not corpus_slug:
        meta["note_file"] = _note_file(key, str(paper.get("title") or ""))
    return meta


def build_chunks(papers: list[dict], *, progress=None) -> tuple[list, dict]:
    """근거를 청크로 쪼갠다 (코퍼스 재사용 > PDF 전문 > 초록).

    Returns:
        (chunks, papers_meta) — chunks 는 `_search_index.json` 과 같은 모양
        `{slug, section, text, text_sha}` 이라 Deep Research UI 가 그대로 읽는다.
    """
    from .corpus_assets import corpus_chunks
    bsi = _import_search_index()
    chunks: list[dict] = []
    meta: dict[str, dict] = {}
    reused_vecs: dict[str, bytes] = {}   # 코퍼스에서 잘라 온 벡터 (재임베딩 불필요)
    corpus_idx = None

    for i, p in enumerate(papers, 1):
        key = paper_key(p)

        # 코퍼스 논문은 이미 섹션 단위로 청킹·임베딩돼 있다. 잘라 쓰면 Gemini
        # 호출이 0회이고, 검증된 섹션 구조(Essence/Motivation/…)도 보존된다.
        cslug = p.get("_corpus_slug")
        if cslug:
            if corpus_idx is None:
                from .corpus_assets import load_corpus_index
                corpus_idx = load_corpus_index()
            cchunks, cvecs = corpus_chunks(cslug, corpus_idx)
            if cchunks:
                for c in cchunks:
                    c["slug"] = key
                    chunks.append(c)
                reused_vecs[key] = cvecs
                meta[key] = {
                    **_reference_meta(p, key, cslug),
                    "evidence": EV_CORPUS,
                    "connections": p.get("_connections") or [],
                    "chunks": len(cchunks),
                }
                if progress and (i % 5 == 0 or i == len(papers)):
                    progress("index", f"코퍼스 청크 재사용 {i}/{len(papers)}편")
                continue

        # PDF 가 있으면 전문, 없으면 초록이라도 인덱싱한다. 근거가 얇은 건
        # 사실이지만 검색 대상에서 통째로 빠지는 것보다는 낫다.
        text = pdf_fulltext(p.get("_pdf_path", ""))
        evidence = EV_PDF if len(text) >= 500 else ""
        if not evidence:
            text = str(p.get("abstract") or "").strip()
            evidence = EV_ABSTRACT if len(text) >= MIN_ABSTRACT else ""
        if not evidence:
            logger.debug("근거 부족, 건너뜀: %s", p.get("title", "")[:50])
            continue

        windows = bsi._text_windows(text, size=CHUNK_SIZE,
                                    overlap=CHUNK_OVERLAP)
        added = 0
        cap = MAX_CHUNKS_PER_PAPER if evidence == EV_PDF else 4
        for w in windows[:cap]:
            body = bsi.clean_chunk_text(w)
            if len(body) < 200:
                continue
            chunks.append({
                "slug": key,
                "section": "본문" if evidence == EV_PDF else "초록",
                "text": body,
                "text_sha": hashlib.sha256(body.encode("utf-8")).hexdigest()[:16],
            })
            added += 1

        if added:
            meta[key] = {
                **_reference_meta(p, key),
                "evidence": evidence,
                "chunks": added,
            }
        if progress and (i % 5 == 0 or i == len(papers)):
            progress("index", f"본문 청킹 {i}/{len(papers)}편 · 청크 {len(chunks)}개")

    return chunks, meta, reused_vecs


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


def write_evidence_notes(out_dir: Path, meta: dict, chunks: list[dict]) -> int:
    """코퍼스 밖 인용논문을 Obsidian에서 연결할 최소 evidence note로 저장."""
    notes_dir = out_dir / "notes"
    by_key: dict[str, list[dict]] = {}
    for chunk in chunks:
        by_key.setdefault(chunk.get("slug", ""), []).append(chunk)

    written = 0
    seed_slug = out_dir.parent.name
    for key, paper in meta.items():
        if paper.get("reference_type") == EV_CORPUS:
            slug = paper.get("corpus_slug", "")
            paper["local_html"] = f"../../{slug}/"
            paper["local_md"] = f"../../{slug}/review.md"
            paper["obsidian_path"] = f"papers/{slug}/review"
            continue

        note_file = paper.get("note_file") or _note_file(key, paper.get("title", ""))
        note_stem = Path(note_file).stem
        paper["local_md"] = f"notes/{note_file}"
        paper["obsidian_path"] = (
            f"papers/{seed_slug}/citedby/notes/{note_stem}"
        )
        evidence = by_key.get(key) or []
        authors = paper.get("authors") or ""
        if isinstance(authors, list):
            authors = ", ".join(str(a) for a in authors)
        lines = [
            f"# {paper.get('title') or 'Untitled'}", "",
            f"- Authors: {authors or '-'}",
            f"- Year: {paper.get('year') or '-'}",
            f"- Journal: {paper.get('journal') or '-'}",
            f"- Evidence: {paper.get('evidence') or '-'}",
        ]
        if paper.get("doi"):
            lines.append(f"- DOI: https://doi.org/{paper['doi']}")
        elif paper.get("external_url"):
            lines.append(f"- Source: {paper['external_url']}")
        lines += [
            f"- Seed review: [[papers/{seed_slug}/review|원논문 review]]",
            "", "## Evidence excerpts", "",
        ]
        for i, chunk in enumerate(evidence[:3], 1):
            lines += [
                f"### {i}. {chunk.get('section') or '본문'}", "",
                str(chunk.get("text") or "")[:2200].strip(), "",
            ]
        notes_dir.mkdir(parents=True, exist_ok=True)
        (notes_dir / note_file).write_text(
            "\n".join(lines).rstrip() + "\n", encoding="utf-8")
        written += 1
    return written

def build_index(papers: list[dict], out_dir, *, embed: bool = True,
                progress=None) -> dict | None:
    """PDF 보유 논문으로 Deep Research 인덱스를 만든다.

    기존 `_search_index.json` 과 **같은 스키마**로 낸다 — 벡터는 별도 int8
    사이드카, 청크는 JSON. Deep Research UI 가 코퍼스 인덱스와 구분 없이 읽는다.

    Returns:
        인덱스 요약 dict. 만들 게 없으면 None.
    """
    out_dir = Path(out_dir)
    chunks, meta, reused = build_chunks(papers, progress=progress)
    # 검색 근거가 너무 얇어 청크가 없는 논문도 Obsidian 지식망에서는 사라지면
    # 안 된다. 최소 metadata note를 만들고, 뒤이어 생성되는 HTML report가 같은
    # paper dict에서 그 경로를 읽도록 돌려준다.
    for paper in papers:
        key = paper_key(paper)
        if key not in meta:
            meta[key] = {
                **_reference_meta(
                    paper, key, str(paper.get("_corpus_slug") or "")),
                "evidence": paper.get("_evidence") or EV_TITLE,
                "connections": paper.get("_connections") or [],
                "chunks": 0,
            }
    note_count = write_evidence_notes(out_dir, meta, chunks)
    for paper in papers:
        ref = meta.get(paper_key(paper)) or {}
        paper["_citedby_obsidian_path"] = ref.get("obsidian_path", "")
        paper["_citedby_note_file"] = ref.get("note_file", "")

    if not chunks:
        logger.info("인덱스 생략: 청크 0개")
        return None

    emb = None
    if embed:
        # 코퍼스에서 잘라 온 벡터가 있는 청크는 재임베딩하지 않는다.
        # 청크 순서 = 벡터 순서라, 슬롯을 남겨 두고 새로 만든 것만 채운다.
        need = [c for c in chunks if c["slug"] not in reused]
        fresh = embed_chunks(need, progress=progress) if need else b""
        if fresh is None:
            logger.warning("신규 임베딩 실패 — 벡터 없이 저장")
        else:
            buf, fi = bytearray(), 0
            ok = True
            for c in chunks:
                v = reused.get(c["slug"])
                if v is not None:
                    # 논문 단위로 잘라 온 벡터를 청크 순서대로 소비한다.
                    take = v[:EMBED_DIM]
                    reused[c["slug"]] = v[EMBED_DIM:]
                    if len(take) != EMBED_DIM:
                        ok = False
                        break
                    buf += take
                else:
                    seg = fresh[fi:fi + EMBED_DIM]
                    fi += EMBED_DIM
                    if len(seg) != EMBED_DIM:
                        ok = False
                        break
                    buf += seg
            emb = bytes(buf) if ok else None
            if not ok:
                logger.warning("벡터 조립 실패 — 벡터 없이 저장")
            else:
                logger.info("임베딩: 재사용 %d청크 · 신규 %d청크",
                            len(chunks) - len(need), len(need))

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
        "evidence_notes": note_count,
        "index_path": str(out_dir / INDEX_NAME),
    }
