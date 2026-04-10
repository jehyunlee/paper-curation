---
title: "166_Biomaze_Benchmarking_and_enhancing_large_language_models_for"
authors:
  - "He Zhao"
  - "Chang Ma"
  - "Fangzhi Xu"
  - "Lingpeng Kong"
  - "Zhi-Luo Deng"
date: "2025"
doi: "10.48550/arXiv.2502.16660"
arxiv: ""
score: 4.25
essence: "본 논문은 생물학적 경로(biological pathway) 추론 능력을 평가하기 위한 BioMaze 벤치마크를 제시하고, LLMs의 경로 추론 한계를 보완하기 위해 PathSeeker라는 에이전트 기반 방법을 제안한다. 이를 통해 복잡한 생물학적 시스템에서의 다단계 인과 추론 문제를 해결한다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Domain-specific_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhao et al._2025_Biomaze Benchmarking and enhancing large language models for biological pathway reasoning.pdf"
---

# Biomaze: Benchmarking and enhancing large language models for biological pathway reasoning

> **저자**: He Zhao, Chang Ma, Fangzhi Xu, Lingpeng Kong, Zhi-Luo Deng | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2502.16660](https://doi.org/10.48550/arXiv.2502.16660)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: BioMaze 작업 및 추론 방법의 설명. 생물학적 경로 그래프 데이터 지원 유무에 따른 추론 방식 비교*

본 논문은 생물학적 경로(biological pathway) 추론 능력을 평가하기 위한 BioMaze 벤치마크를 제시하고, LLMs의 경로 추론 한계를 보완하기 위해 PathSeeker라는 에이전트 기반 방법을 제안한다. 이를 통해 복잡한 생물학적 시스템에서의 다단계 인과 추론 문제를 해결한다.

## Motivation

- **Known**: LLMs는 단백질 설계, 신약 발굴, 임상 시험 분석 등 다양한 생물학 과제에서 우수한 성능을 보였다.

- **Gap**: 생물학적 경로 추론, 특히 개입(intervention)과 섭동(perturbation)이 포함된 복잡한 다단계 인과 추론 능력에 대한 체계적 평가가 부재하다. 또한 LLMs의 경로 지식이 사전학습 데이터에서 구조화되지 않아 효과적인 활용이 어렵다.

- **Why**: 생물학적 경로 추론은 생물학자가 현상을 설명하고 가설을 수립하며 실험을 설계하는 근본적인 작업이므로, LLMs가 이를 효과적으로 수행하지 못한다면 생물학 분야의 광범위한 응용 가능성에 의문이 제기된다.

- **Approach**: (1) 6,000개 이상의 생물학적 경로 논문에서 추출한 5.1K 고품질 문제로 구성된 BioMaze 벤치마크 구축, (2) CoT 및 그래프 증강 추론 방법 평가, (3) 경로 그래프를 대화형으로 탐색하는 PathSeeker 에이전트 제안.

## Achievement

![Figure 4](figures/fig4.webp)
*Figure 4: 다양한 LLM의 생물학적 경로 추론 능력 비교. 모든 LLM이 경로 추론에서 어려움을 겪으며, 특히 섭동 시나리오에서 성능 저하가 심함*

![Figure 5](figures/fig5.webp)
*Figure 5: 추론 단계 증가에 따른 Chain-of-Thought 성능 감소*

1. **BioMaze 벤치마크 구축**: 실제 연구 문헌에서 도출된 5.1K 복합 생물학적 경로 문제를 포함하며, 자연 동적 변화, 섭동/개입, 추가 개입 조건, 다중 스케일 연구 대상(단일 인자, 상호작용 과정, 거시적 기능)을 포괄한다. 3가지 분류 체계(질문 유형, 추가 조건, 조사 대상)로 다양한 연구 시나리오를 커버한다.

2. **LLMs의 한계 규명**: 모든 LLM(LLaMA 8B~GPT-4)이 경로 추론에서 투쟁하며, 특히 섭동 시스템에서 성능이 급격히 저하됨을 입증했다. 추론 단계가 증가할수록 성능이 선형적으로 감소한다.

3. **PathSeeker 에이전트 제안**: 대화형 부분그래프(subgraph) 탐색을 통해 경로 추론 성능을 향상시키는 방법론을 제시했으며, 이는 과학자의 경로 추론 방식을 모방한다.

## How

![Figure 2](figures/fig2.webp)
*Figure 2: BioMaze 데이터셋의 생물학적 영역 및 추론 유형 분포. 6개 주요 영역과 3가지 분류 차원 포함*

![Figure 3](figures/fig3.webp)
*Figure 3: PathSeeker의 경로 그래프 데이터베이스 대화형 탐색 메커니즘. 글로벌-로컬 부분그래프를 수요에 맞게 탐색*

**BioMaze 벤치마크 구축**:
- 6,000+ 생물학적 경로 연구논문에서 실험적 개입과 관찰이 포함된 사례 추출
- 각 관찰을 True/False 또는 개방형 질문으로 변환 및 답변 라벨링
- 자동 필터링(불명확한 정의, 특정 측정값 요구, 다중 사실 질문, 자명한 답변, 경로 무관 질문 제거) + 전문가 검수(통과율 ~40%)
- 최종 5.1K 고품질 문제 확보

**분류 체계 (3가지 차원)**:
- **Inquiry Type**: 정상(Normal Source) vs. 섭동(Perturbed Source)
- **Extra Condition**: 자연(Natural) vs. 개입된(Intervened) 조건
- **Investigation Target**: 단일 인자(Single) vs. 상호작용 과정(Interaction) vs. 거시적 기능(Function)

**PathSeeker 방법론**:
- LLM 에이전트가 추론 수행 중 경로 그래프를 대화형으로 탐색
- 글로벌-로컬 부분그래프 네비게이션으로 효율성 향상
- 추론과 경로 브라우징 사이의 상호 강화 관계 수립
- 섭동, 긴 추론 체인, 오류(잘못된 단계, 누락) 등 문제 해결

## Originality

- **새로운 벤치마크**: 생물학적 경로 추론의 체계적 평가를 위한 최초의 대규모 고품질 데이터셋(5.1K 문제)로, 실제 연구 논문에 기반하고 전문가 검수를 거친 신뢰성 높은 자원 제공

- **포괄적 분류 체계**: 자연 동적 변화, 섭동, 추가 개입, 다중 스케일 조사 등 실제 생물학 연구의 다양한 시나리오를 반영한 3차원 분류 방식 도입

- **문제점 규명**: 기존 CoT 및 그래프 증강 방법의 한계를 정량적으로 입증(특히 섭동 시나리오에서의 성능 저하)

- **혁신적 에이전트 방법**: 경로 그래프를 대화형으로 탐색하는 부분그래프 기반 네비게이션 방식으로 기존 검색/LLM 튜닝 방법보다 효율적인 접근법 제시

## Limitation & Further Study

- **데이터 한계**: 벤치마크가 주로 영문 문헌에서 추출되어 언어 편향이 있을 수 있으며, 특정 생물학 영역(예: 특정 질병이나 시스템)의 대표성 검증 필요

- **평가 범위**: 현재 평가는 주로 영어 LLM에 초점을 맞추고 있어, 다국어 모델이나 생물학 특화 모델(예: BioBERT, SciBERT)에 대한 평가 확대 필요

- **PathSeeker 성능**: 제시된 결과에서 PathSeeker의 구체적인 성능 개선 정도가 상세히 제시되지 않아 실제 효과 규모 파악 어려움

- **확장성**: 대규모 경로 그래프(수백만 노드)에 대한 부분그래프 탐색 전략의 확장성과 계산 비용에 대한 분석 부재

- **후속 연구 방향**:
  - PathSeeker의 부분그래프 선택 전략 최적화
  - 생물학적 경로 외 다른 과학 도메인(화학, 물리)으로의 방법 일반화
  - 실제 생물학 실험 설계 및 가설 생성에서의 효용성 검증
  - 미처리된 경로 특성(순환 경로, 피드백 루프)에 대한 추론 능력 강화

## Evaluation

- **Novelty**: 4/5 - BioMaze 벤치마크와 분류 체계는 신규성이 우수하나, 에이전트 기반 그래프 탐색 개념 자체는 기존 연구의 확장

- **Technical Soundness**: 4/5 - 벤치마크 구축 방법론이 체계적이고 데이터 필터링/검수 과정이 철저하나, PathSeeker의 기술적 상세와 실험 비교 분석 부족

- **Significance**: 5/5 - 생물학적 경로 추론이라는 근본적이고 광범위한 응용 분야를 다루며, LLMs의 현실적 한계를 명확히 규명하고 실제 해결책을 제시함

- **Clarity**: 4/5 - 전반적 구성과 설명이 명확하나, Figure 3의 PathSeeker 메커니즘이 다소 추상적이며 알고리즘 의사코드 제시 부재

- **Overall**: 4.25/5

**총평**: 본 논문은 생물학적 경로 추론이라는 미개척 분야에서 대규모 고품질 벤치마크를 제공하고 LLMs의 실질적 한계를 규명했다는 점에서 매우 가치있다. 특히 실제 연구 문헌 기반의 5.1K 문제와 체계적 분류 체계는 학계에 중요한 자산이 될 것이다. 다만 제안된 PathSeeker 방법의 구체적 구현과 성능 개선 효과에 대한 더욱 상세한 실험 결과 제시가 논문의 완성도를 높일 것으로 판단된다.

## Related Papers

- 🧪 응용 사례: [[papers/094_AlphaGenome_advancing_regulatory_variant_effect_prediction_w/review]] — 생물학적 경로 추론이 유전체 변이 효과 예측에 적용됩니다.
- 🏛 기반 연구: [[papers/726_Sciknoweval_Evaluating_multi-level_scientific_knowledge_of_l/review]] — 다층적 생물학 지식 평가가 경로 추론 벤치마크의 기반을 제공합니다.
- 🔗 후속 연구: [[papers/681_Revisiting_Gene_Ontology_Knowledge_Discovery_with_Hierarchic/review]] — 생물학적 경로 추론이 유전자 온톨로지 지식 발견으로 확장됩니다.
- 🏛 기반 연구: [[papers/094_AlphaGenome_advancing_regulatory_variant_effect_prediction_w/review]] — 생물학적 경로 추론이 유전체 변이 효과 예측의 기반이 됩니다.
- 🧪 응용 사례: [[papers/726_Sciknoweval_Evaluating_multi-level_scientific_knowledge_of_l/review]] — 과학 지식 평가가 생물학적 경로 추론에 적용됩니다.
