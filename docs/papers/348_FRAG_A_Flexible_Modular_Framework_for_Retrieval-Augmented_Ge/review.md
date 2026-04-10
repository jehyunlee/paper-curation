---
title: "348_FRAG_A_Flexible_Modular_Framework_for_Retrieval-Augmented_Ge"
authors:
  - "Zengyi Gao"
  - "Yukun Cao"
  - "Hairu Wang"
  - "Ao Ke"
  - "Yuan Feng"
date: "2025"
doi: "10.48550/arXiv.2501.09957"
arxiv: ""
score: 4.0
essence: "본 논문은 지식그래프(KG) 기반 검색증강생성(RAG) 시스템에서 유연성과 검색 품질 사이의 트레이드오프를 해결하기 위해 FRAG 프레임워크를 제안한다. 쿼리의 복잡도를 자동으로 판단하여 단순/복잡 추론 작업에 맞춤형 검색 전략을 적용함으로써 LLM 미세조정 없이 모듈식 설계의 유연성을 유지하면서도 검색 품질을 향상시킨다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Domain-adapted_Instruction_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Gao et al._2025_FRAG A Flexible Modular Framework for Retrieval-Augmented Generation based on Knowledge Graphs.pdf"
---

# FRAG: A Flexible Modular Framework for Retrieval-Augmented Generation based on Knowledge Graphs

> **저자**: Zengyi Gao, Yukun Cao, Hairu Wang, Ao Ke, Yuan Feng | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2501.09957](https://doi.org/10.48550/arXiv.2501.09957)

---

## Essence

![Figure 1: Modular and Coupled KG-RAG Frameworks](figures/fig1.webp)
*Modular과 Coupled KG-RAG 프레임워크의 구조적 차이*

본 논문은 지식그래프(KG) 기반 검색증강생성(RAG) 시스템에서 유연성과 검색 품질 사이의 트레이드오프를 해결하기 위해 FRAG 프레임워크를 제안한다. 쿼리의 복잡도를 자동으로 판단하여 단순/복잡 추론 작업에 맞춤형 검색 전략을 적용함으로써 LLM 미세조정 없이 모듈식 설계의 유연성을 유지하면서도 검색 품질을 향상시킨다.

## Motivation

- **Known**: KG-RAG는 LLM의 할루시네이션과 지식 부족을 완화하는 유망한 방법이며, 두 가지 주요 접근법이 존재한다.
  - *Modular KG-RAG*: 유연성과 확장성 우수, 고정된 검색 전략으로 인한 검색 품질 저하
  - *Coupled KG-RAG*: 검색 품질 향상, LLM 미세조정으로 인한 복잡성 증가, 유연성/확장성 손상

- **Gap**: 기존 방법들은 KG 구조 정보에 대한 사전 지식 부재로 인해 검색 및 랭킹 파라미터를 효과적으로 조정하지 못하거나, 이를 위해 LLM 미세조정이라는 높은 비용을 지불해야 한다.

- **Why**: 추론 경로의 **호프 수(hop count)** 같은 구조 정보는 KG뿐만 아니라 쿼리 자체와도 밀접한 관련이 있으며, 일반적으로 쿼리가 복잡할수록 더 많은 호프를 필요로 한다.

- **Approach**: 쿼리 텍스트만을 이용하여 추론 경로의 호프 범위를 예측하고 단순/복잡으로 분류한 후, 각 복잡도에 맞는 맞춤형 검색 파이프라인을 적용한다.

## Achievement

![Figure 2: Analysis of Semantic and Structural Information in Reasoning Paths](figures/fig2.webp)
*추론 경로의 의미론적(semantic) 정보와 구조적(structural) 정보 분석*

1. **유연성과 품질의 동시 달성**: LLM 미세조정 없이 모듈식 설계의 격리성, 유연성, 확장성을 유지하면서 동적 검색 전략으로 검색 품질 향상

2. **효율성 향상**: 추가 LLM 호출이나 미세조정이 필요 없어 자원 소비를 최소화하고 계산 효율성 극대화

3. **최첨단 성능**: 벤치마크 데이터셋에서 기존 방법들과 비교하여 우수한 성능 달성

## How

![Figure 3: Framework of FRAG](figures/fig3.webp)
*FRAG의 세 가지 주요 모듈 구조*

**1. Reasoning-Aware 모듈** (쿼리 복잡도 분류)
- 쿼리 컨텍스트에서 의미론적, 통계적 특징을 추출하여 교차 도메인 분류기 훈련
- 호프 수의 정확한 예측 대신 **coarse-grained 호프 범위**(단순/복잡)로 단순화하여 예측 오류 영향 최소화
- LLM 피드백을 활용한 최적화 전략으로 특정 KG에 대한 분류기 성능 개선

**2. Flexible-Retrieval 모듈** (맞춤형 검색 파이프라인)
- 전처리(Preprocessing) → 검색(Retrieval) → 후처리(Postprocessing) 3단계 파이프라인 설계
- **단순 추론**: BFS(Breadth-First Search) + 랭킹으로 짧은 경로의 효율적·정확한 검색
- **복잡 추론**: 최단 경로 검색(Shortest Path Retrieval) + 랭킹으로 계산 오버헤드 최소화 및 노이즈 감소

**3. Generation 모듈**
- 검색된 상위 k개 추론 경로를 이용하여 쿼리를 증강(augment)
- LLM으로 최종 출력 생성

## Originality

- **신규 관점**: 추론 경로의 의미론적 정보(KG 의존)와 구조적 정보(쿼리 의존)를 구분하고, 구조적 정보는 쿼리만으로 예측 가능함을 제시

- **경량 사전계산**: KG 미세조정 대신 쿼리 기반 호프 범위 예측만으로 검색 파라미터 최적화 달성

- **이중 적응 메커니즘**: 초기 교차 도메인 분류기 + LLM 피드백 기반 최적화로 일반성과 특정성 사이의 균형 추구

- **모듈식 유연성**: 전처리/검색/후처리 각 단계를 독립적으로 커스터마이징 가능한 구조로 다양한 KG와 도메인에 확장 용이

## Limitation & Further Study

**한계**:
- 호프 수의 coarse-grained 분류(단순/복잡)로 인한 정보 손실 가능성
- 임계값(δ) 설정의 도메인 민감성 미분석
- 극도로 길거나 매우 희소한 KG에서의 성능 보장 부족
- 쿼리 특징 추출의 한계(특정 도메인 특성이 강한 경우)

**후속 연구**:
- 더 세밀한 호프 범위 분류를 위한 다단계 분류기(multi-tier classifier) 개발
- 도메인별 최적 임계값 자동 결정 메커니즘
- 다언어 쿼리에 대한 확장 가능성 탐구
- 극단적 KG 규모(초대형 또는 초소형)에 대한 적응 메커니즘

## Evaluation

- **Novelty (독창성)**: 4/5
  - 쿼리 기반 구조 정보 예측이라는 새로운 관점 제시하나, 호프 분류 자체는 기존 연구에서 다루어진 개념
  
- **Technical Soundness (기술적 타당성)**: 4/5
  - 명확한 설계 원리와 논리적 파이프라인 구성이 우수하나, 예측 모델의 이론적 근거가 충분하지 않을 수 있음
  
- **Significance (의의)**: 4/5
  - 모듈식 KG-RAG의 주요 약점을 실질적으로 해결하고 리소스 효율성 측면에서 기여도 높음
  
- **Clarity (명확성)**: 4/5
  - 전체적인 프레임워크 설명은 명확하나, 일부 기술 상세(특히 LLM 피드백 최적화)의 설명이 부족
  
- **Overall (종합)**: 4/5

**총평**: FRAG는 모듈식 KG-RAG의 성능 한계를 쿼리 기반 호프 예측과 맞춤형 파이프라인으로 우아하게 해결하는 실용적 접근법이다. LLM 미세조정을 배제하면서도 검색 품질을 향상시키는 기여는 의미 있으나, 호프 분류의 세밀도와 도메인 적응성에 대한 더욱 심화된 분석이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/1092_Table-llm-specialist_Language_model_specialists_for_tables_u/review]] — 테이블 작업 전문가 모델과 달리 지식그래프 기반 RAG의 유연성을 통한 범용적 접근
- 🏛 기반 연구: [[papers/659_REALM_Retrieval-Augmented_Language_Model_Pre-Training/review]] — 검색증강 언어모델 사전훈련 방법론을 지식그래프 특화 RAG 시스템으로 발전시킨 기반
- 🔄 다른 접근: [[papers/393_Graphusion_a_rag_framework_for_knowledge_graph_construction/review]] — 지식그래프 구축에 중점을 둔 Graphusion과 달리 기존 KG 활용 최적화에 집중
- 🏛 기반 연구: [[papers/535_MetaOpenFOAM_an_LLM-based_multi-agent_framework_for_CFD/review]] — 검색 증강 생성의 유연한 모듈 프레임워크가 MetaOpenFOAM의 RAG 기술 기반 CFD 지식 검색 및 처리 시스템의 핵심 기술적 토대이다.
- 🔗 후속 연구: [[papers/659_REALM_Retrieval-Augmented_Language_Model_Pre-Training/review]] — REALM의 검색 증강 기법을 더 유연한 모듈형 프레임워크로 발전시킨 연구
- 🔄 다른 접근: [[papers/1092_Table-llm-specialist_Language_model_specialists_for_tables_u/review]] — RAG 프레임워크의 유연성 추구와 달리 테이블 작업에 특화된 전문 모델 개발 접근
