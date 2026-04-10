---
title: "862_Using_artificial_intelligence_for_systematic_review_the_exam"
authors:
  - "Nathan Bernard"
  - "Yoshimasa Sagawa Jr"
  - "Nathalie Bier"
  - "Thomas Lihoreau"
  - "Lionel Pazart"
date: "2025.03"
doi: "10.1186/s12874-025-02528-y"
arxiv: ""
score: 3.0
essence: "Elicit이라는 AI 도구를 이용한 체계적 문헌고찰(systematic review) 과정이 기존의 전통적 선별 방법과 비교하여 부가가치를 제공하는지 검증한 연구이다. 재현성, 신뢰성, 정확성 세 가지 기준으로 Elicit의 성능을 평가하였다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Peer_Review"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Bernard et al._2025_Using artificial intelligence for systematic review the example of elicit.pdf"
---

# Using artificial intelligence for systematic review: the example of elicit

> **저자**: Nathan Bernard, Yoshimasa Sagawa Jr, Nathalie Bier, Thomas Lihoreau, Lionel Pazart, Thomas Tannou | **날짜**: 2025-03-18 | **DOI**: [10.1186/s12874-025-02528-y](https://doi.org/10.1186/s12874-025-02528-y)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1  The diagram from Tannou et al. study (left), Elicit (right), and the comparisons at different steps of the syste*

Elicit이라는 AI 도구를 이용한 체계적 문헌고찰(systematic review) 과정이 기존의 전통적 선별 방법과 비교하여 부가가치를 제공하는지 검증한 연구이다. 재현성, 신뢰성, 정확성 세 가지 기준으로 Elicit의 성능을 평가하였다.

## Motivation

- **Known**: 인공지능(AI) 도구들이 문헌고찰 과정의 선별(screening), 비뚤림 위험 평가, 자료 추출 등 다양한 단계에서 연구자를 지원하고 있다. Elicit은 GPT-3 기반의 언어모델로 의미론적 유사성을 통해 관련 논문을 식별하고 연구 질문의 요약을 생성할 수 있다.
- **Gap**: 기존 AI 도구들의 효과성에 대한 실증적 검증이 부족하며, 특히 Elicit이 전통적 선별 방법과 비교하여 실제로 부가가치를 제공하는지에 대한 직접적인 비교 연구가 필요하다.
- **Why**: 체계적 문헌고찰은 시간과 노력이 많이 소요되는 과정이므로, AI 도구의 효용성을 명확히 규명하면 연구 효율성 향상과 안정성 있는 AI 도구 개발에 기여할 수 있다.
- **Approach**: 기존의 AI 미사용 우산형 문헌고찰(umbrella review)과 Elicit을 이용한 문헌고찰을 동일한 선정 기준으로 비교하였으며, 재현성(반복성), 신뢰성, 정확성 세 가지 측면에서 평가했다.

## Achievement

![Figure 1](figures/fig1.webp)

*Fig. 1  The diagram from Tannou et al. study (left), Elicit (right), and the comparisons at different steps of the syste*

- **재현성 부족**: 동일한 검색 조건에서 3회 반복 검색 결과가 각각 246, 169, 172개로 상이하여 일관성이 낮음을 확인
- **부분적 중복**: 최종 포함된 17개 논문 중 3개(17.6%)만 양쪽 방법에서 공통으로 식별되어 낮은 일치도 확인
- **새로운 논문 발굴**: Elicit 전용으로 3개 논문을 식별했으나, 전통 방법이 14개를 추가로 식별하여 누락률 높음
- **보완적 도구로의 위치**: Elicit이 완전한 대체 도구는 아니지만 체계적 문헌고찰의 설계 및 작성 단계에서 보완적 가치를 가짐을 제시

## How


- 2023년 4월 19-20일에 동일한 연구 질문('스마트 생활환경의 노화 제자리 지원 효과')을 3회 반복 검색", '문서 유형(체계적 문헌고찰) 및 출판연도(2005-2021) 필터 적용
- 9개의 연도별 검색(2005, 2010, 2015-2021)으로 중복 최소화
- Elicit의 'show more' 기능으로 추가 논문이 없을 때까지 수집", '원본 문헌고찰 저자가 동일한 포함/제외 기준으로 제목, 초록, 전문 검토 시행
- 기술통계(백분율)를 이용하여 두 방법의 중복도 평가

## Originality

- AI 도구(Elicit)의 체계적 문헌고찰 기여도를 실증적으로 검증한 최초의 직접 비교 연구
- 재현성, 신뢰성, 정확성이라는 명확한 평가 틀을 제시하여 AI 도구 평가의 방법론적 토대 제공
- AI 도구 사용 시 방법론적 엄격성 유지의 필요성을 실증적으로 강조
- Elicit의 기술적 한계(낮은 재현성)를 정량적으로 입증

## Limitation & Further Study

- 단일 주제(노화와 스마트 생활환경) 연구로 다른 분야 적용 가능성 제한
- 단일 저자의 수동 검토로 인한 평가자 간 신뢰성(inter-rater reliability) 부재
- 2005-2021년 출판물만 대상으로 하여 최근 논문 누락 가능성
- Elicit의 알고리즘 변화에 따른 결과 변동 가능성 미검토
- 후속 연구: 다양한 주제 영역에서의 검증, 다중 평가자 참여, 다른 AI 도구와의 비교, Elicit의 알고리즘 개선 시점에서의 재검증 필요

## Evaluation

- Novelty: 3/5
- Technical Soundness: 2/5
- Significance: 3/5
- Clarity: 4/5
- Overall: 3/5

**총평**: 본 연구는 AI 도구의 실제 효용성을 실증적으로 검증한 의미 있는 시도이나, 재현성 부족과 높은 누락률 등 중대한 한계를 발견했다. Elicit은 보완적 도구로서의 가치는 있으나 현재 단계에서 전통적 방법을 완전히 대체할 수 없으며, AI 도구의 개선과 사용 가이드라인 개발이 시급함을 시사한다.

## Related Papers

- 🧪 응용 사례: [[papers/042_Academicbrowse_Benchmarking_academic_browse_ability_of_llms/review]] — 학술 검색 능력 벤치마킹이 AI 도구 기반 체계적 문헌고찰의 검색 단계 성능 평가에 활용된다.
- 🏛 기반 연구: [[papers/510_Llms_for_literature_review_Are_we_there_yet_arXiv_preprint_a/review]] — 문헌고찰을 위한 LLM 연구 현황이 AI 기반 체계적 리뷰 도구 활용의 이론적 배경을 제공한다.
- 🧪 응용 사례: [[papers/154_Best_Practices_for_Using_AI_When_Writing_Scientific_Manuscri/review]] — 과학 논문 작성에서의 AI 활용 모범 사례가 체계적 문헌 고찰에서 AI 도구의 효과적이고 윤리적 활용에 직접 적용된다
