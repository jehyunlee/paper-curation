---
title: "1018_Science_Mapping_and_Science_Maps"
authors:
  - "Eugenio Petrovich"
date: "2021"
doi: "10.5771/0943-7444-2021-7-8-535"
arxiv: ""
score: 4.0
essence: "과학 지도(Science Maps)는 학술 지식의 구조와 동역학을 시각적으로 표현하는 방법론으로, 인용 네트워크(Citation Networks)와 용어 공동 출현(Term Co-occurrence) 기반의 다양한 매핑 기법들을 체계적으로 소개한다."
tags:
  - "cat/Science_of_Science_Research"
  - "sub/Bibliometrics_and_Science_Mapping"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Petrovich_2021_Science Mapping and Science Maps.pdf"
---

# Science Mapping and Science Maps

> **저자**: Eugenio Petrovich | **날짜**: 2021 | **DOI**: [10.5771/0943-7444-2021-7-8-535](https://doi.org/10.5771/0943-7444-2021-7-8-535)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1. Example of citation network. Nodes represent document and ar-*

과학 지도(Science Maps)는 학술 지식의 구조와 동역학을 시각적으로 표현하는 방법론으로, 인용 네트워크(Citation Networks)와 용어 공동 출현(Term Co-occurrence) 기반의 다양한 매핑 기법들을 체계적으로 소개한다.

## Motivation

- **Known**: 과학 지도는 1960년대 이후 대규모 학술 데이터베이스의 등장으로 가능해졌으며, 학문 분야 간의 관계, 주요 연구자 및 기관, 시간에 따른 과학 분야의 발전을 시각화하는 데 사용되어 왔다.
- **Gap**: 기존 연구들은 수학적 형식화에 집중했으나, 개념적·이론적·방법론적 문제들에 대한 종합적 설명이 부족하며, 특히 과학 지도의 해석, 맥락화, 평가를 위한 인식론적·사회학적 논의가 체계화되지 않았다.
- **Why**: 과학 지도는 지식 조직화(Knowledge Organization)부터 과학 철학(Philosophy of Science), 과학 정책(Science Policy)에 이르기까지 메타과학의 모든 분야에 적용될 수 있으며, 과학의 구조적 변화와 신흥 분야의 출현을 이해하는 데 필수적이다.
- **Approach**: 이 논문은 과학 지도 구축의 표준 워크플로우를 제시하고, 데이터 수집·전처리에서부터 인용 기반·용어 기반·공저 네트워크 등 다양한 유형의 지도 생성, 시간 축 통합, 해석 단계까지 전체 프로세스를 상세히 설명한다.

## Achievement


- **과학 지도 역사 및 계보**: 중세의 자유 7학예(Liberal Arts) 시각화부터 현대 데이터 기반 매핑까지 과학 지도의 진화 과정을 체계적으로 추적
- **표준 워크플로우 제시**: 데이터 수집(Data Collection) → 필드 한정(Field Delineation) → 전처리(Pre-processing) → 네트워크 추출(Network Extraction) → 시각화 및 해석의 명확한 단계별 절차 제공
- **다양한 매핑 기법 분류**: 인용 기반(Citation-based), 용어 기반(Term-based), 공저(Co-authorship), 편집자 연계(Interlocking Editorship), 특허 기반, 지리적 지도(Geographic Maps) 등 6가지 유형 상세 분석
- **정규화(Normalization) 및 시각화 기법**: Graph-based와 Distance-based의 두 가지 주요 시각화 방식과 군집화(Clustering)를 통한 해석 보완 방법 설명
- **인식론적·사회학적 논의**: 과학 지도의 객관성, 출판된 과학과 과학적 실천의 관계, 인용의 의미 등 철학적 기초 제시
- **과학 정책 응용**: 학문 분야 분류, 신흥 분야 식별, 학제 간 연구 추적 등 정책 수립을 위한 구체적 활용 방안 제시

## How


- 인용 네트워크 구축: 발행물(Publications)을 노드(Nodes)로, 인용 관계를 엣지(Edges)로 표현하여 학술 연결성 파악
- 용어 공동 출현 분석: 발행물의 제목, 초록, 키워드에서 자동 추출(Natural Language Processing)한 용어 간 공동 출현 빈도로 개념적 관계 도출
- 정규화 점수 계산: Raw Relatedness Scores를 표준화하여 비교 가능한 단위로 변환
- 그래프 시각화: Force-directed algorithms 등을 이용하여 네트워크 구조를 2D/3D 평면에 배치
- 거리 기반 시각화: 관계의 강도를 거리로 인코딩하여 시각적 표현
- 군집화 기법: 높은 차수의 클러스터가 낮은 차수의 클러스터를 포함하는 계층적 구조 형성
- 시간 축 통합: 정적 스냅샷(Static Snapshots)이나 동적 추적(Dynamic Tracking)으로 시간에 따른 과학 분야의 진화 표현

## Originality

- 과학 지도 방법론의 **종합적·체계적 검토**: 산재된 문헌들을 일관된 프레임워크로 통합하여 체계적 이해 제공
- 개념적 명확성 강조: 수학적 형식화보다 이론적·방법론적 근거에 집중하여 접근성 향상
- **다학제적 관점 통합**: 서지학, 과학사회학, 과학철학, 지식조직화 등 여러 분야의 관점을 연결
- 인식론적 기초 제시: 과학 지도의 객관성, 신뢰성, 해석의 한계에 대한 철학적 논의 개시
- 실무적 가이드 제공: CiteSpace, VOSviewer 등 기존 도구에 대한 리뷰로 실제 적용 가능성 강화

## Limitation & Further Study

- 수학적 형식화의 부재: 기술적 깊이가 제한되어 고급 사용자들을 위한 수학적 설명 필요
- 구체적 사례 분석 부족: 이론 중심으로 실제 과학 지도 사례의 분석이 제한적
- 특정 도구에 대한 상세 가이드 미흡: 부록에서 두 가지 도구만 다루어 다른 매핑 소프트웨어 활용 방안 부재
- 후속연구 방향: **인문학 분야의 적용 가능성 탐색** - 자연과학 데이터 중심의 방법론을 인문학 문헌에 적용할 때의 한계와 개선 방안 연구 필요
- 후속연구 방향: **머신러닝 기반 자동화** - NLP 기술의 발전에 따른 더욱 정교한 용어 추출 및 관계 식별 방법 개발
- 후속연구 방향: **대규모 다중 모달 매핑** - 텍스트, 이미지, 데이터셋 등 다양한 형태의 학술 결과물을 통합한 지도 생성 기법 연구

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 논문은 과학 지도 방법론에 대한 포괄적이고 체계적인 입문서로서, 산재된 기술과 개념들을 명확한 워크플로우로 통합하고 인식론적·사회학적 기초를 제시함으로써 지식조직화와 과학 정책 분야에서의 활용성을 크게 높인다. 다만 수학적 형식화 부재와 실제 사례 분석의 부족은 고급 실무자들을 위한 보충 자료의 필요성을 시사한다.

## Related Papers

- 🧪 응용 사례: [[papers/1024_Software_survey_VOSviewer_a_computer_program_for_bibliometri/review]] — VOSviewer와 같은 구체적인 소프트웨어 도구를 통해 과학 지도 작성의 실용적 구현 방법을 제공한다.
- 🔗 후속 연구: [[papers/949_Comparative_science_mapping_a_novel_conceptual_structure_ana/review]] — 비교 과학 지도화 개념을 통해 기존 과학 매핑 방법론을 확장하여 더 정교한 분석이 가능하다.
- 🧪 응용 사례: [[papers/949_Comparative_science_mapping_a_novel_conceptual_structure_ana/review]] — 새로운 개념 구조 분석을 과학 매핑과 과학 지도의 혁신적 시각화 방법으로 적용한다.
- 🏛 기반 연구: [[papers/969_Hierarchical_Classification_of_Research_Fields_in_the_Web_of/review]] — 과학 매핑의 이론적 기초와 실제 구현 방법론을 이해하는 데 필수적인 배경 지식을 제공한다.
- 🏛 기반 연구: [[papers/1013_Rethinking_Thematic_Evolution_in_Science_Mapping_An_Integrat/review]] — 과학 지도 작성의 기본 개념과 방법론적 기반을 제공하여 주제 진화 분석의 이론적 토대가 된다.
- 🏛 기반 연구: [[papers/1024_Software_survey_VOSviewer_a_computer_program_for_bibliometri/review]] — 과학 매핑과 과학 지도의 이론적 배경과 다양한 시각화 접근법을 제공한다.
- 🏛 기반 연구: [[papers/944_Co-Citation_Analysis_Bibliographic_Coupling_and_Direct_Citat/review]] — 공인용분석과 서지결합의 비교 평가가 과학 매핑의 다양한 접근법 이해의 기반이 된다.
