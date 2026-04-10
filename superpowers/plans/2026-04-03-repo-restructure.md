# Repo 구조 개선 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** root의 .py 파일과 배포 파일을 분리하여 `pipeline/` (스크립트) + `docs/` (GitHub Pages) 구조로 재편

**Architecture:** `pipeline/`에 모든 .py + lib/ 이동, `docs/`에 papers/ai4s/scisci/ 이동. config_loader.py에 PROJECT_ROOT/DOCS_DIR 경로 상수를 추가하여 모든 스크립트가 한 곳에서 경로를 참조. HTML 상대 경로는 papers/ai4s/scisci가 docs/ 하위에서 동일한 형제 관계를 유지하므로 변경 불필요.

**Tech Stack:** Python (pathlib, os.path), Git (git mv), GitHub Pages (/docs source)

---

### Task 1: 디렉토리 생성 + 파일 이동 (git mv)

**Files:**
- Create: `pipeline/`, `pipeline/_img_workflows/`, `pipeline/_img_timelines/`
- Move: 13 .py files → `pipeline/`, `lib/` → `pipeline/lib/`, `workflow/generate_workflow.py` → `pipeline/`
- Move: `papers/` → `docs/papers/`, `ai4s/` → `docs/ai4s/`, `scisci/` → `docs/scisci/`
- Move: `skill/README.md` → `docs/setup-guide.md`
- Delete: `src/`, `_legacy/`, `skill/`, `workflow/`

- [ ] **Step 1: pipeline 디렉토리 생성**

```bash
cd C:/Users/jehyu/Arbeitplatz/paper-curation
mkdir -p pipeline/_img_workflows pipeline/_img_timelines/ai4s pipeline/_img_timelines/scisci
```

- [ ] **Step 2: .py 파일 이동**

```bash
git mv build_category_summaries.py pipeline/
git mv build_papers_index.py pipeline/
git mv build_topic_index.py pipeline/
git mv classify_papers.py pipeline/
git mv config_loader.py pipeline/
git mv generate_timelines.py pipeline/
git mv prepare_deploy.py pipeline/
git mv register_zotero.py pipeline/
git mv review_to_html.py pipeline/
git mv run_update_force.py pipeline/
git mv search_papers.py pipeline/
git mv setup.py pipeline/
git mv sync_zotero.py pipeline/
```

- [ ] **Step 3: lib/ 이동**

```bash
git mv lib pipeline/lib
```

- [ ] **Step 4: workflow → pipeline**

```bash
git mv workflow/generate_workflow.py pipeline/generate_workflow.py
```

workflow/ 내 PNG 파일들은 gitignore되어 있으므로 수동 이동 후 디렉토리 삭제:

```bash
cp workflow/*.png pipeline/_img_workflows/ 2>/dev/null; rm -rf workflow/
```

- [ ] **Step 5: 배포 파일을 docs/로 이동**

```bash
mkdir -p docs
git mv papers docs/papers
git mv ai4s docs/ai4s
git mv scisci docs/scisci
```

- [ ] **Step 6: skill/README.md → docs/setup-guide.md**

```bash
git mv skill/README.md docs/setup-guide.md
rm -rf skill/
```

- [ ] **Step 7: 불필요 디렉토리 삭제**

```bash
rm -rf src/ _legacy/
```

- [ ] **Step 8: 커밋**

```bash
git add -A
git commit -m "refactor: move scripts to pipeline/, deploy files to docs/"
```

---

### Task 2: config_loader.py 경로 상수 추가

**Files:**
- Modify: `pipeline/config_loader.py`

현재 `REPO = Path(__file__).resolve().parent`는 이동 후 `pipeline/`을 가리킨다. project root와 docs 경로를 분리.

- [ ] **Step 1: REPO → PROJECT_ROOT/PIPELINE_DIR/DOCS_DIR 분리**

`pipeline/config_loader.py`의 상단 경로 상수를 다음으로 교체:

```python
PIPELINE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = PIPELINE_DIR.parent
CONFIG_PATH = PROJECT_ROOT / "config.json"

# 배포 파일 경로 (GitHub Pages 서빙 루트)
DOCS_DIR = PROJECT_ROOT / "docs"
PAPERS_DIR = DOCS_DIR / "papers"

# 타임라인/워크플로우 이미지 출력
IMG_TIMELINES_DIR = PIPELINE_DIR / "_img_timelines"
IMG_WORKFLOWS_DIR = PIPELINE_DIR / "_img_workflows"


def get_topic_dir(topic: str) -> Path:
    """docs/{topic} 경로 반환."""
    return DOCS_DIR / topic


def get_papers_index_path() -> Path:
    """papers/_papers_index.json 경로 반환."""
    return PAPERS_DIR / "_papers_index.json"
```

- [ ] **Step 2: 커밋**

```bash
git add pipeline/config_loader.py
git commit -m "feat: add PROJECT_ROOT, DOCS_DIR, PAPERS_DIR path constants to config_loader"
```

---

### Task 3: 각 pipeline 스크립트의 경로 참조 업데이트

**Files:**
- Modify: `pipeline/build_papers_index.py`
- Modify: `pipeline/build_topic_index.py`
- Modify: `pipeline/build_category_summaries.py`
- Modify: `pipeline/classify_papers.py`
- Modify: `pipeline/generate_timelines.py`
- Modify: `pipeline/review_to_html.py`
- Modify: `pipeline/run_update_force.py`
- Modify: `pipeline/prepare_deploy.py`
- Modify: `pipeline/search_papers.py`
- Modify: `pipeline/register_zotero.py`
- Modify: `pipeline/sync_zotero.py`
- Modify: `pipeline/generate_workflow.py`

모든 스크립트에 동일한 패턴 적용: 자체 `REPO` 변수 대신 `config_loader`의 경로 상수를 사용.

- [ ] **Step 1: build_papers_index.py 수정**

현재:
```python
REPO = os.path.dirname(os.path.abspath(__file__))
PAPERS_DIR = os.path.join(REPO, "papers")
```

변경:
```python
from config_loader import PAPERS_DIR, get_papers_index_path
```

`os.path.join(PAPERS_DIR, "_papers_index.json")` → `str(get_papers_index_path())`

- [ ] **Step 2: build_topic_index.py 수정**

현재:
```python
REPO_DIR = os.path.dirname(os.path.abspath(__file__))
PAPERS_DIR = os.path.join(REPO_DIR, "papers")
TOPIC_DIR = os.path.join(REPO_DIR, TOPIC)
```

변경:
```python
from config_loader import PAPERS_DIR as _PAPERS_DIR_PATH, get_topic_dir
PAPERS_DIR = str(_PAPERS_DIR_PATH)
TOPIC_DIR = str(get_topic_dir(TOPIC))
```

Note: 이 스크립트는 `os.path.join(PAPERS_DIR, ...)` 형태를 광범위하게 사용하므로 str로 변환하여 기존 코드와의 호환성 유지.

- [ ] **Step 3: build_category_summaries.py 수정**

현재:
```python
REPO = os.path.dirname(os.path.abspath(__file__))
PAPERS_DIR = os.path.join(REPO, "papers")
topic_dir = os.path.join(REPO, args.topic)
```

변경:
```python
from config_loader import PAPERS_DIR as _PD, get_topic_dir
PAPERS_DIR = str(_PD)
# main() 내부:
topic_dir = str(get_topic_dir(args.topic))
```

- [ ] **Step 4: classify_papers.py 수정**

현재:
```python
REPO = os.path.dirname(os.path.abspath(__file__))
PAPERS_DIR = os.path.join(REPO, "papers")
topic_dir = os.path.join(REPO, args.topic)
```

변경:
```python
from config_loader import PAPERS_DIR as _PD, get_topic_dir
PAPERS_DIR = str(_PD)
# main() 내부:
topic_dir = str(get_topic_dir(args.topic))
```

- [ ] **Step 5: generate_timelines.py 수정**

현재:
```python
REPO = os.path.dirname(os.path.abspath(__file__))
PAPERS_DIR = os.path.join(REPO, "papers")
topic_dir = os.path.join(REPO, topic)
candidates_dir = os.path.join(topic_dir, "timeline_candidates_pb")
```

변경:
```python
from config_loader import PAPERS_DIR as _PD, get_topic_dir, IMG_TIMELINES_DIR
PAPERS_DIR = str(_PD)
# main() 내부:
topic_dir = str(get_topic_dir(topic))
candidates_dir = str(IMG_TIMELINES_DIR / topic)
```

타임라인 deploy 로직도 변경: 1번 후보를 `docs/{topic}/`으로 번호 제거 후 복사.

현재 `deploy_candidate(results, os.path.join(topic_dir, deploy_name))` 호출을 유지하되, 후보 저장은 `IMG_TIMELINES_DIR/{topic}/`에, deploy 복사는 `docs/{topic}/`에 수행.

- [ ] **Step 6: review_to_html.py 수정**

현재:
```python
REPO = os.path.dirname(os.path.abspath(__file__))
PAPERS = os.path.join(REPO, "papers")
```

변경:
```python
from config_loader import PAPERS_DIR
PAPERS = str(PAPERS_DIR)
```

`back_href` 값 (`../../ai4s/index.html`, `../../scisci/index.html`)은 papers에서의 상대 경로이므로 변경 불필요 — docs/ 내에서 형제 관계 동일.

- [ ] **Step 7: run_update_force.py 수정**

현재:
```python
REPO = os.path.dirname(os.path.abspath(__file__))
PAPERS_DIR = os.path.join(REPO, "papers")
CHECKPOINT_FILE = os.path.join(REPO, "_update_force_checkpoint.json")
```

변경:
```python
from config_loader import PAPERS_DIR as _PD, PIPELINE_DIR
PAPERS_DIR = str(_PD)
CHECKPOINT_FILE = str(PIPELINE_DIR / "_update_force_checkpoint.json")
```

또한 `sys.path.insert(0, REPO)` (line 660) → `sys.path.insert(0, str(PIPELINE_DIR))`

- [ ] **Step 8: prepare_deploy.py 수정**

현재:
```python
REPO = os.path.dirname(os.path.abspath(__file__))
```

`papers/`, `ai4s/`, `scisci/` 경로 참조를 `DOCS_DIR` 기준으로 변경:
```python
from config_loader import DOCS_DIR, PAPERS_DIR, PROJECT_ROOT
```

- [ ] **Step 9: search_papers.py 수정**

현재:
```python
output_dir = Path(__file__).resolve().parent / topic
```

변경:
```python
from config_loader import get_topic_dir
output_dir = get_topic_dir(topic)
```

- [ ] **Step 10: register_zotero.py 수정**

현재:
```python
REPO = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(REPO, topic, "_register_results.json")
input_path = args.input or os.path.join(REPO, topic, "_search_results.json")
```

변경:
```python
from config_loader import get_topic_dir
# main() 내부:
topic_dir = str(get_topic_dir(topic))
out_path = os.path.join(topic_dir, "_register_results.json")
input_path = args.input or os.path.join(topic_dir, "_search_results.json")
```

- [ ] **Step 11: sync_zotero.py 수정**

`REPO` 변수가 있다면 `config_loader`의 경로로 교체. `papers/` 참조를 `PAPERS_DIR`로.

- [ ] **Step 12: generate_workflow.py 수정**

현재 `workflow/` 디렉토리 기준이었던 경로를 `pipeline/` 기준으로 변경.

```python
from config_loader import IMG_WORKFLOWS_DIR
# 출력 경로:
output_dir = str(IMG_WORKFLOWS_DIR)
```

- [ ] **Step 13: pipeline/lib/paperbanana.py 수정**

현재:
```python
from config_loader import get_paperbanana_dir
```

이동 후에도 `config_loader`가 같은 `pipeline/` 안에 있으므로 import는 그대로 동작.
단, 이 모듈이 `sys.path`에 의존하는 경우 확인 필요.

- [ ] **Step 14: 전체 스크립트 syntax check**

```bash
cd C:/Users/jehyu/Arbeitplatz/paper-curation
for f in pipeline/*.py pipeline/lib/*.py; do python -c "import ast; ast.parse(open('$f', encoding='utf-8').read())" && echo "OK: $f" || echo "FAIL: $f"; done
```

- [ ] **Step 15: 커밋**

```bash
git add pipeline/
git commit -m "refactor: update all path references to use config_loader constants"
```

---

### Task 4: .gitignore 업데이트

**Files:**
- Modify: `.gitignore`

- [ ] **Step 1: .gitignore 전체 교체**

```gitignore
# Everything excluded by default, then whitelist
*

# Whitelist: core project files
!.gitignore
!.nojekyll
!README.md
!config.example.json

# Pipeline scripts
!pipeline/
!pipeline/*.py
!pipeline/lib/
!pipeline/lib/*.py

# Documentation
!docs/
!docs/**

# GitHub Pages deployment (under docs/)
!docs/papers/
!docs/papers/*/
!docs/papers/*/index.html
!docs/papers/*/review.md
!docs/papers/*/figures/
!docs/papers/*/figures/*.webp

!docs/ai4s/
!docs/ai4s/index.html
!docs/ai4s/*.png
!docs/ai4s/timelines/
!docs/ai4s/timelines/*/
!docs/ai4s/timelines/*/*.png

!docs/scisci/
!docs/scisci/index.html
!docs/scisci/*.png

# Exclude pipeline-generated data (created by running scripts)
docs/ai4s/_*.json
docs/ai4s/_*.txt
docs/ai4s/*.json
docs/scisci/_*.json
docs/scisci/_*.txt
docs/scisci/*.json
docs/papers/*/text.md

# Exclude local config and temp files
config.json
__pycache__/
pipeline/__pycache__/
pipeline/lib/__pycache__/
pipeline/_update_force_checkpoint.json
pipeline/_update_force.log
pipeline/_img_timelines/
pipeline/_img_workflows/
_regen_*.py
```

- [ ] **Step 2: 커밋**

```bash
git add .gitignore
git commit -m "refactor: update .gitignore for pipeline/ + docs/ structure"
```

---

### Task 5: CLAUDE.md 경로 업데이트

**Files:**
- Modify: `CLAUDE.md`

- [ ] **Step 1: CLAUDE.md 내 경로 참조 업데이트**

주요 변경:
- `papers/` → `docs/papers/`
- `papers/_papers_index.json` → `docs/papers/_papers_index.json`
- `papers/{NNN_Slug}/` → `docs/papers/{NNN_Slug}/`
- `ai4s/`, `scisci/` → `docs/ai4s/`, `docs/scisci/`
- Pipeline Scripts 테이블의 스크립트 경로에 `pipeline/` prefix 추가
- Common Commands 섹션의 실행 명령어 업데이트: `python build_topic_index.py` → `python pipeline/build_topic_index.py`
- Architecture 섹션의 디렉토리 설명 업데이트

- [ ] **Step 2: 커밋**

```bash
git add CLAUDE.md
git commit -m "docs: update CLAUDE.md paths for pipeline/ + docs/ structure"
```

---

### Task 6: README.md + setup-guide 링크

**Files:**
- Modify: `README.md`

- [ ] **Step 1: README.md에 setup-guide 링크 추가**

README.md 상단 또는 Getting Started 섹션에 추가:

```markdown
## Getting Started

See the [Setup Guide](docs/setup-guide.md) for installation and configuration instructions.
```

프로젝트 구조 설명도 새 구조에 맞게 업데이트:

```markdown
## Project Structure

```
paper-curation/
├── pipeline/          # Pipeline scripts and libraries
├── docs/              # GitHub Pages site (papers, topic views)
├── config.example.json # Configuration template
└── README.md
```
```

- [ ] **Step 2: 커밋**

```bash
git add README.md
git commit -m "docs: update README.md with new structure and setup-guide link"
```

---

### Task 7: SKILL.md.template 경로 업데이트

**Files:**
- Modify: `SKILL.md.template`

- [ ] **Step 1: 모든 스크립트 경로에 pipeline/ prefix 추가**

`SKILL.md.template` 내 bash 명령어 참조를 업데이트:

- `python search_papers.py` → `python pipeline/search_papers.py`
- `python register_zotero.py` → `python pipeline/register_zotero.py`
- `python run_update_force.py` → `python pipeline/run_update_force.py`
- `python classify_papers.py` → `python pipeline/classify_papers.py`
- `python build_category_summaries.py` → `python pipeline/build_category_summaries.py`
- `python build_papers_index.py` → `python pipeline/build_papers_index.py`
- `python build_topic_index.py` → `python pipeline/build_topic_index.py`
- `python review_to_html.py` → `python pipeline/review_to_html.py`
- `python generate_timelines.py` → `python pipeline/generate_timelines.py`
- `python prepare_deploy.py` → `python pipeline/prepare_deploy.py`

또한 `ai4s/`, `scisci/`, `papers/` 경로 참조를 `docs/` prefix로 업데이트.

- [ ] **Step 2: 커밋**

```bash
git add SKILL.md.template
git commit -m "docs: update SKILL.md.template paths for pipeline/ structure"
```

---

### Task 8: Claude Code skill 파일 업데이트

**Files:**
- Modify: `.claude/skills/*/skill.md` (paper-curation 관련 skill 파일들)

- [ ] **Step 1: paper-curation skill 경로 확인 및 업데이트**

`.claude/skills/` 내 skill.md 파일들에서 스크립트 경로 참조를 `pipeline/` prefix로 업데이트.
`papers/`, `ai4s/`, `scisci/` 경로 참조를 `docs/` prefix로 업데이트.

검색:
```bash
grep -r "python.*\.py\|papers/\|ai4s/\|scisci/" C:/Users/jehyu/Arbeitplatz/paper-curation/.claude/skills/ --include="*.md" -l
```

해당 파일들의 경로 참조를 모두 업데이트.

- [ ] **Step 2: paper-curation-workflow skill 업데이트**

workflow 출력 경로를 `pipeline/_img_workflows/`로 변경.

- [ ] **Step 3: 커밋**

```bash
git add .claude/
git commit -m "docs: update Claude Code skill paths for new structure"
```

---

### Task 9: docs/setup-guide.md 경로 업데이트

**Files:**
- Modify: `docs/setup-guide.md`

- [ ] **Step 1: setup-guide 내 경로 업데이트**

`skill/README.md`에서 이동한 파일이므로 내부의 경로 참조를 새 구조에 맞게 수정:

- `config_loader.py` → `pipeline/config_loader.py`
- 스크립트 실행 예시: `python build_topic_index.py` → `python pipeline/build_topic_index.py`
- 디렉토리 참조 업데이트

- [ ] **Step 2: 커밋**

```bash
git add docs/setup-guide.md
git commit -m "docs: update setup-guide paths for new structure"
```

---

### Task 10: 검증

- [ ] **Step 1: Python syntax 전체 검증**

```bash
cd C:/Users/jehyu/Arbeitplatz/paper-curation
for f in pipeline/*.py pipeline/lib/*.py; do python -c "import ast; ast.parse(open('$f', encoding='utf-8').read())" && echo "OK: $f" || echo "FAIL: $f"; done
```

- [ ] **Step 2: import 경로 검증**

```bash
cd C:/Users/jehyu/Arbeitplatz/paper-curation/pipeline
PYTHONUTF8=1 python -c "from config_loader import DOCS_DIR, PAPERS_DIR, PROJECT_ROOT, get_topic_dir; print(DOCS_DIR); print(PAPERS_DIR); print(get_topic_dir('ai4s'))"
```

Expected output:
```
C:\Users\jehyu\Arbeitplatz\paper-curation\docs
C:\Users\jehyu\Arbeitplatz\paper-curation\docs\papers
C:\Users\jehyu\Arbeitplatz\paper-curation\docs\ai4s
```

- [ ] **Step 3: HTML 상대 경로 검증**

`docs/ai4s/index.html` 내의 `../papers/{slug}/index.html` 링크가 `docs/papers/{slug}/index.html`을 정확히 가리키는지 확인:

```bash
grep -o '../papers/[^"]*' C:/Users/jehyu/Arbeitplatz/paper-curation/docs/ai4s/index.html | head -5
```

`docs/ai4s/`에서 `../papers/`는 `docs/papers/`를 가리키므로 정상.

- [ ] **Step 4: .gitignore 검증**

```bash
cd C:/Users/jehyu/Arbeitplatz/paper-curation
git status
```

- pipeline/*.py 파일들이 tracked 상태인지
- docs/papers/*/index.html, docs/ai4s/index.html 등이 tracked 상태인지
- docs/ai4s/_*.json 등 데이터 파일이 ignored 상태인지
- config.json이 ignored 상태인지

- [ ] **Step 5: 최종 커밋**

```bash
git add -A
git commit -m "chore: verify repo restructure complete"
```

---

### Task 11: GitHub Pages 설정 변경 안내

이 작업은 수동으로 수행:

- [ ] **Step 1: GitHub Settings 변경**

GitHub repo → Settings → Pages → Build and deployment → Source: "Deploy from a branch" → Branch: `master`, Folder: `/docs`

- [ ] **Step 2: push 후 사이트 확인**

```bash
git push origin master
```

배포 후 `https://jehyunlee.github.io/paper-curation/` 에서 사이트가 정상 동작하는지 확인.
