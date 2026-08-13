# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Academic paper curation pipeline. Papers are fetched from Zotero, reviewed via Claude/Gemini APIs, classified into categories, and published as a searchable HTML index with per-paper review pages. Topic pages also expose a **Deep Research UI** that performs client-side RAG against a pre-built embedding index (Google `gemini-embedding-001`, 768d int8, task-typed) and streams Claude answers with `[ref:N]` citations and inline figures. Retrieval is hybrid BM25+dense fused with RRF and LLM re-ranked; query embeddings are computed for the reader by the worker `/api/embed` route (deployed) or `pipeline/serve_local.py` (local), so readers need no API key for retrieval — keys (BYOK) are only for answer generation.

- **Topics**: Configured per-user in `config.json` (e.g., `ai4s`, `scisci`, `bioml`). Per-topic Core-1 search keywords are configurable via the `search_keywords` block (`{topic: {primary: [...], secondary: [...]}}`); `ai4s`/`scisci` ship built-in defaults, so new topics add their own there.
- **Deploy architecture** (split hosting):
  - **Cloudflare Workers (Static Assets + Functions)** serves the full content at the custom domain `paper-curation.jehyunlee.dev` (the `CF_BASE_URL` constant in `prepare_deploy.py`, provisioned via the `[[routes]]` block in `wrangler.toml`; the default `*.workers.dev` URL also resolves but is not the canonical one). `pipeline/prepare_deploy.py` runs `npx wrangler deploy` (token via `CLOUDFLARE_API_TOKEN`/`CF_API_TOKEN` + `CLOUDFLARE_ACCOUNT_ID`). Uploads everything under `docs/` except entries in `docs/.assetsignore` (ai4s/scisci are local-only). `worker/index.js` exposes two routes that need wrangler secrets (`wrangler secret put`): `/api/embed` (Deep Research query embeddings — `GOOGLE_API_KEY`) and `/api/audio-email` (Audio Overview email — `RESEND_API_KEY`).
  - **GitHub `gh-pages` branch** holds tiny redirect stubs only — one `{topic}/index.html` per deployable topic that `meta refresh` + `window.location.replace()` to the Cloudflare URL. Synced idempotently by `prepare_deploy.py`.
  - **GitHub `master` branch** holds only code, `config.example.json`, `wrangler.toml`, and `docs/.assetsignore`. `docs/papers/`, `docs/humanoid/`, `docs/physical-ai/`, etc. are `.gitignore`'d to keep the repo small (full content lives only on Cloudflare + local).
  - User access: `jehyunlee.github.io/paper-curation/{topic}/` → gh-pages stub → Cloudflare URL → full content.
- **Language**: All reviews are written in Korean with technical terms in English

## Installation Flow (Claude Code)

사용자가 "여기에 paper-curation을 설치해줘: https://github.com/jehyunlee/paper-curation" 같은 요청을 하면, 아래 순서대로 진행한다.

### Step 1: Clone & Dependencies
```bash
git clone https://github.com/jehyunlee/paper-curation.git
cd paper-curation
pip install anthropic google-genai pymupdf Pillow requests opendataloader-pdf
```

### Step 2: config.json 생성
사용자에게 아래 정보를 **하나씩 질문**하고 config.json을 생성한다:
1. **Zotero API Key** — **환경변수 `ZOTERO_API_KEY` 전용.** `config.json` 에 저장하지 않고 묻지도 않는다. 없으면 발급 링크를 안내하고 설치를 중단한다 (과거 이 키가 소스에 하드코딩된 채 public master 로 유출된 사고가 있었다 — 2026-08-13)
2. **이메일** — Zotero/Unpaywall용
3. **Zotero 컬렉션 이름** — "Zotero에서 큐레이션할 컬렉션 이름이 뭔가요?"
4. **Topic alias** — "앞으로 이 Collection의 Paper Curation을 운영하려면 부르기 편한 이름을 하나 정하는 게 좋습니다. 짧은 이름을 하나 지어주세요. 뭐라고 부를까요?" (예: `bioml`, `climate`)
5. **Zotero PDF 저장 경로**
6. **PaperBanana 경로** — "PaperBanana가 이미 설치된 경로가 있으면 알려주세요. 없으면 자동으로 클론합니다." (없으면 생략, setup.py가 자동 클론)
7. **GitHub 설정** — 선택사항 (정적 호스팅 자동 배포용), 없으면 생략
8. **GOOGLE_API_KEY** — Deep Research 검색 인덱스 빌드(`build_search_index.py`)가 Google `gemini-embedding-001` 로 임베딩하므로 **필수**다 (Figure 검증·TTS 와 공용). 환경변수에 없으면 setup.py가 직접 입력받아 `config.json` 에 저장한다. `OPENAI_API_KEY` 는 **선택** — 독자 BYOK 답변과 insights fallback 에만 쓰이고, 없어도 설치가 진행된다.

### Step 3: setup.py 실행 및 검증
```bash
PYTHONUTF8=1 python pipeline/setup.py
```
setup.py는 6단계 설치 후 곧바로 첫 파이프라인을 실행한다:
- [1/6] config.json 로드 (없으면 인터랙티브 생성)
- [2/6] 환경변수 확인 — **`ANTHROPIC_API_KEY` 와 `GOOGLE_API_KEY` (검색 임베딩 `gemini-embedding-001` · Figure 검증 · TTS) 는 필수**. `OPENAI_API_KEY` 는 선택 (독자 BYOK 답변 · insights fallback) 이라 없어도 경고만.
- [3/6] Zotero 연결 테스트 (User ID + 컬렉션 검증)
- [4/6] PaperBanana 확인 (없으면 자동 클론)
- [5/6] SKILL.md 생성
- [6/6] SKILL.md를 `~/.claude/skills/paper-curation/` 에 설치
- [Step 7] `run_update_force.py --topic {alias}` 자동 실행 → Zotero 가져오기 → 리뷰 → 분류 → 인덱스 → Deep Research 검색 인덱스 → (GitHub 설정 시) 배포까지 한 번에. `--no-run` 플래그로 이 자동 실행은 건너뛸 수 있다.

### 컬렉션 오류 처리
setup.py 출력에 `[COLLECTION_ERROR]`가 포함되면 컬렉션 이름이 잘못된 것이다.
출력에서 `available` 목록을 추출하여 사용자에게 보여주고 올바른 이름을 다시 질문한다:

> "Zotero에서 '{입력한 이름}' 컬렉션을 찾을 수 없습니다. 사용 가능한 컬렉션은 다음과 같습니다:
> `컬렉션A`, `컬렉션B`, `컬렉션C`, ...
> 어떤 컬렉션을 사용하시겠어요?"

사용자가 올바른 이름을 알려주면 config.json을 수정하고 setup.py를 다시 실행한다.

### 설치 완료 후 안내
setup.py 출력의 "다음 단계" 섹션을 사용자에게 전달한다. 특히:
- 파이프라인 실행 시간이 논문 편수에 따라 크게 달라진다는 점을 안내
- 사용자의 topic alias가 반영된 실행 명령어를 보여준다

## Architecture

### Central Data Store

`docs/papers/` is the single source of truth for all paper content:
- `docs/papers/_papers_index.json` — master index (965 entries) with metadata, categories, scores
- `docs/papers/{NNN_Slug}/review.md` — Korean review in structured markdown
- `docs/papers/{NNN_Slug}/index.html` — generated from review.md by `review_to_html.py`
- `docs/papers/{NNN_Slug}/figures/*.webp` — extracted figures (PNG→WebP for deploy)

### Topic Views

`docs/ai4s/` and `docs/scisci/` each contain:
- `index.html` — category-grouped card view (generated by `build_topic_index.py`)
- `network.html` — D3.js force-directed network visualization (generated by `generate_network.py`)
- `_new_classification.json` — category definitions + paper→category assignments
- `_category_summaries.json` — per-category descriptions, sub-themes
- `_timeline_narrative.json` — executive summary + category analyses (Korean)
- `_category_narratives.json` — per-category narrative cache for timeline generation
- `_method_text_*.txt` — methodology narrative per category
- `category_timeline_*.png` — per-category timeline images (PaperBanana)

### Shared Modules

`pipeline/lib/` contains shared utilities:
- `categories.py` — `CATEGORIES_BY_TOPIC` (canonical category lists) + `category_slug()` (name→filesystem slug)
- `paperbanana.py` — PaperBanana wrapper (path management, agent init, diagram generation)
- `dateutil.py` — Date parsing and formatting utilities

### Pipeline Scripts (execution order)

| Step | Script | Purpose |
|------|--------|---------|
| Entry | `pipeline/run_full.py` | 3-axis orchestrator (`--mode/--source/--images`). Chains all steps below in the right order; also exposes `--mode audit/fix-matching/dedup/validate` as standalone tool entrypoints |
| 0 | `pipeline/search_papers.py` | arXiv/S2/OpenAlex search + dedup + relevance filter |
| 0 | `pipeline/register_zotero.py` | Zotero registration + PDF download |
| 0 | `pipeline/sync_zotero.py` | Sync deletions/renames from Zotero |
| 0.5 | `pipeline/dedup_zotero.py` | Zotero collection dedup (title60 + DOI + arXiv + PDF). Preflight (dry-run) auto-integrated into `run_update_force` |
| 1 | `pipeline/run_update_force.py` | Full batch: Zotero fetch → PDF parse → figure extract → **Zotero↔text sanity gate** → review → HTML. ID-first `find_pdf()` with `--strict-pdf` blocking fuzzy |
| 1.5 | `pipeline/run_metrics.py` | **피인용수·레퍼런스** — `citations.md`(이력 append + 피인용 10회↑ 인용목록) + `references.md`(DOI>URL>서지). 기본 30일 증분이라 매 사이클 태워도 비용 거의 없음. **soft step**(외부 API 장애가 파이프라인을 죽이지 않음). `--skip-metrics` 로 생략 |
| 2 | `pipeline/build_papers_index.py` | Rebuild `_papers_index.json` with integrity fields (`text_md_sha256`, `doi_verified`, `zotero_item_key`) via atomic write |
| 3 | `pipeline/classify_papers.py` | **HDBSCAN approximate_predict (원 설계)** — `topic_modeling` 이 저장한 `_hdbscan_model.joblib` 번들(hdbscan_model + UMAP transformer + centroids + tid→cat) 로드 → UMAP 5D 투영 → `hdbscan.approximate_predict` 로 primary sub-cluster 결정. Outlier(-1)는 768D centroid 코사인 최단점으로 강제 배정. `all_categories` 는 centroid 거리 오름차순 top-N parent. SPECTER2 임베딩은 proximity adapter + CLS pooling (업그레이드 후 새 임베딩을 반영하려면 `topic_modeling.py` 를 한 번 재실행해 `_hdbscan_model.joblib` 번들을 재생성해야 함). LLM 호출 없음. **UMAP/hdbscan/sentence-transformers env 필수** (py312 단독 — py314 금지, `_env_guard` 가 py312 로 자동 재실행) |
| 4 | `pipeline/build_category_summaries.py` | Per-category 한글 description + sub-themes via Haiku |
| 4.5 | `pipeline/extract_insights.py` | Paper connections via Sonnet (Core 기본). Cross-category Research Insights 생성은 **opt-in** — `run_full --insights` 일 때만. Auto Haiku-summarization fallback when prompt >988k tokens (compress toward 900k). cross-category 호출은 Anthropic → OpenAI → Gemini fallback |
| 5 | `pipeline/generate_timelines.py` | Bottom-up timeline narrative (Opus) + PaperBanana images. Gemini retry schedule 3×60s → 2×1800s |
| 5.5 | `pipeline/generate_network.py` | D3.js force-directed network visualization |
| 5.5 | `pipeline/generate_workflow.py` | Pipeline workflow diagram (PaperBanana, `--style cat/fairy/academic`) |
| 6 | `pipeline/validate_papers.py` | Strict validation gate: figure refs, classification schema, category whitelist, DOI cross-validation, duplicate text.md, timeline↔category match. `--strict` exits 1 |
| 7 | `pipeline/review_to_html.py` | Convert review.md → index.html (canonical template) |
| 8 | `pipeline/build_topic_index.py` | Generate `{topic}/index.html` with cards, search, timelines, Deep Research UI |
| 8.5 | `pipeline/build_search_index.py` | Build Deep Research RAG index — section-aware chunks + Google `gemini-embedding-001` (`output_dimensionality=768`, `task_type=RETRIEVAL_DOCUMENT`; non-3072 차원은 비정규화로 돌아오므로 **반드시 L2-normalize 후 int8 양자화**) + BM25 sparse terms → `{topic}/_search_index.json`. 쿼리 임베딩은 worker `/api/embed` / `serve_local.py` 가 `RETRIEVAL_QUERY` 로 처리 |
| 9 | `pipeline/cleanup.py` | Remove stale files (old timelines, graphify temp, caches) + prune stale category entries from narrative JSONs |
| 10 | `pipeline/prepare_deploy.py` | PNG→WebP, API-key strip/restore, `wrangler deploy` → Cloudflare, idempotent gh-pages stub sync, Cloudflare 200 OK polling, then master commit (code/config only — docs/* gitignored) |
| Recover | `pipeline/audit_matching.py` | PDF↔review mismatch audit (duplicate text.md + 4-axis cross-check). Output `{topic}/_audit_report.json` |
| Recover | `pipeline/fix_matching.py` | Recovery tool: delete review/figure artifacts for audit-flagged slugs + print re-review command. Default dry-run, `--execute` for real |
| Recover | `pipeline/fix_review_headers.py` | **제목 헤더 복구** — review.md 본문의 `# 제목` + `> **저자**:` 헤더가 유실되면 `review_to_html` 이 제목을 slug 디렉터리 **절대경로**로 대체해 `<title>`·`<h1>`·`og:title` 에 로컬 경로가 노출된다. `review.md.broken.bak` 에 원본 헤더가 있으면 그대로 회수하고, 없으면 frontmatter(title/authors/date/doi)로 재구성한 뒤 `index.html` 을 재생성한다. 기본 dry-run, `--execute` 로 적용. `validate_papers.py` 의 `NO_TITLE_HEADER` 체크가 재발을 잡는다 |
|Tool|`pipeline/run_citedby.py`|**Citedby** — DOI 하나로 인용논문 수집(OpenAlex·Scopus·S2·arXiv) → 독창성 추출 → 주제 필터 + 5W1H 요약 → **자기완결 HTML 문서** + CSV. 브라우저 [PDF 출력] 버튼으로 링크 살아있는 PDF. 내 Zotero 라이브러리에 있는 논문은 `zotero://open-pdf` 바로열기 링크. 코어는 `pipeline/lib/citedby/`|
| Tool | `pipeline/run_citedby.py --pdf-first` | **PDF-first citedby** — 인용논문을 코퍼스·내 Zotero 로컬 DB(`zotero.sqlite`)와 대조해 **근거 등급**(코퍼스 전처리물 > 보유 PDF 전문 > 초록 > 제목)을 매기고, 전문을 청킹·임베딩해 `_citedby_index.json` 생성(`--build-index`). 리포트에 Deep Research 패널(BM25+dense RRF, BYOK) · 논문별 `zotero://open-pdf` 링크 · **컬렉션 배정 제안**(기존 컬렉션만) 포함. Deep Research 는 `serve_local.py` 로 열어야 동작 |
|Tool|`pipeline/run_metrics.py`|**Metrics** — 코퍼스 논문의 피인용수·레퍼런스 수집 → `docs/papers/{slug}/citations.md`(피인용 **이력** 누적 + 임계값 10회 이상이면 인용논문 목록) + `references.md`(DOI>URL>서지 순 표기). 기본 30일 증분. 피인용수는 소스별 보존(Scopus·Crossref·OpenAlex) + OpenAlex 연차보정 백분위. 코어는 `pipeline/lib/metrics/`|
| Tool | `pipeline/build_slide_deck.py` | **Slide deck** — 토픽 코퍼스(`_category_summaries` / `_timeline_narrative` / `_new_classification` / `_insights` + `_papers_index`)에서 대분류 8개 × 편수 상위 서브카테고리 5개 = 40장 + 오프닝·종합 10장 = **발표 슬라이드 50장 원고**를 생성. **편수는 `_category_summaries.json` 의 `count` 를 믿지 않고 `load_corpus()` 가 `recount_categories()` 로 `_new_classification.json` 에서 다시 센다** — 요약본은 `build_category_summaries.py` 가 돌던 시점의 스냅샷이라 이후 신규 논문이 빠진다. 두 기준을 함께 싣는다: `count`(고유 배정 = primary만, 8개 합 = 코퍼스 크기, 커버리지 산술의 분모) + `card_count`(중복 포함 = all_categories, **토픽 인덱스 `build_topic_index.py` 의 카테고리 헤더 편수와 동일** — 사이트는 논문을 배정된 모든 카테고리에 카드로 노출). 사례는 `--since`(기본 2025) 이후 우선, 불릿의 시스템명이 대표 논문과 일치할 때만 `[n]` 인용 마커를 붙이고 레퍼런스는 **논문별 리뷰 문서(`docs/papers/{slug}/index.html`)로 링크**. 출력은 `reports/build/{topic}_slides_50.html`(자기완결·인쇄용) + `reports/source/{topic}_slides_50.md`(Obsidian) |
| Tool | `pipeline/build_slide_essay.py` | **Slide essay (v2)** — `build_slide_deck.py` 의 데이터·레퍼런스·인용 마커 로직을 재사용하되, 슬라이드 한 장을 **책 한 절 분량의 줄글**로 쓴 판본. 본문은 `pipeline/lib/slide_prose_ai4s.py` 의 `PROSE`(lead/body/close, 50장·약 5.8만자)에서 오고, 화면에 띄울 한 줄은 v1 헤드라인을 그대로 쓴다. `pipeline/lib/slide_prose_ai4s.py` 의 손으로 쓴 `{N}편` 은 코퍼스가 늘면 어긋나므로 `pipeline/tests/test_build_slide_deck.py` 의 `Ai4sProseCountDriftTests` 가 게이트한다. 출력은 `reports/build/{topic}_slides_50_v2.html` + `reports/source/{topic}_slides_50_v2.md` |
| Tool | `pipeline/build_institution_report.py` | **Institution report** — 토픽 상위 N개 기관의 **연구 흐름 서술 문단**(측정값에서 조립, LLM 미사용) + **연도별 누적 막대 SVG**(분류별 색분할) + **대표 도판 3장**(N/S/C 우선) + **연도별 주제 흐름** + **연구그룹**(저자 공유 연결성분 → 저자가 겹치지 않으면 다른 랩으로 보고 시간과 무관하게 병렬 배치) + **주요 연구자**(편수·Nature/Science/Cell 게재) + **링크된 레퍼런스**. `.cache/bibliography.sqlite3` 만 읽고 코퍼스를 바꾸지 않는다. 출력은 `reports/build/{topic}_institutions_top{n}.html`(자기완결) + `reports/source/{topic}_institutions_top{n}.md`. 호출: `run_full.py --mode report --top N` · `pipeline.api.institution_report()` · 직접 실행 |

Step 0 scripts are for full/update modes only (skipped in --local). Step 1 is the heavy batch (default `--concurrency 16`, Tier 4 — see README "Concurrency 가이드"). Wall-clock is ~20~30분 for ~80 papers at concurrency 16; ~1.5h at 4 (Tier 1 보수값).

### Optional Step 0 boost: scholar-megasearch

`pipeline/search_papers.py` 는 arXiv + Semantic Scholar + OpenAlex 3개 소스만 본다. **신규 토픽 첫 build** 나 **분야가 넓어 단일 인덱스 누락이 우려되는 주간 사이클** 에는 [scholar-megasearch](https://github.com/TaewoooPark/scholar-megasearch) 스킬을 Step 0 대안으로 쓸 수 있다 — 20+ DB (Crossref / PubMed / bioRxiv / medRxiv / DOAJ / CORE / BASE / OpenAIRE / Zenodo / Unpaywall / HAL / DBLP / IACR / SSRN / Europe PMC + arXiv / S2 / OpenAlex) fan-out → DOI/arXiv/title30 dedup with provenance → corroboration ranking → OA PDF 다운로드까지 한 번에. 한국 망 arXiv 429 도 자동 fallback.

| Step | Script | Purpose |
|------|--------|---------|
| 0-mega | scholar-megasearch (skill) | 20+ DB fan-out → `literature_search/<topic>_<date>/corpus.json` + `pdfs/manifest.json` |
| 0-mega | `pipeline/megasearch_to_zotero.py` | corpus → `_search_results.json` 변환 + `_papers_index.json` cross-dedup (이미 리뷰한 논문 자동 제외) + 받아둔 PDF 를 Zotero PDF 디렉토리로 pre-stage |

연결 패턴:

```bash
# 1) Claude Code 안에서 스킬 실행 (예: bioml 토픽 첫 build)
#    "search every database for biology + ML for the last year, L4 with PDFs"
#    → literature_search/bioml-ml_2026-06-08/{corpus.json, pdfs/}

# 2) corpus → _search_results.json 변환 (cross-dedup + PDF pre-stage)
PYTHONUTF8=1 python pipeline/megasearch_to_zotero.py \
  --topic bioml \
  --corpus literature_search/bioml-ml_2026-06-08/corpus.json \
  --pdfs-dir literature_search/bioml-ml_2026-06-08/pdfs \
  --min-sources 2          # 2개 이상 DB 가 surface 한 corroborated 만

# 3) 기존 파이프라인 진입 — register_zotero 가 Zotero 등록 + PDF 첨부
PYTHONUTF8=1 python pipeline/register_zotero.py --topic bioml

# 4) 이후는 평소대로 — run_full --mode curate --source zotero 가 sync → review → ...
PYTHONUTF8=1 python pipeline/run_full.py --topic bioml --mode curate --source zotero
```

`megasearch_to_zotero.py` 가 자동으로 처리하는 것:
- **min-sources 필터** — `--min-sources 2` 이상이면 corroboration 노이즈 컷
- **`_papers_index.json` cross-dedup** — DOI / arXiv-id / title30 매치 시 skip, `_megasearch_skipped_known.json` 에 로그
- **PDF pre-stage** — scholar-megasearch 가 받은 OA PDF 를 `safe_filename(title) + ".pdf"` 형식으로 Zotero PDF 디렉토리에 복사 → `register_zotero.download_pdf()` 가 존재 체크에서 단축되어 재다운로드 안 함
- **paper dict 매핑** — `year` → `date`, `sources` → `_megasearch_sources` (traceability 유지)

`--register` 한 줄로 변환 + Zotero 등록까지 한 번에:

```bash
PYTHONUTF8=1 python pipeline/megasearch_to_zotero.py \
  --topic bioml --corpus run/corpus.json --pdfs-dir run/pdfs --register
```

**언제 쓰나**:
- 신규 토픽 첫 build — 광범위 sweep + L3+ citation snowball 로 seed corpus 확보
- bioml/chem/medical 처럼 `search_papers.py` 가 잡지 못하는 PubMed/bioRxiv/medRxiv 가 중요한 토픽
- 한국 망에서 arXiv 429 가 chronic 한 시기

**언제 안 쓰나**:
- 주간 운영 (`run_full --mode curate --source web --days 7`) — 기존 `search_papers.py` 가 빠르고 충분
- `--source zotero` (로컬 Zotero 만) — Step 0 자체가 skip

**MCP 의존성**: `~/.claude.json` 의 `mcpServers` 에 `arxiv-mcp-server` / `asta` / `paper-search-mcp` 가 등록돼 있어야 함 (`scholar-megasearch/setup/install.sh` 가 자동 등록). `uv` 가 없으면 arxiv-mcp-server 만 비활성 (paper-search-mcp 가 arXiv 도 커버하므로 운영에는 영향 없음).

### run_update_force.py flags

| Flag | Effect |
|------|--------|
| `--resume` | Update mode: skip existing review.md, preserve categories |
| `--timeline` | Regenerate timeline images (with --resume: changed cats only) |
| `--category` | Re-run topic_modeling, auto-enables --timeline for changed cats |
| `--resume --timeline` | Update + changed category timeline images |
| `--resume --category` | Update + full reclassification + changed cat timelines |

## Python Environment

**표준 환경: 단일 conda env `py312` (Python 3.12, macOS / Linux)** — 오케스트레이터·LLM·웹·PDF·HTML·클러스터링 단계 모두 여기서 돌린다. `requirements.txt` 가 umap-learn / hdbscan / sentence-transformers 를 포함하므로, 현재 인터프리터로 클러스터링 라이브러리 import 가 성공하면 `topic_modeling.py` / `classify_papers.py` 가 **별도 서브프로세스 없이 in-process** 로 실행된다. Python 3.12 는 numba 의 `CALL_KW` 비호환 문제가 없어 단일 env 로 충분하다.

**⚠️ py314 사용 금지 (운영자 지시 2026-06-18)**: paper-curation 은 **py312 단독**으로만 돌린다. Python 3.14 는 numba 의 bytecode interpreter 가 3.14 의 `CALL_KW` opcode 를 처리하지 못해 `umap_cluster.transform()` → `sklearn.pairwise_distances(metric=callable)` 경로에서 죽는다 (`op_CALL_KW: pop from empty list`). 이를 피하려고 과거엔 py314 메인 + py312 보조 듀얼을 썼으나, 지금은 **py312 단일 표준**으로 통일했다. 모든 실행 진입점(`__main__`)이 `_env_guard.force_py312()` 를 호출해, py312 가 아닌 인터프리터(예: py314)로 실행되면 **py312 로 자동 재실행**한다. py312 를 못 찾으면 명확히 실패하며 절대 py314 로 진행하지 않는다 (탐색 우선순위: `PAPER_CURATION_PY312` → 형제 env `../py312/bin/python` → `which python3.12`).

### macOS / Linux (권장)

```bash
# 1) miniconda 가 이미 깔려 있다고 가정. 최초 1회 단일 env 생성:
conda create -n py312 -c conda-forge python=3.12 pip -y
conda activate py312

# 2) 핵심 의존성 설치 (umap-learn / hdbscan / sentence-transformers 포함)
pip install -r requirements.txt

# 3) Java Runtime — opendataloader-pdf 는 Java CLI 래퍼. 없으면 PyMuPDF 로
#    조용히 fallback 되어 표/구조 추출 품질이 떨어짐.
brew install --cask temurin   # macOS Eclipse Temurin (OpenJDK)

# 4) 새 셸이 열릴 때 py312 자동 활성화
echo 'conda activate py312' >> ~/.zshrc

# 5) 평소 사용 — 클러스터링 라이브러리가 import 되므로 classify/topic_modeling 도 in-process 로 실행
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode curate --source web --days 7
```

> py312 단독 환경만 지원한다. py314 등 다른 인터프리터로 실행해도 `_env_guard.force_py312()` 가 py312 로 자동 재실행하므로, 별도 듀얼 env 구성은 필요 없다 (위 "⚠️ py314 사용 금지" 참조).

### Windows fallback (Smart App Control 환경)

Windows Smart App Control(WDAC) 이 Python 3.14 의 numba/llvmlite DLL 을 차단하는 경우도 위와 동일한 `py312` env 로 분리되어 자동 라우팅된다. 콘다 env 가 형제 위치 (`<base>/envs/py312`) 에 없으면 `PAPER_CURATION_PY312` 환경변수로 절대 경로를 지정:

```cmd
set PAPER_CURATION_PY312=C:\Users\<you>\miniconda3\envs\py312\python.exe
PYTHONUTF8=1 python pipeline\run_full.py --topic ai4s --mode curate --source zotero
```

### 한국 망 환경 우회 (SPECTER2 / arXiv)

한국 ISP 에서 `huggingface.co` LFS 가 막혀 SPECTER2 (`allenai/specter2_base`) 다운로드 실패하는 경우, AWS S3 미러로 한 번 받으면 `topic_modeling.py` 의 `SPECTER2_MODEL` 상수가 `.cache/base/` 를 자동 인식한다:

```bash
mkdir -p .cache && cd .cache
curl -L -o specter2_0.tar.gz "https://ai2-s2-research-public.s3.amazonaws.com/specter2_0/specter2_0.tar.gz"
tar -xzf specter2_0.tar.gz   # base/ + adapters/
```

arXiv 가 chronic 429/timeout 인 경우 `search_papers.py --skip-arxiv` 로 우회 (OpenAlex + S2 만 사용, 윈도우당 ~8분 단축). README "한국 망 환경 우회" 섹션 참고.

## Bibliography DB (persistent corpus memory)

`pipeline/build_bibliography_db.py` is the canonical builder for the collection-independent bibliographic DB. It stores title, authors, first author, DOI/URL, publication date, journal, Zotero item key, one review directory, normalized institutions, parent groups, country names, and institution aliases. Do not rely on conversational memory for this dataset.

- Query by institution/country/author: `PYTHONUTF8=1 python pipeline/query_bibliography.py --institution "Cambridge" --sort date`
- Validate completeness before using or publishing: `PYTHONUTF8=1 python pipeline/check_bibliography_db.py --strict`
- The Mac mini local DB (`.cache/bibliography.sqlite3`) is canonical; the MacBook keeps its own local copy and `pipeline/sync_bibliography_db.py` pulls before review generation and pushes after DB updates. Google Drive is only a backup/transport copy, never a live SQLite volume.
- Rebuild the full DB only with `--all`; the full-corpus worker uses a persistent Mac mini LaunchAgent and writes progress to `.cache/logs/bibliography_full.log`.
- Only one review-generation job may write the canonical SQLite file at a time. The MacBook sync hook refuses to treat Google Drive as a live database and transfers atomically over SSH.
- Review-generation progress is persisted in `.cache/review_progress.json` and phase labels are printed as `PDF 매칭 → text.md 추출 → figure 추출 → review.md 생성 → HTML 변환`; use the JSON file or the run log for a live status view.
- Any new paper-ingestion or Zotero-sync workflow that changes `_papers_index.json` MUST either rebuild the DB or leave a clearly visible stale-db validation failure. The DB is not authoritative when its paper count differs from `_papers_index.json`.
- Affiliation resolution order is Zotero first (its records are transcribed from the publisher, so they are ground truth for bibliographic fields), then Scopus FULL abstract metadata and PDF front matter as **gap-fillers only** — never overrides. Institutions come from Scopus plus active PDF verification using the leading pages and author-information blocks; the reference list is never read. Scopus-only rows stay `scopus-unconfirmed`; PDF-confirmed rows use `scopus+pdf`. `pipeline/tests/test_affiliation_extraction_contract.py` gates this — it is backed by strings that actually reached the shipped DB.
- The affiliation organisation registry (`affiliation_registry.json`, `affiliation_organizations`, `lib/affiliation_registry.py`, `audit_affiliation_registry.py`) was retired 2026-08-09: `institutions.organization_id` was NULL for every row, all 4,373 organisations were typed `other`, and the whole 45 MB payload reduced to two usable aliases. The ISO country map survives as `lib/country_map.py`, the writer lock as `lib/bibliography_lock.py`, and the CAS content digest as `lib/db_digest.py`.
- Review generation writes a per-paper `docs/papers/{slug}/bibliography.json` sidecar (`run_update_force.write_bibliography_sidecar`): the Zotero record, its creator list, and the ROR-normalised institutions — captured while the Zotero item, `text.md` and the matched PDF are all still in hand. `build_bibliography_db.py` consumes it and **skips paging the Zotero library entirely** when every paper in the build has one (that read is a fixed ~200 s and its failure mode was silent `zotero_item_key` loss). A sidecar is refused when its schema is unknown, the Zotero key is missing, or `text_md_sha256` no longer matches `text.md`, so a stale one never outranks a fresh extraction. It is a file rather than a direct DB write because reviews run at `--concurrency 16` and a per-paper insert would serialise them behind one SQLite writer lock.
- Institution naming is ROR-backed. `pipeline/setup_affiliation_sources.py` is the reproducible acquisition step (idempotent; `--check` reports, `--refresh-ror` pulls a new release): it downloads the ROR dump from Zenodo, projects `.cache/ror/ror_index.sqlite3`, and resolves the operator-curated Scopus group table across three layers, most explicit first — `PAPER_CURATION_AFGROUP_DICT` (live copy, so operator edits apply without a commit), `pipeline/data/dict_afgroupname_confident.json` (**pinned baseline committed to the repo**, which is what makes a clean checkout reproduce the same parent groups), then `.cache/affiliation/` (staged from the KIER Google Drive as a last resort). `check_bibliography_db.py --strict` fails when no layer has it, because losing the table costs 2,336 curated hierarchies while ROR keeps resolving — nothing else in the report would move. `run_update_force.py` runs it before `build_bibliography_db`, because all three artifacts live under gitignored `.cache/` and a wiped cache otherwise degrades silently to raw PDF strings — `check_bibliography_db.py --strict` now fails when `ror_share` drops below 0.40.
- `institutions` carries `ror_id`, `parent_name`, `parent_ror_id`, `name_source`. Multilingual and acronym variants collapse onto one ROR record (`Universität Wien`=`University of Vienna`, `清华大学`=`Tsinghua University`, `Fraunhofer …(ISE)`=`Fraunhofer … ISE`); English labels win over native ROR display names. `parent_name` is the *outermost* eligible research umbrella (Max Planck Society, Helmholtz Association, Chinese Academy of Sciences, Fraunhofer-Gesellschaft). Ineligible as parents: administrative organs (`Ministry`, `Government of`, `Board of`, `Office of`, `Department of`, VA networks) and multi-campus public university systems, whose campuses are independent research performers. Co-occurrence on one affiliation line is not a hierarchy — the umbrella must own the institute in ROR.
- Institution aliases belong in `institution_aliases`; never create a second spelling ad hoc in downstream queries.
- Completion reporting is part of the worker contract: the full run sends a Resend email to `jehyun.lee@gmail.com` when `RESEND_API_KEY` is available.
## Common Commands

All scripts require `PYTHONUTF8=1` on Windows to avoid cp949 encoding issues. Single entrypoint is `pipeline/run_full.py` (3축: `--mode/--source/--images`); 개별 스크립트는 디버깅·복구용으로만 직접 호출.

```bash
# 주간 운영 — 검색 + Zotero 등록 + sync + 신규 리뷰
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode curate --source web --days 7

# 로컬 업데이트 — 검색 스킵, sync만
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode curate --source zotero

# 특정 슬러그만 force-rebuild (감사·복구 시)
#   --slugs 는 "이 논문들만 바뀌었다"는 선언이라 후처리도 그 범위로 좁혀진다:
#   topic_modeling 은 저장된 HDBSCAN 번들을 재사용(--skip-classification)하고,
#   narrative/timeline 은 바뀐 카테고리만, review_to_html 은 해당 논문 + 연결된
#   이웃 페이지만 다시 만든다. (--slugs 없는 --mode rebuild 는 전편 재생성이므로
#   토픽 전체 재생성이 그대로 맞다.)
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode rebuild --slugs 088,1093 --strict-pdf

# 분류만 다시 (Phase 3 node-based, LLM 호출 없음)
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode reclassify

# 타임라인 narrative + 이미지 재생성
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode retime --images all

# 배포만: wrangler deploy → Cloudflare + gh-pages 스텁 동기화 + master 코드 push
# (humanoid·physical-ai 만 Cloudflare; ai4s/scisci는 docs/.assetsignore 로 제외)
# 요구 env: CF_API_TOKEN (or CLOUDFLARE_API_TOKEN) + CLOUDFLARE_ACCOUNT_ID
# Worker secrets (1회): wrangler secret put GOOGLE_API_KEY (/api/embed) + RESEND_API_KEY (/api/audio-email)
PYTHONUTF8=1 python pipeline/run_full.py --topic humanoid --mode deploy

# 에이전트/CLI 읽기 전용 검색 — 기본 _cross, 빌드/파일 변경 없음
python pipeline/query_search_index.py --query "scientific discovery agents" --mode bm25 --json
python pipeline/query_search_index.py --topic humanoid --query "VLA action tokenization" --mode hybrid --json
# Python: from pipeline.api import query_search_index

# 검색 품질 회귀 — 고정 query vector, 네트워크 호출 없음
python pipeline/evaluate_retrieval.py \
  --queries pipeline/eval/retrieval_queries.jsonl \
  --vectors pipeline/eval/retrieval_query_vectors.json \
  --all --baseline pipeline/eval/retrieval_baseline.json \
  --min-recall-at-5 0 --strict \
  --output pipeline/eval/results/latest.json

# 실행 계획 미리보기 (변경 0)
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode curate --source web --dry-run
```

### 개별 스크립트 (디버깅·감사·복구)

```bash
# 오매칭 감사·복구
PYTHONUTF8=1 python pipeline/audit_matching.py --topic ai4s
PYTHONUTF8=1 python pipeline/fix_matching.py --topic ai4s --execute

# Zotero 중복 탐지·삭제
PYTHONUTF8=1 python pipeline/dedup_zotero.py --topic ai4s
PYTHONUTF8=1 python pipeline/dedup_zotero.py --topic ai4s --execute

# 빌드 검증 게이트 (--strict 면 이슈 시 exit 1)
PYTHONUTF8=1 python pipeline/validate_papers.py --topic ai4s --strict

# 분류만 단독 (UMAP transform + hdbscan.approximate_predict)
# 사전 조건: topic_modeling 이 `_hdbscan_model.joblib` 번들을 미리 저장해 두었어야 함
PYTHONUTF8=1 python pipeline/classify_papers.py --topic ai4s
PYTHONUTF8=1 python pipeline/classify_papers.py --topic ai4s --slugs 088,1093 --dry-run

# Topic modeling (UMAP/hdbscan/sentence-transformers 의존 — 단일 py312 env 활성 상태)
PYTHONUTF8=1 python pipeline/topic_modeling.py --topic ai4s

# Cleanup stale files (dry-run / execute)
PYTHONUTF8=1 python pipeline/cleanup.py
PYTHONUTF8=1 python pipeline/cleanup.py --execute
```

### 안전 플래그 (run_full / run_update_force 공통)

- `--strict-pdf` — fuzzy 매칭 차단, ID(Zotero/DOI/arXiv)로만
- `--slugs A,B,C` — 특정 슬러그만 처리
- `--dry-run` — 실행 계획만 출력
- `--skip-dedup` / `--dedup-execute` — Zotero dedup preflight 제어
- `--insights` — 크로스카테고리 Research Insights 생성 opt-in (기본 Core 는 paper-connections 만)
- `--yes` — `--mode rebuild` 확인 게이트 우회

## Key Design Decisions

- **Bottom-up topic modeling**: `topic_modeling.py`는 BERTopic 대신 sklearn HDBSCAN + UMAP을 직접 사용. HDBSCAN fine-grained clustering → c-TF-IDF 키워드 추출 (Grootendorst 2022, 클러스터=1문서 tf × 클래스 idf) → Sonnet 배치 작명 → Sonnet 카테고리 그룹핑. `min_cluster_size`를 자동 조정하여 sub-topic 40~100개를 목표로 한다.
- **Multi-class classification**: Papers get 1 `primary_category` + 1-3 `all_categories`. The topic index shows cards under every matching category.
- **Whitelist .gitignore**: Everything is excluded by default (`*`), then only code + configs are whitelisted. Under `docs/` only `index.html` (landing redirect), `setup-guide.md`, and `.assetsignore` are tracked on master. All topic content (`docs/papers/`, `docs/humanoid/`, `docs/physical-ai/`, etc.) is gitignored — it lives locally and on Cloudflare, never on master. `wrangler deploy` uses `docs/` directly; `docs/.assetsignore` excludes ai4s/scisci and local caches from the Cloudflare upload.
- **Two themes**: `ai4s` uses red accent (#D63423), `scisci` uses blue (#2374D6). Theme selection flows through `review_to_html.py` and `build_topic_index.py`.
- **Figure extraction**: PyMuPDF renders pages containing "Figure N" / "Fig. N" at 3x zoom. Up to 5 figures per paper from pages 0-14.
- **Slug format**: `{NNN}_{Title_first_40_chars}` where NNN is zero-padded sequence number.
- **PDF-change auto-detect**: `run_update_force.py` 가 매 실행 시작 시 `_papers_index.json` 의 `pdf_path` 캐시와 디스크 mtime을 비교해 PDF가 review.md 보다 새 것이면 자동으로 `forced_slugs` 에 추가한다 (Zotero API 호출 0, 순수 stat). 캐시는 `find_pdf()` 성공 시 자동 적재되므로 처음 한 사이클을 돈 뒤부터 작동.
- **Subprocess timeouts (LLM steps)**: `run_step()` 에 박힌 wall-clock cap — `topic_modeling=3600s`, `extract_insights=14400s (4h)`, `generate_timelines=21600s (6h)`. 실제 토픽 크기(논문 수)에 맞춰 한 번 늘려 둠 — 한국망↔Anthropic 응답 변동성 + paper_connections 의 카테고리×배치 곱셈 비용을 흡수.
- **Anthropic SDK 안정화**: 모든 Anthropic client 는 `Anthropic(timeout=180.0, max_retries=4)` (streaming Opus 만 `timeout=600.0`). `generate_timelines.opus_streaming_call` 은 mid-stream `Connection reset` 을 5-회 exp backoff 로 자체 wrap (SDK 의 max_retries 가 stream 시작 후 끊김을 못 잡음). `fetch_zotero_items` 도 동일한 retry 로직 적용.
- **Zotero `attachments:` URI 핸들링**: `find_pdf()` priority 1 (Zotero children API) 에서 `attachments:<filename>` 접두사를 `ZOTERO_DIR/<filename>` 으로 해석. Zotero 의 "Linked Attachment Base Directory" 설정을 따른다.

## External Dependencies

- **Zotero Web API**: Collection names and API key are configured in `config.json`
- **Anthropic API**: Claude Haiku/Sonnet for classification, reviews, summaries, and insights (`ANTHROPIC_API_KEY` env var). Deep Research UI도 같은 키를 사용 — 빌드 시 환경변수에서 읽어 HTML에 주입.
- **Google Gemini API**: Figure validation in `pipeline/run_update_force.py`, TTS for Audio Overview, and **Deep Research embeddings** — `gemini-embedding-001` (`output_dimensionality=768`, `task_type=RETRIEVAL_DOCUMENT` for the index in `pipeline/build_search_index.py`, `RETRIEVAL_QUERY` for queries). Query embeddings are served to readers by the worker `/api/embed` route (deployed) or `pipeline/serve_local.py` (local), so readers need no key for retrieval. Key from `GOOGLE_API_KEY` env var or `config.json`. **Gotcha**: non-3072 dims come back non-normalized — L2-normalize before int8 quantization.
- **OpenAI API (optional)**: reader BYOK answer generation + `extract_insights` cross-category fallback. No longer required for the search index. Key from `OPENAI_API_KEY` env var or the `openai_api_key` field in `config.json`.
- **PyMuPDF (fitz)**: PDF text extraction and figure rendering
- **Pillow**: PNG→WebP conversion in `pipeline/prepare_deploy.py`
- **Zotero PDF storage**: `config.json` 의 `zotero.pdf_dir`. 같은 라이브러리를 여러 머신에서
  쓰면 경로가 다르므로 `get_zotero_dir()` 이 순서대로 해결한다 —
  ① `ZOTERO_DIR` 환경변수 → ② `zotero.pdf_dir_by_host[<hostname>]` (짧은 호스트명, 대소문자·
  `.local` 무시) → ③ `zotero.pdf_dir_candidates` 중 **실제로 존재하는** 첫 경로 → ④ `zotero.pdf_dir`.
  Zotero 의 `linked_file` 첨부는 **만들어진 머신의 절대경로**를 그대로 들고 있어서
  (`C:\\Users\\jehyu\\GoogleDrive\\Zotero\\...`), 경로를 하나로 박으면 다른 머신에서 1,025편이
  "파일 없음" 이 된다. `audit_zotero_pdf.resolve_pdf_path` 가 두 구분자 모두에서 파일명을 잘라
  로컬 디렉토리에서 찾는다.

### 저자↔기관 정확도는 교차 검증으로 못 잰다 (2026-08-13 측정)

OpenAlex 기탁 소속과 PDF 파서 결과를 비교해 일치율을 내려 했으나 **지표로
쓸 수 없다.** 335쌍에서 0%, 상위 관계까지 펼쳐 1,017쌍에서 1.7% 가 나왔는데
둘 다 오류가 아니라 **겸직과 입도 차이**였다.

```
Ming Y. Lu   OpenAlex: Brigham and Women's Hospital, Mass General, MIT
             PDF     : Broad Institute, Harvard Medical School      ← 양쪽 다 맞음

Gang Huang   OpenAlex: Peking University
             PDF     : National Key Laboratory of Data Space …      ← 후자가 전자 산하
```

- 한 저자가 여러 기관에 속하는 게 정상이고, 두 출처가 **서로 다른 소속을 골라**
  기록해도 불일치로 셈된다
- 상위 관계로 펼쳐도 `parent_name` 이 3,526곳 중 588곳에만 있어 대부분 해결 안 됨

**`check_attribution_accuracy.py` 는 일치율을 내지 않는다.** 두 출처가 완전히
다른 기관을 말하는 쌍만 뽑아 **국가 불일치 순으로** 정렬해 사람이 볼 목록을
만든다 — `University of Hong Kong` vs `Massachusetts Institute of Technology`
같은 건 겸직이 아니라 한쪽의 오류다.

**정확도는 표본 수동 검증으로만 확인된다.** 지금까지의 실측:

|검증|결과|
|---|---|
|LLM 판독 vs 마커 파서 (30편, 70쌍)|88.6% 일치, 불일치 8건 중 2건은 파서가 틀림|
|`shared-byline` 수동 검토 (16편)|4편 오류 발견 → 규칙 수정|
|라벨↔정식명 정합성 (13,208건)|불일치 368건(2.79%), 다수는 번역·정식명 오탐|

### 저자↔기관 파서를 고칠 때 반드시 회귀를 먼저 잰다

`pipeline/check_attribution_regression.py --snapshot` → 수정 → `--compare`.
논문 단위로 "어느 파서가 이 논문을 푸는가"를 기록하므로, 총계로는 보이지 않는
교환(신규 N편 / 손실 N편)이 드러난다. 손실이 있으면 exit 2.

이 절차가 실제로 막은 것들:

|시도|결과|
|---|---|
|마커 알파벳을 발견된 문자로만 제한|회귀 330|
|소속 블록을 고정 기호 집합으로 파싱|회귀 125|
|문서 각주가 지명한 알파벳을 무조건 신뢰|회귀 11|
|`looks_like_affiliation` 에 200자 상한|회귀 116 · 신규 23|
|`extract_header` 줄번호 가드를 ROR 기반으로 교체|회귀 1 · 목표 논문 미해결 → 되돌림|
|**후행 기호 마커(`MIT†`) + 전원 공통 기호(`■`) 무시**|**회귀 5 · 신규 0 → 되돌림**|

마지막 항목은 형태 자체는 실재한다(`MIT†`, `Google DeepMind‡`, `UC Berkeley§`).
그러나 대상 논문(`1455`, `1567`)은 그 수정으로도 끝까지 풀리지 않았고 — 블록을
읽어도 기관 행 대조에서 막힌다 — 대신 정상 동작하던 5편(`AutoGen`, `LIBERO`,
`Open Catalyst 2020` 등)이 깨졌다. **효과 0, 손실 5.**

### arXiv API 는 소속·DOI 보강에 쓰지 않는다 (2026-08-13 측정)

arXiv Atom API (`export.arxiv.org/api/query`) 를 저자 소속 또는 DOI 보강에
쓰자는 제안이 반복해서 나오는데, **둘 다 실측 결과 쓸 수 없다.**

|측정 대상|결과|
|---|---|
|`<arxiv:affiliation>` — 미해결 논문 56편|**0편 (0%)**, 저자 705명 중 0명|
|`<arxiv:affiliation>` — 코퍼스 무작위 150편|1편 (0.7%), 저자 1,642명 중 4명 (0.2%)|
|`<arxiv:doi>` — DOI 없는 arXiv 논문 805편 전수|**4편 (0.5%)**|

- **소속**: `<arxiv:affiliation>` 은 투고자가 제출 폼에 직접 입력해야만 채워지는
  선택 필드다. arXiv 는 PDF 에서 추출하지 않고 입력을 요구하지도 않는다.
  스키마에는 있지만 실제로는 거의 비어 있다.
- **DOI**: 805편 전수 조회에 **약 40분** 걸렸고 (한국망 429 로 5개 배치 실패,
  배치당 8초 대기 필수) 얻은 것은 4편이다. 비용 대비 가치가 없다.
- 저자별 소속이 실제로 필요하면 **Scopus (`authors.author[].affiliation`) 와
  OpenAlex (`authorships`)** 를 쓴다 — 둘 다 출판사 기탁 정보라 채워져 있다.
  전제 조건은 DOI 이고, DOI 보강은 `resolve_missing_dois.py` 의 제목 검색이
  담당한다 (2,374편 중 259편, 11%).

## 분야별 기관·연구자 분석 (Field leaders)

`python pipeline/report_field_leaders.py --topic ai4s --top 20`

**근거 등급을 반드시 구분한다.** 논문이 어떤 기관 소속을 달고 있다는 사실
(`paper_institutions`)은 그대로 세도 되지만, **저자를 그 기관 중 하나에 귀속**시키려면
바이라인 위첨자가 필요하다. 기관이 여럿인데 마커가 없으면 빌더는 저자×기관 전조합을
넣는다 — `paper_author_institutions` 의 86%(31,566/36,667)가 이 `pdf.unmarked-multi`
추정이다. 이걸로 기관별 연구자를 세면 **그 기관에 있던 적 없는 사람**이 상위에 올라온다.

리포트가 세는 링크는 셋뿐이다:

|source|의미|
|---|---|
|`openalex`|출판사가 기탁한 저자↔기관 매핑 (ROR 기반) — 가장 강함|
|`pdf.byline-marker`|위첨자가 실제로 해석된 것|
|`pdf.sole-affiliation`|기관이 하나뿐이라 모호함이 없는 것|

`--include-guessed` 를 주면 전조합까지 포함하되 리포트에 경고가 찍힌다.

**OpenAlex 보강** — `python pipeline/enrich_openalex_authorships.py --execute`
DOI 보유 논문에 대해 저자별 기관(ROR)·교신저자 플래그·OpenAlex 저자 ID·ORCID 를 가져와
`source='openalex'` 로 **기존 PDF 링크 옆에** 추가한다(덮어쓰지 않음). 이게 없으면
교신저자와 ORCID 는 DB 전체에서 0건이다.

**피인용** — `python pipeline/run_metrics.py` (기본 30일 증분).
`--quiet` 는 진행 출력을 끄고, 수집은 전량을 모은 뒤 일괄 기록하므로 중간에 파일이
늘지 않는다. DOI 가 있어야 조회되므로 상한은 DOI 보유 논문 수다(현재 1,812/4,196 = 43%).
리포트가 커버리지를 함께 출력하는 이유 — 일부만 수집된 피인용으로 순위를 매기면
**수집된 논문이 먼저 올라올 뿐**이다.

## paper-curio (Zotero 플러그인) — 두 번째 리뷰 생성기

소스: `/Users/jehyunlee/Documents/내노트북/01_Work/01_Devs/AX/paper-curio` (TypeScript, Zotero 플러그인).
앞으로 서지정보 DB 등록은 **실질적으로 이쪽을 통해 이루어진다**.

같은 Zotero 라이브러리와 같은 `docs/papers/{slug}/` 를 공유하며, `src/core/pipeline.ts` 가
text.md → figures → review.md → index.html → `_papers_index.json` 순으로 본체와 동일한 산출물을
쓴다. 무거운 단계는 `src/extract/pybridge.ts` 가 이 저장소의 py312 함수(`extract_text`,
`extract_figures`, `write_review`)를 직접 호출하고, 실패 시 TS(pdf.js/멀티프로바이더)로 폴백한다.
자기가 만든 항목은 Zotero item 의 `extra` 에 `papercurio: {slug};{date}` 마커를 남긴다 —
출처 판별은 이 마커가 유일하게 확실한 신호다(슬러그 대소문자는 정황 증거일 뿐).

**서지 DB 등록 완성도** (`pipeline/audit_ingest_inputs.py` 로 실측, papercurio 224편 vs 본체 3,972편):

|지표|papercurio|본체|
|---|---|---|
|`source_documents(text)` 보유|78.1%|100%|
|저자↔기관 링크|70.1%|79.2%|
|기관 링크|82.1%|84.0%|
|`scopus-unconfirmed` 소속|22.8%|8.0%|
|`zotero_item_key` 누락|0편|44편|

- text.md 가 없는 49편 중 **40편은 Zotero 에 PDF 자체가 없다** — 추출할 원문이 없으니 본체도 동일하게
  비운다. papercurio 결함이 아니다. 나머지 10편은 PDF 가 리뷰 생성 **이후** 첨부된 경우다.
- `scopus-unconfirmed` 가 2.8배 높은 건 위 결과다: 대조할 본문이 없으면 Scopus 소속을 확인할 수 없어
  신뢰도 0.95(`scopus+pdf`) 로 승격되지 못한다.
- **유일하게 papercurio 가 쓰지 않는 산출물은 `bibliography.json` 사이드카**다. 이게 없으면
  `build_bibliography_db.py` 가 매 빌드마다 Zotero 라이브러리 전체를 페이징한다(~200초, 실패 시
  `zotero_item_key` 조용히 유실). 본체는 리뷰 생성 시 이 파일을 남긴다.

**PDF 를 나중에 붙일 때 주의**: 아이템의 `url` 을 눌러 받은 PDF 는 그 url 이 가리키는 논문이지 그
아이템의 논문이 아닐 수 있고, Zotmoov 가 파일명을 **아이템 제목으로 자동 변경**하므로 파일명으로는
절대 판별할 수 없다. 본문 텍스트로 확인해야 한다 —
`python pipeline/inspect_zotero_item.py --keys <KEY> --check-pdf`.

