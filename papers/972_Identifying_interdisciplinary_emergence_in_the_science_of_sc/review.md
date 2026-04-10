---
title: "972_Identifying_interdisciplinary_emergence_in_the_science_of_sc"
authors:
  - "Keungoui Kim"
  - "Dieter F. Kogler"
  - "Sira Maliphol"
date: "2024.05"
doi: "10.1057/s41599-024-03044-y"
arxiv: ""
score: 4.0
essence: "본 연구는 BERTopic 임베딩 토픽 모델링과 네트워크 분석을 결합하여 과학 출판 메타데이터에서 학제간 지식 결합을 통한 신흥 과학 분야의 출현을 식별하는 방법론을 제시한다."
tags:
  - "cat/Bibliometric_Network_Analysis"
  - "sub/Scientific_Mapping_and_Visualization"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Kim et al._2024_Identifying interdisciplinary emergence in the science of science combination of network analysis a.pdf"
---

# Identifying interdisciplinary emergence in the science of science: combination of network analysis and BERTopic

> **저자**: Keungoui Kim, Dieter F. Kogler, Sira Maliphol | **날짜**: 2024-05-10 | **DOI**: [10.1057/s41599-024-03044-y](https://doi.org/10.1057/s41599-024-03044-y)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1 Overall research process. The overall research process is performed*

본 연구는 BERTopic 임베딩 토픽 모델링과 네트워크 분석을 결합하여 과학 출판 메타데이터에서 학제간 지식 결합을 통한 신흥 과학 분야의 출현을 식별하는 방법론을 제시한다.

## Motivation

- **Known**: 과학 출판량이 지수적으로 증가하고 있으며, 학제간 연구가 혁신과 글로벌 과제 해결의 핵심이다. 기존 연구는 인용 분석과 네트워크 분석을 통해 과학 emergence를 연구해왔다.
- **Gap**: 신흥 과학 분야의 출현을 정확히 예측하기 어렵고, 특히 학제간 지식 결합 과정에 대한 체계적인 연구가 부족하다. 기술 수렴(technology convergence)에 비해 학제간 지식 재조합 과정에 대한 연구는 미흡하다.
- **Why**: 과학적 생산성 저하와 혁신 속도 둔화 문제를 해결하기 위해 신흥 학제간 분야를 조기에 식별하고, 이를 바탕으로 과학기술혁신(STI) 정책 수립과 미래 혁신 궤도 예측이 필요하다.
- **Approach**: Web of Science 데이터베이스에서 추출한 메타데이터로부터 과학 범주 공동출현 네트워크를 구성하고, BERTopic을 활용한 임베딩 토픽 모델링으로 학제간 분류를 수행하며, 시계열 비교를 통해 영향력 변화 패턴을 분석한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2 Science category-subject co-occurrence network. The Science*

- **학제간 emergence 식별 프레임워크 개발**: 네트워크 중심성 지수(network centrality index)를 활용한 신규 emergence 측정 지표 개발
- **BERTopic 적용**: 자연언어처리(NLP) 기반의 임베딩 토픽 모델링 기법을 과학 emergence 연구에 최초로 적용하여 비지도 학습 방식의 학제간 분류 실현
- **시계열 분석**: 시간 경과에 따른 학제간 영향력 변화 패턴 파악으로 동적 emergence 추적
- **정성적 검증**: 출현한 학제간 분야의 근원을 파악하고 글로벌 학제간 영역 병합을 통한 미래 수렴 활동 예측 가능성 제시

## How

![Figure 4](figures/fig4.webp)

*Fig. 4 Process of BERTopic modeling. The process of BERTopic modeling*

- Web of Science Core Collection 데이터베이스에서 연구 출판 메타데이터 수집 및 데이터셋 구성
- 과학 범주(science category) 기반 공동출현 네트워크(co-occurrence network) 생성으로 글로벌 과학 지도(science map) 구축
- 복수의 과학 범주를 포함하는 연구를 학제간 분야로 정의하고 시계열 비교를 통해 학제간성(interdisciplinarity) 관점에서 영향력 변화 패턴 추적
- BERTopic (Bidirectional Encoder Representations from Transformers) 임베딩 토픽 모델링을 활용한 비지도 학습 기반 학제간 분류
- 네트워크 중심성 지수를 기반으로 신흥 주제에 대한 정량적 측정 수행 및 정성적 검증

## Originality

- **방법론 결합의 참신성**: 임베딩 토픽 모델링(BERTopic)과 공동출현 네트워크 분석을 결합한 통합 접근법이 신흥 과학 식별에 최초로 적용됨
- **학제간 지식 재조합 포커스**: 기술 수렴에 대한 기존 연구와 달리, 학제간 지식 재조합 과정의 과학적 emergence를 체계적으로 추적하는 관점 제시
- **글로벌 스케일의 분석**: Web of Science 전체 데이터를 기반으로 한 글로벌 과학 지도 분석으로 영역 경계를 넘는 emergence 패턴 포착
- **신규 정량 지표**: 네트워크 중심성 지수 기반의 새로운 emergence 측정 지표 개발

## Limitation & Further Study

- Web of Science 메타데이터에 포함된 공식 과학 범주 분류에 의존하므로 신흥 분야가 기존 분류 체계에 미처 반영되지 않을 수 있음
- BERTopic의 토픽 수(topic number) 결정이 주관적일 수 있으며, 초기 파라미터 설정에 따라 결과가 민감하게 변동할 가능성
- 정성적 검증이 제한적일 수 있으므로 전문가 패널을 통한 더욱 체계적인 검증 필요
- **후속 연구**: 다양한 출판 데이터베이스(Scopus, 특허 데이터 등) 통합, 시간 가중치를 고려한 동적 모델링, 국가/기관별 학제간 emergence 차이 분석, 실제 혁신 성과와의 인과관계 추적

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 BERTopic과 네트워크 분석을 결합하여 학제간 지식 재조합을 통한 과학의 emergence를 식별하는 참신한 방법론을 제시하며, 과학정책 수립과 미래 혁신 예측에 실질적 가치를 제공한다.

## Related Papers

- 🧪 응용 사례: [[papers/936_Atypical_Combinations_and_Scientific_Impact/review]] — BERTopic 모델링으로 식별된 학제간 결합이 실제로 비전형적 조합을 통한 과학적 임팩트로 이어지는지 검증할 수 있다.
- 🔗 후속 연구: [[papers/975_Interdisciplinary_papers_supported_by_disciplinary_grants_ga/review]] — 학제간 연구가 단일 분야 펀딩으로도 높은 성과를 낼 수 있다는 발견과 학제간 출현 탐지 연구가 상호 보완적이다.
- 🏛 기반 연구: [[papers/1013_Rethinking_Thematic_Evolution_in_Science_Mapping_An_Integrat/review]] — 주제 진화를 추적하는 통합적 접근법이 학제간 출현 탐지의 방법론적 토대를 제공한다.
- 🧪 응용 사례: [[papers/975_Interdisciplinary_papers_supported_by_disciplinary_grants_ga/review]] — 과학의 과학 분야에서 학제간 출현을 식별하는 연구와 연결되어 그랜트 지원 방식이 학제간 연구의 질적 성과에 미치는 영향을 분석한다.
- 🔗 후속 연구: [[papers/936_Atypical_Combinations_and_Scientific_Impact/review]] — 학제간 융합의 출현을 식별하는 연구에 비전형적 조합 분석을 적용하여 혁신적 융합 연구를 예측할 수 있다.
- 🧪 응용 사례: [[papers/1110_A_cross-disciplinary_research_framework_at_institution_level/review]] — 과학의 과학 분야에서 학제간 출현을 식별하는 방법론을 IFISC의 학제간 연구 프레임워크 설계에 활용할 수 있다.
