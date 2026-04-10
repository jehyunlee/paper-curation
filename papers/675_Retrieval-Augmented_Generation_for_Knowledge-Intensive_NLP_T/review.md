---
title: "675_Retrieval-Augmented_Generation_for_Knowledge-Intensive_NLP_T"
authors:
  - "Yunfan Gao"
  - "Yun Xiong"
  - "Xinyu Gao"
  - "Kangxiang Jia"
  - "Jin Pan"
date: "2023"
doi: "N/A"
arxiv: ""
score: 4.3
essence: "대규모 언어모델(LLM)의 환각(hallucination), 지식 노후화, 추론 과정의 불투명성을 해결하기 위해 외부 데이터베이스에서 관련 정보를 검색하여 생성 과정을 보강하는 **Retrieval-Augmented Generation (RAG)** 기술을 종합적으로 분석한 논문이다. 본 논문은 RAG의 발전 단계를 Naive RAG, Advanced RAG, Modular RAG로 체계화하고 각 단계의 핵심 기술과 평가 방법론을 상세히 제시한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Retrieval-augmented_Generation_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Gao et al._2023_Retrieval-Augmented Generation for Large Language Models A Survey.pdf"
---

# Retrieval-Augmented Generation for Large Language Models: A Survey

> **저자**: Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jin Pan | **날짜**: 2023 | **DOI**: N/A

---

## Essence

![Figure 2](figures/fig1.webp) 
*그림 2: 질의응답에 적용된 RAG 프로세스 - 인덱싱, 검색, 생성의 3단계*

대규모 언어모델(LLM)의 환각(hallucination), 지식 노후화, 추론 과정의 불투명성을 해결하기 위해 외부 데이터베이스에서 관련 정보를 검색하여 생성 과정을 보강하는 **Retrieval-Augmented Generation (RAG)** 기술을 종합적으로 분석한 논문이다. 본 논문은 RAG의 발전 단계를 Naive RAG, Advanced RAG, Modular RAG로 체계화하고 각 단계의 핵심 기술과 평가 방법론을 상세히 제시한다.

## Motivation

- **Known**: 
  - LLM은 뛰어난 성능을 보이지만 학습 데이터 범위 밖의 질문에 대해 사실적으로 부정확한 내용을 생성하는 문제 발생
  - ChatGPT의 등장 이후 RAG 연구가 급속도로 증가했으나 체계적인 종합 분석 부재

- **Gap**: 
  - 기존 연구는 개별 RAG 방법론 제시에 중점을 두고 있으나, RAG의 진화 과정, 핵심 기술 통합, 평가 체계에 대한 종합적 정리 부족
  - 100건 이상의 RAG 관련 논문이 산재되어 있으나 통일된 분류 체계 및 기술 트리(technology tree) 부재

- **Why**: 
  - 현업 적용을 위해서는 RAG의 각 구성 단계(Retrieval, Generation, Augmentation)의 기술적 특성과 한계를 명확히 이해 필요
  - 다양한 도메인별 평가 지표 및 벤치마크에 대한 체계적 정리가 필요

- **Approach**: 
  - RAG 패러다임의 진화 과정을 3단계로 분류하여 설명
  - 검색(Retrieval), 생성(Generation), 보강(Augmentation)의 3가지 핵심 기술 깊이 있게 분석
  - 26개 작업, 약 50개 데이터셋, 평가 지표 및 벤치마크 종합 정리

## Achievement

![Figure 1](figures/fig1.webp)
*그림 1: RAG 연구의 기술 트리 - 사전학습, 파인튜닝, 추론 단계별 RAG 적용*

![Figure 3](figures/fig1.webp)
*그림 3: 세 가지 RAG 패러다임 비교 - Naive RAG(순차적), Advanced RAG(최적화), Modular RAG(모듈식)*

1. **체계적 패러다임 분류**: 
   - **Naive RAG**: 인덱싱 → 검색 → 생성의 기본 3단계 프로세스로 단순하지만 검색 정확도, 생성 환각, 정보 통합의 문제 존재
   - **Advanced RAG**: 사전 검색 최적화(쿼리 재작성, 확장) 및 사후 검색 처리(재순위화, 컨텍스트 압축)로 Naive RAG의 한계 보완
   - **Modular RAG**: 모듈식 설계로 반복 검색, 적응형 검색, 모듈 교체 등 유연한 구조 제공

2. **핵심 기술 통합 분석**: 
   - 임베딩 최적화, 인덱싱 기법, 쿼리 변환, 재순위화, 컨텍스트 압축, 파인튜닝 등 각 단계별 세부 기술 분류
   - 검색과 생성 간의 시너지 효과 및 각 기술의 상호작용 메커니즘 명시

3. **포괄적 평가 체계 제시**: 
   - 26개 다운스트림 태스크, 약 50개 데이터셋 및 평가 지표 정리
   - 현존 벤치마크(TREC, MS MARCO, SQuAD 등) 및 평가 도구 분류

## How

- **Naive RAG의 3단계 구조**:
  - 인덱싱(Indexing): 원본 문서 정제 → 청크 분할 → 벡터 임베딩 → 벡터 데이터베이스 저장
  - 검색(Retrieval): 쿼리 벡터화 → 유사도 계산 → Top-K 청크 반환
  - 생성(Generation): 쿼리 + 검색 결과 → 프롬프트 구성 → LLM 응답 생성

- **Advanced RAG의 개선 전략**:
  - 사전 검색 최적화: 슬라이딩 윈도우, 세밀한 청크 분할, 메타데이터 추가, 쿼리 재작성/확장
  - 사후 검색 처리: 검색 결과 재순위화(가장 관련성 높은 정보를 프롬프트 중앙에 배치), 컨텍스트 압축으로 정보 오버로드 완화

- **Modular RAG의 유연한 구조**:
  - 유사도 검색 모듈, 파인튜닝 검색기, 재구성된 RAG 모듈, 재배열된 파이프라인 등 다양한 전략 조합 가능
  - 순차 검색뿐 아니라 반복적(iterative), 적응형(adaptive) 검색 포함

## Originality

- **체계적 분류 체계의 부재 해결**: 100건 이상의 산재된 RAG 연구를 Naive → Advanced → Modular의 진화 구도로 명확히 정리한 최초의 종합 조사

- **기술 트리(Technology Tree) 제시**: 사전학습, 파인튜닝, 추론 단계별 RAG 적용 상황을 시각화하여 LLM 시대 RAG의 연구 방향을 체계화

- **삼각형 기술 분석 틀**: 검색(Retrieval), 생성(Generation), 보강(Augmentation)의 3가지 핵심 기술 영역을 독립적으로 분석하면서도 상호작용 분석으로 통합적 이해 제공

- **포괄적 평가 프레임워크**: 26개 태스크, 약 50개 데이터셋, 다양한 메트릭을 정리하여 RAG 평가의 표준화에 기여 가능한 자산 제공

## Limitation & Further Study

- **기술 깊이의 제한**: 
  - 각 개선 기법의 정량적 성능 비교 및 실험 결과 부재로 방법 간 우열 판단 어려움
  - 특정 태스크나 도메인에 어느 패러다임이 적합한지에 대한 상황별 가이드라인 부족

- **평가 체계의 통일성 문제**: 
  - 태스크마다 다양한 평가 메트릭 사용으로 인한 성능 비교의 어려움
  - RAG 특화 평가 메트릭(검색 정확도, 생성 충실도, 전체 시스템 효율성)의 표준화 부재

- **신규 기술 포괄의 한계**: 
  - 2023년 발행이므로 하이브리드 검색(Dense + Sparse), 그래프 기반 검색, LLM 기반 재순위화 등 그 이후 급속 발전한 기술 미포함

- **후속 연구 방향**:
  - 도메인 특화 평가 벤치마크 개발 및 표준화
  - 다중 단계 RAG 파이프라인의 최적화 방법론
  - 검색-생성 간 역량 균형 문제에 대한 이론적 분석
  - 비용-성능 트레이드오프 분석

## Evaluation

- **Novelty (독창성)**: 4/5
  - 체계적인 분류 체계와 기술 트리 제시는 신선하나, 개별 기술 자체는 기존 연구 종합

- **Technical Soundness (기술적 타당성)**: 4/5
  - RAG의 구조와 각 단계별 기술 설명은 명확하고 체계적이나, 정량적 실험 비교 부족

- **Significance (중요도)**: 5/5
  - LLM 시대 RAG의 필수적 이해 자료로 높은 학술·실무적 가치
  - 26개 태스크, 약 50개 데이터셋 정리로 벤치마킹에 직접 활용 가능

- **Clarity (명확성)**: 4.5/5
  - 그림과 텍스트의 조화로운 설명이지만, 복잡한 기술 간 상호작용 관계는 좀 더 상세한 시각화 필요

- **Overall**: 4.3/5

**총평**: 본 논문은 RAG 분야의 최초 대규모 종합 조사로서 체계적인 분류 체계와 기술 트리를 제시하여 학계와 산업계의 RAG 이해를 크게 향상시킨 의미 있는 기여를 했다. 다만 개별 기술의 정량적 성능 비교와 실무 적용 시 의사결정 가이드라인이 보강되면 더욱 가치 있는 자료가 될 것이다.

## Related Papers

- 🧪 응용 사례: [[papers/212_Chemist-X_Large_Language_Model-empowered_Agent_for_Reaction/review]] — RAG 기술을 화학 실험 자동화 시스템의 지식 검색 및 의사결정 지원에 적용할 수 있다
- 🔗 후속 연구: [[papers/593_Openscholar_Synthesizing_scientific_literature_with_retrieva/review]] — 과학 문헌 합성을 위한 검색 증강을 일반적인 RAG 시스템의 과학 특화 확장으로 발전시킬 수 있다
- 🔄 다른 접근: [[papers/602_Paperqa_Retrieval-augmented_generative_agent_for_scientific/review]] — 과학 논문 정보 처리를 위해 일반 RAG와 과학 특화 검색 증강 생성이라는 다른 접근법을 사용한다
- 🏛 기반 연구: [[papers/740_Search-R1_Training_LLMs_to_Reason_and_Leverage_Search_Engine/review]] — 검색 증강 생성 서베이는 Search-R1의 강화학습 기반 검색 통합 방법론에 RAG 시스템의 이론적 배경과 설계 원칙을 제공한다.
- 🏛 기반 연구: [[papers/212_Chemist-X_Large_Language_Model-empowered_Agent_for_Reaction/review]] — 검색 증강 생성 기술을 화학 합성 반응 최적화에 적용하기 위한 핵심 기반 기술을 제공한다
- 🔄 다른 접근: [[papers/034_A_Survey_on_RAG_Meeting_LLMs_Towards_Retrieval-Augmented_Lar/review]] — 대규모 언어모델을 위한 검색 증강 생성에 대한 다른 관점의 서베이를 제시한다.
- 🏛 기반 연구: [[papers/404_Hiperrag_High-performance_retrieval_augmented_generation_for/review]] — 대형 언어 모델을 위한 검색 증강 생성 서베이가 과학 문헌 특화 RAG 시스템 설계의 이론적 기반입니다.
- 🏛 기반 연구: [[papers/904_How_AI-powered_science_search_engines_can_speed_up_your_rese/review]] — LLM을 위한 검색증강 생성 조사가 AI 기반 과학 검색 엔진의 기술적 토대를 제공한다.
- 🏛 기반 연구: [[papers/651_RAG-Enhanced_Collaborative_LLM_Agents_for_Drug_Discovery/review]] — 검색 증강 생성의 일반적 방법론이 신약 발견을 위한 협력적 LLM 에이전트 시스템의 기술적 기반이다.
- 🔄 다른 접근: [[papers/295_Dynamic_multi-agent_orchestration_and_retrieval_for_multi-so/review]] — 대규모 언어모델을 위한 검색 증강 생성의 다른 체계적 접근 방법을 제시한다.
- 🏛 기반 연구: [[papers/659_REALM_Retrieval-Augmented_Language_Model_Pre-Training/review]] — REALM이 제시한 검색 증강 생성의 초기 방법론이 RAG 연구의 기초가 됨
