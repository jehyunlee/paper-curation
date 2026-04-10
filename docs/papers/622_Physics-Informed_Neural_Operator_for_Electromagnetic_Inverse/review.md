---
title: "622_Physics-Informed_Neural_Operator_for_Electromagnetic_Inverse"
authors:
  - "Q. C. Dong"
  - "Zi-Xuan Su"
  - "Qing Huo Liu"
  - "Wen Chen"
  - "Zhizhang Chen"
date: "2026.03"
doi: "미공개"
arxiv: ""
score: 4.0
essence: "본 논문은 신경 연산자(Neural Operator)와 물리 정보를 결합한 PINO 프레임워크를 제안하여 전자기 역산란 문제를 신속하고 정확하게 해결한다. 학습 가능한 텐서로 유전율을 표현하고 하이브리드 손실 함수(state loss, data loss, TV 정규화)로 신경 연산자와 물질 특성을 동시에 최적화한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Neural_Differential_Equations"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Dong et al._2026_Physics-Informed Neural Operator for Electromagnetic Inverse Scattering Problems.pdf"
---

# Physics-Informed Neural Operator for Electromagnetic Inverse Scattering Problems

> **저자**: Q. C. Dong, Zi-Xuan Su, Qing Huo Liu, Wen Chen, Zhizhang Chen | **날짜**: 2026-03-26 | **DOI**: [미공개](https://doi.org/)

---

## Essence

![Figure 2](figures/fig2.webp) 
*그림 2: 전자기 역산란 문제 해결을 위한 PINO 프레임워크. 정규화된 좌표 X, Y를 입력으로 하고, 신경 연산자의 출력은 예측된 유도 전류 Ĵ*

본 논문은 신경 연산자(Neural Operator)와 물리 정보를 결합한 PINO 프레임워크를 제안하여 전자기 역산란 문제를 신속하고 정확하게 해결한다. 학습 가능한 텐서로 유전율을 표현하고 하이브리드 손실 함수(state loss, data loss, TV 정규화)로 신경 연산자와 물질 특성을 동시에 최적화한다.

## Motivation

- **Known**: 기존의 대비 소스 역산란 (CSI: Contrast Source Inversion) 방법들은 비선형성과 병적 부정확성(ill-posedness)으로 인해 계산 시간이 길고 정확도가 낮으며 노이즈에 취약하다. 최근 딥러닝 기반 방법들(CNN, U-Net, GAN)은 속도 향상을 제공하지만 훈련 데이터 분포를 벗어난 경우 일반화 성능이 저하된다.

- **Gap**: 기존 데이터 기반 딥러닝 모델들은 물리 제약을 충분히 고려하지 못하며, 위상 정보가 없는 무위상 역산란(phaseless inversion)이나 다중 주파수 조건에서 유연한 대응이 어렵다.

- **Why**: 물리 정보와 신경 연산자를 통합하면 더 강력한 일반화 능력을 갖춘 통합 프레임워크를 구축할 수 있고, 다양한 측정 조건(단일/다중 주파수, 위상 유무)에서 적응 가능하다.

- **Approach**: FNO, U-FNO, F-FNO 세 가지 신경 연산자 아키텍처를 비교하며, 좌표 주파수 인코딩(frequency encoding)으로 공간 표현 능력을 강화하고, 상태 손실(state loss)과 데이터 손실(data loss)을 결합한 완전 미분 가능한 프레임워크를 구성한다.

## Achievement

![Figure 1](figures/fig1.webp)
*그림 1: 2차원 TMz 산란 시나리오 모델링 설정*

1. **우수한 복원 정확도**: 단일/다중 주파수 환경에서 노이즈(5%, 10%)가 있어도 기존 CSI 방법을 일관되게 능가하며, 위상 없는 데이터로도 안정적인 복원을 달성한다.

2. **유연한 일반화**: 하나의 신경 연산자로 여러 주파수에 대응 가능하고, 위상 정보 유무를 모두 처리할 수 있는 통일된 프레임워크를 제공한다.

3. **아키텍처 비교**: FNO, U-FNO, F-FNO의 성능 차이를 정량적으로 분석하여 각 신경 연산자의 장단점을 명확히 한다.

## How

![Figure 2](figures/fig2.webp)

- **주파수 인코딩**: 공간 좌표 (X, Y)를 삼각함수 기저 함수로 인코딩하여 M=10까지의 고주파 정보를 표현 능력에 추가한다.

- **신경 연산자 구조**: 선형 lifting 연산자 P로 인코딩된 입력을 고차원 특징 공간으로 투영하고, Fourier 변환 기반 kernel 연산자 K를 통해 반복적으로 특징 필드를 업데이트한다 (d₀ → d₁ → ... → dₙ).

- **학습 가능한 텐서**: 유전율 대비 χ̂를 신경망 파라미터와 독립적인 학습 가능한 텐서로 표현하여 물질 특성 공간을 직접 최적화한다.

- **하이브리드 손실 함수** (식 15):
  - **State loss** (식 13): Lippmann-Schwinger 적분 방정식으로부터 유도되어 물리 제약을 강제한다.
  - **Data loss** (식 14): 측정 산란장 데이터 d*와의 일치를 보장한다.
  - **TV 정규화**: ‖∇χ̂‖₁/₂ 항으로 복원 이미지의 평탄성을 강제하여 과적합을 방지한다.

- **무위상 역산란**: 위상 정보 손실에 의한 비선형성 완화를 위해 softplus 함수로 χ̂를 재매개변수화하여 비음성 제약을 적용한다 (식 16).

## Originality

- **신경 연산자 + 물리 정보 결합**: NeRF 개념을 차용한 좌표 주파수 인코딩과 신경 연산자를 전자기 역산란에 처음 적용하여 기존 CNN/U-Net 기반 방법과 차별화된다.

- **학습 가능한 텐서 표현**: 신경망과 별도로 물질 특성을 직접 최적화하는 설계는 물리 제약과 데이터 기반 학습을 명확히 분리하여 해석성을 높인다.

- **완전 미분 가능한 프레임워크**: 무위상 데이터 처리를 포함한 여러 역산란 시나리오를 단일 프레임워크로 통합하며, 기존 CSI의 복잡한 재공식화 없이 손실 함수 수정만으로 대응 가능하다.

- **다중 신경 연산자 비교**: FNO, U-FNO, F-FNO를 같은 프레임워크 내에서 체계적으로 비교하여 아키텍처 선택에 대한 실용적 지침을 제공한다.

## Limitation & Further Study

- **제한사항**:
  - 2D TMz 문제에만 적용되었으며, 3D 또는 다른 편광 모드로의 확장 가능성이 명확하지 않다.
  - 학습에 필요한 훈련 데이터셋의 규모와 생성 방법이 명시되어 있지 않아 실제 적용 난이도를 평가하기 어렵다.
  - 하이퍼파라미터 λ₁, λ₂, λᴿ의 선택 기준과 민감도 분석이 제시되지 않았다.
  - 무위상 역산란에서 softplus 재매개변수화의 효과에 대한 이론적 근거가 부족하다.

- **후속 연구**:
  - 3D 벡터 파 문제 및 다양한 매질 모델로의 확장
  - 비선형 신경 연산자(nonlinear operator) 적용 가능성 탐색
  - 실험 데이터와의 검증을 통한 실제 응용성 평가
  - 신경 연산자의 물리 정보 부호화 메커니즘에 대한 이론적 분석
  - 불확실성 정량화(uncertainty quantification) 추가

## Evaluation

- **Novelty**: 4/5 — 신경 연산자와 물리 정보 결합은 신선하지만, 기본 개념(NeRF, FNO)은 기존 기술이며 역산란 문제 자체는 잘 알려진 영역이다.

- **Technical Soundness**: 4/5 — 수식 유도와 프레임워크 설계가 건전하고, 정규화 설정이 합리적이나, 하이퍼파라미터 선택과 무위상 데이터 처리의 이론적 정당화가 미흡하다.

- **Significance**: 4/5 — 통일된 역산란 프레임워크로서 실용적 가치가 있고, CSI 대비 명확한 성능 향상을 보이나, 2D 문제 제한과 훈련 데이터 요구사항이 임팩트를 제한한다.

- **Clarity**: 3/5 — 전체 구조는 명확하나, 훈련 절차, 데이터셋 생성, 하이퍼파라미터 선택 상세가 부족하며, 프리프린트 상태로 일부 섹션이 미완성이다.

- **Overall**: 4/5

**총평**: 본 논문은 신경 연산자와 물리 정보를 통합하여 전자기 역산란 문제에 새로운 접근법을 제시하며, 다양한 측정 조건에서 기존 방법 대비 우수한 성능을 입증한다. 다만 2D 제한, 훈련 데이터 세부 사항 미흡, 이론적 심화가 필요하고, 3D 확장과 실험 검증을 통한 실제 응용성 강화가 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/621_Physics-informed_neural_network_for_multi-objective_design_o/review]] — 물리 정보 신경 연산자를 전자기 역산란과 열관리 설계라는 서로 다른 물리 문제에 적용한 사례들이다.
- 🏛 기반 연구: [[papers/574_Neural-POD_A_Plug-and-Play_Neural_Operator_Framework_for_Inf/review]] — 즉석 학습을 위한 신경 연산자 플러그인 프레임워크가 전자기 역산란 문제 해결의 기술적 기반을 제공한다.
- 🔗 후속 연구: [[papers/427_Incorporating_Continuous_Dependence_Qualifies_Physics-Inform/review]] — 연속 의존성을 고려한 PINN 개선 방법을 전자기 역산란의 신경 연산자 학습에 적용할 수 있다.
- 🔗 후속 연구: [[papers/440_Inverse_designing_metamaterials_with_programmable_nonlinear/review]] — 메타물질 역설계를 위한 GNN 접근법이 전자기 역문제 해결을 위한 물리 정보 기반 신경 연산자로 확장되었다
- 🏛 기반 연구: [[papers/576_Nonlinear_stochastic_and_quantum_motion_from_Coulomb_forces/review]] — 물리 정보 신경 연산자의 전자기 역산란 적용 연구에서 쿨롱 상호작용의 물리적 이해가 도움이 될 수 있다.
- 🔄 다른 접근: [[papers/621_Physics-informed_neural_network_for_multi-objective_design_o/review]] — 물리 정보 신경망의 다목적 설계 최적화와 전자기 역산란 문제라는 서로 다른 공학적 응용을 보여준다.
