---
title: "192_Cchall_A_novel_benchmark_for_joint_cross-lingual_and_cross-m"
authors:
  - "Yongheng Zhang"
  - "Xu Liu"
  - "Ruoxi Zhou"
  - "Qiguang Chen"
  - "Hao Fei"
date: "2025"
doi: "10.48550/arXiv.2505.19108"
arxiv: ""
score: 4.2
essence: "본 논문은 대규모 언어 모델(LLM)이 교차-언어 및 교차-모달 상황에서 동시에 겪는 환각(hallucination) 문제를 평가하기 위한 새로운 벤치마크 **CCHall(Cross-lingual and Cross-modal Hallucinations)**을 제시한다. 기존 연구가 단일 시나리오(교차-언어 또는 교차-모달)에만 집중한 반면, 이 연구는 두 문제가 결합된 실제 상황을 평가하는 최초의 종합 벤치마크를 개발했다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Cross-modal_Language_Detection"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhang et al._2025_Cchall A novel benchmark for joint cross-lingual and cross-modal hallucinations detection in large.pdf"
---

# Cchall: A novel benchmark for joint cross-lingual and cross-modal hallucinations detection in large language models

> **저자**: Yongheng Zhang, Xu Liu, Ruoxi Zhou, Qiguang Chen, Hao Fei, Wenpeng Lü, Libo Qin | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2505.19108](https://doi.org/10.48550/arXiv.2505.19108)

---

## Essence

![Figure 1](figure1.png)
*그림 1: (a) 교차-언어 환각(cross-lingual hallucination) - "stand"를 "站在"로 오역, (b) 교차-모달 환각(cross-modal hallucination) - 존재하지 않는 "bridge" 생성, (c) 교차-언어 및 교차-모달 환각의 결합*

본 논문은 대규모 언어 모델(LLM)이 교차-언어 및 교차-모달 상황에서 동시에 겪는 환각(hallucination) 문제를 평가하기 위한 새로운 벤치마크 **CCHall(Cross-lingual and Cross-modal Hallucinations)**을 제시한다. 기존 연구가 단일 시나리오(교차-언어 또는 교차-모달)에만 집중한 반면, 이 연구는 두 문제가 결합된 실제 상황을 평가하는 최초의 종합 벤치마크를 개발했다.

## Motivation

- **Known**: 기존 연구는 교차-언어 환각(cross-lingual hallucination, 예: mFACT, HalOmi)과 교차-모달 환각(cross-modal hallucination, 예: CHAIR, POPE, HallusionBench)을 개별적으로 평가해왔다. 각 분야에서 상당한 진전이 있었으나 두 문제가 결합된 상황에 대한 평가는 부재한다.

- **Gap**: 의료 진단, 이미지 캡셔닝, 음성-텍스트 변환 등 실제 응용 분야에서는 다중 언어 쿼리와 다중 모달 입력이 동시에 요구되나, 이러한 결합된 환각 현상에 대한 벤치마크와 평가 방법이 없다.

- **Why**: 교차-언어와 교차-모달 상황이 결합되면 언어 차이와 다중모달 입력으로 인한 환각이 증가하여 실제 배포에 심각한 문제를 초래한다. 그림 2(a)의 결과에 따르면 결합된 환각 인식 성능이 개별 문제보다 3.4~10.9 포인트 저하된다.

- **Approach**: VQA(Visual Question Answering)와 이미지 캡셔닝(Image Captioning) 태스크를 기반으로 원본 다중모달 데이터셋을 선택하고, 자동 필터링과 데이터 번역을 통해 체계적으로 교차-모달, 교차-언어, 결합된 환각 데이터셋을 구성한다.

## Achievement

![Figure 2](figure2.png)
*그림 2(a): 다양한 환각 유형에 대한 MLLM의 F1-점수 성능 분석, (b): 기존 벤치마크와 CCHall의 비교*

1. **최초의 결합 벤치마크 제시**: 교차-언어 및 교차-모달 환각을 동시에 평가하는 최초의 벤치마크 CCHall을 개발했으며, 기존 벤치마크(XL-Sum, CHAIR, POPE 등)는 한 가지 시나리오만 다룬다.

2. **포괄적 평가 결과**: InternVL2-8B(65.9%), Llama-3.2-11B-Vision(46.2%), Qwen2-VL-7B(38.7%) 등 다양한 규모의 모델을 평가하여, 현재 MLLM들이 결합된 환각에 여전히 어려움을 겪고 있음을 입증했다.

3. **완화 전략의 차별화된 효과성**: 소규모 모델(<12B)에는 기본 전략이, 대규모 모델에는 고급 전략(다중언어 문맥, 도구 보조)이 더 효과적임을 입증했다.

## How

![Figure 3](figure3.png)
*그림 3: CCHall 구성 과정 - (a) 원본 다중모달 데이터셋 선택, (b) 교차-모달 환각 데이터 구성, (c) 교차-언어 환각 데이터 구성, (d) 결합된 벤치마크*

- **데이터셋 선택 단계**: GQA, AMBER(VQA용 3,600개 이미지, 337개 객체 범주), XM3600, xFlickr&Co(이미지 캡셔닝용 다양한 문화권 이미지) 등을 통합 선택

- **자동 샘플 제거**: 이미지-텍스트 쌍 불일치, 고아(orphan) 데이터 등 비정상 데이터 자동 필터링으로 데이터 품질 보증

- **교차-모달 환각 데이터 구성**: 정확한 이미지-텍스트 쌍을 선정하고 교차-모달 환각을 자동 생성(오류 유형 정의 및 패턴 기반 생성)

- **교차-언어 환각 데이터 구성**: 영어 참조 답변을 자동 번역(중국어, 아랍어 등 다국어) 및 인간 재검증을 통해 구성

- **인간 재검증**: 자동 생성된 환각 샘플에 대한 다국어 주석자의 재검증으로 레이블 신뢰성 확보

## Originality

- **새로운 문제 정의**: 기존에 알려지지 않은 "교차-언어 및 교차-모달 결합 환각(Joint Cross-Lingual and Cross-Modal Hallucinations)" 문제를 최초로 정의하고 이론화했다(식 3 제시).

- **체계적 벤치마크 개발**: 세 가지 유형의 환각(교차-모달만, 교차-언어만, 결합)을 모두 포함하는 다중 시나리오 벤치마크를 최초로 구축했다.

- **다양한 주제와 모달리티 포함**: 사진&미술(34%), 건강(28%), 이벤트&초상화(16%) 등 6개 카테고리의 3,600개 이미지를 통합하여 현실적 다양성을 확보했다.

- **정량화된 성능 갭 분석**: 개별 시나리오 대비 결합 시나리오에서 F1-점수 3.4~10.9 포인트 저하라는 구체적 수치를 제시하여 문제의 심각성을 입증했다.

## Limitation & Further Study

- **언어 범위의 제한**: 논문의 일부만 제공되어 정확한 다국어 범위를 특정하기 어려우나, 중국어와 아랍어 중심으로 보여 유럽/아프리카 언어 확장 필요

- **모델 범위**: 평가가 주로 비전-언어 모델(MLLM)에 집중되어 있으며, 순수 LLM의 교차-언어 환각 메커니즘과의 연관성 분석 부족

- **환각 생성 방법론의 자동화**: 자동 생성된 환각이 실제 모델의 환각 패턴을 충분히 반영하는지에 대한 검증 부재

- **후속 연구 방향**: 
  - 환각 원인에 대한 심층 분석(표현 공간의 교차-모달/교차-언어 정렬 실패 원인)
  - 동적 환각 완화 전략 개발
  - 추가 언어쌍 및 모달리티(오디오, 비디오) 확장
  - 다중-단계 추론 시나리오에서의 환각 연쇄 효과 연구


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.2/5

**총평**: CCHall은 기존 연구의 명확한 갭을 식별하고 실제 응용에서 중요한 결합 환각 문제를 평가하는 최초의 벤치마크로, 높은 실용성과 학문적 가치를 제공한다. 다만 자동 환각 생성 방법론의 검증과 메커니즘 분석이 보강되면 더욱 강력한 자료가 될 수 있다.

## Related Papers

- ⚖️ 반론/비판: [[papers/460_Language_models_surface_the_unwritten_code_of_science_and_so/review]] — LLM의 편향을 진단 도구로 활용하자는 관점과 교차-언어/모달 환각을 문제로 보는 관점이 대조됨
- 🏛 기반 연구: [[papers/753_Shared_imagination_Llms_hallucinate_alike/review]] — LLM들이 유사한 환각을 보인다는 기초 연구가 교차-언어/모달 환각 벤치마크 개발의 이론적 근거를 제공함
- 🔗 후속 연구: [[papers/827_Towards_effective_extraction_and_evaluation_of_factual_claim/review]] — 팩트체킹에서 주장 추출의 모호성 처리 문제가 교차-언어/모달 상황에서 더욱 복잡해지는 확장된 도전과제임
- 🔗 후속 연구: [[papers/119_Autocap_Towards_automatic_cross-lingual_alignment_planning_f/review]] — 교차언어 및 교차문화 이해를 위한 새로운 벤치마크가 AutoCAP의 영점 교차언어 추론 프레임워크를 문화적 맥락까지 고려하는 더 포괄적인 평가로 확장함
- ⚖️ 반론/비판: [[papers/460_Language_models_surface_the_unwritten_code_of_science_and_so/review]] — LLM의 편향을 진단 도구로 활용하자는 관점과 교차-언어/모달 환각을 문제로 보는 관점이 대조됨
