---
title: "905_If_in_a_Crowdsourced_Data_Annotation_Pipeline_a_GPT-4__Proce"
authors:
  - "Zeyu He"
  - "Chieh-Yang Huang"
  - "Chien-Kuang Cornelia Ding"
  - "Shaurya Rohatgi"
  - "Ting-Hao Kenneth Huang"
date: "1145"
doi: "10.1145/3613904.3642834"
arxiv: ""
score: 4.0
essence: "GPT-4와 최적화된 크라우드소싱 파이프라인의 데이터 라벨링 능력을 비교한 연구로, GPT-4가 개별 성능에서 우수하지만 라벨 집계(Label Aggregation)를 통해 크라우드 라벨과 결합하면 더 높은 정확도를 달성할 수 있음을 보여줌."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Domain-adapted_Instruction_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/He et al._If in a Crowdsourced Data Annotation Pipeline, a GPT-4  Proceedings of the 2024 CHI Conference on H.pdf"
---

# If in a Crowdsourced Data Annotation Pipeline, a GPT-4 | Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems

> **저자**: Zeyu He, Chieh-Yang Huang, Chien-Kuang Cornelia Ding, Shaurya Rohatgi, Ting-Hao Kenneth Huang | **날짜**:  | **DOI**: [10.1145/3613904.3642834](https://doi.org/10.1145/3613904.3642834)

---

## Essence

![Figure 4](figures/fig4.webp)

*Figure 4: Aggregation Methods for All Workers, Exclude-By-Worker, and Exclude-By-Batch. Among the various models and*

GPT-4와 최적화된 크라우드소싱 파이프라인의 데이터 라벨링 능력을 비교한 연구로, GPT-4가 개별 성능에서 우수하지만 라벨 집계(Label Aggregation)를 통해 크라우드 라벨과 결합하면 더 높은 정확도를 달성할 수 있음을 보여줌.

## Motivation

- **Known**: 최근 연구들은 GPT-4가 Amazon Mechanical Turk(MTurk) 워커들보다 데이터 라벨링 정확도에서 우월하다고 주장함. 하지만 이러한 연구들은 표준 크라우드소싱 관행을 벗어났고 개별 워커 성능에만 초점을 맞춰 비판을 받아옴.
- **Gap**: 기존 연구들은 개별 워커 성능에만 집중했으나, 실제 크라우드소싱 파이프라인의 전체 과정(인터페이스 설계, 라벨 집계 알고리즘 등)을 고려한 홀리스틱한 비교 연구가 부재함. 또한 데이터 오염 우려가 있는 기존 데이터셋을 사용하는 문제가 있음.
- **Why**: LLM 시대에 크라우드소싱의 역할과 베스트 프랙티스가 재정의되어야 하며, GPT-4와 크라우드 라벨의 상호보완적 강점을 활용하는 방안을 모색하는 것이 중요함.
- **Approach**: 415명의 MTurk 워커가 2022년 이후 출판된 200개의 학술 논문에서 3,177개의 문장 세그먼트를 5분류(Background, Purpose, Method, Finding/Contribution, Other)로 라벨링하도록 하고, 8가지 라벨 집계 알고리즘을 적용하여 GPT-4와 비교함.

## Achievement

![Figure 4](figures/fig4.webp)

*Figure 4: Aggregation Methods for All Workers, Exclude-By-Worker, and Exclude-By-Batch. Among the various models and*

- **GPT-4의 우월성 확인**: 최적화된 MTurk 파이프라인의 최고 정확도 81.5%를 GPT-4의 83.6%가 상회 (p<0.05)
- **하이브리드 접근의 우수성**: GPT-4 라벨을 고급 워커 인터페이스 수집 라벨과 결합하면 2개 알고리즘에서 87.5%, 87.0% 정확도 달성 (p<0.01)
- **상호보완성 발견**: 크라우드가 Finding/Contribution 클래스에 우수하고 GPT-4가 다른 클래스에 우수한 상호보완적 강점 파악
- **홀리스틱 평가**: 표준 크라우드소싱 관행을 준수하면서 전체 파이프라인을 평가한 첫 체계적 연구

## How


- 2022년 이후 출판된 학술 논문 200개에서 3,177개 문장 세그먼트 수집
- 415명의 MTurk 워커 모집 (Master Qualification 미사용, 공정한 보수 제공)
- 2가지 워커 인터페이스 설계 (기본 인터페이스, 고급 인터페이스) 적용
- 각 문장 세그먼트당 20개의 라벨 수집 (총 127,080개 라벨)
- Majority Voting, DawidSkene 등 8가지 라벨 집계 알고리즘 적용
- GPT-4에 동일한 라벨링 작업 수행 요청
- 정확도(Accuracy) 기반 성능 비교 및 통계적 유의성 검증
- 워커와 GPT-4의 라벨링 패턴 분석 및 상호보완성 검토

## Originality

- 기존 연구의 주요 비판점들(데이터 오염, 비표준 크라우드소싱 관행)을 해결하기 위해 신규 데이터셋 구성
- 개별 워커 성능이 아닌 전체 라벨링 파이프라인의 성능을 평가하는 홀리스틱 접근
- GPT-4 단독 사용이 아닌 크라우드-LLM 하이브리드 접근의 가치를 처음으로 체계적으로 입증
- 2가지 워커 인터페이스를 통해 인터페이스 설계의 영향을 통제하는 엄격한 실험 설계

## Limitation & Further Study

- 단일 라벨링 작업(문장 분류)에만 초점이 맞춰져 다양한 NLP 작업에 대한 일반화 가능성 미확인
- CODA-19 스킴의 5개 클래스로 제한되어 다른 분류 체계에서의 성능은 알 수 없음
- 415명의 워커는 유의미한 규모이나 대규모 크라우드소싱 환경에서의 결과 재현성 검증 필요
- GPT-4의 지식 차단일(2021년 9월) 이후의 최신 정보 라벨링 능력은 평가 안 됨
- **후속 연구 방향**: (1) 다양한 NLP 작업(개체명 인식, 감정 분석 등)에서의 일반화, (2) 비용-효율성 분석(크라우드 비용 vs. API 비용), (3) GPT-4 외 다른 LLM(Claude, Llama 등)과의 비교, (4) 동적 라벨 집계 방식 개발, (5) 워커 전문성 수준에 따른 성능 차이 분석

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 기존 GPT-4 vs 크라우드 워커 비교 연구의 방법론적 문제점을 충실히 해결하면서, 최적화된 크라우드소싱 파이프라인의 정확성을 검증하고 GPT-4와의 하이브리드 접근이 더 나은 성능을 제공할 수 있음을 입증했다는 점에서 높은 학술적 가치를 가짐. 특히 LLM 시대 크라우드소싱의 새로운 역할을 제시한 중요한 연구임.

## Related Papers

- 🔄 다른 접근: [[papers/206_ChatGPT_outperforms_crowd_workers_for_text-annotation_tasks/review]] — 둘 다 크라우드소싱 vs AI 성능 비교를 다루지만 하나는 데이터 주석에서 GPT-4와 크라우드워커 비교에, 다른 하나는 텍스트 주석 작업에서 ChatGPT와 크라우드워커 비교에 초점을 맞춘다.
- 🔗 후속 연구: [[papers/128_Automatically_evaluating_the_paper_reviewing_capability_of_l/review]] — LLM의 논문 리뷰 능력 자동 평가 프레임워크가 GPT-4와 크라우드소싱 데이터 라벨링 품질 비교 연구에 적용될 수 있다.
- 🏛 기반 연구: [[papers/373_Generalization_Bias_in_Large_Language_Model_Summarization_of/review]] — 대규모 언어 모델 요약에서의 일반화 편향 연구가 GPT-4와 크라우드소싱 파이프라인의 데이터 주석 품질 차이를 이해하는 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/206_ChatGPT_outperforms_crowd_workers_for_text-annotation_tasks/review]] — 크라우드소싱 데이터 주석에서 GPT-4의 활용 연구로 텍스트 주석 작업의 자동화 범위를 확장합니다.
