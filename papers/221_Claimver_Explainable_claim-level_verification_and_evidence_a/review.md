---
title: "221_Claimver_Explainable_claim-level_verification_and_evidence_a"
authors:
  - "Preetam Prabhu Srikar Dammu"
  - "Himanshu Naidu"
  - "Mouly Dewan"
  - "Youngmin Kim"
  - "Tanya Roosta"
date: "2024"
doi: "N/A"
arxiv: ""
score: 3.5
essence: "본 논문은 지식 그래프(Knowledge Graph, KG)를 활용하여 텍스트의 각 주장(claim)을 세분화된 수준에서 검증하고, 각 검증 결과에 대한 명확한 증거와 설명을 제공하는 ClaimVer 프레임워크를 제안한다. 단순한 이진 판정 대신 주장 단위의 세밀한 분석을 통해 사용자의 신뢰도를 향상시킨다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Fact_Verification_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Dammu et al._2024_Claimver Explainable claim-level verification and evidence attribution of text through knowledge gr.pdf"
---

# Claimver: Explainable claim-level verification and evidence attribution of text through knowledge graphs

> **저자**: Preetam Prabhu Srikar Dammu, Himanshu Naidu, Mouly Dewan, Youngmin Kim, Tanya Roosta, Aman Chadha, Chirag Shah | **날짜**: 2024 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) 
*ClaimVer의 주장 검증 및 증거 귀속 시연. 자동 색상 코딩(황색: 외삽, 적색: 모순)과 위키데이터 기반 증거 제시*

본 논문은 지식 그래프(Knowledge Graph, KG)를 활용하여 텍스트의 각 주장(claim)을 세분화된 수준에서 검증하고, 각 검증 결과에 대한 명확한 증거와 설명을 제공하는 ClaimVer 프레임워크를 제안한다. 단순한 이진 판정 대신 주장 단위의 세밀한 분석을 통해 사용자의 신뢰도를 향상시킨다.

## Motivation

- **Known**: 기존의 사실 검증 도구(HealthFeedback, Google Fact Check Tools)들은 텍스트 전체에 대한 포괄적 레이블만 제공하며, 문장(sentence) 또는 단락(paragraph) 수준의 검증에 머물러 있음.
- **Gap**: (1) 한 텍스트 내 다중 주장에 대한 세분화된 검증 부재, (2) 검증 근거의 명확한 제시 부족, (3) 사용자 신뢰 형성을 위한 설명가능성(explainability) 부족.
- **Why**: AI 생성 텍스트의 확산으로 미정보(misinformation)와 환각(hallucination) 문제가 심화되고 있으며, 사용자가 자동화된 검증 시스템을 신뢰하기 위해서는 근거 있는 설명이 필수적.
- **Approach**: 위키데이터(Wikidata) 기반 지식 그래프를 검증의 신뢰할 수 있는 참조 자료로 활용하고, LLM을 미세 조정하여 주장 수준의 세밀한 검증과 증거 귀속을 동시에 수행.

## Achievement

![Figure 2](figures/fig2.webp) 
*ClaimVer 프레임워크의 전체 처리 흐름. 전처리 단계에서 NER, 공참 해결, KG 엔티티 링킹을 거쳐 관련 삼중항(triplet) 검색 및 미세조정된 LLM을 통한 검증 수행*

1. **주장 단위 세분화 검증**: 단일 텍스트를 다수의 독립적 주장으로 분해하여 각각을 검증하므로, 일부 주장이 거짓이더라도 나머지 주장의 검증 결과를 차별화하여 제시 가능.

2. **KG 기반 다중 참조 통합**: 단일 참조 문헌과의 일대일 매핑 방식을 벗어나 지식 그래프라는 통합된 정보 저장소를 활용하여 여러 출처에서 수집된 정보를 종합적으로 검증.

3. **설명가능한 검증 결과**: 각 주장에 대해 (1) 예측(Attributable/Extrapolatory/Contradictory), (2) 관련 삼중항, (3) 설명(rationale), (4) 귀속 점수(Knowledge Attribution Score, KAS)를 함께 제시.

4. **위키데이터 엔티티 연결**: 검증 결과와 함께 관련 위키 엔티티의 ID와 설명을 시각적으로 표시하여 사용자가 검증의 근거를 직접 확인 가능.

## How

![Figure 3](figures/fig3.webp)
*미세조정용 LLM 지시어 프롬프트. 주장과 관련 삼중항을 입력받아 검증 카테고리, 설명, 귀속 점수를 출력하도록 구조화*

- **전처리(Preprocessing)**: 위키 엔티티에 특화된 명명 엔티티 인식(NER), 공참 해결(coreference resolution), KG 엔티티 링킹(entity linking), 문맥 길이 초과 시 구획화(compartmentalization) 수행.

- **관련 삼중항 검색**: Woolnet 알고리즘(다중 노드 너비 우선 탐색, BFS)을 통해 각 주장과 관련된 지식 그래프 상의 삼중항 추출. 최대 3홉(hop), 최대 4개 경로 제한으로 관련성 있는 삼중항만 검색.

- **검증 목적 함수**: 세 가지 카테고리 정의
  - **Attributable**: 삼중항이 주장을 완전히 지지
  - **Extrapolatory**: 주장 평가에 불충분한 정보
  - **Contradictory**: 삼중항이 주장과 모순

- **LLM 미세조정**: Llama3-8B-Chat, Mistral-7B-v0.3-Chat 등의 오픈소스 모델을 지시어 기반으로 미세조정하여 주장, 관련 삼중항, 위키데이터 정의를 입력받아 검증 카테고리, 설명, 귀속 점수를 예측하도록 학습.

- **귀속 점수(KAS)**: 검증된 주장의 신뢰도를 0과 1 사이의 점수로 정량화하여 다운스트림 작업에 적용 가능하게 설계.

## Originality

- **세분화된 분석 수준**: 기존 문장/단락 수준 검증을 주장(claim) 수준으로 확대하여 더 세밀한 오류 지적 가능.

- **KG 기반 다중 참조 통합**: 일대일 텍스트-참조 매핑 방식을 벗어나 지식 그래프라는 통합 정보원을 활용함으로써 정보 출처의 분산 문제 해결.

- **설명과 증거의 동시 제시**: 단순 예측에 그치지 않고 설명(rationale), 관련 삼중항(triplets), 위키 엔티티 정보를 함께 제공하여 사용자 신뢰 향상.

- **일반적 프레임워크**: 위키데이터에 국한되지 않고 삼중항 형식의 모든 지식 그래프에 적용 가능한 범용 설계.

- **정량화된 귀속 점수**: Knowledge Attribution Score(KAS)라는 새로운 메트릭 도입으로 검증 결과의 활용성 확대.

## Limitation & Further Study

- **지식 그래프의 한계**: Wikidata의 완성도와 최신성에 의존하므로, KG에 미포함된 사실에 대해서는 검증 불가. 신속히 변화하는 뉴스나 통계 데이터의 경우 시의성 문제 발생 가능.

- **복잡한 추론 필요한 주장**: 다중 단계의 논리적 연쇄(multi-hop reasoning)가 필요한 주장의 경우 검증 정확성이 떨어질 수 있으며, 인과관계나 조건부 명제는 삼중항 구조로 표현하기 어려움.

- **LLM 미세조정의 데이터 의존성**: 학습 데이터의 품질과 규모에 따라 성능이 크게 좌우될 수 있으나, 논문에서 사용한 학습 데이터셋의 규모와 구성에 대한 구체적 정보 부족.

- **평가 방법론 제시 부족**: 본 논문 발췌본에서는 실제 실험 결과, 정량적 평가 지표, 기존 방법과의 비교 분석이 제시되지 않음.

- **후속 연구 방향**:
  - 다양한 도메인과 언어에 대한 광범위한 평가 필요
  - 실시간 정보 업데이트를 반영하는 동적 KG 연계
  - 사용자 신뢰도 향상의 실제 효과 측정을 위한 사용성 연구
  - 증거 선택 과정의 투명성 강화(왜 특정 삼중항이 선택되었는가)

## Evaluation

- **Novelty**: 4/5
  - 주장 단위 세분화와 KG 기반 다중 참조 통합이 참신하나, 개별 기술 요소(NER, 공참 해결, BFS)는 기존 기법의 조합.

- **Technical Soundness**: 3.5/5
  - 전반적 설계는 논리적이고 일관성 있으나, 복잡한 주장의 처리 방식, 미세조정 손실 함수의 상세 정의, 하이퍼파라미터 선택 근거 등이 불명확.

- **Significance**: 4/5
  - 사실 검증의 실용적 적용 맥락에서 설명가능성과 세분화의 중요성을 잘 포착했으며, 미정보 대응의 현실적 니즈를 반영함. 다만 평가 결과 미제시로 실제 효과의 입증이 부족.

- **Clarity**: 3.5/5
  - 사례를 통한 직관적 설명은 우수하나, 방법론 섹션의 기술적 세부사항(특히 LLM 미세조정, 손실 함수 정의, 평가 프로토콜)이 간략함.

- **Overall**: 3.5/5

**총평**: ClaimVer는 사용자 중심의 설명가능한 사실 검증이라는 중요한 문제에 접근한 실용적 프레임워크로, 주장 단위 검증과 KG 기반 증거 제시 방식이 신선하다. 다만 정량적 평가 결과의 부재와 기술적 세부사항의 부족으로 인해 재현성과 신뢰성 검증이 필요하며, 실제 시스템 성능과 사용자 신뢰도 향상의 실증적 증거가 제시되어야 완성도 있는 연구로 평가될 수 있다.

## Related Papers

- 🔄 다른 접근: [[papers/685_Robust_claim_verification_through_fact_detection/review]] — 간결한 사실 추출 방식 대신 지식 그래프를 활용한 설명가능한 주장 검증을 제시한다
- 🏛 기반 연구: [[papers/328_Explainable_biomedical_claim_verification_with_large_languag/review]] — 지식 그래프 기반 주장 검증의 기초 방법론을 의료 분야에 특화하여 확장한다
- 🔗 후속 연구: [[papers/057_aedfact_Scientific_fact-checking_made_easier_via_semi-automa/review]] — 반자동 팩트체킹을 더 체계적이고 설명가능한 프레임워크로 발전시킨다
- 🔄 다른 접근: [[papers/685_Robust_claim_verification_through_fact_detection/review]] — 주장 검증을 위한 다른 접근법으로 지식 그래프를 활용한 설명가능한 방법을 제시한다
- 🔄 다른 접근: [[papers/057_aedfact_Scientific_fact-checking_made_easier_via_semi-automa/review]] — 웹 기반 반자동 검색 대신 지식 그래프를 활용한 체계적 주장 검증 방법을 제시한다
- 🧪 응용 사례: [[papers/328_Explainable_biomedical_claim_verification_with_large_languag/review]] — 지식 그래프 기반 설명가능한 검증을 의료 주장 검증에 구체적으로 적용한다
