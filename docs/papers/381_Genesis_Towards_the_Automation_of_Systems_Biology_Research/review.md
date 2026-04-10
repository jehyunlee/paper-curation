---
title: "381_Genesis_Towards_the_Automation_of_Systems_Biology_Research"
authors:
  - "Ievgeniia A. Tiukova"
  - "Daniel Brunnsåker"
  - "Erik Y. Bjurström"
  - "Alexander H. Gower"
  - "Filip Kronström"
date: "2024.08"
doi: "10.48550/arXiv.2408.10689"
arxiv: ""
score: 4.2
essence: "Genesis는 수천 개의 상호작용하는 인과관계 성분을 가진 시스템 생물학 모델을 자동으로 개선하기 위해 설계된 다음 세대 로봇 과학자이며, 하루에 1,000개의 가설 기반 폐쇄 루프 실험 사이클을 병렬로 실행할 수 있다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Autonomous_Laboratory_Biology"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Tiukova et al._2024_Genesis Towards the Automation of Systems Biology Research.pdf"
---

# Genesis: Towards the Automation of Systems Biology Research

> **저자**: Ievgeniia A. Tiukova, Daniel Brunnsåker, Erik Y. Bjurström, Alexander H. Gower, Filip Kronström, Gabriel K. Reder, Ronald S. Reiserer, Konstantin Korovin, Larisa B. Soldatova, John P. Wikswo, Ross D. King | **날짜**: 2024-08-20 | **DOI**: [10.48550/arXiv.2408.10689](https://doi.org/10.48550/arXiv.2408.10689)

---

## Essence

![Fig 1](Genesis_fig1.png)
*그림 1. Genesis 시스템의 전체 아키텍처: 1,000개의 컴퓨터 제어식 μ-바이오리액터, 질량분석기, RNA-SEQ, 온톨로지 기반 지식베이스, AI 모듈이 통합된 완전 자동화 시스템*

Genesis는 수천 개의 상호작용하는 인과관계 성분을 가진 시스템 생물학 모델을 자동으로 개선하기 위해 설계된 다음 세대 로봇 과학자이며, 하루에 1,000개의 가설 기반 폐쇄 루프 실험 사이클을 병렬로 실행할 수 있다.

## Motivation

- **Known**: Adam(효모 기능 생물학)과 Eve(신약 개발 초기 단계) 로봇 과학자가 성공적으로 개발되어 폐쇄 루프 자동화 실험의 가능성을 입증함
- **Gap**: 기존 고처리량 방식은 각 실험이 모델에 대한 가설을 직접 검증하지 못하므로 시스템 생물학 모델 개선에 부적합함. 진핵생물 시스템 생물학 모델의 복잡성(수천 개 유전자, 단백질, 소분자 상호작용)은 인간의 직관적 이해를 초과함
- **Why**: 정보이론에 따르면 생물학적 시스템 이해에 필수적인 방대한 수의 실험이 필요하며, Duhem 논제(실험은 고립된 가설이 아닌 전체 이론 집단을 검증)로 인해 AI 기반 접근이 더 효율적임
- **Approach**: 1,000개의 μ-바이오리액터, 자동화된 질량분석(AutonoMS), 구조화된 온톨로지 기반 데이터베이스(Genesis-DB), 모델 수정 추적(RIMBO), 관계형 학습 기반 개선 알고리즘(LGEM+)을 통한 통합 플랫폼 개발

## Achievement

![Fig 2](Genesis_fig2.png)
*그림 2. Genesis 하드웨어: (a) Chalmers에서 운영 중인 초기 12개 μ-바이오리액터 시스템, (b) 유체 및 마이크로-포뮬레이터 설계 개요*

![Fig 3](Genesis_fig3.png)
*그림 3. Genesis 질량분석 플랫폼: Agilent RapidFire 로봇 시스템과 이온 이동도 질량분석(IM-MS) 6560 시스템*

1. **하드웨어 혁신**: 1,000개의 컴퓨터 제어식 μ-바이오리액터 시스템 개발 완료(초기 12개 시스템 운영). 각 바이오리액터는 배치(batch), 유가식 배치(fed-batch), 연속 배양 모드를 실시간으로 전환 가능하며, 실험 조건의 광범위한 탐색 가능

2. **고처리량 분석 플랫폼**: AutonoMS를 통해 하루 약 10,000회의 대사체(metabolite) 측정 수행 가능 달성(크로마토그래피 단계 제거로 기존 시스템 대비 획기적 향상). 5초 샘플 분석 시간으로 표적 및 비표적 대사체학 실험 검증 완료

3. **구조화된 데이터 인프라**: Genesis-DB를 통해 RDF/Datalog 기반 구조화 정보에 대한 소프트웨어 에이전트 접근 환경 구축. 유전자 발현 데이터로부터 자동 가설 생성 및 실험 설계 가능 시연(그림 4)

4. **모델 변화 추적**: RIMBO(Revisions for Improvements of Models in Biology Ontology) 온톨로지 개발로 수십만 건의 모델 수정사항을 체계적으로 기록 및 추론 가능하게 함

## How

![Fig 4](Genesis_fig4.png)
*그림 4. 유전자 발현 네트워크 재구성 → 실험 조건 검색 → 가설 및 실험 절차 기록 → 신규 데이터 포함 네트워크 재구성 → 시각화 업데이트의 사이클*

- **실험 설계 매개변수**: 유전체(20,000개 삭제 및 리포터 변이주 라이브러리), 성장률/OD(케모스탯/터빈도스탯), 배양 배지(10개 대사물질 칵테일, ~100가지 조합), 약물(~10,000가지 화합물 조합)

- **데이터 수집**: 성장률(배치 배양), 배양액 대사 분석(~10가지 화합물), 효모 내부 상태(~100개 대사물질), 유전자 발현 수준(~6,000개 유전자)을 자동화된 방식으로 수집

- **온톨로지 기반 지식 관리**: 실험 조건(온도, pH, 배지, 샘플링 시간 등), 실험 결과(유전자 카운트, 질량분석 데이터) 메타데이터를 RDF 형식으로 구조화하여 과거 실험 추론 및 미래 실험 계획 지원

- **AI 모듈**: 귀납 논리 프로그래밍(ILP) 기반 실험 계획과 LGEM+(게놈 규모 대사 모델의 자동 개선을 위한 관계형 학습 시스템) 적용

## Originality

- **복잡도의 획기적 증가**: 기존 폐쇄 루프 자동 시스템은 단순 입출력 블랙박스 최적화에 집중했으나, Genesis는 수천 개의 상호작용하는 인과관계 성분과 수만 개의 매개변수를 가진 모델을 다룸

- **병렬 처리 규모**: 하루 1,000개의 가설 기반 폐쇄 루프 실험 사이클을 병렬 실행 가능한 첫 시스템(이전 시스템은 수십 개 규모)

- **통합 온톨로지 아키텍처**: 실험 조건, 결과, 시스템 모델을 RDF 기반 통일된 형식으로 관리하여 소프트웨어 에이전트의 자율적 추론 및 계획 가능하게 함

- **고처리량 자동화 분석**: AutonoMS를 통해 기존 크로마토그래피 기반 질량분석(수시간)을 5초 단위로 단축하고 일일 10,000회 측정 달성

- **실증된 비용-편익 목표**: 인간 과학자 대비 100배 비용 효율성 달성 목표로 설정하고 단계적 검증

## Limitation & Further Study

- **완성도 미달**: 논문에서 표시된 italics 모듈(예: 고수준 AI 단위 일부)이 아직 미완성 상태이며, 전체 1,000개 바이오리액터 시스템은 초기 12개 시스템 단계에서 스케일링 필요

- **LGEM+ 상세 기술 부족**: 관계형 학습을 통한 게놈 규모 대사 모델 자동 개선 알고리즘의 구체적 구현 및 성능 평가 결과가 제시되지 않음

- **검증 데이터 제한**: 이전 증명-개념 연구(diauxic shift)에서 92개 유전자 및 1,048개 상호작용 추가 성과가 언급되었으나, Genesis 플랫폼 완성 후 대규모 실험 데이터 없음

- **비용 분석 미흡**: 100배 비용 효율성 목표는 제시하였으나, 상세한 경제학적 분석(개발비, 운영비, 시간당 비용) 제공 부족

- **생물학적 일반화 가능성**: 효모(S. cerevisiae)에 최적화되어 있어 다른 진핵생물로의 전이 가능성 불명확

## Evaluation

- **Novelty**: 4.5/5 — 폐쇄 루프 자동화 규모의 획기적 확대와 온톨로지 기반 통합 아키텍처의 창의성 높음. 단, 개별 기술(μ-바이오리액터, 질량분석, ILP)은 기존 기술 조합

- **Technical Soundness**: 4/5 — 하드웨어 시스템(초기 12개 바이오리액터)과 AutonoMS 검증 완료. 그러나 전체 1,000개 시스템과 LGEM+ 알고리즘의 성능 평가 데이터 부재로 완전한 기술 검증 미완료

- **Significance**: 4.5/5 — 시스템 생물학 연구의 자동화 가능성을 혁신적으로 제시하며, 약물 개발 및 합성생물학에 광범위한 응용 가능. 인간 과학자의 역할 재정의라는 철학적 함의도 중요

- **Clarity**: 3.5/5 — 전체 아키텍처 및 하드웨어는 명확하나, LGEM+ 알고리즘, RIMBO 온톨로지 세부 구조(그림 5 텍스트 절단), 소프트웨어 에이전트의 구체적 동작 메커니즘이 불충분하게 설명됨

- **Overall**: 4.2/5

**총평**: Genesis 프로젝트는 AI 기반 과학 자동화의 다음 단계를 제시하는 야심 찬 계획으로, 통합된 하드웨어-소프트웨어 플랫폼과 온톨로지 기반 지식 관리의 혁신성이 높다. 다만 대규모 시스템 완성과 LGEM+ 알고리즘의 성능 검증이 필요하며, 논문의 일부 핵심 기술 설명이 미완성된 점이 한계이다.

## Related Papers

- 🔄 다른 접근: [[papers/805_The_Virtual_Lab_of_AI_agents_designs_new_SARS-CoV-2_nanobodi/review]] — Genesis의 시스템 생물학 대규모 자동화와 Virtual Lab의 특정 단백질 설계 자동화는 서로 다른 규모에서 생물학적 발견을 자동화하는 접근이다.
- 🔗 후속 연구: [[papers/745_Self-driving_laboratories_to_autonomously_navigate_the_prote/review]] — 자율적 단백질 공간 탐색을 위한 실험실 자동화가 Genesis의 대규모 병렬 가설 검증 시스템을 단백질 특화 영역으로 확장한 적용이다.
- 🏛 기반 연구: [[papers/133_Automating_quantum_computing_laboratory_experiments_with_an/review]] — 양자 컴퓨팅 실험 자동화 방법론이 Genesis의 고속 병렬 실험 사이클 구현을 위한 핵심적인 기술적 토대를 제공한다.
- 🏛 기반 연구: [[papers/805_The_Virtual_Lab_of_AI_agents_designs_new_SARS-CoV-2_nanobodi/review]] — Genesis의 대규모 병렬 실험 자동화 방법론이 Virtual Lab의 학제간 AI 에이전트 협업을 통한 단백질 설계의 기술적 토대이다.
