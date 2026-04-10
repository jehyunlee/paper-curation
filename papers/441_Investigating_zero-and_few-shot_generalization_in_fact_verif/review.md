---
title: "441_Investigating_zero-and_few-shot_generalization_in_fact_verif"
authors:
  - "Liangming Pan"
  - "Yunxiang Zhang"
  - "Min-Yen Kan"
date: "2023"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "본 논문은 fact verification(FV) 모델의 zero-shot 및 few-shot 일반화 능력을 체계적으로 조사한 첫 번째 연구로, 11개 FV 데이터셋을 수집하여 도메인 간 전이 학습의 현황을 분석하고 개선 방안을 제시한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Fact_Verification_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Pan et al._2023_Investigating zero-and few-shot generalization in fact verification.pdf"
---

# Investigating zero-and few-shot generalization in fact verification

> **저자**: Liangming Pan, Yunxiang Zhang, Min-Yen Kan | **날짜**: 2023 | **DOI**: N/A

---

## Essence

본 논문은 fact verification(FV) 모델의 zero-shot 및 few-shot 일반화 능력을 체계적으로 조사한 첫 번째 연구로, 11개 FV 데이터셋을 수집하여 도메인 간 전이 학습의 현황을 분석하고 개선 방안을 제시한다.

## Motivation

- **Known**: FEVER 같은 Wikipedia 기반 대규모 FV 데이터셋으로 학습한 모델들이 뛰어난 성능을 보이고 있음. 최근 다양한 도메인(뉴스, 소셜미디어, 과학 문서 등)에서 FV 데이터셋들이 구축되고 있음.

- **Gap**: 인간 주석은 시간이 많이 걸리고 비용이 높기 때문에 모든 도메인에서 충분한 labeled data를 확보하기 어렵다. 기존 연구에서는 FV 모델이 도메인 간에 어떻게 일반화되는지, 어느 정도까지 기존 데이터셋을 활용할 수 있는지 분석하지 않았다.

- **Why**: 저자원 도메인(scholarly documents, social media)에서 효과적인 FV 시스템을 구축하려면, 고자원 도메인(Wikipedia)의 주석 데이터를 어떻게 활용할 수 있는지 이해해야 한다.

- **Approach**: 8개의 핵심 FV 데이터셋을 선별하고 증거의 세분성에 따라 처리하여 총 11개 데이터셋을 구성한 후, RoBERTa 모델을 이용해 source-target 데이터셋 쌍에 대한 zero-shot 및 few-shot 성능을 체계적으로 평가.

## Achievement

1. **포괄적 벤치마크 데이터셋 구축**: 6개 도메인(Wikipedia, Climate, Science, Health, Forum, Question)의 11개 FV 데이터셋을 표준화된 (claim, evidence, label) 형식으로 통합. Group I은 인공 claim(FEVER, VitaminC, FoolMeTwice), Group II는 자연 claim(Climate-FEVER, Sci-Fact, PubHealth, COVID-Fact, FAVIQ)을 포함.

2. **일반화 능력 부족 실증**: RoBERTa 기반 FV 모델들이 특정 학습 데이터셋에 과적합되어 타 도메인으로의 zero-shot 전이에서 심각한 성능 저하를 보임. 특히 Wikipedia 기반 인공 claim으로 학습한 모델의 실제 도메인(real-world domains) 성능이 낮음.

3. **일반화에 영향을 미치는 요인 규명**: 
   - 데이터셋 크기 증가에 따른 자연 claim으로의 일반화 개선
   - 증거 길이(evidence length)의 중요성
   - Claim 유형(인공 vs 자연)에 따른 차이
   - 데이터셋 간 lexical 및 semantic 차이

4. **일반화 개선 방법 제시**: 
   - 도메인 특화 사전학습(Domain-specific Pretraining): 전문 도메인으로 학습된 언어 모델로 초기화
   - 데이터 증강(Data Augmentation): 자동 claim 생성을 통한 훈련 데이터 생성

5. **Few-shot 성능 개선**: 소량의 타겟 도메인 훈련 데이터로 미세조정하면 성능이 상당히 향상됨을 입증.

## How

- **데이터셋 선별 기준**: 텍스트 기반 증거, human-annotated 문서/문장 수준 증거, 이진/3진 라벨을 포함하는 데이터셋만 선택

- **데이터셋 처리**: 
  - 모든 데이터셋을 통일된 (claim, evidence, label) 삼중항 형식으로 변환
  - 증거 세분성에 따라 문장 수준(sent-level)과 문서 수준(doc-level) 변형 생성 → 11개 데이터셋

- **실험 설정**:
  - Zero-shot: source 데이터셋으로 학습 → target 데이터셋에서 평가 (추가 훈련 데이터 없음)
  - Few-shot: 소량의 target 훈련 예제 추가 활용
  - 모델: RoBERTa-large (355M parameters), [CLS] claim [SEP] evidence 입력 형식

- **평가 지표**: 3진 분류(supports/refutes/NEI)에 대한 macro-averaged F1

- **분석 방법**: 
  - tSNE를 통한 데이터셋 표현 분석
  - Confusion matrix를 통한 오분류 패턴 분석
  - 데이터셋 크기, 증거 길이, claim 유형별 영향도 분석

## Originality

- **첫 번째 종합 분석**: 기존 연구는 개별 FV 데이터셋에 초점을 맞췄으나, 본 논문은 최초로 11개 데이터셋을 포함한 포괄적 cross-domain 일반화 분석 수행

- **표준화된 벤치마크**: 서로 다른 형식의 FV 데이터셋들을 통일된 형식으로 처리하여 공정한 비교 가능

- **체계적 인자 분석**: 단순한 성능 평가를 넘어 데이터셋 크기, 증거 길이, claim 유형 등 구체적 요인들이 일반화에 미치는 영향을 체계적으로 규명

- **실무적 해결책 제시**: 도메인 특화 사전학습과 자동 claim 생성이라는 두 가지 실질적 개선 방안 제안

- **공개 리소스**: 데이터셋 컬렉션과 코드를 공개하여 향후 연구 지원

## Limitation & Further Study

- **모델 제한성**: RoBERTa만 사용했으며, 다른 최신 모델(BERT, ELECTRA, 대형 언어 모델 등)에서의 일반화 능력은 미검토

- **데이터셋 편향**: 많은 원본 데이터셋이 공식 테스트셋을 공개하지 않아 train/dev 분할을 사용. 이는 평가 신뢰도에 영향을 미칠 수 있음

- **도메인 특화 사전학습의 한계**: 특정 도메인의 추가 사전학습 코퍼스 확보 어려움, 높은 계산 비용, 모델 간 유연성 부족

- **자동 claim 생성의 문제**: 생성된 claim의 라벨 일관성, 다양성, 실제 도메인과의 일치도 미흡

- **증거 검색 과정 부재**: 본 논문은 gold evidence가 주어진 상황에만 초점을 맞춤. 실제 환경에서는 증거 검색(evidence retrieval)이 중요한 병목

- **후속 연구 방향**:
  - 다양한 모델 아키텍처 및 사전학습 방식 탐색
  - 멀티태스크 학습, meta-learning 등 고급 전이 학습 기법 적용
  - 증거 검색과 검증을 통합한 end-to-end 시스템 연구
  - 도메인 간 특성 차이를 학습하는 적응형(adaptive) 방법론 개발
  - 인간 주석 효율성을 높이는 능동 학습(active learning) 적용

## Evaluation

- **Novelty**: 4.5/5
  - 체계적인 cross-domain 분석의 부재를 처음으로 다룸. 다만 개별 기법의 참신성은 중간 수준

- **Technical Soundness**: 4/5
  - 데이터셋 통합 및 실험 설계는 견고하나, 단일 모델 사용과 제한된 분석 방법이 아쉬움

- **Significance**: 4.5/5
  - FV 커뮤니티에 중요한 벤치마크와 인사이트 제공. 공개 리소스는 높은 실용적 가치를 가짐

- **Clarity**: 4/5
  - 전반적으로 잘 구성되었으나, 데이터셋 처리 세부사항(특히 NEI 증거 검색)과 일부 분석 결과의 해석에 대한 상세 설명 부족

- **Overall**: 4.2/5

**총평**: 본 논문은 fact verification의 도메인 일반화 문제를 처음으로 종합적으로 분석한 의미 있는 연구로, 체계적인 벤치마크 구축과 실무적 개선 방안 제시를 통해 해당 분야에 기여하지만, 단일 모델 사용과 제한된 개선 기법 등에서 보완의 여지가 있다.

## Related Papers

- 🏛 기반 연구: [[papers/332_Fact-checking_complex_claims_with_program-guided_reasoning/review]] — 팩트 검증 모델의 일반화 능력 분석이 복잡한 주장의 프로그램 가이드 팩트체킹 시스템 개발의 기초를 제공함
- 🔗 후속 연구: [[papers/827_Towards_effective_extraction_and_evaluation_of_factual_claim/review]] — 기본적인 팩트 검증의 일반화 문제를 주장 추출과 평가의 더 복잡한 프로세스로 확장함
- 🏛 기반 연구: [[papers/859_Unsupervised_pretraining_for_fact_verification_by_language_m/review]] — 팩트 검증을 위한 비지도 사전학습 방법이 zero-shot 및 few-shot 일반화 연구의 방법론적 기초를 제공함
- 🏛 기반 연구: [[papers/117_Augmenting_the_veracity_and_explanations_of_complex_fact_che/review]] — 사실 검증에서 제로샷과 퓨샷 일반화 조사는 복잡한 사실 검증에서 설명 일관성과 핫스팟 인식 능력 평가의 이론적 기반을 제공합니다
- 🔗 후속 연구: [[papers/332_Fact-checking_complex_claims_with_program-guided_reasoning/review]] — 기본적인 팩트 체킹을 복잡한 주장의 프로그램 가이드 추론으로 확장하여 더 정교한 사실 검증 방법을 제시함
- 🔗 후속 연구: [[papers/827_Towards_effective_extraction_and_evaluation_of_factual_claim/review]] — 팩트 검증의 일반화 문제를 주장 추출의 품질 평가와 모호성 처리라는 더 세부적인 프로세스로 확장함
