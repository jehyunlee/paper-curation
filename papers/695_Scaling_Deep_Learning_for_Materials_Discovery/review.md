---
title: "695_Scaling_Deep_Learning_for_Materials_Discovery"
authors:
  - "Amil Merchant"
  - "Simon Batzner"
  - "Samuel S. Schoenholz"
  - "Muratahan Aykol"
  - "Gowoon Cheon"
date: "2023"
doi: "10.1038/s41586-023-06735-9"
arxiv: ""
score: 4.8
essence: "그래프 신경망(GNN)을 대규모로 학습시킨 GNoME(Graph Networks for Materials Exploration) 모델을 통해 물질 안정성 예측에서 전례 없는 일반화 성능을 달성하였으며, 220만 개의 신규 안정 결정질 구조를 발견하여 인류가 알고 있는 안정 물질을 약 10배 확장했다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Materials_Discovery_Hypotheses"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Merchant et al._2023_Scaling Deep Learning for Materials Discovery.pdf"
---

# Scaling Deep Learning for Materials Discovery

> **저자**: Amil Merchant, Simon Batzner, Samuel S. Schoenholz, Muratahan Aykol, Gowoon Cheon, Ekin Dogus Cubuk | **날짜**: 2023 | **DOI**: [10.1038/s41586-023-06735-9](https://doi.org/10.1038/s41586-023-06735-9)

---

## Essence

![Figure 1](figures/fig1.webp)
*GNoME 기반 효율적 발견. (a) 모델 기반 필터링과 DFT의 데이터 피드백 루프, (b) 381,000개의 신규 안정 물질 발견으로 기존 대비 거의 10배 증가, (c) 736개 구조의 독립적 실험 검증, (d) 6개 원소 포함 물질까지 확장된 예측 능력*

그래프 신경망(GNN)을 대규모로 학습시킨 GNoME(Graph Networks for Materials Exploration) 모델을 통해 물질 안정성 예측에서 전례 없는 일반화 성능을 달성하였으며, 220만 개의 신규 안정 결정질 구조를 발견하여 인류가 알고 있는 안정 물질을 약 10배 확장했다.

## Motivation

- **Known**: 무기 결정질의 발견은 종전에 밀도함수이론(DFT) 기반 고전적 계산과 화학 직관에 의존한 제한적 대체 방식으로 수행되어 왔으며, Materials Project 등을 통해 약 48,000개의 계산적으로 안정한 구조만 카탈로깅됨
  
- **Gap**: 기존 머신러닝 기법들은 에너지 볼록껍질(convex hull) 대비 분해 에너지(decomposition energy) 예측에서 실패했으며, 특히 4개 이상의 원소를 포함한 조합론적 화학 공간의 탐색이 비효율적이었음

- **Why**: 언어, 비전, 생물학 분야에서 데이터와 계산량 증가에 따른 신경망의 신흥(emergent) 예측 능력이 입증되었으므로, 물질 과학에도 유사한 스케일링 법칙이 적용될 수 있다는 가설

- **Approach**: (1) 대칭 인식 부분 대체(SAPS, Symmetry-Aware Partial Substitutions)와 임의 구조 탐색(AIRSS)을 통한 다양한 후보 구조 생성, (2) GNN 기반 에너지 모델 구축, (3) 6라운드의 능동 학습(active learning) 반복을 통한 데이터 피드백 루프 구성

## Achievement

![Figure 2](figures/fig2.webp)
*발견된 안정 결정질의 요약. (a) 4개 이상 원소를 포함한 물질에서 GNoME의 우수한 발견 효율, (b) 4원계(quaternary) 물질의 위상 분리 에너지 분포*

1. **물질 발견의 획기적 확장**: 381,000개의 신규 안정 물질 발견으로 총 421,000개의 안정 결정질 카탈로그 구성 (기존 대비 약 10배 증가). 이 중 736개 구조가 독립적으로 실험 검증됨

2. **예측 성능의 현저한 향상**: 
   - 에너지 예측 오차를 11 meV/atom으로 감소 (기존 28 meV/atom)
   - 구조 정보 기반 안정성 예측 정확도(hit rate) 80% 이상 달성 (기존 1% 대비)
   - 조성 정보만으로 100시도당 33% 정확도 (기존 1%)

3. **신흥 일반화 능력**: 학습 데이터에 없던 5개 이상 원소를 포함한 구조에 대한 정확한 예측, 임의 구조 탐색으로부터의 분포 외(out-of-distribution) 데이터에 대한 강건성 확보

4. **하위 응용 모델링 능력**: 대규모 이방성 상호작용 포텐셜(equivariant interatomic potentials) 학습으로 분자동역학(molecular dynamics) 시뮬레이션 및 이온 전도도 영점 샷(zero-shot) 예측 가능

## How

![Figure 3](figures/fig3.webp)
*학습된 상호작용 포텐셜 스케일링. 이방성 신경망 포텐셜의 성능 향상*

- **구조적 파이프라인**: 
  - 기존 결정질 수정을 통한 후보 생성, SAPS를 통한 불완전 치환으로 10억 개 이상의 구조 생성
  - 부피 기반 테스트-시간 증강(test-time augmentation)과 깊은 앙상블(deep ensemble)을 통한 불확실성 정량화
  - 다형(polymorph) 순위 매김 및 클러스터링

- **조성 파이프라인**:
  - 완화된 산화 상태 제약으로 기존 규칙 회피 (예: Li₁₅Si₄)
  - GNoME 필터링 후 AIRSS를 통해 각 조성마다 100개의 임의 구조 평가

- **능동 학습 메커니즘**:
  - DFT 계산 결과를 다음 라운드 학습 데이터로 지속 편입
  - 6라운드 반복으로 모델 견고성 단계적 향상
  - 재료 프로젝트의 표준화된 DFT 설정(VASP) 사용

- **그래프 신경망 아키텍처**:
  - 메시지 패싱 형식으로 원자 간 관계 모델링
  - 얕은 다층 퍼셉트론(shallow MLP)의 집계 프로젝션
  - 데이터셋 전체의 평균 인접성(average adjacency)으로 정규화

- **성능 지표**:
  - 검증: Materials Project 및 r2SCAN 고정밀 계산과의 비교
  - 메트릭: 평균절대오차(MAE), 안정성 예측 정확도(hit rate), 위상 분리 에너지

## Originality

- **능동 학습의 물질 과학 적용**: 첫 대규모 피드백 루프를 통해 데이터 자체를 지속 생성하면서 모델을 개선하는 혁신적 접근

- **SAPS 방법론**: 대칭성을 고려한 부분 치환으로 화학 직관의 한계를 돌파하고 조합론적 공간 탐색을 가능하게 함

- **신흥 일반화 현상**: 언어·비전 분야의 스케일링 법칙이 물질 과학에도 적용됨을 최초 입증 (전력 법칙을 따르는 성능 향상)

- **다중 파이프라인 통합**: 구조적, 조성적 접근을 병렬 처리하여 탐색 공간의 다양성과 효율성을 동시 확보

- **이방성 포텐셜의 획기적 확장**: 수백만 구조의 완화 궤적(relaxation trajectories) 데이터로 상호작용 포텐셜을 학습하여 분자동역학 시뮬레이션의 정확도 혁신

## Limitation & Further Study

- **동적 안정성 미검증**: 발견된 물질의 동적 안정성(phonon 주파수)이나 열역학적 안정성(온도 영향)에 대한 검증 부재; 향후 포논 계산(DFPT) 통합 필요

- **실험 검증의 제한성**: 736개(약 0.2%)의 독립적 실험 검증에 그쳤으므로, 나머지 물질의 실제 합성 가능성에 대한 불확실성 존재

- **높은 원소 개수에서의 성능 저하**: 5개 이상 원소 시스템은 학습 데이터 부재로 인한 일반화 부족 (비록 개선되었으나 여전히 도전적)

- **계산 비용의 현실적 한계**: 기술 응용 평가에 필요한 전자적 성질(밴드갭, 전도성), 기계적 성질 예측은 별도 모델 필요

- **향후 연구 방향**:
  - 온도, 압력 등 환경 조건 변수 포함 확장
  - 결함(defects), 표면 특성까지 고려한 모델 개발
  - 소재 합성 난이도 예측 모델 병합
  - 더 높은 정밀도의 범함수(hybrid functionals, GW 근사) 검증

## Evaluation

- **Novelty**: 5/5
  - 물질 과학에 능동 학습 기반 데이터 피드백 루프 최초 도입
  - 신흥 일반화 현상의 첫 실증
  - SAPS 등 새로운 구조 생성 기법

- **Technical Soundness**: 5/5
  - 견고한 GNN 아키텍처와 불확실성 정량화
  - 6라운드 반복 능동 학습의 체계적 설계
  - DFT, r2SCAN 등 다중 검증 방법론

- **Significance**: 5/5
  - 인류가 알고 있는 안정 물질을 약 10배 확장 (과학적 영향력 극대)
  - 청정 에너지(고체 전해질, 층상 물질) 응용 시연
  - 736개 실험 검증으로 실용성 입증
  - 이방성 포텐셜을 통한 하위 모델링 능력 개방

- **Clarity**: 4.5/5
  - 전체 방법론과 결과가 명확하게 제시됨
  - Figure 1-3의 시각화가 효과적
  - 다만, 보충 자료 없이는 SAPS의 세부 구현이 다소 불명확

- **Overall**: 4.8/5

**총평**: 본 연구는 그래프 신경망의 대규모 학습과 능동 학습을 결합하여 무기 결정질 발견에 혁명을 일으킨 획기적 성과로, 220만 개 신규 물질 발견과 신흥 일반화 능력 달성으로 계산 물질 과학의 새로운 패러다임을 제시하며, Nature 최고 수준의 학제 간 기여를 입증한다.

## Related Papers

- 🏛 기반 연구: [[papers/343_Foundation_models_for_materials_discovery__current_state_and/review]] — GNoME의 성공이 재료발견 분야 파운데이션 모델 발전의 중요한 사례가 된다.
- 🧪 응용 사례: [[papers/372_General-Purpose_Machine-Learned_Potential_for_CrCoNi_Alloys/review]] — 대규모 재료 발견 결과를 특정 합금 시스템의 머신러닝 포텐셜 개발에 적용한다.
- 🔗 후속 연구: [[papers/241_Criteria-first_semantics-later_reproducible_structure_discov/review]] — 재료 구조 발견을 이미지 기반 구조 추출 방법론으로 확장할 수 있다.
- 🧪 응용 사례: [[papers/343_Foundation_models_for_materials_discovery__current_state_and/review]] — 파운데이션 모델 이론을 GNoME 같은 대규모 재료 발견에 실제 적용한 사례이다.
- 🧪 응용 사례: [[papers/372_General-Purpose_Machine-Learned_Potential_for_CrCoNi_Alloys/review]] — 대규모 재료 발견 결과를 특정 합금 시스템의 정밀 모델링에 적용한다.
- 🏛 기반 연구: [[papers/241_Criteria-first_semantics-later_reproducible_structure_discov/review]] — 구조 발견 방법론이 대규모 재료 발견 결과의 해석과 검증에 필요하다.
- 🔗 후속 연구: [[papers/1099_Generative_Inversion_of_Spectroscopic_Data_for_Amorphous_Str/review]] — 재료 발견을 위한 딥러닝 확장성에서 분광 데이터 역변환으로의 발전
- 🏛 기반 연구: [[papers/758_Simulations_in_the_era_of_exascale_computing/review]] — 재료 발견을 위한 딥러닝 확장 연구가 엑사스케일 컴퓨팅 활용의 기술적 기반을 제공한다.
- 🏛 기반 연구: [[papers/354_From_GPU_Engineering_to_Scientific_Discovery_Parallelism_Tec/review]] — 재료 발견을 위한 딥러닝 확장 연구가 GPU 병렬화 기법의 실제 적용 사례와 최적화 필요성을 제시한다.
