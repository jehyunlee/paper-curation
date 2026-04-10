---
title: "1087_Gpt4_is_slightly_helpful_for_peer-review_assistance_A_pilot"
authors:
  - "Zachary Robertson"
date: "2023"
doi: ""
arxiv: ""
score: 3.0
essence: "GPT-4가 피어리뷰(peer-review) 보조 도구로서 인간 리뷰어와 유사한 수준의 도움을 제공할 수 있는지를 파일럿 연구를 통해 조사한 논문이다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/LLM_Review_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Robertson_2023_Gpt4 is slightly helpful for peer-review assistance A pilot study.pdf"
---

# Gpt4 is slightly helpful for peer-review assistance: A pilot study

> **저자**: Zachary Robertson | **날짜**: 2023 | **URL**: [https://arxiv.org/abs/2307.05492](https://arxiv.org/abs/2307.05492)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Mean Helpfulness Ratings of GPT and Human Reviews. The bar chart illustrates the mean*

GPT-4가 피어리뷰(peer-review) 보조 도구로서 인간 리뷰어와 유사한 수준의 도움을 제공할 수 있는지를 파일럿 연구를 통해 조사한 논문이다.

## Motivation

- **Known**: 학술 출판의 질 보증을 위해 피어리뷰는 필수적이나, 연구 산출물의 급증으로 인해 인간 리뷰어의 역량이 점점 부족해지고 있다.
- **Gap**: GPT와 같은 대규모 언어모델(Large Language Model, LLM)이 학술 피어리뷰 프로세스에서 실제로 얼마나 유용한지에 대한 실증적 증거가 부족하다.
- **Why**: 리뷰 자원의 부족이 심화되는 상황에서 AI 기반 리뷰 지원 도구는 학술 출판 시스템의 확장성과 효율성을 크게 향상시킬 수 있는 잠재력을 가진다.
- **Approach**: 10명의 참여자를 대상으로 통제된 실험을 설계하여 GPT-4가 생성한 리뷰와 인간 리뷰어의 리뷰를 비교했으며, 추가로 적대적 공격(adversarial attack)에 대한 강건성 실험을 수행했다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: Mean Helpfulness Ratings of GPT and Human Reviews. The bar chart illustrates the mean*

- **동등한 도움 수준**: GPT 리뷰(3.0 ± 0.96)와 인간 리뷰(3.1 ± 0.57)가 5점 척도에서 동일한 수준의 도움 평가를 받음
- **GPT 리뷰의 특징**: 인간 리뷰보다 일관되게 논문 요약을 제공하며, 신규 논문에 대해 더 유용할 수 있음
- **강건성 분석**: GPT-4는 초록 변경 감지(recall 0.7)는 잘하지만 문장 수준의 비형식성 감지(recall 0.05-0.6)에는 취약함
- **맥락 크기의 역설적 효과**: 더 큰 맥락 윈도우(32k)가 오히려 성능을 저하시키는 현상 발견

## How


- 10명 참여자 모집, NeurIPS 리뷰 지침 기반 구조화된 가이드라인 제공
- GPT-4 8k 토큰 맥락으로 3단계 프롬프트 기법 적용: (1) 섹션별 노트 생성 → (2) 노트 구조화 → (3) 형식화된 리뷰 생성
- 형식 검증을 위한 반복 프로세스 구현 (평균 4.8 ± 1.1회 재시도)
- 저자가 1-5 척도로 리뷰 도움도 평가
- 추상 변경 및 비형식 문장 삽입 실험으로 20개 NeurIPS 논문에 대한 강건성 평가

## Originality

- 학술 피어리뷰 도메인에서 GPT의 실제 효용성을 인간 평가자와 직접 비교한 최초의 파일럿 연구
- 다단계 프롬프팅 기법으로 GPT가 구조화된 리뷰 생성하도록 하는 혁신적 방법론
- 적대적 공격을 통한 모델의 약점 분석으로 피어리뷰 도메인의 고유한 취약점 규명

## Limitation & Further Study

- 매우 제한적 샘플 크기(n=10, 실제로는 n=9)로 인한 일반화 불가능
- 참여자 선택의 편향성(자신의 논문 리뷰를 원하는 사람들이 자기선택 편향 발생 가능)
- 1회 평가만으로 신뢰성 있는 비교 불가능, 반복 측정 부재
- GPT 리뷰의 높은 분산(variance)이 불안정성을 시사하나 원인 분석 부족
- 맥락 크기 효과의 역설적 결과 설명 부족, 후속 연구 필요
- 블라인드 평가 미실시로 평가자가 GPT/인간 리뷰 식별 가능, 평가 편향 우려
- 제한된 도메인(NeurIPS) 실험으로 다른 학문 분야 적용성 미확인

## Evaluation

- Novelty: 3/5
- Technical Soundness: 3/5
- Significance: 3/5
- Clarity: 4/5
- Overall: 3/5

**총평**: 이 파일럿 연구는 학술 피어리뷰에 AI를 활용할 수 있는 가능성을 최초로 실증적으로 탐색했다는 점에서 의의가 있으나, 극도로 제한된 샘플 크기(n=9)와 설계상의 여러 편향으로 인해 강한 결론을 도출하기 어렵다. GPT의 높은 분산성과 문장 수준 오류 감지 부족은 현재 상태에서는 독립적인 리뷰 도구보다는 인간 리뷰의 보조 수단으로만 활용 가능함을 시사한다.

## Related Papers

- 🏛 기반 연구: [[papers/080_AI_is_transforming_peer_review__and_many_scientists_are_worr/review]] — GPT-4의 실제 동료평가 성능 검증이 AI 동료평가에 대한 우려의 근거를 제공한다
- 🔄 다른 접근: [[papers/809_Three_AI-powered_steps_to_faster_smarter_peer_review/review]] — 단순한 보조 역할을 넘어 체계적인 AI 동료평가 워크플로우를 제시한다
- ⚖️ 반론/비판: [[papers/860_Unveiling_the_sentinels_Assessing_ai_performance_in_cybersec/review]] — Doc2Vec 기반 접근법이 GPT-4보다 높은 정확도를 달성하는 대안적 결과를 보여준다
- 🔗 후속 연구: [[papers/080_AI_is_transforming_peer_review__and_many_scientists_are_worr/review]] — GPT-4의 동료평가 보조 역할에 대한 구체적 실험을 통해 우려를 검증한다
- 🔄 다른 접근: [[papers/860_Unveiling_the_sentinels_Assessing_ai_performance_in_cybersec/review]] — GPT-4 대신 Doc2Vec 기반 접근법으로 더 높은 정확도의 동료평가 예측을 달성한다
- 🏛 기반 연구: [[papers/809_Three_AI-powered_steps_to_faster_smarter_peer_review/review]] — GPT-4의 동료평가 보조 능력을 바탕으로 더 체계적인 워크플로우를 구축한다
- 🏛 기반 연구: [[papers/609_Peerarg_Argumentative_peer_review_with_llms/review]] — GPT-4의 동료평가 보조 능력을 바탕으로 더 구조화된 논증 기반 접근법을 제시한다
- 🔗 후속 연구: [[papers/776_Streamlining_the_review_process_Ai-generated_annotations_in/review]] — GPT-4의 동료평가 보조 역할을 원고 주석이라는 구체적 작업으로 특화한다
