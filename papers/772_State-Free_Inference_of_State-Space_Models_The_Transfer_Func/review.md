---
title: "772_State-Free_Inference_of_State-Space_Models_The_Transfer_Func"
authors:
  - "Rom N. Parnichkun"
  - "Stefano Massaroli"
  - "Alessandro Moro"
  - "Jimmy T. H. Smith"
  - "Ramin Hasani"
date: "2024.05"
doi: ""
arxiv: ""
score: 4.25
essence: "상태공간모델(State-Space Model, SSM)을 전달함수(Transfer Function) 표현으로 재설계하여, 상태 크기의 증가에도 불구하고 메모리와 계산 비용이 증가하지 않는 상태-자유(state-free) 병렬 추론 알고리즘을 제안한다. FFT(Fast Fourier Transform)를 기반으로 한 이 접근법은 기존 S4/S5 대비 35% 더 빠른 학습 속도를 달성한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Neural_Differential_Equations"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Parnichkun et al._2024_State-Free Inference of State-Space Models The Transfer Function Approach.pdf"
---

# State-Free Inference of State-Space Models: The Transfer Function Approach

> **저자**: Rom N. Parnichkun, Stefano Massaroli, Alessandro Moro, Jimmy T. H. Smith, Ramin Hasani, Mathias Lechner, Qi An, Christopher Ré, Hajime Asama, Stefano Ermon, Taiji Suzuki, Atsushi Yamashita, Michael Poli | **날짜**: 2024-05-10

---

## Essence

상태공간모델(State-Space Model, SSM)을 전달함수(Transfer Function) 표현으로 재설계하여, 상태 크기의 증가에도 불구하고 메모리와 계산 비용이 증가하지 않는 상태-자유(state-free) 병렬 추론 알고리즘을 제안한다. FFT(Fast Fourier Transform)를 기반으로 한 이 접근법은 기존 S4/S5 대비 35% 더 빠른 학습 속도를 달성한다.

## Motivation

- **Known**: 선형 시간불변(LTI) SSM은 병렬 스캔(parallel scan) 또는 FFT를 통해 효율적인 시퀀스 병렬화가 가능하며, 상수 시간 자동회귀 추론을 지원한다.

- **Gap**: 기존 SSM들(S4, S5, LRU, Mamba)은 다음과 같은 문제점을 가진다:
  - 대각(diagonal) 모드 SSM은 표현력이 제한됨
  - 병렬 스캔은 상태-승법적(state-multiplicative) 메모리 복잡도 O(ℓn)를 가짐 (ℓ: 시퀀스 길이, n: 상태 크기)
  - S4/S4D의 Cauchy/Vandermonde 행렬 알고리즘은 O((ℓ+n)log²(ℓ+n))로 병목(FFT는 O(ℓlog ℓ))
  - 상태 크기가 클수록 메모리 사용량이 급증

- **Why**: 상태 크기 증가 시 메모리 비용이 선형적으로 증가하지 않으면서도, 완전한 표현력(dense 행렬 포함)을 유지하고 최적화된 FFT 알고리즘만 사용하는 방법이 필요.

- **Approach**: 상태공간모델을 유리 전달함수(Rational Transfer Function, RTF) 표현 H(z) = h₀ + (b₁z⁻¹ + ... + bₙz⁻ⁿ)/(1 + a₁z⁻¹ + ... + aₙz⁻ⁿ)로 직접 매개변수화하고, 분자/분모 계수(a, b)를 시퀀스 길이로 패딩한 후 FFT를 이용하여 임펄스 응답 필터를 계산.

## Achievement

![Figure 1](figures/fig1.webp)
*메모리 소비 측면에서 S5(스캔 기반)는 상태 크기에 따라 메모리가 급증하지만, RTF는 선형적으로 증가*

1. **상태-자유 복잡도 달성**: 
   - 공간 복잡도: **O(ℓ)** (상태 독립적)
   - 시간 복잡도: **O(ℓlog ℓ)** (FFT 기한)
   - 기존 S4는 O(ℓ+n), S5는 O(ℓn)

2. **완전한 표현력 보존**: 
   - 대각 행렬 제약 없이 임의의 밀집(dense) 상태 전이 행렬 A에 대응 가능
   - 선형 시불변 시스템의 완전한 함수 공간 포괄

3. **실증 성능**:
   - Long Range Arena (LRA) 벤치마크에서 S4 대비 **평균 35% 학습 속도 개선**
   - 어텐션-자유 모델 중 최고 수준 정확도 달성
   - WikiText103 언어모델링에서 Hyena 필터 기준선 대비 개선된 당혹도(perplexity)

## How

![Figure 2](figures/fig2.webp)
*상태-자유 병렬 추론 알고리즘: (a) RTF 표현, (b) 알고리즘 흐름도(rFFT→패딩→합성곱→irFFT), (c) 단일 스텝 추론용 재귀 형태*

- **전달함수 표현의 좌표 불변성(Coordinate Invariance)**: 
  상태공간 표현 (A, B, C, h₀)은 유사변환으로 무한히 많으나, 전달함수 H(z)는 고유하므로 매개변수화 안정성 증가

- **병렬 추론 알고리즘**:
  1. 분자 계수 b와 분모 계수 a를 시퀀스 길이 ℓ로 패딩
  2. 실수-FFT (rFFT)를 이용해 주파수 영역으로 변환
  3. 주파수 영역에서 요소별 곱셈(⊙) 수행
  4. 역FFT (irFFT)로 임펄스 응답 필터 h = [h₀, h₁, ..., hₗ₋₁] 복원
  5. 입력 u와 필터 h를 합성곱 (convolution): y = h ∗ u

- **재귀 형태(Recurrent Form)**: 
  자동회귀 생성 시에는 companion matrix 형태의 재귀식 사용으로 O(n²) 단일 스텝 계산 유지

- **안정성 보장**: 
  분모 계수 a로부터 특성 다항식의 근(pole)이 단위원 내부에 있도록 제약하여 BIBO 안정성 보장

## Originality

- **전달함수 기반 SSM 매개변수화**: 기존의 상태공간 직접 매개변수화(S4, S5) 또는 구조화 행렬(Structured matrix) 대신 유리 전달함수를 학습 파라미터로 사용 → 이론적으로 완전한 표현

- **순수 FFT 기반 추론**: 복잡한 Cauchy/Vandermonde 알고리즘 제거, 산업 표준 FFT 라이브러리 활용으로 플랫폼 최적화 용이

- **상태-자유성의 형식적 증명**: 메모리/시간 복잡도가 상태 크기 n과 무관함을 이론 및 실험으로 입증

- **재귀 형태와의 이중성**: 훈련 시 병렬 합성곱 모드, 추론 시 효율적 재귀 모드를 자유롭게 전환 가능한 설계

## Limitation & Further Study

- **수치 안정성**: FFT의 부동소수점 오차 축적이 긴 시퀀스에서 문제될 수 있으며, 안정성 분석 부족
  
- **비선형성 미지원**: LTI 시스템만 지원하므로 상태-의존적 가중치(상태-적응형 SSM)와 결합 불가

- **다중 채널 확장**: 다차원 시스템(MIMO)으로의 확장 방법이 명확하지 않음 (현재는 채널별 독립적 SISO 적용)

- **초기 상태 학습**: 초기 상태 x₀을 0으로 고정하는데, 학습 가능한 초기 상태의 영향 미탐색

- **후속 연구 방향**:
  - 고차 전달함수(분자 차수 > 분모 차수) 또는 다항식 근사를 통한 비선형 성분 통합
  - 혼합 정밀도(mixed-precision) 계산으로 수치 안정성 강화
  - 계층적 SSM 아키텍처와의 결합


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.5/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4.25/5

**총평**: 이 논문은 SSM의 전달함수 표현을 통해 상태 크기와 무관한 O(ℓ) 메모리 추론을 달성하는 우아한 이론적 기여와 35% 학습 속도 개선이라는 실질적 이득을 제공한다. 다만 수치 안정성 분석 부족, 비선형성 확장의 제한, MIMO 시스템 지원 미흡 등이 실무 적용 범위를 다소 좁힌다. 선형 시퀀스 모델링 분야에서 중요한 진전이나, 최근 하이브리드 아키텍처(예: Hyena+Mamba 계열) 대비 상대적 위치 재평가가 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/829_Towards_Foundation_Models_for_Scientific_Machine_Learning_Ch/review]] — 과학 머신러닝의 파운데이션 모델 패러다임이 상태공간모델의 전달함수 접근법에 기반을 제공한다
- 🔄 다른 접근: [[papers/454_Lagrangian_neural_networks/review]] — 상태공간 vs 라그랑주 기반 물리 시스템 모델링의 다른 수학적 접근법을 비교할 수 있다
- 🏛 기반 연구: [[papers/572_Neural_Ordinary_Differential_Equations/review]] — 신경 상미분방정식이 상태공간모델의 전달함수 표현에 수학적 기반을 제공한다
- 🔄 다른 접근: [[papers/574_Neural-POD_A_Plug-and-Play_Neural_Operator_Framework_for_Inf/review]] — 신경 연산자와 상태공간모델의 물리 기반 추론에서 다른 접근법을 비교할 수 있다
- 🧪 응용 사례: [[papers/829_Towards_Foundation_Models_for_Scientific_Machine_Learning_Ch/review]] — 과학 머신러닝 파운데이션 모델 패러다임을 상태공간모델의 물리 시스템 학습에 적용할 수 있다
- 🔄 다른 접근: [[papers/454_Lagrangian_neural_networks/review]] — 물리 시스템 모델링에서 라그랑주 vs 상태공간 기반의 다른 수학적 접근법을 비교할 수 있다
