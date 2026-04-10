---
title: "346_Foundation-Model_Surrogates_Enable_Data-Efficient_Active_Lea"
authors:
  - "Jeffrey Hu"
  - "Rongzhi Dong"
  - "Ying Feng"
  - "Ming Hu"
  - "Jianjun Hu"
date: "2026.03"
doi: "10.48550/arXiv.2603.12567"
arxiv: ""
score: 4.2
essence: "소재 발견을 위한 능동 학습(Active Learning, AL)에서 기존 가우스 프로세스(GP)와 랜덤 포레스트(RF) 서로게이트 모델의 한계를 극복하기 위해, 트랜스포머 기반의 기초 모델(Foundation Model, FM)인 TabPFN을 서로게이트로 도입하는 문맥 내 능동 학습(In-Context Active Learning, ICAL) 프레임워크를 제안한다. TabPFN은 메타 학습을 통해 소량의 실험 데이터에서도 표현력 높은 예측과 보정된 불확실성을 동시에 제공한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Agent_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Hu et al._2026_Foundation-Model Surrogates Enable Data-Efficient Active Learning for Materials Discovery.pdf"
---

# Foundation-Model Surrogates Enable Data-Efficient Active Learning for Materials Discovery

> **저자**: Jeffrey Hu, Rongzhi Dong, Ying Feng, Ming Hu, Jianjun Hu | **날짜**: 2026-03-24 | **DOI**: [10.48550/arXiv.2603.12567](https://doi.org/10.48550/arXiv.2603.12567)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: 기초 모델이 능동 학습의 서로게이트 모델링 딜레마를 해결함. (a) 기존 모델들은 예측 능력과 불확실성 추정 간의 트레이드오프 직면 (b) 기초 모델은 메타 학습된 사전 정보를 통해 표현력 높은 예측과 보정된 불확실성 결합*

소재 발견을 위한 능동 학습(Active Learning, AL)에서 기존 가우스 프로세스(GP)와 랜덤 포레스트(RF) 서로게이트 모델의 한계를 극복하기 위해, 트랜스포머 기반의 기초 모델(Foundation Model, FM)인 TabPFN을 서로게이트로 도입하는 문맥 내 능동 학습(In-Context Active Learning, ICAL) 프레임워크를 제안한다. TabPFN은 메타 학습을 통해 소량의 실험 데이터에서도 표현력 높은 예측과 보정된 불확실성을 동시에 제공한다.

## Motivation

- **Known**: 능동 학습은 소재 발견에서 비용이 많이 드는 실험 평가를 효율화하는 강력한 방법. 현재 실무에서는 GP(원리적 불확실성 추정이지만 모델 표현력 제한) 또는 RF(높은 표현력이지만 소량 데이터에서 비신뢰적 불확실성)를 주로 사용

- **Gap**: 소재 과학 데이터의 전형적 특성(57%가 500개 미만 샘플)에서 "모델 정확도"와 "신뢰적 불확실성" 사이의 기본적 트레이드오프가 미해결 상태

- **Why**: 능동 학습의 획득 함수(acquisition function)는 신뢰적 불확실성을 통해서만 탐색-활용(exploration-exploitation) 균형을 효과적으로 맞출 수 있으므로, 서로게이트 모델의 불확실성 보정이 성능을 좌우함

- **Approach**: 메타 학습을 통해 백만 개의 합성 회귀 과제로 사전학습된 TabPFN을 서로게이트 모델로 도입. 데이터별 재훈련 없이 단일 순전파로 베이지안 추론을 근사하여 소량 데이터 환경에 최적화

## Achievement

![Figure 3](figures/fig3.webp)
*그림 3: Cu 경도(hardness) 데이터셋에서 ICAL의 성능. (a-b) TabPFN vs GP 비교*

![Figure 4](figures/fig4.webp)
*그림 4: (a)(c) Cu 전기전도도 및 (b)(d) 벌크 금속 유리(Glass_DS3) 데이터셋에서의 비교*

1. **평가 효율성 개선**: 10개 소재 데이터셋 중 8개에서 TabPFN이 최소 평가 횟수 달성. GP 대비 평균 52%, RF 대비 29.77% 평가 횟수 감소

2. **불확실성 보정 우월성**: 크로스 밸리데이션 분석 결과, TabPFN이 가장 낮은 음의 로그 우도(Negative Log-Likelihood, NLL)와 희소화 오류 곡선 아래 면적(Area Under the Sparsification Error curve, AUSE)을 달성하여 우수한 불확실성 보정 증명

## How

![Figure 2](figures/fig2.webp)
*그림 2: 소재 발견을 위한 풀 기반 능동 학습 파이프라인. EI(Expected Improvement)는 다른 획득 함수로 대체 가능*

![Figure 5](figures/fig5.webp)
*그림 5: 원소 농도 특성을 사용한 LTC_conc 데이터셋에서의 ICAL 성능 비교*

- **기초 모델 선택**: TabPFN은 트랜스포머 기반으로 수백만 개의 합성 회귀 과제에 대해 메타학습을 통해 함수 공간에 대한 보편적 사전(universal prior) 습득

- **추론 메커니즘**: 데이터셋별 그래디언트 기반 최적화 없이 단일 순전파로 전체 예측 분포(predictive distribution) 출력. GP처럼 원리적이지만 RF/NN 수준의 표현력 제공

- **획득 함수 개선**: 탐욕적 획득(greedy acquisition)의 중복 쿼리 문제를 해결하기 위해 품질(획득 함수 점수)과 다양성(diversity) 균형을 맞추는 샘플 선택 전략 도입

- **구현 방식**: 기존 AL 루프에 즉시 통합 가능. 매 반복마다 새 데이터를 포함하여 TabPFN의 문맥 내 학습(in-context learning) 수행

## Originality

- **기초 모델의 AL 응용**: 기초 모델(특히 정제된 베이지안 추론 근사 모델)을 전통적 AL 서로게이트로 대체한 것이 새로운 시도. 기존 소재 발견 AL 연구들은 GP/RF/NN 중심이었음

- **메타학습을 통한 소량 데이터 해결**: 합성 과제 메타학습이라는 패러다임을 통해 소량 데이터 환경에서 표현력과 불확실성을 동시에 해결한 점이 획기적

- **보편적 불확실성 보정**: 데이터별 특화 모델 없이도 NLL과 AUSE 지표에서 우월한 보정을 달성한 것이 기존의 휴리스틱 불확실성 추정과 차별화

- **다중 소재 시스템 검증**: 구리 합금, 벌크 금속 유리, 결정 격자 열전도도, 전해질 등 다양한 소재 클래스에 걸친 광범위 벤치마킹으로 범용성 입증

## Limitation & Further Study

- **데이터셋 크기 한계**: 실험 평가 횟수 감소를 정량적으로 검증했지만, 아직 실제 실험실 자동화(self-driving lab, SDL) 환경에서의 폐루프 검증 부재

- **TabPFN의 설계 영역**: 현재 정제된 수치적 표 형식(tabular) 데이터에 최적화. 고차원 화학 그래프 특성이나 구조 특성을 포함한 확장 가능성 미검토

- **계산 비용 분석 부족**: 순전파 효율성은 언급되었으나, GP의 O(n³) 복잡도 대비 TabPFN의 정확한 계산 오버헤드(예: 컨텍스트 윈도우 크기, GPU 메모리) 상세 분석 필요

- **획득 함수 일반화**: 현재 EI 중심으로 평가. 다른 획득 함수(UCB, Thompson Sampling 등)에서 TabPFN의 우수성이 유지되는지 확인 필요

- **후속 연구 방향**:
  - 고차원 특성 공간 및 그래프 신경망 통합 검토
  - 실제 SDL 파이프라인과의 엔드-투-엔드 통합
  - 다중-목표 소재 최적화(multi-objective optimization) 확장
  - 전이 학습을 통한 관련 소재 도메인 간 성능 향상


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.2/5

**총평**: 본 논문은 기초 모델의 메타학습 능력을 소재 발견 능동 학습의 핵심 문제(표현력 vs. 불확실성 트레이드오프)에 창의적으로 적용하였으며, 광범위한 벤치마크로 우월성을 입증했다. 다만 실제 실험 환경 검증과 고차원 특성 공간 확장이 완성되면 임팩트가 더욱 강화될 것으로 예상된다.

## Related Papers

- 🧪 응용 사례: [[papers/451_Knowledge-guided_large_language_model_for_material_science/review]] — 재료과학 LLM 방법론을 능동 학습 기반 소재 발견에 구체적으로 적용하는 실용적 사례입니다.
- 🔗 후속 연구: [[papers/037_A_Survey_on_Uncertainty_Quantification_Methods_for_Deep_Lear/review]] — 불확실성 정량화를 기초 모델 기반 능동 학습으로 확장하여 데이터 효율성을 크게 개선합니다.
- 🔄 다른 접근: [[papers/626_Polymer_Brushes_and_Grafted_Polymers_AIML-Driven_Synthesis_S/review]] — 소재 발견을 위한 AI/ML 워크플로우라는 동일한 목표를 다른 재료 시스템(일반 vs 중합체)으로 접근합니다.
- 🏛 기반 연구: [[papers/451_Knowledge-guided_large_language_model_for_material_science/review]] — 재료 발견을 위한 능동 학습 시스템의 도메인 특화 언어 모델 기반을 제공합니다.
- 🔄 다른 접근: [[papers/626_Polymer_Brushes_and_Grafted_Polymers_AIML-Driven_Synthesis_S/review]] — 소재 연구 자동화라는 동일한 목표를 중합체와 일반 소재라는 다른 재료 시스템으로 접근합니다.
- 🔗 후속 연구: [[papers/258_Deep_active_learning_based_experimental_design_to_uncover_sy/review]] — 기초 모델 기반 대리 모델이 HIV 감염 유전자 상호작용 발견에서 능동학습을 더욱 효율화할 수 있습니다.
