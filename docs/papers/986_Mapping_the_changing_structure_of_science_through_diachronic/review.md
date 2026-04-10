---
title: "986_Mapping_the_changing_structure_of_science_through_diachronic"
authors:
  - "Zhuoqi Lyu"
  - "Qing Ke"
date: "2025.12"
doi: "10.1016/j.chaos.2025.117295"
arxiv: ""
score: 4.0
essence: "학술지의 시간변화 임베딩(diachronic embedding)을 개발하여 과학 구조의 진화를 추적하고, 물리-생명-보건 삼각형 매핑을 통해 학제간 과학 경관의 변화를 정량화한다."
tags:
  - "cat/Bibliometric_Network_Analysis"
  - "sub/Temporal_and_Longitudinal_Analysis"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Lyu and Ke_2025_Mapping the changing structure of science through diachronic periodical embeddings.pdf"
---

# Mapping the changing structure of science through diachronic periodical embeddings

> **저자**: Zhuoqi Lyu, Qing Ke | **날짜**: 12/2025 | **DOI**: [10.1016/j.chaos.2025.117295](https://doi.org/10.1016/j.chaos.2025.117295)

---

## Essence


학술지의 시간변화 임베딩(diachronic embedding)을 개발하여 과학 구조의 진화를 추적하고, 물리-생명-보건 삼각형 매핑을 통해 학제간 과학 경관의 변화를 정량화한다.

## Motivation

- **Known**: 학술지는 과학 구조를 탐색하기 위한 중요한 대상으로 사용되어 왔으나, 기존 연구들은 정적인 표현만 제공하여 시간에 따른 과학의 동적 진화를 포착하지 못했다.
- **Gap**: 과학 분야의 출현, 학제간 통합, 출판 기술 변화 등으로 인한 동적 변화를 추적할 수 있는 시간 변화형 학술지 표현이 부재하다.
- **Why**: 과학의 진화 메커니즘을 이해하고 신흥 연구 분야의 형성과 발전을 추적하는 것은 과학 정책과 자원 배분 결정에 필수적이다.
- **Approach**: 인용 네트워크에서 랜덤 워크로 생성한 학술지 흔적(periodical trail)에 Word2Vec을 적용하여 10년 단위 임베딩을 학습하고, 최근접 이웃의 변화로 의미 변화(semantic change)를 정량화한다.

## Achievement

![Figure 3](figures/fig3.webp)

*Fig. 3A presents the positions of all periodicals within the triangle for the 2010s, with*

- **시간변화 임베딩 검증**: Nature, Science, PNAS 등 다학제 저널의 학문 분야별 발행량과 유사도 간의 긍정적 상관(R²=0.526)을 확인하여 방법론 유효성 입증
- **의미 변화 정량화**: 학술지 최근접 이웃의 변화를 측정하는 메트릭(d) 개발로 PRSB의 1980년대 컴퓨터 비전 분야로의 의미 드리프트 발견
- **학제간 경관 매핑**: 물리-생명-보건 삼각형 내 학술지 위치 추적으로 대부분 학술지의 전문화 추세와 생명과학 학술지의 학제간성 증가 현상 발견
- **신흥 주제 탐지**: 학술지 클러스터 형성 모니터링으로 1980년대 AIDS 연구, 나노기술 등 신흥 연구 분야 자동 식별

## How


- 1950년대부터 각 10년 단위로 인용 네트워크 구축
- 인용 네트워크에서 랜덤 워크 수행으로 논문 인용 흔적(paper citation trail) 생성
- 논문을 발행 학술지로 매핑하여 학술지 수준의 흔적(periodical-level trail) 변환
- Word2Vec 알고리즘으로 각 10년 단위의 학술지 벡터 표현(v^t_i) 학습
- k-최근접 이웃(k-NN, k=10)의 코사인 유사도 벡터 간 거리로 의미 변화 메트릭(d) 계산
- 학술지 집단의 위치를 물리-생명-보건 삼각형 공간에 매핑하여 시간 궤적 분석
- 로컬 클러스터 형성 추적으로 신흥 주제 탐지

## Originality

- 학술지 수준에서의 첫 시간변화 임베딩 방법론으로 기존 정적 매핑의 한계 극복
- 계산언어학의 단어 의미 변화 정량화 기법을 과학지도 분야에 창의적으로 적용
- 인용 네트워크 기반 랜덤 워크를 학술지 맥락 생성에 활용하는 새로운 접근
- 다차원 분류(물리-생명-보건) 삼각형 내 동적 위치 추적으로 학제간성 변화의 시각화 제시

## Limitation & Further Study

- 분석 기간이 1950년대부터이어서 초기 학술 커뮤니케이션 역사 미포함
- 랜덤 워크 파라미터(길이, 횟수)와 Word2Vec 하이퍼파라미터 선택에 대한 민감도 분석 부재
- k=10으로 고정된 최근접 이웃 수가 다양한 규모의 학술지에 최적인지 미검증
- 신흥 주제 탐지의 자동성 평가를 위한 전문가 검증 또는 정량적 벤치마크 부재
- 학술지 내 논문 샘플링 편향(높은 인용도 논문 과대표현) 가능성 미논의
- 후속 연구: 다른 학제 분류 체계(예: CCS, MeSH) 적용, 시간 윈도우 세분화(5년 단위), 학술지 규모 별 분석, 신흥 주제 탐지 정밀성 개선

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 과학의 동적 구조 변화를 정량적으로 추적하는 혁신적인 방법론을 제시하며, 검증과 응용 사례를 통해 타당성을 입증한 견고한 연구다. 과학지도학과 과학정책 분야에 실질적 기여가 기대된다.

## Related Papers

- 🔄 다른 접근: [[papers/989_Modeling_Changing_Scientific_Concepts_with_Complex_Networks/review]] — 복잡 네트워크를 통한 과학 개념 모델링과 저널 임베딩을 통한 과학 구조 추적이라는 서로 다른 시간적 분석 접근법이다.
- 🏛 기반 연구: [[papers/1013_Rethinking_Thematic_Evolution_in_Science_Mapping_An_Integrat/review]] — 과학 매핑에서 주제 진화 추적의 통합적 접근법이 시간변화 학술지 분석의 이론적 토대를 제공한다.
- 🔗 후속 연구: [[papers/930_A_Survey_on_Knowledge_Organization_Systems_of_Research_Field/review]] — 연구 분야 지식 조직 시스템에 대한 체계적 조사가 과학 구조 진화 추적의 분류학적 기반이 된다.
- 🧪 응용 사례: [[papers/952_Design_and_Update_of_a_Classification_System_The_UCSD_Map_of/review]] — 통시적 복합 네트워크를 통한 과학 구조 변화 매핑에 UCSD 맵의 업데이트된 분류 체계가 시간적 변화 추적의 기준점을 제공한다.
- 🔗 후속 연구: [[papers/1013_Rethinking_Thematic_Evolution_in_Science_Mapping_An_Integrat/review]] — 과학 구조의 통시적 변화 분석을 통합된 네트워크 프레임워크로 확장하여 더욱 정교한 분석을 가능하게 한다.
- 🔄 다른 접근: [[papers/989_Modeling_Changing_Scientific_Concepts_with_Complex_Networks/review]] — 과학 구조의 통시적 변화를 LLM 임베딩 대신 복잡 네트워크로 분석하는 해석 가능한 대안적 접근법을 제시한다.
- 🔗 후속 연구: [[papers/1120_SciEvo_A_2_Million_30-Year_Cross-disciplinary_Dataset_for_Te/review]] — arXiv 기반 학문 진화 분석을 더 넓은 시계열에서 과학 구조의 통시적 변화 매핑으로 확장한다.
