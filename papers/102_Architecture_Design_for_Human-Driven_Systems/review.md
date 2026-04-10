---
title: "102_Architecture_Design_for_Human-Driven_Systems"
authors:
  - "Mahyar T. Moghaddam"
  - "Moamin B. Abughazala"
  - "Vittorio Cortellessa"
  - "Antinisca Di Marco"
  - "Henry Muccini"
date: "2021.09"
doi: "미제공"
arxiv: ""
score: 3.5
essence: "본 논문은 인간의 사회적·이동 행동을 IoT 아키텍처 설계에 통합하여 소시오-테크니컬 시스템의 지속가능성을 향상시키는 인간 중심 아키텍처 설계 방법론을 제시한다. 에이전트 기반 사회 시뮬레이션(ABSS)과 모델 주도 공학(MDE) 접근법을 결합하여 QoS(Quality of Service)와 QoE(Quality of Experience)의 균형을 맞추는 최적 아키텍처 구성을 도출한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Structured_Research_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Moghaddam et al._2021_Architecture Design for Human-Driven Systems.pdf"
---

# Architecture Design for Human-Driven Systems

> **저자**: Mahyar T. Moghaddam, Moamin B. Abughazala, Vittorio Cortellessa, Antinisca Di Marco, Henry Muccini, Fabrizio Rossi, Karthik Vaidhyanathan | **날짜**: 2021-09-21 | **DOI**: [미제공]

---

## Essence

본 논문은 인간의 사회적·이동 행동을 IoT 아키텍처 설계에 통합하여 소시오-테크니컬 시스템의 지속가능성을 향상시키는 인간 중심 아키텍처 설계 방법론을 제시한다. 에이전트 기반 사회 시뮬레이션(ABSS)과 모델 주도 공학(MDE) 접근법을 결합하여 QoS(Quality of Service)와 QoE(Quality of Experience)의 균형을 맞추는 최적 아키텍처 구성을 도출한다.

## Motivation

- **Known**: 소프트웨어 아키텍처 설계는 전통적으로 기술적 요구사항에 기반하며, 최근에는 비즈니스 가치와 지속가능성이 고려되고 있다. 그러나 인간의 사회적·개인적 지속가능성에 대한 관심은 부족하다.

- **Gap**: 기존 IoT 시스템 아키텍처 설계는 인간의 행동 패턴과 사용자 경험을 충분히 반영하지 못한다. 시스템의 QoS와 사용자의 QoE 간의 상충관계를 체계적으로 분석하고 최적화할 방법이 없다.

- **Why**: 군중 관리, 스마트 시티 등 사용자가 직접 참여하는 시스템에서는 인간의 행동이 에너지 소비, 데이터 수집 주기 등 아키텍처 결정에 직접적인 영향을 미친다.

- **Approach**: ABSS로 인간 행동을 모델링하고, CAPS 프레임워크로 IoT 아키텍처를 정의한 후, CupCarbon으로 통합 시뮬레이션을 수행하여 최적 구성을 도출한다.

## Achievement

1. **통합 설계 방법론**: 인간 행동 모델(ABM/ABSS)과 IoT 아키텍처 모델(CAPS)을 결합하는 4단계 방법론 제시
   - Agent Modeling & Simulation Stage
   - Agent-IoT Composition Stage
   - IoT Modeling & Simulation Stage
   - Analysis Stage (Trade-off Score 계산)

2. **정량적 평가 지표**: QoS/QoE 가중치 조합을 통한 Trade-off Score (ts = ws·Qs + we·Qe)로 아키텍처 선택을 자동화

3. **실제 사례 검증**: 우피치 갤러리(Uffizi Galleries) 군중 관리 시스템에 적용하여 두 가지 시나리오(혼잡도 기반/사회적 집단화)에서 최적 구성 도출

## How

- **ABSS 모델링**: PedSim을 사용하여 나이, 성별, 신체 조건, 사회적 집단화 등 인간 특성을 에이전트로 표현
  
- **IoT 아키텍처 정의**: CAPS 프레임워크로 다중 관점(소프트웨어, 하드웨어, 물리 공간) 모델링
  - 사람 카운터(People Counter)
  - 카메라(Camera)
  - RFID 리더(RFID Reader)
  - QR 리더(QR Reader)

- **센서 모드 구성**: 정상 모드(낮은 주기)와 위기 모드(높은 주기)의 두 가지 작동 모드로 에너지-정확성 균형 조절

- **시뮬레이션 실행**: 36개 시뮬레이션(6개 모델 × 3개 구성 × 2개 시나리오) 수행으로 Trade-off Score 계산

## Originality

- **인간 행동 중심 설계**: 일반적인 비즈니스/환경 지속가능성을 넘어 인간의 사회적·개인적 지속가능성을 아키텍처 설계에 명시적으로 통합

- **ABM-IoT 통합 프레임워크**: ABSS 결과를 자동으로 IoT 시뮬레이션 입력으로 변환하는 Agent-IoT Data Composition(AIDC) 프로세스 제안

- **다차원 최적화**: QoS와 QoE를 동시에 고려하는 정량적 Trade-off Score 메트릭으로 아키텍처 선택의 객관성 제공

## Limitation & Further Study

- **데이터 의존성**: 실제 행동 데이터 수집의 어려움과 시뮬레이션 파라미터 설정의 정확성에 크게 의존

- **제한된 시나리오**: 우피치 갤러리 사례에만 검증되었으며, 다양한 도메인(병원, 공항, 대중교통 등)에서의 일반화 여부 미확인

- **시뮬레이션 복잡도**: 36개 시뮬레이션만 수행되어 아키텍처 공간의 탐색이 제한적이며, 확장성 문제 미해결

- **향후 연구**: 도구화(Tool) 개발으로 실제 소프트웨어 아키텍트가 사용 가능한 형태로 발전시킬 계획


## Evaluation

- Novelty: 4/5
- Technical Soundness: 3.5/5
- Significance: 3.5/5
- Clarity: 3/5
- Overall: 3.5/5

**총평**: 인간 행동을 IoT 아키텍처 설계에 통합한다는 혁신적 아이디어와 체계적인 방법론을 제시했으나, 단일 사례 연구와 제한된 검증, 도구 부재로 인한 실용성 미흡이 주요 약점이다. 이 작업은 소시오-테크니컬 시스템 설계 분야에 중요한 기여를 하지만, 추가 사례 적용과 도구화를 통해 보완이 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/254_DataJoint_20_A_Computational_Substrate_for_Agentic_Scientifi/review]] — 인간 중심 시스템 아키텍처 설계가 에이전틱 과학 연구를 위한 계산 기반 구조 구축의 이론적 기초를 제공한다.
- 🔗 후속 연구: [[papers/175_Building_machines_that_learn_and_think_with_people/review]] — 인간과 함께 학습하고 사고하는 기계 구축 원리를 IoT 환경에서의 소시오-테크니컬 시스템으로 확장할 수 있다.
- 🧪 응용 사례: [[papers/365_Future_of_Work_with_AI_Agents_Auditing_Automation_and_Augmen/review]] — 인간 중심 아키텍처 설계 방법론을 AI 에이전트와의 미래 업무 환경 구축에 적용하여 더 효과적인 인간-AI 협업 시스템을 만들 수 있다.
- 🔄 다른 접근: [[papers/462_Large_Language_Model_Agent_as_a_Mechanical_Designer/review]] — 기계 설계 자동화에서 LLM 기반과 인간 중심 시스템 설계 접근법을 비교할 수 있습니다.
