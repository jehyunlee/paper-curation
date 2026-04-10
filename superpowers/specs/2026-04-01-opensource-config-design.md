# Open-Source Config 체계 설계

**날짜**: 2026-04-01
**목적**: paper-curation 프로젝트를 오픈소스 배포 가능하게 만들기 위해, 하드코딩된 개인 정보를 `config.json` 기반 설정 체계로 전환한다. Python 스크립트와 paper-curation SKILL.md 모두 포함.

## 현황 분석

### 하드코딩된 개인 정보 (3개 레이어)

1. **Python 스크립트**: Zotero API key, user ID, email, PDF 저장 경로, collection key가 6개 레거시 파일에 직접 하드코딩. 메인 파이프라인(`run_update_force.py`, `sync_zotero.py`)은 `config_loader.py`를 사용하지만, `ZOTERO_DIR`과 `classify_papers.py`의 collection key는 하드코딩.
2. **`prepare_deploy.py`**: `git push origin master` 하드코딩. GitHub 계정/branch 설정 없음.
3. **SKILL.md**: `jehyunlee/paper-curation` 레포명, `jehyunlee.github.io` URL, `C:\Users\jehyu\...` 경로가 직접 기재.

### 기존 인프라

`config_loader.py`가 이미 하이브리드 패턴(config.json 우선, 환경변수 폴백)을 구현하고 있다. 이를 확장한다.

## 설계

### 1. `config.json` 스키마 확장

현재 config.json에 `zotero.pdf_dir`과 `github` 섹션을 추가한다.

```json
{
  "zotero": {
    "api_key": "...",
    "email": "...",
    "collections": {
      "ai4s": "AI assisted Research",
      "scisci": "Science of Science"
    },
    "pdf_dir": "C:\\Users\\jehyu\\GoogleDrive\\Zotero"
  },
  "unpaywall_email": "...",
  "github": {
    "repo": "jehyunlee/paper-curation",
    "branch": "master",
    "pages_base_url": "https://jehyunlee.github.io/paper-curation"
  },
  "paperbanana_dir": "C:\\Users\\jehyu\\Arbeitplatz\\01_Work\\01_Devs\\AX\\paperbanana"
}
```

### 2. `config.example.json` 신규 생성

커밋되는 예시 파일. 자기 설명적 예시값 포함.

```json
{
  "zotero": {
    "api_key": "YOUR_ZOTERO_API_KEY_HERE",
    "email": "your.email@example.com",
    "collections": {
      "ai4s": "Your AI Collection Name",
      "scisci": "Your SciSci Collection Name"
    },
    "pdf_dir": "/path/to/your/zotero/pdfs"
  },
  "unpaywall_email": "your.email@example.com",
  "github": {
    "repo": "your-username/paper-curation",
    "branch": "master",
    "pages_base_url": "https://your-username.github.io/paper-curation"
  },
  "paperbanana_dir": "/path/to/your/PaperBanana"
}
```

### 3. PaperBanana 외부 의존성 정리

PaperBanana(`dwzhu-pku/PaperBanana`)는 논문 다이어그램 생성에 사용되는 외부 프로젝트다. 사용자가 별도로 clone/설치한 뒤, 그 경로를 config.json에 지정하는 방식으로 연결한다.

- `config.json`에 `paperbanana_dir` **유지** — PaperBanana 설치 경로
- `lib/paperbanana.py` (194줄 래퍼)를 프로젝트 안으로 복사
- 래퍼의 `PAPERBANANA_DIR` 결정 로직을 **config 전용**으로 변경 (폴백 없음):
  - `config.json`의 `paperbanana_dir` → 없거나 빈 값이면 에러
  - 기존의 vendored/external 자동 탐색 로직 제거
- `config.json`에서 `scisci_lib` 필드 **제거** — 유일한 사용처인 `ai4s/process_reviews.py`는 레거시로 삭제 대상
- `config_loader.py`에서 `get_scisci_lib()` **제거**, `get_paperbanana_dir()` **유지**
- `generate_timelines.py`, `workflow/generate_workflow.py`의 외부 경로 sys.path.insert → `from lib.paperbanana import generate_diagram` 직접 import로 변경

### 4. `config_loader.py` 확장

새로 추가할 함수들:

| 함수 | 반환값 | 환경변수 폴백 |
|------|--------|--------------|
| `get_zotero_dir()` | Zotero PDF 저장 디렉토리 | `ZOTERO_DIR` |
| `get_github_repo()` | `owner/repo` 문자열 | `GITHUB_REPO` |
| `get_github_branch()` | branch명 (기본 `master`) | `GITHUB_BRANCH` |
| `get_pages_base_url()` | GitHub Pages base URL | `PAGES_BASE_URL` |

삭제할 함수들:
- `get_scisci_lib()` — 레거시 스크립트 삭제로 불필요

기존 함수(`get_zotero_api_key`, `get_zotero_user_id`, `get_collections` 등)는 변경 없음.

### 5. 스크립트 수정 (3개 파일)

#### `run_update_force.py`
- **line 33**: `ZOTERO_DIR = r"C:\Users\jehyu\GoogleDrive\Zotero"` → `from config_loader import get_zotero_dir; ZOTERO_DIR = get_zotero_dir()`

#### `classify_papers.py`
- **line 24**: `COLLECTIONS = {"ai4s": "WKEZLEE8", "scisci": "3KVIDDKH"}` → `from config_loader import get_collections; COLLECTIONS = get_collections()`
- collection key 해석은 `config_loader._resolve_collection_value()`가 이미 처리함

#### `prepare_deploy.py`
- **line 203**: `["git", "push", "origin", "master"]` → config에서 branch를 읽어 동적 대입
- `from config_loader import get_github_branch`

### 6. 레거시 스크립트 삭제 (6개 파일)

`run_update_force.py`와 `sync_zotero.py`가 동일 기능을 커버하므로 제거:

- `ai4s/zotero_register.py` — Zotero 등록 (run_update_force.py로 대체)
- `ai4s/process_zotero_bulk.py` — 벌크 처리 (run_update_force.py로 대체)
- `scisci/zotero_register.py` — Zotero 등록 (run_update_force.py로 대체)
- `scisci/fetch_zotero_scisci.py` — Zotero fetch (sync_zotero.py로 대체)
- `scisci/_fix_pdfs.py` — PDF 수정 유틸 (1회성)
- `scisci/_fix_pdfs_round2.py` — PDF 수정 유틸 (1회성)

### 7. SKILL.md 템플릿화

하드코딩된 값을 플레이스홀더로 교체:

| 현재 값 | 플레이스홀더 | config 소스 |
|---------|------------|------------|
| `jehyunlee/paper-curation` | `{github_repo}` | `github.repo` |
| `https://jehyunlee.github.io/paper-curation/` | `{pages_base_url}` | `github.pages_base_url` |
| `C:\Users\jehyu\GoogleDrive\Zotero` | `{zotero_dir}` | `zotero.pdf_dir` |
| `C:/Users/jehyu/Arbeitplatz/paper-curation` | `{project_dir}` | 실행 시 `os.getcwd()` 또는 repo root 자동 감지 |
| `jehyun.lee@gmail.com` (SKILL 내) | `{email}` | `zotero.email` |

SKILL.md 원본은 `SKILL.md.template`로 보존하고, `setup.py`가 치환 결과를 `SKILL.md`로 출력한다.

### 8. `setup.py` 설치 스크립트

```
python setup.py
```

실행 흐름:
1. `config.json` 존재 확인 → 없으면 `config.example.json` 복사 후 편집 안내 출력, 종료
2. `config.json` 로드
3. `SKILL.md.template`의 플레이스홀더를 config 값으로 치환 → `SKILL.md` 출력
4. `.gitignore`에 `config.json` 포함 여부 확인 → 없으면 추가
5. 완료 메시지 출력

### 9. `.gitignore` 변경

추가:
```
config.json
```

커밋 대상:
- `config.example.json` (예시)
- `SKILL.md.template` (템플릿 원본)
- `setup.py` (설치 스크립트)

### 10. 변경하지 않는 것

- `config_loader.py`의 기존 함수 시그니처 — 하위 호환 유지
- `prepare_deploy.py`의 PNG→WebP 로직 — push 관련 부분만 수정
- `build_topic_index.py`, `review_to_html.py`, `build_papers_index.py` — config 의존성 없음
- git remote 설정 — 사용자가 직접 `git remote add origin` 수행 (setup.py 범위 밖)

## 파일 변경 요약

| 작업 | 파일 | 유형 |
|------|------|------|
| 신규 | `config.example.json` | 생성 |
| 신규 | `setup.py` | 생성 |
| 신규 | `lib/paperbanana.py` | 외부에서 복사 (194줄) |
| 수정 | `config.json` | `zotero.pdf_dir`, `github` 추가 / `scisci_lib` 제거 |
| 수정 | `config_loader.py` | 4개 함수 추가, 1개 함수 제거 (`get_scisci_lib`) |
| 수정 | `run_update_force.py` | ZOTERO_DIR → config |
| 수정 | `classify_papers.py` | COLLECTIONS → config |
| 수정 | `prepare_deploy.py` | branch → config |
| 수정 | `generate_timelines.py` | 외부 sys.path → `from lib.paperbanana` 직접 import |
| 수정 | `workflow/generate_workflow.py` | 외부 sys.path → `from lib.paperbanana` 직접 import |
| 수정 | `.gitignore` | `config.json` 추가 |
| 템플릿화 | `SKILL.md` → `SKILL.md.template` + `SKILL.md` | 플레이스홀더 치환 |
| 삭제 | 레거시 6개 파일 | 제거 |
