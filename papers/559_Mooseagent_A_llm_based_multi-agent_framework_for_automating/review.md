---
title: "559_Mooseagent_A_llm_based_multi-agent_framework_for_automating"
authors:
  - "Tao Zhang"
  - "Zhenhai Liu"
  - "Yong Xin"
  - "Yongjun Jiao"
date: "2025"
doi: "미제공"
arxiv: ""
score: 4.0
essence: "본 논문은 대규모 언어 모델(LLM)과 다중 에이전트 기술을 활용하여 복잡한 유한요소법(FEM) 기반 Moose 멀티피직스 시뮬레이션의 자동화를 달성한 MooseAgent 시스템을 제안한다. 자연언어 요구사항으로부터 자동으로 Moose 입력 파일을 생성하여 평균 93%의 성공률을 달성했다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Scientific_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhang et al._2025_Mooseagent A llm based multi-agent framework for automating moose simulation.pdf"
---

# Mooseagent: A llm based multi-agent framework for automating moose simulation

> **저자**: Tao Zhang, Zhenhai Liu, Yong Xin, Yongjun Jiao | **날짜**: 2025 | **DOI**: [미제공](https://doi.org/)

---

## Essence

![Figure 1](figures/fig1.webp)
*MooseAgent의 전체 프레임워크 개요: 사용자 요구사항으로부터 Moose 시뮬레이션 결과까지의 자동화된 워크플로우*

본 논문은 대규모 언어 모델(LLM)과 다중 에이전트 기술을 활용하여 복잡한 유한요소법(FEM) 기반 Moose 멀티피직스 시뮬레이션의 자동화를 달성한 MooseAgent 시스템을 제안한다. 자연언어 요구사항으로부터 자동으로 Moose 입력 파일을 생성하여 평균 93%의 성공률을 달성했다.

## Motivation

- **Known**: 유한요소법과 Moose 멀티피직스 프레임워크는 구조역학, 열전달, 전자기장 해석 등 다양한 분야에서 강력한 도구로 활용되고 있으며, 특히 원자력 분야에서 광범위하게 적용되고 있다.

- **Gap**: 전통적인 FEM 시뮬레이션 워크플로우는 형상 생성, 메시 생성, 해석기 매개변수 설정, 결과 시각화 등 복잡한 과정을 요구하고 높은 전문성을 필요로 하여 기술적 진입장벽이 높다. 특히 Moose는 높은 자유도와 복잡한 설정으로 인해 습득이 어렵다.

- **Why**: 최근 LLM과 다중 에이전트 시스템(MAS)의 발전은 자연언어 이해, 지식 추론, 작업 자동화에서 뛰어난 잠재력을 보여주고 있으며, OpenFOAM 및 FLUKA 같은 복잡한 시뮬레이션 소프트웨어 자동화에 이미 성공적으로 적용되었다.

- **Approach**: LLM 기반 다중 에이전트 시스템, 검색 증강 생성(RAG), 벡터 지식 데이터베이스, 다중 반복 검증 메커니즘을 결합하여 사용자의 자연언어 요구사항을 Moose 입력 파일로 자동 변환한다.

## Achievement

![Figure 2](figures/fig2.webp)
*자동 주석 워크플로우: 미주석 입력 파일에서 상세 주석이 포함된 입력 파일로의 자동화 프로세스*

1. **높은 자동화 성공률**: 열전달, 역학 등 전형적인 물리 사례에서 평균 93%의 성공률 달성

2. **경제성**: 사례당 평균 1원 미만의 비용으로 매우 낮은 운영 비용 실현

3. **포괄적 지식 데이터베이스 구축**: Moose 공식 저장소에서 수집한 8,000개 이상의 주석 처리된 입력 파일과 모든 함수의 상세 문서화로 구성된 벡터 데이터베이스 구축

4. **개방형 소프트웨어**: 코드를 GitHub에 오픈소스로 공개하여 커뮤니티 기여 기반 마련

## How

- **작업 분해(Task Decomposition)**: 사용자 요구사항을 "정렬(Alignment)", "입력 파일 작성(Write Input Card)", "실행-분석-수정(Execute-Analyze-Correct)" 세 가지 주요 단계로 분해

- **멀티 에이전트 협업**: LangGraph 기반 각 에이전트에 고유한 역할과 프롬프트를 할당하여 순차적 또는 비동기적 작업 수행

- **검색 증강 생성(RAG)**: BGE-M3 임베딩 모델로 텍스트를 벡터화하고 FAISS 데이터베이스에 저장하여 유사도 기반 상위 3개 청크 검색

- **반복적 검증 및 수정**: 최대 3회까지 실행-분석-수정 루프를 통해 입력 파일 오류를 체계적으로 해결하며, 반복되는 오류는 다른 구현 방식 제안

- **하이브리드 LLM 활용**: 입력 파일 생성에는 추론 능력이 뛰어난 Deepseek-R1 사용, 나머지 모듈은 Deepseek-V3로 처리하여 효율성과 품질 균형

- **자동 주석 워크플로우**: 미주석 입력 파일에서 Moose 함수 설명을 검색하여 LLM이 상세 주석을 자동으로 생성하는 반복적 프로세스

- **온도 매개변수 최적화**: Temperature를 0.01로 설정하여 생성 텍스트의 무작위성을 최소화하고 결정론적 출력 보장

## Originality

- **새로운 응용 영역**: FEM 해석 분야, 특히 복잡한 멀티피직스 결합 플랫폼인 Moose에 LLM 기반 다중 에이전트 자동화 시스템을 처음으로 적용

- **포괄적 지식 베이스 구축**: 8,000개 이상의 자동 주석 처리된 입력 파일과 함수 문서를 체계적으로 수집·처리하여 도메인 특화 RAG 지식 데이터베이스 구축

- **다층적 오류 처리 메커니즘**: 반복되는 오류 인식, 다른 구현 방식 제안, 전담 Moose Assistant를 통한 기술 지원 등 단계적 오류 해결 전략

- **실용적 다중 에이전트 아키텍처**: 작업 분해, 역할 할당, 상호작용 정의를 명확히 하여 효율적인 다중 에이전트 협업 실현

- **비용 효율성 검증**: 사례당 1원 미만의 비용으로 경제적 실행 가능성을 입증

## Limitation & Further Study

- **반복 횟수 제한의 명확한 분석 부족**: 3회 반복 횟수가 최적인 이유에 대한 이론적 분석이 제한적이며, 문제의 복잡도에 따른 적응형 반복 메커니즘 개발 필요

- **평가 사례의 제한성**: 논문에서는 9가지 테스트 사례만 제시되었으며, 더 복잡한 멀티피직스 결합 문제(유체-구조 상호작용, 전자기-열 결합 등)에 대한 평가 부족

- **할루시네이션(Hallucination) 완전 제거 불가**: RAG 기반 접근에도 불구하고 LLM의 근본적인 할루시네이션 문제를 완전히 해결하지 못함

- **사용자 대화 품질 평가 부재**: 정렬 단계에서 사용자와의 상호작용 품질과 명확화 대화의 효율성에 대한 정량적 평가 결여

- **후속 연구 방향**:
  - 고급 연료 또는 원자로 설계 지능 에이전트로의 확장
  - 다양한 복잡도의 멀티피직스 문제에 대한 확장성 검증
  - 강화 학습을 통한 다중 에이전트 협업 전략의 자동 최적화
  - 사용자 피드백 루프를 통한 지식 데이터베이스의 동적 업데이트 메커니즘


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: MooseAgent는 LLM과 다중 에이전트 기술을 유한요소법 시뮬레이션 분야에 창의적으로 적용하여 높은 자동화 성공률(93%)을 달성한 실용적이고 가치 있는 시스템이다. 특히 오픈소스 공개와 경제성 입증은 산업 적용 가능성을 높이나, 더 다양한 멀티피직스 문제에 대한 확장성 검증과 이론적 분석 강화가 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/535_MetaOpenFOAM_an_LLM-based_multi-agent_framework_for_CFD/review]] — MetaOpenFOAM과 MooseAgent 모두 CFD 시뮬레이션 자동화를 위한 LLM 기반 다중 에이전트 프레임워크이지만 서로 다른 시뮬레이션 플랫폼을 대상으로 한다.
- 🔗 후속 연구: [[papers/587_OpenFOAM_The_Open_Source_Computational_Fluid_Dynamics_Toolbo/review]] — OpenFOAMGPT 2.0의 계산유체역학 자동화 시스템은 Moose 멀티피직스 시뮬레이션 자동화와 유사한 접근방식을 유체역학에 적용한다.
- 🏛 기반 연구: [[papers/103_Architectures_variants_and_performance_of_neural_operators_A/review]] — 신경 연산자의 아키텍처와 변형에 대한 연구는 MooseAgent가 복잡한 유한요소법 시뮬레이션을 자동화하는 이론적 배경을 제공한다.
