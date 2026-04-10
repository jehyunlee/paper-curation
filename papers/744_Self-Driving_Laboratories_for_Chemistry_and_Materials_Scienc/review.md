---
title: "744_Self-Driving_Laboratories_for_Chemistry_and_Materials_Scienc"
authors:
  - "Gary Tom"
  - "Stefan P. Schmid"
  - "Sterling G. Baird"
  - "Yang Cao"
  - "Kourosh Darvish"
date: "2024.08"
doi: "10.1021/acs.chemrev.4c00055"
arxiv: ""
score: 4.2
essence: "자율 실험실(Self-Driving Laboratories, SDL)은 실험 워크플로우의 자동화와 데이터 기반 의사결정을 결합하여 화학 및 재료 과학 연구의 속도를 획기적으로 가속화할 수 있는 기술이다. 이 종합 리뷰는 SDL의 현황, 기반 기술, 실제 응용 사례, 그리고 각 분야의 도전 과제를 체계적으로 분석한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/AI_Chemistry_Planning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Tom et al._2024_Self-Driving Laboratories for Chemistry and Materials Science.pdf"
---

# Self-Driving Laboratories for Chemistry and Materials Science

> **저자**: Gary Tom, Stefan P. Schmid, Sterling G. Baird, Yang Cao, Kourosh Darvish, Han Hao, Stanley Lo, Sergio Pablo-García, Ella M. Rajaonson, Marta Skreta, Naruki Yoshikawa, Samantha Corapi, Gun Deniz Akkoc, Felix Strieth-Kalthoff, Martin Seifrid, Alán Aspuru-Guzik | **날짜**: 2024-08-28 | **DOI**: [10.1021/acs.chemrev.4c00055](https://doi.org/10.1021/acs.chemrev.4c00055)

---

## Essence

자율 실험실(Self-Driving Laboratories, SDL)은 실험 워크플로우의 자동화와 데이터 기반 의사결정을 결합하여 화학 및 재료 과학 연구의 속도를 획기적으로 가속화할 수 있는 기술이다. 이 종합 리뷰는 SDL의 현황, 기반 기술, 실제 응용 사례, 그리고 각 분야의 도전 과제를 체계적으로 분석한다.

## Motivation

- **Known**: 실험실 자동화는 1940년대부터 시작되었으며, 액체 처리(liquid handling), 시료 준비(sample preparation), 데이터 분석 등 기초적인 작업에 초점을 맞추어 왔다. 기존 연구 방법은 점진적 진행과 낮은 효율성으로 특징지어진다.

- **Gap**: 전통적 연구 방법만으로는 기후 변화, 에너지 지속성, 의료 위기 등 전지구적 도전에 대응하기에 불충분하며, 자동화와 데이터 기반 의사결정의 통합에 관한 체계적 종합 분석이 부재하다.

- **Why**: 기후 변화와 자원 부족, 신흥 보건 위기에 직면하여 가속화된 재료 개발과 과학적 이해가 필수적이며, 자동화된 실험은 높은 처리량(throughput), 정확도, 폐쇄형 루프(closed-loop) 최적화를 제공한다. 또한 재현성 문제와 귀무 결과(null results)의 미보도 문제를 해결할 수 있다.

- **Approach**: 자동화된 실험 워크플로우(하드웨어)와 자동화된 데이터 기반 의사결정(소프트웨어)의 이중 구조를 바탕으로 SDL을 분류하고, 하드웨어와 소프트웨어 자율성 수준을 Level 1-5로 계층화하여 화학 반응 최적화, 약물 발견, 구조 재료, 광전자, 에너지 저장 등 다양한 분야의 실제 사례를 포괄적으로 검토한다.

## Achievement

![Figure 1: SDL 자율성 수준의 개념적 분류](https://doi.org/10.1021/acs.chemrev.4c00055)
*하드웨어와 소프트웨어 자율성 범주에 따른 SDL의 자율성 수준 분류*

1. **SDL 자율성의 계층적 분류 체계 제시**: 소프트웨어 자율성(실험 선택)을 3단계(단일 반복 자동화 실험, 폐쇄형 루프 반복, 생성적 접근), 하드웨어 자율성(실험 실행)을 3단계(단일 작업 설정, 다중 작업 워크플로우, 완전 자동화 실험실)로 구분하고, Level 1-5의 계층화된 분류 시스템을 제안하여 SDL의 다양한 형태를 명확하게 정의.

2. **SDL 기반 기술의 포괄적 개요**: 특수 로봇, 범용 로봇 응용, 개방형 하드웨어, 컴퓨터 비전(computer vision), 디지털 트윈(digital twin), 안전 프로토콜 등 하드웨어; 오케스트레이션(orchestration), 통신 프로토콜, 데이터 관리, AI 역할, 베이지안 최적화(Bayesian optimization), 능동 학습(active learning) 등 소프트웨어 기술을 상세히 분석.

3. **광범위한 실제 응용 사례의 검증**: 반응 최적화(단일/다중 단계 유기 반응, 촉매 발견), 약물 발견(약물 발견 파이프라인, 합성 생물학), 구조 재료(합금 설계, 콘크리트 포뮬레이션), 광전자(페로브스카이트, 나노입자, 박막), 에너지 저장(리튬 이온 배터리, 연료전지) 등 다양한 분야에서의 성공적 적용 사례를 제시.

## How

- **이중 자율성 축 구조**: 소프트웨어 자율성(실험 선택의 자동화, 데이터 기반 의사결정)과 하드웨어 자율성(실험 실행의 자동화)을 독립적으로 평가하여 SDL의 역량을 다차원적으로 분류

- **폐쇄형 루프 최적화 메커니즘**: 초기 실험 결과를 알고리즘에 피드백하여 다음 실험을 자동으로 설계하는 반복적 프로세스로 화학 공간 탐색 효율성 극대화

- **베이지안 최적화와 능동 학습**: 제한된 데이터로부터 확률론적 모델을 구축하여 불확실성을 정량화하고, 정보 가치가 높은 실험을 우선적으로 선택

- **AI/ML 통합 의사결정**: 고품질 대규모 데이터셋을 생성하는 자동화된 실험을 통해 머신러닝 모델의 정확도를 향상시키고, 더 나은 예측 기반 실험 계획 수립

- **표준화된 프로토콜 관리**: 실험 재현성과 데이터 공유를 위한 오케스트레이션 소프트웨어와 통신 프로토콜 개발로 상이한 하드웨어 플랫폼의 통합 운영

## Originality

- **처음으로 시도된 포괄적 체계화**: SDL 기술의 역사(1940년대부터 현대)를 종합적으로 추적하고, 하드웨어-소프트웨어 이중 축의 자율성 분류 프레임워크를 제시하여 SDL 분야의 개념적 기초 정립

- **다학제적 응용 범위의 확대**: 약물 발견, 화학 합성, 재료 과학(광전자, 에너지 저장), 생합성 등 화학 및 재료 과학의 모든 주요 분야를 아우르는 최초의 포괄적 리뷰

- **실제 구현 사례 중심의 실용적 관점**: 개념적 분류에 그치지 않고, Level 2-4 SDL의 수십 개 실제 사례를 분석하여 각 분야의 구체적 성과와 한계를 명확히 규명

- **기술 수렴의 시점 포착**: AI/ML 발전, 정교한 로봇 기술, 컴퓨터 비전의 성숙으로 일반 목적의 화학 실험실 작업 자동화가 가능해진 최신 동향을 문서화

## Limitation & Further Study

- **Level 5 SDL의 미실현**: 현재까지 진정한 Level 5 SDL(소프트웨어와 하드웨어 양 측면에서 완전 자율성 달성)은 달성되지 못했으며, 복잡한 다단계 유기 합성이나 미지의 반응 조건 탐색에서의 한계 존재

- **하드웨어 일반화 문제**: 대부분의 현존 SDL이 특정 작업(액체 처리, 특정 반응 유형)에 특화되어 있어, 다양한 화학 반응과 재료 합성을 아우르는 범용 로봇 시스템 개발이 필요

- **데이터 품질 및 공유의 표준화 부재**: 자동화된 실험으로부터 생성되는 대규모 데이터를 효과적으로 활용하기 위한 통일된 데이터 포맷, 저장소, 접근성 표준 미비

- **안전성, 규제, 윤리 문제 미흡**: 실험실 로봇의 안전 프로토콜, 규제 준수(특히 약물 발견), 과학적 투명성 및 윤리에 관한 깊이 있는 논의 필요

- **후속 연구 방향**:
  - 범용 로봇과 컴퓨터 비전의 추가 발전으로 복잡한 화학 작업 자동화 실현
  - 다중 로봇 협력 시스템 및 분산 자동화 실험실 네트워크 개발
  - 대규모 데이터셋 기반 생성 모델(generative model)의 화학 공간 탐색 능력 확대
  - 학제 간 협력을 통한 SDL 기술과 화학 도메인 지식의 심화된 통합

## Evaluation

- **Novelty**: 4.5/5
  - SDL의 계층적 분류 체계와 이중 자율성 축 프레임워크는 혁신적이며, 역사적 맥락에서의 체계적 정리가 우수함. 다만, 개별 기술(베이지안 최적화, 능동 학습 등)의 기원은 기존 연구에 기반함.

- **Technical Soundness**: 4/5
  - 반응 최적화, 약물 발견, 재료 과학 등 다양한 분야의 구체적 사례 분석과 기술 설명이 정확하고 신뢰성 있음. 다만, 일부 신흥 기술(디지털 트윈, 조작 기술 학습)에 대한 깊이 있는 기술적 평가는 제한적.

- **Significance**: 4.5/5
  - 화학 및 재료 과학 분야의 연구 패러다임 전환을 시사하며, 산업계(제약, 재료)와 학계 양측에 높은 실용적 가치를 제공함. SDL 기술의 채택 확대를 촉진할 가능성이 높음.

- **Clarity**: 4/5
  - 명확한 구조와 단계별 설명으로 복잡한 SDL 개념을 일반화하려는 노력이 탁월함. Figure 1의 자율성 분류도 직관적임. 다만, 기술 용어의 정의가 때로 간결하여 초보자 입문성은 다소 낮음.

- **Overall**: 4.2/5

**총평**: 이 리뷰는 자율 실험실 기술의 현황을 종합적으로 분석한 권위 있는 문헌으로, 명확한 분류 체계와 다양한 실제 응용 사례를 통해 SDL 분야의 로드맵을 제시한다. 다만 Level 5 SDL의 미실현과 범용 시스템 개발의 과제는 향후 해결해야 할 중요한 기술적 난제를 시사한다.

## Related Papers

- 🧪 응용 사례: [[papers/461_LARC_Towards_Human-level_Constrained_Retrosynthesis_Planning/review]] — LARC의 제약조건 기반 역합성 계획은 자율 실험실에서 실제 화학 합성을 자동화하는 핵심 응용 기술입니다
- 🔗 후속 연구: [[papers/126_Automated_review_generation_method_based_on_large_language_m/review]] — 자율 실험실의 자동화된 실험 워크플로우는 대형 언어모델 기반 자동 리뷰 생성을 실험 설계 영역으로 확장한 응용입니다
- 🏛 기반 연구: [[papers/133_Automating_quantum_computing_laboratory_experiments_with_an/review]] — 양자 컴퓨팅 실험실 자동화는 자율 실험실 기술의 특수한 분야별 구현 사례를 제공합니다
- 🧪 응용 사례: [[papers/254_DataJoint_20_A_Computational_Substrate_for_Agentic_Scientifi/review]] — 자율 실험실 프레임워크가 과학 워크플로우 기반 위에서 구현됨
- 🧪 응용 사례: [[papers/461_LARC_Towards_Human-level_Constrained_Retrosynthesis_Planning/review]] — 자율 실험실 기술은 LARC의 역합성 계획을 실제 화학 실험으로 구현하는 응용 분야입니다
- 🏛 기반 연구: [[papers/614_Perspective_on_utilizing_foundation_models_for_laboratory_au/review]] — 화학 및 재료 과학을 위한 자율주행 실험실이 실험실 자동화에서 기초 모델 활용의 이론적 토대입니다.
- 🏛 기반 연구: [[papers/1125_Accelerating_cell_culture_media_development_using_Bayesian_o/review]] — 화학과 재료과학의 자율주행 실험실이 베이지안 최적화의 이론적 기반
- 🏛 기반 연구: [[papers/1126_Autonomous_platform_for_solution_processing_of_electronic_po/review]] — 화학 및 재료과학을 위한 자율주행 실험실 서베이는 Polybot의 AI 기반 자동화 연구실 설계에 이론적 배경과 방법론적 가이드라인을 제공한다.
