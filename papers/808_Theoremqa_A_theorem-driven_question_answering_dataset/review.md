---
title: "808_Theoremqa_A_theorem-driven_question_answering_dataset"
authors:
  - "Wenhu Chen"
  - "Ming Yin"
  - "Max Ku"
  - "Pan Lu"
  - "Yixin Wan"
date: "2023"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "대학 수준의 수학, 물리, 금융, 전산 분야에서 350개 이상의 정리(theorem)를 포함하는 800개의 고품질 질문-답변 쌍으로 구성된 정리 중심 질문 답변 데이터셋을 제시한다. 이는 LLM의 도메인 지식 적용 능력을 평가하는 첫 번째 벤치마크이다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Research_Ideation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chen et al._2023_Theoremqa A theorem-driven question answering dataset.pdf"
---

# TheoremQA: A Theorem-driven Question Answering Dataset

> **저자**: Wenhu Chen, Ming Yin, Max Ku, Pan Lu, Yixin Wan, Xueguang Ma, Jianyu Xu, Xinyi Wang, Tony Xia | **날짜**: 2023 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*TheoremQA의 개요 및 적용된 프롬프팅 전략*

대학 수준의 수학, 물리, 금융, 전산 분야에서 350개 이상의 정리(theorem)를 포함하는 800개의 고품질 질문-답변 쌍으로 구성된 정리 중심 질문 답변 데이터셋을 제시한다. 이는 LLM의 도메인 지식 적용 능력을 평가하는 첫 번째 벤치마크이다.

## Motivation

- **Known**: GPT-4와 PaLM-2 등 최근 LLM들은 GSM8K 데이터셋에서 90% 이상의 정확도를 달성하여 기초 수학 문제에서는 우수한 성능을 보이고 있음.

- **Gap**: 기존 수학 문제 데이터셋(MATH, AQuA, MathQA 등)은 초중등 수준의 산술/대수 문제가 주를 이루며, 특정 정리를 적용해야 하는 도메인 특화 지식을 요구하는 대학 수준의 어려운 문제를 충분히 포함하지 않음.

- **Why**: 현존하는 가벼운 벤치마크로는 최신 LLM의 실제 한계를 파악하기 어렵고, 실제로 인류가 해결해야 하는 도전적인 과학 문제들에 대한 LLM의 적용 가능성을 검증하지 못함.

- **Approach**: 도메인 전문가 집단이 (1) 수학, 물리, 금융, 전산 분야의 약 400개 정리를 열거하고, (2) 각 정리와 관련된 대학 수준의 질문을 인터넷과 교과서에서 수집하며, (3) 자동 평가를 위해 답안 형식을 표준화(정수, 실수, 불린, 선택지)한 후 최종 800개의 높은 품질의 질문-정리-답변 3중쌍을 확보.

## Achievement

![Figure 2](figures/fig2.webp)
*TheoremQA의 예시. Stokes 정리를 이용한 적분 변환 문제*

1. **광범위한 정리 커버리지**: 수학(199개), 물리(52개), 금융(55개), 전산(48개) 등 354개의 정리를 포함하며, 대수학, 정수론, 그래프 이론, 정보이론 등 다양한 세부분야를 포괄.

2. **LLM 성능의 계층화 된 격차 발견**:
   - GPT-4: Program-of-Thoughts (PoT) 프롬프팅으로 51% 정확도 (최고 성능)
   - ChatGPT: 35% 정확도
   - 오픈소스 모델들(Alpaca, LLaMA 등): 모두 15% 이하로 무작위 추측(10%)과 거의 동등한 수준

3. **오류 분석을 통한 성능 개선 여지 파악**: GPT-4의 오류 중 약 50%는 계산 오류, 반올림 오류 등 사소한 실수에서 비롯되어 더 정교한 프롬프팅으로 개선 가능함. 반면 오픈소스 모델의 오류 90%는 정리 자체에 대한 지식 부족으로 근본적 개선 필요.

4. **멀티모달 평가**: 51개의 이미지 포함 질문을 통해 멀티모달 모델들을 평가했으나, 도표 및 텍스트가 혼재된 이미지의 비자연성으로 인해 기존 시각 인코더가 충분한 개선을 제공하지 못함.

## How

![Figure 3](figures/fig3.webp)
*TheoremQA의 답변 타입 분포*

**데이터셋 구성 프로세스**:
- **정리 열거**: GPT-4를 이용하여 각 분야의 주요 세부분야를 파악한 후, 도메인 전문가 집단이 정리 목록을 정제 및 보완
- **질문 수집**: 온라인 자료, 교과서, 전문가 창작 문제를 수집하면서 학습 데이터 오염(data contamination) 위험을 완화하기 위해 질문 수정 권장
- **답안 정규화**: 행렬, 기호, 도형 형태의 답을 정수/실수/불린/선택지 형태로 변환 (예: 행렬 문제 → 행렬의 대각합(trace) 질문으로 변경)
- **프롬프팅 전략**: 
  - Chain-of-Thoughts (CoT): 사고 과정을 텍스트로 표현
  - Program-of-Thoughts (PoT): Python 프로그램으로 사고 과정을 표현

**정리 통합 실험**:
- 정리 정보를 단순히 질문에 연결(concatenation)하는 방식의 정리 강화 생성(theorem-augmented generation)을 시도했으나 유의미한 성능 향상을 얻지 못함
- 더 복잡한 통합 전략의 필요성을 시사

## Originality

- **첫 번째 정리 중심 벤치마크**: 기존 수학 문제 데이터셋들(MATH, GSM8K, AQuA 등)과 달리, 대학 수준의 다양한 정리를 명시적으로 포함하고 정리 적용 능력을 평가하는 최초의 데이터셋.

- **광범위한 도메인 커버리지**: 수학, 물리, 금융, 전산 등 STEM 분야 전반에 걸친 종합적 평가 가능.

- **도메인 전문가 주도 품질 관리**: 석박사급 전문가들이 정리 선정, 질문 수집/수정, 답안 정규화 등의 전 과정에 참여하여 높은 품질 보증.

- **포괄적 모델 평가**: GPT-4, Claude, LLaMA, CodeGen, StarCoder 등 16개 모델을 다양한 프롬프팅 전략(CoT, PoT)으로 평가하여 현황의 명확한 스냅샷 제공.

- **멀티모달 포함**: 54개의 이미지 포함 질문으로 시각 이해 측면도 평가.

## Limitation & Further Study

**한계**:
- 정리 강화 생성(theorem-augmented generation)의 단순 연결 방식이 효과적이지 않았으며, 더 정교한 통합 전략이 필요함.
- 멀티모달 모델들이 도표와 텍스트가 혼재된 이미지를 효과적으로 처리하지 못하고 있으며, 이는 기존 시각 인코더의 한계를 반영.
- 오픈소스 모델들의 성능이 극히 낮아(15% 이하) 실제 적용 가능성이 제한적.
- 800개의 질문은 규모가 다소 제한적이며, 더 많은 샘플로 통계적 신뢰도를 높일 여지가 있음.

**후속 연구 방향**:
- 과학 분야 특화 사전학습(science-focused pre-training) 또는 미세조정(fine-tuning)을 통한 오픈소스 모델의 성능 개선.
- 정리 정보를 더 효과적으로 활용하는 프롬프팅 전략 및 아키텍처 개발.
- 도표/기호가 포함된 과학 이미지에 특화된 시각 인코더 개발.
- 더 정교한 프롬프팅이나 인간 개입을 통한 GPT-4의 계산 오류 감소 방안.
- 데이터셋 규모 확대 및 추가 도메인(생물학, 화학 등) 포함.

## Evaluation

- **Novelty (독창성)**: 4.5/5
  - 첫 번째 정리 중심 평가 벤치마크로서 새로운 가치 제공, 다만 기존 수학 문제 데이터셋의 자연스러운 확장의 성격도 있음.

- **Technical Soundness (기술적 타당성)**: 4/5
  - 도메인 전문가 주도의 체계적 데이터 구성, 자동 평가 가능한 표준화된 답변 형식, 포괄적 모델 평가. 다만 정리 강화 생성 실험이 단순하고 결과 분석이 다소 제한적.

- **Significance (중요성)**: 4/5
  - 최신 LLM의 한계를 드러내는 도움이 되는 벤치마크이며, 과학 문제 해결 능력 평가에 실질적 가치. 다만 실제 과학 연구나 실무 적용까지의 거리는 여전히 있음.

- **Clarity (명확성)**: 4.5/5
  - 논문 구조가 명확하고, 데이터셋 구성 과정, 평가 결과, 분석이 충분히 설명됨. 몇몇 섹션에서 추가 상세 설명 가능.

- **Overall (종합)**: 4.2/5

**총평**: TheoremQA는 LLM의 도메인 특화 지식 활용 능력을 체계적으로 평가하는 첫 번째 벤치마크로서 의미 있는 기여를 하며, 광범위한 모델 평가를 통해 현재의 성능 격차를 명확히 드러낸다. 다만 오픈소스 모델의 극히 낮은 성능은 평가의 변별력을 제한하고, 정리 통합 방식의 개선 여지가 크다는 점이 아쉽다.

## Related Papers

- 🏛 기반 연구: [[papers/697_Scaling_physical_reasoning_with_the_physics_dataset/review]] — PHYSICS 데이터셋의 물리 문제 평가 방식이 TheoremQA의 정리 기반 질문 답변 벤치마크 설계에 참고가 됨
- 🔗 후속 연구: [[papers/539_Minif2f_a_cross-system_benchmark_for_formal_olympiad-level_m/review]] — MinIF2F의 형식적 올림피아드 수학 벤치마크가 TheoremQA의 정리 적용 능력 평가를 더욱 엄밀하게 확장함
- 🔄 다른 접근: [[papers/706_SciBench_Evaluating_College-Level_Scientific_Problem-Solving/review]] — 둘 다 과학 문제 해결 벤치마크이지만 TheoremQA는 정리 중심, SciBench는 대학 수준 전반을 다루는 차이가 있음
- 🏛 기반 연구: [[papers/339_Fimo_A_challenge_formal_dataset_for_automated_theorem_provin/review]] — 정리 기반 질의응답이 형식적 수학 문제 해결의 방법론적 기초
- 🔄 다른 접근: [[papers/706_SciBench_Evaluating_College-Level_Scientific_Problem-Solving/review]] — 과학 문제 해결 능력을 대학 수준 vs 정리 증명 수준에서 각각 평가한다.
- 🔗 후속 연구: [[papers/697_Scaling_physical_reasoning_with_the_physics_dataset/review]] — TheoremQA의 정리 기반 평가 방식이 PHYSICS 데이터셋의 물리 문제 해결 능력 평가를 더욱 체계화함
- 🔄 다른 접근: [[papers/807_Theoremexplainagent_Towards_video-based_multimodal_explanati/review]] — 정리 설명을 위한 비디오 기반 접근법과 텍스트 기반 질문 답변의 서로 다른 다중모드 수학 교육 방식을 비교할 수 있다.
