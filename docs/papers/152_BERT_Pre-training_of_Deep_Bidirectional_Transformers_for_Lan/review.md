---
title: "152_BERT_Pre-training_of_Deep_Bidirectional_Transformers_for_Lan"
authors:
  - "Jacob Devlin"
  - "Ming-Wei Chang"
  - "Kenton Lee"
  - "Kristina Toutanova"
date: "2018"
doi: "10.48550/ARXIV.1810.04805"
arxiv: ""
score: 4.7
essence: "BERT는 양방향(Bidirectional) 자기주의(Self-Attention)를 활용하여 마스크된 토큰 예측(Masked Language Model, MLM) 목표로 사전학습한 심층 트랜스포머 인코더로, 최소한의 파인튜닝만으로 11개 NLP 작업에서 최고 성능을 달성한 혁신적인 언어 표현 모델이다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Scientific_Language_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Devlin et al._2018_BERT Pre-training of Deep Bidirectional Transformers for Language Understanding.pdf"
---

# BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

> **저자**: Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova | **날짜**: 2018 | **DOI**: [10.48550/ARXIV.1810.04805](https://doi.org/10.48550/ARXIV.1810.04805)

---

## Essence

![Figure 1](BERT_architecture.png) *그림 1: BERT의 전체 사전학습 및 파인튜닝 절차. 동일한 아키텍처가 사전학습과 파인튜닝에 사용되며, 특수 토큰 [CLS]와 [SEP]를 통해 다양한 NLP 작업 처리*

BERT는 양방향(Bidirectional) 자기주의(Self-Attention)를 활용하여 마스크된 토큰 예측(Masked Language Model, MLM) 목표로 사전학습한 심층 트랜스포머 인코더로, 최소한의 파인튜닝만으로 11개 NLP 작업에서 최고 성능을 달성한 혁신적인 언어 표현 모델이다.

## Motivation

- **Known**: ELMo와 OpenAI GPT 같은 기존 사전학습 모델들이 NLP 성능 개선에 효과적이며, 특히 GPT의 파인튜닝 기반 접근법이 주목받고 있음
- **Gap**: 기존 언어 모델들은 단방향(좌→우 또는 우→좌)으로만 학습되므로, 양방향 문맥을 동시에 활용하는 심층 양방향 표현을 얻기 어려움. GPT의 좌→우 제약은 질의응답 같은 토큰 수준 작업에서 특히 해로움
- **Why**: 표준 조건부 언어 모델에서 양방향 학습 시 토큰이 자기 자신을 간접적으로 "볼" 수 있어 자명한 예측이 가능해지는 문제 해결 필요
- **Approach**: Cloze 작업에서 영감을 받아 입력 토큰의 일부를 무작위로 마스킹한 후 원래 값을 예측하는 MLM 목표로 양방향 조건화를 가능하게 함

## Achievement

![Figure 3](BERT_comparison.png) *그림 3: BERT는 양방향 트랜스포머를 사용하며, OpenAI GPT는 좌측 문맥만 참조하는 제약된 자기주의 사용*

1. **11개 주요 NLP 벤치마크에서 최고 성능 달성**
   - GLUE: 80.5% (기존 대비 +7.7%p)
   - MultiNLI: 86.7% (+4.6%p)
   - SQuAD v1.1: 93.2 F1점 (+1.5%p)
   - SQuAD v2.0: 83.1 F1점 (+5.1%p)

2. **파인튜닝 기반 표현 모델 중 최초로 문장 수준 및 토큰 수준 작업에서 모두 최고 성능 달성**

3. **작업별 복잡한 아키텍처 설계 필요성 제거** - 최소한의 출력층 추가만으로 다양한 작업 처리 가능

## How

![Figure 2](BERT_input.png) *그림 2: BERT 입력 표현 구성. 토큰 임베딩, 세그먼트 임베딩, 위치 임베딩의 합으로 구성*

### 모델 아키텍처
- **기반**: 멀티층 양방향 트랜스포머 인코더 (Vaswani et al., 2017)
- **2가지 크기**: 
  - BERT_BASE: 12층, 768 은닉 크기, 12 헤드, 1.1억 개 파라미터
  - BERT_LARGE: 24층, 1024 은닉 크기, 16 헤드, 3.4억 개 파라미터
- **핵심 차이**: GPT의 제약된 자기주의(좌측만) vs BERT의 양방향 자기주의

### 입력 표현
- **WordPiece 임베딩**: 30,000 토큰 어휘
- **특수 토큰**: [CLS] (분류 작업용 집계 표현), [SEP] (문장 분리)
- **세그먼트 임베딩**: 문장 A/B 구분
- **위치 임베딩**: 토큰의 절대 위치 정보
- 각 토큰의 입력 표현 = 토큰 임베딩 + 세그먼트 임베딩 + 위치 임베딩

### 사전학습 목표

**Task #1: 마스크된 언어 모델(MLM)**
- 입력 토큰의 15%를 무작위로 마스킹
- 마스킹된 토큰의 최종 은닉 벡터에 소프트맥스를 적용하여 원래 어휘 ID 예측
- 양방향 문맥 활용으로 기존 단방향 언어 모델의 제약 해결

**Task #2: 다음 문장 예측(NSP)**
- 문장 쌍 입력: [CLS] + 문장 A + [SEP] + 문장 B + [SEP]
- 문장 B가 실제 다음 문장인지 무작위 문장인지 분류
- 문장 간 관계 이해 능력 강화

### 파인튜닝
- 사전학습된 모델의 모든 파라미터를 작업별 레이블된 데이터로 파인튜닝
- 작업별 출력층만 추가 (분류, 토큰 분류, 시작/종료 스팬 예측 등)
- 동일한 사전학습 모델에서 출발하지만 작업별로 독립적인 파인튜닝 모델 생성

## Originality

- **양방향 심층 사전학습의 혁신**: 기존의 ELMo (좌→우/우→좌의 얕은 연결) 또는 GPT (순방향만)와 달리, MLM을 통해 진정한 양방향 조건화를 모든 층에서 달성

- **간단하면서도 강력한 설계**: Cloze 작업이라는 고전적 NLP 개념을 현대적 심층 학습에 적용하여 개념적 단순성과 실증적 강력함을 동시에 달성

- **통합된 아키텍처의 우월성**: 사전학습과 파인튜닝 단계에서 거의 동일한 아키텍처를 유지하면서도 다양한 작업에서 최고 성능 달성 - 작업별 맞춤형 아키텍처의 필요성 제거

- **NSP 작업 도입**: 문장 쌍 관계 학습으로 자연언어 추론, 의역 탐지 등 문장 수준 작업 성능 향상

## Limitation & Further Study

- **계산 비용**: BERT_LARGE의 3.4억 개 파라미터는 사전학습 및 파인튜닝에 상당한 계산 자원 필요 - 경량 모델 개발 및 지식 증류(Knowledge Distillation) 기법 필요

- **마스킹 비율 최적화**: 논문에서 15% 마스킹 비율 사용하나, 다양한 작업별 최적 비율에 대한 상세 분석 부족

- **NSP 작업의 유효성**: 일부 후속 연구에서 NSP 제거가 성능 감소를 유발하지 않는다는 결과 보고 - NSP의 실제 기여도에 대한 재검토 필요

- **다국어 및 도메인 특화 모델**: 본 논문은 영어 일반 도메인 중심 - 다른 언어와 특정 도메인(의료, 법률 등)에 대한 BERT 적응 필요

- **해석 가능성**: 양방향 학습이 어떤 언어적 지식을 습득하는지에 대한 심층 분석 부족 - 어텐션 가시화 및 프로빙 작업(probing tasks)을 통한 후속 연구 필요

## Evaluation

- **Novelty**: 4.5/5
  - MLM을 통한 양방향 사전학습은 새로우나, 개별 구성요소(마스킹, 트랜스포머)는 기존 기술. 개념적 혁신성은 높지만 기술적 참신성은 중간

- **Technical Soundness**: 5/5
  - 모델 설계, 사전학습 목표, 파인튜닝 절차 모두 견고함. 광범위한 실험으로 검증됨

- **Significance**: 5/5
  - 11개 NLP 작업에서 최고 성능, 이후 수년간 NLP 분야의 표준 모델로 자리잡음. 학문적·실무적 영향력 극대

- **Clarity**: 5/5
  - 모델 구조, 목표 함수, 파인튜닝 절차가 명확하게 설명됨. 논문 후 공개된 코드와 사전학습 모델이 재현성 극대화

- **Overall**: 4.7/5

**총평**: BERT는 MLM이라는 우아한 아이디어로 양방향 심층 사전학습을 달성하고 최소한의 아키텍처 수정으로 다양한 NLP 작업에서 최고 성능을 보임으로써, 현대 NLP의 기초를 마련한 획기적 연구이다. 높은 계산 비용과 일부 설계 선택(NSP)의 유효성 재검토 여지는 있으나, 학문적 영향력과 실무 적용성 측면에서 최상의 기여를 했다.

## Related Papers

- 🔗 후속 연구: [[papers/707_SciBERT_A_Pretrained_Language_Model_for_Scientific_Text/review]] — BERT의 과학 도메인 특화 버전으로 과학 텍스트에서 더 나은 성능을 달성함
- 🔄 다른 접근: [[papers/659_REALM_Retrieval-Augmented_Language_Model_Pre-Training/review]] — BERT의 암묵적 지식 저장 방식과 달리 명시적 검색을 통해 지식을 활용하는 다른 접근법
- 🔗 후속 연구: [[papers/161_BioBERT_a_pre-trained_biomedical_language_representation_mod/review]] — BERT를 생의학 도메인에 특화시켜 의료 텍스트 이해 성능을 개선함
- 🔗 후속 연구: [[papers/367_Galactica_A_Large_Language_Model_for_Science/review]] — BERT의 과학 도메인 확장판으로 1200억 토큰의 과학 논문으로 학습된 대규모 모델
- 🔄 다른 접근: [[papers/659_REALM_Retrieval-Augmented_Language_Model_Pre-Training/review]] — BERT의 암묵적 지식 저장과 달리 외부 코퍼스에서 명시적 검색을 통한 지식 활용 방식
- 🔗 후속 연구: [[papers/707_SciBERT_A_Pretrained_Language_Model_for_Scientific_Text/review]] — BERT의 일반 도메인 사전학습을 과학 텍스트에 특화시켜 과학 NLP 성능을 향상
- 🔄 다른 접근: [[papers/467_Large_Language_Models/review]] — 트랜스포머 기반 언어모델과 양방향 사전훈련 모델이 서로 다른 언어 이해 접근법을 제시합니다.
