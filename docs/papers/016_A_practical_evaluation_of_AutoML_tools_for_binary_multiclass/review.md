---
title: "016_A_practical_evaluation_of_AutoML_tools_for_binary_multiclass"
authors:
  - "Marcelo V. C. Aragão"
  - "Augusto G. Afonso"
  - "Rafaela C. Ferraz"
  - "Rairon G. Ferreira"
  - "Sávio G. Leite"
date: "2025.05"
doi: "10.1038/s41598-025-02149-x"
arxiv: ""
score: 4.0
essence: "16개의 주요 AutoML 도구를 21개의 실제 데이터셋에서 이진, 다중클래스, 다중라벨 분류 작업으로 체계적으로 벤치마킹하여, 각 도구의 성능-효율성 트레이드오프를 분석한 종합 평가 연구이다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/AI_Benchmarking_Taxonomy"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Aragão et al._2025_A practical evaluation of AutoML tools for binary, multiclass, and multilabel classification.pdf"
---

# A practical evaluation of AutoML tools for binary, multiclass, and multilabel classification

> **저자**: Marcelo V. C. Aragão, Augusto G. Afonso, Rafaela C. Ferraz, Rairon G. Ferreira, Sávio G. Leite, Felipe A. P. De Figueiredo, Samuel B. Mafra | **날짜**: 2025-05-21 | **DOI**: [10.1038/s41598-025-02149-x](https://doi.org/10.1038/s41598-025-02149-x)

---

## Essence


16개의 주요 AutoML 도구를 21개의 실제 데이터셋에서 이진, 다중클래스, 다중라벨 분류 작업으로 체계적으로 벤치마킹하여, 각 도구의 성능-효율성 트레이드오프를 분석한 종합 평가 연구이다.

## Motivation

- **Known**: 여러 AutoML 도구들이 존재하며, 각각 고유한 특성을 가지고 있으나, 이진/다중클래스 분류에 대한 벤치마킹 연구는 있었지만 세 분류 유형을 모두 포함하는 통합적 평가 연구는 부족했다.
- **Gap**: 기존 벤치마크 연구들은 (1) 분류 작업의 일부만 포함, (2) 제한된 도구 수만 평가, (3) 다중라벨 분류의 네이티브 vs 라벨-파워셋(label-powerset) 표현 비교 부재, (4) 엄격한 다층 통계 검증 부족의 문제가 있다.
- **Why**: AutoML의 급속한 산업 채택에도 불구하고, 세 가지 분류 유형을 모두 포함하면서 통계적으로 엄격하고 재현 가능한 단일 벤치마크가 필요하며, 이는 실무자와 연구자들의 최적 도구 선택에 필수적이다.
- **Approach**: 16개의 Python 기반 AutoML 프레임워크를 21개의 실제 데이터셋에서 5분의 시간 제약 하에 운영하고, 가중 F1 점수와 학습 시간을 표준화된 메트릭으로 사용하며, 데이터셋별-전체 데이터셋-통합 수준에서 다층 통계 검증을 수행한다.

## Achievement


- **포괄적 벤치마킹**: 이진, 다중클래스, 네이티브 다중라벨, 라벨-파워셋 다중라벨 작업을 동시에 다루는 첫 번째 체계적 AutoML 비교 연구
- **도구별 성능 특성 규명**: AutoSklearn은 높은 정확도(장시간 학습), Lightwood/AutoKeras는 빠른 학습(낮은 정확도), AutoGluon은 정확도-효율성 균형
- **다중라벨 분류 심층 분석**: 네이티브 및 라벨-파워셋 표현 비교를 통해 여러 도구의 다중라벨 기능 제약 발견
- **다층 통계 검증**: 데이터셋별, 전체 데이터셋 간, 통합 수준의 의미 있는 성능 차이 확인으로 정확도-속도 트레이드오프 정량화
- **재현성 보장**: 오픈소스 코드 및 전체 통계 스크립트 공개로 연구 결과의 신뢰성과 확장성 제공

## How

![Figure 2](figures/fig2.webp)

*Figure 2 illustrates the general workflow of HPO, emphasizing its iterative nature. The problem setup includes*

- 16개 AutoML 도구 선정: AutoGluon, AutoSklearn, TPOT, PyCaret, Lightwood 등 주요 프레임워크 포함
- 21개 실제 데이터셋 구성: 이진, 다중클래스, 다중라벨 분류 작업을 모두 포함
- 5분 시간 제약의 하드웨어 제어 실험 설계로 동일 조건에서 평가
- 표준화된 메트릭: 가중 F1 점수(weighted-F1) 및 학습 시간 측정
- 다층 통계 검증: (1) 데이터셋별 분석, (2) 데이터셋 간 비교, (3) 통합 수준 유의성 검사
- 기존 4개의 대표적 벤치마크와 비교하여 결과 검증
- 네이티브 vs 라벨-파워셋 다중라벨 표현 방식 비교 분석

## Originality

- 세 분류 유형(이진, 다중클래스, 다중라벨)을 동시에 포함하는 첫 번째 통합 벤치마크
- 다중라벨 분류에서 네이티브와 라벨-파워셋 표현의 명시적 비교 분석
- 데이터셋별-전체 데이터셋-통합 수준의 삼층 구조 통계 검증 프레임워크
- 기존 벤치마크(Truong et al., Wever et al., Gijbers et al.)의 한계를 모두 보완하는 포괄적 설계
- 도구의 정확도-속도 트레이드오프를 정량적으로 분석하는 체계적 접근

## Limitation & Further Study

- 5분 시간 제약이 일부 고급 AutoML 도구의 성능을 제한할 수 있으며, 장시간 실험의 필요성
- 21개 데이터셋의 규모가 전체 자동화 학습 문제 공간을 완전히 대표하기에는 제한적
- 특정 도메인(의료, 금융 등)의 데이터셋 부재로 도메인 특화 성능 분석 부족
- 실험 당시 존재하는 도구만 평가하였으므로 신규 도구 출현 시 재평가 필요
- **후속 연구**: 장시간 시간 제약 실험, 더 큰 데이터셋 규모 포함, 도메인 특화 분석, 신규 AutoML 도구 추가 평가

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 연구는 AutoML 도구 선택의 실무적 어려움을 해결하기 위해 세 분류 유형을 모두 포함한 최초의 체계적이고 통계적으로 엄격한 벤치마크를 제시하며, 재현 가능한 실험 프로토콜과 공개 코드를 통해 학술 및 산업계에 즉각적인 가치를 제공한다.

## Related Papers

- 🧪 응용 사례: [[papers/006_A_deep_subgrouping_framework_for_precision_drug_repurposing/review]] — AutoML 도구의 체계적 벤치마킹 방법론은 정밀 약물 재창출을 위한 딥러닝 프레임워크의 성능 평가에 직접 적용될 수 있습니다
- 🔄 다른 접근: [[papers/713_Scicueval_A_comprehensive_dataset_for_evaluating_scientific/review]] — AutoML 도구 벤치마킹과 과학적 맥락 이해 평가는 모두 AI 시스템의 실제 성능을 종합적으로 측정하는 서로 다른 접근법입니다
- 🏛 기반 연구: [[papers/135_Automl_in_the_age_of_large_language_models_Current_challenge/review]] — 대형 언어모델 시대의 AutoML 현재 도전과 미래 방향은 AutoML 도구 실제 평가의 이론적 맥락과 발전 방향을 제시합니다
- 🔄 다른 접근: [[papers/713_Scicueval_A_comprehensive_dataset_for_evaluating_scientific/review]] — AutoML 도구의 체계적 벤치마킹과 과학적 맥락 이해 평가는 모두 AI 시스템의 실제 성능을 종합적으로 측정하는 서로 다른 접근법입니다
- 🏛 기반 연구: [[papers/006_A_deep_subgrouping_framework_for_precision_drug_repurposing/review]] — AutoML 도구의 실제 데이터셋 체계적 벤치마킹은 정밀 약물 재창출을 위한 딥러닝 프레임워크 평가의 방법론적 기반을 제공합니다
