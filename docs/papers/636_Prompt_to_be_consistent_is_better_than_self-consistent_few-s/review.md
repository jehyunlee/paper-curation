---
title: "636_Prompt_to_be_consistent_is_better_than_self-consistent_few-s"
authors:
  - "Fengzhu Zeng"
  - "Wei Gao"
date: "2023"
doi: "arXiv:2306.02569"
arxiv: ""
score: 4.0
essence: "본 논문은 사전학습 언어모델(PLM)의 일관성(consistency)을 명시적으로 강제하여 소수샘플(few-shot) 및 영샘플(zero-shot) 사실검증 성능을 향상시키는 **ProToCo** 방법을 제안한다. 클레임의 다양한 변형을 생성하고 이들 간의 논리적 일관성을 제약조건으로 활용하여 파라미터-효율적 미세조정(PEFT)을 수행한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Self-Refining_Text_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Singhal et al._2023_Prompt to be consistent is better than self-consistent few-shot and zero-shot fact verification wit.pdf"
---

# Prompt to be consistent is better than self-consistent? Few-shot and zero-shot fact verification with pre-trained language models

> **저자**: Fengzhu Zeng, Wei Gao | **소속**: Singapore Management University | **날짜**: 2023 | **DOI**: [arXiv:2306.02569](https://arxiv.org/abs/2306.02569)

---

## Essence

본 논문은 사전학습 언어모델(PLM)의 일관성(consistency)을 명시적으로 강제하여 소수샘플(few-shot) 및 영샘플(zero-shot) 사실검증 성능을 향상시키는 **ProToCo** 방법을 제안한다. 클레임의 다양한 변형을 생성하고 이들 간의 논리적 일관성을 제약조건으로 활용하여 파라미터-효율적 미세조정(PEFT)을 수행한다.

## Motivation

- **Known**: 사전학습 언어모델은 자체 일관성(self-consistency)을 보이지만, 이를 다운스트림 과제에 전이하기 어렵다는 것이 실증적으로 확인됨. 또한 대규모 학습데이터 수집이 어려운 새로운 도메인(예: COVID-19)에서의 사실검증이 어려움.

- **Gap**: 기존 few-shot 사실검증 방법들은 PLM의 암묵적 지식만 활용하거나 모델 파라미터를 업데이트하지 않아 일반화 성능이 낮음. Self-consistency 기반 방법(예: CoT)은 QA에 효과적이나 사실검증 과제에 직접 적용하기 부적절.

- **Why**: 사실검증에서 클레임과 그 변형(확인, 부정, 불확실성)들 사이에는 자연스러운 논리적 관계가 존재함. 이를 명시적 제약조건으로 활용하면 모델의 일관성을 개선할 수 있음.

- **Approach**: 프롬프트 템플릿 변형을 통해 클레임의 세 가지 변형(CON, NEG, UNC)을 생성하고, 이들 간의 논리적 일관성을 제약조건으로 설정한 후, T-Few 모델에 PEFT 방식으로 미세조정.

## Achievement

![Figure 2](figures/fig2.webp)
*ProToCo의 아키텍처: 클레임-증거 쌍에서 프롬프트 템플릿 변형을 통해 확인(CON), 불확실성(UNC), 부정(NEG) 변형을 생성하고, (IA)3를 이용한 PEFT로 모델 일관성 학습*

1. **Few-shot 성능**: 세 개의 공개 사실검증 데이터셋에서 최신 few-shot 기준선 대비 최대 30.4% 상대 F1 개선

2. **Zero-shot 성능**: 레이블 없는 인스턴스만으로도 강력한 영샘플 학습기 T0-3B를 지속적으로 상회

3. **대규모 모델 비교**: OPT-30B를 능가하고, Self-Consistency 기반 OPT-6.7B를 유의미하게 초과 (few-shot, zero-shot 모두)

## How

![Figure 1](figures/fig1.webp)
*일관성 메커니즘의 예시: 동일한 증거에 대해 원본, 확인, 부정, 불확실성 변형의 클레임에 대한 판단이 논리적으로 일치해야 함*

### 프롬프트 기반 변형 생성
- 입력 템플릿 T_x와 타겟 템플릿 T_y로 구성된 프롬프트 템플릿 T 정의
- 원본 클레임으로부터 세 가지 변형 자동 생성:
  - **확인 변형(CON)**: "it is true that [claim]"
  - **부정 변형(NEG)**: "it is false that [claim]"  
  - **불확실 변형(UNC)**: "it is unclear that [claim]"

### 일관성 제약조건 정의
- 증거가 Support하는 경우: CON=Support, NEG=Refute, UNC=NEI
- 증거가 Refute하는 경우: CON=Refute, NEG=Support, UNC=NEI
- 증거가 NEI인 경우: 모든 변형이 NEI

### 파라미터-효율적 미세조정
- T-Few 모델의 (IA)3 PEFT 방식 활용
- 원본 및 세 변형에 대한 일관성 제약이 있는 학습 데이터 구성
- 텍스트-투-텍스트 PLM(T5 기반)의 autoreggressive 생성 확률로 학습

## Originality

- **사실검증 맥락의 일관성**: 자체 일관성(self-consistency)이 아닌 **사실성-기반 일관성(factuality-grounded consistency)** 개념 도입. 클레임-증거 관계라는 도메인 특정 지식을 명시적으로 모델에 주입

- **프롬프트 기반 변형**: 복잡한 생성 메커니즘 없이 프롬프트 템플릿 변형만으로 일관성 학습용 데이터셋 자동 구성

- **PEFT 결합**: 프롬프트 기반 접근과 파라미터-효율적 미세조정의 조합으로 적은 학습 데이터에서 효율적 적응

- **일반성**: 특정 도메인 특화 없이 다양한 사실검증 데이터셋(FEVER, CovidFact, SCIFACT)에 적용 가능한 일반적 프레임워크

## Limitation & Further Study

- **개발셋 미사용 가정**: 데이터 부족 시나리오를 반영하기 위해 개발셋을 사용하지 않음. 실제 응용에서는 하이퍼파라미터 튜닝 어려움

- **일관성 메커니즘의 단순성**: 세 가지 변형에만 기한정. 더 복잡한 논리 관계(예: 다중 증거, 조건부 클레임)로 확장 가능성 제한

- **모델 크기 제약**: 주로 T-Few(T5 기반) 같은 소형~중형 PLM에 초점. 매우 대규모 모델(GPT-3, GPT-4)과의 상호작용 미분석

- **후속 연구**: (1) 다양한 논리 관계를 포함한 확장된 변형 생성, (2) 멀티홉(multi-hop) 사실검증으로 확장, (3) 크로스도메인 일반화 능력 강화

## Evaluation

- **Novelty**: 4/5 — 사실성-기반 일관성이라는 명확한 개념 도입이나, 일관성 제약 자체는 직관적이고 구현은 단순함

- **Technical Soundness**: 4/5 — 프롬프트 변형과 일관성 제약의 논리는 타당하나, 이론적 정당화가 제한적이며 hyperparameter 선택 근거 부족

- **Significance**: 4/5 — Few-shot 설정에서 실질적 개선과 실용적 가치가 있으나, zero-shot에서의 개선은 상대적으로 제한적(T0-3B 대비)

- **Clarity**: 4/5 — 전반적으로 명확하게 작성됨. 다만 일관성 제약의 일반화 규칙을 더 형식적으로 정의하면 좋을 듯

- **Overall**: 4/5

**총평**: 본 논문은 사실검증 과제의 내재적 논리 구조를 활용하여 명시적 일관성 제약을 통한 few-shot/zero-shot 학습을 효과적으로 구현했다. 프롬프트 기반의 간단하면서도 실용적인 접근이 돋보이나, 이론적 깊이와 확장성 측면에서는 개선 여지가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/790_Teaching_Large_Language_Models_to_Self-Debug/review]] — 언어모델의 일관성 강제와 자기 디버깅은 모두 자기 수정 메커니즘이지만, 논리적 제약과 실행 피드백이라는 다른 검증 방식을 사용한다.
- 🏛 기반 연구: [[papers/747_Selfcheck_Using_llms_to_zero-shot_check_their_own_step-by-st/review]] — LLM의 단계별 자기 검증 능력이 일관성 기반 팩트 체킹에서 논리적 제약 조건을 효과적으로 적용하기 위한 기본 전제가 된다.
- 🔗 후속 연구: [[papers/242_CRITIC_Large_Language_Models_Can_Self-Correct_with_Tool-Inte/review]] — 도구 통합 자기 수정을 일관성 제약 조건과 결합하여 더 강력한 팩트 검증 시스템을 구축할 수 있다.
- 🔗 후속 연구: [[papers/512_Lm-combiner_A_contextual_rewriting_model_for_chinese_grammat/review]] — Few-shot 일관성 개선 기법이 중국어 문법 오류 수정에서 과도한 수정 문제 해결에 적용될 수 있다.
- 🏛 기반 연구: [[papers/222_Clam_Selective_clarification_for_ambiguous_questions_with_ge/review]] — 일관성을 위한 프롬프트가 자기 일관성보다 효과적임을 보여 본 논문의 선택적 명확화 접근법의 이론적 근거를 제공한다.
- 🔄 다른 접근: [[papers/421_Improving_demonstration_diversity_by_human-free_fusing_for_t/review]] — 소수샷 학습에서 시연 다양성과 일관성 프롬프팅의 서로 다른 성능 향상 전략을 비교할 수 있습니다.
- 🏛 기반 연구: [[papers/790_Teaching_Large_Language_Models_to_Self-Debug/review]] — 자기 디버깅의 반복적 수정 메커니즘이 일관성 기반 팩트 체킹에서 논리적 제약 조건을 효과적으로 적용하기 위한 기본 프레임워크를 제공한다.
