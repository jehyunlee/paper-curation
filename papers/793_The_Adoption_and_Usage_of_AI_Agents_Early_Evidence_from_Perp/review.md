---
title: "793_The_Adoption_and_Usage_of_AI_Agents_Early_Evidence_from_Perp"
authors:
  - "Jeremy Yang"
  - "Noah Yonack"
  - "Kate Zyskowski"
  - "Denis Yarats"
  - "Johnny Ho"
date: "2025.12"
doi: "10.48550/arXiv.2512.07828"
arxiv: ""
score: 4.5
essence: "본 논문은 Perplexity의 AI 브라우저 Comet과 그 내장 에이전트인 Comet Assistant를 통해 수억 건의 사용자 상호작용을 분석한 첫 번째 대규모 현장 연구로서, AI 에이전트의 채택, 사용 강도, 그리고 구체적인 활용 사례를 체계적으로 규명한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/AI_in_Scientific_Research"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yang et al._2025_The Adoption and Usage of AI Agents Early Evidence from Perplexity.pdf"
---

# The Adoption and Usage of AI Agents: Early Evidence from Perplexity

> **저자**: Jeremy Yang, Noah Yonack, Kate Zyskowski, Denis Yarats, Johnny Ho, Jerry Ma | **날짜**: 2025-12-10 | **DOI**: [10.48550/arXiv.2512.07828](https://doi.org/10.48550/arXiv.2512.07828)

---

## Essence

본 논문은 Perplexity의 AI 브라우저 Comet과 그 내장 에이전트인 Comet Assistant를 통해 수억 건의 사용자 상호작용을 분석한 첫 번째 대규모 현장 연구로서, AI 에이전트의 채택, 사용 강도, 그리고 구체적인 활용 사례를 체계적으로 규명한다.

## Motivation

- **Known**: AI 에이전트는 이론적 구성에서 실제 상용화된 보조 도구로 진화하고 있으며, 전문가 설문이나 코딩 보조 도구 같은 특화된 에이전트에 대한 연구만 존재함
- **Gap**: 일반 목적의 AI 에이전트가 실제로 어떻게 채택되고 사용되는지에 관한 체계적인 행동 증거가 부재함
- **Why**: 글로벌 에이전틱 AI 시장이 2025년 80억 달러에서 2034년 1,990억 달러로 성장할 것으로 예상되는 만큼, 실제 사용 패턴 이해가 연구자, 기업, 정책입안자, 교육자에게 필수적
- **Approach**: 2025년 7월 9일부터 10월 22일 사이에 수집한 Comet 데스크톱 사용자 데이터(수억 건의 쿼리)를 분석하여 세 가지 근본적인 질문에 답함: (1) 누가 AI 에이전트를 사용하는가? (2) 얼마나 강하게 사용하는가? (3) 무엇을 위해 사용하는가?

## Achievement

![Figure 1: Hierarchical Structure of the Agentic Taxonomy](figures/fig1.webp)
*에이전틱 분류체계의 계층적 구조: 주제(Topic) → 소주제(Subtopic) → 작업(Task) → 환경(Environment)*

1. **채택 및 사용 강도의 이질성 규명**: 
   - 초기 채택자(Early adopters)는 GA 사용자보다 에이전트 채택 확률이 2배 높고, 에이전틱 쿼리는 9배 많음
   - 국가별 수준에서는 1인당 GDP와 평균 교육 년수와 강한 양의 상관관계 확인
   - 직업별로는 디지털 기술(28%), 학술(academia), 금융, 마케팅, 창업 등 지식집약적 분야가 전체 채택자와 쿼리의 70% 이상 차지

2. **계층적 에이전틱 분류체계 개발 및 사용 사례 분류**:
   - 생산성&워크플로우(36%)와 학습&연구(21%)가 모든 에이전틱 쿼리의 57% 차지
   - 소주제 수준에서는 온라인 강좌(13%), 상품 쇼핑(9%), 연구(8%), 문서 편집(8%), 계정 관리(7%), 소셜 미디어(7%)가 주요 항목
   - 개인 용도(55%), 전문적 용도(30%), 교육적 용도(16%) 비율 파악
   - 단기적으로는 사용 사례가 강한 점착성(stickiness)을 보이지만, 시간이 경과하면서 더 인지적으로 지향된 주제로 이동하는 경향 관찰

## How

![Figure 4: Topic Breakdown by Subtopic Percentage](figures/fig4.webp)
*주제별 소주제 비율 분석: 생산성, 학습, 미디어, 쇼핑 간 상대적 비중*

- **데이터 수집 및 샘플링**: 
  - 전체 Comet 사용자 및 쿼리에 대한 익명화된 데이터(수백만 사용자, 수억 쿼리)
  - 임의 추출 100,000 Comet 사용자를 O*NET 직업 클러스터로 분류
  - 별도 임의 추출 100,000 에이전트 사용자의 모든 에이전틱 쿼리를 계층적 분류체계로 분류

- **분류 및 분석 방법**:
  - ReAct 프레임워크를 기반으로 한 에이전틱 워크플로우 이해(Think → Act → Observe 순환)
  - 신규 개발한 3단계 계층적 분류체계(주제-소주제-작업-환경) 적용
  - 국가, 직업, 시간대별 변이 분석 및 주제 전환 패턴 추적

- **기술적 특징**:
  - Comet Assistant는 웹 기반 개방형 환경에서 다중 단계 작업 계획 및 실행 가능
  - 스케줄링, 문서 편집, 이메일 송신, 항공편 예약, 구매 등 다양한 도구 활용 능력

## Originality

- **최초성**: 개방형 웹 환경에서 작동하는 일반 목적 AI 에이전트의 대규모 현장 연구로서 선구적 기여
- **분류체계 개발**: 에이전트 사용 사례를 체계적으로 특성화하기 위한 새로운 계층적 분류 프레임워크 제시
- **행동 데이터 기반**: 비대표성 설문 조사에 의존하지 않고 수억 건의 실제 사용자 상호작용 분석
- **다차원 분석**: 채택, 사용 강도, 사용 사례, 지리적/직업적 이질성, 시간적 동역학을 통합적으로 조사
- **정책 적절성**: 연구자, 기업, 정책입안자, 교육자 모두를 위한 실증적 기초 제공

## Limitation & Further Study

- **데이터 범위 한계**: 
  - Comet 데스크톱 사용자만 대상 (모바일 미포함)
  - 2025년 7월-10월 초기 단계 데이터로서 장기 추세 반영 부족
  - 구독자 기반 사용자 집단(초기에 Max 티어, 이후 Pro, 최종적으로 전체)의 선택 편향 가능성
  - 익명화된 데이터로 인한 개별 사용자 추적 불가능

- **분류체계 한계**:
  - 수동 분류의 주관성 가능성 (신뢰도 검증 미제시)
  - 다중 목적의 쿼리 분류 방식 명확화 필요

- **후속 연구 방향**:
  - AI 에이전트 사용이 사용자 생산성, 학습 성과, 노동 시장에 미치는 인과적 영향 평가
  - 에이전트 실패, 오류, 사용자 신뢰도 등 부작용 분석
  - 다양한 에이전트 플랫폼(OpenAI Operator, Claude Computer Use 등) 간 비교
  - 기업 및 조직 수준의 에이전트 도입 영향 연구
  - 에이전트 사용과 불평등, 일자리, 교육 기회의 관계 규명

## Evaluation

- **Novelty**: 5/5 - 개방형 환경의 일반 목적 AI 에이전트 최초 대규모 현장 연구이며 새로운 분류체계 제시
- **Technical Soundness**: 4/5 - 대규모 실제 데이터 기반 분석이지만 분류 방법론의 신뢰도/타당도 검증 상세 부족
- **Significance**: 5/5 - 에이전틱 AI의 급속한 상용화 시점에 정책, 기업, 학술 의사결정에 직접적 영향을 줄 수 있는 연구
- **Clarity**: 4/5 - 계층적 분류체계가 명확하게 제시되었으나 일부 기술적 세부사항과 분류 기준 설명 강화 필요
- **Overall**: 4.5/5

**총평**: 본 논문은 AI 에이전트의 실제 채택 및 사용 패턴에 관한 첫 번째 체계적 증거를 제시함으로써 급속히 성장하는 에이전틱 AI 분야에 중요한 경험적 기초를 마련한다. 다만 초기 단계 특정 플랫폼 데이터라는 한계를 고려하여 인과 관계 및 장기 영향 연구가 후속되어야 한다.

## Related Papers

- 🔗 후속 연구: [[papers/280_Divergent_llm_adoption_and_heterogeneous_convergence_paths_i/review]] — ChatGPT 이후 학술 글쓰기 변화 연구를 AI 에이전트 실제 사용 패턴으로 확장하여 더 구체적인 사용자 행동 분석을 제공합니다.
- 🧪 응용 사례: [[papers/174_Browsecomp_A_simple_yet_challenging_benchmark_for_browsing_a/review]] — AI 에이전트 사용 패턴 연구의 실제 평가를 위한 도전적인 웹 브라우징 벤치마크를 제공합니다.
- 🏛 기반 연구: [[papers/813_Toolformer_Language_Models_Can_Teach_Themselves_to_Use_Tools/review]] — 언어모델의 도구 사용 학습 연구가 AI 에이전트 채택과 활용 사례 분석의 기술적 배경을 제공합니다.
- 🔗 후속 연구: [[papers/365_Future_of_Work_with_AI_Agents_Auditing_Automation_and_Augmen/review]] — 개인 사용자 관점에서 AI 에이전트 채택과 사용에 대한 초기 증거를 확장하여 제시한다.
- 🔗 후속 연구: [[papers/280_Divergent_llm_adoption_and_heterogeneous_convergence_paths_i/review]] — ChatGPT 이후 학술글쓰기 변화를 대규모 분석한 연구로서 AI 에이전트 사용 패턴 연구의 확장된 관점을 제공합니다.
- 🏛 기반 연구: [[papers/107_Artificial_intelligence_tools_expand_scientists_impact_but_c/review]] — AI 에이전트의 개인 차원에서의 채택과 사용에 대한 초기 증거로 본 연구의 개별 과학자 영향 분석 기반을 제공한다.
- 🔄 다른 접근: [[papers/174_Browsecomp_A_simple_yet_challenging_benchmark_for_browsing_a/review]] — 웹 에이전트 평가를 위한 벤치마크로서 AI 에이전트 사용 패턴 연구와 상호 보완적인 평가 관점을 제시합니다.
- 🔗 후속 연구: [[papers/813_Toolformer_Language_Models_Can_Teach_Themselves_to_Use_Tools/review]] — 도구 사용 학습 모델에서 실제 AI 에이전트 사용 패턴과 채택 현황으로 확장한 실증적 연구입니다.
