# Robin: A multi-agent system for automating scientific discovery

`10.1038/s41586-026-10652-y`

각 값 옆의 `table.column` 이 그 값이 실제로 저장된 위치다.

## `papers` — 서지 본체

논문 1편 = 1행. Zotero 레코드를 참값으로 두고 Scopus·PDF 가 빈칸만 채운다.

| 항목 | 값 | 저장 위치 |
|---|---|---|
| 슬러그 — `docs/papers/{slug}/` 와 1:1 | `10726_robin_a_multi-agent_system_for_automating_scientific_d` | `papers.slug` |
| 제목 | Robin: A multi-agent system for automating scientific discovery | `papers.title` |
| DOI | `10.1038/s41586-026-10652-y` | `papers.doi` |
| URL | https://doi.org/10.1038/s41586-026-10652-y | `papers.url` |
| arXiv ID | 2505.13400 | `papers.arxiv_id` |
| 저널 | Nature | `papers.journal_name` |
| 권 | 655 | `papers.volume` |
| 호 | 8122 | `papers.issue` |
| 쪽 | 497-505 | `papers.pages` |
| 출판사 | Springer Science and Business Media LLC | `papers.publisher` |
| ISSN | 0028-0836 | `papers.issn` |
| 발행일 | 2026-05-19 | `papers.publication_date` |
| 투고일 | 2025-05-23 | `papers.received_date` |
| 게재확정일 | 2026-05-12 | `papers.accepted_date` |
| 온라인 공개일 | 2026-05-19 | `papers.published_online_date` |
| 문서 유형 | journalArticle | `papers.document_type` |
| Zotero 아이템 키 | `VHR6LWX7` | `papers.zotero_item_key` |
| Scopus EID | `2-s2.0-105043785067` | `papers.scopus_eid` |
| **서지 출처** | zotero-local+scopus+pdf | `papers.bibliography_source` |
| 소속 출처 | scopus+pdf | `papers.affiliation_source` |
| 소속 신뢰도 | 0.95 | `papers.affiliation_confidence` |
| 리뷰 디렉토리 | `docs/papers/10726_robin_a_multi-agent_system_for_automating_scientific_d` | `papers.review_dir` |
| DB 최초 기록 | 2026-08-07 09:11:08 | `papers.created_at` |

> `bibliography_source = zotero-local+scopus+pdf` — Zotero + Scopus + PDF 보충

## `authors` + `paper_authors` — 저자 14명

이름 정본은 `authors`, 이 논문에서의 순서·역할은 `paper_authors` 에 있다.

| # | 저자 | 역할 | 저장 위치 |
|---|---|---|---|
| 1 | Ali E. Ghareeb | 제1저자 | `authors.display_name` / `paper_authors.author_order` |
| 2 | Benjamin Chang | — | `authors.display_name` / `paper_authors.author_order` |
| 3 | Ludovico Mitchener | — | `authors.display_name` / `paper_authors.author_order` |
| 4 | Angela Yiu | — | `authors.display_name` / `paper_authors.author_order` |
| 5 | Caralyn J. Szostkiewicz | — | `authors.display_name` / `paper_authors.author_order` |
| 6 | Dmytro Shved | — | `authors.display_name` / `paper_authors.author_order` |
| 7 | Gavin J. Gyimesi | — | `authors.display_name` / `paper_authors.author_order` |
| 8 | Jon M. Laurent | — | `authors.display_name` / `paper_authors.author_order` |
| 9 | Samantha M. Wright | — | `authors.display_name` / `paper_authors.author_order` |
| 10 | Muhammed T. Razzak | — | `authors.display_name` / `paper_authors.author_order` |
| 11 | Andrew D. White | — | `authors.display_name` / `paper_authors.author_order` |
| 12 | Silvia C. Finnemann | — | `authors.display_name` / `paper_authors.author_order` |
| 13 | Michaela M. Hinks | — | `authors.display_name` / `paper_authors.author_order` |
| 14 | Samuel G. Rodriques | — | `authors.display_name` / `paper_authors.author_order` |

> 출처: `paper_authors.source = review.frontmatter/_papers_index`

## `institutions` + `paper_institutions` — 기관 3곳

기관 정본은 `institutions` (ROR 정규화), 이 논문과의 연결과 **원문 문자열**은 `paper_institutions` 에 있다.

### 1. Fordham University

| 항목 | 값 | 저장 위치 |
|---|---|---|
| 소재 국가 | United States | `institutions.country_name_en` |
| 본사 국가 | United States | `institutions.hq_country_name_en` |
| 상위 그룹 | — (최상위) | `institutions.parent_name` |
| ROR ID | `03qnxaf80` | `institutions.ror_id` |
| 정규화 근거 | `ror:ror_display` | `institutions.name_source` |
| 링크 출처 | `scopus+pdf` — Scopus 가 제시하고 PDF 본문에서 확인됨 | `paper_institutions.source` |
| PDF 원문 | `Fordham University` | `paper_institutions.raw_name` |

### 2. FutureHouse Inc.

| 항목 | 값 | 저장 위치 |
|---|---|---|
| 소재 국가 | United States | `institutions.country_name_en` |
| 본사 국가 | — | `institutions.hq_country_name_en` |
| 상위 그룹 | — (최상위) | `institutions.parent_name` |
| ROR ID | `미해결` | `institutions.ror_id` |
| 정규화 근거 | `—` | `institutions.name_source` |
| 링크 출처 | `scopus+pdf` — Scopus 가 제시하고 PDF 본문에서 확인됨 | `paper_institutions.source` |
| PDF 원문 | `FutureHouse Inc.` | `paper_institutions.raw_name` |

### 3. University of Oxford

| 항목 | 값 | 저장 위치 |
|---|---|---|
| 소재 국가 | United Kingdom | `institutions.country_name_en` |
| 본사 국가 | United Kingdom | `institutions.hq_country_name_en` |
| 상위 그룹 | — (최상위) | `institutions.parent_name` |
| ROR ID | `052gg0110` | `institutions.ror_id` |
| 정규화 근거 | `umbrella-only` | `institutions.name_source` |
| 링크 출처 | `scopus+pdf` — Scopus 가 제시하고 PDF 본문에서 확인됨 | `paper_institutions.source` |
| PDF 원문 | `University of Oxford` | `paper_institutions.raw_name` |

## `source_documents` — 원문 파일

변경 감지용 해시. `--changed-only` 빌드가 이 값으로 재처리 여부를 정한다.

| 유형 | 크기 | SHA-256 | 경로 |
|---|---:|---|---|
| `review` | 6,163B | `648a214a91d485bb…` | `docs/papers/10726_robin_a_multi-agent_system_for_automating_scientific_d/review.md` |
| `text` | 102,277B | `035343be038ba298…` | `docs/papers/10726_robin_a_multi-agent_system_for_automating_scientific_d/text.md` |

## `citation_snapshots` — 피인용

| 관측일 | OpenAlex | Crossref | Scopus | 백분위 |
|---|---:|---:|---:|---:|
| 2026-07-25 | 8 | None | None | None |

## DB 밖에 있는 것

| 자산 | 위치 | 연결 |
|---|---|---|
| 한글 리뷰 | `docs/papers/10726_robin_a_multi-agent_system_for_automating_scientific_d/review.md` | `papers.review_dir` |
| PDF 본문 | `docs/papers/10726_robin_a_multi-agent_system_for_automating_scientific_d/text.md` | `source_documents.path` |
| 도판 | `docs/papers/10726_robin_a_multi-agent_system_for_automating_scientific_d/figures/` | 슬러그 |
| 토픽 분류 | `docs/{topic}/_new_classification.json` | 슬러그 |
| 마스터 인덱스 | `docs/papers/_papers_index.json` | 슬러그 |
