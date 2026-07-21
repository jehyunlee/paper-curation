#!/usr/bin/env python3
"""Cross-topic 통합 Deep/Deeper Research 콘솔 (로컬 전용).

여러 토픽의 Deep Research 검색 인덱스(``_search_index.json`` + ``_search_index_emb.bin``)와
연결 그래프(``_paper_connections.json``)를 **slug 기준 dedup 병합**해 ``docs/_cross/`` 에 쓰고,
build_topic_index 의 검증된 DR 클라이언트를 그대로 재사용해 ``docs/_cross/index.html`` 을 만든다.

- 병합 규칙: 같은 논문(slug)이 여러 토픽에 있으면 **청크 수가 가장 많은(=본문 청크까지 포함한)
  버전**을 채택. ``ai4s+scisci`` 처럼 ``ai4s`` / ``scisci`` 와 겹치는 통합 토픽도 dedup 으로 자동 흡수.
- 연결 그래프: slug 별 edge union + (target-slug, relation) dedup. 코퍼스에 존재하는 target 만 유지
  (Deeper 확장이 항상 resolve 되도록).
- **배포 금지**: ``docs/.assetsignore`` 에 ``_cross/`` 를 자동 등록한다 (Cloudflare 로 안 나감).
- 열람: ``python pipeline/serve_local.py`` → ``http://localhost:8000/_cross/``

Usage:
    PYTHONUTF8=1 python pipeline/build_cross_index.py                # 모든 토픽 자동 병합
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


def discover_topics() -> list[str]:
    """docs/ 아래 검색 인덱스를 가진 토픽 디렉토리를 mtime 무관, 이름순으로."""
    out = []
    for d in sorted(DOCS_DIR.iterdir()):
        if not d.is_dir() or d.name.startswith("."):
            continue
        if d.name in _SKIP_DIRS:
            continue
        if (d / SEARCH_INDEX).exists() and (d / EMB_BIN).exists():
            out.append(d.name)
    return out


def merge_indexes(topics: list[str]):
    """slug-dedup 병합. 반환: (merged_index_dict, merged_emb_bytes, per_topic_paper_counts)."""
    model = None
    dim = None
    best: dict[str, dict] = {}   # slug -> {n, chunks, emb, meta, topic}
    order: list[str] = []        # slug 최초 등장 순서
    topic_paper_counts: dict[str, int] = {}
    source_indexes: dict[str, dict] = {}

    for t in topics:
        tdir = DOCS_DIR / t
        idx_path = tdir / SEARCH_INDEX
        emb_path = tdir / EMB_BIN
        if not idx_path.exists() or not emb_path.exists():
            print(f"[cross] skip {t}: 검색 인덱스 없음")
            continue
        idx_bytes = idx_path.read_bytes()
        idx = json.loads(idx_bytes)
        tmodel = idx.get("model")
        tdim = int(idx.get("dim") or 0)
        if not isinstance(tmodel, str) or not tmodel.strip():
            raise SystemExit(f"[cross] {t}: 유효한 임베딩 모델 정보가 없습니다")
        tquant = idx.get("quant")
        if tdim <= 0:
            raise SystemExit(f"[cross] {t}: 유효하지 않은 임베딩 차원 {tdim}")
        if tquant != "int8-l2norm":
            raise SystemExit(
                f"[cross] {t}: 지원하지 않는 양자화 {tquant!r}; "
                "build_search_index 로 int8-l2norm 인덱스를 재빌드하세요."
            )
        if model is None:
            model, dim = tmodel, tdim
        elif tmodel != model or tdim != dim:
            raise SystemExit(
                f"[cross] 임베딩 모델/차원 불일치: {t} 는 {tmodel}/{tdim}, 기준은 {model}/{dim}. "
                "동일 모델로 재빌드 후 병합하세요."
            )
        chunks = idx.get("chunks", [])
        emb = emb_path.read_bytes()
        if len(emb) != len(chunks) * dim:
            raise SystemExit(
                f"[cross] {t}: emb 사이드카 {len(emb)}B != count*dim {len(chunks) * dim}B "
                "— build_search_index 로 재빌드하세요."
            )
        tpapers = idx.get("papers", {}) or {}
        topic_paper_counts[t] = len(tpapers)
        source_indexes[t] = {
            "source_fingerprint": idx.get("source_fingerprint"),
            "index_sha256": hashlib.sha256(idx_bytes).hexdigest(),
            "embedding_sha256": hashlib.sha256(emb).hexdigest(),
            "count": len(chunks),
        }

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
                    "chunks": [chunks[i] for i in idxs],
                    "emb": b"".join(emb[i * dim:(i + 1) * dim] for i in idxs),
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
        merged_emb += b["emb"]
        if b["meta"] is not None:
            papers[slug] = b["meta"]

    if len(merged_emb) != len(merged_chunks) * dim:
        raise SystemExit(
            f"[cross] 병합 emb {len(merged_emb)}B != count*dim {len(merged_chunks) * dim}B (내부 오류)"
        )

    out = {
        "model": model,
        "dim": dim,
        "quant": "int8-l2norm",
        "count": len(merged_chunks),
        "emb_file": EMB_BIN,
        "papers": papers,
        "chunks": merged_chunks,
    }
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


def build_cross(topics, title, make_page=True):
    collections = load_config().get("zotero", {}).get("collections", {})
    cross_dir = DOCS_DIR / CROSS_NAME
    cross_dir.mkdir(parents=True, exist_ok=True)

    print(f"[cross] 병합 토픽: {', '.join(topics)}")
    index, emb, topic_counts = merge_indexes(topics)
    keep = set(index["papers"].keys())
    conns = merge_connections(topics, keep)

    (cross_dir / SEARCH_INDEX).write_text(
        json.dumps(index, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    (cross_dir / EMB_BIN).write_bytes(emb)
    (cross_dir / CONN).write_text(
        json.dumps(conns, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

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
    (cross_dir / CROSS_META).write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

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
    parser.add_argument("--title", default="통합 Deep Research",
                        help="페이지 제목 (기본: '통합 Deep Research')")
    parser.add_argument("--no-page", action="store_true", help="데이터만 병합하고 HTML 생성은 생략")
    args = parser.parse_args()

    topics = args.topics if args.topics else discover_topics()
    if not topics:
        raise SystemExit("[cross] 대상 토픽이 없습니다. 먼저 build_search_index 로 토픽 인덱스를 만드세요.")

    build_cross(topics, args.title, make_page=not args.no_page)


if __name__ == "__main__":
    from _env_guard import force_py312
    force_py312()
    main()
