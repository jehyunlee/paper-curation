"""
Obsidian MOC (Map of Content) 자동 생성.

_insights.json → MOC_Insights.md (교차 트렌드, 갭, 정책 시사점)
_papers_index.json → MOC_Categories.md (카테고리별 논문 wikilink 목록)

Usage:
  PYTHONUTF8=1 python pipeline/generate_moc.py --topic ai4s
  PYTHONUTF8=1 python pipeline/generate_moc.py --topic scisci
"""

import argparse
import json
import os
from collections import defaultdict
from datetime import datetime

from config_loader import PAPERS_DIR as _PAPERS_DIR, get_topic_dir

PAPERS_DIR = str(_PAPERS_DIR)

INSIGHT_TYPE_LABELS = {
    "convergence": "\U0001F504 융합 트렌드",
    "gap": "\u26A0\uFE0F 연구 갭",
    "emerging": "\U0001F331 신흥 트렌드",
    "declining": "\u2B07\uFE0F 감소 추세",
}


def log(msg):
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def generate_moc_insights(topic, topic_dir):
    """_insights.json → MOC_Insights.md"""
    insights_path = os.path.join(topic_dir, "_insights.json")
    if not os.path.exists(insights_path):
        log(f"  SKIP: {insights_path} not found")
        return

    with open(insights_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    cross = data.get("cross_category", [])
    per_cat = data.get("per_category", {})
    meta = data.get("meta", {})
    generated = data.get("generated_at", "")
    paper_count = data.get("paper_count", 0)

    lines = [
        f"# Research Insights — {topic}",
        f"",
        f"*자동 생성: {generated} | {paper_count}편 분석 기반*",
        f"",
    ]

    # Group by type
    by_type = defaultdict(list)
    for ins in cross:
        by_type[ins.get("type", "gap")].append(ins)

    for itype in ["convergence", "emerging", "gap", "declining"]:
        items = by_type.get(itype, [])
        if not items:
            continue
        label = INSIGHT_TYPE_LABELS.get(itype, itype)
        lines.append(f"## {label}")
        lines.append("")
        for ins in items:
            title = ins.get("title", "")
            desc = ins.get("description", "")
            evidence = ins.get("evidence", [])
            policy = ins.get("policy_implication", "")
            cats = ins.get("categories", [])
            strength = ins.get("signal_strength", "")

            ev_links = " ".join(f"[[papers/{_num_to_slug(num)}/review|[{num}]]]" for num in evidence)
            cats_text = " · ".join(cats)

            lines.append(f"### {title}")
            lines.append(f"{desc}")
            lines.append("")
            lines.append(f"**근거 논문**: {ev_links}")
            lines.append(f"**관련 카테고리**: {cats_text}")
            if policy:
                lines.append(f"**정책 시사점**: {policy}")
            lines.append("")

    # Per-category insights
    if per_cat:
        lines.append("## 카테고리별 핵심 발견")
        lines.append("")
        for cat_name, ci in per_cat.items():
            trend = ci.get("trend", "")
            kf = ci.get("key_finding", "")
            gap = ci.get("gap", "")
            pi = ci.get("policy_implication", "")
            lines.append(f"### {cat_name} ({trend})")
            if kf:
                lines.append(f"- **핵심**: {kf}")
            if gap:
                lines.append(f"- **갭**: {gap}")
            if pi:
                lines.append(f"- **정책**: {pi}")
            lines.append("")

    # Meta
    underserved = meta.get("underserved_domains", [])
    hot = meta.get("hot_combinations", [])
    if underserved or hot:
        lines.append("## Meta")
        lines.append("")
        if underserved:
            lines.append(f"**연구 부족 분야**: {', '.join(underserved)}")
        if hot:
            lines.append("**주목할 조합**:")
            for h in hot:
                pair = h.get("pair", [])
                desc = h.get("description", "")
                lines.append(f"- {' × '.join(pair)}: {desc}")
        lines.append("")

    moc_path = os.path.join(topic_dir, "MOC_Insights.md")
    with open(moc_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    log(f"  Written: {moc_path}")


def generate_moc_categories(topic, topic_dir):
    """_papers_index.json → MOC_Categories.md"""
    with open(os.path.join(PAPERS_DIR, "_papers_index.json"), "r", encoding="utf-8") as f:
        all_papers = json.load(f)

    topic_papers = [p for p in all_papers if topic in p.get("topics", [])]

    # Group by primary_category
    cat_papers = defaultdict(list)
    for p in topic_papers:
        cls = p.get("classifications", {}).get(topic, {})
        pc = cls.get("primary_category", "Other")
        cat_papers[pc].append(p)

    lines = [
        f"# Categories — {topic}",
        f"",
        f"*{len(topic_papers)}편 | {len(cat_papers)} 카테고리*",
        f"",
    ]

    for cat_name in sorted(cat_papers.keys()):
        papers = sorted(cat_papers[cat_name], key=lambda x: -x.get("score", 0))
        lines.append(f"## {cat_name} ({len(papers)}편)")
        lines.append("")
        for p in papers:
            slug = p.get("slug", "")
            title = p.get("title", slug)[:80]
            score = p.get("score", 0)
            lines.append(f"- [[papers/{slug}/review|{title}]] — score: {score}")
        lines.append("")

    moc_path = os.path.join(topic_dir, "MOC_Categories.md")
    with open(moc_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    log(f"  Written: {moc_path}")


# Slug lookup helper
_slug_cache = {}


def _num_to_slug(num):
    """논문 번호 → slug 변환."""
    global _slug_cache
    if not _slug_cache:
        idx_path = os.path.join(PAPERS_DIR, "_papers_index.json")
        if os.path.exists(idx_path):
            with open(idx_path, "r", encoding="utf-8") as f:
                for p in json.load(f):
                    n = p["slug"].split("_")[0]
                    _slug_cache[n] = p["slug"]
    return _slug_cache.get(num, num)


def main():
    parser = argparse.ArgumentParser(description="Generate Obsidian MOC files")
    parser.add_argument("--topic", default="ai4s")
    args = parser.parse_args()

    topic = args.topic
    topic_dir = str(get_topic_dir(topic))

    log(f"Generating MOC for {topic}...")
    generate_moc_insights(topic, topic_dir)
    generate_moc_categories(topic, topic_dir)
    log("Done!")


if __name__ == "__main__":
    main()
