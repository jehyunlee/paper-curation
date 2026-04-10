---
title: "470_Large_language_models_can_self-improve"
authors:
  - "Jiaxin Huang"
  - "Shixiang Gu"
  - "Le Hou"
  - "Yuexin Wu"
  - "Xuezhi Wang"
date: "2022"
doi: "N/A"
arxiv: ""
score: 4.25
essence: "대규모 언어모델(LLM)이 레이블 없는 데이터만으로 자기 생성 고신뢰도 추론(reasoning) 경로를 통해 자가 개선(self-improve)할 수 있음을 입증한 논문이다. Chain-of-Thought 프롬팅과 자기 일관성(self-consistency)을 활용하여 감독 신호 없이 모델의 추론 능력을 향상시킨다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Self-Refining_Text_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Huang et al._2022_Large language models can self-improve.pdf"
---

# Large language models can self-improve

> **저자**: Jiaxin Huang, Shixiang Gu, Le Hou, Yuexin Wu, Xuezhi Wang, Hongkun Yu, Jiawei Han | **날짜**: 2022 | **DOI**: N/A

---

## Essence

![Figure 1: 방법의 개요. Chain-of-Thought 예시를 활용하여 언어모델이 여러 개의 CoT 추론 경로를 생성하고, 다수결 투표(Majority Voting)로 고신뢰도 답변을 선택한 후, 이를 파인튜닝 데이터로 활용](figures/fig1.webp)

*그림 1: 방법의 개요. Chain-of-Thought 예시를 활용하여 언어모델이 여러 개의 CoT 추론 경로를 생성하고, 다수결 투표(Majority Voting)로 고신뢰도 답변을 선택한 후, 이를 파인튜닝 데이터로 활용*

대규모 언어모델(LLM)이 레이블 없는 데이터만으로 자기 생성 고신뢰도 추론(reasoning) 경로를 통해 자가 개선(self-improve)할 수 있음을 입증한 논문이다. Chain-of-Thought 프롬팅과 자기 일관성(self-consistency)을 활용하여 감독 신호 없이 모델의 추론 능력을 향상시킨다.

## Motivation

- **Known**: LLM은 scaling을 통해 우수한 성능을 달성했으며, 특히 Chain-of-Thought(CoT) 프롬팅과 자기 일관성(self-consistency) 기법으로 추론 능력이 향상되고 있다. 하지만 성능 개선을 위해서는 여전히 대규모 고품질 감독 데이터(supervised dataset)가 필요하다.

- **Gap**: 기존 방식은 FLAN, T0, InstructGPT 등이 모두 대량의 인간 주석 데이터를 수집하거나 크라우드소싱에 의존한다. 반면 인간 뇌는 외부 입력 없이 자체 추론을 통해 메타인지(metacognition) 과정으로 학습한다.

- **Why**: 레이블 없는 데이터로도 LLM을 개선할 수 있다면, 비용이 많이 드는 인간 주석 작업을 크게 줄일 수 있을 것이다. 또한 모델이 자신의 추론 과정을 학습하는 방식은 인간의 학습 메커니즘과 유사하다.

- **Approach**: (1) 레이블 없는 질문 데이터에 CoT 프롬팅으로 다중 추론 경로 생성 (2) 다수결 투표로 고신뢰도 답변 선택 (3) 해당 답변으로 이어지는 모든 추론 경로를 파인튜닝 데이터로 사용 (4) 혼합 형식(mixed format) 증강으로 다양한 학습 데이터 생성

## Achievement

![Figure 2: GSM8K 훈련 집합에서 다중 경로 디코딩 후 다수결 투표 답변의 신뢰도와 정확도 관계](figures/fig2.webp)

*그림 2: GSM8K 훈련 집합에서 다중 경로 디코딩 후 다수결 투표 답변의 신뢰도와 정확도 관계*

1. **도메인 내 성능 대폭 향상**: 540B 파라미터 PaLM 모델에서 GSM8K 74.4%→82.1%, DROP 78.2%→83.0%, OpenBookQA 90.0%→94.4%, ANLI-A3 63.4%→67.9%로 개선. 감독 신호 없이 최신 수준(state-of-the-art) 성능 달성

2. **도메인 외 일반화(Out-of-Domain Generalization)**: AQUA, StrategyQA, MNLI 등 훈련 분포와 다른 데이터셋에서도 성능 개선. 자가 개선이 특정 데이터셋에 과적합(overfitting)되지 않고 일반적 추론 능력을 향상시킴을 입증

3. **상태 추적 능력**: 신뢰도 척도(confidence measure)가 실제 정확도와 높은 상관관계를 보임(Figure 2). 모델이 자신의 신뢰도를 정확히 평가할 수 있음을 시사

## How

![Figure 3: PaLM-540B에서 다중 경로 샘플링을 사용한 GSM8K 테스트 집합에서의 정확도 결과](figures/fig3.webp)

*그림 3: PaLM-540B에서 다중 경로 샘플링을 사용한 GSM8K 테스트 집합에서의 정확도 결과*

- **다중 경로 디코딩(Multiple Path Decoding)**: 각 질문 x_i에 대해 샘플링 온도 T > 0으로 m개의 CoT 추론 경로 {r_i1, r_i2, ..., r_im} 생성

- **다수결 투표 기반 필터링(Majority Voting Filtering)**: 생성된 경로들의 최종 답변 {y_i1, y_i2, ..., y_im}에 대해 다수결 투표로 가장 일관성 있는 답변 ỹ_i 선택. 반드시 정답일 필요는 없지만 여러 경로가 합의한 답변

- **자기 일관성 데이터셋 구성**: ỹ_i에 도달하는 모든 추론 경로 {r_ij | y_ij = ỹ_i}만 D_self-consistent에 포함

- **혼합 형식 증강(Mixed Format Augmentation)**: 동일한 (질문, 답변) 쌍에 대해 다양한 추론 형식을 함께 학습하여 강건성(robustness) 향상

- **파인튜닝**: 생성된 고신뢰도 (질문, 추론-답변) 쌍들로 원래 모델을 파인튜닝하여 자가 개선

- **추가 방법 탐색**: (1) 모델이 질문을 자체 생성하는 방식 (2) 모델이 CoT 프롬프트 템플릿을 생성하는 방식도 실험 (후자는 GSM8K에서 74.2% 달성으로 제로샷 최신 성능)

## Originality

- **신규 관점**: 레이블 없는 데이터로 LLM 자가 개선이 가능함을 처음 체계적으로 입증. 자기 일관성(self-consistency)을 단순 추론 개선 도구에서 자가 감독 신호 생성 메커니즘으로 활용

- **기존 기법의 창의적 결합**: CoT + self-consistency + 파인튜닝의 조합 자체는 새로운 아이디어이나, 각 구성 요소는 기존 연구에 기반. 그 조합의 효과성을 실증한 것이 기여

- **일관성-정확도 상관관계 활용**: 다수결 투표의 신뢰도가 정확도와 상관관계를 보인다는 관찰을 기반으로, 인간 주석 없이도 "고신뢰도" 학습 신호를 자동 추출하는 방법 개발

- **다방향 검증**: 도메인 내 4개 데이터셋, 도메인 외 3개 데이터셋, 하이퍼파라미터 연구, 절제 연구 등으로 강력한 실증 증거 제시

## Limitation & Further Study

- **신뢰도 평가의 한계**: 다수결 투표 신뢰도가 정확도와 상관관계를 보이지만 완벽하지는 않음. 비일관적(inconsistent) 오류나 체계적(systematic) 오류가 있는 경로도 학습 데이터에 포함될 수 있어 음의 영향 가능성

- **훈련 데이터 편향 증폭**: 자가 개선 과정에서 원래 모델의 편향(bias)이 증폭될 위험. 특히 소수 집단에 대한 편향이나 사실적 오류가 강화될 수 있음

- **계산 비용**: 다중 경로 디코딩으로 인한 추론 비용 증가는 언급되지 않음. m개 경로 생성 시 m배의 계산 필요

- **파인튜닝 데이터 품질 의존성**: "고신뢰도" 판정 기준이 단순 다수결이므로, 모델이 특정 오류 패턴을 보일 때 다수의 같은 오류가 학습될 수 있음

- **후속 연구 방향**: (1) 더욱 정교한 신뢰도 평가 메커니즘 개발 (2) 반복적 자가 개선 과정 연구 (3) 편향 및 오류 증폭 방지 기법 (4) 자가 생성 프롬프트 품질 향상 (5) 소형 모델에의 적용 가능성

## Evaluation

- **Novelty**: 4/5 
  - 자가 일관성을 자가 감독 신호로 활용하는 아이디어는 참신하나, 개별 구성 요소(CoT, self-consistency, fine-tuning)는 기존 기법 기반

- **Technical Soundness**: 4/5
  - 방법론이 명확하고 실험 설계가 합리적이나, 신뢰도-정확도 상관관계에 대한 이론적 분석 부족. 오류 증폭 위험에 대한 분석 미흡

- **Significance**: 5/5
  - 대규모 모델의 감독 없는 개선이 가능함을 실증적으로 보여주어 실무적 중요성 높음. 향후 LLM 개선 패러다임 변화의 가능성

- **Clarity**: 4/5
  - 전체적으로 명확하게 기술되었으나, 혼합 형식(mixed format) 증강의 구체적 방식이 덜 상세함. 모델 크기별 성능 분석 부족

- **Overall**: 4.25/5

**총평**: 이 논문은 레이블 없는 데이터로 대규모 언어모델이 자가 개선할 수 있음을 명확히 입증한 중요한 연구다. Chain-of-Thought와 자기 일관성을 창의적으로 조합하여 강력한 자동 감독 신호를 얻었으며, 도메인 내외 다수 데이터셋에서 상태 추적 수준의 성능을 달성했다. 다만 신뢰도 평가의 정교성, 오류 증폭 위험, 계산 비용 등의 한계가 있으나, 감독 신호 의존성을 크게 줄일 수 있다는 점에서 실무적 가치가 매우 높다.

## Related Papers

- 🏛 기반 연구: [[papers/746_Self-Refine_Iterative_Refinement_with_Self-Feedback/review]] — 자기 일관성과 고신뢰도 추론을 통한 자가 개선 방법론이 Self-Refine의 피드백 기반 반복적 정제 시스템의 이론적 토대를 마련함
- 🔗 후속 연구: [[papers/447_Iterative_self-incentivization_empowers_large_language_model/review]] — 반복적 자기 인센티브 방법이 레이블 없는 데이터를 통한 자가 개선을 강화학습 기반의 더 정교한 자기 동기 시스템으로 발전시킨 연구임
- ⚖️ 반론/비판: [[papers/471_Large_Language_Models_Cannot_Self-Correct_Reasoning_Yet/review]] — LLM이 아직 추론에서 자기 수정을 완전히 수행할 수 없다는 비판적 분석이 자가 개선 가능성에 대한 낙관적 결과에 반박하는 관점을 제시함
- 🏛 기반 연구: [[papers/746_Self-Refine_Iterative_Refinement_with_Self-Feedback/review]] — 둘 다 LLM이 외부 지도 없이 자기 개선하는 메커니즘을 다루지만, Self-Refine은 피드백 기반, 이 논문은 추론 경로 기반 접근법을 사용
- 🏛 기반 연구: [[papers/314_Enabling_language_models_to_implicitly_learn_self-improvemen/review]] — LLM의 일반적인 자기개선 능력에 대한 기초 연구가 암묵적 자기개선 프레임워크 개발의 이론적 토대를 제공함
