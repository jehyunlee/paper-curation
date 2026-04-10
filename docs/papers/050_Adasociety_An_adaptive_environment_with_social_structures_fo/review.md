---
title: "050_Adasociety_An_adaptive_environment_with_social_structures_fo"
authors:
  - "Mingjie Bi"
  - "Xue Feng"
  - "Yizhe Huang"
  - "Fanqi Kong"
  - "Hao Liu"
date: "2024"
doi: "미제공"
arxiv: ""
score: 4.2
essence: "본 논문은 **적응형 물리적 환경과 동적 사회 구조를 결합한 다중 에이전트 의사결정 환경(AdaSociety)**을 제시한다. 에이전트들이 행동함에 따라 과제가 자동으로 생성되며, 사회적 연결이 보상과 정보 접근을 형성하여 다양한 학습 문제를 제공한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-agent_Task_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Bi et al._2024_Adasociety An adaptive environment with social structures for multi-agent decision-making.pdf"
---

# AdaSociety: An adaptive environment with social structures for multi-agent decision-making

> **저자**: Mingjie Bi, Xue Feng, Yizhe Huang, Fanqi Kong, Hao Liu, Siyuan Qi, Aoyang Qin, Min Tang, Xingbo Wang, Song-Chun Zhu | **날짜**: 2024 | **DOI**: [미제공]

---

## Essence

![Figure 1: AdaSociety의 물리적 요소와 사회적 요소 개요](figures/fig1.webp)

본 논문은 **적응형 물리적 환경과 동적 사회 구조를 결합한 다중 에이전트 의사결정 환경(AdaSociety)**을 제시한다. 에이전트들이 행동함에 따라 과제가 자동으로 생성되며, 사회적 연결이 보상과 정보 접근을 형성하여 다양한 학습 문제를 제공한다.

## Motivation

- **Known**: 기존 단일 에이전트 적응형 환경(Crafter, MineDojo 등)은 에이전트 행동에 따라 새로운 과제를 생성하여 과제 다양성을 확대함.
  
- **Gap**: 기존 다중 에이전트 환경들은 고정된 사회 구조와 제한된 상호작용만을 지원하며, 적응형 물리적 환경과 동적 사회 구조를 동시에 다루지 못함. 사회 연결이 에이전트의 의사결정에 미치는 영향이 충분히 연구되지 않음.

- **Why**: 다중 에이전트 설정에서 과제 집합은 물리적 환경뿐만 아니라 에이전트 간의 사회적 연결에 의해 결정됨. 중앙화(centralized) vs 분산화(decentralized) 구조는 전혀 다른 의사결정 문제를 야기하며, 이러한 구조들의 동적 변화는 추론 능력, 신뢰 형성, 계층 구조 형성 등 다양한 사회 지능을 요구함.

- **Approach**: 물리적 요소(자원, 이벤트, 에이전트 인벤토리)와 사회적 요소(다층 방향성 그래프로 표현된 동적 연결)를 명시적으로 통합한 적응형 환경을 설계하고, 3가지 미니게임을 통해 다양한 사회 구조와 학습 문제를 제시.

## Achievement

![Figure 2: 세 가지 미니게임의 개요](figures/fig2.webp)

1. **첫 다중 에이전트 적응형 환경**: 물리적 환경의 확장과 사회적 연결의 동적 변화를 동시에 지원하는 최초의 환경. 다층 방향성 그래프로 사회 상태를 명시적으로 정량화하여 연합 형성, 계층 구조 출현 등을 연구 가능하게 함.

2. **확장 가능한 상태-행동 공간**: 에이전트의 행동(자원 합성)에 따라 물리적 상태 공간이 동적으로 확장되며, 사회 행동(연결/단절)에 따라 사회적 상태 공간이 변화. 이는 다양한 승리 경로(multiple victory paths)를 창출하여 의사결정 복잡도를 증가.

3. **포괄적 평가 메트릭**: 개별 보상, 공정성 점수(Fairness score), 과제 완료율, 사회 네트워크 차수(degree) 등 다양한 평가 지표를 제공하여 개인 및 집단 성과를 균형있게 평가.

4. **실증적 발견**: 특정 사회 구조가 개인 및 집단 이익을 모두 증진할 수 있음을 보여줌. 그러나 현재 강화학습(RL) 및 대형언어모델(LLM) 기반 알고리즘들은 사회 구조를 활용하는 데 제한적 효과를 보임.

## How

![Figure 4: 합성 트리의 예시](figures/fig4.webp)

- **물리적 요소 설계**:
  - 자연 자원은 맵에 무작위로 분산, 합성 자원은 특정 이벤트 그리드와 필수 자원을 통해 생성
  - 합성 트리(Synthesis Tree)로 자원 간 관계를 정의하되, 에이전트는 상호작용을 통해 점진적으로 학습
  - 에이전트 인벤토리의 용량 제약과 자원 선호도(heterogeneous preferences) 설정으로 스킬 다양성 구현
  - 2D 상징형(symbolic) 맵으로 의사결정에 집중 (지각 문제 제외)

- **사회적 요소 설계**:
  - 다층 방향성 그래프(Multi-layer directed graph)로 에이전트-에이전트, 에이전트-조직 간 연결 표현
  - 사회 행동(Social actions): 연결/단절, 정보/보상 공유, 협상 등
  - 연결 의미론(Connection semantics)을 동적으로 협상 가능하게 설계
  - 계층 구조 형성을 지원하는 조직(Organization) 메커니즘

- **관찰 및 행동 공간**:
  - 부분 관찰성: 에이전트는 자신의 인벤토리와 전체 사회 상태는 알지만, 타 에이전트의 인벤토리는 부분 관찰 윈도우 범위 내에서만 확인
  - 신체 행동(Physical actions): 이동, 채집, 버리기, 합성, 통신
  - 행동 공간의 동적 확장: 새 자원 합성 시 선택지 증가

- **Growing-MG 문제 정식화**: 
  - 에이전트들이 적응형 물리 환경과 동적 사회 구조를 동시에 탐색해야 하는 일반합(general-sum) 게임 프레임워크 제시

![Figure 5: 에이전트와 AdaSociety 간의 상호적응](figures/fig5.webp)

## Originality

- **사회적 상태의 명시적 표현**: 기존 환경들이 사회적 상태를 암묵적으로만 다루던 반면, 다층 방향성 그래프로 사회 구조를 정량적이고 명시적으로 표현하는 것은 혁신적. 이는 계층 구조, 연합 형성 등 고수준의 사회 지능 연구를 가능하게 함.

- **적응형 물리 + 동적 사회의 동시 결합**: Table 1의 비교에서 보듯이, 기존 환경들(AI Economist, SMAC, Xland 등)은 동적 공간 OR 적응형 연결 중 하나만 지원. AdaSociety는 유일하게 둘 다 지원하면서 상호 영향을 모델링.

- **일반 합 게임 프레임워크**: 협력과 경쟁이 공존하는 일반 합 게임으로 다중 에이전트 상호작용을 모델링하여, 현실적인 사회 시나리오 반영.

- **LLM과 RL 모두 지원**: 기존 환경 대비 더 넓은 에이전트 타입(Tensor 기반 RL, LLM 기반)을 모두 지원하도록 설계.

## Limitation & Further Study

- **현존 알고리즘의 낮은 성능**: 논문에서 제시된 RL 및 LLM 기반 방법들이 사회 구조를 효과적으로 활용하지 못하고 있으며, 이는 새로운 알고리즘 개발의 필요성을 강하게 시사.

- **계산 복잡도 분석 부재**: 동적으로 확장되는 상태-행동 공간에서 계산 비용이 어떻게 증가하는지에 대한 이론적 분석이 부족.

- **기준 성능(Baseline) 제한**: 제시된 RL 및 LLM 기반 기준이 상대적으로 단순하여, 더 정교한 다중 에이전트 강화학습(MARL) 알고리즘의 성능 비교가 필요.

- **사회적 구조의 의미론 제한**: 현재는 정보 공유, 보상 공유, 분업 등 기본적인 의미론만 구현되어 있으며, 더 복잡한 사회적 개념(명성, 신뢰도 동적 변화 등)의 통합 가능성 제시 필요.

- **후속 연구 방향**:
  - 사회 구조를 명시적으로 활용하는 새로운 다중 에이전트 알고리즘 개발
  - 계층 구조와 권력 역학 연구를 위한 확장
  - 실제 사회 현상(신뢰, 평판)을 모델링한 심화 버전 설계
  - LLM 에이전트의 사회적 협상 및 의사소통 능력 강화


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.2/5

**총평**: AdaSociety는 적응형 물리 환경과 동적 사회 구조를 결합한 혁신적 다중 에이전트 환경을 제시하며, 사회적 지능 연구를 위한 중요한 벤치마크 플랫폼을 제공한다. 다층 방향성 그래프 기반의 명시적 사회 상태 표현과 일반 합 게임 프레임워크는 기존 환경들과 차별화된다. 다만, 현존 RL/LLM 알고리즘의 낮은 성능과 Growing-MG 문제의 제한적 형식화는 이 환경이 새로운 알고리즘 개발의 필요성을 강력히 드러내면서도, 구체적인 해결 방향을 제시하지 못한 점이 아쉽다. 벤치마크로서의 가치는 높지만, 학술적 깊이를 위해서는 이론적 분석과 기준 알고리즘의 강화가 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/120_AutoGen_Enabling_Next-Gen_LLM_Applications_via_Multi-Agent_C/review]] — AutoGen의 다중 에이전트 대화 메커니즘이 AdaSociety의 사회적 구조 기반 협력 환경 구축에 핵심적인 기술적 토대를 제공한다.
- 🔗 후속 연구: [[papers/175_Building_machines_that_learn_and_think_with_people/review]] — AdaSociety의 적응형 사회 구조가 Building machines의 협력적 인지 프레임워크를 다중 에이전트 환경에서 구현한 확장 사례이다.
- 🧪 응용 사례: [[papers/356_From_individual_to_society_A_survey_on_social_simulation_dri/review]] — AdaSociety의 동적 사회 구조 시뮬레이션이 사회과학 연구의 사회 시뮬레이션 방법론을 실제 구현한 응용 사례이다.
