---
title: "483_Learning_to_Discover_Regulatory_Elements_for_Gene_Expression"
authors:
  - "Xingyu Su"
  - "Haiyang Yu"
  - "Degui Zhi"
  - "Shuiwang Ji"
date: "2025"
doi: "10.48550/arXiv.2502.13991"
arxiv: ""
score: 4.25
essence: "본 논문은 DNA 서열과 에피지노믹 신호로부터 유전자 발현을 예측하되, 능동적으로 상호작용하는 조절 요소(regulatory elements)를 자동으로 발견하는 **Seq2Exp** 프레임워크를 제안한다. 정보 병목(information bottleneck) 원리를 활용하여 인과적 조절 요소만을 추출함으로써 기존 방법들을 능가하는 성능을 달성한다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Domain-specific_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Su et al._2025_Learning to Discover Regulatory Elements for Gene Expression Prediction.pdf"
---

# Learning to Discover Regulatory Elements for Gene Expression Prediction

> **저자**: Xingyu Su, Haiyang Yu, Degui Zhi, Shuiwang Ji | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2502.13991](https://doi.org/10.48550/arXiv.2502.13991)

---

## Essence

![Figure 1: Causal relationships between epigenomic signals, sequence, gene expression Y and related regulatory elements](figures/fig1.webp)
*그림 1: 에피지노믹 신호, DNA 서열, 유전자 발현 Y 및 관련 조절 요소 간의 인과관계*

본 논문은 DNA 서열과 에피지노믹 신호로부터 유전자 발현을 예측하되, 능동적으로 상호작용하는 조절 요소(regulatory elements)를 자동으로 발견하는 **Seq2Exp** 프레임워크를 제안한다. 정보 병목(information bottleneck) 원리를 활용하여 인과적 조절 요소만을 추출함으로써 기존 방법들을 능가하는 성능을 달성한다.

## Motivation

- **Known**: 
  - 최근 HyenaDNA, Caduceus 등 DNA 언어 모델이 유전자 발현 예측에 적용되고 있음
  - EPInformer 등은 DNA 서열과 에피지노믹 신호를 모두 활용하려는 시도가 있음

- **Gap**: 
  - 기존 DNA 언어 모델은 세포 유형별 차이를 반영하는 에피지노믹 신호를 간과함
  - EPInformer는 통계적 피크 검출(MACS3)에만 의존하여, DNA 서열과 신호 간의 복잡한 관계를 놓침
  - 장거리 상호작용(long-range interactions)과 희소한(sparse) 조절 요소 발견의 어려움

- **Why**: 
  - DNA 서열과 에피지노믹 신호는 생물학적 정보의 다른 측면을 포착
  - Hi-C/HiChIP은 물리적 상호작용 빈도, DNase-seq은 조절 요소의 기능 활성을 나타냄
  - 두 정보를 통합하면 예측 정확도 향상 가능

- **Approach**: 
  - 조절 요소(Rg), 측정된 조절 요소(Rm), 능동적으로 상호작용하는 요소(Rag)의 인과 관계 구조화
  - 정보 병목 기법으로 인과적 성분만 필터링하는 mask 학습

## Achievement

![Figure 2: Pipeline of proposed architectures. The input data contains the DNA sequence Xseq](figures/fig2.webp)
*그림 2: 제안된 아키텍처의 파이프라인*

1. **성능 우위**: 유전자 발현 예측에서 기존 베이스라인들(Enformer, GraphReg, EPInformer)을 능가하는 SOTA 성능 달성

2. **조절 요소 발견의 우수성**: 추출된 조절 요소 영역이 MACS3 같은 통계적 피크 검출 방법보다 더 정확하고 생물학적으로 의미 있는 영역 식별

3. **통합 프레임워크**: DNA 서열과 에피지노믹 신호를 체계적으로 결합하여 표준화된 방식으로 영향력 있는 영역 발견

## How

제안된 **Seq2Exp** 프레임워크는 다음과 같이 동작한다:

- **구조적 인과 모델(SCM) 기반**: Figure 1의 인과관계를 따라 설계
  - Xseq ← Rg: DNA 서열은 잠재적 조절 요소와 비인과적 부분으로 구성
  - Xsig → Rm: 에피지노믹 신호가 측정된 조절 요소를 나타냄
  - Rag → Y: 능동적 상호작용 요소만이 최종 유전자 발현에 영향

- **Mask 학습 분해**: 두 개의 독립적 mask 생성 경로
  - DNA 서열 기반 mask
  - 에피지노믹 신호 기반 mask
  - Beta 분포를 통한 확률 결합

- **정보 병목 적용**:
  ```
  L = I(Z; Y) - β·I(X; Z)
  ```
  - 최대 정보량 I(Z; Y): 대상 유전자 발현과의 상호정보량 최대화
  - 최소 정보량 제약: I(X; Z) ≤ Ic로 압축 강제
  - β 하이퍼파라미터로 압축-적관성 트레이드오프 조절

- **토큰 레벨 이진/소프트 mask**: 
  - 생성(Generator) 모듈에서 M ∈ {0,1} 또는 M ∈ [0,1] 학습
  - 예측(Predictor) 모듈에서 추출된 부분 서열로 발현값 예측

- **입력 처리**:
  - L = 200,000 bp (전사 시작점 중심)
  - 충분한 맥락정보 제공으로 장거리 상호작용 포착

## Originality

- **인과관계 명시화**: 단순히 예측하는 것이 아니라 Rg, Rm, Rag의 세 범주로 조절 요소를 분류하고 그 관계를 SCM으로 명시화

- **정보 병목의 생물학적 응용**: 기존 이미지/언어 분야의 IB 방법을 DNA 서열 분석에 처음 적용하여, 인과적 성분 필터링을 자동화

- **이중 신호 통합 메커니즘**: DNA 서열과 에피지노믹 신호로부터 각각 mask를 생성한 후 Beta 분포로 결합하는 통합 방식

- **최소 감독 학습**: 통계적 피크 검출에 의존하지 않고 end-to-end 학습으로 조절 요소 자동 발견

## Limitation & Further Study

- **계산 복잡도**: 200,000 bp 길이 서열 처리로 인한 계산 비용 미상세 기술 필요

- **생물학적 검증 부족**: 발견된 조절 요소의 실제 실험적 검증(ATAC-seq, ChIP-seq 수행) 제시 부재

- **세포 유형 일반화**: 특정 세포 유형에서의 성능 검증이 주이며, 세포 유형 간 전이 학습 가능성 미탐색

- **Beta 분포 선택의 정당성**: Beta 분포 사용 이유와 다른 분포와의 비교 실험 부족

- **긴 서열 모델링**: 200,000 bp 처리의 한계와 더 긴 상호작용 거리 처리 가능성 미논의

- **후속 연구 방향**:
  - 다양한 세포 유형 및 생물종으로의 확장
  - 실험적 검증을 통한 발견 조절 요소의 생물학적 타당성 확인
  - 3D 게놈 구조와의 명시적 통합
  - 마스킹 분해의 이론적 근거 강화

## Evaluation

- **Novelty** (독창성): 4.5/5
  - 인과관계 명시화와 정보 병목의 조합은 신선함
  - 다만 정보 병목 자체는 기존 기법이므로 부분 감점

- **Technical Soundness** (기술적 타당성): 4/5
  - SCM 기반 설명과 mask 학습 논리는 타당함
  - 정보 병목 하한(lower bound) 도출과정이 표준적 방식
  - Beta 분포 선택의 이론적 정당성 미흡

- **Significance** (의의): 4.5/5
  - 유전자 발현 예측의 실제 성능 향상 입증
  - 조절 요소 발견 자동화의 생물정보학적 가치 높음
  - 광범위한 임상 응용 잠재력

- **Clarity** (명확성): 4/5
  - 인과관계 도식(Figure 1)이 직관적
  - 방법론 설명은 체계적이나 기술 세부사항 일부 부족
  - 하이퍼파라미터 선택 과정 미상세

- **Overall** (종합): 4.25/5

**총평**: 본 논문은 인과관계 기반의 명확한 문제 정의와 정보 병목 기법의 효과적인 응용으로 유전자 발현 예측에서 의미 있는 진전을 이루었으며, ICLR 2025 게재작으로서 생물정보학과 머신러닝의 교차점에서 실질적 기여를 하고 있다.

## Related Papers

- 🔄 다른 접근: [[papers/094_AlphaGenome_advancing_regulatory_variant_effect_prediction_w/review]] — 유전자 발현 예측을 위한 서로 다른 조절 요소 발견 접근법을 제시합니다.
- 🏛 기반 연구: [[papers/696_Scaling_Large_Language_Models_for_Next-Generation_Single-Cel/review]] — 단일 세포 분석을 위한 대규모 언어모델이 유전자 발현 예측의 기반을 제공합니다.
- 🔗 후속 연구: [[papers/302_Effective_gene_expression_prediction_from_sequence_by_integr/review]] — 조절 요소 발견이 더 효과적인 유전자 발현 예측으로 확장됩니다.
- 🔄 다른 접근: [[papers/094_AlphaGenome_advancing_regulatory_variant_effect_prediction_w/review]] — 둘 다 DNA 서열로부터 유전자 발현을 예측하되 서로 다른 접근법을 사용합니다.
