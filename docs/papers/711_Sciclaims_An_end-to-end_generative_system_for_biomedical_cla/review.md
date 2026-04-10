---
title: "711_Sciclaims_An_end-to-end_generative_system_for_biomedical_cla"
authors:
  - "Raúl Ortega"
  - "José Manuel Gómez-Pérez"
date: "2025"
doi: "미제공"
arxiv: ""
score: 4.0
essence: "SciClaims는 생의학 텍스트에서 과학적 주장을 자동으로 추출하고, PubMed에서 관련 증거를 검색한 후, 단일 대규모 언어모델(LLM)을 사용하여 검증하는 통합 시스템이다. 체계적 문헌고찰(Systematic Literature Review, SLR)과 특허 검증 등 고위험도 활용 사례를 지원한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Fact_Verification_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ortega and G'omez-P'erez_2025_Sciclaims An end-to-end generative system for biomedical claim analysis.pdf"
---

# SciClaims: An end-to-end generative system for biomedical claim analysis

> **저자**: Raúl Ortega, José Manuel Gómez-Pérez | **날짜**: 2025 | **DOI**: [미제공](https://doi.org/)

---

## Essence

![Figure 1: System Architecture](figures/fig1.webp)
*시스템 아키텍처: Llama3 8B Instruct 모델과 Elasticsearch 기반 검색 엔진으로 구성된 생의학 논문 분석 파이프라인*

SciClaims는 생의학 텍스트에서 과학적 주장을 자동으로 추출하고, PubMed에서 관련 증거를 검색한 후, 단일 대규모 언어모델(LLM)을 사용하여 검증하는 통합 시스템이다. 체계적 문헌고찰(Systematic Literature Review, SLR)과 특허 검증 등 고위험도 활용 사례를 지원한다.

## Motivation

- **Known**: 기존 방법론들은 청구 추출(claim extraction), 증거 검색(evidence retrieval), 검증(verification)의 개별 단계에 대해서는 상당한 진전을 이루었으나, 이들을 통합한 end-to-end 시스템은 여전히 미흡함. 특히 많은 시스템이 이미 식별된 주장에만 초점을 맞추고 원본 텍스트에서 주장을 추출하는 첫 단계를 무시함.

- **Gap**: 생의학 문헌에서 자동으로 주장을 추출하고, 대규모 문헌 코퍼스에서 관련 증거를 검색하며, 이를 검증하는 완전한 파이프라인이 부재함. 또한 기존 방법론들은 다단계 NLP 파이프라인으로 인한 실패에 취약하고 문서당 과도한 수의 주장을 생성하는 문제가 있음.

- **Why**: 체계적 문헌고찰은 생의학 연구와 제약산업에서 임상 의사결정, 규제 제출, R&D 파이프라인을 지원하는 핵심 작업이나, 과학적 주장의 검증은 노동집약적이고 오류 가능성이 높으며 점증하는 과학 논문 수로 인해 확장이 어려움.

- **Approach**: 단일 GPU에서 효율적으로 동작하도록 최적화된 Llama3 8B Instruct 모델을 기반으로 하는 통합 시스템 개발. 추출-검색-검증의 세 단계를 자연어 설명과 증거 강조를 포함하여 웹 인터페이스로 제공.

## Achievement

![Figure 2: SciClaims 데모 인터페이스](figures/fig2.webp)
*사용자 인터페이스: 입력 텍스트 분석 시 추출된 주장, 검증 결과, 관련 증거, 근거 제시*

1. **포괄적 End-to-End 파이프라인**: 주장 추출, 증거 검색, 검증을 단일 LLM으로 통합하여 추가 미세조정(fine-tuning) 없이 구현. 기존 다단계 파이프라인의 실패 가능성을 제거하고 인터프리터빌리티(interpretability) 향상.

2. **실제 배포 최적화**: 24GB VRAM GPU 하나에서 효율적으로 동작하며, 최대 10,000자 길이의 문서 처리 가능. vLLM을 활용한 고처리량 추론으로 실시간 성능 구현.

3. **품질 높은 증거 코퍼스**: Semantic Scholar의 Highly Influential Citations 메트릭으로 큐레이션된 4.7백만 개 PubMed 초록(2000-2022) 활용. 각 문서는 최소 3개의 고도로 인용된 논문으로 지지받음.

4. **사용자 친화적 인터페이스**: 30개 이상의 사전 설정 예제(생의학 논문, COVID 관련 뉴스, SNS, 특허) 제공. 모순된 증거에 대해 모든 관련 쌍을 반환하여 사용자가 정확도를 판단 가능. 신뢰성 점수(confidence score)와 근거(rationale) 제시.

## How

![Figure 1 재참조: 시스템 아키텍처 상세 구조](figures/fig1.webp)

- **Claim Extraction (청구 추출)**
  - Llama3 8B Instruct 모델에 두 번 호출
  - 첫 호출: 초기 청구 목록 생성
  - 두 번째 호출: 청구 정제 및 필터링으로 품질 개선
  - 원자적 사실 단위(atomic factual units) 생성으로 간결성과 해석 가능성 확보

- **Document Retrieval (문서 검색)**
  - Elasticsearch 인덱스 기반 검색
  - 청구를 쿼리로 사용하여 관련 문서 검색
  - Elasticsearch 스코링으로 필터링하지 않고 최대 재현율(recall) 확보
  - 후속 검증 모듈에서 무관련 문서 제거

- **Claim Verification (청구 검증)**
  - LLM에 청구와 검색된 문서 함께 제공
  - 3가지 레이블 할당: SUPPORT, REFUTE, NEI (Not Enough Information)
  - 근거 제공: 결정을 뒷받침하는 가장 관련성 높은 문장 식별
  - 자연언어 근거(rationale)로 투명성과 해석 가능성 강화

- **구현 기술**
  - 백엔드: Llama3 8B Instruct + vLLM
  - 검색: Elasticsearch (BM-25 기반)
  - 프론트엔드: 웹 기반 인터페이스
  - 공개: 데모, 코드(백엔드/프론트엔드) 및 튜토리얼 영상 공개

## Originality

- **통합 파이프라인의 새로운 실현**: 기존 개별 부품 중심의 접근에서 벗어나 주장 추출부터 검증까지 단일 LLM 기반 완전 통합 시스템 구현. 추가 미세조정 불필요.

- **실용적 배포 설계**: 단일 GPU 최적화로 실제 운영 환경에 적합한 경량 시스템 구현. BM-25와 Elasticsearch를 선택하여 검색 품질과 계산 효율성의 균형 달성.

- **높은 품질의 증거 기반**: Semantic Scholar 인용 지표 기반 큐레이션으로 신뢰성 높은 PubMed 코퍼스 구성. 기존 일반 코퍼스 대비 향상된 증거 품질.

- **투명성 강화 설계**: 신뢰성 점수, 근거 문장 강조, 자연언어 설명 제공으로 의료/제약 등 고위험도 도메인의 신뢰 가능성 높임.

- **확장성**: 30개 이상의 다양한 예제(학술지, 뉴스, SNS, 특허)로 광범위한 사용 사례 시연.

## Limitation & Further Study

- **검증 데이터 제한**: 평가가 주로 SciFact 벤치마크와 LLM 판사(LLM-as-judge) 평가에 의존하며, 제한된 인간 평가만 수행됨. 더 광범위한 인간 평가가 필요.

- **검색 정확도**: Elasticsearch 기반 검색은 Dense Passage Retrieval(ColBERT 등)보다 정확도가 낮을 수 있음. 계산 효율성과 검색 정확도의 트레이드오프 존재.

- **주장 품질 변동성**: 추출된 주장의 품질이 입력 텍스트 특성에 따라 변할 수 있으며, 매우 기술적이거나 모호한 표현에서의 성능 미검토.

- **시간 역학(Temporal Dynamics)**: 시스템이 PubMed 2000-2022 데이터로 제한되어 최신 과학적 발견 반영 부족. 정기적 코퍼스 업데이트 메커니즘 부재.

- **도메인 외(Out-of-Domain) 적용**: 생의학 특화 시스템으로 다른 과학 분야(물리학, 화학 등) 적용성 미검증.

**후속 연구 방향**:
- 더 신선한 데이터로의 확장 및 동적 업데이트 메커니즘
- Dense Retrieval 방법론 통합을 통한 검색 정확도 향상
- 다중 도메인 적용성 평가
- 사용자 피드백 루프를 통한 반복적 개선 시스템 구축

## Evaluation

- **Novelty (독창성)**: 4/5
  - End-to-end 통합 파이프라인 및 실제 배포 최적화에서 높은 독창성. 다만 개별 기술(LLM 기반 추출, BM-25 검색, LLM 검증)은 기존 방법론의 조합.

- **Technical Soundness (기술 타당성)**: 4/5
  - 시스템 아키텍처는 견고하고 실용적. SciFact 평가에서 기준선 대비 개선 입증. 그러나 인간 평가 규모가 제한적이고, 일부 설계 선택(BM-25 vs Dense Retrieval)의 정당성 논증 부족.

- **Significance (중요성)**: 4/5
  - 체계적 문헌고찰과 특허 검증 등 고위험도 영역에서의 실질적 영향력 존재. 공개 데모 및 코드 제공으로 확장성 높음. 다만 도메인 특화성으로 인한 일반화 제한.

- **Clarity (명확성)**: 4/5
  - 시스템 설명, 아키텍처, 인터페이스가 명확하고 이해하기 쉬움. 프롬프트와 구현 세부사항이 부록에 포함. 다만 일부 평가 방법론(LLM-as-judge 기준 상세함) 설명 보충 필요.

- **Overall (종합평가)**: 4/5
  - 생의학 도메인의 실제 문제를 종합적으로 해결하는 잘 설계된 실용 시스템. 공개 배포 및 접근성 높은 인터페이스가 장점. 평가의 깊이와 도메인 외 적용성 입증이 개선 영역.

**총평**: SciClaims는 과학적 주장 검증의 완전한 파이프라인을 단일 LLM으로 통합하여 실제 배포 가능하도록 최적화한 우수한 시스템 데모이다. 생의학 분야의 체계적 문헌고찰 같은 고위험도 활용에 직접적 가치를 제공하며, 공개 코드와 인터페이스를 통해 재현성과 확장성을 담보한다. 다만 평가 범위 확대와 도메인 외 적용성 검증으로 더욱 강화될 수 있다.

## Related Papers

- 🔄 다른 접근: [[papers/657_Reading_and_Reasoning_over_Chart_Images_for_Evidence-based_A/review]] — 생의학 주장 분석과 차트 기반 팩트 체킹은 모두 증거 기반 검증을 수행하지만 텍스트와 시각적 증거라는 다른 정보원을 활용한다.
- 🏛 기반 연구: [[papers/880_What_makes_medical_claims_un_verifiable_analyzing_entity_and/review]] — 의료 주장의 검증 가능성 분석이 생의학 주장의 자동 추출과 검증에서 처리 가능한 주장 유형을 식별하는 핵심 기준을 제공한다.
- 🔗 후속 연구: [[papers/602_Paperqa_Retrieval-augmented_generative_agent_for_scientific/review]] — 과학적 질의응답을 위한 검색 증강 에이전트를 생의학 주장 분석이라는 특화된 도메인으로 확장하여 더 정밀한 증거 검색과 검증이 가능하다.
- 🔄 다른 접근: [[papers/657_Reading_and_Reasoning_over_Chart_Images_for_Evidence-based_A/review]] — 차트 기반 팩트 체킹과 생의학 주장 검증은 서로 다른 증거 유형을 활용하지만 동일한 증거 기반 검증 프레임워크를 공유한다.
- 🔗 후속 연구: [[papers/880_What_makes_medical_claims_un_verifiable_analyzing_entity_and/review]] — 의료 주장의 검증 가능성 분석이 생의학 주장의 자동 분석 시스템에서 처리 가능한 주장을 사전에 필터링하는 핵심 구성 요소로 활용된다.
