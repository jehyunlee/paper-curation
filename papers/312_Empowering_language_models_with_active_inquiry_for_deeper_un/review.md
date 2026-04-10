---
title: "312_Empowering_language_models_with_active_inquiry_for_deeper_un"
authors:
  - "Jing-Cheng Pang"
  - "Heng-Bo Fan"
  - "Pengyuan Wang"
  - "Jiahao Xiao"
  - "Nan Tang"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.25
essence: "본 논문은 대형 언어모델(LLM)이 사용자의 모호한 질의를 명확히 하기 위해 능동적으로 질문을 제기하는 LaMAI(Language Model with Active Inquiry) 방법을 제안한다. 능동학습(active learning) 기법을 활용하여 가장 정보량이 많은 질문을 선택함으로써 LLM의 응답 정확도를 크게 향상시킨다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Large_Language_Model_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Pang et al._2024_Empowering language models with active inquiry for deeper understanding.pdf"
---

# Empowering language models with active inquiry for deeper understanding

> **저자**: Jing-Cheng Pang, Heng-Bo Fan, Pengyuan Wang, Jiahao Xiao, Nan Tang, Si-Hang Yang, Chengxing Jia, Sheng-Jun Huang, Yang Yu | **날짜**: 2024 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: 능동적 문의를 통한 언어모델의 질의 응답 과정. (A) 문의 없이 직접 답변, (B) 사용자에게 명확한 질문을 통해 능동적으로 정보 수집*

본 논문은 대형 언어모델(LLM)이 사용자의 모호한 질의를 명확히 하기 위해 능동적으로 질문을 제기하는 LaMAI(Language Model with Active Inquiry) 방법을 제안한다. 능동학습(active learning) 기법을 활용하여 가장 정보량이 많은 질문을 선택함으로써 LLM의 응답 정확도를 크게 향상시킨다.

## Motivation

- **Known**: 기존 대형 언어모델은 사용자 질의에 직접 답변하는 자동회귀(autoregressive) 방식을 사용하며, RAG(Retrieval-Augmented Generation) 방법은 외부 지식 활용에는 효과적이지만 모호한 사용자 입력을 처리하는 데는 부족하다.

- **Gap**: 자연 인간 상호작용에서는 명확한 질문을 통해 정보를 수집하지만, 현재 LLM은 사용자의 모호한 의도를 파악하지 못하고 부정확하거나 도움이 되지 않는 응답을 생성하는 문제가 있다.

- **Why**: 사용자는 자신의 맥락을 공유한다고 가정하지만 LLM은 이에 접근할 수 없으므로, 대화형 명확화(interactive clarification)를 통해 실제 사용자의 의도를 파악하는 것이 필수적이다.

- **Approach**: 불확실성 추정을 통해 LLM의 모호함 수준을 판단하고, 능동학습을 적용하여 가장 정보량이 많은 명확화 질문을 선택한 후, 사용자 피드백을 기반으로 질의를 갱신하는 반복 대화 방식을 채택한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2: LaMAI 메서드의 전체 워크플로우. (A) 사용자 질의의 불확실성 평가, (B) 불확실성 추정 모듈, (C) 능동 문의 모듈, (D) 답변 생성 모듈*

1. **정확도 대폭 향상**: 복잡한 데이터셋에서 기존 31.9%에서 50.9%로 답변 정확도 향상, 다른 질의응답 프레임워크를 초과 성능 달성

2. **인간 평가에서의 우수성**: 실제 인간 참여 시나리오에서 기준 방법 대비 82% 이상의 경우에서 동등하거나 우수한 응답 생성

3. **다양한 LLM과의 호환성**: GPT-3.5, GPT-4 등 다양한 언어모델에 통합 가능하며, 방법의 견고성과 확장성 입증

## How

![Figure 3](figures/fig3.webp)

*Figure 3: QMSum 데이터셋에서의 LaMAI 비교 및 분석 결과*

LaMAI는 다음 세 가지 핵심 구성요소로 구성된다:

- **불확실성 추정(Uncertainty Estimation)**: 다중 답변 샘플링을 통해 T개의 답변 {A₁, A₂, ..., A_T}를 생성하고, 답변 간 변동성(variation)을 계산하여 모델의 불확실성을 정량화한다.

- **능동 문의(Active Inquiry)**: 불확실성이 높을 때, LLM에게 사용자 질의에 대한 명확화 질문 후보를 생성하도록 프롬프트하고, 능동학습 기법을 활용하여 가장 정보량이 많은 질문을 선택한다.

- **답변 생성(Answer Generation)**: 원래 사용자 질의에 명확화 질문에 대한 사용자 피드백을 추가하여 질의를 갱신하고, 업데이트된 질의를 기반으로 최종 답변을 생성한다.

- **반복 프로세스**: 불확실성이 만족스러운 수준으로 감소할 때까지 불확실성 재추정과 능동 문의 과정을 반복 수행한다.

## Originality

- **새로운 생성 방식**: 정적 지식베이스에 의존하는 기존 방법과 달리, 사용자와의 동적 정보 교환을 통해 질의-특정적 정보를 획득하는 새로운 LLM 답변 생성 스킴 제안

- **능동학습의 창의적 적용**: 정보성(informativeness)과 대표성(representativeness) 기반의 능동학습 기법을 LLM의 대화형 질문 선택에 처음으로 체계적으로 적용

- **인간 상호작용 패러다임**: 자연 인간 대화의 명확화 과정을 모델링하여, 기존의 일방향 LLM 응답 방식에서 쌍방향 대화형 접근으로의 패러다임 전환 제시

- **불확실성 기반 적응형 전략**: 단순한 고정 질문이 아니라 모델의 불확실성에 동적으로 반응하여 필요할 때만 문의하는 효율적 메커니즘 설계

## Limitation & Further Study

- **제한사항**: 
  - 방법의 효과는 사용자의 질문 응답 품질과 성실도에 크게 의존하며, 현실 환경에서 악의적이거나 부정확한 사용자 피드백에 대한 대응 메커니즘 부족
  - 명확화 질문 생성의 자동화 평가 메트릭이 제한적이고, GPT-4 기반 평가에의 의존성 높음
  - 반복 문의 횟수의 증가에 따른 사용자 피로도(user fatigue) 고려 부족

- **후속 연구**:
  - 신뢰도 낮은 피드백을 감지하고 가중치를 조정하는 메커니즘 개발
  - 사용자 만족도 최적화를 위한 질문 개수 자동 결정 알고리즘 연구
  - 도메인-특화 데이터셋에서의 적용 확대 및 실시간 상호작용 시나리오에서의 성능 평가 필요


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.0/5
- Significance: 4.5/5
- Clarity: 4.0/5
- Overall: 4.25/5

**총평**: LaMAI는 LLM이 모호한 사용자 질의를 처리하기 위해 능동적으로 명확화 질문을 제기하도록 하는 창의적인 접근으로, 불확실성 추정과 능동학습을 체계적으로 결합하여 상당한 성능 향상을 달성했다. 다만 현실 환경에서의 피드백 품질 관리와 사용자 경험 최적화 관련 더 깊이 있는 논의가 필요하다.

## Related Papers

- 🧪 응용 사례: [[papers/184_Can_large_language_models_provide_useful_feedback_on_researc/review]] — 능동적 질의 방법이 논문 피드백의 명확화에 활용됩니다.
- 🏛 기반 연구: [[papers/222_Clam_Selective_clarification_for_ambiguous_questions_with_ge/review]] — 모호성 해결을 위한 상호작용이 능동적 질의의 기반을 제공합니다.
- 🔗 후속 연구: [[papers/450_Knowledge_navigator_Llm-guided_browsing_framework_for_explor/review]] — 능동적 질의가 LLM 기반 탐색적 브라우징으로 확장됩니다.
