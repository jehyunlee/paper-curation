---
title: "290_DrugAgent_Automating_AI-aided_Drug_Discovery_Programming_thr"
authors:
  - "Sizhe Liu"
  - "Yizhou Lu"
  - "Siyu Chen"
  - "Xiyang Hu"
  - "Jieyu Zhao"
date: "2024"
doi: "10.48550/arXiv.2411.15692"
arxiv: ""
score: 4.25
essence: "LLM 기반 다중 에이전트 프레임워크 DrugAgent는 신약 발견 분야의 전문적 지식을 통합하여 일반 목적 AI 에이전트의 한계를 극복하고, DTI(약물-표적 상호작용) 예측에서 ReAct 대비 4.92% 향상된 성능을 달성했다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/LLM_Drug_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liu et al._2024_DrugAgent Automating AI-aided Drug Discovery Programming through LLM Multi-Agent Collaboration.pdf"
---

# DrugAgent: Automating AI-aided Drug Discovery Programming through LLM Multi-Agent Collaboration

> **저자**: Sizhe Liu, Yizhou Lu, Siyu Chen, Xiyang Hu, Jieyu Zhao | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2411.15692](https://doi.org/10.48550/arXiv.2411.15692)

---

## Essence

![Figure 1](figures/fig1.webp)
*DrugAgent 프레임워크 개요: LLM Planner와 LLM Instructor의 협력을 통해 자연언어로 표현된 신약 발견 과제를 자동으로 ML 프로그래밍으로 변환*

LLM 기반 다중 에이전트 프레임워크 DrugAgent는 신약 발견 분야의 전문적 지식을 통합하여 일반 목적 AI 에이전트의 한계를 극복하고, DTI(약물-표적 상호작용) 예측에서 ReAct 대비 4.92% 향상된 성능을 달성했다.

## Motivation

- **Known**: LLM의 자동 추론과 코딩 지원 능력이 여러 분야에서 입증되었으며, 신약 발견을 위한 AI 준비 데이터셋(ADMET, DTI, HTS)과 딥러닝 기법이 널리 가용화되어 있다.

- **Gap**: 신약 발견은 생물학, 화학, 제약 과학, 컴퓨터 과학이 교집합하는 극도로 전문화된 분야로서, 일반 목적 ML 에이전트(MLAgentBench, AI-Scientist)는 신약 발견의 특수성을 반영하지 못한다. SMILES 문자열 처리, 생물학적 데이터 타입 해석 같은 작은 실수도 디버깅이 어렵다.

- **Why**: ChemCrow, MultiToolCoT 같은 화학 도구 기반 프레임워크는 데이터 전처리부터 모델 평가까지 확장된 ML 작업을 충분히 지원하지 못한다.

- **Approach**: 신약 발견 분야의 도메인 지식을 체계적으로 검증하고, 아이디어 공간(idea space) 수준의 동적 계획과 전문화된 도메인 문서화를 통합한 다중 에이전트 프레임워크를 제안한다.

## Achievement

![Figure 2](figures/fig2.webp)
*DAVIS(DTI) 데이터셋에서 오류 모드 분석: ReAct와 ResearchAgent는 도메인 지식이 필요한 단계에서 오류 발생 비율이 높지만, DrugAgent는 해당 카테고리에서 오류가 없음*

1. **성능 우위**: DrugAgent@Top3는 ADMET에서 0.8206, HTS에서 0.8257, DTI에서 0.8950의 ROC-AUC 달성. ReAct 대비 DTI 과제에서 4.92% 상대 개선율, 전 과제에서 100% 유효 제출률 달성(ReAct는 50-87.5%).

2. **도메인 지식 통합의 효과**: 오류 추적 분석 결과 DrugAgent는 도메인 지식이 필요한 단계에서의 오류 비율이 0%로, 일반 에이전트 대비 현저히 낮은 오류율(ReAct, ResearchAgent는 30-40% 오류) 달성.

3. **전문가 수준 성능**: 인간 전문가 기준(Human Baseline)과 비교하여 competitive한 성능 달성 (DTI에서 동일 성능 0.8950).

## How

![Figure 1](figures/fig1.webp) 참조

- **LLM Planner (아이디어 공간 관리)**:
  - Phase 1: 과제 설명으로부터 K개의 가능한 해결책 아이디어 도출
  - Phase 2: 아이디어 선택 → Instructor에 전송 → 실험적 평가 → 성공/실패 피드백 기반 아이디어 집합 수정 (부실적 또는 불가능한 아이디어 폐기)
  - 반복 수행 후 최고 성능 아이디어 제출

- **LLM Instructor (도메인 특화 코드 생성)**:
  - 표준 ML 작업 실행 (파일 읽기/편집, 코드 실행)
  - 3가지 큐레이션된 문서 참조: ①Raw Data Acquisition (생물학적 데이터 검색/전처리), ②Featurizing Biological Data (분자/단백질 인코딩: fingerprints, graph 표현), ③Domain-Specific Models (ChemBERTa, ESM 같은 사전학습 모델)
  - 코딩 각 단계에서 도메인 지식 명시적 통합, 실패 시 명확한 실패 리포트 반환

- **동적 아이디어 정제**: 초기 다양한 옵션 생성 후 실험 결과 기반 점진적 정제로 hallucination 위험 완화

## Originality

- **도메인 특화 ML 에이전트 설계**: 일반 목적 ML 에이전트(ResearchAgent)와 화학 도구 기반 프레임워크(ChemCrow) 간 격차를 메우고, 신약 발견의 전체 ML 파이프라인(데이터 전처리→모델링→평가)을 지원하는 최초 프레임워크.

- **아이디어 공간 수준의 계획**: 단순 추론-행동(ReAct) 수준을 넘어 고수준 아이디어의 생성·검증·정제 프로세스를 명시적으로 설계.

- **체계적 도메인 지식 통합**: 도메인 지식 필요 지점을 사전에 식별하고 구조화된 문서(Raw Data, Featurization, Model)로 대응하는 체계적 접근.

- **종합 비교 연구**: 세 가지 representative 신약 발견 과제(ADMET, HTS, DTI)에서 multiple baselines(CoT, ReAct, ResearchAgent) 대비 평가 및 오류 모드 상세 분석 제공.

## Limitation & Further Study

- **평가 범위 제한**: 3개 과제, 1개 LLM 기반(GPT-4o)만 평가. 다양한 신약 발견 과제, 개방형 문제(de novo 약물 설계) 확대 필요.

- **검증-테스트 불일치**: DrugAgent@Top3 > DrugAgent@Top1 성능 격차 시사, 검증 성능이 테스트 성능을 항상 예측하지 못함. 더 정교한 모델 선택 메커니즘 필요.

- **도메인 문서 확장성**: 현재 3가지 문서 카테고리의 포괄성, 새로운 신약 발견 과제 영역(단백질 구조 예측, 임상 설계)으로의 확대 방안 미제시.

- **계산 비용 미분석**: 다중 라운드 아이디어 생성 및 평가로 인한 LLM API 호출 비용 미분석. 실무 적용성을 위한 효율성 분석 필요.

- **인간 전문가와 협력**: 에이전트 결과의 전문가 검증 메커니즘, 약물 개발 실무진과의 통합 방안 제시 부족.


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.25/5

**총평**: DrugAgent는 신약 발견 분야의 도메인 지식을 LLM 에이전트에 체계적으로 통합하는 실질적 접근을 제시하며, 일반 목적 에이전트 대비 유의미한 성능 개선과 신뢰성(유효 제출률, 오류율)을 입증했다. 다만 평가 범위 확대, 계산 비용 분석, 실제 신약 개발 환경과의 검증이 추가되면 임상 적용성이 강화될 것으로 기대된다.

## Related Papers

- 🔗 후속 연구: [[papers/212_Chemist-X_Large_Language_Model-empowered_Agent_for_Reaction/review]] — AI 기반 약물 발견 프로그래밍을 화학 합성 자동화로 확장하는 연구 방향을 제시한다
- 🏛 기반 연구: [[papers/490_LIDDIA_Language-based_Intelligent_Drug_Discovery_Agent/review]] — DrugAgent의 AI 기반 프로그래밍 자동화 접근법이 LIDDIA의 계산 도구 통합 방법론의 기반이 됨
- 🔗 후속 연구: [[papers/651_RAG-Enhanced_Collaborative_LLM_Agents_for_Drug_Discovery/review]] — AI 기반 약물 발견 프로그래밍 자동화 연구를 RAG 증강 협력 프레임워크로 확장할 수 있다.
- 🔗 후속 연구: [[papers/616_PharmAgents_Building_a_Virtual_Pharma_with_Large_Language_Mo/review]] — AI 기반 약물 발견 프로그래밍 자동화로 약물 개발 자동화를 확장한다.
