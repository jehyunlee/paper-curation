---
title: "992_OpenAlex_in_focus_Metadata_quality_of_publication_type_and_l"
authors:
  - "Güleda ed Doǧan"
  - "Ayça Nur Sezen"
date: "2026.03"
doi: "10.47989/ir31iconf64207"
arxiv: ""
score: 4.0
essence: "OpenAlex 데이터베이스의 출판물 유형(publication type)과 언어(language) 메타데이터 품질을 평가하여 43%의 출판물 유형 불일치와 3.3%의 언어 불일치를 발견했다. 체계적인 데이터 검증의 필요성을 강조한다."
tags:
  - "cat/Bibliometric_Network_Analysis"
  - "sub/Bibliometric_Datasets_and_Infrastructure"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Doǧan and Sezen_2026_OpenAlex in focus Metadata quality of publication type and language fields in an open peer review c.pdf"
---

# OpenAlex in focus: Metadata quality of publication type and language fields in an open peer review corpus

> **저자**: Güleda ed Doǧan, Ayça Nur Sezen | **날짜**: 2026-03-20 | **DOI**: [10.47989/ir31iconf64207](https://doi.org/10.47989/ir31iconf64207)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1 illustrates the differences between the Assigned Type (OpenAlex) and the Verified Type*

OpenAlex 데이터베이스의 출판물 유형(publication type)과 언어(language) 메타데이터 품질을 평가하여 43%의 출판물 유형 불일치와 3.3%의 언어 불일치를 발견했다. 체계적인 데이터 검증의 필요성을 강조한다.

## Motivation

- **Known**: OpenAlex는 Microsoft Academic Graph의 후속으로 2022년 출범한 무료 개방형 서지 데이터베이스로 광범위한 커버리지와 접근성을 제공한다. 다만 메타데이터 신뢰성 문제가 지속적으로 보고되고 있다.
- **Gap**: OpenAlex의 출판물 유형과 언어 필드에 대한 체계적인 메타데이터 품질 평가가 부족했다. 특히 이 두 필드는 문헌 선별과 포함/배제 기준 결정에 직접적으로 영향을 미치는 중요 요소이다.
- **Why**: 출판물 유형과 언어는 서지계량 분석과 체계적 문헌고찰에서 핵심적인 필터링 기준이므로 메타데이터 정확성이 연구 결과의 타당성을 직접적으로 좌우한다. OpenAlex의 광범위한 사용으로 인해 메타데이터 품질 검증은 매우 시급한 문제이다.
- **Approach**: OpenAlex에서 '개방형 동료심사(open peer review)'를 검색하여 6,640개 레코드를 수동으로 검증했다. 출판사 웹사이트와의 교차검증 및 Crossref 데이터와 비교하여 메타데이터 불일치를 분석했다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1 illustrates the differences between the Assigned Type (OpenAlex) and the Verified Type*

- **출판물 유형 불일치 정량화**: 6,640개 레코드 중 2,878개(43%)에서 출판물 유형 불일치 발견, 'Article' 카테고리가 가장 자주 오용됨을 확인", '**언어 메타데이터 오류 식별**: 222개 레코드(3.3%)에서 언어 불일치, 비영어 저작에 영어 레이블이 부정확하게 할당된 사례 다수 발견
- **분류 스킴 개발**: 12개 카테고리의 정제된 출판물 유형 분류 스킴 구축 (article, blog post, book, book chapter, book review, editorial, peer review, proceeding paper, opinion/commentary, report, review, thesis/dissertation, other)
- **Crossref 비교 분석**: Crossref 데이터가 OpenAlex와 광범위한 카테고리에서는 일치하나 수동 검증과는 괴리를 보임

## How


- 2024년 11월 26일 OpenAlex에서 'open peer review' 및 'open peer-review' 검색어로 데이터 수집 (9,315개 레코드)", '출판물 유형 기준으로 초기 필터링 수행 (2,184개 제거, 7,090개 유지)
- DOI 식별자를 사용한 중복 제거 및 데이터 정제 (최종 6,640개 고유 출판물)
- 출판사 웹사이트 검토 및 Google 자동 번역, ChatGPT를 활용한 수동 검증
- OpenAlex, 수동 분류, Crossref 데이터 간 일치도 평가 (agreement analysis)

## Originality

- 대규모 개방형 데이터베이스(OpenAlex)의 메타데이터 품질을 체계적으로 평가한 실증 연구
- 출판물 유형과 언어라는 구체적인 메타데이터 필드에 초점을 맞춘 상세한 분석
- 12개 카테고리 분류 스킴을 통한 OpenAlex 메타데이터와 출판사 정보의 교차검증 방법론 제시
- Crossref, OpenAlex, 수동 분류의 세 가지 데이터 소스 간 비교 분석

## Limitation & Further Study

- 단일 검색어('open peer review')에 제한되어 일반화 가능성이 제한적 - 다양한 주제 영역 및 출판물 유형에 대한 확대 검증 필요", '수동 검증 과정의 주관성 가능성 - 여러 검증자 간 일치도(inter-rater reliability) 평가 부족
- 비영어 출판물의 검증에 자동 번역 및 ChatGPT에 의존 - 복잡한 학술 용어의 정확한 분류에 한계 가능
- OpenAlex의 메타데이터 소스 계층 구조(publisher, Crossref, repositories 등) 영향에 대한 분석 부족
- 시간 경과에 따른 메타데이터 개선 추이에 대한 종단 분석 미포함

## Evaluation

- Novelty: 3/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 연구는 OpenAlex의 메타데이터 품질 문제를 정량적으로 입증하고 실용적인 검증 방안을 제시함으로써 개방형 학술 인프라의 신뢰성 향상에 기여한다. 연구자들의 체계적인 데이터 정제의 필요성을 강조하는 중요한 경고 사례가 된다.

## Related Papers

- ⚖️ 반론/비판: [[papers/993_OpenAlex_A_fully-open_index_of_scholarly_works_authors_venue/review]] — OpenAlex의 메타데이터 품질 문제점과 완전 개방형 학술 색인으로서의 장점이 상반된 관점을 제시한다.
- 🔄 다른 접근: [[papers/1015_S2ORC_The_Semantic_Scholar_Open_Research_Corpus/review]] — S2ORC와 OpenAlex 모두 대규모 오픈 학술 데이터셋이지만 데이터 품질 평가 관점에서 서로 다른 특성을 보인다.
- 🏛 기반 연구: [[papers/1071_Data_measurement_and_empirical_methods_in_the_science_of_sci/review]] — 과학학에서의 데이터 측정과 실증 방법론 연구가 메타데이터 품질 평가의 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/1015_S2ORC_The_Semantic_Scholar_Open_Research_Corpus/review]] — S2ORC 데이터의 메타데이터 품질 문제를 OpenAlex와 비교하여 대규모 학술 데이터베이스의 신뢰성을 평가한다.
- 🏛 기반 연구: [[papers/1044_The_State_of_OA_A_Large-Scale_Analysis_of_the_Prevalence_and/review]] — OpenAlex의 메타데이터 품질 분석을 통해 OA 연구의 데이터 신뢰성을 확보하고 더 정확한 분석 기반을 마련한다.
- 🏛 기반 연구: [[papers/937_Authorship_titles_and_open_access_as_drivers_of_citation_per/review]] — 출판 유형과 메타데이터 품질에 대한 체계적 분석이 인용 성과 요인 연구의 데이터 신뢰성 기반을 제공한다.
- 🔗 후속 연구: [[papers/1115_Google_Scholar_Microsoft_Academic_Scopus_Dimensions_Web_of_S/review]] — OpenAlex의 메타데이터 품질을 다른 주요 인용 데이터베이스와 비교하여 각 플랫폼의 특성을 종합적으로 평가한다.
- 🔗 후속 연구: [[papers/939_BibFusion_A_Python_package_to_integrate_deduplicate_and_harm/review]] — OpenAlex의 메타데이터 품질 분석과 연결되어 다양한 서지 데이터베이스 통합 시 고려해야 할 데이터 품질 이슈를 다룬다.
