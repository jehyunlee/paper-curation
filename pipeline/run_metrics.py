#!/usr/bin/env python3
"""코퍼스 논문의 피인용수·레퍼런스를 수집해 논문 디렉토리에 남긴다.

    docs/papers/{slug}/citations.md    피인용수 이력 + 인용논문 목록
    docs/papers/{slug}/references.md   이 논문이 인용한 논문 목록

기본은 **증분**이다 — `citations.md` 의 `updated` 가 30일 이상 지난 논문만
다시 조회한다. 매달 돌리면 이력이 쌓여 인용 속도가 남는다.

    # 갱신 대상만 (기본)
    PYTHONUTF8=1 python pipeline/run_metrics.py

    # 계획만 보기
    PYTHONUTF8=1 python pipeline/run_metrics.py --dry-run

    # 특정 슬러그 강제 갱신
    PYTHONUTF8=1 python pipeline/run_metrics.py --slugs 187,042 --force

소스 권위 (실측 근거):
    피인용수    Scopus(Search 등급) + Crossref + OpenAlex — 병합 없이 각자 보존
    citing     OpenAlex (Scopus REFEID 는 400 — entitlement 부족)
    references Crossref (Scopus view=REF 는 401)
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

PIPELINE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(PIPELINE_DIR))

DOCS_DIR = PIPELINE_DIR.parent / "docs"
PAPERS_DIR = DOCS_DIR / "papers"
INDEX_PATH = PAPERS_DIR / "_papers_index.json"


def _load_index() -> list[dict]:
    if not INDEX_PATH.exists():
        raise SystemExit(f"논문 인덱스를 찾을 수 없다: {INDEX_PATH}")
    data = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    papers = data if isinstance(data, list) else (data.get("papers") or [])
    return _fill_dois_from_db(papers)


def _fill_dois_from_db(papers: list[dict]) -> list[dict]:
    """Take the DOI the bibliography DB knows when the index has none.

    `build_papers_index.py` derives `doi` from review.md frontmatter alone,
    while the DB reconciles Zotero, Scopus, the PDF and the resolutions
    `resolve_missing_dois.py` recovered. The index therefore knew 1,404 DOIs
    against the DB's 2,071, and every source here is queried by DOI — so 667
    papers whose DOI was already known could never have their citations
    collected.
    """
    db = PIPELINE_DIR.parent / ".cache" / "bibliography.sqlite3"
    if not db.exists():
        return papers
    try:
        import sqlite3
        conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
        try:
            known = {slug: doi for slug, doi in conn.execute(
                "SELECT slug, doi FROM papers WHERE doi LIKE '10.%'")}
            arxiv_ids = {slug: aid for slug, aid in conn.execute(
                "SELECT slug, arxiv_id FROM papers WHERE arxiv_id != ''")}
        finally:
            conn.close()
    except Exception as exc:                      # DB is optional here
        print(f"  서지 DB DOI 조회 생략: {exc}", file=sys.stderr)
        return papers
    filled = preprints = 0
    for paper in papers:
        if (paper.get("doi") or "").strip().startswith("10."):
            continue
        slug = paper.get("slug", "")
        doi = known.get(slug)
        if doi:
            paper["doi"] = doi
            filled += 1
            continue
        # A preprint's arXiv DOI is not its bibliographic identity — that is
        # why `lib.doi.clean_doi` drops it — but it is a perfectly good key for
        # asking OpenAlex how often the preprint was cited, and a third of this
        # corpus never got published. 359 papers were already collected this
        # way before the index started normalising DOIs; without this they
        # would silently fall out of the refresh.
        arxiv = (arxiv_ids.get(slug) or "").strip()
        if arxiv:
            paper["doi"] = f"10.48550/arXiv.{arxiv}"
            preprints += 1
    if filled:
        print(f"  서지 DB 에서 DOI 보충 {filled:,}편")
    if preprints:
        print(f"  arXiv 프리프린트 DOI 로 보충 {preprints:,}편")
    return papers


def _select(papers: list[dict], args) -> list[dict]:
    """대상 논문을 고른다 — 슬러그 필터 → DOI 보유 → 갱신 주기."""
    from lib.metrics import needs_refresh

    if args.slugs:
        wanted = {s.strip() for s in args.slugs.split(",") if s.strip()}
        papers = [p for p in papers
                  if p.get("slug") in wanted
                  or any(p.get("slug", "").startswith(f"{w}_") for w in wanted)]

    # DOI 가 없으면 어느 소스도 조회할 수 없다.
    papers = [p for p in papers if (p.get("doi") or "").strip()]

    if args.force:
        return papers
    return [p for p in papers
            if needs_refresh(PAPERS_DIR / p["slug"], days=args.refresh_days)]


def main() -> int:
    ap = argparse.ArgumentParser(
        description="코퍼스 논문의 피인용수·레퍼런스 수집",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--slugs", default="", help="쉼표 구분 슬러그(접두 번호 허용)")
    ap.add_argument("--force", action="store_true", help="갱신 주기 무시")
    ap.add_argument("--refresh-days", type=int, default=30,
                    help="이 일수 이상 지난 논문만 갱신 (기본 30)")
    ap.add_argument("--min-citations", type=int, default=10,
                    help="이 값 이상일 때만 인용논문 목록 수집 (기본 10)")
    ap.add_argument("--no-references", action="store_true",
                    help="references.md 생성 생략")
    ap.add_argument("--no-citing", action="store_true",
                    help="인용논문 목록 수집 생략 (피인용수만)")
    ap.add_argument("--no-scopus", action="store_true",
                    help="Scopus 조회 생략")
    ap.add_argument("--limit", type=int, default=0, help="처리 편수 상한 (시험용)")
    ap.add_argument("--dry-run", action="store_true", help="계획만 출력")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    from lib.citedby import scopus as sc
    from lib.metrics import CitationSnapshot, write_citations, write_references
    from lib.metrics.collect import collect_many
    from lib.metrics.db import sync_metrics_database
    import datetime

    papers = _load_index()
    targets = _select(papers, args)
    if args.limit:
        targets = targets[:args.limit]

    use_scopus = not args.no_scopus
    if use_scopus:
        ok, why = sc.available()
        if not ok:
            print(f"  Scopus 건너뜀 — {why}")
            use_scopus = False
        elif not args.quiet:
            print(f"  Scopus 키: {sc.key_origin()}")

    print(f"코퍼스 {len(papers):,}편 · DOI 보유 중 갱신 대상 {len(targets):,}편"
          f" (주기 {args.refresh_days}일)")
    if args.dry_run:
        for p in targets[:20]:
            print(f"    {p['slug']}")
        if len(targets) > 20:
            print(f"    … 외 {len(targets) - 20:,}편")
        return 0
    if not targets:
        print("  갱신할 논문이 없다.")
        try:
            db_result = sync_metrics_database(
                [], datetime.date.today().isoformat())
            if not db_result.get("skipped"):
                print(f"  기존 citations.md 이력 {db_result['snapshots']:,}건 DB 동기화")
        except Exception as exc:
            print(f"  서지 DB 연동 실패: {exc}")
        return 0

    started = time.time()

    def on_progress(done, total):
        if not args.quiet and (done % 25 == 0 or done == total):
            print(f"  수집 {done:,}/{total:,}", flush=True)

    results = collect_many(
        targets, on_progress=on_progress,
        min_citations=args.min_citations, use_scopus=use_scopus,
        want_references=not args.no_references,
        want_citing=not args.no_citing)

    today = datetime.date.today().isoformat()
    wrote_c = wrote_r = with_citing = 0
    latest_by_slug: dict[str, dict] = {}

    for r in results:
        slug = r["slug"]
        pdir = PAPERS_DIR / slug
        if not pdir.exists():
            continue
        snap = CitationSnapshot(
            date=today, openalex=r["counts"]["openalex"],
            crossref=r["counts"]["crossref"], scopus=r["counts"]["scopus"],
            percentile=r["percentile"])
        write_citations(pdir, slug=slug, doi=r["doi"], title=r["title"],
                        snapshot=snap, citing=r["citing"],
                        citing_fetched=r["citing_fetched"],
                        min_citations=args.min_citations)
        wrote_c += 1
        if r["citing_fetched"]:
            with_citing += 1
        if r["references"]:
            write_references(pdir, slug=slug, doi=r["doi"], title=r["title"],
                             references=r["references"])
            wrote_r += 1

        best, src = snap.best()
        if best is not None:
            latest_by_slug[slug] = {
                "citation_count": best, "citations_source": src,
                "citations_asof": today, "citations_percentile": r["percentile"],
            }

    _update_index(latest_by_slug)
    try:
        db_result = sync_metrics_database(results, today)
        if db_result.get("skipped"):
            print(f"  서지 DB 연동 생략 — {db_result['reason']}")
        else:
            print(f"  서지 DB 이력 {db_result['snapshots']:,}건 · "
                  f"연도별 인용 {db_result['yearly']:,}건 갱신")
    except Exception as exc:
        # Metrics is a soft pipeline step; a DB synchronization failure must
        # not discard citations.md or abort the remaining curation pipeline.
        print(f"  서지 DB 연동 실패: {exc}")

    print(f"\n  citations.md {wrote_c:,}편 · references.md {wrote_r:,}편 · "
          f"인용목록 {with_citing:,}편 · {time.time() - started:.0f}초")
    print(f"  _papers_index.json 최신값 갱신 {len(latest_by_slug):,}편")
    return 0


def _update_index(latest: dict[str, dict]) -> None:
    """`_papers_index.json` 에 최신값 캐시를 반영 (원자적 쓰기).

    1차 저장소는 citations.md 다. 여기 두는 건 **조회용 사본** — 4,177개 md 를
    열어 파싱해야 정렬이 되는 상황을 피한다.
    """
    if not latest:
        return
    try:
        data = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"  인덱스 갱신 생략 (읽기 실패): {e}")
        return

    entries = data if isinstance(data, list) else (data.get("papers") or [])
    for e in entries:
        upd = latest.get(e.get("slug", ""))
        if upd:
            e.update(upd)

    tmp = INDEX_PATH.with_suffix(".json.tmp")
    try:
        tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2),
                       encoding="utf-8")
        tmp.replace(INDEX_PATH)
    except OSError as e:
        print(f"  인덱스 갱신 실패: {e}")
        tmp.unlink(missing_ok=True)


if __name__ == "__main__":
    try:
        import _env_guard
        _env_guard.force_py312()
    except ImportError:
        pass
    sys.exit(main())
