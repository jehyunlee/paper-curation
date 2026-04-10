---
title: "499_LLM_With_Tools_A_Survey"
authors:
  - "Zhuocheng Shen"
date: "2024"
doi: "10.48550/arXiv.2409.18807"
arxiv: ""
score: 3.5
essence: "본 논문은 대규모 언어 모델(LLM)에 외부 도구 통합을 통해 모델의 성능을 향상시키는 방법론을 체계적으로 조사한 종합 리뷰이다. 사용자 지시 이해부터 도구 선택, 실행, 피드백 처리까지의 표준화된 패러다임을 제시하고, 미세조정(Fine-tuning)과 문맥 내 학습(In-Context Learning) 기법을 통해 LLM의 도구 활용 능력을 강화하는 방법을 탐구한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Language_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Shen_2024_LLM With Tools A Survey.pdf"
---

# LLM With Tools: A Survey

> **저자**: Zhuocheng Shen | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2409.18807](https://doi.org/10.48550/arXiv.2409.18807)

---

## Essence

![Figure 1](figures/fig1.webp) *LLM이 도구를 사용하는 전체 프로세스*

본 논문은 대규모 언어 모델(LLM)에 외부 도구 통합을 통해 모델의 성능을 향상시키는 방법론을 체계적으로 조사한 종합 리뷰이다. 사용자 지시 이해부터 도구 선택, 실행, 피드백 처리까지의 표준화된 패러다임을 제시하고, 미세조정(Fine-tuning)과 문맥 내 학습(In-Context Learning) 기법을 통해 LLM의 도구 활용 능력을 강화하는 방법을 탐구한다.

## Motivation

- **Known**: ChatGPT, GPT-4 등 대규모 언어 모델은 우수한 자연어 이해 및 추론 능력을 보유하고 있으나, 확률 기반 모델의 특성상 실시간 정보 처리, 정밀한 수학 연산, 최신 지식 활용 시 환각(hallucination) 문제가 발생함
  
- **Gap**: 기존 LLM 단독으로는 전문 분야의 정밀한 작업, 복잡한 수학 연산, 실시간 데이터 접근이 필요한 작업에서 성능이 만족스럽지 않음

- **Why**: 도구는 인류 문명의 정수이며 능력의 확장이므로, 동일한 원리를 LLM에 적용하면 정확성과 효율성을 향상시킬 수 있음

- **Approach**: (1) 사용자 의도 이해 → (2) 도구 기능 이해 → (3) 작업 분해 → (4) 동적 계획 조정의 통합 프레임워크 제시

## Achievement

![Figure 1](figures/fig1.webp) *사용자 명령에서 피드백 처리까지의 도구 활용 전체 사이클*

1. **표준화된 도구 활용 패러다임**: 6개의 함수(f_intent, f_plan, f_exec, f_feedback, f_perceive, f_adjust)로 구성된 형식적 프레임워크 정의로, 도구 통합의 일관성 있는 이해를 제공

2. **도구 활용의 6가지 핵심 도전 과제 체계화**: 도구 호출 시점, 도구 선택 정확성, 호출 방법, 추론 견고성, 시간 효율성, 일반화 능력을 명확히 구분하여 분석

3. **미세조정 기반 도구 통합 기법**: <TOOL> 태그를 활용한 특수 구문 구조(Equation 2)와 데이터셋 구성(Equation 1)으로, 모델이 도구 호출 시점, 도구명, 입력 매개변수를 효과적으로 학습하도록 지원

4. **Chameleon 재현 및 분석**: ScienceQA에서 Chameleon의 결과를 재현하고 코드 구조를 분석하여 실제 구현의 검증

## How

![Figure 1](figures/fig1.webp) *도구 사용 흐름도: 사용자 명령 → 의도 파악 → 계획 수립 → 실행 → 피드백 → 조정 → 반복*

- **의도 파악 (Intent Recognition)**: 함수 f_intent(u) → i로 사용자의 실제 필요를 추출하여 후속 계획의 방향성 결정

- **도구 이해**: 도구의 기본 연산, 적용 시나리오, 한계점을 깊이 있게 학습하여 '언제, 어디서, 어떻게' 사용할지 결정

- **작업 분해**: 복잡한 작업을 소작업(subtask)으로 분할하여 유연한 계획 조정 및 상황 적응성 향상

- **미세조정 데이터셋 구성**: C* 데이터셋에 <TOOL> ... </TOOL> 태그로 감싼 도구 호출 예제를 포함하여 모델 학습 (Eq. 1-2)

- **추론 과정의 견고성**: 오류 누적 방지를 위한 역추적(backtracking) 및 오류 수정 메커니즘 도입

- **병렬 처리 및 최적화**: 도구 호출의 시간 효율성을 위한 병렬화 전략

- **Algorithm 1 (InferWithTool)**: 모델이 <TOOL> 토큰을 생성하면 도구 쿼리 추출 → 도구 호출 → 응답 통합의 추론 시간 실행 절차

## Originality

- LLM과 도구 통합의 포괄적이고 체계화된 리뷰로, 산재된 연구를 일관된 패러다임 하에서 통합 제시

- 6개의 수학적 함수로 정의된 형식적 도구 사용 프로세스 모델은 기존 비구조화된 설명을 대체하는 더 정밀한 추상화 제공

- 특수 구문 구조 E(c; r) = <TOOL> ac(ic) ! r </TOOL>를 통한 미세조정 접근법의 명시적 설계

- 도구 호출 시점 결정의 중요성 강조: "도구를 호출하기 위해 도구를 호출하지 말 것(tools should not be called for the sake of calling them)" 원칙 제시

- 도구 생성 능력(tool creation)으로의 확장 제안으로, 단순 사용자(tool user)에서 창조자(tool creator)로의 역할 전환 모색

## Limitation & Further Study

- **한계**:
  - 논문이 주로 개념적 프레임워크 제시에 중점을 두어 구체적 실험 결과나 벤치마크 비교가 제한적
  - Chameleon 결과 재현을 언급하나 상세한 실험 설정, 정량적 성능 비교, 통계적 유의성 검증 부재
  - 도구 선택 정확성 향상을 위한 구체적 알고리즘이 충분히 제시되지 않음
  - 다양한 도구 조합 시의 상호작용 복잡성(tool interaction complexity)에 대한 논의 미흡
  - 구체적 데이터셋 증강(augmentation) 방법론 부족

- **후속 연구**:
  - 도구 호출 오류 복구의 견고성을 위한 백트래킹 알고리즘의 실제 구현 및 성능 평가
  - 대규모 도구 집합에서의 도구 선택 정확성 향상을 위한 신경망 기반 도구 랭킹 메커니즘
  - LLM이 자체적으로 도구를 생성하고 최적화하는 메타-도구 창조 프레임워크 개발
  - 일반화 능력 평가를 위한 표준화된 벤치마크 및 평가 메트릭 수립
  - 미세조정과 문맥 내 학습의 상대적 효율성 비교를 통한 최적 전략 도출


## Evaluation

- Novelty: 3.5/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 3.5/5
- Overall: 3.5/5

**총평**: 본 논문은 LLM의 도구 통합이라는 중요한 주제를 체계적이고 형식적인 프레임워크로 정리한 가치 있는 종합 리뷰이나, 개념적 프레임워크 제시에 치중되어 있어 구체적 실험 검증, 정량적 성과 비교, 실제 구현 상세 부족으로 인해 원본 리서치 논문으로서의 기여도는 제한적이다.

## Related Papers

- 🏛 기반 연구: [[papers/813_Toolformer_Language_Models_Can_Teach_Themselves_to_Use_Tools/review]] — 언어 모델이 스스로 도구 사용법을 학습하는 Toolformer의 기초 연구를 제공한다.
- 🔗 후속 연구: [[papers/815_ToolLLM_Facilitating_Large_Language_Models_to_Master_16000_R/review]] — 16,000개 이상의 도구를 마스터하는 LLM 훈련으로 도구 활용 능력을 대폭 확장한다.
- ⚖️ 반론/비판: [[papers/814_Tooling_or_Not_Tooling_The_Impact_of_Tools_on_Language_Agent/review]] — 언어 에이전트에서 도구 사용이 미치는 영향에 대한 비판적 분석을 제공한다.
- 🔗 후속 연구: [[papers/114_Augmented_Language_Models_a_Survey/review]] — 언어모델의 추론 및 도구 사용 확장에 대한 조사가 도구를 활용하는 LLM에 대한 더 포괄적이고 구체적인 서베이로 발전했다
- 🧪 응용 사례: [[papers/735_SciToolAgent_a_knowledge-graph-driven_scientific_agent_for_m/review]] — 도구를 활용한 LLM 연구의 포괄적 조사를 과학 도구 특화 에이전트 개발에 적용할 수 있다
- 🏛 기반 연구: [[papers/848_TxAgent_An_AI_Agent_for_Therapeutic_Reasoning_Across_a_Unive/review]] — 도구를 활용한 LLM의 포괄적 조사가 211개 생의학 도구를 활용한 치료 추론 에이전트의 기반을 제공한다
- 🔗 후속 연구: [[papers/814_Tooling_or_Not_Tooling_The_Impact_of_Tools_on_Language_Agent/review]] — 도구를 활용한 LLM에 대한 종합적 조사를 화학 분야의 구체적 사례 분석으로 확장한다.
- 🏛 기반 연구: [[papers/496_LLM_Agents_Making_Agent_Tools/review]] — 도구 사용을 위한 LLM 조사 연구가 TOOLMAKER의 과학 도구 자동 생성 및 LLM 호환성 구현의 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/842_Tree-planner_Efficient_close-loop_task_planning_with_large_l/review]] — LLM의 도구 활용 능력을 토큰 효율적인 계획 수립으로 확장한 구체적 구현체를 제시한다.
- 🏛 기반 연구: [[papers/815_ToolLLM_Facilitating_Large_Language_Models_to_Master_16000_R/review]] — LLM 도구 사용에 대한 포괄적 서베이에서 제시된 방법론을 대규모 벤치마크로 구현
