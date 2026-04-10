---
title: "835_Towards_Scientific_Intelligence_A_Survey_of_LLM-based_Scient"
authors:
  - "Shuo Ren"
  - "Can Xie"
  - "Pu Jian"
  - "Zhenjiang Ren"
  - "Chunlin Leng"
date: "2025.03"
doi: "제공되지"
arxiv: ""
score: 4.0
essence: "본 논문은 가설 생성, 실험 설계, 데이터 분석 등 과학적 발견 전 과정을 자동화하는 LLM 기반 과학 에이전트(Scientific Agent)의 아키텍처, 설계, 벤치마크, 응용, 윤리적 고려사항을 포괄적으로 검토한 서베이 논문이다. 일반 목적의 LLM과 달리 도메인 특화 지식, 고급 도구 집합, 강건한 검증 메커니즘을 통합하여 재현성 있는 과학적 발견을 주도한다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Large_Language_Model_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents.pdf"
---

# Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents

> **저자**: Shuo Ren, Can Xie, Pu Jian, Zhenjiang Ren, Chunlin Leng, Jiajun Zhang | **날짜**: 2025-03-31 | **DOI**: [제공되지 않음]

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: LLM 기반 과학 에이전트의 전형적인 아키텍처*

본 논문은 가설 생성, 실험 설계, 데이터 분석 등 과학적 발견 전 과정을 자동화하는 LLM 기반 과학 에이전트(Scientific Agent)의 아키텍처, 설계, 벤치마크, 응용, 윤리적 고려사항을 포괄적으로 검토한 서베이 논문이다. 일반 목적의 LLM과 달리 도메인 특화 지식, 고급 도구 집합, 강건한 검증 메커니즘을 통합하여 재현성 있는 과학적 발견을 주도한다.

## Motivation

- **Known**: 기존 LLM 에이전트 서베이(Wang et al., 2024; Xi et al., 2023 등)는 대화형 어시스턴트, 코딩 지원 등 일반적 응용에 초점을 맞춤
  
- **Gap**: 과학 연구의 증가하는 복잡성(방대한 데이터 관리, 학제 간 협업, 가속화된 발견)에 대응하기 위해서는 과학 특화 에이전트의 체계적 검토 필요. 기존 라이프사이클 기반 또는 역할 기반 분류(Luo et al., 2025; Wang et al., 2025c; Wei et al., 2025)는 아키텍처 설계 원칙을 명확히 하지 못함

- **Why**: 일반 에이전트와 달리 과학 에이전트는 (1) 다양한 데이터 타입 처리(수치 데이터, 분자 구조, 생물 서열), (2) 이질적 액션 공간(API, 시뮬레이터, 실험기기), (3) 도메인 특화 지식 통합, (4) 재현성 보장의 고도화된 요구사항을 가짐

- **Approach**: 메커니즘 중심 분류체계 도입. Planner, Memory, Action Space, Verifier의 4대 아키텍처 핵심 요소와 각 하위 유형들을 체계화하여 과학 에이전트 설계의 "레시피북" 제공

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: Planner 메커니즘의 분류체계 (P1-P6: Prompt-Native, L1-L2: Learned)*

1. **메커니즘 중심 분류체계**: 기존 라이프사이클 기반 분류를 넘어 4대 아키텍처 메커니즘(Planner, Memory, Action Space, Verifier)을 기반으로 한 세분화된 분류체계 제시. Prompt-Native Planner 6개 유형(Instructional/Schema-Driven, Context-Augmented, Deliberative/Reflective, Search-Based, Role-Interactive, Programmatic)과 Learned Planner 2개 유형(SFT/Domain-Trained, RL/Preference-Optimized) 구분

2. **구성 요소별 설계 청사진**: 각 메커니즘의 구체적 구현 방식들을 세분화하고, 캐소드 설계(cathode design) 사례를 통해 엔드-투-엔드 에이전트 구축 방법론을 일관되게 제시

3. **문헌 및 벤치마크 아틀라스**: 120편 이상의 대표 논문과 40개 이상의 도메인 벤치마크를 메커니즘 수준으로 분류하여 연구자들의 빠른 기술 탐색 가능하게 함

4. **윤리성과 재현성의 설계 필수요소화**: 기존의 주변적 고려에서 벗어나 편향 완화(bias mitigation), 재현성 보증을 에이전트 아키텍처와 검증 모듈에 내재화

## How

![Figure 1](figures/fig1.webp)
*그림 1: 전형적 LLM 기반 과학 에이전트의 워크플로우*

**아키텍처 및 메커니즘 설계**:

- **Planner 메커니즘**: 사용자의 과학 문제를 부분 과제(sub-task)로 분해하고, 메모리에서 맥락/지식을 검색, 액션 스페이스를 통해 도구 호출 조율. Prompt 기반 (명시적 템플릿, 맥락 보강, 자기 성찰, 탐색 기반, 역할 상호작용, 프로그래밍 기반)과 학습 기반(도메인 미세조정, 강화학습) 두 가족으로 구분

- **Memory 메커니즘**: 과거 실행 궤적, 검색된 문헌, 도메인 지식 베이스, 검증 결과 등을 저장하여 이후 결정 정제에 활용

- **Action Space**: API 호출, 코드 실행, 시뮬레이터 상호작용, 문헌 검색 등 다양한 외부 도구 및 환경과의 인터페이스

- **Verifier**: 중간 결과의 정확도, 일관성, 과학적 타당성을 검증하고, 추가 액션 또는 수정이 필요한 경우 Planner에 피드백 제공

**반복 프로세스**: 사용자 쿼리 → Planner 분해 → Memory 검색 → Action Space 실행 → Verifier 검증 → 메모리 저장 → (필요시 재계획) → 최종 결과 반환

## Originality

- **메커니즘 중심 패러다임의 도입**: 기존 서베이(역할 기반: Assistant/Partner/Avatar, 라이프사이클 기반)와 달리 아키텍처 설계 원칙 수준에서의 분석으로 새로운 에이전트 설계의 이론적 틀 제공

- **세분화된 Planner 분류**: 단순한 "planning" 범주를 넘어 Prompt-Native 6개, Learned 2개 유형으로 세분화하여 각 기법의 장단점과 적용 시나리오를 명확히 함

- **구성 가능성(composability) 강조**: 각 컴포넌트의 혼합 조합을 통한 "레시피북" 방식으로 도메인 연구자들이 자신의 과제에 맞춘 에이전트를 설계할 수 있는 실용적 가이드 제공

- **윤리성의 아키텍처화**: 재현성, 편향 완화, 투명성을 주변적 고려가 아닌 설계 제약조건으로 내재화

## Limitation & Further Study

**현재 한계**:
- 논문이 제공된 15,000자 본문에서는 Planner와 Architecture 개요만 상세히 다루고, Memory, Action Space, Verifier의 구체적 구현, 벤치마크 평가, 실제 응용 사례는 미제시 상태
- 각 메커니즘의 성능 비교 메트릭, 수렴성(convergence), 계산 비용(computational cost) 분석 부재
- 도메인 간 전이 가능성(transferability) 및 새로운 과학 분야로의 확장성에 대한 실증적 평가 부족

**후속 연구 방향**:
- 학제 간 지식 통합을 위한 온톨로지(ontology) 및 메타러닝(meta-learning) 기법 개발
- 동적 적응(dynamic adaptation) 메커니즘: 에이전트가 새로운 도구, 데이터 형식, 도메인 특성에 실시간으로 적응
- 표준화된 재현성 프로토콜: 과학 커뮤니티 전역에서 통용 가능한 에이전트 평가 및 검증 표준 수립
- 멀티모달 과학 데이터(이미지, 그래프, 시계열)의 통합 처리 고도화
- 사람-기계 협업 인터페이스 개선: 도메인 전문가의 의도 반영과 결과 해석 용이성 강화


## Evaluation

- Novelty: 4/5
- Technical Soundness: 3.5/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 LLM 기반 과학 에이전트에 대한 첫 체계적 메커니즘 중심 분석을 제공하며, 120+ 논문과 40+ 벤치마크를 정리한 포괄적 자원으로서의 가치가 크다. 다만 제공된 본문에서는 아키텍처 개요만 다루어 Memory, Action Space, Verifier, Benchmarks, Applications, Ethics에 대한 실질적 내용이 부족하며, 실증적 성능 비교와 도메인 간 전이 가능성에 대한 정량적 평가가 필요하다. 완성된 서베이로서는 높은 참고 가치를 가질 것으로 예상되나, 현재 제시된 본문만으로는 메커니즘 분류의 명확성과 실용적 설계 가이드라인에 주로 의존한다.

## Related Papers

- 🔗 후속 연구: [[papers/038_A_vision_for_auto_research_with_llm_agents/review]] — Scientific Agent 서베이가 Auto Research 비전을 구체적인 에이전트 아키텍처와 설계 원칙으로 발전시켜 실현 가능한 로드맵을 제시한다.
- 🧪 응용 사례: [[papers/673_Researchtown_Simulator_of_human_research_community/review]] — Scientific Agent의 이론적 프레임워크가 ResearchTown의 멀티에이전트 시뮬레이션에서 실제 구현되어 연구 자동화의 실현 가능성을 검증할 수 있다.
- 🏛 기반 연구: [[papers/820_Toward_Reliable_Scientific_Hypothesis_Generation_Evaluating/review]] — Scientific Agent의 강건한 검증 메커니즘 요구사항이 TruthHypo의 진실성 평가와 환각 탐지 연구의 필요성을 뒷받침한다.
- 🧪 응용 사례: [[papers/286_Domain-specific_ReAct_for_physics-integrated_iterative_model/review]] — Scientific Agent의 도메인 특화 지식 통합 방법론이 물리학 통합 모델링의 ReAct 프레임워크에서 실제 적용 사례로 구현된다.
- 🔄 다른 접근: [[papers/506_LLM4SR_A_Survey_on_Large_Language_Models_for_Scientific_Rese/review]] — LLM 기반 과학 지능에 대한 서로 다른 관점의 서베이를 제시합니다.
- 🔗 후속 연구: [[papers/673_Researchtown_Simulator_of_human_research_community/review]] — ResearchTown의 멀티에이전트 시뮬레이션이 Scientific Agent 서베이에서 제시하는 이론적 프레임워크의 실제 구현 사례로 활용될 수 있다.
- 🧪 응용 사례: [[papers/730_Sciqag_A_framework_for_auto-generated_science_question_answe/review]] — SciQAG의 고품질 QA 데이터가 Scientific Agent의 지식 기반 구축과 추론 능력 향상을 위한 핵심 자원으로 활용될 수 있다.
- 🏛 기반 연구: [[papers/748_Semi-Supervised_2D_Human_Pose_Estimation_Driven_by_Position/review]] — 도메인 특화 과학 추론 사례로서 Scientific Agent 설계에서 특정 영역 전문성 통합 방법론의 실제 구현 예시를 제공한다.
- 🏛 기반 연구: [[papers/820_Toward_Reliable_Scientific_Hypothesis_Generation_Evaluating/review]] — TruthHypo의 환각 탐지와 진실성 평가가 Scientific Agent의 신뢰성 있는 과학적 발견을 위한 핵심적인 검증 메커니즘을 제공한다.
- 🧪 응용 사례: [[papers/286_Domain-specific_ReAct_for_physics-integrated_iterative_model/review]] — 에너지 공학의 도메인 특화 ReAct 프레임워크가 Scientific Agent 서베이에서 제시하는 도메인 전문성 통합 방법론의 실제 구현 사례이다.
- 🏛 기반 연구: [[papers/038_A_vision_for_auto_research_with_llm_agents/review]] — Auto Research 비전이 Scientific Agent 서베이에서 체계화되어 구체적인 아키텍처와 구현 방법론으로 발전한다.
