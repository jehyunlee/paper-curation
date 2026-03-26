# PatFig: Generating Short and Long Captions for Patent Figures

> **저자**: Dana Aubakirova, Kim Gerdes, Lufei Liu | **날짜**: 2023 | **학회**: ICCVW 2023 (IEEE/CVF) | **DOI**: 10.1109/ICCVW60793.2023.00305

---

## Essence

Qatent PatFig는 11,000건 이상의 유럽 특허 출원에서 추출한 30,000+개의 특허 도면으로 구성된 최초의 대규모 특허 도면 캡셔닝 데이터셋이다. 각 도면에 대해 짧은/긴 캡션, 참조 번호(reference numerals)와 대응 용어, 최소 청구항 집합을 제공하며, MiniGPT-4를 fine-tuning하여 특허 도면의 자동 캡션 생성 가능성을 검증하였다.

## Motivation

- **알려진 것**: 과학 논문 figure captioning(SciCap 등)에 대한 연구는 존재하나, 특허 도면은 참조 번호, 용어 목록, 짧은/긴 설명, 청구항 등 고유한 구조적 특성을 가짐
- **Gap**: 기존 특허 도면 데이터셋(CLEF-IP 2011: 211건, DeepPatent: 디자인 특허 한정)은 규모가 작거나 캡션이 없어 figure captioning 연구에 부적합
- **왜 중요한가**: 특허 도면은 복잡한 기술 개념을 시각적으로 전달하는 핵심 요소이며, 자동 캡션 생성은 특허 변리사의 업무 효율화와 특허 검색/분류 개선에 직결
- **접근법**: EPO 데이터베이스에서 rule-based 방식으로 short/long caption을 추출하고, OCR(docTR)로 참조 번호를 매칭한 뒤, MiniGPT-4를 fine-tuning하여 Vision-only 및 Vision+Text 캡셔닝 실험 수행

## Achievement

1. **대규모 데이터셋 구축**: 30,714개 특허 도면(15,645개 특허)에서 정제된 17,877/2,417 train/test 세트 구성, 412개 도면 유형 분류체계 확립
2. **OCR 벤치마크**: 4개 OCR 라이브러리 비교 -- docTR가 72.08% 정확도로 최고 성능 (PyOCR 14.03%, Pytesseract 17.42%, EasyOCR 53.22%)
3. **Short caption 최고 성능**: Image+Title 조합에서 BLEU4 0.4276, ROUGE 0.4390, CIDEr 0.7939 달성 (참조 번호 제외 평가)
4. **Long caption 개선**: Image+Title+Terms 조합이 CIDEr 0.0587로 Vision-only(0.0142) 대비 약 4배 향상
5. **Textual cue 효과 분석**: Title 추가는 일관되게 성능 향상, Terms 추가는 long caption에서만 효과적이고 short caption에서는 오히려 성능 저하

## How

- **데이터 수집**: Qatent의 Solr DB에서 EPO 특허 텍스트 데이터 확보, Espacenet에서 2020년 특허 이미지 62,513장 스크래핑
- **Short caption 추출**: "Brief Description of Drawings" 섹션에서 rule-based 추출, IQR 기반 10~40 토큰 필터링
- **Long caption 추출**: 텍스트 정규화 후 반복 figure 번호 참조를 추적하여 관련 단락 추출, 40~500 토큰 필터링
- **Figure-type 분류**: Short caption에서 "is a/an", "shows", "illustrates" 등의 패턴으로 1,506개 클래스 추출 후 수작업으로 412개로 정제
- **모델**: MiniGPT-4 (ViT + Q-Former + Linear Projection + Vicuna LLM) -- 2nd stage fine-tuning만 수행, linear projection layer만 학습
- **학습 설정**: 10 epochs, short caption max 50 tokens (RTX A6000), long caption max 500 tokens (A100 80GB), batch size 4
- **평가 메트릭**: BLEU-2/4, ROUGE, METEOR, CIDEr

## Originality

- **최초의 특허 도면 캡셔닝 데이터셋**: 과학 figure captioning(SciCap)과 달리 참조 번호, 용어 목록, 청구항을 포함한 rich annotation 제공
- **Multi-granularity 캡션**: 동일 도면에 대해 short/long 두 가지 수준의 캡션을 함께 제공하는 구조는 기존 데이터셋에 없던 설계
- **Textual cue 활용 전략**: Patent-specific 메타데이터(title, terms)를 LVLM 입력에 통합하여 도메인 특화 캡셔닝의 가능성을 탐색
- **도면 유형 분류체계**: Photo/View/Diagram/Chart/Table로 이어지는 계층적 특허 도면 분류 taxonomy 제안

## Limitation & Further Study

### 저자들이 언급한 한계

- MiniGPT-4의 frozen Q-Former가 visual-spatial grounding 정보를 손실할 수 있음
- 단일 linear projection layer만 학습하여 visual-text alignment 학습 능력이 제한적
- Multi-GPU fine-tuning 미지원으로 학습 효율성이 낮음 (batch size 4, 4500 steps)

### 자체판단 아쉬운 점

- 정량적 성능이 전반적으로 낮음 (특히 long caption CIDEr 0.06 수준) -- 실용적 활용 가능성에 대한 논의가 부족
- Human evaluation이 전혀 수행되지 않아, 자동 메트릭으로 측정되지 않는 캡션 품질(정확성, 유용성)을 평가하지 못함
- 데이터셋이 2020년 EPO 특허에 한정되어, 기술 분야/시대/특허청 간 일반화 가능성이 검증되지 않음
- 비교 대상 모델이 MiniGPT-4 하나뿐이며, BLIP-2 등 다른 LVLM과의 비교가 없어 baseline의 대표성이 약함
- Rule-based caption 추출의 정확도/커버리지에 대한 정량적 평가가 없음

### 후속 연구

- Fine-tuning 단계에서 textual cue를 포함한 학습 및 참조 번호 제거 텍스트 학습
- 이미지에서 참조 번호를 제거한 학습 데이터 구성
- 도면 유형별 성능 분석 및 유형별 특화 모델 개발
- Text-to-image 방향의 특허 도면 자동 생성 연구
- 이미지 없이 텍스트만으로 도면 내용 예측이 가능한 임계점 탐색

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 2/5 |
| Significance | 3/5 |
| Clarity | 3/5 |
| Overall | 3/5 |

**총평**: 특허 도면이라는 미개척 영역에 최초의 대규모 캡셔닝 데이터셋을 구축한 의의가 있으나, 실험 설계(단일 모델, human evaluation 부재)와 성능 수준(long caption CIDEr < 0.06)이 미흡하여 데이터셋 소개 논문으로서의 완성도가 아쉽다. 데이터셋 자체의 풍부한 annotation(참조 번호, 용어, 청구항)은 후속 연구에 유용한 자원이 될 수 있다.
