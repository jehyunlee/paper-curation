---
title: "842_Tree-planner_Efficient_close-loop_task_planning_with_large_l"
authors:
  - "Mengkang Hu"
  - "Yao Mu"
  - "Xinmiao Yu"
  - "Mingyu Ding"
  - "Shiguang Wu"
date: "2023"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "대규모 언어모델(LLM)을 활용한 폐루프 태스크 플래닝에서 토큰 효율성과 오류 수정 효율성을 동시에 개선하는 TREE-PLANNER를 제안한다. 기존의 반복적 플래닝(iterative planning) 대신 계획 샘플링-액션 트리 구성-그라운디드 의사결정의 3단계로 재구조화하여 토큰 소비 92.2% 감소와 오류 수정 40.5% 감소를 달성한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/AI-Powered_Research_Planning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Hu et al._2023_Tree-planner Efficient close-loop task planning with large language models.pdf"
---

# Tree-planner: Efficient close-loop task planning with large language models

> **저자**: Mengkang Hu, Yao Mu, Xinmiao Yu, Mingyu Ding, Shiguang Wu, Wenqi Shao, Qiguang Chen, Bin Wang, Yu Qiao, Ping Luo | **날짜**: 2023 | **DOI**: N/A

---

## Essence

![Figure 2](figures/fig2.webp)
*TREE-PLANNER의 3단계 파이프라인: (I) 실행 전 잠재적 계획 샘플링, (II) 샘플링된 계획들을 집계하여 액션 트리 구성, (III) 폐루프에서 LLM이 액션 트리 상에서 의사결정*

대규모 언어모델(LLM)을 활용한 폐루프 태스크 플래닝에서 토큰 효율성과 오류 수정 효율성을 동시에 개선하는 TREE-PLANNER를 제안한다. 기존의 반복적 플래닝(iterative planning) 대신 계획 샘플링-액션 트리 구성-그라운디드 의사결정의 3단계로 재구조화하여 토큰 소비 92.2% 감소와 오류 수정 40.5% 감소를 달성한다.

## Motivation

- **Known**: 최근 LLM 기반 태스크 플래닝은 각 타임스텝마다 LLM을 반복 호출하여 액션을 생성하는 반복적 플래닝(ITERATIVE-PLANNER) 패러다임이 주류이다. 이 방식에서 오류 발생 시 LOCAL REPLAN(현재 타임스텝 재생성) 또는 GLOBAL REPLAN(전체 계획 재생성)으로 대응한다.

- **Gap**: ITERATIVE-PLANNER는 두 가지 근본적 비효율성을 가진다: (1) 토큰 비효율성 - 환경 정보, 문맥 예시 등의 프롬프트 토큰이 매 단계마다 반복되어 비용이 급증하며, (2) 수정 비효율성 - LOCAL REPLAN은 과거 오류를 감지하기 어렵고, GLOBAL REPLAN은 전체 계획을 재생성해야 해 시간과 토큰이 낭비된다.

- **Why**: 현대의 응용에서 대규모 추론(large-scale inference)과 빈번한 사용을 고려할 때, 토큰 효율성과 수정 효율성 개선이 시급하다.

- **Approach**: 계획 샘플링(단일 LLM 호출)과 그라운디드 의사결정(반복 호출)으로 쿼리를 분리하고, 이를 액션 트리로 연결하여 더 유연한 백트래킹(backtracking)을 가능하게 한다.

## Achievement

![Figure 1](figures/fig1.webp)
*기존 반복적 플래닝 패러다임의 개요*

1. **토큰 효율성**: ITERATIVE-PLANNER 대비 53.29%, LOCAL REPLAN 대비 74.36%, GLOBAL REPLAN 대비 92.24% 토큰 소비 감소. 환경 정보와 문맥 예시가 계획 샘플링 단계에서 단 1회만 청구되기 때문.

2. **수정 효율성**: LOCAL REPLAN 대비 37.99%, GLOBAL REPLAN 대비 40.52% 오류 수정 횟수 감소. 액션 트리의 백트래킹으로 불필요한 재결정 감소.

3. **성능**: VirtualHome 환경에서 수정 없는 설정(no correction)에서 기존 최고 성능 대비 3.65%, 수정 있는 설정(with correction)에서 1.29% 향상.

## How

![Figure 3](figures/fig3.webp)
*액션 트리 구성 프로세스: 샘플링된 계획들의 공통 프리픽스를 집계하여 트리 구조로 변환*

**Stage I. 계획 샘플링 (Plan Sampling)**
- LLM(ρ_ps, g) = {c₁, c₂, ..., c_N}을 통해 N개의 잠재적 계획을 단일 호출로 샘플링
- 프롬프트 구성: 명령어(instruction), 환경 정보(global information), 초기 관찰(initial observation), 문맥 예시(in-context examples)
- LLM의 상식 지식을 먼저 추출하는 단계로, 실행 전 다양한 계획 후보 생성

**Stage II. 액션 트리 구성 (Action Tree Construction)**
- 샘플링된 계획들의 공통 프리픽스를 식별하고 집계
- 동일한 초기 액션 시퀀스를 공유하는 계획들의 중복을 제거하며 트리 구조로 병합
- 이를 통해 계획들 간의 공통성을 활용하고 의사결정 공간을 체계화

**Stage III. 그라운디드 의사결정 (Grounded Deciding)**
- 폐루프: 환경 관찰을 받아 액션 트리를 top-down 방식으로 탐색
- 각 타임스텝에서 현재 노드의 자식 노드(가능한 다음 액션) 중 최적을 선택
- 액션 실패 시 해당 노드를 무효 표시하고 백트래킹하여 대체 경로 탐색
- 부분 관찰 가능 마르코프 결정 과정(POMDP) 프레임워크에서 최적 정책 π(a_t|g, h_t, o_t) 추구

**핵심 메커니즘**
- 토큰 효율: 환경 설명과 예시 토큰이 계획 샘플링에서만 청구되고, 그라운디드 의사결정에서는 더 간결한 프롬프트 사용
- 수정 효율: 로컬 재계획(LOCAL)보다 조정 범위가 크고, 글로벌 재계획(GLOBAL)보다 비용이 적은 중간 지점 제공

## Originality

- **새로운 태스크 플래닝 패러다임**: 기존의 순차적 액션 생성에서 벗어나, 계획 샘플링과 의사결정을 명시적으로 분리하는 2단계 쿼리 구조 제시.

- **액션 트리 자료구조**: 여러 계획을 트리로 집계하여 공통 부분을 활용하고, 동적 백트래킹 기반 오류 수정을 가능하게 하는 중간 표현 도입.

- **토큰 효율성의 이론적 검증**: 반복적 플래닝 대비 토큰 효율성의 상한(upper bound)을 형식적으로 도출하고, 샘플링 계획 수의 임계값 분석.

- **폐루프 태스크 플래닝의 실질적 개선**: 단순한 성능 향상을 넘어 실제 응용 가능성을 높이는 효율성 개선에 초점.

## Limitation & Further Study

- **샘플링 다양성의 제한**: 계획 샘플링이 LLM의 고정된 지식에만 의존하므로, 환경의 예기치 않은 상황(예: 일반적이지 않은 객체 배치)에 대응하는 새로운 계획 생성이 제한될 수 있다.

- **액션 트리 규모 증가**: N개 계획이 충분히 다양하면 트리의 깊이와 너비가 급증할 수 있으며, 큰 트리에서의 의사결정 효율성 감소 가능성.

- **VirtualHome 환경의 제약**: 논문이 단일 시뮬레이션 환경(가정 태스크)에서만 평가되었으므로, 로봇 조작, 실제 네비게이션 등 다양한 도메인에서의 일반화 가능성 미검증.

- **오류 분석 부족**: 수동 오류 분석이 언급되었으나 상세 분석 결과가 제한적이며, 어떤 유형의 오류가 개선되었는지, 어떤 오류가 여전히 발생하는지 명확하지 않음.

- **향후 연구 방향**:
  - 동적 환경에서 실시간 계획 샘플링 추가 (현재는 실행 전 고정)
  - 실제 로봇에서의 적용 및 물리적 제약 통합
  - 메모리 효율적인 트리 구조 최적화
  - 다중 에이전트 협력 태스크 플래닝으로 확장

## Evaluation

- **Novelty**: 4/5 - 계획 샘플링과 의사결정의 명시적 분리, 액션 트리 기반 백트래킹은 새롭지만, 기본 아이디어는 기존 방법들의 자연스러운 진화.

- **Technical Soundness**: 4/5 - POMDP 프레임워크 적용, 토큰 효율성 형식 검증, 체계적 실험 설계가 견고하나, 트리 구성 알고리즘의 최적성 증명 부재.

- **Significance**: 4/5 - 토큰 효율 92% 감소는 실질적 영향이 크고, LLM 기반 플래닝의 확장성 문제를 직접 해결하나, 단일 환경 평가의 한계.

- **Clarity**: 4/5 - 파이프라인 3단계가 명확하고 Figure 2가 직관적이나, 일부 형식화(notation)가 과도하고 액션 트리 구성 세부사항 설명 부족.

- **Overall**: 4/5

**총평**: TREE-PLANNER는 LLM 기반 폐루프 태스크 플래닝의 토큰 효율성과 오류 수정 효율성을 동시에 해결하는 실용적이고 효과적인 방법으로, 계획 샘플링과 의사결정 분리라는 명확한 패러다임 전환을 제시한다. 다만 VirtualHome에 국한된 평가와 실제 로봇 환경으로의 검증 필요가 남아있어 완성도 4점이다.

## Related Papers

- 🏛 기반 연구: [[papers/625_PlanGenLLMs_A_Modern_Survey_of_LLM_Planning_Capabilities/review]] — LLM의 계획 생성 능력에 대한 포괄적 조사로 Tree-planner의 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/499_LLM_With_Tools_A_Survey/review]] — LLM의 도구 활용 능력을 토큰 효율적인 계획 수립으로 확장한 구체적 구현체를 제시한다.
- 🔄 다른 접근: [[papers/740_Search-R1_Training_LLMs_to_Reason_and_Leverage_Search_Engine/review]] — 강화학습 기반 검색 및 추론 훈련으로 계획 수립의 다른 접근 방식을 보여준다.
