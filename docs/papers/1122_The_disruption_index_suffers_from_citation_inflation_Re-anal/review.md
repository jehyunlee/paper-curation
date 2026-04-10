---
title: "1122_The_disruption_index_suffers_from_citation_inflation_Re-anal"
authors:
  - "Alexander Michael Petersen"
  - "Felber J. Arroyave"
  - "Fabio Pammolli"
date: "2025.02"
doi: "10.1016/j.joi.2024.101605"
arxiv: ""
score: 4.0
essence: "인용 지수(CD)는 참고문헌 길이의 증가로 인한 인용 인플레이션(Citation Inflation)으로 인해 체계적으로 감소하며, 이는 혁신의 실제 감소가 아닌 측정 편향을 반영한다."
tags:
  - "cat/Scientific_Impact_and_Innovation"
  - "cat/Science_of_Science_Research"
  - "sub/Citation_metrics_and_impact_measurement"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Petersen et al._2025_The disruption index suffers from citation inflation Re-analysis of temporal CD trend and relations.pdf"
---

# The disruption index suffers from citation inflation: Re-analysis of temporal CD trend and relationship with team size reveal discrepancies

> **저자**: Alexander Michael Petersen, Felber J. Arroyave, Fabio Pammolli | **날짜**: 02/2025 | **DOI**: [10.1016/j.joi.2024.101605](https://doi.org/10.1016/j.joi.2024.101605)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1. Citation inﬂation is an inextricable feature of citation networks. The disruption index 𝐶𝐷𝑝is calculated accordi*

인용 지수(CD)는 참고문헌 길이의 증가로 인한 인용 인플레이션(Citation Inflation)으로 인해 체계적으로 감소하며, 이는 혁신의 실제 감소가 아닌 측정 편향을 반영한다.

## Motivation

- **Known**: disruption index (CD)는 학술 출판 및 특허 인용 네트워크에서 혁신 속도를 측정하기 위해 개발되었으며, Park et al. (2023)은 CD가 시간에 따라 감소한다고 보고했다.
- **Gap**: CD의 장기적 감소 추세가 실제 혁신 감소를 의미하는지, 아니면 측정 편향을 반영하는지에 대한 명확한 구분이 부재하였고, 참고문헌 길이 증가의 인과적 영향을 직접 검증한 연구가 없었다.
- **Why**: 혁신 측정의 정확성은 과학 정책 수립 및 기관 관리에 근본적으로 중요하며, CD의 편향을 파악하지 못하면 잘못된 정책 결정으로 이어질 수 있다.
- **Approach**: 수학적 추론, 계산 시뮬레이션, PNAS/PNAS Plus 준실험적 비교(참고문헌 길이 차이 제외 동일), 대규모 다변량 회귀 분석(780만 개 논문, 1995-2015)을 통해 citation inflation 가설을 검증한다.

## Achievement

![Figure 4](figures/fig4.webp)

*Fig. 4. Quasi-experimental test and validation of the CI hypothesis: counterfactual juxtaposition of research articles p*

- **Citation Inflation의 인과관계 입증**: 참고문헌 길이 증가가 CD를 체계적으로 감소시키는 구조적 메커니즘임을 수학적 및 실험적으로 증명
- **행동적 메커니즘 식별**: 자기인용 관행 등 기술-사회적 요인으로 인한 행동적 변화가 CD 감소의 또 다른 원인임을 규명
- **재분석을 통한 추세 수정**: CD가 2005-2015년 기간에 증가했으며, 시간 기반 감소 추세는 데이터 품질 문제로 인한 것임을 실증
- **팀 규모 관계의 재평가**: CD와 팀 규모의 부정적 관계는 전체 크기 효과가 매우 작으며, 8명 이상의 공동저자 시 양의 관계로 전환됨을 발견

## How

![Figure 3](figures/fig3.webp)

*Fig. 3. Computational simulation of growing citation networks: after ‘turning oﬀ’ CI, the systematic decline in 𝐶𝐷revers*

- 수학적 연역: CD 정의와 참고문헌 집합의 관계로부터 citation inflation의 인과적 영향 도출
- 계산 시뮬레이션: 성장하는 인용 네트워크에서 참고문헌 길이 증가의 영향을 모델링
- 준실험 설계: PNAS(표준 형식)와 PNAS Plus(온라인 장문)의 참고문헌 길이 차이를 이용한 자연실험
- 다변량 회귀분석: 참고문헌 길이, 자기인용율, 시간 변수 등을 통제변수로 포함한 대규모 분석
- SciSciNet 데이터베이스 분석: 실제 인용 네트워크 데이터에 기반한 검증

## Originality

- Citation inflation을 측정 편향의 구조적 원인으로 명시적으로 규명한 첫 체계적 연구
- 준실험적 방법론(PNAS vs PNAS Plus)을 통해 참고문헌 길이의 인과적 효과를 자연실험으로 검증
- 행동적 메커니즘(자기인용 관행)과 구조적 메커니즘(citation inflation)을 구분하여 분석한 이중 프레임워크
- 선행연구의 통계적 편향(omitted variable bias)을 구체적으로 지적하고 방법론적 개선안 제시

## Limitation & Further Study

- PNAS Plus 준실험은 2011-2015년 5년간의 특정 저널 데이터로 제한되어 다른 학문 분야나 시기에 대한 일반화에 주의 필요
- Behavioral mechanism의 양적 정량화가 제한적이며, 자기인용 관행의 변화 원인에 대한 심층 분석 부재
- 장기적 시간대(1995-2015년)에서 인용 관행의 급격한 변화가 있었는지 여부에 대한 상세한 추적 분석 부족
- 후속연구는 다른 학문 분야(life sciences, engineering 등)에 대한 재검증과 citation inflation 조정 방법론 개발 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 광범위한 실증 분석과 엄밀한 방법론을 통해 CD 측정의 근본적 편향을 규명하고, 선행연구의 '혁신 감소' 해석이 통계적 오류임을 명확히 입증했다. 과학 정책 수립의 기초가 되는 혁신 측정의 신뢰성을 크게 향상시키는 중요한 기여이다.

## Related Papers

- 🔗 후속 연구: [[papers/995_Papers_and_patents_are_becoming_less_disruptive_over_time/review]] — 파괴성 지수의 전반적 감소 현상이 인용 인플레이션이라는 측정 편향에서 기인할 수 있음을 규명하여 기존 연구를 보완한다.
- ⚖️ 반론/비판: [[papers/1080_Robust_Evidence_for_Declining_Disruptiveness_Assessing_the_R/review]] — 파괴성 감소에 대한 강력한 증거를 제시하는 연구와 측정 편향을 지적하는 연구 간의 대립적 관점을 보여준다.
- 🔗 후속 연구: [[papers/1080_Robust_Evidence_for_Declining_Disruptiveness_Assessing_the_R/review]] — 혁신성 지수의 인용 인플레이션 문제와 영인용 논문 효과를 함께 고려하여 혁신성 측정의 정확성을 높일 수 있다.
- 🧪 응용 사례: [[papers/1049_Universality_of_citation_distributions_Toward_an_objective_m/review]] — 보편적 인용 분포 모델을 파괴성 지수의 인플레이션 문제 분석에 적용한다.
- ⚖️ 반론/비판: [[papers/1009_Relative_Citation_Ratio_A_New_Metric_That_Uses_Citation_Rate/review]] — 인용 기반 지표들이 공통적으로 겪는 인용 인플레이션 문제를 보여주며 RCR 지표의 한계를 지적한다.
- 🔗 후속 연구: [[papers/977_Introducing_multiverse_analysis_to_bibliometrics_The_case_of/review]] — 팀 규모 연구에서 사용된 파괴성 지수의 인용 인플레이션 문제를 다중우주분석으로 재평가 필요
- ⚖️ 반론/비판: [[papers/995_Papers_and_patents_are_becoming_less_disruptive_over_time/review]] — 혁신성 지수가 인용 인플레이션으로 인해 문제가 있다고 지적하여 혁신성 감소 결론에 이의를 제기한다
- 🔗 후속 연구: [[papers/934_Are_disruptive_papers_more_likely_to_impact_technology_and_s/review]] — 파괴성 지수와 기술/사회 영향력 관계 분석을 인용 인플레이션으로 인한 파괴성 지수의 근본적 한계 재분석으로 확장한다.
