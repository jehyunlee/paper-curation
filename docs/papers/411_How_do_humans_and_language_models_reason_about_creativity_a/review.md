---
title: "411_How_do_humans_and_language_models_reason_about_creativity_a"
authors:
  - "Antonio Laverghetta Jr."
  - "Tuhin Chakrabarty"
  - "Tom Hope"
  - "Jimmy Pronchick"
  - "Krupa Bhawsar"
date: "2025"
doi: "arXiv:2502.03253v2"
arxiv: ""
score: 4.0
essence: "본 논문은 STEM 분야의 창의성 평가에서 인간 전문가와 대규모 언어모델(LLM)이 어떻게 다르게 추론하는지를 비교 분석한다. 예시 제공 여부에 따른 창의성 평가 방식의 변화를 통해 인간과 AI의 인지 메커니즘과 편향의 차이를 규명한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Human-AI_Performance_Detection"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Sharma et al._2025_How do humans and language models reason about creativity a comparative analysis.pdf"
---

# How do humans and language models reason about creativity? a comparative analysis

> **저자**: Antonio Laverghetta Jr., Tuhin Chakrabarty, Tom Hope, Jimmy Pronchick, Krupa Bhawsar, Roger E. Beaty | **날짜**: 2025 | **DOI**: [arXiv:2502.03253v2](https://arxiv.org/abs/2502.03253v2)

---

## Essence

![Figure 3](figures/fig3.webp) *인간과 GPT-4O-MINI의 창의성 점수 비교*

본 논문은 STEM 분야의 창의성 평가에서 인간 전문가와 대규모 언어모델(LLM)이 어떻게 다르게 추론하는지를 비교 분석한다. 예시 제공 여부에 따른 창의성 평가 방식의 변화를 통해 인간과 AI의 인지 메커니즘과 편향의 차이를 규명한다.

## Motivation

- **Known**: 
  - CAT(Consensual Assessment Technique)는 창의성 평가의 표준 방식으로 높은 신뢰도를 보임
  - LLM은 인간 창의성 평가를 예측하는 데 인상적인 정확도 달성
  - 창의성은 '참신성(uncommonness)', '원거리성(remoteness)', '영리함(cleverness)' 세 가지 측면으로 구성

- **Gap**: 
  - 인간 전문가의 평가 과정에서 어떤 인지 메커니즘이 작동하는지 불명확
  - LLM이 어떤 특징에 주목하여 판단하는지, 인간과의 차이가 무엇인지 미해명
  - STEM 창의성 평가는 충분히 연구되지 않음

- **Why**: 
  - AI가 과학 연구(동료 평가, 아이디어 생성)에서 역할 확대
  - 신뢰할 수 있는 AI 창의성 평가 시스템 개발 필요
  - 인간-AI 평가 전략의 정렬 필요

- **Approach**: 
  - 72명의 STEM 전문가(예시 제공/미제공 조건)를 대상으로 설계 문제(Design Problems Task, DPT) 평가
  - 세부 평가 기준(참신성, 원거리성, 영리함) + 평가 설명 문장 수집
  - 계산 언어 분석(LLM 기반 심리언어 특성 분석) 및 LLM 병렬 분석

## Achievement

![Figure 1](figures/fig1.webp) *인간 피어슨 상관계수 비교*

![Figure 2](figures/fig2.webp) *LLM 피어슨 상관계수 비교*

1. **인간의 인지 과정의 차별화**:
   - 예시 미제공 전문가: 비교 언어("더 나음/못함") 과다 사용, 참신성 강조 → 메모리 검색 기반 비교 의존
   - 예시 제공 전문가: 더 정교한 평가 설명, 다양한 평가 기준 고려
   - 같은 수준의 정확도에도 불구하고 인지 프로세스 상이

2. **LLM의 동질화된 평가 메커니즘**:
   - 예시 미제공: 참신성과 원거리성 우선시 (의미 유사성 기반)
   - 예시 제공: 정확도 향상하나, 세 가지 측면과 참신성 간 상관계수 0.99 이상으로 급증 → 개별 측면의 동질화/구별 불가

## How

![Figure 4](figures/fig4.webp) *인간과 GPT-4O-MINI 설명 비교*

- **데이터 수집**:
  - 학부 STEM 전공자 7000+ 응답 (기존 DPT 데이터셋 활용)
  - 80명 모집 (STEM 학위 소유, 영어 유창)
  - 2가지 조건: 예시 제공(3개 샘플: 점수 1, 3, 5) vs 미제공

- **평가 프로토콜**:
  - 1단계: 참신성 점수(5점 리커트)
  - 2단계: 평가 설명 작성(1-2문장)
  - 3단계: 참신성, 원거리성, 영리함 세부 평가

- **분석 방법**:
  - LLM 기반 심리언어 특성 자동 추출: 과거/미래 지향성, 비교 언어, 분석적 언어, 인지적 메커니즘 등
  - LIWC 대비 LLM이 심리언어 특성 예측에서 더 강한 성능 (선행연구)
  - 상관분석, 회귀분석, 텍스트 분석

- **품질 관리**:
  - 최종 샘플: 예시 조건 37명(481평가) + 미제공 35명(455평가)
  - 제외 기준: 승인률 <90%, AI 사용 보고, 불충분한 설명 등

## Originality

- **혁신적 접근**:
  - STEM 창의성 평가 분야에 **세분화된 인지 과정 분석** 도입
  - LIWC 대신 **LLM 기반 심리언어 분석** 활용으로 방법론 개선
  - **맥락 정보의 영향**을 체계적으로 조사 (예시 제공 조건 실험 설계)

- **이론적 기여**:
  - 인간과 AI의 창의성 평가 메커니즘의 **본질적 차이** 규명
  - LLM의 예시 제공 시 "동질화(homogenization)" 현상 발견 → 다중 측면 평가 능력 약화 지적
  - 메모리 검색 vs 의미 유사성 기반 평가 전략의 구분

- **실무적 기여**:
  - AI 창의성 평가 시스템 설계 시 해석가능성(interpretability) 고려 필요
  - 인간-AI 평가 정렬 전략 개발을 위한 기초 데이터 제공

## Limitation & Further Study

- **한계**:
  - 표본 크기 상대적으로 소수 (최종 72명 전문가)
  - DPT 과제의 특수성으로 인한 일반화 제한 (다른 STEM 영역, 창의성 평가 유형으로의 확장 필요)
  - LLM 분석이 특정 모델(GPT-4O-mini)에 집중 → 다양한 아키텍처 비교 부재
  - 인과성 추론의 한계 (관찰 연구)

- **후속 연구 방향**:
  - 다양한 LLM 아키텍처(Claude, Llama 등)와의 비교 분석
  - 미세조정(fine-tuning)된 모델 vs 영점 학습(zero-shot) 모델의 비교
  - 인간-AI 협력 창의성 평가 시스템 개발
  - 다른 STEM 평가 과제(과학 논문, 엔지니어링 설계안) 확대 적용
  - 평가자 전문성 수준에 따른 차이 분석


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 STEM 창의성 평가에서 인간 전문가와 LLM의 인지 메커니즘의 근본적 차이를 체계적으로 규명하는 의미 있는 연구로, 맥락 정보의 영향과 LLM의 동질화 현상이라는 새로운 발견을 제시한다. 다만 표본 규모 확대와 다양한 모델 비교를 통한 일반화 강화가 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/417_HypoBench_Towards_Systematic_and_Principled_Benchmarking_for/review]] — STEM 창의성 평가의 체계적 벤치마킹이 인간-AI 창의성 추론 비교 연구의 평가 기반을 제공합니다.
- 🔗 후속 연구: [[papers/494_Liveideabench_Evaluating_llms_scientific_creativity_and_idea/review]] — 창의성과 아이디어 평가에서 인간과 LLM의 차이를 더 포괄적인 과학적 창의성 벤치마크로 확장한 연구입니다.
- 🔄 다른 접근: [[papers/409_How_ai_ideas_affect_the_creativity_diversity_and_evolution_o/review]] — AI가 인간 창의성에 미치는 영향과 인간-AI 창의성 평가 방식의 차이라는 서로 다른 관점을 제시합니다.
- 🏛 기반 연구: [[papers/153_Best_humans_still_outperform_artificial_intelligence_in_a_cr/review]] — 인간과 언어 모델의 창의성에 대한 추론 방식을 분석하여 본 논문의 창의성 비교 연구의 이론적 기반을 제공한다.
