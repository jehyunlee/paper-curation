---
title: "335_Few-shot_Learning_with_Retrieval_Augmented_Language_Models"
authors:
  - "Gautier Izacard"
  - "Patrick Lewis"
  - "M. Lomeli"
  - "Lucas Hosseini"
  - "F. Petroni"
date: "2022"
doi: "N/A"
arxiv: ""
score: 4.5
essence: "본 논문은 매개변수 메모리에 의존하지 않고 외부 지식 소스를 활용하는 검색 증강 언어 모델(Atlas)을 제시하여, 550억 개 매개변수 모델보다 50배 적은 매개변수(110억)로 우수한 few-shot 학습 성능을 달성한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Scientific_Question_Answering"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Izacard et al._2022_Few-shot Learning with Retrieval Augmented Language Models.pdf"
---

# Few-shot Learning with Retrieval Augmented Language Models

> **저자**: Gautier Izacard, Patrick Lewis, M. Lomeli, Lucas Hosseini, F. Petroni | **날짜**: 2022 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: Atlas는 사전학습과 미세조정 단계 모두에서 검색을 활용하는 검색 증강 언어 모델로, 지식 기반 작업에서 강력한 few-shot 성능을 보임*

본 논문은 매개변수 메모리에 의존하지 않고 외부 지식 소스를 활용하는 검색 증강 언어 모델(Atlas)을 제시하여, 550억 개 매개변수 모델보다 50배 적은 매개변수(110억)로 우수한 few-shot 학습 성능을 달성한다.

## Motivation

- **Known**: 대규모 언어 모델(LLM)은 few-shot 학습에서 우수한 성능을 보이지만, 질의응답이나 사실 검증 같은 지식 집약적 작업에서는 막대한 매개변수가 필요하다.

- **Gap**: 검색 증강 모델(retrieval-augmented models)이 지식 집약적 작업에서 효과적임이 알려져 있으나, few-shot 설정에서의 성능은 불명확하다. 또한 few-shot 학습이 모델의 매개변수에 방대한 정보 저장을 필수로 하는지 검증되지 않았다.

- **Why**: 지식은 외부 비파라미터 메모리(external non-parametric memory)로 아웃소싱할 수 있으며, 이를 통해 모델의 적응성, 해석가능성, 효율성을 개선할 수 있다.

- **Approach**: 검색 증강 아키텍처를 활용하되, 사전학습 단계에서 retriever와 언어 모델을 함께 학습하고, 네 가지 novel한 retriever 학습 목적 함수(ADist, EMDR2, PDist, Margin-MSE)를 제시하여 few-shot 성능을 최적화한다.

## Achievement

![Figure 2](figures/fig2.webp)
*Figure 2: KILT 벤치마크의 다양한 작업(사실 검증, 질의응답, 엔티티 링킹)에 대한 쿼리-출력 쌍의 예시*

1. **Few-shot 성능 우수성**: NaturalQuestions에서 64개 예시만으로 42.4% 정확도 달성 (PaLM 540B 대비 3% 우수), Wikipedia 인덱스만 사용 시 45.1% 달성

2. **Full-dataset 성능 최고 성과**: NaturalQuestions (+8.1%), TriviaQA (+9.3%), FEVER, KILT의 5개 작업에서 새로운 최고 성능 기록

3. **MMLU 성능**: 매개변수 15배 많은 모델과 동등하거나 우수한 성능 달성

4. **인덱스 압축**: Product quantization을 이용한 압축 인덱스가 비압축 인덱스와 유사한 성능을 유지하면서 5배 메모리 감소 달성

## How

### 아키텍처 설계

- **Retriever**: Contriever 기반의 dual-encoder 구조로, 쿼리와 문서를 독립적으로 임베딩하여 dot-product로 유사도 계산. MoCo 대조 손실로 사전학습.

- **Language Model**: T5 sequence-to-sequence 아키텍처에 Fusion-in-Decoder(FiD) 적용. 각 문서를 인코더에서 독립적으로 처리한 후 디코더에서 결합된 출력에 대해 교차-주의(cross-attention) 수행.

### Retriever 학습 목적 함수

1. **Attention Distillation (ADist)**: 언어 모델의 교차-주의 점수(α_n ∥v_n∥²)를 retriever 확률 분포로 KL-divergence 최소화하여 증류

2. **EMDR² (End-to-end Multi-Document Reader and Retriever)**: EM 알고리즘 영감, 검색된 문서를 잠재 변수로 취급하여 $\log[\sum_{k=1}^K p_{lm}(a|q,d_k)p_{retr}(d_k|q)]$ 최대화

3. **Perplexity Distillation (PDist)**: 언어 모델이 각 문서로부터 받는 perplexity 개선을 학습 신호로 활용하는 단순한 손실 함수

4. **Margin-MSE**: 문서 쌍 간의 상대적 순위를 고려한 마진 기반 평균제곱오차(MSE) 손실

### 사전학습 전략

- 다양한 자가지도학습(self-supervised) 작업 활용: Masked Language Modeling(MLM), Span Corruption, 대조 학습
- Retriever와 언어 모델의 공동 사전학습이 few-shot 성능의 핵심

### 미세조정 전략

- Retriever와 언어 모델 양쪽을 효율적으로 적응시키기 위한 다양한 파라미터 업데이트 전략 제시
- Task별로 선택적 업데이트 가능

## Originality

- **Novel 학습 목적 함수**: Attention 점수에서 value norm 고려(α_n ∥v_n∥²)라는 개선된 attention distillation 제시

- **Systematic 설계 연구**: Few-shot 학습을 위한 검색 증강 모델의 사전학습과 미세조정 전략을 체계적으로 연구한 첫 수준의 연구

- **Scalable 아키텍처**: Fusion-in-Decoder를 통해 검색 문서 수에 따른 quadratic 복잡도 문제 해결

- **Index 업데이트 가능성**: 외부 문서 인덱스의 동적 업데이트가 가능하여 지식의 시간적 변화에 대응 가능

- **Interpretability**: 검색된 문서를 명시적으로 확인 가능하여 모델 결정에 대한 설명가능성 제공

## Limitation & Further Study

- **Index 크기 제약**: 대규모 인덱스 구축 및 관리의 계산 비용이 여전히 존재하며, 인덱스 품질의 편향 문제 검토 필요

- **Retriever 성능 의존성**: 전체 시스템의 성능이 retriever의 성능에 크게 의존하므로, retriever 오류 분석 및 개선 필요

- **Generalization across domains**: 특정 도메인에서 학습한 모델이 다른 도메인으로의 전이 가능성에 대한 추가 연구 필요

- **Real-time 검색**: 매우 대규모 인덱스에서의 실시간 검색 지연 시간 개선 필요

- **Cross-lingual few-shot learning**: 다국어 few-shot 학습 설정에서의 성능 평가 필요

## Evaluation

- **Novelty**: 4.5/5 — 검색 증강과 few-shot 학습의 결합이 신선하고, 여러 novel한 학습 목적 함수 제시. 다만 개별 요소(retriever, FiD)들은 기존 연구 기반.

- **Technical Soundness**: 4.5/5 — 아키텍처 설계와 학습 전략이 타당하고 충분히 검증됨. Attention distillation의 개선(α_n ∥v_n∥²)이 잘 동기화됨.

- **Significance**: 4.5/5 — 매개변수 효율성에서 대규모 모델을 능가하는 실용적 의의 높음. 지식 집약적 작업의 새로운 패러다임 제시.

- **Clarity**: 4.5/5 — 논문 구조 명확하고 방법론 설명 이해하기 쉬움. 실험 설정과 결과 해석이 충분하나 일부 하이퍼파라미터 선택 근거 추가 필요.

- **Overall**: 4.5/5

**총평**: 본 논문은 검색 증강 언어 모델의 few-shot 학습 능력을 체계적으로 탐구하여, 매개변수 효율성과 성능 간의 새로운 균형점을 제시한 고품질 연구다. 특히 실무 적용 가능성과 지식 업데이트 용이성 측면에서 학계와 산업계에 모두 기여할 수 있는 중요한 작업이다.

## Related Papers

- 🔗 후속 연구: [[papers/593_Openscholar_Synthesizing_scientific_literature_with_retrieva/review]] — 소규모 검색 증강 모델의 기본 아이디어를 대규모 과학 문헌 데이터베이스로 확장한 발전된 형태의 연구입니다.
- 🔄 다른 접근: [[papers/768_Splade_v2_Sparse_lexical_and_expansion_model_for_information/review]] — 밀집 표현 기반 검색 증강과 희소 렉시컬 표현 기반 검색의 서로 다른 정보검색 접근법을 제시합니다.
- 🧪 응용 사례: [[papers/224_Clinical_entity_augmented_retrieval_for_clinical_information/review]] — 검색 증강 언어모델의 일반적 원리를 임상 정보 추출이라는 구체적 도메인에 적용한 사례입니다.
- 🏛 기반 연구: [[papers/224_Clinical_entity_augmented_retrieval_for_clinical_information/review]] — 검색 증강 언어모델의 기본 원리를 임상 도메인에 특화하여 적용한 실제 구현 사례입니다.
- 🔄 다른 접근: [[papers/768_Splade_v2_Sparse_lexical_and_expansion_model_for_information/review]] — 희소 렉시컬 표현과 밀집 표현 기반 검색 증강이라는 서로 다른 정보검색 패러다임의 장단점을 비교할 수 있습니다.
- 🔗 후속 연구: [[papers/593_Openscholar_Synthesizing_scientific_literature_with_retrieva/review]] — 소규모 검색 증강 모델의 기본 개념을 4천500만 개 논문을 다루는 대규모 과학 문헌 시스템으로 발전시킨 연구입니다.
- 🏛 기반 연구: [[papers/421_Improving_demonstration_diversity_by_human-free_fusing_for_t/review]] — 검색 증강 언어모델의 소수샷 학습이 시연 다양성 개선의 기초적인 방법론을 제공합니다.
- 🔄 다른 접근: [[papers/613_Personalized_graph-based_retrieval_for_large_language_models/review]] — 검색 증강 생성에서 개인화 접근법과 소수샘플 학습 방법의 차이점을 비교하여 각각의 장단점을 이해할 수 있다.
