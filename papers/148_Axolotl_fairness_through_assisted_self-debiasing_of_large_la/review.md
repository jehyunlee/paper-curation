---
title: "148_Axolotl_fairness_through_assisted_self-debiasing_of_large_la"
authors:
  - "Sana Ebrahimi"
  - "Kaiwen Chen"
  - "Abolfazl Asudeh"
  - "Gautam Das"
  - "Nick Koudas"
date: "2024"
doi: "N/A"
arxiv: ""
score: 3.9
essence: "AXOLOTL은 대규모언어모델(LLM)의 출력물에서 편향을 식별하고 자체 수정하도록 유도하는 포스트프로세싱 프레임워크로, 모델 내부 파라미터에 접근하지 않고 공개 API만을 이용하여 계산 비용을 최소화하면서 편향 완화를 실현한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Self-improving_Reward_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ebrahimi et al._2024_Axolotl fairness through assisted self-debiasing of large language model outputs.pdf"
---

# Axolotl: fairness through assisted self-debiasing of large language model outputs

> **저자**: Sana Ebrahimi, Kaiwen Chen, Abolfazl Asudeh, Gautam Das, Nick Koudas | **날짜**: 2024 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*시스템 아키텍처: 편향 방향 식별 → 불쾌한 특성 식별 → 쾌적한 해결책 제시 → 새로운 프롬프트 생성*

AXOLOTL은 대규모언어모델(LLM)의 출력물에서 편향을 식별하고 자체 수정하도록 유도하는 포스트프로세싱 프레임워크로, 모델 내부 파라미터에 접근하지 않고 공개 API만을 이용하여 계산 비용을 최소화하면서 편향 완화를 실현한다.

## Motivation

- **Known**: 사전학습된 LLM은 학습 데이터에 내재된 성별, 인종, 직업 등 다양한 형태의 편향을 상속받아 불공정한 결과를 초래함
- **Gap**: 기존 편향 완화 기법들(재학습, 토큰 분포 조정, 임베딩 수정 등)은 높은 계산 비용, 모델 성능 저하, 모델 내부 구조 접근 필수라는 근본적 제약이 있음
- **Why**: 폐쇄형 LLM 서비스(GPT 등)가 증가하고 있으며, 저비용·고효율의 편향 완화 기법의 필요성이 증대됨
- **Approach**: 모델을 블랙박스로 취급하고 임베딩 벡터 기반 편향 감지 후 모델 자체의 재작성 능력을 활용한 자체-편향제거(self-debiasing) 유도

## Achievement

1. **모델-무종속성(Model-agnostic) 달성**: OpenAI, Llama 2 등 다양한 LLM에 적용 가능하며 사전학습/미세조정 불필요
2. **다중 민감 속성 지원**: 성별(binary/non-binary), 인종, 직업 등 여러 민감 속성과 민감 그룹을 동시에 처리 가능
3. **공개 API 기반 운영**: 모델 내부 파라미터 접근 없이 API 호출만으로 동작하여 계산 비용 극소화
4. **세 단계 제로샷 프로세스**: (1)편향 방향 식별 → (2)불쾌한 특성 감지 → (3)쾌적한 대안 제시를 통해 체계적 편향 완화

## How

![Figure 1](figures/fig1.webp)

**단계 1: 편향 방향 식별 (Bias Orientation Detection)**
- 모델 출력 r의 임베딩 벡터 v⃗ᵣ과 각 민감 그룹 g⃗ₖ 간 코사인 유사도 계산
- 유사도 > ε 이면 특정 그룹에 대한 방향성 편향으로 판정
- 수식: k = arg max β_r(g⃗ᵢ), orientation(r) = gₖ if β_r(g⃗ₖ) ≥ ε

**단계 2: 불쾌한 특성 식별 (Unpleasant Characteristic Detection)**
- May et al. (2019)의 그룹별 불쾌-쾌적 단어 집합(T⁻, T⁺) 활용
- 출력 r과 불쾌 단어 w⁻ 간 최대 유사도 > ε 이면 해당 특성이 편향 원인으로 식별
- 수식: w⁻ = arg max cos(v⃗ᵣ, t⃗) for t⃗ ∈ T⁻ₖ

**단계 3: 쾌적한 해결책 제시 (Pleasant Resolution)**
- 수정 벡터 u⃗*를 계산하여 v⃗ᵣ + u⃗*가 w⃗⁻과 직교하도록 설정
- 벡터 거부 공식(vector rejection formula) 사용: u⃗* = (u⃗₁/||u⃗₁|| - v⃗₁)
- 가장 가까운 쾌적 단어 w⁺ 선택: arg max cos(w⃗, u⃗*)

**단계 4: 자체-편향제거 유도 (Self-Debiasing)**
- 식별된 편향 방향, 불쾌 특성, 쾌적 대안을 포함한 재작성 지시문 생성
- LLM이 원래 출력을 재생성하되 쾌적한 표현으로 대체하도록 유도

## Originality

- **최초 구현**: 블랙박스 LLM에 대한 재학습 없는 포스트프로세싱 편향 완화 기법 최초 제시
- **임베딩 기반 편향 감지**: 기존 방법의 복잡한 통계 분석 대신 임베딩 유사도와 벡터 기하학 활용
- **모델 자체 능력 활용**: LLM의 자연스러운 재작성 능력을 편향 완화에 활용하는 창의적 접근
- **민감 속성의 유연성**: 이진 그룹뿐 아니라 다중-값 민감 속성(다양한 인종, 직업) 처리 가능

## Limitation & Further Study

- **선택된 단어 집합의 문제**: T⁺, T⁻의 기선택 단어들이 문화적·맥락적 편향을 가질 수 있으며, 새로운 민감 속성 추가 시 수동 큐레이션 필요
- **임베딩 모델 의존성**: INSTRUCTOR 임베딩의 품질에 크게 의존하며, 임베딩 모델 자체의 편향이 전파될 수 있음
- **상위수준 편향 미처리**: 문장-수준 임베딩 분석으로 인해 문서 수준이나 다회차 상호작용에서의 편향 놓칠 수 있음
- **평가 지표 제약**: Toxicity, Regard 지표가 모든 형태의 편향(예: 미묘한 표현 편향) 포착 불가
- **비용-성능 트레이드오프**: 추가 API 호출로 인한 지연시간 증가 및 장기 실시간 애플리케이션 적용성 미검증

**후속 연구 방향**:
- 자동화된 T⁺, T⁻ 생성 메커니즘 개발
- 다중 문화권, 다중 언어 환경에서의 일반화 연구
- 대화형 장기문맥에서의 누적 편향 완화 기법 개발


## Evaluation

- Novelty: 4/5
- Technical Soundness: 3.5/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 3.9/5

**총평**: AXOLOTL은 블랙박스 LLM에 대한 실용적이고 비용 효율적인 편향 완화 기법을 제시한 혁신적 작업이나, 사전 정의된 단어 집합의 한계와 임베딩 모델 의존성이 장기 적용성을 제약한다. 공개 API 기반 접근은 산업적 가치가 높으나, 기술적 견고성과 평가 범위 확대가 필요하다.

## Related Papers

- ⚖️ 반론/비판: [[papers/471_Large_Language_Models_Cannot_Self-Correct_Reasoning_Yet/review]] — AXOLOTL이 LLM의 자체 편향 수정을 가능하다고 주장하는 반면, 이 논문은 LLM이 아직 추론에서 자체 수정을 할 수 없다고 반박한다.
- 🔄 다른 접근: [[papers/158_Biasfilter_An_inference-time_debiasing_framework_for_large_l/review]] — 둘 다 LLM의 편향 완화를 다루지만 하나는 사후처리 자체 편향 제거에, 다른 하나는 추론 시점 편향 필터링에 초점을 맞춘다.
- 🏛 기반 연구: [[papers/846_TrustLLM_Trustworthiness_in_Large_Language_Models/review]] — 대규모 언어 모델의 신뢰성에 대한 종합적인 평가 프레임워크가 AXOLOTL의 편향 완화 효과를 체계적으로 검증하는 기반을 제공한다.
