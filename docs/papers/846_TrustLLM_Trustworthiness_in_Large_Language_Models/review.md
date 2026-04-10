---
title: "846_TrustLLM_Trustworthiness_in_Large_Language_Models"
authors:
  - "Lichao Sun"
  - "Yue Huang"
  - "Haoran Wang"
  - "Siyuan Wu"
  - "Qihui Zhang 외 40명"
date: "2024"
doi: "10.48550/arXiv.2401.05561"
arxiv: ""
score: 4.4
essence: "본 논문은 대규모 언어모델(Large Language Models, LLMs)의 신뢰성을 종합적으로 평가하기 위한 원칙 기반의 벤치마크 **TrustLLM**을 제시한다. 진실성, 안전성, 공정성, 견고성, 프라이버시, 기계윤리 등 6가지 핵심 차원에서 16개 주요 LLM을 평가하여 신뢰성의 다층적 특성을 규명한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Cognitive_LLM_Evaluation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Sun et al._2024_TrustLLM Trustworthiness in Large Language Models.pdf"
---

# TrustLLM: Trustworthiness in Large Language Models

> **저자**: Lichao Sun, Yue Huang, Haoran Wang, Siyuan Wu, Qihui Zhang 외 40명 | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2401.05561](https://doi.org/10.48550/arXiv.2401.05561)

---

## Essence

본 논문은 대규모 언어모델(Large Language Models, LLMs)의 신뢰성을 종합적으로 평가하기 위한 원칙 기반의 벤치마크 **TrustLLM**을 제시한다. 진실성, 안전성, 공정성, 견고성, 프라이버시, 기계윤리 등 6가지 핵심 차원에서 16개 주요 LLM을 평가하여 신뢰성의 다층적 특성을 규명한다.

## Motivation

- **Known**: ChatGPT와 같은 LLM들이 뛰어난 자연어처리 능력을 보유하고 있으며, 다양한 분야에서 광범위하게 활용되고 있음
- **Gap**: 기존 연구들이 신뢰성의 특정 측면만 부분적으로 다루고 있으며, LLM 신뢰성에 대한 포괄적이고 원칙 기반의 벤치마크가 부재함
- **Why**: 생의료, 금융, 법률 등 민감한 분야에서 LLM 활용이 증가하면서 신뢰성 보장이 필수적이나, 현재 LLM들의 신뢰성 수준에 대한 체계적 평가가 부족함
- **Approach**: 신뢰성의 8가지 차원(진실성, 안전성, 공정성, 견고성, 프라이버시, 기계윤리, 투명성, 책임성)에 대한 원칙을 수립하고, 이를 기반으로 30개 이상의 데이터셋을 포함하는 벤치마크 구축

## Achievement

![Figure 1](figures/fig1.webp)
*그림 1: TRUSTLLM에서 16개 LLM의 신뢰성 성능 순위카드*

1. **포괄적 벤치마크 구축**: 6개 차원 30개 데이터셋을 아우르는 최초의 종합 신뢰성 평가 프레임워크 제시
   
2. **주요 경험적 발견**:
   - 신뢰성과 유용성(기능적 효과성)이 일반적으로 양의 상관관계: GPT-4, ERNIE, Llama2와 같은 고성능 모델들이 신뢰성에서도 우수
   - 대형 폐쇄형(proprietary) LLM이 대부분의 오픈소스 모델을 능가하지만, Llama2는 여러 과제에서 폐쇄형 모델과 경쟁력 있는 성능 보임
   - 일부 모델(예: Llama2)은 과도한 안전 교정(over-calibration)으로 인해 유용성 저하 문제 발생

3. **차원별 핵심 통찰**:
   - **진실성**: 훈련 데이터의 잡음, 허위정보, 구식 정보로 인한 어려움; 외부 지식 통합 시 성능 현저히 개선
   - **안전성**: 오픈소스 모델들이 폐쇄형 모델에 비해 특히 탈옥(jailbreak), 독성, 오용 측면에서 큰 격차
   - **공정성**: 고정관념 인식 능력 부족 (최고 성능 GPT-4도 65% 정확도)
   - **견고성**: 개방형 과제와 분포 외(out-of-distribution) 과제에서 큰 편차
   - **프라이버시**: 프라이버시 규범 인식은 있으나 개인정보 처리에 편차 큼; 일부 모델에서 정보 유출 관찰
   - **기계윤리**: 기본적 도덕 이해는 있으나 복잡한 윤리 시나리오에서 부족

## How

![Figure 2](figures/fig2.webp)
*그림 2: TRUSTLLM 벤치마크 설계*

**평가 방법론**:

- **원칙 기반 설계**: 8개 신뢰성 차원별 명확한 평가 원칙 수립
- **다층적 평가**:
  - 진실성: 내부 지식만 사용, 외부 지식 통합, 환각(hallucination), 아부(sycophancy), 적대적 사실성 검증
  - 안전성: 탈옥 공격, 과도한 안전성, 독성, 오용 가능성 평가
  - 공정성: 고정관념, 폄하, 주관적 선택 편향 측정
  - 견고성: 자연 잡음에 대한 저항성, 개방형 과제, OOD(분포 외) 복원력
  - 프라이버시: 프라이버시 인식 및 정보 유출 평가
  - 기계윤리: 암묵적/명시적 윤리, 인식도 평가

- **평가 대상 모델**: 16개 주류 LLM (GPT-3.5-Turbo, GPT-4, Claude, Llama2, Alpaca, Falcon 등)

- **정량화 및 비교**: 모델별 성능 순위카드 생성, 성능 분포 시각화, 상관관계 분석

## Originality

- **최초 종합 신뢰성 벤치마크**: 기존의 단편적 안전성/공정성 평가를 넘어 8개 차원의 통합 프레임워크 제시
- **원칙 기반 평가 프레임워크**: 단순 점수 기반이 아닌 명확한 철학적/윤리적 원칙에 기반한 체계적 평가 체계
- **대규모 실증 평가**: 16개 모델, 30개+ 데이터셋을 통한 그 당시 최대 규모의 비교 실험
- **새로운 문제 제기**: 유용성과 신뢰성의 트레이드오프, "과도한 안전성(exaggerated safety)" 현상 규명
- **투명성과 책임성 강조**: 기술적 평가를 넘어 거버넌스 측면의 투명성, 책임성, 규제 논의 포함
- **오픈 액세스 제공**: 데이터셋, 코드, 리더보드 공개로 커뮤니티 기여 용이

## Limitation & Further Study

**한계**:
- 30개 데이터셋이 신뢰성의 모든 측면을 완전히 포괄하지 못할 가능성 (문화적, 언어적 다양성 부족)
- 프라이버시 평가가 주로 인식도와 Enron 이메일 데이터셋 기반으로 제한적
- 기계윤리 평가의 주관성 문제 (도덕적 판단 기준의 문화적 차이)
- 평가 메트릭이 일부 정성적 판단에 의존
- LLM의 빠른 발전으로 벤치마크의 시간-정확성(temporal accuracy) 문제 가능

**후속 연구 방향**:
- 더 다양한 문화적, 언어적 맥락에서의 신뢰성 평가
- 신뢰성 개선 기술의 효과성 검증 (RAG, fine-tuning 등)
- 신뢰성과 유용성의 최적 균형점 탐색
- 동적 벤치마크 구축으로 모델 진화 추적
- 산업-학계-오픈소스 커뮤니티 협력을 통한 신뢰성 표준화


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4.4/5

**총평**: 본 논문은 LLM 신뢰성에 대한 최초의 포괄적이고 원칙 기반의 벤치마크를 제시하여, AI 안전성과 신뢰성 연구에 중대한 기여를 한다. 8개 차원에 걸친 체계적 평가와 16개 모델에 대한 대규모 실증 연구는 큰 의미가 있으나, 평가 메트릭의 일부 주관성과 문화적 다양성 부족이 개선 과제이다. 오픈 액세스 제공으로 커뮤니티 기여 활성화 가능성이 높다.

## Related Papers

- 🔄 다른 접근: [[papers/736_SciTrust_Evaluating_the_Trustworthiness_of_Large_Language_Mo/review]] — 과학 분야 LLM 신뢰성 평가의 다른 접근법과 벤치마크 제시
- 🧪 응용 사례: [[papers/322_Evaluation_of_openai_o1_Opportunities_and_challenges_of_agi/review]] — OpenAI O1 모델 평가가 신뢰성 차원에서 구체적 사례 연구가 됨
- 🏛 기반 연구: [[papers/017_A_practical_review_of_mechanistic_interpretability_for_trans/review]] — 대형 언어모델의 신뢰성 평가는 기계적 해석가능성을 통한 모델 내부 이해의 궁극적인 목표와 평가 기준을 제공합니다
- 🏛 기반 연구: [[papers/388_GPT-4o_System_Card/review]] — 대규모 언어모델의 전반적인 신뢰성 평가 체계가 GPT-4o의 멀티모달 안전성 평가의 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/736_SciTrust_Evaluating_the_Trustworthiness_of_Large_Language_Mo/review]] — 대규모 언어모델의 전반적인 신뢰성 평가를 과학 분야에 특화하여 구체적으로 확장한 사례이다.
- 🏛 기반 연구: [[papers/237_Confidence_in_Large_Language_Model_Evaluation_A_Bayesian_App/review]] — 대규모 언어모델 신뢰성 연구가 베이지안 평가 방법론의 이론적 기초
- 🧪 응용 사례: [[papers/037_A_Survey_on_Uncertainty_Quantification_Methods_for_Deep_Lear/review]] — 대규모 언어 모델의 신뢰성 평가에 불확실성 정량화 방법을 실제 적용하는 사례를 제공합니다.
- 🔄 다른 접근: [[papers/810_Through_the_lens_of_core_competency_Survey_on_evaluation_of/review]] — LLM의 신뢰성 평가가 핵심 역량 중심 평가와는 다른 관점에서 모델 성능을 분석한다.
- 🏛 기반 연구: [[papers/800_The_hidden_dimensions_of_llm_alignment_A_multi-dimensional_s/review]] — TrustLLM의 신뢰성 평가 프레임워크가 LLM 안전 정렬 행동의 다차원 분석 방법론의 기초가 됨
- 🔗 후속 연구: [[papers/390_Grammars_of_formal_uncertainty_When_to_trust_llms_in_automat/review]] — 대규모 언어 모델의 신뢰성 종합 평가가 형식 검증에서의 불확실성 정량화를 더 광범위한 신뢰성 차원으로 확장한 연구이다.
- ⚖️ 반론/비판: [[papers/477_Large_language_models_pass_the_turing_test/review]] — LLM의 신뢰성 문제를 지적하며 튜링 테스트 통과만으로는 진정한 지능을 증명할 수 없음을 논의
- 🧪 응용 사례: [[papers/158_Biasfilter_An_inference-time_debiasing_framework_for_large_l/review]] — LLM 신뢰성 향상을 위해 추론 시간 편향 완화 기법을 체계적으로 적용
- 🏛 기반 연구: [[papers/148_Axolotl_fairness_through_assisted_self-debiasing_of_large_la/review]] — 대규모 언어 모델의 신뢰성에 대한 종합적인 평가 프레임워크가 AXOLOTL의 편향 완화 효과를 체계적으로 검증하는 기반을 제공한다.
