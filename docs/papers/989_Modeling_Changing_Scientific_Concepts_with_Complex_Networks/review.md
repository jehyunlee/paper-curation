---
title: "989_Modeling_Changing_Scientific_Concepts_with_Complex_Networks"
authors:
  - "Sofía Aguilar-Valdez"
  - "Stefania Degaetano-Ortlieb"
date: "2026"
doi: "10.48550/ARXIV.2603.17594"
arxiv: ""
score: 4.0
essence: "LLM의 맥락 임베딩 대신 복잡 네트워크 기반 프레임워크를 사용하여 과학 개념의 시간적 변화를 해석 가능하게 모델링하며, 화학혁명의 플로지스톤(phlogiston) vs 산소(oxygen) 이론 경쟁 사례를 통해 개념 변화가 엔트로피(entropy)와 위상 밀도(topological density) 증가와 연관됨을 입증한다."
tags:
  - "cat/Scientific_Information_Systems"
  - "sub/Knowledge_Graphs_and_Semantic_Mapping"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Aguilar-Valdez and Degaetano-Ortlieb_2026_Modeling Changing Scientific Concepts with Complex Networks A Case Study on the Chemical Revolution.pdf"
---

# Modeling Changing Scientific Concepts with Complex Networks: A Case Study on the Chemical Revolution

> **저자**: Sofía Aguilar-Valdez, Stefania Degaetano-Ortlieb | **날짜**: 2026 | **DOI**: [10.48550/ARXIV.2603.17594](https://doi.org/10.48550/ARXIV.2603.17594)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Diachronic prototypical concepts. This*

LLM의 맥락 임베딩 대신 복잡 네트워크 기반 프레임워크를 사용하여 과학 개념의 시간적 변화를 해석 가능하게 모델링하며, 화학혁명의 플로지스톤(phlogiston) vs 산소(oxygen) 이론 경쟁 사례를 통해 개념 변화가 엔트로피(entropy)와 위상 밀도(topological density) 증가와 연관됨을 입증한다.

## Motivation

- **Known**: LLM 임베딩은 의미 변화 추적에 효과적이지만 해석 불가능성과 시간 인식 부족 문제가 있으며, 프로토타입 의미론(prototype semantics)은 개념을 중심-주변부(core-periphery) 구조로 표현할 수 있다.
- **Gap**: 시간-인식적(time-aware)이고 해석 가능한 개념 궤적(concept trajectories) 모델링 방법이 부족하며, 역사 데이터의 편향 증강(bias augmentation) 위험에 대한 대응이 필요하다.
- **Why**: 과학 개념은 역사적 변화의 지표이며, 특히 과학 개념은 문화적 모호성의 영향을 받지 않아 역사 변화의 보편적 센서 역할을 할 수 있기 때문이다.
- **Approach**: 토픽 모델(topic model) 기반 복잡 네트워크로 개념을 표현하고, Royal Society Corpus에서 추출한 시계열 데이터를 분석하여 개념 구조 이동(conceptual structure shift)을 감지한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: Diachronic prototypical concepts. This*

- **해석 가능한 개념 궤적 모델링**: 프로토타입 의미론 기반 네트워크 프레임워크로 개념의 시간적 변화를 시각화 가능하고 도메인 전문가가 검증 가능한 방식으로 모델링
- **온마시올로지 변화(onomasiological change) 검증**: 엔트로피 및 위상 밀도 증가가 동일 개념을 지칭하는 어휘들의 다양화와 연결성 증가를 나타냄을 정량적으로 입증
- **과학혁명 사례연구**: 1750-1800년대 플로지스톤에서 산소 이론으로의 전환 과정에서 air는 중심에서 주변부로, acid는 주변부에서 중심으로 이동하는 동적 개념 구조 변화 실증

## How

![Figure 2](figures/fig2.webp)

*Figure 2: Topic models evaluation. These results, produced by evaluating models for the 1800s non-cumulative*

- Royal Society Corpus에서 1750-1800년대 화학 관련 텍스트 추출
- 토픽 모델(Topic Modeling)을 이용하여 각 시간 슬라이스(decade)별 주제 분포 생성
- 토픽 클러스터를 기반으로 개념 네트워크 구성 (노드: 어휘, 엣지: 토픽 공동 출현)
- 네트워크 엔트로피(entropy) 및 밀도(density) 계산하여 시간 추이 분석
- Gephi 등 네트워크 시각화 도구로 중심-주변부 구조 가시화

## Originality

- LLM 임베딩 대신 **토픽 기반 복잡 네트워크** 사용으로 해석 가능성 확보
- **온마시올로지 접근법(onomasiological approach)** 적용: 단어의 의미 변화(semasiological) 추적이 아닌 고정된 개념의 어휘적 표현 경쟁 분석
- **프로토타입 의미론과 네트워크 과학의 융합**: 언어학 이론을 그래프 표현으로 구현
- **Digital Humanities 맥락에서 편향 저감**: 역사 데이터 편향 문제를 인식하고 주제 기반 필터링으로 대응

## Limitation & Further Study

- 단일 과학혁명 사례(화학혁명)만 분석되어 다른 과학 분야나 시대로의 일반화 검증 필요
- 토픽 모델의 주제 수(topic number) 결정이 주관적이며, 다양한 파라미터 설정에 따른 민감도 분석 부족
- Royal Society Corpus의 언어적/시간적 편향(영문, 특정 기관의 출판물)이 결과에 미치는 영향 미평가
- 개념의 "중심" vs "주변부" 경계 설정의 객관성 기준 부족
- **후속연구**: 다양한 과학 분야와 시대 확대, 자동화된 토픽 수 결정 방법, 다국어 코퍼스 확장, 개념 경계 자동 감지 알고리즘 개발

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: Digital Humanities와 NLP, 언어학을 교차학제적으로 결합하여 해석 가능하고 시간 인식적인 과학 개념 변화 분석 프레임워크를 제시하며, 화학혁명 사례에서 강력한 실증적 증거를 제공한다. 다만 단일 사례 분석 범위의 한계와 토픽 모델 의존성에 대한 추가 검증이 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/1068_Artificial_intelligence_and_illusions_of_understanding_in_sc/review]] — 과학에서 이해의 착각을 다루어 과학 개념 변화의 해석 가능한 모델링이 중요한 이유의 인지적 배경을 제공한다.
- 🔄 다른 접근: [[papers/986_Mapping_the_changing_structure_of_science_through_diachronic/review]] — 과학 구조의 통시적 변화를 LLM 임베딩 대신 복잡 네트워크로 분석하는 해석 가능한 대안적 접근법을 제시한다.
- 🧪 응용 사례: [[papers/1040_The_Price-Pareto_growth_model_of_networks_with_community_str/review]] — Price-Pareto 모델을 과학 개념의 변화하는 복잡 네트워크 모델링에 적용한다.
- 🔄 다른 접근: [[papers/986_Mapping_the_changing_structure_of_science_through_diachronic/review]] — 복잡 네트워크를 통한 과학 개념 모델링과 저널 임베딩을 통한 과학 구조 추적이라는 서로 다른 시간적 분석 접근법이다.
- 🧪 응용 사례: [[papers/929_A_network_approach_to_topic_models/review]] — 문서-단어 이분 네트워크 접근법을 과학 개념 변화의 복잡 네트워크 모델링에 적용한다.
