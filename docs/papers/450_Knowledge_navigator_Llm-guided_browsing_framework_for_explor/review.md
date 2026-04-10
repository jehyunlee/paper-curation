---
title: "450_Knowledge_navigator_Llm-guided_browsing_framework_for_explor"
authors:
  - "Uri Katz"
  - "Mosh Levy"
  - "Yoav Goldberg (Bar-Ilan University"
  - "Allen Institute for AI)"
date: "2024"
doi: "arXiv:2408.15836"
arxiv: ""
score: 4.0
essence: "대규모 과학 문헌에서 탐색적 검색을 지원하기 위해 LLM과 클러스터링 기법을 결합하여 검색 결과를 2단계 계층 구조의 주제로 자동 조직화하는 시스템을 제안한다. 이를 통해 연구자들이 수백 개의 문서를 직관적으로 탐색할 수 있도록 한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Scientific_Question_Answering"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Smits et al._2024_Knowledge navigator Llm-guided browsing framework for exploratory search in scientific literature.pdf"
---

# Knowledge Navigator: LLM-guided Browsing Framework for Exploratory Search in Scientific Literature

> **저자**: Uri Katz, Mosh Levy, Yoav Goldberg (Bar-Ilan University, Allen Institute for AI) | **날짜**: 2024 | **DOI**: [arXiv:2408.15836](https://arxiv.org/abs/2408.15836)

---

## Essence

![Figure 1](figures/fig1.webp)
*"Tool Use in Animals" 쿼리에 대해 생성된 계층적 지식 맵으로, 주요 주제와 하위 주제들을 체계적으로 조직화함*

대규모 과학 문헌에서 탐색적 검색을 지원하기 위해 LLM과 클러스터링 기법을 결합하여 검색 결과를 2단계 계층 구조의 주제로 자동 조직화하는 시스템을 제안한다. 이를 통해 연구자들이 수백 개의 문서를 직관적으로 탐색할 수 있도록 한다.

## Motivation

- **Known**: 전통적 검색 엔진은 특정 쿼리에 최적화되어 있으나, 광범위한 주제 검색 시 수백~수천 개의 관련 논문들을 랭크 리스트 형태로 제시하여 정보 과부하 발생
- **Gap**: 과거 클러스터 기반 탐색 연구(Scatter/Gather 등)는 문서 표현의 부족함, 낮은 해석 가능성으로 인해 실무 채택 실패
- **Why**: 과학자들의 실제 문헌 검색 행동은 "탐색적 검색(exploratory search)"으로, 여러 관점에서 도메인 구조를 이해하고 부분 주제를 발견하려는 욕구를 가짐
- **Approach**: 최신 LLM의 고급 텍스트 이해 능력과 현대적 NLP/IR 기법을 활용하여 클러스터 기반 네비게이션을 재구현

## Achievement

![Figure 2](figures/fig2.webp)
*Knowledge Navigator 워크플로우: 검색 결과 임베딩 및 클러스터링 → 클러스터 판독기를 통한 설명/명명 → 주제 조직화 → 부분주제 확장*

1. **효과적인 계층 구조 생성**: 광범위한 쿼리(예: "Tool Use in Animals")에 대해 신뢰성 높은 2단계 주제 계층을 자동 생성하며, 각 부분주제는 구체적인 문서들로 근거화됨

2. **평가 벤치마크 구축 및 검증**: 
   - CLUSTREC-COVID: TREC-COVID 벤치마크를 부분주제 클러스터링, 클러스터 기반 측면 생성, 쿼리 생성 작업에 맞게 개선
   - SCITOC: Annual Reviews 저널의 목차에서 추출한 과학 분야별 새로운 데이터셋 구축
   - 자동 평가 및 도메인 전문가 평가 모두에서 각 컴포넌트 성능 입증

3. **다양한 모델 호환성**: GPT-4o(독점) 및 Mixtral-8x7B(오픈소스) 포함 여러 LLM에서 실행 가능함을 시연

## How

![Figure 2](figures/fig2.webp)

**시스템 5단계 아키텍처**:

1. **주제 코퍼스 구성**: 검색 엔진(Google Scholar 등)에서 광범위한 쿼리(T)에 대해 상위 K개 문서(최대 1000개) 수집

2. **임베딩 및 클러스터링**: 
   - 문맥 임베딩(contextual embeddings)을 활용한 저비용 연산
   - 코퍼스를 응집력 있는 소규모 부분주제 그룹으로 분할

3. **클러스터 판독기(Cluster Reader)**: 
   - 각 클러스터를 개별적으로 LLM에 입력
   - 공통 주제 분석, 설명 생성, 명명, 관련성 점수 부여

4. **주제 조직화**: 
   - 관련성 필터링을 통과한 모든 클러스터 명칭과 설명을 2차 LLM에 입력
   - 클러스터들을 주제별 그룹으로 조직화하여 계층 구조 형성

5. **부분주제 확장기(Subtopic Expander)**: 
   - 사용자가 선택한 부분주제에 대해 세분화된 추가 문서 검색을 위한 쿼리 자동 생성

**설계 원칙**:
- LLM 호출 최소화 및 효율성 극대화 (비용 제약 고려)
- 하향식(bottom-up) 정보 추상화로 각 단계에서 입력 크기 감소
- 클러스터링은 전역 연산, 명명은 클러스터별이지만 쿼리와 다수 문서 고려
- 최종 조직화는 모든 필터링된 클러스터의 전역 관점 제공

## Originality

- **LLM 기반 클러스터 네비게이션의 재구현**: 과거 실패한 클러스터 기반 탐색 방식을 현대적 LLM으로 효과적으로 부활시킨 첫 사례

- **구조화된 다단계 아키텍처**: 임베딩-클러스터링부터 계층 조직화까지 각 단계를 체계적으로 설계하여 대규모 코퍼스 처리 가능

- **새로운 평가 벤치마크**: CLUSTREC-COVID과 SCITOC 두 개의 새로운 데이터셋 공개로 향후 연구 자산 제공

- **문서 기반 근거화(grounding)**: 매개변수 지식에만 의존하지 않고 쿼리에서 나온 실제 문서들로 모든 출력을 근거화

- **공개 자료 제공**: 코드, 프롬프트, 벤치마크, Streamlit 앱 공개로 재현성 및 확장성 강화

## Limitation & Further Study

- **계산 비용 논의 부족**: 실제 운영 환경에서 1000개 문서 처리 시 LLM 호출 수와 비용에 대한 구체적 분석 부재

- **클러스터링 방법의 제한성**: 임베딩과 클러스터링 전 단계가 비교적 기존 방식(clustering algorithms)을 사용하며, 이 부분의 성능이 전체 결과에 미치는 영향 분석 부족

- **도메인 다양성**: 평가가 COVID-19 관련 문헌과 Annual Reviews 저널에 주로 집중되어 다양한 과학 분야에 대한 일반화 가능성 검증 부족

- **사용자 상호작용 메커니즘**: 부분주제 확장 후 재귀적 탐색, 사용자 피드백 반영 메커니즘 등에 대한 실제 사용자 연구 부재

- **후속 연구 방향**:
  - 다양한 도메인 및 언어에 대한 확장 가능성 검증
  - 실제 사용자 스터디를 통한 상호작용 방식 개선
  - 부분주제 간 관계(연결성) 시각화 및 탐색
  - 증분(incremental) 업데이트 및 문서 추가에 따른 계층 구조 동적 변화 처리


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 5/5
- Overall: 4/5

**총평**: 본 논문은 대규모 과학 문헌의 탐색적 검색을 위해 LLM을 활용한 실용적이고 효과적인 시스템을 제시하며, 새로운 벤치마크와 공개 자료를 제공하여 향후 연구의 토대를 마련한다. 다만 기술적 혁신성은 중간 수준이고 사용자 연구를 통한 실제 효과성 검증이 부족한 점이 아쉽다.

## Related Papers

- 🔄 다른 접근: [[papers/602_Paperqa_Retrieval-augmented_generative_agent_for_scientific/review]] — 과학 문헌 탐색에서 LLM 가이드 클러스터링과 검색 증강 생성 에이전트의 서로 다른 조직화 방법을 비교할 수 있습니다.
- 🏛 기반 연구: [[papers/402_Hierarchical_catalogue_generation_for_literature_review_a_be/review]] — 계층적 카탈로그 생성의 구조적 접근법이 LLM 가이드 탐색 프레임워크의 조직화 기반을 제공합니다.
- 🔗 후속 연구: [[papers/174_Browsecomp_A_simple_yet_challenging_benchmark_for_browsing_a/review]] — 단순한 브라우징 과제를 대규모 과학 문헌의 체계적 탐색으로 확장한 고도화된 시스템입니다.
- 🔗 후속 연구: [[papers/042_Academicbrowse_Benchmarking_academic_browse_ability_of_llms/review]] — LLM 기반 탐색적 검색 프레임워크로 ScholarSearch 벤치마크의 실제 활용 사례를 제시한다.
- 🔗 후속 연구: [[papers/312_Empowering_language_models_with_active_inquiry_for_deeper_un/review]] — 능동적 질의가 LLM 기반 탐색적 브라우징으로 확장됩니다.
- 🔗 후속 연구: [[papers/063_Agent-enhanced_large_language_models_for_researching_politic/review]] — CongressRA의 정치기관 연구 지원은 Knowledge Navigator의 탐색적 지식 발견 프레임워크를 정치학 도메인에 특화시켜 체계적인 연구 도구로 발전시킵니다.
- 🔗 후속 연구: [[papers/874_WebWatcher_Breaking_New_Frontier_of_Vision-Language_Deep_Res/review]] — LLM 가이드 웹 브라우징 프레임워크에서 비전-언어 통합으로 확장된 탐색 능력을 보여준다.
- 🔗 후속 연구: [[papers/174_Browsecomp_A_simple_yet_challenging_benchmark_for_browsing_a/review]] — LLM 가이드 브라우징 프레임워크의 성능을 체계적으로 평가할 수 있는 도전적인 벤치마크를 제공합니다.
- 🔄 다른 접근: [[papers/402_Hierarchical_catalogue_generation_for_literature_review_a_be/review]] — 문헌 탐색에서 계층적 카탈로그 구조와 LLM 가이드 클러스터링의 서로 다른 조직화 방식을 비교할 수 있습니다.
