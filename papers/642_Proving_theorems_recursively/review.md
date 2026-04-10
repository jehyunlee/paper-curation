---
title: "642_Proving_theorems_recursively"
authors:
  - "Haiming Wang"
  - "Huajian Xin"
  - "Zhengying Liu"
  - "Wenda Li"
  - "Yinya Huang"
date: "2024"
doi: "arXiv:2405.14414"
arxiv: ""
score: 4.2
essence: "신경망 기반 자동 정리 증명(automated theorem proving)에서 기존의 단계적(step-by-step) 탐색 방식의 한계를 극복하기 위해, 본 논문은 **POETRY(PrOvE Theorems RecursivelY)**를 제안한다. 이는 Isabelle 정리 증명기에서 재귀적이고 계층적 접근을 통해 증명을 단계적으로 구성하는 방법으로, 중간 명제들의 증명을 `sorry` 플레이스홀더로 미루고 더 깊은 레벨에서 해결하는 방식이다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Formal_Theorem_Proving"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Boyer and Moore_2024_Proving theorems recursively.pdf"
---

# Proving Theorems Recursively

> **저자**: Haiming Wang, Huajian Xin, Zhengying Liu, Wenda Li, Yinya Huang, Jianqiao Lu, Zhicheng Yang, Jing Tang, Jian Yin, Zhenguo Li, Xiaodan Liang | **날짜**: 2024 | **DOI**: [arXiv:2405.14414](https://arxiv.org/abs/2405.14414)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: 단계적 증명과 재귀적 증명의 비교. (a) 단계적 접근은 증명의 계층 구조를 무시하고 증명 단계들의 시퀀스로만 취급. (b) 재귀적 증명은 검증 가능한 증명 스케치를 여러 레벨로 분해하여 단계별로 중간 명제 증명을 미루는 방식으로 진행.*

신경망 기반 자동 정리 증명(automated theorem proving)에서 기존의 단계적(step-by-step) 탐색 방식의 한계를 극복하기 위해, 본 논문은 **POETRY(PrOvE Theorems RecursivelY)**를 제안한다. 이는 Isabelle 정리 증명기에서 재귀적이고 계층적 접근을 통해 증명을 단계적으로 구성하는 방법으로, 중간 명제들의 증명을 `sorry` 플레이스홀더로 미루고 더 깊은 레벨에서 해결하는 방식이다.

## Motivation

- **Known**: 신경언어모델과 탐색 알고리즘을 결합한 신경 정리 증명이 최근 많은 진전을 이루었으며, 대부분의 방법들은 로그확률이나 가치함수 점수 같은 근시안적(short-sighted) 휴리스틱을 기반으로 함.

- **Gap**: 기존 단계적 증명 방법들은 (1) 근시안적 휴리스틱으로 인해 최적이 아닌 또는 산만한 부분목표(subgoal)를 탐색하여 긴 증명을 찾기 어렵고, (2) 증명 길이 증가에 따른 기하급수적 탐색공간 확장에 대응할 정확한 휴리스틱이 부족함.

- **Why**: 정리 증명의 계층적 구조(hierarchical structure)를 활용하면 복잡한 문제를 관리 가능한 부분 문제로 분해할 수 있고, 각 레벨에서 검증 가능한 증명 스케치를 먼저 확보하면 탐색 효율이 크게 향상될 것으로 예상됨.

- **Approach**: Isabelle의 `sorry` 타틱을 활용하여 중간 명제의 증명을 임시로 건너뛰고, 각 레벨에서 검증 가능한 증명 스케치를 먼저 탐색한 후, 다음 레벨에서 미뤄진 명제들을 재귀적으로 증명하는 방식.

## Achievement

![Figure 3](figures/fig3.webp)
*그림 3: POETRY와 GPT-f 기준선 간 증명 길이 비교. y축은 로그 스케일로 표시.*

1. **정량적 성능 향상**: miniF2F 데이터셋에서 평균 5.1% 절대 개선율 달성 (42.2% 통과율), PISA 데이터셋에서 재귀적 증명을 통해 단계적 기준선 대비 3.9% 절대 개선.

2. **증명 길이 대폭 확장**: 최대 증명 길이가 단계적 방식의 10단계에서 262단계로 증가 (miniF2F 기준), PISA에서도 26단계로 확장. 이는 더 복잡한 정리들을 증명할 수 있음을 시사.

3. **재귀적 구조의 이점**: 거짓 중간 명제를 포함한 검증된 스케치도 다음 레벨에서 증명 불가능할 때 새로운 스케치 탐색으로 자동 보정되어, 강건한 탐색 프레임워크 구성.

## How

![Figure 2](figures/fig2.webp)
*그림 2: 재귀적 BFS(Best-First Search) 탐색의 상세 예시. 증명 트리의 각 노드는 증명 상태(proof state)를 나타냄.*

- **증명 스케치 추출(Proof Sketch Extraction)**: 기존 완전 증명(complete proof)의 데이터에서 Isabelle의 `proof level` 정보를 활용하여 계층 구조를 추출. Algorithm 1의 `EXTRACTPROOFSKETCH` 함수가 증명 단계들을 재귀적으로 처리하며, 깊이가 증가하는 지점에서 `sorry`로 중간 증명을 대체.

- **재귀적 데이터 구성**: 각 완전 증명으로부터 다중 레벨의 증명 스케치들을 추출하여 훈련 데이터 구성. 이를 통해 언어모델이 각 레벨에서 스케치를 생성하는 법을 학습.

- **재귀적 탐색 알고리즘**: BFS 기반 탐색에서 (1) 목표 정리/중간 명제에 대해 검증 가능한 스케치를 먼저 탐색, (2) 스케치 내 모든 `sorry`를 해결할 때까지 다음 레벨의 명제들에 대해 동일한 재귀적 탐색 수행.

- **언어모델 활용**: 표준 GPT-f 형식의 사전훈련 언어모델 사용. 입력으로 컨텍스트와 현재 증명 상태를 받아 다음 증명 단계(또는 증명 스케치)를 샘플링.

## Originality

- **계층적 재귀 구조의 도입**: 정리 증명에 증명 레벨이라는 자연스러운 계층 구조를 체계적으로 활용한 최초의 신경 증명 방법. 기존 방법들이 증명을 일렬의 단계들로만 취급한 것과 대비.

- **근시안성 극복**: 근시안적 휴리스틱 대신, 각 레벨에서 검증 가능한 스케치(complete outline)를 찾음으로써 더 정보 풍부한 신호를 제공하는 새로운 탐색 패러다임.

- **데이터 재구성 방법론**: 기존 완전 증명으로부터 자동으로 다중 레벨 증명 스케치를 추출하는 알고리즘 제시. 기존 증명 데이터를 효율적으로 재활용.

- **`sorry` 타틱의 창의적 활용**: Isabelle의 기본 기능인 `sorry`를 신경 증명의 핵심 메커니즘으로 재해석. 이를 통해 거짓 중간 명제의 경우 자동으로 다시 탐색하는 자정(self-correction) 메커니즘 구현.

## Limitation & Further Study

- **거짓 명제의 불완전한 처리**: 검증된 스케치가 거짓 중간 명제를 포함할 경우, 다음 레벨에서 증명 불가능할 때까지 깨닫지 못함. 사전에 명제 올바름을 검증하는 메커니즘 부재.

- **Isabelle에 한정된 구현**: 현재 Isabelle의 `proof level`과 `sorry` 타틱에 강하게 의존. Lean, Coq, HOL 등 다른 형식 환경으로의 확장은 추가 공학적 노력이 필요하며, 저자들도 이를 향후 과제로 명시.

- **언어모델 크기/능력 의존성 미분석**: 재귀적 접근의 이점이 언어모델 크기나 사전훈련 데이터에 얼마나 민감한지 상세 분석 부족. 소형 모델에서의 성능은 미검증.

- **계산 비용 분석 부재**: 재귀적 탐색이 더 긴 증명을 찾는 대신, 탐색 비용(GPU시간, 탐색 노드 수)이 얼마나 증가하는지에 대한 정량 분석 미제시.

- **다른 형식 환경과의 비교 필요**: Lean 기반의 최신 신경 정리 증명 방법들과의 직접 비교 없음. 재귀적 접근의 일반성에 대한 의문 존재.

## Evaluation

- **Novelty**: 4.5/5
  - 정리 증명에 재귀적 계층 구조를 명확히 도입한 참신한 아이디어. 다만 `sorry`의 활용은 형식 환경의 기존 기능에 가까움.

- **Technical Soundness**: 4/5
  - Algorithm 1의 증명 스케치 추출 알고리즘은 명확하고 구현 가능함. 거짓 명제에 대한 자정 메커니즘은 경험적 증거에 의존하며, 이론적 보장 부족.

- **Significance**: 4.5/5
  - 정리 증명의 증명 길이를 26배 확장하고, 여러 데이터셋에서 SOTA 대비 5%+ 개선은 상당한 성과. 다만 절대 통과율(42%)은 여전히 낮으며, 실무 적용 가능성은 미지수.

- **Clarity**: 4/5
  - 논문 구조와 주요 아이디어는 명확하게 표현. 그림 1(b)의 예시는 직관적. 다만 거짓 명제 처리와 탐색 비용 등 일부 중요 세부사항 설명 부족.

- **Overall**: 4.2/5

**총평**: POETRY는 형식 증명의 자연스러운 계층 구조를 처음 체계적으로 활용하여 근시안적 단계적 탐색의 한계를 극복한 창의적 방법이다. 특히 증명 길이 확장과 SOTA 성능 달성은 주목할 만하나, 거짓 명제 사전 검증 부재, 계산 비용 분석 미흡, Isabelle 의존성 등의 한계가 있으며, 다른 형식 환경으로의 일반성 입증이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/1095_Towards_large_language_models_as_copilots_for_theorem_provin/review]] — Lean Copilot의 인간-AI 협업 접근과 달리 완전 자동화된 재귀적 증명 방식 추구
- 🧪 응용 사례: [[papers/030_A_survey_on_deep_learning_for_theorem_proving/review]] — 정리 증명에 대한 심층학습 기법 서베이에서 제시된 방법론을 재귀적 접근으로 구현
- 🏛 기반 연구: [[papers/617_Phi-4_technical_report/review]] — 수학적 추론에 강한 Phi-4의 능력을 정리 증명 자동화에 활용할 수 있는 기반
- 🔗 후속 연구: [[papers/379_Generative_language_modeling_for_automated_theorem_proving/review]] — 생성형 언어모델 기반 정리 증명을 재귀적 계층 구조로 발전시킨 확장 연구
- 🔗 후속 연구: [[papers/807_Theoremexplainagent_Towards_video-based_multimodal_explanati/review]] — TheoremExplainAgent의 비디오 기반 설명 생성을 재귀적 정리 증명으로 확장하여 더 체계적이고 단계적인 수학 학습 환경을 조성할 수 있다.
- 🔗 후속 연구: [[papers/379_Generative_language_modeling_for_automated_theorem_proving/review]] — GPT-f의 정리 증명 기법을 재귀적 증명 방법론으로 확장한 연구
- 🧪 응용 사례: [[papers/617_Phi-4_technical_report/review]] — 수학적 추론에 특화된 Phi-4의 능력을 정리 증명 작업에 활용하는 응용
- 🏛 기반 연구: [[papers/030_A_survey_on_deep_learning_for_theorem_proving/review]] — 정리 증명 심층학습 기법들을 재귀적 증명 방법론으로 발전시킨 이론적 기반
- 🔄 다른 접근: [[papers/1095_Towards_large_language_models_as_copilots_for_theorem_provin/review]] — 완전 자동화된 재귀적 증명과 달리 인간 수학자와 AI의 협업을 통한 증명 보조 접근
- 🔄 다른 접근: [[papers/489_Lf_a_foundational_higher-order-logic/review]] — 둘 다 정리 증명의 논리적 기반을 다루지만 하나는 과학 형식화를 위한 고차 논리 체계에, 다른 하나는 재귀적 정리 증명에 초점을 맞춘다.
