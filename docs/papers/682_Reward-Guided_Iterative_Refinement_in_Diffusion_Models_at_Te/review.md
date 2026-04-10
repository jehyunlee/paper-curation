---
title: "682_Reward-Guided_Iterative_Refinement_in_Diffusion_Models_at_Te"
authors:
  - "Masatoshi Uehara"
  - "Xingyu Su"
  - "Yulai Zhao"
  - "Xiner Li"
  - "Aviv Regev"
date: "2025"
doi: "10.48550/arXiv.2502.14944"
arxiv: ""
score: 4.2
essence: "본 논문은 확산 모델(Diffusion Models)에서 테스트 타임 보상 최적화를 위한 반복적 개선 프레임워크를 제안한다. 기존의 단일 샷(single-shot) 방식과 달리, 부분 노이징과 보상 유도 디노이징의 두 단계를 반복하여 점진적으로 설계(design)를 개선할 수 있다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Reward-guided_Diffusion_Models"
  - "topic/ai4s"
---

# Reward-Guided Iterative Refinement in Diffusion Models at Test-Time with Applications to Protein and DNA Design

> **저자**: Masatoshi Uehara, Xingyu Su, Yulai Zhao, Xiner Li, Aviv Regev | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2502.14944](https://doi.org/10.48550/arXiv.2502.14944)

---

## Essence

![Figure 1](figures/fig1.webp) *그림 1: 제안된 프레임워크는 반복적 과정을 따르며, 각 반복에서 샘플에 노이즈를 주입한 후 보상을 최적화하면서 디노이징하는 과정*

본 논문은 확산 모델(Diffusion Models)에서 테스트 타임 보상 최적화를 위한 반복적 개선 프레임워크를 제안한다. 기존의 단일 샷(single-shot) 방식과 달리, 부분 노이징과 보상 유도 디노이징의 두 단계를 반복하여 점진적으로 설계(design)를 개선할 수 있다.

## Motivation

- **Known**: 확산 모델은 텍스트-이미지, 단백질 서열 생성 등 다양한 분야에서 성공적이며, 분류기 유도(classifier guidance)나 도함수-프리(derivative-free) 방법들이 보상 유도 생성(reward-guided generation)에 활용되고 있다.

- **Gap**: 기존 방법들은 완전 노이징 상태에서 디노이징 상태로의 단일 패스에만 의존하며, 두 가지 핵심 문제가 존재한다: (1) 보상 유도 디노이징 중 발생한 오류를 수정할 메커니즘 부재, (2) 특히 마스크 확산 모델에서 한번 변경된 토큰은 끝까지 고정되는 문제, (3) 하드 제약조건(hard constraints) 처리의 어려움.

- **Why**: 생물학적 서열 설계(단백질, DNA)에서는 구조적 안정성, 결합 친화력, 세포타입 특이성 등 복잡한 보상함수 최적화가 필요하며, 추론 시간 계산량을 증가시켜 더 나은 설계를 얻을 수 있을 것으로 예상된다.

- **Approach**: 테스트 타임에 임의의 양의 계산을 활용하여 설계를 지속적으로 개선하는 반복적 개선 알고리즘(noising + reward-guided denoising) 제안.

## Achievement

![Figure 2](figures/fig2.webp) *그림 2: 기존 보상 유도 알고리즘은 소프트 최적 정책 {p⋆_t}로부터 순차적 샘플링으로 볼 수 있으며, 알고리즘의 차이는 p⋆_t 근사 방식에 있다*

1. **이론적 기여**: 제안된 알고리즘이 exp(r(x))p_pre(·) 분포로부터 샘플링함을 수학적으로 증명하여, 생성된 설계의 자연스러움(naturalness)과 보상 최적화 간 균형을 이론적으로 보장.

2. **방법론 혁신**: 단순한 반복적 개선을 통해 마스크 확산 모델의 근본적 한계(한번 변경된 토큰 고정)를 극복하고, 하드 제약조건을 포함하는 복잡한 보상함수 최적화 가능.

3. **실험적 우수성**: 단백질 구조 설계(target RMSD 최소화)와 세포타입 특이성 DNA 설계에서 기존 방법들을 능가하는 성능 달성.

## How

![Figure 3](figures/fig3.webp) *그림 3: RERD 알고리즘 요약 - 반복적으로 부분 노이징과 보상 유도 디노이징 수행*

**핵심 알고리즘 구조:**

- **반복적 단계**: 각 반복 k에서 (1) 현재 샘플 x^(k)에 부분 노이즈 주입 → 중간상태 생성, (2) 보상 유도 디노이징을 통해 x^(k+1) 획득
  
- **소프트 최적 정책 근사**: 식 (2)의 소프트 가치함수 v_t(x_t)를 근사하기 위해 재구성된 x_0 예측값 x̂_0(x_t)의 보상 r(x̂_0(x_t)) 활용

- **대규모 행동공간 처리**: 분류기 유도(연속) 또는 중요도 샘플링(이산)으로 p⋆_t 근사

- **하드 제약조건 처리**: 초기 시드 시퀀스를 가능 영역 C 내에서 선택하여 제약조건 자동 만족

- **진화 알고리즘과의 연결**: 보상 기반 선택과 부분 변이(노이징)의 조합이 유전 알고리즘(genetic algorithms)과 유사한 구조

## Originality

- **첫 확산 모델 반복 개선**: 언어모델의 반복 개선(BERT-style refinement) 개념을 확산 모델에 처음 적용하여 테스트 타임 보상 최적화의 새로운 패러다임 제시.

- **오류 수정 메커니즘**: 기존 단일 패스 방식의 결정 불가역성 문제를 부분 노이징을 통한 재샘플링으로 해결 - 특히 마스크 확산 모델에서 매우 중요.

- **제약조건 통합 설계**: 하드 제약조건을 reward function으로 단순 설정하는 대신, 초기 조건 선택을 통해 실질적으로 달성하는 실용적 방안 제시.

- **통합 이론 프레임워크**: KL 정규화된 보상 최적화 목표(식 1)와 확산 모델의 수학적 연결을 명확히 하고, 제안 알고리즘의 최적성 보장.

## Limitation & Further Study

- **계산비용 증가**: 반복적 개선으로 인한 추론 시간 증가는 실제 응용에서 병목이 될 수 있으며, 효율성 개선 방안 필요.

- **부분 노이징 스케줄 미최적화**: 각 반복에서 주입할 노이즈 수준(noise level)을 선택하는 전략이 휴리스틱으로 보이며, 이론적 최적화 부재.

- **실제 검증 제한**: 단백질 설계의 경우 구조 예측(ESMFold)만 사용하고 실제 생화학적 검증 부재, DNA 설계도 세포 실험 검증 미흡.

- **보상함수 품질 의존성**: 알고리즘의 성능이 보상함수의 정확성에 크게 의존하지만, 부정확한 보상함수에 대한 견고성(robustness) 분석 부족.

- **후속 연구**: (1) 적응형 노이징 스케줄 학습, (2) 불완전한 보상함수 환경에서의 성능 특성화, (3) 다른 생성 모델(flow-based, autoregressive)로의 확장, (4) 실제 생물학적 검증 수행.

## Evaluation

- **Novelty**: 4.5/5
  - 확산 모델에 반복적 개선 도입은 신선하나, 개별 요소(반복, 보상 유도)는 기존. 마스크 확산에서의 오류 수정 메커니즘이 특히 참신.

- **Technical Soundness**: 4/5
  - 이론적 도출(exp(r(x))p_pre 분포 증명)은 견고하나, 가치함수 근사의 정확성 가정이 강하고 부분 노이징 스케줄 선택에 대한 이론적 정당성 부족.

- **Significance**: 4.5/5
  - 단백질/DNA 설계라는 고영향 응용과 실제 어려운 제약조건 처리 가능이 중요하나, 계산비용 증가로 인한 실용성이 제한적. 기존 방법 대비 일관된 성능 향상 입증.

- **Clarity**: 4/5
  - 논문 구조와 알고리즘 설명은 명확하나, 마스크 확산 모델의 기술적 세부사항이 복잡하고 Figure 3의 가시성 개선 필요. 하드 제약조건 처리 메커니즘 설명 보충 필요.

- **Overall**: 4.2/5
  - **총평**: 확산 모델의 테스트 타임 최적화에 혁신적인 반복 개선 접근을 제시하고, 특히 마스크 확산의 토큰 고정 문제 해결과 하드 제약조건 처리는 실질적 기여다. 단백질/DNA 설계에서 일관된 성능 향상을 보이나, 계산 효율성 분석 부재와 실제 생물학적 검증 부족이 한계. 학술적 우수성은 높으나 실무 적용을 위해서는 효율화와 검증이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/296_Dynamic_Search_for_Inference-Time_Alignment_in_Diffusion_Mod/review]] — 둘 다 확산 모델의 추론 시간 보상 최적화를 다루지만 반복적 개선과 동적 탐색이라는 서로 다른 전략을 사용함
- 🔗 후속 연구: [[papers/446_Iterative_Distillation_for_Reward-Guided_Fine-Tuning_of_Diff/review]] — 반복적 증류 방법이 보상 유도 확산 모델의 테스트 시간 개선 과정을 더욱 효율화할 수 있음
- 🏛 기반 연구: [[papers/428_Inference-Time_Alignment_in_Diffusion_Models_with_Reward-Gui/review]] — 추론 시간 정렬의 보상 유도 방법론이 반복적 개선 프레임워크의 핵심 이론적 기반을 제공함
- 🔗 후속 연구: [[papers/428_Inference-Time_Alignment_in_Diffusion_Models_with_Reward-Gui/review]] — 테스트 시간 보상 유도 반복 개선이 추론 시간 확산 모델 정렬로 확장될 수 있습니다.
- 🔄 다른 접근: [[papers/446_Iterative_Distillation_for_Reward-Guided_Fine-Tuning_of_Diff/review]] — 둘 다 확산모델의 보상 기반 미세조정을 다루지만 서로 다른 기법적 접근을 제시한다.
- 🔗 후속 연구: [[papers/269_Derivative-Free_Guidance_in_Continuous_and_Discrete_Diffusio/review]] — 테스트 시간 확산 모델 개선에 미분 자유 보상 최적화 기법을 확장 적용할 수 있다
- 🔄 다른 접근: [[papers/296_Dynamic_Search_for_Inference-Time_Alignment_in_Diffusion_Mod/review]] — 둘 다 확산 모델의 추론 시간 정렬을 다루지만 동적 탐색과 반복적 개선이라는 서로 다른 최적화 전략을 사용함
- 🏛 기반 연구: [[papers/337_Figgen_Text_to_scientific_figure_generation/review]] — 확산 모델에서 보상 기반 반복적 정제 방법이 FigGen의 과학 도형 생성 정확도 개선에 기반을 제공한다.
