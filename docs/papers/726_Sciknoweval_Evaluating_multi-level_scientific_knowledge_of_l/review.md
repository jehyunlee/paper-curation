---
title: "726_Sciknoweval_Evaluating_multi-level_scientific_knowledge_of_l"
authors:
  - "Kehua Feng"
  - "Xinyi Shen"
  - "Weijie Wang"
  - "Xiang Zhuang"
  - "Yuqi Tang"
date: "2024"
doi: "arXiv:2406.09098"
arxiv: ""
score: 4.25
essence: "본 논문은 대규모 언어모델(LLM)의 과학 지식을 5단계(기억, 이해, 추론, 판별, 적용)로 체계적으로 평가하는 28K 규모의 종합 벤치마크 데이터셋 SciKnowEval을 제안한다. 생물학, 화학, 물리학, 재료과학 4개 영역에서 LLM의 과학적 역량을 다층적으로 진단하고 20개 모델을 평가하여 개선의 필요성을 제시한다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Domain-specific_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Feng et al._2024_Sciknoweval Evaluating multi-level scientific knowledge of large language models.pdf"
---

# Sciknoweval: Evaluating multi-level scientific knowledge of large language models

> **저자**: Kehua Feng, Xinyi Shen, Weijie Wang, Xiang Zhuang, Yuqi Tang, Qiang Zhang, Keyan Ding | **날짜**: 2024 | **DOI**: [arXiv:2406.09098](https://arxiv.org/abs/2406.09098)

---

## Essence

![Figure 1](https://arxiv.org/html/2406.09098v4/x1.png)
*Figure 1: SciKnowEval의 전체 구조. (a) 4개 과학 영역, (b) 다양한 데이터 소스, (c) 4가지 질문 유형, (d) 5단계 진행적 지식 수준별 예제, (e) 영역 및 수준별 질문 분포*

본 논문은 대규모 언어모델(LLM)의 과학 지식을 5단계(기억, 이해, 추론, 판별, 적용)로 체계적으로 평가하는 28K 규모의 종합 벤치마크 데이터셋 SciKnowEval을 제안한다. 생물학, 화학, 물리학, 재료과학 4개 영역에서 LLM의 과학적 역량을 다층적으로 진단하고 20개 모델을 평가하여 개선의 필요성을 제시한다.

## Motivation

- **Known**: 최근 Galactica, SciGLM, ChemLLM 등 과학 특화 LLM이 등장하며 과학 연구 분야에서 중요한 역할을 수행 중이다. 일부 벤치마크(AGIEval, MMLU, SciQ 등)에서 과학 문제를 포함하고 있다.

- **Gap**: 기존 벤치마크의 한계점은 (1) 고등학교 수준의 문제만 포함하여 깊이 부족, (2) 체계적 평가 프레임워크 부재로 이해도 제한적, (3) 과학 연구의 윤리 및 안전성 평가 미흡이다.

- **Why**: LLM의 진정한 과학적 역량은 단순 사실 암기를 넘어 이해, 추론, 윤리적 판단, 실제 응용까지 포함해야 하므로, 이를 다층적으로 평가할 종합 벤치마크가 필요하다.

- **Approach**: 공자의 "학이시습지(學而時習之)" 철학에서 영감을 얻아 5단계 진행적 학습 과정을 모방한 평가 프레임워크를 설계하고, 문헌, 교과서, 과학 데이터베이스에서 다양하게 데이터를 수집하여 고품질의 대규모 데이터셋을 구축한다.

## Achievement

![Figure 2](https://arxiv.org/html/2406.09098v4/x2.png)
*Figure 2: 3가지 데이터 수집 방법. (I) 문헌에서 새로운 QA 생성, (II) 기존 QA 재구성, (III) 과학 데이터베이스를 텍스트 형식으로 변환*

1. **포괄적 평가 프레임워크 구축**: 5단계 진행적 지식 평가 체계 (L1: 기억, L2: 이해, L3: 추론, L4: 판별, L5: 적용)를 제안하여 인간의 학습 과정을 반영한 다층적 평가 가능

2. **대규모 고품질 데이터셋 구성**: 28,392개의 다양한 과학 문제를 4개 영역에서 수집하고, 관계 추출, 객관식, 주관식, 참/거짓 질문 등 4가지 형식으로 구성 (L1: 37.15%, L2: 34.22%, L3: 7.43%, L4: 14.39%, L5: 6.81%)

3. **광범위한 모델 평가 및 순위화**: 7개 상용 LLM, 8개 오픈소스 범용 LLM, 5개 과학 특화 LLM 총 20개 모델을 평가하여 각 모델의 강점과 약점 분석

4. **과학 윤리 및 안전성 평가 강화**: L4 판별 단계에서 유해물질 합성, 약물 상호작용 등 과학 관련 안전 문제를 명시적으로 평가

## How

- **데이터 수집 3가지 방식**:
  - (I) 문헌 기반 생성: BioRxiv, PubMed, LibreTexts에서 수집한 논문/교과서 단락에서 LLM을 활용하여 자동으로 QA 쌍 생성
  - (II) 기존 QA 재구성: MedMCQA, SciEval, MMLU, XieZhi, PubMedQA, HarmfulQA 등에서 샘플링한 QA를 LLM으로 리라이팅, 선택지 순서 변경, 수준 자동 분류
  - (III) 과학 데이터베이스 변환: PubChem, UniProtKB, SHARE-seq 등의 구조화된 데이터(분자, 단백질, 세포 서열 정보)를 다양한 질문 템플릿으로 텍스트 형식으로 변환

- **품질 관리**: 도메인 전문가의 조언을 바탕으로 정교한 프롬프트 설계, RDKit을 이용한 화학적으로 유효하지 않은 SMILES 필터링, 엄격한 품질 검수 절차 적용

- **평가 메트릭**: 객관식은 정확도, 주관식은 BLEU, ROUGE, BERTScore 등 활용

## Originality

- **첫 체계적 5단계 평가 프레임워크**: 기존 벤치마크는 단일 차원 평가 또는 제한된 수준만 포함한 반면, 본 논문은 인간의 학습 과정을 철학적으로 반영한 진행적 5단계 평가 체계 제시

- **윤리 및 안전성 통합 평가**: L4 판별 단계를 통해 기존 벤치마크에서 간과한 과학적 해로움, 독성, 윤리적 함의를 명시적으로 평가

- **다양하고 신뢰할 수 있는 데이터 구성**: 문헌, 교과서, 구조화 데이터베이스 3가지 독립적 소스에서 균형있게 데이터 수집하여 편향 최소화

- **대규모 모델 비교 평가**: 상용 모델, 오픈소스 범용 모델, 과학 특화 모델까지 20개 모델을 일관된 프레임워크로 평가하여 생태계 전반 현황 파악 가능

## Limitation & Further Study

- **데이터 생성의 자동화 의존성**: 문헌에서 LLM을 활용한 QA 생성 및 기존 QA의 자동 레벨 분류 시 생성 오류 또는 부정확한 분류 가능성. 인간 검증 비율과 범위가 명확하지 않음

- **L3, L5 비율 불균형**: 추론(L3) 7.43%, 적용(L5) 6.81%으로 상대적으로 적어 고난도 문제에 대한 평가 신뢰도 제한

- **영어 데이터셋 편향**: 수집 소스(PubMed, arXiv 등)가 영어 문헌 중심이므로 다언어 과학 지식 평가 미흡

- **평가 메트릭의 한계**: 주관식 답변에 대해 자동화 메트릭(BLEU, ROUGE)만 사용하여 과학적 정확성의 미묘한 차이 포착 불충분

- **후속 연구 방향**: (1) 인간-LLM 혼합 검증 강화, (2) 다언어 과학 벤치마크 확장, (3) 과학 특화 LLM의 미세조정(fine-tuning) 가이드라인 제시, (4) 시간에 따른 과학 지식 업데이트 메커니즘 개발


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.25/5

**총평**: SciKnowEval은 기존 벤치마크의 한계를 명확히 인식하고 철학적 기초를 갖춘 체계적인 5단계 평가 프레임워크를 제시하며, 28K 규모의 다양한 고품질 데이터셋을 구축하여 과학 LLM 평가의 새로운 표준을 제안한다는 점에서 의의가 크다. 특히 과학 윤리와 안전성 평가를 명시적으로 포함한 점이 실용적 가치를 높인다. 다만 자동 생성 데이터의 검증 비율 명시, 고난도 문제 비율 확충, 주관식 평가의 정성적 메트릭 강화가 필요하다.

## Related Papers

- 🧪 응용 사례: [[papers/556_MolQuest_A_Benchmark_for_Agentic_Evaluation_of_Abductive_Rea/review]] — 다층적 과학 지식 평가가 화학 추론 벤치마크에 적용됩니다.
- 🧪 응용 사례: [[papers/166_Biomaze_Benchmarking_and_enhancing_large_language_models_for/review]] — 과학 지식 평가가 생물학적 경로 추론에 적용됩니다.
- 🔄 다른 접근: [[papers/713_Scicueval_A_comprehensive_dataset_for_evaluating_scientific/review]] — 과학 지식 평가를 위한 서로 다른 포괄적 접근법을 제시합니다.
- 🏛 기반 연구: [[papers/556_MolQuest_A_Benchmark_for_Agentic_Evaluation_of_Abductive_Rea/review]] — 다층적 과학 지식 평가가 화학 귀추적 추론의 기반을 제공합니다.
- 🏛 기반 연구: [[papers/166_Biomaze_Benchmarking_and_enhancing_large_language_models_for/review]] — 다층적 생물학 지식 평가가 경로 추론 벤치마크의 기반을 제공합니다.
- 🏛 기반 연구: [[papers/701_Scholarchemqa_Unveiling_the_power_of_language_models_in_chem/review]] — 과학적 지식 평가의 기초적 접근이 화학 분야 특화 QA 시스템 개발의 이론적 배경을 제공함
