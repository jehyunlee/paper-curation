---
title: "789_Taxonomy_tree_generation_from_citation_graph"
authors:
  - "Yuntong Hu"
  - "Zhuofeng Li"
  - "Zheng Zhang"
  - "Ling Chen"
  - "Raasikh Kanjiani"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "인용 그래프(Citation Graph)로부터 계층적 분류 체계(Taxonomy Tree)를 자동으로 생성하는 엔드-투-엔드 프레임워크 HiGTL을 제안한다. 텍스트 콘텐츠와 인용 구조를 결합하여 의미론적으로 일관성 있고 구조적으로 응집력 있는 분류 체계를 구축한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Hierarchical_Knowledge_Graphs"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Hu et al._2024_Taxonomy tree generation from citation graph.pdf"
---

# Taxonomy tree generation from citation graph

> **저자**: Yuntong Hu, Zhuofeng Li, Zheng Zhang, Ling Chen, Raasikh Kanjiani, Boxin Zhao, Liang Zhao | **날짜**: 2024 | **DOI**: N/A

---

## Essence

인용 그래프(Citation Graph)로부터 계층적 분류 체계(Taxonomy Tree)를 자동으로 생성하는 엔드-투-엔드 프레임워크 HiGTL을 제안한다. 텍스트 콘텐츠와 인용 구조를 결합하여 의미론적으로 일관성 있고 구조적으로 응집력 있는 분류 체계를 구축한다.

## Motivation

- **Known**: 학술 문헌의 분류 체계는 문헌 검토, 지식 조직, 연구 트렌드 파악에 필수적이며, 기존 택소노미 학습 기법들은 텍스트 기반의 언어 패턴 추출에 초점을 맞추고 있음.

- **Gap**: 기존 택소노미 학습 방법들은 일반 텍스트 코퍼스를 위해 설계되었으며, 그래프의 연결성(connectivity)과 커뮤니티 구조를 활용할 수 없어 인용 그래프로부터의 택소노미 생성에는 부적합함. 또한 수작업으로 택소노미를 구축하는 것은 노동집약적이고 인간의 편향을 포함함.

- **Why**: 인용 그래프는 (1) 관련된 논문들 간의 인용 관계 정보와 (2) 각 논문의 풍부한 텍스트 콘텐츠를 동시에 포함하므로, 두 모달리티를 효과적으로 통합하는 것이 필수적임. 또한 택소노미 노드를 의미론적으로 일관성 있게 표현하는 것도 도전과제임.

- **Approach**: 계층적 인용 그래프 클러스터링과 택소노미 노드 표현화(verbalization)의 두 하위 문제로 분해하고, 이를 결합 최적화 프레임워크로 통합하여 학습함.

## Achievement

![Figure 1: Citation graph와 Taxonomy의 계층적 대응 관계](figures/fig1.webp)

1. **계층적 그래프 클러스터링**: 텍스트 콘텐츠와 인용 구조를 모두 고려하여 재귀적으로 논문들을 그룹화하는 방법 제안. 각 레벨에서 하위 주제의 노드들을 상위 주제의 슈퍼노드로 클러스터링하면서 특성 집계(feature aggregation)를 통해 의미론적 일관성 유지.

2. **택소노미 노드 표현화**: 대규모 언어 모델(LLM)을 활용하여 각 클러스터의 중심 개념을 반복적으로 생성하는 전략 개발. 클러스터 레벨 그래프 임베딩과 논문 레벨 정보를 결합하여 계층 구조 전체에 걸쳐 의미론적으로 풍부한 및 일관성 있는 택소노미 생성.

3. **평가 데이터셋**: 컴퓨터 과학 분야의 고품질 인간 작성 문헌 리뷰에 대응하는 518개의 인용 그래프 수집 및 공개, 향후 연구를 위한 벤치마크 제공.

## How

![Figure 2: 계층적 택소노미 생성 프레임워크의 전체 구조](figures/fig2.webp)

- **문제 분해**: 택소노미 생성을 계층 구조 유도 함수 g와 개념 추상화 함수 h의 합성으로 표현 (f = h∘g)

- **계층적 클러스터링 모듈**: 
  - 인용 그래프를 텍스트 임베딩(BERT 기반)과 그래프 구조 정보를 결합하여 재귀적으로 분해
  - 각 레벨에서 최소 신장 트리(MST) 기반 방법 또는 모듈성(modularity) 기반 커뮤니티 탐지 활용
  - 특성 집계를 통해 슈퍼노드의 표현 생성

- **택소노미 노드 표현화 모듈**:
  - Retrieval-Augmented Generation (RAG) 기법 활용
  - 각 클러스터의 상위 논문들 검색 후 LLM 프롬프팅으로 중심 개념 생성
  - 사용자 선호 주제(query q)를 프롬프트에 포함하여 관련성 강화

- **결합 최적화**:
  - Pre-training: 클러스터링 모듈의 가중치를 먼저 학습
  - Fine-tuning: 구조 정확도와 생성된 택소노미의 품질을 동시에 고려하여 매개변수 조정
  - Parameter-Efficient Fine-Tuning (PEFT) 기법(Adapters, LoRA) 활용으로 계산 효율성 확보

## Originality

- 인용 그래프를 입력으로 하는 자동 택소노미 생성이라는 새로운 문제 정의 및 엔드-투-엔드 솔루션 제시
- 그래프 위상 정보와 텍스트 의미 정보를 통합하는 계층적 클러스터링 기법의 novel 설계
- LLM 기반 계층적 개념 추상화 전략으로 의미론적 일관성을 보장하는 방법 개발
- 그래프 클러스터링과 LLM 기반 표현화를 결합 최적화하는 프레임워크 설계
- 518개의 고품질 인용 그래프 데이터셋 구축 및 공개로 벤치마크 제공

## Limitation & Further Study

- **데이터셋 한계**: 컴퓨터 과학 분야만 대상으로 하고 있어, 다른 학술 분야(생물학, 의학 등)로의 일반화 가능성은 미지수
- **클러스터링 제약**: 엄격한 트리 구조 요구로 인해 실제 인용 관계의 복잡한 다중 관계를 완전히 포착하지 못할 가능성
- **LLM 의존성**: 생성된 개념이 LLM의 사전 학습 데이터와 편향에 영향을 받을 수 있음
- **확장성**: 초대규모 인용 그래프(수백만 개 논문)에 대한 성능과 계산 비용 미실험
- **후속 연구**:
  - 방향성 비순환 그래프(DAG) 구조 지원으로 다중 부모-자식 관계 허용
  - 다국어 및 다분야 데이터셋 확장
  - 동적 인용 그래프(시간 경과에 따른 변화)에 대한 적응형 택소노미 생성
  - 인터랙티브 사용자 피드백 통합으로 택소노미 개선 메커니즘 개발

## Evaluation

- **Novelty**: 4/5 
  - 인용 그래프 기반 택소노미 생성이라는 새로운 문제 정의와 다중 모달 통합 접근이 신규적이나, 개별 기술 요소들(그래프 클러스터링, LLM 프롬팅, PEFT)은 기존 기법의 조합

- **Technical Soundness**: 4/5 
  - 계층적 클러스터링과 LLM 기반 표현화의 결합이 합리적이고 실험이 충분하나, 이론적 수렴 보장이나 최적성에 대한 분석 부재

- **Significance**: 4/5 
  - 자동 택소노미 생성은 학술 커뮤니티에 실질적 가치 제공하고, 고품질 벤치마크 데이터셋 공개의 의의는 크나, 현재로서는 컴퓨터 과학 분야 한정

- **Clarity**: 4/5 
  - 문제 정의와 방법론 설명이 명확하고 그림이 효과적이나, 일부 세부 구현 사항(프롬프트 엔지니어링, 하이퍼파라미터)의 기술이 부족

- **Overall**: 4/5

**총평**: 인용 그래프로부터 자동으로 고품질 분류 체계를 생성하는 실용적이고 체계적인 접근을 제시하며, 계층적 그래프 클러스터링과 LLM 기반 개념 생성의 결합이 효과적임을 입증했다. 다만 방법론의 다분야 일반화와 이론적 깊이 심화가 향후 과제로 남아있다.

## Related Papers

- 🔗 후속 연구: [[papers/742_Select_read_and_write_A_multi-agent_framework_of_full-text-b/review]] — 인용 그래프에서 생성된 분류 체계가 관련 연구 섹션 작성에서 문헌 간의 계층적 관계를 체계적으로 구조화하는 핵심 도구로 활용된다.
- 🔄 다른 접근: [[papers/752_Shallow_synthesis_of_knowledge_in_gpt-generated_texts_A_case/review]] — 구조적 인용 그래프 분석을 통한 체계적 분류 생성이 GPT의 얕은 문헌 종합 문제에 대한 대안적 해결 방안을 제시한다.
- 🏛 기반 연구: [[papers/330_Exploiting_LLMs_for_Automatic_Hypothesis_Assessment_via_a_Lo/review]] — 연구 논문 간의 관계 설명에 필요한 기본적인 분류 체계가 인용 그래프에서 자동으로 생성되어 체계적인 문헌 구조화를 가능하게 한다.
- 🏛 기반 연구: [[papers/215_Chime_Llm-assisted_hierarchical_organization_of_scientific_s/review]] — 인용 그래프에서 분류 체계 트리 생성 방법으로 본 논문의 계층적 트리 구조 조직화 기반을 제공한다.
- 🔄 다른 접근: [[papers/329_Explaining_relationships_among_research_papers/review]] — 인용 그래프에서 분류 체계 트리 생성으로 본 논문과 다른 방식의 논문 간 관계 구조화를 제시한다.
- 🏛 기반 연구: [[papers/742_Select_read_and_write_A_multi-agent_framework_of_full-text-b/review]] — 인용 그래프에서 분류 체계 생성이 관련 연구 섹션에서 참고 문헌 간의 관계를 체계적으로 구조화하는 기본 프레임워크를 제공한다.
- 🔄 다른 접근: [[papers/752_Shallow_synthesis_of_knowledge_in_gpt-generated_texts_A_case/review]] — 인용 그래프 분석과 분류 체계 생성은 문헌 종합의 구조적 한계를 극복하기 위한 대안적 접근 방법을 제시한다.
