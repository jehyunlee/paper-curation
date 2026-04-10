---
title: "204_Chartx__chartvlm_A_versatile_benchmark_and_foundation_model"
authors:
  - "Renqiu Xia"
  - "Bo Zhang"
  - "Hancheng Ye"
  - "Xiangchao Yan"
  - "Qi Liu"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "본 논문은 다중모달 대형언어모델(MLLM)의 차트 이해 능력을 종합적으로 평가하기 위해 ChartX 벤치마크와 ChartVLM 기초모델을 제시한다. 특히 차트 데이터 추출과 복잡한 추론을 포함하는 다단계 작업에서 모델의 해석가능성을 강화하는 새로운 접근방식을 제안한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Multimodal_Scientific_Benchmarks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Xia et al._2024_Chartx & chartvlm A versatile benchmark and foundation model for complicated chart reasoning.pdf"
---

# Chartx & chartvlm: A versatile benchmark and foundation model for complicated chart reasoning

> **저자**: Renqiu Xia, Bo Zhang, Hancheng Ye, Xiangchao Yan, Qi Liu, Hongbin Zhou, Zijun Chen, Min Dou, Botian Shi, Junchi Yan, Yu Qiao | **날짜**: 2024 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: ChartX 평가 데이터셋과 ChartVLM 모델의 개요. ChartX는 22개 분야, 18개 차트 유형, 7개 작업을 포함하며, ChartVLM은 instruction adapter를 통해 작업을 동적으로 선택하고 인식 작업 결과를 추론 작업에 통합하여 해석가능성을 향상시킨다.*

본 논문은 다중모달 대형언어모델(MLLM)의 차트 이해 능력을 종합적으로 평가하기 위해 ChartX 벤치마크와 ChartVLM 기초모델을 제시한다. 특히 차트 데이터 추출과 복잡한 추론을 포함하는 다단계 작업에서 모델의 해석가능성을 강화하는 새로운 접근방식을 제안한다.

## Motivation

- **Known**: 최근 GPT-4V, Claude 등 다양한 MLLM이 일반적인 시각-언어 작업(VQA, 수학 추론 등)에서 우수한 성능을 보이고 있음
  
- **Gap**: 하지만 차트에서 수치 데이터를 추출하고 이를 기반으로 복잡한 논리 추론을 수행하는 능력은 아직 충분히 탐색되지 않음. 기존 차트 벤치마크는 차트 유형(3-10개)과 작업 범위(1-4개)가 제한적이며, 평가 지표도 일원화되어 있음

- **Why**: 차트는 데이터 분석, 과학 보고, 비즈니스 의사결정 등 다양한 분야에서 핵심 역할을 하므로, 차트 기반 추론 능력은 MLLM의 실용성을 판단하는 중요한 지표임

- **Approach**: (1) 18개 차트 유형, 22개 분야 주제, 7개 작업을 포함하는 고품질 48K 멀티모달 차트 데이터셋 ChartX 구축; (2) 인식 작업(perception tasks) 결과를 인지 작업(cognition tasks)에 통합하여 해석가능성을 강화하는 ChartVLM 개발

## Achievement

![Figure 4](figures/fig4.webp)
*Figure 4: ChartVLM의 아키텍처. 기본 디코더는 제목/유형/구조 추출(SE)을 담당하고, 보조 디코더는 instruction adapter를 통해 동적으로 QA, 설명, 요약, 코드 재생성 등의 작업을 선택 실행한다.*

1. **포괄적 벤치마크 구축**: 기존 벤치마크 대비 6배 이상의 차트 유형(18개 vs 3-10개)과 5배 이상의 분야 주제(22개)를 포함하는 ChartX 데이터셋 개발. EM, SCRM, GPT-accuracy, GPT-score 등 다층적 평가 지표 도입

2. **해석가능성 강화 모델**: 차트 구조 추출 → 데이터 기반 추론의 순차적 처리 파이프라인으로 각 단계의 근거를 명확하게 제시. Instruction adapter를 통한 동적 작업 선택으로 상호작용성 향상

3. **성능 우월성**: ChartVLM이 기존 차트 특화 모델들과 범용 MLLM(LLaVA, Qwen-VL 등)을 능가하며 GPT-4V와 유사 수준의 성능 달성

## How

![Figure 3](figures/fig3.webp)
*Figure 3: 차트 데이터 수집 및 품질 검증 파이프라인*

### ChartX 데이터셋 구축

- **차트 생성**: 22개 분야의 실제 데이터를 이용하여 18개 차트 유형별로 체계적 생성
- **멀티모달 구성**: 각 차트마다 이미지, CSV, Python 코드, 텍스트 설명 4가지 모달리티 포함
- **작업 분류**:
  - 인식 작업(3개): 차트 제목 추출, 차트 유형 분류, 구조 정보 추출
  - 인지 작업(4개): QA, 설명 생성, 요약, 코드 재생성
- **품질 관리**: 자동 생성 후 수동 검수를 통해 데이터 품질 보증

### ChartVLM 모델 구조

- **기본 구성**: Vision encoder(시각 특성 추출) + Vision-language connector(정렬) + Language model(언어 처리)
- **이중 디코더 구조**:
  - Base decoder: 차트 제목, 유형, 구조 추출(인식 작업) 담당
  - Auxiliary decoder: 사용자 지시에 따라 QA, 설명, 요약, 코드 재생성(인지 작업) 수행
- **Instruction adapter**: 사용자 입력으로부터 필요한 작업을 자동 인식하여 적절한 디코더 활성화
- **학습 전략**: ChartQA, Chart-to-text, PlotQA, SimChart9K 등 기존 오픈소스 데이터셋으로 학습하되, ChartX 데이터는 평가 용도로만 사용(데이터 누출 방지)

## Originality

- **차트 벤치마크의 획기적 확장**: 단순 차트 유형 확대를 넘어 학제 간 다양한 분야(상업, 산업, 사회, 문화, 생활) 주제 통합으로 실제 응용 시나리오 반영

- **해석가능성 중심의 아키텍처**: 기존 end-to-end 추론과 달리 구조적 정보 추출을 명시적 중간 단계로 삽입하여 모델 의사결정 과정을 추적 가능하게 설계

- **동적 작업 선택 메커니즘**: Instruction adapter를 통해 단일 모델이 7개 작업을 통합 처리하면서도 각 작업에 대한 최적화 유지

- **멀티모달 일관성**: 이미지, CSV, 코드, 텍스트를 모두 포함함으로써 다양한 다운스트림 응용(데이터 검증, 코드 생성, 자동 분석 등)에 활용 가능

## Limitation & Further Study

- **데이터 합성의 한계**: 차트 이미지를 프로그래매틱하게 생성하므로 복잡한 시각적 왜곡(회전, 부분 가림, 낮은 해상도 등) 시나리오 부족. 실제 출판된 과학 논문이나 보고서의 차트 포함 필요

- **평가 지표의 자동화 문제**: GPT-score 등 LLM 기반 평가 지표는 일관성 논쟁 가능성 있음. 더 엄밀한 자동 평가 메트릭(정보 추출 F1 등) 개발 필요

- **모델 확장성 미검증**: 현재 LLaMA 기반 언어 모델 사용으로, GPT-4V 같은 초대규모 모델과의 성능 격차 원인 분석 부족

- **도메인 특화 차트 부족**: 금융(캔들스틱), 의료, 기상 등 도메인 특화 차트가 상대적으로 적은 편. 분야별 차트 비중 재균형 필요

- **후속 연구**: (1) 실제 출판 자료에서 추출한 자연 차트 데이터 추가; (2) 멀티언어 차트 데이터셋 확장; (3) 약한 감독(weak supervision)을 이용한 자동 주석 생성 방법; (4) 차트 생성 역작업(text-to-chart) 통합

## Evaluation

- **Novelty (독창성)**: 4.5/5
  - 벤치마크의 규모와 다양성 측면에서 획기적이나, 개별 작업 정의는 기존 연구 활용
  
- **Technical Soundness (기술 타당성)**: 4/5
  - 아키텍처와 학습 전략은 합리적이나, 이중 디코더 구조의 필요성에 대한 ablation study 미흡
  
- **Significance (중요도)**: 4.5/5
  - 차트 이해 능력이 MLLM의 실무 응용을 좌우하는 핵심 요소임을 강력하게 입증. 데이터셋 공개로 커뮤니티 기여도 높음
  
- **Clarity (명확성)**: 4/5
  - 전체 구조와 목표는 명확하나, 데이터 생성 프로세스의 세부 알고리즘(OCR, 구조 추출 등) 설명 부족
  
- **Overall (종합)**: 4.2/5

**총평**: ChartX & ChartVLM은 차트 이해 벤치마킹과 모델 개발에 있어 중요한 이정표를 제시한다. 특히 해석가능성을 강조하는 설계 철학과 공개 데이터셋의 규모는 해당 분야의 향후 연구 방향을 형성할 가능성이 높다. 다만 실제 자연 차트 데이터 통합과 모델 스케일링 측면에서 추가 개선이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/197_Chartcoder_Advancing_multimodal_large_language_model_for_cha/review]] — 코드 생성에 특화된 ChartCoder와 달리 차트 이해 전반을 다루는 종합적 접근
- 🏛 기반 연구: [[papers/722_Scifibench_Benchmarking_large_multimodal_models_for_scientif/review]] — 과학 그림 해석 벤치마크 SciFIBench의 방법론을 차트 특화 영역에 적용한 기반
- 🔗 후속 연구: [[papers/196_ChartAssisstant_A_Universal_Chart_Multimodal_Language_Model/review]] — 범용 차트 언어모델 ChartAssistant의 성능을 더 체계적으로 평가하는 벤치마크
- 🧪 응용 사례: [[papers/315_Enhancing_chart-to-code_generation_in_multimodal_large_langu/review]] — 차트-코드 생성 성능 향상 연구에 활용할 수 있는 평가 기준 제공
- 🔗 후속 연구: [[papers/315_Enhancing_chart-to-code_generation_in_multimodal_large_langu/review]] — 차트 기반 모델이 코드 생성까지 확장된 종합적 프레임워크
- 🔗 후속 연구: [[papers/198_ChartGemma_Visual_Instruction-tuning_for_Chart_Reasoning_in/review]] — ChartGemma의 차트 추론 능력이 더 포괄적인 차트 벤치마크로 확장됩니다.
- 🔗 후속 연구: [[papers/551_MMC_Advancing_Multimodal_Chart_Understanding_with_Large-scal/review]] — ChartX & ChartVLM의 기초 모델을 대규모 명령어 튜닝으로 발전시킨 연구
- 🔄 다른 접근: [[papers/722_Scifibench_Benchmarking_large_multimodal_models_for_scientif/review]] — 차트 이해에 특화된 ChartX와 달리 전반적인 과학 논문 그림 해석 능력을 평가하는 포괄적 벤치마크
- 🔄 다른 접근: [[papers/197_Chartcoder_Advancing_multimodal_large_language_model_for_cha/review]] — 차트 이해와 추론에 중점을 둔 ChartX와 달리 차트-코드 변환이라는 구체적 작업에 특화
- 🔄 다른 접근: [[papers/196_ChartAssisstant_A_Universal_Chart_Multimodal_Language_Model/review]] — 차트 이해 벤치마크와 달리 다양한 차트 작업을 단일 모델로 처리하는 통합 접근
- 🏛 기반 연구: [[papers/709_SciCap_A_Knowledge_Augmented_Dataset_to_Study_the_Challenges/review]] — 다목적 차트 및 시각화 모델이 SciCap+의 과학 도형 이해에 필요한 기반 기술을 제공한다.
