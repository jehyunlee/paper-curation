---
title: "944_Co-Citation_Analysis_Bibliographic_Coupling_and_Direct_Citat"
authors:
  - "Kevin W. Boyack"
  - "Richard Klavans"
date: "2010.12"
doi: "10.1002/asi.21419"
arxiv: ""
score: 4.0
essence: "대규모 생의학 문헌(2004-2008, 215만 개 논문)을 이용하여 공인용분석(co-citation analysis), 서지적 결합(bibliographic coupling), 직접 인용(direct citation), 그리고 하이브리드 접근법의 4가지 유사성 기반 방법이 연구 최전선을 얼마나 정확하게 표현하는지 비교 평가했다."
tags:
  - "cat/Bibliometric_Network_Analysis"
  - "cat/Scientific_Information_Systems"
  - "sub/Citation_Metrics_and_Indices"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Boyack and Klavans_2010_Co‐citation analysis, bibliographic coupling, and direct citation Which citation approach represent.pdf"
---

# Co‐citation analysis, bibliographic coupling, and direct citation: Which citation approach represents the research front most accurately?

> **저자**: Kevin W. Boyack, Richard Klavans | **날짜**: 12/2010 | **DOI**: [10.1002/asi.21419](https://doi.org/10.1002/asi.21419)

---

## Essence


대규모 생의학 문헌(2004-2008, 215만 개 논문)을 이용하여 공인용분석(co-citation analysis), 서지적 결합(bibliographic coupling), 직접 인용(direct citation), 그리고 하이브리드 접근법의 4가지 유사성 기반 방법이 연구 최전선을 얼마나 정확하게 표현하는지 비교 평가했다.

## Motivation

- **Known**: 공인용분석과 서지적 결합은 과학 지도화의 오래된 기법이며, 여러 선행연구에서 다양한 방법론들의 정확성을 비교한 바 있으나 결과가 일관되지 않았다.
- **Gap**: 대규모 코퍼스에서 citation-based 접근법들의 정확성을 체계적으로 비교한 연구가 부족하며, 특히 실제 포트폴리오 분석 응용에 적합한 정확도 측정 지표가 필요하다.
- **Why**: 과학 지도화는 연구 기획 및 평가, 자금 배분 등 실제 의사결정에 사용되므로, 어떤 citation 접근법이 가장 정확한 클러스터링을 제공하는지 파악하는 것이 중요하다.
- **Approach**: 2.15백만 개 논문의 대규모 생의학 문헌 코퍼스에 대해 4가지 유사성 접근법을 적용하고, Jensen-Shannon 발산을 이용한 텍스트 응집도(textual coherence)와 MEDLINE의 연구비-논문 연계 데이터 기반 집중도(concentration measure) 두 가지 정확성 지표로 평가했다.

## Achievement


- **세 가지 순수 citation 기반 방법의 정확성 순위 규명**: 서지적 결합이 공인용분석을 약간 상회하며, 직접 인용이 가장 낮은 정확성을 보였다
- **하이브리드 접근법의 우수성 입증**: citation-text 하이브리드 방법(서지적 결합 기반)이 순수 서지적 결합 결과를 모든 지표에서 개선했다
- **대규모 코퍼스에서 높은 클러스터링 성공률**: 4가지 접근법 모두 92% 이상의 논문을 성공적으로 클러스터링했다
- **새로운 정확도 측정 지표 개발**: 연구비 연계 데이터 기반의 포트폴리오 분석 친화적 평가 지표를 제시했다

## How


- 2004-2008년 생의학 문헌 2,153,769개 논문의 대규모 코퍼스 구축
- 4가지 citation 유사성 접근법(co-citation, bibliographic coupling, direct citation, hybrid) 구현 및 적용
- Jensen-Shannon 발산을 이용한 클러스터 내 텍스트 응집도(within-cluster textual coherence) 계산
- MEDLINE 연구비 인정(acknowledgment) 정보로부터 grant-to-article 연계 추출 및 클러스터 집중도 측정
- 두 가지 정확성 지표를 이용한 방법론 간 비교 분석

## Originality

- 대규모 코퍼스(215만 개 논문)를 대상으로 한 첫 종합적 citation 방법 비교 연구
- 연구비 연계 데이터를 활용한 참신한 정확도 측정 지표 개발로 포트폴리오 분석과의 직접적 연계 제시
- citation 접근법의 이론적 차이를 시각화(Figure 1)하여 각 방법의 장단점을 명확하게 설명
- 직접 인용(direct citation) 방법의 정확성에 대한 첫 대규모 실증 평가

## Limitation & Further Study

- 분석 대상이 생의학 분야로 제한되어 다른 학문 분야에의 일반화 가능성 미지수
- 한국어 및 비영문 문헌 미포함으로 인한 국제 대표성 한계
- 논문 발행 후 인용 누적에 시간이 필요하므로 최신 논문의 정확한 클러스터링이 어려울 수 있음
- 후속연구로서 텍스트 기반 방법론과의 비교, 다른 학문 분야 적용, 시간 경과에 따른 안정성 검증이 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 대규모 코퍼스와 새로운 정확도 지표를 활용하여 citation 기반 science mapping 방법론의 상대적 성능을 처음으로 체계적으로 평가한 중요한 연구로, 생의학 분야의 포트폴리오 분석 등 실제 응용에 직접 활용 가능한 신뢰성 높은 결과를 제시했다.

## Related Papers

- 🧪 응용 사례: [[papers/982_Mapping_Knowledge_Topic_Analysis_of_Science_Locates_Research/review]] — 서지학적 유사성 방법론을 주제 수준에서 연구 분야의 지리적 위치 매핑에 적용한다.
- 🏛 기반 연구: [[papers/969_Hierarchical_Classification_of_Research_Fields_in_the_Web_of/review]] — 서지학적 유사성 기반 연구 최전선 표현이 Web of Science 기반 연구 분야 계층적 분류의 방법론적 기반이 된다.
- 🧪 응용 사례: [[papers/978_Introducing_the_open_biomedical_map_of_science/review]] — 생의학 분야의 서지학적 결합 분석을 생의학 과학 지도의 개방형 구축에 적용한다.
- 🏛 기반 연구: [[papers/1018_Science_Mapping_and_Science_Maps/review]] — 공인용분석과 서지결합의 비교 평가가 과학 매핑의 다양한 접근법 이해의 기반이 된다.
- 🔗 후속 연구: [[papers/932_An_empirical_analysis_of_open_access_citation_advantages_in/review]] — 오픈 액세스의 인용 우위를 분석하여 다양한 인용 기반 방법들이 연구 최전선을 표현하는 정확도에 미치는 영향을 확장 분석한다.
- 🧪 응용 사례: [[papers/1053_Visualizing_the_context_of_citations_referencing_papers_publ/review]] — 논문 발표 후 인용 맥락을 시각화하여 직접 인용과 공인용 분석의 실제적 차이를 구체적으로 보여준다.
- 🔗 후속 연구: [[papers/1053_Visualizing_the_context_of_citations_referencing_papers_publ/review]] — 전통적인 공인용분석과 서지결합을 인용 맥락 기반 네트워크 분석으로 확장한다.
- 🔄 다른 접근: [[papers/990_Networks_of_Scientific_Papers/review]] — 동시인용, 서지결합, 직접인용이라는 세 가지 인용 기반 분석법이 초기 인용 네트워크 연구의 방법론적 확장이다.
