---
title: "296_Dynamic_Search_for_Inference-Time_Alignment_in_Diffusion_Mod"
authors:
  - "Xiner Li"
  - "Masatoshi Uehara"
  - "Xingyu Su"
  - "Gabriele Scalia"
  - "Tommaso Biancalani"
date: "2025"
doi: "10.48550/arXiv.2503.02039"
arxiv: ""
score: 4.1
essence: "확산 모델(diffusion models)의 추론 시간 정렬(inference-time alignment) 문제를 트리 탐색 문제로 재정의하고, 동적 빔 폭 조정을 통해 비미분 보상 함수(non-differentiable reward functions)에 대한 효율적인 최적화를 달성하는 새로운 방법을 제시한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Reward-guided_Diffusion_Models"
  - "topic/ai4s"
---

# Dynamic Search for Inference-Time Alignment in Diffusion Models

> **저자**: Xiner Li, Masatoshi Uehara, Xingyu Su, Gabriele Scalia, Tommaso Biancalani | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2503.02039](https://doi.org/10.48550/arXiv.2503.02039)

---

## Essence

확산 모델(diffusion models)의 추론 시간 정렬(inference-time alignment) 문제를 트리 탐색 문제로 재정의하고, 동적 빔 폭 조정을 통해 비미분 보상 함수(non-differentiable reward functions)에 대한 효율적인 최적화를 달성하는 새로운 방법을 제시한다.

## Motivation

- **Known**: 확산 모델은 다양한 도메인에서 강력한 생성 능력을 보유하고 있으나, 보상 함수와의 정렬이 어려운 문제가 존재. 기존의 분류기 유도(classifier guidance)는 미분 가능한 보상 함수에 의존하는 한계 있음.

- **Gap**: 실제 과학 응용 분야(약물 설계, 단백질 구조 예측 등)에서 AutoDock Vina, AlphaFold3, DSSP 등의 보상 함수는 물리 시뮬레이션, 룩업 테이블 기반으로 비미분이거나 블랙박스 형태. 기존 그래디언트 프리 유도 방법들도 최적의 정렬을 보장하지 못함.

- **Why**: 확산 모델의 디노이징 과정(denoising process)이 트리 구조를 형성한다는 통찰을 기반으로, 검색 알고리즘을 통해 더 효율적인 정렬이 가능할 것으로 예상.

- **Approach**: 사전학습된 확산 모델의 디노이징 과정을 트리로 형식화하고, 동적 빔 탐색(dynamic beam search)을 적용하여 빔 폭과 트리 너비를 시간 단계에 따라 동적으로 조정.

## Achievement

![Figure 1: Inference-time alignment of diffusion model as a search problem](figures/fig1.webp)
*Figure 1: 확산 모델의 추론 시간 정렬을 탐색 문제로 프레임화. 녹색 원은 트리 노드(후보 샘플)를 나타내고, 어두운 노드는 높은 잠재 보상을 표시. 파란 화살표는 동적으로 선택된 고보상 궤적*

1. **탐색 프레임워크 제안**: 확산 모델의 디노이징 프로세스를 트리 구조로 형식화하여, 보상 최적화를 체계적인 탐색 문제로 재구성. 이는 기존의 ad-hoc한 유도 방식과 달리 일관된 이론적 기초 제공.

2. **동적 빔 탐색(DSearch) 알고리즘**: 고정 너비 빔 탐색의 비효율성을 해결하기 위해, 시간 단계별로 빔 폭 b(t)와 트리 너비 w(t)를 동적으로 조정. 약한 빔의 계산 자원을 다른 빔으로 재할당하여 효율성 극대화(w(t)·b(t) 고정).

3. **다중 도메인 검증**: 생물학적 수열 설계(biological sequence design), 분자 최적화(molecular optimization), 이미지 생성 등 다양한 도메인에서 기존 방법 대비 우수한 보상 최적화 성과 입증.

## How

![Figure 2: Illustration of DSearch with dynamic width adjustment](figures/fig2.webp)
*Figure 2: DSearch의 트리 너비 확장과 빔 폭 동적 조정. 약한 빔의 자원을 다른 빔으로 재할당하면서 w(t)b(t) 유지*

**트리 정의 및 너비 제한**:
- 나이브 접근의 O(|X|^T) 복잡도를 해결하기 위해 사전학습된 정책으로부터 샘플링하여 트리 너비 w(t) 제한
- w(t)=1일 경우 best-of-N 샘플링으로 축소되는 일반적 형태 유지

**휴리스틱 함수(Heuristic Function)**:
- 중간 노드의 가치를 평가하기 위해 추정된 가치 함수(estimated value function) 도입
- 기존의 단순 근사 ν̂_t(x_t) := r(x̂_0(x_t))를 개선하는 더 정확한 접근법 제시

**룩어헤드 휴리스틱(Lookahead Heuristic)**:
- Algorithm 1에서 K 스텝 선점 탐색을 통해 소프트 가치 함수의 근사 정확도 향상
- 소수의 추가 시뮬레이션으로 더 신뢰할 만한 중간 노드 평가 가능

**노이즈 레벨 기반 동적 스케줄링**:
- 노이즈 레벨에 따라 적응적으로 트리 확장 일정 조정
- 초기 단계(높은 노이즈)에서 넓은 탐색, 후기 단계(낮은 노이즈)에서 선택적 탐색

## Originality

- **탐색 프레임워크의 혁신**: 확산 모델의 추론 시간 정렬을 처음으로 체계적인 트리 탐색 문제로 정의. 이는 기존의 기울기 기반 또는 휴리스틱한 유도 방식과 근본적으로 다른 접근.

- **동적 빔 폭 조정**: 고정 빔 탐색의 비효율성을 인식하고, 시간 단계와 노이즈 레벨에 따라 자원을 동적으로 재할당하는 새로운 전략 제시. 이는 단순하지만 효과적인 개선.

- **향상된 휴리스틱 함수**: 기존의 단순한 x̂_0 기반 근사를 넘어, 룩어헤드 탐색을 통한 더 정확한 중간 노드 가치 추정 방법 개발.

- **비미분 보상 함수 지원**: 그래디언트가 필요 없는 완전한 그래디언트 프리 프레임워크로, 실제 과학 응용의 복잡한 블랙박스 보상 함수에 직접 적용 가능.

## Limitation & Further Study

**한계**:
- 트리 너비 w(t)와 빔 폭 b(t)의 설정이 휴리스틱하며, 최적값 선택에 대한 이론적 지침이 부족. 다양한 도메인에서의 하이퍼파라미터 민감도 분석 필요.
- 룩어헤드 스텝 K의 증가에 따른 계산 비용 증가로 인한 트레이드오프 미분석. 실제 적용 시 계산 예산(computational budget) 제약에서의 최적 K 선택 방법 미제시.
- 샘플 다양성(diversity)과 자연스러움(naturalness) 사이의 균형에 대한 이론적 분석 부족. 온도 파라미터 α의 설정과 성과 간의 정량적 관계 미제시.

**후속 연구**:
- 동적 빔 폭 조정의 최적성에 대한 이론적 분석 (예: regret bounds 도출)
- 다양한 도메인/모델에 대한 자동 하이퍼파라미터 선택 전략 개발
- 대규모 생성 모델(예: 텍스트 생성, 동영상 생성)으로의 확장 및 확장성 검증
- 여러 보상 함수의 다목적 최적화(multi-objective optimization)로의 확대

## Evaluation

| 항목 | 점수 | 근거 |
|------|------|------|
| **Novelty** | 4.2/5 | 트리 탐색 프레임워크는 신선하고, 동적 빔 폭 조정도 창의적. 다만 개별 기법들(빔 탐색, 휴리스틱 함수)은 기존 문헌의 조합으로 보일 수 있음. |
| **Technical Soundness** | 4.0/5 | 수학적 유도는 명확하며, 소프트 가치 함수의 근사 논리는 타당. 다만 근사 오차 한계(approximation error bounds)에 대한 엄밀한 분석 부족. |
| **Significance** | 4.1/5 | 비미분 보상 함수에 대한 실용적 해결책 제시로 과학 응용 분야의 실제 임팩트 높음. 그러나 이론적 진전이나 근본적 혁신성은 중간 수준. |
| **Clarity** | 3.9/5 | 전반적 구성은 논리적이나, 동적 스케줄링의 정확한 메커니즘과 알고리즘 구현 세부사항이 부분적으로 모호. Figure 2의 설명이 더 상세할 필요. |
| **Overall** | 4.1/5 | 실무적 가치가 높고 여러 도메인에서 경험적 검증이 우수한 견고한 논문. 이론적 깊이나 독창성은 최고 수준은 아니나, 비미분 보상 함수 정렬이라는 중요한 문제에 체계적이고 효과적인 해법 제시. |

**총평**: DSearch는 확산 모델의 추론 시간 정렬 문제를 체계적인 탐색으로 재해석한 실용적이고 견고한 방법론으로, 특히 비미분 보상 함수가 많은 과학 분야에서 높은 적용 가치를 가진다. 다만 동적 조정 메커니즘의 이론적 정당화와 최적성 분석이 보강되면 더욱 강력한 기여가 될 수 있을 것으로 판단된다.

## Related Papers

- 🔄 다른 접근: [[papers/682_Reward-Guided_Iterative_Refinement_in_Diffusion_Models_at_Te/review]] — 둘 다 확산 모델의 추론 시간 정렬을 다루지만 동적 탐색과 반복적 개선이라는 서로 다른 최적화 전략을 사용함
- 🔗 후속 연구: [[papers/740_Search-R1_Training_LLMs_to_Reason_and_Leverage_Search_Engine/review]] — Search-R1의 검색 기반 추론이 확산 모델의 동적 탐색 과정에서 더 효과적인 빔 폭 조정을 가능하게 함
- 🏛 기반 연구: [[papers/269_Derivative-Free_Guidance_in_Continuous_and_Discrete_Diffusio/review]] — 미분 없는 유도 방법이 비미분 보상 함수에 대한 확산 모델 최적화의 이론적 기반을 제공함
- 🔄 다른 접근: [[papers/269_Derivative-Free_Guidance_in_Continuous_and_Discrete_Diffusio/review]] — 확산 모델의 추론 시간 정렬에서 다른 동적 탐색 vs 보상 가이던스 접근법을 비교할 수 있다
- 🔄 다른 접근: [[papers/682_Reward-Guided_Iterative_Refinement_in_Diffusion_Models_at_Te/review]] — 둘 다 확산 모델의 추론 시간 보상 최적화를 다루지만 반복적 개선과 동적 탐색이라는 서로 다른 전략을 사용함
- 🔗 후속 연구: [[papers/337_Figgen_Text_to_scientific_figure_generation/review]] — 확산 모델에서 추론 시점 정렬을 위한 동적 검색 기법이 FigGen의 과학 도형 생성 품질 향상에 적용될 수 있다.
