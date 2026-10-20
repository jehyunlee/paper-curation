#!/usr/bin/env python3
"""AI for Science 지형도 — 정책 브리핑용 PPTX (과학기술정보통신부 보고 형식).

58장 발표 덱(`build_slide_deck.py`)의 데이터·집필본을 재사용하되, 정책 결정자를
대상으로 **그림 중심**으로 다시 짠 판본이다. 글은 헤드라인·시사점 수준으로 줄이고,
각 대분류는 코퍼스 논문의 도판(리뷰가 '핵심' 으로 고른 Figure)과 네이티브 차트로
보여 준다. 줄글(`PROSE`)은 발표자 노트로 들어간다.

구성(≈40장):
  표지 · 한눈에 보기 · 목차
  I.  코퍼스와 방법       — 연도 분포(차트) · 방법 흐름도 · 지형도(UMAP 지도) · 10개 지형 규모(차트)
  II. 10개 지형           — 대분류마다 2장: 개요(서브카테고리 차트 + 대표 도판) · 대표 연구(도판 3장)
  III. 흐름과 신호        — 관통 서사 · 수렴 · 부상/쇠퇴 · 공백
  IV. 검증으로의 전환     — 여섯 축 · 근거 도판
  V.  정책 제언           — 행동 5 · 관전 포인트
  부록                    — 방법 상세 · 지형-서브카테고리 표 · 도판 출처

출력: reports/build/{topic}_brief_<N>.pptx  (+ 지도 PNG: .cache/slide-brief/<topic>/landscape.png)

Usage:
  PYTHONUTF8=1 python pipeline/build_slide_brief.py --topic ai4s
"""
import argparse
import json
import os
import re
import sqlite3
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION, XL_LEGEND_POSITION
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

PIPE = Path(__file__).resolve().parent
sys.path.insert(0, str(PIPE))
PROJECT_ROOT = PIPE.parent

import build_slide_deck as B  # noqa: E402
from config_loader import PAPERS_DIR, get_topic_dir  # noqa: E402
from lib.slide_prose_ai4s import CATEGORY_KO, PROSE  # noqa: E402
from lib.slide_brief_ai4s import BRIEF_LEAD, BRIEF_NARRATIVE, ACTION_RATIONALE  # noqa: E402

NARRATIVE = BRIEF_NARRATIVE      # 브리핑 문체(명사 종결·음슴체) 판본 — 58장 덱의 NARRATIVE 와 키 동일
CATEGORY_LEAD = BRIEF_LEAD

REPORTS = PROJECT_ROOT / "reports"
CACHE = PROJECT_ROOT / ".cache" / "slide-brief"

# ── 디자인 토큰 ─────────────────────────────────────────────────────────────
W, H = Inches(13.333), Inches(7.5)
M = Inches(0.55)                      # 좌우 여백
TOP = Inches(1.3)                     # 본문 시작 y
BOTTOM = H - Inches(0.55)             # 본문 끝 y (푸터 위)
INNER_W = W - 2 * M

NAVY = RGBColor(0x0B, 0x2E, 0x4F)
INK = RGBColor(0x1F, 0x29, 0x37)
MUTED = RGBColor(0x6B, 0x72, 0x80)
LINE = RGBColor(0xD9, 0xDE, 0xE5)
PANEL = RGBColor(0xF4, 0xF6, 0xF8)
ACCENT = RGBColor(0x1A, 0x6F, 0xC4)
LINK = RGBColor(0x1F, 0x4E, 0x9A)
GOLD = RGBColor(0xE0, 0x9F, 0x1F)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
RED = RGBColor(0xC0, 0x39, 0x2B)
GREEN = RGBColor(0x2E, 0x8B, 0x57)

PALETTE = ["1F4E79", "2A9D8F", "E76F51", "C9A227", "6A4C93",
           "3C8D5A", "B23A48", "4C78A8", "8C6D3F", "5C6B73"]

FONT_LATIN = "Helvetica Neue"
FS = 1.2   # 본문 글자 배율(타이틀 제외). 가독성 요구로 20% 확대
FONT_EA = "Malgun Gothic"   # Office(Win·Mac) 동봉. 비우면 PowerPoint(Mac) 가 바탕체로 대체한다.
KOREAN_TTC = "/System/Library/Fonts/AppleSDGothicNeo.ttc"  # 지도(matplotlib) 렌더용

_MD_BOLD = re.compile(r"\*\*(.+?)\*\*")
_SREF_PAREN = re.compile(r"\s*\((?:S\d{2})(?:[·,]\s*S\d{2})*\)")
_SREF = re.compile(r"\bS(\d{2})\b")

# ── 텍스트 유틸 ─────────────────────────────────────────────────────────────


def E(v):
    """EMU 정수화. `INNER_W * 0.6` 같은 float 가 xfrm 에 그대로 쓰이면(cx="6711513.0")
    PowerPoint 는 그 도형·차트를 조용히 버린다(LibreOffice 는 관대하다)."""
    return Emu(int(round(v)))



def rgb(hex_str):
    hex_str = hex_str.lstrip("#")
    return RGBColor(int(hex_str[0:2], 16), int(hex_str[2:4], 16), int(hex_str[4:6], 16))


def _set_font(run, size, bold=False, italic=False, color=INK, scale=True):
    f = run.font
    f.size = Pt(round(size * (FS if scale else 1.0), 1))
    f.bold = bold
    f.italic = italic
    f.name = FONT_LATIN
    f.color.rgb = color
    rpr = run._r.get_or_add_rPr()
    ea = rpr.find(qn("a:ea"))
    if ea is None:
        ea = rpr.makeelement(qn("a:ea"), {})
        rpr.append(ea)
    ea.set("typeface", FONT_EA)


def add_runs(paragraph, text, size, color=INK, bold=False, italic=False, scale=True):
    """`**굵게**` 마크다운을 run 으로 풀어 넣는다. `scale=False` 는 슬라이드 타이틀(배율 제외)."""
    pos = 0
    for m in _MD_BOLD.finditer(text):
        if m.start() > pos:
            r = paragraph.add_run()
            r.text = text[pos:m.start()]
            _set_font(r, size, bold, italic, color, scale)
        r = paragraph.add_run()
        r.text = m.group(1)
        _set_font(r, size, True, italic, color, scale)
        pos = m.end()
    if pos < len(text):
        r = paragraph.add_run()
        r.text = text[pos:]
        _set_font(r, size, bold, italic, color, scale)


def textbox(slide, x, y, w, h, *, anchor=MSO_ANCHOR.TOP, fill=None, line=None, inset=0.08,
            inset_v=None, radius=False):
    if fill is not None or line is not None or radius:
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE,
                                       E(x), E(y), E(w), E(h))
        if radius:
            shape.adjustments[0] = 0.06
        if fill is not None:
            shape.fill.solid()
            shape.fill.fore_color.rgb = fill
        else:
            shape.fill.background()
        if line is not None:
            shape.line.color.rgb = line
            shape.line.width = Pt(0.75)
        else:
            shape.line.fill.background()
        shape.shadow.inherit = False
    else:
        shape = slide.shapes.add_textbox(E(x), E(y), E(w), E(h))
    tf = shape.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(inset)
    tf.margin_top = tf.margin_bottom = Inches(inset if inset_v is None else inset_v)
    return shape, tf


def para(tf, first):
    return tf.paragraphs[0] if first else tf.add_paragraph()


def rect(slide, x, y, w, h, color, line=None, shape_type=MSO_SHAPE.RECTANGLE):
    shp = slide.shapes.add_shape(shape_type, E(x), E(y), E(w), E(h))
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
        shp.line.width = Pt(0.75)
    shp.shadow.inherit = False
    return shp


def strip_srefs(text, sub_ko_by_no):
    """58장 덱용 슬라이드 참조(S17 등)를 이 덱에서는 서브카테고리 이름으로 바꾼다."""
    text = _SREF_PAREN.sub("", text)
    return _SREF.sub(lambda m: f"'{sub_ko_by_no.get(int(m.group(1)), 'S' + m.group(1))}'", text)


def strip_year(point):
    """불릿 머리의 '2026 ' / '배경: ' 를 떼어낸다 (그림 캡션용)."""
    return re.sub(r"^(?:\d{4}(?:[–-]\d{4})?\s+|배경:\s*)", "", point).strip()


_SLUG_REFS = re.compile(r"\s*\(\s*(?!(?:19|20)\d{2}\s*\))\d{3,5}(?:\s*[,/]\s*\d{3,5})*\s*\)")
# 괄호 없이 박힌 근거 번호: "예측 10900/10714," — 연도(1990–2039)·단위가 붙은 수는 남긴다
_BARE_SLUGS = re.compile(r"(?<![A-Za-z0-9.\-])(?!(?:19|20)\d{2}(?![\d/]))\d{3,5}(?:/\d{3,5})*(?![\d%편개배장종회x×KMBp.])")


def ko_names(text):
    """인사이트 본문에 섞인 영문 대분류명을 한국어 표기로 바꾸고, 근거 슬러그 번호 괄호는 뗀다."""
    text = _SLUG_REFS.sub("", text or "")
    text = _BARE_SLUGS.sub("", text)
    text = re.sub(r"\s+([,.)])", r"\1", re.sub(r"[ ]{2,}", " ", text))
    for en, ko in sorted(CATEGORY_KO.items(), key=lambda kv: -len(kv[0])):
        text = re.sub(re.escape(en) + r"(?:\s+카테고리)?", ko, text)
    return text


def text_budget(w, h, size=10.5, reserve=Inches(0.0)):
    """카드 폭·높이에 들어가는 대략의 글자 수(한글 기준). 넘치면 shorten 으로 자른다."""
    size = size * FS
    cpl = int((w - Inches(0.36)) / (Inches(0.0118) * size))
    lines = int((h - reserve) / (Pt(size) * 1.4))
    return max(40, int(cpl * lines * 0.95))


def text_lines(text, w, size=10.5):
    """폭 w 에 size pt 로 적었을 때 줄 수(한글 기준 추정). 줄바꿈 문자는 그대로 센다."""
    cpl = max(1, int(w / (Inches(0.0118) * size * FS)))
    return sum(max(1, -(-len(line) // cpl)) for line in (text or "").split("\n"))


def shorten(text, n):
    text = re.sub(r"\s+", " ", text or "").strip()
    if len(text) <= n:
        return text
    cut = text[:n]
    # 문장 경계 → 절 경계(연결어미 뒤의 쉼표). 명사구 중간의 쉼표에서는 자르지 않는다('…데이터와 부합하는지를' 방지)
    for sep in _CUT_SEPS:
        i = cut.rfind(sep)
        if i >= n * 0.55:
            return cut[:i + len(sep) - 1].rstrip(", ")
    return cut.rstrip() + "…"


_CUT_SEPS = ("다. ", "다, ", ". ", "고, ", "며, ", "지만, ", "으나, ", "면서, ", "있어, ", "없어, ", "해, ", "돼, ", "되어, ", "하여, ")


# ── 명사형 종결(음슴체) 변환 ─────────────────────────────────────────────────
# 리뷰 essence·인사이트 설명처럼 저작 단계를 거치지 않은 문장은 규칙으로 '~다.' 를 '~음/~ㅁ' 으로 바꾼다.
# 저작 텍스트(lib/slide_brief_ai4s.py)는 이미 명사형이라 여기 오지 않는다.

_HANGUL0 = 0xAC00
_JONG = ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ",
         "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
_JONG_M, _JONG_N, _JONG_B, _JONG_L = 16, 4, 17, 8
# ㅂ 규칙 활용 어간(좁다·잡다·입다…)은 그대로 '~음', 나머지 ㅂ 어간은 '~우+ㅁ'(어렵다→어려움)
_B_REGULAR = {"좁", "잡", "입", "씹", "뽑", "업", "접", "집", "굽"}
# 절 끝에서 잘린 연결형 → 명사형 (있어→있음, 보여 줘→보여 줌)
_ENDING_MAP = {"있어": "있음", "없어": "없음", "되어": "됨", "하여": "함", "해": "함", "돼": "됨", "줘": "줌", "이어": "임"}
_CONNECTIVE = re.compile(r"(?:며|고|지만|으나|면서|어서|아서|고자)$")   # 어간은 남긴다: 시스템이며→시스템이→시스템임
_ENDING = re.compile(r"(?P<stem>[가-힣]+?)(?P<tail>는다|ㄴ다|다)(?P<punct>[.!]?)$")


def _jamo(ch):
    code = ord(ch) - _HANGUL0
    return code // 588, (code % 588) // 28, code % 28


def _compose(cho, jung, jong):
    return chr(_HANGUL0 + cho * 588 + jung * 28 + jong)


def _nominal_stem(stem):
    """어간 → 명사형. 받침 없음·ㄴ받침(현재형)→ㅁ 받침, ㅆ받침(과거)·그 외 받침→'음'."""
    if not stem or not ("가" <= stem[-1] <= "힣"):
        return stem
    cho, jung, jong = _jamo(stem[-1])
    if jong == 0:
        return stem[:-1] + _compose(cho, jung, _JONG_M)
    if jong == _JONG_N:   # 한다→함, 된다→됨, 본다→봄
        return stem[:-1] + _compose(cho, jung, _JONG_M)
    if jong == _JONG_B and stem[-1] not in _B_REGULAR:   # 어렵→어려움
        return stem[:-1] + _compose(cho, jung, 0) + "움"
    if jong == _JONG_L:   # 길다→긺, 살다→삶
        return stem[:-1] + _compose(cho, jung, 10)   # ㄻ
    return stem + "음"


def _nominal_sentence(sent):
    sent = sent.strip()
    if not sent:
        return sent
    body, punct = (sent[:-1], sent[-1]) if sent[-1] in ".!" else (sent, "")
    m = re.search(r"([가-힣]+)$", body)
    if not m:
        return sent
    word = m.group(1)
    head = body[:m.start()]
    for suf, rep in _ENDING_MAP.items():
        if word.endswith(suf) and (len(word) > len(suf) or head.endswith(" ")):   # '보여 줘' 의 '줘'
            return head + word[:-len(suf)] + rep + punct
    if word.endswith("는다") and len(word) > 2:
        new = word[:-2] + "음"                      # 먹는다→먹음
    elif word.endswith("다") and len(word) > 1:
        new = _nominal_stem(word[:-1])              # 한다→함, 했다→했음, 이다→임, 높다→높음
    else:
        c = _CONNECTIVE.search(word)                # 문장 중간에서 잘린 '~이며' '~하고' 등
        if c and c.start() > 0:
            new = _nominal_stem(word[:c.start()])
        else:
            return sent
    return head + new + punct


def nominalize(text):
    """'~다.' 서술형 종결을 명사형으로. 문장 단위로 처리하고 라틴 문자·숫자로 끝나는 문장은 그대로 둔다."""
    text = re.sub(r"\s+", " ", text or "").strip()
    if not text:
        return text
    parts = re.split(r"(?<=[.!])\s+", text)
    out = [_nominal_sentence(pt) for pt in parts]
    res = " ".join(out)
    return re.sub(r"…$", "", res) if res.endswith("…") and not text.endswith("…") else res


# ── 출처 링크 ───────────────────────────────────────────────────────────────


def source_links(slugs):
    """slug → (표시 문자열, URL). DOI 가 있으면 doi.org, 없으면 원문 URL(arXiv 등).
    인덱스에는 검증된 DOI 만 실려 있어 서지 DB(.cache/bibliography.sqlite3) 를 함께 본다."""
    db_path = Path(os.environ.get("PAPER_CURATION_BIBLIO_DB", str(PROJECT_ROOT / ".cache" / "bibliography.sqlite3")))
    out = {}
    if db_path.exists():
        con = sqlite3.connect(str(db_path))
        try:
            rows = con.execute("SELECT slug, doi, url FROM papers").fetchall()
        finally:
            con.close()
        for slug, doi, url in rows:
            if slug not in slugs:
                continue
            doi = (doi or "").strip()
            url = (url or "").strip()
            if doi:
                out[slug] = (f"doi.org/{doi}", f"https://doi.org/{doi}")
            elif url:
                out[slug] = (re.sub(r"^https?://(www\.)?", "", url), url)
    return out


# ── 도판 인덱스 ─────────────────────────────────────────────────────────────
_FIG_RE = re.compile(r"!\[Figure (\d+)\]\(figures/(fig\d+\.\w+)\)\s*\n\s*\n\*(.*?)\*", re.S)


def figure_index(papers, papers_dir):
    """리뷰 문서가 실은 도판(순서 = 리뷰가 Essence→Achievement→How 로 고른 순)과 크기."""
    out = {}
    for p in papers:
        if not p.get("has_figures"):
            continue
        d = Path(papers_dir) / p["slug"]
        try:
            md = (d / "review.md").read_text(encoding="utf-8")
        except FileNotFoundError:
            continue
        figs, seen = [], set()
        for m in _FIG_RE.finditer(md):
            fname = m.group(2)
            if fname in seen:
                continue
            seen.add(fname)
            path = d / "figures" / fname
            if not path.exists():
                continue
            try:
                with Image.open(path) as im:
                    w, h = im.size
            except Exception:
                continue
            figs.append({"path": path, "w": w, "h": h, "n": int(m.group(1)),
                         "caption": re.sub(r"\s+", " ", m.group(3)).strip()})
        if figs:
            out[p["slug"]] = figs
    return out


def good_figure(figs):
    """슬라이드에 올릴 첫 도판: 폭 700px 이상, 가로세로비 0.45~2.8.
    리뷰가 고른 순서(Essence → Achievement → How)를 그대로 따른다. PDF 추출 시 본문 단이
    딸려온 도판을 이미지 통계로 걸러내는 시도는 축 라벨·패널까지 잘라 먹어 접었다."""
    for f in figs:
        if f["w"] >= 700 and 0.45 <= f["w"] / f["h"] <= 2.8:
            return f
    return None


def autocrop(im, thresh=245, pad=12):
    """도판 둘레의 흰 여백(PDF 추출 시 딸려온 캡션 주변 공백 등)을 잘라낸다."""
    from PIL import ImageChops
    gray = im.convert("L").point(lambda v: 255 if v >= thresh else 0)
    bbox = ImageChops.invert(gray).getbbox()
    if not bbox:
        return im
    x0, y0, x1, y1 = bbox
    # 거의 전체면 그대로, 너무 작게 잘리면(본문 글자만 남는 경우) 원본 유지
    if (x1 - x0) * (y1 - y0) < 0.12 * im.width * im.height:
        return im
    x0, y0 = max(0, x0 - pad), max(0, y0 - pad)
    x1, y1 = min(im.width, x1 + pad), min(im.height, y1 + pad)
    return im.crop((x0, y0, x1, y1))


def to_png(src, cache_dir, max_px=1600):
    """webp → png (PowerPoint 호환), 흰 여백 제거, 긴 변 max_px 로 축소. 캐시."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    out = cache_dir / (src.parent.parent.name + "_" + src.stem + ".png")
    if out.exists() and out.stat().st_mtime >= src.stat().st_mtime:
        return out
    with Image.open(src) as raw:
        im = autocrop(raw.convert("RGB"))
    if max(im.size) > max_px:
        im.thumbnail((max_px, max_px), Image.LANCZOS)
    im.save(out, "PNG", optimize=True)
    return out


def fit_picture(slide, path, x, y, w, h, *, frame=True, pad=Inches(0.06)):
    """박스 안에 비율을 지키며 가운데 배치. 테두리 패널은 선택."""
    with Image.open(path) as im:
        im_w, im_h = im.size
    box_w, box_h = w - 2 * pad, h - 2 * pad
    scale = min(box_w / im_w, box_h / im_h)
    pw, ph = int(im_w * scale), int(im_h * scale)
    px, py = x + (w - pw) // 2, y + (h - ph) // 2
    if frame:
        rect(slide, x, y, w, h, WHITE, line=LINE)
    pic = slide.shapes.add_picture(str(path), E(px), E(py), E(pw), E(ph))
    return pic


# ── 지형도(UMAP) 이미지 ─────────────────────────────────────────────────────


def render_landscape(topic, cats, classification, out_path, colors, *, dark=False):
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib import font_manager as fm

    coords = json.loads((get_topic_dir(topic) / "_umap_coords.json").read_text(encoding="utf-8"))
    fp = fm.FontProperties(fname=KOREAN_TTC, weight="bold") if Path(KOREAN_TTC).exists() else None
    pts = defaultdict(list)
    for a in classification.get("assignments", []):
        c = coords.get(a["slug"])
        if c:
            pts[a.get("primary_category")].append((c["x"], c["y"]))
    fig, ax = plt.subplots(figsize=(12.2, 6.2) if not dark else (7.0, 6.2), dpi=160)
    if dark:
        bg = "#0B2E4F"
        fig.patch.set_facecolor(bg)
        ax.set_facecolor(bg)
    for c in cats:
        P = np.array(pts.get(c["category"]) or [[0, 0]])
        ax.scatter(P[:, 0], P[:, 1], s=8 if not dark else 6, c="#" + colors[c["category"]],
                   alpha=0.75 if not dark else 0.55, linewidths=0)
    if dark:
        ax.set_axis_off()
        ax.margins(0.03)
        plt.tight_layout(pad=0.2)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(out_path, dpi=160, facecolor=bg)
        plt.close(fig)
        return out_path
    for c in cats:
        P = np.array(pts.get(c["category"]) or [[0, 0]])
        cx, cy = np.median(P[:, 0]), np.median(P[:, 1])
        ax.text(cx, cy, f"{CATEGORY_KO.get(c['category'], c['category'])}\n{len(P):,}편",
                fontproperties=fp, fontsize=10.5, ha="center", va="center", color="white",
                bbox=dict(boxstyle="round,pad=0.35", fc="#" + colors[c["category"]], ec="white", lw=1.2, alpha=0.96))
    ax.set_axis_off()
    ax.margins(0.02)
    plt.tight_layout(pad=0.2)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=160, facecolor="white")
    plt.close(fig)
    return out_path


# ── 덱 ─────────────────────────────────────────────────────────────────────


class Brief:
    def __init__(self, topic, corpus, insights, figs, colors, sub_ko_by_no):
        self.topic = topic
        self.corpus = corpus
        self.ctx = corpus["ctx"]
        self.insights = insights
        self.figs = figs
        self.colors = colors
        self.sub_ko_by_no = sub_ko_by_no
        self.links = source_links({p["slug"] for p in corpus["papers"]})
        self.prs = Presentation()
        self.prs.slide_width, self.prs.slide_height = W, H
        self.footers = []
        self.sources = []   # (slide_no, paper, fig) 도판 출처 부록
        self.toc = []       # (part, title)
        self.cache_dir = CACHE / topic / "figs"

    # ── 공통 크롬 ──
    def slide(self):
        return self.prs.slides.add_slide(self.prs.slide_layouts[6])

    def chrome(self, s, section, title, subtitle="", accent=None):
        accent = accent or ACCENT
        rect(s, 0, 0, W, Inches(0.08), NAVY)
        _, tf = textbox(s, M, Inches(0.22), INNER_W, Inches(0.28), inset=0.0)
        add_runs(tf.paragraphs[0], section, 10, accent, bold=True)
        _, tf = textbox(s, M, Inches(0.46), INNER_W - Inches(3.2), Inches(0.6), anchor=MSO_ANCHOR.MIDDLE, inset=0.0)
        add_runs(tf.paragraphs[0], title, 24, NAVY, bold=True, scale=False)
        if subtitle:
            _, tf = textbox(s, M, Inches(1.0), INNER_W, Inches(0.28), inset=0.0)
            add_runs(tf.paragraphs[0], subtitle, 11, MUTED)
        rect(s, M, Inches(1.24), INNER_W, Emu(9525), LINE)
        self.footer(s)

    def footer(self, s, dark=False):
        color = RGBColor(0xB8, 0xC4, 0xD0) if dark else MUTED
        _, tf = textbox(s, M, H - Inches(0.42), Inches(8), Inches(0.3), inset=0.0, anchor=MSO_ANCHOR.MIDDLE)
        add_runs(tf.paragraphs[0], "AI for Science 지형도 2026  |  과학기술정보통신부 보고  |  논문 리뷰 코퍼스 "
                 f"{self.ctx.total:,}편", 8, color)
        box, tf = textbox(s, W - M - Inches(1.2), H - Inches(0.42), Inches(1.2), Inches(0.3), inset=0.0,
                          anchor=MSO_ANCHOR.MIDDLE)
        tf.paragraphs[0].alignment = PP_ALIGN.RIGHT
        self.footers.append((tf, color))

    def notes(self, s, *texts):
        body = "\n\n".join(re.sub(r"\*\*(.+?)\*\*", r"\1", t) for t in texts if t)
        if body:
            s.notes_slide.notes_text_frame.text = body

    def prose_notes(self, key):
        p = PROSE.get(key)
        if not p:
            return ""
        return "\n\n".join([p["lead"], *p["body"], p["close"]])

    def fill(self, text, cat=None, sub=None):
        return strip_srefs(self.ctx.fill(text, cat=cat, sub=sub), self.sub_ko_by_no)

    # ── 구성 요소 ──
    def kpi(self, s, x, y, w, h, number, label, color=NAVY):
        rect(s, x, y, w, h, PANEL)
        rect(s, x, y, Inches(0.07), h, color)
        _, tf = textbox(s, x + Inches(0.2), y + Inches(0.1), w - Inches(0.3), h * 0.58, anchor=MSO_ANCHOR.BOTTOM, inset=0.0)
        add_runs(tf.paragraphs[0], number, 34, color, bold=True, scale=False)
        _, tf = textbox(s, x + Inches(0.2), y + h * 0.62, w - Inches(0.3), h * 0.36, inset=0.0)
        add_runs(tf.paragraphs[0], label, 11, MUTED)

    def card(self, s, x, y, w, h, title, body, *, color=ACCENT, number=None, tag=None, size=11):
        """제목·태그·본문 카드. 제목이 두 줄로 접히면 본문을 그만큼 내린다. 본문 시작 y 를 돌려준다."""
        rect(s, x, y, w, h, WHITE, line=LINE)
        rect(s, x, y, w, Inches(0.06), color)
        ty = y + Inches(0.16)
        if number is not None:
            circ = rect(s, x + Inches(0.16), ty, Inches(0.34), Inches(0.34), color, shape_type=MSO_SHAPE.OVAL)
            tf = circ.text_frame
            tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
            tf.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf.paragraphs[0].alignment = PP_ALIGN.CENTER
            add_runs(tf.paragraphs[0], str(number), 11, WHITE, bold=True)
            tx = x + Inches(0.6)
        else:
            tx = x + Inches(0.18)
        tw = w - (tx - x) - Inches(0.15)
        t_lines = text_lines(title, tw, size + 2)
        th = Inches(0.5) + (Pt((size + 2) * FS) * 1.2 if t_lines > 1 else 0)
        _, tf = textbox(s, tx, ty - Inches(0.02), tw, th, inset=0.0, anchor=MSO_ANCHOR.MIDDLE)
        add_runs(tf.paragraphs[0], title, size + 2, NAVY, bold=True)
        by = ty + th
        if tag:
            _, tf = textbox(s, x + Inches(0.18), by, w - Inches(0.36), Inches(0.26), inset=0.0)
            add_runs(tf.paragraphs[0], tag, 9, color, bold=True)
            by += Inches(0.26)
        _, tf = textbox(s, x + Inches(0.18), by, w - Inches(0.36), y + h - by - Inches(0.12), inset=0.0)
        add_runs(tf.paragraphs[0], body, size, INK)
        return by

    def figure(self, s, paper, fig, x, y, w, h, *, title=None, caption=None, sub_name=None,
               title_size=11, cap_size=9.5, cap_lines=3, frame=True):
        """도판 + 아래 캡션(굵은 한 줄 + 설명 + 출처). 출처는 부록에 모은다."""
        cap_h = Inches(0.24) * (1 + cap_lines) + Inches(0.22)
        pic_h = h - cap_h
        png = to_png(fig["path"], self.cache_dir)
        fit_picture(s, png, x, y, w, pic_h, frame=frame)
        cy = y + pic_h + Inches(0.06)
        _, tf = textbox(s, x, cy, w, cap_h - Inches(0.06), inset=0.02)
        p = tf.paragraphs[0]
        head = title or B.clean_title(paper.get("title", ""))
        add_runs(p, shorten(head, 60), title_size, NAVY, bold=True)
        if caption:
            p = tf.add_paragraph()
            p.space_before = Pt(2)
            add_runs(p, caption, cap_size, INK)
        p = tf.add_paragraph()
        p.space_before = Pt(2)
        label, url = self.links.get(paper["slug"], ("", ""))
        if label:
            r = p.add_run()
            r.text = label
            _set_font(r, 8, color=LINK)
            r.hyperlink.address = url
        tail = f"  ·  Fig. {fig['n']}"
        if sub_name:
            tail += f"  ·  {sub_name}"
        r = p.add_run()
        r.text = tail
        _set_font(r, 8, color=MUTED)
        self.sources.append((len(self.prs.slides), paper, fig))

    def bar_chart(self, s, x, y, w, h, labels, values, color, *, horizontal=True, size=10,
                  number_format="#,##0", point_colors=None, series_name="편수"):
        data = CategoryChartData()
        data.categories = labels
        data.add_series(series_name, values)
        kind = XL_CHART_TYPE.BAR_CLUSTERED if horizontal else XL_CHART_TYPE.COLUMN_CLUSTERED
        gf = s.shapes.add_chart(kind, E(x), E(y), E(w), E(h), data)
        ch = gf.chart
        ch.has_legend = False
        ch.has_title = False
        ch.font.size = Pt(round(size * FS))
        ch.font.name = FONT_LATIN
        plot = ch.plots[0]
        plot.gap_width = 60
        plot.has_data_labels = True
        dl = plot.data_labels
        dl.font.size = Pt(round(size * FS))
        dl.font.color.rgb = INK
        dl.number_format = number_format
        dl.number_format_is_linked = False
        dl.position = XL_LABEL_POSITION.OUTSIDE_END
        ser = plot.series[0]
        ser.format.fill.solid()
        ser.format.fill.fore_color.rgb = color
        if point_colors:
            for i, pc in enumerate(point_colors):
                pt = ser.points[i]
                pt.format.fill.solid()
                pt.format.fill.fore_color.rgb = pc
        va, ca = ch.value_axis, ch.category_axis
        va.visible = False
        va.has_major_gridlines = False
        va.maximum_scale = max(values) * (1.18 if horizontal else 1.22)
        ca.tick_labels.font.size = Pt(round(size * FS))
        ca.tick_labels.font.color.rgb = INK
        ca.format.line.color.rgb = LINE
        ca.has_major_gridlines = False
        if horizontal:
            ca.reverse_order = True
        # 축 글꼴에도 한글 글꼴 지정
        for ax in (ca, va):
            txPr = ax.tick_labels._element if hasattr(ax.tick_labels, "_element") else None
        return ch

    def finish_footers(self):
        n = len(self.prs.slides)
        for (tf, color), no in zip(self.footers, self._footer_no):
            add_runs(tf.paragraphs[0], f"{no} / {n}", 8, color)

    # ── 슬라이드들 ──
    def build(self):
        self._footer_no = []
        c = self.corpus
        self.s_cover()
        self.s_summary()
        self.s_toc()
        self.divider("I", "코퍼스와 방법", "대상과 분류 절차", ["연도 분포", "분류 방법", "지형도", "10개 지형의 규모"])
        self.s_corpus()
        self.s_method()
        self.s_landscape_map()
        self.s_landscape_sizes()
        self.divider("II", "10개 지형", "대분류별 전선 · 대표 연구", [CATEGORY_KO.get(x["category"], x["category"]) for x in c["cats"]])
        for i, cat in enumerate(c["cats"], start=1):
            self.s_category_overview(i, cat)
            self.s_category_figures(i, cat)
        self.divider("III", "흐름과 신호", "지형 횡단 신호", ["관통 서사", "수렴 신호", "부상과 쇠퇴", "비어 있는 자리"])
        self.s_arc()
        self.s_convergence()
        self.s_riseandfall()
        self.s_gaps()
        self.divider("IV", "검증으로의 전환", "2026년 공통 주제", ["여섯 축", "근거 도판"])
        self.s_verification()
        self.s_verification_evidence()
        self.divider("V", "정책 제언", "국내 연구기관·기업·정부의 과제", ["다섯 가지 행동", "관전 포인트 12개월"])
        self.s_actions()
        self.s_watchlist()
        self.divider("부록", "방법 상세 · 출처", "", ["분류 방법 상세", "지형-서브카테고리 표", "도판 출처"])
        self.s_appendix_method()
        self.s_appendix_table()
        self.s_appendix_sources()
        self.finish_footers()
        return self.prs

    def _num(self, s):
        self._footer_no.append(len(self.prs.slides))

    def s_cover(self):
        s = self.slide()
        rect(s, 0, 0, W, H, NAVY)
        png = render_landscape(self.topic, self.corpus["cats"], self.corpus["classification"],
                               CACHE / self.topic / "landscape_dark.png", self.colors, dark=True)
        fit_picture(s, png, W - Inches(6.4), Inches(0.3), Inches(6.2), H - Inches(1.3), frame=False, pad=0)
        rect(s, 0, H - Inches(0.9), W, Inches(0.9), RGBColor(0x08, 0x22, 0x3B))
        rect(s, M, Inches(2.1), Inches(0.9), Inches(0.06), GOLD)
        _, tf = textbox(s, M, Inches(1.45), INNER_W, Inches(0.5), inset=0.0)
        add_runs(tf.paragraphs[0], "AI FOR SCIENCE  ·  연구 지형 브리핑", 13, RGBColor(0xB8, 0xC4, 0xD0), bold=True)
        _, tf = textbox(s, M, Inches(2.3), Inches(7.2), Inches(2.3), inset=0.0)
        add_runs(tf.paragraphs[0], "AI for Science", 42, WHITE, bold=True, scale=False)
        p = tf.add_paragraph()
        add_runs(p, "2026년 지형도", 42, WHITE, bold=True, scale=False)
        p = tf.add_paragraph()
        p.space_before = Pt(12)
        add_runs(p, f"논문 리뷰 코퍼스 {self.ctx.total:,}편이 보여 주는", 17, RGBColor(0xDC, 0xE4, 0xEC))
        p = tf.add_paragraph()
        add_runs(p, f"{len(self.corpus['cats'])}개 지형과 검증으로의 전환", 17, RGBColor(0xDC, 0xE4, 0xEC))
        _, tf = textbox(s, M, Inches(5.0), Inches(6.6), Inches(1.0), inset=0.0)
        add_runs(tf.paragraphs[0], self.fill(NARRATIVE["cover"]["headline"]), 13, GOLD)
        _, tf = textbox(s, M, H - Inches(0.75), INNER_W, Inches(0.5), inset=0.0, anchor=MSO_ANCHOR.MIDDLE)
        add_runs(tf.paragraphs[0], f"과학기술정보통신부 보고용  |  {date.today().strftime('%Y년 %m월 %d일')}  |  "
                 f"paper-curation ai4s 코퍼스(리뷰 완료 전수) · 사례 {self.ctx.since}년 이후 우선",
                 10, RGBColor(0xB8, 0xC4, 0xD0))
        self._footer_no.append(len(self.prs.slides))
        self.footers.append((textbox(s, W - M - Inches(1.2), H - Inches(0.42), Inches(1.2), Inches(0.3), inset=0.0)[1],
                             RGBColor(0x08, 0x22, 0x3B)))
        self.notes(s, self.prose_notes("cover"))

    def s_summary(self):
        s = self.slide()
        self.chrome(s, "한눈에 보기", "핵심 요약", "숫자 넷 · 메시지 넷")
        self._num(s)
        ctx = self.ctx
        kw = (INNER_W - Inches(0.6)) / 4
        y = TOP + Inches(0.1)
        kpis = [(f"{ctx.total:,}편", "리뷰 완료 논문 전수", NAVY),
                (f"{len(self.corpus['cats'])}개", f"대분류 지형 · 서브카테고리 {ctx.n_subs}개", ACCENT),
                (f"{ctx.recent_share}%", f"{ctx.since}년 이후 논문 비중", GOLD),
                (f"{ctx.years.get(2026, 0):,}편", f"2026년 논문 · 전년 {ctx.years.get(2025, 0):,}편의 "
                 f"{ctx.years.get(2026, 0) / max(1, ctx.years.get(2025, 1)):.1f}배", RED)]
        for i, (num, label, color) in enumerate(kpis):
            self.kpi(s, M + i * (kw + Inches(0.2)), y, kw, Inches(1.45), num, label, color)
        y += Inches(1.75)
        msgs = [("지형", NARRATIVE["landscape"]["headline"]),
                ("서사", NARRATIVE["arc"]["headline"]),
                ("검증", NARRATIVE["verification"]["headline"]),
                ("제언", NARRATIVE["action"]["headline"])]
        row_h = Inches(0.78)
        for i, (tag, msg) in enumerate(msgs):
            yy = y + i * (row_h + Inches(0.1))
            rect(s, M, yy, Inches(1.0), row_h, NAVY)
            _, tf = textbox(s, M, yy, Inches(1.0), row_h, anchor=MSO_ANCHOR.MIDDLE, inset=0.0)
            tf.paragraphs[0].alignment = PP_ALIGN.CENTER
            add_runs(tf.paragraphs[0], tag, 13, WHITE, bold=True)
            _, tf = textbox(s, M + Inches(1.0), yy, INNER_W - Inches(1.0), row_h, anchor=MSO_ANCHOR.MIDDLE,
                            fill=PANEL, inset=0.2)
            add_runs(tf.paragraphs[0], self.fill(msg), 14, INK)
        self.notes(s, NARRATIVE["cover"]["sowhat"], self.prose_notes("arc"))

    def s_toc(self):
        s = self.slide()
        self.chrome(s, "목차", "발표 구성", "")
        self._num(s)
        parts = [("I", "코퍼스와 방법", "연도 분포 · 분류 방법 · 지형도 · 규모"),
                 ("II", "10개 지형", "대분류별 개요 · 대표 연구"),
                 ("III", "흐름과 신호", "관통 서사 · 수렴 · 부상/쇠퇴 · 공백"),
                 ("IV", "검증으로의 전환", "여섯 축 · 근거"),
                 ("V", "정책 제언", "행동 5 · 관전 포인트 12개월")]
        y = TOP + Inches(0.15)
        for i, (no, title, desc) in enumerate(parts):
            yy = y + i * Inches(0.98)
            rect(s, M, yy, Inches(0.9), Inches(0.8), NAVY if i < 4 else GOLD)
            _, tf = textbox(s, M, yy, Inches(0.9), Inches(0.8), anchor=MSO_ANCHOR.MIDDLE, inset=0.0)
            tf.paragraphs[0].alignment = PP_ALIGN.CENTER
            add_runs(tf.paragraphs[0], no, 20, WHITE, bold=True)
            _, tf = textbox(s, M + Inches(1.1), yy, INNER_W - Inches(1.1), Inches(0.8), anchor=MSO_ANCHOR.MIDDLE, inset=0.0)
            add_runs(tf.paragraphs[0], title, 18, NAVY, bold=True)
            p = tf.add_paragraph()
            add_runs(p, desc, 11, MUTED)
            rect(s, M + Inches(1.1), yy + Inches(0.86), INNER_W - Inches(1.1), Emu(9525), LINE)

    def divider(self, no, title, subtitle, items):
        s = self.slide()
        rect(s, 0, 0, W, H, NAVY)
        rect(s, 0, 0, Inches(0.35), H, GOLD)
        _, tf = textbox(s, Inches(1.0), Inches(1.5), Inches(3), Inches(1.6), inset=0.0)
        add_runs(tf.paragraphs[0], no, 72, GOLD, bold=True, scale=False)
        _, tf = textbox(s, Inches(1.0), Inches(3.2), Inches(11), Inches(1.0), inset=0.0)
        add_runs(tf.paragraphs[0], title, 36, WHITE, bold=True, scale=False)
        if subtitle:
            p = tf.add_paragraph()
            add_runs(p, subtitle, 16, RGBColor(0xB8, 0xC4, 0xD0))
        _, tf = textbox(s, Inches(1.0), Inches(4.6), Inches(11), Inches(2.2), inset=0.0)
        first = True
        for it in items:
            p = para(tf, first)
            first = False
            p.space_after = Pt(3)
            add_runs(p, "—  " + it, 12, RGBColor(0xDC, 0xE4, 0xEC))
        self._footer_no.append(len(self.prs.slides))
        self.footer(s, dark=True)
        self.toc.append((no, title))

    def s_corpus(self):
        s = self.slide()
        self.chrome(s, "I. 코퍼스와 방법", "코퍼스 연도 분포", self.fill(NARRATIVE["corpus"]["headline"]))
        self._num(s)
        years = self.ctx.years
        ys = [y for y in sorted(years) if y >= 2018]
        cw = INNER_W * 0.6
        self.bar_chart(s, M, TOP + Inches(0.05), cw, BOTTOM - TOP - Inches(0.1), [str(y) for y in ys],
                       [years[y] for y in ys], ACCENT, horizontal=False, size=11,
                       point_colors=[NAVY if y >= self.ctx.since else RGBColor(0xA9, 0xB8, 0xC9) for y in ys])
        x = M + cw + Inches(0.3)
        w = INNER_W - cw - Inches(0.3)
        _, tf = textbox(s, x, TOP + Inches(0.1), w, Inches(1.2), fill=PANEL, inset=0.18, anchor=MSO_ANCHOR.MIDDLE)
        add_runs(tf.paragraphs[0], f"{self.ctx.recent_share}%", 30, NAVY, bold=True)
        p = tf.add_paragraph()
        add_runs(p, f"{self.ctx.since}년 이후 논문 비중", 11, INK)
        _, tf = textbox(s, x, TOP + Inches(1.5), w, BOTTOM - TOP - Inches(1.6), inset=0.05)
        first = True
        for pt in NARRATIVE["corpus"].get("points", []):
            p = para(tf, first)
            first = False
            p.space_after = Pt(8)
            add_runs(p, "•  " + self.fill(pt), 11.5, INK)
        p = tf.add_paragraph()
        p.space_before = Pt(6)
        add_runs(p, "시사점  ", 10, ACCENT, bold=True)
        add_runs(p, self.fill(NARRATIVE["corpus"]["sowhat"]), 10.5, INK)
        self.notes(s, self.prose_notes("corpus"))

    def s_method(self):
        s = self.slide()
        self.chrome(s, "I. 코퍼스와 방법", "이 지도는 어떻게 만들어졌나", self.fill(NARRATIVE["method"]["headline"]))
        self._num(s)
        steps = [("전수 리뷰", f"{self.ctx.total:,}편 본문 정독 ·\n한국어 리뷰"),
                 ("의미 임베딩", "SPECTER2\n논문 특화 벡터"),
                 ("클러스터링", "UMAP 5차원 →\nHDBSCAN 밀도 군집"),
                 ("서브카테고리 명명", f"c-TF-IDF 키워드 →\n{self.ctx.n_subs}개 이름"),
                 ("대분류 그룹핑", f"{len(self.corpus['cats'])}개 지형 ·\n다중 배정(최대 3)"),
                 ("타임라인 분석", "기간·상태·대표 도구\n수렴/공백 신호")]
        n = len(steps)
        gap = Inches(0.18)
        bw = (INNER_W - gap * (n - 1)) / n
        y = TOP + Inches(0.3)
        for i, (t, d) in enumerate(steps):
            x = M + i * (bw + gap)
            shp = rect(s, x, y, bw, Inches(1.5), NAVY if i % 2 == 0 else ACCENT, shape_type=MSO_SHAPE.CHEVRON if i else MSO_SHAPE.PENTAGON)
            shp.adjustments[0] = 0.18
            _, tf = textbox(s, x + Inches(0.3), y + Inches(0.12), bw - Inches(0.6), Inches(1.3), anchor=MSO_ANCHOR.MIDDLE, inset=0.0)
            tf.paragraphs[0].alignment = PP_ALIGN.CENTER
            add_runs(tf.paragraphs[0], t, 12, WHITE, bold=True)
            p = tf.add_paragraph()
            p.alignment = PP_ALIGN.CENTER
            p.space_before = Pt(4)
            add_runs(p, d, 9.5, RGBColor(0xDC, 0xE4, 0xEC))
        y += Inches(1.85)
        half = (INNER_W - Inches(0.3)) / 2
        boxes = [("편수 기준 두 가지",
                  f"고유 배정(primary, 1편 = 1칸, 합 {self.ctx.total:,}편) · 중복 포함(all_categories, 합 {self.ctx.cards:,}편). "
                  "커버리지 산술은 고유 배정 기준"),
                 ("시기·상태·대표 도구",
                  "카테고리별 타임라인 분석(연도순 전환점) 기반. "
                  "상태 등급: 가속·안정·부상·감소")]
        for i, (t, d) in enumerate(boxes):
            self.card(s, M + i * (half + Inches(0.3)), y, half, Inches(1.35), t, d, color=NAVY, size=10.5)
        y += Inches(1.55)
        pts = [self.fill(p) for p in NARRATIVE["method"].get("points", [])]
        for i, pt in enumerate(pts[:2]):
            self.card(s, M + i * (half + Inches(0.3)), y, half, BOTTOM - y - Inches(0.05),
                      pt.split(":")[0] if ":" in pt[:12] else "한계", pt.split(":", 1)[1].strip() if ":" in pt[:12] else pt,
                      color=GOLD, size=10.5)
        self.notes(s, self.prose_notes("method"))

    def s_landscape_map(self):
        s = self.slide()
        self.chrome(s, "I. 코퍼스와 방법", f"{len(self.corpus['cats'])}개 지형 — 의미 지도",
                    "SPECTER2 임베딩의 UMAP 2차원 지도 · 점 = 논문 1편 · 색 = 고유 배정 대분류")
        self._num(s)
        png = render_landscape(self.topic, self.corpus["cats"], self.corpus["classification"],
                               CACHE / self.topic / "landscape.png", self.colors)
        fit_picture(s, png, M, TOP + Inches(0.02), INNER_W, BOTTOM - TOP - Inches(0.4), frame=False, pad=0)
        _, tf = textbox(s, M, BOTTOM - Inches(0.36), INNER_W, Inches(0.34), inset=0.0, anchor=MSO_ANCHOR.MIDDLE)
        add_runs(tf.paragraphs[0], "해석  ", 10, ACCENT, bold=True)
        add_runs(tf.paragraphs[0], "인접 = 내용 유사 · 경계가 번지는 곳(자율 AI 과학 발견 ↔ LLM 벤치마크) = III부 수렴 신호 · 라벨 = 대분류 중앙값", 10, MUTED)
        self.notes(s, self.prose_notes("landscape"))

    def s_landscape_sizes(self):
        s = self.slide()
        self.chrome(s, "I. 코퍼스와 방법", f"{len(self.corpus['cats'])}개 지형의 규모", self.fill(NARRATIVE["landscape"]["headline"]))
        self._num(s)
        cats = self.corpus["cats"]
        labels = [CATEGORY_KO.get(c["category"], c["category"]) for c in cats]
        cw = INNER_W * 0.56
        data = CategoryChartData()
        data.categories = labels
        data.add_series("고유 배정", [c.get("count", 0) for c in cats])
        data.add_series("중복 포함", [c.get("card_count", 0) for c in cats])
        gf = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, E(M), E(TOP + Inches(0.05)), E(cw), E(BOTTOM - TOP - Inches(0.1)), data)
        ch = gf.chart
        ch.has_legend = True
        ch.legend.position = XL_LEGEND_POSITION.BOTTOM
        ch.legend.include_in_layout = False
        ch.legend.font.size = Pt(round(10 * FS))
        ch.font.size = Pt(round(10 * FS))
        plot = ch.plots[0]
        plot.gap_width = 45
        plot.overlap = -10
        plot.has_data_labels = True
        plot.data_labels.font.size = Pt(round(9 * FS))
        plot.data_labels.number_format = "#,##0"
        plot.data_labels.number_format_is_linked = False
        plot.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
        for ser, col in zip(plot.series, (NAVY, RGBColor(0xA9, 0xB8, 0xC9))):
            ser.format.fill.solid()
            ser.format.fill.fore_color.rgb = col
        ch.value_axis.visible = False
        ch.value_axis.has_major_gridlines = False
        ch.value_axis.maximum_scale = max(c.get("card_count", 0) for c in cats) * 1.15
        ch.category_axis.reverse_order = True
        ch.category_axis.tick_labels.font.size = Pt(round(10 * FS))
        ch.category_axis.format.line.color.rgb = LINE
        x = M + cw + Inches(0.3)
        w = INNER_W - cw - Inches(0.3)
        _, tf = textbox(s, x, TOP + Inches(0.1), w, BOTTOM - TOP - Inches(0.2), inset=0.05)
        first = True
        for pt in NARRATIVE["landscape"].get("points", []):
            p = para(tf, first)
            first = False
            p.space_after = Pt(9)
            add_runs(p, "•  " + self.fill(pt), 11.5, INK)
        p = tf.add_paragraph()
        p.space_before = Pt(8)
        add_runs(p, "시사점  ", 10, ACCENT, bold=True)
        add_runs(p, self.fill(NARRATIVE["landscape"]["sowhat"]), 11, INK)
        self.notes(s, self.prose_notes("landscape"))

    # ── 대분류 ──
    def _cat_refs(self, cat, sub):
        """58장 덱과 같은 규칙으로 서브카테고리 대표 논문을 고른다(제목 호명 우선)."""
        analyses = self.corpus["analyses"]
        name = sub["name"]
        tl = B.match_timeline(analyses, cat["category"], name) or {}
        nar = self.ctx.fill_all(NARRATIVE.get(name, {}), cat=cat, sub=sub)
        tools = tl.get("representative_tools") or []
        kds = [re.sub(r"\s+", " ", k) for k in (tl.get("key_developments") or [])]
        points = nar.get("points") or kds
        named = [w for w in re.findall(r"[A-Za-z][A-Za-z0-9]*(?:[-–][A-Za-z0-9]+)*", " ".join(points))
                 if len(w) >= 4 and (sum(1 for ch in w if ch.isupper()) >= 2 or any(ch.isdigit() for ch in w))]
        probes = named + list(B._tokens(name)) + [w for k in kds for w in re.findall(r"[A-Z][A-Za-z0-9\-]{3,}", k)]
        pool = self.corpus["by_sub"].get((cat["category"], name), [])
        picked = B.pick_papers(pool, tools, probes, "", limit=8, since=self.ctx.since)
        by_slug = {p["slug"]: p for p in pool}
        body = " ".join(points)
        forced = [p for p in pool if B.title_phrase_hit(p, body)]
        ordered, seen = [], set()
        for p in forced + [by_slug[r["slug"]] for r in picked if r["slug"] in by_slug]:
            if p["slug"] in seen:
                continue
            seen.add(p["slug"])
            ordered.append(p)
        return ordered, points, tools, nar

    def _point_for(self, paper, points, tools):
        """논문을 호명한 불릿이 있으면 그 문장을 캡션으로 쓴다."""
        keys = B.ref_keys(paper, tools)
        for pt in points:
            if B.title_phrase_hit(paper, pt) or any(re.search(B._key_pattern(k), pt, re.I) for k in keys):
                return strip_year(pt)
        return ""

    def _cat_figures(self, cat, limit=4):
        """대분류의 도판 후보: 서브카테고리 순서대로, 서브카테고리당 1편 우선."""
        subs = sorted(cat.get("sub_themes", []), key=lambda s: -s.get("count", 0))[:self.ctx.per_category]
        rounds = []
        for sub in subs:
            ordered, points, tools, nar = self._cat_refs(cat, sub)
            cands = []
            for p in ordered:
                fig = good_figure(self.figs.get(p["slug"], []))
                if fig:
                    cands.append((p, fig, self._point_for(p, points, tools), sub, nar))
            rounds.append(cands)
        out, seen = [], set()
        # 1차: 서브카테고리마다 첫 후보, 2차: 남는 후보
        for depth in range(3):
            for cands in rounds:
                if depth < len(cands) and cands[depth][0]["slug"] not in seen:
                    seen.add(cands[depth][0]["slug"])
                    out.append(cands[depth])
                if len(out) >= limit:
                    return out
        return out

    def s_category_overview(self, i, cat):
        s = self.slide()
        name = cat["category"]
        ko = CATEGORY_KO.get(name, name)
        color = rgb(self.colors[name])
        subs = sorted(cat.get("sub_themes", []), key=lambda x: -x.get("count", 0))[:self.ctx.per_category]
        n_recent = sum(1 for p in self.corpus["papers"]
                       if self.corpus["assigned"].get(p["slug"], {}).get("primary_category") == name
                       and B.year_of(p.get("date")) >= self.ctx.since)
        self.chrome(s, f"II. 10개 지형  ·  제{i}부", ko, name, accent=color)
        self._num(s)
        # 우상단 통계 칩
        chips = [f"고유 배정 {cat.get('count', 0):,}편", f"중복 포함 {cat.get('card_count', 0):,}편",
                 f"서브카테고리 {len(cat.get('sub_themes', []))}개", f"{self.ctx.since}+ {round(n_recent / max(1, cat.get('count', 1)) * 100)}%"]
        cx = W - M
        for chip in reversed(chips):
            cw = Inches(0.12) * len(chip) + Inches(0.25)
            cx -= cw
            _, tf = textbox(s, cx, Inches(0.56), cw, Inches(0.3), anchor=MSO_ANCHOR.MIDDLE, fill=PANEL, inset=0.0, radius=True)
            tf.paragraphs[0].alignment = PP_ALIGN.CENTER
            add_runs(tf.paragraphs[0], chip, 9, NAVY, bold=True)
            cx -= Inches(0.08)
        # 좌: 리드 + 차트 + 헤드라인
        lw = INNER_W * 0.46
        y = TOP + Inches(0.08)
        rect(s, M, y, Inches(0.07), Inches(0.8), color)
        _, tf = textbox(s, M + Inches(0.15), y, lw - Inches(0.15), Inches(0.8), anchor=MSO_ANCHOR.MIDDLE, inset=0.04)
        add_runs(tf.paragraphs[0], self.fill(CATEGORY_LEAD.get(name, ""), cat=cat), 14, NAVY, bold=True)
        y += Inches(0.95)
        _, tf = textbox(s, M, y, lw, Inches(0.26), inset=0.0)
        add_runs(tf.paragraphs[0], f"상위 서브카테고리 {len(subs)}개 · 편수", 10, MUTED, bold=True)
        labels = []
        for st in subs:
            tl = B.match_timeline(self.corpus["analyses"], name, st["name"]) or {}
            status = B.STATUS_KO.get(tl.get("status"), "")
            labels.append((NARRATIVE.get(st["name"], {}).get("ko") or st["name"]) + (f" · {status}" if status else ""))
        ch_h = Inches(0.42) * len(subs) + Inches(0.3)
        self.bar_chart(s, M - Inches(0.05), y + Inches(0.22), lw + Inches(0.05), ch_h, labels, [st.get("count", 0) for st in subs], color, size=10)
        y += Inches(0.3) + ch_h
        _, tf = textbox(s, M, y, lw, BOTTOM - y, inset=0.02)
        first = True
        for st in subs[:3]:
            hd = (NARRATIVE.get(st["name"]) or {}).get("headline")
            if not hd:
                continue
            p = para(tf, first)
            first = False
            p.space_after = Pt(5)
            add_runs(p, f"**{(NARRATIVE[st['name']].get('ko') or st['name'])}**  ", 10.5, color)
            add_runs(p, self.fill(hd, cat=cat, sub=st), 10.5, INK)
        # 우: 대표 도판
        figs = self._cat_figures(cat, limit=4)
        self._cat_fig_cache = {name: figs}
        rx = M + lw + Inches(0.35)
        rw = INNER_W - lw - Inches(0.35)
        if figs:
            p, fig, point, sub, nar = figs[0]
            self.figure(s, p, fig, rx, TOP + Inches(0.08), rw, BOTTOM - TOP - Inches(0.1),
                        caption=point or nominalize(shorten(p.get("essence", ""), 120)),
                        sub_name=nar.get("ko") or sub["name"], cap_lines=3)
        notes = [self.fill(CATEGORY_LEAD.get(name, ""), cat=cat)]
        for st in subs:
            pr = PROSE.get(st["name"])
            if pr:
                notes.append(f"[{NARRATIVE[st['name']].get('ko', st['name'])}] " + self.ctx.fill(pr["lead"], cat=cat, sub=st))
        self.notes(s, *notes)

    def s_category_figures(self, i, cat):
        s = self.slide()
        name = cat["category"]
        ko = CATEGORY_KO.get(name, name)
        color = rgb(self.colors[name])
        self.chrome(s, f"II. 10개 지형  ·  제{i}부", f"{ko} — 대표 연구", f"{self.ctx.since}년 이후 사례 중심", accent=color)
        self._num(s)
        figs = self._cat_fig_cache.get(name) or self._cat_figures(cat, limit=4)
        figs = figs[1:4] if len(figs) > 3 else figs[-3:]
        n = max(1, len(figs))
        gap = Inches(0.3)
        fw = (INNER_W - gap * (n - 1)) / n
        y = TOP + Inches(0.08)
        fh = BOTTOM - y - Inches(0.8)
        for j, (p, fig, point, sub, nar) in enumerate(figs):
            x = M + j * (fw + gap)
            self.figure(s, p, fig, x, y, fw, fh, caption=nominalize(shorten(point or p.get("essence", ""), 105)),
                        sub_name=nar.get("ko") or sub["name"], cap_lines=3, title_size=10.5, cap_size=9)
        # 하단: 시사점 스트립 (편수 최대 서브카테고리의 sowhat)
        subs = sorted(cat.get("sub_themes", []), key=lambda x: -x.get("count", 0))[:self.ctx.per_category]
        sow = ""
        for st in subs:
            sow = (NARRATIVE.get(st["name"]) or {}).get("sowhat")
            if sow:
                sow = self.fill(sow, cat=cat, sub=st)
                break
        yy = BOTTOM - Inches(0.7)
        _, tf = textbox(s, M, yy, INNER_W, Inches(0.66), anchor=MSO_ANCHOR.MIDDLE, fill=PANEL, inset=0.18)
        add_runs(tf.paragraphs[0], "우리에게 무엇인가  ", 10.5, color, bold=True)
        add_runs(tf.paragraphs[0], sow, 11.5, INK)
        notes = []
        for st in subs:
            pr = PROSE.get(st["name"])
            if pr:
                notes.append(f"[{NARRATIVE[st['name']].get('ko', st['name'])}]\n" + "\n".join(self.ctx.fill(t, cat=cat, sub=st) for t in pr["body"]))
        self.notes(s, *notes)

    # ── III ──
    def s_arc(self):
        s = self.slide()
        nar = NARRATIVE["arc"]
        self.chrome(s, "III. 흐름과 신호", nar.get("title_ko") or "관통하는 한 줄", self.fill(nar["headline"]))
        self._num(s)
        pts = [self.fill(p) for p in nar.get("points", [])]
        n = len(pts)
        y_line = TOP + Inches(1.0)
        rect(s, M, y_line, INNER_W, Inches(0.05), LINE)
        gap = Inches(0.2)
        bw = (INNER_W - gap * (n - 1)) / n
        for i, pt in enumerate(pts):
            x = M + i * (bw + gap)
            m = re.match(r"^(배경:|\d{4}(?:[–-]\d{4})?)\s*(.*)$", pt)
            label, body = (m.group(1).rstrip(":"), m.group(2)) if m else ("", pt)
            col = NAVY if i < n - 2 else (ACCENT if i == n - 2 else RED)
            rect(s, x + bw / 2 - Inches(0.17), y_line - Inches(0.15), Inches(0.34), Inches(0.34), col, shape_type=MSO_SHAPE.OVAL)
            _, tf = textbox(s, x, TOP + Inches(0.15), bw, Inches(0.6), anchor=MSO_ANCHOR.BOTTOM, inset=0.0)
            tf.paragraphs[0].alignment = PP_ALIGN.CENTER
            add_runs(tf.paragraphs[0], label, 16, col, bold=True)
            _, tf = textbox(s, x, y_line + Inches(0.45), bw, BOTTOM - y_line - Inches(1.4), fill=WHITE, line=LINE, inset=0.14)
            add_runs(tf.paragraphs[0], body, 11, INK)
        _, tf = textbox(s, M, BOTTOM - Inches(0.75), INNER_W, Inches(0.7), anchor=MSO_ANCHOR.MIDDLE, fill=PANEL, inset=0.18)
        add_runs(tf.paragraphs[0], "시사점  ", 10.5, ACCENT, bold=True)
        add_runs(tf.paragraphs[0], self.fill(nar["sowhat"]), 11.5, INK)
        self.notes(s, self.prose_notes("arc"))

    def _insight_items(self, *types):
        return [it for it in (self.insights.get("cross_category") or []) if it.get("type") in types]

    def _evidence_figs(self, items, limit=2, exclude=()):
        out, seen = [], set(exclude)
        for it in items:
            for ev in it.get("evidence", []):
                p = self.corpus["by_prefix"].get(str(ev))
                if not p or p["slug"] in seen:
                    continue
                fig = good_figure(self.figs.get(p["slug"], []))
                if fig:
                    seen.add(p["slug"])
                    out.append((p, fig, it))
                    if len(out) >= limit:
                        return out
        return out

    def _insight_slide(self, section, title, headline, items, sowhat, notes_key, *, colors=None, extra_items=None):
        s = self.slide()
        self.chrome(s, section, title, self.fill(headline))
        self._num(s)
        figs = self._evidence_figs(items, limit=2)
        y = TOP + Inches(0.08)
        avail = BOTTOM - y - Inches(0.85)
        n = max(1, len(items))
        gap = Inches(0.2)
        top_h = avail * (0.52 if (figs or extra_items) else 1.0)
        cw = (INNER_W - gap * (n - 1)) / n
        budget = text_budget(cw, top_h - Inches(0.95))
        for k, it in enumerate(items):
            col = (colors or {}).get(it.get("type"), ACCENT)
            cats_ko = " × ".join(CATEGORY_KO.get(c, c) for c in it.get("categories", []))
            tag = {"convergence": "수렴", "emerging": "부상", "declining": "쇠퇴", "gap": "공백"}.get(it.get("type"), "")
            desc = ko_names(it.get("description", ""))
            pol = ko_names(it.get("policy_implication", "") or "")
            if pol and budget >= 240:
                body = nominalize(shorten(desc, budget - 120)) + "\n정책 함의 — " + nominalize(shorten(pol, 100))
            else:
                body = nominalize(shorten(desc, budget))
            self.card(s, M + k * (cw + gap), y, cw, top_h, f"{tag} · {it.get('title')}", body,
                      color=col, tag=cats_ko, size=10.5)
        y2 = y + top_h + Inches(0.18)
        bot_h = BOTTOM - Inches(0.85) - y2
        x = M
        if extra_items:
            label, lst = extra_items
            ew = INNER_W * (0.42 if figs else 1.0)
            per = max(45, text_budget(ew, bot_h - Inches(0.7)) // max(1, len(lst)) - 4)
            self.card(s, x, y2, ew, bot_h, label, "\n".join("•  " + nominalize(shorten(ko_names(v), per)) for v in lst),
                      color=GOLD, size=10.5)
            x += ew + Inches(0.25)
        if figs:
            fw = (W - M - x - Inches(0.25) * (len(figs) - 1)) / len(figs)
            for k, (p, fig, it) in enumerate(figs):
                self.figure(s, p, fig, x + k * (fw + Inches(0.25)), y2, fw, bot_h,
                            title=shorten(B.clean_title(p.get("title", "")), 48),
                            caption=nominalize(shorten(p.get("essence", ""), 85)), sub_name=it.get("title"),
                            cap_lines=2, title_size=9.5, cap_size=8.5)
        _, tf = textbox(s, M, BOTTOM - Inches(0.7), INNER_W, Inches(0.66), anchor=MSO_ANCHOR.MIDDLE, fill=PANEL, inset=0.18)
        add_runs(tf.paragraphs[0], "시사점  ", 10.5, ACCENT, bold=True)
        add_runs(tf.paragraphs[0], self.fill(sowhat), 11.5, INK)
        self.notes(s, self.prose_notes(notes_key))

    def s_convergence(self):
        items = self._insight_items("convergence")
        hot = (self.insights.get("meta") or {}).get("hot_combinations") or []
        extra = ("자주 결합되는 조합", [f"{CATEGORY_KO.get(h['pair'][0], h['pair'][0])} × {CATEGORY_KO.get(h['pair'][1], h['pair'][1])}: {h['description']}"
                                for h in hot[:3]]) if hot else None
        self._insight_slide("III. 흐름과 신호", "수렴 신호: 경계가 무너지는 곳", NARRATIVE["convergence"]["headline"], items,
                            NARRATIVE["convergence"]["sowhat"], "convergence", colors={"convergence": ACCENT}, extra_items=extra)

    def s_riseandfall(self):
        items = self._insight_items("emerging") + self._insight_items("declining")
        self._insight_slide("III. 흐름과 신호", "부상과 쇠퇴", NARRATIVE["riseandfall"]["headline"], items,
                            NARRATIVE["riseandfall"]["sowhat"], "riseandfall", colors={"emerging": GREEN, "declining": RED})

    def s_gaps(self):
        items = self._insight_items("gap")
        under = (self.insights.get("meta") or {}).get("underserved_domains") or []
        self._insight_slide("III. 흐름과 신호", "비어 있는 자리", NARRATIVE["gaps"]["headline"], items,
                            NARRATIVE["gaps"]["sowhat"], "gaps", colors={"gap": GOLD},
                            extra_items=("미개척 영역(코퍼스 메타 분석)", under[:4]) if under else None)

    # ── IV ──
    def s_verification(self):
        s = self.slide()
        nar = NARRATIVE["verification"]
        self.chrome(s, "IV. 검증으로의 전환", nar.get("title_ko") or "검증 전환의 축", self.fill(nar["headline"]))
        self._num(s)
        raw_pts = [self.ctx.fill(p) for p in nar.get("points", [])]   # S번호 유지
        pts = [strip_srefs(p, self.sub_ko_by_no) for p in raw_pts]
        cols = 3
        rows = (len(pts) + cols - 1) // cols
        gap = Inches(0.22)
        cw = (INNER_W - gap * (cols - 1)) / cols
        avail = BOTTOM - TOP - Inches(0.95)
        ch = (avail - gap * (rows - 1)) / rows
        for k, pt in enumerate(pts):
            m = re.match(r"^\*\*(.+?)\*\*\s*[—-]\s*(?:([^:]+):\s*)?(.*)$", pt)
            title, systems, body = (m.group(1), m.group(2) or "", m.group(3)) if m else (f"축 {k + 1}", "", pt)
            x = M + (k % cols) * (cw + gap)
            y = TOP + Inches(0.08) + (k // cols) * (ch + gap)
            self.card(s, x, y, cw, ch, title, body, color=NAVY, number=k + 1, tag=systems.strip(), size=12)
            related = [self.sub_ko_by_no[int(no)] for no in _SREF.findall(raw_pts[k]) if int(no) in self.sub_ko_by_no]
            if related:
                _, tf = textbox(s, x + Inches(0.18), y + ch - Inches(0.5), cw - Inches(0.36), Inches(0.42), inset=0.0,
                                anchor=MSO_ANCHOR.BOTTOM)
                add_runs(tf.paragraphs[0], "관련 지형  " + " · ".join(related), 8.5, ACCENT)
        _, tf = textbox(s, M, BOTTOM - Inches(0.75), INNER_W, Inches(0.7), anchor=MSO_ANCHOR.MIDDLE, fill=PANEL, inset=0.18)
        add_runs(tf.paragraphs[0], "시사점  ", 10.5, ACCENT, bold=True)
        add_runs(tf.paragraphs[0], self.fill(nar["sowhat"]), 11.5, INK)
        self.notes(s, self.prose_notes("verification"))

    def s_verification_evidence(self):
        s = self.slide()
        nar = NARRATIVE["verification"]
        self.chrome(s, "IV. 검증으로의 전환", "근거 — 검증 전환 대표 연구", "여섯 축의 대표 시스템")
        self._num(s)
        refs = B.refs_by_names(nar.get("refs") or [], self.corpus["papers"], "", self.ctx.since, limit=12)
        by_slug = {p["slug"]: p for p in self.corpus["papers"]}
        picked = []
        for r in refs:
            p = by_slug.get(r["slug"])
            fig = good_figure(self.figs.get(r["slug"], [])) if p else None
            if fig:
                picked.append((p, fig))
            if len(picked) >= 3:
                break
        pts = [self.fill(p) for p in nar.get("points", [])]
        n = max(1, len(picked))
        gap = Inches(0.3)
        fw = (INNER_W - gap * (n - 1)) / n
        y = TOP + Inches(0.08)
        for j, (p, fig) in enumerate(picked):
            cap = ""
            for pt in pts:
                if B.title_phrase_hit(p, pt) or any(re.search(B._key_pattern(k), pt, re.I) for k in B.ref_keys(p, [])):
                    m = re.match(r"^\*\*(.+?)\*\*\s*[—-]\s*(.*)$", pt)
                    cap = (f"[{m.group(1)}] " + m.group(2)) if m else pt
                    break
            self.figure(s, p, fig, M + j * (fw + gap), y, fw, BOTTOM - y - Inches(0.1),
                        caption=cap or nominalize(shorten(p.get("essence", ""), 120)), cap_lines=4, title_size=10.5, cap_size=9)
        self.notes(s, self.prose_notes("verification"))

    # ── V ──
    _ORDINALS = ["첫째", "둘째", "셋째", "넷째", "다섯째", "여섯째"]

    def _ordinal_segments(self):
        """ACTION_RATIONALE(브리핑 문체 5문단)에서 '첫째~다섯째' 근거와 '실행 순서' 문단을 뽑는다."""
        segs, order = {}, ""
        for para_text in ACTION_RATIONALE:
            t = self.fill(para_text).strip()
            if t.startswith("실행 순서"):
                order = re.sub(r"^실행 순서[^:：]*[:：]?\s*", "", t).strip()
                continue
            for i, w in enumerate(self._ORDINALS):
                m = re.match(r"^" + w + r"[는은]?\s*[:：,]?\s*(.*)$", t, re.S)
                if m:
                    segs.setdefault(i, m.group(1).strip())
                    break
        return segs, order

    def s_actions(self):
        s = self.slide()
        nar = NARRATIVE["action"]
        self.chrome(s, "V. 정책 제언", "그래서 무엇을 할 것인가", self.fill(nar["headline"]))
        self._num(s)
        raw_pts = [self.ctx.fill(p) for p in nar.get("points", [])]   # S번호 유지
        pts = [strip_srefs(p, self.sub_ko_by_no) for p in raw_pts]
        segs, order = self._ordinal_segments()

        def _toks(t):
            return {w for w in re.findall(r"[가-힣A-Za-z]{2,}", t)}

        # 줄글의 '첫째…다섯째' 순서가 불릿 순서와 다를 수 있어 어휘 겹침으로 짝을 맞춘다
        seg_for = {}
        for k, pt in enumerate(pts):
            best = max(segs.items(), key=lambda kv: len(_toks(kv[1]) & _toks(pt)), default=(None, ""))
            seg_for[k] = best[1] if best[0] is not None and len(_toks(best[1]) & _toks(pt)) >= 2 else segs.get(k, "")
        n = len(pts)
        gap = Inches(0.2)
        cw = (INNER_W - gap * (n - 1)) / n
        y = TOP + Inches(0.08)
        strip_h = Inches(0.95) if order else 0
        ch = BOTTOM - y - Inches(0.95) - strip_h - (Inches(0.15) if order else 0)
        for k, pt in enumerate(pts):
            m = re.match(r"^\*\*(.+?)\*\*\s*[—-]\s*(.*)$", pt)
            title, body = (m.group(1), m.group(2)) if m else (f"행동 {k + 1}", pt)
            related = [self.sub_ko_by_no[int(no)] for no in _SREF.findall(raw_pts[k]) if int(no) in self.sub_ko_by_no]
            x = M + k * (cw + gap)
            color = NAVY if k < n - 1 else GOLD
            by = self.card(s, x, y, cw, ch, title, body, color=color, number=k + 1, size=10.5)
            # 근거 문단(줄글) + 관련 서브카테고리
            ty = by + Pt(10.5 * FS) * 1.4 * text_lines(body, cw - Inches(0.36), 10.5) + Inches(0.16)
            seg = seg_for.get(k, "")
            # 첫 문장이 카드 제목을 되풀이하면('검증기 우선 투자.') 뺀다
            lead = re.match(r"^([^.]{2,18})\.\s*", seg)
            if lead and len(_toks(lead.group(1)) & _toks(title)) >= 1:
                seg = seg[lead.end():]
            if seg:
                _, tf = textbox(s, x + Inches(0.18), ty, cw - Inches(0.36), ch - (ty - y) - Inches(0.6), inset=0.0)
                add_runs(tf.paragraphs[0], "왜  ", 9, color, bold=True)
                add_runs(tf.paragraphs[0], shorten(seg, text_budget(cw, ch - (ty - y) - Inches(0.6), 9.5) - 4), 9.5, MUTED)
            if related:
                _, tf = textbox(s, x + Inches(0.18), y + ch - Inches(0.5), cw - Inches(0.36), Inches(0.42), inset=0.0,
                                anchor=MSO_ANCHOR.BOTTOM)
                add_runs(tf.paragraphs[0], "관련 지형  " + " · ".join(related), 8.5, ACCENT)
        if order:
            _, tf = textbox(s, M, y + ch + Inches(0.15), INNER_W, strip_h, anchor=MSO_ANCHOR.MIDDLE, fill=PANEL, inset=0.18)
            add_runs(tf.paragraphs[0], "실행 순서  ", 10.5, ACCENT, bold=True)
            add_runs(tf.paragraphs[0], order, 11, INK)
        _, tf = textbox(s, M, BOTTOM - Inches(0.8), INNER_W, Inches(0.75), anchor=MSO_ANCHOR.MIDDLE, fill=NAVY, inset=0.2)
        add_runs(tf.paragraphs[0], self.fill(nar["sowhat"]), 13, WHITE, bold=True)
        self.notes(s, self.prose_notes("action"))

    def s_watchlist(self):
        s = self.slide()
        nar = NARRATIVE["action"]
        self.chrome(s, "V. 정책 제언", "관전 포인트 — 다음 12개월", "다음 보고의 네 축")
        self._num(s)
        items = []
        for label, lst in (nar.get("extra") or {}).items():
            items = list(lst)
        n = max(1, len(items))
        y = TOP + Inches(0.15)
        rh = (BOTTOM - y - Inches(1.2) - Inches(0.14) * (n - 1)) / n
        for k, it in enumerate(items):
            yy = y + k * (rh + Inches(0.14))
            rect(s, M, yy, Inches(0.7), rh, ACCENT)
            _, tf = textbox(s, M, yy, Inches(0.7), rh, anchor=MSO_ANCHOR.MIDDLE, inset=0.0)
            tf.paragraphs[0].alignment = PP_ALIGN.CENTER
            add_runs(tf.paragraphs[0], f"Q{k + 1}", 16, WHITE, bold=True)
            _, tf = textbox(s, M + Inches(0.7), yy, INNER_W - Inches(0.7), rh, anchor=MSO_ANCHOR.MIDDLE, fill=PANEL, inset=0.22)
            add_runs(tf.paragraphs[0], self.fill(it), 14, INK)
        _, tf = textbox(s, M, BOTTOM - Inches(1.0), INNER_W, Inches(0.95), anchor=MSO_ANCHOR.MIDDLE, fill=NAVY, inset=0.25)
        add_runs(tf.paragraphs[0], "마무리  ", 11, GOLD, bold=True)
        add_runs(tf.paragraphs[0], self.fill(NARRATIVE["verification"]["sowhat"]), 13, WHITE)
        self.notes(s, self.prose_notes("action"))

    # ── 부록 ──
    def s_appendix_method(self):
        s = self.slide()
        self.chrome(s, "부록 A", "분류 방법 상세", "")
        self._num(s)
        half = (INNER_W - Inches(0.3)) / 2
        left = [("코퍼스", f"paper-curation ai4s 토픽 논문 {self.ctx.total:,}편 전수. 편마다 본문 정독 후 한국어 리뷰(핵심·성취·방법·독창성·한계) 작성. 도판 출처 = 각 리뷰"),
                ("임베딩·클러스터링", "SPECTER2(논문 특화 임베딩) → UMAP 5차원 → HDBSCAN 밀도 군집 → c-TF-IDF 키워드 → LLM 명명 → 대분류 그룹핑"),
                ("배정", "논문당 primary_category 1개 + all_categories 최대 3개. 집계는 '고유 배정'(primary) 과 '중복 포함'(all) 병기")]
        right = [("타임라인·상태", "대분류별 논문 연도순 전환점 서술 → 서브카테고리별 기간·상태(가속/안정/부상/감소)·대표 도구 추출"),
                 ("인사이트", "대분류 횡단 수렴·부상·쇠퇴·공백 신호와 미개척 영역은 별도 메타 분석 결과"),
                 ("한계", f"편수 = 관심의 밀도, 중요도 아님. 최신 편향({self.ctx.since}년 이후 {self.ctx.recent_share}%). 2026년 논문은 피인용 미축적 → 인용 순위 미사용")]
        for col, items in enumerate((left, right)):
            y = TOP + Inches(0.1)
            ch = (BOTTOM - y - Inches(0.3)) / 3
            for k, (t, d) in enumerate(items):
                self.card(s, M + col * (half + Inches(0.3)), y + k * (ch + Inches(0.15)), half, ch - Inches(0.05), t, d, color=NAVY, size=10.5)
        self.notes(s, self.prose_notes("method"))

    def s_appendix_table(self):
        s = self.slide()
        self.chrome(s, "부록 B", "지형 × 상위 서브카테고리", "고유 배정 편수 · 괄호 = 상태")
        self._num(s)
        cats = self.corpus["cats"]
        rows = []
        for c in cats:
            subs = sorted(c.get("sub_themes", []), key=lambda x: -x.get("count", 0))[:self.ctx.per_category]
            cells = []
            for st in subs:
                tl = B.match_timeline(self.corpus["analyses"], c["category"], st["name"]) or {}
                status = B.STATUS_KO.get(tl.get("status"), "")
                cells.append(f"{NARRATIVE.get(st['name'], {}).get('ko') or st['name']} {st.get('count', 0)}" + (f"({status})" if status else ""))
            rows.append([CATEGORY_KO.get(c["category"], c["category"]), f"{c.get('count', 0):,}", " · ".join(cells)])
        shape = s.shapes.add_table(len(rows) + 1, 3, E(M), E(TOP + Inches(0.1)), E(INNER_W), E(Inches(0.42) * (len(rows) + 1)))
        tbl = shape.table
        tbl_pr = tbl._tbl.tblPr
        tbl_pr.set("firstRow", "0")
        tbl_pr.set("bandRow", "0")
        sid = tbl_pr.find(qn("a:tableStyleId"))
        if sid is not None:
            sid.text = "{5940675A-B579-460E-94D1-54222C63F5DA}"
        widths = [Inches(2.6), Inches(1.0), INNER_W - Inches(3.6)]
        for j, col in enumerate(tbl.columns):
            col.width = E(widths[j])
        for j, h in enumerate(["대분류", "편수", "상위 서브카테고리 (편수·상태)"]):
            cell = tbl.cell(0, j)
            cell.text = ""
            cell.fill.solid()
            cell.fill.fore_color.rgb = NAVY
            add_runs(cell.text_frame.paragraphs[0], h, 10, WHITE, bold=True)
        for i, row in enumerate(rows, start=1):
            for j, v in enumerate(row):
                cell = tbl.cell(i, j)
                cell.text = ""
                cell.fill.solid()
                cell.fill.fore_color.rgb = WHITE if i % 2 else PANEL
                cell.margin_top = cell.margin_bottom = Inches(0.03)
                cell.vertical_anchor = MSO_ANCHOR.MIDDLE
                add_runs(cell.text_frame.paragraphs[0], v, 9 if j == 2 else 10, INK, bold=(j == 0))
        for r in tbl.rows:
            r.height = E(Inches(0.42))

    def s_appendix_sources(self):
        """도판 출처 목록 — 한 장에 안 들어가면 여러 장."""
        seen, items = set(), []
        for no, p, fig in self.sources:
            if (p["slug"], fig["n"]) in seen:
                continue
            seen.add((p["slug"], fig["n"]))
            items.append((no, p, fig))
        per = 30
        for start in range(0, len(items), per):
            s = self.slide()
            self.chrome(s, "부록 C", "도판 출처", "슬라이드 · 논문(리뷰 링크) · Figure · DOI/URL")
            self._num(s)
            chunk = items[start:start + per]
            half = (len(chunk) + 1) // 2
            colw = (INNER_W - Inches(0.3)) / 2
            for col in range(2):
                _, tf = textbox(s, M + col * (colw + Inches(0.3)), TOP + Inches(0.05), colw, BOTTOM - TOP - Inches(0.1), inset=0.02)
                first = True
                for no, p, fig in chunk[col * half:(col + 1) * half]:
                    para_ = para(tf, first)
                    first = False
                    para_.space_after = Pt(4)
                    r = para_.add_run()
                    r.text = f"S{no:02d}  "
                    _set_font(r, 8.5, True, False, ACCENT)
                    r = para_.add_run()
                    r.text = shorten(B.clean_title(p.get("title", "")), 58)
                    _set_font(r, 8.5, False, False, NAVY)
                    r.hyperlink.address = f"../../docs/papers/{p['slug']}/index.html"
                    label, url = self.links.get(p["slug"], ("", ""))
                    r = para_.add_run()
                    r.text = f"  Fig. {fig['n']}  "
                    _set_font(r, 8.5, False, False, MUTED)
                    if label:
                        r = para_.add_run()
                        r.text = label
                        _set_font(r, 8.5, False, False, LINK)
                        r.hyperlink.address = url


def build_brief(topic, per_category=5, since=2025):
    summaries, classification, timeline, insights, index = B.load_corpus(topic)
    corpus = B.prepare_corpus(summaries, classification, timeline, index, per_category, since)
    corpus["classification"] = classification
    corpus["assigned"] = {a["slug"]: a for a in classification.get("assignments", [])}
    figs = figure_index(corpus["papers"], PAPERS_DIR)
    colors = {c["category"]: PALETTE[i % len(PALETTE)] for i, c in enumerate(corpus["cats"])}
    sub_ko_by_no = {no: (NARRATIVE.get(name) or {}).get("ko", name) for name, no in corpus["ctx"].slide_no.items()}
    brief = Brief(topic, corpus, insights, figs, colors, sub_ko_by_no)
    prs = brief.build()
    return prs, brief


def main():
    ap = argparse.ArgumentParser(description="AI for Science 지형도 — 정책 브리핑 PPTX")
    ap.add_argument("--topic", default="ai4s")
    ap.add_argument("--per-category", type=int, default=5)
    ap.add_argument("--since", type=int, default=2025)
    ap.add_argument("--out-dir", default=None, help="출력 루트 (기본 reports/)")
    args = ap.parse_args()
    try:
        prs, brief = build_brief(args.topic, args.per_category, args.since)
    except B.TaxonomyMismatch as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 2
    root = Path(args.out_dir) if args.out_dir else REPORTS
    out = root / "build" / f"{args.topic}_brief_{len(prs.slides)}.pptx"
    out.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(out))
    n_figs = len({(p["slug"], f["n"]) for _, p, f in brief.sources})
    print(f"[OK] 브리핑 {len(prs.slides)}장 · 도판 {n_figs}장 · 발표자 노트 {sum(1 for s in prs.slides if s.has_notes_slide)}장")
    print(f"  PPTX : {out}")
    return 0


if __name__ == "__main__":
    from _env_guard import force_py312
    force_py312()
    sys.exit(main())
