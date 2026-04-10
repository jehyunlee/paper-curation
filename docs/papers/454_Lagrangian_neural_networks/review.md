---
title: "454_Lagrangian_neural_networks"
authors:
  - "Miles Cranmer"
  - "Sam Greydanus"
  - "Stephan Hoyer"
  - "Peter Battaglia"
  - "David N. Spergel"
date: "2020"
doi: "10.48550/arXiv.2003.04630"
arxiv: ""
score: 4.2
essence: "신경망으로 라그랑주 함수(Lagrangian)를 직접 학습하여 정규 좌표계(canonical coordinates) 없이도 물리계의 에너지 보존 법칙을 자동으로 만족하는 동역학 모델을 구축한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Neural_Differential_Equations"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Cranmer et al._2020_Lagrangian neural networks.pdf"
---

# Lagrangian neural networks

> **저자**: Miles Cranmer, Sam Greydanus, Stephan Hoyer, Peter Battaglia, David N. Spergel, Shirley Ho | **날짜**: 2020 | **DOI**: [10.48550/arXiv.2003.04630](https://arxiv.org/abs/2003.04630)

---

## Essence

신경망으로 라그랑주 함수(Lagrangian)를 직접 학습하여 정규 좌표계(canonical coordinates) 없이도 물리계의 에너지 보존 법칙을 자동으로 만족하는 동역학 모델을 구축한다.

## Motivation

- **Known**: 신경망은 이미지 분류, 자연어 처리 등에서 뛰어난 성능을 보이지만, 에너지·운동량 보존 같은 기본 물리 대칭성을 학습하지 못한다.
- **Gap**: 기존 해밀턴 신경망(HNN)은 정준 좌표 조건(식 1의 Poisson bracket 관계)을 만족해야 하는데, 많은 실제 데이터셋이 이를 만족하지 않는다. 깊은 라그랑주 네트워크(DeLaN)는 운동에너지 형태를 $T = \dot{q}^T M \dot{q}$로 제한한다.
- **Why**: 라그랑주 형식(Lagrangian formalism)은 정준 좌표를 요구하지 않으면서도 에너지 보존을 자동으로 보장하므로, 임의의 좌표계에서 동작 가능한 일반적 모델을 만들 수 있다.
- **Approach**: 신경망으로 파라미터화된 라그랑주 함수 $L$에 대해 오일러-라그랑주 방정식(식 3-6)을 수치적으로 풀어 가속도를 계산하고, JAX를 이용해 효율적으로 구현한다.

## Achievement

![Figure 1](https://arxiv.org/html/2003.04630v2/x1.png)
*라그랑주 신경망(LNN, 파란색)은 기존 신경망(빨간색)과 달리 장시간에 걸쳐 에너지를 보존한다.*

1. **이중 진자 문제**: LNN이 기존 신경망 대비 에너지 오차를 20배 감소(8% → 0.4%)시키며, 정확도는 유사하게 유지

2. **특수상대론 입자**: 정준 좌표 없이도 상대론적 라그랑주 함수 $L = ((1-\dot{q}^2)^{-1/2}-1) + gq$를 학습하여 HNN이 실패하는 경우를 극복

3. **1D 파동 방정식**: 라그랑주 그래프 네트워크(Lagrangian Graph Network)를 통해 연속 시스템과 격자 구조에도 확장 가능함을 입증

## How

![Figure 2](https://arxiv.org/html/2003.04630v2/x2.png)
*이중 진자에서 단시간(a)은 비슷하지만, 장시간 에너지 추적(b)에서 LNN의 우월성이 명확히 드러난다.*

**핵심 기술:**

- **오일러-라그랑주 방정식 수치화** (식 6):
  - 매개변수 라그랑주 $L_\theta$에 대해 $\ddot{q} = (\nabla_{\dot{q}}\nabla_{\dot{q}}^T L)^{-1}[\nabla_q L - (\nabla_q\nabla_{\dot{q}}^T L)\dot{q}]$ 계산
  - 헤시안(Hessian) 역행렬 계산 필요 → JAX의 자동 미분으로 효율적 구현

- **활성화 함수 선택**: 2차 미분이 필요하므로 ReLU 대신 softplus 사용 (하이퍼파라미터 탐색 결과)

- **라그랑주 그래프 네트워크** (식 7-8):
  - 라그랑주 밀도 $L_i$를 각 격자점에서 국소적으로 계산하고 합산
  - 그래프 구조를 활용하여 헤시안 희소성(sparsity) 이용 가능

- **손실함수**: 예측 가속도 $\ddot{x}_L$과 실제 가속도 $\ddot{x}_{true}$ 간 오차

![Figure 3](https://arxiv.org/html/2003.04630v2/x3.png)
*상대론적 입자에서 HNN은 정준 좌표 없으면 실패(a)하지만, LNN은 임의 좌표(c)에서도 동작한다.*

## Originality

- **정준 좌표 요구 제거**: 라그랑주 형식의 본질적 특성을 활용하여 HNN의 주요 제약 극복
- **일반적 라그랑주 함수 학습**: DeLaN과 달리 운동에너지 형태에 제약 없음 (예: 상대론적, 자기장 내 입자 등 지원)
- **그래프/연속 시스템 확장**: 라그랑주 그래프 네트워크를 통해 편미분 방정식 영역으로 확장
- **JAX 기반 효율적 구현**: 고차 미분과 행렬 역산을 간결하게 구현하는 방법론 제시

## Limitation & Further Study

- **계산복잡성**: 헤시안 역산이 $O(d^3)$이므로 고차원 시스템(large $d$)에서 확장성 제한
- **특이 헤시안**: 의사 역행렬(pseudoinverse) 사용하지만, 시스템이 물리적으로 이상한 경우 안정성 미지수
- **초기화 민감성**: 부록 C의 특별한 초기화 스킴 필수 → 일반화 가능성 확인 필요
- **후속 연구 방향**:
  - 고차원 복잡계(분자동역학, 유체역학)에 대한 확장성 검증
  - 노이즈 있는 실측 데이터에 대한 견고성 평가
  - 비보존 힘(비보존력, damping)이 있는 개방계 모델링 방법
  - 다른 물리 대칭성(회전 불변성, 게이지 대칭성) 통합 가능성

## Evaluation

- **Novelty**: 4.5/5 — 라그랑주 형식 기반 접근은 새로우며, HNN의 제약을 본질적으로 해결
- **Technical Soundness**: 4/5 — 오일러-라그랑주 방정식의 수치 구현은 타당하나, 고차원에서의 수치 안정성 분석 부족
- **Significance**: 4.5/5 — 물리-기반 신경망의 중요한 진전; 상대론, 파동방정식 등 다양한 응용 가능성
- **Clarity**: 4/5 — 이론 설명은 명확하나, JAX 구현 세부사항은 부록에만 있음
- **Overall**: 4.2/5

**총평**: 라그랑주 형식의 수학적 우아함을 신경망에 결합하여 정준 좌표 없이도 에너지 보존을 자동으로 만족하는 모델을 제시한 기여작. 다만 계산 복잡도와 고차원 시스템 확장성은 향후 과제이다.

## Related Papers

- 🏛 기반 연구: [[papers/427_Incorporating_Continuous_Dependence_Qualifies_Physics-Inform/review]] — 라그랑주 기반 물리 법칙 보존이 물리정보신경망의 연속 의존성 구현에 기반을 제공한다
- 🔄 다른 접근: [[papers/304_Efficient_and_Equivariant_Graph_Networks_for_Predicting_Quan/review]] — 고전역학 vs 양자역학 시스템에서 물리 법칙 보존 신경망의 다른 적용을 비교할 수 있다
- 🧪 응용 사례: [[papers/140_Autonomous_reinforcement_learning_agent_for_chemical_vapor_d/review]] — 라그랑주 신경망의 에너지 보존 법칙을 화학기상증착 공정 모델링에 적용할 수 있다
- 🔄 다른 접근: [[papers/772_State-Free_Inference_of_State-Space_Models_The_Transfer_Func/review]] — 물리 시스템 모델링에서 라그랑주 vs 상태공간 기반의 다른 수학적 접근법을 비교할 수 있다
- 🔄 다른 접근: [[papers/572_Neural_Ordinary_Differential_Equations/review]] — 물리 시스템 모델링을 Neural ODE vs Lagrangian 신경망으로 접근한다.
- 🧪 응용 사례: [[papers/140_Autonomous_reinforcement_learning_agent_for_chemical_vapor_d/review]] — 물리 법칙 보존을 고려한 신경망을 화학기상증착 공정 최적화에 적용할 수 있다
- 🔄 다른 접근: [[papers/304_Efficient_and_Equivariant_Graph_Networks_for_Predicting_Quan/review]] — 양자 시스템 vs 고전 역학 시스템에서 물리 법칙 보존 신경망의 다른 적용 분야를 비교할 수 있다
- 🔄 다른 접근: [[papers/772_State-Free_Inference_of_State-Space_Models_The_Transfer_Func/review]] — 상태공간 vs 라그랑주 기반 물리 시스템 모델링의 다른 수학적 접근법을 비교할 수 있다
- 🔗 후속 연구: [[papers/427_Incorporating_Continuous_Dependence_Qualifies_Physics-Inform/review]] — 라그랑주 신경망의 물리 법칙 보존 개념을 연속 의존성으로 확장한 연구다
