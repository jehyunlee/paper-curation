---
title: "428_Inference-Time_Alignment_in_Diffusion_Models_with_Reward-Gui"
authors:
  - "Masatoshi Uehara"
  - "Yulai Zhao"
  - "Chenyu Wang"
  - "Xiner Li"
  - "Aviv Regev"
date: "2025"
doi: "10.48550/arXiv.2501.09685"
arxiv: ""
score: 4.0
essence: "본 튜토리얼은 사전학습된 확산 모델을 미세조정하지 않으면서 추론 시간(inference time)에 보상 함수(reward function)를 최대화하는 정렬(alignment) 기법들을 통일된 관점에서 리뷰하고, 단백질 설계 같은 과학 분야에서 실제로 유용한 비미분 가능한 보상 피드백을 다루는 방법론들을 포괄적으로 다룬다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Visual_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Uehara et al._2025_Inference-Time Alignment in Diffusion Models with Reward-Guided Generation Tutorial and Review.pdf"
---

# Inference-Time Alignment in Diffusion Models with Reward-Guided Generation: Tutorial and Review

> **저자**: Masatoshi Uehara, Yulai Zhao, Chenyu Wang, Xiner Li, Aviv Regev | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2501.09685](https://doi.org/10.48550/arXiv.2501.09685)

---

## Essence

![Figure 2: 대표적인 추론 시간 알고리즘들의 요약](figures/fig2.webp)
*Figure 2: 최적화 목표 달성을 위한 다양한 추론 시간 기법들 (Best-of-N, 분류기 가이던스, SMC 기반 가이던스, 값 기반 중요도 샘플링)*

본 튜토리얼은 사전학습된 확산 모델을 미세조정하지 않으면서 추론 시간(inference time)에 보상 함수(reward function)를 최대화하는 정렬(alignment) 기법들을 통일된 관점에서 리뷰하고, 단백질 설계 같은 과학 분야에서 실제로 유용한 비미분 가능한 보상 피드백을 다루는 방법론들을 포괄적으로 다룬다.

## Motivation

- **Known**: 확산 모델은 이미지와 단백질 3D 구조 생성 등에서 뛰어난 생성 능력을 입증했으며, 대규모 데이터셋으로 사전학습된 기초 모델(foundation model)들이 존재한다.

- **Gap**: 실제 응용에서는 단순히 자연스러운 샘플 생성을 넘어 안정성, 결합력(affinity), 목표 구조 근접도 등 특정 메트릭을 최대화해야 하는데, 이를 달성하기 위해 전체 모델을 다시 학습하는 것은 계산 비용이 매우 높다.

- **Why**: 추론 시간 기법들은 (1) 미세조정이 필요 없어 구현이 간단하고, (2) 사후학습 방법과 경쟁할 수 있는 성능을 제공하며, (3) 증가된 계산 예산으로 성능 개선이 가능하고, (4) 심지어 미세조정된 모델에도 추가 적용 가능한 이점이 있다.

- **Approach**: 모든 추론 시간 알고리즘들이 공통적으로 목표로 하는 "소프트 최적 정책(soft optimal policy)"을 수식 (1)로 통일되게 표현하고, 이 목표 분포에 도달하는 방식의 차이에 따라 기법들을 분류하며 새로운 알고리즘들도 제시한다.

## Achievement

![Figure 3: 값 기반 빔 서치를 통한 계산 확장](figures/fig3.webp)
*Figure 3: 트리 너비(tree width) 증가에 따른 보상 함수 최적화의 개선 - 단백질 안정성(pLDDT)과 이미지 미적 점수 모두에서 계산 예산 증가에 비례한 성능 향상 관찰*

1. **통일된 이론적 틀**: 순차 몬테카를로(SMC) 기반 가이던스, 값 기반 중요도 샘플링, 분류기 가이던스 등 기존의 다양한 기법들이 모두 동일한 소프트 최적 정책을 근사하려고 시도함을 보여줌으로써, 각 방법의 근본적 연결성 제시

2. **비미분 보상에 대한 포괄적 기법**: 분자 설계에서 흔한 비미분 가능한 물리 시뮬레이션이나 분자 지문(fingerprint) 기반 학습 모델을 다루는 SMC 기반 및 값 기반 중요도 샘플링 방법들을 상세히 리뷰

3. **계산 확장성 입증**: Figure 3에서 보듯이 트리 너비를 증가시키면서 추론 시간 계산을 확장할 때 보상 함수가 선형에 가까운 개선 달성 가능함을 시각화

4. **교차 도메인 통찰**: 언어 모델과 확산 모델의 추론 시간 기법들 간 연결성 논의 및 탐색 알고리즘(search algorithm) 기반 접근법 추가

## How

![Figure 1: 추론 시간 기법의 목표](figures/fig1.webp)
*Figure 1: 미세조정 없이 사전학습 생성 모델과 보상 모델을 통합하여 기능성 높은 자연스러운 설계 생성*

**핵심 수식적 표현**:
- 목표 분포: $p_{\text{pre}}(·) \times \exp(r(·)/\alpha) / C$
  - 전항(pre-trained distribution): 자연스러움(naturalness) 보장
  - 후항(reward term): 높은 기능성 보장

- 각 시간 단계 최적 정책: $p_t^* (·|x_t) = p_{\text{pre}}^t(·|x_t) \times \exp(v_t(·)/\alpha)$
  - $p_{\text{pre}}^t(·|x_t)$: 사전학습된 정책
  - $v_t(·)$: 중간 상태에서 종말 보상 예측하는 룩어헤드 함수(look-ahead function)

**주요 기법들의 구분 기준**:
- **Best-of-N 샘플링**: 단순하지만 보상 최적화가 어려울 때 비효율적
- **분류기 가이던스**: 미분 가능한 값 함수 모델 필요, 기울기(gradient) 정보 활용
- **SMC 기반 가이던스**: 그래디언트 미사용, 중간 상태의 순차적 선별, 비미분 보상에 적합
- **값 기반 중요도 샘플링 (빔 서치)**: 값 함수의 구체적 미분 불필요, 병렬 계산 용이

**선택 고려사항**:
1. 계산/메모리 효율성과 병렬화 가능성
2. 최적화 목표 (분류 vs. 회귀형 보상)
3. 보상 피드백의 미분 가능 여부

## Originality

- **통합 이론 틀**: 산재된 추론 시간 기법들을 단일한 소프트 최적 정책 프레임워크로 체계화한 첫 포괄적 시도

- **비미분 보상 중심**: 분자 설계 같은 과학 도메인에서 실제로 마주치는 비미분 보상을 전면에 다룬 드문 리뷰 (기존 대부분은 컴퓨터 비전/NLP의 미분 가능 보상에 집중)

- **탐색 알고리즘 재조명**: 트리 서치, 빔 서치 기반 추론 시간 기법들이 이전 연구에서 주목받지 못했음을 지적하고 체계적으로 정리

- **사후학습과의 상호작용**: 단순한 추론 시간 기법 리뷰를 넘어 데이터 증강, 정책 증류(policy distillation), 미세조정된 모델에 대한 추가 적용 등 사후학습과의 연계 논의

- **단백질 설계 실제 구현**: 논문의 개념들을 단백질 설계에 직접 적용한 코드 공개 (AlignInversePro)

## Limitation & Further Study

- **불완전한 이론 분석**: 각 기법이 소프트 최적 정책을 얼마나 잘 근사하는지에 대한 정량적 수렴 분석(convergence analysis)이나 근사 오차(approximation error) 경계가 상세히 제시되지 않음

- **값 함수 추정의 정확성 의존**: 비미분 방법들도 결국 $v_t(·)$를 정확히 추정해야 하는데, 이 추정 오류가 최종 성능에 미치는 영향에 대한 체계적 분석 부족

- **계산 비용 분석 미흡**: Figure 3은 성능 향상을 보이지만, 실제 벽시계 시간(wall-clock time), 메모리 사용량, 병렬화 효율 간의 정량적 trade-off 분석이 제한적

- **도메인별 적용 한계**: 대부분의 논의가 단백질과 이미지에 집중되어 있으며, 다른 과학 도메인(약물 발견, 재료 과학 등)으로의 일반화 가능성 미검증

- **보상 함수 설계의 어려움**: 튜토리얼이 추론 시간 기법 최적화에 집중하면서, 실제 병목인 "좋은 보상 함수 설계"에 대한 논의는 상대적으로 경미

- **미래 연구 방향**:
  - 소프트 최적 정책 근사 품질의 이론적 보증 제공
  - 값 함수 추정 오류와 최종 성능 간 상관관계 정량화
  - 더 복잡한 제약 조건(constraint)이나 다중 목표(multi-objective) 최적화 문제 확장
  - 실시간 적응형 보상(dynamic reward) 업데이트 메커니즘 개발

## Evaluation

- **Novelty**: 4/5
  - 산재된 기법들의 통일 틀은 신선하나, 개별 기법의 새로움은 제한적 (기존 논문들의 재정리)
  - 비미분 보상 중심 관점과 탐색 알고리즘 재조명은 의미 있음

- **Technical Soundness**: 4/5
  - 수식적 표현과 개념은 명확하고 일관성 있음
  - 다만 수렴성, 근사 오차, 실증적 비교 분석의 엄밀성 부족

- **Significance**: 4/5
  - 생물학, 화학 등 과학 도메인에서 즉시 활용 가능한 실용적 가치 높음
  - 사전학습 모델의 효율적 활용이라는 시의적절한 주제
  - 다만 이론적 새로움이나 벤치마크 개선의 폭은 중간 수준

- **Clarity**: 4.5/5
  - Figure 1-4와 정리된 분류체계로 복잡한 주제를 잘 구조화
  - 동기, 기법, 고려사항을 명확히 구분하여 제시
  - 다만 일부 수식 표기(예: normalizing constant C의 정의)가 간략함

- **Overall**: 4/5

**총평**: 본 튜토리얼은 확산 모델의 추론 시간 정렬 기법들을 처음으로 체계적으로 통합하는 시도로서, 특히 비미분 보상이 실제인 과학 도메인의 관점에서 현실적 가치가 높으며, 제시된 프레임워크는 향후 연구의 이론적 기초가 될 수 있다. 다만 각 기법의 근사 품질, 수렴성, 값 함수 오차의 영향 등에 대한 정량적 이론 분석이 보강된다면 더욱 강력한 참고 자료가 될 것이다.

## Related Papers

- 🔄 다른 접근: [[papers/269_Derivative-Free_Guidance_in_Continuous_and_Discrete_Diffusio/review]] — 확산 모델 정렬에서 보상 유도 생성과 미분 불가능한 가이던스 접근법을 비교할 수 있습니다.
- 🔗 후속 연구: [[papers/682_Reward-Guided_Iterative_Refinement_in_Diffusion_Models_at_Te/review]] — 테스트 시간 보상 유도 반복 개선이 추론 시간 확산 모델 정렬로 확장될 수 있습니다.
- 🏛 기반 연구: [[papers/446_Iterative_Distillation_for_Reward-Guided_Fine-Tuning_of_Diff/review]] — 확산 모델의 보상 유도 미세조정을 위한 반복 증류가 추론 시간 정렬의 이론적 기반입니다.
- 🔄 다른 접근: [[papers/446_Iterative_Distillation_for_Reward-Guided_Fine-Tuning_of_Diff/review]] — 생물분자 설계를 위한 확산모델 최적화의 다른 접근법을 제공한다.
- 🏛 기반 연구: [[papers/682_Reward-Guided_Iterative_Refinement_in_Diffusion_Models_at_Te/review]] — 추론 시간 정렬의 보상 유도 방법론이 반복적 개선 프레임워크의 핵심 이론적 기반을 제공함
