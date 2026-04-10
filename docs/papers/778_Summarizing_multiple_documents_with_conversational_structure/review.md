---
title: "778_Summarizing_multiple_documents_with_conversational_structure"
authors:
  - "Miao Li"
  - "Eduard Hovy"
  - "Jey Han Lau"
date: "2023"
doi: "arXiv:2305.01498"
arxiv: ""
score: 4.2
essence: "학술 논문 심사 과정에서 메타리뷰(meta-review)를 자동 생성하기 위해 리뷰어들의 상충된 의견과 다중 순환 대화를 포함한 계층적 구조를 갖춘 새로운 다중문서 요약 데이터셋(PEERSUM)과 이를 활용하는 관계-인식 모델(RAMMER)을 제안한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Scientific_Literature_Summarization"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liu et al._2023_Summarizing multiple documents with conversational structure for meta-review generation.pdf"
---

# Summarizing multiple documents with conversational structure for meta-review generation

> **저자**: Miao Li, Eduard Hovy, Jey Han Lau | **날짜**: 2023 | **DOI**: [arXiv:2305.01498](https://arxiv.org/abs/2305.01498)

---

## Essence

![Figure 1](figures/fig1.webp)
*계층적 대화 구조를 가진 PEERSUM 데이터셋 예시: 공식 리뷰, 저자 응답, 공개 리뷰 등이 스레드 형태로 조직됨*

학술 논문 심사 과정에서 메타리뷰(meta-review)를 자동 생성하기 위해 리뷰어들의 상충된 의견과 다중 순환 대화를 포함한 계층적 구조를 갖춘 새로운 다중문서 요약 데이터셋(PEERSUM)과 이를 활용하는 관계-인식 모델(RAMMER)을 제안한다.

## Motivation

- **Known**: 기존 다중문서 요약(MDS) 데이터셋은 뉴스나 위키피디아 도메인에 집중되어 있으며, 문서 간 명시적 구조나 관계 정보를 제공하지 않음

- **Gap**: 문서 간 상충하는 정보, 계층적 대화 구조, 상호참조 등 복잡한 관계를 명시적으로 다루는 MDS 데이터셋과 방법론 부족

- **Why**: 메타리뷰 생성은 개별 리뷰, 저자-리뷰어 대화, 논문 초록 등 다양한 출처의 정보를 통합해야 하며, 리뷰어들 간 의견 충돌을 처리해야 함. 이는 기계의 추론, 집계, 요약 능력을 평가하는 좋은 프로브(probe)가 될 수 있음

- **Approach**: (1) 명시적 계층적 대화 구조와 상충 관계 표시를 포함한 PEERSUM 데이터셋 구성 (2) Transformer의 주의(attention) 메커니즘을 관계-인식 희소 주의(sparse attention)로 대체하고 메타데이터 예측을 위한 다중 작업 학습을 도입한 RAMMER 모델 제안

## Achievement

![Figure 1](figures/fig1.webp)
*PEERSUM의 계층적 구조: 공식 리뷰 스레드, 저자 응답, 공개 리뷰, 논문 초록 등이 트리 구조로 구성됨 (평균 높이 3.63, 너비 5.31)*

1. **PEERSUM 데이터셋**: 14,993개 샘플(ICLR 2018-2022, NeurIPS 2021-2022)로 구성. 기존 MDS 데이터셋과 달리:
   - 명시적 계층적 대화 구조 포함
   - 높은 추상성(abstractiveness): 유니그램 42%, 바이그램 77%, 트라이그램 81%가 소스 문서에 없음
   - 신뢰도 높음(faithfulness): 메타리뷰가 소스 문서를 충실히 반영
   - 상충 샘플 13.6%: 리뷰 평점 차이 ≥4인 경우 명시적 표시

2. **RAMMER 모델의 성능**: 자동 평가 메트릭(ROUGE, 논문 수용 여부 예측 기반 메트릭)에서 기준 모델들을 능가

## How

- **희소 주의 메커니즘**: Transformer의 전체 주의를 대화 구조의 부모-자식 관계를 따르는 희소 주의로 대체하여 구조 정보를 인코더에 도입
  
- **다중 작업 학습**: 메타리뷰 생성의 주 작업 외에 보조 작업으로 다음을 예측:
  - 소스 문서 유형(공식 리뷰, 저자 응답 등)
  - 리뷰 평점/신뢰도(1-5 또는 1-10)
  - 논문 수용 여부
  
- **입력 표현**: 문서를 평탄화(flattening)하되 토큰 시퀀스에 임베딩을 통해 계층적 위치 정보 통합

- **경량 설계**: 그래프 신경망(GNN)과 달리 학습 가능한 파라미터를 최소화

## Originality

- **새로운 도메인/태스크**: 피어리뷰 도메인에서 명시적 계층적 대화 구조와 상충 관계를 갖춘 최초의 대규모 MDS 데이터셋

- **현실적 복잡성**: 기존 MDS 데이터셋에 부족했던 상충하는 의견(conflicting opinions) 13.6%를 명시적으로 포함하고 표시

- **구조-인식 주의**: 기존 주의 조작 방법이 문장 내 구문 구조나 단일 문서 구조에 초점을 맞춘 반면, RAMMER는 문서 간 담론 구조(inter-document discourse structure) 포착

- **메타데이터 활용**: 리뷰 평점, 신뢰도, 수용 여부 등 풍부한 메타데이터를 다중 작업 학습을 통해 활용

## Limitation & Further Study

- **상충 처리의 한계**: RAMMER를 포함한 모든 기준 모델이 상충하는 정보가 있는 샘플에서 어려움을 겪음. 리뷰어 간 불일치를 명시적으로 인식하고 해결하는 방법론 필요

- **비공개 논의 제외**: 리뷰어-메타리뷰어 간 비공개 대화가 메타리뷰에 영향을 미칠 수 있으나 관찰 불가능 (저자들은 리뷰 수정을 통해 반영된다고 가정)

- **도메인 특화성**: 피어리뷰 도메인 전용으로, 다른 다중문서 요약 작업으로의 일반화 가능성 미검토

- **평가 메트릭**: ROUGE 외 새로운 평가 메트릭 제안(논문 수용 여부 예측)하나, 인간 평가의 규모와 세부사항 부족

- **후속 연구**:
  - 상충 인식 및 해결을 위한 명시적 메커니즘 개발
  - 다양한 도메인(정책 분석, 법률 검토 등)으로 확장
  - 희소 주의 구조의 최적화 및 다른 그래프 구조 탐색
  - 더 큰 규모의 인간 평가 수행

## Evaluation

- **Novelty**: 4.5/5 — 명시적 계층 구조와 상충 관계를 포함한 새로운 도메인의 MDS 데이터셋으로 독창적이나, 모델 아키텍처는 기존 희소 주의 아이디어의 자연스러운 확장

- **Technical Soundness**: 4/5 — 데이터셋 구성이 체계적이고 분석이 충실하나, 모델의 상충 처리 실패에 대한 깊이 있는 분석 부족

- **Significance**: 4.5/5 — 피어리뷰 자동화라는 실질적 응용가치가 있고, 다중문서 요약 연구에 새로운 도전 과제 제시. 다만 도메인 특수성으로 인한 영향력 제한

- **Clarity**: 4/5 — 전반적으로 명확하나, 계층 구조 인코딩 세부사항과 희소 주의 구체적 구현이 다소 모호함

- **Overall**: 4.2/5

**총평**: 복잡한 구조와 상충하는 정보를 다루는 현실적이고 도전적인 다중문서 요약 데이터셋을 제시한 점에서 학술적 기여도가 높으나, 제안된 모델이 핵심 문제(상충 해결)를 해결하지 못함을 보여주어 향후 연구의 방향을 명확히 제시한다.

## Related Papers

- 🔄 다른 접근: [[papers/561_Ms2_Multi-document_summarization_of_medical_studies/review]] — 둘 다 의료/학술 분야 다중문서 요약을 다루지만 하나는 동료평가, 다른 하나는 체계적 문헌 검토에 중점을 둠
- 🔄 다른 접근: [[papers/581_Oarelatedwork_A_large-scale_dataset_of_related_work_sections/review]] — 둘 다 학술 논문의 다중문서 요약을 다루지만 하나는 메타리뷰, 다른 하나는 관련 업무 생성에 중점을 둠
- 🔄 다른 접근: [[papers/561_Ms2_Multi-document_summarization_of_medical_studies/review]] — 둘 다 의료/학술 분야 다중문서 요약을 다루지만 하나는 체계적 문헌 검토, 다른 하나는 동료평가에 중점을 둠
- 🔄 다른 접근: [[papers/581_Oarelatedwork_A_large-scale_dataset_of_related_work_sections/review]] — 둘 다 학술 논문의 다중문서 요약을 다루지만 하나는 관련 업무, 다른 하나는 메타리뷰 생성에 중점을 둠
- 🔄 다른 접근: [[papers/022_A_sentiment_consolidation_framework_for_meta-review_generati/review]] — 둘 다 동료평가에서 감정 통합을 다루지만 서로 다른 프레임워크와 접근 방식을 사용함
