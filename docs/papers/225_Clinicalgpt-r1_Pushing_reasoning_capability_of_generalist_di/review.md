---
title: "225_Clinicalgpt-r1_Pushing_reasoning_capability_of_generalist_di"
authors:
  - "Wuyang Lan"
  - "Wenzheng Wang"
  - "Changwei Ji"
  - "Guoxing Yang"
  - "Yongbo Zhang"
date: "2025"
doi: "N/A"
arxiv: ""
score: 3.5
essence: "본 논문은 실제 임상 기록을 기반으로 한 20,000개의 임상 데이터셋에서 학습하여, 질병 진단에서 추론 능력을 강화한 의료 특화 대규모 언어모델(LLM) ClinicalGPT-R1을 제시한다. 지도학습 미세조정(SFT)과 강화학습(RL)의 두 단계 학습을 통해 진단 추론 능력을 향상시키며, 중국어 진단 작업에서 GPT-4o를 능가하는 성능을 달성한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Biomedical_Causal_Modeling"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhuang et al._2025_Clinicalgpt-r1 Pushing reasoning capability of generalist disease diagnosis with large language mod.pdf"
---

# ClinicalGPT-R1: Pushing reasoning capability of generalist disease diagnosis with large language model

> **저자**: Wuyang Lan, Wenzheng Wang, Changwei Ji, Guoxing Yang, Yongbo Zhang, Xiaohong Liu, Song Wu, Guangyu Wang | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: 합성 데이터 생성 파이프라인*

본 논문은 실제 임상 기록을 기반으로 한 20,000개의 임상 데이터셋에서 학습하여, 질병 진단에서 추론 능력을 강화한 의료 특화 대규모 언어모델(LLM) ClinicalGPT-R1을 제시한다. 지도학습 미세조정(SFT)과 강화학습(RL)의 두 단계 학습을 통해 진단 추론 능력을 향상시키며, 중국어 진단 작업에서 GPT-4o를 능가하는 성능을 달성한다.

## Motivation

- **Known**: OpenAI-o1, DeepSeek-R1 등의 최신 LLM이 수학, 프로그래밍 등의 분야에서 우수한 추론 능력을 보여줌. 일반 도메인에서는 확장된 사고의 연쇄(Chain-of-Thought, CoT) 프롬프팅과 강화학습이 모델 추론을 향상시키는 데 효과적임이 입증됨.

- **Gap**: 의료 영역에서 LLM의 추론 과정을 검증하는 것이 어려움. 수학이나 프로그래밍과 달리, 실제 임상 진단은 명확한 중간 단계나 검증 가능한 피드백이 부족함. 다지선다형 데이터셋(예: MedQA)은 실제 임상 진단 워크플로우의 복잡성을 포착하지 못함.

- **Why**: 정확한 진단과 치료를 위해 임상 환경에서는 견고한 장형식 추론이 필수적이며, 의료 응용에서 추론 기능이 강화된 LLM의 개발과 평가가 매우 중요함.

- **Approach**: 실제 임상 기록을 기반으로 한 임상 진단 데이터셋을 구축하고, 탐색 전략(탐험, 역추적, 검증, 수정)을 포함한 다양한 합성 데이터 생성 기법을 적용한 후, SFT와 RL의 두 단계 훈련을 통해 모델의 추론 능력을 개선함.

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: 서로 다른 훈련 방법에 따른 ClinicalGPT-R1 성능 비교 (SFT vs SFT+RL)*

![Figure 3](figures/fig3.webp)
*그림 3: 서로 다른 훈련 데이터 소스에 따른 ClinicalGPT-R1 성능 비교*

1. **성과 1 - 중국어 진단 우수성**: ClinicalGPT-R1은 중국어 진단 작업에서 GPT-4o를 능가하는 성능 달성. 7개 의료 부서 전반에서 평균 정확도 향상 입증.

2. **성과 2 - 두 단계 훈련의 효과성**: SFT+RL 조합 훈련이 SFT 단독 훈련보다 우수한 성능을 달성. 강화학습 단계를 통한 추론 최적화의 효과 입증 (그림 2).

3. **성과 3 - 데이터 합성 전략의 유효성**: GPT-4o-mini로 생성한 합성 데이터가 DeepSeek-v3-0324로 생성한 데이터보다 더 높은 진단 성능 달성 (그림 3, 평균 정확도 20.4% vs 22.4%).

4. **성과 4 - 벤치마크 구축**: 7개 주요 의료 부서(호흡기계, 위장관계, 비뇨기계, 심혈관계, 면역학, 신경학, 내분비학)를 포괄한 3,500개 샘플의 도전적 평가 벤치마크 MedBench-Hard 구축.

## How

![Figure 1](figures/fig1.webp)
*그림 1: 임상 기록 기반 합성 데이터 생성 파이프라인 상세도*

**의료 데이터 구축:**
- MedDX-FT와 익명화된 전자의료기록(EHR)으로부터 실제 임상 데이터 수집
- 상태 기반 LLM(GPT-4o-mini, DeepSeek-v3-0324)을 데이터 생성기로 활용하여 합성 데이터 생성
- 탐색 전략(Exploring New Paths, Backtracking, Verification, Corrections) 적용으로 최대 3회 시도, 실패 시 정답 제시로 추론 경로 생성

**장형 추론(Long CoT) 생성:**
- 추론 궤적을 응집력 있는 자연언어 형식으로 재구성
- 완화 표현("hmm", "also", "wait" 등) 포함으로 토큰 사용량 감소

**두 단계 학습:**
1. **지도학습 미세조정(SFT)**: 질문, 추론 과정(thinking), 최종 응답으로 구성된 명령어 튜닝 데이터셋 활용
2. **강화학습(RL)**: 정책 근처 최적화(Proximal Policy Optimization, PPO) 알고리즘 활용하여 장기 추론 능력 최적화

**보상 설계:**
- 결과 기반 보상: 명확한 추론 과정 + 정확한 응답 = 1.0, 정확한 응답 (추론 과정 없음) = 0.1, 응답 없음 = 0
- 대규모 모델 검증기를 통해 정량적 피드백 생성

## Originality

- **의료 특화 추론 LLM**: 일반 도메인의 추론 기법을 의료 진단에 체계적으로 적용한 첫 시도. 실제 임상 기록 기반의 장형 추론 데이터 구축으로 진정한 의료 추론 학습 실현.

- **적응형 합성 데이터 생성**: 실패 시 역추적, 검증, 수정 등 4가지 탐색 전략을 순차적으로 적용하는 동적 파이프라인 개발로 높은 품질의 합성 데이터 생성.

- **이중 언어 성능 검증**: 중국어와 영어 모두에서 성능을 체계적으로 비교함으로써 다언어 의료 AI의 가능성 제시.

- **도전적 평가 벤치마크**: ICD-10 기반의 층화 표본추출로 7개 의료 부서의 다양한 질병(희귀질환 포함)을 포괄하는 MedBench-Hard 구축.

## Limitation & Further Study

**한계:**
- 평가가 제한적임: 논문에서 제시된 성능 수치가 절대적으로 낮음(평균 20-22% 정확도). 이는 진단 작업의 난이도 반영이나 평가 메트릭의 엄격성을 시사.

- 기반 모델 의존성: Qwen-2.5-7B-Instruct만 사용하여 다양한 기반 모델에 대한 일반화 가능성 미검증.

- 보상 모델의 단순성: 결과 기반 보상만 사용하며, 추론 과정 자체의 의료적 타당성을 평가하지 못함.

- 언어 간 성능 격차: 중국어에서는 GPT-4o 능가, 영어에서는 동등 수준으로 성능 차이 존재하는 원인 분석 부족.

**후속 연구 방향:**
- 프로세스 감독(process supervision) 보상 모델 개발으로 중간 추론 단계의 의료적 타당성 평가
- 더 큰 규모의 의료 기록 데이터 수집으로 절대 성능 향상
- 임상의 검증을 통한 실제 의료 현장에서의 적용성 평가
- 다양한 기반 모델(Llama, Mistral 등)에 대한 호환성 확장
- 진단 근거 제시(explainability) 및 불확실성 정량화 기능 추가


## Evaluation

- Novelty: 3.5/5
- Technical Soundness: 3.5/5
- Significance: 3/5
- Clarity: 3.5/5
- Overall: 3.5/5

**총평**: ClinicalGPT-R1은 일반 도메인의 추론 기법을 의료에 체계적으로 적용하고 실제 임상 기록 기반의 데이터셋을 활용한 점에서 창의적이나, 절대 성능 수치의 낮음과 평가의 제한성, 그리고 중국어 중심의 성과로 인해 일반적 임상 응용성이 아직 미흡하다. 의료 AI 분야에서 추론 강화의 중요성을 보여주는 선도적 연구이나, 실용화를 위해서는 더욱 강력한 성능 개선과 임상 타당성 검증이 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/226_ClinicalGPT_Large_Language_Models_Finetuned_with_Diverse_Med/review]] — ClinicalGPT의 기본 의료 언어모델 구조가 추론 능력 강화를 위한 ClinicalGPT-R1의 기술적 기반을 제공한다.
- 🔄 다른 접근: [[papers/529_MedAgents_Large_Language_Models_as_Collaborators_for_Zero-sh/review]] — 의료 진단에서 단일 모델과 다중 에이전트 시스템의 서로 다른 접근 방식을 비교하여 임상 환경에 최적화된 솔루션을 찾을 수 있다.
- 🧪 응용 사례: [[papers/507_Llmeval-med_A_real-world_clinical_benchmark_for_medical_llms/review]] — ClinicalGPT-R1의 진단 추론 능력을 실제 임상 벤치마크에 적용하여 의료 LLM의 실용성을 검증할 수 있다.
- 🏛 기반 연구: [[papers/507_Llmeval-med_A_real-world_clinical_benchmark_for_medical_llms/review]] — 의료 분야 LLM의 추론 능력 개발 연구로 LLMEval-Med의 평가 기준 설계에 참고가 된다.
- 🔄 다른 접근: [[papers/244_Cross_sectional_pilot_study_on_clinical_review_generation_us/review]] — 임상 분야 특화 GPT 모델이 일반 LLM과 다른 임상 리뷰 생성 접근법을 보여준다.
- 🧪 응용 사례: [[papers/006_A_deep_subgrouping_framework_for_precision_drug_repurposing/review]] — 다양한 의료 데이터로 파인튜닝된 ClinicalGPT-R1은 STEDR의 정밀 약물 재창출 프레임워크가 실제 임상에 적용된 사례입니다
- 🧪 응용 사례: [[papers/359_From_large_language_models_to_multimodal_ai_A_scoping_review/review]] — 생성형 AI의 임상 추론 능력을 의료 분야 멀티모달 시스템 발전의 실제 사례로 보여준다
- 🔗 후속 연구: [[papers/848_TxAgent_An_AI_Agent_for_Therapeutic_Reasoning_Across_a_Unive/review]] — 임상 추론을 위한 생성형 AI를 정밀 치료를 위한 다도구 AI 에이전트로 확장할 수 있다
- 🧪 응용 사례: [[papers/163_Biodsa-1k_Benchmarking_data_science_agents_for_biomedical_re/review]] — 임상 추론 능력을 생의학 데이터 과학 가설 검증에 적용할 수 있다
