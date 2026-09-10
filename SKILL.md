---
name: paper-curation
description: "논문 읽기·리뷰·근거 기반 요약/대화·검색·서지·오디오·타임라인을 선택 실행한다. 공통 기능 계약은 pipeline/features.json과 pipeline/run_feature.py이며, 전체 큐레이션과 배포는 별도 명시적 작업이다."
---

# Paper Curation — Selected Capability Dispatcher

## Execution boundary

- 작업 디렉터리는 설치된 paper-curation checkout이다. 기본 설치는 `python pipeline/setup.py`이며 키 입력·모델 실행·원격 동기화·배포를 시작하지 않는다.
- 먼저 `python pipeline/run_feature.py --list`로 실제 지원 기능과 요구사항을 읽는다. 기능 ID·입력 스키마·전송 대상은 `pipeline/features.json`이 단일 출처다.
- 사용자에게 요청받지 않은 모듈을 추가하지 않는다. 리뷰 하나를 요청받았으면 분류·의미 검색·오디오·그림·메일·배포를 연쇄 실행하지 않는다.
- 요청은 JSON **파일**로 만든다. `--request`에 JSON 문자열이나 비밀값을 넘기지 않는다.
- `python pipeline/run_feature.py --request feature-request.json`은 계획이다. 실행은 기능·대상·제공자·전송 대상·비용 계획을 확인한 뒤 `--execute`로 명시한다.
- 실패를 성공으로 바꾸거나 다른 회사로 자동 재전송하지 않는다. 지원하지 않는 기능/런타임/권한, 자료 부족, 비용 상한 초과를 그대로 보고한다.

## Routes

| 목적 | 경로 |
|---|---|
| 기존 문서 읽기 | 기존 HTML/PDF 열람. 키와 생성 작업 불필요 |
| 로컬 PDF 리뷰 | `local_review.py --request review-request.json`, 확인 후 `--execute` |
| 요약·근거 기반 질의·비교 | `run_feature.py`의 `summary` / `chat` / `comparison` |
| 키워드 색인·조회 | `keyword-search`, `params.operation`은 `build` 또는 `query` |
| 의미 색인·조회 | `semantic-search`, Google 임베딩은 이 기능에서만 요구 |
| 서지·기관 DB 반영 | `bibliography-update`, 기본 offline/changed-only/skip-zotero/no-email |
| 공개 기관표 | `institution-export`, 원본 DB·개인정보를 직접 공개하지 않음 |
| 오디오 | `audio`, 기존 리뷰/검증된 대본 → MP3, 메일 자동 발송 없음 |
| 타임라인 | `timeline-text`와 `timeline-image`를 별도로 실행 |
| 동기화·공개·이메일 | `zotero-sync`, `publish`, `email`을 각각 명시적으로 선택 |

정확한 입력 예시와 생성된 기능표는 `docs/setup-guide.md`를 따른다. 없는 입력을 임의로 채우거나 빈 `params`를 완성된 요청으로 제시하지 않는다.

## Providers and credentials

- 리뷰 기본 모델은 Anthropic `claude-sonnet-5`. OpenAI/Google은 명시적 대안이며 동일한 리뷰 스키마 검증을 통과해야 한다.
- 로컬 모델은 Ollama `qwen3.8:27b-mlx` 하나다. 요약·근거 기반 대화용이며 리뷰/비전/임베딩/TTS의 자동 대체 수단이 아니다.
- 자격증명은 환경변수 우선, 다음은 OS keyring 서비스 `paper-curation`이다. 요청/설정에는 `credential:<provider>` 참조만 둔다. 평문 config/file fallback은 없다.
- 키를 argv·요청 JSON·로그·공유 HTML에 쓰지 않는다. `credentials.py --operation read`는 private subprocess pipe 전용이며 터미널에 출력하지 않는다.
- 키 저장은 Curio 설정의 OS 저장 버튼 또는 getpass → stdin 경로를 사용한다:

```bash
python -c 'import getpass,sys; sys.stdout.write(getpass.getpass())' | python pipeline/credentials.py --operation write --provider anthropic
python pipeline/credentials.py --operation status --provider anthropic
```

- API 키 설정과 API 사용 권한·잔액·발신 도메인 인증은 다르다. 사전 검사가 확인하지 않은 권한을 검증됐다고 말하지 않는다.
- 비용 상한은 명시한 요율과 보수적인 토큰 상한으로 검사한다. 요율/비용 산정이 불가능한 유료 기능에는 상한 보장을 꾸며내지 않고 `budget-unavailable`로 차단한다.

## Corpus safety

- Curio는 Python corpus transaction으로 slug를 예약하고 완성된 산출물만 등록한다. 같은 코퍼스의 예약/등록/취소, index lock과 작업 lease를 우회하는 JSON 직접 덮어쓰기는 하지 않는다.
- 리뷰 실패 후 보존된 partial/cache를 확인한다. HTML·서지 실패를 이유로 유료 리뷰를 무조건 재요청하지 않는다.
- `sidecar-only`는 전역 서지 DB 반영 완료가 아니다. 명시적 `bibliography-update` 이후 `check_bibliography_db.py --strict`로 review/text 해시를 대조한다.
- 원본 Zotero SQLite를 플러그인 밖에서 직접 수정하지 않는다. 로컬 PDF 경로와 원래 creator JSON/저널/항목 키를 보존한다.
- 공개 HTML에 운영자 키를 넣지 않는다. 공개 XLSX는 ZIP metadata·관계·수식·개인 경로/연락처도 검사한다. 출처별 재배포 조건은 별도로 확인한다.

## Explicit full workflows

사용자가 전체 큐레이션을 요청한 경우에만 `run_full.py`를 사용한다. 기존 단계의 자동 실행을 단일 모듈 요청에 적용하지 않는다.

```bash
python pipeline/run_full.py --topic my_topic --mode curate --source zotero --dry-run
python pipeline/run_full.py --topic my_topic --mode curate --source web --days 7 --dry-run
```

계획을 확인한 뒤 실행한다. `rebuild`는 명시적으로 요청된 범위만 대상으로 하며, 사용자 요청 없이 `--yes`·삭제·재분류·push·배포를 추가하지 않는다. `publish`는 실제 업로드 및 저장소 변경을 수반하므로 전송 대상·공개 권한을 확인한다. 저수준 스크립트는 디버깅용이며 공통 writer 경계를 우회해 병렬 실행하지 않는다.

## Completion evidence

- 선택한 기능·대상·실제로 사용한 제공자/모델과 산출물을 보고한다.
- 계획만 확인했는지, mock 테스트인지, 실제 API/GUI 검증인지 구분한다.
- 검증하지 않은 제공자의 품질·권한·요금을 보장하지 않는다.
- 요청하지 않은 배포/메일/전체 코퍼스 갱신을 완료 조건으로 덧붙이지 않는다.
