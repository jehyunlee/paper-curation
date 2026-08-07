"""AI4Science 발표 원고 v2 — 슬라이드 50장을 '줄글'로 쓴 판본.

v1(`build_slide_deck.py`)이 불릿 요약 카드였다면, v2는 슬라이드 한 장당
책 한 절(section) 분량의 서술형 본문을 싣는다. 데이터·레퍼런스·인용 마커
로직은 v1 모듈을 그대로 재사용하고, 본문 줄글만 `lib/slide_prose_ai4s.py`
에서 가져온다.

  - `reports/build/{topic}_slides_50_v2.html`  : 브라우저·인쇄용(자기완결)
  - `reports/source/{topic}_slides_50_v2.md`   : Obsidian 용

Usage:
  PYTHONUTF8=1 python pipeline/build_slide_essay.py --topic ai4s
"""
import argparse
import html as H
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

PIPE = Path(__file__).resolve().parent
sys.path.insert(0, str(PIPE))
PROJECT_ROOT = PIPE.parent

import build_slide_deck as B  # noqa: E402
from lib.atomic_io import atomic_write_text  # noqa: E402
from lib.slide_prose_ai4s import PROSE  # noqa: E402

REPORTS = PROJECT_ROOT / "reports"

# 오프닝·종합 슬라이드의 고정 골격 (제목·표시 헤드라인). 본문은 PROSE 에서 온다.
FRAME = [
    ("cover", "표지", "오프닝", "AI for Science, 2026년 지형도",
     "논문 한 편씩 읽어서는 보이지 않는 것 — 어디에 사람이 몰렸고, 어디가 비었는가."),
    ("method", "방법", "오프닝", "이 지도는 어떻게 만들어졌나",
     "사람이 카테고리를 먼저 정하지 않았다. 논문이 뭉친 모양에서 카테고리를 꺼냈다."),
    ("corpus", "코퍼스", "오프닝", "코퍼스 한눈에 보기",
     "이 코퍼스는 '누적 지식'이 아니라 '현재 전선'에 가깝다."),
    ("landscape", "지형도", "오프닝", "여덟 개 대분류의 지형",
     "'만드는 연구'와 '재는 연구'가 나란히 1·2위. 이 조합이 2026년의 성격이다."),
    ("arc", "서사", "오프닝", "관통하는 한 줄: 예측 → 설계 → 자율 → 검증",
     "2026년은 '무엇을 더 할 수 있나'가 아니라 '무엇을 믿을 수 있나'를 묻는 해다."),
]

CLOSING = [
    ("convergence", "종합", "수렴 신호: 경계가 무너지는 곳",
     "서로 다른 분야가 같은 문제를 풀기 시작하면, 그 지점이 다음 3년의 표준이 된다."),
    ("riseandfall", "종합", "부상과 쇠퇴",
     "단독 LLM으로 과학하겠다는 접근은 접히는 중이고, 그 자리를 신경-기호와 추론시간 확장이 채운다."),
    ("gaps", "종합", "비어 있는 자리",
     "가장 큰 공백은 기술이 아니다 — AI가 만든 과학을 검증할 체계가 없다."),
    ("verification", "종합", "2026 검증 전환의 여섯 축",
     "같은 해에, 서로 모르는 여덟 개 분야가 같은 결론에 도달했다 — 성능이 아니라 증거."),
    ("action", "마무리", "그래서 무엇을 할 것인가",
     "따라잡기 경쟁은 이미 졌다. 이길 수 있는 자리는 검증·도메인 데이터·대형시설이다."),
]


def prose_for(key, fallback_points=None):
    """줄글 본문을 가져온다. 아직 집필되지 않은 칸은 v1 불릿으로 임시 대체한다."""
    p = PROSE.get(key)
    if p:
        return {"lead": p.get("lead", ""), "body": list(p.get("body", [])),
                "close": p.get("close", ""), "drafted": True}
    return {"lead": "", "body": list(fallback_points or []), "close": "", "drafted": False}


def build(topic, per_category=5, link_base="../../docs/papers", since=2025):
    summaries, classification, timeline, insights, index = B.load_corpus(topic)
    assigned = {a["slug"]: a for a in classification.get("assignments", [])}
    idx_by_slug = {p["slug"]: p for p in index}
    papers = [idx_by_slug[s] for s in assigned if s in idx_by_slug]

    by_prefix = {}
    for p in index:
        by_prefix.setdefault(p["slug"].split("_")[0], p)

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

    analyses = timeline.get("category_analyses", {})
    cats = sorted(summaries, key=lambda c: -c.get("count", 0))
    total = len(papers)
    recent_share = round(sum(v for y, v in years.items() if y >= since) / max(1, total) * 100)
    n_subs = sum(len(c.get("sub_themes", [])) for c in cats)

    slides = []

    def add(**kw):
        kw["no"] = len(slides) + 1
        kw.setdefault("refs", [])
        kw.setdefault("badges", [])
        kw.setdefault("tools", [])
        slides.append(kw)
        return kw

    # ── 오프닝 5장 ─────────────────────────────────────────────────────────
    ymax = max(years.values()) if years else 1
    frame_tables = {
        "corpus": {"head": ["연도", "편수", ""],
                   "rows": [[str(y), f"{years[y]:,}편",
                             "█" * max(1, round(years[y] / ymax * 30))]
                            for y in sorted(years) if y >= 2018]},
        "landscape": {"head": ["대분류", "고유 배정", "중복 포함", "서브카테고리",
                               "최대 서브카테고리"],
                      "rows": [[B.CATEGORY_KO.get(c["category"], c["category"]),
                                f"{c.get('count', 0):,}", f"{c.get('card_count', 0):,}",
                                str(len(c.get("sub_themes", []))),
                                (sorted(c.get("sub_themes", []),
                                        key=lambda s: -s.get("count", 0))[0]["name"]
                                 if c.get("sub_themes") else "-")] for c in cats]},
    }
    for key, kind, part, title, headline in FRAME:
        pr = prose_for(key)
        add(key=key, kind=kind, part=part, title_ko=title, headline=headline,
            lead=pr["lead"], body=pr["body"], close=pr["close"], drafted=pr["drafted"],
            table=frame_tables.get(key),
            stat_line=(f"코퍼스 {total:,}편 · 대분류 {len(cats)}개 · 서브카테고리 {n_subs}개 · "
                       f"{since}년 이후 {recent_share}%" if key == "cover" else ""))

    # ── 본문 40장 ──────────────────────────────────────────────────────────
    for ci, c in enumerate(cats, start=1):
        cat = c["category"]
        cat_ko = B.CATEGORY_KO.get(cat, cat)
        part = f"제{ci}부 · {cat_ko}"
        subs = sorted(c.get("sub_themes", []), key=lambda s: -s.get("count", 0))[:per_category]
        share = round(sum(s.get("count", 0) for s in subs) / max(1, c.get("count", 1)) * 100)
        for si, st in enumerate(subs, start=1):
            name = st.get("name")
            tl = B.match_timeline(analyses, cat, name)
            nar = B.NARRATIVE.get(name, {})
            tools = (tl or {}).get("representative_tools", []) or []
            kds = [re.sub(r"\s+", " ", k) for k in ((tl or {}).get("key_developments") or [])]
            pr = prose_for(name, fallback_points=nar.get("points") or kds)

            texts = ([pr["lead"]] if pr["lead"] else []) + pr["body"] + \
                    ([pr["close"]] if pr["close"] else [])
            named = [w for w in re.findall(r"[A-Za-z][A-Za-z0-9]*(?:[-–][A-Za-z0-9]+)*",
                                          " ".join(texts))
                     if len(w) >= 4 and (sum(1 for ch in w if ch.isupper()) >= 2
                                         or any(ch.isdigit() for ch in w))]
            probes = named + list(B._tokens(name)) + [w for k in kds
                                                      for w in re.findall(r"[A-Z][A-Za-z0-9\-]{3,}", k)]
            pool = by_sub.get((cat, name), [])
            refs = B.pick_papers(pool, tools, probes, link_base, limit=6, since=since)
            body_text = " ".join(texts)
            forced = [p for p in pool if B.title_phrase_hit(p, body_text)]
            if forced:
                seen, merged = set(), []
                for r in [B.make_ref(p, link_base) for p in forced] + refs:
                    fp = B.title_fingerprint(r["title"])
                    if fp in seen:
                        continue
                    seen.add(fp)
                    merged.append(r)
                refs = merged[:max(6, len(forced) + 4)]

            marked = B.attach_markers(texts, refs, tools)
            lead = marked[0] if pr["lead"] else ""
            offset = 1 if pr["lead"] else 0
            body = marked[offset:offset + len(pr["body"])]
            close = marked[-1] if pr["close"] else ""

            n_recent = sum(1 for p in pool if B.year_of(p.get("date")) >= since)
            badges = [f"{st.get('count', 0)}편"]
            if tl:
                badges += [f"{tl.get('start')}–{tl.get('end')}",
                           B.STATUS_KO.get(tl.get("status"), "")]
            badges.append(f"{since}+ {n_recent}편")

            add(key=name, kind="서브카테고리", part=part, category=cat, category_ko=cat_ko,
                title_ko=nar.get("ko") or name, title_en=name,
                alias_en=((tl or {}).get("name") if (tl and tl.get("name") != name) else ""),
                badges=[b for b in badges if b],
                context=(B.CATEGORY_LEAD.get(cat, "") if si == 1 else ""),
                cat_meta=(f"{cat_ko} 고유 배정 {c.get('count', 0):,}편"
                          f"(중복 포함 {c.get('card_count', 0):,}편 · 웹 인덱스 기준) · 서브카테고리 "
                          f"{len(c.get('sub_themes', []))}개 · 본 파트 {len(subs)}개로 {share}% 커버"
                          if si == 1 else ""),
                headline=nar.get("headline") or "",
                lead=lead, body=body, close=close, drafted=pr["drafted"],
                tools=tools, refs=refs, sowhat=nar.get("sowhat") or "")

    # ── 종합 5장 ───────────────────────────────────────────────────────────
    cross = insights.get("cross_category", []) or []
    by_type = defaultdict(list)
    for item in cross:
        by_type[item.get("type")].append(item)
    meta = insights.get("meta", {}) or {}

    def insight_refs(items, limit=6):
        pool = [by_prefix[str(ev)] for it in items for ev in it.get("evidence", [])
                if str(ev) in by_prefix]
        seen, uniq = set(), []
        for p in sorted(pool, key=lambda p: (0 if B.year_of(p.get("date")) >= since else 1,
                                            -B.year_of(p.get("date")),
                                            -(p.get("citation_count") or 0))):
            if p["slug"] in seen:
                continue
            seen.add(p["slug"])
            uniq.append(B.make_ref(p, link_base))
            if len(uniq) >= limit:
                break
        return uniq

    closing_refs = {
        "convergence": insight_refs(by_type.get("convergence", [])),
        "riseandfall": insight_refs(by_type.get("emerging", []) + by_type.get("declining", [])),
        "gaps": insight_refs(by_type.get("gap", [])),
        "verification": [],
        "action": [],
    }
    closing_extra = {
        "gaps": {"미개척 영역(코퍼스 메타 분석)": meta.get("underserved_domains") or []},
        "action": {"관전 포인트 (다음 12개월)": [
            "자율 에이전트의 습식 검증 성공률이 공개 벤치마크에서 재현되는가",
            "형식 검증기가 수학 밖(재료·코드·회로)으로 얼마나 확장되는가",
            "AI 수치예보의 극단 이벤트 외삽에 대한 독립 검증 결과",
            "AI 생성 논문·리뷰에 대한 학회·출판사 표준의 성립 여부",
        ]},
    }
    for key, kind, title, headline in CLOSING:
        pr = prose_for(key)
        refs = closing_refs.get(key) or []
        texts = ([pr["lead"]] if pr["lead"] else []) + pr["body"] + \
                ([pr["close"]] if pr["close"] else [])
        marked = B.attach_markers(texts, refs, [])
        lead = marked[0] if pr["lead"] else ""
        offset = 1 if pr["lead"] else 0
        add(key=key, kind=kind, part="종합", title_ko=title, headline=headline,
            lead=lead, body=marked[offset:offset + len(pr["body"])],
            close=marked[-1] if pr["close"] else "",
            drafted=pr["drafted"], refs=refs, extra=closing_extra.get(key))

    chars = sum(len(t) for s in slides
                for t in [s.get("lead", ""), s.get("close", "")] + list(s.get("body", [])))
    stats = {"total": total, "categories": cats, "years": years, "n_subs": n_subs,
             "per_category": per_category, "since": since, "recent_share": recent_share,
             "link_base": link_base, "chars": chars,
             "drafted": sum(1 for s in slides if s.get("drafted"))}
    return slides, stats


# ── 렌더링: HTML ──────────────────────────────────────────────────────────
CSS = """
:root{--accent:__ACCENT__;--ink:#1a1a1a;--muted:#5f5f5f;--soft:#9a9a9a;
--rule:#e3e3e0;--bg:#f3f2ef;--card:#fffefb}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{background:var(--bg);color:var(--ink);line-height:1.9;-webkit-font-smoothing:antialiased;
font-family:-apple-system,BlinkMacSystemFont,"Pretendard","Apple SD Gothic Neo","Noto Sans KR",sans-serif}
a{color:inherit}
.wrap{max-width:900px;margin:0 auto;padding:52px 26px 96px}
header.deck{border-bottom:3px solid var(--ink);padding-bottom:24px}
header.deck .eyebrow{font-size:11.5px;letter-spacing:.24em;color:var(--accent);font-weight:700;text-transform:uppercase}
header.deck h1{font-size:34px;line-height:1.28;margin:.4em 0 .3em;letter-spacing:-.024em}
header.deck p.lede{margin:0;color:var(--muted);font-size:15px;line-height:1.8}
.stats{display:flex;flex-wrap:wrap;gap:9px;margin:22px 0 0}
.stat{background:var(--card);border:1px solid var(--rule);border-radius:10px;padding:9px 14px;min-width:112px}
.stat b{display:block;font-size:20px;letter-spacing:-.01em}
.stat span{font-size:11px;color:var(--muted)}
nav.toc{background:var(--card);border:1px solid var(--rule);border-radius:12px;padding:20px 22px;margin:28px 0 34px}
nav.toc h2{font-size:12px;letter-spacing:.16em;color:var(--soft);margin:0 0 12px;text-transform:uppercase}
nav.toc ol{margin:0;padding:0;list-style:none;display:grid;
grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:1px 20px}
nav.toc li{font-size:12.8px;color:var(--muted);padding:1px 0;line-height:1.7}
nav.toc li a{text-decoration:none}
nav.toc li a:hover{color:var(--accent)}
nav.toc li .n{display:inline-block;min-width:36px;color:var(--soft);font-size:11.5px;font-variant-numeric:tabular-nums}
nav.toc li.part{margin-top:10px;font-weight:700;color:var(--ink);font-size:12px;grid-column:1/-1;
border-top:1px solid var(--rule);padding-top:9px}
.slide{background:var(--card);border:1px solid var(--rule);border-radius:14px;
padding:38px 46px 32px;margin:0 0 22px;scroll-margin-top:14px}
.rail{display:flex;align-items:center;gap:9px;margin-bottom:16px}
.rail .no{background:var(--ink);color:#fff;font-size:11.5px;font-weight:700;letter-spacing:.06em;
padding:3px 9px;border-radius:5px;font-variant-numeric:tabular-nums}
.rail .kind{font-size:10.5px;letter-spacing:.15em;color:var(--accent);font-weight:700;text-transform:uppercase}
.rail .part{font-size:11.5px;color:var(--soft);margin-left:auto}
.slide h2{font-size:27px;line-height:1.32;margin:0 0 6px;letter-spacing:-.024em}
.slide .en{font-size:12.8px;color:var(--muted);margin:0;font-style:italic}
.slide .alias{font-size:11.5px;color:var(--soft);margin:3px 0 0}
.badges{display:flex;flex-wrap:wrap;gap:6px;margin:14px 0 0}
.badge{font-size:11.5px;border:1px solid var(--rule);border-radius:20px;padding:2px 11px;color:var(--muted);background:#fafaf8}
.badge.n{border-color:var(--accent);color:var(--accent);font-weight:700}
.badge.recent{border-color:#c9c9c5;color:#4a4a48;font-weight:600}
.badge.st-가속{background:#fdf1ef;border-color:#f0c6bf;color:#a8291a}
.badge.st-부상{background:#f1f6fd;border-color:#c3d8f0;color:#1f5b9e}
.badge.st-안정{background:#f5f5f3;border-color:#dcdcda;color:#5a5a58}
.badge.st-감소{background:#f7f7f6;border-color:#e2e2e0;color:#8a8a88}
.catmeta{font-size:11.8px;color:var(--soft);margin:11px 0 0}
.context{margin:18px 0 0;padding:11px 16px;border-left:3px solid var(--rule);background:#faf9f6;
color:var(--muted);font-size:13.6px;border-radius:0 6px 6px 0;line-height:1.75}
.onscreen{margin:22px 0 6px;padding:16px 20px;background:#fbf5f4;border-left:4px solid var(--accent);
border-radius:0 8px 8px 0}
.onscreen b{display:block;font-size:10.5px;letter-spacing:.16em;color:var(--accent);
text-transform:uppercase;margin-bottom:6px;font-weight:700}
.onscreen p{margin:0;font-size:17.5px;font-weight:600;line-height:1.6;letter-spacing:-.012em}
p.lead{font-size:17px;line-height:1.85;margin:26px 0 0;font-weight:500;color:#111}
p.para{font-size:15.6px;line-height:1.95;margin:17px 0 0;word-break:keep-all}
p.close{font-size:15.8px;line-height:1.9;margin:22px 0 0;padding:15px 19px;background:#f6f7f9;
border:1px solid #e2e5ea;border-radius:9px;word-break:keep-all}
sup.cite{font-size:10.5px;font-weight:700;color:var(--accent);vertical-align:super;margin-left:1px}
table.grid{width:100%;border-collapse:collapse;margin:22px 0 4px;font-size:13.3px;line-height:1.6}
table.grid th{text-align:left;font-size:11px;letter-spacing:.08em;color:var(--soft);text-transform:uppercase;
border-bottom:2px solid var(--ink);padding:7px 10px 7px 0}
table.grid td{border-bottom:1px solid var(--rule);padding:7px 10px 7px 0;vertical-align:top}
table.grid td:nth-child(2){font-variant-numeric:tabular-nums;white-space:nowrap}
table.grid td:last-child{color:var(--accent);letter-spacing:-1px}
.block-label{font-size:10.5px;letter-spacing:.16em;color:var(--soft);text-transform:uppercase;
margin:26px 0 8px;font-weight:700}
.tools{display:flex;flex-wrap:wrap;gap:5px}
.tool{font-size:11.8px;background:#f4f4f1;border:1px solid var(--rule);border-radius:5px;padding:2px 8px;color:#444}
ul.plain{margin:0;padding-left:20px}
ul.plain li{font-size:14.6px;line-height:1.85;margin-bottom:6px}
ol.refs{margin:0;padding-left:22px}
ol.refs li{font-size:13.2px;margin-bottom:8px;line-height:1.65}
ol.refs a{font-weight:600;text-decoration:none;border-bottom:1px solid rgba(0,0,0,.18)}
ol.refs a:hover{color:var(--accent);border-bottom-color:var(--accent)}
ol.refs .m{color:var(--soft);font-size:11.8px;font-variant-numeric:tabular-nums}
ol.refs .e{display:block;color:var(--muted);font-size:12.4px;margin-top:2px}
.appendix{background:var(--card);border:1px solid var(--rule);border-radius:14px;padding:30px 40px}
.appendix h2{font-size:21px;margin:0 0 4px}
.appendix p.sub{color:var(--muted);font-size:12.5px;margin:0 0 16px}
.appendix ol{padding-left:24px;margin:0}
.appendix li{font-size:13px;margin-bottom:6px;line-height:1.65}
footer.deck{margin-top:36px;padding-top:18px;border-top:1px solid var(--rule);
font-size:11.5px;color:var(--soft);text-align:center;line-height:1.8}
@media print{
 body{background:#fff}
 .wrap{max-width:none;padding:0}
 header.deck,nav.toc{page-break-after:always}
 .slide{page-break-inside:avoid;page-break-after:always;border:none;border-radius:0;padding:14px 0;margin:0}
 @page{size:A4;margin:16mm}
}
"""


def _inline(text):
    out = H.escape(str(text))
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"`(.+?)`", r"<code>\1</code>", out)
    out = re.sub(r"\[(\d+)\]", r'<sup class="cite">[\1]</sup>', out)
    return out


def render_html(topic, slides, stats):
    today = datetime.now().strftime("%Y-%m-%d")
    css = CSS.replace("__ACCENT__", B.ACCENT.get(topic, "#D63423"))
    o = ["<!DOCTYPE html><html lang='ko'><head><meta charset='utf-8'>",
         "<meta name='viewport' content='width=device-width,initial-scale=1'>",
         f"<title>AI for Science 발표 원고 v2 — 슬라이드 {len(slides)}장 ({topic})</title>",
         f"<style>{css}</style></head><body><div class='wrap'>"]

    o.append("<header class='deck'>")
    o.append(f"<div class='eyebrow'>{H.escape(topic)} · slide essay v2 · {today}</div>")
    o.append(f"<h1>AI for Science 지형도 — 발표 원고 {len(slides)}장</h1>")
    o.append("<p class='lede'>슬라이드 한 장마다 책 한 절 분량의 줄글 본문을 실었다. "
             "맨 위 붉은 박스는 화면에 띄울 한 줄, 그 아래가 말할 내용이다. "
             f"사례는 {stats['since']}년 이후를 우선했고, 레퍼런스 제목을 클릭하면 해당 논문의 리뷰 문서로 이동한다.</p>")
    o.append("<div class='stats'>")
    for value, label in [(f"{stats['total']:,}", "코퍼스 논문"),
                         (str(len(stats["categories"])), "대분류"),
                         (str(stats["n_subs"]), "서브카테고리"),
                         (str(len(slides)), "슬라이드"),
                         (f"{stats['chars']:,}", "본문 글자수"),
                         (f"{stats['recent_share']}%", f"{stats['since']}년 이후 비중")]:
        o.append(f"<div class='stat'><b>{value}</b><span>{H.escape(label)}</span></div>")
    o.append("</div></header>")

    o.append("<nav class='toc'><h2>목차</h2><ol>")
    cur = None
    for s in slides:
        if s["part"] != cur:
            cur = s["part"]
            o.append(f"<li class='part'>{H.escape(cur)}</li>")
        badge = f" · {H.escape(s['badges'][0])}" if s.get("badges") else ""
        o.append(f"<li><a href='#s{s['no']:02d}'><span class='n'>S{s['no']:02d}</span>"
                 f"{H.escape(s['title_ko'])}</a>{badge}</li>")
    o.append("</ol></nav>")

    for s in slides:
        o.append(f"<section class='slide' id='s{s['no']:02d}'>")
        o.append(f"<div class='rail'><span class='no'>S{s['no']:02d}</span>"
                 f"<span class='kind'>{H.escape(s['kind'])}</span>"
                 f"<span class='part'>{H.escape(s['part'])}</span></div>")
        o.append(f"<h2>{H.escape(s['title_ko'])}</h2>")
        if s.get("title_en"):
            o.append(f"<p class='en'>{H.escape(s['title_en'])}</p>")
        if s.get("alias_en"):
            o.append(f"<p class='alias'>타임라인 분석 명칭: {H.escape(s['alias_en'])}</p>")
        if s.get("badges"):
            o.append("<div class='badges'>")
            for i, b in enumerate(s["badges"]):
                cls = ("badge n" if i == 0 else
                       "badge recent" if b.startswith(str(stats["since"])) else
                       f"badge st-{b}" if b in B.STATUS_KO.values() else "badge")
                o.append(f"<span class='{cls}'>{H.escape(b)}</span>")
            o.append("</div>")
        if s.get("stat_line"):
            o.append(f"<p class='catmeta'>{H.escape(s['stat_line'])}</p>")
        if s.get("cat_meta"):
            o.append(f"<p class='catmeta'>{H.escape(s['cat_meta'])}</p>")
        if s.get("context"):
            o.append(f"<div class='context'>{_inline(s['context'])}</div>")
        if s.get("headline"):
            o.append(f"<div class='onscreen'><b>슬라이드에 띄울 한 줄</b>"
                     f"<p>{_inline(s['headline'])}</p></div>")
        if s.get("lead"):
            o.append(f"<p class='lead'>{_inline(s['lead'])}</p>")
        if s.get("table"):
            o.append("<table class='grid'><thead><tr>")
            o += [f"<th>{H.escape(h)}</th>" for h in s["table"]["head"]]
            o.append("</tr></thead><tbody>")
            for row in s["table"]["rows"]:
                o.append("<tr>" + "".join(f"<td>{H.escape(str(x))}</td>" for x in row) + "</tr>")
            o.append("</tbody></table>")
        for para in s.get("body", []):
            o.append(f"<p class='para'>{_inline(para)}</p>")
        for label, items in (s.get("extra") or {}).items():
            items = [i for i in items if i]
            if items:
                o.append(f"<div class='block-label'>{H.escape(label)}</div><ul class='plain'>")
                o += [f"<li>{_inline(i)}</li>" for i in items]
                o.append("</ul>")
        if s.get("close"):
            o.append(f"<p class='close'>{_inline(s['close'])}</p>")
        if s.get("tools"):
            o.append("<div class='block-label'>대표 도구 · 시스템</div><div class='tools'>")
            o += [f"<span class='tool'>{H.escape(t)}</span>" for t in s["tools"]]
            o.append("</div>")
        if s.get("refs"):
            o.append("<div class='block-label'>레퍼런스 — 제목 클릭 시 논문 리뷰</div><ol class='refs'>")
            for r in s["refs"]:
                cit = f" · 인용 {r['citations']:,}" if r["citations"] else ""
                who = f"{H.escape(r['author'])}, " if r["author"] else ""
                o.append(f"<li><a href='{H.escape(r['url'])}'>{H.escape(r['title'])}</a> "
                         f"<span class='m'>{who}{H.escape(r['date'])}{cit}</span>"
                         + (f"<span class='e'>{H.escape(r['essence'])}</span>" if r["essence"] else "")
                         + "</li>")
            o.append("</ol>")
        o.append("</section>")

    seen, allrefs = set(), []
    for s in slides:
        for r in s.get("refs", []):
            if r["slug"] not in seen:
                seen.add(r["slug"])
                allrefs.append(r)
    allrefs.sort(key=lambda r: (-int(r["year"] or 0), r["title"]))
    o.append("<section class='appendix'>")
    o.append(f"<h2>부록 · 전체 레퍼런스 {len(allrefs)}편</h2>")
    o.append(f"<p class='sub'>모든 링크는 코퍼스 내 논문 리뷰 문서"
             f"({H.escape(stats['link_base'])}/&lt;slug&gt;/index.html)로 연결된다.</p><ol>")
    for r in allrefs:
        cit = f" · 인용 {r['citations']:,}" if r["citations"] else ""
        who = f"{H.escape(r['author'])}, " if r["author"] else ""
        o.append(f"<li><a href='{H.escape(r['url'])}'>{H.escape(r['title'])}</a> "
                 f"<span class='m'>{who}{H.escape(r['date'])}{cit}</span></li>")
    o.append("</ol></section>")
    o.append(f"<footer class='deck'>pipeline/build_slide_essay.py --topic {H.escape(topic)} · {today}"
             f"<br>근거 코퍼스 {stats['total']:,}편 · 본문 {stats['chars']:,}자</footer>")
    o.append("</div></body></html>")
    return "\n".join(o)


# ── 렌더링: Markdown (Obsidian) ────────────────────────────────────────────
def render_markdown(topic, slides, stats):
    today = datetime.now().strftime("%Y-%m-%d")
    L = ["---",
         f'title: "AI for Science 지형도 — 발표 원고 v2 ({len(slides)}장, 줄글)"',
         f"topic: {topic}",
         f"slides: {len(slides)}",
         f"corpus_papers: {stats['total']}",
         f"body_chars: {stats['chars']}",
         f"evidence_since: {stats['since']}",
         f"generated: {today}",
         "tags:"]
    L += [f"  - {t}" for t in ("ai4science", "발표원고", "연구동향", topic)]
    L += ["---", "",
          f"# AI for Science 지형도 — 발표 원고 {len(slides)}장 (v2 · 줄글)", "",
          f"> [!info] 읽는 법\n"
          f"> 슬라이드 한 장 = 절(section) 하나. `> [!abstract]` 는 **화면에 띄울 한 줄**, "
          f"그 아래 문단이 **말할 내용**이다.\n"
          f"> 코퍼스 **{stats['total']:,}편** · 대분류 **{len(stats['categories'])}개** · "
          f"서브카테고리 **{stats['n_subs']}개** 중 상위 **{stats['per_category']}개씩** · "
          f"본문 **{stats['chars']:,}자**.\n"
          f"> 사례는 **{stats['since']}년 이후 우선**(코퍼스의 {stats['recent_share']}%). "
          f"레퍼런스 링크는 논문별 리뷰 문서(`{stats['link_base']}/<slug>/index.html`)로 연결된다.",
          "", "## 목차", ""]
    cur = None
    for s in slides:
        if s["part"] != cur:
            cur = s["part"]
            L.append(f"- **{cur}**")
        badge = f" — {s['badges'][0]}" if s.get("badges") else ""
        L.append(f"    - `S{s['no']:02d}` {s['title_ko']}{badge}")
    L.append("")

    for s in slides:
        L += ["---", "", f"## S{s['no']:02d} · {s['title_ko']}", ""]
        meta = [f"*{s['part']}*"]
        if s.get("title_en"):
            meta.append(f"**{s['title_en']}**")
        meta.append(f"*{s['kind']}*")
        L.append(" · ".join(meta))
        if s.get("alias_en"):
            L += ["", f"<sub>타임라인 분석 명칭: {s['alias_en']}</sub>"]
        if s.get("badges"):
            L += ["", " ".join(f"`{b}`" for b in s["badges"])]
        if s.get("stat_line"):
            L += ["", f"<sub>{s['stat_line']}</sub>"]
        if s.get("cat_meta"):
            L += ["", f"<sub>{s['cat_meta']}</sub>"]
        L.append("")
        if s.get("context"):
            L += [f"> [!quote] 파트 도입\n> {s['context']}", ""]
        if s.get("headline"):
            L += [f"> [!abstract] 화면에 띄울 한 줄\n> {s['headline']}", ""]
        if s.get("lead"):
            L += [f"**{s['lead']}**", ""]
        if s.get("table"):
            head = s["table"]["head"]
            L.append("| " + " | ".join(head) + " |")
            L.append("|" + "|".join(["---"] * len(head)) + "|")
            L += ["| " + " | ".join(str(x) for x in row) + " |" for row in s["table"]["rows"]]
            L.append("")
        for para in s.get("body", []):
            L += [para, ""]
        for label, items in (s.get("extra") or {}).items():
            items = [i for i in items if i]
            if items:
                L += [f"**{label}**", ""] + [f"- {i}" for i in items] + [""]
        if s.get("close"):
            L += [f"> [!tip] 정리\n> {s['close']}", ""]
        if s.get("tools"):
            L += [f"**대표 도구·시스템** — {' · '.join(s['tools'])}", ""]
        if s.get("refs"):
            L += ["**레퍼런스** (제목 클릭 → 논문 리뷰)", ""]
            for i, r in enumerate(s["refs"], start=1):
                cit = f" · 인용 {r['citations']:,}" if r["citations"] else ""
                who = f"{r['author']}, " if r["author"] else ""
                L.append(f"{i}. [{r['title']}]({r['url']}) — {who}{r['date']}{cit}")
            L.append("")

    seen, allrefs = set(), []
    for s in slides:
        for r in s.get("refs", []):
            if r["slug"] not in seen:
                seen.add(r["slug"])
                allrefs.append(r)
    allrefs.sort(key=lambda r: (-int(r["year"] or 0), r["title"]))
    L += ["---", "", f"## 부록 · 전체 레퍼런스 {len(allrefs)}편", ""]
    for r in allrefs:
        cit = f" · 인용 {r['citations']:,}" if r["citations"] else ""
        who = f"{r['author']}, " if r["author"] else ""
        L.append(f"- [{r['title']}]({r['url']}) — {who}{r['date']}{cit}")
    L += ["",
          f"*생성: `pipeline/build_slide_essay.py --topic {topic}` · {today} · "
          f"근거 코퍼스 {stats['total']:,}편 · 본문 {stats['chars']:,}자*", ""]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description="토픽 코퍼스 → 줄글 발표 원고 v2 (HTML + Obsidian MD)")
    ap.add_argument("--topic", default="ai4s")
    ap.add_argument("--per-category", type=int, default=5)
    ap.add_argument("--since", type=int, default=2025)
    ap.add_argument("--link-base", default="../../docs/papers")
    ap.add_argument("--out-dir", default=None)
    args = ap.parse_args()

    slides, stats = build(args.topic, per_category=args.per_category,
                          link_base=args.link_base, since=args.since)
    root = Path(args.out_dir) if args.out_dir else REPORTS
    html_path = root / "build" / f"{args.topic}_slides_{len(slides)}_v2.html"
    md_path = root / "source" / f"{args.topic}_slides_{len(slides)}_v2.md"
    atomic_write_text(html_path, render_html(args.topic, slides, stats))
    atomic_write_text(md_path, render_markdown(args.topic, slides, stats))

    n_refs = len({r["slug"] for s in slides for r in s.get("refs", [])})
    todo = [f"S{s['no']:02d}" for s in slides if not s.get("drafted")]
    print(f"[OK] 슬라이드 {len(slides)}장 · 본문 {stats['chars']:,}자 · 레퍼런스 {n_refs}편")
    print(f"  HTML : {html_path}")
    print(f"  MD   : {md_path}")
    if todo:
        print(f"  [줄글 미집필 {len(todo)}장] {', '.join(todo)}")
    return 0


if __name__ == "__main__":
    from _env_guard import force_py312
    force_py312()
    sys.exit(main())
