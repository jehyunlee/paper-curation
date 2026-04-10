---
title: "939_BibFusion_A_Python_package_to_integrate_deduplicate_and_harm"
authors:
  - "Angelo Britto"
  - "Sebastian Robledo"
  - "Martha Zuluaga"
date: "2026.02"
doi: "10.47909/ijsmc.342"
arxiv: ""
score: 4.0
essence: "BibFusion은 Scopus와 Web of Science의 서지 데이터를 통합, 중복 제거 및 조화(harmonize)하여 서지계량 분석에 활용할 수 있는 Python 패키지이다. DOI 기반 식별자와 메타데이터 정규화를 통해 분석 준비된 통합 말뭉치를 제공한다."
tags:
  - "cat/Science_of_Science_Research"
  - "sub/Bibliometrics_and_Science_Mapping"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Britto et al._2026_BibFusion A Python package to integrate, deduplicate, and harmonize exported bibliographic records.pdf"
---

# BibFusion: A Python package to integrate, deduplicate, and harmonize exported bibliographic records from Scopus and Web of Science for bibliometric analysis

> **저자**: Angelo Britto, Sebastian Robledo, Martha Zuluaga | **날짜**: 2026-02-14 | **DOI**: [10.47909/ijsmc.342](https://doi.org/10.47909/ijsmc.342)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2 presents the unified ER model of the*

BibFusion은 Scopus와 Web of Science의 서지 데이터를 통합, 중복 제거 및 조화(harmonize)하여 서지계량 분석에 활용할 수 있는 Python 패키지이다. DOI 기반 식별자와 메타데이터 정규화를 통해 분석 준비된 통합 말뭉치를 제공한다.

## Motivation

- **Known**: Scopus와 Web of Science는 서지계량 연구의 주요 데이터 소스이지만, 두 플랫폼은 범위, 수출 형식, 메타데이터 완정성이 상이하여 통합 시 중복, 저자명 불일치, 불완전한 소속 정보 등의 문제가 발생한다. 기존 도구(bibliometrix, VOSviewer 등)는 데이터 시각화는 우수하나 크로스 데이터베이스 통합을 위한 전처리 기능이 부족하다.
- **Gap**: 기존 통합 워크플로우들은 자동화된 병합에 중점을 두지만, (i) 관계형 엔티티-관계(ER) 모델의 명시적 표현과 (ii) 병합 및 저자 구분 결정을 문서화한 감사 가능한(auditable) 아티팩트 제공이 부족하다.
- **Why**: 재현 가능하고 투명한 서지 통합 전처리는 생산성, 협력 네트워크, 지리적 분포 등 하위 지표의 편향을 제거하고 신뢰할 수 있는 과학계량 분석을 보장한다.
- **Approach**: BibFusion은 DOI 우선 중복 제거 전략(부재 시 제목-연도-첫 저자 대체)과 OpenAlex 기반 DOI 해석을 통한 선택적 메타데이터 풍부화를 적용한다. 정규 PersonID 계층(ORCID → OpenAlexAuthorID → 정규화 이름)을 통해 저자를 구분하고, 병합 결정과 감사 추적을 기록한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2 presents the unified ER model of the*

- **통합 및 정규화**: Scopus CSV와 WoS TXT 파일을 수입하여 제목/키의 ASCII/대문자 표준화, 소속 정보 파싱 및 국가 추출 등 체계적 정규화 수행
- **메타데이터 풍부화**: DOI 기반 OpenAlex 해석으로 OpenAlex 저작 ID, ORCID, OpenAlex 저자 ID 등 지속적 식별자 회수
- **중복 제거 및 통합**: DOI 우선 중복 제거 캐스케이드 + 보수적 대체 규칙으로 436개 원본 레코드를 253개 고유 저작으로 통합
- **저자 구분 및 인용 정리**: 정규 PersonID 계층으로 저자 모호성 제거, 인용 문자열 정리 및 ISSN/EISSN 규칙으로 저널 정보 통합
- **분석 준비 말뭉치**: 8,569개 논문의 높은 식별자 및 지리적 완정성을 갖춘 통합 말뭉치와 일관된 인용 네트워크 제공

## How

![Figure 1](figures/fig1.webp)

*Figure 1 provides a synopsis of the end-to-end*

- 메타데이터 정규화(ASCII 표준화, 대소문자 통일)
- OpenAlex API를 통한 DOI 기반 식별자 해석
- DOI 우선, 제목-연도-첫 저자 대체 규칙에 따른 다단계 중복 제거
- ORCID/OpenAlexAuthorID/정규화 이름 기반 저자 정규 식별자(PersonID) 생성
- 인용 문자열 정리 및 일관된 인용 링크 유지
- ISSN/EISSN 규칙에 따른 저널 및 Scimago 정보 통합
- 병합 결정 및 불확실성을 문서화한 감사 아티팩트(alias, 충돌, 병합 로그) 생성

## Originality

- 관계형 ER 모델의 명시적 표현으로 핵심 엔티티와 링킹 테이블 구분
- DOI 기반 OpenAlex 해석과 보수적 대체 규칙을 결합한 혁신적 중복 제거 전략
- 정규 PersonID 계층(ORCID → OpenAlexAuthorID → 정규화 이름)을 통한 체계적 저자 구분
- 병합 결정 및 잔존 불확실성을 명시적으로 문서화하는 감사 가능한(auditable) 워크플로우
- 재현 가능성과 투명성에 중점을 두어 기존 자동화 지향 도구와 차별화

## Limitation & Further Study

- DOI 부재나 오류가 있는 경우 중복 제거 정확도 저하 가능성 (제목-연도-저자명 규칙에 의존)
- ORCID 및 OpenAlexAuthorID 등 외부 식별자의 불완전성으로 인해 저자 구분 한계
- 인용 참고문헌은 쿼리 시간 범위를 초과할 수 있어 인용 네트워크 생성 시 문서 타입 불일치 가능
- 영어 저널 논문 중심으로 설계되어 다국어 또는 비논문 문헌에 대한 적용성 제한
- **후속 연구**: 기계학습 기반 문자열 유사도 알고리즘 도입, OpenAlex 외 추가 메타데이터 소스 통합, 사용자 정의 중복 제거 규칙 설정 옵션 추가

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: BibFusion은 Scopus-WoS 통합의 구조적 문제(중복, 저자 불일치, 소속 불완정)를 해결하는 재현 가능하고 감사 가능한 Python 패키지로, 관계형 데이터 모델과 명시적 아티팩트를 통해 기존 도구의 한계를 넘어선다. 실제 entrepreneurial marketing 사례(436→253 고유 저작, 8,569 논문)로 효과성을 입증했으며, 과학계량 연구의 데이터 전처리 표준화에 기여할 잠재력이 높다.

## Related Papers

- 🔄 다른 접근: [[papers/1024_Software_survey_VOSviewer_a_computer_program_for_bibliometri/review]] — VOSviewer의 서지계량 분석 도구와 다른 접근으로 데이터 전처리 단계에서 Scopus와 Web of Science 통합을 위한 Python 기반 솔루션을 제공한다.
- 🔗 후속 연구: [[papers/992_OpenAlex_in_focus_Metadata_quality_of_publication_type_and_l/review]] — OpenAlex의 메타데이터 품질 분석과 연결되어 다양한 서지 데이터베이스 통합 시 고려해야 할 데이터 품질 이슈를 다룬다.
- 🧪 응용 사례: [[papers/1071_Data_measurement_and_empirical_methods_in_the_science_of_sci/review]] — 서지정보 통합과 중복 제거를 위한 실용적 도구를 통해 대규모 데이터셋 구축의 구체적 방법론을 제시한다.
