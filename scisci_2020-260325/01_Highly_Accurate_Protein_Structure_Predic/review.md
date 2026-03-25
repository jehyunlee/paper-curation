# Highly Accurate Protein Structure Prediction with AlphaFold

> **저자**: John Jumper, Richard Evans, Alexander Pritzel, Tim Green, Michael Figurnov, Olaf Ronneberger, Kathryn Tunyasuvunakool, Russ Bates, Augustin Žídek, Anna Potapenko, Alex Bridgland, Clemens Meyer, Simon A. A. Kohl, Andrew J. Ballard, Andrew Cowie, Bernardino Romera-Paredes, Stanislav Nikolov, Rishub Jain, Jonas Adler, Trevor Back, Stig Petersen, David Reiman, Ellen Clancy, Michal Zielinski, Martin Steinegger, Michalina Pacholska, Tamas Berghammer, Sebastian Bodenstein, David Silver, Oriol Vinyals, Andrew W. Senior, Koray Kavukcuoglu, Pushmeet Kohli, Demis Hassabis | **날짜**: 2021 | **Journal**: Nature | **DOI**: 10.1038/s41586-021-03819-2

---

## Essence

아미노산 서열만으로 단백질 3D 구조를 원자 수준 정확도로 예측할 수 있다. AlphaFold는 CASP14에서 backbone 중앙값 정확도 0.96 A r.m.s.d.95를 달성하여, 차점자(2.8 A)를 약 3배 앞섰으며, 이는 탄소 원자 직경(1.4 A) 수준의 정밀도다. All-atom 정확도는 1.5 A r.m.s.d.95로, 대다수 경우에서 실험적 구조 결정과 경쟁할 수 있는 수준이다.

## Motivation

실험적으로 결정된 단백질 구조는 약 10만 개에 불과하지만, 알려진 단백질 서열은 수십억 개에 달한다. 단일 단백질 구조를 실험적으로 결정하는 데 수개월에서 수년이 소요되어, 구조 생물학의 병목이 되고 있었다. 서열로부터 3D 구조를 예측하는 "단백질 접힘 문제"는 50년 이상의 난제였으며, 기존 계산 방법들은 상동 구조가 없는 경우 원자 수준 정확도에 크게 미달했다. 물리적 시뮬레이션과 진화적 공변이(covariation) 분석이라는 두 가지 전통적 접근법의 한계를 딥러닝 기반 end-to-end 구조 예측으로 돌파하고자 했다.

## Achievement

1. **CASP14 최고 성능**: Backbone 정확도 중앙값 0.96 A r.m.s.d.95 (95% CI: 0.85-1.16 A), 차점자 대비 약 3배 우수
2. **All-atom 정확도**: 1.5 A r.m.s.d.95 (95% CI: 1.2-1.6 A)로 side chain까지 정밀 예측, 차점자(3.5 A) 대비 2배 이상 향상
3. **대형 단백질 예측**: 구조적 상동체가 없는 2,180잔기 단백질에 대해서도 정확한 도메인 및 도메인 패킹 예측 성공
4. **신뢰도 추정**: per-residue pLDDT 점수가 실제 lDDT-Ca 정확도를 신뢰성 있게 예측하며, TM-score도 정확하게 추정
5. **추론 속도**: 앙상블 없이 256잔기 단백질 0.6분, 384잔기 1.1분, 2,500잔기 약 2.1시간 (V100 GPU 단일 모델)

## How

- **데이터**: PDB 구조 데이터(약 10만 개), MSA 구축을 위한 UniRef90, BFD(약 22억 서열), MGnify 등 대규모 서열 데이터베이스, HHBlits/JackHMMER로 MSA 생성
- **모델 아키텍처**: Evoformer(MSA 표현과 pair 표현 간 정보 교환을 위한 attention 기반 블록) + Structure Module(잔기별 회전/병진으로 3D 좌표 생성, Invariant Point Attention)
- **핵심 기법**: Triangle multiplicative update(쌍별 표현의 기하학적 일관성 강화), FAPE loss(다중 정렬 기반 좌표 손실), recycling(반복 정제), noisy student self-distillation(약 35만 개 비표지 서열로 자기증류)
- **학습**: 128 TPUv3 코어에서 약 1주일 초기 학습 + 추가 fine-tuning
- **후처리**: Amber99sb force field로 구조 relaxation (정확도 향상 없이 입체화학적 위반 제거)

## Originality

- **Evoformer**: MSA와 pair 표현 간 양방향 정보 흐름을 가능케 하는 새로운 신경망 블록으로, 기존 distance matrix 예측 후 3D 복원하는 2단계 파이프라인을 end-to-end로 대체
- **Triangle update**: 쌍별 거리 표현에 삼각 부등식 등 기하학적 제약을 직접 반영하는 attention 및 multiplicative update 메커니즘
- **Invariant Point Attention (IPA)**: 3D 공간에서 쿼리/키/값 포인트를 잔기 로컬 프레임으로 변환하여 전역 회전/병진에 불변인 구조 업데이트 실현
- **Residue gas 표현**: 펩타이드 결합 제약을 일시적으로 해제하여 모든 잔기를 독립적으로 정제할 수 있게 하는 구조 표현 방식
- **Self-distillation 활용**: 비표지 서열 35만 개의 예측 구조를 학습 데이터로 재활용하여 정확도 향상

## Limitation & Further Study

### 저자들이 언급한 한계
- MSA 깊이가 약 30개 서열 미만일 때 정확도가 크게 감소하며, MSA 구축이 불가능한 단백질(예: 고아 서열)에는 적용이 어려움
- 이종 복합체(heteromeric complex) 내에서 다른 사슬과의 접촉이 주된 형태를 결정하는 bridging domain에 대해서는 예측력이 현저히 저하
- 단백질 동역학이나 앙상블 구조는 다루지 않으며, 단일 정적 구조만 예측

### 리뷰어 판단 아쉬운 점
- 학습에 사용된 PDB 데이터의 실험적 해상도 분포나 품질에 대한 분석이 부족하여, 학습 데이터 편향의 영향을 판단하기 어려움
- 본질적으로 무질서한(intrinsically disordered) 영역에 대한 체계적 평가가 제한적
- 리간드, 보조인자, 번역 후 변형(PTM) 등이 구조에 미치는 영향을 고려하지 않음
- GPU 메모리 제약으로 인해 대형 단백질(약 1,300잔기 이상)은 특수 설정이 필요하며, 접근성에 한계

### 후속 연구
- 이종 복합체(heteromeric complex) 구조 예측으로의 확장 (저자들이 직접 언급)
- 단백질-리간드 상호작용 및 약물 결합 부위 예측과의 통합
- 단백질 동역학 및 conformational ensemble 예측
- MSA 없이도 작동하는 단일 서열 기반 구조 예측 (이후 ESMFold 등으로 실현)
- 구조 예측을 활용한 대규모 기능 주석(functional annotation) 파이프라인 구축

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 5/5 |
| Technical Soundness | 5/5 |
| Significance | 5/5 |
| Clarity | 4/5 |
| Overall | 5/5 |

**총평**: 50년 난제인 단백질 구조 예측 문제를 원자 수준 정확도로 해결한 획기적 연구로, Evoformer와 IPA 등 독창적 아키텍처 설계가 물리적/기하학적 귀납적 편향을 딥러닝에 성공적으로 통합했다. 구조 생물학과 AI 분야 모두에 근본적 영향을 미친 랜드마크 논문이다.
