# SciCap+: A Knowledge Augmented Dataset to Study the Challenges of Scientific Figure Captioning

> **저자**: Zhishen Yang, Raj Dabre, Hideki Tanaka, Naoaki Okazaki | **날짜**: 2023 | **학회**: arXiv (AAAI format) | **DOI**: 10.48550/ARXIV.2306.03491

---

## Essence

SciCap+는 기존 SciCap 데이터셋(414K 과학 figure-caption 쌍)을 mention-paragraph(본문에서 해당 figure를 언급하는 단락)과 OCR 토큰(figure 내 텍스트 및 위치 정보)으로 확장한 knowledge-augmented 데이터셋이다. 과학 figure captioning을 단순 image-to-caption이 아닌 multimodal summarization task으로 재정의하고, M4C-Captioner를 통해 맥락 지식이 캡션 생성 품질을 대폭 향상시킴을 실증하였다.

## Motivation

- **알려진 것**: SciCap(Hsu et al., 2021)이 arXiv CS 논문에서 추출한 대규모 과학 figure captioning 데이터셋을 제공하였으나, figure-to-caption 단일 매핑으로 한정
- **Gap**: 과학 figure는 자연 이미지와 달리 텍스트와 데이터 포인트가 핵심 시각 객체이며, 캡션이 단순 객체 기술이 아닌 과학적 발견의 해석을 담아야 하므로 배경 지식 없이는 적절한 캡션 생성이 불가능
- **왜 중요한가**: 과학 논문의 figure 캡션 자동 생성은 논문 작성 지원과 과학 커뮤니케이션 품질 향상에 직결
- **접근법**: SciCap에 mention-paragraph와 OCR 토큰을 추가하여 SciCap+를 구축하고, multimodal transformer 기반 M4C-Captioner로 다양한 modality 조합의 효과를 검증

## Achievement

1. **대규모 데이터셋 구축**: 394,005/10,336/10,468 (train/test/val) 규모의 SciCap+ 데이터셋, document-level 분할로 기존 SciCap의 data leakage 문제 해결
2. **Mention-paragraph의 결정적 효과**: Figure-only CIDEr 4.6 → Mention-only CIDEr 49.0 (약 10배 향상), 전체 feature 결합 시 CIDEr 55.8
3. **Figure 이미지 불필요 발견**: Mention + OCR만 사용 시 CIDEr 56.4로 전체 feature(55.8)보다 오히려 높아, figure 시각 정보가 현재 모델에서는 noise에 가까움
4. **Human evaluation 실시**: 인간 평가자도 figure-only 조건에서 모델과 유사한 수준의 저조한 캡션 생성 (annotator CIDEr 14.6~23.8 vs. 모델 18.7), 배경 지식의 필요성을 실증
5. **적절성 평가**: Ground-truth 캡션조차 평균 적절성 점수 ~2.0/4.0으로 낮아, 과학 figure captioning의 본질적 난이도를 정량적으로 확인

## How

- **데이터 확장**: Kaggle arXiv dataset에서 PDF 확보 → PDFFigures 2.0으로 본문 추출 → 정규표현식으로 figure 번호 기반 mention-paragraph 매칭 → Google Vision OCR API로 OCR 토큰(텍스트 + bounding box) 추출
- **데이터 품질 검증**: 200개 figure에 대해 2명의 CS PhD 평가자가 mention-paragraph/OCR 토큰과 캡션의 관련성 1-5점 평가 (64%/79.5%가 3점 이상, Cohen's kappa 0.28)
- **모델**: M4C-Captioner (M4C 기반 multimodal transformer + pointer network) -- 고정 사전 또는 OCR 토큰에서 단어를 선택하여 OOV 문제 해결
- **인코더**: ResNet-152 (figure), SciBERT 3-layer (mention-paragraph), FastText + PHOC + Faster R-CNN fc6/fc7 (OCR 토큰)
- **학습**: 8x V100 GPU, batch 128, Adam lr=0.001, CIDEr 기반 early stopping, max decoding 67 steps
- **평가**: BLEU-4, METEOR, ROUGE-L, SPICE, CIDEr + human generation task (100 figures) + appropriateness evaluation (1-4 scale)

## Originality

- **Task 재정의**: 과학 figure captioning을 knowledge-augmented image captioning (multimodal summarization)으로 최초 재정의 -- figure 이미지만이 아닌 mention-paragraph와 OCR 토큰이라는 cross-modal knowledge의 필요성을 공식화
- **Mention-paragraph 활용**: 본문 내 figure 언급 단락을 명시적 지식 소스로 추출하여 captioning에 활용하는 접근은 기존 figure captioning 연구에서 시도되지 않은 방법
- **Document-level 분할**: 기존 SciCap의 figure-level 분할이 야기하는 정보 누출 문제를 지적하고 document-level로 재분할
- **Human vs. Machine 직접 비교**: 동일 조건에서 인간 캡션 생성과 모델 캡션 생성을 정량적으로 비교하여 task 난이도를 객관적으로 측정

## Limitation & Further Study

### 저자들이 언급한 한계

- 모델 생성 캡션이 자동 메트릭에서는 양호하나 인간 적절성 평가에서는 여전히 낮은 수준 (~2/4)
- Ground-truth 캡션 자체도 적절성이 낮아, 캡션 작성 규범의 부재가 과제의 본질적 어려움
- Human evaluator 간 낮은 일치도 (Cohen's kappa 0.23-0.36)로 figure captioning 평가의 주관성 확인

### 자체판단 아쉬운 점

- 데이터셋이 arXiv CS 논문의 graph plot에 한정되어, 다른 분야(생물학, 화학 등)나 다른 figure 유형(현미경 이미지, 분자 구조 등)에 대한 일반화 불명
- M4C-Captioner 단일 모델만 실험하여, 당시 이미 존재하던 BLIP-2, Flamingo 등 최신 LVLM과의 비교가 없음
- ResNet-152 visual encoder가 과학 figure에 부적합하다는 결론을 내렸으나, ViT 등 대안 encoder 실험 없이 "figure 이미지 불필요"라는 결론에 이름
- Human evaluation이 2명의 평가자에 의존하여 통계적 신뢰성이 제한적
- Mention-paragraph 추출의 정규표현식 기반 방법이 복수 figure 언급, figure 번호 변형 등을 얼마나 잘 처리하는지 체계적 분석 부족

### 후속 연구

- Multimodal pretraining 전략을 활용한 figure captioning 모델 개발
- 과학 figure 전용 vision encoder 학습
- 다양한 학문 분야 및 figure 유형으로의 확장
- 캡션 작성 가이드라인 수립 및 캡션 품질 개선 연구

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 3/5 |
| Significance | 3/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: 과학 figure captioning을 knowledge-augmented task으로 재정의하고 mention-paragraph의 결정적 기여를 실증한 것은 의미 있는 통찰이나, 단일 모델(M4C-Captioner) 실험과 CS graph plot 한정이라는 범위 제약이 아쉽다. "Figure 이미지가 noise"라는 발견은 visual encoder의 한계를 반영할 뿐 figure 시각 정보 자체의 무용성을 의미하지 않으며, 이 점에 대한 심층 분석이 필요하다.
