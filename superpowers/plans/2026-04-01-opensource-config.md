# Open-Source Config 체계 구현 계획

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 하드코딩된 개인 정보를 config.json 기반 설정으로 전환하여 오픈소스 배포 가능하게 만든다.

**Architecture:** `config_loader.py`의 기존 하이브리드 패턴(config.json 우선, 환경변수 폴백)을 확장하여 Zotero PDF 경로, GitHub 설정을 추가한다. SKILL.md는 템플릿 변수 방식으로 전환하고 `setup.py`가 설치 시 치환한다. PaperBanana 래퍼를 프로젝트 내부로 복사하고 config 전용 경로 결정으로 변경한다.

**Tech Stack:** Python 3, JSON config, Git

**Spec:** `docs/superpowers/specs/2026-04-01-opensource-config-design.md`

---

## File Structure

| 파일 | 역할 | 작업 |
|------|------|------|
| `config.json` | 실제 설정 (비커밋) | 수정: `zotero.pdf_dir`, `github` 추가, `scisci_lib` 제거 |
| `config.example.json` | 예시 설정 (커밋) | 신규 생성 |
| `config_loader.py` | 설정 로더 | 수정: 4개 함수 추가, 1개 제거 |
| `lib/__init__.py` | lib 패키지 | 신규 (빈 파일) |
| `lib/paperbanana.py` | PaperBanana 래퍼 | 외부에서 복사 + 경로 로직 수정 |
| `run_update_force.py` | 배치 실행 | 수정: ZOTERO_DIR → config |
| `classify_papers.py` | 분류 | 수정: COLLECTIONS → config |
| `prepare_deploy.py` | 배포 준비 | 수정: branch → config |
| `generate_timelines.py` | 타임라인 생성 | 수정: 외부 경로 → lib import |
| `workflow/generate_workflow.py` | 워크플로우 다이어그램 | 수정: 외부 경로 → lib import |
| `setup.py` | 설치 스크립트 | 신규 생성 |
| `.gitignore` | Git 제외 설정 | 수정: `!lib/` 추가 |

---

### Task 1: config.json 확장 + config.example.json 생성

**Files:**
- Modify: `config.json`
- Create: `config.example.json`

- [ ] **Step 1: config.json에 새 필드 추가, scisci_lib 제거**

```json
{
  "zotero": {
    "api_key": "4R2R3iQKe7I7NBHWlCWDRk8X",
    "email": "jehyun.lee@gmail.com",
    "collections": {
      "ai4s": "AI assisted Research",
      "scisci": "Science of Science"
    },
    "pdf_dir": "C:\\Users\\jehyu\\GoogleDrive\\Zotero"
  },
  "unpaywall_email": "jehyun.lee@gmail.com",
  "github": {
    "repo": "jehyunlee/paper-curation",
    "branch": "master",
    "pages_base_url": "https://jehyunlee.github.io/paper-curation"
  },
  "paperbanana_dir": "C:\\Users\\jehyu\\Arbeitplatz\\01_Work\\01_Devs\\AX\\paperbanana"
}
```

- [ ] **Step 2: config.example.json 생성**

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

- [ ] **Step 3: 검증**

```bash
cd C:/Users/jehyu/Arbeitplatz/paper-curation
PYTHONUTF8=1 python -c "from config_loader import load_config; c = load_config(); print(c.get('github')); print(c['zotero'].get('pdf_dir'))"
```

Expected: `{'repo': 'jehyunlee/paper-curation', 'branch': 'master', ...}` 출력, `pdf_dir` 출력.

- [ ] **Step 4: 커밋**

```bash
git add config.example.json
git commit -m "Add config.example.json and extend config schema with github/zotero.pdf_dir"
```

주의: `config.json`은 `.gitignore`에 이미 포함되어 커밋되지 않음.

---

### Task 2: config_loader.py 확장

**Files:**
- Modify: `config_loader.py`

- [ ] **Step 1: 새 함수 4개 추가, get_scisci_lib 제거**

`config_loader.py` 끝부분에서 `get_scisci_lib()` 삭제하고, 아래 함수들을 추가:

```python
def get_zotero_dir():
    """Zotero PDF 저장 디렉토리."""
    cfg = load_config()
    return (cfg.get("zotero", {}).get("pdf_dir", "")
            or os.environ.get("ZOTERO_DIR", ""))


def get_github_repo():
    """GitHub repo (owner/repo 형식)."""
    cfg = load_config()
    return (cfg.get("github", {}).get("repo", "")
            or os.environ.get("GITHUB_REPO", ""))


def get_github_branch():
    """GitHub branch (기본 master)."""
    cfg = load_config()
    return (cfg.get("github", {}).get("branch", "")
            or os.environ.get("GITHUB_BRANCH", "master"))


def get_pages_base_url():
    """GitHub Pages base URL."""
    cfg = load_config()
    return (cfg.get("github", {}).get("pages_base_url", "")
            or os.environ.get("PAGES_BASE_URL", ""))
```

- [ ] **Step 2: 검증**

```bash
PYTHONUTF8=1 python -c "
from config_loader import get_zotero_dir, get_github_repo, get_github_branch, get_pages_base_url
print('zotero_dir:', get_zotero_dir())
print('github_repo:', get_github_repo())
print('github_branch:', get_github_branch())
print('pages_base_url:', get_pages_base_url())
"
```

Expected: config.json의 값들이 출력.

```bash
PYTHONUTF8=1 python -c "from config_loader import get_scisci_lib" 2>&1
```

Expected: `ImportError` — 함수가 삭제되었으므로.

- [ ] **Step 3: 커밋**

```bash
git add config_loader.py
git commit -m "Extend config_loader: add github/zotero_dir getters, remove get_scisci_lib"
```

---

### Task 3: lib/paperbanana.py 복사 + 경로 로직 수정

**Files:**
- Create: `lib/__init__.py`
- Create: `lib/paperbanana.py` (외부에서 복사 후 수정)

- [ ] **Step 1: lib 디렉토리 및 __init__.py 생성**

```bash
mkdir -p C:/Users/jehyu/Arbeitplatz/paper-curation/lib
touch C:/Users/jehyu/Arbeitplatz/paper-curation/lib/__init__.py
```

- [ ] **Step 2: paperbanana.py 복사**

```bash
cp "C:/Users/jehyu/Arbeitplatz/01_Work/01_Devs/AX/scisci/scie/lib/paperbanana.py" \
   C:/Users/jehyu/Arbeitplatz/paper-curation/lib/paperbanana.py
```

- [ ] **Step 3: PAPERBANANA_DIR 결정 로직을 config 전용으로 수정**

`lib/paperbanana.py`의 기존 경로 탐색 로직 (line 13-16):

```python
# Vendored copy (inside scisci repo) takes priority over external install
_VENDORED_DIR = Path(__file__).resolve().parent.parent / "vendor" / "paperbanana"
_EXTERNAL_DIR = Path(__file__).resolve().parent.parent.parent.parent / "paperbanana"
PAPERBANANA_DIR = _VENDORED_DIR if _VENDORED_DIR.exists() else _EXTERNAL_DIR
```

이를 다음으로 교체:

```python
import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from config_loader import get_paperbanana_dir

_pb_dir = get_paperbanana_dir()
if not _pb_dir:
    raise ValueError(
        "paperbanana_dir not set. "
        "Set it in config.json or PAPERBANANA_DIR env var. "
        "Clone from: https://github.com/dwzhu-pku/PaperBanana"
    )
PAPERBANANA_DIR = Path(_pb_dir)
```

- [ ] **Step 4: 검증**

```bash
PYTHONUTF8=1 python -c "from lib.paperbanana import PAPERBANANA_DIR; print(PAPERBANANA_DIR)"
```

Expected: `C:\Users\jehyu\Arbeitplatz\01_Work\01_Devs\AX\paperbanana` 출력.

- [ ] **Step 5: 커밋**

```bash
git add -f lib/__init__.py lib/paperbanana.py
git commit -m "Add lib/paperbanana.py wrapper with config-based path resolution"
```

---

### Task 4: 스크립트 수정 — run_update_force.py

**Files:**
- Modify: `run_update_force.py:33`

- [ ] **Step 1: ZOTERO_DIR 하드코딩 제거**

기존 (line 33):
```python
ZOTERO_DIR = r"C:\Users\jehyu\GoogleDrive\Zotero"
```

교체:
```python
from config_loader import get_zotero_dir
ZOTERO_DIR = get_zotero_dir()
```

주의: line 36의 기존 `from config_loader import ...`에 `get_zotero_dir`를 합쳐도 됨:

```python
from config_loader import get_zotero_api_key, get_zotero_user_id, get_collection_key, get_collections, get_zotero_dir
```

그 후 line 33을 `ZOTERO_DIR = get_zotero_dir()`로 변경.

- [ ] **Step 2: 검증**

```bash
PYTHONUTF8=1 python -c "
import run_update_force
print('ZOTERO_DIR:', run_update_force.ZOTERO_DIR)
"
```

Expected: `C:\Users\jehyu\GoogleDrive\Zotero` 출력 (config.json에서 읽음).

- [ ] **Step 3: 커밋**

```bash
git add run_update_force.py
git commit -m "run_update_force: use config for ZOTERO_DIR instead of hardcoded path"
```

---

### Task 5: 스크립트 수정 — classify_papers.py

**Files:**
- Modify: `classify_papers.py:20-24`

- [ ] **Step 1: COLLECTIONS 하드코딩 제거**

기존 (line 24):
```python
COLLECTIONS = {"ai4s": "WKEZLEE8", "scisci": "3KVIDDKH"}
```

교체 — line 20의 import에 추가하고 line 24를 변경:

```python
from config_loader import get_collections

COLLECTIONS = get_collections()
```

주의: `config_loader`는 이미 collection 이름 → key 자동 변환을 지원하므로 (`_resolve_collection_value`), config.json에 이름으로 지정하면 API를 통해 key를 자동 조회한다.

- [ ] **Step 2: 검증**

```bash
PYTHONUTF8=1 python -c "
import classify_papers
print('COLLECTIONS:', classify_papers.COLLECTIONS)
"
```

Expected: `{'ai4s': 'WKEZLEE8', 'scisci': '3KVIDDKH'}` (이름이 key로 자동 변환됨).

- [ ] **Step 3: 커밋**

```bash
git add classify_papers.py
git commit -m "classify_papers: use config for COLLECTIONS instead of hardcoded keys"
```

---

### Task 6: 스크립트 수정 — prepare_deploy.py

**Files:**
- Modify: `prepare_deploy.py:19,203`

- [ ] **Step 1: git push에서 branch를 config에서 읽도록 수정**

파일 상단 import 영역 (line 19 이후)에 추가:

```python
from config_loader import get_github_branch
```

기존 (line 203):
```python
subprocess.run(["git", "push", "origin", "master"], check=True)
```

교체:
```python
branch = get_github_branch()
subprocess.run(["git", "push", "origin", branch], check=True)
```

- [ ] **Step 2: 검증**

```bash
PYTHONUTF8=1 python -c "
import prepare_deploy
from config_loader import get_github_branch
print('branch:', get_github_branch())
"
```

Expected: `master` 출력.

- [ ] **Step 3: 커밋**

```bash
git add prepare_deploy.py
git commit -m "prepare_deploy: use config for git branch instead of hardcoded 'master'"
```

---

### Task 7: generate_timelines.py + workflow/generate_workflow.py 수정

**Files:**
- Modify: `generate_timelines.py:39-47`
- Modify: `workflow/generate_workflow.py:19-27`

- [ ] **Step 1: generate_timelines.py의 외부 경로 로직 제거**

기존 (line 39-47):
```python
from config_loader import get_paperbanana_dir, get_scisci_lib

SCISCI_LIB = get_scisci_lib()
PAPERBANANA_DIR = get_paperbanana_dir()
if SCISCI_LIB:
    sys.path.insert(0, SCISCI_LIB)
if PAPERBANANA_DIR:
    sys.path.insert(0, PAPERBANANA_DIR)
```

교체:
```python
# PaperBanana wrapper (config.json의 paperbanana_dir 경로 사용)
# generate_diagram()만 사용: from lib.paperbanana import generate_diagram
```

주의: `generate_diagram`의 실제 import는 파일 내에서 지연 import (`from lib.paperbanana import generate_diagram`)로 이미 사용되고 있을 수 있음. 파일 전체에서 `from lib.paperbanana import generate_diagram` 또는 `from paperbanana import generate_diagram` 패턴을 확인하고, `lib.paperbanana`로 통일한다.

generate_timelines.py line 324 부근:
```python
    from lib.paperbanana import generate_diagram
```

이 import가 이미 `lib.paperbanana`를 가리키도록 변경. 기존이 `from lib.paperbanana import generate_diagram`이면 그대로. 기존이 다른 경로면 수정.

- [ ] **Step 2: workflow/generate_workflow.py의 외부 경로 로직 제거**

기존 (line 19-27):
```python
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))  # repo root for config_loader
from config_loader import get_paperbanana_dir, get_scisci_lib

SCISCI_LIB = get_scisci_lib()
PAPERBANANA_DIR = get_paperbanana_dir()
if SCISCI_LIB:
    sys.path.insert(0, SCISCI_LIB)
if PAPERBANANA_DIR:
    sys.path.insert(0, PAPERBANANA_DIR)
```

교체:
```python
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))  # repo root
```

그리고 파일 내 `from lib.paperbanana import generate_diagram` (line 145 부근)이 정상 동작하는지 확인.

- [ ] **Step 3: 검증**

```bash
PYTHONUTF8=1 python -c "
import generate_timelines
print('import OK')
"
```

```bash
PYTHONUTF8=1 python -c "
import sys; sys.path.insert(0, 'workflow/..'); 
from lib.paperbanana import generate_diagram
print('lib.paperbanana import OK')
"
```

Expected: 둘 다 에러 없이 import 성공.

- [ ] **Step 4: 커밋**

```bash
git add generate_timelines.py workflow/generate_workflow.py
git commit -m "Remove external sys.path dependencies, use lib.paperbanana wrapper"
```

---

### Task 8: 레거시 스크립트 삭제

**Files:**
- Delete: `ai4s/zotero_register.py`
- Delete: `ai4s/process_zotero_bulk.py`
- Delete: `scisci/zotero_register.py`
- Delete: `scisci/fetch_zotero_scisci.py`
- Delete: `scisci/_fix_pdfs.py`
- Delete: `scisci/_fix_pdfs_round2.py`

- [ ] **Step 1: 삭제 전 다른 파일에서 참조되지 않는지 확인**

```bash
cd C:/Users/jehyu/Arbeitplatz/paper-curation
grep -r "zotero_register\|process_zotero_bulk\|fetch_zotero_scisci\|_fix_pdfs" --include="*.py" \
  | grep -v "ai4s/zotero_register\|ai4s/process_zotero_bulk\|scisci/zotero_register\|scisci/fetch_zotero_scisci\|scisci/_fix_pdfs"
```

Expected: 매칭 없음 (다른 파일에서 import하지 않음).

- [ ] **Step 2: 파일 삭제**

```bash
rm ai4s/zotero_register.py
rm ai4s/process_zotero_bulk.py
rm scisci/zotero_register.py
rm scisci/fetch_zotero_scisci.py
rm scisci/_fix_pdfs.py
rm scisci/_fix_pdfs_round2.py
```

- [ ] **Step 3: 커밋**

```bash
git add -A ai4s/zotero_register.py ai4s/process_zotero_bulk.py \
  scisci/zotero_register.py scisci/fetch_zotero_scisci.py \
  scisci/_fix_pdfs.py scisci/_fix_pdfs_round2.py
git commit -m "Delete legacy scripts replaced by run_update_force.py and sync_zotero.py"
```

---

### Task 9: .gitignore에 lib/ 화이트리스트 추가

**Files:**
- Modify: `.gitignore`

- [ ] **Step 1: lib/ 디렉토리 화이트리스트 추가**

`.gitignore`의 `!workflow/` 라인 아래에 추가:

```
!lib/
!lib/*.py
```

- [ ] **Step 2: setup.py 화이트리스트 추가**

`!*.py`가 루트의 .py를 이미 커버하고, `setup.py`도 루트에 있으므로 추가 불필요.

`!docs/` 관련 화이트리스트도 확인:

```
!docs/
!docs/**
```

- [ ] **Step 3: 검증**

```bash
git status -u
```

Expected: `lib/__init__.py`, `lib/paperbanana.py`가 untracked로 보임 (화이트리스트 적용).

- [ ] **Step 4: 커밋**

```bash
git add .gitignore
git commit -m "Whitelist lib/ and docs/ in .gitignore"
```

---

### Task 10: SKILL.md 템플릿화

**Files:**
- Create: `SKILL.md.template` (기존 SKILL.md를 복사 후 플레이스홀더 치환)

이 작업은 `~/.claude/skills/paper-curation/SKILL.md`를 대상으로 한다.

- [ ] **Step 1: SKILL.md를 SKILL.md.template로 복사**

```bash
cp ~/.claude/skills/paper-curation/SKILL.md \
   C:/Users/jehyu/Arbeitplatz/paper-curation/SKILL.md.template
```

- [ ] **Step 2: 플레이스홀더 치환**

`SKILL.md.template`에서 다음을 검색-치환:

| 검색 | 치환 |
|------|------|
| `jehyunlee/paper-curation` | `{github_repo}` |
| `https://jehyunlee.github.io/paper-curation` | `{pages_base_url}` |
| `https://jehyunlee.github.io/` (단독 사용) | `{pages_base_url}/` (context에 따라) |
| `C:\Users\jehyu\GoogleDrive\Zotero` | `{zotero_dir}` |
| `C:/Users/jehyu/GoogleDrive/Zotero` | `{zotero_dir}` |
| `C:/Users/jehyu/Arbeitplatz/paper-curation` | `{project_dir}` |
| `C:\Users\jehyu\Arbeitplatz\paper-curation` | `{project_dir}` |
| `jehyun.lee@gmail.com` (SKILL 내) | `{email}` |

주의: 모든 변형(슬래시 방향, 이스케이프)을 처리. `jehyunlee.github.io`가 `pages_base_url` 안에 포함된 경우만 치환하고, 단독 `jehyunlee` 언급(credit 등)은 유지할 수 있음 — 판단 필요.

- [ ] **Step 3: 검증 — 하드코딩된 개인 정보가 남아있지 않은지 확인**

```bash
grep -n "jehyunlee\|jehyun\.lee\|1356104\|GoogleDrive\|C:\\\\Users\\\\jehyu" SKILL.md.template
```

Expected: 매칭 없음 (credit 라인 제외 가능).

- [ ] **Step 4: 커밋**

```bash
git add -f SKILL.md.template
git commit -m "Add SKILL.md.template with placeholder variables for open-source distribution"
```

---

### Task 11: setup.py 생성

**Files:**
- Create: `setup.py`

- [ ] **Step 1: setup.py 작성**

```python
"""
paper-curation 설치 스크립트.

config.json → SKILL.md 플레이스홀더 치환.

Usage:
  python setup.py
"""

import json
import os
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
CONFIG_PATH = REPO / "config.json"
EXAMPLE_PATH = REPO / "config.example.json"
TEMPLATE_PATH = REPO / "SKILL.md.template"
SKILL_OUTPUT = REPO / "SKILL.md"
GITIGNORE_PATH = REPO / ".gitignore"


def main():
    # Step 1: config.json 확인
    if not CONFIG_PATH.exists():
        if EXAMPLE_PATH.exists():
            shutil.copy2(EXAMPLE_PATH, CONFIG_PATH)
            print(f"config.example.json → config.json 복사 완료.")
        else:
            print("ERROR: config.example.json이 없습니다.")
            sys.exit(1)
        print(f"config.json을 편집한 후 다시 실행해주세요: {CONFIG_PATH}")
        sys.exit(0)

    # Step 2: config.json 로드
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        cfg = json.load(f)

    zotero = cfg.get("zotero", {})
    github = cfg.get("github", {})

    replacements = {
        "{github_repo}": github.get("repo", ""),
        "{pages_base_url}": github.get("pages_base_url", ""),
        "{zotero_dir}": zotero.get("pdf_dir", ""),
        "{project_dir}": str(REPO),
        "{email}": zotero.get("email", "") or cfg.get("unpaywall_email", ""),
    }

    # 값 검증
    missing = [k for k, v in replacements.items() if not v]
    if missing:
        print(f"WARNING: config.json에 빈 값: {', '.join(missing)}")
        print("SKILL.md의 해당 플레이스홀더가 빈 문자열로 치환됩니다.")

    # Step 3: SKILL.md.template → SKILL.md 치환
    if TEMPLATE_PATH.exists():
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            content = f.read()

        for placeholder, value in replacements.items():
            content = content.replace(placeholder, value)

        with open(SKILL_OUTPUT, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"SKILL.md 생성 완료: {SKILL_OUTPUT}")
    else:
        print(f"SKILL.md.template이 없습니다. 건너뜁니다.")

    # Step 4: .gitignore에 config.json 확인
    if GITIGNORE_PATH.exists():
        gi = GITIGNORE_PATH.read_text(encoding="utf-8")
        if "config.json" not in gi:
            with open(GITIGNORE_PATH, "a", encoding="utf-8") as f:
                f.write("\nconfig.json\n")
            print(".gitignore에 config.json 추가.")

    print("\n설치 완료!")
    print(f"  Config: {CONFIG_PATH}")
    if SKILL_OUTPUT.exists():
        print(f"  SKILL:  {SKILL_OUTPUT}")
        print(f"\n  SKILL.md를 Claude Code skills 디렉토리에 복사하세요:")
        print(f"    cp {SKILL_OUTPUT} ~/.claude/skills/paper-curation/SKILL.md")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: 검증**

```bash
PYTHONUTF8=1 python setup.py
```

Expected: config.json이 이미 존재하므로 SKILL.md 치환 실행. `SKILL.md 생성 완료` 출력.

```bash
grep "jehyunlee" SKILL.md 2>/dev/null | head -5
```

Expected: 하드코딩 없음 (config.json의 실제 값으로 치환됨).

- [ ] **Step 3: 커밋**

```bash
git add setup.py
git commit -m "Add setup.py for config-based SKILL.md template substitution"
```

---

### Task 12: 최종 검증 + 정리 커밋

- [ ] **Step 1: 전체 import 검증**

```bash
cd C:/Users/jehyu/Arbeitplatz/paper-curation
PYTHONUTF8=1 python -c "
from config_loader import (
    load_config, get_zotero_api_key, get_zotero_user_id,
    get_collections, get_zotero_dir,
    get_github_repo, get_github_branch, get_pages_base_url,
    get_paperbanana_dir, get_unpaywall_email
)
print('config_loader OK')

from lib.paperbanana import PAPERBANANA_DIR
print(f'paperbanana_dir: {PAPERBANANA_DIR}')

import run_update_force
print(f'ZOTERO_DIR: {run_update_force.ZOTERO_DIR}')

import classify_papers
print(f'COLLECTIONS: {classify_papers.COLLECTIONS}')

from config_loader import get_github_branch
print(f'branch: {get_github_branch()}')
"
```

Expected: 모든 import 성공, 올바른 값 출력.

- [ ] **Step 2: 하드코딩 잔여 확인**

```bash
grep -rn "jehyun\.lee@gmail\|1356104\|C:\\\\Users\\\\jehyu\\\\GoogleDrive" --include="*.py" \
  | grep -v "_legacy/" | grep -v "__pycache__"
```

Expected: 활성 스크립트에 매칭 없음.

- [ ] **Step 3: git status 확인 및 최종 커밋**

```bash
git status
```

모든 변경이 커밋되었는지 확인. 미커밋 파일이 있으면 정리.
