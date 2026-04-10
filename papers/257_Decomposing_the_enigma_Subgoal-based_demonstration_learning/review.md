---
title: "257_Decomposing_the_enigma_Subgoal-based_demonstration_learning"
authors:
  - "Xueliang Zhao"
  - "Wenda Li"
  - "Lingpeng Kong"
date: "2023"
doi: "10.48550/arXiv.2305.16366"
arxiv: ""
score: 4.2
essence: "대형 언어 모델(LLM)을 형식 정리 증명(formal theorem proving)에 활용할 때, 시연 예제의 구조화와 조직화 방식을 개선함으로써 증명 성공률을 38.9%에서 45.5%로 향상시키는 부분목표 기반 학습 프레임워크를 제안한다."
tags:
  - "cat/Reinforcement_Learning_and_Self-Verification"
  - "sub/Autonomous_Agent_Learning_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhao et al._2023_Decomposing the enigma Subgoal-based demonstration learning for formal theorem proving.pdf"
---

# Decomposing the enigma: Subgoal-based demonstration learning for formal theorem proving

> **저자**: Xueliang Zhao, Wenda Li, Lingpeng Kong | **날짜**: 2023 | **DOI**: [10.48550/arXiv.2305.16366](https://doi.org/10.48550/arXiv.2305.16366)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: 왼쪽은 비형식적 증명과 부분목표 기반 증명의 예시, 오른쪽은 확산 모델을 사용한 시연 예제의 최적 부분집합과 순서 결정*

대형 언어 모델(LLM)을 형식 정리 증명(formal theorem proving)에 활용할 때, 시연 예제의 구조화와 조직화 방식을 개선함으로써 증명 성공률을 38.9%에서 45.5%로 향상시키는 부분목표 기반 학습 프레임워크를 제안한다.

## Motivation

- **Known**: 최근 LLM이 형식 정리 증명 분야에서 진전을 이루었으며, 비형식적 증명 초안과 형식 스케치 생성의 두 단계 과정을 통해 작동한다. 이 과정에서 시연 예제의 품질이 핵심이다.

- **Gap**: 기존 연구는 시연 예제의 포맷과 조직화 방식에 대해 충분히 탐구하지 않았다. 특히 형식 정리 증명의 길이 제약으로 인해 매우 제한된 수의 시연 예제만 포함할 수 있으며, 예제의 선택과 순서가 성능에 미치는 영향이 미흡하게 다루어졌다.

- **Why**: 강화학습 및 로보틱스 분야의 부분목표 학습(subgoal learning) 이론에 따르면, 복잡한 작업을 작고 균일한 부분목표로 분해하면 학습 효율이 향상된다. 또한 NP-완전 문제인 시연 예제 조직화 문제를 최근 성공적으로 적용되고 있는 확산 모델로 해결할 수 있다.

- **Approach**: (1) 비형식적 증명을 부분목표 기반 증명으로 재구조화하고 ChatGPT와의 반복적 상호작용을 통해 정제, (2) 확산 모델을 훈련하여 시연 예제의 최적 부분집합과 순서를 동시에 결정

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: miniF2F-test에서 문제 해결 수 vs LLM 호출 횟수*

1. **성능 향상**: miniF2F 벤치마크에서 45.5% 통과율 달성 (이전 SOTA 38.5% 대비 6.6% 절대 개선, 17.0% 상대 개선)

2. **샘플링 효율 5배 향상**: 확산 모델을 통한 시연 조직화로 이전 SOTA 수준(38.5%)을 100회 대신 20회의 LLM 호출로 달성

## How

![Figure 3](figures/fig3.webp)
*그림 3: 제안된 방법으로 생성한 형식 스케치*

**부분목표 기반 증명 구성:**
- 수동 작성된 비형식적 증명으로부터 시작하여 초기 부분목표 집합 생성
- 각 부분목표가 초기 상태(statement)와 최종 상태(증명 통과) 모두에서 도달 가능한지 검증
- 자동 정리 보조기(proof assistant)를 재귀적으로 호출하여 부분목표의 유효성 확인 및 반복 정제
- k번의 반복을 통해 부분목표의 스타일 일관성 개선

**확산 모델 기반 시연 조직화:**
- 문제를 그래프상의 (부분)해밀턴 경로 찾기로 공식화 (노드=시연 예제, 경로=선택 및 순서)
- 증명 성공한 시연 예제 조직을 훈련 데이터로 수집
- 그래프 신경망(GNN)을 이용한 이산 확산 모델(discrete diffusion model) 훈련
- 조건부 분포 p_θ(ψ₀|x)를 학습하여 주어진 정리 문장 x에 대한 최적 조직 예측
- 추론 시 병렬 처리 가능하여 계산 효율성 향상

## Originality

- **부분목표 학습 이론의 정리 증명 적용**: 강화학습 분야의 잘 알려진 원칙(subgoal learning)을 형식 정리 증명 도메인에 처음 체계적으로 적용하여 증명 구조를 세분화

- **확산 모델을 통한 시연 조직화**: NP-완전 문제인 시연 예제 선택과 순서 결정을 확산 모델로 동시에 해결하는 창의적 접근. 그래프 레벨에서의 이산 확산 모델 적용은 이 문제에 특화된 설계

- **반복적 검증 기반 정제**: 증명 보조기의 피드백을 활용한 자동 부분목표 정제 알고리즘은 인간 개입을 최소화하면서도 품질을 보장

## Limitation & Further Study

- **부분목표 구성의 초기화 문제**: 초기 부분목표는 여전히 수동으로 작성되어야 하며, ChatGPT의 부분적 자동화도 완전히 독립적이지 않음

- **확산 모델 훈련 데이터**: 성공 사례만 훈련 데이터로 사용하므로, 실패 경로로부터의 학습 신호가 부재. 부정 사례를 포함한 학습 방식 탐색 필요

- **도메인 특이성**: miniF2F 벤치마크에 특화된 평가이므로, 다른 정리 증명 환경(Coq, Lean 등)이나 대규모 수학 문제로의 일반화 가능성 미확인

- **확산 모델의 해석성**: 확산 모델이 학습한 시연 선택 및 순서화 원칙에 대한 해석적 분석 부재

- **문맥 길이 제약**: 3072 토큰 제약 하에서 평균 4.79개 예제만 포함 가능. 더 긴 문맥을 활용하는 새로운 모델이나 압축 기법 탐색 필요


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.2/5

**총평**: 형식 정리 증명에서 LLM의 효율성을 높이기 위해 부분목표 분해와 확산 모델 기반 시연 조직화라는 두 가지 창의적 접근을 결합한 우수한 연구이다. 실증적 성과(45.5%)가 의미 있으며, 반복적 검증 기반의 부분목표 정제 알고리즘은 자동화 수준을 높인 점이 인정된다. 다만 초기 부분목표의 수동 구성, 확산 모델 학습 데이터의 제약성, 그리고 miniF2F에 국한된 평가는 일반화 가능성에 대한 의문을 남긴다. 추가로 확산 모델의 의사결정 원리에 대한 심층 분석과 다양한 정리 증명 환경으로의 확장이 향후 연구로 기대된다.

## Related Papers

- 🔄 다른 접근: [[papers/484_Learning_to_generate_research_idea_with_dynamic_control/review]] — 두 논문 모두 연구 방법론 개선을 다루되 형식 정리 증명은 구조화된 시연, 연구 아이디어 생성은 동적 제어에 초점을 맞춘다.
- 🔗 후속 연구: [[papers/264_Deepseek-prover_Advancing_theorem_proving_in_llms_through_la/review]] — DeepSeek-Prover의 대규모 언어모델 정리 증명은 부분목표 기반 시연 학습을 LLM 기반 자동 증명 시스템으로 확장한다.
- 🏛 기반 연구: [[papers/288_Draft_sketch_and_prove_Guiding_formal_theorem_provers_with_i/review]] — 형식 정리 증명에서의 초안-스케치-증명 가이드 방법론은 부분목표 기반 시연 학습의 구조화된 증명 과정 설계에 이론적 근거를 제공한다.
