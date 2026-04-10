---
title: "242_CRITIC_Large_Language_Models_Can_Self-Correct_with_Tool-Inte"
authors:
  - "Zhibin Gou"
  - "Zhihong Shao"
  - "Yeyun Gong"
  - "Yelong Shen"
  - "Yujiu Yang"
date: "2023"
doi: "10.48550/arXiv.2305.11738"
arxiv: ""
score: 4.25
essence: "대규모 언어모델(LLM)이 외부 도구(검색엔진, 코드 인터프리터 등)와 상호작용하여 자신의 출력을 검증하고 반복적으로 자가수정(self-correct)할 수 있도록 하는 통합 프레임워크를 제안한다. 인간의 비판적 사고 방식을 모방하여 할루시네이션, 코드 오류, 독성 콘텐츠 등의 문제를 완화한다."
tags:
  - "cat/Reinforcement_Learning_and_Self-Verification"
  - "sub/LLM_Self-Correction_and_Verification"
  - "topic/ai4s"
---

# CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing

> **저자**: Zhibin Gou, Zhihong Shao, Yeyun Gong, Yelong Shen, Yujiu Yang | **날짜**: 2023 | **DOI**: [10.48550/arXiv.2305.11738](https://doi.org/10.48550/arXiv.2305.11738)

---

## Essence

![Figure 1](https://github.com/microsoft/ProphetNet/tree/master/CRITIC) *CRITIC 프레임워크: 외부 도구와 상호작용하여 검증(Verify)한 후 비판(Critique)에 기반해 수정(Correct)하는 반복 과정*

대규모 언어모델(LLM)이 외부 도구(검색엔진, 코드 인터프리터 등)와 상호작용하여 자신의 출력을 검증하고 반복적으로 자가수정(self-correct)할 수 있도록 하는 통합 프레임워크를 제안한다. 인간의 비판적 사고 방식을 모방하여 할루시네이션, 코드 오류, 독성 콘텐츠 등의 문제를 완화한다.

## Motivation

- **Known**: ChatGPT 등 최신 LLM은 인상적인 성능을 보이지만, 사실 오류(hallucination), 코드 결함, 독성 콘텐츠 등의 일관성 없는 문제를 드러낸다. 기존 해결책은 대규모 인간 주석이나 과제 특화 학습을 필요로 한다.

- **Gap**: 인간은 검색엔진으로 팩트체크하거나 코드 인터프리터로 디버깅하는 등 외부 도구를 활용해 내용을 검증하고 수정하지만, 블랙박스 LLM은 이런 도구 상호작용 기반 자가수정 능력이 부족하다.

- **Why**: 외부 피드백(external feedback)없이 LLM의 자체 검증만으로는 신뢰성이 낮고, 자가수정(self-correction) 효과가 제한적이다. 도구 기반 객관적 검증이 필수적이다.

- **Approach**: 인컨텍스트 러닝(in-context learning)과 몇샷 데모(few-shot demonstration)를 통해, 추가 학습 없이 블랙박스 LLM이 적절한 외부 도구와 상호작용하여 비판을 생성하고 이를 기반으로 반복 수정하도록 유도한다.

## Achievement

![Figure 2](https://github.com/microsoft/ProphetNet/tree/master/CRITIC) *다양한 과제(QA, 수학 프로그램 합성, 독성 감소)에서 CRITIC 프롬프트 예시: 검증 후 비판 생성, 수정된 답변 제시*

1. **정량적 성과**: ChatGPT 적용 시 3개 QA 과제에서 7.7 F1 향상, 3개 수학추론 과제에서 7.0% 절대 성능 향상, 독성 확률 79.2% 감소 달성. LLaMA-2(7B, 13B, 70B) 등 다양한 모델에서 일관된 개선 확인.

2. **방법론 유효성**: 외부 도구 상호작용이 없는 순수 자가수정은 효과 미미하거나 성능 저하를 초래하지만, CRITIC의 검증-수정 반복 과정은 지속적 개선을 보장한다. 자가수정의 필수 조건으로 외부 피드백의 중요성을 입증.

## How

![Figure 3-5](https://github.com/microsoft/ProphetNet/tree/master/CRITIC) *반복 과정을 통한 성능 변화: QA, GSM8k 수학 추론, 독성 감소 과제별 반복 횟수에 따른 개선 추이*

**알고리즘 (Algorithm 1)**:
- **초기화(1단계)**: 입력 x에 대해 모델 M이 초기 출력 ŷ₀ 생성
- **검증(3단계)**: 프롬프트 ℘, 초기 출력 ŷᵢ를 포함한 컨텍스트에서 LLM이 외부 도구 T(검색엔진, 코드 인터프리터, 계산기 등)와 상호작용하여 비판 cᵢ 생성
- **중단 조건(4-6단계)**: 생성된 비판이 현재 출력이 정확함을 나타내면 반환
- **수정(7단계)**: 입력, 이전 출력, 비판을 모두 포함한 컨텍스트에서 개선된 출력 ŷᵢ₊₁ 생성
- **반복(2-8단계)**: n번 반복하거나 중단 조건 만족 시 종료

**핵심 프롬프트 전략**:
- 검증 단계: "위 답변의 문제점은 무엇인가?" 형태로 LLM의 평가 능력 활용
- 비판 생성: 타당성(Plausibility), 정확성(Correctness), 진실성(Truthfulness) 등 다차원적 검증
- 도구 활용: API 호출 결과(검색 쿼리, 코드 실행 결과 등)를 프롬프트에 자동 포함
- 과제 특화: QA는 팩트체크, 수학은 코드 실행 검증, 독성은 독성 감지기 활용

## Originality

- **도구-상호작용 기반 자가수정**: 기존의 인간 피드백이나 학습 기반 접근과 달리, 외부 객관적 도구를 통한 검증을 자가수정의 핵심으로 제시. 인간의 비판적 사고(critical thinking) 프로세스를 체계화한 첫 시도.

- **블랙박스 모델의 범용성**: 추가 학습, 파인튜닝, 거대 규모 인간 주석을 요구하지 않고 순수 인컨텍스트 러닝으로 ChatGPT, GPT-3.5, LLaMA 등 이질적 모델에 적용 가능한 범용 프레임워크.

- **외부 피드백의 필수성 입증**: 순수 자가수정의 한계를 실증적으로 보이고, LLM은 자체 검증 능력이 부족하므로 객관적 외부 도구가 필수임을 강조(Kadavath et al. 등 선행 연구 재확인 및 확장).

- **다과제 통합**: QA(사실성), 수학(논리성), 독성 감소(안전성) 등 이질적 평가 차원의 과제에 단일 프레임워크를 적용, 방법의 범용성 입증.

## Limitation & Further Study

- **도구 의존성**: CRITIC의 성능은 사용 가능한 외부 도구의 품질과 정확성에 크게 의존. 검색 결과가 부정확하거나 코드 인터프리터가 에러 처리를 잘못하면 잘못된 비판 생성 가능. 도구 신뢰도 평가 메커니즘 부재.

- **반복 횟수 결정**: 현재 중단 기준은 LLM이 "출력이 정확하다"고 판단하는 것인데, 이 판단 자체의 신뢰성이 불명확. 최적 반복 횟수를 동적으로 결정하는 방법 필요.

- **프롬프트 민감도**: 검증 및 수정 프롬프트 설계가 성능에 미치는 영향에 대한 체계적 분석 부족. 과제별 최적 프롬프트 발견이 수작업(manual)에 의존.

- **계산 비용**: 반복적 도구 호출로 인한 API 비용과 지연 시간 증가. 수렴 속도 분석 및 계산 효율성 개선 방안 제시 부족.

- **후속 연구 방향**:
  - 도구 신뢰도를 고려한 적응적 검증(adaptive verification) 메커니즘
  - 강화학습(RL) 기반 최적 도구 선택 및 반복 횟수 결정
  - 멀티홉(multi-hop) 도구 조합을 통한 복잡한 추론 문제 확장
  - 인간-LLM 협업 설정에서 도구 설명(tool explanation) 제공

## Evaluation

| 항목 | 평가 |
|------|------|
| **Novelty (독창성)** | 4/5 |
| **Technical Soundness (기술 타당성)** | 4.5/5 |
| **Significance (중요성)** | 4.5/5 |
| **Clarity (명확성)** | 4/5 |
| **Overall (종합)** | 4.25/5 |

**총평**: CRITIC은 LLM의 자가수정 문제를 외부 도구 상호작용으로 우아하게 해결하며, 추가 학습 없이 범용적으로 적용 가능한 실용적 프레임워크를 제시한다는 점에서 높은 가치가 있다. 다만 도구 품질 의존성, 프롬프트 설계의 수작업 필요성, 계산 비용 증가 등의 실무적 제약이 있으며, 이들을 보완하는 추가 연구가 필요하다. ICLR 2024 채택된 것을 고려하면 LLM 신뢰성 개선 분야에서 의미 있는 기여를 한 것으로 평가된다.

## Related Papers

- 🔄 다른 접근: [[papers/598_PAG_Multi-Turn_Reinforced_LLM_Self-Correction_with_Policy_as/review]] — 두 논문 모두 LLM 자기 수정을 다루되 CRITIC은 외부 도구 활용, PAG는 내부 정책-검증자 전환에 의존한다.
- 🏛 기반 연구: [[papers/813_Toolformer_Language_Models_Can_Teach_Themselves_to_Use_Tools/review]] — Toolformer의 언어 모델 도구 사용 학습 방법론은 CRITIC의 외부 도구 상호작용 프레임워크 설계에 핵심적인 이론적 기반을 제공한다.
- 🧪 응용 사례: [[papers/176_CACTUS_Chemistry_Agent_Connecting_Tool_Usage_to_Science/review]] — CRITIC의 도구 기반 자기수정 프레임워크는 CACTUS의 화학 도구 활용에서 실험 결과 검증과 오류 수정에 직접 적용될 수 있다.
- 🏛 기반 연구: [[papers/262_Deepreview_Improving_llm-based_paper_review_with_human-like/review]] — 도구 통합 기반 자기교정 기법으로 DeepReview의 다단계 구조화 프레임워크의 이론적 기반을 제공한다.
- ⚖️ 반론/비판: [[papers/471_Large_Language_Models_Cannot_Self-Correct_Reasoning_Yet/review]] — 도구 통합을 통한 자기 수정 방법론이 순수 LLM 자기 수정의 한계를 극복할 수 있음
- 🔗 후속 연구: [[papers/598_PAG_Multi-Turn_Reinforced_LLM_Self-Correction_with_Policy_as/review]] — CRITIC의 외부 도구 기반 자기수정을 PAG가 모델 내부의 정책-검증자 역할 전환으로 발전시켜 더 효율적인 워크플로우를 제공한다.
- 🔄 다른 접근: [[papers/371_GeneAgent_self-verification_language_agent_for_gene-set_anal/review]] — 생명과학과 일반 추론에서 각각 자기검증 메커니즘으로 LLM 환각 문제를 해결하는 서로 다른 접근법을 제시한다.
- 🔗 후속 연구: [[papers/396_Hallucination_mitigation_using_agentic_ai_natural_language-b/review]] — 도구 통합 자기 수정 능력으로 환각 완화 방법론을 확장한다.
- 🔄 다른 접근: [[papers/435_Interfeedback_Unveiling_interactive_intelligence_of_large_mu/review]] — 도구 기반 자기수정과 달리 인간 피드백을 통한 상호작용적 개선 능력에 집중
- 🔗 후속 연구: [[papers/747_Selfcheck_Using_llms_to_zero-shot_check_their_own_step-by-st/review]] — 도구를 활용한 자기 수정에서 도구 없이 순수하게 자체 추론을 검증하는 더 순수한 형태의 자기 검증 연구입니다.
- 🔄 다른 접근: [[papers/746_Self-Refine_Iterative_Refinement_with_Self-Feedback/review]] — 자기 정제 방식에서 CRITIC은 외부 도구를 활용하는 반면 Self-Refine은 단일 LLM만으로 피드백과 개선을 수행하는 차이점이 있음
- 🔄 다른 접근: [[papers/743_Self-critique_guided_iterative_reasoning_for_multi-hop_quest/review]] — 둘 다 LLM의 자기교정 능력을 다루지만 하나는 질의응답, 다른 하나는 도구 통합 추론에 중점을 둠
- 🔗 후속 연구: [[papers/610_Pelican_Correcting_Hallucination_in_Vision-LLMs_via_Claim_De/review]] — CRITIC의 도구 기반 자기 수정 프레임워크를 시각-언어 영역으로 확장하여 더 구조화된 검증 과정을 제공한다.
- 🔗 후속 연구: [[papers/636_Prompt_to_be_consistent_is_better_than_self-consistent_few-s/review]] — 도구 통합 자기 수정을 일관성 제약 조건과 결합하여 더 강력한 팩트 검증 시스템을 구축할 수 있다.
- 🏛 기반 연구: [[papers/790_Teaching_Large_Language_Models_to_Self-Debug/review]] — 자기 디버깅의 기본 개념이 도구 통합 자기 수정 시스템에서 더 포괄적인 오류 검출과 수정 능력을 구현하는 기초가 된다.
