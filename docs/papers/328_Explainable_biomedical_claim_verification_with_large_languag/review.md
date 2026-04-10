---
title: "328_Explainable_biomedical_claim_verification_with_large_languag"
authors:
  - "Siting Liang"
  - "Daniel Sonntag"
date: "2025"
doi: "arXiv:2502.21014"
arxiv: ""
score: 3.5
essence: "대규모 언어 모델(LLM)과 SHAP 설명가능성을 결합하여 의료 주장 검증의 투명성을 높이는 대화형 시스템을 제시한다. 사용자는 과학 문헌에서 관련 연구를 검색하고, CoENLI 프레임워크를 통해 LLM의 추론 과정을 검토하며, SHAP 값으로 단어 수준의 기여도를 파악할 수 있다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Fact_Verification_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Matar et al._2025_Explainable biomedical claim verification with large language models.pdf"
---

# Explainable biomedical claim verification with large language models

> **저자**: Siting Liang, Daniel Sonntag | **날짜**: 2025 | **DOI**: [arXiv:2502.21014](https://arxiv.org/abs/2502.21014)

---

## Essence

![Figure 1](figures/fig1.webp) 
*그림 1: 생의학 주장 검증 시스템의 대화형 컴포넌트들*

대규모 언어 모델(LLM)과 SHAP 설명가능성을 결합하여 의료 주장 검증의 투명성을 높이는 대화형 시스템을 제시한다. 사용자는 과학 문헌에서 관련 연구를 검색하고, CoENLI 프레임워크를 통해 LLM의 추론 과정을 검토하며, SHAP 값으로 단어 수준의 기여도를 파악할 수 있다.

## Motivation

- **Known**: 생의학 주장 검증은 미세 조정된 자연어 추론(NLI) 모델을 통해 "Support", "Contradict", "Not Enough Information" 중 하나로 분류하는 표준 파이프라인을 따른다. LLM은 복잡한 의료 문서 처리와 전문 용어 해석에 효과적이다.

- **Gap**: 의료·과학 도메인의 고위험 결정 상황에서 LLM의 투명성, 설명가능성, 신뢰성이 부족하다. 기존 Chain-of-Thought(CoT)는 일반적이며, 최종 분류까지의 의사결정 과정의 불투명성이 남아있다.

- **Why**: 의료 분야의 실제 적용에서는 클리니션과 연구자가 모델의 추론 과정을 이해하고 결정에 참여할 수 있어야 신뢰 가능한 인간-AI 협업이 가능하다.

- **Approach**: CoENLI(Chain of Evidence-based NLI) 프레임워크와 SHAP 설명가능성을 통합한 대화형 검증 시스템 개발. 사용자는 다중 LLM의 비교 분석, 생성된 근거 기반 설명, 단어 수준의 기여도 분석을 통해 최종 판단을 내린다.

## Achievement

![Figure 2](figures/fig1.webp)
*그림 2: 증거 분석과 SHAP 기반 설명의 이중층 설명가능성*

1. **CoENLI 프레임워크 개발**: 의미 기반화(Semantic Grounding) → 증거 기반 평가(Evidence-Based Evaluation) → 관계 예측(Relation Prediction)의 3단계 체계화된 추론으로 NLI4CT와 SciFact 벤치마크에서 CoT 대비 성능 향상을 달성했다.

2. **이중층 설명가능성 구현**: LLM의 근거 분석과 SHAP 기반 단어 기여도를 함께 제시하여 모델의 의사결정 과정을 다층적으로 해석 가능하게 만들었다.

3. **인간-AI 협업 워크플로우**: 사용자가 분류 결과를 검토하고 조정할 수 있으며, 모델이 조정된 판단에 대한 근거 기반 정당화(narrative justification)를 생성하는 순환적 과정을 구현했다.

## How

![Figure 4](figures/fig1.webp)
*그림 4: CoENLI 프레임워크의 3단계 추론 과정*

**시스템 워크플로우**:
- **Step 1**: 사용자가 검증할 주장(claim) 선택 → BM25 알고리즘으로 관련 과학 논문 검색
- **Step 2**: 다중 LLM을 CoENLI 프레임워크로 평가 실행
  - 의미 기반화: 주장의 핵심 용어 해석
  - 증거 기반 평가: 연구에서 관련 사실 추출 후 주장의 각 요소 비교 평가
  - 관계 예측: 생성된 해석과 평가를 기반으로 최종 분류
- **Step 3**: SHAP 값으로 생성된 설명문의 단어별 기여도 시각화 (양수: 빨강, 음수: 파랑)
- **Step 4**: 사용자가 분류 결과 검토 및 필요 시 조정, 모델이 조정 사유에 대한 정당화 생성

**기술적 구성요소**:
- BM25 기반 문헌 검색
- 다중 LLM 통합 (비교 분석 제공)
- CoENLI 프롬프트 엔지니어링
- SHAP 설명가능성 모듈 (Mistral 모델 기반)

## Originality

- **CoENLI 프레임워크**: 기존 Chain-of-Thought를 의료 주장 검증에 맞게 재설계하여 의미 기반화, 증거 기반 평가, 관계 예측의 명시적 3단계 구조 제시

- **SHAP 통합**: LLM의 중간 생성물(근거 기반 설명)에 대한 단어 수준의 설명가능성을 추가하여 "왜 이 단어들이 최종 결정에 영향을 미쳤는가"에 답변

- **인간-중심 대화형 설계**: 사용자가 모델의 설명을 검토하고 비동의 시 결정을 조정하며 모델이 이에 응답하는 양방향 협업 메커니즘 구현

- **다중 LLM 비교 제시**: 단일 모델이 아닌 여러 LLM의 결과와 추론을 병렬 제시하여 결정의 신뢰성 강화

## Limitation & Further Study

- **평가 완성도**: 논문의 평가 섹션(Section 3)이 불완전하게 제시되어 NLI4CT, SciFact 벤치마크에서의 정량적 성능 비교 결과가 누락됨

- **사용성 검증 부재**: 사용자 연구(user study)를 계획했으나 결과가 미포함. 실제 임상의나 연구자가 시스템을 사용했을 때의 신뢰도, 의사결정 개선도, 사용 편의성에 대한 평가 필요

- **확장성 한계**: 현재는 NLI4CT와 SciFact 같은 특정 벤치마크에 제한. 다양한 의료 도메인(약물 상호작용, 부작용 예측 등)으로의 일반화 가능성 미검토

- **SHAP 계산 비용**: SHAP 값 계산의 계산량(computational complexity)과 실시간 시스템 적용 가능성에 대한 논의 부재

- **후속 연구**: 
  - 더 큰 규모의 사용자 연구를 통한 신뢰도 및 의사결정 질 개선 검증
  - 더 넓은 의료 주장 유형 및 복잡도에 대한 CoENLI 성능 평가
  - 증거 종합(evidence synthesis) 프레임워크로의 통합 및 임상 워크플로우 적용

## Evaluation

| 평가 항목 | 점수 | 근거 |
|---------|------|------|
| **Novelty** | 4/5 | CoENLI와 SHAP 통합은 창신적이나, CoT 기반의 점진적 개선으로 혁신성은 중간 수준 |
| **Technical Soundness** | 3.5/5 | 방법론 설계는 타당하나 평가 결과 미제시로 검증 불완전, 사용자 연구 미포함 |
| **Significance** | 4/5 | 의료 분야의 고위험 결정에 투명성과 설명가능성을 추가하는 실질적 가치 높음 |
| **Clarity** | 4/5 | 시스템 아키텍처와 CoENLI 프로세스가 명확하게 설명됨. 다만 평가 섹션 미완성으로 감점 |
| **Overall** | 3.5/5 | 의료 AI의 설명가능성과 인간-AI 협업을 다루는 중요한 주제로, 시스템 설계는 우수하나 정량적 검증과 사용자 평가 미완료 |

**총평**: 생의학 주장 검증의 투명성을 위해 CoENLI와 SHAP을 결합한 대화형 시스템은 실질적 가치 있는 제안이나, 논문이 미완성된 상태(평가 섹션 절반만 기재, 사용자 연구 결과 누락)로 과학적 검증이 불충분하다. 후속 완전판 논문 발표 시 상당히 향상될 것으로 예상된다.

## Related Papers

- 🔗 후속 연구: [[papers/685_Robust_claim_verification_through_fact_detection/review]] — 일반적인 사실 검증을 의료 분야로 특화하고 설명가능성을 추가한 확장 연구이다
- 🧪 응용 사례: [[papers/221_Claimver_Explainable_claim-level_verification_and_evidence_a/review]] — 지식 그래프 기반 설명가능한 검증을 의료 주장 검증에 구체적으로 적용한다
- 🔄 다른 접근: [[papers/057_aedfact_Scientific_fact-checking_made_easier_via_semi-automa/review]] — 웹 기반 반자동 검색 대신 LLM과 SHAP를 결합한 대화형 검증 시스템을 제시한다
- 🔄 다른 접근: [[papers/159_Bio-sieve_exploring_instruction_tuning_large_language_models/review]] — 생명의학 주장 검증과 초록 스크리닝 자동화의 다른 의료 AI 접근법
- 🔗 후속 연구: [[papers/235_Comparing_knowledge_sources_for_open-domain_scientific_claim/review]] — 설명 가능한 생물의학 주장 검증 연구로 본 논문의 과학적 주장 검증을 의료 도메인으로 확장한다.
- 🔗 후속 연구: [[papers/685_Robust_claim_verification_through_fact_detection/review]] — 의료 분야로 특화하여 사실 검증에 설명가능성을 추가한 확장 연구이다
- 🔗 후속 연구: [[papers/057_aedfact_Scientific_fact-checking_made_easier_via_semi-automa/review]] — 과학적 팩트체킹을 의료 분야로 확장하고 설명가능성을 추가한다
- 🏛 기반 연구: [[papers/221_Claimver_Explainable_claim-level_verification_and_evidence_a/review]] — 지식 그래프 기반 주장 검증의 기초 방법론을 의료 분야에 특화하여 확장한다
