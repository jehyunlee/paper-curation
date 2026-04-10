---
title: "930_A_Survey_on_Knowledge_Organization_Systems_of_Research_Field"
authors:
  - "Angelo Salatino"
  - "Tanay Aggarwal"
  - "Andrea Mannocci"
  - "Francesco Osborne"
  - "Enrico Motta"
date: "2025.06"
doi: "10.1162/qss_a_00363"
arxiv: ""
score: 4.0
essence: "본 논문은 학술 분야의 지식 조직 체계(Knowledge Organization Systems, KOS) 45개를 scope, structure, curation, usage, links 등 5가지 차원으로 분석하여 현황을 파악하고 통합 솔루션의 필요성을 제시한다."
tags:
  - "cat/Science_of_Science_Research"
  - "sub/Bibliometrics_and_Science_Mapping"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Salatino et al._2025_A Survey on Knowledge Organization Systems of Research Fields Resources and Challenges.pdf"
---

# A Survey on Knowledge Organization Systems of Research Fields: Resources and Challenges

> **저자**: Angelo Salatino, Tanay Aggarwal, Andrea Mannocci, Francesco Osborne, Enrico Motta | **날짜**: 2025-06-20 | **DOI**: [10.1162/qss_a_00363](https://doi.org/10.1162/qss_a_00363)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2. The aspects and features used for the analysis of Knowledge Organization Systems.*

본 논문은 학술 분야의 지식 조직 체계(Knowledge Organization Systems, KOS) 45개를 scope, structure, curation, usage, links 등 5가지 차원으로 분석하여 현황을 파악하고 통합 솔루션의 필요성을 제시한다.

## Motivation

- **Known**: KOS는 학술 정보의 분류, 관리, 검색에 필수적이며 디지털 도서관과 연구 커뮤니티에서 광범위하게 활용되고 있다. 다양한 학술 분야가 자체 KOS를 개발했지만 상당한 이질성이 존재한다.
- **Gap**: 현재까지 학술 분야의 KOS에 대한 체계적이고 심층적인 분석이 부족하며, 각 KOS의 특성과 상호 연계성에 대한 종합적 이해가 필요하다.
- **Why**: 학술 논문의 급증, 오픈사이언스 확산, 학제간 연구 증대에 따라 강력한 KOS 기반 AI 시스템이 문헌 검색, 연구 영향력 평가, 연구 동향 예측에 필수적이 되었다.
- **Approach**: 45개의 KOS를 체계적인 포함/제외 기준으로 선별하고, scope, structure, curation, usage, links 5가지 측면과 15개 세부 특성에 따라 비교 분석하였다.

## Achievement

![Figure 3](figures/fig3.webp)

*Figure 3. Depth distribution for single-field and multi-field KOSs.*

- **45개 KOS의 포괄적 목록화**: 전 학술 분야를 아우르는 현존 KOS의 전체 현황을 체계적으로 문서화
- **이질성 규명**: scope, scale, quality, usage 측면에서 KOS들의 상당한 편차 확인 (예: 의학 분야는 다수의 KOS 보유, 지리학/역사학 등은 전무)
- **구조적 분석**: 개념 수, 계층 깊이, 동의어, 언어 지원 등 KOS의 구조적 특성을 정량화
- **관리 체계 평가**: 업데이트 빈도, 라이선스, 생성 절차 등 KOS의 큐레이션 품질 분석
- **상호연계 현황 파악**: KOS 간 링크와 호환성을 분석하여 통합 가능성 모색
- **오픈사이언스 실천**: 분석 결과와 처리 코드를 공개 데이터와 GitHub로 공개

## How


- 체계적 문헌 검토를 통한 45개 KOS 후보 선별
- 각 KOS에 대해 15개 특성(scope, structure, curation, usage, links)에 따른 데이터 수집 및 표준화
- 학술 분야별 KOS 분포, 구조, 업데이트 패턴 등을 정량적으로 분석
- 다양한 KOS의 특성을 비교표로 시각화하여 패턴 도출
- Open Research Knowledge Graph와 GitHub를 통한 결과 공개 및 재현성 확보

## Originality

- 학술 분야 KOS에 대한 **최초의 대규모 체계적 조사** - 기존에는 개별 KOS나 특정 분야에 대한 연구만 존재
- **5차원 분석 프레임워크** (scope, structure, curation, usage, links) 개발로 이질적인 KOS들을 일관된 기준으로 평가
- **45개 KOS의 메타데이터 통합 데이터베이스** 구축으로 비교 분석 가능하도록 함
- LLM 시대에도 **구조화된 지식 표현의 가치** 재조명 - 환각 제거, 해석가능성 향상 측면 강조
- KOS 간 **상호연계 및 통합 가능성** 분석으로 미래 방향성 제시

## Limitation & Further Study

- 45개 KOS 선정의 객관적 기준이 명확하지 않으면 완전성에 대한 의문 가능 - 후속 연구에서 다른 KOS 추가 발굴 필요
- 각 KOS의 실제 **사용 현황(usage)** 데이터 수집의 어려움 - 공개된 통계가 부족할 수 있음
- KOS 업데이트 빈도 등 **시간 변동 데이터**의 스냅샷 특성 - 지속적인 모니터링 체계 필요
- 특정 학술 분야(예: 인문학)의 **언어별 KOS 다양성**을 완전히 포착하지 못했을 가능성
- KOS 간 **상호연계의 기술적 실현 방안**에 대한 구체적 제안 부족 - 구현 로드맵 개발 필요
- 분석 대상을 **영어권 및 주요 학술 분야**에 편향되었을 가능성 - 비영어권 학술 생태계 포함 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 학술 분야 KOS에 대한 최초의 체계적 대규모 조사로서, 현재 학술 정보 조직의 이질성을 명확히 규명하고 통합 솔루션의 필요성을 강하게 제시한다. 오픈사이언스 원칙에 따라 데이터와 코드를 공개하여 추후 연구의 기초가 될 수 있는 중요한 기여이나, KOS 선정 기준 명확화와 사용 현황 데이터 수집 강화가 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/952_Design_and_Update_of_a_Classification_System_The_UCSD_Map_of/review]] — UCSD Map of Science의 분류 체계 설계 경험을 바탕으로 다양한 지식 조직 체계들의 통합 솔루션 개발에 필요한 구조적 이해를 제공한다.
- 🧪 응용 사례: [[papers/1054_Whats_In_Your_Field_Mapping_Scientific_Research_with_Knowled/review]] — 과학 연구 분야 매핑에 사용되는 지식 체계들의 현황 분석이 실제 연구 분야 매핑 도구 개발에 직접 활용될 수 있다.
- 🔗 후속 연구: [[papers/986_Mapping_the_changing_structure_of_science_through_diachronic/review]] — 연구 분야 지식 조직 시스템에 대한 체계적 조사가 과학 구조 진화 추적의 분류학적 기반이 된다.
- 🏛 기반 연구: [[papers/1112_CS-KG_20_A_Large-scale_Knowledge_Graph_of_Computer_Science/review]] — 연구 분야의 지식 조직 시스템에 대한 이론적 기반을 제공하여 컴퓨터과학 지식그래프 구축의 개념적 토대가 된다.
