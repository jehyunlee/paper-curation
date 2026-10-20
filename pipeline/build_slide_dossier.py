#!/usr/bin/env python3
"""덱 재집필용 근거 묶음(dossier) 내보내기.

`build_slide_deck.py` / `lib/slide_prose_ai4s.py` 의 집필본은 분류체계에 묶인
손 산출물이라, topic_modeling 이 대분류를 다시 짜면 TaxonomyMismatch 로 빌드가
거부된다. 이 스크립트는 그때 재집필자(사람 또는 보조 에이전트)에게 넘길 근거를
카테고리별 JSON 으로 뽑는다 — 덱이 실제로 읽는 것과 같은 파일에서, 같은 규칙
(recount_categories / match_timeline / pick 순서) 으로.

출력: reports/slide-dossier/<topic>/_frame.json + <category-slug>.json
"""
import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

PIPE = Path(__file__).resolve().parent
sys.path.insert(0, str(PIPE))

import build_slide_deck as B  # noqa: E402
from config_loader import PAPERS_DIR, get_topic_dir  # noqa: E402


def _read(path):
    if not path.exists():
        raise SystemExit(f"[ERROR] 필요한 파일이 없습니다: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def _slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def _paper_row(p):
    return {
        "slug": p.get("slug"),
        "title": B.clean_title(p.get("title", "")),
        "date": p.get("date"),
        "score": p.get("score"),
        "citations": p.get("citation_count") or 0,
        "essence": (p.get("essence") or "")[:260],
    }


def _newest_reviews(pool, limit=4):
    """가장 최근에 리뷰된 논문. 피인용 0인 신규 유입분이 순위 목록에서 밀려나도
    집필자가 볼 수 있게 따로 실는다(리뷰 날짜가 없는 논문은 제외)."""
    dated = [p for p in pool if p.get("review_date")]
    dated.sort(key=lambda p: str(p.get("review_date")), reverse=True)
    return [_paper_row(p) | {"review_date": p.get("review_date")} for p in dated[:limit]]


def _rank_papers(pool, since, limit):
    """덱의 레퍼런스 선정과 같은 우선순위: since 이후 → 피인용 → 최신."""
    ordered = sorted(pool, key=lambda p: (0 if B.year_of(p.get("date")) >= since else 1,
                                          -(int(p.get("citation_count") or 0)),
                                          -B.year_of(p.get("date")),
                                          -float(p.get("score") or 0)))
    return [_paper_row(p) for p in ordered[:limit]]


def build_dossier(topic, per_category=5, since=2025, papers_per_sub=16):
    tdir = get_topic_dir(topic)
    summaries = _read(tdir / "_category_summaries.json")
    classification = _read(tdir / "_new_classification.json")
    timeline = _read(tdir / "_timeline_narrative.json")
    ins_path = tdir / "_insights.json"
    insights = json.loads(ins_path.read_text(encoding="utf-8")) if ins_path.exists() else {}
    index = _read(Path(PAPERS_DIR) / "_papers_index.json")
    B.recount_categories(summaries, classification)

    assigned = {a["slug"]: a for a in classification.get("assignments", [])}
    idx_by_slug = {p["slug"]: p for p in index}
    papers = [idx_by_slug[s] for s in assigned if s in idx_by_slug]
    by_sub = defaultdict(list)
    for slug, a in assigned.items():
        p = idx_by_slug.get(slug)
        if p:
            by_sub[(a.get("primary_category"), a.get("sub_category"))].append(p)

    years = Counter()
    for p in papers:
        y = B.year_of(p.get("date"))
        if 2015 <= y <= 2030:
            years[y] += 1
    total = len(papers)
    analyses = timeline.get("category_analyses", {})
    cats = sorted(summaries, key=lambda c: -c.get("count", 0))
    cards_total = sum(c.get("card_count", 0) for c in cats)
    per_cat_ins = (insights.get("per_category") or {})

    frame = {
        "topic": topic, "total": total, "cards_total": cards_total, "since": since,
        "years": {str(y): years[y] for y in sorted(years)},
        "recent_share": round(sum(v for y, v in years.items() if y >= since) / max(1, total) * 100),
        "n_subs": sum(len(c.get("sub_themes", [])) for c in cats),
        "categories": [{
            "category": c["category"], "count": c.get("count", 0),
            "card_count": c.get("card_count", 0),
            "share_pct": round(c.get("count", 0) / max(1, total) * 100),
            "n_subs": len(c.get("sub_themes", [])),
            "top_subs": [s["name"] for s in sorted(c.get("sub_themes", []),
                                                   key=lambda s: -s.get("count", 0))[:per_category]],
            "description_ko": c.get("description_ko") or c.get("description", ""),
        } for c in cats],
        "executive_summary_ko": timeline.get("executive_summary_ko", ""),
        "cross_category": insights.get("cross_category", []),
        "meta": insights.get("meta", {}),
    }

    dossiers = []
    for rank, c in enumerate(cats, start=1):
        cat = c["category"]
        subs_sorted = sorted(c.get("sub_themes", []), key=lambda s: -s.get("count", 0))
        top = subs_sorted[:per_category]
        covered = sum(s.get("count", 0) for s in top)
        entry = {
            "category": cat, "rank": rank, "count": c.get("count", 0),
            "card_count": c.get("card_count", 0),
            "share_pct": round(c.get("count", 0) / max(1, total) * 100),
            "description_ko": c.get("description_ko") or c.get("description", ""),
            "avg_score": c.get("avg_score"),
            "n_subs": len(subs_sorted),
            "top_cover_pct": round(covered / max(1, c.get("count", 1)) * 100),
            "all_subs": [{"name": s["name"], "count": s.get("count", 0)} for s in subs_sorted],
            "insight": per_cat_ins.get(cat, {}),
            "sub_themes": [],
        }
        for st in top:
            name = st["name"]
            tl = B.match_timeline(analyses, cat, name) or {}
            pool = by_sub.get((cat, name), [])
            n_recent = sum(1 for p in pool if B.year_of(p.get("date")) >= since)
            entry["sub_themes"].append({
                "name": name, "count": st.get("count", 0),
                "share_of_category_pct": round(st.get("count", 0) / max(1, c.get("count", 1)) * 100),
                "recent_count": n_recent,
                "description_ko": st.get("description_ko") or st.get("description", ""),
                "timeline": {
                    "alias": tl.get("name") if tl.get("name") != name else "",
                    "start": tl.get("start"), "end": tl.get("end"), "status": tl.get("status"),
                    "key_developments": tl.get("key_developments") or [],
                    "representative_tools": tl.get("representative_tools") or [],
                } if tl else None,
                "papers": _rank_papers(pool, since, papers_per_sub),
                "newest_reviews": _newest_reviews(pool),
                "years": dict(sorted(Counter(B.year_of(p.get("date")) for p in pool).items())),
            })
        dossiers.append(entry)
    return frame, dossiers


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--topic", default="ai4s")
    ap.add_argument("--per-category", type=int, default=5)
    ap.add_argument("--since", type=int, default=2025)
    ap.add_argument("--papers-per-sub", type=int, default=16)
    ap.add_argument("--out", default=None, help="기본 reports/slide-dossier/<topic>")
    args = ap.parse_args()

    frame, dossiers = build_dossier(args.topic, args.per_category, args.since, args.papers_per_sub)
    out = Path(args.out) if args.out else B.REPORTS / "slide-dossier" / args.topic
    out.mkdir(parents=True, exist_ok=True)
    (out / "_frame.json").write_text(json.dumps(frame, ensure_ascii=False, indent=2), encoding="utf-8")
    for d in dossiers:
        (out / f"{_slug(d['category'])}.json").write_text(
            json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[dossier] {args.topic}: {len(dossiers)} categories, "
          f"{sum(len(d['sub_themes']) for d in dossiers)} sub-themes → {out}")
    for d in dossiers:
        print(f"  {d['rank']:2}. {d['category']} ({d['count']}/{d['card_count']}) "
              f"subs={[s['count'] for s in d['sub_themes']]}")


if __name__ == "__main__":
    main()
