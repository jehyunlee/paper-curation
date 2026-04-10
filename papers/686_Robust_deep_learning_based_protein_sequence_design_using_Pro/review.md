---
title: "686_Robust_deep_learning_based_protein_sequence_design_using_Pro"
authors:
  - "J. Dauparas"
  - "I. Anishchenko"
  - "N. Bennett"
  - "H. Bai"
  - "R. Ragotte"
date: "2022"
doi: "10.1126/science.add2187"
arxiv: ""
score: 4.5
essence: ""
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Protein-Drug_Design_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Dauparas et al._2022_Robust deep learning based protein sequence design using ProteinMPNN.pdf"
---

# Robust deep learning based protein sequence design using ProteinMPNN

> **저자**: J. Dauparas, I. Anishchenko, N. Bennett, H. Bai, R. Ragotte | **날짜**: 2022 | **DOI**: [10.1126/science.add2187](https://doi.org/10.1126/science.add2187)

---

## Essence

![Figure 1](figures/fig1.webp) *ProteinMPNN 아키텍처: 메시지 패싱 신경망(MPNN) 기반의 순서-비의존적 자가회귀 모델로, 다중 체인 및 대칭성을 고려한 위치 결합 설계 가능*

**깊은 신경망 기반 단백질 서열 설계 방법 ProteinMPNN을 개발하여, 기존의 물리 기반 방법(Rosetta)보다 우수한 성능을 보이며 다양한 단백질 설계 문제에 광범위하게 적용 가능함을 입증했다.**

## Motivation

- **Known**: 
  - 깊은 학습이 단백질 구조 예측을 혁신했으나(AlphaFold), 대부분의 실험적으로 검증된 드노보(de novo) 단백질 설계는 Rosetta 같은 물리 기반 접근법으로 생성됨
  - 기존 깊은 학습 서열 설계 방법들은 단일 단백질 모노머에만 제한적이고 실험적 검증 부족

- **Gap**: 
  - 단백질 설계의 광범위한 현실적 문제(올리머, 나노입자, 단백질-단백질 인터페이스)를 해결할 수 있는 통합적 깊은 학습 방법 부재
  - 설계된 서열이 목표 구조를 견고하게 인코딩하는지 검증하는 체계적 접근 부족

- **Why**: 
  - 단백질 설계는 매우 넓은 서열 공간에서 주어진 백본 구조에 폴딩될 최적 서열을 찾는 문제로, 물리 기반 방법의 계산 비용과 정확도 제약을 극복 필요
  - 실제 응용(불완전한 백본 기하학, 구조 예측 기반 설계)에서 더 견고한 모델 필요

- **Approach**: 
  - 메시지 패싱 신경망(MPNN)을 기반으로 순서-비의존적(order-agnostic) 자가회귀 모델로 확장
  - 백본 노이즈 추가 학습, 다중 체인 및 대칭성 인식 설계, 논리(logit) 평균화를 통한 멀티-상태 설계 지원

## Achievement

![Figure 2](figures/fig2.webp) *ProteinMPNN의 전산 평가: (A) Rosetta 대비 월등한 서열 복구율(52.4% vs 32.9%), (B) 모노머(52%), 호모머(55%), 헤테로머(51%) 중위 서열 복구율, (C) 백본 노이즈 추가 학습의 영향, (E) 단일 서열 AlphaFold 예측에서 ProteinMPNN 서열의 우수한 구조 부호화*

1. **높은 서열 복구율**: 네이티브 단백질 백본에서 52.4% 서열 복구율로 Rosetta(32.9%)를 60% 이상 능가하며, 단백질 핵심에서 표면까지 모든 영역에서 일관되게 우수한 성능

2. **광범위한 적용성**: 
   - 모노머, 호모올리머, 헤테로머에 일관되게 높은 성능(51-55% 중위 복구율)
   - 순서-비의존적 디코딩으로 부분 고정 설계 가능(예: 리간드 결합 영역 고정)
   - 대칭성 제약 및 멀티-상태 설계 지원으로 대칭 단백질, 반복 단백질 설계 가능

3. **구조 견고성 향상**: 백본 노이즈(std=0.02Å) 추가 학습으로 AlphaFold 예측 구조에서 서열 복구율 증대, ProteinMPNN 설계 서열이 단일 서열 AlphaFold 예측에서 원본 네이티브 서열보다 훨씬 정확하게 목표 구조 채택

4. **계산 효율성**: 100개 잔기당 1.2초(ProteinMPNN) vs 4.3분(Rosetta) - 약 200배 빠른 속도

## How

![Figure 1](figures/fig1.webp) *ProteinMPNN 모델 아키텍처의 주요 개선 사항*

**아키텍처 개선**:
- 입력 특징: Cα-Cα 거리, 상대 방향(relative orientation), 백본 이면각에서 **N, Cα, C, O 및 가상 Cβ 원자 간 거리**로 확장 (41.2% → 49.0% 복구율)
- 노드 업데이트 외 **엣지 업데이트 추가** (49.0% → 50.5%)
- 국소 연결 그래프 신경망: 32-48개 최근접 Cα 이웃으로 포화 (구조 예측과 달리 백본 국소성이 중요)

**순서-비의존적 자가회귀 모델**:
- 고정 N→C 터미널 디코딩 대신 **모든 순열에서 무작위 샘플링**
- 이는 부분 서열 고정 설계(예: 알려진 리간드 결합 영역) 및 다중 체인 설계 가능하게 함

**다중 체인 및 대칭성 인식**:
- 체인 순서 등변성(equivariance): 상대 위치 인코딩 ±32 잔기로 제한 + 체인 간/체인 내 이진 특징
- **위치 결합 설계**: 대응 위치(예: C2 호모이량체의 A1/B1)에 대해 결합된 로짓 생성 후 정규화된 확률분포 구성
- **멀티-상태 설계**: 여러 상태에서 예측된 로짓 평균화 또는 선형결합으로 양성/음성 서열 설계 가능

**학습 설정**:
- PDB 고해상도(>3.5Å) X-선 결정학/극저온전자현미경(cryo-EM) 구조: 25,361개 클러스터(30% 서열 동일성 기준)
- **백본 노이즈 학습**: 불완전한 구조 모델(AlphaFold 등)에 대한 견고성 증진
- 높은 온도(higher temperature)에서의 확률적 추론으로 설계된 서열의 구조 부호화 강화

## Originality

- **메시지 패싱 신경망의 혁신적 확장**: 기존 MPNN 기반 방법을 순서-비의존적 자가회귀로 전환하여 다양한 제약 조건(부분 고정, 대칭성, 멀티-상태) 통일적으로 처리 가능하게 함

- **견고성 중심의 설계 철학**: 네이티브 서열 복구율 최대화 대신 **백본 노이즈 학습으로 구조 예측 알고리즘에서의 실제 성능 최적화** - 실용적 관점의 전환

- **위치 결합(positional coupling) 메커니즘**: 로짓 평균화를 통해 대칭 올리머, 대칭 단백질, 멀티-상태 설계를 우아하고 확장 가능한 방식으로 구현

- **국소 그래프 신경망의 정당화**: 구조-서열 매핑이 국소 기하학에만 의존하므로 전역 정보가 필수적인 구조 예측과 달리 국소 연결 네트워크로 충분함을 실증

- **광범위한 실험적 검증 약속**: Rosetta/AlphaFold 실패 사례 구제, X-선 결정학, 극저온전자현미경 및 기능 연구로 다각적 검증 체계 제시

## Limitation & Further Study

**한계**:
- **서열 복구율의 절대값**: 52% 평균 복구율은 여전히 50% 이상을 설계 배제(misses)하므로, 실제 설계 성공률과의 상관관계 명확화 필요
- **표면 잔기의 낮은 복구율**: 표면에서 35% 정도로 낮아, 상호작용 특이성이 필요한 표면 설계에 한계
- **단백질 크기 제한**: 10,000 잔기 이하로 제한되어 초대형 복합체 설계 불가능
- **백본 노이즈 최적값**: 어느 정도의 노이즈가 최적인지에 대한 체계적 분석 부족

**후속 연구 방향**:
- 표면 잔기 설계 개선을 위한 상호작용 특이성 모델링(예: 특정 리간드 결합 정보 통합)
- 더 큰 규모 단백질 복합체 설계로 확장
- 효소 기능 설계 등 구체적 기능 최적화를 위한 목적함수 개발
- 실험적 고처리량 검증을 통한 예측 모델의 신뢰도 정량화


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.5/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4.5/5

**총평**: ProteinMPNN은 깊은 학습 기반 단백질 설계에서 기존 물리 기반 방법의 한계를 혁신적으로 극복한 작업으로, 순서-비의존적 자가회귀와 견고성 중심의 학습 철학이 핵심이며, 모노머부터 올리머, 나노입자까지 광범위한 실용적 적용 가능성을 갖춘 분야 선도적 연구다.

## Related Papers

- 🔗 후속 연구: [[papers/171_Boltz-1_Democratizing_Biomolecular_Interaction_Modeling/review]] — 구조 예측과 서열 설계를 결합하여 통합적 단백질 엔지니어링 파이프라인을 구성한다.
- 🧪 응용 사례: [[papers/1129_SARS-CoV-2_simulations_go_exascale_to_predict_dramatic_spike/review]] — 단백질 서열 설계 기법을 바이러스 단백질 구조 연구에 적용할 수 있다.
- 🔗 후속 연구: [[papers/638_ProtAgents_protein_discovery_via_large_language_model_multi-/review]] — 단백질 설계를 LLM 기반 다중 에이전트 시스템으로 확장한다.
- 🔗 후속 연구: [[papers/1060_Accurate_prediction_of_protein_structures_and_interactions_u/review]] — 단백질 구조 예측을 견고한 딥러닝 기반 서열 설계로 발전시킨 연구
- 🔗 후속 연구: [[papers/256_De_novo_design_of_protein_structure_and_function_with_RFdiff/review]] — 강건한 단백질 서열 설계를 목표 동역학을 갖는 구조 설계로 확장할 수 있다
- 🔗 후속 연구: [[papers/171_Boltz-1_Democratizing_Biomolecular_Interaction_Modeling/review]] — 단백질 구조 예측을 서열 설계와 결합하여 통합적 단백질 엔지니어링을 가능하게 한다.
- 🔗 후속 연구: [[papers/634_PRIME_A_Multi-Agent_Environment_for_Orchestrating_Dynamic_Co/review]] — PRIME의 동적 계산 워크플로우 조율 기법을 견고한 딥러닝 기반 단백질 서열 설계로 확장하여 더 신뢰할 수 있는 단백질 공학 시스템을 구축할 수 있다.
- 🔗 후속 연구: [[papers/1129_SARS-CoV-2_simulations_go_exascale_to_predict_dramatic_spike/review]] — ProteinMPNN의 서열 설계 기법을 스파이크 단백질 동역학 연구에 적용할 수 있다.
