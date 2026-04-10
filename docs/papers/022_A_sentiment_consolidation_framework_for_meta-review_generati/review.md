---
title: "022_A_sentiment_consolidation_framework_for_meta-review_generati"
authors:
  - "Miao Li"
  - "Jey Han Lau"
  - "Eduard Hovy"
date: "2024"
doi: ""
arxiv: ""
score: 4.0
essence: "과학 논문 동료 평가(peer review)에서 메타리뷰 생성을 위해 감정 통합의 3계층 프레임워크를 제안하고, LLM 프롬프팅과 평가 메트릭을 개발하여 검증한 연구."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Scientific_Literature_Summarization"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Li et al._2024_A sentiment consolidation framework for meta-review generation.pdf"
---

# A sentiment consolidation framework for meta-review generation

> **저자**: Miao Li, Jey Han Lau, Eduard Hovy | **날짜**: 2024 | **URL**: [https://arxiv.org/abs/2402.18005](https://arxiv.org/abs/2402.18005)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: The three-layer framework of the underlying*

과학 논문 동료 평가(peer review)에서 메타리뷰 생성을 위해 감정 통합의 3계층 프레임워크를 제안하고, LLM 프롬프팅과 평가 메트릭을 개발하여 검증한 연구.

## Motivation

- **Known**: LLM은 간단한 지시로 요약을 생성할 수 있지만, 특히 의견 정보가 포함된 문서에서 정보 통합 능력의 불확실성이 존재한다. 기존 감정 요약 연구는 주로 제품 리뷰 도메인에 집중되어 있다.
- **Gap**: 과학 도메인에서의 감정 요약(메타리뷰 생성)은 충분히 탐구되지 않았으며, 인간 메타리뷰어의 실제 정보 통합 논리와 감정 융합 과정에 대한 설명이 부족하다.
- **Why**: 메타리뷰 생성은 여러 리뷰어의 의견을 이해하고 다층 토론을 종합하여 최종 결정을 지원해야 하므로, 복잡한 감정 통합이 필요한 중요한 과제이다.
- **Approach**: 인간 메타리뷰어가 따르는 3계층 감정 통합 프레임워크(입력층-통합층-생성층)를 가설화하고, 이를 LLM 프롬프팅 방법론과 평가 메트릭으로 구현하여 경험적으로 검증한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: The three-layer framework of the underlying*

- **3계층 감정 통합 프레임워크**: 메타리뷰어가 판정을 식별, 재조직(평가 측면별), 의견 통합하는 과정을 체계화
- **인간 주석 데이터**: 메타리뷰와 원본 문서에 대한 구조화된 감정 주석 수집 및 공개
- **자동 평가 메트릭**: 생성된 메타리뷰의 감정 정확성을 평가하는 참조 기반/무참조 메트릭 제안
- **경험적 검증**: 프레임워크 기반 프롬프팅이 기본 지시보다 우수한 메타리뷰 생성을 달성함을 증명

## How

![Figure 1](figures/fig1.webp)

*Figure 1: The three-layer framework of the underlying*

- PeerSum 데이터셋의 리뷰 및 토론 입력 데이터 활용
- Novelty, Soundness, Clarity, Advancement, Compliance, Overall quality 등 6개 평가 측면 정의
- 인간 주석자 2명이 판정(Content Expression, Sentiment Expression, Review Facet, Sentiment Level, Convincingness Level) 추출
- GPT-4 기반 자동 주석을 통한 대규모 데이터 확장
- 3계층 프레임워크를 LLM 프롬프트로 통합하여 구조화된 메타리뷰 생성 유도

## Originality

- 과학 도메인 감정 요약 작업의 새로운 정의 및 체계화
- 메타리뷰어의 인지 과정을 3계층 구조로 명시화한 혁신적 프레임워크
- 판정의 5개 구성요소 체계를 통한 세밀한 감정 분석
- 감정 통합 논리를 설명 가능하게 만든 접근법

## Limitation & Further Study

- 현재 초점은 메타리뷰의 전체 감정 정확성에 제한되어 있으며, 생성된 텍스트의 다른 품질 측면(충실성, 관련성 등)은 미검토
- 30개 표본에 기반한 인간 주석으로 규모가 제한적
- LLM 기반 자동 주석의 신뢰성 검증 필요
- 다른 학문 분야나 비영어 논문에 대한 프레임워크 일반화 검토 필요
- 후속 연구: 메타리뷰 생성의 다른 품질 차원 통합, 더 큰 규모 데이터셋 확보, 추론 및 갈등 해결 메커니즘 심화 연구

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 메타리뷰 생성이라는 현실적이고 중요한 과제에 대해 인간의 의사결정 논리를 기반한 혁신적인 3계층 프레임워크를 제안하였으며, 경험적 검증을 통해 그 효과성을 입증한 의미 있는 연구이다.

## Related Papers

- 🔄 다른 접근: [[papers/778_Summarizing_multiple_documents_with_conversational_structure/review]] — 둘 다 동료평가에서 감정 통합을 다루지만 서로 다른 프레임워크와 접근 방식을 사용함
- 🔗 후속 연구: [[papers/270_Detecting_llm-written_peer_reviews/review]] — 동료평가의 감정 통합을 AI 생성 리뷰 탐지와 결합하여 더 포괄적인 동료평가 품질 관리 방법을 제시함
- 🏛 기반 연구: [[papers/665_Remor_Automated_peer_review_generation_with_llm_reasoning_an/review]] — LLM을 활용한 동료평가 생성의 기초적 접근이 감정 통합 프레임워크를 통한 메타리뷰 생성의 이론적 토대를 제공함
- 🔄 다른 접근: [[papers/385_Glimpse_Pragmatically_informative_multi-document_summarizati/review]] — 메타 리뷰 생성을 위한 감정 통합 프레임워크로 다중 문서 요약과 다른 접근 방식의 리뷰 종합을 제공한다.
- 🧪 응용 사례: [[papers/739_Seagraph_Unveiling_the_whole_story_of_paper_review_comments/review]] — 메타 리뷰 생성에 SEAGraph의 감정 통합 프레임워크를 적용할 수 있다.
- 🔗 후속 연구: [[papers/534_Meta-review_generation_with_checklist-guided_iterative_intro/review]] — 감정 통합 프레임워크를 체크리스트 기반 반복 자기성찰로 확장하여 더 체계적인 메타리뷰 생성을 가능하게 합니다.
