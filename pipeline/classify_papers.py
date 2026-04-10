"""
Paper classification: primary_category + all_categories (multi-class) + sub_category.

Usage:
  PYTHONUTF8=1 python classify_papers.py --topic ai4s
  PYTHONUTF8=1 python classify_papers.py --topic ai4s --sub-only   # sub-category만 재분류

Multi-class 분류 규칙:
- 각 논문에 primary_category 1개 + all_categories 1~3개 할당
- 논문이 2개 이상 카테고리에 의미 있게 걸치면 all_categories에 모두 포함
- build_topic_index.py가 all_categories 기반으로 여러 카테고리에 카드를 표시
- sub_category: primary_category 내에서의 세부 분류
"""

import argparse
import json
import os
import re
from collections import defaultdict, Counter
from anthropic import Anthropic
from config_loader import get_collections

from config_loader import PAPERS_DIR as _PAPERS_DIR, get_topic_dir
PAPERS_DIR = str(_PAPERS_DIR)
COLLECTIONS = get_collections()

from lib.categories import CATEGORIES_BY_TOPIC


def get_classification(paper, topic):
    """Get classification for a specific topic from paper entry."""
    cls = paper.get("classifications", {})
    return cls.get(topic, {})


def set_classification(paper, topic, primary, all_cats, sub=""):
    """Set classification for a specific topic."""
    if "classifications" not in paper:
        paper["classifications"] = {}
    paper["classifications"][topic] = {
        "primary_category": primary,
        "all_categories": all_cats,
        "sub_category": sub,
    }


def classify_categories(papers, client, topic="ai4s", batch_size=30):
    """Phase 1: primary_category + all_categories (multi-class).
    Only classifies papers that belong to the given topic AND don't already have
    a classification for that topic (--update safe)."""
    CATEGORIES = CATEGORIES_BY_TOPIC.get(topic, CATEGORIES_BY_TOPIC["ai4s"])

    # Filter: only papers belonging to this topic
    topic_papers = [p for p in papers if topic in p.get("topics", [])]
    # Among those, only papers without existing classification for this topic
    to_classify = [p for p in topic_papers if not get_classification(p, topic).get("primary_category")]
    already = len(topic_papers) - len(to_classify)

    print(f"Topic '{topic}': {len(topic_papers)} papers ({already} already classified, {len(to_classify)} to classify)")
    print(f"Categories: {len(CATEGORIES)} (multi-class)")

    if not to_classify:
        print("Nothing to classify.")
        # Still print stats from existing
        cats = Counter(get_classification(p, topic).get("primary_category", "Other") for p in topic_papers)
        print("Primary distribution:")
        for c in CATEGORIES:
            print(f"  {c}: {cats.get(c, 0)}")
        return

    for i in range(0, len(to_classify), batch_size):
        batch = to_classify[i:i+batch_size]
        paper_list = "\n".join(
            f"[{p['slug'].split('_')[0]}] {p['title'][:70]} | {p.get('essence','')[:80]}"
            for p in batch
        )

        prompt = f"""Classify these papers into categories. IMPORTANT: assign ALL relevant categories, not just one.

Categories: {', '.join(CATEGORIES)}

Papers:
{paper_list}

Rules:
- "p": the BEST matching category (primary)
- "a": ALL categories where the paper makes a meaningful contribution (1~3 categories)
- Most papers belong to 1-2 categories. Some interdisciplinary papers belong to 3.
- Be generous with multi-class: if a paper uses agents (Autonomous Agents) to do NLP tasks (Scientific NLP), include BOTH.
- If a paper builds a foundation model (Scientific Foundation Models) and benchmarks it (Benchmarks), include BOTH.

Return JSON array: [{{"n":"001","p":"primary","a":["cat1","cat2"]}}]"""

        try:
            resp = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=3000,
                messages=[{"role": "user", "content": prompt}]
            )
            text = resp.content[0].text.strip()
            if "```" in text:
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]
            results = json.loads(text)
            rmap = {r["n"]: r for r in results}
            for p in batch:
                num = p["slug"].split("_")[0]
                if num in rmap:
                    primary = rmap[num].get("p", "Other")
                    all_cats = rmap[num].get("a", [primary])
                    if primary not in all_cats:
                        all_cats.insert(0, primary)
                    set_classification(p, topic, primary, all_cats)
        except Exception as e:
            print(f"  Batch {i//batch_size} error: {e}")

        print(f"  {min(i+batch_size, len(to_classify))}/{len(to_classify)}")

    # Stats (all topic papers including previously classified)
    multi = sum(1 for p in topic_papers if len(get_classification(p, topic).get("all_categories", [])) > 1)
    cats = Counter(get_classification(p, topic).get("primary_category", "Other") for p in topic_papers)
    print(f"\nMulti-class: {multi}/{len(topic_papers)} ({multi*100//max(1,len(topic_papers))}%)")
    print("Primary distribution:")
    for c in CATEGORIES:
        print(f"  {c}: {cats.get(c, 0)}")


def generate_sub_themes(cat_name, plist, client, n=5):
    """Sub_themes가 없는 카테고리에 대해 LLM으로 sub-theme 이름 생성."""
    titles = "\n".join(f"- {p['title'][:80]}" for p in plist[:50])
    try:
        resp = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=300,
            messages=[{"role": "user", "content":
                f"Category: {cat_name}\n\nPapers:\n{titles}\n\n"
                f"Generate {n} specific sub-category names for grouping these papers. "
                f"Short noun phrases (2-4 words). No numbering.\n"
                f"JSON: [\"Sub A\", \"Sub B\", ...]"}]
        )
        text = resp.content[0].text.strip()
        if "```" in text:
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]
        return json.loads(text)
    except Exception as e:
        print(f"  ERR generating sub_themes for {cat_name}: {e}")
        return []


def classify_subcategories(papers, summaries, client, topic="ai4s", batch_size=40):
    """Phase 2: sub_categories for EACH category in all_categories.
    Each paper gets a sub_category per category it belongs to (not just primary).
    Stored as sub_categories dict: { "Category A": "Sub A", "Category B": "Sub B" }."""
    topic_papers = [p for p in papers if topic in p.get("topics", [])]

    # Build category → sub_theme names from summaries
    cat_subs = {}
    for s in summaries:
        subs = [st["name"] for st in s.get("sub_themes", [])]
        if subs:
            cat_subs[s["category"]] = subs

    # Group papers by each category they belong to (via all_categories)
    cat_papers = defaultdict(list)
    for p in topic_papers:
        cls = get_classification(p, topic)
        for cat in cls.get("all_categories", []):
            cat_papers[cat].append(p)

    print(f"\nClassifying sub-categories per category (topic={topic})...")

    # Collect all categories that need sub-classification (from cat_papers)
    all_cats = set(cat_papers.keys())
    for cat in all_cats:
        if cat not in cat_subs and cat != "Other":
            plist = cat_papers[cat]
            if len(plist) >= 3:
                print(f"  Generating sub_themes for {cat} ({len(plist)} papers)...")
                subs = generate_sub_themes(cat, plist, client)
                if subs:
                    cat_subs[cat] = subs
                    print(f"    → {subs}")

    for cat_name, sub_list in cat_subs.items():
        plist = cat_papers.get(cat_name, [])
        if not plist or len(plist) < 3:
            continue

        # Only classify papers that don't have sub_categories[cat_name] yet
        to_classify = []
        for p in plist:
            cls = get_classification(p, topic)
            sc = cls.get("sub_categories", {})
            if cat_name not in sc:
                to_classify.append(p)

        if not to_classify:
            dist = Counter(
                get_classification(p, topic).get("sub_categories", {}).get(cat_name, "?")
                for p in plist
            )
            print(f"  {cat_name} ({len(plist)}): all classified {dict(dist.most_common(5))}")
            continue

        subs_str = ", ".join(sub_list)
        print(f"  {cat_name} ({len(plist)}, new={len(to_classify)})...")

        for i in range(0, len(to_classify), batch_size):
            batch = to_classify[i:i+batch_size]
            first_key = batch[0]["slug"].split("_")[0] if batch else "N"
            paper_lines = "\n".join(
                f"[{p['slug'].split('_')[0]}] {p['title'][:70]}" for p in batch
            )

            try:
                resp = client.messages.create(
                    model="claude-haiku-4-5-20251001",
                    max_tokens=2000,
                    messages=[{"role": "user", "content":
                        f"Classify into sub-categories.\nCategory: {cat_name}\n"
                        f"Sub-categories: {subs_str}\n\nPapers:\n{paper_lines}\n\n"
                        f"Use the EXACT N value from each [N] label. "
                        f"JSON: [{{\"n\":\"{first_key}\",\"s\":\"sub-category\"}}]"}]
                )
                text = resp.content[0].text.strip()
                if "```" in text:
                    text = text.split("```")[1]
                    if text.startswith("json"):
                        text = text[4:]
                results = json.loads(text)
                rmap = {r["n"]: r["s"] for r in results}
                for p in batch:
                    num = p["slug"].split("_")[0]
                    if num in rmap:
                        cls = get_classification(p, topic)
                        if "sub_categories" not in cls:
                            cls["sub_categories"] = {}
                        cls["sub_categories"][cat_name] = rmap[num]
                        # Keep legacy sub_category for primary
                        if cls.get("primary_category") == cat_name:
                            cls["sub_category"] = rmap[num]
                        p.setdefault("classifications", {})[topic] = cls
            except Exception as e:
                print(f"  ERR {cat_name} batch {i//batch_size}: {e}")

        dist = Counter(
            get_classification(p, topic).get("sub_categories", {}).get(cat_name, "?")
            for p in plist
        )
        print(f"    {dict(dist.most_common(5))}")

        dist = Counter(get_classification(p, topic).get("sub_category", "?") for p in plist)
        print(f"  {cat_name} ({len(plist)}, new={len(to_classify)}): {dict(dist.most_common(5))}")


def main():
    parser = argparse.ArgumentParser(description="Classify papers into categories")
    parser.add_argument("--topic", default="ai4s")
    parser.add_argument("--sub-only", action="store_true", help="Sub-category only")
    args = parser.parse_args()

    index_path = os.path.join(PAPERS_DIR, "_papers_index.json")
    with open(index_path, "r", encoding="utf-8") as f:
        papers = json.load(f)

    topic_dir = str(get_topic_dir(args.topic))
    sum_path = os.path.join(topic_dir, "_category_summaries.json")
    summaries = []
    if os.path.exists(sum_path):
        with open(sum_path, "r", encoding="utf-8") as f:
            summaries = json.load(f)

    client = Anthropic()

    if not args.sub_only:
        classify_categories(papers, client, topic=args.topic)

    if summaries:
        classify_subcategories(papers, summaries, client, topic=args.topic)

    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(papers, f, ensure_ascii=False, indent=2)
    print(f"\nSaved: {index_path}")


if __name__ == "__main__":
    main()
