#!/usr/bin/env python3
"""브리핑 문체 집필본(JSON) → `pipeline/lib/slide_brief_<topic>.py` 조립 + 계약 검사.

입력: reports/slide-dossier/<topic>/brief/<category-slug>.json ×N, _frame.json
      (58장 덱 NARRATIVE 와 같은 키 구조, 값만 명사 종결·음슴체·30% 짧게)
출력: BRIEF_LEAD(대분류 → 리드), BRIEF_NARRATIVE(서브카테고리·프레임 키 → {ko, headline, points, sowhat, …}),
      ACTION_RATIONALE(행동 카드 '왜' 문단 5개)

검사(위반 시 실패):
  - 키 집합이 58장 덱 NARRATIVE/CATEGORY_LEAD 와 일치(서브카테고리는 상위 5개만)
  - 각 항목의 플레이스홀더 multiset 이 원문과 동일
  - 길이: 각 항목 ≤ 원문의 0.70 (기본; --max-ratio) — 플레이스홀더 치환 전 글자 수
  - 서술형 종결 금지: `…다.`/`…다`/`…요` 로 끝나는 문장(명사·음슴체만 허용)
  - 라틴 문자 시스템명: 원문에 없는 새 토큰 금지(삭제는 허용)

Usage:
  python pipeline/assemble_slide_brief.py --topic ai4s [--check]
"""
import argparse
import json
import re
import sys
from pathlib import Path

PIPE = Path(__file__).resolve().parent
sys.path.insert(0, str(PIPE))
ROOT = PIPE.parent

from build_slide_deck import FRAME_KEYS  # noqa: E402
from lib.slide_prose_ai4s import CATEGORY_LEAD, NARRATIVE, PROSE  # noqa: E402

_PH = re.compile(r"\{[a-z_]+(?::[^{}]+)?\}")
_LATIN = re.compile(r"[A-Za-z][A-Za-z0-9]*(?:[-–.][A-Za-z0-9]+)*")
# '~다' 종결, 해요체('~어요/~아요/~해요/~예요/~지요/~네요/~죠'). '필요/중요' 같은 명사의 '요' 는 아니다.
_VERB_END = re.compile(r"(?:[가-힣]다|[어아해예지네]요|죠)\s*[.!]?\s*$")
_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")
_KEEP_FIELDS = ("headline", "points", "sowhat", "title_ko", "title_en", "extra", "refs")


class ContractError(Exception):
    pass


def _texts(v):
    if isinstance(v, str):
        return [v]
    if isinstance(v, list):
        return [t for x in v for t in _texts(x)]
    if isinstance(v, dict):
        return [t for x in v.values() for t in _texts(x)]
    return []


def _verb_ending_sentences(text):
    bad = []
    for sent in _SENT_SPLIT.split(text.strip()):
        core = re.sub(r"\*\*|\(.*?\)|\[.*?\]", "", sent).strip()
        if core and _VERB_END.search(core):
            bad.append(sent)
    return bad


def check_item(label, new, old, max_ratio, errors):
    if sorted(_PH.findall(new)) != sorted(_PH.findall(old)):
        errors.append(f"{label}: 플레이스홀더 불일치 {sorted(_PH.findall(old))} → {sorted(_PH.findall(new))}")
    # 길이는 플레이스홀더를 뺀 글자 수로 잰다(이름·편수는 치환 후 같은 길이로 늘어난다)
    # 짧은 항목(100자 미만)은 시스템명이 대부분이라 '12자 이상 감축' 도 인정
    n_len, o_len = len(_PH.sub("", new)), len(_PH.sub("", old))
    allowed = o_len * max_ratio if o_len >= 100 else max(o_len * max_ratio, o_len - 12)
    if o_len >= 30 and n_len > allowed:
        errors.append(f"{label}: 길이 {n_len}/{o_len} = {n_len / o_len:.2f} > {max_ratio}")
    for sent in _verb_ending_sentences(new):
        errors.append(f"{label}: 서술형 종결 — {sent[:50]}")
    new_tokens = {t for t in _LATIN.findall(_PH.sub("", new)) if len(t) >= 4 and not t.islower()}
    old_tokens = {t for t in _LATIN.findall(_PH.sub("", old)) if len(t) >= 4}
    extra = new_tokens - old_tokens
    if extra:
        errors.append(f"{label}: 원문에 없는 시스템명 {sorted(extra)}")


def check_entry(label, new, old, max_ratio, errors):
    for k in _KEEP_FIELDS:
        if k not in old:
            continue
        if k not in new:
            if k in ("title_en", "refs"):
                continue  # 원문에서 복사
            errors.append(f"{label}: '{k}' 누락")
            continue
        if k == "points":
            if len(new[k]) != len(old[k]):
                errors.append(f"{label}: points {len(new[k])}개 ≠ 원문 {len(old[k])}개")
            for i, (n, o) in enumerate(zip(new[k], old[k])):
                check_item(f"{label}.points[{i}]", n, o, max_ratio, errors)
        elif k == "extra":
            for ek, lst in old[k].items():
                nl = new[k].get(ek) or new[k].get(next(iter(new[k]), ek)) if isinstance(new[k], dict) else None
                if not nl:
                    errors.append(f"{label}: extra '{ek}' 누락")
                    continue
                for i, (n, o) in enumerate(zip(nl, lst)):
                    check_item(f"{label}.extra[{i}]", n, o, max_ratio, errors)
        elif k in ("title_en", "refs"):
            continue
        else:
            check_item(f"{label}.{k}", new[k], old[k], max_ratio, errors)


def load(topic, in_dir):
    cats, frame = {}, None
    for f in sorted(in_dir.glob("*.json")):
        if f.name.startswith("_source_"):
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        if f.name == "_frame.json":
            frame = d
        elif "category" in d:
            cats[d["category"]] = d
    if frame is None:
        raise ContractError("_frame.json 없음")
    return cats, frame


def validate(cats, frame, max_ratio):
    errors = []
    missing = set(CATEGORY_LEAD) - set(cats)
    if missing:
        errors.append(f"대분류 집필 누락: {sorted(missing)}")
    for name, d in cats.items():
        if name not in CATEGORY_LEAD:
            errors.append(f"모르는 대분류 {name}")
            continue
        check_item(f"{name}.lead", d["lead"], CATEGORY_LEAD[name], max_ratio, errors)
        for sub, ent in d["sub_themes"].items():
            if sub not in NARRATIVE:
                errors.append(f"{name}: 모르는 서브카테고리 {sub}")
                continue
            if ent.get("ko") != NARRATIVE[sub].get("ko"):
                errors.append(f"{sub}: ko 변경 금지 ({NARRATIVE[sub].get('ko')} → {ent.get('ko')})")
            check_entry(sub, ent, NARRATIVE[sub], max_ratio, errors)
    for key in FRAME_KEYS:
        if key not in frame:
            errors.append(f"frame '{key}' 누락")
            continue
        check_entry(f"frame.{key}", frame[key], NARRATIVE[key], max_ratio, errors)
    # 행동 근거: 행동 수(points) + '실행 순서' 1문단. 원문 줄글은 셋째·넷째가 한 문단이라 수가 다를 수 있다.
    body = frame.get("_action_prose_body")
    n_pts = len(NARRATIVE["action"]["points"])
    if not isinstance(body, list) or len(body) != n_pts + 1:
        errors.append(f"_action_prose_body: 문단 수 {len(body) if isinstance(body, list) else 0} ≠ 행동 {n_pts} + 실행 순서 1")
    else:
        ordinals = ["첫째", "둘째", "셋째", "넷째", "다섯째", "여섯째"]
        for i, para in enumerate(body[:n_pts]):
            if not para.startswith(ordinals[i]):
                errors.append(f"_action_prose_body[{i}]: '{ordinals[i]}' 로 시작해야 함")
            if _VERB_END.search(para):
                errors.append(f"_action_prose_body[{i}]: 서술형 종결 — {para[-30:]}")
        if not body[-1].startswith("실행 순서"):
            errors.append("_action_prose_body[-1]: '실행 순서' 로 시작해야 함")
        total_new = sum(len(x) for x in body)
        total_old = sum(len(x) for x in PROSE["action"]["body"])
        if total_new > total_old * max_ratio:
            errors.append(f"_action_prose_body: 총 길이 {total_new}/{total_old} = {total_new / total_old:.2f} > {max_ratio}")
    if errors:
        raise ContractError("\n".join(errors))


def render_module(topic, cats, frame, authored):
    lead = {name: d["lead"] for name, d in sorted(cats.items())}
    narrative = {}
    for name, d in sorted(cats.items()):
        for sub, ent in d["sub_themes"].items():
            narrative[sub] = {k: ent[k] for k in ("ko", "headline", "points", "sowhat") if k in ent}
    for key in FRAME_KEYS:
        src = NARRATIVE[key]
        ent = {k: frame[key][k] for k in _KEEP_FIELDS if k in frame[key]}
        for k in ("title_en", "refs"):
            if k in src and k not in ent:
                ent[k] = src[k]
        narrative[key] = ent
    rationale = list(frame["_action_prose_body"])

    def lit(v, indent=0):
        pad = " " * indent
        if isinstance(v, str):
            return json.dumps(v, ensure_ascii=False)
        if isinstance(v, list):
            if not v:
                return "[]"
            return "[\n" + ",\n".join(pad + "    " + lit(x, indent + 4) for x in v) + ",\n" + pad + "]"
        if isinstance(v, dict):
            return "{\n" + ",\n".join(pad + "    " + json.dumps(k, ensure_ascii=False) + ": " + lit(x, indent + 4)
                                      for k, x in v.items()) + ",\n" + pad + "}"
        return repr(v)

    return (f'"""브리핑 문체 집필본 ({topic}) — assemble_slide_brief.py 가 생성. 손으로 고칠 땐 이 파일을 고친다.\n\n'
            f"58장 덱 `slide_prose_{topic}.py` 의 NARRATIVE/CATEGORY_LEAD 와 키가 같고, 값만 과기정통부 보고용\n"
            f"문체(명사 종결·음슴체, 원문 대비 ≤70% 길이)다. 플레이스홀더는 원문과 동일.\n"
            f'"""\n\nBRIEF_AUTHORED = {json.dumps(authored)}\n\n'
            f"BRIEF_LEAD = {lit(lead)}\n\n"
            f"BRIEF_NARRATIVE = {lit(narrative)}\n\n"
            f"ACTION_RATIONALE = {lit(rationale)}\n")


def main():
    ap = argparse.ArgumentParser(description="브리핑 문체 집필본 조립")
    ap.add_argument("--topic", default="ai4s")
    ap.add_argument("--in-dir", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--authored", default=None, help="집필 일자 YYYY-MM-DD")
    ap.add_argument("--max-ratio", type=float, default=0.70)
    ap.add_argument("--check", action="store_true", help="검사만")
    args = ap.parse_args()
    in_dir = Path(args.in_dir) if args.in_dir else ROOT / "reports" / "slide-dossier" / args.topic / "brief"
    out = Path(args.out) if args.out else PIPE / "lib" / f"slide_brief_{args.topic}.py"
    try:
        cats, frame = load(args.topic, in_dir)
        validate(cats, frame, args.max_ratio)
    except ContractError as exc:
        print(f"[FAIL] 계약 위반\n{exc}", file=sys.stderr)
        return 1
    n_subs = sum(len(d["sub_themes"]) for d in cats.values())
    print(f"[check] 대분류 {len(cats)}개 · 서브카테고리 {n_subs}개 · 프레임 {len(FRAME_KEYS)}개 — 계약 통과")
    if args.check:
        return 0
    from datetime import date
    out.write_text(render_module(args.topic, cats, frame, args.authored or date.today().isoformat()), encoding="utf-8")
    print(f"  → {out} ({out.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
