---
title: "887_Wrong-of-thought_An_integrated_reasoning_framework_with_mult"
authors:
  - "Yongheng Zhang"
  - "Qiguang Chen"
  - "Jingxuan Zhou"
  - "Peng Wang"
  - "Jiasheng Si"
date: "2024"
doi: "arXiv:2410.04463"
arxiv: ""
score: 4.0
essence: "대규모 언어 모델(LLM)의 추론 성능을 향상시키기 위해 다중 관점에서 검증하고 이전 오류 정보를 활용하는 WoT(Wrong-of-Thought) 프레임워크를 제안한다. 기존 XoT의 단일 검증 방식과 오류 정보 무시 문제를 해결하여 8개 데이터셋과 5개 LLM에서 우수한 성능을 달성했다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Agent_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Holmstrm and Tirole_2024_Wrong-of-thought An integrated reasoning framework with multi-perspective verification and wrong in.pdf"
---

# Wrong-of-Thought: An Integrated Reasoning Framework with Multi-Perspective Verification and Wrong Information

> **저자**: Yongheng Zhang, Qiguang Chen, Jingxuan Zhou, Peng Wang, Jiasheng Si, Jin Wang, Wenpeng Lu, Libo Qin | **날짜**: 2024 | **DOI**: [arXiv:2410.04463](https://arxiv.org/abs/2410.04463)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: 기존 다중 사고 통합 방법(a)은 단일 검증만 사용하고 오류 정보를 활용하지 않는 반면, WoT(b)는 다중 관점 검증과 오류 정보 활용을 제공한다.*

대규모 언어 모델(LLM)의 추론 성능을 향상시키기 위해 다중 관점에서 검증하고 이전 오류 정보를 활용하는 WoT(Wrong-of-Thought) 프레임워크를 제안한다. 기존 XoT의 단일 검증 방식과 오류 정보 무시 문제를 해결하여 8개 데이터셋과 5개 LLM에서 우수한 성능을 달성했다.

## Motivation

- **Known**: Chain-of-Thought (CoT) 기반의 반복적 검증과 개선 방식이 LLM의 추론 성능을 향상시키고 있으며, XoT는 PoT, EoT, CoT를 통합하는 프레임워크로 이미 개발됨
  
- **Gap**: (1) 기존 방법들은 단순한 어설션(assertion) 검증만 사용하여 불완전한 검증을 수행함 (2) 오류 발생 시 오류 정보를 버리고 처음부터 재추론하므로 귀중한 피드백 신호를 손실함

- **Why**: 인간의 문제 해결 과정에서 실패는 학습의 중요한 원천이며, 다양한 관점의 검증과 과거 오류로부터의 학습이 추론 정확도를 향상시킬 수 있음

- **Approach**: (1) 어설션 검증, 프로세스 검증, 결과 검증의 3가지 관점으로 다중 검증 수행 (2) 이전 오류 정보를 현재 추론 문맥에 포함시켜 동일한 실수 반복 방지

## Achievement

![Figure 3](figures/fig3.webp)
*그림 3: WoT 프레임워크의 구조. 계획 및 풀이, 다중 관점 검증, 오류 정보 활용의 세 가지 핵심 모듈로 구성된다.*

1. **종합적 성능 향상**: 8개 벤치마크 데이터셋(GSM8K, GSM-Hard, Algebra, MultiArith 등)과 5개 LLM(Mistral-7B, Qwen-7B/14B, Gemini-1.0-Pro, GPT-3.5-Turbo)에서 모든 기존 베이스라인을 능가

2. **어려운 계산 문제 해결 능력**: 특히 복잡한 수학적 추론이 필요한 문제에서 탁월한 성능 입증

3. **오류 정보 활용의 효과성**: 잘못된 추론 정보를 다시 제시함으로써 LLM이 유사한 오류를 반복할 확률 감소

## How

![Figure 2](figures/fig2.webp)
*그림 2: XoT 프레임워크. 추론 방법 선택 후 어설션 검증을 통해 판단하고, 오류 시 다른 방법으로 전환하여 재시작한다.*

### 다중 관점 검증(Multi-Perspective Verification)

- **어설션 검증**: XoT의 기존 방식을 채용하여 중간 변수를 어설션 문장으로 형식화하고 외부 도구로 실행 검증

- **프로세스 검증**: 계산 결과를 제외한 추론 과정만 제시하여 LLM이 각 단계의 변수가 문제의 정보와 일대일로 대응되는지 확인하도록 유도

- **결과 검증**: 추론 과정과 계산 결과를 모두 제시한 후, 문제를 처음부터 다시 풀어서 결과의 일관성 검증

- **투표 메커니즘**: 식(1)을 통해 세 검증 방법의 결과 중 가장 일치도가 높은 판단을 최종 결과로 선택

$$\hat{V} = \arg\max_{V_t \in V} \sum_{t=1}^{N} \sum_{R \in M_i} \mathbb{1}(V_t = R)$$

### 오류 정보 활용(Wrong Information Utilization)

- 이전 추론에서 발생한 오류 정보를 현재 풀이 문맥에 포함시킴

- 식(2)로 표현되는 조건부 확률을 최대화하여 오류 정보 WI가 추가된 상태에서 최적의 추론 경로 R을 생성

$$\hat{R} = \arg\max_{R \in M_i} P(R|Q, I, WI)$$

- 재검증 후에도 오류 발생 시, 현재와 이전의 오류 정보를 모두 CoT 추론의 부정적 예시로 활용

## Originality

- **문제 정의의 명확성**: 단일 검증 방식의 한계와 오류 정보 무시라는 구체적인 문제점을 체계적으로 지적

- **다중 관점 검증의 설계**: 인간의 문제 해결 방식에 영감을 받아 어설션, 프로세스, 결과라는 세 가지 독립적 검증 관점 제시 및 투표 기반 통합

- **오류 정보의 적극적 활용**: 기존 폐기식 접근에서 오류를 학습 신호로 변환하는 패러다임 전환

- **광범위한 실험 검증**: 8개 데이터셋과 5개 LLM(오픈소스 및 클로즈드소스)에서 일관된 성능 개선 입증

## Limitation & Further Study

- **검증 오버헤드**: 세 가지 검증 방식을 모두 수행하므로 계산 비용이 증가하며, 추론 시간 대비 성능 향상의 효율성 분석 부재

- **투표 메커니즘의 한계**: 세 검증 방법 중 정확도가 상이할 수 있으나 동등한 가중치로 취급하는 문제 (가중 투표 방식 미검토)

- **오류 정보 표현의 단순성**: 오류 정보를 단순히 프롬프트에 추가하는 수준이며, 어떤 오류 특징이 가장 유효한지에 대한 분석 부족

- **도메인 확장성**: 주로 수학 추론 문제에 초점되어 있으며, 자연언어 추론이나 상식 추론 등 다른 도메인에서의 성능 미검증

- **후속 연구 방향**: (1) 검증 방식별 신뢰도 학습 및 적응형 가중치 적용 (2) 오류 분류 체계 구축 및 특정 오류 유형에 대한 최적화 (3) 다양한 도메인으로의 확장 실험


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: WoT는 단순하지만 효과적인 개선책을 통해 LLM의 추론 성능을 일관되게 향상시키며, 광범위한 실험으로 그 유효성을 입증했다. 다만 검증 오버헤드와 오류 정보 활용의 심화 방안에 대한 추가 연구가 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/243_Critique-GRPO_Advancing_LLM_Reasoning_with_Natural_Language/review]] — 자연어 비판을 통한 LLM 추론 개선 방법이 오류 정보 활용 접근법과 상호 보완적이다.
- 🏛 기반 연구: [[papers/833_Towards_reasoning_era_A_survey_of_long_chain-of-thought_for/review]] — 긴 사고 연쇄 추론에 대한 종합적 조사가 다중 관점 검증 프레임워크의 이론적 배경을 제공한다.
- 🔗 후속 연구: [[papers/482_Lean-star_Learning_to_interleave_thinking_and_proving/review]] — 형식 증명에서 잘못된 추론 단계를 감지하고 수정하는 통합 프레임워크로 Lean-star의 사고-증명 교차 학습을 보완한다.
