---
title: "979_Large_teams_develop_and_small_teams_disrupt_science_and_tech"
authors:
  - "Lingfei Wu"
  - "Dashun Wang"
  - "James A. Evans"
date: "2019.02"
doi: "10.1038/s41586-019-0941-9"
arxiv: ""
score: 4.0
essence: "65백만 개 이상의 논문, 특허, 소프트웨어 제품 분석을 통해 소규모 팀은 과학기술을 혁신(disrupt)하고 대규모 팀은 기존 아이디어를 발전(develop)시킨다는 것을 입증했다."
tags:
  - "cat/Research_Quality_and_Demographics"
  - "sub/Collaboration_and_Team_Effects"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wu et al._2019_Large teams develop and small teams disrupt science and technology.pdf"
---

# Large teams develop and small teams disrupt science and technology

> **저자**: Lingfei Wu, Dashun Wang, James A. Evans | **날짜**: 2019-02-21 | **DOI**: [10.1038/s41586-019-0941-9](https://doi.org/10.1038/s41586-019-0941-9)

---

## Essence

![Figure 2](figures/fig2.webp)

*Fig. 2 | Small teams disrupt whereas large teams develop. a–c, For*

65백만 개 이상의 논문, 특허, 소프트웨어 제품 분석을 통해 소규모 팀은 과학기술을 혁신(disrupt)하고 대규모 팀은 기존 아이디어를 발전(develop)시킨다는 것을 입증했다.

## Motivation

- **Known**: 과학기술 분야에서 팀 규모의 증가 추세가 관찰되고 있으며, 이는 전문화, 통신기술 발전, 학제간 협력 필요성 때문으로 알려져 있다. 그러나 팀 규모가 지식발견과 기술혁신에 최적화되어 있는지는 증거 부족 상태이다.
- **Gap**: 대규모 팀이 더 많은 인용을 받는다는 것은 알려져 있으나, 단순 인용 수만으로는 혁신적 기여와 발전적 기여를 구분할 수 없다. 팀 규모와 과학기술의 혁신성(disruption) 간의 체계적 관계는 규명되지 않았다.
- **Why**: 과학기술 정책과 자금 배분이 대규모 팀 중심으로 편향되어 있는 현황에서, 소규모 팀의 혁신적 역할을 입증함으로써 다양한 팀 규모를 지원하는 균형잡힌 정책 수립의 근거를 제공한다.
- **Approach**: 세 가지 출처(Web of Science 논문, US 특허, GitHub 소프트웨어)에서 수집한 65백만 개 데이터에 대해 disruption 지수(-1~1)를 계산하여 팀 규모별 과학기술의 혁신성을 정량적으로 측정하고 비교 분석했다.

## Achievement


- **팀 규모와 혁신성의 역관계**: 팀이 1명에서 50명으로 증가할 때 논문, 특허, 소프트웨어의 disruption 점수가 각각 70, 30, 50 백분위수 감소
- **고임팩트 작업의 명확한 분화**: 상위 5% 인용 수준에서 솔로 저자는 고임팩트 논문 생산 확률이 10인 팀과 동등하나, 혁신적 논문 생산 확률은 72% 더 높음
- **시간과 분야에 걸친 일관성**: 1954-2014년 전 기간과 90% 학문 분야에서 팀 규모와 disruption의 음의 상관관계 일관되게 관찰
- **disruption 지수의 타당성 검증**: 노벨상 수상 논문이 상위 2% disruption 분포에 위치, BTW 모델 논문(혁신)은 상위 1%, Bose-Einstein 응축 논문(발전)은 하위 3%에 위치

## How

![Figure 1](figures/fig1.webp)

*Fig. 1 | Quantifying disruption. a, Simplified illustration of disruption.*

- Web of Science에서 42백만 논문(611백만 인용), USPTO에서 500만 특허(6500만 인용), GitHub에서 1600만 소프트웨어 프로젝트와 900만 포크 수집
- Citation displacement를 기반으로 한 disruption 지수 D = (p_i - p_j)/(n_i + n_j + n_k) 계산 (i: 해당 논문, j: 인용된 논문, k: 동시 인용 논문)
- 팀 규모별로 disruption 점수의 분포를 분석하고 백분위 변화 측정
- 고임팩트 작업(상위 5% 인용)에 대해 별도 분석 실행
- 시간 기간, 학문 분야, 논문 유형(이론/경험, 리뷰/원저)별 층화 분석 실행
- arXiv 매칭을 통해 논문의 그림 개수로 이론-경험 구분 후 통제 분석 실행

## Originality

- **disruption 지수의 새로운 적용**: 기존 특허 분석용 지수를 학술 논문, 특허, 소프트웨어에 걸쳐 대규모로 체계적 적용
- **세 도메인 통합 분석**: 65백만 개 규모의 이질적 데이터 소스를 동일한 개념으로 통합 분석하여 보편적 패턴 규명
- **개별 수준 분석**: 토픽과 연구 설계 통제 후에도 팀 크기 효과가 개인 수준에서 발생함을 입증 (사람들의 팀 이동 추적)
- **고임팩트 작업의 역설 발견**: 대규모 팀이 높은 임팩트 작업을 더 잘 생산하지만, 그것들이 오히려 덜 혁신적이라는 역설적 발견

## Limitation & Further Study

- **출판 및 인용 편향**: 소규모 팀의 혁신 작업이 즉시 인용되지 않고 미래에 평가될 가능성이 높아 현재 데이터로는 잠재적 혁신을 과소평가할 가능성
- **분야별 예외**: 컨퍼런스 중심의 컴퓨터 공학과 공학 분야에서 패턴이 약화되어 출판 문화에 따른 편향 존재
- **인과관계 미규명**: 팀 규모가 혁신성을 직접 결정하는지, 아니면 혁신적 사람들이 소규모 팀을 선택하는지는 미결정
- **GitHub 데이터 한계**: 2011-2014년 최근 4년만 포함하여 장기 추세 관찰 부족
- **후속 연구 필요**: 팀 조성(다양성, 위계), 기금 배분, 기관 구조 등 팀 성과에 영향미치는 다른 요인들에 대한 추가 조사 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 팀 규모와 혁신성 관계에 대한 과학적 증거를 대규모 데이터로 처음 체계적으로 제시한 중요한 연구이며, 과학정책 수립에 직접적 함의를 제공한다. 다만 인과관계 규명과 분야별 메커니즘에 대한 추가 연구가 필요하다.

## Related Papers

- ⚖️ 반론/비판: [[papers/977_Introducing_multiverse_analysis_to_bibliometrics_The_case_of/review]] — 팀 규모-파괴성 관계의 견고성에 대한 의문을 다중우주분석을 통해 체계적으로 검증받음
- 🔗 후속 연구: [[papers/934_Are_disruptive_papers_more_likely_to_impact_technology_and_s/review]] — 파괴적 논문의 기술-사회 영향력을 팀 규모별로 분석하여 혁신의 다층적 효과 이해 가능
- 🏛 기반 연구: [[papers/995_Papers_and_patents_are_becoming_less_disruptive_over_time/review]] — 논문과 특허의 파괴성 감소 현상을 팀 규모 변화와 연결하여 과학 발전의 구조적 변화 설명
- 🔗 후속 연구: [[papers/960_Evolution_of_the_social_network_of_scientific_collaborations/review]] — 과학 협력 네트워크에서 팀 크기가 연구 성과에 미치는 영향을 우선적 부착 메커니즘과 연결하여 분석한다.
- 🔗 후속 연구: [[papers/1046_The_structure_of_scientific_collaboration_networks/review]] — 협력 네트워크의 소규모 세계 특성을 팀 크기가 과학적 발견과 혁신에 미치는 차별적 영향으로 확장한다.
- 🔗 후속 연구: [[papers/1010_Remote_collaboration_fuses_fewer_breakthrough_ideas/review]] — 대규모 팀과 소규모 팀의 혁신 패턴 차이가 원격 협업에서 더욱 두드러지게 나타나는 현상을 설명할 수 있다.
- 🔗 후속 연구: [[papers/975_Interdisciplinary_papers_supported_by_disciplinary_grants_ga/review]] — 대형 팀이 과학기술을 발전시키고 소형 팀이 파괴적 혁신을 일으킨다는 연구와 연결하여 학제간 연구에서 팀 크기와 펀딩 방식의 상호작용을 이해한다.
- 🏛 기반 연구: [[papers/977_Introducing_multiverse_analysis_to_bibliometrics_The_case_of/review]] — 다중우주분석을 통해 팀 규모-혁신성 관계의 견고성을 검증하고 원 연구의 한계 보완
- 🏛 기반 연구: [[papers/995_Papers_and_patents_are_becoming_less_disruptive_over_time/review]] — 대규모 팀과 소규모 팀의 서로 다른 역할이 혁신성 변화의 기초적 메커니즘을 설명한다
- 🧪 응용 사례: [[papers/1030_The_Burden_of_Knowledge_and_the_Death_of_the_Renaissance_Man/review]] — 지식 부담 이론이 대규모 팀과 소규모 팀의 서로 다른 혁신 패턴을 설명하는 구체적 사례를 제공한다.
- 🔗 후속 연구: [[papers/1034_The_Increasing_Dominance_of_Teams_in_Production_of_Knowledge/review]] — 팀 기반 연구의 우세와 함께 대형 팀과 소형 팀이 각각 다른 유형의 과학적 기여를 한다는 세분화된 분석을 제공한다.
- 🔗 후속 연구: [[papers/999_Principles_of_Scientific_Research_Team_Formation_and_Evoluti/review]] — 대규모팀과 소규모팀의 지식 생산 방식 차이와 연구팀 형성 진화 원리가 상호 보완적인 팀 과학 연구이다.
