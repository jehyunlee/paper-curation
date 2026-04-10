---
title: "605_PatFig_Generating_Short_and_Long_Captions_for_Patent_Figures"
authors:
  - "Dana Aubakirova"
  - "Kim Gerdes"
  - "Lufei Liu"
date: "2023.10"
doi: "10.1109/ICCVW60793.2023.00305"
arxiv: ""
score: 3.5
essence: "본 논문은 유럽 특허청(EPO)의 11,000개 이상 특허에서 추출한 30,000개 이상의 특허 도형으로 구성된 대규모 데이터셋 **Qatent PatFig**를 소개하며, 대규모 비전-언어 모델(LVLM)을 미세조정하여 특허 도형에 대한 짧고 긴 캡션을 자동 생성하는 방법을 제시한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Scientific_Figure_Captioning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Aubakirova et al._2023_PatFig Generating Short and Long Captions for Patent Figures.pdf"
---

# PatFig: Generating Short and Long Captions for Patent Figures

> **저자**: Dana Aubakirova, Kim Gerdes, Lufei Liu | **날짜**: 2023-10-2 | **DOI**: [10.1109/ICCVW60793.2023.00305](https://doi.org/10.1109/ICCVW60793.2023.00305)

---

## Essence

![Figure 1](figures/fig1.webp)

본 논문은 유럽 특허청(EPO)의 11,000개 이상 특허에서 추출한 30,000개 이상의 특허 도형으로 구성된 대규모 데이터셋 **Qatent PatFig**를 소개하며, 대규모 비전-언어 모델(LVLM)을 미세조정하여 특허 도형에 대한 짧고 긴 캡션을 자동 생성하는 방법을 제시한다.

## Motivation

- **Known**: 특허 도형은 복잡한 기술 정보를 효율적으로 전달하는 중요한 매체이며, 과학 도형 캡셔닝 연구가 존재한다(FigCAP, SciCap 등).

- **Gap**: 특허 도형 캡셔닝은 여전히 미개척 영역이며, 기존 특허 도형 데이터셋(CLEF-IP, DeepPatent)은 상세한 설명이나 참조 기호(reference numerals)와 용어(terms) 정보가 부족하다.

- **Why**: 특허 도형은 참조 기호, 용어 목록, 짧고 긴 설명, 특허 청구항 간의 복잡한 관계를 포함하고 있어 특화된 데이터셋과 방법론이 필요하다.

- **Approach**: 대규모 비전-언어 모델(MiniGPT-4)을 PatFig 데이터셋으로 미세조정하고, 특허 제목, 참조 기호, 용어 등 다양한 텍스트 단서를 예측 단계에서 활용하여 캡션 생성 성능을 개선한다.

## Achievement

1. **PatFig 데이터셋 구축**: 30,714개의 특허 도형으로 구성된 대규모 데이터셋 개발(최종 개정본: 17,877개 훈련, 2,417개 테스트)
   - 짧은 캡션(Short captions)과 긴 캡션(Long captions) 포함
   - 참조 기호(reference numerals), 용어(terms), 도형 유형, 최소 청구항 정보 제공

2. **LVLM 기반 캡션 생성**: MiniGPT-4를 활용한 효과적인 특허 도형 캡션 생성 시스템 개발
   - 짧은 캡션: 최고 BLEU2 0.5573, CIDEr 0.7939
   - 긴 캡션: 최고 BLEU2 0.3478, CIDEr 0.0587

3. **텍스트 단서의 영향 분석**: 제목과 용어 추가가 캡션 품질 향상에 미치는 영향 실증

## How

![Table 3](figures/fig1.webp)

### 데이터셋 구축 방법

- **데이터 수집**: 유럽 특허청(EPO)의 2020년 1월~12월 발행 특허 중 62,513개 이미지 스크래핑
  
- **짧은 캡션 추출**: 규칙 기반 방법을 통해 "Brief Description of Drawings" 섹션에서 표준화된 형식의 설명 자동 추출(10-40 토큰 범위)

- **긴 캡션 추출**: 텍스트 정규화, 도형 번호 참조 반복 검색, 관련 섹션 추출, 과도한 길이 트리밍(40-500 토큰 범위)

- **도형 유형 분류**: 규칙 기반 방법으로 짧은 캡션의 핵심 구문 추출(1,506개 → 수동 수정 후 412개 클래스)

- **OCR 기반 참조 기호 매칭**: docTR OCR 라이브러리 선택(정확도 72.08%)으로 참조 기호 추출 및 설명과 매칭

### LVLM 미세조정 실험

- **Vision-only 모델**: 이미지와 일반 프롬프트만으로 캡션 생성

- **Vision+Text 모델 (두 가지 버전)**:
  - 프롬프트에 특허 제목 추가
  - 프롬프트에 제목과 참조 기호-용어 정보 추가

- **훈련 설정**: MiniGPT-4의 선형 계층만 미세조정, 10 에포크, 짧은 캡션(최대 50 토큰), 긴 캡션(최대 500 토큰)

- **평가 지표**: BLEU, ROUGE, METEOR, CIDEr

## Originality

- **첫 대규모 특허 도형 캡션 데이터셋**: 짧은/긴 캡션, 참조 기호, 용어, 청구항 정보를 통합한 최초의 종합 데이터셋

- **특허 도형 특화 데이터 추출**: OCR 기반 참조 기호 매칭 등 특허 도형의 고유한 특성을 반영한 데이터 전처리 방법

- **LVLM을 활용한 특허 캡셔닝**: 특허 도형 캡셔닝에 최신 대규모 비전-언어 모델 처음 적용

- **다중 텍스트 단서 통합**: 이미지 기반 정보와 특허 메타데이터(제목, 용어)를 결합한 캡션 생성 방식

## Limitation & Further Study

- **제한사항**:
  - 미세조정 효율성 부족: 긴 캡션 학습에 4,500단계 필요, 다중 GPU 옵션 미지원
  - 긴 캡션 생성 성능 낮음: CIDEr 점수가 매우 낮음(0.0114-0.0587)
  - 제한된 테스트 세트: 용어 포함 실험은 500개 샘플 부분집합에서만 수행
  - 참조 기호 포함 시 성능 저하: 표 3에서 Terms 추가 시 오히려 점수 감소

- **후속 연구**:
  - 긴 캡션 생성 성능 향상 방안 연구 필요
  - 특허 도형의 구조적 특성(블록 다이어그램, 흐름도 등)을 고려한 모델 개선
  - 더 효율적인 미세조정 방법 개발
  - 실제 특허 변리사 업무에서의 실용성 검증
  - 다국어 특허 도형 캡셔닝 확장


## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 3/5
- Clarity: 4/5
- Overall: 3.5/5

**총평**: 본 논문은 특허 도형 캡셔닝이라는 새로운 도메인을 개척하고 대규모 주석 데이터셋을 제공한 점에서 의미있는 기여를 하였으나, LVLM 기반 방법의 실제 성능(특히 긴 캡션)이 만족스럽지 못하고 기술적 혁신성이 부족하여 후속 연구 개선이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/178_Can_ai_examine_novelty_of_patents_Novelty_evaluation_based_o/review]] — 둘 다 AI의 특허 분야 활용을 다루지만 하나는 특허 도형 캡션 생성에, 다른 하나는 특허 신규성 검토에 초점을 맞춘다.
- 🏛 기반 연구: [[papers/196_ChartAssisstant_A_Universal_Chart_Multimodal_Language_Model/review]] — 범용 차트 멀티모달 언어 모델이 특허 도형의 다양한 시각적 요소를 이해하고 캡션을 생성하는 기반을 제공한다.
- 🔗 후속 연구: [[papers/564_Multi-llm_collaborative_caption_generation_in_scientific_doc/review]] — 과학 문서에서 다중 LLM 협업 캡션 생성 기법이 특허 도형의 복잡한 기술적 내용을 더욱 정확하게 캡션화하는데 활용될 수 있다.
