---
title: "061_Agent_S_An_Open_Agentic_Framework_that_Uses_Computers_Like_a"
authors:
  - "Saaket Agashe"
  - "Jiuzhou Han"
  - "Shuyu Gan"
  - "Jiachen Yang"
  - "Ang Li"
date: "2024"
doi: "10.48550/arXiv.2410.08164"
arxiv: ""
score: 4.0
essence: "Agent S는 계층적 계획 수립, 경험 기억 시스템, 그리고 Agent-Computer Interface(ACI)를 통합한 GUI 자동화 프레임워크로, 복잡한 멀티스텝 데스크톱 작업을 인간처럼 자동으로 수행한다. OSWorld 벤치마크에서 기존 방법 대비 83.6% 상대 개선율을 달성한 최신 최고 성능(SOTA) 모델이다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Language_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Agashe et al._2024_Agent S An Open Agentic Framework that Uses Computers Like a Human.pdf"
---

# Agent S: An Open Agentic Framework that Uses Computers Like a Human

> **저자**: Saaket Agashe, Jiuzhou Han, Shuyu Gan, Jiachen Yang, Ang Li | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2410.08164](https://doi.org/10.48550/arXiv.2410.08164)

---

## Essence

![Figure 1: Agent S uses a computer like a human to solve diverse desktop tasks on different systems.](figures/fig1.webp)

Agent S는 계층적 계획 수립, 경험 기억 시스템, 그리고 Agent-Computer Interface(ACI)를 통합한 GUI 자동화 프레임워크로, 복잡한 멀티스텝 데스크톱 작업을 인간처럼 자동으로 수행한다. OSWorld 벤치마크에서 기존 방법 대비 83.6% 상대 개선율을 달성한 최신 최고 성능(SOTA) 모델이다.

## Motivation

- **Known**: 최근 GPT-4o, Claude 등의 멀티모달 대형언어모델(MLLM)이 발전하면서 GUI 에이전트 개발이 가능해졌으나, 현존 방법들의 성능은 여전히 낮음(~11%)
  
- **Gap**: GUI 에이전트가 해결해야 할 세 가지 핵심 문제
  1. 빠르게 변화하는 다양한 애플리케이션의 도메인 지식 부족
  2. 장기 지평(long-horizon) 멀티스텝 작업의 계획 어려움
  3. 동적이고 비균형적인 GUI 인터페이스 처리

- **Why**: 컴퓨터 자동화는 개별 사용자의 데이터 입력, 일정 관리 등의 작업 효율화뿐만 아니라 장애인의 기술 접근성을 획기적으로 개선할 수 있음

- **Approach**: 외부 웹 지식과 내부 에피소드 메모리를 활용한 경험 강화 계층적 계획, 자체 평가 기반 연속적 메모리 업데이트, 그리고 언어 중심 ACI를 통한 정확한 GUI 제어

## Achievement

![Figure 2: Agent S vs. OSWorld Agent results across five broad computer task categories.](figures/fig2.webp)

1. **OSWorld 벤치마크 성능 대폭 향상**: 11.21%에서 20.58%로 개선(9.37%p 절대 향상, 83.6% 상대 향상), 새로운 SOTA 달성. 5개 카테고리(Operating System, Office, Daily, Professional Workflow) 모두에서 일관된 개선

2. **WindowsAgentArena 일반화 검증**: 명시적 적응 없이도 13.3%에서 18.2%로 성능 향상, 서로 다른 운영체제 간 높은 일반화 능력 입증

## How

![Figure 3: Overview of the Agent S framework. Given task Tu and initial environment observation o0, the Manager conducts experience-augmented hierarchical planning using web knowledge and narrative memory to produce subtasks s0, . . . , sn. For each si, Worker wi draws from episodic memory to generate an action at at time t, which is executed by the ACI to return the next immediate observation ot+1.](figures/fig3.webp)

**세 가지 핵심 요소:**

### 3.1 경험 강화 계층적 계획(Experience-Augmented Hierarchical Planning)

- **Manager 모듈**: 사용자 작업과 현재 환경 관찰을 입력으로 받아 "How to do X" 형식의 쿼리 생성
  - Online Web Search(Perplexica 엔진): 최신 외부 지식 검색
  - Narrative Memory 검색: 과거 성공/실패 작업의 추상적 요약 검색
  - 두 가지 정보원을 융합하여 복잡한 작업을 실행 가능한 서브태스크(S₀...Sₙ)로 분해

- **Worker 모듈**: 각 서브태스크별 실행
  - Episodic Memory에서 단계적 실행 경험 검색
  - Action Generator가 구체적 행동(aₜ) 생성
  - ACI를 통해 환경에 실행하고 즉시 피드백(oₜ₊₁) 수신

### 3.2 연속적 메모리 업데이트(Continual Memory Update)

- **자체 평가자(Self-Evaluator)**: 인간 피드백 없이 서브태스크 성공/실패 자동 평가
  
- **Narrative Memory(요약 메모리)**: 성공/실패 전체 작업 궤적의 추상적 요약 저장
  - 구체적 행동 제거하여 일반화 가능성 향상
  
- **Episodic Memory(에피소드 메모리)**: 세부 단계별 행동 순서 저장
  - 서브태스크 실행 시 구체적 지침 제공

### 3.3 Agent-Computer Interface(ACI)

- **이중 입력 전략(Dual-Input Strategy)**:
  1. 시각 입력: 스크린샷으로 환경 변화 감지
  2. 이미지 증강 접근성 트리: 모든 유효한 GUI 요소의 정확한 위치 정보(ID) 제공

- **제한된 행동 공간(Bounded Action Space)**:
  - 언어 기반 원시 행동(click(element_id), type(), drag_and_drop() 등)
  - MLLM의 상식적 추론에 최적화
  - 적절한 시간 해상도에서 환경 전환 가능

- **OCR 강화**: 텍스트 인식으로 요소 그라운딩 정확도 향상

## Originality

- **통합적 프레임워크**: 웹 지식 검색, 내부 경험 메모리, 계층적 계획, ACI를 일관되게 통합한 첫 시도
  
- **자체 평가 기반 연속 학습**: 인간 주석 없이 성공/실패를 자동으로 판별하고 메모리에 저장하는 폐쇄 루프 시스템

- **Narrative + Episodic 이원 메모리 구조**: 계획 단계에서는 추상적 요약을, 실행 단계에서는 구체적 행동을 각각 활용하는 차별화된 메모리 구성

- **ACI의 GUI 에이전트 확장**: 소프트웨어 공학 분야의 ACI 개념을 GUI 자동화에 맞게 재해석하고 실장

## Limitation & Further Study

- **메모리 확장성**: 장기간 누적된 경험 메모리가 검색 효율성에 미치는 영향 미분석

- **에러 분석 부재**: 논문 초반부에는 상세한 실패 원인 분석이 부재함 (다만 "comprehensive error analysis"를 언급했으므로 전체 논문에는 포함 가능)

- **도메인 특화 성능**: 각 도메인(Office, Professional)별 성능 편차가 존재하며, 특정 도메인의 낮은 성능 개선 원인에 대한 심층 분석 필요

- **일반화의 한계**: 모바일(Android) 환경이나 웹 환경으로의 확장 가능성 미검증

- **후속 연구 방향**:
  - 장기 메모리 관리 및 망각 메커니즘(forgetting mechanism) 도입
  - 다중 에이전트 협업 체계 구축
  - 사용자별 맞춤형 경험 메모리 구성
  - 실시간 환경 변화에 대한 적응 메커니즘 강화

## Evaluation

- **Novelty**: 4.5/5
  - 웹 지식 + 내부 메모리 + 계층적 계획의 통합은 새로움
  - 다만 개별 요소들(RAG, hierarchical planning, memory)의 개념은 기존 연구에서 차용
  - ACI의 GUI 적용이 가장 창의적인 부분

- **Technical Soundness**: 4/5
  - 전체 파이프라인의 설계가 논리적이고 실행 가능
  - 자체 평가 메커니즘의 신뢰성에 대한 충분한 검증 필요 (오류 전파 위험성)
  - 메모리 검색 효율성 분석 부족

- **Significance**: 4.5/5
  - GUI 자동화 분야의 실질적 성능 향상(83.6% 상대 개선)은 상당히 의미 있음
  - OSWorld와 WindowsAgentArena 두 벤치마크 검증으로 신뢰도 상승
  - 실제 데스크톱 환경 자동화의 실용성 향상

- **Clarity**: 3.5/5
  - 프레임워크의 전체 개요는 명확하나, 메모리 구성 및 업데이트 프로세스의 세부 설명이 다소 복잡
  - Figure 3의 구성 요소 간 상호작용 흐름이 한 번에 파악하기 어려움
  - Narrative Memory와 Episodic Memory의 구분이 명확하지 않은 부분 있음

- **Overall**: 4/5

**총평**: Agent S는 웹 지식 검색과 이원 메모리 시스템을 통해 GUI 자동화의 장기 계획 문제를 효과적으로 해결하고, 83.6%의 상대 성능 개선으로 실질적 기여를 입증한 우수한 연구이다. 다만 자체 평가 메커니즘의 신뢰성 검증과 메모리 관리의 확장성에 대한 더 깊은 분석이 보완되면 완성도가 높아질 것이다.

## Related Papers

- 🔄 다른 접근: [[papers/849_UI-TARS_Pioneering_Automated_GUI_Interaction_with_Native_Age/review]] — Agent S와 UI-TARS는 모두 GUI 자동화를 다루지만, 인간과 유사한 컴퓨터 사용과 네이티브 에이전트 기반 자동화라는 서로 다른 접근 방식을 채택합니다.
- 🔗 후속 연구: [[papers/871_WebAgent-R1_Training_Web_Agents_via_End-to-End_Multi-Turn_Re/review]] — Agent S의 GUI 자동화 프레임워크는 WebAgent-R1의 웹 에이전트 훈련 기법을 확장하여 더 넓은 범위의 데스크톱 응용프로그램까지 포괄하는 범용 자동화를 실현합니다.
