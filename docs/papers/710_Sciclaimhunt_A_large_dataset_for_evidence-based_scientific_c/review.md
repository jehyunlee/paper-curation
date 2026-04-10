---
title: "710_Sciclaimhunt_A_large_dataset_for_evidence-based_scientific_c"
authors:
  - "Sujit Kumar"
  - "Anshul Sharma"
  - "Siddharth Hemant Khincha"
  - "Gautam Shroff"
  - "Sanasam Ranbir Singh"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "본 논문은 과학 논문에서 추출한 대규모 научных 주장 검증 데이터셋 SciClaimHunt와 SciClaimHunt Num을 소개한다. 정치적 주장과 달리 과학적 주장의 검증은 도메인 전문성과 복잡한 기술 용어를 요구하는 고도의 과제이며, 이를 해결하기 위해 87,109개의 주장과 이를 지원하거나 반박하는 과학 논문 증거로 구성된 대규모 데이터셋을 제시한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Data_Interpretation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Kumar et al._2025_Sciclaimhunt A large dataset for evidence-based scientific claim verification.pdf"
---

# Sciclaimhunt: A large dataset for evidence-based scientific claim verification

> **저자**: Sujit Kumar, Anshul Sharma, Siddharth Hemant Khincha, Gautam Shroff, Sanasam Ranbir Singh, Rahul Mishra | **날짜**: 2025 | **DOI**: N/A

---

## Essence

본 논문은 과학 논문에서 추출한 대규모 научных 주장 검증 데이터셋 SciClaimHunt와 SciClaimHunt Num을 소개한다. 정치적 주장과 달리 과학적 주장의 검증은 도메인 전문성과 복잡한 기술 용어를 요구하는 고도의 과제이며, 이를 해결하기 위해 87,109개의 주장과 이를 지원하거나 반박하는 과학 논문 증거로 구성된 대규모 데이터셋을 제시한다.

## Motivation

- **Known**: 정치적 또는 뉴스 관련 주장 검증에 대한 팩트체킹 연구는 활발하며, SCIFACT, SCIFACT-OPEN 등의 과학 주장 검증 데이터셋이 존재한다.

- **Gap**: 기존 과학 주장 검증 데이터셋의 한계:
  - (i) 규모가 매우 제한적 (수천 개 샘플)
  - (ii) 연구 논문의 초록(abstract)만을 증거로 사용하여 정보 부족
  - (iii) 인용문 포함 문장에서만 주장 추출하여 결과/토론/결론 섹션의 중요한 통찰 누락
  - (iv) 수치 또는 기수(cardinal values)를 포함하는 과학 주장 데이터셋 부재

- **Why**: 전문 도메인 지식이 필요하고 복잡한 증거를 다루는 과학 주장 검증을 위해서는 충분한 규모와 다양성의 훈련 데이터가 필수적이다.

- **Approach**: LLM 기반 소수-샷(few-shot) 프롬팅을 활용하여 과학 논문의 결과/토론/결론 섹션에서 긍정적 주장을 자동 생성하고, 부정(negation), 명명된 개체 교체(NER), 수치 변경 등 4가지 방법으로 반박 주장을 생성한다.

## Achievement

1. **대규모 데이터셋 구축**: 87,109개의 주장-증거 쌍으로 구성된 SciClaimHunt (훈련/개발/테스트: 87,109/10,884/10,900)와 수치 값을 포함하는 20,319개 주장의 SciClaimHunt Num 데이터셋 제시

2. **높은 품질 보증**: Krippendorff α (0.693-0.784)와 Fleiss kappa (0.699-0.823) 점수를 통해 인간 주석 간 높은 일치도 달성, 유창성(fluency), 원자성(atomicity), 문맥 독립성(decontextualization), 충실성(faithfulness) 4가지 평가 기준 충족

3. **포괄적 검증**: 검색 증강 생성(RAG) 기반 기선 모델과 다중 헤드 어텐션을 활용한 주장-증거 매칭 방법론 제시 및 평가

## How

- **긍정적 주장 생성**: Promptagator 방식의 소수-샷 프롬팅으로 Llama 2 13B 모델에 12개 예제 쌍(수동 추출된 주장-단락)을 제공하여 새로운 주장 자동 생성

- **부정적 주장 생성 (4가지 방법)**:
  - (i) LLM 기반 강력한 부정(strong negation): 방법론/결과 변경
  - (ii) 주장-논문 미스매칭: 참인 (C_i, R_i) 쌍을 (C_i, R_j)로 재조합하여 반박 관계 형성
  - (iii) 수치/기수 값 변경: 주장 내 정량적 정보 수정
  - (iv) 다른 전략: 상세 기술 없음

- **증거 활용**: 연구 논문의 전체 본문을 증거로 사용 (초록만 아님), 특히 결과/토론/결론 섹션 중점

## Originality

- 기존 연구 대비 **10배 이상 규모** 확대 (기존: 1-5천 개 → 본 논문: 87,109개)

- **다중 섹션 활용**: 인용 관련 문장만 아닌 결과/토론/결론 섹션 포함으로 더 실질적인 과학 주장 포착

- **수치 인식 검증**: 주장과 증거 간 수치적 일관성 검증이라는 새로운 부작업 정의 (SciClaimHunt Num)

- **완전한 논문 컨텍스트**: 초록만이 아닌 전체 본문을 증거로 사용하여 실제 과학 검증 작업에 더 근접

- **다층적 부정 전략**: 단순 명명된 개체 교체를 넘어 강력한 부정, 미스매칭, 수치 변경 등 다양한 음성 샘플 생성 방법론

## Limitation & Further Study

- **LLM 자동생성의 한계**: Llama 2 기반 소수-샷 프롬팅으로 생성된 주장의 품질이 완전히 보장되지 않을 수 있으며, 다양한 LLM 모델 비교 실험 부족

- **도메인 범위**: 과학 논문 전체 도메인이 균등하게 포함되었는지 불명확 (특정 분야 편향 가능성)

- **인간 평가 규모**: 전체 87,109개 주장 중 일부만 인간 평가되었을 것으로 추정되며, 전체 데이터셋의 정확한 오류율 분석 필요

- **후속 연구 방향**:
  - 바이오메디컬 등 특정 도메인별 성능 분석
  - 초다국어(multilingual) 과학 주장 검증 데이터셋 확장
  - 더 정교한 증거 검색 기법과 LLM 통합 모델 개발
  - 제로-샷(zero-shot) 과학 주장 검증 능력 향상 연구

## Evaluation

- **Novelty**: 4/5
  - 규모와 품질에서 기존 데이터셋 크게 상회하나, 기본 개념(증거 기반 주장 검증)은 기존 연구와 동일

- **Technical Soundness**: 4/5
  - 체계적인 데이터 생성 및 인간 평가 절차가 합리적이나, LLM 기반 자동 생성의 잠재적 노이즈에 대한 상세 분석 부족

- **Significance**: 4.5/5
  - 과학 주장 검증 연구 커뮤니티에 즉시 활용 가능한 대규모 고품질 자원 제공으로 높은 실제 가치 있음

- **Clarity**: 4/5
  - 전반적으로 명확하나, 4가지 부정 생성 방법 중 일부(특히 4번째)가 본문 제시 전에 끝남

- **Overall**: 4.2/5

**총평**: 본 논문은 과학 주장 검증을 위한 기존의 규모 제한적이고 초록 중심적인 데이터셋의 한계를 실질적으로 해결하며, 결과/토론/결론 섹션을 포함한 전체 논문 컨텍스트와 수치 인식 검증이라는 새로운 평가 차원을 도입함으로써 과학 팩트체킹 연구에 상당한 기여를 할 것으로 기대된다.

## Related Papers

- 🔗 후속 연구: [[papers/629_Pre_A_peer_review_based_large_language_model_evaluator/review]] — 과학적 주장 검증의 엄밀성을 LLM 기반 동료 평가 시스템의 신뢰성 향상에 적용합니다.
- 🏛 기반 연구: [[papers/151_Benchmarking_ai_scientists_in_omics_data-driven_biological_r/review]] — 과학적 주장의 증거 기반 검증이 AI 과학자의 생물학적 발견 능력 평가의 기준을 제공합니다.
- 🔄 다른 접근: [[papers/486_Lego-prover_Neural_theorem_proving_with_growing_libraries/review]] — 과학적 검증이라는 동일한 목표를 문헌 기반 주장 검증과 논리적 정리 증명이라는 다른 방식으로 달성합니다.
- 🔗 후속 연구: [[papers/579_Nsf-scify_Mining_the_nsf_awards_database_for_scientific_clai/review]] — NSF 데이터를 확장하여 증거 기반 과학적 주장 탐지 시스템으로 발전
- 🔗 후속 연구: [[papers/151_Benchmarking_ai_scientists_in_omics_data-driven_biological_r/review]] — 과학적 주장 검증을 생물학적 발견 평가로 확장하여 AI 과학자의 신뢰성을 높입니다.
- 🔗 후속 연구: [[papers/486_Lego-prover_Neural_theorem_proving_with_growing_libraries/review]] — 과학적 주장 검증을 수학적 증명 검증으로 확장하여 더 엄밀한 논리적 추론을 구현합니다.
- 🏛 기반 연구: [[papers/629_Pre_A_peer_review_based_large_language_model_evaluator/review]] — 과학적 주장의 증거 기반 검증이 LLM 동료 평가 시스템의 신뢰성 확보에 핵심적 역할을 합니다.
