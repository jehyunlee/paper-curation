#!/usr/bin/env python3
"""집필 JSON → lib/slide_prose_ai4s.py 조립.

입력(기본 reports/slide-dossier/<topic>/prose/):
  <category-slug>.json  — build_slide_dossier.py 가 뽑은 대분류별 근거로 집필한 항목
                          {category, ko, lead, sub_themes: {name: {ko, headline, points,
                           sowhat, prose: {lead, body, close}}}}
  _frame.json           — 오프닝·종합 10장
                          {frame: {key: {headline, sowhat, points?, title_ko?, title_en?,
                           refs?, extra?}}, prose: {key: {lead, body, close}}}

출력: pipeline/lib/slide_prose_ai4s.py — PROSE_AUTHORED, CATEGORY_KO, CATEGORY_LEAD,
NARRATIVE(서브카테고리 + 오프닝/종합 키), PROSE(동일 키).

조립 전에 계약을 검사한다: 대분류·서브카테고리 누락, 불릿 5개, 줄글 분량,
플레이스홀더 문법과 `{n:NAME}`/`{s:NAME}` 이름 유효성. 어긋나면 모듈을 쓰지 않는다.
"""
import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

PIPE = Path(__file__).resolve().parent
PROJECT_ROOT = PIPE.parent
sys.path.insert(0, str(PIPE))

from lib.atomic_io import atomic_write_text  # noqa: E402

FRAME_KEYS = ("cover", "method", "corpus", "landscape", "arc",
              "convergence", "riseandfall", "gaps", "verification", "action")
_PLACEHOLDER = re.compile(r"\{(?P<key>[a-z_]+)(?::(?P<arg>[^{}]+))?\}")
_GLOBAL_KEYS = {"total", "cards", "n_cats", "n_subs", "n_body", "per_category", "since",
                "recent_share", "y", "n", "sub", "ko", "s"}
_CAT_KEYS = {"cat_count", "cat_cards", "cat_share", "nsubs", "cat_ko"}
_SUB_KEYS = {"count", "recent", "sub_share"}
_MIN_PROSE_CHARS = 1000
_POINTS = 5


class ContractError(ValueError):
    pass


def _walk(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for v in value:
            yield from _walk(v)
    elif isinstance(value, dict):
        for v in value.values():
            yield from _walk(v)


def check_placeholders(value, where, names, slide_names, allow):
    """플레이스홀더 키 범위와 이름 참조를 검사한다. 어긋나면 ContractError."""
    for text in _walk(value):
        for m in _PLACEHOLDER.finditer(text):
            key, arg = m.group("key"), m.group("arg")
            if key not in allow:
                raise ContractError(f"{where}: 허용되지 않는 플레이스홀더 {{{key}}}")
            if key in ("n", "ko") and arg not in names:
                raise ContractError(f"{where}: {{{key}:{arg}}} — 분류체계에 없는 이름")
            if key == "cards" and arg and arg not in names:
                raise ContractError(f"{where}: {{cards:{arg}}} — 분류체계에 없는 이름")
            if key == "sub" and arg not in slide_names:
                raise ContractError(f"{where}: {{sub:{arg}}} — 서브카테고리가 아닌 이름")
            if key == "s" and arg not in slide_names:
                raise ContractError(f"{where}: {{s:{arg}}} — 본문 슬라이드가 아닌 이름")
            if key == "y" and not re.fullmatch(r"\d{4}", arg or ""):
                raise ContractError(f"{where}: {{y:{arg}}} — 연도 4자리여야 한다")
        # 치환 뒤에 남을 홀짝 괄호(문법 오류)도 잡는다.
        if re.search(r"\{[^{}]*$|^[^{}]*\}", _PLACEHOLDER.sub("", text)):
            raise ContractError(f"{where}: 짝이 맞지 않는 중괄호 — {text[:60]!r}")


def _prose_len(p):
    return len(p.get("lead", "")) + sum(len(x) for x in p.get("body", [])) + len(p.get("close", ""))


def load_inputs(in_dir, frame_json):
    """dossier `_frame.json` 이 정한 대분류·상위 서브카테고리 전부에 집필본이 있는지 확인."""
    frame = json.loads(Path(frame_json).read_text(encoding="utf-8"))
    expected = {c["category"]: c["top_subs"] for c in frame["categories"]}
    live_counts = {"_total": frame.get("total"), "_cards": frame.get("cards_total")}
    for c in frame["categories"]:
        live_counts[c["category"]] = {"count": c.get("count"), "card_count": c.get("card_count"),
                                      "subs": {}}
    for path in Path(frame_json).parent.glob("*.json"):
        if path.name == "_frame.json":
            continue
        d = json.loads(path.read_text(encoding="utf-8"))
        if d.get("category") in live_counts:
            live_counts[d["category"]]["subs"] = {s["name"]: s["count"] for s in d.get("sub_themes", [])}
    names = set(expected)
    slide_names = set()
    for subs in expected.values():
        names.update(subs)
        slide_names.update(subs)

    by_cat = {}
    for path in sorted(Path(in_dir).glob("*.json")):
        if path.name == "_frame.json":
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        cat = data.get("category")
        if cat not in expected:
            raise ContractError(f"{path.name}: 분류체계에 없는 대분류 {cat!r}")
        if cat in by_cat:
            raise ContractError(f"{path.name}: 대분류 {cat!r} 집필본 중복")
        by_cat[cat] = data

    missing = sorted(set(expected) - set(by_cat))
    if missing:
        raise ContractError(f"집필본 없는 대분류: {missing}")

    fpath = Path(in_dir) / "_frame.json"
    if not fpath.exists():
        raise ContractError(f"오프닝/종합 집필본 없음: {fpath}")
    frame_prose = json.loads(fpath.read_text(encoding="utf-8"))
    return expected, names, slide_names, by_cat, frame_prose, live_counts


def validate(expected, names, slide_names, by_cat, frame_prose, live_counts=None):
    live_counts = live_counts or {}
    for cat, subs in expected.items():
        d = by_cat[cat]
        where = f"[{cat}]"
        for field in ("ko", "lead"):
            if not d.get(field):
                raise ContractError(f"{where}: {field} 없음")
        check_placeholders(d["lead"], where + " lead", names, slide_names,
                           _GLOBAL_KEYS | _CAT_KEYS)
        got = list(d.get("sub_themes", {}).keys())
        if got != list(subs):
            raise ContractError(f"{where}: sub_themes 키가 dossier 와 다르다\n  기대 {subs}\n  실제 {got}")
        for name, ent in d["sub_themes"].items():
            w = f"{where} {name}"
            for field in ("ko", "headline", "sowhat", "prose"):
                if not ent.get(field):
                    raise ContractError(f"{w}: {field} 없음")
            if len(ent.get("points") or []) != _POINTS:
                raise ContractError(f"{w}: points {len(ent.get('points') or [])}개 (기대 {_POINTS})")
            pr = ent["prose"]
            if not pr.get("lead") or not pr.get("close") or len(pr.get("body") or []) < 4:
                raise ContractError(f"{w}: prose 는 lead·close·body 4문단 이상")
            if _prose_len(pr) < _MIN_PROSE_CHARS:
                raise ContractError(f"{w}: prose {_prose_len(pr)}자 < {_MIN_PROSE_CHARS}")
            check_placeholders(ent, w, names, slide_names, _GLOBAL_KEYS | _CAT_KEYS | _SUB_KEYS)
            # 코퍼스 편수를 숫자로 박았는지: 라이브 값과 같은 '{N}편' 리터럴만 잡는다
            # (논문이 보고한 데이터셋 규모 '51,529편' 같은 수치는 정당하다).
            live = live_counts.get(cat, {})
            forbidden = {live.get("count"), live.get("card_count"), live_counts.get("_total"),
                         live_counts.get("_cards")}
            forbidden |= {live.get("subs", {}).get(name)}
            forbidden.discard(None)
            for text in _walk(ent):
                for n in forbidden:
                    if re.search(rf"(?<![\d,{{:]){n:,}편", text):
                        raise ContractError(f"{w}: 코퍼스 편수 하드코딩 {n:,}편 — 플레이스홀더로 ({text[:50]!r})")

    fr, pr = frame_prose.get("frame", {}), frame_prose.get("prose", {})
    for key in FRAME_KEYS:
        w = f"[frame:{key}]"
        if key not in fr or key not in pr:
            raise ContractError(f"{w}: frame/prose 둘 다 있어야 한다")
        if not fr[key].get("headline") or not fr[key].get("sowhat"):
            raise ContractError(f"{w}: headline·sowhat 필수")
        if key in ("arc", "verification", "action") and len(fr[key].get("points") or []) < 4:
            raise ContractError(f"{w}: points 4개 이상")
        if key == "verification" and not fr[key].get("refs"):
            raise ContractError(f"{w}: refs(시스템명 목록) 필수")
        if not pr[key].get("lead") or not pr[key].get("close") or len(pr[key].get("body") or []) < 4:
            raise ContractError(f"{w}: prose 는 lead·close·body 4문단 이상")
        if _prose_len(pr[key]) < _MIN_PROSE_CHARS:
            raise ContractError(f"{w}: prose {_prose_len(pr[key])}자 < {_MIN_PROSE_CHARS}")
        check_placeholders(fr[key], w, names, slide_names, _GLOBAL_KEYS)
        check_placeholders(pr[key], w + " prose", names, slide_names, _GLOBAL_KEYS)


# ── Python 리터럴 출력 ────────────────────────────────────────────────────
def _s(text):
    return json.dumps(text, ensure_ascii=False)


def _emit(value, indent):
    pad = " " * indent
    if isinstance(value, str):
        return _s(value)
    if isinstance(value, list):
        if not value:
            return "[]"
        inner = ",\n".join(pad + "    " + _emit(v, indent + 4) for v in value)
        return "[\n" + inner + ",\n" + pad + "]"
    if isinstance(value, dict):
        if not value:
            return "{}"
        inner = ",\n".join(pad + "    " + _s(k) + ": " + _emit(v, indent + 4) for k, v in value.items())
        return "{\n" + inner + ",\n" + pad + "}"
    return repr(value)


def render_module(expected, by_cat, frame_prose, authored):
    cat_ko = {cat: by_cat[cat]["ko"] for cat in expected}
    cat_lead = {cat: by_cat[cat]["lead"] for cat in expected}
    narrative, prose = {}, {}
    for cat in expected:
        for name, ent in by_cat[cat]["sub_themes"].items():
            narrative[name] = {k: ent[k] for k in ("ko", "headline", "points", "sowhat")}
            prose[name] = {k: ent["prose"][k] for k in ("lead", "body", "close")}
    for key in FRAME_KEYS:
        narrative[key] = frame_prose["frame"][key]
        prose[key] = {k: frame_prose["prose"][key][k] for k in ("lead", "body", "close")}

    L = ['"""ai4s 발표 원고 집필본 — 덱(불릿)·줄글 두 판본의 한국어 본문.',
         "",
         "assemble_slide_prose.py 가 reports/slide-dossier/<topic>/prose/*.json 에서 조립한다.",
         "손으로 고칠 때는 이 파일을 직접 고친다(조립 입력은 reports/ 아래라 커밋되지 않는다).",
         "",
         "키: `_category_summaries.json` 의 sub_themes[].name, 또는 오프닝/종합 슬라이드 id",
         "    (cover, method, corpus, landscape, arc, convergence, riseandfall, gaps, verification, action).",
         "편수는 전부 플레이스홀더다 — build_slide_deck.ProseContext 가 빌드 시점 값으로 치환한다.",
         '"""',
         "",
         f'PROSE_AUTHORED = "{authored}"',
         "",
         "CATEGORY_KO = " + _emit(cat_ko, 0),
         "",
         "CATEGORY_LEAD = " + _emit(cat_lead, 0),
         "",
         "# ── 슬라이드 불릿판: ko / headline / points / sowhat (오프닝·종합은 refs/extra/title 추가) ──",
         "NARRATIVE = " + _emit(narrative, 0),
         "",
         "# ── 줄글판: lead / body[] / close ──",
         "PROSE = " + _emit(prose, 0),
         ""]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--topic", default="ai4s")
    ap.add_argument("--in-dir", default=None, help="기본 reports/slide-dossier/<topic>/prose")
    ap.add_argument("--frame-json", default=None, help="기본 reports/slide-dossier/<topic>/_frame.json")
    ap.add_argument("--out", default=None, help="기본 pipeline/lib/slide_prose_<topic>.py")
    ap.add_argument("--authored", default=date.today().isoformat(), help="PROSE_AUTHORED 날짜")
    ap.add_argument("--check", action="store_true", help="검사만 하고 쓰지 않는다")
    args = ap.parse_args()

    base = PROJECT_ROOT / "reports" / "slide-dossier" / args.topic
    in_dir = Path(args.in_dir) if args.in_dir else base / "prose"
    frame_json = Path(args.frame_json) if args.frame_json else base / "_frame.json"
    out = Path(args.out) if args.out else PIPE / "lib" / f"slide_prose_{args.topic}.py"

    try:
        expected, names, slide_names, by_cat, frame_prose, live = load_inputs(in_dir, frame_json)
        validate(expected, names, slide_names, by_cat, frame_prose, live)
    except ContractError as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 2
    n_subs = sum(len(v) for v in expected.values())
    print(f"[check] 대분류 {len(expected)}개 · 서브카테고리 {n_subs}개 · 오프닝/종합 {len(FRAME_KEYS)}개 — 계약 통과")
    if args.check:
        return 0
    text = render_module(expected, by_cat, frame_prose, args.authored)
    compile(text, str(out), "exec")
    atomic_write_text(out, text)
    print(f"[OK] {out} ({len(text):,} chars, PROSE_AUTHORED={args.authored})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
