---
title: "325_Executable_Code_Actions_Elicit_Better_LLM_Agents"
authors:
  - "Xingyao Wang"
  - "Yangyi Chen"
  - "Lifan Yuan"
  - "Yizhe Zhang"
  - "Yunzhu Li"
date: "2024"
doi: "10.48550/arXiv.2402.01030"
arxiv: ""
score: 4.3
essence: "LLM 에이전트의 액션 공간을 통합하기 위해 실행 가능한 Python 코드를 직접 사용하는 CodeAct 프레임워크를 제안하며, 기존의 JSON/텍스트 기반 액션 방식 대비 최대 20% 높은 성공률을 달성한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Language_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2024_Executable Code Actions Elicit Better LLM Agents.pdf"
---

# Executable Code Actions Elicit Better LLM Agents

> **저자**: Xingyao Wang, Yangyi Chen, Lifan Yuan, Yizhe Zhang, Yunzhu Li | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2402.01030](https://doi.org/10.48550/arXiv.2402.01030)

---

## Essence

![Figure 1](figures/fig1.webp) *CodeAct와 Text/JSON 액션의 비교: (상) 다양한 액션 형식 간 예시 비교, (하) M3ToolEval 벤치마크에서의 정량적 결과*

LLM 에이전트의 액션 공간을 통합하기 위해 실행 가능한 Python 코드를 직접 사용하는 CodeAct 프레임워크를 제안하며, 기존의 JSON/텍스트 기반 액션 방식 대비 최대 20% 높은 성공률을 달성한다.

## Motivation

- **Known**: LLM 에이전트는 일반적으로 JSON이나 사전 정의된 텍스트 형식으로 액션을 생성하도록 프롬프트되고 있다. 이러한 방식은 다양한 성공 사례를 보여주고 있으나, 도구 호출(tool invocation)과 로봇 제어 등의 실제 응용에 활용되고 있다.

- **Gap**: 기존 JSON/텍스트 기반 액션 방식은 (1) 사전 정의된 도구 범위로 제한되는 액션 공간, (2) 여러 도구 합성 불가능 등의 제약이 존재한다. 코드 기반 액션을 사용한 선행 연구들도 동적으로 환경 피드백에 반응하거나 액션을 조정하는 데 어려움을 겪고 있다.

- **Why**: 현대 LLM들은 대규모 코드 데이터로 사전학습되어 프로그래밍 언어에 친숙하며, Python은 제어 흐름(control flow)과 데이터 흐름(data flow)을 네이티브로 지원하여 복잡한 논리 연산을 단일 액션으로 표현할 수 있다.

- **Approach**: 실행 가능한 Python 코드를 통합 액션 공간으로 사용하고, Python 인터프리터와 통합하여 다중턴 상호작용을 통해 동적으로 액션을 조정 및 개선하는 CodeAct 프레임워크를 제안한다.

## Achievement

![Figure 2](figures/fig2.webp) *LLM 에이전트의 일반적 다중턴 상호작용 프레임워크: 에이전트, 사용자, 환경의 역할을 나타내며 CodeAct의 역할과 데이터 수집의 동기를 설명한다.*

1. **광범위한 실증적 검증**: 17개 LLM(오픈소스 및 폐쇄형)에 대한 실험으로 CodeAct의 우수성 입증. 기본 도구 호출 작업(API-Bank)에서는 대부분의 모델이 기준선과 동등하거나 우수한 성능 달성.

2. **복잡한 작업에서의 성능 향상**: 새로운 벤치마크 M3ToolEval (82개 인간 큐레이션 작업)에서 최대 20% 절대 성공률 향상 및 액션 수 30% 감소. 모델 능력이 증가할수록 성능 격차 확대.

3. **실용적 에이전트 개발**: CodeActInstruct (7k 다중턴 상호작용) 데이터셋 수집 및 이를 활용한 CodeActAgent (Llama2, Mistral 기반) 개발. 모델 학습, 데이터 시각화 등 고도화된 작업을 기존 Python 패키지로 자동 디버깅 능력과 함께 수행.

4. **일반 능력 보존**: 기존 지시 튜닝 데이터와 함께 사용하여 에이전트 작업 성능 개선 동시에 일반 능력(QA, 코딩, 지시 따르기) 유지.

## How

![Figure 3](figures/fig3.webp) *CodeActAgent (Mistral-7b)와의 Python 패키지 다중턴 상호작용 예시: 컨텍스트 내 시연 없이 고도화된 작업 수행*

- **CodeAct 프레임워크**: Python 코드를 실행 가능한 액션으로 사용하며, Python 인터프리터와 통합하여 코드 실행 결과와 오류 메시지를 관찰(observation)으로 수신

- **다중턴 상호작용**: 에이전트가 관찰(실행 결과, 오류)을 기반으로 동적으로 이전 액션을 조정하거나 새로운 액션을 발행. Chain-of-Thought와 자가 반성(self-reflection) 포함

- **통합 액션 공간**: 컴퓨터 환경(정보 검색, 소프트웨어 패키지 사용, 외부 메모리) 및 물리적 환경(로봇 계획)과 상호작용하는 다양한 작업을 단일 프레임워크로 처리

- **지시 튜닝 데이터**: 에이전트-환경 상호작용(컴퓨터/물리적 세계)과 자가 개선 행동(self-improvement planning)을 중심으로 선별된 7k 다중턴 궤적. 기존 대화 데이터와 혼합하여 일반 능력 유지

- **자동 디버깅**: Python의 오류 메시지(traceback) 등 기존 프로그래밍 인프라의 자동 피드백 메커니즘 활용으로 LLM이 자율적 오류 수정 수행

## Originality

- **새로운 액션 표현 패러다임**: JSON/텍스트 기반 액션에서 벗어나 실행 가능한 Python 코드를 통합 액션 공간으로 사용하는 혁신적 접근. 기존 코드 기반 연구와 달리 동적 환경 피드백과 다중턴 상호작용을 체계적으로 설계

- **포괄적 이론적 배경**: 코드의 4가지 주요 장점(사전학습 데이터 풍부성, 복잡 연산 지원, 기존 소프트웨어 패키지 활용, 자동화된 피드백 메커니즘)을 명확히 정의하고 실증적으로 검증

- **대규모 벤치마크 개발**: 82개 인간 큐레이션 작업으로 구성된 M3ToolEval 벤치마크 신규 도입으로 다중 도구 조합 작업의 평가 기준 제시

- **고품질 데이터셋 구축**: 다중턴 에이전트-환경 상호작용에 초점을 맞춘 CodeActInstruct (7k 궤적)의 신중한 데이터 선별로 자가 개선(self-debugging) 능력 강조

- **재현성과 개방성**: 코드, 데이터, 모델, 데모를 모두 공개하여 커뮤니티의 추가 연구 용이

## Limitation & Further Study

- **프로그래밍 언어 의존성**: Python 중심 설계로 다른 프로그래밍 언어나 도메인 특화 언어(Domain-Specific Language)로의 확장 가능성이 제한적. 다국어 코드 실행 환경과의 호환성 연구 필요

- **보안 및 신뢰성**: 임의의 Python 코드 실행 시 보안 위험 존재. 샌드박싱, 코드 검증, 권한 제어 등의 안전 메커니즘 강화 필요

- **에러 복구 한계**: 자동 디버깅이 복잡한 오류나 환경 의존적 오류에 대해 제한적일 수 있으며, 반복적 오류에 대한 수렴성 보장 부재

- **벤치마크 다양성**: M3ToolEval이 주로 정보 검색, 소프트웨어 패키지 사용 등에 집중되어 물리적 로봇 제어나 실시간 상호작용의 검증 부족

- **후속 연구**: (1) 더 광범위한 프로그래밍 언어 지원, (2) 실시간 시스템 환경에서의 성능 평가, (3) 보안 샌드박싱 기술 고도화, (4) 멀티모달 환경(시각, 음성 입력)과의 통합


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.3/5

**총평**: CodeAct는 LLM 에이전트의 액션 공간 표현에 대한 패러다임 전환을 제시하며, 광범위한 실증적 검증과 실용적 에이전트 개발을 통해 높은 실용 가치를 입증했다. 다만 보안, 신뢰성, 프로그래밍 언어 다양성 측면의 개선과 물리적 환경에서의 추가 검증이 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/655_ReAct_Synergizing_Reasoning_and_Acting_in_Language_Models/review]] — ReAct의 추론-행동 패러다임을 코드 실행 기반으로 구체화하여 실행 가능한 행동으로 확장한다.
