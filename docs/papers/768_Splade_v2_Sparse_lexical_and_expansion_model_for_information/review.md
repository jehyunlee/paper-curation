---
title: "768_Splade_v2_Sparse_lexical_and_expansion_model_for_information"
authors:
  - "Thibault Formal"
  - "Carlos Lassance"
  - "Benjamin Piwowarski"
  - "Stéphane Clinchant"
date: "2021"
doi: "10.1145/nnnnnnn.nnnnnnn"
arxiv: ""
score: 4.5
essence: "본 논문은 신경망 기반 정보검색에서 희소(sparse) 렉시컬 표현을 학습하는 SPLADE 모델을 개선하여, 밀집 표현(dense embedding)의 효율성과 전통적 가방 단어(bag-of-words) 모델의 해석가능성을 결합한 첫 단계 검색기를 제안한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Long_Context_Embeddings"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Formal et al._2021_Splade v2 Sparse lexical and expansion model for information retrieval.pdf"
---

# Splade v2: Sparse lexical and expansion model for information retrieval

> **저자**: Thibault Formal, Carlos Lassance, Benjamin Piwowarski, Stéphane Clinchant | **날짜**: 2021 | **DOI**: [10.1145/nnnnnnn.nnnnnnn](https://doi.org/10.1145/nnnnnnn.nnnnnnn)

---

## Essence

본 논문은 신경망 기반 정보검색에서 희소(sparse) 렉시컬 표현을 학습하는 SPLADE 모델을 개선하여, 밀집 표현(dense embedding)의 효율성과 전통적 가방 단어(bag-of-words) 모델의 해석가능성을 결합한 첫 단계 검색기를 제안한다.

## Motivation

- **Known**: 최근 신경망 기반 정보검색은 밀집 표현을 사용한 근사 최근접 이웃 검색(ANN)과 전통적 가방 단어 모델 간의 트레이드오프에 직면해 있다. SPLADE 모델이 희소 표현으로 경쟁력 있는 결과를 보였으나, 여전히 개선 여지가 있다.

- **Gap**: 기존 SPLADE는 합산(sum) 풀링을 사용하며, 쿼리 확장으로 인한 온라인 계산 비용, 그리고 증류(distillation)를 통한 성능 향상의 미적용 등의 한계를 가진다.

- **Why**: 정보검색의 첫 단계 검색기는 효율성과 효과성 사이의 균형이 중요하며, 정확한 용어 매칭, 역인덱스 효율성, 그리고 해석가능성을 동시에 만족해야 한다.

- **Approach**: (1) 최대값 풀링(max pooling)으로 풀링 메커니즘 개선, (2) 쿼리 확장 없는 문서 인코더 버전 제안, (3) 증류 기법을 통한 성능 부스팅

## Achievement

![Figure 1: Performance vs FLOPS for SPLADE models trained](figures/fig1.webp)
*Figure 1: SPLADE 모델들의 성능 대비 연산량(FLOPS) 비교*

1. **NDCG@10 향상**: TREC DL 2019에서 기존 SPLADE 대비 **9% 이상의 성능 향상** 달성
2. **BEIR 벤치마크 최고 성능**: 제로샷 평가에서 BEIR 벤치마크의 최고 성능 달성
3. **효율성 개선**: SPLADE-doc 모델로 모든 계산을 오프라인에서 수행 가능하면서도 경쟁력 있는 성능 유지
4. **MS MARCO 통과**: 증류된 SPLADE (DistilSPLADE-max)로 최신 기술 수준에 근접한 결과 달성

## How

![Figure 2: Performance vs average document length](figures/fig2.webp)
*Figure 2: 문서 길이에 따른 성능 변화 분석*

**핵심 기술 개선사항:**

- **최대값 풀링 (Max Pooling)**: 기존의 로그-포화 합산 연산(Eq. 2)을 최대값 연산(Eq. 6)으로 변경
  ```
  w_j = max_{i∈t} log(1 + ReLU(w_ij))
  ```
  이를 통해 토큰 간 상호작용을 보다 효과적으로 모델링

- **SPLADE-doc (문서 전용 인코더)**: 쿼리 확장 제거로 온라인 추론 비용 감소
  ```
  s(q,d) = Σ_{j∈q} w_d_j
  ```
  문서의 가중치를 모두 오프라인에서 사전 계산

- **FLOPS 정규화**: 역인덱스 효율성을 직접 최적화
  ```
  ℓ_FLOPS = Σ_{j∈V} (1/N Σ_{i=1}^N w(d_i)_j)^2
  ```
  게시 목록(posting list) 균형 분배를 통한 검색 효율성 향상

- **이단계 증류 (Two-stage Distillation)**: 
  1단계: SPLADE 검색기와 크로스-인코더 재정렬기 학습
  2단계: 더 어려운 부정 샘플로 재학습

- **손실 함수**: 대조적 손실(contrastive loss)과 FLOPS 정규화 결합
  ```
  L = L_rank-IBN + λ_q L_q_reg + λ_d L_d_reg
  ```

**훈련 상세:**
- DistilBERT-base 초기화
- ADAM 최적화기 (학습률 2e-5)
- 배치 크기 124, 150k 반복
- 하드 부정 샘플링 (BM25 기반)
- 쿼리와 문서에 대한 별도 정규화 가중치 사용

## Originality

- **풀링 메커니즘 개선의 단순성과 효과성**: 합산에서 최대값으로의 변경이 9% 성능 향상을 가져온 점은 직관적이면서도 혁신적
  
- **문서 전용 모델의 실용성**: 쿼리 확장 없이도 경쟁력 있는 성능을 유지하면서 효율성을 극대화한 설계

- **FLOPS 정규화의 창의적 적용**: 단순한 ℓ1 정규화를 넘어, 실제 검색 효율성(부동소수점 연산)과 직접 연결된 정규화 항 도입

- **체계적인 증류 전략**: 두 단계의 증류 과정으로 점진적으로 어려운 학습 신호 활용

- **종합적 벤치마킹**: MS MARCO, TREC DL, BEIR 등 다양한 평가 데이터셋에서 일관된 개선 입증

## Limitation & Further Study

- **어휘 크기 고정**: BERT WordPiece 어휘(30,522)에 제한되어 도메인 특화 어휘 부족 시 확장성 제약

- **쿼리 확장의 필요성**: SPLADE-max는 여전히 쿼리 확장을 필요로 하여 온라인 추론 비용 증가 (SPLADE-doc은 완화하나 성능 저하)

- **ANN 효과 미평가**: 실험이 정확한 전전계(brute-force) 검색을 기반으로 하여, 실제 ANN 사용 시의 성능 저하 정도가 불명확

- **대규모 컬렉션 검증 부족**: MS MARCO(8.8M 문서)보다 훨씬 큰 실제 운영 규모의 검색 엔진에서의 검증 필요

- **하이퍼파라미터 민감도**: λ_q, λ_d 등 정규화 가중치에 대한 상세한 민감도 분석 부재

**후속 연구 방향:**
- 도메인 적응형 희소 표현 학습
- ANN 검색 시뮬레이션을 통한 실제 검색 효율성 평가
- 매우 큰 규모 컬렉션(10억 이상 문서)에서의 성능 검증
- 다국어 및 크로스랭귀지 검색 확장
- 쿼리-문서 상호작용의 더 정교한 모델링


## Evaluation

- Novelty: 4/5
- Technical Soundness: 5/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4.5/5

**총평**: 본 논문은 SPLADE 모델에 대한 정밀한 개선을 통해 희소 렉시컬 표현 기반 정보검색의 새로운 최고 성능을 달성했으며, 특히 최대값 풀링과 문서 전용 인코더 같은 단순하면서도 효과적인 기법들이 실무 적용 가치가 높다. 다만 초대규모 컬렉션과 실제 ANN 검색 환경에 대한 검증이 더 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/335_Few-shot_Learning_with_Retrieval_Augmented_Language_Models/review]] — 희소 렉시컬 표현과 밀집 표현 기반 검색 증강이라는 서로 다른 정보검색 패러다임의 장단점을 비교할 수 있습니다.
- 🏛 기반 연구: [[papers/593_Openscholar_Synthesizing_scientific_literature_with_retrieva/review]] — 희소-밀집 하이브리드 검색 모델이 대규모 과학문헌 검색 시스템의 첫 단계 검색기로 활용될 수 있는 기술적 기반을 제공합니다.
- 🔗 후속 연구: [[papers/659_REALM_Retrieval-Augmented_Language_Model_Pre-Training/review]] — REALM의 밀집 표현 기반 검색을 희소 표현과 결합한 발전된 형태의 검색 증강 사전학습 모델입니다.
- 🔗 후속 연구: [[papers/224_Clinical_entity_augmented_retrieval_for_clinical_information/review]] — 희소 렉시컬 검색 모델을 임상 엔티티 기반 검색으로 발전시킨 도메인 특화 응용 연구입니다.
- 🔄 다른 접근: [[papers/335_Few-shot_Learning_with_Retrieval_Augmented_Language_Models/review]] — 밀집 표현 기반 검색 증강과 희소 렉시컬 표현 기반 검색의 서로 다른 정보검색 접근법을 제시합니다.
