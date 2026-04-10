---
title: "345_Foundation_Molecular_Grammar_Multi-Modal_Foundation_Models_I"
authors:
  - "Michael Sun"
  - "Weize Yuan"
  - "Gang Liu"
  - "Wojciech Matusik"
  - "Jie Chen"
date: "2025"
doi: "10.48550/arXiv.2505.22948"
arxiv: ""
score: 4.1
essence: "다중 모달 기반 모델(MMFM)의 화학 지식을 활용하여 분자를 이미지와 텍스트로 표현하고, 계층적 분해 알고리즘과 연쇄 추론(chain-of-thought)을 결합해 해석 가능한 분자 그래프 문법(graph grammar)을 자동으로 학습하는 프레임워크를 제안한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Multimodal_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Sun et al._2025_Foundation Molecular Grammar Multi-Modal Foundation Models Induce Interpretable Molecular Graph Lan.pdf"
---

# Foundation Molecular Grammar: Multi-Modal Foundation Models Induce Interpretable Molecular Graph Languages

> **저자**: Michael Sun, Weize Yuan, Gang Liu, Wojciech Matusik, Jie Chen | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2505.22948](https://doi.org/10.48550/arXiv.2505.22948)

---

## Essence

![Figure 1](figures/fig1.webp)
*주요 FMG 알고리즘 모듈: 기저 클리크 추출부터 근 모티프 선택까지의 단계적 프로세스. MMFM이 의미 있는 부분구조 병합과 화학적 중요도 판단을 수행.*

다중 모달 기반 모델(MMFM)의 화학 지식을 활용하여 분자를 이미지와 텍스트로 표현하고, 계층적 분해 알고리즘과 연쇄 추론(chain-of-thought)을 결합해 해석 가능한 분자 그래프 문법(graph grammar)을 자동으로 학습하는 프레임워크를 제안한다.

## Motivation

- **Known**: 최근 데이터 효율적 분자 생성 방법들이 그래프 문법을 활용하여 해석성을 도입하고 있으나, 기존 문법 학습은 전문가 주석 또는 신뢰도 낮은 휴리스틱에 의존
  
- **Gap**: MMFM(GPT-4o 등)의 강력한 이미지 및 자연언어 이해 능력이 분자 발견에 충분히 활용되지 못했으며, 체계적인 문법 유도 알고리즘 부재

- **Why**: RDKit 같은 표준화된 분자 렌더링 API가 보편화되어 MMFM이 분자 이미지를 학습했을 가능성이 높고, 이를 활용한 구조적 접근이 필요

- **Approach**: 클리크 트리 분해(clique tree decomposition) 알고리즘을 기반으로 각 단계마다 MMFM의 의사결정 모듈을 통합하고, LLM 논쟁(debate) 메커니즘으로 화학적 타당성을 검증

## Achievement

![Figure 1](figures/fig1.webp)
*FMG 파이프라인: (좌) 기저 클리크 초기화, (중좌) 클리크 그래프 삼각분할, (중앙) MMFM 기반 모티프 병합 결정, (중우) 중요도 낮은 상호작용 제거, (우) 근 모티프 선택.*

1. **데이터 효율성 및 다양성**: 기존 SOTA 방법 대비 분자 생성 벤치마크에서 우수한 성능 달성 (합성 가능성, 다양성, 데이터 효율성 모두 개선)

2. **내재적 해석성**: 생성된 문법 규칙이 관능기(functional groups) 등 화학적으로 의미 있는 부분구조로 구성되며, 단계별 추론 과정을 "설계 내러티브(design narrative)"로 기록하여 투명성 확보

3. **전문가 검증**: LLM 판사 및 토너먼트 시스템을 통해 분해(decomposition)의 화학적 타당성을 자동 검증하고, 전문가 기준 레이블과 비교 검증

## How

![Figure 1](figures/fig1.webp)

**알고리즘 단계:**

1. **기저 클리크 추출(Base Clique Extraction)**
   - 분자 구조를 하이퍼그래프로 변환 (노드=결합, 하이퍼엣지=원자 공유 관계 및 최소 고리)
   - 분자 클리크 그래프 생성 (최대 클리크 추출)

2. **클리크 그래프 삼각분할(Triangulation)**
   - 유효한 클리크 트리 존재 보장

3. **모티프 병합(Motif Merging)** - MMFM 개입 지점 1
   - 기저 클리크들을 이미지로 시각화
   - MMFM에 "어떤 쌍을 병합하여 화학적으로 의미 있는 부분구조를 형성할 것인가?"라고 질문
   - 연쇄 추론으로 기능기(ester 그룹, 아크릴레이트 등) 식별

4. **스패닝 트리 엣지 선택(Spanning Tree Construction)** - MMFM 개입 지점 2
   - 클리크 그래프의 사이클 제거
   - MMFM에 "가장/최소 중요한 상호작용은 무엇인가?"라고 질문
   - 화학적 중요도 기반 엣지 제거

5. **근 모티프 선택(Root Motif Selection)** - MMFM 개입 지점 3
   - 파스 트리의 근(root)으로 가장 중요한 모티프 선택
   - 최종 클리크 트리 완성

6. **HRG 변환**
   - 클리크 트리를 초엣지 대체 문법(Hyperedge Replacement Grammar)으로 변환
   - 각 모-자 관계가 생성 규칙이 됨

**프롬프팅 전략:**
- 분자 이미지와 텍스트 설명을 동시에 제시하여 다중 모달 정렬(implicit alignment)
- 주석이 달린 이미지로 중간 변수 시각화
- LLM 토너먼트: 여러 분해 방안을 LLM 판사로 평가하여 최고 품질 선택

## Originality

- **최초의 MMFM 기반 자동 분자 문법 유도**: 전문가 주석과 휴리스틱 필요성 제거

- **클리크 트리 분해 + MMFM 통합**: 견고한 그래프 이론 기반(NP-난제이지만 실용적 알고리즘)을 MMFM의 적응형 의사결정과 결합

- **다중 모달 프롬프팅 기법**: 분자 이미지 렌더링과 자연언어 설명을 창의적으로 활용한 in-context alignment

- **설계 내러티브**: 추론 과정을 명시적으로 저장하여 결정의 투명성 및 검증 가능성 보장

- **LLM 기반 자동 검증**: 전문가 개입 없이도 화학적 타당성 판단 메커니즘 제안

## Limitation & Further Study

- **MMFM 신뢰도**: GPT-4o 같은 특정 모델에 의존하며, 더 작은 모델이나 특화 분자 모델의 성능 미검증

- **스케일 검증**: 대규모 분자 라이브러리(예: 백만 개 이상)에 대한 계산 효율성 및 성능 미평가

- **화학적 중요도의 정의**: "중요한 상호작용"의 정의가 MMFM의 학습 데이터에 암묵적으로 의존하며, 특정 응용(약물 설계, 고분자 등)에서의 편향 가능성

- **후속 연구**:
  - 다양한 기초 모델(Gemini, Claude 등) 벤치마킹
  - 도메인 특화 분자 모델의 미세 조정(fine-tuning) 가능성 탐색
  - 특정 화학 작업(반응성, 합성 경로)에 최적화된 문법 학습
  - 분자 성질 예측 태스크로의 확대 적용

## Evaluation

- **Novelty**: 4.5/5
  - MMFM을 구조적 문법 유도에 처음 적용하고, 다중 모달 프롬프팅의 창의적 활용이 돋보임
  - 다만 기본 알고리즘(클리크 트리)은 기존 것이고, MMFM의 사용도 완전히 새로운 개념은 아님

- **Technical Soundness**: 4/5
  - 클리크 트리 분해의 수학적 기초가 견고하고 알고리즘 단계가 명확
  - MMFM 의사결정의 일관성과 반복성에 대한 이론적 보장 부족
  - 실험 검증 충분하나 대규모 데이터셋 평가 미흡

- **Significance**: 4/5
  - 자동화된 해석 가능 분자 문법 학습은 실무적 가치 높음
  - 분자 발견 워크플로우에 즉시 적용 가능한 실용성
  - 다만 기존 SOTA 방법과의 성능 차이 검증 필요 및 범용성 입증 추가 필요

- **Clarity**: 4/5
  - 알고리즘 흐름과 프롬프팅 전략이 구체적으로 설명됨
  - Figure 1의 시각화가 명확함
  - 수학적 표기(하이퍼그래프, HRG)가 다소 복잡하여 중간 정도 배경지식 요구

- **Overall**: 4.1/5

**총평**: 
본 논문은 다중 모달 기초 모델의 화학 이해 능력을 구조적 그래프 문법 유도에 창의적으로 활용한 우수한 논문이다. 전문가 주석 의존성을 제거하고 자동 검증 메커니즘을 제시함으로써 실무적 기여도가 높으나, MMFM의 일관성 이론적 보장과 대규모 검증이 보완되면 더욱 강력할 것으로 예상된다.

## Related Papers

- 🔗 후속 연구: [[papers/555_Molgan_An_implicit_generative_model_for_small_molecular_grap/review]] — MolGAN의 분자 생성 결과를 Foundation Molecular Grammar의 해석 가능한 문법 구조로 체계적으로 분석할 수 있음
- 🏛 기반 연구: [[papers/487_Leveraging_biomolecule_and_natural_language_through_multi-mo/review]] — 생체분자와 자연어의 멀티모달 결합 방법론이 분자 이미지와 텍스트 표현 통합의 핵심 기반이 됨
- 🔗 후속 연구: [[papers/383_Geometry_Informed_Tokenization_of_Molecules_for_Language_Mod/review]] — 분자의 기하학적 토큰화 방법이 Foundation Molecular Grammar의 계층적 분해 알고리즘을 더욱 정교화함
- 🔄 다른 접근: [[papers/487_Leveraging_biomolecule_and_natural_language_through_multi-mo/review]] — 분자 문법 기반 파운데이션 모델과 생물분자 다중모달 학습의 대조적 방법론
- 🔗 후속 연구: [[papers/349_Fragment_and_Geometry_Aware_Tokenization_of_Molecules_for_St/review]] — 멀티모달 분자 문법 기초 모델이 프래그먼트 기반 분자 토큰화 방법을 더 포괄적으로 확장할 수 있습니다.
- 🔗 후속 연구: [[papers/555_Molgan_An_implicit_generative_model_for_small_molecular_grap/review]] — Foundation Molecular Grammar의 해석 가능한 분자 문법이 MolGAN의 생성 결과를 체계적으로 분석하는 도구로 활용됨
