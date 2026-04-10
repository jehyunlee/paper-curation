---
title: "858_Unsupervised_crosslingual_representation_learning_at_scale"
authors:
  - "Alexis Conneau"
  - "Kartikay Khandelwal"
  - "et al. (Facebook AI)"
date: "2019"
doi: "arXiv:1911.02116"
arxiv: ""
score: 4.5
essence: "본 논문은 100개 언어에서 2TB 이상의 필터링된 CommonCrawl 데이터로 사전학습한 XLM-RoBERTa (XLM-R)를 제시하며, 다언어 마스크 언어 모델링이 대규모로 학습될 때 교차언어 전이학습 성능을 크게 향상시킴을 보여준다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/AI_Benchmarking_Taxonomy"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Reimers and Gurevych_2019_Unsupervised crosslingual representation learning at scale.pdf"
---

# Unsupervised Crosslingual Representation Learning at Scale

> **저자**: Alexis Conneau, Kartikay Khandelwal, et al. (Facebook AI) | **날짜**: 2019 | **DOI**: [arXiv:1911.02116](https://arxiv.org/abs/1911.02116)

---

## Essence

![Figure 1](figures/fig1.webp) 
*그림 1: 88개 언어에 대한 데이터 크기 비교 (GiB, 로그 스케일). CommonCrawl은 저자원 언어의 데이터를 수십 배 이상 증가시킴*

본 논문은 100개 언어에서 2TB 이상의 필터링된 CommonCrawl 데이터로 사전학습한 XLM-RoBERTa (XLM-R)를 제시하며, 다언어 마스크 언어 모델링이 대규모로 학습될 때 교차언어 전이학습 성능을 크게 향상시킴을 보여준다.

## Motivation

- **Known**: mBERT와 XLM 같은 다언어 마스크 언어 모델은 Wikipedia 기반 사전학습으로 교차언어 이해 작업에서 진전을 이뤘음
- **Gap**: 기존 모델들은 상대적으로 제한된 규모의 데이터(Wikipedia)에서만 학습되었으며, 저자원 언어의 성능이 여전히 부족함
- **Why**: 단언어 모델의 확장 효과(RoBERTa 등)가 다언어 설정에서도 적용될 수 있는지 체계적으로 검증 필요
- **Approach**: CommonCrawl의 대규모 정제 데이터로 100개 언어를 학습하고, 다언어성의 저주(curse of multilinguality) 등 핵심 트레이드오프를 실증적으로 분석

## Achievement

1. **교차언어 성능 향상**: XNLI에서 평균 14.6% 정확도, MLQA에서 평균 13% F1, NER에서 2.4% F1 향상
2. **저자원 언어 개선**: Swahili 15.7%, Urdu 11.4% XNLI 정확도 향상 (이전 XLM 대비)
3. **단언어 성능 경쟁력**: GLUE와 XNLI에서 RoBERTa 같은 최강 단언어 모델과 경쟁 가능한 성능 달성 (다언어 모델으로는 처음)

## How

![Figure 1 Data Comparison](figures/fig1.webp)

- **데이터 확장**: Wikipedia 대신 정제된 CommonCrawl 사용으로 저자원 언어 데이터 100배 이상 증가
- **모델 아키텍처**: Transformer 기반 MLM 사용, 언어 임베딩 제거 (코드스위칭 개선), 250K 어휘 크기
- **언어 샘플링**: α=0.3 smoothing을 적용한 다언어 배치 샘플링
- **모델 크기**: Base (12층, 768차원, 270M 파라미터)와 Large (24층, 1024차원, 550M 파라미터) 두 가지 제시
- **평가 벤치마크**: XNLI, NER (CoNLL), MLQA, GLUE를 통한 다각적 평가

## Originality

- **다언어성의 저주(Curse of Multilinguality) 명시적 분석**: 고정된 모델 용량에서 언어 수 증가 시 성능 저하 현상을 체계적으로 규명하고, 용량 증가로 완화 가능함을 입증
- **저자원 언어 중심 데이터 구성**: CommonCrawl의 대규모 정제로 저자원 언어의 데이터 부족 문제 해결
- **단언어-다언어 성능 동시 달성**: 단일 모델이 언어별 성능 손실 없이 모든 언어를 처리 가능함을 최초 입증
- **상세한 실증 분석**: 언어 수(7→15→30→60→100), 데이터 크기, 어휘 크기 등 핵심 요소에 대한 체계적 ablation study

## Limitation & Further Study

- **계산 비용**: 모델 용량 증가가 다언어성의 저주를 해결하는 주요 방법이지만, 계산 예산이 제한된 시스템에서는 여전히 트레이드오프 존재
- **100개 언어 한계**: 1000개 이상의 극저자원 언어들은 미포함; 더욱 광범위한 언어 커버리지 필요
- **언어 간 표현 간섭**: 고자원 언어가 저자원 언어 표현을 압도할 수 있는 메커니즘에 대한 심층 분석 부재
- **후속 연구**: (1) 더욱 효율적인 다언어 모델 설계, (2) 제로샷 교차언어 전이 능력 분석, (3) 극저자원 언어에 특화된 전략 개발


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.5/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4.5/5

**총평**: XLM-R은 대규모 다언어 데이터와 모델 확장이 교차언어 이해의 새로운 지평을 열 수 있음을 명확히 보여준 영향력 있는 연구로, 특히 다언어성의 저주 개념 도입과 저자원 언어 성능 혁신이 후속 연구에 미친 영향이 매우 큼. 다만 계산 효율성 측면의 개선 방안은 향후 과제로 남음.

## Related Papers

- 🔗 후속 연구: [[papers/368_Gemini_15_Unlocking_multimodal_understanding_across_millions/review]] — 다언어 표현학습이 멀티모달 이해로 확장되는 자연스러운 발전 경로
- 🧪 응용 사례: [[papers/245_Crosslingual_capabilities_and_knowledge_barriers_in_multilin/review]] — 다언어 능력의 실제적 한계와 지식 장벽을 실증적으로 분석함
- 🔗 후속 연구: [[papers/690_Rule-based_neural_and_llm_back-translation_Comparative_insig/review]] — 대규모 무감독 교차언어 표현 학습이 라딘어와 같은 저자원 언어의 역번역 성능 향상에 적용될 수 있다.
- 🔗 후속 연구: [[papers/755_Simalign_High_quality_word_alignments_without_parallel_train/review]] — 대규모 무감독 크로스링구얼 표현 학습이 SimAlign의 정적/문맥화 임베딩 활용 방식을 더 큰 규모로 확장한 연구임
