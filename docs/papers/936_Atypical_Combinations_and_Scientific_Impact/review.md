---
title: "936_Atypical_Combinations_and_Scientific_Impact"
authors:
  - "Brian Uzzi"
  - "Satyam Mukherjee"
  - "Michael Stringer"
  - "Ben Jones"
date: "2013"
doi: "10.1126/science.1240474"
arxiv: ""
score: 4.0
essence: "1790만 개 논문 분석을 통해 최고 영향력의 과학은 기존 지식의 매우 관례적 조합을 기반으로 하면서도 동시에 비전형적 조합의 '침입'을 특징으로 함을 발견했다. 이러한 조합을 가진 논문은 높은 인용도를 보일 확률이 2배 높았다."
tags:
  - "cat/Scientific_Impact_and_Innovation"
  - "sub/Research_innovation_and_novelty"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Uzzi et al._2013_Atypical Combinations and Scientific Impact.pdf"
---

# Atypical Combinations and Scientific Impact

> **저자**: Brian Uzzi, Satyam Mukherjee, Michael Stringer, Ben Jones | **날짜**: 2013 | **DOI**: [10.1126/science.1240474](https://doi.org/10.1126/science.1240474)

---

## Essence

![Figure 2](figures/fig2.webp)

*Fig. 2. The probability of a “hit” paper, conditional on novelty and conventionality. This figure*

1790만 개 논문 분석을 통해 최고 영향력의 과학은 기존 지식의 매우 관례적 조합을 기반으로 하면서도 동시에 비전형적 조합의 '침입'을 특징으로 함을 발견했다. 이러한 조합을 가진 논문은 높은 인용도를 보일 확률이 2배 높았다.

## Motivation

- **Known**: 과학 혁신은 기존 지식의 독창적 조합으로부터 비롯되며, 팀 과학이 학문 경계를 넘나들며 새로운 아이디어를 촉발할 수 있다는 것이 알려져 있다.
- **Gap**: 그러나 비전형적 지식과 관례적 지식 사이의 최적 균형 조성이 혁신성과 영향력을 연결하는 핵심인지, 그리고 과학자들이 이를 어떻게 달성할 수 있는지는 거의 알려져 있지 않다.
- **Why**: 과학이 점점 더 좁은 전문 영역으로 세분화되는 상황에서 지식의 경계를 효과적으로 넘나들면서도 분야 수준의 관례적 사고의 이점을 유지하는 방법을 이해하는 것이 중요하다.
- **Approach**: 웹 오브 사이언스(WOS)의 1790만 개 논문을 대상으로 참고문헌의 저널 쌍 조합을 분석하고, 무작위 인용 네트워크와 비교하여 z-score를 계산해 비전형성을 정량화했다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2. The probability of a “hit” paper, conditional on novelty and conventionality. This figure*

- **비전형성의 정량화**: z-score 기반 방법으로 저널 쌍의 비전형성 정도를 측정하여, 전형적(높은 z-score)과 비전형적(낮은 z-score) 조합을 구분했다.
- **영향력과의 관계 규명**: 높은 관례성(높은 중앙값 z-score)과 함께 비전형적 조합(10분위수 z-score < 0)을 포함한 논문이 'hit' 논문(높은 인용도)일 확률이 약 2배 높음을 발견했다.", '**팀의 역할 밝히기**: 단독 저자 대비 팀이 친숙한 지식 영역에 비전형적 조합을 삽입할 확률이 37.7% 높음을 보였다.
- **학문 분야 간 보편성**: 이러한 패턴이 모든 과학 분야에서 거의 보편적으로 나타남을 입증했다.

## How

![Figure 1](figures/fig1.webp)

*Fig. 1. Novelty and conventionality in science. For a sample paper,*

- 웹 오브 사이언스 인덱싱된 15,613개 저널의 1억 2천만 개 이상의 저널 쌍에 대해 분석
- 각 논문의 참고문헌 목록에서 저널 쌍의 공인용(co-citation) 빈도 계산
- 몬테카를로 알고리즘 기반 무작위 인용 네트워크 생성 (각 논문의 인용 수와 시간 분포 보존)
- 관찰된 빈도와 무작위 예상 빈도를 비교하여 각 저널 쌍에 대한 z-score 계산
- 각 논문의 median z-score (관례성 중심 경향)와 10th-percentile z-score (비전형적 조합) 추출
- 논문의 인용도를 종속변수로 하여 이들 지표와의 관계 분석

## Originality

- 대규모 데이터(1790만 논문)를 활용한 과학적 창의성 연구의 규모와 체계성이 혁신적이다.
- z-score 기반의 '비전형성' 정량화 방법이 객관적이고 재현 가능한 측정 기준을 제시한다.", "단순한 학제 간 연구가 아닌, '관례적 기반 위의 비전형적 침입'이라는 구체적 패턴을 규명했다.", '팀 저자와 단독 저자의 혁신성 차이를 정량적으로 비교 분석한 것이 새롭다.
- 선행 연구들이 개별 사례나 제한된 분야에 초점을 맞춘 반면, 이 연구는 전 과학 분야의 보편적 패턴을 발견했다.

## Limitation & Further Study

- **저널 쌍 수준 분석의 한계**: 논문 수준이 아닌 저널 수준에서 조합을 분석하므로, 개별 논문의 미세한 혁신성을 완전히 포착하지 못할 수 있다.
- **인용도 중심의 영향력 측정**: 단기 인용도만 측정하므로 장기적 영향력이나 실제 과학적 기여도를 충분히 반영하지 않을 수 있다.
- **WOS 편향**: WOS 인덱싱 저널에 편향되어 있으며, 신흥 분야나 비영어 논문은 과소 대표된다.
- **인과관계 규명 부족**: 비전형적 조합이 높은 영향력을 '야기하는지', 아니면 고영향 논문들이 사후에 비전형적으로 보이는지는 명확하지 않다.", '**후속 연구**: 특정 분야별 최적 비전형성 수준의 차이 분석, 논문의 실제 방법론 수준에서의 비전형성 검증, 저자의 경력단계별 차이 분석이 필요하다.

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 논문은 거대 규모 데이터 분석을 통해 과학적 혁신의 구체적 패턴을 규명한 중요한 연구이다. 관례성과 비전형성의 균형이 높은 영향력의 핵심이라는 통찰은 과학 정책과 팀 구성에 실질적 함의를 제공한다.

## Related Papers

- 🧪 응용 사례: [[papers/962_Forecasting_high-impact_research_topics_via_machine_learning/review]] — 비전형적 조합을 통한 고영향 연구의 특성을 기계학습으로 미래 연구 토픽을 예측하는데 활용할 수 있다.
- 🔗 후속 연구: [[papers/972_Identifying_interdisciplinary_emergence_in_the_science_of_sc/review]] — 학제간 융합의 출현을 식별하는 연구에 비전형적 조합 분석을 적용하여 혁신적 융합 연구를 예측할 수 있다.
- 🔗 후속 연구: [[papers/954_Do_novel_papers_attract_more_social_attention/review]] — 비전형적 조합이 과학적 영향력에 미치는 효과 연구를 소셜 미디어 관심도까지 확장하여 혁신성의 다면적 영향을 검증한다.
- 🧪 응용 사례: [[papers/972_Identifying_interdisciplinary_emergence_in_the_science_of_sc/review]] — BERTopic 모델링으로 식별된 학제간 결합이 실제로 비전형적 조합을 통한 과학적 임팩트로 이어지는지 검증할 수 있다.
- 🏛 기반 연구: [[papers/1032_The_Diversity-Innovation_Paradox_in_Science/review]] — 비전형적 조합이 과학적 영향을 높이지만 소수집단의 기여가 과소평가되는 역설을 설명하는 이론적 기반을 제공한다.
- 🔄 다른 접근: [[papers/995_Papers_and_patents_are_becoming_less_disruptive_over_time/review]] — 비전형적 조합이 과학적 영향력을 높인다는 상반된 관점을 제시한다
- 🧪 응용 사례: [[papers/1030_The_Burden_of_Knowledge_and_the_Death_of_the_Renaissance_Man/review]] — 비정형적 조합이 과학적 영향에 미치는 효과를 통해 전문화 심화 속에서도 혁신을 창출하는 메커니즘을 구체적으로 보여준다.
- 🧪 응용 사례: [[papers/927_A_Dynamic_Network_Measure_of_Technological_Change/review]] — 기술 변화의 동적 측정을 비전형적 조합이 과학적 영향력에 미치는 효과 분석에 적용한다.
- 🧪 응용 사례: [[papers/951_Defining_and_identifying_Sleeping_Beauties_in_science/review]] — 비전형적 조합과 과학적 영향력 연구와 연결되어 잠자는 미녀 논문들이 보이는 비전형적 특성과 지연된 인정 패턴을 설명한다.
