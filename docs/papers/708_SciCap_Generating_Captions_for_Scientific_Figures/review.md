---
title: "708_SciCap_Generating_Captions_for_Scientific_Figures"
authors:
  - "Ting-Yao Hsu"
  - "C Lee Giles"
  - "Ting-Hao Huang"
date: "2021"
doi: "10.18653/v1/2021.findings-emnlp.277"
arxiv: ""
score: 4.0
essence: "과학 논문의 그래프, 차트 등 과학적 도형(scientific figures)에 대한 자동 캡션 생성을 위해 arXiv 논문 29만여 편에서 추출한 200만 개 이상의 실제 도형-캡션 쌍으로 구성된 대규모 데이터셋 SciCap을 구축하고, 기준 모델들을 통해 과학 도형 캡션 생성의 가능성과 과제를 제시한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Scientific_Figure_Captioning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Hsu et al._2021_SciCap Generating Captions for Scientific Figures.pdf"
---

# SciCap: Generating Captions for Scientific Figures

> **저자**: Ting-Yao Hsu, C Lee Giles, Ting-Hao Huang | **날짜**: 2021 | **DOI**: [10.18653/v1/2021.findings-emnlp.277](https://doi.org/10.18653/v1/2021.findings-emnlp.277)

---

## Essence

과학 논문의 그래프, 차트 등 과학적 도형(scientific figures)에 대한 자동 캡션 생성을 위해 arXiv 논문 29만여 편에서 추출한 200만 개 이상의 실제 도형-캡션 쌍으로 구성된 대규모 데이터셋 SciCap을 구축하고, 기준 모델들을 통해 과학 도형 캡션 생성의 가능성과 과제를 제시한다.

## Motivation

- **Known**: 기존 연구는 합성된(synthetic) 도형과 일반적인 캡션으로 과학 도형 캡션 생성을 시도해왔으며(FigCAP, FigureQA 등), 합성 캡션은 "6개의 카테고리가 있다" 같은 제네릭한 설명에 그침

- **Gap**: 실제 과학 논문의 인간이 작성한 고품질 캡션은 의미 있는 부분을 강조하고 맥락을 제공하지만, 실제 과학 도형을 대상으로 한 대규모 데이터셋과 벤치마크가 부족함

- **Why**: (1) 연구자들이 더 나은 도형 캡션 작성을 돕기 위함, (2) 시각장애인을 위해 과학 도형의 접근성을 높이기 위함

- **Approach**: arXiv의 컴퓨터과학 논문(2010-2020)에서 PDFFigures 2.0으로 도형-캡션을 추출하고, 도형 분류, 소도형 제거, 텍스트 정규화 등의 전처리를 통해 대규모 데이터셋을 구축한 후, CNN+LSTM 기반 기준 모델로 그래프 도형 캡션 생성 평가

## Achievement

1. **SciCap 데이터셋 구축**: 29만 5,028개 논문에서 추출한 133,543개의 단일 그래프 도형(graph plots) 데이터셋 구성 (기본 분석을 위해 2,000개 수동 라벨링)

2. **데이터셋 다양성 제공**: 3가지 수집 전략 제공
   - First Sentence: 모든 도형의 첫 문장 (133,543개)
   - Single-Sentence Caption: 단문 캡션만 (94,110개)
   - ≤100 Words: 100 토큰 이하 캡션 (131,319개)

3. **기준 모델 평가**: Vision-only, Vision+Text, Text-only 변형 모델로 도형 캡션 생성의 실현 가능성과 과제 제시

## How

- **데이터 수집**: CC-0 라이선스의 arXiv 데이터셋 활용 (195만 개 논문 중 cs./stat.ML 분야 2010-2020년 논문 29만 5,028개 선정)

- **도형 추출**: PDFFigures 2.0 활용으로 도형 이미지, 캡션, 범례, 축 레이블, 제목 등 추출

- **도형 분류**: 기존 Figure-Seer 분류기(86% 정확도) 사용하여 7개 유형 분류 → 그래프 도형(19.2%)에 집중

- **소도형 제거**: 수동 규칙(부분 문자 감지) + FigureSeparator CNN 모델(85.9% 정확도) 조합으로 소도형 포함 도형 제거 (35.72% → 32.04%로 감소)

- **텍스트 정규화**: NLTK 토큰화, 소문자 변환, 도형 번호 제거, 숫자를 [NUM]으로, 수식을 [EQUATION]으로, 괄호 내용을 [BRACKET]으로 치환

- **모델 구조**: ResNet-101 인코더(2048차원) + Luong attention이 적용된 512차원 LSTM 디코더

## Originality

- **첫 실제 대규모 과학 도형 데이터셋**: 합성 데이터 대신 실제 arXiv 논문의 인간이 작성한 고품질 캡션 기반

- **체계적 전처리 파이프라인**: 도형 분류, 소도형 제거, 텍스트 정규화 등 다단계 품질 관리 절차를 실증적으로 개발

- **다양한 캡션 컬렉션**: 연구자 요구에 맞춘 3가지 데이터 수집 전략 제공

- **접근성 동기**: 시각장애인을 위한 과학 콘텐츠 접근성 개선이라는 사회적 가치 강조

## Limitation & Further Study

- **범위 제한**: 컴퓨터과학 분야만 포함 (다른 분야의 도형 특성 미반영)

- **도형 유형 한정**: 그래프 도형만 중점 (테이블, 방정식, 순서도 등 다른 유형은 제외)

- **기준 모델의 한계**: CNN+LSTM은 classical한 구조로, 최신 vision transformer 등 고급 아키텍처 미적용

- **평가 지표 제한**: BLEU-4만 사용으로 의미론적 품질이 충분히 반영되지 않을 가능성

- **후속 연구 방향**:
  - 다른 학문 분야(생물학, 물리학 등)로 확대
  - 테이블, 방정식, 순서도 등 다른 도형 유형에 대한 캡션 생성
  - Vision transformer, CLIP 등 최신 멀티모달 모델 적용
  - 인간 평가 기반의 캡션 품질 평가 메트릭 개발
  - 문맥 정보(논문 텍스트, 관련 섹션 등)를 활용한 멀티모달 접근


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 과학 도형 캡션 생성 분야에서 첫 대규모 실제 데이터셋을 제공하고 체계적인 전처리 파이프라인을 구축했다는 점에서 의의가 있으며, 시각장애인 접근성이라는 사회적 가치도 강조했으나, 한정된 도형 유형과 기본적인 모델 구조, BLEU 지표만의 평가 등에서 개선 여지가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/336_FigCaps-HF_A_Figure-to-Caption_Generative_Framework_and_Benc/review]] — 둘 다 과학 도형 캡션 생성을 다루지만 하나는 arXiv 데이터셋 구축에, 다른 하나는 벤치마크 프레임워크 개발에 초점을 맞춘다.
- 🔗 후속 연구: [[papers/783_Synchart_Synthesizing_charts_from_language_models/review]] — LLM을 활용한 합성 차트 데이터셋이 SciCap의 실제 과학 도형 캡션 생성 연구를 보완하고 확장한다.
- 🏛 기반 연구: [[papers/551_MMC_Advancing_Multimodal_Chart_Understanding_with_Large-scal/review]] — 대규모 멀티모달 차트 이해 데이터셋이 과학 도형 캡션 생성의 기술적 기반을 제공한다.
- 🔄 다른 접근: [[papers/727_Scimage_How_good_are_multimodal_large_language_models_at_sci/review]] — 과학적 그림에 대한 캡션 생성과 달리 텍스트에서 과학적 이미지를 생성하는 역방향 능력을 평가한다.
- 🔗 후속 연구: [[papers/323_Every_part_matters_Integrity_verification_of_scientific_figu/review]] — 과학 그림 검증이 더 포괄적인 과학 캡션 생성으로 확장됩니다.
- 🔗 후속 연구: [[papers/853_Understanding_how_paper_writers_use_ai-generated_captions_in/review]] — 과학 도표 캡션 자동 생성 기술이 실제 논문 작성자들에게 어떻게 활용되는지 보여주는 후속 연구이다.
- 🔗 후속 연구: [[papers/691_S1-MMAlign_A_Large-Scale_Multi-Disciplinary_Dataset_for_Scie/review]] — 과학적 그림 캡션 생성을 대규모 이미지-텍스트 정렬로 확장한 연구다
- 🔗 후속 연구: [[papers/336_FigCaps-HF_A_Figure-to-Caption_Generative_Framework_and_Benc/review]] — 기본적인 과학 캡션 생성을 인간 피드백 기반 최적화로 발전시킨 확장
- 🏛 기반 연구: [[papers/524_MatViX_Multimodal_Information_Extraction_from_Visually_Rich/review]] — 과학 그림을 위한 캡션 생성 기술이 재료과학 논문의 복잡한 시각적 정보를 구조화된 텍스트로 변환하는 MatViX 시스템의 핵심 구성 요소를 제공함
- 🏛 기반 연구: [[papers/399_Helm_Highlighted_evidence_augmented_language_model_for_enhan/review]] — 과학적 도형 캡션 생성의 기본 방법론을 표 캡션 생성에 적용한 기초 연구입니다.
- 🔗 후속 연구: [[papers/515_Machine-in-the-loop_rewriting_for_creative_image_captioning/review]] — 과학적 도형 캡션 생성을 창의적이고 비유적인 표현으로 확장하여 더 풍부한 서술이 가능한 방법을 제시합니다.
- 🏛 기반 연구: [[papers/564_Multi-llm_collaborative_caption_generation_in_scientific_doc/review]] — 과학적 도형 캡션 생성의 기본 방법론이 다중 LLM 협업 캡션 생성의 이론적 기반을 제공합니다.
