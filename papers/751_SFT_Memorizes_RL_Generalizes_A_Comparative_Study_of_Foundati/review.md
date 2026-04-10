---
title: "751_SFT_Memorizes_RL_Generalizes_A_Comparative_Study_of_Foundati"
authors:
  - "Tianzhe Chu"
  - "Yuexiang Zhai"
  - "Jihan Yang"
  - "Shengbang Tong"
  - "Saining Xie"
date: "2025"
doi: "10.48550/arXiv.2501.17161"
arxiv: ""
score: 4.2
essence: "본 논문은 기초 모델의 사후훈련(post-training) 단계에서 지도학습 미세조정(SFT)과 강화학습(RL)의 일반화(generalization) 능력을 비교하는 체계적 연구로, **RL은 규칙 기반 추론과 시각 작업에서 우수한 일반화 성능을 보이는 반면, SFT는 훈련 데이터의 암기(memorization)에 치중한다**는 핵심 발견을 제시한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Domain-adapted_Instruction_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chu et al._2025_SFT Memorizes, RL Generalizes A Comparative Study of Foundation Model Post-training.pdf"
---

# SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training

> **저자**: Tianzhe Chu, Yuexiang Zhai, Jihan Yang, Shengbang Tong, Saining Xie | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2501.17161](https://doi.org/10.48550/arXiv.2501.17161)

---

## Essence

![Figure 1](figures/fig1.webp) *Figure 1: V-IRL 시각 네비게이션 환경에서 RL과 SFT의 비교 연구. OOD 곡선은 서로 다른 텍스트 액션 공간을 사용한 동일 작업의 성능을 나타냄*

본 논문은 기초 모델의 사후훈련(post-training) 단계에서 지도학습 미세조정(SFT)과 강화학습(RL)의 일반화(generalization) 능력을 비교하는 체계적 연구로, **RL은 규칙 기반 추론과 시각 작업에서 우수한 일반화 성능을 보이는 반면, SFT는 훈련 데이터의 암기(memorization)에 치중한다**는 핵심 발견을 제시한다.

## Motivation

- **Known**: SFT와 RL은 모두 대규모 기초 모델 훈련의 표준 기법으로 광범위하게 사용되고 있음 (GPT, Gemini, DeepSeek 등)

- **Gap**: 두 기법의 서로 다른 일반화와 암기 특성, 그리고 복잡한 다중모달(multimodal) 작업에서의 역할이 명확하게 규명되지 않았음

- **Why**: 신뢰할 수 있고 견고한 AI 시스템 구축을 위해서는 두 접근법이 데이터를 암기하는지 혹은 전이 가능한 원칙을 습득하는지를 명확히 이해해야 함

- **Approach**: (1) 텍스트 기반 규칙 일반화와 시각 일반화 두 가지 관점에서 평가, (2) GeneralPoints (산술 추론 카드 게임)와 V-IRL (실제 네비게이션 환경) 두 가지 새로운/기존 벤치마크 도입, (3) SFT 후 RL을 순차적으로 적용하는 다단계 RL 프레임워크 채용

## Achievement

![Figure 4 & 5 병합 개념](figures/fig4.webp) *Figure: GeneralPoints와 V-IRL에서 RL과 SFT의 성공률(%) 추이 비교. RL이 분포 외 데이터(OOD)에서 일관된 성능 개선을 유지*

1. **우수한 규칙 기반 일반화**: RL은 훈련된 규칙을 미보유(unseen) 규칙 변형에 성공적으로 전이시키는 반면, SFT는 분포 외(out-of-distribution) 작업에서 큰 성능 저하를 보임

2. **시각 영역 일반화**: RL은 색상, 공간 배치 등 시각 입력 변형에 대해서도 일관된 일반화를 달성하고, V-IRL 벤치마크에서 최첨단 성능 달성 (+33.8%: 44.0% → 77.8%)

3. **시각 인식 능력 향상**: 결과 기반 보상(outcome-based reward) 함수를 사용한 RL 훈련이 모델의 기저 시각 인식 능력을 개선하는 메커니즘 규명

4. **SFT의 보조 역할**: SFT는 출력 포맷 안정화 "형식 교사(format teacher)" 역할을 하여 RL의 성능 이득 달성을 가능하게 함

5. **추론시간 계산 스케일링**: 최대 검증 단계 수 증대를 통한 추론시간 계산 확장이 RL 일반화의 핵심 요소임을 입증

## How

![Figure 2 & 3 참조](figures/fig2.webp) *Figure 2-3: 검증자(verifier)를 이용한 순차적 수정 공식화. 상태-액션 전이 예시*

- **순차적 수정(Sequential Revision) 공식화**: 
  - 초기 시점(t=0)에는 시스템 프롬프트로 시작
  - 이후 시점(t≥1)에서는 시스템 프롬프트에 이전 모델 및 검증자 출력을 누적 결합
  - 이를 통해 모델이 오류를 식별하고 자체 수정 가능하게 구성

- **검증자 기반 보상**: VER: V^n → ℝ × V^k 함수가 생성된 출력을 평가하고 결과 기반 보상(outcome-based reward) 반환

- **RL 알고리즘**: 모델을 정책 네트워크 π_θ로 취급하고 PPO(Proximal Policy Optimization)를 백본 알고리즘으로 사용

- **일반화 평가 프로토콜**:
  - 텍스트 규칙 변형: 훈련된 규칙과 미보유 규칙 변형 간 성능 전이 측정
  - 시각 변형: 색상, 공간 배치, 스타일 등의 변화에 대한 일관성 측정

- **GeneralPoints 환경**: 4장의 카드(텍스트 또는 이미지)에서 목표 숫자(기본값 24) 달성 방정식 생성 작업 설계

- **V-IRL 환경**: 실제 실내 장면에서 자연어 지시사항을 따르는 공간 추론 네비게이션 작업

## Originality

- **비교 연구의 체계성**: SFT와 RL을 암기-일반화 관점에서 직접 비교하는 통합적 분석이 기존 연구와 차별화 (기존: 단일 기법에 초점)

- **GeneralPoints 환경 신규 개발**: Points24를 확장하여 다양한 규칙 변형과 시각 변형을 체계적으로 평가 가능한 환경 구축

- **다중모달 통합 분석**: LLM(GeneralPoints-L)과 VLM(GeneralPoints-VL)에서 동시에 진행하여 결과의 일반성 입증

- **시각 인식 능력 개선 메커니즘 규명**: RL이 단순히 작업 성능만 개선하는 것이 아니라 기저 시각 인식 능력까지 향상시킨다는 점 발견

- **추론시간 계산과 일반화의 연결**: 최근 확장 법칙(scaling laws) 연구와 일반화 능력을 연결한 실증적 분석

## Limitation & Further Study

- **제한된 작업 범위**: GeneralPoints와 V-IRL 두 가지 주로 정량적 피드백을 받는 작업에만 초점 → 자유형식 생성 작업(번역, 요약 등)에서의 일반화 특성은 미규명

- **모델 크기 및 아키텍처 단일화**: 특정 백본 모델(가능성 높음: Gemini 계열)에서만 실험 → 다양한 모델 크기와 아키텍처에서의 일반화 필요

- **SFT-RL 순차 결합만 검토**: SFT 없이 RL 직접 적용, 또는 역순서 적용 등의 변형 실험 부재

- **보상 함수 설계의 영향**: 결과 기반 보상에만 초점 → 중간 과정 기반 보상(process-based reward)이나 인간 피드백 기반 보상의 영향은 미분석

- **후속 연구 방향**:
  - 자유형식 언어 생성, 대화 시스템 등 다양한 작업 클래스 확대
  - 매우 큰 규모 모델(100B+ 파라미터)에서의 일반화 패턴 조사
  - 적응형 보상 함수와 커리큘럼 학습을 통한 SFT-RL 협력 최적화
  - 시각 인식 개선의 신경망 수준 분석(어떤 레이어가 개선되는가)


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4.5/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.2/5

**총평**: 본 논문은 대규모 기초 모델 훈련에서 광범위하게 사용되는 두 주요 기법의 일반화 능력을 체계적으로 비교한 중요한 실증 연구로, "RL은 일반화, SFT는 암기"라는 명확한 구분을 통해 향후 모델 개발 전략에 실질적 지침을 제공한다. 다만 작업 범위와 모델 다양성 측면에서의 확장이 필요하며, SFT-RL 상호작용의 최적화 메커니즘에 대한 더 깊은 분석이 요구된다.

## Related Papers

- 🔗 후속 연구: [[papers/538_Mind_the_gap_Examining_the_self-improvement_capabilities_of/review]] — 자기개선 메커니즘에서 SFT의 암기와 RL의 일반화 능력 차이를 체계적으로 분석한 확장
- 🏛 기반 연구: [[papers/1100_Representative_Informative_and_De-Amplifying_Requirements_fo/review]] — RL 기반 실험설계 최적화에서 일반화 능력의 중요성을 입증하는 이론적 기반
- 🧪 응용 사례: [[papers/265_DeepSeek-R1_incentivizes_reasoning_in_LLMs_through_reinforce/review]] — DeepSeek-R1의 강화학습 기반 추론이 일반화 능력 향상에 미치는 영향 분석에 적용
- 🔄 다른 접근: [[papers/598_PAG_Multi-Turn_Reinforced_LLM_Self-Correction_with_Policy_as/review]] — 정책 기반 강화학습과 달리 사후훈련 단계에서 SFT와 RL의 근본적 차이 분석
- 🏛 기반 연구: [[papers/538_Mind_the_gap_Examining_the_self-improvement_capabilities_of/review]] — SFT와 RL의 일반화 능력 비교 연구에서 자기개선 메커니즘의 이론적 기반 제공
- 🧪 응용 사례: [[papers/1092_Table-llm-specialist_Language_model_specialists_for_tables_u/review]] — 테이블 전문가 모델에서 생성-검증 이중 작업이 SFT 대비 일반화 성능 향상에 기여
- 🧪 응용 사례: [[papers/1100_Representative_Informative_and_De-Amplifying_Requirements_fo/review]] — 강화학습의 일반화 능력 향상을 위해 R-IDeA 획득함수를 통한 견고한 실험설계 적용
- 🔗 후속 연구: [[papers/649_Qwen25_technical_report/review]] — SFT와 RL의 비교 연구가 Qwen2.5에서 사용된 DPO와 GRPO 같은 후학습 기법의 효과를 이론적으로 뒷받침한다.
