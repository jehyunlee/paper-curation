---
title: "490_LIDDIA_Language-based_Intelligent_Drug_Discovery_Agent"
authors:
  - "Reza Averly"
  - "Frazier N. Baker"
  - "Xia Ning"
date: "2025"
doi: "10.48550/arXiv.2502.13959"
arxiv: ""
score: 4.2
essence: "본 논문은 대규모 언어 모델(LLM)의 추론 능력을 활용하여 전임상 신약개발 과정을 자동화하는 지능형 에이전트 LIDDIA를 제시한다. LIDDIA는 계산 도구들을 결합하여 분자 생성, 최적화, 선별을 통해 주요 약학적 기준을 만족하는 신규 치료약물 후보를 식별할 수 있다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Drug_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Averly et al._2025_LIDDIA Language-based Intelligent Drug Discovery Agent.pdf"
---

# LIDDIA: Language-based Intelligent Drug Discovery Agent

> **저자**: Reza Averly, Frazier N. Baker, Xia Ning | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2502.13959](https://doi.org/10.48550/arXiv.2502.13959)

---

## Essence

![Figure 1](figures/fig1.webp) *LIDDIA 프레임워크의 개요: 사용자 프롬프트(AR/NR3C4 타겟팅 분자)에서 시작하여 REASONER, EXECUTOR, EVALUATOR, MEMORY 네 가지 연결된 컴포넌트를 통해 약물 후보군을 생성하는 과정*

본 논문은 대규모 언어 모델(LLM)의 추론 능력을 활용하여 전임상 신약개발 과정을 자동화하는 지능형 에이전트 LIDDIA를 제시한다. LIDDIA는 계산 도구들을 결합하여 분자 생성, 최적화, 선별을 통해 주요 약학적 기준을 만족하는 신규 치료약물 후보를 식별할 수 있다.

## Motivation

- **Known**: 최근 AI 발전으로 개별 신약개발 작업(분자 생성, 성질 예측 등)의 자동화가 진행되고 있음. 또한 LLM이 과학 발견의 추론 엔진으로 활용되는 사례가 증가 중.

- **Gap**: 기존 LLM 기반 에이전트들(CHEMCROW, CACTUS, DRUGAGENT 등)은 신약개발의 복잡한 전체 과정을 통합적으로 네비게이션하지 못하며, 특히 구조 기반 신약개발(SBDD)을 위한 확립된 계산 도구를 활용하지 않음.

- **Why**: 신약개발은 장기간 소요되는 복잡한 과정으로, 다양한 약학적 요구사항 간의 균형을 취해야 함. 의약화학자의 전문성을 모방하는 자동화 에이전트가 필요.

- **Approach**: LLM의 추론 능력을 약물 발견 계산 도구(도킹, 성질 예측, 분자 생성 최적화)와 통합하여 REASONER, EXECUTOR, EVALUATOR, MEMORY 네 개 컴포넌트로 구성된 모듈식 에이전트 구축.

## Achievement

![Figure 3](figures/fig3.webp) *좌측: 분자 품질 분석 - 여러 약학적 성질(QED, Vina 스코어 등)에서 생성된 분자들의 성능 분포. 우측: 액션 분석 - GENERATE, OPTIMIZE, SCREEN 액션의 호출 패턴*

1. **높은 성공률**: 30개의 임상적으로 관련된 치료 타겟 중 70% 이상에서 핵심 약학적 기준을 충족하는 분자들을 생성 성공.

2. **탐색-활용 균형**: LIDDIA가 화학 공간(chemical space)에서 탐색(exploration)과 활용(exploitation)을 지능적으로 균형을 맞추는 패턴 확인 - 이것이 성공 결과의 핵심 메커니즘.

3. **신규 후보 발굴**: AR/NR3C4(전립선암 및 유방암의 중요한 타겟) 타겟에 대해 약속 있는 신규 약물 후보 1개 식별.

## How

![Figure 4](figures/fig4.webp) *다양한 타겟에 걸친 LIDDIA 액션 궤적: 각 타겟별로 GENERATE, OPTIMIZE, SCREEN 액션이 어떻게 순차적으로 수행되는지 보여주는 궤적 분석*

- **REASONER**: 메모리의 분자 정보와 성질 프로파일을 기반으로 LLM을 활용하여 다음 액션을 계획. GENERATE(새 분자 생성), OPTIMIZE(기존 분자 개선), SCREEN(선별) 세 가지 액션 타입 수행.

- **EXECUTOR**: 각 액션별 최신 계산 도구 통합
  - GENERATE: Pocket2Mol 등 구조 기반 생성 모델로 표적 결합 부위 고려하여 분자 생성
  - OPTIMIZE: 분자 정제 생성 모델로 약물 유사성 및 구조 최적화
  - SCREEN: 복잡한 논리 기반 선별, 분자 조직화 및 관리

- **EVALUATOR**: 표적 결합 친화력, 약물 유사성(QED), 합성 접근성, Lipinski 규칙, 신규성, 다양성 등 다각적 평가. 플러그-앤-플레이 설계로 새 도구 추가 용이.

- **MEMORY**: 사용자 프롬프트(단백질 구조, 요구사항, 참고 분자), 액션 궤적, 생성 분자, 성질 정보 동적 저장 및 업데이트. REASONER의 정보 기반 계획 지원.

## Originality

- **첫 통합 시스템**: 구조 기반 신약개발(SBDD)을 위한 확립된 계산 도구들(도킹 시뮬레이션, 성질 예측)과 LLM 추론을 통합하는 첫 시도. 기존 에이전트들은 LLM의 내재 지식이나 웹 검색에만 의존.

- **생성 AI 기반 전체 파이프라인**: 히트 식별(GENERATE)부터 리드 최적화(OPTIMIZE)까지 생성 모델 활용으로 화학 공간 확장. 기존 약물 라이브러리 검색 방식의 한계 극복.

- **의약화학 워크플로우 모방**: 탐색-활용 균형, 반복적 분자 설계 최적화 등 실제 의약화학자의 의사결정 과정을 구현.

- **모듈식 및 확장 가능 설계**: 각 컴포넌트의 독립적 교체/개선 가능. 새로운 계산 도구 통합 용이.

## Limitation & Further Study

- **계산 도구 의존성**: EXECUTOR의 성능은 Pocket2Mol, 도킹 시뮬레이션 등 기반 도구의 정확성에 제한. 도구의 오류 축적 가능성.

- **LLM 환각(Hallucination) 위험**: REASONER의 화학 지식 제한으로 화학적으로 불가능한 최적화 제안 가능성.

- **대규모 실험 검증 부족**: 30개 타겟에 대한 in silico 평가이며, 실제 실험적 검증 미포함. 신약개발 후기 단계(임상시험) 통합 미실시.

- **탐색-활용 균형의 명시적 제어 메커니즘 부재**: 현재 LLM의 암묵적 의사결정에 의존하며, 명시적 제어 전략 개발 필요.

- **후속 연구 방향**:
  - 실제 화학 실험과의 통합 (셀프드라이빙 랩)
  - 세포/동물 모델 기반 생물학적 검증
  - 독성, 약물동역학 등 후기 개발 특성 예측 통합
  - 다중 타겟 및 조합 치료 시나리오 확장

## Evaluation

| 평가 항목 | 점수 | 근거 |
|---------|------|------|
| **Novelty** | 4.5/5 | SBDD 도구와 LLM 통합은 창신적이나, 개별 컴포넌트는 기존 기술의 조합. 그러나 이러한 통합 자체는 신약개발 분야에서 최초 수준. |
| **Technical Soundness** | 4/5 | 아키텍처 설계와 구성 요소는 타당하나, in silico 평가에만 의존하고 생성 도구의 신뢰성에 대한 상세 분석 부족. LLM 입력 프롬프트 설계에 대한 상세 기술 미제시. |
| **Significance** | 4.5/5 | 신약개발 자동화의 실질적 진전을 보여주며, 산업 및 학계 적용 가능성 높음. 다만 임상 검증 없어 영향도 제한적. |
| **Clarity** | 4/5 | 프레임워크 구조와 전체 파이프라인은 명확하나, 구체적인 프롬프트 엔지니어링, LLM 모델 선택(어떤 LLM 사용?), 초매개변수 설정 등 구현 세부사항이 부족. |
| **Overall** | 4.2/5 | 신약개발 분야의 의미 있는 진전을 제시하는 잘 설계된 시스템으로, 모듈식 아키텍처와 강력한 결과가 강점. 그러나 실험 검증의 제한, 기술 세부사항 부족, 실제 신약개발 프로세스와의 경제성 비교 분석 필요. |

**총평**: LIDDIA는 LLM의 추론 능력과 구조 기반 신약개발 도구를 통합하여 자동화된 신약개발을 향한 의미 있는 첫걸음을 제시한다. 70% 이상의 타겟에서 약학적 기준 충족 달성과 신규 후보 발굴은 고무적이나, in silico 평가에만 의존하고 실제 실험 검증이 부재한 점, 그리고 LLM의 화학적 신뢰성에 대한 심화 분석이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/177_Can_ai_agents_design_and_implement_drug_discovery_pipelines/review]] — 같은 신약개발 자동화를 다루지만 LIDDIA는 전임상 과정 전반을, Deep Thought는 파이프라인 설계에 집중한 차이점을 보임
- 🔗 후속 연구: [[papers/213_ChemReasoner_Heuristic_Search_over_a_Large_Language_Models_K/review]] — LIDDIA의 분자 생성 기능이 ChemReasoner의 화학 추론 능력과 결합하면 더 정교한 신약 후보 발견이 가능함
- 🏛 기반 연구: [[papers/290_DrugAgent_Automating_AI-aided_Drug_Discovery_Programming_thr/review]] — DrugAgent의 AI 기반 프로그래밍 자동화 접근법이 LIDDIA의 계산 도구 통합 방법론의 기반이 됨
- 🔗 후속 연구: [[papers/856_Unimatch_Universal_matching_from_atom_to_task_for_few-shot_d/review]] — 언어 기반 지능형 약물 발견 에이전트가 계층적 매칭을 실제 약물 발견 워크플로우로 확장한다.
- 🔄 다른 접근: [[papers/292_Drugpilot_Llm-based_parameterized_reasoning_agent_for_drug_d/review]] — 신약 발견에서 LLM 기반 에이전트의 다른 설계 접근법과 구현 방식을 비교할 수 있다
- 🔄 다른 접근: [[papers/177_Can_ai_agents_design_and_implement_drug_discovery_pipelines/review]] — 둘 다 AI 기반 신약 발견을 다루지만 Deep Thought는 파이프라인 설계에, LIDDIA는 전체 전임상 과정에 집중함
- 🔄 다른 접근: [[papers/291_Drugclip_Contrastive_drug-disease_interaction_for_drug_repur/review]] — 언어 기반 지능형 약물 발견과 대조학습 재창출의 다른 접근법
