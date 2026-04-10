---
title: "739_Seagraph_Unveiling_the_whole_story_of_paper_review_comments"
authors:
  - "Jianxiang Yu"
  - "Jiaqi Tan"
  - "Zichen Ding"
  - "Jiapeng Zhu"
  - "Jiahao Li"
date: "2024"
doi: "10.48550/arXiv.2412.11939"
arxiv: ""
score: 4.0
essence: "본 논문은 피어 리뷰(peer review) 과정에서 저자들이 리뷰어의 의견을 더 잘 이해할 수 있도록 돕기 위해 SEAGraph라는 프레임워크를 제안한다. 의미론적 마인드 그래프(semantic mind graph)와 계층적 배경 그래프(hierarchical background graph)를 구성하여 리뷰 댓글의 숨겨진 의도를 파악하고 저자가 논문을 개선할 수 있도록 지원한다."
tags:
  - "cat/Academic_Peer_Review_Automation"
  - "sub/Citation_Dataset_Analysis"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yu et al._2024_Seagraph Unveiling the whole story of paper review comments.pdf"
---

# Seagraph: Unveiling the whole story of paper review comments

> **저자**: Jianxiang Yu, Jiaqi Tan, Zichen Ding, Jiapeng Zhu, Jiahao Li, Yao Cheng, Qier Cui, Yunshi Lan, Yao Liu, Xiang Li | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2412.11939](https://doi.org/10.48550/arXiv.2412.11939)

---

## Essence

본 논문은 피어 리뷰(peer review) 과정에서 저자들이 리뷰어의 의견을 더 잘 이해할 수 있도록 돕기 위해 SEAGraph라는 프레임워크를 제안한다. 의미론적 마인드 그래프(semantic mind graph)와 계층적 배경 그래프(hierarchical background graph)를 구성하여 리뷰 댓글의 숨겨진 의도를 파악하고 저자가 논문을 개선할 수 있도록 지원한다.

## Motivation

- **Known**: 전통적인 피어 리뷰 과정에서 리뷰어는 귀중한 피드백을 제공하지만, 저자들은 시간 제약 하에서 모호하거나 상세하지 않은 의견을 완벽히 이해하고 대응하기 어렵다. 최근 LLM(Large Language Models)은 강력한 텍스트 이해 및 생성 능력을 보여주고 있다.

- **Gap**: 단순히 LLM에 논문 전체와 리뷰 댓글을 입력하면 전체 논문에서 핵심을 찾기 어렵고, RAG 기반 접근은 조각난 정보를 반환하여 리뷰어의 논리적 사고 구조를 포착하지 못한다.

- **Why**: 리뷰어는 논문을 읽으며 형성한 일관된 논리 구조를 바탕으로 댓글을 작성하는데, 단순 텍스트 검색으로는 이를 재구성하기 어렵다.

- **Approach**: GraphRAG의 성공에 영감을 받아 논문의 구조적 특성(섹션/서브섹션)을 활용하여 두 가지 그래프를 구성하고, 맞춤형 검색 방법으로 각 리뷰 댓글에 대한 관련 콘텐츠를 추출한 후 LLM으로 일관된 설명을 생성한다.

## Achievement

![Figure 1: SEAGraph can help authors better understand reviewers' comments by providing detailed insights and evidence.](figures/fig1.webp)
*그림 1: SEAGraph는 저자가 리뷰어 의견을 이해하도록 상세한 통찰과 증거를 제공*

1. **리뷰 댓글 이해를 위한 새로운 프레임워크 제시**: SEAGraph는 리뷰 댓글 이해 분야를 개척하는 최초의 프레임워크로, 저자들이 리뷰어의 의도를 파악하고 논문을 개선할 수 있도록 직관적인 증거와 논거를 제공한다.

2. **이중 그래프 구조의 설계**: 의미론적 마인드 그래프는 논문의 내재적 논증과 증거를 포착하고, 계층적 배경 그래프는 연구 도메인의 맥락을 형식화하여 리뷰어의 관점을 시뮬레이션하는 데 필수적인 배경지식을 제공한다.

## How

![Figure 2: The overall framework of SEAGraph consists of the construction of the semantic mind graph and the hierarchical background graph, along with the corresponding retrieval module.](figures/fig2.webp)
*그림 2: SEAGraph의 전체 프레임워크*

- **데이터 전처리**: Nougat(시각 변환기 기반 논문 파서)를 사용하여 PDF 논문을 처리하고, LLM으로 리뷰 댓글을 개별 항목(강점, 약점, 질문)으로 추출

- **의미론적 마인드 그래프 구성**:
  - **문장 기반 청킹(Paper Chunking)**: Spacy로 문장 수준으로 분해한 후 Sentence-BERT 임베딩을 사용하여 의미 유사도 임계값(θ₁)을 기준으로 인접 문장을 병합
  - **청크 연결(Chunk Linking)**: 같은 섹션 내 청크들의 주제 유사도와 섹션 간 논리적 흐름을 바탕으로 노드와 엣지를 연결하여 논문의 쓰기 논리를 모델링

- **계층적 배경 그래프 구성**:
  - **논문 수집**: Related Work 섹션에서 인용된 논문을 Google Scholar에서 다운로드
  - **주제 추론 및 분류**: LLM을 사용하여 논문들의 주제를 추론하고 분류
  - **보완 논문 검색**: 주제 기반으로 추가 관련 논문을 검색하여 연구 맥락 형성

- **맞춤형 검색 모듈**: 각 리뷰 댓글에 대해 의미론적 부분그래프와 배경 부분그래프에서 관련 콘텐츠를 추출

- **LLM 기반 설명 생성**: 검색된 콘텐츠를 LLM에 입력하여 일관되고 논리적인 설명 생성

## Originality

- **새로운 응용 분야**: 리뷰 댓글 이해라는 구체적이고 실용적인 문제를 처음으로 다루며, 저자-리뷰어 간 소통 효율성을 개선하는 목표 설정

- **이중 그래프 설계의 창의성**: 마인드 맵 개념에서 영감을 받은 의미론적 마인드 그래프와 도메인 지식 맥락을 제공하는 계층적 배경 그래프의 조합으로 검색 품질 향상

- **구조 활용의 효율성**: 논문의 자연스러운 섹션 구조를 체계적으로 활용하여 GraphRAG보다 더 명확한 논리 구조 추출

- **다층적 맥락 통합**: 논문 내부의 논리 구조와 외부의 연구 도메인 맥락을 동시에 고려하는 통합적 접근

## Limitation & Further Study

- **확장성 한계**: 대규모 논문(수백 개 섹션) 처리 시 그래프 복잡성 증가로 인한 계산 효율성 문제 미제시

- **평가 부재**: 논문에서 정량적 실험 결과가 첫 15,000자 범위에 포함되지 않아 검증된 성능 수치 확인 불가

- **언어 범위 제한**: 현재 영문 논문 중심으로 개발되었으며, 비영문 학술 논문에 대한 적용 가능성 미검토

- **리뷰어 관점 완전성**: 특정 분야의 암묵적 지식이나 논문 특정 저자의 이전 작업에 대한 인식 부족 문제

- **후속 연구 방향**:
  - 다국어 지원 확장
  - 실시간 리뷰 댓글 분류 및 우선순위 지정 기능 추가
  - 저자의 리뷰 대응 내용과 리뷰어의 의도 간 일치도 측정 메커니즘 개발
  - 특정 학문 분야별 맞춤 그래프 구성 방식 연구

## Evaluation

- **Novelty**: 4/5
  - 리뷰 댓글 이해라는 새로운 응용 분야를 개척했으나, 기술적으로는 기존 GraphRAG와 마인드 맵 개념의 조합

- **Technical Soundness**: 4/5
  - 청크 연결과 그래프 구성 방법론이 합리적이나, 정량적 성능 지표 부재로 완전한 검증 어려움

- **Significance**: 4/5
  - 학술 출판 생태계의 실질적 문제 해결에 기여할 수 있는 높은 잠재력, 다만 실제 영향력은 추가 평가 필요

- **Clarity**: 4/5
  - 전반적으로 명확한 구조와 설명이지만, 그래프 구성의 세부 알고리즘과 검색 메커니즘의 상세 기술 부족

- **Overall**: 4/5

**총평**: SEAGraph는 피어 리뷰 프로세스의 실질적 문제를 해결하기 위해 의미론적 마인드 그래프와 계층적 배경 그래프를 효과적으로 결합한 창의적인 프레임워크이나, 정량적 실험 결과와 실제 사용 사례를 통한 검증이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/608_Peer_Review_as_A_Multi-Turn_and_Long-Context_Dialogue_with_R/review]] — 피어 리뷰를 다중 턴 대화로 모델링하는 다른 접근 방식을 제시한다.
- 🔗 후속 연구: [[papers/679_Revieweval_An_evaluation_framework_for_ai-generated_reviews/review]] — AI 생성 리뷰 평가 프레임워크로 SEAGraph의 리뷰 댓글 분석 결과를 검증할 수 있다.
- 🏛 기반 연구: [[papers/262_Deepreview_Improving_llm-based_paper_review_with_human-like/review]] — 인간과 유사한 리뷰 생성 방법론이 SEAGraph의 의미론적 분석에 기초 이론을 제공한다.
- 🧪 응용 사례: [[papers/022_A_sentiment_consolidation_framework_for_meta-review_generati/review]] — 메타 리뷰 생성에 SEAGraph의 감정 통합 프레임워크를 적용할 수 있다.
- 🧪 응용 사례: [[papers/883_When_reviewers_lock_horn_Finding_disagreement_in_scientific/review]] — 피어 리뷰 코멘트의 전체 스토리 공개가 리뷰어 간 의견 불일치 분석의 실제 적용 영역이다.
