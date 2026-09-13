# 초보자용 간단버전: Paper Curation과 Paper Curio

[English version](beginner.en.md)

논문 한 편을 **안전하게 읽고, 계획을 확인한 뒤, HTML 리뷰로 여는** 첫 경험을 위한 안내입니다.
처음에는 한 편만 처리하세요. 컬렉션 전체 처리·배포·타임라인은 [고급 안내](advanced.md)에서 다룹니다.

![Paper Curation과 Paper Curio의 첫 사용 흐름: 설치, 연결, 논문 선택, 계획 확인, 리뷰 HTML 열기](images/quickstart.png)

그림은 화면 캡처가 아니라 개념도입니다. 텍스트로 보면 다음 순서입니다.

> Paper Curation 설치 → Paper Curio 설치 → 경로와 키 설정 → 로컬 PDF가 있는 상위 논문 항목 선택 → 계획 확인 → 리뷰 실행 → HTML 열기

## 두 도구와 세 가지 경로

| 도구 | 하는 일 | 처음 사용할 때 |
|---|---|---|
| **Paper Curation** | Python 기반 엔진·웹 문서·명령줄. PDF에서 리뷰와 HTML을 만들고, 선택적으로 검색·서지·오디오 등을 실행합니다. | 설치 후 명령줄로 계획을 확인하거나 Curio의 공통 엔진이 됩니다. |
| **Paper Curio** | Zotero 9 플러그인. Zotero의 논문 항목에서 대화, 리뷰, 공통 기능 모듈을 엽니다. | Zotero 안에서 PDF와 대화하거나 리뷰를 요청합니다. |

- **읽기·내보내기**는 키 없이 가능합니다. 기존 리뷰 HTML 열기, 공개 사이트 열람, 로컬 PDF 추출, 키워드 검색 등이 여기에 해당합니다.
- **AI**(리뷰·요약·질의·비교)는 선택한 제공자만 사용하며, 실패해도 다른 회사 모델로 자동 전송하지 않습니다.
- **컬렉션 작업**(색인·서지·타임라인·배포·메일)은 별도의 작업입니다. 한 편의 리뷰는 전체 파이프라인을 시작하지 않습니다.

## 1. Paper Curation 설치

macOS/Linux에서는 **Python 3.12 정확히**가 필요합니다. 3.14 등 다른 버전은 로컬 리뷰에서 거부됩니다. Windows는 로컬 리뷰와 코퍼스 잠금을 지원하지 않지만, 읽기와 AI Chat은 사용할 수 있습니다.

Git과 conda가 설치되어 있어야 합니다. `conda` 명령이 없으면 Miniconda를 먼저 설치하세요. 의존성 다운로드 시간은 환경마다 다릅니다.

```bash
git clone https://github.com/jehyunlee/paper-curation.git
cd paper-curation
conda create -n py312 -c conda-forge python=3.12 pip -y
conda activate py312
pip install -r requirements.txt
PYTHONUTF8=1 python pipeline/setup.py
python pipeline/run_feature.py --list
```

마지막 명령이 기능 목록 JSON을 출력하면 기본 설치가 끝났습니다. `setup.py`는 키를 묻지 않고 네트워크 호출이나 전체 파이프라인을 실행하지 않습니다. 설치 문제와 다른 운영체제 안내는 [설치 안내](../setup-guide.md)를 따르세요.

## 2. Paper Curio 설치 및 연결

1. [Paper Curio 최신 릴리스](https://github.com/jehyunlee/paper-curio/releases/latest)에서 `paper-curio.xpi`를 받습니다.
2. Zotero 9에서 **Tools → Plugins → ⚙️ → Install Plugin From File…**를 열고 XPI를 선택합니다.
3. Zotero → **Settings → Paper Curio → 출력 위치**에서 다음을 설정합니다.

| 항목 | 값 |
|---|---|
| **paper-curation 루트 경로** | 방금 클론한 폴더의 절대 경로. 그 안에 `docs/papers/`가 있어야 합니다. |
| **Python 경로** | 비워 두면 기본 conda `py312`를 사용합니다. 다른 환경이면 해당 Python 3.12 인터프리터 경로를 입력합니다. |
| **Fallback 출력 경로** | paper-curation 없는 컴퓨터에서 기존 리뷰를 열람할 위치입니다. 새 리뷰를 만들 수는 없습니다. |

설정 창의 상태가 “연동됨”이면 Enhanced 모드가 준비된 것입니다. 연동하지 않아도 Light 모드에서 AI Chat과 Comparative Chat을 쓸 수 있지만, API 키가 필요합니다.

## 3. 키와 비용을 안전하게 설정하기

기존 HTML 읽기는 키가 필요 없지만, 클라우드 리뷰·대화 등 새 AI 결과를 생성할 때는 키가 필요합니다. Zotero → **Settings → Paper Curio → API 키**에서 **리뷰 제공자** 하나를 고르고, 해당 키를 입력한 뒤 **OS 키 저장소에 저장**을 누르세요.

- 설정에는 `credential:<provider>` 참조만 남고, 값은 OS 키 저장소에 보관됩니다. 빈 값을 저장하면 키를 삭제합니다.
- 키를 `config.json`, 요청 JSON, 명령줄 인자, 메모에 넣지 마세요. 자동화에서는 환경변수가 OS 키 저장소보다 우선합니다.
- Claude/GJC OAuth 구독 로그인은 이 파이프라인의 API 자격증명이 아닙니다. 선택한 제공자의 API 키 또는 올바르게 주입한 환경변수를 사용해야 합니다.
- **리뷰 비용 상한**은 선택 사항입니다. 설정하면 현재 제공자의 입력·출력 100만 토큰당 USD 단가도 함께 입력해야 하며, 단가를 모르면 실행이 차단됩니다. 가격을 추정해 적지 마세요.

## 4. Zotero에서 첫 리뷰 만들기

1. Zotero에서 **PDF 첨부 줄이 아닌 상위 논문 항목** 하나를 선택합니다. 접근 가능한 로컬 PDF가 첨부되어야 합니다.
2. 우클릭 → **paper-curation Review 생성**을 선택합니다.
3. 계획 창에서 제공자·모델, `docs/papers/{번호}_{제목}/` 아래의 Output 경로, 예상 비용과 상한을 읽습니다.
4. 맞으면 OK로 이 리뷰만 실행합니다. 취소하면 API 호출 없이 예약을 해제합니다. 예약이 있으므로 계획 단계에 파일이 절대 생기지 않는다고 가정하지 마세요.
5. 완료 뒤 우클릭 → **paper-curation Review HTML 열기**를 선택합니다.

성공하면 `review.md`, `index.html`, `bibliography.json`이 출력 폴더에 생기며, HTML이 브라우저에서 열립니다. “리뷰 완료 … **서지 DB 반영 대기**”는 리뷰 실패가 아니라 전역 서지 DB 갱신이 아직 별도라는 뜻입니다.

이미 완성된 리뷰는 기본적으로 건너뜁니다. 다시 만들려면 **기존 review 덮어쓰기 (Overwrite existing)**를 켜되, Paper Curio가 직접 만든 리뷰는 이 설정과 무관하게 재생성됩니다.

## 5. Zotero 없이 명령줄로 한 편 처리하기

아래 내용을 `request.json`으로 저장합니다. 경로와 서지정보를 실제 값으로 바꾸고, 먼저 계획만 확인하세요. 키 자체는 넣지 않습니다.

```json
{
  "schema_version": 1,
  "feature": "review",
  "pdf_path": "/absolute/path/to/paper.pdf",
  "output_dir": "/absolute/path/to/output/paper-slug",
  "item": {
    "key": "LOCAL_ITEM_KEY", "title": "Paper title",
    "creators": [{"firstName": "Ada", "lastName": "Lovelace", "creatorType": "author"}],
    "date": "2026", "DOI": "10.0000/example", "abstractNote": "Abstract text",
    "url": "https://example.org/paper", "publicationTitle": "Journal name"
  },
  "overwrite": false,
  "provider": "anthropic",
  "credential_ref": "credential:anthropic"
}
```

```bash
python pipeline/local_review.py --request request.json
python pipeline/local_review.py --request request.json --execute
```

첫 명령에서 `ready`인지 확인한 뒤에만 둘째 명령을 실행합니다. `completed`는 완료, `exists`는 같은 완성 리뷰가 이미 있다는 뜻입니다. `needs-key`, `needs-runtime`, `insufficient-data`는 실행 전에 고칠 수 있는 상태입니다. 더 많은 제공자·예산·출력 계약은 [설치 안내의 단일 PDF 예시](../setup-guide.md#단일-pdf-로컬-리뷰)를 보세요.

## 다음으로 할 수 있는 일

- **로컬 대화·요약:** **(adv.) run Paper Curation modules → 논문 AI**에서 선택 PDF 본문을 준비한 뒤, 설치·실행 중인 Ollama `qwen3.8:27b-mlx`로 요약·질의를 실행할 수 있습니다. 클라우드 API 요금은 없지만 로컬 연산 자원을 사용합니다. 기존 **AI Chat — single** 메뉴와는 다른 경로이며, 리뷰와 비교는 클라우드 제공자 기능입니다.
- **근거 기반 요약·질의·비교:** 우클릭 메뉴 맨 아래의 **(adv.) run Paper Curation modules**에서 카드를 열고 **실행 계획 확인** 후 **선택 작업 실행**을 누릅니다. 입력을 바꾸면 계획을 다시 만듭니다.
- 검색 색인, 서지 갱신, 컬렉션 전체 처리, 배포와 이메일은 [고급 안내](advanced.md)에서 계획·확인·권한을 먼저 확인하세요.

## 짧은 문제 해결

| 보이는 상태 또는 증상 | 확인할 것 |
|---|---|
| `needs-key` | **API 키**에서 선택한 제공자의 키를 **OS 키 저장소에 저장**했는지 확인합니다. |
| `needs-runtime` | **출력 위치**의 루트와 Python 3.12, 의존성 설치를 확인합니다. |
| `insufficient-data` | 상위 논문 항목을 선택했고 접근 가능한 로컬 PDF가 있는지 확인합니다. |
| `busy` 또는 예약 관련 메시지 | 다른 코퍼스 작업이나 예약이 끝난 뒤 다시 시도합니다. |
| HTML은 열리는데 목록이 갱신되지 않음 | `partial`일 수 있습니다. 리뷰 파일은 보존되므로 HTML을 열고, 같은 항목을 다시 실행해 등록을 재시도합니다. |
| Windows에서 리뷰 생성 실패 | macOS/Linux의 Python 3.12 환경에서 로컬 리뷰를 실행합니다. Windows에서는 읽기와 AI Chat을 사용합니다. |

더 넓은 기능의 출발점은 [매뉴얼 목차](index.md), 설치 세부사항은 [설치 안내](../setup-guide.md), 운영 작업은 [고급 안내](advanced.md)입니다.
