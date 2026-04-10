---
title: "046_Accurate_structure_prediction_of_biomolecular_interactions_w"
authors:
  - "Josh Abramson"
  - "Jonas Adler"
  - "Jack Dunger"
  - "Richard Evans"
  - "Tim Green 외 다수"
date: "2024"
doi: "10.1038/s41586-024-07487-w"
arxiv: ""
score: 4.75
essence: "AlphaFold 3는 단백질, 핵산, 소분자, 이온, 변형된 잔기를 포함한 생체분자 복합체 구조를 통합된 딥러닝 프레임워크 내에서 정확하게 예측하는 모델이다. 확산 기반(diffusion-based) 아키텍처를 통해 기존 특화된 도킹 및 예측 도구들을 크게 능가하는 성능을 달성했다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Protein_Structure_Prediction"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Abramson et al._2024_Accurate structure prediction of biomolecular interactions with AlphaFold 3 1.pdf"
---

# Accurate structure prediction of biomolecular interactions with AlphaFold 3

> **저자**: Josh Abramson, Jonas Adler, Jack Dunger, Richard Evans, Tim Green 외 다수 | **날짜**: 2024 | **DOI**: [10.1038/s41586-024-07487-w](https://doi.org/10.1038/s41586-024-07487-w)

---

## Essence

AlphaFold 3는 단백질, 핵산, 소분자, 이온, 변형된 잔기를 포함한 생체분자 복합체 구조를 통합된 딥러닝 프레임워크 내에서 정확하게 예측하는 모델이다. 확산 기반(diffusion-based) 아키텍처를 통해 기존 특화된 도킹 및 예측 도구들을 크게 능가하는 성능을 달성했다.

## Motivation

- **Known**: AlphaFold 2는 단백질 구조 예측에서 혁명을 일으켰고, 간단한 입력 수정으로 단백질 상호작용 예측도 가능했음. 특정 상호작용 유형별로 다양한 특화된 예측 도구들이 개발됨.

- **Gap**: 기존 방법들은 특정 상호작용 유형에만 특화되어 있으며, 리간드, 핵산, 변형된 잔기 등을 포함한 일반적인 생체분자 복합체를 정확하게 예측하지 못함. 물리 기반 방법들이 여전히 더 나은 성능을 보임.

- **Why**: 생물학적 복합체의 정확한 모델링은 세포 기능 이해와 치료제 합리적 설계에 필수적임.

- **Approach**: AlphaFold 2 아키텍처를 대폭 개선하여, Evoformer를 간단한 Pairformer로 교체하고 Structure Module을 Diffusion Module로 대체하여 일반화된 생체분자 복합체 예측 가능하게 함.

## Achievement

![Figure 1 - AlphaFold 3의 예측 정확도](figures/fig1.webp)
*그림 1: AlphaFold 3는 다양한 생체분자 복합체에서 정확하게 구조를 예측함*

1. **포괄적 성능 향상**: 단백질-리간드 상호작용에서는 최고 수준의 도킹 도구를 능가하고, 단백질-핵산 상호작용에서는 핵산 특화 예측기를 초과하는 성능 달성

2. **통합 프레임워크**: 단백질, 핵산, 소분자, 이온, 변형 잔기를 포함한 거의 모든 PDB 분자 유형을 단일 모델로 예측

3. **항체-항원 예측**: AlphaFold-Multimer v2.3보다 유의미하게 높은 정확도로 항체-항원 상호작용 예측

4. **구조적 신뢰도 개선**: 원자 수준(atom-level)과 쌍 수준(pairwise)의 오류를 예측하는 신뢰도 지표 개발 (pLDDT, PAE, PDE)

## How

![Figure 2 - 아키텍처 개선사항](figures/fig2.webp)
*그림 2: Diffusion Module을 통한 원자 좌표 직접 예측*

- **MSA 처리 축소**: Evoformer의 4개 블록으로 축소하고 pair-weighted averaging 사용으로 계산 효율성 증대

- **Pairformer 도입**: 쌍 표현(pair representation)과 단일 표현(single representation)만 처리하여 MSA 표현 제거

- **Diffusion Module**: 백본 프레임이나 side chain torsion 각도 대신 원자 좌표를 직접 예측
  - Noised 원자 좌표로부터 실제 좌표 예측하도록 학습
  - 저 노이즈에서 국부 입체화학 학습, 고 노이즈에서 전역 구조 학습
  - Stereochemical violation penalty 제거 가능

- **Cross-distillation**: AlphaFold-Multimer v2.3 예측 구조로 학습 데이터 강화하여 hallucination(구조화되지 않은 영역의 허위 구조 생성) 감소

- **Confidence head 학습**: 확산 "rollout" 절차로 전체 구조 생성 시뮬레이션 후 신뢰도 메트릭 계산

- **선택적 샘플링**: 제한된 학습 샘플의 과적합을 방지하기 위해 훈련 세트별 샘플링 확률 조정

## Originality

- 생체분자 구조 예측에 확산 모델의 생성적 접근을 적용하여 임의의 화학 구조 자동 처리

- Cross-distillation 방법으로 생성 모델의 hallucination 문제를 통합 학습을 통해 해결하는 혁신적 접근

- 회전 불변성(rotational invariance)과 등변성(equivariance) 제거로 아키텍처 단순화 달성

- 원자 수준 좌표 직접 예측으로 단백질-특화 parametrization 제거하고 일반 리간드 처리 용이

- Diffusion rollout을 통한 새로운 신뢰도 학습 방법 제시

## Limitation & Further Study

- **Hallucination 관리**: Cross-distillation이 hallucination을 감소시켰으나, CAID 2 벤치마크에서 여전히 개선의 여지 있음

- **계산 비용**: 논문에서 추론 시간, 메모리 요구사항 등 계산 복잡성에 대한 구체적 분석 부재

- **제한된 평가 범위**: 15,000자 범위 내에서는 모든 복합체 유형에 대한 벤치마크 결과가 완전히 제시되지 않음

- **동역학 정보 부재**: 정적 구조 예측에 집중되어 있으며 단백질-리간드 상호작용의 동역학적 특성 미반영

- **후속 연구 방향**: 
  - 확산 모델의 불확실성 정량화를 통한 구조 다양성 샘플링
  - 단백질 동역학 및 유연성 예측으로 확장
  - 막 단백질과 같은 어려운 케이스에 대한 특화된 개선


## Evaluation

- Novelty: 5/5
- Technical Soundness: 5/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4.75/5

**총평**: AlphaFold 3는 확산 기반 생성 모델을 생체분자 구조 예측에 혁신적으로 적용하여, 단백질부터 리간드, 핵산까지 모든 유형의 복합체를 통합 프레임워크로 정확하게 예측함으로써 구조생물학과 약물 설계 분야에 패러다임 전환을 가져오는 매우 중요한 기여이다.

## Related Papers

- 🏛 기반 연구: [[papers/403_Highly_accurate_protein_structure_prediction_with_AlphaFold/review]] — AlphaFold 2의 단일 단백질 구조 예측 기술을 기반으로 생체분자 복합체 예측으로 확장한 직접적인 후속 연구이다
- 🧪 응용 사례: [[papers/1129_SARS-CoV-2_simulations_go_exascale_to_predict_dramatic_spike/review]] — 생체분자 복합체 구조 예측 기술이 바이러스-숙주 상호작용 연구와 약물-단백질 결합 분석에 직접 활용될 수 있다
- 🔄 다른 접근: [[papers/440_Inverse_designing_metamaterials_with_programmable_nonlinear/review]] — 확산 모델 기반 생체분자 구조 예측과 그래프 신경망 기반 메타물질 설계가 서로 다른 도메인에서 유사한 역설계 문제를 해결한다
- 🔄 다른 접근: [[papers/305_Efficient_Evolutionary_Search_Over_Chemical_Space_with_Large/review]] — 확산 기반 생체분자 구조 예측과 LLM 기반 화학 공간 탐색이 각각 구조와 서열 관점에서 분자 설계 문제에 접근한다
- 🔗 후속 연구: [[papers/403_Highly_accurate_protein_structure_prediction_with_AlphaFold/review]] — AlphaFold의 단일 단백질 구조 예측을 생체분자 복합체 상호작용 예측으로 확장한 직접적인 발전이다
- 🔄 다른 접근: [[papers/305_Efficient_Evolutionary_Search_Over_Chemical_Space_with_Large/review]] — LLM을 활용한 분자 진화 탐색과 확산 모델 기반 생체분자 구조 예측이 각각 서열과 구조 관점에서 분자 설계 문제에 접근한다
- 🔄 다른 접근: [[papers/440_Inverse_designing_metamaterials_with_programmable_nonlinear/review]] — 그래프 신경망 기반 메타물질 설계와 확산 모델 기반 생체분자 구조 예측이 각각 공학과 생물학 분야에서 유사한 역설계 접근법을 보여준다
- 🔄 다른 접근: [[papers/171_Boltz-1_Democratizing_Biomolecular_Interaction_Modeling/review]] — AlphaFold3와 같은 성능을 오픈소스로 구현하여 접근성을 높인다.
- 🔗 후속 연구: [[papers/1129_SARS-CoV-2_simulations_go_exascale_to_predict_dramatic_spike/review]] — AlphaFold 3의 생체분자 복합체 예측 기술과 스파이크 단백질의 동역학 시뮬레이션이 상호 보완적인 구조-기능 분석을 가능하게 한다
