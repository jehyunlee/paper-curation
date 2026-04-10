---
title: "962_Forecasting_high-impact_research_topics_via_machine_learning"
authors:
  - "Xuemei Gu"
  - "Mario Krenn"
date: "2025.06"
doi: "10.1088/2632-2153/add6ef"
arxiv: ""
score: 4.0
essence: "21백만 개 과학논문으로부터 구축한 진화하는 지식그래프(evolving knowledge graph)와 머신러닝을 활용하여, 아직 발표되지 않은 새로운 연구 아이디어의 미래 임팩트를 미리 예측하는 방법을 개발했다."
tags:
  - "cat/Bibliometric_Network_Analysis"
  - "sub/Temporal_and_Longitudinal_Analysis"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Gu and Krenn_2025_Forecasting high-impact research topics via machine learning on evolving knowledge graphs.pdf"
---

# Forecasting high-impact research topics via machine learning on evolving knowledge graphs

> **저자**: Xuemei Gu, Mario Krenn | **날짜**: 2025-06-30 | **DOI**: [10.1088/2632-2153/add6ef](https://doi.org/10.1088/2632-2153/add6ef)

---

## Essence


21백만 개 과학논문으로부터 구축한 진화하는 지식그래프(evolving knowledge graph)와 머신러닝을 활용하여, 아직 발표되지 않은 새로운 연구 아이디어의 미래 임팩트를 미리 예측하는 방법을 개발했다.

## Motivation

- **Known**: 기존에는 논문 발표 후 인용도 기반으로 개별 논문의 영향력을 예측했으나, 이는 연구가 완료된 후 오래 지난 시점에서의 평가이다. 의미론적 지식그래프(semantic knowledge graphs)를 통한 링크 예측(link prediction)은 미래 연구 주제는 예측하나 그 임팩트까지는 고려하지 못했다.
- **Gap**: 개념 수준(concept level)에서 결합된 적 없는 새로운 과학 개념 조합이 미래에 얼마나 임팩트 있을지 조기에 예측할 수 있는 방법이 부재했다. 이는 인공지능 뮤즈(AI muse)가 과학자들에게 영향력 있는 아이디어를 제시하기 위해 필수적인 기능이다.
- **Why**: 과학논문의 지수적 증가로 인해 연구자들이 자신의 좁은 분야에만 집중하게 되며, 새로운 임팩트 있는 연구 방향과 학제 간 협력 발견이 어려워진다. 연구 초기 단계에서 임팩트를 예측할 수 있다면 전 지구적 과학 발전을 가속화할 수 있다.
- **Approach**: 의미론적 네트워크(개념 공동 연구)와 인용 네트워크(임팩트)를 결합한 멀티레이어 진화 지식그래프를 구축하고, 과거의 네트워크 동역학(network dynamics)으로 학습한 머신러닝 모델로 미래의 높은 인용도를 가질 새로운 개념 쌍을 예측한다.

## Achievement


- **대규모 지식그래프 구축**: 1709년부터 2023년 4월까지 21,165,421개 논문으로부터 368,825개 과학 개념과 시간-인용 정보가 포함된 지식그래프 생성
- **높은 예측 정확도**: 대부분의 실험에서 AUC 0.9 이상의 성능으로 미발표 개념 조합의 미래 인용도 예측 달성
- **최신 과학 트렌드 발굴**: 페로브스카이트 태양전지(perovskite solar cell), 비에르미안 위상(non-Hermitian topology), 머신러닝-물리학 융합 등 혁신적 분야 자동 추출
- **조기 영향력 평가**: 논문 작성 전 개념 수준에서 임팩트 예측으로 과학적 아이디어 초기 단계 평가 가능

## How


- arXiv, bioRxiv, medRxiv, chemRxiv 등 4개 프리프린트 서버에서 2,444,442개 논문 추출
- RAKE(Rapid Automatic Keyword Extraction) 알고리즘으로 제목과 초록에서 자동으로 주요 개념 추출
- 각 개념이 특정 최소 출현 빈도(2단어 개념: 9개 이상 논문)를 충족하는지 필터링
- 각 논문의 발표 연도와 누적 인용도, 연 단위 인용도로 간선(edge) 가중화
- 시간 윈도우를 설정하여 과거 네트워크 상태로부터 미래 간선 생성 및 인용도를 이진/다중클래스 분류 또는 회귀 문제로 정식화
- 그래프 신경망, 통계 기반 모델 등 다양한 머신러닝 기법 적용 및 성능 비교

## Originality

- **개념 수준의 임팩트 예측**: 기존 논문-수준 영향력 예측을 개념 쌍 수준으로 확장하여 아이디어 초기 단계에서의 평가 가능
- **하이브리드 지식그래프**: 의미론적 네트워크와 인용 네트워크를 통합하여 '무엇을 연구할 것인가'와 '그것이 얼마나 임팩트 있을 것인가'를 동시에 포착", '**대규모 다학제 데이터**: 양자물리, 광학, 머신러닝 등 다양한 분야를 포함한 21백만 논문 규모의 종합 지식그래프는 기존 연구 대비 획기적
- **미래 과학 어시스턴트 기초**: 단순한 예측 넘어 '인공 뮤즈'로서 과학자들에게 영감을 주는 새로운 인공지능 과학 도구의 개념 제시

## Limitation & Further Study

- **인용도의 한계**: 임팩트 지표로 인용도만 사용하여 인문학, 사회과학, 실용적 임팩트 등을 반영 못함
- **도메인 제한성**: 현재 양자물리와 광학 분야에 집중되어 있어 다른 과학 분야로의 일반화 필요
- **개념 추출의 자동화**: RAKE 기반 키워드 추출은 휴리스틱 기반이므로 고도화된 NLP/LLM 기반 개념 정제 필요
- **외부 변수 미반영**: 자금 지원, 연구 커뮤니티 규모, 정책 변화 등 외부 요인이 실제 연구 방향 결정에 미치는 영향 미포함
- **검증 한계**: 예측된 유망 개념 조합에 대한 현재 시점(2025년)의 실제 발생 여부 검증 데이터 부족
- **후속 연구**: 다양한 임팩트 메트릭 통합, 전체 과학 분야 포괄, LLM 기반 개념 정제, 실시간 예측 시스템 구축

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 미발표 연구 아이디어의 미래 임팩트를 예측하는 혁신적 접근법으로, 대규모 지식그래프와 머신러닝을 결합하여 높은 정확도를 달성했다. 과학 지원 AI 시스템의 새로운 패러다임을 제시하는 중요한 기여이나, 도메인 확장성과 인용도 기반의 임팩트 평가 한계 개선이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/1076_Predicting_research_trends_with_semantic_and_neural_networks/review]] — 둘 다 머신러닝을 활용해 연구 트렌드를 예측하지만 지식그래프와 신경망이라는 서로 다른 접근법을 사용한다.
- 🔗 후속 연구: [[papers/1003_Quantifying_Long-term_Scientific_Impact/review]] — 연구 아이디어의 미래 임팩트 예측이 장기적 과학적 영향력 정량화 연구의 발전된 형태이다.
- 🏛 기반 연구: [[papers/1020_Scientific_prize_network_predicts_who_pushes_the_boundaries/review]] — 과학상 수상자 네트워크 분석을 통한 혁신 예측 연구가 고임팩트 연구 예측의 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/1014_Risk_and_Artificial_Intelligence_Adoption_A_Scientometric_an/review]] — AI 위험 연구 트렌드 분석을 머신러닝 기반 고영향 연구 주제 예측 방법론으로 확장한다.
- 🧪 응용 사례: [[papers/1017_Science_as_exploration_in_a_knowledge_landscape_tracing_hots/review]] — 기계학습 기법을 통해 지식 공간에서의 탐색 패턴을 바탕으로 미래 연구 주제를 예측하는 구체적 적용 사례를 제시한다.
- 🏛 기반 연구: [[papers/998_Predicting_Scientific_Breakthroughs_Based_on_Structural_Dyna/review]] — 머신러닝을 통한 고영향 연구 주제 예측의 방법론적 기초를 제공한다
- 🧪 응용 사례: [[papers/1111_A_Strategic_Guide_to_White_Space_Analysis_for_Pharmaceutical/review]] — 머신러닝을 통한 고영향 연구 주제 예측을 제약 R&D의 백색공간 분석에 적용하여 혁신 기회를 발견한다.
- 🧪 응용 사례: [[papers/936_Atypical_Combinations_and_Scientific_Impact/review]] — 비전형적 조합을 통한 고영향 연구의 특성을 기계학습으로 미래 연구 토픽을 예측하는데 활용할 수 있다.
- 🔄 다른 접근: [[papers/1116_Harnessing_the_Power_of_Adversarial_Prompting_and_Large_Lang/review]] — 기계학습을 통한 고영향 연구 주제 예측과 다른 접근으로 적대적 프롬프팅을 통한 가설 생성 방법을 제안한다.
