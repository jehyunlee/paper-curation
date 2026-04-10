---
title: "747_Selfcheck_Using_llms_to_zero-shot_check_their_own_step-by-st"
authors:
  - "Ning Miao"
  - "Yee Whye Teh"
  - "Tom Rainforth"
date: "2023"
doi: "N/A"
arxiv: ""
score: 4.4
essence: "대규모 언어 모델(LLM)이 자체 단계별 추론에서 발생한 오류를 외부 자원 없이 인식할 수 있는지 탐구하며, 4단계 분해 검증 방식(SelfCheck)을 통해 제로샷(zero-shot) 오류 감지 및 답변 정확도 향상을 달성한 연구이다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Self-Refining_Text_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Miao et al._2023_Selfcheck Using llms to zero-shot check their own step-by-step reasoning.pdf"
---

# Selfcheck: Using llms to zero-shot check their own step-by-step reasoning

> **저자**: Ning Miao, Yee Whye Teh, Tom Rainforth | **날짜**: 2023 | **DOI**: N/A

---

## Essence

대규모 언어 모델(LLM)이 자체 단계별 추론에서 발생한 오류를 외부 자원 없이 인식할 수 있는지 탐구하며, 4단계 분해 검증 방식(SelfCheck)을 통해 제로샷(zero-shot) 오류 감지 및 답변 정확도 향상을 달성한 연구이다.

## Motivation

- **Known**: Chain-of-Thought(CoT) 프롬팅의 발명으로 LLM이 복잡한 문제를 단계별 추론으로 해결 가능해졌으나, GPT-4도 MATH 데이터셋에서 42.5%의 정확도에 불과할 정도로 오류가 빈번함. 기존 검증 방법들은 외부 검증 모델이나 소수 샷 학습(few-shot in-context learning)을 요구하여 실용성 제한.

- **Gap**: 추가 훈련 데이터나 도메인 특화 예제 없이 LLM 자체만으로 자신의 추론 오류를 인식할 수 있는 범용 제로샷 검증 방법이 부재. 직접적인 "정답 확인" 요청은 90% 이상의 확률로 오답도 정답으로 표시.

- **Why**: 다중 단계 추론에서 개별 단계의 오류율이 낮아도 누적되면 최종 정답이 틀릴 확률이 높음. 따라서 자동으로 오류를 식별하고 신뢰도 점수를 제공하는 메커니즘이 필요.

- **Approach**: LLM의 생성 능력을 활용하되, 검증 과정을 목표 추출(target extraction) → 정보 수집(information collection) → 단계 재생성(step regeneration) → 결과 비교(result comparison)의 4단계로 분해하여 각 단계의 난이도를 낮추고 상관관계 있는 오류를 감소.

## Achievement

![Figure 1](figures/fig1.webp)
*SelfCheck의 구체적 실행 예시: 5번 단계의 정사각형 완성(completing the square) 검증 과정을 4단계로 분해하여 수행*

1. **오류 인식 성능**: GSM8K, MathQA, MATH 데이터셋의 세 수학 과제 모두에서 단순 다수결 투표(majority voting) 대비 최종 정답 정확도 대폭 상승. 낮은 신뢰도 솔루션 필터링 시 부정답 비율을 9%, 22.8%, 16.2% 감소.

2. **신뢰도 점수의 유효성**: SelfCheck가 제공하는 신뢰도 점수를 가중치로 사용한 가중 투표(weighted voting)를 통해 정답 정확도 향상. 신뢰도 점수가 실제 정답 여부와 의미 있는 상관관계 보유.

## How

![Figure 1](figures/fig1.webp)
*단계 검증의 4단계 분해 프로세스*

### 핵심 방법론

- **4단계 분해 구조의 설계 이유**: 
  - 직접 "정답 확인" 요청은 LLM이 동시에 처리해야 할 여러 측면(내용 이해, 맥락 정보 수집, 정확성 판단)이 많아 비효과적
  - "검증"은 LLM 훈련 말뭉치에서 상대적으로 드물어 LLM의 강점과 부합하지 않음
  - 분해를 통해 각 단계를 LLM의 생성 능력에 더 적합한 작업으로 전환

- **목표 추출(Target Extraction)**: 현재 단계의 핵심 목적 파악 ("직선의 기울기 계산", "제곱 완성" 등)

- **정보 수집(Information Collection)**: 해당 단계가 직접 의존하는 선행 단계 및 조건 식별

- **단계 재생성(Step Regeneration)**: 추출된 목표와 수집된 정보만으로 독립적인 대체 단계 생성. 원본 생성의 오류와 재생성의 오류 간 상관관계 최소화

- **결과 비교(Result Comparison)**: 원본 단계와 재생성 단계의 일치도 비교. 일치 시 단계 통과, 불일치 시 오류 가능성 높음으로 판단

- **신뢰도 점수 통합**: 개별 단계 검증 결과를 종합하여 전체 솔루션에 대한 [0,1] 범위의 신뢰도 점수 w 산출

- **가중 투표**: 동일 질문의 여러 솔루션에 대해 신뢰도 점수를 가중치로 사용하여 최종 답변 선택

## Originality

- **새로운 4단계 분해 프레임워크**: 직접 검증 방식의 근본적인 한계를 인식하고, LLM의 생성 강점을 활용하는 창의적 대안 제시

- **제로샷 일반성**: 추가 훈련, 미세조정(finetuning), 도메인 특화 예제 불필요. 기존 방법들(Few-shot verification, External resources, Training verifier)과 달리 즉시 적용 가능

- **오류 상관관계 감소 전략**: 재생성을 통해 원본과 검증의 독립적인 오류를 유도하는 통찰

- **인간 검증 프로세스 모방**: "자신의 풀이를 다시 확인한다"는 휴리스틱을 체계화

## Limitation & Further Study

- **재생성의 일관성 문제**: 동일한 목표와 정보로도 LLM이 매번 다른 결과를 생성할 수 있으며, 이것이 검증 정확도에 영향. 재생성 결과의 변동성 관리 방안 필요

- **복합 단계 처리**: 여러 작업을 동시에 수행하는 복합 단계의 경우 목표 추출 및 정보 수집이 불완전할 가능성

- **도메인 일반화**: 수학 문제 중심의 평가. 상식 추론(commonsense reasoning), 문학 분석 등 다른 영역에서의 효과성 미검증

- **계산 비용**: 각 단계마다 4번의 추가 LLM 호출 필요로 계산량 증가 (솔루션 당 4n번의 호출, n=단계 수)

- **명시적 오류 분류 부재**: 오류 인식만 가능하고 오류 유형(논리 오류, 계산 오류, 개념 오류) 분류 불가

- **향후 연구 방향**: 
  - 여러 모델 간 검증 가능성 탐구
  - 더 복잡한 추론 작업(증명, 코딩)으로 확장
  - 재생성 다양성 활용한 앙상블 방법 개발
  - 계산 비용 감소 방안

## Evaluation

| 항목 | 평가 |
|------|------|
| Novelty | 4.5/5 |
| Technical Soundness | 4/5 |
| Significance | 4.5/5 |
| Clarity | 4.5/5 |
| Overall | 4.4/5 |

**총평**: 이 논문은 LLM 자체검증의 오랜 난제를 창의적인 4단계 분해 방식으로 해결하며, 제로샷 범용성과 실제 정확도 향상을 동시에 달성한 실질적 기여를 한다. 다만 계산 비용 증가와 수학 문제 중심의 평가가 한계이며, 향후 더 광범위한 도메인과 오류 분류 체계 개발이 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/172_Boolq_Exploring_the_surprising_difficulty_of_natural_yesno_q/review]] — 자연 예/아니오 질문의 어려움을 보인 연구에서 LLM이 자체 추론을 검증할 수 있는지로 확장한 더 고차원적 연구입니다.
- 🔄 다른 접근: [[papers/746_Self-Refine_Iterative_Refinement_with_Self-Feedback/review]] — 자체 검증과 자체 개선이라는 서로 다른 LLM 자기 향상 메커니즘을 탐구하는 상호 보완적 연구입니다.
- 🔗 후속 연구: [[papers/242_CRITIC_Large_Language_Models_Can_Self-Correct_with_Tool-Inte/review]] — 도구를 활용한 자기 수정에서 도구 없이 순수하게 자체 추론을 검증하는 더 순수한 형태의 자기 검증 연구입니다.
- 🏛 기반 연구: [[papers/172_Boolq_Exploring_the_surprising_difficulty_of_natural_yesno_q/review]] — 자연어 예/아니오 질문의 도전성을 보인 연구가 LLM의 자체 추론 검증 능력 연구의 기초적 동기를 제공합니다.
- 🔄 다른 접근: [[papers/222_Clam_Selective_clarification_for_ambiguous_questions_with_ge/review]] — LLM의 단계별 자기 점검 방법으로 본 논문의 애매한 질문 처리와 다른 접근법의 품질 보장을 제시한다.
- 🏛 기반 연구: [[papers/636_Prompt_to_be_consistent_is_better_than_self-consistent_few-s/review]] — LLM의 단계별 자기 검증 능력이 일관성 기반 팩트 체킹에서 논리적 제약 조건을 효과적으로 적용하기 위한 기본 전제가 된다.
