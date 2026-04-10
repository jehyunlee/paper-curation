---
title: "158_Biasfilter_An_inference-time_debiasing_framework_for_large_l"
authors:
  - "Xiaoqing Cheng"
  - "Ruizhe Chen"
  - "Hongying Zan"
  - "Yuxiang Jia"
  - "Min Peng"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "BiasFilter는 추론 시간(inference-time)에 대규모 언어모델(LLM)의 사회적 편향을 완화하는 모델-무관적(model-agnostic) 프레임워크로, 모델 재학습이나 파인튜닝 없이 생성 과정 중 실시간으로 편향 출력을 필터링하는 방식을 제시한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Self-improving_Reward_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Cheng et al._2025_Biasfilter An inference-time debiasing framework for large language models.pdf"
---

# BiasFilter: An inference-time debiasing framework for large language models

> **저자**: Xiaoqing Cheng, Ruizhe Chen, Hongying Zan, Yuxiang Jia, Min Peng | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*BiasFilter의 개요: 베이스 모델과 통합되어 생성 과정 중 공정성을 주기적으로 평가하고, 편향된 출력을 필터링하는 메커니즘*

BiasFilter는 추론 시간(inference-time)에 대규모 언어모델(LLM)의 사회적 편향을 완화하는 모델-무관적(model-agnostic) 프레임워크로, 모델 재학습이나 파인튜닝 없이 생성 과정 중 실시간으로 편향 출력을 필터링하는 방식을 제시한다.

## Motivation

- **Known**: 기존의 편향 완화 방법은 프롬프트 기반(prompt-based) 또는 파인튜닝 기반(fine-tuning-based)으로 분류되며, 전자는 세밀한 제어가 어렵고 후자는 높은 계산 비용과 데이터 필요성 문제를 가짐

- **Gap**: 오픈소스 LLM뿐만 아니라 API 기반 블랙박스 모델(GPT 등)에 적용 가능하면서도 계산 효율적인 추론시간 편향 완화 방법이 부재

- **Why**: LLM이 생성하는 편향 콘텐츠는 소수 집단의 표현을 왜곡하고 사회적 고정관념을 강화하여 실제 피해를 야기하므로, 실용적이고 확장 가능한 해결책이 필요

- **Approach**: 공정성 선호도 데이터셋을 구축하고 토큰 수준의 보상 모델(reward model)을 학습하여, 생성 과정 중 후보 세그먼트들을 주기적으로 평가하고 저점수 세그먼트를 제거하는 방식으로 공정성 강제

## Achievement

![Figure 2](figures/fig2.webp)
*공정성 선호도 데이터셋 구축 과정: HolisticBias 소스 데이터셋에서 프롬프트 샘플링, 다중 모델 응답 생성, GPT-4 및 인간 검증을 통한 다단계 주석*

1. **효과적인 편향 완화**: 연령, 성별, 인종, 종교 관련 사회적 편향을 광범위한 LLM(LLaMA, Mistral, Qwen, GPT-3.5-Turbo, GPT-4o)에서 체계적으로 완화하며, 6개의 경쟁 방법을 모두 능가

2. **생성 품질 보존**: 텍스트 유창성(fluency)과 다양성(diversity)을 유지하거나 오히려 개선, 단일 및 다중 턴 시나리오에서 일관된 성능 (CEB, FairMT 벤치마크 활용)

3. **실용성과 확장성**: 모델-무관적 설계로 오픈소스와 API 기반 모델 모두에 적용 가능하며, 계산 비용과 편향 완화 효과 간의 균형 달성

## How

![Figure 3](figures/fig3.webp)
*BiasFilter 프레임워크: 공정성 보상 모델을 통해 베이스 모델의 중간 생성물을 평가하고, 저점수 후보를 필터링하며, 공정한 출력을 계속 생성하는 과정*

- **공정성 선호도 데이터셋 구성** (4,195개 선호도 쌍):
  - HolisticBias에서 3,000개 프롬프트 샘플링 (4가지 인구통계학적 속성: 종교, 성별, 연령, 인종)
  - 5개 모델(Llama-2-70b, Llama-3-8b, Mistral-7B, GPT-3.5-Turbo, GPT-4)로 각 프롬프트마다 5개 응답 생성
  - GPT-4 기반 자동 평가 후 점수 차이 15 이상인 선호도 쌍만 인간 검증으로 정제

- **토큰 수준 보상 모델 학습**:
  - DPO(Direct Preference Optimization) 손실함수를 활용하여 참조 정책(πref)과 대상 정책(π) 간 로그 확률 비율 최대화
  - 공정성 점수를 직접 생성

- **추론시간 디코딩 알고리즘**:
  - 생성을 K개의 세그먼트로 분할 (세그먼트 길이 l)
  - 각 단계마다 활성 세트의 모든 부분 생성물(y_{1:k})에서 Nchildren개의 자식 세그먼트 생성
  - 보상 모델로 모든 후보 세그먼트 점수 매김
  - 상위 N개 세그먼트만 유지하고 나머지 제거 (beam search 개념과 유사하나 공정성 기준 적용)
  - 최종 출력은 전체 경로 중 최고 점수 선택

- **효율성 최적화**:
  - API 기반 모델에 대해서는 별도 출력 수정 불필요 (부분 생성 지원 안 되는 경우)
  - 고정된 간격에서만 평가 → 계산 오버헤드 최소화

## Originality

- **토큰 수준 공정성 평가**: 기존 대부분 방법이 전체 생성물 수준에서만 평가하는 반면, BiasFilter는 생성 과정 중 토큰 수준에서 실시간 공정성 제어

- **모델-무관적 설계**: 파인튜닝이나 모델 파라미터 수정 없이 추론시간에만 작동하므로, API 기반 블랙박스 모델에 즉시 적용 가능

- **실용적 데이터셋**: 다양한 베이스 모델과 인간-GPT-4 협력 주석을 통해 고품질 공정성 선호도 데이터셋 구축 및 공개

- **다층적 필터링**: 생성 과정 중 부분 출력 수준에서 편향을 점진적으로 제거함으로써, 초기 단계의 편향이 최종 출력에 축적되는 것을 방지

## Limitation & Further Study

- **계산 비용**: K × Nchildren번의 추가 전방 패스(forward pass) 필요로, 매우 큰 모델의 경우 여전히 실시간 적용에 제약. 세그먼트 크기와 후보 수 튜닝의 자동화 방법 부재

- **보상 모델의 일반화**: 특정 4가지 속성(종교, 성별, 연령, 인종)에 한정되어 학습된 보상 모델이, 학습되지 않은 다른 형태의 편향(문화적, 지역적)에 대한 효과성이 불명확

- **생성 다양성 트레이드오프**: 상위 N개 세그먼트만 유지하는 방식이 생성 경로를 제한할 수 있으며, 창의적인 텍스트 생성 작업에서의 영향 미측정

- **다국어 및 도메인 특수성**: 영어 중심으로 평가되었으며, 다른 언어나 전문 도메인(의료, 법률)에서의 성능 미검증

- **후속 연구 방향**:
  - 더 가벼운 보상 모델 설계로 계산 오버헤드 감소
  - 다양한 편향 유형에 대한 다목적 보상 모델 학습
  - 생성 다양성을 보존하는 샘플링 전략 개선
  - 다국어 및 도메인 특수 데이터셋 확장

## Evaluation

- **Novelty**: 4/5
  - 추론시간 편향 완화 자체는 새로운 개념은 아니나, 토큰 수준의 세밀한 공정성 제어와 모델-무관적 설계는 실질적 기여. 다만 기본 아이디어(beam search + reward filtering)는 기존 기법의 응용

- **Technical Soundness**: 4/5
  - DPO 기반 보상 모델 학습과 다단계 필터링 알고리즘이 명확하고 체계적. 데이터셋 구축 과정이 철저함. 다만 일부 하이퍼파라미터(세그먼트 길이, 후보 수) 선정 근거가 제한적

- **Significance**: 4/5
  - 실무적 중요성이 높음: API 기반 모델 적용 가능, 계산 비용 합리적, 다양한 LLM 검증. 하지만 특정 4가지 속성에 한정된 평가, 장문 생성(long-form)에서 효과성 미증명

- **Clarity**: 4.5/5
  - 논문 구조가 명확하고 Figure들이 직관적. 알고리즘이 상세히 제시됨. 다만 일부 실험 설정(세그먼트 크기, 후보 수 선택 기준) 설명 불충분

- **Overall**: 4/5

**총평**: BiasFilter는 추론시간에 작동하는 모델-무관적 편향 완화 프레임워크로서, 실무적 적용성이 높고 광범위한 실험을 통해 유효성을 입증했다. 특히 API 기반 모델에도 적용 가능한 점과 생성 품질 보존은 장점이나, 계산 비용 추가, 특정 속성에 한정된 학습, 다양한 편향 유형에 대한 확장성 제약은 보완 필요 영역이다.

## Related Papers

- 🧪 응용 사례: [[papers/245_Crosslingual_capabilities_and_knowledge_barriers_in_multilin/review]] — 다국어 LLM의 교차언어 편향 문제를 추론 시간에 실시간으로 완화하는 응용
- 🏛 기반 연구: [[papers/1127_MMSD20_Towards_a_Reliable_Multi-modal_Sarcasm_Detection_Syst/review]] — 멀티모달 풍자 탐지에서 허위 신호 제거를 위한 편향 완화 기법의 기반
- 🔗 후속 연구: [[papers/435_Interfeedback_Unveiling_interactive_intelligence_of_large_mu/review]] — 인간 피드백 기반 개선을 편향 제거라는 구체적 목표로 특화한 확장
- 🧪 응용 사례: [[papers/846_TrustLLM_Trustworthiness_in_Large_Language_Models/review]] — LLM 신뢰성 향상을 위해 추론 시간 편향 완화 기법을 체계적으로 적용
- 🧪 응용 사례: [[papers/245_Crosslingual_capabilities_and_knowledge_barriers_in_multilin/review]] — 다국어 LLM의 편향 완화를 위해 BiasFilter와 같은 추론 시간 편향 제거 기법 적용 가능
- 🔄 다른 접근: [[papers/148_Axolotl_fairness_through_assisted_self-debiasing_of_large_la/review]] — 둘 다 LLM의 편향 완화를 다루지만 하나는 사후처리 자체 편향 제거에, 다른 하나는 추론 시점 편향 필터링에 초점을 맞춘다.
- 🏛 기반 연구: [[papers/755_Simalign_High_quality_word_alignments_without_parallel_train/review]] — 다국어 임베딩의 편향 문제를 다루는 BiasFilter와 SimAlign의 크로스링구얼 정렬 방법론이 상호 보완적 관계에 있음
- 🔗 후속 연구: [[papers/375_Generating_full_length_wikipedia_biographies_The_impact_of_g/review]] — 대규모 언어 모델을 위한 추론 시간 편향 제거 프레임워크로 본 논문의 성별 편향 문제를 해결하는 방법론을 제시한다.
- 🏛 기반 연구: [[papers/1127_MMSD20_Towards_a_Reliable_Multi-modal_Sarcasm_Detection_Syst/review]] — 추론 시점 편향 제거 프레임워크는 멀티모달 풍자 탐지에서 허위 신호 제거와 신뢰성 확보를 위한 기술적 기반을 제공합니다
