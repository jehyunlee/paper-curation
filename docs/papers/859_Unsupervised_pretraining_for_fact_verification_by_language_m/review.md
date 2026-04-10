---
title: "859_Unsupervised_pretraining_for_fact_verification_by_language_m"
authors:
  - "Adrián Bazaga"
  - "Píetro Lió"
  - "Gos Micklem"
date: "2023"
doi: ""
arxiv: ""
score: 4.3
essence: "본 논문은 **SFAVEL(Self-supervised Fact Verification via Language Model Distillation)**을 제안하여, 인간의 주석 없이 사전학습된 언어모델의 지식을 증류(distillation)함으로써 클레임과 근거 간의 의미론적 정렬을 학습하는 자기지도학습 기반 팩트 검증 프레임워크를 소개한다. 이는 FB15k-237에서 +5.3% Hits@1, FEVER에서 +8% 정확도 개선을 달성했다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Fact_Verification_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Bazaga et al._2023_Unsupervised pretraining for fact verification by language model distillation.pdf"
---

# Unsupervised pretraining for fact verification by language model distillation

> **저자**: Adrián Bazaga, Píetro Lió, Gos Micklem | **날짜**: 2023 | **소속**: University of Cambridge

---

## Essence

본 논문은 **SFAVEL(Self-supervised Fact Verification via Language Model Distillation)**을 제안하여, 인간의 주석 없이 사전학습된 언어모델의 지식을 증류(distillation)함으로써 클레임과 근거 간의 의미론적 정렬을 학습하는 자기지도학습 기반 팩트 검증 프레임워크를 소개한다. 이는 FB15k-237에서 +5.3% Hits@1, FEVER에서 +8% 정확도 개선을 달성했다.

## Motivation

- **Known**: 기존 팩트 검증 연구는 주로 NLI(Natural Language Inference) 모델이나 지식그래프 기반 방법론에 의존하며, 대규모 주석 데이터셋(FEVER, MultiFC 등)을 필요로 한다. 사전학습 언어모델은 강력한 의미 이해 능력을 보유하지만 할루시네이션(hallucination) 문제를 겪는다.

- **Gap**: 기존 팩트 검증 방법들은 대부분 지도학습에 의존하고 있으며, 자기지도학습 기반의 팩트 검증 기법은 여전히 부족하다. 또한 LaPraDoR 같은 일반적인 대비 학습 방법은 작업별 특화성이 부족하여 FEVER에서 지도학습 SOTA와 큰 성능차를 보인다.

- **Why**: 방대한 미표지 데이터를 활용하면서도 주석 비용을 제거할 수 있는 자기지도학습 접근법이 필요하며, 팩트 검증 작업에 특화된 대비 손실함수의 설계가 중요하다.

- **Approach**: 사전학습된 언어모델의 특징을 지식그래프 임베딩 공간으로 증류(distillation)하는 새로운 자기지도학습 프레임워크를 제안한다. 클레임-사실 정렬(alignment)을 위한 작업별 맞춤형 손실함수(distillation loss, scoring loss, intra-sample contrastive loss)를 설계한다.

## Achievement

1. **SOTA 성능 달성**: FB15k-237에서 Hits@1 기준 +5.3% 개선, FEVER에서 +8% 정확도 향상으로 선형평가(linear evaluation) 기준 새로운 SOTA 달성

2. **주석 불필요한 자기지도학습**: 인간의 레이블 없이 순전히 자기지도학습만으로 우수한 성능 달성, 대규모 미표지 데이터 활용 가능

3. **언어모델 증류의 효과성**: 8개 사전학습 언어모델의 의미론적 지식을 효과적으로 지식모델 공간으로 이전하며, 작업 특화 설계의 중요성을 입증

## How

![Figure 1: SFAVEL 프레임워크 개요 - (a) 자기지도학습 기반 언어모델 증류 사전학습 과정을 보여주며, 고정된 언어모델로부터 클레임 임베딩을 획득하고, 지식모델로 사실 임베딩을 생성한 후, 스코어링 모듈이 근거를 점수화하고, 세 가지 손실함수(증류, 스코어링, 대비)를 결합하여 최적화한다.](figures/fig1.webp)

**데이터 처리 파이프라인**:
- 미표지 클레임 배치 x = {xᵢ}ₙᵢ₌₁과 지식그래프 G(ε, R) (엔티티와 관계 포함) 사용
- 사실 F는 (head, relation, tail) 삼중항으로 표현

**사전학습 방법론**:
- **언어모델 인코더(Frozen)**: 입력 클레임으로부터 X_LM 특징 획득 (8개 SOTA 사전학습 모델 중 선택)
- **지식모델**: 지식그래프의 모든 사실을 고차원 임베딩 X_F로 변환
- **스코어링 모듈**: 클레임 임베딩을 조건으로 하여 각 사실에 대한 점수 S ∈ [0,1] 생성
- **상위-K 증거 선택**: 점수가 높은 상위 K개 사실을 양성 부분그래프 X_F⁺로 선택
- **음성 풀**: 임의로 샘플링된 사실들로 음성 풀 구성

**세 가지 손실함수 조합**:
1. **증류 손실(ℒ_distill)**: 클레임과 양성 사실 임베딩 간 대비 손실로 언어모델 지식을 지식모델 공간으로 증류
2. **스코어링 손실(ℒ_scoring)**: 양성 사실에 높은 점수, 음성 사실에 낮은 점수를 부여하도록 스코어링 모듈 학습
3. **대비 손실(ℒ_intra)**: 동일 클레임의 양성 사실들 간 의미 관계 보존, 코사인 유사도 기반 대비 학습

**선택적 미세조정**: 사전학습된 모델을 지도학습 팩트 검증 분류 작업에 미세조정 가능

## Originality

- **작업별 특화 설계**: 일반적인 대비 학습과 달리 팩트 검증의 클레임-사실 정렬 문제에 특화된 삼중 손실함수 설계로 LaPraDoR 등 기존 방법의 성능 격차 해소

- **다중 언어모델 지식 통합**: 단일 모델이 아닌 8개 SOTA 사전학습 모델의 의미론적 지식을 체계적으로 지식그래프 임베딩으로 증류하는 프레임워크

- **의미 관계 보존**: 단순 대비 학습을 넘어 코퍼스 전체 의미 관계를 보존하면서 클레임-증거 정렬을 달성하는 대비 손실함수 개발

- **엔드투엔드 자기지도 파이프라인**: 주석 없이 미표지 데이터만으로 완전한 사전학습 가능한 자기지도 학습 프레임워크 (기존의 반지도/지도학습 방식과 차별화)

## Limitation & Further Study

**한계**:
- 지식그래프의 품질과 커버리지에 의존: 지식베이스에 존재하지 않는 사실 검증에는 한계
- 고정된 언어모델 사용: 지식모델과의 동적 상호작용 불가능
- 상위-K 임계값 선택의 영향: Figure 3에서 K 값에 따른 성능 편차 존재
- 계산 효율성: 8개 모델 앙상블의 추론 시간 및 메모리 오버헤드 미상세

**후속 연구**:
- 동적 언어모델 미세조정과 지식모델의 공동 학습 메커니즘
- 다중 언어 데이터셋(MultiFC 등)으로의 확장 및 언어 간 전이 성능 평가
- 희소 지식그래프 환경에서의 성능 개선 (예: 관계 예측과의 통합)
- 대규모 언어모델의 할루시네이션 감소에 미치는 영향 정량화

## Evaluation

- **Novelty (독창성)**: 4.5/5 – 자기지도학습을 팩트 검증에 적용한 것은 참신하며, 작업 특화 손실함수 설계가 우수하나, 언어모델 증류 자체는 기존 기법의 조합으로 볼 여지 있음

- **Technical Soundness (기술적 타당성)**: 4.5/5 – 삼중 손실함수의 설계가 명확하고 이론적으로 타당하며, 광범위한 실험과 절제 연구(ablation study)로 검증되었으나, 일부 설계 선택의 정당화가 충분하지 않음 (예: K값 선택, 음성 샘플링 전략)

- **Significance (중요성)**: 4.5/5 – FEVER와 FB15k-237에서 SOTA 달성으로 실질적 성과이며, 주석 불필요한 자기지도 접근법은 확장성 측면에서 중요하나, 지식그래프 의존성으로 인한 실제 적용 범위에 제약

- **Clarity (명확성)**: 4/5 – Figure 1과 방법론이 전반적으로 명확하나, 스코어링 모듈의 아키텍처 세부사항, 특정 하이퍼파라미터 선택 근거 등 구현 세부사항이 다소 부족함

- **Overall**: 4.3/5

**총평**: SFAVEL은 팩트 검증에 특화된 자기지도학습 프레임워크로 SOTA 성능을 달성했으며, 주석 불필요한 확장 가능한 접근법을 제시한 의미 있는 기여이다. 다만 지식그래프 의존성과 설계 선택의 이론적 깊이가 보강된다면 더욱 강력한 연구가 될 수 있다.

## Related Papers

- 🔄 다른 접근: [[papers/832_Towards_llm-based_fact_verification_on_news_claims_with_a_hi/review]] — SFAVEL은 언어모델 증류를 통한 무감독 접근을, HiSS는 계층적 단계별 프롬프팅을 사용하여 서로 다른 방식으로 팩트 검증 문제를 해결함
- 🔗 후속 연구: [[papers/332_Fact-checking_complex_claims_with_program-guided_reasoning/review]] — 프로그램 가이드 추론을 통한 복잡한 클레임 검증이 SFAVEL의 기본적인 클레임-근거 정렬 학습을 더 정교한 추론 체계로 발전시킨 연구임
- ⚖️ 반론/비판: [[papers/541_Missing_counter-evidence_renders_nlp_fact-checking_unrealist/review]] — 반박 증거의 부재가 NLP 팩트 체킹을 비현실적으로 만든다는 지적이 SFAVEL의 자기지도학습 접근법의 한계를 보여줌
- 🏛 기반 연구: [[papers/183_Can_large_language_models_detect_misinformation_in_scientifi/review]] — 과학 뉴스의 오보 탐지를 위한 타당성 차원 정의가 SFAVEL의 클레임-근거 의미론적 정렬 학습의 이론적 기반을 제공함
- 🔄 다른 접근: [[papers/832_Towards_llm-based_fact_verification_on_news_claims_with_a_hi/review]] — HiSS가 계층적 단계별 프롬프팅을 통해 뉴스 클레임을 세분화하는 반면, SFAVEL은 언어모델 증류를 통한 무감독 학습으로 서로 다른 팩트 검증 접근법을 제시함
- 🏛 기반 연구: [[papers/441_Investigating_zero-and_few-shot_generalization_in_fact_verif/review]] — 팩트 검증을 위한 비지도 사전학습 방법이 zero-shot 및 few-shot 일반화 연구의 방법론적 기초를 제공함
- 🔗 후속 연구: [[papers/567_Multivers_Improving_scientific_claim_verification_with_weak/review]] — 비감독 사전훈련을 약한 감독 학습으로 확장하여 더 정교한 과학 사실 검증 시스템을 구축합니다.
