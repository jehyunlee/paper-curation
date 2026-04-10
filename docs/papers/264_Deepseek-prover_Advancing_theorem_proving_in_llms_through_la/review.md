---
title: "264_Deepseek-prover_Advancing_theorem_proving_in_llms_through_la"
authors:
  - "Huajian Xin"
  - "Daya Guo"
  - "Zhihong Shao"
  - "Z. Ren"
  - "Qihao Zhu"
date: "2024"
doi: "미공개"
arxiv: ""
score: 4.25
essence: "이 논문은 비형식적 수학 문제에서 자동으로 대규모 형식 증명 데이터(Lean 4)를 합성하는 방법을 제시하고, 이를 통해 미세조정된 LLM이 GPT-4를 능가하는 정리 증명 성능을 달성했다. 특히 800만 개의 정형화된 명제-증명 쌍을 생성하여 훈련 데이터 부족 문제를 해결했다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Formal_Theorem_Proving"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Xin et al._2024_Deepseek-prover Advancing theorem proving in llms through large-scale synthetic data.pdf"
---

# Deepseek-prover: Advancing theorem proving in llms through large-scale synthetic data

> **저자**: Huajian Xin, Daya Guo, Zhihong Shao, Z. Ren, Qihao Zhu, Bo Liu, Chong Ruan, Wenda Li, Xiaodan Liang | **날짜**: 2024 | **DOI**: 미공개

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: 접근 방법의 개요. 비형식 수학 문제에서 형식적 증명 데이터를 생성하는 반복적 파이프라인*

이 논문은 비형식적 수학 문제에서 자동으로 대규모 형식 증명 데이터(Lean 4)를 합성하는 방법을 제시하고, 이를 통해 미세조정된 LLM이 GPT-4를 능가하는 정리 증명 성능을 달성했다. 특히 800만 개의 정형화된 명제-증명 쌍을 생성하여 훈련 데이터 부족 문제를 해결했다.

## Motivation

- **Known**: Lean, Isabelle, Coq 같은 형식 증명 보조기(proof assistant)는 수학적 증명의 정확성과 신뢰성을 보장하지만, 형식 증명 작성은 매우 복잡하고 전문적 지식이 필요함. 최근 LLM의 수학적 추론 능력이 향상되었음.

- **Gap**: LLM 기반 자동 정리 증명(automated theorem proving)의 발전이 훈련 데이터 부족으로 심각하게 저해되고 있음. 프로그래밍 언어와 달리 형식 증명 언어는 소수의 수학자만 사용하므로 병렬 코퍼스(parallel corpus)가 극도로 제한적임.

- **Why**: 기존 자동형식화(autoformalization) 연구는 규칙 기반 변환이나 소규모 LLM 번역에 그쳐 데이터셋이 너무 작아 LLM의 잠재력을 충분히 활용하지 못함.

- **Approach**: 비형식 수학 경시 문제(고등학교~학부 수준)를 형식 명제로 자동변환하고, 품질 필터링과 검증 과정을 거쳐 대규모 형식 증명 데이터를 반복적으로 생성. 각 반복에서 생성된 정확한 증명 쌍으로 모델을 재훈련하여 데이터 질과 양을 동시에 확보.

## Achievement

1. **데이터셋 규모**: 869,659개의 비형식 수학 문제에서 800만 개의 고품질 형식 명제-증명 쌍 생성 (기존 자동형식화 연구의 수십~수백배 규모)

2. **벤치마크 성능**:
   - miniF2F-test: 64 샘플 기준 **46.3%** 전체 증명 정확도 (GPT-4: 23.0%, RL 방법: 41.0%)
   - miniF2F 누적: **52%** 정확도
   - FIMO 벤치마크: 100 샘플로 **4/148**, 4096 샘플로 **5/148** 증명 성공 (GPT-4: 0/148)

3. **반복 학습의 유효성**: 애블레이션 실험으로 각 반복마다 miniF2F 해결 문제 수가 점진적으로 증가함을 입증

## How

![Figure 1 참조]

**4단계 반복 파이프라인**:

1. **자동형식화 (Autoformalization)**
   - DeepSeekMath-Base 7B를 MMA 데이터셋(Lean 4 mathlib 기반)으로 미세조정
   - 구조화된 프롬프트를 통해 비형식 문제를 Lean 4 형식 명제로 변환
   - 웹 스크래핑으로 수집한 869,659개 고등학교~학부 수준 경시 문제 활용

2. **품질 보증 (Quality Assurance)**
   - **모델 스코링**: 단순 명제 필터링으로 증명 난이도 높은 문제 선별
   - **가설 거부 전략 (Hypothesis Rejection)**: 비형식적으로 부정확한 명제 제거
   - 형식 검증자로 생성된 명제 유효성 검사

3. **증명 생성 및 검증 (Statements Proving)**
   - DS-Prover가 형식 명제의 증명 코드 생성
   - Lean 4 형식 검증자로 증명 정확성 자동 확인
   - **병렬 증명 최적화**: 원래 명제와 부정 명제를 동시에 증명하여 탐색 공간 축소 (unprovable 명제는 부정 증명으로 빠르게 배제)

4. **반복 훈련 (Iterative Fine-tuning)**
   - 검증된 명제-증명 쌍으로 DS-Prover 재훈련
   - 모델 성능 향상 → 더 나은 형식화 및 증명 생성 → 고품질 데이터 증가
   - 성능 개선이 수렴할 때까지 반복

## Originality

- **대규모 합성 데이터 생성 파이프라인**: 기존 자동형식화 연구보다 한 자리수 이상 큰 규모(800만)의 형식 증명 데이터를 체계적으로 생성하는 반복 방법론 제시

- **품질-규모 동시 확보**: 단순히 데이터 양만 늘리지 않고, 형식 검증 기반의 필터링과 반복 훈련으로 데이터 품질을 보장하는 순환 구조 설계

- **병렬 증명 최적화**: 부정 명제 병렬 증명을 통해 unprovable 명제 처리 시간을 단축하는 실용적 가속 기법

- **오픈소스 기여**: 800만 규모의 형식 증명 데이터셋과 훈련된 모델을 공개 예정으로, 정리 증명 연구의 인프라 기여

## Limitation & Further Study

**한계점**:
- 고등학교~학부 수준 경시 문제에 국한 (대학원급 고급 수학 미포함)
- 주로 대수, 정수론 중심 (기하, 조합론, 통계는 부분적)
- miniF2F에서 46.3%, FIMO에서 3.4% 정확도로 여전히 실용적 활용에는 거리 있음
- 생성된 형식 명제의 내재적 품질 분포 및 편향성 분석 부재
- 병렬 증명 최적화의 구체적 성능 개선 정량화 미흡

**후속 연구 방향**:
- 고급 정리(advanced theorems)로 데이터셋 확장
- 다중 형식 언어(Isabelle, Coq) 지원
- 강화학습(reinforcement learning)과 합성 데이터의 결합
- 생성된 데이터셋의 다양성 분석 및 편향 해결
- 대규모 모델(13B, 70B 등)로의 확장 연구


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.25/5

**총평**: 이 논문은 정형식 증명의 오래된 데이터 부족 문제를 대규모 자동 합성과 반복 검증을 통해 실용적으로 해결한 견고한 연구로, 특히 800만 규모 오픈소스 데이터셋의 공개는 자동정리증명 분야에 상당한 인프라 기여를 할 것으로 예상된다. 다만 정리 증명의 절대 성능은 여전히 제한적이며, 고급 수학으로의 확장 가능성 검증이 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/379_Generative_language_modeling_for_automated_theorem_proving/review]] — GPT-f의 초기 형식 증명 연구를 대규모 합성 데이터와 Lean 4로 크게 발전시킴
- 🧪 응용 사례: [[papers/539_Minif2f_a_cross-system_benchmark_for_formal_olympiad-level_m/review]] — DeepSeek-Prover의 형식 증명 능력을 miniF2F 벤치마크로 체계적으로 평가할 수 있음
- ⚖️ 반론/비판: [[papers/251_Data_for_mathematical_copilots_Better_ways_of_presenting_pro/review]] — 대규모 데이터 합성 접근법과 달리 증명의 동기와 사고 과정의 중요성을 간과할 수 있음
- 🔄 다른 접근: [[papers/288_Draft_sketch_and_prove_Guiding_formal_theorem_provers_with_i/review]] — 비형식 증명 활용과 달리 순수 형식적 데이터 합성으로 성능 향상을 달성
- 🔗 후속 연구: [[papers/339_Fimo_A_challenge_formal_dataset_for_automated_theorem_provin/review]] — IMO 수준 정리증명을 LLM 기반 증명으로 확장한 자동정리증명 발전
- 🔗 후속 연구: [[papers/257_Decomposing_the_enigma_Subgoal-based_demonstration_learning/review]] — DeepSeek-Prover의 대규모 언어모델 정리 증명은 부분목표 기반 시연 학습을 LLM 기반 자동 증명 시스템으로 확장한다.
- 🏛 기반 연구: [[papers/568_Mustard_Mastering_uniform_synthesis_of_theorem_and_proof_dat/review]] — 형식 수학에서의 정리 증명 능력을 위한 언어모델 기반 기술의 핵심 기반을 제공한다
- 🧪 응용 사례: [[papers/182_Can_language_models_falsify_evaluating_algorithmic_reasoning/review]] — 정리 증명에서 LLM의 논리적 추론 능력을 반례 생성 맥락에서 평가할 수 있다
- 🏛 기반 연구: [[papers/513_M2F_Automated_Formalization_of_Mathematical_Literature_at_Sc/review]] — 수학적 증명과 형식화에서 LLM의 근본적인 추론 능력 향상 방법론을 제공한다.
- 🏛 기반 연구: [[papers/826_Towards_Autonomous_Mathematics_Research/review]] — DeepSeek-Prover의 대규모 언어 모델 기반 정리 증명이 Aletheia의 자율적 수학 연구 및 증명 능력의 핵심적인 기술적 토대이다.
- 🔗 후속 연구: [[papers/379_Generative_language_modeling_for_automated_theorem_proving/review]] — GPT-f의 초기 형식 증명 연구를 대규모 합성 데이터로 발전시켜 성능을 크게 개선함
- 🧪 응용 사례: [[papers/539_Minif2f_a_cross-system_benchmark_for_formal_olympiad-level_m/review]] — DeepSeek-Prover의 대규모 형식 증명 데이터 합성 기법을 miniF2F 벤치마크로 평가할 수 있음
- ⚖️ 반론/비판: [[papers/251_Data_for_mathematical_copilots_Better_ways_of_presenting_pro/review]] — DeepSeek-Prover의 대규모 데이터 접근법과 달리 증명의 질적 측면과 사고 과정을 중시
- 🔄 다른 접근: [[papers/288_Draft_sketch_and_prove_Guiding_formal_theorem_provers_with_i/review]] — DeepSeek-Prover의 대규모 합성 데이터와 달리 기존 비형식 증명 활용하는 접근법
- 🔗 후속 연구: [[papers/030_A_survey_on_deep_learning_for_theorem_proving/review]] — 정리 증명 심층학습 기법을 LLM 기반 접근으로 발전시킨 최신 연구 동향
- 🔗 후속 연구: [[papers/1095_Towards_large_language_models_as_copilots_for_theorem_provin/review]] — DeepSeek-Prover의 LLM 기반 증명 방법을 인간-AI 협업 환경으로 확장
- 🔄 다른 접근: [[papers/482_Lean-star_Learning_to_interleave_thinking_and_proving/review]] — 둘 다 형식 정리 증명에서 LLM의 추론 능력을 향상시키는 방법을 연구하지만, 하나는 자연언어 사고를 통합하고 다른 하나는 강화학습 기반 접근법을 사용한다.
