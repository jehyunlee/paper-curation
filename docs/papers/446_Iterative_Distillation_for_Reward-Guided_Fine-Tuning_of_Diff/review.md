---
title: "446_Iterative_Distillation_for_Reward-Guided_Fine-Tuning_of_Diff"
authors:
  - "Xingyu Su"
  - "Xiner Li"
  - "Masatoshi Uehara"
  - "Sunwoo Kim"
  - "Yulai Zhao"
date: "2025"
doi: "10.48550/arXiv.2507.00445"
arxiv: ""
score: 4.5
essence: "생물분자 설계에서 미분불가능한 보상함수(reward function)를 최적화하기 위해 확산모델(diffusion model)을 안정적으로 미세조정하는 새로운 프레임워크 VIDD(Value-guided Iterative Distillation for Diffusion models)를 제안한다. 기존 강화학습 기반 방법들의 불안정성과 모드 붕괴 문제를 오프정책(off-policy) 학습과 정방향 KL 발산(forward KL divergence) 최소화를 통해 해결한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Reward-guided_Diffusion_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Su et al._2025_Iterative Distillation for Reward-Guided Fine-Tuning of Diffusion Models in Biomolecular Design.pdf"
---

# Iterative Distillation for Reward-Guided Fine-Tuning of Diffusion Models in Biomolecular Design

> **저자**: Xingyu Su, Xiner Li, Masatoshi Uehara, Sunwoo Kim, Yulai Zhao | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2507.00445](https://doi.org/10.48550/arXiv.2507.00445)

---

## Essence

생물분자 설계에서 미분불가능한 보상함수(reward function)를 최적화하기 위해 확산모델(diffusion model)을 안정적으로 미세조정하는 새로운 프레임워크 VIDD(Value-guided Iterative Distillation for Diffusion models)를 제안한다. 기존 강화학습 기반 방법들의 불안정성과 모드 붕괴 문제를 오프정책(off-policy) 학습과 정방향 KL 발산(forward KL divergence) 최소화를 통해 해결한다.

## Motivation

- **Known**: 확산모델은 단백질, 작은 분자 등 복잡한 고차원 데이터 분포 모델링에 탁월하며, 컴퓨터 비전에서는 미분가능한 보상함수의 기울기 역전파(gradient backpropagation)로 최적화 가능
- **Gap**: 생물분자 설계 분야에서 보상함수는 물리 시뮬레이터(예: AutoDock Vina), 구조 검증 알고리즘(예: DSSP), 신경망 기반 예측기(예: AlphaFold3) 등 대부분 미분불가능하므로 직접 역전파 불가능
- **Why**: 기존 RL 기반 방법(PPO, DPOK, DDPO)은 온정책(on-policy) 특성으로 인해 탐색 범위가 좁고, 역방향 KL 발산 목적함수는 모드 추구 행동으로 모드 붕괴를 야기하며, 확산 모델 미세조정 시 높은 불안정성을 보임
- **Approach**: 오프정책 수집 단계(roll-in), 값함수 기반 소프트 최적정책 모의(roll-out), 정방향 KL 발산 최소화를 통한 모델 업데이트(model update)의 세 단계를 반복하는 정책 증류(policy distillation) 프레임워크

## Achievement

![Figure 1](figures/fig1.webp)
*그림 1: VIDD의 개요. 오프정책 롤인, 값함수 기반 보상가중 롤아웃, 정방향 KL 기반 모델 업데이트를 반복적으로 수행*

1. **안정성 향상**: 오프정책 데이터 수집과 정방향 KL 목적함수를 통해 온정책 방법 대비 훈련 안정성이 향상되고 모드 붕괴 위험 감소

2. **샘플 효율 개선**: 기존 RL 방법들(PPO, DDPO)보다 우수한 샘플 효율로 더 적은 보상 평가로 수렴

3. **광범위한 작업 지원**: 단백질 설계(이차 구조 매칭, PD-L1/IFNAR2 결합 설계), 작은 분자 설계, 조절 DNA 설계 등 다양한 생물분자 설계 과제에서 우수한 성능 입증

4. **비미분가능 보상 최적화**: 물리 시뮬레이션이나 과학 지식 기반 보상 등 임의의 비미분가능 보상함수에 대응 가능

## How

![Figure 1](figures/fig1.webp)
*그림 1: VIDD의 알고리즘 구조 및 세 가지 핵심 단계*

**알고리즘 구조:**

- **Roll-in (오프정책 수집)**: 사전훈련된 모델과 이전 미세조정 정책의 혼합분포에서 궤적(trajectory)을 샘플링하여 다양한 탐색 보장. 이를 통해 현재 정책 주변의 좁은 영역으로 제한되지 않음

- **Roll-out (소프트 최적정책 모의)**: 수집된 중간 상태 $x_t$에서 시작하여, 값함수 $\hat{v}_{t→1}$로 가중치를 부여한 보상 기반 소프트 최적정책 $p_{out}$을 구성. 이는 보상을 최적화하면서도 현재 정책과의 거리를 유지하는 KL 제약이 암묵적으로 포함됨

- **Model Update (정방향 KL 최소화)**: 롤아웃으로부터 생성된 소프트 최적정책과 현재 모델 정책 사이의 KL 발산 최소화:
  $$\mathcal{L} = KL(p_{out} || p_ω)$$
  이는 전향적(forward) KL 목적함수로 모드 커버링(mode covering) 행동을 유도하여 다양성 보존

- **값함수 설계**: 확산모델의 특성에 맞춘 값함수 $v_t(x_t) = \log p_{pre}(x_t) + \mathbb{E}[R(x_0)]$를 사용하여 보상과 분포 적합성 간의 균형 조절

## Originality

- **정책 증류 프레임워크**: 확산모델 미세조정에 정책 증류 개념을 적용한 최초의 체계적 시도로, 기존 직접 역전파나 온정책 RL의 한계 극복

- **오프정책 확산 학습**: 확산모델 미세조정에서 오프정책 데이터 수집을 통해 탐색-활용 균형을 개선하고 분포 이동(distribution shift) 완화

- **정방향 KL 기반 목적함수**: 역방향 KL(reverse KL)을 사용하는 기존 PPO 기반 방법들과 달리 정방향 KL을 적용하여 모드 붕괴 문제를 근본적으로 해결

- **확산 특화 값함수**: $\log p_{pre}(x_t)$ 항을 포함하여 사전훈련 분포와의 거리를 명시적으로 고려하는 값함수 설계는 확산모델의 특수성을 반영한 기여

- **과학 응용 맥락**: 생물분자 설계의 실제 요구(비미분가능 보상)에 직접 대응하는 실용적이고 구체적인 해결책 제시

## Limitation & Further Study

- **계산 복잡도**: 값함수 근사, 소프트 최적정책 모의, 모델 업데이트 등 여러 단계를 거치므로 온정책 방법 대비 계산 비용 증가 가능성이 논의되지 않음

- **하이퍼파라미터 민감도**: 롤인 혼합 비율(roll-in mixture ratio), KL 제약 강도(ε), 값함수 근사 정확도 등에 대한 상세한 민감도 분석 부족

- **확장성**: 매우 높은 차원의 설계 공간(예: 큰 단백질, 매우 큰 분자 라이브러리)에 대한 확장성과 효율성 미검증

- **이론적 수렴성**: 알고리즘의 수렴 보장(convergence guarantee)과 최적성 해석(optimality characterization)에 대한 이론적 분석 부족

- **후속 연구 방향**:
  - 값함수 근사 오차의 영향 분석 및 적응적 값함수 학습 기법 개발
  - 대규모 생물분자 설계 문제에 대한 확장 및 병렬화
  - 다중 목표 보상함수 최적화로의 확장
  - 실험적 검증 통한 생물학적 유효성 확인

## Evaluation

- **Novelty**: 4.5/5
  - 오프정책 확산 미세조정과 정책 증류의 결합은 신선하고 기존 방법들과 명확한 차별성 보유. 다만 개별 구성 요소(정책 증류, 값함수 기반 보상 가중치)는 기존 개념의 응용

- **Technical Soundness**: 4/5
  - 알고리즘 설계와 실증적 검증이 견고함. 다만 확산 프로세스의 수학적 엄밀성(특히 값함수 정의와 소프트 최적정책 근사)에 대한 이론적 분석 약화

- **Significance**: 4.5/5
  - 생물분자 설계라는 중요한 응용 영역에서 비미분가능 보상 최적화라는 실질적 문제를 해결. 단백질/분자 설계 커뮤니티의 실질적 영향력 높음. 일반화된 확산 모델 최적화 기법으로서의 영향도 상당

- **Clarity**: 4/5
  - 논문 전체 구조와 주요 메시지가 명확하고 동기 부여가 잘됨. Figure 1이 방법을 직관적으로 설명. 다만 수학적 표기법의 일부 부분(특히 정책 표기)이 다소 중복되고, 값함수 설계 선택의 정당성 설명이 더 상세할 필요

- **Overall**: 4.5/5

**총평**: 이 논문은 생물분자 설계에서 미분불가능한 보상 최적화라는 실질적 도전 과제를 오프정책 학습과 정방향 KL 기반 정책 증류로 우아하게 해결한 강력한 기여다. 단백질·분자 설계 분야에서의 광범위한 실증과 기존 방법 대비 안정성 및 샘플 효율 개선이 논문의 가치를 높인다. 다만 이론적 분석과 대규모 문제에 대한 확장성 검증이 보강되면 더욱 우수한 논문이 될 수 있다.

## Related Papers

- 🔄 다른 접근: [[papers/682_Reward-Guided_Iterative_Refinement_in_Diffusion_Models_at_Te/review]] — 둘 다 확산모델의 보상 기반 미세조정을 다루지만 서로 다른 기법적 접근을 제시한다.
- 🔗 후속 연구: [[papers/269_Derivative-Free_Guidance_in_Continuous_and_Discrete_Diffusio/review]] — 미분불가능한 보상함수 최적화를 연속/이산 확산모델로 확장한다.
- 🔄 다른 접근: [[papers/428_Inference-Time_Alignment_in_Diffusion_Models_with_Reward-Gui/review]] — 생물분자 설계를 위한 확산모델 최적화의 다른 접근법을 제공한다.
- 🏛 기반 연구: [[papers/428_Inference-Time_Alignment_in_Diffusion_Models_with_Reward-Gui/review]] — 확산 모델의 보상 유도 미세조정을 위한 반복 증류가 추론 시간 정렬의 이론적 기반입니다.
- 🔄 다른 접근: [[papers/269_Derivative-Free_Guidance_in_Continuous_and_Discrete_Diffusio/review]] — 확산 모델에서 보상 기반 가이던스의 다른 최적화 접근법을 비교할 수 있다
- 🔗 후속 연구: [[papers/682_Reward-Guided_Iterative_Refinement_in_Diffusion_Models_at_Te/review]] — 반복적 증류 방법이 보상 유도 확산 모델의 테스트 시간 개선 과정을 더욱 효율화할 수 있음
- 🧪 응용 사례: [[papers/282_DMFlow_Disordered_Materials_Generation_by_Flow_Matching/review]] — 확산 모델의 보상 가이드 미세조정을 무질서 재료 생성에 적용
