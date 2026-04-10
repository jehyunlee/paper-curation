---
title: "173_Bridging_social_psychology_and_llm_reasoning_Conflict-aware"
authors:
  - "Wei Chen"
  - "Han Ding"
  - "Meng Yuan"
  - "Zhao Zhang"
  - "Deqing Wang"
date: "2025"
doi: "arXiv:2503.13879"
arxiv: ""
score: 4.1
essence: "학술 동료심사 시스템의 메타-리뷰(종합의견) 자동생성을 위해 Kahneman의 이원인지이론(dual-process theory)을 LLM에 적용한 인지정렬프레임워크(CAF)를 제안하며, 기존 LLM 방식의 앵커링 효과(anchoring effect)와 동조편향(conformity bias)을 정량화하고 완화한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Multi-Hop_Reasoning_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Hadi et al._2025_Bridging social psychology and llm reasoning Conflict-aware meta-review generation via cognitive al.pdf"
---

# Bridging social psychology and llm reasoning: Conflict-aware meta-review generation via cognitive alignment

> **저자**: Wei Chen, Han Ding, Meng Yuan, Zhao Zhang, Deqing Wang, Fuzhen Zhuang | **날짜**: 2025 | **DOI**: [arXiv:2503.13879](https://arxiv.org/abs/2503.13879)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: 인간의 메타-리뷰 작성에서 "빠른 사고"와 "느린 사고" 과정*

학술 동료심사 시스템의 메타-리뷰(종합의견) 자동생성을 위해 Kahneman의 이원인지이론(dual-process theory)을 LLM에 적용한 인지정렬프레임워크(CAF)를 제안하며, 기존 LLM 방식의 앵커링 효과(anchoring effect)와 동조편향(conformity bias)을 정량화하고 완화한다.

## Motivation

- **Known**: 급증하는 학술논문 투고로 인해 LLM 기반 동료심사 자동화 도구의 필요성이 증대되었으며, Chain-of-Thought(CoT) 등의 추론 방식이 개별 리뷰 생성에는 성과를 보이고 있음

- **Gap**: 기존 LLM 기반 메타-리뷰 생성 방식은 (1) 상충하는 평가의견을 효과적으로 처리하지 못하고, (2) 인간 의사결정의 인지편향(앵커링 효과: 첫 리뷰가 0.255의 계수로 과도하게 영향, 인간은 0.193; 동조편향: LLM의 동조계수 κ=0.125-0.25 vs 인간 1.00)을 증폭시킴

- **Why**: 메타-리뷰는 단순 요약이 아닌 증거기반의 합의도출과 갈등해결이 필요한 고차적 인지작업이며, 인간 심사위원회는 저갈등 상황에서는 직관적 판단(빠른 사고), 고갈등 상황에서는 심층 분석(느린 사고)을 구분 적용함

- **Approach**: 이원인지이론을 LLM에 구현하여 (1) 핵심정보 추출, (2) 갈등인식 점진적 통합, (3) 인지정렬(이원추론)의 3단계 파이프라인 구성

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: 서로 다른 리뷰어(R1-R5)의 최종 스코어 영향도 및 앵커링 효과 차이(Δ)*

![Figure 3](figures/fig3.webp)
*그림 3: 제안된 CAF 모델의 아키텍처*

1. **인지편향 정량화**: 앵커링 효과와 동조편향을 수학적으로 정의·측정하는 메트릭 개발 (로지스틱 회귀를 통한 계수 ξᵢ 산출, 동조계수 κ 정의)

2. **성능 개선**: CAF 적용 결과 감정 일관성(sentiment consistency) 최대 19.47% 향상, 내용 일관성(content consistency) 최대 12.95% 개선 달성

## How

- **초기화 단계(Initialization)**: 각 리뷰로부터 F_LLM을 통해 핵심 요소 추출, 모든 리뷰의 정보를 S₁∼ₙ = ⋃F_LLM(Rᵢ)로 통합

- **점진적 통합 단계(Incremental Integration)**: 순차적으로 리뷰를 처리하면서 동시에 상충(conflict) 맵핑 수행 (한 번에 모든 리뷰 처리로 인한 앵커링 효과 완화)

- **인지정렬 단계(Cognitive Alignment)**: 갈등 수준 판정 후 (1) 저갈등: 빠른 사고로 직관적 종합, (2) 고갈등: 느린 사고로 각 의견의 강점·약점 분석, 증거기반 추론을 통한 합의 도출

## Originality

- **첫 시도**: 학술 메타-리뷰 생성 태스크에서 앵커링 효과와 동조편향을 실증적으로 규명한 첫 연구

- **이론적 토대**: 사회심리학의 이원인지이론을 LLM 아키텍처에 구체적으로 구현하여 심리학과 NLP의 교차 연구 확장

- **메커니즘 설계**: 갈등맵핑과 이원추론 경로의 결합으로 단순 프롬프트 기법이 아닌 구조화된 프레임워크 제시

## Limitation & Further Study

- **평가 규모**: 50편 논문 기반 초기 실험(앵커링, 동조편향 측정)으로 대규모 검증 필요

- **편향 측정의 한계**: 동조계수 κ가 '다수결이 맞는 경우의 비율'만 측정하여 인지편향의 방향성을 직접 포착하지 못할 수 있음

- **모델 일반화**: GPT-4o, GPT-3.5, Qwen2.5-7B 등 특정 모델에서의 편향 정량화이며 다양한 LLM 아키텍처에 대한 검증 부족

- **후속 방향**: (1) 대규모 학술 메타-리뷰 벤치마크 구축, (2) 다층 갈등 분류(사실적/방법론적/해석적 갈등) 세분화, (3) 인간-LLM 협업 시나리오에서의 편향 완화 효과 검증

## Evaluation

| 항목 | 점수 | 근거 |
|------|------|------|
| **Novelty** | 4.5/5 | 사회심리학 이론을 LLM 메타-리뷰에 처음 적용, 인지편향의 정량적 측정 메트릭 개발 |
| **Technical Soundness** | 4/5 | 이원인지 아키텍처 설계는 명확하나, 갈등 수준 판정 기준(threshold)의 수학적 정의 부재, 로지스틱 회귀 기반 편향 측정은 타당하나 샘플 크기 제한 |
| **Significance** | 4/5 | 학술심사 자동화의 중요한 문제(메타-리뷰 신뢰성)를 다루며 19.47% 향상 달성, 다만 실제 학술지 도입까지의 검증 경로 명확하지 않음 |
| **Clarity** | 4/5 | 이론 배경과 프레임워크 구조는 명확하나, 초기화/통합 단계의 구체적 프롬프트와 갈등 판정 로직이 본문에 부분 생략 |
| **Overall** | 4.1/5 | - |

**총평**: 사회심리학의 이원인지이론을 학술 메타-리뷰 생성이라는 실무적 과제에 창의적으로 접목하고, 기존 LLM의 앵커링·동조편향을 최초로 정량화한 의미 있는 연구이나, 평가 규모 확대와 갈등 판정 기준의 수학적 정교화가 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/537_Mind_the_blind_spots_A_focus-level_evaluation_framework_for/review]] — 포커스 레벨 평가와 인지정렬프레임워크는 모두 LLM 리뷰 시스템의 편향 문제를 다루는 상호 보완적인 접근법입니다
- 🔗 후속 연구: [[papers/608_Peer_Review_as_A_Multi-Turn_and_Long-Context_Dialogue_with_R/review]] — 다중 턴 장문맥 대화로서의 동료심사는 메타-리뷰의 갈등 인식 프레임워크를 실제 리뷰 프로세스로 확장한 응용입니다
- 🏛 기반 연구: [[papers/883_When_reviewers_lock_horn_Finding_disagreement_in_scientific/review]] — 과학적 리뷰에서 의견 불일치 발견은 메타-리뷰에서 갈등 인식 및 완화의 이론적 기반이 되는 현상을 분석합니다
- 🔄 다른 접근: [[papers/537_Mind_the_blind_spots_A_focus-level_evaluation_framework_for/review]] — 인지정렬프레임워크의 앵커링 효과 완화와 포커스 레벨 평가는 모두 LLM 리뷰의 편향 문제를 다루는 상호 보완적 접근법입니다
- 🔗 후속 연구: [[papers/319_Ethnography_and_machine_learning_Synergies_and_new_direction/review]] — 사회심리학과 LLM 추론의 결합이 민족지학과 머신러닝 융합의 구체적인 확장 사례이다.
- 🔄 다른 접근: [[papers/179_Can_ai_replace_human_subjects_a_large-scale_replication_of_p/review]] — 심리학 실험 재현 vs 사회심리학과 LLM 추론 연결의 서로 다른 심리학 접근
- 🏛 기반 연구: [[papers/458_Language_agents_mirror_human_causal_reasoning_biases/review]] — 사회 심리학과 LLM 추론의 연결이 언어 에이전트 편향 연구의 이론적 기반을 제공한다
- 🧪 응용 사례: [[papers/077_AI_for_social_science_and_social_science_of_AI_A_Survey/review]] — LLM 추론에서 갈등 인식 사회심리학 연구가 사회과학을 위한 AI의 실제 활용 방법을 제시한다.
- 🧪 응용 사례: [[papers/498_LLM_as_a_Mastermind_A_Survey_of_Strategic_Reasoning_with_Lar/review]] — 사회심리학과 LLM 추론의 갈등 인식 연구가 다중 에이전트 환경에서의 전략적 추론 메커니즘에 직접 적용되는 심리학적 통찰이다.
- 🏛 기반 연구: [[papers/331_Exploring_collaboration_mechanisms_for_llm_agents_A_social_p/review]] — 사회심리학과 LLM 추론의 갈등 인식 연구는 LLM 에이전트 간 협력 메커니즘 탐색의 이론적 기반을 제공한다.
