---
title: "957_Emergence_of_Scaling_in_Random_Networks"
authors:
  - "Albert-László Barabási"
  - "Réka Albert"
date: "1999"
doi: "10.1126/science.286.5439.509"
arxiv: ""
score: 4.0
essence: "복잡한 네트워크의 위상 구조가 스케일-프리(scale-free) 멱법칙 분포를 따르며, 이는 네트워크의 지속적 성장과 선호적 부착(preferential attachment)이라는 두 가지 보편적 메커니즘에서 비롯된다."
tags:
  - "cat/Bibliometric_Network_Analysis"
  - "sub/Network_Structure_and_Detection"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Barabási and Albert_1999_Emergence of Scaling in Random Networks.pdf"
---

# Emergence of Scaling in Random Networks

> **저자**: Albert-László Barabási, Réka Albert | **날짜**: 1999 | **DOI**: [10.1126/science.286.5439.509](https://doi.org/10.1126/science.286.5439.509)

---

## Essence


복잡한 네트워크의 위상 구조가 스케일-프리(scale-free) 멱법칙 분포를 따르며, 이는 네트워크의 지속적 성장과 선호적 부착(preferential attachment)이라는 두 가지 보편적 메커니즘에서 비롯된다.

## Motivation

- **Known**: 기존 Erdős-Rényi 랜덤 그래프 모델은 포아송 분포를 가정하며 highly connected 정점이 지수적으로 감소한다. 최근 수집된 대규모 네트워크 데이터가 이러한 예측과 맞지 않음을 보여준다.
- **Gap**: 기존 네트워크 모델들이 현실 네트워크의 두 가지 핵심 특성인 지속적 성장과 선호적 부착을 고려하지 않아 스케일-프리 분포를 설명할 수 없다.
- **Why**: 유전자 네트워크, 월드와이드웹, 사회 네트워크 등 다양한 복잡 시스템들이 동일한 스케일-프리 구조를 보이므로, 이의 일반적 원리를 이해하는 것은 다학제적 중요성을 갖는다.
- **Approach**: 성장 메커니즘(매 시간 새로운 정점 추가)과 선호적 부착 확률(기존 정점의 연결도에 비례)을 포함한 확률론적 모델을 제안하고, 실제 네트워크 데이터와 비교 검증한다.

## Achievement


- **스케일-프리 분포의 보편적 발견**: 배우 네트워크(γ=2.3), WWW(γ=2.1), 전력망(γ≃4), 인용 네트워크(γ=3) 등 다양한 시스템에서 멱법칙 지수 2.1~4의 일관된 패턴 발견
- **모델의 성공**: 성장과 선호적 부착을 포함한 모델이 γ_model=2.9±0.1의 스케일-프리 분포를 생성하며 시간에 무관한 정상상태(stationary state) 달성
- **필요조건 규명**: 두 가지 변형 모델(성장만, 부착만)의 실패를 통해 성장과 선호적 부착이 모두 필수임을 증명

## How


- 실제 네트워크 데이터: 영화 배우 협력 그래프, WWW 링크 구조, 전력망 위상, 학술지 인용 패턴 수집 및 P(k) 분포 분석
- 제안 모델: m₀개 초기 정점에서 시작하여 각 시간 단계에 m개 간선을 가진 새 정점 추가, 정점 i에 연결될 확률을 Π(kᵢ)=kᵢ/Σⱼkⱼ로 설정
- 비교 검증: 모델 A(균일 부착), 모델 B(고정 정점)과의 대조를 통해 성장+선호적 부착의 필요성 입증
- 역학 분석: 부착율 방정식 ∂kᵢ/∂t=kᵢ/2t를 통해 초기 연결도 차이가 증폭되는 현상 설명

## Originality

- 스케일-프리 분포의 보편성을 다양한 시스템에서 처음 체계적으로 입증
- 성장과 선호적 부착이라는 간단하지만 강력한 두 가지 원리로 복잡한 위상 구조 설명 가능함을 시연
- 자기조직화(self-organization)를 통한 스케일 불변성의 출현 메커니즘을 제시하여 복잡계 과학의 새로운 패러다임 제공

## Limitation & Further Study

- 모델이 정점 추가율과 부착 간선 수(m)가 상수라는 단순화된 가정을 함. 실제로는 이들이 시간 변동할 수 있음
- power grid 데이터는 크기가 작아 스케일링 영역이 덜 뚜렷하며, 전체 WWW 데이터의 부분 샘플만 사용
- 모델이 네트워크 구조 이외의 동역학(예: 정점 제거, 간선 제거)을 고려하지 않음
- 후속 연구로 다양한 m값, 시간 변동하는 성장률, 선호적 부착의 다른 함수형 등을 탐구할 필요 있음

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 논문은 복잡한 네트워크의 보편적 구조 원리를 간단한 확률 모델로 설명함으로써 복잡계 과학에 혁신적 기여를 한다. 스케일-프리 분포와 선호적 부착의 개념은 이후 네트워크 과학 전반에 거대한 영향을 미쳤다.

## Related Papers

- 🔄 다른 접근: [[papers/947_Collective_dynamics_of_small-world_networks/review]] — 작은 세계 네트워크와 스케일-프리 네트워크는 모두 실제 네트워크의 비자명한 위상 구조를 설명하는 대표적인 이론 모델이다.
- 🧪 응용 사례: [[papers/1046_The_structure_of_scientific_collaboration_networks/review]] — 과학자 협력 네트워크가 실제로 스케일-프리 특성을 보이는지 실증적으로 검증한 연구이다.
- 🔗 후속 연구: [[papers/1034_The_Increasing_Dominance_of_Teams_in_Production_of_Knowledge/review]] — 선호적 부착 메커니즘이 과학 연구에서 팀 규모 증가와 협력 패턴 형성에 어떻게 작용하는지 보여준다.
- 🏛 기반 연구: [[papers/1040_The_Price-Pareto_growth_model_of_networks_with_community_str/review]] — 무작위 네트워크에서 scale-free 특성의 출현 원리를 커뮤니티 구조를 가진 Price-Pareto 모델의 이론적 기반으로 제공한다.
- 🔗 후속 연구: [[papers/928_A_General_Theory_of_Bibliometric_and_Other_Cumulative_Advant/review]] — 누적 우위 과정을 무작위 네트워크에서 scale-free 특성이 출현하는 구체적 메커니즘으로 확장한다.
