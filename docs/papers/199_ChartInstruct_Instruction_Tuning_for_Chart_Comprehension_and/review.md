---
title: "199_ChartInstruct_Instruction_Tuning_for_Chart_Comprehension_and"
authors:
  - "Ahmed Masry"
  - "Mehrad Shahmohammadi"
  - "Md Rizwan Parvez"
  - "Enamul Hoque"
  - "Shafiq Joty"
date: "2024.03"
doi: "10.48550/arXiv.2403.09028"
arxiv: ""
score: 4.25
essence: "본 논문은 차트 이해와 추론을 위한 대규모 지시문 튜닝 데이터셋(191K 지시문, 71K 차트)을 제시하고, 차트 특화 비전-언어 모델(VLM)의 일반화 능력을 대폭 향상시키는 두 가지 시스템을 제안한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Cognitive_LLM_Evaluation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Masry et al._2024_ChartInstruct Instruction Tuning for Chart Comprehension and Reasoning 1.pdf"
---

# ChartInstruct: Instruction Tuning for Chart Comprehension and Reasoning

> **저자**: Ahmed Masry, Mehrad Shahmohammadi, Md Rizwan Parvez, Enamul Hoque, Shafiq Joty | **날짜**: 2024-03-14 | **DOI**: [10.48550/arXiv.2403.09028](https://doi.org/10.48550/arXiv.2403.09028)

---

## Essence

![Figure 1](figures/fig1.webp)
*다양한 차트 관련 작업 예시: 요약, 질문-답변, 팩트 체킹, 추론, 코딩 능력 등을 포함한 8가지 유형의 지시문 튜닝 작업*

본 논문은 차트 이해와 추론을 위한 대규모 지시문 튜닝 데이터셋(191K 지시문, 71K 차트)을 제시하고, 차트 특화 비전-언어 모델(VLM)의 일반화 능력을 대폭 향상시키는 두 가지 시스템을 제안한다.

## Motivation

- **Known**: 기존 차트 분석 모델은 차트 질문-답변, 요약, 팩트 체킹 등 특정 작업에만 최적화되어 있으며, 일반 비전-언어 모델(CLIP 기반)을 미세조정한 방식은 차트의 구조적 특성(축, 범례, 막대 등의 관계)을 제대로 모델링하지 못함

- **Gap**: 기존 지시문 튜닝 연구는 LLM(InstructGPT, FLAN-T5 등)에 집중되어 있으며, 차트 도메인에서의 지시문 튜닝은 충분히 탐색되지 않았음. 동시 연구들도 합성 차트나 제한된 실제 차트만 사용하고 좁은 범위의 작업만 다룸

- **Why**: 실제 응용을 위해서는 다양한 소스의 실제 차트(157개 온라인 플랫폼)와 광범위한 작업 유형이 필요하며, 차트 특화 비전 인코더와 체계적인 접근이 필수적

- **Approach**: (1) 157개 온라인 플랫폼에서 수집한 71K 개의 다양한 실제 차트, (2) GPT-3.5/4와 Gemini를 활용한 191K 지시문 자동 생성, (3) 차트 특화 비전 인코더(UniChart)를 통합한 두 가지 VLM 아키텍처 개발

## Achievement

![Figure 2](figures/fig2.webp)
*지시문 튜닝 파이프라인: WebCharts 수집, 자동 데이터 테이블 추출, 다양한 작업별 지시문 생성 과정*

1. **새로운 벤치마크 성능 달성**: ChartQA, Chart2Text, OpenCQA, ChartFC 등 4개 벤치마크에서 최고 성능(SOTA) 달성. UniChart 비전 인코더를 LLaVA 아키텍처에 통합하여 기존 CLIP 기반 모델 대비 성능 향상

2. **광범위한 작업 다양성**: 191K 지시문이 6가지 작업 카테고리(CoT 추론 14.3%, 요약 28.24%, 팩트 체킹 12.67%, 개방형 QA 22.26%, 코딩 10.26%, 신규 작업 12.27%)를 균형있게 커버하여 미학습 작업에 대한 일반화 능력 증명

3. **두 가지 실용적 시스템**: 
   - 엔드-투-엔드 모델: Llama2-7B/Flan-T5-XL + UniChart 인코더
   - 파이프라인 모델: 차트→데이터 테이블 추출 후 LLM 입력으로 해석 가능성 제공

## How

![Figure 3](figures/fig3.webp)
*지시문의 주요 동사(Root Verb) 분포: 다양한 작업 유형을 반영하는 언어적 다양성*

**데이터 구성**:
- UniChart 코퍼스 30K 차트 (기존 데이터셋)
- 신규 WebCharts 코퍼스 41K 차트 (웹 크롤링 + VIT 분류기 + 수동 정제)
- Gemini Pro Vision을 통한 자동 데이터 테이블 추출

**지시문 생성 전략**:
- **기존 작업 기반**: 차트 요약, 개방형 QA, 팩트 체킹, CoT 추론, 코드 생성
- **LLM 기반 신규 작업 발굴**: GPT-4를 활용하여 기존 9개 작업 유형 외 새로운 23,410개 지시문(신규 작업) 자동 생성
- **이중 아키텍처**:
  1. 엔드-투-엔드: Vision Encoder(UniChart) → Projection Layer → LLM (Llama2/Flan-T5)
  2. 파이프라인: Chart Image → Table Extraction Module → LLM

**평가**:
- 자동 평가: 기존 벤치마크 메트릭 (정확도, BLEU, ROUGE 등)
- 인간 평가: 신규 작업 성능 및 실제 시나리오 적용성 검증

## Originality

- **차트 특화 대규모 지시문 튜닝 데이터셋**: 157개 온라인 플랫폼의 실제 차트 71K개와 191K 다중 작업 지시문으로 기존 합성/제한 데이터셋 대비 규모와 다양성 획기적 증대

- **LLM 기반 신규 작업 발굴**: 기존 작업뿐 아니라 GPT-4가 제안한 새로운 차트 추론 작업 자동 생성으로 작업 다양성 확대 (12.27% 신규 작업)

- **차트 특화 비전 인코더 통합**: UniChart 사전학습 인코더를 VLM에 통합하여 자연 이미지 기반 CLIP 대비 차트 구조 이해도 개선

- **이중 시스템 설계**: 엔드-투-엔드와 파이프라인 방식으로 성능-해석 가능성 트레이드오프를 사용자 필요에 맞춰 선택 가능하게 함

- **공개 자원 제공**: 코드와 데이터셋 공개로 재현성 및 후속 연구 촉진

## Limitation & Further Study

- **데이터 추출의 한계**: WebCharts의 데이터 테이블을 Gemini 비전 모델로 자동 추출하므로 추출 오류가 누적될 수 있으며, 추출 정확도에 대한 정량적 분석 부재

- **모델 크기 제약**: 실험 모델이 Llama2-7B, Flan-T5-XL 등 상대적 소형 모델로 제한되어 있어, 최신 대형 모델(LLaMA-2-70B, GPT-4V 등)과의 성능 비교 필요

- **차트 유형의 편향성**: 웹 크롤링 기반 수집으로 인기 있는 차트 유형(막대, 선 그래프)에 편중되었을 가능성이 있으며, 복잡한 차트(히트맵, 산점도 행렬 등) 커버리지 부족

- **신규 작업의 타당성**: LLM이 생성한 신규 작업 12.27%에 대해 작업의 의미있음과 실제 유용성에 대한 충분한 인간 평가 부족

- **도메인 적응성 미흡**: 특정 도메인(의료, 금융 등)의 전문 차트에 대한 세부 평가 없음

**후속 연구 방향**:
- 더 큰 규모의 기초 모델 통합 및 멀티모달 학습 강화
- 차트 유형별 성능 분석 및 장시간 문맥 이해 확장
- 다국어 차트 데이터셋 구축을 통한 언어별 일반화


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.25/5

**총평**: 본 논문은 차트 도메인에서 처음으로 대규모 지시문 튜닝 데이터셋을 구축하고 차트 특화 VLM을 개발하여 차트 이해의 일반화 능력을 획기적으로 향상시켰다는 점에서 중요한 기여를 하였으나, 자동 데이터 추출 오류, 제한된 모델 크기, 신규 작업 타당성 검증 부족 등이 개선할 점으로 남아 있다.

## Related Papers

- 🔗 후속 연구: [[papers/315_Enhancing_chart-to-code_generation_in_multimodal_large_langu/review]] — 차트 이해에서 코드 생성으로의 자연스러운 발전 단계
- 🏛 기반 연구: [[papers/551_MMC_Advancing_Multimodal_Chart_Understanding_with_Large-scal/review]] — 대규모 차트 데이터셋이 차트 이해 모델 훈련의 기반이 됨
- 🏛 기반 연구: [[papers/315_Enhancing_chart-to-code_generation_in_multimodal_large_langu/review]] — 차트 이해 능력이 차트-투-코드 생성의 전제 조건이 됨
- 🏛 기반 연구: [[papers/566_Multimodal_deepresearcher_Generating_text-chart_interleaved/review]] — 차트 이해와 생성을 위한 인스트럭션 튜닝은 멀티모달 보고서 생성에서 FDV 표현의 기반 기술입니다
- 🔄 다른 접근: [[papers/200_Chartist_Task-driven_Eye_Movement_Control_for_Chart_Reading/review]] — 차트 읽기 시선 제어 vs 차트 이해 지시 튜닝의 서로 다른 차트 AI 접근법
- 🔗 후속 연구: [[papers/783_Synchart_Synthesizing_charts_from_language_models/review]] — 차트 이해 및 추론을 위한 지시 튜닝 방법론이 SynChart 데이터셋으로 학습된 모델의 성능 향상에 활용될 수 있다.
