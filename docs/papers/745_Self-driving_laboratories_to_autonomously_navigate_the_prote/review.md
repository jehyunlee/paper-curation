---
title: "745_Self-driving_laboratories_to_autonomously_navigate_the_prote"
authors:
  - "Jacob T. Rapp"
  - "Bennett J. Bremer"
  - "Philip A. Romero"
date: "2023"
doi: "10.1101/2023.05.20.541582"
arxiv: ""
score: 4.5
essence: "단백질 공학을 완전히 자동화하는 SAMPLE(Self-driving Autonomous Machines for Protein Landscape Exploration) 플랫폼을 제시하며, 지능형 에이전트와 로봇 실험 시스템이 협력하여 글리코사이드 하이드롤라제(GH1)의 열 안정성을 12°C 이상 향상시킨 신약 개발 패러다임을 제안한다. ---"
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Autonomous_Laboratory_Biology"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Rapp et al._2023_Self-driving laboratories to autonomously navigate the protein fitness landscape.pdf"
---

# Self-driving laboratories to autonomously navigate the protein fitness landscape

> **저자**: Jacob T. Rapp, Bennett J. Bremer, Philip A. Romero | **날짜**: 2023 | **DOI**: [10.1101/2023.05.20.541582](https://doi.org/10.1101/2023.05.20.541582)

---

## Essence

![Figure 1](figures/fig1.webp)
*SAMPLE 플랫폼의 개요: (a) 지능형 에이전트가 서열-기능 관계를 학습하고 단백질을 설계하면, 자동화된 실험실 환경이 검증하고 피드백을 제공하는 폐쇄 루프 시스템 (b) 다중 출력 가우시안 프로세스 모델의 성능 (c-d) 시뮬레이션 기반 설계 전략 비교 (e) 자동화 파이프라인의 재현성 검증 (f) 다층 예외 처리 및 데이터 품질 관리 시스템*

단백질 공학을 완전히 자동화하는 SAMPLE(Self-driving Autonomous Machines for Protein Landscape Exploration) 플랫폼을 제시하며, 지능형 에이전트와 로봇 실험 시스템이 협력하여 글리코사이드 하이드롤라제(GH1)의 열 안정성을 12°C 이상 향상시킨 신약 개발 패러다임을 제안한다.

---

## Motivation

- **Known**: 인간 연구자들은 가설 생성 → 실험 설계 → 습식 실험 → 데이터 해석의 반복적 사이클을 통해 단백질 공학을 수행해왔으나, 로봇 과학자와 자율 실험실이 화학, 재료과학 등 다양한 분야에서 발견 과정을 가속화하고 있음

- **Gap**: 단백질 공학과 합성생물학 분야는 (1) 복잡하고 비선형적인 생물학적 표현형, (2) 고차원의 게놈 탐색 공간, (3) 오류가 많고 자동화가 어려운 다단계 습식 실험 처리 등의 고유한 난제로 인해 완전 자율 시스템의 구현이 지연되어 왔음

- **Why**: 인간의 개입 없이 설계-테스트-학습 사이클을 자동으로 반복할 수 있는 완전 자율 플랫폼이 필요하며, 이는 단백질 서열-기능 관계의 복잡한 지형을 효율적으로 탐색할 수 있음

- **Approach**: 베이지안 최적화(Bayesian Optimization)를 기반으로 한 지능형 에이전트와 유전자 조립, 세포무기 발현, 생화학적 특성화를 통합한 완전 자동화 로봇 시스템을 결합하여 단백질 피트니스 지형을 자율적으로 탐색

---

## Achievement

![Figure 1c-d](figures/fig1cd.webp)
*UCB positive와 Expected UCB 설계 전략이 표준 UCB 및 무작위 샘플링보다 3-4배 효율적으로 열 안정성 최적화 달성*

1. **완전 자동화 폐쇄 루프 시스템 구축**: 지능형 에이전트가 단백질을 설계하면 로봇 시스템이 검증하고 데이터를 에이전트에 반환하여 자동 반복하는 9시간/사이클의 완전 독립형 플랫폼 개발 (오류율 0.4°C 이내의 재현성 확보)

2. **효율적 최적화 달성**: 4개의 독립적 SAMPLE 에이전트가 모두 전체 탐색공간의 2% 미만만 평가하면서 초기 서열 대비 12°C 이상의 열 안정성 향상 달성; UCB positive 및 Expected UCB 휴리스틱이 표준 UCB 대비 3-4배의 샘플 효율성 제공

3. **다중 출력 가우시안 프로세스 모델 개발**: 활성/비활성 분류(83% 정확도)와 열 안정성 예측(r = 0.84)을 동시에 수행하여 비활성 "구멍" 영역의 탐사 오버헤드 최소화

4. **견고한 자동화 파이프라인**: Golden Gate 클로닝, 형광 DNA 검출, T7 기반 세포무기 발현, 온도 기반 활성 측정의 다층 예외 처리 메커니즘으로 높은 신뢰성 확보

---

## How

![Figure 1a](figures/fig1a.webp)
*SAMPLE 플랫폼의 설계-테스트-학습 통합 루프 아키텍처*

**지능형 에이전트 설계:**
- 베이지안 최적화를 단백질 공학에 응용하여 탐색(exploration) vs 활용(exploitation) 간의 효율적 트레이드오프 달성
- 다중 출력 가우시안 프로세스(GP) 모델로 활성/비활성 상태와 연속 함수값을 동시 모델링
- UCB positive: 활성으로 예측된 서열 중 상신뢰도 상한값(Upper Confidence Bound) 최대화 선택
- Expected UCB: UCB 점수에 활성 확률을 가중치로 곱하여 기댓값 최대화

**자동화 실험실 시스템:**
- **유전자 조립**: Golden Gate 클로닝으로 사전합성 DNA 조각 조합 (약 1시간)
- **품질 관리**: EvaGreen 형광 염료로 이중 가닥 DNA 검출 (약 1시간 PCR)
- **단백질 발현**: T7 기반 세포무기 발현 시스템 (약 3시간)
- **생화학적 특성화**: 색측정/형광 어세이로 열 안정성(T50) 측정 (약 3시간)
- **품질 보증**: 3단계 예외 처리 (DNA 확인 → 반응곡선 검증 → 배경 잡음 제거)

**조합형 서열 공간 설계:**
- DNA 조립 그래프로 자연 GH1 가족 요소, Rosetta 설계 요소, 진화 정보 기반 요소를 조합
- 제한된 DNA 조각으로부터 기하급수적 확장을 통해 1,352개의 고유한 GH1 서열 생성

---

## Originality

- **선도적 완전 자율화**: 단백질 공학 분야에서 인간 개입 없이 완전히 독립적으로 작동하는 엔드-투-엔드 설계-테스트-학습 루프 구현은 기존 반자동 시스템과 근본적으로 다름

- **혁신적 BO 휴리스틱**: 비활성 "구멍" 문제를 해결하기 위해 활성/비활성 분류기를 명시적으로 통합한 UCB positive 및 Expected UCB 방법은 단백질 공학의 독특한 도전과제를 직접 해결

- **다중 출력 GP 모델**: 이항 분류(활성/비활성)와 연속 회귀(열 안정성)를 동시에 모델링하는 접근법으로 정보 손실 최소화 및 샘플 효율성 극대화

- **포괄적 자동화 엔지니어링**: 유전자 조립부터 최종 표현형 측정까지의 모든 단계를 통합하고 다층 품질 제어를 구현한 로봇 시스템은 재현성과 신뢰성의 새로운 기준 제시

- **조합형 라이브러리 설계**: 자연, 계산 설계, 진화적 정보를 통합한 구조화된 서열 공간은 1,352개 변이체의 광범위한 탐색을 가능하게 함

---

## Limitation & Further Study

**한계:**

- **단일 단백질 가족 테스트**: 글리코사이드 하이드롤라제에서만 검증되었으므로, 다른 단백질 가족(예: 항체, 전자 전달 단백질)에서의 일반화 가능성이 미확인

- **측정 노이즈의 영향**: 4개 에이전트 간 탐색 경로의 차이가 실험적 측정 노이즈에서 비롯되었으며, 이의 정량적 특성화 및 완화 전략이 부족

- **표현형 복잡성의 제한**: 열 안정성(T50)과 같은 단일 특성만 최적화했으며, 활성, 기질 특이성, 발현 수준 등 다중 목표 최적화는 미구현

- **계산 모델의 불확실성**: 가우시안 프로세스 모델의 예측 신뢰도가 r = 0.84에 그쳤으므로, 더 큰 탐색공간에서의 성능 저하 가능성

- **확장성 고려 부족**: 2% 미만의 탐색공간 평가로 충분했으나, 훨씬 더 큰 단백질 공간(예: 모든 가능한 아미노산 조합)에서의 효율성은 미검증

**후속 연구 방향:**

- 다중 목표 최적화(활성, 안정성, 발현, 특이성 동시 개선) 알고리즘 개발로 현실적 단백질 공학 요구사항 대응

- 전이 학습 및 메타 러닝을 통해 한 단백질 가족에서의 학습을 다른 단백질로 이전하여 초기 데이터 요구량 감소

- 고차원 서열공간(예: 전체 유전체 규모)에 대한 확장 가능성 검토 및 효율적 탐색 전략 개발

- 측정 노이즈 특성화, 불확실성 정량화, 로버스트 최적화 기법 적용으로 시스템 신뢰성 향상

- 다른 단백질 가족(항체, 효소, 구조 단백질 등) 및 생물학적 시스템(대사 경로, 유전 회로)으로의 확장 실증

- 실시간 기계 학습 모델 업데이트, 분산 멀티 에이전트 조정, 동적 파라미터 자동 조정 등 고급 자동화 기법 통합

---


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.5/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4.5/5

## Related Papers

- 🔄 다른 접근: [[papers/141_Autonomous_robotic_system_with_optical_coherence_tomography/review]] — 생명과학과 의료 분야에서 각각 단백질 공학과 수술 로봇이라는 서로 다른 자율 실험실 구현을 보여준다.
- 🔗 후속 연구: [[papers/099_An_autonomous_laboratory_for_the_accelerated_synthesis_of_in/review]] — 단백질 특화 자동화를 더 넓은 화학 합성 자동화로 확장하여 포괄적인 자율 실험실 구축 방향을 제시한다.
- 🏛 기반 연구: [[papers/764_Sparks_Multi-Agent_Artificial_Intelligence_Model_Discovers_P/review]] — 자동화된 실험이 AI 기반 과학 발견의 핵심 요소임을 실증적으로 뒷받침한다.
- 🔗 후속 연구: [[papers/614_Perspective_on_utilizing_foundation_models_for_laboratory_au/review]] — 단백질 공간 자율 탐색을 위한 자율주행 실험실이 재료 과학 자동화를 생물학적 시스템으로 확장합니다.
- 🔄 다른 접근: [[papers/141_Autonomous_robotic_system_with_optical_coherence_tomography/review]] — 의료 수술과 생화학 실험이라는 서로 다른 영역에서 자율 로봇 시스템의 구현 방식을 비교한다.
- 🔗 후속 연구: [[papers/381_Genesis_Towards_the_Automation_of_Systems_Biology_Research/review]] — 자율적 단백질 공간 탐색을 위한 실험실 자동화가 Genesis의 대규모 병렬 가설 검증 시스템을 단백질 특화 영역으로 확장한 적용이다.
- 🔗 후속 연구: [[papers/118_Autobio_A_simulation_and_benchmark_for_robotic_automation_in/review]] — AutoBio의 생물 실험실 로봇 자동화 벤치마크는 단백질 공학을 위한 자율 실험실 연구의 로봇 자동화 개념을 VLA 모델 평가로 확장하여 더 포괄적인 과학 자동화 평가를 제공합니다.
- 🔗 후속 연구: [[papers/310_Embodied_Science_Closing_the_Discovery_Loop_with_Agentic_Emb/review]] — 단백질 공간 탐색을 위한 자율 연구소는 Embodied Science의 물리적 세계 상호작용 개념을 생물학적 발견으로 확장한다.
- 🔄 다른 접근: [[papers/851_Uncovering_bottlenecks_and_optimizing_scientific_lab_workflo/review]] — 제약 실험실 최적화와 단백질 공간 자율 탐색에서 실험실 자동화의 다른 응용을 보여준다.
- 🔗 후속 연구: [[papers/1126_Autonomous_platform_for_solution_processing_of_electronic_po/review]] — 단백질 공간을 자율적으로 탐색하는 실험실에서 고분자 최적화로의 확장
