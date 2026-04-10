---
title: "596_OWL_Optimized_Workforce_Learning_for_General_Multi-Agent_Ass"
authors:
  - "Mengkang Hu"
  - "Yuhang Zhou"
  - "Wendong Fan"
  - "Yuzhou Nie"
  - "Bowei Xia"
date: "2025.06"
doi: "10.48550/arXiv.2505.23885"
arxiv: ""
score: 4.2
essence: "LLM 기반 다중 에이전트 시스템에서 도메인별 특화된 설계로 인한 이식성 부족 문제를 해결하기 위해, 전략 계획(Planner)과 도메인 특화 실행(Worker)을 분리한 모듈식 WORKFORCE 프레임워크와 이를 최적화하는 OWL 학습 패러다임을 제안한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-agent_Task_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Hu et al._2025_OWL Optimized Workforce Learning for General Multi-Agent Assistance in Real-World Task Automation.pdf"
---

# OWL: Optimized Workforce Learning for General Multi-Agent Assistance in Real-World Task Automation

> **저자**: Mengkang Hu, Yuhang Zhou, Wendong Fan, Yuzhou Nie, Bowei Xia, Tao Sun, Ziyu Ye, Zhaoxuan Jin, Yingru Li, Qiguang Chen, Zeyu Zhang, Yifeng Wang, Qianshuo Ye, Bernard Ghanem, Ping Luo, Guohao Li | **날짜**: 2025-06-11 | **DOI**: [10.48550/arXiv.2505.23885](https://doi.org/10.48550/arXiv.2505.23885)

---

## Essence

![Figure 2](figures/fig2.webp)
*Figure 2: WORKFORCE와 OWL의 개요. 기존 접근과 달리 새 도메인 적응 시 전체 재학습 없이 모듈식 확장 가능*

LLM 기반 다중 에이전트 시스템에서 도메인별 특화된 설계로 인한 이식성 부족 문제를 해결하기 위해, 전략 계획(Planner)과 도메인 특화 실행(Worker)을 분리한 모듈식 WORKFORCE 프레임워크와 이를 최적화하는 OWL 학습 패러다임을 제안한다.

## Motivation

- **Known**: 최근 LLM 기반 다중 에이전트 시스템(MAS)이 복잡한 현실 작업 자동화에 유망한 결과 보임. 기존 MAS(MetaGPT, MALT 등)는 도메인별 성능 우수.
  
- **Gap**: (1) 추론 단계: 새 도메인 적용 시 전체 아키텍처 재설계 필요. (2) 학습 단계: 모든 에이전트 컴포넌트를 재학습해야 하므로 확장성 제한. 기존 시스템들은 도메인 특화 설계로 교차 도메인 이식성이 매우 낮음.

- **Why**: 현실 세계 작업은 다양한 도메인을 포함하므로 범용 AI 어시스턴트 구현에는 모듈식이고 재사용 가능한 아키텍처 필수.

- **Approach**: (1) 도메인 불가지론 Planner(작업 분해) + Coordinator(작업 관리) + 도메인 특화 Worker nodes(도구 호출)로 구성된 계층적 다중 에이전트 프레임워크 제안. (2) Planner만 최적화하고 Worker는 교체 가능한 OWL 훈련 패러다임 도입.

## Achievement

![Figure 1](figures/fig1.webp)
*Figure 1: GAIA 벤치마크에서 WORKFORCE와 OWL의 성능 비교. 상용 시스템 OpenAI Deep Research 능가*

1. **최첨단 성능**: WORKFORCE는 GAIA 벤치마크에서 69.70% 정확도 달성, OpenAI Deep Research (55.15%) 대비 2.34% 초과, 기존 오픈소스 SOTA (67.46%) 능가

2. **효율적 학습**: OWL로 훈련된 Qwen2.5-32B-Instruct 모델이 52.73% (+16.37%) 달성, GPT-4o-mini (47.27%), Qwen2.5-72B-Instruct (49.09%) 초과. GAIA 데이터 미사용 학습으로도 일반화 능력 입증

3. **모듈식 확장성**: 새 도메인 적응 시 Worker nodes만 추가/수정하면 되므로 재설계 및 재훈련 최소화

## How

![Figure 3](figures/fig3.webp)
*Figure 3: WORKFORCE 프레임워크 개요. Planner, Coordinator, Worker Pool의 계층적 구조*

**추론 메커니즘 (Inference)**:
- **Planner Agent**: 사용자 질문을 분석하여 worker 역량 레지스트리 기반 세부 작업으로 분해
- **Coordinator Agent**: Worker 역량 평가 후 적절한 worker에 작업 할당, 작업 의존성 관리, 결과 통합
- **Worker Nodes**: 웹 에이전트(검색, 웹 콘텐츠 추출), 문서 처리 에이전트(멀티모달 데이터), 추론/코딩 에이전트(분석, 코드 실행) 등 도메인 특화 도구 활용하여 작업 수행
- **Task Channel**: 중앙화된 공유 채널로 작업 및 결과 통신, Worker 간 직접 메시징 제거로 컨텍스트 정리
- **Replanning Mechanism**: Worker 실패 감지 시 자동 재계획으로 추론 시간 스케일링 가능

**훈련 메커니즘 (OWL)**:
- **2단계 훈련**: (1) Supervised Fine-Tuning(SFT)으로 Planner 초기화, (2) 실제 환경 피드백 기반 강화학습(RL)으로 일반화 능력 향상
- **도메인 불가지론 Planner 최적화**: Worker 아키텍처 변경 없이 Planner만 학습하므로 재훈련 오버헤드 최소화
- **Custom Dataset**: GAIA 벤치마크 미사용 독립적 데이터셋으로 훈련하여 도메인 간 일반화 검증

## Originality

- **모듈식 아키텍처의 혁신성**: 도메인 불가지론 계획과 도메인 특화 실행의 명확한 분리로 추론/훈련 단계 모두에서 교차 도메인 이식성 달성. 기존 MAS와 근본적으로 다른 설계 철학

- **OWL 훈련 패러다임**: Planner만 최적화하는 부분 훈련 접근으로 전체 에이전트 재훈련의 계산 부담 해결. 강화학습과 실제 환경 피드백 활용으로 일반화 강화

- **Replanning 메커니즘**: 실패 기반 동적 재계획으로 추론 시 복잡도에 따른 자동 스케일링 가능

- **벤치마크 결과 우월성**: 상용 시스템 초과 달성 + 32B 오픈소스 모델로 70B+ 모델 능가

## Limitation & Further Study

- **Worker 설계의 일반성 미검증**: 제시된 3개 Worker(웹, 문서, 추론)가 모든 도메인을 충분히 커버하는지 불명확. 도메인 특화 Worker 설계 원칙 부재
  
- **Task Channel 확장성**: 중앙화된 통신 메커니즘이 매우 많은 Worker 규모로 확장 시 병목 가능성

- **OWL 훈련 데이터 정보 부족**: Custom dataset의 규모, 구성, 도메인 분포에 대한 상세 정보 부족으로 재현성 제한

- **실제 환경 피드백의 정의 모호**: RL에서 "실제 환경 피드백"이 정확히 무엇인지(자동 평가? 휴먼 레이블?) 불명확

- **후속 연구**: (1) Worker 모듈식 설계 원칙 체계화, (2) 매우 큰 에이전트 수 처리 위한 분산 통신 메커니즘, (3) 더 다양한 도메인 작업에서의 일반화 검증, (4) OWL RL 보상 함수의 자동화 및 일반화

## Evaluation

- **Novelty (독창성)**: 4.5/5 - 도메인-작업 분리의 명확한 아이디어와 부분 훈련 패러다임은 다중 에이전트 설계에서 신선함. 다만 개별 컴포넌트 기술은 기존 기법 조합

- **Technical Soundness (기술적 견고성)**: 4/5 - 계층적 아키텍처와 훈련 방법론이 논리적으로 일관되고 잘 설계됨. 다만 OWL RL 상세 구현과 Task Channel 확장성 분석 필요

- **Significance (중요성)**: 4.5/5 - 도메인 간 이식성이 실제 문제이며, 해결책이 범용 AI 어시스턴트 개발에 중요. 벤치마크 성과도 설득력 있음

- **Clarity (명확성)**: 4/5 - 전체 구조는 명확하나, OWL 훈련 상세(reward signal, RL 알고리즘, dataset)와 Worker 설계 원칙이 불충분하게 기술됨

- **Overall**: 4.2/5

**총평**: WORKFORCE와 OWL은 다중 에이전트 시스템의 도메인 간 이식성 문제에 우아한 모듈식 해결책을 제시하며, GAIA 벤치마크에서 상용 시스템을 초과하는 성능을 달성했다는 점에서 실질적 기여가 있다. 다만 Worker 설계 일반화, 학습 메커니즘 상세화, 보다 다양한 도메인 검증 등이 추가되면 영향력이 더 높아질 것으로 예상된다.

## Related Papers

- 🔗 후속 연구: [[papers/120_AutoGen_Enabling_Next-Gen_LLM_Applications_via_Multi-Agent_C/review]] — OWL의 모듈식 WORKFORCE 프레임워크가 AutoGen의 다중 에이전트 시스템을 도메인 이식성 문제 해결을 위해 발전시킨 확장된 아키텍처이다.
- 🏛 기반 연구: [[papers/823_Towards_a_Science_of_Scaling_Agent_Systems/review]] — 에이전트 시스템 확장의 과학이 OWL의 일반화된 다중 에이전트 지원 시스템 설계의 이론적 기반과 확장성 원리를 제공한다.
- 🧪 응용 사례: [[papers/464_Large_Language_Model_based_Multi-Agents_A_Survey_of_Progress/review]] — 대규모 언어 모델 기반 다중 에이전트의 진행 조사가 OWL의 범용 다중 에이전트 프레임워크 개발에 직접적으로 적용되는 방법론적 통찰이다.
- 🔗 후속 연구: [[papers/120_AutoGen_Enabling_Next-Gen_LLM_Applications_via_Multi-Agent_C/review]] — OWL의 모듈식 WORKFORCE 프레임워크가 AutoGen의 대화형 다중 에이전트 시스템을 도메인 범용성을 위해 발전시킨 확장 버전이다.
