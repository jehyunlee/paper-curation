---
title: "168_Biomni_A_General-Purpose_Biomedical_AI_Agent"
authors:
  - "Kexin Huang"
  - "Serena Zhang"
  - "Hanchen Wang"
  - "Yuanhao Qu"
  - "Yingzhou Lu"
date: "2025"
doi: "10.1101/2025.05.30.656746"
arxiv: ""
score: 4.2
essence: "본 논문은 생의학 연구의 단편화된 워크플로우 문제를 해결하기 위해 일반목적 생의학 AI 에이전트 Biomni를 제시한다. 이는 150개의 전문 도구, 105개의 소프트웨어 패키지, 59개의 데이터베이스를 통합한 최초의 통합 생의학 행동 공간(Biomni-E1)과 이를 활용하는 지능형 에이전트 아키텍처(Biomni-A1)로 구성되어 있다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Biomedical_Research_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Huang et al._2025_Biomni A General-Purpose Biomedical AI Agent.pdf"
---

# Biomni: A General-Purpose Biomedical AI Agent

> **저자**: Kexin Huang, Serena Zhang, Hanchen Wang, Yuanhao Qu, Yingzhou Lu | **날짜**: 2025 | **DOI**: [10.1101/2025.05.30.656746](https://doi.org/10.1101/2025.05.30.656746)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: Biomni의 통합 생의학 행동 공간 및 에이전트 환경 개요. (a) 생의학 논문에서 체계적으로 행동을 발견하는 워크플로우*

본 논문은 생의학 연구의 단편화된 워크플로우 문제를 해결하기 위해 일반목적 생의학 AI 에이전트 Biomni를 제시한다. 이는 150개의 전문 도구, 105개의 소프트웨어 패키지, 59개의 데이터베이스를 통합한 최초의 통합 생의학 행동 공간(Biomni-E1)과 이를 활용하는 지능형 에이전트 아키텍처(Biomni-A1)로 구성되어 있다.

## Motivation

- **Known**: 최근 AI 에이전트가 소프트웨어 공학, 법률, 재료과학 등 다양한 분야에서 반복적 작업을 자동화하고 생산성을 향상시키고 있다.

- **Gap**: 기존 생의학 AI 시스템은 특정 작업에만 최적화된 specialist agentic workflows에 의존하여 다양한 생의학 하위 분야에 걸쳐 일반화되지 못하고 있다. 또한 LLM의 추론 능력을 복잡한 생의학 행동의 실행과 결합하는 것이 기술적으로 도전적이다.

- **Why**: 생의학 데이터는 풍부하지만 분석 전문 인력이 부족하며, 복잡한 실험, 대규모 데이터셋, 수많은 분석 도구, 광범위한 문헌으로 인해 반복적이고 단편화된 워크플로우가 발견을 저해하고 있다.

- **Approach**: (1) 25개 생의학 도메인의 수천 개 논문을 분석하여 AI 기반 행동 발견 에이전트로 필수 도구, 데이터베이스, 프로토콜 추출, (2) 검색 기반 계획과 코드 기반 실행을 통합한 일반목적 에이전트 아키텍처 개발, (3) 사전정의된 템플릿 없이 동적 워크플로우 구성 가능하도록 설계.

## Achievement

![Figure 2](figures/fig2.webp)
*Figure 2: 다양한 현실적 생의학 작업에 대한 Biomni의 영점사격(Zero-shot) 일반화. (a) Biomni가 6개 기준 모델보다 우수함*

1. **통합 생의학 행동 공간 구축**: 25개 생의학 도메인에 걸쳐 150개의 특화된 도구, 105개의 소프트웨어 패키지, 59개의 데이터베이스를 포함하는 Biomni-E1 환경 최초 구축. 이는 체계적인 AI 기반 논문 분석을 통해 수행됨.

2. **강력한 일반화 성능**: 원인 유전자 우선순위 지정(causal gene prioritization), 약물 재표적화(drug repurposing), 희귀질환 진단, 미생물군집 분석, 분자 클로닝 등 다양한 생의학 작업에서 작업 특화 프롬프트 튜닝 없이 강력한 성능 달성.

3. **다중 모달 생의학 데이터 분석**: 458개 웨어러블 센서 데이터 파일 분석, 단일세포 RNA-seq 및 ATAC-seq 데이터에 대한 포괄적 생정보학 분석을 자율적으로 수행하여 실험 검증 가능한 가설 생성.

4. **습식 실험실 프로토콜 설계**: 10개의 실제 클로닝 시나리오에 대한 개방형 클로닝 벤치마크에서 실험실 연구자를 지원하기 위한 자동화된 프로토콜 설계 능력 시연.

## How

![Figure 3](figures/fig3.webp)
*Figure 3: Biomni가 자율적으로 복잡한 다중모달 생의학 분석을 실행하여 가설 생성. (a-d) Biomni가 신속하게...*

**Biomni-E1 (환경) 구축:**
- 생의학 논문 100개/도메인 × 25개 도메인에서 AI 에이전트를 통해 작업, 도구, 데이터베이스 자동 추출
- 전문가 검증을 거친 150개 도구의 상세 구현 (복잡한 코드, 도메인 전문성, AI 모델 포함)
- 105개 생물학 소프트웨어 패키지 사전 설치 (Python, R, Bash 지원)
- 웹 API 기반 관계형 데이터베이스(PDB, OpenTarget, ClinVar)와 로컬 데이터레이크 통합 데이터베이스 구현
- 자연언어 쿼리를 LLM으로 동적 데이터베이스 쿼리로 변환하는 통합 함수 설계

**Biomni-A1 (에이전트) 아키텍처:**
- **검색 기반 도구 선택**: 사용자 목표에 따라 LLM이 관련 도구/데이터베이스 동적 선택
- **코드 기반 실행**: 루프, 병렬화, 조건부 로직을 포함한 복잡한 워크플로우 구성 가능
- **절차적 로직 통합**: 사전정의된 함수 서명을 따르지 않는 소프트웨어, 도구, 데이터베이스, 원본 데이터 작업 유연하게 통합
- **LLM 기반 추론**: 도메인 전문성과 결합된 LLM 추론으로 상세한 단계별 계획 생성

![Figure 4](figures/fig4.webp)
*Figure 4: Biomni가 습식 실험실 실험 프로토콜 설계. (a) 10개 실제 클로닝 시나리오의 개방형 클로닝 벤치마크*

## Originality

- **최초의 통합 생의학 행동 공간**: 25개 도메인의 수천 개 논문으로부터 체계적으로 추출한 150개 도구 + 105개 소프트웨어 + 59개 데이터베이스의 포괄적 환경 구축이 선례 없음.

- **AI 기반 행동 발견 방법론**: LLM 에이전트를 활용하여 생의학 문헌에서 자동으로 필수 작업, 도구, 데이터베이스를 체계적으로 추출하는 접근법의 혁신성.

- **코드 기반 액션 인터페이스**: 전통적인 함수 호출 방식 대신 코드를 범용 액션 인터페이스로 사용하여 생의학 워크플로우의 동적 복잡성 지원.

- **작업 특화 없는 일반화**: 사전정의된 템플릿이나 작업 특화 프롬프트 튜닝 없이 영점사격(zero-shot) 일반화를 다양한 현실적 생의학 작업에서 달성.

- **실증적 영향력**: 웨어러블 데이터 분석, 고처리량 생정보학 분석, 습식실험실 프로토콜 설계 등 실제 생의학 연구 사례에서 자율적 수행 능력 입증.

## Limitation & Further Study

- **성능 평가의 제한**: 논문의 첫 15,000자에서는 벤치마크 세부 방법론과 정량적 성능 지표(정확도, F1 점수 등)가 명확히 제시되지 않아 다른 방법과의 비교 강도 판단 어려움.

- **도구 정확성 보증 부재**: 복잡한 생의학 도구의 정확성, 버전 호환성, 예상치 못한 오류 처리에 대한 검증 체계의 명확한 설명 부족.

- **데이터 접근성과 개인정보 보호**: 민감한 임상 데이터나 개인의료정보(PHI)를 포함한 생의학 작업의 실제 배포 시 규제 준수와 데이터 보안에 대한 논의 미흡.

- **에이전트 오류 상황 처리**: 도구 호출 실패, 데이터베이스 쿼리 오류, 논리 오류 발생 시 에이전트의 자기 수정(self-correction) 및 폴백(fallback) 메커니즘 상세 설명 부재.

- **후속 연구 방향**: (1) 더 대규모 생의학 도메인으로 확장, (2) 멀티에이전트 협업 시스템 설계로 인간 생의학자와의 상호작용 강화, (3) 실제 실험실 환경과의 연동 자동화 수준 향상, (4) 설명 가능성(explainability) 강화로 에이전트의 의사결정 과정 투명성 증대.


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.2/5

**총평**: 본 논문은 생의학 연구의 실질적 병목을 해결하기 위한 최초의 일반목적 생의학 AI 에이전트를 제시하는 역작으로, 대규모 통합 환경 구축과 다양한 현실 사례 입증을 통해 높은 임팩트를 보이나, 정량적 벤치마킹과 기술 상세 설명의 강화로 더욱 견실한 기여가 될 수 있다.

## Related Papers

- 🔄 다른 접근: [[papers/151_Benchmarking_ai_scientists_in_omics_data-driven_biological_r/review]] — 생의학 연구 지원이라는 동일한 목표를 통합 에이전트와 벤치마크 평가라는 상호 보완적 접근으로 달성합니다.
- 🔗 후속 연구: [[papers/260_DeepCRE_Transforming_Drug_RD_via_AI-Driven_Cross-drug_Respon/review]] — 약물 반응 예측을 포함한 포괄적 생의학 워크플로우로 약물 개발 AI를 확장합니다.
- 🧪 응용 사례: [[papers/626_Polymer_Brushes_and_Grafted_Polymers_AIML-Driven_Synthesis_S/review]] — 통합 생의학 플랫폼의 개념을 중합체 연구라는 특정 재료과학 분야에 적용하는 사례입니다.
- 🏛 기반 연구: [[papers/014_A_multimodal_generative_AI_copilot_for_human_pathology/review]] — 범용 생물의학 AI 에이전트로 병리학 특화 AI 어시스턴트 개발의 기술적 기반을 제공한다.
- 🏛 기반 연구: [[papers/359_From_large_language_models_to_multimodal_ai_A_scoping_review/review]] — 범용 생의학 AI 에이전트가 의료 멀티모달 AI 발전의 기술적 기반을 제공한다
- 🔄 다른 접근: [[papers/151_Benchmarking_ai_scientists_in_omics_data-driven_biological_r/review]] — 생물의학 AI의 성능 평가라는 동일한 목표를 다른 접근법(벤치마크 vs 통합 에이전트)으로 달성합니다.
- 🏛 기반 연구: [[papers/260_DeepCRE_Transforming_Drug_RD_via_AI-Driven_Cross-drug_Respon/review]] — 통합된 생의학 AI 에이전트 환경에서 약물 반응 예측이 핵심 구성요소로 활용될 수 있습니다.
- 🔄 다른 접근: [[papers/626_Polymer_Brushes_and_Grafted_Polymers_AIML-Driven_Synthesis_S/review]] — 자율 실험실 개념을 생의학과 재료과학이라는 서로 다른 연구 분야에 적용하는 학제간 접근입니다.
- 🏛 기반 연구: [[papers/612_PersonaAI_An_Interactive_Agentic-AI_Framework_for_Autonomous/review]] — 범용 생의학 AI 에이전트가 노화 연구의 복잡성을 다루는 PersonaAI 프레임워크의 기술적 기반을 제공합니다.
- 🏛 기반 연구: [[papers/839_Transforming_Behavioral_Neuroscience_Discovery_with_In-Conte/review]] — 생명의학 분야의 일반적인 AI 에이전트 프레임워크를 신경과학 특화 도구로 응용할 수 있다.
- 🔗 후속 연구: [[papers/055_Advancing_multimodal_medical_capabilities_of_gemini/review]] — BiOMNI의 일반 목적 생의학 AI 에이전트가 Med-Gemini의 특화된 의료 멀티모달 능력을 더 광범위한 생의학 영역으로 확장함
- 🔄 다른 접근: [[papers/226_ClinicalGPT_Large_Language_Models_Finetuned_with_Diverse_Med/review]] — 의료 특화 대규모 언어모델의 두 가지 다른 설계 철학을 비교하여 의료 AI의 범용성과 특화성 간의 균형점을 찾을 수 있다.
- 🏛 기반 연구: [[papers/027_A_survey_of_llm-based_agents_in_medicine_How_far_are_we_from/review]] — 의료 LLM 에이전트 연구는 BiomeMedLM과 같은 의료 특화 언어모델이 제공하는 도메인 지식 기반 위에 구축된 다중 에이전트 시스템을 분석합니다.
- 🏛 기반 연구: [[papers/357_From_intention_to_implementation_automating_biomedical_resea/review]] — 범용 바이오메디컬 AI 에이전트 Biomni는 BioResearcher의 모듈형 멀티 에이전트 아키텍처 설계에 기초 아이디어를 제공한다.
- 🔄 다른 접근: [[papers/774_STELLA_Towards_a_Biomedical_World_Model_with_Self-Evolving_M/review]] — STELLA와 Biomni 모두 범용 바이오의학 AI 에이전트를 추구하지만 자기진화형 vs 사전 훈련된 접근방식을 사용한다.
