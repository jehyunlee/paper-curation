# Highly Accurate Protein Structure Prediction with AlphaFold

> **저자**: John Jumper, Richard Evans, Alexander Pritzel, Tim Green, Michael Figurnov, Olaf Ronneberger, Kathryn Tunyasuvunakool, Russ Bates, Augustin Zidek, Anna Potapenko, Alex Bridgland, Clemens Meyer, Simon A. A. Kohl, Andrew J. Ballard, Andrew Cowie, Bernardino Romera-Paredes, Stanislav Nikolov, Rishub Jain, Jonas Adler, Trevor Back, Stig Petersen, David Reiman, Ellen Clancy, Michal Zielinski, Martin Steinegger, Michalina Pacholska, Tamas Berghammer, Sebastian Bodenstein, David Silver, Oriol Vinyals, Andrew W. Senior, Koray Kavukcuoglu, Pushmeet Kohli, Demis Hassabis | **날짜**: 2021 | **Journal**: Nature | **DOI**: 10.1038/s41586-021-03819-2

---

## Essence

AlphaFold는 아미노산 서열만으로 단백질 3D 구조를 원자 수준 정확도로 예측하는 최초의 computational method이다. CASP14에서 median backbone accuracy 0.96 A r.m.s.d.95를 달성하여, 차순위 방법(2.8 A)을 압도적으로 능가했으며, 이는 탄소 원자 폭(~1.4 A)에 근접하는 실험적 구조 수준의 정확도이다.

## Motivation

- **알려진 것**: 실험적으로 약 100,000개의 단백질 구조가 결정되었으나, 이는 수십억 개의 알려진 단백질 서열 중 극히 일부에 불과
- **Gap**: 단일 단백질 구조 결정에 수개월~수년이 소요되어 구조적 커버리지가 병목 상태
- **왜 중요한가**: 50년 이상 미해결이었던 protein folding problem의 structure prediction 구성요소를 해결해야 large-scale structural bioinformatics가 가능
- **접근법**: 진화적, 물리적, 기하학적 제약조건을 deep learning architecture에 통합하는 새로운 neural network (AlphaFold) 설계

## Achievement

1. **CASP14 압도적 성능**: Median backbone accuracy 0.96 A r.m.s.d.95 (95% CI: 0.85-1.16 A) -- 차순위 대비 약 3배 정확 (2.8 A r.m.s.d.95)
2. **All-atom 정확도**: 1.5 A r.m.s.d.95 달성 (차순위 3.5 A 대비 2배 이상 개선)
3. **최근 PDB 구조 검증**: 10,795개 단백질 체인에서 full chain median 1.46 A r.m.s.d.95 (training set 이후 구조)
4. **신뢰도 추정**: pLDDT가 실제 lDDT-Ca와 높은 상관관계 (Pearson's r = 0.76), pTM과 TM-score 간 r = 0.85
5. **대규모 단백질 처리**: 2,180-residue 단백질도 정확한 domain packing으로 예측 가능, GPU 분~시간 단위 추론 속도

## How

- **데이터**: PDB 구조 (training cutoff 2018.04.30), MSA (UniRef90, BFD, Uniclust30, MGnify), template 구조
- **아키텍처 (Evoformer)**: MSA representation과 pair representation을 48개 블록에서 반복적으로 교환하는 novel neural network block. Triangle multiplicative update와 triangle self-attention으로 기하학적 일관성 보장
- **Structure Module**: Invariant Point Attention (IPA)을 사용하여 residue gas representation (각 잔기의 독립적 rotation/translation)을 iterative하게 정제. 8개 shared-weight 블록, 3회 recycling
- **Loss Function**: Frame Aligned Point Error (FAPE) -- 다중 alignment 하에서의 clamped L1 loss
- **Self-distillation**: 350,000개 Uniclust30 서열의 예측 구조를 high-confidence subset으로 필터링하여 재학습
- **BERT-style MSA masking**: 진화적/공변이 관계 학습을 위한 masked MSA objective를 구조 loss와 jointly training
- **학습 인프라**: 128 TPU v3 코어, 초기 학습 ~1주, fine-tuning ~4일 추가

## Originality

- **Evoformer**: MSA와 pairwise feature를 jointly embed하는 최초의 architecture로, triangle inequality에 기반한 update 메커니즘이 핵심 혁신
- **Invariant Point Attention (IPA)**: 3D 공간에서 SE(3)-equivariant한 attention 연산을 구현하여, 전역 회전/이동에 불변한 구조 정제 가능
- **Residue Gas Representation**: 단백질 체인 제약을 의도적으로 깨뜨려(breaking chain constraint) 모든 부분의 동시 local refinement를 가능하게 한 발상의 전환
- **End-to-end Structure Prediction**: 3D 좌표를 직접 출력하는 differentiable pipeline으로, 기존의 distance matrix → heuristic 구조 복원 파이프라인을 완전히 대체
- **물리적+진화적 접근의 통합**: Handcrafted feature 최소화하면서 물리적/기하학적 inductive bias를 network design에 내재화

## Limitation & Further Study

### 저자들이 언급한 한계

- MSA depth가 약 30 서열 미만일 때 정확도가 크게 감소하는 threshold effect 존재
- Heterotypic contact가 지배적인 단백질(bridging domain 등)에서 성능이 약함 -- intra-chain/homotypic contact가 적은 경우
- 단일 체인 예측에 한정되며, hetero-complex 예측은 미래 시스템에서 다룰 예정

### 자체판단 아쉬운 점

- Intrinsically disordered region에 대한 체계적 평가가 부족하며, pLDDT가 낮은 영역이 실제 disorder인지 예측 실패인지 구분 어려움
- Ligand, cofactor, post-translational modification의 영향을 explicit하게 모델링하지 않아, 이들에 의해 구조가 결정되는 단백질에서의 한계가 명확히 분석되지 않음
- 128 TPU v3로 학습하는 계산 비용이 매우 높아, 재현성과 접근성 측면에서 학계에 부담
- Conformational ensemble이나 dynamic 정보를 제공하지 못하며, 단일 static 구조만 예측

### 후속 연구

- AlphaFold-Multimer로의 확장을 통한 protein complex 예측 (실제 후속 연구로 진행됨)
- 단백질-리간드 상호작용 예측 및 drug discovery 적용
- Conformational flexibility/dynamics 예측으로의 확장
- MSA-free 또는 few-shot 방식의 orphan protein 구조 예측
- Proteome-scale 구조 예측 데이터베이스 구축 (AlphaFold DB로 실현)

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 5/5 |
| Technical Soundness | 5/5 |
| Significance | 5/5 |
| Clarity | 4/5 |
| Overall | 5/5 |

**총평**: 50년 이상 미해결이었던 protein structure prediction 문제를 사실상 해결한 획기적 연구로, Evoformer와 IPA라는 독창적 architecture 혁신을 통해 실험적 정확도에 필적하는 성능을 달성했다. AI for Science 분야의 가장 대표적인 성공 사례이자, 구조생물학의 패러다임을 근본적으로 전환시킨 milestone 논문이다.
