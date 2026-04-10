---
title: "625_PlanGenLLMs_A_Modern_Survey_of_LLM_Planning_Capabilities"
authors:
  - "Hui Wei"
  - "Zihao Zhang"
  - "Shenghua He"
  - "Tian Xia"
  - "Shijia Pan"
date: "2025"
doi: "10.48550/arXiv.2502.11221"
arxiv: ""
score: 4.2
essence: "본 논문은 대규모 언어 모델(LLM)의 계획 수립(Planning) 능력에 대한 포괄적 조사 연구로, 초기 AI 계획 시스템의 평가 기준을 현대화하여 6가지 핵심 성능 지표를 통해 LLM 기반 계획 수립 시스템을 체계적으로 분석한다. 이를 통해 다양한 도메인에서 LLM 계획 시스템의 비교 평가 틀을 제공하고 향후 연구 방향을 제시한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/AI_Chemistry_Planning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wei et al._2025_PlanGenLLMs A Modern Survey of LLM Planning Capabilities.pdf"
---

# PlanGenLLMs: A Modern Survey of LLM Planning Capabilities

> **저자**: Hui Wei, Zihao Zhang, Shenghua He, Tian Xia, Shijia Pan | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2502.11221](https://doi.org/10.48550/arXiv.2502.11221)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: LLM 계획 수립의 분류체계 - 6가지 핵심 성능 기준과 대표 기법들의 매핑*

본 논문은 대규모 언어 모델(LLM)의 계획 수립(Planning) 능력에 대한 포괄적 조사 연구로, 초기 AI 계획 시스템의 평가 기준을 현대화하여 6가지 핵심 성능 지표를 통해 LLM 기반 계획 수립 시스템을 체계적으로 분석한다. 이를 통해 다양한 도메인에서 LLM 계획 시스템의 비교 평가 틀을 제공하고 향후 연구 방향을 제시한다.

## Motivation

- **Known**: 웹 네비게이션, 여행 계획, 데이터베이스 쿼리 등 다양한 분야에서 LLM 기반 계획 수립 시스템이 활발히 연구되고 있으며, 각 분야마다 개별화된 벤치마크와 평가 방법론이 존재한다.

- **Gap**: 기존 연구들(Huang et al., 2024c; Li et al., 2024d)이 계획 수립 방법론과 평가 벤치마크를 다루었으나, 서로 다른 도메인 간의 LLM 계획 시스템 비교가 어렵고, 명확하고 일관된 평가 기준이 부족하다. 이는 고급 LLM 계획 시스템 개발의 저해 요인으로 작용할 수 있다.

- **Why**: 계획 수립(initial state → goal state로의 행동 순열 생성)은 인간 지능의 핵심 능력이며, 이를 자동화하기 위한 체계적인 평가 프레임워크가 필요하다.

- **Approach**: 1990년 Kartam과 Wilkins의 고전 AI 계획 시스템 평가 기준을 재검토하여, LLM 시대에 맞는 6가지 핵심 성능 기준(완전성, 실행 가능성, 최적성, 표현력, 일반화, 효율성)을 제시하고 각각에 대한 대표 연구들을 분석한다.

## Achievement

1. **6가지 핵심 평가 기준의 체계화**: 
   - **완전성(Completeness)**: 계획 정확성(plan correctness)과 달성 가능성(plan achievability) 평가
   - **실행 가능성(Executability)**: 객체 접지(object grounding), 행동 접지(action grounding), 샘플-필터(sample-then-filter), 폐쇄 루프 시스템(closed-loop systems)
   - **최적성(Optimality)**: LLM+최적화기, A* 탐색 기반 방법론
   - **표현력(Representation)**: LLM-as-a-Translator vs. LLM-as-a-Planner 구분
   - **일반화(Generalization)**: 미세 조정, 일반화된 계획, 기술 저장소 기반 접근
   - **효율성(Efficiency)**: LLM/월드 모델 호출 감소, 입출력 토큰 단축, 소형 모델 활용

2. **포괄적 기법 분류**: 
   - 태스크 분해(sequential, parallel, asynchronous)
   - LLM+고전 계획 수립 하이브리드 방식(LLM+P, LLM-DP 등)
   - 탐색 알고리즘(Tree of Thought, MCTS, Greedy Best-First Search)
   - 미세 조정 기반 접근(RobLM, Agent-FLAN, AgentOhana)

3. **다양한 도메인 평가 자료**: 
   - 구체화 환경(BlocksWorld, ALFRED, VirtualHome, ALFWorld)
   - 작업 스케줄링(TravelPlanner)
   - 게임(MineCraft, SmartPlay)
   - 도구 사용, 프로그래밍, 웹 네비게이션 등 다운스트림 태스크

## How

### LLM 계획 수립 기초 방법론

- **태스크 분해**: 추상적 목표를 구체적 부분목표로 단계적 분해
  - 순차 분해(sequential): 선행 부분목표의 효과가 후행 부분목표의 전제조건
  - 병렬 분해(parallel): 동일 전제조건/효과를 가진 부분목표
  - 비동기 분해(asynchronous): 각 분기의 고유 전제조건/효과를 가진 병렬화

- **LLM+고전 계획 수립 하이브리드**: LLM의 세계 지식과 고전 계획기(Fast Downward, BFS(f))의 정확성 결합
  - PDDL 표현 변환 담당(LLM) → 형식적 계획 생성(고전 계획기)
  - 초기 계획 생성 후 반복적 개선(LPG 플래너)

- **탐색 알고리즘**: 계획을 탐색 문제로 재구성
  - 4가지 핵심 구성요소: (1)탐색 정책(search policy), (2)확장(expansion, 행동 제안), (3)월드 모델(상태 전이), (4)평가(목표 진행도 점수)
  - BFS/DFS, MCTS(Monte Carlo Tree Search), Greedy Best-First Search 등 활용
  - 월드 모델: LLM 기반, 고전 계획기 기반, 외부 환경 시뮬레이터 기반

- **미세 조정**: 매개변수 업데이트를 통한 계획 특화 학습
  - 계획 전용 태스크 또는 광범위 에이전트 능력 미세 조정
  - 프롬프트 기반 방법의 근본적 성능 한계 극복

## Originality

- **고전 AI 계획 기준의 현대화**: 30년 전 Kartam & Wilkins(1990)의 평가 프레임워크를 LLM 시대에 맞게 재검토하여 6가지 실질적 기준 도출
  
- **도메인 횡단적 분석 체계**: 웹 네비게이션부터 로봇 제어까지 다양한 응용 도메인을 통일된 평가 기준으로 분석

- **4가지 LLM 계획 기초 패러다임의 체계적 분류**: 태스크 분해, 하이브리드 계획기, 탐색 알고리즘, 미세 조정을 독립적이면서도 상호보완적으로 분석

- **평가 방법론의 포괄적 정리**: 검증기(verifier), 인간 평가, LLM-as-a-Judge, 메트릭스(성공률, 최적성 비율, 실행 가능성 비율 등) 통합 정리

## Limitation & Further Study

- **표현력 문제(Representation Gap)**: 자연언어와 형식적 계획 표현 간의 의미 손실 문제 미해결 - 더 나은 중간 표현 형식 개발 필요

- **환각(Hallucination) 문제**: LLM이 존재하지 않는 객체/행동을 생성하는 근본적 한계 - 자체 검증 메커니즘 강화 필요

- **정렬(Alignment) 이슈**: LLM의 생성 목표와 계획 과제의 실제 요구사항 간 불일치 - 강화 학습 기반 정렬 기법 탐색 필요

- **다중 에이전트 계획**: 현 연구의 대부분이 단일 에이전트 중심 - 협업, 협상, 갈등 해결 기반의 다중 에이전트 계획 시스템 미발달

- **에이전트 워크플로우 연계**: 계획 수립과 실행, 피드백 루프의 통합 시스템화 부족 - 실시간 환경 변화 대응의 adaptive planning 강화 필요

- **평가 벤치마크 표준화 부족**: 도메인별로 산재된 벤치마크로 인한 공정한 비교 평가의 어려움 - 통일된 평가 프레임워크 개발 필요

## Evaluation

- **Novelty**: 4/5
  - 고전 평가 기준의 현대화는 창의적이나, 개별 기법들의 분류는 기존 연구를 정리하는 수준

- **Technical Soundness**: 4.5/5
  - 6가지 기준의 정의와 분류가 명확하고 논리적이며, 대표 연구들의 선정이 적절함

- **Significance**: 4.5/5
  - LLM 계획 분야의 체계적 조사로서 연구자들에게 실질적 가치 제공, 향후 연구 방향 제시

- **Clarity**: 4/5
  - 분류체계(Figure 1)가 명확하고 각 섹션의 구성이 체계적이나, 15,000자 범위 내 세부 내용의 깊이 제한

- **Overall**: 4.2/5

**총평**: 본 논문은 LLM 계획 수립 분야의 현황을 포괄적으로 정리한 중요한 조사 논문으로, 고전 AI 계획 평가 기준을 현대화하여 도메인 횡단적 비교 분석 틀을 제공한다. 다만 새로운 방법론 제안보다는 기존 연구의 체계적 분류에 중점을 두고 있으며, 표현력, 환각, 다중 에이전트 계획 등 미해결 문제들을 향후 연구 과제로 명확히 제시함으로써 학계의 관심을 유도하는 데 효과적이다.

## Related Papers

- 🏛 기반 연구: [[papers/033_A_survey_on_large_language_model_based_autonomous_agents/review]] — 대규모 언어모델 기반 자율 에이전트 조사는 LLM 계획 수립 능력 분석의 이론적 기반을 제공합니다
- 🔄 다른 접근: [[papers/854_Understanding_the_planning_of_LLM_agents_A_survey/review]] — LLM 에이전트 계획 이해에 대한 조사와 LLM 계획 능력의 현대적 조사는 상호 보완적인 관점을 제공합니다
- 🔗 후속 연구: [[papers/464_Large_Language_Model_based_Multi-Agents_A_Survey_of_Progress/review]] — 멀티 에이전트 기반 대형 언어모델의 진전 조사는 개별 LLM의 계획 능력을 다중 에이전트 환경으로 확장한 연구입니다
- 🔄 다른 접근: [[papers/854_Understanding_the_planning_of_LLM_agents_A_survey/review]] — LLM 계획 능력에 대한 현대적 조사와 LLM 에이전트 계획의 이해 모두 동일한 주제를 다루지만 접근 관점이 다르다.
- 🔗 후속 연구: [[papers/249_Curriculum_Reinforcement_Learning_from_Easy_to_Hard_Tasks_Im/review]] — LLM 계획 능력에 대한 현대적 조사는 E2H Reasoner의 커리큘럼 기반 계획 학습 접근방식을 더 넓은 맥락에서 이해할 수 있게 한다.
- 🏛 기반 연구: [[papers/842_Tree-planner_Efficient_close-loop_task_planning_with_large_l/review]] — LLM의 계획 생성 능력에 대한 포괄적 조사로 Tree-planner의 이론적 기반을 제공한다.
