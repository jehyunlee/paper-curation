"""review.md 제목 헤더(H1 + 저자 blockquote) 유실 복구 도구.

과거 리뷰 재생성(salvage) 경로에서 `# 제목` / `> **저자**: …` 헤더가 통째로
빠진 review.md 가 만들어졌고, `review_to_html.py` 가 제목을 slug 디렉터리
절대경로로 대체해 `<title>`·`<h1>`·`og:title` 에 로컬 경로가 노출됐다.

이 스크립트는 frontmatter(authoritative)에서 헤더를 재구성해 본문 맨 앞에
삽입한다. `review.md.broken.bak` 이 남아 있고 거기에 원본 헤더가 있으면
그 헤더를 그대로 쓴다(원문 표기 보존).

기본은 dry-run. 실제 수정은 `--execute`.

Usage:
  python fix_review_headers.py                     # 점검만
  python fix_review_headers.py --execute           # 복구 + index.html 재생성
  python fix_review_headers.py --execute --no-html # review.md 만 복구
  python fix_review_headers.py --slug 483_Learning_to_Discover --execute
"""
import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from config_loader import PAPERS_DIR  # noqa: E402
from inject_frontmatter import _rebuild_title_header  # noqa: E402

PAPERS_DIR = str(PAPERS_DIR)
FM_RE = re.compile(r'^---\n(.*?)\n---\n', re.DOTALL)
H1_RE = re.compile(r'^#\s+\S', re.MULTILINE)


def split_review(text):
    """(frontmatter 블록 전체, frontmatter 본문, 본문) 으로 분리."""
    m = FM_RE.match(text)
    if not m:
        return "", "", text
    return m.group(0), m.group(1), text[m.end():]


def header_from_backup(slug_dir):
    """원본 백업에 남은 제목 헤더(H1 ~ 구분선)를 그대로 회수한다."""
    bak = os.path.join(slug_dir, "review.md.broken.bak")
    if not os.path.exists(bak):
        return ""
    with open(bak, encoding="utf-8") as f:
        _, _, body = split_review(f.read())
    m = re.search(r'(^#\s+.+?\n)(.*?)(?=^##\s)', body, re.DOTALL | re.MULTILINE)
    return m.group(0) if m and H1_RE.search(m.group(0)) else ""


def needs_fix(text):
    _, _, body = split_review(text)
    return not H1_RE.search(body)


def fix_one(slug_dir, execute=False):
    review = os.path.join(slug_dir, "review.md")
    if not os.path.exists(review):
        return None
    with open(review, encoding="utf-8") as f:
        text = f.read()
    if not needs_fix(text):
        return None

    fm_block, fm_body, body = split_review(text)
    header = header_from_backup(slug_dir) or _rebuild_title_header(fm_body)
    source = "backup" if header_from_backup(slug_dir) else "frontmatter"
    title = re.match(r'#\s+(.+)', header).group(1).strip()
    tm = re.search(r'(?m)^primary_topic:\s*(.+)$', fm_body)
    topic = tm.group(1).strip().strip('"').strip("'") if tm else "ai4s"

    if execute:
        new = fm_block + "\n" + header.rstrip("\n") + "\n\n" + body.lstrip("\n")
        tmp = review + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(new)
        os.replace(tmp, review)
    return {"slug": os.path.basename(slug_dir), "title": title,
            "source": source, "topic": topic}


def main():
    ap = argparse.ArgumentParser(description="review.md 제목 헤더 유실 복구")
    ap.add_argument("--slug", action="append", default=[],
                    help="특정 슬러그만 (여러 번 지정 가능, 접두어 매칭)")
    ap.add_argument("--execute", action="store_true", help="실제 수정 (기본 dry-run)")
    ap.add_argument("--no-html", action="store_true", help="index.html 재생성 생략")
    ap.add_argument("--topic", default="", help="HTML 테마 토픽 고정 (기본: 논문 frontmatter 의 primary_topic)")
    args = ap.parse_args()

    names = sorted(n for n in os.listdir(PAPERS_DIR)
                   if os.path.isdir(os.path.join(PAPERS_DIR, n)) and not n.startswith("_"))
    if args.slug:
        names = [n for n in names if any(n.startswith(s) for s in args.slug)]

    fixed = []
    for name in names:
        r = fix_one(os.path.join(PAPERS_DIR, name), execute=args.execute)
        if r:
            fixed.append(r)
            tag = "FIX" if args.execute else "WOULD-FIX"
            print(f"[{tag}] {r['slug']}\n        → {r['title']}  ({r['source']})")

    print(f"\n제목 헤더 유실: {len(fixed)}편"
          + ("" if args.execute else "  — 실제 수정하려면 --execute"))

    # index.html 재생성 — review.md 를 고쳤거나, 과거에 경로가 제목으로 박힌 HTML.
    # convert_review 는 문자열을 돌려줄 뿐이라 호출부가 직접 써야 한다.
    if args.no_html:
        return 0
    targets = {r["slug"]: r["topic"] for r in fixed}
    for name in names:
        ix = os.path.join(PAPERS_DIR, name, "index.html")
        if name in targets or not os.path.exists(ix):
            continue
        with open(ix, encoding="utf-8", errors="replace") as f:
            head = f.read(3000)
        m = re.search(r'<title>(.*?)</title>', head, re.DOTALL)
        if m and m.group(1).strip().startswith("/"):
            review = os.path.join(PAPERS_DIR, name, "review.md")
            if not os.path.exists(review):
                continue
            with open(review, encoding="utf-8") as f:
                _, fm_body, _ = split_review(f.read())
            tm = re.search(r'(?m)^primary_topic:\s*(.+)$', fm_body)
            targets[name] = tm.group(1).strip().strip('"').strip("'") if tm else "ai4s"

    if not targets:
        return 0
    if not args.execute:
        print(f"index.html 재생성 대상: {len(targets)}편 — --execute 필요")
        return 0

    from review_to_html import convert_review
    ok = 0
    for slug, topic in sorted(targets.items()):
        slug_dir = os.path.join(PAPERS_DIR, slug)
        try:
            html = convert_review(os.path.join(slug_dir, "review.md"),
                                  args.topic or topic, slug_dir)
            out = os.path.join(slug_dir, "index.html")
            tmp = out + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                f.write(html)
            os.replace(tmp, out)
            ok += 1
        except Exception as e:  # noqa: BLE001 — 한 편 실패가 전체를 막지 않게
            print(f"  [HTML 실패] {slug}: {e}")
    print(f"index.html 재생성: {ok}/{len(targets)}편")
    return 0


if __name__ == "__main__":
    from _env_guard import force_py312
    force_py312()
    sys.exit(main())
