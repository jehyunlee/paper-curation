---
title: "736_SciTrust_Evaluating_the_Trustworthiness_of_Large_Language_Mo"
authors:
  - "Emily Herron"
  - "Junqi Yin"
  - "Feiyi Wang"
date: "2024.01"
doi: "10.1109/SCW63240.2024.00017"
arxiv: ""
score: 3.8
essence: "과학 분야에서 사용되는 대규모 언어모델(LLM)의 신뢰성을 평가하기 위한 포괄적 프레임워크 SciTrust를 제시한다. 다중 평가 방식(객관식 벤치마크, 오픈엔드형 질문, LLM 기반 판정자)을 결합하여 진실성, 환각(hallucination), 아첨(sycophancy) 측면에서 다섯 가지 LLM의 성능을 비교 분석했다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Cognitive_LLM_Evaluation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Herron et al._2024_SciTrust Evaluating the Trustworthiness of Large Language Models for Science.pdf"
---

# SciTrust: Evaluating the Trustworthiness of Large Language Models for Science

> **저자**: Emily Herron, Junqi Yin, Feiyi Wang | **날짜**: 2024-01 | **DOI**: [10.1109/SCW63240.2024.00017](https://doi.org/10.1109/SCW63240.2024.00017)

---

## Essence

과학 분야에서 사용되는 대규모 언어모델(LLM)의 신뢰성을 평가하기 위한 포괄적 프레임워크 SciTrust를 제시한다. 다중 평가 방식(객관식 벤치마크, 오픈엔드형 질문, LLM 기반 판정자)을 결합하여 진실성, 환각(hallucination), 아첨(sycophancy) 측면에서 다섯 가지 LLM의 성능을 비교 분석했다.

## Motivation

- **Known**: LLM은 자연어 처리에 혁신을 가져왔으나 과학 분야 적용 시 신뢰성 문제(부정확성, 환각, 논리적 오류, 아첨 경향)를 야기
- **Gap**: 기존 연구는 일반적 LLM 신뢰성만 다루거나 과학적 추론 능력에만 초점을 두며, 과학 LLM의 신뢰성을 체계적으로 평가하는 포괄적 프레임워크 부재
- **Why**: 과학 발견 과정(가설 형성, 아이디어 생성, 동료 검토)에서 LLM 활용 증가에 따라 신뢰성 평가의 필요성 대두
- **Approach**: 진실성의 네 가지 관점(오정보 저항, 논리적 추론, 환각 저항, 아첨 저항)에서 과학 LLM을 평가하는 다층적 프레임워크 구축

## Achievement

1. **포괄적 평가 프레임워크 개발**: 객관식 벤치마크(SciQ, GPQA-Diamond, ARC-C, MMLU)와 신규 오픈엔드형 데이터셋(컴퓨터과학, 화학, 생물학, 물리학 각 500개 질문)을 통합한 SciTrust 프레임워크 구축

2. **다양한 평가 메트릭 도입**: ROUGE, BERT 점수(의미론적 유사성), BART 점수, GPT-4o 판정자 기반 평가를 결합하여 자동화된 오픈엔드형 질문 평가 최초 시도

3. **모델 성능 비교 분석**: 
   - Llama3-70B-Instruct가 전반적으로 우수한 성능(MMLU 과학 영역 평균 64.5%)
   - 과학 특화 모델 중 Galactica-120B가 최고 성능(MMLU 평균 41.6%)
   - Darwin-7B는 모든 벤치마크에서 극히 저조한 성능(대부분 1% 이하)

4. **고성능 컴퓨팅 확장성 평가**: Frontier 엑사스케일 슈퍼컴퓨터와 H100 테스트베드에서 다중 선택형 및 오픈엔드형 추론의 지연시간 측정 및 비교

## How

- **오정보 저항 평가**: 기존 과학 벤치마크와 GPT-4o를 이용한 논문 기반 신규 질문-답변 쌍 생성
- **질문 생성 전략**: Semantic Scholar API를 활용하여 2005년 이후 인용 500회 이상 저널 논문 필터링으로 고품질 과학 데이터셀 확보
- **출력 평가 방법**: 
  - 객관식: 정확 일치(exact match) 검증
  - 오픈엔드형: 어휘적(ROUGE-1, ROUGE-L), 의미적(BERT, BART) 유사성 + LLM 판정자 점수(0-10) 종합
- **추론 설정**: 객관식 최대 3토큰, 오픈엔드형 최대 300토큰, 각 프롬프트당 4회 반복 출력
- **프롬프트 설계**: 0-shot, 2-shot 데모를 포함한 명확한 프롬프트 형식 표준화

## Originality

- **신규 벤치마크**: 고인용도 저널 논문 기반 오픈엔드형 과학 데이터셋 4개(총 2,000개 질문) 신규 구성
- **통합 평가 메트릭**: 어휘, 의미, LLM 기반 판정을 통합한 최초의 자동화된 오픈엔드형 평가 체계
- **과학 특화 평가 프레임워크**: 기존 일반적 LLM 신뢰성 연구를 과학 도메인에 특화하여 확장
- **공개 제공**: 프레임워크, 스크립트, 데이터셋 전체를 GitHub에 공개하여 재현성 및 활용성 확보

## Limitation & Further Study

- **한계**:
  - 오픈엔드형 질문 평가에서 GPT-4o 점수와 ROUGE/BERT 점수 간 불일치(FORGE-L이 의미론적 메트릭에서는 높지만 GPT-4o 점수는 낮음) → 평가 메트릭의 신뢰성 검증 필요
  - Darwin-7B의 극저조 성능으로 인해 과학 특화 모델들 간 충분한 비교 분석 제한
  - 논리적 추론, 환각, 아첨 저항 평가는 프레임워크에 포함되었으나 본문에서 결과 미제시
  - 고성능 컴퓨팅 성능 평가 결과 미제시

- **후속 연구**:
  - LLM 판정자와 인간 평가 간 상관관계 검증
  - 환각, 논리적 추론, 아첨 저항에 대한 정량적 결과 제공
  - 더 많은 과학 특화 모델(최신 SciLLM 포함) 평가
  - 과학 도메인별 신뢰성 차이의 근본 원인 분석
  - 모델의견 보정(calibration) 및 신뢰성 개선 방안 탐구

## Evaluation

- **Novelty**: 4/5
  - 과학 도메인 특화 신뢰성 평가는 신규이나, 개별 평가 방법론들은 기존 연구 활용

- **Technical Soundness**: 3.5/5
  - 평가 설계는 타당하나 다중 메트릭 간 불일치(의미론적 vs LLM 판정) 해결 미흡
  - 논리적 추론, 환각, 아첨 평가의 구체적 방법론 결여

- **Significance**: 4/5
  - 과학 LLM의 신뢰성 평가를 위한 포괄적 기초 제공
  - 공개 자료로 인한 높은 재현성과 활용성

- **Clarity**: 3.5/5
  - 프레임워크 설명은 명확하나 일부 핵심 결과(논리, 환각, 아첨) 미제시
  - 표 형식의 복잡성으로 인한 가독성 저하

- **Overall**: 3.8/5

**총평**: SciTrust는 과학 도메인에 특화된 LLM 신뢰성 평가의 중요한 기초를 마련하였으며, 공개된 벤치마크와 평가 프레임워크의 가치가 높다. 다만 평가 메트릭 간의 불일치 해결과 모든 신뢰성 측면에 대한 정량적 결과 제시가 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/124_Automated_justification_production_for_claim_veracity_in_fac/review]] — 과학 분야 LLM의 환각과 편향 문제가 팩트체킹 시스템의 정당화 생성에서 신뢰할 수 있는 판단 근거 제시의 기반이 된다.
- 🔄 다른 접근: [[papers/388_GPT-4o_System_Card/review]] — 과학 분야 LLM 신뢰성 평가와 GPT-4o 안전성 평가가 동일한 신뢰성 목표를 가지지만 평가 도메인과 방법이 다르다.
- 🔗 후속 연구: [[papers/846_TrustLLM_Trustworthiness_in_Large_Language_Models/review]] — 대규모 언어모델의 전반적인 신뢰성 평가를 과학 분야에 특화하여 구체적으로 확장한 사례이다.
- 🔄 다른 접근: [[papers/846_TrustLLM_Trustworthiness_in_Large_Language_Models/review]] — 과학 분야 LLM 신뢰성 평가의 다른 접근법과 벤치마크 제시
- 🔗 후속 연구: [[papers/124_Automated_justification_production_for_claim_veracity_in_fac/review]] — 과학 분야 LLM의 신뢰성 평가에서 환각과 편향을 다루는 것이 팩트체킹의 정당화 생성과 직접 연결된다.
- 🔄 다른 접근: [[papers/388_GPT-4o_System_Card/review]] — GPT-4o의 안전성 평가와 SciTrust의 과학 분야 LLM 신뢰성 평가가 동일한 평가 목표를 가지지만 다른 도메인과 방법론을 사용한다.
