# Paper Curation — Architecture & Internals

파이프라인 단계별 상세, 신뢰성 설계, 내부 구조 레퍼런스입니다.
빠른 시작과 전체 그림은 [README](../README.md), 운영 레시피는 [operations.md](operations.md) 를 보세요.

## 파이프라인 단계 상세

### 1. 데이터 수집

| | 설명 |
|---|---|
| **입력** | <ul><li>Zotero 컬렉션의 PDF</li><li>선택: arXiv / Semantic Scholar / OpenAlex 병렬 검색 + Zotero 자동 등록</li></ul> |
| **처리** | <ul><li>PyMuPDF로 텍스트 추출</li><li>Figure 렌더링 (3× zoom, 최대 5장)</li><li>Gemini가 Figure 품질 검증</li></ul> |
| **출력** | <ul><li><code>papers/{slug}/text.md</code></li><li><code>papers/{slug}/figures/*.webp</code></li></ul> |

### 2. 구조화 리뷰

| | 설명 |
|---|---|
| **입력** | 추출된 텍스트 + Figure |
| **처리** | <ul><li>Claude Haiku가 한국어 리뷰 6개 섹션 작성 (Essence · Motivation · Achievement · How · Originality · Evaluation)</li><li>기술 용어는 원문 그대로 유지</li><li>동시 처리 (기본 16, Tier 4)</li></ul> |
| **출력** | <ul><li><code>papers/{slug}/review.md</code></li><li><code>papers/{slug}/index.html</code></li></ul> |
| **활용** | 브라우저에서 리뷰 열람, Figure 인라인 표시, Related Papers 자동 연결 |

### 3. 토픽 모델링 + 분류

| | 설명 |
|---|---|
| **입력** | 전체 리뷰의 Essence + Title |
| **처리** | Bottom-up, LLM 호출 최소화:<ul><li>SPECTER2 임베딩 (proximity adapter + CLS pooling) → HDBSCAN fine-grained 클러스터링</li><li>c-TF-IDF 키워드 추출 (BERTopic 표준 — 클러스터 단위 구별성) → Claude Sonnet이 클러스터 작명</li><li>Ward linkage로 카테고리 그룹핑</li><li>논문당 1~3개 카테고리 복수 분류 (Node-based Hybrid C: KNN-vote primary + qualified-vote multi)</li></ul> |
| **출력** | <ul><li><code>_new_classification.json</code></li><li><code>_papers_index.json</code></li></ul> |

### 4. 인사이트 + 타임라인

| | 설명 |
|---|---|
| **입력** | 카테고리별 논문 목록 + 리뷰 |
| **처리 (Core)** | <ul><li>Claude Sonnet이 카테고리 요약·세부 주제 작성</li><li>**같이 보면 좋은 논문**: 임베딩 top-20 후보 → Sonnet이 관계 유형 + 한국어 이유 선별. 망 장애에 강건 — multi-round 재시도(막힌 배치만), 연결 0개 논문 우선 처리(priority-first), 그래도 남으면 `--local-fallback`(Option)으로 로컬 모델이 완결</li><li>Claude Opus가 카테고리별 연구 동향 내러티브 작성</li><li>PaperBanana가 카테고리당 다이어그램 후보를 여러 장 생성하고, Claude 비전 심사가 그중 최적안을 선별 — 카테고리별 색상이 일관되게 배치됐는지, 카테고리의 등장·소멸·융합·분기가 또렷한지, 색상 이름·번호 같은 불필요한 텍스트가 없는지를 기준으로</li></ul> |
| **처리 (Option O-2, `--insights`)** | <ul><li>크로스카테고리 Research Insights 분석 (Anthropic → OpenAI → Gemini 3-backend fallback)</li><li>네트워크 시각화(<code>network.html</code>) 재생성</li></ul> |
| **출력** | <ul><li><code>_category_summaries.json</code></li><li><code>_paper_connections.json</code></li><li><code>_timeline_narrative.json</code></li><li><code>category_timeline_*.png</code></li><li>(O-2) <code>_insights.json</code> + <code>network.html</code></li></ul> |

### 5. Deep Research 인덱스

| | 설명 |
|---|---|
| **입력** | 전체 리뷰 + 개인 메모(<code>notes/</code>) |
| **처리** | <ul><li>Section-aware chunking</li><li>Google <code>gemini-embedding-001</code> 임베딩 (768d, <code>task_type=RETRIEVAL_DOCUMENT</code>, L2 정규화 후 int8 양자화)</li><li>BM25 sparse 텀도 함께 인덱싱 (hybrid 검색용)</li><li>개인 메모도 인덱싱되어 다음 질의에 반영</li></ul> |
| **출력** | <code>_search_index.json</code> + <code>_search_index_emb.bin</code> |
| **활용** | 토픽 페이지에서 자연어 질의 → 질의 임베딩은 worker <code>/api/embed</code> (배포) 또는 <code>pipeline/serve_local.py</code> (로컬) 가 <code>gemini-embedding-001</code> (<code>task_type=RETRIEVAL_QUERY</code>) 로 대신 계산 → **hybrid 검색** (BM25 + dense, RRF 융합) → LLM 이 상위 후보를 한 문장씩 re-rank → 사용자 키 prefix 자동 감지로 **Anthropic / OpenAI / Google 중 하나**가 논문 근거 답변 스트리밍. 검색에는 독자 키가 전혀 필요 없고, 키(BYOK)는 답변 생성에만 쓰입니다. 응답은 자연어 본문 + 클릭 가능 `[N]` 인용 + 자동 figure 인라인. Fast/Smart 토글 라벨은 감지된 백엔드의 실제 모델명을 표시 (예: `Fast (cost: Sonnet 5)`) |
| **CLI/API 활용** | <code>query_search_index.py</code>가 동일 토크나이저·BM25(<code>k1=1.5, b=0.75</code>)·dense cosine·RRF(<code>k=60</code>)를 읽기 전용으로 실행합니다. 기본 컬렉션은 <code>_cross</code>. <code>--mode bm25</code>는 키 없이 동작하고, hybrid/dense는 Gemini <code>RETRIEVAL_QUERY</code>를 사용합니다. <code>pipeline.api.query_search_index()</code>로 에이전트/자동화에서 JSON 결과를 직접 소비할 수 있습니다. |
| **갱신·품질 경계** | 질의는 인덱스를 재빌드하지 않습니다. curate/rebuild의 <code>run_update_force.py</code>가 source 인덱스와 <code>_cross</code>를 자동 갱신하고 source fingerprint를 기록합니다. 이어 고정 40질의·고정 query vector 평가를 네트워크 없이 실행하며, source 컬렉션 또는 <code>_cross</code>의 recall@5가 baseline보다 0.025 초과 하락하면 배포를 중단합니다. macmini launchd도 같은 평가를 매주 실행합니다. |

### 6. 인덱스 + 네트워크

| | 설명 |
|---|---|
| **입력** | 전체 분류 + 리뷰 + 타임라인 + UMAP 좌표 |
| **처리** | <ul><li>(Core) 카테고리 카드·검색·타임라인·Deep Research UI·Audio Overview 모달을 하나의 HTML로 조립</li><li>(Option O-2, `--insights`) UMAP 2D/3D 좌표로 D3.js + Three.js 인터랙티브 네트워크 재생성</li></ul> |
| **출력** | <ul><li><code>{topic}/index.html</code></li><li>(O-2) <code>{topic}/network.html</code></li></ul> |
| **활용** | <code>cd docs && python -m http.server 8000</code> → 브라우저에서 바로 사용. 개별 논문 페이지 / Deep Research 답변 양쪽에서 🎧 **Audio Overview** 버튼으로 팟캐스트형 한국어 오디오 생성 (Gemini TTS, 브라우저 안에서 MP3 인코딩 → 즉시 다운로드). 배포 환경에선 완성된 MP3 가 이메일로도 자동 발송됨 |

### Citedby: corpus-first 인용 계보와 다중 출력

`pipeline/run_citedby.py`는 한 DOI의 인용논문을 수집한 뒤
`docs/papers/{seed_slug}/citedby/`에 자기완결 HTML·CSV·검색 인덱스를 만듭니다.

| 계층 | 동작 |
|------|------|
| **수집·정규화** | OpenAlex·Scopus·Semantic Scholar·arXiv 결과를 DOI > arXiv ID > 정규화 제목 순으로 병합합니다. 웹 검색 결과도 같은 identity resolver를 거쳐 corpus hit와 중복되지 않습니다. |
| **근거 선택** | `pdf_corpus.tier_papers()`가 corpus 전처리물 > Zotero PDF > 초록 > 제목 순으로 근거를 선택합니다. Corpus 논문은 기존 section chunk와 embedding을 재사용합니다. |
| **타임라인** | 생성·소멸·분기·융합을 중심으로 종합 narrative와 stream별 설명을 만들고 PaperBanana 후보를 생성·비평해 그림을 고릅니다. 전체 wall-clock 상한은 1800초이며, 실패해도 narrative와 보고서는 보존됩니다. |
| **Deep(er) Research** | `_citedby_index.json`과 int8 embedding sidecar를 BM25+dense RRF로 검색합니다. 답변 계획·related-paper 탐색·선택적 웹 검색·streaming 응답을 `/api/citedby-answer`가 제공합니다. |
| **Reference identity** | 웹 citation이 DOI·arXiv·제목으로 corpus와 일치하면 corpus reference로 승격합니다. 본문 `[ref:N]`은 Reference section의 동일 항목을 가리킵니다. |
| **출력별 링크** | 화면(localhost)은 `/papers/{slug}/` review HTML, print/PDF는 DOI·arXiv·원문 URL, Obsidian은 `papers/{slug}/review` 또는 seed 아래 evidence note를 사용합니다. HTML의 `data-local`/`data-external` 쌍과 `beforeprint`/`afterprint` 전환으로 같은 보고서에서 이를 보장합니다. |
| **독립 export** | 원 Citedby 보고서와 Deep(er) Research 답변은 각각 PDF·Markdown·Obsidian·Audio Overview를 내보냅니다. PDF footer에는 프로젝트 출처를 넣습니다. |

`--serve --open`은 `pipeline/lib/citedby/serve.py`를 통해 기존
`serve_local.py`의 `/api/health`를 확인하거나 서버를 기동한 뒤 localhost URL을
엽니다. 따라서 `file://`에서 사용할 수 없는 embedding·streaming·Audio 경로도
생성 직후 동작합니다.


---


> 아래는 유지보수·심화용 레퍼런스입니다. 처음 사용에는 필요 없습니다.

## Reliability (v2+)

최근 리팩터링으로 추가된 안전장치:

| 장치 | 설명 |
|------|------|
| `run_full.py` 오케스트레이터 | 3축(`--mode/--source/--images`) 단일 진입점. 검색·등록·sync·리뷰·후처리·배포 자동 체인. dry-run plan 출력 |
| `find_pdf()` ID-first | Zotero attachment → DOI → arXiv → fuzzy(강화) 순서. 과거 fuzzy 오매칭 근본 원인 제거 |
| `--strict-pdf` | fuzzy 완전 차단 모드. 신규/복구 리뷰에 권장 |
| `classify_papers.py` (Phase 3) | SPECTER2 임베딩 → UMAP transform 5D → `hdbscan.approximate_predict` (density-faithful primary sub-cluster) → outlier(-1) 는 768D centroid 코사인 최단점으로 강제 배정 → `all_categories` = centroid 거리 top-N parent. LLM 호출 0. `py312` 환경에서 실행. |
| `find_pdf()` cross-platform basename | Zotero linked attachment 이 Windows 절대경로 (`C:\Users\…\foo.pdf`) 로 저장된 경우 macOS `os.path.basename` 이 백슬래시를 분리자로 인식 못해 매칭 실패하던 버그. `path.replace("\\", "/").rsplit("/", 1)[-1]` 로 해결 |
| `make_slug()` 40-char collision fix | 25-char prefix matching 이 다른 논문을 거짓 매칭하던 버그 (예: "A Hierarchical Framework for Humanoid Locomotion" ↔ "A hierarchical framework for measuring scientific impact"). 비교 길이를 `min(40, min(len(a), len(b)))` 로 변경, 10-char floor 추가. 짧은 제목의 자기-자신 매칭 (예: "Robot Learning from Human Videos: A Survey", 35 norm chars) 보존 |
| `_zotero_text_sanity()` 한국어/ASCII 듀얼 패스 | Zotero 에 한국어 제목으로 등록된 영문 PDF 케이스 통과. 한글 syllable 을 keyword 추출 정규식에 포함, threshold 스케일링 (구 `max(3, …)` → `max(1, len(kw)*coverage)`), ASCII-only fallback (영문 token 만 일치해도 DOI/author 통과하면 OK) |
| `extract_insights` 3-backend fallback | cross-category insights 호출에 Anthropic → OpenAI → Gemini chain. `EXTRACT_INSIGHTS_CC_BACKENDS` env var 로 순서 override. ReadTimeout/connection 에러 시 다음 backend 자동 시도. 각 backend 는 동일한 tool-use / structured output schema 로 강제 |
| `run_step()` CRITICAL_STEPS hard-fail | `build_papers_index` / `topic_modeling*` / `classify_papers` / source·`_cross` 검색 인덱스 빌드와 품질 평가는 실패 시 `RuntimeError` 로 abort. 신규 분류 누락, stale 검색 인덱스, retrieval recall 회귀 상태로 배포되는 것을 차단. LLM narrative/이미지 생성은 degradable 로 soft-fail 유지 |
| `audit_matching.py` | 동일 text.md 해시 공유 슬러그 탐지 (duplicate PDF) + 4축 cross-check |
| `fix_matching.py` | 감사 결과 기반 리뷰 삭제 + 재리뷰 명령 자동 출력 (기본 dry-run) |
| `dedup_zotero.py` | Zotero 컬렉션 중복 탐지/삭제 (제목 60자 + DOI + arXiv + PDF 공유). `run_update_force` preflight 자동 통합 |
| `validate_papers.py --strict` | 카테고리↔timeline 이미지 매치, duplicate text.md 탐지. 배포 게이트 |
| `cleanup.py` | stale 카테고리 timeline/캐시 삭제 + narrative JSON 내 stale 엔트리 pruning. 후처리 단계에 자동 통합 |
| `prepare_deploy.py` | split-host 배포 자동화: `wrangler deploy` → Cloudflare, gh-pages 리다이렉트 스텁 idempotent 동기화, Cloudflare 200 OK 폴링, master에 코드 변경만 push. API 키 메모리 제거 후 로컬 원복 |
| 21600s timeout | `generate_timelines` 후처리 호출 타임아웃 1h → 6h (PaperBanana 다중 카테고리 완주) |

**오매칭 감사·복구 워크플로우**:
```bash
PYTHONUTF8=1 python pipeline/audit_matching.py --topic my_topic          # 1. 탐지
PYTHONUTF8=1 python pipeline/fix_matching.py --topic my_topic            # 2. dry-run
PYTHONUTF8=1 python pipeline/fix_matching.py --topic my_topic --execute  # 3. 삭제
# 4. fix_matching이 출력한 run_update_force --slugs ... --strict-pdf 실행
PYTHONUTF8=1 python pipeline/audit_matching.py --topic my_topic          # 5. 검증
```

---

## Internal architecture (post-refactor)

파이프라인을 외부 코드에서 부분 호출하거나, 성능을 튜닝하려는 사용자를 위한 내부 구조 노트.

### 1. 프로그래매틱 API — `pipeline/api/`

19 개 CLI 스크립트의 핵심 로직이 `pipeline/api/__init__.py` 에 함수 facade 로 노출됩니다 (총 25 개 public 함수). subprocess 오버헤드 없이 다른 코드/워크플로에서 직접 호출 가능:

```python
from pipeline.api import (
    search, register, sync, dedup_zotero,                        # ingest
    curate,                                                       # full batch
    build_papers_index, topic_model, classify,                   # index + classify
    category_summary, insights, timeline,                        # narrative (LLM)
    network, search_index, topic_index, review_to_html, deploy,  # render + publish
    validate, audit_matching, fix_matching, cleanup,             # safety
)

# 헬퍼
from pipeline.api._llm import cached_call, paper_cache_dir, topic_cache_dir
from pipeline.api.extract import pre_validate_figure
```

각 함수는 thin CLI wrapper 와 같은 `_run_X(**kwargs)` 본체를 공유하므로 CLI 와 API 가 100% 같은 동작을 합니다.

### 2. LLM 호출 캐싱 — `api/_llm.cached_call`

`(prompt, model, schema_version)` 의 SHA-256 해시를 키로 결과를 JSON 으로 저장합니다. 캐시 디렉토리:

- 카테고리/토픽 단위: `docs/{topic}/.llm_cache/{hash}.json`
- 논문 단위 (`write_review`): `docs/papers/{slug}/.llm_cache/{hash}.json`

미변경 입력 재실행 시 LLM 호출 0회. `force=True` 로 우회 가능.

### 3. 카테고리 단위 ThreadPool 병렬화

LLM I/O bound 단계는 카테고리 단위로 병렬화돼 wall-clock 이 약 4× 단축됩니다. env var 로 worker 수 조정:

| 단계 | env var | 기본 worker | 모델 |
|---|---|---|---|
| `build_category_summaries` (카테고리 한글 description + sub-themes) | `CAT_SUMMARY_PARALLEL` | 8 | Haiku |
| `generate_timelines` STEP 1 narrative | `TIMELINE_NARRATIVE_PARALLEL` | 8 | Opus streaming |
| `generate_timelines` STEP 2 PaperBanana 이미지 | `TIMELINE_IMAGE_PARALLEL` | 4 | Gemini image |
| `extract_insights` per-category paper_connections | `EXTRACT_INSIGHTS_PARALLEL` | 4 | Sonnet |

Tier 1~3 에서는 worker 수를 낮춰 ITPM cap 을 피해야 합니다.

### 4. Tool-use schema 강제 — Anthropic structured output

LLM 응답의 JSON 파싱 흔들림을 0 으로 만들기 위해 Anthropic tool-use schema 를 강제합니다. SDK 가 schema mismatch 시 자동 재시도하므로 post-hoc fixer (구 `fix_python_list_literals` / `fix_figure_paths` / `fix_evaluation_format`) 가 모두 폐기됐습니다.

| 호출처 | tool 이름 | 모델 |
|---|---|---|
| `write_review` (논문 1편 리뷰 JSON) | `emit_review` | Haiku |
| `extract_insights.extract_cross_category_insights` | `emit_insights` | Sonnet (+ OpenAI/Gemini fallback) |
| `extract_insights._call_connections_batch` (Anthropic 분기) | `emit_connections` | Sonnet (+ OpenAI `response_format=json_object` fallback) |

### 5. Figure pre-validator — `api/extract.pre_validate_figure`

Gemini 의 figure 검증 호출 전 cheap heuristic check:

1. 파일 크기 < 4 KB → clipped
2. dimension < 100 px → clipped
3. 그레이스케일 픽셀 variance < 30 → near-uniform (clipped)

각 케이스에서 Gemini 의 응답 shape 와 동일한 dict 를 반환하므로 caller 분기 변경 없이 ~30 % 의 LLM 호출이 절감됩니다.

### 6. Schema v1 frontmatter — Obsidian Properties 호환

모든 `docs/papers/{slug}/review.md` 가 v1 YAML frontmatter 를 가집니다 (`inject_frontmatter.py` 가 `_papers_index.json` 에서 생성). 정본 필드 + 본문 섹션 구조:

```yaml
---
title: "<full paper title>"
authors: ["First Last", ...]
date: "2021-07-15"
doi: "..."
primary_topic: ai4s
primary_category: "..."
all_categories: [...]
sub_categories: {"Category": "Sub-category", ...}
scores: {novelty: 5, technical: 5, significance: 5, clarity: 4, overall: 5}
score: 5            # top-level (Obsidian sort)
essence: "..."
tags: [paper, ai4s, "ai4s/category-slug/sub-slug", ...]
schema_version: v1
---
```

기존 review.md 는 `pipeline/_archive/migrate_to_toolschema.py` (일회성 마이그레이션, 현재 아카이브됨) 로 일괄 변환 (백업: `docs/papers/.legacy/{slug}_v0.md`). 재실행 idempotent. 모든 readers (`build_papers_index` / `build_topic_index` / `validate_papers`) 가 frontmatter fast path 우선, 레거시 body-regex 는 fallback.

---

## Karpathy LLM Wiki와의 비교

[Karpathy의 LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)는 "LLM이 정리하고 사람이 큐레이션하는 persistent knowledge base"라는 강력한 개념을 제안했습니다. Paper Curation은 이 철학을 공유하면서, 학술 논문에 특화된 자동화 파이프라인을 결합합니다.

| | Karpathy LLM Wiki | Paper Curation |
|---|---|---|
| **핵심 개념** | LLM이 정보를 정리하고 사람이 큐레이션 | 동일 + 자동 파이프라인 |
| **입력** | 자유 형식 텍스트, 웹 페이지 등 | Zotero PDF (학술 논문 특화) |
| **구조화** | 사용자가 직접 마크다운 작성 | 6개 섹션 자동 생성 (Essence~Evaluation) |
| **분류** | 수동 태깅/폴더 | Bottom-up 자동 분류 (HDBSCAN + UMAP) |
| **검색** | 키워드/전문 검색 | 임베딩 RAG + 자연어 질의 + Claude 답변 |
| **Figure** | 지원하지 않음 | PDF에서 자동 추출 + 인라인 표시 |
| **시각화** | 없음 | 타임라인 다이어그램 + UMAP 2D/3D 네트워크 |
| **지식 축적** | wiki-link 기반 | Obsidian wiki-link + 메모 -> 인덱스 재반영 |
| **배포** | 로컬 파일 | 로컬 + 정적 호스팅 (선택) |
| **설치** | 직접 구성 | Claude Code 한 줄 설치 |
| **장점** | 범용, 가벼움, 어떤 주제든 적용 가능 | 논문 특화 자동화, Figure/분류/시각화 내장 |
| **단점** | 논문 메타데이터/Figure 수동 처리 | 학술 논문 외 콘텐츠에는 과도할 수 있음 |

Paper Curation의 Obsidian 연동은 LLM Wiki의 compounding 개념을 그대로 구현합니다:

```
Deep Research 질의 -> Obsidian 메모 작성 -> 인덱스 재빌드 -> 다음 질의에 내 메모가 인용됨
```


---

## 요구사항

| 구분 | 항목 |
|------|------|
| **필수** | Python 3.12 (macOS conda env `py312`), Zotero (API Key + 컬렉션 + PDF) |
| **API** | Anthropic (Claude Haiku/Sonnet/Opus), Google (Gemini + `gemini-embedding-001` 검색 임베딩), Zotero Web API, Resend (배포 시 Audio Overview 이메일). OpenAI 는 선택 (답변 BYOK·insights fallback) |
| **Python** | `pip install -r requirements.txt` — anthropic, openai, google-genai, pymupdf, Pillow, requests, pyzotero, opendataloader-pdf, numpy, scikit-learn, joblib, umap-learn, hdbscan, sentence-transformers |
| **선택** | Obsidian (메모/Graph View), PaperBanana (타임라인 이미지), Zotero Desktop (PDF 원클릭) |
