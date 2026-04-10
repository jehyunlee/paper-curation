---
title: "223_Clarify_when_necessary_Resolving_ambiguity_through_interacti"
authors:
  - "Michael J.Q. Zhang"
  - "Eunsol Choi"
date: "2023"
doi: "N/A"
arxiv: ""
score: 4.25
essence: "대규모 언어모델(LLM)이 모호한 사용자 입력을 처리할 때 명확화 질문을 통해 상호작용하도록 하는 작업 중립적 프레임워크를 제시하고, 사용자 의도 엔트로피 추정 방식인 INTENT-SIM을 통해 명확화가 필요한 경우를 효과적으로 식별한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Scientific_Question_Answering"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhang and Choi_2023_Clarify when necessary Resolving ambiguity through interaction with lms.pdf"
---

# Clarify when necessary: Resolving ambiguity through interaction with LMs

> **저자**: Michael J.Q. Zhang, Eunsol Choi | **날짜**: 2023 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*세 단계 프레임워크: (1) 명확화 필요 여부 판단, (2) 명확화 질문 생성, (3) 명확화 정보를 활용한 응답*

대규모 언어모델(LLM)이 모호한 사용자 입력을 처리할 때 명확화 질문을 통해 상호작용하도록 하는 작업 중립적 프레임워크를 제시하고, 사용자 의도 엔트로피 추정 방식인 INTENT-SIM을 통해 명확화가 필요한 경우를 효과적으로 식별한다.

## Motivation

- **Known**: 자연언어의 모호성(ambiguity)은 필연적이며, ChatGPT, Claude 등 현대의 AI 어시스턴트들이 널리 사용되고 있음. 그러나 기존 LLM들은 모호한 요청을 해결하기 위해 사용자와 상호작용하는 능력이 부족함.

- **Gap**: 언제 명확화를 요청할 것인지, 어떤 질문을 할 것인지, 받은 정보를 어떻게 활용할 것인지에 대한 체계적 프레임워크와 방법론이 부족함. 특히 모호성으로 인한 불확실성(aleatoric uncertainty)과 지식 부족으로 인한 불확실성(epistemic uncertainty)을 구분하는 방법이 없음.

- **Why**: 상호작용을 통한 모호성 해결은 자연언어 의사소통의 핵심 특성이며, 실제 AI 어시스턴트의 사용 가능성을 높이는 중요한 기능임.

- **Approach**: 3단계 작업 중립적 프레임워크를 설계하고, 사용자 의도의 분포를 모델링하여 명확화의 효용성을 판단하는 INTENT-SIM 방식을 제안. 질문응답(QA), 기계번역(MT), 자연언어 추론(NLI) 세 가지 NLP 과제에서 평가.

## Achievement

1. **명확화 필요성 판단의 정확성 향상**: INTENT-SIM이 기존 불확실성 추정 방식들(baseline uncertainty estimation approaches)보다 명확화로 개선될 예측을 식별하는 데 일관되게 우수한 성능을 보임. 예제의 10%만 명확화할 수 있을 때, 무작위 선택 대비 성능 개선을 2배 달성.

2. **강건성(Robustness) 검증**: INTENT-SIM이 다양한 NLP 과제와 LM에서 개선 효과를 보이며, 평가된 6가지 LM-과제 조합 중 4가지에서 최고 성능 달성.

3. **체계적 프레임워크 제공**: 모호성 해결을 위한 작업 중립적 3단계 프레임워크를 통해 다양한 NLP 응용에 적용 가능한 기초를 마련.

## How

![Figure 1](figures/fig1.webp)

**3단계 프레임워크 구조**:

- **Task 1 (명확화 필요 여부 판단)**: 
  - 불확실성 추정값 u(x)를 예측하여 상호작용 예산(interaction budget) b% 내에서 명확화가 필요한 상위 예제 선별
  - 평가 지표: 고정된 상호작용 예산 하에서의 성능(Performance Under Fixed Interaction Budget), AUROC (명확화로 개선될 예측 식별 능력)
  - 핵심: 높은 aleatoric 불확실성(의미적 모호성)과 낮은 epistemic 불확실성(지식 보유)을 가진 경우만 선택

- **Task 2 (명확화 질문 생성)**:
  - 오라클(oracle) 프롬팅 방식을 통해 각 사용자 의도에 대응하는 명확화 질문-답변 쌍 생성
  - 다양한 사용자 의도에 대한 안정적인 테스트베드 제공

- **Task 3 (명확화 활용 응답)**:
  - 입력 x와 명확화 QA 쌍을 조건으로 최종 응답 생성
  - SAMPLED와 UNIFORM 두 가지 데이터 생성 설정으로 평가 (빈도 분포 vs 균등 분포)

**INTENT-SIM 알고리즘**:
- 사용자 의도의 분포 P(y=y*|x) 상에서의 엔트로피를 추정하여 명확화의 효용성 판단
- 여러 사용자-어시스턴트 상호작용 시뮬레이션을 통해 의도 분포의 엔트로피 계산

## Originality

- **새로운 문제 정의**: 모호성 해결을 위한 명확화 상호작용을 체계적 3단계 프레임워크로 구조화한 최초의 작업
- **aleatoric vs epistemic 불확실성 구분**: 모호성으로 인한 불확실성과 지식 부족으로 인한 불확실성을 구분하는 명확한 개념적 틀 제시
- **INTENT-SIM 방식**: 사용자 의도의 엔트로피를 직접 추정하여 명확화의 실질적 효용을 판단하는 혁신적 접근
- **다중 과제 평가**: 작업 중립적 프레임워크를 QA, MT, NLI 등 다양한 NLP 과제에 적용하여 일반성 증명
- **현실적 데이터 분포 활용**: 기존 데이터셋의 다중 주석을 활용하여 자연스러운 사용자 의도 분포를 모델링

## Limitation & Further Study

- **Task 2의 제한성**: 명확화 질문 생성에 오라클 방식을 사용하여 현실적인 질문 생성의 한계를 노출. 실제 시스템에서는 LLM이 직접 생성해야 하므로 추가 연구 필요.

- **단순화된 가정**: 명확화 답변 집합 A와 최종 응답 Y 간의 일대일 대응(bipartite matching) 가정이 실제 상황의 복잡성을 완전히 반영하지 못함.

- **상호작용 비용 모델링 부족**: 사용자의 상호작용 거부율, 부정확한 답변, 여러 번의 명확화 필요성 등을 고려하지 않음.

- **언어 다양성**: 영어 기반 데이터셋에만 평가. 다른 언어 및 문화적 모호성 양식에 대한 확장 필요.

- **후속 연구 방향**:
  - Task 2에서 실제 LLM 기반 명확화 질문 생성 방식 개발 및 평가
  - 사용자 거부, 잘못된 응답 등 현실적 상호작용 시나리오 모델링
  - 다중 순차 명확화(sequential clarification) 전략 탐구
  - 명확화 질문의 자연스러움과 명확성 trade-off 분석

## Evaluation

- **Novelty**: 4.5/5
  - 모호성 해결을 위한 명확화 상호작용의 체계적 프레임워크 제시가 참신함. 다만 개별 구성요소(불확실성 추정, 질문 생성)들은 기존 연구를 활용.

- **Technical Soundness**: 4/5
  - INTENT-SIM의 엔트로피 추정 방식과 실험 설계가 엄밀함. 다만 오라클 기반 Task 2, 단순화된 가정들이 기술적 한계를 나타냄.

- **Significance**: 4.5/5
  - 현대 AI 어시스턴트의 실용적 문제를 다루며, 다양한 NLP 과제에 적용 가능한 일반적 프레임워크 제공. 산업적 영향 가능성이 높음.

- **Clarity**: 4/5
  - 전반적으로 명확하게 작성되었으나, 세 과제 간 상호의존성과 INTENT-SIM 알고리즘의 상세 설명이 부족할 수 있음.

- **Overall**: 4.25/5

**총평**: 본 논문은 LLM의 모호성 해결을 위한 명확화 상호작용이라는 미개척 영역에 체계적 프레임워크를 도입하고, INTENT-SIM을 통해 현실적 성능 개선을 달성한 견실한 연구이다. 다만 명확화 질문 생성에서 오라클 기반 접근의 한계와 현실적 상호작용 복잡성의 단순화로 인해, 실제 배포 시스템으로의 전환에는 추가 연구가 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/222_Clam_Selective_clarification_for_ambiguous_questions_with_ge/review]] — CLAM의 선택적 명확화 방법이 Clarify when necessary의 모호성 해결 프레임워크를 더 정교한 질문 생성과 답변 시스템으로 발전시킨 연구임
- 🧪 응용 사례: [[papers/641_Prototypical_human-ai_collaboration_behaviors_from_llm-assis/review]] — LLM 지원 글쓰기에서의 인간-AI 협력 행동 분석이 명확화 질문을 통한 상호작용 패턴의 실제 사용 사례를 보여줌
- 🏛 기반 연구: [[papers/435_Interfeedback_Unveiling_interactive_intelligence_of_large_mu/review]] — 대규모 모델의 인터랙티브 지능에 대한 연구가 사용자 의도 엔트로피 추정과 명확화 필요성 판단의 이론적 배경을 제공함
- 🧪 응용 사례: [[papers/641_Prototypical_human-ai_collaboration_behaviors_from_llm-assis/review]] — 명확화 질문을 통한 모호성 해결 프레임워크가 실제 LLM 지원 글쓰기 환경에서 관찰된 사용자-AI 상호작용 패턴의 이론적 설명을 제공함
- 🔗 후속 연구: [[papers/222_Clam_Selective_clarification_for_ambiguous_questions_with_ge/review]] — 상호작용을 통한 모호성 해결 연구로 본 논문의 명확화 프레임워크를 대화형 시스템으로 확장한다.
