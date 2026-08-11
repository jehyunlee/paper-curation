# Strategic Hypothesis Testing

`10.52202/085713-4894`

각 값 옆의 `table.column` 이 그 값이 실제로 저장된 위치다.

## `papers` — 서지 본체

논문 1편 = 1행. Zotero 레코드를 참값으로 두고 Scopus·PDF 가 빈칸만 채운다.

| 항목 | 값 | 저장 위치 |
|---|---|---|
| 슬러그 — `docs/papers/{slug}/` 와 1:1 | `10506_Strategic_Hypothesis_Testing` | `papers.slug` |
| 제목 | Strategic Hypothesis Testing | `papers.title` |
| DOI | `10.52202/085713-4894` | `papers.doi` |
| URL | https://doi.org/10.52202/085713-4894 | `papers.url` |
| 저널 | Advances in Neural Information Processing Systems 38 | `papers.journal_name` |
| 쪽 | 162375-162402 | `papers.pages` |
| 출판사 | Neural Information Processing Systems Foundation, Inc. (NeurIPS) | `papers.publisher` |
| 발행일 | 2025 | `papers.publication_date` |
| 문서 유형 | journalArticle | `papers.document_type` |
| Zotero 아이템 키 | `6TK5DIBK` | `papers.zotero_item_key` |
| **서지 출처** | zotero-local | `papers.bibliography_source` |
| 소속 출처 | scopus+pdf | `papers.affiliation_source` |
| 소속 신뢰도 | 0.95 | `papers.affiliation_confidence` |
| 리뷰 디렉토리 | `docs/papers/10506_Strategic_Hypothesis_Testing` | `papers.review_dir` |
| DB 최초 기록 | 2026-08-07 09:11:04 | `papers.created_at` |

> `bibliography_source = zotero-local` — Zotero 단독으로 완결 (출판사 전사본)

## `authors` + `paper_authors` — 저자 3명

이름 정본은 `authors`, 이 논문에서의 순서·역할은 `paper_authors` 에 있다.

| # | 저자 | 역할 | 저장 위치 |
|---|---|---|---|
| 1 | Yatong Chen | 제1저자 | `authors.display_name` / `paper_authors.author_order` |
| 2 | Safwan Hossain | — | `authors.display_name` / `paper_authors.author_order` |
| 3 | Yiling Chen | — | `authors.display_name` / `paper_authors.author_order` |

> 출처: `paper_authors.source = review.frontmatter/_papers_index`

## `institutions` + `paper_institutions` — 기관 3곳

기관 정본은 `institutions` (ROR 정규화), 이 논문과의 연결과 **원문 문자열**은 `paper_institutions` 에 있다.

### 1. Harvard University

| 항목 | 값 | 저장 위치 |
|---|---|---|
| 소재 국가 | United States | `institutions.country_name_en` |
| 본사 국가 | United States | `institutions.hq_country_name_en` |
| 상위 그룹 | — (최상위) | `institutions.parent_name` |
| ROR ID | `03vek6s52` | `institutions.ror_id` |
| 정규화 근거 | `ror:ror_display` | `institutions.name_source` |
| 링크 출처 | `scopus+pdf` — Scopus 가 제시하고 PDF 본문에서 확인됨 | `paper_institutions.source` |
| PDF 원문 | `Harvard University` | `paper_institutions.raw_name` |

### 2. Max Planck Institute for Intelligent Systems

| 항목 | 값 | 저장 위치 |
|---|---|---|
| 소재 국가 | Germany | `institutions.country_name_en` |
| 본사 국가 | Germany | `institutions.hq_country_name_en` |
| 상위 그룹 | Max Planck Society | `institutions.parent_name` |
| ROR ID | `04fq9j139` | `institutions.ror_id` |
| 정규화 근거 | `ror:ror_display` | `institutions.name_source` |
| 링크 출처 | `scopus+pdf` — Scopus 가 제시하고 PDF 본문에서 확인됨 | `paper_institutions.source` |
| PDF 원문 | `Max Planck Institute for Intelligent Systems` | `paper_institutions.raw_name` |

### 3. Tübingen AI Center

| 항목 | 값 | 저장 위치 |
|---|---|---|
| 소재 국가 | Germany | `institutions.country_name_en` |
| 본사 국가 | Germany | `institutions.hq_country_name_en` |
| 상위 그룹 | University of Tübingen | `institutions.parent_name` |
| ROR ID | `0107nyd78` | `institutions.ror_id` |
| 정규화 근거 | `ror:ror_display` | `institutions.name_source` |
| 링크 출처 | `scopus+pdf` — Scopus 가 제시하고 PDF 본문에서 확인됨 | `paper_institutions.source` |
| PDF 원문 | `Tübingen AI Center` | `paper_institutions.raw_name` |

## `source_documents` — 원문 파일

변경 감지용 해시. `--changed-only` 빌드가 이 값으로 재처리 여부를 정한다.

| 유형 | 크기 | SHA-256 | 경로 |
|---|---:|---|---|
| `review` | 6,094B | `d0cfdc2183bb14ba…` | `docs/papers/10506_Strategic_Hypothesis_Testing/review.md` |
| `text` | 95,526B | `148658cb5c4d871a…` | `docs/papers/10506_Strategic_Hypothesis_Testing/text.md` |

## `citation_snapshots` — 피인용

기록 없음 — `run_metrics.py` 가 아직 이 논문을 수집하지 않았다.

## DB 밖에 있는 것

| 자산 | 위치 | 연결 |
|---|---|---|
| 한글 리뷰 | `docs/papers/10506_Strategic_Hypothesis_Testing/review.md` | `papers.review_dir` |
| PDF 본문 | `docs/papers/10506_Strategic_Hypothesis_Testing/text.md` | `source_documents.path` |
| 도판 | `docs/papers/10506_Strategic_Hypothesis_Testing/figures/` | 슬러그 |
| 토픽 분류 | `docs/{topic}/_new_classification.json` | 슬러그 |
| 마스터 인덱스 | `docs/papers/_papers_index.json` | 슬러그 |
