---
title: "413_Human-ai_teaming_using_large_language_models_Boosting_brain-"
authors:
  - "Maryna Kapitonova"
  - "Tonio Ball"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.1
essence: "본 논문은 대규모 언어 모델(LLM)을 기반으로 한 인간-AI 협력 프레임워크를 제시하며, 이를 뇌-컴퓨터 인터페이스(BCI) 및 뇌 신호 분석 연구에 적용하는 ChatBCI 도구를 소개한다. 완전 자동화된 \"AI 연구자\"보다는 인간 전문가의 암묵적 지식을 활용하는 협력적 접근을 강조한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Multimodal_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Brown_2024_Human-ai teaming using large language models Boosting brain-computer interfacing (bci) and brain re.pdf"
---

# Human-ai teaming using large language models: Boosting brain-computer interfacing (bci) and brain research

> **저자**: Maryna Kapitonova, Tonio Ball | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 2](figures/fig2.webp) *Janusian Vision: 인간 전문성과 AI 능력을 모두 향하는 이중 설계 접근*

본 논문은 대규모 언어 모델(LLM)을 기반으로 한 인간-AI 협력 프레임워크를 제시하며, 이를 뇌-컴퓨터 인터페이스(BCI) 및 뇌 신호 분석 연구에 적용하는 ChatBCI 도구를 소개한다. 완전 자동화된 "AI 연구자"보다는 인간 전문가의 암묵적 지식을 활용하는 협력적 접근을 강조한다.

## Motivation

- **Known**: 
  - AI 과학자 시스템(AI Scientist Systems, AISS)이 분자생물학, 컴퓨터과학 등에서 자동화된 연구 수행 가능성 입증
  - LLM 기반 AI가 가설 수립, 실험 설계, 논문 작성까지 자동 수행 가능

- **Gap**: 
  - 뇌 신호 연구는 작고 다양한 데이터셋, 낮은 데이터 품질, 다중 스케일 뇌 역학의 복잡성으로 인해 일반 AI 과학자 시스템을 직접 적용하기 어려움
  - 과학 출판물 폭증(2016-2022년 47% 증가)과 불충분한 편집 감시로 인한 훈련 데이터 품질 저하
  - 뇌 연구에 내재된 암묵적, 맥락 의존적 전문 지식을 AI 시스템에 통합하는 방법 부재

- **Why**: 
  - EEG 기반 BCI 연구는 공개 벤치마크 부족, 데이터 접근성 제한 등 도메인 특화 문제 존재
  - 인간 전문가의 직관과 암묵적 지식이 연구 효율성과 질을 좌우

- **Approach**: 
  - Janusian Design Principles에 기반한 인간-AI 협력 워크스페이스 제안
  - ChatBCI Python 도구상자로 LLM과의 구조화된 상호작용 지원
  - 구체적 EEG 운동 상상(motor imagery) 디코딩 프로젝트를 통해 검증

## Achievement

![Figure 1](figures/fig1.webp) *AI 기반 BCI 연구 프로세스: 자동화 수준을 색상으로 표현한 유연한 공유 자율성 모델*

1. **ChatBCI 도구 개발**: 
   - EEG 전처리, 분석, 디코딩 모델, 학습, 해석 가능성, 시각화 통합
   - 공개 EEG 데이터셋 컬렉션 및 검증된 BCI 지식 베이스 포함
   - PyTorch 및 GPT-4o 기반 구현

2. **협력 효율성 달성**:
   - 데이터 임포트부터 결과 해석까지 전체 BCI 연구 사이클을 시간 효율적으로 완료
   - 심층 합성곱 신경망(deep CNN) 기반 뇌 신호 디코더 자동 생성
   - 데이터 증강이 통합된 훈련 루프 자동 구성

3. **인간-AI 상호학습(co-learning)**:
   - 인간 전문가의 비자명한(non-obvious) EEG 데이터셋 특성이 AI 에이전트로 전이
   - ChatBCI가 인간 측에 대한 가치있는 학습 파트너 역할 수행
   - 순수 인간 접근보다 현저히 빠른 협력적 완료

## How

![Figure 3](figures/fig3.webp) *모든 피험자의 훈련 데이터에 걸친 ERP 파형: 화살표 신호 발생부터 반응까지의 시간축*

### 방법론

- **Janusian Design Principles (7가지 원칙)**:
  1. **공통 언어**: 직관적 인터페이스와 맥락 피드백으로 자연스러운 협력 언어 개발
  2. **투명성과 신뢰**: 양방향 투명성 강조, 설명 가능한 AI(XAI) 및 AI의 명확화 질의 메커니즘 포함
  3. **공유 지식 베이스**: Janusian Wiki (Jiki)로 워크플로우, 모범 사례, 도메인 지식 중앙화
  4. **우선순위 공동 통합**: 즉각적 행동 vs 장기 목표, 하향식(top-down) vs 상향식(bottom-up) 우선순위 조화
  5. **적응적 자율성(Adaptive Autonomy)**: 협력적 테스트 주도 개발(TDD)로 일상적 작업은 자동화, 중요 결정은 인간 감독
  6. **초보자부터 전문가까지 접근성**: 교육 사용과 전문가 기능의 이중 최적화
  7. **지속적 피드백 루프**: 반복적 개선과 학습 메커니즘 내장

- **구현 구조**:
  - Python 기반 모듈식 아키텍처
  - EEG 전처리 파이프라인(고역통과 필터 4Hz 등)
  - 운동 상상 분류(방향별 화살표 신호)
  - LLM 통신 도구로 자동 코드 생성 및 검증

- **협력 방식**:
  - 인간이 고수준 연구 목표 및 데이터 특성 정의
  - AI가 코드 생성, 모델 아키텍처 제안, 결과 해석 지원
  - 반복적 피드백 루프로 모델 개선

## Originality

- **새로운 설계 철학**: Janusian Design Principles는 완전 자동화가 아닌 **상호 학습 중심의 협력 모델**로 과학 AI의 새로운 패러다임 제시
  
- **도메인 특화 AI**: 일반 LLM을 BCI 연구의 특수성(소규모 다양한 데이터셋, 복잡한 뇌 역학)에 맞춘 최초의 체계적 적응

- **AutoML의 신로운 범주**: LLM이 생성한 뇌 신호 디코더는 신경신호 분석용 자동 기계학습의 새로운 클래스

- **암묵적 지식 전이 메커니즘**: 구조화된 상호작용으로 인간의 비자명한 도메인 지식을 AI 시스템으로 전이하는 실제 사례 제시

- **교육 및 훈련 도구로의 적용**: 초보자부터 전문가까지 모두 활용 가능한 유연한 설계

## Limitation & Further Study

- **암묵적 지식 표현의 한계**: 
  - Jiki (지식 베이스)가 어떤 수준의 세밀도(granularity)로 암묵적 지식을 포착하는지 명확하지 않음
  - 복잡한 뇌 역학 지식의 완전한 전이 가능성 검증 필요

- **확장성 및 일반화 미검증**:
  - 단일 프로젝트(운동 상상 EEG)에서만 검증되어 다른 BCI 패러다임이나 뇌 신호(fMRI, LFP 등)로의 전이 가능성 미확인
  - 대규모 다중 기관 연구로의 확장 가능성 불명확

- **품질 관리 및 검증**:
  - LLM 생성 코드의 자동 검증 메커니즘 부족
  - 생성된 모델의 해석 가능성 및 신뢰성에 대한 엄격한 평가 기준 부재

- **인간-AI 상호작용의 정량화**:
  - 협력의 시간 효율성은 보고되나, 학습 곡선, 오류율, 반복 필요도 등의 정량적 메트릭 부족
  - 인간 전문가 역할의 명확한 정의 및 최적 배치 전략 미개발

- **후속 연구 방향**:
  - 다양한 BCI 패러다임(P300, SSVEP, 운동 피질 임플란트) 적용 확대
  - "뇌-이해 AI" (brain-grokking AI) 달성을 위한 장기 연구 로드맵 수립
  - 다중 신경신호 모달리티 통합 연구
  - 임상 환경에서의 실시간 BCI 응용

## Evaluation

- **Novelty**: 4.5/5
  - Janusian Design Principles는 과학 AI 설계의 새로운 철학을 제시하나, 원칙 자체의 수학적 엄밀성 부족
  - ChatBCI 도구는 신기술적이나 기존 LLM과 EEG 처리의 조합

- **Technical Soundness**: 4/5
  - EEG 전처리 및 CNN 아키텍처는 표준적이고 적절함
  - 그러나 생성된 모델의 신경과학적 타당성, 해석 가능성에 대한 검증 부족
  - 단일 공개 데이터셋에서만 검증되어 일반화 가능성 미증명

- **Significance**: 4/5
  - BCI 및 신경과학 연구의 효율성 향상 가능성 높음
  - 암묵적 지식 전이 메커니즘은 과학 전반에 적용 가능한 중요 개념
  - 그러나 실제 임상 또는 대규모 연구에서의 영향 미증명

- **Clarity**: 4/5
  - Janusian Design Principles는 명확하고 잘 구조화됨
  - ChatBCI 구현 세부사항이 다소 부족하며, 코드 공개 대기 중
  - 그림과 설명이 일반적이어서 구체적 기술 세부사항 파악 어려움

- **Overall**: 4.1/5

**총평**: 본 논문은 대규모 언어 모델과 인간 전문가의 협력 패러다임을 BCI 연구에 창의적으로 도입하며, 암묵적 도메인 지식 전이의 실제 메커니즘을 제시하는 점에서 큰 가치를 지닌다. 다만 단일 프로젝트 검증, 생성 모델의 신경과학적 타당성 검증 부족, 그리고 대규모 적용 가능성 미증명 등이 아쉬운 한계이며, 향후 다양한 BCI 패러다임과 신경신호에 대한 광범위한 검증이 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/529_MedAgents_Large_Language_Models_as_Collaborators_for_Zero-sh/review]] — MedAgents의 제로샷 의료 협력이 ChatBCI의 뇌-컴퓨터 인터페이스 연구에서 인간-AI 협력 방식을 확장함
- 🧪 응용 사례: [[papers/606_Patientsim_A_persona-driven_simulator_for_realistic_doctor-p/review]] — PatientSim의 환자 시뮬레이션이 ChatBCI의 뇌 신호 분석 연구에서 실제 임상 시나리오 검증에 활용됨
- 🏛 기반 연구: [[papers/412_HuggingGPT_Solving_AI_Tasks_with_ChatGPT_and_its_Friends_in/review]] — HiAgent의 계층적 작업 메모리 관리가 ChatBCI의 복잡한 뇌 신호 분석 과정에서 정보 처리 효율성을 높임
- 🔗 후속 연구: [[papers/233_Cognitio_emergens_Agency_dimensions_and_dynamics_in_human-ai/review]] — 뇌-컴퓨터 인터페이스 분야에서 인간-AI 팀워크의 실제 구현 방법을 제시한다.
