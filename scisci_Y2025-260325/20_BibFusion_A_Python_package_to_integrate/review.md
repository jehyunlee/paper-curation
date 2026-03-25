# BibFusion: A Python package to integrate, deduplicate, and harmonize exported bibliographic records from Scopus and Web of Science for bibliometric analysis

> **저자**: Angelo Britto, Sebastian Robledo, Martha Zuluaga | **날짜**: 2026-02-14 | **DOI**: 10.47909/ijsmc.342

---

## 핵심 요약
본 연구는 Scopus와 Web of Science의 서지 레코드를 통합, 중복 제거, 정규화하여 분석 가능한 단일 코퍼스로 변환하는 Python 패키지 BibFusion을 제시한다. DOI 기반 중복 제거, OpenAlex를 통한 식별자 보강, ORCID/OpenAlexAuthorID 기반 저자 명확화, 인용 문자열 정제 등의 기능을 갖추며, 기업가적 마케팅 쿼리 시연에서 436건의 소스 레코드를 253개의 고유 저작물로 통합하였다.

## 연구 배경 및 동기
Bibliometric 분석의 타당성은 기저 서지 메타데이터의 일관성에 달려 있으나, Scopus와 WoS는 커버리지, 내보내기 구조, 필드 완전성에서 차이가 있어 통합이 어렵다. DOI 누락, 저자명 변이, 소속 불일치, 인용 문자열 비표준화 등으로 중복이 팽창하고 인용 링크가 단절되어 생산성, 협업, 과학 지리 지표에 편향을 초래한다. 기존 도구(bibliometrix, VOSviewer 등)는 데이터 시각화에는 강하지만 크로스 데이터베이스 통합 전처리는 추가 작업이 필요하다.

## 방법론
- **입력**: Scopus CSV 파일과 WoS TXT 파일
- **정규화**: ASCII/대문자 표준화, 소속 파싱 및 국가 추출
- **보강**: DOI 기반 OpenAlex 조회로 영구 식별자(OpenAlex work ID, ORCID, OpenAlex author ID) 회복
- **중복 제거**: DOI 우선 cascade + 보수적 fallback(제목-연도-제1저자)
- **저자 명확화**: 정식 PersonID 계층(ORCID → OpenAlexAuthorID → 정규화된 이름)
- **인용 정제**: 인용 문자열 정제 및 일관된 인용 링크 보존
- **저널 정보**: ISSN/EISSN 규칙을 활용한 Scimago 정보 통합
- **감사**: 출처, 병합 결정, 잔여 불확실성에 대한 감사 산출물 생성

## 주요 결과
- 기업가적 마케팅 쿼리 시연에서 436건 소스 레코드를 253개 고유 저작물로 통합
- 통합 코퍼스에서 8,569편의 분석 가능한 인용 레이어 구축
- 높은 식별자 및 지리적 완전성 달성
- 중복 팽창과 메타데이터 단편화를 효과적으로 감소
- 감사 산출물(별칭, 잠재적 충돌, 병합 로그)을 통한 투명성 확보

## 독창성 및 기여
Scopus-WoS 통합을 위한 재사용 가능하고 감사 가능한 Python 파이프라인을 제공한 점이 핵심 기여이다. DOI 기반 OpenAlex 보강, 정식 PersonID 계층을 통한 저자 명확화, 인용 문자열 정제와 재매핑을 통합적으로 수행하며, 모든 병합 결정에 대한 감사 추적성을 갖춘 점이 기존 도구 대비 차별화 요소이다.

## 한계 및 향후 연구
- DOI가 없는 레코드에 대한 fallback 규칙(제목-연도-제1저자)이 보수적이어서 일부 중복 미제거 가능
- OpenAlex 자체의 메타데이터 불완전성이 보강 품질에 영향
- ORCID 보급률이 분야별로 상이하여 저자 명확화 품질 편차
- 소규모 시연(436건)으로 대규모 데이터셋에서의 성능 미검증
- 영어 저널 논문에 초점을 맞추어 비영어 문헌 처리 미확인
- 향후 추가 데이터 소스(Dimensions, OpenAlex 직접 등) 지원 및 대규모 벤치마킹 필요

## 평가
| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 4/5 |
| Significance | 3/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: Bibliometric 연구의 데이터 전처리 파이프라인이라는 실질적 문제를 체계적으로 해결하는 유용한 도구 논문으로, 재현 가능성과 감사 추적성에 대한 강조가 높이 평가된다.
