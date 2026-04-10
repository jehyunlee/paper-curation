---
title: "404_Hiperrag_High-performance_retrieval_augmented_generation_for"
authors:
  - "Ozan Gökdemir"
  - "Carlo Siebenschuh"
  - "Alexander Brace"
  - "Azton I. Wells"
  - "Brian Hsu"
date: "2025"
doi: "10.1145/3732775.3733586"
arxiv: ""
score: 4.0
essence: "본 논문은 360만 개 이상의 과학 논문을 처리하기 위해 고성능 컴퓨팅(HPC)을 활용한 검색-증강 생성(RAG) 시스템 HiPerRAG를 제시하며, 과학 문헌의 복잡한 구조를 처리하는 새로운 문서 파싱 기법(Oreo)과 과학 텍스트 특화 인코더(ColTrast)를 개발했다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Retrieval-augmented_Generation_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Gökdemir et al._2025_Hiperrag High-performance retrieval augmented generation for scientific insights.pdf"
---

# HiPerRAG: High-performance retrieval augmented generation for scientific insights

> **저자**: Ozan Gökdemir, Carlo Siebenschuh, Alexander Brace, Azton I. Wells, Brian Hsu, Kyle Hippe, Priyanka V. Setty, Aswathy Ajith, J. Gregory Pauloski, Varuni Sastry, Sam Foreman, Huihuo Zheng, Heng Ma, Bharat Kale, Nicholas Chia, Tom Gibbs, Michael E. Papka, Thomas Brettin, Francis J. Alexander, Anima Anandkumar | **날짜**: 2025 | **DOI**: [10.1145/3732775.3733586](https://doi.org/10.1145/3732775.3733586)

---

## Essence

![Figure 1](figures/fig1.webp)
*HiPerRAG 워크플로우: 멀티모달 문서 파싱(Oreo), 질의-인식형 인코더 미세조정(ColTrast), 그리고 대규모 벡터 검색을 통합한 과학 문헌 RAG 시스템*

본 논문은 360만 개 이상의 과학 논문을 처리하기 위해 고성능 컴퓨팅(HPC)을 활용한 검색-증강 생성(RAG) 시스템 HiPerRAG를 제시하며, 과학 문헌의 복잡한 구조를 처리하는 새로운 문서 파싱 기법(Oreo)과 과학 텍스트 특화 인코더(ColTrast)를 개발했다.

## Motivation

- **Known**: 과학 출판물의 양이 1년에 150만 개 이상 증가하고 있으며, 대규모 언어모델(LLM)은 지식-집약적 작업에 유용하나 환각(hallucination) 문제가 있음. RAG는 검색을 통해 LLM의 사실성을 개선할 수 있는 유망한 방법.

- **Gap**: RAG를 백만 규모의 과학 논문에 확장하려면 세 가지 주요 도전과제가 있음:
  1) 과학 논문의 다양한 레이아웃(표, 그림, 수식)에서 의미 있는 텍스트 파싱의 어려움
  2) 과학 콘텐츠 특화 인코더 개발의 필요성 (일반 목적 인코더는 과학 텍스트에서 부진)
  3) 과학 문헌 평가 벤치마크의 부재

- **Why**: 현존 문서 파싱 기법(PyPDF, Nougat 등)은 처리량(throughput)과 정확도 간의 트레이드오프가 있으며, 과학 특화 검색 성능을 평가할 공개 데이터셋이 부족함.

- **Approach**: (1) 레이아웃 감지 + 선택적 OCR 기반 두 단계 파싱(Oreo), (2) 대조학습과 후기-상호작용(late-interaction) 기법을 결합한 과학 특화 인코더(ColTrast), (3) 단백질 상호작용/기능 예측 Q&A 벤치마크 개발, (4) HPC 시스템(Polaris, Sunspot, Frontier)에서의 분산 처리.

## Achievement

![Figure 2](figures/fig2.webp)
*Oreo 파싱 워크플로우: YOLO 기반 레이아웃 감지 → 영역별 선택적 처리(추출 또는 OCR)*

1. **문서 파싱 성과**: Oreo가 최신 파서(Nougat, Marker)와 비교하여 유사한 정확도를 유지하면서 **약 10배 높은 처리량** 달성. 대규모 과학 논문 코퍼스 처리에 가장 적합한 솔루션 제공.

2. **검색 성능**: ColTrast 인코더로 미세조정한 결과, **SciQ에서 90% 정확도, PubMedQA에서 76% 정확도** 달성. PubMedGPT 등 도메인 특화 모델과 GPT-4 같은 상용 LLM을 모두 능가.

3. **평가 벤치마크**: 단백질 상호작용(7,591 Q&A)과 단백질 기능(17,646 Q&A) 예측용 새로운 생물의학 벤치마크 개발. 검색 정확도 평가용 합성 데이터셋(BioSynthQPs, 1,500개 도메인 특화 구절) 구성.

4. **확장성**: 3개의 슈퍼컴퓨터에서 수천 개의 GPU로 확장 가능한 분산 워크플로우(Parsl 프레임워크 활용) 구현. 백만 규모 문서의 실시간 처리 가능.

## How

![Figure 3](figures/fig3.webp)
*ColTrast 인코더 워크플로우: 질의 샘플링 → 대조학습 → 후기-상호작용 기법 적용*

### 문서 파싱 (Oreo)

- **2단계 하이브리드 접근**: (1) YOLO CNN을 이용한 고속 레이아웃 감지로 PDF를 텍스트/표/이미지/수식 영역으로 분할, (2) 영역 유형에 따라 추출 기반(born-digital) 또는 OCR 기반(스캔 PDF) 파싱 적용
- 다양한 실패 케이스 처리로 견고성 증대
- 표와 수식 처리를 위한 특화된 후처리 모듈

### 인코더 미세조정 (ColTrast)

- **대조학습(Contrastive Learning)**: 질의-구절 쌍의 의미적 거리를 최소화하도록 인코더 훈련
- **후기-상호작용(Late-Interaction)**: 개별 토큰 수준의 유사도를 계산한 후 집계하여 더 세밀한 의미 포착
- 과학 문헌의 도메인 특화 어휘와 개념 관계를 학습하도록 최적화
- 기존 범용 인코더보다 과학 콘텐츠에서 월등한 성능

### 시스템 확장

- **Parsl 기반 분산 처리**: 문서 파싱, 의미 청킹, 인코딩, 색인화, 검색 각 단계를 HPC 노드에 분산
- 강한 확장성(strong scaling) 달성으로 처리 시간 단축
- 벡터 데이터베이스와 통합하여 실시간 쿼리 응답 가능

## Originality

- **Oreo의 혁신성**: 레이아웃 감지와 영역별 선택적 처리를 결합한 하이브리드 방식으로, 기존 end-to-end 신경망 기반 파서(Nougat)의 계산량을 획기적으로 감소시키면서 정확도 유지. 과학 논문의 멀티모달 콘텐츠(표, 수식, 그림) 처리에 최적화.

- **ColTrast의 차별성**: 대조학습과 후기-상호작용 기법을 명시적으로 결합한 인코더 미세조정은 기존 범용 인코더의 과학 텍스트 이해 능력 한계를 극복. 질의 인식형 미세조정으로 특정 도메인 특화.

- **벤치마크 기여**: ProteinInteractionQA, ProteinFunctionQA 등 실제 생물의학 예측 작업 기반의 새로운 Q&A 벤치마크는 이전의 추상적 데이터셋과 달리 검증 가능한 과학적 사실 기반.

- **HPC-AI 통합**: RAG 시스템의 각 컴포넌트를 HPC 워크플로우에 통합한 최초의 대규모 사례. 과학 커뮤니티의 실질적 수요(360만 개 논문 처리)를 충족시키는 실용적 접근.

## Limitation & Further Study

- **문서 파싱의 한계**: Oreo는 여전히 복잡한 다열(multi-column) 레이아웃, 악화된 이미지 품질의 스캔 PDF에서 성능 저하 가능. 수식 인식의 정확도도 개선 여지 있음.

- **인코더의 일반화**: ColTrast는 생물의학 문헌 중심으로 미세조정되어 다른 과학 분야(물리학, 화학 등)로의 전이 성능 평가 부족. 도메인 간 성능 격차 분석 필요.

- **평가의 제한**: SciQ와 PubMedQA 벤치마크는 객관식이거나 특정 질문 유형에 한정. 개방형 질문, 다중 선택지 비교, 종합적 문헌 분석 요구 질문 평가 미흡.

- **RAG의 근본적 문제**: 검색된 구절이 항상 정확한 답변을 포함하지 않을 가능성. 검색 실패 시 LLM 환각의 위험 여전함. 검색 품질과 생성 품질의 상관관계에 대한 분석 심화 필요.

- **후속 연구 방향**:
  - 다국어 과학 논문 처리 확장
  - 동적 벡터 데이터베이스 업데이트 메커니즘 개발
  - 검색-생성 파이프라인의 엔드-투-엔드 최적화
  - 다중 모달(표, 그림) 콘텐츠의 의미 통합 강화
  - 과학자 커뮤니티와의 협력으로 실제 사용 패턴 피드백 반영

## Evaluation

- **Novelty**: 4/5
  - Oreo의 하이브리드 파싱과 ColTrast의 대조학습 조합은 창의적이나, 개별 기법들(YOLO, contrastive learning, late-interaction)은 기존 방법론의 응용. 새로운 벤치마크는 기여하지만 평가 방법론의 근본적 혁신은 제한적.

- **Technical Soundness**: 4.5/5
  - 시스템 설계와 구현이 견고하며, 실험은 체계적. HPC 확장 실험이 설득력 있음. 다만 ColTrast 미세조정의 이론적 근거 설명 부족. 파싱 정확도 평가의 세부 지표(precision, recall, F1) 명시 필요.

- **Significance**: 4/5
  - 과학 커뮤니티의 실질적 수요(360만 논문 처리) 해결. 현재 RAG 시스템 중 규모와 성능 모두 최고 수준. 그러나 기본적 LLM 환각 문제의 근본 해결은 아니며, 특정 도메인(생물의학) 중심으로 평가된 한계.

- **Clarity**: 4/5
  - 전반적으로 명확한 설명과 시각화. 워크플로우 다이어그램이 유용. 다만 ColTrast의 구체적 알고리즘 수식, 대조 쌍 구성 방식, 하이퍼파라미터 설정에 대한 상세 기술 필요.

- **Overall**: 4/5
  - **총평**: 본 논문은 대규모 과학 문헌 처리를 위한 RAG 시스템의 실용적이고 확장 가능한 솔루션을 제시한다. Oreo 파서와 ColTrast 인코더는 개별적으로 의미 있는 기여를 하며, HPC와의 통합은 산업 적용 가능성을 높인다. 다만 새로운 벤치마크 대부분이 단일 도메인(단백질 예측)에 한정되고, 검색-생성 통합 최적화, LLM 환각 저감의 근본적 해결책 제시는 미흡하다. 과학 커뮤니티의 정보 과부하 문제 해결에 기여할 실용적 시스템이지만, 학술적 혁신성 측면에서는 기존 기법의 공학적 우수 조합에 가깝다.

## Related Papers

- 🏛 기반 연구: [[papers/675_Retrieval-Augmented_Generation_for_Knowledge-Intensive_NLP_T/review]] — 대형 언어 모델을 위한 검색 증강 생성 서베이가 과학 문헌 특화 RAG 시스템 설계의 이론적 기반입니다.
- 🔄 다른 접근: [[papers/659_REALM_Retrieval-Augmented_Language_Model_Pre-Training/review]] — 과학 문헌 처리에서 멀티모달 사전훈련과 고성능 컴퓨팅 기반 접근법을 비교할 수 있습니다.
- 🔗 후속 연구: [[papers/593_Openscholar_Synthesizing_scientific_literature_with_retrieva/review]] — 과학 문헌 합성을 위한 검색 증강 방법이 HiPerRAG의 대규모 처리 능력과 결합될 수 있습니다.
- 🔗 후속 연구: [[papers/393_Graphusion_a_rag_framework_for_knowledge_graph_construction/review]] — 고성능 RAG 시스템의 과학 문헌 처리 기법이 지식그래프 기반 검색 증강에 확장 적용될 수 있습니다.
- 🔗 후속 연구: [[papers/659_REALM_Retrieval-Augmented_Language_Model_Pre-Training/review]] — REALM의 검색 증강 개념을 고성능으로 최적화한 HiPerRAG로 발전
