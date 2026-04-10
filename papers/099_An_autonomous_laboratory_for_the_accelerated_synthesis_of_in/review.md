---
title: "099_An_autonomous_laboratory_for_the_accelerated_synthesis_of_in"
authors:
  - "N. Szymanski"
  - "Bernardus Rendy"
  - "Yuxing Fei"
  - "Rishi E. Kumar"
  - "T. He"
date: "2023"
doi: "10.1038/s41586-023-06734-w"
arxiv: ""
score: 4.8
essence: "A-Lab(자율 실험실)은 계산화학, 기계학습, 능동 학습을 통합한 로봇 시스템으로, 17일간의 연속 운영을 통해 57개 목표 재료 중 36개(63% 성공률)의 무기 분말 화합물 합성에 성공하였다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Materials_Discovery_Hypotheses"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Szymanski et al._2023_An autonomous laboratory for the accelerated synthesis of inorganic materials.pdf"
---

# An autonomous laboratory for the accelerated synthesis of inorganic materials

> **저자**: N. Szymanski, Bernardus Rendy, Yuxing Fei, Rishi E. Kumar, T. He | **날짜**: 2023 | **DOI**: [10.1038/s41586-023-06734-w](https://doi.org/10.1038/s41586-023-06734-w)

---

## Essence

A-Lab(자율 실험실)은 계산화학, 기계학습, 능동 학습을 통합한 로봇 시스템으로, 17일간의 연속 운영을 통해 57개 목표 재료 중 36개(63% 성공률)의 무기 분말 화합물 합성에 성공하였다.

## Motivation

- **Known**: 고처리량(high-throughput) 계산 스크리닝을 통해 새로운 물질을 대규모로 발굴할 수 있지만, 이들의 실험적 실현은 어렵고 시간이 많이 소요된다.

- **Gap**: 계산 화면(screening)의 속도와 실험적 검증 속도 사이의 큰 차이가 존재한다. 기존 자율 연구 사례들은 특정 최적화 영역(광기전력, 촉매활성 등)에만 국한되어 있다.

- **Why**: 인간 연구자는 풍부한 배경 지식을 통합하여 의사결정하는데, 이를 기계학습과 활용 데이터, 능동 학습으로 구현해야 한다.

- **Approach**: 로봇공학, ab initio 데이터베이스, 문헌 채굴 기반 ML 모델(합성 제안), 능동 학습(ARROWS3)을 통합한 자율 실험실 플랫폼 개발.

## Achievement

![A-Lab 자율 재료 합성 시스템 개요. DFT 계산 convex hull에서 공기 안정 목표 물질을 선정하고, 문헌 기반 ML 모델로 합성 조리법을 제안한 후, 로봇 실험실에서 실행 및 특성화. 높은 수율을 얻지 못하면 능동 학습 알고리즘이 반응 경로를 최적화.](figure1.png)

1. **높은 성공률 달성**: 57개 목표 물질 중 36개 합성 성공(63%), 33개 원소와 40개 구조 원형(structural prototype)을 포함

2. **문헌 기반 초기 조리법의 효과**: 353개 테스트된 합성 조리법 중 30%만 성공했으나, ML 모델이 제안한 처음 5개 조리법으로 30개 재료 합성 가능 (문헌에서 유사 재료를 효과적으로 판별)

3. **능동 학습의 개선 효과**: ARROWS3 알고리즘을 통해 9개 목표 물질 최적화, 이 중 6개는 초기 조리법에서 0% 수율이었으나 개선됨

4. **계산 화면의 신뢰성 증명**: 분해 에너지(decomposition energy) 범위에서 열역학적 안정성과 합성 성공 사이 명확한 상관관계 부재 → 계산만으로 합성 가능성을 충분히 예측하기 어려움을 시사

## How

![A-Lab 작동 흐름도. (1) 분말 투여 및 혼합, (2) 샘플 가열, (3) XRD 특성화. 각 단계는 로봇팔로 자동 연결. ML 모델이 XRD 패턴을 분석하고 Rietveld 정제로 확인.](figure1.png)

- **재료 선정**: Materials Project 및 Google DeepMind convex hull에서 공기 안정 물질(<10 meV/atom) 선정, O₂/CO₂/H₂O와 반응하지 않는 물질만 포함

- **초기 조리법 생성**: 문헌에서 추출한 대규모 합성 데이터셋으로 학습한 ML 모델이 목표 물질과 유사한 기존 물질 기반의 조리법 제안 (최대 5개), 별도 ML 모델이 가열 온도 예측

- **자동 합성 수행**: 
  - Station 1: 전구체 분말 투여·혼합 및 알루미나 도가니로 이송
  - Station 2: 4개 박스 로를 이용한 가열
  - Station 3: 분쇄 및 XRD 측정

- **XRD 분석 및 피드백**:
  - 확률적 ML 모델(ICSD 학습)이 XRD 패턴에서 상(phase) 및 중량 분율 추출
  - 계산 구조로부터 시뮬레이션된 회절 패턴과 비교 (DFT 오차 보정)
  - 자동 Rietveld 정제로 확인

- **능동 학습**: 목표 수율 50% 미달 시, ARROWS3 알고리즘이 (1) 쌍대 반응 가정과 (2) 최소 구동력 중간 상태 회피를 통해 개선된 경로 제시

- **의사결정 자동화**: API 기반 통합으로 인간 개입 없이 실시간 의사결정 및 작업 제출 가능

## Originality

- **자동화에서 자율성으로의 도약**: 단순 로봇 자동화가 아닌, ML과 능동 학습으로 데이터 해석 및 의사결정을 수행하는 진정한 자율 시스템 구현

- **고체 분말 합성의 고유한 과제 해결**: 액체 취급 기반 유기화학의 자율 워크플로우와 달리, 고체 분말의 밀도, 유동성, 입자 크기 등 다양한 물리적 성질 대응

- **다층적 지식 통합**: ab initio 계산, 문헌 텍스트 마이닝, 구조 데이터베이스, 열역학 기반 능동 학습을 단일 플랫폼에 결합

- **상업화 친화적 설계**: 다중 그램 샘플 생산으로 소자 수준 테스트 가능, 고체 분말 형태는 스케일업 및 제조에 유리

- **미처리 대상에 대한 첫 시도**: 모든 목표 물질이 훈련 데이터에 미포함된 신규 화합물로, 일반화 능력 증명

## Limitation & Further Study

- **샘플 순도 문제**: 4시간 유지(hold time)로 인해 불완전한 반응으로 많은 부산물 포함. 더 긴 유지 시간과 간헐적 재분쇄로 상 순도 개선 가능

- **자동 XRD 해석의 한계**: 다중 상 혼합물을 결정적으로 식별하기 어렵지만, 주 상(majority phase) 식별은 신뢰성 있음. 4개 재료는 주관적 재검토 결과 불확실

- **계산 실패 모드**: 17개 미합성 재료 중 일부는 계산 예측 오류로 인한 실패. DFT 구조의 부분 무질서(partial disorder) 표현 불가

- **알고리즘 개선 여지**: 의사결정 알고리즘의 경미한 수정으로 67% 성공률, 계산 기법 개선으로 70% 달성 예상

- **향후 연구 방향**:
  - 액체 취급 자동화 추가로 화학 다양성 확대
  - 더 정교한 활성 학습으로 반응 경로 최적화
  - 소자 특성화(device-level characterization) 통합
  - 구조 무질서 표현 능력 향상


## Evaluation

- Novelty: 5/5
- Technical Soundness: 4.5/5
- Significance: 5/5
- Clarity: 4.5/5
- Overall: 4.8/5

**총평**: 본 논문은 계산 화면과 실험 검증 사이의 병목을 해결하는 획기적인 자율 실험실을 제시하며, ab initio 계산, 기계학습, 능동 학습의 통합을 통해 63%의 높은 합성 성공률을 입증하였다. 고체 분말 합성의 고유한 과제를 해결하고 향후 AI 기반 재료 발굴의 새로운 패러다임을 제시한다는 점에서 재료과학 분야의 중요한 이정표이다.

## Related Papers

- 🔄 다른 접근: [[papers/684_Robot-assisted_mapping_of_chemical_reaction_hyperspaces_and/review]] — 화학반응 매핑과 재료 합성 자동화라는 서로 다른 자율실험실 응용분야를 다룬다.
- 🔗 후속 연구: [[papers/658_Real-time_experiment-theory_closed-loop_interaction_for_auto/review]] — AMASE의 실시간 폐루프 개념을 재료 합성 최적화에 적용할 수 있다.
- 🏛 기반 연구: [[papers/134_Automating_the_practice_of_science_Opportunities_challenges/review]] — 과학 자동화의 일반적 프레임워크가 자율 실험실 구현의 이론적 기반을 제공한다.
- 🔄 다른 접근: [[papers/684_Robot-assisted_mapping_of_chemical_reaction_hyperspaces_and/review]] — 둘 다 자율 실험실 개념이지만 A-Lab은 무기재료, 이 논문은 화학반응에 특화되어 있다.
- 🔄 다른 접근: [[papers/658_Real-time_experiment-theory_closed-loop_interaction_for_auto/review]] — 재료 탐색의 실시간 폐루프 vs 자율 합성이라는 서로 다른 자동화 접근법을 보여준다.
- 🔗 후속 연구: [[papers/043_Accelerating_Drug_Discovery_Through_Agentic_AI_A_Multi-Agent/review]] — 자율 실험실의 무기 고체 합성 자동화가 Artificial 플랫폼의 신약 개발 워크플로우 조정 능력을 소재 과학으로 확장함
- 🔗 후속 연구: [[papers/745_Self-driving_laboratories_to_autonomously_navigate_the_prote/review]] — 단백질 특화 자동화를 더 넓은 화학 합성 자동화로 확장하여 포괄적인 자율 실험실 구축 방향을 제시한다.
- 🔗 후속 연구: [[papers/1126_Autonomous_platform_for_solution_processing_of_electronic_po/review]] — 무기 재료의 가속 합성을 위한 자율 실험실은 Polybot의 전자 고분자 최적화 방법론을 더 넓은 재료 합성 영역으로 확장한다.
