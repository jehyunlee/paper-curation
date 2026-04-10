---
title: "743_Self-critique_guided_iterative_reasoning_for_multi-hop_quest"
authors:
  - "Zheng Chu"
  - "Haiming Fan"
  - "Jingchang Chen"
  - "Qianyu Wang"
  - "Mingda Yang"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "대규모 언어모델(LLM)의 지식 제한 문제를 해결하기 위해, 자기비판 피드백을 통해 반복적 추론 과정을 유도하는 새로운 다중 홉 질의응답 방법을 제안한다. 모델이 질문 분해, 검색, 추론, 자기평가를 학습하여 중간 단계의 오류를 줄이고 최적 추론 경로를 선택할 수 있도록 한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Scientific_Question_Answering"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chu et al._2025_Self-critique guided iterative reasoning for multi-hop question answering.pdf"
---

# Self-critique guided iterative reasoning for multi-hop question answering

> **저자**: Zheng Chu, Haiming Fan, Jingchang Chen, Qianyu Wang, Mingda Yang, Jiafeng Liang, Zhongjie Wang, Hao Li, Guoan Tang, Ming Liu, Bing Qin | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: 다중 홉 질의응답에서 반복적 검색과 자기비판 유도 추론의 비교. 제안 방법은 반복적 추론 중 자기비판을 통합하고 피드백에 기반한 탐색을 수행함*

대규모 언어모델(LLM)의 지식 제한 문제를 해결하기 위해, 자기비판 피드백을 통해 반복적 추론 과정을 유도하는 새로운 다중 홉 질의응답 방법을 제안한다. 모델이 질문 분해, 검색, 추론, 자기평가를 학습하여 중간 단계의 오류를 줄이고 최적 추론 경로를 선택할 수 있도록 한다.

## Motivation

- **Known**: LLM은 Chain-of-Thought 프롬프팅으로 강한 추론 능력을 보이지만, 지식 집약적 작업에서는 사실 정확성이 낮다. 단일 검색은 다중 홉 질의응답에 불충분하며, 기존 반복적 검색이나 분해 기반 방법도 한계가 있다.

- **Gap**: (1) 초기 질문 분해 오류가 후속 추론을 왜곡함, (2) 반복적 검색은 복잡한 문제 계획이 부족하여 부정확한 검색 발생, (3) 중간 단계 지도 부재로 오류 증폭(cascading error) 발생

- **Why**: 다중 홉 질의응답의 정확성 향상을 위해서는 반복적 질문 분해를 통한 단계적 계획과 중간 추론 단계의 품질 피드백이 필수적이다.

- **Approach**: 자기비판 모듈(critic model)이 검색 적절성, 추론 유용성, 전체 품질을 평가하는 보상을 생성하고, 이를 통해 훈련 중 감독 신호를 제공하고 추론 중 최적 경로를 선택하도록 한다.

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: SiGIR의 전체 구조. (I) 자기비판 기능을 가진 반복적 추론기 학습 과정, (II) 질문 분해/검색/추론/평가를 포함한 SC-Reasoner의 특성, (III) 탐색과 보상 기반 탐색을 통한 최적 경로 선택*

1. **성능 향상**: HotpotQA, 2WikiMQA, MuSiQue 세 데이터셋에서 평균 8.6% 성능 향상(SOTA 대비), DeepSeek-V2.5, Mistral, LLaMA2, Qwen2.5 모델에서 일관된 개선

2. **효율성과 비용**: Monte Carlo Tree Search 같은 고비용 탐색 방법 대비 계산 오버헤드를 줄이면서도 추론 확장(inference-time scaling) 효과 달성

## How

- **훈련 레시피**:
  - 단계 1: 고급 LLM의 few-shot 프롬프트로 반복적 추론 궤적 합성(질문 분해, 부분질문 추론)
  - 단계 2: 작은 모델을 critic 역할로 학습하여 검색 적절성(Relevant/Partially Relevant/Irrelevant), 추론 유용성(Useful/Partially Useful/Useless), 전체 품질 평가
  - 단계 3: 합성된 궤적에 자기비판 신호를 추가하여 SC-Reasoner(Rsc) 학습

- **추론 과정**:
  - 반복적 질문 분해: 비원자적(non-atomic) 질문을 원자적 부분질문으로 단계적 분해
  - 자기비판 유도 검색: 각 부분질문에 대해 여러 문서 검색 후 관련성 평가
  - 자기비판 유도 추론: 검색된 문서로부터 추론하며 유용성 평가
  - 빔 서치: 누적 보상이 높은 상위 K개 경로만 유지하며 탐색
  - 반복 종료: 모든 부분질문 해결 후 누적 보상이 최고인 궤적 선택

## Originality

- **자기비판의 다층적 적용**: 검색 품질, 추론 품질, 전체 품질을 구별하여 세분화된 피드백 제공하는 점에서 기존 검색증강생성(RAG) 방법과 차별화

- **반복적 분해의 유연성**: 초기 전체 분해 대신 단계별 분해로 오류 누적 문제 완화

- **비용 효율적 탐색**: 시뮬레이션 기반 MCTS 대신 학습된 보상으로 유도된 빔 서치로 추론 시간 확장을 효율적으로 구현

- **엔드-투-엔드 학습**: 분해, 검색, 추론, 자기평가, 질문 축소 능력을 통합적으로 학습하는 통일된 모델 구성

## Limitation & Further Study

- **critic 모델의 일반화**: 특정 데이터셋으로 학습한 critic 모델이 도메인 간 이전 가능성에 대한 분석 부족

- **보상 신호의 정확성**: LLM 기반 합성 데이터의 품질이 최종 성능에 미치는 영향에 대한 상세 분석 필요

- **장기 추론**: 5홉 이상의 매우 긴 추론 체인에서의 성능 확장성 미검증

- **후속 연구**: (1) 다중 모달 질의응답으로의 확장, (2) 동적 보상 조정 메커니즘, (3) 도메인 적응 critic 학습 전략 개발

## Evaluation

- **Novelty**: 4/5 — 자기비판의 세분화된 적용과 반복적 분해는 신선하지만, 검색증강과 빔 서치 자체는 기존 기법의 조합

- **Technical Soundness**: 4.5/5 — 훈련 및 추론 파이프라인이 명확하고 실험 설계가 체계적이며, 합성 데이터 생성 프로세스가 신중함

- **Significance**: 4.5/5 — 8.6% 성능 향상과 세 데이터셋에서의 일관된 개선은 실질적 의의를 가지며, 지식 집약적 추론 문제의 중요성을 감안하면 높은 가치

- **Clarity**: 4/5 — 전체 구조와 방법론이 명확히 설명되었으나, critic 데이터 구성 및 보상 점수 계산 세부사항이 본문에 부족

- **Overall**: 4.2/5

**총평**: 자기비판 피드백을 다층적으로 활용한 반복적 추론 프레임워크는 다중 홉 질의응답에서 실질적 성능 향상을 달성했으며, 특히 중간 단계 오류 제어와 효율적 탐색 측면에서 기여도가 높다. 다만 critic 모델의 일반화 능력과 극단적 복잡성 시나리오에서의 확장성에 대한 추가 분석이 요구된다.

## Related Papers

- 🏛 기반 연구: [[papers/701_Scholarchemqa_Unveiling_the_power_of_language_models_in_chem/review]] — 도메인 특화 QA의 기초적 접근이 자기비판 기반 반복적 추론이라는 더 고도화된 질의응답 방법의 토대를 제공함
- 🔄 다른 접근: [[papers/242_CRITIC_Large_Language_Models_Can_Self-Correct_with_Tool-Inte/review]] — 둘 다 LLM의 자기교정 능력을 다루지만 하나는 질의응답, 다른 하나는 도구 통합 추론에 중점을 둠
- 🔗 후속 연구: [[papers/667_ReSearch_Learning_to_Reason_with_Search_for_LLMs_via_Reinfor/review]] — 기본적인 추론 학습을 검색과 강화학습을 통한 더 체계적인 추론 능력 향상 방법으로 확장함
- 🔗 후속 연구: [[papers/701_Scholarchemqa_Unveiling_the_power_of_language_models_in_chem/review]] — 화학 도메인의 특화된 QA를 다중 홉 질의응답의 일반적 추론 방법으로 확장하여 더 복잡한 추론 과정을 다룸
