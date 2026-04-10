---
title: "500_Llm-based_corroborating_and_refuting_evidence_retrieval_for"
authors:
  - "Siyuan Wang"
  - "James R. Foulds"
  - "Md Osman Gani"
  - "Shimei Pan"
date: "2025"
doi: "arXiv:2503.07937"
arxiv: ""
score: 4.0
essence: "CIBER는 검색 증강 생성(RAG) 프레임워크를 확장하여 과학적 주장(claim)을 검증하기 위해 지지 증거와 반박 증거를 체계적으로 식별하고 검색하는 프레임워크이다. 다양한 질문 프로브(probe)를 통해 LLM의 응답 일관성을 평가함으로써 환각(hallucination) 문제를 완화한다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Scientific_Literature_Analysis"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Vargas et al._2025_Llm-based corroborating and refuting evidence retrieval for scientific claim verification.pdf"
---

# LLM-based Corroborating and Refuting Evidence Retrieval for Scientific Claim Verification

> **저자**: Siyuan Wang, James R. Foulds, Md Osman Gani, Shimei Pan | **날짜**: 2025 | **DOI**: [arXiv:2503.07937](https://arxiv.org/abs/2503.07937)

---

## Essence

![Figure 1](figures/fig1.webp)
*CIBER 시스템 아키텍처: 다중 측면 심문(MAI), 응답 해석(RR), 판정 및 신뢰도(V&C) 모듈로 구성*

CIBER는 검색 증강 생성(RAG) 프레임워크를 확장하여 과학적 주장(claim)을 검증하기 위해 지지 증거와 반박 증거를 체계적으로 식별하고 검색하는 프레임워크이다. 다양한 질문 프로브(probe)를 통해 LLM의 응답 일관성을 평가함으로써 환각(hallucination) 문제를 완화한다.

## Motivation

- **Known**: RAG는 LLM의 환각 문제를 완화하는 효과적인 기법으로 알려져 있으나, 여전히 잡음 견고성(noise robustness), 부정적 거절(negative rejection), 정보 통합 측면에서 오류가 발생한다. 특히 과학적 주장 검증과 같은 고신뢰도가 요구되는 분야에서는 문제가 심각하다.

- **Gap**: 기존 RAG 방식은 단순히 관련 문서를 검색하여 LLM에 제시하는 수준에 머물러 있으며, LLM 응답의 신뢰성을 다각적으로 평가하고 여러 관점의 증거를 체계적으로 통합하는 메커니즘이 부족하다.

- **Why**: 과학적 주장은 높은 정확성과 신뢰성을 요구하며, 단일 질문으로는 LLM의 일관성 있는 판단을 보장할 수 없다. 따라서 다양한 표현과 논리적 변이를 포함한 프로브를 통해 응답의 견고성을 검증할 필요가 있다.

- **Approach**: (1) 다중 측면 심문(MAI)으로 동일한 주장에 대해 다양한 표현의 프로브를 생성하고, (2) 응답 해석(RR) 모듈로 LLM의 자유로운 응답을 정규화하며, (3) 판정 및 신뢰도(V&C) 모듈에서 증거 융합 전략으로 최종 판정을 도출한다.

## Achievement

![Figure 1](figures/fig1.webp)
*CIBER의 세 가지 핵심 모듈 구성*

1. **지원/반박 증거 검색의 체계화**: 단순한 관련성 검색을 넘어 과학적 주장을 명확하게 지지하는 증거와 반박하는 증거를 구분하여 검색하고 제시할 수 있는 프레임워크 개발

2. **LLM 응답 신뢰성 평가 메커니즘**: 동일 프로브의 반복 실행과 다양한 표현 변이(PAG, PCF) 를 통해 LLM의 응답 일관성을 정량적으로 측정하고 신뢰도 점수(confidence score) 산출

3. **화이트박스/블랙박스 모델 모두 지원**: LLM의 내부 정보(파라미터, 학습 데이터)에 접근하지 않고도 동작하므로 ChatGPT, Claude 등 다양한 API 기반 LLM에 적용 가능

4. **비감독(Unsupervised) 접근**: 도메인별 라벨링 데이터를 요구하지 않아 다양한 과학 분야로 쉽게 확장 가능

## How

![Figure 1](figures/fig1.webp)
*CIBER 아키텍처의 세 가지 신규 모듈*

**1. 다중 측면 심문(Multi-Aspect Interrogation, MAI)**
- 원본 프로브(pO): "논문 A의 연구에 기반하여 주장 C가 참인가?"
- 동의 프로브 세트(PAG): pO 및 그 패러프레이즈(paraphrase)로 LLM 응답이 일치해야 함
- 충돌 프로브 세트(PCF): ¬pO(부정형) 및 그 패러프레이즈로 LLM 응답이 대조되어야 함
- 각 프로브에 대해 K번 반복 실행하여 확률 기반 응답 분포 수집

**2. 응답 해석(Response Resolution, RR)**
- 프롬프트 엔지니어링: GPT-2의 경우 "relatively/quite" 같은 부사를 추가하여 응답 제약, GPT-3.5/4는 "yes/no 또는 I am not sure"로 형식 제한
- 어휘 및 정규표현 기반 파서: "is true/false", "correct/incorrect" 등의 변이 표현을 정규 형식(Support, Refute, Neutral)으로 매핑

**3. 판정 및 신뢰도(Verdict and Confidence, V&C)**
세 가지 증거 융합 전략:
- **가중 비율(Weighted Proportions, WP)**: PAG와 PCF의 응답 확률을 가중 평균으로 결합 (α는 trade-off 파라미터)
  - WPS = α·Prob(Support|PAG) + (1-α)·Prob(Support|PCF)
  - 최종 판정: argmax(WPS, WPR, WPN)
- **Dempster-Shafer 신념 업데이트(DS)**: 확률 이론 기반의 더 정교한 증거 통합
- **추가 전략**: 중앙값(median), 다수결(majority voting) 등 다양한 통합 방식 실험

## Originality

- **새로운 프레임워크 설계**: RAG의 생성 단계(generation stage)에 초점을 맞춰 LLM 응답의 불확실성을 체계적으로 측정하는 최초의 접근

- **논리적 일관성 검증**: 동의/충돌 프로브 쌍(agreement/conflict probe pairs)을 통해 LLM의 논리적 일관성뿐 아니라 어휘-구문 변이에 대한 강건성 평가

- **모델 비의존적 설계**: 블랙박스 LLM에 적용 가능하며, 특정 모델의 아키텍처에 의존하지 않는 범용적 접근법

- **비감독 학습**: 도메인 특화 라벨링 데이터 없이도 다양한 과학 분야에 즉시 적용 가능한 일반화 가능성

- **합성 및 실제 데이터셋 구축**: 평가를 위해 새로운 합성 데이터셋(synthetic datasets) 2개와 실제 데이터셋(real datasets) 2개 구축

## Limitation & Further Study

- **응답 파싱의 한계**: 프롬프트 엔지니어링과 정규표현 기반 파서가 LLM의 모든 표현 변이를 완벽하게 포착하지 못할 수 있으며, 모델별로 별도 튜닝 필요

- **계산 비용**: K번 반복 실행과 다중 프로브 조합으로 인한 API 호출 증가로 계산 비용과 지연 시간이 증가 (효율성 개선 필요)

- **증거 융합 전략의 최적화**: 현재 세 가지 기본 전략을 제시했으나, α 파라미터 설정과 최적 융합 방식에 대한 이론적 근거가 부족

- **대규모 평가의 필요성**: 다양한 과학 도메인(생의학, 기후과학, 기계학습 등)에서의 광범위한 벤치마크 평가와 실제 과학 문헌 대규모 말뭉치에서의 검증

- **설명가능성 강화**: 최종 판정에 이르는 과정에서 어느 문서와 프로브가 결정적 역할을 했는지에 대한 설명가능성 제공 방안 연구

## Evaluation

- **Novelty**: 4.5/5 — RAG 프레임워크의 생성 단계 강화라는 참신한 접근, 다중 측면 심문의 체계적 설계는 우수하나, 개념 자체는 응답 일관성 평가의 자연스러운 확장

- **Technical Soundness**: 4/5 — 프롬프트 엔지니어링과 정규표현 파서의 실용성은 좋으나, 응답 파싱의 견고성과 다양한 LLM에 대한 일반화 가능성은 추가 검증 필요

- **Significance**: 4/5 — 과학적 주장 검증이라는 중요한 응용 분야에서 실질적 개선을 제시하나, 평가가 주로 합성 데이터와 소규모 실제 데이터에 한정됨

- **Clarity**: 4/5 — 시스템 아키텍처와 각 모듈의 역할이 명확하게 설명되었고, 구체적 사례(기후변화, 심혈관질환)로 이해도 높으나, 수학적 기호와 증거 융합 전략의 설명이 다소 간결함

- **Overall**: 4/5

**총평**: CIBER는 RAG의 생성 단계에 초점을 맞춰 다중 측면 심문을 통해 LLM 응답의 신뢰성을 체계적으로 평가하는 혁신적 프레임워크로, 과학적 주장 검증과 같은 고신뢰도 응용에서 실질적 가치를 제공한다. 다만 대규모 실제 데이터에서의 광범위한 검증과 계산 비용 최적화, 설명가능성 강화가 향후 과제이다.

## Related Papers

- 🔗 후속 연구: [[papers/579_Nsf-scify_Mining_the_nsf_awards_database_for_scientific_clai/review]] — NSF 과학적 주장 데이터셋을 활용한 증거 검색 및 검증 시스템
- 🏛 기반 연구: [[papers/426_Improving_Scientific_Hypothesis_Generation_with_Knowledge_Gr/review]] — 지식 그래프 기반 가설 생성이 과학적 주장 검증의 방법론적 기반
- 🔗 후속 연구: [[papers/567_Multivers_Improving_scientific_claim_verification_with_weak/review]] — 과학적 주장 검증을 약한 지도학습으로 개선한 멀티모달 접근
- 🔄 다른 접근: [[papers/332_Fact-checking_complex_claims_with_program-guided_reasoning/review]] — 증거 검색 vs 프로그램 가이드 추론으로 사실 확인의 서로 다른 접근법
- 🔗 후속 연구: [[papers/426_Improving_Scientific_Hypothesis_Generation_with_Knowledge_Gr/review]] — 지식 그래프 기반 가설 생성을 과학적 주장 검증으로 확장한 방법론
- 🏛 기반 연구: [[papers/579_Nsf-scify_Mining_the_nsf_awards_database_for_scientific_clai/review]] — 대규모 과학적 주장 데이터셋이 주장 검증 시스템의 핵심 데이터 기반
