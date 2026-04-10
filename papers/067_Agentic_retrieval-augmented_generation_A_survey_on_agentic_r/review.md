---
title: "067_Agentic_retrieval-augmented_generation_A_survey_on_agentic_r"
authors:
  - "Aditi Singh"
  - "Abul Ehtesham"
  - "Saket Kumar"
  - "T. T. Khoei"
date: "2025"
doi: "10.48550/arXiv.2501.09136"
arxiv: ""
score: 4.0
essence: "대규모 언어모델(LLM)의 정적 학습 데이터 의존성을 극복하기 위해 자율 AI 에이전트를 RAG 파이프라인에 통합한 Agentic RAG 시스템에 대한 포괄적인 설문 논문이다. 이는 반성(reflection), 계획(planning), 도구 활용(tool use), 다중 에이전트 협력을 통해 동적 검색 전략과 적응형 워크플로우를 가능하게 한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Retrieval-augmented_Generation_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Singh et al._2025_Agentic retrieval-augmented generation A survey on agentic rag.pdf"
---

# Agentic retrieval-augmented generation: A survey on agentic rag

> **저자**: Aditi Singh, Abul Ehtesham, Saket Kumar, T. T. Khoei | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2501.09136](https://doi.org/10.48550/arXiv.2501.09136)

---

## Essence

![Figure 1](figures/fig1.webp) *Agentic RAG의 전체 개요*

대규모 언어모델(LLM)의 정적 학습 데이터 의존성을 극복하기 위해 자율 AI 에이전트를 RAG 파이프라인에 통합한 Agentic RAG 시스템에 대한 포괄적인 설문 논문이다. 이는 반성(reflection), 계획(planning), 도구 활용(tool use), 다중 에이전트 협력을 통해 동적 검색 전략과 적응형 워크플로우를 가능하게 한다.

## Motivation

- **Known**: LLM은 우수한 텍스트 생성 능력을 보유하지만 정적 학습 데이터에 의존하여 구식 정보 제공, 할루시네이션(hallucination) 발생, 실시간 쿼리에 대한 대응 불가능
- **Gap**: 전통적 RAG는 선형적 정적 워크플로우의 한계로 인해 복잡한 다단계 추론, 깊은 문맥 이해, 반복적 응답 정제 능력 부족
- **Why**: 의료, 금융, 교육 등 다양한 산업에서 실시간 데이터 통합, 복잡한 의사결정, 적응형 처리가 필수적으로 요구됨
- **Approach**: AI 에이전트의 agentic 패턴(반성, 계획, 도구 활용, 다중 에이전트 협력)을 RAG에 통합하여 동적 적응성과 확장성 달성

## Achievement

![Figure 2](figures/fig2.webp) *RAG의 핵심 구성 요소: 검색(Retrieval), 증강(Augmentation), 생성(Generation)*

1. **RAG 진화 체계화**: Naïve RAG → Advanced RAG → Modular RAG → Graph RAG → Agentic RAG으로 이어지는 패러다임 진화를 명확히 제시하고 각 단계의 특성, 강점, 한계를 상세히 분석

2. **Agentic RAG 분류법 제시**: 단일 에이전트, 다중 에이전트, 그래프 기반 프레임워크를 포함하는 포괄적인 분류 체계 제공

3. **실무 구현 가이드**: 벤치마크, 데이터셋, 도구 및 프레임워크, 윤리적 고려사항을 다루는 실질적 구현 전략 제시

## How

![Figure 3](figures/fig3.webp) *Naïve RAG: 단순 키워드 기반 검색의 한계*

![Figure 4](figures/fig4.webp) *Advanced RAG: 밀집 벡터 검색과 반복적 검색 메커니즘*

![Figure 5](figures/fig5.webp) *Modular RAG: 하이브리드 검색 전략과 구성 가능한 파이프라인*

- **RAG 기초**: 외부 데이터 소스(지식베이스, API, 벡터 데이터베이스)에서 실시간 정보 검색하여 LLM의 생성 능력과 통합
- **Agentic 패턴**: 반성(자가 검증), 계획(목표 분해), 도구 활용(외부 시스템 상호작용), 다중 에이전트 협력(분산 문제 해결)
- **워크플로우 패턴**: 프롬프트 체이닝(prompt chaining), 라우팅(routing), 병렬화(parallelization), 오케스트레이터-워커 모델, 평가자-최적화자 패턴
- **동적 적응**: 에이전트가 검색 전략을 자동으로 선택·조정하고 반복적으로 문맥 이해를 정제

## Originality

- **포괄적 설문 구성**: RAG의 역사적 진화부터 최신 Agentic RAG까지 체계적으로 정리한 유일한 대규모 설문 논문
- **분류 체계 신규**: Agentic 패턴과 워크플로우 패턴을 명확히 분류하여 이해를 체계화
- **산업별 응용 사례**: 의료, 금융, 교육 등 다양한 도메인의 실제 적용 사례 제시
- **구현 실무화**: 오픈소스 도구, 프레임워크, 벤치마크를 구체적으로 제시하여 실무 적용 가능성 높임
- **윤리 및 확장성 논의**: 자율 에이전트의 윤리적 의사결정과 시스템 확장성 문제를 명시적으로 다룸

## Limitation & Further Study

- **형식적 설문**: 논문이 설문(survey) 성격으로 신규 알고리즘이나 모델을 제시하지 않음
- **벤치마크 부족**: 다양한 Agentic RAG 시스템의 정량적 성능 비교가 제한적
- **윤리 프레임워크 미완성**: 자율 에이전트의 윤리적 의사결정에 대한 구체적 검증 메커니즘 부재
- **확장성 검증 부족**: 대규모 실제 데이터셋에서의 성능과 확장성 한계에 대한 실증적 데이터 제한
- **후속 연구**: (1) Agentic RAG 시스템의 통일된 벤치마크 개발, (2) 멀티모달 에이전트 RAG 확장, (3) 분산 다중 에이전트 환경에서의 성능 최적화, (4) 신뢰성 있는 에이전트 의사결정을 위한 형식 검증(formal verification) 연구 필요

## Evaluation

- **Novelty**: 3.5/5
  - RAG 진화 체계화와 분류법은 우수하나, 새로운 기술 개발보다는 기존 개념의 종합적 정리 성격
  
- **Technical Soundness**: 4/5
  - 각 패러다임의 기술적 설명이 명확하고 체계적이나, 실제 구현의 기술적 세부사항이 제한적
  
- **Significance**: 4.5/5
  - Agentic RAG의 실무 적용에 대한 포괄적 가이드를 제공하여 산업 활용도 높음
  
- **Clarity**: 4.5/5
  - 진화 단계별 시각화와 명확한 구조로 복잡한 개념을 효과적으로 설명
  
- **Overall**: 4/5

**총평**: 본 논문은 RAG에서 Agentic RAG로의 패러다임 진화를 체계적으로 정리하고 실무 구현을 위한 실질적 가이드를 제공하는 우수한 설문 논문이다. 다만 신규 알고리즘 개발이나 대규모 실증적 검증이 부재하여 기여도에는 한계가 있으며, 향후 Agentic RAG의 성능 벤치마킹과 윤리적 검증 연구가 필요하다.

## Related Papers

- 🧪 응용 사례: [[papers/602_Paperqa_Retrieval-augmented_generative_agent_for_scientific/review]] — 과학 연구를 위한 검색 증강 생성 에이전트의 실제 구현 사례를 제시한다.
