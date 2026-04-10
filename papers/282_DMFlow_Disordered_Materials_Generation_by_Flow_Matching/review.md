---
title: "282_DMFlow_Disordered_Materials_Generation_by_Flow_Matching"
authors:
  - "Liming Wu"
  - "Rui Jiao"
  - "Qi Li"
  - "Mingze Li"
  - "Songyou Li"
date: "2026.02"
doi: "10.48550/arXiv.2602.04734"
arxiv: ""
score: 4.0
essence: "본 논문은 완전히 정렬된 결정체만 생성하던 기존 심화 학습 모델의 한계를 극복하기 위해, **치환 무질서(Substitutional Disorder, SD)와 위치 무질서(Positional Disorder, PD)를 모두 생성 가능한 DMFlow 프레임워크**를 제시한다. 리만 기하학적 흐름 매칭(Riemannian Flow Matching)과 구 재매개변수화를 통해 확률 심플렉스 제약을 만족하는 물리적으로 타당한 무질서 가중치를 생성한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/3D_Molecular_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wu et al._2026_DMFlow Disordered Materials Generation by Flow Matching.pdf"
---

# DMFlow: Disordered Materials Generation by Flow Matching

> **저자**: Liming Wu, Rui Jiao, Qi Li, Mingze Li, Songyou Li, Shifeng Jin, Wenbing Huang | **날짜**: 2026-02-04 | **DOI**: [10.48550/arXiv.2602.04734](https://doi.org/10.48550/arXiv.2602.04734)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: 완전 정렬 결정체 vs. 무질서 결정체. 화살표는 슈퍼셀 축소, BL/BR은 좌측/우측 위치를 표시*

본 논문은 완전히 정렬된 결정체만 생성하던 기존 심화 학습 모델의 한계를 극복하기 위해, **치환 무질서(Substitutional Disorder, SD)와 위치 무질서(Positional Disorder, PD)를 모두 생성 가능한 DMFlow 프레임워크**를 제시한다. 리만 기하학적 흐름 매칭(Riemannian Flow Matching)과 구 재매개변수화를 통해 확률 심플렉스 제약을 만족하는 물리적으로 타당한 무질서 가중치를 생성한다.

## Motivation

- **Known**: 
  - 기존 심화 생성 모델(VAE, 확산 모델, 흐름 기반 모델)은 완벽하게 정렬된 결정체만을 다룸
  - 고엔트로피 합금, 고체 전해질, 초전도체 등 무질서 결정체는 기술적으로 중요하나 생성 모델의 대상이 아님

- **Gap**: 
  - 기존 모델은 확정적인 원자 배치를 가정하므로, 확률적 점유율(SD) 및 위치 편차(PD)를 표현할 통일된 방법이 없음
  - 무질서 가중치는 심플렉스 제약(합=1, 모두≥0)을 만족해야 하는데, 기존 생성 모델은 유클리드 공간에서만 작동

- **Why**: 
  - 무질서 결정체의 확률적 특성을 제대로 모델링하면 신물질 발견 가속화 가능
  - 공개 벤치마크 부재로 연구 기반 부족

- **Approach**: 
  - 각 결정학적 위치를 중심으로 통일된 표현 개발: (si, fi, wi, f'i) 튜플로 SD와 PD 동시 표현
  - 리만 흐름 매칭으로 심플렉스 기하학을 존중하는 생성 경로 학습
  - 물리 대칭성을 인코딩한 맞춤형 그래프 신경망(GNN) 설계

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: DMFlow의 전체 프레임워크. (a) 선행 분포에서 목표 데이터 분포로의 흐름 매칭 과정, (b) 각 다양체의 기하학적 표현, (c) 속도 예측 네트워크의 GNN 아키텍처*

1. **통일된 표현 체계**: 
   - 완전 정렬 결정체, SD, PD, 혼합 구조를 모두 수용하는 단일 프레임워크 실현
   - 식 (1): C := (L, S, F, W, F') 통합 표현으로 격자, 분수좌표, 무질서 가중치, 이차 위치를 동시 생성

2. **리만 흐름 매칭 혁신**:
   - 구 재매개변수화를 통해 심플렉스 제약 만족
   - 심플렉스에서 고차원 구면으로의 변환으로 수치 안정성 확보
   - 기존 직접 심플렉스 구현의 조건수(conditioning) 문제 해결

3. **벤치마크 및 실증 성과**:
   - 결정학 공개 데이터베이스(COD)에서 SD/PD/SPD 혼합 구조 포함 최초 공개 벤치마크 구축
   - 결정 구조 예측(CSP) 및 신규 생성(DNG) 작업에서 기존 기준 모델 대비 유의한 성능 향상

## How

![Figure 3](figures/fig3.webp)
*그림 3: 앙상블 투표(Ensemble Voting) 절차를 통한 이산화*

- **통일된 표현 설계**:
  - SD: 점유 벡터 si ∈ Δ^(D-1)로 각 원소 종 k의 확률 si,k 표현
  - PD: 위치 벡터 wi ∈ Δ^1과 이차 분수좌표 f'i로 이진 위치 무질서 모델링
  - 일반화된 튜플 (si, fi, wi, f'i)로 확장

- **조건부 흐름 매칭(CFM) 적용**:
  - 격자 L: 유클리드 공간 ℝ^(3×3)
  - 분수좌표 F: 토러스 [0,1)³ 위의 주기 불변성
  - 무질서 가중치 S, W: 심플렉스에서 구면으로의 매니폴드
  - 각 성분의 기하학적 특성에 맞춘 측지선(geodesic) 기반 경로 설계

- **맞춤형 GNN 벡터장 학습**:
  - 메시지 계산(ϕmsg): 다중 상호작용으로 PD의 복잡한 위치 관계 포착
  - 특성 업데이트(ϕfeat): 대칭성 제약 유지
  - 출력 헤드(ϕout): 격자, 좌표, SD, PD 성분 동시 예측
  - 주기 불변성(periodic invariance) 명시적 인코딩

- **2단계 이산화 절차**:
  - 1단계: 정렬된 위치 식별 (wi,0 > threshold)
  - 2단계: 무질서 위치에 대한 앙상블 투표로 다중-핫(multi-hot) 할당 전환

## Originality

- **첫 번째 통합 생성 모델**: 
  - 기존에는 SD(Petersen et al., 2025의 VAE) 또는 성질 예측만 가능했으나, SD와 PD를 동시에 다루는 첫 생성 프레임워크

- **리만 흐름 매칭의 창의적 확장**:
  - 심플렉스라는 새로운 매니폴드에 대한 Riemannian CFM 구현
  - 구 재매개변수화로 수치 안정성 확보하는 기술 혁신

- **물리 제약 명시적 인코딩**:
  - 주기 불변성, 대칭성, 무질서 가중치 제약을 아키텍처 수준에서 구현
  - 일반적인 black-box 신경망과 달리 물리 원리 직접 반영

- **벤치마크 기여**:
  - 무질서 결정체 생성의 첫 공개 평가 데이터셋
  - CSP/DNG 두 실용적 작업에 초점

## Limitation & Further Study

- **이진 위치 무질서(Binary PD) 제한**:
  - 현재는 각 위치가 최대 2개 위치만 차지 가능하도록 제한 (COD 데이터 중 이진 PD 주로 존재)
  - 3개 이상 위치 무질서는 자연 확장 가능하지만 미구현

- **데이터셋 편향**:
  - COD 기반 벤치마크는 실험적으로 검증된 구조로 치우쳐 있을 가능성
  - 합성된 고엔트로피 합금 등 다양한 무질서 재료 포함 필요

- **생성된 구조의 안정성 검증**:
  - 논문에서는 구조 생성만 다루며, 예측 구조의 열역학/동역학 안정성 검증은 제한적
  - 추가 DFT 계산이나 분자동역학 시뮬레이션과의 결합 필요

- **확장성**:
  - 대규모 초셀(supercell)이나 복잡한 다중 서브래티스 무질서에 대한 확장성 미검증
  - 계산 복잡도 분석 및 최적화 여지

- **후속 연구 방향**:
  - 다중 위치 무질서, 고차 무질서 타입 포함 일반화
  - 무질서 정도 제어 생성 (조건부 생성으로 원하는 무질서 수준 조정)
  - 물성 예측 모델과의 연계로 설계-합성 파이프라인 완성

## Evaluation

- **Novelty**: 4.5/5
  - 무질서 결정체 생성은 완전히 미개척 분야로, 통합 표현과 리만 흐름 매칭 적용은 창의적
  - 다만 흐름 매칭 자체는 기존 기술이며, 이진 PD 제약은 일반성 감소

- **Technical Soundness**: 4/5
  - 수학적 기초(리만 기하학, CFM) 견고함
  - 구 재매개변수화 기술 혁신적이나 자세한 수치 안정성 분석 부족
  - 2단계 이산화 절차의 최적성 미증명

- **Significance**: 4/5
  - 무질서 재료 생성이 기술적으로 중요한 미개척 영역
  - 첫 공개 벤치마크 구축으로 커뮤니티 기여 큼
  - 실제 신물질 발견과의 연결 가능성은 아직 검증 초기 단계

- **Clarity**: 4/5
  - 논문 구조와 설명이 대체로 명확함
  - 통일 표현과 기하학적 직관이 잘 설명됨
  - 일부 GNN 아키텍처 세부사항(메시지 계산 식)이 본문에서 생략되어 부록 의존

- **Overall**: 4/5

**총평**: DMFlow는 무질서 결정체 생성이라는 중요하면서도 미개척된 문제를 처음 체계적으로 해결한 논문으로, 리만 흐름 매칭과 통합 표현이라는 기술적 혁신을 통해 높은 완성도를 보인다. 다만 이진 PD 제약, 생성 구조의 물리적 검증 부족, 대규모 구조에 대한 확장성 미검증 등이 향후 개선 과제이며, 실제 신물질 발견으로의 영향력은 추가 실증이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/383_Geometry_Informed_Tokenization_of_Molecules_for_Language_Mod/review]] — 언어모델 분자 생성과 무질서 재료 생성의 다른 생성 모델 접근법
- 🏛 기반 연구: [[papers/555_Molgan_An_implicit_generative_model_for_small_molecular_grap/review]] — 소분자용 암시적 생성모델 MolGAN이 무질서 재료 생성의 기반 제공
- 🔗 후속 연구: [[papers/269_Derivative-Free_Guidance_in_Continuous_and_Discrete_Diffusio/review]] — 연속 이산 확산의 미분 프리 가이던스에서 무질서 재료로의 확장
- 🧪 응용 사례: [[papers/446_Iterative_Distillation_for_Reward-Guided_Fine-Tuning_of_Diff/review]] — 확산 모델의 보상 가이드 미세조정을 무질서 재료 생성에 적용
- 🏛 기반 연구: [[papers/555_Molgan_An_implicit_generative_model_for_small_molecular_grap/review]] — DMFlow의 무질서 물질 생성 방법론이 MolGAN의 분자 그래프 생성 알고리즘 개발에 기초가 됨
- 🔄 다른 접근: [[papers/1099_Generative_Inversion_of_Spectroscopic_Data_for_Amorphous_Str/review]] — 비정질 재료 구조 생성에서 흐름 매칭과 확산 모델의 다른 접근법
