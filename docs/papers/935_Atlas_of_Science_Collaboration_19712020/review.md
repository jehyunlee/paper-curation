---
title: "935_Atlas_of_Science_Collaboration_19712020"
authors:
  - "Keisuke Okamura"
date: "2024.06"
doi: "10.1007/s42979-024-02973-4"
arxiv: ""
score: 4.0
essence: "1971년부터 2020년까지 OpenAlex 데이터를 활용하여 15개 자연과학 분야의 국제·기관 간 연구 협력 관계를 시각화한 아틀라스를 제시한다. 세계 지도와 다양한 다이어그램을 통해 국가 및 국제 협력 패턴의 변화를 보여준다."
tags:
  - "cat/Scientific_Information_Systems"
  - "sub/Scientific_Collaboration_Networks"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Okamura_2024_Atlas of Science Collaboration, 1971–2020.pdf"
---

# Atlas of Science Collaboration, 1971–2020

> **저자**: Keisuke Okamura | **날짜**: 2024-06-11 | **DOI**: [10.1007/s42979-024-02973-4](https://doi.org/10.1007/s42979-024-02973-4)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1(a) | The World Map of Artificial Intelligence Collaboration. The bubbles represent the top 199 institutions*

1971년부터 2020년까지 OpenAlex 데이터를 활용하여 15개 자연과학 분야의 국제·기관 간 연구 협력 관계를 시각화한 아틀라스를 제시한다. 세계 지도와 다양한 다이어그램을 통해 국가 및 국제 협력 패턴의 변화를 보여준다.

## Motivation

- **Known**: 과학 협력은 점차 국제화되고 있으며, 선진국과 개발도상국 간의 협력이 증가하고 있다. 기존 bibliometrics 연구들은 Scopus, Web of Science 등 상용 데이터베이스에 의존해왔다.
- **Gap**: 개방형 데이터 기반의 광범위한 과학 협력 지형 분석과 시각화가 부족했으며, 정책입안자와 외교관을 위한 직관적 자료의 제공이 제한적이었다. OpenAlex의 포괄적 데이터 활용 사례가 부족했다.
- **Why**: 과학 정책 결정과 국제 협력 전략 수립을 위해 전지구적 협력 현황의 체계적 이해가 필수적이다. 공개 데이터 기반 분석은 투명성과 재현성을 강화한다.
- **Approach**: OpenAlex API를 통해 2023년 8월 기준 논문 메타데이터를 수집하고, 공저 관계 (coauthorship) 기반의 기관 간 협력을 추출했다. 4개 시간대 구간별로 15개 과학분야를 분석하여 지도, 행렬 다이어그램, 계층적 클러스터링으로 시각화했다.

## Achievement


- **OpenAlex 활용의 타당성 입증**: 기존 상용 DB 대비 비영어 논문, 글로벌 사우스 산출물, 전자출판물을 포괄적으로 포함하여 더 정확한 R&D 활동 규모 파악 가능
- **다층 시각화 프레임워크 개발**: 세계 지도 버블 차트, 상위 30개 기관 맵, 국제 협력 행렬 다이어그램, 기관 간 협력 덴드로그램 등 4가지 상보적 시각화 방식 제시
- **50년 장기 협력 트렌드 추적**: 1971-2020년을 4개 시간대로 분할하여 각 과학분야별 협력 중심의 지리적 이동과 클러스터 형성 과정 정량화
- **정책 수용성 높은 결과물**: 과학기술정책 입안자, 외교관, 국제기구, 대학 연구기획팀 등 다양한 이해관계자를 위한 직관적 시각 자료 제공

## How


- OpenAlex 개념 분류 체계 Level-1 개념 15개 (Artificial Intelligence, Quantum Science 등) 선정
- 각 Level-1 개념의 하위 Level-2 이상 관련 개념들을 포함하여 확장된 분야 정의
- 기관별 논문 생산량 기준으로 상위 199개 기관(상위 50개는 별도 상세 분석) 선택
- 공저자 관계를 기반으로 기관 간 쌍방향 협력 관계 추출 (최소 5편 이상 논문)
- R의 maps, geosphere, ggplot2 패키지를 활용한 대원(great circle) 곡선 기반 지도 시각화
- 국가 수준의 이분 협력 관계 계수를 반영한 행렬 다이어그램 작성
- 상위 50개 기관의 계층적 클러스터링을 통한 협력 네트워크 구조 분석

## Originality

- OpenAlex의 개방형 데이터 (CC0 라이선스)를 처음으로 대규모 협력 지형 분석에 체계적으로 적용
- 15개 과학분야에 대한 통일된 분석 틀 제시로 학제 간 비교 연구 기반 제공
- 상위 50대 기관에만 국한하지 않고 상위 199개 기관을 포함한 다층적 시각화로 협력 지형의 세밀한 변화 포착
- Big 5 과학국가 (미국, 중국, EU27, 영국, 일본) 중심의 정책친화적 분석 프레임 설계

## Limitation & Further Study

- **버전 1의 임시성**: OpenAlex 자체가 지속적 업데이트 중이므로 현재 시각화가 완전하거나 정확하지 않을 수 있으며, 향후 더 정확한 버전 기대
- **행렬 다이어그램의 불완전성**: 상위 50개 기관만 포함하므로 영(zero) 값이 협력 부재가 아닌 순위 외 기관 제외를 의미할 수 있음
- **기관 귀속 문제**: OpenAlex의 ROR (Research Organization Registry) 기반 기관 식별이 미흡할 경우 협력 관계 과소 계산 가능성
- **공저 기준의 단순성**: 공저자 관계만 협력으로 정의하여 인용, 자금 지원, 공동 프로젝트 등 다른 협력 형태는 미반영
- **후속 과제**: Zenodo 등 개방 플랫폼에서 개정판 지속 배포 필요, OpenAlex 데이터 품질 개선 시 재분석 수행, 협력 강도(경중) 분석 추가

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 연구는 OpenAlex 개방 데이터를 활용하여 50년간 15개 과학분야의 국제 협력 지형을 처음으로 체계적으로 시각화했으며, 정책입안자와 과학외교 관계자에게 직관적이고 활용 가능한 자료를 제공한다. 다만 현재는 v1 버전으로 향후 데이터 품질 개선에 따른 지속적 업데이트가 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/1029_The_altering_landscape_of_USChina_science_collaboration_from/review]] — 미중 과학 협력의 변화하는 지형을 50년간의 국제 과학 협력 아틀라스의 맥락에서 구체적으로 분석한다.
- 🏛 기반 연구: [[papers/967_Global_patterns_of_migration_of_scholars_with_economic_devel/review]] — 경제 발전에 따른 학자들의 글로벌 이동 패턴을 제공하여 국제 과학 협력 변화의 기반 동력을 설명한다.
- 🧪 응용 사례: [[papers/967_Global_patterns_of_migration_of_scholars_with_economic_devel/review]] — 학자 이동 패턴을 과학 협력 지도를 통해 시각화하고 지리적 분포 변화 추적 가능
- 🔗 후속 연구: [[papers/1023_SciSciNet_A_large-scale_open_data_lake_for_the_science_of_sc/review]] — 과학 협력의 지도화 연구를 더 포괄적이고 최신의 데이터로 확장할 수 있는 인프라를 제공한다.
- 🧪 응용 사례: [[papers/1029_The_altering_landscape_of_USChina_science_collaboration_from/review]] — 1971-2020년 과학 협력 지도를 통해 미중 협력 변화를 더 넓은 글로벌 맥락에서 비교 분석할 수 있다.
