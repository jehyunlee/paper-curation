---
title: "813_Toolformer_Language_Models_Can_Teach_Themselves_to_Use_Tools"
authors:
  - "Timo Schick"
  - "Jane Dwivedi-Yu"
  - "Roberto Dessì"
  - "Roberta Raileanu"
  - "Maria Lomeli"
date: "2023.02"
doi: "10.48550/arXiv.2302.04761"
arxiv: ""
score: 4.4
essence: "언어 모델이 자기 자신의 피드백만을 이용하여 계산기, 검색 엔진, 질의응답 시스템 등의 외부 도구를 언제 어떻게 사용할지 자동으로 학습할 수 있는 Toolformer 모델을 제안한다. 인간의 주석 없이 자가감독(self-supervised) 방식으로 학습되며, 6.7B 매개변수의 소규모 모델이 GPT-3보다 나은 성능을 달성한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/AI_in_Scientific_Research"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Schick et al._2023_Toolformer Language Models Can Teach Themselves to Use Tools.pdf"
---

# Toolformer: Language Models Can Teach Themselves to Use Tools

> **저자**: Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom | **날짜**: 2023-02-09 | **DOI**: [10.48550/arXiv.2302.04761](https://doi.org/10.48550/arXiv.2302.04761)

---

## Essence

![Figure 1](figures/fig1.webp) *Figure 1: Toolformer의 예시적 예측. 모델이 자율적으로 다양한 API(위에서부터: 질의응답 시스템, 계산기, 기계번역 시스템, Wikipedia 검색 엔진)를 호출하여 텍스트 완성에 필요한 정보를 획득한다.*

언어 모델이 자기 자신의 피드백만을 이용하여 계산기, 검색 엔진, 질의응답 시스템 등의 외부 도구를 언제 어떻게 사용할지 자동으로 학습할 수 있는 Toolformer 모델을 제안한다. 인간의 주석 없이 자가감독(self-supervised) 방식으로 학습되며, 6.7B 매개변수의 소규모 모델이 GPT-3보다 나은 성능을 달성한다.

## Motivation

- **Known**: 대규모 언어 모델(LM)은 맥락 학습(in-context learning)을 통해 새로운 작업에 뛰어난 능력을 보이지만, 산술 계산, 최신 정보 검색, 사실 확인 등의 기초적 기능에서는 취약하다.

- **Gap**: 기존의 도구 사용 접근법들은 대량의 인간 주석이 필요하거나 특정 작업에만 제한되어, 일반적인 언어 모델에 광범위하게 적용하기 어렵다.

- **Why**: 인간이 유용하다고 판단하는 것과 모델이 실제로 유용하다고 판단하는 것이 다를 수 있으므로, 인간 주석 없이 모델 자신의 손실함수(loss)를 기반으로 도구 사용 여부를 결정하는 것이 더 효과적이다.

- **Approach**: 사전학습된 대규모 언어 모델의 인-컨텍스트 학습 능력을 이용하여 잠재적 API 호출을 생성하고, 자가감독 손실함수를 통해 실제로 도움이 되는 호출만을 필터링한 후, 필터링된 API 호출들과 함께 원본 데이터셋으로 모델을 파인튜닝한다.

## Achievement

![Figure 2](figures/fig2.webp) *Figure 2: 접근 방식의 핵심 단계. 입력 텍스트 x가 주어지면 (1) 가능한 API 호출 위치와 후보들을 샘플링하고, (2) API 호출을 실행한 후, (3) 손실함수 감소에 기여하지 않는 호출들을 필터링하여 최종 데이터셋을 구성한다.*

1. **성능 향상**: 6.7B 매개변수의 Toolformer(GPT-J 기반)가 다양한 다운스트림 작업에서 175B 매개변수의 GPT-3을 능가하는 제로샷(zero-shot) 성능을 달성한다.

2. **일반성 보존**: 원본 사전학습 데이터셋을 그대로 사용하여 파인튜닝함으로써 언어 모델의 기본 능력을 손상시키지 않으면서 도구 사용 능력을 추가한다.

3. **다양한 도구 통합**: 질의응답 시스템, Wikipedia 검색, 계산기, 번역 시스템, 달력 등 5가지 이질적인 도구를 하나의 프레임워크에서 운영할 수 있다.

## How

![Figure 3](figures/fig3.webp) *Figure 3: 질의응답 도구를 위한 프롬프트 P(x)의 예. 모델에게 몇 가지 데모를 통해 API 호출의 형식과 위치를 학습시킨다.*

- **API 호출 샘플링 (Sampling)**: 
  - 프롬프트 P(x)를 통해 모델이 API 호출을 시작할 확률 p_i를 계산하고, 임계값(τ_s) 이상의 위치에서 최대 k개의 API 호출을 샘플링
  - 각 위치 i에서 최대 m개의 후보 API 호출 생성

- **API 호출 실행 (Executing)**:
  - 샘플링된 모든 API 호출을 실제로 실행하여 결과 획득
  - 도구마다 다른 실행 방식(신경망 호출, Python 스크립트 실행, 검색 시스템 등)

- **API 호출 필터링 (Filtering)**:
  - 가중 교차 엔트로피 손실(weighted cross-entropy loss)을 이용하여 유용성 판단
  - L⁻_i = min(L_i(ε), L_i(e(c_i, ε))): API 호출이 없거나 결과 없는 경우의 손실
  - L⁺_i = L_i(e(c_i, r_i)): API 호출과 결과가 제공되는 경우의 손실
  - 조건: L⁻_i - L⁺_i ≥ τ_f 를 만족하는 호출만 유지

- **모델 파인튜닝 (Finetuning)**:
  - 필터링된 API 호출들을 원본 텍스트에 삽입하여 새로운 데이터셋 C* 구성
  - 표준 언어 모델링 목적함수로 파인튜닝

- **추론 (Inference)**:
  - "→" 토큰이 생성되면 디코딩을 중단하고 해당 API 호출 실행
  - 결과와 </API> 토큰을 삽입한 후 디코딩 재개

## Originality

- **자가감독 학습의 혁신적 적용**: 인간의 주석 없이 모델 자신의 손실함수를 기반으로 도구 사용 필요성을 판단하는 방식은 완전히 새로운 접근이다.

- **인-컨텍스트 학습의 창의적 활용**: 사전학습된 대규모 모델의 인-컨텍스트 학습 능력을 이용하여 자동으로 API 호출 데이터셋을 생성함으로써 비용이 많이 드는 수작업 주석을 제거했다.

- **도구-불가지론적 프레임워크(Tool-agnostic framework)**: 텍스트 입출력만 지원하면 어떤 도구든 통합 가능한 일반적이고 확장성 있는 설계.

- **도구 호출의 명시적 표현**: 특수 토큰(API, /API, →)을 사용하여 API 호출을 텍스트에 자연스럽게 통합하고, 기존 어휘를 수정하지 않고도 작동 가능하도록 설계.

## Limitation & Further Study

- **제한사항**:
  - 텍스트 입출력만 지원하므로, 이미지나 구조화된 데이터 입력이 필요한 도구는 활용 불가능
  - 도구 결과가 항상 정확하다고 가정하지만, 실제로는 오류가 발생할 수 있고 이에 대한 강건성이 미흡할 수 있음
  - 필터링 임계값(τ_f, τ_s) 선택이 경험적이며, 최적화된 설정에 대한 체계적 연구 부족
  - 계산기는 기본 산술만 지원하고, 더 복잡한 수학 연산이나 기호적 추론은 미지원

- **후속 연구 방향**:
  - 도구의 오류 처리 및 오류 복구 메커니즘 개발
  - 더 복잡한 도구(이미지 생성기, 데이터 분석 도구 등)와의 통합
  - 다국어 설정에서의 도구 사용 능력 평가
  - 도구 호출의 최적성과 효율성에 대한 이론적 분석
  - 도구 조합(tool composition) 및 순차적 도구 호출의 학습

## Evaluation

- **Novelty (독창성)**: 4.5/5
  - 자가감독 기반 도구 학습 방식이 혁신적이나, 인-컨텍스트 학습과 손실함수 기반 필터링 개념 자체는 기존 아이디어의 조합

- **Technical Soundness (기술적 건전성)**: 4.5/5
  - 방법론이 명확하고 체계적이지만, 필터링 임계값 선택의 경험적 특성과 단순한 평가 메트릭 사용이 약점
  - API 호출 위치의 삽입 방식(prefix로만 제공)에 대한 충분한 정당화 필요

- **Significance (중요성)**: 4.5/5
  - 언어 모델의 한계를 극복하는 실질적 해결책을 제시하며, 산업 적용 가능성이 높음
  - 소규모 모델이 대규모 모델을 능가할 수 있음을 보여주는 중요한 증거

- **Clarity (명확성)**: 4.5/5
  - 전반적으로 잘 구성되어 있고 Figure가 효과적이나, 필터링 메커니즘의 수학적 표현이 다소 복잡하게 느껴질 수 있음
  - 각 도구별 구현 세부사항이 부록에 제한되어 있어 주문에 따른 확장성 평가 어려움

- **Overall (종합 평가)**: 4.4/5

**총평**: Toolformer는 인간 주석 없이 모델 자신의 피드백으로부터 도구 사용을 학습하는 획기적인 접근법을 제시함으로써, 언어 모델의 근본적 한계를 극복하는 실질적이고 일반적인 해결책을 제공한다. 비록 기술적으로는 기존 개념들의 신중한 조합이지만, 자동화된 데이터셋 생성과 효율적인 필터링을 통해 실용적 가치가 높으며, 소규모 모델의 대규모 모델 능가라는 임팩트있는 결과를 달성했다는 점에서 높이 평가된다.

## Related Papers

- 🏛 기반 연구: [[papers/174_Browsecomp_A_simple_yet_challenging_benchmark_for_browsing_a/review]] — 언어모델의 도구 사용 학습 연구가 복잡한 웹 브라우징 에이전트 평가 벤치마크의 기술적 기반을 제공합니다.
- 🔗 후속 연구: [[papers/793_The_Adoption_and_Usage_of_AI_Agents_Early_Evidence_from_Perp/review]] — 도구 사용 학습 모델에서 실제 AI 에이전트 사용 패턴과 채택 현황으로 확장한 실증적 연구입니다.
- 🔗 후속 연구: [[papers/655_ReAct_Synergizing_Reasoning_and_Acting_in_Language_Models/review]] — 도구 사용 학습에서 추론과 행동을 결합한 더 포괄적인 에이전트 프레임워크로 발전한 연구입니다.
- 🏛 기반 연구: [[papers/242_CRITIC_Large_Language_Models_Can_Self-Correct_with_Tool-Inte/review]] — Toolformer의 언어 모델 도구 사용 학습 방법론은 CRITIC의 외부 도구 상호작용 프레임워크 설계에 핵심적인 이론적 기반을 제공한다.
- 🏛 기반 연구: [[papers/114_Augmented_Language_Models_a_Survey/review]] — 증강 언어모델의 도구 사용 개념이 언어모델이 스스로 도구 사용을 학습하는 자율적 시스템 개발의 중요한 이론적 토대가 되었다
- 🔗 후속 연구: [[papers/496_LLM_Agents_Making_Agent_Tools/review]] — Toolformer의 언어 모델 자체 도구 사용 학습이 TOOLMAKER의 과학 논문 기반 자동 도구 생성으로 발전한 확장된 형태이다.
- 🏛 기반 연구: [[papers/499_LLM_With_Tools_A_Survey/review]] — 언어 모델이 스스로 도구 사용법을 학습하는 Toolformer의 기초 연구를 제공한다.
- 🏛 기반 연구: [[papers/174_Browsecomp_A_simple_yet_challenging_benchmark_for_browsing_a/review]] — 도구 사용을 학습하는 언어모델 연구의 기반 위에서 더 복잡한 웹 브라우징 능력을 평가하는 벤치마크를 구축합니다.
- 🏛 기반 연구: [[papers/793_The_Adoption_and_Usage_of_AI_Agents_Early_Evidence_from_Perp/review]] — 언어모델의 도구 사용 학습 연구가 AI 에이전트 채택과 활용 사례 분석의 기술적 배경을 제공합니다.
