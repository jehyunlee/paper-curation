---
title: "563_Multi-document_scientific_summarization_from_a_knowledge_gra"
authors:
  - "Pancheng Wang"
  - "Shasha Li"
  - "Kunyuan Pang"
  - "Liangliang He"
  - "Dong Li"
date: "2022"
doi: "미제공"
arxiv: ""
score: 4.0
essence: "본 논문은 지식 그래프(Knowledge Graph, KG)를 중심으로 다중 문서 과학 논문 요약(Multi-Document Scientific Summarization, MDSS)을 수행하는 KGSum 모델을 제안한다. 인코딩과 디코딩 전 과정에서 지식 그래프를 활용하여 논문의 주요 내용과 논문 간 관계를 효과적으로 모델링한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Scientific_Literature_Summarization"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2022_Multi-document scientific summarization from a knowledge graph-centric view.pdf"
---

# Multi-document scientific summarization from a knowledge graph-centric view

> **저자**: Pancheng Wang, Shasha Li, Kunyuan Pang, Liangliang He, Dong Li, Jintao Tang, Ting Wang | **날짜**: 2022 | **DOI**: [미제공](https://doi.org/)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: 입력 과학 논문의 초록과 금표준 요약에서 구성된 지식 그래프*

본 논문은 지식 그래프(Knowledge Graph, KG)를 중심으로 다중 문서 과학 논문 요약(Multi-Document Scientific Summarization, MDSS)을 수행하는 KGSum 모델을 제안한다. 인코딩과 디코딩 전 과정에서 지식 그래프를 활용하여 논문의 주요 내용과 논문 간 관계를 효과적으로 모델링한다.

## Motivation

- **Known**: 기존 MDSS 방법들은 모든 텍스트 단위를 동등하게 처리하거나, seq2seq 모델로 논문 간 관계를 포착하려 시도했으나 세분화된 텍스트 단위 간의 명시적 링크를 고려하지 않음

- **Gap**: (1) 과학 논문의 복잡한 개념, 기술 용어, 약자 등 저빈도 정보를 놓침 (2) 논문 간의 순차적, 병렬적, 보완적, 대조적 관계를 효과적으로 모델링하지 못함

- **Why**: 지식 그래프는 도메인 특화 개체(entity)와 관계(relation)를 통해 논문의 핵심 내용을 컴팩트하게 표현하며, 개체 상호작용을 통해 논문 간 관계를 자연스럽게 포착할 수 있음

- **Approach**: 인코딩 단계에서 그래프 업데이터(Graph Updater)와 개체-문장 업데이터(Entity-Sentence Updater)를 통해 지식 그래프 정보를 논문 표현에 통합하고, 디코딩 단계에서는 두 단계 디코더를 제안하여 먼저 요약의 지식 그래프를 서술 문장 형태(KGtext)로 생성한 후 최종 요약을 생성

## Achievement

![Figure 2](figures/fig2.webp)
*Figure 2: 제안된 모델의 전체 프레임워크*

1. **지식 그래프 중심 MDSS 모델**: 다중 입력 논문의 지식 그래프를 하나의 통합 그래프로 융합하고, 그래프 트랜스포머를 활용하여 개체와 관계 표현을 학습함으로써 논문 내용과 논문 간 관계를 동시에 모델링

2. **두 단계 디코더 구조**: KGtext 생성기(KGtext Generator)에서 요약의 지식 그래프를 서술 문장으로 변환하고, 요약 생성기(Summary Generator)에서 이를 가이드로 최종 요약을 생성하는 이원적 구조로 중간 지식 정보를 활용

3. **Multi-XScience 데이터셋에서 우수한 성능**: 자동 평가(ROUGE, 개체 매칭) 및 인간 평가를 통해 기존 베이스라인 대비 상당한 개선을 달성

## How

- **지식 그래프 구성**: DYGIE++(과학 도메인 정보 추출 시스템)을 사용하여 개체(Task, Method, Metric, Material, Generic, OtherScientificTerm), 관계(Compare, Used-for, Feature-of, Hyponym-of, Evaluate-for, Part-of, Conjunction)를 추출하고 Levi 변환을 적용하여 레이블 없는 방향 그래프로 변환

- **그래프 업데이터**: 토큰 수준 Transformer 인코딩을 통해 개체 표현을 초기화하고, Graph Transformer를 사용하여 다중 헤드 자기주의(Multi-head Self-Attention)로 각 노드를 문맥화하여 지식 그래프 표현 학습

- **개체-문장 업데이터**: 이질적 그래프(Heterogeneous Graph)를 구성하여 개체 노드와 문장 노드 간의 정보 흐름을 통해 문장 표현을 업데이트

- **KGtext 생성기**: 마스크된 자기주의(Masked Self-Attention)와 복사 주의(Copy Attention)를 활용하여 요약의 지식 그래프를 자연 언어 형태로 생성

- **요약 생성기**: KGtext 컨텍스트와 그래프 컨텍스트를 모두 활용하는 교차 주의(Cross-Graph Attention, Cross-KGtext Attention) 메커니즘으로 최종 요약 생성

## Originality

- **새로운 관점**: 지식 그래프를 인코딩과 디코딩의 중심으로 하는 MDSS 접근법은 이전 연구들과 차별화됨

- **중간 표현 활용**: KGtext를 명시적 중간 출력으로 도입하여 지식 구조 정보가 최종 요약 생성에 직접 영향을 미치도록 설계

- **다중 그래프 활용**: 논문의 지식 그래프뿐만 아니라 개체-문장 이질적 그래프를 동시에 활용하여 다층적 정보 모델링 구현

- **정보 보존**: Levi 변환을 통해 레이블 있는 그래프를 정보 손실 없이 무방향 그래프로 변환하면서도 구조 정보 유지

## Limitation & Further Study

- **제한사항**: 
  - 지식 그래프 구성이 DYGIE++ 추출기의 성능에 의존하므로 추출 오류가 누적될 수 있음
  - 계산 복잡도가 높아 대규모 논문 클러스터 처리에 확장성 제한 가능
  - 특정 도메인(과학 논문)에 최적화되어 있어 다른 분야로의 전이 학습 효과 미검증

- **후속 연구**:
  - 추출 오류 견고성 향상을 위한 그래프 노이즈 처리 메커니즘 개발
  - 계산 효율성을 위한 그래프 축약 또는 계층적 그래프 처리 방법 탐색
  - 다양한 도메인의 요약 작업으로 일반화 가능성 검증
  - 사용자 인터랙티브 요약 생성을 위한 확장

## Evaluation

- **Novelty**: 4.5/5
  - 지식 그래프를 MDSS의 중심으로 하는 접근법은 참신하나, 개별 컴포넌트(Graph Transformer, 이질적 그래프)는 기존 기술의 조합

- **Technical Soundness**: 4/5
  - 전체 아키텍처가 논리적으로 일관되고 기술적으로 타당하나, 그래프 구성 및 Levi 변환의 필요성에 대한 심화 분석 부족

- **Significance**: 4/5
  - Multi-XScience 벤치마크에서 의미 있는 성능 향상을 보였으며, MDSS 분야에 실질적 기여를 함. 다만 단일 데이터셋 평가로 일반화 가능성 제한

- **Clarity**: 3.5/5
  - 전반적 구조는 명확하나, KGtext 정의와 생성 방식이 다소 모호하며, 개체-문장 업데이터의 구체적 작동 메커니즘에 대한 설명 부족

- **Overall**: 4/5

**총평**: 본 논문은 지식 그래프 구조를 체계적으로 활용한 창의적인 MDSS 접근법을 제시하며, 두 단계 디코더 구조를 통해 중간 지식 표현을 명시적으로 활용하는 점이 인상적이다. 다만 추출 기반 지식 그래프의 노이즈 문제와 계산 복잡도 측면의 개선이 필요하며, 더 다양한 평가를 통한 일반화 가능성 검증이 요구된다.

## Related Papers

- 🔄 다른 접근: [[papers/401_Hierarchical_attention_graph_for_scientific_document_summari/review]] — 과학 문서 요약에서 지식 그래프 중심 접근법과 계층적 어텐션 그래프 방식의 서로 다른 구조적 모델링을 비교할 수 있습니다.
- 🏛 기반 연구: [[papers/573_Neural_related_work_summarization_with_a_joint_context-drive/review]] — 관련 연구 요약의 문맥-그래프 결합 주의 메커니즘이 지식 그래프 중심 다중 문서 요약의 기초 방법론을 제공합니다.
- 🔗 후속 연구: [[papers/032_A_Survey_on_Knowledge_Graphs_Representation_Acquisition_and/review]] — 지식 그래프의 표현과 획득에 대한 포괄적 조사를 과학 문서 요약에 특화된 지식 그래프 활용으로 확장한 응용 연구입니다.
- 🏛 기반 연구: [[papers/374_Generating_a_structured_summary_of_numerous_academic_papers/review]] — 지식 그래프 기반 의료 연구 다중 문서 요약으로 구조화된 요약 생성의 이론적 기반을 제공한다.
- 🏛 기반 연구: [[papers/385_Glimpse_Pragmatically_informative_multi-document_summarizati/review]] — 지식 그래프 기반 다중 문서 요약 기법으로 차별적 다중 문서 요약의 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/108_Ask_retrieve_summarize_A_modular_pipeline_for_scientific_lit/review]] — 지식 그래프에서 다중 문서 과학 요약을 수행하여 본 논문의 요약 방법론을 구조화된 지식과 결합한다.
- 🔄 다른 접근: [[papers/401_Hierarchical_attention_graph_for_scientific_document_summari/review]] — 과학 문서 요약에서 계층적 어텐션 그래프와 지식 그래프 중심 접근법의 성능을 비교할 수 있습니다.
- 🏛 기반 연구: [[papers/402_Hierarchical_catalogue_generation_for_literature_review_a_be/review]] — 다중 문서 요약의 지식 그래프 활용이 계층적 카탈로그 생성의 구조적 기반을 제공합니다.
- 🔄 다른 접근: [[papers/573_Neural_related_work_summarization_with_a_joint_context-drive/review]] — 관련 연구 요약에서 문맥-그래프 결합 주의와 지식 그래프 중심 접근법의 서로 다른 구조적 모델링을 비교할 수 있습니다.
