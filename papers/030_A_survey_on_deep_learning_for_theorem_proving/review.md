---
title: "030_A_survey_on_deep_learning_for_theorem_proving"
authors:
  - "Zhaoyu Li"
  - "Jialiang Sun"
  - "Logan Murphy"
  - "Qidong Su"
  - "Zenan Li"
date: "2024"
doi: ""
arxiv: ""
score: 4.0
essence: "본 논문은 정리 증명(Theorem Proving)에 대한 심층학습 기법들을 포괄적으로 조사한 서베이 논문으로, 자동형식화, 전제 선택, 증명 단계 생성, 증명 탐색 등 주요 작업들과 방법론, 데이터셋, 평가 지표를 체계적으로 정리한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Formal_Theorem_Proving"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Li et al._2024_A survey on deep learning for theorem proving.pdf"
---

# A survey on deep learning for theorem proving

> **저자**: Zhaoyu Li, Jialiang Sun, Logan Murphy, Qidong Su, Zenan Li, Xian Zhang, Kaiyu Yang, Xujie Si | **날짜**: 2024 | **URL**: [https://arxiv.org/abs/2404.09939](https://arxiv.org/abs/2404.09939)

---

## Essence


본 논문은 정리 증명(Theorem Proving)에 대한 심층학습 기법들을 포괄적으로 조사한 서베이 논문으로, 자동형식화, 전제 선택, 증명 단계 생성, 증명 탐색 등 주요 작업들과 방법론, 데이터셋, 평가 지표를 체계적으로 정리한다.

## Motivation

- **Known**: 정리 증명은 수학의 기초이며, 1990년대부터 학습 기반 접근법이 연구되었다. 최근 대규모 언어모델(LLM)의 발전으로 이 분야의 연구가 급증하고 있으며, 2016년 2편에서 2023년 45편으로 증가했다.
- **Gap**: 깊은 학습을 이용한 정리 증명 연구가 급속도로 증가하고 있으나, 다양한 작업(task), 방법론, 데이터셋, 평가 방식이 산재되어 있어 진행 상황을 파악하고 과제를 식별할 수 있는 통합적 프레임워크가 부재하다.
- **Why**: 정리 증명의 자동화는 수학적 검증을 효율화하고, 소프트웨어 검증, 하드웨어 설계 등 실제 응용으로 확대될 수 있으며, 이를 위해 현황을 체계적으로 정리하는 것이 필수적이다.
- **Approach**: 180개 이상의 논문을 수집하여 비형식적/형식적 정리 증명의 배경, 5가지 주요 작업과 방법론, 데이터셋 분류, 평가 지표 및 최신 성능을 포괄적으로 분석하고, 미해결 과제와 향후 방향을 제시한다.

## Achievement


- **포괄적 작업 분류**: 자동형식화(Autoformalization), 전제 선택(Premise Selection), 증명 단계 생성(Proof-step Generation), 증명 탐색(Proof Search) 등 5가지 핵심 작업을 체계적으로 정리
- **방법론 분석**: 신경기계번역, 인코더-디코더 모델부터 대규모 언어모델(LLM)까지 진화 과정을 추적하고 각 작업별 최적 방법론 제시
- **데이터셋 및 합성 데이터 전략**: 수작업 큐레이션 데이터셋과 합성 데이터 생성 전략을 분류하고 정리
- **평가 지표 및 성능 비교**: 상태 최신 방법들의 성능을 평가 지표별로 비교 분석
- **문제점 및 미래 방향**: 현존하는 도전 과제를 명확히 하고 향후 연구 방향을 제시

## How

![Figure 2](figures/fig2.webp)

*Figure 2: Top: The informal statement and proof of the Fundamental Theorem of Arithmetic*

- 비형식적 정리 증명과 형식적 정리 증명(ATP, ITP)의 기본 개념 정의
- Lean, Coq, Isabelle 등 증명 보조기(Proof Assistant) 기반의 형식화된 증명 표현 방식 분석
- Transformer 기반 신경망, 주의(Attention) 메커니즘, 강화학습(Reinforcement Learning) 활용 방법 조사
- 수동 큐레이션 데이터셋(mathlib, ProofNet 등)과 프롬프트 기반 합성 데이터 생성 기법 정리
- 정확도(Accuracy), 통과율(Pass@k), 증명 완성도 등 다양한 평가 지표 제시
- 증명 트리(Proof Tree) 구조를 이용한 탐색 공간 모델링

## Originality

- 심층학습 기반 정리 증명 연구의 첫 번째 포괄적 서베이로, 180개 이상의 논문을 체계적으로 분류하고 통합 프레임워크 제공
- 비형식적 증명과 형식적 증명의 구조적 차이를 구체적 예시(산술의 기본정리)로 명확히 설명
- ATP와 ITP의 구별, 다양한 증명 보조기의 특징을 통합적으로 소개
- 단순한 논문 나열이 아닌 작업별 방법론 진화, 성능 비교, 한계 분석을 포함한 심층적 분석 제공

## Limitation & Further Study

- 서베이 논문으로서 완전히 새로운 방법론이나 알고리즘을 제시하지 않으며, 기존 연구의 정리 수준
- 2024년 7월까지의 데이터만 포함하여 신속한 발전 분야의 최신 동향 일부가 누락될 수 있음
- 형식적 증명(특히 Lean, Coq)에 초점이 있어 다른 형식 시스템(Isabelle, Metamath 등)의 심층 분석이 부족할 가능성
- 평가 지표의 표준화 부재 문제를 지적하지만 구체적 표준화 방안을 제시하지 않음
- **후속 연구**: LLM의 한계(hallucination, 신뢰성)를 극복하기 위한 검증 메커니즘 개발, 자동형식화 정확도 향상, 대규모 형식적 증명 데이터셋 구축 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 정리 증명 분야의 깊은 학습 응용에 대한 최초의 포괄적 서베이로, 급성장하는 연구 분야를 체계적으로 정리하고 통일된 프레임워크를 제공하는 중요한 기여를 한다. 높은 완성도와 명확한 설명으로 해당 분야 연구자들의 필수 참고자료가 될 것이다.

## Related Papers

- 🏛 기반 연구: [[papers/642_Proving_theorems_recursively/review]] — 정리 증명 심층학습 기법들을 재귀적 증명 방법론으로 발전시킨 이론적 기반
- 🏛 기반 연구: [[papers/1095_Towards_large_language_models_as_copilots_for_theorem_provin/review]] — 정리 증명 자동화 연구 동향이 Lean Copilot과 같은 실용적 도구 개발의 기반
- 🧪 응용 사례: [[papers/379_Generative_language_modeling_for_automated_theorem_proving/review]] — 생성형 정리 증명 연구에서 제시된 심층학습 기법들의 구체적 응용 사례
- 🔗 후속 연구: [[papers/264_Deepseek-prover_Advancing_theorem_proving_in_llms_through_la/review]] — 정리 증명 심층학습 기법을 LLM 기반 접근으로 발전시킨 최신 연구 동향
- 🧪 응용 사례: [[papers/642_Proving_theorems_recursively/review]] — 정리 증명에 대한 심층학습 기법 서베이에서 제시된 방법론을 재귀적 접근으로 구현
- 🧪 응용 사례: [[papers/1095_Towards_large_language_models_as_copilots_for_theorem_provin/review]] — 정리 증명 심층학습 서베이에서 제시된 방법론들을 실제 Lean 환경에서 구현한 응용
- 🏛 기반 연구: [[papers/489_Lf_a_foundational_higher-order-logic/review]] — 정리 증명을 위한 딥러닝에 대한 포괄적인 조사가 LF 논리 체계의 자동화 가능성을 이해하는 기반을 제공한다.
