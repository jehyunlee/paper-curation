---
title: "767_SPINONet_Scalable_Spiking_Physics-informed_Neural_Operator_f"
authors:
  - "Shailesh Garg"
  - "Luis Mandl"
  - "Somdatta Goswami"
  - "Souvik Chakraborty"
date: "2026.03"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "본 논문은 에너지 효율성을 갖춘 물리정보신경망(Physics-informed Neural Network, PINN) 기반의 연산자 학습 모델을 제안한다. 신경과학에 영감을 받은 스파이킹 뉴런(spiking neuron)을 통해 희소 이벤트 기반 연산을 구현하면서도 물리 제약 조건 시행에 필요한 미분 가능성을 유지하는 아키텍처적 분리(architectural separation)를 핵심으로 한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Physics-informed_Neural_Networks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Garg et al._2026_SPINONet Scalable Spiking Physics-informed Neural Operator for Computational Mechanics Applications.pdf"
---

# SPINONet: Scalable Spiking Physics-informed Neural Operator for Computational Mechanics Applications

> **저자**: Shailesh Garg, Luis Mandl, Somdatta Goswami, Souvik Chakraborty | **날짜**: 2026-03-23 | **DOI**: N/A

---

## Essence

본 논문은 에너지 효율성을 갖춘 물리정보신경망(Physics-informed Neural Network, PINN) 기반의 연산자 학습 모델을 제안한다. 신경과학에 영감을 받은 스파이킹 뉴런(spiking neuron)을 통해 희소 이벤트 기반 연산을 구현하면서도 물리 제약 조건 시행에 필요한 미분 가능성을 유지하는 아키텍처적 분리(architectural separation)를 핵심으로 한다.

## Motivation

- **Known**: DeepONet, Fourier Neural Operator(FNO), Wavelet Neural Operator(WNO) 등 물리정보 연산자 학습 기법이 계산역학 문제에서 우수한 성능을 입증했다. 특히 분리 가능한(separable) DeepONet은 고차원 문제에 확장 가능하다.

- **Gap**: 기존 모델들은 연속적으로 활성화된 뉴런(continuously active neurons)을 사용하여, 입력의 정보 함량과 무관하게 모든 forward 평가에서 전체 multiply-accumulate 연산을 수행한다. 이는 엣지 디바이스나 임베디드 환경과 같은 전력 제약 환경에서 배포 시 높은 계산 비용과 에너지 소비를 초래한다.

- **Why**: 매개변수화된 PDE 분석, 불확실성 정량화, 디지털 트윈 모델링 등에서 동일한 연산자를 반복적으로 평가해야 하기 때문에 에너지 효율성은 실무 적용의 핵심 요소이다.

- **Approach**: 신경과학에서 영감을 받은 희소 이벤트 기반 뉴런 모델과 분리 가능한 DeepONet 아키텍처의 구조적 특성을 결합한다. 입력 함수 인코딩 경로(branch)에만 스파이킹 동역학을 도입하고, 공간-시간 좌표 경로(trunk)는 연속 미분 가능하도록 유지하여 양립 불가능한 두 요구사항을 해결한다.

## Achievement

![Figure 1: Mean per-layer spiking activity in the branch-network VSN layers across all numerical examples.](figures/fig1.webp)
*모든 수치 예제에서 branch 네트워크 VSN 레이어의 계층별 평균 스파이킹 활동도*

1. **아키텍처적 분리를 통한 물리정보 스파이킹 연산자 학습**: SPINONet은 입력 함수 인코딩 경로에 Variable Spiking Neuron(VSN)을 도입하여 희소 이벤트 기반 연산을 가능하게 하면서, 좌표 종속 trunk 네트워크를 연속 미분 가능하게 유지함으로써 PDE 잔차 계산(residual computation)에 필요한 공간-시간 편미분을 정확히 계산할 수 있다. 좌표별 인수분해(coordinate-wise factorization)로 명시적 전체 메시 평가를 제거하여 해상도 증가에 따른 계산 비용이 선형적으로 증가한다.

2. **정확도 유지와 안정성 향상**: 시간 종속 및 정상 상태 PDE, 고차원 공간-시간-매개변수 설정을 포함한 다양한 벤치마크에서 SPINONet은 기존 물리정보 연산자 학습 기법(PI-DeepONet)과 비교하여 희소 통신으로 인한 성능 저하 없이 유사한 예측 정확도를 달성한다. 순수 물리정보 학습이 퇴화 해(spurious solution)로 수렴할 수 있는 어려운 영역에서, 소량의 감독 데이터(limited data supervision)를 하이브리드 방식으로 추가하면 근본적 물리정보 손실 함수 공식을 수정하지 않으면서도 성능과 안정성이 개선된다.

## How

![Figure 3: Viscous Burgers equation: Comparison of SPINONet and PI-DeepONet computational cost as a function](figures/fig3.webp)
*점성 Burgers 방정식: 함수 대비 SPINONet과 PI-DeepONet 계산 비용 비교*

![Figure 2: Representative spatio-temporal predictions on unseen test samples.](figures/fig2.webp)
*보이지 않은 테스트 샘플에 대한 대표적 공간-시간 예측*

- **분리 가능한 DeepONet 구조**: Vanilla DeepONet (식 2)을 확장하여 d차원 공간-시간 좌표에 대해 d개의 독립적 trunk 네트워크를 사용. 각 trunk 네트워크 $\text{tr}_j: \mathbb{R} \to \mathbb{R}^{pr}$는 일차원 좌표 $\xi_j$를 입력받아 $p \times r$ 크기의 기저 함수를 생성(여기서 $p$는 잠재 차원, $r$은 저차 분해 순위).

- **VSN 기반 희소 계수 생성**: Branch 네트워크에서 Variable Spiking Neuron을 사용하여 입력 함수 인코딩. VSN은 연속값 스파이크를 지원하여 회귀 및 연산자 학습에 적합. 스파이킹 활동이 낮으면 multiply-accumulate 연산 감소로 에너지 절감.

- **Forward-mode 자동 미분 활용**: 분리 가능한 구조에서 trunk 평가 비용을 $\mathcal{O}(d \cdot n_{\max})$로 제한 (여기서 $d$는 차원, $n_{\max}$는 최대 그리드 점수). Forward-mode 자동 미분으로 Jacobian-벡터 곱셈을 효율적으로 계산하여 PDE 잔차와 그래디언트 계산 비용을 추가로 감소.

- **하이브리드 학습**: 순수 물리정보 손실 $\mathcal{L}_{\text{PINN}}$과 제한된 감독 손실 $\mathcal{L}_{\text{data}}$를 결합하여 비합치(non-convex) 최적화에서의 수렴 안정성 향상: $\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{PINN}} + \lambda \mathcal{L}_{\text{data}}$

- **그래디언트 기반 학습**: 불연속 스파이킹 동역학에도 불구하고, straight-through estimator(STE) 또는 surrogate gradient method를 통해 역전파 가능하게 구현. VSN의 연속값 스파이크와 미분 가능 활성화 함수로 end-to-end 학습 가능.

## Originality

- **구조적 분리의 혁신**: 스파이킹 신경망과 물리정보 학습의 양립 불가능성(spiking dynamics의 불연속성 vs. PDE 미분 가능 요구)을 아키텍처 분리로 우아하게 해결. Branch(입력 인코딩)와 trunk(좌표 처리) 경로의 독립성을 활용한 첫 시도.

- **분리 가능한 DeepONet과 스파이킹의 결합**: 기존 neuroscience-inspired PINN은 해 네트워크(solution networks)에만 적용되었고, WNO에 적용된 사례가 유일했으나, SPINONet은 분리 가능한 DeepONet 구조에 처음으로 적용하여 고차원 확장성 달성.

- **하드웨어 무관적 효율성 분석**: 스파이킹 활동, 분리 가능한 trunk 평가, forward-mode 미분의 계산 및 에너지 절감 효과를 이론적으로 엄밀하게 정량화. 단순한 경험적 검증을 넘어 체계적 분석 제시.

- **회귀-친화적 뉴런 모델 선택**: Variable Spiking Neuron(VSN)을 채택하여 연속값 스파이크 지원으로 회귀 성능을 최적화. 기존 LIF(Leaky Integrate-and-Fire) 등과 달리 이산 스파이크 문제 회피.

## Limitation & Further Study

- **VSN 선택의 정당화 부족**: 논문에서 QIF(Quadratic Integrate-and-Fire) 모델과의 비교 분석이 제시되지 않았다. VSN vs. QIF의 회귀 성능, 계산 효율, 수렴 특성에 대한 실험적 비교가 필요하다.

- **에너지 절감 검증의 한계**: 하드웨어 무관적 계산 비용 분석은 제시되었으나, 실제 하드웨어(GPU, 뉴로모픽 칩, FPGA 등)에서의 에너지 소비 측정 및 검증이 부재하다. 단순 FLOPs 감소가 실제 전력 절감으로 변환되는지 실증적 확인 필요.

- **고차원 문제의 제한된 검증**: 논문에서 제시된 예제가 최대 몇 차원인지 명확하지 않다. "고차원" 확장성 주장을 뒷받침하기 위해 10차원 이상의 현실적 문제에 대한 추가 벤치마크 필요.

- **하이브리드 학습의 일반화**: 데이터 혼합 비율 $\lambda$ 선택 기준이 불명확하다. 문제별/데이터셋별 최적 $\lambda$ 결정 방법론 부재. 자동 적응형 $\lambda$ 조정 알고리즘 개발 필요.

- **스파이킹 활동의 동적 제어**: Fig. 1에서 층별 스파이킹 활동의 편차가 크게 나타난다. 활동도를 더 균등하게 제어하고 압축률을 극대화하는 기법 부족.

- **비정상 상태(Non-stationary) PDE**: 시간에 따라 물리 매개변수가 변하는 동역학계(예: 물질 특성 변화) 또는 인과적 구조 변화 문제에 대한 적용성 미검증.


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 3.5/5
- Overall: 4/5

## Related Papers

- 🏛 기반 연구: [[papers/721_Scientific_Machine_Learning_through_Physics-Informed_Neural/review]] — 물리 정보 신경망에 대한 종합 리뷰가 스파이킹 물리 정보 신경 연산자의 이론적 배경을 제공합니다.
- 🔗 후속 연구: [[papers/103_Architectures_variants_and_performance_of_neural_operators_A/review]] — 신경 연산자의 아키텍처와 변형에 대한 연구가 스파이킹 기반 에너지 효율적 설계로 확장됩니다.
- 🔄 다른 접근: [[papers/574_Neural-POD_A_Plug-and-Play_Neural_Operator_Framework_for_Inf/review]] — 계산 과학에서 에너지 효율적 스파이킹 기반과 플러그 앤 플레이 신경 연산자 접근법을 비교할 수 있습니다.
- 🔗 후속 연구: [[papers/721_Scientific_Machine_Learning_through_Physics-Informed_Neural/review]] — 에너지 효율적인 스파이킹 물리 정보 신경 연산자가 PINN의 계산 효율성을 향상시키는 확장 연구입니다.
