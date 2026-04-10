---
title: "659_REALM_Retrieval-Augmented_Language_Model_Pre-Training"
authors:
  - "Kelvin Guu"
  - "Kenton Lee"
  - "Zora Tung"
  - "Panupong Pasupat"
  - "Ming-Wei Chang"
date: "2020"
doi: "arXiv:2002.08909"
arxiv: ""
score: 4.5
essence: "REALM은 지식을 신경망 파라미터에 암묵적으로 저장하는 대신, 학습 가능한 텍스트 검색 모듈을 통해 명시적으로 외부 코퍼스(예: Wikipedia)에서 관련 문서를 동적으로 검색하고 활용하는 검색증강 언어 모델 사전학습 프레임워크다. 비지도 마스크된 언어 모델(MLM) 목표 신호를 통해 검색기를 end-to-end로 학습할 수 있다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Scientific_Language_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Guu et al._2020_REALM Retrieval-Augmented Language Model Pre-Training.pdf"
---

# REALM: Retrieval-Augmented Language Model Pre-Training

> **저자**: Kelvin Guu, Kenton Lee, Zora Tung, Panupong Pasupat, Ming-Wei Chang | **날짜**: 2020 | **DOI**: [arXiv:2002.08909](https://arxiv.org/abs/2002.08909)

---

## Essence

![Figure 1](figures/fig1.webp) *REALM은 언어 모델 사전학습에 신경망 기반 지식 검색기(neural knowledge retriever)를 통합하여, 백엔드에서 수백만 개의 문서를 고려하는 검색 단계를 통해 학습 신호를 역전파한다.*

REALM은 지식을 신경망 파라미터에 암묵적으로 저장하는 대신, 학습 가능한 텍스트 검색 모듈을 통해 명시적으로 외부 코퍼스(예: Wikipedia)에서 관련 문서를 동적으로 검색하고 활용하는 검색증강 언어 모델 사전학습 프레임워크다. 비지도 마스크된 언어 모델(MLM) 목표 신호를 통해 검색기를 end-to-end로 학습할 수 있다.

## Motivation

- **Known**: BERT, RoBERTa, T5 등 최신 언어 모델들은 사전학습 중 대규모 텍스트 코퍼스로부터 방대한 세계 지식을 습득하며, 이는 질문 응답(QA)과 같은 지식 집약적 작업에서 중요한 역할을 수행한다.

- **Gap**: 그러나 이러한 지식이 신경망의 파라미터에 암묵적으로 저장되어 있어, (1) 어떤 지식이 어디에 저장되어 있는지 파악하기 어렵고, (2) 더 많은 사실을 포함하려면 계속해서 더 큰 모델을 학습해야 하므로 계산 비용이 급증한다.

- **Why**: 지식을 모듈화되고 해석 가능한 방식으로 저장하며 필요할 때 동적으로 접근할 수 있는 메커니즘이 필요하다.

- **Approach**: 학습 가능한 검색기 p(z|x)와 지식 증강 인코더 p(y|z,x)를 도입하여, 입력에 대해 관련 문서를 검색한 후 이를 조건으로 출력을 예측하는 retrieve-then-predict 방식의 잠재변수 언어 모델로 설계한다. 검색기는 unsupervised MLM 신호에 의존하여 역전파 학습이 가능하다.

## Achievement

![Figure 2](figures/fig2.webp) *REALM의 전체 프레임워크: (좌) 비지도 사전학습에서 검색기와 지식 증강 인코더가 공동으로 학습되고, (우) 지도 미세조정에서 사전학습된 파라미터를 다운스트림 과제에 적용한다.*

1. **Open-QA 벤치마크에서 SOTA 달성**: NaturalQuestions-Open, WebQuestions, CuratedTrec의 세 가지 주요 Open-QA 벤치마크에서 기존 방법 대비 4-16% 절대 정확도(absolute accuracy) 향상을 달성했다. 이는 명시적 지식 저장(retrieval-based) 방법과 암묵적 지식 저장(T5 같은 대규모 생성 모델) 모두를 능가한다.

2. **비지도 학습으로 검색기 최적화**: 처음으로 수백만 개의 문서를 고려하는 거대 규모 검색 단계를 통해 역전파를 수행하는 방식으로, 라벨 없이 MLM 신호만을 이용하여 신경망 검색기를 사전학습하는 방법을 제시했다.

3. **해석 가능성 및 모듈화**: 검색된 문서가 명시적으로 노출되어 모델 예측의 근거를 추적할 수 있으며, 검색기와 인코더를 독립적으로 업데이트하거나 지식 코퍼스를 교체할 수 있다.

## How

![Figure 3](figures/fig3.webp) *REALM 사전학습에서 비동기 MIPS를 활용한 대규모 검색 최적화.*

**핵심 방법론:**

- **생성 과정 모델링**: p(y|x) = Σ_z∈Z p(y|z,x)p(z|x) 형태로 검색을 잠재변수로 취급하여 모든 가능한 문서에 대해 주변화(marginalize)한다.

- **신경망 검색기 구조**: 
  - 입력 x와 문서 z를 각각 BERT 기반 변환기로 d차원 벡터로 임베딩
  - 관련도 점수 f(x,z) = Embed_input(x)⊤ Embed_doc(z)를 내적으로 계산
  - 검색 확률분포: p(z|x) = softmax(f(x,z))

- **지식 증강 인코더**:
  - 입력과 검색된 문서를 연결하여 단일 시퀀스로 변환([CLS] x [SEP] z_body [SEP])
  - 별도의 변환기로 처리하여 x와 z 사이의 풍부한 교차-주의(cross-attention) 수행

- **계산 효율화 (MIPS)**:
  - 각 문서별 임베딩을 캐싱하고 비동기적으로 업데이트
  - 상위 k개 문서 선택을 Maximum Inner Product Search(MIPS)로 공식화하여 근사적으로 해결

- **목적 함수**:
  - **사전학습**: MLM 손실을 통해 마스킹된 토큰 예측 → 검색 단계를 통해 역전파
  - **미세조정**: 답이 검색된 문서의 연속 토큰 구간(span)으로 표현되도록 학습

- **훈련 안정화**: Retrieval Utility(RU)라는 지표를 사용하여 검색기가 유용한 문서를 선택하고 있는지 모니터링

## Originality

- **최초의 규모 있는 신경망 검색기 사전학습**: 이전 k-NN LM은 retrieval을 미세조정 단계에서 활용하지 못했으나, REALM은 비지도 신호로 검색기 자체를 학습하고 다운스트림 과제로 전이 가능하게 설계했다.

- **End-to-end 미분 가능 검색**: 수백만 개 문서를 고려하는 검색 단계를 마스크 언어 모델링 목표와 직접 연결하여 역전파를 통한 최적화를 구현했다.

- **Retrieve-then-predict 패러다임의 사전학습 통합**: 기존 Open-QA의 heuristic 검색 방식을 학습 가능한 framework으로 일반화하여 사전학습 단계에 적용한 첫 시도다.

- **모듈화된 설계**: 검색기와 인코더를 분리하여 지식 소스 교체나 독립적 업데이트가 용이하고, 모델 크기 확장 없이 지식 확장이 가능하다.

## Limitation & Further Study

- **검색 병목**: 매 학습 단계마다 수백만 개 문서에 대한 관련도 계산 및 역전파가 필요하므로, MIPS 근사로 인한 품질 손실과 계산 복잡도 간의 trade-off가 존재한다.

- **문서 표현 고정성**: 사전학습 중 문서 임베딩(Embed_doc)을 주기적으로 업데이트하지만, 모든 검색 단계에서 실시간 업데이트를 하지 않아 수렴 속도가 느릴 수 있다.

- **Answer span 가정**: Open-QA 미세조정에서 답이 항상 검색된 문서에 연속 구간으로 존재한다고 가정하므로, 다중-홉(multi-hop) 추론이나 계산이 필요한 답에 대한 확장성이 제한된다.

- **코퍼스 크기에 따른 성능 변동**: 지식 코퍼스의 크기, 품질, 구성에 따른 성능 민감도에 대한 심층 분석 필요.

- **후속 연구 방향**:
  - Dense passage retrieval과의 통합
  - 동적 코퍼스 업데이트 메커니즘
  - 다중-홉 추론을 위한 iterative retrieval 확장
  - 다언어 및 도메인 특화 버전 개발


## Evaluation

- Novelty: 5/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4.5/5

**총평**: REALM은 검색 메커니즘을 신경망 사전학습 단계에 최초로 통합하여 규모 있는 비지도 학습을 달성한 획기적 연구다. 명시적 지식 접근을 통해 해석 가능성과 모듈화를 확보하면서도 Open-QA에서 기존 모든 방법을 능가하는 성능을 보여줬다. 다만 대규모 검색의 계산 비용 및 문서 표현 업데이트의 지연성은 실무 적용 시 고려할 점이며, 향후 더 정교한 retrieval 전략과의 결합으로 한계를 극복할 여지가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/152_BERT_Pre-training_of_Deep_Bidirectional_Transformers_for_Lan/review]] — BERT의 암묵적 지식 저장과 달리 외부 코퍼스에서 명시적 검색을 통한 지식 활용 방식
- 🔗 후속 연구: [[papers/348_FRAG_A_Flexible_Modular_Framework_for_Retrieval-Augmented_Ge/review]] — REALM의 검색 증강 기법을 더 유연한 모듈형 프레임워크로 발전시킨 연구
- 🏛 기반 연구: [[papers/675_Retrieval-Augmented_Generation_for_Knowledge-Intensive_NLP_T/review]] — REALM이 제시한 검색 증강 생성의 초기 방법론이 RAG 연구의 기초가 됨
- 🔗 후속 연구: [[papers/404_Hiperrag_High-performance_retrieval_augmented_generation_for/review]] — REALM의 검색 증강 개념을 고성능으로 최적화한 HiPerRAG로 발전
- 🔄 다른 접근: [[papers/404_Hiperrag_High-performance_retrieval_augmented_generation_for/review]] — 과학 문헌 처리에서 멀티모달 사전훈련과 고성능 컴퓨팅 기반 접근법을 비교할 수 있습니다.
- 🔄 다른 접근: [[papers/152_BERT_Pre-training_of_Deep_Bidirectional_Transformers_for_Lan/review]] — BERT의 암묵적 지식 저장 방식과 달리 명시적 검색을 통해 지식을 활용하는 다른 접근법
- 🏛 기반 연구: [[papers/348_FRAG_A_Flexible_Modular_Framework_for_Retrieval-Augmented_Ge/review]] — 검색증강 언어모델 사전훈련 방법론을 지식그래프 특화 RAG 시스템으로 발전시킨 기반
- 🔗 후속 연구: [[papers/768_Splade_v2_Sparse_lexical_and_expansion_model_for_information/review]] — REALM의 밀집 표현 기반 검색을 희소 표현과 결합한 발전된 형태의 검색 증강 사전학습 모델입니다.
