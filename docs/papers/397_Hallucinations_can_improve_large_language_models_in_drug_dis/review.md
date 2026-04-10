---
title: "397_Hallucinations_can_improve_large_language_models_in_drug_dis"
authors:
  - "Shuzhou Yuan"
  - "Zhan Qu"
  - "Ashish Yashwanth Kangen"
  - "Michael Färber"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "일반적으로 문제로 간주되는 대규모 언어모델(LLM)의 환각(hallucinations)이 오히려 약물 발견의 분자 특성 예측 과제에서 모델의 성능을 향상시킬 수 있다는 역설적인 발견을 제시한다. 구조적 오기술(structural misdescription)과 같은 특정 유형의 환각이 모델의 일반화 능력을 증대시키는 암묵적 반사실(implicit counterfactual)로 작동함을 보여준다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Drug_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yuan et al._2025_Hallucinations can improve large language models in drug discovery.pdf"
---

# Hallucinations can improve large language models in drug discovery

> **저자**: Shuzhou Yuan, Zhan Qu, Ashish Yashwanth Kangen, Michael Färber | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) *HHEM-2.1-Open 모델을 사용한 사실적 일관성 점수. 대부분의 LLM이 MolT5 기준 설명과 낮은 일관성을 보여 광범위한 환각을 나타냄*

일반적으로 문제로 간주되는 대규모 언어모델(LLM)의 환각(hallucinations)이 오히려 약물 발견의 분자 특성 예측 과제에서 모델의 성능을 향상시킬 수 있다는 역설적인 발견을 제시한다. 구조적 오기술(structural misdescription)과 같은 특정 유형의 환각이 모델의 일반화 능력을 증대시키는 암묵적 반사실(implicit counterfactual)로 작동함을 보여준다.

## Motivation

- **Known**: LLM은 분자 특성 예측을 포함한 초기 약물 발견 과제에서 점점 더 활용되고 있으며, 자연언어 설명이 일반화를 개선할 수 있음이 증명되었다. 동시에 LLM이 생성하는 텍스트는 광범위한 환각을 포함하고 있다.

- **Gap**: 기존 연구는 환각을 제거 또는 완화해야 할 오류로만 취급했으나, 환각이 실제로 과학적 모델링 과제에서 창의성을 통해 유익한 역할을 할 수 있는지에 대한 체계적 조사가 부족하다.

- **Why**: 약물 발견 도메인에서는 방대한 화학 공간에 대한 추론이 필요하고, 창의성이 중요한 자산이다. 환각된 텍스트가 암묵적 반사실로 기능하여 미지의 화합물에 대한 모델의 일반화를 돕는 고수준 해석을 제공할 수 있다는 가설이 제기된다.

- **Approach**: 7개의 명령어 튜닝된 LLM을 5개의 분자 특성 예측 데이터셋(MoleculeNet)에서 평가. SMILES 문자열로부터 자연언어 설명을 생성하여 분류 과제의 프롬프트에 포함시킨 후, SMILES 전용, MolT5 기준 설명, PubChem 규칙 기반 텍스트 등 3가지 기준과 비교.

## Achievement

![Figure 2](figures/fig2.webp) *HIV 데이터셋 샘플을 이용한 방법 설명. SMILES로부터 환각된 분자 설명을 생성한 후 이진 분류 과제의 프롬프트에 포함*

1. **성능 향상**: Falcon3-Mamba-7B가 환각 포함 시 모든 기준선을 초과하며 PubChem 기준선보다 ROC-AUC 8.22% 개선. Llama-3.1-8B는 SMILES 기준선 대비 15.8%, MolT5 기준선 대비 11.2% 향상. GPT-4o에서 생성된 환각이 모델들 간 가장 일관된 성과 제공.

2. **환각 분석**: 18,000개 이상의 유익한 환각을 식별 및 분류. 구조적 오기술이 가장 영향력 있는 유형으로 도출되어, 분자 구조에 대한 환각된 진술이 모델 신뢰도를 증가시킬 수 있음을 시사. 기타 유형: 기능적 환각(functional hallucination), 유추적 환각(analogical hallucination), 일반적 수사(generic fluff).

## How

![Figure 3](figures/fig3.webp) *7개 LLM 전반의 ROC-AUC 평균 향상도*

- **프롬프트 설계**: 모든 모델과 데이터셋에서 일관성 보장을 위해 표준화된 프롬프트 템플릿 사용. 시스템 롤을 "약물 발견 전문가"로 정의하여 화학 관련 출력 유도

- **환각 정의**: 생성 텍스트에서 분자의 실제 구조 또는 알려진 특성으로 뒷받침되지 않는 모든 정보로 정의

- **사실적 일관성 평가**: HHEM-2.1-Open 모델 사용하여 생성 설명과 MolT5 기준 설명 간 정렬 측정. 대부분의 LLM은 7.42~13.58% 일관성만 달성 (ChemLLM 제외: 20.89%)

- **환각 유형 주석**: Deepseek-R1을 사용한 대규모 자동 주석. Fleiss' Kappa κ = 0.57로 인간 주석가와의 중간 수준 일치도 달성

- **과제 공식화**: 이진 분류 문제로 정의. 각 인스턴스는 [SMILES], [Description], [Instruct]로 구성된 프롬프트 입력. Eq. 1에 따라 최고 확률 토큰 선택

- **절제 연구**: 모델 크기(larger models가 환각으로부터 더 큰 이익) 및 생성 온도(사실성에 영향하나 하류 성능에는 제한적 영향) 효과 분석

## Originality

- **첫 체계적 조사**: 환각이 분자 특성 예측, 초기 약물 발견의 핵심 부분 과제에서 LLM 성능을 개선할 수 있는지 최초 체계적으로 규명

- **환각의 긍정적 재해석**: 기존의 "오류 제거" 관점에서 벗어나 환각을 암묵적 반사실(implicit counterfactuals) 또는 "창의적 변형"으로 해석하는 패러다임 전환

- **다차원 분석**: 7개 LLM, 5개 데이터셋, 4가지 환각 유형, 모델 크기/온도 등 다층적 실증 분석을 통한 포괄적 이해 제공

- **도메인-특화 적용**: 추상적 함수 특성과 화학 공간에 대한 추론이 필요한 약물 발견이라는 도메인에 맞춤형 가설 제시

## Limitation & Further Study

- **주석 신뢰도 제약**: 자동 주석 기반 분석이지만 Kappa 0.57은 중간 수준이므로, 후속 연구에서는 더 높은 인간 검증 비율 필요

- **메커니즘 이해 부족**: 구조적 오기술이 왜 특히 유익한지에 대한 심층적 메커니즘 분석 미흡. 단순 신뢰도 증가 이상의 설명 필요

- **일반화 범위 제한**: 5개 MoleculeNet 데이터셋으로 평가했으나, 다른 도메인(단백질 설계, 재료 과학 등)으로의 확장성 미확인

- **모델 편향성 미분석**: 특정 LLM(특히 GPT-4o)의 환각이 일관되게 더 유익한 이유에 대한 모델 아키텍처/훈련 데이터 기반 분석 부재

- **온도 매개변수 효과**: 온도가 하류 성능에 제한적 영향을 미친다는 발견이 반직관적이므로, 추가 샘플링 전략 탐색 필요

- **실제 약물 발견 적용**: 초기 단계 특성 예측에 국한된 평가로, 실제 신약 개발 파이프라인에서의 임상적 유용성 검증 필요


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 환각의 역설적 유익성을 실증적으로 제시하는 창의적 연구로, 약물 발견 도메인에 새로운 관점을 제공한다. 다만 메커니즘 이해와 실제 적용 가능성 검증이 보완되면 임팩트가 더욱 강화될 것이다.

## Related Papers

- ⚖️ 반론/비판: [[papers/814_Tooling_or_Not_Tooling_The_Impact_of_Tools_on_Language_Agent/review]] — 화학 분야에서 도구 증강이 항상 성능 향상으로 이어지지 않는다는 발견과 환각이 오히려 도움이 된다는 발견이 기존 AI 개선 방식에 대한 의문을 제기한다.
- 🏛 기반 연구: [[papers/836_Towards_uncovering_how_large_language_model_works_An_explain/review]] — LLM의 환각 현상을 이해하기 위해서는 언어 모델의 내부 메커니즘에 대한 근본적 이해가 필요하다.
- 🔄 다른 접근: [[papers/471_Large_Language_Models_Cannot_Self-Correct_Reasoning_Yet/review]] — 자기 수정 능력의 한계를 다룬 연구로, 환각이 성능 향상에 도움이 된다는 발견과 모델의 자기 개선 한계를 대조적으로 보여준다.
- 🔗 후속 연구: [[papers/291_Drugclip_Contrastive_drug-disease_interaction_for_drug_repur/review]] — 약물 발견에서 LLM 환각 개선에서 대조학습 약물 재창출로의 확장
- 🏛 기반 연구: [[papers/814_Tooling_or_Not_Tooling_The_Impact_of_Tools_on_Language_Agent/review]] — 도구 증강의 한계를 보여주는 연구로, 환각이 오히려 도움이 될 수 있다는 발견과 연결하여 AI 성능 개선의 복잡성을 이해할 수 있다.
- 🏛 기반 연구: [[papers/836_Towards_uncovering_how_large_language_model_works_An_explain/review]] — LLM의 해석가능성 연구가 환각 현상이 성능에 미치는 영향을 이해하는 데 필요한 기계적 이해를 제공한다.
