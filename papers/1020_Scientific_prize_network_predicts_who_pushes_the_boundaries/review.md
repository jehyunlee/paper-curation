---
title: "1020_Scientific_prize_network_predicts_who_pushes_the_boundaries"
authors:
  - "Yifang Ma"
  - "Brian Uzzi"
date: "2018"
doi: "10.1073/pnas.1800485115"
arxiv: ""
score: 4.0
essence: "3,000개 이상의 과학상(Scientific Prize)과 10,455명의 수상자 데이터를 분석하여 과학상 네트워크(Prize Network)가 과학의 경계를 확장하는 과학자들을 예측할 수 있음을 보여준다. 과학상의 집중도 증가와 학제 간 연결성이 과학의 엘리트 계층화와 지식 전파 경로를 드러낸다."
tags:
  - "cat/Science_of_Science_Research"
  - "sub/Research_Evaluation_and_Impact"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ma and Uzzi_2018_Scientific prize network predicts who pushes the boundaries of science.pdf"
---

# Scientific prize network predicts who pushes the boundaries of science

> **저자**: Yifang Ma, Brian Uzzi | **날짜**: 2018 | **DOI**: [10.1073/pnas.1800485115](https://doi.org/10.1073/pnas.1800485115)

---

## Essence

![Figure 2](figures/fig2.webp)

*Fig. 2 The exponential distribution of scientific prizewinning.  Plot and inset show*

3,000개 이상의 과학상(Scientific Prize)과 10,455명의 수상자 데이터를 분석하여 과학상 네트워크(Prize Network)가 과학의 경계를 확장하는 과학자들을 예측할 수 있음을 보여준다. 과학상의 집중도 증가와 학제 간 연결성이 과학의 엘리트 계층화와 지식 전파 경로를 드러낸다.

## Motivation

- **Known**: 과학상은 동료 과학자들의 최고 수준의 인정이며 신뢰성 부여, 재정 지원, 공동체 강화 등의 기능을 한다. 그러나 과학상의 전반적 효과에 대한 정량적 분석은 부족했다.
- **Gap**: 과학상의 폭발적 증가(연 100년 전 약 20개 → 현재 350개 이상)에도 불구하고, 글로벌 과학상 네트워크의 구조적 특성과 과학 발전과의 연관성에 대한 대규모 정량 분석이 부재했다.
- **Why**: 과학상 네트워크의 구조를 이해하면 향후 과학 발전 방향을 예측할 수 있고, 과학계의 계층화 메커니즘을 파악할 수 있으며, 어떤 과학자와 아이디어가 영향력을 갖게 될지 사전 식별이 가능하다.
- **Approach**: 100년 이상 50개국의 3,062개 과학상 수상자들의 발표, 인용, 제휴, 계보(Genealogy) 데이터를 수집하고, 네트워크 분석과 통계 모델링을 통해 상 간 전이 확률과 수상 결정 요인을 파악했다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2 The exponential distribution of scientific prizewinning.  Plot and inset show*

- **상의 폭발적 증가와 집중화 역설**: 과학상 수는 20년마다 약 2배 증가했으나, 1985년 이후 수상자 중 64.1%가 2개 이상, 13.7%가 5개 이상의 상을 수상하며 소수 엘리트의 수상 집중도가 유의미하게 증가했다(p<10⁻²¹)
- **분야별 계층적 명성 구조**: 각 분야는 상위 1-3개의 극고명성상(10,000 Wikipedia 조회), 중상층 명성상(1,000 조회), 전문화된 상(10-100 조회)의 3단계 계층 구조를 보인다
- **학제 간 지식 전파 경로 규명**: 다중 상 수상자들을 통해 분야 내·간 상들이 '상 전이 행렬(Transition Matrix)'로 정량화되는 네트워크를 형성하며, 이는 지식의 신뢰 전파와 확산 경로를 나타낸다", '**계보 및 공동저자 관계의 예측력**: 과학자의 계보 네트워크(Genealogical Network)와 공동저자 네트워크가 수상 여부와 수상 집중도를 강하게 예측하며, 이는 엘리트 과학자와 혁신 아이디어 간의 높은 상호연결성을 설명한다

## How

![Figure 3](figures/fig3.webp)

*Fig. 3 shows that the number of scientific prizes varies by discipline and is clustered by*

- 전 세계 3,062개 과학상의 포괄적 데이터베이스 구축 (100년 이상, 50개국, 10,455명 수상자)
- 각 수상자의 출판물, 인용도, 기관 소속, 과학 활동 기간, 계보적 관계, 공동저자 관계 기록
- 상을 노드로, 동일 과학자에 의한 상 수상을 간선으로 하는 '상 네트워크(Prize Network)' 구성", '간선 가중치: 두 상을 모두 수상한 과학자의 수로 정의하여 상 간 연결 강도 정량화
- Wikipedia 조회수를 기반으로 상의 명성(Prestige) 측정 및 10,000/1,000/100/10 조회수 기준으로 등급화
- Modularity 계산을 통해 분야별 상의 군집화 분석 (Modularity = 0.492)
- 상 전이 확률 행렬(Transition Matrix) 도출로 상 간 연결 경로의 통계적 특성 파악
- 계보 네트워크와 공동저자 네트워크를 독립변수로 하는 회귀 모형으로 수상 예측력 검증

## Originality

["과학상 네트워크의 '전역적(Global)' 구조를 처음으로 대규모 정량 분석한 연구 - 기존 Harriet Zuckerman의 노벨상 중심 연구를 3,000개 상으로 확장", "상의 폭발적 증가가 동시에 '계층화 심화'를 초래한다는 역설적 발견 - 기존의 '다양성 확대' 논의에 대한 실증적 반박", "'상 전이 행렬'을 통해 추상적인 지식 전파를 네트워크 과학으로 정량화 - 학제 간 경계와 지식 흐름의 메커니즘 규명", '계보적 관계(Advisor-Student, PhD lineage)를 포함한 학연 네트워크 분석 - 사회적 자본의 과학상 수상 영향도를 계량화한 첫 시도']

## Limitation & Further Study

- Wikipedia 조회수를 상의 명성 지표로 사용한 것의 편향성 - 온라인 가시성(Visibility)이 실제 과학적 영향도를 완벽히 반영하지 못할 수 있음
- 데이터 수집 시점의 시간적 한계 - 상의 선정 기준과 인정 체계가 시대별로 변했을 수 있으나 통제 부족
- 인과관계 규명의 한계 - 계보/공동저자 관계가 수상을 '결정'하는지, 아니면 우수 과학자들이 이미 네트워크화된 것인지 구분 불명확", '상 간 인정 기준의 상이성 미흡 - 각 분야의 나이(Age), 규모(Scale), 자금 구조가 상 수의 차이를 초래하나 정규화 부족
- **후속연구**: (1) 동적 인과 추론(Dynamic Causal Inference)으로 계보 효과의 순수 영향도 파악, (2) 상 수상이 이후 논문 인용도·특허화(Patenting)에 미치는 영향 추적, (3) 상 수상의 사회경제적 배경(Gender, Geography, Institutional Prestige)에 따른 불평등 분석

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 과학상 네트워크의 전역 구조를 최초로 정량 분석하여 과학의 계층화 메커니즘과 지식 전파 경로를 규명한 고도로 독창적이고 중요한 연구이다. 계보·공동저자 네트워크의 높은 예측력은 과학 엘리트의 형성이 개인 역량뿐 아니라 사회적 자본에도 크게 의존함을 시사하며, 과학정책과 과학사 연구에 실질적 기여를 한다.

## Related Papers

- ⚖️ 반론/비판: [[papers/941_Big_Names_or_Big_Ideas_Do_Peer-Review_Panels_Select_the_Best/review]] — 동료평가에서 명성과 아이디어 중 어느 것이 더 중요한지에 대한 상반된 관점을 제시하여 과학상 예측력의 한계를 보여준다.
- 🔗 후속 연구: [[papers/1035_The_Innovation_Recognition_Paradox_How_Science_Undervalues_t/review]] — 과학에서 혁신의 인정 역설을 통해 과학상 네트워크가 진정한 혁신을 얼마나 잘 포착하는지 비판적으로 검토할 수 있다.
- 🏛 기반 연구: [[papers/962_Forecasting_high-impact_research_topics_via_machine_learning/review]] — 과학상 수상자 네트워크 분석을 통한 혁신 예측 연구가 고임팩트 연구 예측의 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/1056_Where_Do_Your_Citations_Come_From_Citation-Constellation_A_F/review]] — 인용 네트워크 분석을 과학상 네트워크가 과학 경계 확장 예측에 미치는 영향으로 확장한다.
