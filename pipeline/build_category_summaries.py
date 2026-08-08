"""
_category_summaries.json 생성.

카테고리별 description_ko, sub_themes (with description_ko), papers 목록을 생성한다.
classify_papers.py 실행 후에 실행해야 한다 (primary_category 필요).

Usage:
  PYTHONUTF8=1 python build_category_summaries.py --topic ai4s
  PYTHONUTF8=1 python build_category_summaries.py --topic ai4s --regen-ko  # 한글 설명만 재생성
"""

import argparse
import json
import os
import re
from collections import defaultdict
from lib.llm_client import get_chat_client

from config_loader import PAPERS_DIR as _PAPERS_DIR, get_topic_dir
PAPERS_DIR = str(_PAPERS_DIR)

def _anthropic_text(resp):
    parts = []
    for block in getattr(resp, "content", []) or []:
        if getattr(block, "type", None) == "text" and getattr(block, "text", None):
            parts.append(block.text)
    text = "".join(parts).strip()
    if not text:
        types = [getattr(b, "type", type(b).__name__) for b in getattr(resp, "content", []) or []]
        raise RuntimeError(f"Anthropic response contained no text blocks: {types}")
    return text


# Categories are now dynamic from _papers_index.json (BERTopic-generated)


def collect_sub_themes_from_index(cat_name, papers, topic):
    """classifications[topic].sub_categories[cat_name] 값을 정본으로 수집. LLM 생성 안 함."""
    from collections import Counter
    sub_counts = Counter()
    for p in papers:
        cls = p.get("classifications", {}).get(topic, {})
        # New schema: sub_categories dict per category
        sc = cls.get("sub_categories", {}).get(cat_name, "")
        # Fallback: legacy sub_category (for primary only)
        if not sc and cls.get("primary_category") == cat_name:
            sc = cls.get("sub_category", "")
        if sc:
            sub_counts[sc] += 1

    if not sub_counts:
        return []

    return [
        {"name": name, "description": f"{name} ({count} papers in {cat_name})", "count": count}
        for name, count in sub_counts.most_common()
    ]


def _call_with_invariant_gate(prompt, model, max_tokens, label, client,
                                max_retries=1):
    """Call Haiku and enforce ``validate_description`` invariants.

    On a violation we retry once with a hint that explicitly names the
    issue. If the retry still fails we return the best attempt and let
    the caller decide whether to log/escalate. Returns (text, issue) —
    ``issue`` is ``None`` on success.
    """
    last_text = ""
    last_issue = None
    for attempt in range(max_retries + 1):
        local_prompt = prompt
        if attempt > 0 and last_issue:
            local_prompt = (
                f"{prompt}\n\n[직전 출력의 문제]: {last_issue}\n"
                "위 문제를 고치되 같은 규칙을 모두 지켜 다시 작성하세요."
            )
        try:
            resp = client.messages.create(
                model=model,
                max_tokens=max_tokens,
                messages=[{"role": "user", "content": local_prompt}],
            )
            text = _anthropic_text(resp)
            if text and text[-1] not in ".다":
                text += "."
        except Exception as e:
            return "", f"{label}: 호출 실패 ({type(e).__name__})"

        issue = validate_description(text, label)
        if issue is None:
            return text, None
        last_text = text
        last_issue = issue
    return last_text, last_issue


def generate_description_ko(cat_name, papers, sub_themes, client, topic="ai4s"):
    """카테고리 overview 한글 설명 생성 ([NNN] 마커).

    invariant gate (length, korean ratio, [NNN] residue, terminal punct)
    위반 시 1회 자동 재호출.
    """
    top = sorted(papers, key=lambda x: -x.get("score", 0))[:20]
    refs = "\n".join(f"[{p['slug'].split('_')[0]}] {p['title'][:60]}" for p in top)
    sub_names = ", ".join(st["name"] for st in sub_themes)

    prompt = f"""{topic} 카테고리 "{cat_name}" ({len(papers)}편) 개요를 한국어로 작성하세요.

Sub-themes: {sub_names}
논문 목록:
{refs}

규칙:
- 한국어 4~6문장, 기술용어 영문 병기
- 논문 인용은 [N] 형식만 (위 목록의 대괄호 번호를 그대로 사용)
- 논문 제목을 본문에 직접 쓰지 마세요
- 반드시 마침표(.)로 끝나는 완결된 문장
- 텍스트만 출력"""

    text, issue = _call_with_invariant_gate(
        prompt, "claude-haiku-4-5-20251001", 1500, cat_name, client,
    )
    if issue is not None and text:
        print(f"  WARN overview {cat_name}: {issue} (best-effort 반환)")
    elif not text:
        print(f"  ERR overview {cat_name}: {issue}")
    return text


def generate_sub_theme_ko(cat_name, st_name, st_desc, papers, client):
    """Sub-theme 한글 설명 생성 ([NNN] 마커). invariant gate 적용."""
    refs = "\n".join(f"[{p['slug'].split('_')[0]}] {p['title'][:60]}"
                     for p in sorted(papers, key=lambda x: -x.get('score', 0))[:8])
    if not refs:
        return st_desc

    prompt = f"""다음 sub-category에 대해 한국어 설명을 작성하세요.

Category: {cat_name}
Sub-category: {st_name} ({len(papers)}편)

논문 목록:
{refs}

규칙:
- 한국어 4~6문장, 기술용어 영문 병기
- 논문 인용은 [NNN] 형식만 (최소 2개 인용)
- 반드시 마침표(.)로 끝나는 완결된 문장
- 텍스트만 출력"""

    label = f"{cat_name}/{st_name}"
    text, issue = _call_with_invariant_gate(
        prompt, "claude-haiku-4-5-20251001", 1000, label, client,
    )
    if issue is not None and text:
        print(f"  WARN sub-ko {label}: {issue} (best-effort 반환)")
    elif not text:
        print(f"  ERR sub-ko {label}: {issue}")
        return st_desc
    return text


def validate_description(text, label):
    """설명 품질 검증. 문제가 있으면 이유 반환, 없으면 None."""
    if not text or len(text) < 50:
        return f"{label}: 너무 짧음 ({len(text or '')}자)"
    korean = len(re.findall(r'[\uac00-\ud7af]', text))
    if korean < len(text) * 0.3:
        return f"{label}: 한국어 비율 낮음"
    if "[NNN]" in text:
        return f"{label}: [NNN] 리터럴 잔류"
    if text.strip()[-1] not in ".다":
        return f"{label}: 마침표로 끝나지 않음"
    return None


def _run_category_summary(topic="ai4s", *, regen_ko=False, categories=None):
    """Programmatic entrypoint for build_category_summaries.

    `categories` is a list of category names to selectively regenerate.
    """
    topic_dir = str(get_topic_dir(topic))
    sum_path = os.path.join(topic_dir, "_category_summaries.json")

    with open(os.path.join(PAPERS_DIR, "_papers_index.json"), "r", encoding="utf-8") as f:
        papers = json.load(f)

    topic_papers = [p for p in papers if topic in p.get("topics", [])]
    print(f"Topic '{topic}': {len(topic_papers)} papers (of {len(papers)} total)")

    cat_papers = defaultdict(list)
    for p in topic_papers:
        cls = p.get("classifications", {}).get(topic, {})
        cat_papers[cls.get("primary_category", "Other")].append(p)

    sub_papers = defaultdict(list)
    for p in topic_papers:
        cls = p.get("classifications", {}).get(topic, {})
        pc = cls.get("primary_category", "")
        sc = cls.get("sub_categories", {}).get(pc, cls.get("sub_category", ""))
        key = (pc, sc)
        sub_papers[key].append(p)

    client = get_chat_client(timeout=180.0, max_retries=4)

    if regen_ko and os.path.exists(sum_path):
        with open(sum_path, "r", encoding="utf-8") as f:
            summaries = json.load(f)
    else:
        summaries = []

    if not regen_ko:
        if categories and os.path.exists(sum_path):
            with open(sum_path, "r", encoding="utf-8") as f:
                existing = json.load(f)
            current_cats = set(cat_papers.keys())
            preserved = [s for s in existing
                         if s["category"] not in categories
                         and s["category"] in current_cats]
            dropped = [s["category"] for s in existing
                       if s["category"] not in categories
                       and s["category"] not in current_cats]
            summaries = preserved
            CATEGORIES = [c for c in categories if c in cat_papers]
            print(f"  Selective update: {len(CATEGORIES)} categories to regenerate, {len(preserved)} preserved")
            if dropped:
                print(f"  Dropped {len(dropped)} stale categories: {dropped}")
        else:
            summaries = []
            CATEGORIES = sorted(c for c in cat_papers.keys() if c != "Other") + (["Other"] if "Other" in cat_papers else [])
        for cat_name in CATEGORIES:
            plist = cat_papers.get(cat_name, [])
            if not plist:
                continue

            print(f"\n{cat_name} ({len(plist)} papers)...")

            if len(plist) > 30:
                sub_themes = collect_sub_themes_from_index(cat_name, plist, topic)
                print(f"  {len(sub_themes)} sub-themes (from index)")
            else:
                sub_themes = []

            top = sorted(plist, key=lambda x: -x.get("score", 0))[:20]

            summaries.append({
                "category": cat_name,
                "description": f"AI for Science category: {cat_name}",
                "count": len(plist),
                "avg_score": round(sum(p.get("score", 0) for p in plist) / max(1, len(plist)), 2),
                "sub_themes": sub_themes,
                "papers": [{"slug": p["slug"], "dir": p["slug"], "title": p["title"],
                            "score": p.get("score", 0), "date": p.get("date", "")} for p in top],
            })

    print("\nGenerating Korean descriptions (parallel per-category)...")
    issues = []
    issues_lock = __import__("threading").Lock()
    regen_set = set(categories) if categories else None

    def _process_one(s):
        """Generate KO description + sub-theme descriptions for a single
        category. Mutates ``s`` in place; safe because each thread owns
        its own ``s`` dict reference."""
        cat = s["category"]
        if regen_set and cat not in regen_set:
            return
        plist = cat_papers.get(cat, [])

        existing_ko = s.get("description_ko", "")
        if not existing_ko or regen_ko or validate_description(existing_ko, cat):
            ko = generate_description_ko(cat, plist, s.get("sub_themes", []), client, topic=topic)
            s["description_ko"] = ko
            issue = validate_description(ko, cat)
            if issue:
                with issues_lock:
                    issues.append(issue)
            print(f"  {cat}: overview {len(ko)}chars")

        for st in s.get("sub_themes", []):
            existing_stko = st.get("description_ko", "")
            label = f"{cat}/{st['name']}"
            if not existing_stko or regen_ko or validate_description(existing_stko, label):
                sp = sub_papers.get((cat, st["name"]), [])
                ko = generate_sub_theme_ko(cat, st["name"], st.get("description", ""), sp, client)
                st["description_ko"] = ko
                issue = validate_description(ko, label)
                if issue:
                    with issues_lock:
                        issues.append(issue)
            print(f"    {st['name']}: {len(st.get('description_ko',''))}chars")

    # ThreadPool: Haiku calls are I/O-bound. Anthropic Tier 4 (~5k RPM,
    # 400k ITPM) easily handles 8 concurrent category workers.
    from concurrent.futures import ThreadPoolExecutor, as_completed
    max_workers = int(os.environ.get("CAT_SUMMARY_PARALLEL", "8"))
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        futures = [ex.submit(_process_one, s) for s in summaries]
        for fut in as_completed(futures):
            # Surface exceptions; per-category failure shouldn't kill the rest.
            try:
                fut.result()
            except Exception as e:
                print(f"  [category failed] {str(e)[:120]}")

    os.makedirs(topic_dir, exist_ok=True)
    from lib.atomic_io import atomic_write_json
    atomic_write_json(sum_path, summaries)

    print(f"\nSaved: {sum_path} ({len(summaries)} categories)")
    if issues:
        print(f"\nWARNING: {len(issues)} quality issues:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("OK: All descriptions pass quality check")
    return summaries


def main():
    parser = argparse.ArgumentParser(description="Build _category_summaries.json")
    parser.add_argument("--topic", default="ai4s")
    parser.add_argument("--regen-ko", action="store_true", help="한글 설명만 재생성")
    parser.add_argument("--categories", nargs="+", help="Specific categories to regenerate (others preserved)")
    args = parser.parse_args()
    _run_category_summary(topic=args.topic, regen_ko=args.regen_ko,
                          categories=args.categories)


if __name__ == "__main__":
    main()
