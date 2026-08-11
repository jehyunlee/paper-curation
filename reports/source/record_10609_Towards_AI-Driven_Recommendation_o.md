# Towards AI-Driven Recommendation of Liquid Chromatography Conditions for Chemical Reactions

`10.1021/acs.analchem.6c02058`

각 값 옆의 `table.column` 이 그 값이 실제로 저장된 위치다.

## `papers` — 서지 본체

논문 1편 = 1행. Zotero 레코드를 참값으로 두고 Scopus·PDF 가 빈칸만 채운다.

| 항목 | 값 | 저장 위치 |
|---|---|---|
| 슬러그 — `docs/papers/{slug}/` 와 1:1 | `10609_Towards_AI-Driven_Recommendation_of_Liquid_Chromatography_Co` | `papers.slug` |
| 제목 | Towards AI-Driven Recommendation of Liquid Chromatography Conditions for Chemical Reactions | `papers.title` |
| DOI | `10.1021/acs.analchem.6c02058` | `papers.doi` |
| URL | https://doi.org/10.1021/acs.analchem.6c02058 | `papers.url` |
| 저널 | Analytical Chemistry | `papers.journal_name` |
| 권 | 98 | `papers.volume` |
| 호 | 24 | `papers.issue` |
| 쪽 | 18151-18163 | `papers.pages` |
| 출판사 | American Chemical Society (ACS) | `papers.publisher` |
| ISSN | 0003-2700 | `papers.issn` |
| 발행일 | 2026-06-09 | `papers.publication_date` |
| 문서 유형 | journalArticle | `papers.document_type` |
| Zotero 아이템 키 | `6PMIZKW3` | `papers.zotero_item_key` |
| **서지 출처** | zotero-local | `papers.bibliography_source` |
| 소속 출처 | scopus+pdf | `papers.affiliation_source` |
| 소속 신뢰도 | 0.95 | `papers.affiliation_confidence` |
| 리뷰 디렉토리 | `docs/papers/10609_Towards_AI-Driven_Recommendation_of_Liquid_Chromatography_Co` | `papers.review_dir` |
| DB 최초 기록 | 2026-08-07 09:11:06 | `papers.created_at` |

> `bibliography_source = zotero-local` — Zotero 단독으로 완결 (출판사 전사본)

## `authors` + `paper_authors` — 저자 5명

이름 정본은 `authors`, 이 논문에서의 순서·역할은 `paper_authors` 에 있다.

| # | 저자 | 역할 | 저장 위치 |
|---|---|---|---|
| 1 | Youngchun Kwon | 제1저자 | `authors.display_name` / `paper_authors.author_order` |
| 2 | Hyukju Kwon | — | `authors.display_name` / `paper_authors.author_order` |
| 3 | Jinju Park | — | `authors.display_name` / `paper_authors.author_order` |
| 4 | Youn-Suk Choi | — | `authors.display_name` / `paper_authors.author_order` |
| 5 | Seokho Kang | — | `authors.display_name` / `paper_authors.author_order` |

> 출처: `paper_authors.source = review.frontmatter/_papers_index`

## `institutions` + `paper_institutions` — 기관 2곳

기관 정본은 `institutions` (ROR 정규화), 이 논문과의 연결과 **원문 문자열**은 `paper_institutions` 에 있다.

### 1. Samsung Electronics

| 항목 | 값 | 저장 위치 |
|---|---|---|
| 소재 국가 | South Korea | `institutions.country_name_en` |
| 본사 국가 | South Korea | `institutions.hq_country_name_en` |
| 상위 그룹 | Samsung (South Korea) | `institutions.parent_name` |
| ROR ID | `020m7t761` | `institutions.ror_id` |
| 정규화 근거 | `ror:segment` | `institutions.name_source` |
| 링크 출처 | `scopus+pdf` — Scopus 가 제시하고 PDF 본문에서 확인됨 | `paper_institutions.source` |
| PDF 원문 | `Samsung Advanced Institute of Technology, Samsung Electronics Co. Ltd., Suwon 16678, Republic of Korea` | `paper_institutions.raw_name` |

### 2. Sungkyunkwan University

| 항목 | 값 | 저장 위치 |
|---|---|---|
| 소재 국가 | South Korea | `institutions.country_name_en` |
| 본사 국가 | South Korea | `institutions.hq_country_name_en` |
| 상위 그룹 | — (최상위) | `institutions.parent_name` |
| ROR ID | `04q78tk20` | `institutions.ror_id` |
| 정규화 근거 | `ror:segment` | `institutions.name_source` |
| 링크 출처 | `scopus+pdf` — Scopus 가 제시하고 PDF 본문에서 확인됨 | `paper_institutions.source` |
| PDF 원문 | `Department of Industrial Engineering, Sungkyunkwan University, Suwon 16419, Republic of Korea` | `paper_institutions.raw_name` |

## `source_documents` — 원문 파일

변경 감지용 해시. `--changed-only` 빌드가 이 값으로 재처리 여부를 정한다.

| 유형 | 크기 | SHA-256 | 경로 |
|---|---:|---|---|
| `review` | 7,107B | `910d2e9b88a189d3…` | `docs/papers/10609_Towards_AI-Driven_Recommendation_of_Liquid_Chromatography_Co/review.md` |
| `text` | 57,643B | `3ab86eedce7fea16…` | `docs/papers/10609_Towards_AI-Driven_Recommendation_of_Liquid_Chromatography_Co/text.md` |

## `citation_snapshots` — 피인용

기록 없음 — `run_metrics.py` 가 아직 이 논문을 수집하지 않았다.

## DB 밖에 있는 것

| 자산 | 위치 | 연결 |
|---|---|---|
| 한글 리뷰 | `docs/papers/10609_Towards_AI-Driven_Recommendation_of_Liquid_Chromatography_Co/review.md` | `papers.review_dir` |
| PDF 본문 | `docs/papers/10609_Towards_AI-Driven_Recommendation_of_Liquid_Chromatography_Co/text.md` | `source_documents.path` |
| 도판 | `docs/papers/10609_Towards_AI-Driven_Recommendation_of_Liquid_Chromatography_Co/figures/` | 슬러그 |
| 토픽 분류 | `docs/{topic}/_new_classification.json` | 슬러그 |
| 마스터 인덱스 | `docs/papers/_papers_index.json` | 슬러그 |
