---
title: "222_Clam_Selective_clarification_for_ambiguous_questions_with_ge"
authors:
  - "Lorenz Kuhn"
  - "Yarin Gal"
  - "Sebastian Farquhar"
date: "2023"
doi: "arXiv:2212.07769"
arxiv: ""
score: 4.0
essence: "대규모 언어모델(LLM)이 애매한 사용자 질문에 대해 명확화를 요청하지 않고 부정확한 답변을 제공하는 문제를 해결하기 위해, CLAM 프레임워크를 제안한다. 이는 애매한 질문을 감지하고 명확화 질문을 생성한 후 사용자의 명확화 정보를 바탕으로 최종 답변을 제공하는 선택적 명확화(selective clarification) 접근법이다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Scientific_Question_Answering"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liu et al._2022_Clam Selective clarification for ambiguous questions with generative language models.pdf"
---

# CLAM: Selective clarification for ambiguous questions with generative language models

> **저자**: Lorenz Kuhn, Yarin Gal, Sebastian Farquhar | **날짜**: 2023 | **DOI**: [arXiv:2212.07769](https://arxiv.org/abs/2212.07769)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1. (a) 일반적인 언어모델의 동작 (b) CLAM: 애매한 질문 감지 및 명확화 질문 생성*

대규모 언어모델(LLM)이 애매한 사용자 질문에 대해 명확화를 요청하지 않고 부정확한 답변을 제공하는 문제를 해결하기 위해, CLAM 프레임워크를 제안한다. 이는 애매한 질문을 감지하고 명확화 질문을 생성한 후 사용자의 명확화 정보를 바탕으로 최종 답변을 제공하는 선택적 명확화(selective clarification) 접근법이다.

## Motivation

- **Known**: 최신 Transformer 기반 LLM은 명확하게 정의된 질문-답변 작업에서 높은 성능을 보임. 정보검색 분야에서는 사용자 질문의 애매함이 잘 알려진 문제임.

- **Gap**: LLM 기반 질문-답변 커뮤니티에서 애매한 질문에 대한 문제가 거의 주목받지 못했음. SotA 모델들이 애매한 질문에 명확화를 요청하지 않고 대신 부정확한 답변을 제공하는 현상을 실증적으로 보임.

- **Why**: 실제 대화 시스템 배포 환경에서 사용자는 자주 애매한 질문을 제기하며, 이는 모델의 할루시네이션(hallucination) 문제와 맞닿아 있음.

- **Approach**: 프롬팅(prompting)을 이용한 메타인지(meta-cognition) 기반 프레임워크로 (1) 애매함 감지, (2) 명확화 질문 생성, (3) 명확화 후 답변 제공의 3단계 구현.

## Achievement

![Figure 2](figures/fig2.webp)
*Figure 2. 선택적 명확화의 4단계 과정*

1. **CLAM 프레임워크 제안**: 애매한 질문을 감지하고 선택적으로 명확화를 요청하는 통합 프레임워크 개발. 기존 SotA 모델 대비 애매한 질문 포함 데이터셋에서 유의미한 정확도 향상 달성.

2. **메타인지 개념 도입**: 언어모델이 "생각에 대한 생각"을 명시적으로 수행하는 메타인지를 새로운 설계 패러다임으로 제시. Chain-of-thought 프롬팅보다 체계화된 접근법 제공.

3. **자동 평가 프로토콜**: 비용이 많이 드는 인간 평가를 대체하기 위해, 특권정보(privileged information)를 제공받은 언어모델이 사용자 역할을 수행하는 자동 평가 방식 개발. 다중턴 대화 평가의 확장성 문제 해결.

4. **Ambiguous TriviaQA 데이터셋**: 200개의 애매한/명확한 질문 쌍으로 구성된 벤치마크 데이터셋 구축. 기존 ClariQ, CLAQUA 등의 한계를 보완.

## How

![Figure 3](figures/fig3.webp)
*Figure 3. 애매한 사용자 입력을 명확화하기 위한 프롬트 구조*

**CLAM 프레임워크 구현:**

- **Step 1a-1b: 애매함 감지** - Few-shot 프롬팅으로 질문을 이진 분류(애매/명확). 모델의 로그 확률(log probability)을 연속값 예측자로 활용

- **Step 2: 명확화 질문 생성** - 원문에 "이 질문에 답하기 위해 다음 명확화 질문을 제기해야 합니다"를 추가하는 프롬트로 영(zero-shot) 또는 소수샷(few-shot) 생성

- **Step 3: 사용자 명확화** - 실제 사용자 대신 특권정보를 가진 LLM이 명확화 정보 제공 (자동 평가)

- **Step 4: 최종 답변** - 원래 질문 + 명확화 질문 + 사용자 명확화를 모두 포함한 컨텍스트로 최종 답변 생성

**자동 평가 프로토콜:**
- 애매한 질문에 대한 명확화 정보(정답)를 언어모델에 프롬트로 제공
- 모델이 명확한 질문의 정답을 바탕으로 명확화 정보 생성
- 다중턴 대화 평가를 데이터셋 기반에서 데이터 생성 프로세스 기반으로 전환

## Originality

- **메타인지 패러다임**: 언어모델 설계에 메타인지 개념을 체계적으로 도입한 최초 작업. 단순 프롬팅 조합이 아닌 이론적 프레임 제시

- **자동 평가의 혁신**: 인간 평가 대신 특권정보 기반 LLM 시뮬레이션으로 다중턴 대화 평가 자동화. "평가 데이터셋→평가 데이터 생성 프로세스" 전환 제시

- **실용적 한계 해결**: 기존 데이터셋(ClariQ, CLAQUA)이 선택적 명확화 QA의 전체 파이프라인을 평가하지 못하는 한계를 명확히 하고, Ambiguous TriviaQA로 보완

- **명확한 실증**: 모델이 애매함을 감지할 수 있지만 명확화를 요청하지 않는 현상을 보여줌. 이는 사전학습/미세조정 데이터의 명확화 대화 부족이 원인임을 시사

## Limitation & Further Study

- **단일 반복 제한**: 현재 프레임워크는 1회 명확화만 수행. 다중 반복 명확화(recursive clarification)로 더 복잡한 애매함 해결 가능성은 미탐구

- **프롬트 의존성**: Few-shot 및 Zero-shot 프롬팅의 품질에 큰 의존. 프롬트 설계의 민감성과 일반화 가능성에 대한 심화 분석 부족

- **애매함 정의의 모호성**: 데이터셋이 TriviaQA에서 구성되어 특정 유형의 애매함(대명사, 명사구)만 포함. 의미적/논리적 애매함 등 다양한 유형 미포함

- **자동 평가의 한계**: 특권정보 기반 LLM 시뮬레이션이 실제 인간 행동을 완벽히 모사하는지 검증 부족. 인간 평가와의 상관관계 분석 필요

- **모델 크기/아키텍처 일반화**: 특정 LLM 모델에 대한 평가로 제한. 다양한 크기와 아키텍처의 모델에서의 효과 미검증

## Evaluation

- **Novelty**: 4.5/5 - 메타인지 패러다임과 자동 평가 프로토콜은 새로우나, 핵심 기술은 기존 프롬팅 기반

- **Technical Soundness**: 4/5 - 방법론은 견고하나 자동 평가의 타당성 검증 부족, 단일 반복 한계

- **Significance**: 4/5 - 실용적 중요성 높음. 배포 환경의 실제 문제 해결이나, 데이터셋 규모(200쌍)가 상대적으로 소규모

- **Clarity**: 4.5/5 - 프레임워크와 논의 명확함. 도표와 예시가 잘 구성되어 있으나 자동 평가 프로토콜 상세 설명 필요

- **Overall**: 4/5

**총평**: 애매한 질문에 대한 LLM의 선택적 명확화 요청이라는 실용적 문제를 메타인지 패러다임으로 창의적으로 해결하고, 자동 평가 프로토콜로 다중턴 대화 평가의 확장성을 높인 좋은 연구이다. 다만 기술적 독창성과 평가 규모에서 개선 여지가 있다.

## Related Papers

- 🔗 후속 연구: [[papers/223_Clarify_when_necessary_Resolving_ambiguity_through_interacti/review]] — 상호작용을 통한 모호성 해결 연구로 본 논문의 명확화 프레임워크를 대화형 시스템으로 확장한다.
- 🏛 기반 연구: [[papers/636_Prompt_to_be_consistent_is_better_than_self-consistent_few-s/review]] — 일관성을 위한 프롬프트가 자기 일관성보다 효과적임을 보여 본 논문의 선택적 명확화 접근법의 이론적 근거를 제공한다.
- 🔄 다른 접근: [[papers/747_Selfcheck_Using_llms_to_zero-shot_check_their_own_step-by-st/review]] — LLM의 단계별 자기 점검 방법으로 본 논문의 애매한 질문 처리와 다른 접근법의 품질 보장을 제시한다.
- 🏛 기반 연구: [[papers/312_Empowering_language_models_with_active_inquiry_for_deeper_un/review]] — 모호성 해결을 위한 상호작용이 능동적 질의의 기반을 제공합니다.
- 🔗 후속 연구: [[papers/223_Clarify_when_necessary_Resolving_ambiguity_through_interacti/review]] — CLAM의 선택적 명확화 방법이 Clarify when necessary의 모호성 해결 프레임워크를 더 정교한 질문 생성과 답변 시스템으로 발전시킨 연구임
