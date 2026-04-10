---
title: "269_Derivative-Free_Guidance_in_Continuous_and_Discrete_Diffusio"
authors:
  - "Xiner Li"
  - "Yulai Zhao"
  - "Chenyu Wang"
  - "Gabriele Scalia"
  - "Gökçen Eraslan"
date: "2024"
doi: "10.48550/arXiv.2408.08252"
arxiv: ""
score: 4.25
essence: "본 논문은 사전학습된 확산 모델(diffusion model)에서 미분 불가능한 보상 함수를 최적화하면서도 자연스러운 샘플을 생성하는 새로운 추론 시간 기법 SVDD(Soft Value-based Decoding in Diffusion models)를 제안한다. 이 방법은 모델 미세조정 없이 연속 및 이산 확산 모델에 모두 적용 가능하며, 분자 생성 및 DNA/RNA 생성 등 생물정보학적 응용에 특히 유용하다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Reward-guided_Diffusion_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Li et al._2024_Derivative-Free Guidance in Continuous and Discrete Diffusion Models with Soft Value-Based Decoding.pdf"
---

# Derivative-Free Guidance in Continuous and Discrete Diffusion Models with Soft Value-Based Decoding

> **저자**: Xiner Li, Yulai Zhao, Chenyu Wang, Gabriele Scalia, Gökçen Eraslan | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2408.08252](https://doi.org/10.48550/arXiv.2408.08252)

---

## Essence

본 논문은 사전학습된 확산 모델(diffusion model)에서 미분 불가능한 보상 함수를 최적화하면서도 자연스러운 샘플을 생성하는 새로운 추론 시간 기법 SVDD(Soft Value-based Decoding in Diffusion models)를 제안한다. 이 방법은 모델 미세조정 없이 연속 및 이산 확산 모델에 모두 적용 가능하며, 분자 생성 및 DNA/RNA 생성 등 생물정보학적 응용에 특히 유용하다.

## Motivation

- **Known**: 확산 모델은 이미지, 분자, DNA/RNA 등 자연스러운 설계 공간을 잘 포착하지만, 실제 응용에서는 사전학습 모델의 자연스러움을 보존하면서 동시에 특정 보상 함수를 최적화해야 한다.

- **Gap**: 기존 방법들의 한계:
  - **분류기 유도(Classifier guidance)**: 미분 가능한 프록시 모델 필요 → 물리 기반 시뮬레이션(Vina, Rosetta) 등 비미분 피드백 활용 불가
  - **분류기-무료 유도**: 확산 모델의 재미세조정 필요 → 계산 비용 증가
  - **이산 확산 모델**: 표준 분류기 유도를 원칙적으로 적용 불가능

- **Why**: 약물 발견, 단백질 설계 등 과학 영역에서 보상 함수가 종종 비미분이며, 기초 모델의 재학습은 비용이 크다.

- **Approach**: 중간 노이즈 상태(noisy state)가 향후 높은 보상으로 이어지는지 예측하는 소프트 가치 함수(soft value function)를 도입하고, 추론 시간에 다중 샘플 중 가장 높은 가치를 가진 상태를 선택하는 방식으로 접근.

## Achievement

1. **미분 불필요한 설계**: 비미분 보상 피드백(물리 기반 시뮬레이션, 분자 기술자 등)을 직접 활용 가능하며, 추가 학습이 필요 없는 SVDD-PM 변형 제시

2. **통합된 프레임워크**: 연속 공간과 이산 공간의 확산 모델에 원칙적으로 적용 가능한 단일 방법론 제공

3. **광범위한 검증**: 이미지 생성, 분자 생성(도킹 점수, QED, SA 최적화), DNA/RNA 생성(활성도 최적화)에서 효과 입증

## How

### 핵심 기술 원리

- **소프트 가치 함수 정의**: $v(x_{t-1}) := \mathbb{E}[r(x_0)|x_{t-1}]$로 정의하여 중간 상태에서 최종 보상의 기댓값을 예측

- **SVDD-MC (몬테카를로 기반)**:
  - 사전학습 모델에서 M개의 다중 노이즈 상태 생성: $\{x_t^{(m)}\}_{m=1}^M$
  - 각 시간 스텝에서 가치 함수로 평가하여 최고 값을 가진 샘플 선택
  - 가치 함수 학습을 위해 보상 모델 필요

- **SVDD-PM (파라미터 가정 기반)**:
  - 확산 모델의 전진 과정(forward process) 특성 활용하여 시간 t에서 최종 시간 0의 예상 상태를 직접 계산
  - 추가 학습 없이 작동 가능: $\hat{x}_0(x_t;\theta)$를 이용해 직접 보상 계산

### 알고리즘 구조

```
1. 시간 t = T에서 t = 0으로 역방향 진행
2. 각 스텝에서:
   - 사전학습 모델로부터 M개 샘플 생성
   - 가치 함수로 평가 (또는 직접 보상 계산)
   - 최고 값 샘플 선택하여 다음 스텝으로 진행
```

## Originality

- **미분-무료 가이던스**: 기울기 계산 없이 가치 기반 선택을 통해 보상 최적화 달성 — 기존 분류기 유도의 본질적 한계 극복

- **이산 모델에 대한 원칙적 확장**: 연속 공간 가정에서 벗어나 범주형 분포에도 동일하게 적용 가능한 통합 프레임워크

- **무학습 변형(SVDD-PM)**: 확산 모델의 수학적 구조(노이즈 스케줄, x₀ 예측)를 활용하여 추가 학습 단계 완전 제거

- **현실성**: 실제 과학 응용(약물 설계의 물리 시뮬레이터, 단백질 설계의 복잡한 기술자)에서 자주 마주치는 비미분 함수 직접 수용

## Limitation & Further Study

- **계산 비용**: M개 샘플 생성 및 평가로 인한 순차적 계산량 증가 — 최적의 M 값 선택이 문제 종속적

- **가치 함수 품질**: SVDD-MC에서 보상 모델의 학습 품질이 성능을 크게 좌우하며, 분포 외(out-of-distribution) 상태에서의 예측 신뢰성 미상

- **이산 공간 스케일링**: 매우 큰 어휘 크기(large vocabulary)를 가진 이산 확산 모델에서의 실제 적용 가능성 검토 필요

- **자연스러움 보존 정량화**: 보상 최적화 과정에서 원본 데이터 분포로부터의 편차 정도를 정량적으로 측정하는 메커니즘 부족

- **향후 연구**: 
  - 적응적 샘플링(adaptive sampling)으로 M 최적화
  - 가치 함수의 불확실성 정량화 및 신뢰도 평가
  - 매우 높은 차원의 이산 공간에서의 확장성 검증


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.25/5

**총평**: 본 논문은 미분-무료 가이던스라는 실용적이고 새로운 관점으로 확산 모델의 보상 최적화 문제를 해결하며, 특히 비미분 피드백을 활용해야 하는 생물정보학 응용에 큰 기여할 수 있다. 다만 계산 효율성과 이산 공간에서의 확장성 면에서 추가 개선이 필요하고, SVDD-PM의 가정이 실제 환경에서 얼마나 타당한지에 대한 더 깊은 분석이 요구된다.

## Related Papers

- 🔄 다른 접근: [[papers/446_Iterative_Distillation_for_Reward-Guided_Fine-Tuning_of_Diff/review]] — 확산 모델에서 보상 기반 가이던스의 다른 최적화 접근법을 비교할 수 있다
- 🧪 응용 사례: [[papers/304_Efficient_and_Equivariant_Graph_Networks_for_Predicting_Quan/review]] — 미분 불가능한 보상 함수 최적화를 양자 해밀토니안 예측에 적용할 수 있다
- 🔗 후속 연구: [[papers/682_Reward-Guided_Iterative_Refinement_in_Diffusion_Models_at_Te/review]] — 테스트 시간 확산 모델 개선에 미분 자유 보상 최적화 기법을 확장 적용할 수 있다
- 🔄 다른 접근: [[papers/296_Dynamic_Search_for_Inference-Time_Alignment_in_Diffusion_Mod/review]] — 확산 모델의 추론 시간 정렬에서 다른 동적 탐색 vs 보상 가이던스 접근법을 비교할 수 있다
- 🔄 다른 접근: [[papers/428_Inference-Time_Alignment_in_Diffusion_Models_with_Reward-Gui/review]] — 확산 모델 정렬에서 보상 유도 생성과 미분 불가능한 가이던스 접근법을 비교할 수 있습니다.
- 🔗 후속 연구: [[papers/446_Iterative_Distillation_for_Reward-Guided_Fine-Tuning_of_Diff/review]] — 미분불가능한 보상함수 최적화를 연속/이산 확산모델로 확장한다.
- 🧪 응용 사례: [[papers/304_Efficient_and_Equivariant_Graph_Networks_for_Predicting_Quan/review]] — SE(3) 등변 그래프 네트워크를 확산 모델의 분자 생성에 적용할 수 있다
- 🏛 기반 연구: [[papers/296_Dynamic_Search_for_Inference-Time_Alignment_in_Diffusion_Mod/review]] — 미분 없는 유도 방법이 비미분 보상 함수에 대한 확산 모델 최적화의 이론적 기반을 제공함
- 🔗 후속 연구: [[papers/282_DMFlow_Disordered_Materials_Generation_by_Flow_Matching/review]] — 연속 이산 확산의 미분 프리 가이던스에서 무질서 재료로의 확장
