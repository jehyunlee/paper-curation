---
title: "120_AutoGen_Enabling_Next-Gen_LLM_Applications_via_Multi-Agent_C"
authors:
  - "Qingyun Wu"
  - "Gagan Bansal"
  - "Jieyu Zhang"
  - "Yiran Wu"
  - "Beibin Li"
date: "2023"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "AutoGen은 LLM 기반 에이전트들이 서로 대화하면서 협력하여 복잡한 작업을 해결할 수 있는 오픈소스 프레임워크로, 개발자가 다양한 도메인의 LLM 애플리케이션을 빠르게 구축할 수 있도록 돕는다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-agent_Task_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wu et al._2023_AutoGen Enabling Next-Gen LLM Applications via Multi-Agent Conversation.pdf"
---

# AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation

> **저자**: Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li | **날짜**: 2023 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) *AutoGen이 지원하는 다중 에이전트 대화 기반 LLM 애플리케이션의 다양한 형태*

AutoGen은 LLM 기반 에이전트들이 서로 대화하면서 협력하여 복잡한 작업을 해결할 수 있는 오픈소스 프레임워크로, 개발자가 다양한 도메인의 LLM 애플리케이션을 빠르게 구축할 수 있도록 돕는다.

## Motivation

- **Known**: 대규모 언어모델(LLM)이 추론, 도구 활용, 관찰 적응 등에서 뛰어난 능력을 보유하고 있으며, 여러 에이전트의 협력이 다양한 사고(divergent thinking), 사실성 개선, 검증 능력 향상에 도움이 됨

- **Gap**: 다양한 복잡도와 LLM 용량을 가진 애플리케이션들을 구축하기 위한 일관된 프레임워크가 부재했으며, 서로 다른 대화 패턴과 에이전트 상호작용을 유연하게 지원할 수 있는 통합 인터페이스가 필요했음

- **Why**: (1) 최신 LLM들(GPT-4 등)은 피드백을 통합하고 대화를 통해 협력할 수 있는 능력을 갖추고 있으며, (2) 단일 LLM도 올바른 프롬프트와 설정으로 광범위한 기능을 수행할 수 있고, (3) 복잡한 작업을 더 간단한 부작업으로 분할하는 것이 효과적이기 때문

- **Approach**: 다중 에이전트 대화(multi-agent conversation) 기반의 프레임워크 설계를 통해 (1) 맞춤형·대화 가능한 에이전트와 (2) 대화 기반 프로그래밍 패러다임을 제공

## Achievement

![Figure 2](figures/fig2.webp) *AutoGen을 이용한 다중 에이전트 대화 프로그래밍의 구조 및 실행 예시*

1. **맞춤형 대화 가능 에이전트 (Conversable Agents)**: ConversableAgent를 기본 추상화로 하여 LLM, 인간, 도구를 자유롭게 조합하여 다양한 역할(코드 생성, 코드 실행, 인간 피드백 수집, 검증 등)의 에이전트를 빠르게 구성 가능

2. **대화 중심 프로그래밍 패러다임 (Conversation Programming)**: 복잡한 LLM 워크플로우를 다중 에이전트 대화로 단순화하고, 자연어와 프로그래밍 언어의 조합으로 다양한 대화 패턴(계층적 채팅, 공동 채팅 등) 구현 가능

3. **통합 인터페이스**: send, receive, generate_reply 등의 통일된 대화 인터페이스로 다양한 복잡도의 애플리케이션 개발 지원

4. **광범위한 응용성**: 수학, 코딩, 질의응답, 운영연구, 온라인 의사결정, 엔터테인먼트 등 다양한 도메인에서 효과성 입증

## How

![Figure 3-4](figures/fig3.webp) *다양한 애플리케이션 사례 및 성능 비교*

- **에이전트 설계**: 
  - ConversableAgent를 기반으로 AssistantAgent(LLM 백엔드), UserProxyAgent(인간·도구 백엔드), GroupChatManager 등 사전구성된 에이전트 제공
  - 각 에이전트는 LLM 기반 응답 생성, 코드 실행, 인간 입력 수집 등의 기능을 선택적으로 활성화 가능

- **대화 프로그래밍**:
  - Computation: agent.generate_reply()를 통해 수신한 메시지에 대한 응답 생성 (LLM 추론, 도구 실행, 인간 입력 등 조합)
  - Control Flow: agent.send(), agent.receive() 및 등록된 reply 함수를 통해 메시지 흐름 제어
  - 조건부 메시지 라우팅, 동적 에이전트 추가, 종료 조건 설정 등으로 유연한 대화 흐름 구성

- **향상된 LLM 추론 레이어**: 결과 캐싱, 에러 처리, 메시지 템플릿팅 등으로 효율성과 안정성 향상

- **프롬프트 엔지니어링**: 역할 정의, 암묵적 상태 추론, 다단계 문제 해결 등을 지원하는 시스템 메시지 설계

## Originality

- **다중 에이전트 대화의 추상화**: 기존의 단일 에이전트 또는 tool-use 패러다임에서 벗어나 에이전트 간 대화 자체를 계산 단위로 설정하는 새로운 프로그래밍 패러다임 제시

- **대화 중심 제어 흐름**: 조건문이나 루프가 아닌 에이전트 간 메시지 교환을 통해 자연스럽게 제어 흐름이 결정되는 방식으로, 복잡한 워크플로우를 직관적으로 구성 가능

- **통합된 에이전트 인터페이스**: LLM, 인간, 도구 백엔드를 동일한 에이전트 인터페이스로 조합 가능하게 하여 높은 유연성과 재사용성 달성

- **실용적 오픈소스 제공**: 학술적 개념뿐 아니라 완전히 구현된 프레임워크(https://github.com/microsoft/autogen)로 제공하여 실제 애플리케이션 개발 촉진

## Limitation & Further Study

- **확장성 검증 부족**: 논문에서 제시된 예시들이 상대적으로 규모가 작으며, 매우 복잡한 대규모 멀티에이전트 시스템에서의 성능과 관리 가능성에 대한 검증이 제한적

- **에이전트 협력 최적화**: 에이전트 간 대화가 수렴하지 않거나 불필요하게 길어지는 경우에 대한 명시적 해결책이 부족하며, 대화 최적화 전략에 대한 깊이 있는 논의 필요

- **LLM 비용 고려**: 멀티턴 에이전트 대화는 많은 LLM API 호출을 유발하는데, 비용 최적화 및 효율성 개선 방안에 대한 논의 미흡

- **인간-에이전트 상호작용 설계**: 인간 개입 시점과 방식에 대한 원칙적 가이드라인 부재로, 실제 애플리케이션에서는 시행착오가 필요할 수 있음

- **후속 연구 방향**: (1) 다양한 도메인의 대규모 실전 애플리케이션 사례 축적, (2) 에이전트 대화 수렴성 및 효율성 이론 개발, (3) 자동 프롬프트 최적화 및 에이전트 역할 분배 최적화 알고리즘 개발

## Evaluation

- **Novelty**: 4.5/5 — 다중 에이전트 대화를 중심으로 한 프로그래밍 패러다임과 통합 에이전트 인터페이스 설계가 신선하며, 기존 도구 사용(tool-use) 패러다임과의 차별성이 명확함

- **Technical Soundness**: 4/5 — 프레임워크 설계와 구현이 견고하고, 다양한 응용 사례에서의 작동 가능성을 보여줌. 다만 이론적 기초나 수렴성 분석 등이 상대적으로 부족

- **Significance**: 4.5/5 — LLM 기반 애플리케이션 개발의 실질적 편의성을 크게 향상시키고, 오픈소스로 배포되어 커뮤니티에 미친 영향이 큼. 다양한 도메인의 실제 문제 해결 가능성 시연

- **Clarity**: 4/5 — 전체적인 구조와 개념 설명이 명확하고, Figure 2를 통한 시각화가 직관적임. 다만 프롬프트 엔지니어링의 세부 사항과 에이전트 커스터마이제이션 고급 기법에 대한 설명은 부분적

- **Overall**: 4.2/5

**총평**: AutoGen은 다중 에이전트 대화 기반의 혁신적인 프로그래밍 패러다임을 제시하여 LLM 애플리케이션 개발의 복잡성을 크게 감소시킨 실질적이고 영향력 있는 오픈소스 프레임워크이다. 다양한 도메인에서의 적용 가능성과 개발자 친화적인 설계가 큰 강점이며, 향후 대규모 시스템 최적화와 이론적 토대 구축이 추가로 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/596_OWL_Optimized_Workforce_Learning_for_General_Multi-Agent_Ass/review]] — OWL의 모듈식 WORKFORCE 프레임워크가 AutoGen의 대화형 다중 에이전트 시스템을 도메인 범용성을 위해 발전시킨 확장 버전이다.
- 🧪 응용 사례: [[papers/358_From_Labor_to_Collaboration_A_Methodological_Experiment_Usin/review]] — 인문사회과학 연구를 위한 Agentic Workflow가 AutoGen의 다중 에이전트 협업 메커니즘을 특정 학문 영역에 적용한 실용 사례이다.
- 🏛 기반 연구: [[papers/655_ReAct_Synergizing_Reasoning_and_Acting_in_Language_Models/review]] — ReAct의 추론-행동 결합 패러다임이 AutoGen의 에이전트 간 대화형 문제 해결 메커니즘의 기본적인 설계 원리를 제공한다.
- 🔗 후속 연구: [[papers/447_Iterative_self-incentivization_empowers_large_language_model/review]] — AutoGen의 멀티 에이전트 프레임워크는 EXSEARCH의 단일 에이전트 자기 개선을 여러 에이전트 간 협력적 학습으로 확장한다.
- 🏛 기반 연구: [[papers/193_CellAgent_An_LLM-driven_Multi-Agent_Framework_for_Automated/review]] — 다중 에이전트 시스템의 일반적 프레임워크가 단일세포 분석 특화 에이전트의 기술적 기반을 제공한다
- 🏛 기반 연구: [[papers/327_Experiential_co-learning_of_software-developing_agents/review]] — 차세대 LLM 애플리케이션을 위한 다중 에이전트 프레임워크의 이론적 토대를 제공한다.
- 🔗 후속 연구: [[papers/464_Large_Language_Model_based_Multi-Agents_A_Survey_of_Progress/review]] — 차세대 LLM 애플리케이션을 위한 멀티에이전트 프레임워크가 복잡한 문제 해결의 구체적 구현 사례입니다.
- 🔗 후속 연구: [[papers/823_Towards_a_Science_of_Scaling_Agent_Systems/review]] — AutoGen의 다중 에이전트 프레임워크에 정량적 확장 법칙을 적용하여 성능 예측 가능성을 높인다.
- 🏛 기반 연구: [[papers/050_Adasociety_An_adaptive_environment_with_social_structures_fo/review]] — AutoGen의 다중 에이전트 대화 메커니즘이 AdaSociety의 사회적 구조 기반 협력 환경 구축에 핵심적인 기술적 토대를 제공한다.
- 🧪 응용 사례: [[papers/358_From_Labor_to_Collaboration_A_Methodological_Experiment_Usin/review]] — AutoGen의 다중 에이전트 대화 프레임워크가 인문사회과학 연구의 특수성을 고려한 협업 워크플로우에 구체적으로 적용된 사례이다.
- 🔗 후속 연구: [[papers/596_OWL_Optimized_Workforce_Learning_for_General_Multi-Agent_Ass/review]] — OWL의 모듈식 WORKFORCE 프레임워크가 AutoGen의 다중 에이전트 시스템을 도메인 이식성 문제 해결을 위해 발전시킨 확장된 아키텍처이다.
