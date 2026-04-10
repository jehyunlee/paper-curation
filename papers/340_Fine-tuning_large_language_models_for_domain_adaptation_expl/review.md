---
title: "340_Fine-tuning_large_language_models_for_domain_adaptation_expl"
authors:
  - "Wei Lu"
  - "Rachel K. Luu"
  - "Markus J. Buehler"
date: "2025.03"
doi: "10.1038/s41524-025-01564-y"
arxiv: ""
score: 4.3
essence: "본 논문은 재료과학 등 전문 도메인에 대응하는 대형언어모델(LLM)의 파인튜닝 전략을 체계적으로 탐구하며, 특히 여러 미세조정 모델의 병합(model merging)이 개별 모델의 능력을 초월하는 창발적 기능(emergent capabilities)을 생성할 수 있음을 실증한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Domain-adapted_Instruction_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Lu et al._2025_Fine-tuning large language models for domain adaptation exploration of training strategies, scaling.pdf"
---

# Fine-tuning large language models for domain adaptation: exploration of training strategies, scaling, model merging and synergistic capabilities

> **저자**: Wei Lu, Rachel K. Luu, Markus J. Buehler | **날짜**: 2025-03-28 | **DOI**: [10.1038/s41524-025-01564-y](https://doi.org/10.1038/s41524-025-01564-y)

---

## Essence

![Figure 2](figures/fig2.webp) *모델 훈련, 병합 및 평가 단계. A: 기존의 선형 훈련 파이프라인(CPT→SFT→DPO/ORPO). B: 모델 병합을 포함한 대안적 파이프라인*

본 논문은 재료과학 등 전문 도메인에 대응하는 대형언어모델(LLM)의 파인튜닝 전략을 체계적으로 탐구하며, 특히 여러 미세조정 모델의 병합(model merging)이 개별 모델의 능력을 초월하는 창발적 기능(emergent capabilities)을 생성할 수 있음을 실증한다.

## Motivation

- **Known**: LLM은 자연언어처리에서 강력한 능력을 보유하고 있으며, Llama, Mistral 등 오픈소스 아키텍처가 활발히 개발 중이다. 기존 LoRA(Low-Rank Adaptation) 같은 파인튜닝 기법이 존재한다.

- **Gap**: 도메인 적응(domain adaptation)을 위한 다양한 파인튜닝 전략(CPT, SFT, DPO, ORPO)의 상대적 효과에 대한 체계적 비교 데이터가 부족하며, 모델 병합의 메커니즘과 창발성에 대한 이해가 제한적이다.

- **Why**: 재료과학, 생물재료공학 등 전문 분야에서 LLM을 효과적으로 활용하려면 지식 습득과 선호도 정렬 간 균형을 맞춘 체계적 파인튜닝 전략이 필수적이다. 또한 모델 병합이 단순 집계가 아닌 창발적 기능을 생성할 수 있다면 이는 AI 시스템 개발의 새로운 도구가 될 수 있다.

- **Approach**: Continued Pretraining(CPT), Supervised Fine-Tuning(SFT), Direct Preference Optimization(DPO), Odds Ratio Preference Optimization(ORPO)을 조직적으로 비교하고, Spherical Linear Interpolation(SLERP) 기반 모델 병합의 효과를 다양한 모델 규모(8B, 7B, 1.7B 파라미터)에서 실험한다.

## Achievement

![Figure 4](figures/fig4.webp) *Llama-3.1 모델 변형체의 성능 평가*

![Figure 5](figures/fig5.webp) *Mistral-7B-v0.3 모델 변형체의 성능 평가*

1. **모델 병합의 창발성**: 여러 미세조정 모델의 SLERP 기반 병합이 개별 부모 모델의 능력을 단순 합산하지 않고, 매개변수 간의 비선형 상호작용을 통해 어느 부모 모델도 단독으로 달성하지 못한 새로운 기능을 생성하며, 도메인 특화 평가에서 개선된 성능을 달성함을 실증했다.

2. **훈련 전략의 체계적 비교**: CPT를 통한 도메인 지식 습득, SFT를 통한 작업 특화, DPO/ORPO를 통한 선호도 정렬의 순차적 파이프라인이 각 단계에서 모델 능력을 단계적으로 향상시키며, 다양한 모델 아키텍처(Llama 3.1 8B, Mistral 7B)에서 일관된 거동을 보임을 확인했다.

3. **스케일링과 창발성의 관계**: 모델 병합의 창발적 기능이 모델 규모에 의존적이며, 1.7B 파라미터의 소규모 LLM은 모델 병합 시 창발 기능을 나타내지 않아 모델 스케일이 핵심 요소임을 시사한다.

4. **개방형 대화 평가**: 인간-AI 모델 간의 자유로운 대화 평가에서 가장 작은 모델조차 추론 깊이, 창의성, 명확성, 정량적 정확성 등의 핵심 기준에서 높은 지능 점수를 달성할 수 있음을 보였다.

## How

![Figure 3](figures/fig3.webp) *SLERP(구면 선형 보간법)와 LERP(선형 보간법)의 비교. SLERP는 모델 매개변수 공간의 기하학적 구조를 보존하여 의미 있는 능력 혼합을 가능하게 함*

- **훈련 파이프라인 설계**: 베이스 모델 → CPT(도메인 특화 원시 텍스트, 추론/요약/증류 텍스트) → SFT(질답, 지시응답, 대화 쌍) → DPO/ORPO(양성/음성 예제 기반 선호도 최적화)로 구성된 순차적 단계 실행

- **SLERP 기반 모델 병합**: 선형 보간(LERP)과 달리, SLERP는 매개변수 공간의 구면 기하학을 보존하여 선형 결합으로 인한 손실을 피하고, 매개변수 간 각도 관계를 유지함으로써 의미 있고 응집력 있는 능력 혼합 실현

- **다중 모델 아키텍처 검증**: Llama 3.1 8B, Mistral 7B v0.3, 1.7B 파라미터 소규모 LLM을 포함한 다양한 모델 규모에서 일관성과 스케일링 효과 검토

- **평가 프레임워크**: 도메인 특화 벤치마크 평가 + 개방형 채팅 대화를 통한 정성적 평가 + 생물 재료 영감 디자인 개념 기반 이미지 생성 프롬프트 개발을 통한 다각적 능력 평가

## Originality

- **모델 병합의 비선형 창발성 체계적 분석**: 기존 연구는 모델 병합을 단순 집계로 이해했으나, 본 논문은 매개변수 간 비선형 상호작용이 창발적 기능을 생성함을 체계적으로 입증하고, 이러한 창발성의 조건(부모 모델 간 다양성, 파인튜닝 기법 선택, 모델 규모)을 규명했다.

- **도메인 적응 파인튜닝 전략의 통합적 비교**: CPT, SFT, DPO, ORPO를 연쇄적으로 적용하는 포괄적 파이프라인을 제시하고, 각 단계의 역할을 명확히 함으로써 재료과학 같은 전문 도메인에 최적화된 실증적 가이드라인 제공

- **SLERP를 통한 기하학적 구조 보존**: 컴퓨터 그래픽스에서 회전 보간용으로 개발된 SLERP를 LLM 병합에 응용하여 모델 매개변수 공간의 기하학적 특성을 수학적으로 보존하는 신규 접근법 시연

- **스케일링과 창발성의 명시적 연관성 제시**: 모델 규모(8B, 7B, 1.7B)에 따른 창발 기능의 차이를 실험으로 보여줌으로써, 향후 LLM 설계와 스케일링 전략에 대한 중요한 경험적 기초 제공

## Limitation & Further Study

- **한계**:
  - 모델 병합의 창발성이 명확한 이론적 프레임워크 없이 경험적 관찰에 의존하고 있으며, 어떤 매개변수 상호작용이 창발을 유도하는지에 대한 근본적 메커니즘 설명 부족
  - 1.7B 모델에서 창발 기능이 나타나지 않는 현상에 대해 정확한 임계값(critical threshold)을 규명하지 못함
  - 도메인 특화 평가가 주로 재료과학·생물재료공학에 집중되어, 다른 기술 도메인(의료, 화학, 제조 등)에서의 일반화 가능성이 미검증됨
  - 계산 비용과 훈련 시간에 대한 상세 분석이 제시되지 않아, 실무 적용 시 자원 요구사항 파악 어려움

- **후속 연구**:
  - 매개변수 수준의 상세 분석(activation patterns, attention mechanism visualization 등)을 통해 모델 병합 시 창발성의 수학적 근거 규명
  - 스케일링 법칙(scaling laws) 연구로 모델 규모와 창발 기능 간의 정량적 관계 도출
  - 다양한 도메인(생명과학, 제조, 금융 등)에서의 파인튜닝 전략 적용 및 일반화 가능성 검증
  - 모델 병합 시 부모 모델의 최적 조합 선택을 위한 사전 예측 지표 개발
  - 더 작은 모델에서 창발 기능을 유발할 수 있는 조건(특정 데이터셋, 병합 비율, 사전학습 방식 등) 탐색


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.3/5

**총평**: 본 논문은 모델 병합을 통한 창발적 기능의 실증과 도메인 특화 파인튜닝 전략의 체계적 비교를 제시하여 LLM 활용의 새로운 가능성을 제시하는 가치 있는 연구이나, 창발성의 근본 메커니즘 분석과 이론적 기초가 강화되면 더욱 영향력 있는 기여가 될 수 있다.

## Related Papers

- 🔗 후속 연구: [[papers/707_SciBERT_A_Pretrained_Language_Model_for_Scientific_Text/review]] — SciBERT의 단일 도메인 특화를 여러 모델 병합으로 확장하여 창발적 기능 생성
- 🧪 응용 사례: [[papers/522_MatPilot_an_LLM-enabled_AI_Materials_Scientist_under_the_Fra/review]] — 재료과학 도메인 적응 연구가 MatPilot 같은 재료과학 특화 LLM 개발에 직접 적용
- 🏛 기반 연구: [[papers/287_Dont_Stop_Pretraining_Adapt_Language_Models_to_Domains_and_T/review]] — 도메인 적응의 기본 원리가 과학 분야 LLM 개발의 핵심 방법론이 됨
- 🧪 응용 사례: [[papers/523_MatterChat_A_Multi-Modal_LLM_for_Material_Science/review]] — 재료과학 도메인 파인튜닝 전략이 MatterChat 같은 멀티모달 재료과학 LLM에 활용
- 🔗 후속 연구: [[papers/287_Dont_Stop_Pretraining_Adapt_Language_Models_to_Domains_and_T/review]] — 도메인 적응을 과학 분야로 확장한 구체적 사례와 실험을 제공한다.
- 🏛 기반 연구: [[papers/690_Rule-based_neural_and_llm_back-translation_Comparative_insig/review]] — 도메인 적응을 위한 대규모 언어 모델 파인튜닝 경험이 저자원 언어 번역 모델 선택에 유용한 통찰을 제공한다.
