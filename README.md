# Paper Curation

**키 없이 설치하고, 단일 PDF 리뷰부터 전체 큐레이션까지 필요한 범위만 명시적으로 실행합니다.**

논문 PDF → 한국어 구조화 리뷰 → 자동 분류 → 연구 동향 타임라인 → 검색 가능한 사이트 + **Deep Research**(논문 근거 RAG Q&A)까지 — Claude Code가 오케스트레이션하는 개인 논문 큐레이션 파이프라인.

**라이브 데모 — 설치 없이 바로 보기:**

- **Humanoid** — https://paper-curation.jehyunlee.dev/humanoid/
- **Physical AI** — https://paper-curation.jehyunlee.dev/physical-ai/

**세 가지 경로 — 필요한 범위만 고르고, 계획을 확인한 뒤 실행합니다:**

![세 가지 사용 경로](usage_workflow.png)

| 경로 | 무엇을 | 필요한 것 | 어디에서 |
|------|--------|-----------|----------|
| **Read** | 생성된 리뷰·검색·타임라인 열람, 공개 기관표·보고서 내보내기 | 키 없음 | 웹 사이트 · Zotero 우클릭 **Review HTML 열기** · 기능 모듈 |
| **AI** | PDF 리뷰, 근거 기반 요약·질의·비교, AI Chat | 선택한 제공자 하나 (Anthropic 기본 / OpenAI / Google, 요약·질의는 로컬 Ollama 가능) | Zotero 우클릭 **Review 생성** · **Paper Curation 기능 모듈** · CLI |
| **Collection** | 검색 색인·지표·서지 DB·오디오·타임라인, Zotero 동기화·배포·이메일, 컬렉션 전체 처리 | 기능별 요구조건, 명시적 확인 | 기능 모듈 **컬렉션 관리 / 선택 기능** 탭 · `run_feature.py` · `run_full.py` |

모든 작업은 **계획(요구조건·전송 대상·비용) → 확인 → 실행** 순서이며, 리뷰 하나가
분류·색인·타임라인·배포를 자동으로 끌고 가지 않습니다. 실패해도 다른 제공자로
자동 전송하지 않고, API 키는 설정 파일이 아닌 **OS 키 저장소**에 둡니다.

📘 **[활용 매뉴얼](docs/user-guide.md)** — 어디에서 무엇을 설정하고 어떻게 동작시키는지 단계별 안내
(설치·연결 → 키 저장 → 리뷰 → 모듈 → 상태 메시지 읽는 법). Zotero 플러그인 Curio와 CLI는
같은 기능 레지스트리를 사용하며, 기능 ID·요구조건 표는
[Setup Guide의 생성 영역](docs/setup-guide.md#공유-기능-레지스트리)이 기준입니다.

🇬🇧 [English README](README.en.md)

<details>
<summary>🐱 전체 큐레이션(Collection 경로) 파이프라인 한 장 — 수집부터 배포까지</summary>

![Paper Curation 전체 파이프라인](workflow.png)

</details>

> 📚 **[서지 확정 — 누가 어디 소속인가](docs/attribution.md)** — 논문의 저자를
> 기관에 귀속시키는 과정, 왜 LLM 을 마지막에 두는지, 저자 신원을 어떻게
> 정하는지를 따로 정리했습니다.

## 목차

- [📘 활용 매뉴얼](docs/user-guide.md) — 설정 위치와 단계별 동작법
- [📖 독자로 둘러보기](#-독자로-둘러보기)
- [🔧 운영자로 설치하기](#-운영자로-설치하기)
- [💰 비용 가이드](#-비용-가이드)
- [기능](#기능)
- [파이프라인](#파이프라인)
- [사용 모드](#사용-모드)
- [서지 확정](docs/attribution.md) — 저자↔기관 귀속, 근거 등급, 검증
- [문서](#문서) — Setup / Operations(megasearch · 한국 망 우회 · Concurrency) / Architecture
- [발표/참고자료](#발표참고자료)

## 📖 독자로 둘러보기

설치도, API 키도 필요 없습니다. 위 라이브 데모 링크를 열면 바로 열람할 수 있습니다.

- **웹에서 보기** — [Humanoid](https://paper-curation.jehyunlee.dev/humanoid/) · [Physical AI](https://paper-curation.jehyunlee.dev/physical-ai/). 카테고리별 카드, 검색, 타임라인, 논문별 한국어 리뷰 페이지가 모두 정적으로 제공됩니다.
- **Deep Research 사용법** — 토픽 페이지 상단의 검색창에 자연어로 질문하면 됩니다. **검색(retrieval)은 키가 전혀 필요 없습니다** — 질의 임베딩은 서버(worker `/api/embed`)가 대신 계산합니다. 답변 생성만 본인 API 키(BYOK)를 브라우저에 입력하면 되며, 입력한 키의 제공자 하나로만 근거 답변을 스트리밍합니다(다른 제공자로 자동 전송 없음). 코퍼스 밖 최신 정보가 필요하면 **웹 검색 토글**을 켜 인라인 링크 인용으로 보강할 수 있습니다.
- **RSS 구독** — 각 토픽은 Atom 피드를 제공합니다: [Humanoid feed](https://paper-curation.jehyunlee.dev/humanoid/feed.xml) · [Physical AI feed](https://paper-curation.jehyunlee.dev/physical-ai/feed.xml). 리더로 구독하면 새로 추가되는 리뷰를 받아볼 수 있습니다.

## 🔧 운영자로 설치하기

기본 설치에는 API 키나 Zotero 컬렉션이 필요하지 않습니다. `setup.py`는 완전
비대화형으로 최소 `config.json`과 `docs/papers/`를 만들며, 키를 묻거나
`config.json`에 복사하지 않고 전체 파이프라인도 자동 실행하지 않습니다.

**가장 쉬운 방법 — Claude Code에서 한 줄** (전체 설치 플로우는 [CLAUDE.md](CLAUDE.md)의 "Installation Flow (Claude Code)" 참고):

> "여기에 paper-curation을 설치해줘: https://github.com/jehyunlee/paper-curation"

**수동 설치:**

```bash
# 1) 클론 + 의존성 (단일 conda env: py312)
git clone https://github.com/jehyunlee/paper-curation.git && cd paper-curation
conda create -n py312 -c conda-forge python=3.12 pip -y && conda activate py312
pip install -r requirements.txt

# 2) 키 없는 로컬 config + SKILL 생성/설치 (파이프라인은 실행하지 않음)
PYTHONUTF8=1 python pipeline/setup.py

# 기능 목록과 요청 계획(쓰기 없음)
python pipeline/run_feature.py --list
python pipeline/run_feature.py --request feature-request.json
```

기본 설치는 keyless입니다. 키는 설정 파일에 저장하지 않습니다. 환경변수가 있으면
OS keyring보다 우선하며, 없으면 `credential:<provider>` 참조가 OS keyring
서비스 `paper-curation`의 비밀값을 가리킵니다. 평문·null·실패 backend는
거부되고 평문 config/file fallback은 없습니다. 키를 argv·요청 JSON·로그에 넣지
마세요. 안전한 저장 예시는 Setup Guide의 credentials 절을 참고하세요.

`--no-install`은 SKILL 설치만 건너뜁니다. setup은 PaperBanana를 클론하거나
클러스터링을 시험하거나 첫 전체 실행을 시작하지 않습니다. 전체
`run_full.py --mode curate`는 Zotero·Anthropic·Google 등 해당 워크플로의
환경변수와 설정을 준비한 뒤 별도로 실행합니다. 배포/이메일도 별도 옵션입니다.

### Zotero에서 시작하기 (Paper Curio)

1. [Paper Curio 최신 릴리스](https://github.com/jehyunlee/paper-curio/releases/latest)에서 **사용 중인 Zotero 버전에 맞는 XPI**를 받아 Zotero **Tools → Plugins**에서 설치합니다 — Zotero 10은 `paper-curio-zotero10.xpi`, Zotero 9(7·8 포함)는 `paper-curio-zotero9.xpi`. 릴리스마다 두 파일이 함께 나오며 기능은 동일합니다.
2. Zotero **Settings → Paper Curio → 출력 위치**에 위 체크아웃 경로를 넣습니다(Python 경로는 비우면 `py312`).
3. **Settings → Paper Curio → API 키**에서 리뷰 제공자 하나를 고르고 키를 **OS 키 저장소에 저장**합니다.
4. 논문 항목 우클릭 → **paper-curation Review 생성** → 계획 확인 → 실행. 요약·질의·비교 등은 우클릭 **Paper Curation 기능 모듈**에서 같은 방식으로 실행합니다.

화면별 설정 항목과 상태 메시지 해석은 **[활용 매뉴얼](docs/user-guide.md)** 을 따릅니다.

### 명령줄에서 시작하기

CLI는 [Setup Guide의 PDF 요청 예시](docs/setup-guide.md#단일-pdf-로컬-리뷰)를
`review-request.json`으로 저장한 뒤 실행합니다.

```bash
python pipeline/local_review.py --request review-request.json            # 계획만
python pipeline/local_review.py --request review-request.json --execute  # 확인 후 실행
```

`run_feature.py --request`도 **JSON 파일 경로**를 받습니다. 기능별 입력과 전송 대상은
[레지스트리에서 생성한 기능표](docs/setup-guide.md#공유-기능-레지스트리)를 확인하세요.

기본 리뷰는 Anthropic Sonnet 5이며 자동 fallback이 없습니다. OpenAI와 Google은
명시적으로 고르는 provider입니다. Ollama `qwen3.8:27b-mlx`는 요약·대화 전용이며
리뷰 대체가 아닙니다. `provider`, `credential_ref`, `budget`은 요청에서 선택할
수 있고, 예산의 알 수 없는 요율 또는 상한 초과는 실행을 막습니다. 요청 계획을
먼저 확인한 뒤에만 `--execute`를 붙이세요.

기관·서지 DB 갱신은 `bibliography-update`의 별도 로컬 단계입니다. 기본은 변경분만
ingest하며, `--changed-only --skip-zotero --offline --no-email`로 외부 동기화,
온라인 보강, 이메일 없이 실행합니다. 온라인 보강은 선택 사항입니다.

사전 준비 체크리스트, config.json 스키마, 설치 확인, 문제 해결 → **[Setup Guide](docs/setup-guide.md)**

## 💰 비용 가이드

> 정확한 실측이 아니라 **오더 오브 매그니튜드(order-of-magnitude) 가이드**입니다. 실제 비용은 논문 편수·본문 길이·타임라인 재생성 빈도·Insights opt-in 여부에 따라 크게 달라집니다.

단계별로 쓰이는 모델과 단가(입력/출력, 100만 토큰당):

| 단계 | 모델 | 단가 (입력 / 출력) |
|------|------|------|
| 리뷰 기본 제공자 · 인사이트 | `claude-sonnet-5` | $2 / $10 (인트로, ~2026-08-31) → $3 / $15 |
| 연결 선택·관계·이유 생성 | SPECTER2/BM25 후보 + 메타데이터 규칙 | 이 단계의 LLM 호출 없음 |
| Figure 검증 (vision judge) | `claude-haiku-4-5` | $1 / $5 |
| 타임라인 내러티브 | `claude-opus-5` (5) | $5 / $25 |
| 분류 | — (HDBSCAN + UMAP) | **LLM 호출 0회 → $0** |
| 검색 임베딩 | Google `gemini-embedding-001` | Google 임베딩 요금(소액) |

**편당 리뷰 대략치** — 리뷰 1편은 논문 본문 발췌 + 프롬프트를 입력, 6섹션 한국어 리뷰를 출력합니다. 대략 입력 ~15k · 출력 ~4k 토큰으로 잡으면:

- 인트로 단가($2/$10): `15k × $2/1M + 4k × $10/1M ≈ $0.03 + $0.04 = ~$0.07`
- 9/1 이후($3/$15): `15k × $3/1M + 4k × $15/1M ≈ $0.045 + $0.06 = ~$0.11`
- 여기에 연결 생성(증분) + Figure 검증(Haiku)까지 얹으면 **편당 대략 $0.05–0.15** 수준입니다.

**월간 운영 대략치** — 주간 ~20편(월 ~80편) 사이클 기준:

- 리뷰: 80편 × ~$0.10 ≈ **$8**
- 연결(증분, dirty 논문만) + 카테고리 요약(Haiku) ≈ **$1–3**
- 타임라인(변경된 카테고리만, Opus, 비정기) ≈ **$1–3**
- **합계 ≈ 월 $10–20** 수준 (Insights opt-in `--insights` 또는 전체 타임라인 재생성 시 증가)

> **각주**: Sonnet 5 인트로 단가는 2026-08-31까지이며 **9/1 인트로 종료 후 재평가 예정**입니다. 분류 단계는 LLM을 전혀 호출하지 않으므로(HDBSCAN) 비용이 없습니다. Deep Research 답변 생성은 독자 BYOK라 운영자 비용에 포함되지 않습니다.

## 기능

**경로별 기능** — 각 기능은 독립적으로 요청하며, 기능 ID는 `pipeline/features.json`의 값입니다:

| 경로 | 기능 (ID) | 설명 |
|------|-----------|------|
| Read | 열람 · `institution-export` · `extract` | 생성된 리뷰·검색·타임라인 열람(키 없음), 공개 기관표 내보내기, 로컬 PDF 텍스트·그림 추출 |
| AI | **구조화 리뷰** `review` | PDF에서 텍스트/Figure 추출 → 선택한 제공자가 6개 섹션(Essence·Motivation·Achievement·How·Originality·Evaluation) 한국어 리뷰 작성 → HTML + 서지 사이드카 |
| AI | `summary` · `chat` · `comparison` | 선택한 PDF 본문만 근거로 **원문 인용이 붙은 주장**을 생성. 인용을 찾을 수 없는 답변은 거부. 요약·질의는 로컬 Ollama 가능 |
| AI | **AI Chat / Citedby** | PDF와 멀티턴 대화, 인용 계보 분석 — Zotero 플러그인의 기존 기능 |
| Collection | `keyword-search` · `semantic-search` | BM25 색인·조회(키 없음) / Gemini 임베딩 hybrid 색인·조회(Google 키) |
| Collection | `metrics` · `bibliography-update` | 피인용·레퍼런스 누적, 서지 DB·기관 귀속 반영(기본 offline) |
| Collection | `audio` · `timeline-text` · `timeline-image` | 기존 리뷰의 팟캐스트형 MP3(Gemini TTS), 카테고리 내러티브, PaperBanana 타임라인 그림 — 각각 따로 |
| Collection | `zotero-sync` · `publish` · `email` | 원격 삭제 동기화(dry-run 기본), Cloudflare 배포, 기존 MP3 전달 — **모두 명시적 확인 필수** |

**전체 큐레이션(고급)** — `run_full.py --mode curate`가 아래를 순서대로 실행합니다. 리뷰 하나로는 실행되지 않습니다:

| 기능 | 설명 |
|------|------|
| **자동 분류** | Bottom-up 토픽 모델링(SPECTER2 + HDBSCAN + UMAP)으로 카테고리 자동 생성·배정 — LLM 호출 0회 |
| **같이 보면 좋은 논문** | `topic_modeling.py`와 `extract_insights.py`는 SPECTER2 dense + 제목·저자 BM25를 RRF로 융합하고 동일한 결정론적 builder로 관계 유형과 한국어 이유를 생성합니다. 연결 단계는 LLM을 호출하지 않으며, 관계는 메타데이터 기반 휴리스틱이지 인용·인과관계의 확정 판정이 아닙니다. |
| **Deep Research** | 자연어 질의 → hybrid 검색(BM25+dense) → 독자 BYOK 제공자의 답변 + `[N]` 인용 |
| **타임라인** | 카테고리별 연구 동향 내러티브 + 다이어그램(PaperBanana) + main research timeline |
| **지식 축적** | Obsidian 연동 — 메모가 다음 질의에 반영되는 compounding knowledge |
| **논문 검색/등록** | arXiv·Semantic Scholar·OpenAlex 병렬 검색 + Zotero 자동 등록(선택) |

**전체 큐레이션 옵션** — 플래그/모드로 켤 때만:

| 옵션 | 켜는 법 | 설명 |
|------|---------|------|
| **콘텐츠 배포 (O-1)** | `--mode deploy` 또는 기능 `publish` | Cloudflare Workers + gh-pages 스텁 — [운영 매뉴얼](docs/operations.md#deploy-option-o-1). Audio 이메일은 별도 `email` 기능 |
| **Insights + 네트워크 (O-2)** | `--insights` | 크로스카테고리 인사이트 + UMAP 2D/3D 인터랙티브 네트워크 재생성 |
| **워크플로 다이어그램** | `generate_usage_diagram.py` · `generate_workflow.py` | 사용 경로 그림(matplotlib, 키 없음) · 상단 고양이 다이어그램(PaperBanana, `--style cat/fairy/academic`) |

**전체 curate 워크플로 요구사항**: Zotero 컬렉션 + PDF와 자격증명
`ZOTERO_API_KEY`, `ANTHROPIC_API_KEY`, `GOOGLE_API_KEY`(환경변수 또는 OS 키 저장소의
`credential:<provider>`). OpenAI는 Chat/Deep Research 등의 선택 경로용입니다.

## 파이프라인

`run_full.py` 한 줄이 아래 Core 단계를 순서대로 실행합니다 (위 그림이 전체 흐름):

1. **데이터 수집** — Zotero PDF → `text.md` + `figures/` (선택: arXiv·S2·OpenAlex 검색 후 Zotero 등록)
2. **구조화 리뷰** — Claude가 6섹션 한국어 `review.md`
3. **피인용·레퍼런스** — `citations.md`(이력 누적) + `references.md`. 기본 30일 증분, 외부 API 장애가 파이프라인을 죽이지 않는 soft step(`--skip-metrics`)
4. **토픽 모델링 + 분류** — SPECTER2 + HDBSCAN + UMAP로 카테고리 자동 생성·배정
5. **같이 보면 좋은 논문** — SPECTER2 코사인 + 제목·저자 BM25를 RRF로 융합해 후보를 정렬하고, `lib.related.build_connections`가 순위와 기록된 메타데이터로 연결을 생성합니다. 전체 실행의 `extract_insights.py`도 동일한 builder를 사용합니다.
6. **카테고리 요약 + 타임라인 내러티브/main·category 다이어그램** & **Deep Research 검색 인덱스**(BM25 + Gemini 임베딩)
7. **토픽 인덱스** `index.html`(Deep Research·Audio Overview 내장) → **로컬 열람**(`serve_local.py`) 또는 **배포**

**브라우저 안에서**: Deep Research(키 자동 감지)와 Audio Overview(Gemini TTS → MP3)가 동작합니다.
**Option 분기**: `--insights`(크로스카테고리 인사이트 + 네트워크) · `--mode deploy`(Cloudflare + gh-pages).

## Citedby — 한 논문에서 시작하는 인용 계보 분석

DOI 또는 로컬 리뷰 논문을 기준으로 OpenAlex·Scopus·Semantic Scholar·arXiv에서
인용논문을 수집하고, 시간에 따른 연구 흐름을 자기완결 HTML 보고서로 만듭니다.

```bash
PYTHONUTF8=1 python pipeline/run_citedby.py \
  --doi 10.xxxx/xxxxx \
  --pdf-first --build-index --serve --open
```

- **인용 흐름 타임라인** — 연구 주제의 생성·소멸·분기·융합, turning-point 논문,
  주요 연구 그룹을 2–3단락의 종합 narrative와 stream별 설명으로 정리
- **PaperBanana 시각화** — 타임라인 그림과 narrative를 기본 생성
  (`--no-timeline`으로 생략)
- **PDF-first 근거 등급** — 기존 corpus 리뷰 > Zotero 보유 PDF 전문 > 초록 > 제목
- **Deep(er) Research** — BM25+dense hybrid retrieval, 답변 계획, related-paper 탐색,
  선택적 웹 검색, streaming 답변 및 `[ref:N]` 인용
- **Corpus 우선 identity 통합** — 웹 검색 결과가 corpus 논문과 DOI·arXiv·제목으로
  일치하면 외부 자료를 중복 인용하지 않고 기존 corpus reference를 사용
- **문맥별 링크** — 로컬 HTML은 corpus review HTML, PDF는 DOI·arXiv·원문 URL,
  Obsidian은 `papers/{slug}/review.md` 또는 citedby evidence note로 연결
- **독립 출력** — Citedby 보고서와 Deep(er) Research 답변 각각
  PDF·Markdown·Obsidian·Audio Overview 지원
- **로컬 서버 열람** — `--serve --open`으로 `file://` 대신
  `http://localhost:8000/...`을 열어 embedding·streaming·Audio API를 바로 사용


**CLI/에이전트 검색** — 인덱스를 재빌드하지 않는 읽기 전용 질의 경로:
```bash
# Google 없이 키워드 인덱스 구축 (기존 리뷰/논문 목록 필요)
python pipeline/build_search_index.py --topic my_topic --mode bm25
python pipeline/query_search_index.py --topic my_topic --query "과학적 발견 자동화" --mode bm25 --json

# 통합 컬렉션(_cross), API 키 없이 BM25
python pipeline/query_search_index.py --query "과학적 발견 자동화" --mode bm25

# Gemini 질의 임베딩 + BM25 RRF, 구조화 JSON 출력
python pipeline/query_search_index.py --topic humanoid --query "VLA action tokenization" --json
```
기본 컬렉션은 `_cross`이며 `hybrid`·`dense`·`bm25`를 지원합니다. Python에서는
`pipeline.api.query_search_index()`를 호출합니다. 질의는 인덱스를 변경하지 않으며,
curate/rebuild가 인덱스를 갱신하고 deploy preflight가 fingerprint freshness를 확인합니다.
구축은 `pipeline.api.build_search_index(..., mode="bm25")`입니다. 구축을 뜻하던
모호한 `pipeline.api.search_index` 호환 별칭은 제거했습니다.

`build_search_index.py --mode bm25`는 임베딩 API·NumPy·벡터 캐시 없이
`_search_index.json`만 만듭니다. 선택한 토픽의 기존 인덱스 JSON은 바뀌지만 이전
벡터 파일/캐시는 지우지 않습니다. 기본 `--mode hybrid`는 기존 Google 임베딩 경로입니다.
`--dry-run`은 두 모드 모두 파일을 바꾸지 않는 미리보기이며 가짜 벡터를 저장하지 않습니다.
BM25 인덱스를 사용하는 브라우저 답변도 `/api/embed`를 호출하지 않고 선택한 LLM만
사용합니다. 키워드 일치가 없으면 근거 없는 문서를 골라 답변하지 않습니다.
BM25 인덱스에 `dense`/`hybrid` 질의를 보내면 자동 폴백 대신 명시적으로 실패합니다.
개인 메모와 원문 보강은 로컬 전용 토픽에 한하며 공개 토픽에는 넣지 않습니다.

**검색 품질 회귀 테스트** — 8개 컬렉션의 고정 40질의·고정 Gemini query vector로
`recall@5/10`, `MRR@10`, 실패 질의를 네트워크 없이 측정합니다. 인덱스 재빌드 뒤에는
해당 컬렉션과 `_cross`가 baseline보다 하락하면 배포를 중단하며, macmini에서는
`scripts/install-retrieval-eval-launchd.sh`로 매주 일요일 03:17 평가를 설치합니다.
초기 `retrieval-v2-bootstrap`은 BM25 top-1 known-item 라벨이므로 절대 품질 점수가 아니라
회귀 감지용입니다. 평가 자료·결정 기록은 `pipeline/eval/`에 있습니다.

단계별 입력·처리·출력 상세 → **[Architecture & Internals](docs/architecture.md)**

## 사용 모드

단일 오케스트레이터 `run_full.py` (3축: `--mode` / `--source` / `--images`):

```bash
# 주간 운영 — 검색 → Zotero 등록 → sync → 신규 리뷰 + timeline 보강
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode curate --source web --days 7

# 로컬 업데이트 — 검색 스킵, 신규/누락 narrative·timeline 기본 보강
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode curate --source zotero

# timeline 보강까지 끄고 리뷰/분류만 돌리려면
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode curate --source zotero --images skip

# 분류만 / 타임라인만 / 배포만
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode reclassify
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode retime --images all
PYTHONUTF8=1 python pipeline/run_full.py --topic humanoid --mode deploy

# 실행 계획 미리보기 / 로컬 서버
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode curate --dry-run
PYTHONUTF8=1 python pipeline/serve_local.py     # localhost:8000 + /api/embed + /api/citedby-answer
```

전체 모드 표, 안전 플래그, Concurrency 튜닝, 복구 절차 → **[Operations Manual](docs/operations.md)**

## 문서

| 문서 | 내용 |
|------|------|
| **[초보자·파워유저 매뉴얼](docs/manual/index.md)** | Paper Curation + Paper Curio 간단버전·심화버전 · PaperBanana 개념도 |
| **[활용 매뉴얼](docs/user-guide.md)** | 세 가지 경로 · 설정 위치(Zotero Settings → Paper Curio) · 리뷰/모듈 단계별 실행 · 상태 메시지 해석 · FAQ |
| **[Setup Guide](docs/setup-guide.md)** | 사전 준비 · Claude Code/수동 설치 · config.json · 설치 확인 · 문제 해결 |
| **[Operations Manual](docs/operations.md)** | 모드/안전 플래그 · Concurrency · 한국 망 우회(SPECTER2/arXiv/로컬 fallback) · 배포(O-1) · 복구 |
| **[Architecture & Internals](docs/architecture.md)** | 파이프라인 단계 상세 · 신뢰성 설계 · 내부 구조 · Karpathy LLM Wiki 비교 · 요구사항 |
| **[English README](README.en.md)** | Full English documentation |

## 발표/참고자료

이 프로젝트는 **AAiCON 2026** (국립중앙과학관, 2026.06.25–26)에서 발표되었습니다.

| 형식 | 자료 |
|------|------|
| **구두 발표** | [260625_이제현_AAiCon.pdf](docs/public/260625_이제현_AAiCon.pdf) |
| **포스터** | [260625_이제현_AAiCon_poster.pdf](docs/public/260625_이제현_AAiCon_poster.pdf) |
| **AIX 클리닉 1회** | [AIX 클리닉 1회 (KIST 존슨강당, 2026.07.16.)](docs/public/260715_AIX_clinic_paper_curation.pdf) |

---

*Built with Claude Code.* 🐱
