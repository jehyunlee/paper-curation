---
title: "628_Position_The_ai_conference_peer_review_crisis_demands_author"
authors:
  - "Jaeho Kim"
  - "Yunseok Lee"
  - "Seulki Lee"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "본 논문은 AI 학술대회의 급증하는 논문 제출(연 10,000편 초과)로 인한 피어 리뷰 품질 저하 문제를 진단하고, **양방향 피드백 시스템과 체계적 심사자 보상 제도**를 통해 심사자 책임성과 동기 부여를 강화하는 개혁방안을 제시한다."
tags:
  - "cat/Academic_Peer_Review_Automation"
  - "sub/AI_Peer_Review"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chubb et al._2025_Position The ai conference peer review crisis demands author feedback and reviewer rewards.pdf"
---

# Position: The AI Conference Peer Review Crisis Demands Author Feedback and Reviewer Rewards

> **저자**: Jaeho Kim, Yunseok Lee, Seulki Lee | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*AI 학술대회 제출 논문 수의 급증 추세 (2019-2025). NeurIPS, CVPR, AAAI, ICML, ICLR 등 주요 학회의 제출 논문이 2025년까지 10,000편을 초과했으며, ICLR의 경우 2025년 한 해에만 59.8% 증가함.*

본 논문은 AI 학술대회의 급증하는 논문 제출(연 10,000편 초과)로 인한 피어 리뷰 품질 저하 문제를 진단하고, **양방향 피드백 시스템과 체계적 심사자 보상 제도**를 통해 심사자 책임성과 동기 부여를 강화하는 개혁방안을 제시한다.

## Motivation

- **Known**: AI 학술대회(ICML, ICLR, NeurIPS, CVPR 등)의 논문 제출이 기하급수적으로 증가하고 있으며, 전통적 피어 리뷰 시스템이 이를 감당하지 못하고 있음
  
- **Gap**: 현재의 일방향 리뷰 시스템에서 심사자는 책임성이 없는 반면, 저자는 거부에 대한 모든 결과를 감수해야 하는 **권력 불균형** 존재. 심사자에 대한 동기부여 메커니즘 부재

- **Why**: 
  - 심사자 방치(Reviewer Negligence): 영향력 없는 심사에 대한 책임성 부족
  - LLM 생성 리뷰의 증가로 인한 기술적 깊이 저하
  - 심사자 착취: 보상 없는 고강도 업무 부담 (짧은 마감, 이중 역할)
  - 시스템 측의 동기부여 부족

- **Approach**: 
  1. **양방향 2단계 리뷰 시스템**: 저자가 리뷰 품질을 평가하되, 보복 행동을 최소화하는 구조
  2. **체계화된 심사자 보상 제도**: 검증 가능한 학술 자격으로 축적 가능한 보상 프레임워크

## Achievement

![Figure 2](figures/fig2.webp)
*제안된 양방향 2단계 피어 리뷰 시스템 수정안. (A) 현재의 표준 더블블라인드 시스템, (B) 2단계 및 3단계에서의 최소한의 수정으로 저자 피드백 및 심사자 평가 단계 삽입.*

1. **구조적 개혁**: 기존 더블블라인드 시스템에 최소한의 수정을 가하여 **양방향 피드백 메커니즘** 도입
   - 1차: 요약(Summary), 강점(Strengths), 질문(Questions) 공개
   - 저자 피드백: 논문 이해도 + LLM 플래그 평가
   - 2차: 약점(Weaknesses), 등급(Rating) 공개

2. **심사자 보상 제도**: 디지털 배지 시스템을 통한 **검증 가능한 학술 자격 축적**으로 장기적 전문성 신뢰도 구축

## How

- **2단계 더블블라인드 프로세스**:
  - 1단계 리뷰 공개 후 저자가 논문 이해도 및 LLM 생성 여부 평가
  - 보복 우려 최소화를 위해 평가 정보는 다음 단계에서만 심사자 공개
  - 기존 타임라인 내에서 구현 가능

- **저자 피드백 메커니즘**:
  - 객관적 기준(논문 이해도, LLM 탐지 플래그)에 기반한 평가
  - 심사자 신원 보호 유지

- **심사자 보상 시스템**:
  - 품질 리뷰에 대한 누적 인정
  - 이력서/CV에 명시 가능한 검증 가능한 자격
  - 학술 경력에서의 실질적 가치 제공

## Originality

- **이원적 책임성 프레임워크**: 저자와 심사자 간의 비대칭적 책임구조를 최소한의 수정으로 개선
- **심사 품질 평가의 객관화**: LLM 탐지 등 기술적 지표와 이해도 평가를 결합한 평가 방식
- **실행 가능한 설계**: 기존 컨퍼런스 타임라인과 인프라(OpenReview)에 용이하게 적응 가능
- **근본 원인 분류**: 해결 불가능한 원인(제출 급증, AI 분야의 빠른 변화)과 해결 가능한 원인(심사자 방치, 착취, 시스템 미흡)의 명확한 구분

## Limitation & Further Study

- **근본적 한계**: 제출 논문 증가와 AI 분야의 급속한 변화는 "리뷰 품질 천장선(review quality ceiling)"을 만들어 시스템 개선만으로는 극복 불가
- **실행 장애물**: 
  - 컨퍼런스 간 보상 시스템의 호환성 문제
  - 저자의 보복 행동 완전 차단 불가능성
  - LLM 탐지 도구의 신뢰성 부족
  
- **후속 연구 필요**:
  - 보상 시스템의 게임화(gamification) 방지 메커니즘 개발
  - 컨퍼런스 간 상호 인증 가능한 글로벌 심사자 자격 시스템 구축
  - 선택적 논문 제출 제한 및 리뷰 쇼핑(review shopping) 억제 정책 개발
  - 심사 품질 평가의 더욱 정교한 메트릭 개발

## Evaluation

- **Novelty (참신성)**: 4/5
  - 양방향 피드백 시스템 자체는 새로운 개념은 아니나, AI 컨퍼런스의 구체적 문제 맥락에서 최소한의 수정으로 제안한 점이 독창적
  - 심사자 보상 시스템과 결합한 종합적 접근이 참신

- **Technical Soundness (기술적 타당성)**: 3.5/5
  - 제안된 2단계 시스템의 구현 방안이 상세하지 않음
  - LLM 탐지 메커니즘에 대한 신뢰성 논의 부재
  - 보복 방지 메커니즘의 완결성 미흡

- **Significance (중요도)**: 4.5/5
  - AI 학술계의 가장 시급한 문제 중 하나를 다룸
  - 제안된 해결책이 즉시 실행 가능하고 광범위한 영향력 보유
  - 학술 생태계의 지속가능성에 직접 영향

- **Clarity (명확성)**: 4/5
  - 문제 진단(저자, 심사자, 시스템의 3자 책임)이 명확하고 체계적
  - 해결 가능/불가능한 원인 분류가 논리적
  - 그림을 통한 시각화가 효과적
  - 보상 시스템의 구체적 운영 방식은 추상적 수준에 머무름

- **Overall (종합)**: 4/5

**총평**: 본 논문은 AI 컨퍼런스 피어 리뷰 위기의 근본 원인을 체계적으로 분석하고, 권력 불균형 해소와 심사자 동기부여라는 두 가지 관점에서 실행 가능한 개혁안을 제시한 의미 있는 위치 논문이다. 다만 양방향 피드백 시스템의 세부 구현과 보복 방지 메커니즘, 보상 시스템의 실질적 운영 방안에 대한 더욱 정교한 설계가 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/591_Openreview_should_be_protected_and_leveraged_as_a_community/review]] — OpenReview 플랫폼 보호와 함께 AI 학술대회 피어 리뷰 위기 해결을 위한 상호 보완적 접근이다.
- 🔗 후속 연구: [[papers/870_Vulnerability_of_text-matching_in_mlai_conference_reviewer_a/review]] — 심사위원 배정 시스템 취약성과 함께 피어 리뷰 품질 저하의 복합적 원인을 다루어 종합적 개혁이 필요하다.
- 🏛 기반 연구: [[papers/608_Peer_Review_as_A_Multi-Turn_and_Long-Context_Dialogue_with_R/review]] — 다중턴 대화 기반 피어 리뷰로 양방향 피드백 시스템 구현의 기술적 기반을 제공한다.
- 🔗 후속 연구: [[papers/870_Vulnerability_of_text-matching_in_mlai_conference_reviewer_a/review]] — AI 학술대회 피어 리뷰 위기의 원인 중 하나로 심사위원 배정 시스템 취약성을 구체적으로 입증한다.
- 🔗 후속 연구: [[papers/608_Peer_Review_as_A_Multi-Turn_and_Long-Context_Dialogue_with_R/review]] — AI 학술대회 피어 리뷰 위기에 대한 해결책으로 다중턴 대화 기반 리뷰 시스템을 제안한다.
- 🔄 다른 접근: [[papers/591_Openreview_should_be_protected_and_leveraged_as_a_community/review]] — AI 학술대회 피어 리뷰 위기 해결을 위한 다른 접근으로 커뮤니티 자산 보호와 저자 피드백 시스템을 함께 고려해야 한다.
- 🔗 후속 연구: [[papers/154_Best_Practices_for_Using_AI_When_Writing_Scientific_Manuscri/review]] — AI 기반 논문 작성 도구의 책임감 있는 사용이 동료 심사 위기 해결을 위한 AI 시스템 도입의 윤리적 기반을 제공한다
- 🏛 기반 연구: [[papers/877_What_Can_Natural_Language_Processing_Do_for_Peer_Review/review]] — 동료 심사 과정의 NLP 지원 체계가 AI 시대 동료 심사 위기 해결을 위한 기술적 솔루션의 중요한 기반을 제공한다
- 🏛 기반 연구: [[papers/070_Agentreview_Exploring_peer_review_dynamics_with_llm_agents/review]] — AI 기반 피어 리뷰의 위기 상황에서 편향과 사회적 영향을 정량화할 수 있는 분석 도구를 제공한다.
- ⚖️ 반론/비판: [[papers/794_The_AI_Scientist-v2_Workshop-Level_Automated_Scientific_Disc/review]] — AI 학회 동료 심사 위기에 대한 우려는 AI Scientist-v2가 동료 심사를 통과한 논문을 생성했다는 성과와 상반된 시각을 제시한다.
- 🏛 기반 연구: [[papers/083_AI-Driven_Review_Systems_Evaluating_LLMs_in_Scalable_and_Bia/review]] — AI 학회 동료평가 위기에 대한 체계적 분석이 자동화된 검토 시스템 개발의 필요성과 방향성을 제시하는 이론적 근거가 됨
