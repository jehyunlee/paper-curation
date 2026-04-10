---
title: "709_SciCap_A_Knowledge_Augmented_Dataset_to_Study_the_Challenges"
authors:
  - "Zhishen Yang"
  - "Raj Dabre"
  - "Hideki Tanaka"
  - "Naoaki Okazaki"
date: "2023"
doi: "10.48550/ARXIV.2306.03491"
arxiv: ""
score: 4.0
essence: "과학 논문의 도표 캡션 자동 생성을 지식 증강 이미지 캡셔닝(knowledge-augmented image captioning) 문제로 재정의하고, 멘션 문단(mention-paragraph)과 OCR 토큰을 포함한 SciCap+ 데이터셋을 구축하여 다중모드(multimodal) 컨텍스트 정보가 캡션 생성에 미치는 영향을 분석한 연구이다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Scientific_Figure_Captioning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yang et al._2023_SciCap+ A Knowledge Augmented Dataset to Study the Challenges of Scientific Figure Captioning.pdf"
---

# SciCap+: A Knowledge Augmented Dataset to Study the Challenges of Scientific Figure Captioning

> **저자**: Zhishen Yang, Raj Dabre, Hideki Tanaka, Naoaki Okazaki | **날짜**: 2023 | **DOI**: [10.48550/ARXIV.2306.03491](https://doi.org/10.48550/ARXIV.2306.03491)

---

## Essence

![Figure 1](figure1.png)
*그림 1: 멘션 문단과 OCR 토큰이 없으면 데이터 해석이 불가능함을 보여주는 예시*

과학 논문의 도표 캡션 자동 생성을 지식 증강 이미지 캡셔닝(knowledge-augmented image captioning) 문제로 재정의하고, 멘션 문단(mention-paragraph)과 OCR 토큰을 포함한 SciCap+ 데이터셋을 구축하여 다중모드(multimodal) 컨텍스트 정보가 캡션 생성에 미치는 영향을 분석한 연구이다.

## Motivation

- **Known**: 선행 연구(SciCap)는 도표만으로 캡션을 생성하는 도표-캡션 쌍(figure-to-caption) 작업으로 정의했으며, 상대적으로 낮은 성능을 보임
- **Gap**: 과학 도표는 자연 이미지와 달리 텍스트와 데이터 포인트로 구성되며, 배경 지식 없이 정보성 있는 캡션을 작성하기 어려움. 기존 연구는 이러한 특성을 간과함
- **Why**: 인간도 충분한 배경 지식 없이는 도표를 해석하고 캡션을 작성하기 어려우므로, 모델도 텍스트와 시각 모달리티에서 추출한 컨텍스트 지식이 필요
- **Approach**: 기존 SciCap 데이터셋에 멘션 문단과 OCR 토큰을 추가하여 SciCap+ 구축하고, M4C-Captioner(다중모드 트랜스포머 기반 포인터 네트워크 모델)로 실험

## Achievement

![Figure 2](figure2.png)
*그림 2: SciCap+ 데이터셋 생성을 위한 데이터 증강 워크플로우*

1. **데이터셋 확장**: 414k 개의 도표를 포함하는 SciCap을 멘션 문단과 OCR 토큰(좌표 정보 포함)으로 확장하여 SciCap+ 구축
   - 훈련 세트: 394,005개 도표, 검증/테스트: 각 ~10k개 도표
   - 문서 레벨에서 재분할하여 데이터 누수(leakage) 해결

2. **성능 향상**: 멘션 문단 및 OCR 토큰을 추가하면 자동 평가 지표(automatic evaluation metrics)에서 도표만 사용한 베이스라인 대비 **유의미한 성능 개선** 달성

3. **인간 평가 통찰**:
   - 모델 생성 캡션이 인간이 작성한 캡션만큼 정보 제공
   - 평가자들이 둘 중 하나를 선호하지 않음
   - 멘션 문단을 참고해도 인간이 원문 캡션에 가까운 캡션을 작성하기 어려움

## How

![Figure 3](figure3.png)
*그림 3: 멘션 문단과 OCR 토큰과 도표 캡션 간 관련성 점수 분포 (코헨 카파: 0.28)*

**데이터 수집 및 처리**:
- PDFFigures 2.0을 이용해 PDF에서 도표 및 본문 추출
- 도표 번호 기반 정규표현식으로 멘션 문단 추출 (첫 번째 매칭 문단만 선택)
- Google Vision OCR API로 도표 내 텍스트와 바운딩 박스 추출

**모델 아키텍처**:
- 베이스라인: M4C-Captioner (Multimodal Multi-Copy Mesh 기반)
- 포인터 네트워크를 통해 OCR 토큰이나 고정 딕셔너리에서 단어 선택
- 도표, 멘션 문단, OCR 토큰의 3가지 입력 특성 사용

**인코더 구성**:
- 시각 인코더: ResNet-152 (2D 적응형 평균 풀링으로 2048차원 특성 추출)
- 텍스트 인코더: SciBERT (758차원 특성 벡터)
- SentencePiece로 32,000 서브워드 딕셔너리 구축

## Originality

- **첫 시도**: 과학 도표 캡셔닝을 다중모드 요약(multimodal summarization) 작업으로 재정의
- **컨텍스트 통합**: 기존 도표 중심 접근에서 텍스트 및 시각 모달리티 컨텍스트 통합
- **데이터셋 개선**: 기존 SciCap의 문서 레벨 재분할로 평가 공정성 확보
- **종합 평가**: 자동 평가 지표와 인간 평가를 결합하여 작업의 내재적 어려움 규명

## Limitation & Further Study

**한계**:
- 평가자 간 합의도가 낮음(코헨 카파 0.28): 도표 캡션 평가의 주관성 문제 미해결
- 컴퓨터과학 논문만 대상이므로 다른 학문 분야로의 일반화 불명확
- 멘션 문단 관련성 점수 분포가 편향적(64~79.5%만 점수 3 이상): 노이즈 많은 데이터 포함 가능
- 문서 레벨 재분할로 인한 훈련 세트 규모 감소의 영향 미분석

**후속 연구**:
- 도표 유형별(선그래프, 막대그래프, 산점도 등) 성능 분석
- 멘션 문단의 구체적 어떤 정보가 가장 도움이 되는지 정밀 분석 (어텐션 가시화)
- 다른 학문 분야(생물학, 화학, 물리학 등)로의 확장
- 인간 평가자 간 합의 개선 방안(가이드라인 강화, 다수 평가자 활용)
- 더 강력한 다중모드 모델(예: 비전-랭귀지 사전학습 모델) 탐색


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 과학 논문 도표 캡션 생성을 위한 지식 증강 데이터셋 구축이라는 실용적 기여는 분명하지만, 모델 혁신이 부재하고 인간 평가 신뢰도 문제가 있어 순수 학술적 기여는 중상 수준이다. 공개 데이터셋의 가치와 컨텍스트 정보의 효과 입증이 주요 의의이다.

## Related Papers

- 🔗 후속 연구: [[papers/338_Figuring_out_figures_Using_textual_references_to_caption_sci/review]] — 텍스트 참조를 활용한 과학 도형 캡션 생성이 SciCap+의 지식 증강 접근법과 상호 보완적인 멀티모달 컨텍스트를 제공한다.
- 🏛 기반 연구: [[papers/204_Chartx__chartvlm_A_versatile_benchmark_and_foundation_model/review]] — 다목적 차트 및 시각화 모델이 SciCap+의 과학 도형 이해에 필요한 기반 기술을 제공한다.
- 🔄 다른 접근: [[papers/197_Chartcoder_Advancing_multimodal_large_language_model_for_cha/review]] — 둘 다 멀티모달 차트 이해를 다루지만 하나는 과학 논문의 지식 증강에, 다른 하나는 일반적인 차트 코딩에 초점을 맞춘다.
- 🏛 기반 연구: [[papers/336_FigCaps-HF_A_Figure-to-Caption_Generative_Framework_and_Benc/review]] — 과학 캡션 생성의 도전과제 분석이 RLHF 기반 개선 방법론의 기반
