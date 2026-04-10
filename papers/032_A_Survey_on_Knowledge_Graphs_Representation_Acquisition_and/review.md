---
title: "032_A_Survey_on_Knowledge_Graphs_Representation_Acquisition_and"
authors:
  - "Shaoxiong Ji"
  - "Shirui Pan"
  - "E. Cambria"
  - "Pekka Marttinen"
  - "Philip S. Yu"
date: "2020"
doi: "10.1109/TNNLS.2021.3070843"
arxiv: ""
score: 4.0
essence: "본 논문은 지식 그래프(Knowledge Graph)의 표현 학습, 획득, 시간적 동적성, 응용을 포괄적으로 조사하는 설문 논문으로, 최신 딥러닝 기법을 통한 구조화된 지식 표현 및 추론 방법을 체계적으로 정리한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Hierarchical_Knowledge_Graphs"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ji et al._2020_A Survey on Knowledge Graphs Representation, Acquisition, and Applications.pdf"
---

# A Survey on Knowledge Graphs: Representation, Acquisition, and Applications

> **저자**: Shaoxiong Ji, Shirui Pan, E. Cambria, Pekka Marttinen, Philip S. Yu | **날짜**: 2020 | **DOI**: [10.1109/TNNLS.2021.3070843](https://doi.org/10.1109/TNNLS.2021.3070843)

---

## Essence

![Figure 2](figures/fig2.webp)

*Fig. 2: Categorization of research on knowledge graphs.*

본 논문은 지식 그래프(Knowledge Graph)의 표현 학습, 획득, 시간적 동적성, 응용을 포괄적으로 조사하는 설문 논문으로, 최신 딥러닝 기법을 통한 구조화된 지식 표현 및 추론 방법을 체계적으로 정리한다.

## Motivation

- **Known**: 지식 그래프는 의미 있는 엔티티-관계-엔티티 삼중쌍(triple)으로 구성된 구조화된 지식 표현으로, Google Knowledge Graph 등 대규모 상용 시스템에서 활용되고 있다. RDF, OWL 등 표준 프레임워크가 확립되어 있다.
- **Gap**: 기존 연구는 개별 기법(임베딩, 경로 추론, 규칙 기반 추론)에 분산되어 있으며, 메타 관계 학습, 상식 추론, 시간적 동적성을 다루는 통합적 관점이 부족하다.
- **Why**: 지식 그래프는 AI의 인지 능력과 인간 수준의 지능 달성을 위한 핵심 기술이며, 추천 시스템, 질문 응답, 정보 검색 등 다양한 실제 응용에서 성능 향상을 가능하게 한다.
- **Approach**: 네 가지 핵심 영역(표현 학습, 지식 획득, 시간적 지식 그래프, 지식인식 응용)을 유기적으로 연결하는 포괄적 분류체계를 제시하고, 각 영역의 최신 신경망 아키텍처와 방법론을 체계화한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2: Categorization of research on knowledge graphs.*

- **포괄적 분류체계**: 지식 그래프 연구를 표현 공간(representation space), 점수 함수(scoring function), 인코딩 모델(encoding models), 보조 정보(auxiliary information) 네 가지 관점에서 세분화
- **지식 획득 방법론**: 임베딩 기반 랭킹, 관계 경로 추론, 논리 규칙 추론, 메타 관계 학습을 통합적으로 검토
- **신흥 기술 포괄**: Transformer 기반 인코딩, Graph Neural Network 기반 전파, 강화학습 기반 경로 추론, 메타 학습 등 최신 기법 상세 분석
- **자료 및 구현 제공**: 다양한 작업에 대한 큐레이션된 데이터셋 목록과 오픈소스 라이브러리 제공으로 재현성 확보

## How


- 지식 그래프의 역사적 발전을 추적(의미망 → RDF/OWL → 현대 지식 그래프)
- KRL(Knowledge Representation Learning)을 네 가지 차원에서 분류: 표현 공간(벡터/행렬/텐서/초복소수), 점수 함수(거리 기반 vs 유사도 기반), 인코딩 모델(CNN/RNN/Transformer/GNN), 보조 정보(타입/경로/구조)
- 지식 완성(KGC)을 임베딩 기반, 경로 추론, 논리 규칙, 메타 학습으로 구분
- 엔티티 획득을 인식(recognition), 타입 지정(typing), 중복 제거(disambiguation), 정렬(alignment)로 세분화
- 관계 추출을 신경망 패러다임(CNN/RNN/attention/GNN)에 따라 분류
- 시간적 지식 그래프의 정적-동적 표현 학습 방법 검토
- 추천 시스템, 질문 응답, 링크 예측 등 응용 분야별 활용 방식 분석

## Originality

- 단편적 기법 중심 기존 설문과 달리, 표현-획득-시간성-응용을 유기적으로 연결하는 4단계 프레임워크 제시
- 표현 학습을 4가지 독립적 관점(공간/함수/모델/정보)으로 다중 분류하여 기술 간 관계성 명확화
- 메타 관계 학습, 상식 추론, 시간적 동적성 등 신흥 주제를 기존 체계에 통합
- Transformer, GNN, 강화학습 등 최신 딥러닝 기법의 지식 그래프 적용 현황을 체계적으로 정리
- 학술 연구와 실제 응용(Google/Microsoft)의 갭을 연결하는 관점 제시

## Limitation & Further Study

- **확장성 한계**: 대규모 지식 그래프(수십억 엔티티/관계)에 대한 학습 효율성, 메모리 최적화 방안이 충분히 논의되지 않음
- **불완전성 처리**: 현실의 지식 그래프는 오류와 중복이 많으나, 노이즈 강건성(noise robustness)에 대한 체계적 검토 부재
- **다중 언어 및 문화 편향**: 영어 중심 지식 그래프와 비영어권 지식의 통합, 문화적 관점의 차이 처리 미흡
- **추론의 해석성**: 신경망 기반 추론과 논리 기반 추론의 결합에서 의사결정 과정의 명확성 부족
- **시간적 추론의 정확성**: 시간적 동적성 모델링이 과거 이력에 의존적이어서 미래 예측 성능 제한
- **후속 연구 방향**: (1) 이질적 정보(멀티모달, 텍스트, 이미지)의 통합 표현, (2) 전이 학습과 도메인 적응 메커니즘, (3) 설명 가능 AI를 위한 신경-기호 하이브리드 접근, (4) 개인정보 보호를 고려한 연합 학습 방식

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 지식 그래프 연구의 포괄적 현황을 체계적으로 정리한 고수준의 설문으로, 정확한 분류체계와 신흥 기술의 포함으로 학자와 실무자 모두에게 가치 있는 참고 자료를 제공한다. 다만 현실적 확장성, 노이즈 강건성, 추론의 해석성 등 실무적 한계에 대한 심화 분석이 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/020_A_Review_of_Relational_Machine_Learning_for_Knowledge_Graphs/review]] — 관계형 기계학습과 지식 그래프의 표현 학습에 대한 이론적 기반을 제공한다.
- 🧪 응용 사례: [[papers/393_Graphusion_a_rag_framework_for_knowledge_graph_construction/review]] — 지식 그래프 구축을 위한 RAG 프레임워크로 본 서베이의 지식 표현 방법론을 실제 구현에 적용한다.
- 🔗 후속 연구: [[papers/448_Kgvalidator_A_framework_for_automatic_validation_of_knowledg/review]] — 지식 그래프의 자동 검증 프레임워크로 본 논문의 지식 획득 방법론을 확장한다.
- 🔗 후속 연구: [[papers/563_Multi-document_scientific_summarization_from_a_knowledge_gra/review]] — 지식 그래프의 표현과 획득에 대한 포괄적 조사를 과학 문서 요약에 특화된 지식 그래프 활용으로 확장한 응용 연구입니다.
