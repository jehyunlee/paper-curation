---
title: "288_Draft_sketch_and_prove_Guiding_formal_theorem_provers_with_i"
authors:
  - "Albert Q. Jiang"
  - "Sean Welleck"
  - "Jin Zhou"
  - "Wenda Li"
  - "Jiacheng Liu"
date: "2022"
doi: "미기재"
arxiv: ""
score: 4.3
essence: "본 논문은 **비형식적 증명(informal proofs)을 형식적 증명 스케치(formal proof sketches)로 변환하여 자동 정리 증명기(automated theorem prover)를 유도하는 혁신적 방법론**을 제시한다. 이는 풍부한 수학 텍스트 데이터를 활용하면서도 형식 시스템의 논리적 엄밀성을 보장한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Formal_Theorem_Proving"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Jiang et al._2022_Draft, sketch, and prove Guiding formal theorem provers with informal proofs.pdf"
---

# Draft, sketch, and prove: Guiding formal theorem provers with informal proofs

> **저자**: Albert Q. Jiang, Sean Welleck, Jin Zhou, Wenda Li, Jiacheng Liu, Mateja Jamnik, Timothée Lacroix, Yuhuai Wu, Guillaume Lample | **날짜**: 2022 | **DOI**: [미기재](https://arxiv.org/abs/2210.12283)

---

## Essence

![Figure 1](figures/fig1.webp)
*Draft, Sketch, and Prove 프레임워크. 비형식적 명제에서 형식적 증명까지 도달하는 3단계 과정*

본 논문은 **비형식적 증명(informal proofs)을 형식적 증명 스케치(formal proof sketches)로 변환하여 자동 정리 증명기(automated theorem prover)를 유도하는 혁신적 방법론**을 제시한다. 이는 풍부한 수학 텍스트 데이터를 활용하면서도 형식 시스템의 논리적 엄밀성을 보장한다.

## Motivation

- **Known**: 형식적 증명의 자동화는 깊은 학습으로 성공하지 못했으나, 최근 대규모 언어 모델(LLM)이 비형식적 수학 추론에서 뛰어난 능력을 보임. 반면 형식 증명 데이터는 극도로 부족함 (Isabelle 코퍼스 < 0.6GB).

- **Gap**: 기존 접근법은 강력한 탐색 알고리즘에만 집중했으며, **기존의 풍부하게 존재하는 비형식적 증명을 활용하지 못했음**.

- **Why**: 비형식적 증명은 수학 교과서에 풍부하게 존재하며, LLM이 생성할 수도 있다. 이들을 형식적 증명으로 변환할 수 있다면 데이터 부족 문제를 해결할 수 있음.

- **Approach**: 3단계 파이프라인 - (1) 비형식적 증명 작성(또는 생성), (2) LLM을 통해 형식적 증명 스케치로 매핑, (3) 자동 정리 증명기로 미증명 추측(open conjectures) 해결.

## Achievement

![Figure 2](figures/fig2.webp)
*Isabelle의 증명 스케치 예시. 비형식적 증명 세그먼트(빨간색)와 형식적 상대물의 정렬*

1. **성능 향상**: miniF2F 데이터셋에서 자동 정리 증명기의 성공률을 **20.9%에서 38.9%(LLM 생성 증명)~39.3%(인간 작성 증명)로 증대**.

2. **구조화된 스케치 생성**: 대규모 언어 모델이 비형식적 증명과 동일한 추론 단계를 따르는 **잘 구조화된 형식적 스케치를 생성 가능함을 입증**.

3. **데이터셋 구축**: miniF2F 데이터셋과 정렬된 **수동 큐레이션된 비형식적 명제 및 증명 데이터셋 구축**.

## How

![Figure 3](figures/fig3.webp)
*자동형식화 시도 횟수에 따른 miniF2F 해결 문제 수*

**3단계 파이프라인:**

- **단계 1 - 비형식적 증명 작성(Drafting)**: 
  - 시나리오 A: 인간 작성 증명 (기존 교과서에서)
  - 시나리오 B: LLM 생성 증명 (수학 텍스트로 학습된 모델)

- **단계 2 - 형식적 스케치 매핑(Sketching)**:
  - Few-shot 프롬프팅으로 LLM("autoformalizer")을 이용
  - 비형식적 증명의 고수준 구조를 보존하면서 형식적 언어로 변환
  - 저수준 세부사항은 `<···>` 토큰으로 표시된 개방 추측으로 남김
  - 비형식적 증명 세그먼트와 형식적 상대물의 주석으로 정렬 개선

- **단계 3 - 개방 추측 증명(Proving)**:
  - 자동 정리 증명기(off-the-shelf automated provers)를 사용하여 각 개방 추측을 독립적으로 증명
  - 프레임워크는 특정 증명기 선택에 무관(기술적 중립성)

## Originality

- **비형식적-형식적 증명의 최초 대규모 연결**: 기존 연구는 명제 자동형식화만 수행했으나, 본 연구는 **증명 전체의 자동형식화**를 처음 시도.

- **증명 스케치의 창의적 활용**: 저수준 세부사항은 버리고 고수준 구조만 유지하는 **중간 표현으로서의 증명 스케치 도입**으로, 비형식-형식 간 간극 축소.

- **LLM의 Few-shot 능력 활용**: 기존 ML 기반 정리 증명은 소규모 모델(< 1B 파라미터)에 의존했으나, 본 연구는 **대규모 LLM(175B 파라미터)의 뛰어난 In-Context Learning 활용**.

- **이중 설정의 실용성**: 인간 증명과 LLM 생성 증명 두 가지 설정으로 **다양한 현실 시나리오 반영**.

## Limitation & Further Study

- **LLM 생성 증명의 정확성**: LLM이 생성한 비형식적 증명이 항상 수학적으로 타당한 것은 아니며, 이는 최종 형식적 증명 성공에 영향을 미침. 증명 검증 메커니즘 강화 필요.

- **개방 추측의 난이도**: 스케치의 개방 추측이 원래 문제만큼 어려울 수 있으며, 자동 증명기의 한계로 인해 성능 향상이 제한될 수 있음.

- **데이터셋 규모**: miniF2F는 상대적으로 작은 수학 경시 문제 집합으로, 더 다양한 수학 영역(대수, 기하학, 해석학 등)에서의 확장 필요.

- **후속 연구 방향**: 
  - 비형식적 증명의 정확성 자동 평가 방법 개발
  - 더 큰 규모의 수학 텍스트 코퍼스 구축
  - 증명 스케치 생성의 개선(구조적 일관성 향상)
  - 다양한 형식적 시스템(Lean, Coq 등)으로의 일반화

## Evaluation

- **Novelty**: 4.5/5
  - 비형식-형식 증명 연결의 혁신적 접근이나, 개별 구성요소(LLM 프롬프팅, 자동 증명)는 기존 기술의 조합

- **Technical Soundness**: 4/5
  - 방법론은 타당하고 3단계 파이프라인이 명확하나, 개방 추측의 복잡도 분석 부족

- **Significance**: 4.5/5
  - 형식적 증명 자동화 분야에 중대한 진전을 제시하며, 실제 달성된 성능 향상(약 2배)이 의미 있음

- **Clarity**: 4/5
  - 전체 구조와 동기가 명확하나, 몇몇 기술적 세부사항(prompt 설계, 증명기 선택)의 설명이 부족

- **Overall**: 4.3/5

**총평**: 본 논문은 비형식적 증명의 풍부한 자료를 형식 시스템의 엄밀성과 결합하는 **실용적이고 혁신적인 접근법**을 제시하며, miniF2F에서 약 2배의 성능 향상을 달성하였다. 특히 LLM의 생성 능력과 자동 증명기의 검증 능력을 효과적으로 활용한 점이 돋보이지만, 생성된 증명의 정확성 평가와 더 대규모 데이터셋으로의 확장이 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/379_Generative_language_modeling_for_automated_theorem_proving/review]] — GPT-f의 직접적 형식 증명 생성을 비형식 증명 활용으로 개선한 혁신적 방법론
- 🏛 기반 연구: [[papers/251_Data_for_mathematical_copilots_Better_ways_of_presenting_pro/review]] — 비형식적 증명의 중요성을 강조하며 형식 시스템과의 연결점을 제시
- 🔄 다른 접근: [[papers/264_Deepseek-prover_Advancing_theorem_proving_in_llms_through_la/review]] — DeepSeek-Prover의 대규모 합성 데이터와 달리 기존 비형식 증명 활용하는 접근법
- 🧪 응용 사례: [[papers/532_MerLean_An_Agentic_Framework_for_Autoformalization_in_Quantu/review]] — 비형식에서 형식으로의 변환 방법론이 MerLean의 자동형식화 프레임워크에 적용됨
- 🏛 기반 연구: [[papers/257_Decomposing_the_enigma_Subgoal-based_demonstration_learning/review]] — 형식 정리 증명에서의 초안-스케치-증명 가이드 방법론은 부분목표 기반 시연 학습의 구조화된 증명 과정 설계에 이론적 근거를 제공한다.
- 🔗 후속 연구: [[papers/379_Generative_language_modeling_for_automated_theorem_proving/review]] — GPT-f의 형식적 증명 생성을 비형식적 증명에서 유도하는 방법론으로 발전시킴
- 🏛 기반 연구: [[papers/539_Minif2f_a_cross-system_benchmark_for_formal_olympiad-level_m/review]] — 비형식적 증명에서 형식적 증명으로의 변환 방법론이 miniF2F 문제 해결의 기초가 됨
- 🏛 기반 연구: [[papers/251_Data_for_mathematical_copilots_Better_ways_of_presenting_pro/review]] — 비형식적 증명의 풍부한 정보가 형식적 증명 스케치 생성에 필수적임을 보여줌
- 🧪 응용 사례: [[papers/532_MerLean_An_Agentic_Framework_for_Autoformalization_in_Quantu/review]] — 비형식에서 형식으로의 증명 변환 방법론을 양자계산 분야에 특화하여 완전 자동화
- 🔄 다른 접근: [[papers/264_Deepseek-prover_Advancing_theorem_proving_in_llms_through_la/review]] — 비형식 증명 활용과 달리 순수 형식적 데이터 합성으로 성능 향상을 달성
