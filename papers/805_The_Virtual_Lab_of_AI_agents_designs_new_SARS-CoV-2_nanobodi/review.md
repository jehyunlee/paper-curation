---
title: "805_The_Virtual_Lab_of_AI_agents_designs_new_SARS-CoV-2_nanobodi"
authors:
  - "Kyle Swanson"
  - "Wesley Wu"
  - "Nash L. Bulaong"
  - "John E. Pak"
  - "James Zou"
date: "2025.07"
doi: "10.1038/s41586-025-09442-9"
arxiv: ""
score: 4.2
essence: "LLM 기반의 다중 AI 에이전트 시스템(Virtual Lab)이 학제 간 협업을 통해 SARS-CoV-2 신규 나노바디(nanobody) 92개를 설계하고 실험적으로 검증하여, 최근 변이주(JN.1, KP.3)에 대한 개선된 결합 특성을 가진 유망 후보들을 발견했다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/LLM_Drug_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Swanson et al._2025_The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies 1.pdf"
---

# The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies

> **저자**: Kyle Swanson, Wesley Wu, Nash L. Bulaong, John E. Pak, James Zou | **날짜**: 2025-07-29 | **DOI**: [10.1038/s41586-025-09442-9](https://doi.org/10.1038/s41586-025-09442-9)

---

## Essence

LLM 기반의 다중 AI 에이전트 시스템(Virtual Lab)이 학제 간 협업을 통해 SARS-CoV-2 신규 나노바디(nanobody) 92개를 설계하고 실험적으로 검증하여, 최근 변이주(JN.1, KP.3)에 대한 개선된 결합 특성을 가진 유망 후보들을 발견했다.

## Motivation

- **Known**: 대규모 언어 모델(LLM)이 특정 과학 질문 답변에 탁월하며, 여러 연구 프레임워크(ChemCrow, Coscientist, AI Scientist)가 제한된 범위의 과학 문제 해결을 시도했음
- **Gap**: 기존 LLM 기반 접근법들은 (1) 단일 학문 분야에 국한되거나, (2) 실제 실험 검증이 없거나, (3) 좁은 범위의 연구 문제만 다룸. 개방형 학제 간 연구 문제를 수행하는 LLM의 능력이 검증되지 않음
- **Why**: 자원이 제한된 연구 그룹이 여러 분야의 전문가에 접근하기 어렵고, 복잡한 생물의학 연구(예: SARS-CoV-2 변이주 대응)는 신속한 솔루션이 필요함
- **Approach**: 인간 연구자의 고수준 지도 하에 LLM 기반 PI(Principal Investigator) 에이전트가 여러 과학자 에이전트(면역학자, 계산생물학자, ML 전문가)를 조율하는 "Virtual Lab" 아키텍처 도입

## Achievement

1. **Virtual Lab 아키텍처 개발**: 팀 회의(team meetings)와 개별 회의(individual meetings)를 통해 LLM 에이전트들이 협업하는 확장 가능한 시스템 구축
   - PI 에이전트가 자동으로 필요한 과학자 에이전트 생성
   - Scientific Critic 에이전트가 각 단계에서 비판적 피드백 제공
   - 5단계 프로세스(팀 선택 → 프로젝트 명세 → 도구 선택 → 도구 구현 → 워크플로우 설계)를 자동 진행

2. **나노바디 설계 성과**: 
   - ESM(단백질 언어 모델), AlphaFold-Multimer(단백질 구조 예측), Rosetta(계산 생물학 소프트웨어)를 통합한 신규 계산 나노바디 설계 파이프라인 구축
   - 4개의 기존 나노바디(Ty1, H11-D4, Nb21, VHH-72)로부터 92개의 변이 나노바디 설계
   - 90% 이상의 높은 발현 및 용해도 달성
   - **2개의 유망 후보 발굴**: JN.1 또는 KP.3 변이주에 대해 개선된 결합력 보이면서 조상형(Wuhan) 스파이크 단백질에 대한 강한 결합력 유지

## How

- **Virtual Lab 구조**: 
  - 각 에이전트는 프롬프트를 통해 정의(Title, Expertise, Goal, Role)
  - PI 에이전트가 팀 회의를 주도하고 과학자 에이전트들의 응답을 종합
  - 각 라운드마다 Scientific Critic이 응답을 비판하고, 에이전트는 피드백을 기반으로 개선

- **나노바디 설계 워크플로우**:
  - ESM: 단일 점 돌연변이의 로그우도비(LLR) 계산 → 상위 20개 변이체 선정
  - AlphaFold-Multimer: 나노바디-RBD 복합체 구조 예측 → 결합 인터페이스 신뢰도(AF ipLDDT) 평가
  - Rosetta: 구조 안정성 및 바인딩 에너지 재점수(rescoring) → 최적화된 변이체 선정
  - 반복적 최적화: 각 라운드에서 상위 후보를 기반으로 다음 세대 변이체 생성

- **실험 검증**: 설계된 92개 나노바디에 대해 발현 테스트, 용해도 평가, 바인딩 프로필 분석

## Originality

- **AI-인간 협업의 새로운 패러다임**: 단순 질문 응답을 넘어 개방형 연구 문제의 설계부터 실행까지 LLM이 주도적 역할 수행
- **학제 간 에이전트 자동 생성**: 인간의 프로젝트 설명만으로 필요한 전문가 에이전트를 LLM이 자동 생성하는 혁신적 접근
- **실제 실험 검증을 동반한 첫 사례**: 이전 LLM 기반 연구 프레임워크와 달리, 설계된 나노바디가 생화학적으로 검증되고 실제 바이러스 변이주에 대한 효과 입증
- **통합 계산 파이프라인**: ESM, AlphaFold-Multimer, Rosetta를 순차적으로 조합한 나노바디 설계 전략이 LLM에 의해 자동으로 제안되고 구현됨

## Limitation & Further Study

- **제한사항**:
  - 현재는 4개의 기존 나노바디를 모판으로 시작 → 완전히 신규 나노바디 설계로의 확장 필요
  - GPT-4o에만 의존 → 다른 LLM 모델에서의 성능, 비용 효율성 미검증
  - 나노바디 92개 중 2개만이 최종적으로 유망 후보 → 설계 정확도 개선 필요
  - 계산 도구(ESM, AlphaFold-Multimer, Rosetta)의 예측 정확도가 전체 성공률을 제한
  - 실시간 반복 피드백 시 인간 연구자의 개입 정도와 최적 가이드라인 미명확

- **후속 연구**:
  - Virtual Lab을 암 면역치료, 신약 개발 등 다른 의약 분야로 확장
  - 설계 효율성 향상: 머신러닝 기반 스크리닝으로 유망 후보 사전 필터링
  - 대규모 병렬 실험 통합: 고처리량 스크리닝과 Virtual Lab의 피드백 루프 자동화
  - 오픈소스 LLM 활용으로 접근성 및 재현성 강화
  - 다중 모달(multimodal) 에이전트 개발: 실험 데이터 직접 입력 → 설계 개선

## Evaluation

- **Novelty**: 4.5/5
  - LLM 기반 AI-인간 협업 프레임워크는 창신적이나, 개별 도구(ESM, AlphaFold-Multimer, Rosetta)는 기존 기술

- **Technical Soundness**: 4/5
  - 3단계 계산 파이프라인이 합리적이고 검증됨
  - 단, 각 도구의 예측 신뢰도 상호작용 및 오류 누적에 대한 깊이 있는 분석 부족

- **Significance**: 4.5/5
  - SARS-CoV-2 변이주 대응이라는 중요한 실제 문제 해결
  - 학제 간 연구의 자동화 가능성 제시
  - 다만 임상 적용까지는 추가 단계 필요

- **Clarity**: 4/5
  - Virtual Lab 아키텍처와 워크플로우가 명확히 설명됨
  - 에이전트별 역할 정의가 체계적
  - 일부 기술 세부사항(LLR 계산, AF ipLDDT 기준) 추가 설명 가능

- **Overall**: 4.2/5

**총평**: 이 연구는 LLM이 단순한 조언자에서 과학 연구의 설계 및 실행을 주도하는 지능형 협력자로 진화했음을 보여주는 이정표적 논문이다. Virtual Lab이라는 새로운 패러다임과 SARS-CoV-2 나노바디라는 구체적 성과를 통해 AI-인간 협업의 가능성을 실증했으나, 설계 효율성 개선과 다양한 과학 분야으로의 일반화가 앞으로의 과제이다.

## Related Papers

- 🔄 다른 접근: [[papers/144_AutoProteinEngine_A_Large_Language_Model_Driven_Agent_Framew/review]] — Virtual Lab의 특정 나노바디 설계와 AutoProteinEngine의 일반적 단백질 공학 자동화는 서로 다른 범위에서 단백질 설계를 다루는 접근이다.
- 🏛 기반 연구: [[papers/381_Genesis_Towards_the_Automation_of_Systems_Biology_Research/review]] — Genesis의 대규모 병렬 실험 자동화 방법론이 Virtual Lab의 학제간 AI 에이전트 협업을 통한 단백질 설계의 기술적 토대이다.
- 🔗 후속 연구: [[papers/112_Atomically_accurate_de_novo_design_of_antibodies_with_RFdiff/review]] — RFdiffusion을 사용한 원자적으로 정확한 항체 설계가 Virtual Lab의 나노바디 설계 방법론을 더 정밀한 구조적 정확도로 확장한 발전된 접근이다.
- 🏛 기반 연구: [[papers/806_The_Virtual_Lab_AI_Agents_Design_New_SARS-CoV-2_Nanobodies_w/review]] — 동일한 연구의 초기 버전으로서 가상 실험실 프레임워크의 개념적 기반을 제공한다.
- 🔄 다른 접근: [[papers/144_AutoProteinEngine_A_Large_Language_Model_Driven_Agent_Framew/review]] — AutoProteinEngine의 일반적 단백질 공학 자동화와 Virtual Lab의 특정 나노바디 설계는 서로 다른 범위에서 단백질 설계를 자동화하는 접근이다.
- 🔄 다른 접근: [[papers/381_Genesis_Towards_the_Automation_of_Systems_Biology_Research/review]] — Genesis의 시스템 생물학 대규모 자동화와 Virtual Lab의 특정 단백질 설계 자동화는 서로 다른 규모에서 생물학적 발견을 자동화하는 접근이다.
- 🔗 후속 연구: [[papers/514_MAC-AMP_A_Closed-Loop_Multi-Agent_Collaboration_System_for_M/review]] — Virtual Lab의 나노바디 설계 성공이 MAC-AMP의 항균펩타이드 설계를 위한 다중 에이전트 협업 방법론의 효과를 다른 단백질 영역에서 확장 검증한다.
- 🔗 후속 연구: [[papers/554_Modular_large_language_model_agents_for_multi-task_computati/review]] — Virtual Lab의 실제 나노바디 설계 성공이 PharmAgents의 가상 제약회사 개념을 특정 단백질 영역에서 실증한 구체적 확장 사례이다.
- 🔄 다른 접근: [[papers/868_Virtual_lab_powered_by_AI_scientists_super-charges_biomedica/review]] — SARS-CoV-2 나노바디 설계라는 동일한 연구 성과를 서로 다른 관점에서 보도하여 AI 과학자 시스템의 성능을 종합적으로 평가할 수 있다.
