---
title: "934_Are_disruptive_papers_more_likely_to_impact_technology_and_s"
authors:
  - "Alex J. Yang"
  - "Xiaohui Yan"
  - "Haotian Hu"
  - "Hanlin Hu"
  - "Jia Kong"
date: "2025.03"
doi: "10.1002/asi.24947"
arxiv: ""
score: 4.0
essence: "거의 4천만 개의 논문을 분석하여 높은 CD index(파괴적 지수)를 가진 논문이 역설적으로 기술·사회 영향력이 낮다는 것을 발견했으며, 대신 '파괴적 인용(disruptive citation)' 지표가 더 강한 예측력을 가짐을 밝혔다."
tags:
  - "cat/Bibliometric_Network_Analysis"
  - "sub/Citation_Metrics_and_Indices"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yang et al._2025_Are disruptive papers more likely to impact technology and society.pdf"
---

# Are disruptive papers more likely to impact technology and society?

> **저자**: Alex J. Yang, Xiaohui Yan, Haotian Hu, Hanlin Hu, Jia Kong, Sanhong Deng | **날짜**: 03/2025 | **DOI**: [10.1002/asi.24947](https://doi.org/10.1002/asi.24947)

---

## Essence


거의 4천만 개의 논문을 분석하여 높은 CD index(파괴적 지수)를 가진 논문이 역설적으로 기술·사회 영향력이 낮다는 것을 발견했으며, 대신 '파괴적 인용(disruptive citation)' 지표가 더 강한 예측력을 가짐을 밝혔다.

## Motivation

- **Known**: CD index는 인용 네트워크의 구조적 특성을 분석하여 과학 논문의 파괴적 성격을 정량화하는 지표이다. 과학은 이론상 공공재이지만 정책입안자와 과학자 간의 상호작용 부족으로 실제 활용이 제한되어 왔다.
- **Gap**: CD index의 높은 값이 반드시 높은 인용도와 관련이 없다는 것은 알려져 있으나, 이러한 편향이 기술·사회 영향력 영역에까지 확장되는지는 체계적으로 검증되지 않았다. 상대적 파괴성과 절대적 파괴 영향의 구분이 명확하지 않았다.
- **Why**: 과학의 실질적 사회 영향력을 평가하는 메커니즘 이해는 정책입안자와 연구자가 임팩트 있는 과학 연구를 육성하는 데 필수적이다. 파괴적 혁신과 사회적 유용성 간의 역설적 관계는 과학 평가 체계를 재검토하게 한다.
- **Approach**: Microsoft Academic Graph(MAG) 데이터셋의 1950-2020년 논문 약 4천만 개를 분석하고, 특허 인용, 임상시험, 뉴스 매체, 소셜미디어 등 4가지 기술·사회 연결 지표와 연관시켰다. 새로운 '파괴적 인용' 메트릭을 제안하여 CD index와 비교 분석했다.

## Achievement


- **CD index의 역설적 효과**: 높은 CD index를 가진 논문이 기술·사회 영향력과 부(-)의 상관관계를 보임을 발견
- **파괴적 인용의 긍정적 영향**: 절대적 파괴 영향을 측정하는 '파괴적 인용' 지표는 기술·사회 영향력과 강한 양(+)의 상관관계 확인", '**시간·분야별 편향 분석**: CD index에 대한 편향이 최근 20년과 STEM 분야에서 두드러지나, 파괴적 인용의 긍정 효과는 모든 시기와 분야에서 일관됨
- **강건성 검증**: 대안적 파괴성 측정 지표와 총 인용 수 통제 시에도 결과의 견고성 확인

## How


- Microsoft Academic Graph(MAG) 데이터셋에서 1950-2020년 약 4천만 개 논문 수집
- CD index(Funk & Owen-Smith 2017)를 활용한 상대적 파괴성 측정
- 새로운 'disruptive citation' 메트릭 개발으로 절대적 파괴 영향 측정", '4가지 기술·사회 영역 변수 구성: 특허 인용(patent citations), 임상시험 언급(clinical trials), 뉴스 미디어(news outlets), 소셜미디어(social media)
- 이항 로지스틱 회귀(binary logistic regression) 분석으로 파괴성과 기술·사회 영향력의 연관성 검증
- 연도별, 분야별(STEM vs. 비STEM) 이질성 분석 수행
- 대안적 파괴성 측정 지표와 통제변수 추가로 견고성 검증

## Originality

- 상대적 파괴성(CD index)과 절대적 파괴 영향의 개념적 구분을 명확히 하고 이를 실증적으로 검증한 최초의 연구
- disruptive citation' 이라는 새로운 메트릭 제안으로 기존 CD index의 한계 보완", '대규모 데이터셋(약 4천만 개 논문)과 다양한 기술·사회 영향 지표를 통합하여 과학 임팩트의 다차원적 분석 제시
- CD index의 편향이 시간과 분야에 따라 다르게 나타나는 패턴을 최초로 체계적으로 분석

## Limitation & Further Study

- Microsoft Academic Graph 데이터의 완전성 및 정확성 문제(특히 구 데이터의 누락 가능성)
- 기술·사회 영향 측정이 영어권 문헌과 디지털화된 정보에 편향되어 있을 가능성
- 특허 인용, 뉴스 언급 등이 반드시 의도적인 활용을 의미하지 않을 수 있음
- 인과관계가 아닌 상관관계만 입증되었으므로 파괴성이 직접적으로 영향력을 제약하는 메커니즘 규명 필요
- 후속 연구로 논문의 의미론적 내용 분석, 학문분야별 세분화, 시간 지연 효과(lag effect) 검증 권장

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 파괴적 과학과 사회 영향력 간의 역설적 관계를 대규모 데이터로 최초 입증하고, 새로운 측정 지표를 제안하여 과학 평가 체계에 중요한 시사점을 제공한 우수한 논문이다. 다만 인과관계 규명과 문화적 편향 완화를 위한 후속 연구가 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/1122_The_disruption_index_suffers_from_citation_inflation_Re-anal/review]] — 파괴성 지수와 기술/사회 영향력 관계 분석을 인용 인플레이션으로 인한 파괴성 지수의 근본적 한계 재분석으로 확장한다.
- ⚖️ 반론/비판: [[papers/1080_Robust_Evidence_for_Declining_Disruptiveness_Assessing_the_R/review]] — 파괴성과 영향력의 역설적 관계에 대해 파괴성 감소 현상의 견고한 증거를 제시한다.
- 🔄 다른 접근: [[papers/951_Defining_and_identifying_Sleeping_Beauties_in_science/review]] — 즉각적 파괴성 대신 장기간 잠들어 있다가 재발견되는 논문의 특성을 분석한다.
- 🔗 후속 연구: [[papers/954_Do_novel_papers_attract_more_social_attention/review]] — 파괴성과 기술 영향력의 관계를 논문의 새로움과 소셜 미디어 관심도의 관계로 확장한다.
- 🧪 응용 사례: [[papers/1080_Robust_Evidence_for_Declining_Disruptiveness_Assessing_the_R/review]] — 혁신적 논문이 기술과 사회에 미치는 영향을 혁신성 하락 추세와 연결하여 과학의 사회적 기여 변화를 평가할 수 있다.
- 🔗 후속 연구: [[papers/979_Large_teams_develop_and_small_teams_disrupt_science_and_tech/review]] — 파괴적 논문의 기술-사회 영향력을 팀 규모별로 분석하여 혁신의 다층적 효과 이해 가능
- 🔗 후속 연구: [[papers/1004_Quantifying_spatialtemporal_citation_diffusion_of_individual/review]] — 인용 확산 패턴과 파괴적 지수 간의 관계를 통해 논문의 장기적 기술/사회 영향력을 예측한다.
- 🔗 후속 연구: [[papers/927_A_Dynamic_Network_Measure_of_Technological_Change/review]] — 파괴적 논문이 기술과 사회에 미치는 영향을 CDt 지수를 통해 더 정교하게 측정할 수 있는 방법론을 제시한다.
