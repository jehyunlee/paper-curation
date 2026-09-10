# Paper Curation — Setup Guide

Paper Curation의 keyless 기본 설치, 선택 기능 검사, 단일 PDF 로컬 리뷰와
별도의 전체 큐레이션 워크플로 설정을 설명합니다.

## 기본 설치 사전 준비

기본 `setup.py` 실행에 API 키, Zotero 컬렉션, PaperBanana는 필요하지 않습니다.
키를 입력받거나 `config.json`에 복사하지 않으며 네트워크 호출이나 첫 전체
파이프라인 실행도 하지 않습니다.

- [Claude Code](https://claude.ai/code) 설치(Claude Code에서 설치할 때만)
- Git과 **conda env 하나 (Python 3.12, `py312`)**:
  ```bash
  conda create -n py312 -c conda-forge python=3.12 pip -y
  conda activate py312
  pip install -r requirements.txt
  ```

Java Runtime, Zotero, API 키는 선택한 기능을 실제 실행할 때만 준비합니다.
`opendataloader-pdf`를 쓰는 PDF 추출에는 Java가 권장됩니다(macOS:
`brew install --cask temurin`); 없으면 PyMuPDF로 fallback합니다.

## Claude Code에서 설치 (권장)

Claude Code에서 아래와 같이 요청하면 자동으로 설치가 진행됩니다:

> **"여기에 paper-curation을 설치해줘: https://github.com/jehyunlee/paper-curation"**

Claude Code가 다음 과정만 수행합니다:

1. **레포지토리 클론** 및 **Python 의존성 설치**
2. `PYTHONUTF8=1 python pipeline/setup.py` 실행
3. 최소 `config.json`과 `docs/papers/` 생성
4. SKILL.md 생성 및 SKILL 설치

setup은 완전 비대화형이며 API 키·이메일·Zotero·GitHub·PaperBanana 경로를
묻지 않습니다.
PaperBanana 자동 clone, 클러스터링 probe, Zotero 연결, 전체 파이프라인 자동
실행도 없습니다. `--no-install`은 SKILL 설치만 건너뛰며 SKILL 생성/설치
실패는 nonzero로 종료합니다.

### 공유 기능 레지스트리

Curio의 모듈 패널과 CLI는 같은 레지스트리를 사용합니다. 기본 설치 뒤에는 키 없이
기능을 나열하고, 요청을 계획한 뒤, 명시적으로 실행합니다.

```bash
python pipeline/run_feature.py --list
python pipeline/run_feature.py --request feature-request.json
python pipeline/run_feature.py --request feature-request.json --execute
```

`--request`는 JSON **파일 경로**를 받으며 계획만 반환합니다. `--execute`가 있어야 실행합니다.
예를 들어 기존 리뷰가 있는 토픽의 키워드 색인은 다음을 `feature-request.json`으로 저장합니다:

```json
{
  "schema_version": 1,
  "feature": "keyword-search",
  "params": {"topic": "my_topic", "operation": "build"}
}
```

요청 형식은
`{"schema_version":1,"feature":"…","params":{…}}`이며 필요에 따라
`provider`, `credential_ref`, `budget`을 더합니다. `budget`에는
`max_cost_usd`, `input_per_million_usd`, `output_per_million_usd`,
`max_output_tokens`를 지정할 수 있습니다. 요율을 알 수 없거나 상한을 넘으면
실행을 막습니다.

<!-- GENERATED FEATURE REGISTRY: pipeline/run_feature.py --list; parent generator owns this region. -->
| 모듈 | 기능 ID | 기능 / Feature | 제공자 | 전송 대상 | 비용 유형 |
|---|---|---|---|---|---|
| M1 | `review` | 논문 리뷰 / Paper review | anthropic, openai, google | selected cloud provider | paid |
| M1 | `summary` | 근거 기반 요약 / Grounded summary | anthropic, openai, google, ollama | selected provider; Ollama stays on loopback | provider-dependent |
| M1 | `chat` | 근거 기반 질의 / Grounded chat | anthropic, openai, google, ollama | selected provider; Ollama stays on loopback | provider-dependent |
| M1 | `comparison` | 근거 기반 비교 / Grounded comparison | anthropic, openai, google | selected cloud provider | paid |
| M0 | `extract` | 로컬 PDF 추출 / Local PDF extraction | none / configured sources | none | local |
| M2 | `keyword-search` | 키워드 검색·색인 / Keyword search and indexing | none / configured sources | none | local |
| M3 | `semantic-search` | 의미 검색·색인 / Semantic search and indexing | google | Google embedding API | paid |
| M4 | `metrics` | 피인용·서지 지표 / Citation and bibliography metrics | none / configured sources | Crossref/OpenAlex/Scopus source APIs | unpriced |
| M4 | `bibliography-update` | 서지 DB·기관 반영 / Bibliography and affiliation update | none / configured sources | none offline; configured bibliography sources when online; never Zotero Web paging | unpriced |
| M4 | `institution-export` | 공개 기관표 내보내기 / Public institution table export | none / configured sources | none; source redistribution terms remain applicable | local |
| M5 | `audio` | 오디오 만들기 / Generate audio | google | Google script and TTS API; no email | paid |
| M6 | `timeline-text` | 텍스트 타임라인 / Text timeline | anthropic | Anthropic narrative API; no image backend | paid |
| M6 | `timeline-image` | 타임라인 그림 / Timeline images | none / configured sources | configured PaperBanana backends; inspect preflight | unpriced |
| M7 | `zotero-sync` | Zotero 원격 동기화 / Zotero remote sync | zotero | Zotero API; may remove local deleted entries when applied | unpriced |
| M7 | `publish` | 명시적 웹 배포 / Explicit web publication | cloudflare | Cloudflare/GitHub; publishes artifacts and repository updates | unpriced |
| M8 | `email` | 기존 MP3 이메일 전달 / Email an existing MP3 | resend | Resend and the specified recipient; domain/recipient rights checked only by send response | unpriced |
<!-- END GENERATED FEATURE REGISTRY -->

각 기능은 독립적으로 요청합니다. 지원하지 않는 runtime·capability·권한은 성공으로
바꾸지 않고 상태로 반환됩니다. Collection 작업은 AI 작업의 자동 후속 단계가
아닙니다. `publish`와 `email`은 각각 명시적으로 요청하며, 클라우드 게시와 이메일
발송 권한·대상·내보낼 콘텐츠의 권리는 운영자가 별도로 확인해야 합니다.

`keyword-search`와 `semantic-search`는 `params.operation`에 `"query"` 또는
`"build"`를 명시할 수 있으며, 생략하면 `"query"`입니다. 기관·서지 DB 단계는
`bibliography-update` 기능으로 독립 실행합니다. 기본은 변경된 항목만 로컬 DB에
ingest하며, `--changed-only --skip-zotero --offline --no-email`은 외부 동기화,
온라인 보강, 이메일을 수행하지 않습니다. 온라인 보강은 별도 선택입니다.

### 자격증명

비밀값은 OS keyring 서비스 `paper-curation`에 저장하고
`credential:<provider>` 참조만 요청에 둡니다. 환경변수가 keyring보다 우선합니다.
예를 들어 Anthropic은 `ANTHROPIC_API_KEY`, Google은
`GOOGLE_API_KEY` 또는 `GEMINI_API_KEY`를 사용합니다. keyring의 평문,
`keyrings.alt`, null, fail backend는 거부되며 config/file fallback은 없습니다.
키를 argv, config, 요청 JSON, 로그, UI로 전달하지 마세요.

```bash
# 터미널에 표시하지 않고 입력하여 표준입력으로 전달
python -c 'import getpass,sys; sys.stdout.write(getpass.getpass())' | \
  python pipeline/credentials.py --operation write --provider anthropic

# 비밀값을 표시하지 않는 상태 확인
python pipeline/credentials.py --operation status --provider anthropic
```

`read`는 Curio 내부 IPC 전용입니다. 터미널에서 직접 실행하지 말고, 출력은 private
pipe에서만 소비하며 UI나 로그에 중계하지 마세요. 읽기 결과는
`{"reference":"credential:ID","value":"…"}` 형식이며, 값이 없으면 빈 문자열입니다.

## 수동 설치 (Claude Code 없이)

<details>
<summary>Python CLI로 직접 설치하기</summary>

### 1. Clone & Dependencies

```bash
git clone https://github.com/jehyunlee/paper-curation.git
cd paper-curation
pip install -r requirements.txt   # 전체 의존성 (anthropic·openai·umap-learn·hdbscan·sentence-transformers 등)
```

> 표준은 단일 `py312` env 입니다 (`requirements.txt` 에 클러스터링 의존성 포함).

### 2. Setup

```bash
python pipeline/setup.py
```

`setup.py`는 입력 prompt 없이 최소 `config.json`과 `docs/papers/`를 만들고
SKILL.md를 생성·설치합니다. 키 검사, Zotero 연결, PaperBanana clone, 전체
파이프라인 실행은 기본 동작이 아닙니다.

스킬 설치를 건너뛰려면 `--no-install` 옵션을 사용하세요.

### config.json 직접 편집

새 설치가 생성하는 최소 스키마는 다음과 같습니다:

```json
{
  "zotero": {
    "collections": {}
  }
}
```

| Field | Description |
|-------|-------------|
| `zotero.collections` | 전체 Zotero workflow를 나중에 설정할 수 있는 빈 alias→collection mapping |

기존 config의 non-secret field는 보존합니다. 어떤 API 키도 새로 저장하지 않으며
env의 키를 config로 복사하지 않습니다. setup이 config를 저장할 때 발견한 legacy
`zotero.api_key`는 제거합니다.

</details>

## 단일 PDF 로컬 리뷰

리뷰 기본 제공자는 Anthropic Sonnet 5이고 자동 fallback은 없습니다. OpenAI와
Google은 명시적으로 선택하는 제공자이며 같은 검토 스키마를 사용합니다. Ollama
`qwen3.8:27b-mlx`는 요약·대화 전용이고 리뷰를 대신하지 않습니다. Curio 모듈
패널은 이 요청을 만들며, CLI와 동일한 credential reference와 예산 규칙을 적용합니다.

`request.json` 경로는 상대/절대 경로 모두 허용됩니다. 요청 스키마는 정확히
다음과 같습니다:

```json
{
  "schema_version": 1,
  "feature": "review",
  "pdf_path": "/absolute/path/to/paper.pdf",
  "output_dir": "/absolute/path/to/output/paper-slug",
  "item": {
    "key": "ZOTERO_ITEM_KEY",
    "title": "Paper title",
    "creators": [
      {
        "firstName": "Ada",
        "lastName": "Lovelace",
        "creatorType": "author"
      }
    ],
    "date": "2026",
    "DOI": "10.0000/example",
    "abstractNote": "Abstract text",
    "url": "https://example.org/paper",
    "publicationTitle": "Journal name"
  },
  "overwrite": false,
  "provider": "anthropic",
  "credential_ref": "credential:anthropic",
  "budget": {
    "max_cost_usd": 1.00,
    "input_per_million_usd": 3.00,
    "output_per_million_usd": 15.00,
    "max_output_tokens": 6000
  }
}
```

```bash
python pipeline/local_review.py --request request.json
python pipeline/local_review.py --request request.json --execute
```

stdout은 마지막까지 JSON만 출력합니다. 상태는 `ready`, `needs-key`,
`needs-runtime`, `insufficient-data`, `failed`, `completed`, `exists` 중 하나입니다.
`overwrite: false`이고 기존 산출물이 완전하며 요청과 일치하면 `exists`입니다.
불완전하거나 불일치하는 기존 묶음은 `failed`이며 자동으로 덮어쓰지 않습니다.
리뷰 생성 뒤 HTML 등 후속 단계가 실패하면 응답의 `partial`에 보존된 리뷰와
캐시 상태를 표시합니다. 캐시 보존은 다른 입력의 재실행까지 무료라는 뜻이 아닙니다.

`--execute`는 PDF sanity 검증, canonical text 추출, geometric figure 추출(Gemini
검증 비활성), Sonnet 5 리뷰, canonical HTML, 필수 `bibliography.json` sidecar만
해당 `output_dir`에 publish합니다. 즉 `text.md`, `figures/`, `review.md`,
`index.html`, `bibliography.json`과 필요한 그림 다운로드 payload를 생성합니다. 분류, 논문 검색, semantic index,
타임라인, 이메일, 배포, Zotero Web API/remote DB sync는 실행하지 않습니다.
CLI 자체는 전역 `_papers_index.json`이나 서지 DB도 수정하지 않습니다.

공유 코퍼스에 쓰는 작업은 reserve/register/cancel 트랜잭션과 공통 잠금으로
충돌을 조정하고 Curio 목록을 갱신합니다. 이는 분류·검색 인덱스·타임라인·배포를
자동 실행한다는 뜻이 아닙니다. 기존 전체 workflow는 아래의 별도 고급 작업입니다.

## Google 없는 키워드 검색과 답변

기존 리뷰와 `_papers_index.json`의 토픽 소속 정보가 준비된 코퍼스에서 실행합니다.
이 기능은 새 논문 수집·리뷰 생성·서지 DB 등록을 대신하지 않습니다.

```bash
python pipeline/setup.py --check-feature keyword-search

# 토픽의 키워드 인덱스 구축 — 임베딩 API/벡터 캐시 사용 없음
python pipeline/build_search_index.py --topic my_topic --mode bm25

# 조회는 파일을 변경하지 않음
python pipeline/query_search_index.py --topic my_topic \
  --query "scientific discovery" --mode bm25 --json

# 실제 파일 변경 없이 구축 내용 확인
python pipeline/build_search_index.py --topic my_topic --mode bm25 --dry-run
```

- `--mode bm25`: 내용만 든 `_search_index.json`을 만들고 Google/NumPy/벡터 캐시를
  사용하지 않습니다. 명시적으로 지정한 토픽의 JSON을 교체하지만 이전 임베딩 바이너리와
  캐시는 삭제하지 않습니다.
- 기본 `--mode hybrid`: 기존 Google 문서 임베딩 + BM25 경로입니다. 의미 검색이
  필요할 때만 선택하고, 다른 모델/차원의 벡터를 같은 인덱스에 섞지 않습니다.
- `--dry-run`: 두 모드 모두 읽기 전용이며 가짜 벡터나 출력 파일을 생성하지 않습니다.
- BM25 인덱스는 `dim: 0`, `model: null`, `quant: null`, `retrieval_mode: "bm25"`이고
  `emb_file`과 chunk 벡터가 없습니다. `dense`/`hybrid` 조회는 임베딩 요청 전에 거부합니다.
- 브라우저 Deep Research도 해당 인덱스에서는 키워드 검색만 하며 `/api/embed`나
  벡터 파일을 읽지 않습니다. 답변 생성에는 선택한 Anthropic/OpenAI/Google 키가 별도로
  필요합니다. 키워드 일치가 없으면 임의 문서를 근거로 답변하지 않습니다.
- 개인 메모와 `text.md` 원문 보강은 로컬 전용 토픽에만 포함합니다. 공개 토픽에는
  넣지 않으며 `--include-text yes`도 공개 토픽에서 허용하지 않습니다.
- 배포 freshness 검사는 sparse에 바이너리가 없다는 이유로 실패하거나 hybrid 재구축을
  요구하지 않습니다. 운영 인덱스의 모드 전환이나 전체 재구축은 별도 명시적 작업입니다.

## 전체 curate/full 워크플로 (명시적 별도 실행)

기존 종합 큐레이션은 setup이나 단일 PDF 리뷰가 자동으로 이어서 실행하지
않습니다. Zotero 컬렉션 수집·분류·검색 인덱스·타임라인·배포가 필요할 때 해당
설정과 환경변수를 준비한 뒤 명시적으로 실행합니다.

### 전체 워크플로 환경변수

CLI 비밀값은 환경변수 또는 공통 OS keyring 참조로 전달합니다. Zotero도
`ZOTERO_API_KEY` 또는 `credential:zotero`를 사용하며, `zotero.api_key`를
읽거나 저장하지 않습니다. 공통 실행기는 필요한 키만 자식 프로세스 환경에 주입합니다.

| 환경변수 | 필요한 기능 |
|----------|-------------|
| `ZOTERO_API_KEY` | Zotero 수집/sync 및 원격 identity·collection 조회 |
| `ZOTERO_USER_ID` | Zotero user ID를 명시할 때 |
| `ZOTERO_DIR` | Zotero PDF 저장 경로를 override할 때 |
| `ANTHROPIC_API_KEY` | 리뷰·인사이트 |
| `GOOGLE_API_KEY` | semantic search embedding(`gemini-embedding-001`)·Figure 검증·TTS |
| `OPENAI_API_KEY` | 기존 Chat/Deep Research BYOK·insights fallback(선택) |
| `RESEND_API_KEY` | 배포 시 Audio Overview 이메일(선택 workflow) |
| `GITHUB_REPO` | GitHub 배포(선택 workflow) |
| `GITHUB_BRANCH` | Git branch(기본: master) |
| `PAGES_BASE_URL` | GitHub Pages base URL |

```bash
export ZOTERO_API_KEY=...
export ANTHROPIC_API_KEY=...
export GOOGLE_API_KEY=...
PYTHONUTF8=1 python pipeline/run_full.py \
  --topic my_topic --mode curate --source zotero
```

리뷰에서 Anthropic은 기본값이고 OpenAI·Google은 검토된 스키마의 명시 선택입니다.
Resend는 email/deploy workflow를 실제 선택할 때만 필요합니다.

### 전체 워크플로 config 확장

fresh setup의 `zotero.collections` 등에 기존 full-pipeline 설정을 필요에 따라
추가합니다. API key는 추가하지 않습니다:

```json
{
  "zotero": {
    "email": "your_email@example.com",
    "collections": {
      "my_topic": "My Zotero Collection Name"
    },
    "pdf_dir": "/path/to/your/zotero/pdfs"
  },
  "unpaywall_email": "your_email@example.com",
  "search_keywords": {
    "my_topic": {
      "primary": ["machine learning biology", "protein language model"],
      "secondary": ["single cell RNA", "drug target prediction"]
    }
  },
  "paperbanana_dir": "/path/to/an/existing/paperbanana"
}
```

| Field | Description |
|-------|-------------|
| `zotero.email` | Zotero 및 Unpaywall용 이메일 |
| `zotero.collections` | Topic alias → Zotero 컬렉션 이름 매핑 |
| `zotero.pdf_dir` | Zotero PDF가 저장된 로컬 경로 |
| `search_keywords` | 토픽별 Core-1 검색 키워드(선택) |
| `paperbanana_dir` | 직접 설치한 PaperBanana 경로(선택); setup은 clone하지 않음 |

타임라인에 PaperBanana가 필요하면 아래의 선택 설치 절차를 먼저 수행합니다.
전체 실행 시간과 concurrency 권장값은
[Operations Manual](operations.md#concurrency-anthropic-tier-4-default)을
참고하세요.

## 사용법

### `/paper-curation`

메인 파이프라인. Claude Code에서 아래와 같이 사용합니다:

```
/paper-curation my_topic                        # 전체 파이프라인
/paper-curation my_topic --local                # Zotero에 이미 있는 논문만 처리
/paper-curation my_topic --local --update       # 새 논문만 추가, 기존 유지
/paper-curation my_topic --local --update-force  # 모든 리뷰 재생성
```

트리거: "논문 큐레이션", "최신 논문 찾아줘", "paper curation"

### `/paper-curation-workflow`

파이프라인 워크플로우 다이어그램을 생성합니다.

```
/paper-curation-workflow                  # 5 candidates (기본)
/paper-curation-workflow --candidates=10  # 10 candidates
```

트리거: "workflow 만들어줘"

## Pipeline Scripts

전체 큐레이션의 단일 진입점은 `run_full.py` (3축 오케스트레이터)이고, 아래
개별 스크립트는 디버깅·복구용입니다. `local_review.py`는 그 전역 파이프라인과
분리된 request 기반 P1 endpoint입니다. 하드코딩된 인증 정보는 없습니다.

| Script | Purpose |
|--------|---------|
| `pipeline/local_review.py` | 단일 PDF plan/execute; 논문별 산출물과 sidecar만 생성 |
| `pipeline/config_loader.py` | 공유 설정; API 키는 환경변수/OS keyring, 평문 config 키는 읽지 않음 |
| `pipeline/sync_zotero.py` | Zotero에서 삭제/제목 변경 동기화 |
| `pipeline/run_update_force.py` | 배치 리뷰 생성 (PDF → 텍스트 → Figure → 리뷰) |
| `pipeline/build_papers_index.py` | 마스터 인덱스 재구축 |
| `pipeline/classify_papers.py` | 다중 카테고리 + 서브 카테고리 분류 |
| `pipeline/build_category_summaries.py` | 카테고리별 한국어 설명 생성 |
| `pipeline/generate_timelines.py` | Bottom-up 타임라인 생성 (Opus + PaperBanana) |
| `pipeline/review_to_html.py` | review.md → index.html 변환 |
| `pipeline/build_topic_index.py` | Topic 인덱스 페이지 생성 |
| `pipeline/prepare_deploy.py` | PNG→WebP 변환 + Cloudflare + gh-pages 배포 |

## PaperBanana (타임라인 생성용, 선택)

타임라인 생성에는 PaperBanana와 scisci 래퍼가 필요합니다. 없어도 파이프라인은 정상 동작하며, 타임라인 생성만 건너뜁니다.

<details>
<summary>PaperBanana 설치 방법</summary>

```bash
# 1. PaperBanana 클론
git clone https://github.com/dwzhu-pku/PaperBanana.git /path/to/paperbanana
cd /path/to/paperbanana
pip install -r requirements.txt

# 2. scisci 클론 (PaperBanana 래퍼)
git clone https://github.com/jehyunlee/scisci.git /path/to/scisci
```

`config.json`에 경로를 추가하세요:

```json
{
  "paperbanana_dir": "/path/to/paperbanana",
  "scisci_lib": "/path/to/scisci/scie"
}
```

의존성 체인:
```
pipeline/generate_timelines.py
  → scisci/scie/lib/paperbanana.py   (래퍼: 경로 관리, async 실행)
    → paperbanana/                    (7-agent pipeline: Retriever → Planner → Visualizer → Critic)
  → scisci/scie/lib/timeline.py      (LLM 내러티브 분석)
```

</details>

## 전체 워크플로 config.json 작동 원리

```
config.json
  ├── (Zotero API key)   → config.json 이 아니라 환경변수 ZOTERO_API_KEY
  ├── zotero.email       → Zotero 계정 식별
  ├── zotero.collections → Topic alias → Collection name
  │     ↓ (자동 변환)
  │   Zotero API: name → collection key
  │   Zotero API: ZOTERO_API_KEY → user ID
  └── unpaywall_email    → Open Access PDF 조회
```

전체 Zotero workflow에서 collection key나 User ID는 `ZOTERO_API_KEY`를 사용해
자동 조회됩니다. 기본 setup은 이 원격 조회를 실행하지 않습니다.

## 설치 확인 & 문제 해결

### 전체 워크플로 설치 확인 (verify)

긴 파이프라인을 돌리기 전에, 한 줄로 의존성이 제대로 깔렸는지 확인하세요:

```bash
python -c "import umap, hdbscan, sentence_transformers, fitz, sklearn, anthropic; print('py312 OK')"
```

`OK` 가 찍히면 준비 완료입니다. 실행 계획만 먼저 보려면 `--dry-run` 도 가능합니다:

```bash
PYTHONUTF8=1 python pipeline/run_full.py --topic my_topic --mode curate --source zotero --dry-run
```

### 문제 해결 (Troubleshooting)

| 증상 / 에러 메시지 | 원인 | 해결 |
|---|---|---|
| `op_CALL_KW: pop from empty list` (numba 트레이스백) | `py312` env 밖에서 분류가 실행됨 | `conda activate py312` 후 재실행 |
| `ModuleNotFoundError: umap` / `hdbscan` / `sentence_transformers` | 의존성 누락 | env 활성화 후 `pip install -r requirements.txt` (umap-learn·hdbscan·sentence-transformers 포함) |
| Figure 품질이 낮음 / 표·구조가 깨짐 | Java 미설치로 PyMuPDF fallback | `brew install --cask temurin` (macOS) 후 재실행 |
| SPECTER2 / arXiv 다운로드가 멈춤 (한국 망) | huggingface LFS·arXiv 차단 | [operations.md "Korean network workarounds"](operations.md#korean-network-workarounds) 의 S3 미러 명령 사용 |
| 전체 Zotero workflow의 `[COLLECTION_ERROR]` | Zotero 컬렉션 이름 오타 | 출력의 사용 가능한 컬렉션 목록에서 올바른 이름 선택 후 재실행 |
| 검색 인덱스가 빈 임베딩으로 빌드됨 | `GOOGLE_API_KEY` 미설정 | `export GOOGLE_API_KEY=...` 후 재실행 — 검색 임베딩은 Google `gemini-embedding-001` 사용 (OpenAI 키는 더 이상 필수 아님) |
