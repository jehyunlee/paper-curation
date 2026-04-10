---
title: "205_Chatdev_Communicative_agents_for_software_development"
authors:
  - "Qian Chen"
  - "Wei Liu"
  - "Hongzhang Liu"
  - "Nuo Chen"
  - "Yufan Dang"
date: "2023"
doi: "arXiv:2307.07924"
arxiv: ""
score: 4.0
essence: "본 논문은 대규모 언어모델(LLM) 기반의 전문화된 에이전트들이 자연언어 및 프로그래밍 언어를 통해 상호 통신하며 소프트웨어 개발의 설계, 코딩, 테스트 단계를 협력적으로 수행하는 ChatDev 프레임워크를 제시한다. 이는 기존의 개별 단계별 고립된 딥러닝 접근법을 통일된 언어기반 통신으로 연결하여 전체적인 소프트웨어 개발 프로세스의 일관성과 효율성을 향상시킨다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-agent_Task_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chen et al._2023_Chatdev Communicative agents for software development.pdf"
---

# ChatDev: Communicative Agents for Software Development

> **저자**: Qian Chen, Wei Liu, Hongzhang Liu, Nuo Chen, Yufan Dang, Jiahao Li, Cheng Yang, Weize Chen, Yu-Sheng Su, Xin Cong, Juyuan Xu, Dahai Li, Zhiyuan Liu, Maosong Sun | **날짜**: 2023 | **DOI**: [arXiv:2307.07924](https://arxiv.org/abs/2307.07924)

---

## Essence

![Figure 2](figures/fig2.webp) 
*그림 2: 소프트웨어 에이전트들이 다단계 통신을 수행하며 설계, 코딩, 테스트 단계의 세부 작업을 협력하여 수행하는 체인-구조 워크플로우*

본 논문은 대규모 언어모델(LLM) 기반의 전문화된 에이전트들이 자연언어 및 프로그래밍 언어를 통해 상호 통신하며 소프트웨어 개발의 설계, 코딩, 테스트 단계를 협력적으로 수행하는 ChatDev 프레임워크를 제시한다. 이는 기존의 개별 단계별 고립된 딥러닝 접근법을 통일된 언어기반 통신으로 연결하여 전체적인 소프트웨어 개발 프로세스의 일관성과 효율성을 향상시킨다.

## Motivation

- **Known**: LLM은 자연언어 이해 및 역할극(role-playing) 능력이 뛰어나며, 자율 에이전트는 메모리, 계획, 도구 사용 등 고급 기능을 갖추고 있음. 소프트웨어 개발은 요구사항 분석, 시스템 설계, 코딩, 테스트 등 다양한 역량을 가진 팀원의 협력이 필수적임.

- **Gap**: 기존 딥러닝 기반 소프트웨어 개발 연구들은 각 단계(설계, 코딩, 테스트)별로 고유한 모델 설계를 요구하여 단계 간 기술적 불일치 및 단편화된 개발 프로세스 문제 발생. LLM 기반 코드 생성 시 불완전하거나 실행 불가능한 코딩 환각(hallucination) 문제가 빈번히 발생.

- **Why**: 다양한 역할을 가진 LLM 에이전트들이 체계적인 통신 구조 속에서 협력한다면, 통일된 언어 기반 인터페이스로 전체 개발 프로세스를 통합하고, 환각 문제를 완화할 수 있을 것으로 예상됨.

- **Approach**: (1) 체인-구조 워크플로우(chat chain)로 각 단계를 세부 작업으로 분해, (2) 이중 에이전트(instructor-assistant) 대화 패턴으로 안정적 통신, (3) 통신식 환각 제거(communicative dehallucination) 메커니즘으로 정보 요청 및 정확한 응답 확보.

## Achievement

![Figure 1](figures/fig1.webp)
*그림 1: ChatDev 프레임워크 - 다양한 사회적 역할을 가진 LLM 에이전트들이 다중 에이전트 협력을 통해 포괄적 솔루션 개발*

1. **개발 프로세스 통합**: 설계/코딩/테스트 단계에 대한 통일된 언어 기반 통신으로 기존의 단편화된 접근 방식을 체계적으로 통합. 자연언어는 시스템 설계에, 프로그래밍 언어는 소프트웨어 최적화에 각각 유효함을 실증.

2. **소프트웨어 품질 향상**: 생성된 소프트웨어의 완전성(completeness), 실행 가능성(executability), 요구사항 일관성이 모두 개선됨. 통신식 환각 제거 메커니즘을 통해 코딩 오류 발생률 감소.

3. **투명한 개발 과정**: 체인-구조 워크플로우는 중간 단계의 해결책을 검토할 수 있도록 하여 문제 식별 및 추적이 용이.

## How

![Figure 2](figures/fig2.webp)
*그림 2: 세부 작업별 instructor-assistant 에이전트의 다중 라운드 통신 및 합의 도달 과정*

- **Chat Chain (체인-구조 워크플로우)**
  - 전체 개발을 세 개의 순차 단계로 구성: 설계(Design) → 코딩(Coding) → 테스트(Testing)
  - 각 단계를 더욱 세분화된 서브태스크(subtask)로 분해 (예: 코딩 단계 = 코드 작성 + 코드 완성; 테스트 단계 = 정적 테스트 + 동적 테스트)
  - 수식: $C = \langle P_1, P_2, \ldots, P_{|C|} \rangle$, $P_i = \langle T^1, T^2, \ldots, T^{|P_i|} \rangle$

- **이중 에이전트 대화 패턴**
  - 각 서브태스크마다 Instructor(지시자)와 Assistant(보조자) 역할 배정
  - Instructor가 태스크 달성을 향한 지시를 제공 → Assistant가 이를 따르며 응답
  - Inception prompting 메커니즘으로 시스템 프롬프트($P_I$, $P_A$) 설정: $I = \rho(LLM, P_I)$, $A = \rho(LLM, P_A)$
  - 역할 반복, 지시 중복, 거짓 응답 등의 문제 제어

- **통신식 환각 제거(Communicative Dehallucination)**
  - 에이전트가 직접 응답하기 전에 더 구체적인 정보를 요청하는 메커니즘
  - 이를 통해 불완전하거나 부정확한 코드 생성 사전에 방지

- **메모리 관리**
  - 단기 메모리(short-term memory): 단일 단계 내 대화 연속성 유지
  - 장기 메모리(long-term memory): 단계 간 맥락 정보 보존
  - 일반 LLM의 제한된 컨텍스트 길이 극복

## Originality

- **다중 에이전트 협력의 새로운 패러다임**: 소프트웨어 개발을 전통적 역할(CEO, CTO, 프로그래머, 테스터) 기반의 LLM 에이전트 협력으로 재정의. 언어를 자율 에이전트 간 문제 해결의 통일적 다리로 제시한 점이 창신적.

- **체인-구조 워크플로우의 설계**: 단순하지만 효과적인 chain 구조로 복잡한 다중 에이전트 토폴로지를 회피하면서도 단계 간 순차적 협력을 가능케 한 점.

- **통신식 환각 제거 메커니즘**: LLM의 환각 문제를 해결하기 위해 에이전트가 능동적으로 상세 정보를 요청하는 상호작용 기반의 새로운 접근법.

- **자연언어와 프로그래밍 언어의 이중 활용**: 같은 프레임워크 내에서 자연언어는 설계 단계에, 프로그래밍 언어는 디버깅 단계에 각각 활용되도록 설계하여, 각 언어의 장점을 최대화.

## Limitation & Further Study

- **규모 제약**: 복잡한 대규모 소프트웨어 프로젝트(수천 줄 이상의 코드)에 대한 실제 성능 평가 부족. 현재 평가는 상대적으로 단순한 게임(Gomoku) 등 제한된 범위의 과제로 제한됨.

- **환각 제거의 완전성**: 통신식 환각 제거가 모든 유형의 코딩 오류(논리 오류, 성능 최적화 부재 등)를 완벽히 해결하지 못할 가능성. 통계적 성공률 제시가 필요.

- **에이전트 역할의 경직성**: CEO, CTO, Programmer, Tester 등 역할이 사전 정의되어 있어, 상황별 유연한 역할 재구성의 제한성.

- **평가 데이터의 한계**: 논문에서 구축한 데이터셋의 규모 및 다양성에 대한 상세 설명 부족. 더 다양한 도메인(웹 애플리케이션, 데이터 처리 등)에 대한 검증 필요.

- **후속 연구 방향**: 
  - 계층적 또는 반복적 에이전트 토폴로지 도입으로 대규모 프로젝트 대응
  - 코드 실행 피드백을 통한 실시간 디버깅 루프 통합
  - 외부 도구(정적 분석, 컴파일러 오류) 활용 강화
  - 다양한 LLM 백엔드 간 비교 분석

## Evaluation

- **Novelty (독창성)**: 4.5/5  
  다중 에이전트 협력과 언어 기반 통신을 소프트웨어 개발에 적용한 점은 참신하나, 체인 구조 자체는 기존 워터폴 모델의 변형이고, 각 구성 요소(프롬프트 엔지니어링, 메모리 관리)는 선행 연구에서 차용.

- **Technical Soundness (기술적 타당성)**: 4/5  
  제안된 메커니즘(inception prompting, 이중 에이전트 패턴, 메모리 분할)이 논리적으로 타당하고 구현 가능함. 다만 환각 제거 메커니즘의 이론적 근거가 다소 약함. 실제 성능 메트릭(완전성, 실행 가능성)에 대한 객관적 평가 방법론이 상세하지 않음.

- **Significance (중요성)**: 4/5  
  소프트웨어 개발 자동화의 통합적 접근법을 제시하여 실무적 영향력 높음. 다만 현재는 제한된 규모의 프로젝트에만 적용되어, 산업적 규모 적용까지는 갈 길이 멈. LLM 기반 개발 도구 발전에 기여할 수 있는 잠재력 있음.

- **Clarity (명확성)**: 4.5/5  
  논문 구성이 명확하고 Figure 2를 통한 시각화가 효과적. 수식 표현도 이해하기 용이. 다만 메모리 관리 및 프롬프트 엔지니어링의 세부 내용이 본 문에서 완전히 설명되지 않음.

- **Overall (종합)**: 4/5

**총평**: ChatDev는 LLM 기반 다중 에이전트 협력을 소프트웨어 개발 전 단계에 체계적으로 적용한 의미 있는 프레임워크로, 체인-구조 워크플로우와 통신식 환각 제거라는 실용적인 해결책을 제시한다. 다만 대규모 실제 프로젝트에 대한 검증 부족과 환각 완전 제거의 한계가 남아있어, 향후 확장성 및 견고성 개선이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/586_Opendevin_An_open_platform_for_ai_software_developers_as_gen/review]] — ChatDev와 OpenHands는 모두 LLM 기반 소프트웨어 개발을 다루지만, 에이전트 간 통신 중심과 오픈 플랫폼 기반이라는 서로 다른 구현 철학을 가집니다.
- 🔗 후속 연구: [[papers/327_Experiential_co-learning_of_software-developing_agents/review]] — ChatDev의 협력적 소프트웨어 개발은 경험적 공동학습 연구의 소프트웨어 에이전트 학습 기법을 확장하여 실제 개발 프로세스에서 에이전트 간 지식 공유와 역할 전문화를 실현합니다.
- 🔄 다른 접근: [[papers/327_Experiential_co-learning_of_software-developing_agents/review]] — 다중 에이전트 소프트웨어 개발에서 커뮤니케이션 기반 협력 방식의 다른 접근법을 제시한다.
- 🔗 후속 연구: [[papers/416_Hyperagent_Generalist_software_engineering_agents_to_solve_c/review]] — ChatDev의 소프트웨어 개발을 위한 의사소통 에이전트가 HYPERAGENT의 전문화된 에이전트 시스템으로 발전한 확장 형태이다.
