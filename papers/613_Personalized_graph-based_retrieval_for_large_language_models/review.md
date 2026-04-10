---
title: "613_Personalized_graph-based_retrieval_for_large_language_models"
authors:
  - "Steven Au"
  - "Cameron J. Dimacali"
  - "Ojasmitha Pedirappagari"
  - "Namyong Park"
  - "Franck Dernoncourt"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "본 논문은 지식 그래프 기반의 개인화된 검색 증강 생성(PGraphRAG)을 제안하여 사용자 이력이 부족한 콜드스타트 환경에서도 LLM의 개인화된 텍스트 생성 능력을 향상시킨다. 구조화된 사용자 정보를 검색 과정에 통합하여 희소 프로필 상황에서도 유의미한 개인화를 가능하게 한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Long_Context_Embeddings"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Au et al._2025_Personalized graph-based retrieval for large language models.pdf"
---

# Personalized graph-based retrieval for large language models

> **저자**: Steven Au, Cameron J. Dimacali, Ojasmitha Pedirappagari, Namyong Park, Franck Dernoncourt, Yu Wang, Nikos Kanakaris, Hanieh Deilamsalehy, Ryan A. Rossi, Nesreen K. Ahmed | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*PGraphRAG 프레임워크 개요. 사용자 프로필과 상호작용 데이터로부터 사용자 중심 그래프를 구성하고, 그래프에서 구조화된 사용자 관련 정보를 검색하여 언어 모델의 생성을 조건부화함*

본 논문은 지식 그래프 기반의 개인화된 검색 증강 생성(PGraphRAG)을 제안하여 사용자 이력이 부족한 콜드스타트 환경에서도 LLM의 개인화된 텍스트 생성 능력을 향상시킨다. 구조화된 사용자 정보를 검색 과정에 통합하여 희소 프로필 상황에서도 유의미한 개인화를 가능하게 한다.

## Motivation

- **Known**: LLM 기반 개인화 생성은 사용자 이력(user history)에 의존하는 기존 접근법들(LaMP, LongLaMP)이 존재하며, 이들은 정보 검색 및 추천 시스템에서 개인화의 중요성을 인식하고 있음

- **Gap**: 기존 벤치마크는 최소 프로필 크기 임계값을 설정하여 대다수 사용자(Amazon 데이터셋의 99.99%)를 제외하고 있으며, 이는 실제 배포 환경의 콜드스타트 문제를 반영하지 못함

- **Why**: 실제 서비스에서는 대부분의 신규 사용자가 충분한 이력 데이터를 가지지 않아 기존 방법들이 일반적이고 무의미한 출력을 생성하게 됨

- **Approach**: 사용자-아이템 상호작용으로 구성된 이분 그래프(bipartite graph)에서 사용자 프로필 뿐만 아니라 이웃 프로필(neighboring profiles)까지 검색하여 맥락을 보강

## Achievement

![Figure 2](figures/fig2.webp)
*Amazon 사용자-제품 데이터셋에서 사용자 프로필 크기의 분포. 대부분의 사용자가 소수의 리뷰만 보유하고 있으며, 빨간 수직선은 LaMP와 LongLaMP 같은 선행 벤치마크에서 사용한 최소 프로필 크기 임계값을 표시*

1. **벤치마크 기여**: 장문 생성(4개 작업), 단문 생성(4개 작업), 서수 분류(4개 작업)로 구성된 12개 작업의 개인화된 그래프 기반 텍스트 생성 벤치마크 제시. 실제 희소 프로필 환경을 반영하는 최초의 포괄적 평가 자료

2. **성능 향상**: 장문 생성에서 평균 ROUGE-1 14.8% 개선, 단문 생성에서 4.6% 개선. 희소 프로필 환경에서 LaMP 대비 현저히 우수한 성능

## How

![Figure 3](figures/fig3.webp)
*사용자, 아이템, 상호작용 간선(예: 리뷰)을 보여주는 이분 사용자 중심 그래프 G = (U, V, E)의 예시*

- **개인화 텍스트 생성 정의**: 입력 쿼리(x), 목표 출력(y), 사용자 프로필(Pi)이 주어질 때, Pr(y' | x, Pi)를 최대화하는 개인화된 출력(ŷ) 생성
  
- **그래프 기반 검색**: 구조화된 사용자 중심 이분 그래프에서 사용자의 자체 프로필 뿐만 아니라 유사 사용자나 아이템의 관련 정보도 함께 검색. 검색된 맥락 R(Pi) ⊆ Pi을 프롬프트에 증강

- **네 가지 데이터 도메인**: 
  - Amazon Reviews 2023 (사용자-제품)
  - Datafiniti Hotel Reviews (호텔 경험)
  - Grammar and Online Product (스타일화된 피드백)
  - B2W-Reviews (다국어: 브라질 포르투갈어)

- **작업 구성**:
  - 장문: 상품 리뷰, 호텔 경험, 피드백, 다국어 리뷰 생성
  - 단문: 리뷰 제목, 호텔 요약, 피드백 제목, 다국어 제목 생성
  - 분류: 별점 평가 (5개 클래스)

## Originality

- **그래프 기반 이웃 활용**: 기존 사용자 이력 기반 개인화에서 벗어나, 그래프 구조를 통해 유사 사용자/아이템의 정보까지 확장. 콜드스타트 문제에 대한 새로운 해결책 제시

- **실제 희소 데이터 환경 반영**: 대부분의 사용자가 최소한의 이력을 가진 현실적 시나리오를 벤치마크에 포함시킨 최초의 노력

- **다중 도메인 포괄**: 4개의 서로 다른 도메인과 언어를 포함하는 종합적인 벤치마크로 일반화 가능성 입증

- **공식적 문제 정의**: Pr(y' | x, R(Pi)) 형태의 명확한 수학적 정식화를 통해 검색 증강 생성의 개인화 문제를 정확히 정의

## Limitation & Further Study

- **그래프 구성의 단순성**: 이분 그래프만 사용하며, 더 복잡한 다중 유형 노드/간선 그래프 구조의 활용 가능성 미탐색

- **검색 메커니즘 상세 부족**: 제시된 15,000자 내에서 정확한 검색 알고리즘(BM25 사용 언급은 있으나 상세 미기재) 및 그래프 순회 방법이 충분히 설명되지 않음

- **모델 규모별 분석 제한**: 구체적인 LLM 모델(GPT-4o-mini, o1 등 언급되나 상세 비교 부족) 및 모델 크기별 개인화 효과 차이 분석 미흡

- **후속 연구**: 
  - 더 정교한 그래프 신경망 기반 검색 메커니즘 개발
  - 속성 기반 그래프(attribute-based graphs) 활용
  - 계산 효율성 개선 및 대규모 그래프에 대한 확장성 검증
  - 크로스 도메인 전이 학습 탐색

## Evaluation

- **Novelty**: 4/5 - 그래프 기반 이웃 활용은 새롭지만, RAG와 개인화의 조합 자체는 점진적 진전

- **Technical Soundness**: 4/5 - 문제 정의와 평가 설계는 견고하나, 제시된 텍스트에서 검색 알고리즘의 기술적 상세가 부족

- **Significance**: 5/5 - 실제 콜드스타트 환경을 처음으로 체계적으로 다루는 벤치마크로, 실무 가치가 매우 높음

- **Clarity**: 3/5 - 개요는 명확하나, 그래프 검색 및 프롬프트 증강의 구체적 메커니즘이 불충분

- **Overall**: 4/5

**총평**: 본 논문은 실제 희소 프로필 환경을 반영한 포괄적 벤치마크를 제시하고 그래프 기반 검색을 통해 개인화된 LLM 생성 문제를 효과적으로 해결한다는 점에서 실무적 가치가 크지만, 기술적 상세성과 새로운 알고리즘 개발 측면에서는 개선의 여지가 있다.

## Related Papers

- 🏛 기반 연구: [[papers/775_Step-back_profiling_Distilling_user_history_for_personalized/review]] — 사용자 이력 증류 기법이 개인화된 그래프 기반 검색에서 콜드스타트 문제 해결을 위한 핵심 전처리 방법론으로 활용된다.
- 🔄 다른 접근: [[papers/335_Few-shot_Learning_with_Retrieval_Augmented_Language_Models/review]] — 검색 증강 생성에서 개인화 접근법과 소수샘플 학습 방법의 차이점을 비교하여 각각의 장단점을 이해할 수 있다.
- 🔗 후속 연구: [[papers/451_Knowledge-guided_large_language_model_for_material_science/review]] — 지식 안내 언어 모델의 개념을 개인화된 지식 그래프로 확장하여 더 정교한 사용자별 정보 검색이 가능하다.
- 🧪 응용 사례: [[papers/185_Can_large_language_models_understand_you_better_an_mbti_pers/review]] — 대규모 언어 모델을 위한 개인화된 그래프 기반 검색에서 본 논문의 MBTI 성격 정보를 개인화 요소로 활용할 수 있다.
- 🔗 후속 연구: [[papers/775_Step-back_profiling_Distilling_user_history_for_personalized/review]] — 사용자 이력 증류 기법이 개인화된 그래프 기반 검색에서 효율적인 사용자 프로필 생성을 위한 핵심 전처리 방법론으로 활용된다.
