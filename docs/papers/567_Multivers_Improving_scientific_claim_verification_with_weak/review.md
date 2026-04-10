---
title: "567_Multivers_Improving_scientific_claim_verification_with_weak"
authors:
  - "David Wadden"
  - "Kyle Lo"
  - "Lucy Lu Wang"
  - "Arman Cohan"
  - "Iz Beltagy"
date: "2021"
doi: "arXiv:2112.01640"
arxiv: ""
score: 4.0
essence: "과학 청구 검증 시스템이 선택된 근거 문장만 사용하지 않고 전체 문서 맥락을 활용하며, 약한 감독(weak supervision)을 통해 문장 수준의 주석 없이도 학습할 수 있는 멀티태스크 모델을 제시한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Fact_Verification_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Röttger et al._2021_Multivers Improving scientific claim verification with weak supervision and full-document context.pdf"
---

# Multivers: Improving scientific claim verification with weak supervision and full-document context

> **저자**: David Wadden, Kyle Lo, Lucy Lu Wang, Arman Cohan, Iz Beltagy, Hannaneh Hajishirzi | **날짜**: 2021 | **DOI**: [arXiv:2112.01640](https://arxiv.org/abs/2112.01640)

---

## Essence

![Figure 1](figures/fig1.webp) *Ibuprofen 청구가 COVID-19 증상을 악화시킨다는 주장이 의료 논문 초록으로 반박되는 예시. 빨간색 문장은 근거이지만 파란색 맥락 없이는 올바르게 해석될 수 없음*

과학 청구 검증 시스템이 선택된 근거 문장만 사용하지 않고 전체 문서 맥락을 활용하며, 약한 감독(weak supervision)을 통해 문장 수준의 주석 없이도 학습할 수 있는 멀티태스크 모델을 제시한다.

## Motivation

- **Known**: 기존 "추출-후-분류(extract-then-label)" 접근법은 선택된 근거 문장만으로 분류 결정을 내림. 이는 근거 문장이 약어, 지시 표현, 한정사(qualifier) 등으로 인해 맥락 없이는 불완전할 수 있음.

- **Gap**: 1) 추출된 근거가 단독으로는 충분한 정보를 제공하지 못함 2) 문장 수준의 근거 주석은 매우 비싸지만, 문서 수준의 분류는 휴리스틱으로 저렴하게 생성 가능

- **Why**: 전문 분야의 사실 검증은 전문가 주석의 높은 비용으로 인해 소수 샘플(few-shot) 또는 영-샷(zero-shot) 설정에서의 성능이 중요함

- **Approach**: 1) Longformer를 사용한 전체 문서 맥락의 공유 인코딩 2) 멀티태스크 방식으로 추상화 수준의 분류와 문장 수준의 근거 선택을 동시에 수행 3) 약한 감독으로 학습 가능하도록 설계

## Achievement

1. **성능 개선**: 3개 과학 청구 검증 데이터셋(COVIDFact, HealthVer, SCIFACT)에서 두 개의 SOTA 기준선 대비 평균 11% 향상(추상화 F1 기준). 소수-샷 및 영-샷 설정에서 각각 14%, 26% 개선

2. **약한 감독의 효과**: 고정밀 휴리스틱으로 생성된 약하게 레이블된 데이터로 학습 시 영-샷 도메인 적응 성능이 2배 이상 증가

3. **효율성**: 비교 기준선 중 하나(VERT5ERINI, T5-3B)보다 10배 이상 적은 파라미터로 우월한 성능 달성

## How

- **입력 처리**: 청구(claim), 제목(title), 문장들을 "</s>" 토큰으로 구분하여 연결: `<s> c </s> t </s> s1 </s>₁ ... sn </s>ₙ`

- **Long-document 인코딩**: Longformer 사용으로 512 토큰 제한 초과하는 긴 초록 처리. `<s>` 토큰, 청구의 모든 토큰, 모든 `</s>` 토큰에 전역 주의(global attention) 할당

- **멀티태스크 헤드**: 
  - 문장 수준 근거 선택: `</s>ᵢ` 토큰 위의 이진 분류(피드포워드 2층 + softmax)
  - 추상화 수준 분류: `<s>` 토큰 위의 3-방향 분류(SUPPORTS/REFUTES/NEI)

- **손실 함수**: L = L_label + λ_rationale × L_rationale (λ 값은 개발 세트에서 튜닝)

- **추론 시 일관성 강제**: 먼저 분류 레이블 예측 → NEI이면 근거 없음 → SUPPORTS/REFUTES이면 softmax > 0.5인 문장들을 근거로 선택(없으면 최고 점수 문장 1개)

## Originality

- **멀티태스크 아키텍처의 혁신**: 기존의 순차적 "근거 추출 → 분류" 파이프라인 대신 전체 맥락에서 동시에 두 작업을 수행하되, 추론 시 레이블 예측이 근거 선택을 조건화하도록 함. 이는 감정 분석의 토큰 수준 근거 작업과 유사하지만 문서 수준 과학 검증에 최초 적용

- **약한 감독 활용**: 문장 수준 주석 없는 데이터로도 학습 가능하게 설계함으로써 비용 대비 효율성을 크게 개선

- **Longformer 활용**: 과학 논문 초록의 길이 특성(평균 175 토큰, 일부 500+ 토큰)을 처리하기 위해 효율적인 장문서 인코더 도입

## Limitation & Further Study

- **문장 경계 의존성**: 모델이 미리 정해진 문장 단위로만 근거를 선택할 수 있으며, 문장 경계 오류에 영향받을 수 있음

- **약한 감독 휴리스틱의 한계**: 논문 제목-초록 일치 기반 휴리스틱은 특정 도메인(COVID-19)에서만 적용되었으며, 다른 과학 분야로의 일반화 가능성 미검증

- **근거 정의의 단순화**: 원본 SCIFACT 정의에서 단순화되었으며, 여러 문장의 복합적 상호작용이 필요한 복잡한 근거 관계 미처리

- **후속 연구 방향**: 1) 다른 전문 도메인(법률, 바이오의료)의 약한 감독 휴리스틱 개발 2) 토큰 수준 근거 선택으로 확장 3) 다언어 청구 검증 적용

## Evaluation

- **Novelty**: 4/5 — 멀티태스크 아키텍처와 약한 감독의 결합은 창의적이나, 개별 기술은 기존 아이디어의 응용

- **Technical Soundness**: 4.5/5 — 구현이 명확하고 실험 설계가 철저함. Longformer 활용과 주의 메커니즘이 적절. 다만 복잡한 근거 관계의 한계는 남음

- **Significance**: 4/5 — 과학 청구 검증이라는 중요한 응용 분야에서 실질적 성능 향상을 달성했으며, 특히 영-샷/소수-샷 적응은 실무 가치가 높음

- **Clarity**: 4/5 — 논문이 잘 구성되었고 시각화(Figure 1)로 문제점을 명확히 제시. 다만 일부 기술적 세부사항은 더 명시적일 수 있음

- **Overall**: 4/5

**총평**: MULTIVERS는 전체 문서 맥락을 활용하고 약한 감독으로 학습 가능한 실용적 설계를 통해 과학 청구 검증의 성능을 크게 향상시킨 견고한 연구이며, 특히 전문 분야의 저자원 시나리오에서의 기여가 눈에 띈다.

## Related Papers

- 🏛 기반 연구: [[papers/541_Missing_counter-evidence_renders_nlp_fact-checking_unrealist/review]] — NLP 사실 확인의 비현실적 측면 분석이 과학 청구 검증에서 약한 감독 학습의 한계 이해에 기초를 제공합니다.
- 🔄 다른 접근: [[papers/333_Factkg_Fact_verification_via_reasoning_on_knowledge_graphs/review]] — 과학 청구 검증에서 약한 감독과 지식 그래프 추론의 서로 다른 사실 검증 접근법을 비교할 수 있습니다.
- 🔗 후속 연구: [[papers/859_Unsupervised_pretraining_for_fact_verification_by_language_m/review]] — 비감독 사전훈련을 약한 감독 학습으로 확장하여 더 정교한 과학 사실 검증 시스템을 구축합니다.
- 🔗 후속 연구: [[papers/500_Llm-based_corroborating_and_refuting_evidence_retrieval_for/review]] — 과학적 주장 검증을 약한 지도학습으로 개선한 멀티모달 접근
