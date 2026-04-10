---
title: "624_Piors_Personalized_intelligent_outpatient_reception_based_on"
authors:
  - "Zhijie Bao"
  - "Qingyun Liu"
  - "Ying Guo"
  - "Zhengqiang Ye"
  - "Jun Shen"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "중국의 과포화 외래 접수 업무를 해결하기 위해 대규모언어모델(LLM) 기반 다중 에이전트 시스템을 제안하고, 실제 임상 시나리오에 맞춘 의료 대화 데이터 생성 프레임워크를 통해 개인화된 고품질 접수 서비스를 제공한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Agent_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liu et al._2024_Piors Personalized intelligent outpatient reception based on large language model with multi-agents.pdf"
---

# PIORS: Personalized intelligent outpatient reception based on large language model with multi-agents medical scenario simulation

> **저자**: Zhijie Bao, Qingyun Liu, Ying Guo, Zhengqiang Ye, Jun Shen, Shirong Xie, Jiajie Peng, Xuanjing Huang, Zhongyu Wei | **날짜**: 2024 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) *PIORS의 전체 프레임워크. 상단은 SFMSS 프레임워크, 하단은 환자, 접수 간호사(PIORS-Nurse), 임상의, 정보 보조원으로 구성된 PIORS의 상세 구조*

중국의 과포화 외래 접수 업무를 해결하기 위해 대규모언어모델(LLM) 기반 다중 에이전트 시스템을 제안하고, 실제 임상 시나리오에 맞춘 의료 대화 데이터 생성 프레임워크를 통해 개인화된 고품질 접수 서비스를 제공한다.

## Motivation

- **Known**: 중국에서 연간 93억 건의 외래 진료가 이루어지며, 접수 간호사는 분당 1건, 시간당 2,149.2단어의 업무량을 처리하고 있음. LLM의 뛰어난 성능과 비용 효율성이 입증되었음.

- **Gap**: 기존 지식 중심의 LLM 훈련 방식과 실제 복잡하고 동적인 임상 환경 간의 괴리. 실제 외래 접수 프로세스의 복잡한 서비스 플로우(department guiding, information gathering 등)를 충분히 반영하지 못함.

- **Why**: 접수 간호사의 과중한 업무 부담으로 인한 서비스 질 저하, 환자 대기 시간 비효율, 의료진의 행정 부담 증가가 발생.

- **Approach**: (1) 병원정보시스템(HIS)과 통합된 LLM 기반 접수 간호사 에이전트 개발, (2) 실제 외래 기록 기반의 서비스 플로우 인식 의료 시나리오 시뮬레이션(SFMSS) 프레임워크를 통한 고품질 훈련 데이터 생성.

## Achievement

![Figure 3](figures/fig3.webp) *PIORS-Nurse와 기준 모델들의 성능 비교*

1. **자동 평가 우수성**: PIORS-Nurse가 GPT-4o를 포함한 모든 기준 모델을 상회하는 부서 지정 정확도 및 정보 수집 능력 입증

2. **사용자 평가 만족도**: 15명의 사용자 평가에서 최고 기준 모델 대비 81% 이상의 동등 또는 우수 비율 달성, 실제 시나리오에서의 우월한 경험 제공

3. **임상 전문가 평가**: 15명의 임상 전문가가 PIORS-Nurse의 질문 능력(inquiry capabilities)과 간결한 응답 능력에서 현저한 우수성 인정

## How

![Figure 2](figures/fig2.webp) *SFMSS의 상세 구조. 좌측은 데이터 소스, 우측은 시뮬레이션 프로세스*

**PIORS 시스템 구조**:
- **상호작용 모듈(Interaction Module)**: 환자와 직접 상호작용, 부서 지정 및 기본 의료 문의 대응
- **쿼리 생성 모듈(Query Generation Module)**: HIS로부터 필요한 정보(병력, 부서 위치, 의료진 일정) 검색 여부 판단 및 쿼리 생성
- **요약 모듈(Summarization Module)**: 대화로부터 증상 및 병력 정보를 반복적으로 추출하여 의료 기록 생성 지시사항 및 임상의용 사전진단 보고서 작성

**HospInfo-Assistant**:
- 자연언어 지시를 구조화된 파라미터로 변환하여 HIS API 호출
- 환자 기록 관리(생성, 검색, 업데이트, 삭제)
- 행정 정보 검색

**SFMSS 데이터 생성 프로세스**:
- 시나리오 준비(Scenario Preparing): 실제 외래 기록을 기반으로 LLM이 시나리오 설정 및 환자 프로필 생성
- 간호사 시뮬레이터(Nurse Agent): 부서 지정, 정보 수집, 행정 상담 등의 역할 수행
- 환자 시뮬레이터(Patient Agent): 다양한 환자 행동 패턴 모의
- 감독 에이전트(Supervisor Agent): 간호사의 행동을 실제 임상 기준에 맞게 정제
- 2,400건의 중국 병원 외래 기록을 기반으로 훈련 데이터 생성

## Originality

- **멀티 에이전트 협업 설계**: 접수 간호사, 정보 보조원, 환자, 감독자의 4개 에이전트가 역할 기반 협업을 통해 현실적인 시뮬레이션 구현

- **서비스 플로우 인식 데이터 생성**: 단순한 의료 지식 기반을 벗어나 실제 임상 프로세스의 순서적 진행(department guidance → information gathering → record documentation)을 명시적으로 모델링

- **실제 임상 환경 통합**: 단순한 챗봇이 아닌 HIS와의 통합으로 실제 병원 워크플로우에 즉시 적용 가능한 시스템 설계

- **도메인별 평가 다층화**: 자동 평가, 사용자 평가, 임상 전문가 평가를 구분하여 실무 적용성 검증

## Limitation & Further Study

- **데이터 제한성**: 2,400건의 중국 병원 외래 기록만 사용하여 다양한 지역, 문화, 의료 시스템에서의 일반화 가능성 미검증

- **언어 범위**: 중국어 중심으로 개발되어 다국어 적용 가능성 부재

- **복잡한 케이스 대응**: 논문에서 다중 질환, 응급 상황, 복잡한 사회적 요인 등 어려운 케이스에 대한 처리 방안이 상세히 제시되지 않음

- **시스템 확장성**: 보고서 해석, 검사 계획 등의 추가 기능은 "향후 가능성"으로만 언급되어 실제 구현 사항 부족

- **후속 연구**: (1) 다국어 및 다양한 의료 시스템 적용, (2) 환자 프라이버시 및 보안 메커니즘 강화, (3) 실제 병원 환경에서의 장기간 운영 평가 및 지속적인 모델 개선 방안 개발 필요

## Evaluation

- **Novelty (독창성)**: 4/5 - 멀티 에이전트 협업 및 서비스 플로우 인식 데이터 생성이 신참이나, 개별 기술의 조합 측면이 있음

- **Technical Soundness (기술적 타당성)**: 4/5 - 시스템 설계 및 평가 방법론이 타당하나, 복잡한 시나리오 처리 능력에 대한 상세 분석 부족

- **Significance (중요성)**: 5/5 - 실제 병원 운영의 심각한 문제(접수 과부하)를 다루고 즉시 적용 가능한 실용적 솔루션 제시

- **Clarity (명확성)**: 4/5 - 전반적으로 명확하나, SFMSS의 감독 에이전트 정제 프로세스에 대한 상세 설명 부족

- **Overall**: 4/5

**총평**: 실제 의료 현장의 구체적인 문제를 해결하기 위해 LLM 기반 멀티 에이전트 시스템과 현실 기반 시뮬레이션 데이터 생성을 효과적으로 결합한 우수한 연구이며, 임상 전문가 검증을 통해 실용성을 입증했으나, 다양한 의료 환경으로의 일반화 가능성 검증이 필요한 상황이다.

## Related Papers

- 🔄 다른 접근: [[papers/608_Peer_Review_as_A_Multi-Turn_and_Long-Context_Dialogue_with_R/review]] — 의료 접수 업무에서 다중 에이전트 시스템과 다중 턴 대화 기반 접근법을 비교할 수 있습니다.
- 🔗 후속 연구: [[papers/606_Patientsim_A_persona-driven_simulator_for_realistic_doctor-p/review]] — 환자 시뮬레이션을 위한 페르소나 기반 시스템이 개인화된 외래 접수 서비스로 확장될 수 있습니다.
- 🏛 기반 연구: [[papers/531_Medsyn_Enhancing_diagnostics_with_human-ai_collaboration/review]] — 진단을 위한 인간-AI 협력 향상이 개인화된 의료 접수 서비스 설계의 방법론적 기반을 제공합니다.
