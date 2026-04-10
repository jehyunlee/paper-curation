---
title: "258_Deep_active_learning_based_experimental_design_to_uncover_sy"
authors:
  - "Haonan Zhu"
  - "Mary Silva"
  - "Jose Cadena"
  - "Braden C. Soper"
  - "Michal Lisicki"
date: "2025"
doi: "미제공"
arxiv: ""
score: 4.0
essence: "본 논문은 HIV 감염에서 숙주 유전자 쌍의 시너지 상호작용을 효율적으로 발견하기 위해 생물학적 지식 그래프(SPOKE)와 딥러닝 기반 능동학습(Deep Active Learning, DeepAL)을 통합한 프레임워크를 제시한다. 356개 유전자의 상호작용 공간(356×356 행렬)에서 실험 비용을 최소화하면서 효과적인 이중 녹다운(double knockdown) 쌍을 발견한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Agent_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhu et al._2025_Deep active learning based experimental design to uncover synergistic genetic interactions for host.pdf"
---

# Deep active learning based experimental design to uncover synergistic genetic interactions for host targeted therapeutics

> **저자**: Haonan Zhu, Mary Silva, Jose Cadena, Braden C. Soper, Michal Lisicki, Braian Peetoom, Sergio Baranzini, Shivshankar Sundaram, P. Ray, J. Drocco | **날짜**: 2025 | **DOI**: [미제공](https://doi.org/)

---

## Essence

![Figure 1](figures/fig1.webp)
*Deep Active Learning 프레임워크의 전체 흐름: SPOKE 지식 그래프에서 생성된 유전자 임베딩을 초기화하고, 신경망을 통해 상호작용을 예측하며, 획득함수 기반 능동학습 루프로 다음 탐사 대상 유전자 쌍을 선정*

본 논문은 HIV 감염에서 숙주 유전자 쌍의 시너지 상호작용을 효율적으로 발견하기 위해 생물학적 지식 그래프(SPOKE)와 딥러닝 기반 능동학습(Deep Active Learning, DeepAL)을 통합한 프레임워크를 제시한다. 356개 유전자의 상호작용 공간(356×356 행렬)에서 실험 비용을 최소화하면서 효과적인 이중 녹다운(double knockdown) 쌍을 발견한다.

## Motivation

- **Known**: 
  - 고처리량 기술이 숙주-바이러스 상호작용 연구를 가능하게 했으나, 유전자 쌍의 시너지 상호작용 검증은 여전히 느리고 노동집약적임
  - 단일 유전자 녹다운(single-gene knockdown)에 대한 능동학습 방법들이 존재하나, 이중 녹다운(double-knockdown) 데이터는 소규모(50×50 이하)에 국한됨
  - 바이러스는 단일 표적에 대해 빠르게 내성을 발달시키므로, 조합 치료가 필수적

- **Gap**: 
  - 기존 연구들은 단일 녹다운 실험 데이터에만 검증되었거나 극도로 제한된 이중 녹다운 탐색 공간(160/100,576 쌍)에서만 작동
  - 대규모 이중 녹다운 데이터(356×356 행렬)에 대한 능동학습 프레임워크 부재
  - 기존 그래프 학습 접근(ITERPER)은 동질 그래프(homogeneous graph)만 지원하고, 단순 가우시안 노이즈 모델로 불확실성을 추정

- **Why**: 
  - 조합 치료 표적 발견 시간/비용 절감이 항바이러스 치료 개발의 핵심
  - 호스트 표적 치료는 바이러스의 선택 압력을 받지 않아 장기 효과 가능성 높음

- **Approach**: 
  - 이질 지식 그래프(heterogeneous knowledge graph) SPOKE를 활용한 R-GCN 기반 표현 학습
  - 앙상블(ensemble) 방법을 통한 불확실성 정량화
  - 탐색-활용(exploration-exploitation) 균형을 갖춘 능동학습 루프

## Achievement

![Figure 2](figures/fig2.webp)
*다양한 획득함수 전략 비교: 제안된 방법이 감염율(viral load) 최소화 측면에서 우월함*

1. **획기적 규모의 실험 데이터 처리**: 356개 유전자의 이중 녹다운 상호작용 매트릭스(356×356)에 대해 처음으로 의미 있는 결과를 달성한 능동학습 방법 제시

2. **통합 프레임워크의 유효성**: 
   - R-GCN 기반 임베딩이 자체 감독 학습(self-supervised learning)으로 초기화되어 지식 그래프의 위상 정보 활용
   - 앙상블 기반 불확실성 정량화가 단순 가우시안 모델보다 딥러닝 모델의 불확실성을 더 정확히 포착

3. **생물학적 해석가능성**: 경로 분석(pathway analysis)을 통해 알고리즘이 선택한 유전자 쌍의 생물학적 의미 검증

## How

![Figure 3](figures/fig3.webp)
*제안된 방법의 주요 컴포넌트에 대한 제거 연구(ablation study): 각 구성 요소의 기여도 검증*

- **자체 감독 표현 학습 (Self-Supervised Representation Learning)**:
  - SPOKE 지식 그래프에서 목표 유전자를 시작점으로 random walk (깊이=5, 경로=5)로 부분그래프 추출
  - R-GCN(Relational Graph Convolutional Network)을 통해 다양한 에지 타입(유전자-단백질, 단백질-단백질, 유전자-생물학적 과정 등)을 처리하여 유전자 임베딩 생성

- **엣지 예측 모델 (Edge Prediction Model)**:
  - DistMulti 기반 쌍방향 상호작용 모델: 두 유전자의 임베딩(x_i, x_j)을 입력으로 하여 상호작용 강도 예측
  - Huber 손실함수를 통한 robust 회귀 수행

- **앙상블 기반 불확실성 정량화 (Ensemble-Based Uncertainty Quantification)**:
  - M개의 동일 구조 모델을 서로 다른 초기값으로 독립 학습
  - 예측값의 표준편차를 불확실성 측도로 사용하여 모델 불확실성 포착

- **능동학습 획득함수 (Acquisition Function)**:
  - 탐색(exploration): 예측 불확실성이 높은 쌍 선정
  - 활용(exploitation): 예측 바이러스 감염율이 낮은(효과적인) 쌍 선정
  - 여러 획득 전략 비교: Upper Confidence Bound (UCB), Thompson Sampling, Expected Improvement 등

- **반복 최적화**:
  - T라운드에 걸쳐 N개 쌍씩 선택-실험-학습 반복
  - 매 라운드마다 R-GCN과 회귀 모델을 관측된 데이터로 재학습하여 표현 개선

## Originality

- **이질 지식 그래프의 첫 적용**: HIV 유전자 상호작용 발견에 SPOKE의 다중 에지 타입 정보를 활용한 첫 시도
  
- **대규모 이중 녹다운 스크린 최적화**: 기존 50×50 또는 소수 쌍 레벨의 연구에서 356×356 규모로 확장

- **앙상블 불확실성 정량화**: 딥러닝 기반 능동학습에서 확률론적 불확실성을 더 효과적으로 포착하는 방법론 적용

- **생물학적 해석성**: 경로 분석을 통해 머신러닝 선택사항의 생물학적 근거 제시

## Limitation & Further Study

- **지식 그래프 의존성**: SPOKE의 완성도와 정확성에 의존; 누락되거나 잘못된 상호작용 정보는 임베딩 품질 저하
  
- **계산 복잡도 미분석**: 356개 노드 규모에서 R-GCN 학습 비용 및 확장성에 대한 명시적 논의 부족

- **실험 검증 한계**: 논문이 학술대회 절차(GLBIO 2025)를 위한 초기 결과로, 독립적 생물 실험 검증 미기재

- **후속 연구 방향**:
  - 다른 바이러스(COVID-19, 인플루엔자 등) 및 질병 시스템으로 프레임워크 확장
  - 실험실에서 선정된 상위 유전자 쌍의 기능 검증
  - 더욱 복잡한 다중 유전자(3-way 이상) 상호작용 탐색 방법론 개발
  - 동적 지식 그래프 업데이트 메커니즘 통합

## Evaluation

- **Novelty**: 4.5/5
  - 대규모 이중 녹다운 데이터에 능동학습 적용한 첫 사례
  - 이질 지식 그래프-기반 표현학습 접근은 신선하나, 개별 기술(R-GCN, 앙상블)은 기존 방법론

- **Technical Soundness**: 4/5
  - 방법론 구성이 논리적이고 알고리즘 기술이 명확함
  - 제거 연구(ablation study)로 주요 컴포넌트 기여도 검증
  - 다만 계산 복잡도 분석, 하이퍼파라미터 선택 근거, 통계적 유의성 검증 부족

- **Significance**: 4/5
  - 숙주 표적 치료 개발에 실질적 기여 가능성 높음
  - 대규모 유전자 상호작용 스크린 자동화는 산업적 가치 높음
  - 다만 실제 생물 실험 검증 전이므로 임상 영향은 아직 미지수

- **Clarity**: 3.5/5
  - 전체 프레임워크 설명이 체계적이고 Figure 1이 직관적
  - 수학 표기법이 명확하나, 일부 기술 세부사항(예: random walk 파라미터 선택 근거) 설명 부족
  - 논문 길이 제약(8페이지)으로 인한 실험 상세 정보 한계

- **Overall**: 4/5

**총평**: 본 논문은 생물학적 지식 그래프와 딥러닝 능동학습을 효과적으로 통합하여 대규모 유전자 상호작용 공간을 효율적으로 탐색하는 실용적이고 혁신적인 프레임워크를 제시한다. 특히 356×356 규모의 이중 녹다운 데이터 처리는 이 분야에서 획기적이며, 경로 분석을 통한 생물학적 해석가능성도 강점이다. 다만 실제 실험실 검증, 계산 효율성 분석, 그리고 다양한 질병 시스템에의 일반화 가능성에 대한 추가 연구가 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/118_Autobio_A_simulation_and_benchmark_for_robotic_automation_in/review]] — 생물학적 상호작용 발견에서 능동학습 기반과 로봇 자동화 기반 접근법을 비교할 수 있습니다.
- 🔗 후속 연구: [[papers/346_Foundation-Model_Surrogates_Enable_Data-Efficient_Active_Lea/review]] — 기초 모델 기반 대리 모델이 HIV 감염 유전자 상호작용 발견에서 능동학습을 더욱 효율화할 수 있습니다.
- 🏛 기반 연구: [[papers/788_Targeted_materials_discovery_using_Bayesian_algorithm_execut/review]] — 베이지안 알고리즘 실행을 통한 타겟 재료 발견이 생물학적 상호작용 탐색의 방법론적 기반을 제공합니다.
