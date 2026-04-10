---
title: "287_Dont_Stop_Pretraining_Adapt_Language_Models_to_Domains_and_T"
authors:
  - "Suchin Gururangan"
  - "Ana Marasović"
  - "Swabha Swayamdipta"
  - "Kyle Lo"
  - "Iz Beltagy"
date: "2020"
doi: "10.18653/v1/2020.acl-main.740"
arxiv: ""
score: 4.5
essence: "광범위한 데이터로 사전학습(pretraining)된 대규모 언어 모델(RoBERTa)을 도메인별·작업별로 추가 적응(adaptation)하면, 다양한 자원 환경에서 지속적인 성능 향상을 달성할 수 있음을 보여준다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Structured_Research_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Gururangan et al._2020_Don’t Stop Pretraining Adapt Language Models to Domains and Tasks.pdf"
---

# Don't Stop Pretraining: Adapt Language Models to Domains and Tasks

> **저자**: Suchin Gururangan, Ana Marasović, Swabha Swayamdipta, Kyle Lo, Iz Beltagy | **날짜**: 2020 | **DOI**: [10.18653/v1/2020.acl-main.740](https://doi.org/10.18653/v1/2020.acl-main.740)

---

## Essence

광범위한 데이터로 사전학습(pretraining)된 대규모 언어 모델(RoBERTa)을 도메인별·작업별로 추가 적응(adaptation)하면, 다양한 자원 환경에서 지속적인 성능 향상을 달성할 수 있음을 보여준다.

## Motivation

- **Known**: RoBERTa와 같은 대규모 사전학습 언어 모델은 160GB 이상의 이질적(heterogeneous) 대규모 텍스트에서 학습되어 다양한 NLP 작업에서 강력한 성능을 보임
- **Gap**: 최신의 광범위한 커버리지(broad-coverage) 모델이 충분히 범용적(universal)인지, 여전히 특정 도메인/작업에 맞춤형 모델 구축이 필요한지에 대한 체계적 검증 부재
- **Why**: 기존 도메인 적응 연구는 단일 도메인만 다루거나 더 작은 사전학습 코퍼스를 사용했으며, 레이블된 데이터 규모나 원본 사전학습 코퍼스와의 거리와 같은 요인의 영향을 미처 조사하지 못함
- **Approach**: 4개 도메인(생의학, 컴퓨터과학, 뉴스, 리뷰)의 8개 분류 작업에 대해 도메인 적응 사전학습(DAPT: Domain-Adaptive PreTraining)과 작업 적응 사전학습(TAPT: Task-Adaptive PreTraining)을 체계적으로 비교 분석

## Achievement

![Figure 2: 도메인 간 어휘 중복도(%) 분석 - RoBERTa 사전학습 도메인(PT)과 각 도메인 간의 유사성 정량화](figures/fig2.webp)
*어휘 중복도를 통한 도메인 유사성 분석: CS와 생의학(BioMed) 도메인이 PT 도메인과 가장 멀리 떨어져 있음*

1. **도메인 적응 사전학습(DAPT)의 일관된 효과**: 생의학, CS, 리뷰 도메인에서 RoBERTa 대비 지속적 성능 향상 달성(예: ACL-ARC 63.0% → 75.4%, CHEMPROT 81.9% → 84.2%). 고자원/저자원 설정 모두에서 개선 확인
   
2. **도메인 적응과 작업 적응의 상승 효과**: DAPT 후 TAPT를 추가로 적용하면 더 큰 성능 향상 달성, 즉 다단계 적응 사전학습(multi-phase adaptive pretraining)이 효과적임을 입증

3. **도메인 관련성의 중요성**: 무관한 도메인으로 적응한 경우(¬DAPT) RoBERTa보다 성능이 악화되어, 단순 데이터 노출 증가가 아닌 도메인 관련성이 핵심 요인임을 증명

4. **자동 데이터 선택 전략**: 인간 큐레이션 데이터 부재 시 간단한 데이터 선택 전략으로 작업 적응 사전학습 성능을 향상시킬 수 있는 실용적 대안 제시

## How

![Figure 1: 데이터 분포의 계층 구조 - 관찰 가능한 작업 분포(task distribution)와 더 넓은 도메인 분포(domain distribution)의 관계 도시](figures/fig1.webp)
*작업 데이터는 도메인 분포의 부분집합이며, 원본 사전학습 도메인과 반드시 겹치지 않음을 시각화*

- **도메인 적응 사전학습(DAPT)**: RoBERTa를 각 도메인의 대규모 비레이블 텍스트(7.55B~8.10B 토큰)에서 12.5K 스텝(단일 epoch) 추가 학습. 마스크 언어 모델(masked language modeling) 목적 함수 유지

- **어휘 중복 분석**: 상위 10K 빈도 단어(stopword 제외)의 도메인 간 겹침 정도로 사전 적응 잠재력 평가. PT(RoBERTa) 도메인과의 거리가 멀수록 높은 개선 예상

- **작업 적응 사전학습(TAPT)**: 각 작업의 비레이블 데이터(레이블된 훈련 데이터와 추가 비레이블 데이터 포함)에서 추가 학습. DAPT와 독립적 또는 순차적 적용 가능

- **제어 실험**: 무관한 도메인으로의 적응(¬DAPT)을 대조 조건으로 설정, 순수한 도메인 관련성 효과만 격리

- **분류 아키텍처**: 표준 접근법([CLS] 토큰 표현을 작업 특화 선형층에 입력)으로 모든 작업 일관성 유지

## Originality

- **체계적 비교 분석의 선도성**: 단일 강력한 기저 모델(RoBERTa)에서 도메인 적응, 작업 적응, 무관한 도메인 적응을 체계적으로 비교한 첫 대규모 연구

- **다차원 분석 축**: 4개 도메인 × 8개 작업 × 고/저 자원 설정을 모두 포괄하는 포괄적 실험 설계

- **도메인 관련성의 정량적 검증**: 어휘 겹침 분석으로 도메인 유사성을 수치화하고, 실제 성능 향상과의 관계를 경험적으로 입증

- **실무적 대안 제시**: 인간 큐레이션 데이터 부재 시 자동 데이터 선택 전략을 제안, 실제 적용 가능성 향상

- **공개 자원 기여**: 학습된 도메인/작업 적응 모델과 코드를 공개하여 후속 연구 활성화

## Limitation & Further Study

- **도메인 정의의 모호성**: 도메인을 장르/포럼 기준으로 정의했으나, 더 세분화된 도메인 정의나 도메인 경계의 유동성에 대한 논의 부재

- **뉴스(NEWS) 도메인의 예외**: 뉴스는 RoBERTa 사전학습 데이터에 이미 포함되어 있어 DAPT 효과가 미미함. 도메인 겹침이 큰 경우의 적응 이점에 대한 깊이 있는 분석 필요

- **적응 학습량의 고정성**: 모든 도메인에서 동일한 12.5K 스텝으로 학습했으나, 도메인별 최적 학습량이 다를 수 있음을 시사하지 않음

- **장거리 의존성 작업의 미포함**: 대부분의 평가 작업이 문장/짧은 텍스트 분류이며, 문서 수준 또는 생성 작업에서의 적응 효과는 미검증

- **다언어/저자원 언어에 대한 확장 부재**: 영어에만 국한된 실험. 언어 다양성에 따른 적응 효과의 변동 가능성

- **후속 연구 방향**:
  - 동적 적응 학습량 결정 알고리즘 개발
  - 도메인과 작업 간의 전이성(transferability) 메커니즘 심화 연구
  - 생성 작업(요약, 기계 번역 등)에서의 적응 효과 검증
  - 도메인 이동(domain shift) 강건성 평가


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 5/5
- Overall: 4.5/5

**총평**: 본 논문은 현대 NLP의 통념(대규모 광범위 모델로 충분함)에 대한 실증적 반박을 제공하는 중요한 연구로, 4개 도메인의 8개 작업에 걸친 체계적 비교를 통해 도메인/작업 적응 사전학습의 일관된 효과를 입증했다. 어휘 겹침 분석으로 적응 이득을 사전에 예측 가능하게 하고, 자동 데이터 선택 전략으로 실무적 적용성을 높였다는 점에서 ACL 2020의 주요 기여 논문으로 평가받을 만하다.

## Related Papers

- 🏛 기반 연구: [[papers/343_Foundation_models_for_materials_discovery__current_state_and/review]] — 도메인 적응 기법이 재료과학 파운데이션 모델의 특화 학습에 필수적이다.
- 🧪 응용 사례: [[papers/306_Efficient_fine-tuning_of_single-cell_foundation_models_enabl/review]] — 언어모델 도메인 적응 방법을 단일세포 파운데이션 모델 미세조정에 적용한다.
- 🔗 후속 연구: [[papers/340_Fine-tuning_large_language_models_for_domain_adaptation_expl/review]] — 도메인 적응을 과학 분야로 확장한 구체적 사례와 실험을 제공한다.
- 🏛 기반 연구: [[papers/343_Foundation_models_for_materials_discovery__current_state_and/review]] — 도메인 적응 기법이 재료과학 파운데이션 모델 개발의 핵심 방법론이다.
- 🏛 기반 연구: [[papers/340_Fine-tuning_large_language_models_for_domain_adaptation_expl/review]] — 도메인 적응의 기본 원리가 과학 분야 LLM 개발의 핵심 방법론이 됨
