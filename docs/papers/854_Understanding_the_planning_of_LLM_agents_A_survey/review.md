---
title: "854_Understanding_the_planning_of_LLM_agents_A_survey"
authors:
  - "Xu Huang"
  - "Weiwen Liu"
  - "Xiaolong Chen"
  - "Xingmei Wang"
  - "Hao Wang 외"
date: "2024"
doi: "10.48550/arXiv.2402.02716"
arxiv: ""
score: 4.0
essence: "본 논문은 대규모 언어모델(LLM)을 자율 에이전트의 계획 모듈로 활용하는 최신 연구들을 체계적으로 분석한 첫 번째 종합 설문 논문이다. 기존의 기호 기반 방법과 강화학습 기반 방법의 한계를 극복하기 위해 LLM의 추론 및 도구 활용 능력을 활용한 계획 수립 방법들을 5가지 범주로 분류하여 상세히 분석한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Multi-Hop_Reasoning_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Huang et al._2024_Understanding the planning of LLM agents A survey.pdf"
---

# Understanding the planning of LLM agents: A survey

> **저자**: Xu Huang, Weiwen Liu, Xiaolong Chen, Xingmei Wang, Hao Wang 외 | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2402.02716](https://doi.org/10.48550/arXiv.2402.02716)

---

## Essence

![Figure 1: Taxonomy on LLM-Agent planning](figures/fig1.webp)
*LLM 기반 에이전트 계획 수립의 5가지 주요 분류*

본 논문은 대규모 언어모델(LLM)을 자율 에이전트의 계획 모듈로 활용하는 최신 연구들을 체계적으로 분석한 첫 번째 종합 설문 논문이다. 기존의 기호 기반 방법과 강화학습 기반 방법의 한계를 극복하기 위해 LLM의 추론 및 도구 활용 능력을 활용한 계획 수립 방법들을 5가지 범주로 분류하여 상세히 분석한다.

## Motivation

- **Known**: 기존 자율 에이전트의 계획 수립은 기호 기반 방법(PDDL)과 강화학습(RL) 기반 방법에 의존해왔으며, 이들은 각각 전문가의 노력 필요, 오류 불내성, 높은 데이터 요구량 등의 한계를 가짐

- **Gap**: 최근 LLM의 급속한 발전으로 LLM 기반 에이전트 계획 연구가 급증했으나, 기존 설문들은 LLM의 추론, 도구 학습, 자율 에이전트 전반을 다루면서 계획 능력 자체에 대한 상세한 분석이 부족함

- **Why**: LLM은 자연언어 처리, 복잡한 추론, 다양한 도구 활용, 지시 따르기 능력을 보유하고 있어 에이전트의 인지 코어로서 계획 능력을 크게 향상시킬 수 있는 잠재력이 있음

- **Approach**: LLM 기반 에이전트 계획의 최신 연구들을 체계적으로 분류하고 분석하여 5가지 주요 방향으로 구조화하며, 4개 벤치마크에서 대표 방법들을 평가하여 종합적 인사이트를 제공

## Achievement

![Figure 2: Types of task decomposition manners](figures/fig2.webp)
*작업 분해의 두 가지 방식: (a) 분해-우선 방식과 (b) 인터리빙 방식*

1. **체계적 분류 체계 제시**: 기존에 산발적으로 연구되던 LLM 기반 에이전트 계획 방법들을 **작업 분해(Task Decomposition)**, **다중 계획 선택(Multi-plan Selection)**, **외부 모듈 활용(External Planner-aided Planning)**, **반사 및 개선(Reflection & Refinement)**, **메모리 증강 계획(Memory-augmented Planning)** 5가지로 체계적으로 분류

2. **각 방향별 상세 분석**: 각 범주에 대해 동기, 기본 아이디어, 대표 방법들(CoT, ReAct, HuggingGPT, Plan-and-Solve 등), 장단점을 포괄적으로 논의

3. **공식적 문제 표현**: 각 방법을 수학적으로 명확히 표현하여 상이한 접근 방식 간의 본질적 차이를 명확히 함

4. **종합적 벤치마크 평가**: 4개의 주요 벤치마크에서 대표 방법들을 평가하여 실증적 비교 제공

## How

**작업 분해(Task Decomposition) 방법**
- 복잡한 작업을 분할 정복 전략으로 여러 부분작업(sub-task)으로 분해
- **분해-우선 방식**: 모든 부분작업을 미리 분해 후 순차적으로 계획 수립 (HuggingGPT, Plan-and-Solve, ProgPrompt)
- **인터리빙 방식**: 부분작업 분해와 계획을 번갈아 수행하며 동적 조정 (CoT, ReAct, PAL, PoT)
  - CoT: 소수의 예제를 통해 단계별 추론 유도
  - Zero-shot CoT: "단계별로 생각해보자"는 지시로 추론 능력 활성화
  - ReAct: 추론(Thought)과 계획(Action)을 분리하여 교대로 수행
  - PoT/PAL: 프로그래밍 코드로 추론 과정을 형식화

**다중 계획 선택(Multi-plan Selection)**
- 여러 대안 계획을 생성한 후 트리 탐색 등의 전략으로 최적 계획 선택
- ToT(Tree-of-Thought), GoT(Graph-of-Thought), CoT-SC 등이 대표

**외부 모듈 활용(External Planner-aided Planning)**
- LLM이 작업을 형식화하고 전문 계획 시스템(예: PDDL 기반 계획기)이 실제 계획 생성
- LLM+P, LLM+PDDL 등의 방법

**반사 및 개선(Reflection & Refinement)**
- 초기 계획 생성 후 오류 반영, 피드백 수집, 계획 개선의 반복 프로세스
- Reflexion, CRITIC, Self-Refine 등이 실패 경험으로부터 학습

**메모리 증강 계획(Memory-augmented Planning)**
- 상식, 과거 경험, 도메인 지식 등을 별도 메모리에 저장하고 계획 시 검색 활용
- REMEMBER, MemoryBank 등의 방법

## Originality

- **최초의 체계적 종합 분석**: LLM 기반 에이전트 계획 능력에 특화된 첫 번째 설문으로, 기존 일반 에이전트/추론/도구 학습 설문들과 차별화

- **포괄적 분류 체계**: 5가지 직교적 범주로 기존 산발적 연구들을 명확히 구조화하여, 각 방법의 본질적 아이디어와 차이를 명확화

- **형식적 문제 정의**: 각 방향을 수학적으로 엄밀하게 표현하여 비교 분석 용이성 증대

- **상세한 실증 비교**: Table 1을 통한 체계적 비교와 4개 벤치마크에서의 정량적 평가 제공

## Limitation & Further Study

**현재 한계점**
- 논문 초반부로 전체 내용이 제시되지 않아 각 방법의 구체적 성능 비교, 개별 한계점에 대한 상세 분석이 확인 불가
- 작업 분해 방식에서 분해-우선 방식의 오류 누적 문제, 인터리빙 방식의 환각(hallucination) 문제 지적에 그침
- 다양한 방법 간 상충 관계나 결합 가능성에 대한 상세한 논의 부재

**후속 연구 방향**
- LLM 기반 계획의 견고성(robustness) 향상: 오류 복구, 동적 재계획 메커니즘 개발
- 계획 효율성 개선: 긴 궤적(trajectory)에서의 환각 문제 해결
- 여러 방법의 하이브리드 접근: 작업 분해, 외부 계획기, 메모리의 결합 효과 연구
- 도메인 특화 평가: 로봇공학, 웹 에이전트, 과학적 발견 등 구체적 응용에서의 계획 능력 평가
- 계획의 해석가능성(interpretability) 향상: LLM의 계획 과정의 투명성 증대

## Evaluation

- **Novelty** (독창성): 4/5
  - LLM 기반 에이전트 계획에 특화된 첫 체계적 설문이며, 5가지 분류 체계는 기존 산발적 연구를 효과적으로 구조화함. 다만 분류 자체가 기존 방법들의 특성 추출일 수 있어 완전히 새로운 개념 도입은 제한적

- **Technical Soundness** (기술적 건전성): 4/5
  - 각 방향을 수학적으로 명확하게 표현하고, 기존 연구들의 핵심 아이디어를 정확히 포착함. 다만 제시된 부분에서 방법들 간 상충이나 한계에 대한 심화 분석은 추가 필요

- **Significance** (중요성): 4/5
  - LLM 에이전트 연구가 급속히 확산되는 상황에서 계획 능력을 체계적으로 정리한 것은 커뮤니티에 큰 가치 제공. 단 구체적인 응용 분야 연결이나 실무적 가이드라인은 제한적

- **Clarity** (명확성): 4.5/5
  - 논문 구조가 명확하고, Figure 1을 통한 시각적 분류와 Table 1을 통한 체계적 비교가 이해를 도움. 각 방법의 수식 표현도 직관적임

- **Overall** (종합 평가): 4/5

**총평**: 본 논문은 급속히 발전하는 LLM 기반 에이전트 계획 분야에 대한 첫 체계적 종합 분석을 제공하며, 5가지 명확한 분류 체계와 상세한 기술적 분석을 통해 커뮤니티에 중요한 참고자료가 될 것으로 평가된다. 향후 각 방향의 한계 극복과 방법론 간 결합 연구가 핵심 과제가 될 것으로 예상된다.

## Related Papers

- 🏛 기반 연구: [[papers/412_HuggingGPT_Solving_AI_Tasks_with_ChatGPT_and_its_Friends_in/review]] — 계층적 작업 메모리 관리가 LLM 에이전트의 장기 계획 수립에서 핵심적인 기반 기술을 제공한다.
- 🔄 다른 접근: [[papers/625_PlanGenLLMs_A_Modern_Survey_of_LLM_Planning_Capabilities/review]] — LLM 계획 능력에 대한 현대적 조사와 LLM 에이전트 계획의 이해 모두 동일한 주제를 다루지만 접근 관점이 다르다.
- 🔗 후속 연구: [[papers/577_Nova_An_iterative_planning_and_search_approach_to_enhance_no/review]] — 반복적 계획과 검색을 통한 추론 향상이 LLM 에이전트 계획 수립의 구체적인 확장 방법이다.
- 🔄 다른 접근: [[papers/625_PlanGenLLMs_A_Modern_Survey_of_LLM_Planning_Capabilities/review]] — LLM 에이전트 계획 이해에 대한 조사와 LLM 계획 능력의 현대적 조사는 상호 보완적인 관점을 제공합니다
- 🧪 응용 사례: [[papers/412_HuggingGPT_Solving_AI_Tasks_with_ChatGPT_and_its_Friends_in/review]] — LLM 에이전트의 계획 수립에서 계층적 메모리 관리가 장기 작업 수행에 필수적인 구성 요소이다.
