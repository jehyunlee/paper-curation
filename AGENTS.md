# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

## Project Overview

Academic paper curation pipeline. Papers are fetched from Zotero, reviewed via Codex/Gemini APIs, classified into categories, and published as a searchable HTML index with per-paper review pages. Topic pages also expose a **Deep Research UI** that performs client-side RAG against a pre-built embedding index (Google `gemini-embedding-001`, 768d int8, task-typed) and streams Codex answers with `[ref:N]` citations and inline figures. Retrieval is hybrid BM25+dense fused with RRF and LLM re-ranked; query embeddings are computed for the reader by the worker `/api/embed` route (deployed) or `pipeline/serve_local.py` (local), so readers need no API key for retrieval — keys (BYOK) are only for answer generation.

- **Topics**: Configured per-user in `config.json` (e.g., `ai4s`, `scisci`, `bioml`). Per-topic Core-1 search keywords are configurable via the `search_keywords` block (`{topic: {primary: [...], secondary: [...]}}`); `ai4s`/`scisci` ship built-in defaults, so new topics add their own there.
- **Deploy architecture** (split hosting):
  - **Cloudflare Workers (Static Assets + Functions)** serves the full content at the custom domain `paper-curation.jehyunlee.dev` (the `CF_BASE_URL` constant in `prepare_deploy.py`, provisioned via the `[[routes]]` block in `wrangler.toml`; the default `*.workers.dev` URL also resolves but is not the canonical one). `pipeline/prepare_deploy.py` runs `npx wrangler deploy` (token via `CLOUDFLARE_API_TOKEN`/`CF_API_TOKEN` + `CLOUDFLARE_ACCOUNT_ID`). Uploads everything under `docs/` except entries in `docs/.assetsignore` (ai4s/scisci are local-only). `worker/index.js` exposes two routes that need wrangler secrets (`wrangler secret put`): `/api/embed` (Deep Research query embeddings — `GOOGLE_API_KEY`) and `/api/audio-email` (Audio Overview email — `RESEND_API_KEY`).
  - **GitHub `gh-pages` branch** holds tiny redirect stubs only — one `{topic}/index.html` per deployable topic that `meta refresh` + `window.location.replace()` to the Cloudflare URL. Synced idempotently by `prepare_deploy.py`.
  - **GitHub `master` branch** holds only code, `config.example.json`, `wrangler.toml`, and `docs/.assetsignore`. `docs/papers/`, `docs/humanoid/`, `docs/physical-ai/`, etc. are `.gitignore`'d to keep the repo small (full content lives only on Cloudflare + local).
  - User access: `jehyunlee.github.io/paper-curation/{topic}/` → gh-pages stub → Cloudflare URL → full content.
- **Language**: All reviews are written in Korean with technical terms in English

## Installation Flow (Codex)

사용자가 "여기에 paper-curation을 설치해줘: https://github.com/jehyunlee/paper-curation" 같은 요청을 하면, 아래 순서대로 진행한다.

### Step 1: Clone & Dependencies
```bash
git clone https://github.com/jehyunlee/paper-curation.git
cd paper-curation
pip install anthropic google-genai pymupdf Pillow requests opendataloader-pdf
```

### Step 2: config.json 생성
사용자에게 아래 정보를 **하나씩 질문**하고 config.json을 생성한다:
1. **Zotero API Key** — 환경변수 `ZOTERO_API_KEY`가 있으면 자동 사용, 없으면 질문
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
- [6/6] SKILL.md를 `~/.Codex/skills/paper-curation/` 에 설치
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
|Tool|`pipeline/run_citedby.py`|**Citedby** — DOI 하나로 인용논문 수집(OpenAlex·Scopus·S2·arXiv) → 독창성 추출 → 주제 필터 + 5W1H 요약 → **자기완결 HTML 문서** + CSV. 브라우저 [PDF 출력] 버튼으로 링크 살아있는 PDF. 내 Zotero 라이브러리에 있는 논문은 `zotero://open-pdf` 바로열기 링크. 코어는 `pipeline/lib/citedby/`|
|Tool|`pipeline/run_metrics.py`|**Metrics** — 코퍼스 논문의 피인용수·레퍼런스 수집 → `docs/papers/{slug}/citations.md`(피인용 **이력** 누적 + 임계값 10회 이상이면 인용논문 목록) + `references.md`(DOI>URL>서지 순 표기). 기본 30일 증분. 피인용수는 소스별 보존(Scopus·Crossref·OpenAlex) + OpenAlex 연차보정 백분위. 코어는 `pipeline/lib/metrics/`|

Step 0 scripts are for full/update modes only (skipped in --local). Step 1 is the heavy batch (default `--concurrency 16`, Tier 4 — see README "Concurrency 가이드"). Wall-clock is ~20~30분 for ~80 papers at concurrency 16; ~1.5h at 4 (Tier 1 보수값).

### Optional Step 0 boost: scholar-megasearch

`pipeline/search_papers.py` 는 arXiv + Semantic Scholar + OpenAlex 3개 소스만 본다. **신규 토픽 첫 build** 나 **분야가 넓어 단일 인덱스 누락이 우려되는 주간 사이클** 에는 [scholar-megasearch](https://github.com/TaewoooPark/scholar-megasearch) 스킬을 Step 0 대안으로 쓸 수 있다 — 20+ DB (Crossref / PubMed / bioRxiv / medRxiv / DOAJ / CORE / BASE / OpenAIRE / Zenodo / Unpaywall / HAL / DBLP / IACR / SSRN / Europe PMC + arXiv / S2 / OpenAlex) fan-out → DOI/arXiv/title30 dedup with provenance → corroboration ranking → OA PDF 다운로드까지 한 번에. 한국 망 arXiv 429 도 자동 fallback.

| Step | Script | Purpose |
|------|--------|---------|
| 0-mega | scholar-megasearch (skill) | 20+ DB fan-out → `literature_search/<topic>_<date>/corpus.json` + `pdfs/manifest.json` |
| 0-mega | `pipeline/megasearch_to_zotero.py` | corpus → `_search_results.json` 변환 + `_papers_index.json` cross-dedup (이미 리뷰한 논문 자동 제외) + 받아둔 PDF 를 Zotero PDF 디렉토리로 pre-stage |

연결 패턴:

```bash
# 1) Codex 안에서 스킬 실행 (예: bioml 토픽 첫 build)
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

**MCP 의존성**: `~/.Codex.json` 의 `mcpServers` 에 `arxiv-mcp-server` / `asta` / `paper-search-mcp` 가 등록돼 있어야 함 (`scholar-megasearch/setup/install.sh` 가 자동 등록). `uv` 가 없으면 arxiv-mcp-server 만 비활성 (paper-search-mcp 가 arXiv 도 커버하므로 운영에는 영향 없음).

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

## Common Commands

All scripts require `PYTHONUTF8=1` on Windows to avoid cp949 encoding issues. Single entrypoint is `pipeline/run_full.py` (3축: `--mode/--source/--images`); 개별 스크립트는 디버깅·복구용으로만 직접 호출.

```bash
# 주간 운영 — 검색 + Zotero 등록 + sync + 신규 리뷰
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode curate --source web --days 7

# 로컬 업데이트 — 검색 스킵, sync만
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode curate --source zotero

# 특정 슬러그만 force-rebuild (감사·복구 시)
#   주의: --mode rebuild 는 토픽 전체의 categorization/insights/timelines 까지 재생성한다 (수 시간, API 비용 ↑).
#   PDF 한 편 교체 후 review.md만 갱신하고 싶으면 다음 패턴이 가볍다:
#     rm docs/papers/{NNN}_*/review.md
#     python pipeline/run_full.py --topic ai4s --mode curate --source zotero --skip-dedup
#   (이후 분류 영향까지 반영하려면 --mode reclassify 별도 실행)
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
- **Anthropic API**: Codex Haiku/Sonnet for classification, reviews, summaries, and insights (`ANTHROPIC_API_KEY` env var). Deep Research UI도 같은 키를 사용 — 빌드 시 환경변수에서 읽어 HTML에 주입.
- **Google Gemini API**: Figure validation in `pipeline/run_update_force.py`, TTS for Audio Overview, and **Deep Research embeddings** — `gemini-embedding-001` (`output_dimensionality=768`, `task_type=RETRIEVAL_DOCUMENT` for the index in `pipeline/build_search_index.py`, `RETRIEVAL_QUERY` for queries). Query embeddings are served to readers by the worker `/api/embed` route (deployed) or `pipeline/serve_local.py` (local), so readers need no key for retrieval. Key from `GOOGLE_API_KEY` env var or `config.json`. **Gotcha**: non-3072 dims come back non-normalized — L2-normalize before int8 quantization.
- **OpenAI API (optional)**: reader BYOK answer generation + `extract_insights` cross-category fallback. No longer required for the search index. Key from `OPENAI_API_KEY` env var or the `openai_api_key` field in `config.json`.
- **PyMuPDF (fitz)**: PDF text extraction and figure rendering
- **Pillow**: PNG→WebP conversion in `pipeline/prepare_deploy.py`
- **Zotero PDF storage**: Path configured in `config.json` (`zotero.pdf_dir`)
