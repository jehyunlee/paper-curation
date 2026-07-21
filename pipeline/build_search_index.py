"""
Build a Deep Research search index (for client-side RAG).

Reads every review.md that belongs to the given topic, splits each one
into section-aware chunks (Essence, Motivation, How, Achievement,
Originality), embeds each chunk with Google `gemini-embedding-001`
(task_type RETRIEVAL_DOCUMENT, output_dimensionality=768),
L2-normalises and quantises the 768-dim float32 vectors down to int8,
then writes `docs/{topic}/_search_index.json`.

주의(gotcha): gemini-embedding-001 은 output_dimensionality 가 3072 가
아닐 때 정규화되지 않은 벡터를 돌려준다. int8 양자화 전에 반드시 L2
정규화해야 한다 — quantize_int8_l2() 가 그 정규화를 수행하므로 커버된다.

The resulting JSON is fetched lazily by the topic's index.html when a
user activates Deep Research mode. The browser dequantises the int8
embeddings (no scale needed because L2-normalisation maps everything
to [-1, 1] with an implicit scale of 1/127) and performs cosine-
similarity retrieval client-side before calling Claude with the top-k
chunks as context.

Usage:
  PYTHONUTF8=1 python pipeline/build_search_index.py --topic ai4s
  PYTHONUTF8=1 python pipeline/build_search_index.py --topic scisci
  PYTHONUTF8=1 python pipeline/build_search_index.py --topic ai4s --limit 10    # debug
  PYTHONUTF8=1 python pipeline/build_search_index.py --topic ai4s --dry-run     # chunk only, no API
"""

import argparse
import base64
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

PIPELINE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(PIPELINE_DIR))
from config_loader import DOCS_DIR, PAPERS_DIR, PROJECT_ROOT, get_topic_dir, get_papers_index_path

# Zotero metadata (normalized-title -> {url, doi}) captured by build_topic_index.
# Gives a real external URL for papers whose review.md frontmatter has a
# placeholder DOI ("미제공"/"N/A"/"-") or none. Optional + local-only.
_ZMETA_CACHE = None


def source_fingerprint(topic, slugs, *, docs_dir=None, papers_dir=None):
    """Fingerprint files that feed one topic index without parsing/re-embedding.

    Path + size + nanosecond mtime make deploy freshness checks cheap. The
    builder records this after collecting papers; prepare_deploy recomputes it.
    """
    docs_root = Path(docs_dir) if docs_dir is not None else Path(DOCS_DIR)
    papers_root = Path(papers_dir) if papers_dir is not None else Path(PAPERS_DIR)
    files = []
    for slug in sorted(set(slugs)):
        for name in ("review.md", "notes.md"):
            path = papers_root / slug / name
            if path.exists():
                files.append((f"papers/{slug}/{name}", path))
    notes_root = docs_root / "notes" / topic
    if notes_root.exists():
        for path in sorted(notes_root.rglob("*.md")):
            if not path.name.startswith("_"):
                files.append((f"notes/{topic}/{path.relative_to(notes_root).as_posix()}", path))

    digest = hashlib.sha256()
    for rel, path in files:
        stat = path.stat()
        digest.update(f"{rel}\0{stat.st_size}\0{stat.st_mtime_ns}\n".encode("utf-8"))
    return digest.hexdigest(), len(files)


def _zotero_meta():
    global _ZMETA_CACHE
    if _ZMETA_CACHE is None:
        _ZMETA_CACHE = {}
        try:
            _p = DOCS_DIR / "_zotero_meta.json"
            if _p.exists():
                _ZMETA_CACHE = json.load(open(_p, encoding="utf-8"))
        except Exception:
            _ZMETA_CACHE = {}
    return _ZMETA_CACHE


def _znorm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def _resolve_external(title, doi, arxiv):
    """(clean_doi, clean_arxiv, external_url): prefer a valid 10.x DOI, then an
    arXiv id (incl. one mislabeled into the doi field), then a Zotero URL."""
    doi = (doi or "").strip()
    arxiv = (arxiv or "").strip()
    if not arxiv and re.search(r"ar[xX]iv", doi):
        m = re.search(r"(\d{4}\.\d{4,5})", doi)
        if m:
            arxiv = m.group(1)
    if not re.match(r"^10\.\d{3,}/", doi):
        doi = ""  # drop placeholders / mislabeled ids
    z = _zotero_meta().get(_znorm(title)) or {}
    if not doi:
        zd = (z.get("doi") or "").strip()
        if re.match(r"^10\.\d{3,}/", zd):
            doi = zd
    zurl = (z.get("url") or "").strip()
    if doi:
        ext = f"https://doi.org/{doi}"
    elif arxiv:
        ext = f"https://arxiv.org/abs/{arxiv}"
    elif zurl.startswith("http"):
        ext = zurl
    else:
        ext = ""
    return doi, arxiv, ext


def _load_gemini_key_from_config() -> str:
    """Fallback: read gemini/google api key from config.json (written by setup.py)."""
    try:
        cfg_path = PROJECT_ROOT / "config.json"
        if cfg_path.exists():
            with open(cfg_path, "r", encoding="utf-8") as f:
                cfg = json.load(f)
            return (cfg.get("gemini_api_key") or cfg.get("google_api_key") or "") or ""
    except Exception:
        pass
    return ""

try:
    import numpy as np
except ImportError:
    print("ERROR: numpy not installed. Run: pip install numpy")
    sys.exit(1)


# Sections worth indexing (order matters — determines which chunk is
# retrieved first when there is a tie). "How" carries method details,
# "Achievement" carries results, "Originality" carries novelty framing.
#
# Limitation/Evaluation 은 모든 review.md 에 100% 존재하지만 누락돼 있었음:
#   - Limitation: 약점·미해결 과제 검색 ("이 분야 한계는?")
#   - Evaluation: 벤치마크·메트릭 검색 ("X benchmark 성능 비교")
# extract_sections() 가 'Limitation & Further Study' → 'Limitation' 키로
# 정규화하므로 짧은 이름으로 매칭 가능.
#
# Related Papers 는 cross-citation noise (다른 논문 제목/저자 leak) 우려로 보류.
SECTIONS_TO_INDEX = [
    "Essence", "Motivation", "How", "Achievement", "Originality",
    "Limitation", "Evaluation",
]

# Evaluation 섹션의 점수 루브릭 줄("- Novelty: 4/5" 등)은 거의 모든
# 논문에서 동일한 scaffolding 이라, 그대로 임베딩하면 ~2362 개의 사실상
# 중복 벡터가 생겨 top-k 검색을 오염시킨다. chunking 전에 이 점수 줄만
# 제거하고 paper-specific 한 **총평** 산문만 남긴다. (점수만 있고 산문이
# 없으면 MIN_CHUNK_CHARS 미달로 자연히 chunk 가 빠진다.) Limitation 은
# 진짜 산문이므로 그대로 둔다.
EVAL_RUBRIC_LINE_RE = re.compile(
    r"(?im)^[ \t]*[-*]?\s*"
    r"(?:Novelty|Technical\s+Soundness|Significance|Clarity|Overall)"
    r"\s*[:：]\s*\d+(?:\.\d+)?\s*/\s*\d+(?:\.\d+)?\s*$\n?"  # 4/5 또는 4.5/5
)

H2_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
FIGURE_RE = re.compile(
    r"!\[([^\]]*)\]\((figures/[^)]+\.(?:webp|png|jpg|jpeg))\)",
    re.IGNORECASE,
)
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
MD_IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]+\)")
TABLE_LINE_RE = re.compile(r"^\s*\|.*\|\s*$", re.MULTILINE)
WS_RE = re.compile(r"[ \t]+")
BLANK_RE = re.compile(r"\n\s*\n\s*\n+")

# Gemini limits: gemini-embedding-001 accepts up to 2048 tokens per input.
# Korean averages ~2 chars/token, so 6000 chars (~3000 tokens) can overflow;
# auto_truncate=True 로 초과분은 모델이 잘라낸다. 6000 자 cap 은 JSON
# payload 크기를 적당히 유지하기 위한 것이기도 하다.
MAX_CHUNK_CHARS = 6000
MIN_CHUNK_CHARS = 40


def extract_sections(md_text: str) -> dict:
    """Split a review.md into {section_name: body_text}."""
    matches = list(H2_RE.finditer(md_text))
    sections = {}
    for i, m in enumerate(matches):
        name = m.group(1).strip()
        # Normalise compound headers ("Limitation & Further Study")
        name_key = name.split("&")[0].strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(md_text)
        body = md_text[start:end].strip()
        sections[name_key] = body
        sections[name] = body  # keep full name too
    return sections


# Caption pattern in PyMuPDF-extracted text. Matches lines like
#   "Figure 1: Schematic of the proposed system."
#   "Fig. 2. Performance comparison across baselines"
#   "FIG 3 -- Synthesis pipeline"
# Group 1 captures the figure number, group 2 the caption sentence.
PDF_CAPTION_RE = re.compile(
    r"(?im)^[ \t]*(?:Figure|Fig\.?|FIG\.?)\s*0*(\d+)\s*[\.:\-\u2013\u2014]\s*([^\n]{20,400})"
)

def _captions_from_text(text_md: str) -> dict:
    """Pull "Figure N: ..." style captions out of the raw PDF text."""
    out: dict = {}
    for m in PDF_CAPTION_RE.finditer(text_md):
        num = m.group(1)
        cap = m.group(2).strip().rstrip(".")
        if not num or not cap:
            continue
        # Keep the longest caption per figure number (later occurrences
        # are usually richer than the in-text reference).
        prev = out.get(num, "")
        if len(cap) > len(prev):
            out[num] = cap
    return out


def extract_figures(md_text: str, slug: str) -> list:
    """Return every figure that physically exists on disk for this paper.

    PyMuPDF extracts up to 5 figures per paper, but the Claude-written
    review.md typically only cites 1-3 of them in fig_essence /
    fig_achievement / fig_how. The rest sit on disk unused.

    Caption resolution priority for each on-disk file:
      1. The italic caption authored by Claude in review.md (Korean)
      2. The original "Figure N: ..." sentence pulled from text.md
         (English, PyMuPDF extraction of the PDF body)
      3. A numeric "Figure N" placeholder

    text.md is git-ignored, so step 2 only succeeds when the build
    runs locally (operator side). The captions still get baked into
    _search_index.json which IS shipped to Cloudflare, so visitors
    benefit from the better captions even though text.md itself
    never reaches the public site.
    """
    # 1) Captions Claude wrote in review.md (Korean alt text on the image)
    caption_by_path: dict = {}
    for m in FIGURE_RE.finditer(md_text):
        cap = m.group(1).strip()
        path = m.group(2)  # "figures/fig1.webp"
        if cap and path not in caption_by_path:
            caption_by_path[path] = cap

    # 2) Captions from PyMuPDF-extracted text (only if text.md is on disk)
    text_path = PAPERS_DIR / slug / "text.md"
    text_caption_by_num: dict = {}
    if text_path.exists():
        try:
            text_md = text_path.read_text(encoding="utf-8")
            text_caption_by_num = _captions_from_text(text_md)
        except Exception:
            pass

    fig_dir = PAPERS_DIR / slug / "figures"
    if not fig_dir.exists():
        return []

    files = sorted(
        f.name for f in fig_dir.iterdir()
        if f.suffix.lower() in (".webp", ".png", ".jpg", ".jpeg")
    )

    figures = []
    for fname in files:
        rel = f"figures/{fname}"
        # Prefer the human-written Korean caption from review.md.
        cap = caption_by_path.get(rel, "")
        if not cap:
            # Fall back to the original PDF caption when available.
            num_m = re.search(r"(\d+)", fname)
            num = num_m.group(1) if num_m else None
            if num and num in text_caption_by_num:
                cap = text_caption_by_num[num]
            elif num:
                cap = f"Figure {num}"
            else:
                cap = fname
        figures.append({
            "caption": cap,
            # URL is resolved from docs/{topic}/ (the page that will host
            # the search UI), hence the ../papers/ prefix.
            "url": f"../papers/{slug}/{rel}",
        })
    return figures


def clean_chunk_text(text: str) -> str:
    """Strip markdown artefacts so the embedding reflects raw content."""
    text = MD_IMAGE_RE.sub("", text)                          # drop images
    text = MD_LINK_RE.sub(r"\1", text)                        # link -> label
    text = TABLE_LINE_RE.sub("", text)                        # drop table rows
    text = WS_RE.sub(" ", text)
    text = BLANK_RE.sub("\n\n", text)
    return text.strip()


def parse_review(md_path: Path, slug: str) -> dict:
    """Return {title, year, figures, chunks, authors, first_author, doi, arxiv} for a review.md.

    Authors / DOI / arXiv come from the schema v1 frontmatter when
    present (cheapest + most accurate). Falls back to body-blockquote
    regex parsing for any review.md not yet migrated.
    """
    try:
        text = md_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  WARN: {slug}: cannot read review.md ({e})")
        return None

    # ── Frontmatter fast path (schema v1) ────────────────────────────────
    authors: list[str] = []
    doi = ""
    arxiv = ""
    journal = ""
    body = text
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            try:
                import yaml as _yaml  # PyYAML
                fm = _yaml.safe_load(text[3:end]) or {}
                if isinstance(fm.get("authors"), list):
                    authors = [str(a).strip() for a in fm["authors"] if str(a).strip()]
                doi = str(fm.get("doi") or "").strip()
                arxiv = str(fm.get("arxiv") or "").strip()
                journal = str(fm.get("journal") or "").strip()
            except Exception:
                pass
            body = text[end + 4:]

    # ── Body-blockquote 저자 라인 ────────────────────────────────────────
    # frontmatter authors 는 build_papers_index 단계에서 5명으로 truncate되어
    # 시니어(주로 마지막) 저자가 누락된다(예: Dashun Wang). 본문 "> **저자**:"
    # 라인은 전체 저자를 보존하므로 더 긴 쪽을 채택해 저자 기반 검색 누락을 막는다.
    am = re.search(r"\*\*저자\*\*:\s*([^|*\n]+?)(?:\s*\|)", body)
    if am:
        body_authors = [a.strip() for a in am.group(1).split(",") if a.strip()]
        if len(body_authors) > len(authors):
            authors = body_authors
    if not doi:
        dm = re.search(r"\*\*DOI\*\*:\s*\[?([^\]\s\)]+)", body)
        if dm:
            doi = dm.group(1).strip()
    if not arxiv:
        xm = re.search(r"arxiv\.org/abs/([0-9.]+)", body)
        if xm:
            arxiv = xm.group(1).strip()

    first_author = authors[0] if authors else ""

    title_m = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else slug

    # Year: first 4-digit looking date in the first 800 chars
    year = None
    ym = re.search(r"\b(20\d{2}|19\d{2})\b", body[:800])
    if ym:
        year = int(ym.group(0))

    sections = extract_sections(text)
    figures = extract_figures(text, slug)

    chunks = []
    for sec_name in SECTIONS_TO_INDEX:
        if sec_name not in sections:
            continue
        raw = sections[sec_name]
        # Evaluation 은 점수 루브릭 줄을 떼어내 중복 벡터 오염을 막는다.
        # (총평 산문만 남으면 paper-specific, 점수만 있으면 MIN 미달로 drop)
        if sec_name == "Evaluation":
            raw = EVAL_RUBRIC_LINE_RE.sub("", raw)
        cleaned = clean_chunk_text(raw)
        if len(cleaned) < MIN_CHUNK_CHARS:
            continue
        if len(cleaned) > MAX_CHUNK_CHARS:
            cleaned = cleaned[:MAX_CHUNK_CHARS].rsplit(" ", 1)[0] + "…"
        chunks.append({"section": sec_name, "text": cleaned})

    # Personal notes: if a notes.md file sits alongside review.md
    # (Obsidian-edited, git-ignored), include it as an extra chunk so
    # Deep Research can cite the operator's own ideas and hypotheses.
    notes_path = md_path.parent / "notes.md"
    if notes_path.exists():
        try:
            notes_text = notes_path.read_text(encoding="utf-8")
            notes_cleaned = clean_chunk_text(notes_text)
            if len(notes_cleaned) >= MIN_CHUNK_CHARS:
                chunks.append({
                    "section": "My Notes",
                    "text": notes_cleaned[:MAX_CHUNK_CHARS],
                })
        except Exception:
            pass

    return {
        "title": title,
        "year": year,
        "authors": authors,              # 전체 저자 유지 (저자 기반 검색 완전성)
        "first_author": first_author,
        "doi": doi,
        "arxiv": arxiv,
        "journal": journal,
        "figures": figures,
        "chunks": chunks,
    }


def quantize_int8_l2(vec: list) -> bytes:
    """L2-normalise then quantise to int8.

    L2-normalisation makes cosine similarity equivalent to a dot product,
    and also ensures every component is in [-1, 1] so we can multiply by
    127 without needing a per-vector scale factor.
    """
    arr = np.asarray(vec, dtype=np.float32)
    norm = float(np.linalg.norm(arr))
    if norm > 0:
        arr = arr / norm
    q = np.clip(np.round(arr * 127.0), -128, 127).astype(np.int8)
    return q.tobytes()


# ── Content-addressed embedding cache ────────────────────────────────────
# 매 build 마다 ~16k chunk 를 전부 재임베딩하면 한국망 Gemini 호출이 느리고
# (transient 429 한 번에 전체가 죽고) 비용이 든다. chunk_text 는 review.md
# 에서 deterministic 하게 나오므로, sha256(model + text) → 양자화된 emb(b64)
# 로 캐싱한다. 양자화된 벡터(=index 에 그대로 들어가는 값)를 저장하므로
# 재양자화로 인한 drift 가 없다 (int8 quantization 과 100% 일관).
EMBED_CACHE_NAME = "_embedding_cache.json"
# 임베딩 바이너리 사이드카 — chunk 순서대로 dim 바이트씩 (JSON 의 chunks 와 1:1)
EMB_BIN_NAME = "_search_index_emb.bin"


def _chunk_sha(model: str, text: str) -> str:
    """Cache key = sha256 over model + chunk text (deterministic)."""
    h = hashlib.sha256()
    h.update(model.encode("utf-8"))
    h.update(b"\n")
    h.update(text.encode("utf-8"))
    return h.hexdigest()


def load_embedding_cache(topic_dir: Path, model: str) -> dict:
    """Build {text_sha: emb_b64} from the prior index + sidecar cache.

    Two sources, both keyed by the same sha so a hit is a hit:
      1. the previous _search_index.json (already shipped, has text+emb)
      2. the _embedding_cache.json sidecar (partial-save / resume store)
    Entries whose model does not match are ignored (model is part of the sha).
    """
    cache: dict = {}

    # 1) previous index — derive sha from stored text + (its) model
    prev_path = topic_dir / "_search_index.json"
    if prev_path.exists():
        try:
            prev = json.loads(prev_path.read_text(encoding="utf-8"))
            prev_model = prev.get("model", model)
            if prev_model == model:
                prev_chunks = prev.get("chunks", [])
                # 신형 포맷: emb 는 바이너리 사이드카(emb_file)에 chunk 순서대로
                # dim 바이트씩 — 거기서 잘라 b64 로 복원해 캐시에 넣는다.
                bin_blob = None
                prev_dim = int(prev.get("dim") or 0)
                if prev.get("emb_file") and prev_dim > 0:
                    bin_path = topic_dir / prev["emb_file"]
                    if (bin_path.exists()
                            and bin_path.stat().st_size == prev_dim * len(prev_chunks)):
                        bin_blob = bin_path.read_bytes()
                for ci, ch in enumerate(prev_chunks):
                    txt = ch.get("text")
                    if not txt:
                        continue
                    emb = ch.get("emb")
                    if not emb and bin_blob is not None:
                        emb = base64.b64encode(
                            bin_blob[ci * prev_dim:(ci + 1) * prev_dim]
                        ).decode("ascii")
                    if not emb:
                        continue
                    sha = ch.get("text_sha") or _chunk_sha(model, txt)
                    cache[sha] = emb
        except Exception as e:
            print(f"      WARN: could not read prior index for cache ({e})")

    # 2) sidecar cache — already keyed by sha, model-scoped
    side_path = topic_dir / EMBED_CACHE_NAME
    if side_path.exists():
        try:
            side = json.loads(side_path.read_text(encoding="utf-8"))
            if side.get("model") == model:
                for sha, emb in (side.get("emb") or {}).items():
                    cache[sha] = emb
        except Exception as e:
            print(f"      WARN: could not read embedding cache ({e})")

    return cache


def save_embedding_cache(topic_dir: Path, model: str, sha_to_emb: dict) -> None:
    """Persist the full {text_sha: emb_b64} map to the sidecar (atomic)."""
    side_path = topic_dir / EMBED_CACHE_NAME
    tmp = side_path.with_suffix(side_path.suffix + ".tmp")
    payload = {"model": model, "count": len(sha_to_emb), "emb": sha_to_emb}
    tmp.write_text(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    os.replace(tmp, side_path)


EMBED_MAX_ATTEMPTS = 6
EMBED_BACKOFF_CAP_S = 60.0


def _retry_after_seconds(err) -> float | None:
    """Best-effort extraction of a Retry-After hint from a Gemini error.

    한국↔Gemini 경로의 429 는 7초 backoff 로는 못 벗어날 수 있다. 에러가
    노출하는 retry hint (응답 헤더 또는 .retry_after) 를 존중해 backoff 를
    맞춘다 (상한 EMBED_BACKOFF_CAP_S). google-genai APIError 가 hint 를
    안 주면 None 을 돌려주고 지수 backoff 로 떨어진다.
    """
    val = getattr(err, "retry_after", None)
    if val is None:
        resp = getattr(err, "response", None)
        headers = getattr(resp, "headers", None)
        if headers is not None:
            try:
                val = headers.get("retry-after") or headers.get("Retry-After")
            except Exception:
                val = None
    if val is None:
        return None
    try:
        return float(val)
    except (TypeError, ValueError):
        return None


def embed_batch(client, texts: list, model: str) -> list:
    """Embed a batch with gemini-embedding-001 (RETRIEVAL_DOCUMENT) + retry.

    768-dim 출력을 task_type RETRIEVAL_DOCUMENT 로 요청한다. Retry-After 를
    존중하고 backoff 를 EMBED_BACKOFF_CAP_S 로 cap 하며, 반환 벡터 수가
    입력 수와 다르면 (조용한 chunk↔embedding misalignment 대신) 시끄럽게
    실패한다. 정규화는 호출측 quantize_int8_l2() 가 수행한다 (gemini 는
    output_dimensionality != 3072 일 때 비정규화 벡터를 돌려주므로).
    """
    from google.genai import types as _gtypes

    cfg = _gtypes.EmbedContentConfig(
        task_type="RETRIEVAL_DOCUMENT",
        output_dimensionality=768,
    )
    last_err = None
    for attempt in range(EMBED_MAX_ATTEMPTS):
        try:
            resp = client.models.embed_content(model=model, contents=texts, config=cfg)
            vecs = [list(e.values) for e in (resp.embeddings or [])]
            # Per-batch length guard — a short/long batch would otherwise
            # silently misalign chunks↔embeddings downstream (zip()).
            if len(vecs) != len(texts):
                raise RuntimeError(
                    f"embedding count {len(vecs)} != input count {len(texts)}"
                )
            return vecs
        except Exception as e:
            last_err = e
            if attempt == EMBED_MAX_ATTEMPTS - 1:
                break
            hint = _retry_after_seconds(e)
            wait = hint if hint is not None else 2 ** attempt
            wait = min(float(wait), EMBED_BACKOFF_CAP_S)
            print(f"    embed retry {attempt + 1}/{EMBED_MAX_ATTEMPTS} after {wait:.0f}s ({e})")
            time.sleep(wait)
    raise RuntimeError(f"embed_batch failed after {EMBED_MAX_ATTEMPTS} attempts: {last_err}")


# ── text.md 고신호 본문 청크 (로컬 토픽 전용) ─────────────────────────────
# review.md 는 정량 디테일(수치/데이터셋/하이퍼파라미터)을 요약하며 떨군다. A/B 실험
# 결과 매몰 사실 질의 적중률이 review-only 대비 크게 오른다(ai4s 6%→56%, scisci
# 47%→67%) — 일반 질의 회귀는 없었다. 단 원문 발췌라 저작권상 **배포 토픽엔 절대
# 포함하지 않는다**(클라우드 비공개). docs/.assetsignore 로 로컬/배포를 자동 판별.
_TXT_REF_RE = re.compile(r'(?im)^\s*#{0,4}\s*(references|bibliography|참고문헌|acknowledg(e?ments)?)\b')
_TXT_SIGNAL = re.compile(r'(?i)\b(method|approach|propos|algorithm|model|train|fine-?tun|'
                         r'dataset|corpus|experiment|evaluat|result|baseline|ablation|'
                         r'accuracy|precision|recall|f1|auc|benchmark|metric|parameter|'
                         r'hyper-?parameter|we (train|use|evaluate|propose|find|observe|measure|report))\b')
_TXT_NUM = re.compile(r'\b\d+(?:\.\d+)?\s?%|\b\d+\.\d+\b')
TEXTMD_MAX_CHUNKS = 5
TEXTMD_CHAR_BUDGET = 9000


def _text_windows(t, size=1400, overlap=200):
    out, i = [], 0
    while i < len(t):
        out.append(t[i:i + size])
        i += size - overlap
    return out


def textmd_high_signal_chunks(slug: str) -> list:
    """text.md 의 References 이전 본문에서 method/experiment/수치 밀도 상위 윈도우만 추출."""
    p = PAPERS_DIR / slug / "text.md"
    if not p.exists():
        return []
    try:
        t = p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return []
    m = _TXT_REF_RE.search(t)
    if m:
        t = t[:m.start()]
    scored = []
    for w in _text_windows(t):
        s = len(_TXT_SIGNAL.findall(w)) + 0.5 * len(_TXT_NUM.findall(w))
        if s >= 3:
            scored.append((s, w))
    scored.sort(key=lambda x: -x[0])
    out, total = [], 0
    for _, w in scored[:TEXTMD_MAX_CHUNKS]:
        c = clean_chunk_text(w)[:MAX_CHUNK_CHARS]
        if len(c) >= MIN_CHUNK_CHARS:
            out.append(c)
            total += len(c)
        if total >= TEXTMD_CHAR_BUDGET:
            break
    return out


def is_local_topic(topic: str) -> bool:
    """배포(Cloudflare) 제외 토픽인지 — docs/.assetsignore 에 '{topic}/' 가 있으면 로컬."""
    ai = DOCS_DIR / ".assetsignore"
    if not ai.exists():
        return False
    want = f"{topic}/"
    return any(line.strip() == want for line in ai.read_text(encoding="utf-8").splitlines())


def build_index(topic: str, model: str, limit: int | None, dry_run: bool,
                include_text: str = "auto"):
    topic_dir = get_topic_dir(topic)
    if not topic_dir.exists():
        print(f"ERROR: topic dir {topic_dir} does not exist")
        sys.exit(2)

    papers_index_path = get_papers_index_path()
    if not papers_index_path.exists():
        print(f"ERROR: {papers_index_path} not found")
        sys.exit(2)

    all_papers = json.loads(papers_index_path.read_text(encoding="utf-8"))
    topic_papers = [
        p for p in all_papers
        if p.get("primary_topic") == topic or topic in (p.get("topics") or [])
    ]
    print(f"[1/4] Found {len(topic_papers)} papers for topic '{topic}'")

    if limit:
        topic_papers = topic_papers[:limit]
        print(f"      --limit={limit} -> using {len(topic_papers)}")

    # --- text.md 보강 정책: 클라우드=review-only(A), 로컬=review+text(B) ---
    local = is_local_topic(topic)
    if include_text == "auto":
        use_text = local
    elif include_text == "yes":
        if not local:
            print(f"ERROR: --include-text=yes 는 배포(클라우드) 토픽 '{topic}' 에 허용되지 않음 "
                  f"(원문 발췌가 _search_index.json 으로 클라우드에 노출됨). 로컬 토픽에서만 가능.")
            sys.exit(4)
        use_text = True
    else:  # "no"
        use_text = False
    print(f"      [text.md 보강] {'ON — 로컬 토픽(B)' if use_text else 'OFF — review-only(A)'}"
          f"  (local={local})")

    # --- Parse reviews ---
    papers_meta: dict = {}
    pending_chunks: list = []  # each: {slug, section, text}
    skipped = 0
    text_chunk_count = 0
    print("[2/4] Parsing reviews and chunking...")
    for p in topic_papers:
        slug = p["slug"]
        review_path = PAPERS_DIR / slug / "review.md"
        if not review_path.exists():
            skipped += 1
            continue
        parsed = parse_review(review_path, slug)
        if not parsed or not parsed["chunks"]:
            skipped += 1
            continue

        category = (
            (p.get("classifications") or {})
            .get(topic, {})
            .get("primary_category")
            or p.get("primary_category")
            or ""
        )

        # External URL preference: DOI > arXiv > local relative path. The
        # local relative path only works on the live topic page; HTML
        # exports / shared answers need an external URL that resolves
        # from anywhere.
        _doi = (parsed.get("doi") or p.get("doi") or "").strip()
        _arxiv = (parsed.get("arxiv") or p.get("arxiv") or "").strip()
        # Clean placeholder DOIs + extract a mislabeled arXiv id, and fall back
        # to the real Zotero URL so non-DOI papers still get a portable link.
        _doi, _arxiv, _ext_url = _resolve_external(
            parsed.get("title") or p.get("title") or "", _doi, _arxiv)

        papers_meta[slug] = {
            "title": parsed["title"],
            "year": parsed["year"] or p.get("date") or "",
            "category": category,
            "url": f"../papers/{slug}/",         # local (Cloudflare-hosted)
            "external_url": _ext_url,            # DOI/arXiv (portable)
            "authors": parsed.get("authors", []),
            "first_author": parsed.get("first_author", ""),
            "doi": _doi,
            "arxiv": _arxiv,
            "journal": (parsed.get("journal") or "").strip() or "preprint",
            "figures": parsed["figures"],
        }
        for ch in parsed["chunks"]:
            pending_chunks.append({
                "slug": slug,
                "section": ch["section"],
                "text": ch["text"],
            })
        # 로컬 토픽: review 가 떨군 정량 디테일을 text.md 고신호 청크로 보강(B)
        if use_text:
            for _ti, _tc in enumerate(textmd_high_signal_chunks(slug)):
                pending_chunks.append({
                    "slug": slug,
                    "section": f"Detail ({_ti + 1})",
                    "text": _tc,
                })
                text_chunk_count += 1

    print(f"      {len(papers_meta)} papers, {len(pending_chunks)} chunks "
          f"(review {len(pending_chunks) - text_chunk_count} + text.md {text_chunk_count}), {skipped} skipped")

    # --- Index personal notes from docs/notes/{topic}/ (git-ignored) ---
    # These are operator-authored markdown files (hypotheses, meeting notes,
    # gap analyses, etc.) edited in Obsidian or any text editor. They are
    # chunked and embedded alongside paper reviews so Deep Research can
    # cite the operator's own thinking in its answers.
    _notes_dir = DOCS_DIR / "notes" / topic
    _notes_count = 0
    if _notes_dir.exists():
        for _note_path in sorted(_notes_dir.rglob("*.md")):
            if _note_path.name.startswith("_"):
                continue
            try:
                _note_text = _note_path.read_text(encoding="utf-8")
            except Exception:
                continue
            _cleaned = clean_chunk_text(_note_text)
            if len(_cleaned) < MIN_CHUNK_CHARS:
                continue

            _title_m = re.search(r"^#\s+(.+)$", _note_text, re.MULTILINE)
            _title = _title_m.group(1).strip() if _title_m else _note_path.stem.replace("-", " ").replace("_", " ").title()
            _note_slug = f"_note_{_note_path.stem}"

            _rel = _note_path.relative_to(DOCS_DIR / "notes").as_posix()
            papers_meta[_note_slug] = {
                "title": _title,
                "year": "",
                "category": "Personal Notes",
                "url": f"../notes/{_rel}",
                "figures": [],
            }
            # Split into paragraphs (max 5 chunks per note). clean_chunk_text
            # collapses 3+ blank lines to exactly two newlines, so a REAL
            # "\n\n" is the correct separator (not the literal 4-char string).
            _paras = [p.strip() for p in _cleaned.split("\n\n") if len(p.strip()) >= MIN_CHUNK_CHARS]
            if not _paras:
                _paras = [_cleaned]
            for _i, _para in enumerate(_paras[:5]):
                pending_chunks.append({
                    "slug": _note_slug,
                    "section": "Personal Note" if len(_paras) == 1 else f"Personal Note ({_i + 1})",
                    "text": _para[:MAX_CHUNK_CHARS],
                })
            _notes_count += 1
    if _notes_count:
        print(f"      + {_notes_count} personal notes from {_notes_dir}")

    if not pending_chunks:
        print("ERROR: no chunks to embed")
        sys.exit(3)

    total_chars = sum(len(c["text"]) for c in pending_chunks)
    approx_tokens = total_chars // 3  # conservative estimate
    # gemini-embedding-001: $0.15 / 1M input tokens
    print(f"      approx {approx_tokens:,} input tokens ~= ${approx_tokens * 0.00000015:.4f} (gemini-embedding-001)")

    # Cache key per chunk (sha256(model + text)); reused everywhere below.
    for ch in pending_chunks:
        ch["text_sha"] = _chunk_sha(model, ch["text"])

    # --- Content-addressed embedding cache (incremental) ---
    # sha → 양자화된 emb(b64). 이전 index + sidecar 에서 로드한 뒤, 캐시에
    # 없는 chunk 만 Gemini 로 보낸다. dry-run 도 캐시 hit 은 재사용한다.
    sha_to_emb: dict = load_embedding_cache(topic_dir, model)
    miss_chunks = [c for c in pending_chunks if c["text_sha"] not in sha_to_emb]
    n_hit = len(pending_chunks) - len(miss_chunks)
    print(f"      cache: {n_hit} hit / {len(miss_chunks)} miss (of {len(pending_chunks)})")

    # --- Embed (cache misses only) ---
    if dry_run:
        print("[3/4] --dry-run: zero-vectors for cache misses")
        for c in miss_chunks:
            qbytes = quantize_int8_l2([0.0] * 768)
            sha_to_emb[c["text_sha"]] = base64.b64encode(qbytes).decode("ascii")
        dim = 768
    elif not miss_chunks:
        print("[3/4] All chunks served from cache — no API calls")
        dim = 0  # filled in below from any cached vector
    else:
        print(f"[3/4] Embedding {len(miss_chunks)} chunks with {model}...")
        try:
            from google import genai
        except ImportError:
            print("ERROR: google-genai package not installed. Run: pip install google-genai")
            sys.exit(1)

        api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY") or _load_gemini_key_from_config()
        if not api_key:
            print("ERROR: GOOGLE_API_KEY not set (env var or config.json).")
            print("       Set GOOGLE_API_KEY/GEMINI_API_KEY or run 'python pipeline/setup.py' to save it into config.json.")
            sys.exit(1)

        client = genai.Client(api_key=api_key)
        # gemini-embedding-001 은 요청당 최대 100 input 까지 받지만, 한국망
        # 타임아웃·부분실패 노출면을 줄이려 50 으로 둔다.
        BATCH = 50
        t0 = time.time()
        embedded = 0
        for i in range(0, len(miss_chunks), BATCH):
            batch = miss_chunks[i:i + BATCH]
            texts = [c["text"] for c in batch]
            try:
                vecs = embed_batch(client, texts, model)
            except Exception as e:
                # Partial-save: persist everything embedded so far (plus all
                # cache hits) so a later run resumes instead of re-embedding
                # the ~N good batches we already paid for. Do NOT clobber the
                # existing _search_index.json — leave it stale-but-valid.
                save_embedding_cache(topic_dir, model, sha_to_emb)
                remaining = len(miss_chunks) - embedded
                print(f"ERROR: embedding aborted after {embedded}/{len(miss_chunks)} "
                      f"new chunks ({e})")
                print(f"       Saved partial cache to {topic_dir / EMBED_CACHE_NAME}; "
                      f"rerun to resume the remaining {remaining}.")
                sys.exit(4)
            # embed_batch already asserts len(vecs)==len(texts); fold the
            # freshly-embedded (quantized) vectors into the sha→emb map.
            for c, emb in zip(batch, vecs):
                qbytes = quantize_int8_l2(emb)
                sha_to_emb[c["text_sha"]] = base64.b64encode(qbytes).decode("ascii")
            embedded += len(batch)
            done = embedded
            elapsed = time.time() - t0
            rate = done / elapsed if elapsed > 0 else 0
            eta = (len(miss_chunks) - done) / rate if rate > 0 else 0
            print(f"      {done}/{len(miss_chunks)}  ({rate:.1f}/s, ETA {eta:.0f}s)")
        dim = 0  # filled in below

    # dim from the int8 byte length of any cached/embedded vector (1 byte/dim)
    if pending_chunks:
        _sample = sha_to_emb.get(pending_chunks[0]["text_sha"])
        if _sample:
            dim = len(base64.b64decode(_sample))
    print(f"      dim={dim}")

    # --- Assemble JSON (every chunk's emb must now be present) ---
    print("[4/4] Assembling and writing JSON...")
    # Loud guard: no pending chunk may be missing its embedding, otherwise
    # the index would silently ship misaligned/short.
    missing = [c["text_sha"] for c in pending_chunks if c["text_sha"] not in sha_to_emb]
    if missing:
        print(f"ERROR: {len(missing)} chunk(s) have no embedding after embed pass — aborting")
        sys.exit(4)

    # 임베딩은 JSON 이 아니라 바이너리 사이드카(.bin)로 분리한다.
    # 이유 (cold-load 최적화, 2026-06-12): emb(b64) 가 인덱스 JSON 의 ~64% 를
    # 차지해 JSON.parse 가 무겁고, 쿼리마다 per-chunk atob 디코드 비용도 컸다.
    # .bin 은 chunk 순서대로 dim 바이트씩 — 브라우저가 ArrayBuffer 로 받아
    # Int8Array 뷰만 만들면 파싱 0ms. (구형 chunk.emb 포맷은 클라이언트가
    # 계속 지원하므로 미재빌드 토픽도 동작.)
    out_chunks = []
    emb_blob = bytearray()
    for chunk in pending_chunks:
        raw = base64.b64decode(sha_to_emb[chunk["text_sha"]])
        if len(raw) != dim:
            print(f"ERROR: embedding byte length {len(raw)} != dim {dim} "
                  f"(sha {chunk['text_sha'][:12]}) — aborting")
            sys.exit(4)
        emb_blob.extend(raw)
        out_chunks.append({
            "slug": chunk["slug"],
            "section": chunk["section"],
            "text": chunk["text"],
            "text_sha": chunk["text_sha"],   # self-describing cache key
        })
    assert len(out_chunks) == len(pending_chunks), (
        f"out_chunks {len(out_chunks)} != pending_chunks {len(pending_chunks)}"
    )
    assert len(emb_blob) == dim * len(out_chunks), (
        f"emb blob {len(emb_blob)}B != dim {dim} × {len(out_chunks)} chunks"
    )

    out = {
        "model": model,
        "dim": dim,
        "quant": "int8-l2norm",
        "count": len(out_chunks),
        "emb_file": EMB_BIN_NAME,
        "papers": papers_meta,
        "chunks": out_chunks,
    }
    source_fp, source_count = source_fingerprint(topic, papers_meta)
    out["source_fingerprint"] = source_fp
    out["source_file_count"] = source_count
    out["built_at"] = int(time.time())

    bin_path = topic_dir / EMB_BIN_NAME
    bin_path.write_bytes(bytes(emb_blob))
    out_path = topic_dir / "_search_index.json"
    out_path.write_text(
        json.dumps(out, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    size_kb = out_path.stat().st_size // 1024
    bin_kb = bin_path.stat().st_size // 1024
    print(f"      wrote {out_path} ({size_kb:,} KB) + {EMB_BIN_NAME} ({bin_kb:,} KB)")

    # Refresh the sidecar cache so the next build resumes from real vectors.
    # Skip on dry-run — its zero-vectors must never poison the cache.
    if not dry_run:
        # Keep only shas that are part of this build (prune drifted entries).
        live = {c["text_sha"]: sha_to_emb[c["text_sha"]] for c in pending_chunks}
        save_embedding_cache(topic_dir, model, live)
    print("Done.")


def _run_search_index(topic, *, model="gemini-embedding-001", limit=None, dry_run=False,
                      include_text="auto"):
    """Programmatic entrypoint for build_search_index."""
    return build_index(topic, model, limit, dry_run, include_text=include_text)


def main():
    parser = argparse.ArgumentParser(description="Build Deep Research search index")
    parser.add_argument("--topic", required=True, help="topic alias (e.g. ai4s, scisci)")
    parser.add_argument("--model", default="gemini-embedding-001")
    parser.add_argument("--limit", type=int, default=None, help="limit number of papers (debug)")
    parser.add_argument("--dry-run", action="store_true", help="chunk only, no API calls")
    parser.add_argument("--include-text", choices=["auto", "yes", "no"], default="auto",
                        help="text.md 고신호 청크 보강. auto=로컬 토픽만 ON(클라우드 review-only). "
                             "yes 는 배포 토픽에 거부됨(저작권).")
    args = parser.parse_args()
    _run_search_index(topic=args.topic, model=args.model, limit=args.limit,
                      dry_run=args.dry_run, include_text=args.include_text)


if __name__ == "__main__":
    from _env_guard import force_py312
    force_py312()
    main()
