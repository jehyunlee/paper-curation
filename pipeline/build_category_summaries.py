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
from anthropic import Anthropic

from config_loader import PAPERS_DIR as _PAPERS_DIR, get_topic_dir
PAPERS_DIR = str(_PAPERS_DIR)

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


def generate_description_ko(cat_name, papers, sub_themes, client, topic="ai4s"):
    """카테고리 overview 한글 설명 생성 ([NNN] 마커)."""
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

    try:
        resp = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1500,
            messages=[{"role": "user", "content": prompt}]
        )
        ko = resp.content[0].text.strip()
        if ko and ko[-1] not in ".다":
            ko += "."
        return ko
    except Exception as e:
        print(f"  ERR overview {cat_name}: {e}")
        return ""


def generate_sub_theme_ko(cat_name, st_name, st_desc, papers, client):
    """Sub-theme 한글 설명 생성 ([NNN] 마커)."""
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

    try:
        resp = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )
        ko = resp.content[0].text.strip()
        if ko and ko[-1] not in ".다":
            ko += "."
        return ko
    except Exception as e:
        print(f"  ERR sub-ko {cat_name}/{st_name}: {e}")
        return st_desc


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


def main():
    parser = argparse.ArgumentParser(description="Build _category_summaries.json")
    parser.add_argument("--topic", default="ai4s")
    parser.add_argument("--regen-ko", action="store_true", help="한글 설명만 재생성")
    parser.add_argument("--categories", nargs="+", help="Specific categories to regenerate (others preserved)")
    args = parser.parse_args()

    topic_dir = str(get_topic_dir(args.topic))
    sum_path = os.path.join(topic_dir, "_category_summaries.json")

    with open(os.path.join(PAPERS_DIR, "_papers_index.json"), "r", encoding="utf-8") as f:
        papers = json.load(f)

    # Filter papers belonging to this topic, read from classifications[topic]
    topic_papers = [p for p in papers if args.topic in p.get("topics", [])]
    print(f"Topic '{args.topic}': {len(topic_papers)} papers (of {len(papers)} total)")

    cat_papers = defaultdict(list)
    for p in topic_papers:
        cls = p.get("classifications", {}).get(args.topic, {})
        cat_papers[cls.get("primary_category", "Other")].append(p)

    # Sub-category papers mapping (from classifications[topic])
    sub_papers = defaultdict(list)
    for p in topic_papers:
        cls = p.get("classifications", {}).get(args.topic, {})
        pc = cls.get("primary_category", "")
        sc = cls.get("sub_categories", {}).get(pc, cls.get("sub_category", ""))
        key = (pc, sc)
        sub_papers[key].append(p)

    client = Anthropic()

    # Load existing or start fresh
    if args.regen_ko and os.path.exists(sum_path):
        with open(sum_path, "r", encoding="utf-8") as f:
            summaries = json.load(f)
    else:
        summaries = []

    if not args.regen_ko:
        # --categories: preserve existing, only regenerate specified categories
        if args.categories and os.path.exists(sum_path):
            with open(sum_path, "r", encoding="utf-8") as f:
                existing = json.load(f)
            preserved = [s for s in existing if s["category"] not in args.categories]
            summaries = preserved
            CATEGORIES = [c for c in args.categories if c in cat_papers]
            print(f"  Selective update: {len(CATEGORIES)} categories to regenerate, {len(preserved)} preserved")
        else:
            summaries = []
            CATEGORIES = sorted(c for c in cat_papers.keys() if c != "Other") + (["Other"] if "Other" in cat_papers else [])
        for cat_name in CATEGORIES:
            plist = cat_papers.get(cat_name, [])
            if not plist:
                continue

            print(f"\n{cat_name} ({len(plist)} papers)...")

            # Collect sub-themes from classifications[topic] (canonical names)
            if len(plist) > 30:
                sub_themes = collect_sub_themes_from_index(cat_name, plist, args.topic)
                print(f"  {len(sub_themes)} sub-themes (from index)")
            else:
                sub_themes = []

            # Top papers
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

    # Generate Korean descriptions
    print("\nGenerating Korean descriptions...")
    issues = []
    regen_set = set(args.categories) if args.categories else None
    for s in summaries:
        cat = s["category"]
        # Skip categories not in regen set (already have description_ko)
        if regen_set and cat not in regen_set:
            continue
        plist = cat_papers.get(cat, [])

        # Overview
        existing_ko = s.get("description_ko", "")
        if not existing_ko or args.regen_ko or validate_description(existing_ko, cat):
            ko = generate_description_ko(cat, plist, s.get("sub_themes", []), client, topic=args.topic)
            s["description_ko"] = ko
            issue = validate_description(ko, cat)
            if issue:
                issues.append(issue)
            print(f"  {cat}: overview {len(ko)}chars")

        # Sub-theme descriptions
        for st in s.get("sub_themes", []):
            existing_stko = st.get("description_ko", "")
            label = f"{cat}/{st['name']}"
            if not existing_stko or args.regen_ko or validate_description(existing_stko, label):
                sp = sub_papers.get((cat, st["name"]), [])
                ko = generate_sub_theme_ko(cat, st["name"], st.get("description", ""), sp, client)
                st["description_ko"] = ko
                issue = validate_description(ko, label)
                if issue:
                    issues.append(issue)
            print(f"    {st['name']}: {len(st.get('description_ko',''))}chars")

    # Save
    os.makedirs(topic_dir, exist_ok=True)
    with open(sum_path, "w", encoding="utf-8") as f:
        json.dump(summaries, f, ensure_ascii=False, indent=2)

    print(f"\nSaved: {sum_path} ({len(summaries)} categories)")
    if issues:
        print(f"\nWARNING: {len(issues)} quality issues:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("OK: All descriptions pass quality check")


if __name__ == "__main__":
    main()
