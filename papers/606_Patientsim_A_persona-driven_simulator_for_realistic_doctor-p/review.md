---
title: "606_Patientsim_A_persona-driven_simulator_for_realistic_doctor-p"
authors:
  - "Daeun Kyung"
  - "Hyunseung Chung"
  - "Seongsu Bae"
  - "Jiho Kim"
  - "Jae Ho Sohn"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "PATIENTSIM은 다양한 환자 페르소나를 반영하여 현실적인 의사-환자 상호작용을 시뮬레이션하는 LLM 기반 환자 시뮬레이터로, 임상 전문가의 검증을 통해 강건성을 입증했다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Clinical_Multi-Agent_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Srirag et al._2025_Patientsim A persona-driven simulator for realistic doctor-patient interactions.pdf"
---

# Patientsim: A Persona-Driven Simulator for Realistic Doctor-Patient Interactions

> **저자**: Daeun Kyung, Hyunseung Chung, Seongsu Bae, Jiho Kim, Jae Ho Sohn, Taerim Kim, Soo Kyung Kim, Edward Choi | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) *PATIENTSIM의 전체 프레임워크: 실제 의료 데이터(MIMIC-IV, MIMIC-ED)에서 추출한 170개의 임상 프로필과 4가지 축(성격, 언어 능력, 의료 이력 회상 수준, 인지 혼동 수준)으로 정의된 37개의 고유한 페르소나를 결합하여 현실적인 의사-환자 대화를 생성함*

PATIENTSIM은 다양한 환자 페르소나를 반영하여 현실적인 의사-환자 상호작용을 시뮬레이션하는 LLM 기반 환자 시뮬레이터로, 임상 전문가의 검증을 통해 강건성을 입증했다.

## Motivation

- **Known**: 대규모 언어 모델(LLM)은 의료 단일 턴 질문-답변 벤치마크(MedQA, MedMCQA 등)에서 우수한 성능을 보이지만, 실제 임상 진료는 다중 턴(multi-turn), 맥락 인식적 대화(context-aware communication)를 필요로 함

- **Gap**: 기존 LLM 기반 환자 시뮬레이터는 임상 현장의 다양한 환자 페르소나를 충분히 반영하지 못하며, 환자의 감정 상태, 언어 능력, 의료 지식 수준 등 상담 품질에 영향을 미치는 요소들을 무시함

- **Why**: 표준화 환자(Standardized Patients, SP)는 높은 비용, 일관성 부족, 확장성의 한계로 인해 실용적이지 않으므로, 확장 가능하고 비용 효율적인 LLM 기반 대안이 필요함

- **Approach**: 실제 의료 데이터(MIMIC-IV, MIMIC-ED)에서 추출한 임상 프로필과 4가지 축(성격, 언어 능력, 의료 이력 회상 수준, 인지 혼동 수준)으로 정의된 다양한 페르소나를 결합하여 현실적인 환자 시뮬레이터 개발

## Achievement

![Figure 1](figures/fig1.webp) *170개의 실제 임상 프로필 × 37개의 페르소나 조합으로 구성된 PATIENTSIM의 구조 및 다양한 환자-의사 대화의 예시*

1. **포괄적 페르소나 프레임워크**: 4개의 축(성격, 언어 능력, 의료 이력 회상 수준, 인지 혼동 수준)과 실제 임상 데이터를 결합하여 37개의 고유한 환자 페르소나와 170개의 임상 프로필(총 6,290개의 시뮬레이션 가능)을 생성

2. **8개 LLM 평가 및 최적 모델 선정**: Llama 3.3 70B를 최종 모델로 선정하며, 팩트 정확도(factual accuracy)와 페르소나 일관성(persona consistency)을 동시에 유지함을 입증

3. **임상 전문가 검증**: 4명의 임상의가 6가지 평가 기준에서 평균 3.89/4.0의 점수를 부여하여 시뮬레이션의 강건성 확인

4. **오픈소스 기반 확장 가능 플랫폼**: 개인정보 보호를 준수하면서 의료 대화 시스템 평가를 위한 재현 가능하고 확장 가능한 솔루션 제공

## How

![Figure 2](figures/fig2.webp) *문장 수준의 팩트 검증 프로세스: PATIENTSIM의 각 응답에 대해 임상 프로필과의 일관성 확인*

- **임상 프로필 구성**: MIMIC-IV와 MIMIC-ED에서 170개의 실제 환자 프로필 추출(나이, 성별, 혼인 상태, 의료력, 주요 증상, 약물 등 포함)

- **페르소나 축 설정**: 
  - 성격(Personality): Neutral, Impatient, Distrustful, Overanxious, Pleasing, Verbose (6가지)
  - 언어 능력(Language Proficiency): Basic, Intermediate, Advanced (3가지)
  - 의료 이력 회상 수준(Medical History Recall Level): High Recall, Low Recall (2가지)
  - 인지 혼동 수준(Cognitive Confusion Level): Normal, Highly Confused (2가지)
  - 총 6 × 3 × 2 × 2 = 72가지 조합 중 임상적으로 타당한 37가지 선정

- **히스토리 테이킹 중심 설계**: 진단의 약 80%가 히스토리 테이킹에만 의존한다는 임상 증거를 기반으로, 객관적 데이터(검사 결과)의 불완전성 문제를 회피하고 주관적 데이터(환자 진술)의 자연스러운 가변성을 활용

- **LLM 선택 및 평가**: 8개 모델(GPT-4, GPT-4o, Claude-3 계열, Llama 계열 등)을 팩트 정확도와 페르소나 일관성 기준으로 평가하여 Llama 3.3 70B 최종 선정

- **응답 품질 검증**: 임상 프로필과의 일관성, 환자 안전성, 상담 자연스러움 등 6가지 기준으로 임상 전문가 검증

## Originality

- 심리 상담 시뮬레이션의 감정적 현실성과 일반 진료 시뮬레이션의 임상 정확도를 결합한 최초의 환자 시뮬레이터 프레임워크

- 4개 축의 페르소나를 체계적으로 정의하고, 단순 키워드 설명(Big Five 특성 등)이 아닌 실제 다중 턴 대화 생성 및 평가를 통한 페르소나 구현

- 히스토리 테이킹에 집중하여 의료 데이터의 불완전성 문제를 우아하게 해결하고, 실제 임상 진료의 정보 수집 프로세스와의 높은 유사성 달성

- 170개의 실제 환자 프로필(MIMIC 데이터) × 37개 페르소나 조합으로 6,290개의 다양한 시뮬레이션 구성 가능

- 오픈소스 기반으로 재현 가능성과 접근성을 높이고, 플랫폼의 커스터마이징 가능성 제공

## Limitation & Further Study

- **단일 세션, ED 방문 중심 제약**: 연구가 응급실 첫 방문 단일 세션으로 제한되어, 치료 효과, 질병 진행, 추적 관찰 등을 포함한 종단 환자 상태 변화(longitudinal patient state changes) 모델링 불가능

- **객관적 데이터의 부재**: 신체 검사, 검사실 결과, 영상 검사 등 객관적 데이터 생성 기능 부재로, 진단의 다른 80%를 커버하지 못함. 향후 신뢰성 있는 합성 검사 결과 생성 방법론 개발 필요

- **페르소나 조합의 임상적 타당성**: 37개 페르소나 중 일부 조합(예: 매우 혼동된 상태의 발달된 의료 지식)은 임상적으로 드물 수 있으므로, 더 정교한 가중치 기반 페르소나 선정 방안 고려 필요

- **언어 및 문화적 다양성 부족**: 영어 중심 설계로, 다국어 및 문화적으로 다양한 환자 행동 반영 제한. 향후 다국어 및 다문화 페르소나 확장 필요

- **의료 전문 분야 확대**: 현재 ED(응급실) 중심이므로, 만성질환 추적, 정신건강 상담, 전문의 진료 등 다양한 임상 환경으로의 확장 고려

## Evaluation

- **Novelty**: 4/5
  - 페르소나 기반 환자 시뮬레이션 프레임워크의 체계적 설계는 창신성이 높으나, 개별 요소(LLM 활용, MIMIC 데이터 사용)는 기존 연구와 유사

- **Technical Soundness**: 4/5
  - 히스토리 테이킹 중심 설계 등 임상적으로 타당한 기술 선택이 탁월하나, 객관적 데이터 생성 제약과 종단 모델링 불가는 완전성 측면에서 미흡

- **Significance**: 4/5
  - 의료 교육 및 의사 LLM 평가를 위한 실질적 도구 제공으로 의의 높으나, 응급실 단일 세션으로 제한되어 임상 전체 범위 커버는 미충분

- **Clarity**: 4/5
  - 프레임워크 설명과 동기부여가 명확하며, Figure 1이 전체 구조를 직관적으로 표현함. 다만 일부 기술적 세부사항(페르소나 선정 알고리즘 등)의 상세 설명 부족

- **Overall**: 4/5

**총평**: PATIENTSIM은 실제 의료 데이터와 체계적인 페르소나 프레임워크를 결합하여 현실적인 의사-환자 상호작용 시뮬레이션에서 의미 있는 진전을 이루었으며, 임상 전문가 검증과 오픈소스 제공으로 의료 AI 교육 및 평가를 위한 실용적 기여를 제시한다. 다만 단일 세션 제약과 객관적 데이터 부재는 향후 개선이 필요한 주요 한계점이다.

## Related Papers

- 🔄 다른 접근: [[papers/433_Interactive_agents_Simulating_counselor-client_psychological/review]] — PATIENTSIM과 Interactive agents 모두 의료 상담 시뮬레이션을 다루지만 의사-환자 vs 상담사-내담자 관계에 초점을 둔다.
- 🔗 후속 연구: [[papers/644_Psyche_A_multi-faceted_patient_simulation_framework_for_eval/review]] — 다면적 환자 시뮬레이션 프레임워크 Psyche는 PATIENTSIM의 페르소나 기반 환자 시뮬레이션을 심리학적 측면까지 확장한다.
- 🧪 응용 사례: [[papers/528_MedAgentGym_A_Scalable_Agentic_Training_Environment_for_Code/review]] — 코딩 능력을 위한 확장 가능한 에이전트 훈련 환경 MedAgentGym은 환자 시뮬레이터의 의료 교육 활용을 구체화한다.
- 🧪 응용 사례: [[papers/838_Training_socially_aligned_language_models_in_simulated_human/review]] — 의사-환자 시뮬레이션은 사회적으로 정렬된 언어모델 학습이 의료 분야에 적용된 구체적인 사례입니다
- 🔗 후속 연구: [[papers/821_Towards_a_client-centered_assessment_of_llm_therapists_by_cl/review]] — 표준화된 환자 개념을 LLM 치료사 평가로 확장한 의료 시뮬레이션 발전
- 🔗 후속 연구: [[papers/624_Piors_Personalized_intelligent_outpatient_reception_based_on/review]] — 환자 시뮬레이션을 위한 페르소나 기반 시스템이 개인화된 외래 접수 서비스로 확장될 수 있습니다.
- 🧪 응용 사례: [[papers/413_Human-ai_teaming_using_large_language_models_Boosting_brain-/review]] — PatientSim의 환자 시뮬레이션이 ChatBCI의 뇌 신호 분석 연구에서 실제 임상 시나리오 검증에 활용됨
- 🔗 후속 연구: [[papers/078_Ai_hospital_Benchmarking_large_language_models_in_a_multi-ag/review]] — AI Hospital의 다중 에이전트 의료 시뮬레이션은 PatientSim의 페르소나 기반 환자 시뮬레이션을 확장하여 의사-환자 상호작용을 포함한 완전한 병원 환경을 구현합니다.
- 🔄 다른 접근: [[papers/433_Interactive_agents_Simulating_counselor-client_psychological/review]] — Interactive agents와 PATIENTSIM 모두 의료 상담 시뮬레이션을 다루지만 상담사-내담자 vs 의사-환자 관계에 초점을 둔다.
