---
title: "063_Agent-enhanced_large_language_models_for_researching_politic"
authors:
  - "Joseph Loffredo"
  - "Suyeol Yun"
date: "2025"
doi: "미제공"
arxiv: ""
score: 4.0
essence: "본 논문은 대규모 언어 모델(LLM)에 사전 정의된 함수와 특화된 도구를 장착하여 에이전틱 검색증강생성(Agentic RAG)을 구현한 LLM 에이전트가 정치기관 연구에서 데이터 수집, 전처리, 분석을 효율화할 수 있음을 보여준다. CongressRA라는 미 의회 연구 지원용 LLM 에이전트를 사례로 제시하며 이러한 접근법의 잠재력을 입증한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Specialized_Domain_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Loffredo and Yun_2025_Agent-enhanced large language models for researching political institutions.pdf"
---

# Agent-enhanced large language models for researching political institutions

> **저자**: Joseph Loffredo, Suyeol Yun | **날짜**: 2025 | **DOI**: [미제공](https://arxiv.org/abs/2503.13524)

---

## Essence

![Figure 2](figures/fig2.webp) *Agentic RAG: 연구자가 정의한 함수 집합과 AI 어시스턴트 프레임워크를 통해 LLM이 언제, 어디서, 어떻게 외부 정보를 검색할지 동적으로 결정하는 자율 에이전트로 작동*

본 논문은 대규모 언어 모델(LLM)에 사전 정의된 함수와 특화된 도구를 장착하여 에이전틱 검색증강생성(Agentic RAG)을 구현한 LLM 에이전트가 정치기관 연구에서 데이터 수집, 전처리, 분석을 효율화할 수 있음을 보여준다. CongressRA라는 미 의회 연구 지원용 LLM 에이전트를 사례로 제시하며 이러한 접근법의 잠재력을 입증한다.

## Motivation

- **Known**: 
  - LLM은 콘텐츠 생성, 텍스트 분석, 인간 행동 시뮬레이션 등 다양한 정치과학 작업에 활용되고 있음
  - RAG(Retrieval-Augmented Generation)는 외부 지식베이스를 통해 LLM의 할루시네이션(hallucination) 문제를 부분적으로 해결함

- **Gap**: 
  - 기존 RAG는 사전 정의된 검색 과정에 의존하여 유연성이 부족함
  - 정치기관 연구에서 필요한 컨텍스트별 복잡한 다단계 작업(데이터 수집, 전처리, 측정 구성)에 LLM을 종합적으로 활용하는 사례 부재

- **Why**: 
  - 정치기관 연구는 시간 경과에 따른 맥락별 데이터 처리가 필수적이며, 아카이브 자료 수집과 코딩 등 노동집약적 작업이 많음
  - LLM 에이전트는 이러한 반복적이고 시간 소비적 작업을 자동화하여 연구 비용을 절감할 수 있음

- **Approach**: 
  - Agentic RAG를 통해 LLM이 자율적으로 SQL 데이터베이스, 벡터 데이터베이스, API 등 다양한 외부 정보원을 선택하고 쿼리할 수 있도록 구현
  - 문서 요약, 분류, 통계 분석 등의 모듈식 도구를 통합한 에이전트 설계
  - 미 의회 입법 경직도(legislative gridlock) 지수 재구성을 통한 실증적 검증

## Achievement

![Figure 1](figures/fig1.webp) *검색증강생성(RAG): 사용자 쿼리를 외부 정보로 보강하여 LLM이 최신의 맥락적으로 관련된 콘텐츠 생성 가능*

![Figure 3](figures/fig3.webp) *CongressRA 아키텍처: U.S. 의회 연구 지원용 LLM 에이전트의 구조*

1. **LLM 에이전트의 연구 지원 역할 규명**: 전통적 RAG를 넘어 Agentic RAG가 LLM에 자율적 의사결정 능력을 부여하여 복합적 연구 작업 지원 가능함을 이론적으로 정립

2. **CongressRA 구현 및 검증**: Binder(1999)의 입법 경직도 지수를 재구성함으로써 LLM 에이전트가 기존 연구를 복제하고 확장할 수 있음을 실증적으로 입증

3. **모듈식 설계의 재사용성**: 작업별 지시사항 변경만으로 다양한 정치기관 연구 맥락에 적용 가능한 이식 가능한 도구 시스템 구현

## How

![Figure 4](figures/fig4.webp) *CongressRA를 활용한 입법 경직도 측정: 체계적 워크플로우를 통해 의회 기록에서 관련 정보 추출 및 분석 프로세스*

- **Agentic RAG 구현**:
  - LLM이 사용자 쿼리에 응답하기 위해 필요한 정보를 특정하고 최적의 데이터 소스(SQL DB, 벡터 DB, 그래프 DB, API, 웹 자원) 선택
  - 반복적 쿼리 정제를 통해 신뢰성 높은 정보 추출

- **모듈식 도구 통합**:
  - 문서 요약, 텍스트 분류, 정성적 변수 분류, 통계 모델링 등 다양한 함수를 모듈로 구성
  - 공유 도구 세트는 유지하면서 작업별 지시사항으로 맥락화(contextual)

- **정치기관 연구 워크플로우**:
  - 관련 사례 식별 → 데이터 소스 위치 파악 → 전처리 → 측정 구성 → 분석의 통합 자동화
  - 분산된 정보원에 걸친 종합적 데이터 통합

- **투명성 및 신뢰성 강화**:
  - 외부 데이터베이스 접근을 통해 정적 사전학습 지식의 한계 극복
  - 정보 출처 추적 가능성으로 할루시네이션 감소

## Originality

- **LLM 에이전트의 정치과학 적용 프레임워크**: 기존 RAG의 한계를 넘어 Agentic RAG라는 보다 정교한 아키텍처를 정치기관 연구에 처음으로 체계적으로 적용

- **모듈식 에이전트 설계 원칙**: 단일 에이전트가 다양한 정치기관 연구 컨텍스트에 적응 가능하도록 하는 설계 철학 제시

- **실증적 검증 사례**: 이론적 논의를 넘어 CongressRA를 통해 기존 연구(Binder 1999) 재구성이라는 구체적 성과로 증명

- **재현성 및 확장성 강조**: 샘플 코드 공개를 통해 다른 연구자들의 손쉬운 도입과 확장 가능성 제시

## Limitation & Further Study

- **할루시네이션 완전 해결 불가**: Agentic RAG가 할루시네이션을 감소시키나 완전히 제거하지는 못하며, 잘못된 쿼리 생성 가능성 존재

- **모델 편향 문제**: LLM의 사전학습 데이터에 내재된 편향이 여전히 검색 및 분석 과정에 영향 미칠 수 있음 (Feng et al., 2023; Motoki et al., 2024 등)

- **계산 비용 및 API 의존성**: 외부 API/데이터베이스 접근에 따른 비용 및 서드파티 서비스 의존성 미검토

- **도메인별 최적화 부재**: 현재 논의는 정치기관 연구 일반에 대한 것이며, 구체적 하위 분야(의회, 행정부, 사법부, 지방 정부 등)별 최적화 방안 미제시

- **후속 연구 방향**:
  - 다양한 정치과학 연구 맥락(비교정치학, 국제관계, 정치 이념 측정 등)에서 LLM 에이전트의 성능 비교 평가
  - LLM 에이전트가 생성한 측정치와 기존 인간 코더/표준 방법론의 타당성(validity) 검증 연구
  - 에이전트의 의사결정 과정(어떤 데이터 소스를 왜 선택했는가)에 대한 해석가능성(interpretability) 강화
  - 정보 보안 및 데이터 프라이버시 문제에 대한 거버넌스 프레임워크 개발

## Evaluation

- **Novelty**: 4/5
  - LLM 에이전트의 정치과학 적용은 새로우나, Agentic RAG 자체의 기술적 혁신성은 제한적(기존 개념의 응용)

- **Technical Soundness**: 3.5/5
  - 아키텍처 설계는 타당하나, CongressRA의 구체적 기술 상세(프롬프트 엔지니어링, 에러 핸들링, 성능 메트릭)가 불충분하게 제시됨

- **Significance**: 4/5
  - 정치기관 연구의 노동집약적 작업 자동화라는 높은 실용적 가치 제시하나, 아직 실증적 영향(다수의 연구자 채택, 논문 질 향상 등)은 검증 전 단계

- **Clarity**: 4/5
  - 전체적으로 명확하나, 기술 세부사항(데이터베이스 스키마, 함수 정의 방식)과 한계에 대한 설명이 다소 부족

- **Overall**: 4/5

**총평**: 본 논문은 LLM 에이전트의 정치과학 연구 적용이라는 실질적으로 중요한 주제를 다루며, Agentic RAG를 통한 해결책 제시와 CongressRA라는 구체적 구현 사례를 제공함으로써 학문 공동체에 기여한다. 다만 기술적 혁신성이 제한적이고, 할루시네이션 및 편향 문제에 대한 심화된 논의와 대규모 실증 검증이 추가될 필요가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/488_Leveraging_LLMs_in_Scholarly_Knowledge_Graph_Question_Answer/review]] — 정치기관 연구용 LLM 에이전트와 Leveraging LLMs in Scholarly Knowledge Graph QA는 모두 학술 연구 지원을 다루지만, 특정 도메인 특화와 지식그래프 기반 질의응답이라는 서로 다른 접근법을 취합니다.
- 🔗 후속 연구: [[papers/450_Knowledge_navigator_Llm-guided_browsing_framework_for_explor/review]] — CongressRA의 정치기관 연구 지원은 Knowledge Navigator의 탐색적 지식 발견 프레임워크를 정치학 도메인에 특화시켜 체계적인 연구 도구로 발전시킵니다.
