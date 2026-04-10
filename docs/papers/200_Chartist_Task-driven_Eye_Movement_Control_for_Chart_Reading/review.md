---
title: "200_Chartist_Task-driven_Eye_Movement_Control_for_Chart_Reading"
authors:
  - "Danqing Shi"
  - "Yao Wang"
  - "Yunpeng Bai"
  - "Andreas Bulling"
  - "Antti Oulasvirta"
date: "2025"
doi: "10.48550/ARXIV.2502.03575"
arxiv: ""
score: 4.0
essence: "본 논문은 차트 읽기 시 사용자의 작업별 안구 움직임 패턴(스캔패스)을 예측하는 첫 번째 계산 모델인 Chartist를 제시한다. 계층적 제어 아키텍처(LLM 기반 인지 제어기와 강화학습 기반 안구운동 제어기)를 통해 값 검색, 필터링, 극값 찾기와 같은 분석 작업을 수행할 때 인간과 유사한 시선 순서를 생성한다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Scientific_Literature_Analysis"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Shi et al._2025_Chartist Task-driven Eye Movement Control for Chart Reading.pdf"
---

# Chartist: Task-driven Eye Movement Control for Chart Reading

> **저자**: Danqing Shi, Yao Wang, Yunpeng Bai, Andreas Bulling, Antti Oulasvirta | **날짜**: 2025 | **DOI**: [10.48550/ARXIV.2502.03575](https://doi.org/10.48550/ARXIV.2502.03575)

---

## Essence

![Figure 1](figures/fig1.webp)
*Chartist가 다양한 분석 작업(값 검색, 필터링, 극값 찾기)에 걸쳐 작업 중심적 스캔패스를 예측하는 방식을 보여주는 예시*

본 논문은 차트 읽기 시 사용자의 작업별 안구 움직임 패턴(스캔패스)을 예측하는 첫 번째 계산 모델인 Chartist를 제시한다. 계층적 제어 아키텍처(LLM 기반 인지 제어기와 강화학습 기반 안구운동 제어기)를 통해 값 검색, 필터링, 극값 찾기와 같은 분석 작업을 수행할 때 인간과 유사한 시선 순서를 생성한다.

## Motivation

- **Known**: 
  - 시각 주의(visual attention)는 정보 시각화 설계에 중요한 역할을 함
  - 안구 추적(eye tracking)을 통해 인간의 스캔패스 수집 가능하나 비용과 시간이 많이 소요됨
  - 기존 스캔패스 예측 모델들은 자유로운 시청(free-viewing) 상황의 하향식(bottom-up) 주의에만 초점

- **Gap**: 
  - 분석 작업에 따른 상향식(top-down) 작업 중심적 스캔패스 예측 모델 부재
  - 시간적 정보와 개인별 행동 특성이 결여됨
  - 기존 목표 중심 스캔패스 모델들은 시각 검색(visual search) 작업에만 제한적

- **Why**: 
  - 사용자들은 작업마다 완전히 다른 차트 영역을 관찰함
  - 같은 분석 작업의 스캔패스는 자유로운 시청보다 일관성 있음
  - 시뮬레이션을 통한 저비용 스캔패스 예측이 경험적 연구를 보완할 수 있음

- **Approach**: 
  - 계층적 제어 아키텍처: 고수준 인지 제어기(LLM)와 저수준 안구운동 제어기(강화학습)의 이분 구조
  - 세 가지 분석 작업(retrieve value, filter, find extreme)에 대한 인간 스캔패스 데이터 분석
  - 차트 이미지와 분석 작업 문장을 입력으로 인간과 유사한 고정점 수열 생성

## Achievement

![Figure 2](figures/fig2.webp)
*작업 중심적 안구 움직임 제어 개념도: 누적 정보에 기반하여 다음 부작업(subtask)을 결정하고, 각 부작업이 픽셀 수준의 안구 움직임 제어*

1. **첫 번째 작업 중심 스캔패스 예측 모델**: 자유로운 시청이 아닌 분석 작업 수행 중 시간적 순서를 포함한 스캔패스 예측의 첫 계산 모델 제시

2. **계층적 제어 아키텍처의 효과성**: 인지과학의 계층적 의사결정 프레임워크 개념을 반영하여 복잡한 작업을 단순한 부작업으로 분해 가능

3. **인간 유사성**: 기존 기준 모델들(일반 스캔패스 예측, 시각적 질문 답변, 자유로운 시청 차트 스캔패스)보다 인간 데이터와의 스캔패스 유사도가 높음

4. **인간 유사 시선 행동 특성**: 모델 예측이 고정점 지속 시간, 고정점 간 거리 등 요약 통계에서 인간과 유사한 안구 움직임 행동 특현

## How

![Figure 3](figures/fig3.webp)
*계층적 안구 움직임 제어 아키텍처 개요: 차트와 작업 입력 시 인지 제어기의 의사결정 흐름*

- **고수준 인지 제어기**:
  - LLM(Large Language Model)을 활용하여 현재까지 얻은 정보를 메모리에 저장
  - 작업을 이해하고 수집할 정보 운영(operation) 선택
  - "어디를 다음에 봐야 할까?" 결정

- **저수준 안구운동 제어기**:
  - 각 운영별로 별도의 강화학습(RL) 에이전트 훈련
  - 선택된 부작업에 따라 픽셀 수준의 세부 시선 움직임 수행
  - 망막 중심부(foveal vision) 영역에서 정보 추출

- **내부 메모리 구조**:
  - 방문 영역, 추출된 정보, 진행 상황 추적
  - 인지 제어기가 이전 관찰 정보 활용하여 미래 고정점 결정

- **훈련 워크플로우**:
  - 차트 수집 및 라벨링 (실제 데이터 + 합성 데이터)
  - 인간 스캔패스 데이터 분석
  - 강화학습 에이전트 훈련 (인간 안구 움직임 데이터 없이 수행 가능)

## Originality

- **첫 번째 작업 중심 스캔패스 모델**: 분석 작업의 시간적 순서를 포함한 스캔패스 예측은 선행 연구에서 다루지 않음

- **계층적 아키텍처의 새로운 적용**: LLM 기반 인지 제어와 RL 기반 안구운동 제어의 결합으로 모듈화된 접근법 제시

- **인간 데이터 없이 모델 훈련**: 강화학습을 통해 인간 안구 추적 데이터 없이도 모델 훈련 가능한 구조

- **분석 작업의 명시적 모델링**: 이전 모델들의 암묵적 작업 영향에서 벗어나 명시적으로 세 가지 분석 작업 정의 및 처리

## Limitation & Further Study

- **일반화 가능성 제한**: 
  - 세 가지 분석 작업(값 검색, 필터링, 극값 찾기)에만 적용됨
  - 통계 차트에 초점으로 다른 시각화 유형(네트워크 그래프, 지도 등)에 미적용

- **예측 정확도 문제**: 
  - 복잡한 차트나 다중 변수 분석 작업에서 정확도 저하 가능성
  - 개인차와 전문성 수준의 차이 반영 부족

- **메모리 및 맥락 처리**: 
  - 장기 스캔패스(많은 고정점)에서 인지 제어기의 메모리 제약
  - LLM의 컨텍스트 윈도우 제한

- **평가 범위 한계**:
  - 제한된 규모의 인간 스캔패스 데이터로만 검증
  - 동적 상호작용(마우스 클릭, 드래그 등)이 포함된 작업 미다룸

- **후속 연구 방향**:
  - 더 다양한 차트 유형 및 복잡한 분석 작업으로 확장
  - 사용자 특성(전문성, 도메인 지식)을 고려한 모델 개선
  - 실제 상호작용 시각화 환경에서의 검증
  - 다중 회귀 또는 주의 메커니즘을 통한 시선 움직임 개선

## Evaluation

- **Novelty**: 4.5/5
  - 작업 중심 스캔패스 예측 모델이 새로우며, 계층적 아키텍처의 적용이 창의적임
  - 다만 개별 기술(LLM, RL)은 기존 것의 조합

- **Technical Soundness**: 4/5
  - 계층적 제어 아키텍처가 논리적으로 타당하고 구현 가능
  - 강화학습 훈련 전략이 명확하나 세부 기술적 설명 부족
  - 인간 데이터 없이 훈련하는 것이 긍정적이나 검증 방식이 제한적

- **Significance**: 4/5
  - 시각화 설계 평가, 설명 가능한 AI, 최적화 등 다양한 적용 가능성
  - 정보 시각화 연구에 새로운 방향 제시
  - 현실 적용에는 일반화 제한으로 즉시 활용 어려움

- **Clarity**: 3.5/5
  - 논문 구조와 모델 개념이 대체로 명확
  - 계층적 아키텍처의 세부 구현(LLM 프롬프팅, RL 보상 함수)에 대한 설명 부족
  - Figure 2는 개념 설명에 도움이 되나 더 상세한 알고리즘 다이어그램 필요

- **Overall**: 4/5

**총평**: Chartist는 차트 읽기에서 작업 중심의 안구 움직임을 예측하는 첫 계산 모델로, 계층적 제어 아키텍처를 통해 새로운 접근을 제시한다. 기술적으로 타당하고 인간 유사성이 우수하나, 일반화 가능성과 예측 정확도 측면의 한계가 있으며, 세부 기술 설명과 광범위한 평가가 필요하다. 정보 시각화 분야에 의미 있는 기여를 하면서도 실제 응용을 위해서는 추가 개선이 요구된다.

## Related Papers

- 🧪 응용 사례: [[papers/339_Fimo_A_challenge_formal_dataset_for_automated_theorem_provin/review]] — 수학 문제 해결에서의 시각적 주의 제어를 차트 읽기 작업으로 확장한 응용
- 🔗 후속 연구: [[papers/315_Enhancing_chart-to-code_generation_in_multimodal_large_langu/review]] — 차트 이해를 작업별 안구운동 제어로 발전시킨 멀티모달 AI 연구
- 🏛 기반 연구: [[papers/551_MMC_Advancing_Multimodal_Chart_Understanding_with_Large-scal/review]] — 대규모 차트 데이터셋이 차트 읽기 시선 패턴 예측의 데이터 기반 제공
- 🔄 다른 접근: [[papers/199_ChartInstruct_Instruction_Tuning_for_Chart_Comprehension_and/review]] — 차트 읽기 시선 제어 vs 차트 이해 지시 튜닝의 서로 다른 차트 AI 접근법
- 🏛 기반 연구: [[papers/339_Fimo_A_challenge_formal_dataset_for_automated_theorem_provin/review]] — 수학 올림피아드 형식 문제가 차트 읽기 작업의 고차원 인지 능력 평가 기준
- 🔄 다른 접근: [[papers/203_Chartsketcher_Reasoning_with_multimodal_feedback_and_reflect/review]] — 차트 추론에서 스케칭 기반 접근법과 시각적 지시 튜닝 기반 접근법을 비교할 수 있습니다.
