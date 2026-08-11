# FraPPE: Fast and Efficient Preference-based Pure Exploration

`10.52202/085713-0312`

각 값 옆의 `table.column` 이 그 값이 실제로 저장된 위치다.

## `papers` — 서지 본체

논문 1편 = 1행. Zotero 레코드를 참값으로 두고 Scopus·PDF 가 빈칸만 채운다.

| 항목 | 값 | 저장 위치 |
|---|---|---|
| 슬러그 — `docs/papers/{slug}/` 와 1:1 | `9682_FraPPE_Fast_and_Efficient_Preference-based_Pure_Exploration` | `papers.slug` |
| 제목 | FraPPE: Fast and Efficient Preference-based Pure Exploration | `papers.title` |
| DOI | `10.52202/085713-0312` | `papers.doi` |
| URL | https://doi.org/10.52202/085713-0312 | `papers.url` |
| 저널 | Advances in Neural Information Processing Systems 38 | `papers.journal_name` |
| 쪽 | 10190-10236 | `papers.pages` |
| 출판사 | Neural Information Processing Systems Foundation, Inc. (NeurIPS) | `papers.publisher` |
| 발행일 | 2025 | `papers.publication_date` |
| 문서 유형 | journalArticle | `papers.document_type` |
| Zotero 아이템 키 | `NB4ET7MP` | `papers.zotero_item_key` |
| **서지 출처** | zotero-local | `papers.bibliography_source` |
| 소속 출처 | scopus+pdf | `papers.affiliation_source` |
| 소속 신뢰도 | 0.95 | `papers.affiliation_confidence` |
| 리뷰 디렉토리 | `docs/papers/9682_FraPPE_Fast_and_Efficient_Preference-based_Pure_Exploration` | `papers.review_dir` |
| DB 최초 기록 | 2026-08-07 09:18:27 | `papers.created_at` |

> `bibliography_source = zotero-local` — Zotero 단독으로 완결 (출판사 전사본)

## `authors` + `paper_authors` — 저자 3명

이름 정본은 `authors`, 이 논문에서의 순서·역할은 `paper_authors` 에 있다.

| # | 저자 | 역할 | 저장 위치 |
|---|---|---|---|
| 1 | Udvas Das | 제1저자 | `authors.display_name` / `paper_authors.author_order` |
| 2 | Apurv Shukla | — | `authors.display_name` / `paper_authors.author_order` |
| 3 | Debabrota Basu | — | `authors.display_name` / `paper_authors.author_order` |

> 출처: `paper_authors.source = review.frontmatter/_papers_index`

## `institutions` + `paper_institutions` — 기관 1곳

기관 정본은 `institutions` (ROR 정규화), 이 논문과의 연결과 **원문 문자열**은 `paper_institutions` 에 있다.

### 1. University of Michigan

| 항목 | 값 | 저장 위치 |
|---|---|---|
| 소재 국가 | United States | `institutions.country_name_en` |
| 본사 국가 | United States | `institutions.hq_country_name_en` |
| 상위 그룹 | — (최상위) | `institutions.parent_name` |
| ROR ID | `00jmfr291` | `institutions.ror_id` |
| 정규화 근거 | `ror:ror_display` | `institutions.name_source` |
| 링크 출처 | `scopus+pdf` — Scopus 가 제시하고 PDF 본문에서 확인됨 | `paper_institutions.source` |
| PDF 원문 | `Department of EECS, University of Michigan` | `paper_institutions.raw_name` |

## `source_documents` — 원문 파일

변경 감지용 해시. `--changed-only` 빌드가 이 값으로 재처리 여부를 정한다.

| 유형 | 크기 | SHA-256 | 경로 |
|---|---:|---|---|
| `review` | 6,460B | `180aef5429dd1e9e…` | `docs/papers/9682_FraPPE_Fast_and_Efficient_Preference-based_Pure_Exploration/review.md` |
| `text` | 131,787B | `b5d226478ab18c1a…` | `docs/papers/9682_FraPPE_Fast_and_Efficient_Preference-based_Pure_Exploration/text.md` |

## `citation_snapshots` — 피인용

기록 없음 — `run_metrics.py` 가 아직 이 논문을 수집하지 않았다.

## DB 밖에 있는 것

| 자산 | 위치 | 연결 |
|---|---|---|
| 한글 리뷰 | `docs/papers/9682_FraPPE_Fast_and_Efficient_Preference-based_Pure_Exploration/review.md` | `papers.review_dir` |
| PDF 본문 | `docs/papers/9682_FraPPE_Fast_and_Efficient_Preference-based_Pure_Exploration/text.md` | `source_documents.path` |
| 도판 | `docs/papers/9682_FraPPE_Fast_and_Efficient_Preference-based_Pure_Exploration/figures/` | 슬러그 |
| 토픽 분류 | `docs/{topic}/_new_classification.json` | 슬러그 |
| 마스터 인덱스 | `docs/papers/_papers_index.json` | 슬러그 |
