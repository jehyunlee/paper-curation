---
title: "966_Global_citation_inequality_is_on_the_rise"
authors:
  - "Mathias Wullum Nielsen"
  - "Jens Peter Andersen"
date: "2021"
doi: "10.1073/pnas.2012208118"
arxiv: ""
score: 4.0
essence: "2000-2015년 15년간 4백만 명의 저자와 2,600만 편의 논문을 분석한 결과, 상위 1% 인용 엘리트 과학자들의 인용 점유율이 14-21%로 증가하며 글로벌 인용 불평등(Gini 계수 0.65→0.70)이 심화되고 있음을 보여줌."
tags:
  - "cat/Scientific_Impact_and_Innovation"
  - "sub/Equity_and_diversity_in_science"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Nielsen and Andersen_2021_Global citation inequality is on the rise.pdf"
---

# Global citation inequality is on the rise

> **저자**: Mathias Wullum Nielsen, Jens Peter Andersen | **날짜**: 2021 | **DOI**: [10.1073/pnas.2012208118](https://doi.org/10.1073/pnas.2012208118)

---

## Essence


2000-2015년 15년간 4백만 명의 저자와 2,600만 편의 논문을 분석한 결과, 상위 1% 인용 엘리트 과학자들의 인용 점유율이 14-21%로 증가하며 글로벌 인용 불평등(Gini 계수 0.65→0.70)이 심화되고 있음을 보여줌.

## Motivation

- **Known**: 과학은 계층화된 사회 체계이며 Matthew 효과에 의해 성공한 과학자들이 더 많은 보상을 받는다는 것이 알려져 있음. 출판물과 인용이 과학 지위의 핵심이며 엘리트 과학자들이 대부분의 출판과 인용을 차지함.
- **Gap**: 학문 분야, 기관, 국가별 인용 집중도의 변화 추이와 저자 수준에서의 인용 불평등이 시간에 따라 심화되었는지 여부가 불명확함.
- **Why**: 과학의 불평등 심화는 창의적 경쟁을 촉진할 수 있으나, 한편으로는 자원 집중으로 인한 수익 감소, 아이디어 시장의 독점을 초래할 수 있어 과학 진화에 대한 중요한 함의를 가짐.
- **Approach**: 저자 판별(author disambiguation) 기술을 활용하여 WoS 데이터의 4백만 명 저자를 추적하고, 필드 정규화 인용 지수(ncs, nics)와 Gini 계수를 통해 시간별 인용 집중도 추이를 정량 분석함.

## Achievement


- **인용 불평등의 증가**: 상위 1% 저자의 인용 점유율이 14.7%에서 19.6%(fractional count)로, 14.1%에서 21%(full count)로 증가(상대 증가율 33-49%)
- **출판 활동의 이원화**: 상위 1%는 풀카운트 논문 출판이 연 10.1편에서 12.4편으로 증가했으나, 중위수 저자는 감소
- **협력 활동의 차별화**: 상위 1%는 공저 논문의 증가와 분할 카운트 출판의 감소 폭이 작아 총 출판 점유율 확대(5%→12%)
- **지역별 격차 심화**: 상위 인용 과학자들이 서유럽과 오세아니아 고등급 대학에 집중되는 한편, 미국의 엘리트 집중도는 소폭 감소
- **Gini 계수 상승**: 인용 불평등을 나타내는 Gini 계수가 0.65에서 0.70으로 상승

## How


- Clarivate Web of Science에서 의료과학, 자연과학, 농업과학 분야의 출판 및 인용 데이터 수집
- 저자 판별 알고리즘을 활용하여 5개 이상 출판 기록을 가진 저자의 개별 프로필 구성
- 필드 정규화 인용 스코어(ncs)를 인용 인플레이션으로 조정한 nics 지수 계산
- 전체 카운트(full count)와 분할 카운트(fractional count) 방식으로 개별 저자의 누적 인용 영향력 측정
- 인용 밀도 그래프(citation density plots)와 Gini 계수를 통해 불평등 추이 정량화
- 물리학/천문학의 대규모 협력 실험(LHC 등) 영향을 제거하기 위해 학문 분야별 별도 분석

## Originality

- 4백만 명 저자와 2,600만 편 논문을 포함한 대규모 링크드 데이터셋을 활용한 글로벌 규모의 실증 분석으로, 기존 연구의 제한적 범위를 확대
- 15년(2000-2015) 장기 시계열 추적으로 인용 불평등의 동적 변화를 최초로 정량화
- 출판, 인용, 협력 활동의 삼각형 관계를 분석하여 엘리트 과학자와 일반 과학자의 행동 양식의 차별화를 규명
- 학문 분야, 국가, 기관별 세밀한 계층 분석을 통해 불평등의 공간적 분포 패턴 제시
- 물리학/천문학의 대규모 협력 프로젝트 영향을 분리함으로써 구조적 불평등과 분야별 이상치를 구분

## Limitation & Further Study

- WoS 데이터에 의존하여 저널 출판 중심 학문만 포함되며, 도서, 회의 논문, 오픈액세스 등 다양한 학술활동이 누락될 수 있음
- 인용 수를 성공의 유일한 지표로 사용하여 연구의 질적 영향력이나 사회적 가치를 측정하지 못함
- 저자 판별 알고리즘의 오류율이 불평등 측정에 미치는 영향에 대한 검증이 부재
- 인용 불평등 증가의 인과 메커니즘(대학 평가 시스템, 펀딩 구조, 개방 과학 운동 등)에 대한 심층 분석 부족
- **후속연구**: 문항 정성 분석으로 엘리트 과학자의 채용, 펀딩, 협력 네트워크 기제 규명 필요; 2015년 이후 오픈액세스와 디지털화 영향 추적; 개발도상국 과학자의 위치 변화와 불평등 심화 메커니즘 분석

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 저자 판별 기술을 활용한 대규모 글로벌 데이터 분석으로 과학 시스템의 인용 불평등 심화를 처음 정량화하였으며, 출판-협력-인용의 연계 분석으로 엘리트와 일반 과학자의 행동 분화를 규명한 높은 수준의 실증 연구.

## Related Papers

- 🔗 후속 연구: [[papers/1059_Women_are_credited_less_in_science_than_men/review]] — 과학에서 여성이 받는 인정 부족 문제를 전체 인용 불평등 심화 현상의 구체적 사례로 확장하여 이해할 수 있다.
- ⚖️ 반론/비판: [[papers/1080_Robust_Evidence_for_Declining_Disruptiveness_Assessing_the_R/review]] — 파괴적 혁신성 감소에 대한 강건한 증거와 함께 인용 불평등 심화 현상을 종합적으로 검토하여 과학 발전의 복합적 양상을 파악한다.
- 🏛 기반 연구: [[papers/1032_The_Diversity-Innovation_Paradox_in_Science/review]] — 과학에서 다양성과 혁신의 역설적 관계가 인용 불평등 심화와 어떻게 연결되는지 이론적 기반을 제공한다.
- 🧪 응용 사례: [[papers/1049_Universality_of_citation_distributions_Toward_an_objective_m/review]] — 보편적 인용 분포 모델을 전세계 인용 불평등 증가 현상의 정량적 분석에 적용한다.
- 🏛 기반 연구: [[papers/1027_Systemic_Gendered_Citation_Imbalance_in_Computer_Science_Evi/review]] — 글로벌 인용 불평등의 증가 추세 속에서 성별 기반 인용 불균형이 어떤 위치에 있는지 맥락적으로 이해할 수 있다.
