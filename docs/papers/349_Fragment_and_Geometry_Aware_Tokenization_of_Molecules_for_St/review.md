---
title: "349_Fragment_and_Geometry_Aware_Tokenization_of_Molecules_for_St"
authors:
  - "Cong Fu"
  - "Xiner Li"
  - "Blake Olson"
  - "Heng Ji"
  - "Shuiwang Ji"
date: "2024"
doi: "arXiv:2408.09730"
arxiv: ""
score: 4.0
essence: "본 논문은 구조 기반 약물 설계(Structure-Based Drug Design, SBDD)를 위해 언어 모델(Language Models, LMs)을 활용하는 새로운 방법인 Frag2Seq를 제시한다. SE(3)-동변(equivariant) 좌표계를 통해 3D 분자 기하학 정보를 보존하면서 프래그먼트 기반 시퀀스로 변환하고, 단백질 포켓 임베딩을 교차 주의(cross-attention)로 통합하여 표적 단백질에 높은 결합 친화도를 가진 약물 유사 리간드를 효율적으로 생성한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Geometric_Prior_Learning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Fu et al._2024_Fragment and Geometry Aware Tokenization of Molecules for Structure-Based Drug Design Using Language.pdf"
---

# Fragment and Geometry Aware Tokenization of Molecules for Structure-Based Drug Design Using Language Models

> **저자**: Cong Fu, Xiner Li, Blake Olson, Heng Ji, Shuiwang Ji | **날짜**: 2024 | **DOI**: [arXiv:2408.09730](https://arxiv.org/abs/2408.09730)

---

## Essence

본 논문은 구조 기반 약물 설계(Structure-Based Drug Design, SBDD)를 위해 언어 모델(Language Models, LMs)을 활용하는 새로운 방법인 Frag2Seq를 제시한다. SE(3)-동변(equivariant) 좌표계를 통해 3D 분자 기하학 정보를 보존하면서 프래그먼트 기반 시퀀스로 변환하고, 단백질 포켓 임베딩을 교차 주의(cross-attention)로 통합하여 표적 단백질에 높은 결합 친화도를 가진 약물 유사 리간드를 효율적으로 생성한다.

## Motivation

- **Known**: 언어 모델은 자연어 처리와 다양한 분야에서 뛰어난 성능을 보이며, 확산 모델(diffusion models)보다 생성 효율이 우수하다. 프래그먼트 기반 생성은 원자 단위 생성보다 더 현실적인 부분구조를 생산할 수 있다.

- **Gap**: 기존의 자동회귀(autoregressive) 모델과 확산 모델 기반 SBDD 방법은 원자 단위 생성에만 집중하여 생성 단계가 많고, 프래그먼트 기반 언어 모델 적용은 미탐색 상태이다. 언어 모델을 분자의 3D 기하학 구조와 단백질-리간드 상호작용에 적응시키는 것이 도전적이다.

- **Why**: SBDD는 약물 개발에서 핵심적이지만, 복잡한 단백질-리간드 상호작용과 광활한 화학 공간으로 인해 여전히 도전적이다. 언어 모델의 강력한 패턴 학습 능력과 프래그먼트 기반 생성의 이점을 결합하면 더 효율적이고 효과적인 약물 설계가 가능할 수 있다.

- **Approach**: (1) 회전 가능한 결합을 잘라 3D 분자를 프래그먼트로 분해, (2) SE(3)-동변 좌표계를 구성하여 기하학 정보를 보존한 SE(3)-불변(invariant) 시퀀스 생성, (3) 역 폴딩 모델에서 추출한 단백질 포켓 임베딩을 교차 주의로 통합.

## Achievement

1. **바인딩 친화도 개선**: Vina 스코어에서 기준 모델들을 능가하며, QED와 Lipinski 준칙 준수율이 높아 약물 유사성이 우수한 리간드를 생성한다.

2. **생성 효율 극대화**: 원자 기반 자동회귀 및 확산 모델 대비 최대 약 300배의 속도 향상을 달성하여 단계적 생성의 이점을 입증한다.

## How

- **3D 분자 분해**: 다음 세 조건을 만족하는 회전 가능한 결합을 절단: (1) 고리 외부, (2) 단일 결합, (3) 양쪽 원자의 차수 > 1. 이는 기능기(functional groups)를 보존한다.

- **정준 순서(Canonical Order) 설정**: 정준 SMILES(Canonical SMILES) 표현에 따라 원자를 정렬하여 3D 분자 그래프 동형성(3D graph isomorphism)을 구별할 수 있는 완전하고 건전한 순서를 보장한다. **Lemma 3.2**: 두 3D 분자가 3D 동형 ⟺ 같은 정준 순서를 가짐.

- **SE(3)-동변 좌표계 구성**: 각 원자에 대해 이웃 원자의 위치와 기하학 정보를 이용해 국소 좌표계(local frame)를 설정. 이를 통해 분자를 회전·이동해도 시퀀스 표현은 불변이다.

- **SE(3)-불변 시퀀스 추출**: 각 프래그먼트의 상대 좌표, 방향, 원자 타입 정보를 담은 불변 시퀀스를 생성하여 언어 모델의 입력으로 사용.

- **단백질 조건 통합**: 사전 학습된 역 폴딩 모델(inverse folding model)에서 단백질 포켓의 임베딩을 추출하고, 교차 주의 메커니즘을 통해 언어 모델에 통합하여 표적 인식 분자 생성을 구현.

- **학습 및 생성 전략**: 다음 토큰 예측(next-token prediction) 손실로 학습하며, 생성 시에는 단백질 조건 하에서 프래그먼트를 순차적으로 생성.

## Originality

- **3D 기하학 정보 보존의 신규성**: SE(3)-동변·불변 개념을 활용하여 3D 분자 정보를 시퀀스 형태로 변환하면서 기하학 정보를 보존하는 것은 기존 언어 모델 기반 화학 방법들과 달리 명시적이고 수학적으로 견고하다.

- **프래그먼트 기반 언어 모델 최초 적용**: SBDD 분야에서 언어 모델을 프래그먼트 단위로 생성하는 데 적용한 것은 선례가 없다. 기존 작업들(TamGen, Lingo3DMol)은 SMILES 기반이거나 별도의 좌표 예측 단계가 필요하다.

- **이론적 근거 제공**: 3D 분자 그래프 동형성의 정의와 정준 순서의 완전성·건전성을 Lemma 3.2로 증명하여 순서 설정의 타당성을 수학적으로 보증한다.

- **통합 프레임워크**: 분자 분해, 시퀀스 변환, 단백질 조건 통합, 생성을 하나의 일관된 프레임워크로 구성하여 파이프라인의 복잡도를 줄였다.

## Limitation & Further Study

- **3D 동형성의 근사성**: 실제 분자 좌표는 노이즈와 반올림 오차를 포함하므로, 엄밀한 3D 동형성 대신 ϵ-제약 3D 동형성을 가정한다. ϵ 값의 선택이 모델 성능에 미치는 영향을 체계적으로 분석할 필요가 있다.

- **프래그먼트 분해 전략의 한계**: 회전 가능한 결합 절단 규칙은 휴리스틱(heuristic)이며, 화학적으로 의미 있는 더 다양한 프래그먼트 분해 방식의 탐색이 필요하다.

- **역 폴딩 모델 의존성**: 단백질 포켓 임베딩을 위해 사전 학습된 역 폴딩 모델에 의존하므로, 이 모델의 성능 한계가 전체 시스템에 영향을 미칠 수 있다. 단백질 표현 학습의 개선이 중요하다.

- **생성 평가의 확장**: 현재 바인딩 친화도, QED, Lipinski 준칙이 주요 평가 지표인데, 생체 이용률, 독성 예측, 신약성(novelty) 등 추가 약물학적 성질의 평가를 포함해야 한다.

- **대규모 실험의 필요성**: 더 다양한 단백질 표적과 화학 공간에서의 일반화 능력을 검증하고, 실험적 검증을 통한 교차 검증이 필요하다.

## Evaluation

| 항목 | 평가 |
|------|------|
| Novelty (독창성) | 4/5 |
| Technical Soundness (기술적 건전성) | 4/5 |
| Significance (중요성) | 4/5 |
| Clarity (명확성) | 3.5/5 |
| **Overall (종합)** | **4/5** |

**총평**: 본 논문은 SE(3)-동변 이론을 기반으로 3D 분자 기하학을 보존하면서 언어 모델을 SBDD에 최초로 프래그먼트 단위로 적용한 창의적인 접근이다. 수학적 근거(Lemma 3.2)와 높은 생성 효율(~300배 속도향상)은 강점이지만, 휴리스틱한 프래그먼트 분해 전략, 단백질 포켓 임베딩의 한계, 그리고 실험 검증의 범위가 제한적인 점은 개선이 필요하다. 향후 더 넓은 스펙트럼의 약물학적 성질 평가와 실험적 검증을 통해 임상 적용 가능성을 입증할 수 있다면 상당한 임팩트를 가질 수 있는 논문이다.

## Related Papers

- 🔄 다른 접근: [[papers/383_Geometry_Informed_Tokenization_of_Molecules_for_Language_Mod/review]] — 구조 기반 약물 설계에서 SE(3) 좌표계와 기하학적 토큰화 접근법을 비교할 수 있습니다.
- 🔗 후속 연구: [[papers/345_Foundation_Molecular_Grammar_Multi-Modal_Foundation_Models_I/review]] — 멀티모달 분자 문법 기초 모델이 프래그먼트 기반 분자 토큰화 방법을 더 포괄적으로 확장할 수 있습니다.
- 🏛 기반 연구: [[papers/555_Molgan_An_implicit_generative_model_for_small_molecular_grap/review]] — 소분자 그래프 생성을 위한 암시적 생성 모델이 구조 기반 분자 토큰화의 방법론적 기반을 제공합니다.
- 🏛 기반 연구: [[papers/439_Invariant_Tokenization_of_Crystalline_Materials_for_Language/review]] — 분자의 기하학적 토큰화 연구가 결정 구조 불변 토큰화의 방법론적 기초
- 🔄 다른 접근: [[papers/383_Geometry_Informed_Tokenization_of_Molecules_for_Language_Mod/review]] — 구조화된 표현을 위한 분자 조각과 기하학 토큰화의 다른 접근법
- 🏛 기반 연구: [[papers/811_Tikzero_Zero-shot_text-guided_graphics_program_synthesis/review]] — 분자의 기하학적 토크나이제이션 기법이 TikZ 그래픽 프로그램의 구조적 표현 학습에 응용될 수 있는 이론적 기반을 제공한다.
