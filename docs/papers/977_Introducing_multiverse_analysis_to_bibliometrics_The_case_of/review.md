---
title: "977_Introducing_multiverse_analysis_to_bibliometrics_The_case_of"
authors:
  - "Christian Leibel"
  - "Lutz Bornmann"
date: "2026.03"
doi: "10.1162/qss.a.475"
arxiv: ""
score: 4.0
essence: "본 연구는 다중우주분석(multiverse analysis)을 문헌계량학에 도입하여 팀 규모가 파괴적 연구에 미치는 영향에 대한 모델 불확실성을 체계적으로 평가한다. Wu et al. (2019)의 '소규모 팀이 더 파괴적 연구를 생산한다'는 주장의 견고성을 재검토한다."
tags:
  - "cat/Research_Quality_and_Demographics"
  - "sub/Collaboration_and_Team_Effects"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Leibel and Bornmann_2026_Introducing multiverse analysis to bibliometrics The case of team size effects on disruptive resear.pdf"
---

# Introducing multiverse analysis to bibliometrics: The case of team size effects on disruptive research

> **저자**: Christian Leibel, Lutz Bornmann | **날짜**: 2026-03-23 | **DOI**: [10.1162/qss.a.475](https://doi.org/10.1162/qss.a.475)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1 shows the range and the density of estimates from the multiverse of 180 equally*

본 연구는 다중우주분석(multiverse analysis)을 문헌계량학에 도입하여 팀 규모가 파괴적 연구에 미치는 영향에 대한 모델 불확실성을 체계적으로 평가한다. Wu et al. (2019)의 '소규모 팀이 더 파괴적 연구를 생산한다'는 주장의 견고성을 재검토한다.

## Motivation

- **Known**: Wu et al. (2019)은 소규모 팀이 대규모 팀보다 더 파괴적(disruptive) 연구를 생산한다고 주장했으나, Petersen et al. (2025)는 이를 반박했다. 연구자의 모델링 결정이 분석 결과에 상당한 영향을 미친다는 점이 문헌에서 잘 알려져 있다.
- **Gap**: 문헌계량학에서 모델 불확실성(model uncertainty)을 체계적으로 측정하고 보고하는 관행이 부족하며, 기존 견고성 검증(robustness check)은 제한된 모델 부분집합만 고려한다. 상충되는 연구 결과들을 종합적으로 평가할 메커니즘이 부재하다.
- **Why**: 과학 정책 입안자들이 파괴적 연구 촉진을 위해 소규모 또는 대규모 팀을 육성해야 하는지 판단해야 하는데, 현재의 불확실한 증거로는 신뢰할 수 있는 정책 결정이 어렵다. 문헌계량학 결과의 신뢰성과 투명성을 높이려면 모델 불확실성에 대한 체계적 평가가 필수적이다.
- **Approach**: 다중우주분석을 문헌계량학에 도입하여, 데이터 선택, 지표 구성, 모델링 결정 등의 모든 합리적 조합을 고려한 K개의 동등하게 타당한 모델(M₁, …, Mₖ)을 구성한다. 모든 모델 추정치의 분산을 계산하여 모델 표준편차(√Vₘ)와 영향통계량(influence statistics)을 도출한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1 shows the range and the density of estimates from the multiverse of 180 equally*

- **다중우주분석의 문헌계량학 도입**: 상태 최고 수준의 통계 방법론을 문헌계량학에 처음 체계적으로 적용하여, 모델 불확실성 측정의 새로운 표준 제시
- **팀 규모 효과의 견고성 검증**: 180개의 모델 사양에 대한 포괄적 분석을 통해 팀 규모의 음(negative) 효과는 견고하나, 효과 크기(effect size)는 모델 명세에 따라 상당히 변함을 발견
- **모델 영향 요인 규명**: 어떤 모델링 결정이 연구 결과에 가장 큰 영향을 미치는지 투명하게 식별 가능하게 함
- **정책적 함의의 명확화**: 문헌계량학 결과의 실제 정책적 의미를 더 정확하게 해석할 수 있는 토대 제공

## How

![Figure 1](figures/fig1.webp)

*Figure 1 shows the range and the density of estimates from the multiverse of 180 equally*

- Wu et al. (2019)과 Petersen et al. (2025)의 모델링 가정 비교 분석
- 데이터 선택 기준(예: 시간 범위, 필드 선택)의 모든 합리적 조합 도출
- 종속변수 조작화(disruption index 정의), 통제변수 선택, 추정 절차의 다양한 사양 구성
- 각 모델 사양에서 팀 규모 계수(β) 추정
- 식 (1)을 이용한 모델 분산 Vₘ = (1/K)Σ(bₖ - b̄)² 계산
- 개별 모델링 결정의 한계 효과(marginal effect) 계산을 통한 영향통계량(Δβ) 도출
- 추정치의 분포 시각화 및 견고성 패턴 분석

## Originality

- 문헌계량학 분야에서 다중우주분석을 최초로 도입한 개척적 연구
- 표준 견고성 검증을 넘어 '모든 합리적 모델'을 포괄하는 포괄적 접근법 제시", '모델 영향통계량을 이용하여 임의적 모델 선택의 영향을 정량화하고 투명화
- Wu-Petersen 논쟁을 해결하는 새로운 프레임워크 제시로 실질적 과학 정책 기여

## Limitation & Further Study

- 모델 공간 정의의 주관성: 어떤 모델 사양이 '동등하게 타당한지' 결정하는 기준이 여전히 연구자 판단에 의존", '계산 복잡성: 모델 조합이 기하급수적으로 증가하면 실행 가능성 제약 가능
- 인과 추론의 한계: 다중우주분석도 관찰 데이터의 인과성 문제를 완전히 해결하지 못함
- 후속 연구: (1) 모델 공간 정의에 대한 이론적 가이드라인 개발, (2) 다양한 문헌계량학 주제(저자 인정도, 학제간 영향 등)에 대한 다중우주분석 적용, (3) 베이지안 모델 평균(Bayesian Model Averaging) 등 대안 방법론과의 비교

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 모델 불확실성이라는 실질적 문제를 문헌계량학에 처음 체계적으로 다루며, 다중우주분석이라는 강력한 방법론을 도입하여 연구 신뢰성과 투명성을 획기적으로 향상시킨다. Wu-Petersen 논쟁을 통해 실제 적용 사례를 제시함으로써 문헌계량학 연구의 표준 관행 개선에 중대한 기여를 한다.

## Related Papers

- 🏛 기반 연구: [[papers/979_Large_teams_develop_and_small_teams_disrupt_science_and_tech/review]] — 다중우주분석을 통해 팀 규모-혁신성 관계의 견고성을 검증하고 원 연구의 한계 보완
- 🔗 후속 연구: [[papers/1122_The_disruption_index_suffers_from_citation_inflation_Re-anal/review]] — 팀 규모 연구에서 사용된 파괴성 지수의 인용 인플레이션 문제를 다중우주분석으로 재평가 필요
- 🔄 다른 접근: [[papers/1080_Robust_Evidence_for_Declining_Disruptiveness_Assessing_the_R/review]] — 파괴성 감소 현상에 대한 견고한 증거와 팀 규모 효과의 불확실성이라는 대조적 관점 제시
- ⚖️ 반론/비판: [[papers/979_Large_teams_develop_and_small_teams_disrupt_science_and_tech/review]] — 팀 규모-파괴성 관계의 견고성에 대한 의문을 다중우주분석을 통해 체계적으로 검증받음
