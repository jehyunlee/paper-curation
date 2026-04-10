---
title: "529_MedAgents_Large_Language_Models_as_Collaborators_for_Zero-sh"
authors:
  - "Xiangru Tang"
  - "Anni Zou"
  - "Zhuosheng Zhang"
  - "Ziming Li"
  - "Yilun Zhao"
date: "2023.11"
doi: "N/A"
arxiv: ""
score: 4.3
essence: "대규모 언어 모델(LLM)의 의료 추론 능력을 향상시키기 위해 다학제 협력 프레임워크를 제안하며, 역할 놀이와 반복적 토론을 통해 훈련 없이도 의료 지식을 효과적으로 활용한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Clinical_Multi-Agent_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Tang et al._2023_MedAgents Large Language Models as Collaborators for Zero-shot Medical Reasoning.pdf"
---

# MedAgents: Large Language Models as Collaborators for Zero-shot Medical Reasoning

> **저자**: Xiangru Tang, Anni Zou, Zhuosheng Zhang, Ziming Li, Yilun Zhao, Xingyao Zhang, Arman Cohan, Mark Gerstein | **날짜**: 2023-11-16 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) *MedAgents 프레임워크의 5단계 파이프라인: 전문가 수집, 분석 제안, 보고서 요약, 협력 협의, 의사결정*

대규모 언어 모델(LLM)의 의료 추론 능력을 향상시키기 위해 다학제 협력 프레임워크를 제안하며, 역할 놀이와 반복적 토론을 통해 훈련 없이도 의료 지식을 효과적으로 활용한다.

## Motivation

- **Known**: LLM은 일반 도메인에서는 우수한 성능을 보이지만, 의료 분야에서는 상대적으로 제한적이다. 기존 프롬프팅 방법(CoT, Self-Consistency)은 의료 분야에서 환각(hallucination) 문제를 야기한다.

- **Gap**: 의료 분야의 두 가지 핵심 도전: (i) 의료 훈련 데이터의 부족 및 일반 데이터에 비한 낮은 특이성, (ii) 의료 지식과 추론 능력을 프롬프팅만으로는 효과적으로 이끌어내기 어려움.

- **Why**: 다중 에이전트 협력 방식이 각 LLM 내에 내재된 전문 지식을 효과적으로 드러낼 수 있음을 최근 연구가 보여준다.

- **Approach**: 의료 질문의 다학제 관점을 반영하는 여러 도메인 전문가 에이전트가 역할 놀이를 통해 반복적으로 토론하고 합의에 도달하는 프레임워크 제안.

## Achievement

![Figure 2](figures/fig2.webp) *MedAgents의 실제 적용 예시: VSD 진단 사례에서 소아과, 심장학, 유전학 등 여러 전문가 에이전트가 참여하여 최종 일치 보고서 생성*

1. **평가 성능**: 9개 데이터셋(MedQA, MedMCQA, PubMedQA, MMLU의 6개 의료 서브태스크)에서 CoT 및 Self-Consistency 프롬프팅 방법을 초과 달성. 특히 zero-shot 설정에서 5-shot 기준선보다 우수한 성능 기록.

2. **해석 가능성 및 신뢰도**: 역할 놀이와 협력 토론을 통해 모델의 추론 과정이 명시적이고 검증 가능해지며, RAG(Retrieval Augmented Generation) 없이도 정확한 의료 지식 활용 가능 증명.

3. **실무 적용성**: 훈련이 필요 없는 플러그 앤 플레이 방식으로 Med-PaLM 2 등 기존 의료 LLM을 보완할 수 있음.

## How

![Figure 3](figures/fig3.webp) *전문가 에이전트 수의 영향 분석*

**5단계 프레임워크:**

- **①Expert Gathering (전문가 수집)**: 주어진 의료 질문과 선택지에 기반하여 질문 도메인 전문가(QD)와 선택지 도메인 전문가(OD)를 체계적으로 모집. 역할 프롬프트를 통해 LLM이 특정 의료 분야 전문가 역할 수행.

- **②Analysis Proposition (분석 제안)**: 각 도메인 전문가가 질문 분석(QA)과 선택지 분석(OA)을 독립적으로 생성. 선택지 분석 시 질문 분석 결과를 참고하여 상호 연관성 고려.

- **③Report Summarization (보고서 요약)**: 모든 도메인 전문가의 분석을 의료 보고서 작성 보조역이 종합하여 핵심 지식(Key Knowledge)과 총체적 분석(Total Analysis)을 추출한 예비 보고서 생성.

- **④Collaborative Consultation (협력 협의)**: 전문가들이 예비 보고서에 대해 동의/불동의를 표현하며 반복적으로 토론. 모든 전문가의 승인을 얻을 때까지 보고서 반복 수정으로 합의 도출.

- **⑤Decision Making (의사결정)**: 합의된 최종 보고서(Unanimous Report)로부터 최종 답변 도출.

**핵심 메커니즘**:
- 각 단계가 LLM 함수 호출로 구성되며, 시스템 역할(role)과 가이드라인 프롬프트를 활용한 명시적 지시
- 반복적 협의를 통한 자체 수정 메커니즘으로 오류 감소

## Originality

- **최초성**: 의료 분야에서 다중 에이전트 협력 프레임워크를 처음으로 도입하고, 의료 질문 답변에서 합의 기반 협력 메커니즘의 효과를 최초 입증.

- **차별성**: 기존 다중 에이전트 방식과 달리, 의료 분야의 다학제 특성을 명시적으로 모델링하여 질문 도메인과 선택지 도메인을 분리한 접근.

- **실용성**: 훈련 없는 zero-shot 설정으로 실제 의료 현장 적용 가능성 제고. RAG 없이 LLM 내 암묵적 지식만으로 작동.

- **투명성**: 각 단계의 명시적 논리 구조와 역할 프롬프팅으로 "왜 이 답인가"를 추적 가능하게 함.

## Limitation & Further Study

![Figure 4, 5](figures/fig4.webp) *오류 분석: 도메인 지식 부족, 지식 오인출, 일관성 오류, CoT 오류의 4가지 주요 카테고리*

- **한계 1 - 도메인 지식 부족**: LLM이 특정 의료 지식을 훈련 데이터에서 충분히 습득하지 못한 경우 협력도 근본적으로 제한적. 의료 특화 파인튜닝의 필요성 남음.

- **한계 2 - 지식 오인출**: 모델이 의료 지식을 소유하고 있어도 프롬프팅에 따라 부정확한 지식을 활용하거나 혼동하는 경우 발생.

- **한계 3 - 계산 비용**: 각 단계마다 다수의 LLM 호출이 필요하여 계산 비용 상당. 에이전트 수의 영향 분석 필요.

- **한계 4 - 합의 메커니즘의 한계**: 모든 전문가가 동의하면서도 집단적으로 잘못된 결론에 도달할 가능성(집단 환각).

- **후속 연구 방향**: 
  - 검색 보강 생성(RAG)과의 결합을 통한 지식 정확성 향상
  - 의료 특화 미세조정(domain-specific fine-tuning)과의 조합
  - 도메인 지식 부족과 오인출 오류 감소를 위한 표적화된 개선
  - 계산 효율성 최적화

## Evaluation

- **Novelty (참신성)**: 4.5/5 - 의료 분야 다중 에이전트 협력의 처음 적용이나, 일반 다중 에이전트 개념의 응용

- **Technical Soundness (기술 건전성)**: 4/5 - 방법론이 명확하고 실험 설계는 적절하나, 오류 분석에서 근본적 한계점이 노출됨

- **Significance (중요도)**: 4.5/5 - 의료 AI의 실무 적용성을 크게 향상시킬 수 있는 실용적 방법론. 9개 데이터셋에서 일관된 개선 입증

- **Clarity (명확성)**: 4.5/5 - 5단계 프레임워크가 논리적이며 Figure 예시가 직관적. 다만 프롬프트 상세 내용이 부록에만 제시

- **Overall (종합)**: 4.3/5

**총평**: MedAgents는 의료 분야에서 LLM의 잠재된 지식을 효과적으로 활용하는 창의적인 다학제 협력 프레임워크로, 훈련 없는 zero-shot 설정에서 실질적인 성능 개선을 달성하였다. 다만 도메인 지식 부족 및 환각 문제의 근본적 해결과 계산 효율성 개선이 추가 과제이다.

## Related Papers

- 🔗 후속 연구: [[papers/014_A_multimodal_generative_AI_copilot_for_human_pathology/review]] — 제로샷 의료 진단을 위한 다중 에이전트 협업으로 PathChat의 병리학 전문 기능을 확장한다.
- 🔗 후속 연구: [[papers/244_Cross_sectional_pilot_study_on_clinical_review_generation_us/review]] — 제로샷 협업을 위한 의료 에이전트들이 임상 리뷰 생성을 다중 에이전트 협업으로 확장한다.
- 🏛 기반 연구: [[papers/189_CASSIA_a_multi-agent_large_language_model_for_reference_free/review]] — 의료 분야 다중 에이전트 협력이 생물학적 데이터 분석의 기반이 됨
- 🔄 다른 접근: [[papers/311_Empowering_Biomedical_Discovery_with_AI_Agents/review]] — 생의학 발견 vs 의료 진단에서 서로 다른 생의학 AI 에이전트 응용 영역
- 🔗 후속 연구: [[papers/163_Biodsa-1k_Benchmarking_data_science_agents_for_biomedical_re/review]] — 다중 에이전트 의료 협업을 생의학 연구 가설 검증 시나리오에 적용한 확장 연구다
- 🔗 후속 연구: [[papers/413_Human-ai_teaming_using_large_language_models_Boosting_brain-/review]] — MedAgents의 제로샷 의료 협력이 ChatBCI의 뇌-컴퓨터 인터페이스 연구에서 인간-AI 협력 방식을 확장함
- 🏛 기반 연구: [[papers/068_AgentMD_Empowering_Language_Agents_for_Risk_Prediction_with/review]] — MedAgents의 제로샷 의료 협력 방법론이 AgentMD의 임상 계산기 자동 큐레이션과 환자 기록 적용에 기반을 제공함
- 🔄 다른 접근: [[papers/160_BioAgents_Democratizing_Bioinformatics_Analysis_with_Multi-A/review]] — 생물정보학 분야에서 소형 언어모델 기반과 대형 언어모델 기반의 다중 에이전트 시스템 접근법을 비교하여 각각의 장단점을 분석할 수 있다.
- 🔄 다른 접근: [[papers/225_Clinicalgpt-r1_Pushing_reasoning_capability_of_generalist_di/review]] — 의료 진단에서 단일 모델과 다중 에이전트 시스템의 서로 다른 접근 방식을 비교하여 임상 환경에 최적화된 솔루션을 찾을 수 있다.
- 🔄 다른 접근: [[papers/027_A_survey_of_llm-based_agents_in_medicine_How_far_are_we_from/review]] — 의료 LLM 에이전트 서베이와 MedAgents는 모두 의료 AI 에이전트를 다루지만, 포괄적 현황 분석과 제로샷 의료 진단이라는 서로 다른 관점을 제시합니다.
- 🔗 후속 연구: [[papers/663_Reinforcing_clinical_decision_support_through_multi-agent_sy/review]] — 제로샷 의료 분류를 위한 LLM 기반 다중 에이전트로 의료 AI 협력을 확장한다.
