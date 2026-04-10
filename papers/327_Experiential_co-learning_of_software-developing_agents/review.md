---
title: "327_Experiential_co-learning_of_software-developing_agents"
authors:
  - "Cheng Qian"
  - "Yufan Dang"
  - "Jiahao Li"
  - "Wei Liu"
  - "Weize Chen"
date: "2023"
doi: "N/A"
arxiv: ""
score: 4.1
essence: "본 논문은 대규모 언어모델(LLM) 기반 다중 에이전트 시스템이 과거 작업 경험을 축적하고 활용하는 \"경험적 협력학습(Experiential Co-Learning)\" 프레임워크를 제안한다. 이를 통해 소프트웨어 개발 작업에서 반복적인 오류를 감소시키고 에이전트 간의 협력 효율성을 현저히 향상시킨다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Code_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Qian et al._2023_Experiential co-learning of software-developing agents.pdf"
---

# Experiential co-learning of software-developing agents

> **저자**: Cheng Qian, Yufan Dang, Jiahao Li, Wei Liu, Weize Chen, Cheng Yang, Zhiyuan Liu, Maosong Sun | **날짜**: 2023 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*Experiential Co-Learning 프레임워크: Co-Tracking, Co-Memorizing, Co-Reasoning 세 모듈을 통해 Instructor와 Assistant 에이전트가 과거 경험을 학습하고 활용하여 소프트웨어 개발 작업을 효율적으로 수행*

본 논문은 대규모 언어모델(LLM) 기반 다중 에이전트 시스템이 과거 작업 경험을 축적하고 활용하는 "경험적 협력학습(Experiential Co-Learning)" 프레임워크를 제안한다. 이를 통해 소프트웨어 개발 작업에서 반복적인 오류를 감소시키고 에이전트 간의 협력 효율성을 현저히 향상시킨다.

## Motivation

- **Known**: 최근 LLM 기반 자율 에이전트는 복잡한 작업을 수행할 수 있으며, 다중 에이전트 협력(예: ChatDev)을 통해 소프트웨어 개발 작업의 자동화가 가능해졌다. 에이전트 간 통신과 작업 분할을 통해 상당한 성과를 보이고 있다.

- **Gap**: 기존 다중 에이전트 협력 방법들은 각 작업을 독립적으로 처리하며, 과거 완료된 작업에서 누적된 경험을 효과적으로 활용하는 방법론이 부재하다. 이로 인해 유사한 작업에서도 반복적인 오류와 불필요한 시행착오가 발생한다.

- **Why**: 소프트웨어 개발은 자연언어와 프로그래밍 언어의 조합, 지속적인 코드 수정, 객관적인 피드백이 필요한 복잡한 작업이다. 다중 에이전트의 협력 역학을 체계적으로 개선할 수 있는 대표적인 도메인이다.

- **Approach**: 과거 작업 궤적(trajectory)에서 "지름길(shortcut)"을 추출하여 경험 풀(experience pool)을 구축하고, 새로운 작업 해결 시 이러한 경험을 활용하는 세 가지 모듈(Co-Tracking, Co-Memorizing, Co-Reasoning)을 제안한다.

## Achievement

![Figure 1](figures/fig1.webp)

1. **경험 기반 협력학습의 첫 시도**: LLM 기반 다중 에이전트 협력에 과거 경험을 통합한 최초의 연구로, Co-Tracking/Co-Memorizing/Co-Reasoning을 통해 Instructor와 Assistant 역할의 에이전트 간 협력학습을 실현했다.

2. **작업 실행 그래프 기반 지름길 추출**: 절차적 궤적에서 인접하지 않은 노드를 연결하는 "지름길"을 추출하여 에이전트의 단축 사고(shortcut thinking)를 유도하는 혁신적 경험 표현 방식을 제안했다.

3. **다각적 검증**: 소프트웨어 개발의 다양한 작업에 대해 광범위한 실험을 수행하여, 제안된 프레임워크가 에이전트의 협력 품질과 효율성을 유의미하게 향상시킴을 입증했다.

## How

![Figure 3](figures/fig3.webp)
*작업 실행 그래프의 주요 요소 분포: 에지(instruction), 상태 전환, 지름길의 구성 비율*

### Co-Tracking 모듈
- Instructor 에이전트와 Assistant 에이전트 간의 통신을 추적하여 **절차적 궤적(procedural trajectory)** 수집
- 각 궤적은 교육(instructions) $I = \{i_1, i_2, \cdots, i_n\}$과 해결책(solutions) $S = \{s_1, s_2, \cdots, s_n\}$ 쌍으로 구성
- 지향성 체인(directed chain) $G = (N, E)$로 모델링하여 작업 실행의 동적 진행 과정을 명확히 기록

### Co-Memorizing 모듈
- **상태 전환 그래프** 생성: 체인의 동일 내용 노드들을 해시 함수 $\phi$를 통해 통합하여 중복 제거
- **지름길 추출**: 인접하지 않은 노드 간의 직접 연결을 식별하여 비효율적인 단계를 건너뛸 수 있는 경험으로 저장
- 외부 환경 피드백(컴파일 성공, 테스트 통과 등)을 이용한 휴리스틱 기반 필터링

### Co-Reasoning 모듈
- 새로운 작업 해결 시 **키-값(key-value) 경험 풀** 활용
- Instructor와 Assistant가 각각의 경험 풀을 참조하여 개선된 지시사항과 해결책 생성
- 의미적 유사성(semantic similarity) 기반 관련 경험 검색 및 활용

## Originality

- **다중 에이전트 경험 학습의 선구성**: 기존의 단일 에이전트 경험 학습(예: Reflexion, ExpeL)을 다중 에이전트 협력 맥락으로 확장하여 Instructor와 Assistant 역할별 경험 축적을 구현한 첫 연구

- **작업 실행 그래프 기반 지름길 개념**: 절차적 궤적을 그래프로 변환하고 상태 중복을 제거한 후, 비인접 노드 연결을 지름길로 추출하는 혁신적 경험 표현 방식

- **Shortcut 기반 사고 유도**: 단순한 성공 궤적 저장이 아니라, 불필요한 단계를 건너뛸 수 있는 더 효율적인 경로를 추출하여 에이전트의 추론 시 직관적 활용을 가능하게 함

- **협력학습의 체계화**: Co-Tracking(궤적 수집) → Co-Memorizing(경험 추출) → Co-Reasoning(경험 활용)의 명확한 세 단계 프레임워크로 다중 에이전트 경험 학습을 체계적으로 설계

## Limitation & Further Study

- **작업 도메인 제한**: 소프트웨어 개발 도메인에 특화된 설계로, 다른 도메인(이미지 생성, 과학 연구 등)으로의 일반화 가능성이 불명확하다.

- **경험 표현의 단순성**: Key-Value 형식의 경험 풀이 복잡한 인과관계나 조건부 상황을 충분히 표현하지 못할 가능성이 있다.

- **확장성 문제**: 작업이 증가함에 따라 경험 풀의 규모가 증가하면, 관련 경험 검색의 효율성과 LLM의 문맥 길이 제약이 병목이 될 수 있다.

- **지름길 추출의 완전성**: 휴리스틱 기반 필터링으로 인해 시험-오류 과정에서의 가치 있는 음의 경험(실패 경험)을 충분히 캡처하지 못할 수 있다.

- **향후 연구 방향**:
  - 계층적 경험 표현과 동적 메모리 관리 기법 개발
  - 다중 도메인 적응을 위한 일반화된 경험 추출 알고리즘
  - 장기적 협력학습에서의 경험 망각(experience forgetting) 메커니즘 도입
  - 인간 전문가의 피드백을 활용한 경험 품질 개선 방법론

## Evaluation

- **Novelty**: 4.5/5
  - 다중 에이전트 협력 맥락에서 경험 학습을 처음 도입했으나, 단일 에이전트 경험 학습 연구의 자연스러운 확장이라는 점에서 완전히 새로운 개념은 아님

- **Technical Soundness**: 4/5
  - Co-Tracking, Co-Memorizing, Co-Reasoning의 세 모듈이 논리적으로 일관되고, 작업 실행 그래프와 지름길 추출 방식이 타당함
  - 다만 경험 필터링의 휴리스틱 기반 접근이 이론적 근거가 충분하지 않을 수 있음

- **Significance**: 4/5
  - 실제 소프트웨어 개발 작업 자동화에 실질적인 효율성 개선을 제시하며, 다중 에이전트 협력 연구에 중요한 기여
  - 하지만 도메인 특화성으로 인한 일반화 가능성의 제한이 영향력을 다소 감소시킴

- **Clarity**: 4/5
  - 논문의 구조와 개념 설명이 명확하며, Figure 1이 프레임워크를 직관적으로 보여줌
  - 일부 휴리스틱 기반 설계 선택의 동기가 더 명시적으로 설명될 수 있음

- **Overall**: 4.1/5

**총평**: 본 논문은 LLM 기반 다중 에이전트의 협력학습에 경험 축적과 활용이라는 중요한 개념을 처음 도입한 의미 있는 연구이며, 작업 실행 그래프 기반 지름길 추출이라는 창의적인 방법론을 제시한다. 실제 소프트웨어 개발 자동화에서의 효율성 증대를 입증했으나, 도메인 특화성과 경험 표현의 단순성이 향후 개선 과제로 남아있다.

## Related Papers

- 🔄 다른 접근: [[papers/205_Chatdev_Communicative_agents_for_software_development/review]] — 다중 에이전트 소프트웨어 개발에서 커뮤니케이션 기반 협력 방식의 다른 접근법을 제시한다.
- 🏛 기반 연구: [[papers/120_AutoGen_Enabling_Next-Gen_LLM_Applications_via_Multi-Agent_C/review]] — 차세대 LLM 애플리케이션을 위한 다중 에이전트 프레임워크의 이론적 토대를 제공한다.
- 🧪 응용 사례: [[papers/782_SWE-bench_Can_Language_Models_Resolve_Real-World_GitHub_Issu/review]] — 실제 GitHub 이슈 해결을 통해 경험적 협력학습의 효과를 검증할 수 있는 벤치마크를 제공한다.
- 🔗 후속 연구: [[papers/205_Chatdev_Communicative_agents_for_software_development/review]] — ChatDev의 협력적 소프트웨어 개발은 경험적 공동학습 연구의 소프트웨어 에이전트 학습 기법을 확장하여 실제 개발 프로세스에서 에이전트 간 지식 공유와 역할 전문화를 실현합니다.
