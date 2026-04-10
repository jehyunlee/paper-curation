---
title: "995_Papers_and_patents_are_becoming_less_disruptive_over_time"
authors:
  - "Michael Park"
  - "Erin Leahey"
  - "Russell J. Funk"
date: "2023"
doi: "10.1038/s41586-022-05543-x"
arxiv: ""
score: 4.0
essence: "45백만 논문과 390만 특허 데이터를 분석하여 과학과 기술의 혁신성(disruptiveness)이 시간이 지남에 따라 지속적으로 감소하고 있음을 규명했다. 이러한 감소 추세는 연구자들이 과거 지식의 범위를 좁혀서 활용하는 경향과 연관되어 있다."
tags:
  - "cat/Science_of_Science_Research"
  - "sub/Research_Evaluation_and_Impact"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Park et al._2023_Papers and patents are becoming less disruptive over time.pdf"
---

# Papers and patents are becoming less disruptive over time

> **저자**: Michael Park, Erin Leahey, Russell J. Funk | **날짜**: 2023 | **DOI**: [10.1038/s41586-022-05543-x](https://doi.org/10.1038/s41586-022-05543-x)

---

## Essence

![Figure 2](figures/fig2.webp)

*Fig. 2: Decline of disruptive science and technology.*

45백만 논문과 390만 특허 데이터를 분석하여 과학과 기술의 혁신성(disruptiveness)이 시간이 지남에 따라 지속적으로 감소하고 있음을 규명했다. 이러한 감소 추세는 연구자들이 과거 지식의 범위를 좁혀서 활용하는 경향과 연관되어 있다.

## Motivation

- **Known**: 과학과 기술의 진전은 이전 누적된 지식을 기반으로 하는 내생적 과정이며, 최근 수십 년간 새로운 과학적, 기술적 지식의 양이 지수적으로 증가했다. 그럼에도 불구하고 여러 주요 분야에서 진전 속도가 감소하고 있다는 연구 결과들이 보고되고 있다.
- **Gap**: 대규모 데이터와 표준화된 정량적 지표를 사용하여 과학과 기술 전반에서 혁신성의 감소 현상을 체계적으로 검증한 연구가 부재했다. 또한 이러한 감소의 근본 원인이 무엇인지 규명하지 못했다.
- **Why**: 과학과 기술 발전의 기초를 이루는 혁신성의 감소 추세를 이해하는 것은 향후 과학 정책 수립과 혁신 촉진 전략 수립에 필수적이다. 이는 사회 전반의 기술 발전과 경제 성장에 직접적인 영향을 미친다.
- **Approach**: CD index(Citation Disruption index)라는 새로운 정량적 지표를 개발하여 논문과 특허가 인용 네트워크에서 얼마나 기존의 흐름을 전환하는지 측정했다. 6개의 대규모 데이터셋을 활용하여 60년간의 추세를 분석했다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2: Decline of disruptive science and technology.*

- **혁신성 감소의 규명**: 모든 학문 분야에서 논문과 특허의 혁신성이 지속적으로 감소하는 보편적 패턴을 발견했다.
- **견고한 검증**: 인용 기반 및 텍스트 기반의 여러 지표를 사용하여 이 패턴이 강건하고 일관되게 나타남을 입증했다.
- **근본 원인 규명**: 혁신성 감소가 연구자들의 좁아진 지식 활용 범위와 연관되어 있음을 발견했다.
- **질 변화 배제**: 발표된 과학의 질 변화, 인용 관행, 분야별 특수 요인이 주요 원인이 아님을 입증했다.

## How

![Figure 1](figures/fig1.webp)

*Fig. 1: Overview of the measurement approach.*

- 45백만 논문(6개 데이터셋 포함: American Physical Society, JSTOR, Microsoft Academic Graph, PubMed, WoS)과 390만 특허(PatentsView) 데이터 수집
- CD index를 적용하여 각 논문/특허가 인용 네트워크에서 기존 조합을 파괴하는 정도를 측정
- 시간 경과에 따른 CD index 추세 분석으로 혁신성의 변화 추적
- 텍스트 분석을 통해 논문과 특허의 언어 변화 확인
- 고품질 과학(Nobel laureate 등)의 CD index 추적으로 선택성 검증
- 이전 지식의 범위 측정(backward citation diversity)으로 좁아지는 지식 활용 패턴 확인
- 통계적 회귀분석(Stata, Python 사용)으로 인과관계 검증

## Originality

- 대규모 데이터(45백만 논문, 390만 특허)를 이용한 전체 과학과 기술 분야에 걸친 체계적 분석
- 새로운 정량적 지표 CD index 개발로 혁신성을 객관적으로 측정할 수 있는 방법론 제시
- 인용 기반 및 텍스트 기반 다중 지표를 병행하여 검증 견고성 강화
- 혁신성 감소와 좁아지는 지식 활용 범위 간의 직접적 연관성 규명

## Limitation & Further Study

- 인용 데이터의 시간 지연(publication lag)으로 인한 최근 기간 분석의 한계
- 출판 관행 및 인용 문화의 변화가 측정에 미치는 영향을 완전히 통제하기 어려움
- 데이터셋별 특성 차이(학문 분야, 시간 범위 등)가 결과에 미치는 영향 추가 분석 필요
- 혁신성 감소 원인에 대한 더 깊은 메커니즘 분석(예: 자금 구조, 팀 구성, 인센티브 구조의 역할)
- 좁아진 지식 활용이 필연적인지, 선택적인지 구분하는 추가 연구 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 연구는 과학과 기술의 혁신성 감소를 대규모 데이터와 새로운 정량적 지표를 통해 체계적으로 입증한 우수한 연구이다. 이는 과학 정책 수립과 향후 혁신 촉진 전략에 중요한 함의를 제공한다.

## Related Papers

- ⚖️ 반론/비판: [[papers/1122_The_disruption_index_suffers_from_citation_inflation_Re-anal/review]] — 혁신성 지수가 인용 인플레이션으로 인해 문제가 있다고 지적하여 혁신성 감소 결론에 이의를 제기한다
- 🏛 기반 연구: [[papers/979_Large_teams_develop_and_small_teams_disrupt_science_and_tech/review]] — 대규모 팀과 소규모 팀의 서로 다른 역할이 혁신성 변화의 기초적 메커니즘을 설명한다
- 🔄 다른 접근: [[papers/936_Atypical_Combinations_and_Scientific_Impact/review]] — 비전형적 조합이 과학적 영향력을 높인다는 상반된 관점을 제시한다
- 🏛 기반 연구: [[papers/1080_Robust_Evidence_for_Declining_Disruptiveness_Assessing_the_R/review]] — 과학과 특허의 혁신성 하락을 뒷받침하는 강건한 증거로서 영인용 논문 제외 후에도 하락 추세가 지속됨을 확인한다.
- ⚖️ 반론/비판: [[papers/968_Growth_Rates_of_Modern_Science_Bibliometric_Analysis_Based_o/review]] — 과학의 지속적 성장 패턴과 최근 과학의 파괴적 혁신 감소 현상이 상반된 관점을 제시한다.
- 🏛 기반 연구: [[papers/979_Large_teams_develop_and_small_teams_disrupt_science_and_tech/review]] — 논문과 특허의 파괴성 감소 현상을 팀 규모 변화와 연결하여 과학 발전의 구조적 변화 설명
- 🔗 후속 연구: [[papers/1122_The_disruption_index_suffers_from_citation_inflation_Re-anal/review]] — 파괴성 지수의 전반적 감소 현상이 인용 인플레이션이라는 측정 편향에서 기인할 수 있음을 규명하여 기존 연구를 보완한다.
- 🏛 기반 연구: [[papers/927_A_Dynamic_Network_Measure_of_Technological_Change/review]] — 기술 변화의 동적 네트워크 측정이 과학과 기술에서 파괴성 감소 현상을 이해하는 방법론적 기반을 제공한다.
