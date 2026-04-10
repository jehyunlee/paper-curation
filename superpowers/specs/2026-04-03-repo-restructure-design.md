# Repo 구조 개선 설계

**Date:** 2026-04-03
**Status:** Approved
**Goal:** 배포 가능한 Claude Code skill로서 깔끔한 repo 구조 제공

## 배경

현재 repo는 GitHub Pages 정적 사이트와 파이프라인 스크립트가 root에 혼재되어 있다.
- root에 `.py` 13개가 펼쳐져 있어 배포 파일과 구분이 안 됨
- `skill/` 디렉토리에 실제 skill이 없고 README.md만 존재
- `src/` 빈 디렉토리, `_legacy/` 미사용 코드 잔존
- `.gitignore`가 whitelist 방식으로 복잡

## 설계 원칙

- **핵심은 파이프라인 스크립트** — clone한 사용자가 로컬에서 실행하는 도구
- **GitHub Pages 사이트는 부산물** — 파이프라인 실행 결과
- **GitHub Actions 불필요** — 오프라인 실행 우선, `docs/` source 설정만 변경
- **데이터 파일은 실행 결과물** — repo에 포함하지 않고 `.gitignore`로 제외

## 최종 구조

```
paper-curation/
├── pipeline/                        ← 파이프라인 스크립트 + 라이브러리
│   ├── run_update_force.py
│   ├── build_papers_index.py
│   ├── build_topic_index.py
│   ├── build_category_summaries.py
│   ├── classify_papers.py
│   ├── generate_timelines.py
│   ├── review_to_html.py
│   ├── prepare_deploy.py
│   ├── search_papers.py
│   ├── register_zotero.py
│   ├── sync_zotero.py
│   ├── config_loader.py
│   ├── setup.py
│   ├── generate_workflow.py          ← workflow/에서 이동
│   ├── lib/
│   │   ├── __init__.py
│   │   ├── categories.py
│   │   ├── dateutil.py
│   │   └── paperbanana.py
│   ├── _img_workflows/               ← workflow diagram PNG 출력
│   └── _img_timelines/               ← PaperBanana 타임라인 후보 전체
│       ├── ai4s/
│       │   ├── research_timeline_1.png
│       │   ├── research_timeline_2.png
│       │   ├── category_timeline_*_1.png
│       │   └── ...
│       └── scisci/
│           └── (동일 구조)
│
├── docs/                             ← GitHub Pages 서빙 루트 (/docs)
│   ├── papers/
│   │   └── {NNN_Slug}/
│   │       ├── index.html            ← 배포 (git tracked)
│   │       ├── review.md             ← 소스 (git tracked)
│   │       └── figures/*.webp        ← 배포 (git tracked)
│   ├── ai4s/
│   │   ├── index.html                ← 배포
│   │   ├── research_timeline.png     ← 1번 후보 복사 (번호 제거)
│   │   ├── category_timeline_*.png   ← 1번 후보 복사 (번호 제거)
│   │   ├── timelines/                ← 기존 timeline HTML
│   │   ├── _new_classification.json  ← gitignore 제외 (실행 결과물)
│   │   ├── _category_summaries.json  ← gitignore 제외
│   │   ├── _timeline_narrative.json  ← gitignore 제외
│   │   └── _method_text_*.txt        ← gitignore 제외
│   ├── scisci/
│   │   └── (ai4s와 동일 구조)
│   └── setup-guide.md                ← skill/README.md에서 이동
│
├── config.json                       ← gitignore 제외 (사용자별 설정)
├── config.example.json               ← git tracked (템플릿)
├── CLAUDE.md
└── README.md                         ← setup-guide.md 링크 포함
```

## 삭제 대상

| 디렉토리 | 사유 |
|-----------|------|
| `src/` | 빈 디렉토리 |
| `_legacy/` | 미사용 구버전 코드 |
| `skill/` | README.md만 존재, `docs/setup-guide.md`로 이동 |
| `workflow/` | `generate_workflow.py` → `pipeline/`, PNG → `pipeline/_img_workflows/` |

## 스크립트 수정 사항

### 1. 출력 경로 변경

모든 pipeline 스크립트가 참조하는 `papers/`, `ai4s/`, `scisci/` 경로를 `docs/` 기준으로 변경.

`config_loader.py`에 `docs_dir` 경로를 한 곳에서 관리:

```python
DOCS_DIR = Path(__file__).parent.parent / "docs"
PAPERS_DIR = DOCS_DIR / "papers"

def get_topic_dir(topic: str) -> Path:
    return DOCS_DIR / topic
```

각 스크립트에서 하드코딩된 경로 대신 `config_loader`의 경로 함수 사용.

### 2. 타임라인 이미지 흐름

```
generate_timelines.py
  → PaperBanana 실행
  → 후보 전체 저장: pipeline/_img_timelines/{topic}/
  → 1번 후보 복사: docs/{topic}/ (파일명에서 번호 제거)
```

### 3. workflow 이미지 흐름

```
generate_workflow.py (pipeline/ 내)
  → 후보 생성: pipeline/_img_workflows/
```

### 4. import 경로

`pipeline/` 내부에서 `from lib.xxx import ...` 유지 (상대 위치 동일).

`config_loader.py`는 `pipeline/` 안에 있고 `config.json`은 root에 있으므로, config 로딩 경로를 `Path(__file__).parent.parent / "config.json"`으로 변경.

### 5. 함께 수정할 파일

| 파일 | 변경 내용 |
|------|-----------|
| `.gitignore` | whitelist 경로를 `docs/` 기준으로 업데이트 |
| `CLAUDE.md` | 경로 참조 전체 업데이트 |
| `README.md` | `docs/setup-guide.md` 링크 추가 |
| `.claude/skills/paper-curation/` | 스크립트 경로 업데이트 |
| `.claude/skills/paper-curation-workflow/` | workflow 출력 경로 업데이트 |
| `SKILL.md.template` | 스크립트 경로 업데이트 |

## GitHub Pages 설정

GitHub repo Settings → Pages → Source를 `/ (root)` → `/docs`로 변경 (1회, 수동).

## 실행 방식

```bash
# 기존
PYTHONUTF8=1 python run_update_force.py --topic ai4s

# 변경 후
PYTHONUTF8=1 python pipeline/run_update_force.py --topic ai4s
```
