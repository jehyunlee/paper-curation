---
title: "073_AI_Agents_in_Engineering_Design_A_Multi-Agent_Framework_for"
authors:
  - "Mohamed Elrefaie"
  - "Janet Qian"
  - "Raina Wu"
  - "Qian Chen"
  - "Angela Dai"
date: "2025.03"
doi: "10.48550/arXiv.2503.23315"
arxiv: ""
score: 4.2
essence: "본 논문은 자동차 설계 분야에 AI 설계 에이전트(Design Agents)를 도입하여, 스케칭부터 공기역학 시뮬레이션까지 전 설계 주기를 수 주일에서 수 분으로 단축하는 다중 에이전트 프레임워크를 제시한다. VLM, LLM, 기하 딥러닝 기법을 활용한 전문화된 에이전트들이 엔지니어와 디자이너와 협력하여 설계 창의성과 효율성을 대폭 향상시킨다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Large_Language_Model_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Elrefaie et al._2025_AI Agents in Engineering Design A Multi-Agent Framework for Aesthetic and Aerodynamic Car Design.pdf"
---

# AI Agents in Engineering Design: A Multi-Agent Framework for Aesthetic and Aerodynamic Car Design

> **저자**: Mohamed Elrefaie, Janet Qian, Raina Wu, Qian Chen, Angela Dai, Faez Ahmed | **날짜**: 2025-03-30 | **DOI**: [10.48550/arXiv.2503.23315](https://doi.org/10.48550/arXiv.2503.23315)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: AI 설계 에이전트 프레임워크로 자동차 설계 프로세스 가속화. VLM(비전-언어 모델), 기하 딥러닝, LLM을 통합하고 AutoGen으로 에이전트 간 협업 조율*

본 논문은 자동차 설계 분야에 AI 설계 에이전트(Design Agents)를 도입하여, 스케칭부터 공기역학 시뮬레이션까지 전 설계 주기를 수 주일에서 수 분으로 단축하는 다중 에이전트 프레임워크를 제시한다. VLM, LLM, 기하 딥러닝 기법을 활용한 전문화된 에이전트들이 엔지니어와 디자이너와 협력하여 설계 창의성과 효율성을 대폭 향상시킨다.

## Motivation

- **Known**: 자동차 설계는 공기역학적 성능과 미적 가치를 동시에 추구하는 복합 학제적 프로세스로, 기존 워크플로우는 개념 스케칭 → CAD 모델링 → 물리 시뮬레이션 → 최적화 → 풍동 테스트 등 수주일의 반복 개선 과정이 필수적이다.

- **Gap**: 기존 생성형 AI 연구들은 개별 단계(예: 스타일링 또는 형상 생성)에만 집중하거나 대규모 멀티모달 데이터셋 부재로 인해 미적 요소와 성능 평가를 통합하지 못했다.

- **Why**: 설계 프로세스 가속화, 설계자-엔지니어 간 협력 개선, 그리고 설계 공간의 체계적 탐색을 위해서는 엔드-투-엔드 AI 에이전트 시스템이 필요하다.

- **Approach**: DrivAerNet++ 데이터셋(8,000개 산업 표준 자동차 설계)을 기반으로 4개의 전문화된 AI 에이전트(스타일링, CAD, 메싱, 시뮬레이션 에이전트)를 AutoGen으로 조율하는 다중 에이전트 프레임워크 개발.

## Achievement

![Figure 2](figures/fig2.webp)
*Figure 2: 다중 에이전트 시스템의 상호작용 흐름. 2D 스케치 입력 → 스타일링 렌더링 → CAD 검색/생성 → 메시 생성 → 공기역학 예측*

1. **설계 사이클 가속화**: 개념 설계부터 공기역학 평가까지의 과정을 주 단위에서 분 단위로 단축하여 수십 배의 효율성 향상 달성

2. **통합형 멀티모달 프레임워크**: 2D 스케칭, 3D 형상 생성, CFD 메싱, 고충실도 공기역학 시뮬레이션을 일관되게 연결하는 최초의 엔드-투-엔드 시스템 구축

3. **실시간 성능 예측**: 대체 모델(Surrogate Model)을 통해 고비용 CFD 시뮬레이션을 대체하면서도 높은 정확도 유지

4. **설계 공간 탐색**: t-SNE 기반 비선형 차원 축소로 DrivAerNet++ 고차원 설계 공간의 고성능 설계 클러스터 식별

## How

![Figure 3](figures/fig3.webp)
*Figure 3: AI 다중 에이전트 시스템 사용 사례. 디자이너가 2D 스케치를 입력하면 다양한 스타일 옵션의 고해상도 렌더링 생성*

**핵심 방법론:**

- **스타일링 에이전트(Styling Agent)**: Stable Diffusion XL, ControlNet, DALL·E를 활용하여 설계자 프롬프트에 기반한 고해상도 렌더링 생성 및 미적 개선

- **CAD 에이전트(CAD Agent)**: DrivAerNet++ 데이터베이스에서 유사 설계 검색 또는 기하 딥러닝(DeepSDF, PointNet, RegDGCNN, TripNet) 활용 3D 메시 생성

- **메싱 에이전트(Meshing Agent)**: OpenFOAM과 상호작용하여 CFD 해석용 고품질 계산 격자 자동 생성 및 격자 품질 검증

- **시뮬레이션 에이전트(Simulation Agent)**: 사전 학습된 대체 모델로 실시간 공기역학 성능 예측 또는 데이터베이스에서 기존 시뮬레이션 결과 검색

- **AutoGen 기반 조율**: 다중 에이전트 간의 통신, 태스크 의존성 관리, 자동 워크플로우 실행

- **Python API 통합**: 엔지니어링 소프트웨어(Blender, OpenFOAM, ParaView) 자동화

## Originality

- **첫 통합형 다중 에이전트 설계 시스템**: 스케칭부터 고충실도 공기역학 평가까지 전 단계를 단일 프레임워크로 자동화한 최초 연구

- **대규모 멀티모달 데이터셋 활용**: DrivAerNet++(8,000개 자동차 + CFD 데이터)를 이용한 학습으로 실제 산업 기준 설계 반영

- **설계 공간 분석**: 고차원 설계 공간의 체계적 탐색을 위한 비선형 차원 축소 기법 적용

- **에이전트 간 협력 아키텍처**: AutoGen 기반의 자동 태스크 조율로 인간-AI 협력의 새로운 패러다임 제시

- **엔지니어링 도구 네이티브 통합**: 기존 산업용 소프트웨어(OpenFOAM, Blender)와의 직접 상호작용으로 실무 적용성 확보

## Limitation & Further Study

**한계:**
- 본문에 명시되지 않았으나, 제한된 설계 도메인(승용차 중심)에서의 검증
- 대체 모델의 성능한계 및 복잡한 설계 변형에 대한 일반화 가능성 미검증
- 사용자 선호도 및 브랜드 정체성 같은 주관적 요소의 정량화 어려움
- CFD 메싱 자동화의 품질 편차 가능성

**후속 연구:**
- 항공우주, 산업용품 등 다양한 엔지니어링 도메인으로 프레임워크 확장
- 구조 해석(FEA), 열 해석 등 추가 물리 시뮬레이션 통합
- 사용자 피드백 루프를 통한 대체 모델 온라인 학습
- 제조 제약(금형, 공정 한계) 조건의 자동 포함
- 멀티에이전트 시스템의 자동 최적화 전략 개발

## Evaluation

- **Novelty**: 4.5/5 — 다중 에이전트 프레임워크와 엔드-투-엔드 통합이 신규이나, 개별 기술(VLM, 대체 모델)은 기존 기법 활용

- **Technical Soundness**: 4/5 — 체계적인 방법론이나 검증 세부사항(모델 성능 메트릭, 비교 실험)이 본문에 부분적으로만 제시

- **Significance**: 4.5/5 — 설계 산업의 실질적 시간 단축과 다분야 확장 가능성이 높으나, 아직 산업 파일럿 단계 미소개

- **Clarity**: 4/5 — 시스템 아키텍처와 사용 사례는 명확하나, 기술 세부 구현(에이전트 간 메시지 형식, 오류 처리)은 불충분

- **Overall**: 4.2/5

**총평**: 본 논문은 생성형 AI와 기하 딥러닝을 자동차 설계에 체계적으로 통합한 혁신적 프레임워크를 제시하며, 산업 규모 데이터셋과 자동화된 워크플로우를 통해 설계 사이클 획기적 단축을 입증했다. 다만 정량적 성능 평가와 실제 설계 프로젝트에서의 엔드유저 피드백이 추가되면 학술적 임팩트와 실무 적용성이 한층 강화될 것으로 기대된다.

## Related Papers

- 🔄 다른 접근: [[papers/084_Ai-driven_robotics_for_free-space_optics/review]] — 자동차 설계와 광학 실험 모두 물리적 시스템의 AI 기반 자동화를 다룹니다.
- 🏛 기반 연구: [[papers/849_UI-TARS_Pioneering_Automated_GUI_Interaction_with_Native_Age/review]] — 네이티브 에이전트의 상호작용이 엔지니어링 설계 자동화의 기반을 제공합니다.
- 🔗 후속 연구: [[papers/462_Large_Language_Model_Agent_as_a_Mechanical_Designer/review]] — 자동차 설계가 더 일반적인 기계 설계로 확장됩니다.
- 🔄 다른 접근: [[papers/084_Ai-driven_robotics_for_free-space_optics/review]] — 자동차 설계와 광학 실험 모두 물리적 시스템의 AI 기반 설계 자동화를 다룹니다.
- 🔄 다른 접근: [[papers/849_UI-TARS_Pioneering_Automated_GUI_Interaction_with_Native_Age/review]] — GUI 자동화와 엔지니어링 설계 자동화 모두 인간-AI 협업을 다룹니다.
