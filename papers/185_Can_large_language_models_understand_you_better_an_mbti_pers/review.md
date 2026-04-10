---
title: "185_Can_large_language_models_understand_you_better_an_mbti_pers"
authors:
  - "Bohan Li"
  - "Jiannan Guan"
  - "Longxu Dou"
  - "Yunlong Feng 외"
date: "2024"
doi: "arXiv:2412.12510"
arxiv: ""
score: 4.0
essence: "본 논문은 **Myers-Briggs Type Indicator (MBTI) 성격 탐지의 과도한 낙관성을 개선**하기 위해, 심리학 전문가의 지도 하에 심리 전문가가 직접 주석을 단 **첫 번째 소프트 라벨 MBTI 데이터셋 MBTIBENCH**를 구축했다. 이는 자기보고식 라벨의 부정확성(29.58% 오류)과 극단적 성격만 표현하는 하드 라벨의 한계를 해결한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Academic_Writing_Personalization"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Fong et al._2024_Can large language models understand you better an mbti personality detection dataset aligned with.pdf"
---

# Can Large Language Models Understand You Better? An MBTI Personality Detection Dataset Aligned with Population Traits

> **저자**: Bohan Li, Jiannan Guan, Longxu Dou, Yunlong Feng 외 | **날짜**: 2024 | **DOI**: [arXiv:2412.12510](https://arxiv.org/abs/2412.12510)

---

## Essence

![Figure 1](figures/fig1.webp)
*MBTIBENCH의 초점: 기존 MBTI 성격 탐지 데이터셋의 데이터 품질 문제와 소프트 라벨 부재 해결*

본 논문은 **Myers-Briggs Type Indicator (MBTI) 성격 탐지의 과도한 낙관성을 개선**하기 위해, 심리학 전문가의 지도 하에 심리 전문가가 직접 주석을 단 **첫 번째 소프트 라벨 MBTI 데이터셋 MBTIBENCH**를 구축했다. 이는 자기보고식 라벨의 부정확성(29.58% 오류)과 극단적 성격만 표현하는 하드 라벨의 한계를 해결한다.

## Motivation

- **Known**: 
  - MBTI는 가장 널리 인식된 비임상 성격 모델로, 소셜 미디어 텍스트로부터 자동으로 성격 유형을 탐지하는 연구가 활발함
  - 기존 Twitter, Kaggle, PANDORA 데이터셋이 존재함

- **Gap**: 
  - (1) 기존 데이터셋은 사용자의 **자기보고식 MBTI 라벨**을 사용하는데, 자기인식의 부정확성으로 인해 자기보고 라벨과 실제 텍스트의 성격 특성이 불일치 (예: 외향형이라고 자기보고했으나 텍스트에는 내향형 특성 드러남)
  - (2) 기존 데이터셋은 **이진 하드 라벨(hard labels)만 사용**하지만, 심리학적으로 대부분의 사람은 극단적 성격이 아닌 중간 정도의 성격을 보임

- **Why**: 
  - 성격 탐지의 현실적 정확성 향상 필요
  - 인구 통계적 성격 특성과 실제 데이터 분포의 정렬 필요

- **Approach**: 
  - 데이터 필터링 가이드라인 수립 (라벨 누수, 쓸모없는 잡음 제거)
  - 심리학자 지도 하 수동 재주석
  - **극성 경향(polarity tendency)** 도출을 통한 소프트 라벨 추정

## Achievement

![Figure 2](figures/fig2.webp)
*MBTI의 4가지 차원 정의: 외향성/내향성(E/I), 감각/직관(S/N), 사고/감정(T/F), 판단/인식(J/P)*

1. **데이터 품질 개선**: 라벨 누수(직접 성격 누수, 성격 특성 누수, 교차 이론 특성 누수)와 쓸모없는 잡음(정보 부족, 깨진 텍스트, 링크/미디어) 제거로 기존 데이터셋의 **29.58% 오류 해결**

2. **소프트 라벨 도입**: [0, 1] 범위의 연속 표현으로 극성 경향 표현 (예: 외향성 40% = 내향성 60%), 비극단적 성격 특성을 가진 사람이 더 많음을 확인

3. **LLM 편향 분석**: 6개 대규모 언어모델(LLM)과 4가지 프롬프팅 방법 평가로 **극단화된 예측(polarized predictions)과 편향**을 주요 연구 방향으로 제시

## How

![Figure 3](figures/fig3.webp)
*MBTIBENCH 구축 워크플로우: 데이터 필터링 → 주석 학습 → 형식적 주석 → 소프트 라벨 추정*

- **데이터 필터링 가이드라인**:
  - 라벨 누수 3가지 유형 정의 및 제거
  - 쓸모없는 잡음 3가지 유형 정의 및 제거
  - 100단어 이상 기준, 깨진 텍스트·링크 제거

- **주석 프로세스**:
  - 심리학 박사과정 학생이 참여한 가이드라인 수립
  - 시험 주석을 통한 전문가 가이드라인 생성
  - 경험 많은 주석자를 통한 형식적 주석 수행
  - 전문가 재검증 및 품질 보증

- **소프트 라벨 추정**:
  - 각 샘플의 극성 경향(polarity tendency) 도출
  - 4개 차원 각각에 대한 극성 정도를 [0, 1] 범위로 표현
  - 기존 3개 데이터셋(Twitter, Kaggle, PANDORA)의 테스트셋 재구축

## Originality

- **첫 번째 MBTI 성격 탐지용 데이터 필터링 가이드라인** 제시 (라벨 누수 3유형, 쓸모없는 잡음 3유형)

- **첫 번째 소프트 라벨 MBTI 데이터셋** 구축으로 심리학적 현실성 향상

- **성격 탐지의 과도한 낙관성에 대한 비판적 관점** 제시 (자기보고식 라벨 부정확성, 극단화된 표현의 한계)

- 심리학 전문가 지도 하의 수동 재주석으로 **높은 데이터 품질 보증**

- LLM의 극단화된 예측과 편향을 구체적으로 분석하는 **새로운 평가 관점**

## Limitation & Further Study

- **데이터셋 규모**: 3개 기존 데이터셋의 테스트셋만 재구축했으므로 전체 데이터셋 규모가 상대적으로 제한적일 수 있음

- **소프트 라벨 추정 방법론**: 극성 경향 도출 방식이 명시적으로 상세히 설명되지 않아, 소프트 라벨의 신뢰도 검증 필요

- **LLM 편향의 원인 분석**: 극단화된 예측이 발생하는 근본 원인에 대한 심화 분석 부족

- **후속 연구 방향**:
  - 소프트 라벨이 다른 심리학적 과제(Big Five 등)에 미치는 영향 조사
  - LLM의 극단화 예측 완화 방법 개발
  - 다국어 MBTI 데이터셋 확장
  - 실시간 소셜 미디어 데이터로 데이터셋 지속 업데이트

## Evaluation

- **Novelty**: 4.5/5
  - 첫 소프트 라벨 MBTI 데이터셋, 데이터 필터링 가이드라인 등 신규성 높음
  - 다만 소프트 라벨 추정 기술의 창의성은 중간 정도

- **Technical Soundness**: 4/5
  - 심리학 전문가 참여와 체계적 주석 프로세스로 기술적 타당성 우수
  - 소프트 라벨 도출 방법론의 수학적 엄밀성 부족

- **Significance**: 4.5/5
  - 기존 MBTI 연구의 과도한 낙관성을 비판하고 현실적 대안 제시
  - 실무적 가치와 심리학적 현실성 모두 높음
  - LLM 편향 분석은 향후 연구에 중요한 지표 제공

- **Clarity**: 3.5/5
  - 전반적 논리 구조는 명확하나, 소프트 라벨 추정 과정이 상세하지 않음
  - Figure가 풍부하여 이해를 돕지만, 기술적 세부사항 기술 필요

- **Overall**: 4/5

**총평**: 본 논문은 MBTI 성격 탐지 연구의 **데이터 품질 문제와 심리학적 현실성 간극을 체계적으로 해결**한 의미 있는 기여다. 특히 심리학 전문가와의 협업을 통한 고품질 재주석과 소프트 라벨 도입은 향후 성격 탐지 및 LLM의 심리 이해도 평가에 중요한 벤치마크를 제공할 것으로 기대된다.

## Related Papers

- 🏛 기반 연구: [[papers/838_Training_socially_aligned_language_models_in_simulated_human/review]] — 시뮬레이션된 인간 사회에서 사회적으로 정렬된 언어 모델 훈련 연구로 본 논문의 성격 탐지 데이터셋 구축의 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/879_What_factors_affect_multimodal_in-context_learning_an_in-dep/review]] — 다중모달 맥락 내 학습에 영향을 미치는 요인들을 심층 분석하여 본 논문의 성격 탐지 연구를 확장한다.
- 🧪 응용 사례: [[papers/613_Personalized_graph-based_retrieval_for_large_language_models/review]] — 대규모 언어 모델을 위한 개인화된 그래프 기반 검색에서 본 논문의 MBTI 성격 정보를 개인화 요소로 활용할 수 있다.
