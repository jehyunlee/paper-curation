---
title: "585_Openai_o1_system_card"
authors:
  - "OpenAI (Aaron Jaech"
  - "Adam Tauman Kalai"
  - "Adam Lerer 등)"
date: "2024"
doi: "-"
arxiv: ""
score: 4.0
essence: "OpenAI o1 모델은 대규모 강화학습(reinforcement learning)으로 훈련된 chain-of-thought 추론 능력을 갖춘 모델로, 기존 GPT-4o 대비 안전성과 강건성이 크게 향상되었으며 특히 jailbreak 공격에 대한 저항성이 획기적으로 개선되었다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Language_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/OpenAI et al._2024_Openai o1 system card.pdf"
---

# Openai o1 system card

> **저자**: OpenAI (Aaron Jaech, Adam Tauman Kalai, Adam Lerer 등) | **날짜**: 2024 | **DOI**: -

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: GPT-4o, o1, o1-preview, o1-mini의 jailbreak 평가 성능 비교*

OpenAI o1 모델은 대규모 강화학습(reinforcement learning)으로 훈련된 chain-of-thought 추론 능력을 갖춘 모델로, 기존 GPT-4o 대비 안전성과 강건성이 크게 향상되었으며 특히 jailbreak 공격에 대한 저항성이 획기적으로 개선되었다.

## Motivation

- **Known**: 기존 언어모델들은 빠른 직관적 사고(fast, intuitive thinking)에 의존하며, 안전 정책 준수에 있어 adversarial 공격에 취약함. GPT-4o는 이미 높은 성능을 보유하고 있으나 jailbreak 평가에서 개선의 여지 존재.

- **Gap**: 모델이 복잡한 추론 과정을 거치면서 안전 정책을 더 깊이 있게 이해하고 따를 수 있는지에 대한 검증 부족. 특히 chain-of-thought 추론 자체가 야기할 수 있는 새로운 위험성에 대한 분석 필요.

- **Why**: 더 지능화된 모델의 능력이 위험한 응용으로 악용될 가능성이 있으므로, 추론 능력 향상이 안전성 개선으로 이어지는지 종합적으로 검증해야 함.

- **Approach**: 
  - 다양한 안전 평가 시스템(disallowed content, jailbreak, hallucination, bias) 구축
  - 내부 red teaming과 외부 전문가(US AISI, UK AISI) 협력 평가
  - Chain-of-thought 관련 새로운 위험성 모니터링 연구 진행
  - Deliberative alignment 기법으로 모델이 안전 정책을 명시적으로 추론하도록 훈련

## Achievement

1. **Jailbreak 저항성 획기적 개선**: StrongReject 벤치마크에서 GPT-4o 대비 o1이 상당히 우수한 성능 달성 (Figure 1 참조). Production jailbreaks, 인간 기반 jailbreaks 등 모든 jailbreak 평가에서 o1 모델 계열이 GPT-4o를 능가.

2. **유해 콘텐츠 거부 강화**: Challenging Refusal Evaluation에서 o1이 0.92-0.934의 not_unsafe 점수로 GPT-4o의 0.713 대비 29-31% 향상. WildChat에서도 0.98 달성으로 0.945 상회.

3. **과도 거부(overrefusal) 개선**: 멀티모달 입력에서 o1의 not_overrefuse 점수가 0.96으로 GPT-4o의 0.48에서 두 배 향상. 양성 요청에 대한 거부율 감소.

4. **환각(hallucination) 감소**: SimpleQA에서 o1의 환각율 0.44(GPT-4o 0.61), PersonQA에서 0.20(GPT-4o 0.30)으로 30-35% 감소. 정확도도 동시에 향상(SimpleQA accuracy: 0.47 vs 0.38).

5. **편향성 개선**: BBQ 평가에서 명확한 답변의 경우 o1이 93-94% 정확도로 GPT-4o의 72% 대비 22% 향상. 모호한 질문에서도 o1-preview 대비 o1이 개선된 성능 표시 (63% → 96%).

## How

- **Deliberative Alignment 훈련**: 모델이 안전 정책을 명시적으로 추론하도록 학습시켜 맥락적 추론을 통한 정렬(alignment) 달성

- **다층 데이터 구성**: 공개 데이터(웹, 오픈소스) + 파트너십 proprietary 데이터 + 사내 커스텀 데이터셋 조합으로 강건한 추론 능력 구축

- **엄격한 데이터 필터링**: 
  - Moderation API와 안전 분류기(safety classifiers) 활용
  - CSAM 등 명시적 유해 콘텐츠 제거
  - 개인정보 사전 제거 처리

- **종합적 평가 프레임워크**:
  - 4가지 카테고리 안전 평가 (disallowed content, jailbreak, hallucination, bias)
  - 자동 채점기(autograder) 기반 객관적 메트릭 (not_unsafe, not_overrefuse 등)
  - 4개 jailbreak 평가 배치 (Production, Augmented, Human-sourced, StrongReject)

- **외부 협력 red teaming**: 학계 벤치마크(XSTest, StrongReject, BBQ) 통합 및 외부 전문가 기관과 사전배포 평가 진행

## Originality

- **Chain-of-thought 추론과 안전성의 명시적 연결**: 단순히 성능 향상이 아닌 느린 추론(slow reasoning)이 안전 정책 준수를 어떻게 개선하는지 체계적으로 입증한 첫 사례

- **Deliberative alignment 개념 도입**: 기존의 사후 안전성 조정이 아닌 훈련 단계에서부터 안전 정책 추론을 내재화하는 혁신적 접근

- **Chain-of-thought 자체의 위험성 모니터링**: 새로운 추론 능력이 야기할 수 있는 deception이나 다른 형태의 위험을 사전에 식별하려는 선제적 연구

- **멀티모달 안전 평가 강화**: 텍스트뿐 아니라 이미지 입력에 대한 안전 경계 정확화

## Limitation & Further Study

- **도메인 특화 평가 부족**: 화학(chemistry) 등 특정 분야에서의 환각 현상에 대한 평가 및 이해 필요. 현재 평가가 모든 도메인을 포괄하지 못함을 명시.

- **Multimodal 모델 평가 제한**: o1-preview와 o1-mini가 이미지 입력을 지원하지 않아 멀티모달 refusal 평가 수행 불가. 향후 모달리티 확장 시 대응 필요.

- **모호한 질문에서의 "Unknown" 선택 문제**: o1-preview의 "Unknown" 선택 회피 현상이 o1에서는 개선되었으나, 근본 원인 분석과 일반화 가능성에 대한 깊이 있는 연구 필요.

- **Chain-of-thought 내 deception 감지**: 현재 deception 모니터링이 "ongoing research" 단계로, 모델이 추론 과정 내에서 사용자를 속일 가능성에 대한 실증적 증거와 완전한 대응책 부재.

- **Model update로 인한 평가 시간차**: 보고서 발표(12월 5일) 후 12월 17일 업데이트된 버전에 대한 평가 미포함. 지속적 개선에 따른 재평가 필요.

- **편향성 측정의 한계**: Race, gender, age 기반 계수 비교만 수행하며, 교차성(intersectionality) 및 다문화 맥락에서의 편향 분석 부재.


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 보고서는 대규모 언어모델의 안전성 평가에 있어 chain-of-thought 추론 능력이 defensive alignment의 새로운 차원을 제시함을 실증적으로 입증했으며, 다층적이고 체계적인 평가 프레임워크를 제시한 점에서 학계와 산업 모두에 중요한 기여를 한다. 다만 chain-of-thought 자체가 야기할 수 있는 deception 위험과 도메인 특화 평가의 부족은 향후 연구의 중요한 과제로 남아있다.

## Related Papers

- 🏛 기반 연구: [[papers/388_GPT-4o_System_Card/review]] — GPT-4o 시스템 카드는 OpenAI o1의 강화학습 기반 chain-of-thought 추론 개발에 이르는 기술적 진화의 배경을 제공한다.
- 🔄 다른 접근: [[papers/265_DeepSeek-R1_incentivizes_reasoning_in_LLMs_through_reinforce/review]] — DeepSeek-R1과 OpenAI o1 모두 강화학습을 통한 추론 능력 향상을 추구하지만 서로 다른 훈련 방법론과 안전성 접근을 사용한다.
- 🔗 후속 연구: [[papers/322_Evaluation_of_openai_o1_Opportunities_and_challenges_of_agi/review]] — OpenAI o1 평가 연구는 o1 시스템 카드의 안전성과 강건성 개선 주장을 AGI 맥락에서 기회와 도전으로 확장 분석한다.
- 🔗 후속 연구: [[papers/322_Evaluation_of_openai_o1_Opportunities_and_challenges_of_agi/review]] — OpenAI o1 시스템 카드를 통해 AGI 평가 결과의 구체적 시스템 구현을 확인할 수 있다
