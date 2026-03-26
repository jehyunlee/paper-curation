# SciCap: Generating Captions for Scientific Figures

> **저자**: Ting-Yao Hsu, C. Lee Giles, Ting-Hao Huang | **날짜**: 2021 | **Conference**: Findings of EMNLP 2021 | **DOI**: 10.18653/v1/2021.findings-emnlp.277

---

## Essence

SciCap은 과학 논문의 figure에 대한 자동 캡션 생성을 위해 구축된 최초의 대규모 실세계 figure-caption 데이터셋이다. arXiv 컴퓨터과학 논문 290,000편 이상에서 200만 개 이상의 figure를 추출하고, figure type 분류, subfigure 제거, 텍스트 정규화 등 체계적 전처리 파이프라인을 통해 graph plot 중심의 133,543개 고품질 figure-caption 쌍을 제공하며, CNN+LSTM 기반 baseline 모델로 과학 figure captioning의 가능성과 도전과제를 실증적으로 제시했다.

## Motivation

- **알려진 것**: 과학 논문에서 figure는 복잡한 정보를 전달하는 핵심 매체이며, 캡션의 품질이 독자의 이해도에 직접적 영향을 미침
- **Gap**: 기존 figure captioning 연구(FigCAP, FigureQA, DVQA)는 합성(synthetic) figure와 generic한 캡션에 의존하여, 실제 과학 논문의 맥락적이고 통찰 중심적인 캡션과 괴리가 큼. 대규모 실세계 과학 figure-caption 데이터셋이 부재
- **왜 중요한가**: (1) 연구자가 더 나은 캡션을 작성하도록 지원, (2) 시각장애 독자를 위한 과학 figure 접근성 향상이라는 이중 동기
- **접근법**: arXiv 공개 데이터셋에서 실세계 figure-caption 쌍을 대규모로 수집하고, 체계적 전처리 후 end-to-end neural captioning baseline을 구축

## Achievement

1. **대규모 데이터셋 구축**: 295,028편의 arXiv CS 논문에서 2,170,719개 figure를 추출하고, graph plot 133,543개의 정제된 figure-caption 쌍을 제공
2. **체계적 전처리 파이프라인**: Figure type 분류(7종, 95% accuracy), subfigure 필터링(precision 0.98), 텍스트 정규화(Basic/Advanced), 3가지 캡션 선택 전략 수립
3. **Baseline 성능 확립**: CNN+LSTM 모델로 Vision-only, Text-only, Vision+Text 3가지 변형을 실험하여 BLEU-4 기준 0.02~0.03 수준의 성능을 보고
4. **합성 vs 실세계 캡션 차이 규명**: 합성 캡션은 "This is a line plot. It contains 6 categories."처럼 generic한 반면, 실세계 캡션은 맥락적 통찰을 포함함을 실증
5. **공개 데이터셋**: CC-0 라이선스 하에 GitHub에서 데이터셋과 코드를 공개하여 후속 연구 촉진

## How

- **데이터 소스**: arXiv dataset (2010-2020, CS + stat.ML), CC-0 라이선스, 총 295,028편
- **Figure 추출**: PDFFigures 2.0으로 figure 이미지, 캡션, figure 내부 텍스트(legend, 축 라벨 등) 동시 추출
- **Figure Type 분류**: FigureSeer classifier (Siegel et al., 2016)로 7가지 유형 분류 -- graph plot(19.2%), table(23.6%), flowchart(8.5%), equation(5.9%), bar chart(4.7%), scatter plot(2.0%), other(36.1%)
- **Subfigure 제거**: Rule-based 패턴 매칭 + FigureSeparator CNN 모델 조합으로 compound figure 필터링 (precision 0.98)
- **텍스트 정규화**: NLTK 기반 토큰화, 소문자 변환, figure 번호 제거, 수치/수식/괄호 치환 ([NUM], [EQUATION], [BRACKET])
- **캡션 선택 전략**: First Sentence (133,543), Single-Sentence (94,110), <=100 Words (131,319) 3가지 컬렉션
- **Baseline 모델**: Pre-trained ResNet-101 encoder + LSTM decoder (hidden size 512) + global attention. Adam optimizer, dropout 0.5, learning rate 4e-4
- **평가**: BLEU-4 metric, 80/10/10 train/val/test split

## Originality

- **실세계 대규모 데이터셋**: 합성 figure에 의존하던 기존 연구와 달리, 실제 과학 논문에서 추출한 200만 개 이상의 figure-caption 쌍을 최초로 대규모 구축
- **체계적 전처리 파이프라인**: Figure type 분류, subfigure 감지, 텍스트 정규화, 캡션 선택의 multi-step 파이프라인을 설계하여 과학 figure 데이터셋 구축의 방법론적 표준을 제시
- **Graph plot 특화 접근**: 전체 figure 유형을 한꺼번에 다루는 대신, 가장 빈도 높고 분류 정확도가 높은 graph plot에 집중하는 실용적 전략
- **Multi-modal feature 실험**: 시각 정보(Vision), figure 내부 텍스트(Text), 결합(Vision+Text)의 상대적 기여를 체계적으로 비교

## Limitation & Further Study

### 저자들이 언급한 한계

- BLEU-4 점수가 0.02~0.03으로 매우 낮아, 과학 figure captioning이 아직 초기 단계임을 시사
- 텍스트 정규화가 BLEU-4 향상에 명확한 이점을 보이지 않음
- Vision+Text 결합이 단일 모달리티보다 오히려 성능이 낮아, 효과적인 multi-modal fusion 방법이 필요

### 자체판단 아쉬운 점

- Graph plot에만 한정하여 bar chart, scatter plot, flowchart 등 다른 figure 유형에 대한 일반화 가능성이 검증되지 않음
- BLEU-4만을 평가 지표로 사용하여, 생성된 캡션의 정보성(informativeness)이나 정확성(factual accuracy)을 측정하지 못함
- 논문의 본문 텍스트 맥락을 활용하지 않아, figure가 논문 내에서 어떤 역할을 하는지에 대한 contextual understanding이 결여
- 2021년 기준 CNN+LSTM baseline만 사용하여, 당시 이미 강력했던 Transformer 기반 모델(ViT, GPT-2 등)과의 비교가 부재
- Human evaluation이 데이터셋 품질 검증에만 사용되고, 생성된 캡션의 품질에 대한 인간 평가가 없음

### 후속 연구

- Pre-trained language model(SciBERT 등)과 vision-language model을 활용한 성능 개선
- 논문 본문 텍스트를 추가 context로 활용하는 document-aware captioning
- Graph plot 외 다른 figure 유형으로의 확장
- Figure captioning의 factual accuracy 평가를 위한 새로운 metric 개발
- Large multimodal model(GPT-4V 등)의 등장으로 인한 zero-shot 과학 figure captioning 가능성 탐구

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 3/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: SciCap은 과학 figure captioning이라는 중요한 문제를 정의하고, 최초의 대규모 실세계 데이터셋을 구축한 데 의의가 있다. 데이터 수집 및 전처리 파이프라인이 체계적이고 재현 가능하며, 합성 데이터와 실세계 데이터 간의 근본적 차이를 명확히 드러냈다. 다만, baseline 모델의 성능이 매우 낮고 모델링 측면의 기여가 제한적이어서, 데이터셋 논문으로서의 가치가 모델링 논문으로서의 가치보다 훨씬 크다. 이후 multimodal LLM 시대에 이 데이터셋이 벤치마크로 활용될 잠재력은 높다.
