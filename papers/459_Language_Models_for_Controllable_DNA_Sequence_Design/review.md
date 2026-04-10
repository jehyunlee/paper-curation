---
title: "459_Language_Models_for_Controllable_DNA_Sequence_Design"
authors:
  - "Xingyu Su"
  - "Xiner Li"
  - "Yu-Ching Lin"
  - "Ziqian Xie"
  - "Degui Zhi"
date: "2025"
doi: "10.48550/arXiv.2507.19523"
arxiv: ""
score: 4.0
essence: "ATGC-Gen은 트랜스포머 기반 언어 모델을 활용하여 생물학적 특성(세포 타입, 전사인자 결합 등)을 조건으로 하는 제어 가능한 DNA 서열 생성을 수행하는 프레임워크이다. 교차 모달 인코딩을 통해 다양한 생물학적 신호를 통합하여 기능적이고 다양한 DNA 서열을 생성한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/3D_Molecular_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Su et al._2025_Language Models for Controllable DNA Sequence Design.pdf"
---

# Language Models for Controllable DNA Sequence Design

> **저자**: Xingyu Su, Xiner Li, Yu-Ching Lin, Ziqian Xie, Degui Zhi | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2507.19523](https://doi.org/10.48550/arXiv.2507.19523)

---

## Essence

ATGC-Gen은 트랜스포머 기반 언어 모델을 활용하여 생물학적 특성(세포 타입, 전사인자 결합 등)을 조건으로 하는 제어 가능한 DNA 서열 생성을 수행하는 프레임워크이다. 교차 모달 인코딩을 통해 다양한 생물학적 신호를 통합하여 기능적이고 다양한 DNA 서열을 생성한다.

## Motivation

- **Known**: 최근 확산 모델(diffusion model)과 흐름 매칭(flow matching)을 기반한 DNA 생성 방법들이 전역 구조 모델링에서 우수한 성능을 보이고 있다. 또한 DNABERT, Nucleotide Transformer 등의 DNA 언어 모델이 예측 및 표현 학습에서 강력한 능력을 입증했다.

- **Gap**: 기존 확산/흐름 기반 방법들은 이산적이고 가변 길이 서열 생성에 자연스럽게 설계되지 않았다. 또한 DNA 언어 모델들은 주로 인코딩과 예측에 초점을 두었으며, 명시적인 제어 가능한 서열 설계는 미흡하다. 각 조건마다 별도의 모델 학습이 필요했다.

- **Why**: 실제 DNA 설계 응용에서는 특정 단백질 결합, 전사 활성화 등 구체적인 생물학적 성질을 만족하는 서열이 필요하며, 다양한 생물학적 특성을 통합적으로 처리할 수 있는 단일 프레임워크의 필요성이 있다.

- **Approach**: 트랜스포머 기반 언어 모델에 교차 모달 조건 인코딩을 통합하여, 이산적 서열 생성의 자연스러운 특성과 다중 생물학적 신호 처리를 동시에 달성한다.

## Achievement

1. **ATGC-Gen 프레임워크 개발**: 디코더 전용(GPT 스타일)과 인코더 전용(BERT 스타일) 트랜스포머 아키텍처 모두를 지원하는 통합 프레임워크로, 자동회귀 및 마스크 복구 목표 함수를 유연하게 적용 가능하다.

2. **새로운 ChIP-Seq 기반 데이터셋**: 단백질-DNA 결합 패턴을 포착하는 ChIP-Seq 실험 기반 데이터셋을 도입하여 복잡한 생물학적 맥락에서의 생성 능력을 평가하는 벤치마크를 제시한다.

3. **종합적 평가 및 우수한 성능**: 프로모터(promoter), 인핸서(enhancer), ChIP-Seq 기반 작업에서 기존 방법들을 능가하는 제어성(controllability), 기능성(functionality), 유동성(fluency), 다양성(diversity)을 입증한다.

## How

ATGC-Gen은 다음과 같은 구조로 작동한다:

- **표현 인코딩(Representation Encoding)**: 서열 수준 통합(Sequence-level integration)을 통해 세포 타입, 풀링된 통계 등 전역적 생물학적 맥락을 인코딩하고, 단백질 서열 같은 추가 생물학적 정보도 인코딩한다.

- **교차 모달 조건화**: 생물학적 특성 임베딩을 DNA 서열 임베딩과 교차 주의(cross-attention) 메커니즘을 통해 통합하여, 모델이 조건에 맞는 서열을 생성하도록 지도한다.

- **훈련 목표 함수**: 
  - 디코더 전용: 표준 자동회귀 언어 모델링 손실(causal language modeling loss)
  - 인코더 전용: 마스크된 토큰 복구 목표(masked token recovery objective)로 양방향 처리를 통해 서열과 조건 정보 간의 상호작용을 강화한다.

- **생성 과정**: 조건 표현이 주입된 상태에서 자동회귀적으로 또는 반복적 마스크 복구를 통해 기능적 DNA 서열을 생성한다.

## Originality

- **첫 번째 본격적 시도**: DNA 서열 생성에 대한 언어 모델 적용이 상대적으로 미흡했던 가운데, 이를 체계적으로 탐구하고 실용적 프레임워크를 제시한 첫 주요 연구이다.

- **교차 모달 통합 설계**: 단순한 조건 결합이 아닌 구조화된 교차 모달 인코딩을 통해 이질적 생물학적 신호(세포 타입, 단백질 서열, 조절 신호)를 통합하는 설계 관점의 독창성이 있다.

- **유연한 아키텍처 지원**: 동일 프레임워크 내에서 디코더 전용과 인코더 전용 두 가지 트랜스포머 패러다임을 모두 지원하여 다양한 생성 목표에 적응 가능하다.

- **새로운 벤치마크**: 기존 프로모터/인핸서 작업을 넘어 ChIP-Seq 기반 단백질-DNA 결합 특이성 모델링이라는 새로운 평가 과제를 도입한다.

## Limitation & Further Study

- **길이 제약**: 현재 프레임워크에서 처리 가능한 DNA 서열 길이가 제한적이며, 매우 긴 조절 영역이나 게놈 규모의 설계에 대한 확장성 평가가 부족하다.

- **조건 복잡도**: 현재 다루는 조건들(세포 타입, 단백질 결합 등)이 상대적으로 단순하며, 다중 상충하는 조건이나 계층적 생물학적 제약을 동시에 만족하는 경우의 성능은 검토되지 않았다.

- **생물학적 검증 부족**: 생성된 서열의 생물학적 기능성이 주로 계산학적 메트릭으로 평가되었으며, 실제 세포 실험을 통한 검증이 제시되지 않았다.

- **후속 연구**: (1) 초장 서열 처리를 위한 효율적 아키텍처 적용(예: Mamba, HyenaDNA 기반 변형), (2) 실험적 검증 파이프라인 구축, (3) 상호 모순적 설계 목표의 파레토 최적해 탐색 방법론 개발.

## Evaluation

- **Novelty**: 4/5 — DNA 생성에 언어 모델을 체계적으로 적용하고 교차 모달 조건화를 도입한 점에서 신선하지만, 기본 아키텍처는 기존 트랜스포머의 직접 적용이다.

- **Technical Soundness**: 4/5 — 전반적으로 설계가 명확하고 다양한 배경을 가진 데이터셋에서 일관된 성능을 보이나, 방법론의 기술적 혁신성(새로운 손실 함수, 정규화 기법 등)은 제한적이다.

- **Significance**: 4/5 — 계산 생물학과 합성 생물학 분야에 실용적 가치를 제공하며, 새로운 벤치마크는 향후 연구의 기초가 될 수 있다. 다만 실제 실험적 임팩트는 아직 미지수이다.

- **Clarity**: 4/5 — 대체로 명확하게 작성되었으나, 교차 주의 메커니즘의 세부 구현과 초매개변수 선택 근거에 대한 설명이 간결하다.

- **Overall**: 4/5

**총평**: 본 논문은 DNA 서열 설계라는 중요한 생물학적 문제에 트랜스포머 언어 모델을 체계적으로 적용하고, 교차 모달 조건화를 통해 다양한 생물학적 신호를 통합하는 실용적 프레임워크를 제시한다. 새로운 ChIP-Seq 벤치마크와 일관된 실험 결과는 강점이나, 실제 생물학적 검증과 방법론의 기술적 깊이 측면에서는 개선의 여지가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/472_Large_language_models_design_sequence-defined_macromolecules/review]] — 거대분자 설계를 위한 LLM 활용이라는 공통점이 있지만, DNA 서열 생성과 자기조립 구조 설계라는 다른 타겟을 다룬다.
- 🔗 후속 연구: [[papers/474_Large_language_models_for_zero-shot_inference_of_causal_stru/review]] — 생물학적 인과관계 추론 능력을 DNA 서열의 기능적 특성 예측과 설계에 활용할 수 있다.
- 🏛 기반 연구: [[papers/461_LARC_Towards_Human-level_Constrained_Retrosynthesis_Planning/review]] — 제약 조건 하에서의 역합성 계획 연구가 조건부 DNA 서열 생성의 방법론적 기반을 제공한다.
- 🧪 응용 사례: [[papers/383_Geometry_Informed_Tokenization_of_Molecules_for_Language_Mod/review]] — 제어 가능한 DNA 서열 설계를 3D 분자 토큰화에 언어모델로 적용
- 🔄 다른 접근: [[papers/472_Large_language_models_design_sequence-defined_macromolecules/review]] — 언어 모델을 활용한 생체분자 설계라는 공통 주제이지만 거대분자 자기조립과 DNA 서열 설계로 응용 영역이 다르다.
