---
title: "978_Introducing_the_open_biomedical_map_of_science"
authors:
  - "Michael Ginda"
  - "Bruce W. Herr"
  - "Katy Börner"
date: "2023.10"
doi: "10.3389/frma.2023.1274793"
arxiv: ""
score: 4.0
essence: "PubMed 인용 데이터베이스를 활용하여 개방형 생의학 과학 지도(OBMS)를 개발하는 진행 중인 연구로, 저널과 MeSH 기술어(Medical Subject Heading) 간의 이중양식 네트워크 관계를 시각화한다."
tags:
  - "cat/Scientific_Information_Systems"
  - "sub/Knowledge_Graphs_and_Semantic_Mapping"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ginda et al._2023_Introducing the open biomedical map of science.pdf"
---

# Introducing the open biomedical map of science

> **저자**: Michael Ginda, Bruce W. Herr, Katy Börner | **날짜**: 2023-10-4 | **DOI**: [10.3389/frma.2023.1274793](https://doi.org/10.3389/frma.2023.1274793)

---

## Essence


PubMed 인용 데이터베이스를 활용하여 개방형 생의학 과학 지도(OBMS)를 개발하는 진행 중인 연구로, 저널과 MeSH 기술어(Medical Subject Heading) 간의 이중양식 네트워크 관계를 시각화한다.

## Motivation

- **Known**: 기존 과학 지도들은 상용 데이터베이스에 의존하여 재현 불가능하고 폐쇄적이다. PubMed는 개방형 인용 데이터베이스로 MeSH 제어 어휘를 사용하여 생의학 분야의 문헌을 체계적으로 색인한다.
- **Gap**: FAIR 원칙(검색 가능성, 접근성, 상호운용성, 재사용성)을 충족하는 개방형 과학 지도가 현재 부재하며, PubMed 데이터를 활용한 종합적 생의학 과학 지도의 체계적 개발이 필요하다.
- **Why**: 개방형 과학 지도는 투명성과 재현 가능성을 제공하며 연구자들이 자유롭게 접근하고 수정할 수 있어 생의학 분야의 연구 동향 파악 및 학제 간 관계 분석에 중요하다.
- **Approach**: PubMed의 2009-2019년 저널 및 MeSH 기술어 데이터를 수집하여 UCSD 과학 지도와 비교 검증하고, 이중양식 네트워크를 구성한 후 ZMLT 알고리즘으로 시각화한다.

## Achievement


- **데이터 기반 저널 포함 기준 설정**: 10년간 최소 20개 이상의 논문을 색인한 8,209개 저널을 OBMS에 포함하기 위한 임계값 결정
- **학제 커버리지 분석**: PubMed의 18,234개 저널 중 34.6%(6,307개)가 UCSD 지도와 겹치며, 의학·보건 및 사회과학에 강한 커버리지 확인
- **이중양식 네트워크 구성**: 8,209개 저널 노드와 6,824개 MeSH 기술어 노드로 이루어진 14,982개 노드와 14,981개 간선의 프로토타입 네트워크 개발
- **대화형 시각화 도구 개발**: ZMLT 알고리즘과 map4sci 소프트웨어를 통해 검색 가능한 대규모 네트워크 그래프의 지도식 시각화 구현

## How


- PubMed 데이터베이스를 2022년 8월 16일 기준으로 쿼리하여 2009-2019년 기간의 저널, MeSH 기술어, 이중양식 간선 목록 추출
- Sci2 Tool을 사용하여 PubMed 저널 제목을 UCSD 2011 과학 지도와 매핑하고 577개 저널 제목에 대해 수동 검증
- 저널별 색인 논문 빈도 분포를 히스토그램으로 시각화하여 최소 포함 기준(20개 논문) 결정
- 이중양식 네트워크에서 각 저널당 상위 50개 MeSH 기술어만 필터링하여 프로토타입 구성
- MST Pathfinder Network Scaling 알고리즘으로 네트워크 백본 추출하여 가장 중요한 간선 식별
- ZMLT 레이아웃 알고리즘 적용으로 대규모 네트워크 그래프의 지도식 시각화 생성

## Originality

- 완전 개방형 데이터(PubMed, MeSH)만을 사용하여 FAIR 원칙을 준수하는 과학 지도 개발 시도의 선도적 사례
- 저널-기술어 이중양식 네트워크로 기존 단일양식(저널-저널, 논문-논문) 접근과 차별화된 과학 구조 표현
- MeSH 계층 구조의 다분야 커버리지를 활용하여 생의학을 넘어 인접 학문 영역 포괄
- 체계적인 임계값 분석(최소 20개 논문)을 통해 과학 지도 포함 기준의 정량적 근거 제시

## Limitation & Further Study

- PubMed의 편향된 커버리지: 인문학(2.1%), 생명공학(2.5%), 지구과학(2.7%)에 약한 학제 표현으로 종합적 과학 지도와 제한적
- 시간 범위 제한: 2009-2019년 분석 기간과 최종 2013-2022년 커버리지 간 불일치로 시간 전후 비교 분석의 일관성 부재
- 프로토타입 수준: 각 저널당 상위 50개 MeSH 기술어만 필터링하여 낮은 빈도 주제의 손실 가능성 및 전체 네트워크 구조 왜곡
- 검증 부족: UCSD 지도와의 비교는 수행하였으나 독립적 검증이나 사용자 만족도 평가 미흡
- **후속 연구**: 추가 학제 커버리지 확보, 시간 범위 통일, MeSH 필터링 기준 최적화, 대규모 사용자 연구를 통한 실용성 평가 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 연구는 완전 개방형 데이터와 개방 표준만으로 FAIR 원칙을 준수하는 과학 지도 개발의 가능성을 제시하며, 저널-기술어 이중양식 네트워크라는 혁신적 접근으로 과학 구조를 새롭게 표현한다. 다만 PubMed의 학제 편향성과 프로토타입 수준의 한계를 극복하기 위한 추가 개선과 검증이 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/1109_A_comprehensive_large-scale_biomedical_knowledge_graph_for_A/review]] — PubMed 기반의 생의학 과학 지도를 AI 기반 drug discovery를 위한 포괄적 지식그래프로 확장 발전시킨다.
- 🏛 기반 연구: [[papers/969_Hierarchical_Classification_of_Research_Fields_in_the_Web_of/review]] — Web of Science의 연구 분야 계층적 분류 체계를 제공하여 생의학 과학 지도의 분류학적 기반이 된다.
- 🧪 응용 사례: [[papers/973_Impacts_of_inter-institutional_mobility_on_scientific_perfor/review]] — 학술-산업 이동 연구를 생의학 지식 지도를 통해 특정 분야별 이동 패턴과 성과 차이 분석 가능
- 🧪 응용 사례: [[papers/985_Mapping_scientific_communities_at_scale/review]] — 생의학 과학 지도 구축 경험이 대규모 과학 공동체 매핑 방법론의 특정 도메인 적용 사례가 된다.
- 🧪 응용 사례: [[papers/944_Co-Citation_Analysis_Bibliographic_Coupling_and_Direct_Citat/review]] — 생의학 분야의 서지학적 결합 분석을 생의학 과학 지도의 개방형 구축에 적용한다.
