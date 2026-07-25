#!/usr/bin/env python3
"""citedby CLI — DOI 하나로 인용논문 분석 HTML 문서를 만든다.

산출물은 **자기완결 HTML 파일 한 장**이다. 브라우저로 열어 읽고, [PDF 출력]
버튼으로 인쇄하면 링크가 살아있는 PDF 가 나온다. 내 Zotero 라이브러리에 있는
논문은 제목 옆 [Zotero] 링크로 PDF 를 바로 열 수 있다.

    # 기본 — 인용논문 전체
    PYTHONUTF8=1 python pipeline/run_citedby.py --doi 10.1038/s41597-023-02198-9

    # 주제 필터 + 5W1H 요약
    PYTHONUTF8=1 python pipeline/run_citedby.py \\
        --doi 10.1038/s41597-023-02198-9 --topic "다른 분야간 융합연구"

    # 특정 논문 폴더 아래로 (paper-curio 브리지가 쓰는 형태)
    PYTHONUTF8=1 python pipeline/run_citedby.py --doi 10.1/x --slug 042_Some_Paper

    # 소스 제한 / LLM 없이 rule-based 만 / JSON 요약 출력
    PYTHONUTF8=1 python pipeline/run_citedby.py --doi 10.1/x \\
        --sources openalex,semanticscholar --no-llm-originality --json

기본 소스는 Scopus·WoS 포함 전체다. Scopus 는 pybliometrics.cfg + 기관 IP 가
있어야 결과가 나오고, WoS 는 Starter API 가 citing 쿼리를 지원하지 않아 항상
0건이다 (둘 다 실패해도 나머지 소스로 계속 진행한다).
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

PIPELINE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = PIPELINE_DIR.parent
DOCS_DIR = PROJECT_ROOT / "docs"
sys.path.insert(0, str(PIPELINE_DIR))


def _default_out_dir(slug: str) -> Path:
    """산출물 기본 위치. slug 가 있으면 그 논문 폴더 아래.

    `docs/papers/` 는 gitignore + .assetsignore 대상이라 저장소·배포를
    오염시키지 않는다.
    """
    if slug:
        return DOCS_DIR / "papers" / slug / "citedby"
    return DOCS_DIR / "citedby"


def _export_paper(paper: dict) -> dict:
    """Zotero 등록에 필요한 서지 필드만 추린 dict.

    citing 레코드는 내부 필드(`_zotero_url` 등)와 빈 컬럼이 많아 그대로
    내보내면 소비자가 지저분해진다. NaN/빈 값은 빈 문자열로 정규화한다.
    """
    def _s(key):
        v = paper.get(key)
        if v is None:
            return ""
        s = str(v).strip()
        return "" if s.lower() in ("nan", "none") else s

    return {
        "title": _s("title"),
        "doi": _s("doi"),
        "arxiv_id": _s("arxiv_id"),
        "url": _s("pdf_url"),
        "journal": _s("journal"),
        # 소스가 준 **완전한 날짜**(YYYY-MM-DD). Zotero 의 Date 필드로 그대로
        # 들어간다. year 는 date 가 없을 때의 폴백.
        "date": _s("date") or _s("year"),
        "year": _s("year"),
        "volume": _s("volume"),
        "issue": _s("issue"),
        "pages": _s("pages"),
        "issn": _s("issn"),
        "publisher": _s("publisher"),
        "language": _s("language"),
        "item_type": _s("item_type"),
        "authors": [a.strip() for a in _s("author_names").split(";") if a.strip()],
        "abstract": _s("abstract"),
        # 피인용수 — 소스마다 세는 우주가 달라 병합하지 않는다. 대표값에
        # 출처·시점을 붙여 내보내고, 소스별 원값도 함께 넘긴다.
        "citation_count": _s("citationCount"),
        "citation_source": _s("citations_source"),
        "citation_asof": _s("citations_asof"),
        "citation_percentile": _s("citations_percentile"),
        "citations_by_source": {
            src: paper.get(f"citations_{src}")
            for src in ("scopus", "crossref", "openalex", "s2")
            if paper.get(f"citations_{src}") is not None
            and str(paper.get(f"citations_{src}")).strip() not in ("", "nan")
        },
        "source": _s("source"),
        "originality": _s("originality"),
        "topic_reason": _s("topic_reason"),
    }


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="DOI → 인용논문 분석 HTML 문서 (+ CSV)",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--doi", required=True, help="분석할 논문의 DOI")
    p.add_argument("--topic", default="",
                   help="주제 필터 (비우면 인용논문 전체, 요약 생략)")
    p.add_argument("--sources", default="",
                   help="쉼표 구분 소스 목록 (기본: scopus,wos,openalex,"
                        "semanticscholar,arxiv)")
    p.add_argument("--lang", default="ko", choices=["ko", "en"],
                   help="리포트 언어 (기본 ko)")
    p.add_argument("--slug", default="",
                   help="논문 슬러그 — docs/papers/{slug}/citedby/ 에 저장")
    p.add_argument("--out", default="",
                   help="출력 디렉토리 직접 지정 (--slug 보다 우선)")
    p.add_argument("--max-per-source", type=int, default=5000,
                   help="소스당 최대 수집 건수 (기본 5000)")
    p.add_argument("--no-llm-originality", action="store_true",
                   help="독창성 추출을 rule-based 로만 (LLM 호출 0)")
    p.add_argument("--no-zotero-links", action="store_true",
                   help="Zotero PDF 링크를 붙이지 않는다")
    p.add_argument("--json", dest="as_json", action="store_true",
                   help="사람이 읽는 진행 로그 대신 결과 JSON 한 줄만 출력")
    p.add_argument("--quiet", action="store_true", help="진행 로그 억제")
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)

    sources = [s.strip() for s in args.sources.split(",") if s.strip()] or None
    out_dir = Path(args.out) if args.out else _default_out_dir(args.slug)

    def on_event(phase, message, current=0, total=0):
        if args.quiet or args.as_json:
            return
        bar = f" [{current}/{total}]" if total else ""
        print(f"  {phase:16} {message}{bar}", flush=True)

    from lib.citedby import run_citedby

    try:
        result = run_citedby(
            args.doi, sources=sources, topic=args.topic, lang=args.lang,
            max_results_per_source=args.max_per_source,
            use_llm_originality=not args.no_llm_originality,
            on_event=on_event)
    except Exception as e:  # noqa: BLE001 — CLI 경계
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    # --no-zotero-links 는 리포트를 다시 렌더해 링크를 뺀다 (run_citedby 는
    # 기본으로 붙인다). 재수집·재필터링은 없다.
    if args.no_zotero_links:
        from lib.citedby import build_report_html
        result["report_html"] = build_report_html(
            papers=result["papers"], paper_info=result["paper_info"],
            topic=result["topic"], lang=args.lang,
            source_counts=result["source_counts"])

    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%y%m%d_%H%M")
    report_path = out_dir / f"report_{stamp}.html"
    report_path.write_text(result["report_html"], encoding="utf-8")

    csv_path = None
    if result.get("csv"):
        csv_path = out_dir / f"citing_{stamp}.csv"
        csv_path.write_text(result["csv"], encoding="utf-8")

    # 논문 목록 JSON — Zotero 일괄 등록(paper-curio) 처럼 후속 소비자가
    # CSV 를 파싱하지 않고 바로 읽을 수 있게 서지 필드만 추려 낸다.
    papers_path = None
    if result.get("papers"):
        papers_path = out_dir / f"papers_{stamp}.json"
        papers_path.write_text(json.dumps(
            [_export_paper(p) for p in result["papers"]],
            ensure_ascii=False), encoding="utf-8")

    payload = {
        "ok": True,
        "doi": result["doi"],
        "topic": result["topic"],
        "matched": result["matched"],
        "total": result["total"],
        "elapsed_sec": result["elapsed_sec"],
        "source_counts": result["source_counts"],
        "report": str(report_path),
        "csv": str(csv_path) if csv_path else "",
        "papers_json": str(papers_path) if papers_path else "",
    }

    if args.as_json:
        print(json.dumps(payload, ensure_ascii=False))
    elif not args.quiet:
        print()
        print(f"  인용논문 {result['total']}편 → 리포트 {result['matched']}편"
              f" ({result['elapsed_sec']}초)")
        print(f"  리포트: {report_path}")
        if csv_path:
            print(f"  CSV   : {csv_path}")
        print(f"  브라우저로 열어 [PDF 출력] 버튼을 누르면 링크가 살아있는 "
              f"PDF 가 나옵니다.")
    return 0


if __name__ == "__main__":
    from _env_guard import force_py312
    force_py312()
    raise SystemExit(main())
