---
title: "028_A_survey_of_reasoning_with_foundation_models"
authors:
  - "Jiankai Sun"
  - "Chuanyang Zheng"
  - "Enze Xie"
  - "Zhengying Liu"
  - "Ruihang Chu"
date: "2023"
doi: ""
arxiv: ""
score: 4.0
essence: "파운데이션 모델(Foundation Models)의 추론(Reasoning) 능력을 체계적으로 조사한 종합 서베이로, 다양한 추론 작업, 방법론, 벤치마크를 다루고 멀티모달 학습, 자율 에이전트, 슈퍼 정렬과의 연관성을 논의한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Knowledge_Graph_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Sun et al._2023_A survey of reasoning with foundation models.pdf"
---

# A survey of reasoning with foundation models

> **저자**: Jiankai Sun, Chuanyang Zheng, Enze Xie, Zhengying Liu, Ruihang Chu, Jianing Qiu, Jiaqi Xu, Mingyu Ding, Hongyang Li, Mengzhe Geng, Yue Wu, Wenhai Wang, Junsong Chen, Zhangyue Yin, Xiaozhe Ren, Jie Fu, Junxian He, Wu Yuan, Qi Liu, Xihui Liu | **날짜**: 2023 | **URL**: [https://arxiv.org/abs/2312.11562](https://arxiv.org/abs/2312.11562)

---

## Essence

![Figure 2](figures/fig2.webp)

*Fig. 2: Left: Overview of the reasoning tasks introduced in this survey, as detailed*

파운데이션 모델(Foundation Models)의 추론(Reasoning) 능력을 체계적으로 조사한 종합 서베이로, 다양한 추론 작업, 방법론, 벤치마크를 다루고 멀티모달 학습, 자율 에이전트, 슈퍼 정렬과의 연관성을 논의한다.

## Motivation

- **Known**: 파운데이션 모델은 자연어처리, 컴퓨터 비전, 멀티모달 작업에서 탁월한 성능을 보였으나, 인간과 같은 추론 능력을 보유했는지에 대한 의문이 존재했다. 기존 서베이들은 파운데이션 모델의 응용 잠재력을 다양한 관점에서 탐색했다.
- **Gap**: 멀티모달 및 상호작용 추론에 중점을 둔 체계적이고 포괄적인 서베이가 부족했으며, 인간 추론 스타일을 더 밀접하게 모방하는 최근 발전을 종합적으로 다루는 자료가 필요했다.
- **Why**: 추론은 복잡한 문제 해결, 협상, 의료 진단, 범죄 수사 등 실제 응용에서 필수적이며, AGI(Artificial General Intelligence) 개발의 기본 방법론으로서 매우 중요하다.
- **Approach**: 다양한 추론 작업(상식추론, 수학추론, 논리추론, 인과추론 등)과 기술(사전학습, 파인튜닝, 정렬 학습, 맥락 내 학습, 자율 에이전트)을 체계적으로 분류하고, 관련 벤치마크와 데이터셋을 정리하여 포괄적인 지식 기반을 제공한다.

## Achievement

![Figure 5](figures/fig5.webp)

*Fig. 5: Taxonomy of Reasoning Tasks with Foundation Models. Only the representa-*

- **광범위한 추론 작업 분류**: 상식추론, 수학추론, 논리추론, 인과추론, 시각추론, 오디오추론, 멀티모달추론, 에이전트 추론 등 10개 이상의 주요 범주로 체계화
- **파운데이션 모델 기술 체계화**: 사전학습, 파인튜닝, 정렬 학습, MoE(Mixture of Experts), 맥락 내 학습, Chain-of-Thought 등 핵심 기술 방법론 정리
- **풍부한 벤치마크 및 데이터셋 수집**: 각 추론 작업별로 대표적인 벤치마크, 데이터셋, 평가 지표를 상세히 제시
- **미래 연구 방향 제시**: 안전성/개인정보, 해석 가능성, 자율 언어 에이전트, 과학을 위한 추론, 슈퍼 정렬 등 향후 중요 과제 제안
- **지속적 자료 업데이트**: GitHub 저장소를 통해 추론 관련 논문 및 벤치마크를 지속적으로 갱신하는 살아있는 자료 제공

## How

![Figure 3](figures/fig3.webp)

*Fig. 3: Foundation models can be mainly categorized into language, vision, and*

- 추론을 연역(Deductive), 귀납(Inductive), 귀납적(Abductive) 추론으로 분류하고 수학적 표현 제시
- 언어 파운데이션 모델, 비전 파운데이션 모델, 멀티모달 파운데이션 모델의 특징과 프롬프팅 방법 설명
- 각 추론 작업별로 정의, 하위 범주, 관련 응용 사례를 계층적으로 구조화
- 사전학습의 데이터 소스와 네트워크 아키텍처, 파인튜닝의 파라미터 효율적 방법론 상세 분석
- In-context Learning의 시연 예시 선택, Chain-of-Thought 프롬프팅, 다중 라운드 프롬프팅 기법 검토
- 자율 에이전트의 introspective, extrospective, embodied, 다중 에이전트 추론 형태 분류
- 도전 과제, 한계, 위험성에 대한 비판적 논의 제시

## Originality

- 기존 서베이와 달리 **멀티모달 추론**과 **상호작용 추론(interactive reasoning)**을 중심적으로 다루어 최근 발전을 반영
- **인간 추론 스타일 모방**이라는 관점에서 System 1/System 2 이분법을 도입하여 추론의 이론적 기초 제공
- **자율 에이전트 추론**을 별도 범주로 신설하여 embodied reasoning, multi-agent reasoning, autonomous driving 등 새로운 응용 포함
- **지속적 갱신 모델** 도입으로 GitHub 저장소를 통한 살아있는 서베이 구현
- **형식 언어 추론과 자연 언어 추론**의 이원적 분류를 명확히 하여 다양한 응용 영역 포괄

## Limitation & Further Study

- **빠른 발전 속도**: 논문 발표 이후 새로운 모델(GPT-4, Claude 등)과 기법이 지속적으로 등장하여 내용이 빠르게 구식화될 수 있음
- **평가 방법론의 다양성**: 각 추론 작업별로 평가 지표와 벤치마크가 다양하여 교차 비교 어려움
- **이론적 설명 부족**: 파운데이션 모델이 추론 능력을 어떻게 획득하는지에 대한 깊이 있는 이론적 분석 부족
- **실제 적용의 한계**: 학술 벤치마크에서의 성능 향상이 실제 복잡한 현실 문제 해결로 얼마나 전이되는지 미명확
- **후속 연구 방향**: 형식 검증(Formal Verification) 방법론과의 결합, 추론 과정의 해석 가능성(Interpretability) 향상, 도메인 특화 추론 능력 개발이 필요
- **비용과 환경 영향**: 대규모 파운데이션 모델의 학습 및 운영에 따른 높은 계산 비용과 환경 영향 고려 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 서베이는 파운데이션 모델의 추론 능력을 다루는 분야에서 현재까지의 연구 성과를 가장 포괄적으로 정리한 중요한 자료이며, 특히 멀티모달 및 에이전트 추론이라는 최신 방향을 반영하고 지속적 갱신 계획을 제시함으로써 학계에 큰 기여를 할 것으로 예상된다.

## Related Papers

- 🔗 후속 연구: [[papers/833_Towards_reasoning_era_A_survey_of_long_chain-of-thought_for/review]] — 파운데이션 모델의 추론을 장기 사고 연쇄 추론으로 확장하여 더 깊은 추론 능력을 다룬다.
- 🧪 응용 사례: [[papers/652_Rbf_Quantifying_and_optimizing_reasoning_boundaries_across_m/review]] — 다양한 작업에서 추론 경계를 정량화하고 최적화하는 구체적인 방법론을 제시한다.
- ⚖️ 반론/비판: [[papers/471_Large_Language_Models_Cannot_Self-Correct_Reasoning_Yet/review]] — 대규모 언어모델이 아직 자기 수정 추론을 완전히 수행할 수 없다는 한계를 지적한다.
- 🏛 기반 연구: [[papers/243_Critique-GRPO_Advancing_LLM_Reasoning_with_Natural_Language/review]] — 파운데이션 모델의 추론 능력 서베이는 Critique-GRPO의 자연언어 비판 통합 접근법에 추론 메커니즘의 이론적 배경을 제공한다.
