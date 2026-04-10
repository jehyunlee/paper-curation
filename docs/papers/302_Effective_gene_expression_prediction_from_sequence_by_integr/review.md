---
title: "302_Effective_gene_expression_prediction_from_sequence_by_integr"
authors:
  - "Žiga Avsec"
  - "Vikram Agarwal"
  - "D. Visentin"
  - "J. Ledsam"
  - "A. Grabska-Barwinska"
date: "2021"
doi: "10.1038/s41592-021-01252-x"
arxiv: ""
score: 4.5
essence: "DNA 서열로부터 유전자 발현을 예측하는 문제에서 Transformer 기반 자기주목(self-attention) 메커니즘을 통해 100 kb까지의 장거리 규제 요소를 통합함으로써 예측 정확도를 획기적으로 향상시킨 연구이다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Biological_Foundation_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Avsec et al._2021_Effective gene expression prediction from sequence by integrating long-range interactions.pdf"
---

# Effective gene expression prediction from sequence by integrating long-range interactions

> **저자**: Žiga Avsec, Vikram Agarwal, D. Visentin, J. Ledsam, A. Grabska-Barwinska | **날짜**: 2021 | **DOI**: [10.1038/s41592-021-01252-x](https://doi.org/10.1038/s41592-021-01252-x)

---

## Essence

DNA 서열로부터 유전자 발현을 예측하는 문제에서 Transformer 기반 자기주목(self-attention) 메커니즘을 통해 100 kb까지의 장거리 규제 요소를 통합함으로써 예측 정확도를 획기적으로 향상시킨 연구이다.

## Motivation

- **Known**: 딥 합성곱 신경망(CNN)이 DNA 서열로부터 유전자 발현 예측의 최첨단 기술이나, 전사 시작점(TSS)으로부터 20 kb 이내의 서열 요소만 고려 가능함
- **Gap**: 많은 생물학적 규제 요소(인핸서, 억제인자, 인슐레이터)는 20 kb 이상 원거리에서 유전자 발현에 영향을 미치나, 기존 CNN의 국소적 합성곱 구조로는 이러한 장거리 상호작용 정보 흐름이 제한됨
- **Why**: 비코딩 DNA가 어떻게 서로 다른 세포 유형에서 유전자 발현을 결정하는지 이해하고, 질병 관련 유전 변이의 효과를 예측하는 것이 인간 유전학에서 중요함
- **Approach**: Transformer의 주목 메커니즘을 적용하여 장거리 정보 흐름을 개선하고, 다중 작업 학습(multitask learning)으로 인간 및 마우스 게놈의 에피유전체 및 전사 데이터셋 수천 개를 동시에 예측

## Achievement

![Figure 1: Enformer improves gene expression prediction in held-out genes by using a larger receptive field](figures/fig1.webp)
*그림 1: Enformer는 200 kb 입력 서열에서 128 bp 해상도로 게놈 트랙을 예측하며, Transformer 모듈을 통해 Basenji2 대비 5배 큰 수용장(100 kb vs 20 kb)을 달성*

1. **예측 정확도 획기적 향상**: CAGE(Cap Analysis Gene Expression)를 통한 RNA 발현 예측에서 평균 상관계수가 0.81에서 0.85로 증가 (Basenji1→Basenji2 개선의 2배 규모, 실험 수준 정확도 0.94와의 격차 1/3 해소)

2. **장거리 규제 요소 통합**: 수용장을 20 kb에서 100 kb로 확대함으로써 고신뢰도 인핸서-유전자 쌍의 포함 비율을 47%에서 84%로 증가

3. **세포 유형 특이성 향상**: 조직 또는 세포 유형 특이성 예측이 개선되었으며, 밀접하게 관련된 샘플들에서도 우수한 성능 발휘

![Figure 2: Enformer attends to cell-type-specific enhancers, enabling enhancer prioritization](figures/fig2.webp)
*그림 2: Enformer의 기여도 점수가 세포 유형 특이적 인핸서를 식별하며, ABC 점수와 필적하는 인핸서 우선순위화 성능 달성*

4. **인핸서 우선순위화**: DNA 서열만을 입력으로 하면서도 실험 데이터(HiC, H3K27ac)를 사용하는 ABC 점수와 동등하거나 더 우수한 성능으로 인핸서-유전자 상호작용 예측

5. **절연체 요소 학습**: 위상 연관 영역(TAD) 경계에 대한 주목이 임의의 위치보다 높고, 경계 반대편 영역에 대한 주목이 낮은 패턴으로 절연체 기능 학습 확인

## How

- **아키텍처**: Enformer(enhancer와 transformer의 합성어)는 Transformer 계층을 사용하여 입력 서열의 모든 위치 간에 직접 주목(attention) 연산 수행, 이를 통해 기존 CNN의 다층 구조 없이도 장거리 정보 통합 가능

- **상대 위치 부호화(Relative Positional Basis Functions)**: NLP의 표준 방식 대신 프로모터 상류/하류를 구분하고 근거리/원거리 규제 요소를 구분하기 위한 맞춤형 상대 위치 함수 적용으로 성능 향상

- **다중 작업 학습**: 4가지 유형의 게놈 전역 트랙(CAGE, 히스톤 수정, 전사인자(TF) 결합, DNA 접근성) 예측을 여러 세포 유형 및 조직에서 동시 학습

- **기여도 점수 계산**: 입력 구배(input gradient × input)와 주목 가중치를 계산하여 예측에 가장 기여하는 서열 요소(특히 인핸서) 식별

- **주목 행렬 분석**: TAD 경계에 중점을 두고 절연체 기능을 검증하기 위해 내부 주목 행렬 시각화

## Originality

- **Transformer 적용의 적절성**: NLP에서 성공한 Transformer 아키텍처를 유전체학 문제에 효과적으로 적용하되, 게놈의 특성(상류/하류 구분, 거리 민감성)을 고려한 맞춤형 위치 부호화 도입

- **해석 가능성 제공**: 모델의 주목 메커니즘과 기여도 점수를 통해 "어떤 서열 요소"가 예측에 영향하는지 생물학적으로 검증 가능한 방식으로 제시

- **광범위한 평가**: CRISPRi 인핸서 검증, 직접 돌연변이 유발 실험, eQTL 분석 등 다양한 독립적 생물학적 벤치마크로 모델 검증

## Limitation & Further Study

- **계산 복잡성**: Transformer의 이차 복잡도(O(n²))로 인해 매우 긴 서열에 대한 확장성 제한 가능성 (현재 200 kb 제한)

- **세포 유형 외삽화(Extrapolation)**: 학습 데이터에 없는 세포 유형이나 조직에 대한 예측 성능 미검증으로, 임상 적용 가능성 미확인

- **인과성 vs 상관성**: 기여도 점수가 인핸서를 식별하지만, 이것이 실제 인과적 규제를 의미하는지 vs 단순 상관성인지에 대한 추가 검증 필요

- **후속 연구 방향**: 
  - 더 긴 서열(수 메가베이스)을 처리 가능한 효율적 Transformer 변형 개발
  - 구조 변이(structural variant)와 같은 복잡한 유전 변이 효과 예측으로 확장
  - 진화적 규제 요소 보존 패턴 학습 및 비교 게놈학 응용

## Evaluation

- **Novelty**: 4.5/5 - Transformer를 유전체 예측에 적용한 것은 참신하나, Transformer 자체는 기존 기술이며 주요 혁신은 아키텍처 적응과 위치 부호화의 개선

- **Technical Soundness**: 4.5/5 - 철저한 실험 설계, 적절한 대조군(dilated convolutions 비교), 여러 독립적 벤치마크로 검증되었으나, 계산 복잡성에 대한 심화 분석 부재

- **Significance**: 5/5 - 유전자 발현 예측 정확도의 실질적 개선, 인간 질병 관련 변이 미세 지도화에 대한 직접적 영향, 여러 하위 영역(인핸서 우선순위화, 돌연변이 효과 예측)에서 광범위한 적용 가능성

- **Clarity**: 4.5/5 - 논문 구조와 설명이 명확하고 체계적이나, 일부 기술적 세부사항(상대 위치 부호화 함수)에 대한 더 자세한 설명 필요

- **Overall**: 4.5/5

**총평**: 본 논문은 Transformer의 자기주목 메커니즘을 통해 DNA 서열로부터의 유전자 발현 예측이라는 오랜 문제를 실질적으로 해결하며, 다양한 생물학적 검증을 통해 모델의 생물학적 타당성까지 입증한 매우 높은 수준의 연구이다. 특히 장거리 규제 상호작용 통합이라는 생물학적 직관을 기술적으로 구현하고, 인간 유전학의 여러 응용 분야에서 즉각적인 임상 가능성을 제시한 점에서 높이 평가된다.

## Related Papers

- 🔄 다른 접근: [[papers/696_Scaling_Large_Language_Models_for_Next-Generation_Single-Cel/review]] — DNA 서열 기반 유전자 발현 예측과 단일세포 데이터의 텍스트 변환 처리가 유전체학 빅데이터 분석의 서로 다른 접근법을 보여준다
- 🧪 응용 사례: [[papers/105_Artificial_Intelligence_for_Direct_Prediction_of_Molecular_D/review]] — 장거리 규제 요소를 통합한 Transformer 기반 예측이 물리 시스템에서 자기주목 메커니즘과 대칭성 활용의 생물학적 적용 사례이다
- 🏛 기반 연구: [[papers/749_Sequence_modeling_and_design_from_molecular_to_genome_scale/review]] — 유전자 발현 예측을 위한 서열 모델링 연구가 분자부터 게놈 규모까지의 서열 모델링 및 설계 연구의 중요한 기초가 되었다
- 🔗 후속 연구: [[papers/382_Genome_modeling_and_design_across_all_domains_of_life_with_E/review]] — DNA 서열로부터 유전자 발현 예측 기술이 모든 생명체 도메인에 걸친 게놈 모델링 및 설계로 확장되었다
- 🔗 후속 연구: [[papers/483_Learning_to_Discover_Regulatory_Elements_for_Gene_Expression/review]] — 조절 요소 발견이 더 효과적인 유전자 발현 예측으로 확장됩니다.
