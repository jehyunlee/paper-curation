---
title: "125_Automated_latex_code_generation_from_handwritten_math_expres"
authors:
  - "Jayaprakash Sundararaj"
  - "Akhil Vyas"
  - "Benjamin Gonzalez-Maldonado"
date: "2024"
doi: "제시되지"
arxiv: ""
score: 3.5
essence: "필기 수학식 이미지를 LaTeX 코드로 변환하는 작업에서 Vision Transformer (ViT) 기반 인코더-디코더 아키텍처가 기존 CNN-LSTM 기준 모델을 능가하는 성능을 달성했다. 이 연구는 컴퓨터 비전과 자연어 처리를 결합한 이미지-투-시퀀스 문제에서 트랜스포머의 우월성을 입증한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Scientific_Text_Translation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Sundararaj et al._2024_Automated latex code generation from handwritten math expressions using vision transformer.pdf"
---

# Automated latex code generation from handwritten math expressions using vision transformer

> **저자**: Jayaprakash Sundararaj, Akhil Vyas, Benjamin Gonzalez-Maldonado | **날짜**: 2024 | **DOI**: [제시되지 않음]

---

## Essence

필기 수학식 이미지를 LaTeX 코드로 변환하는 작업에서 Vision Transformer (ViT) 기반 인코더-디코더 아키텍처가 기존 CNN-LSTM 기준 모델을 능가하는 성능을 달성했다. 이 연구는 컴퓨터 비전과 자연어 처리를 결합한 이미지-투-시퀀스 문제에서 트랜스포머의 우월성을 입증한다.

## Motivation

- **Known**: CNN-RNN(LSTM) 인코더-디코더 아키텍처는 수학식 인식의 표준 기준 모델로 자리잡았으며, 일부 연구는 양방향 디코더를 통해 성능을 개선했다.
  
- **Gap**: CNN-RNN 모델은 장거리 의존성 캡처와 입력 특성 표현에서 한계를 보이며, RNN의 순차 처리 제약과 소실 기울기(vanishing gradient) 문제가 존재한다.

- **Why**: Vision Transformer는 자기-주의(self-attention) 메커니즘을 통해 이미지의 지역적(local) 및 전역적(global) 특성을 동시에 포착할 수 있으며, 순환 구조의 제약을 극복한다.

- **Approach**: Vision Transformer 인코더와 트랜스포머 디코더를 결합한 아키텍처를 설계하고, CNN-LSTM, ResNet50-LSTM 기준 모델과 비교 실험을 수행한다.

## Achievement

![Figure 1](figures/fig1.webp)
*Figure 1: LaTeX 수식의 길이별 분포 (1~150 심볼 범위)*

![Figure 4](figures/fig4.webp)
*Figure 4: 원본 LaTeX 이미지와 생성된 패치 (10×10 픽셀 크기)*

1. **Vision Transformer의 우월성**: ViT 기반 모델이 CNN-RNN 기준 모델 대비 더 높은 정확도(accuracy)와 BLEU 점수를 달성하고, 더 낮은 Levenshtein 거리를 기록했다.

2. **개선된 특성 추출**: 이미지를 100개의 10×10 픽셀 패치로 분할하여 처리함으로써 지역적 세부 정보와 전역적 구조를 효과적으로 포착한다.

3. **확장성과 재현성**: 200,000개 데이터 포인트로 학습하여 실용적 규모의 검증을 완료했으며, GitHub에서 코드를 공개하여 재현 가능성을 보장한다.

## How

![Figure 2](figures/fig2.webp)
*Figure 2: CNN 기준 모델 인코더 구조 (50,200) → (25,100) → (12,50) 차원 축소*

![Figure 3](figures/fig3.webp)
*Figure 3: ResNet50 사전학습 모델 인코더와 LSTM 디코더*

![Figure 5](figures/fig5.webp)
*Figure 5: 트랜스포머 인코더 아키텍처 (8개 레이어, 4개 주의 헤드)*

### 기준 모델 (CNN-LSTM)
- 3×3 합성곱 필터와 2×2 최대 풀링을 3회 반복하는 인코더
- 토큰 임베딩과 이미지 인코딩을 결합하여 LSTM/GRU에 입력
- 최종 완전연결층에서 소프트맥스 활성화로 예측 생성

### ResNet50-LSTM 개선 모델
- 사전학습된 ResNet50을 인코더로 활용 (98 MB, ImageNet 사전학습)
- 그레이스케일 입력을 RGB로 변환 (`tf.image.grayscale_to_rgb`) 후 254×254로 리사이징
- 풍부한 특성 추출 능력으로 기준 모델 개선

### Vision Transformer 아키텍처
**인코더**:
- 이미지를 10×10 픽셀 패치 100개로 분할
- 선형 임베딩과 위치 임베딩 적용
- 8개 트랜스포머 레이어 (각 4개 주의 헤드)
- 각 레이어에 2,048→1,024 유닛의 MLP 블록 포함

**디코더**:
- 4개 주의 레이어 (교차-주의 및 자기-주의 각 8개 헤드)
- 교차-주의: 이미지의 관련 영역 식별
- 자기-주의: 생성 시퀀스의 의존성 모델링

### 학습 설정
- 데이터: Im2latex-100k, Im2latex-230k (총 200,000개 샘플, 849 MB)
- 입력: 50×200 픽셀 그레이스케일 이미지
- 어휘: 540개 심볼
- 배치 크기: CNN-LSTM, ResNet-LSTM은 128, ViT는 64
- 최적화: CNN/ResNet은 Adam(lr=0.001), ViT는 AdamW(lr: 1e-4→1e-6 감쇠)
- 조기 중단: 인내도 10 에포크
- 학습 시간: 1.5~2시간 (AWS G6.xlarge GPU)

## Originality

- **패치 기반 비전 트랜스포머 적용**: 필기 수학식 인식에 ViT를 체계적으로 적용한 것은 기존 CNN-RNN 기준과의 명확한 성능 비교를 제공한다.

- **그레이스케일-RGB 변환 기법**: 사전학습된 ResNet50을 그레이스케일 수학식 이미지에 효과적으로 적용하는 실용적 해결책을 제시한다.

- **교차-주의와 자기-주의의 이중 구조**: 이미지 영역 식별(교차-주의)과 시퀀스 일관성(자기-주의)을 동시에 처리하는 디코더 설계는 수학식 구조의 복잡성을 효과적으로 모델링한다.

- **오픈 소스 구현**: 재현 가능성을 높이고 후속 연구를 촉진하는 GitHub 공개는 학술 기여도를 증진한다.

## Limitation & Further Study

- **패치 크기의 경험적 선택**: 10×10 픽셀 패치 크기가 하이퍼파라미터 탐색 없이 선택되었으며, 다양한 패치 크기의 체계적 비교가 부족하다.

- **제한된 입력 해상도**: 50×200 픽셀의 낮은 해상도는 복잡하고 밀집된 수학식의 세부 정보 손실 가능성을 시사한다.

- **배치 크기 불일치**: GPU 메모리 제약으로 ViT(배치 64)와 CNN/ResNet(배치 128)의 배치 크기가 다르며, 이것이 공정한 비교를 저해할 수 있다.

- **정성적 오류 분석 부재**: 모델이 실패하는 패턴(예: 중첩 분수, 행렬 구조)에 대한 구체적 분석이 제시되지 않았다.

- **후속 연구 방향**:
  - 더 높은 해상도의 입력 이미지 처리 및 적응형 패치 크기 설정
  - 주의 메커니즘의 시각화를 통한 해석 가능성 향상
  - 실제 필기 데이터(OCR 기반이 아닌)를 포함한 데이터셋 확장
  - 디코딩 제약(유효한 LaTeX 문법 강제)을 통한 오류율 감소

## Evaluation

- **Novelty**: 3.5/5
  - Vision Transformer를 수학식 인식에 적용한 것은 적절한 선택이나, 각 구성 요소(패치 분할, 인코더-디코더 구조)가 기존 ViT 논문을 크게 벗어나지 않는다. 아키텍처 혁신보다는 응용 영역 확대에 가깝다.

- **Technical Soundness**: 4/5
  - 인코더-디코더 아키텍처의 설계는 타당하며, 그레이스케일-RGB 변환 같은 실무적 해결책이 잘 구현되었다. 다만 교차-주의 메커니즘의 상세한 설명과 수렴 분석이 부족하고, 하이퍼파라미터 선택의 정당성이 충분하지 않다.

- **Significance**: 3.5/5
  - 수학식 인식의 실용적 개선을 보여주지만, 최첨단 성능 달성 여부나 정량적 개선 폭에 대한 구체적 수치가 제시되지 않았다. 학계 및 산업 응용의 영향력 평가가 어렵다.

- **Clarity**: 4/5
  - 아키텍처 설명과 실험 설정이 명확하며, 도표와 수식이 적절히 배치되었다. 다만 결과 분석 섹션(실험 설정 이후)의 내용이 완성되지 않아 성능 비교표와 정성적 분석의 부재로 인해 결론의 설득력이 감소한다.

- **Overall**: 3.5/5

**총평**: 이 논문은 Vision Transformer를 필기 수학식 인식 작업에 체계적으로 적용하고 기존 CNN-RNN 기준 모델과 비교한 실용적 연구이다. 아키텍처 설계와 구현은 견고하며 오픈 소스 공개로 재현성을 확보했다. 그러나 완성되지 않은 결과 분석 섹션, 정량적 성능 수치의 부재, 그리고 아키텍처 혁신보다는 기존 기법의 응용에 머물러 있다는 점이 학술적 기여도를 제한한다. 추가적으로 더 높은 해상도 입력과 실제 필기 데이터 실험이 필요하며, 오류 사례 분석을 통한 통찰력 제공이 논문의 가치를 크게 높일 수 있을 것으로 예상된다.

## Related Papers

- 🔄 다른 접근: [[papers/383_Geometry_Informed_Tokenization_of_Molecules_for_Language_Mod/review]] — 둘 다 분자 및 수학적 구조의 언어 모델 토크나이제이션을 다루지만 하나는 필기 수학식의 LaTeX 변환에, 다른 하나는 분자의 기하학적 토크나이제이션에 초점을 맞춘다.
- 🔗 후속 연구: [[papers/439_Invariant_Tokenization_of_Crystalline_Materials_for_Language/review]] — 결정 물질의 불변 토크나이제이션 기법이 필기 수학식 이미지의 구조적 표현 학습에 적용될 수 있다.
- 🏛 기반 연구: [[papers/748_Semi-Supervised_2D_Human_Pose_Estimation_Driven_by_Position/review]] — 위치 임베딩 기반의 반지도 학습 방법이 필기 수학식의 공간적 구조 인식에 이론적 기반을 제공한다.
- 🔄 다른 접근: [[papers/690_Rule-based_neural_and_llm_back-translation_Comparative_insig/review]] — 둘 다 언어 간 변환을 다루지만 하나는 저자원 언어 역번역이고 다른 하나는 필기 수학식의 LaTeX 변환이다.
