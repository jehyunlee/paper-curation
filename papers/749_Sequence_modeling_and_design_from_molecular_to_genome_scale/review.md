---
title: "749_Sequence_modeling_and_design_from_molecular_to_genome_scale"
authors:
  - "Eric Nguyen"
  - "Michael Poli"
  - "Matthew G. Durrant"
  - "Armin W. Thomas"
  - "Brian Kang 외"
date: "2024"
doi: "10.1101/2024.02.27.582234"
arxiv: ""
score: 4.4
essence: "Evo는 131 kilobase의 매우 긴 문맥길이(context length)를 가진 70억 파라미터의 게놈 기초 모델(genomic foundation model)로, 단일 뉴클레오타이드 해상도에서 DNA 서열을 예측하고 생성할 수 있다. StripedHyena 아키텍처를 기반으로 270만 개의 원핵생물 및 박테리오파지 게놈으로 학습하여 분자 규모에서 게놈 규모까지 다양한 생물학적 예측 및 생성 작업을 수행한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Evolutionary_Chemistry_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Nguyen et al._2024_Sequence modeling and design from molecular to genome scale with Evo.pdf"
---

# Sequence modeling and design from molecular to genome scale with Evo

> **저자**: Eric Nguyen, Michael Poli, Matthew G. Durrant, Armin W. Thomas, Brian Kang 외 | **날짜**: 2024 | **DOI**: [10.1101/2024.02.27.582234](https://doi.org/10.1101/2024.02.27.582234)

---

## Essence

Evo는 131 kilobase의 매우 긴 문맥길이(context length)를 가진 70억 파라미터의 게놈 기초 모델(genomic foundation model)로, 단일 뉴클레오타이드 해상도에서 DNA 서열을 예측하고 생성할 수 있다. StripedHyena 아키텍처를 기반으로 270만 개의 원핵생물 및 박테리오파지 게놈으로 학습하여 분자 규모에서 게놈 규모까지 다양한 생물학적 예측 및 생성 작업을 수행한다.

## Motivation

- **Known**: 최근 기계학습과 대규모 게놈 데이터셋의 발전으로 생물학 분야에서 기초 모델(foundation model) 개발이 진행 중이나, 기존 연구들은 단백질, 조절DNA, RNA 등 특정 양식(modality)에만 특화된 모델에 집중되어 있음
- **Gap**: CRISPR-Cas 복합체나 전이가능 원소(transposable elements) 같은 복잡한 생물학적 과정은 여러 분자 양식 간의 상호작용을 필요로 하는데, 기존 생성형 모델들은 단일 분자나 짧은 DNA 서열 설계에만 제한됨
- **Why**: DNA는 생물학적 정보의 기본 계층이며, 단일 뉴클레오타이드 해상도에서 전체 게놈을 모델링하면 조절DNA, RNA, 단백질의 상호작용과 진화적 효과를 모두 포착할 수 있음
- **Approach**: StripedHyena 아키텍처(주의 메커니즘과 데이터 제어식 합성곱 연산자의 하이브리드)를 활용하여 긴 서열을 효율적으로 처리하고, 300억 뉴클레오타이드 토큰의 OpenGenome 데이터셋으로 사전학습

## Achievement

![Figure 1 개념도](./fig1_concept.png)
*Figure 1: 원핵생물 게놈에서 게놈 기초 모델 사전학습. StripedHyena 아키텍처를 사용한 7B 파라미터 Evo 모델의 학습 구성.*

1. **영점학습 기능 예측(Zero-shot Function Prediction)**: 
   - E. coli 단백질의 돌연변이 적응도(fitness) 예측에서 최첨단 단백질 언어 모델과 비교 가능 또는 초과 성능
   - 비코딩 RNA 돌연변이 적응도 예측에서 특화된 RNA 언어 모델 능가
   - 조절 서열만으로 프로모터-리보솜결합부위(RBS) 쌍의 유전자 발현 활성화 조합 예측

2. **다중 요소 생성 작업(Multi-element Generation)**:
   - 코딩 및 비코딩 서열의 공진화 연쇄(co-evolutionary linkage) 학습을 통해 합성 CRISPR-Cas 분자 복합체 생성 (최초)
   - 전체 전이가능 원소 시스템 생성 (최초)

3. **전체 게놈 규모 작업**:
   - 감독 없이 세균 및 박테리오파지의 필수 유전자 예측 (뉴클레오타이드 해상도)
   - 650 kb 길이의 기능적 게놈 구조를 가진 코딩 서열 생성 (기존 방법보다 수십 배 이상 길음)

## How

![Figure 2 성능 평가](./fig2_performance.png)
*Figure 2: 단백질, 비코딩 RNA, 조절 영역에 대한 영점학습 기능 예측 성능.*

- **StripedHyena 아키텍처**: 29개의 데이터 제어식 합성곱 연산자(hyena layer)와 3개(10%)의 다중 헤드 주의(attention) 층을 교대로 배치. Hyena 층은 단기 및 장기 필터의 합성으로 DNA의 노이즈 패턴 필터링 및 뉴클레오타이드를 모티프로 집계
  
- **문맥 길이 및 토큰화**: 131,000 토큰의 문맥길이, 단일 뉴클레오타이드 바이트-수준 토큰화로 기존 Transformer 기반 DNA 모델의 한계 극복

- **2단계 사전학습**: 
  - 1단계: 8,000 토큰 문맥길이로 학습
  - 2단계: 문맥 확장으로 131,000 토큰으로 학습
  
- **데이터셋**: GTDB(80,000+ 세균 및 고균 게놈), IMG/PR(예측된 원핵생물 파지 및 플라스미드), IMG/VR(진핵생물 숙주 바이러스 제외) - 총 300억 뉴클레오타이드 토큰

- **스케일링 법칙**: 300+ 모델을 Transformer++, Mamba, Hyena, StripedHyena 4가지 아키텍처로 학습. StripedHyena가 바이트 해상도에서 최적의 스케일링 성능 입증

## Originality

- **DNA 데이터에 대한 첫 스케일링 법칙 분석**: 게놈 서열 모델링에 최적의 모델 크기와 데이터셋 크기의 관계를 체계적으로 분석

- **단일 뉴클레오타이드 해상도의 131kb 문맥길이**: 기존 DNA 언어 모델들(Transformer 기반)의 문맥길이 제약 극복

- **분자-게놈 스케일 통합 모델링**: 하나의 모델에서 단백질, RNA, 조절 DNA의 세 가지 양식을 동시에 다루는 첫 시도

- **합성 생물학적 복합체 생성**: CRISPR-Cas 시스템과 전이가능 원소 같은 다중 분자 상호작용 시스템의 생성적 설계 최초 시연

- **650kb 코딩 서열 생성**: 기존 방법(DaSilva et al., 650bp 규모)과 비교하여 천배 이상의 길이 달성

## Limitation & Further Study

- **학습 데이터의 제한성**: 원핵생물 및 파지 게놈에만 제한되어 진핵생물의 복잡한 기능(조절 영역의 복잡성, 선택적 스플라이싱 등) 미반영

- **생성된 서열의 검증 부족**: 길게 생성된 650kb 서열이 실제 생물학적으로 기능하는지에 대한 실험적 검증 미제시

- **필수 유전자 예측의 기전 해석**: 영점학습으로 필수 유전자를 예측하는 메커니즘(서열 특성? 문맥 정보?)에 대한 상세 분석 부족

- **후속 연구 방향**:
  - 진핵생물 게놈으로 확장하여 더 복잡한 생물학적 현상 모델링
  - 생성된 합성 CRISPR-Cas 및 전이가능 원소의 실험적 검증
  - 파인튜닝 효율성 및 적응성 개선
  - 구조적 변이(structural variants)와 같은 대규모 게놈 변화 모델링


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.5/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.4/5

**총평**: Evo는 게놈 수준의 장문맥 시퀀스 모델링과 생성에서 획기적인 진전을 이루었으며, DNA 스케일링 법칙 제시와 다중 분자 복합체 생성 능력은 합성생물학 분야에 새로운 가능성을 열었다. 다만 생성된 서열의 실생물 검증과 더 광범위한 생물체로의 확장이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/382_Genome_modeling_and_design_across_all_domains_of_life_with_E/review]] — 동일한 Evo 모델의 다른 버전으로 성능 개선사항 비교 분석 가능
- 🧪 응용 사례: [[papers/305_Efficient_Evolutionary_Search_Over_Chemical_Space_with_Large/review]] — 진화적 탐색 방법론이 게놈 설계와 생성에 실제 적용됨
- 🔄 다른 접근: [[papers/382_Genome_modeling_and_design_across_all_domains_of_life_with_E/review]] — 동일한 Evo 모델이지만 다른 해상도와 응용 관점에서 접근함
- 🏛 기반 연구: [[papers/302_Effective_gene_expression_prediction_from_sequence_by_integr/review]] — 유전자 발현 예측을 위한 서열 모델링 연구가 분자부터 게놈 규모까지의 서열 모델링 및 설계 연구의 중요한 기초가 되었다
