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
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

from config_loader import get_unpaywall_email, _ssl_ctx
from lib.categories import CATEGORIES_BY_TOPIC

# ---------------------------------------------------------------------------
# 검색 키워드 정의
# ---------------------------------------------------------------------------

SEARCH_KEYWORDS = {
    "ai4s": {
        "primary": [
            "AI for science",
            "machine learning science",
            "scientific discovery AI",
            "neural network physics",
            "deep learning chemistry",
            "AI drug discovery",
            "scientific foundation model",
            "AI materials",
        ],
        "secondary": [
            "molecular dynamics",
            "protein structure",
            "weather prediction",
            "quantum chemistry",
            "scientific NLP",
            "research automation",
        ],
    },
    "scisci": {
        "primary": [
            "science of science",
            "bibliometrics",
            "scientometrics",
            "research evaluation",
            "citation analysis",
            "scientific collaboration",
        ],
        "secondary": [
            "h-index",
            "research impact",
            "academic careers",
            "peer review",
            "research funding",
            "open access",
            "reproducibility",
        ],
    },
}

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
# arXiv 검색
# ---------------------------------------------------------------------------

def search_arxiv(keywords: list, since_date: str, max_per_keyword: int = 100) -> list:
    """arXiv API로 논문 검색. since_date: 'YYYY-MM-DD' 형식."""
    results = []
    ns = "http://www.w3.org/2005/Atom"

    for kw in keywords:
        query = urllib.parse.quote(f"all:{kw}")
        url = (
            f"http://export.arxiv.org/api/query"
            f"?search_query={query}"
            f"&start=0"
            f"&max_results={max_per_keyword}"
            f"&sortBy=submittedDate"
            f"&sortOrder=descending"
        )
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "PaperCuration/1.0"})
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

def search_openalex(keywords: list, since_date: str, email: str, max_per_keyword: int = 100) -> list:
    """OpenAlex API로 논문 검색."""
    results = []

    for kw in keywords:
        query = urllib.parse.quote(kw)
        params = (
            f"search={query}"
            f"&filter=from_publication_date:{since_date}"
            f"&per_page={max_per_keyword}"
            f"&sort=publication_date:desc"
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

def main():
    parser = argparse.ArgumentParser(description="다중 소스 학술 논문 검색")
    parser.add_argument("--topic", required=True, choices=list(SEARCH_KEYWORDS.keys()),
                        help="검색 주제 (ai4s 또는 scisci)")
    parser.add_argument("--days", type=int, default=7, help="검색 기간(일, 기본: 7)")
    parser.add_argument("--max-papers", type=int, default=100, help="최대 결과 수 (기본: 100)")
    parser.add_argument("--threshold", type=float, default=0.3, help="관련성 점수 임계값 (기본: 0.3)")
    parser.add_argument("--output", default="", help="출력 JSON 경로 (기본: {topic}/_search_results.json)")
    args = parser.parse_args()

    topic = args.topic
    days = args.days
    max_papers = args.max_papers
    threshold = args.threshold

    # 날짜 계산
    now = datetime.now(timezone.utc)
    since_dt = now - timedelta(days=days)
    since_date = since_dt.strftime("%Y-%m-%d")
    since_year = since_dt.year

    # 출력 경로
    if args.output:
        output_path = Path(args.output)
    else:
        from config_loader import get_topic_dir
        output_dir = get_topic_dir(topic)
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / "_search_results.json"

    # 키워드 로드
    kw_config = SEARCH_KEYWORDS[topic]
    primary_kws = kw_config["primary"]
    secondary_kws = kw_config["secondary"]
    all_keywords = primary_kws + secondary_kws

    # 이메일 (OpenAlex polite pool)
    try:
        email = get_unpaywall_email()
    except Exception:
        email = ""

    print(f"\n논문 검색 시작: {topic} (최근 {days}일, {since_date} 이후)")
    print(f"  키워드: {len(primary_kws)}개 주요 + {len(secondary_kws)}개 보조")

    # --- arXiv ---
    print("\n[1/3] arXiv 검색 중...")
    arxiv_papers = search_arxiv(all_keywords, since_date, max_per_keyword=100)
    print(f"  arXiv: {len(arxiv_papers)}건 수집")

    # --- Semantic Scholar ---
    print("\n[2/3] Semantic Scholar 검색 중...")
    ss_papers = search_semantic_scholar(all_keywords, since_year, max_per_keyword=100)
    print(f"  Semantic Scholar: {len(ss_papers)}건 수집")

    # --- OpenAlex ---
    print("\n[3/3] OpenAlex 검색 중...")
    oa_papers = search_openalex(all_keywords, since_date, email, max_per_keyword=100)
    print(f"  OpenAlex: {len(oa_papers)}건 수집")

    # --- 중복 제거 ---
    all_papers = arxiv_papers + ss_papers + oa_papers
    unique_papers = deduplicate(all_papers)
    print(f"\n중복 제거 후: {len(unique_papers)}건 고유 논문")

    # --- 관련성 점수 부여 및 필터링 ---
    for p in unique_papers:
        p["relevance_score"] = round(score_relevance(p, primary_kws, secondary_kws), 3)

    filtered = [p for p in unique_papers if p["relevance_score"] >= threshold]
    filtered.sort(key=lambda p: p["relevance_score"], reverse=True)
    filtered = filtered[:max_papers]
    print(f"필터링 후 (≥{threshold}): {len(filtered)}건")

    # --- 저장 ---
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(filtered, f, ensure_ascii=False, indent=2)

    # --- 요약 출력 ---
    print(f"\n검색 완료: {topic} ({days}일)")
    print(f"  arXiv: {len(arxiv_papers)}건")
    print(f"  Semantic Scholar: {len(ss_papers)}건")
    print(f"  OpenAlex: {len(oa_papers)}건")
    print(f"  중복 제거 후: {len(unique_papers)}건 고유")
    print(f"  필터링 후 (≥{threshold}): {len(filtered)}건")
    print(f"  출력: {output_path}")


if __name__ == "__main__":
    main()
