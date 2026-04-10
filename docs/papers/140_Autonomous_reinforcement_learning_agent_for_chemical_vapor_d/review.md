---
title: "140_Autonomous_reinforcement_learning_agent_for_chemical_vapor_d"
authors:
  - "P. Rajak"
  - "A. Krishnamoorthy"
  - "Ankit Mishra"
  - "R. Kalia"
  - "A. Nakano"
date: "2021"
doi: "10.1038/s41524-021-00535-3"
arxiv: ""
score: 4.25
essence: "오프라인 강화학습(Offline Reinforcement Learning)을 활용하여 화학기상증착(CVD)을 통한 MoS₂ 양자소재 합성의 최적 합성 스케줄을 자동으로 예측하는 에이전트를 개발했으며, 10,000개의 반응 분자동역학 시뮬레이션 데이터로 학습하여 높은 품질의 결정성 MoS₂를 생성하는 미지의 합성 조건을 발견했다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Materials_Discovery_Hypotheses"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Rajak et al._2021_Autonomous reinforcement learning agent for chemical vapor deposition synthesis of quantum materials.pdf"
---

# Autonomous reinforcement learning agent for chemical vapor deposition synthesis of quantum materials

> **저자**: P. Rajak, A. Krishnamoorthy, Ankit Mishra, R. Kalia, A. Nakano | **날짜**: 2021 | **DOI**: [10.1038/s41524-021-00535-3](https://doi.org/10.1038/s41524-021-00535-3)

---

## Essence

오프라인 강화학습(Offline Reinforcement Learning)을 활용하여 화학기상증착(CVD)을 통한 MoS₂ 양자소재 합성의 최적 합성 스케줄을 자동으로 예측하는 에이전트를 개발했으며, 10,000개의 반응 분자동역학 시뮬레이션 데이터로 학습하여 높은 품질의 결정성 MoS₂를 생성하는 미지의 합성 조건을 발견했다.

## Motivation

- **Known**: 고성능 재료 발굴은 계산 재료 과학을 통해 급속히 진전되었으나(수십만 개 재료 스크리닝), 실제 합성 방법론 개발은 여전히 시행착오 기반의 경험적 접근에 의존하고 있어 약 20년의 재료 개발 기간이 소요됨
- **Gap**: CVD와 같은 비용액 기반 양자 재료 합성은 온도, 농도 등 시간-상관 매개변수가 복잡하게 얽혀 있어 기존 고처리량(high-throughput) 실험 합성이나 텍스트 마이닝 기반 ML 기법으로는 미흡함
- **Why**: 합성 스케줄 최적화는 수천 개의 조정 가능한 매개변수와 거대한 탐색 공간에서 시간 수열의 순차적 의사결정 문제로, 이는 강화학습의 적합한 응용 분야임
- **Approach**: 반응 분자동역학(RMD) 시뮬레이션으로 10,000개 합성 데이터 생성 → 신경 자기회귀 밀도 추정기(NADE-CVD)로 빠른 대체 모델 구축 → 오프라인 모델 기반 강화학습으로 최적 합성 정책 발굴

## Achievement

![Figure 1: RMD 계산 합성의 개요. (a) 20나노초 길이의 단일 합성 스케줄에 대한 RMD 시뮬레이션 도식. 초기 MoO₃ 슬래브가 시간-변동 황화 환경과 반응하여 MoS₂ 및 MoO₃₋ₓ로 구성된 최종 구조를 생성. (b) MoS₂ 합성의 RMD 시뮬레이션 스냅샷. S₂, H₂, H₂S 가스를 포함하는 황화 환경이 시뮬레이션 셀 중앙의 MoOₓSᵧ 슬래브와 반응.](figures/fig1.webp)

1. **NADE-CVD 모델의 높은 정확도**: 10,000개 RMD 시뮬레이션으로 훈련된 신경망 기반 대체 모델이 약 3.5 원자(RMSE) 오차로 CVD 합성 결과를 예측하여, 개별 상(phase)에 대해 ≤30 원자 이내의 최대 예측 오차 달성

2. **미지의 최적 합성 스케줄 발굴**: RL 에이전트가 학습한 임계 온도(threshold temperature)와 화학포텐셜(chemical potential)을 기반으로 높은 결정성, 상순도(phase purity)를 갖는 반도성 MoS₂를 생성하는 기존에 알려지지 않은 합성 조건 예측

3. **장시간 거동 예측 가능성**: 분자동역학 시뮬레이션의 적용 범위를 넘어 실험 합성과 직접 연관된 더 긴 시간 스케일의 반응 시스템 거동 예측 가능성 입증

## How

![Figure 2: NADE-CVD를 통한 합성 스케줄 출력 예측. (a, b) 베이즈 네트워크의 구조. (c) NADE-CVD 모델 아키텍처로, 인코더, 디코더, 및 순환 신경망(RNN)으로 구성되며, 시뮬레이션 이력 Z₁:ₜ, X₁:ₜ에 의해 인코딩된 숨겨진 상태 hₜ의 함수로서 평균 μₜ₊₁과 분산 σₜ₊₁을 출력.](figures/fig2.webp)

**반응 분자동역학 시뮬레이션**:
- MoO₃ 결정과 H₂S, S₂, H₂를 포함하는 황화 환경의 다단계 반응 모의
- 20나노초를 20개 단계(각 1ns)로 분할, 매 단계마다 온도(T), 분자 개수(nH₂, nS₂, nH₂S) 4가지 변수로 정의된 합성 quartet 사용
- 각 RMD 시뮬레이션은 약 2일 소요

**신경 자기회귀 밀도 추정기(NADE-CVD) 모델**:
- 베이즈 네트워크로 CVD 합성 과정을 확률적 표현으로 변환
- 관측 변수 X(합성 조건): 온도, 기체 농도
- 비관측 변수 Z: 시간 의존적 상 분율(2H, 1T, 결함)
- 조건부 독립성을 활용한 자기회귀 확률 밀도 함수: P(Zₜ₊₁|Z₁:ₜ, X₁:ₜ) = N(μₜ₊₁, σₜ₊₁)
- 인코더-디코더 및 RNN 구조로 합성 이력 인코딩

**오프라인 모델 기반 강화학습**:
- NADE-CVD 모델을 정책 평가 환경으로 사용하여 최적 합성 정책 학습
- 보상 함수: 2H 반도성 상의 최대 상 분율 달성 시간 최소화
- 오프라인 학습으로 안전성 보장 (실험 비용 절감)

## Originality

- **학제 간 혁신**: 강화학습을 재료 합성 최적화에 최초 적용하여 시간-상관 다중 매개변수의 순차적 최적화 문제를 체계적으로 해결
- **계산 과학과의 통합**: RMD 시뮬레이션으로 충분한 훈련 데이터 생성하고, 신경망 기반 대체 모델(NADE-CVD)로 계산 비용을 1000배 이상 단축
- **오프라인 강화학습의 재료 과학 응용**: 실험 데이터의 부재 또는 부족 상황에서 시뮬레이션 기반 데이터만으로 학습 가능한 오프라인 RL의 장점 활용
- **물리적 해석 가능성**: 임계 온도, 화학포텐셜 등 물리적 의미 있는 합성 매개변수 상관관계 발굴

## Limitation & Further Study

**한계**:
- 현재 MoS₂ 단일 재료에만 적용하였으며, 다른 2D 재료나 벌크 재료로의 확장성 미검증
- NADE-CVD 모델은 훈련 데이터 분포 범위 내에서만 신뢰도 높은 예측 제공 (외삽 제한)
- RMD 시뮬레이션 자체의 정확도 한계(예: 장거리 상호작용, 양자 효과 미흡)가 최종 모델 성능에 반영
- 실험적 검증 미실시 (계산 결과의 실험 재현성 미확인)

**후속 연구**:
- 다양한 2D 양자 재료(WS₂, MoSe₂ 등)와 복잡한 다상(multi-phase) 헤테로구조 합성으로 확장
- 다중 목표(multi-task) 강화학습으로 결정성, 상순도, 합성 시간, 비용 등 여러 목적함수 동시 최적화
- 실험 데이터와의 피드백 루프 구축으로 모델 검증 및 재훈련
- 다른 합성 방법(PVD, 용액 기반 등)으로의 적용 확대

## Evaluation

- **Novelty** (독창성): 4.5/5  
  강화학습을 재료 합성 설계에 최초 적용하고, NADE-CVD를 통한 확률적 모델링이 참신하나, 단일 재료(MoS₂)에 국한

- **Technical Soundness** (기술적 타당성): 4/5  
  RMD, NADE, RL의 각 구성 요소는 견고하고 수학적으로 엄밀하나, 실험 검증 부재로 예측 신뢰도 완전히 확인되지 않음

- **Significance** (중요도): 4.5/5  
  재료 개발 시간 단축이라는 거대한 도전에 체계적 접근을 제시하며, 다른 재료 과학 문제로의 확장 가능성 높음

- **Clarity** (명확성): 4/5  
  방법론 설명이 대체로 명확하나, NADE 모델의 상세한 아키텍처 및 RL 보상 함수 설계에 대한 추가 설명 필요

- **Overall** (종합): 4.25/5

**총평**: 강화학습과 계산 모의를 결합하여 재료 합성 최적화라는 미충족 문제에 데이터 기반 혁신적 솔루션을 제시한 의미 있는 연구이나, 단일 사례 연구(MoS₂)이고 실험 검증이 미흡하여 일반화 가능성 평가가 향후 필요하다.

## Related Papers

- 🧪 응용 사례: [[papers/454_Lagrangian_neural_networks/review]] — 물리 법칙 보존을 고려한 신경망을 화학기상증착 공정 최적화에 적용할 수 있다
- 🏛 기반 연구: [[papers/829_Towards_Foundation_Models_for_Scientific_Machine_Learning_Ch/review]] — 과학 머신러닝의 파운데이션 모델 패러다임이 화학 공정 최적화에 적용될 수 있는 이론적 기반을 제공한다
- 🔄 다른 접근: [[papers/249_Curriculum_Reinforcement_Learning_from_Easy_to_Hard_Tasks_Im/review]] — 강화학습을 통한 과학적 과제 해결에서 단일 vs 다중 과제 학습의 다른 접근법을 비교할 수 있다
- 🔗 후속 연구: [[papers/662_Reinforcement_Learning_for_Dynamic_Microfluidic_Control/review]] — 오프라인 강화학습의 견고성 평가 방법론을 화학 공정 제어에 적용한 확장 연구다
- 🔗 후속 연구: [[papers/380_Generative_machine_learning_in_adaptive_control_of_dynamic_m/review]] — 화학 기상 증착 프로세스에서 자율 강화학습 에이전트로 생성형 머신러닝 제어를 확장한다.
- 🧪 응용 사례: [[papers/829_Towards_Foundation_Models_for_Scientific_Machine_Learning_Ch/review]] — 편미분방정식 학습의 사전학습-미세조정 패러다임을 화학 공정 최적화에 적용할 수 있다
- 🧪 응용 사례: [[papers/454_Lagrangian_neural_networks/review]] — 라그랑주 신경망의 에너지 보존 법칙을 화학기상증착 공정 모델링에 적용할 수 있다
- 🔗 후속 연구: [[papers/1125_Accelerating_cell_culture_media_development_using_Bayesian_o/review]] — 화학 기상 증착의 자율 강화학습에서 베이지안 최적화로의 확장
