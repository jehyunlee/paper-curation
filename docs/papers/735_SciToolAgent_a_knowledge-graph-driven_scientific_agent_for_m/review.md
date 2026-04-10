---
title: "735_SciToolAgent_a_knowledge-graph-driven_scientific_agent_for_m"
authors:
  - "Keyan Ding"
  - "Jing Yu"
  - "Junjie Huang"
  - "Yuchen Yang"
  - "Qiang Zhang"
date: "2025"
doi: "10.1038/s43588-025-00849-y"
arxiv: ""
score: 4.3
essence: "본 논문은 대규모 언어 모델(LLM)을 과학 도구 지식 그래프(SciToolKG)와 통합하여 생물학, 화학, 재료과학 등 다양한 분야의 수백 개 과학 도구를 자동으로 활용할 수 있는 지능형 과학 에이전트를 제시한다. 복잡한 다중 도구 과학 워크플로우 자동화에서 기존 방식 대비 10% 이상의 성능 향상을 달성했다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Knowledge_Graph_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ding et al._2025_SciToolAgent a knowledge-graph-driven scientific agent for multitool integration.pdf"
---

# SciToolAgent: a knowledge-graph-driven scientific agent for multitool integration

> **저자**: Keyan Ding, Jing Yu, Junjie Huang, Yuchen Yang, Qiang Zhang | **날짜**: 2025 | **DOI**: [10.1038/s43588-025-00849-y](https://doi.org/10.1038/s43588-025-00849-y)

---

## Essence

![Figure 1](figures/fig1.webp)
*SciToolAgent의 전체 개요: (a) 다양한 생물학, 화학, 재료과학 도구 포함, (b) 도구 간 관계를 인코딩한 SciToolKG, (c) 계획-실행-요약의 LLM 기반 워크플로우*

본 논문은 대규모 언어 모델(LLM)을 과학 도구 지식 그래프(SciToolKG)와 통합하여 생물학, 화학, 재료과학 등 다양한 분야의 수백 개 과학 도구를 자동으로 활용할 수 있는 지능형 과학 에이전트를 제시한다. 복잡한 다중 도구 과학 워크플로우 자동화에서 기존 방식 대비 10% 이상의 성능 향상을 달성했다.

## Motivation

- **Known**: LLM은 자연언어 이해와 복잡한 추론 능력을 보여주고 있으며, Coscientist, ChemChat, ChemCrow 등 도구 통합 시스템들이 화학 및 생물학 분야에서 개발되어 왔음

- **Gap**: 기존 도구-LLM 통합 시스템들은 (1) 제한된 도구 세트(일반적으로 20개 미만)만 지원하고, (2) 도구 간의 의존성(sequential dependencies)을 고려하지 않으며, (3) 안전성과 윤리적 고려사항을 간과함

- **Why**: 도구 간 의존성을 명시적으로 모델링하지 않으면 복잡한 다단계 과학 워크플로우에서 최적의 해가 아닌 결과를 도출하게 되며, 자동화된 과학 발견의 윤리적 문제가 중요함

- **Approach**: (1) 도구 간의 관계, 입출력 형식, 안전 수준 등을 인코딩하는 과학 도구 지식 그래프(SciToolKG) 구축, (2) 그래프 기반 검색 증강 생성(graph-based RAG)을 통한 계획-실행-요약 파이프라인, (3) 안전 검사 모듈 통합

## Achievement

![Figure 2](figures/fig2.webp)
*다양한 에이전트와 기초 모델의 성능 비교: SciToolAgent는 Level-1(단일 도구), Level-2(다중 도구), 그리고 전체 성능에서 일관되게 최고의 결과 달성*

1. **벤치마크 성능**: 531개의 다양한 과학 문제로 구성된 SciToolEval 벤치마크에서 94%의 종합 정확도 달성, ReAct 및 Reflexion 대비 ~20%, ChemCrow/CACTUS 대비 10-12% 향상

2. **다중 도구 작업 강화**: Level-2(다중 도구) 문제에서 특히 우수한 성능 발휘, 복잡한 워크플로우 자동화 능력 입증 (최종 답변 정확도 94.01%)

3. **실제 응용 검증**: 단백질 설계 분석, 화학 반응성 예측, 화학 합성, MOF(Metal-Organic Framework) 스크리닝 등 4가지 실제 사례 연구를 통해 복잡한 과학 워크플로우 자동화 능력 입증

4. **모델 유연성**: GPT-4o, OpenAI-o1, Qwen2.5-72B 등 다양한 기초 모델에서 작동 가능하며, OpenAI-o1은 최고 성능(96.97%), GPT-4o는 비용-정확도 최적 균형 달성

## How

![Figure 3](figures/fig3.webp)
*단백질 설계 및 분석 워크플로우: SciToolAgent가 순차적으로 여러 생물정보학 도구를 통합하여 단백질 구조 예측 및 특성 분석 수행*

- **SciToolKG 구축**: 각 도구의 기능, 입출력 형식, 안전 수준, 선행 조건, 도구 간 호환성 등을 포함하는 포괄적인 지식 그래프를 수동으로 구성

- **계획 단계(Planner)**: LLM이 사용자 쿼리를 받아 SciToolKG 기반 검색 증강 생성으로 최적의 도구 체인을 생성

- **실행 단계(Executor)**: 계획된 도구들을 순차적으로 실행하며, 오류 발생 시 재시도 메커니즘 적용

- **안전 검사 모듈**: 도구 실행 과정에서 잠재적으로 해로운 응답을 식별하기 위해 안전 검사 데이터베이스 검색 활용

- **요약 단계(Summarizer)**: 다양한 도구의 출력을 종합하여 최종 답변 생성, 문제 해결 성공 여부 판단, 필요시 Planner에 도구 체인 개선 지시

- **메모리 모듈**: 최종 답변을 메모리에 저장하여 다음 쿼리의 컨텍스트로 활용

## Originality

- 수백 개의 과학 도구를 통합하는 최초의 대규모 멀티 도메인 과학 에이전트 시스템

- 도구 간의 의존성과 순차 관계를 명시적으로 모델링하는 과학 도구 지식 그래프(SciToolKG) 개발로, 기존 in-context learning 방식의 한계 극복

- 자동화된 과학 발견에 안전성 및 윤리 검사 모듈을 최초로 통합하여 책임감 있는 AI 과학 연구 추진

- 531개 문제로 구성된 포괄적인 과학 도구 평가 벤치마크(SciToolEval) 구축

- 다양한 기초 모델(proprietary/open-source, 대규모/소규모)에서의 확장성 입증

## Limitation & Further Study

- **지식 그래프 수동 구축**: SciToolKG를 수동으로 구성하므로 확장성에 한계가 있으며, 새로운 도구 추가 시 별도의 주석 작업 필요

- **도구 오류 처리**: 도구 실행 중 오류 발생 시 재시도만 수행하고 있으며, 더 정교한 오류 복구 메커니즘 부재

- **평가 범위 제한**: 531개 문제는 과학 분야의 전체 범위를 완전히 대표하지 못할 수 있으며, 더 광범위한 도메인 커버리지 필요

- **계산 비용**: LLM 기반 계획-실행-요약 파이프라인의 토큰 사용량 증가로 인한 계산 비용 미분석

- **도구 신뢰성**: 기저 도구들의 계산 오류나 부정확성에 대한 영향 평가 부족

- **후속 연구**: (1) 자동화된 지식 그래프 구축 방법론 개발, (2) 도구 오류 복구 및 롤백 메커니즘 강화, (3) 더 많은 과학 도메인으로의 확장, (4) LLM 기반 의사결정과 도구 신뢰성의 상호작용 분석

## Evaluation

- **Novelty**: 4.5/5 - 대규모 멀티 도메인 과학 도구 통합과 지식 그래프 기반 접근이 참신하나, 개별 기술들의 조합 성격

- **Technical Soundness**: 4/5 - 견고한 방법론이지만, 지식 그래프 수동 구축의 확장성 문제와 도구 오류 처리의 미흡함

- **Significance**: 4.5/5 - 과학 연구 도구 활용의 민주화와 자동화라는 중요한 문제 해결, 실제 사례 연구로 실용성 입증

- **Clarity**: 4/5 - 전체 시스템 설계와 평가 구성이 명확하나, 일부 기술적 세부사항(예: 안전 검사 모듈의 구체적 구현)은 상세하지 않음

- **Overall**: 4.3/5

**총평**: SciToolAgent는 과학 도구 자동화의 중요한 진전을 보여주는 체계적이고 포괄적인 시스템으로, 지식 그래프 기반 접근과 안전성 고려가 돋보인다. 다만 지식 그래프의 확장성 문제와 더 정교한 오류 처리 메커니즘 개발이 향후 과제이다.

## Related Papers

- 🏛 기반 연구: [[papers/769_StableToolBench_Towards_Stable_Large-Scale_Benchmarking_on_T/review]] — 안정적인 대규모 도구 벤치마킹이 과학 도구 지식 그래프 기반 에이전트의 평가 기반을 제공한다
- 🔗 후속 연구: [[papers/448_Kgvalidator_A_framework_for_automatic_validation_of_knowledg/review]] — 지식 그래프 검증 프레임워크를 과학 도구 지식 그래프의 품질 보장으로 확장할 수 있다
- 🧪 응용 사례: [[papers/499_LLM_With_Tools_A_Survey/review]] — 도구를 활용한 LLM 연구의 포괄적 조사를 과학 도구 특화 에이전트 개발에 적용할 수 있다
- 🔗 후속 연구: [[papers/769_StableToolBench_Towards_Stable_Large-Scale_Benchmarking_on_T/review]] — 대규모 도구 벤치마킹을 과학 도구 지식 그래프 기반의 특화된 평가로 확장할 수 있다
