---
title: "464_Large_Language_Model_based_Multi-Agents_A_Survey_of_Progress"
authors:
  - "Taicheng Guo"
  - "Xiuying Chen"
  - "Yaqi Wang"
  - "Ruidi Chang"
  - "Shichao Pei"
date: "2024"
doi: "10.48550/arXiv.2402.01680"
arxiv: ""
score: 4.0
essence: "대규모 언어모델(LLM)의 계획 및 추론 능력을 활용하여 여러 자율 에이전트가 협력하는 멀티에이전트 시스템(LLM-MA)이 복잡한 문제 해결과 세계 시뮬레이션에서 상당한 진전을 이루고 있다. 본 논문은 LLM 기반 멀티에이전트 시스템의 필수 측면(에이전트-환경 인터페이스, 프로파일링, 통신, 능력 획득)과 도메인 적용을 체계적으로 정리한 종합 서베이이다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Agent_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Guo et al._2024_Large Language Model based Multi-Agents A Survey of Progress and Challenges.pdf"
---

# Large Language Model based Multi-Agents: A Survey of Progress and Challenges

> **저자**: Taicheng Guo, Xiuying Chen, Yaqi Wang, Ruidi Chang, Shichao Pei | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2402.01680](https://doi.org/10.48550/arXiv.2402.01680)

---

## Essence

![Figure 1](https://arxiv.org/html/2402.01680v2/x1.png)
*그림 1: LLM 기반 멀티에이전트 연구 분야의 상승 추세. 문제 해결 및 세계 시뮬레이션 범주에서 최근 연구를 3개월 간격으로 분류.*

대규모 언어모델(LLM)의 계획 및 추론 능력을 활용하여 여러 자율 에이전트가 협력하는 멀티에이전트 시스템(LLM-MA)이 복잡한 문제 해결과 세계 시뮬레이션에서 상당한 진전을 이루고 있다. 본 논문은 LLM 기반 멀티에이전트 시스템의 필수 측면(에이전트-환경 인터페이스, 프로파일링, 통신, 능력 획득)과 도메인 적용을 체계적으로 정리한 종합 서베이이다.

## Motivation

- **Known**: 단일 LLM 기반 에이전트는 뛰어난 인지 능력과 의사결정 능력을 갖춘 것으로 입증되었으며, 소프트웨어 개발, 로봇 시스템, 정책 시뮬레이션 등 다양한 작업에 활용 중이다.

- **Gap**: LLM 기반 멀티에이전트 시스템에 대한 기존의 독립적인 연구들이 증가하고 있으나, 이들을 체계적으로 정리하고 통합된 프레임워크를 제시하는 종합적인 리뷰가 부재한 상태이다.

- **Why**: LLM-MA는 여러 자율 에이전트의 집단 지능(collective intelligence)과 전문화된 프로파일 및 기술을 활용하여 복잡한 실제 환경을 효과적으로 시뮬레이션할 수 있어, 단일 에이전트 시스템보다 향상된 능력을 제공한다.

- **Approach**: 에이전트-환경 인터페이스, 에이전트 프로파일링, 에이전트 통신, 에이전트 능력 획득이라는 4가지 핵심 측면을 중심으로 LLM-MA 시스템의 구조를 분석하고, 문제 해결(problem-solving)과 세계 시뮬레이션(world simulation) 응용 분야로 분류하여 최신 연구 동향을 체계화한다.

## Achievement

![Figure 2](https://arxiv.org/html/2402.01680v2/x2.png)
*그림 2: LLM-MA 시스템의 아키텍처. 에이전트-환경 인터페이스, 에이전트 프로파일, 통신 메커니즘, 능력 획득 과정을 통합적으로 표현.*

1. **종합적 분류 체계 수립**: LLM-MA 시스템을 4가지 핵심 차원(인터페이스, 프로파일링, 통신, 능력 획득)과 2가지 응용 분야(문제 해결, 세계 시뮬레이션)로 체계적으로 분류하여 연구 지형도를 제시.

2. **에이전트-환경 인터페이스 분석**: 샌드박스(Sandbox), 물리적(Physical), 없음(None)의 3가지 인터페이스 유형을 규정하고, 각 유형에서 에이전트의 상호작용 방식을 명확히 분석.

3. **에이전트 프로파일링 방법론**: Pre-defined(사전 정의), Model-Generated(모델 생성), Data-Derived(데이터 기반)의 3가지 프로파일링 방법을 체계화하여 다양한 에이전트 정의 방식 제시.

4. **에이전트 통신 체계화**: 통신 패러다임(Communication Paradigm), 정보 통과 메커니즘(Message-Passing Mechanism), 프로토콜(Protocol)의 3가지 측면에서 에이전트 간 상호작용 구조를 분석.

## How

![Figure 3](https://arxiv.org/html/2402.01680v2/x3.png)
*그림 3: 에이전트 통신 구조. 브로드캐스트(Broadcast), 라우팅(Routing), 토폴로지(Topology) 등 다양한 통신 패턴을 나타냄.*

- **에이전트-환경 인터페이스**: 에이전트가 환경과 상호작용하는 방식을 3가지로 분류 - (1) 샌드박스: 코드 인터프리터(소프트웨어 개발), 게임 규칙(게임 시뮬레이션) 등 시뮬레이션 환경, (2) 물리적: 로봇이 실제 환경에서 반복적으로 행동하고 관찰하는 방식, (3) 없음: 외부 환경 없이 에이전트 간 토론/합의 시스템

- **에이전트 프로파일링**: 역할(role), 행동(behavior), 기술(skill), 제약(constraint)을 포함한 특성을 정의. 방법론으로는 시스템 설계자가 명시적으로 정의하는 방식(Pre-defined), LLM이 생성하는 방식(Model-Generated), 기존 데이터셋 기반 구성(Data-Derived)을 활용

- **에이전트 능력 획득 메커니즘**: 인-컨텍스트 학습(In-Context Learning), 경험 학습(Experience Learning), 외부 지식 통합(External Knowledge Integration) 등을 통해 에이전트의 능력을 확장

- **통신 프로토콜**: 브로드캐스트(모든 에이전트에 동시 전송), 라우팅(특정 에이전트 대상), 계층적 토폴로지(hierarchical communication) 등 다양한 메시지 전달 방식 구현

## Originality

- **포괄적 분류 체계**: 기존 단일 에이전트 시스템 연구에서 벗어나 멀티에이전트 시스템의 고유한 특성(다중 에이전트 간 상호작용, 집단 의사결정)을 중심으로 한 새로운 분석 틀 제시

- **다학제적 관점의 통합**: AI 전문가뿐 아니라 사회과학, 심리학, 정책 연구 분야의 관점을 통합하여 LLM-MA 연구의 광범위한 응용을 조망

- **체계적 아키텍처 모델링**: 에이전트-환경 인터페이스, 프로파일링, 통신, 능력 획득을 연결하는 통합 아키텍처를 제시하여 LLM-MA 시스템의 설계 원리 명확화

- **응용 분야의 명확한 분류**: 문제 해결과 세계 시뮬레이션이라는 2가지 주요 응용 스트림으로 구분하여 각 영역의 특성과 요구사항을 체계적으로 분석

## Limitation & Further Study

- **이론적 기초의 부재**: 멀티에이전트 시스템이 왜 단일 에이전트보다 우수한지에 대한 이론적 분석이나 성능 향상의 원인에 대한 심층적 논의 부족

- **평가 메트릭의 표준화 미흡**: 멀티에이전트 시스템의 효과성을 측정하기 위한 표준화된 평가 지표가 제시되지 않아, 서로 다른 시스템 간 비교가 어려움

- **확장성과 신뢰성 문제**: 에이전트 수 증가에 따른 통신 오버헤드, 에이전트 오류에 따른 시스템 견고성 저하 등 실제 대규모 배포 시 발생할 수 있는 문제에 대한 논의 부족

- **향후 연구 방향**: (1) LLM-MA 시스템의 성능과 효율성에 대한 이론적 분석 강화, (2) 에이전트 수, 복잡도, 이질성(heterogeneity)에 따른 체계적 성능 평가, (3) 다양한 도메인 간 전이 학습(transfer learning) 가능성 탐색, (4) 개방형 환경에서의 안전성 및 신뢰성 보장 메커니즘 개발

## Evaluation

- **Novelty**: 4/5 - LLM-MA 시스템의 4가지 핵심 차원을 통합적으로 분석하는 새로운 프레임워크를 제시했으나, 개별 기술의 혁신성보다는 기존 연구의 체계적 정리에 중점

- **Technical Soundness**: 4/5 - 에이전트-환경 인터페이스, 프로파일링, 통신 메커니즘 등의 분류가 타당하고 명확하나, 각 구성요소 간의 상호작용에 대한 형식적 분석 부족

- **Significance**: 4/5 - LLM-MA 분야의 빠른 성장에 대응하여 포괄적 개요를 제공하며, 다양한 학문 분야의 연구자들에게 유용한 참고 자료가 될 수 있으나, 실제 시스템 설계에 대한 구체적 지침은 제한적

- **Clarity**: 4/5 - 전체 구조와 분류 체계가 명확하게 제시되었으나, 각 개념 간의 관계와 상호의존성에 대한 상세한 설명 필요

- **Overall**: 4/5

**총평**: 본 논문은 급속히 발전하는 LLM 기반 멀티에이전트 연구 분야에 대한 체계적이고 포괄적인 서베이를 제공하며, 에이전트-환경 인터페이스, 프로파일링, 통신, 능력 획득이라는 4가지 핵심 차원으로 LLM-MA 시스템을 분석하는 새로운 프레임워크를 제시하여 학술적 가치가 높다. 다만 이론적 분석의 깊이와 실제 적용 시 마주칠 수 있는 확장성, 신뢰성 문제에 대한 논의가 보강된다면 더욱 실용적인 자료가 될 것으로 예상된다.

## Related Papers

- 🏛 기반 연구: [[papers/033_A_survey_on_large_language_model_based_autonomous_agents/review]] — 대형 언어 모델 기반 자율 에이전트 서베이가 멀티에이전트 시스템 설계의 이론적 토대를 제공합니다.
- 🔗 후속 연구: [[papers/120_AutoGen_Enabling_Next-Gen_LLM_Applications_via_Multi-Agent_C/review]] — 차세대 LLM 애플리케이션을 위한 멀티에이전트 프레임워크가 복잡한 문제 해결의 구체적 구현 사례입니다.
- 🧪 응용 사례: [[papers/331_Exploring_collaboration_mechanisms_for_llm_agents_A_social_p/review]] — LLM 에이전트 간 협력 메커니즘 탐색이 멀티에이전트 시스템의 실제 적용 방안을 제시합니다.
- 🔄 다른 접근: [[papers/361_From_LLM_Reasoning_to_Autonomous_AI_Agents_A_Comprehensive_R/review]] — 멀티 에이전트 LLM 시스템에 대한 다른 관점의 포괄적 조사
- 🔗 후속 연구: [[papers/625_PlanGenLLMs_A_Modern_Survey_of_LLM_Planning_Capabilities/review]] — 멀티 에이전트 기반 대형 언어모델의 진전 조사는 개별 LLM의 계획 능력을 다중 에이전트 환경으로 확장한 연구입니다
- 🏛 기반 연구: [[papers/052_Advances_and_challenges_in_foundation_agents_From_brain-insp/review]] — 파운데이션 에이전트의 현황과 도전과제 분석이 LLM 기반 멀티 에이전트 시스템의 발전과 한계에 대한 포괄적 이해를 제공한다
- 🔗 후속 연구: [[papers/033_A_survey_on_large_language_model_based_autonomous_agents/review]] — LLM 기반 다중 에이전트의 진전과 도전과제를 포괄적으로 다루어 자율 에이전트 연구를 확장한다.
- 🏛 기반 연구: [[papers/025_A_Survey_of_AI_for_Materials_Science_Foundation_Models_LLM_A/review]] — 멀티 에이전트 LLM 발전 조사가 AI 소재 과학에서 LLM 에이전트 활용 방안의 이론적 기반을 제공함
- 🏛 기반 연구: [[papers/823_Towards_a_Science_of_Scaling_Agent_Systems/review]] — 다중 에이전트 시스템 확장의 이론적 원칙을 머신러닝 하이퍼파라미터 최적화 등 구체적 응용에 적용할 수 있는 기반을 제공한다.
- 🧪 응용 사례: [[papers/596_OWL_Optimized_Workforce_Learning_for_General_Multi-Agent_Ass/review]] — 대규모 언어 모델 기반 다중 에이전트의 진행 조사가 OWL의 범용 다중 에이전트 프레임워크 개발에 직접적으로 적용되는 방법론적 통찰이다.
- 🔗 후속 연구: [[papers/760_Small_Language_Models_are_the_Future_of_Agentic_AI/review]] — LLM 기반 다중 에이전트의 진전 조사는 소규모 언어모델의 에이전트 적합성을 기존 대규모 모델 기반 에이전트 연구와 비교 분석한다.
