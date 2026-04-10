---
title: "1056_Where_Do_Your_Citations_Come_From_Citation-Constellation_A_F"
authors:
  - "Mahbub Ul Alam"
date: "2026.03"
doi: ""
arxiv: ""
score: 4.0
essence: "Citation-Constellation은 인용 네트워크의 사회구조적 경로를 분석하여 연구자의 인용 프로필을 분해하는 무료 오픈소스 도구로, BARON과 HEROCON 두 가지 상보적 지표를 제시한다."
tags:
  - "cat/Bibliometric_Network_Analysis"
  - "sub/Citation_Metrics_and_Indices"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Alam_2026_Where Do Your Citations Come From Citation-Constellation A Free, Open-Source, No-Code, and Auditab.pdf"
---

# Where Do Your Citations Come From? Citation-Constellation: A Free, Open-Source, No-Code, and Auditable Tool for Citation Network Decomposition with Complementary BARON and HEROCON Scores

> **저자**: Mahbub Ul Alam | **날짜**: 2026-03-25 | **URL**: [https://arxiv.org/abs/2603.24216v1](https://arxiv.org/abs/2603.24216v1)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2: Score panel in both interfaces.*

Citation-Constellation은 인용 네트워크의 사회구조적 경로를 분석하여 연구자의 인용 프로필을 분해하는 무료 오픈소스 도구로, BARON과 HEROCON 두 가지 상보적 지표를 제시한다.

## Motivation

- **Known**: 인용 지표들이 모든 인용을 동등하게 취급하며, 인용 패턴이 사회적 네트워크 구조를 따른다는 것이 알려져 있다. 하지만 이를 실제로 구현하고 감사 가능한 도구로 변환하는 것은 저자 식별 오류, 메타데이터 품질, 다층 네트워크 감지의 복잡성으로 인해 어려웠다.
- **Gap**: 표준 인용 지표는 외부 독립 연구자의 인용과 공동저자/동료/편집위원의 인용을 구별하지 못하며, 이러한 구조적 차이를 측정하는 감사 가능하고 접근 가능한 도구가 부재했다.
- **Why**: 인용의 사회구조적 출처를 이해하는 것은 책임감 있는 연구 평가와 학자적 영향력의 진정한 범위를 파악하는 데 중요하며, 특히 글로벌 남반부 연구자들의 고비용 데이터베이스 접근 불평등을 해소할 수 있다.
- **Approach**: 자기인용 분석, 공동저자 그래프 순회, 시간기반 기관 소속 매칭(ROR), AI 에이전트 기반 학술장소 거버넌스 추출의 4단계 아키텍처를 통해 인용 네트워크를 계층적으로 분해한다.

## Achievement

![Figure 3](figures/fig3.webp)

*Figure 3: Classification breakdown donut chart.*

- **BARON과 HEROCON 이중 점수 체계**: 경계기반 연구 확산 네트워크(BARON) 점수는 협력 네트워크 외부 인용만 계산하는 엄격한 이진 지표이고, 전체 균형 연구 확산 별자리(HEROCON) 점수는 관계 근접성에 따라 집단 내 인용에 부분 가중치를 할당한다.
- **접근성과 민주화**: 설치, 프로그래밍 지식, 기관 구독, 등록, 결제가 필요 없는 웹 인터페이스 제공으로 표준 인용 분석 도구의 접근 불평등을 해소한다.
- **ORCID 기반 저자 정체성 해결**: 저자 식별 오류를 최소화하고 인용 분석의 신뢰성을 높인다.
- **포괄적 감사 추적**: 모든 분류 결정을 구조화된 JSON으로 문서화하여 완전한 재현성과 이의 제기 가능성을 보장한다.
- **UNKNOWN 분류**: 불충분한 메타데이터를 가진 인용을 호직으로 보고하여 메타데이터 불충분 연구자에 대한 체계적 편향을 방지한다.

## How

![Figure 4](figures/fig4.webp)

*Figure 4: Co-author network graph (overview).*

- OpenAlex, ORCID, ROR 등 개방형 데이터 소스 활용
- 4단계 네트워크 감지 아키텍처 (각 단계가 독립적으로 의미 있는 점수 생성)
- 지역 배포 대형언어모델(LLM) 활용 AI 에이전트 기반 편집위원회/프로그램위원회 구성원 자동 추출
- 공동저자 네트워크 그래프 시각화 및 대화형 인터페이스
- 비교 기능을 통한 다중 연구자 프로필 병렬 분석
- 명령줄 도구와 웹 인터페이스 이중 배포

## Originality

- 공동저자, 기관 소속, 학술장소 거버넌스를 통합한 다층 네트워크 분석 프레임워크의 실무 구현
- 편집위원회/프로그램위원회 추출을 위한 LLM 기반 자동화 시스템의 신규 적용
- 구조적 진단 지표로서 BARON/HEROCON의 상보적 설계와 '점수 간격'을 내부원형 의존성 진단으로 활용", '완전한 감사 추적과 UNKNOWN 분류를 통한 투명성과 데이터 품질 정직성 강조
- 글로벌 남반부 연구자 포함 진정한 민주적 접근성 달성

## Limitation & Further Study

- HEROCON의 관계 근접성 가중치는 실험적이며 경험적 교정이 필요함
- 4단계(학술장소 거버넌스)는 아직 개발 중으로 완전히 작동하지 않음
- 메타데이터 부족으로 인한 UNKNOWN 분류의 비율이 높을 수 있으며, 이것이 점수 해석에 미치는 영향 미분석
- 인용 동기(citation motivation) 연구와의 교차 검증 필요
- 도구가 구조적 진단으로만 명시되었으나, 실제 채용/승진/펀딩 의사결정에 오용될 위험 존재
- 시간 기반 기관 소속 매칭의 정확성이 ROR 데이터 품질에 의존

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 논문은 이론적으로 확립된 인용 네트워크 분석 통찰을 실제 감사 가능하고 접근 가능한 도구로 변환한 중요한 기여이며, 특히 개방성과 투명성에 대한 강조와 글로벌 접근성 제고를 통해 책임감 있는 연구 평가 운동에 부합한다.

## Related Papers

- 🧪 응용 사례: [[papers/946_Collective_Credit_Allocation_in_Science/review]] — 인용 네트워크의 사회구조적 경로 분석을 다중저자 논문의 집단적 신용 배분 문제에 적용한다.
- 🔗 후속 연구: [[papers/1052_Updated_science-wide_author_databases_of_standardized_citati/review]] — 표준화된 저자 데이터베이스를 인용 네트워크의 사회구조적 분석으로 확장한다.
- 🧪 응용 사례: [[papers/974_Information_Pathways_in_Online_Science_Communication_The_Rol/review]] — 인용 네트워크의 경로 분석을 온라인 과학 커뮤니케이션의 정보 전달 경로 연구에 적용한다.
- 🔗 후속 연구: [[papers/1020_Scientific_prize_network_predicts_who_pushes_the_boundaries/review]] — 인용 네트워크 분석을 과학상 네트워크가 과학 경계 확장 예측에 미치는 영향으로 확장한다.
- 🔗 후속 연구: [[papers/1047_Theory_and_Practice_of_the_g-index/review]] — 단순 인용 집계를 넘어 인용 네트워크의 사회구조적 경로를 분석하여 더 정교한 영향력 측정을 제안한다.
