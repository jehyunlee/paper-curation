---
title: "1049_Universality_of_citation_distributions_Toward_an_objective_m"
authors:
  - "Filippo Radicchi"
  - "Santo Fortunato"
  - "Claudio Castellano"
date: "2008"
doi: "10.1073/pnas.0806977105"
arxiv: ""
score: 4.0
essence: "다양한 학문분야의 논문 인용 분포가 상대지표 cf = c/c0로 정규화되면 보편적 곡선(universal curve)으로 수렴함을 보이며, 이를 기반으로 학문분야 간 과학적 영향력을 객관적으로 비교할 수 있는 방법을 제시한다."
tags:
  - "cat/Bibliometric_Network_Analysis"
  - "sub/Citation_Metrics_and_Indices"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Radicchi et al._2008_Universality of citation distributions Toward an objective measure of scientific impact.pdf"
---

# Universality of citation distributions: Toward an objective measure of scientific impact

> **저자**: Filippo Radicchi, Santo Fortunato, Claudio Castellano | **날짜**: 2008 | **DOI**: [10.1073/pnas.0806977105](https://doi.org/10.1073/pnas.0806977105)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2: Rescaled probability distribution c0P(c, c0) of the*

다양한 학문분야의 논문 인용 분포가 상대지표 cf = c/c0로 정규화되면 보편적 곡선(universal curve)으로 수렴함을 보이며, 이를 기반으로 학문분야 간 과학적 영향력을 객관적으로 비교할 수 있는 방법을 제시한다.

## Motivation

- **Known**: 인용 분석(citation analysis)은 학자와 기관의 학문적 성과를 평가하는 중요한 도구이지만, 수학의 IF(Impact Factor) 2.55 vs 의학 분야의 IF 50+ 등 학문분야 간 인용 관습의 차이로 인해 순수 인용 수의 비교는 편향되어 있다.
- **Gap**: 기존 정규화 방법들은 평균 인용 수만으로 정규화하지만, 인용 분포가 매우 왜곡(skewed)되어 있어 평균값만으로의 정규화가 적절한지 검증되지 않았다.
- **Why**: 객관적이고 공정한 인용 분석은 연구비 배분, 채용 심사, 기관 평가 등 중요한 학술적 결정에 영향을 미치므로, 학문분야 간 비교를 위한 신뢰할 수 있는 척도 개발이 필수적이다.
- **Approach**: 14개 학문분야, 20개 범주의 논문 데이터(1990, 1999, 2004년 발표)를 수집하여 상대지표 cf = c/c0의 분포를 분석하고, 로그정규분포(lognormal distribution)로 적합시켜 보편성을 입증한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2: Rescaled probability distribution c0P(c, c0) of the*

- **보편적 인용 분포 발견**: 14개 서로 다른 학문분야의 논문 인용 분포가 상대지표 cf로 정규화되면 σ² ≈ 1.3인 동일한 로그정규분포로 수렴
- **시간적 안정성**: 동일 분야에서 다른 연도(1990, 1999, 2004)에 발표된 논문들도 동일한 보편 곡선을 따르며, cf가 연도별 차이도 적절히 보정함
- **일반화된 h-지수**: 상대지표 cf를 기반으로 서로 다른 분야의 과학자들을 공정하게 비교할 수 있는 h-지수 확장 버전 제시
- **통계적 검증**: 모든 범주에서 χ²/df < 0.02로 로그정규분포 적합이 우수하며, σ² 값들이 3표준편차 이내에서 일치

## How

![Figure 1](figures/fig1.webp)

*Figure 1: Normalized histogram of the number of articles*

- Journal of Citation Reports의 학문분야 분류 시스템을 사용하여 학문분야 기준 정의
- 각 학문분야와 연도별로 발표된 모든 논문의 인용 수(c) 수집 및 평균 인용 수(c0) 계산
- 상대지표 cf = c/c0를 산출하여 모든 학문분야 데이터를 단일 축에서 정규화
- 정규화된 확률분포 c0P(c, c0)를 로그정규분포로 적합시키되, E[cf]=1 제약조건(σ²=-2μ)을 적용하여 모수 단순화
- 각 범주별 적합 파라미터(σ², χ²/df)를 비교하여 보편성 검증

## Originality

- 기존 정규화가 평균값만 사용한 반면, 전체 분포를 고려한 보편성 분석으로 개념 확장
- 정규화된 분포의 보편성(universality)을 물리학의 scaling law 개념으로 해석하여 새로운 관점 제시
- 선거 투표율 분석 등 타 분야와의 유사성 언급으로 광범위한 응용 가능성 제시
- 단순한 정규화 방법으로도 14개 분야를 모두 포함하는 강력한 보편 곡선 도출

## Limitation & Further Study

- 자기인용(self-citation), 암묵적 인용(implicit citation) 등 인용의 질적 차이는 여전히 미반영
- 저자 수와 인용 수의 상관관계, 시간에 따른 누적 인용의 영향을 개별적으로 분석하지 않음
- Journal of Citation Reports 분류의 한계(예: 학제적 논문의 분류 문제)를 고려하지 않음
- 후속연구: 더 세분화된 학문분야 또는 저널 단위로의 검증, 자기인용 제거 후 재분석, 개인 및 기관 수준의 h-지수 적용 검토

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 상대지표 cf의 보편성을 엄밀하게 입증한 연구로, 학문분야 간 공정한 성과 평가를 위한 강력한 이론적 기초를 제공하며, 간결하면서도 일반성이 높은 접근법이 실용적 가치가 뛰어나다.

## Related Papers

- 🧪 응용 사례: [[papers/966_Global_citation_inequality_is_on_the_rise/review]] — 보편적 인용 분포 모델을 전세계 인용 불평등 증가 현상의 정량적 분석에 적용한다.
- 🏛 기반 연구: [[papers/1009_Relative_Citation_Ratio_A_New_Metric_That_Uses_Citation_Rate/review]] — 학문분야 간 객관적 비교를 위한 상대적 인용 비율 계산의 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/987_Meta-assessment_of_Bias_in_Science/review]] — 보편적 인용 분포를 이용한 객관적 측정을 과학 전반의 편향성 메타 평가로 확장한다.
- 🧪 응용 사례: [[papers/1122_The_disruption_index_suffers_from_citation_inflation_Re-anal/review]] — 보편적 인용 분포 모델을 파괴성 지수의 인플레이션 문제 분석에 적용한다.
- 🏛 기반 연구: [[papers/1047_Theory_and_Practice_of_the_g-index/review]] — g-index와 같은 개별 지표를 넘어 학문분야별 인용 분포의 보편적 특성을 이해하는 기반을 제공한다.
- 🏛 기반 연구: [[papers/1003_Quantifying_Long-term_Scientific_Impact/review]] — 인용 분포의 보편성에 대한 이론적 기반을 제공하여 장기 영향력 예측 모델의 수학적 토대를 마련한다.
- 🏛 기반 연구: [[papers/1009_Relative_Citation_Ratio_A_New_Metric_That_Uses_Citation_Rate/review]] — 인용 분포의 보편성에 대한 이해가 상대인용비율 지표 개발의 이론적 기반을 제공한다.
- 🏛 기반 연구: [[papers/933_An_index_to_quantify_an_individuals_scientific_research_outp/review]] — h-index와 같은 개별 지표를 넘어 학문분야 간 객관적 비교를 위한 보편적 인용 분포 모델을 제공한다.
