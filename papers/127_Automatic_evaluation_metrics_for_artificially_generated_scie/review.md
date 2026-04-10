---
title: "127_Automatic_evaluation_metrics_for_artificially_generated_scie"
authors:
  - "Niklas Hoepner"
  - "Leon Eshuijs"
  - "Dimitrios Alivanistos"
  - "Giacomo Zamprogno"
  - "Ilaria Tiddi"
date: "2025"
doi: "arXiv:2503.05712"
arxiv: ""
score: 4.0
essence: "AI가 생성한 과학 논문의 품질 평가를 위해 인용 횟수 예측(Citation Count Prediction)과 리뷰 점수 예측(Review Score Prediction)을 자동 평가 지표로 제안하며, 단순 모델이 LLM 기반 검토자보다 인간 평가와 더 일치함을 입증한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Human-AI_Performance_Detection"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Jain et al._2025_Automatic evaluation metrics for artificially generated scientific research.pdf"
---

# Automatic evaluation metrics for artificially generated scientific research

> **저자**: Niklas Hoepner, Leon Eshuijs, Dimitrios Alivanistos, Giacomo Zamprogno, Ilaria Tiddi | **날짜**: 2025 | **DOI**: [arXiv:2503.05712](https://arxiv.org/abs/2503.05712)

---

## Essence

![Figure 1](figures/fig1.webp) *논문 표현을 위한 context model의 아키텍처: 제목-초록(초록색)과 관련 작업, 방법론, 실험 결과, 결론(파랑색)을 결합하여 처리*

AI가 생성한 과학 논문의 품질 평가를 위해 인용 횟수 예측(Citation Count Prediction)과 리뷰 점수 예측(Review Score Prediction)을 자동 평가 지표로 제안하며, 단순 모델이 LLM 기반 검토자보다 인간 평가와 더 일치함을 입증한다.

## Motivation

- **Known**: 기초 모델(Foundation Models)은 연구 가설 생성, 논문 작성, 동료 검토 등 과학 연구의 여러 단계에서 활용되고 있으며, 일부 도메인 전문가는 AI 생성 가설을 인간이 생성한 것보다 더 참신하다고 평가함
  
- **Gap**: 생성된 과학 콘텐츠의 품질 평가가 핵심 과제이나, 전문가 검토는 비용이 많이 들고 LLM 기반 검토자의 신뢰성 문제가 최근 드러났으며(무작위 추측 수준의 성능), 연구 가설만으로 과학적 품질을 예측하는 연구가 부족하고 미래 작업으로의 일반화가 검증되지 않음

- **Why**: 효율적이고 신뢰할 수 있으며 미래 작업으로 일반화할 수 있는 자동 평가 지표가 필요함

- **Approach**: OpenReview의 모든 제출 논문을 파싱하여 인용 횟수, 참고문헌, 연구 가설로 보강한 후, 인용 횟수 예측과 리뷰 점수 예측을 품질 대리 지표로 비교 분석

## Achievement

![Figure 2](figures/fig2.webp) *다양한 조건에서의 Pearson 상관계수 히트맵: 리뷰 점수와 인용 횟수의 관계*

1. **인용 횟수 예측의 우월성**: 리뷰 점수 예측보다 인용 횟수 예측이 더 실행 가능함을 입증하였으며, 제목과 초록만 사용한 단순 모델도 LLM 기반 검토자를 능가하는 일관성을 보임

2. **데이터셋 구축**: OpenReview의 모든 제출 논문을 통일된 형식으로 파싱하고 추가 메타데이터(인용 횟수, 연구 가설)로 보강한 대규모 데이터셋 제공

3. **예측 난이도 비교**: 전체 논문 정보 대비 연구 가설 정보만으로는 점수 예측이 훨씬 어려우며, 완전한 논문 텍스트의 이점이 명확함을 확인

## How

![Figure 1](figures/fig1.webp) *모델 아키텍처: SPECTER2 embedding을 이용한 문맥 정보 통합*

- **임베딩 방식**: SPECTER2 모델의 회귀 어댑터(Regression Adapter)를 사용하여 과학 논문 텍스트에 맞춘 고품질 표현 생성

- **문맥 모델링**: 제목-초록으로 논문을 표현하고, 관련 작업/방법론/실험 결과/결론 또는 참고문헌의 제목-초록을 문맥으로 활용하여 Transformer 인코더를 통해 처리

- **손실 함수**: (1) 쌍별 비교(Pairwise Comparison)—이진 교차 엔트로피로 두 논문의 상대적 품질 학습, (2) 직접 점수 예측(Direct Score Prediction)—L1 거리로 절대 점수 학습

- **대상 점수**: 인용 횟수는 월별 평균 인용 수의 로그값, 리뷰 점수는 평균 전체 점수 및 영향도(Impact) 점수

- **모델 구조**: 문맥 없음 시 단층 MLP, 문맥 포함 시 Transformer 인코더 층 1개 + MLP

## Originality

- OpenReview 전체 데이터를 통일된 형식으로 파싱하고 인용 횟수 및 연구 가설으로 보강한 최초의 대규모 표준화된 데이터셋 제공으로 기존 연구의 메타데이터 부족 문제 해결

- 연구 가설만으로 과학적 품질 예측 가능성을 최초로 체계적으로 검증

- 인용 횟수와 리뷰 점수의 상관관계를 OpenReview 전체 데이터로 확장하여 분석(기존: ICLR 2017-2019만 분석)

- LLM 기반 검토자와의 직접 성능 비교를 통해 간단한 통계 모델의 신뢰성 우월성을 실증적으로 입증

- 시간적 일반화(Temporal Generalization)를 명시적으로 고려한 실험 설계(기존 연구는 최대 1개월 차이만 검증)

## Limitation & Further Study

- **제한점**: 
  - 단층 모델(단층 MLP, 1개 Transformer 인코더)만 사용하여 과도한 과적합(Overfitting) 방지를 단순하게 처리한 점으로, 더 복잡한 아키텍처의 잠재력 미탐색
  - 인용 횟수 예측이 리뷰 점수 예측보다 우수하더라도 인간 수준의 일관성(Human-level Consistency)에는 미달
  - AI 생성 논문의 특정 특성(예: 특이한 문체, 구조 이상)을 명시적으로 고려하지 않음
  - 도메인별 차이(물리학, 생물학, 컴퓨터 과학 등)가 분석되지 않음

- **후속 연구**:
  - AI 생성 콘텐츠 특화 평가 지표 개발 필요
  - 인용 횟수와 리뷰 점수의 약한 상관관계에 대한 심층 분석
  - 시간에 따른 인용 패턴 변화를 고려한 동적 예측 모델 개발
  - 다양한 도메인 및 학회 간 일반화 성능 검증

## Evaluation

- **Novelty**: 4/5 — OpenReview 전체 파싱 및 AI 생성 과학 콘텐츠 평가 관점의 문제 재설정은 새로우나, 인용/리뷰 점수 예측 자체는 기존 과제

- **Technical Soundness**: 4/5 — SPECTER2 사용, 적절한 손실 함수, 문맥 모델링이 타당하나 모델 아키텍처가 의도적으로 단순하여 성능 상한선 미파악

- **Significance**: 4/5 — LLM 생성 과학 콘텐츠 평가의 실질적 대안 제시 및 표준화 데이터셋 제공의 가치는 높으나, 인간 수준 성능 미달로 실용성 제한

- **Clarity**: 4/5 — 동기, 방법론, 결과 설명이 명확하나 전체 데이터 파싱 프로세스와 통계적 유의성 검정 세부 사항이 부족

- **Overall**: 4/5

**총평**: 이 논문은 AI 생성 과학 콘텐츠 평가의 중요한 문제에 대해 실용적이고 신뢰할 수 있는 자동 지표를 제안하며 대규모 표준화 데이터셋을 제공함으로써 학계에 유의미한 기여를 하고 있으나, 인간 수준 성능 달성과 모델 복잡도 향상 여지가 남아있다.

## Related Papers

- 🏛 기반 연구: [[papers/373_Generalization_Bias_in_Large_Language_Model_Summarization_of/review]] — 대규모 언어 모델 요약의 일반화 편향을 분석하여 AI 생성 논문 평가의 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/678_ReviewerGPT_An_Exploratory_Study_on_Using_Large_Language_Mod/review]] — 논문 심사에서 대규모 언어 모델 사용에 대한 탐색적 연구로 본 논문의 평가 지표를 실제 심사 환경에 적용한다.
- 🔄 다른 접근: [[papers/092_Align_then_Fusion_Generalized_Large-scale_Multi-view_Cluster/review]] — AI 생성 연구의 참신성과 표절 문제를 다루어 본 논문의 품질 평가와 다른 관점의 자동 평가를 제시한다.
