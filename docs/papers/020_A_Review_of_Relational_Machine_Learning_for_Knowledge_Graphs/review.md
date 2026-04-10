---
title: "020_A_Review_of_Relational_Machine_Learning_for_Knowledge_Graphs"
authors:
  - "Maximilian Nickel"
  - "K. Murphy"
  - "Volker Tresp"
  - "E. Gabrilovich"
date: "2015"
doi: "10.1109/JPROC.2015.2483592"
arxiv: ""
score: 4.0
essence: "본 논문은 지식 그래프(Knowledge Graphs)에 대한 관계형 기계학습(Relational Machine Learning) 기법들을 종합적으로 검토하며, 잠재 특성 모델(Latent Feature Models)과 그래프 패턴 마이닝 기반 모델을 통해 누락된 사실(엣지)을 예측하는 방법을 제시한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Hierarchical_Knowledge_Graphs"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Nickel et al._2015_A Review of Relational Machine Learning for Knowledge Graphs.pdf"
---

# A Review of Relational Machine Learning for Knowledge Graphs

> **저자**: Maximilian Nickel, K. Murphy, Volker Tresp, E. Gabrilovich | **날짜**: 2015 | **DOI**: [10.1109/JPROC.2015.2483592](https://doi.org/10.1109/JPROC.2015.2483592)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1. Sample knowledge graph. Nodes represent entities, edge labels represent*

본 논문은 지식 그래프(Knowledge Graphs)에 대한 관계형 기계학습(Relational Machine Learning) 기법들을 종합적으로 검토하며, 잠재 특성 모델(Latent Feature Models)과 그래프 패턴 마이닝 기반 모델을 통해 누락된 사실(엣지)을 예측하는 방법을 제시한다.

## Motivation

- **Known**: 지식 그래프는 엔티티와 관계를 (주어, 술어, 목적어) 삼중항으로 표현하는 구조화된 지식베이스이며, YAGO, DBpedia, Freebase 등 대규모 공개 지식 그래프들이 존재한다. 전통적 기계학습은 특성 벡터 기반이지만 관계형 데이터는 그래프 구조를 가진다.
- **Gap**: 대규모 지식 그래프의 불완전성(completeness) 문제를 해결하고, 텍스트 기반 정보 추출과 통계적 관계형 모델을 효과적으로 결합하여 자동 지식베이스 구축을 수행하는 확장 가능한 방법론의 부족이 있다.
- **Why**: 지식 그래프의 누락된 사실 예측은 웹에서 자동으로 추출한 노이즈가 있는 정보의 신뢰성을 검증할 수 있게 하며, 이를 통해 완전하고 정확한 지식베이스를 자동으로 구축할 수 있다.
- **Approach**: 논문은 (1) 텐서 분해와 신경망 기반의 잠재 특성 모델, (2) 관찰 가능한 그래프 패턴 기반 모델, (3) 두 가지 접근법의 결합을 제시하며, 이들을 Google의 Knowledge Vault 프로젝트와 같은 실제 시스템에 적용한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Fig. 1. Sample knowledge graph. Nodes represent entities, edge labels represent*

- **관계형 기계학습 프레임워크**: 통계적 관계형 학습(SRL)을 지식 그래프에 적용하여 누락된 엣지 예측, 노드 속성 예측, 연결성 기반 클러스터링 등의 작업을 수행할 수 있는 체계적 방법론 제시
- **이중 모델 아키텍처**: 잠재 특성 모델(RESCAL, 신경망)과 관찰 가능 패턴 모델의 장점을 결합하여 예측 성능과 계산 효율성의 균형 달성
- **확장성 있는 기법**: 지식 그래프의 수백만 노드와 수십억 엣지 규모에 적용 가능한 선형 시간 복잡도의 알고리즘 제시
- **자동 지식베이스 구축 파이프라인**: 정보 추출과 통계적 모델을 결합하여 웹에서 추출한 노이즈가 있는 사실들의 신뢰성을 자동으로 검증하고 필터링하는 방법 제시

## How

![Figure 3](figures/fig3.webp)

*Fig. 3. Tensor representation of binary relational data.*

- - 지식 그래프를 3-모드 텐서로 표현하여 텐서 분해(Tensor Factorization) 기법 적용
- - 다층 신경망(Multiway Neural Networks)을 이용한 엔티티 임베딩 학습
- - 그래프의 부분구조(substructure)와 경로 패턴(path patterns)을 기반으로 한 규칙 마이닝
- - 잠재 특성과 관찰 가능 패턴을 결합한 하이브리드 모델 구성
- - 마르코프 확률장(Markov Random Fields)을 이용한 관계형 확률 모델링
- - 정보 추출 결과와 관계형 기계학습 모델의 신뢰도 점수(confidence scores) 결합

## Originality

- - 대규모 지식 그래프에 특화된 관계형 기계학습 프레임워크의 최초 종합 검토
- - 잠재 특성 모델과 그래프 패턴 모델을 이론적/실증적으로 결합한 새로운 접근법
- - 개방 세계 가정(Open World Assumption)과 지역 폐쇄 세계 가정(Local Closed World Assumption)의 명시적 구분 및 적용
- - 텍스트 기반 정보 추출과 통계적 관계형 모델의 통합 파이프라인 제시
- - Google Knowledge Vault와 같은 대규모 실제 시스템 구현 사례 분석

## Limitation & Further Study

- - 고차 관계(higher-arity relations)를 기본적으로 지원하지 않으며 2진 관계(binary relations)에 중점
- - 동적 지식 그래프나 시간적 정보의 변화를 모델링하는 방법 부족
- - 잠재 특성 모델의 해석가능성(interpretability) 문제로 인한 실무 적용의 어려움
- - 정보 추출 방법의 노이즈와 편향(bias)이 최종 모델 성능에 미치는 영향에 대한 심화 분석 필요
- - 다국어 또는 멀티모달 지식 그래프로의 확장 방법론 개발 필요
- - 후속 연구로 신경망 임베딩의 개선, 엣지 타입 예측, 관계형 학습과 깊은 학습의 통합 등이 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 지식 그래프 분야의 핵심 기술과 이론을 포괄적으로 정리한 중요한 종합 리뷰로, 관계형 기계학습의 두 가지 주요 패러다임을 체계적으로 제시하고 실제 대규모 시스템 적용 사례를 통해 실용성을 입증했다.

## Related Papers

- 🏛 기반 연구: [[papers/434_Interesting_Scientific_Idea_Generation_using_Knowledge_Graph/review]] — 지식 그래프의 관계형 기계학습에 대한 체계적 검토가 과학 아이디어 생성을 위한 지식 그래프 활용의 이론적 토대를 제공함
- 🏛 기반 연구: [[papers/393_Graphusion_a_rag_framework_for_knowledge_graph_construction/review]] — 관계형 기계학습의 이론적 기초가 지식 그래프 구축을 위한 RAG 프레임워크 개발의 방법론적 배경을 제공함
- 🏛 기반 연구: [[papers/066_Agentic_Personas_for_Adaptive_Scientific_Explanations_with_K/review]] — 지식 그래프 관계형 머신러닝 리뷰는 Agentic Personas의 지식그래프 기반 설명 생성 시스템 설계에 핵심적인 이론적 배경을 제공한다.
- 🏛 기반 연구: [[papers/393_Graphusion_a_rag_framework_for_knowledge_graph_construction/review]] — 지식 그래프를 위한 관계형 기계학습 리뷰가 과학 지식그래프 구축의 이론적 토대를 제공합니다.
- 🏛 기반 연구: [[papers/882_When_large_language_models_meet_citation_A_survey/review]] — 지식 그래프와 관계형 머신러닝 기반이 LLM-인용 분석 결합의 이론적 토대를 제공한다.
- 🏛 기반 연구: [[papers/448_Kgvalidator_A_framework_for_automatic_validation_of_knowledg/review]] — 지식 그래프를 위한 관계형 기계학습에 대한 포괄적 리뷰로 이론적 기반을 제공한다.
- 🏛 기반 연구: [[papers/032_A_Survey_on_Knowledge_Graphs_Representation_Acquisition_and/review]] — 관계형 기계학습과 지식 그래프의 표현 학습에 대한 이론적 기반을 제공한다.
