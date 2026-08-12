# The reorganization of the American innovation ecosystem and the challenge of translating science

`10.3389/frma.2021.751553`

각 값 옆의 `table.column` 이 그 값이 실제로 저장된 위치다.

## `papers` — 서지 본체

논문 1편 = 1행. Zotero 레코드를 참값으로 두고 Scopus·PDF 가 빈칸만 채운다.

| 항목 | 값 | 저장 위치 |
|---|---|---|
| 슬러그 — `docs/papers/{slug}/` 와 1:1 | `1042_The_Scholarly_Knowledge_Ecosystem_Challenges_and_Opportuniti` | `papers.slug` |
| 제목 | The reorganization of the American innovation ecosystem and the challenge of translating science | `papers.title` |
| DOI | `10.3389/frma.2021.751553` | `papers.doi` |
| URL | https://doi.org/10.3389/frma.2021.751553 | `papers.url` |
| 저널 | Industrial and Corporate Change | `papers.journal_name` |
| 권 | 34 | `papers.volume` |
| 호 | 6 | `papers.issue` |
| 쪽 | 1206-1228 | `papers.pages` |
| 출판사 | Oxford University Press | `papers.publisher` |
| ISSN | 1464-3650; 0960-6491 | `papers.issn` |
| 발행일 | 2025-12-01 | `papers.publication_date` |
| 투고일 | 2021-08-01 | `papers.received_date` |
| 게재확정일 | 2021-12-15 | `papers.accepted_date` |
| 문서 유형 | journalArticle | `papers.document_type` |
| Zotero 아이템 키 | `RM7J55RG` | `papers.zotero_item_key` |
| Scopus EID | `2-s2.0-85145045585` | `papers.scopus_eid` |
| **서지 출처** | zotero-local+scopus+pdf | `papers.bibliography_source` |
| 소속 출처 | scopus+pdf | `papers.affiliation_source` |
| 소속 신뢰도 | 0.95 | `papers.affiliation_confidence` |
| 리뷰 디렉토리 | `docs/papers/1042_The_Scholarly_Knowledge_Ecosystem_Challenges_and_Opportuniti` | `papers.review_dir` |
| DB 최초 기록 | 2026-08-07 09:11:03 | `papers.created_at` |

> `bibliography_source = zotero-local+scopus+pdf` — Zotero + Scopus + PDF 보충

## `authors` + `paper_authors` — 저자 2명

이름 정본은 `authors`, 이 논문에서의 순서·역할은 `paper_authors` 에 있다.

| # | 저자 | 역할 | 저장 위치 |
|---|---|---|---|
| 1 | Micah Altman | 제1저자 | `authors.display_name` / `paper_authors.author_order` |
| 2 | Philip N. Cohen | — | `authors.display_name` / `paper_authors.author_order` |

> 출처: `paper_authors.source = review.frontmatter/_papers_index`

## `institutions` + `paper_institutions` — 기관 4곳

기관 정본은 `institutions` (ROR 정규화), 이 논문과의 연결과 **원문 문자열**은 `paper_institutions` 에 있다.

### 1. Griffith University

| 항목 | 값 | 저장 위치 |
|---|---|---|
| 소재 국가 | Australia | `institutions.country_name_en` |
| 본사 국가 | Australia | `institutions.hq_country_name_en` |
| 상위 그룹 | — (최상위) | `institutions.parent_name` |
| ROR ID | `02sc3r913` | `institutions.ror_id` |
| 정규화 근거 | `ror:segment` | `institutions.name_source` |
| 링크 출처 | `scopus+pdf` — Scopus 가 제시하고 PDF 본문에서 확인됨 | `paper_institutions.source` |
| PDF 원문 | `Grifﬁth University, Australia` | `paper_institutions.raw_name` |

### 2. MIT Libraries

| 항목 | 값 | 저장 위치 |
|---|---|---|
| 소재 국가 | United States | `institutions.country_name_en` |
| 본사 국가 | — | `institutions.hq_country_name_en` |
| 상위 그룹 | — (최상위) | `institutions.parent_name` |
| ROR ID | `미해결` | `institutions.ror_id` |
| 정규화 근거 | `—` | `institutions.name_source` |
| 링크 출처 | `scopus+pdf` — Scopus 가 제시하고 PDF 본문에서 확인됨 | `paper_institutions.source` |
| PDF 원문 | `MIT Libraries` | `paper_institutions.raw_name` |

### 3. Massachusetts Institute of Technology

| 항목 | 값 | 저장 위치 |
|---|---|---|
| 소재 국가 | United States | `institutions.country_name_en` |
| 본사 국가 | United States | `institutions.hq_country_name_en` |
| 상위 그룹 | — (최상위) | `institutions.parent_name` |
| ROR ID | `042nb2s44` | `institutions.ror_id` |
| 정규화 근거 | `ror:ror_display` | `institutions.name_source` |
| 링크 출처 | `scopus+pdf` — Scopus 가 제시하고 PDF 본문에서 확인됨 | `paper_institutions.source` |
| PDF 원문 | `1 Center for Research in Equitable and Open Scholarship, MIT Libraries, Massachusetts Institute of Technology,` | `paper_institutions.raw_name` |

### 4. University of Maryland, College Park

| 항목 | 값 | 저장 위치 |
|---|---|---|
| 소재 국가 | United States | `institutions.country_name_en` |
| 본사 국가 | United States | `institutions.hq_country_name_en` |
| 상위 그룹 | — (최상위) | `institutions.parent_name` |
| ROR ID | `047s2c258` | `institutions.ror_id` |
| 정규화 근거 | `ror:ror_display` | `institutions.name_source` |
| 링크 출처 | `scopus+pdf` — Scopus 가 제시하고 PDF 본문에서 확인됨 | `paper_institutions.source` |
| PDF 원문 | `University of Maryland, College Park` | `paper_institutions.raw_name` |

## `source_documents` — 원문 파일

변경 감지용 해시. `--changed-only` 빌드가 이 값으로 재처리 여부를 정한다.

| 유형 | 크기 | SHA-256 | 경로 |
|---|---:|---|---|
| `review` | 12,353B | `94ee28f9cdee1dfe…` | `docs/papers/1042_The_Scholarly_Knowledge_Ecosystem_Challenges_and_Opportuniti/review.md` |
| `text` | 57,420B | `52dab02c2276d99f…` | `docs/papers/1042_The_Scholarly_Knowledge_Ecosystem_Challenges_and_Opportuniti/text.md` |

## `citation_snapshots` — 피인용

| 관측일 | OpenAlex | Crossref | Scopus | 백분위 |
|---|---:|---:|---:|---:|
| 2026-07-25 | 17 | 13 | 17 | 0.94978872 |

## DB 밖에 있는 것

| 자산 | 위치 | 연결 |
|---|---|---|
| 한글 리뷰 | `docs/papers/1042_The_Scholarly_Knowledge_Ecosystem_Challenges_and_Opportuniti/review.md` | `papers.review_dir` |
| PDF 본문 | `docs/papers/1042_The_Scholarly_Knowledge_Ecosystem_Challenges_and_Opportuniti/text.md` | `source_documents.path` |
| 도판 | `docs/papers/1042_The_Scholarly_Knowledge_Ecosystem_Challenges_and_Opportuniti/figures/` | 슬러그 |
| 토픽 분류 | `docs/{topic}/_new_classification.json` | 슬러그 |
| 마스터 인덱스 | `docs/papers/_papers_index.json` | 슬러그 |
