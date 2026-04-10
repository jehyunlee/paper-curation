---
title: "482_Lean-star_Learning_to_interleave_thinking_and_proving"
authors:
  - "H. Lin"
  - "Zhiqing Sun"
  - "Sean Welleck"
  - "Yiming Yang"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "언어 모델이 형식 수학 증명을 수행할 때, 인간의 사고 과정을 나타내는 자연언어 생각(informal thought)을 각 증명 단계 전에 생성하도록 학습시켜 정리 증명 능력을 향상시키는 프레임워크를 제시한다. 이를 통해 형식 증명에 내재된 정보만으로는 부족한 추론 과정을 보완한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Formal_Theorem_Proving"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Lin et al._2024_Lean-star Learning to interleave thinking and proving.pdf"
---

# Lean-star: Learning to interleave thinking and proving

> **저자**: H. Lin, Zhiqing Sun, Sean Welleck, Yiming Yang | **날짜**: 2024 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: 사고(thought) 유무에 따른 한 증명 단계에서의 전술 예측 비교*

언어 모델이 형식 수학 증명을 수행할 때, 인간의 사고 과정을 나타내는 자연언어 생각(informal thought)을 각 증명 단계 전에 생성하도록 학습시켜 정리 증명 능력을 향상시키는 프레임워크를 제시한다. 이를 통해 형식 증명에 내재된 정보만으로는 부족한 추론 과정을 보완한다.

## Motivation

- **Known**: 기존 언어 모델 기반 정리 증명(theorem proving) 접근법은 형식 증명 데이터(formal proof code)의 (증명 상태, 다음 전술) 쌍으로만 학습되어 왔음. 이는 GPT-f 프레임워크의 표준 방식을 따름.

- **Gap**: 형식 증명 코드에는 인간이 증명 과정에서 거치는 중간 사고 과정(intermediate reasoning)이 명시적으로 나타나지 않음. Chain-of-Thought와 같은 자연언어 추론의 이점이 formal mathematics에서 활용되지 못함.

- **Why**: 많은 선행 연구에서 수학 문제 해결, 과학 추론, 코드 생성 등에서 단계별 추론(step-by-step rationale)이 성능 향상에 효과적임을 보였음. 그러나 형식 수학에서는 자연언어 추론 데이터의 부족과 수동 주석의 비실용성이 이를 적용하기 어렵게 만듦.

- **Approach**: GPT-4 같은 오라클 모델(oracle model)을 이용하여 정답 전술(ground-truth tactic)을 조건으로 하는 "역방향 생성(retrospective rationale generation)"을 통해 50,000개의 자동 주석 데이터를 생성하고, 이를 기반으로 생각-강화 전술 예측 모델을 학습한 후 전문가 반복(expert iteration)으로 추가 최적화.

## Achievement

![Figure 3](figures/fig3.webp)
*그림 3: Lean-STaR 전체 파이프라인 - (1) GPT-4로 CoT 데이터셋 생성 (2) SFT 모델을 CoT로 미세 조정하여 Lean-CoT 획득 (3) 전문가 반복으로 STaR 데이터셋 생성 및 반복 미세 조정*

1. **성능 향상**: InternLM2-7b 기반 모델에서 43.4% → 46.3% (Pass@64)의 유의미한 성능 개선 달성. 더 강력한 InternLM2-7b-plus 모델 사용 시 45.4% (Pass@32) 달성으로 기존 최고 성능 초과.

2. **최초 생각-강화 데이터셋**: 정리 증명 분야에서 처음으로 (상태, 생각, 전술) 삼중 쌍 형태의 학습 데이터셋 구축. 약 50,000개의 Mathlib 기반 데이터와 전문가 반복을 통한 추가 50,000개 합성 데이터로 총 100,000개 규모.

## How

![Figure 2](figures/fig2.webp)
*그림 2: Lean-STaR이 생성한 증명과 생각의 예시 - 생각에 계산 오류가 있어도(빨간색) Lean의 nlinarith 전술이 실제 계산을 수행하므로 증명의 정확성에 영향 없음*

- **역방향 생각 생성(Retrospective Rationale Generation)**: 형식 증명 데이터셋에서 (상태 s_i, 전술 a_i) 쌍을 추출하고, 정답 전술을 조건으로 하여 GPT-4에 그 전술에 도달한 이유를 설명하는 자연언어 생각 t_i를 생성하도록 요청. 이는 모델이 사후(hindsight) 생각을 방지하고 실제 추론 과정을 반영하도록 설계됨.

- **생각-강화 전술 예측 모델(Thought-augmented Tactic Prediction)**: 기존의 π(a|s) 대신 분해된 조건부 확률 π(a|s) = Σ_t π(a|t,s)π(t|s)을 사용하여 상태에서 생각을 먼저 생성한 후 전술을 예측하는 구조로 학습.

- **Supervised Fine-tuning (SFT) 단계**: Lean-CoT 모델을 생각-강화 데이터셋에 대해 미세 조정.

- **전문가 반복(Expert Iteration)**: (1) 현재 모델으로 증명 시도 샘플링, (2) Lean 검증기로 정확성 확인, (3) 성공한 증명만으로 모델 재학습. 다단계 성공률(multi-step success rate)을 보상으로 사용하여 2회 반복 수행.

- **추론 시 구조**: 생각과 전술을 순차적으로 생성. 생각은 다음 전술 선택을 안내하는 중간 표현 역할 수행.

## Originality

- **최초성**: 형식 정리 증명에서 자연언어 chain-of-thought를 체계적으로 통합한 첫 연구. 기존 Draft-Sketch-Prove 등은 전체 비형식 증명 생성에 초점을 두었으나, 본 연구는 단계별 생각 생성에 집중.

- **역방향 생성 기법**: 형식 시스템의 정확성 신호를 활용한 창의적 해결책. 정답 전술을 알고 있을 때 그에 맞는 생각을 생성하는 방식으로 데이터 부족 문제를 우회.

- **프레임워크 결합**: Self-Taught Reasoner (STaR)와 전문가 반복을 형식 증명 영역에 적용하며, 생각-전술 분해 구조의 도입으로 새로운 차원의 부트스트래핑 가능성 제시.

- **신경-기호 시스템의 강점 부각**: Figure 2 예제에서 보듯이, 생각에 계산 오류가 있어도 Lean의 기호적 전술이 검증하는 방식으로, 신경망의 유연성과 형식 증명의 엄밀성을 자연스럽게 결합.

## Limitation & Further Study

- **한계**:
  - 오라클 모델(GPT-4) 의존성: 생각 생성의 품질이 GPT-4의 능력에 좌우되며, 비용 문제가 있을 수 있음. 
  - 데이터 규모 제한: 약 50,000개 Mathlib 데이터는 상대적으로 제한적이며, 더 큰 규모의 형식 수학 라이브러리 부재.
  - 평가 제한: miniF2F-test만 사용되었으며, 다양한 어려움 수준과 영역의 정리에 대한 평가 부족.
  - 모델 크기: 7B 모델의 상대적 소규모로 인한 성능 천장이 존재할 가능성.

- **후속 연구**:
  - 더 강력한 오픈소스 모델로 오라클 모델 대체 가능성 탐색
  - 비형식 수학(informal mathematics)으로부터 생각 자동 추출 방법 개발
  - 생각의 품질과 증명 성공률 간의 인과관계 상세 분석
  - 다양한 형식 증명 시스템(Isabelle, Coq)으로의 확장 검토
  - 인간-기계 협업 환경에서의 활용 가능성 연구

## Evaluation

- **Novelty (독창성)**: 4/5
  - 형식 증명에 생각 통합이라는 명확한 신규 아이디어
  - 역방향 생성 기법이 창의적이나, STaR 프레임워크 자체는 기존 아이디어의 응용

- **Technical Soundness (기술 타당성)**: 4/5
  - MDP 정식화와 확률적 분해가 수학적으로 타당함
  - 실험 설계가 합리적이고 재현 가능해 보임
  - 다만, 생각 품질 평가의 객관적 메트릭이 부재

- **Significance (중요성)**: 4/5
  - 형식 수학과 자연언어 추론의 연결이라는 중요한 방향성 제시
  - 성능 개선이 유의미하나 절대값으로는 여전히 해결 과제 많음
  - 향후 여러 연구의 기초가 될 가능성 높음

- **Clarity (명확성)**: 4/5
  - 전체 파이프라인과 동기가 명확하게 설명됨
  - Figure와 예제가 이해를 돕고 있으나, 일부 기술적 세부사항(예: 프롬프트 설계 원칙)은 부록 의존도 높음

- **Overall (종합)**: 4/5

**총평**: Lean-STaR은 형식 수학 증명에 자연언어 사고 과정을 체계적으로 통합한 창의적 연구로, 역방향 생성이라는 실용적 해법을 통해 데이터 부족 문제를 해결했다. 일관된 성능 개선과 신경-기호 시스템의 강점을 보여주는 점에서 의의가 있으나, 오라클 모델 의존성과 절대 성능 수준 개선폭의 측면에서 추가 발전 여지가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/264_Deepseek-prover_Advancing_theorem_proving_in_llms_through_la/review]] — 둘 다 형식 정리 증명에서 LLM의 추론 능력을 향상시키는 방법을 연구하지만, 하나는 자연언어 사고를 통합하고 다른 하나는 강화학습 기반 접근법을 사용한다.
- 🏛 기반 연구: [[papers/539_Minif2f_a_cross-system_benchmark_for_formal_olympiad-level_m/review]] — Lean-star의 형식 증명 생성 능력을 평가할 수 있는 표준화된 올림피아드 수준 벤치마크를 제공한다.
- 🔗 후속 연구: [[papers/887_Wrong-of-thought_An_integrated_reasoning_framework_with_mult/review]] — 형식 증명에서 잘못된 추론 단계를 감지하고 수정하는 통합 프레임워크로 Lean-star의 사고-증명 교차 학습을 보완한다.
- 🔗 후속 연구: [[papers/513_M2F_Automated_Formalization_of_Mathematical_Literature_at_Sc/review]] — 기본적인 정리 증명을 대규모 교과서 형식화로 확장하여 실용적 응용 가능성을 보여준다.
