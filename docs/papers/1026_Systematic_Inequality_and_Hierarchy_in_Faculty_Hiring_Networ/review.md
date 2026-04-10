---
title: "1026_Systematic_Inequality_and_Hierarchy_in_Faculty_Hiring_Networ"
authors:
  - "Aaron Clauset"
  - "Samuel Arbesman"
  - "Daniel B. Larremore"
date: "2015.02"
doi: "10.1126/sciadv.1400005"
arxiv: ""
score: 4.0
essence: "대학원 졸업생의 교수 채용 네트워크를 분석하여 학계의 체계적 불평등과 계층 구조를 정량화하고, 박사 학위 기관의 명성(prestige)이 최종 배치를 더 잘 예측함을 보여줌."
tags:
  - "cat/Research_Quality_and_Demographics"
  - "cat/Bibliometric_Network_Analysis"
  - "sub/Bias_and_Inequality"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Clauset et al._2015_Systematic inequality and hierarchy in faculty hiring networks.pdf"
---

# Systematic inequality and hierarchy in faculty hiring networks

> **저자**: Aaron Clauset, Samuel Arbesman, Daniel B. Larremore | **날짜**: 2015-02-06 | **DOI**: [10.1126/sciadv.1400005](https://doi.org/10.1126/sciadv.1400005)

---

## Essence

![Figure 2](figures/fig2.webp)

*Fig. 2. Inequality in faculty production. (A) Lorenz curves showing the fraction of*

대학원 졸업생의 교수 채용 네트워크를 분석하여 학계의 체계적 불평등과 계층 구조를 정량화하고, 박사 학위 기관의 명성(prestige)이 최종 배치를 더 잘 예측함을 보여줌.

## Motivation

- **Known**: 교수 채용 시장은 학자의 경력과 학문적 우선순위를 형성하지만, 시스템 차원의 정량적 이해가 부족함. U.S. News & World Report 같은 순위는 기관을 독립적으로 평가하여 상호작용을 반영하지 못함.
- **Gap**: faculty hiring network(누가 누구의 대학원 졸업생을 교수로 채용하는지)의 전체 구조와 패턴을 정량적으로 분석한 연구가 없음. 명성(prestige)이 채용 결정에 미치는 영향을 체계적으로 측정할 방법이 부족함.
- **Why**: 교수 채용은 학문 분야의 연구 우선순위, 교육 성과, 개인의 경력 궤적, 자원 배분을 근본적으로 형성하므로, 이 시스템의 불평등 구조를 이해하는 것은 학계 개혁과 공정성 개선에 필수적임.
- **Approach**: 컴퓨터과학, 경영학, 역사학 3개 분야의 약 19,000명의 교수진 배치 데이터를 hand-curated하여 comprehensive network 구축. Minimum violation ranking(최소 위반 순위) 기법을 사용하여 관찰된 채용 네트워크를 가장 잘 설명하는 기관 명성 순위를 추출.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2. Inequality in faculty production. (A) Lorenz curves showing the fraction of*

- **계층적 불평등의 정량화**: Gini 계수(G = 0.62-0.76)로 측정한 결과, faculty production이 매우 불평등하며 미국 소득 불평등(G = 0.45)보다도 심함. 상위 25% 기관이 71-86%의 교수를 배출
- **명성의 예측력**: 박사 학위 기관의 명성(prestige ranking)이 U.S. News & World Report 순위보다 최종 배치(ultimate placement)를 더 잘 예측
- **젠더 격차**: 같은 기관 졸업 여성이 남성보다 일반적으로 더 나쁜 배치 결과를 보임
- **선순환 구조**: 기관 명성이 높을수록 faculty production, faculty placement, 학문 내 영향력이 모두 증가하는 긍정적 feedback loop 발견
- **분야 간 공통 패턴**: computer science, business, history 등 이질적 분야에서도 동일한 steep hierarchical structure 확인

## How

![Figure 1](figures/fig1.webp)

*Fig. 1. Prestige hierarchies in faculty hiring networks. (Top) Placements for 267 computer science*

- 3개 분야(computer science, business, history)의 Ph.D.-granting institutions에서 완전하고 수작업으로 검증된 faculty placement 데이터 수집
- Faculty hiring network를 directed graph로 모델링 (vertex = institution, directed edge (u,v) = v의 교수 중 u에서 박사학위 취득)
- Minimum violation ranking 알고리즘 적용하여 각 edge가 downward pointing할 확률을 최대화하는 prestige hierarchy 추출
- Gini coefficient를 사용하여 faculty production의 불평등 정량화
- Kolmogorov-Smirnov test로 size-proportional placement hypothesis 검정
- Prestige ranking과 U.S. News & World Report, NRC 순위의 예측력 비교
- 성별에 따른 배치 결과 분석

## Originality

- **Novel network-based prestige ranking 기법**: 기관 간의 실제 상호작용(faculty hiring)을 기반으로 prestige를 추출하는 새로운 방법론. 기존 input-based ranking(reputation, wealth)과 달리 output-based assessment 제공
- **사회 불평등 측정의 이전(transfer)**: Gini coefficient 같은 경제학적 불평등 척도를 학계에 적용하여 새로운 관점 제공
- **Faculty hiring과 사회 계층화의 연결**: 학계 채용 시스템과 사회적 위계 구조 사이의 명시적 연결 시도
- **대규모 hand-curated dataset**: 약 19,000명의 faculty에 대한 정교하게 검증된 데이터베이스 구축으로 신뢰도 높은 분석 기반 제공

## Limitation & Further Study

- **지리적 제한**: 북미 기관만 포함되어 있어 전 지구적 학계 구조를 반영하지 못함
- **시간적 정적(static) 분석**: 특정 시점의 스냅샷이므로 hiring patterns의 시간적 변화와 동역학(dynamics)을 포착하지 못함
- **명성과 능력의 혼동**: Prestige rank가 merit(능력)과 status(지위)를 모두 반영하므로, 비-공정성 요소의 정확한 기여도 분리 어려움
- **3개 분야의 제한적 대표성**: 더 다양한 분야(STEM, 사회과학, 인문학 등)를 포함하여 결과의 보편성 검증 필요
- **후속 연구 방향**: 시계열 분석으로 prestige hierarchy의 안정성과 변화 추적; 여성과 소수자 그룹의 배치 차이 심화 원인 분석; 비-공정성 요소(지역, 언어, 문화자본)의 영향 정량화

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 학계의 불평등 구조를 처음으로 체계적으로 정량화하고, 명성(prestige)이 실제 채용 결정에 미치는 강력한 영향을 네트워크 분석으로 입증한 획기적 연구. 방법론은 우아하고 결과는 명확하지만, 시간적 동역학과 지역적 보편성 검증이 필요함.

## Related Papers

- 🏛 기반 연구: [[papers/1000_Productivity_Prominence_and_the_Effects_of_Academic_Environm/review]] — 교수 채용의 계층적 불평등이 이후 연구 환경과 성과에 미치는 지속적 영향을 보여주는 연결고리를 제공한다.
- 🔗 후속 연구: [[papers/970_Historical_Comparison_of_Gender_Inequality_in_Scientific_Car/review]] — 학계 채용 불평등의 역사적 변화와 성별 격차를 함께 분석하면 구조적 불평등의 전체적 양상을 파악할 수 있다.
- 🧪 응용 사례: [[papers/976_Intersectional_inequalities_in_science/review]] — 교차적 불평등 관점에서 채용 네트워크의 계층 구조가 다양한 정체성 집단에 미치는 복합적 영향을 분석할 수 있다.
- 🔗 후속 연구: [[papers/1121_Superstar_Extinctionsupsup/review]] — 교수 채용 네트워크의 위계적 불평등을 협업 네트워크 붕괴가 개별 연구자에게 미치는 영향으로 확장한다.
- 🔄 다른 접근: [[papers/967_Global_patterns_of_migration_of_scholars_with_economic_devel/review]] — 국내 교수 채용의 위계구조 대신 국제적 학자 이주 패턴과 경제발전 간의 관계를 분석한다.
- 🔗 후속 연구: [[papers/973_Impacts_of_inter-institutional_mobility_on_scientific_perfor/review]] — 교수 채용 네트워크의 위계가 기관 간 이동이 과학적 성과에 미치는 영향으로 이어진다.
- ⚖️ 반론/비판: [[papers/1039_The_Preeminence_of_Ethnic_Diversity_in_Scientific_Collaborat/review]] — 명성 기반 위계구조의 문제점에 대해 민족적 다양성이 과학 협력에 미치는 긍정적 효과를 제시한다.
- 🏛 기반 연구: [[papers/1000_Productivity_Prominence_and_the_Effects_of_Academic_Environm/review]] — 교수 채용 네트워크에서 나타나는 체계적 불평등이 학술 환경의 명성 효과를 뒷받침하는 구조적 기반을 제공한다.
- 🏛 기반 연구: [[papers/955_Does_Science_Advance_One_Funeral_at_a_Time/review]] — 교수 채용 네트워크의 위계적 불평등 구조가 저명 과학자의 영향력과 후속 연구자 진입 패턴을 설명하는 이론적 토대를 제공한다.
- 🧪 응용 사례: [[papers/999_Principles_of_Scientific_Research_Team_Formation_and_Evoluti/review]] — 교수 채용 네트워크의 체계적 불평등을 팀 형성 원리로 분석할 수 있다
