---
title: "442_Iris_Interactive_research_ideation_system_for_accelerating_s"
authors:
  - "Aniketh Garikaparthi"
  - "Manasi Patwardhan"
  - "Lovekesh Vig"
  - "Arman Cohan"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "LLM의 자동화 능력을 활용하면서도 연구자의 투명한 제어와 감시를 가능하게 하는 인터랙티브 연구 아이디어 생성 시스템 IRIS를 제안하며, Monte Carlo Tree Search(MCTS) 기반의 적응형 탐색과 세분화된 피드백 메커니즘을 통해 과학적 가설 생성을 가속화한다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Scientific_Hypothesis_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Garikaparthi et al._2025_Iris Interactive research ideation system for accelerating scientific discovery.pdf"
---

# Iris: Interactive research ideation system for accelerating scientific discovery

> **저자**: Aniketh Garikaparthi, Manasi Patwardhan, Lovekesh Vig, Arman Cohan | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) *Human-in-the-loop Idea Generation with Monte-Carlo-Tree-Search*

LLM의 자동화 능력을 활용하면서도 연구자의 투명한 제어와 감시를 가능하게 하는 인터랙티브 연구 아이디어 생성 시스템 IRIS를 제안하며, Monte Carlo Tree Search(MCTS) 기반의 적응형 탐색과 세분화된 피드백 메커니즘을 통해 과학적 가설 생성을 가속화한다.

## Motivation

- **Known**: LLM 기반 자동 가설 생성 연구가 확대되고 있으며, 최근 다중 에이전트 프레임워크와 확장된 테스트-타임 계산이 제안되고 있음
- **Gap**: 기존 방식들은 (1) 단일 패스 생성으로 반복적 개선 부재, (2) 추상적 피드백만 제공, (3) 단순 RAG 기반 문헌 검색, (4) 비효율적 아이디어 공간 탐색, (5) 오픈소스 구현 부재 등의 문제 존재. 더 근본적으로, 인간 감시의 부재로 인해 "보상 해킹(reward hacking)", 가짜 정보 생성, 표절 등의 위험성 존재
- **Why**: 과학적 발견의 초기 단계인 가설 생성에서 LLM의 자동화와 인간의 지능을 진정한 상호보완적 방식으로 결합할 필요성이 절실함. 연구자의 목표와 일치하고 투명하며 조정 가능한 시스템이 필수적
- **Approach**: Human-in-the-Loop(HITL) 프레임워크와 MCTS 기반 체계적 탐색, 세분화된 피드백 분류체계, 쿼리 기반 문헌 합성을 통합한 대화형 플랫폼 개발

## Achievement

![Figure 2](figures/fig2.webp) *IRIS Platform Interface with Retrieval Panel, Chat Overview Panel, Research Brief Panel*

1. **HITL 프레임워크**: 완전 자동화를 피하고 계획(planning), 생성(generation), 회고(retrospection) 단계 전반에서 연구자 개입을 가능하게 하는 사용자 중심 설계 구현

2. **세분화된 평가 및 피드백**: 실제 과학적 비평에 기반한 위계적 분류체계(Table 2)를 통해 연구 브리프의 특정 부분(제목, 방법론, 실험 계획)에 대한 실행 가능한 피드백 제공, 연구자 검증을 통해 보상 해킹 방지

3. **MCTS 기반 아이디어 공간 탐색**: 탐색(exploration)과 활용(exploitation) 단계를 체계적으로 교대하며 테스트-타임 계산 확장, 주관적 품질 평가가 가능하도록 LLM 기반 리뷰 에이전트를 보상 대리자로 활용

4. **지능형 문헌 검색**: ScholarAI 기반의 쿼리 생성, 다단계 재순위화, 클러스터링, 인용 기반 요약을 통한 포괄적 기술 문서 제공

5. **오픈소스 플랫폼**: 학계 채택을 촉진하는 공개 구현

## How

![Figure 3](figures/fig3.webp) *Iterative improvement in hypothesis quality*

**시스템 아키텍처**:
- **아이디어 에이전트(Ideation Agent)**: 반자동 모드(연구자 지도)와 완전 자동 모드(MCTS 기반 탐색) 간 전환 가능
- **리뷰 에이전트(Review Agent)**: 
  - 자동 트리거 모드: 각 생성 후 전체 브리프에 대해 평균 점수 계산
  - 세분화 모드: 연구자 요청 시 분류체계의 각 측면별로 특정 부분에 대한 상세 피드백 제공
- **검색 에이전트(Retrieval Agent)**:
  - Semantic Scholar API 활용 (2억 건 이상 논문)
  - 2단계 검색(스니펫 추출 → 재순위화) + 3단계 생성(인용 추출 → 계획 생성 → 섹션별 보고서 생성)

**MCTS 적응**:
- 상태 s: {현재 연구 브리프 b, 컨텍스트 c}로 정의
- 객관적 보상이 없는 주관적 품질 평가 영역에서 LLM 기반 리뷰 에이전트를 보상 함수로 사용
- 탐색-활용 균형을 통한 아이디어 다양성과 품질 동시 추구

## Originality

- **HITL 설계 원칙 체계화**: 단순 검증 단계의 인간 개입을 넘어 생성 과정 전반에 걸친 상호작용 설계로, 기존 완전 자동 시스템의 한계(보상 해킹, 표절 등) 직접 해결
- **세분화된 피드백 분류체계**: 전체 아이디어에 대한 추상적 평가를 벗어나 연구 브리프의 구체적 구성 요소별 실행 가능한 피드백 제공
- **과학적 아이디어이션에 특화된 MCTS 적용**: 객관적 보상이 존재하지 않는 창의적 작업에 MCTS를 적응시키기 위해 LLM을 판정자로 사용
- **지능형 문헌 합성**: 단순 키워드 기반 RAG를 넘어 대화형 쿼리 생성, 재순위화, 클러스터링, 인용 추적이 통합된 포괄적 문헌 검색

## Limitation & Further Study

- **주관적 보상 문제**: MCTS에서 LLM 기반 리뷰 에이전트를 보상 대리자로 사용하는 것이 실제 연구자의 선호도와 완벽히 일치하는지 검증 필요
- **확장성 평가 부재**: 극도로 새로운 영역이나 학제간 연구에서의 성능에 대한 분석 부족
- **계산 비용**: MCTS 기반 탐색과 다중 에이전트 운영으로 인한 계산 오버헤드 정량화 필요
- **후속 연구**: 
  - 다양한 학문 분야에 걸친 광범위한 사용자 연구 확대
  - 생성된 가설의 실제 과학적 타당성에 대한 장기 추적 연구
  - 인간 피드백 루프의 최적화를 통한 더 효율적인 탐색 전략 개발

## Evaluation

- **Novelty**: 4.5/5 - 완전 자동 시스템의 한계를 직시하고 HITL 원칙을 과학적 아이디어이션에 체계적으로 구현하되, 세분화된 피드백과 MCTS 적응은 창의적이나 각 요소 자체는 기존 아이디어의 조합

- **Technical Soundness**: 4/5 - 세 개 에이전트의 아키텍처는 명확하고 MCTS 적응도 합리적이나, 주관적 보상 평가의 안정성과 신뢰성에 대한 이론적 분석 부족

- **Significance**: 4/5 - 과학적 발견의 초기 단계에 LLM을 실질적으로 활용하기 위한 중요한 제시이며 오픈소스 공개로 학계 기여도 높으나, 사용자 연구 규모와 다양한 학문 분야 검증이 제한적

- **Clarity**: 4.5/5 - 시스템 개요와 동기는 명확하게 설명되었으나, 본문 앞부분에서 완전한 기술 설명(특히 MCTS 형식화)이 제공되지 않음

- **Overall**: 4.2/5

**총평**: IRIS는 LLM 기반 과학적 발견 가속화라는 중요한 과제에서 완전 자동화의 함정을 인식하고 투명성과 조정 가능성을 갖춘 HITL 시스템으로 실질적 해결책을 제시한다. 세분화된 피드백과 MCTS 기반 탐색은 기술적으로 창의적이며, 오픈소스 공개는 높이 평가되나, 사용자 연구의 범위 확대와 다양한 학문 영역에서의 검증이 더 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/847_Two_heads_are_better_than_one_A_multi-agent_system_has_the_p/review]] — 단일 연구자 대상 인터랙티브 시스템 vs 다중 에이전트 협력 시스템의 대조적 접근
- 🏛 기반 연구: [[papers/417_HypoBench_Towards_Systematic_and_Principled_Benchmarking_for/review]] — 가설 생성 벤치마킹 기준을 실제 시스템 개발에 적용한 사례
- 🔗 후속 연구: [[papers/728_SciMON_Scientific_Inspiration_Machines_Optimized_for_Novelty/review]] — MCTS 기반 적응형 탐색을 참신성 최적화로 발전시킨 연구
- 🧪 응용 사례: [[papers/725_Sciidea_Context-aware_scientific_ideation_using_token_and_se/review]] — 토큰 기반 아이디어 생성 방법론을 인터랙티브 환경으로 확장한 응용
- 🔄 다른 접근: [[papers/847_Two_heads_are_better_than_one_A_multi-agent_system_has_the_p/review]] — 다중 에이전트 협력 시스템 vs 단일 연구자 대상 인터랙티브 시스템의 대조적 접근
- 🔗 후속 연구: [[papers/417_HypoBench_Towards_Systematic_and_Principled_Benchmarking_for/review]] — 가설 생성 벤치마크를 실제 인터랙티브 연구 시스템으로 구현한 응용 사례
- 🔄 다른 접근: [[papers/045_Acceleron_A_tool_to_accelerate_research_ideation/review]] — 둘 다 연구 아이디어 생성 도구이지만 Acceleron은 LLM 에이전트에, IRIS는 대화형 시스템에 집중하는 차이가 있음
