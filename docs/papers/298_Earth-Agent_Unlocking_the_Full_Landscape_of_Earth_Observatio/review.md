---
title: "298_Earth-Agent_Unlocking_the_Full_Landscape_of_Earth_Observatio"
authors:
  - "Peilin Feng"
  - "Zhutao Lv"
  - "Junyan Ye"
  - "Xiaolei Wang"
  - "Xinjie Huo"
date: "2025.09"
doi: "미제공"
arxiv: ""
score: 4.5
essence: "본 논문은 RGB 이미지를 넘어 다중스펙트럼 데이터와 지구 관측 제품(Earth Products)을 통합적으로 처리하는 에이전트 기반 프레임워크 Earth-Agent를 제시하며, 이를 평가하기 위한 248개의 전문가 검증 과제로 구성된 Earth-Bench 벤치마크를 소개한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/GIS_Research_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Feng et al._2025_Earth-Agent Unlocking the Full Landscape of Earth Observation with Agents.pdf"
---

# Earth-Agent: Unlocking the Full Landscape of Earth Observation with Agents

> **저자**: Peilin Feng, Zhutao Lv, Junyan Ye, Xiaolei Wang, Xinjie Huo, Jinhua Yu, Wanghan Xu, Wenlong Zhang, Lei Bai, Conghui He, Weijia Li | **날짜**: 2025-09-27 | **DOI**: [미제공](https://doi.org/)

---

## Essence

![Figure 1](figures/fig1.webp)
*Earth-Agent의 종합 개요: 기존 MLLM 기반 연구, 에이전트 기반 연구와의 비교 및 제안된 Earth-Agent의 차별성*

본 논문은 RGB 이미지를 넘어 다중스펙트럼 데이터와 지구 관측 제품(Earth Products)을 통합적으로 처리하는 에이전트 기반 프레임워크 Earth-Agent를 제시하며, 이를 평가하기 위한 248개의 전문가 검증 과제로 구성된 Earth-Bench 벤치마크를 소개한다.

## Motivation

- **Known**: 최근 다중모달 대규모 언어 모델(MLLM)은 원격탐사 이미지 분류, 객체 탐지 등 단순 인식 작업에서 우수한 성능을 보여주었으나, RGB 이미지만 처리 가능하고 단일 또는 소수 이미지 처리, 단계별 추론의 한계를 가짐

- **Gap**: 기존 에이전트 기반 지구 관측 연구(ThinkGeo, RSAgent, ChangeAgent)도 초기 단계로 RGB 인식에 국한되고, 도구 활용이 제한적이며, 추론 궤적과 최종 결과를 모두 평가하는 체계적 벤치마크 부재

- **Why**: 지구 과학자들이 수행하는 실제 분석 작업은 다중 스펙트럼 데이터(TIR, SAR, 하이퍼스펙트럼), 처리된 지구 제품(Earth Products from GEE, NASA Earthdata) 등 다양한 모달리티와 수십 개 이미지의 시공간 분석을 요구함

- **Approach**: Model Context Protocol(MCP) 기반 104개 전문 도구를 통합한 구조화된 에이전트 프레임워크(ReAct 방식)를 구축하고, 다중스펙트럼-RGB 데이터를 모두 지원하며, 추론 궤적과 결과를 함께 평가하는 벤치마크 구성

## Achievement

![Figure 2](figures/fig2.webp)
*Earth-Agent가 Spectrum, Products, RGB 데이터를 활용한 다단계 추론으로 복잡한 과제 해결: 건기지수 스파이크 계산, 야간 조명 강도 추세 분석, 항만 면적 차이 계산*

1. **포괄적 다중모달 처리**: RGB 이미지, 원본 스펙트럼 데이터, 지구 제품(NDVI, LST, TVDI 등)을 단일 프레임워크에서 통합 처리. 기존 MLLM은 RGB만 지원하던 것에서 진화

2. **체계적 도구 생태계**: 104개 전문 도구를 Index(지수 계산), Inversion(역산), Perception(인식), Analysis(분석), Statistics(통계) 등 5개 도메인 특화 toolkit으로 구조화. MCP 기반으로 확장성 보장

3. **다단계 복잡 추론**: 단순 분류/VQA를 넘어 지구물리학 매개변수 역산, 시공간 추세 분석 등 다단계 과학적 분석 지원

4. **이중수준 평가 프로토콜**: 추론 궤적(reasoning trajectory)과 최종 결과를 모두 평가하는 8가지 메트릭(Tools_any_order, Tools_in_order, Tools_exact_match, Parameters, Step by Step, End to End, Efficiency, Accuracy)

5. **Earth-Bench 벤치마크**: 13,729개 이미지, 248개 전문가 검증 질문으로 구성되어 스펙트럼, 제품, RGB 모달리티 모두 포함

## How

![Figure 3](figures/fig3.webp)
*Earth-Agent 프레임워크: ReAct 스타일 워크플로우를 통한 LLM 기반 추론과 도구 호출의 상호작용*

- **ReAct 기반 에이전트 루프**: LLM(Claude, GPT-4 등)이 현재 상태를 관찰(Observation) → 사고(Thought) → 행동(Action, 도구 호출 또는 최종 답변)의 순환 구조로 다단계 추론 수행

- **MCP 프로토콜 기반 도구 통합**: Model Context Protocol을 활용하여 다양한 외부 도구, 모델, 데이터소스(Google Earth Engine, NASA Earthdata, 전문 RS 모델)를 표준화된 방식으로 연결

- **구조화된 Toolkit**: 5개 도메인 특화 키트로 104개 도구 조직화
  - **Index Toolkit**: NDVI, NDBI, LST, TVDI 등 원격탐사 지수 계산
  - **Inversion Toolkit**: 에어로졸 광학 두께 등 역산 모델
  - **Perception Toolkit**: SM3Det, SAM2 등 객체 탐지/분할 모델
  - **Analysis Toolkit**: 변화 탐지, 추세 분석 등 시공간 분석
  - **Statistics Toolkit**: 선형 회귀, 통계 검정 등 정량 분석

- **이중 쿼리 모드**: 
  - Auto-Planning: 질문에 대해 에이전트가 자동으로 도구 호출 계획
  - Instruction-Following: 명시적 도구 호출 지시를 포함한 질문

- **평가 메커니즘**:
  - **궤적 평가**: 도구 사용 순서 정확성(Tools_exact_match), 매개변수 정확성(Parameters)
  - **결과 평가**: 최종 답변 정확도(End to End), 효율성(Efficiency)

## Originality

- **첫번째 통합 EO 에이전트**: 지구 관측 분야에서 RGB와 스펙트럼 데이터를 동시에 지원하는 첫 에이전트 프레임워크. 기존 연구는 RGB 또는 단순 분류 작업에만 국한

- **MCP 기반 구조화된 도구 생태계**: 표준화된 프로토콜로 104개 도구를 체계적으로 통합하여 확장성과 상호운용성 확보. 이전 연구는 미리 정의된 도구 생태계 부재

- **이중수준 평가 프로토콜의 혁신**: 추론 궤적을 포함한 평가는 "어떻게 답했는가"를 중시하는 과학적 엄밀성 추구. 기존 벤치마크는 최종 답변만 평가

- **전문가 검증 멀티모달 벤치마크**: 13,729개 이미지와 248개 전문가 검증 질문으로 구성된 Earth-Bench는 실제 지구과학 워크플로우를 반영하여 단순 원격탐사 벤치마크와 차별화

- **정량적 시공간 추론**: 시계열 트렌드 분석, 면적 계산, 통계 검정 등 기존 MLLM이 지원하지 못했던 정량적 분석 지원으로 지구과학 적용성 확대

## Limitation & Further Study

- **도구 정의의 한계**: 104개 도구로도 모든 지구 관측 작업을 커버하기 어려우며, 새로운 도메인(해양 관측, 빙하 모니터링 등)이 추가될 때마다 도구 확장 필요

- **LLM 추론 오류의 누적**: 다단계 추론에서 각 단계의 오류가 누적되어 최종 답변 정확도 저하 가능. 특히 복잡한 계산 단계에서 LLM의 수치 오류 발생

- **실시간 처리의 미흡**: 대량의 이미지(수십만 개) 처리 시 LLM 호출 비용과 응답 시간이 문제. 배치 처리 최적화와 캐싱 메커니즘 추가 필요

- **도메인 전문성의 한계**: LLM이 지구 관측 도메인의 암묵적 지식(예: 특정 지역의 계절 특성)을 충분히 활용하지 못할 수 있으며, 도메인 특화 사전학습(pre-training) 고려 필요

- **평가 데이터 규모**: 248개 질문은 MLLM 벤치마크 대비 작은 규모로, 모델 성능의 통계적 유의성 검증에 제한. 더 대규모 데이터셋 필요

- **후속 연구 방향**:
  - 지구 관측 특화 소규모 언어 모델(SLM) 개발으로 응답 속도 및 비용 개선
  - 다중 에이전트 협력 시스템(multi-agent collaboration) 도입으로 복잡한 대규모 분석 지원
  - 사용자 피드백을 통한 온라인 학습으로 도구 선택의 정확성 개선
  - 시계열 데이터와 공간 관계를 더 효과적으로 처리하는 구조화된 추론 메커니즘 개발


## Evaluation

- Novelty: 5/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4.5/5

**총평**: Earth-Agent는 지구 관측 분야에서 에이전트 기반 분석의 새로운 표준을 수립하는 매우 가치 있는 연구로, RGB 이미지만 처리하던 기존 MLLM의 한계를 극복하고 과학적 엄밀성을 갖춘 이중수준 평가 체계를 도입함으로써 학술적·실무적 기여도가 높다. 다만 도구 확장성, LLM 오류 축적, 실시간 처리 등의 실질적 문제 해결을 위한 후속 연구가 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/208_ChatMOF_an_artificial_intelligence_system_for_predicting_and/review]] — 지구 관측 데이터와 화학 소재라는 서로 다른 과학 영역에서 멀티모달 AI 에이전트 접근법을 비교할 수 있다.
- 🔗 후속 연구: [[papers/384_GIS_Copilot_towards_an_autonomous_GIS_agent_for_spatial_anal/review]] — GIS 분야에서 Earth-Agent의 접근법을 더 넓은 지리공간 분석으로 확장하여 자율적 데이터 검색 기능을 강화한다.
- 🏛 기반 연구: [[papers/764_Sparks_Multi-Agent_Artificial_Intelligence_Model_Discovers_P/review]] — 전문 도메인에서의 다중모달 데이터 처리가 자동화된 과학 발견의 핵심 구성요소임을 입증한다.
- 🧪 응용 사례: [[papers/299_Earthse_A_benchmark_evaluating_earth_scientific_exploration/review]] — 지구 관측 전체 환경 탐색을 지구과학 탐사 벤치마크에 적용
- 🔗 후속 연구: [[papers/831_Towards_llm_agents_for_earth_observation/review]] — 지구 관측을 위한 다중 에이전트 시스템의 전체적 관점을 LLM 에이전트 준비도 평가라는 구체적 벤치마킹으로 발전시킨다.
- 🔗 후속 연구: [[papers/098_An_autonomous_GIS_agent_framework_for_geospatial_data_retrie/review]] — 자율 GIS 에이전트 프레임워크는 Earth-Agent의 지구 관측 데이터 분석 기능을 확장하여 지리공간 데이터의 자동 발견과 다운로드까지 포괄하는 완전한 지리정보 처리 파이프라인을 제공합니다.
