---
title: "758_Simulations_in_the_era_of_exascale_computing"
authors:
  - "Choongseok Chang"
  - "Volker L. Deringer"
  - "Kalpana S. Katti"
  - "Veronique Van Speybroeck"
  - "Christopher M. Wolverton"
date: "2023.03"
doi: "10.1038/s41578-023-00540-6"
arxiv: ""
score: 4.0
essence: "엑사스케일(exascale) 슈퍼컴퓨터의 등장으로 계산 재료과학(computational materials science) 분야에서 획기적인 발전이 가능해지고 있으며, 다양한 분야의 연구자들이 이 기술을 활용하여 새로운 시뮬레이션 가능성과 직면한 도전과제를 공유하는 관점 논문이다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Scientific_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chang et al._2023_Simulations in the era of exascale computing.pdf"
---

# Simulations in the era of exascale computing

> **저자**: Choongseok Chang, Volker L. Deringer, Kalpana S. Katti, Veronique Van Speybroeck, Christopher M. Wolverton | **날짜**: 2023-03-13 | **DOI**: [10.1038/s41578-023-00540-6](https://doi.org/10.1038/s41578-023-00540-6)

---

## Essence

엑사스케일(exascale) 슈퍼컴퓨터의 등장으로 계산 재료과학(computational materials science) 분야에서 획기적인 발전이 가능해지고 있으며, 다양한 분야의 연구자들이 이 기술을 활용하여 새로운 시뮬레이션 가능성과 직면한 도전과제를 공유하는 관점 논문이다.

## Motivation

- **Known**: 기존의 슈퍼컴퓨터는 제한된 계산 능력으로 인해 시뮬레이션 길이 및 시간 스케일에 제약이 있었으며, 실험 관찰과의 간극이 존재했음

- **Gap**: 초당 10^18 부동소수점 연산(FLOPS)을 수행할 수 있는 엑사스케일 컴퓨터(2022년 미국 Frontier 등장, 중국의 OceanLight·Tianhe-3, 유럽의 JUPITER 계획)의 출현에도 불구하고, 이들이 각 분야에서 실제로 어떤 기회와 도전을 제시하는지에 대한 다학제적 분석이 부족함

- **Why**: 단순한 계산 능력 증대뿐 아니라 알고리즘·방법론 혁신과 함께 실제 응용 가능성을 다루어야 함

- **Approach**: 융합 에너지(fusion research), 계산 화학·재료 모델링, 생물학적 시스템 시뮬레이션, 구조 복잡성 재료과학, 재료 발견 등 5개 분야의 전문가들이 각자의 관점에서 엑사스케일 컴퓨팅의 기회와 병목(bottleneck)을 분석

## Achievement

1. **엑사스케일 컴퓨팅의 분야별 기회 제시**:
   - **재료 모델링**: 더 큰 원자 시스템, 현실적인 길이 스케일, 결함 포함, 더 긴 시간 스케일의 시뮬레이션 가능
   - **융합 에너지**: ITER 및 미래 자기 핵융합 반응로의 열부하 발자국(heat-load footprint) 물리학을 더 높은 충실도(fidelity)로 연구 가능
   - **생물 시스템**: 다단계(multiscale) 생물학적 모델링으로 조직 재생, 신경질환, 암 진행·전이 이해의 비약적 진전 예상
   - **구조 재료**: 원자 규모 시뮬레이션의 현실성 증대로 "설명적" 역할에서 "예측적" 역할로 전환 — 실험 전에 합성 과정을 원자 단계에서 기술하고 반응물·조건 예측

2. **다학제적 관점의 통합**: 물리, 화학, 생물학, 재료공학 등 다양한 분야의 도전과제를 체계적으로 정의

## How

- **알고리즘 혁신과 병행**: 단순 컴퓨팅 파워 증대뿐 아니라 신규 코드 개발·기존 코드 적응이 필수적
  
- **길이·시간 스케일 극복**: 
  - 원자 규모 시뮬레이션과 실험 관찰 길이 스케일의 수렴(nanoscale devices에서 high-resolution electron microscopy와의 일치)
  - 다단계 모델링(multiscale modeling), 조대화(coarse-graining), 유한요소법(finite-element modeling), 이산요소법(discrete element modeling) 등의 연계

- **동역학적 복잡성 포착**:
  - 결함(defects), 작동 조건(operating conditions)에서의 동적 과정 모델링
  - 음성 피드백(non-local, nonlinear) 및 다중 시간 스케일을 포함한 통합 최적화

- **기계학습 활용**: 데이터 기반 모델과 물리 기반 모델의 통합으로 계산 효율성 향상

- **워크플로우 자동화**: 개별 시뮬레이션 수작업 대신 효율적인 자동화 환경 구축

## Originality

- **다학제적 종합 분석**: 물리·화학·생물·재료공학 등 서로 다른 분야 전문가들이 각각의 도전과제를 체계적으로 기술하여, 엑사스케일 컴퓨팅의 일반적 기회와 분야별 특수성을 동시에 제시

- **"설명에서 예측으로의 전환" 강조**: 전통적 사후 분석(post-hoc explanation)에서 사전 예측 가이드(predictive guidance)로의 패러다임 전환을 명확히 제시

- **아직 풀리지 않은 과제의 명시**: 단순한 낙관론을 넘어 계산 인프라의 부족, 검증(validation) 난제, 의료 커뮤니티의 신뢰도 확보 등 현실적 장애물을 솔직하게 언급

## Limitation & Further Study

- **추상적 기술의 한계**: 실제 구현 방법론이나 구체적인 알고리즘 제시 부족 — "뭐가 가능한가"는 명확하지만 "어떻게 하는가"는 덜 구체적

- **검증·신뢰도 문제의 심화**: 시뮬레이션 데이터 폭증에 따른 검증 어려움, 기계학습 모델의 블랙박스 특성에 대한 솔루션 부재

- **데이터·코드 공개의 문화적 과제**: 기술적 진전만큼이나 오픈 사이언스 문화 정착의 필요성이 강조되지만 구체적 전략 부족

- **후속 연구 방향**:
  - 엑사스케일 컴퓨터에 최적화된 새로운 알고리즘 개발
  - 길이·시간 스케일 변환 기술의 이론적 근거 강화
  - 기계학습과 물리 기반 시뮬레이션의 신뢰도 높은 통합 방안
  - 각 분야에서의 실제 사례 연구 및 벤치마킹

## Evaluation

- **Novelty**: 4/5 — 엑사스케일 시대의 다학제적 종합 분석은 신선하지만, 개별 기술 혁신보다는 기존 기술의 스케일 활용에 초점

- **Technical Soundness**: 3.5/5 — 각 분야의 전문가 견해는 신뢰할 만하지만, 구체적 기술적 증거나 수치 결과 부족

- **Significance**: 4.5/5 — 엑사스케일 시대 계산 과학의 로드맵을 제시하여 정책·연구 방향 결정에 매우 중요한 의견 제공

- **Clarity**: 4/5 — 다양한 분야를 아울러 전체적으로 이해하기 쉽지만, 학제 간 용어 차이로 인한 혼동 가능성

- **Overall**: 4/5

**총평**: 본 Viewpoint는 엑사스케일 컴퓨팅이 계산 과학 전반에 가져올 변혁적 기회를 다학제적 관점에서 균형 있게 제시하며, 기술 발전뿐 아니라 알고리즘 혁신, 검증 체계, 오픈 사이언스 문화의 중요성을 강조하는 전략적 문서로서의 가치가 높다.

## Related Papers

- 🧪 응용 사례: [[papers/621_Physics-informed_neural_network_for_multi-objective_design_o/review]] — 엑사스케일 컴퓨팅의 발전이 물리 정보 신경망을 활용한 대규모 다목적 설계 최적화를 가능하게 한다.
- 🔗 후속 연구: [[papers/1129_SARS-CoV-2_simulations_go_exascale_to_predict_dramatic_spike/review]] — SARS-CoV-2 시뮬레이션의 엑사스케일 확장이 계산 재료과학 분야 엑사스케일 활용의 구체적 사례이다.
- 🏛 기반 연구: [[papers/695_Scaling_Deep_Learning_for_Materials_Discovery/review]] — 재료 발견을 위한 딥러닝 확장 연구가 엑사스케일 컴퓨팅 활용의 기술적 기반을 제공한다.
- 🔗 후속 연구: [[papers/095_AMDAT_An_Open-Source_Molecular_Dynamics_Analysis_Toolkit_for/review]] — 엑사스케일 컴퓨팅 시대에서 시뮬레이션의 확장된 역할과 가능성
