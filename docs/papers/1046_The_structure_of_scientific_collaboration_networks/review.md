---
title: "1046_The_structure_of_scientific_collaboration_networks"
authors:
  - "M. E. J. Newman"
date: "2001"
doi: "10.1073/pnas.98.2.404"
arxiv: ""
score: 4.0
essence: "과학자들의 공저 관계로 구성된 협력 네트워크의 구조를 분석하여 과학 커뮤니티가 '작은 세상(small world)' 특성을 가짐을 보였다."
tags:
  - "cat/Bibliometric_Network_Analysis"
  - "sub/Network_Structure_and_Detection"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Newman_2001_The structure of scientific collaboration networks.pdf"
---

# The structure of scientific collaboration networks

> **저자**: M. E. J. Newman | **날짜**: 2001 | **DOI**: [10.1073/pnas.98.2.404](https://doi.org/10.1073/pnas.98.2.404)

---

## Essence


과학자들의 공저 관계로 구성된 협력 네트워크의 구조를 분석하여 과학 커뮤니티가 '작은 세상(small world)' 특성을 가짐을 보였다.

## Motivation

- **Known**: 소셜 네트워크는 50년 이상 연구되었으며, Milgram의 '6단계 분리' 실험이 작은 세상 가설을 뒷받침했다. 그러나 대규모 실제 인간관계 네트워크의 상세한 구조에 대한 연구는 부족했다.
- **Gap**: 이전 소셜 네트워크 연구는 소규모 설문조사(수백 명 규모)이거나 인공적 네트워크(전력망, 인터넷)를 사용했으며, 실제 인간관계를 정확히 측정할 수 없었다.
- **Why**: 네트워크 구조는 정보 전파와 질병 확산에 중요한 영향을 미치므로, 대규모 실제 협력 네트워크의 구조적 특성을 파악하는 것이 중요하다.
- **Approach**: MEDLINE, Los Alamos e-Print Archive, SPIRES, NCSTRL 등 4개 데이터베이스에서 1995-1999년 논문 데이터를 수집하여, 공저 관계를 기반으로 명시적 협력 네트워크 그래프를 구축했다.

## Achievement


- **작은 세상 특성 입증**: 무작위로 선택한 과학자 쌍이 짧은 중간 인물 경로로 연결됨을 확인했다.
- **협력자 수 분포**: 저자별 평균 협력자 수는 분야별로 다르게 나타났다 (MEDLINE 14.8명, NCSTRL 3.59명).
- **클러스터링 분석**: 네트워크에 클러스터링이 존재하여 삼각형 구조가 형성됨을 보였다.
- **분야별 협력 패턴 차이**: 생의학, 물리학, 컴퓨터과학 간 협력 구조와 강도의 현저한 차이를 규명했다.
- **대규모 네트워크 분석**: 100만 명 이상의 과학자를 포함한 거대 협력 네트워크 특성을 최초로 상세히 분석했다.

## How


- 4개 주요 과학 데이터베이스(MEDLINE, Los Alamos Archive, SPIRES, NCSTRL)에서 5년간(1995-1999) 논문 메타데이터 수집
- 저자 이름 정규화: 전체 초성 사용 분석과 첫 글자만 사용한 분석으로 상한/하한 경계값 설정
- 그래프 이론 적용: 정점(scientist)과 간선(co-authorship)으로 협력 네트워크 구축
- 네트워크 특성 지표 계산: 평균 경로 길이, 차수 분포, 클러스터링 계수 등 측정
- 거대 연결 성분(giant component) 분석 및 분야별 비교
- Erdős number 개념 활용하여 논문 기반 협력 거리 정량화

## Originality

- 과학 협력 네트워크를 소셜 네트워크 연구의 대상으로 처음 체계적으로 제시
- 100만 명 규모의 대규모 실제 인간관계 네트워크를 정확한 정의(공저)로 분석한 최초 시도
- 저자 이름 정규화의 불확실성을 정량적으로 다루는 상한/하한 바운드 방법론 도입
- 여러 학문 분야(생의학, 물리, 컴퓨터과학)의 협력 패턴을 최초로 비교 분석

## Limitation & Further Study

- 저자 이름의 중복 및 표기 방식 차이로 인한 불확실성 존재 (상한/하한 경계값으로 제시)
- 5년 윈도우만 분석하여 장기적 네트워크 진화를 반영하지 못함
- 일부 데이터베이스는 미검증 프리프린트 포함으로 인한 품질 편향 가능성
- 논문 공저만 협력의 정의로 사용하여 비공식 협력이나 감정적 관계를 미처 포함하지 못함
- 후속 연구: 시간 경과에 따른 네트워크 동적 변화, 협력 강도 가중치 적용, 국제 협력 vs 국내 협력 비교, 학문분야 간 협력 연결성 분석 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 과학 협력 네트워크를 최초로 대규모 실제 데이터로 분석하여 작은 세상 가설을 입증하고, 학문 분야별 협력 구조의 차이를 규명한 획기적 연구다. 명확한 정의와 견고한 방법론으로 사회 네트워크 연구의 새로운 방향을 제시했다.

## Related Papers

- 🔗 후속 연구: [[papers/960_Evolution_of_the_social_network_of_scientific_collaborations/review]] — 과학 협력 네트워크의 정적 구조 분석을 시간적 진화 패턴 분석으로 확장한다.
- 🧪 응용 사례: [[papers/1034_The_Increasing_Dominance_of_Teams_in_Production_of_Knowledge/review]] — 개별 과학자 협력 네트워크 분석을 팀 기반 지식 생산의 증가 현상 이해에 적용한다.
- 🔗 후속 연구: [[papers/979_Large_teams_develop_and_small_teams_disrupt_science_and_tech/review]] — 협력 네트워크의 소규모 세계 특성을 팀 크기가 과학적 발견과 혁신에 미치는 차별적 영향으로 확장한다.
- 🧪 응용 사례: [[papers/965_Gender-diverse_teams_produce_more_novel_and_higher-impact_sc/review]] — 과학 협력 네트워크 구조 분석을 성별 다양성이 팀 성과에 미치는 영향 연구에 적용한다.
- 🧪 응용 사례: [[papers/957_Emergence_of_Scaling_in_Random_Networks/review]] — 과학자 협력 네트워크가 실제로 스케일-프리 특성을 보이는지 실증적으로 검증한 연구이다.
- 🧪 응용 사례: [[papers/947_Collective_dynamics_of_small-world_networks/review]] — 소규모 세계 네트워크 이론을 실제 과학자 협력 네트워크에 적용하여 과학 커뮤니티의 구조적 특성을 규명한다.
- 🔄 다른 접근: [[papers/990_Networks_of_Scientific_Papers/review]] — 논문 인용 네트워크와 다른 관점에서 과학자 협력 네트워크의 구조적 특성을 분석한다.
