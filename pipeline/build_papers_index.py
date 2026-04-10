"""
papers/_papers_index.json 재생성.

모든 papers/{slug}/review.md를 파싱하여 마스터 인덱스를 생성한다.

Usage:
  PYTHONUTF8=1 python build_papers_index.py
  PYTHONUTF8=1 python build_papers_index.py --topic ai4s  # topics 필드에 topic 할당
"""

import argparse
import json
import os
import re

from config_loader import PAPERS_DIR as _PAPERS_DIR, get_papers_index_path
PAPERS_DIR = str(_PAPERS_DIR)


from lib.dateutil import normalize_date as normalize_date_to_yyyymm


def parse_review(slug):
    """review.md에서 메타데이터와 평가 점수를 추출."""
    review_path = os.path.join(PAPERS_DIR, slug, "review.md")
    if not os.path.exists(review_path):
        return None

    with open(review_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Title
    title_m = re.search(r'^#\s+(.+)', content, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else slug

    # Authors
    authors_m = re.search(r'\*\*저자\*\*:\s*(.+?)(?:\s*\|)', content)
    authors = [a.strip() for a in authors_m.group(1).split(",")] if authors_m else []

    # Date — normalize to YYYY.MM
    date_m = re.search(r'\*\*날짜\*\*:\s*(.+?)(?:\s*\||\s*$)', content, re.MULTILINE)
    date_raw = date_m.group(1).strip() if date_m else ""
    date = normalize_date_to_yyyymm(date_raw)

    # DOI
    doi_m = re.search(r'\*\*DOI\*\*:\s*\[?([^\]\s\)]+)', content)
    doi = doi_m.group(1).strip() if doi_m else ""

    # Essence
    essence = ""
    ess_m = re.search(r'## Essence\s*\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
    if ess_m:
        lines = [l.strip() for l in ess_m.group(1).strip().split('\n')
                 if l.strip() and not l.strip().startswith('![') and not l.strip().startswith('*')]
        essence = " ".join(lines)[:300]

    # Scores
    scores = {}
    for label, key in [("Novelty", "novelty"), ("Technical Soundness", "tech"),
                        ("Significance", "sig"), ("Clarity", "clarity"), ("Overall", "overall")]:
        m = re.search(rf'{label}\D*(\d+(?:\.\d+)?)\s*/\s*5', content)
        if m:
            scores[key] = float(m.group(1))

    # Verdict
    verdict_m = re.search(r'\*\*총평\*\*[:\s]*(.+?)(?:\n|$)', content)
    verdict = verdict_m.group(1).strip() if verdict_m else ""

    # Figures
    fig_dir = os.path.join(PAPERS_DIR, slug, "figures")
    has_figs = os.path.isdir(fig_dir) and any(f.endswith(('.png', '.webp')) for f in os.listdir(fig_dir))

    # Has PDF (text.md exists = had PDF)
    has_pdf = os.path.exists(os.path.join(PAPERS_DIR, slug, "text.md"))

    return {
        "title": title,
        "authors": authors[:5],
        "date": date,
        "doi": doi,
        "essence": essence,
        "score": scores.get("overall", 0),
        "has_pdf": has_pdf,
        "has_figures": has_figs,
        "verdict": verdict,
    }


def main():
    parser = argparse.ArgumentParser(description="Rebuild _papers_index.json")
    parser.add_argument("--topic", default="ai4s", help="Topic to assign to papers")
    args = parser.parse_args()

    # Load existing index to preserve classifications
    index_path = os.path.join(PAPERS_DIR, "_papers_index.json")
    existing = {}
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            for p in json.load(f):
                existing[p["slug"]] = p

    # Scan all paper directories
    index = []
    for slug in sorted(os.listdir(PAPERS_DIR)):
        slug_dir = os.path.join(PAPERS_DIR, slug)
        if not os.path.isdir(slug_dir) or not slug[0].isdigit():
            continue

        parsed = parse_review(slug)
        if not parsed:
            continue

        # Preserve existing data
        prev = existing.get(slug, {})

        # Migrate old flat fields → classifications[topic] structure
        # Only migrate into the topic that matches --topic arg (prevents cross-contamination)
        classifications = prev.get("classifications", {})
        if not classifications and prev.get("primary_category"):
            # Old schema: migrate flat fields into the primary_topic only
            primary_topic = prev.get("primary_topic", args.topic)
            classifications[primary_topic] = {
                "primary_category": prev.get("primary_category", ""),
                "all_categories": prev.get("all_categories", []),
                "sub_category": prev.get("sub_category", ""),
            }

        entry = {
            "slug": slug,
            "title": parsed["title"],
            "authors": parsed["authors"],
            "date": parsed["date"],
            "doi": parsed["doi"],
            "topics": prev.get("topics", [args.topic]),
            "primary_topic": prev.get("primary_topic", args.topic),
            "classifications": classifications,
            "score": parsed["score"],
            "essence": parsed["essence"],
            "has_pdf": parsed["has_pdf"],
            "has_figures": parsed["has_figures"],
            "review_date": prev.get("review_date", ""),
        }
        index.append(entry)

    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    with_scores = sum(1 for p in index if p["score"] > 0)
    with_cats = sum(1 for p in index if p.get("classifications"))
    print(f"Generated _papers_index.json: {len(index)} papers")
    print(f"  With scores: {with_scores}")
    print(f"  With category: {with_cats}")
    print(f"  With essence: {sum(1 for p in index if p['essence'])}")


if __name__ == "__main__":
    main()
