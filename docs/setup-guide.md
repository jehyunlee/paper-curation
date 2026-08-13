# Paper Curation — Setup Guide

Paper Curation 파이프라인의 설치 및 설정 가이드입니다.

## 사전 준비

시작하기 전에 아래 항목을 준비하세요:

- [Claude Code](https://claude.ai/code) 설치
- [Zotero API Key](https://www.zotero.org/settings/keys) 발급
- API 키 — `ANTHROPIC_API_KEY` (리뷰·인사이트 — **필수**), `GOOGLE_API_KEY` (검색 임베딩 `gemini-embedding-001`·Figure 검증·TTS — **필수**), `RESEND_API_KEY` (배포 시 Audio Overview 이메일 — 배포 필수), `OPENAI_API_KEY` (답변 BYOK·insights fallback — 선택)
- Zotero 컬렉션 이름 확인 (리뷰할 논문들이 모인 컬렉션)
- Zotero PDF 저장 경로 확인
- **conda env 하나 (Python 3.12, `py312`)** — `requirements.txt` 가 umap-learn / hdbscan / sentence-transformers 를 포함하므로 오케스트레이터가 토픽 모델링/분류를 별도 서브프로세스 없이 in-process 로 실행합니다. 생성 명령:
  ```bash
  conda create -n py312 -c conda-forge python=3.12 pip -y
  conda activate py312
  pip install -r requirements.txt
  ```
- **Java Runtime** — `opendataloader-pdf` 가 Java CLI 래퍼. macOS: `brew install --cask temurin`. 없으면 PyMuPDF 로 자동 fallback (표/구조 추출 품질 ↓).

## Claude Code에서 설치 (권장)

Claude Code에서 아래와 같이 요청하면 자동으로 설치가 진행됩니다:

> **"여기에 paper-curation을 설치해줘: https://github.com/jehyunlee/paper-curation"**

Claude Code가 자동으로 다음 과정을 수행합니다:

1. **레포지토리 클론** 및 **Python 의존성 설치**
2. **인터랙티브 설정** — 아래 항목을 차례로 질문합니다:
   - (Zotero API Key 는 묻지 않습니다 — `ZOTERO_API_KEY` 환경변수 전용)
   - 이메일 (Zotero/Unpaywall용)
   - 컬렉션 alias — 파이프라인에서 `--topic` 인자로 사용할 짧은 이름 (예: `bioml`, `climate`)
   - Zotero 컬렉션 이름 — alias에 매핑할 실제 Zotero 컬렉션
   - Zotero PDF 저장 경로
   - GitHub Pages 배포 설정 (선택)
3. **환경변수 확인** — `ANTHROPIC_API_KEY`, `GOOGLE_API_KEY` 설정 여부를 체크합니다
4. **Zotero 연결 테스트** — API key로 User ID를 조회하고 컬렉션이 실제 존재하는지 검증합니다
   - 컬렉션 이름이 잘못된 경우, 사용 가능한 컬렉션 목록을 보여주고 다시 질문합니다
5. **PaperBanana 확인** — 타임라인 생성용 [PaperBanana](https://github.com/dwzhu-pku/PaperBanana)가 없으면 `paper-curation/paperbanana/`에 자동으로 클론합니다
6. **SKILL.md 생성 및 설치** — Claude Code 스킬로 등록하여 이후 `/paper-curation` 명령으로 사용할 수 있습니다

설치가 완료되면 **파이프라인 실행** 안내가 표시됩니다.

> **⚠ 파이프라인 실행 시간**: Zotero 컬렉션의 논문 편수에 따라 크게 달라집니다 (Anthropic Tier·concurrency 의존).
> 10편 이하: 수 분 / 50편: ~15분 (Tier 4 default `--concurrency 16`) ~ 1~2시간 (Tier 1 `--concurrency 4`) / 500편 이상: 비례 증가. Tier별 권장값은 [Operations Manual의 Concurrency 표](operations.md#concurrency-anthropic-tier-4-default) 참고.

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
export ANTHROPIC_API_KEY=your_key     # 리뷰·인사이트 (필수)
export GOOGLE_API_KEY=your_key        # 검색 임베딩 gemini-embedding-001·Figure 검증·TTS (필수)
export OPENAI_API_KEY=your_key        # 답변 BYOK·insights fallback (선택)
python pipeline/setup.py
```

`setup.py`가 인터랙티브 설정 마법사를 실행하여 config.json 생성, Zotero 연결 테스트, SKILL.md 생성 및 설치를 한 번에 수행합니다.

스킬 설치를 건너뛰려면 `--no-install` 옵션을 사용하세요.

### config.json 직접 편집

설정 마법사 대신 직접 편집할 수도 있습니다:

```json
{
  "zotero": {
    "_comment": "Zotero API key 는 여기 두지 않습니다 — 환경변수 ZOTERO_API_KEY 전용",
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
  "paperbanana_dir": "/path/to/paperbanana"
}
```

| Field | Description |
|-------|-------------|
| ~~`api_key`~~ | **config.json 에 두지 않습니다.** Zotero API key 는 환경변수 `ZOTERO_API_KEY` 에서만 읽습니다 ([발급](https://www.zotero.org/settings/keys)) |
| `email` | 이메일 (Zotero 및 Unpaywall용) |
| `collections` | Topic alias → Zotero 컬렉션 이름 매핑. Collection key는 Zotero API를 통해 자동 변환됩니다. |
| `pdf_dir` | Zotero PDF가 저장된 로컬 경로 |
| `search_keywords` | 토픽별 Core-1 검색 키워드 (`{topic: {primary: [...], secondary: [...]}}`). `primary` 매칭 0.5점, `secondary` 0.2점. `ai4s`/`scisci` 는 빌트인 기본값이 있어 생략 가능하고, 그 외 신규 토픽은 여기에 추가합니다. (선택) |
| `paperbanana_dir` | [PaperBanana](https://github.com/dwzhu-pku/PaperBanana) clone 경로 (선택) |

### 환경변수

`ZOTERO_API_KEY` 는 **필수이며 환경변수 전용**입니다 — 파이프라인은 `config.json` 의
`zotero.api_key` 를 읽지 않습니다. 나머지 키는 `config.json` 으로도 설정할 수 있습니다.

```bash
export ZOTERO_API_KEY=...   # ~/.zshrc 등 셸 설정에 넣어 두세요
```

| 환경변수 | 용도 |
|----------|------|
| `ZOTERO_API_KEY` | Zotero API key (**환경변수 전용 — config.json 불가**) |
| `ZOTERO_USER_ID` | Zotero user ID |
| `ZOTERO_DIR` | Zotero PDF 저장 경로 |
| `ANTHROPIC_API_KEY` | Claude API key (리뷰·인사이트 — 필수) |
| `GOOGLE_API_KEY` | Google AI key (검색 임베딩 `gemini-embedding-001`·Figure 검증·TTS — 필수) |
| `OPENAI_API_KEY` | OpenAI key (답변 BYOK·insights fallback — 선택) |
| `RESEND_API_KEY` | Resend key (배포 시 Audio Overview 이메일 — wrangler secret 으로도 등록) |
| `GITHUB_REPO` | GitHub repo (owner/repo) |
| `GITHUB_BRANCH` | Git branch (기본: master) |
| `PAGES_BASE_URL` | GitHub Pages base URL |

</details>

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

단일 진입점은 `run_full.py` (3축 오케스트레이터)이고, 아래 개별 스크립트는 디버깅·복구용입니다. 모든 스크립트는 `pipeline/config_loader.py`를 통해 `config.json`을 읽습니다. 하드코딩된 인증 정보는 없습니다.

| Script | Purpose |
|--------|---------|
| `pipeline/config_loader.py` | 공유 설정: Zotero API key, User ID (자동), collection keys (자동) |
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

## config.json 작동 원리

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

Collection key나 User ID는 직접 입력할 필요 없이 Zotero API를 통해 자동으로 조회됩니다.

## 설치 확인 & 문제 해결

### 설치 확인 (verify)

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
| `[COLLECTION_ERROR]` | Zotero 컬렉션 이름 오타 | 출력의 사용 가능한 컬렉션 목록에서 올바른 이름 선택 후 재실행 |
| 검색 인덱스가 빈 임베딩으로 빌드됨 | `GOOGLE_API_KEY` 미설정 | `export GOOGLE_API_KEY=...` 후 재실행 — 검색 임베딩은 Google `gemini-embedding-001` 사용 (OpenAI 키는 더 이상 필수 아님) |
