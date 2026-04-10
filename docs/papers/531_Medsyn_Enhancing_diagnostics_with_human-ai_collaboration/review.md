---
title: "531_Medsyn_Enhancing_diagnostics_with_human-ai_collaboration"
authors:
  - "Burcu Sayin"
  - "Ipek Baris Schlicht"
  - "Ngoc Vo Hong"
  - "Sara Allievi"
  - "Jacopo Staiano"
date: "2025"
doi: "N/A"
arxiv: ""
score: 3.5
essence: "본 논문은 의사와 대규모언어모델(Large Language Models, LLM)이 다중 턴 대화를 통해 협력하는 하이브리드 의료진단 프레임워크 MedSyn을 제안한다. 의사의 인지적 편향과 정보 불완전성을 보완하기 위해 동적 대화 기반의 의료 의사결정 지원 시스템을 개발하였다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Clinical_Multi-Agent_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Sayin et al._2025_Medsyn Enhancing diagnostics with human-ai collaboration.pdf"
---

# Medsyn: Enhancing diagnostics with human-ai collaboration

> **저자**: Burcu Sayin, Ipek Baris Schlicht, Ngoc Vo Hong, Sara Allievi, Jacopo Staiano, Pasquale Minervini, Andrea Passerini | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) *MedSyn 프레임워크 개요: 의사와 LLM 어시스턴트 간의 다중 턴 대화 구조*

본 논문은 의사와 대규모언어모델(Large Language Models, LLM)이 다중 턴 대화를 통해 협력하는 하이브리드 의료진단 프레임워크 MedSyn을 제안한다. 의사의 인지적 편향과 정보 불완전성을 보완하기 위해 동적 대화 기반의 의료 의사결정 지원 시스템을 개발하였다.

## Motivation

- **Known**: 최근 LLM이 임상 의사결정 지원 도구로 활용될 가능성을 보여주고 있으며, 의료진단에서 인지적 편향과 불완전한 정보로 인한 오진 위험이 존재한다.

- **Gap**: 기존의 정적(static) 일회성 의료 의사결정 지원 도구는 실제 임상 실무의 복잡성을 충분히 반영하지 못하며, 의사와 AI 간의 상호작용적 협력을 통한 다중 턴 대화 기반 접근이 부족하다.

- **Why**: 시간 압박과 높은 인지 부하가 있는 실무 환경(응급실 등)에서 의사와 AI 어시스턴트의 상호작용적 논의가 진단 정확도와 치료 결정을 향상시킬 수 있다.

- **Approach**: 의사 에이전트는 환자의 주요증상만 접근하고, 어시스턴트 LLM은 전체 임상 기록에 접근하여 반복적 질문과 협력적 추론을 통해 다중 턴 대화를 시뮬레이션한다.

## Achievement

1. **오픈소스 LLM 평가**: 25개의 오픈소스 모델을 조사하여 다중 턴 대화 능력을 평가한 결과, Llama3(8B, 70B)과 Gemma2(27B)가 가장 유망한 후보로 식별되었다. 대부분의 의료 도메인 특화 모델(Meditron, MedLlama2)은 실제 대화 유지에 제한이 있었다.

2. **다중 턴 대화의 효과성**: 시뮬레이션된 의사-LLM 상호작용을 통해 반복적 다중 스텝 교환이 일회성 기본 모델(baseline "phy w/complaint")에 비해 더욱 포괄적인 환자 평가와 진단 명확성을 제공함을 입증했다.

3. **데이터셋 구축**: MIMIC-IV와 MIMIC-IV-Note를 통합하여 74,850개 환자 기록(테스트셋 1,000개)으로 구성된 표준화된 의료 데이터셋을 구축하였고, 2,350개의 고유 진단명과 5.61개의 평균 ICD-10 코드를 포함한다.

## How

- **프레임워크 구조**: 의사가 환자의 주요증상으로 초기 평가를 요청하면, LLM 어시스턴트는 전체 임상 기록을 분석하여 상세한 평가를 제공한다. 이후 의사는 추가 정보가 필요하면 추가 질문을 하고, 충분한 정보를 수집하여 확신할 때까지 대화를 지속한다.

- **에이전트 설정**: 기본 사례(Baseline)는 의사 에이전트가 주요증상만 접근하여 일회성 진단을 내리고, 두 에이전트 사례(Two-agent)는 의사 에이전트가 어시스턴트와 대화하며 정보를 수집한다.

- **기술 스택**: Ollama와 Langroid를 사용한 다중 에이전트 환경 구현으로 실제 임상 상황의 대화 시뮬레이션을 수행한다.

- **평가 방법**: Zero-shot prompting을 사용하여 LLM 의사결정 과정과 대화 추적을 정성적으로 분석하고, 의료진 검토를 통해 유효성을 검증한다.

- **ICD-10 코드링**: 진단과 함께 임상 표준 ICD-10 코드 생성을 포함하여 실제 의료 워크플로우를 반영한다.

## Originality

- **하이브리드 협력 모델**: 기존의 단방향 AI 의료 지원 도구와 달리, 의사와 LLM이 대등한 입장에서 상호 비판적으로 검토하는 쌍방향 협력 구조를 제안한 점이 혁신적이다.

- **다중 턴 대화 중심**: 일회성 추론이 아닌 반복적 질의응답을 통해 의료진단의 불확실성을 감소시키는 접근법이 기존 의료 AI 시스템과 차별화된다.

- **실제 임상 시나리오 모의**: MIMIC 데이터셋을 기반으로 실제 임상 기록 구조(주요증상, 병력, 신체검사, 검사결과, ICD-10 코딩)를 완전히 반영한 현실적인 평가 환경을 구축했다.

- **오픈소스 모델 중심 평가**: 상용 클로즈드 모델이 아닌 오픈소스 LLM의 의료 적용 가능성을 체계적으로 검증함으로써 의료기관의 배포 용이성을 고려했다.

## Limitation & Further Study

**한계**:
- 현재는 LLM 간 시뮬레이션에 기반한 평가로, 실제 의료진과의 상호작용 데이터 부재로 실임상 효과성을 입증하지 못함
- 인지적 편향 감소와 진단 정확도 향상의 정량적 메트릭이 부족함
- MIMIC 데이터셋의 제한된 접근성으로 인해 재현성과 외부 검증이 어려움
- 25개 모델 중 대부분이 의료 다중 턴 대화에서 성능 저하를 보였으나, 그 원인 분석 부족
- ICD-10 코드 매칭의 정확성 평가 메트릭이 명시되지 않음

**후속 연구**:
- 실제 의료진과의 인터랙션을 통한 MedSyn의 임상 유효성 검증 필요
- 진단 정확도, 환자 안전성, 의료진의 인지 부하 감소 등에 대한 정량적 평가 수행
- 더 큰 규모의 환자 사례와 다양한 임상 설정(특화 진료과)에서의 일반화 능력 평가
- 의료 도메인 특화 LLM의 다중 턴 대화 능력 향상을 위한 파인튜닝 전략 개발
- 환각(hallucination) 문제와 의료 윤리적 고려사항에 대한 심층 분석

## Evaluation

- **Novelty**: 4/5
  - 의료 AI의 다중 턴 협력 대화 프레임워크는 혁신적이나, 대화형 의료 AI 자체는 완전히 새로운 개념은 아님

- **Technical Soundness**: 3.5/5
  - 프레임워크 설계와 데이터셋 구축은 견고하나, LLM 시뮬레이션 기반 평가의 타당성 제한 및 정량적 메트릭 부족

- **Significance**: 3.5/5
  - 의료 의사결정 지원 분야에서 실용적 가치가 높으나, 아직 실임상 검증 전단계로 임상적 영향력 미확인

- **Clarity**: 4/5
  - 전반적으로 명확하게 작성되었으나, 모델 평가 결과와 두 시나리오의 성능 비교 분석이 구체적으로 제시되지 않음

- **Overall**: 3.5/5

**총평**: MedSyn은 의료 의사결정에서 인간-AI 협력의 새로운 패러다임을 제시하는 흥미로운 프레임워크이나, 현재는 LLM 시뮬레이션 기반의 예비 결과 단계로 실제 의료진 참여와 임상적 검증이 시급하다.

## Related Papers

- 🏛 기반 연구: [[papers/233_Cognitio_emergens_Agency_dimensions_and_dynamics_in_human-ai/review]] — 인간-AI 지식 협력의 이론적 프레임워크를 의료 진단 분야에 구체적으로 적용한다.
- 🔗 후속 연구: [[papers/663_Reinforcing_clinical_decision_support_through_multi-agent_sy/review]] — 임상 의사결정 지원에서 다중 에이전트 시스템으로 의료 AI 협력을 확장한다.
- 🧪 응용 사례: [[papers/821_Towards_a_client-centered_assessment_of_llm_therapists_by_cl/review]] — 클라이언트 중심 LLM 치료사 평가로 의료 분야 인간-AI 협력의 다른 적용을 보여준다.
- 🧪 응용 사례: [[papers/821_Towards_a_client-centered_assessment_of_llm_therapists_by_cl/review]] — 클라이언트 시뮬레이션을 실제 진단 향상에 적용한 Human-AI 협력 사례
- 🏛 기반 연구: [[papers/624_Piors_Personalized_intelligent_outpatient_reception_based_on/review]] — 진단을 위한 인간-AI 협력 향상이 개인화된 의료 접수 서비스 설계의 방법론적 기반을 제공합니다.
- 🧪 응용 사례: [[papers/233_Cognitio_emergens_Agency_dimensions_and_dynamics_in_human-ai/review]] — 인간-AI 협력의 이론적 프레임워크를 의료 진단 분야에 구체적으로 적용한 사례를 보여준다.
- 🔄 다른 접근: [[papers/663_Reinforcing_clinical_decision_support_through_multi-agent_sy/review]] — 의료 진단에서 ICU 환경 임상 의사결정 지원으로 의료 AI 협력의 다른 응용을 제시한다.
