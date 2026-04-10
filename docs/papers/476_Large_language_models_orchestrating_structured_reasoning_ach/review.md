---
title: "476_Large_language_models_orchestrating_structured_reasoning_ach"
authors:
  - "Antoine Grosnit"
  - "Alexandre Maraval"
  - "Refinath S N"
  - "Zichao Zhao"
  - "James Doran"
date: "2024"
doi: "arXiv:2411.03562"
arxiv: ""
score: 4.5
essence: "본 논문은 Kolb의 경험적 학습 이론(Experiential Learning Theory)과 Vygotsky의 근접발달영역(Zone of Proximal Development, ZPD)을 계산적으로 구현한 Agent K를 제시하며, 이를 통해 LLM 기반 자율 에이전트가 실제 데이터 과학 경진대회(Kaggle)에서 최상위 인간 수준의 성능을 달성하였다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-agent_Task_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2024_Large language models orchestrating structured reasoning achieve kaggle grandmaster level.pdf"
---

# Large Language Models Orchestrating Structured Reasoning Achieve Kaggle Grandmaster Level

> **저자**: Antoine Grosnit, Alexandre Maraval, Refinath S N, Zichao Zhao, James Doran, Giuseppe Paolo, Albert Thomas, Jonas Gonzalez, Abhineet Kumar, Khyati Khandelwal, Abdelhakim Benechehab, Hamza Cherkaoui, Youssef Attia El-Hili, Kun Shao, Jianye Hao, Jun Yao, Balázs Kégl, Haitham Bou-Ammar, Jun Wang (Huawei Noah's Ark Lab, AI Centre UCL, TU Darmstadt) | **날짜**: 2024 | **DOI**: [arXiv:2411.03562](https://arxiv.org/abs/2411.03562)

---

## Essence

![Figure 1](figures/fig1.webp)
*Kolb의 경험적 학습 이론의 계산적 형식화: 내재적 함수(반성과 추상화)와 외재적 함수(환경과의 상호작용)의 순환 구조*

본 논문은 Kolb의 경험적 학습 이론(Experiential Learning Theory)과 Vygotsky의 근접발달영역(Zone of Proximal Development, ZPD)을 계산적으로 구현한 Agent K를 제시하며, 이를 통해 LLM 기반 자율 에이전트가 실제 데이터 과학 경진대회(Kaggle)에서 최상위 인간 수준의 성능을 달성하였다.

## Motivation

- **Known**: 
  - 최신 LLM은 사전학습(pretraining), 미세조정(fine-tuning), RLHF 등을 통해 우수한 일반화 능력과 추론 능력을 보유
  - ReAct, Reflexion, Voyager 같은 최근 에이전트 연구는 기본적인 반성(reflection)과 계획 수정 능력 입증
  - 강화학습(RL) 기반 에이전트는 AlphaGo 등에서 초인간 성능 달성 (단, 잘 정의된 환경에 제한)

- **Gap**: 
  - 기존 LLM 에이전트는 정적 데이터에 기반한 학습에 의존하며, 프롬프트 수준의 휴리스틱만 사용
  - 장기간에 걸친 **구조화된 학습**이나 **내부 전략 적응**을 위한 원칙적 아키텍처 부재
  - 인간처럼 경험-반성-추상화-실험의 순환을 통해 진정한 의미의 학습 능력을 갖춘 에이전트 없음

- **Why**: 
  - 인류의 학습은 Kolb의 학습 순환(구체적 경험 → 반성적 관찰 → 추상적 개념화 → 능동적 실험)을 따름
  - Vygotsky의 ZPD는 체계적 스캐폴딩(scaffolding)을 통한 단계적 학습의 중요성 강조
  - 전 지구적 데이터 포화로 정적 사전학습만으로는 한계 도달

- **Approach**: 
  - Kolb 학습 순환을 계산적으로 형식화: 내재적 함수(intrinsic functions)와 외재적 함수(extrinsic functions)의 반복 구조
  - Vygotsky의 ZPD를 적용한 스캐폴드 기반 학습 → 자유형 학습 단계로 구성
  - 81개 Kaggle 경진대회를 통한 실증 평가

## Achievement

![Figure 2](figures/fig1.webp)
*스캐폴드 기반 경험적 학습에서 자율적 일반화로의 진행 흐름*

![Figure 4](figures/fig1.webp)
*Agent K의 Elo-MMR 점수와 인간 참여자들의 성능 비교*

1. **Kaggle 최상위 성능 달성**: 
   - Elo-MMR 점수 1694로 Kaggle Masters(상위 2%, 20만+ 사용자 중)의 중앙값 수준 도달
   - 81개 과제 전반에서 완전 자동화된 end-to-end 데이터 과학 파이프라인 구축
   - 상금이 수여되는 경진대회에서 금메달 4개, 은메달 4개 달성

2. **다중 모달리티에서의 일관된 성능**:
   - 표형 데이터(tabular), 컴퓨터 비전(vision), 자연어처리(NLP) 과제 전반에서 인간 경쟁자 수준의 성과
   - 총 메달 등급: 금메달 9개, 은메달 8개, 동메달 12개 (다양한 경진대회)

3. **완전 자율 에이전트의 첫 사례**:
   - 인간 개입 없이 Kaggle 문제 페칭, 솔루션 구축, 반복 개선, 결과 제출의 전 과정 자동화
   - 오프라인 데이터셋이나 부분 자동화에 의존하지 않는 실제 플랫폼 통합

## How

![Figure 1](figures/fig1.webp)
*내재적 및 외재적 함수의 구성적 순환 구조*

### 핵심 계산적 형식화

- **Kolb 순환의 계산적 구현**:
  - 내재적 함수 조합 I^(k)_t: 에이전트의 내부 상태 Σ_t를 반성-추상화를 통해 Σ'_t로 변환
  - 외재적 함수 E_t: 변환된 상태 Σ'_t를 기반으로 환경과 상호작용하여 피드백 F_t 획득
  - 상태 업데이트 함수 U_t: Σ_{t+1} = U_t(Σ'_t, F_t)를 통한 순차적 학습

- **ReAct 기반 기본 인지 단위**:
  - 단일 reflect-act 루프를 최소 intrinsic-extrinsic 순환으로 모델링
  - 다중 ReAct 단계 연쇄를 통해 완전한 Kolb 순환으로 확장

- **Vygotsky의 ZPD를 통한 스캐폴딩 학습**:
  - **1단계**: 구조화된 작업 환경(preprocessing, modeling, optimization)에서의 스캐폴드 기반 학습
  - **2단계**: 에이전트의 ZPD 범위 내에서의 경험적 학습
  - **3단계**: ZPD를 넘어 자유형(scaffold-free) 일반화 학습

- **Agent K의 구체적 파이프라인**:
  - 내부 상태: <task_info>, <plan>, <code>, <error>, <error_analysis> 등의 컨텍스트 누적
  - 반복적 오류 분석 및 코드 정제: I^1_t(Σ_t) = Σ_t ∪ {<error_analysis_k>}
  - 도구 사용: 데이터 전처리, 모델 구축, 하이퍼파라미터 최적화를 위한 통합 도구 세트

- **LLM의 활용**:
  - 개방형 입출력 자연스럽게 지원하여 비구조화 동적 환경에서의 경험적 학습 가능
  - 프롬프트를 통한 요약, 오류 분석, 계획 수립 등 내재적 함수 구현

## Originality

- **인지 이론과 계산의 최초 통합**: Kolb의 경험적 학습 이론을 엄밀하게 계산적으로 형식화하고 LLM 에이전트에 적용한 최초 사례

- **Vygotsky ZPD의 계산적 구현**: 스캐폴드된 환경 → 자율 학습으로의 단계적 전이를 명확하게 구조화

- **내재적-외재적 함수 분리**: 기존의 ReAct 같은 단순 reflect-act 패턴을 일반화하여 복잡한 다단계 추론을 가능하게 함

- **완전 자동화된 실제 경진대회 시스템**: 이전 AutoML이나 부분 자동화 연구와 달리, 실제 Kaggle 플랫폼에 직접 통합되어 최종 리더보드에서 인간과 경쟁하는 첫 사례

- **모달리티 불문 일관된 성능**: 표형, 비전, NLP 등 다양한 도메인에서 단일 프레임워크로 최상위 성능 달성

## Limitation & Further Study

- **LLM 의존성**: Agent K는 LLM의 추론 능력에 근본적으로 의존하므로, LLM 성능 향상과 비용 감소 필요

- **계산 비용**: 각 실험 단계마다 LLM 호출이 반복되어 상당한 계산 자원과 비용 소모 (구체적 비용-효율성 분석 부재)

- **오류 분석의 한계**: 복잡한 데이터 과학 문제에서 LLM 기반 오류 분석이 항상 정확하지 않을 수 있음

- **스캐폴딩 설계의 일반성**: 현재 스캐폴딩 구조(preprocessing, modeling, optimization)가 데이터 과학에 특화되어 있어, 다른 도메인으로의 전이 가능성이 불명확함

- **후속 연구 방향**:
  - 더 효율적인 LLM 활용을 통한 계산 비용 감축 메커니즘
  - 다양한 도메인(로봇 제어, 과학 연구 등)으로의 Kolb-Vygotsky 프레임워크 확장
  - 내재적 함수의 효과성을 더 깊이 분석하는 ablation study 강화
  - 인간과의 하이브리드 협업 시나리오 탐색

## Evaluation

- **Novelty**: 4.5/5
  - Kolb-Vygotsky 이론의 계산적 형식화는 혁신적이며, 기존 에이전트 연구와 구별되는 명확한 원리 기반 접근
  - 다만, ReAct 등 기존 개념의 자연스러운 확장으로 볼 여지도 있음

- **Technical Soundness**: 4/5
  - 내재적-외재적 함수의 형식화와 구현이 명확하고 일관성 있음
  - 단, LLM 기반 오류 분석의 정확성, 스캐폴딩 설계의 일반성에 대한 이론적 보증 부족
  - 대규모 실제 환경에서의 재현성 검증 필요

- **Significance**: 5/5
  - 완전 자동화된 에이전트가 실제 최고 난이도의 인간 경진대회에서 최상위 수준 달성은 AI 일반화 분야의 이정표
  - 경험적 학습과 구조화된 추론의 통합은 향후 자율 에이전트 설계의 중요한 패러다임 제시

- **Clarity**: 4.5/5
  - 인지 이론에서 계산 모델로의 전환 과정이 논리적이고 명확함
  - Figure 1-2의 시각화가 개념 이해를 돕고, 구체적 파이프라인 설명도 상세함
  - 다만, 일부 기술 세부사항(예: 정확한 프롬프트, 하이퍼파라미터)이 부족할 수 있음

- **Overall**: 4.5/5

**총평**: 본 논문은 인지 과학 이론(Kolb, Vygotsky)을 엄밀하게 계산적으로 구현하여 LLM 기반 자율 에이전트의 설계 원리를 제시하고, 이를 실제 최고 수준의 Kaggle 경진대회에서 검증함으로써 AI 일반화 능력의 새로운 수준을 입증한 매우 의미 있는 연구이다. 다만 계산 효율성, 오류 분석 정확성, 다른 도메인으로의 확장성 측면에서는 추가 연구가 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/594_OSDA_Agent_Leveraging_Large_Language_Models_for_De_Novo_Desi/review]] — Kaggle 경쟁과 자동화된 데이터 과학에서 각각 학습 이론과 케이스 기반 추론이라는 서로 다른 이론적 기반을 사용한다.
- 🔗 후속 연구: [[papers/828_Towards_end-to-end_automation_of_AI_research/review]] — 데이터 과학 경쟁에서 검증된 자율 학습 능력을 과학 연구 전체 과정으로 확장하여 완전 자동화를 달성한다.
- 🏛 기반 연구: [[papers/121_Autokaggle_A_multi-agent_framework_for_autonomous_data_scien/review]] — 자동화된 데이터 과학의 다중 에이전트 접근법에 대한 구체적 구현 사례를 제공한다.
- 🔗 후속 연구: [[papers/429_Infiagent-dabench_Evaluating_agents_on_data_analysis_tasks/review]] — 기본적인 데이터 분석 평가를 실제 경진대회 수준의 고난도 작업으로 확장하여 더 도전적인 벤치마크를 제공한다.
- 🔄 다른 접근: [[papers/594_OSDA_Agent_Leveraging_Large_Language_Models_for_De_Novo_Desi/review]] — 케이스 기반 추론과 경험적 학습 이론이라는 서로 다른 이론적 접근으로 자동화된 데이터 과학을 구현한다.
