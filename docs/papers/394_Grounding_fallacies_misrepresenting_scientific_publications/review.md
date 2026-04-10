---
title: "394_Grounding_fallacies_misrepresenting_scientific_publications"
authors:
  - "Max Glockner"
  - "Yufang Hou"
  - "Preslav Nakov"
  - "Iryna Gurevych"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "건강 관련 허위정보는 신뢰할 수 있는 생의학 논문을 증거로 잘못 인용하며, 논리적 오류(logical fallacy)를 적용하여 거짓 주장을 지원하는 것처럼 보이게 한다. 본 논문은 실제 학술지 구절에 기반하여 이러한 오류를 탐지하고 설명하기 위해 MISSCIPLUS 데이터셋을 제시한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Fact_Verification_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Glockner et al._2024_Grounding fallacies misrepresenting scientific publications in evidence.pdf"
---

# Grounding fallacies misrepresenting scientific publications in evidence

> **저자**: Max Glockner, Yufang Hou, Preslav Nakov, Iryna Gurevych | **날짜**: 2024 | **DOI**: N/A

---

## Essence

건강 관련 허위정보는 신뢰할 수 있는 생의학 논문을 증거로 잘못 인용하며, 논리적 오류(logical fallacy)를 적용하여 거짓 주장을 지원하는 것처럼 보이게 한다. 본 논문은 실제 학술지 구절에 기반하여 이러한 오류를 탐지하고 설명하기 위해 MISSCIPLUS 데이터셋을 제시한다.

## Motivation

- **Known**: 기존 MISSCI 데이터셋은 단순화되고 의역된 짧은 구절(paraphrased phrases)을 증거로 사용하여 허위정보를 탐지함. 기존 논리적 오류 탐지 연구는 명시적으로 표현된 오류를 가정하며, 표면 수준의 오류에 집중함.

- **Gap**: 실제 상황에서는 모델이 전체 논문에서 관련 구절을 먼저 찾아야 하고, 복잡한 과학 텍스트를 기반으로 논리적 오류를 추론해야 함. MISSCI의 단순화된 맥락은 실세계 적용성이 제한적.

- **Why**: 자동 사실 검증(AFC) 모델은 실제로 잘못 대표되는 과학 논문의 구절을 입력으로 받으므로, 이를 평가할 수 있는 현실적인 데이터셋이 필요함.

- **Approach**: MISSCI의 2,257개 의역된 구절을 실제 논문의 구절과 수동 주석으로 연결(grounding)하여 MISSCIPLUS 데이터셋을 구축.

## Achievement

![Figure 1](figures/fig1.webp)
*Figure 1: MISSCI의 의역된 맥락을 실제 논문 구절과 연결. LLM은 (i) 원본 논문에서 관련 구절을 찾고 (ii) 거짓 주장을 지원하기 위한 논리적 오류를 생성해야 함*

1. **현실적 데이터셋 구축**: 허위정보 주장과 실제 학술지 구절을 쌍으로 연결한 최초의 논리적 오류 데이터셋 제시. AFC 모델이 사용하는 입력과 동일한 형태로 구성.

2. **포괄적 벤치마킹**: 
   - 구절 검색 모델의 성능 평가 (정확한 증거 구절 선택)
   - LLM의 논리적 오류 재구성 능력 평가 (단순화된 내용 vs. 원본 텍스트)
   - AFC 모델의 허위정보 탐지 성능 평가

## How

![Figure 2](figures/fig2.webp)
*Figure 2: 실제 논문 구절 (Vincent et al., 2005)이 MISSCI의 의역된 내용 "연구는 세포 배양을 사용함"과 어떻게 연결되는지 보여줌*

- **데이터 수집**: PMC(PubMed Central)에서 이용 가능한 100개 논문 기반 118개의 논리적 오류 argument 선택

- **구절 연결**: 
  - 정확한 전제(accurate premise, p₀)를 지원하는 구절 S⁰ⱼ 식별
  - 논리적 오류를 드러내는 출판 맥락(publication context, sᵢ)에 해당하는 추가 구절 검색
  - 구절이 의역된 정보를 함축(entail)하면 연결

- **세부 과제 분해**:
  1. 주장이 기반한 구절 S⁰ⱼ 검색 (정확한 전제)
  2. 논리적 오류 탐지에 필요한 모든 구절 Sⱼ 검색 (출판 맥락)
  3. 실제 구절을 사용한 argument 재구성

- **모델 평가**:
  - 검색 방법: 어휘 기반(lexical), 의미 기반(semantic) 유사성 모델
  - LLM: 원본 구절 기반 오류 재구성 성능
  - AFC 모델: 잘못 표현된 증거를 사용한 허위정보 탐지

## Originality

- **최초의 접지된 논리적 오류 데이터셋**: 실제 과학 논문 구절과 허위정보 주장을 연결한 최초 데이터셋으로, 다른 오류 탐지 연구와 차별화

- **AFC와 오류 탐지의 교량**: 과학적 사실 검증과 논리적 오류 탐지를 결합하여 새로운 연구 방향 제시

- **현실주의적 설정**: 단순화된 입력이 아닌 전체 논문에서 관련 구절을 검색해야 하는 현실적 조건 구성

- **다층적 평가**: 구절 검색, 오류 재구성, 사실 검증의 세 가지 관점에서 모델 성능 체계적 평가

## Limitation & Further Study

- **오라클 입력 가정**: 각 세부 과제에서 이전 단계의 완벽한 성능을 가정하므로, 실제 파이프라인에서는 오류 전파 문제 발생 가능

- **제한된 데이터셋 규모**: 118개의 argument와 100개의 논문은 대규모 언어모델 학습에 충분하지 않을 수 있음

- **특정 도메인 (건강 관련)**: 다른 분야(정치, 기술 등)의 허위정보로의 일반화 가능성 미검증

- **후속 연구**:
  - 엔드-투-엔드 오류 전파를 고려한 통합 모델 개발
  - 다른 도메인으로의 확장 및 데이터셋 규모 확대
  - 더 정교한 검색 알고리즘 (예: 그래프 기반, 구조적 추론)
  - 모델이 잘못된 주장을 거부하지 못하는 이유에 대한 심층 분석


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4.5/5
- Overall: 4.2/5

**총평**: 본 논문은 허위정보 탐지의 실제 적용을 위해 논리적 오류를 실제 과학 논문과 연결한 혁신적인 데이터셋을 제시하며, 기존 AFC 모델과 LLM이 오류가 있는 증거를 효과적으로 활용하지 못함을 실증적으로 보여줌으로써 향후 연구 방향을 제시한다.

## Related Papers

- 🔗 후속 연구: [[papers/827_Towards_effective_extraction_and_evaluation_of_factual_claim/review]] — 일반적인 팩트체킹에서 과학 출판물 오용을 탐지하는 특화된 도메인으로 확장하여 더 구체적인 문제를 다룸
- 🔄 다른 접근: [[papers/332_Fact-checking_complex_claims_with_program-guided_reasoning/review]] — 둘 다 복잡한 사실 검증을 다루지만 하나는 과학 논문 오용, 다른 하나는 일반적 복잡한 주장에 중점을 둠
- 🏛 기반 연구: [[papers/460_Language_models_surface_the_unwritten_code_of_science_and_so/review]] — 과학과 사회의 암묵적 편향을 드러내는 연구가 과학 출판물을 잘못 인용하는 논리적 오류 탐지의 맥락을 제공함
- 🔗 후속 연구: [[papers/460_Language_models_surface_the_unwritten_code_of_science_and_so/review]] — 과학과 사회의 암묵적 편향을 드러내는 일반적 접근을 과학 출판물 오용 탐지라는 구체적 응용으로 확장함
- 🏛 기반 연구: [[papers/827_Towards_effective_extraction_and_evaluation_of_factual_claim/review]] — 과학 출판물 오용에 대한 구체적 연구가 일반적인 주장 추출과 평가 프레임워크 개발의 실제적 동기를 제공함
