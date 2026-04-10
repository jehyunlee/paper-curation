---
title: "783_Synchart_Synthesizing_charts_from_language_models"
authors:
  - "Mengchen Liu"
  - "Qixiu Li"
  - "Dongdong Chen"
  - "Dong Chen"
  - "Jianmin Bao"
date: "2024"
doi: "미공개"
arxiv: ""
score: 4.0
essence: "LLM(Large Language Model)만을 활용하여 약 400만 개의 다양한 차트 이미지와 7,500만 개 이상의 밀집 주석(데이터 테이블, 코드, 설명, QA)으로 구성된 대규모 합성 차트 데이터셋 SynChart를 구축하고, 이를 통해 4.2B 매개변수의 차트 전문가 모델을 학습하여 ChartQA 벤치마크에서 GPT-4O에 근접하면서도 GPT-4V를 능가하는 성능을 달성했다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Scientific_Graphics_Evaluation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liu et al._2024_Synchart Synthesizing charts from language models.pdf"
---

# Synchart: Synthesizing charts from language models

> **저자**: Mengchen Liu, Qixiu Li, Dongdong Chen, Dong Chen, Jianmin Bao, Yunsheng Li | **날짜**: 2024 | **DOI**: [미공개](https://doi.org/)

---

## Essence

![Figure 2](figures/fig2.webp)
*Data generation pipeline: Stage 1 데이터 생성, Stage 2 차트 생성, Stage 3 QA 쌍 생성*

LLM(Large Language Model)만을 활용하여 약 400만 개의 다양한 차트 이미지와 7,500만 개 이상의 밀집 주석(데이터 테이블, 코드, 설명, QA)으로 구성된 대규모 합성 차트 데이터셋 SynChart를 구축하고, 이를 통해 4.2B 매개변수의 차트 전문가 모델을 학습하여 ChartQA 벤치마크에서 GPT-4O에 근접하면서도 GPT-4V를 능가하는 성능을 달성했다.

## Motivation

- **Known**: GPT-4V(O) 같은 대형 멀티모달 모델이 뛰어난 성능을 보이고 있으며, 이를 위한 의사 라벨(pseudo label) 생성이 대중화되고 있음. 다만 이러한 모델의 기반이 되는 LLM에서 출발하여 멀티모달 능력을 갖춘 모델로 발전시키는 과정은 여전히 불명확함.

- **Gap**: 제한된 예산 내에서 LLM만을 활용하여 경쟁력 있는 멀티모달 모델을 구축할 수 있는지, 특히 도메인 특화(차트 이해) 관점에서 검증할 방법이 부족함. 데이터 수집 방식 간 질-량(quality-quantity) 트레이드오프에 대한 체계적 분석이 없음.

- **Why**: 차트 데이터는 (1) 인터넷에서 수집 가능한 차트의 수가 제한적(100만 미만)이고, (2) 웹상의 텍스트 라벨과 차트 간 연관성이 약하며(50% 미만 토큰 레벨 관련성), (3) 합성 데이터는 높은 라벨 품질을 보장하면서도 확장 가능하다는 점에서 LLM 기반 합성이 효과적임.

- **Approach**: 
  1. 데이터 수집 방식 비교 분석 (웹 수집 vs. 일반 이미지셋 필터링 vs. 코드 기반 합성)
  2. Stage별 LLM 활용 데이터 생성 파이프라인 설계:
     - Stage 1: 트렌드, 제약조건, 테마를 기반으로 다양한 데이터 테이블 생성
     - Stage 2: Matplotlib, Seaborn, Plotly, Bokeh 엔진 활용 차트 코드 생성 및 인간-루프 개선
     - Stage 3: 단순/복잡 질문-답변 쌍 생성

## Achievement

![Figure 1](figures/fig1.webp)
*ChartQA 정확도 비교: 다양한 모델과 성분의 기여도 시각화*

1. **대규모 데이터셋 구축**: 약 393만 개 차트 이미지 + 7,860만 개 설명, 4,580만 개 단순 QA, 1,390만 개 복잡 QA로 구성된 SynChart 완성. 기존 ChartLlama(11K)와 비교해 약 360배 규모 확대.

2. **강력한 모델 성능**: 
   - ChartQA 벤치마크에서 평균 84.6% 정확도 달성 (GPT-4O: 85.7%, GPT-4V: 78.5%)
   - 4.2B 소규모 모델로 70B+ 대규모 모델(Llama 3-V 70B: 83.2%, LLaVA OneVision-72B: 83.7%)을 능가
   - 기존 ChartLlama(7B)의 69.7% 대비 약 21% 상대 성능 향상

3. **확장성 검증**: 데이터 양 증가에 따라 성능이 지속적으로 개선되며 포화 징후가 없음(표 5). 공개 데이터 대비 1:6 비율(14배 훈련 비용)에서 83.2% 달성, 합성 데이터의 다양성 충분성 입증.

## How

![Figure 2](figures/fig2.webp)
*세 단계 데이터 생성 파이프라인의 상세 구성*

**Stage 1: 데이터 테이블 생성**
- 상위 9개 차트 유형 식별 (Obelics/ChartBench 샘플에서 모델 예측 + 인간 주석)
- LLM을 통해 74개 트렌드 생성 (9개 차트 유형별 다양한 데이터 추세 정의)
- 행/열 제약조건 수동 정제 (차트 유형별 데이터 구조 요구사항)
- StackExchange 105개 토픽 기반 약 1,262개 테마 생성 (현실성 보장)
- LLM이 테마+트렌드+제약조건 조합으로 다양한 데이터 테이블 생성

**Stage 2: 차트 생성**
- 4개 데이터 시각화 엔진 선택 (Matplotlib, Seaborn, Plotly, Bokeh):
  - LLM 코드 생성 능력 우수성
  - 다양한 차트 유형 지원 범위
- LLM이 데이터 테이블 → Python 코드 스니펫 생성
- 인간-루프 반복 개선:
  - 초기 성공률 64.0% → 개선 후 76.8% (Matplotlib 기준)
  - 약 600K 추가 차트 이미지 확보

**Stage 3: 질문-답변 쌍 생성**
- 단순 QA: 한 단어/구 답변 필요 (예: "가장 높은 값은?")
- 복잡 QA: 추론 과정 포함 (예: "어느 기간에 가장 큰 증가를 보였나?")
- 각 차트마다 여러 QA 쌍 생성으로 밀집 주석(dense annotations) 실현

**훈련 파이프라인**
- 베이스 모델: Phi-3.5-mini-instruct (3.8B LLM) + CLIP ViT-L/14 (0.3B 비전 인코더)
- 프리트레이닝: 코드, 데이터 테이블, 설명 활용
- 포스트트레이닝: QA 쌍 + 공개 데이터셋 활용
- 입력 이미지 해상도: 1344×1344 픽셀

## Originality

- **체계적 데이터 수집 방식 분석**: 웹 수집(품질 높음, 규모 작음: K-M), 일반 이미지셋 필터링(규모 중간, 라벨 품질 중간: M-B), 합성 데이터(규모 큼, 라벨 품질 높음: M-B) 간 명확한 트레이드오프 제시 및 정량적 평가(웹상 관련성 50% 미만 제시).

- **포괄적 LLM 기반 파이프라인**: 단순 코드 생성(ChartLlama)을 넘어 데이터 테이블 다양성 확보(트렌드 74개, 테마 1,262개), 현실성 보장(StackExchange 기반), 인간-루프 개선 메커니즘 통합으로 처음부터 끝까지 LLM 활용.

- **규모의 비약**: 기존 11K → 393만 개(약 360배), 밀집 주석으로 75M+ 어노테이션 제공. 소규모 모델(4.2B)로 대규모 모델 능가하는 효율성 시연.

- **확장성 검증 및 포화 분석**: 합성 데이터 특유의 "빠른 포화" 우려를 배제하고, 14배 훈련 비용까지 지속적 성능 향상을 실증적으로 보여줌 (표 5).

## Limitation & Further Study

- **도메인 특화의 한계**: 차트 이해에만 집중하여 일반 멀티모달 능력으로의 확대 가능성 미검증. 다른 시각 영역(문서, 사진, 다이어그램 등)으로 방법론 전이 방안 필요.

- **LLM 의존성**: 모든 단계에서 LLM(Phi-3.5 또는 GPT-4)에 의존하므로, LLM의 성능 한계(예: 복잡한 데이터 구조 생성 오류)가 최종 데이터셋 품질을 제한함. LLM 의존 완화 방안 모색 필요.

- **차트 유형 커버리지**: 상위 9개 차트 유형에 집중했으나, 희귀 또는 전문 차트(sunburst, sankey, heatmap 등)에 대한 커버리지 부족. 더 다양한 차트 유형 추가 가능성 미탐색.

- **평가 벤치마크 제한**: ChartQA 벤치마크만 주요 평가 대상. 다른 차트 이해 작업(차트 캡셔닝, 정보 추출, 시각적 질문 응답) 에 대한 검증 부족.

- **계산 효율성 미분석**: 데이터 생성 파이프라인의 총 LLM API 호출 비용, 인간-루프 개선의 인력 비용 등 경제적 효율성 미제시.

- **후속 연구 방향**:
  - 생성된 차트의 시각적 다양성(색상, 스타일, 레이아웃) 강화
  - 자동 평가 메트릭(생성 차트와 실제 데이터 정확도 검증) 개발
  - 타 도메인(의료, 과학, 금융) 특화 데이터셋으로 확대 적용


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4/5

**총평**: SynChart는 LLM을 활용한 대규모 합성 데이터 구축의 실제 성공 사례로, 데이터 수집 방식에 대한 명

## Related Papers

- 🔄 다른 접근: [[papers/315_Enhancing_chart-to-code_generation_in_multimodal_large_langu/review]] — 둘 다 차트 생성 및 이해를 다루지만 하나는 LLM 기반 합성 데이터셋 구축에, 다른 하나는 멀티모달 LLM의 차트-투-코드 생성 향상에 초점을 맞춘다.
- 🔗 후속 연구: [[papers/199_ChartInstruct_Instruction_Tuning_for_Chart_Comprehension_and/review]] — 차트 이해 및 추론을 위한 지시 튜닝 방법론이 SynChart 데이터셋으로 학습된 모델의 성능 향상에 활용될 수 있다.
- 🏛 기반 연구: [[papers/657_Reading_and_Reasoning_over_Chart_Images_for_Evidence-based_A/review]] — 차트 이미지 읽기 및 추론을 위한 증거 기반 답변 생성 기법이 SynChart의 QA 주석 생성에 이론적 기반을 제공한다.
- 🔄 다른 접근: [[papers/201_ChartLlama_A_Multimodal_LLM_for_Chart_Understanding_and_Gene/review]] — 전문 차트 이해 모델과 언어모델을 통한 차트 합성이 차트 처리의 해석과 생성 측면에서 상호 보완적 접근법을 제시한다
- 🔄 다른 접근: [[papers/129_Automatikz_Text-guided_synthesis_of_scientific_vector_graphi/review]] — Synchart가 차트 합성에 특화된 반면 AutomaTikZ는 과학 벡터 그래픽 전반을 다룸
- 🔗 후속 연구: [[papers/708_SciCap_Generating_Captions_for_Scientific_Figures/review]] — LLM을 활용한 합성 차트 데이터셋이 SciCap의 실제 과학 도형 캡션 생성 연구를 보완하고 확장한다.
