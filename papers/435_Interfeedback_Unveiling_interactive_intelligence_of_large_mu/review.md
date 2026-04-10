---
title: "435_Interfeedback_Unveiling_interactive_intelligence_of_large_mu"
authors:
  - "Henry Hengyuan Zhao"
  - "Wenqi Pei"
  - "Yifei Tao"
  - "Haiyang Mei"
  - "Mike Zheng Shou"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "대형 다중모달 모델(LMM)이 인간의 피드백을 통해 자신의 응답을 개선할 수 있는 상호작용 능력을 평가하는 최초의 벤치마크를 제시한다. 기존 벤치마크들이 정적 평가에 집중한 반면, 본 연구는 대화형 인간-AI 상호작용 시나리오에서의 모델 성능을 측정한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Multimodal_Scientific_Benchmarks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhao et al._2025_Interfeedback Unveiling interactive intelligence of large multimodal models via human feedback.pdf"
---

# InterFeedback: Unveiling interactive intelligence of large multimodal models via human feedback

> **저자**: Henry Hengyuan Zhao, Wenqi Pei, Yifei Tao, Haiyang Mei, Mike Zheng Shou | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: 대화형 피드백 시나리오 예시. 모델이 잘못된 응답을 생성할 때 인간 사용자가 관련 피드백을 제공하여 답변을 상호작용적으로 개선함*

대형 다중모달 모델(LMM)이 인간의 피드백을 통해 자신의 응답을 개선할 수 있는 상호작용 능력을 평가하는 최초의 벤치마크를 제시한다. 기존 벤치마크들이 정적 평가에 집중한 반면, 본 연구는 대화형 인간-AI 상호작용 시나리오에서의 모델 성능을 측정한다.

## Motivation

- **Known**: 최신 LMM들(GPT-4o, Qwen2-VL, LLaVA 등)은 단일 라운드 다중모달 과제 해결에서 탁월한 성능을 보임
- **Gap**: 기존 벤치마크들은 LMM의 정적 문제해결 능력만 평가하며, 인간 피드백을 통한 점진적 개선 능력은 거의 평가되지 않음
- **Why**: 일반적인 AI 어시스턴트 개발에는 두 가지 핵심 능력이 필요: (1) 우수한 문제해결 능력 (2) 피드백을 통한 자기 개선 능력. 현재 이 두 번째 능력은 충분히 검토되지 않았음
- **Approach**: 프로프라이터리 모델(GPT-4o)을 인간 역할로 사용하여 자동화된 피드백을 생성하고, 테스트 데이터를 정확히 선별하는 InterFeedback 프레임워크 제안

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: InterFeedback-Bench의 테스트 데이터 구성 프로세스. 각 LMM별로 피드백 수신자가 실패한 사례(음성 집합)와 피드백 제공자가 성공한 사례(양성 집합)의 교집합을 선별*

1. **InterFeedback 프레임워크**: 모든 LMM과 데이터셋에 적용 가능한 확장성 있는 상호작용 평가 프레임워크 개발. POMDP(부분 관찰 가능 마르코프 결정 과정) 형식으로 상호작용 문제해결 과정을 수식화

2. **InterFeedback-Bench 벤치마크**: MMMU-Pro(1,730개)와 MathVerse(3,940개) 데이터셋을 이용하여 10개의 오픈소스 LMM 평가, 그리고 GPT-4o, OpenAI-o1, Claude-Sonnet-4 등 4개 프로프라이터리 모델의 인간 평가 수행

3. **InterFeedback-Human 데이터셋**: 프로프라이터리 모델의 상호작용 성능을 수동으로 테스트하기 위해 120개 사례로 구성된 새로운 수집 데이터셋 제시

4. **주요 발견**: 
   - OpenAI-o1을 포함한 최신 모델도 피드백 기반 응답 개선에서 평균 50% 미만의 성능을 보임
   - 대부분의 LMM이 피드백 해석 및 통합에 최적화되지 않은 성능 발휘
   - 고품질 피드백의 중요성: 낮은 품질의 피드백은 단순 이진 정확성 신호보다도 더 성능을 저하시킴
   - 모델이 진정한 추론보다는 추측에 의존하는 경우 발견

## How

![Figure 3](figures/fig3.webp)
*그림 3: 모델의 자기개선 능력을 평가하기 위한 제안된 InterFeedback 프레임워크 개요*

### 자동화된 상호작용 벤치마킹 (Automated Interactive Benchmarking)

- **POMDP 형식화**: 자연어 질문 q와 이미지 v를 입력으로 받아, 모델이 관찰(O)에서 상태(S)를 인식하고 행동(A)을 생성. 보상 함수 R은 예측 답변과 정답의 정확도 매칭(0 또는 1)을 반환

- **데이터 선별 프로세스**: 
  - 피드백 수신자(Mr) LMM이 실패한 과제들의 음성 집합(Un) 구성
  - 피드백 제공자(Mp) LMM이 성공한 과제들의 양성 집합(Up) 구성
  - 교집합(Utest = Un ∩ Up) 선별을 통해 신뢰할 수 있는 피드백만 사용

- **InterFeedback 프레임워크**: 
  - 피드백 수신자(Mr): 평가 대상 LMM으로 다중 라운드 상호작용 수행
  - 피드백 제공자(Mp): 프로프라이터리 모델(GPT-4o, Claude)이 인간 피드백 시뮬레이션
  - 반복 라운드를 통해 모델이 피드백을 통합하고 개선된 답변 생성

### 인간 기반 평가 (Human-based Evaluation)

- **InterFeedback-Human 데이터셋**: 120개의 수동 선별 사례로 구성된 검증 데이터셋
- **학습된 사용자(Trained User)**: 인간 평가자가 직접 피드백 제공하여 모델의 실제 상호작용 능력 평가
- **피드백 제공 전략**: 모델의 오류 유형에 맞춤형 피드백 제공으로 신뢰성 있는 평가 보장

## Originality

- **최초 시도**: LMM의 인간 피드백을 통한 상호작용 개선 능력을 체계적으로 평가하는 첫 벤치마크 제시
- **신뢰성 있는 피드백 생성**: 기존 사용자 시뮬레이션 연구와 달리, 교집합 선별을 통해 피드백 제공자의 신뢰성 보장 (음성/양성 집합 교차 검증)
- **POMDP 형식화**: 다중 라운드 상호작용 문제해결을 엄격한 수학적 틀로 표현
- **다층적 평가**: 자동화된 벤치마크와 인간 평가를 결합하여 종합적 검증
- **광범위한 모델 커버리지**: 오픈소스(10개) 및 프로프라이터리 모델(4개) 모두 평가

## Limitation & Further Study

- **제한사항**:
  - 피드백 제공자(Mp)의 정확성 자체가 제한되므로, 완벽한 피드백을 보장하지 못함 (MMMU-Pro에서 GPT-4o도 64.7% 정확도)
  - 교집합 선별 방식으로 인해 각 모델별 테스트 데이터셋이 상이하여 직접 비교의 공정성 문제 가능
  - 피드백 형식이 자연언어로 제한되어, 시각적 피드백이나 다른 상호작용 양식은 미포함
  - 인간 평가(InterFeedback-Human)의 샘플 수가 120개로 상대적으로 제한적

- **후속 연구 방향**:
  - LMM의 피드백 이해 및 통합 능력을 향상시키는 새로운 학습 방법(fine-tuning, instruction tuning) 개발
  - 다양한 피드백 유형(정정, 설명, 시각적 힌트)의 효과 분석
  - 더 큰 규모의 인간 평가 데이터셋 구축으로 벤치마크 확장
  - 모델의 진정한 추론 능력 vs. 추측 행동을 구분하는 진단 방법 개발

## Evaluation

- **Novelty (독창성)**: 4.5/5
  - 인간 피드백을 통한 LMM의 상호작용 개선 능력을 평가하는 첫 체계적 접근
  - 교집합 선별을 통한 신뢰할 수 있는 자동 피드백 생성 방법이 독창적
  - 다만, 기존의 사용자 시뮬레이션 기술을 활용한 점에서 완전히 새로운 방법론은 아님

- **Technical Soundness (기술적 타당성)**: 4/5
  - POMDP 형식화가 명확하고 수학적으로 엄밀함
  - 데이터 선별 프로세스가 체계적이고 합리적
  - 다만, 교집합 선별로 인한 테스트셋 불균형과 편향 가능성에 대한 심층 분석 부족

- **Significance (중요성)**: 4.5/5
  - LMM의 실제 응용(AI 어시스턴트) 관점에서 중요한 능력(피드백 수용성) 평가
  - 광범위한 모델 평가로 산업계에 실질적 인사이트 제공
  - 다만, 현재 모든 모델의 저조한 성능이 개선 가능성과 실용성을 다소 제한

- **Clarity (명확성)**: 4/5
  - 전체 프레임워크와 파이프라인이 명확하게 설명됨
  - Figure 2의 데이터 구성 프로세스 설명이 직관적
  - 다만, 일부 구현 세부사항(예: 피드백 프롬프트 설계, 라운드 수 결정 기준)이 불충분

- **Overall (종합)**: 4.2/5

**총평**: 본 논문은 LMM의 상호작용 지능을 평가하는 중요하면서도 미개척된 영역에 최초로 접근하며, 자동화된 벤치마크와 인간 평가를 결합한 포괄적 평가 방법론을 제시한다. 다만, 현재 모든 모델의 낮은 성능과 피드백 제공자의 완벽성 미달 문제는 벤치마크의 실용성을 다소 제한하며, 후속 연구에서 모델 개선 방법론이 함께 제시되어야 할 것으로 판단된다.

## Related Papers

- 🏛 기반 연구: [[papers/538_Mind_the_gap_Examining_the_self-improvement_capabilities_of/review]] — LLM의 자기개선 능력 분석이 인간 피드백 기반 상호작용 능력 평가의 이론적 기반
- 🔗 후속 연구: [[papers/722_Scifibench_Benchmarking_large_multimodal_models_for_scientif/review]] — 정적 과학 그림 해석 평가를 대화형 피드백 기반 개선 능력으로 확장한 연구
- 🔄 다른 접근: [[papers/242_CRITIC_Large_Language_Models_Can_Self-Correct_with_Tool-Inte/review]] — 도구 기반 자기수정과 달리 인간 피드백을 통한 상호작용적 개선 능력에 집중
- 🧪 응용 사례: [[papers/1127_MMSD20_Towards_a_Reliable_Multi-modal_Sarcasm_Detection_Syst/review]] — 멀티모달 풍자 탐지에서 인간 피드백을 활용한 모델 개선 능력 평가에 적용 가능
- 🔗 후속 연구: [[papers/538_Mind_the_gap_Examining_the_self-improvement_capabilities_of/review]] — 자기개선 메커니즘 분석을 인간-AI 상호작용에서의 피드백 활용 능력으로 확장
- 🔗 후속 연구: [[papers/158_Biasfilter_An_inference-time_debiasing_framework_for_large_l/review]] — 인간 피드백 기반 개선을 편향 제거라는 구체적 목표로 특화한 확장
- 🔄 다른 접근: [[papers/336_FigCaps-HF_A_Figure-to-Caption_Generative_Framework_and_Benc/review]] — 멀티모달 상호작용과 달리 과학 그림 캡션 생성에 특화된 인간 피드백 활용
- 🏛 기반 연구: [[papers/223_Clarify_when_necessary_Resolving_ambiguity_through_interacti/review]] — 대규모 모델의 인터랙티브 지능에 대한 연구가 사용자 의도 엔트로피 추정과 명확화 필요성 판단의 이론적 배경을 제공함
- 🧪 응용 사례: [[papers/1127_MMSD20_Towards_a_Reliable_Multi-modal_Sarcasm_Detection_Syst/review]] — 멀티모달 풍자 탐지에서 인간 피드백을 통한 모델 성능 개선 능력 평가에 적용
