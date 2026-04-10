---
title: "033_A_survey_on_large_language_model_based_autonomous_agents"
authors:
  - "Lei Wang"
  - "Chengbang Ma"
  - "Xueyang Feng"
  - "Zeyu Zhang"
  - "Hao-ran Yang"
date: "2023"
doi: "10.1007/s11704-024-40231-1"
arxiv: ""
score: 4.0
essence: "본 논문은 대규모 언어모델(LLM)을 기반으로 한 자율 에이전트의 구성, 응용, 평가에 대한 체계적 종합 리뷰를 제시한다. LLM의 광범위한 지식과 인간 수준의 지능을 활용하여 자율적 의사결정이 가능한 에이전트 구축 방법론을 통합 프레임워크로 제안한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Agent_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2023_A survey on large language model based autonomous agents.pdf"
---

# A survey on large language model based autonomous agents

> **저자**: Lei Wang, Chengbang Ma, Xueyang Feng, Zeyu Zhang, Hao-ran Yang | **날짜**: 2023 | **DOI**: [10.1007/s11704-024-40231-1](https://doi.org/10.1007/s11704-024-40231-1)

---

## Essence

![Figure 2](figures/fig2.webp)

*Fig. 2*

본 논문은 대규모 언어모델(LLM)을 기반으로 한 자율 에이전트의 구성, 응용, 평가에 대한 체계적 종합 리뷰를 제시한다. LLM의 광범위한 지식과 인간 수준의 지능을 활용하여 자율적 의사결정이 가능한 에이전트 구축 방법론을 통합 프레임워크로 제안한다.

## Motivation

- **Known**: 기존 자율 에이전트 연구는 제한된 환경에서 단순한 정책 함수로 학습되어 왔으나, 인간의 학습 과정과 큰 차이가 있다. 최근 LLM이 광대한 웹 지식을 통해 인간 수준의 지능을 보이면서 LLM 기반 에이전트 연구가 급증하고 있다.
- **Gap**: 기존 연구들은 메모리, 계획, 도구 사용 등 다양한 기능을 가진 LLM 기반 에이전트를 제안했으나, 이들을 체계적으로 정리하고 비교하는 종합적 분석이 부족하다. 에이전트 구성, 응용, 평가에 대한 통일된 프레임워크가 필요하다.
- **Why**: LLM 기반 자율 에이전트는 제한된 학습 환경을 벗어나 개방형 도메인에서 인간 수준의 의사결정을 가능하게 하며, 자연언어 인터페이스로 설명 가능성을 제공한다. 이는 AGI(인공 일반지능) 달성의 유망한 접근법으로 인정받고 있다.
- **Approach**: 저자들은 LLM 기반 에이전트를 (1) 아키텍처 설계와 (2) 능력 획득이라는 두 가지 관점에서 분석한다. 프로파일링, 메모리, 계획, 행동 모듈로 구성된 통합 프레임워크를 제안하고, 사회과학, 자연과학, 공학 분야의 응용 사례와 평가 전략을 종합적으로 검토한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Fig. 1*

- **통합 아키텍처 프레임워크**: 프로파일(Profile), 메모리(Memory), 계획(Planning), 행동(Action) 모듈로 구성된 통일된 LLM 기반 에이전트 설계 프레임워크를 제시하여 기존 다양한 접근법을 체계적으로 정리
- **에이전트 능력 획득 전략**: 핸드크래프팅, LLM 생성, 데이터셋 정렬 등 프로파일 생성 방법과 메모리 관리, 단일/다중 경로 추론 등 기능 강화 전략을 분류
- **광범위한 응용 도메인**: 사회과학(에이전트 시뮬레이션), 자연과학(과학 실험), 공학(소프트웨어 개발) 등 다양한 분야에서의 LLM 에이전트 응용 사례를 체계적으로 분석
- **평가 방법론**: 주관적 평가(인간 평가)와 객관적 평가(자동 메트릭)를 포함한 LLM 기반 에이전트 평가 전략을 종합적으로 검토
- **연구 동향 분석**: 2021년 1월부터 2023년 8월까지의 누적 논문 수 데이터를 통해 LLM 기반 자율 에이전트 연구 분야의 급속한 성장과 다양한 에이전트 카테고리의 출현을 시각화

## How

![Figure 2](figures/fig2.webp)

*Fig. 2*

- 에이전트 아키텍처의 네 가지 핵심 모듈을 정의: 프로파일링(역할 정의), 메모리(과거 경험 저장), 계획(미래 행동 계획), 행동(의사결정 실행)
- 프로파일 생성의 세 가지 전략 분류: 수동 작성(Handcrafting), LLM 자동 생성(LLM-Generation), 데이터셋 정렬(Dataset Alignment)
- 메모리 구조를 통합 메모리와 하이브리드 메모리로 구분하고 메모리 읽기/쓰기/반성 작업 정의
- 계획 모듈의 피드백 유무에 따라 분류: 환경 피드백, 인간 피드백, 모델 피드백 활용
- 행동 모듈의 행동 공간을 도구(Tools), 데이터베이스, 내부 상태, 환경 등으로 정의
- 2021-2023년 주요 에이전트 모델들(WebGPT, AutoGPT, Generative Agent, Voyager 등)의 시간 순 발표 추적을 통해 분야 발전 과정 분석

## Originality

- 첫 LLM 기반 자율 에이전트에 대한 포괄적 종합 리뷰로서, 산발적으로 제안된 다양한 에이전트 연구를 통합 프레임워크로 정리한 점이 독창적
- 아키텍처 설계와 능력 획득이라는 이원적 분석 틀(하드웨어vs소프트웨어)을 통해 LLM 기반 에이전트 구성의 본질을 새롭게 해석
- 사회과학, 자연과학, 공학이라는 광범위한 응용 도메인에서 LLM 에이전트의 활용 가능성을 체계적으로 분석한 점
- 주관적/객관적 평가 전략을 구분하여 LLM 에이전트 평가의 다면적 접근을 제시

## Limitation & Further Study

- 논문은 발췌본으로 제시되어 완전한 내용 분석이 제한적이며, 특히 구체적인 응용 사례와 평가 결과의 상세 분석이 부족함
- LLM 에이전트의 성능 한계(환각, 추론 오류, 신뢰도 문제) 및 실제 환경 적용 시 발생하는 문제들에 대한 깊이 있는 논의가 필요
- 메모리 관리의 확장성, 계획 모듈의 계산 효율성, 다중 에이전트 간 협력 메커니즘 등 구현 측면의 도전과제에 대한 구체적 해결 방안 부족
- 향후 연구 방향으로 에이전트의 안전성과 윤리 문제, 실시간 환경에서의 동적 학습 능력, 도메인 전이(Transfer Learning) 등을 더 깊이 있게 탐구할 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 LLM 기반 자율 에이전트 분야의 급속한 성장 속에서 기존 연구들을 체계적으로 정리하고 통합 프레임워크를 제시한 중요한 종합 리뷰이다. 에이전트 구성, 응용, 평가에 대한 포괄적 분석을 통해 향후 연구의 방향성을 제시하며, 분야 진입 연구자들에게 필수적인 배경 지식을 제공한다.

## Related Papers

- 🔗 후속 연구: [[papers/464_Large_Language_Model_based_Multi-Agents_A_Survey_of_Progress/review]] — LLM 기반 다중 에이전트의 진전과 도전과제를 포괄적으로 다루어 자율 에이전트 연구를 확장한다.
- ⚖️ 반론/비판: [[papers/760_Small_Language_Models_are_the_Future_of_Agentic_AI/review]] — 소형 언어모델이 에이전틱 AI의 미래라는 대안적 관점을 제시한다.
- 🏛 기반 연구: [[papers/823_Towards_a_Science_of_Scaling_Agent_Systems/review]] — 에이전트 시스템 확장의 과학적 기반을 제공한다.
- 🏛 기반 연구: [[papers/361_From_LLM_Reasoning_to_Autonomous_AI_Agents_A_Comprehensive_R/review]] — 자율 AI 에이전트 종합 리뷰의 기반이 되는 일반적인 에이전트 연구 조사
- 🏛 기반 연구: [[papers/625_PlanGenLLMs_A_Modern_Survey_of_LLM_Planning_Capabilities/review]] — 대규모 언어모델 기반 자율 에이전트 조사는 LLM 계획 수립 능력 분석의 이론적 기반을 제공합니다
- 🏛 기반 연구: [[papers/449_Kimi_k15_Scaling_reinforcement_learning_with_llms/review]] — 대규모 언어모델 기반 자율 에이전트 서베이는 Kimi k1.5의 강화학습 기반 에이전트 설계에 이론적 배경과 방법론적 근거를 제공한다.
- 🏛 기반 연구: [[papers/464_Large_Language_Model_based_Multi-Agents_A_Survey_of_Progress/review]] — 대형 언어 모델 기반 자율 에이전트 서베이가 멀티에이전트 시스템 설계의 이론적 토대를 제공합니다.
- 🔗 후속 연구: [[papers/784_Systematic_Framework_of_Application_Methods_for_Large_Langua/review]] — LLM 기반 자율 에이전트 연구를 언어과학 분야의 체계적 방법론으로 확장한다
- 🔗 후속 연구: [[papers/792_Text2world_Benchmarking_large_language_models_for_symbolic_w/review]] — 자율 에이전트 연구의 포괄적 조망에서 세계 모델링이라는 핵심 기능의 구체적 평가 방법을 제시한다.
- 🔗 후속 연구: [[papers/865_Vending-Bench_A_Benchmark_for_Long-Term_Coherence_of_Autonom/review]] — 자율 에이전트 설문조사의 구체적 벤치마크 구현으로 에이전트 평가 방법론을 확장한다.
- 🧪 응용 사례: [[papers/365_Future_of_Work_with_AI_Agents_Auditing_Automation_and_Augmen/review]] — 자율 에이전트에 대한 포괄적 조사로 업무 자동화 에이전트의 구체적 적용 가능성을 보여준다.
