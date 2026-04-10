---
title: "368_Gemini_15_Unlocking_multimodal_understanding_across_millions"
authors:
  - "Machel Reid"
  - "N. Savinov"
  - "Denis Teplyashin"
  - "Dmitry Lepikhin"
  - "T. Lillicrap"
date: "2024"
doi: "arXiv:2403.05530v5"
arxiv: ""
score: 0
essence: "Gemini 1.5는 최대 1,000만 토큰의 컨텍스트를 처리할 수 있는 멀티모달 대규모 언어 모델로, 기존 모델들(Claude 3.0의 20만 토큰, GPT-4 Turbo의 12.8만 토큰)보다 획기적으로 확장된 컨텍스트 윈도우를 구현했다. Gemini 1.5 Pro와 Flash 두 가지 변형은 긴 문서, 영상, 오디오에 대한 검색 및 추론 능력에서 최첨단 성능을 달성하면서도 계산 효율성을 유지한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Multimodal_Scientific_Benchmarks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Reid et al._2024_Gemini 1.5 Unlocking multimodal understanding across millions of tokens of context.pdf"
---

# Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context

> **저자**: Machel Reid, N. Savinov, Denis Teplyashin, Dmitry Lepikhin, T. Lillicrap, Jean-Baptiste Alayrac, Radu Soricut, Angeliki Lazaridou, Orhan Firat, Julian Schrittwieser, Ioannis Antonoglou, Rohan Anil, Sebastian Borgeaud, Andrew M. Dai, Katie Millican, Ethan Dyer, Mia Glaese, Thibault Sottiaux, Benjamin Lee, Fabio Viola | **날짜**: 2024 | **DOI**: [arXiv:2403.05530v5](https://arxiv.org/abs/2403.05530)

---

## Essence

![Figure 1](https://arxiv.org/html/2403.05530v5/x1.png)
*Gemini 1.5 Pro는 모든 모달리티(텍스트, 비디오, 오디오)에서 1M 토큰까지 99.7% 이상의 "needle" recall을 달성하며, 텍스트 모달리티에서는 10M 토큰까지 성능을 유지함*

Gemini 1.5는 최대 1,000만 토큰의 컨텍스트를 처리할 수 있는 멀티모달 대규모 언어 모델로, 기존 모델들(Claude 3.0의 20만 토큰, GPT-4 Turbo의 12.8만 토큰)보다 획기적으로 확장된 컨텍스트 윈도우를 구현했다. Gemini 1.5 Pro와 Flash 두 가지 변형은 긴 문서, 영상, 오디오에 대한 검색 및 추론 능력에서 최첨단 성능을 달성하면서도 계산 효율성을 유지한다.

## Motivation

- **Known**: Transformer 기반 언어 모델의 컨텍스트 길이는 점진적으로 확장되어 왔으나(2-gram → n-gram → RNN → Transformer의 수십만 토큰), 멀티모달 이해에서 장문맥(long-context) 처리의 한계가 존재한다.

- **Gap**: 기존 최첨단 모델들(Claude 3.0, GPT-4 Turbo)은 최대 20만 토큰 수준의 컨텍스트만 지원하며, 이는 수 시간의 비디오나 수십 개의 장문 문서를 동시에 처리하기에 부족하다. 또한 장문맥 확장 시 핵심 능력(수학, 코딩, 추론)이 저하되는 경향이 있다.

- **Why**: 1,000만 토큰 규모의 컨텍스트 처리는 (1) 전체 코드베이스 분석, (2) 여러 시간의 비디오 동시 이해, (3) 새로운 언어의 문법 자료로부터의 in-context learning, (4) 실무자의 생산성 향상 등 실제 응용 분야에서 혁신적 가치를 제공할 수 있다.

- **Approach**: Sparse Mixture-of-Experts (MoE) 기반 Transformer 아키텍처, 개선된 학습 및 증류(distillation) 인프라, 장문맥 특화 주의 메커니즘(attention mechanisms)을 통해 효율성과 성능을 동시에 달성하고, "needle-in-haystack" 합성 태스크와 실제 벤치마크를 통해 검증한다.

## Achievement

![Figure 2](https://arxiv.org/html/2403.05530v5/x2.png)
*Gemini 1.5 Pro (May 2024)는 MATH (58.5% → 67.7%), GPQA (41.5% → 46.2%), MathVista (54.7% → 63.9%), EgoSchema (65.1% → 72.2%) 등 다양한 벤치마크에서 February 버전 대비 일관된 개선을 보임*

1. **초장문맥 처리**: Gemini 1.5 Pro는 텍스트에서 1,000만 토큰(약 700만 단어), 오디오에서 970만 토큰(최대 107시간), 비디오에서 990만 토큰(최대 10.5시간)까지 처리 가능하며, 모든 모달리티에서 99% 이상의 "needle" recall 달성.

2. **핵심 능력 강화**: Gemini 1.5 Pro는 Gemini 1.0 Ultra와 비교하여 종합 벤치마크의 77.8% (35/45), 텍스트의 84.2% (16/19), 비전의 85.7% (18/21)에서 우수한 성능을 달성하면서도, 학습 계산량은 훨씬 적음. 수학(+49.6%), 과학 및 추론(+30.8%), 다국어성(+21.4%), 코드(+21.5%) 등에서 대폭 개선.

3. **혁신적 in-context learning**: 200명 미만의 화자를 가진 파푸아 언어 "Kalamang"의 500쪽 문법 자료를 컨텍스트에 제공하면, 같은 자료로 학습한 인간과 유사한 수준의 번역 능력을 획득. 처음으로 멀티모달 자료(텍스트 + 음성)로부터 새로운 언어의 음성 인식도 학습 가능.

4. **실무 생산성 향상**: 10개 직종에서 전문가와의 협업을 통해 26~75%의 작업 시간 단축 달성.

## How

![Figure 4](https://arxiv.org/html/2403.05530v5/x4.png)
*Kalamang 언어: 500쪽 문법 참고서와 사전을 컨텍스트에 제공하여 영어-Kalamang 번역을 학습*

- **아키텍처**: Sparse Mixture-of-Experts (MoE) Transformer 기반. 조건부 계산(conditional computation)을 통해 각 입력마다 모델의 일부만 활성화하여 효율성 극대화.

- **장문맥 메커니즘**: 기존 주의 메커니즘의 성능 저하 문제를 해결하기 위해 계층적 주의, 국소적 주의(local attention) 및 전역적 주의(global attention)의 혼합, 토큰 압축 기법 도입.

- **학습 및 증류**: 개선된 사전 학습(pre-training) 및 사후 학습(post-training) 절차. Gemini 1.5 Flash는 1.5 Pro에서 파라미터를 선택적으로 제거하는 증류(distillation) 방식으로 개발되어, 성능 저하를 최소화하면서 처리 속도 및 효율성 대폭 향상.

- **평가 방법론**: 
  - Synthetic "needle-in-haystack": 임의로 배치된 정보를 다양한 깊이(0~100%)에서 회상하는 능력 측정
  - 실제 태스크: 장문서 QA, 장비디오 QA, 장문맥 음성 인식(ASR), 코드베이스 분석
  - 표준 벤치마크: MATH, GPQA, MMLU, HumanEval, MathVista, EgoSchema 등 50개 이상의 벤치마크

## Originality

- **10M 토큰 규모 달성**: 기존 모델 대비 50배 이상 확장된 컨텍스트 윈도우를 멀티모달 환경에서 실현한 것은 획기적 진전. 특히 모든 모달리티에서 99% 이상의 검색 성능 유지는 기술적 혁신을 입증.

- **장문맥 확장 시 핵심 능력 보존**: 기존 연구에서는 컨텍스트 확장이 기본 성능 저하를 초래하는 경향을 보였으나, Gemini 1.5는 오히려 전반적 성능을 강화. February 버전 대비 모든 추론 및 다중모달 벤치마크에서 개선.

- **다국어 in-context learning의 실현**: 단일 언어 자료만으로 매우 희귀한 언어의 번역 및 음성 인식을 학습하는 능력은 이전 LLM에서 보고되지 않은 혁신적 역량. 이는 언어학적 자료의 충분한 제공만으로 저자원 언어 처리가 가능함을 시사.

- **효율성과 성능의 이중 달성**: Gemini 1.5 Flash는 1.0 Pro보다 작으면서도 성능은 동등 또는 우수(82% 벤치마크에서 win-rate), 특히 비전에서 1.0 Ultra를 능가(61.9% win-rate)하여, 모델 압축과 성능 간의 새로운 파레토 최적선을 제시.

## Limitation & Further Study

- **오디오 모달리티의 약한 성능**: Gemini 1.5 Flash는 오디오 벤치마크에서 1.0 Pro/Ultra와의 경쟁에서 0% win-rate를 기록하였으며, 이는 오디오 처리의 특수성(음향 특성 vs. 의미론적 정보 균형)이 아직 완전히 해결되지 않음을 시사.

- **컨텍스트 길이 상한의 불명확성**: 실험에서 10M 토큰까지 성능을 검증했으나, 이것이 진정한 상한인지 아니면 추가 확장이 가능한지에 대한 명시적 분석 부족. 향후 수억 토큰 규모에서의 가능성과 한계를 탐색할 필요.

- **계산 비용 분석의 부재**: 전체 학습 토큰 수, 학습 시간, 하드웨어 사용량 등 구체적인 계산 효율성 지표가 논문에 명시되지 않아, 다른 모델과의 객관적 비교가 제한적. 추론(inference) 비용도 장문맥 처리 시 어떻게 확장되는지에 대한 상세 분석 필요.

- **한계 사례(failure cases) 분석 부족**: "needle-in-haystack" 합성 태스크에서는 99% recall을 달성하지만, 실제 복잡한 장문서 추론에서 주의 산만(distraction)이나 모순 처리(contradiction resolution)에 대한 실패 사례 분석이 제한적.

- **다중 모달리티 상호작용의 깊이**: 텍스트, 비디오, 오디오를 동시에 처리하는 능력은 입증되었으나, 이들 간의 정교한 상호작용(cross-modal reasoning)이 얼마나 효과적인지에 대한 심화 평가 필요.

- **책임 있는 배포의 구체성**: 모델 카드가 부록에 포함되었으나, 10M 토큰 규모 처리로 인한 프라이버시(개인정보 재현 위험) 및 보안 문제(악의적 이용)에 대한 심층 논의가 제한적.

## Evaluation

- **Novelty (독창성)**: 4.8/5 — 10M 토큰의 멀티모달 컨텍스트 처리는 정량적으로 50배 이상 확장된 획기적 성과이며, 다국어 in-context learning은 이전에 보고되지 않은 역량. 다만 기본 아키텍처(MoE Transformer)와 주의 메커니즘 자체는 기존 연구의 점진적 개선으로 볼 수 있음.

- **Technical Soundness (기술적 견실성)**: 4.6/5 — Sparse MoE 기반 설계와 "needle-in-haystack" 평가 방법론은 기술적으로 견실하며, 50개 이상 벤치마크에서의 광범위한 검증은 신뢰도를 높임. 다만 구체적인 아키텍처 세부사항(attention 메커니즘, 토큰 압축 기법)이 제한적으로 공개되어 재현성 검증에 제약.

- **Significance (중요성)**: 4.9/5 — 실제 응용 분야(코드 분석, 장비디오 이해, 저자원 언어 처리, 전문가 생산성 향상)에서 구체적 임팩트를 입증했으며, 산업 표준으로서의 영향력은 매우 큼. 다만 오디오 모달리티에서의 약한 성능은 멀티모달성의 완전성을 다소 제한.

## Related Papers

- 🏛 기반 연구: [[papers/036_A_survey_on_transformer_context_extension_Approaches_and_eva/review]] — 트랜스포머 컨텍스트 확장 방법에 대한 조사가 Gemini 1.5의 1천만 토큰 컨텍스트 처리 기술을 이해하는 기반을 제공한다.
- 🔗 후속 연구: [[papers/005_A_comprehensive_survey_on_long_context_language_modeling/review]] — 긴 컨텍스트 언어 모델링에 대한 포괄적인 조사가 Gemini 1.5의 초장기 컨텍스트 처리 능력의 이론적 배경과 한계를 분석한다.
- ⚖️ 반론/비판: [[papers/452_L-citeeval_Do_longcontext_models_truly_leverage_context_for/review]] — 긴 컨텍스트 모델이 실제로 컨텍스트를 제대로 활용하는지에 대한 비판적 평가가 Gemini 1.5의 1천만 토큰 처리 주장을 검증한다.
- 🔗 후속 연구: [[papers/858_Unsupervised_crosslingual_representation_learning_at_scale/review]] — 다언어 표현학습이 멀티모달 이해로 확장되는 자연스러운 발전 경로
- 🔗 후속 연구: [[papers/369_Gemini_a_family_of_highly_capable_multimodal_models/review]] — Gemini 1.5로 발전하면서 더 긴 컨텍스트와 향상된 멀티모달 이해 능력을 제공
