---
title: "564_Multi-llm_collaborative_caption_generation_in_scientific_doc"
authors:
  - "Jaeyoung Kim"
  - "Jongho Lee"
  - "Hong-Jun Choi"
  - "Ting-Yao Hsu"
  - "Chieh-Yang Huang"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "과학 논문의 도형(figure) 캡션 생성은 시각 정보와 텍스트 문맥을 모두 활용해야 하는 복합 작업인데, 본 논문은 여러 LLM의 협업을 통해 고품질 캡션을 자동 생성하는 통합 프레임워크 MLBCAP를 제안한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Table_Caption_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Kim et al._2025_Multi-llm collaborative caption generation in scientific documents.pdf"
---

# Multi-llm collaborative caption generation in scientific documents

> **저자**: Jaeyoung Kim, Jongho Lee, Hong-Jun Choi, Ting-Yao Hsu, Chieh-Yang Huang, Sungchul Kim, Ryan A. Rossi, Tong Yu, C. Lee Giles, Ting-Hao Huang, Sungchul Choi | **날짜**: 2025 | **DOI**: N/A

---

## Essence

과학 논문의 도형(figure) 캡션 생성은 시각 정보와 텍스트 문맥을 모두 활용해야 하는 복합 작업인데, 본 논문은 여러 LLM의 협업을 통해 고품질 캡션을 자동 생성하는 통합 프레임워크 MLBCAP를 제안한다.

## Motivation

- **Known**: 기존 도형 캡션 생성 방법은 이미지-텍스트 변환 또는 텍스트 요약 중 하나만 처리하고 있음. arXiv 데이터셋의 50% 이상이 저품질 캡션을 포함하고 있음.
- **Gap**: 시각적 세부사항(패턴, 색상, 동향)과 텍스트 맥락을 동시에 활용하는 통합 접근법의 부재. 저품질 훈련 데이터로 인한 모델 성능 저하.
- **Why**: 과학 커뮤니케이션에서 정확하고 유익한 캡션이 핵심적 역할을 수행하며, 이를 위해서는 멀티모달 정보의 통합이 필수적.
- **Approach**: 품질 평가(Quality Assessment), 다양한 캡션 생성(Diverse Caption Generation), 판단(Judgment)의 세 가지 모듈로 구성된 협업 프레임워크 제안.

## Achievement

![Figure 1: Overview of the collaborative framework integrating multiple LLMs for caption generation in scientific documents. Initially, two MLLMs generate figure descriptions. Next, three fine-tuned models and GPT-4o generate candidate captions. Finally, GPT-4o selects and refines the best caption from the candidates.](figures/fig1.webp)

1. **저품질 데이터 필터링**: 미세조정된 LLaVA 모델을 통해 훈련 데이터의 품질을 평가하여 고품질 캡션(점수 5-6)만 선별. Kendall's tau 계수 0.5502로 GPT-4o와의 일치도 확인.

2. **인간 평가 우수성**: 도메인 전문가(Ph.D. 학생)의 평가에서 MLBCAP가 저자가 작성한 원본 캡션보다 선호됨을 입증. 35,935개의 고품질 전처리된 훈련 데이터 구축.

3. **장단형 캡션 생성**: 학술지의 페이지 제약을 고려하여 장문(50단어) 및 단문(30단어) 버전의 캡션을 동시에 생성 가능.

## How

![Figure 2: Human evaluation results showing preferences for generated captions](figures/fig2.webp)

### 4.1 품질 평가 모듈
- GPT-4o를 사용하여 3,000개 샘플에 대해 1-6점 척도의 합성 품질 평가 데이터셋 생성
- LLaVA를 미세조정하여 전체 훈련 데이터셋에 대한 품질 예측 수행
- 점수 5-6인 고품질 샘플 집합(D_high) 추출

### 4.2 다양한 캡션 생성 모듈
- **GPT-4o**: Few-shot 프롬프팅(같은 주제의 점수 6 예제 10개)으로 고급 추론 활용
- **LLaMA-3-8B, Yi-1.5-9B**: D_high에서 시각-텍스트 특성으로 미세조정, MiniCPM-V로 도형 설명 생성
- **PEGASUS**: 도형-언급 문단과 OCR 텍스트에 대해 미세조정, 추상적 요약 특화

### 4.3 판단 및 정제 모듈
- GPT-4o가 4개 후보 캡션 중 최고 품질 캡션 선택
- 시각-텍스트 정보를 바탕으로 정확성 오류 수정
- [MAX_LEN] 변수로 장문(50단어), 단문(30단어) 버전 생성

## Originality

- **멀티모달 협업 프레임워크**: 폐쇄형(GPT-4o) 및 개방형(LLaMA, Yi, PEGASUS) LLM을 이미지-텍스트 생성, 텍스트 요약 등 서로 다른 역할로 조합하는 처음의 시도
- **데이터 품질 관리**: 저품질 캡션 문제를 체계적으로 해결하기 위해 멀티모달 평가 모델을 도입한 데이터 정제 파이프라인
- **멀티 길이 출력**: 학술 출판 환경의 현실적 제약(페이지 제한)을 고려한 가변 길이 캡션 생성
- **인간 평가 중심**: 자동 지표(BLEU, ROUGE) 대신 도메인 전문가 평가로 성능 검증

## Limitation & Further Study

- **제한사항**: 
  - 인간 평가 규모가 명시되지 않아 통계적 유의성 판단 어려움
  - GPT-4o에 대한 높은 의존도로 인한 상업적 비용 증가 및 개방형 모델 대체 어려움
  - 특정 도형 유형(graph plot 외의 복잡한 구조적 도형)에 대한 성능 차이 미분석
  - 다국어 또는 비영어 과학 문서로의 확장 가능성 검토 부재

- **후속 연구**:
  - 경량 오픈소스 모델로의 판단 모듈 대체 가능성 탐색
  - 도형 유형별, 학문 분야별 성능 분석 및 특화 모델 개발
  - 캡션 생성 과정의 설명 가능성(interpretability) 향상
  - 사용자 피드백을 통한 온라인 학습 메커니즘 도입

## Evaluation

- **Novelty**: 4/5 - 멀티모달 협업 프레임워크는 참신하나, 개별 기술(품질 평가, few-shot 프롬프팅)들은 기존 기법 활용
- **Technical Soundness**: 4/5 - 파이프라인 설계는 논리적이나, 미세조정 데이터셋 구성, 하이퍼파라미터 선택 등 상세 기술 설명 부족
- **Significance**: 4/5 - 과학 문헌 자동화의 실질적 기여는 크나, 평가 규모 및 범위가 제한적
- **Clarity**: 3.5/5 - 전체 구조는 명확하나, 4.1-4.3 섹션의 프롬프트 상세 내용이 부록으로 미루어져 본문 이해도 저하
- **Overall**: 4/5

**총평**: 과학 도형 캡션 생성의 현실적 과제(저품질 훈련 데이터, 멀티모달 정보 통합)를 체계적으로 해결하는 실용적 프레임워크이며, 인간 평가를 통한 우수성 입증이 강점이나, 경제성 있는 모델 경량화 및 평가의 통계적 엄밀성 강화가 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/399_Helm_Highlighted_evidence_augmented_language_model_for_enhan/review]] — 단일 LLM의 증거 강조를 다중 LLM 협업으로 발전시켜 더 고품질의 과학 도형 캡션을 생성합니다.
- 🏛 기반 연구: [[papers/708_SciCap_Generating_Captions_for_Scientific_Figures/review]] — 과학적 도형 캡션 생성의 기본 방법론이 다중 LLM 협업 캡션 생성의 이론적 기반을 제공합니다.
- 🔄 다른 접근: [[papers/336_FigCaps-HF_A_Figure-to-Caption_Generative_Framework_and_Benc/review]] — 과학 도형 캡션 생성에서 다중 LLM 협업과 단일 생성 프레임워크의 서로 다른 접근법을 비교할 수 있습니다.
- 🔗 후속 연구: [[papers/605_PatFig_Generating_Short_and_Long_Captions_for_Patent_Figures/review]] — 과학 문서에서 다중 LLM 협업 캡션 생성 기법이 특허 도형의 복잡한 기술적 내용을 더욱 정확하게 캡션화하는데 활용될 수 있다.
- 🔗 후속 연구: [[papers/524_MatViX_Multimodal_Information_Extraction_from_Visually_Rich/review]] — 다중 LLM 협업 캡션 생성이 MatViX의 멀티모달 정보 추출을 과학 문서의 시각적 요소 설명 생성으로 확장한 구체적 응용 연구임
- 🔗 후속 연구: [[papers/092_Align_then_Fusion_Generalized_Large-scale_Multi-view_Cluster/review]] — 다중 LLM 협업 캡션 생성에서 본 논문의 앵커 대응 관계 수립 방법론을 활용할 수 있다.
- 🔗 후속 연구: [[papers/329_Explaining_relationships_among_research_papers/review]] — 과학 문서에서 다중 LLM 협업 캡션 생성으로 본 논문의 여러 논문 처리를 다중 모델 협업으로 확장한다.
- 🔗 후속 연구: [[papers/399_Helm_Highlighted_evidence_augmented_language_model_for_enhan/review]] — 단일 LLM의 증거 강조 방식을 다중 LLM 협업으로 확장한 고도화된 접근법을 제시합니다.
