---
title: "338_Figuring_out_figures_Using_textual_references_to_caption_sci"
authors:
  - "Stanley Cao"
  - "K. Liu"
date: "2024"
doi: "arXiv:2407.11008"
arxiv: ""
score: 3.5
essence: "과학 논문의 그래프 및 도형에 대한 자동 캡션 생성을 위해 CLIP+GPT-2 모델에 논문의 메타데이터(제목, 초록, 참고문헌 인용 텍스트)를 SciBERT를 통해 통합한 멀티모달 접근법을 제시한다. 특히 텍스트 정보만 사용한 SciBERT+GPT-2 모델이 BLEU 6.71을 달성하며 기존 CNN+LSTM 기반선(BLEU 2.59)을 크게 상회했다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Scientific_Figure_Captioning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Cao and Liu_2024_Figuring out figures Using textual references to caption scientific figures.pdf"
---

# Figuring out figures: Using textual references to caption scientific figures

> **저자**: Stanley Cao, K. Liu | **날짜**: 2024 | **DOI**: [arXiv:2407.11008](https://arxiv.org/abs/2407.11008)

---

## Essence

과학 논문의 그래프 및 도형에 대한 자동 캡션 생성을 위해 CLIP+GPT-2 모델에 논문의 메타데이터(제목, 초록, 참고문헌 인용 텍스트)를 SciBERT를 통해 통합한 멀티모달 접근법을 제시한다. 특히 텍스트 정보만 사용한 SciBERT+GPT-2 모델이 BLEU 6.71을 달성하며 기존 CNN+LSTM 기반선(BLEU 2.59)을 크게 상회했다.

## Motivation

- **Known**: 자연 이미지 캡셔닝은 발전했지만, 과학 논문의 컴퓨터 생성 도형 캡셔닝은 BLEU 스코어 약 2로 매우 낮은 성능 유지. Hsu et al. [1]의 SCICAP 데이터셋 기반 CNN+LSTM 단층 구조가 현재 최고 성능.

- **Gap**: (1) 도형만으로는 정확한 수치 추출과 맥락적 정보 파악 불충분, (2) 자연 이미지용으로 훈련된 ResNet-101은 과학 도형 분포 미부합, (3) 텍스트 기반 문맥정보 활용 미흡.

- **Why**: 과학 캡션은 도형을 보완하고 문맥을 제공하기 위해 설계되었으므로, 논문의 제목, 초록, 그리고 해당 도형에 대한 인-텍스트 참고문헌 정보를 함께 활용하면 성능 향상 가능.

- **Approach**: CLIP-ViT/B-32 비전 인코더와 SciBERT 텍스트 인코더의 출력을 결합하여 GPT-2 디코더로 캡션 생성. METASCICAP 데이터셋 구성으로 메타데이터와 인-텍스트 참고문헌 통합.

## Achievement

1. **SciBERT+GPT-2 (텍스트만)**: BLEU 6.71, ROUGE-L F1 0.30 달성 → 기존 CNN+LSTM (BLEU 2.59) 대비 **159% 향상**

2. **CLIP+SciBERT+DistilGPT-2 (이미지+텍스트)**: BLEU 4.92, ROUGE-L F1 0.26 달성 → 텍스트 모달리티의 우월성 시사

3. **METASCICAP 데이터셋 구축**: 416,000개 그래프 도형에 메타데이터와 추출된 인-텍스트 참고문헌(±100자 윈도우) 연결

## How

- **모델 아키텍처**:
  - 비전 인코더: CLIP-ViT/B-32 (Vision Transformer, 3×224×224 입력을 32×32 패치로 분할)
  - 텍스트 인코더: SciBERT (scientific text 학습, 메타데이터 토큰화)
  - 디코더: GPT-2 또는 DistilGPT-2 (cross-attention 추가)
  - 인코더 출력 결합: CLIP 임베딩 + SciBERT 임베딩 concatenation

- **데이터 처리**:
  - 이미지: 224×224로 리사이징, CLIP 학습셋 평균/표준편차로 정규화
  - 텍스트: 제목(100자), 초록(150자), 참고문헌(나머지 컨텍스트) → [SEP] 토큰으로 분리
  - 참고문헌 추출: PDF에서 Smith-Waterman 알고리즘으로 캡션 마스킹 후 정규식으로 주변 100자씩 추출

- **훈련 설정**:
  - 옵티마이저: AdamW (학습률 5×10⁻⁵, 선형 감소 스케줄)
  - 에포크: 15 (약 12시간/실험)
  - 정규화: SciBERT 인코딩에 dropout 확률 0.7 적용 (텍스트 과존존 억제)
  - 생성: top-p 샘플링 (p=0.9)
  - 평가: SacreBLEU (case-insensitive), ROUGE-L F1

## Originality

- **멀티모달 정보 통합**: 기존 순수 비전 기반 접근(CNN+LSTM)에서 벗어나 메타데이터와 인-텍스트 참고문헌을 명시적으로 활용한 점

- **METASCICAP 데이터셋 구축**: SCICAP에 논문 메타데이터와 추출된 참고 텍스트를 연결한 새로운 주석 리소스 제공

- **현대 사전훈련 모델 도입**: Vision Transformer(CLIP) 및 도메인 특화 모델(SciBERT)의 조합으로 기존 ResNet+LSTM 대비 구조적 업그레이드

- **음성 결과 분석**: 텍스트 기반 모델이 이미지+텍스트 결합 모델을 상회하는 현상을 드러내며, 모달리티 가중치 문제 제기

## Limitation & Further Study

- **이미지 특성 활용 미흡**: CLIP+SciBERT+GPT-2 (BLEU 4.92)가 SciBERT+GPT-2 (BLEU 6.71)보다 낮으며, 드롭아웃(0.7)을 적용해도 이미지 기여도 제한적 → 멀티모달 정렬(alignment) 개선 필요

- **평가 메트릭 한계**: BLEU와 ROUGE는 어휘 기반으로 의미적 정확성 미흡. 도형의 수치 정확도(numerical accuracy) 평가 지표 부재

- **데이터셋 편향**: 컴퓨터 과학 arXiv 논문만 포함 (2010-2020) → 타 분야(생물학, 화학, 물리학) 및 시간적 다양성 제한

- **생성 안정성**: 텍스트 기반 모델의 과도한 의존성 시사 → 도형의 구조적 특성(축, 범례, 데이터점)을 명시적으로 모델링하는 그래프 파싱 기법 병행 제안

- **후속 연구**:
  - 비전-텍스트 크로스모달 정렬 강화 (contrastive learning, fusion gate 등)
  - 도형 유형별(그래프, 다이어그램, 테이블) 맞춤 모델
  - 설명적 평가(human evaluation) 및 도메인 전문가 검증
  - 더 큰 언어모델(LLaMA, GPT-3.5) 활용 실험


## Evaluation

- Novelty: 3/5
- Technical Soundness: 3.5/5
- Significance: 3.5/5
- Clarity: 4/5
- Overall: 3.5/5

**총평**: 과학 도형 캡셔닝에서 텍스트 메타데이터의 중요성을 명확히 입증한 실용적 연구이나, 멀티모달 모델의 설계 결함(이미지 기여도 역설)을 노출함으로써 향후 보다 근본적인 아키텍처 혁신이 필요함을 시사한다.

## Related Papers

- 🔄 다른 접근: [[papers/488_Leveraging_LLMs_in_Scholarly_Knowledge_Graph_Question_Answer/review]] — 둘 다 과학 논문의 텍스트 정보를 활용한 QA를 다루지만 하나는 도형 캡션 생성에, 다른 하나는 학술 지식 그래프 질의응답에 초점을 맞춘다.
- 🔗 후속 연구: [[papers/602_Paperqa_Retrieval-augmented_generative_agent_for_scientific/review]] — 검색 증강 생성 에이전트를 이용한 과학 QA 시스템이 과학 도형 캡션 생성에서 참조 텍스트 활용을 더욱 정교화할 수 있다.
- 🏛 기반 연구: [[papers/329_Explaining_relationships_among_research_papers/review]] — 연구 논문 간의 관계 설명 기법이 과학 도형과 텍스트 참조 간의 연결 관계를 이해하는 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/709_SciCap_A_Knowledge_Augmented_Dataset_to_Study_the_Challenges/review]] — 텍스트 참조를 활용한 과학 도형 캡션 생성이 SciCap+의 지식 증강 접근법과 상호 보완적인 멀티모달 컨텍스트를 제공한다.
