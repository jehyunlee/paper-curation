---
title: "421_Improving_demonstration_diversity_by_human-free_fusing_for_t"
authors:
  - "Dingzirui Wang"
  - "Longxu Dou"
  - "Xuanliang Zhang"
  - "Qingfu Zhu"
  - "Wanxiang Che"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "본 논문은 대규모 언어모델(LLM)의 문맥 내 학습(in-context learning)을 활용한 Text-to-SQL 작업에서 시연(demonstration) 풀의 다양성을 측정하고 향상시키는 방법을 제안한다. 기존의 인간 라벨링 기반 시연 선택 방식의 낮은 다양성과 높은 비용 문제를 해결하기 위해 FUSED(FUSing itEratively for Demonstrations) 방법을 도입한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Academic_Writing_Diversity"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2024_Improving demonstration diversity by human-free fusing for text-to-sql.pdf"
---

# Improving demonstration diversity by human-free fusing for text-to-sql

> **저자**: Dingzirui Wang, Longxu Dou, Xuanliang Zhang, Qingfu Zhu, Wanxiang Che | **날짜**: 2024 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) *기준선(좌)과 FUSED(우)의 시연(demonstration) 풀 구성 비교. FUSED는 기존 라벨링 없이도 또는 인간 개입 없이 시연 풀을 합성하고 다양성을 향상시킬 수 있음*

본 논문은 대규모 언어모델(LLM)의 문맥 내 학습(in-context learning)을 활용한 Text-to-SQL 작업에서 시연(demonstration) 풀의 다양성을 측정하고 향상시키는 방법을 제안한다. 기존의 인간 라벨링 기반 시연 선택 방식의 낮은 다양성과 높은 비용 문제를 해결하기 위해 FUSED(FUSing itEratively for Demonstrations) 방법을 도입한다.

## Motivation

- **Known**: 현재 Text-to-SQL 작업은 LLM 기반 문맥 내 학습이 주류이며, 인간 라벨링된 시연 풀에서 관련된 시연을 선택하는 연구가 진행되고 있음

- **Gap**: 
  1. **낮은 다양성(Low Diversity)**: 동일 주석자의 라벨링 데이터는 유사성이 높아 다양성 부족
  2. **높은 비용(High Cost)**: 인간 라벨링에 막대한 노동력 필요

- **Why**: 시연 풀의 다양성이 높을수록 예측 불가능한 사용자 질문들에 대해 더 나은 시연을 제공할 수 있음. 따라서 다양성을 정량적으로 측정하고 체계적으로 향상시키는 방법이 필요함

- **Approach**: 
  1. 시연 풀 다양성을 측정하는 지표(DM, Diversity Measurement) 제안
  2. LLM을 활용하여 기존 라벨링 데이터로부터 또는 처음부터 반복적으로 시연을 합성하는 FUSED 방법 개발

## Achievement

![Figure 4, 5](figures/fig4.webp) *기존 라벨링 데이터의 DM 값과 성능 분석. 더 높은 DM을 가진 시연 풀의 존재를 시각적으로 확인*

1. **다양성 지표 정의**: 사용자 질문 중 시연 풀의 가장 유사한 시연과의 유사도가 최소인 질문을 기반으로 하는 DM 지표 도입. 기존 라벨링의 다양성이 추가로 향상될 수 있음을 증명

2. **성능 개선**: 
   - 기존 라벨링 기반: 평균 **3.2% 성능 향상**
   - 처음부터 합성: 평균 **5.0% 성능 향상**
   - Spider, KaggleDBQA 등 주요 벤치마크에서 검증

3. **비용 절감**: 인간 라벨링 없이 LLM 기반 자동 합성으로 라벨링 비용 제거

## How

![Figure 3](figures/fig3.webp) *FUSED의 파이프라인: (1) 시연 샘플링, (2) 시연 융합 단계로 구성*

**FUSED의 반복적 융합 프로세스:**

- **단계 1: 시연 샘플링(Demonstration Sampling)**
  - 인코더를 사용하여 모든 시연의 질문을 벡터로 인코딩
  - K-means 클러스터링으로 유사 시연들을 그룹화
  - 서로 다른 클러스터에서 무작위로 시연 샘플링하여 다양성 확보

- **단계 2: 시연 융합(Demonstration Fusing)**
  - 샘플링된 시연들과 무작위 선택 데이터베이스를 LLM에 입력
  - LLM이 여러 시연의 특성을 결합하되 기존 시연과 구별되는 새로운 시연 생성
  - 생성된 시연을 시연 풀에 추가

- **반복 및 누적**: 위 과정을 여러 번 반복하여 점진적으로 다양한 시연 풀 구성

- **초기화 옵션**: 인간 라벨링 데이터로 시작하거나 LLM으로 처음부터 합성 가능

## Originality

- **DM(Diversity Measurement) 지표의 신규성**: 사용자 질문 관점에서 시연 풀의 다양성을 정량화한 새로운 메트릭으로, 기존의 단순한 다양성 개념을 형식화함

- **반복적 융합 전략**: 단순 생성이 아닌 여러 시연의 특성을 조합하여 의도적으로 새로운 속성의 시연을 만드는 창의적 접근

- **이론적 기초**: 제안된 방법이 DM을 향상시킬 수 있음을 이론적으로 증명 (Appendix D)

- **인간 개입 제거**: 기존 라벨링을 활용하면서도 추가 인간 라벨링 없이 다양성 개선

## Limitation & Further Study

**한계점:**

- DM 지표의 계산이 전체 사용자 질문 집합에 의존하므로, 데이터셋 특성에 따라 일반화 가능성이 제한될 수 있음

- 시연 융합 과정에서 LLM의 생성 품질(정확도, 문법성)에 대한 상세한 검토 부재

- 클러스터 수 k 선택의 기준이 명확하지 않으며, 최적값에 대한 분석 부족

- 계산 비용: 반복적 LLM 호출로 인한 실행 시간 및 비용 분석 미흡

**향후 연구:**

- 다양한 텍스트 생성 작업(요약, 기계 번역 등)으로의 일반화 가능성 탐색

- 다른 다양성 측정 지표와의 체계적 비교 연구

- 더 효율적인 클러스터링 및 샘플링 전략 개발

- 생성된 시연의 품질 자동 평가 메커니즘 도입

## Evaluation

- **Novelty**: 4/5
  - DM 지표와 반복적 융합 아이디어는 참신하나, 기본 개념은 기존 연구의 자연스러운 확장

- **Technical Soundness**: 4/5
  - 방법론은 논리적이고 실험이 적절하나, 일부 설계 선택(클러스터링, 초기화)의 정당성이 부족

- **Significance**: 4/5
  - Text-to-SQL 성능 개선이 실질적이고 비용 절감이 의미 있으나, 개선 폭이 중간 수준

- **Clarity**: 4/5
  - 전반적으로 명확하나 일부 기술 세부사항(DM 계산 과정, 데이터베이스 표현)이 부록에만 설명됨

- **Overall**: 4/5

**총평**: 본 논문은 Text-to-SQL 작업의 시연 풀 다양성을 체계적으로 측정하고 개선하는 실용적인 방법을 제안한다. DM 지표는 명확한 동기를 가지고 있으며, FUSED 방법은 라벨링 비용을 절감하면서도 일관된 성능 향상을 달성했다. 다만 일부 설계 선택의 이론적 근거가 보강되고 생성된 시연의 품질에 대한 상세 분석이 있으면 더욱 우수한 논문이 될 것으로 판단된다.

## Related Papers

- 🔄 다른 접근: [[papers/405_Hit-scir_at_mmnlu22_Consistency_regularization_for_multiling/review]] — 다양성 향상에서 무인 융합 방법과 일관성 정규화 방법이 서로 다른 접근 방식을 제시합니다.
- 🏛 기반 연구: [[papers/335_Few-shot_Learning_with_Retrieval_Augmented_Language_Models/review]] — 검색 증강 언어모델의 소수샷 학습이 시연 다양성 개선의 기초적인 방법론을 제공합니다.
- 🔄 다른 접근: [[papers/636_Prompt_to_be_consistent_is_better_than_self-consistent_few-s/review]] — 소수샷 학습에서 시연 다양성과 일관성 프롬프팅의 서로 다른 성능 향상 전략을 비교할 수 있습니다.
- 🔄 다른 접근: [[papers/405_Hit-scir_at_mmnlu22_Consistency_regularization_for_multiling/review]] — Text-to-SQL에서의 무인 융합 다양성 향상과 SLU에서의 일관성 정규화가 서로 다른 다양성 증진 방법을 제시합니다.
