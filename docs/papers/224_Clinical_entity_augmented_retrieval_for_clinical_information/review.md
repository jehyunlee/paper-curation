---
title: "224_Clinical_entity_augmented_retrieval_for_clinical_information"
authors:
  - "Iván López"
  - "Akshay Swaminathan"
  - "Karthik S. Vedula"
  - "Sanjana Narayanan"
  - "F. Nateghi Haredasht"
date: "2025"
doi: "10.1038/s41746-024-01377-1"
arxiv: ""
score: 4.5
essence: "임상 노트에서 정보를 추출할 때 임상 엔티티(clinical entities)를 기반으로 관련 정보만 효율적으로 검색하여 대규모 언어모델(LLM)에 제공하는 CLEAR 파이프라인을 제안하며, 기존 embedding 기반 검색 대비 70% 이상의 토큰 사용량 감소와 추론 시간 단축을 달성하면서도 성능을 개선했다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Publication_Concept_Extraction"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/López et al._2025_Clinical entity augmented retrieval for clinical information extraction.pdf"
---

# Clinical entity augmented retrieval for clinical information extraction

> **저자**: Iván López, Akshay Swaminathan, Karthik S. Vedula, Sanjana Narayanan, F. Nateghi Haredasht | **날짜**: 2025 | **DOI**: [10.1038/s41746-024-01377-1](https://doi.org/10.1038/s41746-024-01377-1)

---

## Essence

임상 노트에서 정보를 추출할 때 임상 엔티티(clinical entities)를 기반으로 관련 정보만 효율적으로 검색하여 대규모 언어모델(LLM)에 제공하는 CLEAR 파이프라인을 제안하며, 기존 embedding 기반 검색 대비 70% 이상의 토큰 사용량 감소와 추론 시간 단축을 달성하면서도 성능을 개선했다.

## Motivation

- **Known**: 대규모 언어모델(LLM)과 검색 증강 생성(RAG)은 임상 정보 추출에서 이전 방법들보다 성능이 우수하나, embedding 기반 검색의 비효율성이 문제임. 또한 임상 노트의 길이가 LLM의 context window를 초과할 수 있고, 입력 길이 증가에 따라 LLM의 추론 성능이 저하됨.

- **Gap**: 기존 embedding RAG는 관련성 없는 정보까지 검색하여 계산 비용을 증가시키고, 성능을 저하시킬 수 있음. chunk embedding 또는 full-note 접근법은 과도한 토큰 사용과 긴 추론 시간의 문제를 해결하지 못함.

- **Why**: 전자건강기록(EHR)의 비정형 텍스트에 포함된 증상, 진단, 사회적 결정요인 등의 임상 정보를 효율적으로 추출해야 코호트 선택, 표현형화(phenotyping), 관찰 데이터 분석, 예측 모델링 등의 연구 및 품질 개선이 가능함.

- **Approach**: 임상 엔티티 인식(NER), 온톨로지 기반 증강, LLM 기반 동의어 생성을 통해 쿼리와 관련된 임상 엔티티를 식별하고, 이러한 엔티티를 포함하는 노트 청크만 검색하여 LLM에 전달하는 CLEAR 파이프라인 개발.

## Achievement

![Figure 3](figures/fig3.webp) *CLEAR 파이프라인의 개요: (1) 임상 노트와 (2) 쿼리를 입력받아 엔티티 기반 검색을 수행*

1. **성능 우수성**: Stanford MOUD 데이터셋에서 CLEAR의 평균 F1 점수는 0.90으로, embedding RAG(0.86)과 full-note(0.79) 접근법을 능가함. 6개 LLM 모두에서 CLEAR이 최고 또는 경쟁력 있는 성능 달성.

2. **효율성 극대화**: 
   - 추론 시간: CLEAR 4.95초 vs. embedding RAG 17.41초 vs. full-note 20.08초 (각 노트당)
   - 모델 쿼리 횟수: CLEAR 1.68회 vs. embedding RAG 4.94회 vs. full-note 4.18회
   - 평균 입력 토큰: CLEAR 1.1k vs. embedding RAG 3.8k vs. full-note 6.1k
   - **전체적으로 70% 이상의 토큰 사용량 및 추론 시간 감소**

3. **다양한 임상 변수 검증**: 물질 사용(alcohol dependence, tobacco dependence), 정신건강(ADHD, bipolar disorder, depression), 사회적 결정요인(homelessness, unemployment), 흉부 X-ray 소견(pneumonia, cardiomegaly) 등 18개 임상 변수에서 평가.

4. **BERT 모델 미세조정 가능성**: CLEAR로 생성한 라벨로 Bio+Clinical BERT 모델을 미세조정했을 때, 알코올 의존성과 만성 통증에서 LLM trainer 모델의 F1 점수를 초과하는 성능 달성.

## How

![Figure 1](figures/fig1.webp) *Stanford MOUD 데이터셋에서 NER 제거 시 CLEAR 정보 검색의 F1 점수 변화: 일부 변수는 작은 감소, 일부는 큰 감소를 보임*

- **1단계 - Named Entity Recognition (NER)**: Flan-T5 기반의 zero-shot NER을 사용하여 임상 노트에서 관심 엔티티 인식 (NCBI disease: 96% sensitivity, Stanford MOUD: 99% sensitivity)

- **2단계 - 엔티티 증강**: 
  - UMLS 온톨로지를 통한 유의어(synonyms) 확장
  - GPT-4를 사용한 임상적 유의어 생성
  - 이를 통해 sensitivity를 99~100%로 향상

- **3단계 - 엔티티 선택**: 쿼리와 관련된 엔티티만 선택하는 필터링 단계로 노이즈 제거

- **4단계 - 청크 검색**: 선택된 엔티티를 포함하는 노트 청크만 검색하여 LLM의 context window에 맞게 구성

- **5단계 - 정보 추출**: 검색된 청크를 포함한 프롬프트로 LLM이 타겟 임상 변수 추출

## Originality

- **엔티티 기반 RAG의 도입**: 기존의 embedding 기반 유사도 검색과 달리, 명시적인 임상 엔티티를 활용한 새로운 RAG 접근법 제안

- **다층 엔티티 증강 전략**: NER, 온톨로지, LLM 기반 동의어 생성을 조합하여 임상 표현의 다양성 포괄

- **실제 임상 데이터 기반 대규모 검증**: 20,000개 임상 노트, 6개 LLM, 18개 임상 변수에 걸친 체계적 평가

- **약한 지도학습(weak supervision) 대비 우수성 입증**: 정규표현식 기반 약한 지도학습 대비 CLEAR의 성능 우위 시연

- **경량 모델로의 지식 이전 가능성**: LLM으로 생성한 라벨로 BERT 크기의 모델 미세조정이 실용적 적용 가능함을 입증

## Limitation & Further Study

- **NER 의존성**: NER 단계가 여전히 일부 엔티티를 놓칠 수 있으며, 특히 substance use disorder(F1 감소 0.40)처럼 복잡한 개념의 표현 다양성 포괄에 한계

- **온톨로지 완성도 의존**: UMLS 온톨로지에 없는 신규 임상 용어나 도메인별 특화 용어는 증강 불가능

- **도메인 특화성**: 대부분 내부 Stanford 데이터셋과 공개 CheXpert 데이터셋에서만 평가되었으므로, 다른 의료기관의 노트 구조나 임상 표현에 대한 일반화 검증 필요

- **인과관계 및 복잡한 관계 추출**: 질병 간의 인과관계, 약물 부작용 등 복잡한 의미관계 추출에 대한 평가 부재

- **후속 연구 방향**:
  - 다기관 데이터셋에서의 전이학습 가능성 탐색
  - 실시간 임상 의사결정 지원 시스템으로의 통합 평가
  - 생성형 엔티티나 관계 추출 작업으로의 확장
  - 환자 프라이버시와 보안을 고려한 온프레미스 배포 전략

## Evaluation

- **Novelty**: 4/5 - 엔티티 기반 RAG 개념은 신선하나, 개별 기술 요소는 기존 방법 조합

- **Technical Soundness**: 5/5 - 철저한 실험 설계, 우수한 inter-rater reliability(κ=0.86-0.93), 체계적 ablation study

- **Significance**: 4/5 - 임상 정보 추출의 실제 적용성 높음, 계산 효율성 대폭 개선, 하지만 특정 임상 변수에서의 한계 존재

- **Clarity**: 5/5 - 명확한 파이프라인 구조, 상세한 실험 결과 보고, 보충 자료가 충실

- **Overall**: 4.5/5

**총평**: 이 논문은 임상 정보 추출에서 embedding 기반 검색의 비효율성을 명확히 인식하고 엔티티 기반의 실질적 대안을 제시하는 실용적이고 검증된 연구이다. 대규모 임상 데이터셋에서 일관되게 우수한 성능과 효율성을 입증했으나, 온톨로지 의존성과 도메인 특화성 측면에서는 추가 개선의 여지가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/593_Openscholar_Synthesizing_scientific_literature_with_retrieva/review]] — 임상 정보 추출을 위한 엔티티 기반 검색과 과학 문헌 합성을 위한 일반적 검색 증강의 서로 다른 접근법을 제시합니다.
- 🏛 기반 연구: [[papers/335_Few-shot_Learning_with_Retrieval_Augmented_Language_Models/review]] — 검색 증강 언어모델의 기본 원리를 임상 도메인에 특화하여 적용한 실제 구현 사례입니다.
- 🔗 후속 연구: [[papers/768_Splade_v2_Sparse_lexical_and_expansion_model_for_information/review]] — 희소 렉시컬 검색 모델을 임상 엔티티 기반 검색으로 발전시킨 도메인 특화 응용 연구입니다.
- 🧪 응용 사례: [[papers/335_Few-shot_Learning_with_Retrieval_Augmented_Language_Models/review]] — 검색 증강 언어모델의 일반적 원리를 임상 정보 추출이라는 구체적 도메인에 적용한 사례입니다.
- 🔄 다른 접근: [[papers/593_Openscholar_Synthesizing_scientific_literature_with_retrieva/review]] — 일반적인 과학 문헌 검색 합성과 임상 도메인 특화 엔티티 기반 검색이라는 서로 다른 전문 분야 접근법입니다.
- 🔗 후속 연구: [[papers/424_Improving_health_question_answering_with_reliable_and_time-a/review]] — 임상 정보 검색의 개체 증강을 건강 질문 답변의 시간 인식 증거 검색으로 확장한 고도화된 방법입니다.
