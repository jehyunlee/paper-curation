---
title: "960_Evolution_of_the_social_network_of_scientific_collaborations"
authors:
  - "A.L Barabási"
  - "H Jeong"
  - "Z Néda"
  - "E Ravasz"
  - "A Schubert"
date: "2002"
doi: "10.1016/s0378-4371(02"
arxiv: ""
score: 4.5
essence: "과학자들의 공동저자 네트워크를 1991-98년 수학 및 신경과학 데이터베이스를 통해 분석하여, 스케일-프리 네트워크 특성과 우선적 부착(preferential attachment)이 네트워크 진화를 지배함을 규명했다."
tags:
  - "cat/Scientific_Information_Systems"
  - "sub/Scientific_Collaboration_Networks"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Barabási et al._2002_Evolution of the social network of scientific collaborations.pdf"
---

# Evolution of the social network of scientific collaborations

> **저자**: A.L Barabási, H Jeong, Z Néda, E Ravasz, A Schubert, T Vicsek | **날짜**: 2002 | **DOI**: [10.1016/s0378-4371(02)00736-7](https://doi.org/10.1016/s0378-4371(02)00736-7)

---

## Essence


과학자들의 공동저자 네트워크를 1991-98년 수학 및 신경과학 데이터베이스를 통해 분석하여, 스케일-프리 네트워크 특성과 우선적 부착(preferential attachment)이 네트워크 진화를 지배함을 규명했다.

## Motivation

- **Known**: 소셜 네트워크는 작은 세상(small world) 특성, 높은 클러스터링 계수, 멱법칙(power-law) 차수 분포를 가지며, Newman의 선행 연구에서 공동저자 네트워크가 이러한 특성을 갖는 것이 보고되었다.
- **Gap**: 기존 연구는 네트워크의 정적 위상 특성에 집중한 반면, 시간에 따른 동적 진화 메커니즘과 노드 및 링크 추가 과정이 위상 결정에 미치는 영향이 체계적으로 분석되지 않았다.
- **Why**: 공동저자 네트워크는 가장 광범위한 공개 소셜 네트워크 데이터베이스로서 복잡한 동적 네트워크의 진화 법칙을 이해하는 데 중요하며, 그 발견은 웹(WWW), 인터넷, 기타 사회 네트워크 등 다양한 복잡 시스템 분석에 적용될 수 있다.
- **Approach**: 실증적 측정을 통해 네트워크 진화 메커니즘을 규명한 후, 이를 바탕으로 시간 진화를 포착하는 수학 모델을 제안하고, 해석적 풀이와 수치 시뮬레이션을 결합하여 검증했다.

## Achievement


- **스케일-프리 네트워크 특성 확인**: 공동저자 네트워크가 멱법칙 차수 분포를 따르는 스케일-프리 네트워크임을 실증적으로 규명
- **우선적 부착 메커니즘 규명**: 기존 저자와 신규 저자 간 링크(외부 링크) 및 기존 저자 간 협력(내부 링크) 모두 우선적 부착에 의해 지배됨을 발견
- **예상치 못한 동적 특성**: 평균 차수가 시간에 따라 증가하고 노드 간 거리가 감소하는 현상을 발견 (모델 예측과 상이)
- **이중 스케일링 거동**: 제안된 모델이 측정 데이터와 일치하는 이중 영역 스케일링(two-regime scaling)을 예측
- **내부 링크의 중요성**: 수치 시뮬레이션 및 해석 결과가 내부 링크가 스케일링 거동과 네트워크 위상 결정에 핵심 역할을 함을 입증

## How


- 1991-98년 수학(70,975명 저자, 70,901편) 및 신경과학(209,293명 저자, 210,750편) 논문 데이터베이스 구성 및 분석
- 네트워크 위상학적 척도(degree distribution, clustering coefficient, average separation) 시간 진화 측정
- 우선적 부착 확률과 내부/외부 링크 추가율 파라미터 경험적 결정
- 연속체 이론(continuum theory)을 이용한 모델의 해석적 풀이로 스케일링 지수 도출
- 몬테카를로 수치 시뮬레이션으로 해석 이론 검증 및 추가 물리량 예측
- 두 분야 간 발행 패턴 차이(수학: 단독 연구 중심, 신경과학: 협력 집약적) 비교 분석

## Originality

- 공동저자 네트워크를 **동적 진화 관점**에서 최초로 체계적으로 분석하여, 정적 위상 특성만 다룬 선행 연구와 차별화
- **우선적 부착** 메커니즘이 내부 및 외부 링크 모두에 작용함을 규명한 것이 혁신적
- 실증 측정, 해석적 모델링, 수치 시뮬레이션을 **삼중 접근법**으로 통합하여 현상 설명
- 네트워크 진화 과정에서 시간 정보를 활용한 데이터 기반 분석은 당시 매우 새로운 방법론
- 발견된 현상(평균 차수 증가, 노드 거리 감소)이 모델 예측과 불일치하는 부분을 규명하고 내부 링크로 설명한 점이 독창적

## Limitation & Further Study

- 데이터 범위의 제한: 1991-98년 8년간 제한된 기간만 분석 가능하여 장기 네트워크 진화 패턴 파악 부족
- 학문 분야 제한: 계산 자원의 제약으로 물리학 및 생물학 같은 대규모 분야 미포함, 일반성 검증 필요
- 모델의 단순화: 제안된 모델이 저자 탈퇴, 공동저자 관계 단절 등 감소 과정 미포함
- 방법론상 이슈: 한정된 과거 데이터로 인한 초기 조건 불확실성 명확히 해결되지 않음
- **후속 연구 방향**: (1) 더 장기간의 데이터 수집으로 동적 메커니즘 변화 추적, (2) 다양한 학문 분야 확대로 발견의 보편성 검증, (3) 저자 네트워크 진입/퇴출 및 협력 단절 모델링 개선, (4) WWW, 인터넷 등 타 복잡 네트워크 적용 연구

## Evaluation

- Novelty: 5/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4.5/5

**총평**: 본 논문은 공동저자 네트워크의 동적 진화를 최초로 체계적으로 분석하여 우선적 부착과 스케일-프리 특성을 규명한 획기적 연구이며, 복잡 네트워크 이론의 발전과 다양한 사회-경제 시스템 연구에 중대한 기초를 제공했다.

## Related Papers

- 🔗 후속 연구: [[papers/979_Large_teams_develop_and_small_teams_disrupt_science_and_tech/review]] — 과학 협력 네트워크에서 팀 크기가 연구 성과에 미치는 영향을 우선적 부착 메커니즘과 연결하여 분석한다.
- 🏛 기반 연구: [[papers/1034_The_Increasing_Dominance_of_Teams_in_Production_of_Knowledge/review]] — 과학 지식 생산에서 팀워크의 중요성이 증가하는 현상의 네트워크 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/1046_The_structure_of_scientific_collaboration_networks/review]] — 과학 협력 네트워크의 정적 구조 분석을 시간적 진화 패턴 분석으로 확장한다.
- 🏛 기반 연구: [[papers/1050_Unsupervised_embedding_of_trajectories_captures_the_latent_s/review]] — 과학 협력 네트워크의 진화에 대한 기본 이해가 연구자 이동의 잠재 구조를 파악하는 이론적 기반을 제공한다.
- 🏛 기반 연구: [[papers/1029_The_altering_landscape_of_USChina_science_collaboration_from/review]] — 과학 협력 네트워크의 진화 원리를 미중 협력의 구체적 사례에 적용하여 지정학적 요인의 영향을 이해할 수 있다.
- 🧪 응용 사례: [[papers/947_Collective_dynamics_of_small-world_networks/review]] — 소규모 세계 이론을 과학 협력 네트워크의 시간적 진화 패턴 분석에 적용한다.
- 🔗 후속 연구: [[papers/990_Networks_of_Scientific_Papers/review]] — 논문 인용 네트워크에서 발견된 패턴을 과학자 협력 네트워크의 진화적 관점으로 확장하여 분석한다.
