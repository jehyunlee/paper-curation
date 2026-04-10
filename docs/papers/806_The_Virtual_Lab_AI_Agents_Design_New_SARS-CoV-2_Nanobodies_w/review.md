---
title: "806_The_Virtual_Lab_AI_Agents_Design_New_SARS-CoV-2_Nanobodies_w"
authors:
  - "Kyle Swanson"
  - "Wesley Wu"
  - "Nash L. Bulaong"
  - "J. Pak"
  - "James Y. Zou"
date: "2024"
doi: "10.1101/2024.11.11.623004"
arxiv: ""
score: 4.4
essence: "본 연구는 대규모 언어모델(LLM) 기반의 다중 전문가 AI 에이전트 팀이 인간 연구자와 협력하여 학제간 과학 연구를 수행하는 \"Virtual Lab\" 프레임워크를 제시한다. 이를 SARS-CoV-2 나노바디 설계에 적용하여 92개의 신규 나노바디를 설계하고 실험적 검증을 통해 유망한 결합 특성을 가진 후보를 발굴했다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/LLM_Drug_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Swanson et al._2024_The Virtual Lab AI Agents Design New SARS-CoV-2 Nanobodies with Experimental Validation.pdf"
---

# The Virtual Lab: AI Agents Design New SARS-CoV-2 Nanobodies with Experimental Validation

> **저자**: Kyle Swanson, Wesley Wu, Nash L. Bulaong, J. Pak, James Y. Zou | **날짜**: 2024 | **DOI**: [10.1101/2024.11.11.623004](https://doi.org/10.1101/2024.11.11.623004)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: Virtual Lab 아키텍처. (a) PI 에이전트를 중심으로 다양한 과학자 에이전트들이 팀을 이루는 구조, (b) 팀 미팅의 다중 라운드 토론 흐름, (c) 개별 미팅의 반복적 피드백 과정*

본 연구는 대규모 언어모델(LLM) 기반의 다중 전문가 AI 에이전트 팀이 인간 연구자와 협력하여 학제간 과학 연구를 수행하는 "Virtual Lab" 프레임워크를 제시한다. 이를 SARS-CoV-2 나노바디 설계에 적용하여 92개의 신규 나노바디를 설계하고 실험적 검증을 통해 유망한 결합 특성을 가진 후보를 발굴했다.

## Motivation

- **Known**: LLM이 개별 과학 질문에 답변하는 데 뛰어나며, ChemCrow, Coscientist 등의 단일 도메인 AI 연구 프레임워크들이 존재함.

- **Gap**: 기존 LLM 기반 연구 도구들은 ① 단일 과학 분야에 제한되거나, ② 표준화된 작업(화학 합성 계획)에만 적용되거나, ③ 실제 실험 검증이 없는 한계를 보임.

- **Why**: 학제간 과학은 복잡한 다단계 추론, 서로 다른 언어와 우선순위를 가진 여러 분야의 조정이 필수적이며, 자원이 부족한 연구 그룹들은 이러한 전문성에 접근하기 어려움.

- **Approach**: 인간 연구자의 고수준 지시 하에 PI 에이전트(AI 리더)가 분야별 전문 에이전트들(생물학자, 컴퓨터과학자, 비평가)을 동적으로 생성하고 팀 미팅과 개별 미팅을 통해 협력하는 구조로 구현.

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: 나노바디 설계를 위한 Virtual Lab의 적용 워크플로우*

1. **novel nanobody design pipeline 개발**: ESM(단백질 언어 모델), AlphaFold-Multimer(단백질 폴딩), Rosetta(계산 생물학 소프트웨어)를 통합한 새로운 계산 파이프라인을 자동으로 설계. SARS-CoV-2 원래 균주의 RBD(수용체 결합 영역)에 결합하는 기존 나노바디를 최신 변이주에 맞도록 돌연변이 유도.

2. **높은 설계 성공률**: 92개의 설계된 나노바디 중 90% 이상이 발현되고 가용성을 보임. 특히 JN.1 또는 KP.3 변이주에 향상된 결합력을 보이면서도 원조 바이러스 스파이크 단백질에 강한 결합력을 유지하는 2개의 유망 후보 발굴.

3. **실제 과학 발견의 증명**: 순수 계산만이 아닌 실험적 검증을 통해 AI-인간 협력의 실제 영향력을 입증한 첫 사례 중 하나.

## How

![Figure 3](figures/fig3.webp)
*그림 3: Nb21 나노바디 분석. 매 라운드의 설계 반복 과정과 계산 모델들의 예측 신뢰성 검증*

- **에이전트 설정**: 각 에이전트는 4가지 기준(제목, 전문성, 목표, 역할)으로 정의되며, PI 에이전트가 자동으로 프로젝트에 필요한 scientist agents 생성
  
- **팀 미팅 구조**: (1) PI가 아젠다와 질문 제시 → (2) N라운드의 순차적 토론(각 scientist agent 의견 → critic 피드백) → (3) PI의 종합 요약 및 의사결정

- **개별 미팅 구조**: 특정 과제(예: 코드 작성)에 대해 단일 에이전트가 작업하고 critic의 반복적 피드백으로 개선

- **아젠다 기반 제어**: 인간 연구자가 아젠다, 질문, 규칙, 참고 자료(논문 등), 라운드 수를 지정하여 토론 방향 제어

- **도구 통합**: 각 에이전트가 ESM, AlphaFold-Multimer, Rosetta, 분자 동역학 시뮬레이션 등의 과학 도구에 접근 가능

## Originality

- **다중 전문가 협력 시뮬레이션**: LLM 에이전트들이 서로 다른 과학 배경을 가지고 대면(adversarial) 토론 형태로 상호 검증하는 구조로, 기존 단순 도구 통합과 차별화

- **동적 에이전트 생성**: PI 에이전트가 프로젝트 설명만으로 필요한 전문가 팀을 자동 구성하는 메타-레벨의 AI 자율성

- **비평가(Critic) 에이전트의 명시적 포함**: 검증과 오류 포착을 전담하는 독립 에이전트 도입으로 품질 관리 강화

- **학제간 open-ended 문제의 실제 해결**: 나노바디 설계는 생물학, 컴퓨터 과학, 구조 생물학을 아우르는 진정한 복합 문제이며, 실험 검증까지 완료한 점이 선행 연구(AI Scientist, Si et al.)와 차별됨

## Limitation & Further Study

- **LLM 능력의 상한선**: 최신 GPT-4o 기반이나, 과학 추론의 한계(환각, 오래된 정보)는 여전히 존재. 더 강력한 모델이나 fine-tuning으로 개선 필요

- **에이전트 수 및 역할의 최적화**: 현재는 경험적으로 에이전트 팀을 구성했는데, 어떤 조합이 최적인지에 대한 체계적 연구 부재

- **계산 비용 및 확장성**: 다중 LLM 호출로 인한 API 비용과 시간 소요가 크며, 더 큰 규모 프로젝트 적용 시 확장성 미검증

- **나노바디 실험의 제한적 성공률**: 90% 이상의 발현 성공 중 실제 결합 기능을 보인 것은 일부에 불과하며, 설계 품질 개선 필요

- **후속 연구**: (1) 다른 학제간 문제(신약 개발, 재료 과학)로의 확장, (2) 에이전트 팀 구성 최적화 알고리즘 개발, (3) LLM 미세조정을 통한 과학 도메인 특화, (4) 인간-AI 협력의 인지적 상호작용 분석

## Evaluation

- **Novelty**: 4.5/5 — 다중 전문가 에이전트 팀의 협력 구조와 비평가 에이전트는 새로움. 다만 개별 기술(LLM, AlphaFold, Rosetta)은 기존 것의 조합.

- **Technical Soundness**: 4/5 — 아키텍처와 실험 검증이 타당하나, 에이전트 프롬프트 설계의 상세 근거와 프롬프트 민감도 분석 부족. 통계적 엄밀성(n=92의 샘플 크기 타당성) 논의 필요.

- **Significance**: 5/5 — AI-인간 협력의 실제 생물학적 성과(기능성 나노바디 발굴)를 처음으로 입증한 점에서 매우 의미 있음. 자원 부족 연구팀의 가능성 제시.

- **Clarity**: 4/5 — 아키텍처 설명과 그림이 명확하나, 개별 미팅과 팀 미팅의 프롬프트 상세 내용(Appendix 필요)이 본문에 충분하지 않음.

- **Overall**: 4.4/5

**총평**: 본 논문은 LLM 기반 다중 전문가 에이전트가 인간 연구자와 협력하여 실제 학제간 과학 문제(나노바디 설계)를 해결하고 실험적으로 검증한 선도적 사례로, 향후 AI 지원 과학 연구의 패러다임 전환을 시사한다. 다만 대규모 적용 시 비용과 확장성, 그리고 에이전트 팀 최적화 방법론의 추가 개발이 요구된다.

## Related Papers

- 🔄 다른 접근: [[papers/616_PharmAgents_Building_a_Virtual_Pharma_with_Large_Language_Mo/review]] — SARS-CoV-2 나노바디와 가상 제약회사라는 서로 다른 스케일에서 AI 기반 약물 발견의 다중 전문가 접근법을 비교한다.
- 🏛 기반 연구: [[papers/805_The_Virtual_Lab_of_AI_agents_designs_new_SARS-CoV-2_nanobodi/review]] — 동일한 연구의 초기 버전으로서 가상 실험실 프레임워크의 개념적 기반을 제공한다.
- 🔗 후속 연구: [[papers/764_Sparks_Multi-Agent_Artificial_Intelligence_Model_Discovers_P/review]] — 특정 약물 표적 설계에서 검증된 다중 에이전트 접근법을 일반적인 과학 발견으로 확장한다.
