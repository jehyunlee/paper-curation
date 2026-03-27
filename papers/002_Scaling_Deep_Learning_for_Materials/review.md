# Scaling Deep Learning for Materials Discovery

> **저자**: Amil Merchant, Simon Batzner, Samuel S. Schoenholz, Muratahan Aykol, Gowoon Cheon, Ekin Dogus Cubuk | **날짜**: 2023 | **Journal**: Nature | **DOI**: 10.1038/s41586-023-06735-9

---

## Essence

Graph neural network (GNoME)을 대규모 active learning과 결합하여 기존 48,000개에서 381,000개의 새로운 안정 결정 구조를 발견, 인류가 알고 있는 안정 물질을 약 10배 확장했다. 총 2.2M 구조가 기존 convex hull 아래에 위치하며, hit rate를 기존 1%에서 구조 기반 80%, 조성 기반 33%로 향상시켰다.

## Motivation

- **알려진 것**: ICSD에 약 20,000개의 computationally stable 구조가 등록되어 있고, Materials Project/OQMD 등 계산 데이터베이스를 통해 48,000개까지 확장됨
- **Gap**: 실험적 접근은 비용/처리량/합성 문제로 확장 불가능하고, 기존 ML 기법은 convex hull 대비 stability (decomposition energy) 예측에 실패하여 실질적 재료 발견에 무력했음 (hit rate ~1%)
- **왜 중요한가**: Clean energy, 반도체, 배터리, 태양전지 등 기술 혁신이 신규 무기 결정 재료 발견에 의존
- **접근법**: (1) Symmetry-aware partial substitutions (SAPS)와 random structure search로 다양한 후보 생성, (2) GNN 기반 에너지 예측으로 필터링, (3) DFT 검증을 data flywheel로 활용하는 iterative active learning

## Achievement

1. **381,000개 신규 안정 결정 구조** 발견 -- 기존 대비 약 10배 확장, 총 421,000개 안정 결정
2. **에너지 예측 정확도**: MAE 11 meV/atom (기존 28 meV/atom에서 개선), hit rate 80% (구조 기반) / 33% (조성 기반)
3. **Emergent out-of-distribution 일반화**: 학습 데이터에 4원소까지만 포함했음에도 5+ 원소 물질에서 효과적 예측
4. **실험적 검증**: 736개 구조가 독립적으로 실험 합성 확인, r2SCAN 검증에서 84%가 stable 유지
5. **범용 interatomic potential**: GNoME 데이터셋으로 pretrain한 NequIP potential이 zero-shot으로 AIMD 수준 정확도 달성, 623개 미지 조성에서 superionic conductor 분류 가능
6. **응용 시연**: layered materials ~52,000개 (기존 ~1,000), Li-ion conductor 후보 528개 (25배 증가) 식별

## How

- **후보 생성**: (1) Structural pipeline -- 기존 결정에 ionic substitution + SAPS (대칭 인식 부분 치환)으로 10^9개 이상 후보 생성; (2) Compositional pipeline -- 조성 모델 예측 후 AIRSS (Ab initio Random Structure Searching)로 100개 랜덤 구조 초기화
- **GNoME 모델**: Message-passing GNN, one-hot element embedding, 3-6 message passing layers, embedding dim 256, swish activation. Deep ensemble (n=10)과 volume-based test-time augmentation으로 불확실성 정량화
- **Active learning**: 6라운드 반복 -- GNoME 필터링 -> DFT (VASP, PBE functional) 검증 -> 데이터 추가 -> 모델 재학습. Power-law scaling 확인
- **Interatomic potential**: E(3)-equivariant NequIP potential을 GNoME relaxation trajectory에서 pretrain. 5 layers, 128 scalars + 64 vectors + 32 tensors, radial cutoff 5 A, 16.24M parameters
- **검증**: r2SCAN functional로 binary/ternary의 84%, quaternary의 86.8% stable 확인. ICSD 실험 구조와 736개 매칭

## Originality

- **Data flywheel 개념**: Active learning을 통해 ML 예측 -> DFT 검증 -> 학습 데이터 확장의 선순환 구조를 재료 발견에 최초로 대규모 적용
- **SAPS (Symmetry-Aware Partial Substitutions)**: 결정 대칭의 Wyckoff position을 활용한 부분 치환으로, double perovskite 같은 기존 full substitution으로 발견 불가능한 구조 탐색 가능 (381,000개 중 232,477개가 SAPS 유래)
- **Neural scaling law의 재료과학 적용**: 언어/비전 모델에서 관찰된 power-law scaling이 재료 에너지 예측에도 적용됨을 입증
- **Zero-shot universal potential**: Relaxation trajectory만으로 학습한 potential이 AIMD, 고온, vacancy 등 미학습 분포에서도 작동하는 transferable MLIP 실현

## Limitation & Further Study

### 저자들이 언급한 한계

- Phase transition, dynamic stability (vibrational profile), configurational entropy에 대한 이해가 부족
- Synthesizability (실제 합성 가능성)는 thermodynamic stability와 별개 문제
- AIRSS 초기화의 수렴 실패 문제 -- 특정 조성에서 DFT relaxation이 대부분 실패
- Spin ordering을 ferromagnetic으로만 가정하여 antiferromagnetic 물질의 정확한 에너지 계산 제한

### 자체판단 아쉬운 점

- PBE functional의 inherent 오류가 대규모로 전파될 가능성 -- r2SCAN 검증에서 16%가 unstable로 전환
- 비정질(amorphous), 표면(surface), 결함(defect) 구조는 다루지 않아 실제 응용 환경과 괴리
- Bandgap 등 electronic property 예측은 별도 계산이 필요하여 기능성 재료 스크리닝의 통합적 접근이 부족
- Google DeepMind의 대규모 인프라(TPU, Apache Beam)에 의존하여 학계에서의 재현이 사실상 불가능

### 후속 연구

- Synthesizability prediction과 결합한 end-to-end 재료 발견 파이프라인
- Meta-stable phase와 kinetic barrier를 고려한 thermodynamic-kinetic 통합 안정성 평가
- Fine-tuning을 통한 domain-specific MLIP 개발 (촉매, 전극 등)
- 다성분(5+ element) 화학 공간의 체계적 탐색 확대

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 5/5 |
| Technical Soundness | 4/5 |
| Significance | 5/5 |
| Clarity | 4/5 |
| Overall | 5/5 |

**총평**: Active learning 기반 data flywheel과 GNN의 scaling을 결합하여 안정 무기 결정 재료를 10배 확장한 기념비적 연구로, AI for Materials Science 분야의 AlphaFold 격 성과이다. 다만 PBE functional 의존성과 synthesizability 미고려가 실용화까지의 남은 과제이다.
