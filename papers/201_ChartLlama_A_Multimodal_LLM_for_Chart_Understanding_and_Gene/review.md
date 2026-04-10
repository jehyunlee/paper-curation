---
title: "201_ChartLlama_A_Multimodal_LLM_for_Chart_Understanding_and_Gene"
authors:
  - "Yucheng Han"
  - "Chi Zhang"
  - "Xin Chen"
  - "Xu Yang"
  - "Zhibin Wang"
date: "2023"
doi: "10.48550/ARXIV.2311.16483"
arxiv: ""
score: 4.5
essence: "기존 멀티모달 대형언어모델(LLM)들이 일반적인 시각-언어 작업에서는 우수하나, 차트 해석 같은 특정 도메인 데이터 이해에는 크게 부족하다는 문제를 해결하기 위해, **GPT-4 기반의 자동화된 3단계 데이터 생성 파이프라인**을 제안하고, 이로부터 학습한 **ChartLlama**가 기존 벤치마크에서 최고 성능을 달성한 연구다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Visual_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Han et al._2023_ChartLlama A Multimodal LLM for Chart Understanding and Generation.pdf"
---

# ChartLlama: A Multimodal LLM for Chart Understanding and Generation

> **저자**: Yucheng Han, Chi Zhang, Xin Chen, Xu Yang, Zhibin Wang, Gang Yu, Bin Fu, Hanwang Zhang | **날짜**: 2023 | **DOI**: [10.48550/ARXIV.2311.16483](https://doi.org/10.48550/ARXIV.2311.16483)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: ChartLlama의 다양한 능력 시연. 제안된 데이터 생성 파이프라인을 기반으로 한 instruction-tuning 데이터셋을 구축하고, 이를 통해 차트 이해 및 생성 능력 획득*

기존 멀티모달 대형언어모델(LLM)들이 일반적인 시각-언어 작업에서는 우수하나, 차트 해석 같은 특정 도메인 데이터 이해에는 크게 부족하다는 문제를 해결하기 위해, **GPT-4 기반의 자동화된 3단계 데이터 생성 파이프라인**을 제안하고, 이로부터 학습한 **ChartLlama**가 기존 벤치마크에서 최고 성능을 달성한 연구다.

## Motivation

- **Known**: LLaVA, MiniGPT 등의 선행 연구를 통해 시각 인코더와 instruction-tuning 데이터셋의 조합으로 멀티모달 LLM 구축이 가능함이 입증됨. COCO 같은 벤치마크 기반 데이터셋이 일반 사진 이해에서는 효과적이었음.

- **Gap**: 차트와 같은 특화된 시각 자료(specialized visual representations)에 대해서는 멀티모달 LLM의 능력이 현저히 부족함. 차트 데이터셋 구축의 주요 문제: (1) 웹 크롤링 의존으로 인한 낮은 품질과 불완전한 주석, (2) 차트 생성을 위한 코드 주석 부재로 인한 감독 학습의 어려움, (3) 다양한 차트 유형과 작업 범주 부족.

- **Why**: 차트는 학술 논문, 기업 프레젠테이션 등 현실에서 매우 중요한 정보 전달 매체이므로, 멀티모달 LLM의 차트 해석 능력 향상은 필수적.

- **Approach**: GPT-4의 강력한 자연언어처리 및 코딩 능력을 활용한 자동화된 데이터 생성 파이프라인으로 고품질의 다양한 instruction-tuning 데이터셋 구축.

## Achievement

![Figure 3](figures/fig3.webp)
*그림 3: 3단계 데이터 생성 방법론. 데이터 생성(Stage 1), 차트 그리기(Stage 2), Instruction 데이터 생성(Stage 3)으로 구성*

1. **고품질 데이터셋 생성**: GPT-4 기반 파이프라인을 통해 11K개 차트 이미지와 160K개 instruction-tuning 데이터를 생성. 기존 데이터셋 대비 더 다양한 차트 유형(10개)과 작업 유형(7개) 지원 (표 1 참조).

2. **우수한 벤치마크 성능**: ChartQA, Chart-to-text, Chart-extraction 등 기존 벤치마크에서 모든 선행 방법을 능가. 특히 훨씬 적은 학습 데이터(160K)로도 larger-scale datasets(PlotQA 28M 등)에서 학습한 모델을 초과.

3. **다중 차트 이해 및 생성 능력**: Q&A, 차트 설명(chart description), 데이터 추출(chart extraction), 차트-코드 변환(chart-to-chart), 텍스트-차트 생성(text-to-chart), 차트 편집(chart editing) 등 다양한 작업 수행 가능.

## How

![Figure 2](figures/fig2.webp)
*그림 2: 데이터셋 내 작업 유형(위)과 차트 유형(아래) 분포*

**3단계 데이터 생성 파이프라인**:

- **Stage 1 (Chart Data Generation)**: GPT-4에 주제, 데이터 분포, 추세 등의 특성을 지정하여 다양한 표 형식의 데이터 생성. 웹 크롤링 없이 합성 데이터를 유연하게 생성 가능.

- **Stage 2 (Chart Figure Generation)**: GPT-4의 코딩 능력을 활용하여 Stage 1의 데이터와 Matplotlib 등의 라이브러리 문서를 기반으로 차트 생성 코드(Python) 작성 및 실행. 정확하고 다양한 차트 이미지 획득.

- **Stage 3 (Instruction Tuning Data Generation)**: Stage 1, 2의 결과물(원본 데이터, 생성된 이미지, 코드)을 바탕으로 GPT-4가 차트 내용 해석, 관련 질문-답변 쌍 구성. 설명문, Q&A, 수정 코드 등을 포함한 종합적인 instruction-tuning 코퍼스 생성.

**모델 구축**: LLaVA-1.5를 기반으로 하여 생성된 데이터셋으로 fine-tuning. 비전 인코더와 LLM의 조합 구조 활용.

## Originality

- **자동화된 데이터 생성 파이프라인**: 수동 주석 작업을 최소화하면서도 고품질, 고다양성 데이터셋 구축. 기존의 웹 크롤링 기반 방식의 한계를 극복하는 혁신적 접근.

- **유연한 확장성**: 특정 특성(themes, trends, distributions) 지정으로 다양한 차트 유형과 작업 범주를 쉽게 추가 가능. 기존 데이터셋(3-6개 차트 유형, 1개 작업)과 달리 10개 차트 유형, 7개 작업 유형 지원.

- **GPT-4 기능의 효율적 활용**: LLM의 자연언어처리와 코드 생성 능력을 순차적으로 활용하는 체계적 파이프라인 설계.

- **종합적 차트 이해 및 생성**: 기존 연구가 주로 Q&A나 캡셔닝에 국한되었다면, 본 연구는 차트 de-rendering(코드 생성), 편집, 다중 차트 추론 등 포괄적 능력 제시.

## Limitation & Further Study

- **데이터셋 규모**: 160K instruction-tuning 데이터는 PlotQA(28M), Unichart(7M) 등 기존 대규모 데이터셋보다 훨씬 작음. 제한된 학습량으로도 성능이 나은 이유는 데이터 품질 때문으로 추정되나, 규모 증대의 효과는 검증 필요.

- **실제 차트 평가 부족**: 생성된 합성 차트로만 학습하여 실제 웹에서 수집된 차트나 스캔된 논문 차트에 대한 일반화 성능이 미흡할 가능성. 실제 데이터셋(ChartQA, PlotQA 등)에서의 평가는 진행했으나 Out-of-distribution 성능 검증 필요.

- **모델 크기 제약**: LLaVA-1.5 기반으로 진행되었으나, 더 큰 기반 LLM(GPT-4 규모)에 적용했을 때의 성능 개선 정도 미지수.

- **향후 연구 방향**: (1) 더 많은 차트 유형(산점도, 히트맵 등) 추가, (2) 다국어 데이터셋 확장, (3) 차트에서 발생하는 hallucination 완화, (4) 복잡한 분석 작업(추세 예측, 이상 탐지) 확대.


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.5/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.5/5

**총평**: 차트 이해에 특화된 멀티모달 LLM 개발이라는 명확한 목표 하에, GPT-4 기반의 체계적이고 유연한 데이터 생성 파이프라인을 제시하고, 이로부터 기존 벤치마크에서 우수한 성능을 달성한 의미 있는 연구다. 다만 합성 데이터 의존도, 실제 데이터 일반화, 규모 한계 등에 대한 추가 검증이 필요하며, 공개된 데이터셋과 모델이 차트 AI 연구 커뮤니티에 미칠 파급력은 클 것으로 예상된다.

## Related Papers

- 🔗 후속 연구: [[papers/551_MMC_Advancing_Multimodal_Chart_Understanding_with_Large-scal/review]] — 차트 이해와 생성에 특화된 멀티모달 LLM이 대규모 차트 데이터셋을 활용한 범용 차트 이해 모델로 발전했다
- 🧪 응용 사례: [[papers/722_Scifibench_Benchmarking_large_multimodal_models_for_scientif/review]] — 차트 이해 전용 멀티모달 모델의 방법론이 과학 그림 전반을 다루는 대형 멀티모달 모델 벤치마킹에 핵심적으로 적용된다
- 🔗 후속 연구: [[papers/315_Enhancing_chart-to-code_generation_in_multimodal_large_langu/review]] — 차트 해석과 생성 능력이 멀티모달 대형언어모델의 차트-코드 생성 성능 향상으로 직접 확장되었다
- 🔄 다른 접근: [[papers/783_Synchart_Synthesizing_charts_from_language_models/review]] — 전문 차트 이해 모델과 언어모델을 통한 차트 합성이 차트 처리의 해석과 생성 측면에서 상호 보완적 접근법을 제시한다
