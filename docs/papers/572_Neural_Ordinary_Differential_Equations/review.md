---
title: "572_Neural_Ordinary_Differential_Equations"
authors:
  - "Ricky T. Q. Chen"
  - "Yulia Rubanova"
  - "Jesse Bettencourt"
  - "David Duvenaud"
date: "2018.06"
doi: "10.48550/arXiv.1806.07366"
arxiv: ""
score: 4.4
essence: "기존의 이산 깊이(discrete depth) 신경망 대신 숨겨진 상태의 도함수를 신경망으로 매개변수화하고, 이를 상미분방정식(ODE) 초기값 문제로 정의하여 블랙박스 ODE 솔버로 계산하는 혁신적 연속깊이(continuous-depth) 신경망 모델을 제안한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Neural_Differential_Equations"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chen et al._2018_Neural Ordinary Differential Equations.pdf"
---

# Neural Ordinary Differential Equations

> **저자**: Ricky T. Q. Chen, Yulia Rubanova, Jesse Bettencourt, David Duvenaud | **날짜**: 2018-06-19 | **DOI**: [10.48550/arXiv.1806.07366](https://doi.org/10.48550/arXiv.1806.07366)

---

## Essence

![Figure 1](figures/fig1.webp) *좌측: 잔차 네트워크는 이산적 유한 변환 시퀀스 정의 / 우측: ODE 네트워크는 연속적으로 상태를 변환하는 벡터장 정의*

기존의 이산 깊이(discrete depth) 신경망 대신 숨겨진 상태의 도함수를 신경망으로 매개변수화하고, 이를 상미분방정식(ODE) 초기값 문제로 정의하여 블랙박스 ODE 솔버로 계산하는 혁신적 연속깊이(continuous-depth) 신경망 모델을 제안한다.

## Motivation

- **Known**: 잔차 네트워크(ResNet)와 정규화 흐름(normalizing flows)은 이산 시퀀스의 변환을 합성하여 복잡한 변환을 구성한다. 이러한 반복 업데이트는 연속 변환의 오일러 이산화(Euler discretization)로 해석될 수 있다.

- **Gap**: 
  1. 깊은 신경망 학습의 메모리 비용이 깊이에 비례하여 증가
  2. 모든 입력에 동일한 계산 전략 적용
  3. 정규화 흐름에서 야코비안 행렬식 계산의 세제곱 복잡도 병목
  4. 이산 RNN은 임의의 시간 도착 데이터를 자연스럽게 처리할 수 없음

- **Why**: 극한에서 계층을 무한히 추가하고 단계를 무한히 작게 하면 연속 동역학을 ODE로 표현할 수 있으며, 이는 위의 모든 문제를 해결할 수 있는 잠재력을 가짐

- **Approach**: 
  1. 수반민감도 방법(adjoint sensitivity method)을 이용한 ODE 솔버를 통한 효율적 역전파
  2. 인스턴트 변수변환 정리(instantaneous change of variables theorem)로 연속 정규화 흐름 구축
  3. 적응형 ODE 솔버를 활용한 문제 복잡도에 따른 계산 비용 조절

## Achievement

![Figure 2](figures/fig2.webp) *역모드 미분(adjoint sensitivity method)을 통한 ODE 솔버의 블랙박스 기울기 계산. 증강 ODE를 역시간으로 해결하여 원래 상태와 손실에 대한 민감도 동시 계산*

1. **메모리 효율성**: 깊이에 무관한 상수 메모리 비용으로 임의의 깊이 신경망 학습 가능 (O(1) vs O(L))

2. **적응형 계산**: 최신 ODE 솔버의 적응 단계 크기 제어로 입력과 문제 복잡도에 따라 계산 비용 동적 조절 가능

![Figure 3](figures/fig3.webp) *학습된 ODE-Net의 통계: (a) 오차 제어 가능성 (b) 함수 평가 횟수와 계산 시간 선형 관계 (c) 역전파 시 평가 횟수가 정방향의 약 절반 (d) 학습 진행에 따른 함수 평가 횟수 증가*

3. **연속 정규화 흐름**: 행렬식 계산 대신 대각합(trace) 연산으로 O(D³)에서 O(D)로 복잡도 개선, 데이터 차원 분할/순서 제약 제거

4. **연속 시계열 모델**: 임의 시간 도착 데이터를 자연스럽게 처리 가능

## How

![Figure 4](figures/fig4.webp) *인스턴트 변수변환 정리: 연속 변환에서 로그 확률 변화가 야코비안 대각합의 음수로 표현되어 정규화 흐름의 계산 비용 급격히 감소*

**핵심 기술:**

- **수반민감도 방법 (Adjoint Sensitivity Method)**:
  - 손실 L에 대한 상태의 민감도를 정의: a(t) = ∂L/∂z(t)
  - 민감도의 역시간 ODE 정의: da(t)/dt = -a(t)ᵀ∂f/∂z
  - 매개변수 기울기: dL/dθ = -∫a(t)ᵀ∂f/∂θ dt
  - Algorithm 1: 증강 상태 벡터로 z, a, ∂L/∂θ를 단일 ODE 솔버 호출로 동시 계산

- **인스턴트 변수변환 정리 (Theorem 1)**:
  - 연속 확률 변수 z(t)에 대해: ∂log p(z(t))/∂t = -tr(∂f/∂z(t))
  - 야코비안 행렬식 대신 대각합만 계산하면 되므로 O(D) 복잡도 달성
  - 여러 함수 합: tr(∑Jₙ) = ∑tr(Jₙ) 이용하여 M개 은닉유닛에 대해 O(M) 선형 비용

- **구현 전략**:
  - scipy의 implicit Adams 방법(LSODE/VODE) 사용
  - Python autograd로 수반민감도 방법 구현
  - GPU에서 동역학 및 도함수 계산, Fortran ODE 솔버와 통합

## Originality

- **패러다임 전환**: 이산 레이어 시퀀스에서 연속 동역학으로의 근본적 개념 전환

- **수학적 우아성**: 수반민감도 방법을 블랙박스 ODE 솔버에 적용하여 내부 구조 접근 불필요

- **인스턴트 변수변환 정리**: 연속 변환에서 야코비안 행렬식이 대각합으로 축약되는 놀라운 성질 증명

- **선형 확장성**: 정규화 흐름의 은닉유닛 수에 대한 선형 시간 복잡도 처음 달성

- **다분야 적용**: 지도학습, 생성모델, 시계열 분석에 통일된 프레임워크 제공

## Limitation & Further Study

- **계산 오버헤드**: ODE 솔버 호출 비용이 높아 실제 ResNet보다 벽시계 시간(wall-clock time) 상 이점이 미미 (Table 1에서 메모리는 O(1)이지만 시간은 O(L̃))

- **깊이 정의의 모호성**: "연속 깊이"의 정확한 정의 부재, 함수 평가 횟수로만 측정 가능 (Figure 3d에서 학습 중 증가 추세)

- **ODE 가정 검증**: Lipschitz 연속성 및 비특이성(non-singularity) 가정이 실제 신경망 동역학에서 성립하는지 경험적 검증 부족

- **수치 안정성**: 역시간 ODE 풀이 시 수치 오차 누적 가능성, 극단적으로 낮은 오차 허용도에서의 안정성 미검토

- **후속 연구 방향**:
  - 더 복잡한 데이터셋(ImageNet 등)에서의 확장성 검증
  - 비가역 동역학을 허용하는 정규화 흐름 변형
  - 시간 가변 네트워크 아키텍처(하이퍼네트워크)의 체계적 설계
  - 메모리와 속도 트레이드오프의 최적화
  - 확률적 ODE(stochastic ODE) 확장

## Evaluation

- **Novelty**: 4.5/5
  - 연속 동역학으로의 패러다임 전환과 수반민감도 방법 응용은 매우 창의적
  - 인스턴트 변수변환 정리는 예상 밖의 수학적 발견
  - 다만 ODE와 신경망 연결의 기초는 선행연구(Lu et al. 2017, Haber & Ruthotto 2017)에 의존

- **Technical Soundness**: 4.5/5
  - 수반민감도 방법의 수학적 유도가 엄밀하고 Algorithm 1의 구현 명확
  - 인스턴트 변수변환 정리 증명(Appendix A) 타당함
  - 다만 실무 구현에서 암묵적 ODE 솔버의 비선형 최적화 비용, 정확도 제어의 실제 효과 등 세부사항 미흡

- **Significance**: 4.5/5
  - 이후 생성모델, 동역학 학습 분야의 광범위한 후속 연구 촉발 (Neural ODE 기반 연구 수백 편 이상)
  - NeurIPS 2018 최고 인용도 논문 중 하나
  - 실제 산업 응용(의료 진단, 금융 시계열 등)으로 확대 가능성 높음
  - 다만 현 단계에서는 ResNet 대비 벽시계 시간 이점 부재로 실용성 제한

- **Clarity**: 4/5
  - 핵심 아이디어(이산 → 연속)의 설명이 직관적이고 Figure 1의 시각화 우수
  - Algorithm 1이 명확하고 재현 가능
  - 다만 Section 4의 정규화 흐름 부분은 수식이 빠르게 진행되어 수학적 배경 필요
  - 실제 구현(TensorFlow → Fortran → autograd 파이프라인)의 복잡성이 과소 표현됨

- **Overall**: 4.4/5

**총평**: 
이 논문은 신경망을 연속 동역학 시스템으로 재개념화하여 메모리 효율성, 적응형 계산, 선형 복잡도 정규화 흐름이라는 혁신적 이점을 제시한 획기적 작업이다. 수반민감도 방법의 우아한 적용과 인스턴트 변수변환 정리의 수학적 발견은 진정한 원창성을 보여준다. 다만 실제 벽시계 시간 성능, 극단 케이스에서의 수치 안정성, 더 복잡한 데이터셋에서의 검증 등이 미흡하여, 개념적으로는 5점에 가깝지만 현실적 구현과 검증에서 4점 수준의 한계가 있다. 이론의 우아함과 잠재력만큼은 매우 높으며, 이후 학계의 광범위한 응용과 확장으로 이어진 점에서 그 영향력은 측정 불가능할 정도로 크다.

## Related Papers

- 🔗 후속 연구: [[papers/619_Physics_Informed_Deep_Learning_Part_I_Data-driven_Solutions/review]] — Neural ODE가 물리 정보 기반 신경망의 연속시간 모델링을 가능하게 한다.
- 🔗 후속 연구: [[papers/574_Neural-POD_A_Plug-and-Play_Neural_Operator_Framework_for_Inf/review]] — Neural ODE 개념을 신경 연산자 프레임워크로 확장한다.
- 🔄 다른 접근: [[papers/454_Lagrangian_neural_networks/review]] — 물리 시스템 모델링을 Neural ODE vs Lagrangian 신경망으로 접근한다.
- 🔗 후속 연구: [[papers/103_Architectures_variants_and_performance_of_neural_operators_A/review]] — 신경 ODE를 신경 연산자로 확장하는 방법론적 연결점을 제시한다.
- 🏛 기반 연구: [[papers/721_Scientific_Machine_Learning_through_Physics-Informed_Neural/review]] — 신경 상미분방정식이 물리 정보 신경망의 기본적인 수치 해법 이론적 토대를 제공합니다.
- 🏛 기반 연구: [[papers/619_Physics_Informed_Deep_Learning_Part_I_Data-driven_Solutions/review]] — Neural ODE가 Physics-Informed Neural Networks의 연속시간 모델링 기초를 제공한다.
- 🏛 기반 연구: [[papers/772_State-Free_Inference_of_State-Space_Models_The_Transfer_Func/review]] — 신경 상미분방정식이 상태공간모델의 전달함수 표현에 수학적 기반을 제공한다
- 🏛 기반 연구: [[papers/574_Neural-POD_A_Plug-and-Play_Neural_Operator_Framework_for_Inf/review]] — Neural ODE의 연속 시간 동역학 모델링이 Neural-POD의 비선형 직교 기저함수 학습 방법론의 기반이 됨
- 🏛 기반 연구: [[papers/364_From_Theory_to_Application_A_Practical_Introduction_to_Neura/review]] — 신경 상미분방정식이 신경 연산자 아키텍처의 수학적 기반을 제공
- 🔗 후속 연구: [[papers/576_Nonlinear_stochastic_and_quantum_motion_from_Coulomb_forces/review]] — 신경 상미분방정식의 기본 개념을 비선형 확률적 양자 운동 모델링에 확장 적용할 수 있다.
