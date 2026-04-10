---
title: "933_An_index_to_quantify_an_individuals_scientific_research_outp"
authors:
  - "J. E. Hirsch"
date: "2005"
doi: "10.1073/pnas.0507655102"
arxiv: ""
score: 5.0
essence: "개인의 과학적 연구 성과를 정량화하기 위해 h-index를 제안한다. h-index는 h편 이상의 인용수를 가진 논문의 개수로 정의되며, 연구자의 생산성과 영향력을 동시에 반영하는 단일 지표이다."
tags:
  - "cat/Bibliometric_Network_Analysis"
  - "sub/Citation_Metrics_and_Indices"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Hirsch_2005_An index to quantify an individual's scientific research output.pdf"
---

# An index to quantify an individual's scientific research output

> **저자**: J. E. Hirsch | **날짜**: 2005 | **DOI**: [10.1073/pnas.0507655102](https://doi.org/10.1073/pnas.0507655102)

---

## Essence


개인의 과학적 연구 성과를 정량화하기 위해 h-index를 제안한다. h-index는 h편 이상의 인용수를 가진 논문의 개수로 정의되며, 연구자의 생산성과 영향력을 동시에 반영하는 단일 지표이다.

## Motivation

- **Known**: 개별 연구자의 학술적 기여도를 평가하기 위해 총 논문수, 총 인용수, 논문당 평균 인용수 등 다양한 지표들이 사용되어 왔으나, 각각의 지표는 생산성, 영향력, 공저자 효과 등에서 편향성을 갖는다.
- **Gap**: 단일하면서도 생산성과 영향력 모두를 공정하게 반영하고, 서로 다른 경력 단계의 연구자들을 비교 가능하게 하는 평가 지표가 부재하다.
- **Why**: 대학 교원 채용, 펀딩 심사, 상 수상 등 학술 평가 상황에서 연구자의 과학적 기여도를 객관적으로 정량화할 필요성이 있으며, 이는 제한된 자원 배분의 정당성을 위해 필수적이다.
- **Approach**: 출판 기록과 인용 기록이라는 객관적 데이터를 활용하여 새로운 지표 h-index를 정의하고, 물리학자들의 데이터를 실증적으로 분석하여 다른 지표와 비교하고 수학적 모델로 검증한다.

## Achievement


- **h-index 정의 및 개념화**: h편 이상의 인용수를 갖춘 논문의 개수로 정의하여 간단하면서도 강력한 지표 제시
- **기존 지표와의 비교 분석**: 총 논문수, 총 인용수, 논문당 인용수, 고인용 논문 개수 등과 비교하여 h-index의 우월성 입증
- **실증적 검증**: E. Witten (h=110), A.J. Heeger (h=107) 등 저명한 물리학자들의 h-index 계산 및 제시
- **수학적 모델링**: 선형 모델 및 stretched exponential 모델을 통해 h와 총 인용수 관계(Nc,tot = ah²) 도출 및 a값 범위(3-5) 규명
- **학제 간 확장성**: 물리학뿐 아니라 생물학 등 다른 과학 분야에도 적용 가능함을 제시

## How


- Thomson ISI Web of Science 데이터베이스에서 '인용 횟수'로 논문 정렬", '인용수가 논문 순위와 같아지는 지점을 찾아 h-index 결정
- 선형 모델(Nc(y) = N₀ - (N₀-h)y)을 적용하여 이론적 분포 도출
- stretched exponential 분포(Nc(y) = N₀e^(-(y/y₀)^β))로 현실적 모델 구성
- 매개변수 a, β, α를 변화시켜 다양한 연구자 분포 모델링
- h와 경력연수(n)의 관계(h ∼ mn)를 선형 회귀로 분석

## Originality

- 단순하면서도 강력한 h-index 개념 창안 - 이전에 없던 새로운 평가 지표의 개발
- 생산성(논문수)과 영향력(인용수)의 균형을 수학적으로 표현한 혁신적 시도
- 단순 선형 모델에서 stretched exponential 모델로 점진적 정교화
- 총 인용수와 h의 관계식(Nc,tot = ah²) 도출을 통한 이론적 기초 제공
- 경력 단계별 비교 가능성을 고려한 설계(h = mn 관계식)

## Limitation & Further Study

- **공저자 효과**: 여러 저자가 참여한 논문의 경우 개별 기여도 반영 부족
- **학문 분야 간 인용 문화 차이**: 학문 분야별로 인용 관습이 다르기 때문에 cross-field 비교 어려움
- **시간 지체 효과**: 최근 논문은 충분한 인용을 받기까지 시간이 필요하므로 신진 연구자에게 불리
- **'Sleeping Beauty' 논문**: 오랜 시간 인용되지 않다가 이후 높은 인용을 받는 논문의 부정확한 평가", '**리뷰 논문의 과도한 가중**: 리뷰 논문은 높은 인용수를 받지만 순 학문적 기여도와 차이 가능
- **후속 연구**: 학문 분야별 정규화 계수 도입, 저자 기여도 가중치 적용, 인용 시간 경과 고려 등이 필요

## Evaluation

- Novelty: 5/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 5/5
- Overall: 5/5

**총평**: 이 논문은 과학 평가 분야에 혁명적 영향을 미친 h-index를 처음 제안한 기념비적 작업으로, 간결하면서도 강력한 개념 제시와 견고한 수학적 기초, 그리고 실증적 검증을 통해 학술 평가의 새로운 표준을 제시하였다.

## Related Papers

- 🔗 후속 연구: [[papers/1047_Theory_and_Practice_of_the_g-index/review]] — h-index의 한계를 극복하기 위해 상위 논문들의 인용 성과를 더 잘 반영하는 g-index를 제안한다.
- 🏛 기반 연구: [[papers/1049_Universality_of_citation_distributions_Toward_an_objective_m/review]] — h-index와 같은 개별 지표를 넘어 학문분야 간 객관적 비교를 위한 보편적 인용 분포 모델을 제공한다.
- 🔗 후속 연구: [[papers/946_Collective_Credit_Allocation_in_Science/review]] — 개별 연구자의 성과 측정을 다중저자 환경에서 공정한 기여도 배분 문제로 확장한다.
- 🧪 응용 사례: [[papers/1036_The_Matthew_effect_in_science_funding/review]] — h-index와 같은 계량지표가 연구비 배분에서 어떻게 기존 우위를 강화하는지 보여준다.
- 🔗 후속 연구: [[papers/1052_Updated_science-wide_author_databases_of_standardized_citati/review]] — 개별 연구자의 과학적 성과를 정량화하는 h-지수 연구를 전체 과학 분야로 확장한 표준화된 데이터베이스를 제공한다.
- 🔄 다른 접근: [[papers/1007_Redefining_Academic_Performance_The_Development_of_the_NK_Co/review]] — h-index의 한계를 극복하기 위한 다차원적 접근법으로 NK 지수와 상호 보완적 평가가 가능하다.
- 🔄 다른 접근: [[papers/946_Collective_Credit_Allocation_in_Science/review]] — h-지수와 같은 개인 연구 성과 지표와 다른 접근으로 집단 작업에서의 개별 기여도를 정량화하는 대안적 평가 방법을 제안한다.
