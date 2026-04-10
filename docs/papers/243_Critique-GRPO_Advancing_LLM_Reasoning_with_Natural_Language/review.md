---
title: "243_Critique-GRPO_Advancing_LLM_Reasoning_with_Natural_Language"
authors:
  - "Xiaoying Zhang"
  - "Hao Sun"
  - "Yipeng Zhang"
  - "Kaituo Feng"
  - "Chaochao Lu"
date: "2025"
doi: "10.48550/arXiv.2506.03106"
arxiv: ""
score: 4.2
essence: "본 논문은 순수 수치 보상(numerical rewards)의 한계를 극복하기 위해 자연언어 비판(natural language critiques)을 온라인 강화학습(online RL) 프레임워크에 통합한 Critique-GRPO를 제안한다. 이는 LLM의 추론 능력을 향상시키는 새로운 접근 방식이다."
tags:
  - "cat/Reinforcement_Learning_and_Self-Verification"
  - "sub/Reasoning_Enhancement_via_Reinforcement_Learning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhang et al._2025_Critique-GRPO Advancing LLM Reasoning with Natural Language and Numerical Feedback.pdf"
---

# Critique-GRPO: Advancing LLM Reasoning with Natural Language and Numerical Feedback

> **저자**: Xiaoying Zhang, Hao Sun, Yipeng Zhang, Kaituo Feng, Chaochao Lu | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2506.03106](https://doi.org/10.48550/arXiv.2506.03106)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: (a) Critique-GRPO는 수치 피드백만이 아닌 자연어 피드백(비판)을 통해 초기 응답과 자기 개선 모두에서 학습 가능. (b) Qwen3-8B에서 8가지 추론 과제 평균 Pass@1 4.5% 개선. (c) 자기 비판을 통한 자기 개선으로 AIME 2024에서 66.7% Pass@1 달성.*

본 논문은 순수 수치 보상(numerical rewards)의 한계를 극복하기 위해 자연언어 비판(natural language critiques)을 온라인 강화학습(online RL) 프레임워크에 통합한 Critique-GRPO를 제안한다. 이는 LLM의 추론 능력을 향상시키는 새로운 접근 방식이다.

## Motivation

- **Known**: 최근 RL을 활용한 LLM의 복잡한 추론 능력 향상이 의미 있는 진전을 이루고 있음 (R1-Zero 패러다임 등)
  
- **Gap**: 순수 수치 피드백만 사용하는 RL 기반 방법들이 세 가지 근본적인 한계를 가짐:
  - 성능 정체 (plateau): 8배 데이터 증가나 확장 학습에도 불구하고 개선 중단
  - 비효과적 자발적 자기 성찰: "Aha 모멘트"가 문제 해결 성공률을 거의 개선하지 못함
  - 지속적 실패: 모델이 특정 학습 문제에서 반복적으로 실패

- **Why**: 수치 피드백은 본질적으로 표현력이 부족하여 응답이 실패한 *이유*와 *어떻게 수정할지*를 설명할 수 없음. 반면 자연언어 비판(critique)은 명시적 지도를 제공 가능

- **Approach**: 자연언어 비판과 수치 보상을 모두 통합하는 온라인 RL 프레임워크(Critique-GRPO) 개발으로 두 가지 이점을 모두 활용

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: Critique-GRPO 개요. 질문에 대해 초기 응답을 샘플링하고, 보상 시스템의 비판을 활용하여 in-context learning으로 응답을 개선. 이를 초기 응답과 결합하여 정책 최적화 수행.*

1. **광범위한 성능 개선**: 
   - Qwen 모델 계열에서 평균 Pass@1 +15.0-21.6% 개선
   - Llama-3.2-3B-Instruct에서 +7.3% 개선
   - 8가지 도전적인 추론 과제(reasoning benchmarks) 전반에서 우수한 성능

2. **자기 비판을 통한 자기 개선**: 
   - 자기 생성 비판(self-generated critiques)만으로도 GRPO 대비 +16.7% Pass@1 개선 달성 (AIME 2024)
   - 모델이 외부 전문가에 의존하지 않고도 자율적 개선 가능

3. **비판 소스의 강건성**: 
   - 규칙 기반(rule-based) 및 모델 기반(model-based) 보상 시스템 모두에서 일관된 개선
   - 다양한 형태의 비판(지시적 비판, 근거 포함 비판, 연쇄적 사고 비판)에 모두 대응

## How

![Figure 3](figures/fig3.webp)
*그림 3: [상세 메커니즘 시각화]*

- **핵심 메커니즘**: 
  - 표준 생성(standard generation): 초기 응답을 표준 탐색으로 생성
  - 비판 유도 개선(critique-guided refinement): 보상 시스템의 비판에 기반한 in-context learning으로 응답 개선
  
- **기술적 개선 사항**:
  - 엔트로피 폭발(entropy explosion) 방지를 위해 초기 응답에 높은 가중치 부여, 개선 내용은 선택적 포함
  - 정책 형성 함수(policy shaping function) 도입: 성공적이면서도 새로운 개선에는 높은 보상, 실패한 개선에는 패널티 부여
  - 분포 편이(distribution shift)로 인한 성능 저하 완화를 위한 가중 장점 함수(weighted advantage function) 적용

- **알고리즘 기반**: Group Relative Policy Optimization (GRPO)를 확장하여 구현
  - GRPO의 상대적 장점 계산 메커니즘 유지
  - 이중 궤적(dual trajectory) 학습 구조 추가

## Originality

- **새로운 문제 정의**: 순수 수치 피드백 RL의 세 가지 구체적 한계(성능 정체, 비효과적 자기 성찰, 지속적 실패)를 체계적으로 실증적으로 밝혀냄

- **창의적 해결책**: 자연언어 비판을 온라인 RL 루프에 통합하는 처음의 시도
  - 기존 비판 학습 연구는 대부분 정적 비판을 모방하는 감독학습(SFT)에 국한
  - Critique-GRPO는 동적 탐색과 실시간 적응이 가능한 온라인 프레임워크 제공

- **이론적 통찰**: 자연언어 피드백의 "언어적 신용 배정(verbal credit assignment)"이 in-context learning을 통해 스칼라 보상으로 도달 불가능한 고품질 개선 궤적에 접근 가능하게 함을 입증

- **방법론의 일반성**: 특정 모델이나 과제에 국한되지 않는 광범위한 적용 가능성 입증 (Qwen, Llama 등 다양한 모델)

## Limitation & Further Study

- **한계**:
  - 비판 생성 시스템의 품질이 전체 성능에 큰 영향을 미칠 수 있으나, 이에 대한 상세한 민감도 분석 부족
  - 계산 비용이 기존 GRPO 대비 증가함 (초기 응답 + 개선 응답의 이중 생성 및 평가)
  - 비판 유효성 판단과 개선 선택의 기준이 다소 휴리스틱한 특성
  
- **후속 연구**:
  - 더 효율적인 비판 생성 및 선택 메커니즘 개발
  - 다양한 도메인(코드 생성, 창의적 과제 등)으로의 확장
  - 비판과 수치 피드백의 최적 가중 조합에 대한 이론적 분석
  - 자동 비판 생성 시스템의 오류 누적 효과 연구

## Evaluation

- **Novelty**: 4.5/5
  - 자연언어와 수치 피드백의 통합이라는 참신한 시도이나, 개별 구성 요소들(비판, in-context learning, GRPO)은 기존 기술의 조합

- **Technical Soundness**: 4/5
  - 실증적 분석과 알고리즘 설계가 체계적이고 합리적
  - 다만 이론적 근거(엔트로피 폭발 완화 방식, 정책 형성 함수의 설정)가 다소 휴리스틱
  
- **Significance**: 4.5/5
  - RL 기반 LLM 추론 향상에 즉시 적용 가능한 실질적 방법론
  - 광범위한 실험과 일관된 개선이 실제 영향력을 입증

- **Clarity**: 4/5
  - 전반적으로 명확하고 체계적인 서술이나, 세부 구현 사항의 일부(가중치 설정, 선택 기준)가 불충분히 설명됨
  
- **Overall**: 4.2/5

**총평**: 본 논문은 순수 수치 피드백 RL의 구체적 한계를 실증적으로 규명하고, 자연언어 비판과의 통합을 통해 온라인 RL 프레임워크를 성공적으로 확장한 의미 있는 연구이다. 광범위한 실험 결과와 일관된 성능 개선은 실용적 가치가 높으나, 이론적 깊이와 계산 효율성 측면에서는 추가 개선의 여지가 있다.

## Related Papers

- 🏛 기반 연구: [[papers/265_DeepSeek-R1_incentivizes_reasoning_in_LLMs_through_reinforce/review]] — DeepSeek-R1의 순수 강화학습 기반 추론 능력은 Critique-GRPO의 자연언어 비판과 수치 보상 통합에 기본적인 RL 토대를 제공한다.
- 🔗 후속 연구: [[papers/598_PAG_Multi-Turn_Reinforced_LLM_Self-Correction_with_Policy_as/review]] — PAG의 다중 턴 자기 수정 메커니즘을 Critique-GRPO가 자연언어 비판을 추가하여 더 풍부한 피드백 체계로 발전시킨다.
- 🏛 기반 연구: [[papers/028_A_survey_of_reasoning_with_foundation_models/review]] — 파운데이션 모델의 추론 능력 서베이는 Critique-GRPO의 자연언어 비판 통합 접근법에 추론 메커니즘의 이론적 배경을 제공한다.
- 🔗 후속 연구: [[papers/265_DeepSeek-R1_incentivizes_reasoning_in_LLMs_through_reinforce/review]] — 자연언어 비판을 통합한 Critique-GRPO는 DeepSeek-R1의 순수 RL 접근법에 추가적인 언어적 피드백 메커니즘을 제공한다.
- 🔄 다른 접근: [[papers/887_Wrong-of-thought_An_integrated_reasoning_framework_with_mult/review]] — 자연어 비판을 통한 LLM 추론 개선 방법이 오류 정보 활용 접근법과 상호 보완적이다.
