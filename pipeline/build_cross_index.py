#!/usr/bin/env python3
"""Cross-topic 통합 Deep/Deeper Research 콘솔 (로컬 전용).

여러 토픽의 Deep Research 검색 인덱스와 연결 그래프(``_paper_connections.json``)를
**slug 기준 dedup 병합**해 ``docs/_cross/`` 에 쓰고, build_topic_index 의 검증된 DR
클라이언트를 그대로 재사용해 ``docs/_cross/index.html`` 을 만든다.

- 병합 규칙: 같은 논문(slug)이 여러 토픽에 있으면 **청크 수가 가장 많은(=본문 청크까지 포함한)
  버전**을 채택. ``ai4s+scisci`` 처럼 ``ai4s`` / ``scisci`` 와 겹치는 통합 토픽도 dedup 으로 자동 흡수.
- ``--mode hybrid`` (기본): dense sidecar 를 함께 병합. BM25 source 가 하나라도 있으면 쓰기 전에 중단.
- ``--mode bm25``: source JSON 의 본문만 병합하며 embedding sidecar 를 읽거나 쓰지 않음.
- 연결 그래프: slug 별 edge union + (target-slug, relation) dedup. 코퍼스에 존재하는 target 만 유지
  (Deeper 확장이 항상 resolve 되도록).
- **배포 금지**: ``docs/.assetsignore`` 에 ``_cross/`` 를 자동 등록한다 (Cloudflare 로 안 나감).
- 열람: ``python pipeline/serve_local.py`` → ``http://localhost:8000/_cross/``

Usage:
    PYTHONUTF8=1 python pipeline/build_cross_index.py                # 모든 토픽 자동 병합
    PYTHONUTF8=1 python pipeline/build_cross_index.py --mode bm25    # Google-free sparse 병합
    PYTHONUTF8=1 python pipeline/build_cross_index.py --topics ai4s scisci humanoid physical-ai
    PYTHONUTF8=1 python pipeline/build_cross_index.py --no-page      # 데이터만 병합, HTML 생략
"""
import argparse
import hashlib
import json
import os
import sys
import time
from pathlib import Path

PIPELINE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(PIPELINE_DIR))
from config_loader import DOCS_DIR, PROJECT_ROOT, load_config

CROSS_NAME = "_cross"
SEARCH_INDEX = "_search_index.json"
EMB_BIN = "_search_index_emb.bin"
CONN = "_paper_connections.json"
CROSS_META = "_cross_meta.json"

# 병합 대상에서 제외 (컨텐츠 토픽이 아니거나 인덱스가 없는 디렉토리)
_SKIP_DIRS = {"papers", "public", "notes", CROSS_NAME}
_MODES = ("hybrid", "bm25")


def discover_topics() -> list[str]:
    """docs/ 아래 검색 인덱스를 가진 토픽 디렉토리를 mtime 무관, 이름순으로."""
    out = []
    for d in sorted(DOCS_DIR.iterdir()):
        if not d.is_dir() or d.name.startswith("."):
            continue
        if d.name in _SKIP_DIRS:
            continue
        if (d / SEARCH_INDEX).exists():
            out.append(d.name)
    return out


def _validate_source_index(topic: str, index: dict) -> str:
    """Validate one source JSON and return its effective retrieval mode."""
    if not isinstance(index, dict):
        raise SystemExit(f"[cross] {topic}: 검색 인덱스 JSON root 는 object 여야 합니다")

    chunks = index.get("chunks")
    papers = index.get("papers")
    if not isinstance(chunks, list):
        raise SystemExit(f"[cross] {topic}: chunks 가 array 가 아닙니다")
    if type(index.get("count")) is not int or index["count"] != len(chunks):
        raise SystemExit(
            f"[cross] {topic}: count {index.get('count')!r} != chunks {len(chunks)}"
        )
    if not isinstance(papers, dict):
        raise SystemExit(f"[cross] {topic}: papers 가 object 가 아닙니다")
    for pos, chunk in enumerate(chunks):
        if not isinstance(chunk, dict):
            raise SystemExit(f"[cross] {topic}: chunk {pos} 가 object 가 아닙니다")
        slug = chunk.get("slug")
        if not isinstance(slug, str) or not slug:
            raise SystemExit(f"[cross] {topic}: chunk {pos} 의 slug 가 유효하지 않습니다")
        if not isinstance(chunk.get("text"), str):
            raise SystemExit(f"[cross] {topic}: chunk {pos} 의 text 가 문자열이 아닙니다")
        if slug not in papers:
            raise SystemExit(
                f"[cross] {topic}: chunk {pos} 의 slug {slug!r} 가 papers 에 없습니다"
            )

    retrieval_mode = index.get("retrieval_mode")
    if retrieval_mode == "bm25":
        problems = []
        if "model" not in index or index["model"] is not None:
            problems.append("model=null")
        if type(index.get("dim")) is not int or index["dim"] != 0:
            problems.append("dim=0")
        if "quant" not in index or index["quant"] is not None:
            problems.append("quant=null")
        if "emb_file" in index:
            problems.append("emb_file absent")
        for pos, chunk in enumerate(chunks):
            if "emb" in chunk:
                problems.append(f"chunks[{pos}].emb absent")
                break
            if not all(isinstance(chunk.get(key), str)
                       for key in ("slug", "section", "text", "text_sha")):
                problems.append(
                    f"chunks[{pos}] requires string slug/section/text/text_sha"
                )
                break
        if problems:
            raise SystemExit(
                f"[cross] {topic}: malformed bm25 metadata "
                f"({', '.join(problems)})"
            )
        return "bm25"

    if retrieval_mode not in (None, "hybrid"):
        raise SystemExit(
            f"[cross] {topic}: 지원하지 않는 retrieval_mode {retrieval_mode!r}"
        )

    model = index.get("model")
    dim = index.get("dim")
    if not isinstance(model, str) or not model.strip():
        raise SystemExit(f"[cross] {topic}: 유효한 임베딩 모델 정보가 없습니다")
    if type(dim) is not int or dim <= 0:
        raise SystemExit(f"[cross] {topic}: 유효하지 않은 임베딩 차원 {dim!r}")
    if index.get("quant") != "int8-l2norm":
        raise SystemExit(
            f"[cross] {topic}: 지원하지 않는 양자화 {index.get('quant')!r}; "
            "build_search_index --mode hybrid 로 int8-l2norm 인덱스를 재빌드하세요."
        )
    if retrieval_mode == "hybrid":
        emb_file = index.get("emb_file")
        if not isinstance(emb_file, str) or not emb_file.strip():
            raise SystemExit(
                f"[cross] {topic}: hybrid 인덱스의 emb_file 정보가 없습니다"
            )
    return "hybrid"


def _load_source_indexes(topics: list[str], mode: str) -> list[dict]:
    """Read and validate every source JSON before any vector or output I/O."""
    if mode not in _MODES:
        raise ValueError(f"unsupported cross-index mode: {mode!r}")

    sources = []
    for topic in topics:
        if topic in _SKIP_DIRS:
            raise SystemExit(f"[cross] {topic}: 병합 대상이 될 수 없는 reserved directory 입니다")
        index_path = DOCS_DIR / topic / SEARCH_INDEX
        if not index_path.is_file():
            raise SystemExit(
                f"[cross] {topic}: {SEARCH_INDEX} 없음 — source 를 건너뛰지 않고 중단합니다"
            )
        index_bytes = index_path.read_bytes()
        try:
            index = json.loads(index_bytes)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise SystemExit(f"[cross] {topic}: 유효하지 않은 검색 인덱스 JSON: {exc}") from exc
        source_mode = _validate_source_index(topic, index)
        sources.append({
            "topic": topic,
            "index": index,
            "index_bytes": index_bytes,
            "retrieval_mode": source_mode,
        })

    if mode == "hybrid":
        sparse_topics = [s["topic"] for s in sources if s["retrieval_mode"] == "bm25"]
        if sparse_topics:
            joined = ", ".join(sparse_topics)
            raise SystemExit(
                f"[cross] hybrid 모드는 BM25 source 를 병합할 수 없습니다: {joined}. "
                "content-only 통합은 --mode bm25 를 사용하거나, 해당 source 를 "
                "build_search_index --mode hybrid 로 재빌드하세요."
            )
    else:
        missing_fingerprints = [
            s["topic"] for s in sources
            if not isinstance(s["index"].get("source_fingerprint"), str)
            or not s["index"]["source_fingerprint"].strip()
        ]
        if missing_fingerprints:
            raise SystemExit(
                "[cross] bm25 source fingerprint 누락: "
                + ", ".join(missing_fingerprints)
                + ". 각 source index 를 원래 mode 로 재빌드한 뒤 다시 병합하세요."
            )
    return sources


def _bm25_chunk(chunk: dict) -> dict:
    """Return the public sparse chunk contract, recomputing its text hash."""
    text = chunk["text"]
    return {
        "slug": chunk["slug"],
        "section": chunk.get("section") or "",
        "text": text,
        "text_sha": hashlib.sha256(text.encode("utf-8")).hexdigest(),
    }


def merge_indexes(topics: list[str], mode: str = "hybrid"):
    """Slug-dedup merge.

    Returns ``(index, embedding_bytes, per_topic_paper_counts)``. BM25 mode
    intentionally returns ``b""`` and never opens an embedding sidecar.
    """
    sources = _load_source_indexes(topics, mode)
    model = None
    dim = None
    best: dict[str, dict] = {}   # slug -> {n, chunks, emb, meta, topic}
    order: list[str] = []        # slug 최초 등장 순서
    topic_paper_counts: dict[str, int] = {}
    source_indexes: dict[str, dict] = {}

    for source in sources:
        t = source["topic"]
        tdir = DOCS_DIR / t
        idx_bytes = source["index_bytes"]
        idx = source["index"]
        chunks = idx.get("chunks", [])
        emb = b""
        if mode == "hybrid":
            tmodel = idx["model"]
            tdim = idx["dim"]
            if model is None:
                model, dim = tmodel, tdim
            elif tmodel != model or tdim != dim:
                raise SystemExit(
                    f"[cross] 임베딩 모델/차원 불일치: {t} 는 {tmodel}/{tdim}, "
                    f"기준은 {model}/{dim}. 동일 모델로 재빌드 후 병합하세요."
                )
            emb_name = idx.get("emb_file") or EMB_BIN
            emb_path = tdir / emb_name
            if not emb_path.is_file():
                raise SystemExit(f"[cross] {t}: embedding sidecar 없음: {emb_name}")
            emb = emb_path.read_bytes()
            if len(emb) != len(chunks) * dim:
                raise SystemExit(
                    f"[cross] {t}: emb 사이드카 {len(emb)}B != "
                    f"count*dim {len(chunks) * dim}B "
                    "— build_search_index --mode hybrid 로 재빌드하세요."
                )
        tpapers = idx.get("papers", {}) or {}
        topic_paper_counts[t] = len(tpapers)
        source_indexes[t] = {
            "retrieval_mode": source["retrieval_mode"],
            "source_fingerprint": idx.get("source_fingerprint"),
            "index_sha256": hashlib.sha256(idx_bytes).hexdigest(),
            "count": len(chunks),
        }
        if mode == "hybrid":
            source_indexes[t]["embedding_sha256"] = hashlib.sha256(emb).hexdigest()

        by_slug: dict[str, list[int]] = {}
        for i, c in enumerate(chunks):
            by_slug.setdefault(c["slug"], []).append(i)

        for slug, idxs in by_slug.items():
            n = len(idxs)
            if slug not in best:
                order.append(slug)
            if slug not in best or n > best[slug]["n"]:
                best[slug] = {
                    "n": n,
                    "chunks": [
                        _bm25_chunk(chunks[i]) if mode == "bm25" else chunks[i]
                        for i in idxs
                    ],
                    "emb": (
                        b"".join(emb[i * dim:(i + 1) * dim] for i in idxs)
                        if mode == "hybrid" else b""
                    ),
                    "meta": tpapers.get(slug),
                    "topic": t,
                }

    if not order:
        raise SystemExit("[cross] 병합할 청크가 없습니다 — 대상 토픽에 검색 인덱스가 있는지 확인하세요.")

    merged_chunks: list[dict] = []
    merged_emb = bytearray()
    papers: dict[str, dict] = {}
    for slug in order:
        b = best[slug]
        merged_chunks.extend(b["chunks"])
        if mode == "hybrid":
            merged_emb += b["emb"]
        if b["meta"] is not None:
            papers[slug] = b["meta"]

    if mode == "hybrid" and len(merged_emb) != len(merged_chunks) * dim:
        raise SystemExit(
            f"[cross] 병합 emb {len(merged_emb)}B != count*dim {len(merged_chunks) * dim}B (내부 오류)"
        )

    out = {
        "retrieval_mode": mode,
        "model": model if mode == "hybrid" else None,
        "dim": dim if mode == "hybrid" else 0,
        "quant": "int8-l2norm" if mode == "hybrid" else None,
        "count": len(merged_chunks),
        "papers": papers,
        "chunks": merged_chunks,
    }
    if mode == "hybrid":
        out["emb_file"] = EMB_BIN
    source_payload = json.dumps(
        source_indexes, ensure_ascii=False, sort_keys=True,
        separators=(",", ":")).encode("utf-8")
    out["source_fingerprint"] = hashlib.sha256(source_payload).hexdigest()
    out["source_indexes"] = source_indexes
    out["source_file_count"] = len(source_indexes)
    out["built_at"] = int(time.time())
    return out, bytes(merged_emb), topic_paper_counts


def merge_connections(topics: list[str], keep_slugs: set[str]) -> dict:
    """slug 별 edge union + (target, relation) dedup. 코퍼스 내 target 만 유지."""
    merged: dict[str, list] = {}
    for t in topics:
        p = DOCS_DIR / t / CONN
        if not p.exists():
            continue
        conn = json.loads(p.read_text(encoding="utf-8"))
        for slug, edges in conn.items():
            if slug not in keep_slugs or not isinstance(edges, list):
                continue
            bucket = merged.setdefault(slug, [])
            seen = {(e.get("slug"), e.get("relation")) for e in bucket}
            for e in edges:
                tgt = e.get("slug")
                if tgt not in keep_slugs:
                    continue  # 병합 코퍼스 밖 target → Deeper 가 resolve 못 함, 버림
                key = (tgt, e.get("relation"))
                if key in seen:
                    continue
                bucket.append(e)
                seen.add(key)
    return merged


def ensure_assetsignore():
    """docs/.assetsignore 에 '_cross/' 등록 (배포 제외)."""
    ai = DOCS_DIR / ".assetsignore"
    want = f"{CROSS_NAME}/"
    lines = ai.read_text(encoding="utf-8").splitlines() if ai.exists() else []
    if any(ln.strip() == want for ln in lines):
        return
    block = ["", "# Cross-topic 통합 Deep Research (로컬 전용)", want]
    with ai.open("a", encoding="utf-8") as f:
        f.write(("\n" if lines and lines[-1].strip() else "") + "\n".join(block) + "\n")
    print(f"[cross] .assetsignore 에 '{want}' 추가 (배포 제외)")


def _atomic_write(path: Path, payload: bytes) -> None:
    """Replace one artifact atomically without exposing a partial file."""
    tmp = path.with_name(f".{path.name}.{os.getpid()}.{time.time_ns()}.tmp")
    try:
        tmp.write_bytes(payload)
        os.replace(tmp, path)
    finally:
        if tmp.exists():
            tmp.unlink()


def _atomic_write_json(path: Path, value, *, indent=None) -> None:
    payload = json.dumps(
        value, ensure_ascii=False, indent=indent,
        separators=None if indent is not None else (",", ":"),
    ).encode("utf-8")
    _atomic_write(path, payload)


def build_cross(topics, title, make_page=True, mode="hybrid"):
    collections = load_config().get("zotero", {}).get("collections", {})

    print(f"[cross] 병합 토픽 ({mode}): {', '.join(topics)}")
    index, emb, topic_counts = merge_indexes(topics, mode=mode)
    keep = set(index["papers"].keys())
    conns = merge_connections(topics, keep)

    meta = {
        "title": title,
        "paper_count": len(index["papers"]),
        "chunk_count": index["count"],
        "topic_count": len([t for t in topics if topic_counts.get(t)]),
        "topics": [
            {"slug": t, "title": collections.get(t, t), "papers": topic_counts.get(t, 0)}
            for t in topics if topic_counts.get(t)
        ],
    }

    # Validation and all source reads finish before the first _cross mutation.
    cross_dir = DOCS_DIR / CROSS_NAME
    cross_dir.mkdir(parents=True, exist_ok=True)
    if mode == "hybrid":
        _atomic_write(cross_dir / EMB_BIN, emb)
    _atomic_write_json(cross_dir / SEARCH_INDEX, index)
    _atomic_write_json(cross_dir / CONN, conns)
    _atomic_write_json(cross_dir / CROSS_META, meta, indent=2)

    print(f"[cross] 병합 완료: {meta['paper_count']}편 / {index['count']}청크 / "
          f"연결 {len(conns)}개 slug → {cross_dir}")

    ensure_assetsignore()

    if make_page:
        import build_topic_index
        # cross 페이지는 공유 Zotero 키 파일을 재생성할 필요 없음 (per-topic 빌드가 담당).
        os.environ.setdefault("SKIP_ZOTERO_KEYS", "1")
        build_topic_index._run_topic_index(CROSS_NAME, cross=meta)
        print(f"[cross] 페이지: {cross_dir / 'index.html'}  (serve_local → /_cross/)")
    return meta


def main():
    parser = argparse.ArgumentParser(description="Cross-topic 통합 Deep/Deeper Research 콘솔 빌드 (로컬 전용)")
    parser.add_argument("--topics", nargs="*", default=None,
                        help="병합할 토픽 (기본: docs/ 아래 검색 인덱스를 가진 모든 토픽)")
    parser.add_argument("--mode", choices=_MODES, default="hybrid",
                        help="retrieval mode (기본: hybrid; Google-free: bm25)")
    parser.add_argument("--title", default="통합 Deep Research",
                        help="페이지 제목 (기본: '통합 Deep Research')")
    parser.add_argument("--no-page", action="store_true", help="데이터만 병합하고 HTML 생성은 생략")
    args = parser.parse_args()

    topics = args.topics if args.topics else discover_topics()
    if not topics:
        raise SystemExit("[cross] 대상 토픽이 없습니다. 먼저 build_search_index 로 토픽 인덱스를 만드세요.")

    build_cross(topics, args.title, make_page=not args.no_page, mode=args.mode)


if __name__ == "__main__":
    from _env_guard import force_py312
    force_py312()
    main()
