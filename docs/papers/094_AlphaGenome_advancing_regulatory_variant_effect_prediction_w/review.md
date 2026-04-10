---
title: "094_AlphaGenome_advancing_regulatory_variant_effect_prediction_w"
authors:
  - "Žiga Avsec"
  - "Natasha Latysheva"
  - "Jun Cheng"
  - "Guido Novati"
  - "Kyle R. Taylor"
date: "2025"
doi: "10.1101/2025.06.25.661532"
arxiv: ""
score: 4.6
essence: "AlphaGenome은 1 메가베이스(Mb) DNA 서열 입력과 단일 염기쌍(bp) 해상도를 통합하여, 11개의 생물학적 모달리티(유전자 발현, 스플라이싱, 크로마틴 접근성, 조직인자 결합, 3D 크로마틴 구조 등)에 걸쳐 5,930개의 게놈 트랙을 동시에 예측하는 통합 딥러닝 모델이다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Domain-specific_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Avsec et al._2025_AlphaGenome advancing regulatory variant effect prediction with a unified DNA sequence model.pdf"
---

# AlphaGenome: advancing regulatory variant effect prediction with a unified DNA sequence model

> **저자**: Žiga Avsec, Natasha Latysheva, Jun Cheng, Guido Novati, Kyle R. Taylor | **날짜**: 2025 | **DOI**: [10.1101/2025.06.25.661532](https://doi.org/10.1101/2025.06.25.661532)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: AlphaGenome 모델 아키텍처, 학습 방식 및 종합 평가 성능. (a) 모델 개요: 1 Mb DNA 서열을 입력받아 11개 모달리티에서 5,930개의 게놈 트랙을 단일 염기쌍 해상도로 예측. (e) 변이 효과 예측에서 기존 모델 대비 상대적 성능 개선*

AlphaGenome은 1 메가베이스(Mb) DNA 서열 입력과 단일 염기쌍(bp) 해상도를 통합하여, 11개의 생물학적 모달리티(유전자 발현, 스플라이싱, 크로마틴 접근성, 조직인자 결합, 3D 크로마틴 구조 등)에 걸쳐 5,930개의 게놈 트랙을 동시에 예측하는 통합 딥러닝 모델이다.

## Motivation

- **Known**: 기존 sequence-to-function 모델들(SpliceAI, Enformer, Borzoi 등)은 각각 강점과 약점을 보유
  - 단기 시퀀스(≤10kb) + 고해상도(bp 수준) vs 장기 시퀀스(200-500kb) + 저해상도(32-128bp)
  - 단일 모달리티 전문화 vs 다중 모달리티 일반화의 성능 트레이드오프

- **Gap**: 기존 모델들은 다음 중 하나 이상의 제약을 가짐
  - 긴 범위 게놈 상호작용(distal regulatory elements) 포착 불가
  - 염기쌍 수준의 미세한 조절 특성(스플라이스 사이트, 전사인자 발자국) 해상도 부족
  - 스플라이싱 내 여러 예측 양상(splice site vs splice junction) 부재

- **Why**: 98% 이상의 인간 유전 변이가 비코딩 영역에 위치하며, 임상적 의의를 가진 변이들의 분자적 메커니즘을 이해하려면 다양한 생물학적 모달리티를 동시에 평가해야 함

- **Approach**: U-Net 기반 아키텍처와 sequence parallelism을 활용하여 1 Mb 컨텍스트에서 bp 해상도 예측을 가능하게 하고, 다양한 모달리티를 단일 모델로 통합

## Achievement

![Figure 2](figures/fig2.webp)
*Figure 2: AlphaGenome 트랙 예측 예시 및 상세 성능 평가. 관찰된 데이터와 AlphaGenome 예측의 높은 일치도 시연*

1. **게놈 트랙 예측 성능**: 26개의 게놈 트랙 예측 과제 중 22개에서 기존 최강 모델을 능가 (Pearson r 기준 다양한 모달리티 분석)

2. **변이 효과 예측 성능**: 26개의 변이 효과 예측 벤치마크 중 24개에서 우수한 성능 달성
   - 스플라이싱: 15.0% (DeltaSplice 대비), 59.1% (ClinVar splice site region)
   - 유전자 발현: 13.7% (eQTL supervised, Borzoi 대비)
   - 크로마틴 접근성: 8.0-18.0% (bQTL, ds/caQTL)

3. **다중 모달리티 해석**: TAL1 종양원유전자 인근의 임상적으로 관련된 변이들의 메커니즘을 모든 모달리티에서 동시에 정확히 설명

## How

![Figure 3](figures/fig3.webp)
*Figure 3: AlphaGenome은 최첨단 스플라이싱 변이 효과 예측 모델. (a) 스플라이싱 예측 유형의 종합적 비교 및 성능 메트릭*

- **아키텍처**
  - U-Net 스타일 백본: 인코더(다운샘플링) → 트랜스포머 블록(inter-device 통신) → 디코더(업샘플링) → 과제별 출력 헤드
  - 1차원 임베딩(1 bp, 128 bp 해상도): 게놈 트랙 예측용
  - 2차원 임베딩(2048 bp 해상도): 공간적 상호작용(contact map) 예측용

- **학습 전략**
  - 사전학습: 교차검증 fold별로 1 Mb 구간을 증강(shift, reverse complement)하여 학습 → fold-specific & all-folds teacher 모델 생성
  - 증류(Distillation): 학생 모델이 frozen all-folds teacher로부터 학습, 변이 섭동(mutational perturbation) 입력 사용 → 단일 변이 효과 예측 모델 생성

- **기술 혁신**
  - Sequence parallelism: 1 Mb 서열을 131 kb 청크로 분할하여 8개 디바이스에서 병렬 처리
  - 스플라이싱 모달리티: 스플라이스 사이트 + 스플라이스 사이트 사용량 + **스플라이스 정션 예측(신규)** 포함

- **데이터**
  - 인간: 5,930개 게놈 트랙 (11개 모달리티, 다양한 조직/세포주)
  - 마우스: 1,128개 게놈 트랙
  - 다양한 실험 방식: RNA-seq, CAGE-seq, PRO-cap, DNase-seq, ATAC-seq, ChIP-seq, Hi-C/micro-C

## Originality

- **1 Mb + bp 해상도 통합**: 기존의 시퀀스 길이-해상도 트레이드오프를 sequence parallelism과 효율적 아키텍처로 극복한 첫 시도

- **포괄적 스플라이싱 예측**: splice junction 예측과 splice site usage를 통합하여 스플라이싱의 다양한 양상을 동시에 모델링

- **단일 모델의 다중 모달리티**: 11개 모달리티, 5,930개 트랙을 단일 프레임워크로 통합 → 특화 모델과의 성능 경합 달성

- **종합적 증류 방식**: 변이 섭동 기반 증류로 variant effect prediction에 최적화된 모델 생성 (기존 모델들은 track prediction 최적화)

- **광범위한 벤치마킹**: 26개의 변이 효과 예측 과제와 24개의 게놈 트랙 예측 과제로 체계적 평가

## Limitation & Further Study

- **컨텍스트 길이 한계**: 1 Mb가 대부분의 enhancer-gene 쌍을 포괄하지만(99%), 극단적으로 먼 거리의 regulatory element는 여전히 누락될 수 있음

- **해상도 다양성**: 11개 모달리티 중 일부는 32-128 bp 해상도로 제한되어 미세한 변이 효과 포착에 제약

- **세포주 특이성**: 대부분이 세포주 기반 데이터이며, 일부 modality는 조직/세포 타입 다양성 부족

- **후속 연구 방향**
  - 더 장거리 컨텍스트(예: 5-10 Mb) 처리 가능성 검증
  - 실시간 조직 샘플과의 검증을 통한 in vivo 예측 정확도 개선
  - 드문 변이(rare variants) 효과에 대한 특화 fine-tuning
  - 다양한 유전배경(genetic background)에서의 변이 효과 예측 일반화

## Evaluation

- **Novelty**: 4.5/5
  - 1 Mb + bp 해상도 통합은 혁신적이나, 개별 기술(U-Net, transformer, sequence parallelism, distillation)은 기존 방식의 조합

- **Technical Soundness**: 4.8/5
  - 아키텍처, 학습 전략, 증류 방식 모두 기술적으로 견고함
  - 광범위한 ablation study로 설계 선택 정당화 (제시된 본문에는 Figure 7 언급)
  - 재현성을 위한 도구 제공 약속

- **Significance**: 5/5
  - 비코딩 변이 해석의 중요한 도전 과제 해결
  - 24/26 변이 예측 과제에서 최우수 성능 달성
  - TAL1 사례 연구로 임상적 관련성 입증
  - 단일 통합 모델의 실용성 → 다중 특화 모델 필요성 감소

- **Clarity**: 4.5/5
  - 명확한 동기, 포괄적 Figure 1
  - 다양한 subheading으로 각 모달리티별 결과 체계화
  - 일부 기술 세부사항(Extended Data Fig. 1 참조)이 본문에서 간략화됨

- **Overall**: 4.6/5

**총평**: AlphaGenome은 기존의 구조적 트레이드오프를 극복하고 11개 모달리티를 통합하는 강력한 unified model로서, 비코딩 변이의 분자적 효과 해석을 위한 중요한 진전을 제시한다. 광범위한 벤치마킹과 공개 도구 제공으로 실용적 임팩트가 높으나, 컨텍스트 길이 한계와 일부 modality의 해상도 제약이 향후 개선 과제이다.

## Related Papers

- 🔄 다른 접근: [[papers/483_Learning_to_Discover_Regulatory_Elements_for_Gene_Expression/review]] — 둘 다 DNA 서열로부터 유전자 발현을 예측하되 서로 다른 접근법을 사용합니다.
- 🏛 기반 연구: [[papers/166_Biomaze_Benchmarking_and_enhancing_large_language_models_for/review]] — 생물학적 경로 추론이 유전체 변이 효과 예측의 기반이 됩니다.
- 🔗 후속 연구: [[papers/382_Genome_modeling_and_design_across_all_domains_of_life_with_E/review]] — AlphaGenome의 다중 모달리티 예측이 전체 생명체의 게놈 모델링으로 확장됩니다.
- 🧪 응용 사례: [[papers/166_Biomaze_Benchmarking_and_enhancing_large_language_models_for/review]] — 생물학적 경로 추론이 유전체 변이 효과 예측에 적용됩니다.
- 🔄 다른 접근: [[papers/483_Learning_to_Discover_Regulatory_Elements_for_Gene_Expression/review]] — 유전자 발현 예측을 위한 서로 다른 조절 요소 발견 접근법을 제시합니다.
