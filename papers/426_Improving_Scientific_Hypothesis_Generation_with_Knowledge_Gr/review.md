---
title: "426_Improving_Scientific_Hypothesis_Generation_with_Knowledge_Gr"
authors:
  - "Guangzhi Xiong"
  - "Eric Xie"
  - "Amir Hassan Shariatmadari"
  - "Sikun Guo"
  - "Stefan Bekiranov"
date: "2024"
doi: "10.48550/arXiv.2411.02382"
arxiv: ""
score: 4.2
essence: "LLM의 과학적 가설 생성 능력을 지식 그래프(Knowledge Graph)의 구조화된 정보와 통합하여 향상시키고, 생성 과정의 환각(hallucination)을 감지 및 완화하는 KG-CoI 시스템을 제안한다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Scientific_Hypothesis_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Xiong et al._2024_Improving Scientific Hypothesis Generation with Knowledge Grounded Large Language Models.pdf"
---

# Improving Scientific Hypothesis Generation with Knowledge Grounded Large Language Models

> **저자**: Guangzhi Xiong, Eric Xie, Amir Hassan Shariatmadari, Sikun Guo, Stefan Bekiranov | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2411.02382](https://doi.org/10.48550/arXiv.2411.02382)

---

## Essence

![Figure 1](figures/fig1.webp)
*KG-CoI 시스템의 개요: KG 기반 맥락 검색, KG 증강 아이디어 체인 생성, KG 기반 환각 감지 모듈로 구성*

LLM의 과학적 가설 생성 능력을 지식 그래프(Knowledge Graph)의 구조화된 정보와 통합하여 향상시키고, 생성 과정의 환각(hallucination)을 감지 및 완화하는 KG-CoI 시스템을 제안한다.

## Motivation

- **Known**: LLM은 과학 문헌 분석과 가설 생성에 뛰어나며, 약물 발견, 생물 서열 분석 등 실제 과학 연구를 가속화할 수 있는 잠재력을 보유하고 있다.

- **Gap**: 그러나 LLM은 그럴듯하지만 사실상 부정확한 "환각"을 생성하는 경향이 있으며, 이는 엄격한 정확성과 검증 가능성이 요구되는 과학 분야에서 특히 문제가 된다. 기존의 RAG 방식은 이미 존재하는 문헌 기반 검색에 국한되어 미지의 가설 생성에 제한적이다.

- **Why**: 과학적 가설은 아직 탐구되지 않은 잠재적 발견과 관련되므로, 환각을 감지하기 어렵고 검증된 구조화된 지식이 필수적이다.

- **Approach**: 검증된 과학적 정보를 담은 지식 그래프를 LLM의 추론 과정에 직접 통합하고, 단계적 추론 체인(Chain of Ideas)을 구성하며, 생성된 가설의 환각을 KG 기반으로 탐지한다.

## Achievement

![Figure 2](figures/fig2.webp)
*다양한 방법의 성능 비교: 자기 일관성(self-consistency) 설정에서 실행 횟수에 따른 성능 변화*

1. **가설 생성 정확도 향상**: KG-CoI는 기존의 직접 프롬프팅(Direct prompting), 사고의 연쇄(Chain-of-Thought), RAG 방식 대비 가장 높은 정확도로 과학적 가설을 생성한다.

2. **환각 감소 및 신뢰성 개선**: KG 기반 환각 탐지 모듈을 통해 생성된 추론 단계들에서 사실적 오류를 식별하고, 시스템의 신뢰성을 크게 향상시킨다.

3. **새로운 평가 데이터셋 구축**: 지식 그래프 내의 링크를 마스킹하여 LLM의 가설 생성 능력을 정량적으로 평가할 수 있는 벤치마크 데이터셋을 구성하였다.

## How

![Figure 1](figures/fig1.webp)

KG-CoI는 세 가지 주요 모듈로 구성된다:

### 1. KG 기반 맥락 검색 (KG-guided Context Retrieval)
- **지식 향상**: 두 엔티티(eh, et) 사이의 k-스텝 관계 체인을 지식 그래프에서 검색하여, 매개 엔티티들을 통한 연결 정보를 발견
  - eh ↔r₁ e₁ ↔r₂ e₂ ... ↔rₖ et 형태의 경로 추출
- **쿼리 풍부화**: 원래 질문과 검색된 KG 관계로부터 LLM-E 에이전트가 문헌 검색을 위한 키워드를 생성
  - 생성된 키워드: w₁, ⋯, wT = argmax PLLM-E(w₁*, ⋯, wT* | Q, R)
- **문헌 정보 검색**: BM25 스파스 레트리버를 사용하여 PubMed에서 생성된 키워드 기반 관련 문서 검색

### 2. KG 증강 아이디어 체인 생성 (KG-augmented Chain-of-idea Generation)
- 검색된 문헌과 KG 정보를 입력으로 LLM-G 에이전트가 단계적 추론을 수행
- 각 추론 단계가 논리적으로 연결된 아이디어 체인(Chain of Ideas, CoI) 형태로 가설 생성
- 중간 추론 단계의 명시적 표현으로 투명성과 검증 가능성 향상

### 3. KG 기반 환각 탐지 (KG-supported Hallucination Detection)
- LLM-V 에이전트가 생성된 각 추론 단계의 주장(claim)을 검증
- KG-R 레트리버로 KG 내 관련 사실 검색하여 주장의 사실성 확인
- 문헌 정보와 KG 정보가 모두 부족한 경우 환각으로 표시

## Originality

- **KG와 LLM의 정교한 통합**: 단순한 검색 증강을 넘어, 지식 그래프의 구조화된 관계를 LLM의 추론 과정 전 단계에서 활용하는 엔드-투-엔드 시스템 설계

- **과학 가설 생성을 위한 새로운 평가 프레임워크**: KG의 링크 마스킹을 통해 미지의 가설 생성을 평가할 수 있는 객관적 벤치마크 제시

- **환각 탐지의 명시적 처리**: 기존 RAG가 놓치기 쉬운 "그럴듯하지만 사실이 아닌" 환각을 KG와 문헌 기반으로 체계적으로 탐지하는 모듈

- **도메인 특화적 접근**: 생물의학 분야의 특성을 반영하여 BM25와 같은 도메인 친화적 검색 방식 선택

## Limitation & Further Study

- **지식 그래프 의존성**: KG의 품질과 범위가 시스템 성능에 크게 영향을 미치며, 불완전하거나 편향된 KG는 가설 생성을 제약할 수 있다.

- **도메인 한정성**: 논문은 생물의학 영역의 PubMed 데이터셋만 사용했으며, 다른 과학 분야(물리학, 화학, 재료 과학 등)로의 확장성이 명확하지 않다.

- **계산 비용**: 여러 단계의 LLM 호출과 KG 검색을 반복해야 하므로 실시간 가설 생성의 실용성 고려 필요

- **후속 연구 방향**:
  - 다중 도메인 과학 분야로의 확장 및 KG 간 통합 전략 개발
  - 동적 KG 업데이트 메커니즘으로 최신 과학 지식 반영
  - 생성된 가설의 실제 과학적 가치 평가를 위한 도메인 전문가 검증
  - 환각 탐지의 거짓 양성(false positive) 비율 감소 방법 연구


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.2/5

**총평**: KG-CoI는 LLM의 과학적 가설 생성 능력을 향상시키기 위해 지식 그래프를 체계적으로 통합한 참신한 접근법을 제시하며, 특히 환각 탐지 모듈과 새로운 평가 데이터셋은 과학 AI 분야에 실질적 기여를 한다. 다만 생물의학 영역에 국한된 평가와 다른 도메인으로의 일반화 가능성 검증이 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/500_Llm-based_corroborating_and_refuting_evidence_retrieval_for/review]] — 지식 그래프 기반 가설 생성을 과학적 주장 검증으로 확장한 방법론
- 🔄 다른 접근: [[papers/391_Graph_of_ai_ideas_Leveraging_knowledge_graphs_and_llms_for_a/review]] — 같은 지식 그래프 활용 접근이지만 AI 연구 아이디어 생성에 특화된 시스템
- 🏛 기반 연구: [[papers/009_A_GENTIC_H_YPOTHESIS__A_SURVEY_ON_HYPOTHESIS_GENERATION_USIN/review]] — 가설 생성 연구의 포괄적 서베이로서 이론적 기초 제공
- 🔗 후속 연구: [[papers/666_Research_hypothesis_generation_over_scientific_knowledge_gra/review]] — 지식 그래프 기반 가설 생성의 실제 연구 적용 사례
- 🏛 기반 연구: [[papers/819_Toward_reliable_biomedical_hypothesis_generation_Evaluating/review]] — 지식 기반 가설 생성이 생의학 가설의 진실성 평가 기반을 제공합니다.
- 🔄 다른 접근: [[papers/391_Graph_of_ai_ideas_Leveraging_knowledge_graphs_and_llms_for_a/review]] — AI 연구 vs 일반 과학 가설 생성으로 지식 그래프 활용의 서로 다른 도메인 적용
- 🏛 기반 연구: [[papers/500_Llm-based_corroborating_and_refuting_evidence_retrieval_for/review]] — 지식 그래프 기반 가설 생성이 과학적 주장 검증의 방법론적 기반
- 🏛 기반 연구: [[papers/289_Drsr_Llm_based_scientific_equation_discovery_with_dual_reaso/review]] — 지식 그래프를 활용한 과학 가설 생성 연구가 방정식 발견에서 경험적 지식을 활용하는 접근법의 이론적 기반을 제공합니다.
