---
title: "831_Towards_llm_agents_for_earth_observation"
authors:
  - "C. H. Kao"
  - "Wenting Zhao"
  - "Shreelekha Revankar"
  - "Samuel Speas"
  - "Snehal Bhagat"
date: "2025"
doi: "arXiv:2504.12110"
arxiv: ""
score: 4.0
essence: "본 논문은 지구 관측(Earth Observation, EO) 작업을 자동화하기 위한 LLM 에이전트의 준비도를 평가하기 위해 **UnivEARTH** 벤치마크를 제시하고, 현재 최첨단 모델들이 코드 실행 실패(58%)로 인해 33% 수준의 낮은 정확도만 달성함을 보여준다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Scientific_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Kao et al._2025_Towards llm agents for earth observation.pdf"
---

# Towards LLM Agents for Earth Observation

> **저자**: C. H. Kao, Wenting Zhao, Shreelekha Revankar, Samuel Speas, Snehal Bhagat, Rajeev Datta, Cheng Perng Phoo, Utkarsh Mall, Carl Vondrick, Kavita Bala, Bharath Hariharan | **날짜**: 2025 | **DOI**: [arXiv:2504.12110](https://arxiv.org/abs/2504.12110)

---

## Essence

![Figure 1](figures/fig1.webp)
*UnivEARTH 벤치마크는 NASA Earth Observatory 기사에서 추출한 140개의 지구 관측 관련 예/아니오 질문으로 구성되며, Google Earth Engine API를 활용하여 LLM 에이전트를 평가한다.*

본 논문은 지구 관측(Earth Observation, EO) 작업을 자동화하기 위한 LLM 에이전트의 준비도를 평가하기 위해 **UnivEARTH** 벤치마크를 제시하고, 현재 최첨단 모델들이 코드 실행 실패(58%)로 인해 33% 수준의 낮은 정확도만 달성함을 보여준다.

## Motivation

- **Known**: 지구 관측은 환경 모니터링, 재해 관리, 기후 과학 등 다양한 과학 분야에서 중요한 역할을 하며, 단순 자동화 시스템들이 존재하지만 범용적 커스터마이징 쿼리에는 유연성이 부족함
- **Gap**: LLM 기반 에이전트가 지구 관측 작업을 신뢰할 수 있게 자동화할 수 있는지에 대한 체계적 평가 및 벤치마크 부재
- **Why**: 과학 워크플로우에서 올바른 센서, 상품, 위치, 시간을 선택하는 것이 복잡하고 도메인 특화적 지식이 필요하며, 이를 AI가 수행할 수 있는지 검증이 필요함
- **Approach**: NASA Earth Observatory의 신뢰할 수 있는 기사를 기반으로 고품질의 질문-답변 쌍을 엄격히 선별하고, Google Earth Engine API를 활용한 코드 생성 능력으로 LLM 에이전트를 벤치마킹

## Achievement

![Figure 1 - 질문 예시](figures/fig1.webp)
*다양한 주제(표면 반사율, 야간 조명, 산림 범위, 눈 덮음, 이산화질소 등)에 걸친 UnivEARTH의 질문 사례*

1. **고품질 벤치마크 개발**: NASA Earth Observatory 기사에서 추출한 140개의 검증된 예/아니오 질문으로 구성된 UnivEARTH 데이터셋 (13개 주제, 17개 센서/데이터셋)을 구축하여 과학적 신뢰성 확보

2. **신뢰할 수 있는 근거 기반 평가**: 단순 질문 답변뿐 아니라 Google Earth Engine Python API를 활용한 코드 생성으로 근거 기반 답변을 강제하여 더 엄격한 평가 프레임워크 제시

3. **현저한 성능 격차 규명**: Claude-3.7-Sonnet, DeepSeek-V3, DeepSeek-R1, o3-mini 등 최신 모델들이 코드 생성 실패(58%)로 인해 33% 수준의 낮은 정확도만 달성하는 현실을 객관적으로 입증

## How

- **데이터 수집**: Claude-3.5-Sonnet을 활용하여 NASA 기사 분석 및 후보 질문-답변 쌍 생성, 초기 편집 통과 실시
- **검증 단계**: Google Earth Engine에서 데이터 가용성 확인 및 JavaScript 코드 에디터로 테스트 구현 수행
- **독립적 리뷰**: 4명의 리뷰어를 통해 질문 답변 가능성(Q1), 텍스트 기반 근거(Q2), 이미지 기반 근거(Q3), 위치 정보 검증(Q4) 평가 후 반복적 개선 (최종 Q1 100% 동의)
- **다중 프롬프팅 전략**: 제로샷(zero-shot), 퓨샷(few-shot 3개 예시), 반성 기반(reflexion 3라운드) 접근법으로 평가
- **정량 평가 지표**: 정확도(Accuracy), 거절률(Rejection Rate), 선택적 정확도(Selective Accuracy) 측정

## Originality

- **독창적 데이터 소스**: NASA Earth Observatory라는 신뢰할 수 있는 공식 자료를 활용하여 기존 벤치마크와 달리 과학적 신뢰성과 현실성을 동시에 보장

- **근거 기반 평가 프레임워크**: 단순 질문-답변 정확도를 넘어 생성 코드의 실행 가능성과 데이터 접근성까지 평가하여 더 깊이 있는 분석 제시

- **도메인 특화 벤치마크**: 17개의 서로 다른 위성 센서/데이터셋과 13개 주제를 아우르는 다양성 있는 지구 관측 벤치마크로, 단순한 QA 태스크를 넘어 과학 실무와의 연결성 강조

- **엄격한 품질 관리**: 리뷰어 간 동의율 측정(Q1 90.1%-81.7%)과 반복적 개선을 통한 체계적 품질 보증

## Limitation & Further Study

- **제한된 질문 형식**: 예/아니오 질문으로만 제한되어 개방형(open-ended) 과학적 질의를 포함하지 못함, 향후 더 복잡한 질문 형식 포함 필요

- **코드 실행 의존성**: Google Earth Engine Python API의 사용이 필수이므로 API 한계(데이터셋 미가용, 계산 제약 등)가 모델 성능을 과소평가할 가능성 존재

- **모델 성능의 낮은 기준선**: 33% 수준의 정확도만으로는 실제 과학 워크플로우 도입에 미흡하므로, 모델 아키텍처 개선 및 도메인 특화 학습 방법론 개발이 시급

- **센서 데이터 가용성 편향**: GEE에서 이용 가능한 센서만 포함되어 일부 최신 또는 특화된 지구 관측 데이터가 제외됨

- **향후 연구 방향**: (1) 더 큰 규모의 벤치마크 확대, (2) 멀티모달 입력(이미지 + 텍스트) 활용, (3) 도메인 특화 LLM 파인튜닝, (4) 복합 추론이 필요한 다중 센서 쿼리 포함

## Evaluation

| 항목 | 평가 |
|------|------|
| **Novelty** | 4/5 |
| **Technical Soundness** | 4/5 |
| **Significance** | 4/5 |
| **Clarity** | 5/5 |
| **Overall** | 4/5 |

**총평**: 본 논문은 지구 관측이라는 실제 과학 도메인에서 LLM 에이전트의 신뢰성을 평가하는 의미 있는 벤치마크를 제시하며, 현 단계 AI 시스템의 현저한 한계를 객관적으로 입증함으로써 향후 연구 방향을 명확히 제시한다. 다만 질문 형식의 제한과 코드 실행 의존성으로 인한 평가 공정성 논의 필요 및 개선 방향 제시가 더 구체적일 수 있다는 점이 아쉬움.

## Related Papers

- 🔗 후속 연구: [[papers/298_Earth-Agent_Unlocking_the_Full_Landscape_of_Earth_Observatio/review]] — 지구 관측을 위한 다중 에이전트 시스템의 전체적 관점을 LLM 에이전트 준비도 평가라는 구체적 벤치마킹으로 발전시킨다.
- 🔄 다른 접근: [[papers/384_GIS_Copilot_towards_an_autonomous_GIS_agent_for_spatial_anal/review]] — 지구 관측 분야의 자동화라는 공통 목표이지만 LLM 에이전트와 GIS 분석 에이전트라는 다른 접근법을 사용한다.
- 🏛 기반 연구: [[papers/342_Foundation_Models_for_Environmental_Science_A_Survey_of_Emer/review]] — 환경과학을 위한 파운데이션 모델 조사가 지구 관측 LLM 에이전트 개발의 이론적 배경을 제공한다.
- 🔗 후속 연구: [[papers/299_Earthse_A_benchmark_evaluating_earth_scientific_exploration/review]] — 지구 관측용 LLM 에이전트에서 지구과학 탐사 능력 벤치마크로의 확장
- 🔗 후속 연구: [[papers/437_Interpreting_Multi-band_Galaxy_Observations_with_Large_Langu/review]] — 지구 관측을 위한 LLM 에이전트는 천문학적 관측 데이터 해석 기법을 지구 과학 분야로 확장 적용한다.
