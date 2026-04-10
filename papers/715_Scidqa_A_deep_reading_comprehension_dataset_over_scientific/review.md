---
title: "715_Scidqa_A_deep_reading_comprehension_dataset_over_scientific"
authors:
  - "Shruti Singh"
  - "Nandan Sarkar"
  - "Arman Cohan"
date: "2024"
doi: "10.18653/v1/2024.emnlp-main.1163"
arxiv: ""
score: 4.25
essence: "본 논문은 과학 논문의 깊이 있는 이해를 요구하는 새로운 질의응답(QA) 데이터셋 SCIDQA를 소개한다. OpenReview 플랫폼의 피어 리뷰에서 수집한 2,937개의 QA 쌍으로 구성되어 있으며, 표, 그림, 다중 문서 추론을 포함한 복잡한 과학 텍스트 이해를 평가한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Scholarly_Document_QA"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Singh et al._2024_Scidqa A deep reading comprehension dataset over scientific papers.pdf"
---

# Scidqa: A deep reading comprehension dataset over scientific papers

> **저자**: Shruti Singh, Nandan Sarkar, Arman Cohan | **날짜**: 2024 | **DOI**: [10.18653/v1/2024.emnlp-main.1163](https://doi.org/10.18653/v1/2024.emnlp-main.1163)

---

## Essence

![Figure 1](figure1.png)
*과학 논문에 대한 피어 리뷰 중 검토자-저자 토론에서 추출된 질의응답 쌍의 예시*

본 논문은 과학 논문의 깊이 있는 이해를 요구하는 새로운 질의응답(QA) 데이터셋 SCIDQA를 소개한다. OpenReview 플랫폼의 피어 리뷰에서 수집한 2,937개의 QA 쌍으로 구성되어 있으며, 표, 그림, 다중 문서 추론을 포함한 복잡한 과학 텍스트 이해를 평가한다.

## Motivation

- **Known**: 기존 과학 QA 데이터셋(QASPER, COVID-QA 등)은 제목과 초록 중심의 표면 수준 정보 추출에 제한되어 있으며, 깊이 있는 논문 이해를 충분히 평가하지 못함.

- **Gap**: 전체 논문 텍스트에 대한 종합적 이해, 배경 지식, 비판적 사고가 필요한 깊이 있는 질문-답변 데이터셋의 부재.

- **Why**: 과학 문헌은 본질적으로 밀도 높고 복잡하며, 실제 학술 활동에서 연구자들이 필요로 하는 깊이 있는 이해 능력을 평가할 필요가 있음.

- **Approach**: 피어 리뷰에서 검토자의 정보 요청과 저자의 응답을 자동 추출한 후, 도메인 전문가에 의한 수작업 필터링, 재작성, 질품 관리를 통해 고품질 데이터셋 구축.

## Achievement

![Figure 2](figure2.png)
*SCIDQA 데이터셋 구축 파이프라인: 피어 리뷰에서의 LLM 기반 QA 추출 및 인간 전문가 주석 처리*

1. **자연스러운 고품질 데이터셋**: 26,085개 초기 추출 QA 쌍 중 약 41% (2,937개)를 관련성 있는 질문으로 선별하여, 기존 자동 생성 데이터셋 대비 높은 품질 확보.

2. **다양한 추론 양식**: 표(14.03%), 다중 문서(10.9%), 부록/보충 자료(10.01%), 수식/기호(10.32%), 그림(6.98%) 등 다양한 모달리티를 아우르는 복잡한 질문 포함.

3. **장문의 질의응답**: 평균 질문 길이 23.92 단어, 답변 길이 104.67 단어로 기존 데이터셋 대비 더 긴 형식, 심층적 추론 요구.

4. **포괄적 모델 평가**: 여러 오픈소스 및 상용 LLM을 다양한 설정(폐쇄형, 검색 기반, 장문맥)에서 벤치마킹하여 현재 모델들의 과학 논문 이해 능력의 한계 도출.

## How

![Figure 3](figure3.png)
*PaLM 모델을 사용한 질의응답 추출을 위한 프롬프트*

- **데이터 수집**: ICLR(2018-2022), NeurIPS(2021-2022) 등 A* 등급 국제학술대회의 11,400개 논문에서 18,658개 검토자-저자 토론 추출.

- **PDF 처리**: Nougat(시각 트랜스포머 기반 과학 OCR) 모델을 사용하여 PDF에서 텍스트 추출.

- **자동 QA 추출**: 정규표현식 필터링으로 중첩 토론 구조 파싱 후, PaLM API를 활용한 LLM 기반 질의응답 자동 추출.

- **전문가 주석**: 두 명의 NLP/ML 도메인 전문가가 85% 동의율로 관련성 판단, 불명확한 경우 '모호함' 카테고리로 분류.

- **컨텍스트 정규화**: 원래 일인칭 "저자-검토자" 형식을 삼인칭 객관식으로 재작성하여 LLM 편향 방지.

![Figure 4](figure4.png)
*삼인칭 서술로의 재작성이 필요한 질의응답 쌍의 사례*

- **출처 문서 추적**: 초기 제출본과 최종 카메라 완성본 간 변동 추적, 각 QA 쌍의 원본 문서 버전 명기.

![Figure 5](figure5.png)
*참고문헌 표준화: 특정 참고문헌 마크를 플레이스홀더로 대체하여 단순 참고문헌 추출 방지*

- **참고문헌 편집**: 모든 참고문헌을 일관된 형식(r1, r2 또는 1, 2 등)으로 재번호화하여 모델의 참고문헌 마크 기반 답변 추출 회피.

## Originality

- **새로운 데이터 원천**: 기존 데이터셋과 달리 피어 리뷰의 검토자 질문과 저자 답변을 직접 활용함으로써 자연스럽고 도메인 전문가 검증이 이루어진 고품질 데이터 확보.

- **다중 모달 추론 요구**: 텍스트뿐 아니라 표, 그림, 수식, 부록, 다중 문서 추론을 체계적으로 포함하여 진정한 깊이 있는 이해 평가.

- **엄밀한 품질 관리**: 자동 추출 후 수동 필터링, 컨텍스트 정규화, 출처 문서 추적, 참고문헌 표준화 등 다층적 정제 프로세스로 데이터셋 신뢰성 강화.

- **장문 답변 형식**: 기존의 짧은 답변(1-2단어) 대신 평균 104.67단어의 상세한 설명형 답변으로 추론 능력 심층 평가.

## Limitation & Further Study

- **제한된 도메인**: 기계학습(ML) 분야에만 한정되어 있으며, 생물학, 물리학 등 다른 과학 분야로의 확장 필요.

- **데이터셋 규모**: 2,937개 QA 쌍으로 대규모 데이터셋(PubMedQA의 211,269개)에 비해 상대적으로 작은 규모.

- **주석자 제한**: 두 명의 저자 주석자로 제한되었으며, 보다 많은 전문가 주석자의 참여로 재현성 강화 필요.

- **증거 주석의 부분적 제공**: 높은 주석 비용으로 인해 데이터셋 전체의 일부에만 증거 문서 지정, 전체 데이터셋에 대한 증거 추적 수행 미완료.

- **모델 성능의 저하**: 장문맥 처리 시 모델 성능 저하가 나타나며, 이를 해결하기 위한 개선 방안 모색 필요.

## Evaluation

- **Novelty**: 4.5/5
  피어 리뷰 기반의 새로운 데이터 원천과 다중 모달 추론 요구는 독창적이나, 규모 면에서는 다소 제한적.

- **Technical Soundness**: 4.5/5
  PDF 처리, 자동 추출, 수동 정제, 컨텍스트 정규화 등 전반적으로 탄탄한 방법론이나, 주석자 간 합의도(85%)가 높지 않으며 주석자 수 제한.

- **Significance**: 4/5
  깊이 있는 과학 논문 이해 평가의 중요성과 현 모델의 한계 드러내기는 의미 있으나, ML 분야 한정과 데이터 규모 제약이 영향력을 제한.

- **Clarity**: 4/5
  전체적으로 명확하고 구조화된 설명이나, 일부 주석 가이드라인(예: '모호함' 카테고리)의 정의가 다소 모호할 수 있음.

- **Overall**: 4.25/5

**총평**: SCIDQA는 피어 리뷰라는 자연스러운 데이터 원천과 엄밀한 품질 관리를 통해 과학 논문의 깊이 있는 이해를 평가하는 의미 있는 데이터셋을 제공하나, 도메인 제한성과 규모의 소재 측면에서 개선 여지가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/802_The_mighty_torr_A_benchmark_for_table_reasoning_and_robustne/review]] — SciDQA가 과학 논문의 깊이 있는 이해에 초점을 맞춘 반면, ToRR는 표 형식 견고성 평가에 특화되어 서로 다른 각도에서 LLM의 과학 텍스트 처리 능력을 평가함
- 🔗 후속 연구: [[papers/645_Pubmedqa_A_dataset_for_biomedical_research_question_answerin/review]] — PubMedQA의 생의학 질의응답을 전체 과학 논문으로 확장하여 표, 그림, 다중 문서 추론을 포함한 더 복잡한 과학 텍스트 이해 평가로 발전시킨 연구임
- 🏛 기반 연구: [[papers/602_Paperqa_Retrieval-augmented_generative_agent_for_scientific/review]] — PaperQA의 과학 연구용 검색 증강 생성 에이전트가 SciDQA의 복잡한 과학 논문 이해 과제를 실제로 해결할 수 있는 기술적 기반을 제공함
- 🔄 다른 접근: [[papers/802_The_mighty_torr_A_benchmark_for_table_reasoning_and_robustne/review]] — ToRR이 표 추론 견고성에 초점을 맞춘 반면, SciDQA는 과학 논문의 깊이 있는 이해를 평가하여 서로 다른 각도에서 LLM 평가를 다룸
- 🧪 응용 사례: [[papers/602_Paperqa_Retrieval-augmented_generative_agent_for_scientific/review]] — SciDQA의 깊이 있는 과학 논문 이해 평가가 PaperQA 시스템의 복잡한 과학 텍스트 처리 능력을 검증할 수 있는 구체적 벤치마크를 제공함
- 🔄 다른 접근: [[papers/645_Pubmedqa_A_dataset_for_biomedical_research_question_answerin/review]] — PubMedQA가 생의학 초록 기반 yes/no 답변에 특화된 반면, SciDQA는 전체 과학 논문의 깊이 있는 이해를 요구하여 서로 다른 복잡도의 과학 QA를 다룸
- 🏛 기반 연구: [[papers/488_Leveraging_LLMs_in_Scholarly_Knowledge_Graph_Question_Answer/review]] — 과학 문서에 대한 깊이 있는 읽기 이해의 기초를 제공한다
