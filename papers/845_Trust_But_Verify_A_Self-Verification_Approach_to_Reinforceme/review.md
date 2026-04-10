---
title: "845_Trust_But_Verify_A_Self-Verification_Approach_to_Reinforceme"
authors:
  - "Xiaoyuan Liu"
  - "Tian Liang"
  - "Zhiwei He"
  - "Jiahao Xu"
  - "Wenxuan Wang"
date: "2025"
doi: "10.48550/arXiv.2505.13445"
arxiv: ""
score: 4.0
essence: "대규모 언어모델(LLM)의 \"표면적 자기반성(superficial self-reflection)\" 문제를 해결하기 위해, 검증 가능한 보상(verifiable rewards)을 활용하여 문제 풀이 능력과 자기검증 능력을 **동시에 온라인으로 학습**하는 RISE 프레임워크를 제안한다."
tags:
  - "cat/Reinforcement_Learning_and_Self-Verification"
  - "sub/LLM_Self-Correction_and_Verification"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liu et al._2025_Trust, But Verify A Self-Verification Approach to Reinforcement Learning with Verifiable Rewards.pdf"
---

# Trust, But Verify: A Self-Verification Approach to Reinforcement Learning with Verifiable Rewards

> **저자**: Xiaoyuan Liu, Tian Liang, Zhiwei He, Jiahao Xu, Wenxuan Wang | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2505.13445](https://doi.org/10.48550/arXiv.2505.13445)

---

## Essence

![Figure 1](figures/fig1.webp) 
*RISE 프레임워크: (i) 문제 풀이 및 검증 생성 단계와 (ii) RL 최적화 단계로 구성*

대규모 언어모델(LLM)의 "표면적 자기반성(superficial self-reflection)" 문제를 해결하기 위해, 검증 가능한 보상(verifiable rewards)을 활용하여 문제 풀이 능력과 자기검증 능력을 **동시에 온라인으로 학습**하는 RISE 프레임워크를 제안한다.

## Motivation

- **Known**: RLVR(Reinforcement Learning with Verifiable Rewards)을 통해 LLM의 추론 능력을 향상시킬 수 있으며, 최근 논문들이 검증 가능한 보상만으로 성능 개선을 입증했다.

- **Gap**: 기존 RLVR 방법들은 **올바른 답을 생성하지만 자신의 추론 과정을 견고하게 검증하지 못하는 문제**가 있다. 문제 풀이와 검증 학습이 분리되거나 검증 능력에 대한 직접적인 RL 피드백이 부족하다.

- **Why**: LLM이 진정한 추론 능력을 갖추려면 단순한 답 생성뿐 아니라 자신의 결과를 비판적으로 평가할 수 있어야 한다. 이는 테스트 타임 성능 향상과 더 견고한 추론 시스템으로 이어질 수 있다.

- **Approach**: 결과 검증자(outcome verifier)로부터의 검증 가능한 보상을 **풀이 생성과 자기검증 작업 모두에 동시에 활용**하는 온라인 RL 프레임워크를 설계한다.

## Achievement

![Figure 2](figures/fig2.webp)
*다양한 샘플링 예산에서의 테스트 타임 성능 비교 (k값)*

1. **추론 정확도 향상**: Qwen-3B 기준 Zero-RL 베이스라인 대비 3.7% 평균 개선, 지시어 조정 모델(Qwen-3B-Instruct)과 비교하면 일관된 상위 성능

2. **검증 능력 대폭 개선**: 검증 정확도에서 최대 2.8배 향상 달성, Qwen-3B-Instruct 대비 33.4% 성능 이득

3. **테스트 타임 다수결 투표(majority voting) 초과**: RISE-3B와 RISE-7B가 k=4 추론 예산 하에서 표준 다수결 투표를 각각 +0.2%, +1.9% 상회

4. **모델 규모 확장성**: 1.5B, 3B, 7B 모델에서 일관된 성능 개선으로 방법론의 일반성 입증

## How

![Figure 3](figures/fig3.webp)
*RISE와 다른 접근법 간의 비교 분석*

- **2단계 프로세스**:
  1. **문제 풀이 및 검증 생성**: 훈련 배치의 문제에 대해 모델이 chain-of-thought 풀이를 k번 롤아웃으로 생성, 생성된 풀이를 검증 프롬프트 템플릿으로 포맷팅하여 자기검증 지시 생성
  2. **RL 최적화**: 원본 생성 데이터와 검증 데이터를 혼합한 새 배치 구성, PPO 목적함수로 모델 업데이트

- **검증 보상 활용**: 결과 검증자 OV가 생성된 풀이의 정확성에 대해 이진 보상(0 또는 1)을 제공, 동일한 보상 신호를 검증 점수 예측의 정확성 평가에도 적용

- **온라인 메커니즘**: 현재 정책(on-policy)에서 생성된 풀이를 즉시 검증하므로, 모델의 실제 생성 분포에 대한 검증 능력 학습이 가능

- **통합 학습**: 풀이 생성 궤적과 자기검증 궤적의 보상을 함께 사용하여 정책 업데이트, 단일 RL 프로세스 내에서 두 능력 동시 개선

## Originality

- **검증 능력의 명시적 RL 학습**: 기존 연구에서 검증은 주로 풀이 개선의 보조 수단으로만 활용되었으나, RISE는 검증 자체를 동등한 RL 학습 대상으로 취급

- **온라인 자기검증의 설계**: 오프라인 또는 분리된 검증 학습이 아닌, 현재 정책이 생성한 풀이에 대한 실시간 검증 학습으로 분포 불일치(distribution mismatch) 완화

- **P vs NP 이분법 활용**: 컴퓨터 과학의 고전적 P/NP 문제와 연결하여 생성과 검증의 비대칭성을 이론적으로 정당화

- **통합 검증 템플릿**: 원본 문제와 모델 풀이를 조합하여 체계적으로 검증 프롬프트를 생성하는 명확한 방식 제시

## Limitation & Further Study

- **검증자 의존성**: 결과 검증자의 정확도와 신뢰성에 전적으로 의존하므로, 검증자 오류 시 잘못된 신호 전파 가능성

- **이진 보상의 한계**: 검증 가능한 보상이 이진(0/1)이므로, 부분 정확도나 추론 과정의 질에 대한 세밀한 피드백 부족

- **계산 비용**: 각 배치마다 k번의 풀이 롤아웃과 이에 상응하는 검증 프롬프트 처리로 훈련 계산량 증가 (약 2배의 forward pass 필요)

- **수학 영역 중심의 평가**: 주로 수학적 추론 벤치마크(MATH, AMC, AIME 등)에서 평가되어, 다른 도메인(코드, 자연어 이해 등)으로의 일반화 여부 불명확

- **후속 연구 방향**:
  - 검증 능력이 다른 추론 작업(코드 생성, 논리적 추론)으로 전이되는지 검증
  - 더 복잡한 검증 기준(다단계 부분 채점)에서의 확장성 연구
  - 검증 계산 비용 최적화 전략 개발


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 검증 가능한 보상을 활용하여 LLM의 문제 풀이와 자기검증 능력을 동시에 강화하는 실용적이고 효과적인 온라인 RL 프레임워크를 제안하며, 수학적 추론 벤치마크에서의 일관된 성능 개선과 상세한 분석으로 학계의 주목할 만한 기여이다.

## Related Papers

- 🔄 다른 접근: [[papers/598_PAG_Multi-Turn_Reinforced_LLM_Self-Correction_with_Policy_as/review]] — 두 논문 모두 LLM 자기 검증을 다루되 RISE는 검증 가능한 보상 활용, PAG는 다중 턴 정책-검증자 전환에 초점을 맞춘다.
- 🔗 후속 연구: [[papers/683_RM-R1_Reward_Modeling_as_Reasoning/review]] — RM-R1의 추론 능력을 통합한 보상 모델링은 RISE의 검증 가능한 보상 시스템에 더 정교한 평가 메커니즘을 제공한다.
- ⚖️ 반론/비판: [[papers/471_Large_Language_Models_Cannot_Self-Correct_Reasoning_Yet/review]] — 대규모 언어모델이 아직 추론을 자기수정할 수 없다는 연구 결과는 RISE의 동시 학습 접근법이 해결하고자 하는 핵심 한계를 명확히 보여준다.
- 🔄 다른 접근: [[papers/683_RM-R1_Reward_Modeling_as_Reasoning/review]] — 두 논문 모두 보상 모델의 검증 능력을 다루되 RM-R1은 추론 통합, RISE는 자기검증 학습에 초점을 맞춘다.
- 🔄 다른 접근: [[papers/598_PAG_Multi-Turn_Reinforced_LLM_Self-Correction_with_Policy_as/review]] — 두 논문 모두 LLM의 자기 수정 능력을 다루되 PAG는 다중 턴 워크플로우, RISE는 검증 가능한 보상을 통한 동시 학습에 초점을 맞춘다.
- 🔄 다른 접근: [[papers/396_Hallucination_mitigation_using_agentic_ai_natural_language-b/review]] — 강화학습 기반 자기 검증을 통한 환각 문제 해결의 다른 접근 방식을 제시한다.
