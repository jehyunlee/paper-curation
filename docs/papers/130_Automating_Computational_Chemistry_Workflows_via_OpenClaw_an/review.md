---
title: "130_Automating_Computational_Chemistry_Workflows_via_OpenClaw_an"
authors:
  - "Mingwei Ding"
  - "Chen Huang"
  - "Yibo Hu"
  - "Yifan Li"
  - "Zitian Lu"
date: "2026.03"
doi: "논문"
arxiv: ""
score: 0
essence: "본 논문은 **OpenClaw를 기반으로 한 분리된(decoupled) 에이전트-스킬(agent-skill) 설계**를 통해 다단계 계산화학 작업의 자동화를 달성한다. 일반 목적의 대언어모델 기반 에이전트가 추론과 조정을 담당하고, 재사용 가능한 도메인 스킬이 구체적인 화학 계산 절차를 캡슐화하여 확장성과 유지보수성이 높은 시스템을 실현했다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Code_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ding et al._2026_Automating Computational Chemistry Workflows via OpenClaw and Domain-Specific Skills.pdf"
---

# Automating Computational Chemistry Workflows via OpenClaw and Domain-Specific Skills

> **저자**: Mingwei Ding, Chen Huang, Yibo Hu, Yifan Li, Zitian Lu, Xingtai Yu, Duo Zhang, Wenxi Zhai, Tong Zhu, Qiangqiang Gu, Jinzhe Zeng | **날짜**: 2026-03-26 | **DOI**: [논문 제출 중](https://doi.org/)

---

## Essence

본 논문은 **OpenClaw를 기반으로 한 분리된(decoupled) 에이전트-스킬(agent-skill) 설계**를 통해 다단계 계산화학 작업의 자동화를 달성한다. 일반 목적의 대언어모델 기반 에이전트가 추론과 조정을 담당하고, 재사용 가능한 도메인 스킬이 구체적인 화학 계산 절차를 캡슐화하여 확장성과 유지보수성이 높은 시스템을 실현했다.

## Motivation

- **Known**: 기존 계산화학 자동화는 두 가지 극단적 접근법에 의존한다. (1) AiiDA, FireWorks 등의 워크플로우 시스템: 명시적 실행 구조와 강력한 스케줄러 통합은 제공하지만, 사전 정의된 제어 흐름과 제한된 복구 의미론(recovery semantics)에 의존. (2) ChemCrow, CACTUS 등의 LLM 기반 에이전트: 동적 추론과 도구 선택은 가능하나, 워크플로우 구조와 복구 로직이 전문화된 에이전트 스택에 깊게 내장됨.

- **Gap**: 현재 시스템들은 **엔지니어링 얽힘(engineering entanglement)** 문제를 겪는다. 추론, 워크플로우 명세, 도메인 실행, 인프라 적응이 긴밀하게 결합되어 있어서, 새로운 기능 추가를 위해서는 에이전트 자체를 재설계해야 한다. 또한 이질적 HPC 환경, 자주 변경되는 소프트웨어 패키지, 다양한 파일 형식 등을 처리해야 하는 계산화학의 특수성이 충분히 반영되지 않음.

- **Why**: 다단계, 데이터 집약적인 계산화학 작업은 단순히 개별 계산을 자동화하는 것을 넘어, 작업 명세, 소프트웨어 호출, 중간 데이터 전달, HPC 실행 전반에 걸쳐 **강건하고 감사 가능한 종단간(end-to-end) 자동화**를 요구한다.

- **Approach**: 일반 목적 에이전트(OpenClaw)와 재사용 가능한 스킬의 명확한 분리를 통해, 새로운 도메인 기능은 에이전트를 재설계하지 않고도 스킬 수준에서 추가·교체·재사용 가능하도록 설계.

## Achievement

![Figure 1: OpenClaw 기반 분리된 에이전트-스킬 프레임워크의 아키텍처](figures/fig1.webp) 
*OpenClaw는 중앙 제어와 감독을 제공하고, 스키마 정의 계획 스킬이 과학적 목표를 실행 가능한 작업 명세로 변환하며, 도메인 스킬이 계산화학 절차를 캡슐화하고, DPDispatcher가 이질적 HPC 환경에서 작업 실행을 관리한다.*

1. **메탄 산화 분자동역학(MD) 사례 연구 성공**: 자연 언어 명령으로부터 시작하여 분자 최적화, 파일 형식 변환, 반응 시스템 구성, MD 시뮬레이션, HPC 디스패치 및 모니터링, 실패 복구, 궤적 분석까지 **완전한 크로스-툴 실행(cross-tool execution)** 완성.

2. **확장 가능한 스킬 라이브러리 공개**: 양자화학, 분자동역학, 기계학습 포텐셜, 분자 표현 등을 아우르는 **오픈소스 계산화학 스킬 라이브러리** 제공으로 재현성과 확장성 향상.

3. **계획된 복구(Bounded Recovery)**: 런타임 실패로부터의 자동 복구 메커니즘을 구현하여, 사전에 정의되지 않은 실패 상황에도 대응.

4. **반응 네트워크 추출(Reaction Network Extraction)**: MD 시뮬레이션 결과로부터 자동으로 화학 반응 네트워크를 추출하는 후처리 분석 능력 입증.

## How

![Figure 2: (a) LLM 기반 의사결정 프로세스 개요; (b) 워크플로우](figures/fig1.webp)

- **OpenClaw 제어 루프**: 사용자 요청, 도구 접근, 장기 작업 상태 추적을 포함한 세션 컨텍스트 유지. 각 스텝에서 현재 대화 상태와 이전 행동 출력을 읽고, 언어모델이 다음 행동(스킬 로딩, 도구 호출, 도메인 스크립트 실행 등)을 생성. 출력, 오류, 생성된 파일을 캡처하여 다음 턴의 컨텍스트에 추가.

- **스키마 정의 계획 스킬(Schema-Defined Planning Skills)**: 과학적 목표(예: "메탄 산화 경로 탐색")를 실행 가능한 작업 명세(task manifest)로 변환. 어떤 스킬을 어떤 순서로, 어떤 조건에서 조합할지를 명시.

- **도메인 스킬(Domain Skills)**: 구체적인 계산화학 절차를 캡슐화. 각 스킬은 (1) 능력 설명, (2) 사용 방법, (3) 실행 로직으로 구성. uv 도구체인을 기반으로 **격리된 배포(isolated deployment)** 지원하여 의존성 충돌 최소화.

- **uv 도구체인 활용**: uvx로 임시 격리 환경에서 도구 호출. 각 스킬이 필요 패키지와 함께 실행 가능한 명령으로 표현되어, 런타임에 의존성 해결 가능하면서도 스킬 수준에서 모듈식 유지.

- **DPDispatcher 통합**: HPC 스케줄러 인식형(scheduler-aware) 실행 인터페이스로 이질적 HPC 환경(로컬, 슬럼, PBS 등)에 걸친 작업 제출, 모니터링, 복구를 일관된 방식으로 처리.

- **전명 제어 루프 오케스트레이션**: 고수준 계획, HPC 제출, 계산화학 연산이 모두 OpenClaw의 중앙 루프에서 조율되므로, 스킬은 능력 설명과 절차만 제공하고 자율적으로 동작하지 않음.

![Figure 3: 메탄 산화 MD 시뮬레이션 워크플로우](figures/fig1.webp)

## Originality

- **아키텍처 혁신**: 기존의 워크플로우-중심 시스템(고정 제어 흐름)과 전문화된 에이전트 시스템(깊게 내장된 도메인 로직) 사이의 **거짓 이분법을 극복**. 일반 목적 에이전트와 재사용 가능한 스킬의 명확한 계층 분리를 통해, 도메인 전문성을 에이전트 재설계 없이도 추가·교체 가능하도록 구조화.

- **계산화학 특화 설계**: uv 기반 격리 환경, DPDispatcher와의 통합, 계산화학 데이터 형식 및 소프트웨어 에코시스템의 특수성을 명시적으로 반영하여, 단순 일반 에이전트보다 도메인에 적합한 자동화 실현.

- **공개 스킬 라이브러리**: 양자화학, MD, 기계학습 포텐셜 등 다양한 계산화학 도메인을 아우르는 **재사용 가능하고 개선 가능한 스킬 모음** 제공으로 커뮤니티 기여.

- **실패 복구 의미론(Recovery Semantics)**: 사전 정의되지 않은 런타임 실패로부터의 **계획된 자동 복구** 메커니즘을 LLM의 추론 능력과 결합하여, 워크플로우 시스템의 경직성을 완화.

## Limitation & Further Study

- **LLM 추론의 불안정성**: 논문에서는 메탄 산화 사례 연구 하나만 제시했으므로, 더 복잡한 다단계 작업이나 예상치 못한 실패 모드에서의 일반화 가능성이 미지수. LLM의 추론 오류나 할루시네이션(hallucination)이 복잡한 워크플로우에서 어떻게 누적되는지 미분석.

- **스케일과 성능 평가 부재**: 대규모 매개변수 스윕(parameter sweeps), 고처리량(high-throughput) 시나리오에서의 성능, 스킬 오버헤드(로딩, 실행 시간 증가)에 대한 정량적 평가 부족. uv 캐싱의 실제 성능 이득 측정 미흡.

- **스킬 설계의 유연성 한계**: 스킬이 능력 설명과 절차로만 구성된다는 점에서, 매우 이질적이거나 예측 불가능한 도메인 절차(예: 고급 적응형 샘플링)를 어떻게 스킬로 표현하고 조율할지 명확하지 않음.

- **검증 및 테스트 프레임워크**: 자동화된 워크플로우의 정확성, 재현성, 감시 가능성을 보장하기 위한 **체계적인 검증 프레임워크**의 부재. 중간 데이터 손상이나 매개변수 오류가 긴 파이프라인에서 어떻게 탐지되고 보고되는지 불명확.

- **사용자 상호작용**: 자동화는 완전한지, 아니면 사용자가 개입해야 하는 지점이 있는지 명시되지 않음. LLM의 추론이 틀렸을 때 사용자가 개입하는 메커니즘과 비용이 논의되지 않음.

- **후속 연구 방향**:
  - 다양한 계산화학 도메인(결정 구조 예측, 반응 경로 탐색, 기계학습 포텐셜 훈련 등)에서의 적용 범위 확대
  - 더 정교한 LLM 프롬프트 설계와 in-context learning 최적화
  - 워크플로우 정확성과 수렴성(convergence)을 보장하는 형식 검증(formal verification) 방법 개발
  - 사용자 반환(user feedback) 루프와 대화형 디버깅 기능 강화

## Evaluation

- **Novelty (독창성)**: 4/5
  - 에이전트-스킬 분리 설계는 참신하고 실용적이나, 개별 요소(LLM 에이전트, 워크플로우 자동화, HPC 스케줄링)들 자체는 기존 아이디어. 아이디어의 조합과 통합이 주요 기여.

- **Technical Soundness (기술적 건전성)**: 3.5/5
  - 아키텍처 설계와 사용된 기술(uv, OpenClaw, DPDispatcher)은 견고하나, 메탄 산화 사례 연구 하나에만 국한되어 광범위한 검증 부족. LLM 추론 오류 처리, 스킬 실패 시나리오, 복잡한 의존성 관리에 대한 심층 분석 미흡.

- **Significance (중요성)**: 4/5
  - 계산화학의 자동화는 높은 실용적 가치를 가지며, 본

## Related Papers

- 🔄 다른 접근: [[papers/308_El_Agente_An_Autonomous_Agent_for_Quantum_Chemistry/review]] — 양자화학을 위한 자율 에이전트가 계산화학 워크플로우 자동화의 다른 구현 방식을 제시한다.
- 🔗 후속 연구: [[papers/535_MetaOpenFOAM_an_LLM-based_multi-agent_framework_for_CFD/review]] — CFD를 위한 LLM 기반 다중 에이전트 프레임워크가 계산화학 자동화를 다른 계산 과학 분야로 확장한다.
- 🔄 다른 접근: [[papers/839_Transforming_Behavioral_Neuroscience_Discovery_with_In-Conte/review]] — 계산화학 분야의 도메인 특화 자동화 파이프라인 접근법이 행동신경과학에도 적용 가능하다.
- 🧪 응용 사례: [[papers/589_OpenFOAMGPT_A_retrieval-augmented_large_language_model_LLM_a/review]] — 계산 화학 워크플로우 자동화의 구체적 구현으로 OpenClaw와 유사한 자동화 접근법을 보여준다.
