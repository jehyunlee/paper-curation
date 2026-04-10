---
title: "961_Fast_Unfolding_of_Communities_in_Large_Networks"
authors:
  - "Vincent D Blondel"
  - "Jean-Loup Guillaume"
  - "Renaud Lambiotte"
  - "Etienne Lefebvre"
date: "2008"
doi: "10.1088/1742-5468/2008/10/P10008"
arxiv: ""
score: 4.0
essence: "대규모 네트워크의 커뮤니티 구조를 모듈성(modularity) 최적화를 통해 빠르게 추출하는 휴리스틱 알고리즘을 제안한다. 반복적인 두 단계(지역 최적화 및 커뮤니티 응집)를 통해 계층적 커뮤니티 구조를 효율적으로 도출한다."
tags:
  - "cat/Bibliometric_Network_Analysis"
  - "sub/Network_Structure_and_Detection"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Blondel et al._2008_Fast Unfolding of Communities in Large Networks.pdf"
---

# Fast Unfolding of Communities in Large Networks

> **저자**: Vincent D Blondel, Jean-Loup Guillaume, Renaud Lambiotte, Etienne Lefebvre | **날짜**: 2008 | **DOI**: [10.1088/1742-5468/2008/10/P10008](https://doi.org/10.1088/1742-5468/2008/10/P10008)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1. Visualization of the steps of our algorithm. Each pass is made of two phases:*

대규모 네트워크의 커뮤니티 구조를 모듈성(modularity) 최적화를 통해 빠르게 추출하는 휴리스틱 알고리즘을 제안한다. 반복적인 두 단계(지역 최적화 및 커뮤니티 응집)를 통해 계층적 커뮤니티 구조를 효율적으로 도출한다.

## Motivation

- **Known**: 네트워크 커뮤니티 탐지는 중요한 문제이며, 모듈성 최적화에 기반한 여러 알고리즘들이 존재한다. 기존의 가장 빠른 알고리즘(Clauset et al.)도 백만 노드 이상의 네트워크에서는 슈퍼커뮤니티 문제로 인해 계산 시간이 과도하게 증가한다.
- **Gap**: 기존 알고리즘들은 수백만 노드 규모의 대규모 네트워크에 적용 불가능하며, 계층적 커뮤니티 구조를 동시에 드러낼 수 없다. Facebook(6400만 사용자), 모바일 네트워크(2억 사용자) 등 초대형 네트워크 분석 기술이 부족하다.
- **Why**: 소셜 네트워크, 모바일 네트워크, 웹 그래프 등 현대 대규모 시스템의 구조를 이해하기 위해 빠르고 확장 가능한 커뮤니티 탐지 방법이 필수적이다. 커뮤니티 구조는 숨겨진 기능적 모듈(주제, 사이버커뮤니티 등)을 발굴하는 데 핵심 역할을 한다.
- **Approach**: 각 노드를 초기 커뮤니티로 시작하여, 각 노드에 대해 인접 커뮤니티로의 이동 시 모듈성 증가분을 계산하고 최대 증가를 제공하는 커뮤니티로 이동시킨다. 이를 반복하고 발견된 커뮤니티들로 새로운 네트워크를 구성하여 같은 과정을 재귀적으로 수행한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1. Visualization of the steps of our algorithm. Each pass is made of two phases:*

- **계산 복잡도 선형성**: 희소 네트워크에서 거의 선형 복잡도를 달성하여 152분 내 1.18억 노드 네트워크 분석 가능
- **모듈성 최적화 효율성**: 기존 최고 속도 알고리즘보다 우월한 모듈성 값을 달성하면서 계산 시간 단축
- **계층적 구조 자동 추출**: 반복적 패스를 통해 여러 해상도(resolution)의 커뮤니티 구조 자동 발견
- **해상도 한계 극복**: 기존 모듈성 최적화의 해상도 한계 문제를 다층 구조의 특성으로 자연스럽게 해결
- **실제 사례 검증**: 260만 고객의 벨기에 모바일 네트워크(언어 커뮤니티) 및 11억 이상의 링크를 가진 웹 그래프에서 성공적 검증

## How

![Figure 1](figures/fig1.webp)

*Figure 1. Visualization of the steps of our algorithm. Each pass is made of two phases:*

- 초기화: 각 노드를 별도 커뮤니티로 지정
- 1단계(지역 최적화): 각 노드 i에 대해 모든 인접 노드의 커뮤니티를 확인하고 식(2)를 이용해 모듈성 증가분 ΔQ 계산
- 모듈성 증가가 양수인 커뮤니티로 이동(음수 또는 0이면 현재 위치 유지)
- 모든 노드에 대해 지역 최대값(local maxima) 도달 시까지 반복 적용
- 2단계(커뮤니티 응집): 발견된 커뮤니티들을 신규 네트워크의 노드로 변환
- 커뮤니티 간 링크 가중치 = 원본 노드들 간 링크 가중치의 합
- 같은 커뮤니티 내 링크 = 신규 네트워크의 자기 루프(self-loop)로 반영
- 1단계와 2단계를 '패스(pass)'로 묶어 더 이상 개선 불가능할 때까지 반복

## Originality

- 기존 탐욕 알고리즘의 슈퍼커뮤니티 병목 현상을 제거하는 단순하면서도 효과적인 해결책 제시
- 지역 최적화와 커뮤니티 응집을 번갈아 수행하는 다단계 구조로 자연스러운 계층 구조 자동 추출
- 모듈성 증가분 계산 최적화(식 2)로 선형에 가까운 복잡도 달성
- 기존 방법들이 도달하지 못한 수억 노드 규모의 초대형 네트워크 처리 가능성 입증

## Limitation & Further Study

- 노드 처리 순서에 따라 결과 모듈성 값이 달라질 수 있음(저자들이 인정하나, 영향도는 크지 않다고 주장)
- 최적 노드 처리 순서 선택 문제는 미해결 상태로 계산 시간 더 개선 여지 있음
- 해상도 한계 문제를 '자연스럽게 극복'한다 주장하지만 엄밀한 증명 부재", '제시된 실제 사례가 2개뿐(벨기에 모바일 네트워크, 웹 그래프)으로 다양한 도메인 검증 필요
- 후속 연구: 노드 순서 선택 휴리스틱 개발, 가중 방향 그래프(directed weighted graphs) 확장, 오버래핑 커뮤니티(overlapping communities) 처리

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 대규모 네트워크 분석이라는 실질적 문제에 대해 우아하면서도 실용적인 알고리즘 솔루션을 제시했다. 선형에 가까운 복잡도와 우수한 모듈성, 자동 계층 구조 추출이라는 세 가지 장점을 동시에 달성한 점이 매우 인상적이며, 실제 초대형 네트워크에서의 성공 사례를 통해 방법론의 실용성을 입증했다.

## Related Papers

- 🔄 다른 접근: [[papers/948_Community_Detection_in_Graphs/review]] — 모듈성 기반 고속 알고리즘과 다른 커뮤니티 탐지 방법들을 종합적으로 비교할 수 있다.
- 🧪 응용 사례: [[papers/1024_Software_survey_VOSviewer_a_computer_program_for_bibliometri/review]] — VOSviewer는 Louvain 알고리즘을 구현하여 학술 네트워크의 커뮤니티 구조를 시각화하는 도구이다.
- 🔗 후속 연구: [[papers/985_Mapping_scientific_communities_at_scale/review]] — 대규모 과학 공동체 매핑에서 Louvain 알고리즘의 확장성과 실용적 구현 방안을 제시한다.
- 🔗 후속 연구: [[papers/948_Community_Detection_in_Graphs/review]] — 일반적 커뮤니티 탐지 이론을 대규모 네트워크에서 빠른 커뮤니티 구조 발견 알고리즘으로 구체화한다.
- 🔗 후속 연구: [[papers/947_Collective_dynamics_of_small-world_networks/review]] — 소규모 세계 네트워크의 커뮤니티 구조를 효율적으로 탐지하는 알고리즘적 접근법을 제공한다.
- 🏛 기반 연구: [[papers/929_A_network_approach_to_topic_models/review]] — 네트워크에서 커뮤니티 탐지의 기본 알고리즘을 제공하여 토픽 모델링을 커뮤니티 탐지로 재정의하는 이론적 기반이 된다.
