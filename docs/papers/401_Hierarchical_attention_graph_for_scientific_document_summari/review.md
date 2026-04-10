---
title: "401_Hierarchical_attention_graph_for_scientific_document_summari"
authors:
  - "Chenlong Zhao"
  - "Xiwen Zhou"
  - "Xiaopeng Xie"
  - "Yong Zhang"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "과학 논문 같은 장문서의 추출 요약을 위해 그래프 신경망을 활용하여 **문장 내 관계(지역 수준)**와 **문장 간 고차 관계(전역 수준)**를 계층적으로 동시에 모델링하는 HAESum 방법 제시."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Scientific_Literature_Summarization"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhao et al._2024_Hierarchical attention graph for scientific document summarization in global and local level.pdf"
---

# Hierarchical attention graph for scientific document summarization in global and local level

> **저자**: Chenlong Zhao, Xiwen Zhou, Xiaopeng Xie, Yong Zhang | **날짜**: 2024 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) *문서의 지역(local)과 전역(global) 관점에서의 모델링 예시: 단어-문장 간 관계(intra-sentence)와 문장 간 관계(inter-sentence)를 계층적으로 구분*

과학 논문 같은 장문서의 추출 요약을 위해 그래프 신경망을 활용하여 **문장 내 관계(지역 수준)**와 **문장 간 고차 관계(전역 수준)**를 계층적으로 동시에 모델링하는 HAESum 방법 제시. 

## Motivation

- **Known**: 기존의 그래프 기반 추출 요약 방법들은 뛰어난 성과를 보여주고 있으며, 장문서 처리를 위해 GNN(Graph Neural Network)을 활용한 접근이 널리 사용됨

- **Gap**: (1) 기존 방법들은 문장 내 관계(intra-sentence) 또는 문장 간 쌍방향 관계에만 집중하고, **쌍(pair) 이상의 고차 관계(triplet, n-ary relations)**를 간과함. (2) 문서의 계층 구조(words → sentences → sections)를 동시에 반영하지 못하고 모든 수준의 관계를 동시에 업데이트함

- **Why**: 과학 논문의 계층 구조에서 같은 섹션의 문장들은 유사한 주제를 표현하므로, 순차적 하향식 모델링이 필수적. LLM의 "lost-in-the-middle" 현상과 Transformer의 이차 복잡도 문제도 존재

- **Approach**: 이질 그래프(heterogeneous graph)로 지역 수준의 문장-단어 관계를 학습한 후, 하이퍼그래프 자기주의(hypergraph self-attention) 레이어로 문장 간 고차 관계를 포착하는 두 단계 계층적 접근

## Achievement

![Figure 2](figures/fig2.webp) *HAESum 프레임워크 개요: (좌) 지역 수준 이질 그래프(HEGAT)에서 문장-단어 양방향 메시지 패싱, (우) 전역 수준 하이퍼그래프 자기주의(HGSAT)에서 고차 문장 관계 포착*

1. **첫 계층적 GNN 기반 추출 요약 모델**: 기존과 달리 문장 내 관계와 문장 간 관계를 **분리된 그래프에서 순차적으로** 학습하는 방식으로 계층 구조를 효과적으로 활용

2. **새로운 하이퍼그래프 자기주의 레이어**: 노드뿐 아니라 **하이퍼엣지(hyperedge)를 명시적으로** 표현하여 고차 문장 관계를 포착. 사전훈련 모델에 의존하지 않아 저자원 언어 적용 가능

3. **벤치마크 검증**: Arxiv, PubMed 두 데이터셋에서 기존 방법들 대비 효과성 입증

## How

- **지역 수준(Local Level) - 이질 그래프 주의(Heterogeneous Graph Attention, HEGAT)**:
  - 노드: 문서의 모든 단어(Vw)와 문장(Vs)으로 구성
  - 초기화: GloVe로 단어 임베딩, CNN(n-gram 특징) + BiLSTM 연결로 문장 표현 생성
  - 업데이트: 두 단계 메시지 패싱 수행
    1) 문장 주변 단어로부터 정보 집계→단어 표현 갱신 (식 1-4)
    2) 갱신된 단어로부터 문장 표현 업데이트
  - 주의 계수: LeakyReLU + softmax로 계산, 다중 헤드 주의 및 피드포워드 층 포함

- **전역 수준(Global Level) - 하이퍼그래프 자기주의(Hypergraph Self-Attention, HGSAT)**:
  - 하이퍼그래프 구성: 노드는 문장, 하이퍼엣지는 다중 문장 그룹을 연결
  - 엣지-노드 관계를 명시적으로 모델링하여 고차 상호작용 포착
  - 자기주의 메커니즘으로 최종 문장 표현 생성

- **예측**: MLP로 이진 분류(포함/제외) 수행

## Originality

- **계층적 분리 전략**: 단일 그래프에서 모든 관계를 동시 업데이트하는 기존 방식과 달리, 지역 수준(이질 그래프)과 전역 수준(하이퍼그래프)을 명확히 분리하여 계층 구조를 활용

- **하이퍼그래프 자기주의**: 노드와 엣지를 동시에 고려하는 주의 메커니즘으로 쌍 이상의 고차 관계 포착 (기존의 쌍방향 관계만 고려하는 한계 극복)

- **사전훈련 모델 의존성 제거**: CNN+BiLSTM으로 문장 표현을 생성하여 Transformer 기반 인코더에 의존하지 않음 → 저자원 언어 적용성 향상

## Limitation & Further Study

- **문서 길이 제한**: 실험에서 다루는 최대 문서 길이 및 성능 감소 시점에 대한 명시적 분석 부재

- **하이퍼엣지 구성 방식**: 논문에서 하이퍼엣지 생성 기준(유사도, 거리, 섹션 정보 등)이 명확하지 않음. 이에 대한 민감도 분석 필요

- **계산 복잡도**: 이질 그래프와 하이퍼그래프를 순차 처리하므로 매우 장문서에서의 효율성 검토 필요

- **후속 연구**: 
  - 동적 하이퍼엣지 구성 메커니즘 개발
  - 추상 요약(abstractive summarization)으로 확장
  - 다국어 및 다영역 문서 적용 평가

## Evaluation

- **Novelty**: 4/5 — 계층적 분리 전략과 하이퍼그래프 자기주의는 참신하나, GNN 기반 요약의 전반적 프레임은 기존 연구의 점진적 개선

- **Technical Soundness**: 4/5 — 방법론 구성은 논리적이나 하이퍼엣지 구성 세부사항과 복잡도 분석이 불충분

- **Significance**: 4/5 — 과학 논문 같은 장문서 요약에 실질적 기여가 있으나, LLM 대비 명확한 이점 제시 부족

- **Clarity**: 3.5/5 — 전체 흐름은 명확하나, 하이퍼그래프 자기주의 수식 및 구현 세부사항(특히 엣지-노드 주의 계산)의 설명이 불완전

- **Overall**: 4/5

**총평**: 과학 논문 추출 요약을 위해 계층 구조를 효과적으로 활용하는 참신한 접근으로, 지역-전역 수준의 분리적 모델링이 강점이나, 하이퍼엣지 구성의 명시성 부재와 LLM 시대의 의의 제시 보완이 필요함.

## Related Papers

- 🔄 다른 접근: [[papers/563_Multi-document_scientific_summarization_from_a_knowledge_gra/review]] — 과학 문서 요약에서 계층적 어텐션 그래프와 지식 그래프 중심 접근법의 성능을 비교할 수 있습니다.
- 🔗 후속 연구: [[papers/573_Neural_related_work_summarization_with_a_joint_context-drive/review]] — 관련 연구 요약에서 단순 문맥 주의 메커니즘을 계층적 그래프 구조로 발전시킨 진보된 방법입니다.
- 🧪 응용 사례: [[papers/812_TLDR_Extreme_Summarization_of_Scientific_Documents/review]] — 과학 문서의 극한 요약에 계층적 관계 모델링을 적용하여 더 정확한 요약을 생성할 수 있습니다.
- 🔄 다른 접근: [[papers/563_Multi-document_scientific_summarization_from_a_knowledge_gra/review]] — 과학 문서 요약에서 지식 그래프 중심 접근법과 계층적 어텐션 그래프 방식의 서로 다른 구조적 모델링을 비교할 수 있습니다.
- 🏛 기반 연구: [[papers/573_Neural_related_work_summarization_with_a_joint_context-drive/review]] — 문맥 기반 주의 메커니즘이 계층적 어텐션 그래프의 지역-전역 관계 모델링에 기초적인 방법론을 제공합니다.
