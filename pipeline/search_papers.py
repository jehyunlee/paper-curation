"""
search_papers.py - 다중 소스에서 학술 논문 검색

arXiv, Semantic Scholar, OpenAlex를 순차적으로 검색하여
중복 제거 및 관련성 점수 필터링 후 JSON으로 저장.

사용법:
    PYTHONUTF8=1 python search_papers.py --topic scisci --days 7
    PYTHONUTF8=1 python search_papers.py --topic ai4s --days 1 --max-papers 50
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

from config_loader import get_unpaywall_email, get_search_keywords, _ssl_ctx
from lib.categories import CATEGORIES_BY_TOPIC

# ---------------------------------------------------------------------------
# 검색 키워드 정의
# ---------------------------------------------------------------------------
# 키워드는 config_loader.get_search_keywords(topic) 가 제공한다 (config.json 의
# "search_keywords".<topic> 우선, 없으면 빌트인 ai4s/scisci 기본값 폴백).

# ---------------------------------------------------------------------------
# 관련성 점수 계산
# ---------------------------------------------------------------------------

def score_relevance(paper: dict, primary_keywords: list, secondary_keywords: list) -> float:
    """제목 + 초록에서 키워드 매칭으로 관련성 점수 계산 (0.0 ~ 1.0)."""
    text = (paper.get("title", "") + " " + paper.get("abstract", "")).lower()
    score = 0.0
    for kw in primary_keywords:
        if kw.lower() in text:
            score += 0.5
    for kw in secondary_keywords:
        if kw.lower() in text:
            score += 0.2
    return min(score, 1.0)


# ---------------------------------------------------------------------------
# 하이브리드(키워드 + 의미) 관련성 (env SEARCH_RELEVANCE_MODE 로 토글)
# ---------------------------------------------------------------------------
# SEARCH_RELEVANCE_MODE=keyword 면 기존 순수 substring 키워드 점수만 쓴다(바이트
# 동일). 기본값 hybrid 면 키워드 점수 + Haiku 의미 점수를 blend 해서, 키워드가
# 못 잡는 동의어/약어 논문을 살리고(RESCUE) 키워드만 걸린 무관 논문을 떨군다(DROP).
# 어떤 단계든 실패하면(키 없음/네트워크/파싱) 경고를 찍고 키워드-only 로 폴백한다.

def _relevance_mode():
    return (os.environ.get("SEARCH_RELEVANCE_MODE", "hybrid") or "hybrid").strip().lower()


def _build_topic_description(topic, primary_kws, secondary_kws):
    """검색 키워드로부터 토픽 설명 문장 구성 (의미 채점 프롬프트용)."""
    return (
        f"Research topic '{topic}'. "
        f"Core themes: {', '.join(primary_kws) or '(unspecified)'}. "
        f"Related concepts: {', '.join(secondary_kws) or '(none)'}."
    )


def _make_anthropic_client():
    """LLM 클라이언트 생성 (OpenRouter 우선). 키 없거나 실패하면 None (→ 키워드 폴백)."""
    try:
        from lib.llm_client import try_chat_client
        client = try_chat_client(timeout=180.0, max_retries=4)
        if client is None:
            print("  경고: OPENROUTER_API_KEY/ANTHROPIC_API_KEY 없음 — hybrid relevance 건너뜀 (keyword 폴백)",
                  file=sys.stderr)
            return None
        return client
    except Exception as e:
        print(f"  경고: LLM 클라이언트 생성 실패: {str(e)[:80]} (keyword 폴백)",
              file=sys.stderr)
        return None


def _score_keyword_only(papers, primary_kws, secondary_kws):
    """기존 키워드 점수만 부여 (keyword 모드 / 폴백 경로). 바이트 동일 동작."""
    for p in papers:
        p["relevance_score"] = round(score_relevance(p, primary_kws, secondary_kws), 3)


def _score_hybrid(papers, topic, primary_kws, secondary_kws, *, client=None,
                  cache_dir=None):
    """키워드 + 의미 점수를 blend 해 relevance_score 부여.

    성공하면 True (점수 세팅 완료), 의미 신호를 전혀 못 얻으면 False (→ 호출부가
    키워드-only 로 폴백). 의미 채점이 일부만 성공하면 누락 paper 는 키워드 점수로
    채워 부분 결과를 살린다.
    """
    from lib.relevance import expand_keywords, semantic_relevance, combined_score

    if client is None:
        client = _make_anthropic_client()
    if client is None:
        return False

    # (1) 키워드 확장(선택) — 동의어/약어를 secondary 로 추가해 substring recall 보강.
    try:
        extra = expand_keywords(topic, primary_kws, secondary_kws, client,
                                cache_dir=cache_dir)
    except Exception as e:
        print(f"  경고: keyword 확장 실패: {str(e)[:80]}", file=sys.stderr)
        extra = []
    if extra:
        print(f"  키워드 확장: +{len(extra)}개 동의어/약어", file=sys.stderr)
    secondary_aug = list(secondary_kws) + extra

    # (2) 의미 채점 (배치 Haiku) — papers index → 0~1 점수.
    topic_desc = _build_topic_description(topic, primary_kws, secondary_kws)
    sem = semantic_relevance(papers, topic_desc, client)
    if not sem:
        # 전부 실패 → 키워드-only 폴백 신호.
        return False

    # (3) blend. 의미 점수 없는 paper(누락 index)는 키워드 점수 그대로(combined None).
    for i, p in enumerate(papers):
        kw = score_relevance(p, primary_kws, secondary_aug)
        p["relevance_score"] = round(combined_score(kw, sem.get(i)), 3)
    print(f"  hybrid relevance: {len(sem)}/{len(papers)}편 의미 채점 반영", file=sys.stderr)
    return True


# ---------------------------------------------------------------------------
# arXiv 검색
# ---------------------------------------------------------------------------

def search_arxiv(keywords: list, since_date: str, max_per_keyword: int = 100,
                 until_date: str = "") -> list:
    """arXiv API로 논문 검색. since_date / until_date: 'YYYY-MM-DD' 형식.
    until_date 비어있으면 상한 없음 (오늘까지)."""
    results = []
    ns = "http://www.w3.org/2005/Atom"

    # arXiv API guideline: identifiable User-Agent + contact email. Anonymous
    # urllib defaults trigger aggressive throttling.
    contact_email = get_unpaywall_email() or "noreply@example.com"
    arxiv_headers = {
        "User-Agent": f"paper-curation/1.0 (mailto:{contact_email})",
        "From": contact_email,
    }

    for kw in keywords:
        query = urllib.parse.quote(f"all:{kw}")
        url = (
            f"https://export.arxiv.org/api/query"
            f"?search_query={query}"
            f"&start=0"
            f"&max_results={max_per_keyword}"
            f"&sortBy=submittedDate"
            f"&sortOrder=descending"
        )
        try:
            req = urllib.request.Request(url, headers=arxiv_headers)
            with urllib.request.urlopen(req, timeout=30, context=_ssl_ctx) as resp:
                xml_data = resp.read()
            root = ET.fromstring(xml_data)
            for entry in root.findall(f"{{{ns}}}entry"):
                # arxiv ID
                id_elem = entry.find(f"{{{ns}}}id")
                raw_id = id_elem.text.strip() if id_elem is not None else ""
                arxiv_id = raw_id.split("/abs/")[-1] if "/abs/" in raw_id else raw_id

                # 제목
                title_elem = entry.find(f"{{{ns}}}title")
                title = title_elem.text.strip().replace("\n", " ") if title_elem is not None else ""

                # 초록
                summary_elem = entry.find(f"{{{ns}}}summary")
                abstract = summary_elem.text.strip().replace("\n", " ") if summary_elem is not None else ""

                # 저자
                authors = [
                    a.find(f"{{{ns}}}name").text.strip()
                    for a in entry.findall(f"{{{ns}}}author")
                    if a.find(f"{{{ns}}}name") is not None
                ]

                # 날짜
                published_elem = entry.find(f"{{{ns}}}published")
                published_raw = published_elem.text.strip() if published_elem is not None else ""
                date = published_raw[:10] if published_raw else ""

                # 날짜 필터
                if date < since_date:
                    continue
                if until_date and date >= until_date:
                    continue

                # PDF URL
                pdf_url = ""
                for link in entry.findall(f"{{{ns}}}link"):
                    if link.get("title") == "pdf":
                        pdf_url = link.get("href", "")
                        break

                results.append({
                    "title": title,
                    "authors": authors,
                    "abstract": abstract,
                    "date": date,
                    "doi": "",
                    "arxiv_id": arxiv_id,
                    "pdf_url": pdf_url,
                    "source": "arxiv",
                    "relevance_score": 0.0,
                })
        except Exception as e:
            print(f"  경고: arXiv 검색 실패 (키워드: '{kw}'): {e}", file=sys.stderr)

        time.sleep(3)  # arXiv 요청 간격 준수

    return results


# ---------------------------------------------------------------------------
# Semantic Scholar 검색
# ---------------------------------------------------------------------------

def search_semantic_scholar(keywords: list, year: int, max_per_keyword: int = 100) -> list:
    """Semantic Scholar API로 논문 검색. year: 검색 연도."""
    results = []
    fields = "title,abstract,authors,externalIds,year,openAccessPdf,url"

    for kw in keywords:
        query = urllib.parse.quote(kw)
        url = (
            f"https://api.semanticscholar.org/graph/v1/paper/search"
            f"?query={query}"
            f"&year={year}"
            f"&limit={max_per_keyword}"
            f"&fields={fields}"
        )
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "PaperCuration/1.0"},
            )
            with urllib.request.urlopen(req, timeout=30, context=_ssl_ctx) as resp:
                data = json.load(resp)

            for paper in data.get("data", []):
                title = paper.get("title", "") or ""
                abstract = paper.get("abstract", "") or ""
                authors = [
                    a.get("name", "") for a in paper.get("authors", [])
                ]

                ext_ids = paper.get("externalIds", {}) or {}
                doi = ext_ids.get("DOI", "")
                arxiv_id = ext_ids.get("ArXiv", "")

                oa_pdf = paper.get("openAccessPdf") or {}
                pdf_url = oa_pdf.get("url", "") if isinstance(oa_pdf, dict) else ""

                pub_year = paper.get("year")
                date = str(pub_year) if pub_year else ""

                results.append({
                    "title": title,
                    "authors": authors,
                    "abstract": abstract,
                    "date": date,
                    "doi": doi,
                    "arxiv_id": arxiv_id,
                    "pdf_url": pdf_url,
                    "source": "semantic_scholar",
                    "relevance_score": 0.0,
                })
        except urllib.error.HTTPError as e:
            print(f"  경고: Semantic Scholar HTTP 오류 (키워드: '{kw}'): {e.code}", file=sys.stderr)
        except Exception as e:
            print(f"  경고: Semantic Scholar 검색 실패 (키워드: '{kw}'): {e}", file=sys.stderr)

        time.sleep(1)  # 1 req/sec 제한

    return results


# ---------------------------------------------------------------------------
# OpenAlex 검색
# ---------------------------------------------------------------------------

def search_openalex(keywords: list, since_date: str, email: str, max_per_keyword: int = 100,
                    until_date: str = "") -> list:
    """OpenAlex API로 논문 검색. until_date 비어있으면 상한 없음."""
    results = []

    for kw in keywords:
        query = urllib.parse.quote(kw)
        date_filter = f"from_publication_date:{since_date}"
        if until_date:
            date_filter += f",to_publication_date:{until_date}"
        # 정렬을 OpenAlex 기본(relevance_score:desc) 으로 둠. publication_date:desc 정렬은
        # 좁은 윈도우 + to_publication_date 조합 시 결과가 상한 일자에 몰려 윈도우 내 다른 날짜
        # paper 가 누락된다.
        params = (
            f"search={query}"
            f"&filter={date_filter}"
            f"&per_page={max_per_keyword}"
        )
        if email:
            params += f"&mailto={urllib.parse.quote(email)}"
        url = f"https://api.openalex.org/works?{params}"

        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "PaperCuration/1.0"},
            )
            with urllib.request.urlopen(req, timeout=30, context=_ssl_ctx) as resp:
                data = json.load(resp)

            for work in data.get("results", []):
                title = work.get("title", "") or ""

                # 초록 재구성 (inverted index)
                abstract = ""
                inv_index = work.get("abstract_inverted_index")
                if inv_index:
                    word_positions = []
                    for word, positions in inv_index.items():
                        for pos in positions:
                            word_positions.append((pos, word))
                    word_positions.sort(key=lambda x: x[0])
                    abstract = " ".join(w for _, w in word_positions)

                # 저자
                authors = []
                for authorship in work.get("authorships", []):
                    author = authorship.get("author", {}) or {}
                    name = author.get("display_name", "")
                    if name:
                        authors.append(name)

                # DOI
                doi_raw = work.get("doi", "") or ""
                doi = doi_raw.replace("https://doi.org/", "").replace("http://doi.org/", "")

                # arXiv ID (best_oa_location 또는 locations에서 추출)
                arxiv_id = ""
                best_oa = work.get("best_oa_location") or {}
                oa_url = best_oa.get("url", "") or ""
                if "arxiv.org" in oa_url:
                    arxiv_id = oa_url.split("/abs/")[-1].split("/pdf/")[-1].rstrip(".pdf")

                # PDF URL
                pdf_url = best_oa.get("pdf_url", "") or ""

                # 날짜
                date = work.get("publication_date", "") or ""

                # OpenAlex 의 to_publication_date 는 inclusive 라 until 도 포함됨.
                # 우리는 [since, until) 반-개 구간을 의도하므로 결과에서 한 번 더 거른다.
                if until_date and date and date >= until_date:
                    continue

                results.append({
                    "title": title,
                    "authors": authors,
                    "abstract": abstract,
                    "date": date,
                    "doi": doi,
                    "arxiv_id": arxiv_id,
                    "pdf_url": pdf_url,
                    "source": "openalex",
                    "relevance_score": 0.0,
                })
        except urllib.error.HTTPError as e:
            print(f"  경고: OpenAlex HTTP 오류 (키워드: '{kw}'): {e.code}", file=sys.stderr)
        except Exception as e:
            print(f"  경고: OpenAlex 검색 실패 (키워드: '{kw}'): {e}", file=sys.stderr)

        time.sleep(0.5)

    return results


# ---------------------------------------------------------------------------
# 중복 제거
# ---------------------------------------------------------------------------

def _normalize_title(title: str) -> str:
    """제목 정규화: 소문자, 구두점 제거."""
    return re.sub(r"[^a-z0-9 ]", "", title.lower()).strip()


def deduplicate(papers: list) -> list:
    """DOI 정확 일치 → 제목 앞 50자 퍼지 매칭으로 중복 제거.
    메타데이터가 가장 많은 항목을 유지."""
    def meta_count(p):
        return sum(1 for v in p.values() if v)

    # DOI 기준 그룹화
    doi_groups: dict[str, list] = {}
    no_doi = []
    for p in papers:
        doi = (p.get("doi") or "").strip()
        if doi:
            doi_groups.setdefault(doi, []).append(p)
        else:
            no_doi.append(p)

    # DOI 그룹에서 베스트 선택
    deduped = []
    for doi, group in doi_groups.items():
        best = max(group, key=meta_count)
        deduped.append(best)

    # 나머지: 제목 앞 50자로 퍼지 매칭
    seen_title_prefixes: dict[str, int] = {}  # prefix → index in deduped
    for p in no_doi:
        norm = _normalize_title(p.get("title", ""))
        prefix = norm[:50]
        if prefix and prefix in seen_title_prefixes:
            idx = seen_title_prefixes[prefix]
            if meta_count(p) > meta_count(deduped[idx]):
                deduped[idx] = p
        else:
            if prefix:
                seen_title_prefixes[prefix] = len(deduped)
            deduped.append(p)

    return deduped


# ---------------------------------------------------------------------------
# 메인
# ---------------------------------------------------------------------------

def _run_search(topic, *, days=7, max_papers=100, threshold=0.3,
                skip_arxiv=False, since=None, until=None, output=None):
    """Programmatic entrypoint for search_papers."""
    # config.json 의 search_keywords.<topic> 우선, 없으면 빌트인 ai4s/scisci 폴백.
    # 알 수 없는 토픽이면 추가할 JSON 블록을 안내하는 ValueError 발생.
    kw_config = get_search_keywords(topic)
    since = since or ""
    until = until or ""

    now = datetime.now(timezone.utc)
    if since:
        since_date = since
        since_dt = datetime.fromisoformat(since_date).replace(tzinfo=timezone.utc)
    else:
        since_dt = now - timedelta(days=days)
        since_date = since_dt.strftime("%Y-%m-%d")
    until_date = until
    since_year = since_dt.year

    if output:
        output_path = Path(output)
    else:
        from config_loader import get_topic_dir
        output_dir = get_topic_dir(topic)
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / "_search_results.json"

    primary_kws = kw_config["primary"]
    secondary_kws = kw_config["secondary"]
    all_keywords = primary_kws + secondary_kws

    try:
        email = get_unpaywall_email()
    except Exception:
        email = ""

    window_desc = f"[{since_date}, {until_date or 'today'})"
    print(f"\n논문 검색 시작: {topic} (윈도우 {window_desc})")
    print(f"  키워드: {len(primary_kws)}개 주요 + {len(secondary_kws)}개 보조")

    if skip_arxiv:
        print("\n[1/3] arXiv 검색 건너뛰기 (--skip-arxiv)")
        arxiv_papers = []
    else:
        print("\n[1/3] arXiv 검색 중...")
        arxiv_papers = search_arxiv(all_keywords, since_date, max_per_keyword=100, until_date=until_date)
        print(f"  arXiv: {len(arxiv_papers)}건 수집")

    print("\n[2/3] Semantic Scholar 검색 중...")
    ss_papers = search_semantic_scholar(all_keywords, since_year, max_per_keyword=100)
    print(f"  Semantic Scholar: {len(ss_papers)}건 수집")

    print("\n[3/3] OpenAlex 검색 중...")
    oa_papers = search_openalex(all_keywords, since_date, email, max_per_keyword=100, until_date=until_date)
    print(f"  OpenAlex: {len(oa_papers)}건 수집")

    all_papers = arxiv_papers + ss_papers + oa_papers
    unique_papers = deduplicate(all_papers)
    print(f"\n중복 제거 후: {len(unique_papers)}건 고유 논문")

    mode = _relevance_mode()
    scored = False
    if mode == "hybrid":
        print("\n관련성 채점: hybrid (키워드 + Haiku 의미)")
        try:
            scored = _score_hybrid(unique_papers, topic, primary_kws, secondary_kws,
                                   cache_dir=output_path.parent)
        except Exception as e:
            print(f"  경고: hybrid relevance 실패, keyword 폴백: {str(e)[:120]}",
                  file=sys.stderr)
            scored = False
        if not scored:
            print("  → keyword-only 폴백")
    if not scored:
        _score_keyword_only(unique_papers, primary_kws, secondary_kws)

    filtered = [p for p in unique_papers if p["relevance_score"] >= threshold]
    filtered.sort(key=lambda p: p["relevance_score"], reverse=True)
    filtered = filtered[:max_papers]
    print(f"필터링 후 (≥{threshold}): {len(filtered)}건")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(filtered, f, ensure_ascii=False, indent=2)

    print(f"\n검색 완료: {topic} ({days}일)")
    print(f"  arXiv: {len(arxiv_papers)}건")
    print(f"  Semantic Scholar: {len(ss_papers)}건")
    print(f"  OpenAlex: {len(oa_papers)}건")
    print(f"  중복 제거 후: {len(unique_papers)}건 고유")
    print(f"  필터링 후 (≥{threshold}): {len(filtered)}건")
    print(f"  출력: {output_path}")
    return {"output": str(output_path), "filtered": filtered,
            "arxiv": len(arxiv_papers), "s2": len(ss_papers),
            "openalex": len(oa_papers), "unique": len(unique_papers)}


def main():
    parser = argparse.ArgumentParser(description="다중 소스 학술 논문 검색")
    parser.add_argument("--topic", required=True,
                        help="검색 주제 (예: ai4s, scisci). config.json 의 "
                             "search_keywords 에 정의되었거나 빌트인 기본값이 있는 토픽.")
    parser.add_argument("--days", type=int, default=7, help="검색 기간(일, 기본: 7). --since/--until 사용 시 무시.")
    parser.add_argument("--since", default="", help="시작일 YYYY-MM-DD (포함). --days보다 우선.")
    parser.add_argument("--until", default="", help="종료일 YYYY-MM-DD (제외, 즉 [since, until)). 비우면 오늘까지.")
    parser.add_argument("--max-papers", type=int, default=100, help="최대 결과 수 (기본: 100)")
    parser.add_argument("--threshold", type=float, default=0.3, help="관련성 점수 임계값 (기본: 0.3)")
    parser.add_argument("--output", default="", help="출력 JSON 경로 (기본: {topic}/_search_results.json)")
    parser.add_argument("--skip-arxiv", action="store_true",
                        help="arXiv 검색 건너뛰기. 한국 IP 에서 chronic 429/timeout 시 시간 절약 (~8분/호출). "
                             "OpenAlex+Semantic Scholar 만으로도 보통 충분히 broad coverage.")
    args = parser.parse_args()
    _run_search(topic=args.topic, days=args.days, max_papers=args.max_papers,
                threshold=args.threshold, skip_arxiv=args.skip_arxiv,
                since=args.since, until=args.until, output=args.output)


if __name__ == "__main__":
    main()
