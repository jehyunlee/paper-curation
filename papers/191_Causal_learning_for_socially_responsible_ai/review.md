---
title: "191_Causal_learning_for_socially_responsible_ai"
authors:
  - "Lu Cheng"
  - "Ahmadreza Mosallanezhad"
  - "Paras Sheth"
  - "Huan Liu"
date: "2021"
doi: "N/A"
arxiv: ""
score: 0
essence: "본 논문은 AI의 사회적 책임성(Social Responsibility)을 강화하기 위해 인과학습(Causal Learning, CL)의 7가지 도구를 체계적으로 분석하고, 편향 완화, 공정성, 투명성, 일반화 가능성 등 주요 SRAI 과제에 적용하는 방법론을 제시한다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Domain-specific_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Cheng et al._2021_Causal learning for socially responsible ai.pdf"
---

# Causal learning for socially responsible ai

> **저자**: Lu Cheng, Ahmadreza Mosallanezhad, Paras Sheth, Huan Liu | **날짜**: 2021 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: CL for SRAI의 분류체계. 파란 사각형은 SRAI에 일반적으로 사용되는 4가지 인과학습 도구를 나타냄*

본 논문은 AI의 사회적 책임성(Social Responsibility)을 강화하기 위해 인과학습(Causal Learning, CL)의 7가지 도구를 체계적으로 분석하고, 편향 완화, 공정성, 투명성, 일반화 가능성 등 주요 SRAI 과제에 적용하는 방법론을 제시한다.

## Motivation

- **Known**: AI 시스템은 높은 정확도를 추구하면서도 데이터 생성 과정(DGP, Data Generating Process)에 대한 이해 부족으로 인해 사회적 편견과 차별을 내재화하는 경향이 있다. 또한 통계적 상관관계만으로는 인과관계를 파악할 수 없어 AI의 의사결정 메커니즘을 제대로 이해하기 어렵다.

- **Gap**: 기존 AI 공정성 연구는 주로 사후(post-hoc) 평가에 집중하며, AI 시스템이 실제로 어떤 인과적 경로를 통해 편향된 결정을 내리는지 규명하지 못한다. 또한 AI 시스템의 사회적 책임성을 근본적으로 향상시킬 수 있는 통합적 프레임워크가 부재하다.

- **Why**: Pearl의 인과 계층구조(association → intervention → counterfactual)에 따라 통계적 상관관계뿐 아니라 인과적 개입과 반사실적 추론이 가능할 때, AI 시스템의 편향된 의사결정 경로를 명확히 파악하고 개선할 수 있다. 이는 AI의 투명성, 공정성, 일반화 가능성을 동시에 증진한다.

- **Approach**: 인과학습의 7가지 주요 도구(인과가정, Do-calculus, 반사실 분석, 중재분석, 적응성, 결측 데이터 처리, 인과 발견)를 분류하고, 이 중 4가지(인과가정, Do-calculus, 반사실 분석, 적응성)가 편향 완화, 공정성, 투명성, 불변성/일반화 가능성 달성에 어떻게 기여하는지 실증적으로 검토한다.

## Achievement

1. **7가지 인과학습 도구의 체계적 분류**: 
   - 인과가정(Causal Assumptions)은 AI 시스템을 더 투명하고 검증 가능하게 만든다
   - Do-calculus는 혼재변수(confounding)를 제거하여 허위 상관관계를 배제한다
   - 반사실 분석(Counterfactual Analysis)은 "만약 X였다면" 질문의 답변을 가능하게 한다
   - 중재분석(Mediation Analysis)은 인과효과를 직접효과와 간접효과로 분해한다
   - 적응성(Adaptability)은 환경 변화에서 AI의 성능 저하를 해결한다

2. **SRAI 4대 과제에 대한 구체적 응용 방법론 제시**:
   - 편향 완화: 성향점수(Propensity Score), 반사실 데이터 증강(CDA), 인과그래프 활용
   - 공정성: 인과 모델링을 통한 민감속성의 인과효과 추정
   - 투명성: 반사실 설명(Counterfactual Explanation)과 개입 기반 방법
   - 불변성/일반화: Invariant Risk Minimization(IRM), 인과 발견 알고리즘(causal discovery)

## How

![Figure 2](figures/fig2.webp)
*Figure 2: 인기도 편향을 완화하기 위한 인과그래프*

### 편향 완화 (Bias Mitigation)

- **성향점수(Propensity Score)**: 역성향점수 가중치(Inverse Propensity Scoring, IPS)를 사용하여 추천 시스템의 선택 편향(selection bias)과 위치 편향(position bias) 제거
  - 수식: $\arg\min_{\theta} \sum_{O_{u,i}=1} \frac{\hat{\sigma}_{u,i}(r, \hat{r}(\theta))}{P_{u,i}} + \text{Reg}(\theta)$
  - 관찰된 평점이 실제 선호도를 반영하도록 가중치 조정

- **반사실 데이터 증강(CDA)**: 원본 데이터의 민감속성을 인과적으로 개입하여 수정된 데이터 생성
  - 정의: 주어진 데이터셋 S와 개입 c에 대해, c-증강 데이터셋 S' = S ∪ {(c(x), y)}_{(x,y)∈S}
  - NLP 예시: 성별 편향 제거를 위해 문장 템플릿으로 (he:she, her:him/his) 쌍을 체계적으로 교체
  - 감정 분석: 인간 주석자가 긍정 리뷰를 부정 리뷰로 최소한으로 수정하여 균형잡힌 데이터 생성

- **인과그래프 활용**: 민감속성과 결과변수 간의 인과경로를 명시적으로 구조화
  - 추천 시스템의 인기도 편향 완화: 사용자 클릭 = 사용자 관심 + 아이템 인기도로 분해
  - 두 개의 서로 다른 임베딩(사용자 실제 관심 vs. 인기도 기반 의사관심)으로 모델링하여 편향 제거

### 공정성 (Fairness)

![Figure 3](figures/fig3.webp)
*Figure 3: 불변성을 위한 반사실 데이터 증강*

- **인과 모델링 기반 공정성**: 민감속성(예: 성별)의 결과에 대한 인과효과(Causal Effect)를 추정하고 제약
  - 직접 인과효과(Direct Causal Effect, DCE): 민감속성이 직접 영향을 주는 경로만 측정
  - 간접 인과효과(Indirect Causal Effect, ICE): 중재변수를 통한 간접 경로 측정
  - 공정성 정의: 민감속성이 결과에 미치는 모든 인과효과가 제로(zero)가 되도록 제약

- **반사실 공정성**: 특정 개인에 대해 "만약 그의 민감속성이 달랐다면 결과가 어떻게 달라졌을까"를 평가
  - 개인 수준의 공정성 보장: 각 개인별로 동일한 내재 자질에 대해 동일한 의사결정을 받도록 함

### 투명성 (Transparency)

- **반사실 설명(Counterfactual Explanation)**: "이 결정이 변경되려면 어떤 입력값이 달라져야 하는가"를 제시
  - 모델 기반 설명: 학습된 인과모델을 통해 생성
  - 개입 기반 설명: 실제 개입 실험 데이터 기반

- **인과가정의 명시화**: 모델 내 인과가정을 명확히 문서화하고 데이터와의 호환성 검증
  - 투명성 향상: 알고리즘의 내부 로직이 아닌 인과적 가정 기반의 설명

### 일반화 가능성/불변성 (Generalizability/Invariance)

- **Invariant Risk Minimization(IRM)**: 여러 환경에서 불변인 인과 특성(invariant features)을 학습
  - 기존 방법의 한계: 환경 변화(distribution shift)에서 모델 성능 급격히 저하
  - IRM 접근: 각 환경의 데이터 p_e(y|x)에서 불변 선형 분류기 w*를 찾음

- **인과 발견(Causal Discovery)**: 관찰 데이터에서 변수 간 인과 방향성을 자동으로 학습
  - 실제 세계에서 인과그래프가 대부분 미지수이므로, 데이터 기반으로 인과구조 추정

## Originality

- **통합적 분류체계**: 기존에 산발적으로 다루어지던 AI 공정성 관련 인과학습 방법들을 7가지 도구 중심으로 처음 체계적으로 분류하고 분석

- **Pearl의 인과 계층구조 적용**: 통계적 상관(association) → 인과적 개입(intervention) → 반사실 추론(counterfactual)의 3계층을 SRAI 프레임워크로 명확히 정의

- **다분야 응용 사례 통합**: NLP, 추천시스템, 컴퓨터 비전 등 여러 분야의 구체적 사례를 하나의 인과학습 틀로 설명

- **SRAI의 인과론적 재정의**: AI의 사회적 책임성을 단순한 통계적 공정성이 아닌 인과적 불공정(causal unfairness)을 제거하는 관점에서 재정의

## Limitation & Further Study

### 한계점

1. **인과가정의 현실성 문제**: 
   - 실무에서 정확한 인과그래프를 수립하기 어렵고, 부정확한 인과가정은 오히려 편향을 증대시킬 수 있다
   - 성향점수 방법도 올바른 성향점수 형태를 미리 알아야 한다는 가정이 현실성 떨어짐

2. **계산 복잡도 및 확장성**:
   - 대규모 데이터에서 인과 발견 알고리즘의 계산 비용이 매우 높음
   - 고차원 데이터에서 인과관계 식별이 어려움

3. **도메인 지식 의존성**:
   - 반사실 데이터 증강(CDA)은 전문가 주석자의 개입이 필수적이며, 주석 과정에서 새로운 편향이 도입될 위험
   - 인과그래프 구성이 영역 전문 지식에 크게 의존

4. **윤리 및 실험적 제약**:
   - 인과효과를 검증하기 위한 무작위 대조 실험(RCT)이 윤리적·재정적 이유로 불가능한 경우 많음
   - 성향점수 기반 방법은 위치 랜덤화 시 사용자 경험이 심각하게 저하될 수 있음

### 후속 연구 방향

1. **약한 인과가정 조건 개발**: 도메인 지식이 제한적인 상황에서도 작동 가능한 경량 인과가정 프레임워크 개발

2. **인과-통계 하이브리드 방법론**: 인과구조를 완전히 알지 못할 때, 통계적 방법과 부분적 인과지식을 결합하는 방법론 강화

3. **적응형 인과 발견**: 데이터 수집 과정과 인과 발견을 동시에 수행하는 온라인 학습 알고리즘 개발

4. **설명 가능성과 공정성의 트레이드오프**: 투명한 반사실 설명과 모델 성능(utility) 간의 균형을 이루는 방법론

5. **크로스도메인 인과 전이**: 한 분야에서 학습한 인과구조를 다른 분야에 전이하는 메커니즘 연구

6. **동적 환경에서의 불변성**: 시간에 따라 인과구조가 변하는 환경(concept drift)에서의 불변성 보장 방법

## Evaluation

| 평가 항목 | 점수 | 설명 |
|---------|------|------|
| **Novelty (독창성)** | 4/5 | 기존에 산발적인 인과학습 방법들을 처음 통합 분류했으나, 개별 기법의 혁신성은 제한적 |
| **Technical Soundness (기술적 건전성)** | 4/5 | Pearl의 인과 계층구조 기반으로 이론

## Related Papers

- 🧪 응용 사례: [[papers/820_Toward_Reliable_Scientific_Hypothesis_Generation_Evaluating/review]] — 인과학습의 편향 완화 도구들이 과학 가설 생성에서 환각과 편향을 탐지하는 TruthHypo의 검증 메커니즘에 적용될 수 있다.
- 🔄 다른 접근: [[papers/286_Domain-specific_ReAct_for_physics-integrated_iterative_model/review]] — 사회적 책임 AI를 위한 인과학습과 물리학 통합 모델링이 모두 복잡한 인과관계를 다루지만 사회적 vs 물리적 시스템으로 구분된다.
- 🏛 기반 연구: [[papers/730_Sciqag_A_framework_for_auto-generated_science_question_answe/review]] — 인과학습 도구의 체계적 평가를 위해 SciQAG의 자동 질의응답 생성 방법론이 편향성과 공정성 관련 질문 생성에 활용될 수 있다.
- 🧪 응용 사례: [[papers/748_Semi-Supervised_2D_Human_Pose_Estimation_Driven_by_Position/review]] — 사회적 책임 AI의 편향 완화 방법론이 반지도학습 포즈 추정의 의사 레이블 노이즈 제거 기법과 연결되어 AI 시스템의 공정성을 향상시킬 수 있다.
- 🏛 기반 연구: [[papers/190_Causal_intervention_for_abstractive_related_work_generation/review]] — 사회적 책임감 있는 AI를 위한 인과 학습 연구로 관련 업무 생성에서 편향 제거의 이론적 기반을 제공한다.
- 🧪 응용 사례: [[papers/631_Predicting_field_experiments_with_large_language_models/review]] — 경제학 실험 예측 방법론을 사회적 책임 AI의 인과학습 도구 평가에 적용하여 편향성 완화 효과를 실증적으로 검증할 수 있다.
- 🔄 다른 접근: [[papers/673_Researchtown_Simulator_of_human_research_community/review]] — AI 연구 커뮤니티 시뮬레이션과 사회적 책임 AI를 위한 인과학습이 모두 AI 시스템의 사회적 영향을 다루지만 접근 방식이 상이하다.
- 🏛 기반 연구: [[papers/730_Sciqag_A_framework_for_auto-generated_science_question_answe/review]] — SciQAG의 자동 질의응답 생성 방법론이 사회적 책임 AI를 위한 인과학습 도구들의 효과를 평가하는 체계적인 질문 생성에 적용될 수 있다.
- 🧪 응용 사례: [[papers/748_Semi-Supervised_2D_Human_Pose_Estimation_Driven_by_Position/review]] — 반지도학습 포즈 추정의 편향 제거 기법이 사회적 책임 AI의 인과학습 도구에서 편향 완화 방법론으로 적용될 수 있다.
- 🧪 응용 사례: [[papers/820_Toward_Reliable_Scientific_Hypothesis_Generation_Evaluating/review]] — TruthHypo의 환각 탐지 프레임워크가 사회적 책임 AI의 인과학습에서 잘못된 인과관계 추론을 검출하는 도구로 활용될 수 있다.
- 🔄 다른 접근: [[papers/286_Domain-specific_ReAct_for_physics-integrated_iterative_model/review]] — 물리학 통합 모델링과 사회적 책임 AI 인과학습이 모두 복잡한 시스템의 인과관계를 다루지만 물리적 vs 사회적 도메인으로 구분된다.
- 🔗 후속 연구: [[papers/458_Language_agents_mirror_human_causal_reasoning_biases/review]] — 사회적 책임 AI를 위한 인과 학습을 언어 에이전트의 인지 편향 연구로 확장할 수 있다
- 🏛 기반 연구: [[papers/660_Reimagining_urban_science_Scaling_causal_inference_with_larg/review]] — 사회적 책임감 있는 AI를 위한 인과 학습이 도시 인과 추론 자동화의 이론적 기반을 제공합니다.
