---
title: "620_Physics-Informed_Autonomous_LLM_Agents_for_Explainable_Power"
authors:
  - "Junhua Liu"
  - "Fanfan Lin"
  - "Xinze Li"
  - "Shuai Zhao"
  - "K. Lim"
date: "2024"
doi: "10.1609/aaai.v40i47.41441"
arxiv: ""
score: 4.25
essence: "본 논문은 대규모 언어모델(LLM) 기반 자율 에이전트인 PHIA(Physics-Informed Autonomous Agent)를 제안하여, 신재생에너지 시스템의 전력변환기 변조 설계를 자동화하고 최소한의 인간 개입으로 고품질 설계를 생성한다. 물리 정보 신경망과 최적화 알고리즘을 통합함으로써 설명 가능성과 확장성을 동시에 달성한 획기적인 접근법이다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Specialized_Domain_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liu et al._2024_Physics-Informed Autonomous LLM Agents for Explainable Power Electronics Modulation Design.pdf"
---

# Physics-Informed Autonomous LLM Agents for Explainable Power Electronics Modulation Design

> **저자**: Junhua Liu, Fanfan Lin, Xinze Li, Shuai Zhao, K. Lim | **날짜**: 2024 | **DOI**: [10.1609/aaai.v40i47.41441](https://doi.org/10.1609/aaai.v40i47.41441)

---

## Essence

![Figure 2](figures/fig2.webp)
*PHIA 시스템 아키텍처: 엔지니어가 채팅 인터페이스를 통해 설계 요구사항을 제공하면, 플래너가 도구 세트를 조율하여 인간 개입 없이 변조 설계를 반복적으로 생성*

본 논문은 대규모 언어모델(LLM) 기반 자율 에이전트인 PHIA(Physics-Informed Autonomous Agent)를 제안하여, 신재생에너지 시스템의 전력변환기 변조 설계를 자동화하고 최소한의 인간 개입으로 고품질 설계를 생성한다. 물리 정보 신경망과 최적화 알고리즘을 통합함으로써 설명 가능성과 확장성을 동시에 달성한 획기적인 접근법이다.

## Motivation

- **Known**: 재생에너지 통합으로 인한 다중자원 전력시스템의 복잡도 증가로 인해, 전력변환기의 변조 설계가 수동 계산으로는 불가능해짐. 기존 AI 기반 자동화 방법들(XGBoost, Q-learning 등)도 도입되었으나 여전히 한계 존재.

- **Gap**: 기존 방법들의 주요 문제점:
  1. 대규모 시뮬레이션/실험 데이터 요구로 인한 높은 학습 비용
  2. 대규모 모델 학습의 계산 집약성과 에너지 소비
  3. 설명 불가능한 '블랙박스' 모델로 인한 산업 적용 제약
  4. 특정 변조 전략에 한정되어 확장성 부족
  5. 설계 프로세스 전반에 걸친 광범위한 인간 개입

- **Why**: 탄소중립 전환을 위해 신재생에너지 시스템의 최적화가 시급하며, 설명 가능하고 확장 가능한 자동화 솔루션이 필수적.

- **Approach**: LLM 기반 플래너를 중심으로 사용자 요구사항을 자연언어로 처리하고, 물리 정보 대리모델(Surrogate Model)과 최적화 알고리즘을 도구로 활용하여 자율적으로 최적 설계를 생성하고 반복 개선.

## Achievement

![Figure 3](figures/fig3.webp)
*계층적 물리 정보 대리모델: ModNet(스위치 레벨 모델링)과 CirNet(시스템 레벨 모델링) 두 개의 물리 정보 신경망으로 구성하여 전력변환기의 복잡한 동작 정확도 향상*

1. **성능 우수성**: 저데이터 시나리오에서 최고 벤치마크 대비 63.2%, 고데이터 시나리오에서 23.7% 더 낮은 표준평균절대오차(SMAE) 달성

2. **설계 시간 대폭 단축**: 전통적 방법 대비 33배 이상 빠른 설계 프로세스 실현

3. **전문가 검증**: 20명의 도메인 전문가를 대상으로 한 사용자 연구에서 우수한 설계 효율성과 사용성 확인

4. **물리 정보 대리모델 개발**: 희소 데이터 환경에서도 높은 정확도를 유지하는 계층적 구조의 신경망 모델 제시

## How

![Figure 1](figures/fig1.webp)
*전력변환기 응용 사례: DAB(Dual Active Bridge) 변환기는 DC 트랜스포머로서 다양한 DC 버스를 연결하며, 스위치 변조가 전력 전송 효율, 전압 조절, 시스템 안정성에 직접 영향*

**PHIA 시스템의 주요 구성요소 및 작동 방식:**

- **LLM 기반 플래너 모듈**: 채팅 인터페이스를 통해 사용자의 자연언어 요구사항을 대화형으로 획득하고 검증. 설계 사양(operating conditions, modulation strategy, performance objectives)을 자동으로 추출

- **계층적 물리 정보 대리모델**:
  - **ModNet**: 스위치 레벨에서의 전환 동작(switching behaviors) 학습
  - **CirNet**: 시스템 레벨에서의 회로 물리 법칙 학습
  - 두 네트워크의 계층적 결합으로 복잡한 동작 정확도 향상

- **최적화 알고리즘**: 물리 정보 대리모델과 협력하여 사용자 설계 사양에 맞는 최적 변조 파라미터를 반복적으로 도출

- **설명 가능성 인터페이스**: 설계 프로세스 전체에서 텍스트 설명과 시각화 출력 제공으로 의사결정의 투명성 보장

**문제 정의:**
주어진 전력변환기의 운영 조건(정격 전력 Pr, 실제 전력 Pa, 정격/실제 입출력 전압 등), 선택된 변조 전략 S, 우선순위가 지정된 성능 목표 O에 대해, 최적 성능을 달성하는 변조 파라미터를 설계하는 것.

## Originality

- **LLM-에이전트와 물리 정보 신경망의 통합**: 기존에는 분리되어 있던 LLM 기반 자동화와 물리 정보 기반 학습을 결합하여 설명 가능성과 정확성을 동시에 달성

- **대화형 요구사항 획득**: 단순한 파이프라인 기반 방식에서 벗어나 LLM 플래너가 사용자와의 대화를 통해 동적으로 설계 요구사항을 정제

- **계층적 대리모델 아키텍처**: 스위치 레벨과 시스템 레벨 모델링을 분리하여 각각의 물리 법칙을 독립적으로 학습하면서도 전체적 정확도를 향상

- **희소 데이터 환경에서의 강건성**: 물리 정보 제약 조건을 통합하여 제한된 학습 데이터에서도 높은 성능 유지

- **산업 워크플로우 변혁**: 채팅 기반 인터페이스로 엔지니어의 접근성 향상 및 반복적 설계 개선 가능

## Limitation & Further Study

- **도메인 특화성**: 현재 DAB 변환기와 같은 특정 전력변환기에 초점. 다양한 변환기 토폴로지로의 확장성 검증 필요

- **대리모델의 일반화**: 물리 정보 신경망이 학습 데이터 범위 밖의 극단적 운영 조건에서의 성능 보장이 불명확

- **LLM 의존성**: GPT-4 등 특정 LLM에 의존하며, 모델 업데이트나 API 변경에 따른 안정성 영향 가능성

- **실하드웨어 검증 부재**: 시뮬레이션 기반 평가가 주이며, 실제 전력변환기 하드웨어에서의 동작 검증 필요

- **후속 연구 방향**:
  - 다중 변환기 및 복잡한 토폴로지 시스템으로의 확장
  - 실시간 성능 모니터링 및 온라인 설계 파라미터 조정 기능 추가
  - 다양한 LLM 모델과의 호환성 및 견고성 평가
  - 산업 규모 실증 프로젝트 수행


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.25/5

**총평**: 본 논문은 LLM 기반 자율 에이전트와 물리 정보 신경망을 창의적으로 결합하여 전력전자 설계 자동화라는 실질적인 산업 문제를 해결한 우수한 연구이며, 33배의 설계 속도 개선과 63.2%의 오차 감소로 실용성을 입증했다. 다만 실제 하드웨어 검증과 다양한 토폴로지로의 확장 가능성 검증이 보강되면 더욱 강력한 기여가 될 수 있을 것으로 기대된다.

## Related Papers

- 🏛 기반 연구: [[papers/308_El_Agente_An_Autonomous_Agent_for_Quantum_Chemistry/review]] — 물리 정보 기반 자율 LLM 에이전트의 설명 가능성을 양자화학 워크플로우에 적용할 수 있다
- 🔗 후속 연구: [[papers/526_MechAgents_Large_language_model_multi-agent_collaborations_c/review]] — 전력 시스템 분석을 위한 물리 정보 기반 자율 LLM 에이전트가 MechAgents의 역학 문제 해결을 다른 공학 영역으로 확장한 적용이다.
