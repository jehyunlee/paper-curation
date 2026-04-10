---
title: "638_ProtAgents_protein_discovery_via_large_language_model_multi-"
authors:
  - "Alireza Ghafarollahi"
  - "Markus J. Buehler"
date: "2024"
doi: "10.1039/d4dd00013g"
arxiv: ""
score: 4.25
essence: "본 논문은 대규모 언어모델(LLM, Large Language Model) 기반의 다중 에이전트 협업 시스템인 ProtAgents를 제안하여, 물리 기반 시뮬레이션과 머신러닝을 통합함으로써 de novo 단백질 설계 및 분석을 자동화한다. 각 에이전트는 특정 도메인 전문성을 가지고 동적으로 상호작용하면서 복잡한 단백질 설계 문제를 해결한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Protein-Drug_Design_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ghafarollahi and Buehler_2024_ProtAgents protein discovery via large language model multi-agent collaborations combining physics.pdf"
---

# ProtAgents: protein discovery via large language model multi-agent collaborations combining physics and machine learning

> **저자**: Alireza Ghafarollahi, Markus J. Buehler | **날짜**: 2024 | **DOI**: [10.1039/d4dd00013g](https://doi.org/10.1039/d4dd00013g)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: 단백질 발견 및 분석을 위한 다중 에이전트 AI 프레임워크. 각 에이전트는 프로필로 정의된 초점과 맞춤 함수에 접근 가능하며, 그룹 채팅 관리자를 통해 동적으로 협력한다.*

본 논문은 대규모 언어모델(LLM, Large Language Model) 기반의 다중 에이전트 협업 시스템인 ProtAgents를 제안하여, 물리 기반 시뮬레이션과 머신러닝을 통합함으로써 de novo 단백질 설계 및 분석을 자동화한다. 각 에이전트는 특정 도메인 전문성을 가지고 동적으로 상호작용하면서 복잡한 단백질 설계 문제를 해결한다.

## Motivation

- **Known**: 기존 AI 기반 단백질 설계 방법들(AlphaFold, 딥러닝 모델 등)은 구조 예측이나 특정 물성 예측에 뛰어나지만, 이들은 단일 목적 또는 특정 물성에만 집중되어 있으며 도메인 간 지식 통합과 포괄적 데이터 분석 능력이 제한적이다.

- **Gap**: 다양한 도구, 지식, 능력을 통합하면서 물리 기반 모델링과 데이터 기반 도구를 결합하며, 문헌 정보 검색과 반복적 문제 해결을 동시에 수행할 수 있는 지능형 플랫폼이 부재한다.

- **Why**: 단백질 설계 공간이 매우 크고(100개 아미노산 단백질의 경우 20^100 개의 가능한 서열), 실험적 검증 비용이 높으므로, 지능형 자동화 시스템을 통해 설계 공간을 효율적으로 탐색하고 여러 목표를 동시에 달성할 필요가 있다.

- **Approach**: LLM의 뛰어난 추론, 계획 수립 능력을 핵심으로 하는 다중 에이전트 시스템을 구축하여, 물리 시뮬레이터, 생성형 AI 모델, 미세 조정된 변환기(transformer) 모델, 지식 검색 에이전트 등 다양한 도구들이 자율적으로 협력하도록 설계한다.

## Achievement

![Figure 2](figures/fig2.webp)
*Figure 2: 다중 에이전트 팀 멤버들 간의 동적 상호작용 흐름도. 그룹 채팅 관리자가 현재 문맥에 따라 협력할 에이전트를 선택하여 상호 수정과 역할 분담을 가능하게 한다.*

1. **다중 에이전트 아키텍처 개발**: 사용자 프록시(user_proxy), 계획자(planner), 실행 담당자(assistant), 평가자(critic) 등 서로 다른 전문성을 가진 4가지 주요 에이전트로 구성된 협력 시스템을 구현하였으며, 그룹 채팅 관리자(group chat manager)가 동적으로 협력 구조를 조정한다.

![Figure 3](figures/fig3.webp)
*Figure 3: 복잡한 단백질 설계 작업(실험 II)을 해결하기 위한 다중 에이전트 협력 개요. Chroma를 이용한 de novo 단백질 서열 생성, OmegaFold를 통한 3D 구조 예측, 고유 진동수 및 이차 구조 분석을 순차적으로 수행한다.*

2. **통합 도구 생태계**: 물리 PDE 시뮬레이터(고유 진동수 계산), 확산 모델 기반 생성형 AI(Chroma), 미세 조정 변환기(단백질 기계적 물성 예측), 문헌 기반 지식 검색 등을 하나의 시스템에 통합하여 de novo 단백질 설계와 동시에 물성 예측 및 검증이 가능하도록 함.

3. **자동화된 반복적 문제 해결**: 단순 질문에서 출발하여 에이전트들이 자동으로 서브 태스크로 분해하고, 각 도구를 순차적으로 적용하며, 결과를 상호 검증하는 과정을 인간 개입 없이 수행 가능하게 함.

## How

![Figure 4](figures/fig4.webp)
*Figure 4: 복잡한 단백질 설계 작업(실험 III)을 해결하기 위한 다중 에이전트 협력 개요.*

- **LLM 기반 에이전트 설계**: 각 에이전트는 프로필(profile)에 의해 정의된 역할과 관련 맞춤 함수(customized functions)에 접근 가능하며, 자연어를 통해 상호 통신하고 협력한다.

- **동적 역할 분담**: 그룹 채팅 관리자가 현재 대화의 문맥을 파악하여 필요한 에이전트를 선택적으로 활성화하고, 에이전트 간 상호 수정(mutual correction)을 촉진한다.

- **도구 통합 전략**: 
  - 물리 시뮬레이터: PDE 기반 고유 진동수 계산
  - 생성형 AI (Chroma): 조건부/무조건 de novo 단백질 서열 생성
  - 구조 예측 (OmegaFold): 아미노산 서열로부터 3D 폴딩 구조 예측
  - 미세 조정 변환기: 단백질 서열로부터 기계적 물성(예: 탄성) 예측
  - 지식 검색: 과학 문헌 데이터베이스로부터 정보 조회

- **반복적 최적화 루프**: 에이전트들이 목표 물성을 달성할 때까지 서열 생성→구조 예측→물성 계산→평가→재설계 사이클을 자동으로 반복 수행한다.

## Originality

- **LLM 기반 다중 에이전트 프레임워크의 단백질 설계 응용**: 기존 LLM 연구가 주로 텍스트 처리나 코드 생성에 집중한 반면, 본 논문은 LLM의 추론/계획 능력을 핵심으로 하여 물리-데이터 기반 도구들을 자율적으로 통합하는 새로운 패러다임을 제시한다.

- **물리와 머신러닝의 진정한 융합**: 기존 surrogate 모델들이 구조-물성 관계를 일방향으로 모델링한 반면, ProtAgents는 생성형 AI, 물리 시뮬레이션, 머신러닝 예측을 동적으로 조합하여 다중 목표 최적화를 가능하게 한다.

- **도메인 간 지식 통합 능력**: 단백질 설계, 구조 예측, 물성 계산, 과학 문헌 검색 등 서로 다른 분야의 도구와 지식을 하나의 프레임워크 내에서 통합하여 종합적 문제 해결을 자동화한다.

- **적응적 에이전트 협력**: 고정된 워크플로우가 아닌 동적 그룹 채팅을 통해 에이전트들이 상황에 맞게 협력 구조를 자동 조정하므로, 다양한 유형의 단백질 설계 문제에 유연하게 대응 가능하다.

## Limitation & Further Study

- **LLM의 물리적 근거 제한**: LLM은 우수한 추론 능력을 제공하지만 물리 법칙을 엄밀히 준수하지 못할 수 있으므로, 물리 시뮬레이터와의 통합 단계에서 결과 검증 메커니즘이 더욱 강화되어야 한다.

- **확장성 및 계산 비용**: 대규모 단백질 탐색에서 다중 에이전트 협력으로 인한 LLM API 호출 증가가 계산 비용을 증가시킬 수 있으며, 에이전트 체인 길이가 길어질 경우 오류 누적 위험이 존재한다.

- **생성 모델의 제약**: Chroma 등 생성형 AI가 자연 단백질의 진화적 특성을 완전히 학습하지 못해 현실적으로 실현 불가능한 서열을 생성할 수 있으며, 이를 필터링하는 메커니즘의 고도화가 필요하다.

- **후속 연구 방향**:
  - 다른 단백질 특성(접힘 안정성, 활성 부위 설계 등)으로의 확장
  - 실제 실험적 검증과의 통합
  - 에이전트 간 협력 효율성 최적화
  - 더 경량의 LLM 모델 또는 도메인 특화 모델 활용으로 계산 비용 절감
  - 멀티 모달(multimodal) 에이전트 개발


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.25/5

**총평**: 본 논문은 LLM 기반 다중 에이전트 시스템을 단백질 설계에 창의적으로 응용하여, 물리 기반 도구와 머신러닝을 동적으로 통합하는 새로운 패러다임을 제시한다. 자동화된 협력 메커니즘과 다양한 도메인 지식의 통합이 강점이나, LLM의 물리적 근거 부족과 계산 효율성 개선이 향후 과제로 남아 있다. 재료 설계와 AI의 융합 연구에 중요한 기여를 할 수 있는 잠재력 있는 작업이다.

## Related Papers

- 🔄 다른 접근: [[papers/292_Drugpilot_Llm-based_parameterized_reasoning_agent_for_drug_d/review]] — 단백질 vs 약물 발견에서 LLM 기반 다중 에이전트 시스템의 다른 적용 분야를 비교할 수 있다
- 🏛 기반 연구: [[papers/115_Augmenting_large_language_models_with_chemistry_tools/review]] — LLM에 전문 도구를 통합하는 방법론이 단백질 설계 다중 에이전트 시스템의 기반을 제공한다
- 🔗 후속 연구: [[papers/144_AutoProteinEngine_A_Large_Language_Model_Driven_Agent_Framew/review]] — LLM 기반 단백질 엔진 프레임워크를 다중 에이전트 협업으로 확장한 연구다
- 🔄 다른 접근: [[papers/065_Agentic_End-to-End_De_Novo_Protein_Design_for_Tailored_Dynam/review]] — 단백질 설계에서 다중 에이전트 vs 엔드투엔드 단일 시스템의 다른 접근법을 비교할 수 있다
- 🏛 기반 연구: [[papers/256_De_novo_design_of_protein_structure_and_function_with_RFdiff/review]] — LLM 다중 에이전트를 활용한 단백질 발견이 동적 특성 기반 설계의 기반 기술을 제공한다
- 🔄 다른 접근: [[papers/065_Agentic_End-to-End_De_Novo_Protein_Design_for_Tailored_Dynam/review]] — 동일한 단백질 발견 문제를 다중 에이전트 접근법으로 해결하여 상호 보완적인 방법론을 제시합니다.
- 🔗 후속 연구: [[papers/686_Robust_deep_learning_based_protein_sequence_design_using_Pro/review]] — 단백질 설계를 LLM 기반 다중 에이전트 시스템으로 확장한다.
- 🔄 다른 접근: [[papers/115_Augmenting_large_language_models_with_chemistry_tools/review]] — 화학 vs 단백질 분야에서 LLM 기반 전문 도구 통합의 다른 적용을 비교할 수 있다
- 🔄 다른 접근: [[papers/292_Drugpilot_Llm-based_parameterized_reasoning_agent_for_drug_d/review]] — 신약 vs 단백질 발견에서 LLM 기반 다중 에이전트 시스템의 다른 적용 분야를 비교할 수 있다
- 🔄 다른 접근: [[papers/480_Large-Language-Model-Based_AI_Agent_for_Organic_Semiconducto/review]] — 유기 반도체 vs 단백질 분야에서 LLM 기반 소자 개발의 다른 적용을 비교할 수 있다
- 🔗 후속 연구: [[papers/160_BioAgents_Democratizing_Bioinformatics_Analysis_with_Multi-A/review]] — BioAgents의 생물정보학 분석 접근법을 단백질 발견 영역으로 확장하여 더 전문화된 다중 에이전트 시스템을 구축할 수 있다.
- 🔗 후속 연구: [[papers/144_AutoProteinEngine_A_Large_Language_Model_Driven_Agent_Framew/review]] — ProtAgents의 다중 에이전트 기반 단백질 발견이 AutoProteinEngine의 단일 에이전트 AutoML 접근을 협업적 시스템으로 확장한 발전 형태이다.
