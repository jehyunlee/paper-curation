---
title: "927_A_Dynamic_Network_Measure_of_Technological_Change"
authors:
  - "Russell J. Funk"
  - "Jason Owen-Smith"
date: "2017.03"
doi: "10.1287/mnsc.2015.2366"
arxiv: ""
score: 4.0
essence: "본 논문은 기술 네트워크의 동적 변화를 측정하기 위해 특정 발명이 기존 기술 스트림을 공고히(consolidate) 하는지 또는 불안정하게(destabilize) 하는지를 정량화하는 CDt 지수를 제안한다. 대학 연구 상용화 분석을 통해 연방 기금은 파괴적 기술을 유도하지만 상업적 연계는 현상 유지 기술을 강화함을 보여준다."
tags:
  - "cat/Bibliometric_Network_Analysis"
  - "cat/Scientific_Impact_and_Innovation"
  - "sub/Temporal_and_Longitudinal_Analysis"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Funk and Owen-Smith_2017_A Dynamic Network Measure of Technological Change.pdf"
---

# A Dynamic Network Measure of Technological Change

> **저자**: Russell J. Funk, Jason Owen-Smith | **날짜**: 03/2017 | **DOI**: [10.1287/mnsc.2015.2366](https://doi.org/10.1287/mnsc.2015.2366)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1. Illustrative Calculations of the CDt Index for Three Patents*

본 논문은 기술 네트워크의 동적 변화를 측정하기 위해 특정 발명이 기존 기술 스트림을 공고히(consolidate) 하는지 또는 불안정하게(destabilize) 하는지를 정량화하는 CDt 지수를 제안한다. 대학 연구 상용화 분석을 통해 연방 기금은 파괴적 기술을 유도하지만 상업적 연계는 현상 유지 기술을 강화함을 보여준다.

## Motivation

- **Known**: 기술 혁신은 급진적(radical) 기술과 점진적(incremental) 기술로 구분되어 왔으며, 특허 인용 건수(citation count) 기반 측정이 기술 영향력 평가의 주요 방법으로 사용되고 있다.
- **Gap**: 기존의 전방 인용 기반(forward-citation-based) 측정법은 새로운 발명이 선행 기술에 미치는 영향의 질(quality)을 구분하지 못하므로, 기술 변화의 본질적 속성을 포착할 수 없다.
- **Why**: 기술이 기존 기술 체계를 공고히 하는지 파괴하는지를 구분하는 것은 혁신, 기업가정신, 기술 전략, 과학정책 발전에 필수적이며, 대학의 상용화가 학문의 독립성을 훼손하는지 판단하기 위해 필요하다.
- **Approach**: 기술들의 상호 연결 네트워크(network of interlinked technologies)를 동적으로 분석하여, 새로운 발명이 그 기반이 되는 선행 기술의 이후 사용 패턴을 어떻게 변경하는지를 측정한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2. Distribution of the CD5 Index Among U.S. Utility Patents Granted Between 1977 and 2005*

- **CDt 지수 개발**: 발명이 선행 기술의 후속 사용을 얼마나 증가(consolidation) 또는 감소(destabilization)시키는지를 정량화하는 지수를 개발했다.
- **mCDt 지수 제안**: CDt에 영향 가중치(impact weight)를 결합하여 발명의 상대적 중요도를 함께 고려한 측정치를 제시했다.
- **대학 상용화 분석**: 연방 연구비 지원은 파괴적 기술을 유도하지만, 상업적 관계는 현상 유지적 기술을 생성함을 실증적으로 입증했다.
- **측정 도구의 타당성**: 제안된 지수가 알려진 획기적 발명(breakthroughs)을 식별 가능하고 기술의 급진성/점진성과 관련된 기존 개념과 일치함을 검증했다.

## How

![Figure 3](figures/fig3.webp)

*Figure 3. Network Diagrams for the Monsanto (Top), PageRank (Middle), and Axel (Bottom) Patents*

- 특허 인용 네트워크 데이터를 이용하여 발명이 참조하는 선행 기술들의 집합 정의
- 선행 기술들이 이후 발명들에서 인용되는 빈도 변화를 분석하여 consolidation/destabilization 효과 측정
- CDt = (후속 인용률 변화) / (기대되는 배경 인용률)로 계산
- 네 가지 검증 연구 수행: (1) 알려진 기술 특성과의 일치도, (2) 사례 연구, (3) 대학 특성별 회귀분석, (4) 전방 인용과의 비교 분석
- U.S. Patent Citations Data File을 활용한 대규모 특허 데이터 분석

## Originality

- 기존 competency-destroying/enhancing 구분을 네트워크 수준의 동적 측정으로 발전시켜 연속적 스펙트럼으로 개념화했다.
- 조직의 역량이 아닌 기술 네트워크 자체의 구조 변화에 초점을 맞춤으로써 더 광범위한 영향을 포착한다.
- 전방 인용 기반 측정의 한계를 극복하기 위해 선행 기술의 상대적 사용 변화를 직접 측정하는 접근법을 도입했다.
- 대학 상용화의 핵심 논쟁(학문적 독립성 vs 상용적 가치)을 기술 네트워크 특성으로 경험적 검증 가능하게 만들었다.

## Limitation & Further Study

- 특허 데이터의 제한성: 특허되지 않은 혁신, 개인 발명가의 활동, 개발도상국의 기술 혁신 미포함
- 시간 지연 문제(time lag): 특허 인용이 이루어지기까지의 시차로 인해 최근 발명의 영향 측정 어려움
- 산업별 편차: 특허 인용 관행이 산업마다 다르므로 산업간 비교에 제약
- 후속 연구: 특정 산업(반도체, 바이오텍 등)에서의 심화 분석 필요
- 후속 연구: 네트워크 구조의 다층성(multi-layer) 분석을 통한 기술 인접성(technological proximity) 반영
- 후속 연구: 조직의 전략적 의도(strategic intent)와 발명의 consolidation/destabilization 효과의 관계 규명

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 기술 혁신 측정의 오래된 한계를 네트워크 분석으로 창의적으로 극복하였으며, 대학 상용화 논쟁에 대한 새로운 경험적 통찰을 제공한다. 혁신, 기업가정신, 과학정책 등 다양한 분야에 광범위한 적용 가능성을 가진 기초적 기여로 평가된다.

## Related Papers

- 🏛 기반 연구: [[papers/995_Papers_and_patents_are_becoming_less_disruptive_over_time/review]] — 기술 변화의 동적 네트워크 측정이 과학과 기술에서 파괴성 감소 현상을 이해하는 방법론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/934_Are_disruptive_papers_more_likely_to_impact_technology_and_s/review]] — 파괴적 논문이 기술과 사회에 미치는 영향을 CDt 지수를 통해 더 정교하게 측정할 수 있는 방법론을 제시한다.
- 🧪 응용 사례: [[papers/936_Atypical_Combinations_and_Scientific_Impact/review]] — 기술 변화의 동적 측정을 비전형적 조합이 과학적 영향력에 미치는 효과 분석에 적용한다.
- 🧪 응용 사례: [[papers/1075_Open_Catalyst_2020_OC20_Dataset_and_Community_Challenges/review]] — 기술 네트워크 분석을 촉매 과학에서 혁신적 발견을 위한 데이터셋 구축에 적용한다.
- 🔄 다른 접근: [[papers/1004_Quantifying_spatialtemporal_citation_diffusion_of_individual/review]] — 지식공간에서 인용 확산을 측정하는 대신 기술 네트워크에서 발명의 파괴적/통합적 영향을 정량화한다.
