# DMFlow: Disordered Materials Generation by Flow Matching

> **저자**: Liming Wu, Rui Jiao, Qi Li, Mingze Li, Songyou Li, Shifeng Jin, Wenbing Huang | **날짜**: 2026-02-04 | **Repository**: arXiv | **DOI**: 10.48550/arXiv.2602.04734

---

## Essence

DMFlow는 비정렬(disordered) 결정 구조를 생성하기 위해 설계된 최초의 심층 생성 프레임워크이다. 치환 무질서(Substitutional Disorder, SD)와 위치 무질서(Positional Disorder, PD)를 통합적으로 표현하는 방식을 제안하고, simplex 제약조건을 만족시키기 위해 구면 재매개변수화(spherical reparameterization)를 활용한 Riemannian flow matching을 적용하여, Crystal Structure Prediction(CSP)과 De Novo Generation(DNG) 모두에서 기존 ordered crystal 생성 모델 대비 유의미한 성능 향상을 달성했다.

## Motivation

- **알려진 것**: 심층 생성 모델(DiffCSP, FlowMM, MatterGen 등)이 ordered crystal 생성에서 큰 성과를 거두었으나, 이들은 완벽한 주기성을 전제로 설계됨
- **Gap**: 고엔트로피 합금, 고체 전해질, 초전도체 등 기술적으로 중요한 비정렬 결정 재료(disordered crystals)를 다루는 생성 모델이 부재하며, 공개 벤치마크도 존재하지 않음
- **왜 중요한가**: 비정렬 결정은 확률적 사이트 점유(probabilistic site occupancy)와 위치 편차를 본질적으로 포함하여, 기존 one-hot/deterministic 표현으로는 생성이 불가능
- **접근법**: 정렬/SD/PD 결정을 하나의 튜플 (si, fi, wi, f'i)로 통합 표현하고, disorder weight에 대해 simplex 위의 Riemannian flow matching을 적용

## Achievement

1. **통합 표현 체계**: 정렬, SD, PD, 혼합(SPD) 결정을 단일 프레임워크로 표현 가능한 최초의 통합 표현(unified representation) 제안
2. **CSP 성능**: COD-SPD-50에서 Match Rate 45.87% (FlowMM-Prob 44.00% 대비 향상), RMSE 0.0725 (FlowMM-Prob 0.0887 대비 18% 개선)
3. **DNG 성능**: COD-SD-20에서 구조 유효성(structural validity) 88.14%, 조성 유효성(compositional validity) 69.06% 달성 -- L1-Norm 대비 조성 유효성 2.3배 향상
4. **데이터 증강 효과**: 정렬 결정(MP-20) 데이터 추가 시 CSP Match Rate 70.57% → 77.40%, RMSE 47% 감소 (0.0738 → 0.0391)
5. **벤치마크 구축**: COD 기반 SD/PD/SPD 벤치마크 4종(COD-SD-20/50, COD-SPD-20/50) 최초 공개

## How

- **데이터**: Crystallography Open Database(COD)에서 disorder annotation이 있는 구조를 파싱하여 3~50 원자 단위셀 필터링. COD-SD-20(5,701), COD-SD-50(9,096), COD-SPD-20(6,127), COD-SPD-50(11,746) 구조
- **통합 표현**: 각 결정학적 사이트 i를 (si, fi, wi, f'i) 튜플로 표현. si∈Δ^(D-1)은 치환 벡터, fi는 주 분율 좌표, wi∈Δ^1은 위치 벡터, f'i는 이차 위치 좌표
- **Flow Matching**: 격자(lattice)와 분율 좌표는 FlowMM 방식(Euclidean/torus), disorder weight는 Fisher-Rao metric 기반 simplex → 구면 재매개변수화(π(μ)=√μ)를 통해 SD^(D-1)_+ 위에서 Riemannian flow matching 수행
- **GNN 아키텍처**: 연속 disorder weight를 초기 feature로 사용(φ_prob), PD 사이트 간 모든 위치 조합(a,b∈{0,1})에 대해 joint occupancy probability wi,a·wj,b로 가중된 거리/방향 edge embedding 생성 (multiple interaction)
- **이산화(Discretization)**: 2단계 -- (1) 최대/차순위 확률 비율로 정렬 사이트 탐지, (2) 5가지 heuristic(Top-k, 고정 임계값, 백분위, 적응 임계값, 엔트로피 기반)의 앙상블 투표로 비정렬 사이트의 multi-hot 원자 할당
- **학습**: 전체 loss = λ_l·L_l + λ_F·L_F + λ_F'·L_F' + λ_S·L_S + λ_W·L_W, CSP에서는 조성이 주어지므로 λ_S=λ_W=0

## Originality

- **비정렬 결정 생성의 최초 프레임워크**: 기존 생성 모델이 완전히 무시해온 disordered crystal을 체계적으로 다루는 최초의 연구
- **Simplex 위 Riemannian Flow Matching**: Fisher-Rao metric의 경계 발산 문제를 구면 재매개변수화로 우회하여, 확률 simplex 제약을 자연스럽게 만족시키는 생성 경로 설계
- **Multiple Interaction Edge Embedding**: PD 사이트 간 모든 위치 조합의 joint occupancy를 가중치로 사용하는 새로운 기하학적 edge feature 설계
- **앙상블 투표 이산화**: 5가지 상보적 heuristic의 다수결 투표로 단일 heuristic의 편향을 완화하는 robust한 이산화 전략
- **통합 표현을 통한 cross-domain 학습**: 정렬 결정 데이터로 비정렬 모델을 증강할 수 있는 표현의 유연성

## Limitation & Further Study

### 저자들이 언급한 한계

- 위치 무질서(PD)를 이진(binary) 경우로 제한하여, 3개 이상의 위치를 갖는 고차 PD는 부록에서 확장 가능성만 언급
- 기존 ordered crystal 생성 모델과의 직접 비교가 불가능하여, 적응(adaptation)된 baseline만 사용
- 소스 코드를 출판 시 공개 예정이나, 현재 미공개 상태

### 자체판단 아쉬운 점

- 벤치마크가 COD 단일 소스에서만 구축되어, Materials Project나 ICSD 등 다른 데이터베이스의 비정렬 구조와의 교차 검증이 부족
- DNG에서 생성된 비정렬 구조의 열역학적 안정성(stability) 검증이 없으며, DFT 계산을 통한 실질적 물성 평가가 수행되지 않음
- 조성 유효성(compositional validity)이 최대 69%대로, 실용적 재료 설계에는 아직 부족한 수준
- SD와 PD의 상호작용(correlation)을 명시적으로 모델링하지 않으며, 각각의 flow를 독립적으로 학습
- Space group 대칭 제약조건이 생성 과정에 반영되지 않아, 물리적으로 비현실적인 구조가 생성될 가능성

### 후속 연구

- 고차 PD(3개 이상 위치)로의 확장 및 동적 무질서(dynamic disorder) 모델링
- DFT/MLIP 기반 안정성 검증을 포함한 closed-loop 재료 발견 파이프라인 구축
- Space group constrained generation과의 통합
- 대규모 데이터셋(ICSD, Materials Project disorder entries)으로의 확장 및 전이 학습
- 비정렬 재료의 특정 물성(이온 전도도, 초전도 전이온도 등) 조건부 생성

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 5/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 기존 심층 생성 모델이 전혀 다루지 못했던 비정렬 결정 생성이라는 새로운 문제를 정의하고, simplex 위 Riemannian flow matching이라는 수학적으로 우아한 해법을 제시한 선구적 연구이다. 벤치마크 구축과 통합 표현의 설계가 돋보이며, 후속 연구의 기반을 마련했다는 점에서 의의가 크다. 다만 실질적 재료 발견으로의 연결(안정성 검증, 물성 예측)이 부재하여 실용성 측면에서의 검증은 향후 과제로 남아 있다.
