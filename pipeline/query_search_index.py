#!/usr/bin/env python3
"""Read-only retrieval over the Deep Research search-index sidecars.

The scoring intentionally mirrors the browser implementation in
``build_topic_index.py``: ASCII alphanumeric tokens plus Hangul character
bigrams, BM25 (k1=1.5, b=0.75), int8 / 127 document-vector normalization,
and zero-based-rank RRF (k=60).  Querying never builds or changes an index.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import struct
from collections import Counter
from pathlib import Path
from typing import Any, Sequence

BM25_K1 = 1.5
BM25_B = 0.75
RRF_K = 60
MAX_CHUNKS_PER_PAPER = 3
_ASCII_RE = re.compile(r"[a-z0-9]+")
_HANGUL_RE = re.compile(r"[\uAC00-\uD7AF\u1100-\u11FF\u3130-\u318F]+")


def tokenize(text: str) -> list[str]:
    """Mirror browser ``deepTokenize`` for English and Korean text."""
    text = str(text or "").lower()
    tokens = _ASCII_RE.findall(text)
    for run in _HANGUL_RE.findall(text):
        if len(run) == 1:
            tokens.append(run)
        else:
            tokens.extend(run[index:index + 2] for index in range(len(run) - 1))
    return tokens


def _default_docs_dir() -> Path:
    return Path(__file__).resolve().parent.parent / "docs"


def _topic_dir(topic: str, docs_dir: str | Path | None) -> Path:
    root = Path(docs_dir) if docs_dir is not None else _default_docs_dir()
    root = root.resolve()
    candidate = (root / topic).resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"topic must be under docs directory: {topic!r}") from exc
    if not candidate.is_dir():
        raise FileNotFoundError(f"search-index topic directory not found: {candidate}")
    return candidate


def _load_index(topic: str, docs_dir: str | Path | None) -> tuple[dict[str, Any], Path]:
    topic_dir = _topic_dir(topic, docs_dir)
    index_path = topic_dir / "_search_index.json"
    if not index_path.is_file():
        raise FileNotFoundError(f"search index not found: {index_path}")
    try:
        index = json.loads(index_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid search index JSON: {index_path}: {exc.msg}") from exc
    if not isinstance(index, dict):
        raise ValueError(f"invalid search index: {index_path} must contain an object")
    chunks = index.get("chunks")
    if not isinstance(chunks, list):
        raise ValueError("invalid search index: chunks must be a list")
    count, dim = index.get("count"), index.get("dim")
    if not isinstance(count, int) or isinstance(count, bool) or count < 0:
        raise ValueError("invalid search index: count must be a non-negative integer")
    if not isinstance(dim, int) or isinstance(dim, bool) or dim <= 0:
        raise ValueError("invalid search index: dim must be a positive integer")
    if count != len(chunks):
        raise ValueError(f"search index count mismatch: count={count}, chunks={len(chunks)}")
    if not isinstance(index.get("papers"), dict):
        raise ValueError("invalid search index: papers must be an object")
    return index, topic_dir


def _load_embedding_bytes(index: dict[str, Any], topic_dir: Path) -> bytes:
    """Validate and return the compact signed-int8 sidecar unchanged."""
    emb_file = index.get("emb_file")
    if not isinstance(emb_file, str) or not emb_file:
        raise FileNotFoundError("dense retrieval requires search index emb_file sidecar")
    sidecar = (topic_dir / emb_file).resolve()
    try:
        sidecar.relative_to(topic_dir.resolve())
    except ValueError as exc:
        raise ValueError(f"embedding sidecar must be inside topic directory: {emb_file!r}") from exc
    if not sidecar.is_file():
        raise FileNotFoundError(f"embedding sidecar not found: {sidecar}")
    raw = sidecar.read_bytes()
    expected = index["count"] * index["dim"]
    if len(raw) != expected:
        raise ValueError(
            f"embedding sidecar size mismatch: {len(raw)} != {expected} bytes "
            "(count * dim)"
        )
    return raw


def _dense_scores(raw: bytes, dim: int, query_vector: list[float],
                  eligible: list[int]) -> dict[int, float]:
    """Cosine scores directly over int8 bytes without expanding all vectors.

    The `/127` factor cancels between dot product and document norm. Memory
    therefore remains the sidecar size (~27 MB for `_cross`), rather than
    hundreds of MB of Python float/list objects.
    """
    scores: dict[int, float] = {}
    fmt = f"{dim}b"
    for position in eligible:
        values = struct.unpack_from(fmt, raw, position * dim)
        norm = math.sqrt(sum(value * value for value in values)) or 1.0
        scores[position] = sum(
            query_vector[i] * value for i, value in enumerate(values)
        ) / norm
    return scores


def _normalize_query_vector(query_vector: Sequence[float], dim: int) -> list[float]:
    if isinstance(query_vector, (str, bytes)):
        raise ValueError("query_vector must be a numeric sequence")
    try:
        vector = [float(value) for value in query_vector]
    except (TypeError, ValueError) as exc:
        raise ValueError("query_vector must be a numeric sequence") from exc
    if len(vector) != dim:
        raise ValueError(f"query vector dimension mismatch: {len(vector)} != index dim {dim}")
    if not all(math.isfinite(value) for value in vector):
        raise ValueError("query_vector must contain only finite values")
    norm = math.sqrt(sum(value * value for value in vector))
    if norm == 0:
        raise ValueError("query_vector must not be all zeros")
    return [value / norm for value in vector]


def _embed_query(query: str, dim: int) -> list[float]:
    # Deferred import keeps BM25-only imports and queries free of key lookup/network work.
    try:
        from serve_local import gemini_embed, resolve_google_key
    except ImportError:  # Supports ``import pipeline.query_search_index`` as well as script use.
        from pipeline.serve_local import gemini_embed, resolve_google_key
    key = resolve_google_key()
    if not key:
        raise ValueError("dense retrieval requires GOOGLE_API_KEY or GEMINI_API_KEY")
    return _normalize_query_vector(gemini_embed(query, key), dim)


def _build_bm25(chunks: list[dict[str, Any]], query_terms: list[str]
                ) -> tuple[list[Counter[str]], list[int], dict[str, float], float]:
    """Build only query-term TF/DF, sufficient for one-shot CLI BM25.

    The browser caches every term for repeated interactive queries. A CLI call
    has one query, so retaining all corpus terms would waste substantial memory
    on `_cross` while producing identical scores.
    """
    wanted = set(query_terms)
    documents: list[Counter[str]] = []
    lengths: list[int] = []
    document_frequency: Counter[str] = Counter()
    for chunk in chunks:
        terms = tokenize(chunk.get("text", ""))
        frequencies = Counter(term for term in terms if term in wanted)
        documents.append(frequencies)
        lengths.append(len(terms))
        document_frequency.update(frequencies.keys())
    count = len(chunks)
    idf = {
        term: math.log(1 + (count - frequency + 0.5) / (frequency + 0.5))
        for term, frequency in document_frequency.items()
    }
    return documents, lengths, idf, sum(lengths) / (count or 1)


def _bm25_score(tf: Counter[str], length: int, idf: dict[str, float], average_length: float,
                query_terms: list[str]) -> float:
    score = 0.0
    for term in set(query_terms):  # Browser deliberately does not repeat-weight query terms.
        frequency = tf.get(term, 0)
        if frequency:
            score += idf.get(term, 0.0) * (frequency * (BM25_K1 + 1)) / (
                frequency + BM25_K1 * (1 - BM25_B + BM25_B * length / (average_length or 1))
            )
    return score


def _eligible_indexes(index: dict[str, Any], min_year: int | None, max_year: int | None) -> list[int]:
    if min_year is not None and max_year is not None and min_year > max_year:
        raise ValueError("min_year must not be greater than max_year")
    eligible: list[int] = []
    papers = index["papers"]
    for position, chunk in enumerate(index["chunks"]):
        if not isinstance(chunk, dict):
            continue
        paper = papers.get(chunk.get("slug"))
        if not isinstance(paper, dict):
            continue
        if min_year is not None or max_year is not None:
            try:
                year = int(paper.get("year"))
            except (TypeError, ValueError):
                continue
            if (min_year is not None and year < min_year) or (max_year is not None and year > max_year):
                continue
        eligible.append(position)
    return eligible


def _rank(scores: dict[int, float], eligible: list[int]) -> dict[int, int]:
    return {position: rank for rank, position in enumerate(sorted(eligible, key=lambda item: (-scores[item], item)))}


def query_search_index(topic: str, query: str, *, top_k: int = 10, mode: str = "hybrid",
                       min_year: int | None = None, max_year: int | None = None,
                       query_vector: Sequence[float] | None = None,
                       docs_dir: str | Path | None = None) -> dict[str, Any]:
    """Query a topic's prebuilt Deep Research index without modifying it."""
    if mode not in {"hybrid", "dense", "bm25"}:
        raise ValueError("mode must be one of: hybrid, dense, bm25")
    if not isinstance(top_k, int) or isinstance(top_k, bool) or top_k < 1:
        raise ValueError("top_k must be a positive integer")
    if not isinstance(query, str) or not query.strip():
        raise ValueError("query must be a non-empty string")
    if min_year is not None and not isinstance(min_year, int):
        raise ValueError("min_year must be an integer or None")
    if max_year is not None and not isinstance(max_year, int):
        raise ValueError("max_year must be an integer or None")

    index, topic_dir = _load_index(topic, docs_dir)
    chunks = index["chunks"]
    eligible = _eligible_indexes(index, min_year, max_year)
    query_terms = tokenize(query)
    documents, lengths, idf, average_length = _build_bm25(chunks, query_terms)
    bm25_scores = {
        position: _bm25_score(documents[position], lengths[position], idf, average_length, query_terms)
        for position in eligible
    }
    bm25_rank = _rank(bm25_scores, eligible)

    dense_scores: dict[int, float] = {}
    dense_rank: dict[int, int] = {}
    if mode in {"dense", "hybrid"}:
        vector = _normalize_query_vector(query_vector, index["dim"]) if query_vector is not None else _embed_query(query, index["dim"])
        raw_embeddings = _load_embedding_bytes(index, topic_dir)
        dense_scores = _dense_scores(
            raw_embeddings, index["dim"], vector, eligible)
        dense_rank = _rank(dense_scores, eligible)

    if mode == "bm25":
        final_scores = {position: 1 / (RRF_K + bm25_rank[position]) for position in eligible}
    elif mode == "dense":
        final_scores = {position: 1 / (RRF_K + dense_rank[position]) for position in eligible}
    else:
        final_scores = {
            position: 1 / (RRF_K + dense_rank[position]) + 1 / (RRF_K + bm25_rank[position])
            for position in eligible
        }
    ordered = sorted(eligible, key=lambda position: (-final_scores[position], position))

    results: list[dict[str, Any]] = []
    per_paper: Counter[str] = Counter()
    for position in ordered:
        chunk = chunks[position]
        slug = str(chunk.get("slug", ""))
        if per_paper[slug] >= MAX_CHUNKS_PER_PAPER:
            continue
        per_paper[slug] += 1
        paper = index["papers"][slug]
        result: dict[str, Any] = {
            "rank": len(results) + 1,
            "slug": slug,
            "title": paper.get("title", slug),
            "year": paper.get("year"),
            "section": chunk.get("section", ""),
            "text": chunk.get("text", ""),
            "rrf_score": final_scores[position],
            "dense_score": dense_scores.get(position, 0.0),
            "bm25_score": bm25_scores[position],
        }
        url = paper.get("external_url") or paper.get("url")
        if url:
            result["url"] = url
        results.append(result)
        if len(results) >= top_k:
            break
    return {
        "query": query,
        "topic": topic,
        "mode": mode,
        "model": index.get("model"),
        "dim": index["dim"],
        "count": index["count"],
        "results": results,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Query a prebuilt Deep Research search index")
    parser.add_argument("--topic", default="_cross", help="topic directory under docs (default: _cross)")
    parser.add_argument("--query", required=True, help="search query")
    parser.add_argument("--top-k", type=int, default=10, help="maximum results (default: 10)")
    parser.add_argument("--mode", choices=("hybrid", "dense", "bm25"), default="hybrid")
    parser.add_argument("--min-year", type=int)
    parser.add_argument("--max-year", type=int)
    parser.add_argument("--json", action="store_true", dest="as_json", help="emit JSON")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = query_search_index(args.topic, args.query, top_k=args.top_k, mode=args.mode,
                                min_year=args.min_year, max_year=args.max_year)
    if args.as_json:
        print(json.dumps(result, ensure_ascii=False))
    else:
        for item in result["results"]:
            snippet = " ".join(str(item["text"]).split())[:180]
            print(f"{item['rank']}. {item['title']} — {item['section']}: {snippet}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
