#!/usr/bin/env python3
"""originality.md 를 LLM 으로 다시 쓴다 (규칙 기반 추출기 대체).

왜 바꾸나 — `_extract_rule_based` 는 originality 문장을 *고르는* 게 아니라 첫
트리거 문장부터 잘라 온다. 그래서 트리거가 감사문·저자 약력에 걸리면 그 논문의
originality 가 "I went straight there and every day since I've been focused on my
career in robotics." 가 된다(슬러그 9132, 실재). 해시 사이드카는 이걸 못 잡는다 —
출처는 진짜로 그 text.md 가 맞기 때문이다. 출처 게이트는 *어디서 왔는지*를
보장하지 *무엇인지*를 보장하지 않는다.

백엔드 선택은 측정으로 정했다. 소비자가 사람이 아니라 SPECTER2(512토큰 →
768차원)라, 같은 논문에 대한 모델 간 결과 벡터 코사인이 qwen↔haiku 0.985,
qwen↔sonnet 0.980, **haiku↔sonnet 0.977** 이다 — Claude 두 모델끼리가 더 갈린다.
수렴할 "정답"이 없으므로 품질보다 속도·비용·견고성으로 고른다. 8편 표본에서
haiku 2.70s/편, qwen 10.61s/편, sonnet 13.19s/편.

그래서 haiku 가 기본이고, **거부 게이트가 필수**다. 같은 표본에서 haiku 는 8편 중
1편(목차만 추출된 논문)을 거부했다. 거부문이 파일에 들어가면 SPECTER2 가 거부문을
임베딩해 거부당한 논문들끼리 가짜 클러스터를 만든다. 그래서 백엔드 체인을 두고,
전부 실패하면 **기존 파일을 그대로 둔다** — 나쁜 것을 쓰느니 낡은 것을 둔다.

Usage:
  # 프롬프트 튜닝(공짜, 코퍼스 안 건드림)
  python pipeline/regenerate_originality.py --limit 12 --backends local --dry-run

  # 본 실행
  python pipeline/regenerate_originality.py --backends haiku,sonnet,local
"""

import argparse
import json
import os
import sys
import threading
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config_loader import PAPERS_DIR as _PAPERS_DIR
from lib.originality_extractor import (
    looks_unusable, read_provenance, text_digest, write_provenance,
)

PAPERS_DIR = str(_PAPERS_DIR)

# 초록부터 6,000자. 초록 위쪽(표지·소속)은 기여를 담지 않고 토큰만 먹는다.
WINDOW_CHARS = 6000

# 이보다 적은 본문은 LLM 에 넘기지 않는다. 프롬프트가 "절대 거부하지 말라" 고
# 지시하므로 넘길 게 없으면 모델은 거부 대신 **지어낸다** — 거부 게이트도
# `derives_from` 도 못 잡는 실패다. 코퍼스에 PDF 텍스트가 아예 추출되지 않은
# 논문이 51편 있고(대부분 0자), 이들은 기존 `title. essence` 를 그대로 둔다.
MIN_WINDOW_CHARS = 400

PROMPT = (
    "In 2-4 sentences state ONLY what THIS paper newly contributes — the "
    "method/system/dataset it introduces and what it enables. Copy technical "
    "terms verbatim. No background, no citations, no hedging.\n"
    "If the text is fragmentary (a table of contents, slide headings, front "
    "matter), still answer from whatever titles and section names are present. "
    "Never refuse and never describe the text itself; write only about the "
    "paper's contribution. Plain text only.\n\nTEXT:\n{text}"
)

ANTHROPIC_MODELS = {"haiku": "claude-haiku-4-5", "sonnet": "claude-sonnet-5"}
LOCAL_MODEL = os.environ.get("ORIGINALITY_LOCAL_MODEL", "qwen3.8:27b-mlx")
LOCAL_URL = os.environ.get("ORIGINALITY_LOCAL_URL", "http://localhost:11434/api/chat")

_print_lock = threading.Lock()


def log(msg):
    with _print_lock:
        print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def read_window(slug_dir):
    """text.md 의 초록 기준 창. text.md 가 없으면 None."""
    path = os.path.join(slug_dir, "text.md")
    if not os.path.exists(path):
        return None, None
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        full = f.read()
    pos = full.lower().find("abstract")
    window = full[pos:pos + WINDOW_CHARS] if pos >= 0 else full[:WINDOW_CHARS]
    return full, window


def call_anthropic(client, model, window):
    resp = client.messages.create(
        model=model, max_tokens=400,
        messages=[{"role": "user", "content": PROMPT.format(text=window)}])
    return "".join(b.text for b in resp.content if getattr(b, "text", None)).strip()


def call_local(window, timeout=900.0):
    body = json.dumps({
        "model": LOCAL_MODEL, "stream": False, "think": False,
        "options": {"temperature": 0.2, "num_ctx": 8192},
        "messages": [{"role": "user", "content": PROMPT.format(text=window)}],
    }).encode()
    req = urllib.request.Request(LOCAL_URL, data=body,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as fh:
        return (json.load(fh).get("message", {}) or {}).get("content", "").strip()


def build_backends(names):
    """이름 목록 → [(label, callable)]. 키·엔드포인트가 없으면 조용히 제외."""
    chain = []
    anthropic_client = None
    for name in names:
        if name in ANTHROPIC_MODELS:
            if anthropic_client is None:
                if not os.environ.get("ANTHROPIC_API_KEY"):
                    log(f"  [backend] {name}: ANTHROPIC_API_KEY 없음 — 제외")
                    continue
                from anthropic import Anthropic
                anthropic_client = Anthropic(timeout=180.0, max_retries=3)
            model = ANTHROPIC_MODELS[name]
            chain.append((f"llm.{name}",
                          lambda w, m=model, c=anthropic_client: call_anthropic(c, m, w)))
        elif name == "local":
            chain.append(("llm.local", call_local))
        else:
            raise SystemExit(f"unknown backend: {name}")
    if not chain:
        raise SystemExit("사용 가능한 백엔드가 없습니다.")
    return chain


def generate_one(slug, backends, force=False, dry_run=False):
    """한 논문 처리. (slug, status, extractor, detail) 반환."""
    slug_dir = os.path.join(PAPERS_DIR, slug)
    full, window = read_window(slug_dir)
    if full is None:
        return slug, "no-text", "", ""
    if len(window.strip()) < MIN_WINDOW_CHARS:
        # 넘길 본문이 없다 — 기존 originality 를 그대로 둔다.
        return slug, "too-little-text", "", f"{len(window.strip())} chars"
    digest = text_digest(full)

    if not force:
        meta = read_provenance(slug_dir)
        if meta.get("text_md_sha256") == digest and \
                str(meta.get("extractor", "")).startswith("llm."):
            return slug, "skip", meta["extractor"], "already llm-sourced"

    reasons = []
    for label, fn in backends:
        try:
            text = fn(window)
        except Exception as e:
            reasons.append(f"{label}:error({str(e)[:60]})")
            continue
        bad = looks_unusable(text, prompt_echo=PROMPT[:60])
        if bad:
            reasons.append(f"{label}:{bad}")
            continue
        if dry_run:
            return slug, "would-write", label, text
        with open(os.path.join(slug_dir, "originality.md"), "w", encoding="utf-8") as f:
            f.write(text)
        write_provenance(slug_dir, digest, label)
        return slug, "written", label, text
    # 전 백엔드 실패 — 기존 파일을 건드리지 않는다.
    return slug, "kept", "", "; ".join(reasons)


def main():
    p = argparse.ArgumentParser(description="Regenerate originality.md with an LLM")
    p.add_argument("--backends", default="haiku,sonnet,local",
                   help="fallback chain, 순서대로 시도 (haiku/sonnet/local)")
    p.add_argument("--slugs", help="쉼표 구분 슬러그 접두사")
    p.add_argument("--limit", type=int, help="앞에서 N편만 (표본 검증용)")
    p.add_argument("--concurrency", type=int, default=8)
    p.add_argument("--force", action="store_true",
                   help="이미 llm 출처인 논문도 다시 생성")
    p.add_argument("--dry-run", action="store_true",
                   help="생성만 하고 파일은 쓰지 않음")
    args = p.parse_args()

    index = json.load(open(os.path.join(PAPERS_DIR, "_papers_index.json"),
                           encoding="utf-8"))
    slugs = [e["slug"] for e in index]
    if args.slugs:
        want = tuple(s.strip() for s in args.slugs.split(",") if s.strip())
        slugs = [s for s in slugs if s.startswith(want)]
    if args.limit:
        slugs = slugs[:args.limit]

    backends = build_backends([b.strip() for b in args.backends.split(",") if b.strip()])
    log(f"대상 {len(slugs)}편, 체인 {[l for l, _ in backends]}, "
        f"concurrency={args.concurrency}{' (dry-run)' if args.dry_run else ''}")

    stats, kept, done = {}, [], 0
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.concurrency) as ex:
        futures = {ex.submit(generate_one, s, backends, args.force, args.dry_run): s
                   for s in slugs}
        for fut in as_completed(futures):
            slug, status, extractor, detail = fut.result()
            key = f"{status}:{extractor}" if extractor else status
            stats[key] = stats.get(key, 0) + 1
            if status == "kept":
                kept.append((slug, detail))
            done += 1
            if done % 100 == 0 or done == len(slugs):
                rate = done / max(time.time() - t0, 1e-9)
                log(f"  {done}/{len(slugs)}  ({rate:.1f}편/s, "
                    f"남은 {int((len(slugs)-done)/max(rate,1e-9))}s)")

    log(f"완료 {time.time()-t0:.0f}s")
    for k in sorted(stats):
        log(f"  {k:24s} {stats[k]:5,d}")
    if kept:
        log(f"  ── 전 백엔드 실패로 기존 파일 유지: {len(kept)}편")
        for slug, why in kept[:10]:
            log(f"     {slug[:52]:54s} {why[:70]}")


if __name__ == "__main__":
    main()
