---
title: "1066_Accelerating_science_with_human-aware_artificial_intelligenc"
authors:
  - "Jamshid Sourati"
  - "James A. Evans"
date: "2023.07"
doi: "10.1038/s41562-023-01648-z"
arxiv: ""
score: 4.0
essence: "과학자들의 전문성 분포를 AI 모델에 통합하면 미래 과학적 발견을 예측하는 능력이 최대 400% 향상되며, 이는 콘텐츠 기반 AI만으로는 놓치는 인간 중심의 과학 발전 메커니즘을 포착한다."
tags:
  - "cat/Scientific_Information_Systems"
  - "sub/AI-Driven_Research_Discovery"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Sourati and Evans_2023_Accelerating science with human-aware artificial intelligence.pdf"
---

# Accelerating science with human-aware artificial intelligence

> **저자**: Jamshid Sourati, James A. Evans | **날짜**: 2023-07-13 | **DOI**: [10.1038/s41562-023-01648-z](https://doi.org/10.1038/s41562-023-01648-z)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1 | Motivation and design of our approach to simulate human-accessible*

과학자들의 전문성 분포를 AI 모델에 통합하면 미래 과학적 발견을 예측하는 능력이 최대 400% 향상되며, 이는 콘텐츠 기반 AI만으로는 놓치는 인간 중심의 과학 발전 메커니즘을 포착한다.

## Motivation

- **Known**: 출판된 과학 논문 데이터로 학습한 AI 모델은 신약 개발과 신소재 발견에 성공했으나, 과학 커뮤니티의 인간 과학자들의 역할과 협력 네트워크는 간과되어왔다.
- **Gap**: 기존 AI 모델들은 과학 콘텐츠(논문 텍스트)에만 초점을 맞추고, 과학자들의 분포, 협력 관계, 그리고 인지적 접근성(cognitive accessibility)을 반영하지 못하여 미래 발견 예측의 정확도가 제한되어 있다.
- **Why**: 과학 발전은 개별 과학자들의 인지적 배경과 사회적 상호작용에 크게 영향을 받으므로, 인간 중심 AI는 연구 효율성을 극대화하고 미발견 영역의 가능성을 체계적으로 탐색할 수 있게 한다.
- **Approach**: 출판 메타데이터에서 추출한 저자-물질-성질의 혼합 하이퍼그래프(hypergraph) 위에서 랜덤 워크(random walk)를 수행하여 과학자들이 인지적으로 접근 가능한 추론 경로를 시뮬레이션하고, 이를 통해 인간 전문가 분포를 모델에 통합한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2 | Evaluating human-accessible discovery predictions against various*

- **예측 정확도 100% 향상**: 재료 과학 분야에서 기존 Word2Vec 기반 콘텐츠 분석 대비 약 100% 향상된 미래 발견 예측 성능
- **확장 가능성 입증**: 신약 개발(1,000+ 약물, 100+ 질병) 및 COVID-19 치료제 포함 수천 개의 새로운 물질-성질 관계 예측 성능 비교 검증
- **희소 데이터 성능 우수**: 관련 문헌이 제한된 경우 human-aware AI의 성능 향상이 특히 두드러짐
- **보완적 발견 생성**: 과학 커뮤니티의 집단 인지에서 놓친 '이질적(alien)' 가설을 체계적으로 생성하여 미래 과학 발전 가능성 제시

## How

![Figure 1](figures/fig1.webp)

*Fig. 1 | Motivation and design of our approach to simulate human-accessible*

- 혼합 하이퍼그래프 구성: 저자(author), 물질(material), 성질(property) 노드와 논문(hyperedge)을 통합
- 랜덤 워크 시뮬레이션: (1) 성질을 시작점으로 초기화, (2) 해당 성질을 언급한 논문 선택, (3) 논문에서 저자 또는 물질 선택 후 반복하는 마코프 프로세스(Markov process) 수행
- 비균등 샘플링 파라미터 α 도입: 물질과 저자 노드 선택의 불균형 조정으로 협력(α 작음) vs. 독립 연구(α 큼) 강도 조절
- 근접성(proximity) 기반 예측: 저자-저자, 저자-물질, 물질-성질 간 거리를 계산하여 미래 발견 가능성과 관련 과학자 추정
- 가용성 휴리스틱(availability heuristic) 응용: 과학 커뮤니티에서 특정 주제 조합에 대한 집단 관심도가 미래 발견을 예측하는 신호임을 활용

## Originality

- 인간 전문가 분포를 AI 예측 모델에 정량적으로 통합한 새로운 접근법으로, 기존 콘텐츠 기반 AI와의 근본적인 패러다임 전환
- 심리학의 가용성 휴리스틱을 과학 커뮤니티 규모로 확장하여, 개인의 인지 편향이 집단 과학 발전에 미치는 체계적 영향 규명
- 랜덤 워크를 통한 인지적 접근성 시뮬레이션으로 '과학자가 상상할 수 있는 발견'을 명시적으로 모델링", 'Swanson의 지식 발견 휴리스틱을 AI 기반으로 자동화하고, 인간 과학자가 상상하기 어려운 보완적 가설의 체계적 생성 방법 개발

## Limitation & Further Study

- **데이터 제한**: 출판 메타데이터에만 의존하므로 미발표 연구, 동료 간 비공식 커뮤니케이션, 산업 비밀 등을 반영하지 못함
- **파라미터 튜닝의 민감성**: α 값 선택이 결과에 영향을 미치는데, 최적값 결정을 위한 명확한 가이드라인 부족
- **인과성 vs 상관성**: 랜덤 워크 근접성이 미래 발견을 예측한다는 것이 인과적 관계인지 상관적 관계인지 명확하지 않음
- **검증 시간차**: 모델이 미래 발견을 '예측'하는 것이지만, 실제 검증에는 장시간 소요되므로 예측 신뢰도의 즉시 평가 어려움", '**후속 연구**: (1) 실시간 협력 네트워크 데이터 통합, (2) 학제 간 발견의 메커니즘 심화 연구, (3) 모델 해석성(interpretability) 향상으로 특정 발견을 예측한 이유 설명 강화

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 과학적 발견의 사회적·인지적 차원을 AI에 통합한 획기적 연구로, 기존 콘텐츠 기반 AI의 한계를 극복하고 미래 발견 예측의 정확도를 대폭 향상시킨다. 과학 가속화와 혁신적 발견 발굴 모두에 실질적 기여 가능성이 높다.

## Related Papers

- 🔗 후속 연구: [[papers/965_Gender-diverse_teams_produce_more_novel_and_higher-impact_sc/review]] — 성별 다양성이 과학 혁신에 미치는 영향을 인간 중심 AI 접근법으로 확장하여 전문성 분포의 다양성 효과를 분석한다.
- 🏛 기반 연구: [[papers/1032_The_Diversity-Innovation_Paradox_in_Science/review]] — 과학에서 다양성-혁신 역설을 이해하는데 인간의 전문성을 고려한 AI 모델이 제공하는 통찰의 기반이 된다.
- 🔄 다른 접근: [[papers/1001_Public_Profile_Matters_A_Scalable_Integrated_Approach_to_Rec/review]] — 인용 추천에서 인간의 행동 패턴 대신 과학자의 전문성 분포를 AI에 통합하는 다른 접근법을 제시한다.
- ⚖️ 반론/비판: [[papers/1067_After_science/review]] — 인간 인식 AI를 통한 과학 가속화가 AI 주도 과학 이후 시대의 대안적 발전 방향을 제시한다.
