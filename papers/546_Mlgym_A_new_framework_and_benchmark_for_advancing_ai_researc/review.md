---
title: "546_Mlgym_A_new_framework_and_benchmark_for_advancing_ai_researc"
authors:
  - "Deepak Nathani"
  - "Lovish Madaan"
  - "Nicholas Roberts"
  - "Nikolay Bashlykov"
  - "Ajay Menon"
date: "2025"
doi: "미제공"
arxiv: ""
score: 4.25
essence: "본 논문은 LLM 기반 AI 연구 에이전트(AI Research Agent)를 평가하고 개발하기 위한 첫 번째 Gym 환경인 **MLGym**과 13개 과제로 구성된 벤치마크 **MLGym-Bench**를 제시한다. 이는 RL, 커리큘럼 러닝 등 다양한 학습 알고리즘으로 에이전트를 훈련할 수 있는 통합 플랫폼을 제공한다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Large_Language_Model_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Nathani et al._2025_Mlgym A new framework and benchmark for advancing ai research agents.pdf"
---

# MLGym: A new framework and benchmark for advancing ai research agents

> **저자**: Deepak Nathani, Lovish Madaan, Nicholas Roberts, Nikolay Bashlykov, Ajay Menon, Vincent Moens, Amar Budhiraja, Despoina Magka, Vladislav Vorotilov, Gaurav Chaurasia, Dieuwke Hupkes, Ricardo Silveira Cabral, Tatiana Shavrina, Jakob Foerster, Yoram Bachrach, William Yang Wang, Roberta Raileanu | **날짜**: 2025 | **DOI**: [미제공](https://doi.org/)

---

## Essence

![Figure 1](figures/fig1.webp)
*MLGym의 구조: 다양한 AI 연구 작업을 통합하는 프레임워크*

본 논문은 LLM 기반 AI 연구 에이전트(AI Research Agent)를 평가하고 개발하기 위한 첫 번째 Gym 환경인 **MLGym**과 13개 과제로 구성된 벤치마크 **MLGym-Bench**를 제시한다. 이는 RL, 커리큘럼 러닝 등 다양한 학습 알고리즘으로 에이전트를 훈련할 수 있는 통합 플랫폼을 제공한다.

## Motivation

- **Known**: 최근 파운데이션 모델 기반 AI 에이전트가 소프트웨어 엔지니어링(SWE-Bench, SWE-Agent) 및 일부 ML 작업(MLE-Bench, MLAgentBench)에서 평가되고 있음

- **Gap**: 
  - 기존 벤치마크들은 폐쇄형 작업(closed-ended tasks)에 집중하거나 좁은 범위의 도메인만 다룸
  - RL, 게임 이론, SAT 등 알고리즘 설계를 요구하는 개방형 AI 연구 작업 부재
  - 모델 가중치, RL 알고리즘, 코드 등 다양한 연구 산출물을 평가하는 유연한 프레임워크 부족
  - RL 기반 에이전트 훈련을 지원하는 Gym 인터페이스 미존재

- **Why**: AI 에이전트가 진정한 과학적 발견을 가능하게 하려면, 복잡한 실험 설계, 가설 생성, 알고리즘 혁신 등을 포함한 개방형 연구 환경에서의 평가가 필수적

- **Approach**: Gymnasium 표준을 따르는 통합 프레임워크를 설계하고, 다양한 도메인(컴퓨터 비전, NLP, RL, 게임 이론, SAT)의 13개 개방형 연구 작업을 선정하여 최신 LLM(Claude-3.5-Sonnet, Llama-3.1-405B, GPT-4o, o1-preview, Gemini-1.5-Pro) 평가

## Achievement

![Figure 2](figures/fig2.webp)
*Best Attempt@4 및 Best Submission@4 성능 프로필 비교*

1. **첫 번째 Gym 환경 기반 AI 연구 에이전트 프레임워크 제시**: 표준화된 인터페이스로 RL, 커리큘럼 러닝, 개방형 학습 등 다양한 학습 알고리즘 적용 가능

2. **다양한 도메인의 개방형 연구 작업 구성**: 이미지 분류(cifar10), 언어 모델링(mini-gpt2), RL 정책 학습(lunar-lander), 게임 이론(한판 포커), SAT 해결, 신경망 구조 탐색 등 13개 이질적 작업

3. **유연한 평가 아티팩트 지원**: 모델 체크포인트, RL 알고리즘, 전략 코드 등 다양한 형태의 연구 산출물을 직접 평가 가능

4. **AutoML 기반 통합 평가 메트릭 제안**: 최적화 문제의 성능 프로파일(performance profile) 개념을 도입하여 이질적인 평가 지표를 가진 작업들 간 공정한 비교 가능

![Figure 3](figures/fig3.webp)
*Best Attempt AUP@4 vs API 비용: 성능과 경제성 분석*

## How

- **MLGym 아키텍처**:
  - Gymnasium 표준 인터페이스 채택 (환경, 액션, 관찰, 보상 정의)
  - 작업별 도구 모음 통합 (파일시스템, 셸, GPU, 데이터 처리 유틸리티)
  - 에이전트 하니스(agentic harness): 기본 LLM을 프롬프트 기반 에이전트로 변환하는 통합 모듈

- **MLGym-Bench 설계**:
  - 13개 작업을 4가지 카테고리로 분류: 지도학습(3개), 언어 모델링(3개), 강화학습(4개), 조합최적화(3개)
  - 각 작업마다 목표 성능, 평가 함수, 초기 기저선 제공
  - 4회 시도 제한(Best Attempt@4, Best Submission@4) 하에서 에이전트 성능 측정

- **평가 메트릭**:
  - 성능 프로파일(performance profile): 작업별 상이한 메트릭을 정규화하여 AUP(Area Under the Profile) 계산
  - 비용 효율성 분석: API 호출 비용 대비 성능 개선 비율 평가
  - 오류 분류: 종료 오류, 실행 오류, 평가 오류, 성능 오류로 구분

- **AI 연구 에이전트 역량 계층화**:
  - Level 0: 재현(Reproduction)
  - Level 1: 기저선 개선(Baseline Improvement) ← MLGym-Bench 대상
  - Level 2-5: SOTA 달성, 신규 과학적 기여, 획기적 발견, 장기 연구 의제

## Originality

- **최초의 Gym 기반 AI 연구 에이전트 프레임워크**: 강화학습 알고리즘 적용 가능한 표준화된 환경 제공 (기존 벤치마크는 평가 도구일 뿐 훈련 플랫폼 아님)

- **알고리즘 설계 작업 포함**: RL 정책 학습, 게임 이론 전략, SAT 해결 등 단순 하이퍼파라미터 튜닝을 넘어선 알고리즘 혁신을 요구하는 작업 구성

- **다중 도메인 개방형 연구**: 컴퓨터 비전, NLP, RL, 게임 이론, 조합최적화 등 광범위한 AI 분야를 통합하여 에이전트의 일반화 능력 측정

- **유연한 아티팩트 평가 메커니즘**: 모델 가중치, 알고리즘 코드, 정책 네트워크 등 이질적인 연구 산출물을 통일된 평가 함수로 검증

- **계층적 역량 프레임워크**: 단순 재현부터 패러다임 전환적 발견까지 6단계 역량 분류 체계 제시로 향후 AI 연구 에이전트 발전 방향 제시

## Limitation & Further Study

- **현재 LLM의 한계**: 최신 frontier 모델(Claude-3.5, GPT-4o, o1)이 하이퍼파라미터 최적화로는 기저선 개선이 가능하나, 새로운 가설, 알고리즘, 아키텍처 생성 실패

- **평가 지표의 단순화**: 성능 프로파일 기반 정규화가 작업 이질성을 해결하나, 과학적 가치나 창의성 측정은 여전히 정량화 어려움

- **제한된 에이전트 설계**: 기본 하니스가 단순 프롬프트 기반이어서 고도화된 에이전트 (계획, 메모리, 자성찰) 아키텍처 탐색 미흡

- **후속 연구 방향**:
  - Level 2-3(SOTA 달성, 신규 과학적 기여) 작업 확대로 상위 역량 측정
  - RL, 커리큘럼 학습 등 에이전트 훈련 알고리즘 개발 및 검증
  - 인간-에이전트 협업 시나리오에서의 상호작용 연구
  - 더 많은 실제 AI 연구 작업(논문 재현, 신규 데이터셋 개발 등) 추가
  - 장기 연속 작업(weeks/months) 시나리오 구축


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4.5/5
- Overall: 4.25/5

**총평**: MLGym은 AI 연구 자동화 분야의 첫 Gym 환경으로서 표준화된 평가와 훈련을 가능하게 하는 중요한 인프라를 제공하나, 현재 LLM의 진정한 과학적 혁신 능력 부족은 Level 1(기저선 개선)에 머물게 함. 향후 더 고도화된 에이전트 알고리즘과 상위 역량 작업 추가로 진정한 AI 과학자 개발의 발판이 될 수 있을 것으로 기대됨.

## Related Papers

- 🔄 다른 접근: [[papers/528_MedAgentGym_A_Scalable_Agentic_Training_Environment_for_Code/review]] — 머신러닝 vs 생의학 도메인에서의 AI 에이전트 개발 환경을 제시합니다.
- 🧪 응용 사례: [[papers/230_Code_llama_Open_foundation_models_for_code/review]] — 코드 생성 모델이 AI 연구 에이전트 프레임워크에 활용됩니다.
- 🏛 기반 연구: [[papers/782_SWE-bench_Can_Language_Models_Resolve_Real-World_GitHub_Issu/review]] — 실제 개발 문제 해결이 AI 연구 에이전트의 기반을 제공합니다.
- 🏛 기반 연구: [[papers/230_Code_llama_Open_foundation_models_for_code/review]] — 코드 생성 모델이 AI 연구 에이전트 개발의 기반이 됩니다.
- 🔄 다른 접근: [[papers/528_MedAgentGym_A_Scalable_Agentic_Training_Environment_for_Code/review]] — 생의학 vs 머신러닝 도메인에서의 AI 에이전트 훈련 환경을 제시합니다.
