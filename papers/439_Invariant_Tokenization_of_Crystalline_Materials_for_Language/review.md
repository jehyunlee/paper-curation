---
title: "439_Invariant_Tokenization_of_Crystalline_Materials_for_Language"
authors:
  - "Keqiang Yan"
  - "Xiner Li"
  - "Hongyi Ling"
  - "K. Ashen"
  - "Carl N. Edwards"
date: "2025"
doi: "10.48550/arXiv.2503.00152"
arxiv: ""
score: 4.1
essence: "본 연구는 3D 결정 구조(crystal structure)를 언어 모델(LM)이 처리 가능한 1D 수열로 변환하되, SE(3) 불변성과 주기성 불변성을 보장하는 **Mat2Seq** 방법을 제안한다. 이를 통해 동일한 결정에 대해 고유한 수열 표현을 생성하여 언어 모델 기반의 신규 결정 물질 생성을 가능하게 한다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Domain-specific_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yan et al._2025_Invariant Tokenization of Crystalline Materials for Language Model Enabled Generation.pdf"
---

# Invariant Tokenization of Crystalline Materials for Language Model Enabled Generation

> **저자**: Keqiang Yan, Xiner Li, Hongyi Ling, K. Ashen, Carl N. Edwards | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2503.00152](https://doi.org/10.48550/arXiv.2503.00152)

---

## Essence

![Figure 2](figures/fig2.webp)
*Mat2Seq의 파이프라인: 3D 결정 구조를 Niggli 셀 축약과 원시 단위 셀 결정을 거쳐 고유한 1D 수열로 변환*

본 연구는 3D 결정 구조(crystal structure)를 언어 모델(LM)이 처리 가능한 1D 수열로 변환하되, SE(3) 불변성과 주기성 불변성을 보장하는 **Mat2Seq** 방법을 제안한다. 이를 통해 동일한 결정에 대해 고유한 수열 표현을 생성하여 언어 모델 기반의 신규 결정 물질 생성을 가능하게 한다.

## Motivation

- **Known**: 최근 언어 모델의 성공에 힘입어 XYZ, CIF 파일 형식으로 분자 및 결정 구조를 표현하려는 시도들이 있었음. 또한 CDVAE, DiffCSP, MatterGen 등 신경망 기반 결정 구조 생성 모델들이 개발됨.

- **Gap**: 기존 CIF 파일 기반 방법들은 동일한 결정 구조에 대해 원자 순서, 분수 좌표, 격자 벡터 변화 등으로 인해 무한히 많은 서로 다른 수열 표현을 생성하며, 이는 SE(3) 및 주기성 불변성을 만족하지 않고 고유성(uniqueness)을 보장하지 못함.

- **Why**: 언어 모델이 동일 결정의 모든 등가 표현을 동일한 확률로 인식해야 하나, CIF 기반 접근은 대규모 데이터 증강 없이는 이를 달성 불가능. 이는 모델 학습을 크게 부담시킴.

- **Approach**: 고유하고 완전한 결정 수열 표현을 생성하기 위해 (1) Niggli 셀 축약으로 SO(3) 동변적(equivariant) 단위 셀 결정, (2) 이를 SE(3) 불변 수열로 변환하는 두 단계 접근 방식 제시.

## Achievement

![Figure 1](figures/fig1.webp)
*CIF 파일 기반 방법의 한계: 동일 결정이 주기적 변환에 따라 서로 다른 CIF 파일로 표현되는 문제*

1. **고유한 수열 표현 달성**: Mat2Seq은 동일한 결정 구조와 그 등가 표현들을 모두 단일 고유 수열로 매핑하여 데이터 증강 없이 불변성 보장

2. **수학적 엄밀성**: SE(3) 불변성, 주기성 불변성, 완전성(completeness)의 세 가지 요구사항을 형식적으로 정의하고 이를 만족함을 증명

3. **언어 모델 통합의 유효성**: Mat2Seq 기반 토크나이제이션을 통해 언어 모델이 결정 구조 생성 및 조건부 생성(속성 기반) 작업에서 경쟁력 있는 성능 달성

## How

- **Step 1 - SO(3) 동변적 단위 셀 결정**:
  - Niggli 셀 축약(Niggli cell reduction)을 사용하여 임의의 원시 셀에서 세 개의 가장 짧은 비-평면 벡터로 구성된 고유한 격자 벡터 도출
  - 여섯 개의 격자 매개변수(세 변의 길이와 세 각도)로 표현하여 SO(3) 동변성 확보

- **Step 2 - 원시 단위 셀(primitive unit cell) 결정**:
  - Niggli 축약된 격자 벡터 내에서 원자 위치를 정규화하고, 원시 셀의 기저 벡터를 도출하여 중복 원자 제거

- **Step 3 - SE(3) 불변 수열 변환**:
  - 결정된 원시 셀의 원자 종류(atomic species), 원자 위치(fractional coordinates), 격자 벡터를 체계적으로 인코딩하여 위치/회전 불변 특징 추출
  - 예: 원자 간 거리 행렬, 각도 정보 등의 기하학적 불변량 활용

- **Step 4 - 어휘 생성 및 토크나이제이션**:
  - 추출된 기하학적 특징들을 정량화하여 미리 정의된 어휘(vocabulary)의 토큰으로 변환
  - 언어 모델이 이해할 수 있는 수열 형식으로 표현

## Originality

- **개념적 혁신**: 결정 구조의 무한성(주기성)과 SE(3) 불변성을 동시에 보장하는 첫 번째 체계적 토크나이제이션 방법. 기존 CIF 기반 접근의 근본적 한계를 수학적으로 정의하고 해결

- **수학적 엄밀성**: "단위 셀 SE(3) 불변성"과 "주기성 불변성"의 형식적 정의(Definition 1, 2)와 이에 대한 증명을 제공하여 이론적 기초 구축

- **Niggli 셀 활용의 확장**: 전통적 결정학 도구인 Niggli 축약을 언어 모델 시대에 맞게 재해석하여 고유한 단위 셀 선택의 이론적 근거 제시

- **데이터 증강 제거**: 고유한 수열 표현으로 인해 동일 결정의 모든 등가 표현이 자동으로 동일 확률을 가져 광범위한 데이터 증강 불필요

## Limitation & Further Study

- **계산 복잡도**: Niggli 셀 축약 및 원시 셀 결정 과정의 계산 비용이 대규모 데이터셋 처리 시 병목이 될 수 있으며, 이에 대한 최적화 논의 부족

- **토크나이제이션 정보 손실**: 3D 기하학적 정보를 1D 수열로 변환하는 과정에서 미세한 기하학적 세부사항(예: 원자 간의 특정 배치)이 손실될 가능성 미탐색

- **비주기 시스템 미지원**: 표면(surface), 계면(interface) 등 비주기적 구조나 부분적 주기성 시스템으로의 확장 가능성 제시 부족

- **생성 모델의 안정성**: 생성된 결정 구조의 물리적 안정성(thermodynamic stability) 검증 및 실제 합성 가능성에 대한 평가 심화 필요

- **비교 연구**: 동일한 기준 하에서 기존 기하학적 생성 모델(DiffCSP, MatterGen)과의 정량적 비교 분석 추가 필요


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 3.5/5
- Overall: 4.1/5

**총평**: Mat2Seq은 결정 물질의 언어 모델 기반 생성이라는 새로운 분야에서 불변성과 고유성의 근본적 수학적 문제를 처음으로 체계적으로 정의하고 해결하는 의미 있는 기여를 한다. Niggli 셀 축약을 활용한 접근은 우아하고 이론적으로 견고하며, 데이터 증강 제거라는 실질적 이점을 제공한다. 다만 구체적 알고리즘 상세도 및 광범위한 생성 성능 비교 실험 보강이 있으면 영향력 있는 표준 방법론으로 자리 잡을 수 있을 것으로 예상된다.

## Related Papers

- 🔄 다른 접근: [[papers/487_Leveraging_biomolecule_and_natural_language_through_multi-mo/review]] — 결정 구조 vs 생물분자로 대상은 다르지만 동일한 다중모달 토큰화 접근법
- 🧪 응용 사례: [[papers/1104_A_Physics-Informed_Chemical_Rule_for_Topological_Materials_D/review]] — 결정 구조 토큰화를 위상 물질 발견에 적용한 구체적인 응용 사례
- 🏛 기반 연구: [[papers/349_Fragment_and_Geometry_Aware_Tokenization_of_Molecules_for_St/review]] — 분자의 기하학적 토큰화 연구가 결정 구조 불변 토큰화의 방법론적 기초
- 🔗 후속 연구: [[papers/383_Geometry_Informed_Tokenization_of_Molecules_for_Language_Mod/review]] — 분자 기하학 토큰화를 결정 구조의 SE(3) 불변성으로 확장한 발전된 연구
- 🔄 다른 접근: [[papers/487_Leveraging_biomolecule_and_natural_language_through_multi-mo/review]] — 생물분자 vs 결정 구조로 대상은 다르지만 동일한 다중모달 토큰화 접근법
- 🔗 후속 연구: [[papers/383_Geometry_Informed_Tokenization_of_Molecules_for_Language_Mod/review]] — 결정체 재료의 불변 토큰화에서 3D 분자 기하학 토큰화로의 확장
- 🔗 후속 연구: [[papers/125_Automated_latex_code_generation_from_handwritten_math_expres/review]] — 결정 물질의 불변 토크나이제이션 기법이 필기 수학식 이미지의 구조적 표현 학습에 적용될 수 있다.
- 🏛 기반 연구: [[papers/1104_A_Physics-Informed_Chemical_Rule_for_Topological_Materials_D/review]] — 결정 구조의 불변 토큰화가 위상 물질 발견 규칙의 구조적 인코딩 기반
