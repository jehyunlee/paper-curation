---
title: "034_A_Survey_on_RAG_Meeting_LLMs_Towards_Retrieval-Augmented_Lar"
authors:
  - "Wenqi Fan"
  - "Yujuan Ding"
  - "Liang-bo Ning"
  - "Shijie Wang"
  - "Hengyun Li"
date: "2024"
doi: "10.1145/3637528.3671470"
arxiv: ""
score: 4.0
essence: "본 논문은 Retrieval-Augmented Generation (RAG)과 Large Language Models (LLMs)의 통합인 RA-LLMs에 대한 종합적인 설문조사로, 아키텍처, 훈련 전략, 응용 분야의 세 가지 기술적 관점에서 기존 연구를 체계적으로 리뷰한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Retrieval-augmented_Generation_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Fan et al._2024_A Survey on RAG Meeting LLMs Towards Retrieval-Augmented Large Language Models.pdf"
---

# A Survey on RAG Meeting LLMs: Towards Retrieval-Augmented Large Language Models

> **저자**: Wenqi Fan, Yujuan Ding, Liang-bo Ning, Shijie Wang, Hengyun Li | **날짜**: 2024 | **DOI**: [10.1145/3637528.3671470](https://doi.org/10.1145/3637528.3671470)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Retrieval-Augmented Generation (RAG) meets*

본 논문은 Retrieval-Augmented Generation (RAG)과 Large Language Models (LLMs)의 통합인 RA-LLMs에 대한 종합적인 설문조사로, 아키텍처, 훈련 전략, 응용 분야의 세 가지 기술적 관점에서 기존 연구를 체계적으로 리뷰한다.

## Motivation

- **Known**: RAG는 외부 지식 기반을 활용하여 생성 모델의 품질을 향상시키는 기법이며, LLMs는 대규모 사전학습을 통해 뛰어난 언어 이해 및 생성 능력을 보유하고 있다. 그러나 LLMs는 hallucination 문제, 구식 정보, 도메인 특화 지식 부족 등의 내재적 한계를 가지고 있다.
- **Gap**: 기존 연구들이 RAG와 LLMs의 개별적 발전은 다루었으나, 두 기술의 통합인 RA-LLMs에 대한 체계적이고 포괄적인 분류 및 분석이 부족하다. 특히 아키텍처, 훈련 전략, 응용 관점에서의 통합적 검토가 필요하다.
- **Why**: LLMs의 hallucination 문제와 outdated knowledge는 실무 응용을 심각하게 제한하며, RAG를 통한 외부 지식 통합은 이를 근본적으로 해결할 수 있기 때문이다. 특히 의료, 법률 등 최신 정보와 높은 신뢰성이 요구되는 도메인에서 RA-LLMs의 중요성이 증대되고 있다.
- **Approach**: 본 논문은 LLMs의 기초 개념 소개 후, RA-LLMs의 아키텍처(검색, 생성, 증강 관점), 훈련 전략(사전학습, 파인튜닝, In-context Learning), 그리고 다양한 응용 분야를 체계적으로 분류하고 검토한다. 마지막으로 현재의 한계와 향후 연구 방향을 논의한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2: Representing RAG and RA-LLMs methods organized by their main design focus, proposed time and impact (shown by*

- **포괄적 분류 체계**: RAG와 LLMs의 통합 기술을 아키텍처, 훈련 전략, 응용 분야라는 명확한 세 가지 축으로 체계적으로 분류
- **기술적 깊이**: kNN-LM, REALM, FiD, RETRO, DSP 등 주요 RA-LLM 방법론들의 상세한 분석 및 비교
- **실제 적용 사례**: 오픈도메인 QA, AI4Science, 소프트웨어 엔지니어링 등 다양한 응용 분야에서의 실증적 효과 입증
- **Hallucination 감소**: RAG를 통한 외부 지식 통합이 LLMs의 hallucination 문제를 효과적으로 완화할 수 있음을 입증
- **최신 정보 활용**: RA-LLMs이 학습 데이터에 포함되지 않은 최신 정보를 동적으로 활용할 수 있는 능력 제시

## How

![Figure 3](figures/fig3.webp)

*Figure 3: Illustration of the basic Retrieval-Augmented Large Language Models (RA-LLMs) framework for a specific QA task*

- LLMs의 세 가지 카테고리(Encoder-only, Decoder-only, Encoder-Decoder)에 대한 기초 이론 정립
- RA-LLMs 아키텍처를 검색기(Retriever) 설계, 생성기(Generator) 통합, 증강 방식(Augmentation)으로 세분화하여 분석
- Pre-training, Fine-tuning, In-context Learning 등 주요 훈련 패러다임의 특성과 효과 비교
- 시간 축 정렬(Timeline)을 통해 kNN-LM(2019)부터 최신 기법까지의 진화 과정 추적
- 질문응답(QA), 정보검색(IR), 추천시스템(Recommendation), 과학 분야(AI4Science) 등 다양한 도메인에서의 적용 사례 검토
- 기술적 과제(Retrieval quality, Ranking, Dense vs. Sparse retrieval 등)와 해결 방안 제시

## Originality

- 기존 RAG 또는 LLM 관련 설문조사와 달리, RA-LLMs을 명시적으로 정의하고 기술적 관점에서 통합적으로 리뷰한 첫 종합 설문조사
- 아키텍처, 훈련 전략, 응용 분야라는 삼축(Three-dimensional) 분류 체계를 제시하여 기존 설문조사보다 체계적인 조직화
- Multi-modal RAG와 AIGC-specific RAG 등 concurrent survey와의 차별성을 명확히 하여 정위치 제시
- Hallucination 문제 해결을 위한 RAG의 구체적 메커니즘을 실증적 예시와 함께 설명

## Limitation & Further Study

- 설문 논문이므로 새로운 방법론이나 알고리즘을 제시하지 않으며, 기존 연구의 메타-분석에 그침
- 2024년 KDD 출판 기준이므로 그 이후의 RAG-LLM 발전(예: GPT-4o, Llama 3 이후)을 포함하지 못함
- Retriever와 Generator의 상호작용(Co-training, Joint optimization) 관점에서의 깊이 있는 분석 부족 가능성
- 계산 비용(Computational cost), 지연시간(Latency), 메모리 효율성 등 실제 배포 관점의 분석이 제한적
- **후속 연구 방향**: (1) Multi-step retrieval과 iterative refinement 기법의 고도화, (2) Dense and sparse retrieval의 최적 조합, (3) Cross-lingual 및 cross-domain RA-LLMs 개발, (4) RA-LLMs의 해석성(Interpretability) 향상, (5) 실시간 동적 지식 기반 구축 및 관리 기술

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 RAG와 LLMs의 통합이라는 시대적 요구에 부응하여, 기술적 관점에서 가장 체계적이고 포괄적인 설문조사를 제공한다. Hallucination 문제 해결, 최신 정보 활용, 도메인 특화 응용 등의 실제 가치와 함께 아키텍처-훈련-응용이라는 명확한 분류 체계를 제시함으로써 RA-LLMs 연구 분야의 중요한 기준점이 될 것으로 기대된다.

## Related Papers

- 🔄 다른 접근: [[papers/675_Retrieval-Augmented_Generation_for_Knowledge-Intensive_NLP_T/review]] — 대규모 언어모델을 위한 검색 증강 생성에 대한 다른 관점의 서베이를 제시한다.
- 🏛 기반 연구: [[papers/295_Dynamic_multi-agent_orchestration_and_retrieval_for_multi-so/review]] — RAG와 LLM 결합에 대한 포괄적 조사로 검색 증강 생성의 이론적 기반을 제공한다.
- 🧪 응용 사례: [[papers/318_Estimating_optimal_context_length_for_hybrid_retrievalaugmen/review]] — RAG와 LLM 결합의 구체적 구현 사례로 검색 문맥 길이 최적화를 다룬다
