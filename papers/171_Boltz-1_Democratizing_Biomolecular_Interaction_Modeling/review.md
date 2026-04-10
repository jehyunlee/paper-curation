---
title: "171_Boltz-1_Democratizing_Biomolecular_Interaction_Modeling"
authors:
  - "Jeremy Wohlwend"
  - "Gabriele Corso"
  - "Saro Passaro"
  - "Noah Getz"
  - "Mateo Reveiz"
date: "2024.11"
doi: "10.1101/2024.11.19.624167"
arxiv: ""
score: 4.5
essence: "본 논문은 생체분자 복합체(biomolecular complexes)의 3D 구조 예측에서 AlphaFold3 수준의 성능을 달성하면서도 완전히 공개된 오픈소스 모델인 Boltz-1을 소개한다. MIT 라이선스 하에 모든 코드, 가중치, 데이터셋을 공개함으로써 구조생물학 연구의 민주화를 추구한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Protein-Drug_Design_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wohlwend et al._2024_Boltz-1 Democratizing Biomolecular Interaction Modeling.pdf"
---

# Boltz-1 Democratizing Biomolecular Interaction Modeling

> **저자**: Jeremy Wohlwend, Gabriele Corso, Saro Passaro, Noah Getz, Mateo Reveiz, Ken Leidal, Wojtek Swiderski, Liam Atkinson, Tally Portnoi, Itamar Chinn, Jacob Silterra, Tommi Jaakkola, Regina Barzilay | **날짜**: 2024-11-20 | **DOI**: [10.1101/2024.11.19.624167](https://doi.org/10.1101/2024.11.19.624167)

---

## Essence

본 논문은 생체분자 복합체(biomolecular complexes)의 3D 구조 예측에서 AlphaFold3 수준의 성능을 달성하면서도 완전히 공개된 오픈소스 모델인 Boltz-1을 소개한다. MIT 라이선스 하에 모든 코드, 가중치, 데이터셋을 공개함으로써 구조생물학 연구의 민주화를 추구한다.

## Motivation

- **Known**: AlphaFold2(2020)는 단일 체인 단백질 구조 예측에서 실험적 정확도를 달성했으나, AlphaFold3(2024)는 임의의 생체분자 복합체 예측에서 전례 없는 정확도를 보였다.

- **Gap**: AlphaFold3는 상용화된 모델로서 완전히 공개되지 않아, 전세계 연구자와 개발자들이 접근할 수 없다. 또한 생체분자 구조 예측 모델들은 물리적 법칙을 위반하는 hallucination과 비물리적 예측(steric clash, chirality 위반 등)을 빈번히 생성한다.

- **Why**: 공개된 고성능 구조 예측 모델은 전 지구적 협력을 촉진하고, 약물 발견 및 단백질 설계와 같은 중요한 분야의 발전을 가속화할 수 있다.

- **Approach**: AlphaFold3의 일반 프레임워크를 기반으로 하되, (1) 데이터 처리 알고리즘 개선, (2) 아키텍처 및 확산 모델 개선, (3) 신뢰도 모델 재설계, (4) 추론 시간 steering 기법을 통해 물리적 제약 조건을 적용한다.

## Achievement

1. **AlphaFold3 수준의 성능 달성**: 다양한 벤치마크에서 상용 최고 성능 모델과 동등한 성능을 보여주며, 공개된 도구 중 새로운 기준을 설정했다(TM-score 0.95 수준의 정확도).

2. **4배 계산량 감소**: AlphaFold3 대비 약 1/4의 계산량으로 68k 스텝 학습으로 유사한 성능을 달성 (AlphaFold3는 150k 스텝, 배치 크기 256 vs Boltz-1 배치 크기 128).

3. **Boltz-steering 기술**: 추론 시간에 hallucination과 비물리적 예측을 거의 완전히 해결하는 새로운 스티어링 기법을 제시하여 모델 정확도를 유지하면서 물리적 타당성을 보장한다.

4. **완전 공개 모델**: 학습/추론 코드, 모델 가중치, 데이터셋, 벤치마크를 MIT 라이선스로 공개하여 전 세계 연구 커뮤니티의 접근을 가능하게 했다.

## How

### 데이터 파이프라인 (Data Pipeline)

- **데이터 소스**: 2021년 9월 30일 이전 PDB 구조(해상도 9Å 이상), OpenFold 증류 데이터셋(약 270K 구조)

- **밀집 MSA 페어링 알고리즘 (Dense MSA Pairing Algorithm)**: 분류학(taxonomy) 정보를 활용하여 단백질 복합체의 MSA를 페어링하면서도 MSA 밀도를 유지 (모델 복잡도가 MSA 행 수에 선형 비례)

- **통합 크로핑 알고리즘 (Unified Cropping Algorithm)**: 연속적(contiguous) 크로핑과 공간적(spatial) 크로핑의 장점을 결합하여 가변 크기 복합체를 효율적으로 학습

- **강건한 포켓 컨디셔닝 (Robust Pocket-Conditioning)**: 사용자가 정의한 결합 포켓(binding pocket)에 기반한 예측을 강건하게 수행

### 모델링 (Modeling)

- **아키텍처 수정사항**: 표현의 흐름 변경, 확산 학습/추론 절차 개선

- **신뢰도 모델 (Confidence Model)**: 아키텍처 컴포넌트 개정 및 모델 트렁크 레이어의 미세조정으로 재설계

- **최적화**: 추론 속도 최적화를 통해 실무 적용 가능성 향상

### Boltz-Steering 기법

- **목표**: 구조 예측 모델의 물리적 비타당성 문제 해결 (내부 기하학, chirality, steric clash, 체인 겹침 등)

- **메커니즘**: 추론 시간에 제약 포텐셜(constraint potentials)을 적용하여 물리적 법칙을 만족하는 구조로 모델 예측을 유도

- **효과**: 모델의 정확도를 유지하면서 거의 모든 물리적 위반 문제를 해결

### 벤치마크 및 테스트셋

- **새로운 표준화된 테스트셋 공개**: 2023년 1월 13일 이후 출시된 PDB 구조(593개, 크기 100-2000 잔기) 기반 테스트셋으로 일관된 벤치마킹 가능

- **검증셋**: 553개 구조로 구성

## Originality

- **Dense MSA Pairing Algorithm**: 분류학 정보를 기반으로 한 혁신적인 MSA 페어링 방식으로 복합체 학습에서의 신호 품질과 계산 효율성의 균형 달성

- **Unified Cropping Strategy**: 기존의 이원적 크로핑 방식을 통합하여 더 나은 학습 신호 제공

- **Boltz-steering 기법**: 추론 시간의 제약 조건 기반 스티어링을 통해 생성 모델의 물리적 타당성 문제를 처음으로 체계적으로 해결

- **대폭 감소된 계산량**: AlphaFold3 대비 1/4 수준의 계산으로 유사 성능 달성 (데이터 처리 및 모델 설계 최적화)

- **완전 개방 접근**: 상용 모델 수준의 성능을 갖춘 첫 번째 완전 오픈소스 모델로서, 구조생물학 연구의 민주화에 기여

## Limitation & Further Study

- **한계**:
  - 논문은 아직 피어 리뷰 전 preprint 상태로, 커뮤니티 검증이 필요함
  - AlphaFold3는 여전히 비공개 상태로 정확한 성능 비교가 제한적
  - Boltz-steering은 추가 계산을 필요로 하여 실시간 응용에는 제약이 있을 수 있음
  - 매우 크거나 복잡한 생체분자 복합체(예: 바이러스 캡시드)에 대한 성능 평가가 제한적

- **후속 연구**:
  - 커뮤니티 기여를 통한 지속적 모델 개선
  - Boltz-steering 기법의 일반화 및 다른 생성 모델로의 확장
  - 동적 단백질 상호작용 및 시간 변화 구조 예측으로의 확장
  - 특정 산업 응용(신약 개발, 합성 생물학 등)에 최적화된 변형 모델 개발


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4.5/5

**총평**: Boltz-1은 AlphaFold3 수준의 성능을 갖춘 첫 번째 완전 공개 모델로서, Boltz-steering을 통한 물리적 제약 조건 통합과 대폭 감소된 계산량은 높이 평가할 만하다. 단순한 모델 공개를 넘어 구조생물학 연구의 민주화를 실현하는 중요한 이정표이며, MIT 라이선스 하의 완전 공개는 전 세계 과학 커뮤니티의 협력과 혁신을 촉진할 것으로 예상된다.

## Related Papers

- 🔄 다른 접근: [[papers/1129_SARS-CoV-2_simulations_go_exascale_to_predict_dramatic_spike/review]] — 같은 생체분자 구조 예측 문제를 상용 vs 오픈소스 접근법으로 해결한다.
- 🔗 후속 연구: [[papers/686_Robust_deep_learning_based_protein_sequence_design_using_Pro/review]] — 단백질 구조 예측을 서열 설계와 결합하여 통합적 단백질 엔지니어링을 가능하게 한다.
- 🔄 다른 접근: [[papers/046_Accurate_structure_prediction_of_biomolecular_interactions_w/review]] — AlphaFold3와 같은 성능을 오픈소스로 구현하여 접근성을 높인다.
- 🔗 후속 연구: [[papers/112_Atomically_accurate_de_novo_design_of_antibodies_with_RFdiff/review]] — 생체분자 상호작용 모델링의 민주화가 원자 수준 정확한 항체 설계의 발전된 형태를 보여준다.
- 🔗 후속 연구: [[papers/686_Robust_deep_learning_based_protein_sequence_design_using_Pro/review]] — 구조 예측과 서열 설계를 결합하여 통합적 단백질 엔지니어링 파이프라인을 구성한다.
- 🔄 다른 접근: [[papers/1129_SARS-CoV-2_simulations_go_exascale_to_predict_dramatic_spike/review]] — 둘 다 단백질 구조 예측에 초점을 두지만 Boltz-1은 오픈소스 접근법을 제시한다.
