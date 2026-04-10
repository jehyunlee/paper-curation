---
title: "947_Collective_dynamics_of_small-world_networks"
authors:
  - "Duncan J. Watts"
  - "Steven H. Strogatz"
date: "1998.06"
doi: "10.1038/30918"
arxiv: ""
score: 5.0
essence: "규칙적 네트워크와 무작위 네트워크 사이의 중간 영역에 위치한 '소규모 세계(small-world)' 네트워크를 제안하며, 이러한 네트워크가 높은 군집화와 짧은 경로 길이를 동시에 가지는 특성을 규명했다."
tags:
  - "cat/Bibliometric_Network_Analysis"
  - "cat/Scientific_Information_Systems"
  - "sub/Network_Structure_and_Detection"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Watts and Strogatz_1998_Collective dynamics of ‘small-world’ networks.pdf"
---

# Collective dynamics of ‘small-world’ networks

> **저자**: Duncan J. Watts, Steven H. Strogatz | **날짜**: 6/1998 | **DOI**: [10.1038/30918](https://doi.org/10.1038/30918)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2 Characteristic path length L(p) and clustering coefﬁcient C(p) for the*

규칙적 네트워크와 무작위 네트워크 사이의 중간 영역에 위치한 '소규모 세계(small-world)' 네트워크를 제안하며, 이러한 네트워크가 높은 군집화와 짧은 경로 길이를 동시에 가지는 특성을 규명했다.

## Motivation

- **Known**: 기존 네트워크 모델링은 완전히 규칙적이거나 완전히 무작위인 구조를 가정했으나, 실제 생물학적, 기술적, 사회적 네트워크들은 이 두 극단 사이에 위치한다는 것이 알려져 있다.
- **Gap**: 규칙성과 무작위성 사이의 중간 영역(0 < p < 1)에 대한 이해가 부족하며, 실제 자연 현상에서 이러한 중간 구조의 존재와 기능적 중요성이 입증되지 않았다.
- **Why**: 작은 세계 네트워크의 존재와 특성을 이해하면 전염병 확산, 신호 전파, 계산 능력 등 동역학적 시스템의 기능을 예측하고 최적화할 수 있으며, 실제 자연 네트워크의 진화와 설계 원리를 규명할 수 있다.
- **Approach**: 규칙적 고리 격자에서 시작하여 무작위 재배선(random rewiring) 절차로 네트워크를 튜닝하고, 특성 경로 길이(L)와 군집화 계수(C)로 구조적 특성을 정량화한 후, 실제 세 가지 실제 네트워크(배우 협력 그래프, 전력망, C. elegans 신경망)에 적용하여 검증했다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2 Characteristic path length L(p) and clustering coefﬁcient C(p) for the*

- **소규모 세계 네트워크의 정의 및 수학적 특성화**: 무작위 재배선 확률 p에 따라 L(p)는 빠르게 감소하지만 C(p)는 거의 변하지 않는 현상을 발견하여, 높은 군집화와 짧은 경로 길이를 동시에 달성하는 네트워크 구조를 규명했다.
- **단축(short cuts)의 중요성 입증**: 소수의 장거리 연결이 전체 경로 길이에 비선형적으로 큰 영향을 미치는 메커니즘을 규명했다.
- **실제 네트워크의 소규모 세계 성질 입증**: 영화배우 협력 그래프, 미국 서부 전력망, C. elegans 신경망 등 세 가지 실제 시스템이 모두 소규모 세계 특성을 만족함을 입증했다.
- **동역학적 함의**: 소규모 세계 네트워크에서 신호 전파 속도 향상, 계산 능력 증가, 동기화 가능성 개선, 전염병 확산 용이성 증가 등을 예측했다.

## How

![Figure 1](figures/fig1.webp)

*Figure 1 Random rewiring procedure for interpolating between a regular ring*

- 무작위 재배선 확률 p(0 ≤ p ≤ 1)를 매개변수로 하는 네트워크 생성 알고리즘 개발
- 특성 경로 길이 L(p) (전역적 특성)과 군집화 계수 C(p) (국소적 특성) 정의 및 계산
- 이론적 극한값 비교: 규칙 격자(p=0)의 L ~ n/2k, C ~ 3/4 vs 무작위 네트워크(p=1)의 L ~ ln(n)/ln(k), C ~ k/n
- 세 가지 실제 네트워크에서 L과 C 계산: 영화배우 협력 그래프(IMDb 데이터), 전력망(미국 서부), C. elegans 신경망
- 전염병 확산 시뮬레이션으로 동역학적 기능 검증

## Originality

- 규칙-무작위 연속체(regularity-randomness continuum) 개념으로 네트워크 공간을 새로운 관점에서 체계화했다.
- 단순한 재배선 메커니즘만으로 높은 군집화와 짧은 경로 길이의 모순적 결합을 달성하는 현상을 처음 규명했다.
- 이전에 별도의 현상으로 여겨진 '소규모 세계 현상(six degrees of separation)'을 수학적으로 설명하는 구체적 네트워크 모델을 제시했다.", '단일 모델로 사회망, 기술망, 생물망을 통일적으로 설명할 수 있는 프레임워크를 제공했다.

## Limitation & Further Study

- 실제 네트워크의 형성 메커니즘과 진화 과정이 무작위 재배선과 정확히 일치하는지 미확인 상태이다.
- 소규모 세계 특성의 발현에 필요한 최소 재배선 비율의 정확한 임계값이 규명되지 않았다.
- 네트워크 크기, 차수 분포, 가중치 등 다양한 실제 특성에 따른 일반화 가능성이 추가 검증이 필요하다.
- 후속 연구는 소규모 세계 네트워크가 자연 과정에서 어떻게 자발적으로 형성되는지, 그리고 진화적 이점이 무엇인지 규명해야 한다.

## Evaluation

- Novelty: 5/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 5/5
- Overall: 5/5

**총평**: 이 논문은 네트워크 과학의 기초를 확립하는 획기적 연구로, 단순하고 우아한 수학적 모델로 복잡한 자연 현상을 설명하며, 이후 수십 년간 네트워크 분석, 복잡계 과학, 사회과학 등 다양한 분야에 광범위한 영향을 미쳤다.

## Related Papers

- 🧪 응용 사례: [[papers/1046_The_structure_of_scientific_collaboration_networks/review]] — 소규모 세계 네트워크 이론을 실제 과학자 협력 네트워크에 적용하여 과학 커뮤니티의 구조적 특성을 규명한다.
- 🏛 기반 연구: [[papers/948_Community_Detection_in_Graphs/review]] — 소규모 세계 네트워크의 커뮤니티 구조를 탐지하고 분석하기 위한 다양한 알고리즘적 접근법을 제공한다.
- 🔗 후속 연구: [[papers/1040_The_Price-Pareto_growth_model_of_networks_with_community_str/review]] — 소규모 세계 특성을 가진 네트워크에서 커뮤니티별 이질적 성장 dynamics를 모델링하는 확장된 프레임워크를 제안한다.
- 🧪 응용 사례: [[papers/960_Evolution_of_the_social_network_of_scientific_collaborations/review]] — 소규모 세계 이론을 과학 협력 네트워크의 시간적 진화 패턴 분석에 적용한다.
- 🔗 후속 연구: [[papers/961_Fast_Unfolding_of_Communities_in_Large_Networks/review]] — 소규모 세계 네트워크의 커뮤니티 구조를 효율적으로 탐지하는 알고리즘적 접근법을 제공한다.
- 🔄 다른 접근: [[papers/957_Emergence_of_Scaling_in_Random_Networks/review]] — 작은 세계 네트워크와 스케일-프리 네트워크는 모두 실제 네트워크의 비자명한 위상 구조를 설명하는 대표적인 이론 모델이다.
- 🏛 기반 연구: [[papers/990_Networks_of_Scientific_Papers/review]] — 과학논문 인용 네트워크의 small-world 특성을 이해하기 위해 네트워크의 기본 구조적 특성을 제공한다.
