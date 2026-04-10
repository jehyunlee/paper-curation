---
title: "836_Towards_uncovering_how_large_language_model_works_An_explain"
authors:
  - "Haiyan Zhao"
  - "Fan Yang"
  - "Bo Shen"
  - "Himabindu Lakkaraju"
  - "Mengnan Du"
date: "2024"
doi: "arXiv:2402.10688"
arxiv: ""
score: 4.0
essence: "이 논문은 설명가능성(explainability) 관점에서 대규모 언어모델(LLM)의 내부 작동 메커니즘을 체계적으로 검토한 종합 리뷰 논문이다. 기계적 해석가능성(mechanistic interpretability), 표현 공학(representation engineering), 훈련 역학 분석을 통해 LLM의 지식 구성, 부호화, 학습 과정을 밝히고, 이러한 인사이트가 모델 편집, 프루닝, 인간 정렬에 어떻게 활용될 수 있는지 보여준다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Mechanistic_AI_Interpretability"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhao et al._2024_Towards uncovering how large language model works An explainability perspective.pdf"
---

# Towards uncovering how large language model works: An explainability perspective

> **저자**: Haiyan Zhao, Fan Yang, Bo Shen, Himabindu Lakkaraju, Mengnan Du | **날짜**: 2024 | **DOI**: [arXiv:2402.10688](https://arxiv.org/abs/2402.10688)

---

## Essence

![Figure 1](figures/fig1.webp) *대규모 언어모델의 작동 메커니즘: (a) 모델 컴포넌트 내 지식의 아키텍처 구성, (b) 중간 표현에 인코딩된 지식, (c) 훈련 과정에서의 일반화 능력 발달*

이 논문은 설명가능성(explainability) 관점에서 대규모 언어모델(LLM)의 내부 작동 메커니즘을 체계적으로 검토한 종합 리뷰 논문이다. 기계적 해석가능성(mechanistic interpretability), 표현 공학(representation engineering), 훈련 역학 분석을 통해 LLM의 지식 구성, 부호화, 학습 과정을 밝히고, 이러한 인사이트가 모델 편집, 프루닝, 인간 정렬에 어떻게 활용될 수 있는지 보여준다.

## Motivation

- **Known**: LLM(GPT-4, LLaMA-2, Claude-3 등)은 언어 이해 및 생성에서 뛰어난 성능을 보이며, 우수한 일반화 및 추론 능력을 시연함

- **Gap**: 이러한 모델의 성공 뒤의 "어떻게"와 "왜"는 여전히 불투명함. 할루시네이션, 독성, 인간 가치와의 불일치 등의 문제가 해결되지 못함

- **Why**: LLM의 안전하고 효과적인 배포를 위해서는 모델의 내부 작동 원리를 깊이 있게 이해하고, 각 컴포넌트의 기여도를 파악할 필요가 있음

- **Approach**: 기계적 해석가능성, 표현 공학, 훈련 역학 분석 등 기존의 설명가능성 기법들을 종합하여 LLM의 작동 메커니즘을 체계적으로 검토

## Achievement

![Figure 2](figures/fig2.webp) *트랜스포머 회로(Transformer Circuit)의 구조: Query-Key 회로와 Output-Value 회로를 통한 정보 처리 메커니즘*

1. **신경원(Neuron) 수준 분석**: 다의성(polysemanticity)의 발생 원인을 규명하고, 중첩(superposition)과 단일의미성(monosemanticity) 개념을 통해 신경원의 특성을 설명. 희소 자동인코더(sparse autoencoder)를 통해 특징 분해(feature disentanglement)의 가능성 제시

2. **회로(Circuit) 수준 분석**: 트랜스포머 회로에 대한 수학적 프레임워크를 제시하고, Query-Key 회로와 Output-Value 회로의 역할 구분. 귀납 헤드(induction head)가 맥락 내 학습(in-context learning) 능력에 기여함을 밝힘

3. **주의 헤드(Attention Head) 분석**: 귀납 헤드가 패턴 접두사 매칭(prefix matching)과 시퀀스 복사를 통해 맥락 내 학습을 가능하게 함을 실증적으로 입증

4. **훈련 역학 분석**: 그로킹(grokking) 및 기억화(memorization) 현상을 기계적 관점에서 설명하여, 모델의 일반화 능력 발달 과정을 규명

5. **실용적 응용**: 이러한 인사이트를 모델 편집(model editing), 프루닝(pruning), 인간 가치 정렬(human alignment)에 활용하는 방법론 제시

## How

- **기계적 해석가능성(Mechanistic Interpretability)**: 신경원, 회로, 주의 헤드 등 개별 컴포넌트의 기능과 상호작용을 분석하여 모델을 역공학(reverse-engineer)

- **중첩(Superposition) 분석**: 신경원 수보다 특징 수가 많을 때 여러 특징이 하나의 신경원에 인코딩되는 메커니즘을 ReLU 네트워크 등을 통해 규명

- **희소 자동인코더(Sparse Autoencoder)**: 사전 정의된 특징 사전(dictionary)을 활용하여 중첩된 특징을 분해하고 단일의미성을 달성하는 기법

- **트랜스포머 회로 프레임워크**: 디코더 전용 트랜스포머를 수학적으로 분석하여 QK 회로(정보 소스 선택)와 OV 회로(출력 생성)의 역할을 명확화

- **귀납 헤드 식별**: 두 개의 주의 헤드로 구성된 회로가 "[A*][B*]" 패턴으로부터 "[B]"를 예측하는 방식을 분석

- **훈련 동역학 분석**: 기억화 단계와 그로킹 단계를 구분하여 모델의 학습 과정 추적

## Originality

- **종합적 관점**: 기존 리뷰 논문들과 달리 설명가능성 기법 자체보다 "LLM이 어떻게 작동하는가"에 초점을 맞춤. 신경원, 회로, 주의 헤드, 훈련 역학 등 다양한 수준의 분석을 통합적으로 제시

- **계층적 분석 프레임워크**: 신경원-회로-헤드의 계층적 구조에서 지식 구성을 설명하고, 각 수준 간의 관계를 명확히 함

- **실용성 강조**: 설명가능성 분석이 모델 편집, 프루닝, 정렬 개선 등 구체적인 성능 향상으로 이어지는 경로를 보여줌

- **새로운 개념 통합**: 중첩, 단일의미성, 귀납 헤드, 그로킹 등 최근 발견된 개념들을 체계적으로 통합

## Limitation & Further Study

- **이론적 한계**: 대부분의 기계적 해석가능성 연구가 소규모 장난감 모델(toy model)에서 수행되었으며, 실제 LLM(수십억 개 파라미터)에 직접 적용하기 어려움

- **확장성 문제**: 희소 자동인코더 등의 방법이 대규모 모델에서 계산 효율성 측면에서 실용적이지 못할 수 있음

- **해석의 주관성**: 특징이나 회로를 "이해할 수 있는" 개념으로 매핑하는 과정에 주관성이 존재함

- **불완전한 인과성**: 귀납 헤드와 맥락 내 학습 간의 인과관계가 부분적으로만 입증됨

- **후속 연구 방향**:
  - 대규모 모델에 적용 가능한 확장성 있는 해석가능성 기법 개발
  - 특징 분해의 완전성을 보장하는 방법론 제시
  - 해석가능성 분석을 보다 정교한 인간 정렬 기법으로 변환하는 방법 탐색
  - 다중 모달(multimodal) 및 다국어 LLM에 대한 해석가능성 연구 확대

## Evaluation

- **Novelty**: 4/5 - 기존 리뷰보다 "how"에 초점을 맞춘 관점이 신선하며, 계층적 분석 프레임워크가 체계적이나, 개별 발견들은 기존 논문의 종합

- **Technical Soundness**: 4/5 - 제시된 기법들의 이론적 기반이 견고하나, 장난감 모델 기반 결과와 실제 LLM 간의 갭이 명확히 논의되지 않음

- **Significance**: 4/5 - LLM의 안전성과 정렬성 향상에 직결되는 중요한 주제를 다루나, 실제 배포 단계에서의 영향은 아직 제한적

- **Clarity**: 5/5 - 복잡한 개념들이 체계적으로 정리되었으며, Figure를 통한 시각화가 우수함

- **Overall**: 4/5

**총평**: 이 논문은 LLM의 내부 작동 메커니즘을 설명가능성 관점에서 체계적으로 정리한 우수한 리뷰 논문으로, 신경원·회로·헤드·훈련 역학의 계층적 분석을 통해 LLM의 투명성을 높인다. 다만 장난감 모델 기반 결과의 현실적 적용 가능성과 대규모 모델으로의 확장성은 여전히 과제로 남아 있다.

## Related Papers

- 🔗 후속 연구: [[papers/582_On_gradient-like_explanation_under_a_black-box_setting_when/review]] — LLM의 내부 작동 메커니즘 이해를 위한 체계적 검토가 블랙박스 설정에서의 설명가능성 연구의 이론적 확장이다.
- 🏛 기반 연구: [[papers/397_Hallucinations_can_improve_large_language_models_in_drug_dis/review]] — LLM의 해석가능성 연구가 환각 현상이 성능에 미치는 영향을 이해하는 데 필요한 기계적 이해를 제공한다.
- 🔄 다른 접근: [[papers/527_Mechanistic_interpretability_for_ai_safetya_review/review]] — AI 안전성을 위한 기계적 해석가능성과 LLM 작동 메커니즘 이해라는 유사하지만 다른 관점의 해석가능성 연구이다.
- 🔗 후속 연구: [[papers/017_A_practical_review_of_mechanistic_interpretability_for_trans/review]] — 대형 언어모델 작동 방식의 설명가능한 연구는 기계적 해석가능성의 실무 가이드를 더욱 심화된 연구 방향으로 확장합니다
- 🔄 다른 접근: [[papers/527_Mechanistic_interpretability_for_ai_safetya_review/review]] — LLM 작동 메커니즘 이해에서 기계론적 vs 설명가능성 기반의 다른 접근법을 비교할 수 있다
- 🏛 기반 연구: [[papers/397_Hallucinations_can_improve_large_language_models_in_drug_dis/review]] — LLM의 환각 현상을 이해하기 위해서는 언어 모델의 내부 메커니즘에 대한 근본적 이해가 필요하다.
- 🏛 기반 연구: [[papers/582_On_gradient-like_explanation_under_a_black-box_setting_when/review]] — LLM의 해석가능성 연구가 블랙박스 설정에서의 그래디언트 기반 설명 방법 개발의 이론적 배경을 제공한다.
