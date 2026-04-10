---
title: "198_ChartGemma_Visual_Instruction-tuning_for_Chart_Reasoning_in"
authors:
  - "Ahmed Masry"
  - "Megh Thakkar"
  - "Aayush Bajaj"
  - "Aaryaman Kartha"
  - "Enamul Hoque"
date: "2024"
doi: "10.48550/ARXIV.2407.04172"
arxiv: ""
score: 4.6
essence: "차트 이미지에서 직접 생성한 시각적 명령어 데이터로 학습한 멀티모달 모델로, 기존 데이터 테이블 의존성을 제거하고 강력한 비전-언어 백본(PaliGemma)을 활용하여 실제 차트 이해와 추론에서 최고 성능을 달성했다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Scientific_Literature_Analysis"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Masry et al._2024_ChartGemma Visual Instruction-tuning for Chart Reasoning in the Wild.pdf"
---

# ChartGemma: Visual Instruction-tuning for Chart Reasoning in the Wild

> **저자**: Ahmed Masry, Megh Thakkar, Aayush Bajaj, Aaryaman Kartha, Enamul Hoque, Shafiq Joty | **날짜**: 2024 | **DOI**: [10.48550/ARXIV.2407.04172](https://doi.org/10.48550/ARXIV.2407.04172)

---

## Essence

차트 이미지에서 직접 생성한 시각적 명령어 데이터로 학습한 멀티모달 모델로, 기존 데이터 테이블 의존성을 제거하고 강력한 비전-언어 백본(PaliGemma)을 활용하여 실제 차트 이해와 추론에서 최고 성능을 달성했다.

## Motivation

- **Known**: 비전-언어 모델(VLM)은 일반적인 이미지 이해 작업에서 탁월하나, 차트와 같은 특화된 시각화 이해에서는 성능이 제한적이다. 기존 차트 이해 모델들은 명령어 튜닝(instruction-tuning) 기반으로 개선되고 있다.

- **Gap**: 기존 방법들의 두 가지 심각한 문제점: (1) 차트의 기본 데이터 테이블로부터 학습 데이터를 생성하여 시각적 트렌드와 패턴을 무시하며, 테이블 추출 오류가 누적됨 (2) 약한 정렬(weak alignment)을 가진 비전-언어 백본(예: LLaVA)을 사용하여 실제 복잡한 차트에 대한 일반화 능력이 부족함.

- **Why**: 실제 세계의 복잡한 차트들(특히 메타데이터가 없는)을 이해하기 위해서는 차트 이미지의 모든 시각적 특성을 직접 포착해야 하며, 더 강력하게 정렬된 모델 백본이 필요하다.

- **Approach**: 차트 이미지에서 직접 명령어-튜닝 데이터를 생성하고, 더 강력한 백본인 PaliGemma(대규모 정렬 데이터로 사전 학습됨)를 기반으로 구축한 ChartGemma 모델을 제안한다.

## Achievement

![Figure 1](https://arxiv.org/html/2407.04172v2/x1.png)
*Figure 1: 명령어-튜닝 데이터 생성 과정. 차트 이미지를 Gemini Flash 1.5에 입력하여 ChartGemma 미세조정에 사용할 시각적 차트 명령어 생성*

1. **벤치마크 성과**: 차트 요약, 질문 응답, 사실 검증을 아우르는 5개 벤치마크에서 최고 수준의 결과 달성. 기존 모델들(예: UniChart, ChartQA 기반 모델)을 능가함.

2. **정성적 우수성**: 실제 복잡한 차트에 대한 인간 평가 및 GPT-4 평가에서 다른 방법들보다 더 현실적이고 사실에 기반한 요약 생성 확인(Table 1의 사례 참고).

3. **효율성**: 기존 차트 특화 모델들과 비교하여 훨씬 더 작은 모델 크기로 우수한 성능 달성, 실제 응용에 더 적합함.

## How

![Table 1 (개념적 설명)](https://arxiv.org/html/2407.04172v2/x2.png)
*Table 1: 동일한 LLM(Gemini Flash 1.5)이 데이터 테이블 vs. 차트 이미지에서 생성한 요약의 차이로, 시각적 속성 이해의 중요성을 강조*

**방법론**:

- **다양한 차트 말뭉치 구축**: 합성 차트(PlotQA), 큐레이션된 차트(Statista), 웹 수집 차트(WebCharts)에서 총 122,857개 차트 이미지 수집

- **시각적 명령어 데이터 생성**: Gemini Flash 1.5를 사용하여 차트 이미지에서 직접 다음 유형의 명령어 생성:
  - Chain-of-Thought(CoT): 복잡한 추론 질문으로 단계적 문제 해결 능력 강화
  - 요약(Summarization): 차트의 핵심 인사이트와 트렌드 포착
  - 사실 검증(Fact Checking): 진술이 차트 데이터로 지지되는지 확인
  - Chart-to-Markdown: 차트에서 마크다운 형식의 데이터 테이블 생성
  - Program Aided Design: 계산 작업 수행 코드 생성

- **개방형 작업**: 실제 시나리오의 다양한 작업 추가로 일반화 성능 향상

- **강력한 백본 활용**: PaliGemma(SigLIP 비전 인코더 + Gemma 언어 모델)의 강한 비전-언어 정렬 특성 활용

## Originality

- **차트 이미지 직접 기반 학습**: 기존의 데이터 테이블 의존성을 완전히 제거하고 차트 이미지에서 직접 명령어 데이터 생성하는 최초의 접근법

- **강한 정렬 백본 선택**: PaliGemma의 대규모 사전 정렬을 활용하여 약한 정렬의 한계 극복

- **포괄적 평가 패러다임**: 정량 평가(5개 벤치마크)와 정성 평가(인간 평가, GPT-4 평가)를 결합한 철저한 검증

- **재현성과 재사용성**: 코드, 모델 체크포인트, 데이터셋, 데모 공개로 후속 연구 촉진

## Limitation & Further Study

- **LLM 의존성**: 명령어 데이터 생성이 Gemini Flash 1.5에 의존하여, 생성 품질이 기저 모델의 성능에 영향받음. 다양한 LLM으로 생성된 데이터의 효과 비교 연구 필요

- **시각적 특성 균형**: 개별 데이터 포인트와 일반적 트렌드 간의 학습 균형에 대한 더 깊은 분석 필요

- **도메인 특화 차트**: 의료, 금융 등 특정 도메인의 고도로 특화된 차트에 대한 성능 평가 부족

- **후속 방향**: (1) 다중 LLM으로부터의 명령어 생성 비교, (2) 도메인 특화 미세조정 연구, (3) 실시간 차트 생성 및 수정 작업 확대


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.5/5
- Significance: 4.8/5
- Clarity: 4.5/5
- Overall: 4.6/5

**총평**: ChartGemma는 차트 이해 문제의 핵심인 시각적 정보 포착과 강한 모델 정렬에 효과적으로 대응하며, 기존 데이터 테이블 의존 방식의 한계를 극복한 실용적이고 우수한 연구로, 재현성 공개를 통해 학계에 의미 있는 기여를 한다.

## Related Papers

- 🏛 기반 연구: [[papers/315_Enhancing_chart-to-code_generation_in_multimodal_large_langu/review]] — 차트 이해 성능 향상 방법론이 차트 이미지 추론의 기반을 제공합니다.
- 🔄 다른 접근: [[papers/196_ChartAssisstant_A_Universal_Chart_Multimodal_Language_Model/review]] — 차트 이해를 위한 서로 다른 멀티모달 접근법을 제시합니다.
- 🔗 후속 연구: [[papers/204_Chartx__chartvlm_A_versatile_benchmark_and_foundation_model/review]] — ChartGemma의 차트 추론 능력이 더 포괄적인 차트 벤치마크로 확장됩니다.
- 🧪 응용 사례: [[papers/323_Every_part_matters_Integrity_verification_of_scientific_figu/review]] — 과학 그림의 무결성 검증이 차트 추론 능력에 적용됩니다.
- 🏛 기반 연구: [[papers/437_Interpreting_Multi-band_Galaxy_Observations_with_Large_Langu/review]] — 차트 추론을 위한 시각적 instruction-tuning 연구는 분광에너지분포 차트 해석에 필요한 시각적 추론 능력의 기초가 된다.
