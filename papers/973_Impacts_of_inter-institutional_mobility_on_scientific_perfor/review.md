---
title: "973_Impacts_of_inter-institutional_mobility_on_scientific_perfor"
authors:
  - "Yitong Chen"
  - "Keye Wu"
  - "Yue Li"
  - "Jianjun Sun"
date: "2023.06"
doi: "10.1007/s11192-023-04690-w"
arxiv: ""
score: 4.0
essence: "인공지능 분야에서 연구자의 학술기관-산업체 이동(aca.ind mobility)이 연구 성과에 미치는 영향을 연구 자본과 사회 자본 관점에서 분석한 논문으로, PSM 방법을 통해 인과관계를 규명한다."
tags:
  - "cat/Research_Quality_and_Demographics"
  - "sub/Career_Dynamics_and_Outcomes"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chen et al._2023_Impacts of inter-institutional mobility on scientific performance from research capital and social c.pdf"
---

# Impacts of inter-institutional mobility on scientific performance from research capital and social capital perspectives

> **저자**: Yitong Chen, Keye Wu, Yue Li, Jianjun Sun | **날짜**: 06/2023 | **DOI**: [10.1007/s11192-023-04690-w](https://doi.org/10.1007/s11192-023-04690-w)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1   Regression model framework*

인공지능 분야에서 연구자의 학술기관-산업체 이동(aca.ind mobility)이 연구 성과에 미치는 영향을 연구 자본과 사회 자본 관점에서 분석한 논문으로, PSM 방법을 통해 인과관계를 규명한다.

## Motivation

- **Known**: 연구자의 이동성은 과학 발전과 혁신을 촉진하며, 기존 연구는 주로 학술기관 간 이동(aca.aca mobility)에 초점을 맞추고 있다. 기업의 aca.ind 이동이 기업 혁신 성과에 미치는 영향에 대한 연구는 존재하지만, 개별 연구자 수준의 성과 분석은 부족한 상태이다.
- **Gap**: AI 분야에서 aca.ind mobility가 개별 연구자의 과학 성과(publications, collaborations)에 미치는 영향에 대한 정량적 분석이 부족하며, 특히 내생성 문제를 해결한 인과관계 규명이 필요하다.
- **Why**: AI가 국가 전략으로 부상하면서 학술-산업 간 연구자 이동이 증가하고 있으며, 이를 통해 기술 이전과 지식 확산이 일어나므로 개별 연구자의 성과 변화를 이해하는 것이 중요하다.
- **Approach**: PSM(propensity score matching) 방법으로 내생성 문제를 완화하면서, 비블리오메트릭 분석과 회귀분석을 통해 aca.ind mobility와 aca.aca mobility의 영향을 연구 자본(출판) 및 사회 자본(협력) 관점에서 비교 분석한다.

## Achievement

![Figure 3](figures/fig3.webp)

*Fig. 3   The distribution of flow*

- **aca.ind mobility의 선행조건 규명**: 이동 기회를 최대화하려면 단기간 내 많은 연구 출판, 기업 연구자와의 협력, 고임팩트 연구자와의 관계 구축이 필요함을 보였다.
- **사회 자본 축적에서 우위**: aca.ind mobility가 aca.aca mobility 대비 협력 네트워크 규모 확대와 고임팩트 연구자와의 협력 관계 형성에 더 유리함을 입증했다.
- **차별화된 성과 패턴**: aca.aca mobility는 더 많은 연구 자본 축적을 가능하게 하는 반면, aca.ind mobility는 사회 자본 축적을 촉진하는 각각의 특성을 규명했다.
- **정책적 시사점 제공**: 연구자 경력 개발 계획과 기관의 인재 채용, 구조 최적화, 혁신 시스템 평가를 위한 기초 자료를 제시했다.

## How

![Figure 2](figures/fig2.webp)

*Fig. 2   Steps of data preprocessing*

- **데이터 수집**: 과학 문헌(scholarly literature)을 기반으로 AI 분야 연구자의 이동 정보와 출판, 협력 데이터 추출
- **비블리오메트릭 분석**: 연구자 이동의 동기와 패턴을 파악하기 위해 출판 수, 협력자 수 등의 기술통계 분석
- **PSM(Propensity Score Matching)**: 선택 편향(selection bias)을 제거하여 이동성과 성과 간의 인과관계 규명
- **회귀분석**: 통제 변수를 포함한 선형 회귀 모델을 통해 두 가지 이동 유형(aca.aca vs aca.ind)의 성과 차이를 계량화
- **변수 설정**: 연구 자본(publications 수, 질), 사회 자본(coauthors 수, collaborator의 영향력) 등을 종속변수로 활용

## Originality

- **개별 수준의 성과 분석**: 기존 연구의 기관 수준 분석에서 벗어나 개별 연구자 수준의 과학 성과 변화를 종합적으로 분석했다.
- **내생성 문제 해결**: PSM 방법을 도입하여 연구자의 선천적 능력(initial talent)에 의한 편향을 제거하고 순수한 이동 효과를 분리했다.
- **다면적 성과 측정**: 연구 자본과 사회 자본 두 관점을 동시에 고려하여 이동이 미치는 차별화된 영향을 규명했다.
- **AI 분야 특화**: 학술-산업 간 이동이 활발한 AI 분야를 대상으로 최근의 현실적 현상을 분석했다.

## Limitation & Further Study

- **표본 크기 제약**: ind.aca 및 ind.ind 이동 사례가 너무 적어 이를 분석에서 제외했으므로, 양방향 이동(brain circulation)의 전체 효과를 포착하지 못했다.
- **학문 분야 특수성**: AI 분야만을 대상으로 하여 다른 첨단 산업(생명공학, 나노기술 등)에의 일반화 가능성이 제한된다.
- **성과 측정의 한계**: 과학 문헌만을 기반으로 성과를 측정하여 산업체의 특허, 제품화, 경제적 기여 등 비출판 성과를 포괄하지 못했다.
- **추적 기간**: 이동 후 성과 변화를 측정하는 시간 윈도우의 길이와 설정에 따라 결과가 민감할 수 있으므로 추가 시간 분석이 필요하다.
- **후속연구**: (1) 더 많은 산업 분야로 확대하여 aca.ind mobility의 효과를 비교 검증, (2) 종단 연구를 통해 장기적 성과 변화 추적, (3) 정성적 인터뷰를 통해 이동 동기와 성과 간의 메커니즘 규명

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 연구는 PSM 방법으로 내생성을 해결하면서 개별 연구자 수준에서 학술-산업 이동의 차별화된 영향을 체계적으로 분석한 의미 있는 논문으로, 정책 입안자와 연구자 모두에게 실질적인 시사점을 제공한다.

## Related Papers

- 🔄 다른 접근: [[papers/967_Global_patterns_of_migration_of_scholars_with_economic_devel/review]] — 기관-산업 이동의 미시적 효과와 국제 학자 이동의 거시적 패턴이라는 다른 스케일의 모빌리티 연구
- 🏛 기반 연구: [[papers/1030_The_Burden_of_Knowledge_and_the_Death_of_the_Renaissance_Man/review]] — 학술-산업 이동이 지식 부담 증가 시대에 연구자 전문성 확장의 대안적 경로가 될 수 있음
- 🧪 응용 사례: [[papers/978_Introducing_the_open_biomedical_map_of_science/review]] — 학술-산업 이동 연구를 생의학 지식 지도를 통해 특정 분야별 이동 패턴과 성과 차이 분석 가능
- 🔄 다른 접근: [[papers/967_Global_patterns_of_migration_of_scholars_with_economic_devel/review]] — 국가 간 학자 이동과 기관-산업 간 이동이라는 서로 다른 차원의 모빌리티 효과 비교 연구
- 🔄 다른 접근: [[papers/1000_Productivity_Prominence_and_the_Effects_of_Academic_Environm/review]] — 기관 간 이동이 연구 성과에 미치는 영향을 다른 관점에서 분석하여 환경 효과를 보완 설명한다.
- 🔗 후속 연구: [[papers/1026_Systematic_Inequality_and_Hierarchy_in_Faculty_Hiring_Networ/review]] — 교수 채용 네트워크의 위계가 기관 간 이동이 과학적 성과에 미치는 영향으로 이어진다.
