---
title: "383_Geometry_Informed_Tokenization_of_Molecules_for_Language_Mod"
authors:
  - "Xiner Li"
  - "Limei Wang"
  - "Youzhi Luo"
  - "Carl N. Edwards"
  - "Shurui Gui"
date: "2024"
doi: "10.48550/arXiv.2408.10120"
arxiv: ""
score: 4.0
essence: "본 논문은 3D 분자 구조를 SE(3)-불변(invariant) 1D 이산 수열로 변환하는 Geo2Seq 토큰화 방법을 제안하여, 언어 모델(LM)이 3D 분자 생성 태스크를 효과적으로 수행할 수 있도록 한다. 기존의 확산 모델 기반 방법론보다 빠르면서도 더 나은 조건부 생성 성능을 달성한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/3D_Molecular_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Li et al._2024_Geometry Informed Tokenization of Molecules for Language Model Generation.pdf"
---

# Geometry Informed Tokenization of Molecules for Language Model Generation

> **저자**: Xiner Li, Limei Wang, Youzhi Luo, Carl N. Edwards, Shurui Gui | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2408.10120](https://doi.org/10.48550/arXiv.2408.10120)

---

## Essence

![Figure 1](figures/fig1.webp) *Geo2Seq 개요: 정규 표준화 라벨링 순서로 노드를 배열하고 각 노드에 원자 종류와 구면 좌표를 벡터 형태로 채워 수열로 변환*

본 논문은 3D 분자 구조를 SE(3)-불변(invariant) 1D 이산 수열로 변환하는 Geo2Seq 토큰화 방법을 제안하여, 언어 모델(LM)이 3D 분자 생성 태스크를 효과적으로 수행할 수 있도록 한다. 기존의 확산 모델 기반 방법론보다 빠르면서도 더 나은 조건부 생성 성능을 달성한다.

## Motivation

- **Known**: 언어 모델은 자연언어처리(NLP)에서 뛰어난 성능을 보이며, SMILES나 SELFIES 같은 표현으로 2D 분자 생성에도 성공적으로 적용되었다.
- **Gap**: 3D 분자 생성 문제에 대해 언어 모델을 직접 적용한 연구는 거의 없다. 기존 확산 모델 방식들은 수천 단계의 확산 스텝이 필요하여 생성 시간이 길다.
- **Why**: 3D 기하학적 정보는 분자의 성질(예: 원자별 힘, 에너지)을 결정하는 데 결정적이므로, 2D 그래프만으로는 불충분하다. SE(3) 변환(회전, 병진)에 대해 불변인 표현이 필수적이다.
- **Approach**: 분자의 3D 좌표를 SE(3)-불변 구면 좌표(spherical coordinates)로 변환하고, 정규 표준화 라벨링(canonical labeling)을 통해 순서를 결정하여 1D 이산 수열로 인코딩한다.

## Achievement

![Figure 3](figures/fig3.webp) *편극율(Polarizability α) 조건으로 생성된 분자의 시각화*

![Figure 4](figures/fig4.webp) *QM9 데이터셋에서 Geo2Seq + Mamba로 생성된 분자의 시각화*

1. **생성 품질 및 다양성**: Geo2Seq을 다양한 언어 모델(Transformer, Mamba 등 SSM)과 결합하여 화학적으로 유효하고 다양한 3D 분자를 신뢰성 있게 생성할 수 있음을 입증

2. **조건부 생성 성능**: 조건부 생성(conditional generation) 태스크에서 강력한 확산 모델 기저선(EDM 등)을 큰 차이로 초과 달성

3. **효율성**: 확산 모델 대비 훨씬 빠른 생성 속도(자동회귀 디코딩)를 유지하면서 더 나은 성능 제공

## How

![Figure 1](figures/fig1.webp) *Geo2Seq의 핵심 단계: 정규 표준화 라벨링, 구면 좌표 표현, 토큰화, 수열 생성*

- **정규 표준화 라벨링(Canonical Labeling)**: 그래프 동형(isomorphism)을 제외한 정보 손실 없이 분자 그래프의 노드를 고정된 순서로 배열
  
- **구면 좌표 표현**: 각 원자를 `[z_i, d_i, θ_i, φ_i]`로 표현 (z_i: 원자번호, d_i: 거리, θ_i, φ_i: 각도)
  - 이전 원자로부터의 거리와 각도만 사용하므로 자동으로 SE(3)-불변 성질 획득
  - 전역 기준 프레임(global equivariant frame)을 설정하여 회전과 평진에 대해 불변

- **토큰화 및 수열화**: 각 원자의 정보를 연속 벡터로 인코딩하고, 양자화(quantization)를 통해 이산 토큰으로 변환

- **조건부 생성 확장**: 양자 성질(quantum properties) 값을 수열에 포함시켜 LM의 장거리 문맥 의존성(long-context correlation) 활용

- **생성**: 자동회귀 디코딩으로 토큰을 순차적으로 샘플링하고, Top-K 및 온도(temperature) 하이퍼파라미터로 다양성 제어

## Originality

- **SE(3)-불변 토큰화 설계**: 분자 기하학을 직접 1D 수열로 인코딩하면서 회전/병진 불변성을 보장하는 방법론의 참신함

- **모델-불가지론적(Model-agnostic) 접근**: Geo2Seq이 입력 데이터에만 작동하므로, 다양한 LM 아키텍처(Transformer, SSM/Mamba 등)와 조합 가능

- **3D 분자 생성에 순수 언어 모델 적용**: 기존 연구들이 GNN이나 기하학적 모듈을 병렬 또는 추가로 포함한 반면, 순수 LM 기반 접근의 가능성 입증

- **조건부 생성의 우수성**: 장거리 의존성 학습에 우수한 LM 특성을 활용하여 양자 성질 조건부 생성에서 확산 모델 초과 달성

## Limitation & Further Study

- **양자화 손실**: 연속 좌표를 이산 토큰으로 변환하는 과정에서 정밀도 손실이 발생하며, 최적 양자화 레벨에 대한 상세한 분석 부족

- **수열 길이**: 분자 크기가 커질수록 수열 길이가 증가하여 언어 모델의 컨텍스트 윈도우 제약에 직면할 수 있음

- **기하학적 제약 미실장**: 물리적으로 타당한 분자 기하학(예: 결합 각도 범위, 입체 장애)에 대한 명시적 제약이 토큰화 단계에 포함되지 않음

- **정규 표준화의 계산 복잡도**: 그래프 동형 판정의 NP-hardness 특성상, 매우 큰 분자에 대해 정규 표준화 계산이 병목이 될 수 있음

- **후속 연구 방향**: 
  - 더 큰 분자 데이터셋(GEOM 등)에 대한 확장성 검증
  - 에너지, 반응성 등 추가 양자 성질 조건부 생성 평가
  - 다른 기하학적 표현(예: 상대 좌표) 비교 분석

## Evaluation

- **Novelty**: 4/5
  - 3D 분자 생성에 순수 LM 적용과 SE(3)-불변 토큰화는 충분히 참신함. 다만 구면 좌표 표현 자체는 기존 화학 분야에서 널리 사용된 개념

- **Technical Soundness**: 4/5
  - 정규 표준화와 구면 좌표 기반 SE(3)-불변성 보장은 수학적으로 타당함. 다만 양자화 손실과 정규 표준화 복잡도에 대한 상세 논의 부족

- **Significance**: 4/5
  - 3D 분자 생성의 새로운 패러다임을 제시하고 조건부 생성에서 경험적 성공을 달성. 약물 발견 및 재료 과학 응용 가능성이 높음

- **Clarity**: 4/5
  - 전체 흐름과 방법론이 명확하게 설명됨. 다만 몇몇 기술적 세부사항(예: 전역 기준 프레임 설정 방식)에 대한 추가 설명 필요

- **Overall**: 4/5

**총평**: 본 논문은 언어 모델을 3D 분자 생성에 효과적으로 적용하기 위한 창의적인 토큰화 방법을 제안하며, SE(3)-불변성을 엄밀히 보장하면서도 조건부 생성에서 확산 모델을 초과하는 성능을 달성한다. 모델-불가지론적 설계로 확장성도 우수하나, 수치 정밀도와 계산 복잡도 측면의 실용적 제약에 대한 더 깊은 논의가 필요하다.

## Related Papers

- 🧪 응용 사례: [[papers/459_Language_Models_for_Controllable_DNA_Sequence_Design/review]] — 제어 가능한 DNA 서열 설계를 3D 분자 토큰화에 언어모델로 적용
- 🔗 후속 연구: [[papers/439_Invariant_Tokenization_of_Crystalline_Materials_for_Language/review]] — 결정체 재료의 불변 토큰화에서 3D 분자 기하학 토큰화로의 확장
- 🔄 다른 접근: [[papers/349_Fragment_and_Geometry_Aware_Tokenization_of_Molecules_for_St/review]] — 구조화된 표현을 위한 분자 조각과 기하학 토큰화의 다른 접근법
- 🏛 기반 연구: [[papers/230_Code_llama_Open_foundation_models_for_code/review]] — 코드용 오픈 파운데이션 모델이 분자 언어모델 생성의 기반 제공
- 🔗 후속 연구: [[papers/439_Invariant_Tokenization_of_Crystalline_Materials_for_Language/review]] — 분자 기하학 토큰화를 결정 구조의 SE(3) 불변성으로 확장한 발전된 연구
- 🔄 다른 접근: [[papers/349_Fragment_and_Geometry_Aware_Tokenization_of_Molecules_for_St/review]] — 구조 기반 약물 설계에서 SE(3) 좌표계와 기하학적 토큰화 접근법을 비교할 수 있습니다.
- 🔗 후속 연구: [[papers/345_Foundation_Molecular_Grammar_Multi-Modal_Foundation_Models_I/review]] — 분자의 기하학적 토큰화 방법이 Foundation Molecular Grammar의 계층적 분해 알고리즘을 더욱 정교화함
- 🔄 다른 접근: [[papers/282_DMFlow_Disordered_Materials_Generation_by_Flow_Matching/review]] — 언어모델 분자 생성과 무질서 재료 생성의 다른 생성 모델 접근법
- 🔄 다른 접근: [[papers/125_Automated_latex_code_generation_from_handwritten_math_expres/review]] — 둘 다 분자 및 수학적 구조의 언어 모델 토크나이제이션을 다루지만 하나는 필기 수학식의 LaTeX 변환에, 다른 하나는 분자의 기하학적 토크나이제이션에 초점을 맞춘다.
