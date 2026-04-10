---
title: "1004_Quantifying_spatialtemporal_citation_diffusion_of_individual"
authors:
  - "Shuang Zhang"
  - "Feifan Liu"
  - "Haoxiang Xia"
date: "2025.12"
doi: "10.1002/asi.70021"
arxiv: ""
score: 4.0
essence: "본 논문은 문서 표현 학습 알고리즘을 활용하여 지식공간(knowledge space)에서 개별 논문의 인용(citation)이 시간과 공간적으로 어떻게 확산되는지를 정량화한다. 초기 인용 확산 특성이 장기 인용 누적과 논문의 혁신성(novelty)·파괴성(disruptiveness)을 어떻게 결정하는지를 밝힌다."
tags:
  - "cat/Bibliometric_Network_Analysis"
  - "cat/Scientific_Impact_and_Innovation"
  - "sub/Temporal_and_Longitudinal_Analysis"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhang et al._2025_Quantifying spatial–temporal citation diffusion of individual papers in knowledge space.pdf"
---

# Quantifying spatial–temporal citation diffusion of individual papers in knowledge space

> **저자**: Shuang Zhang, Feifan Liu, Haoxiang Xia | **날짜**: 12/2025 | **DOI**: [10.1002/asi.70021](https://doi.org/10.1002/asi.70021)

---

## Essence


본 논문은 문서 표현 학습 알고리즘을 활용하여 지식공간(knowledge space)에서 개별 논문의 인용(citation)이 시간과 공간적으로 어떻게 확산되는지를 정량화한다. 초기 인용 확산 특성이 장기 인용 누적과 논문의 혁신성(novelty)·파괴성(disruptiveness)을 어떻게 결정하는지를 밝힌다.

## Motivation

- **Known**: 개별 논문의 인용 동역학은 멱법칙 분포, '급증-감소(jump-decay)' 트렌드, 초우위 효과(preferential attachment) 등의 시간적 패턴을 보인다는 것이 알려져 있다. 또한 인용은 저널, 학과, 분야를 넘어 확산되며 단순 인용 수로는 논문의 장기 영향을 완전히 측정할 수 없다.
- **Gap**: 기존 연구는 시간적 인용 동역학에 집중했으나, 지식공간에서 인용의 공간적 확산-시간적 축적의 결합 과정(spatial-temporal patterns)은 거의 탐색되지 않았다. 특히 초기 공간적 확산 특성이 장기 인용 누적과 논문 혁신성에 미치는 영향은 미상이다.
- **Why**: 공간-시간적 인용 동역학을 이해하면 단기·장기 영향, 혁신성, 인용 누적의 복잡한 상호작용을 규명할 수 있어 과학평가체계 개선에 필수적이다. 또한 지식공간에서 논문의 광범위하고 먼 영향력을 평가할 수 있게 된다.
- **Approach**: 7개 대규모 학문분야의 수백만 개 논문에서 문서 표현 학습(document representation learning) 알고리즘을 적용하여 의미론적 연관성을 포착하고 저차원 임베딩 공간에서 인용 확산 궤적을 구성한다. 지식거리를 정량적으로 측정하여 공간-시간 확산 패턴을 분석한다.

## Achievement


- **지역화된 인용 이동성**: 인용 범위는 가우스 분포, 인용 거리는 지수 분포를 따르며 의미론적으로 국소화된 인용 패턴을 확인
- **초기 확산과 장기 영향의 연관성**: 초기 인용 확산 폭(breadth)이 넓을수록 장기 인용 성장이 크며, 초기 인용 수가 유사한 논문들 중에서 이 효과가 장기 영향을 크게 증폭
- **혁신/파괴적 논문의 차별적 패턴**: 혁신·파괴적 논문은 인용이 적고 지연되지만 초기에 더 긴 지식거리의 인용을 유인하며, 지식공간에서 광범위하고 먼 영향을 생성(고인용 논문보다도 큼)

## How


- 문서 표현 학습 알고리즘으로 7개 학문분야의 논문들을 저차원 임베딩 공간(지식공간)에 투영
- 각 논문의 인용자(citing papers)들을 시간 순서대로 추적하여 지식공간에서 인용 확산 궤적 구성
- 인용 범위(citation scope): 인용자가 분포한 지식거리 범위를 측정; 인용 거리(citation distance): 각 인용자와 원래 논문 간 임베딩 거리 계산
- 초기 확산 특성(초기 n년의 인용 범위와 거리)과 장기 인용 누적 간 상관분석 및 회귀분석(다른 변수 통제)
- 논문의 혁신성/파괴성을 분류하여 각 그룹의 공간-시간 인용 패턴 비교 분석

## Originality

- 지식공간에서 개별 논문 수준의 공간-시간적 인용 동역학을 정량화한 최초 연구
- 문서 표현 학습 알고리즘을 활용하여 '지식거리' 개념을 정량적으로 구현", '초기 공간적 확산 특성이 장기 인용과 논문 혁신성에 미치는 영향을 실증적으로 규명
- 혁신·파괴적 논문과 고인용 논문의 공간-시간 인용 패턴의 차별성을 체계적으로 밝힘

## Limitation & Further Study

- 7개 주요 학문분야에만 한정되어 다른 분야(인문학 등)의 일반화 가능성 제한
- 문서 표현 학습 알고리즘의 임베딩 공간이 학문적 의미를 완전히 포착하는지 검증 필요
- 인용 동기(방법론적 참고, 반박, 발전 등)를 구분하지 않음
- 후속 연구: 다양한 분야 확대, 인용 동기 분류 추가, 시간에 따른 공간 구조 변화 추적, 학제간 확산의 장기 효과 분석

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 지식공간에서 인용의 공간-시간 확산을 정량화하여 기존 시간적 중심의 인용 분석에 공간적 차원을 추가한 창의적 연구이다. 초기 확산 특성이 장기 영향과 혁신성을 좌우한다는 발견은 과학평가체계와 연구 영향 예측에 중요한 함의를 제공한다.

## Related Papers

- 🔗 후속 연구: [[papers/951_Defining_and_identifying_Sleeping_Beauties_in_science/review]] — 잠자는 미녀 논문의 지연된 인용 패턴을 공간-시간적 확산 모델로 더 정교하게 분석할 수 있는 방법론을 제시한다.
- 🧪 응용 사례: [[papers/1003_Quantifying_Long-term_Scientific_Impact/review]] — 개별 논문의 장기적 과학적 영향력을 정량화하는 연구에 공간-시간적 인용 확산 분석을 적용할 수 있다.
- 🔄 다른 접근: [[papers/927_A_Dynamic_Network_Measure_of_Technological_Change/review]] — 지식공간에서 인용 확산을 측정하는 대신 기술 네트워크에서 발명의 파괴적/통합적 영향을 정량화한다.
- 🏛 기반 연구: [[papers/1050_Unsupervised_embedding_of_trajectories_captures_the_latent_s/review]] — 논문의 궤적을 벡터공간에서 임베딩하여 잠재적 지식구조를 포착하는 방법론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/934_Are_disruptive_papers_more_likely_to_impact_technology_and_s/review]] — 인용 확산 패턴과 파괴적 지수 간의 관계를 통해 논문의 장기적 기술/사회 영향력을 예측한다.
- 🏛 기반 연구: [[papers/1076_Predicting_research_trends_with_semantic_and_neural_networks/review]] — 개별 논문의 공간-시간적 인용 확산 정량화가 의미론적 네트워크 기반 트렌드 예측의 확산 메커니즘 이해를 뒷받침한다.
- 🔗 후속 연구: [[papers/998_Predicting_Scientific_Breakthroughs_Based_on_Structural_Dyna/review]] — 개별 논문의 시공간적 인용 확산을 정량화하여 인용 네트워크 동역학을 확장한다
