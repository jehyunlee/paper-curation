# BibFusion: A Python package to integrate, deduplicate, and harmonize exported bibliographic records from Scopus and Web of Science for bibliometric analysis

> **저자**: Angelo Britto, Sebastian Robledo, Martha Zuluaga | **날짜**: 2026-02-14 | **Journal**: Iberoamerican Journal of Science Measurement and Communication | **DOI**: 10.47909/ijsmc.342

---

## Essence
Scopus와 Web of Science에서 내보낸 서지 데이터를 어떻게 하나의 신뢰할 수 있는 분석용 코퍼스로 통합할 수 있는가? BibFusion은 DOI 우선 중복 제거, ASCII/대문자 정규화, OpenAlex 기반 식별자 보강, ORCID/OpenAlexAuthorID를 활용한 저자 동명이인 해소를 수행하는 Python 패키지다. 기업 마케팅 쿼리 시연에서 436개 원천 레코드를 253개 고유 주요 저작물로 통합하고, 8,569편의 통합 코퍼스를 생성했다.

## Motivation
계량서지학 분석의 타당성은 기초 서지 메타데이터의 일관성에 달려 있으나, Scopus와 WoS는 커버리지, 내보내기 구조, 메타데이터 완전성이 상이하다. DOI 누락, 저자명 변이, 소속 불일치, 비표준 참고문헌 등이 중복 팽창, 저자 모호성, 인용 링크 단절을 초래하여 생산성·협력·지리 지표에 편향을 유발한다. 기존 도구들(bibliometrix, VOSviewer 등)은 데이터 수집 후 분석에 강하나, 교차 데이터베이스 통합 전처리에는 추가 작업이 필요했다.

## Achievement
1. Scopus CSV와 WoS TXT 파일을 수용하는 **재현 가능한 통합 파이프라인** 구현
2. **DOI 우선, 제목-연도-제1저자 보조** 중복 제거 전략
3. OpenAlex DOI 기반 해석으로 **영구 식별자(OpenAlex work ID, ORCID)** 보강
4. **PersonID 계층**(ORCID → OpenAlexAuthorID → 정규화 이름)을 통한 저자 동명이인 해소
5. 인용 문자열 정리, 저널/Scimago 정보 통합, 감사 로그 생성

## How
- **입력**: Scopus CSV, WoS TXT 내보내기 파일
- **처리**: 정규화(ASCII, 대문자, 제목 표준화) → OpenAlex API로 DOI 기반 보강 → DOI 우선 중복 제거 → 저자 PersonID 할당 → 인용 링크 재매핑 → 저널/Scimago ISSN 통합
- **출력**: 연결된 테이블(엔터티 관계형), 감사 아티팩트(별칭, 충돌, 병합 로그)
- **시연**: 기업 마케팅 쿼리 데이터셋

## Originality
- Scopus-WoS 통합에 **OpenAlex 기반 식별자 보강**을 결합한 최초의 오픈소스 Python 도구
- 병합 결정과 잔여 불확실성을 **감사 아티팩트**로 명시적으로 문서화하여 투명성 확보
- 인용 네트워크 구축을 위한 **참고문헌 정리 및 재매핑** 기능 포함

## Limitation & Further Study
### 저자들이 언급한 한계
- DOI가 없는 레코드의 보수적 매칭으로 일부 실제 중복 잔존 가능
- OpenAlex 식별자의 불완전성
- 영어 저널 논문 중심 설계

### 리뷰어 판단 아쉬운 점
- 단일 시연(기업 마케팅)으로 다양한 분야에서의 성능 검증 부족
- 기존 도구(bibliometrix의 mergeDbSources, tosr 등)와의 체계적 비교 실험 없음
- 대규모 데이터셋에서의 처리 시간 및 확장성 정보 부재
- 중복 제거 정확도(precision/recall)에 대한 정량적 평가 없음

### 후속 연구
- 다양한 분야 및 규모의 데이터셋에서 벤치마크 평가
- 기존 도구와의 체계적 비교
- Dimensions, OpenAlex 등 추가 데이터 소스 지원

## Evaluation
| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 3/5 |
| Significance | 3/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: Scopus-WoS 통합이라는 실용적 문제에 대한 체계적 해결책을 제시하나, 성능 검증과 기존 도구 대비 우위 입증이 부족하여 도구의 가치 판단이 어렵다.
