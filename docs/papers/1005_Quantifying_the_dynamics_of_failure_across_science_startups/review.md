---
title: "1005_Quantifying_the_dynamics_of_failure_across_science_startups"
authors:
  - "Yian Yin"
  - "Yang Wang"
  - "James A. Evans"
  - "Dashun Wang"
date: "2019"
doi: "10.1038/s41586-019-1725-y"
arxiv: ""
score: 4.0
essence: "과학, 스타트업, 보안 등 다양한 분야에서 반복된 실패의 역학을 설명하는 일-매개변수 모델을 개발하여, 실패 후 성공으로 이어지는 동역학의 위상 전이를 발견했다."
tags:
  - "cat/Research_Quality_and_Demographics"
  - "sub/Research_Evaluation_and_Metrics"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yin et al._2019_Quantifying the dynamics of failure across science, startups and security.pdf"
---

# Quantifying the dynamics of failure across science, startups and security

> **저자**: Yian Yin, Yang Wang, James A. Evans, Dashun Wang | **날짜**: 2019 | **DOI**: [10.1038/s41586-019-1725-y](https://doi.org/10.1038/s41586-019-1725-y)

---

## Essence

![Figure 3](figures/fig3.webp)

*Figure 3: Phase diagram of the model. (a) Analytical solution of the model reveals that the*

과학, 스타트업, 보안 등 다양한 분야에서 반복된 실패의 역학을 설명하는 일-매개변수 모델을 개발하여, 실패 후 성공으로 이어지는 동역학의 위상 전이를 발견했다.

## Motivation

- **Known**: 혁신과 학습 문헌에서 실패 이후의 성공이 운(chance)과 학습(learning) 메커니즘으로 설명되어 왔으나, 두 메커니즘만으로는 현실의 복잡한 실패 패턴을 완전히 설명하지 못한다.
- **Gap**: 실패의 동역학을 정량적으로 이해하고 초기 신호를 통해 최종 성공 또는 실패를 예측할 수 있는 통합 이론 모델이 부재했다.
- **Why**: 반복된 실패는 인간의 성취에 보편적이지만, 어떤 실패 동역학이 결국 성공을 낳고 어떤 것이 정체로 이어지는지 이해하는 것은 정책 수립과 개인의 의사결정에 중요하다.
- **Approach**: NIH 연구비 신청, 스타트업 투자, 테러 공격 등 3개 대규모 데이터셋에서 개인의 반복 시도 이력을 추적하고, 과거 경험을 얼마나 활용하는지를 나타내는 매개변수 k를 가진 수학 모델을 제시하여 해석적으로 풀었다.

## Achievement

![Figure 4](figures/fig4.webp)

*Figure 4: Testing model predictions. (a-c) Complementary cumulative distribution (CCDF) of*

- **위상 전이 발견**: 매개변수 k에 대해 불연속적인 위상 전이가 존재하며, 임계값 k*을 기준으로 정체(stagnation) 영역과 진전(progression) 영역이 구분됨을 증명했다.
- **보편적 동역학 법칙**: 진전 영역에서 시간 복잡도와 품질 개선이 멱법칙(power law)을 따르며, 이는 Wright's Law와 일치함을 보였다.", '**조기 신호 식별**: 성공과 실패를 경험한 개인들이 초기에는 유사하지만, 후속 시도의 효율성(efficiency)과 품질(quality)의 동역학에서 근본적으로 다른 패턴을 보임을 발견했다.
- **3개 도메인에서 검증**: NIH, 스타트업, 테러 조직 데이터에서 모델 예측이 일관되게 지지됨을 확인했다 (p < 0.05).

## How

![Figure 2](figures/fig2.webp)

*Figure 2: The k model. (a) Here we treat each attempt as a combination of independent compo-*

- NIH R01 신청 776,721건, 스타트업 58,111개, 테러 공격 170,350건의 장기 데이터 수집 및 정제
- 각 시도를 독립적 컴포넌트의 조합으로 모델링하고, 새 버전 생성 확률을 p=(1-x*)^α로 설정
- 매개변수 k(고려할 과거 시도 수)에 대해 모델을 해석적으로 풀고 점근 거동 도출
- 경험적 데이터에서 품질, 효율성, 실패 연속 길이 분포 측정 및 모델 예측과 비교
- 위상 전이를 정준 앙상블(canonical ensemble)의 에너지 준위와 매핑하여 물리적 해석 제시

## Originality

- 기존 학습/운 이분법을 넘어 하이브리드 모델로 통합한 첫 시도
- 개인 반복 시도의 미시적 동역학(component-level)에서 거시적 성공 궤적까지 연결한 다층 분석
- 서로 다른 3개 도메인(학문, 경제, 보안)에서 동일한 수학 구조를 발견한 것은 보편성의 증거
- 위상 전이를 물리학의 정준 앙상블 개념과 연결하여 학제적 관점 제시

## Limitation & Further Study

- 모델이 컴포넌트 독립성을 가정하지만 실제 NIH 제안서나 스타트업 사업계획서는 컴포넌트 간 강한 상호작용이 존재할 수 있다.
- α 매개변수의 도메인 간 차이에 대한 이론적 설명 부족; 각 도메인에서 α 값이 어떻게 결정되는지 메커니즘 미명확
- 스타트업 성공 정의가 5년 내 IPO/M&A로 제한되어 장기 생존성이나 사회적 영향은 미반영
- 테러 공격 성공을 사상자 수로만 정의하여 조직의 장기 목표 달성(정치적 영향)과의 괴리 존재
- 후속 연구: 컴포넌트 의존성을 포함한 확장 모델, 도메인별 α 값의 심층 분석, 동적 임계값 k*의 개인 특성에 따른 변이 연구

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 실패의 동역학을 최초로 수학적으로 정량화하고 위상 전이를 통해 설명한 획기적 연구이며, 3개 대규모 이질적 데이터셋에서 보편성을 입증함으로써 학제적 영향력이 크다.

## Related Papers

- 🔗 후속 연구: [[papers/971_Hot_streaks_in_artistic_cultural_and_scientific_careers/review]] — 실패 후 성공의 동역학과 hot streak 현상을 연결하여 경력 패턴의 위상 전이를 더 깊이 이해할 수 있다.
- 🧪 응용 사례: [[papers/956_Early_career_setback_and_future_achievement_in_professional/review]] — 초기 경력 좌절이라는 구체적 사례에 실패 동역학 모델을 적용하여 예측력을 검증할 수 있다.
- 🏛 기반 연구: [[papers/998_Predicting_Scientific_Breakthroughs_Based_on_Structural_Dyna/review]] — 구조적 역학 기반의 돌파구 예측 방법론이 실패-성공 전이 모델의 이론적 기반을 제공한다.
- 🏛 기반 연구: [[papers/956_Early_career_setback_and_future_achievement_in_professional/review]] — 과학자 경력에서 실패의 역설적 효과를 이해하기 위해 실패 동학의 일반 이론이 필요함
