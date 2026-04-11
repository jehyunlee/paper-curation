"""
Build a Deep Research search index (for client-side RAG).

Reads every review.md that belongs to the given topic, splits each one
into section-aware chunks (Essence, Motivation, How, Achievement,
Originality), embeds each chunk with OpenAI `text-embedding-3-small`,
L2-normalises and quantises the 1536-dim float32 vectors down to int8,
then writes `docs/{topic}/_search_index.json`.

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
import json
import os
import re
import sys
import time
from pathlib import Path

PIPELINE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(PIPELINE_DIR))
from config_loader import DOCS_DIR, PAPERS_DIR, PROJECT_ROOT, get_topic_dir, get_papers_index_path


def _load_openai_key_from_config() -> str:
    """Fallback: read openai_api_key from config.json (written by setup.py)."""
    try:
        cfg_path = PROJECT_ROOT / "config.json"
        if cfg_path.exists():
            with open(cfg_path, "r", encoding="utf-8") as f:
                return json.load(f).get("openai_api_key", "") or ""
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
SECTIONS_TO_INDEX = ["Essence", "Motivation", "How", "Achievement", "Originality"]

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

# OpenAI limits: text-embedding-3-small accepts up to 8192 tokens per
# input. Korean averages ~2 chars/token, so 6000 chars is a safe cap
# that also keeps the JSON payload reasonable.
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


def extract_figures(md_text: str, slug: str) -> list:
    """Return a deduped list of figure refs as relative URLs (from docs/{topic}/)."""
    seen = set()
    figures = []
    for m in FIGURE_RE.finditer(md_text):
        caption = m.group(1).strip()
        path = m.group(2)  # "figures/fig1.webp"
        if path in seen:
            continue
        seen.add(path)
        figures.append({
            "caption": caption,
            # URL is resolved from docs/{topic}/ (the page that will host
            # the search UI), hence the ../papers/ prefix.
            "url": f"../papers/{slug}/{path}",
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
    """Return {title, year, figures, chunks:[{section, text}]} for a review.md."""
    try:
        text = md_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  WARN: {slug}: cannot read review.md ({e})")
        return None

    title_m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else slug

    # Year: first 4-digit looking date in the first 800 chars
    year = None
    ym = re.search(r"\b(20\d{2}|19\d{2})\b", text[:800])
    if ym:
        year = int(ym.group(0))

    sections = extract_sections(text)
    figures = extract_figures(text, slug)

    chunks = []
    for sec_name in SECTIONS_TO_INDEX:
        if sec_name not in sections:
            continue
        cleaned = clean_chunk_text(sections[sec_name])
        if len(cleaned) < MIN_CHUNK_CHARS:
            continue
        if len(cleaned) > MAX_CHUNK_CHARS:
            cleaned = cleaned[:MAX_CHUNK_CHARS].rsplit(" ", 1)[0] + "…"
        chunks.append({"section": sec_name, "text": cleaned})

    return {
        "title": title,
        "year": year,
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


def embed_batch(client, texts: list, model: str) -> list:
    """Call OpenAI embeddings with retry."""
    last_err = None
    for attempt in range(3):
        try:
            resp = client.embeddings.create(input=texts, model=model)
            return [d.embedding for d in resp.data]
        except Exception as e:
            last_err = e
            wait = 2 ** attempt
            print(f"    embed retry {attempt + 1}/3 after {wait}s ({e})")
            time.sleep(wait)
    raise RuntimeError(f"embed_batch failed after 3 attempts: {last_err}")


def build_index(topic: str, model: str, limit: int | None, dry_run: bool):
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

    # --- Parse reviews ---
    papers_meta: dict = {}
    pending_chunks: list = []  # each: {slug, section, text}
    skipped = 0
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

        papers_meta[slug] = {
            "title": parsed["title"],
            "year": parsed["year"] or p.get("date") or "",
            "category": category,
            "url": f"../papers/{slug}/",
            "figures": parsed["figures"],
        }
        for ch in parsed["chunks"]:
            pending_chunks.append({
                "slug": slug,
                "section": ch["section"],
                "text": ch["text"],
            })

    print(f"      {len(papers_meta)} papers, {len(pending_chunks)} chunks, {skipped} skipped")

    if not pending_chunks:
        print("ERROR: no chunks to embed")
        sys.exit(3)

    total_chars = sum(len(c["text"]) for c in pending_chunks)
    approx_tokens = total_chars // 3  # conservative estimate
    print(f"      approx {approx_tokens:,} input tokens ~= ${approx_tokens * 0.00000002:.4f} (text-embedding-3-small)")

    # --- Embed ---
    if dry_run:
        print("[3/4] --dry-run: skipping embedding API calls")
        embeddings = [[0.0] * 1536 for _ in pending_chunks]
    else:
        print(f"[3/4] Embedding {len(pending_chunks)} chunks with {model}...")
        try:
            from openai import OpenAI
        except ImportError:
            print("ERROR: openai package not installed. Run: pip install openai")
            sys.exit(1)

        api_key = os.environ.get("OPENAI_API_KEY") or _load_openai_key_from_config()
        if not api_key:
            print("ERROR: OPENAI_API_KEY not set (env var or config.json).")
            print("       Set OPENAI_API_KEY or run 'python pipeline/setup.py' to save it into config.json.")
            sys.exit(1)

        client = OpenAI(api_key=api_key)
        embeddings: list = []
        BATCH = 100
        t0 = time.time()
        for i in range(0, len(pending_chunks), BATCH):
            batch = pending_chunks[i:i + BATCH]
            texts = [c["text"] for c in batch]
            vecs = embed_batch(client, texts, model)
            embeddings.extend(vecs)
            done = i + len(batch)
            elapsed = time.time() - t0
            rate = done / elapsed if elapsed > 0 else 0
            eta = (len(pending_chunks) - done) / rate if rate > 0 else 0
            print(f"      {done}/{len(pending_chunks)}  ({rate:.1f}/s, ETA {eta:.0f}s)")

    dim = len(embeddings[0]) if embeddings else 0
    print(f"      dim={dim}")

    # --- Quantise + assemble JSON ---
    print("[4/4] Quantising and writing JSON...")
    out_chunks = []
    for chunk, emb in zip(pending_chunks, embeddings):
        qbytes = quantize_int8_l2(emb)
        out_chunks.append({
            "slug": chunk["slug"],
            "section": chunk["section"],
            "text": chunk["text"],
            "emb": base64.b64encode(qbytes).decode("ascii"),
        })

    out = {
        "model": model,
        "dim": dim,
        "quant": "int8-l2norm",
        "count": len(out_chunks),
        "papers": papers_meta,
        "chunks": out_chunks,
    }

    out_path = topic_dir / "_search_index.json"
    out_path.write_text(
        json.dumps(out, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    size_kb = out_path.stat().st_size // 1024
    print(f"      wrote {out_path} ({size_kb:,} KB)")
    print("Done.")


def main():
    parser = argparse.ArgumentParser(description="Build Deep Research search index")
    parser.add_argument("--topic", required=True, help="topic alias (e.g. ai4s, scisci)")
    parser.add_argument("--model", default="text-embedding-3-small")
    parser.add_argument("--limit", type=int, default=None, help="limit number of papers (debug)")
    parser.add_argument("--dry-run", action="store_true", help="chunk only, no API calls")
    args = parser.parse_args()
    build_index(args.topic, args.model, args.limit, args.dry_run)


if __name__ == "__main__":
    main()
