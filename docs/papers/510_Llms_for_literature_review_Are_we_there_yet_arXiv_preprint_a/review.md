---
title: "510_Llms_for_literature_review_Are_we_there_yet_arXiv_preprint_a"
authors:
  - "Shubham Agarwal"
  - "Gaurav Sahu"
  - "Abhay Puri"
  - "Issam Laradji"
  - "Krishnamurthy DJ Dvijotham"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.25
essence: "본 논문은 LLM(Large Language Model)을 활용하여 학술 논문의 문헌 리뷰 작성을 자동화하는 방법을 제시한다. 논문 초록을 입력으로 관련 연구를 검색하고 이를 바탕으로 문헌 리뷰 섹션을 생성하는 두 단계 프로세스를 제안하며, 계획 기반 접근으로 환각(hallucination) 감소를 달성한다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Scientific_Literature_Analysis"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Agarwal et al._2024_Llms for literature review Are we there yet arXiv preprint arXiv2412.15249, 2024..pdf"
---

# Llms for literature review: Are we there yet? arXiv preprint arXiv:2412.15249, 2024.

> **저자**: Shubham Agarwal, Gaurav Sahu, Abhay Puri, Issam Laradji, Krishnamurthy DJ Dvijotham, Jason Stanley, Laurent Charlin, Christopher Pal | **날짜**: 2024 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) *본 논문의 프레임워크 구성: (1) 키워드 및 임베딩 기반 검색, (2) LLM 기반 재순위화, (3) 문헌 리뷰 생성, (4) 계획 기반 최적화*

본 논문은 LLM(Large Language Model)을 활용하여 학술 논문의 문헌 리뷰 작성을 자동화하는 방법을 제시한다. 논문 초록을 입력으로 관련 연구를 검색하고 이를 바탕으로 문헌 리뷰 섹션을 생성하는 두 단계 프로세스를 제안하며, 계획 기반 접근으로 환각(hallucination) 감소를 달성한다.

## Motivation

- **Known**: 문헌 리뷰는 과학 연구의 필수 구성 요소이지만 시간 소비적이고 어렵다. 특히 머신러닝 분야에서는 매월 수천 편의 논문이 arXiv에 공개되어 상황이 악화되고 있다.

- **Gap**: 기존 LLM 연구는 문헌 리뷰 작성을 전체 태스크로 접근하여 성능이 제한적이며, 검색과 생성 단계에서 최적화된 방법론이 부족하다. 또한 최신 LLM의 제로샷 평가 시 테스트 세트 오염(contamination) 문제가 해결되지 않았다.

- **Why**: 논문 집필 초기 단계에서 학자들이 신속하게 관련 연구를 파악하고 문헌 리뷰를 작성할 수 있도록 지원하는 것은 중요하다. 초록만으로도 핵심 아이디어를 파악하고 참고 자료를 제시할 수 있다면 효율성이 극대화될 수 있다.

- **Approach**: 문제를 4가지 하위 태스크로 분해: (1) LLM을 통한 키워드 추출, (2) 키워드 및 임베딩 기반 검색의 결합, (3) LLM 기반 재순위화 및 속성(attribution) 제공, (4) 계획 기반 문헌 리뷰 생성

## Achievement

![Figure 2](figures/fig2.webp) *재순위화 전략의 효과: 다양한 순위 결정 방식이 정규화된 재호출률(normalized recall)에 미치는 영향*

1. **검색 성능 개선**: 키워드 기반 검색과 임베딩 기반 검색을 결합했을 때 정밀도(precision) 10%, 정규화된 재호출률(normalized recall) 30% 향상. LLM 기반 속성 추가로 재호출률이 2배 증가

2. **생성 품질 향상**: 계획 기반 접근법으로 ROUGE 점수 향상 및 인간 평가에서 더 높은 품질 달성. 환각된 참고문헌 18-26% 감소

3. **평가 프로토콜 기여**: 최신 arXiv 논문을 월별로 롤링 방식으로 수집하여 테스트 세트 오염을 방지하는 평가 프로토콜 제안 및 공개

## How

![Figure 4](figures/fig4.webp) *생성 태스크의 파이프라인: 쿼리 논문의 관련 연구 섹션을 생성하는 프로세스*

**검색 단계 (Retrieval)**:
- LLM으로부터 초록 텍스트를 의미 있는 키워드로 추출
- Google Search 및 Semantic Scholar를 통한 키워드 기반 검색 수행
- Sentence-BERT 등을 활용한 임베딩 기반 검색 병렬 수행
- LLM을 재순위화 모듈로 활용하여 후보 논문을 재정렬
- 재순위화 시 특정 문장/구절 기반의 속성(attribution) 정보 제공
- Debate-prone LLM 활용으로 여러 검색 결과의 합의(aggregation) 도모

**생성 단계 (Generation)**:
- 상위 k개 논문 선택 후 LLM에 쿼리 초록과 함께 제공
- 먼저 문헌 리뷰의 구조적 계획(plan) 생성 (자동 생성 또는 사용자 정의)
- 계획에 따라 단계별로 실제 리뷰 텍스트 생성
- 각 문장에서 인용할 논문을 명시적으로 지정

**재순위화 및 속성 기법**:
- 프롬프트 기반의 단순 속성 방식으로 복잡한 gradient 계산 회피
- 확장성 높고 다중 통과 불필요
- 모델의 의사결정 과정에 대한 투명성 증대

## Originality

- 문헌 리뷰 작성을 검색과 생성으로 명확하게 분해하고, 각 단계의 최적화 전략을 제시한 점이 혁신적

- 키워드 추출과 임베딩 기반 검색의 결합으로 상호 보완 효과 창출 (새로운 조합 방식)

- LLM 기반 속성(attribution) 방식의 프롬프팅 기법은 gradient 방식과 달리 간단하면서도 효과적 (확장성 우수)

- 계획 기반 생성(plan-based generation) 접근으로 사용자 제어 능력 향상 및 환각 감소 달성

- 테스트 세트 오염을 방지하는 롤링 평가 프로토콜(Rolling Evaluation Protocol) 제안으로 향후 LLM 평가의 신뢰성 기여

## Limitation & Further Study

**한계**:
- 초록 기반 평가이므로 전체 논문 내용을 활용하지 못함 (다만 프레임워크는 확장 가능하도록 설계)
- 외부 검색 엔진(Google Search, Semantic Scholar)에 의존하므로 폐쇄 도메인(closed domain)에 적용 어려움
- 평가가 주로 자동 메트릭(ROUGE 등)과 제한된 인간 평가에 기반함
- 계획 생성 단계에서도 LLM 오류 가능성 존재

**후속 연구**:
- 전체 논문 내용을 활용하는 경우의 성능 비교 분석
- 도메인 특화 검색 엔진과의 통합
- 더 광범위한 인간 평가 실시
- 사용자와의 상호작용적(interactive) 시스템으로 발전
- 다양한 학문 분야(의학, 법학 등)에 대한 적용성 검증

## Evaluation

- **Novelty**: 4.5/5 - 검색과 생성의 분해, 속성 기반 재순위화, 계획 기반 생성 등이 창의적이며, 롤링 평가 프로토콜도 커뮤니티에 기여

- **Technical Soundness**: 4/5 - 방법론이 합리적이고 실험이 체계적이나, 일부 평가 메트릭의 한계(자동 메트릭의 신뢰성) 지적 가능

- **Significance**: 4/5 - 실제 학술 커뮤니티의 광범위한 문제를 다루며, 정량적 개선(정밀도 10%, 재호출률 30%, 환각 감소 18-26%)이 의미 있음. 공개된 프로토콜과 도구의 가치도 높음

- **Clarity**: 4.5/5 - 논문 구조가 명확하고 프레임워크 다이어그램이 직관적. 각 단계의 설명이 상세함

- **Overall**: 4.25/5

**총평**: 본 논문은 LLM 기반 문헌 리뷰 생성을 실질적으로 개선하기 위해 문제를 체계적으로 분해하고, 검색과 생성 각 단계에서 창의적인 해법을 제시한 우수한 연구이다. 특히 속성 기반 재순위화와 계획 기반 생성으로 환각 감소를 달성한 점과 테스트 세트 오염을 방지하는 평가 프로토콜을 제공한 점이 학계에 큰 기여를 한다.

## Related Papers

- 🔄 다른 접근: [[papers/604_Pasa_An_llm_agent_for_comprehensive_academic_paper_search/review]] — 문헌 리뷰 자동화를 위한 서로 다른 LLM 기반 접근법을 제시합니다.
- 🧪 응용 사례: [[papers/506_LLM4SR_A_Survey_on_Large_Language_Models_for_Scientific_Rese/review]] — 과학 연구에서의 LLM 활용이 문헌 리뷰 작성에 적용됩니다.
- 🔗 후속 연구: [[papers/493_Litllm_A_toolkit_for_scientific_literature_review/review]] — 문헌 리뷰가 더 포괄적인 과학 문헌 검토 도구로 확장됩니다.
- 🔄 다른 접근: [[papers/604_Pasa_An_llm_agent_for_comprehensive_academic_paper_search/review]] — 학술 논문 검색을 위한 서로 다른 자동화 접근법을 제시합니다.
- 🏛 기반 연구: [[papers/862_Using_artificial_intelligence_for_systematic_review_the_exam/review]] — 문헌고찰을 위한 LLM 연구 현황이 AI 기반 체계적 리뷰 도구 활용의 이론적 배경을 제공한다.
- 🏛 기반 연구: [[papers/897_Can_AI_review_the_scientific_literature__and_figure_out_what/review]] — LLM의 문헌 검토 능력에 대한 기초적 평가를 제공한다
