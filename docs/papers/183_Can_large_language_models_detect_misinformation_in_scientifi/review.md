---
title: "183_Can_large_language_models_detect_misinformation_in_scientifi"
authors:
  - "Yupeng Cao"
  - "Aishwarya Muralidharan Nair"
  - "Nastaran Jamalipour Soofi"
  - "Elyon Eyimife"
  - "K.P. Subbalakshmi"
date: "2024"
doi: "arXiv:2402.14268"
arxiv: ""
score: 4.25
essence: "과학 뉴스 기사의 오보(misinformation)를 탐지하기 위해 대규모 언어모델(LLM)의 능력을 평가하고, 과학적 타당성 차원(Dimensions of Validity, DoV)을 정의하여 prompt engineering을 통해 미명시적 주장(explicit claim) 없이도 오보를 검출할 수 있는 세 가지 아키텍처를 제안한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Automated_News_Verification"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Angelis et al._2024_Can large language models detect misinformation in scientific news reporting arXiv preprint arXiv2.pdf"
---

# Can large language models detect misinformation in scientific news reporting? arXiv preprint arXiv:2402.14268, 2024.

> **저자**: Yupeng Cao, Aishwarya Muralidharan Nair, Nastaran Jamalipour Soofi, Elyon Eyimife, K.P. Subbalakshmi | **날짜**: 2024 | **DOI**: [arXiv:2402.14268](https://arxiv.org/abs/2402.14268)

---

## Essence

과학 뉴스 기사의 오보(misinformation)를 탐지하기 위해 대규모 언어모델(LLM)의 능력을 평가하고, 과학적 타당성 차원(Dimensions of Validity, DoV)을 정의하여 prompt engineering을 통해 미명시적 주장(explicit claim) 없이도 오보를 검출할 수 있는 세 가지 아키텍처를 제안한다.

## Motivation

- **Known**: 기존의 과학 fact-checking 방법들은 인간이 뉴스에서 명시적 주장(claim)을 추출해야 하는 번거로운 과정이 필요하며, LLM이 생성한 거짓 정보의 증가로 인해 과학 도메인의 오보 탐지가 더욱 복잡해지고 있음
- **Gap**: 1) 과학 뉴스의 타당성을 정의하는 일반화된 분류체계(taxonomy) 부재, 2) 현실적 시나리오에서 명시적 주장 추출 없이 작동하는 아키텍처 부재, 3) LLM 생성 콘텐츠 혼합 데이터셋 부재
- **Why**: 과학 정보는 비전문가에게 뉴스와 소셜미디어로 전파되므로, 오보의 공중보건 피해가 심각하고(COVID-19, 백신 거부 등), 수동 fact-checking의 확장성 한계
- **Approach**: CoSMis 데이터셋 구축(인간 작성+LLM 생성), DoV 가이드 Chain-of-Thought prompting, 3가지 파이프라인 아키텍처(SERIf, SIf, D2I) 비교 평가

## Achievement

![Figure 1](figures/fig1.webp) *데이터셋 구축 프로세스: 공개 데이터셋, 웹 리소스, LLM 기반 생성을 통한 균형잡힌 코퍼스 수집*

1. **CoSMis(SciNews) 데이터셋 개발**: 2,400개의 COVID-19 관련 뉴스(신뢰 1,200개, 부신뢰 1,200개)와 CORD-19 과학 초록 페어링. 인간 작성(1,200개)과 LLM 생성(1,200개) 균형 포함으로 실제 시나리오 반영

2. **과학적 타당성 차원(DoV) 정의**: 과학 뉴스의 오보를 다차원으로 평가하는 프레임워크 제시

3. **3가지 LLM 파이프라인**: SERIf(Summarization-Evidence Retrieval-Inference), SIf(Evidence Retrieval 제외), D2I(Direct-to-Inference) 아키텍처로 점진적 처리 단계 감소 설계

4. **설명가능성 제공**: DoV 기반 Chain-of-Thought prompting으로 모델 의사결정 과정의 해석 가능성 확보

## How

![Figure 3](figures/fig3.webp) *제안된 3가지 아키텍처: SERIf는 요약→증거 검색→추론의 3단계, SIf는 2단계, D2I는 직접 추론으로 진행*

**방법론**:
- **데이터셋 구축**: MM-CoVaR, COVID19-FNIR, COVID-Rumor 등 공개 데이터셋 활용 + 웹 스크래핑 + 과학 키워드 필터링 + 수동 검증 + LLM 기반 신뢰/불신뢰 뉴스 생성
- **DoV 프레임워크**: 과학적 정확성, 맥락 적절성, 출처 인용, 불확실성 표현 등 다차원 평가 기준 설정
- **Prompt Engineering**: Zero-shot, Few-shot, DoV-guided Chain-of-Thought 전략 적용
- **모델 평가**: GPT-3.5, GPT-4, Llama2(7B/13B/70B), Llama3(8B) 비교 테스트
- **아키텍처 비교**: 각 파이프라인의 처리 단계 차이에 따른 성능 변화 분석

## Originality

- **Novel Dataset**: 인간 작성과 LLM 생성 콘텐츠의 균형잡힌 혼합으로, 현실의 혼합 오보 생태계 반영
- **Taxonomy Creation**: 과학 오보를 체계적으로 분류하는 DoV 차원 정의 - 기존 연구에서 부재했던 개념적 틀 제시
- **No Explicit Claim Requirement**: 명시적 주장 추출 없이 직접 비교 가능한 아키텍처 제안으로 실용성 향상
- **Explainability Focus**: DoV 기반 CoT prompting으로 '왜 오보인가'에 대한 설명 제공 메커니즘 구축
- **Comprehensive Architecture Comparison**: 3가지 복잡도 수준의 파이프라인 비교로 처리 단계의 영향 분석

## Limitation & Further Study

- **데이터셋 제한**: COVID-19 특화 데이터로 다른 과학 도메인(기후, 물리학 등)으로의 일반화 가능성 미검증
- **LLM 의존성**: GPT-3.5/4의 API 비용 문제와 오픈소스 모델(Llama)과의 성능 격차 존재
- **평가 메트릭**: 정확도 기반 평가만 제시, 부분적 오류(partial misinformation)나 문제사항의 심각도 구분 부족
- **사람-모델 비교 부재**: 인간 평가자(과학자, 기자)와 LLM 성능의 직접 비교 필요
- **후속 연구**: 1) 다학제 과학 도메인 확장, 2) Fine-tuning 기반 성능 개선 탐색, 3) 실시간 뉴스 스트림 적용, 4) 멀티모달(이미지+텍스트) 오보 탐지

## Evaluation

- **Novelty**: 4.5/5 - DoV 프레임워크와 LLM 생성 콘텐츠 혼합 데이터셋이 창의적이나, 아키텍처 자체는 비교적 표준적
- **Technical Soundness**: 4/5 - 방법론 타당하나, 평가 과정의 철저성과 통계적 유의성 검증 상세 부족
- **Significance**: 4.5/5 - 실제 과학 오보 탐지 문제의 실용적 해결책 제시하며, 데이터셋 공개로 커뮤니티 기여도 높음
- **Clarity**: 4/5 - 전반적으로 명확하나, DoV 정의와 아키텍처 세부사항 설명이 더 상세할 수 있음
- **Overall**: 4.25/5

**총평**: 이 논문은 과학 뉴스의 오보 탐지 문제를 현대적 관점에서 접근하여 실용적 데이터셋과 명시적 주장 추출이 필요 없는 LLM 파이프라인을 제안했으나, 다중 도메인 일반화와 더 정밀한 평가 프로토콜을 통해 임팩트를 극대화할 수 있는 추가 연구가 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/859_Unsupervised_pretraining_for_fact_verification_by_language_m/review]] — 과학 뉴스의 오보 탐지를 위한 타당성 차원 정의가 SFAVEL의 클레임-근거 의미론적 정렬 학습의 이론적 기반을 제공함
- 🔗 후속 연구: [[papers/880_What_makes_medical_claims_un_verifiable_analyzing_entity_and/review]] — 의료 클레임의 검증 가능성 분석이 과학 뉴스 오보 탐지에서 사용된 과학적 타당성 평가 방법론을 의료 영역으로 확장한 연구임
- 🔄 다른 접근: [[papers/267_Defame_Dynamic_evidencebased_fact-checking_with_multimodal_e/review]] — DEFAME의 멀티모달 동적 증거 기반 접근법이 과학 뉴스 오보 탐지의 텍스트 기반 타당성 평가와 상호 보완적인 검증 방법을 제시함
