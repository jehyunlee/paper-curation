"""AI4Science 발표용 슬라이드 원고 빌더 (오프닝 5 + 본문 + 종합 5).

코퍼스(`docs/{topic}/_category_summaries.json`, `_timeline_narrative.json`,
`_new_classification.json`, `_insights.json`, `docs/papers/_papers_index.json`)에서
카테고리·서브카테고리 규모, 시기, 상태, 대표 도구, 대표 논문을 뽑고
큐레이션된 한국어 내러티브와 합쳐 슬라이드 원고 두 벌을 출력한다.

  - `reports/build/{topic}_slides_<N>.html`  : 브라우저·인쇄용 (자기완결 HTML)
  - `reports/source/{topic}_slides_<N>.md`   : Obsidian 용 (frontmatter + `---` 구분)

슬라이드 구성 (N = 5 + 본문 + 5; ai4s 는 대분류 10개 × 서브카테고리 최대 5개 = 48 → 58장):
  S01–S05  오프닝(표지·방법·코퍼스·지형도·관통 서사)
  S06–     대분류별 서브카테고리(편수 상위 --per-category 개, 4개뿐인 대분류는 4장)
  마지막 5 종합(수렴·부상/쇠퇴·공백·검증 전환·실행 제언)

집필본(한국어 내러티브·줄글)은 lib/slide_prose_ai4s.py 에 있고 분류체계에 묶여 있다.
재집필: build_slide_dossier.py 로 근거를 뽑아 집필 → assemble_slide_prose.py 로 모듈 생성.

Usage:
  PYTHONUTF8=1 python pipeline/build_slide_deck.py --topic ai4s
  PYTHONUTF8=1 python pipeline/build_slide_deck.py --topic ai4s --per-category 5
"""
import argparse
import html as H
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

PIPE = Path(__file__).resolve().parent
sys.path.insert(0, str(PIPE))
PROJECT_ROOT = PIPE.parent

from config_loader import PAPERS_DIR, get_topic_dir  # noqa: E402
from lib.atomic_io import atomic_write_text  # noqa: E402

REPORTS = PROJECT_ROOT / "reports"

ACCENT = {"ai4s": "#D63423", "scisci": "#2374D6"}

STATUS_KO = {
    "ACCELERATING": "가속",
    "STABLE": "안정",
    "EMERGING": "부상",
    "DECLINING": "감소",
}

# 이 덱과 v2 줄글은 lib/slide_prose_ai4s.py 의 CATEGORY_KO 대분류와 그 서브카테고리
# (NARRATIVE/PROSE 키)를 기준으로 손으로 집필한 날짜별 산출물이다.
# topic_modeling 이 분류체계를 다시 짜면(카테고리 이름이 바뀜) 집필본은 더 이상 그
# 코퍼스를 설명하지 않으므로 load_corpus() 가 TaxonomyMismatch 로 빌드를 거부한다.
# 같은 분류체계 안에서 편수만 늘어난 경우는 빌드된다 — 집필본의 편수는 전부
# `{count}` 류 플레이스홀더라 빌드 시점 값으로 치환되고(fill_prose), 치환 불가 키는
# 빌드가 KeyError 로 실패한다. 재집필 절차: build_slide_dossier.py → 집필 →
# assemble_slide_prose.py.
from lib.slide_prose_ai4s import (  # noqa: E402
    CATEGORY_KO, CATEGORY_LEAD, NARRATIVE, PROSE, PROSE_AUTHORED,
)

OPENING_KEYS = ("cover", "method", "corpus", "landscape", "arc")
CLOSING_KEYS = ("convergence", "riseandfall", "gaps", "verification", "action")
FRAME_KEYS = OPENING_KEYS + CLOSING_KEYS


class TaxonomyMismatch(RuntimeError):
    """Live `_category_summaries.json` names categories the deck was not written for."""


def authored_taxonomy_gap(summaries):
    """Live categories that have no hand-written Korean name/lead (= not authored)."""
    return sorted({c.get("category") for c in summaries} - set(CATEGORY_KO))


_PLACEHOLDER = re.compile(r"\{(?P<key>[a-z_]+)(?::(?P<arg>[^{}]+))?\}")


class ProseContext:
    """집필본의 `{count}` 류 플레이스홀더를 빌드 시점 코퍼스 값으로 치환한다.

    전역: {total} {cards} {n_cats} {n_subs} {n_body} {per_category} {since}
          {recent_share} {y:YYYY} {n:NAME} {sub:SUBNAME} {cards:NAME} {ko:NAME} {s:SUBNAME}
    대분류 범위: {cat_count} {cat_cards} {cat_share} {nsubs} {cat_ko}
    서브카테고리 범위: {count} {recent} {sub_share}
    """

    def __init__(self, cats, years, total, per_category, since, n_body, slide_no,
                 n_recent_by_sub):
        self.cats = cats
        self.years = years
        self.total = total
        self.cards = sum(c.get("card_count", 0) for c in cats)
        self.per_category = per_category
        self.since = since
        self.n_body = n_body
        self.slide_no = slide_no
        self.n_recent_by_sub = n_recent_by_sub
        self.n_subs = sum(len(c.get("sub_themes", [])) for c in cats)
        self.recent_share = round(sum(v for y, v in years.items() if y >= since)
                                  / max(1, total) * 100)
        # 서브카테고리가 대분류와 같은 이름일 수 있다(ai4s: "Formal Mathematical Theorem
        # Proving" 은 대분류이자 그 안의 서브카테고리). {n:}/{ko:} 는 대분류를 우선하고,
        # 서브카테고리 편수를 꼭 집어야 하면 {sub:NAME} 을 쓴다.
        self.count_by_name, self.cards_by_name, self.ko_by_name = {}, {}, {}
        self.sub_count_by_name, self.cat_of_sub = {}, {}
        for c in cats:
            for st in c.get("sub_themes", []):
                self.sub_count_by_name[st["name"]] = st.get("count", 0)
                self.count_by_name[st["name"]] = st.get("count", 0)
                self.ko_by_name[st["name"]] = (NARRATIVE.get(st["name"]) or {}).get("ko", st["name"])
                self.cat_of_sub[st["name"]] = c
        for c in cats:
            cat = c["category"]
            self.count_by_name[cat] = c.get("count", 0)
            self.cards_by_name[cat] = c.get("card_count", 0)
            self.ko_by_name[cat] = CATEGORY_KO.get(cat, cat)

    def _lookup(self, table, arg, what):
        if arg not in table:
            raise KeyError(f"집필본 플레이스홀더 {{{what}:{arg}}} — 라이브 분류체계에 없는 이름")
        return table[arg]

    def fill(self, text, cat=None, sub=None):
        if not text:
            return text

        def repl(m):
            key, arg = m.group("key"), m.group("arg")
            if key == "total":
                return f"{self.total:,}"
            if key == "cards":
                return (f"{self._lookup(self.cards_by_name, arg, 'cards'):,}" if arg
                        else f"{self.cards:,}")
            if key == "n_cats":
                return str(len(self.cats))
            if key == "n_subs":
                return str(self.n_subs)
            if key == "n_body":
                return str(self.n_body)
            if key == "per_category":
                return str(self.per_category)
            if key == "since":
                return str(self.since)
            if key == "recent_share":
                return str(self.recent_share)
            if key == "y":
                return f"{self.years.get(int(arg), 0):,}"
            if key == "n":
                return f"{self._lookup(self.count_by_name, arg, 'n'):,}"
            if key == "sub":
                return f"{self._lookup(self.sub_count_by_name, arg, 'sub'):,}"
            if key == "ko":
                return self._lookup(self.ko_by_name, arg, "ko")
            if key == "s":
                return f"S{self._lookup(self.slide_no, arg, 's'):02d}"
            c = cat if cat is not None else (self.cat_of_sub.get(sub["name"]) if sub else None)
            if key in ("cat_count", "cat_cards", "cat_share", "nsubs", "cat_ko"):
                if c is None:
                    raise KeyError(f"집필본 플레이스홀더 {{{key}}} 는 대분류 문맥에서만 쓸 수 있다")
                if key == "cat_count":
                    return f"{c.get('count', 0):,}"
                if key == "cat_cards":
                    return f"{c.get('card_count', 0):,}"
                if key == "cat_share":
                    return str(round(c.get("count", 0) / max(1, self.total) * 100))
                if key == "nsubs":
                    return str(len(c.get("sub_themes", [])))
                return CATEGORY_KO.get(c["category"], c["category"])
            if key in ("count", "recent", "sub_share"):
                if sub is None:
                    raise KeyError(f"집필본 플레이스홀더 {{{key}}} 는 서브카테고리 문맥에서만 쓸 수 있다")
                if key == "count":
                    return f"{sub.get('count', 0):,}"
                if key == "recent":
                    return f"{self.n_recent_by_sub.get(sub['name'], 0):,}"
                return str(round(sub.get("count", 0) / max(1, c.get("count", 1) if c else 1) * 100))
            raise KeyError(f"집필본에 알 수 없는 플레이스홀더 {{{key}}}")

        return _PLACEHOLDER.sub(repl, text)

    def fill_all(self, value, cat=None, sub=None):
        """str / list / dict 를 재귀적으로 치환한다 (NARRATIVE·PROSE 항목용)."""
        if isinstance(value, str):
            return self.fill(value, cat, sub)
        if isinstance(value, list):
            return [self.fill_all(v, cat, sub) for v in value]
        if isinstance(value, dict):
            return {k: self.fill_all(v, cat, sub) for k, v in value.items()}
        return value


# ── 데이터 로딩 ────────────────────────────────────────────────────────────
def load_corpus(topic):
    tdir = get_topic_dir(topic)

    def read(name, root=None):
        p = (root or tdir) / name
        if not p.exists():
            raise SystemExit(f"[ERROR] 필요한 파일이 없습니다: {p}")
        return json.loads(p.read_text(encoding="utf-8"))

    summaries = read("_category_summaries.json")
    classification = read("_new_classification.json")
    timeline = read("_timeline_narrative.json")
    ins_path = tdir / "_insights.json"
    insights = json.loads(ins_path.read_text(encoding="utf-8")) if ins_path.exists() else {}
    index = read("_papers_index.json", root=Path(PAPERS_DIR))
    gap = authored_taxonomy_gap(summaries)
    if gap:
        raise TaxonomyMismatch(
            f"{topic}: 덱 집필본({PROSE_AUTHORED}, 대분류 {len(CATEGORY_KO)}개)에 없는 카테고리 "
            f"{len(gap)}개가 라이브 분류체계에 있다: {', '.join(gap)}. "
            "topic_modeling 이 분류체계를 다시 짠 상태라 CATEGORY_KO/CATEGORY_LEAD/NARRATIVE 와 "
            "lib/slide_prose_ai4s.py 를 새 분류체계로 재집필해야 빌드할 수 있다.")
    recount_categories(summaries, classification)
    return summaries, classification, timeline, insights, index


def recount_categories(summaries, classification):
    """`_category_summaries.json` 의 편수를 `_new_classification.json` 으로 다시 센다.

    요약본은 build_category_summaries.py 가 돌던 시점의 스냅샷이라 이후 신규 논문이
    반영되지 않는다(ai4s: 2,644 → 2,658 로 14편 누락). 여기서 두 기준을 함께 채운다.

    * `count`      — primary_category 기준 '고유 배정' 편수. 대분류 전체를 더하면
                     코퍼스 크기와 정확히 같다. 서브카테고리 커버리지 산술의 분모.
    * `card_count` — all_categories 기준 '중복 배정 포함' 편수. 토픽 인덱스
                     (`build_topic_index.py`) 의 카테고리 헤더 편수와 같은 값 —
                     사이트는 논문을 배정된 모든 카테고리에 카드로 노출한다.
    """
    primary, cards, subs = Counter(), Counter(), Counter()
    for a in classification.get("assignments", []):
        pcat = a.get("primary_category")
        primary[pcat] += 1
        subs[(pcat, a.get("sub_category"))] += 1
        for cat in (a.get("all_categories") or [pcat]):
            cards[cat] += 1
    for c in summaries:
        cat = c.get("category")
        if cat in primary:
            c["count"] = primary[cat]
        c["card_count"] = cards.get(cat, c.get("count", 0))
        for st in c.get("sub_themes", []):
            key = (cat, st.get("name"))
            if key in subs:
                st["count"] = subs[key]


_STOP = {"and", "the", "of", "for", "in", "a", "amp", "with", "on", "to", "via", "using"}
_TITLE_STOP = {"large", "language", "model", "models", "learning", "deep", "neural", "based",
               "towards", "scientific", "science", "data", "analysis", "generative", "using",
               "prediction", "framework", "network", "networks", "benchmark", "evaluation"}


def _tokens(text):
    return {t for t in re.findall(r"[a-z0-9]+", (text or "").lower())
            if t not in _STOP and len(t) > 2}


def match_timeline(analyses, category, name):
    """서브카테고리 이름은 요약본과 타임라인 내러티브에서 다르게 붙을 수 있다.
    토큰 겹침 비율이 가장 높은 항목을 고르고 0.4 미만이면 매칭 실패로 본다."""
    best, best_score = None, 0.0
    want = _tokens(name)
    for st in (analyses.get(category) or {}).get("sub_themes", []):
        score = len(want & _tokens(st.get("name"))) / max(1, len(want))
        if score > best_score:
            best, best_score = st, score
    return best if best_score >= 0.4 else None


def top_sub_name(c):
    """대분류에서 편수가 가장 큰 서브카테고리 이름(없으면 '')."""
    subs = c.get("sub_themes") or []
    return sorted(subs, key=lambda s: -s.get("count", 0))[0]["name"] if subs else ""


def year_of(date_str):
    m = re.match(r"(\d{4})", str(date_str or ""))
    return int(m.group(1)) if m else 0


def ref_keys(paper, tools):
    """본문 불릿에 [n] 마커를 달 때 쓰는 '식별 가능한 고유명' 집합.

    오귀속을 막기 위해 (1) 제목에 처음 등장하는 시스템명(headword) 하나와
    (2) 제목에 실제로 등장하는 대표 도구명(5자 이상)만 인정한다.
    'AlphaFold2' 같은 범용 모델명이 다른 논문 제목에 섞여 있다는 이유로
    엉뚱한 불릿에 마커가 붙는 것을 막는다."""
    title = paper.get("title") or ""
    keys = set()
    for tok in re.findall(r"[A-Za-z][A-Za-z0-9]*(?:[-–][A-Za-z0-9]+)*", title):
        if (len(tok) >= 4 and tok.lower() not in _TITLE_STOP
                and (sum(1 for ch in tok if ch.isupper()) >= 2 or any(ch.isdigit() for ch in tok))):
            keys.add(tok)
            break
    for t in tools:
        if len(t) >= 5 and re.search(r"(?<![A-Za-z0-9])" + re.escape(t) + r"(?![A-Za-z0-9])",
                                     title, re.I):
            keys.add(t)
    return keys


def clean_title(title):
    """제목에 남은 LaTeX·마크다운 잔여물을 표시용으로 정리한다."""
    t = re.sub(r"\\pi\b", "π", title or "")
    t = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"\1/\2", t)
    for _ in range(3):  # \boldsymbol{\frac{1}{\pi}} 처럼 중첩된 경우: 안쪽부터 벗긴다
        t = re.sub(r"\$?\\(?:texttt|textbf|textit|emph|mathrm|mathbf|boldsymbol|text)\{([^{}]*)\}\$?", r"\1", t)
    t = t.replace("$", "").replace("\\", "")
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t)
    return re.sub(r"\s+", " ", t).strip()


def title_fingerprint(title):
    """같은 논문이 두 슬러그로 들어온 경우를 걸러내기 위한 정규화 키."""
    return re.sub(r"[^a-z0-9]", "", clean_title(title).lower())[:60]


def title_phrase_hit(paper, text):
    """불릿이 논문 제목을 그대로 부르는지 검사한다.

    두 가지 호명을 받는다: (1) 제목 앞 4단어(18자 이상), (2) 콜론 앞의 이름 부분
    ("Into the Unknown: Benchmarking …" 의 "Into the Unknown", "Safe-SDL: …" 의 "Safe-SDL") —
    집필자는 보통 부제 없이 이름만 부른다. 이름 부분은 두 단어 이상이거나
    하이픈·숫자가 들어간 시스템명일 때만, 단어 경계로 맞춘다.
    """
    title = clean_title(paper.get("title"))
    words = title.split()
    candidates = []
    if len(words) >= 3:
        phrase = " ".join(words[:4]).rstrip(":,.")
        if len(phrase) >= 18:
            candidates.append(phrase)
    head = title.split(":", 1)[0].strip() if ":" in title else ""
    if head and len(head) >= 8 and (len(head.split()) >= 2 or re.search(r"[-\d]", head)):
        candidates.append(head)
    return any(re.search(r"(?<![A-Za-z0-9])" + re.escape(c) + r"(?![A-Za-z0-9])", text, re.I)
               for c in candidates)


def make_ref(paper, link_base):
    slug = paper.get("slug") or ""
    essence = clean_title(re.sub(r"\s+", " ", paper.get("essence") or "")).strip()
    if len(essence) > 135:
        essence = essence[:134].rstrip() + "…"
    authors = paper.get("authors") or []
    author = (authors[0] + " 외") if len(authors) > 1 else (authors[0] if authors else "")
    return {
        "slug": slug,
        "title": clean_title(paper.get("title")),
        "author": author,
        "date": str(paper.get("date") or ""),
        "year": str(paper.get("date") or "")[:4],
        "citations": paper.get("citation_count") or 0,
        "essence": essence,
        "url": f"{link_base}/{slug}/index.html" if slug else "",
        "doi": paper.get("doi") or "",
    }


def pick_papers(papers, tools, keywords, link_base, limit=4, since=2025):
    """대표 논문 선정. (1) 2025년 이후 우선 (2) 대표 도구·키워드가 제목에 있는 것
    (3) 피인용수 (4) 리뷰 점수 (5) 최신순."""
    probes = [t.lower() for t in tools if len(t) >= 4]
    probes += [w.lower() for w in keywords if len(w) >= 5]

    def key(p):
        title = (p.get("title") or "").lower()
        hit = sum(1 for probe in probes if probe in title)
        y = year_of(p.get("date"))
        return (0 if y >= since else 1, -min(hit, 3), -(p.get("citation_count") or 0),
                -(p.get("score") or 0), -y)

    out, seen = [], set()
    for p in sorted(papers, key=key):
        fp = title_fingerprint(p.get("title"))
        if fp in seen:
            continue
        seen.add(fp)
        out.append(make_ref(p, link_base))
        if len(out) >= limit:
            break
    return out


def _key_pattern(key):
    """단복수 차이(PINNs↔PINN)까지만 흡수하는 단어 경계 패턴."""
    base = key[:-1] if (len(key) > 4 and key.endswith("s")) else key
    return r"(?<![A-Za-z0-9])" + re.escape(base) + r"s?(?![A-Za-z0-9])"


def attach_markers(points, refs, tools):
    """불릿에 등장하는 고유명(또는 제목 그대로의 호명)이 대표 논문과 일치할 때만 [n] 을 붙인다."""
    keysets = [ref_keys({"title": r["title"]}, tools) for r in refs]
    out = []
    for text in points:
        hits = []
        for i, (keys, ref) in enumerate(zip(keysets, refs), start=1):
            if any(re.search(_key_pattern(k), text, re.I) for k in keys) \
                    or title_phrase_hit({"title": ref["title"]}, text):
                hits.append(i)
        out.append(text + "".join(f"[{i}]" for i in hits))
    return out


# ── 슬라이드 조립 ──────────────────────────────────────────────────────────
def prepare_corpus(summaries, classification, timeline, index, per_category=5, since=2025):
    """덱·줄글 두 빌더가 공유하는 코퍼스 통계와 슬라이드 순서.

    본문 슬라이드 순서(대분류 편수 내림차순 → 서브카테고리 편수 내림차순)를 여기서
    한 번만 정해 `slide_no` 로 고정한다. 집필본의 `{s:NAME}` 교차 참조와 두 판본의
    S번호가 같은 근거를 쓰게 하기 위해서다.
    """
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
        y = year_of(p.get("date"))
        if 2015 <= y <= 2030:
            years[y] += 1

    cats = sorted(summaries, key=lambda c: -c.get("count", 0))
    order = []  # (cat dict, sub dict) in slide order
    for c in cats:
        subs = sorted(c.get("sub_themes", []), key=lambda s: -s.get("count", 0))[:per_category]
        order += [(c, st) for st in subs]
    slide_no = {st["name"]: len(OPENING_KEYS) + i + 1 for i, (_, st) in enumerate(order)}
    n_recent_by_sub = {
        st["name"]: sum(1 for p in by_sub.get((c["category"], st["name"]), [])
                        if year_of(p.get("date")) >= since)
        for c, st in order
    }
    ctx = ProseContext(cats, years, len(papers), per_category, since, len(order),
                       slide_no, n_recent_by_sub)
    return {
        "papers": papers, "by_prefix": by_prefix, "by_sub": by_sub, "years": years,
        "cats": cats, "order": order, "total": len(papers), "ctx": ctx,
        "analyses": timeline.get("category_analyses", {}),
        "recent_share": ctx.recent_share, "cards_total": ctx.cards,
        "n_subs": ctx.n_subs, "n_body": len(order),
    }


def frame_entry(key, ctx):
    """오프닝·종합 슬라이드의 집필 항목(NARRATIVE[key])을 치환해서 돌려준다."""
    nar = NARRATIVE.get(key)
    if not nar:
        raise KeyError(f"집필본에 오프닝/종합 항목이 없다: {key}")
    return ctx.fill_all(nar)


def refs_by_names(names, papers, link_base, since, limit=6):
    """본문이 지목한 시스템명을 코퍼스 제목에서 직접 찾아 레퍼런스로 만든다."""
    picked, seen = [], set()
    for nm in names:
        pat = re.compile(r"(?<![A-Za-z0-9])" + re.escape(nm) + r"(?![A-Za-z0-9])", re.I)
        hits = [p for p in papers if pat.search(p.get("title") or "")]
        hits.sort(key=lambda p: (0 if year_of(p.get("date")) >= since else 1,
                                 -(p.get("citation_count") or 0), -year_of(p.get("date"))))
        for p in hits[:1]:
            if p["slug"] not in seen:
                seen.add(p["slug"])
                picked.append(make_ref(p, link_base))
        if len(picked) >= limit:
            break
    return picked


def insight_refs(items, by_prefix, link_base, since, limit=5):
    pool = []
    for it in items:
        for ev in it.get("evidence", []):
            p = by_prefix.get(str(ev))
            if p:
                pool.append(p)
    seen, uniq = set(), []
    for p in sorted(pool, key=lambda p: (0 if year_of(p.get("date")) >= since else 1,
                                         -year_of(p.get("date")),
                                         -(p.get("citation_count") or 0))):
        if p["slug"] in seen:
            continue
        seen.add(p["slug"])
        uniq.append(make_ref(p, link_base))
        if len(uniq) >= limit:
            break
    return uniq


def insight_points(items):
    return [f"**{it.get('title')}** ({' × '.join(CATEGORY_KO.get(x, x) for x in it.get('categories', []))}) "
            f"— {it.get('description')}" for it in items]


def build_slides(topic, summaries, classification, timeline, insights, index,
                 per_category=5, link_base="../../docs/papers", since=2025):
    corpus = prepare_corpus(summaries, classification, timeline, index, per_category, since)
    papers, by_prefix, by_sub = corpus["papers"], corpus["by_prefix"], corpus["by_sub"]
    years, cats, analyses, ctx = corpus["years"], corpus["cats"], corpus["analyses"], corpus["ctx"]
    total, recent_share, cards_total = corpus["total"], corpus["recent_share"], corpus["cards_total"]
    n_subs, n_body = corpus["n_subs"], corpus["n_body"]

    slides = []

    def add(**kw):
        kw["no"] = len(slides) + 1
        kw.setdefault("refs", [])
        slides.append(kw)
        return kw

    trend = " → ".join(f"{y}년 {years[y]:,}편" for y in sorted(y for y in years if y >= 2023))

    # ── 오프닝 ─────────────────────────────────────────────────────────────
    fr = frame_entry("cover", ctx)
    add(kind="표지", part="오프닝",
        title_ko="AI for Science, 2026년 지형도",
        title_en=f"{total:,}편 코퍼스가 말하는 {len(cats)}개 지형과 {n_body}개 최전선",
        headline=fr["headline"],
        points=[
            f"대상 코퍼스: **{topic}** 토픽 {total:,}편(리뷰 완료 전수). 사례는 **{since}년 이후를 우선**해 골랐다.",
            f"구조: 대분류 {len(cats)}개 · 서브카테고리 {n_subs}개 → 편수 상위 최대 {per_category}개씩 총 {n_body}장.",
            f"연도 분포: {trend}. 전체의 **{recent_share}%가 {since}년 이후** 논문이다.",
            "슬라이드 1장 = 서브카테고리 1개. 규모·기간·상태·대표 도구·대표 논문·시사점을 한 화면에.",
            "각 슬라이드 하단 레퍼런스는 코퍼스의 **논문별 리뷰 문서로 바로 연결**된다.",
        ] + list(fr.get("points") or []),
        sowhat=fr["sowhat"])

    fr = frame_entry("method", ctx)
    add(kind="방법", part="오프닝",
        title_ko="이 지도는 어떻게 만들어졌나",
        title_en="Method — SPECTER2 · UMAP · HDBSCAN · c-TF-IDF",
        headline=fr["headline"],
        points=[
            "임베딩: SPECTER2(논문 특화)로 전 논문을 벡터화 → UMAP 5차원 축소 → HDBSCAN 밀도 클러스터링.",
            f"미세 클러스터를 c-TF-IDF로 키워드화하고 LLM이 명명 → 서브카테고리 {n_subs}개 → 대분류 {len(cats)}개로 그룹핑.",
            "각 논문은 primary_category 1개 + all_categories 최대 3개를 가진다(다중 배정).",
            f"편수는 두 기준으로 센다 — **고유 배정**(primary 1편=1칸, {len(cats)}개 합 {total:,}편)과 "
            f"**중복 포함**(all_categories, {len(cats)}개 합 {cards_total:,}편). "
            "웹 인덱스의 카테고리 헤더 편수는 중복 포함 기준이고, 이 덱의 커버리지 산술은 고유 배정 기준이다.",
            "시기(start–end)·상태(가속/안정/부상/감소)·대표 도구는 카테고리별 타임라인 분석에서 가져왔다.",
        ] + list(fr.get("points") or []),
        sowhat=fr["sowhat"])

    fr = frame_entry("corpus", ctx)
    ymax = max(years.values()) if years else 1
    add(kind="코퍼스", part="오프닝",
        title_ko="코퍼스 한눈에 보기",
        title_en="Corpus at a glance",
        headline=fr["headline"],
        table={"head": ["연도", "편수", ""],
               "rows": [[str(y), f"{years[y]:,}편", "█" * max(1, round(years[y] / ymax * 30))]
                        for y in sorted(years) if y >= 2018]},
        points=[
            f"2023년 이후 급증 — {trend}.",
            f"{since}년 이후 논문이 전체의 {recent_share}%. 이 덱이 {since}+ 사례 중심인 이유다.",
        ] + list(fr.get("points") or []),
        sowhat=fr["sowhat"])

    fr = frame_entry("landscape", ctx)
    add(kind="지형도", part="오프닝",
        title_ko=f"{len(cats)}개 대분류 지형도",
        title_en=f"The {len(cats)} territories",
        headline=fr["headline"],
        table={"head": ["대분류", "고유 배정", "중복 포함", "서브카테고리", "최대 서브카테고리"],
               "rows": [[CATEGORY_KO.get(c["category"], c["category"]), f"{c.get('count', 0):,}",
                         f"{c.get('card_count', 0):,}",
                         str(len(c.get("sub_themes", []))),
                         ctx.ko_by_name.get(top_sub_name(c), top_sub_name(c) or "-")]
                        for c in cats]},
        points=list(fr.get("points") or []) + [
            f"이후 {len(cats)}개 파트는 이 순서(고유 배정 편수 내림차순)로 진행한다.",
        ],
        sowhat=fr["sowhat"])

    fr = frame_entry("arc", ctx)
    add(kind="서사", part="오프닝",
        title_ko=fr.get("title_ko") or "관통하는 한 줄",
        title_en=fr.get("title_en") or "The through-line",
        headline=fr["headline"],
        points=list(fr.get("points") or []),
        sowhat=fr["sowhat"])

    # ── 본문: 카테고리별 서브카테고리 ──────────────────────────────────────
    ci = 0
    for c, st in corpus["order"]:
        cat = c["category"]
        cat_ko = CATEGORY_KO.get(cat, cat)
        subs = sorted(c.get("sub_themes", []), key=lambda s: -s.get("count", 0))[:per_category]
        si = subs.index(st) + 1
        if si == 1:
            ci += 1
        part = f"제{ci}부 · {cat_ko}"
        covered = sum(s.get("count", 0) for s in subs)
        share = round(covered / max(1, c.get("count", 1)) * 100)
        name = st.get("name")
        tl = match_timeline(analyses, cat, name)
        nar = ctx.fill_all(NARRATIVE.get(name, {}), cat=c, sub=st)
        tools = (tl or {}).get("representative_tools", []) or []
        kds = [re.sub(r"\s+", " ", k) for k in ((tl or {}).get("key_developments") or [])]
        points = nar.get("points") or kds
        if not points:
            ko = re.sub(r"\s+", " ", st.get("description_ko") or "")
            points = [ko[:300] + ("…" if len(ko) > 300 else "")]
        # 본문에서 실제로 언급한 시스템명을 최우선 탐침으로 써서,
        # 슬라이드가 말하는 논문이 레퍼런스에 실리도록 한다.
        named = [w for w in re.findall(r"[A-Za-z][A-Za-z0-9]*(?:[-–][A-Za-z0-9]+)*",
                                       " ".join(points))
                 if len(w) >= 4 and (sum(1 for ch in w if ch.isupper()) >= 2
                                     or any(ch.isdigit() for ch in w))]
        probes = named + list(_tokens(name)) + [w for k in kds
                                                for w in re.findall(r"[A-Z][A-Za-z0-9\-]{3,}", k)]
        pool = by_sub.get((cat, name), [])
        refs = pick_papers(pool, tools, probes, link_base, since=since)
        # 불릿이 논문 제목을 그대로 부르는 경우(예: 'Discovery of Unstable Singularities')
        # 해당 논문을 레퍼런스 맨 앞에 강제로 싣는다.
        body = " ".join(points)
        forced = [p for p in pool if title_phrase_hit(p, body)]
        if forced:
            seen = set()
            merged = []
            for r in [make_ref(p, link_base) for p in forced] + refs:
                fp = title_fingerprint(r["title"])
                if fp in seen:
                    continue
                seen.add(fp)
                merged.append(r)
            refs = merged[:max(4, len(forced) + 3)]
        n_recent = ctx.n_recent_by_sub.get(name, 0)
        badges = [f"{st.get('count', 0)}편"]
        if tl:
            badges += [f"{tl.get('start')}–{tl.get('end')}", STATUS_KO.get(tl.get("status"), "")]
        badges.append(f"{since}+ {n_recent}편")
        add(kind="서브카테고리", part=part, category=cat, category_ko=cat_ko,
            position=f"{si}/{len(subs)}",
            title_ko=nar.get("ko") or name,
            title_en=name,
            alias_en=((tl or {}).get("name") if (tl and tl.get("name") != name) else ""),
            badges=[b for b in badges if b],
            context=(ctx.fill(CATEGORY_LEAD.get(cat, ""), cat=c) if si == 1 else ""),
            cat_meta=(f"{cat_ko} 고유 배정 {c.get('count', 0):,}편"
                      f"(중복 포함 {c.get('card_count', 0):,}편 · 웹 인덱스 기준) · 서브카테고리 "
                      f"{len(c.get('sub_themes', []))}개 · 본 파트 {len(subs)}개로 {share}% 커버"
                      if si == 1 else ""),
            headline=nar.get("headline") or "",
            points=attach_markers(points, refs, tools),
            tools=tools, refs=refs,
            sowhat=nar.get("sowhat") or "")

    # ── 종합 ───────────────────────────────────────────────────────────────
    cross = insights.get("cross_category", []) or []
    by_type = defaultdict(list)
    for item in cross:
        by_type[item.get("type")].append(item)
    meta = insights.get("meta", {}) or {}

    conv = by_type.get("convergence", [])
    fr = frame_entry("convergence", ctx)
    add(kind="종합", part="종합",
        title_ko="수렴 신호: 경계가 무너지는 곳",
        title_en="Convergence signals",
        headline=fr["headline"],
        points=insight_points(conv) + list(fr.get("points") or []),
        extra={"정책 함의": [it.get("policy_implication") for it in conv if it.get("policy_implication")]},
        refs=insight_refs(conv, by_prefix, link_base, since),
        sowhat=fr["sowhat"])

    rise, fall = by_type.get("emerging", []), by_type.get("declining", [])
    fr = frame_entry("riseandfall", ctx)
    add(kind="종합", part="종합",
        title_ko="부상과 쇠퇴",
        title_en="What is rising, what is fading",
        headline=fr["headline"],
        points=(["**부상 —**"] + insight_points(rise) + ["**쇠퇴 —**"] + insight_points(fall)
                + list(fr.get("points") or [])),
        extra={"정책 함의": [it.get("policy_implication") for it in rise + fall if it.get("policy_implication")]},
        refs=insight_refs(rise + fall, by_prefix, link_base, since),
        sowhat=fr["sowhat"])

    gaps = by_type.get("gap", [])
    fr = frame_entry("gaps", ctx)
    add(kind="종합", part="종합",
        title_ko="비어 있는 자리",
        title_en="Gaps and underserved domains",
        headline=fr["headline"],
        points=(insight_points(gaps) + ["**미개척 영역** — " + x for x in (meta.get("underserved_domains") or [])]
                + list(fr.get("points") or [])),
        refs=insight_refs(gaps, by_prefix, link_base, since),
        sowhat=fr["sowhat"])

    fr = frame_entry("verification", ctx)
    add(kind="종합", part="종합",
        title_ko=fr.get("title_ko") or "검증 전환의 축",
        title_en=fr.get("title_en") or "Axes of the verification turn",
        headline=fr["headline"],
        points=list(fr.get("points") or []),
        refs=refs_by_names(fr.get("refs") or [], papers, link_base, since, limit=8),
        sowhat=fr["sowhat"])

    fr = frame_entry("action", ctx)
    add(kind="마무리", part="종합",
        title_ko="그래서 무엇을 할 것인가",
        title_en="Where to stand",
        headline=fr["headline"],
        points=list(fr.get("points") or []),
        extra=fr.get("extra") or {},
        sowhat=fr["sowhat"])

    return slides, {"total": total, "categories": cats, "years": years, "n_subs": n_subs,
                    "n_body": n_body, "per_category": per_category, "since": since,
                    "recent_share": recent_share, "link_base": link_base}


# ── 렌더링: Markdown (Obsidian) ────────────────────────────────────────────
def render_markdown(topic, slides, stats):
    today = datetime.now().strftime("%Y-%m-%d")
    L = ["---",
         f'title: "AI for Science 지형도 — 발표 슬라이드 원고 {len(slides)}장"',
         f"topic: {topic}",
         f"slides: {len(slides)}",
         f"corpus_papers: {stats['total']}",
         f"evidence_since: {stats['since']}",
         f"generated: {today}",
         "tags:"]
    L += [f"  - {t}" for t in ("ai4science", "슬라이드", "연구동향", topic)]
    L += ["---", "",
          f"# AI for Science 지형도 — 슬라이드 원고 {len(slides)}장", "",
          f"> [!info] 개요\n"
          f"> 코퍼스 **{stats['total']:,}편** · 대분류 **{len(stats['categories'])}개** · "
          f"서브카테고리 **{stats['n_subs']}개** 중 편수 상위 **{stats['per_category']}개씩**.\n"
          f"> 슬라이드 1장 = 서브카테고리 1개(`S{len(OPENING_KEYS) + 1:02d}`–"
          f"`S{len(OPENING_KEYS) + stats['n_body']:02d}`). 사례는 **{stats['since']}년 이후 우선**"
          f"(코퍼스의 {stats['recent_share']}%).\n"
          f"> 레퍼런스 링크는 각 논문의 리뷰 문서(`{stats['link_base']}/<slug>/index.html`)로 연결된다.",
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
        if s.get("cat_meta"):
            L += ["", f"<sub>{s['cat_meta']}</sub>"]
        L.append("")
        if s.get("context"):
            L += [f"> [!quote] 파트 도입\n> {s['context']}", ""]
        if s.get("headline"):
            L += [f"> [!abstract] 핵심 메시지\n> {s['headline']}", ""]
        if s.get("table"):
            head = s["table"]["head"]
            L.append("| " + " | ".join(head) + " |")
            L.append("|" + "|".join(["---"] * len(head)) + "|")
            L += ["| " + " | ".join(str(x) for x in row) + " |" for row in s["table"]["rows"]]
            L.append("")
        if s.get("points"):
            L += [f"- {p}" for p in s["points"]] + [""]
        if s.get("tools"):
            L += [f"**대표 도구·시스템** — {' · '.join(s['tools'])}", ""]
        for label, items in (s.get("extra") or {}).items():
            items = [i for i in items if i]
            if items:
                L += [f"**{label}**", ""] + [f"- {i}" for i in items] + [""]
        if s.get("refs"):
            L += ["**레퍼런스** (제목 클릭 → 논문 리뷰)", ""]
            for i, r in enumerate(s["refs"], start=1):
                cit = f" · 인용 {r['citations']:,}" if r["citations"] else ""
                who = f"{r['author']}, " if r["author"] else ""
                L.append(f"{i}. [{r['title']}]({r['url']}) — {who}{r['date']}{cit}")
                if r["essence"]:
                    L.append(f"    - {r['essence']}")
            L.append("")
        if s.get("sowhat"):
            L += [f"> [!tip] 우리에게 무엇인가\n> {s['sowhat']}", ""]

    # 부록: 전체 레퍼런스
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
          f"*생성: `pipeline/build_slide_deck.py --topic {topic}` · {today} · "
          f"근거 코퍼스 {stats['total']:,}편 (`docs/{topic}`)*", ""]
    return "\n".join(L)


# ── 렌더링: HTML ──────────────────────────────────────────────────────────
CSS = """
:root{--accent:__ACCENT__;--ink:#161616;--muted:#6b6b6b;--soft:#9a9a9a;
--rule:#e5e5e3;--bg:#f4f4f2;--card:#fff}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{background:var(--bg);color:var(--ink);line-height:1.62;-webkit-font-smoothing:antialiased;
font-family:-apple-system,BlinkMacSystemFont,"Pretendard","Apple SD Gothic Neo","Noto Sans KR",sans-serif}
a{color:inherit}
.wrap{max-width:1120px;margin:0 auto;padding:46px 26px 90px}
header.deck{border-bottom:3px solid var(--ink);padding-bottom:22px}
header.deck .eyebrow{font-size:11.5px;letter-spacing:.22em;color:var(--accent);font-weight:700;text-transform:uppercase}
header.deck h1{font-size:33px;line-height:1.24;margin:.35em 0 .3em;letter-spacing:-.022em}
header.deck p.lede{margin:0;color:var(--muted);font-size:14.5px}
.stats{display:flex;flex-wrap:wrap;gap:9px;margin:20px 0 0}
.stat{background:var(--card);border:1px solid var(--rule);border-radius:10px;padding:9px 14px;min-width:118px}
.stat b{display:block;font-size:20px;letter-spacing:-.01em}
.stat span{font-size:11px;color:var(--muted)}
nav.toc{background:var(--card);border:1px solid var(--rule);border-radius:12px;padding:18px 20px;margin:26px 0 30px}
nav.toc h2{font-size:12px;letter-spacing:.16em;color:var(--soft);margin:0 0 10px;text-transform:uppercase}
nav.toc ol{margin:0;padding:0;list-style:none;display:grid;
grid-template-columns:repeat(auto-fill,minmax(258px,1fr));gap:2px 18px}
nav.toc li{font-size:12.8px;color:var(--muted);padding:2px 0}
nav.toc li a{text-decoration:none}
nav.toc li a:hover{color:var(--accent)}
nav.toc li .n{display:inline-block;min-width:36px;color:var(--soft);font-size:11.5px;font-variant-numeric:tabular-nums}
nav.toc li.part{margin-top:9px;font-weight:700;color:var(--ink);font-size:12px;grid-column:1/-1;
border-top:1px solid var(--rule);padding-top:8px}
.slide{background:var(--card);border:1px solid var(--rule);border-radius:14px;
padding:28px 32px 24px;margin:0 0 18px;scroll-margin-top:14px}
.rail{display:flex;align-items:center;gap:9px;margin-bottom:13px}
.rail .no{background:var(--ink);color:#fff;font-size:11.5px;font-weight:700;letter-spacing:.06em;
padding:3px 9px;border-radius:5px;font-variant-numeric:tabular-nums}
.rail .kind{font-size:10.5px;letter-spacing:.15em;color:var(--accent);font-weight:700;text-transform:uppercase}
.rail .part{font-size:11.5px;color:var(--soft);margin-left:auto}
.slide h2{font-size:24px;line-height:1.3;margin:0 0 4px;letter-spacing:-.02em}
.slide .en{font-size:12.8px;color:var(--muted);margin:0;font-style:italic}
.slide .alias{font-size:11.5px;color:var(--soft);margin:3px 0 0}
.badges{display:flex;flex-wrap:wrap;gap:6px;margin:13px 0 0}
.badge{font-size:11.5px;border:1px solid var(--rule);border-radius:20px;padding:2px 11px;color:var(--muted);background:#fafafa}
.badge.n{border-color:var(--accent);color:var(--accent);font-weight:700}
.badge.recent{border-color:#c9c9c9;color:#4a4a4a;font-weight:600}
.badge.st-가속{background:#fdf1ef;border-color:#f0c6bf;color:#a8291a}
.badge.st-부상{background:#f1f6fd;border-color:#c3d8f0;color:#1f5b9e}
.badge.st-안정{background:#f5f5f4;border-color:#dcdcda;color:#5a5a58}
.badge.st-감소{background:#f7f7f7;border-color:#e2e2e2;color:#8a8a8a}
.catmeta{font-size:11.8px;color:var(--soft);margin:10px 0 0}
.context{margin:15px 0 0;padding:10px 15px;border-left:3px solid var(--rule);background:#fafafa;
color:var(--muted);font-size:13.4px;border-radius:0 6px 6px 0}
.headline{margin:17px 0 2px;padding:14px 18px;background:#fbf6f5;border-left:4px solid var(--accent);
border-radius:0 8px 8px 0;font-size:16px;font-weight:600;line-height:1.55}
ul.points{margin:17px 0 0;padding-left:0;list-style:none}
ul.points li{position:relative;padding-left:19px;margin-bottom:8px;font-size:14.3px}
ul.points li::before{content:"";position:absolute;left:3px;top:.62em;width:6px;height:6px;
border-radius:50%;background:var(--accent);opacity:.55}
sup.cite{font-size:10.5px;font-weight:700;color:var(--accent);vertical-align:super;margin-left:1px}
sup.cite a{text-decoration:none}
table.grid{width:100%;border-collapse:collapse;margin:17px 0 4px;font-size:13.3px}
table.grid th{text-align:left;font-size:11px;letter-spacing:.08em;color:var(--soft);text-transform:uppercase;
border-bottom:2px solid var(--ink);padding:7px 10px 7px 0}
table.grid td{border-bottom:1px solid var(--rule);padding:7px 10px 7px 0;vertical-align:top}
table.grid td:nth-child(2){font-variant-numeric:tabular-nums;white-space:nowrap}
table.grid td:last-child{color:var(--accent);letter-spacing:-1px}
.block-label{font-size:10.5px;letter-spacing:.16em;color:var(--soft);text-transform:uppercase;
margin:20px 0 7px;font-weight:700}
.tools{display:flex;flex-wrap:wrap;gap:5px}
.tool{font-size:11.8px;background:#f4f4f2;border:1px solid var(--rule);border-radius:5px;padding:2px 8px;color:#444}
ol.refs{margin:0;padding-left:20px}
ol.refs li{font-size:13.2px;margin-bottom:7px;line-height:1.5}
ol.refs a{font-weight:600;text-decoration:none;border-bottom:1px solid rgba(0,0,0,.18)}
ol.refs a:hover{color:var(--accent);border-bottom-color:var(--accent)}
ol.refs .m{color:var(--soft);font-size:11.8px;font-variant-numeric:tabular-nums}
ol.refs .e{display:block;color:var(--muted);font-size:12.4px;margin-top:2px}
.sowhat{margin:20px 0 0;padding:13px 18px;background:#f6f7f9;border:1px solid #e2e5ea;border-radius:9px;font-size:13.8px}
.sowhat b{color:var(--accent);font-size:10.5px;letter-spacing:.14em;display:block;margin-bottom:4px;text-transform:uppercase}
.appendix{background:var(--card);border:1px solid var(--rule);border-radius:14px;padding:26px 32px}
.appendix h2{font-size:20px;margin:0 0 4px}
.appendix p.sub{color:var(--muted);font-size:12.5px;margin:0 0 14px}
.appendix ol{padding-left:22px;margin:0}
.appendix li{font-size:13px;margin-bottom:5px}
footer.deck{margin-top:34px;padding-top:16px;border-top:1px solid var(--rule);
font-size:11.5px;color:var(--soft);text-align:center}
@media print{
 body{background:#fff}
 .wrap{max-width:none;padding:0}
 header.deck,nav.toc{page-break-after:always}
 .slide{page-break-inside:avoid;page-break-after:always;border:none;border-radius:0;padding:16px 0;margin:0}
 @page{size:A4 landscape;margin:13mm}
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
    css = CSS.replace("__ACCENT__", ACCENT.get(topic, "#D63423"))
    o = ["<!DOCTYPE html><html lang='ko'><head><meta charset='utf-8'>",
         "<meta name='viewport' content='width=device-width,initial-scale=1'>",
         f"<title>AI for Science 지형도 — 슬라이드 원고 {len(slides)}장 ({topic})</title>",
         f"<style>{css}</style></head><body><div class='wrap'>"]

    o.append("<header class='deck'>")
    o.append(f"<div class='eyebrow'>{H.escape(topic)} · slide script · {today}</div>")
    o.append(f"<h1>AI for Science 지형도 — 발표 슬라이드 {len(slides)}장</h1>")
    o.append(f"<p class='lede'>슬라이드 1장 = 서브카테고리 1개. 사례는 {stats['since']}년 이후 우선. "
             f"레퍼런스 제목을 클릭하면 해당 논문의 리뷰 문서로 이동한다.</p>")
    o.append("<div class='stats'>")
    for value, label in [(f"{stats['total']:,}", "코퍼스 논문"),
                         (str(len(stats["categories"])), "대분류"),
                         (str(stats["n_subs"]), "서브카테고리"),
                         (str(len(slides)), "슬라이드"),
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
                cls = "badge n" if i == 0 else ("badge recent" if b.startswith(str(stats["since"]))
                                                else f"badge st-{b}" if b in STATUS_KO.values() else "badge")
                o.append(f"<span class='{cls}'>{H.escape(b)}</span>")
            o.append("</div>")
        if s.get("cat_meta"):
            o.append(f"<p class='catmeta'>{H.escape(s['cat_meta'])}</p>")
        if s.get("context"):
            o.append(f"<div class='context'>{_inline(s['context'])}</div>")
        if s.get("headline"):
            o.append(f"<div class='headline'>{_inline(s['headline'])}</div>")
        if s.get("table"):
            o.append("<table class='grid'><thead><tr>")
            o += [f"<th>{H.escape(h)}</th>" for h in s["table"]["head"]]
            o.append("</tr></thead><tbody>")
            for row in s["table"]["rows"]:
                o.append("<tr>" + "".join(f"<td>{H.escape(str(x))}</td>" for x in row) + "</tr>")
            o.append("</tbody></table>")
        if s.get("points"):
            o.append("<ul class='points'>")
            o += [f"<li>{_inline(p)}</li>" for p in s["points"]]
            o.append("</ul>")
        if s.get("tools"):
            o.append("<div class='block-label'>대표 도구 · 시스템</div><div class='tools'>")
            o += [f"<span class='tool'>{H.escape(t)}</span>" for t in s["tools"]]
            o.append("</div>")
        for label, items in (s.get("extra") or {}).items():
            items = [i for i in items if i]
            if items:
                o.append(f"<div class='block-label'>{H.escape(label)}</div><ul class='points'>")
                o += [f"<li>{_inline(i)}</li>" for i in items]
                o.append("</ul>")
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
        if s.get("sowhat"):
            o.append(f"<div class='sowhat'><b>우리에게 무엇인가</b>{_inline(s['sowhat'])}</div>")
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
    o.append(f"<p class='sub'>모든 링크는 코퍼스 내 논문 리뷰 문서({H.escape(stats['link_base'])}/&lt;slug&gt;/index.html)로 연결된다.</p><ol>")
    for r in allrefs:
        cit = f" · 인용 {r['citations']:,}" if r["citations"] else ""
        who = f"{H.escape(r['author'])}, " if r["author"] else ""
        o.append(f"<li><a href='{H.escape(r['url'])}'>{H.escape(r['title'])}</a> "
                 f"<span class='m'>{who}{H.escape(r['date'])}{cit}</span></li>")
    o.append("</ol></section>")
    o.append(f"<footer class='deck'>pipeline/build_slide_deck.py --topic {H.escape(topic)} · {today} · "
             f"근거 코퍼스 {stats['total']:,}편</footer>")
    o.append("</div></body></html>")
    return "\n".join(o)


def main():
    ap = argparse.ArgumentParser(description="토픽 코퍼스 → 발표 슬라이드 원고(HTML + Obsidian MD)")
    ap.add_argument("--topic", default="ai4s", help="토픽 alias (기본 ai4s)")
    ap.add_argument("--per-category", type=int, default=5, help="대분류당 서브카테고리 슬라이드 수")
    ap.add_argument("--since", type=int, default=2025, help="사례 우선 기준 연도 (기본 2025)")
    ap.add_argument("--link-base", default="../../docs/papers",
                    help="리뷰 문서 링크 베이스. 로컬 서버면 http://localhost:8000/papers")
    ap.add_argument("--out-dir", default=None, help="출력 루트 (기본 reports/)")
    args = ap.parse_args()

    try:
        summaries, classification, timeline, insights, index = load_corpus(args.topic)
    except TaxonomyMismatch as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 2
    slides, stats = build_slides(args.topic, summaries, classification, timeline, insights, index,
                                 per_category=args.per_category, link_base=args.link_base,
                                 since=args.since)

    root = Path(args.out_dir) if args.out_dir else REPORTS
    html_path = root / "build" / f"{args.topic}_slides_{len(slides)}.html"
    md_path = root / "source" / f"{args.topic}_slides_{len(slides)}.md"
    atomic_write_text(html_path, render_html(args.topic, slides, stats))
    atomic_write_text(md_path, render_markdown(args.topic, slides, stats))

    n_refs = len({r["slug"] for s in slides for r in s.get("refs", [])})
    print(f"[OK] 슬라이드 {len(slides)}장 · 레퍼런스 {n_refs}편 "
          f"(코퍼스 {stats['total']:,}편, {stats['since']}+ {stats['recent_share']}%)")
    print(f"  HTML : {html_path}")
    print(f"  MD   : {md_path}")
    return 0


if __name__ == "__main__":
    from _env_guard import force_py312
    force_py312()
    sys.exit(main())
