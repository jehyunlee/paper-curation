"""citedby 리포트 렌더러 — 자기완결 HTML + print CSS (→ 브라우저 PDF 저장).

scisci 의 `lib/report_generator.py`(564줄, python-docx + KoPub 폰트)를 대체한다.
docx 를 만들지 않고 **HTML 한 장**을 낸다:

  * 로컬 웹앱 패널에서 그대로 읽고
  * [PDF 출력] 버튼 → `window.print()` → 브라우저 "PDF로 저장"

이 방식의 핵심 이점은 **링크가 살아있는 PDF** 다. 브라우저의 print-to-PDF 는
`<a href="...">` 를 PDF 링크 주석으로 그대로 보존한다. 그래서 이 모듈의 제1
불변식은 **모든 앵커의 href 가 절대 URL**이라는 것이다 — 상대경로는 PDF 안에서
클릭해도 열리지 않는다 (`_absolute_url` / `paper_url` 참조).

의존성 0 (stdlib 만). python-docx / openpyxl / 폰트 파일 불필요.
"""
from __future__ import annotations

import html
from datetime import datetime

# 5W1H 요약 필드 → 표시 라벨. topic_filter 의 요약 스키마와 맞춘다.
_SUMMARY_FIELDS = (
    ("what", "무엇을", "What"),
    ("how", "어떻게", "How"),
    ("result", "결과", "Result"),
    ("relevance", "관련성", "Relevance"),
)

_LABELS = {
    "ko": {
        "report_title": "인용논문 분석 보고서",
        "seed": "원논문",
        "topic": "주제",
        "generated": "생성",
        "count": "분석 논문",
        "unit": "편",
        "print": "PDF 출력",
        "print_hint": "인쇄 대화상자에서 '대상'을 'PDF로 저장'으로 선택하세요. "
                      "링크는 PDF 안에서도 클릭됩니다.",
        "overview": "개요",
        "papers": "논문별 분석",
        "appendix": "부록 — 전체 목록",
        "no_papers": "조건에 맞는 인용논문이 없습니다.",
        "originality": "독창성",
        "cited": "피인용",
        "source": "출처",
        "year": "연도",
        "title": "제목",
        "journal": "게재지",
        "link": "링크",
        "sources_label": "소스별 수집",
        "year_range": "연도 범위",
        "open": "원문",
        "open_pdf": "PDF 열기",
        "connected": "이어지는 논문",
        "suggest": "권장 컬렉션",
        "suggest_none": "미분류 (뚜렷이 맞는 컬렉션 없음)",
        "col_title": "컬렉션 배정 제안",
        "col_note": "citedby 로 등록한 논문은 컬렉션이 지정되지 않아 Unfiled 에 쌓인다. 기존 컬렉션 중에서만 제안하며, 확신이 없으면 비워 둔다 — 최종 판단은 직접 하시라.",
        "held": "보유",
        "ev_corpus": "리뷰완료",
        "ev_pdf": "전문",
        "ev_abstract": "초록",
        "ev_title": "제목만",
        "ev_note": "각 논문 옆 배지는 분석 근거의 범위다 — 전문(보유 PDF) > 초록 > 제목만.",
        "dr_title": "Deep Research — 보유 PDF 전문 기반",
        "dr_sub": "아래 논문들의 PDF 원문을 근거로 답합니다. 키는 서버 환경설정에서 읽으므로 입력할 필요가 없습니다.",
        "dr_ph": "예: 이 논문들이 공통으로 지적하는 한계는?",
        
        "dr_go": "질문",
        "exp_pdf": "🖨 PDF",
        "exp_md": "⬇ .md",
        "exp_obs": "📝 Obsidian",
        "exp_audio": "🎧 오디오",
        "dr_offline": "<b>로컬 서버로 열어야 합니다.</b> 터미널에서 <code>python pipeline/serve_local.py</code> 를 실행한 뒤 <code>http://localhost:8000/…</code> 로 이 리포트를 여세요. 검색 인덱스 로드와 쿼리 임베딩에 서버가 필요합니다.",
        "timeline": "인용 흐름 타임라인",
        "timeline_note": "주제 갈래가 언제 갈라지고 어디로 모였는지. 아래 표와 같은 데이터를 그림으로 옮긴 것이다.",
        "themes": "인용 주제 분포",
        "themes_note": "주제를 지정하지 않아 인용논문을 자동 군집화했다. 연도별 편수와 누적 피인용으로 각 갈래가 언제 얼마나 퍼졌는지 읽는다.",
        "zotero": "Zotero PDF",
        "zotero_item": "Zotero 서지정보",
        "zotero_col": "Zotero",
    },
    "en": {
        "report_title": "Citing Paper Analysis Report",
        "seed": "Source paper",
        "topic": "Topic",
        "generated": "Generated",
        "count": "Papers analyzed",
        "unit": "",
        "print": "Export PDF",
        "print_hint": "Choose 'Save as PDF' as the destination in the print dialog. "
                      "Links stay clickable inside the PDF.",
        "overview": "Overview",
        "papers": "Per-paper analysis",
        "appendix": "Appendix — full list",
        "no_papers": "No citing papers matched.",
        "originality": "Originality",
        "cited": "Citations",
        "source": "Source",
        "year": "Year",
        "title": "Title",
        "journal": "Journal",
        "link": "Link",
        "sources_label": "By source",
        "year_range": "Year range",
        "open": "Open",
        "zotero": "Zotero PDF",
        "zotero_item": "Zotero record",
        "zotero_col": "Zotero",
    },
}


def _esc(value) -> str:
    """HTML escape. None/NaN 은 빈 문자열."""
    if value is None:
        return ""
    s = str(value)
    if s.strip().lower() in ("nan", "none"):
        return ""
    return html.escape(s, quote=True)


# 링크로 내보낼 수 있는 스킴. `zotero://` 는 Zotero 데스크톱이 처리하는
# 프로토콜 핸들러로, 브라우저에서도 PDF 로 인쇄해도 링크 주석으로 보존된다.
_ALLOWED_SCHEMES = ("https://", "http://", "zotero://")


def _absolute_url(raw: str) -> str:
    """허용 스킴의 절대 URL 만 통과시킨다.

    PDF 안에서 클릭 가능하려면 스킴이 있는 절대 URL 이어야 한다. 상대경로는
    인쇄 시점의 문서 위치에 묶여 PDF 에서 열리지 않으므로 **버린다**
    (빈 문자열 → 호출부가 링크 대신 평문으로 렌더). `javascript:`/`file:` 등
    나머지 스킴도 같은 이유로 차단된다.
    """
    s = (raw or "").strip()
    if not s:
        return ""
    low = s.lower()
    if low.startswith(_ALLOWED_SCHEMES):
        return s
    return ""


def paper_url(paper: dict) -> str:
    """논문의 대표 외부 URL. DOI > arXiv > OA PDF 순.

    citing 논문은 코퍼스 밖 외부 논문이라 DOI/arXiv 가 정본 링크다.
    """
    doi = (paper.get("doi") or "").strip()
    if doi and doi.lower() not in ("nan", "none"):
        # 이미 URL 형태로 들어오는 경우도 흡수
        if doi.lower().startswith("http"):
            return _absolute_url(doi)
        return f"https://doi.org/{doi}"

    arxiv_id = (paper.get("arxiv_id") or "").strip()
    if arxiv_id and arxiv_id.lower() not in ("nan", "none"):
        return f"https://arxiv.org/abs/{arxiv_id}"

    return _absolute_url(paper.get("pdf_url") or "")


def _link(url: str, text: str, *, cls: str = "") -> str:
    """절대 URL 이면 <a>, 아니면 평문. PDF 링크 보존 불변식의 단일 집행 지점."""
    safe_url = _absolute_url(url)
    label = _esc(text)
    if not safe_url:
        return label
    attr = f' class="{cls}"' if cls else ""
    return f'<a href="{_esc(safe_url)}"{attr} rel="noopener">{label}</a>'


def _zotero_label(paper: dict, lbl: dict) -> str:
    """Zotero 링크 라벨 — PDF 를 여는지 서지정보를 여는지 명시한다.

    `_zotero_kind` 는 `build_report_html` 이 ZoteroIndex.url_kind() 로 채운다.
    """
    return lbl["zotero"] if paper.get("_zotero_kind") == "pdf" \
        else lbl["zotero_item"]


def _citation_line(paper: dict) -> str:
    """저자 · 게재지 · 연도 한 줄."""
    bits = []
    authors = (paper.get("author_names") or "").strip()
    if authors and authors.lower() != "nan":
        parts = [a.strip() for a in authors.split(";") if a.strip()]
        if len(parts) > 3:
            bits.append(f"{parts[0]} 외 {len(parts) - 1}인")
        elif parts:
            bits.append(", ".join(parts))
    journal = (paper.get("journal") or "").strip()
    if journal and journal.lower() != "nan":
        bits.append(f"<em>{_esc(journal)}</em>")
    year = paper.get("year")
    if year not in (None, "", 0) and str(year).lower() != "nan":
        bits.append(_esc(year))
    return " · ".join(b if b.startswith("<em>") else _esc(b) for b in bits)


def _summary_table(paper: dict, lbl: dict) -> str:
    """5W1H 요약 표. 요약이 없으면 빈 문자열."""
    summary = paper.get("summary")
    if not isinstance(summary, dict):
        return ""
    rows = []
    for key, ko_label, en_label in _SUMMARY_FIELDS:
        value = (summary.get(key) or "").strip()
        if not value:
            continue
        label = ko_label if lbl is _LABELS["ko"] else en_label
        rows.append(f'<tr><th>{_esc(label)}</th><td>{_esc(value)}</td></tr>')
    if not rows:
        return ""
    return '<table class="sum">' + "".join(rows) + "</table>"


def _stats_block(papers: list[dict], source_counts: dict | None, lbl: dict) -> str:
    years = [int(p["year"]) for p in papers
             if str(p.get("year") or "").isdigit()]
    chips = [f'<span class="chip">{_esc(lbl["count"])} '
             f'<b>{len(papers)}{_esc(lbl["unit"])}</b></span>']
    if years:
        chips.append(f'<span class="chip">{_esc(lbl["year_range"])} '
                     f'<b>{min(years)}–{max(years)}</b></span>')
    if source_counts:
        detail = ", ".join(f"{k} {v}" for k, v in sorted(source_counts.items())
                           if v)
        if detail:
            chips.append(f'<span class="chip">{_esc(lbl["sources_label"])} '
                         f'<b>{_esc(detail)}</b></span>')
    return '<div class="chips">' + "".join(chips) + "</div>"


def _seed_block(paper_info: dict | None, lbl: dict) -> str:
    if not paper_info:
        return ""
    title = (paper_info.get("title") or "").strip()
    url = paper_url(paper_info)
    linked = _link(url, title, cls="seed-t") if title else ""
    meta = _citation_line(paper_info)
    tail = []
    doi = (paper_info.get("doi") or "").strip()
    if doi and doi.lower() != "nan":
        tail.append(_link(paper_url(paper_info), doi))
    zotero_url = (paper_info.get("_zotero_url") or "").strip()
    if zotero_url:
        tail.append(_link(zotero_url, _zotero_label(paper_info, lbl), cls="zot"))
    doi_html = (f'<div class="seed-doi">{" · ".join(tail)}</div>'
                if tail else "")
    return (
        '<section class="seed">'
        f'<div class="seed-label">{_esc(lbl["seed"])}</div>'
        f'<div class="seed-title">{linked or _esc(title)}</div>'
        + (f'<div class="seed-meta">{meta}</div>' if meta else "")
        + doi_html
        + "</section>"
    )


def _audio_blocks(enabled: bool) -> tuple[str, str, str]:
    """Audio Overview (CSS, 모달, 스크립트). paper-curation 모듈을 그대로 쓴다 —
    대본 생성·Gemini TTS·mp3 인코딩·이메일 발송이 전부 거기 들어 있다."""
    if not enabled:
        return "", "", ""
    try:
        from lib.audio_overview import (get_audio_css, audio_modal_html,
                                        audio_script_block)
        from lib.citedby.deep_panel import AUDIO_PROVIDER_JS
    except Exception:  # noqa: BLE001 — 오디오는 부가 기능
        return "", "", ""
    import os
    key = (os.environ.get("GOOGLE_API_KEY")
           or os.environ.get("GEMINI_API_KEY") or "")
    css = get_audio_css("#D63423", "#a82a1c", "#fdecea")
    modal = audio_modal_html(
        "이 답변을 팟캐스트형 오디오로 만듭니다. "
        "(Gemini · 완성본은 이메일로도 전송)")
    script = audio_script_block(key, mode="deep",
                                provider_js=AUDIO_PROVIDER_JS)
    return css, modal, script


def _deep_css(index_file: str) -> str:
    """Deep Research 패널 CSS. 패널이 없으면 한 글자도 넣지 않는다."""
    if not index_file:
        return ""
    from .deep_panel import panel_css
    return panel_css()


def _deep_script(index_file: str, collection: str = "") -> str:
    if not index_file:
        return ""
    from .deep_panel import panel_script
    return panel_script(index_file, collection)


def _pdf_link(paper: dict, lbl: dict) -> str:
    """보유 PDF 바로열기 링크. PDF-first 모드의 핵심 동선이다."""
    attach = (paper.get("_library_attach") or "").strip()
    if attach:
        return _link(f"zotero://open-pdf/library/items/{attach}",
                     lbl["open_pdf"], cls="zot pdf")
    key = (paper.get("_library_key") or "").strip()
    if key:
        return _link(f"zotero://select/library/items/{key}",
                     lbl["zotero_item"], cls="zot")
    return (paper.get("_zotero_url") or "").strip() and _link(
        paper["_zotero_url"], _zotero_label(paper, lbl), cls="zot") or ""


def _paper_card(index: int, paper: dict, lbl: dict) -> str:
    title = (paper.get("title") or "").strip()
    url = paper_url(paper)
    head = _link(url, title) if url else _esc(title)

    meta_bits = [_citation_line(paper)]
    cited = paper.get("citationCount")
    if cited not in (None, "", 0) and str(cited).lower() != "nan":
        meta_bits.append(f'{_esc(lbl["cited"])} {_esc(cited)}')
    src = (paper.get("source") or "").strip()
    if src and src.lower() != "nan":
        meta_bits.append(_esc(src))
    meta = " · ".join(b for b in meta_bits if b)

    # PDF-first — 초록 대신 **원문 링크**가 본문 자리를 차지한다. 초록은 폐쇄형
    # 논문에서 못 받는 반면 보유 PDF 에는 전문이 있으므로, 읽을 사람을 원문으로
    # 곧장 보내는 게 낫다. 요약이 필요하면 5W1H 표가 그 자리를 대신한다.
    links = [_pdf_link(paper, lbl)]
    if url:
        links.append(_link(url, lbl["open"]))
    links_html = (f'<div class="open">{" · ".join(x for x in links if x)}</div>'
                  if any(links) else "")

    originality = (paper.get("originality") or "").strip()
    orig_html = ""
    if originality and originality.lower() != "nan":
        orig_html = (f'<div class="orig"><span class="orig-l">'
                     f'{_esc(lbl["originality"])}</span> {_esc(originality)}</div>')

    conns = paper.get("_connections") or []
    conn_html = ""
    if conns:
        items = " · ".join(
            f'{_esc(c.get("title", "")[:44])} <i>({_esc(c.get("relation", ""))})</i>'
            for c in conns[:4])
        conn_html = (f'<div class="conn"><span class="conn-l">'
                     f'{_esc(lbl["connected"])}</span> {items}</div>')

    sug = ""
    name = (paper.get("_suggest_collection") or "").strip()
    if name:
        conf = (paper.get("_suggest_confidence") or "").strip()
        reason = (paper.get("_suggest_reason") or "").strip()
        sug = (f'<div class="sug">{_esc(lbl["suggest"])}: '
               f'<span class="sug-n">{_esc(name)}</span>'
               + (f'<span class="sug-c">{_esc(conf)}</span>' if conf else "")
               + (f'<div class="sug-r">{_esc(reason)}</div>' if reason else "")
               + "</div>")

    ev = (paper.get("_evidence") or "").strip()
    badge = (f'<span class="ev ev-{ev}">{_esc(lbl.get("ev_" + ev, ev))}</span>'
             if ev else ("" if not paper.get("_library_attach")
                         else '<span class="held">PDF</span>'))
    return (
        '<article class="card">'
        f'<h3><span class="n">{index}</span> {head} {badge}</h3>'
        + (f'<div class="meta">{meta}</div>' if meta else "")
        + links_html
        + orig_html
        + conn_html
        + sug
        + _summary_table(paper, lbl)
        + "</article>"
    )


def _timeline_section(data_uri: str, lbl: dict, narrative: str = "",
                      overview: str = "") -> str:
    """타임라인 그림 + 그 그림을 만든 narrative.

    그림은 base64 data URI 라 파일을 옮겨도 PDF 로 뽑아도 살아 있다.
    narrative 는 LLM 이 인용 흐름을 읽고 쓴 본문 — 그림보다 정보량이 많으므로
    함께 싣는다. 그림이 실패해도 글만으로 절이 성립한다.
    """
    if not data_uri and not narrative and not overview:
        return ""
    out = [f'<h2>{lbl["timeline"]}</h2>']
    if data_uri:
        out.append(
            f'<figure class="tl"><img src="{data_uri}" alt="{_esc(lbl["timeline"])}">'
            f'<figcaption>{_esc(lbl["timeline_note"])}</figcaption></figure>')
    if overview:
        # 독자가 가장 먼저 읽는 줄글. 생성·소멸·분기·융합의 흐름을 문단으로
        # 풀어 쓴 것이라 스트림별 세부보다 앞에 둔다.
        paras = "".join(f"<p>{_esc(x.strip())}</p>"
                        for x in overview.split("\n\n") if x.strip())
        out.append(f'<div class="tl-over">{paras}</div>')
    if narrative:
        # 마크다운 변환은 agent_lecture_digest 의 것을 그대로 쓴다 —
        # 이스케이프·헤딩·굵게·링크를 이미 처리한다.
        try:
            from agent_lecture_digest import md_to_html as _md
            inner = _md(narrative)
        except Exception:  # noqa: BLE001 — 변환 실패해도 글은 보여준다
            inner = "".join(f"<p>{_esc(x.strip())}</p>"
                            for x in narrative.split("\n") if x.strip())
        out.append(f'<div class="tl-narr">{inner}</div>')
    return "".join(out)


def _collections_section(papers: list[dict], lbl: dict) -> str:
    """컬렉션별 제안 집계. 어디에 몇 편을 넣을지 한눈에 보고 결정한다."""
    from .collections import summarize
    rows = summarize(papers)
    if not rows or all(not r["name"] for r in rows):
        return ""

    body = []
    for r in rows:
        label = _esc(r["name"]) if r["name"] else f'<i>{_esc(lbl["suggest_none"])}</i>'
        sample = _esc(" · ".join(t[:38] for t in r["titles"][:2]))
        body.append(f'<tr><td>{label}</td><td class="num">{r["count"]}</td>'
                    f'<td class="dim">{sample}</td></tr>')
    return (
        f'<h2>{lbl["col_title"]}</h2>'
        f'<p class="note">{lbl["col_note"]}</p>'
        '<table class="cols"><thead><tr><th>컬렉션</th>'
        '<th class="num">편수</th><th>예시</th></tr></thead>'
        f'<tbody>{"".join(body)}</tbody></table>'
    )


def _themes_section(themes: dict, lbl: dict) -> str:
    """연도 × 군집 교차표 — "주제별로 얼마나 어떻게 흘러갔는지".

    이미지도 Opus narrative 도 만들지 않는다. year 와 피인용수가 이미 있으므로
    교차표만으로 확산 양상이 읽힌다.
    """
    if not themes or not themes.get("clusters"):
        return ""

    years = themes.get("years") or []
    total = themes.get("total") or 0
    n_cl = len(themes["clusters"])

    head = ["<th>주제</th>", "<th class='num'>편수</th>"]
    head += [f"<th class='num'>{y}</th>" for y in years]
    head.append("<th class='num'>누적 피인용</th>")

    rows = []
    for c in themes["clusters"]:
        cells = [f"<td><b>{_esc(c['name'])}</b>"
                 f"<div class='kw'>{_esc(', '.join(c['keywords']))}</div></td>",
                 f"<td class='num'>{c['count']}</td>"]
        for y in years:
            n = c["years"].get(y, 0)
            cells.append(f"<td class='num'>{n if n else '·'}</td>")
        cells.append(f"<td class='num'>{c['citations']:,}</td>")
        rows.append("<tr>" + "".join(cells) + "</tr>")

    if themes.get("outliers"):
        oy = themes.get("outlier_years") or {}
        cells = "".join(f"<td class='num'>{oy.get(y, 0) or '·'}</td>"
                        for y in years)
        rows.append(
            f"<tr class='muted'><td>미분류</td>"
            f"<td class='num'>{themes['outliers']}</td>{cells}"
            f"<td class='num'>{themes.get('outlier_citations', 0):,}</td></tr>")

    # 합계 행 — 각 열의 합이 전체와 맞는지 눈으로 검산된다.
    # (미분류 피인용을 버려 표 합이 실제와 3 어긋났던 적이 있다.)
    year_totals = {y: sum(c["years"].get(y, 0) for c in themes["clusters"])
                      + (themes.get("outlier_years") or {}).get(y, 0)
                   for y in years}
    total_cells = "".join(f"<td class='num'>{year_totals[y] or '·'}</td>"
                          for y in years)
    rows.append(
        f"<tr class='total'><td><b>합계</b></td>"
        f"<td class='num'><b>{total:,}</b></td>{total_cells}"
        f"<td class='num'><b>{themes.get('total_citations', 0):,}</b></td></tr>")

    return (
        f'<h2>{lbl["themes"]} <span class="dim">— {n_cl}개 갈래 / {total:,}편</span></h2>'
        f'<p class="note">{lbl["themes_note"]}</p>'
        f'<table class="themes"><thead><tr>{"".join(head)}</tr></thead>'
        f'<tbody>{"".join(rows)}</tbody></table>'
    )


def _appendix(papers: list[dict], lbl: dict) -> str:
    if not papers:
        return ""
    rows = []
    for i, p in enumerate(papers, 1):
        url = paper_url(p)
        title = (p.get("title") or "").strip()
        zot = (p.get("_zotero_url") or "").strip()
        zot_label = "PDF" if p.get("_zotero_kind") == "pdf" else "서지"
        rows.append(
            "<tr>"
            f'<td class="num">{i}</td>'
            f"<td>{_link(url, title) if url else _esc(title)}</td>"
            f'<td>{_esc(p.get("journal"))}</td>'
            f'<td class="num">{_esc(p.get("year"))}</td>'
            f'<td class="num">{_esc(p.get("citationCount"))}</td>'
            f'<td class="num">{_link(zot, zot_label, cls="zot") if zot else ""}</td>'
            "</tr>"
        )
    return (
        f'<section class="apx"><h2>{_esc(lbl["appendix"])}</h2>'
        "<table class=\"list\"><thead><tr>"
        f'<th class="num">#</th><th>{_esc(lbl["title"])}</th>'
        f'<th>{_esc(lbl["journal"])}</th>'
        f'<th class="num">{_esc(lbl["year"])}</th>'
        f'<th class="num">{_esc(lbl["cited"])}</th>'
        f'<th class="num">{_esc(lbl["zotero_col"])}</th>'
        "</tr></thead><tbody>" + "".join(rows) + "</tbody></table></section>"
    )


# print CSS 가 이 리포트의 본체다. 화면과 종이를 한 스타일시트로 처리한다.
_CSS = """
:root{--ink:#1f2430;--soft:#5b6478;--line:#e2e5ec;--accent:#D63423;--bg:#f6f7f9;}
*{box-sizing:border-box;}
body{margin:0;background:var(--bg);color:var(--ink);line-height:1.7;
 font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Apple SD Gothic Neo",
 "Noto Sans KR",Roboto,sans-serif;font-size:15px;word-break:keep-all;}
.wrap{max-width:900px;margin:0 auto;padding:2rem 1.5rem 4rem;background:#fff;}
.bar{display:flex;gap:.6rem;align-items:center;margin-bottom:1.4rem;}
.btn{font:inherit;font-size:.86rem;font-weight:600;cursor:pointer;border:1px solid var(--accent);
 background:var(--accent);color:#fff;border-radius:7px;padding:.45rem .95rem;}
.btn:hover{filter:brightness(1.08);}
.hint{font-size:.78rem;color:var(--soft);}
h1{font-size:1.5rem;margin:0 0 .3rem;letter-spacing:-.01em;}
.sub{color:var(--soft);font-size:.86rem;margin-bottom:1.5rem;}
.chips{display:flex;flex-wrap:wrap;gap:.45rem;margin:.9rem 0 1.6rem;}
.chip{background:#eef1f6;border:1px solid var(--line);border-radius:999px;
 padding:.24rem .7rem;font-size:.78rem;color:var(--soft);}
.chip b{color:var(--ink);}
.seed{border-left:3px solid var(--accent);background:#fbfbfc;padding:.8rem 1rem;
 margin:0 0 1.8rem;border-radius:0 8px 8px 0;}
.seed-label{font-size:.72rem;font-weight:700;color:var(--accent);letter-spacing:.04em;}
.seed-title{font-weight:700;margin:.2rem 0 .25rem;}
.seed-meta,.seed-doi{font-size:.83rem;color:var(--soft);}
h2{font-size:1.08rem;margin:2rem 0 .8rem;padding-bottom:.35rem;
 border-bottom:1px solid var(--line);}
.card{border:1px solid var(--line);border-radius:9px;padding:.9rem 1.05rem;
 margin:0 0 .9rem;background:#fff;}
.card h3{font-size:.98rem;margin:0 0 .3rem;font-weight:650;line-height:1.55;}
.card h3 .n{display:inline-block;min-width:1.6em;color:var(--accent);font-weight:800;}
.meta{font-size:.8rem;color:var(--soft);margin-bottom:.5rem;}
.orig{font-size:.86rem;margin:.45rem 0;}
.orig-l{font-size:.72rem;font-weight:700;color:var(--accent);margin-right:.35rem;}
table.sum{width:100%;border-collapse:collapse;margin:.55rem 0 .2rem;font-size:.85rem;}
table.sum th{width:5.2rem;text-align:left;vertical-align:top;background:#eef1f6;
 color:var(--soft);font-weight:600;padding:.35rem .55rem;border:1px solid var(--line);}
table.sum td{padding:.35rem .6rem;border:1px solid var(--line);vertical-align:top;}
table.themes{width:100%;border-collapse:collapse;margin:10px 0 18px;font-size:12.5px}
table.themes th,table.themes td{border:1px solid #e2e5ea;padding:5px 8px;text-align:left}
table.themes th{background:#f2f4f7;font-weight:600}
table.themes td.num,table.themes th.num{text-align:right;font-variant-numeric:tabular-nums}
table.themes tr.muted{color:#8a9099}
.sug{margin-top:6px;font-size:12.5px}
.sug-n{display:inline-block;background:#eef4ff;color:#1a4fa0;border:1px solid #cfe0fb;
 border-radius:5px;padding:1px 7px;font-weight:600}
.sug-c{font-size:11px;color:#8a9099;margin-left:5px}
.sug-r{color:var(--soft);margin-top:3px}
table.cols{width:100%;border-collapse:collapse;margin:10px 0 18px;font-size:13px}
table.cols th,table.cols td{border:1px solid #e2e5ea;padding:5px 9px;text-align:left}
table.cols th{background:#f2f4f7;font-weight:600}
table.cols td.num{text-align:right;font-variant-numeric:tabular-nums}
.held,.ev{font-size:10.5px;font-weight:700;border-radius:4px;padding:1px 5px;vertical-align:middle}
.held{color:#1f7a4d;background:#e6f5ec}
.ev-corpus{color:#5b21b6;background:#f0e9fd}
.ev-pdf{color:#1f7a4d;background:#e6f5ec}
.conn{margin-top:6px;font-size:12.5px;color:var(--soft)}
.conn-l{font-weight:600;color:var(--ink)}
.conn i{color:#7a8089;font-style:normal;font-size:11.5px}
.ev-abstract{color:#8a6d1f;background:#fbf3de}
.ev-title{color:#8a9099;background:#f0f1f3}
a.pdf{font-weight:600}
figure.tl-over{max-width:52rem;margin:1.2rem auto .4rem;font-size:1.05rem;line-height:1.9;color:#242a35}.tl-over p{margin:0 0 1.05rem}.tl-narr{max-width:52rem;margin:.6rem auto 0;line-height:1.75;color:#333}.tl-narr p{margin:0 0 .9rem}.tl{margin:14px 0 22px;padding:0}
figure.tl img{width:100%;height:auto;border:1px solid var(--line);border-radius:8px;display:block}
figure.tl figcaption{font-size:12px;color:var(--soft);margin-top:6px}
table.themes tr.total{background:#f7f8fa;border-top:2px solid #c8ccd2}
.kw{font-size:11px;color:#7a8089;margin-top:2px}
.dim{font-weight:400;color:#7a8089;font-size:13px}
.open{margin-top:.5rem;font-size:.8rem;}
a.zot{color:#8a3a1e;border:1px solid #e6cfc5;border-radius:5px;padding:.02rem .34rem;
 font-size:.92em;background:#fdf5f2;}
table.list{width:100%;border-collapse:collapse;font-size:.82rem;}
table.list th{background:#eef1f6;color:var(--soft);text-align:left;font-weight:600;}
table.list th,table.list td{padding:.4rem .55rem;border-bottom:1px solid var(--line);
 vertical-align:top;}
td.num,th.num{text-align:right;white-space:nowrap;}
a{color:#1257a8;text-decoration:none;}
a:hover{text-decoration:underline;}
.empty{color:var(--soft);padding:2rem 0;}
footer{margin-top:2.5rem;padding-top:.9rem;border-top:1px solid var(--line);
 font-size:.76rem;color:var(--soft);}

@page{size:A4;margin:16mm 14mm 18mm;}
@media print{
  /* 배경/강조색이 인쇄에서 날아가지 않게 (표 헤더·칩 가독성) */
  html,body{background:#fff;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
  .wrap{max-width:none;padding:0;}
  .no-print{display:none !important;}
  body{font-size:10.5pt;line-height:1.55;}
  h1{font-size:15pt;}
  h2{font-size:11.5pt;page-break-after:avoid;break-after:avoid;}
  /* 카드/표가 페이지 경계에서 잘리지 않게 */
  .card,.seed,table.sum tr,table.list tr{page-break-inside:avoid;break-inside:avoid;}
  .apx{page-break-before:auto;}
  /* 링크는 PDF 주석으로 보존되므로 URL 을 본문에 덧붙이지 않는다 */
  a{color:#0b4da2;text-decoration:none;}
}
"""

_PRINT_JS = (
    "<script>function citedbyPrint(){window.print();}</script>"
)


def build_report_html(*,
                      papers: list[dict],
                      paper_info: dict | None = None,
                      topic: str = "",
                      lang: str = "ko",
                      source_counts: dict | None = None,
                      zotero_index=None,
                      themes: dict | None = None,
                      timeline_uri: str = "",
                     timeline_narrative: str = "",
                     timeline_overview: str = "",
                      deep_index: str = "",
                      collection: str = "",
                      generated_at: datetime | None = None) -> str:
    """citedby 결과를 자기완결 HTML 리포트로 렌더한다.

    Args:
        papers: citing 논문 dict 목록. `summary` 키에 5W1H dict 가 있으면 표로 렌더.
        paper_info: 원논문(seed) 메타. 없으면 해당 블록 생략.
        topic: 주제 필터 문자열. 비어 있으면 표시 생략.
        lang: "ko" | "en".
        source_counts: `{source: 원시건수}` — 개요 칩에 표시.
        zotero_index: `zotero_links.ZoteroIndex`. 주면 내 Zotero 라이브러리에
            있는 논문에 `zotero://open-pdf/...` 링크를 붙인다. 로컬 전용
            산출물(`docs/_zotero_keys.json`)에 의존하므로 없으면 생략된다.
        generated_at: 생성 시각(테스트 고정용). 기본 now.

    Returns:
        외부 자원 의존이 없는 HTML 문자열. 파일로 저장해도 그대로 열린다.

    불변식:
        모든 `<a>` 의 href 는 절대 URL 이다. 상대경로는 PDF 안에서 클릭되지
        않으므로 링크 대신 평문으로 떨어진다 (`_absolute_url`).
    """
    lbl = _LABELS.get(lang) or _LABELS["ko"]
    papers = [dict(p) for p in (papers or [])]
    if zotero_index:
        # 내 라이브러리에 있는 논문만 Zotero 링크를 얻는다. 나머지는 외부 DOI.
        for p in papers:
            zurl = zotero_index.url(p)
            if zurl:
                p["_zotero_url"] = zurl
                p["_zotero_kind"] = zotero_index.url_kind(p)
        if paper_info:
            paper_info = dict(paper_info)
            zurl = zotero_index.url(paper_info)
            if zurl:
                paper_info["_zotero_url"] = zurl
                paper_info["_zotero_kind"] = zotero_index.url_kind(paper_info)
    from lib.dateutil import now_local
    ts = (generated_at or now_local()).strftime("%Y-%m-%d %H:%M")

    sub_bits = []
    if topic.strip():
        sub_bits.append(f'{_esc(lbl["topic"])}: <b>{_esc(topic)}</b>')
    sub_bits.append(f'{_esc(lbl["generated"])}: {_esc(ts)}')

    body = [
        '<div class="wrap">',
        '<div class="bar no-print">',
        f'<button type="button" class="btn" onclick="citedbyPrint()">'
        f'\U0001F5A8\uFE0F {_esc(lbl["print"])}</button>',
        f'<span class="hint">{_esc(lbl["print_hint"])}</span>',
        "</div>",
        f'<h1>{_esc(lbl["report_title"])}</h1>',
        f'<div class="sub">{" · ".join(sub_bits)}</div>',
        _seed_block(paper_info, lbl),
        f'<h2>{_esc(lbl["overview"])}</h2>',
        _stats_block(papers, source_counts, lbl),
    ]

    # 주제 분포는 개요 직후의 **독립 섹션**이다. 논문 목록 안에 두면 papers 가
    # 비었을 때 함께 사라지는데, 분포는 목록과 별개의 요약이라 그러면 안 된다.
    # Deep Research 는 주제 분포보다 먼저 — 독자가 먼저 묻고 싶어 하는 자리다.
    if deep_index:
        from .deep_panel import panel_html
        body.append(panel_html(deep_index, lbl))

    body.append(_timeline_section(timeline_uri, lbl, timeline_narrative,
                                  timeline_overview))

    if themes:
        body.append(_themes_section(themes, lbl))

    body.append(_collections_section(papers, lbl))

    if not papers:
        body.append(f'<div class="empty">{_esc(lbl["no_papers"])}</div>')
    else:
        body.append(f'<h2>{_esc(lbl["papers"])}</h2>')
        body.extend(_paper_card(i, p, lbl) for i, p in enumerate(papers, 1))
        body.append(_appendix(papers, lbl))

    body.append(
        f'<footer>paper-curation · citedby · {_esc(ts)}</footer>'
    )
    # Audio Overview 는 Deep Research 패널이 있을 때만 (답변이 있어야 의미가 있다)
    _audio_css, _audio_modal, _audio_script = _audio_blocks(bool(deep_index))

    body.append("</div>")

    return (
        '<!DOCTYPE html><html lang="' + ("ko" if lbl is _LABELS["ko"] else "en") +
        '"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        f'<title>{_esc(lbl["report_title"])}</title>'
        f"<style>{_CSS}{_deep_css(deep_index)}{_audio_css}</style>"
        f"{_PRINT_JS}</head><body>"
        + "".join(body) + _audio_modal + _deep_script(deep_index, collection)
        + _audio_script +
        "</body></html>"
    )


def papers_to_csv(papers: list[dict], columns: list[str] | None = None) -> str:
    """citing 논문 목록을 CSV 문자열로. stdlib 만 사용 (openpyxl 불필요).

    scisci 의 `excel_export.py`(271줄 + openpyxl)를 대체한다. 데이터 export 는
    CSV 로 충분하고 — Excel 에서 그대로 열린다 — 리포트는 HTML/PDF 가 담당한다.
    `url` 컬럼을 덧붙여 표 안에서도 원문으로 바로 갈 수 있게 한다.
    """
    import csv
    import io

    from .citing import CITING_COLUMNS

    cols = list(columns or CITING_COLUMNS)
    extra = [c for c in ("originality", "originality_category") if
             any(c in p for p in papers) and c not in cols]
    fields = cols + extra + ["url"]

    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=fields, extrasaction="ignore")
    writer.writeheader()
    for p in papers:
        row = {k: p.get(k, "") for k in fields}
        row["url"] = paper_url(p)
        writer.writerow(row)
    return buf.getvalue()
