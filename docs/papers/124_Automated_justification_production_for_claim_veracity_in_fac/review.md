---
title: "124_Automated_justification_production_for_claim_veracity_in_fac"
authors:
  - "Islam Eldifrawi"
  - "Shengrui Wang"
  - "Amine Trabelsi"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "본 논문은 자동 팩트체킹 시스템에서 판정 결과를 설명하기 위한 **정당화(justification) 자동 생성**에 초점을 맞춘 종합 서베이로, 최근 트랜스포머와 대형언어모델(LLM) 발전에 따른 설명 가능한 팩트체킹의 진화를 체계적으로 분석하고 정당화 표준화를 위한 다차원 분류체계를 제시한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Cognitive_LLM_Evaluation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Eldifrawi et al._2024_Automated justification production for claim veracity in fact checking A survey on architectures an.pdf"
---

# Automated justification production for claim veracity in fact checking: A survey on architectures and approaches

> **저자**: Islam Eldifrawi, Shengrui Wang, Amine Trabelsi | **날짜**: 2024 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*일반적인 자동 팩트체킹(AFC) 파이프라인: 주장 검증성 탐지 → 증거 검색 및 선택 → 진위 판정 → 정당화 생성*

본 논문은 자동 팩트체킹 시스템에서 판정 결과를 설명하기 위한 **정당화(justification) 자동 생성**에 초점을 맞춘 종합 서베이로, 최근 트랜스포머와 대형언어모델(LLM) 발전에 따른 설명 가능한 팩트체킹의 진화를 체계적으로 분석하고 정당화 표준화를 위한 다차원 분류체계를 제시한다.

## Motivation

- **Known**: 온라인 콘텐츠의 급증으로 자동 팩트체킹의 중요성 증대; 기존 연구는 주로 진위 판정(veracity prediction)에 집중
- **Gap**: 판정 결과만 제시하는 방식은 거짓 정보를 강화할 수 있으며, 신뢰성 있는 설명(justification)을 제공하는 연구는 부족함; Kotonya and Toni (2020a) 이후 트랜스포머/LLM 기반의 새로운 접근법들이 등장했으나 체계적인 정리 부재
- **Why**: 신경망 모델의 해석 어려움을 극복하고 정당화의 신뢰성을 확보하려면 표준화된 평가 기준과 다양한 방법론의 비교 분석이 필수적
- **Approach**: 정당화 생성 방법론을 (1) 파이프라인 아키텍처, (2) 입출력 유형, (3) 주요 접근법, (4) 설명 가능성 등 5개 차원의 다면적 분류체계로 정리하고 진행 상황을 분석

## Achievement

![Figure 3](figures/fig3.webp)
*정당화 생성을 위한 5개 차원의 분류 체계: 파이프라인 아키텍처, 입력 유형, 출력 유형, 설명 가능성, 주요 접근법*

1. **다차원 분류체계 제시**: AFC 정당화 생성을 (i) 파이프라인 아키텍처 (ii) 입력 유형(텍스트/멀티모달) (iii) 출력 유형(자연언어/강조/SPO 트리플) (iv) 설명 가능성(자기설명적/비자기설명적) (v) 주요 방법론(어텐션, 지식그래프, 요약, 멀티홉, LLM RAG/파인튜닝) 등으로 체계적으로 분류

2. **정당화 표준화 진행 상황 분석**: Graves (2018)의 완전성, 일관성, 상호작용성, 실행가능성, 시간성, 참신성, 복잡성, 간결성, 인과성, 중립성 등 10가지 바람직한 특성(desiderata)을 제시하고, Atanasova et al. (2022)의 손실함수 기반 일관성 강화 시도 등 진행 상황 기록

3. **기존 서베이의 한계 극복**: Kotonya and Toni (2020a)의 논문 이후 출현한 새로운 접근법들(특히 LLM 기반)을 포함하며, 멀티모달 정당화 생성 분야의 미개척 영역에 대한 초기 관찰 제공

## How

![Figure 4](figures/fig4.webp)
*정당화 출력 유형의 예시: 자연언어 텍스트, 강조 부분, SPO 트리플*

**AFC 파이프라인의 4단계 구성:**
- **주장 검증성 탐지 (3.1)**: 주장의 중요도, 검증 가능성, 잠재적 해악성 판단
- **증거 검색 및 선택 (3.2)**: 신뢰할 수 있는 출처에서 관련 증거 수집
- **진위 판정 (3.3)**: 이진(참/거짓) 또는 세분화된 다중 분류(부분적 참, 오도적 등)
- **정당화 생성 (3.4)**: 판정 근거를 자연언어로 설명

**주요 정당화 생성 접근법:**
- **어텐션 기반(Attention-based)**: 증거와 주장 간 관계에서 높은 어텐션 스코어 부분 강조
- **지식그래프 기반(Knowledge Graph-based)**: 그래프 구조로 증거 표현, 선택된 노드를 정당화로 활용
- **요약 기반(Summarization-based)**: 관련 증거를 자연언어 텍스트로 요약
- **멀티홉 기반(Multi-hop based)**: 주장을 부분으로 분해하여 순차적 검증
- **LLM 기반(RAG/Fine-tuning)**: 프롬프팅을 통한 LLM 활용

**표준 정장화를 위한 평가 지표:**
- 전역 일관성(global coherence): 정당화와 주장, 판정 레이블의 관련성
- 지역 일관성(local coherence): 정장 내 문장 간 모순 부재

## Originality

- **포괄적 다면적 분류체계**: 기존 Kotonya and Toni (2020a)의 분류를 상당히 확장하여 파이프라인 아키텍처, 입출력 유형, 설명 가능성을 독립적 차원으로 처리
- **최신 기술 반영**: 트랜스포머 및 LLM 기반 접근법의 급속한 발전(2020년 이후)을 체계적으로 정리한 최초 시도
- **정당화 표준화 과정 추적**: Graves, Kotonya & Toni, Atanasova 등의 바람직한 특성(desiderata) 정의부터 실제 평가 구현까지 진화 과정을 명확히 기록
- **멀티모달 정당화 생성의 초기 탐색**: 기존 멀티모달 팩트체킹 서베이에서 언급되지 않은 자연언어 정장화 분야의 새로운 시도들을 포함

## Limitation & Further Study

**한계:**
- 본문 제시 범위(15,000자)로 인해 실제 방법론들에 대한 구체적인 기술 분석이 제한적
- 다양한 접근법의 성능 비교 정량 데이터 부재 (비교 분석은 방향성만 제시)
- 언어별(다국어), 도메인별(정치, 과학, 보건) 성능 차이에 대한 상세 논의 부족
- 멀티모달 정당화 생성 분야의 미성숙성으로 인한 제한된 사례

**후속 연구 방향:**
- 표준 정장화를 위한 자동 평가 메트릭 개발 (인간 평가에 대한 의존도 감소)
- 설명 가능성과 정장 품질 간의 트레이드오프 분석
- 멀티모달 정장화 생성의 체계적 연구 (이미지/비디오 기반 증거 해석)
- 사용자 피드백 기반 대화형 정장화 개선 (interactivity 특성 강화)
- 다언어/크로스도메인 정장화 생성의 일반화 능력 향상

## Evaluation

- **Novelty**: 4/5 - 기존 서베이의 한계를 명확히 인식하고 다면적 분류체계를 제시했으나, 근본적으로 새로운 기술보다는 기존 작업의 체계적 정리
- **Technical Soundness**: 4/5 - 논리적 파이프라인 구조와 평가 기준 정의는 타당하나, 구체적인 기술 분석 깊이는 제한적
- **Significance**: 4/5 - AFC와 설명 가능한 AI 분야의 중요한 연구 방향을 체계화했으나, 실제 시스템 구축에 미치는 영향은 향후 구체적 방법론 발전에 의존
- **Clarity**: 4/5 - 파이프라인과 분류체계는 명확하나, 5개 차원의 분류 기준 간 상호관계와 우선순위가 명확하지 않음
- **Overall**: 4/5

**총평**: 이 서베이는 자동 팩트체킹의 설명 가능성 향상이라는 시의적절한 주제를 다면적 분류체계로 정리한 유용한 참고자료이나, 정장화 표준화의 구체적 기술적 진전과 실제 벤치마킹 결과 분석을 통해 더욱 강화될 수 있을 것으로 판단된다.

## Related Papers

- 🏛 기반 연구: [[papers/117_Augmenting_the_veracity_and_explanations_of_complex_fact_che/review]] — 팩트체킹 시스템의 정확성과 설명력 향상을 위한 기반 연구로서 정당화 생성의 이론적 토대를 제공한다.
- 🧪 응용 사례: [[papers/883_When_reviewers_lock_horn_Finding_disagreement_in_scientific/review]] — 과학 논문 피어 리뷰에서 발생하는 의견 불일치를 자동으로 탐지하는 것이 팩트체킹의 정당화 생성과 유사한 판단 근거 제시 문제이다.
- 🔗 후속 연구: [[papers/736_SciTrust_Evaluating_the_Trustworthiness_of_Large_Language_Mo/review]] — 과학 분야 LLM의 신뢰성 평가에서 환각과 편향을 다루는 것이 팩트체킹의 정당화 생성과 직접 연결된다.
- 🏛 기반 연구: [[papers/883_When_reviewers_lock_horn_Finding_disagreement_in_scientific/review]] — 피어 리뷰에서 리뷰어 간 의견 불일치 탐지가 팩트체킹에서 판정 결과의 정당화 생성과 유사한 판단 근거 분석 문제이다.
- 🏛 기반 연구: [[papers/736_SciTrust_Evaluating_the_Trustworthiness_of_Large_Language_Mo/review]] — 과학 분야 LLM의 환각과 편향 문제가 팩트체킹 시스템의 정당화 생성에서 신뢰할 수 있는 판단 근거 제시의 기반이 된다.
- 🔗 후속 연구: [[papers/237_Confidence_in_Large_Language_Model_Evaluation_A_Bayesian_App/review]] — 사실 확인의 자동 정당화를 베이지안 추론으로 확장한 신뢰도 평가 연구
