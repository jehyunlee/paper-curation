---
title: "292_Drugpilot_Llm-based_parameterized_reasoning_agent_for_drug_d"
authors:
  - "Kun Li"
  - "Zhennan Wu"
  - "Shoupeng Wang"
  - "Jia Wu"
  - "Shirui Pan"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "본 논문은 신약 개발의 전 단계를 지원하는 대형 언어모델(LLM) 기반 에이전트 시스템 DrugPilot을 제시한다. 매개변수화된 메모리 풀(Parameterized Memory Pool, PMP)을 통해 이질적인 약물 데이터를 표준화된 표현으로 변환하고, 피드백-포커스(Fe-Fo) 메커니즘으로 LLM의 추론 오류를 실시간 모니터링하여 정확한 도구 호출과 멀티턴 대화를 가능하게 한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Drug_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Li et al._2025_Drugpilot Llm-based parameterized reasoning agent for drug discovery.pdf"
---

# Drugpilot: Llm-based parameterized reasoning agent for drug discovery

> **저자**: Kun Li, Zhennan Wu, Shoupeng Wang, Jia Wu, Shirui Pan, Wenbin Hu | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 2](figures/fig2.webp) *DrugPilot 프레임워크의 구조: LLM, 매개변수화된 메모리 풀(PMP), Fe-Fo 메커니즘, AI 모델 집합으로 구성된 통합 시스템*

본 논문은 신약 개발의 전 단계를 지원하는 대형 언어모델(LLM) 기반 에이전트 시스템 DrugPilot을 제시한다. 매개변수화된 메모리 풀(Parameterized Memory Pool, PMP)을 통해 이질적인 약물 데이터를 표준화된 표현으로 변환하고, 피드백-포커스(Fe-Fo) 메커니즘으로 LLM의 추론 오류를 실시간 모니터링하여 정확한 도구 호출과 멀티턴 대화를 가능하게 한다.

## Motivation

- **Known**: 최근 AI 기반 신약 개발 도구들(Chemistry42, MolProphet, DrugFlow 등)이 성능을 입증했으며, LLM 기반 에이전트(DrugAgent 등)가 다중 출처 이질 데이터 처리에서 장점을 보임

- **Gap**: 기존 LLM 기반 약물 발견 시스템은 (1) 비전산 사용자의 진입장벽 높음, (2) 단일 작업 중심으로 멀티스테이지 연계 부족, (3) 자연어 출력으로 인한 정확한 도메인 표현 불가, (4) 텍스트 기반 메모리의 정보 손실 문제, (5) 도구 호출 정확도 및 멀티턴 대화 능력 부족

- **Why**: 신약 개발은 약물 생성, 최적화, 타겟 친화성 예측, 분자 특성 예측 등 다단계 프로세스이며, 약학 및 생물학 분야 연구자들은 복잡한 AI 모델 운영, 데이터 전처리, 플랫폼 간 형식 변환에 어려움을 겪음

- **Approach**: 매개변수화된 메모리 풀로 멀티모달 데이터를 구조화하고, Fe-Fo 메커니즘으로 LLM의 추론 오류를 피드백하며, 8개 핵심 약물 발견 작업을 지원하는 통합 에이전트 프레임워크 제안

## Achievement

![Figure 1](figures/fig1.webp) *DrugPilot의 응용 시나리오 및 기존 약물 발견 LLM/에이전트와의 비교: 코드 불필요(Zero-Code), 확장 가능한 데이터 획득, 조율된 멀티태스크 처리, 정확한 실행*

1. **벤치마크 성능**: Berkeley function-calling 벤치마크에서 단순(Simple), 멀티-도구(Multi-tool), 멀티턴(Multi-turn) 시나리오에서 각각 98.0%, 93.5%, 64.0%의 작업 완료율 달성. ReAct 대비 13.2%, 66.1%, 80.3% 향상

2. **신약 발견 데이터셋 구축**: 8개 약물 발견 작업을 아우르는 2,800개의 고품질 주석 샘플로 이루어진 도구 호출 벤치마크(TCDD, Tool-Calling Dataset for Drug Discovery) 최초 제안

3. **실무 적용성**: 분자 최적화 작업에서 기존 LLM 대비 100-1,000배 많은 정확한 SMILES 후보(수십 개 → 수백-수천 개) 생성 가능

## How

![Figure 2](figures/fig2.webp) *PMP의 구조: 키-값 쌍으로 메모리 저장, LLM은 간결한 키와 상호작용하고 도구는 구조화된 값과 직접 상호작용*

- **매개변수화된 메모리 풀(PMP)**: 사용자 입력과 도구 실행 결과를 구조화된 키-값 형식으로 저장. LLM은 간결한 키만 접근하고 도구는 구조화된 값과 직접 상호작용하여 정보 손실 최소화

- **Fe-Fo 메커니즘**: LLM의 PMP 해석 오류와 도구 호출 실패 시 구체적인 오류 피드백 제공 및 원래 질문 재제시로 장시간 대화에서의 포커스 유지

- **멀티턴 대화 지원**: 자동 파일 파싱, 매개변수/예측 결과의 PMP 저장, 다운로드/수정/삭제 연산(CRUD) 지원

- **8단계 AI 모델 통합**: 약물 생성, 최적화, 타겟 친화성 예측, 성질 예측 등 작업별 최신 딥러닝 모델의 무접합 통합(Seamless Integration)

- **이중 출력 형식**: 자연어 기반 결론 제시와 PMP를 통한 데이터 시각화 병행

## Originality

- 신약 개발 특화 LLM 에이전트를 위한 **매개변수화된 메모리 풀** 아키텍처 최초 제안으로, 이질적 데이터의 표준화와 정보 손실 해결

- **피드백-포커스(Fe-Fo) 메커니즘**으로 LLM의 도구 호출 오류를 실시간 감지하고 정정하는 자동 모니터링 체계 구현

- **도구 호출 벤치마크(TCDD)** 최초 구축: 약물 발견 작업 8개, 2,800개 주석 샘플로 LLM 에이전트의 체계적 평가 가능화

- 비전산 사용자의 **코드 불필요(Zero-Code) 인터페이스** 제공으로 약학/생물학 연구자의 접근성 대폭 개선

## Limitation & Further Study

- **PMP 확장성**: 대규모 약물 데이터베이스(예: ChEMBL 수백만 화합물)에서의 메모리 풀 관리 효율성 및 검색 속도 평가 부족

- **도메인 적응성**: 현재 8개 핵심 작업에 한정되어 있으며, 신규 약물 발견 작업(예: 임상 시험 설계, 약동학 모델링)으로의 확장 경로 불명확

- **LLM 의존성**: 기본 LLM 모델의 성능에 크게 의존하며, 도메인 특화 소규모 언어모델(Small Language Models)과의 호환성 검증 필요

- **해석 가능성(Explainability)**: Fe-Fo 메커니즘의 오류 정정 과정과 멀티턴 의사결정 경로의 투명성 강화 필요

- 후속 연구: (1) 약물-단백질 상호작용의 물리적 원리 기반 제약 조건 통합, (2) 실험 검증 피드백 루프 구축, (3) 임상 단계 데이터와의 연계


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.0/5
- Significance: 4.5/5
- Clarity: 4.0/5
- Overall: 4.2/5

**총평**: DrugPilot은 매개변수화된 메모리 풀과 피드백-포커스 메커니즘이라는 혁신적 아키텍처를 통해 LLM 기반 신약 개발 에이전트의 정확성과 사용성을 획기적으로 개선했으며, 첫 약물 발견 도구 호출 벤치마크 제시로 해당 분야의 학술적 기여도가 높다. 다만 대규모 데이터 처리 효율성 평가와 임상 단계로의 확장 경로가 보완되면 실무 적용 가능성이 한층 높아질 것으로 예상된다.

## Related Papers

- 🔄 다른 접근: [[papers/638_ProtAgents_protein_discovery_via_large_language_model_multi-/review]] — 신약 vs 단백질 발견에서 LLM 기반 다중 에이전트 시스템의 다른 적용 분야를 비교할 수 있다
- 🔗 후속 연구: [[papers/306_Efficient_fine-tuning_of_single-cell_foundation_models_enabl/review]] — 단일세포 모델의 약물 반응 예측을 LLM 기반 신약 개발 에이전트와 통합한 확장 연구다
- 🏛 기반 연구: [[papers/115_Augmenting_large_language_models_with_chemistry_tools/review]] — LLM에 전문 도구를 통합하는 방법론이 매개변수화된 추론 에이전트의 기반을 제공한다
- 🔄 다른 접근: [[papers/490_LIDDIA_Language-based_Intelligent_Drug_Discovery_Agent/review]] — 신약 발견에서 LLM 기반 에이전트의 다른 설계 접근법과 구현 방식을 비교할 수 있다
- 🔗 후속 연구: [[papers/306_Efficient_fine-tuning_of_single-cell_foundation_models_enabl/review]] — LLM 기반 신약 개발 에이전트와 단일세포 모델을 결합하여 더 정확한 약물 효과 예측을 할 수 있다
- 🔄 다른 접근: [[papers/638_ProtAgents_protein_discovery_via_large_language_model_multi-/review]] — 단백질 vs 약물 발견에서 LLM 기반 다중 에이전트 시스템의 다른 적용 분야를 비교할 수 있다
- 🔗 후속 연구: [[papers/115_Augmenting_large_language_models_with_chemistry_tools/review]] — 화학 도구 통합 방법론을 신약 개발의 전체 파이프라인으로 확장한 연구다
- 🏛 기반 연구: [[papers/291_Drugclip_Contrastive_drug-disease_interaction_for_drug_repur/review]] — 매개변수화된 추론 약물 파일럿이 약물-질병 상호작용의 기반 제공
