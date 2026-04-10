---
title: "755_Simalign_High_quality_word_alignments_without_parallel_train"
authors:
  - "Masoud Jalili Sabet"
  - "Philipp Dufter"
  - "François Yvon"
  - "Hinrich Schütze"
date: "2021"
doi: "arXiv:2004.08728"
arxiv: ""
score: 4.3
essence: "본 논문은 병렬 학습 데이터 없이 다국어 단어 임베딩(정적 및 문맥화된)을 활용하여 고품질의 단어 정렬을 수행하는 SimAlign 방법을 제안한다. 전통적인 통계적 정렬기(efloral 등)와 비교해서도 우수한 성능을 보인다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Long_Context_Embeddings"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yeginbergenova and Agerri_2020_Simalign High quality word alignments without parallel training data using static and contextualize.pdf"
---

# SimAlign: High quality word alignments without parallel training data using static and contextualized embeddings

> **저자**: Masoud Jalili Sabet, Philipp Dufter, François Yvon, Hinrich Schütze | **날짜**: 2021 | **DOI**: [arXiv:2004.08728](https://arxiv.org/abs/2004.08728)

---

## Essence

![Figure 1](figures/fig1.webp) *다양한 언어 쌍과 혼합 문장에 대한 병렬 학습 데이터 없이 단어 정렬을 수행하는 방법*

본 논문은 병렬 학습 데이터 없이 다국어 단어 임베딩(정적 및 문맥화된)을 활용하여 고품질의 단어 정렬을 수행하는 SimAlign 방법을 제안한다. 전통적인 통계적 정렬기(efloral 등)와 비교해서도 우수한 성능을 보인다.

## Motivation

- **Known**: 통계적 단어 정렬기(IBM 모델, Giza++, fast-align, efloral)와 신경 기계번역(NMT) 기반 정렬 방법이 존재하며, 이들은 기계번역, 주석 투영(annotation projection), 다국어 임베딩 생성 등에 유용함

- **Gap**: 대부분의 기존 방법은 충분한 병렬 학습 데이터를 필요로 하며, 병렬 데이터가 부족한 저자원 언어쌍이나 도메인 특화 환경에서 성능이 급격히 저하됨

- **Why**: 병렬 코퍼스 확보가 어려운 언어쌍이 다수 존재하며, 광산 채취(mining)된 병렬 데이터가 항상 정렬 품질 향상으로 이어지지 않음

- **Approach**: 병렬 데이터 없이 단일언어 데이터에서만 학습된 다국어 임베딩(fastText+VecMap, mBERT, XLM-RoBERTa)의 유사도 행렬(similarity matrix)로부터 단어 정렬을 추출

## Achievement

![Figure 2](figures/fig2.webp) *IterMax 알고리즘: 반복적으로 유사도 행렬을 수정하면서 정렬을 추출*

1. **우수한 성능**: 문맥화된 임베딩(contextualized embeddings)으로부터 얻은 정렬이 100K 병렬 문장으로 학습한 efloral보다 영어-독일어 쌍에서 F1이 5% 포인트 높음 (6개 언어쌍 중 4쌍에서 우수, 2쌍에서 동등)

2. **병렬 데이터 불필요**: 전문 용어 없이 단일언어 데이터만으로 임베딩 학습 가능하여 저자원 언어와 혼합 언어 문장 정렬 가능

3. **유연한 정렬 추출 방법**: 3가지 서로 다른 알고리즘(Argmax, IterMax, Match)으로 정확도(precision)와 재현율(recall)의 트레이드오프 조절 가능

## How

![Figure 3](figures/fig3.webp) *서브단어 수준 정렬을 단어 수준으로 변환하는 프로세스*

### 주요 방법론

- **유사도 행렬 기반 정렬 추출**
  - 병렬 문장 쌍의 각 단어를 d차원 임베딩으로 변환
  - 코사인 유사도를 사용한 유사도 행렬 S ∈ [0,1]^(le×lf) 구성

- **세 가지 정렬 알고리즘**
  - **Argmax**: 단순 베이스라인, 상호 최대값 조건 적용
  - **IterMax** (신규): 이전 반복에서 정렬된 단어쌍의 유사도를 할인 계수 α로 감소시키며 반복 적용 → 희귀 단어 정렬 향상
  - **Match**: 이분 그래프의 최대 무게 정렬(maximum-weight maximal matching) 문제로 프레임화하여 전역 최적해 추구

- **확장 기법**
  - **왜곡 보정(Distortion)**: 상대적 위치 차이에 따른 페널티 적용 (IBM Model 2의 아이디어)
  - **널(Null) 단어 처리**: 높은 엔트로피 임계값 이상 문장의 정렬 제거로 번역되지 않은 단어 모델링

- **임베딩 선택**
  - 정적 임베딩(Static): fastText + VecMap (비지도 다국어 정렬)
  - 문맥화 임베딩(Contextualized): mBERT, XLM-RoBERTa의 여러 계층 활용

- **서브단어 처리**: 서브단어 수준 정렬 후 "임의의 서브단어가 정렬되면 해당 단어 정렬"이라는 휴리스틱으로 단어 수준으로 변환

## Originality

- **새로운 관점**: 전통적 통계 모델 대신 임베딩 유사도 행렬에서 직접 정렬을 추출하는 접근법 (병렬 데이터 불필요)

- **알고리즘 혁신**: IterMax는 탐욕적(greedy) 반복으로 희귀 단어 정렬 개선을 달성하는 간단하면서도 효과적인 방법

- **포괄적 비교**: 정적/문맥화 임베딩 모두 검증하고, 서브단어 vs. 단어 수준 분석, 다양한 언어쌍 평가

- **실용 도구화**: SimAlign 패키지 및 온라인 데모 제공으로 재현성과 접근성 확보

## Limitation & Further Study

- **제한점**
  - mBERT는 104개 언어에만 사전학습되어 있어 저자원/저소수 언어 커버리지 부족
  - 서브단어를 단어로 변환하는 휴리스틱이 언어 및 토크나이저에 따라 성능 편차 발생 가능
  - 왜곡 보정과 널 임계값(τ) 같은 하이퍼파라미터가 경험적으로 설정되어 있어 최적성 보장 불확실
  - 평가가 6개 언어쌍에 한정되어 더 다양한 언어 조합 검증 필요

- **후속 연구**
  - 언어-특화 임베딩(language-specific pretrained models)을 활용한 저자원 언어쌍 성능 향상
  - 동적 하이퍼파라미터 조정을 통한 언어쌍별 최적화
  - 영상/음성 등 다중모달 정렬로의 확장
  - 기계번역 성능 향상에 미치는 영향에 대한 하류 과제(downstream task) 평가


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.3/5

**총평**: SimAlign은 다국어 임베딩의 유사도 행렬에서 단어 정렬을 추출하는 창의적이고 실용적인 방법을 제안하여, 병렬 학습 데이터의 의존성을 제거하면서도 전통적 통계 정렬기를 능가하는 성능을 달성했다는 점에서 의의가 있다. 다만 하이퍼파라미터 최적화와 더 광범위한 언어 커버리지 개선이 향후 과제이다.

## Related Papers

- 🔄 다른 접근: [[papers/119_Autocap_Towards_automatic_cross-lingual_alignment_planning_f/review]] — SimAlign은 병렬 데이터 없는 단어 정렬을, AutoCAP은 다국어 추론에서의 언어 정렬을 다루어 서로 다른 차원의 정렬 문제를 해결함
- 🏛 기반 연구: [[papers/158_Biasfilter_An_inference-time_debiasing_framework_for_large_l/review]] — 다국어 임베딩의 편향 문제를 다루는 BiasFilter와 SimAlign의 크로스링구얼 정렬 방법론이 상호 보완적 관계에 있음
- 🔗 후속 연구: [[papers/858_Unsupervised_crosslingual_representation_learning_at_scale/review]] — 대규모 무감독 크로스링구얼 표현 학습이 SimAlign의 정적/문맥화 임베딩 활용 방식을 더 큰 규모로 확장한 연구임
- 🔄 다른 접근: [[papers/119_Autocap_Towards_automatic_cross-lingual_alignment_planning_f/review]] — AutoCAP이 다국어 추론에서의 자동 언어 선택과 가중치 할당에 초점을 맞춘 반면, SimAlign은 병렬 데이터 없는 단어 수준 정렬에 특화되어 상호 보완적 접근법을 제시함
