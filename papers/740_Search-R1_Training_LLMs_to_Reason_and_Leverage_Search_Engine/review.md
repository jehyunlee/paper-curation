---
title: "740_Search-R1_Training_LLMs_to_Reason_and_Leverage_Search_Engine"
authors:
  - "Bowen Jin"
  - "Hansi Zeng"
  - "Zhenrui Yue"
  - "Dong Wang"
  - "Hamed Zamani"
date: "2025"
doi: "10.48550/arXiv.2503.09516"
arxiv: ""
score: 4.2
essence: "강화학습(RL)을 통해 대언어모델(LLM)이 추론 과정 중 검색 엔진을 자동으로 호출하고 활용하는 방법을 학습하는 프레임워크 Search-R1을 제안하며, 기존 RAG 대비 최대 41%의 성능 향상을 달성한다."
tags:
  - "cat/Reinforcement_Learning_and_Self-Verification"
  - "sub/Search-Augmented_Language_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Jin et al._2025_Search-R1 Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning.pdf"
---

# Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning

> **저자**: Bowen Jin, Hansi Zeng, Zhenrui Yue, Dong Wang, Hamed Zamani | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2503.09516](https://doi.org/10.48550/arXiv.2503.09516)

---

## Essence

강화학습(RL)을 통해 대언어모델(LLM)이 추론 과정 중 검색 엔진을 자동으로 호출하고 활용하는 방법을 학습하는 프레임워크 Search-R1을 제안하며, 기존 RAG 대비 최대 41%의 성능 향상을 달성한다.

## Motivation

- **Known**: LLM은 복잡한 추론과 최신 정보 획득에 어려움을 겪으며, RAG와 검색 도구 활용 방식이 존재함
- **Gap**: 기존 프롬프팅 기반 접근은 일반화 성능이 낮고, 감독 학습 기반 방식은 고품질 데이터 확보가 어려우며, RL을 검색 상호작용에 적용할 때의 안정성, 다중 턴 상호작용, 보상 설계 문제가 해결되지 않음
- **Why**: LLM이 검색 엔진과의 상호작용을 최적화하는 방법을 학습할 수 없으면, 추론 과정에서 부적절한 검색 전략을 사용하게 됨
- **Approach**: RL(PPO/GRPO)에 검색 엔진을 환경의 일부로 모델링하고, 검색된 토큰에 대한 손실 마스킹, 다중 턴 상호작용 구조, 결과 기반 단순 보상 함수를 도입

## Achievement

![Figure 1](figures/fig1.webp)
*Figure 1: PPO와 GRPO에서 검색 엔진을 활용한 훈련 과정. 롤아웃 중 LLM은 검색 엔진과 다중 턴 상호작용 수행*

1. **성능 향상**: Qwen2.5-7B에서 기존 RAG 대비 평균 41% 상대 개선, Qwen2.5-3B에서 20% 개선 (7개 QA 데이터셋 평가)
2. **안정적 훈련**: 검색된 토큰의 손실 마스킹으로 RL 최적화 안정성 확보
3. **해석 가능성**: RL 방법 선택, LLM 모델 차이, 응답 길이 동역학에 대한 실증적 통찰 제공

## How

![Figure 2](figures/fig2.webp)
*Figure 2: PPO vs GRPO 수렴 비교*

**RL 객체 함수** (검색 엔진 통합):
- 정책 LLM πθ가 입력 x에서 검색 엔진 R과의 상호작용을 포함한 출력 y 샘플링
- KL 발산으로 참조 정책으로부터의 편향 제어

**핵심 기술**:
- **손실 마스킹**: 검색된 토큰(I(yt)=0)은 정책 그래디언트 계산에서 제외, LLM 생성 토큰만 최적화
- **PPO 적용**: 식 (2)에서 클리핑된 정책 비율을 사용한 제약된 목적 함수
  ```
  J_PPO(θ) = min(πθ/π_old · A, clip(πθ/π_old, 1-ε, 1+ε) · A)
  ```
- **GRPO 적용**: 그룹 상대 정책 최적화로 비평가 모델 제거, 그룹 점수에서 베이스라인 추정
- **토큰 구조**: `<search>` `</search>`로 검색 쿼리, `<information>` `</information>`으로 검색 결과, `<think>` `</think>`로 추론, `<answer>` `</answer>`로 최종 답변 감싸기
- **보상 함수**: 결과 기반 보상(rϕ)만 사용 (과정 기반 보상 미사용)

![Figure 3](figures/fig3.webp)
*Figure 3: 검색된 토큰 손실 마스킹 연구*

## Originality

- **검색 엔진의 환경 모델링**: 기존 RL에서 검색을 독립적 모듈로 취급했던 것과 달리, 환경의 일부로 통합하여 상호작용 학습 가능
- **손실 마스킹 기법**: 검색된 토큰 vs LLM 생성 토큰의 차별적 최적화로 안정성 확보 (기존 미해결 문제)
- **다중 턴 상호작용**: 단순 토큰 구조로 반복적 추론-검색 사이클 자동 관리
- **최소 보상 설계**: 복잡한 과정 기반 보상 없이 결과만으로 유의미한 검색 행동 학습 가능 입증
- **확장성**: PPO와 GRPO 모두 적용 가능한 일반적 프레임워크

## Limitation & Further Study

- **검색 품질의존성**: 기저 검색 엔진의 성능에 의존적이며, 저품질 검색 결과에 대한 강건성 미분석
- **보상 신호의 단순성**: 결과만으로 충분한지에 대한 이론적 분석 부족 (경험적 검증만 제시)
- **계산 비용**: RL 훈련 자체의 계산 오버헤드에 대한 상세 분석 미흡
- **다국어/특수 도메인 확대**: 영어 QA 중심 평가로, 다른 언어/도메인 일반화 불명확
- **검색 전략 다양성**: 동일한 쿼리에 대한 여러 검색 전략의 학습 가능성 미탐색

**후속 연구**:
- 동적 보상 함수 (과정 신호 혼합)
- 희귀 검색 쿼리 또는 어려운 질문에 대한 특화된 훈련
- 검색 엔진 선택 및 조합 학습

## Evaluation

- **Novelty**: 4.5/5 
  - 검색과 RL의 통합은 신선하고, 손실 마스킹 기법도 실용적이나, 개별 요소는 기존 기술의 조합
  
- **Technical Soundness**: 4/5
  - 수학적 공식화는 명확하고 구현 기술도 타당하나, 손실 마스킹의 이론적 정당성 부족
  
- **Significance**: 4.5/5
  - RAG 성능 향상은 실질적이고, 다양한 QA 벤치마크에서 검증되었으나, 실제 적용 비용과 한계가 불명확
  
- **Clarity**: 4/5
  - 전반적으로 명확한 설명과 구체적 사례 제시, 다만 일부 기호 정의와 전체 알고리즘 플로우 상세화 필요
  
- **Overall**: 4.2/5

**총평**: Search-R1은 검색 엔진 호출을 RL 최적화에 체계적으로 통합한 실용적 프레임워크로, 강력한 실험 결과와 구현 상세함이 강점이나, 이론적 깊이와 계산 효율성에 대한 추가 분석이 요구된다.

## Related Papers

- 🔄 다른 접근: [[papers/667_ReSearch_Learning_to_Reason_with_Search_for_LLMs_via_Reinfor/review]] — 두 논문 모두 검색 기반 추론을 다루되 Search-R1은 검색 엔진 활용, ReSearch는 다중홉 질문 답변에 특화되어 있다.
- 🔗 후속 연구: [[papers/873_WebThinker_Empowering_Large_Reasoning_Models_with_Deep_Resea/review]] — WebThinker의 웹 탐색 능력은 Search-R1의 검색 엔진 활용을 더 동적이고 상호작용적인 정보 수집으로 발전시킨다.
- 🏛 기반 연구: [[papers/675_Retrieval-Augmented_Generation_for_Knowledge-Intensive_NLP_T/review]] — 검색 증강 생성 서베이는 Search-R1의 강화학습 기반 검색 통합 방법론에 RAG 시스템의 이론적 배경과 설계 원칙을 제공한다.
- 🔄 다른 접근: [[papers/873_WebThinker_Empowering_Large_Reasoning_Models_with_Deep_Resea/review]] — 두 논문 모두 추론 과정에서의 검색 통합을 다루되 WebThinker는 웹 탐색, Search-R1은 검색 엔진 활용에 특화되어 있다.
- 🔄 다른 접근: [[papers/667_ReSearch_Learning_to_Reason_with_Search_for_LLMs_via_Reinfor/review]] — 두 논문 모두 강화학습 기반 검색을 다루되 ReSearch는 다중홉 질문 답변, Search-R1은 검색 엔진과의 통합에 특화되어 있다.
- 🔗 후속 연구: [[papers/296_Dynamic_Search_for_Inference-Time_Alignment_in_Diffusion_Mod/review]] — Search-R1의 검색 기반 추론이 확산 모델의 동적 탐색 과정에서 더 효과적인 빔 폭 조정을 가능하게 함
- 🔄 다른 접근: [[papers/281_Dlpo_Towards_a_robust_efficient_and_generalizable_prompt_opt/review]] — 검색 엔진 활용 LLM 훈련과 프롬프트 최적화의 다른 성능 향상 접근법
- 🔄 다른 접근: [[papers/842_Tree-planner_Efficient_close-loop_task_planning_with_large_l/review]] — 강화학습 기반 검색 및 추론 훈련으로 계획 수립의 다른 접근 방식을 보여준다.
