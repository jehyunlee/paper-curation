---
title: "580_Oag-bench_A_human-curated_benchmark_for_academic_graph_minin"
authors:
  - "Fanjin Zhang"
  - "Shijie Shi"
  - "Yifan Zhu"
  - "Bo Chen"
  - "Yukuo Cen"
date: "2024"
doi: "10.1145/3637528.3672354"
arxiv: ""
score: 4.4
essence: "본 논문은 학술 그래프 마이닝(academic graph mining)을 위한 포괄적인 인간-주석(human-curated) 벤치마크인 OAG-Bench를 제시한다. 개방학술그래프(Open Academic Graph, OAG)를 기반으로 저자 이름 중복 제거, 논문 추천, 학자 프로파일링 등 10개의 다양한 과제를 포함하며, 세밀한 다중 관점 주석과 표준화된 평가 프로토콜을 제공한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Knowledge_Graph_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhang et al._2024_Oag-bench A human-curated benchmark for academic graph mining.pdf"
---

# OAG-Bench: A Human-Curated Benchmark for Academic Graph Mining

> **저자**: Fanjin Zhang, Shijie Shi, Yifan Zhu, Bo Chen, Yukuo Cen, Jifan Yu, Yelin Chen, Lulu Wang, Qingfei Zhao, Yuqing Cheng, Tianyi David Han, Yuwei An, Dan Zhang, Weng Lam Tam, Kun Cao, Yunhe Pang, Xinyu Guan, Huihui Yuan, Jian Song, Xiaoyan Li | **날짜**: 2024 | **DOI**: [10.1145/3637528.3672354](https://doi.org/10.1145/3637528.3672354)

---

## Essence

![Figure 1](figures/fig1.webp) *그림 1: OAG-Bench의 포괄적 개요 - 10개 과제, 20개 데이터셋, 70+ 베이스라인 방법*

본 논문은 학술 그래프 마이닝(academic graph mining)을 위한 포괄적인 인간-주석(human-curated) 벤치마크인 OAG-Bench를 제시한다. 개방학술그래프(Open Academic Graph, OAG)를 기반으로 저자 이름 중복 제거, 논문 추천, 학자 프로파일링 등 10개의 다양한 과제를 포함하며, 세밀한 다중 관점 주석과 표준화된 평가 프로토콜을 제공한다.

## Motivation

- **Known**: 기존의 Microsoft Academic Graph (MAG), OAG 등 대규모 학술 그래프와 S2ORC, BLURB 같은 벤치마크들이 존재한다.

- **Gap**: 
  - 기존 학술 그래프는 다중 관점의 세밀한 주석이 부족하여 다양한 하위 과제 평가가 어렵다
  - 기존 벤치마크는 NLP 과제나 특정 도메인(예: 생명의학)에 제한되어 그래프 기반 과제를 포함하지 않는다
  - 분산된 데이터셋들은 대규모 종합 학술 그래프와 정렬되지 않아 실제 시나리오와 괴리가 있다

- **Why**: 과학 문헌의 급증으로 다목적 학술 지식 서비스가 종합적인 학술 그래프 마이닝을 필요로 하기 때문이다.

- **Approach**: OAG를 기반으로 학술 그래프 구성(5개 과제)과 응용(5개 과제)에 걸쳐 10개 과제를 정의하고, 새로운 주석 전략을 개발하며, 70+ 베이스라인 방법과 120+ 실험 결과를 제공한다.

## Achievement

![Figure 2](figures/fig1.webp) *그림 2: OAG-Bench의 전체 구성 프레임워크 - 학술 개체 구성에서 그래프 완성, 지식 획득, 추적 및 예측으로 진행*

1. **포괄적 벤치마크 자원**: 20개의 인간-주석 데이터셋(규모: 수천에서 수백만), 10개 과제, 70+ 베이스라인 방법으로 구성된 학술 그래프 마이닝의 전 생명주기(full life cycle)를 커버하는 벤치마크를 제공한다.

2. **새로운 주석 전략**: 불일치하는 논문-저자 할당 검출을 위해 출처 간 논문 할당 검사(cross-source paper assignment checking) 및 온라인 논문 읽기 그룹을 통한 논문 출처 표시 등의 혁신적인 주석 전략을 제안한다.

3. **엄격한 실험 검증**: LLM(Large Language Models)을 포함한 최신 알고리즘들도 논문 출처 추적(paper source tracing)과 학자 프로파일링(scholar profiling) 같은 핵심 과제에서 어려움을 겪는다는 것을 실험적으로 입증한다.

4. **완전한 개발 생태계**: 데이터 전처리 코드, 알고리즘 구현, 표준화된 평가 프로토콜, 리더보드를 제공하여 연구자들이 빠르게 시작할 수 있도록 지원한다.

## How

![Figure 2](figures/fig1.webp) *학술 개체 구성부터 응용까지의 단계별 프레임워크*

**OAG-Bench 프레임워크의 4단계 구조:**

1. **학술 개체 구성(Academic Entity Construction)**: 
   - 다양한 데이터 출처(Web, ACM, DBLP, ArXiv, MAG)에서 동일한 실제 개체 식별
   - 저자 이름 중복 제거(author name disambiguation) 과제 포함
   - 개체 정렬(entity alignment) 수행

2. **학술 그래프 완성(Academic Graph Completion)**:
   - 구성된 개체 간 연결 관계 확립
   - 학자 프로파일링(scholar profiling)을 통한 세밀한 레이블링
   - 개념 태깅(concept tagging), 개념 분류법 완성(concept taxonomy completion)

3. **학술 지식 획득(Academic Knowledge Acquisition)**:
   - 고품질 그래프 기반 지식 습득
   - 사용자-논문 관계 모델링
   - 실제 학술 시스템의 사용자 행동 기록 수집
   - 학술 질의응답(academic question answering), 논문 추천(paper recommendation), 리뷰어 추천(reviewer recommendation)

4. **학술 추적 및 예측(Academic Trace and Prediction)**:
   - 논문의 영향을 미친 핵심 참고문헌 추적(paper source tracing)
   - 학술 영향력 예측(academic influence prediction)

**평가 방법론:**
- 최소 3개 이상의 베이스라인 방법(전통 머신러닝, CNN/RNN/GNN, BERT, LLM 포함)
- 표준화된 평가 지표 및 프로토콜
- 공개 리더보드를 통한 커뮤니티 참여

## Originality

- **최초의 포괄적 학술 그래프 벤치마크**: 단순 NLP 과제를 넘어 그래프 구성, 지식 획득, 인과 추적까지 전 생명주기를 아우르는 최초의 통합 벤치마크

- **새로운 주석 전략**: 불일치 검출 기반 논문-저자 할당 검증, 온라인 커뮤니티 기반 출처 표시 등 학술 그래프의 특성을 고려한 창의적인 주석 방법론

- **대규모 다중 작업 평가**: 단일 과제가 아닌 관련된 10개 과제의 상호연결된 벤치마킹으로 전체적 이해 제공

- **현실성**: OAG의 실제 학술 데이터(700M 개체, 2B 관계)를 기반으로 하여 실제 시나리오 반영

- **공개성과 확장성**: 데이터, 코드, 리더보드를 모두 공개하고 OAG-Challenge를 통해 지속적인 커뮤니티 참여 유도

## Limitation & Further Study

- **주석 품질 검증**: 인간 주석에 대한 품질 관리 메커니즘과 inter-annotator agreement 지표가 상세히 기술되지 않음

- **도메인 편향**: OAG 데이터가 중국 학술 자원(AMiner)을 포함하여 특정 지역/도메인에 편향될 가능성

- **LLM 성능 분석 부족**: LLM이 특정 과제에서 어려움을 겪는 이유에 대한 심화된 분석이 제한적

- **시간 비용**: 대규모 인간 주석 작업에 소요된 자원과 시간에 대한 정량적 정보 부족

- **후속 연구 방향**:
  - 멀티모달 학술 데이터(이미지, 음성 등)를 포함한 벤치마크 확장
  - 동적 학술 그래프의 시간 진화를 다루는 과제 추가
  - 학술 그래프 기반 기초 모델(foundation models) 개발
  - 도메인 특화 과제의 세분화

## Evaluation

- **Novelty**: 4.5/5
  - 학술 그래프 마이닝의 전 생명주기를 아우르는 포괄적 벤치마크는 독창적이나, 개별 과제들은 기존 문제의 조합

- **Technical Soundness**: 4/5
  - 프레임워크와 방법론이 견고하나, 주석 품질 검증과 통계적 신뢰성에 대한 상세한 기술이 부족

- **Significance**: 5/5
  - 학술 그래프 마이닝 분야의 표준 벤치마크로 장기적 영향력이 크며, 다양한 응용 분야에 기여 가능

- **Clarity**: 4/5
  - 전체 구조는 명확하나, 특정 과제의 정의와 주석 프로토콜에 대한 세부 설명이 제한적

- **Overall**: 4.4/5

**총평**: OAG-Bench는 학술 그래프 마이닝 분야에 필요한 포괄적이고 고품질의 벤치마크를 제시하며, 70+ 베이스라인과 LLM 성능 분석을 통해 현재 알고리즘의 한계를 명확히 드러낸다. 개방성과 확장성으로 인해 학술 그래프 관련 연구의 중요한 참조점이 될 것으로 예상되나, 주석 프로토콜의 세부 기술화와 도메인 편향성 분석이 보완되면 더욱 견고한 자원이 될 것이다.

## Related Papers

- 🔄 다른 접근: [[papers/632_Predicting_the_future_of_ai_with_ai_High-quality_link_predic/review]] — AI 연구의 미래 예측을 위해 학술 그래프와 의미 네트워크라는 다른 접근 방식을 사용한다
- 🧪 응용 사례: [[papers/448_Kgvalidator_A_framework_for_automatic_validation_of_knowledg/review]] — 지식 그래프 검증 프레임워크를 OAG-Bench의 학술 그래프 마이닝 작업에 적용할 수 있다
- 🔗 후속 연구: [[papers/434_Interesting_Scientific_Idea_Generation_using_Knowledge_Graph/review]] — 지식 그래프 기반의 흥미로운 과학적 아이디어 생성을 학술 그래프 마이닝으로 확장할 수 있다
- 🔄 다른 접근: [[papers/632_Predicting_the_future_of_ai_with_ai_High-quality_link_predic/review]] — AI 연구 동향 예측을 위해 의미 네트워크 링크 예측과 학술 그래프 마이닝이라는 다른 방법론을 사용한다
- 🔄 다른 접근: [[papers/913_Semantic_Scholar/review]] — 학술 그래프 마이닝을 위한 다른 접근법과 벤치마크를 제공한다
