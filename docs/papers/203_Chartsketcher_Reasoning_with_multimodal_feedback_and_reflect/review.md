---
title: "203_Chartsketcher_Reasoning_with_multimodal_feedback_and_reflect"
authors:
  - "Muye Huang"
  - "Lingling Zhang"
  - "Jie Ma"
  - "Han Lai"
  - "Fangzhi Xu"
date: "2025"
doi: "arXiv:2505.19076"
arxiv: ""
score: 4.0
essence: "본 논문은 멀티모달 대규모 언어 모델(MLLM)이 차트를 이해할 때 시각적 피드백을 통한 반복적 스케칭(Sketch-CoT)으로 추론 과정을 개선하는 방법을 제안한다. 인간의 인지 행동에서 영감을 받아, 모델이 중간 추론 단계를 차트에 직접 주석 처리하고 이를 다시 입력으로 제공하여 멀티모달 상호작용을 통한 깊이 있는 이해를 실현한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Visual_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Tang et al._2025_Chartsketcher Reasoning with multimodal feedback and reflection for chart understanding.pdf"
---

# ChartSketcher: Reasoning with multimodal feedback and reflection for chart understanding

> **저자**: Muye Huang, Lingling Zhang, Jie Ma, Han Lai, Fangzhi Xu, Yifei Li, Wenjun Wu, Yaqiang Wu, Jun Liu | **날짜**: 2025 | **DOI**: [arXiv:2505.19076](https://arxiv.org/abs/2505.19076)

---

## Essence

![Figure 1](figures/fig1.webp)
*ChartSketcher의 개요: 중간 추론 및 반성 과정(점선)과 각 단계의 스케치 출력*

본 논문은 멀티모달 대규모 언어 모델(MLLM)이 차트를 이해할 때 시각적 피드백을 통한 반복적 스케칭(Sketch-CoT)으로 추론 과정을 개선하는 방법을 제안한다. 인간의 인지 행동에서 영감을 받아, 모델이 중간 추론 단계를 차트에 직접 주석 처리하고 이를 다시 입력으로 제공하여 멀티모달 상호작용을 통한 깊이 있는 이해를 실현한다.

## Motivation

- **Known**: 최근 GPT-4o, Gemini-2.0, Qwen-2VL 등 MLLM이 차트 이해에 상당한 진전을 보이고 있으나, 기존 모델들은 텍스트 기반 논리 추론에 중점을 둠

- **Gap**: 복잡한 차트 요소(겹치는 데이터 포인트, 다중 교차선, 조밀한 수치 정보)를 처리하는 고정밀 시각적 추론 능력이 부족하며, 시각적 이해의 오류로부터 회복할 수 없음

- **Why**: 기존 CoT 방식은 시각 영역 기반 방법(예: VisualCoT의 크로핑)이 여러 영역의 동시 분석을 제한하고, 텍스트 중심 접근은 사용자 해석 가능성(interpretability)을 감소시킴

- **Approach**: 인간이 복잡한 시각 정보를 마주할 때 스케칭으로 핵심 세부사항을 표시하고 문제를 분해하는 자연스러운 행동에서 영감을 받아, Sketch-CoT와 반성 메커니즘을 통해 멀티모달 피드백 기반 추론 방식을 제안

## Achievement

![Figure 2](figures/fig2.webp)
*ChartSketcher 훈련 과정: 상단은 콜드 스타트 단계(지식 증류), 하단은 오프라인 강화학습 최적화*

1. **Sketch-CoT 메커니즘**: MLLM이 중간 추론 단계를 프로그래밍 방식의 스케칭 라이브러리를 통해 차트에 직접 주석 처리하고, 생성된 스케치를 다시 입력으로 받아 반복적 멀티모달 추론을 실현

2. **자동 반성 및 오류 수정**: 단계 간 반성 과정을 포함하여 모델이 이전 단계의 추론 오류를 식별하고 즉시 수정할 수 있는 인간 수준의 반성 능력 구현

3. **두 단계 훈련 전략**: 
   - 콜드 스타트 단계: 300K 세밀한 주석 데이터로 LLM에서 MLLM으로 추론 및 반성 패턴을 교차 모달 증류
   - RL 단계: MCTS 및 다양한 데이터 샘플링으로 50K 단계별 추론 예제를 활용한 오프라인 강화학습

4. **포괄적 데이터셋**: 차트 단계별 추론을 지원하는 300K 콜드 스타트 샘플과 50K 강화학습 샘플 구성

## How

![Figure 4](figures/fig4.webp)
*ChartSketcher의 네 가지 사례: 각 단계의 드로잉 코드는 생략*

**아키텍처 설계**:
- **프로그래밍 스케칭 라이브러리**: 간단한 명령 문법으로 기하학적 도형(점, 선, 원, 화살표 등)을 생성·조작하며, 이동, 회전, 삭제 등의 연산 지원
- **스케칭 추론 파이프라인**: MLLM 출력을 파싱하여 스케치를 생성하고 자동으로 시각화를 다시 MLLM에 피드백하는 "반성-드로우-피드백" 루프 구현

**훈련 방식**:
- **콜드 스타트 단계**:
  1. Sketch-CoT 데이터 합성: 기존 차트 QA 데이터에서 의도적으로 오류를 생성하여 다중 추론 경로 구성
  2. 반성적 추론 데이터 합성: LLM이 오류 감지 및 수정 과정을 생성하도록 유도
  3. 크로스 모달 증류: LLM이 생성한 텍스트 추론을 차트에 스케치하는 형태로 변환하여 MLLM 훈련

- **RL 최적화 단계**:
  1. Sketch-MCTS: 트리 탐색을 통해 여러 추론 경로 생성
  2. KTO(Kahneman-Tversky Optimization) 훈련: 오프라인 방식으로 모델 개선, 보상 신호 없이 선호도 쌍만 필요

## Originality

- **시각-피드백 기반 추론**: 기존 텍스트 중심 CoT나 영역 크로핑 방식과 달리, 직접 스케칭을 통한 멀티모달 피드백 루프 도입으로 차트의 모든 영역을 동시에 고려 가능하게 함

- **자동 반성 메커니즘**: 각 단계 후 모델이 스스로 오류를 감지하고 수정하는 능력 구현으로, 시각적 이해 오류로부터의 회복 가능성 제시

- **체계적 데이터 구성**: 의도적 오류 생성, 반성 패턴 학습, 다중 경로 탐색을 통한 300K+50K 규모의 구조화된 훈련 데이터 구축

- **인간 인지 행동 기반 설계**: 스케칭을 통한 시각적 초점화라는 인간의 자연스러운 문제 해결 방식을 MLLM에 체계적으로 통합

## Limitation & Further Study

- **계산 효율성**: 반복적 스케칭 및 피드백 루프로 인한 추론 시간 및 계산 비용 증가 문제가 상세히 논의되지 않음

- **프로그래밍 라이브러리 복잡성**: 제시된 스케칭 라이브러리의 명령 문법이 MLLM의 실제 코드 생성에서 오류율에 미치는 영향 분석 부족

- **차트 유형 범위**: 실험에 포함된 차트 유형(막대, 선, 산점도 등)의 다양성과 매우 복잡한 차트(히트맵, 3D 차트 등)에 대한 일반화 능력 미검증

- **비교 기준선**: 최근 오픈소스 MLLM(Llama-Vision, Phi-Vision 등)과의 직접 비교 부족

- **후속 연구 방향**:
  1. 스트리밍 추론 및 점진적 스케칭 방식으로 계산 효율 개선
  2. 사용자 상호작용을 포함한 대화형 차트 분석 확장
  3. 표, 과학 그래프 등 다양한 시각화 형식으로 일반화
  4. 모델의 스케칭 실수 자동 감지 및 수정 메커니즘 강화


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 3.5/5
- Overall: 4/5

**총평**: ChartSketcher는 인간의 시각적 추론 행동에서 영감을 받아 MLLM의 차트 이해 능력을 향상시키는 혁신적 방법론을 제시하며, 체계적인 데이터 구축과 두 단계 훈련 전략으로 실증적 효과를 입증했으나, 계산 효율성과 프로그래밍 오버헤드 문제에 대한 충분한 분석이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/200_Chartist_Task-driven_Eye_Movement_Control_for_Chart_Reading/review]] — 차트 추론에서 스케칭 기반 접근법과 시각적 지시 튜닝 기반 접근법을 비교할 수 있습니다.
- 🔗 후속 연구: [[papers/551_MMC_Advancing_Multimodal_Chart_Understanding_with_Large-scal/review]] — 대규모 멀티모달 차트 이해 데이터셋이 반복적 스케칭 방법론의 성능 평가에 확장 적용될 수 있습니다.
- 🏛 기반 연구: [[papers/315_Enhancing_chart-to-code_generation_in_multimodal_large_langu/review]] — 멀티모달 대형 언어 모델의 차트-코드 생성 능력 향상이 시각적 피드백 기반 추론의 이론적 기반입니다.
