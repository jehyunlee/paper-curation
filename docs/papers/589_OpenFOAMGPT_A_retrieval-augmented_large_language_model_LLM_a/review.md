---
title: "589_OpenFOAMGPT_A_retrieval-augmented_large_language_model_LLM_a"
authors:
  - "Sandeep Pandey"
  - "Ran Xu"
  - "Wenkang Wang"
  - "Xu Chu"
date: "2025"
doi: "10.1063/5.0257555"
arxiv: ""
score: 3.8
essence: "본 논문은 OpenFOAM 기반 전산유체역학(CFD) 시뮬레이션을 위해 검색 증강 생성(RAG) 기술로 강화된 대규모 언어모델(LLM) 기반 에이전트 OpenFOAMGPT를 제시한다. GPT-4o와 o1 preview 모델을 활용하여 영점 샷(zero-shot) 시뮬레이션 설정부터 경계조건 수정, 난류 모델 조정, 코드 번역까지 다양한 작업을 자동화한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Computational_Fluid_Dynamics"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Pandey et al._2025_OpenFOAMGPT A retrieval-augmented large language model (LLM) agent for OpenFOAM-based computational.pdf"
---

# OpenFOAMGPT: A retrieval-augmented large language model (LLM) agent for OpenFOAM-based computational fluid dynamics

> **저자**: Sandeep Pandey, Ran Xu, Wenkang Wang, Xu Chu | **날짜**: 2025 | **DOI**: [10.1063/5.0257555](https://doi.org/10.1063/5.0257555)

---

## Essence

본 논문은 OpenFOAM 기반 전산유체역학(CFD) 시뮬레이션을 위해 검색 증강 생성(RAG) 기술로 강화된 대규모 언어모델(LLM) 기반 에이전트 OpenFOAMGPT를 제시한다. GPT-4o와 o1 preview 모델을 활용하여 영점 샷(zero-shot) 시뮬레이션 설정부터 경계조건 수정, 난류 모델 조정, 코드 번역까지 다양한 작업을 자동화한다.

## Motivation

- **Known**: 
  - LLM은 자연언어 이해, 자동화된 추론, 의사결정 분야에서 강력한 도구로 부상
  - 유체역학에서 방정식 발견(equation discovery), 형상 최적화, CFD 워크플로우 자동화 등에 활용되고 있음
  - 기존 연구(Chen et al.)는 LLM 기반 다중 에이전트 시스템으로 CFD 자동화를 제안

- **Gap**: 
  - 일반적인 LLM의 CFD 도메인별 전문 지식 부족
  - OpenFOAM 특화 에이전트의 신뢰성 있는 성능 검증 미흡
  - 반복적 오류 수정 루프와 인간 감시의 필요성에 대한 실증적 분석 부재

- **Why**: 
  - CFD 시뮬레이션의 기술적 진입장벽 감소
  - 전문가 부재 시에도 고품질 시뮬레이션 수행 가능성
  - 다양한 공학 분야(에너지, 항공우주)로의 확장 가능성

- **Approach**: 
  - RAG 파이프라인으로 OpenFOAM 튜토리얼 케이스 기반 도메인 지식 임베딩
  - 다층 에이전트 구조(Builder-Executor-OpenFOAM Agent) 설계
  - 에러 감지 및 반복 수정 루프 구현
  - GPT-4o와 o1 모델 성능 비교 분석

## Achievement

![Figure 1: OpenFOAMGPT 에이전트 구조](figures/fig1.webp)
*다층 구조의 에이전트 설계: 시스템 프롬프트 + 사용자 쿼리 → Builder (RAG 상담) → Executor (워크플로우 조율) → OpenFOAM Agent (실행)*

1. **다양한 시나리오에서 성공적 작동**:
   - 단일상 및 다중상 유동, 층류 및 난류, RANS/LES 등 6가지 OpenFOAM 튜토리얼 케이스 성공
   - Cavity flow, PitzDaily (k-ε 난류), Hotroom (자연대류), Dambreak (VOF), Particle column (MPPIC) 포함

2. **반복 수정 루프를 통한 수렴**:
   - 오류 감지 시 에러 로그를 쿼리에 추가하여 자동 재시도
   - 제한된 반복 횟수로 낮은 토큰 비용에서 수렴

3. **모델 성능 비교**:
   - o1 모델: 토큰 비용 6배 높음(입력 $15/M vs $2.5/M, 출력 $60/M vs $10/M)
   - o1의 연쇄적 사고(Chain-of-Thought) 메커니즘으로 복잡한 작업에서 우수한 성능

4. **도메인 특화 가능성**:
   - RAG 데이터베이스 확장으로 에너지, 항공우주 등 부분 영역 특화 가능
   - 1536차원 벡터로 임베딩된 OpenFOAM 튜토리얼 라이브러리 활용

## How

![Figure 2: RAG 구조](figures/fig2.webp)
*사용자 질문 → 엔진이 프롬프트 생성 → 검색 라이브러리에서 관련 텍스트 검색 → LLM 응답 생성*

- **에이전트 아키텍처**:
  - 최상층: 시스템 프롬프트 + 사용자 쿼리 조합
  - Builder: RAG 데이터베이스 참조하여 구조화된 계획 생성
  - Executor: LLM으로의 쿼리 전달 또는 OpenFOAM 에이전트로 태스크 위임
  - OpenFOAM Agent 내부: Interpreter-Builder-Runner의 3중 협력

- **RAG 파이프라인**:
  - OpenFOAM 튜토리얼 케이스 설명을 OpenAI의 text-embedding-3-small 모델로 1536차원 벡터화
  - 검증된 모범 사례(best practices)와 최신 방법론 제공
  - LangChain 프레임워크로 구현

- **오류 처리**:
  - 시뮬레이션 중 에러 로그 모니터링
  - 실패 감지 시 에러 데이터를 사용자 쿼리에 추가하여 반복 처리
  - 성공 시 워크플로우 종료

- **모델 선택**:
  - GPT-4o: 일반적인 작업에 비용 효율적
  - o1 preview: 복잡한 추론이 필요한 작업에 우수

## Originality

- **OpenFOAM 특화 LLM 에이전트의 최초 구현**: 기존 일반 CFD 에이전트(Chen et al.)를 OpenFOAM에 특화시킨 구체적 실현
- **RAG 기반 도메인 지식 통합**: OpenFOAM 튜토리얼 라이브러리를 벡터 데이터베이스로 체계화
- **다층 에이전트 구조 설계**: Builder-Executor-OpenFOAM Agent의 명확한 역할 분담으로 확장 가능한 아키텍처
- **반복 오류 수정 루프의 실증적 검증**: 자동 오류 감지 및 재시도 메커니즘의 구체적 구현
- **GPT-4o vs o1 모델의 실증적 비교**: 토큰 비용 대비 성능 트레이드오프 분석

## Limitation & Further Study

- **인간 감시의 필수성**: 정확성 보장과 문맥 변화 적응을 위해 인간 개입 필요하며, 이는 완전 자동화 달성이 어려움을 시사
- **시간에 따른 성능 변동**: 모델 성능의 시간적 변동이 관찰되어 미션 크리티컬 애플리케이션에서 모니터링 필요
- **제한된 평가 사례**: 논문에서 제시된 6가지 테스트 케이스의 상세한 성공/실패 결과 분석 부재
- **토큰 비용 증가 부담**: o1 모델의 6배 높은 비용이 실제 산업 적용의 경제성 문제
- **폐쇄형 모델 의존성**: OpenAI API 의존으로 인한 비용, 데이터 프라이버시, 지속가능성 우려

**후속 연구**:
  - 오픈소스 LLM(예: Llama, Qwen)을 활용한 자체 호스팅 가능성 탐색
  - 더 광범위한 CFD 시나리오(3D, 비정상 유동, 복잡 기하학)에 대한 성능 평가
  - 미션 크리티컬 애플리케이션을 위한 인간-AI 협업 프레임워크 개발
  - ANSYS Fluent, COMSOL 등 다른 CFD 소프트웨어로의 프레임워크 확장

## Evaluation

- **Novelty**: 4/5
  - OpenFOAM 특화 RAG-LLM 에이전트의 첫 구현이나, 기술적 개별 요소(RAG, LLM 에이전트)는 기존 개념의 응용

- **Technical Soundness**: 3.5/5
  - 아키텍처 설계와 RAG 파이프라인은 타당하나, 테스트 케이스 선택, 성공 기준 정의, 정량적 성능 메트릭이 부족
  - 6가지 케이스에 대한 상세한 성공/실패 사례 분석 미제시

- **Significance**: 4/5
  - CFD 시뮬레이션의 기술 진입장벽 감소에 의미 있는 기여
  - 다양한 공학 분야 적용 가능성 높음
  - 다만 인간 감시 필수 요구는 실용성을 제한

- **Clarity**: 3.5/5
  - 전반적 구조와 방법론은 명확하나, 에이전트 상세 동작 흐름, 프롬프트 예시, 구체적 오류 처리 사례 부재
  - 평가 섹션(III)이 불완전하게 제시됨(본문 15000자 범위 제약)

- **Overall**: 3.8/5

**총평**: 본 논문은 LLM 기반 CFD 자동화의 실용적 시도로서 가치 있으나, 평가의 완전성과 정량적 성능 검증이 개선되어야 하며, 인간 감시의 필수 요구와 높은 운영 비용은 산업 적용의 주요 과제로 남아 있다.

## Related Papers

- 🔄 다른 접근: [[papers/864_VASPilot_MCP-Facilitated_Multi-Agent_Intelligence_for_Autono/review]] — CFD 시뮬레이션 자동화와 유사하게 DFT 계산을 자동화하는 다중 에이전트 접근법을 제시한다.
- 🔗 후속 연구: [[papers/456_Lang-PINN_From_Language_to_Physics-Informed_Neural_Networks/review]] — 물리 기반 신경망으로 확장하여 자연어에서 실행 가능한 과학 코드 생성의 범위를 넓힌다.
- 🧪 응용 사례: [[papers/130_Automating_Computational_Chemistry_Workflows_via_OpenClaw_an/review]] — 계산 화학 워크플로우 자동화의 구체적 구현으로 OpenClaw와 유사한 자동화 접근법을 보여준다.
- 🔗 후속 연구: [[papers/587_OpenFOAM_The_Open_Source_Computational_Fluid_Dynamics_Toolbo/review]] — 기본적인 CFD 도구 활용을 완전 자동화된 시뮬레이션 시스템으로 발전시킨 기술적 진보를 보여준다.
- 🔄 다른 접근: [[papers/864_VASPilot_MCP-Facilitated_Multi-Agent_Intelligence_for_Autono/review]] — OpenFOAM CFD 자동화와 유사하게 VASP DFT 계산을 자동화하는 다중 에이전트 시스템을 제시한다.
- 🔄 다른 접근: [[papers/456_Lang-PINN_From_Language_to_Physics-Informed_Neural_Networks/review]] — 자연어 기반 과학 코드 생성에서 CFD 시뮬레이션과 물리 신경망이라는 다른 도메인을 다룬다.
