---
title: "1053_Visualizing_the_context_of_citations_referencing_papers_publ"
authors:
  - "Lutz Bornmann"
  - "Robin Haunschild"
  - "Sven E. Hug"
date: "2018.02"
doi: "10.1007/s11192-017-2591-8"
arxiv: ""
score: 4.0
essence: "Eugene Garfield의 논문들을 인용한 문헌들의 인용 맥락(citation context)을 이용하여 키워드 동시출현 네트워크(keyword co-occurrence network)를 구성하는 새로운 유형의 계량분석 방법론을 제시하고, 이를 제목/초록 기반 네트워크와 비교 분석한다."
tags:
  - "cat/Bibliometric_Network_Analysis"
  - "sub/Scientific_Mapping_and_Visualization"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Bornmann et al._2018_Visualizing the context of citations referencing papers published by Eugene Garfield a new type of.pdf"
---

# Visualizing the context of citations referencing papers published by Eugene Garfield: a new type of keyword co-occurrence analysis

> **저자**: Lutz Bornmann, Robin Haunschild, Sven E. Hug | **날짜**: 2018-02-01 | **DOI**: [10.1007/s11192-017-2591-8](https://doi.org/10.1007/s11192-017-2591-8)

---

## Essence

![Figure 3](figures/fig3.webp)

*Fig. 3 Co-occurrence of keywords in citation contexts of papers referencing Eugene Garﬁeld*

Eugene Garfield의 논문들을 인용한 문헌들의 인용 맥락(citation context)을 이용하여 키워드 동시출현 네트워크(keyword co-occurrence network)를 구성하는 새로운 유형의 계량분석 방법론을 제시하고, 이를 제목/초록 기반 네트워크와 비교 분석한다.

## Motivation

- **Known**: 기존의 키워드 동시출현 네트워크는 주로 논문의 제목, 초록, 저자 키워드로부터 추출되었다. 인용 맥락(citation context)은 특정 인용 주변의 단어들로 정의되며, 최근 큰 학술 데이터의 등장으로 인용 맥락 분석이 활성화되고 있다.
- **Gap**: 선행 연구들은 인용 맥락을 분류하거나 분석하였으나, 인용 맥락을 키워드 동시출현 네트워크 구성의 데이터 소스로 사용한 연구는 없었다. 인용 맥락 데이터 추출의 어려움으로 인해 대규모 분석이 제한적이었다.
- **Why**: 인용이 인용된 문헌의 인지적 영향력을 반영한다는 가정 하에서 인용 맥락 분석은 연구평가에 중요하며, 새로운 네트워크 분석 유형은 인용의 의미적 관계를 더 정확하게 파악할 수 있게 한다.
- **Approach**: Microsoft Academic 데이터베이스에서 제공하는 미리 분할된 인용 맥락 데이터를 활용하여 세 가지 키워드 동시출현 네트워크를 구성한다: (1) Garfield 논문의 제목/초록 기반, (2) 인용 논문들의 제목/초록 기반, (3) 인용 맥락 기반.

## Achievement


- **새로운 네트워크 유형 제시**: 인용 맥락을 기반으로 하는 키워드 동시출현 네트워크라는 새로운 계량분석 방법론을 도입
- **의미적 관련성 확인**: Garfield 논문과 인용 맥락 네트워크가 인용 논문들의 제목/초록 네트워크보다 의미적으로 더 밀접한 관련이 있음을 실증적으로 입증
- **대규모 자동화 분석 가능**: Microsoft Academic의 분할된 인용 맥락 데이터 활용으로 대규모 자동화 분석이 가능함을 시연
- **인용 평가론 지지**: 인용이 인용된 문헌의 인지적 영향을 반영한다는 이론적 가정을 계량적으로 검증

## How


- Microsoft Academic API를 통해 Garfield의 1558개 논문 중 MA에 수록된 327개 논문 검색
- 이들을 인용한 343개 논문과 428개의 인용 맥락 추출
- VOSviewer 소프트웨어의 텍스트 마이닝 기능을 사용하여 세 가지 키워드 동시출현 네트워크 생성
- 동일한 설정 적용: 이진 카운팅(binary counting), 최소 4회 이상 출현 키워드, 상위 60% 관련성 키워드 포함
- 생성된 네트워크의 클러스터 해석가능성을 기반으로 클러스터 수 결정 및 수동 제외

## Originality

- 인용 맥락을 키워드 동시출현 네트워크 구성의 데이터 원천으로 최초 활용
- 빅데이터 환경에서 자동화된 인용 맥락 추출을 통한 대규모 분석 방법론 제시
- 세 가지 다른 소스(피인용 논문 제목/초록, 인용 논문 제목/초록, 인용 맥락)의 네트워크를 비교 분석하는 검증 프레임워크 구성

## Limitation & Further Study

- Microsoft Academic의 초기 단계 발전 상태로 인해 Garfield의 1558개 논문 중 327개(21%)만 수록됨
- 인용 맥락이 이용 가능한 논문이 59개에 불과하여 샘플 크기 제한
- 제목, 초록, 인용 맥락에서 추출된 키워드의 수동 제외 과정으로 인한 주관성
- 단일 학자(Garfield)를 사례로 한정하여 일반화 가능성 미확인 → 향후 다양한 학자/분야에 대한 검증 필요
- 인용 맥락의 길이와 맥락 품질에 따른 결과 차이 분석 부재 → 추가 연구 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 인용 맥락을 활용한 새로운 유형의 계량분석 방법론을 제시하고, 대규모 자동화 분석이 가능함을 보여주었으나, 샘플 크기 제한과 일반화 검증이 필요하다. 계량분석 분야에 개념적 기여는 높으나 실증적 범위는 제한적이다.

## Related Papers

- 🏛 기반 연구: [[papers/1051_Unsupervised_Word_Embeddings_Capture_Latent_Knowledge_from_M/review]] — 인용 맥락에서 키워드를 추출하는 비지도 워드 임베딩의 방법론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/944_Co-Citation_Analysis_Bibliographic_Coupling_and_Direct_Citat/review]] — 전통적인 공인용분석과 서지결합을 인용 맥락 기반 네트워크 분석으로 확장한다.
- 🧪 응용 사례: [[papers/1054_Whats_In_Your_Field_Mapping_Scientific_Research_with_Knowled/review]] — 인용 맥락 기반 키워드 매핑을 연구 분야의 지식 지도 작성에 적용한다.
- 🔗 후속 연구: [[papers/943_Citation_Analysis_as_a_Tool_in_Journal_Evaluation/review]] — 저널 평가에서 단순 인용 분석을 인용 맥락의 질적 분석으로 확장한다.
- 🔗 후속 연구: [[papers/1024_Software_survey_VOSviewer_a_computer_program_for_bibliometri/review]] — 전통적 서지학적 지도를 인용 맥락 기반 키워드 네트워크 시각화로 확장한다.
- 🧪 응용 사례: [[papers/944_Co-Citation_Analysis_Bibliographic_Coupling_and_Direct_Citat/review]] — 논문 발표 후 인용 맥락을 시각화하여 직접 인용과 공인용 분석의 실제적 차이를 구체적으로 보여준다.
