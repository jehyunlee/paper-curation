---
title: "879_What_factors_affect_multimodal_in-context_learning_an_in-dep"
authors:
  - "Libo Qin"
  - "Qiguang Chen"
  - "Hao Fei"
  - "Zhi Chen"
  - "Min Li"
date: "2024"
doi: "10.48550/arXiv.2410.20482"
arxiv: ""
score: 4.3
essence: "본 논문은 시각 언어 모델(Vision LLM)에서 멀티모달 인-컨텍스트 학습(MM-ICL)의 성능을 결정하는 요소들을 체계적으로 분석합니다. 6개 모델과 20가지 전략을 통해 시연 검색, 순서 지정, 프롬프트 구성의 세 단계에서 성능에 영향을 미치는 핵심 요인들을 규명합니다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Working_Memory_Benchmarks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Clark_2024_What factors affect multimodal in-context learning an in-depth exploration.pdf"
---

# What factors affect multimodal in-context learning? an in-depth exploration

> **저자**: Libo Qin, Qiguang Chen, Hao Fei, Zhi Chen, Min Li, Wanxiang Che | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2410.20482](https://doi.org/10.48550/arXiv.2410.20482)

---

## Essence

![Figure 1](figures/fig1.webp) 
*멀티모달 인-컨텍스트 학습의 세 가지 핵심 단계: 시연(demonstration) 검색, 순서 지정, 프롬프트 구성*

본 논문은 시각 언어 모델(Vision LLM)에서 멀티모달 인-컨텍스트 학습(MM-ICL)의 성능을 결정하는 요소들을 체계적으로 분석합니다. 6개 모델과 20가지 전략을 통해 시연 검색, 순서 지정, 프롬프트 구성의 세 단계에서 성능에 영향을 미치는 핵심 요인들을 규명합니다.

## Motivation

- **Known**: 대규모 언어 모델(LLM)의 인-컨텍스트 학습(ICL) 능력이 우수하며, 멀티모달 ICL(MM-ICL)은 매개변수 조정 없이 다양한 작업에서 높은 성능을 달성함

- **Gap**: MM-ICL의 성공에도 불구하고 그 효과성을 결정하는 근본적인 메커니즘과 영향 요인들이 체계적으로 탐구되지 않음. 기존 연구들은 MM-ICL 최적화 방법 개발에만 집중하고 성능 결정 요소를 무시함

- **Why**: MM-ICL의 성능 결정 요소를 이해하는 것이 향후 더 나은 전략 개발의 기초가 되며, 연구자들에게 통일된 지침을 제공할 수 있음

- **Approach**: MM-ICL 프로세스의 세 단계(시연 검색, 순서 지정, 프롬프트 구성)를 세분화하여 각 단계에서 다양한 전략들의 영향을 실험적으로 검증

## Achievement

![Figure 2](figures/fig1.webp) 
*시연 검색 프로세스: 샘플 표현, 비교, 선택의 세 단계*

![Figure 3](figures/fig1.webp) 
*시연 순서 지정: 시연 내부(intra) 및 시연 간(inter) 순서의 영향*

1. **멀티모달 정렬이 병목**: 다중모달 검색기(retriever)가 단일모달 방식보다 평균적으로 우수한 성능을 나타냄. 모델의 멀티모달 정렬(alignment) 수준이 매개변수 크기보다 MM-ICL 효과성에 더 큰 영향을 미침. 즉, 백본 구조와 시연 품질 모두에서 정렬이 핵심 제약 요소임을 확인

2. **시연 내부 순서의 중요성**: 시연 내부의 순서(특히 이미지-텍스트 등 모달리티의 순서)가 시연 간 순서보다 모델 성능에 훨씬 더 큰 영향을 미침. 모달리티 순서 조정만으로도 상당한 성능 개선이 가능함을 입증

3. **도입부 지시문의 효과**: 시연 전에 배치된 도입부 지시문(introductory instruction)이 시연 후의 총괄 지시문이나 시연 내부의 지시문보다 작업 이해도와 성능 향상에 더욱 효과적

## How

![Figure 4](figures/fig1.webp) 
*세 가지 지시문 주입 방식: 도입부(a), 총괄(b), 시연 내부(c)*

### 시연 검색(Demonstration Retrieval)

- **샘플 표현**: 텍스트 인코더(Encoder_txt), 시각 인코더(Encoder_vis), 멀티모달 인코더(Encoder_multi) 간 성능 비교를 통해 인코더 선택의 영향 분석
  
- **샘플 비교**: 코사인 유사도(cosine similarity), L2 거리, 의미론적 다양성(semantic diversity) 등 다양한 메트릭을 통해 시연 품질 평가 방식 검증

- **샘플 선택**: 영역 정보(domain), 이미지 스타일(image style), 토큰 거리(token distance) 등 선택 기준이 성능에 미치는 영향을 체계적으로 평가

### 시연 순서 지정(Demonstration Ordering)

- **시연 내부 순서(Intra-demonstration Ordering, IOP)**: 텍스트-이미지-텍스트(IOP_tvt), 텍스트-텍스트-이미지(IOP_ttv), 이미지-텍스트-텍스트(IOP_vtt) 등 모달리티 배치 순서의 영향 분석

- **시연 간 순서(Inter-demonstration Ordering)**: 시연들 사이의 배열 순서(순열 σ_j)가 성능에 미치는 영향을 조사하되, 시연 내부 순서에 비해 상대적으로 중요도가 낮음을 발견

### 프롬프트 구성(Prompt Construction)

- **도입부 지시문(I_intro)**: 시연 이전에 작업 개요를 제공하는 지시문으로 가장 효과적
  
- **총괄 지시문(I_sum)**: 시연 이후에 개념 적용을 유도하는 지시문으로 도입부 방식보다 덜 효과적

- **시연 내부 지시문(I_intra)**: 각 시연 내에 포함된 작업 지시문으로 다른 두 방식보다 성능 개선 효과가 제한적

## Originality

- **체계적 분석 틀**: MM-ICL 프로세스를 명확한 세 단계로 구조화하고, 각 단계에서의 영향 요인들을 세분화된 연구 질문으로 재정의한 점이 혁신적

- **다중 모달 초점**: 기존 일반적인 ICL 연구를 멀티모달 환경으로 확장하면서, 모달리티 순서 등 멀티모달만의 고유 요소를 중점 분석

- **포괄적 실험 설계**: 6개 시각 언어 모델(VLLM)과 20가지 전략을 대상으로 4개 작업(이미지-캡션, VQA, 이미지 분류, 추론)에서 광범위한 검증 수행

- **멀티모달 정렬의 발견**: 모델 크기보다 멀티모달 정렬이 더 중요한 성능 결정 요소라는 인사이트는 모델 개발에 실질적 지침 제공

## Limitation & Further Study

- **작업 범위의 제한**: M3IT와 M3CoT에서만 데이터를 추출하여 4개 작업으로 제한됨. 텍스트 생성, 객체 탐지, 장면 이해 등 다양한 멀티모달 작업으로 확대 필요

- **모델 선택의 편향**: 평가된 6개 VLLMs이 특정 아키텍처(예: Transformer 기반)에 편향되어 있을 수 있으며, 더 다양한 모델 구조의 검증 필요

- **인-도메인 vs 아웃-도메인**: 시연 검색 시 영역 정보의 영향을 단순 비교만 수행하였으며, 도메인 전이 학습에서의 깊이 있는 분석 부족

- **통계적 유의성 검증 미흡**: 관측된 차이들의 통계적 유의성과 신뢰도에 대한 상세한 분석 및 보고 부재

- **동적 프롬프트 최적화**: 현재는 정적 전략 비교 중심이며, 작업이나 쿼리에 따라 동적으로 최적 전략을 선택하는 적응형 접근 개발 필요

- **상호작용 효과 분석**: 세 단계 간의 상호작용(예: 특정 검색 전략과 최적 순서 조합)에 대한 심화 연구 부재

## Evaluation

- **Novelty**: 4/5 
  - MM-ICL의 성능 요인을 체계적으로 분석하는 것은 신규 접근이지만, 기본 개념은 기존 ICL 연구의 멀티모달 확장 수준

- **Technical Soundness**: 4/5
  - 실험 설계 및 평가 메트릭이 적절하나, 통계적 유의성 검증과 신뢰도 구간 제시가 보강 필요

- **Significance**: 4.5/5
  - MM-ICL 최적화를 위한 실질적 지침 제공하며, 멀티모달 정렬의 중요성 발견은 모델 개발에 영향력 있음. 다만 작업 범위 제한으로 일반화 가능성은 중간 수준

- **Clarity**: 4.5/5
  - 시각적 다이어그램과 구조화된 설명으로 이해가 용이하며, 세 단계 분석 프레임이 명확함. 일부 실험 상세 사항은 부록 의존

- **Overall**: 4.3/5

**총평**: 본 논문은 급속히 발전하는 MM-ICL 분야에서 성능을 결정하는 근본 요인들을 처음으로 체계적으로 규명한 중요한 기초 연구입니다. 특히 멀티모달 정렬의 병목 현상과 모달리티 순서의 중요성 등의 발견은 향후 시각 언어 모델 개발과 프롬프트 최적화 연구에 실질적 방향을 제시합니다. 다만 작업 범위 확대, 통계적 엄밀성 강화, 동적 최적화 방향 탐색을 통해 일반화 가능성을 높일 필요가 있습니다.

## Related Papers

- 🔗 후속 연구: [[papers/844_Truly_assessing_fluid_intelligence_of_large_language_models/review]] — 유동 지능 연구의 멀티모달 확장으로 인-컨텍스트 학습 요소 분석
- 🧪 응용 사례: [[papers/196_ChartAssisstant_A_Universal_Chart_Multimodal_Language_Model/review]] — 차트 어시스턴트가 멀티모달 인-컨텍스트 학습의 실제 응용 사례가 됨
- 🏛 기반 연구: [[papers/844_Truly_assessing_fluid_intelligence_of_large_language_models/review]] — 멀티모달 맥락에서 유동 지능 평가의 기반 연구가 됨
- 🔗 후속 연구: [[papers/185_Can_large_language_models_understand_you_better_an_mbti_pers/review]] — 다중모달 맥락 내 학습에 영향을 미치는 요인들을 심층 분석하여 본 논문의 성격 탐지 연구를 확장한다.
