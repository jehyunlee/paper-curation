---
title: "399_Helm_Highlighted_evidence_augmented_language_model_for_enhan"
authors:
  - "Junyi Bian"
  - "Xiaolei Qin"
  - "Wuhe Zhou"
  - "Mengzuo Huang"
  - "Congyi Luo"
date: "2023"
doi: "arXiv:2311.08896"
arxiv: ""
score: 4.0
essence: "표-텍스트 생성 작업에서 입력 테이블의 관련 행(row)을 먼저 강조(highlighting)하는 두 단계 접근 방식을 제안하여, 대규모 언어모델(LLM)이 핵심 증거에 집중하도록 함으로써 생성 품질을 향상시킨다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Table_Caption_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Oh et al._2023_Helm Highlighted evidence augmented language model for enhanced table-to-text generation.pdf"
---

# HeLM: Highlighted Evidence augmented Language Model for Enhanced Table-to-Text Generation

> **저자**: Junyi Bian, Xiaolei Qin, Wuhe Zhou, Mengzuo Huang, Congyi Luo, Ke Zhang, Weidong Zhang | **날짜**: 2023 | **DOI**: [arXiv:2311.08896](https://arxiv.org/abs/2311.08896)

---

## Essence

![Figure 1](figures/fig1.webp) *HeLM의 전체 프레임워크: 상단은 훈련 과정, 하단은 추론 과정을 보여줌*

표-텍스트 생성 작업에서 입력 테이블의 관련 행(row)을 먼저 강조(highlighting)하는 두 단계 접근 방식을 제안하여, 대규모 언어모델(LLM)이 핵심 증거에 집중하도록 함으로써 생성 품질을 향상시킨다.

## Motivation

- **Known**: 최근 LLM들은 표-텍스트 생성 작업에서 인상적인 성능을 보이고 있으며, 온라인 API 기반의 소수-샷 학습이나 맥락 내 학습 방식이 활용되고 있음
- **Gap**: 기존의 표 데이터 처리 방식은 전체 표를 문자열로 펼쳐서 입력하기 때문에, 모델이 질문 관련 정보에 효과적으로 집중하기 어려우며, API 방식은 데이터 유출 위험이 있음
- **Why**: 실제 입력 표는 매우 크지만 최종 출력에 필요한 정보는 소수의 행에만 포함되어 있으므로, 이러한 핵심 증거(evidence)를 식별하고 명시적으로 전달하면 모델 성능이 크게 향상될 수 있음
- **Approach**: 표 강조기(table highlighter)로 관련 행 인덱스를 식별하고, 강조된 표를 기반으로 표 요약기(table summarizer)가 최종 답변을 생성하는 두 단계 파이프라인 구성

## Achievement

![Figure 2](figures/fig2.webp) *강조기와 요약기의 프롬프트 구조*

1. **최첨단 성능**: FetaQA와 QTSumm 데이터셋에서 ROUGE와 BLEU 점수 기준 최첨단 결과 달성
2. **해석 가능성 제공**: 강조된 행 인덱스를 통해 모델의 의사결정 과정을 명확히 제시하여 해석 가능성(interpretability) 향상
3. **효율적 파인튜닝**: QLoRA를 활용한 매개변수 효율적 학습으로 제한된 계산 자원에서도 LLaMA2 파인튜닝 가능

## How

![Figure 3](figures/fig3.webp) *증거 레이블 증류를 위한 프롬프트*

![Figure 4](figures/fig4.webp) *표 강조 예시: 관련 행의 각 셀에 '*' 문자를 붙여 강조*

**방법론:**

- **두 단계 구조**:
  - 단계 1 (강조기): 입력 표 T와 질문 Q를 받아 관련 행 인덱스 E = {e₁, ...}를 생성
  - 단계 2 (요약기): 강조된 표 T*와 질문 Q를 받아 최종 답변 Ŷ 생성

- **강조 메커니즘**: HL(·) 함수를 통해 증거 인덱스로 식별된 행의 모든 셀에 '*' 문자 추가

- **증거 레이블 구성**:
  - **증거 피드백(Evidence Feedback)**: 피드백 모델 M_F가 각 증거의 품질을 평가(BLEU/ROUGE 점수로 리워드 계산)
  - **레이블 증류**: 더 강력한 LLM(GPT-4 등)으로부터 증거 레이블 추출
  - **그리디 검색**: 원본 입력-출력 데이터만으로 자동으로 증거 레이블 구성

- **명령어 튜닝(Instruction Tuning)**: 구조화된 프롬프트를 통해 LLM을 명령어 추종 형식으로 파인튜닝

## Originality

- 표-텍스트 생성에서 **명시적 증거 강조 단계를 독립적 모듈로 분리**하여 해석 가능성과 성능의 균형 달성
- **증거 레이블 구성의 이원적 접근**: 증류 기반 방법과 검색 기반 방법을 결합하여 주석 없는 데이터셋에서도 고품질 레이블 생성 가능
- 표 처리를 위한 **LLM 기반의 엔드-투-엔드 솔루션**으로, SQL 합성이나 추가 사전학습 없이 효율적 구현
- 매개변수 효율적 튜닝으로 개방형 LLM(LLaMA2)의 실용적 활용성 확대

## Limitation & Further Study

- **증거 피드백의 품질 의존성**: 피드백 모델의 성능에 따라 증거 라벨 품질이 영향을 받을 수 있으므로, 더 견고한 피드백 메커니즘 개발 필요
- **행 수준 증거의 한계**: 셀 단위(cell-level) 또는 다중 표 시나리오로의 확장 미흡
- **계산 비용**: 두 개의 LLM 순차 실행으로 인한 추론 시간 증가 문제 미해결
- **후속 연구 방향**:
  - 다중 테이블 및 계층적 구조를 가진 표에 대한 확장
  - 강조기와 요약기의 end-to-end 통합 학습
  - 다국어 표-텍스트 생성으로의 일반화

## Evaluation

- **Novelty**: 4/5 — 표 강조라는 명시적 중간 단계는 창의적이나, 각 개별 기술(증류, 검색, 명령어 튜닝)은 기존 기법의 조합
- **Technical Soundness**: 4/5 — 방법론이 타당하고 구현이 명확하나, 증거 피드백 메커니즘의 이론적 정당화 부족
- **Significance**: 4/5 — 실용적 성과(SOTA 달성)와 해석 가능성 제공으로 중요하나, 응용 범위가 표-텍스트 생성에 제한됨
- **Clarity**: 4/5 — 전체 구조와 프롬프트 설계가 명확하게 제시되었으나, 증거 레이블 병합 과정의 상세 기술 부족
- **Overall**: 4/5

**총평**: HeLM은 표-텍스트 생성에서 명시적 증거 강조를 통해 성능과 해석 가능성을 동시에 달성한 실용적이고 효과적인 접근법이며, 주석 없는 데이터셋에서도 적용 가능한 증거 라벨 구성 방법의 창의성이 돋보인다. 다만 개별 기술의 참신성과 이론적 깊이 측면에서는 보완의 여지가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/515_Machine-in-the-loop_rewriting_for_creative_image_captioning/review]] — 표 캡션 생성에서 기계-인-루프 접근법과 증거 강조 접근법의 비교 분석이 가능합니다.
- 🔗 후속 연구: [[papers/564_Multi-llm_collaborative_caption_generation_in_scientific_doc/review]] — 단일 LLM의 증거 강조 방식을 다중 LLM 협업으로 확장한 고도화된 접근법을 제시합니다.
- 🏛 기반 연구: [[papers/708_SciCap_Generating_Captions_for_Scientific_Figures/review]] — 과학적 도형 캡션 생성의 기본 방법론을 표 캡션 생성에 적용한 기초 연구입니다.
- 🔄 다른 접근: [[papers/515_Machine-in-the-loop_rewriting_for_creative_image_captioning/review]] — 창의적 캡션 작성에서 기계-인-루프 방식과 증거 강조 방식의 서로 다른 인간-AI 협업 접근법을 비교할 수 있습니다.
- 🔗 후속 연구: [[papers/564_Multi-llm_collaborative_caption_generation_in_scientific_doc/review]] — 단일 LLM의 증거 강조를 다중 LLM 협업으로 발전시켜 더 고품질의 과학 도형 캡션을 생성합니다.
