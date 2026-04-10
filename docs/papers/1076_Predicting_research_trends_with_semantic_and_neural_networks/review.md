---
title: "1076_Predicting_research_trends_with_semantic_and_neural_networks"
authors:
  - "Mario Krenn"
  - "Anton Zeilinger"
date: "2020.01"
doi: "10.1073/pnas.1914370116"
arxiv: ""
score: 4.0
essence: "750,000개의 과학 논문으로부터 의미론적 네트워크(SemNet)를 구축하고 신경망을 이용해 양자물리학의 미래 연구 트렌드를 예측하며, 개인화된 혁신적 아이디어를 제시하는 방법을 개발했다."
tags:
  - "cat/Science_of_Science_Research"
  - "sub/Research_Evaluation_and_Impact"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Krenn and Zeilinger_2020_Predicting research trends with semantic and neural networks with an application in quantum physics.pdf"
---

# Predicting research trends with semantic and neural networks with an application in quantum physics

> **저자**: Mario Krenn, Anton Zeilinger | **날짜**: 2020-01-28 | **DOI**: [10.1073/pnas.1914370116](https://doi.org/10.1073/pnas.1914370116)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1.*

750,000개의 과학 논문으로부터 의미론적 네트워크(SemNet)를 구축하고 신경망을 이용해 양자물리학의 미래 연구 트렌드를 예측하며, 개인화된 혁신적 아이디어를 제시하는 방법을 개발했다.

## Motivation

- **Known**: 기존 연구는 생화학, 천문학 등 다양한 분야에서 의미론적 네트워크를 구축했으나, 기계학습을 통한 미래 예측과 개인화된 아이디어 제시는 미흡했다.
- **Gap**: 급속도로 증가하는 과학 출판물을 개별 연구자가 파악하기 어렵고, 자신의 전문분야 밖의 과학적 연결고리를 발견하기 위한 체계적 방법이 부족하다.
- **Why**: 구조화된 과학 지식에 접근할 수 있다면 과학의 경계를 확장하고 학제 간 연구를 촉진할 수 있으며, 특히 급성장하는 양자물리학 분야에서 연구 트렌드 파악이 필수적이다.
- **Approach**: 1919년 이후 발표된 750,000개의 물리학 논문으로부터 물리 개념 간의 동시 출현 관계를 분석해 의미론적 네트워크를 구축하고, 신경망을 이용해 과거 상태로부터 미래를 예측하며 네트워크 이론으로 예외적 성질의 개념 쌍을 식별한다.

## Achievement

![Figure 3](figures/fig3.webp)

*Fig. 3A shows the quantum physics topics that have grown*

- **역사적 우수 연구 주제 검증**: SemNet이 상을 수상한 과거의 양자물리학 주제들을 식별함으로써 유용한 의미론적 지식을 보유하고 있음을 확인
- **미래 트렌드 예측**: 신경망을 이용한 과거 SemNet 상태로부터 향후 5년간의 양자물리학 연구 발전을 높은 정확도로 예측
- **개인화된 혁신 아이디어 제시**: 네트워크 이론적 도구를 활용하여 연구자의 관심분야 범위 내에서 예외적 의미론적 특성을 가진 개념 쌍 식별
- **대규모 데이터 통합**: 100,000개의 arXiv 논문과 650,000개의 미국물리학회(APS) 논문을 통합한 1919년부터의 100년 데이터 활용

## How

![Figure 1](figures/fig1.webp)

*Fig. 1.*

- 인간이 작성한 개념 목록(13개 양자물리학 교과서 색인 + Wikipedia 카테고리)과 RAKE(Rapid Automatic Keyword Extraction)를 이용한 자동 생성 목록 결합으로 6,300개 용어의 개념 목록 구축
- arXiv와 APS 데이터베이스에서 두 개념이 논문 초록에 동시 출현할 때 노드 간 연결 형성
- 과거 SemNet 상태 시계열 데이터로 신경망 학습하여 미래 개념 간 연결 가능성 예측
- 네트워크 중심도(centrality), 근처성(proximity) 등 위상학적 지표를 이용해 독특하고 극단적 의미론적 특성을 가진 개념 쌍 식별
- 동의어 정규화, 사람 이름 제거, 오류 수정을 통한 개념 목록 최적화

## Originality

- 기존 의미론적 네트워크 연구와 달리 기계학습을 통한 과거 상태로부터의 미래 예측 도입
- 네트워크 이론과 기계학습을 결합하여 단순한 트렌드 예측을 넘어 개인화된 혁신적 아이디어 제시
- 100년 규모의 장기 과학 데이터를 활용한 대규모 의미론적 네트워크 구축
- 빠르게 성장하는 양자물리학 분야를 의미론적 네트워크 방법론의 이상적인 테스트베드로 선정하고 적용

## Limitation & Further Study

- 개념 자동 생성(RAKE)의 오류로 인한 수동 보정 필요로 확장성 제한 가능성
- 논문 초록에만 기반한 링크 생성으로 전체 논문 내용의 깊이 있는 관계 파악 미흡
- 예측 정확도 평가가 역사적 데이터 기반으로만 수행되어 실제 미래 예측의 검증 부족
- 물리학에만 적용된 결과로 다른 학문분야 일반화 가능성 미검토
- **후속 연구 방향**: (1) 딥러닝 기반 개념 추출로 자동화 개선, (2) 인용 네트워크나 저자 네트워크 통합, (3) 다른 학문분야 적용 확대, (4) 실시간 예측과 실제 발전 추적 시스템 구축

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 과학 문헌의 대규모 의미론적 네트워크 분석과 신경망 기반 예측을 결합하여 연구 트렌드 예측과 개인화된 혁신 아이디어 제시라는 새로운 가능성을 열었으며, 급성장하는 양자물리학에 성공적으로 적용하여 컴퓨터 지원 과학(computer-inspired science)의 실질적 기여를 입증한 의미 있는 연구이다.

## Related Papers

- 🏛 기반 연구: [[papers/1004_Quantifying_spatialtemporal_citation_diffusion_of_individual/review]] — 개별 논문의 공간-시간적 인용 확산 정량화가 의미론적 네트워크 기반 트렌드 예측의 확산 메커니즘 이해를 뒷받침한다.
- 🔄 다른 접근: [[papers/954_Do_novel_papers_attract_more_social_attention/review]] — 참신한 논문이 사회적 관심을 끄는 정도를 통해 연구 트렌드 예측에서 혁신성 지표의 다른 측면을 제공한다.
- 🔄 다른 접근: [[papers/962_Forecasting_high-impact_research_topics_via_machine_learning/review]] — 둘 다 머신러닝을 활용해 연구 트렌드를 예측하지만 지식그래프와 신경망이라는 서로 다른 접근법을 사용한다.
- 🏛 기반 연구: [[papers/963_Forecasting_the_future_of_artificial_intelligence_with_machi/review]] — 의미 네트워크와 신경망을 활용한 연구 트렌드 예측의 기본 방법론을 AI 분야에 특화하여 적용한다.
- 🧪 응용 사례: [[papers/1120_SciEvo_A_2_Million_30-Year_Cross-disciplinary_Dataset_for_Te/review]] — 30년 종단 데이터셋을 시맨틱 및 신경망 기반 연구 트렌드 예측에 활용한다.
- 🔗 후속 연구: [[papers/929_A_network_approach_to_topic_models/review]] — 네트워크 기반 토픽 모델링을 시맨틱 네트워크와 신경망을 결합한 연구 트렌드 예측으로 확장한다.
- 🧪 응용 사례: [[papers/1118_Paper_Circle_An_Open-source_Multi-agent_Research_Discovery_a/review]] — 의미 네트워크와 신경망을 활용한 연구 트렌드 예측을 다중 에이전트 파이프라인으로 구현하여 실용화한다.
