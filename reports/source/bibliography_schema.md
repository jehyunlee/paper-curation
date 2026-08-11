# Bibliography DB — 구조와 연결

`.cache/bibliography.sqlite3` · 테이블 12개 · 논문 4,196편

## 파이프라인 위치

```
  Zotero Web API            Zotero PDF 디렉토리
  (서지 참값)                (6,009개 로컬 캐시)
        │                          │
        └────────┬─────────────────┘
                 ▼
     run_update_force.py  ── 리뷰 생성 (concurrency 16)
                 │
                 ├─▶ docs/papers/{slug}/text.md      PDF 본문
                 ├─▶ docs/papers/{slug}/review.md    한글 리뷰
                 ├─▶ docs/papers/{slug}/figures/     도판
                 └─▶ docs/papers/{slug}/bibliography.json
                          ↑ 사이드카: Zotero 레코드 + 저자 +
                            ROR 정규화 기관 (리뷰 시점 포착)
                 │
                 ▼  단일 ingest 스레드 (배치 8편)
        .cache/bibliography.sqlite3   ← 이 문서의 대상
                 │
                 ├─ check_bibliography_db.py --strict   게이트
                 └─ sync_bibliography_db.py --push      Mac mini
```

## 외부 권위 자료

| 자료 | 역할 | 위치 |
|---|---|---|
| **Zotero** | 서지 **참값**. 출판사 전사본이라 Scopus·PDF보다 우선 | Web API + 사이드카 |
| **ROR v2.11** | 기관 신원. 다국어·약칭·법인형 변이를 하나로 병합 | `.cache/ror/ror_index.sqlite3` (135,710 조직) |
| **큐레이션 그룹표** | ROR이 빠뜨린 상위관계 보정 | `pipeline/data/dict_afgroupname_confident.json` |
| **Scopus** | 소속·서지 **빈칸만** 채움 | `.cache/scopus_affiliations.json` |
| **OpenAlex/Crossref** | 피인용수 | `run_metrics.py` |

## 테이블

### `papers` — 4,196행

출처: Zotero record (ground truth) + Scopus/PDF gap-fill

| 컬럼 | 타입 | |
|---|---|---|
| `paper_id` | INTEGER | PK |
| `slug` | TEXT |  |
| `title` | TEXT |  |
| `doi` | TEXT |  |
| `zotero_item_key` | TEXT |  |
| `journal_name` | TEXT |  |
| `publication_date` | TEXT |  |
| `bibliography_source` | TEXT |  |
| _+19개 컬럼_ | | |

### `authors` — 12,908행

출처: Zotero creators → review.md frontmatter → index

| 컬럼 | 타입 | |
|---|---|---|
| `author_id` | INTEGER | PK |
| `display_name` | TEXT |  |
| `normalized_name` | TEXT |  |

### `paper_authors` — 16,319행

출처: authorship order, first/corresponding flags

| 컬럼 | 타입 | |
|---|---|---|
| `paper_id` | INTEGER | FK → `papers` |
| `author_id` | INTEGER | FK → `authors` |
| `author_order` | INTEGER |  |
| `is_first_author` | INTEGER |  |
| `is_corresponding_author` | INTEGER |  |
| _+1개 컬럼_ | | |

### `institutions` — 2,260행

출처: ROR v2.11 normalised identity

| 컬럼 | 타입 | |
|---|---|---|
| `institution_id` | INTEGER | PK |
| `institution_name` | TEXT |  |
| `ror_id` | TEXT |  |
| `country_name_en` | TEXT |  |
| `hq_country_name_en` | TEXT |  |
| `parent_name` | TEXT |  |
| `name_source` | TEXT |  |
| _+4개 컬럼_ | | |

### `paper_institutions` — 10,002행

출처: Scopus FULL + PDF front matter

| 컬럼 | 타입 | |
|---|---|---|
| `paper_id` | INTEGER | FK → `papers` |
| `institution_id` | INTEGER | FK → `institutions` |
| `raw_name` | TEXT |  |
| `country_name` | TEXT |  |
| `source` | TEXT |  |

### `institution_aliases` — 8,286행

출처: raw affiliation strings seen in PDFs

| 컬럼 | 타입 | |
|---|---|---|
| `alias_id` | INTEGER | PK |
| `raw_name` | TEXT |  |
| `normalized_alias` | TEXT |  |
| `institution_id` | INTEGER | FK → `institutions` |

### `citation_snapshots` — 204행

출처: OpenAlex · Crossref · Scopus (run_metrics)

| 컬럼 | 타입 | |
|---|---|---|
| `paper_id` | INTEGER | FK → `papers` |
| `observed_date` | TEXT | PK |
| `openalex_count` | INTEGER |  |
| `scopus_count` | INTEGER |  |
| `normalized_percentile` | REAL |  |
| _+1개 컬럼_ | | |

### `citation_yearly` — 5행

출처: per-year citation counts (run_metrics)

| 컬럼 | 타입 | |
|---|---|---|
| `paper_id` | INTEGER | FK → `papers` |
| `citation_year` | INTEGER | PK |
| `citation_count` | INTEGER |  |
| _+2개 컬럼_ | | |

### `institution_groups` — 0행

출처: legacy grouping — superseded by parent_name

| 컬럼 | 타입 | |
|---|---|---|
| `group_id` | INTEGER | PK |
| `group_name` | TEXT |  |
| _+1개 컬럼_ | | |

### `paper_author_institutions` — 5,103행

출처: —

| 컬럼 | 타입 | |
|---|---|---|
| `paper_id` | INTEGER | FK → `papers` |
| `author_id` | INTEGER | FK → `authors` |
| `institution_id` | INTEGER | FK → `institutions` |
| `marker` | TEXT |  |
| `author_order` | INTEGER |  |
| `source` | TEXT |  |

### `paper_connections` — 51,932행

출처: —

| 컬럼 | 타입 | |
|---|---|---|
| `paper_id` | INTEGER | FK → `papers` |
| `related_paper_id` | INTEGER | FK → `papers` |
| `relation` | TEXT | PK |
| `reason` | TEXT |  |
| `topics` | TEXT |  |
| `model` | TEXT |  |
| `generated_at` | TEXT |  |
| `source` | TEXT |  |

### `source_documents` — 8,342행

출처: review.md / text.md content hashes

| 컬럼 | 타입 | |
|---|---|---|
| `paper_id` | INTEGER | FK → `papers` |
| `document_type` | TEXT | PK |
| `path` | TEXT |  |
| `sha256` | TEXT |  |
| _+1개 컬럼_ | | |

## 출처 분포 (실측)

**서지 출처 (papers)**

- `zotero-local` — 3,021
- `zotero-local+scopus` — 587
- `zotero-local+pdf` — 333
- `zotero-local+scopus+pdf` — 255

**소속 출처 (paper_institutions)**

- `scopus+pdf` — 8,941
- `scopus-unconfirmed` — 759
- `pdf` — 302

**원문 (source_documents)**

- `review` — 4,196
- `text` — 4,146

기관 2,260개 중 ROR 해결 1,600개 · 상위그룹 135종
