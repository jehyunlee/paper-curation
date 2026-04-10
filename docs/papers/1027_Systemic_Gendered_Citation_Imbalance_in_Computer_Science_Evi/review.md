---
title: "1027_Systemic_Gendered_Citation_Imbalance_in_Computer_Science_Evi"
authors:
  - "Kazuki Nakajima"
  - "Yuya Sasaki"
  - "Sohei Tokuno"
  - "George Fletcher"
date: "2026.03"
doi: ""
arxiv: ""
score: 4.0
essence: "컴퓨터과학 분야에서 여성 저자 논문이 예상보다 적은 인용을 받는 체계적 불균형을 발견하였으며, 이러한 현상이 학회 논문에서 특히 두드러진다."
tags:
  - "cat/Research_Quality_and_Demographics"
  - "sub/Bias_and_Inequality"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Nakajima et al._2026_Systemic Gendered Citation Imbalance in Computer Science Evidence from Conferences and Journals.pdf"
---

# Systemic Gendered Citation Imbalance in Computer Science: Evidence from Conferences and Journals

> **저자**: Kazuki Nakajima, Yuya Sasaki, Sohei Tokuno, George Fletcher | **날짜**: 2026-03-24 | **URL**: [https://arxiv.org/abs/2603.23273v1](https://arxiv.org/abs/2603.23273v1)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2: Gender imbalance in citations made by papers in computer science. Panels (a), (d),*

컴퓨터과학 분야에서 여성 저자 논문이 예상보다 적은 인용을 받는 체계적 불균형을 발견하였으며, 이러한 현상이 학회 논문에서 특히 두드러진다.

## Motivation

- **Known**: STEM 분야 전반과 컴퓨터과학에서 성별 불균형이 인구통계, 생산성, 인정, 채용, 경력 진행에서 나타나고 있다. 다른 학문 분야에서 여성 저자 논문의 인용 불균형이 보고되었다.
- **Gap**: 컴퓨터과학의 독특한 학회 중심 출판 문화에서 성별 인용 불균형의 패턴이 불명확하다. 학회와 저널 간 성별 인용 불균형의 차이를 비교한 연구가 부족하다.
- **Why**: 컴퓨터과학은 전 세계적으로 규모가 크고 급성장하며 영향력이 크므로, 포용적 대표성을 확보하여 혁신을 촉진하고 학문적 형평성을 달성하는 것이 필수적이다.
- **Approach**: 컴퓨터과학 학회와 저널 논문 394,432개와 인용 752,742개로 구성된 데이터셋을 구축하여 성별 저자의 인용 패턴을 분석했다. 네트워크의 구조적 특성을 고려한 참조 모델(reference model)을 통해 예상되는 인용 행동과 실제 인용 행동의 차이를 특성화했다.

## Achievement

![Figure 5](figures/fig5.webp)

*Figure 5: Gendered citation imbalance in different publication venues of computer science. (a)*

- **학회 논문에서의 성별 불균형**: 여성이 제1저자 또는 제후자인 논문이 예상보다 적은 인용을 받으며, 이 현상이 저널보다 학회 논문에서 특히 두드러짐
- **상위 학회에서의 심화**: 최상위권 학회 논문에서 성별 인용 불균형이 더욱 두드러짐
- **동질성 편향(homophily)의 역할**: 저자들이 특정 속성을 공유하는 논문을 인용하려는 경향이 불균형의 일부 원인임을 규명
- **네트워크 구조의 영향**: 제1저자와 제후자의 저명성과 공저자 네트워크 구조가 불균형의 잠재적 동인임을 확인
- **학회 중심 출판 문화의 증폭 효과**: 컴퓨터과학의 학회 중심 출판 관행이 체계적 불균형을 증폭시킬 수 있음을 제시

## How

![Figure 3](figures/fig3.webp)

*Figure 3: Gendered citation imbalance across subfields and topics in computer science. (a) Gender*

- DBLP와 OpenAlex 두 개의 개방 데이터베이스를 통합하여 독특한 데이터셋 구축
- 각 논문의 메타데이터에 서지정보, 저자 성별, 저자정보, 인용, 출판 장소, 연구 주제 등을 추가 보강
- 저자 성별에 따른 인용 행동을 네트워크 수준의 참조 모델을 이용하여 정규화된 인용 수(observed vs. expected)로 분석
- 학회와 저널 간 성별 인용 불균형을 비교 분석
- 인용 논문의 특성과 성별 인용 행동의 연관성 분석
- 연구 분야, 주제, 시간적 추이에 따른 불균형의 변화 추적

## Originality

- 컴퓨터과학의 학회 중심 출판 문화에서 성별 인용 불균형을 체계적으로 분석한 첫 종합 연구
- 학회와 저널의 성별 인용 불균형을 직접 비교하여 출판 형식의 영향을 규명
- 동질성 편향과 네트워크 구조를 함께 고려한 다층적 분석 제공
- 394,432개 논문과 752,742개 인용으로 구성된 대규모 통합 데이터셋 구축

## Limitation & Further Study

- 저자 성별을 이진(binary) 성별로만 분류하여 비이진 성별 정체성의 다양성을 반영하지 못함
- 성별 추정 알고리즘의 정확도 한계로 인해 일부 저자의 성별이 부정확할 수 있음
- 이진 성별 분류 외에 교차성(intersectionality), 지리적 위치, 기관의 지위 등 다른 사회적 요인의 상호작용을 고려하지 않음
- 시간 효과와 세대 효과의 구분이 명확하지 않아 인과관계 추론에 한계 있음
- 후속 연구에서는 더 세분화된 성별 범주, 저자 위치와 기관의 위계 효과, 동질성 편향을 완화하기 위한 실질적 개입 방안 연구 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 컴퓨터과학 분야의 성별 인용 불균형을 처음으로 체계적으로 규명하고, 학회 중심 출판 문화의 부정적 영향을 입증한 중요한 연구이다. 학계의 형평성 향상을 위한 데이터 기반 정책 수립에 기여할 수 있다.

## Related Papers

- 🔗 후속 연구: [[papers/1059_Women_are_credited_less_in_science_than_men/review]] — 여성 연구자의 업적 인정 부족이 인용 불균형으로도 나타나는 체계적 성별 편향의 다면적 증거를 제공한다.
- 🔄 다른 접근: [[papers/1035_The_Innovation_Recognition_Paradox_How_Science_Undervalues_t/review]] — 여성의 학제간 혁신이 과소평가되는 현상과 인용 불균형을 연결하여 성별 편향의 복합적 메커니즘을 이해할 수 있다.
- 🏛 기반 연구: [[papers/966_Global_citation_inequality_is_on_the_rise/review]] — 글로벌 인용 불평등의 증가 추세 속에서 성별 기반 인용 불균형이 어떤 위치에 있는지 맥락적으로 이해할 수 있다.
- 🧪 응용 사례: [[papers/970_Historical_Comparison_of_Gender_Inequality_in_Scientific_Car/review]] — 컴퓨터 과학의 체계적 성별 인용 불균형 분석과 연결되어 STEM 분야 전반의 성별 불평등이 인용 패턴에 미치는 구체적 영향을 보여준다.
- 🔗 후속 연구: [[papers/1035_The_Innovation_Recognition_Paradox_How_Science_Undervalues_t/review]] — 여성의 혁신적 기여 과소평가가 인용 불균형과 저널 게재 차별로 구체적으로 나타나는 다층적 메커니즘을 보여준다.
- 🏛 기반 연구: [[papers/1059_Women_are_credited_less_in_science_than_men/review]] — 여성 연구자의 업적 인정 부족이 컴퓨터과학 분야의 인용 불균형으로 구체적으로 나타나는 체계적 성별 편향의 연결고리를 보여준다.
