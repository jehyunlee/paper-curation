---
title: "946_Collective_Credit_Allocation_in_Science"
authors:
  - "Hua-Wei Shen"
  - "Albert-László Barabási"
date: "2014.08"
doi: "10.1073/pnas.1401992111"
arxiv: ""
score: 4.0
essence: "다중저자 논문에서 각 저자의 기여도를 정량화하기 위해 인용 패턴 기반의 학제 독립적 신용 배분 알고리즘을 개발했다. 이 방법은 과학 커뮤니티의 비공식적 집단 신용 배분 과정을 수학적으로 모델링한다."
tags:
  - "cat/Science_of_Science_Research"
  - "cat/Bibliometric_Network_Analysis"
  - "sub/Research_Evaluation_and_Impact"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Shen and Barabási_2014_Collective credit allocation in science.pdf"
---

# Collective credit allocation in science

> **저자**: Hua-Wei Shen, Albert-László Barabási | **날짜**: 2014-08-26 | **DOI**: [10.1073/pnas.1401992111](https://doi.org/10.1073/pnas.1401992111)

---

## Essence

![Figure 2](figures/fig2.webp)

*Fig. 2. Illustrating the credit allocation process. a, The target*

다중저자 논문에서 각 저자의 기여도를 정량화하기 위해 인용 패턴 기반의 학제 독립적 신용 배분 알고리즘을 개발했다. 이 방법은 과학 커뮤니티의 비공식적 집단 신용 배분 과정을 수학적으로 모델링한다.

## Motivation

- **Known**: 단일저자 논문의 신용 배분은 명확하지만, 다중저자 논문에서는 학문 분야마다 상이한 비공식적 신용 배분 체계를 운영하고 있다. 저자 기여도 산정의 기존 접근법들(모든 저자 동등 배분, 저자 순서 기반 배분 등)은 커뮤니티의 실제 인식을 반영하지 못한다.
- **Gap**: 현존하는 신용 배분 방법들은 저자 기여도의 실제 차이를 무시하거나 학문 분야별 규칙에 의존하며, 과학 커뮤니티의 집단 인식 메커니즘을 포착하지 못한다. 학제를 초월한 통일된 신용 배분 방법이 부재하다.
- **Why**: 정확한 저자 기여도 평가는 채용, 펀딩, 승진 의사결정에 직접 영향을 미친다. 노벨상 수상자 사례(마지막 저자, 3번째 저자, 1번째 저자)에서 보듯이 커뮤니티는 공식 저자 순서와 무관하게 신용을 배분한다.
- **Approach**: 대상 논문(p0)을 인용하는 논문들(D)과 그들이 함께 인용하는 논문들(P)의 동시인용(co-citation) 네트워크를 구성한다. 동시인용 강도(co-citation strength)와 공저자 정보를 이용하여 신용 배분 행렬 A를 구성하고, 선형 결합으로 각 저자의 신용 점유율을 계산한다.

## Achievement

![Figure 3](figures/fig3.webp)

*Fig. 3. Identifying Nobel laureates from the prize-winning papers in Physics, Chemistry, and Medicine. We apply our meth*

- **학제 독립적 알고리즘 개발**: 분야별 저자 순서 규칙에 무관하게 작동하는 일반화된 신용 배분 방법을 제시했다.
- **노벨상 검증**: 2007, 2012년 물리학상 수상자들을 해당 논문의 저자 위치와 무관하게 정확히 식별했다.
- **동시인용 기반 측정**: 과학 커뮤니티의 암묵적 인식을 동시인용 패턴으로부터 추출하는 방법론을 수립했다.
- **비교 가능성 확보**: 함께 출판하지 않은 연구자들의 상대적 기여도도 같은 분야 내에서 비교 가능하게 만들었다.

## How

![Figure 2](figures/fig2.webp)

*Fig. 2. Illustrating the credit allocation process. a, The target*

- 대상 논문 p0의 모든 인용 논문(citing papers) 집합 D 추출
- D의 논문들이 인용한 모든 논문(co-cited papers) 집합 P 구성
- 각 공인용 논문 pj와 p0 사이의 동시인용 강도 sj 계산 (p0와 pj를 함께 인용한 횟수)
- 공인용 논문들의 저자 정보로부터 신용 배분 행렬 A 구성 (각 저자의 저작 참여 여부 기록)
- 행렬 연산 c = A·s를 통해 각 저자의 정규화된 신용 점유율 계산

## Originality

- **새로운 데이터 소스**: 인용 순서와 저자 위치 대신 동시인용(co-citation) 네트워크를 신용 배분의 증거로 사용한 혁신적 접근
- **커뮤니티 인식의 수학화**: 과학 커뮤니티의 비공식적, 집단적 신용 배분 과정을 처음으로 정량화 가능한 알고리즘으로 표현
- **극단적 사례 분석**: 저자가 다른 저작물의 양에 따라 신용 배분이 변하는 메커니즘을 수학적으로 증명
- **노벨상 기반 검증**: 실제 과학사적 사건(노벨상 수상)을 통해 방법론의 타당성을 입증한 첫 시도

## Limitation & Further Study

- **인용 편향 문제**: 높은 인용도는 반드시 높은 기여도를 의미하지 않으며, 분야별 인용 관행 차이를 충분히 보정하지 못함
- **시간 역학 미반영**: 저자의 기여도 시간 변화를 포착하지 못하며, 논문 발표 후 새로운 해석이나 재평가를 반영할 수 없음
- **신생 분야 적용 한계**: 인용도가 낮은 신규 논문이나 신생 분야에서는 신뢰성이 낮을 수 있음
- **저자 식별 문제**: 동일 저자의 이름 변이(결혼, 하이픈 포함 등)나 중복 이름으로 인한 오류 가능성
- **후속 연구**: 저자 기여도 명시 메타데이터와의 비교 검증, 장시간 추적 연구, 다학제 간 편향 분석 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 과학 신용 배분의 역사적 문제를 동시인용 네트워크 분석으로 혁신적으로 해결한 논문이다. 노벨상 검증을 통해 실제 효용성을 입증했으며, 학제 독립성으로 인해 과학 전반에 광범위하게 적용 가능한 높은 기여도를 지닌다.

## Related Papers

- 🧪 응용 사례: [[papers/1000_Productivity_Prominence_and_the_Effects_of_Academic_Environm/review]] — 집단적 신용 배분 알고리즘을 학술 환경이 개별 연구자의 생산성과 명성에 미치는 효과 분석에 적용한다.
- 🔗 후속 연구: [[papers/1059_Women_are_credited_less_in_science_than_men/review]] — 다중저자 논문의 공정한 신용 배분을 과학에서 성별에 따른 차별적 기여도 인정 문제로 확장한다.
- 🧪 응용 사례: [[papers/1032_The_Diversity-Innovation_Paradox_in_Science/review]] — 집단적 신용 배분을 팀 다양성이 혁신에 미치는 역설적 영향 분석에 적용한다.
- 🔗 후속 연구: [[papers/965_Gender-diverse_teams_produce_more_novel_and_higher-impact_sc/review]] — 저자별 기여도 정량화를 성별 다양성 팀이 생산하는 혁신적 고영향 과학의 신용 배분으로 확장한다.
- 🔄 다른 접근: [[papers/933_An_index_to_quantify_an_individuals_scientific_research_outp/review]] — h-지수와 같은 개인 연구 성과 지표와 다른 접근으로 집단 작업에서의 개별 기여도를 정량화하는 대안적 평가 방법을 제안한다.
- 🧪 응용 사례: [[papers/1056_Where_Do_Your_Citations_Come_From_Citation-Constellation_A_F/review]] — 인용 네트워크의 사회구조적 경로 분석을 다중저자 논문의 집단적 신용 배분 문제에 적용한다.
- 🧪 응용 사례: [[papers/1059_Women_are_credited_less_in_science_than_men/review]] — 과학에서의 집단적 신용 배분 원리를 성별 관점에서 재검토하여 공정한 업적 인정 시스템을 설계할 수 있다.
- 🏛 기반 연구: [[papers/1007_Redefining_Academic_Performance_The_Development_of_the_NK_Co/review]] — 과학에서의 집단적 신용 배분 원리가 NK 지수의 저자 기여도 평가 방법론의 이론적 근거를 제공한다.
- 🔗 후속 연구: [[papers/933_An_index_to_quantify_an_individuals_scientific_research_outp/review]] — 개별 연구자의 성과 측정을 다중저자 환경에서 공정한 기여도 배분 문제로 확장한다.
