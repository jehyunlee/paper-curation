---
title: "952_Design_and_Update_of_a_Classification_System_The_UCSD_Map_of"
authors:
  - "Katy Börner"
  - "Richard Klavans"
  - "Michael Patek"
  - "Angela M. Zoss"
  - "Joseph R. Biberstine"
date: "2012"
doi: "10.1371/journal.pone.0039464"
arxiv: ""
score: 4.0
essence: "UCSD Map of Science의 설계 및 업데이트를 통해 과학 분류 체계(classification system)를 구축하고, 원본 5년 데이터에서 10년 데이터로 확장하여 저널 매핑 정확도와 사용성을 향상시켰다."
tags:
  - "cat/Science_of_Science_Research"
  - "sub/Bibliometrics_and_Science_Mapping"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Börner et al._2012_Design and Update of a Classification System The UCSD Map of Science.pdf"
---

# Design and Update of a Classification System: The UCSD Map of Science

> **저자**: Katy Börner, Richard Klavans, Michael Patek, Angela M. Zoss, Joseph R. Biberstine, Robert P. Light, Vincent Larivière, Kevin W. Boyack | **날짜**: 2012 | **DOI**: [10.1371/journal.pone.0039464](https://doi.org/10.1371/journal.pone.0039464)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1. Visualizations of the UCSD Map: 2D Mercator projection (left) with three 3D spherical insets (top), 1D circula*

UCSD Map of Science의 설계 및 업데이트를 통해 과학 분류 체계(classification system)를 구축하고, 원본 5년 데이터에서 10년 데이터로 확장하여 저널 매핑 정확도와 사용성을 향상시켰다.

## Motivation

- **Known**: 과학 지도(science map)는 학술 데이터의 대규모 분석을 통해 추상적 의미공간(semantic space)을 시각화하여 연구 영역, 전문가, 기관 등을 파악하는 데 활용된다. 기존 200개 이상의 과학 지도가 존재하나 대부분 일회성이며 업데이트된 사례가 드물다.
- **Gap**: 널리 사용되는 과학 지도의 체계적인 업데이트 방법론이 부재하고, 저널 분류의 정확도, 다중 분류 문제, 학제간 연구 반영 등의 개선점이 남아있다.
- **Why**: 과학 지도는 학생, 연구자, 기금 기관, 산업체 등 다양한 이해관계자에게 지식 탐색, 연구 동향 파악, 투자 의사결정 지원 등의 가치를 제공하므로 높은 품질의 분류 체계가 중요하다.
- **Approach**: Scopus와 Web of Science(WoS) 데이터를 통합하여 2001-2010년 약 25,000개 저널을 포함한 업데이트된 분류 체계를 구축하고, 원본과 비교 분석하여 개선 효과를 평가했다.

## Achievement

![Figure 4](figures/fig4.webp)

*Figure 4. Number of journals per discipline for 5-year (grey) and 10-year (black) UCSD science map.*

- **저널 커버리지 확대**: 약 9,409개 저널 추가 매핑 (사회과학 80%, 인문학 119%, 의학 32%, 자연과학 74% 증가)
- **분류 단순화**: 고도로 학제적인 5개 저널을 제외한 모든 저널을 단일 분야에 할당하여 다중 분류 문제 해결
- **균형 잡힌 분포**: 554개 세부 분야(subdiscipline)와 13개 주요 분야(discipline)에 저널이 보다 균등하게 배분
- **인용 데이터 기반 검증**: 논문 수준의 인용 데이터와 비교 시 저널 클러스터 반영도 향상
- **지도 품질 개선**: 매핑 정확도 증가, 이해도 향상, 데이터 오버레이(overlay) 생성 가능성 향상

## How

![Figure 1](figures/fig1.webp)

*Figure 1. Visualizations of the UCSD Map: 2D Mercator projection (left) with three 3D spherical insets (top), 1D circula*

- Elsevier Scopus(약 15,000개 저널, 2001-2005)와 Thomson Reuters WoS(약 9,000개 저널, 2001-2004) 데이터 통합
- 7.2백만 개 논문과 그 인용 관계를 기반으로 저널 간 공인용(co-citation) 네트워크 분석
- 다차원 척도법(multidimensional scaling, MDS)과 클러스터링 알고리즘을 적용하여 고차원 공간을 2차원 지도로 축약
- 원본 분류 구조 유지하면서 신규 저널 할당 및 기존 분류 검증
- Mercator 투영, 3D 구면 표현, 1D 원형 지도 등 다양한 시각화 형식 제공
- SciVal Spotlight, Sci2 데스크톱 도구 등을 통한 데이터 오버레이 기능 구현

## Originality

- **최초의 광범위 과학 지도 업데이트**: 널리 사용되는 과학 지도를 체계적으로 업데이트한 첫 사례
- **이중 데이터 소스 통합**: Scopus와 WoS를 결합하여 더 포괄적인 저널 커버리지 달성
- **명확한 평가 기준 제시**: 과학 지도의 8가지 바람직한 특성을 정의하고 평가 프레임워크 제공
- **학제적 경계 처리**: 고도의 학제적 저널을 의도적으로 최소화하면서도 학제 간 연결성 유지
- **다층적 분류 체계**: 13개 주요 분야와 554개 세부 분야의 계층적 분류 구조 설계

## Limitation & Further Study

- **시간적 제약**: 2010년까지의 데이터만 포함하여 현재의 과학 동향 반영 미흡 (후속 업데이트 필요)
- **저널-논문 간극**: 저널 수준 분류가 개별 논문의 학제적 성격을 완전히 반영하지 못할 가능성
- **데이터베이스 편향**: Scopus와 WoS의 학문 분야 커버리지 차이로 인한 편향 가능성
- **상업적 저널 중심**: 주류 상용 학술지 위주로 구성되어 오픈 액세스 저널, 국가별 특화 저널 등 상대적으로 소외
- **분류 안정성 검증 부족**: 시간 경과에 따른 분류 구조의 안정성 및 재현성에 대한 장기 평가 필요
- **후속연구**: 정기적인 업데이트 주기 확립, 기계학습 기반 자동 분류 개선, 다언어 학술지 통합 등이 요구됨

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 연구는 광범위하게 활용되는 과학 지도를 최초로 체계적으로 업데이트하여 저널 매핑의 정확도와 학문 분야 커버리지를 크게 향상시켰으며, 다양한 이해관계자의 지식 탐색과 의사결정을 지원하는 중요한 기초 자원을 제공한다.

## Related Papers

- 🔗 후속 연구: [[papers/982_Mapping_Knowledge_Topic_Analysis_of_Science_Locates_Research/review]] — 과학 주제 분석을 통한 연구 분야 위치 파악 방법론을 UCSD 맵의 분류 체계와 결합하여 더 정교한 과학 지도 구축을 가능하게 한다.
- 🧪 응용 사례: [[papers/986_Mapping_the_changing_structure_of_science_through_diachronic/review]] — 통시적 복합 네트워크를 통한 과학 구조 변화 매핑에 UCSD 맵의 업데이트된 분류 체계가 시간적 변화 추적의 기준점을 제공한다.
- 🔄 다른 접근: [[papers/969_Hierarchical_Classification_of_Research_Fields_in_the_Web_of/review]] — UCSD 맵과 딥러닝 기반 분류는 모두 과학 분야를 체계적으로 분류하되 서로 다른 방법론을 사용한다.
- 🧪 응용 사례: [[papers/1120_SciEvo_A_2_Million_30-Year_Cross-disciplinary_Dataset_for_Te/review]] — 30년간의 학문 진화 데이터를 연구 분야 분류 시스템의 설계와 업데이트에 활용한다.
- 🔗 후속 연구: [[papers/930_A_Survey_on_Knowledge_Organization_Systems_of_Research_Field/review]] — UCSD Map of Science의 분류 체계 설계 경험을 바탕으로 다양한 지식 조직 체계들의 통합 솔루션 개발에 필요한 구조적 이해를 제공한다.
