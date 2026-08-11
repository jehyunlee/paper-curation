# Mapping fMRI research in disorders of consciousness: a bibliometric study

`10.3389/fneur.2026.1807532`

각 값 옆의 `table.column` 이 그 값이 실제로 저장된 위치다.

## `papers` — 서지 본체

논문 1편 = 1행. Zotero 레코드를 참값으로 두고 Scopus·PDF 가 빈칸만 채운다.

| 항목 | 값 | 저장 위치 |
|---|---|---|
| 슬러그 — `docs/papers/{slug}/` 와 1:1 | `2743_Mapping_fMRI_research_in_disorders_of_consciousness_a_biblio` | `papers.slug` |
| 제목 | Mapping fMRI research in disorders of consciousness: a bibliometric study | `papers.title` |
| DOI | `10.3389/fneur.2026.1807532` | `papers.doi` |
| URL | https://doi.org/10.3389/fneur.2026.1807532 | `papers.url` |
| 저널 | Frontiers in Neurology | `papers.journal_name` |
| 권 | 17 | `papers.volume` |
| ISSN | 1664-2295 | `papers.issn` |
| 발행일 | 2026-05-04 | `papers.publication_date` |
| 투고일 | 2026-02-09 | `papers.received_date` |
| 게재확정일 | 2026-04-20 | `papers.accepted_date` |
| 문서 유형 | journalArticle | `papers.document_type` |
| Zotero 아이템 키 | `N2ZXI7SM` | `papers.zotero_item_key` |
| **서지 출처** | zotero-local+pdf | `papers.bibliography_source` |
| 소속 출처 | scopus+pdf | `papers.affiliation_source` |
| 소속 신뢰도 | 0.95 | `papers.affiliation_confidence` |
| 리뷰 디렉토리 | `docs/papers/2743_Mapping_fMRI_research_in_disorders_of_consciousness_a_biblio` | `papers.review_dir` |
| DB 최초 기록 | 2026-08-07 09:14:58 | `papers.created_at` |

> `bibliography_source = zotero-local+pdf` — Zotero + PDF 앞부분이 빈칸 보충

## `authors` + `paper_authors` — 저자 5명

이름 정본은 `authors`, 이 논문에서의 순서·역할은 `paper_authors` 에 있다.

| # | 저자 | 역할 | 저장 위치 |
|---|---|---|---|
| 1 | Xi-Chen Wang | 제1저자 | `authors.display_name` / `paper_authors.author_order` |
| 2 | Di Zhu | — | `authors.display_name` / `paper_authors.author_order` |
| 3 | Jun Lü | — | `authors.display_name` / `paper_authors.author_order` |
| 4 | Guan-Lan Guo | — | `authors.display_name` / `paper_authors.author_order` |
| 5 | Fan Fu | — | `authors.display_name` / `paper_authors.author_order` |

> 출처: `paper_authors.source = review.frontmatter/_papers_index`

## `institutions` + `paper_institutions` — 기관 5곳

기관 정본은 `institutions` (ROR 정규화), 이 논문과의 연결과 **원문 문자열**은 `paper_institutions` 에 있다.

### 1. Nanjing Medical University

| 항목 | 값 | 저장 위치 |
|---|---|---|
| 소재 국가 | China | `institutions.country_name_en` |
| 본사 국가 | China | `institutions.hq_country_name_en` |
| 상위 그룹 | — (최상위) | `institutions.parent_name` |
| ROR ID | `059gcgy73` | `institutions.ror_id` |
| 정규화 근거 | `ror:segment` | `institutions.name_source` |
| 링크 출처 | `scopus+pdf` — Scopus 가 제시하고 PDF 본문에서 확인됨 | `paper_institutions.source` |
| PDF 원문 | `2Affiliated Teaching Hospital of Kangda College, Nanjing Medical University, Nanjing, China` | `paper_institutions.raw_name` |

### 2. Nantong University

| 항목 | 값 | 저장 위치 |
|---|---|---|
| 소재 국가 | China | `institutions.country_name_en` |
| 본사 국가 | China | `institutions.hq_country_name_en` |
| 상위 그룹 | — (최상위) | `institutions.parent_name` |
| ROR ID | `02afcvw97` | `institutions.ror_id` |
| 정규화 근거 | `ror:word-suffix` | `institutions.name_source` |
| 링크 출처 | `scopus+pdf` — Scopus 가 제시하고 PDF 본문에서 확인됨 | `paper_institutions.source` |
| PDF 원문 | `3Affiliated Nantong Clinical College of Nantong University, Nantong, Jiangsu, China` | `paper_institutions.raw_name` |

### 3. Second Affiliated Hospital of Nantong University

| 항목 | 값 | 저장 위치 |
|---|---|---|
| 소재 국가 | China | `institutions.country_name_en` |
| 본사 국가 | China | `institutions.hq_country_name_en` |
| 상위 그룹 | — (최상위) | `institutions.parent_name` |
| ROR ID | `05pdn2z45` | `institutions.ror_id` |
| 정규화 근거 | `ror:segment` | `institutions.name_source` |
| 링크 출처 | `scopus+pdf` — Scopus 가 제시하고 PDF 본문에서 확인됨 | `paper_institutions.source` |
| PDF 원문 | `1Department of Rehabilitation Medicine, Nantong First People's Hospital, Nantong, Jiangsu, China` | `paper_institutions.raw_name` |

### 4. Shandong University

| 항목 | 값 | 저장 위치 |
|---|---|---|
| 소재 국가 | China | `institutions.country_name_en` |
| 본사 국가 | China | `institutions.hq_country_name_en` |
| 상위 그룹 | — (최상위) | `institutions.parent_name` |
| ROR ID | `0207yh398` | `institutions.ror_id` |
| 정규화 근거 | `ror:ror_display` | `institutions.name_source` |
| 링크 출처 | `scopus+pdf` — Scopus 가 제시하고 PDF 본문에서 확인됨 | `paper_institutions.source` |
| PDF 원문 | `Mani Abdul Karim, XIM University, India Linghui Dong, Shandong University, China` | `paper_institutions.raw_name` |

### 5. Southern Medical University

| 항목 | 값 | 저장 위치 |
|---|---|---|
| 소재 국가 | China | `institutions.country_name_en` |
| 본사 국가 | China | `institutions.hq_country_name_en` |
| 상위 그룹 | — (최상위) | `institutions.parent_name` |
| ROR ID | `01vjw4z39` | `institutions.ror_id` |
| 정규화 근거 | `ror:segment` | `institutions.name_source` |
| 링크 출처 | `scopus+pdf` — Scopus 가 제시하고 PDF 본문에서 확인됨 | `paper_institutions.source` |
| PDF 원문 | `Qiuyou Xie, Southern Medical University, China` | `paper_institutions.raw_name` |

## `source_documents` — 원문 파일

변경 감지용 해시. `--changed-only` 빌드가 이 값으로 재처리 여부를 정한다.

| 유형 | 크기 | SHA-256 | 경로 |
|---|---:|---|---|
| `review` | 14,616B | `7575d3a95a820bae…` | `docs/papers/2743_Mapping_fMRI_research_in_disorders_of_consciousness_a_biblio/review.md` |
| `text` | 69,332B | `20a0ebc3b7ddb196…` | `docs/papers/2743_Mapping_fMRI_research_in_disorders_of_consciousness_a_biblio/text.md` |

## `citation_snapshots` — 피인용

기록 없음 — `run_metrics.py` 가 아직 이 논문을 수집하지 않았다.

## DB 밖에 있는 것

| 자산 | 위치 | 연결 |
|---|---|---|
| 한글 리뷰 | `docs/papers/2743_Mapping_fMRI_research_in_disorders_of_consciousness_a_biblio/review.md` | `papers.review_dir` |
| PDF 본문 | `docs/papers/2743_Mapping_fMRI_research_in_disorders_of_consciousness_a_biblio/text.md` | `source_documents.path` |
| 도판 | `docs/papers/2743_Mapping_fMRI_research_in_disorders_of_consciousness_a_biblio/figures/` | 슬러그 |
| 토픽 분류 | `docs/{topic}/_new_classification.json` | 슬러그 |
| 마스터 인덱스 | `docs/papers/_papers_index.json` | 슬러그 |
